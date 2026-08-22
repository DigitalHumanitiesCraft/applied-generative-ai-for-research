---
type: moc
topic: "Generative-Models"
created: 2026-08-22
updated: 2026-08-22
---

# MOC: Generative-Models

Assertions on what a generative model is as a research system, covering its operation, the system it is embedded in, and the standing of what it produces. The topic carries Part I of the manuscript.

- [[30_assertions/llm-computes-next-token-probabilities]] — the autoregressive operation of a language model
- [[30_assertions/training-objective-differs-from-acquired-capability]] — why the optimisation problem and the acquired capability are not the same thing
- [[30_assertions/model-output-stays-probabilistic]] — stochastic variation as a property of the procedure
- [[30_assertions/fluency-is-not-fidelity-to-the-source]] — why the readability of an output says nothing about its correctness
- [[30_assertions/model-output-is-a-candidate-representation]] — the status a generated output has before it is checked
- [[30_assertions/parametric-knowledge-carries-no-provenance]] — why parametric knowledge cannot supply evidence for its own claims
- [[30_assertions/the-model-boundary-is-not-the-system-boundary]] — the three layers from which a system draws information
- [[30_assertions/tokenisation-fixes-the-unit-of-computation]] — the discrete unit that computation and context budget are counted in
- [[30_assertions/representations-are-contextual-not-fixed]] — why the same token does not carry the same representation twice
- [[30_assertions/attention-relates-positions-across-layers]] — the architectural mechanism behind context dependence
- [[30_assertions/prompting-intervenes-in-the-current-computation]] — the sense in which a prompt acts on the model
- [[30_assertions/pretraining-and-posttraining-are-distinguishable-and-blurred]] — what the training stages separate and where the separation blurs
- [[30_assertions/in-context-adaptation-changes-no-weights]] — why context is a design surface although nothing is learned
- [[30_assertions/the-assistant-is-a-stabilised-character]] — what the figure in the interface is and is not
- [[30_assertions/assistant-behaviour-has-three-shaping-layers]] — the three points at which provider decisions reach observable behaviour
- [[30_assertions/social-fluency-is-no-evidence-of-authority]] — the gap between the manner of an answer and its standing
- [[30_assertions/the-capability-profile-is-jagged]] — the uneven capability profile and the properties behind it
- [[30_assertions/capability-evaluations-measure-different-things]] — why benchmark results do not add up to one number
- [[30_assertions/automation-claims-are-self-descriptions]] — how to read a laboratory's statement of intent
- [[30_assertions/frontier-models-amplify-asymmetrically]] — the author's account of where amplification concentrates
- [[30_assertions/the-latent-program-space-models-prompt-effects]] — the theoretical model this book adopts for prompt effects
- [[30_assertions/interpretability-shows-structure-without-a-theory]] — what interpretability research does and does not establish
- [[30_assertions/prompt-engineering-is-an-external-search]] — prompting as search rather than formulation
- [[30_assertions/agentic-capability-arises-from-the-compound-system]] — the unit of analysis for what a system can do
- [[30_assertions/the-harness-is-the-technical-layer-of-action]] — what the harness is and what it governs
- [[30_assertions/the-harness-supplies-no-scholarly-authority]] — the limit of what technical control settles
- [[30_assertions/harness-quality-changes-what-can-be-evaluated]] — why the runtime substrate belongs in the evaluation
- [[30_assertions/tool-use-changes-the-epistemic-structure]] — what tools add beyond capability
- [[30_assertions/vision-language-models-fail-plausibly]] — the characteristic failure mode of multimodal transcription
- [[30_assertions/probabilistic-and-deterministic-operations-combine]] — the division of labour between generation and deterministic checking
- [[30_assertions/model-choice-is-a-system-choice]] — the dimensions a model decision actually settles
- [[30_assertions/applied-generative-ai-is-an-application-field]] — the definition of the field this book works in
- [[30_assertions/research-data-are-constructed-representations]] — the constructed character of the material a project works from
- [[30_assertions/ai-readiness-is-a-property-of-documentation]] — what makes a dataset usable in a model-supported workflow
- [[30_assertions/the-assessment-vocabulary-has-four-levels]] — the four levels of assessment and what each settles
- [[30_assertions/formal-conformance-is-not-scholarly-adequacy]] — the boundary between formal checking and scholarly judgment
- [[30_assertions/acceptance-is-a-purpose-bound-decision]] — what makes an acceptance statement meaningful
- [[30_assertions/the-critical-expert-designs-the-conditions]] — what the responsible scholarly authority actually does
- [[30_assertions/agents-produce-evidence-without-authority]] — the line between producing evidence and authorising a result
- [[30_assertions/self-revision-is-no-independent-verification]] — why a model checking itself does not close the loop
- [[30_assertions/the-epistemic-infrastructure-conditions-inspection]] — the arrangement in which an output becomes checkable
- [[30_assertions/independent-review-extends-coverage-not-authority]] — what review by several instances adds and what it does not
- [[30_assertions/sycophancy-needs-a-procedural-countermeasure]] — the procedural answer to agreement bias

## Open questions

- Which statements about model operation can be grounded in the feeding artefacts, and which need a further source from the research literature?
- How is the distinction between the model and the product system stated so that it survives a change of model generation?
- The feeding artefacts report the empirical literature on prompt effects, context degradation and interpretability in passing rather than examining it, so every quantitative claim in Part I currently rests on a secondary report.
- Asymmetric amplification and the Latent Program Space reading are the author's own proposals, and the sources name no observation that would count against either.
- Confabulation is named as a property in the sources without a definition that separates it from ordinary error, so the term stands in the outline without an anchor.
- The sources say nothing about the reproducibility consequences of proprietary infrastructure, which the outline assigns to chapter 2.
