---
title: Journal
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
related: [specification, state]
---

# Journal

Chronological decision history of the vault, append-only, newest entry last. Content documents carry only current state; the reasoning that led there lives here. An entry records a decision, a rejected alternative with the reason, or a calibration result of a check mechanism.

## Entry format

```markdown
## 2026-08-22 — <one-line subject>

<What was decided or found, why, and what it replaces. Link the affected
documents. Two to ten sentences.>
```

## 2026-08-22 — Vault instantiated

Instantiated from the Grounded Vault template, `DigitalHumanitiesCraft/grounded-vault` at commit 767edbc, by extracting the committed state of that repository rather than its working tree, which carried uncommitted changes at the time. The class B decisions are recorded in [[knowledge/specification]]; the sub-goals, the feeding map and the revisable settings are in [[knowledge/project]]. Three things were added beyond what the template ships, each because the template's own split rule applies. [[knowledge/project]] carries the charter function, which the template folds into the specification and which this project needs separately because the feeding map changes on a different rhythm than the parameters. [[knowledge/plan]] carries the forward work of the four lanes. [[knowledge/sources]] carries the source register with provenance and rights, which the generated source inventory in [[knowledge/state]] cannot hold, because that inventory is derived from the file state and knows nothing about where a file came from. [[knowledge/handoff]] and [[knowledge/outline]] follow from the Promptotyping document convention and from the need to keep the canonical outline inside the repository.

## 2026-08-22 — The bilingual output lives in the output layer alone

The template assumes one working language of content. English leads and German is a complete parallel version, so the split had to go somewhere. It went into `40_output/en/` and `40_output/de/`, one file per chapter under the same slug, and nowhere else. Distillates and assertions stay English, because a bilingual assertion layer would double every anchor without adding a distinction that the sources make. A German chapter therefore carries the same `assertions` mirror as its English counterpart. The validator reads `40_output/` recursively and judges a chapter by its frontmatter, so the two subfolders needed no change to the invariant mechanics. The alternative of two separate vaults was rejected, because it would split the assertion layer that both versions rest on.

## 2026-08-22 — A skeleton chapter carries a second status field

The template's chapter status is the grounding ladder, `grounded` to `validated` to `verified`, and the validator rejects any other value. A chapter that exists only as a title and a description sits below that ladder, and `SETUP.md` asks for a chapter register whose rows start at a writing status of `planned` while `knowledge/state.md` says the register mirrors the chapter's frontmatter, which has no such field. The instance resolves this with a separate `writing-status` field on the chapter, running `skeleton` to `drafted` to `written`, beside the untouched `status: grounded`. The register mirrors the new field. This is the smallest addition that keeps the validator green and keeps the two ladders apart; the alternative of overloading `status` would have made a formal check impossible.

## 2026-08-22 — Five feeding sources ingested, one conversion effect recorded

The Promptotyping paper, both Full Lecture Notes, the slide-text export and the vault document "Vault als materialisiertes Wissensmodell" entered as `document` sources with their originals in `00_sources/` and their Markdown representations in `10_markdown/documents/`. All five originals are Markdown, so the ingest converted nothing and only stamped a block ID onto every anchor-relevant line, deterministically and sequentially per file. One effect is recorded in [[knowledge/sources]] because it changes the line count of a representation against its original. The slide-text export carries vertical tab characters as soft line breaks inside a slide, and the stamping turned each of them into an ordinary line break. The wording is unchanged and the originals are committed beside the representations, so the effect is checkable.

## 2026-08-22 — The template's docs folder was removed

`SETUP.md` permits an instance to delete `docs/`, and this instance did. The folder held the architecture page of the template, which describes the Grounded Vault rather than this book, and a published book repository that carries a page about a different repository misleads its readers. `docs/` is now free for the reading view that lane U4 builds. `tools/build_docs.py` stays in place because it is a working static-page generator that the reading-view lane may reuse, and the harness block of `CLAUDE.md` records that it currently has no subject.

## 2026-08-22 — The reading view is generated into docs and committed

GitHub Pages serves one folder and the manuscript lives in two, so a deterministic generator renders both language routes into `docs/` as static HTML, which is committed and re-run at milestones. Two alternatives were rejected. Publishing the Markdown for a client-side renderer would make the published text depend on a script and would stop a passage anchor resolving without one. A build step in continuous integration would add a build regime the repository does not otherwise have and would take the published state out of the diff that carries the manuscript producing it. `tools/build_docs.py` was rewritten around the chapter as its subject and kept the Markdown converter it already carried, so the reading view added no third-party dependency; its test renders a skeleton chapter and a drafted chapter in both languages. The design of the surface is in [[knowledge/design]] and the decision in [[knowledge/specification]].

