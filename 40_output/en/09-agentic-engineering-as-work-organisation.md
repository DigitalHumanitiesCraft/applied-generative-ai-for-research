---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/agent-to-agent-protocols-address-a-second-surface]]", "[[30_assertions/agentic-engineering-organises-multi-step-work]]", "[[30_assertions/checking-a-run-covers-behaviour-data-and-requirements]]", "[[30_assertions/harness-quality-changes-what-can-be-evaluated]]", "[[30_assertions/increments-must-stay-inspectable]]", "[[30_assertions/independent-review-extends-coverage-not-authority]]", "[[30_assertions/instruction-files-are-context-not-enforcement]]", "[[30_assertions/least-privilege-and-reversibility-bound-the-run]]", "[[30_assertions/model-routing-separates-functions]]", "[[30_assertions/more-agents-raise-coordination-cost]]", "[[30_assertions/plans-stay-compact-and-revisable]]", "[[30_assertions/skills-package-procedure-with-progressive-disclosure]]", "[[30_assertions/specification-precedes-implementation]]", "[[30_assertions/subagents-bound-context-and-parallelise]]", "[[30_assertions/the-mechanisms-are-not-interchangeable]]", "[[30_assertions/the-organisation-requirements-are-explicit]]", "[[30_assertions/the-workspace-is-part-of-the-method]]", "[[30_assertions/tool-protocols-solve-integration-not-relevance]]"]
posits: 3
lang: en
part: "III. Agentic Research Work"
chapter: 9
title: "Agentic Engineering as Work Organisation"
topic: "[[Agentic-Work]]"
feeding-sources: ["script chapter 6", "slide sections Agentic Engineering and Workflows"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Agentic Engineering as Work Organisation

## The definition and its reach

Agentic Engineering is the systematic organisation and control of multi-step agentic work. It covers the bounding and decomposition of tasks, tool use, the processing of intermediate results, states and handovers, conditions for abort and escalation, and checking and continuation, and its central question is under which conditions the actions of an agent stay traceable, bounded and correctable. Its object reaches beyond code to data descriptions, specifications, mappings, design decisions, process documents and verification concepts.[^1]

The organisational requirements are explicit rather than emergent. Tasks have to be bounded and decomposed, tools, permissions and stopping conditions defined, intermediate results inspected and where necessary escalated, and project state kept understandable across steps, which makes agentic capability a new engineering surface where context, state, tools, control and evaluation are coordinated over time.[^2] Human labour is redistributed rather than removed by this. What moves is the point at which a person acts, from performing each implementation step to preparing knowledge, stating goals, decomposing work, assigning permissions, inspecting intermediate results and verifying outcomes.[^3]

## Before execution

Work begins before the first substantive instruction. The first decision is where the model will work, what is prepared determines which files, tools, knowledge and forms of feedback later become available, and the preparation phase produces a persistent and traceable holding with documented provenance and unchanged source files, so that later work does not begin from nothing.[^4]

An explicit specification then stands between exploratory discussion and implementation. Developing requirements, user stories, data constraints, interfaces and verification criteria before substantial implementation reduces the tacit interpretation delegated to the agent and creates an object that can be reviewed before code exists, and the same discipline appears in the working instruction, which asks for a conceptual approach and a compact plan first and requires the agent to ask about whatever it cannot derive reliably instead of assuming silently.[^5]

Planning has a failure mode of its own. A plan should determine which sub-problems exist, which information is missing, which tools are needed, which checks are foreseen and in which order to proceed, and an extensive plan drawn up before the holdings have been inspected creates false certainty, so a usable plan is compact, checkable against the current state and revisable.[^6]

## Bounds on the run

Two bounds are placed on what an agent may do. A tool call can change the project state, so access follows the least necessary permission, and the concrete pattern reads source files without overwriting them, allows changes to generated files in a working folder, lets validators run without confirmation, requires an explicit release for publication steps and keeps changes versioned and reversible.[^7]

The bound has to be enforced rather than described. An instruction file is context and not a guarantee, and behavioural guidance is a different thing from permissions and hooks, which can hold a boundary independently of whether a model complies.[^8] A project that writes its limits into a document and grants unrestricted access has described a policy and implemented none.[^9]

## Increments and their inspection

Multi-step work proceeds in increments that can be checked. A useful intermediate state can be run or inspected, belongs to a defined project state, can be checked against requirements and is small enough that the cause of an error can be reconstructed, and plans, decisions, check results and open questions belong in persistent project artefacts rather than in the chat history.[^10] Checking a generated artefact covers whether it runs, whether the data are read and displayed correctly, whether the agreed requirements are implemented and whether the source files have remained unchanged, and the last of those is a property of the run rather than of the artefact.[^11]

What makes any of this inspectable at all is partly a property of the environment. A harness that preserves execution traces, test results and failure information leaves a trajectory that someone who was not present can continue or correct, while a capable model in a weak harness may be unable to inspect the consequences of its own actions.[^12]

## Mechanisms and their division of labour

Several mechanisms recur in contemporary agent systems, and treating them as interchangeable labels hides the actual engineering decision, which is which mechanism should carry which type of information or capability.[^13]

A skill packages a reusable procedure. It is a folder with an instruction file and optionally scripts, references and assets, it holds procedural rather than descriptive knowledge, and only its name and description stay present at session start while the full instructions load when it becomes relevant, which lets a system keep many specialised capabilities without injecting all of them into every task.[^14]

A tool protocol standardises the connection between applications and tools, so one server can expose a repository, a database or a validator to every client that speaks the protocol and no bespoke connector is needed per pair. Whether a tool suits the task, whether its data are reliable and how its results are to be interpreted stay outside what the standard settles.[^15] An agent-to-agent standard addresses a second surface, supporting discovery, task management and the exchange of results without requiring an agent to expose its memory, tools or implementation, and it is complementary to a tool protocol. The methodological questions stay open regardless, which agent is responsible for what, which information is handed over, how conflicts become visible and who decides when results contradict one another.[^16]

A subagent bounds a context. A delegated instance works on part of a task in its own fresh context, inspects a defined subset of resources and returns a compact result, which protects the parent context from volumes of intermediate material and lets independent checks run at once, and the pattern carries no formal standard while appearing in nearly identical form across systems. Every delegated instance needs a clear assignment, bounded context, a defined return format and rules for uncertainty.[^17]

The cost side is easy to underestimate. More agents do not produce better results by themselves, and every additional instance creates possible handoffs, divergent assumptions and points of failure.[^18] What several instances do add is coverage. Independent reviewers expose disagreement and locate suspicious cases, the evidence returned by schemas, tests, source comparisons and domain knowledge stays more important than agreement among them, and the purpose of orchestration is a structured trajectory of independent work rather than a larger number of model calls.[^19]

Routing is the last of these decisions. Planning, implementation and review need neither the same model nor the same inference budget, so planning and review can run on a model chosen for reasoning while implementation runs on one chosen for throughput, the specification stays contextualised by the maintained project knowledge, and the routing itself is an engineering decision that changes as models change.[^20]

## Gaps

Three of the topics the outline assigns to this chapter reach past the sources.[^21]
- Handovers are named in the outline and appear in the sources only as one item in the list of what agentic engineering covers. What a handover package contains, and what a receiving party needs from it, is treated in chapter 22 of the other manuscript lane.
- Auditing appears here through the harness that preserves traces and through independent review, and no source describes an audit procedure over a completed trajectory.
- Testing and visual feedback are carried by the four checks of a verification pass and by the reflection questions of chapter 10. A treatment at the level the outline implies needs the hands-on chains, which belong to the other lane.

[^1]: Grounded in [[30_assertions/agentic-engineering-organises-multi-step-work]].
[^2]: Grounded in [[30_assertions/the-organisation-requirements-are-explicit]].
[^3]: Posit: the redistribution of human labour rather than its removal is the outline's own formulation, and the sources state the individual activities without the summary claim. Open evidence question: a comparison of where working time is spent before and after a project adopts agentic workflows.
[^4]: Grounded in [[30_assertions/the-workspace-is-part-of-the-method]].
[^5]: Grounded in [[30_assertions/specification-precedes-implementation]].
[^6]: Grounded in [[30_assertions/plans-stay-compact-and-revisable]].
[^7]: Grounded in [[30_assertions/least-privilege-and-reversibility-bound-the-run]].
[^8]: Grounded in [[30_assertions/instruction-files-are-context-not-enforcement]].
[^9]: Posit: the judgment that a written limit without a technical one implements nothing follows from the preceding assertion and is stated by no source. Open evidence question: how often documented limits are exceeded in projects that rely on guidance alone.
[^10]: Grounded in [[30_assertions/increments-must-stay-inspectable]].
[^11]: Grounded in [[30_assertions/checking-a-run-covers-behaviour-data-and-requirements]].
[^12]: Grounded in [[30_assertions/harness-quality-changes-what-can-be-evaluated]].
[^13]: Grounded in [[30_assertions/the-mechanisms-are-not-interchangeable]].
[^14]: Grounded in [[30_assertions/skills-package-procedure-with-progressive-disclosure]].
[^15]: Grounded in [[30_assertions/tool-protocols-solve-integration-not-relevance]].
[^16]: Grounded in [[30_assertions/agent-to-agent-protocols-address-a-second-surface]].
[^17]: Grounded in [[30_assertions/subagents-bound-context-and-parallelise]].
[^18]: Grounded in [[30_assertions/more-agents-raise-coordination-cost]].
[^19]: Grounded in [[30_assertions/independent-review-extends-coverage-not-authority]].
[^20]: Grounded in [[30_assertions/model-routing-separates-functions]].
[^21]: Posit: the gap list records where this chapter falls short of the outline. Open evidence question: whether an audit procedure over a completed trajectory can be derived from what a harness preserves.
