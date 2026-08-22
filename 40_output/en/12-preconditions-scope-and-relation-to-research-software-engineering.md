---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-research-artefact-is-a-project-specific-operational-form]]", "[[30_assertions/acceptance-is-purpose-specific-and-bounded]]", "[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/data-governance-bounds-what-may-be-processed]]", "[[30_assertions/formal-modelling-does-not-determine-the-operational-form]]", "[[30_assertions/promptotyping-can-begin-from-three-project-conditions]]", "[[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]]", "[[30_assertions/the-boundary-to-research-software-engineering]]", "[[30_assertions/the-method-cannot-supply-missing-competence]]", "[[30_assertions/the-method-redistributes-implementation-labour]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]"]
posits: 1
lang: en
part: "IV. Promptotyping"
chapter: 12
title: "Preconditions, Scope, and Relation to Research Software Engineering"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Preconditions, Scope, and Relation to Research Software Engineering

## What has to be in place

A method that lowers the cost of implementation does not lower the cost of knowing what should be implemented. Promptotyping presupposes research material that is structured or sufficiently semi-structured to be made computationally explicit, since a digital research artefact is an operational form for working with such data towards a defined scholarly purpose.[^1] It presupposes scholarly expertise adequate to contextualise and evaluate that material, because the method supports the articulation, implementation, and revision of an understanding that already exists and cannot supply domain knowledge that practitioners do not possess or cannot recognise as relevant.[^2] Templates and maintained documents make assumptions more explicit and revisable, which is a different service from supplying the assumptions.[^2]

It presupposes a knowledge layer that can be inspected, and there is a practical test for whether one exists. A new contributor or agent instance, given the maintained documents and access to the project resources, should be able to reconstruct the current logic of the project and continue the assigned work without undocumented explanation.[^3] Where that fails, the layer is not yet what the method requires.

It presupposes the ability to formulate requirements, which in this setting means translating scholarly practice into statements that can guide implementation without losing their research purpose. And it presupposes the capacity to verify, since acceptance rests with a person or group competent and accountable for judging whether the project knowledge adequately represents the research material and whether the artefact suits its purpose.[^4] A project that cannot staff that judgement has no way to close an iteration.

Formal preparation of the data does not replace any of this. Modelling and FAIR preparation support machine-actionability, interoperability, and reuse, and they leave open how researchers should work with the data in a particular project, because the same data may support different questions and therefore require different operational forms.[^5] The two contrasting investigations that arose from one shared model of historical accounting transactions make the point concretely, since the interoperable representation supported both and determined neither.[^5]

## The gap the method addresses

Translating scholarly requirements into software has commonly involved collaboration between domain specialists and technical contributors, and that collaboration remains essential for artefacts requiring dependable long-term operation, institutional integration, security, or supported use by third parties. The expertise and resources it needs are not equally available to individual researchers and small projects.[^6] Promptotyping addresses the bounded capacity gap that opens between a researcher who can articulate domain knowledge and research requirements and the technical resources needed to realise a project-specific form.

The gap is bounded in both directions. On one side, the method has an entry condition rather than a starting point, and it can begin from an established research-data state, participate in the development of that state, or operationalise a prospective arrangement before a production corpus exists.[^7] On the other, the effort it addresses is redistributed rather than removed. An agent may produce an initial functional artefact rapidly, while domain specialists still specify requirements, examine outputs, interpret discrepancies, and determine what can be accepted, and Research Software Engineers may later refactor the implementation for dependable operation.[^8]

How much documentary work the method demands follows from what is being delegated. A bounded transformation on a stable and well-understood format may be guided by concise mappings and formal checks. Work that spans interpretation, modelling, implementation, and verification requires an explicit account of sources, assumptions, requirements, and limitations.[^9] The rule is proportionality, and applying the heavy form to the light case wastes exactly the capacity the method was meant to free.

## Where the method does not reach

