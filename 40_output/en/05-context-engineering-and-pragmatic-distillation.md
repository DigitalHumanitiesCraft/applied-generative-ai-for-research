---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-knowledge-document-is-materialised-context-compression]]", "[[30_assertions/compression-reduces-volume-distillation-restructures]]", "[[30_assertions/context-engineering-selects-organises-and-provides]]", "[[30_assertions/distillation-is-task-dependent]]", "[[30_assertions/distillation-runs-through-three-operations]]", "[[30_assertions/formats-require-different-access-paths]]", "[[30_assertions/knowledge-engineering-and-context-engineering-divide-the-work]]", "[[30_assertions/nominal-capacity-is-no-guarantee-of-use]]", "[[30_assertions/not-everything-relevant-enters-the-context]]", "[[30_assertions/over-distillation-removes-what-action-needs]]", "[[30_assertions/the-bottleneck-shifts-from-model-to-context]]", "[[30_assertions/the-context-window-is-a-finite-processing-space]]", "[[30_assertions/the-target-is-a-dense-and-sufficient-context]]", "[[30_assertions/the-unit-is-the-supplied-representation]]", "[[30_assertions/three-levels-separate-holding-task-and-window]]"]
posits: 2
lang: en
part: "II. From Prompting to Grounded Knowledge"
chapter: 5
title: "Context Engineering and Pragmatic Distillation"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper (Project Knowledge Base)", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Context Engineering and Pragmatic Distillation

## The object

Context Engineering is the systematic selection, organisation, maintenance and provision of the information state a task requires. It determines which information, instructions, tools and examples are available at a given moment, in which form and order they are supplied, when further material is loaded and what deliberately stays outside.[^1] The last of those decisions is the one most often left implicit, and it is as consequential as the others.

Three levels have to be kept apart, and collapsing them produces most of the confusion in this area. The Project Knowledge Base preserves the persistent, inspectable and revisable holding. The Working Context is the information state assembled for one concrete task. The context window is the technical space in which that state is processed. General reports, guidelines for other source types, complete logs, superseded schema versions and obsolete attempts belong in the holding and stay out of the working context of a single task, and knowledge documents need not be loaded in full for every task.[^2]

The division of labour that follows is the spine of Part II. Knowledge Engineering builds and maintains the holding, Context Engineering assembles from it what a task needs, and the second presupposes the first, because only a structured holding permits selective loading. That dependence is what separates Context Engineering from a better kind of prompting.[^3]

## What the window is and what it is not

The context window is the finite space that holds everything a run can use. It contains system and project instructions, the current input, the working history, document excerpts, tool descriptions, tool outputs, intermediate results and the generated answer, and when input and output together exceed the limit the system must shorten the sequence through truncation or compaction or refuse the request.[^4]

Nominal capacity is not usable capacity. Position, distraction and volume influence performance, and relevant information becomes harder to find in long inputs when it stands between similar or contradictory material. Context Rot names the observed decline in retrieval and use as contexts grow longer, denser or more distracting, and it is no single settled mechanism, since position effects, distractors, conflicting information, obsolete intermediate state and the structure of the task can all contribute. Performance can therefore fall before the formal limit is reached.[^5]

The conclusion is not that context should be short. Too strong a reduction removes conditions, uncertainties and provenance, and what is wanted is as bounded as possible and as complete and differentiated as the task requires, every statement carrying information, with a minimal core permanently present and depth loaded on demand.[^6] Where the target matters most is the long run, because with growing autonomy the bottleneck of a workflow shifts from the model to the context. Three mechanisms carry that shift, degradation well below the nominal limit, accumulation of noise across a long autonomous run, and a finite reasoning budget spent on navigating disordered material. Strong models stay robust against untidy context for short single queries, and the problem turns at long-horizon delegation, when the agent works with the material independently across many steps.[^7]

## What actually enters a context

A file in a project folder is not part of the context until the system reads, extracts, transforms or inspects it. The path runs from the holding through a tool, parser or script to a supplied representation and then through tokenisation into the window, so a script can return the counts a modelling question needs instead of the material itself, and an agent can inspect complete datasets through tools while only summaries, query results or excerpts enter the token sequence. The methodologically relevant unit is therefore the supplied representation rather than the file.[^8]

