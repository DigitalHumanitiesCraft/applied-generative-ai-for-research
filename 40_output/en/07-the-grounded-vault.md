---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-knowledge-document-is-bounded-structured-and-revisable]]", "[[30_assertions/a-knowledge-document-is-materialised-context-compression]]", "[[30_assertions/a-knowledge-document-is-transferable-compact-and-retrievable]]", "[[30_assertions/an-external-memory-is-shared-between-human-and-agent]]", "[[30_assertions/atomisation-and-consolidation-run-in-opposite-directions]]", "[[30_assertions/context-quality-has-four-criteria]]", "[[30_assertions/distillation-abstracts-a-principle-from-a-case]]", "[[30_assertions/filing-information-is-modelling-work]]", "[[30_assertions/five-transformations-convert-material-into-units]]", "[[30_assertions/four-artefact-kinds-carry-different-duties]]", "[[30_assertions/four-design-principles-guide-the-transformations]]", "[[30_assertions/governance-and-curation-keep-a-holding-usable]]", "[[30_assertions/instruction-files-are-context-not-enforcement]]", "[[30_assertions/knowledge-engineering-makes-knowledge-explicit]]", "[[30_assertions/persistent-knowledge-keeps-change-visible]]", "[[30_assertions/provenance-has-a-standard-form-and-a-research-demand]]", "[[30_assertions/the-granularity-conflict-between-readers-is-unresolved]]", "[[30_assertions/the-knowledge-model-bounds-the-output]]", "[[30_assertions/the-structure-of-a-holding-is-meaning-bearing]]", "[[30_assertions/three-levels-separate-holding-task-and-window]]"]
posits: 6
lang: en
part: "II. From Prompting to Grounded Knowledge"
chapter: 7
title: "The Grounded Vault"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper (Project Knowledge Base)", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# The Grounded Vault

## What the term names

A Grounded Vault is a persistent knowledge environment shared by scholars and computational agents, in which sources, structured data, project knowledge, process memory, action instructions and verification material are maintained in a form that can be traced, criticised and revised. It is defined by the organisation and governance of what it holds rather than by an application, so a repository, a local file system, a plain-text note system or a comparable infrastructure can carry one.[^0]

The reading that makes the term more than a synonym for a folder comes from the sources. A holding of open text files is a materialised semantic net in which links, tags and hierarchies themselves carry meaning, because a link that is set, a tag that is chosen and a division of a document into smaller units decide how the knowledge can later be interpreted by a human reader and by a model alike, fixing which connections are visible, which concepts count as independent and how the net behaves under selective loading.[^1] Filing is therefore modelling, and structural maintenance forms a model of the project's own knowledge rather than tidying a directory.[^2] What that model is worth bounds what can be produced from it, which is the reason the environment is treated here as an object of design.[^3]

The pairing with an agent follows from a property of the systems described in Part I. A context window is a bounded and volatile working memory while a folder of open text files is the long-term store, and because the files are open the agent reads and writes exactly what a person reads and writes.[^4] An external memory of this kind organises individual and institutional knowledge, steers operative work and represents knowledge structures at the same time.

## The conditions

Seven conditions are usually named for such an environment, and they are not equally well supported by the sources this book draws on. Two of them hold without further argument. The environment has to be inspectable, so that people can read, criticise and revise what is maintained, and revisable, so that new findings alter the maintained layer instead of remaining in local outputs. Both follow from the definition of knowledge engineering as the construction and maintenance of explicit, inspectable and revisable project knowledge, whose scope covers acquisition, structuring, curation, provenance, revision and governance.[^5]

Being agent-operable follows from the shared external memory. The agent works on the same files as the person, so the property is a consequence of the format rather than an added feature.[^4] Being layered follows from the three levels that separate a persistent holding from a task-specific working context and from the technical window in which the context is processed, together with the further separation of four artefact kinds, a knowledge document describing a subject, an instruction file governing recurring work, a skill operationalising a procedure and a prompt formulating the current task.[^6]

