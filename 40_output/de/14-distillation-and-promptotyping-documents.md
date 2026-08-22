---
type: chapter
status: grounded
writing-status: skeleton
checked: {}
assertions: []
posits: 0
lang: de
part: "IV. Promptotyping"
chapter: 14
title: "Distillation und Promptotyping Documents"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Distillation und Promptotyping Documents

Distillation translates the understanding produced through Preparation and Exploration into the document set from which implementation proceeds.
A Promptotyping Document is a project-bound knowledge document that is:
  - readable by scholars;
  - actionable for agents;
  - versioned;
  - revisable;
  - sufficiently compact for a managed context architecture;
  - and traceable to the project’s source and decision basis.
Recurring documents include:
### data.md
Describes formats, structures, semantics, provenance, controlled values, gaps, uncertainty, exceptional cases, and known limitations.
### requirements.md
Expresses functional and non-functional requirements, user stories, scenarios, acceptance criteria, and project boundaries.
### design.md
Records interface, interaction, visualisation, and representational decisions, including the treatment of uncertainty, hierarchy, provenance, missingness, and contested classifications.
### verification.md
Defines claims, expected evidence, applicable procedures, authority levels, and acceptance conditions.
### journal.md
Records sessions, attempts, failures, model and tool use, decisions, unresolved questions, and handovers.
### Action documents
Files such as CLAUDE.md, AGENTS.md, or equivalent repository instructions specify how agents should work, which technologies they may use, what they may modify, which checks they must perform, and how findings must be documented.
The completion criterion for Distillation is practical:
A new agent instance with access to the project data and documents should be able to understand the current project logic and continue the work without an undocumented oral explanation.
This criterion does not guarantee completeness. It makes omissions visible when the agent cannot act or produces output that reveals missing context.
