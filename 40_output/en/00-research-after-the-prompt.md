---
type: chapter
status: grounded
writing-status: drafted
checked: {}
assertions: ["[[30_assertions/agentic-engineering-organises-multi-step-work]]", "[[30_assertions/applied-generative-ai-is-an-application-field]]", "[[30_assertions/frontier-models-amplify-asymmetrically]]", "[[30_assertions/neither-model-nor-prompt-alone-carries-the-work]]", "[[30_assertions/producing-an-artefact-is-not-judging-it]]", "[[30_assertions/research-data-are-constructed-representations]]", "[[30_assertions/the-four-engineering-layers-divide-the-field]]", "[[30_assertions/the-harness-mediates-between-the-layers]]", "[[30_assertions/the-prompt-is-one-component-of-the-loop]]", "[[30_assertions/the-translation-into-software-is-not-neutral]]", "[[30_assertions/three-levels-separate-holding-task-and-window]]"]
posits: 4
lang: en
part: Frame
chapter: 0
title: "Research after the Prompt"
feeding-sources: ["all parts of the feeding map"]
seed: "[[knowledge/outline]]"
created: 2026-08-22
updated: 2026-08-22
---

# Research after the Prompt

## The question this book asks

Research data are selected and constructed representations produced through scholarly work, and they need documentation, context and preservation before they can carry a claim. A facsimile, a transcription and an encoded representation of one historical document are therefore not interchangeable, because each has different affordances and a different form of uncertainty.[^0]

Such data become investigable through software, and generic software operates at the level of structures that many projects share. A spreadsheet recognises a table, a graph environment recognises nodes and edges, an edition viewer recognises a text and its apparatus. None of them determines which distinctions matter for a particular research question, how uncertainty should be represented, or which forms of interaction suit a particular scholarly practice. That gap between what software can recognise and what a project needs it to make visible is where this book begins.[^0a]

Generative models change the technical conditions under which project-specific forms can be built. A researcher can describe a data structure, state a requirement, supply examples and receive a transformation, an analysis or an interface derived from that description. Applied generative AI is the field that studies this application and adaptation of generative methods to domain problems, and its object is the integration of such systems into existing knowledge practices together with the methodological consequences of doing so.[^1] The reduction it offers is a reduction of manual formalisation. It leaves untouched the work of modelling the material, selecting what the system should see, specifying what it should produce, inspecting what it produced and deciding whether the result can carry a claim.

The central question is therefore not whether generative models produce useful research outputs. It is how they can be integrated into scholarly work without obscuring the evidential and interpretative foundations on which those outputs depend. The ability to produce an artefact and the ability to judge it are separate abilities, and an agent can inspect resources, combine information, generate and execute code and adapt to what it observes without any of that establishing whether the result is correct or adequate.[^2] What has to be organised, then, are the conditions under which a result is produced, checked, revised and used for a named purpose.

## Why a prompt is the wrong unit

For a bounded task a single precisely worded instruction can be enough. Extract the dates from this table and return them as structured data is a complete assignment. As soon as a task spans several files, several tools and several decisions, the questions that arise no longer belong to one layer. Some concern the design of the current task, some the persistent knowledge of the project, some the selection of what the system should have in view, and some the control of an execution that continues across steps.[^3]

This book follows a division of that field into four layers. Prompt Engineering shapes the current input sequence. Knowledge Engineering builds and maintains the available body of knowledge. Context Engineering assembles the information state a concrete task requires. Agentic Engineering organises multi-step execution inside a technical environment. Each layer answers a different question, how the task is formulated, what must be documented and maintained, which information the system needs now, and how the work is organised, bounded and checked.[^4] The layers are not stages of a process. They are concurrent concerns, and a project that has solved one of them well can still fail on another.

A technical environment mediates between them. It supplies tools and access, manages the state of a piece of work and returns results to the model, and it decides nothing about which reading of a source is defensible or whether an artefact may be published.[^5] Keeping that boundary visible is one of the recurring tasks of the book, because the same infrastructure that makes agentic work possible also makes it easy to mistake a successful run for a warranted result.

## What the book contributes

Three concepts carry the argument. The first is a persistent knowledge environment in which sources, data, project knowledge, process memory, instructions and verification material are maintained in a versioned and traceable form. The book calls it the Grounded Vault and develops it in Part II. Its core is the distinction between a body of knowledge that persists and an information state assembled for one task, a distinction that keeps accumulation from standing in for selection.[^6]

