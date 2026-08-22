---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/agentic-capability-arises-from-the-compound-system]]", "[[30_assertions/automation-claims-are-self-descriptions]]", "[[30_assertions/capability-evaluations-measure-different-things]]", "[[30_assertions/harness-quality-changes-what-can-be-evaluated]]", "[[30_assertions/model-choice-is-a-system-choice]]", "[[30_assertions/probabilistic-and-deterministic-operations-combine]]", "[[30_assertions/the-harness-is-the-technical-layer-of-action]]", "[[30_assertions/the-harness-supplies-no-scholarly-authority]]", "[[30_assertions/tool-use-changes-the-epistemic-structure]]", "[[30_assertions/vision-language-models-fail-plausibly]]"]
posits: 3
lang: en
part: "I. Generative Models as Research Systems"
chapter: 2
title: "Models, Tools, and Generative Systems"
topic: "[[Generative-Models]]"
feeding-sources: ["script chapter 2", "slide section AI Agents"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Models, Tools, and Generative Systems

## The object of evaluation

A large language model rarely operates alone. Contemporary research applications combine a base model with system instructions, retrieval mechanisms, external tools, code execution, memory, interfaces and access to local or remote files, and the capability a project actually has follows from that compound. What the sources of this book state as the general form of the point is that agentic capability arises from the combined system of model, harness and environment rather than from the model considered on its own, so evaluating a model in isolation measures something other than what a project can do with it.[^1]

The consequence for research is a question of naming. When a study reports that a model performed a task, the claim is usually about a compound whose other components were not described. Two runs with the same model in different environments can differ more than two runs with different models in the same environment, and neither difference is visible in a statement that names only the model.[^13]

## What the harness is

The technical layer through which an agent receives context, calls tools, accesses files, executes programs and processes feedback is the harness. It manages state, permissions and control flow, and it fixes which folders may be read or changed, which commands run without confirmation, how tool outputs return into the context, how long a run continues, when a person must be involved and how intermediate results are stored.[^2] Each of those settings determines what a later reader of the run can reconstruct, which makes the harness part of the evidential arrangement rather than a convenience layer around it.

Its quality changes what can be evaluated. A capable model in a weak harness may be unable to inspect or verify the consequences of its own actions, while tools, tests, persistent state and designed feedback make the whole system more capable and more inspectable than a model evaluation would suggest. A harness that preserves execution traces, test results and failure information leaves behind a trajectory that can be continued or corrected by someone who was not present.[^3]

The limit is equally definite. A validator can establish that an element is admissible at a position and cannot decide whether the source is actually illegible or whether another reading is more probable, and one level up the same holds for the environment as a whole. It can bound and record what happens, and it does not determine which project knowledge is relevant or whether a modelling decision is adequate.[^4] Chapter 3 develops what follows from that limit, and Part III returns to it as the boundary that agentic work is organised around.

## What tools change

Tools extend a text generator into a system that can act on an environment. File access, terminals, code execution, search, databases, browsers, validators and specialised interfaces all belong here, and the ones that matter most are those that return evidence about the consequences of an action. A compiler, a test suite or a schema validator answers a question the model would otherwise answer about itself, and that changes the epistemic structure of the workflow, because the system is no longer relying only on generated text and can obtain observations that constrain its next step.[^5]

Multimodal processing is a case where the extension carries a specific risk. A vision language model handles visual and linguistic information within one task, so a general-purpose system can receive a facsimile together with an instruction and return a transcription without being a dedicated recognition system. Visual patterns, layout, linguistic context and the instruction jointly shape the output, which produces the characteristic failure of a reading that fits the sentence and does not fit the page. Whether the resulting ability on unseen handwriting should count as an emergent capability depends on the definition of emergence, on scale and on training data that is not disclosed.[^6]

The productive arrangement combines the two kinds of operation rather than choosing between them. Recognising a table, reading a layout or extracting values from noisy material may require probabilistic behaviour, and once the values are represented explicitly the relations among them can be recomputed deterministically. The recurring pattern runs from probabilistic interpretation through a structured representation to deterministic checking, and invariants such as row and column totals expose internal inconsistency without proving that the source was read correctly.[^7] This is the smallest complete example of the arrangement the whole book describes, and chapter 5 gives it its general form as a division between what the model reads about and what the code reads.

## Choosing a system

Because the compound is the unit, choosing a model is choosing a system. Systems differ in capability, modalities, inference cost, latency, openness, deployment options, context capacity, tool use and the harnesses through which they can operate, and a decision taken on benchmark performance alone silently fixes all the other properties.[^8] A project that needs local execution, or that needs a run to be repeatable in five years, is deciding about deployment and preservation while it appears to be deciding about quality.

The evaluations themselves resist aggregation. Measurements of task duration, of adaptation to unfamiliar problems, of mathematical reasoning and of behaviour in executable environments answer different questions, and collapsing them into one scale discards what each was built to establish.[^9] Public statements from frontier laboratories about automating research belong to a different category again. They record the direction in which a laboratory is attempting to extend capability, and they are no evidence that research has been automated.[^10]

What follows for a research project is a modest procedure. State which properties of the compound the work depends on, check those properties directly, and treat capability reports as evidence about the conditions under which they were produced.[^11]

## Gaps

Two of the topics the outline assigns to this chapter are not covered by the sources of this lane, and one is covered only partially.[^12]
- Retrieval-augmented generation is named in the outline and appears in the feeding sources only as the general observation that external resources can supply information during inference, so the chapter states the layer distinction and not the retrieval architecture. A source on retrieval systems is needed before the topic can be treated.
- Proprietary infrastructure and reproducibility, which the outline assigns here, has no anchor at all in the three feeding sources. The Promptotyping paper of the other manuscript lane treats reconstructability, and chapter 23 carries the topic; a cross-reference will have to replace a treatment here until that distillate is available.
- Persistent memory and stored user context appear in the sources only as part of the general list of what a harness manages, without a description of how memory changes across sessions.

[^1]: Grounded in [[30_assertions/agentic-capability-arises-from-the-compound-system]].
[^2]: Grounded in [[30_assertions/the-harness-is-the-technical-layer-of-action]].
[^3]: Grounded in [[30_assertions/harness-quality-changes-what-can-be-evaluated]].
[^4]: Grounded in [[30_assertions/the-harness-supplies-no-scholarly-authority]].
[^5]: Grounded in [[30_assertions/tool-use-changes-the-epistemic-structure]].
[^6]: Grounded in [[30_assertions/vision-language-models-fail-plausibly]].
[^7]: Grounded in [[30_assertions/probabilistic-and-deterministic-operations-combine]].
[^8]: Grounded in [[30_assertions/model-choice-is-a-system-choice]].
[^9]: Grounded in [[30_assertions/capability-evaluations-measure-different-things]].
[^10]: Grounded in [[30_assertions/automation-claims-are-self-descriptions]].
[^11]: Posit: the procedure follows from the preceding assertions and is stated by no source. Open evidence question: whether projects that adopt it choose differently from projects that read benchmark tables, which a study of documented model decisions could test.
[^12]: Posit: the gap list is the author's judgment of what this chapter cannot support. Open evidence question: whether the Promptotyping paper distillate closes the reproducibility gap or only relocates it to chapter 23.
[^13]: Posit: the comparison between two runs in different environments and two models in one environment is an inference from the compound-system assertion and is measured in no source. Open evidence question: a paired study varying model and harness independently on the same research task.