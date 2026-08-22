---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-failure-becomes-learning-only-through-interpretation]]", "[[30_assertions/a-finding-is-attributed-before-it-is-written-back]]", "[[30_assertions/a-public-deployment-is-the-latest-state-of-a-development-history]]", "[[30_assertions/a-runnable-state-is-not-yet-a-promptotype]]", "[[30_assertions/agentic-capability-arises-from-model-harness-and-environment]]", "[[30_assertions/conformity-to-a-mapping-is-examined-separately-from-its-adequacy]]", "[[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]]", "[[30_assertions/findings-about-agentic-work-change-the-arrangement]]", "[[30_assertions/findings-arise-at-several-non-interchangeable-levels]]", "[[30_assertions/implementation-can-participate-in-the-formation-of-a-model]]", "[[30_assertions/implementation-keeps-the-project-intelligible-and-testable]]", "[[30_assertions/implementation-proceeds-through-bounded-inspectable-increments]]", "[[30_assertions/interface-findings-concern-the-claims-a-representation-implies]]", "[[30_assertions/project-level-and-method-level-write-back-differ]]", "[[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]]", "[[30_assertions/the-handoff-document-is-a-process-inbox]]", "[[30_assertions/write-back-makes-a-finding-durable]]"]
posits: 0
lang: en
part: "IV. Promptotyping"
chapter: 15
title: "Agentic Implementation and Return Paths"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Agentic Implementation and Return Paths

## Handing the document set to an agent

Implementation makes maintained project knowledge actionable through language-model-supported development. It may run as iterative chat-based interaction in which contributors move prompts, code, and results between the model and the project environment, and it is more effectively organised through an AI harness once the agent has to work directly with project files, execute code, inspect intermediate results, and continue across several steps. In either arrangement the work consists of bounded tasks whose consequences become available for examination.[^1] The technical environment is part of the system rather than its packaging, since the harness supplies context, access to project resources, tools, and feedback, and capability arises from model, harness, and environment together.[^2]

What the agent produces from the semi-formal specification is the ordinary material of research software, meaning parsers, transformations, schemas, tests, queries, application code, interfaces, and the visible artefacts a project publishes or uses. The order in which it appears is what distinguishes the method from unstructured generation. Work proceeds through inspectable and versioned increments, and each increment should establish a runnable state that can be compared with the maintained project knowledge before further assumptions become embedded in the implementation.[^1] Early increments may deliberately aim at a transformation, interface, or workflow that is operational enough to support examination and discussion rather than at a complete feature set.

Agentic implementation also has a housekeeping obligation that is not housekeeping. Generated code may require refactoring, and executable checks are added or revised wherever relevant behaviour can be formalised, because those practices preserve the inspectability of the implementation and make it possible to relate observed behaviour to the documents that guide it. The document that carries the test strategy states its guarantees, its deliberate gaps, and its reproducible run commands, and it tells the agent in which form a new guarantee has to be secured, which lifts a sign-off from an assertion that something holds to a measurement that a check is green.[^3]

Where several agents work on bounded components or checks, the division changes the coordination and not the responsibility. Assignments and permissions stay explicit and auditable, access to tools and project resources is limited to the delegated task, the actions and outputs of each agent stay inspectable against project knowledge, sources, and criteria, and increasing the number of agents may increase the work of coordinating and auditing them.[^4]

## The loop that is not between code and output

An implementation state is provisionally sufficient once it is runnable, inspectable, and identifiable through versioning, so that it can support verification and discussion with responsible contributors. That state is the basis from which purpose-specific verification and acceptance proceed and is not yet an accepted iteration.[^5] The generated artefact is therefore not the final authority. It is an implementation through which the adequacy of the maintained project understanding can be tested, and it can participate in forming the model, capture practice, and requirements from which it was developed, on the condition that the consequences disclosed through its use are interpreted, documented, and incorporated.[^6]

That condition is the point at which the method does its work. Findings arise at several interacting but non-interchangeable levels, covering the represented domain, source interpretation, research-data models, capture practices, transformations, interface representations, the organisation of agentic work, checking procedures, and the allocation of authority. Treating every observed problem as a defect in generated code would conceal the scholarly, technical, and organisational decisions through which the artefact was produced, and although an implemented artefact makes the effects of several layers visible at once, responsible interpretation has to distinguish which layer produced the observed consequence.[^7]

Attribution therefore precedes correction. Some findings concern the represented domain and require revision of the data model or capture practice, while others concern how an otherwise adequate distinction is made accessible and can stay within the operational or visual design of the interface.[^8] Getting this wrong in one direction conceals a limitation of the model behind interface logic, and getting it wrong in the other changes a domain model that was never at fault.[^7]

## Where a finding goes

