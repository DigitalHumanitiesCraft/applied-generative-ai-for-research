---
title: Outline
project:
  name: "Applied Generative AI for Research"
  repository: "DigitalHumanitiesCraft/applied-generative-ai-for-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: complete
language: en
created: "2026-08-22"
updated: "2026-08-22"
related: [specification, state, project, plan]
---

# Outline

The canonical outline of the book, carried over verbatim from the expose that the project wrote before this repository existed. It is the reference the chapter register in [[knowledge/state]] and the chapter skeleton in `40_output/` are built from, and the chapter descriptions below are the seed text of the skeleton files. A change to the structure of the book is made here first and then propagated to the register and the skeleton.

## Expose

# Applied Generative AI for Research (Exposé)
## Knowledge, Context, Agents, and Verifiable Research Artefacts
## Abstract
Generative models are increasingly used to support scholarly research through text generation, data transformation, information extraction, analysis, software development, and the construction of digital research environments. Their significance does not lie solely in their capacity to generate individual outputs. Combined with retrieval systems, external tools, code execution, persistent project environments, and agentic workflows, they alter how research knowledge is represented, made available, translated into computational operations, and subjected to verification.
This book develops a methodological framework for **applied generative AI for research**. The term refers to the controlled integration of generative models and agentic systems into scholarly activities without transferring evidential responsibility, interpretative authority, or the authorisation of research claims to those systems. The book argues that responsible use cannot be reduced to writing effective prompts. As the complexity and duration of model-supported work increase, transient instructions must be supplemented by deliberately constructed context, persistent knowledge representations, explicit specifications, and differentiated forms of validation and verification.
The argument develops through a progression from Prompting and Prompt Engineering to Context Engineering, Knowledge Engineering, and Agentic Engineering. Prompt Engineering concerns the iterative design and evaluation of input sequences for defined tasks. Context Engineering determines which information is selected, generated, structured, and made available during a particular interaction or workflow. Knowledge Engineering addresses the more persistent problem of how research knowledge, evidence, concepts, relations, assumptions, decisions, and rules are represented and maintained across interactions. Agentic Engineering concerns the organisation of work in environments in which models can inspect repositories, use tools, execute commands, modify files, evaluate outputs, and continue across several steps between human interventions.
At the centre of the framework is the **Grounded Vault**, a versioned, source-bound, inspectable, and agent-operable knowledge environment. It brings together research sources, structured data, scholarly descriptions, requirements, design decisions, process records, action instructions, and verification materials. A Grounded Vault separates evidence from interpretation, relatively stable project knowledge from volatile instructions, and curated scholarly judgement from deterministically generated reports. It is not defined by a particular software application. It may be implemented through a file system, Git repository, Markdown environment, Obsidian vault, or comparable infrastructure, provided that its knowledge remains traceable, revisable, governed, and usable by both scholars and computational agents.
Within this wider framework, the book develops **Promptotyping** as an iterative, document-driven research method for translating structured research data, scholarly context, and project-specific requirements into inspectable and verifiable research artefacts. Promptotyping integrates Requirements Engineering, Context Engineering, Knowledge Engineering, agentic implementation, deterministic validation, and critical scholarly verification. It proceeds through four recurring forms of work: Preparation gathers sources, data, standards, research questions, and requirements; Exploration examines what the data affords, what it cannot support, and which representational alternatives are appropriate; Distillation expresses the project’s current understanding through persistent Promptotyping Documents; and Implementation derives transformations, tests, code, and interfaces from those documents. Findings made during implementation return to the documents, the assumptions developed during Exploration, or the preparation of the source material.
The book distinguishes several forms of authority and assessment. Deterministic validation can establish properties that have been formalised as rules. LLM-mediated review can extend the coverage of comparison, testing, critique, and anomaly detection. Neither can independently authorise interpretations whose validity depends on source criticism, contextual knowledge, or disciplinary judgement. The **Critical Expert** therefore remains responsible for modelling, specification, evaluation of alternatives, contextualisation, and scholarly acceptance. Human participation is not treated as a generic final checkpoint but as a differentiated form of expertise whose authority depends on the question being decided.
The empirical basis comprises repository-documented projects, teaching cases, research software experiments, digital editions, ontology work, historical data interfaces, multimodal transcription pipelines, and evaluation environments developed over several years. These materials are analysed comparatively to identify recurring knowledge structures, workflows, artefact types, failure modes, and boundary conditions. A worked example follows one research project from the formulation of a research question and inspection of structured data through the construction of a Grounded Vault, the development of project documents, agentic implementation, failure analysis, revision, verification, publication, and possible handover to Research Software Engineering.
The book argues that generative systems do not automate a neutral transition from research data to software or scholarly claims. Research data are already selective and purpose-bound representations, while computational artefacts operationalise particular distinctions, assumptions, and forms of inquiry. Applied generative AI becomes methodologically defensible when these translations remain persistent, versioned, inspectable, revisable, and attributable. Its contribution is therefore best understood as an amplification of scholarly and technical competence rather than its replacement. When generated artefacts become durable, institutionally operated, security-relevant, maintained for external users, or dependent on shared infrastructure, the method reaches its boundary and enters the domain of Research Software Engineering.
-----
# Introduction
## Research after the Prompt
Digital research data become accessible, investigable, and revisable through software. A text editor, spreadsheet, network-analysis environment, edition viewer, or research database makes different aspects of the same data addressable. Yet generic software usually operates at the level of structures shared across many projects. It can recognise tables, graphs, coordinates, annotations, or document hierarchies without determining which distinctions matter for a particular research question, how uncertainty should be represented, or which forms of interaction are appropriate for a specific scholarly practice.
Generative models and agentic systems alter the technical conditions under which project-specific computational forms can be created. Researchers can increasingly express requirements, explain data structures, provide examples, describe representational decisions, and ask models to derive analyses, transformations, interfaces, and software from them. This reduces the amount of manual formalisation and programming required between scholarly intent and an executable artefact. It does not, however, remove the need to model the research material, select relevant context, specify intended behaviour, inspect generated implementations, or verify the resulting scholarly claims.
The central question of this book is therefore not whether generative models can produce useful research outputs. It is how they can be integrated into scholarly work without obscuring the evidential, conceptual, and interpretative foundations on which those outputs depend.
The book develops **applied generative AI for research** as a methodological field concerned with the controlled use of generative and agentic systems in scholarly workflows. It examines how research knowledge must be represented, how context must be constructed, how work can be delegated, how outputs can be verified, and where the authority to accept or reject a result must remain.
Its central argument is that generative AI supports research not only by producing text, code, classifications, or visualisations, but by reorganising the relations among:
  - research sources and structured data;
  - scholarly knowledge and assumptions;
  - task-specific context;
  - specifications and requirements;
  - computational execution;
  - feedback and verification;
  - and the authority attached to different forms of judgement.
