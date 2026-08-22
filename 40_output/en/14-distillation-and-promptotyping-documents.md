---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-governance-document-records-authority-and-permissions]]", "[[30_assertions/a-technology-baseline-carries-a-family-of-artefacts]]", "[[30_assertions/a-wrong-output-is-diagnosed-by-document-type]]", "[[30_assertions/agent-instruction-documents-translate-knowledge-into-imperatives]]", "[[30_assertions/an-outdated-rule-set-is-the-costliest-decay]]", "[[30_assertions/declarative-documents-state-what-the-project-takes-to-be-the-case]]", "[[30_assertions/derived-artefacts-are-not-maintained-knowledge]]", "[[30_assertions/design-knowledge-stays-declarative]]", "[[30_assertions/distillation-is-not-summarisation-or-compression]]", "[[30_assertions/distillation-is-the-documentary-operation-of-context-engineering]]", "[[30_assertions/domain-knowledge-carries-disciplinary-stipulation]]", "[[30_assertions/process-documents-preserve-how-the-understanding-developed]]", "[[30_assertions/the-action-layer-is-injected-and-therefore-kept-thin]]", "[[30_assertions/the-agent-enters-the-knowledge-base-through-its-index]]", "[[30_assertions/the-architecture-document-gives-the-agent-its-module-boundaries]]", "[[30_assertions/the-charter-carries-the-project-identity]]", "[[30_assertions/the-handoff-document-is-a-process-inbox]]", "[[30_assertions/the-index-routes-a-knowledge-base]]", "[[30_assertions/the-integration-document-holds-the-contract-at-the-boundary]]", "[[30_assertions/the-journal-is-a-curated-provenance-index]]", "[[30_assertions/the-knowledge-base-differs-from-the-working-context]]", "[[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]]", "[[30_assertions/the-material-document-carries-epistemic-responsibility]]", "[[30_assertions/the-method-core-of-the-action-layer-is-portable]]", "[[30_assertions/the-plan-is-the-forward-looking-counterpart-of-the-journal]]", "[[30_assertions/the-report-addresses-an-external-reader]]", "[[30_assertions/the-specification-holds-interlocked-questions-in-one-place]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]"]
posits: 0
lang: en
part: "IV. Promptotyping"
chapter: 14
title: "Distillation and Promptotyping Documents"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Distillation and Promptotyping Documents

## The operation

Distillation translates the understanding produced through Preparation and Exploration into the maintained knowledge documents from which implementation and verification proceed, and it is the principal documentary operation of Context Engineering within Promptotyping.[^1] What it produces represents the project knowledge required for the current purpose while leaving the fuller sources and research data available for direct inspection and computational processing.[^1]

The operation is easy to mistake for summarisation, and the mistake has practical consequences. A model's nominal context capacity does not imply that all supplied information will be used reliably, and additional or poorly selected material can make relevant information harder to use, so the point of Distillation is an inspectable and selective representation that preserves the distinctions, conditions, and uncertainties an adequate implementation and verification require.[^2] Because the same material may need to be distilled differently when the purpose or the intended artefact changes, the operation is a form of pragmatic modelling rather than a fixed reduction of the source.[^2]

Selection is therefore constitutive. The persistent knowledge base holds the project's maintained understanding, the working context of an agent holds what a particular assignment needs, and the method treats the choice between them as part of Context Engineering rather than letting accumulation stand in for it.[^3] An agent may receive a distilled account together with task-relevant selections from the data while inspectable computational operations process the complete dataset outside the model context.[^3]

## What a Promptotyping Document is

The documents of the knowledge base are bounded representations distilled from fuller research material, maintained for human inspection and revision and available for inclusion in the working contexts of agents.[^4] Six properties follow from that double readership. Such a document is readable by scholars and actionable for agents, it is versioned and revisable, it stays compact enough for a managed context architecture, and it remains traceable to the project's source and decision basis.

