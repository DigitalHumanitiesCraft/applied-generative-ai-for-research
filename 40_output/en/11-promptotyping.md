---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-research-artefact-is-a-project-specific-operational-form]]", "[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/agentic-capability-arises-from-model-harness-and-environment]]", "[[30_assertions/agentic-engineering-organises-extended-model-mediated-work]]", "[[30_assertions/context-and-agentic-engineering-are-interdependent]]", "[[30_assertions/context-engineering-organises-the-informational-environment]]", "[[30_assertions/distillation-is-the-documentary-operation-of-context-engineering]]", "[[30_assertions/mapping-into-an-existing-tool-confines-the-inquiry]]", "[[30_assertions/models-shift-the-cost-of-project-specific-implementation]]", "[[30_assertions/promptotyping-is-a-knowledge-driven-method]]", "[[30_assertions/software-operationalises-only-encoded-distinctions]]", "[[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]]", "[[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]]", "[[30_assertions/the-knowledge-base-differs-from-the-working-context]]", "[[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]]", "[[30_assertions/the-method-was-consolidated-from-one-practice]]", "[[30_assertions/the-name-promptotyping-keeps-the-prototype-function]]", "[[30_assertions/the-promptotype-is-the-accepted-iteration-state]]", "[[30_assertions/write-back-makes-a-finding-durable]]"]
posits: 2
lang: en
part: "IV. Promptotyping"
chapter: 11
title: "Promptotyping: Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Promptotyping: Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering

## The asymmetry the method addresses

Scholarly work with digital research data passes through software, and software operationalises only what has been encoded in structures its representational model can process.[^1] A tabular file opens as a sortable table and can be imported as a node list wherever its records and attributes match the structures the receiving program expects. Relations encoded in a project's own markup become a network only after entities, relations, and uncertainties have been interpreted and mapped onto a graph model. The direction of that translation has ordinarily run from the project towards the tool, so researchers map their data and their questions into representations built for other purposes.[^1]

That direction has a price beyond the labour it costs. Mapping into an existing tool confines everything that follows to the distinctions, operations, and forms of interaction the tool provides, which is a smaller loss where the tool was built for the question and a large one where it was not.[^2] The alternative has long been to build something adapted to the project, and the expertise and resources for that have not been evenly available.

What has changed is the cost of a first working implementation. Language models reduce parts of the effort of mapping research data to the models existing software expects and of implementing more closely adapted ways of working with them, while any step that first has to recognise or interpret a structure stays probabilistic.[^3] The consequence that matters here is not speed. Because not all relevant requirements can be determined in advance, a provisional artefact can reveal problems in the specification and show what the data can and cannot support, which makes implementation part of determining the requirements rather than their execution.[^3]

## What Promptotyping is

Promptotyping is an iterative, knowledge-driven method for developing project-specific digital research artefacts from structured research data and maintained project knowledge through Context Engineering and Agentic Engineering.[^4] Its organising structure is an evolving and versioned project knowledge base, and findings arising from implementation and examination are written back into it, so that later work proceeds from the revised understanding.[^4] The method is knowledge-driven in a precise sense. Implementation proceeds from a maintained account of how the data are understood and are to be operationalised, and that account is a semi-formal documentary form which supports no formal inference.[^4]

The name joins prompt and prototyping and keeps the established function of a prototype as a provisional implementation through which requirements and design possibilities are examined and refined.[^5] The artefact it produces is a project-specific operational form through which researchers work with structured research data for a defined scholarly purpose, which distinguishes it from the data by its function in the research process.[^6]

The unit of work is neither an isolated prompt nor a single act of code generation. It is a set of interrelated documents, bounded representations distilled from fuller research material, maintained for human inspection and revision and available for inclusion in the working contexts of agents.[^7] Those documents record the project's current understanding of its sources and data, its research context, its requirements, its representational decisions, its technical constraints, its process history, and its criteria of assessment. The persistent knowledge base has to be held apart from the task-specific working context an agent receives for a particular assignment, and the method treats selection as part of Context Engineering rather than letting accumulation stand in for it.[^8]

## The two practices it integrates

Context Engineering is the systematic selection, organisation, maintenance, and provision of the information a language-model-based system requires for its work. It extends Prompt Engineering from individual prompts to the wider informational environment in which they are interpreted, and it does not consist in placing all available material into a context window.[^9] Agentic Engineering is the systematic organisation of the extended, tool-supported work an agent performs, covering how tasks are decomposed and coordinated, how tools are used, when human intervention is required, and how the work is inspected and continued.[^10]

Neither practice compensates for a failure of the other. A carefully maintained knowledge base does not determine an adequate course of action, and a well-organised workflow cannot repair an inadequate account of the data or the research purpose.[^11] Both operate inside a technical environment that is itself part of the system, since the harness supplies context, access to project resources, tools, and feedback, and agentic capability arises from model, harness, and environment together.[^12]

Around these two practices the method arranges the older disciplines it depends on. Requirements Engineering and Scholar-Centred Design supply the translation from scholarly practice into statements that can guide implementation. Knowledge Engineering supplies the persistent representation of what the project takes to be the case. Distillation is the documentary operation through which the understanding produced by preparation and exploration becomes the maintained documents from which implementation and verification proceed.[^13] Deterministic validation, review by models, and verification by a Critical Expert supply the checking arrangement, and they are the subject of chapter 16.