Promptotyping is not a substitute for collaboration with Research Software Engineers or other technical specialists. Artefacts intended for dependable institutional or public operation continue to require expertise in security, accessibility, maintainability, integration, and sustained operation, and the method is inappropriate where contributors cannot reconstruct or assess the relation among sources, research data, maintained project knowledge, implementation, and output.[^6] Lowering the barrier to implementation is not a licence for artefacts whose grounds, limitations, responsibilities, and status cannot be made accountable.[^6]

A second boundary is legal and institutional rather than technical. The method provides no general licence to submit research material to external generative systems, permissibility depends on the material and on the applicable legal, institutional, and architectural conditions, restricted or personally identifiable material may require approved local processing or exclusion, agent access to project resources is bounded through controlled permissions and attributable actions, and purpose-specific scholarly acceptance does not replace institutional responsibility for secure, sustainable, and legally compliant operation.[^10]

A third boundary concerns competence and shows itself only after the fact. Inadequate project knowledge can guide an agent towards an implementation that is coherent and operational and remains inadequate in scholarly terms, which is why responsible application requires critical examination of the provenance, construction, scope, and representational limits of the data before the artefact is built rather than after it convinces.[^2]

## The transition to Research Software Engineering

The boundary is crossed when the obligations attached to an artefact change. An exploratory interface used by its author carries few of them. An artefact that has to be durable, maintained, secure, accessible, institutionally operated, shared across users, dependent on persistent server-side state, integrated into external infrastructure, or supported for third parties carries most of them at once, and each is a competence in its own right.[^6] The change is one of obligation rather than of size, so a small artefact can cross the boundary and a large one can stay inside it.

Purpose-specific acceptance makes the crossing legible. An iteration may be accepted as an experimental processing pipeline, an internal workflow, a proposal-stage demonstrator, or a handover state, and none of those acceptances claims production readiness.[^11] Where the accepted purpose changes to institutional operation, the artefact has entered the domain of Research Software Engineering whether or not its code changed.

Promptotyping Documents can make that handover more inspectable, because the receiving side finds research context, source and data descriptions, requirements, design decisions, verification concepts, known limitations, process history, and unresolved questions already written down rather than reconstructed from code.[^12] What they cannot do is remove the expertise and resources that sustainable research software requires.[^6]

## Gaps
- The composition of a handover package is stated in the outline and is not carried by a source in this vault. The chapter therefore treats it as the book's own conclusion; a grounded treatment would need the templates of a handover-oriented document set entered as source passages, or the lecture notes of the parallel lane.
- The list of obligations that mark the transition to Research Software Engineering comes from the exposé. The paper names the same obligations in prose without enumerating them, so the enumeration in this chapter follows the outline and rests on one assertion for its substance.
- Requirements Engineering as a precondition is described here in the method's own terms. A treatment that cites the requirements-engineering literature directly would need those publications registered as sources.

[^1]: Grounded in [[30_assertions/a-research-artefact-is-a-project-specific-operational-form]].
[^2]: Grounded in [[30_assertions/the-method-cannot-supply-missing-competence]].
[^3]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
[^4]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^5]: Grounded in [[30_assertions/formal-modelling-does-not-determine-the-operational-form]].
[^6]: Grounded in [[30_assertions/the-boundary-to-research-software-engineering]].
[^7]: Grounded in [[30_assertions/promptotyping-can-begin-from-three-project-conditions]].
[^8]: Grounded in [[30_assertions/the-method-redistributes-implementation-labour]].
[^9]: Grounded in [[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]].
[^10]: Grounded in [[30_assertions/data-governance-bounds-what-may-be-processed]].
[^11]: Grounded in [[30_assertions/acceptance-is-purpose-specific-and-bounded]].
[^12]: Posit: a handover package assembled from the maintained documents makes the receiving side's reconstruction cheaper, because the material it would otherwise have to infer from code is already written for inspection. Open evidence question: a documented handover in which a receiving team recorded what the maintained documents answered and what it still had to reconstruct.
