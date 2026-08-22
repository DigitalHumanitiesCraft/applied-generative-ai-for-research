---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-knowledge-base-is-tested-by-bounded-continuation-tasks]]", "[[30_assertions/a-public-deployment-is-the-latest-state-of-a-development-history]]", "[[30_assertions/an-artefact-alone-does-not-witness-its-own-history]]", "[[30_assertions/comparative-evaluation-asks-when-the-arrangement-adds-value]]", "[[30_assertions/data-governance-bounds-what-may-be-processed]]", "[[30_assertions/exploration-scales-through-computational-profiling]]", "[[30_assertions/independent-transfer-is-evaluated-through-sustained-work]]", "[[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]]", "[[30_assertions/proprietary-dependence-limits-durability]]", "[[30_assertions/the-accepted-state-must-remain-identifiable]]", "[[30_assertions/the-journal-is-a-curated-provenance-index]]", "[[30_assertions/the-method-was-consolidated-from-one-practice]]", "[[30_assertions/the-provenance-of-a-generated-process-is-documentary]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]", "[[30_assertions/transferability-differs-from-exact-reproduction]]"]
posits: 2
lang: en
part: "VI. Worked Example, Boundaries, and Implications"
chapter: 23
title: "Reconstructability, Sustainability, and Proprietary Dependence"
topic: "[[Boundaries-and-Implications]]"
feeding-sources: ["paper chapter 4", "hands-on chains from slides and script"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Reconstructability, Sustainability, and Proprietary Dependence

## Why identical regeneration cannot be assumed

Generative systems are stochastic and often proprietary, and recording prompts, data, and model names does not guarantee that a later run produces the same output. Model and harness changes may alter system behaviour even where the project knowledge and the research data stay stable, and the documented practice depends substantially on paid access to proprietary frontier models and capable agentic tools, which introduces direct costs, reduces control over system changes, and sits in tension with the inspectability, reproducibility, and durability sought for research software and data.[^1] The method acknowledges this in its own definition of an iteration, since a renewed implementation using another model, harness, or project state counts as a new iteration rather than as a reproduction of the earlier one.[^2]

The consequence is not that reproducibility becomes irrelevant. Deterministic parts of a workflow stay reproducible and should be kept that way, since the complete dataset is processed by inspectable operations while the generative component works on a distilled account and selected examples.[^17] What changes is which property can be promised for the whole process.

## Reconstructability

A research process is reconstructable when enough of its evidential basis, project knowledge, specifications, code, transformations, decisions, and verification history remain available for another person to understand and reproduce the logic of the work, even where the generated implementation is not byte-identical.[^3] The distinction from exact reproducibility is the same distinction the method already draws for transfer, in that another practitioner may apply the method and produce a different artefact with different documents, models, tools, and project structures, and what is required is that the core relations be established, applied, and reconstructed without undocumented intervention.[^4]

Two things follow. The first is where reconstructability lives. Where interaction logs are not retained, the persistent provenance of a generated process consists of the maintained project knowledge, the working record, the sources, the documented decisions, and the version history, and those materials make consequential stages inspectable while failing to reproduce every interaction, discarded alternative, or element of tacit judgement.[^5] A curated provenance record contributes exactly the part that code cannot, since it evidences per transition whether a result was integrated, discarded, or corrected.[^6] The artefact itself contributes least, because a runnable state establishes that it existed and which operations it offered and cannot establish its history, the decisions behind it, the findings written back, or the authority through which anything was accepted.[^7]

The second is that reconstructability is testable, which reproducibility of a stochastic process is not. A bounded continuation task puts an independent contributor in front of the maintained documents and the project resources and asks them to explain the project, diagnose a selected discrepancy, or continue a delimited implementation task, with observed difficulties attributed to documentary, technical, access-related, or competency-related limitations.[^8] That is the completion criterion of Distillation used as a measurement, and it turns a property that sounds like an aspiration into something a project can fail.[^9]

## What threatens it

Several conditions erode reconstructability, and they differ in whether a project can act on them. Model version changes and changing product behaviour alter what the same instruction produces, hidden system instructions make part of the effective context unavailable for inspection, proprietary models may become unavailable entirely, and service discontinuation removes the component a workflow was built around.[^1] Costs and access restrictions act more quietly, since a process that only a well-funded group can rerun is reconstructable in principle and not in practice, and the same practice that depends on paid frontier access has to say so as a condition of its own results.[^1]

Local and open-weight models are the obvious counter-move, and the documented practice does not establish how far the method remains effective with them.[^1] Recording that gap honestly matters more than closing it rhetorically, because an evaluation would have to treat model and harness as experimental variables rather than as invisible background conditions.[^10]

Against these, three measures are available now. The accepted state has to remain identifiable and reconstructable through a repository release, an archived deposit, or another durable reference, without requiring a particular hosting platform or versioning scheme.[^2] Outputs and intermediate states can be archived alongside the code they came from, which is what makes a public deployment readable as the latest inspectable state of a documented development history rather than as a finished thing.[^11] And provenance can be declared rather than implied, meaning that a published artefact states which models and tools were used, what was checked, by whom, and against what.[^5] Data governance sets the outer bound on all of this, since permissibility depends on the material and on legal, institutional, and architectural conditions, and consequential changes should stay inspectable and reversible.[^12]

## Sustainability preserves the knowledge, not only the code

Sustainability in this setting requires preserving the knowledge and the decisions from which code was derived alongside the code itself.[^13] The reason is visible in what each layer can answer. Preserved code answers what the artefact did. Preserved project knowledge answers why it did that, what the data support, and where the representation stops. An evaluation of an accepted state separates technical conformity, scholarly adequacy, and suitability for the stated purpose, and only the first of those three can be recovered from an executable alone.[^14]

The same reasoning bounds what preservation buys. The documented practice is subject to selection effects, since inspectable implementation states survived more systematically than abandoned experiments, which means a preserved record over-represents the paths that worked.[^15] A project that wants its record to carry the negative results has to preserve them deliberately, and the comparison that would show whether the whole arrangement adds value has to look past the first functional implementation to whether the artefact can still be examined, verified, maintained, revised, and transferred later.[^16]

## Gaps
- Reconstructability as defined here comes from the outline. The sources treat it through the identifiability of the accepted state and through proprietary dependence without giving the definition, which the topic map records as an open question.
- The enumeration of threats, from hidden system instructions to service discontinuation, follows the outline. The sources carry proprietary dependence and behavioural change under model and harness updates, so the individual items rest on that assertion.
- Publication strategies for a promptotype are named in the outline. The sources require a durable reference without prescribing a form, and which archival or publication route the book recommends is recorded as an open question in the topic map.
- The hands-on chains of the lecture notes and the slide deck feed Part VI and belong to the parallel writing lane.

[^1]: Grounded in [[30_assertions/proprietary-dependence-limits-durability]].
[^2]: Grounded in [[30_assertions/the-accepted-state-must-remain-identifiable]].
[^3]: Posit: the definition of reconstructability is taken from the book's own outline, and no source in this vault defines the term. Open evidence question: whether an established definition exists in the reproducibility literature that the book should adopt instead.
[^4]: Grounded in [[30_assertions/transferability-differs-from-exact-reproduction]].
[^5]: Grounded in [[30_assertions/the-provenance-of-a-generated-process-is-documentary]].
[^6]: Grounded in [[30_assertions/the-journal-is-a-curated-provenance-index]].
[^7]: Grounded in [[30_assertions/an-artefact-alone-does-not-witness-its-own-history]].
[^8]: Grounded in [[30_assertions/a-knowledge-base-is-tested-by-bounded-continuation-tasks]].
[^9]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
[^10]: Grounded in [[30_assertions/independent-transfer-is-evaluated-through-sustained-work]].
[^11]: Grounded in [[30_assertions/a-public-deployment-is-the-latest-state-of-a-development-history]].
[^12]: Grounded in [[30_assertions/data-governance-bounds-what-may-be-processed]].
[^13]: Posit: sustainability that preserves only the generated code preserves the answer and discards the question, because the reasons for a representation live in the maintained documents rather than in an executable. Open evidence question: a case in which a preserved codebase without its project knowledge was successfully continued by another team.
[^14]: Grounded in [[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]].
[^15]: Grounded in [[30_assertions/the-method-was-consolidated-from-one-practice]].
[^16]: Grounded in [[30_assertions/comparative-evaluation-asks-when-the-arrangement-adds-value]].
[^17]: Grounded in [[30_assertions/exploration-scales-through-computational-profiling]].
