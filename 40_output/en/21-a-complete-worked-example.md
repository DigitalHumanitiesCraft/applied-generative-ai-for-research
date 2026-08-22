---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-failure-becomes-learning-only-through-interpretation]]", "[[30_assertions/a-finding-is-attributed-before-it-is-written-back]]", "[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/agent-instruction-documents-translate-knowledge-into-imperatives]]", "[[30_assertions/agentic-review-yields-probabilistic-evidence]]", "[[30_assertions/design-knowledge-stays-declarative]]", "[[30_assertions/deterministic-verification-is-bounded-by-its-checks]]", "[[30_assertions/exploration-scales-through-computational-profiling]]", "[[30_assertions/findings-arise-at-several-non-interchangeable-levels]]", "[[30_assertions/formal-modelling-does-not-determine-the-operational-form]]", "[[30_assertions/implementation-proceeds-through-bounded-inspectable-increments]]", "[[30_assertions/interaction-exposes-unwarranted-precision]]", "[[30_assertions/preparation-assembles-an-accessible-source-basis]]", "[[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]]", "[[30_assertions/the-accepted-state-must-remain-identifiable]]", "[[30_assertions/the-boundary-to-research-software-engineering]]", "[[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]]", "[[30_assertions/the-material-document-carries-epistemic-responsibility]]", "[[30_assertions/the-specification-holds-interlocked-questions-in-one-place]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]", "[[30_assertions/user-stories-bridge-scholar-centred-design-and-implementation]]", "[[30_assertions/verification-documents-are-adversarial-and-precede-the-claim]]", "[[30_assertions/write-back-makes-a-finding-durable]]"]
posits: 2
lang: en
part: "VI. Worked Example, Boundaries, and Implications"
chapter: 21
title: "A Complete Worked Example"
topic: "[[Boundaries-and-Implications]]"
feeding-sources: ["paper chapter 4", "hands-on chains from slides and script"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# A Complete Worked Example

## What this chapter carries and what the companion repository carries

The worked example follows one research project from its initial question to a published artefact. Detailed commands, files, prompts, screenshots, exercises, and alternative implementations belong to a companion repository rather than to the monograph, so this chapter sets out the chain, states what each step has to achieve, and names the properties the tutorial dataset has to have.[^1] Read this way the chapter is the specification of the example, and the repository is its execution.

The tutorial dataset has to carry genuine semantic complexity, missing values, uncertainty, several plausible research perspectives, and enough structure for deterministic processing.[^2] Each requirement earns its place. Semantic complexity and several plausible perspectives are needed because the same data may support different research questions and therefore require different operational forms, which is the situation the method exists for.[^3] Missing values and uncertainty are needed because the representation of what the data do not settle is where a technically possible visualisation most easily claims more than the records carry.[^4] Sufficient structure for deterministic processing is needed because the complete dataset is processed by inspectable operations outside the model context while profiles and selected examples enter the working context.[^5]

## The chain

The example proceeds in four movements that correspond to the four forms of work, and the steps within them are ordered without being a fixed sequence, since findings from implementation may return the work to any earlier form.[^6]

The first movement prepares. The research question is formulated, the users and scholarly activities are identified, and the data are inspected and profiled. Preparation brings the material into an accessible project environment and makes its status explicit, requiring accessibility for inspection and computational use with provenance and known limitations documented rather than normalisation or formal modelling.[^7] Profiling belongs to Exploration and follows the scale of the material, so a small tutorial dataset is examined directly while the same step on a large collection would be a script that extracts and aggregates structure across the corpus.[^5] Identifying users and activities produces the narrative form of the requirements, in which a role, a goal, and a benefit are named and later matched to a checkable expectation with an acceptance criterion.[^8]

The second movement distils. The Grounded Vault is created, and the maintained documents are written, meaning the material document that records what the data are, where they come from, how they are modelled, and where they stop carrying;[^9] the specification that holds requirements, scenarios, functional scope, and decisions in one place;[^10] the design document that records design stance and the treatment of uncertainty as declarative knowledge;[^11] the verification criteria that state what will be claimed and how a third party could refute it;[^12] and the action document that translates all of it into imperatives for the agent and carries no knowledge of its own.[^13] Distillation is finished when a new contributor or agent instance could reconstruct the project's logic and continue the work from these documents without undocumented explanation.[^14]

The third movement implements and diagnoses. A minimal artefact is generated, and the increments stay small enough that each establishes a runnable state comparable with the maintained knowledge before further assumptions are embedded.[^15] The artefact is then inspected for factual, conceptual, visual, and technical failures, and each failure is classified by the layer that produced it, because findings arise at several interacting but non-interchangeable levels and treating every problem as a code defect would conceal the decisions through which the artefact was produced.[^16] Attribution decides where the correction goes, since a finding about the represented domain requires a revision of the model or capture practice while a finding about how an adequate distinction is presented can stay in the design of the interface.[^17] The documents are then revised, which is the operation that makes a correction durable rather than local.[^18]

The fourth movement checks and closes. Deterministic validation runs first and settles the formally expressible conditions, reaching exactly as far as the properties its checks encode.[^19] Review by a model extends the scope and depth of inspection through a bounded, tool-supported investigation whose findings stay probabilistic evidence.[^20] Verification by the Critical Expert then decides whether the data are appropriately represented, whether the question is meaningfully addressed, whether uncertainty is treated adequately, and whether the output can be accepted as part of scholarly work.[^21] Publication follows with its provenance documentation, and the accepted state has to remain identifiable and reconstructable through a release, an archived deposit, or another durable reference.[^22] The final step decides between closure, maintenance, and handover to Research Software Engineering, which is a decision about obligations rather than about code, since the boundary is crossed when an artefact has to become durable, maintained, secure, accessible, institutionally operated, shared, integrated, or supported for third parties.[^23]

## What the example is for

An example of this kind demonstrates how to produce an artefact, and its more useful demonstration is how to diagnose why a generated artefact is wrong and where a persistent correction belongs.[^24] The first is a matter of following steps and can be read from any tutorial. The second is the competence the method actually requires, and it is visible only where a failure is followed from its symptom to the layer that produced it and then into the document that changes.

The closing acceptance is bounded like every other. A tutorial promptotype is accepted as a teaching artefact, and evaluating it separates technical conformity, scholarly adequacy, and suitability for that stated purpose, so an exploratory or teaching artefact need not satisfy production-level engineering criteria that lie outside its accepted scope.[^25]

## Gaps
- The dataset that carries the worked example is an open decision recorded in the project plan and in the topic map. Until it is fixed, this chapter states the required properties of the dataset and cannot run the chain on one.
- The paper describes no tutorial project, so the eighteen steps of the outline are grounded here through the general assertions about each form of work rather than through a documented instance.
- The hands-on chains of the lecture notes and the slide deck are named in the feeding map for Part VI and belong to the parallel writing lane, so no teaching version of the chain was available for comparison.
- The companion repository does not exist yet. What it has to contain follows from this chapter, and the decision to create it is an operator decision.

[^1]: Posit: splitting the worked example between a specification in the monograph and an execution in a companion repository follows the outline and keeps the book free of material that ages with a model version or a tool release. Open evidence question: whether readers can follow the chain from the specification alone, which only a trial with readers would show.
[^2]: Posit: the five required properties of the tutorial dataset are stated in the outline, and no source in this vault names a dataset that has them. Open evidence question: which openly available dataset satisfies all five at a size a reader can work through.
[^3]: Grounded in [[30_assertions/formal-modelling-does-not-determine-the-operational-form]].
[^4]: Grounded in [[30_assertions/interaction-exposes-unwarranted-precision]].
[^5]: Grounded in [[30_assertions/exploration-scales-through-computational-profiling]].
[^6]: Grounded in [[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]].
[^7]: Grounded in [[30_assertions/preparation-assembles-an-accessible-source-basis]].
[^8]: Grounded in [[30_assertions/user-stories-bridge-scholar-centred-design-and-implementation]].
[^9]: Grounded in [[30_assertions/the-material-document-carries-epistemic-responsibility]].
[^10]: Grounded in [[30_assertions/the-specification-holds-interlocked-questions-in-one-place]].
[^11]: Grounded in [[30_assertions/design-knowledge-stays-declarative]].
[^12]: Grounded in [[30_assertions/verification-documents-are-adversarial-and-precede-the-claim]].
[^13]: Grounded in [[30_assertions/agent-instruction-documents-translate-knowledge-into-imperatives]].
[^14]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
[^15]: Grounded in [[30_assertions/implementation-proceeds-through-bounded-inspectable-increments]].
[^16]: Grounded in [[30_assertions/findings-arise-at-several-non-interchangeable-levels]].
[^17]: Grounded in [[30_assertions/a-finding-is-attributed-before-it-is-written-back]].
[^18]: Grounded in [[30_assertions/write-back-makes-a-finding-durable]].
[^19]: Grounded in [[30_assertions/deterministic-verification-is-bounded-by-its-checks]].
[^20]: Grounded in [[30_assertions/agentic-review-yields-probabilistic-evidence]].
[^21]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^22]: Grounded in [[30_assertions/the-accepted-state-must-remain-identifiable]].
[^23]: Grounded in [[30_assertions/the-boundary-to-research-software-engineering]].
[^24]: Grounded in [[30_assertions/a-failure-becomes-learning-only-through-interpretation]].
[^25]: Grounded in [[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]].