Being versioned is carried by the observation that persistent project knowledge lets people and systems refer to the same documented state, so statements can be criticised, updated and linked to evidence while changes stay visible.[^7] The property that matters here is the visibility of revision rather than the storage of history.

The remaining two conditions need more care. Governance appears in the sources as a demand and not as a mechanism. It sets the rules for construction, change and use, curation applies them in a structural and a substantive form, an agent can localise problems and propose changes, and consequential changes have to be checked and answered for.[^8] What is missing is enforcement. An instruction file is context rather than a guarantee, and behavioural guidance is a different thing from permissions and hooks that can hold a boundary independently of whether a model complies.[^9] A vault is governed to the extent that it separates the two, and the sources of this lane state the demand without describing an architecture that meets it.[^10]

Being source-bound is the condition the sources reach for and do not supply. Provenance is required by all of them and carries a genuine inheritance, a machine-readable standard with entity, activity, agent and a derivation relation, and a research-practical demand in the FAIR principles, while putting knowledge into filable documents is knowledge codification with a stage model of capturing, packaging and reusing.[^11] Within a document the demand is met by a sources section and by frontmatter recording creation, source and status.[^12] What none of the sources describes is a chain that binds an individual statement to the passage supporting it. That chain is this book's own extension, and it is what the vault behind this manuscript adds to the practice the sources describe.[^13]

## The unit and its production

The environment is built from knowledge documents. Each brings the statements relevant to one delimited subject together in a checkable form, bounded in subject, traceable in structure, visible in its uncertainties, documented in its provenance, revisable, dual-readable and compact in a way that keeps the differentiations its purpose requires.[^14] Its function inside a context is what makes it worth maintaining, because it is a condensation performed in advance that a model no longer has to make from raw material each time.[^15]

A document earns that function by being transferable, compact and retrievable, so the knowledge stays applicable to situations unknown when it was written, only what the application needs is present, and headings, metadata and structure make the knowledge quickly reactivatable.[^16] The route to such a document runs from a concrete case through the extraction of patterns and their abstraction into principles detached from the single instance to a condensation into a storable form, and the acceptance test is whether someone who reads only the document can apply the principle to a new case without asking questions.[^17]

The environment changes through a small set of operations. Five transformations convert material into units, compression or distillation, normalisation, enrichment, consolidation and atomisation.[^18] Two of them are directional opposites serving the same end, atomisation dividing a monolithic record into atomic documents while the original becomes a map, consolidation merging documents with redundant foundations into one with the redundancy removed, both aiming at one concept in one unit.[^19] Four principles guide them, one concept per document, self-containedness, information density and secured provenance, and self-containedness is the one that decides usability as context.[^20] Judged as context, a usable document is of middling size, carries frontmatter, sections and sources, explains itself and duplicates nothing held elsewhere.[^21]

## Curated and generated knowledge

Two kinds of content sit in such an environment and must not be treated alike. Curated documents stay under scholarly responsibility even where a model assisted in drafting them, and generated documents are rendered from data by a named process and are overwritten when that process runs again. The distinction decides whether an edit is a contribution or a loss, and it is one the sources of this lane do not draw.[^22]

What the sources do supply is the maintenance regime that keeps either kind usable. A holding loses usability without curation, documents go out of date, terms become inconsistent and parallel versions contradict one another, so governance sets the rules and curation applies them structurally to names, metadata, links, document types, versions and duplicates and substantively to contradictions, outdated rules, missing constraints, inappropriate condensations and the revision of requirements.[^8]

One question stays open across all of this. A model built for human reading and one built for machine context can demand different granularity, the conflict between compact machine readability and detailed human traceability is unresolved in the sources, and how the quality of a knowledge model could be measured at all is equally open.[^23] A book that recommends building such an environment has to say that the recommendation rests on practice rather than on a measurement.[^24]

## Gaps

