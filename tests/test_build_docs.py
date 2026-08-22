"""Tests for tools/build_docs.py against a temporary two-chapter manuscript.

The generator reads the real output layer, so the subject here is a minimal vault built
in a temporary folder: one skeleton chapter and one drafted chapter, mirrored in both
language routes. The drafted chapter carries the two features the vault depends on, a
trailing block ID and a footnote with its definition.
"""

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).parents[1]
sys.path.insert(0, str(REPO / "tools"))

from build_docs import BOOK_TITLE, build_site, chapters  # noqa: E402

SKELETON = """---
type: chapter
status: grounded
writing-status: skeleton
lang: {lang}
part: Frame
chapter: 0
title: "{title}"
---

# {title}

{lead}

### A section written one level too deep
"""

DRAFTED = """---
type: chapter
status: grounded
writing-status: drafted
lang: {lang}
part: "{part}"
chapter: 1
title: "{title}"
assertions: ["[[30_assertions/metering-reduces-use]]"]
posits: 0
---

# {title}

Water use fell by a third after metering was introduced.[^1] ^p0007

[^1]: Grounded in [[30_assertions/metering-reduces-use]].
"""

TEXT = {
    "en": {
        "intro": "Research after the Prompt",
        "chapter": "What Large Language Models Are",
        "part": "I. Generative Models as Research Systems",
        "lead": "The introduction states the question of the book.",
    },
    "de": {
        "intro": "Forschung nach dem Prompt",
        "chapter": "Was große Sprachmodelle sind",
        "part": "I. Generative Modelle als Forschungssysteme",
        "lead": "Die Einleitung stellt die Frage des Buches.",
    },
}


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    for lang, text in TEXT.items():
        folder = tmp_path / "40_output" / lang
        folder.mkdir(parents=True)
        (folder / "00-research-after-the-prompt.md").write_text(
            SKELETON.format(lang=lang, title=text["intro"], lead=text["lead"]),
            encoding="utf-8",
        )
        (folder / "01-what-large-language-models-are.md").write_text(
            DRAFTED.format(lang=lang, title=text["chapter"], part=text["part"]),
            encoding="utf-8",
        )
    return tmp_path


@pytest.fixture
def site(vault: Path, tmp_path: Path) -> Path:
    output = tmp_path / "docs"
    build_site(vault, output, "2026-08-22")
    return output


def test_a_chapter_file_yields_its_frontmatter(vault: Path) -> None:
    first, second = chapters(vault, "en")
    assert (first.slug, first.part, first.writing_status) == (
        "00-research-after-the-prompt",
        "Frame",
        "skeleton",
    )
    assert (second.title, second.number, second.writing_status) == (
        "What Large Language Models Are",
        1,
        "drafted",
    )


def test_the_run_writes_both_routes_and_the_pages_switch(site: Path) -> None:
    assert (site / ".nojekyll").is_file()
    for lang in ("en", "de"):
        assert (site / lang / "00-research-after-the-prompt.html").is_file()
        assert (site / lang / "01-what-large-language-models-are.html").is_file()
    english = (site / "en" / "01-what-large-language-models-are.html").read_text("utf-8")
    assert 'href="../de/01-what-large-language-models-are.html"' in english
    assert 'hreflang="de"' in english


def test_the_landing_page_carries_the_title_and_both_routes(site: Path) -> None:
    page = (site / "index.html").read_text(encoding="utf-8")
    assert BOOK_TITLE in page
    assert 'id="route-en"' in page and 'id="route-de"' in page
    assert "I. Generative Models as Research Systems" in page
    assert "I. Generative Modelle als Forschungssysteme" in page
    assert 'href="en/00-research-after-the-prompt.html"' in page
    assert 'href="de/01-what-large-language-models-are.html"' in page


def test_a_skeleton_chapter_renders_with_its_state_and_a_sound_heading_order(
    site: Path,
) -> None:
    page = (site / "en" / "00-research-after-the-prompt.html").read_text(encoding="utf-8")
    assert '<span class="status" data-status="skeleton">Skeleton</span>' in page
    assert "<h1>Research after the Prompt</h1>" in page
    assert "The introduction states the question of the book." in page
    # The H1 of the file is dropped and the lone H3 becomes the first H2.
    assert page.count("<h1>") == 1
    assert "<h3" not in page
    assert '<h2 id="a-section-written-one-level-too-deep">' in page


def test_a_drafted_chapter_keeps_its_block_anchor_and_resolves_its_footnote(
    site: Path,
) -> None:
    page = (site / "en" / "01-what-large-language-models-are.html").read_text(
        encoding="utf-8"
    )
    assert '<span class="status" data-status="drafted">Draft</span>' in page
    assert '<p id="p0007">' in page
    assert "^p0007" not in page
    assert '<sup class="fn-ref" id="fnref-1"><a href="#fn-1">1</a></sup>' in page
    assert '<li id="fn-1">Grounded in <code>30_assertions/metering-reduces-use</code>' in page
    assert "[^1]:" not in page


def test_a_marker_without_a_definition_renders_without_a_dead_link(
    vault: Path, tmp_path: Path
) -> None:
    chapter = vault / "40_output" / "en" / "01-what-large-language-models-are.md"
    chapter.write_text(
        chapter.read_text(encoding="utf-8").replace(
            "[^1]: Grounded in [[30_assertions/metering-reduces-use]].", ""
        ),
        encoding="utf-8",
    )
    output = tmp_path / "docs-mid-revision"
    build_site(vault, output, "2026-08-22")
    page = (output / "en" / "01-what-large-language-models-are.html").read_text("utf-8")
    assert '<sup class="fn-ref" id="fnref-1">1</sup>' in page
    assert 'href="#fn-1"' not in page


def test_the_german_route_carries_german_interface_text(site: Path) -> None:
    page = (site / "de" / "01-what-large-language-models-are.html").read_text(
        encoding="utf-8"
    )
    assert '<html lang="de">' in page
    assert ">Entwurf<" in page
    assert ">Anmerkungen<" in page
    assert ">Inhalt<" in page
    assert 'href="../en/01-what-large-language-models-are.html"' in page


def test_an_empty_output_layer_fails_rather_than_writing_an_empty_site(
    tmp_path: Path,
) -> None:
    with pytest.raises(FileNotFoundError):
        build_site(tmp_path, tmp_path / "docs", "2026-08-22")
