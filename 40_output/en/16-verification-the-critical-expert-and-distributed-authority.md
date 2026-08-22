---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-reproducible-metric-does-not-validate-its-own-specification]]", "[[30_assertions/a-verification-names-its-own-ceiling]]", "[[30_assertions/acceptance-is-purpose-specific-and-bounded]]", "[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/agentic-review-investigates-rather-than-scores]]", "[[30_assertions/agentic-review-yields-probabilistic-evidence]]", "[[30_assertions/critical-expert-verification-records-who-is-responsible]]", "[[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]]", "[[30_assertions/data-production-becomes-accountable-through-a-reconstructable-relation]]", "[[30_assertions/deterministic-verification-is-bounded-by-its-checks]]", "[[30_assertions/inspection-is-separated-from-the-authority-to-record]]", "[[30_assertions/scholarly-validation-judges-the-governing-representations]]", "[[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]]", "[[30_assertions/the-accepted-state-must-remain-identifiable]]", "[[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]]", "[[30_assertions/verification-documents-are-adversarial-and-precede-the-claim]]", "[[30_assertions/verification-is-delimited-against-testing-and-provenance]]"]
posits: 2
lang: en
part: "IV. Promptotyping"
chapter: 16
title: "Verification, the Critical Expert, and Distributed Authority"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Verification, the Critical Expert, and Distributed Authority

## Four forms of assessment

Adequacy in scholarly research depends on the interpretation of sources, on the modelling decisions through which they are represented, and on the purpose the resulting data serve, so conformity to a specification settles only part of the question. Technical verification asks whether an output conforms to formalised requirements, scholarly validation asks whether the representation those requirements encode is warranted by the source material and adequate for its purpose, and an implementation can therefore be correct and inadequate at the same time.[^1] The method separates four forms of assessment along that fault line, and their differences became consequential in the documented workflows rather than remaining a taxonomy.[^2]

Deterministic verification tests conformity through schemas, constraints, transformation tests, structural audits, and reproducible measurements. Its conclusions reach exactly as far as the properties its checks encode, and it establishes nothing about whether the requirements themselves are adequate.[^3] Its worked limiting case is a reproducible metric. Character error rate can be calculated identically by anyone once the reference text, the extraction rules, the normalisation, the comparison scope, and the calculation procedure are fixed, and it measures deviation from a selected reference rather than transcription correctness, so the choice and quality of that reference, the treatment of corrections and annotations, the exclusion of particular phenomena, and the reading of the resulting value all remain editorial decisions.[^4]

Agentic review is a bounded, tool-supported investigation in which one or more language-model-based agents examine outputs, data states, implementations, or artefacts against sources, references, requirements, and criteria. It may locate project files, compare sources and outputs, execute formal checks, investigate discrepancies, or coordinate specialised, parallel, or adversarial reviewers, which distinguishes it from a rubric-based judgement that scores a supplied output; such judging can be one operation within agentic review without exhausting it.[^5] Its evidential value depends on how the investigation is organised, meaning how tasks are delimited, which knowledge and sources are supplied, which tools and permissions are available, how several reviewers are coordinated, and when unresolved cases are escalated. It extends the scope and depth of inspection, and its findings stay probabilistic evidence.[^6]

Critical Expert verification and adjudication is the accountable examination of particular outputs against their sources and the resolution of cases the other procedures cannot determine. It can confirm, correct, or reject earlier findings, and it records who assumes responsibility for the resulting judgement.[^7] Scholarly validation takes a wider object, since it asks whether the representations, requirements, evaluation criteria, and artefacts governing a workflow are warranted by the research material and adequate for their intended scholarly purpose.[^8]

Running artefacts are also inspected operationally, for behaviour, layout, readability, missing elements, inconsistent labels, and discrepancies between specification and rendering. That kind of looking is a mode of examination shared across the forms rather than a fifth authority, since the same observation may be recorded as a failed formal check, as an agentic finding, or as an expert judgement depending on who makes it and against what.[^9]

## What the Critical Expert decides

The Critical Expert determines whether the data have been represented appropriately, whether the research question is meaningfully addressed, whether interpretations are supported, whether uncertainty and missingness are treated adequately, whether relevant alternatives have been considered, and whether the output can be accepted as part of scholarly work. Acceptance rests with that role, understood as the person or group competent and accountable for judging whether the project knowledge adequately represents the research material and whether the artefact suits its purpose, and an agent may contribute proposals and assessments without assuming responsibility for their adequacy.[^10]

The role requires more than a human position in a workflow. Maintained project knowledge guides implementation without determining a single adequate realisation, because natural-language descriptions retain ambiguity and different runs may realise the same requirement in materially different ways, so the examination has to reach past detecting errors in generated content to whether relevant alternatives were excluded, whether conventions were reproduced without justification, and whether absences were concealed by an artefact that looks coherent.[^11] That is a competence in the research domain combined with an awareness of how generative systems fail.

Two forms of judgement are at work and may be held by one person or distributed. Scholarly judgement concerns sources, data, interpretation, representation, and research claims. Agentic-engineering judgement concerns decomposition, tools, permissions, testing, implementation strategy, and the diagnosis of technical failures.[^12] Critical expertise may accordingly be held by one hybrid scholar-developer or distributed among contributors with complementary competencies, and agentic work may be divided among agents on bounded components, which changes the coordination without transferring responsibility, keeps assignments and permissions explicit and auditable, limits access to the delegated task, and may increase the work of auditing rather than reduce it.[^12]

