---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/amplification-rather-than-transfer-of-authority]]", "[[30_assertions/an-individual-account-is-not-evidence-for-others]]", "[[30_assertions/capable-systems-widen-the-span-between-production-and-acceptance]]", "[[30_assertions/critical-expert-verification-records-who-is-responsible]]", "[[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]]", "[[30_assertions/data-governance-bounds-what-may-be-processed]]", "[[30_assertions/deterministic-verification-is-bounded-by-its-checks]]", "[[30_assertions/no-claim-about-environmental-efficiency]]", "[[30_assertions/the-artefact-produces-no-knowledge-on-its-own]]", "[[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]]", "[[30_assertions/the-boundary-to-research-software-engineering]]", "[[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]]", "[[30_assertions/the-method-cannot-supply-missing-competence]]", "[[30_assertions/the-provenance-of-a-generated-process-is-documentary]]", "[[30_assertions/the-significance-is-modal-rather-than-economic]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]"]
posits: 3
lang: en
part: "VI. Worked Example, Boundaries, and Implications"
chapter: 24
title: "Amplification, Responsibility, and the Limits of Externalisation"
topic: "[[Boundaries-and-Implications]]"
feeding-sources: ["paper chapter 4", "hands-on chains from slides and script"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Amplification, Responsibility, and the Limits of Externalisation

## What is externalised

Promptotyping externalises part of the translation between scholarly knowledge and computational implementation. Maintained documents hold what the project takes to be the case, an agent implements from them, and the result is examined against the sources and written back. What the arrangement moves out of a person's head and into an inspectable form is the account of the data, the requirements, the representational decisions, and the criteria of assessment.

The limit of that move is stated in the method itself. The maintained documents support the articulation, implementation, and revision of an understanding that already exists, and they cannot supply domain knowledge that practitioners do not possess or cannot recognise as relevant.[^1] The completion criterion of Distillation measures the documents against a task rather than against completeness, since a new contributor or agent instance should be able to reconstruct the project's logic and continue the work, and difficulties in doing so reveal omissions.[^2] Nothing in that criterion promises that everything relevant has been written down.

Some of what remains resists documentation by its nature. Familiarity with a corpus built over years, sensitivity to the exceptional source that does not fit the schema, awareness of which disciplinary debate a modelling choice enters, and the recognition that a plausible alternative is missing from a set of options are competences that show themselves in judgements rather than in rules.[^3] The documentary record of a generated process registers this indirectly, since the maintained knowledge, the working record, the sources, the decisions, and the version history make consequential stages inspectable while failing to reproduce every discarded alternative or element of tacit judgement.[^4]

## Amplification rather than automation

The position the method takes is that the contribution of language-model-based agents to scholarly work is amplification, and that the scholarly competence and accountable judgement it presupposes stay indispensable.[^5] Read as an empirical claim, that position is modest, since the documented cases do not show that the method produces artefacts faster, more cheaply, or more reliably than alternative approaches, and what they show is that forms of project-specific implementation previously outside the practical resources of individual researchers and small projects became workable at all.[^6]

What is amplified can be named with some precision. Maintained project knowledge carries a project's understanding across sessions and across the boundary between people and agents, requirements and design decisions become reusable because they are written where they can be found, implementation stays inspectable because the increments are versioned and comparable against the documents, and the reduced cost of a first working implementation makes alternative computational forms available for comparison rather than for speculation.[^7] The reach of a practitioner who can articulate both a scholarly requirement and a technical constraint extends furthest, which is the mechanism behind the uneven distribution of the benefit.[^8]

What is not amplified is equally definite. The method cannot replace scholarly expertise, source criticism, or data modelling, because it operates on what those produce.[^1] It cannot replace formal validation, since deterministic checks reach exactly as far as the properties they encode and someone has to decide which properties matter.[^9] It cannot replace security engineering, accessibility work, maintenance, or institutional governance, since those are the obligations that mark the boundary to Research Software Engineering.[^10] And it cannot replace the responsibility for published claims.[^5]

An asymmetry runs through all of this and grows rather than shrinks. As the volume, scope, and plausibility of delegable work increase, the distance between what agents can produce and what scholars can responsibly accept widens, and maintained knowledge, differentiated checking, write-back, and purpose-specific acceptance are the means by which that distance stays governable.[^11] Capable systems therefore raise the value of the arrangement rather than making it redundant.

## Where responsibility sits

Responsibility follows from acceptance and publication.[^12] It does not follow from having produced something by hand. That is worth stating because the intuition runs the other way, and because a workflow in which most of the code was generated invites the assumption that responsibility was generated with it.

The method locates responsibility precisely. Acceptance rests with the Critical Expert, the person or group competent and accountable for judging whether the project knowledge adequately represents the research material and whether the artefact suits its purpose, and an agent may contribute proposals and assessments without assuming responsibility for their adequacy.[^13] Verification by that role records who assumes responsibility for the resulting judgement, which turns an abstract accountability into a name against a date.[^14] Distribution across people changes who holds which part and transfers nothing, and distribution across agents changes the coordination while keeping assignments, permissions, and outputs auditable.[^15]

Two further limits bound what acceptance can mean. Purpose-specific scholarly acceptance does not replace institutional responsibility for secure, sustainable, and legally compliant operation, and permissibility of the material and the workflow is decided outside the method.[^16] And an artefact accepted for a stated purpose makes no claim beyond it, which is why an examination has to ask whether relevant alternatives were excluded, whether conventions were reproduced without justification, and whether absences were concealed by an artefact that looks coherent.[^17]

## The honest form of the claim

Two statements have to stand together at the end of this part. The arrangement described in this book made certain work possible for practitioners who could not previously do it, and the evidence for its effects is thin by design rather than by neglect. The resource question is open, since the resource use of models, repeated generations, deployment architectures, and alternative workflows was not comparatively measured, and reduced development effort is therefore no evidence of reduced consumption.[^18] The experience question is open in the same way, since an author's account of an amplified working process describes how one person organised the work and is not evidence about others.[^19]

Holding both of those in view is what keeps the method a method. An artefact produces no scholarly knowledge on its own, and its epistemic relevance arises through operationalisation, examination, interpretation, attribution, and write-back.[^20] The same applies to the arrangement that produces artefacts.

## Gaps
- The list of what resists documentation, from tacit corpus familiarity to the recognition of absent alternatives, comes from the outline. The sources name tacit judgement as something the record cannot reproduce without enumerating its forms, so the enumeration is carried here as the book's own.
- The lists of what the method amplifies and what it cannot replace likewise come from the outline. Each item is grounded here in the assertion that carries it, and the lists themselves are the book's arrangement.
- The hands-on chains of the lecture notes and the slide deck feed Part VI and belong to the parallel writing lane, so the teaching perspective on responsibility is absent from this chapter.

[^1]: Grounded in [[30_assertions/the-method-cannot-supply-missing-competence]].
[^2]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
[^3]: Posit: the four forms of competence named here are the book's own specification of what the sources call tacit judgement, and no source enumerates them. Open evidence question: whether continuation studies can distinguish failures caused by undocumented tacit knowledge from failures caused by documentary omission.
[^4]: Grounded in [[30_assertions/the-provenance-of-a-generated-process-is-documentary]].
[^5]: Grounded in [[30_assertions/amplification-rather-than-transfer-of-authority]].
[^6]: Grounded in [[30_assertions/the-significance-is-modal-rather-than-economic]].
[^7]: Posit: the four things named as amplified follow from the mechanisms the preceding chapters establish, meaning maintained knowledge across sessions, written requirements and decisions, versioned inspectable increments, and a lowered cost of a first implementation. Open evidence question: whether any of the four can be measured against a comparison condition that does not use the method.
[^8]: Grounded in [[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]].
[^9]: Grounded in [[30_assertions/deterministic-verification-is-bounded-by-its-checks]].
[^10]: Grounded in [[30_assertions/the-boundary-to-research-software-engineering]].
[^11]: Grounded in [[30_assertions/capable-systems-widen-the-span-between-production-and-acceptance]].
[^12]: Posit: locating responsibility at acceptance and publication rather than at manual production follows from the method placing acceptance with an accountable role and recording who assumes it. Open evidence question: whether research institutions attribute responsibility the same way where an output was largely generated.
[^13]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^14]: Grounded in [[30_assertions/critical-expert-verification-records-who-is-responsible]].
[^15]: Grounded in [[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]].
[^16]: Grounded in [[30_assertions/data-governance-bounds-what-may-be-processed]].
[^17]: Grounded in [[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]].
[^18]: Grounded in [[30_assertions/no-claim-about-environmental-efficiency]].
[^19]: Grounded in [[30_assertions/an-individual-account-is-not-evidence-for-others]].
[^20]: Grounded in [[30_assertions/the-artefact-produces-no-knowledge-on-its-own]].
