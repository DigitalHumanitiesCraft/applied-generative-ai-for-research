---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/agentic-capability-arises-from-the-compound-system]]", "[[30_assertions/agents-predate-language-models]]", "[[30_assertions/an-agent-pursues-a-goal-across-several-calls]]", "[[30_assertions/autonomy-is-the-span-between-interventions]]", "[[30_assertions/feedback-arrives-from-several-sources]]", "[[30_assertions/intervention-points-are-named-in-advance]]", "[[30_assertions/single-agent-and-federation-are-two-modes]]", "[[30_assertions/the-execution-loop-is-a-control-loop]]", "[[30_assertions/the-scope-of-action-comes-from-tools-and-environment]]", "[[30_assertions/the-semantic-web-took-the-reverse-route]]", "[[30_assertions/the-shift-is-from-response-to-trajectory]]", "[[30_assertions/tool-use-changes-the-epistemic-structure]]"]
posits: 4
lang: en
part: "III. Agentic Research Work"
chapter: 8
title: "From Models to Agents"
topic: "[[Agentic-Work]]"
feeding-sources: ["script chapter 6", "slide sections Agentic Engineering and Workflows"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# From Models to Agents

## What makes a system an agent

An isolated model call produces an output. An agent pursues a goal across several model and tool calls, inspects its environment, selects an action, observes the result and updates its procedure, and the distinction requires no complete autonomy, because contemporary agents work inside human-defined goals, tools, permissions and stopping conditions. What matters is that the model participates in selecting and coordinating several actions.[^1]

The capability is no property of the model. The model contributes flexible planning and interpretation, and the possibilities of action arise from the tools and the environment the surrounding system provides.[^2] Stated at the level of the whole system, agentic capability arises from the compound of model, harness and environment, so evaluating a model in isolation measures something other than what a project can do with it.[^3]

The cycle has a shape that predates the vocabulary. Capturing the state, planning a bounded next step, executing a tool or action, observing the result and updating the procedure is the loop, and its structure is the feedback loop cybernetics described in 1948, a system steering itself by returning information about its own effects, with tool outputs in the place of sensors.[^4] The information that steers a run arrives from validators, tests, error messages, tool outputs, reviews by other agents, human responses and changed requirements, and the sources differ in what each of them can establish.[^5]

## Tools and the epistemic change

Tools extend a text generator into a system that can act. File access, terminals, code execution, search, databases, browsers, validators and specialised interfaces belong here, and those that return evidence about the consequences of an action matter most, because a compiler, a test suite or a schema validator answers a question the model would otherwise answer about itself. The system therefore stops relying only on generated text and can obtain observations that constrain its next step.[^6]

This is where the difference from a conversational system becomes methodological rather than technical. A chatbot exchange can be judged from one response. An agentic system produces a trajectory containing observations, intermediate decisions, tool calls, file modifications, execution results and subsequent actions, so reliability depends on the organisation of the whole sequence, and what is engineered is the trajectory rather than the answer.[^7]

## Autonomy as a span

Autonomy in this practice measures the extent of work between two human interventions, and it does not mean the absence of control.[^8] Reading it as a quantity of freedom leads to the wrong design question. The right one is where a person looks, and the points at which that has to happen are nameable in advance, contradictory requirements, missing scholarly foundations, changes that are hard to reverse, sensitive resources, modelling decisions with consequences in the matter, and validation and acceptance.[^9]

Naming them before a run is what turns intervention into part of the design. It also fixes the relation the outline calls the one between agent capability and specification requirement. As the span grows, more of the purpose, the constraints, the knowledge, the permissions and the verification criteria of a project has to exist in persistent and inspectable form before execution begins, because the agent will pass the points at which a person would have asked.[^10]

## An older concept

The agent concept predates language models by decades. Classical work defines an agent through its relation to an environment and its capacity for autonomous, reactive and goal-directed action, names the four properties of autonomy, reactivity, proactiveness and social ability, and earlier systems show that agency is not tied to language. What language models changed is the practical design space, because natural language, code and heterogeneous digital resources can now form a common interface for planning and action, so the systems of today are a contemporary form of a much older idea. The four properties of 1995 map onto them as running without query across many steps, processing tool results and errors, pursuing goals beyond a single instruction, and delegating to subagents.[^11]

A second lineage is worth naming because it took the opposite route to a comparable goal. The Semantic Web vision of 2001 did not aim at machines understanding human language. Machine-understandable documents meant that a machine solves a well-defined problem on well-defined data, with people structuring their data through ontologies and unique identifiers, and contemporary models process unstructured text directly without that infrastructure.[^12] The comparison matters for Part II, because it locates what a maintained knowledge holding is for. Its role is no longer to be the formal substrate a machine needs in order to act, and it has become the record that lets a person check what the machine did.[^13]

## One agent or several

Two modes of operation are distinguishable at the same tool. In the narrower sense an agent is a modular system driven by a language model for delimited tasks, with tool access, memory and planning around the model. An orchestrated federation adds collaboration, dynamic task decomposition, persistent memory and coordinated autonomy, and it differs by architecture rather than by degree of autonomy, so a system acts as one agent in a simple run and moves towards a federation once it delegates to several coordinated instances.[^14]

Reading this as a ladder would misplace the decision. What the second mode buys and what it costs is the subject of chapter 9, and the point here is that the two are modes rather than categories, so a project chooses between them per task instead of once.[^15]

## Gaps

Two of the topics the outline assigns to this chapter are covered only in part.[^16]
- Memory and persistence appear in the sources as part of the general list of what a harness manages and as the observation that intermediate results belong in persistent artefacts. How memory behaves across sessions, and what a project can rely on it to carry, is described nowhere in these sources.
- Repository and file access and code execution are named here inside the list of tool classes rather than treated separately. The worked example of Part VI is where they acquire the detail the outline implies, and the hands-on chains of the other manuscript lane carry the material.

[^1]: Grounded in [[30_assertions/an-agent-pursues-a-goal-across-several-calls]].
[^2]: Grounded in [[30_assertions/the-scope-of-action-comes-from-tools-and-environment]].
[^3]: Grounded in [[30_assertions/agentic-capability-arises-from-the-compound-system]].
[^4]: Grounded in [[30_assertions/the-execution-loop-is-a-control-loop]].
[^5]: Grounded in [[30_assertions/feedback-arrives-from-several-sources]].
[^6]: Grounded in [[30_assertions/tool-use-changes-the-epistemic-structure]].
[^7]: Grounded in [[30_assertions/the-shift-is-from-response-to-trajectory]].
[^8]: Grounded in [[30_assertions/autonomy-is-the-span-between-interventions]].
[^9]: Grounded in [[30_assertions/intervention-points-are-named-in-advance]].
[^10]: Posit: the inference that a longer span requires more of the project to exist in persistent form before execution is the outline's own and is stated by no source in that generality. Open evidence question: a comparison of runs of increasing span against the completeness of the specification they started from.
[^11]: Grounded in [[30_assertions/agents-predate-language-models]].
[^12]: Grounded in [[30_assertions/the-semantic-web-took-the-reverse-route]].
[^13]: Posit: reading the maintained holding as a record for checking rather than as a substrate for machine action is this book's own placement of the comparison. Open evidence question: whether projects that keep formal representations alongside prose use them for action, for checking or for both.
[^14]: Grounded in [[30_assertions/single-agent-and-federation-are-two-modes]].
[^15]: Posit: the recommendation to choose the mode per task follows from the two-modes assertion and is stated by no source. Open evidence question: which task properties predict that a federation outperforms a single agent.
[^16]: Posit: the gap list records where this chapter falls short of the outline. Open evidence question: whether the hands-on chains of the other manuscript lane carry a description of memory across sessions.
