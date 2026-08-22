---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-demonstrator-can-carry-a-project-before-its-corpus-exists]]", "[[30_assertions/acceptance-is-purpose-specific-and-bounded]]", "[[30_assertions/data-governance-bounds-what-may-be-processed]]", "[[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]]", "[[30_assertions/proprietary-dependence-limits-durability]]", "[[30_assertions/the-accepted-state-must-remain-identifiable]]", "[[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]]", "[[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]]", "[[30_assertions/the-boundary-to-research-software-engineering]]", "[[30_assertions/the-handoff-document-is-a-process-inbox]]", "[[30_assertions/the-integration-document-holds-the-contract-at-the-boundary]]", "[[30_assertions/the-method-redistributes-implementation-labour]]", "[[30_assertions/the-provenance-of-a-generated-process-is-documentary]]", "[[30_assertions/the-report-addresses-an-external-reader]]"]
posits: 3
lang: en
part: "VI. Worked Example, Boundaries, and Implications"
chapter: 22
title: "From Promptotype to Research Software Engineering"
topic: "[[Boundaries-and-Implications]]"
feeding-sources: ["paper chapter 4", "hands-on chains from slides and script"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# From Promptotype to Research Software Engineering

## The boundary is a change of obligation

The technical and organisational boundary of Promptotyping is reached when the obligations attached to an artefact change. Collaboration with Research Software Engineers remains essential for artefacts that require dependable long-term operation, institutional integration, security, or supported use by third parties, the expertise and resources for that work are not evenly available, and the method is inappropriate where contributors cannot reconstruct or assess the relation among sources, research data, maintained knowledge, implementation, and output.[^1]

What makes the boundary legible from inside a project is the accepted purpose. Acceptance is purpose-specific and bounded, so an artefact may be accepted as an experimental processing pipeline, an internal workflow, a proposal-stage demonstrator, or a handover state without any of those acceptances claiming production readiness.[^2] A change of accepted purpose towards institutional operation moves the artefact across the boundary whether or not a line of its code changes. Evaluating it then changes with it, since technical conformity, scholarly adequacy, and suitability for the stated purpose are separate questions and an exploratory artefact need not satisfy production criteria that lie outside its accepted scope.[^3]

## Why static and self-contained is often the right form

For bounded research purposes a static, self-contained artefact is often appropriate, because it can run locally, be deployed through static hosting, avoid persistent backend infrastructure, reduce dependency chains, remain inspectable, and support archiving.[^4] The documented proposal-stage case took exactly that form, in that a bounded path led from a limited textual sample through an encoded representation to a statically hosted edition interface, which made a proposed arrangement examinable without a production infrastructure behind it.[^5] The form also fits the durability requirement of an accepted state, which has to remain identifiable and reconstructable through a release, an archived deposit, or another durable reference.[^6]

The limits of the form are equally definite. Browser memory and large-scale computation bound what a self-contained artefact can process, and shared state, authentication, simultaneous editing, persistent writes, security requirements, accessibility obligations, and continuing institutional support each introduce an obligation the form does not carry.[^4] Where these become central to what the artefact has to do, the artefact has entered the domain of Research Software Engineering.

Two constraints from earlier chapters bear on the same decision. Data governance bounds which materials and workflows may be used at all, since permissibility depends on the material and on legal, institutional, and architectural conditions, agent access has to be bounded through controlled permissions and attributable actions, and purpose-specific scholarly acceptance does not replace institutional responsibility for secure, sustainable, and legally compliant operation.[^7] And dependence on proprietary frontier systems introduces direct costs, reduces control over system changes, and sits in tension with the inspectability, reproducibility, and durability sought for research software, since model and harness changes may alter behaviour while project knowledge and data stay stable.[^8]

## The handover

A handover to professional engineering is a contract at a project boundary, and the method already has a document type for that shape, which holds the currently valid exchange format, the responsibilities, and the acceptance criteria, with exactly one side declared the source of truth where both sides describe it.[^9] What such a handover has to contain follows from what the receiving side would otherwise reconstruct from code, meaning the research context, the source and data descriptions, the requirements, the design decisions, the test and verification concepts, the known limitations, the dependency inventory, the process history, the provenance, and the unresolved questions.[^10]

Most of that is already written in a project that worked in this way. The material document carries source and data descriptions, the specification carries requirements and decisions, the design document carries the representational choices, the test document carries guarantees and deliberate gaps, the provenance record carries the history of transitions with their verdicts, and the process inbox carries what is still open.[^11] The provenance record earns particular attention at a handover, because where interaction logs are not retained, the persistent provenance of a generated process consists of the maintained knowledge, the working record, the sources, the documented decisions, and the version history, and those materials cannot reproduce every discarded alternative or element of tacit judgement.[^12] A receiving team that knows this reads the record for what it does carry rather than for what it appears to promise.

One document type in the set was written for exactly this addressee. A status report is the only document of the method whose reader is external, condensing a state for a third party without prior knowledge of the repository and separated from the internal provenance record by lifecycle and curation rather than by content.[^13]

## What a handover does not remove

Promptotyping can make a handover more inspectable, and it cannot remove the expertise and resources that sustainable research software requires.[^1] The redistribution of labour is the reason to say so plainly. An agent may produce a functional artefact rapidly while domain specialists still specify, examine, interpret, and accept, and Research Software Engineers may later refactor the implementation for dependable operation, so evaluation has to distinguish effort that is reduced from effort that is transferred, newly created, or deferred.[^14] The receiving side of a handover is where deferred effort arrives, and the roles absorb it unevenly, since Research Software Engineers may inherit technical debt while those responsible for verification face more plausible outputs without corresponding resources or authority.[^15]

The proportionality rule applies to the handover as it applies to the work before it. A bounded transformation on a stable format hands over with concise mappings and formal checks, while work spanning interpretation, modelling, implementation, and verification hands over an explicit account of sources, assumptions, requirements, and limitations.[^16] Writing more than the case requires wastes the capacity the method was meant to free, and writing less moves the reconstruction cost onto the receiving side without recording that it was moved.[^17]

## Gaps
- The advantages and limits of static, self-contained artefacts are enumerated in the outline. The sources carry one documented instance of the form and the general boundary criterion, so the enumerations here rest on the outline and are marked as such.
- The composition of a handover package likewise comes from the outline. The chapter grounds each element in the document type that already holds it and treats the list itself as the book's own arrangement.
- The hands-on chains of the lecture notes and the slide deck feed Part VI and belong to the parallel writing lane, so no worked handover example was available.
- No documented handover to a Research Software Engineering team is described in the sources, which is why the effects of the arrangement on a receiving team stay an open evidence question.

[^1]: Grounded in [[30_assertions/the-boundary-to-research-software-engineering]].
[^2]: Grounded in [[30_assertions/acceptance-is-purpose-specific-and-bounded]].
[^3]: Grounded in [[30_assertions/promptotype-evaluation-separates-conformity-adequacy-and-purpose]].
[^4]: Posit: the advantages and the limits of the static, self-contained form are stated in the outline, and the sources name the boundary criterion without enumerating the technical properties on either side of it. Open evidence question: a comparison of documented artefacts by deployment form against the obligations each of them actually had to carry.
[^5]: Grounded in [[30_assertions/a-demonstrator-can-carry-a-project-before-its-corpus-exists]].
[^6]: Grounded in [[30_assertions/the-accepted-state-must-remain-identifiable]].
[^7]: Grounded in [[30_assertions/data-governance-bounds-what-may-be-processed]].
[^8]: Grounded in [[30_assertions/proprietary-dependence-limits-durability]].
[^9]: Grounded in [[30_assertions/the-integration-document-holds-the-contract-at-the-boundary]].
[^10]: Posit: the contents of a handover package follow from what a receiving team would otherwise have to infer from the code, and the outline lists them without a source in this vault carrying the list. Open evidence question: a documented handover in which the receiving team recorded which of these elements it used and which it still had to reconstruct.
[^11]: Grounded in [[30_assertions/the-handoff-document-is-a-process-inbox]].
[^12]: Grounded in [[30_assertions/the-provenance-of-a-generated-process-is-documentary]].
[^13]: Grounded in [[30_assertions/the-report-addresses-an-external-reader]].
[^14]: Grounded in [[30_assertions/the-method-redistributes-implementation-labour]].
[^15]: Grounded in [[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]].
[^16]: Grounded in [[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]].
[^17]: Posit: an under-documented handover transfers the reconstruction cost silently, because the receiving side discovers the omission only while paying it. Open evidence question: whether receiving teams record such costs in a form that would allow the comparison.