This reorganisation gives rise to three related methodological contributions.
First, the book introduces the **Grounded Vault** as a persistent knowledge environment in which sources, data, project knowledge, process memory, instructions, and verification materials are maintained in a versioned and traceable form.
Second, it defines **Agentic Engineering** as a form of work organisation in which models and agents perform an increasing span of repository-based and tool-mediated work between human interventions, while humans shift towards knowledge preparation, specification, decomposition, supervision, and verification.
Third, it develops **Promptotyping** as a method for deriving research artefacts from structured data and scholarly specifications through document-driven context construction, agentic implementation, and critical verification.
These concepts do not describe a transition towards autonomous scholarship. They describe the conditions under which generative systems can amplify scholarly and technical competence without assuming responsibility for the research in which they participate.
The book is guided by four questions:
1.  How do generative and agentic systems reorganise the relationship between scholarly knowledge, computational execution, and verification?
1.  How must research knowledge be represented and maintained so that it can ground complex work across model interactions and agentic workflows?
1.  Which methods allow scholars to derive inspectable research processes and artefacts from generative systems without delegating epistemic authority?
1.  Under which technical, epistemic, and institutional conditions does applied generative AI amplify research practice, and where are its limits?
-----
# Part I
## Generative Models as Research Systems
## Chapter 1
### What Large Language Models Are
This chapter introduces Large Language Models as probabilistic generative systems rather than databases, search engines, formal knowledge bases, or artificial persons. It explains the technical concepts required to understand their role in research without attempting to provide a complete account of contemporary machine learning.
The discussion begins with tokenisation, vector representations, transformer architectures, attention, pretraining, and next-token prediction. It then explains how instruction tuning, preference optimisation, inference procedures, and product-level system instructions shape model behaviour.
The chapter distinguishes between the generation of plausible linguistic continuations and operations such as retrieval, deterministic computation, formal inference, and empirical verification. It shows why models can produce useful explanations, transformations, classifications, code, and analytical suggestions while remaining vulnerable to inconsistency, confabulation, context dependence, and unwarranted confidence.
The purpose of the chapter is methodological: researchers need not reproduce the engineering of a frontier model, but they must understand enough about its operation to interpret its outputs appropriately.
Central topics include:
  - tokens and tokenisation;
  - embeddings and distributed representations;
  - transformer architectures and attention;
  - pretraining and probabilistic continuation;
  - instruction tuning and preference optimisation;
  - inference and stochastic variation;
  - apparent reasoning and its limits;
  - model knowledge versus external evidence;
  - confabulation and misplaced confidence;
  - the jagged frontier of model capability.
