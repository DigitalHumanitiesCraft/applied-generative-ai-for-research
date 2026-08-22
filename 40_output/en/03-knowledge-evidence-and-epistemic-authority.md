---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/acceptance-is-a-purpose-bound-decision]]", "[[30_assertions/agents-produce-evidence-without-authority]]", "[[30_assertions/fluency-is-not-fidelity-to-the-source]]", "[[30_assertions/formal-conformance-is-not-scholarly-adequacy]]", "[[30_assertions/independent-review-extends-coverage-not-authority]]", "[[30_assertions/model-output-is-a-candidate-representation]]", "[[30_assertions/model-output-stays-probabilistic]]", "[[30_assertions/parametric-knowledge-carries-no-provenance]]", "[[30_assertions/self-revision-is-no-independent-verification]]", "[[30_assertions/social-fluency-is-no-evidence-of-authority]]", "[[30_assertions/sycophancy-needs-a-procedural-countermeasure]]", "[[30_assertions/the-assessment-vocabulary-has-four-levels]]", "[[30_assertions/the-capability-profile-is-jagged]]", "[[30_assertions/the-critical-expert-designs-the-conditions]]", "[[30_assertions/the-epistemic-infrastructure-conditions-inspection]]", "[[30_assertions/the-model-boundary-is-not-the-system-boundary]]"]
posits: 2
lang: en
part: "I. Generative Models as Research Systems"
chapter: 3
title: "Knowledge, Evidence, and Epistemic Authority"
topic: "[[Generative-Models]]"
feeding-sources: ["script chapter 2", "slide section AI Agents"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Knowledge, Evidence, and Epistemic Authority

## What a model can be said to know

The verb causes most of the trouble. Saying that a model knows something suggests a relation between a claim and the grounds for it, and the relation a model actually stands in is different. Training changes parameters so that statistical structure from the data influences later generation, no addressable version of a training document remains, and a model can therefore describe a matter accurately while being unable to name the source from which the description was learned.[^1] What sits in the parameters is unusable as evidence, however accurate it happens to be.

Three information layers have to be kept apart for the question to become tractable, the learned representations in the parameters, the retrievable information in external resources, and the information present in the current context. The boundary of the model is not the boundary of the system, so what a system can support with evidence depends on which layer supplied the claim.[^2] A claim from the third layer can be traced to its passage, a claim from the second to its retrieval, and a claim from the first to nothing.

That last case is where the material of this book takes its shape. A generated text that reads well is no report of what the sources say. Fluency, grammaticality and internal coherence carry no information about fidelity to the source, and a transcription can read convincingly while individual readings are wrong.[^3] The practical consequence is a rule about status. Any output stands as a candidate representation whose next step is comparison with the material it claims to represent, because plausibility is not validation.[^4]

## The risks that follow

Several risks in this arrangement have a common shape. The output is probabilistic, so the same input can produce different results and a plausible formulation is no reconstructed fact.[^5] Outputs can carry claims that nothing supports, models can reproduce bias, and a system can align an answer with a belief the user has expressed, all while the internal computation stays only partially understood.[^6] Social competence makes each of these harder to notice. Confidence, empathy and conversational fluency are properties of an assistant character stabilised through training and product design, and none of them says anything about whether the claims inside an answer hold.[^7]

Agreement bias in particular cannot be answered by asking better. It has to be answered in the procedure, by requiring evidence, alternatives or independent critical review wherever agreement with a stated position could shape the result, and by producing independent candidates, inspecting their differences and adjudicating between them.[^8] The same reasoning explains why a model checking its own work does not close the loop. Self-revision can make errors visible and provides no independent verification, because the same system can overlook its own false assumptions or justify them plausibly after the fact, and what makes it more reliable are explicit criteria, external tests and checkable references outside the model.[^9]

The loss of provenance deserves separate mention, because it is the risk that does the most damage quietly. A well-formed answer that has assimilated an unattributed claim looks exactly like a well-formed answer that has not, and the difference becomes visible only where the claim is followed back. This is the reason the vault behind this book anchors every substantive sentence to a passage, and the reason the anchoring has to be mechanical rather than remembered.[^10]

## Four kinds of assessment

Once outputs are treated as candidates, assessment has to be organised. Four forms of it are distinguishable and are frequently confused. Evaluation measures outputs, models or workflows against explicit criteria and may be quantitative or qualitative. Technical verification asks after conformance with formalised requirements and can often be automated for exactly that reason. Scholarly validation asks whether a representation is adequate to source, purpose and disciplinary context. Acceptance is the decision to use an identified state for a stated purpose, and it remains necessary after the other three have run.[^11]

The second and third of these come apart in a way that matters. Valid syntax proves that the syntax is right and schema conformance proves that the formal rules were kept, while whether a transcription corresponds to its source, whether editorial uncertainty is represented adequately, whether an interface supports the intended interpretative actions and whether modelling decisions are made visible or naturalised are questions of another kind. An artefact can pass every formal check and fail all of them.[^12]

Acceptance therefore has to name its purpose. A technically verified artefact can be scholarly unsuitable, and a scholarly interesting demonstrator can be unfit for publication, so an acceptance that does not state what it accepts the state for asserts more than the evidence carries.[^13]

## Where the authority sits

Agents and validators can localise errors, apply criteria, report differences and assemble evidence, and none of that transfers the decision. Expertise is not removed by this arrangement, it moves, to defining purposes, externalising the relevant knowledge, establishing modelling distinctions, setting constraints, designing evaluation criteria and deciding how a piece of evidence affects the status of an output.[^14]

The role that carries this is the Critical Expert. It holds the judgment wherever checking requires knowledge of the sources, interpretation or a design decision, and it decides which reading is defensible, whether a modelling corresponds to the source, whether a surface preserves scholarly distinctions and whether a state is accepted for its purpose. It is a responsible authority in a project rather than a particular person, and its work includes provenance, validation rules, acceptance criteria and procedures for handling uncertainty.[^15] Reading the role as a final human checkpoint mistakes its position in the workflow, because most of what it does happens before anything is generated.

Multiplying reviewers does not substitute for it. Several independent reviewers can expose disagreement and locate suspicious cases, and the evidence returned by schemas, tests, source comparisons and domain knowledge stays more important than agreement among them, so the purpose of orchestrating several instances is a structured trajectory of independent work rather than a larger number of model calls.[^16]

What makes any of this possible is an arrangement rather than a component. Files, project knowledge, schemas, tests, provenance information, model outputs and editorial decisions together establish the conditions under which a generated representation can be criticised, validated and accepted for a purpose, and the question a project has to answer is under which technical and epistemic conditions its outputs can be inspected and used.[^17] Part II builds that arrangement, and Part III organises the work that runs inside it.

## Gaps

Three of the risks the outline names for this chapter cannot be treated at the level the outline implies.[^18]
- Confabulation appears in the sources as a listed property without a definition that separates it from ordinary error, so the chapter states the probabilistic and unsupported-claim properties and avoids the term as a technical one.
- Uncalibrated confidence is treated here through the social-fluency assertion, which is about the manner of an answer, and a claim about calibration in the strict sense needs a source that measures stated confidence against accuracy.
- Conventional but inappropriate representations, named in the outline, has no anchor in these sources. The vault document withheld from this run would be one candidate, and the comparative cases of Part V are the other; until then the topic stays with chapter 17.

[^1]: Grounded in [[30_assertions/parametric-knowledge-carries-no-provenance]].
[^2]: Grounded in [[30_assertions/the-model-boundary-is-not-the-system-boundary]].
[^3]: Grounded in [[30_assertions/fluency-is-not-fidelity-to-the-source]].
[^4]: Grounded in [[30_assertions/model-output-is-a-candidate-representation]].
[^5]: Grounded in [[30_assertions/model-output-stays-probabilistic]].
[^6]: Grounded in [[30_assertions/the-capability-profile-is-jagged]].
[^7]: Grounded in [[30_assertions/social-fluency-is-no-evidence-of-authority]].
[^8]: Grounded in [[30_assertions/sycophancy-needs-a-procedural-countermeasure]].
[^9]: Grounded in [[30_assertions/self-revision-is-no-independent-verification]].
[^10]: Posit: the claim that unattributed assimilation is invisible in a well-formed answer follows from the provenance and fluency assertions and is measured in no source. Open evidence question: how often readers detect an unsupported claim in a fluent generated text without following it back.
[^11]: Grounded in [[30_assertions/the-assessment-vocabulary-has-four-levels]].
[^12]: Grounded in [[30_assertions/formal-conformance-is-not-scholarly-adequacy]].
[^13]: Grounded in [[30_assertions/acceptance-is-a-purpose-bound-decision]].
[^14]: Grounded in [[30_assertions/agents-produce-evidence-without-authority]].
[^15]: Grounded in [[30_assertions/the-critical-expert-designs-the-conditions]].
[^16]: Grounded in [[30_assertions/independent-review-extends-coverage-not-authority]].
[^17]: Grounded in [[30_assertions/the-epistemic-infrastructure-conditions-inspection]].
[^18]: Posit: the gap list records what this chapter cannot support from its own sources. Open evidence question: whether an operator decision to release the withheld vault document changes what the chapter can say about conventional representations.
