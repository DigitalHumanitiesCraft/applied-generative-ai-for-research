---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/a-knowledge-base-is-tested-by-bounded-continuation-tasks]]", "[[30_assertions/a-wrong-output-is-diagnosed-by-document-type]]", "[[30_assertions/independent-transfer-is-evaluated-through-sustained-work]]", "[[30_assertions/teaching-cases-do-not-establish-independent-continuation]]", "[[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]]", "[[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]]", "[[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]]", "[[30_assertions/the-boundary-to-research-software-engineering]]", "[[30_assertions/the-method-cannot-supply-missing-competence]]", "[[30_assertions/the-method-redistributes-implementation-labour]]", "[[30_assertions/the-sufficiency-of-distillation-is-practical]]", "[[30_assertions/transfer-would-require-adaptation]]", "[[30_assertions/transferability-differs-from-exact-reproduction]]"]
posits: 3
lang: en
part: "V. Research Artefacts and Comparative Cases"
chapter: 20
title: "Teaching, Transfer, and Asymmetric Amplification"
topic: "[[Research-Artefacts]]"
feeding-sources: ["paper chapters 2.3 and 3"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Teaching, Transfer, and Asymmetric Amplification

## What teaching cases can show

A method consolidated from one practice raises the question of whether it travels, and teaching is the setting in which that question is usually first asked. The evidence available here is bounded. Teaching cases show that participants can work with structured documents and generated implementations under guided conditions, and they do not show that participants continue such work independently across a sustained project.[^1] The distinction matters because guided completion of an exercise and unsupported continuation of a project test different things, and only the second speaks to transfer.

The stronger test is stated in the sources rather than met by them. New domain contributors should receive the method specification, the relevant project materials, and access to an appropriate technical environment, and should then develop and assess a bounded promptotype without continuing intervention by the originating practitioner, with successful, unsuccessful, and discontinued paths preserved, with changes to project knowledge, artefacts, human intervention, external assistance, and grounds of acceptance recorded, and with model and harness treated as experimental variables rather than as invisible background conditions.[^2] A bounded continuation task is the smaller version of the same test, in which independent contributors explain the project, diagnose a selected discrepancy, or continue a delimited implementation task from the maintained documents, and observed difficulties are attributed where possible to documentary, technical, access-related, or competency-related limitations.[^3]

Transfer also has to be distinguished from reproduction. Another practitioner may apply the method and produce a different artefact with different documents, models, tools, and project structures, so what transfer requires is that the core methodological relations be established, applied, and reconstructed without undocumented intervention by the originator.[^4] And the method itself would need adaptation on the way out of its field, since the relation among maintained knowledge, bounded implementation, examination, write-back, differentiated checking, and accountable judgement is not intrinsically limited to the humanities while the method was developed against a specifically humanistic difficulty profile of heterogeneous sources, interpretative modelling, incomplete evidence, and forms of adequacy that technical conformity cannot determine.[^5]

## Asymmetric amplification

The concept that organises this chapter names an unevenness. Promptotyping may extend the practical reach of articulated scholarly and technical competence, while its benefits stay dependent on data quality, available knowledge, access to capable systems, and the capacity to examine outputs, so researchers and institutions with stronger expertise, infrastructure, and verification capacity may benefit disproportionately.[^6] The same unevenness appears inside a project, where domain specialists may assume additional supervisory work, Research Software Engineers may inherit technical debt, and those responsible for verification may face more plausible outputs without corresponding resources or authority.[^6]

Two mechanisms behind this are already established in earlier chapters. The method redistributes implementation labour rather than eliminating it, so an evaluation has to distinguish effort that is reduced from effort that is transferred, newly created, or deferred, and the combined burden of maintaining knowledge, coordinating agentic work, and preserving a verifiable state has not been measured in the documented cases.[^7] And the method cannot supply domain knowledge that practitioners do not possess or cannot recognise as relevant, because templates and maintained documents make assumptions explicit and revisable without providing them, while inadequate project knowledge can guide an agent towards an implementation that is coherent, operational, and scholarly inadequate.[^8]

Read together, these give the concept its edge. The capacity that most determines the benefit is the capacity to notice that something is wrong, and that capacity is exactly what is unevenly distributed.[^9]

## What teaching therefore has to cover

Teaching cannot restrict itself to the formulation of prompts. It has to cover model literacy, meaning what generative systems do and how they fail; research data literacy, meaning what a dataset represents and where it stops carrying; the organisation of context and knowledge, meaning what belongs in a maintained document and what belongs in a working context; specification, meaning the translation of scholarly practice into statements that guide implementation; failure diagnosis; verification; and awareness of the boundary to Research Software Engineering.[^10]

Three of those items have a testable form in the method itself. Failure diagnosis has a grid, since a formally wrong output, a break in style, or an ignored prohibition is diagnosed in the action document while a substantively wrong output is diagnosed in the knowledge documents.[^11] Verification has a distinction, since technical verification asks about conformity to formalised requirements while scholarly validation asks whether the represented arrangement is warranted by the material and adequate for its purpose.[^12] And the boundary to professional software engineering has a criterion, since it is crossed when an artefact takes on obligations of durability, maintenance, security, accessibility, institutional operation, shared use, persistent state, integration, or third-party support.[^13]

Knowledge organisation has a testable form as well, and it is the completion criterion of Distillation. A new contributor or agent instance, given the documents and access to the resources, should be able to reconstruct the project's logic and continue the work without undocumented explanation.[^14] Because that criterion is a task rather than a judgement, it is teachable and examinable in the same operation, which makes it the most useful single exercise a course on the method can set.[^15] How much documentary work a given project needs follows from what is being delegated, so the exercise scales with the case rather than imposing a fixed standard.[^16]

## Gaps
- The teaching material of the lecture notes and the slide deck feeds this chapter and belongs to the parallel writing lane, so the chapter rests on the paper's short account of the teaching cases alone.
- The outline asks which concepts can be taught reliably, where participants require technical support, how templates influence the quality of specifications, whether non-programmers can inspect generated implementations, and which forms of verification remain difficult. The sources answer none of these, and the chapter states them as the open questions of the teaching line rather than answering them.
- How Grounded Vaults support continuity across sessions is named in the outline and is treated in Part II by the other lane, so this chapter refers to the completion criterion of Distillation instead.
- No teaching case is described individually here, because the sources report the teaching setting only as insufficient evidence of independent transfer.

[^1]: Grounded in [[30_assertions/teaching-cases-do-not-establish-independent-continuation]].
[^2]: Grounded in [[30_assertions/independent-transfer-is-evaluated-through-sustained-work]].
[^3]: Grounded in [[30_assertions/a-knowledge-base-is-tested-by-bounded-continuation-tasks]].
[^4]: Grounded in [[30_assertions/transferability-differs-from-exact-reproduction]].
[^5]: Grounded in [[30_assertions/transfer-would-require-adaptation]].
[^6]: Grounded in [[30_assertions/the-benefit-of-the-method-is-distributed-unevenly]].
[^7]: Grounded in [[30_assertions/the-method-redistributes-implementation-labour]].
[^8]: Grounded in [[30_assertions/the-method-cannot-supply-missing-competence]].
[^9]: Posit: naming the capacity to detect inadequacy as the decisive one follows from combining the redistribution of labour with the limit on what documents can compensate for, since both leave the burden of noticing with the reader of the output. Open evidence question: a study that measures detection of inadequate generated output against the technical and domain competence of the reader.
[^10]: Posit: the seven components of a curriculum for the method are the book's own arrangement of what the preceding chapters require of a practitioner, and the sources name no curriculum. Open evidence question: which of the seven can be taught to a measurable standard, which the teaching cases were not designed to establish.
[^11]: Grounded in [[30_assertions/a-wrong-output-is-diagnosed-by-document-type]].
[^12]: Grounded in [[30_assertions/technical-verification-and-scholarly-validation-differ-in-kind]].
[^13]: Grounded in [[30_assertions/the-boundary-to-research-software-engineering]].
[^14]: Grounded in [[30_assertions/the-sufficiency-of-distillation-is-practical]].
[^15]: Posit: the continuation criterion doubles as a teaching exercise because it is passed or failed by an observable attempt rather than by an assessor's impression. Open evidence question: whether courses that set it produced better maintained documents than courses that taught the document types descriptively.
[^16]: Grounded in [[30_assertions/the-account-must-be-proportionate-to-what-is-delegated]].