## Chapter 2
### Models, Tools, and Generative Systems
A Large Language Model rarely operates alone. Contemporary research applications combine a base model with system instructions, retrieval mechanisms, external tools, code execution, memory, user interfaces, safety layers, and access to local or remote files.
This chapter distinguishes the model from the system in which it is embedded. The same underlying model may behave differently across products because different applications provide different instructions, retrieval sources, tools, permissions, context-selection procedures, and post-processing mechanisms.
The chapter examines:
  - base models and application layers;
  - system prompts and hidden instructions;
  - retrieval-augmented generation;
  - function calling and external tools;
  - code execution and deterministic computation;
  - multimodal and vision-language systems;
  - persistent memory and stored user context;
  - model and product versioning;
  - proprietary infrastructure and reproducibility;
  - the attribution of system-level capabilities to models.
This distinction is essential for research because the object being evaluated is often not a model in isolation but a changing sociotechnical system.
## Chapter 3
### Knowledge, Evidence, and Epistemic Authority
This chapter examines what it means to say that a language model “knows” something. It distinguishes among parametric patterns acquired during training, information supplied in context, retrieved evidence, generated hypotheses, and externally verified claims.
The chapter argues that models can contribute to knowledge work without becoming the final authority for the knowledge produced. Their outputs may be useful as proposals, transformations, comparisons, classifications, summaries, or critiques. Their validity depends on the relations between output, evidence, method, and responsible judgement.
The chapter introduces several risks relevant to research:
  - confabulation;
  - sycophancy;
  - uncalibrated confidence;
  - inherited bias;
  - conventional but inappropriate representations;
  - the loss of provenance;
  - and the substitution of plausibility for evidence.
It concludes by distinguishing productive model participation from epistemic authorisation. A system may generate a claim, but the authority to accept it depends on the applicable standards of evidence and expertise.
-----
# Part II
## From Prompting to Grounded Knowledge
## Chapter 4
### Prompting and Prompt Engineering
Prompting is introduced as the construction of an input sequence that conditions a model’s output distribution. It includes not only direct instructions but also examples, data, constraints, terminology, ordering, formatting rules, and interaction history.
The chapter distinguishes informal prompting from **Prompt Engineering**, defined as the iterative design and evaluation of input sequences for a specified task. Prompt Engineering requires more than discovering persuasive formulations. It involves defining the task, specifying expected outputs, constructing representative cases, testing failures, comparing variants, and documenting changes.
The chapter covers:
  - instructions, data, examples, and constraints;
  - zero-shot and few-shot prompting;
  - structured-output requirements;
  - role and perspective instructions;
  - decomposition and iterative refinement;
  - representative test cases;
  - evaluation criteria;
  - prompt versioning;
  - stable and stochastic behaviour;
  - model-specific and portable instructions;
  - the limits of prompt optimisation.
The central limitation is that complex work cannot be governed reliably through an isolated prompt. As tasks become longer and more dependent on project-specific information, the problem shifts from wording an instruction to constructing and maintaining the context within which an instruction operates.
## Chapter 5
### Context Engineering and Pragmatic Distillation
Context Engineering concerns the selection, construction, organisation, and maintenance of information made available to a model during a task or workflow.
The chapter distinguishes transient prompts from wider context architectures. It examines how context can be retrieved, generated, compressed, refreshed, ordered, and separated according to its function. It also addresses the limitations of nominally large context windows: the presence of information in a context does not ensure that the model will use it consistently or appropriately.
Central topics include:
  - prompts versus context;
  - context windows;
  - task-relative relevance;
  - context saturation and degradation;
  - long-context limitations;
  - retrieval and selective inclusion;
  - persistent and transient context;
  - generated context;
  - context architectures;
  - context refresh and revision.
