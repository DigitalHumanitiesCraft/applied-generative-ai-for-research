---
type: chapter
status: grounded
writing-status: skeleton
checked: {}
assertions: []
posits: 0
lang: de
part: "IV. Promptotyping"
chapter: 11
title: "Promptotyping. Forschungsdaten durch Context Engineering und Agentic Engineering in Forschungsartefakte übersetzen"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Promptotyping. Forschungsdaten durch Context Engineering und Agentic Engineering in Forschungsartefakte übersetzen

This chapter presents the central method of the book and may also be published as an independent paper.
Promptotyping is an iterative, document-driven research method for deriving research artefacts from structured research data, scholarly context, and project-specific requirements through LLM-based agentic coding tools.
It integrates:
  - Requirements Engineering;
  - Scholar-Centred Design;
  - Context Engineering;
  - Knowledge Engineering;
  - pragmatic Distillation;
  - agentic implementation;
  - deterministic validation;
  - LLM-mediated review;
  - and verification by a Critical Expert.
Promptotyping addresses the translation between modelled research data and the computational forms through which those data can be investigated, interpreted, enriched, corrected, verified, or published.
Its unit of work is not an isolated prompt or code generation. It is a versioned set of documents that records the project’s current understanding of:
  - its sources and data;
  - research context;
  - requirements;
  - representational decisions;
  - technical constraints;
  - process history;
  - and verification criteria.
An agent implements from these documents. Scholars inspect the specification and verify the resulting artefact against the sources, data, requirements, and research purpose. Findings made during implementation are written back into the maintained knowledge layer.
The documents remain authoritative relative to the generated implementation, but their authority is procedural rather than absolute. When an implementation exposes an unsupported assumption, incomplete requirement, or overlooked property of the data, the documented understanding must be revised.
