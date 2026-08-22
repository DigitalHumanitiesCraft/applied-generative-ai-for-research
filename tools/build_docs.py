"""Render the bilingual manuscript in 40_output/ into the static reading view in docs/.

Data flow: every chapter file of `40_output/en/` and `40_output/de/` is read, its YAML
frontmatter parsed, its Markdown body converted to HTML, and the result written to
`docs/<lang>/<slug>.html`. `docs/index.html` carries the book title and the part and
chapter navigation of both language routes. `docs/.nojekyll` is written so that GitHub
Pages serves the folder unprocessed.

The generator writes HTML only. The stylesheet, the script and the brand assets under
`docs/assets/` are hand-maintained and are never touched by a run, so a rebuild can
never lose them.

The Markdown subset covers what a chapter of this vault uses: headings, paragraphs,
lists, tables, blockquotes, fenced code, inline code, bold, italic, ordinary links,
wikilinks, footnote markers with their definitions, and trailing block IDs. Complete
CommonMark coverage is deliberately out of scope.

Two conversions are load-bearing for the vault. A trailing block ID (` ^p0007`) becomes
the `id` of the element it closes, so a provenance link into a chapter passage resolves
in the published page. A footnote marker becomes a link into the notes section of the
same page, because the anchor contract of the output layer rests on those markers.

The generation date is a required argument rather than the system date, so that a
rebuild of an older state stays reproducible.

Usage: python tools/build_docs.py --date 2026-08-22
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

# The citable form of both strings stands in CITATION.cff; the split into title and
# subtitle is a presentation decision of this page and lives here.
BOOK_TITLE = "Applied Generative AI for Research"
BOOK_SUBTITLE = "Knowledge, Context, Agents, and Verifiable Research Artefacts"

SITE_URL = "https://digitalhumanitiescraft.github.io/applied-generative-ai-for-research/"
REPOSITORY_URL = (
    "https://github.com/DigitalHumanitiesCraft/applied-generative-ai-for-research"
)
PUBLISHER_URL = "https://dhcraft.org"

LANGS = ("en", "de")
OTHER = {"en": "de", "de": "en"}

# Interface text of both routes. A reader of the German route reads German chrome, and
# the language switch is labelled in the language it leads to.
UI = {
    "en": {
        "route": "English",
        "route_other": "Deutsch",
        "skip": "Skip to the text",
        "contents": "Contents",
        "previous": "Previous",
        "next": "Next",
        "chapter": "Chapter",
        "notes": "Notes",
        "back_to_text": "Back to the text",
        "language": "Language",
        "chapters": "Chapters",
        "state": "Writing state",
        "generated": f"Generated from the manuscript of the {BOOK_TITLE} repository, state of",
        "switch_hint": "Read this chapter in German",
        "licence": "Manuscript text CC BY 4.0, code MIT",
        "status": {
            "skeleton": "Skeleton",
            "drafted": "Draft",
            "written": "Written",
        },
    },
    "de": {
        "route": "Deutsch",
        "route_other": "English",
        "skip": "Zum Text springen",
        "contents": "Inhalt",
        "previous": "Zurück",
        "next": "Weiter",
        "chapter": "Kapitel",
        "notes": "Anmerkungen",
        "back_to_text": "Zurück zum Text",
        "language": "Sprache",
        "chapters": "Kapitel",
        "state": "Schreibstand",
        "generated": f"Erzeugt aus dem Manuskript des Repositoriums {BOOK_TITLE}, Stand",
        "switch_hint": "Dieses Kapitel auf Englisch lesen",
        "licence": "Manuskripttext CC BY 4.0, Code MIT",
        "status": {
            "skeleton": "Skelett",
            "drafted": "Entwurf",
            "written": "Geschrieben",
        },
    },
}

_FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
_CODE_SPAN = re.compile(r"`([^`]+)`")
_WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
_FOOTNOTE_REF = re.compile(r"\[\^([^\]\s]+)\]")
_FOOTNOTE_DEF = re.compile(r"^\[\^([^\]\s]+)\]:\s?(.*)$")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC = re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_ITEM = re.compile(r"^(\s*)([-*]|\d+[.)])\s+(.*)$")
_TABLE_RULE = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
_BLOCK_ID = re.compile(r"\s+\^([A-Za-z0-9][A-Za-z0-9-]*)\s*$")
_NON_SLUG = re.compile(r"[^a-z0-9]+")


@dataclass(frozen=True)
class Chapter:
    """One chapter file of one language route, as the page generator needs it."""

    lang: str
    slug: str
    part: str
    number: object
    title: str
    writing_status: str
    body: tuple[str, ...]


def _slugify(text: str) -> str:
    return _NON_SLUG.sub("-", text.lower()).strip("-") or "section"


def _unique(candidate: str, seen: set[str]) -> str:
    """A page-unique id, because a duplicate id breaks anchor resolution."""
    name = candidate
    suffix = 2
    while name in seen:
        name = f"{candidate}-{suffix}"
        suffix += 1
    seen.add(name)
    return name


def _split_anchor(text: str) -> tuple[str, str | None]:
    """Separate a trailing block ID from the text of the block it closes."""
    match = _BLOCK_ID.search(text)
    if match is None:
        return text, None
    return text[: match.start()].rstrip(), match.group(1)


def _attr(anchor: str | None) -> str:
    return f' id="{html.escape(anchor, quote=True)}"' if anchor else ""


def _footnote_ref(key: str, seen: set[str] | None) -> str:
    """A marker in the text. A chapter may cite the same note more than once, so the
    element id is made unique and the back link of the note leads to the first use."""
    ident = f"fnref-{key}" if seen is None else _unique(f"fnref-{key}", seen)
    return (
        f'<sup class="fn-ref" id="{html.escape(ident, quote=True)}">'
        f'<a href="#fn-{html.escape(key, quote=True)}">{html.escape(key)}</a></sup>'
    )


def _inline(text: str, seen: set[str] | None = None) -> str:
    """Convert inline Markdown, keeping code spans free of further markup."""
    parts = _CODE_SPAN.split(text)
    out = []
    for index, part in enumerate(parts):
        if index % 2:
            out.append(f"<code>{html.escape(part)}</code>")
            continue
        piece = html.escape(part)
        piece = _WIKILINK.sub(lambda m: f"<code>{m.group(1)}</code>", piece)
        piece = _FOOTNOTE_REF.sub(lambda m: _footnote_ref(m.group(1), seen), piece)
        piece = _LINK.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', piece)
        piece = _BOLD.sub(r"<strong>\1</strong>", piece)
        piece = _ITALIC.sub(r"<em>\1</em>", piece)
        out.append(piece)
    return "".join(out)


def _starts_block(line: str) -> bool:
    stripped = line.lstrip()
    return (
        not stripped
        or stripped.startswith(("```", ">", "|"))
        or bool(_HEADING.match(line))
        or bool(_ITEM.match(line))
    )


def _split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _dedent(lines: list[str]) -> list[str]:
    indents = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
    cut = min(indents) if indents else 0
    return [line[cut:] if line.strip() else "" for line in lines]


def _render_fence(lines: list[str], start: int) -> tuple[str, int]:
    index = start + 1
    body = []
    while index < len(lines) and not lines[index].lstrip().startswith("```"):
        body.append(lines[index])
        index += 1
    code = html.escape("\n".join(_dedent(body)))
    return f"<pre><code>{code}</code></pre>", index + 1


def _render_table(lines: list[str], start: int, seen: set[str]) -> tuple[str, int]:
    header = _split_row(lines[start])
    index = start + 2
    rows = []
    while index < len(lines) and lines[index].lstrip().startswith("|"):
        rows.append(_split_row(lines[index]))
        index += 1
    head = "".join(f"<th>{_inline(cell, seen)}</th>" for cell in header)
    body = "".join(
        "<tr>" + "".join(f"<td>{_inline(cell, seen)}</td>" for cell in row) + "</tr>"
        for row in rows
    )
    table = f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"
    return f'<div class="scroll">{table}</div>', index


def _render_quote(lines: list[str], start: int, seen: set[str]) -> tuple[str, int]:
    index = start
    body = []
    while index < len(lines) and lines[index].lstrip().startswith(">"):
        body.append(lines[index].lstrip()[1:].removeprefix(" "))
        index += 1
    return f"<blockquote>{_render_blocks(body, seen)}</blockquote>", index


def _render_item(buffer: list[str], seen: set[str]) -> str:
    text, anchor = _split_anchor(buffer[0].strip())
    first = _inline(text, seen)
    rest = _dedent(buffer[1:])
    inner = _render_blocks(rest, seen) if any(line.strip() for line in rest) else ""
    ident = _attr(_unique(anchor, seen)) if anchor else ""
    return f"<li{ident}>{first}{inner}</li>"


def _render_list(lines: list[str], start: int, seen: set[str]) -> tuple[str, int]:
    match = _ITEM.match(lines[start])
    if match is None:
        raise ValueError(f"not a list item: {lines[start]!r}")
    base = len(match.group(1))
    ordered = match.group(2)[0].isdigit()
    index = start
    items: list[str] = []
    buffer: list[str] = []
    while index < len(lines):
        line = lines[index]
        item = _ITEM.match(line)
        indent = len(line) - len(line.lstrip())
        if item and indent == base:
            if buffer:
                items.append(_render_item(buffer, seen))
            buffer = [item.group(3)]
        elif not line.strip():
            # A blank line ends the list unless an indented continuation or a
            # further item at the same level follows (loose list).
            following = next((x for x in lines[index + 1 :] if x.strip()), "")
            following_indent = len(following) - len(following.lstrip())
            continues = following_indent > base or (
                following_indent == base and _ITEM.match(following)
            )
            if not following or not continues:
                break
            buffer.append("")
        elif indent > base and buffer:
            buffer.append(line)
        else:
            break
        index += 1
    if buffer:
        items.append(_render_item(buffer, seen))
    tag = "ol" if ordered else "ul"
    return f"<{tag}>{''.join(items)}</{tag}>", index


def _render_blocks(lines: list[str], seen: set[str] | None = None) -> str:
    seen = set() if seen is None else seen
    out: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
        elif line.lstrip().startswith("```"):
            block, index = _render_fence(lines, index)
            out.append(block)
        elif heading := _HEADING.match(line):
            level = min(len(heading.group(1)), 6)
            text, anchor = _split_anchor(heading.group(2))
            ident = _unique(anchor or _slugify(text), seen)
            out.append(f"<h{level}{_attr(ident)}>{_inline(text, seen)}</h{level}>")
            index += 1
        elif (
            line.lstrip().startswith("|")
            and index + 1 < len(lines)
            and _TABLE_RULE.match(lines[index + 1])
        ):
            block, index = _render_table(lines, index, seen)
            out.append(block)
        elif line.lstrip().startswith(">"):
            block, index = _render_quote(lines, index, seen)
            out.append(block)
        elif _ITEM.match(line):
            block, index = _render_list(lines, index, seen)
            out.append(block)
        else:
            paragraph = [line.strip()]
            index += 1
            while index < len(lines) and not _starts_block(lines[index]):
                paragraph.append(lines[index].strip())
                index += 1
            text, anchor = _split_anchor(" ".join(paragraph))
            ident = _attr(_unique(anchor, seen)) if anchor else ""
            out.append(f"<p{ident}>{_inline(text, seen)}</p>")
    return "".join(out)


_DANGLING = re.compile(
    r'<sup class="fn-ref" id="([^"]+)"><a href="#fn-([^"]+)">([^<]*)</a></sup>'
)


def _unlink_undefined(rendered: str, defined: set[str]) -> str:
    """Leave a marker whose note is missing as plain text.

    A chapter under revision can carry a marker before its definition exists, and a
    link into a note that is not on the page would resolve nowhere. The defect itself
    is reported by `tools/validate.py`, which is where it belongs.
    """

    def keep(match: re.Match[str]) -> str:
        if match.group(2) in defined:
            return match.group(0)
        return f'<sup class="fn-ref" id="{match.group(1)}">{match.group(3)}</sup>'

    return _DANGLING.sub(keep, rendered)


def _split_footnotes(lines: list[str]) -> tuple[list[str], list[tuple[str, str]]]:
    """Separate footnote definitions from the running text they belong to."""
    text: list[str] = []
    notes: list[tuple[str, str]] = []
    index = 0
    while index < len(lines):
        match = _FOOTNOTE_DEF.match(lines[index])
        if match is None:
            text.append(lines[index])
            index += 1
            continue
        parts = [match.group(2).strip()]
        index += 1
        while index < len(lines) and lines[index][:1].isspace() and lines[index].strip():
            parts.append(lines[index].strip())
            index += 1
        notes.append((match.group(1), " ".join(parts).strip()))
    return text, notes


def _normalise_headings(lines: list[str]) -> list[str]:
    """Drop the document H1 and shift the remaining headings so the shallowest is H2.

    The page carries the chapter title from the frontmatter as its H1, so the H1 of the
    file would duplicate it, and a chapter whose top-level sections are written as H3
    would otherwise produce a heading order that skips a level.
    """
    out: list[str] = []
    seen_title = False
    levels: list[int] = []
    for line in lines:
        heading = _HEADING.match(line)
        if heading and len(heading.group(1)) == 1 and not seen_title:
            seen_title = True
            continue
        if heading:
            levels.append(len(heading.group(1)))
        out.append(line)
    shift = 2 - min(levels) if levels else 0
    if shift == 0:
        return out
    shifted: list[str] = []
    for line in out:
        heading = _HEADING.match(line)
        if heading is None:
            shifted.append(line)
            continue
        level = max(2, min(len(heading.group(1)) + shift, 6))
        shifted.append(f"{'#' * level} {heading.group(2)}")
    return shifted


def _read_chapter(path: Path, lang: str) -> Chapter | None:
    """One chapter file, or None when the file carries no usable frontmatter."""
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = _FRONTMATTER.match(text)
    if match is None:
        return None
    try:
        fm = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None
    body = _normalise_headings(text[match.end() :].split("\n"))
    return Chapter(
        lang=lang,
        slug=path.stem,
        part=str(fm.get("part") or "").strip(),
        number=fm.get("chapter"),
        title=str(fm.get("title") or path.stem).strip(),
        writing_status=str(fm.get("writing-status") or "").strip(),
        body=tuple(body),
    )


def chapters(root: Path, lang: str) -> list[Chapter]:
    """The chapters of one language route, in the reading order the slugs give."""
    folder = root / "40_output" / lang
    if not folder.is_dir():
        return []
    found = [_read_chapter(path, lang) for path in sorted(folder.glob("*.md"))]
    return [chapter for chapter in found if chapter is not None]


def _runs(items: list[Chapter]) -> list[tuple[str, list[Chapter]]]:
    """Group consecutive chapters by their part, so a part that frames the book at both
    ends (introduction and conclusion) keeps its two positions instead of collapsing."""
    grouped: list[tuple[str, list[Chapter]]] = []
    for chapter in items:
        if grouped and grouped[-1][0] == chapter.part:
            grouped[-1][1].append(chapter)
        else:
            grouped.append((chapter.part, [chapter]))
    return grouped


def _status_badge(chapter: Chapter, lang: str) -> str:
    label = UI[lang]["status"].get(chapter.writing_status, chapter.writing_status)
    if not label:
        return ""
    return (
        f'<span class="status" data-status="{html.escape(chapter.writing_status, quote=True)}">'
        f"{html.escape(label)}</span>"
    )


def _page(lang: str, title: str, prefix: str, description: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description, quote=True)}">
<link rel="icon" type="image/png" href="{prefix}assets/favicon-32.png">
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
{body}<script src="{prefix}assets/app.js" defer></script>
</body>
</html>
"""