The return paths of the cycle can be read off the levels. An implementation defect is corrected in the code. An incomplete or ambiguous instruction to the agent is corrected in the agent configuration, along with working contexts, permissions, escalation procedures, verification states, or acceptance criteria where those are what failed.[^9] A missing or misstated requirement belongs in the declarative document that carries it. An unsupported assumption returns the work to Exploration, and a changed source or an incomplete schema returns it to Preparation, since the phases are recurrent and findings from Implementation may return the work to any of them.[^10]

Two levels deserve their own treatment because their failures look alike from the outside. A transformation may conform to its mapping and produce schema-valid output while representing the source inadequately, and an error in the implementation of an adequate mapping is corrected in the transformation rather than in the mapping, which is why the implemented result lets conformity be examined separately from the scholarly adequacy of what it conforms to.[^11] A representation may likewise assert more than its data carry, as when dates encoded with an earliest and a latest bound were shown as precise points on a timeline and were then represented as intervals, so that the write-back concerned the visual and operational treatment of uncertainty and left the underlying records untouched.[^12]

Write-back is the operation that makes any of this durable. A correction becomes methodologically consequential when it is incorporated into the maintained project knowledge instead of remaining in the current implementation, its purpose is to carry the interpreted consequence of a finding into the project state rather than to preserve every observation, and not every consequential finding calls for revision, because implementation may instead establish the boundary of what an iteration can responsibly claim.[^13] Where a project keeps a process inbox, the mechanics are fixed as well, in that durable content is integrated into the responsible document first, a short entry then records subject, source, target, and result, and the open point is removed only afterwards.[^14]

## Project-level and method-level learning

Write-back has a scope as well as a level. Project-level write-back changes the maintained knowledge, implementation conditions, or checking arrangements of one project, while method-level write-back incorporates a finding into more general rules, and generalisation depends on the available evidence, the recurrence of the problem across cases, and the consequences of adopting the proposed rule.[^15] The restraint is deliberate, since a method that absorbed every local workaround as a general prescription would become unusable in exactly the projects it was meant to serve. One documented observation of qualitative degradation during extended implementation sessions led to changes in session length, context refresh, and reliance on maintained documents, and it stands as a candidate for a general rule rather than as one.[^15]

Neither kind of learning happens by itself. An observed failure becomes project-level or method-level knowledge only through interpretation, attribution, documentation, and incorporation into the maintained project state, and without those operations it stays a local implementation event that the next iteration will repeat.[^16] The repositories of the documented cases show what the alternative looks like when it is done, since they retain evidence of alternatives that were tested, restricted, replaced, or abandoned, which makes their public deployments the latest inspectable states of documented development histories.[^17]

## Gaps
- The hands-on chain of the lecture notes that walks through an implementation session belongs to the parallel writing lane, so this chapter carries no transcript of an agentic session and no example of a milestone sequence.
- The list of artefact kinds an agent produces from the specification comes from the outline. The sources describe the products of implementation in general terms, so the enumeration rests on the outline rather than on a passage of its own.
- Concrete practices of agent configuration, such as permission scoping and escalation design, are named here at the level the sources reach. A treatment with worked configurations would need the action-layer templates read as instructions rather than as document specifications.

[^1]: Grounded in [[30_assertions/implementation-proceeds-through-bounded-inspectable-increments]].
[^2]: Grounded in [[30_assertions/agentic-capability-arises-from-model-harness-and-environment]].
[^3]: Grounded in [[30_assertions/implementation-keeps-the-project-intelligible-and-testable]].
[^4]: Grounded in [[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]].
[^5]: Grounded in [[30_assertions/a-runnable-state-is-not-yet-a-promptotype]].
[^6]: Grounded in [[30_assertions/implementation-can-participate-in-the-formation-of-a-model]].
[^7]: Grounded in [[30_assertions/findings-arise-at-several-non-interchangeable-levels]].
[^8]: Grounded in [[30_assertions/a-finding-is-attributed-before-it-is-written-back]].
[^9]: Grounded in [[30_assertions/findings-about-agentic-work-change-the-arrangement]].
[^10]: Grounded in [[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]].
[^11]: Grounded in [[30_assertions/conformity-to-a-mapping-is-examined-separately-from-its-adequacy]].
[^12]: Grounded in [[30_assertions/interface-findings-concern-the-claims-a-representation-implies]].
[^13]: Grounded in [[30_assertions/write-back-makes-a-finding-durable]].
[^14]: Grounded in [[30_assertions/the-handoff-document-is-a-process-inbox]].
[^15]: Grounded in [[30_assertions/project-level-and-method-level-write-back-differ]].
[^16]: Grounded in [[30_assertions/a-failure-becomes-learning-only-through-interpretation]].
[^17]: Grounded in [[30_assertions/a-public-deployment-is-the-latest-state-of-a-development-history]].
