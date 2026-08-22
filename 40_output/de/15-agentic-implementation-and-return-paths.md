---
type: chapter
status: grounded
writing-status: skeleton
checked: {}
assertions: []
posits: 0
lang: de
part: "IV. Promptotyping"
chapter: 15
title: "Agentische Implementierung und Rückwege"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
working-title: true
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Agentische Implementierung und Rückwege

Implementation hands the maintained document set to an agentic coding system operating within the project repository.
The agent translates the semi-formal specification into:
  - parsers;
  - transformations;
  - schemas;
  - tests;
  - queries;
  - code;
  - interfaces;
  - and visible research artefacts.
Implementation should proceed through inspectable milestones. Each increment must remain small enough to evaluate before further complexity is added.
The defining loop does not run only between code and output. Findings return to different depths of the project:
  - an implementation defect may require a code correction;
  - an incomplete action instruction may require revision of the agent configuration;
  - a missing requirement belongs in a declarative document;
  - an unsupported assumption returns the project to Exploration;
  - a changed source or incomplete schema returns it to Preparation.
The generated artefact is therefore not the final authority. It is an implementation through which the adequacy of the maintained project understanding can be tested.