Three things follow from the vault's own contracts. A trailing block ID becomes the element id of the passage it closes, so a provenance link into a chapter resolves in the published page. A footnote marker links to its note inside the same page, and a marker whose definition is missing is rendered as plain text, because the manuscript is published while it is being written and a link into a note that does not exist would resolve nowhere; `tools/validate.py` reports that defect where it belongs. The `writing-status` of every chapter is shown as a labelled badge, so a reader cannot mistake a seed text for finished prose.

Two decisions wait on someone else. Enabling Pages on the `docs/` folder is a repository setting and belongs to the operator, and the expected address `https://digitalhumanitiescraft.github.io/applied-generative-ai-for-research/` is recorded in the README and in the design document without any setting being touched. The book has no German title, so the masthead carries the English title on both routes until the manuscript supplies one.

## 2026-08-22 — Parts IV to VI written from the paper and the template set

The Promptotyping document templates entered as one source rather than as one source per template, which closes the open question [[knowledge/plan]] carried. The templates form one set with one origin, one commit and one licence, the book cites them as a set, and block IDs already give the anchor granularity that seventeen registrations would have bought at the price of seventeen rows of bookkeeping. The folder holds seventeen templates and not the eighteen the earlier note assumed, which [[knowledge/sources]] now records. Its original is assembled rather than copied, in the functional order of the index template and with each template's headings demoted by two levels, and that assembly is described in the conversion section of the register so a reader can rebuild it. The assembled original stays out of version control under the existing ignore rule for `00_sources/`, unlike the five originals of the first ingest, which are tracked; the Markdown representation carries the full text either way, so nothing is lost, and the inconsistency in the source layer is a finding for the operator rather than something this lane resolved on its own.

Assertions partition their grounding. Each distillate statement supports exactly one assertion, so no grounding set is contained in another and `W-DUPLICATE-GROUNDING` stays silent inside a chapter scope, where a warning fails the run. The rule cost nothing in this material, because the two sources overlap only on the document set, and it forces a decision that would otherwise stay implicit, namely which single statement a claim actually rests on. All one hundred and eighty-one statements of the two distillates are grounded in.

Two things about the chapter files are conventions this lane set rather than rules the schema states. Each chapter ends with a gap list under its own heading, written as a heading-led block, which keeps it outside the paragraph check of the anchor contract because it is apparatus about the chapter's own state rather than a claim about the world. And the outline reaches past the sources in several places, so those passages carry posits with their open evidence question instead of being written as if grounded. The recurring cases are enumerations the expose supplies where the paper argues in prose, the term for the critique of tool positivism, the audit interface as a fifth interface type, the definition of reconstructability, and the composition of a handover package.

Where the outline and the paper describe the same matter differently, the chapters follow the paper and say so. The four forms of assessment are the paper's deterministic verification, agentic review, Critical Expert verification and scholarly validation, and the operational and visual inspection the outline lists as a fourth form is treated as a mode of examination shared across them, because the four are distinguished by the authority of their verdicts. Project designations that contain the name of a person are given descriptively throughout Part V, under the naming rule the project works under, which costs the comparative chapter its identifiability and is recorded there as an operator decision.

## 2026-08-22 — The reading view is recorded under the custom domain

The published address of record is now `https://dhcraft.org/applied-generative-ai-for-research/`, the custom domain of the organisation, to which the repository's `github.io` address redirects. The README and [[knowledge/design]] carry the new address, so a reader who follows a recorded link reaches the served page directly. Three occurrences of the old address remain, each for its own reason. This journal keeps it in the entry on the reading-view build, because the file is append-only and holds what was decided at the time. [[knowledge/specification]] and the `SITE_URL` constant of `tools/build_docs.py` still carry it. The constant is defined and never read, so no generated page carries the old address and nothing under `docs/` had to change; correcting or removing the constant is left to the next run on the generator, together with the sentence in the specification.

The harness block of `CLAUDE.md` still said that `tools/build_docs.py` had no subject in this instance, which the reading-view build had made false. It now routes an agent working on the reading view to [[knowledge/design]] as the binding document and asks for a generator run after a chapter milestone.
