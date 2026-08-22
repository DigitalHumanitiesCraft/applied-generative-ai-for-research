---
title: Sources
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
related: [project, specification, state, schema, operations]
---

# Sources

The register of the material this book is written from. It names each source, where its original came from, at which state it was taken, and what it feeds. The processing state of each source, meaning whether it is ingested and distilled, is generated from the file state into the source inventory of [[knowledge/state]] and is not repeated here. The rules that decide what a source is and how it is anchored are in [[knowledge/schema]].

The register carries texts under the source type `document`, because the project holds the rights to all of them and their full text may therefore be stored in the vault and anchored by block reference. The source type `publication` is active for the research literature the book cites through the paper and the lecture notes, and its records enter `references/` as CSL JSON when the first such citation is grounded. The source type `data` is inactive.

## Feeding artefacts

| Source | Vault path | Origin | Repository | Commit | Retrieved |
|---|---|---|---|---|---|
| Promptotyping paper, version 0.9 | `00_sources/promptotyping-paper.md`, `10_markdown/documents/promptotyping-paper.md` | `research-artefacts/promptotyping-paper.md` | DigitalHumanitiesCraft/Promptotyping | bf0c848a5c0ebf4a7fa320f114721afe1b648df2 | 2026-08-22 |
| Full Lecture Notes, English | `00_sources/lecture-notes-en.md`, `10_markdown/documents/lecture-notes-en.md` | `script/full-lecture-notes-en.md` | DigitalHumanitiesCraft/knowledge-context-agentic-engineering | 5c0e9d66bc9a169a0c184742bfe247fc232c7439 | 2026-08-22 |
| Full Lecture Notes, German | `00_sources/lecture-notes-de.md`, `10_markdown/documents/lecture-notes-de.md` | `script/full-lecture-notes-de.md` | DigitalHumanitiesCraft/knowledge-context-agentic-engineering | 5c0e9d66bc9a169a0c184742bfe247fc232c7439 | 2026-08-22 |
| Full Slide Deck, slide-text export | `00_sources/slide-deck.md`, `10_markdown/documents/slide-deck.md` | `slides/full-slide-deck.md` | DigitalHumanitiesCraft/knowledge-context-agentic-engineering | 5c0e9d66bc9a169a0c184742bfe247fc232c7439 | 2026-08-22 |
| Vault als materialisiertes Wissensmodell | `00_sources/vault-as-materialised-knowledge-model.md`, `10_markdown/documents/vault-as-materialised-knowledge-model.md` | `Vault Operations/Theorie/Vault als materialisiertes Wissensmodell.md` | private Obsidian vault of the author, no public remote | 4bb3192228146e4e3db45621e7abf0cb5367f998 | 2026-08-22 |
| Promptotyping Document Templates | `00_sources/promptotyping-document-templates.md`, `10_markdown/documents/promptotyping-document-templates.md` | `_content/promptotyping-document/` | DigitalHumanitiesCraft/Promptotyping | 6a5cfa46a767a8443908aeecbbf44831f3aea277 | 2026-08-22 |

Both source repositories were clean at the commit named above when the copies were taken, so the file in `00_sources/` is the committed state and not a working-tree variant.

## What each source feeds

The binding assignment of sources to parts is the feeding map in [[knowledge/project]]. This section resolves the shorthand of that map onto the registered files.

- *script chapter N* is chapter N of the German Full Lecture Notes, whose numbered subsections carry the chapter through. The English Full Lecture Notes hold the same material under prose headings without numbers, so a passage of the English version is located by its heading and a passage of the German version by its section number.
- *paper chapter N* is section N of the Promptotyping paper, which numbers its sections 1 to 4 with subsections. The Project Knowledge Base named for Part II is section 2.1.
- *slide section* names a run of slides in the deck export, located by the slide title. The export carries no heading structure of its own.
- *hands-on chains* are the sections 3.8, 4.6, 5.8, 6.7 and 7.11 of the German Full Lecture Notes together with the slides that accompany them.
- *Promptotyping templates* is the template set of `_content/promptotyping-document/`, entered as one source. The folder holds seventeen templates at the commit named in the register, where the note that preceded the ingest said eighteen. A single template is located inside the source by its heading, which carries the file name of the template it reproduces.

## Sources named by the feeding map and not yet ingested

- **Research literature.** The publications the paper and the lecture notes cite. They enter as `publication` sources with a CSL JSON record in `references/` at the point where an assertion needs one of them directly rather than through the paper.

## Rights

The two source repositories are public. The Promptotyping repository carries the MIT licence, and the teaching repository licenses its text content under CC BY 4.0 while checking slide images separately for third-party image rights. The licence of each source stands in the `metadata` block of its Markdown representation.

The vault document is the author's own writing and came from a private Obsidian vault that carries no licence statement. Its full text is committed here and becomes public with this repository, which is a publication decision that stands until the operator revises it. Its licence field records the gap.

## Conversion

The originals are Markdown, so the ingest converted nothing and only stamped a block ID onto every anchor-relevant line. The template set is the one source assembled rather than copied. Its original is the seventeen template files concatenated in the functional order of the index template, each under a heading that names its file and its template version, with the headings of each template demoted by two levels so that the assembled file carries one hierarchy. The template texts themselves are unchanged. One effect is worth knowing when a slide passage is quoted. The slide-text export carries vertical tab characters as soft line breaks inside a slide, and the stamping turned each of them into an ordinary line break, so the representation of the deck holds more lines than its original. The wording is unchanged.
