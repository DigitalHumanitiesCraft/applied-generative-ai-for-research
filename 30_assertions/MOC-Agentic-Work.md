---
type: moc
topic: "Agentic-Work"
created: 2026-08-22
updated: 2026-08-22
---

# MOC: Agentic-Work

Assertions on agentic systems as a form of work organisation, on the span of work between two human interventions, and on the failure modes that better prompt wording cannot reach. The topic carries Part III of the manuscript.

- [[30_assertions/an-agent-pursues-a-goal-across-several-calls]] — what makes a system an agent
- [[30_assertions/the-scope-of-action-comes-from-tools-and-environment]] — where the ability to act actually comes from
- [[30_assertions/the-execution-loop-is-a-control-loop]] — the shape of the agentic cycle and its older name
- [[30_assertions/autonomy-is-the-span-between-interventions]] — the measure the word autonomy carries here
- [[30_assertions/the-shift-is-from-response-to-trajectory]] — what has to be organised once work runs across steps
- [[30_assertions/agents-predate-language-models]] — the older concept behind the current systems
- [[30_assertions/the-semantic-web-took-the-reverse-route]] — the older route to the same goal and where it differs
- [[30_assertions/single-agent-and-federation-are-two-modes]] — the two modes a single system can run in
- [[30_assertions/agentic-engineering-organises-multi-step-work]] — the definition of the fourth layer and its reach
- [[30_assertions/the-organisation-requirements-are-explicit]] — what has to be settled before a long run begins
- [[30_assertions/least-privilege-and-reversibility-bound-the-run]] — the two bounds placed on what an agent may do
- [[30_assertions/plans-stay-compact-and-revisable]] — what a usable plan looks like and when it misleads
- [[30_assertions/feedback-arrives-from-several-sources]] — where the information that steers a run comes from
- [[30_assertions/increments-must-stay-inspectable]] — the properties of a checkable increment
- [[30_assertions/intervention-points-are-named-in-advance]] — where a run is designed to stop for a person
- [[30_assertions/tool-protocols-solve-integration-not-relevance]] — what a tool standard settles and what it leaves open
- [[30_assertions/agent-to-agent-protocols-address-a-second-surface]] — the second standardised surface and what it leaves unsettled
- [[30_assertions/subagents-bound-context-and-parallelise]] — what delegation to a child instance buys and costs
- [[30_assertions/more-agents-raise-coordination-cost]] — the cost side of multi-agent arrangements
- [[30_assertions/skills-package-procedure-with-progressive-disclosure]] — how a reusable procedure is packaged and loaded
- [[30_assertions/the-mechanisms-are-not-interchangeable]] — the decision behind the vocabulary of agent components
- [[30_assertions/model-routing-separates-functions]] — how phases of work are assigned to models
- [[30_assertions/an-early-error-propagates-along-the-trajectory]] — how one early defect reaches the end of a run
- [[30_assertions/long-runs-accumulate-noise]] — the second failure mode of long trajectories
- [[30_assertions/implementation-tests-the-project-understanding]] — what an implementation reveals about the documented understanding
- [[30_assertions/the-interface-can-manufacture-false-certainty]] — the failure an artefact can commit while working correctly
- [[30_assertions/findings-must-be-written-back]] — the return path from implementation into the holding
- [[30_assertions/the-prompt-is-one-component-of-the-loop]] — the place of the instruction inside the development cycle
- [[30_assertions/specification-precedes-implementation]] — what stands between discussion and code
- [[30_assertions/checking-a-run-covers-behaviour-data-and-requirements]] — what a verification pass over a generated artefact covers

## Open questions

- Which failure modes are documented in the sources with a case, and which are asserted without one?
- Is verification debt a term of a source or a coinage of this book?
- The sources carry error propagation, context noise and false certainty in the interface, and they name neither implementation drift, uncontrolled dependency growth, overengineering nor automation bias, so those four rungs of the outline have no anchor.
- The sources state that a defect can originate in different layers without giving a procedure for deciding which layer a given defect belongs to.
- The principle of least necessary permission is stated without a rule for determining which permission an individual task requires.
- The sources report that accumulated unchecked output is a risk without naming a way to measure how much of it a project is carrying.
