---
title: State
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
related: [operations, journal]
---

# State

Everything volatile in one place, so the rule documents stay stable. Update rows here as work proceeds; never record processing state anywhere else.

## Source inventory

One row per source. Processing status: `new` → `ingested` → `distilled`. This section is generated from the real file state by `python tools/inventory.py . --write` and is never edited by hand; everything between the two markers is overwritten on each run.

<!-- inventory:begin -->
| Source | Type | Channel | Markdown representation | Distillate | Status |
|---|---|---|---|---|---|
| Knowledge, Context and Agentic Engineering for Knowledge Work. Full Lecture Notes, English | document | handover | [[10_markdown/documents/lecture-notes-en]] | — | ingested |
| Knowledge, Context and Agentic Engineering for Knowledge Work. Full Lecture Notes, German | document | handover | [[10_markdown/documents/lecture-notes-de]] | — | ingested |
| Knowledge, Context and Agentic Engineering for Knowledge Work. Full Slide Deck, slide-text export | document | handover | [[10_markdown/documents/slide-deck]] | — | ingested |
| Promptotyping. Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering | document | handover | [[10_markdown/documents/promptotyping-paper]] | — | ingested |
| Vault als materialisiertes Wissensmodell | document | handover | [[10_markdown/documents/vault-as-materialised-knowledge-model]] | — | ingested |
<!-- inventory:end -->

## Chapter register

One row per chapter of the output, with the English file and its German counterpart side by side, because the two languages carry the same chapter. Writing status mirrors the `writing-status` field of the chapter's frontmatter, which runs `skeleton` to `drafted` to `written`; the grounding status of the same file runs on the separate ladder that [[knowledge/schema]] defines.

