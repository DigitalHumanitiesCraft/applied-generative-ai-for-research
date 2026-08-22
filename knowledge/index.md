---
title: Index
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
related: [project, specification, plan, sources, outline, schema, operations, state, journal, handoff]
---

# Index

Navigation and terminology of the vault. Human readers start at [[HOME]]; agents start at `CLAUDE.md`, which routes onto these documents.

## Reading paths

- **Understand the project**: [[knowledge/project]] for what is being built and from what, [[knowledge/specification]] for purpose and parameters, then [[knowledge/state]] for where work stands.
- **Find the next step**: [[knowledge/plan]] for the lanes and their order, [[knowledge/handoff]] for open handover points.
- **Work on a chapter**: [[knowledge/outline]] for what the chapter has to cover, [[knowledge/sources]] for the material it draws on.
- **Produce or check content**: [[knowledge/schema]] for what a well-formed artifact is, [[knowledge/operations]] for the chain that produces it.
- **Understand a past decision**: [[knowledge/journal]], append-only, newest last.

## The knowledge documents

| Document | Holds | Changes |
|---|---|---|
| [[knowledge/index]] | navigation, terminology | rarely |
| [[knowledge/project]] | what the book is, its sub-goals, the feeding map, the revisable settings | on scope changes |
| [[knowledge/specification]] | purpose, parameters, settled decisions | on decisions |
| [[knowledge/plan]] | the four lanes and their order | as work proceeds |
| [[knowledge/outline]] | the canonical outline of the book, verbatim from the expose | on structure changes |
| [[knowledge/sources]] | the source register with provenance and rights | on a new source |
| [[knowledge/handoff]] | open handover points waiting for integration | as points arrive |
| [[knowledge/schema]] | layer model, document types, anchor mechanics, audit trail | rarely, by decision |
| [[knowledge/operations]] | the chains: acquire, ingest, distill, assertions, chapters, query, check | rarely, by decision |
| [[knowledge/state]] | source inventory, chapter register, everything volatile | constantly |
| [[knowledge/journal]] | decision history | append-only |

A document is split only when its sections develop divergent update rhythms or divergent readers.

## Terminology

- **Source**: The original file exactly as it arrived, kept untouched so that every later form of its content can be checked against it.
- **Markdown representation**: The uniform Markdown form of a source, produced once by converting the original and given block IDs so that later layers anchor into passages that never change afterwards.
- **Distillate**: The set of single statements extracted from one source, each anchored to the passage of the representation it was taken from.
- **Assertion**: A single source-supported statement synthesized from the distillates of a topic and grounded in at least one distillate statement.
- **Chapter**: An output text in which every load-bearing sentence carries a footnote to an assertion and every own conclusion is marked as a posit.
- **Source type**: a class of sources defined by its Markdown representation, its distillation operation and its grounding anchor.
- **Grounding**: the anchor relation between an assertion and its source locations. A structural property an agent can produce; it says nothing about whether the statement is true.
- **Evidence**: a grounding relation that has passed human expert verification. Relational and deliberately rare; a fresh vault contains grounding, evidence arises only through review.
- **Provenance chain**: the unbroken anchor path from an output sentence through assertions and distillates to source locations. A break anywhere is a defect that validation detects.
- **Audit trail**: the principle that status fields record outcomes of checks that actually ran, each with its date on the checked document.
- **Posit**: a conclusion in the output without source support, explicitly marked with its rationale and open evidence question.
- **Validation / machine review / verification**: the three checking instances, deterministic, adversarial-probabilistic, human. Note that this assignment inverts the IEEE convention; here establishing truth is a human act.
