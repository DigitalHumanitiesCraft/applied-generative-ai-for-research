---
title: Specification
project:
  name: "Applied Generative AI for Research"
  repository: "DigitalHumanitiesCraft/applied-generative-ai-for-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-08-22"
updated: "2026-08-22"
related: [index, project, plan, schema, operations, outline, sources]
---

# Specification

Purpose, parameters and settled decisions of this vault instance. The invariant architecture (layer model, anchor mechanics, check contracts, status progression) lives in [[knowledge/schema]] and [[knowledge/operations]]; this document holds what this project decided.

## Purpose

This vault produces the book manuscript *Applied Generative AI for Research. Knowledge, Context, Agents, and Verifiable Research Artefacts*, a bilingual scholarly synthesis on the controlled use of generative models and agentic systems in research. Its readers are researchers and research-support staff who work with structured research data and want to know how model-supported work can be organised without transferring evidential responsibility to the systems that perform it. The evidence obligation is that every substantive claim of the manuscript resolves to a passage in one of the feeding artefacts registered in [[knowledge/sources]] or in a further source entered there, through the anchor chain the schema defines. The book therefore applies the Grounded Vault method to its own genesis, and the manuscript is the audit object of the argument it makes.

## Parameters

| Parameter | Value |
|---|---|
| Controlled topic set | Generative-Models, Grounded-Knowledge, Agentic-Work, Promptotyping, Research-Artefacts, Boundaries-and-Implications <!-- becomes the MOC set in 30_assertions/ --> |
| Active source types | `document` and `publication`; `data` inactive <!-- document, publication, data --> |
| Output genre | scholarly synthesis, book manuscript <!-- strategy, proposal, report, scholarly synthesis --> |
| Chapter register | see [[knowledge/state]] |
| Working language of content | English leads for output, assertions and distillates; German is a complete parallel output version |
| Verification role | the author as Critical Expert, Digital Humanities Craft <!-- role and institution --> |
| Validation mechanism | `tools/validate.py` |
| Machine review mechanism | a reviewer model from a different family than the producing agent, to be fixed by the operator; until then a fresh-context review by a separate Claude agent through `tools/review.py`, marked as same-family in every finding <!-- reviewer model and pairing tooling --> |

The six topics of the controlled topic set are the six parts of the manuscript, so that an assertion is filed where the argument uses it. The parts are named in [[knowledge/outline]] and the mapping of parts to topics is one to one.

### Bilingual output

The template assumes a single working language of content. This instance keeps the single language at the distillate and assertion layers, where English is the only language, and extends the output layer alone. `40_output/en/` holds the English manuscript and `40_output/de/` the German parallel version, one file per chapter under the same slug in both folders. The validator reads `40_output/` recursively and judges a chapter by its frontmatter, so the two subfolders need no change to the invariant mechanics. A German chapter carries the same `assertions` mirror as its English counterpart, because both express the same grounded statements. German titles of the skeleton are working titles until the German version is written.

## Style sheet

The register is matter-of-fact scholarly prose. Technical terms stay English in the German version, so that *Context Engineering*, *Grounded Vault*, *Promptotyping* and *Critical Expert* read the same in both.

The following rules bind every chapter.

- No en dash and no em dash, and no colon as a connector, for emphasis, or before an inline list. A colon stands only before a quotation, a code block, or a list whose items are set on their own lines. The en dash stays available in numeric and alphanumeric ranges, which is notation.
- Never the trailing negative apposition in the pattern "X, not Y" or "not X, but Y". The point is stated positively and the excluded alternative, where it matters, gets its own sentence.
- No triadic figures as a stylistic device and no parallelism used as rhetoric. An antithesis is admissible where it carries content.
- No paragraph engineered towards a closing aphorism and no closing platitude at the end of a chapter.
- No filler, no hollow intensifiers, no meta-announcements of the chapter's own approach.
- Citations are displayed as the schema prescribes. Every load-bearing sentence carries a footnote marker whose definition begins with `Grounded in` and names its assertions by wikilink; every own conclusion carries a footnote beginning with `Posit:` and states its open evidence question. The frontmatter mirrors the referenced assertions and counts the posits.

## Settled decisions

<!-- One line per decision with date; the reasoning behind each lives in the journal. -->

- 2026-08-22: Vault instantiated from the Grounded Vault template (`DigitalHumanitiesCraft/grounded-vault` at 767edbc).
- 2026-08-22: The book is published from its own public repository, and a reading view on GitHub Pages is prepared by a later lane. No venue is pursued.
- 2026-08-22: English leads and German is a complete parallel version; the bilingual split lives in the output layer alone.
- 2026-08-22: The controlled topic set is the six parts of the manuscript.
- 2026-08-22: `data` stays an inactive source type until a source enters that is anchored by computation.
- 2026-08-22: Licences are split, CC BY 4.0 for manuscript text and documentation, MIT for code and tooling.
- 2026-08-22: The reading view is a generated static site under `docs/`, produced by `tools/build_docs.py`; the section below holds the decision.

## Reading view

GitHub Pages serves one folder, and the manuscript lives in two others. A deterministic generator therefore renders `40_output/en/*.md` and `40_output/de/*.md` together with the navigation into `docs/` as static HTML, and the result is committed and re-run at milestones. Publishing the Markdown for a client-side renderer was rejected, because a page that assembles the book in the browser makes the published text depend on a script and stops resolving a passage anchor without one. A build step in continuous integration was rejected as well, because the repository has no build regime and a committed `docs/` keeps the published state readable in the same diff as the manuscript that produced it.

The generator is `tools/build_docs.py`, the page generator the template shipped, rewritten around the chapter as its subject and keeping the Markdown converter it already carried. It writes `docs/index.html` with the book title and the part and chapter navigation of both routes, one page per chapter at `docs/en/<slug>.html` and `docs/de/<slug>.html`, and `docs/.nojekyll`. Its test is `tests/test_build_docs.py`, which renders a skeleton chapter and a drafted chapter in both languages and checks the language switch, the writing-state badge, the heading order, the block anchor and the footnote.

Four properties are binding for the output. The pages are static HTML with no external dependency, so nothing is fetched from a third-party host at read time. The text is readable with JavaScript switched off, and the script does no more than remember the language route and offer a filter on the landing page. The Markdown conversion uses the standard library and the converter inside the generator, so no third-party package entered `pyproject.toml`. A block ID in the chapter text becomes the element id of the passage it closes, so a later provenance link into a chapter passage resolves in the published page.

The stylesheet, the script and the brand assets under `docs/assets/` are hand-maintained and are never written by a run, so a rebuild cannot lose them. The design of the surface is described in [[knowledge/design]]. The published address is `https://dhcraft.org/applied-generative-ai-for-research/`; the Pages setting on the `docs/` folder and the custom domain are repository settings and belong to the operator.
