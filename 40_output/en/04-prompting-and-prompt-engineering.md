---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-prompt-is-a-bounded-specification]]", "[[30_assertions/a-prompt-is-the-whole-input-sequence]]", "[[30_assertions/iteration-runs-in-bounded-passes]]", "[[30_assertions/no-single-prompting-strategy-is-optimal]]", "[[30_assertions/personas-produce-hypotheses]]", "[[30_assertions/precision-does-not-follow-from-length]]", "[[30_assertions/prompt-effects-are-local]]", "[[30_assertions/prompt-engineering-is-iterative-design-and-evaluation]]", "[[30_assertions/prompt-variants-are-experimental-interventions]]", "[[30_assertions/prompting-does-not-replace-work-organisation]]", "[[30_assertions/prompting-intervenes-in-the-current-computation]]", "[[30_assertions/role-assignment-adds-no-domain-knowledge]]", "[[30_assertions/structured-output-has-four-levels-of-conformance]]", "[[30_assertions/the-object-shifts-to-the-information-state]]"]
posits: 1
lang: en
part: "II. From Prompting to Grounded Knowledge"
chapter: 4
title: "Prompting and Prompt Engineering"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper (Project Knowledge Base)", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Prompting and Prompt Engineering

## What a prompt is

A prompt is the whole input sequence supplied for a model call. It can carry a task, source material, context information, requirements, constraints, examples, procedural notes and specifications for the expected output, so reading it as a question hides most of what is actually being handed over.[^1] The word invites the wrong picture, of a formulation addressed to an interlocutor, when the object is a data structure whose parts have different functions.

Prompt Engineering is the iterative design and evaluation of such a sequence for a defined model and task. The work proceeds by changing content, structure or applied technique and assessing the result, and the term stays deliberately narrower than Context Engineering, because it addresses one input sequence rather than the whole information environment of a longer trajectory.[^2] Chapter 5 takes over at the point where that narrowness stops being useful.

## The prompt as a bounded specification

The productive form is a bounded specification set inside an existing context of knowledge and work. Its typical components are goal, initial situation, requirements, constraints, procedure, output form and completion criterion, and separating the immediate task from source context, rules and output contract makes each part inspectable on its own. The categories can be changed independently, so a different source changes the context and a different editorial policy changes the rules, which makes the arrangement a transparent separation rather than a universal template.[^3]

Length is the wrong measure of quality here. A very long prompt can be contradictory or hard to prioritise, and a short one suffices where the relevant rules already stand in knowledge documents and instruction files, so a task prompt that points at the persistent holding rather than restating it stays compact. What a bounded formulation achieves is a reduction in the number of silent assumptions, and it guarantees no correct result.[^4]

Roles are a special case worth stating carefully. Assigning one can influence terminology, style, perspective and level of detail by making learned patterns of specialist communication more probable, and it adds no domain knowledge. A brief functional assignment and an elaborated persona with background, experience, goals and situation of use should be considered together without being treated as the same instrument, and roles remain useful where a task genuinely requires a particular perspective, audience or evaluative frame.[^5]

A synthetic persona produces hypotheses about users. It can make possible problems visible and define a consistent perspective from which an artefact is inspected, and its answers have to be checked against real people, observations or existing user research. Personas suit style variation, changes of perspective, early material critique, the preparation of interviews and the identification of likely queries, and they replace neither domain knowledge nor real stakeholders, empirical research or scholarly validation.[^6]

## Why prompting findings do not travel

The empirical literature on prompt effects is heterogeneous in a way that is itself the finding. Studies report effects of emotional additions, of politeness and of unusual automatically generated prompts, while other work shows that irrelevant additions degrade performance or that effects fail to replicate on newer models. A changed result after a variation does not show that the wording works for the reason assumed, and effects observed in one model generation may weaken, disappear or reverse in another.[^7] What produces this instability is the number of factors involved, model and version, task and dataset, language, the position and structure of the information, the evaluation metric and random variation.