Their types are organisational heuristics rather than a prescribed file structure, so projects may name, combine, and distribute the functions as their work requires.[^4] Three functions recur. Declarative documents state what the project currently takes to be the case and what the artefact is required to realise.[^5] Process documents preserve how the understanding developed and where the work is going.[^6] Agent instruction documents translate the maintained knowledge into imperatives and carry no knowledge of their own.[^7]

The types are not distinguished by tone, and a rule written as reasoned prose can still be an action document. The question that decides is which document has to be revised when the output is wrong. A formally wrong output, a break in style, or an ignored prohibition is diagnosed in the action document; a substantively wrong output is diagnosed in the knowledge documents and is not patched in the action layer.[^8]

## The recurring documents

An index opens the knowledge base once it holds more than three documents. It addresses a human reviewer, a newly set up coding agent, and the person responsible for the project returning after an interval, and it answers which documents exist, which question each of them serves, in which order they are read, and which terms are constitutive. Its only update obligation is consistency against the real folder content, because an index that loses it is worse than none, since it creates false confidence.[^9] The reading order it prescribes is the entry path of every session, running from the index through the open handover points to the task-relevant document, and it must point at repository-internal sources, because a repository whose method knowledge lives only in an external vault is blind in a session without access to that vault.[^10]

A charter carries the identity and scope of the project. It is the canonical account of what the project is, and a public README may derive from it while referring back to the knowledge base.[^11]

The material document carries the epistemic responsibility for the data. It answers what they are, where they come from, how they are modelled, and where they stop carrying, recording per source the origin, capture logic, licence, provenance, and capture period.[^12] A domain-knowledge document carries whatever disciplinary stipulation follows neither from the material nor from a software requirement, such as editorial guidelines, an encoding mapping, a calculation logic, or an ontology, and it separates the reasoning layer that explains why from the rule set that fixes how.[^13] The most expensive failure of the whole knowledge base lives here, in a rule set that still describes a superseded schema as valid while the working team has already moved on, which is why a schema change carries the rule set with it in the same working step.[^14]

The specification holds requirements, narrative scenarios, functional scope, and decisions together, because a story motivates a requirement, a feature implements it, and a decision justifies why that feature is built as it is, so that separating the layers would let a change in one silently age the others.[^15] The architecture document carries the technical realisation and gives the agent the module boundaries it builds against, since a description too vague produces code that ignores the intended layers.[^16] Where several projects build artefacts of one family, a technology baseline carries the shared stack decisions centrally, and the architecture of an instance records only its own stack and its deviations.[^17] The design document carries design stance, design system, interaction patterns, and visualisation logic as declarative knowledge, and the socialisation of an agent on the aesthetic layer arises through the action layer pointing at it rather than through imperatives inside it.[^18] Where a project shares data, formats, or responsibilities across a boundary, an integration document holds the currently valid contract, with exactly one side declared the source of truth where both sides describe it.[^19]

Two documents carry the process. A plan orders outstanding work into milestones whose exit conditions are anchored against acceptance criteria or quality gates of the specification and are formulated as done-when statements.[^20] A journal is the curated retrospective index of transitions, recording per transition whether the result was integrated, discarded, or corrected, and carrying no current status, no open tasks, and no detailed check results.[^21] Between them sits the process inbox, which carries open handover points alone, and whose processing integrates durable content into the responsible document, writes the short entry in the journal, and then removes the point completely.[^22]

The action layer is the one document written for the agent alone. It routes into the knowledge base and translates it into imperatives, and because it is injected at every session start, drift there is more expensive than anywhere else, so every line derivable from the code or the knowledge base is deleted rather than maintained.[^23] Its method core, covering routing, handoff processing, provenance rules, checking rules, design principles, scope, and the hierarchy of truth, survives a change of coding agent, and only the tool-specific block is exchanged.[^24]

Two further documents sit at the edges of the set. A status report is the one document type whose addressee is external, and it is separated from the journal by lifecycle and curation rather than by content.[^25] A governance document is optional and enters where agents act across several persistent resources or handle consequential claims, rights, and release decisions, recording authority, permissions, evidential status, write-back targets, and escalation paths.[^26]