def _footer(lang: str, prefix: str, date: str) -> str:
    ui = UI[lang]
    return f"""<footer class="site-footer">
<div class="shell">
<a class="colophon-mark" href="{PUBLISHER_URL}">
<img src="{prefix}assets/dhcraft-logo-watercolor.png" alt="Digital Humanities Craft" width="1600" height="1203">
</a>
<p class="colophon-note">{html.escape(ui["generated"])} {html.escape(date)}.
<a href="{REPOSITORY_URL}">Repository</a>.</p>
<p class="colophon-note">{html.escape(ui["licence"])}.</p>
</div>
</footer>
"""


def _toc(items: list[Chapter], lang: str) -> str:
    ui = UI[lang]
    parts = []
    for part, group in _runs(items):
        entries = []
        for chapter in group:
            number = "" if chapter.number is None else str(chapter.number)
            label = (
                f'<span class="toc-number">{html.escape(number)}</span>' if number else ""
            )
            entries.append(
                f'<li class="toc-entry">{label}'
                f'<a href="{lang}/{chapter.slug}.html">{html.escape(chapter.title)}</a>'
                f"{_status_badge(chapter, lang)}</li>"
            )
        heading = html.escape(part) if part else ui["chapters"]
        parts.append(
            f'<section class="toc-part">\n<h3>{heading}</h3>\n'
            f'<ul class="toc-list">{"".join(entries)}</ul>\n</section>'
        )
    return "\n".join(parts)