The chapter develops **Distillation** as a form of pragmatic modelling rather than simple compression. A distilled representation retains the distinctions required for a particular task while leaving the full source, dataset, or formal model intact.
This is expressed through a central arrangement:
The model reads about the data and writes code that reads the data.
The complete research data remain the evidential and computational basis. The model receives a task-specific description of their structure, semantics, uncertainty, exceptions, and relevance. Generated code then processes the complete data outside the model’s context.
## Chapter 6
### Knowledge Engineering for Generative Research
Context Engineering determines what is made available during a particular interaction. Knowledge Engineering addresses the prior and more persistent question of how project knowledge is represented, maintained, related, validated, and made reusable across interactions.
This chapter distinguishes information, evidence, knowledge, assumptions, rules, requirements, and decisions. It discusses formal and semi-formal knowledge representation, including controlled vocabularies, schemas, ontologies, structured documents, and task-specific conceptual models.
The chapter argues that successful agentic work depends not merely on retrieving more information but on maintaining a governed knowledge layer in which:
  - concepts and relations are explicit;
  - provenance can be inspected;
  - stable descriptions are distinguished from provisional assumptions;
  - uncertainty remains visible;
  - contradictions can be identified;
  - instructions do not silently overwrite factual or scholarly descriptions;
  - and new findings can be incorporated into a persistent project understanding.
Knowledge Engineering thereby supplies the durable basis from which task-specific contexts can be constructed.
## Chapter 7
### The Grounded Vault
The Grounded Vault is a versioned, source-bound, inspectable, revisable, and agent-operable knowledge environment shared by scholars and computational agents.
It is not defined by a specific application. It may be implemented through a Git repository, local file system, Markdown environment, Obsidian vault, or comparable infrastructure. What matters is the organisation and governance of the knowledge it contains.
A Grounded Vault fulfils seven conditions:
1.  **Source-bound** Claims and descriptions can be traced to research sources, structured data, references, or documented decisions.
1.  **Versioned** Changes remain historically and procedurally inspectable.
1.  **Layered** Evidence, interpretation, process memory, and action instructions are distinguished.
1.  **Inspectable** Human researchers can read, criticise, and revise the maintained knowledge.
1.  **Agent-operable** Computational agents can retrieve, process, and act from the relevant materials.
1.  **Revisable** New findings alter the maintained knowledge layer rather than remaining isolated in local outputs or conversations.
1.  **Governed** Provenance, authority, permissions, and overwrite behaviour are explicitly controlled.
The Grounded Vault may include:
  - research sources;
  - structured datasets;
  - schemas and standards;
  - data descriptions;
  - requirements;
  - design documents;
  - verification concepts;
  - journals;
  - decision records;
  - agent instructions;
  - generated corpus reports;
  - scripts;
  - tests;
  - and published artefacts.
The chapter distinguishes three knowledge layers:
### Declarative Documents
These state what is currently understood about the sources, data, requirements, design, mappings, and intended artefact.
### Process Documents
These record how the work proceeded, which alternatives were considered, why decisions were made, and what remains unresolved.
### Action Documents
These specify how agents and tools should act, including technical baselines, permissions, file boundaries, tests, checkpoints, and documentation duties.
The chapter also distinguishes curated knowledge from deterministically generated knowledge. Curated documents remain under scholarly responsibility even when models assist with drafting. Generated documents are rendered from data through named scripts or processes and are overwritten when those processes run again.
-----
# Part III
## Agentic Research Work
## Chapter 8
### From Models to Agents
A model becomes part of an agentic system when it can interact with an environment across multiple steps. It may inspect repositories, read files, use tools, execute commands, modify documents, run tests, inspect outputs, and adapt its next action according to feedback.
This chapter does not define agents through marketing categories or a fixed list of components. Instead, it treats agentic behaviour as a continuum and focuses on the **span of work performed between two human interventions**.
As this span increases, more of the project’s purpose, constraints, knowledge, permissions, and verification criteria must exist in persistent and inspectable form before execution begins.
The chapter examines:
  - planning and execution loops;
  - repository and file access;
  - code execution;
  - tool use;
  - environmental feedback;
  - memory and persistence;
  - autonomy as a continuum;
  - intervention points;
  - and the relation between agent capability and specification requirements.
## Chapter 9
### Agentic Engineering as Work Organisation
Agentic Engineering is defined as a form of work organisation in which human activity shifts from manually performing each implementation step towards preparing knowledge, specifying goals, decomposing work, assigning permissions, inspecting intermediate results, and verifying outcomes.
It includes:
  - specification before execution;
  - bounded task decomposition;
  - inspectable milestones;
  - repository-level context;
  - role and permission design;
  - the principle of least privilege;
  - single-agent and multi-agent workflows;
  - testing and visual feedback;
  - process documentation;
  - handovers;
  - and auditing.
Agentic Engineering does not imply the removal of human labour. It changes its distribution. The executing instance may be an agent, but the coherence and legitimacy of the work depend on how its environment and authority have been designed.
## Chapter 10
### Failure, Drift, and Verification Debt
This chapter examines failures that cannot be solved through better prompt wording alone.
Recurring failure modes include:
  - local code patches that are not written back into the maintained specification;
  - hidden assumptions;
  - loss of scholarly context;
  - implementation drift;
  - uncontrolled dependency growth;
  - overengineering;
  - unauthorised classifications;
  - self-verification by the producing system;
  - plausible but unsupported transformations;
  - accumulation of uninspected output;
  - and automation bias.
