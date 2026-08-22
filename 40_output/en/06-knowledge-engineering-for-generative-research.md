---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-file-collection-is-not-a-knowledge-base]]", "[[30_assertions/a-knowledge-base-is-purpose-bound]]", "[[30_assertions/a-knowledge-document-is-bounded-structured-and-revisable]]", "[[30_assertions/a-knowledge-document-is-materialised-context-compression]]", "[[30_assertions/a-knowledge-document-is-transferable-compact-and-retrievable]]", "[[30_assertions/atomisation-and-consolidation-run-in-opposite-directions]]", "[[30_assertions/context-quality-has-four-criteria]]", "[[30_assertions/distillation-abstracts-a-principle-from-a-case]]", "[[30_assertions/filing-information-is-modelling-work]]", "[[30_assertions/five-transformations-convert-material-into-units]]", "[[30_assertions/four-artefact-kinds-carry-different-duties]]", "[[30_assertions/four-design-principles-guide-the-transformations]]", "[[30_assertions/governance-and-curation-keep-a-holding-usable]]", "[[30_assertions/instruction-files-are-context-not-enforcement]]", "[[30_assertions/instruction-files-externalise-stable-rules]]", "[[30_assertions/knowledge-acquisition-has-two-sources]]", "[[30_assertions/knowledge-engineering-makes-knowledge-explicit]]", "[[30_assertions/markdown-exposes-structure-without-guaranteeing-content]]", "[[30_assertions/provenance-has-a-standard-form-and-a-research-demand]]", "[[30_assertions/the-document-is-the-concept-and-markdown-a-serialization]]", "[[30_assertions/the-five-part-systematics-is-an-own-coinage]]", "[[30_assertions/the-formalisation-target-has-shifted]]", "[[30_assertions/the-gap-is-between-possessed-and-available-knowledge]]", "[[30_assertions/the-granularity-conflict-between-readers-is-unresolved]]", "[[30_assertions/the-knowledge-model-bounds-the-output]]", "[[30_assertions/the-knowledge-system-is-a-production-system]]", "[[30_assertions/the-structure-of-a-holding-is-meaning-bearing]]", "[[30_assertions/the-transformations-are-anchored-in-older-disciplines]]", "[[30_assertions/three-traditions-feed-the-practice]]"]
posits: 1
lang: en
part: "II. From Prompting to Grounded Knowledge"
chapter: 6
title: "Knowledge Engineering for Generative Research"
topic: "[[Grounded-Knowledge]]"
feeding-sources: ["script chapters 3 to 5", "paper (Project Knowledge Base)", "Vault als materialisiertes Wissensmodell"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Knowledge Engineering for Generative Research

## The prior question

Context Engineering decides what is available during one interaction. Knowledge Engineering answers the earlier and more durable question of how project knowledge is represented, maintained, related and made reusable across interactions, and it makes terms, rules, decisions, constraints and uncertainties visible enough to be read, criticised and continued. Its shift of focus runs from files to maintained knowledge, so its scope covers acquisition, structuring, curation, provenance, revision and governance.[^1]

The starting point is a gap. Experts rely on tacit distinctions, remembered decisions, local file structures, disciplinary conventions and experience that no one has represented, a model cannot use what remains in a person's memory, and an agent cannot reconstruct conventions that were never written down. The question is therefore whether the relevant knowledge has been externalised in a usable and revisable form.[^2]

Having the files does not close that gap. Knowledge in a project is distributed across guidelines, correspondence, examples and the experience of individuals, and long-standing participants supply the missing connections without noticing they do it. An agent can search everything and still mix an old rule with a new one or generalise a single example into a convention, because existing local order is not yet a holding usable across a system.[^3] The failure is worth stating precisely, because it looks like a retrieval problem and is a representation problem.

## Where the knowledge comes from

Two sources feed a holding. Existing documents and data are prepared and converted into machine-readable and distilled forms, and knowledge standing in no document is raised through document analysis, interviews, workshops, observation of workflows, error analysis and joint modelling, then brought into the same structured form. The implicit part covers the reasons for earlier decisions, known exceptions, expectations of the target artefact, acceptance criteria and practical experience with particular source types, and a rule practised for years may appear in no guideline until an interview surfaces it.[^4]

What has changed against the classical reading of the term is the formalisation target. Knowledge Engineering comes from the expert-system tradition, and structured natural language with a light metadata component now suffices where logic and ontology were once required, because the language model supplies the language understanding that a formal representation previously had to encode.[^5] The older traditions still feed the practice. Knowledge modelling identifies the concepts of a domain and makes them queryable, personal information management studies how people acquire, organise, maintain, retrieve, use and share information across formats and locations with fragmentation as its core problem, and project management contributes procedures for initiating, planning, executing, monitoring and closing work. A maintained environment therefore holds conceptual definitions, source references, requirements, decisions, process descriptions, instructions, open questions and evaluation criteria at once.[^6]

The holding stays purpose-bound. It carries the part of the knowledge required for particular forms of work, decision and checking, and completeness is not its criterion.[^7] That is easier to hold to once the purpose is stated, because the system serves the derivation of target artefacts rather than storage. Curated and condensed documents are the input of the step that produces a concept, a proposal, a specification or a data model, and the user story bridges the two activities by putting a requirement into a form a person understands and an agent can use as context. Requirements themselves arise from the relation among data, research questions and scholarly practices rather than from the data model alone.[^8]

## The unit and its properties

A knowledge document brings the statements relevant to one delimited subject together in a checkable form, so that a rule, its exceptions and its consequences can be read in one place instead of being searched again for every task. It is bounded in subject, traceable in structure, visible in its uncertainties, documented in its provenance, revisable, dual-readable for people and for models, and compact in a way that keeps the differentiations its purpose requires.[^9]

The document is a concept rather than a file format. Plain text with light structure is used here because it is open, versionable, linkable and readable by people and models alike, and the format exposes structure with little markup while guaranteeing nothing about content. It creates a shared surface on which people and agents work on the same holding, and it is not superior to richer formats where encoding standards, structured data formats, databases or schemas are required by their semantics or constraints.[^10]

What makes such a document worth writing is what it does in a context. It is materialised context compression, a condensation performed in advance that a model no longer has to make from raw material each time.[^11] The properties follow from that function. A good document is transferable, so the knowledge stays applicable to situations unknown when it was written, compact, so only what the application needs is present, and retrievable, so headings, metadata and structure make it quickly reactivatable, and it presupposes a reader who knows the context or can work it out.[^12]

The production of one has a shape and an acceptance test. Distillation moves from a concrete case through the extraction of patterns and their abstraction into principles detached from the single instance to a condensation into a storable form, the result applies independently of its originating example, and the test is whether someone who reads only the document can apply the principle to a new case without asking questions.[^13] Judged as context, a usable document is of middling size rather than a stub or a monolith, carries frontmatter, sections and sources, explains itself without presupposing other documents, and duplicates nothing held elsewhere.[^14]

## Operations on the holding

A holding changes through a small set of operations. Knowledge transformations convert information into reusable, contextualised structures, and five of them carry the procedure, compression or distillation, normalisation, enrichment, consolidation and atomisation, each defined by its input, its output and the direction of its information flow.[^15] Two of them run in opposite directions and serve the same end. Atomisation divides a monolithic record in which many separately referenceable concepts lie mixed into atomic documents while the original becomes a map that points to them, consolidation merges several documents with redundant foundations into one with the redundancy removed, and both aim at the clean assignment of one concept to one unit.[^16]

Four principles guide the operations. One concept inhabits exactly one document, every document stays understandable on its own, information density is maximised per token without redundancy across documents, and provenance is secured through a sources section and frontmatter. Self-containedness is the principle that decides usability as context, because the context a document needs has to stand inside it rather than only in its links.[^17]

The operations are not invented. Compression corresponds to abstracting, normalisation to formal description according to a rule set, enrichment to subject indexing and semantic description, consolidation to information consolidation with its separation of restructuring from repackaging, and atomisation to the monographic principle of documentation and to a card-index practice with atomic, fixed-address, cross-linked units.[^18] Provenance likewise carries an inheritance, a machine-readable standard with entity, activity, agent and a derivation relation, and a research-practical demand in the FAIR principles, while the whole procedure of putting knowledge into filable documents is knowledge codification with a stage model of capturing, packaging and reusing.[^19] The five-part scheme itself is a coinage. No canonical taxonomy of document transformations exists in either contributing discipline, and the scheme is derived as a facetted classification over two axes, at the unit boundaries by dividing or merging and at the unit itself by reducing content, extending content or reordering form.[^20]

## What the structure decides

The structure of a holding carries meaning. A link that is set, a tag that is chosen and a division of a document into smaller units decide how the knowledge can later be interpreted by a human reader and by a model alike, because they fix which connections are visible, which concepts count as independent and how the net behaves under selective loading.[^21] Filing is therefore modelling, and structural maintenance forms a model of one's own knowledge rather than tidying a folder.[^22] What that model is worth bounds what can be produced from it.[^23]

Two things follow for practice. The first is that maintenance is substantive work. A holding loses usability without it, documents go out of date, terms become inconsistent and parallel versions contradict one another, so governance sets the rules and curation applies them in a structural form covering names, metadata, links, document types, versions and duplicates and a substantive form covering contradictions, outdated rules, missing constraints, inappropriate condensations and the revision of requirements. An agent can localise problems and propose changes, and consequential changes have to be checked and answered for.[^24]

The second is that four artefact kinds carry different duties and should not absorb one another. A knowledge document describes what is known about a subject, an instruction file fixes recurring rules for the work, a skill operationalises a reusable procedure, and a prompt formulates the current task.[^25] Instruction files earn their place by externalising what would otherwise be retyped, holding durable person-level policy at one level and project facts at another, with the signals for an entry being that the agent repeats a mistake, that a review finds something it should have known, that the same correction is typed again, or that a new participant would need the same context.[^26] They are context rather than enforcement, and behavioural guidance is a different thing from permissions and hooks that can hold a boundary independently of compliance.[^27]

One question stays open in the sources. A model built for human reading and one built for machine context can demand different granularity, the conflict between compact machine readability and detailed human traceability is unresolved, and how the quality of a knowledge model could be measured at all is equally open.[^28]

## Gaps

Two topics the outline assigns to this chapter reach past the sources of this lane.[^29]
- Formal and semi-formal representation, controlled vocabularies, schemas and ontologies, appear here only as the neighbouring tradition of knowledge modelling and as the note that richer formats stay preferable where their semantics are required. When a project should reach for a formal representation instead of structured prose is stated nowhere in these sources.
- The distinction between knowledge, assumptions, rules, requirements and decisions is carried in the sources by the list of what a maintained environment holds rather than by a typology with criteria. The document typology of the other manuscript lane is the place that distinction belongs, and this chapter defers it to chapter 14.

[^1]: Grounded in [[30_assertions/knowledge-engineering-makes-knowledge-explicit]].
[^2]: Grounded in [[30_assertions/the-gap-is-between-possessed-and-available-knowledge]].
[^3]: Grounded in [[30_assertions/a-file-collection-is-not-a-knowledge-base]].
[^4]: Grounded in [[30_assertions/knowledge-acquisition-has-two-sources]].
[^5]: Grounded in [[30_assertions/the-formalisation-target-has-shifted]].
[^6]: Grounded in [[30_assertions/three-traditions-feed-the-practice]].
[^7]: Grounded in [[30_assertions/a-knowledge-base-is-purpose-bound]].
[^8]: Grounded in [[30_assertions/the-knowledge-system-is-a-production-system]].
[^9]: Grounded in [[30_assertions/a-knowledge-document-is-bounded-structured-and-revisable]].
[^10]: Grounded in [[30_assertions/the-document-is-the-concept-and-markdown-a-serialization]], [[30_assertions/markdown-exposes-structure-without-guaranteeing-content]].
[^11]: Grounded in [[30_assertions/a-knowledge-document-is-materialised-context-compression]].
[^12]: Grounded in [[30_assertions/a-knowledge-document-is-transferable-compact-and-retrievable]].
[^13]: Grounded in [[30_assertions/distillation-abstracts-a-principle-from-a-case]].
[^14]: Grounded in [[30_assertions/context-quality-has-four-criteria]].
[^15]: Grounded in [[30_assertions/five-transformations-convert-material-into-units]].
[^16]: Grounded in [[30_assertions/atomisation-and-consolidation-run-in-opposite-directions]].
[^17]: Grounded in [[30_assertions/four-design-principles-guide-the-transformations]].
[^18]: Grounded in [[30_assertions/the-transformations-are-anchored-in-older-disciplines]].
[^19]: Grounded in [[30_assertions/provenance-has-a-standard-form-and-a-research-demand]].
[^20]: Grounded in [[30_assertions/the-five-part-systematics-is-an-own-coinage]].
[^21]: Grounded in [[30_assertions/the-structure-of-a-holding-is-meaning-bearing]].
[^22]: Grounded in [[30_assertions/filing-information-is-modelling-work]].
[^23]: Grounded in [[30_assertions/the-knowledge-model-bounds-the-output]].
[^24]: Grounded in [[30_assertions/governance-and-curation-keep-a-holding-usable]].
[^25]: Grounded in [[30_assertions/four-artefact-kinds-carry-different-duties]].
[^26]: Grounded in [[30_assertions/instruction-files-externalise-stable-rules]].
[^27]: Grounded in [[30_assertions/instruction-files-are-context-not-enforcement]].
[^28]: Grounded in [[30_assertions/the-granularity-conflict-between-readers-is-unresolved]].
[^29]: Posit: the gap list records where this chapter falls short of the outline. Open evidence question: whether a criterion for choosing a formal representation over structured prose can be derived from the comparative cases of Part V.