What does not belong in the set is equally definite. Derived project artefacts are regenerable outputs produced from a referenced project state through an identified process, and they record derived observations rather than interpretations or decisions that contributors have examined and adopted, which is what keeps them outside the maintained knowledge.[^27]

## When Distillation is finished

The completion criterion is practical. A new contributor or agent instance, given the relevant knowledge documents and access to the project resources, should be able to reconstruct the project's current logic and continue the assigned work without undocumented explanation, and difficulties in doing so reveal omissions in the maintained account.[^28] The criterion does not guarantee completeness, and it makes omissions visible at the point where the agent cannot act or produces output that betrays the missing context. Successful implementation establishes nothing about scholarly adequacy, because a specification may be executable while resting on assumptions that cannot be justified.[^28]

## Gaps
- The templates describe a document set considerably larger than the three types the paper names, and the topic map records the open question of whether the book presents the full set or the typology with the templates as its instantiation. This chapter presents both and does not settle the question.
- The templates are written in German with English function names. Which of their terms the book carries untranslated is undecided, and the chapter uses descriptive English names throughout as a provisional choice.
- Chapter 7 of the lecture notes covers the same material for a teaching audience and belongs to the parallel lane, so no comparison with its formulation of the document set was possible.
- The verification document is named here as a member of the set and treated in chapter 16, where the forms of checking are the subject.

[^1]: Grounded in [[30_assertions/distillation-is-the-documentary-operation-of-context-engineering]].
[^2]: Grounded in [[30_assertions/distillation-is-not-summarisation-or-compression]].
[^3]: Grounded in [[30_assertions/the-knowledge-base-differs-from-the-working-context]].
[^4]: Grounded in [[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]].
[^5]: Grounded in [[30_assertions/declarative-documents-state-what-the-project-takes-to-be-the-case]].
[^6]: Grounded in [[30_assertions/process-documents-preserve-how-the-understanding-developed]].
[^7]: Grounded in [[30_assertions/agent-instruction-documents-translate-knowledge-into-imperatives]].
[^8]: Grounded in [[30_assertions/a-wrong-output-is-diagnosed-by-document-type]].
[^9]: Grounded in [[30_assertions/the-index-routes-a-knowledge-base]].
[^10]: Grounded in [[30_assertions/the-agent-enters-the-knowledge-base-through-its-index]].
[^11]: Grounded in [[30_assertions/the-charter-carries-the-project-identity]].
[^12]: Grounded in [[30_assertions/the-material-document-carries-epistemic-responsibility]].
[^13]: Grounded in [[30_assertions/domain-knowledge-carries-disciplinary-stipulation]].
[^14]: Grounded in [[30_assertions/an-outdated-rule-set-is-the-costliest-decay]].
[^15]: Grounded in [[30_assertions/the-specification-holds-interlocked-questions-in-one-place]].
[^16]: Grounded in [[30_assertions/the-architecture-document-gives-the-agent-its-module-boundaries]].
[^17]: Grounded in [[30_assertions/a-technology-baseline-carries-a-family-of-artefacts]].
[^18]: Grounded in [[30_assertions/design-knowledge-stays-declarative]].
[^19]: Grounded in [[30_assertions/the-integration-document-holds-the-contract-at-the-boundary]].
[^20]: Grounded in [[30_assertions/the-plan-is-the-forward-looking-counterpart-of-the-journal]].
[^21]: Grounded in [[30_assertions/the-journal-is-a-curated-provenance-index]].
[^22]: Grounded in [[30_assertions/the-handoff-document-is-a-process-inbox]].
[^23]: Grounded in [[30_assertions/the-action-layer-is-injected-and-therefore-kept-thin]].
[^24]: Grounded in [[30_assertions/the-method-core-of-the-action-layer-is-portable]].
[^25]: Grounded in [[30_assertions/the-report-addresses-an-external-reader]].
[^26]: Grounded in [[30_assertions/a-governance-document-records-authority-and-permissions]].
[^27]: Grounded in [[30_assertions/derived-artefacts-are-not-maintained-knowledge]].
[^28]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