The chapter introduces **verification debt** as the body of generated work that has been accepted provisionally but not yet examined at the level required for scholarly or operational use.
Failure analysis should identify the layer in which correction belongs. A visible defect may originate in implementation, instructions, requirements, data understanding, source preparation, or the research question itself.
-----
# Part IV
## Promptotyping
## Chapter 11
### Promptotyping: Translating Research Data into Research Artefacts through Context Engineering and Agentic Engineering
This chapter presents the central method of the book and may also be published as an independent paper.
Promptotyping is an iterative, document-driven research method for deriving research artefacts from structured research data, scholarly context, and project-specific requirements through LLM-based agentic coding tools.
It integrates:
  - Requirements Engineering;
  - Scholar-Centred Design;
  - Context Engineering;
  - Knowledge Engineering;
  - pragmatic Distillation;
  - agentic implementation;
  - deterministic validation;
  - LLM-mediated review;
  - and verification by a Critical Expert.
Promptotyping addresses the translation between modelled research data and the computational forms through which those data can be investigated, interpreted, enriched, corrected, verified, or published.
Its unit of work is not an isolated prompt or code generation. It is a versioned set of documents that records the project’s current understanding of:
  - its sources and data;
  - research context;
  - requirements;
  - representational decisions;
  - technical constraints;
  - process history;
  - and verification criteria.
An agent implements from these documents. Scholars inspect the specification and verify the resulting artefact against the sources, data, requirements, and research purpose. Findings made during implementation are written back into the maintained knowledge layer.
The documents remain authoritative relative to the generated implementation, but their authority is procedural rather than absolute. When an implementation exposes an unsupported assumption, incomplete requirement, or overlooked property of the data, the documented understanding must be revised.
## Chapter 12
### Preconditions, Scope, and Relation to Research Software Engineering
Promptotyping presupposes:
  - structured and machine-actionable research data;
  - sufficient scholarly expertise to contextualise and evaluate them;
  - an inspectable project knowledge layer;
  - the ability to formulate requirements;
  - and the capacity to verify the resulting artefact.
The method addresses a bounded capacity gap between researchers who can articulate domain knowledge and research requirements and the technical resources required to implement project-specific computational forms.
It does not replace professional software development. It does not confer the experience of a Research Software Engineer on its users. It is best suited to bounded prototypes, specialised interfaces, processing environments, and research-specific artefacts whose technical and organisational obligations remain limited.
The transition to Research Software Engineering occurs when an artefact must become:
  - durable;
  - maintained;
  - secure;
  - accessible;
  - institutionally operated;
  - shared across multiple users;
  - dependent on persistent server-side state;
  - integrated into external infrastructure;
  - or supported for third parties.
Promptotyping Documents may support this transition as a handover package, but they do not remove the responsibilities attached to maintained research software.
## Chapter 13
### Preparation and Exploration
Promptotyping begins with **Preparation**.
Preparation gathers and structures:
  - source materials;
  - research data;
  - standards;
  - schemas;
  - domain documentation;
  - research questions;
  - editorial and mapping guidelines;
  - existing software;
  - and initial requirements.
Requirements Engineering belongs at this stage because an artefact cannot be specified independently of the scholarly activities it is intended to support. Personas, epics, user stories, scenarios, and acceptance criteria translate scholarly practice into statements that can guide implementation without losing their research purpose.
**Exploration** then examines the relationship between the research question and the available material. Its purpose is not merely to determine whether an interface can be built. It asks:
  - What can the data support?
  - What can they not support?
  - Which distinctions are represented?
  - Which assumptions remain implicit?
  - Which additional modelling is required?
  - Which visual or computational forms may distort the material?
  - Which alternative representations should be compared?
Exploration may involve deterministic profiling scripts, inventories, schema-versus-corpus comparisons, anomaly detection, generated design alternatives, and provisional interfaces.
Generated proposals are treated as hypotheses rather than accepted solutions. They enlarge the possibility space, while the scholar evaluates them against the sources, data model, research context, and disciplinary practice.
## Chapter 14
### Distillation and Promptotyping Documents
Distillation translates the understanding produced through Preparation and Exploration into the document set from which implementation proceeds.
A Promptotyping Document is a project-bound knowledge document that is:
  - readable by scholars;
  - actionable for agents;
  - versioned;
  - revisable;
  - sufficiently compact for a managed context architecture;
  - and traceable to the project’s source and decision basis.
