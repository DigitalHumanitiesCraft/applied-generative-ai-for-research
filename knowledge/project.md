---
title: Project
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
related: [specification, plan, sources, outline, state, journal]
---

# Project

This repository produces the book *Applied Generative AI for Research. Knowledge, Context, Agents, and Verifiable Research Artefacts*, a bilingual scholarly synthesis on the controlled use of generative models and agentic systems in research. The manuscript is written inside a Grounded Vault instance, so the book applies the method it describes to its own genesis and every substantive claim of the finished text resolves through the anchor chain to a passage in a registered source. The purpose in full, with the evidence obligation and the parameters of the instance, stands in [[knowledge/specification]].

## Sub-goals

The work is cut into four sub-goals. Their order and their current state are in [[knowledge/plan]].

| Sub-goal | Content |
|---|---|
| U1 | Repository and knowledge base. Instantiate the template, register the feeding sources, and lay out the chapter skeleton. |
| U2 | Manuscript parts I to III, written from the lecture notes and the slide deck. |
| U3 | Manuscript parts IV to VI, written from the Promptotyping paper, the Promptotyping document templates and the hands-on chains. |
| U4 | Reading view on GitHub Pages. |

## Feeding map

Each part of the manuscript draws on a fixed set of feeding artefacts. The map is binding for the assertion work; a part that needs material beyond its row enters that material as a new source in [[knowledge/sources]] first.

| Part | Feeding artefacts |
|---|---|
| I. Generative Models as Research Systems | script chapter 2, slide section AI Agents |
| II. From Prompting to Grounded Knowledge | script chapters 3 to 5, paper (Project Knowledge Base), "Vault als materialisiertes Wissensmodell" |
| III. Agentic Research Work | script chapter 6, slide sections Agentic Engineering and Workflows |
| IV. Promptotyping | paper chapter 2, script chapter 7, Promptotyping templates |
| V. Research Artefacts and Comparative Cases | paper chapters 2.3 and 3 |
| VI. Worked Example, Boundaries, and Implications | paper chapter 4, hands-on chains from slides and script |

The numbered script chapters are the numbered chapters of the German Full Lecture Notes, where chapter 2 covers language models and the step from model to agent, chapters 3 to 5 cover prompt, context and knowledge engineering, chapter 6 covers agentic engineering, and chapter 7 covers Promptotyping with verification and write-back. The English Full Lecture Notes carry the same material under prose headings without numbers, so a passage cited from the English version is located by its heading. The hands-on chains are the sections numbered 3.8, 4.6, 5.8, 6.7 and 7.11 of the German version. The slide sections are located by their slide titles in the deck export, which carries no heading structure. Every feeding artefact and its vault path stands in [[knowledge/sources]].

## Revisable settings

These were set at instantiation and can be changed by the operator without touching the invariant architecture. The reasoning behind each is in [[knowledge/journal]].

| Setting | Value |
|---|---|
| Controlled topic set | the six parts of the manuscript, one topic map each |
| Bilingual layout | `40_output/en/` and `40_output/de/`, same slug per chapter |
| Skeleton state | `writing-status: skeleton` beside the grounding status, because the template's `status` vocabulary has no rung below `grounded` |
| Machine review | fresh-context review by a separate Claude agent until a cross-family reviewer is fixed; every finding marked as same-family |
| Licences | CC BY 4.0 for manuscript text and documentation, MIT for code and tooling |
| Source register | `knowledge/sources.md` rather than the convention's canonical `data.md`, because `data` names an inactive source type of this vault and the file would misroute an agent |
| Template docs | the template's `docs/` folder was removed at instantiation; the reading-view lane decides what `docs/` holds |