Two consequences follow. The first is procedural. A prompt variant is an experimental intervention and is assessed like one, by fixing goal and metric, defining a baseline, changing only one relevant component, using several examples and repetitions, checking on new cases, documenting model and version, and assessing quality in the matter separately from style and format.[^8] The second is a limit on generalisation. No single strategy performs optimally across models, tasks and evaluation settings, so effective prompting is a combination of context selection, instruction design, inference strategy and evaluation rather than the discovery of one formulation.[^9]

A related discipline applies to output formats. Requiring a structured format reduces ambiguity, and the levels it can settle are limited. Syntactic conformance, structural completeness, semantic correctness and scholarly adequacy are separate questions, and a format requirement reaches the first two.[^10] Iteration helps for the same reason. A productive exchange runs through bounded passes of generating, checking, correcting and condensing, and separating the pass that finds defects from the pass that repairs them keeps each of them assessable.[^11]

## Where the prompt stops

Prompt Engineering makes a current task more precise. It cannot on its own resolve missing or inaccessible project knowledge, contradictory guidelines, unresolved requirements, an overloaded context, absent documentation, tool and permission management, technical tests or scholarly validation, and it does not organise a longer trajectory.[^12] Each of those is a different kind of problem, and a project that tries to solve them by rewording an instruction will produce longer instructions and the same defects.

The object of design therefore shifts. Complex work contains more relevant information than should enter a single prompt, because goals, documents, data, policies, requirements, examples, design decisions, previous findings, open questions and validation criteria all matter without mattering at the same time, and the design question moves from the wording of an instruction to what is available, how it is represented, in which order it appears, what can be retrieved and what is deliberately omitted.[^13]

There is one further reason to expect the shift, and it comes from chapter 1. If a prompt is an intervention in the computation the model is currently performing, then the whole sequence conditions that computation, and the instruction is one part of the sequence among the material, the examples and the accumulated history.[^14] Improving the instruction while leaving the rest unmanaged optimises a fraction of what actually determines the result.

## Gaps

Two topics of the outline are treated more thinly here than the outline intends.[^15]
- Prompt versioning is named in the outline and appears in the sources only inside the experimental procedure, as the requirement to document model and version. A practice of versioning prompts as project artefacts would need the Promptotyping document templates of the other manuscript lane.
- Zero-shot and few-shot prompting as named techniques do not appear in the feeding sources of this lane, which treat examples as one component of the input sequence without the terminology. The survey literature the sources cite would have to enter as a publication record before the terms can be used.

[^1]: Grounded in [[30_assertions/a-prompt-is-the-whole-input-sequence]].
[^2]: Grounded in [[30_assertions/prompt-engineering-is-iterative-design-and-evaluation]].
[^3]: Grounded in [[30_assertions/a-prompt-is-a-bounded-specification]].
[^4]: Grounded in [[30_assertions/precision-does-not-follow-from-length]].
[^5]: Grounded in [[30_assertions/role-assignment-adds-no-domain-knowledge]].
[^6]: Grounded in [[30_assertions/personas-produce-hypotheses]].
[^7]: Grounded in [[30_assertions/prompt-effects-are-local]].
[^8]: Grounded in [[30_assertions/prompt-variants-are-experimental-interventions]].
[^9]: Grounded in [[30_assertions/no-single-prompting-strategy-is-optimal]].
[^10]: Grounded in [[30_assertions/structured-output-has-four-levels-of-conformance]].
[^11]: Grounded in [[30_assertions/iteration-runs-in-bounded-passes]].
[^12]: Grounded in [[30_assertions/prompting-does-not-replace-work-organisation]].
[^13]: Grounded in [[30_assertions/the-object-shifts-to-the-information-state]].
[^14]: Grounded in [[30_assertions/prompting-intervenes-in-the-current-computation]].
[^15]: Posit: the gap list records where this chapter falls short of the outline. Open evidence question: whether the template set of the other manuscript lane carries a prompt-versioning practice or only document versioning.