Formats differ in what that path costs. Plain text and source code can usually be read directly, tabular material can be profiled or queried selectively, office formats have to be extracted, layout formats combine text, structure and image, images are processed multimodally or described, and databases are used through queries without being loaded.[^9] Relevance to a project and relevance to a task are separate properties. The complete holding matters to the project while not all of it belongs in a context at once, and further resources can stay where they are and be reached through tools when needed.[^10]

This is where the arrangement chapter 2 introduced takes its general form. The model reads about the data and writes code that reads the data. What the model receives is a task-specific description of structure, semantics, uncertainty, exceptions and relevance, and the generated code processes the complete material outside the context.[^11]

## Distillation as pragmatic modelling

Reduction comes in two kinds that are frequently confused. Compression reduces the volume of what is supplied through selection of sections, summary, removal of repetition, aggregation and compaction of a working history, and a shorter version is not automatically a better one, because a summary can smooth uncertainty, remove justifications or turn several alternatives into an apparently unambiguous rule. Distillation goes further and transfers available understanding into a selective, structured, inspectable and revisable representation intended to be sufficient for the work that follows.[^12]

Three operations carry it. Selection decides what is relevant to the subject, structuring makes terms, rules and relations explicit, and condensation removes redundancy without losing necessary differentiation, and what has to survive are the relevant terms and distinctions, the relations and dependencies, the conditions and constraints, the uncertainties and open questions, and the justifications behind decisions.[^13] The counter-risk is a representation condensed past the point where it can guide work, recognisable by what it no longer carries rather than by its length.[^14]

Distillation is therefore task-dependent. A general introduction, an implementation specification and a verification task need different representations of one body of knowledge, and every reduction decides which distinctions remain available for the work that follows, which makes it epistemically consequential rather than a matter of convenience.[^15] A distilled document also moves the reduction out of the run. As materialised context compression it performs in advance a condensation the model would otherwise have to make from raw material each time, which is the practical reason a maintained holding outperforms a well-worded instruction over a long task.[^16]

## Gaps

Two of the topics the outline assigns to this chapter are treated only partially.[^17]
- Retrieval and selective inclusion are named in the outline. The sources of this lane state that resources can be reached through tools and that a database can be queried without being loaded, and they describe no retrieval architecture, so the chapter states the principle and omits the mechanism.
- Context refresh and revision appear here through the layered arrangement with a permanently present core, and the sources give no procedure for deciding when a context should be rebuilt during a run. The other manuscript lane treats the working context in its Promptotyping chapters, and a cross-reference will have to carry the topic until that distillate can be read against this one.

[^1]: Grounded in [[30_assertions/context-engineering-selects-organises-and-provides]].
[^2]: Grounded in [[30_assertions/three-levels-separate-holding-task-and-window]].
[^3]: Grounded in [[30_assertions/knowledge-engineering-and-context-engineering-divide-the-work]].
[^4]: Grounded in [[30_assertions/the-context-window-is-a-finite-processing-space]].
[^5]: Grounded in [[30_assertions/nominal-capacity-is-no-guarantee-of-use]].
[^6]: Grounded in [[30_assertions/the-target-is-a-dense-and-sufficient-context]].
[^7]: Grounded in [[30_assertions/the-bottleneck-shifts-from-model-to-context]].
[^8]: Grounded in [[30_assertions/the-unit-is-the-supplied-representation]].
[^9]: Grounded in [[30_assertions/formats-require-different-access-paths]].
[^10]: Grounded in [[30_assertions/not-everything-relevant-enters-the-context]].
[^11]: Posit: the formula that the model reads about the data while generated code reads the data is the outline's own condensation of the preceding assertions and stands in no feeding source in that form. Open evidence question: a comparison of results where the same task is given once with the data in context and once with a description plus generated processing code.
[^12]: Grounded in [[30_assertions/compression-reduces-volume-distillation-restructures]].
[^13]: Grounded in [[30_assertions/distillation-runs-through-three-operations]].
[^14]: Grounded in [[30_assertions/over-distillation-removes-what-action-needs]].
[^15]: Grounded in [[30_assertions/distillation-is-task-dependent]].
[^16]: Grounded in [[30_assertions/a-knowledge-document-is-materialised-context-compression]].
[^17]: Posit: the gap list records where this chapter falls short of the outline. Open evidence question: whether the Promptotyping paper distillate carries a procedure for refreshing a working context during a run.