## The line between inspecting and authorising

The sharpest rule of the arrangement came out of a failure. In one documented workflow an agent-screening process assigned approval labels although no responsible contributor had granted approval; the labels were abolished and the findings were reclassified as provisional evidence pending adjudication. The general rule is that agents may assemble evidence, compare materials, investigate discrepancies, execute checks, and record provisional assessments, and that they may not independently assign an authorised verification status, a scholarly validation, an approval, or an acceptance.[^13] The capacity to inspect an output and the authority to record it as verified are separate, and a system that conflates them produces states no one has stood behind.

The documentary counterpart of that rule is a verification document. Its trigger is the externally effective claim rather than the existence of data, so a project that only explores internally needs none, and it comes into being before the first such claim leaves the project, because a verification supplied afterwards examines an already published formulation and can only restrict it. Its stance is adversarial, in that the procedure tries to refute its own claims, and the binding rule is that an outward claim may be used only in the form the verification licenses.[^14] It is delimited against the neighbouring functions by object and by time, since quality assurance examines system behaviour against the specification while verification examines whether substantive claims are covered by the raw data, and the provenance record holds the chronology while verification is the synchronous examination of one claim against its evidence. It also names the units under examination and the reference standard they are held against.[^15] And it states what its own procedure structurally cannot achieve, for example that ground-truth-free procedures measure plausibility rather than correctness, that agreement among several models guarantees no truth, and that errors below the detection threshold pass; a verification without named limits is incomplete.[^16]

## Distributed authority

Authority in this arrangement is distributed. It is not handed from one instance to the next. The data provide the evidential basis. The maintained documents provide the procedural reference from which implementation proceeds and against which it is judged. Deterministic systems decide the questions that have been formalised. Models extend the reach of implementation and of review. The Critical Expert retains responsibility wherever acceptance depends on scholarly judgement.[^17]

Acceptance closes an iteration under that division. It is purpose-specific and bounded, so an artefact may be accepted as an experimental processing pipeline or a handover state without being accepted as a completed edition, and it does not imply that knowledge, data, or artefact have become final.[^18] What it does require is that the accepted state stay identifiable and reconstructable through a repository release, an archived deposit, or another durable reference, and that a renewed implementation with another model, harness, or project state be treated as a new iteration.[^19] Accountability in agent-supported work rests on that reconstructable relation among sources, maintained project knowledge, versioned implementation, differentiated evidence, and responsible judgement, and the significance of a documented workflow lies as much in its rejected assumptions, detected validation gaps, withdrawn approval states, corrected readings, and documented limitations as in what it produced.[^20]

## Gaps
- The outline names operational and visual inspection as a form of assessment in its own right, while the sources describe four forms in which such inspection is an operation rather than an authority. The chapter follows the sources and marks the difference as its own reading.
- Chapter 7 of the lecture notes treats verification and write-back for a teaching audience and belongs to the parallel lane, so its formulation of the Critical Expert could not be compared with the paper's.
- The list of what the Critical Expert determines comes from the outline. The sources carry the substance of each item, and the enumeration itself follows the outline.
- The machine-review contract of this vault requires a reviewer from a different model family than the producing agent, which the project has not yet fixed. The forms of assessment described here are therefore stated and not yet exercised on this chapter.

[^1]: Grounded in [[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]].
[^2]: Grounded in [[30_assertions/inspection-is-separated-from-the-authority-to-record]].
[^3]: Grounded in [[30_assertions/deterministic-verification-is-bounded-by-its-checks]].
[^4]: Grounded in [[30_assertions/a-reproducible-metric-does-not-validate-its-own-specification]].
[^5]: Grounded in [[30_assertions/agentic-review-investigates-rather-than-scores]].
[^6]: Grounded in [[30_assertions/agentic-review-yields-probabilistic-evidence]].
[^7]: Grounded in [[30_assertions/critical-expert-verification-records-who-is-responsible]].
[^8]: Grounded in [[30_assertions/scholarly-validation-judges-the-governing-representations]].
[^9]: Posit: treating operational and visual inspection as a mode of examination rather than as a fifth authority follows from the four forms being distinguished by the authority of their verdicts, since the same observation carries a different weight depending on who records it and against what. Open evidence question: whether any source treats operational inspection as an authority of its own.
[^10]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^11]: Grounded in [[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]].
[^12]: Grounded in [[30_assertions/critical-expertise-may-be-distributed-without-transferring-responsibility]].
[^13]: Grounded in [[30_assertions/inspection-is-separated-from-the-authority-to-record]].
[^14]: Grounded in [[30_assertions/verification-documents-are-adversarial-and-precede-the-claim]].
[^15]: Grounded in [[30_assertions/verification-is-delimited-against-testing-and-provenance]].
[^16]: Grounded in [[30_assertions/a-verification-names-its-own-ceiling]].
[^17]: Posit: the five-part division of authority among data, documents, deterministic systems, models, and Critical Experts restates the four forms of assessment as a standing arrangement, and the sources describe the forms without setting out the arrangement in these terms. Open evidence question: whether the lecture notes state the division of authority explicitly.
[^18]: Grounded in [[30_assertions/acceptance-is-purpose-specific-and-bounded]].
[^19]: Grounded in [[30_assertions/the-accepted-state-must-remain-identifiable]].
[^20]: Grounded in [[30_assertions/data-production-becomes-accountable-through-a-reconstructable-relation]].