Recurring documents include:
### data.md
Describes formats, structures, semantics, provenance, controlled values, gaps, uncertainty, exceptional cases, and known limitations.
### requirements.md
Expresses functional and non-functional requirements, user stories, scenarios, acceptance criteria, and project boundaries.
### design.md
Records interface, interaction, visualisation, and representational decisions, including the treatment of uncertainty, hierarchy, provenance, missingness, and contested classifications.
### verification.md
Defines claims, expected evidence, applicable procedures, authority levels, and acceptance conditions.
### journal.md
Records sessions, attempts, failures, model and tool use, decisions, unresolved questions, and handovers.
### Action documents
Files such as CLAUDE.md, AGENTS.md, or equivalent repository instructions specify how agents should work, which technologies they may use, what they may modify, which checks they must perform, and how findings must be documented.
The completion criterion for Distillation is practical:
A new agent instance with access to the project data and documents should be able to understand the current project logic and continue the work without an undocumented oral explanation.
This criterion does not guarantee completeness. It makes omissions visible when the agent cannot act or produces output that reveals missing context.
## Chapter 15
### Agentic Implementation and Return Paths
Implementation hands the maintained document set to an agentic coding system operating within the project repository.
The agent translates the semi-formal specification into:
  - parsers;
  - transformations;
  - schemas;
  - tests;
  - queries;
  - code;
  - interfaces;
  - and visible research artefacts.
Implementation should proceed through inspectable milestones. Each increment must remain small enough to evaluate before further complexity is added.
The defining loop does not run only between code and output. Findings return to different depths of the project:
  - an implementation defect may require a code correction;
  - an incomplete action instruction may require revision of the agent configuration;
  - a missing requirement belongs in a declarative document;
  - an unsupported assumption returns the project to Exploration;
  - a changed source or incomplete schema returns it to Preparation.
The generated artefact is therefore not the final authority. It is an implementation through which the adequacy of the maintained project understanding can be tested.
## Chapter 16
### Verification, the Critical Expert, and Distributed Authority
Promptotyping distinguishes several forms of assessment.
### Deterministic validation
Schemas, tests, constraints, linters, and build systems can determine whether formally expressible conditions are satisfied.
### Operational and visual inspection
Running artefacts can be inspected for behaviour, layout, readability, missing elements, inconsistent labels, and discrepancies between specification and rendering.
### LLM-mediated review
Models can compare files, inspect transformations, operate interfaces, identify inconsistencies, and test implementations against stated requirements. This expands review coverage but does not constitute scholarly authorisation.
### Verification by the Critical Expert
The Critical Expert determines whether:
  - the data have been represented appropriately;
  - the research question is meaningfully addressed;
  - interpretations are supported;
  - uncertainty and missingness are treated adequately;
  - relevant alternatives have been considered;
  - and the output can be accepted as part of scholarly work.
The Critical Expert is not merely any human in a loop. The role requires competence in the relevant research domain and awareness of generative-system failure modes.
Two forms of judgement may be combined or distributed:
  - **Scholarly judgement** concerns sources, data, interpretation, representation, and research claims.
  - **Agentic-engineering judgement** concerns decomposition, tools, permissions, testing, implementation strategy, and the diagnosis of technical failures.
Authority is therefore distributed rather than transferred. Data provide the evidential basis. Documents provide the maintained procedural reference. Deterministic systems decide formalised questions. Models extend implementation and review. Critical Experts retain responsibility where acceptance depends on scholarly judgement.
-----
# Part V
## Research Artefacts and Comparative Cases
## Chapter 17
### Research Artefacts as Scholarly Arguments
Research artefacts are computational forms adapted to particular data, research questions, and scholarly practices. They may include models, pipelines, interfaces, transformations, editions, verification environments, and software applications.
They do not merely display research data. Their structures and interactions operationalise interpretations.
Decisions such as:
  - which entities become nodes;
  - whether an edge is directed;
  - how observations are aggregated;
  - whether missing values remain visible;
  - how temporal uncertainty is represented;
  - which categories are selectable;
  - and which comparisons are enabled
