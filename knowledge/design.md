---
title: Design
project:
  name: "Applied Generative AI for Research"
  repository: "DigitalHumanitiesCraft/applied-generative-ai-for-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
template:
  name: Vorlage Design
  version: 0.2
  url: https://dhcraft.org/Promptotyping/promptotyping-document/design
status: draft
language: en
created: "2026-08-22"
updated: "2026-08-22"
related: [specification, project, state, journal]
---

# Design

The reading view publishes a scholarly book manuscript while it is being written. It is a reading surface with one column, a serif running text and chrome that stays quiet, and it keeps its distance from the documentation-site look with a permanent sidebar, a search field and a dense navigation tree. The two language versions of the manuscript are equal routes through the same book, and the writing state of every chapter is legible before the reader opens it.

## Design stance

Reading is the purpose of the surface, so the measure of the text column, the leading and the vertical rhythm carry the design and everything else defers to them. The typographic tradition it stands in is the printed scholarly book, and the interface elements it borrows from the web stay at the edges of the page.

The manuscript is published in an unfinished state, which the surface shows rather than conceals. A chapter whose text is still the seed from the outline is labelled a skeleton, a chapter under revision a draft. A reader who could not see that distinction would take a seed text for finished prose, and the vault's own separation of grounding from evidence would lose its counterpart in the published form.

Provenance survives the conversion to HTML. A block ID in the chapter text becomes the element id of the passage it closes, so a link that names a passage resolves in the published page as it resolves in the repository. A footnote marker resolves inside the page to its note, because the anchor contract of the output layer rests on those markers.

The two languages are mirrored routes with the same slug per chapter, and neither is presented as an appendix of the other. The German route carries German interface text, the English route English.

The page is readable without JavaScript and makes no request outside its own folder. No font file, no stylesheet and no script is loaded from a third-party host, which keeps the published book free of the tracking that a font or script CDN introduces and keeps it archivable as a folder of files.

## Design system

Tokens. Colour, typography, spacing, the reading measure and the corner radius are declared as custom properties in the token block of `docs/assets/style.css`, and no literal value stands below that block. The colour set holds a page ground, a raised ground, text and muted text, a rule, an accent with a quiet variant, the light plate the brand mark sits on, and one colour per writing state. The dark scheme is a swap of the same token names under `prefers-color-scheme: dark`, so the scheme follows the reader's system setting and needs no control on the page.

Typography. A serif family carries the running text, a sans family the chrome and the tabular elements, a monospace family the code and the wikilinked anchors. The families are system stacks, so the page loads no font file. The sizes run on a fluid scale built with `clamp()`, which lets the type grow with the viewport without a breakpoint.

Components. The surface has few of them, and each is a class in the same stylesheet. The landing page carries the masthead and the table of contents, whose entry holds the chapter number, the title and the state badge. A chapter page carries the site header with the contents link and the language switch, the chapter head with its part and state, the running text, the notes section and the pager. Every page carries the colophon.

Layout. One centred column at the reading measure, with a gutter that grows with the viewport. Responsive behaviour needs a single narrow breakpoint below the measure, where the header stacks, the table of contents entry drops from three columns to two and the pager runs vertically. Wide viewports need no second column, because a reading column that grows past its measure reads worse.

Mark. The coloured watercolour logo of Digital Humanities Craft is the default mark and stands in the colophon of every page; the monochrome invert mark is not used. The file is `dhcraft_logo_watercolor+text_web.png` from the brand repository `DigitalHumanitiesCraft/brand-assets`, stored as `docs/assets/dhcraft-logo-watercolor.png`. The artwork is raster with a white ground baked into it and its transparent master is far too large for a repository asset, so the mark sits on a light plate in both schemes, which reads as a printed logo on paper. The tab icon is the watercolour favicon from the same repository.

## Interaction patterns

Navigation runs on links alone. The landing page lists both routes part by part, and every chapter of a route is reachable from it in one step. A chapter page leads back to the contents, across to the mirrored chapter of the other language, and forward or back to its neighbour in the same route.

The language switch leads to the same chapter under the same slug in the other route. Where a mirror is missing, the label stands without a link rather than leading nowhere.

The landing page shows both routes when JavaScript is off. With JavaScript a filter appears above them and holds the chosen route, and a chapter page records the language it is written in, so the landing page opens on the route the reader last read in. The stored preference is a convenience of the reader's browser and changes nothing about what the page contains.

The state badge carries its label as text and uses colour only in addition, so the distinction survives a monochrome display and a reader who does not separate the hues.

Anchors are stable. Every heading has an id from its block ID or from its slug, every passage that carries a block ID keeps it as its element id, and a footnote marker used more than once keeps its own id per occurrence while the note leads back to the first use.

Assistive use is carried by the structure. Every page opens with a skip link, uses the landmark elements, marks the current language on the elements that carry text of another language, exposes the pressed state of the filter buttons, and keeps a visible focus outline.

## Generation and routes

GitHub Pages serves one folder, so the reading view is generated rather than assembled by hand. `tools/build_docs.py` reads `40_output/en/*.md` and `40_output/de/*.md`, converts each chapter and writes `docs/index.html`, `docs/en/<slug>.html`, `docs/de/<slug>.html` and `docs/.nojekyll`. The conversion from Markdown to HTML uses the standard library and the small converter that already lived in the script, so the repository gained no third-party dependency. The generator writes HTML only, and the stylesheet, the script and the brand assets under `docs/assets/` are hand-maintained and are never touched by a run. The generation date is an argument of the run rather than the system date, which keeps a rebuild of an older state reproducible. The decision and its alternatives are recorded in [[knowledge/specification]].

The published address is `https://dhcraft.org/applied-generative-ai-for-research/`, the custom domain of the organisation, to which the `github.io` address of the repository redirects. The Pages setting on the `docs/` folder of the default branch and the custom domain are repository settings and belong to the operator.

The book has no German title yet, so the masthead carries the English title on both routes and the German route is labelled by its language. A German title enters here and in the generator once the manuscript carries one.

## Connection to the action layer

`CLAUDE.md` in the repository root names this document as binding for the reading view and names `tools/build_docs.py` as the generator to run after a chapter milestone. The imperative translation of the stance above still belongs there under a heading for the design principles, in the form of a few sentences derived from this document. Two examples of what would stand there are that the writing state of a chapter is always rendered as a visible label, and that a block ID in the chapter text is always carried into the generated page as an element id. This document holds the declarative form and carries no imperatives of its own.