def build_index(routes: dict[str, list[Chapter]], date: str) -> str:
    """The landing page, carrying the book title and both language routes."""
    sections = []
    for lang in LANGS:
        items = routes.get(lang) or []
        if not items:
            continue
        sections.append(
            f'<section class="route" id="route-{lang}" lang="{lang}" data-lang="{lang}">\n'
            f'<h2>{html.escape(UI[lang]["route"])}</h2>\n{_toc(items, lang)}\n</section>'
        )
    routes_html = "\n".join(sections)
    body = f"""<a class="skip-link" href="#routes">{html.escape(UI["en"]["skip"])}</a>
<header class="masthead">
<div class="shell">
<p class="masthead-kicker">Digital Humanities Craft</p>
<h1>{html.escape(BOOK_TITLE)}</h1>
<p class="masthead-subtitle">{html.escape(BOOK_SUBTITLE)}</p>
</div>
</header>
<main class="shell" id="routes">
<div class="route-filter" id="route-filter" hidden></div>
{routes_html}
</main>
{_footer("en", "", date)}"""
    return _page(
        "en",
        f"{BOOK_TITLE}. {BOOK_SUBTITLE}",
        "",
        "The bilingual manuscript of the book, one page per chapter, English and German.",
        body,
    )


def build_chapter_page(
    chapter: Chapter,
    previous: Chapter | None,
    following: Chapter | None,
    mirrored: bool,
    date: str,
) -> str:
    """One chapter page, with its language switch, its pager and its notes."""
    ui = UI[chapter.lang]
    other = OTHER[chapter.lang]
    text, notes = _split_footnotes(list(chapter.body))
    seen: set[str] = set()
    rendered = _unlink_undefined(_render_blocks(text, seen), {key for key, _ in notes})
    if notes:
        entries = "".join(
            f'<li id="fn-{html.escape(key, quote=True)}">{_inline(value)} '
            f'<a class="fn-back" href="#fnref-{html.escape(key, quote=True)}" '
            f'aria-label="{html.escape(ui["back_to_text"], quote=True)}">&#8617;</a></li>'
            for key, value in notes
        )
        rendered += (
            f'<section class="notes" aria-labelledby="notes-heading">'
            f'<h2 id="notes-heading">{html.escape(ui["notes"])}</h2>'
            f"<ol>{entries}</ol></section>"
        )

    if mirrored:
        switch = (
            f'<a class="route-switch" href="../{other}/{chapter.slug}.html" '
            f'hreflang="{other}" lang="{other}" data-lang="{other}" '
            f'title="{html.escape(ui["switch_hint"], quote=True)}">'
            f'{html.escape(ui["route_other"])}</a>'
        )
    else:
        switch = (
            f'<span class="route-switch is-absent" lang="{other}">'
            f'{html.escape(ui["route_other"])}</span>'
        )

    pager = []
    if previous is not None:
        pager.append(
            f'<a class="pager-previous" rel="prev" href="{previous.slug}.html">'
            f'<span class="pager-label">{html.escape(ui["previous"])}</span>'
            f"<span>{html.escape(previous.title)}</span></a>"
        )
    if following is not None:
        pager.append(
            f'<a class="pager-next" rel="next" href="{following.slug}.html">'
            f'<span class="pager-label">{html.escape(ui["next"])}</span>'
            f"<span>{html.escape(following.title)}</span></a>"
        )

    number = "" if chapter.number is None else f'{ui["chapter"]} {chapter.number}'
    meta = [f'<span class="chapter-number">{html.escape(number)}</span>'] if number else []
    badge = _status_badge(chapter, chapter.lang)
    if badge:
        meta.append(badge)

    body = f"""<a class="skip-link" href="#text">{html.escape(ui["skip"])}</a>
<header class="site-header">
<div class="shell">
<a class="site-title" href="../index.html">{html.escape(BOOK_TITLE)}</a>
<nav class="header-nav" aria-label="{html.escape(ui["language"], quote=True)}">
<a class="header-link" href="../index.html">{html.escape(ui["contents"])}</a>
{switch}
</nav>
</div>
</header>
<main class="shell" id="text">
<article class="chapter" lang="{chapter.lang}">
<p class="chapter-part">{html.escape(chapter.part)}</p>
<h1>{html.escape(chapter.title)}</h1>
<p class="chapter-meta">{"".join(meta)}</p>
{rendered}
</article>
<nav class="pager" aria-label="{html.escape(ui["chapters"], quote=True)}">
{"".join(pager)}
</nav>
</main>
{_footer(chapter.lang, "../", date)}"""
    return _page(
        chapter.lang,
        f"{chapter.title}. {BOOK_TITLE}",
        "../",
        f"{chapter.part}. {chapter.title}.",
        body,
    )