| Chapter | File (en) | File (de) | Status | Notes |
|---|---|---|---|---|
| Research after the Prompt (Frame) | [[40_output/en/00-research-after-the-prompt]] | [[40_output/de/00-research-after-the-prompt]] | skeleton | German title is a working title |
| 1. What Large Language Models Are (I) | [[40_output/en/01-what-large-language-models-are]] | [[40_output/de/01-what-large-language-models-are]] | skeleton | German title is a working title |
| 2. Models, Tools, and Generative Systems (I) | [[40_output/en/02-models-tools-and-generative-systems]] | [[40_output/de/02-models-tools-and-generative-systems]] | skeleton | German title is a working title |
| 3. Knowledge, Evidence, and Epistemic Authority (I) | [[40_output/en/03-knowledge-evidence-and-epistemic-authority]] | [[40_output/de/03-knowledge-evidence-and-epistemic-authority]] | skeleton | German title is a working title |
| 4. Prompting and Prompt Engineering (II) | [[40_output/en/04-prompting-and-prompt-engineering]] | [[40_output/de/04-prompting-and-prompt-engineering]] | skeleton | German title is a working title |
| 5. Context Engineering and Pragmatic Distillation (II) | [[40_output/en/05-context-engineering-and-pragmatic-distillation]] | [[40_output/de/05-context-engineering-and-pragmatic-distillation]] | skeleton | German title is a working title |
| 6. Knowledge Engineering for Generative Research (II) | [[40_output/en/06-knowledge-engineering-for-generative-research]] | [[40_output/de/06-knowledge-engineering-for-generative-research]] | skeleton | German title is a working title |
| 7. The Grounded Vault (II) | [[40_output/en/07-the-grounded-vault]] | [[40_output/de/07-the-grounded-vault]] | skeleton | German title is a working title |
| 8. From Models to Agents (III) | [[40_output/en/08-from-models-to-agents]] | [[40_output/de/08-from-models-to-agents]] | skeleton | German title is a working title |
| 9. Agentic Engineering as Work Organisation (III) | [[40_output/en/09-agentic-engineering-as-work-organisation]] | [[40_output/de/09-agentic-engineering-as-work-organisation]] | skeleton | German title is a working title |
| 10. Failure, Drift, and Verification Debt (III) | [[40_output/en/10-failure-drift-and-verification-debt]] | [[40_output/de/10-failure-drift-and-verification-debt]] | skeleton | German title is a working title |
| 11. Promptotyping: Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering (IV) | [[40_output/en/11-promptotyping]] | [[40_output/de/11-promptotyping]] | skeleton | German title is a working title |
| 12. Preconditions, Scope, and Relation to Research Software Engineering (IV) | [[40_output/en/12-preconditions-scope-and-relation-to-research-software-engineering]] | [[40_output/de/12-preconditions-scope-and-relation-to-research-software-engineering]] | skeleton | German title is a working title |
| 13. Preparation and Exploration (IV) | [[40_output/en/13-preparation-and-exploration]] | [[40_output/de/13-preparation-and-exploration]] | skeleton | German title is a working title |
| 14. Distillation and Promptotyping Documents (IV) | [[40_output/en/14-distillation-and-promptotyping-documents]] | [[40_output/de/14-distillation-and-promptotyping-documents]] | skeleton | German title is a working title |
| 15. Agentic Implementation and Return Paths (IV) | [[40_output/en/15-agentic-implementation-and-return-paths]] | [[40_output/de/15-agentic-implementation-and-return-paths]] | skeleton | German title is a working title |
| 16. Verification, the Critical Expert, and Distributed Authority (IV) | [[40_output/en/16-verification-the-critical-expert-and-distributed-authority]] | [[40_output/de/16-verification-the-critical-expert-and-distributed-authority]] | skeleton | German title is a working title |
| 17. Research Artefacts as Scholarly Arguments (V) | [[40_output/en/17-research-artefacts-as-scholarly-arguments]] | [[40_output/de/17-research-artefacts-as-scholarly-arguments]] | skeleton | German title is a working title |
| 18. An Epistemic Typology of Research Interfaces (V) | [[40_output/en/18-an-epistemic-typology-of-research-interfaces]] | [[40_output/de/18-an-epistemic-typology-of-research-interfaces]] | skeleton | German title is a working title |
| 19. Comparative Project Cases (V) | [[40_output/en/19-comparative-project-cases]] | [[40_output/de/19-comparative-project-cases]] | skeleton | German title is a working title |
| 20. Teaching, Transfer, and Asymmetric Amplification (V) | [[40_output/en/20-teaching-transfer-and-asymmetric-amplification]] | [[40_output/de/20-teaching-transfer-and-asymmetric-amplification]] | skeleton | German title is a working title |
| 21. A Complete Worked Example (VI) | [[40_output/en/21-a-complete-worked-example]] | [[40_output/de/21-a-complete-worked-example]] | skeleton | German title is a working title |
| 22. From Promptotype to Research Software Engineering (VI) | [[40_output/en/22-from-promptotype-to-research-software-engineering]] | [[40_output/de/22-from-promptotype-to-research-software-engineering]] | skeleton | German title is a working title |
| 23. Reconstructability, Sustainability, and Proprietary Dependence (VI) | [[40_output/en/23-reconstructability-sustainability-and-proprietary-dependence]] | [[40_output/de/23-reconstructability-sustainability-and-proprietary-dependence]] | skeleton | German title is a working title |
| 24. Amplification, Responsibility, and the Limits of Externalisation (VI) | [[40_output/en/24-amplification-responsibility-and-the-limits-of-externalisation]] | [[40_output/de/24-amplification-responsibility-and-the-limits-of-externalisation]] | skeleton | German title is a working title |
| Grounded Generative Research (Frame) | [[40_output/en/25-grounded-generative-research]] | [[40_output/de/25-grounded-generative-research]] | skeleton | German title is a working title |

## Open work

<!-- Short, current list; done items are deleted, decisions go to the journal. -->

- Run the first vertical production pass on one source of Part II, from its distillate through one assertion to one written paragraph, before a second source is distilled.
- Fix the cross-family reviewer for the machine review contract.
- Decide whether the Promptotyping document templates enter as one source or as eighteen.
- Decide which dataset carries the worked example of Part VI.
