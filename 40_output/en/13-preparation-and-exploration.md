---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/distillation-preserved-uncertainty-and-negative-findings]]", "[[30_assertions/early-interfaces-make-a-model-discussable-through-operations]]", "[[30_assertions/exploration-determines-what-the-knowledge-base-must-represent]]", "[[30_assertions/exploration-scales-through-computational-profiling]]", "[[30_assertions/interaction-exposes-unwarranted-precision]]", "[[30_assertions/models-shift-the-cost-of-project-specific-implementation]]", "[[30_assertions/preparation-assembles-an-accessible-source-basis]]", "[[30_assertions/prompt-borne-metadata-can-enter-a-transcription]]", "[[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]]", "[[30_assertions/the-material-document-carries-epistemic-responsibility]]", "[[30_assertions/user-stories-bridge-scholar-centred-design-and-implementation]]"]
posits: 0
lang: en
part: "IV. Promptotyping"
chapter: 13
title: "Preparation and Exploration"
topic: "[[Promptotyping]]"
feeding-sources: ["paper chapter 2", "script chapter 7", "Promptotyping document templates"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Preparation and Exploration

## Preparation

Promptotyping begins by assembling what the work will proceed from. Preparation brings the relevant research material into an accessible project environment and makes its current status explicit, which for most projects means gathering source materials and research data alongside the standards, schemas, and domain documentation that describe them, the research questions and editorial or mapping guidelines that govern their treatment, whatever software already exists around them, and the requirements that have already been articulated.[^1]

The demand at this stage is weaker than it first appears. Preparation does not require the material to be normalised, formally modelled, or placed directly in an agent's working context. It requires the material to remain accessible for inspection and computational use, with its provenance and known limitations documented.[^1] Analogue material may first have to be digitised, and digital material may stay distributed across heterogeneous formats and levels of structure without blocking the phase. Preparation is provisionally sufficient once the source basis and the research context are digitally accessible and documented well enough to support systematic examination.[^1]

What the material document of the knowledge base later has to hold is already decided here. Per source it records origin, capture logic, licence, provenance, and capture period, and where several sources are combined it explains the relation between them, because the reader who has to judge data quality, the agent that has to process the data, and the domain expert who has to follow the selection logic all depend on that record.[^2] Preparation is where the information for it is collected, even though the writing belongs to Distillation.

Requirements Engineering belongs at this stage because an artefact cannot be specified independently of the scholarly activities it is meant to support. The narrative form of a requirement names a role, a goal, and a benefit, arises from sessions with domain experts during Preparation and Exploration, and is refined iteratively; its formal counterpart is a recorded expectation of the system in checkable language with an acceptance criterion.[^3] Keeping both forms lets scholarly practice and system behaviour be compared against each other rather than one being read off the other.

## Exploration

Exploration examines the prepared material to understand its structure and limitations and to determine what the project knowledge base must represent.[^4] Its question is not whether an interface can be built. It asks what the data can support and what they cannot, which distinctions are actually represented, which assumptions remain implicit, which further modelling would be required, which visual or computational forms would distort the material, and which alternative representations deserve comparison.

The form of the work follows the scale of the material. A single text or a small collection may be examined directly, including through a language model where that helps, while large or heterogeneous collections require computational profiling, for example code that extracts and aggregates structural information across thousands of encoded documents.[^5] The division of labour that follows is worth stating plainly. The collection stays within the project environment and is processed by inspectable operations, while the resulting profiles and selected examples are what enter the agent's working context.[^5]

Exploration also reaches into the material through provisional artefacts. Rapidly developed interfaces let project partners enter, display, filter, and compare information in a shared operational environment rather than discussing a model only through schemas and abstract descriptions, and the categories, relations, and capture requirements stay open to revision while that happens.[^6] Interaction of this kind has revealed where distinctions could be supported by the available material, where categories remained ambiguous, where additional information or qualification was required during capture, and where a technically possible visualisation would imply a degree of precision, completeness, or certainty that the data could not warrant.[^7]

The same phase turns up findings about the processing arrangement rather than the material. In one documented workflow, contextual information from existing encoded records was inserted into the prompt supplied with each manuscript image, and a controlled comparison then showed that richer metadata could introduce information from the prompt into a transcription even where that information was not visible in the image.[^8] A finding of that kind is available only to a project that examines its own arrangement instead of only its outputs.

## The status of what Exploration produces

Whatever Exploration yields is provisional. Its outputs are observations rather than maintained project knowledge, and they enter the knowledge base only through interpretation and Distillation.[^4] The same holds for the proposals a model generates during this phase. They enlarge the space of possibilities and are treated as hypotheses, while the evaluation against sources, data model, research context, and disciplinary practice stays with the scholar.[^9]

Exploration is provisionally sufficient once the material has been understood and documented well enough to determine what has to be carried forward. Two properties of what it produces are easy to lose at that transition. Uncertainty and negative findings belong in the maintained account, including phenomena that the available reference material does not represent and therefore cannot support as a basis for comparison, and the documented workflows preserved exactly that rather than converting incomplete evidence into apparently settled requirements.[^10]

The phases are recurrent rather than sequential, so this transition is not a gate passed once. Findings from Implementation return the work to Exploration whenever an assumption turns out to be unsupported, and to Preparation whenever a source changes or a schema proves incomplete.[^11]

## Gaps
- The hands-on chain of the lecture notes that accompanies this phase belongs to the parallel writing lane, so the chapter carries no step-by-step profiling example and no exercise material.
- Personas, epics, scenarios, and acceptance criteria are named in the outline as instruments of Preparation. Only user stories and formal requirements are anchored here, because the templates treat personas as a separate artefact and the paper does not discuss them.
- Anomaly detection and schema-versus-corpus comparison are named in the outline as exploration techniques. The sources describe computational profiling in general terms, so the specific techniques rest on the general assertion rather than on passages of their own.

[^1]: Grounded in [[30_assertions/preparation-assembles-an-accessible-source-basis]].
[^2]: Grounded in [[30_assertions/the-material-document-carries-epistemic-responsibility]].
[^3]: Grounded in [[30_assertions/user-stories-bridge-scholar-centred-design-and-implementation]].
[^4]: Grounded in [[30_assertions/exploration-determines-what-the-knowledge-base-must-represent]].
[^5]: Grounded in [[30_assertions/exploration-scales-through-computational-profiling]].
[^6]: Grounded in [[30_assertions/early-interfaces-make-a-model-discussable-through-operations]].
[^7]: Grounded in [[30_assertions/interaction-exposes-unwarranted-precision]].
[^8]: Grounded in [[30_assertions/prompt-borne-metadata-can-enter-a-transcription]].
[^9]: Grounded in [[30_assertions/models-shift-the-cost-of-project-specific-implementation]].
[^10]: Grounded in [[30_assertions/distillation-preserved-uncertainty-and-negative-findings]].
[^11]: Grounded in [[30_assertions/the-four-forms-of-work-recur-without-a-fixed-order]].