## The cycle and its authority

Work proceeds through four recurrent forms, Preparation, Exploration, Distillation, and Implementation. They are analytically distinct and do not form a fixed or exclusively linear sequence; their depth, order, and recurrence follow the state and purpose of the project, and findings from implementation may return the work to any earlier form, most often to Distillation.[^14] The return path is the mechanism rather than an accident of practice. A correction becomes methodologically consequential when it is incorporated into maintained project knowledge instead of being confined to the current implementation, which is what write-back means and why it is not a further phase.[^15]

This arrangement gives the documents an authority that is procedural.[^20] They are the reference from which implementation proceeds, and they are revisable by exactly the implementation they govern. Where an implementation exposes an unsupported assumption, an incomplete requirement, or an overlooked property of the data, the documented understanding is what changes.

Acceptance is a separate act. An iteration becomes a promptotype when maintained project knowledge, the resulting artefact, the referenced research-data state, and the documented grounds of acceptance form a coherent and identifiable state for a stated purpose, and a runnable or plausible artefact does not reach that threshold if its relation to knowledge, data, and grounds cannot be reconstructed.[^16] The decision belongs to the Critical Expert, the person or group competent and accountable for judging whether the project knowledge adequately represents the research material and whether the artefact suits its purpose. An agent may contribute proposals and assessments and cannot assume responsibility for their adequacy.[^17]

Behind that division of labour lies a distinction the whole method depends on. Technical verification asks whether an output conforms to formalised requirements. Scholarly validation asks whether the representation those requirements encode is warranted by the source material and adequate for its purpose. An implementation can therefore be correct and inadequate at once, because it faithfully realises a requirement that should not have been stated in that form.[^18]

## The standing of the claim

The method was consolidated from documented practice rather than derived from a theory or tested against a control. The account that follows in this part reports a practice led by one hybrid scholar-developer since 2023, whose cases form no controlled or representative sample, whose documentation is subject to selection effects because inspectable implementation states survived more systematically than abandoned experiments, and whose observed improvements cannot be attributed cleanly to the method rather than to more capable systems, better tools, or increased experience.[^19] Every claim in the following chapters is bounded by that scope, and where the argument reaches past it, the text says so.

This book applies the method to its own production, which is a further reason to state the boundary early. A method that organises its own genesis can make that genesis inspectable, and it cannot thereby demonstrate its own effectiveness.[^21]

## Gaps
- Chapter 7 of the lecture notes describes the same method for a teaching audience and is distilled by the parallel writing lane. The teaching formulation of the four forms of work and of the Critical Expert is therefore not yet available for comparison with the paper's formulation, and the topic map records the open question of which formulation the book carries.
- The hands-on chains of the lecture notes and the accompanying slides are named in the feeding map for Part IV and belong to the other lane. The chapter therefore carries no worked illustration of a first Promptotyping cycle.
- Requirements Engineering and Scholar-Centred Design are named here as the disciplines the method integrates. Their treatment rests on the paper's summary account; a direct anchor in the requirements-engineering literature would need those publications entered as sources.

[^1]: Grounded in [[30_assertions/software-operationalises-only-encoded-distinctions]].
[^2]: Grounded in [[30_assertions/mapping-into-an-existing-tool-confines-the-inquiry]].
[^3]: Grounded in [[30_assertions/models-shift-the-cost-of-project-specific-implementation]].
[^4]: Grounded in [[30_assertions/promptotyping-is-a-knowledge-driven-method]].
[^5]: Grounded in [[30_assertions/the-name-promptotyping-keeps-the-prototype-function]].
[^6]: Grounded in [[30_assertions/a-research-artefact-is-a-project-specific-operational-form]].
[^7]: Grounded in [[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]].
[^8]: Grounded in [[30_assertions/the-knowledge-base-differs-from-the-working-context]].
[^9]: Grounded in [[30_assertions/context-engineering-organises-the-informational-environment]].
[^10]: Grounded in [[30_assertions/agentic-engineering-organises-extended-model-mediated-work]].
[^11]: Grounded in [[30_assertions/context-and-agentic-engineering-are-interdependent]].
[^12]: Grounded in [[30_assertions/agentic-capability-arises-from-model-harness-and-environment]].
[^13]: Grounded in [[30_assertions/distillation-is-the-documentary-operation-of-context-engineering]].
[^14]: Grounded in [[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]].
[^15]: Grounded in [[30_assertions/write-back-makes-a-finding-durable]].
[^16]: Grounded in [[30_assertions/the-promptotype-is-the-accepted-iteration-state]].
[^17]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^18]: Grounded in [[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]].
[^19]: Grounded in [[30_assertions/the-method-was-consolidated-from-one-practice]].
[^20]: Posit: calling the authority of the documents procedural follows from the return paths of the cycle, since a reference that the work it governs may revise binds the next step rather than the matter. Open evidence question: whether the sources anywhere state the authority relation in these terms rather than describing its effects.
[^21]: Posit: a method applied to its own production yields an inspectable record of that production and no evidence about its effect on other work, because the case is single and its author is the method's originator. Open evidence question: an evaluation in which contributors who did not develop the method produce and accept a comparable artefact from the same specification.