def build_site(root: Path, output: Path, date: str) -> list[Path]:
    """Write the whole reading view and return the files the run produced."""
    routes = {lang: chapters(root, lang) for lang in LANGS}
    if not any(routes.values()):
        raise FileNotFoundError(f"no chapter files under {root / '40_output'}")

    written: list[Path] = []
    output.mkdir(parents=True, exist_ok=True)
    nojekyll = output / ".nojekyll"
    nojekyll.write_text("", encoding="utf-8")
    written.append(nojekyll)

    index = output / "index.html"
    index.write_text(build_index(routes, date), encoding="utf-8")
    written.append(index)

    for lang, items in routes.items():
        if not items:
            continue
        folder = output / lang
        folder.mkdir(parents=True, exist_ok=True)
        mirror = {chapter.slug for chapter in routes.get(OTHER[lang]) or []}
        for position, chapter in enumerate(items):
            page = folder / f"{chapter.slug}.html"
            page.write_text(
                build_chapter_page(
                    chapter,
                    items[position - 1] if position else None,
                    items[position + 1] if position + 1 < len(items) else None,
                    chapter.slug in mirror,
                    date,
                ),
                encoding="utf-8",
            )
            written.append(page)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--date", required=True, help="generation date, ISO 8601")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="vault root (default: the repository this script lives in)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="target folder (default: <root>/docs)",
    )
    args = parser.parse_args()

    root: Path = args.root.resolve()
    output: Path = args.output or root / "docs"
    try:
        written = build_site(root, output, args.date)
    except FileNotFoundError as error:
        print(f"FEHLER: {error}", file=sys.stderr)
        return 1
    print(f"OK: {output} ({len(written)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
