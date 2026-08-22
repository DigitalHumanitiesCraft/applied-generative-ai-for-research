---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/assistant-behaviour-has-three-shaping-layers]]", "[[30_assertions/attention-relates-positions-across-layers]]", "[[30_assertions/capability-evaluations-measure-different-things]]", "[[30_assertions/fluency-is-not-fidelity-to-the-source]]", "[[30_assertions/in-context-adaptation-changes-no-weights]]", "[[30_assertions/interpretability-shows-structure-without-a-theory]]", "[[30_assertions/llm-computes-next-token-probabilities]]", "[[30_assertions/model-output-is-a-candidate-representation]]", "[[30_assertions/model-output-stays-probabilistic]]", "[[30_assertions/parametric-knowledge-carries-no-provenance]]", "[[30_assertions/pretraining-and-posttraining-are-distinguishable-and-blurred]]", "[[30_assertions/prompt-engineering-is-an-external-search]]", "[[30_assertions/prompting-intervenes-in-the-current-computation]]", "[[30_assertions/representations-are-contextual-not-fixed]]", "[[30_assertions/social-fluency-is-no-evidence-of-authority]]", "[[30_assertions/the-assistant-is-a-stabilised-character]]", "[[30_assertions/the-capability-profile-is-jagged]]", "[[30_assertions/the-latent-program-space-models-prompt-effects]]", "[[30_assertions/the-model-boundary-is-not-the-system-boundary]]", "[[30_assertions/tokenisation-fixes-the-unit-of-computation]]", "[[30_assertions/training-objective-differs-from-acquired-capability]]"]
posits: 1
lang: en
part: "I. Generative Models as Research Systems"
chapter: 1
title: "What Large Language Models Are"
topic: "[[Generative-Models]]"
feeding-sources: ["script chapter 2", "slide section AI Agents"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# What Large Language Models Are

## The operation

Reading the output of a generative system correctly requires an account of how it was produced, and the account required for that purpose is smaller than a treatment of contemporary machine learning. What a researcher needs is the part that bears on interpretation, because an output is a candidate representation whose next step is comparison with the material it claims to represent, and each technical property below changes how that comparison has to be conducted.[^13]

A large language model produces text autoregressively. From the input sequence available so far it computes a probability distribution over the next token, the token it selects becomes part of the context, and the computation repeats until the output ends.[^1] What a reader perceives as a finished answer is the accumulation of that repetition, and no step in it consults a store of facts.

The training objective and the acquired capability are not the same thing. Next-token prediction names the optimisation problem, and performing it well across heterogeneous material requires representations and transformations associated with syntax, concepts, relations, styles, code and recurring patterns of reasoning. Those structures then support work the objective never named. The objective asks which continuation is probable and leaves aside whether a proposition is true, so a system optimised in this way can build broad representations of the world while truth remains outside what it was trained to estimate.[^2]

The unit over which all of this operates is fixed by tokenisation. A tokenizer converts character sequences into discrete units that may correspond to a word, a fragment of a word or punctuation, and each unit becomes a numerical identifier before it enters the network. The boundaries follow an engineering trade-off between vocabulary size, sequence length and the ability to represent unseen strings, which is why they are not linguistically intuitive. Context capacity, input cost and output length are counted in these units, so a rare proper name in a historical source can consume several times the budget of a common word.[^3]

Those identifiers become vectors. An embedding provides the initial mapping into a high-dimensional space in which systematic relations among recurring patterns can emerge, and the familiar illustration in which related words lie near one another gives a first intuition without accounting for meaning. The initial mapping is transformed repeatedly across the network into representations that depend on the surrounding tokens and the current task, so two sentences of similar meaning written in different registers can condition different internal states.[^4] The architecture that performs those transformations is the Transformer, in which attention mechanisms across repeated layers let information at different positions influence one another, and the probability finally assigned to a continuation is the outcome of that layered computation.[^5]

This is the point at which a technical fact becomes a methodological one. Prompts and context alter the token sequence supplied to the model and thereby condition the computation from which the next tokens follow, and different formulations change the internal activations behind the output distribution. A prompt is therefore an intervention in a computation rather than a wrapper around an answer the system already holds.[^6]

## What training leaves behind

Pretraining builds broad representations from large heterogeneous material, and posttraining through instruction tuning, preference learning and related methods shapes how that repertoire is expressed. Describing the first as knowledge and the second as behaviour is a simplification, because knowledge and capability are entangled throughout, and contemporary development pipelines may carry intermediate stages that different laboratories name differently.[^7] A statement about what a model learned at which stage is therefore weaker evidence than it looks.

What training leaves behind is no retrievable copy of its material. Training changes parameters so that statistical structure from the data influences later generation, and no addressable version of a training document remains. A model can consequently describe a matter accurately while being unable to name the source from which the description was learned, and it holds no reliable register of pages or references.[^8] For research this settles a practical question. Parametric knowledge is unusable as evidence, and the parts of an answer that need provenance have to come from somewhere the system can cite.

Three information layers therefore have to be kept apart, the learned representations in the parameters, the retrievable information in external resources, and the information actually present in the current context. The boundary of the model is not the boundary of the system, so a claim about what a system can know is underdetermined as long as it names only the model.[^9] Within the current context the model adapts strongly to instructions, examples and supplied material without any weight being changed, which is what makes context a design surface and what makes the whole of Part II possible.[^10]

## What the output is

The output remains probabilistic. The same prompt can produce different results across runs, and a plausible formulation is therefore no reconstructed fact.[^11] This is the property that most reliably surprises a reader who arrives from database work, where the same query returns the same rows.

Fluency compounds the problem. A generated transcription can read convincingly while individual readings are wrong, and a generated encoding can look formally plausible while it violates the guidelines of the project, so the linguistic quality of an output and its reliability in the matter are separate properties.[^12] The first is the property a reader perceives immediately, which is why an output should be treated as a candidate representation whose next step is comparison with the material it claims to represent.[^13]

The capability profile itself is uneven. Frontier models can perform extremely difficult tasks and fail on neighbouring tasks that look simple, which makes their competence hard to extrapolate from any single success. Outputs can carry plausible but unsupported claims, models can reproduce bias and align an answer with a belief the user has expressed, and their internal computation is only partially understood.[^14] Measurement does not repair the unevenness. Evaluations of task duration, of adaptation to unfamiliar problems, of mathematical reasoning and of behaviour in executable environments answer different questions, and reading them as points on one scale of intelligence discards what each was built to establish.[^15]

## The figure in the interface

What answers a user is not the network. The assistant is a behavioural pattern stabilised by training, runtime instructions, policy layers and product design, and it is no human counterpart.[^16] Three shaping layers should be kept apart, training artefacts such as a published specification, character training and posttraining, and the system prompt that operates at runtime inside one deployment. The behaviour a user meets is produced by the interaction of trained parameters with the current runtime context.[^17]

The practical consequence is a warning about one specific inference. Models trained extensively on human communication generate convincing social behaviour, and confidence, empathy and conversational competence carry no information about whether the claims inside an answer hold.[^18] A researcher who has learned to read hedging in a colleague's prose as an epistemic signal will misread it here, because the hedging is a stylistic disposition of the assistant rather than a report of its confidence.

## A model of prompt effects

The account so far explains why wording matters and leaves open how. This book adopts a theoretical model for that. On this reading a model contains a large repertoire of learned computational transformations, and a prompt acts partly as a signal that selects and combines them. A vector program of this kind is a distributed transformation implemented through high-dimensional representations and parameters rather than a symbolic program stored as a discrete object, and behaviours such as translating, summarising or classifying are recurring patterns arising from the weights and the current activation course.[^19] Iterative prompt engineering is then an external search in which a user varies the address and evaluates the resulting behaviour.[^20]

Interpretability research supports the shape of this picture without completing it. Attribution graphs and related procedures reconstruct parts of internal pathways, show that particular internal structures relate to observable behaviour and demonstrate that interventions on representations change outputs systematically. None of that yields a map from which the effect of a natural-language prompt could be predicted.[^21] The model is therefore adopted here as a working account that organises observations, and chapter 4 draws the practical consequence, which is that a prompting finding has to be tested rather than transferred.

## Gaps

Three topics the outline assigns to this chapter have no anchor in the sources of this lane.[^22]
- Confabulation is named as a property in the feeding sources without a definition that separates it from ordinary error, so the term cannot yet be used as a technical one; a source from the research literature on hallucination and calibration is needed.
- The quantitative claims behind the jagged capability profile, the measurements of task duration and of adaptation to unfamiliar tasks, are reported by the lecture notes in passing, and grounding them properly needs the underlying publications entered as records of their own.
- The account of inference procedures and stochastic variation stays qualitative here, because the sources describe the variation without naming the sampling parameters that produce it.

[^1]: Grounded in [[30_assertions/llm-computes-next-token-probabilities]].
[^2]: Grounded in [[30_assertions/training-objective-differs-from-acquired-capability]].
[^3]: Grounded in [[30_assertions/tokenisation-fixes-the-unit-of-computation]].
[^4]: Grounded in [[30_assertions/representations-are-contextual-not-fixed]].
[^5]: Grounded in [[30_assertions/attention-relates-positions-across-layers]].
[^6]: Grounded in [[30_assertions/prompting-intervenes-in-the-current-computation]].
[^7]: Grounded in [[30_assertions/pretraining-and-posttraining-are-distinguishable-and-blurred]].
[^8]: Grounded in [[30_assertions/parametric-knowledge-carries-no-provenance]].
[^9]: Grounded in [[30_assertions/the-model-boundary-is-not-the-system-boundary]].
[^10]: Grounded in [[30_assertions/in-context-adaptation-changes-no-weights]].
[^11]: Grounded in [[30_assertions/model-output-stays-probabilistic]].
[^12]: Grounded in [[30_assertions/fluency-is-not-fidelity-to-the-source]].
[^13]: Grounded in [[30_assertions/model-output-is-a-candidate-representation]].
[^14]: Grounded in [[30_assertions/the-capability-profile-is-jagged]].
[^15]: Grounded in [[30_assertions/capability-evaluations-measure-different-things]].
[^16]: Grounded in [[30_assertions/the-assistant-is-a-stabilised-character]].
[^17]: Grounded in [[30_assertions/assistant-behaviour-has-three-shaping-layers]].
[^18]: Grounded in [[30_assertions/social-fluency-is-no-evidence-of-authority]].
[^19]: Grounded in [[30_assertions/the-latent-program-space-models-prompt-effects]].
[^20]: Grounded in [[30_assertions/prompt-engineering-is-an-external-search]].
[^21]: Grounded in [[30_assertions/interpretability-shows-structure-without-a-theory]].
[^22]: Posit: the gap list records what this chapter cannot support from its own sources. Open evidence question: which publications the reference layer has to carry before the quantitative claims of this chapter can be grounded directly.
