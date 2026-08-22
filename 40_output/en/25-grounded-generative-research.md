---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-research-artefact-is-a-project-specific-operational-form]]", "[[30_assertions/acceptance-rests-with-the-critical-expert]]", "[[30_assertions/agentic-engineering-organises-extended-model-mediated-work]]", "[[30_assertions/amplification-rather-than-transfer-of-authority]]", "[[30_assertions/capable-systems-widen-the-span-between-production-and-acceptance]]", "[[30_assertions/context-and-agentic-engineering-are-interdependent]]", "[[30_assertions/context-engineering-organises-the-informational-environment]]", "[[30_assertions/data-governance-bounds-what-may-be-processed]]", "[[30_assertions/distillation-is-not-summarisation-or-compression]]", "[[30_assertions/inspection-is-separated-from-the-authority-to-record]]", "[[30_assertions/models-shift-the-cost-of-project-specific-implementation]]", "[[30_assertions/promptotyping-is-a-knowledge-driven-method]]", "[[30_assertions/software-operationalises-only-encoded-distinctions]]", "[[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]]", "[[30_assertions/the-artefact-produces-no-knowledge-on-its-own]]", "[[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]]", "[[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]]", "[[30_assertions/the-method-was-consolidated-from-one-practice]]", "[[30_assertions/the-significance-is-modal-rather-than-economic]]", "[[30_assertions/write-back-makes-a-finding-durable]]"]
posits: 1
lang: en
part: Frame
chapter: 25
title: "Grounded Generative Research"
feeding-sources: ["all parts of the feeding map"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Grounded Generative Research

## The passage is not neutral

Generative systems reduce the amount of manual formalisation required between a scholarly description and an executable computational form. Analyses, transformations, interfaces, and research software can be derived from natural-language specifications and structured data, and parts of the implementation effort that once made project-specific development impractical for individual researchers and small projects have become affordable.[^1]

That capacity does not create a neutral passage from research material to computational output. Research data are selective representations in which particular aspects of material are made computationally explicit for a defined purpose, and what counts as research data depends on the context in which the material was selected and interpreted.[^2] Context is constructed for particular purposes rather than assembled once, since the same material has to be distilled differently when the purpose or the intended artefact changes.[^3] Specifications remain incomplete, because natural-language descriptions retain ambiguity and different runs may realise the same requirement in materially different ways.[^4] Generated implementation is probabilistic wherever a structure has to be recognised or interpreted rather than mapped.[^1] And every research artefact operationalises decisions about what becomes visible, comparable, modifiable, or verifiable, since software processes only what has been encoded in structures its representational model supports.[^5]

The methodological task that follows is to build environments in which scholarly knowledge guides agentic work and in which generated outputs stay inspectable against their evidential and conceptual foundations. Making agents autonomous from scholarship is a different project, and this book has not pursued it.[^20]

## Five connected concepts

The argument has run through five practices that fit together rather than competing.[^21]

Prompt Engineering is the systematic design and evaluation of model inputs, meaning the iterative development of a prompt through changes to its content or to the techniques applied to it. Context Engineering extends that from individual prompts to the wider informational environment in which they are interpreted, covering the selection, organisation, maintenance, and provision of what a model-based system needs, and it does not consist in placing all available material into a context window.[^6] Knowledge Engineering supplies the persistent representation and governance of what a project takes to be the case, which in this method takes the form of maintained documents that state the data, the requirements, and the representational decisions.[^7] Agentic Engineering organises the extended, tool-supported work an agent performs, covering how tasks are decomposed, how tools are used, when human intervention is required, and how the work is inspected and continued.[^8] Promptotyping arranges all four into a method for translating structured research data and scholarly specifications into verifiable research artefacts, with a versioned project knowledge base as its organising structure and write-back as the mechanism that makes findings durable.[^9]

The knowledge environment connecting these practices is the maintained knowledge base, whose documents are bounded representations distilled from fuller material, kept for human inspection and revision and available for the working contexts of agents.[^7] The Grounded Vault is the form this book gives that environment, and it is the subject of an earlier part.

Scholarly authority sits with the Critical Expert wherever acceptance depends on interpretation, contextualisation, source criticism, and disciplinary judgement, understood as the person or group competent and accountable for judging whether the project knowledge adequately represents the material and whether the artefact suits its purpose.[^10] The line that makes the arrangement work is the one between inspecting an output and authorising it, since agents may assemble evidence, compare materials, investigate discrepancies, execute checks, and record provisional assessments, and may not independently assign an authorised verification status, a scholarly validation, an approval, or an acceptance.[^11]

## What defines the field

Applied generative AI for research is defined by a methodological arrangement rather than by the use of a particular model or tool. What the arrangement holds together is a set of relations that stay explicit, meaning the relation of an output to the evidence that supports it, of a specification to the knowledge it was written from, of an execution to the context it received, of a finding to the document it changes, and of an accepted state to the person who accepted it.[^12]

Two distinctions carry most of that weight. Technical verification asks whether an output conforms to formalised requirements, and scholarly validation asks whether the representation those requirements encode is warranted by the material and adequate for its purpose, so an implementation can be correct and inadequate at once.[^13] And a correction becomes methodologically consequential when it is incorporated into the maintained project knowledge rather than confined to the current implementation, which is what keeps a project from relearning the same lesson.[^14]

Generative systems can amplify research work under conditions that can be stated. Outputs have to be grounded in something a reader can reach. Actions have to be bounded by permissions and by an inspectable scope, and permissibility of the material and the workflow is decided outside the method.[^15] Transformations have to stay inspectable, and limitations have to be documented rather than discovered. Claims have to remain subject to critical scholarly verification.[^10]

## What the book has and has not shown

The evidence for these conditions comes from a documented practice rather than from a controlled comparison. It was consolidated primarily through projects led by one hybrid scholar-developer, the cases form no representative sample, their documentation is subject to selection effects, and observed improvements cannot be attributed cleanly to the method rather than to more capable systems, better tools, or increased experience.[^16] What the practice supports is a modal claim, in that forms of project-specific implementation previously outside the practical resources of individual researchers and small projects became workable, and it supports no claim that the method is faster, cheaper, or more reliable than the alternatives.[^17]

The argument for the arrangement therefore does not rest on measured advantage. It rests on the observation that the span between what agents can produce and what scholars can responsibly accept widens as the systems grow more capable, and that maintained knowledge, differentiated checking, write-back, and purpose-specific acceptance are the means by which that span stays governable.[^18] Within the evidential scope this book has declared, the contribution of model-based agents to scholarly work is amplification, and the competence and accountable judgement it presupposes remain indispensable.[^19]

## Gaps
- Prompt Engineering, Knowledge Engineering, and the Grounded Vault are the subjects of Parts I to III, which the parallel writing lane writes from the lecture notes, the slide deck, and the vault document. This conclusion states them from the assertions available in the Promptotyping topic and will need revision once those parts and their assertions exist.
- Knowledge Engineering has no definitional anchor in the sources distilled here, so its treatment rests on what the method's document set does rather than on a definition.
- The five concepts are named in the outline as the connected argument of the book. Their arrangement here follows the outline, and the relation among them is grounded per concept rather than as a whole.
- The conclusion is drafted before Parts I to III exist. Its claims about what the book has shown are therefore claims about Parts IV to VI.

[^1]: Grounded in [[30_assertions/models-shift-the-cost-of-project-specific-implementation]].
[^2]: Grounded in [[30_assertions/a-research-artefact-is-a-project-specific-operational-form]].
[^3]: Grounded in [[30_assertions/distillation-is-not-summarisation-or-compression]].
[^4]: Grounded in [[30_assertions/the-critical-expert-examines-what-a-coherent-artefact-conceals]].
[^5]: Grounded in [[30_assertions/software-operationalises-only-encoded-distinctions]].
[^6]: Grounded in [[30_assertions/context-engineering-organises-the-informational-environment]].
[^7]: Grounded in [[30_assertions/the-knowledge-base-is-a-set-of-interrelated-documents]].
[^8]: Grounded in [[30_assertions/agentic-engineering-organises-extended-model-mediated-work]].
[^9]: Grounded in [[30_assertions/promptotyping-is-a-knowledge-driven-method]].
[^10]: Grounded in [[30_assertions/acceptance-rests-with-the-critical-expert]].
[^11]: Grounded in [[30_assertions/inspection-is-separated-from-the-authority-to-record]].
[^12]: Posit: naming five relations that have to stay explicit restates the arrangement of the preceding parts in one sentence, and no source states the arrangement in this form. Open evidence question: whether a project can be shown to fail through the loss of exactly one of these relations while the others hold.
[^13]: Grounded in [[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]].
[^14]: Grounded in [[30_assertions/write-back-makes-a-finding-durable]].
[^15]: Grounded in [[30_assertions/data-governance-bounds-what-may-be-processed]].
[^16]: Grounded in [[30_assertions/the-method-was-consolidated-from-one-practice]].
[^17]: Grounded in [[30_assertions/the-significance-is-modal-rather-than-economic]].
[^18]: Grounded in [[30_assertions/capable-systems-widen-the-span-between-production-and-acceptance]].
[^19]: Grounded in [[30_assertions/amplification-rather-than-transfer-of-authority]].
[^20]: Grounded in [[30_assertions/the-artefact-produces-no-knowledge-on-its-own]].
[^21]: Grounded in [[30_assertions/context-and-agentic-engineering-are-interdependent]].
