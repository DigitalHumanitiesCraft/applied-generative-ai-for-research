---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/acceptance-is-a-purpose-bound-decision]]", "[[30_assertions/agents-produce-evidence-without-authority]]", "[[30_assertions/an-early-error-propagates-along-the-trajectory]]", "[[30_assertions/findings-must-be-written-back]]", "[[30_assertions/formal-conformance-is-not-scholarly-adequacy]]", "[[30_assertions/implementation-tests-the-project-understanding]]", "[[30_assertions/increments-must-stay-inspectable]]", "[[30_assertions/independent-review-extends-coverage-not-authority]]", "[[30_assertions/long-runs-accumulate-noise]]", "[[30_assertions/more-agents-raise-coordination-cost]]", "[[30_assertions/self-revision-is-no-independent-verification]]", "[[30_assertions/the-assessment-vocabulary-has-four-levels]]", "[[30_assertions/the-bottleneck-shifts-from-model-to-context]]", "[[30_assertions/the-interface-can-manufacture-false-certainty]]", "[[30_assertions/the-prompt-is-one-component-of-the-loop]]"]
posits: 5
lang: en
part: "III. Agentic Research Work"
chapter: 10
title: "Failure, Drift, and Verification Debt"
topic: "[[Agentic-Work]]"
feeding-sources: ["script chapter 6", "slide sections Agentic Engineering and Workflows"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Failure, Drift, and Verification Debt

## Failures that wording cannot reach

The failures treated here survive better instructions. They arise from the length of a trajectory, from the arrangement around the model and from the way results are accepted, and each of them is a property of the workflow rather than of a single call.[^0]

The first is propagation. With growing task duration the number of places at which an error can enter later steps rises alongside the possible output, and an agent that reads an outdated guideline can produce an unsuitable pattern, transform it and adapt everything downstream to the wrong structure, so each single step looks correct while the original defect travels to the end.[^1] Nothing in the run reports this, because every local check passes.

The second is accumulation. A long run gathers outputs, errors, tool results and earlier decisions, and in one undifferentiated context the agent can spend substantial effort navigating its own history, which is why stable knowledge belongs outside the transient conversation, relevant parts are loaded when needed, and completed stages leave compact artefacts that later stages consume instead of every token being carried forward.[^2] The same mechanism appears from the other side in the context layer. Performance degrades well below the nominal window limit, noise accumulates, the reasoning budget is finite, and with growing autonomy the bottleneck moves from the model to the context.[^3]

The third is a failure of the surface. An interface can present uncertainty as settled, so the questions to ask of a running artefact are whether uncertainties appear as uncertainties, whether the surface produces false unambiguity, which modelling problems become visible only there and which documents must be revised as a result. Every stage from source through transcription, data model and transformation to display carries decisions about which differences become visible, editable and interpretable, and an agent cannot take over responsibility for them.[^4]

## Why the layer matters more than the symptom

A defect that shows up in an artefact rarely belongs where it shows up. Implementation is a form of investigation rather than neutral execution, because a missing rule or a modelling that is too coarse can become visible only through the working artefact, and a frontend can force a distinction the data model collapses. Requirements often cannot be completely specified before implementation, so a provisional artefact makes assumptions and limitations visible and lets alternative operationalisations be compared, while the consequential judgments stay with the domain experts.[^5]

The diagnostic question is therefore which layer a correction belongs in. A visible defect may originate in the implementation, in the action instructions, in the requirements, in the understanding of the data, in the preparation of the sources or in the research question itself, and repairing it at the layer where it appeared leaves the cause in place.[^6] Findings do not become project knowledge by being produced, they are inspected and, where warranted, returned into the maintained holding, which is what prevents relevant knowledge from remaining only in the chat, in the code or in the memory of individuals.[^7]

This is the point at which the whole arrangement closes. The prompt is one operational component of a cycle that runs from project knowledge through a working context and an implementation to a checking step that revises the project knowledge, and artefact and documented understanding develop together.[^8] A project that repairs code without returning findings keeps the cycle open, and each subsequent run starts from an understanding the previous run has already shown to be wrong.[^9]

## Self-checking and its limits

Two properties of the systems described in Part I keep reappearing here. Self-revision by the producing model can make errors visible and provides no independent verification, because the same system can overlook its own false assumptions or justify them plausibly after the fact, and what makes it more reliable are explicit criteria, external tests and checkable references outside the model.[^10] Agents and validators can localise errors, apply criteria, report differences and assemble evidence, and none of that transfers the decision to accept a result.[^11]

Adding reviewers extends coverage rather than authority. Independent instances expose disagreement and locate suspicious cases, and the evidence returned by schemas, tests, source comparisons and domain knowledge stays more important than agreement among them.[^12] Each added instance also costs something, because more agents create more handoffs, divergent assumptions and points of failure.[^13]

The countermeasure that does work is procedural. Increments stay inspectable when they can be run, belong to a defined project state, can be checked against requirements and are small enough that a cause can be reconstructed, and the material that would otherwise vanish, plans, decisions, check results and open questions, goes into persistent artefacts.[^14]

## Verification debt

The term this book uses for what accumulates is verification debt, the body of generated work that has been accepted provisionally and not yet examined at the level that scholarly or operational use requires.[^15] It behaves like other forms of technical debt in one respect and differs in another. It grows silently, because a provisional acceptance leaves no trace in the artefact, and unlike an unrefactored module it can invalidate a claim rather than slow a change.

Two things make it measurable in principle. Acceptance is a purpose-bound decision, so a state accepted for one purpose and used for another is a debt that has already come due, and naming the purpose at the moment of acceptance is what turns an implicit debt into a recorded one.[^16] The four assessment levels then say what has actually been done, whether an artefact was evaluated against criteria, verified against formalised requirements, validated as adequate to source and purpose, and accepted for a stated use.[^17] A project that records which of the four ran on which state can read its debt off the record.

Formal conformance is where the debt most often hides. Valid syntax proves the syntax and schema conformance proves the formal rules, while whether a transcription corresponds to its source, whether uncertainty is represented adequately, whether an interface supports the intended interpretative actions and whether modelling decisions are naturalised are questions of another kind, and an artefact can pass every formal check and fail all of them.[^18]

## Gaps

Four of the failure modes the outline lists have no anchor in the sources of this lane, and the central term of the chapter is a coinage.[^19]
- Implementation drift, uncontrolled dependency growth, overengineering and automation bias are named in the outline and appear in none of the three sources. The comparative cases of Part V are where they would acquire evidence, and until then the chapter treats propagation, accumulation and false certainty in their place.
- Verification debt is this book's term. No source of this lane uses it, and its definition here is assembled from the assertions on purpose-bound acceptance and the four assessment levels.
- The diagnostic procedure for assigning a defect to a layer is stated as a question and not as a method. The document typology of the other manuscript lane carries a diagnostic grid that routes a defect to a responsible document, and chapter 15 is where the two meet.
- Unauthorised classification, which the outline lists among the failure modes, is treated here only through the interface that manufactures false certainty. A case in which a generated classification enters a dataset without authorisation belongs to Part V.

[^0]: Posit: grouping these failures by their origin in trajectory length, arrangement and acceptance is this book's own classification, and no source of this lane orders them that way. Open evidence question: whether a set of documented agentic failures falls into these three groups or requires further ones.
[^1]: Grounded in [[30_assertions/an-early-error-propagates-along-the-trajectory]].
[^2]: Grounded in [[30_assertions/long-runs-accumulate-noise]].
[^3]: Grounded in [[30_assertions/the-bottleneck-shifts-from-model-to-context]].
[^4]: Grounded in [[30_assertions/the-interface-can-manufacture-false-certainty]].
[^5]: Grounded in [[30_assertions/implementation-tests-the-project-understanding]].
[^6]: Posit: the layered diagnosis is the outline's own, and the sources establish that a defect can originate outside the implementation without giving a procedure for locating it. Open evidence question: a set of documented defects classified by the layer their correction actually required.
[^7]: Grounded in [[30_assertions/findings-must-be-written-back]].
[^8]: Grounded in [[30_assertions/the-prompt-is-one-component-of-the-loop]].
[^9]: Posit: the claim that an unclosed cycle makes each run start from a refuted understanding follows from the write-back assertion and is measured in no source. Open evidence question: how often a repeated defect in a project traces back to a finding that was never written back.
[^10]: Grounded in [[30_assertions/self-revision-is-no-independent-verification]].
[^11]: Grounded in [[30_assertions/agents-produce-evidence-without-authority]].
[^12]: Grounded in [[30_assertions/independent-review-extends-coverage-not-authority]].
[^13]: Grounded in [[30_assertions/more-agents-raise-coordination-cost]].
[^14]: Grounded in [[30_assertions/increments-must-stay-inspectable]].
[^15]: Posit: verification debt is this book's coinage for the accumulation of provisionally accepted generated work, and no source of this lane uses the term. Open evidence question: a measure of how much unexamined generated output a project is carrying at a given moment.
[^16]: Grounded in [[30_assertions/acceptance-is-a-purpose-bound-decision]].
[^17]: Grounded in [[30_assertions/the-assessment-vocabulary-has-four-levels]].
[^18]: Grounded in [[30_assertions/formal-conformance-is-not-scholarly-adequacy]].
[^19]: Posit: the gap list records what this chapter cannot support from its own sources. Open evidence question: whether the comparative cases of Part V supply documented instances of drift, dependency growth, overengineering and automation bias.