Three points of the outline are covered only in part.[^25]
- The distinction between curated and deterministically generated knowledge is named here and grounded in nothing. No source of this lane draws it, and the document typology of the other manuscript lane is where it belongs, so chapter 14 carries it.
- The list of what a Grounded Vault may include, from schemas and standards through verification concepts to published artefacts, is stated in the outline and appears in these sources only as the looser list of what a maintained environment holds. The Promptotyping paper distillate is the place to ground the fuller list.
- The seven conditions are treated here by grounding each one separately, and the number seven is the outline's own count. Whether the set is complete is a question no source of this lane can answer.

[^0]: Posit: the term Grounded Vault and the definition given here are this book's own, assembled from the properties its sources describe separately. Open evidence question: whether an environment that satisfies the definition can be recognised as such by a reader who has only the definition and one implemented instance.
[^1]: Grounded in [[30_assertions/the-structure-of-a-holding-is-meaning-bearing]].
[^2]: Grounded in [[30_assertions/filing-information-is-modelling-work]].
[^3]: Grounded in [[30_assertions/the-knowledge-model-bounds-the-output]].
[^4]: Grounded in [[30_assertions/an-external-memory-is-shared-between-human-and-agent]].
[^5]: Grounded in [[30_assertions/knowledge-engineering-makes-knowledge-explicit]].
[^6]: Grounded in [[30_assertions/three-levels-separate-holding-task-and-window]], [[30_assertions/four-artefact-kinds-carry-different-duties]].
[^7]: Grounded in [[30_assertions/persistent-knowledge-keeps-change-visible]].
[^8]: Grounded in [[30_assertions/governance-and-curation-keep-a-holding-usable]].
[^9]: Grounded in [[30_assertions/instruction-files-are-context-not-enforcement]].
[^10]: Posit: reading the governed condition as satisfied only where guidance and enforcement are separated is this book's own criterion, and no source states it. Open evidence question: a comparison of projects that separate the two against projects that do not, measured on unauthorised changes to a maintained holding.
[^11]: Grounded in [[30_assertions/provenance-has-a-standard-form-and-a-research-demand]].
[^12]: Grounded in [[30_assertions/four-design-principles-guide-the-transformations]].
[^13]: Posit: the anchor chain that binds an individual statement to a supporting passage is this book's extension of the practice its sources describe, and it is the mechanism by which this manuscript itself is written. Open evidence question: whether the chain survives contact with a project whose sources cannot be stored in full, where a quotation has to take the place of a block reference.
[^14]: Grounded in [[30_assertions/a-knowledge-document-is-bounded-structured-and-revisable]].
[^15]: Grounded in [[30_assertions/a-knowledge-document-is-materialised-context-compression]].
[^16]: Grounded in [[30_assertions/a-knowledge-document-is-transferable-compact-and-retrievable]].
[^17]: Grounded in [[30_assertions/distillation-abstracts-a-principle-from-a-case]].
[^18]: Grounded in [[30_assertions/five-transformations-convert-material-into-units]].
[^19]: Grounded in [[30_assertions/atomisation-and-consolidation-run-in-opposite-directions]].
[^20]: Grounded in [[30_assertions/four-design-principles-guide-the-transformations]].
[^21]: Grounded in [[30_assertions/context-quality-has-four-criteria]].
[^22]: Posit: the distinction between curated and deterministically generated content is taken from the outline and is grounded in no source of this lane. Open evidence question: whether the Promptotyping paper distillate carries it, and with which criterion it decides the case of a generated document a person has since edited.
[^23]: Grounded in [[30_assertions/the-granularity-conflict-between-readers-is-unresolved]].
[^24]: Posit: naming the recommendation as resting on practice rather than measurement follows from the open question the sources leave. Open evidence question: a measure of knowledge-model quality that could be applied to two holdings and compared.
[^25]: Posit: the gap list records where this chapter falls short of the outline. Open evidence question: whether the seven conditions form a complete set, which only a comparison across several implemented environments could settle.