The second is Agentic Engineering as a form of work organisation. It is the systematic organisation and control of multi-step agentic work, covering the bounding and decomposition of tasks, tool use, the processing of intermediate results, handovers, conditions for abort and escalation, and checking and continuation. Its reach extends past code to data descriptions, specifications, mappings, design decisions, process documents and verification concepts.[^7] The question it asks of any arrangement is under which conditions the actions of an agent stay traceable, bounded and correctable.

The third is Promptotyping, an iterative and document-driven method for deriving research artefacts from structured data and scholarly specifications, developed in Part IV. Its unit of work is a versioned document set rather than an isolated instruction, and the prompt is one operational component inside a loop that runs from project knowledge through a working context and an implementation to a checking step that revises the project knowledge.[^8]

None of this describes a passage towards autonomous scholarship. The arrangement automates no neutral translation of research data into software. What it does is make explicit the part of that translation which can be formulated, documented and checked, and responsibility for the interpretation of the data, for the adequacy of the modelling and for the acceptance of an artefact stays with the people responsible for the research.[^9]

## Four guiding questions

The book is organised around four questions.[^0b] How do generative and agentic systems reorganise the relation between scholarly knowledge, computational execution and verification? How must research knowledge be represented so that it can ground complex work across model interactions? Which methods let scholars derive inspectable research processes without delegating epistemic authority? Under which conditions does applied generative AI amplify research practice, and where are its limits?

The fourth question has an answer that shapes the others. Amplification is uneven. It concentrates where the relevant information is digitally represented, where actions can be executed through software and where the environment returns useful feedback, and it depends on existing expertise, accessible data, technical infrastructure and the ability to assess an output. The same system therefore extends different practitioners by very different amounts.[^10] A book about method has to say this early, because a method that assumes uniform benefit will be written for a reader who does not exist.

## How to read the parts

Part I treats generative models as research systems and asks what a model is, what the system around it contributes and what standing its outputs have. Part II follows the progression from prompting through context engineering to knowledge engineering and arrives at the Grounded Vault. Part III treats agentic work, its organisation and its failure modes. Part IV develops Promptotyping as a method, Part V examines research artefacts and comparative cases, and Part VI works through a complete example and the boundaries of the approach. The order is cumulative in its vocabulary while its difficulty stays roughly level, so a reader who works on data modelling may find Part II the entry point and a reader who already runs agentic workflows may begin at Part III. Each chapter names the assertions it rests on, so a claim can be followed to the passage that supports it.[^0c]

## Gaps

This chapter draws on the teaching material of the project and on the slide deck, and three things it needs lie elsewhere.[^11]
- The Grounded Vault is introduced here by its function and characterised fully in chapter 7, where its source-bound and governed conditions need material the feeding sources of this lane do not carry.
- The characterisation of Promptotyping is deliberately thin, because the paper that defines the method belongs to the other manuscript lane and its distillate is the anchor for Part IV.
- The claim that research data are already selective representations, which the outline places in this introduction, is developed in chapter 3 from the English lecture notes and would be stronger with a source from the research-data literature entered as a publication record.

[^0]: Grounded in [[30_assertions/research-data-are-constructed-representations]].
[^0a]: Posit: the limit of generic software is stated here from the practice of the projects this book draws on and from no measurement. Open evidence question: a comparison of what a project needs to make visible against what a general-purpose environment exposes, taken across several disciplines.
[^0b]: Posit: the four questions are the frame the author sets for the book. Open evidence question: whether the parts as drafted answer them, which only the finished manuscript settles.
[^0c]: Posit: the reading order is the author's recommendation. Open evidence question: whether readers entering at Part II or Part III carry the vocabulary they need, which the teaching cases of Part V could test.
[^1]: Grounded in [[30_assertions/applied-generative-ai-is-an-application-field]].
[^2]: Grounded in [[30_assertions/producing-an-artefact-is-not-judging-it]].
[^3]: Grounded in [[30_assertions/neither-model-nor-prompt-alone-carries-the-work]].
[^4]: Grounded in [[30_assertions/the-four-engineering-layers-divide-the-field]].
[^5]: Grounded in [[30_assertions/the-harness-mediates-between-the-layers]].
[^6]: Grounded in [[30_assertions/three-levels-separate-holding-task-and-window]].
[^7]: Grounded in [[30_assertions/agentic-engineering-organises-multi-step-work]].
[^8]: Grounded in [[30_assertions/the-prompt-is-one-component-of-the-loop]].
[^9]: Grounded in [[30_assertions/the-translation-into-software-is-not-neutral]].
[^10]: Grounded in [[30_assertions/frontier-models-amplify-asymmetrically]].
[^11]: Posit: the gap list is the author's judgment of what this chapter cannot yet support. Open evidence question: whether the vault document withheld from this run and the Promptotyping paper distillate close the first two gaps or open further ones.
