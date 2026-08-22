---
type: chapter
status: grounded
writing-status: skeleton
checked: {}
assertions: []
posits: 0
lang: en
part: "II. From Prompting to Grounded Knowledge"
chapter: 5
title: "Context Engineering and Pragmatic Distillation"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper, Project Knowledge Base", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Context Engineering and Pragmatic Distillation

Context Engineering concerns the selection, construction, organisation, and maintenance of information made available to a model during a task or workflow.
The chapter distinguishes transient prompts from wider context architectures. It examines how context can be retrieved, generated, compressed, refreshed, ordered, and separated according to its function. It also addresses the limitations of nominally large context windows: the presence of information in a context does not ensure that the model will use it consistently or appropriately.
Central topics include:
  - prompts versus context;
  - context windows;
  - task-relative relevance;
  - context saturation and degradation;
  - long-context limitations;
  - retrieval and selective inclusion;
  - persistent and transient context;
  - generated context;
  - context architectures;
  - context refresh and revision.
The chapter develops **Distillation** as a form of pragmatic modelling rather than simple compression. A distilled representation retains the distinctions required for a particular task while leaving the full source, dataset, or formal model intact.
This is expressed through a central arrangement:
The model reads about the data and writes code that reads the data.
The complete research data remain the evidential and computational basis. The model receives a task-specific description of their structure, semantics, uncertainty, exceptions, and relevance. Generated code then processes the complete data outside the model’s context.
