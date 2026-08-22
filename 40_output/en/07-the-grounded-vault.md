---
type: chapter
status: grounded
writing-status: skeleton
checked: {}
assertions: []
posits: 0
lang: en
part: "II. From Prompting to Grounded Knowledge"
chapter: 7
title: "The Grounded Vault"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper, Project Knowledge Base", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# The Grounded Vault

The Grounded Vault is a versioned, source-bound, inspectable, revisable, and agent-operable knowledge environment shared by scholars and computational agents.
It is not defined by a specific application. It may be implemented through a Git repository, local file system, Markdown environment, Obsidian vault, or comparable infrastructure. What matters is the organisation and governance of the knowledge it contains.
A Grounded Vault fulfils seven conditions:
1.  **Source-bound** Claims and descriptions can be traced to research sources, structured data, references, or documented decisions.
1.  **Versioned** Changes remain historically and procedurally inspectable.
1.  **Layered** Evidence, interpretation, process memory, and action instructions are distinguished.
1.  **Inspectable** Human researchers can read, criticise, and revise the maintained knowledge.
1.  **Agent-operable** Computational agents can retrieve, process, and act from the relevant materials.
1.  **Revisable** New findings alter the maintained knowledge layer rather than remaining isolated in local outputs or conversations.
1.  **Governed** Provenance, authority, permissions, and overwrite behaviour are explicitly controlled.
The Grounded Vault may include:
  - research sources;
  - structured datasets;
  - schemas and standards;
  - data descriptions;
  - requirements;
  - design documents;
  - verification concepts;
  - journals;
  - decision records;
  - agent instructions;
  - generated corpus reports;
  - scripts;
  - tests;
  - and published artefacts.
The chapter distinguishes three knowledge layers:
### Declarative Documents
These state what is currently understood about the sources, data, requirements, design, mappings, and intended artefact.
### Process Documents
These record how the work proceeded, which alternatives were considered, why decisions were made, and what remains unresolved.
### Action Documents
These specify how agents and tools should act, including technical baselines, permissions, file boundaries, tests, checkpoints, and documentation duties.
The chapter also distinguishes curated knowledge from deterministically generated knowledge. Curated documents remain under scholarly responsibility even when models assist with drafting. Generated documents are rendered from data through named scripts or processes and are overwritten when those processes run again.