shape the forms of inquiry that an artefact supports.
A functioning implementation is therefore not necessarily a scholarly adequate one. Technical success can coexist with unsupported categories, inappropriate mappings, misleading visual conventions, or concealed uncertainty.
The chapter develops a critique of **tool positivism**, understood as the assumption that an adequate technical implementation is itself an adequate solution to the underlying scholarly problem.
## Chapter 18
### An Epistemic Typology of Research Interfaces
Research interfaces are classified according to the primary epistemic activities they support.
### Exploration Interfaces
Enable investigation through filters, linked views, alternative navigation, comparison, and visualisation.
### Verification Interfaces
Expose intermediate or final outputs beside sources, ground truth, or alternative procedures so that errors can be identified and corrected.
### Edition Interfaces
Connect encoded texts with facsimiles, apparatus, translations, annotations, and editorial interventions.
### Capture Interfaces
Support structured data entry, annotation, correction, and metadata creation while testing the adequacy of the underlying data model.
### Audit Interfaces
Expose processing histories, disagreements, provenance, evaluation results, transformations, and decision pathways.
These types are not mutually exclusive. A single artefact may combine several functions. Their purpose is to identify the epistemic role of an interface rather than classify it solely by technology or data format.
## Chapter 19
### Comparative Project Cases
This chapter analyses documented projects comparatively rather than presenting them only as isolated success stories.
The cases are organised around four analytical problems.
### Semantic explicitness and task-specific context
Cases include the Bookkeeping Ontology, Semantic Markdown, ontology-based historical data, and project vocabularies. They show how formal semantic structures can support context construction while still requiring project-specific interpretation.
### Research artefacts as representations
Cases include DEPCHA, the Wheaton Day Book, historical accounting interfaces, editions, and visual exploration environments. They demonstrate how different research perspectives require different computational forms even when they use interoperable data.
### Generative processing and verification
Cases include the Stefan Zweig handwritten-text-recognition pipeline, OCR and HTR workflows, transcription environments, and stage-specific verification systems. They demonstrate the need to distinguish production from authorisation.
### Evaluation and audit
Cases include model-comparison environments, disagreement analysis, bias evaluation, pipeline inspection, and audit interfaces. They show how generative research processes themselves can become objects of investigation.
Each comparison examines:
  - project context;
  - data and source structure;
  - knowledge representations;
  - agentic workflow;
  - document architecture;
  - verification procedure;
  - artefact type;
  - failure modes;
  - and boundary conditions.
## Chapter 20
### Teaching, Transfer, and Asymmetric Amplification
Teaching cases involving researchers with and without programming backgrounds provide evidence about the transferability and limits of the method.
The chapter examines:
  - which concepts can be taught reliably;
  - where participants require technical support;
  - how templates influence the quality of specifications;
  - whether non-programmers can inspect generated implementations;
  - which forms of verification remain difficult;
  - how Grounded Vaults support continuity;
  - and where existing technical competence produces disproportionate benefits.
The concept of **asymmetric amplification** describes the possibility that generative systems extend the capabilities of already hybrid scholar-developers more strongly than those of researchers without the ability to diagnose technical behaviour or inspect generated code.
Teaching therefore cannot focus only on prompt formulation. It must include:
  - model literacy;
  - research data literacy;
  - context and knowledge organisation;
  - specification;
  - failure diagnosis;
  - verification;
  - and awareness of the boundary to Research Software Engineering.
-----
# Part VI
## Worked Example, Boundaries, and Implications
## Chapter 21
### A Complete Worked Example
A complete example follows one research project from its initial question to a published artefact.
The tutorial project uses an open, manageable dataset with:
  - genuine semantic complexity;
  - missing values;
  - uncertainty;
  - several plausible research perspectives;
  - and sufficient structure for deterministic processing.
The chapter proceeds through:
1.  formulation of the research question;
2.  identification of users and scholarly activities;
3.  inspection and profiling of the data;
4.  creation of the Grounded Vault;
5.  preparation of data.md;
6.  preparation of requirements.md;
7.  preparation of design.md;
8.  definition of verification criteria;
9.  creation of the action document;
10. generation of a minimal artefact;
11. inspection of factual, conceptual, visual, and technical failures;
12. classification of each failure by knowledge layer;
13. revision of the documents;
14. deterministic validation;
15. LLM-mediated review;
16. verification by the Critical Expert;
17. publication and provenance documentation;
18. decision between closure, maintenance, and RSE handover.
The worked example demonstrates not only how to produce an artefact but how to diagnose why a generated artefact is wrong and where a persistent correction belongs.
Detailed commands, files, prompts, screenshots, exercises, and alternative implementations are provided in a companion repository rather than reproduced in full within the monograph.
## Chapter 22
### From Promptotype to Research Software Engineering
The technical and organisational boundary of Promptotyping is reached when the obligations attached to an artefact change.
Static, self-contained artefacts are often appropriate for bounded research purposes because they can:
  - operate locally;
  - be deployed through static hosting;
  - avoid persistent backend infrastructure;
  - reduce dependency chains;
  - remain inspectable;
  - and support archiving.
