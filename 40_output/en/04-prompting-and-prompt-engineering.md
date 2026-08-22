---
type: chapter
status: grounded
writing-status: skeleton
checked: {}
assertions: []
posits: 0
lang: en
part: "II. From Prompting to Grounded Knowledge"
chapter: 4
title: "Prompting and Prompt Engineering"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper, Project Knowledge Base", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Prompting and Prompt Engineering

Prompting is introduced as the construction of an input sequence that conditions a model’s output distribution. It includes not only direct instructions but also examples, data, constraints, terminology, ordering, formatting rules, and interaction history.
The chapter distinguishes informal prompting from **Prompt Engineering**, defined as the iterative design and evaluation of input sequences for a specified task. Prompt Engineering requires more than discovering persuasive formulations. It involves defining the task, specifying expected outputs, constructing representative cases, testing failures, comparing variants, and documenting changes.
The chapter covers:
  - instructions, data, examples, and constraints;
  - zero-shot and few-shot prompting;
  - structured-output requirements;
  - role and perspective instructions;
  - decomposition and iterative refinement;
  - representative test cases;
  - evaluation criteria;
  - prompt versioning;
  - stable and stochastic behaviour;
  - model-specific and portable instructions;
  - the limits of prompt optimisation.
The central limitation is that complex work cannot be governed reliably through an isolated prompt. As tasks become longer and more dependent on project-specific information, the problem shifts from wording an instruction to constructing and maintaining the context within which an instruction operates.