Their limits include:
  - browser memory;
  - large-scale computation;
  - shared state;
  - authentication;
  - simultaneous editing;
  - persistent writes;
  - security requirements;
  - accessibility obligations;
  - and continuing institutional support.
When these conditions become central, the artefact enters the domain of Research Software Engineering.
The handover should include:
  - research context;
  - source and data descriptions;
  - requirements;
  - design decisions;
  - test and verification concepts;
  - known limitations;
  - dependency inventories;
  - process history;
  - provenance;
  - and unresolved questions.
Promptotyping can make the handover more inspectable. It cannot eliminate the expertise and resources required for sustainable software engineering.
## Chapter 23
### Reconstructability, Sustainability, and Proprietary Dependence
Generative systems are stochastic and often proprietary. Identical regeneration cannot be assumed even when prompts, data, and model names are recorded.
The chapter therefore distinguishes exact reproducibility from **reconstructability**.
A research process is reconstructable when enough of its evidential basis, project knowledge, specifications, code, transformations, decisions, and verification history remain available for another person to understand and reproduce the logic of the work, even if the generated implementation is not byte-identical.
The chapter examines:
  - model version changes;
  - hidden system instructions;
  - unavailable proprietary models;
  - changing product behaviour;
  - costs and access restrictions;
  - service discontinuation;
  - dependency preservation;
  - local and open models;
  - archived outputs;
  - provenance declarations;
  - and publication strategies.
Sustainability requires preserving not only generated code but also the knowledge and decisions from which that code was derived.
## Chapter 24
### Amplification, Responsibility, and the Limits of Externalisation
Promptotyping externalises parts of the translation between scholarly knowledge and computational implementation. It does not externalise all scholarly competence.
Tacit knowledge, familiarity with a corpus, sensitivity to exceptional sources, awareness of disciplinary debates, and recognition of absent alternatives may resist complete documentation.
The method should therefore be understood as **amplification rather than automation**.
It amplifies:
  - the continuity of scholarly knowledge across sessions;
  - the reach of a hybrid scholar-developer;
  - the reuse of requirements and design decisions;
  - the inspectability of implementation;
  - the ability to generate alternative computational forms;
  - and the transfer of project understanding between humans and agents.
It cannot replace:
  - scholarly expertise;
  - source criticism;
  - data modelling;
  - formal validation;
  - security engineering;
  - accessibility work;
  - maintenance;
  - institutional governance;
  - professional Research Software Engineering;
  - or responsibility for published claims.
Responsibility follows from acceptance and publication, not from exclusive manual production.
-----
# Conclusion
## Grounded Generative Research
Generative systems reduce the amount of manual formalisation required between scholarly descriptions and executable computational forms. They make it possible to derive analyses, transformations, interfaces, and research software from natural-language specifications and structured data.
This capacity does not create a neutral passage from research material to computational output. Research data are selective representations, context is constructed for particular purposes, specifications remain incomplete, generated implementation is stochastic, and every research artefact operationalises decisions about what should become visible, comparable, modifiable, or verifiable.
The methodological task is therefore not to make agents autonomous from scholarship. It is to create environments in which scholarly knowledge can guide agentic work and in which generated outputs remain inspectable against their evidential and conceptual foundations.
The book has developed this argument through five connected concepts:
  - **Prompt Engineering** as the systematic design and evaluation of model inputs;
  - **Context Engineering** as the task-specific construction of information available during model interaction;
  - **Knowledge Engineering** as the persistent representation and governance of project knowledge;
  - **Agentic Engineering** as the organisation of extended model-mediated work;
  - and **Promptotyping** as a method for translating structured research data and scholarly specifications into verifiable research artefacts.
The Grounded Vault provides the knowledge environment connecting these practices. The Critical Expert preserves scholarly authority where acceptance depends on interpretation, contextualisation, source criticism, and disciplinary judgement.
Applied generative AI for research is therefore not defined by the use of a particular model or tool. It is defined by a methodological arrangement in which evidence, knowledge, context, execution, feedback, and authority remain explicitly related.
Generative systems can amplify research when their outputs are grounded, their actions are bounded, their transformations are inspectable, their limitations are documented, and their claims remain subject to critical scholarly verification.
## Ressourcen die man einbauen kann: 
  - <https://docs.google.com/document/d/1LK8nLJ6elOMukM_iUtNKXFvn0CHKvBVeyC1jnd0kBYM/edit?tab=t.0> 
  - [https://dhcraft.org/excellence/blog](https://dhcraft.org/excellence/blog/)
