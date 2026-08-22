---
type: distillate
source-type: document
representation: "[[10_markdown/documents/slide-deck]]"
topics: ["[[Generative-Models]]", "[[Grounded-Knowledge]]", "[[Agentic-Work]]", "[[Promptotyping]]"]
status: grounded
checked: {}
created: 2026-08-22
updated: 2026-08-22
---

# Distillate: Full Slide Deck

The slide-text export of the teaching deck carries the compact definitional slides of the three engineering layers together with the speaker notes, and the notes hold formulations that neither set of lecture notes contains, on the two sources of Knowledge Engineering, on the shift of the formalisation target, on the knowledge system as a production system, and on the mechanisms behind the context bottleneck. Statements the lecture notes already carry in the same sense are not repeated here; the parallel distillates are [[20_distillates/documents/lecture-notes-de]] and [[20_distillates/documents/lecture-notes-en]].

## Core statements

- Knowledge Engineering, Context Engineering and Agentic Engineering denote three connected layers of work with LLM-based AI agents. [[10_markdown/documents/slide-deck#^p0008]] ^k1
- Knowledge Engineering covers research data, documentation, requirements, design decisions and process knowledge as well as knowledge that is at first only implicitly present in individual experts or an organisation, held in a form in which it can be read, checked, extended and corrected. [[10_markdown/documents/slide-deck#^p0009]] ^k2
- Context Engineering concerns the information state of a concrete task and determines which information, instructions, tools and examples are available in the context window at a given moment, in which order they are supplied and what is deliberately not loaded. [[10_markdown/documents/slide-deck#^p0010]] ^k3
- Agentic Engineering is broader than agentic software development, because the work is directed not only at code but also at data descriptions, specifications, mappings, design decisions, process documents and verification concepts. [[10_markdown/documents/slide-deck#^p0011]] ^k4
- The harness provides access to files, tools and execution environments and the management of state, permissions and feedback, and it does not itself decide which project knowledge is relevant or scholarly adequate. [[10_markdown/documents/slide-deck#^p0012]] ^k5
- The arrangement of the three layers automates no neutral translation of research data into software and instead makes explicit that part of the translation which can be formulated, documented and checked. [[10_markdown/documents/slide-deck#^p0014]] ^k6
- Responsibility for the interpretation of the data, for the scholarly adequacy of the modelling and for the acceptance of a digital research artefact remains with the persons responsible for the research. [[10_markdown/documents/slide-deck#^p0014]] ^k7
- An AI agent is an LLM-based system for multi-step, tool-supported task execution. [[10_markdown/documents/slide-deck#^p0056]] ^k8
- An AI harness is the technical environment in which AI agents receive context, use tools, execute tasks and process feedback. [[10_markdown/documents/slide-deck#^p0060]] ^k9
- Context Engineering is the selection, organisation and provision of task-relevant information in the context window of an LLM. [[10_markdown/documents/slide-deck#^p0066]] ^k10
- The harness manages state, access rights and control flow. [[10_markdown/documents/slide-deck#^p0077]] ^k11
- The preparation phase of an agentic workflow establishes a reliable project holding before the agent analyses or implements anything. [[10_markdown/documents/slide-deck#^p0118]] ^k12
- A preparation prompt states a goal rather than prescribing every single action, and the agent works inside a harness that gives it access to files, the web, a terminal and further tools. [[10_markdown/documents/slide-deck#^p0119]] ^k13
- The agent perceives and changes the existing project state through files, reaches web resources and the local environment through tool use, and repeats the sequence of checking the state, choosing an action, executing a tool, processing the result and deciding the next step. [[10_markdown/documents/slide-deck#^p0120]] ^k14
- The result of the preparation phase is a persistent and traceable project holding rather than an answer in the chat, with sources structured, their provenance documented and the source files unchanged. [[10_markdown/documents/slide-deck#^p0121]] ^k15
- Preparation matters methodologically because later work does not begin from nothing and every further step builds on the prepared holding. [[10_markdown/documents/slide-deck#^p0122]] ^k16
- The planning step asks for a conceptual approach before implementation and for a very compact plan in simple language without losing complexity. [[10_markdown/documents/slide-deck#^p0128]] ^k17
- The feedback step instructs the agent to ask targeted questions about everything that cannot be derived reliably from the existing files and to make no silent assumptions. [[10_markdown/documents/slide-deck#^p0148]] ^k18
- The verification step checks whether the artefact runs, whether the data are read and displayed correctly, whether the agreed requirements are implemented and whether the source files have remained unchanged. [[10_markdown/documents/slide-deck#^p0160]] ^k19
- In an eight-thousand-token window, six thousand input tokens leave room for two thousand output tokens, while ten thousand input tokens with fifteen hundred generated tokens exceed the limit by three and a half thousand, so the system must shorten the sequence through truncation or compaction or reject the request. [[10_markdown/documents/slide-deck#^p0190]] ^k20
- The formal context limit determines which tokens can be available while context rot concerns how reliably the model uses them, so task performance can decline before the formal limit is reached. [[10_markdown/documents/slide-deck#^p0190]] ^k21
- Context compression denotes only the reduction of volume, which does not suffice for Context Engineering. [[10_markdown/documents/slide-deck#^p0198]] ^k22
- Distillation should preserve relevant terms and distinctions, relations and dependencies, conditions and constraints, uncertainties and open questions, and justifications and decision contexts. [[10_markdown/documents/slide-deck#^p0201]] ^k23
- The same source material can be distilled differently when purpose or task change, so a summary for a general introduction differs from a representation that is to guide an agent in implementation or verification. [[10_markdown/documents/slide-deck#^p0207]] ^k24
- Distillation is expressly demarcated from mere summary and from context compression, because it produces an inspectable representation intended to be sufficient for further work. [[10_markdown/documents/slide-deck#^p0208]] ^k25
- A knowledge document treats a clearly delimited subject or fulfils a particular function rather than depicting the whole body of knowledge. [[10_markdown/documents/slide-deck#^p0316]] ^k26
- Markdown suits the serialization of knowledge documents because it is open plain text, supports simple structures, is versionable and linkable, and can be read directly by humans and by LLMs. [[10_markdown/documents/slide-deck#^p0327]] ^k27
- Knowledge documents lie persistently in a knowledge base or project environment and need not be loaded into the context window in full for every task. [[10_markdown/documents/slide-deck#^p0236]] ^k28
- The knowledge base preserves available knowledge and Context Engineering assembles from it the working context suited to a concrete task, and the two must not be equated because they fulfil different functions. [[10_markdown/documents/slide-deck#^p0252]] ^k29
- Agentic Engineering comprises the systematic organisation of multi-step agentic work, in particular the decomposition and coordination of tasks, the use of tools, the response to intermediate results, the necessary human interventions and the checking and continuation of the work. [[10_markdown/documents/slide-deck#^p0255]] ^k30
- Agentic Engineering organises how an AI agent acts across several steps, responds to results and continues its work in a checkable manner. [[10_markdown/documents/slide-deck#^p0267]] ^k31
- Knowledge Engineering covers the construction and maintenance of explicit, revisable project knowledge that records the current understanding a project has of its data, its purpose and the decisions relevant to implementation. [[10_markdown/documents/slide-deck#^p0269]] ^k32
- Knowledge can be present without being explicitly documented, shared or usable by an agent. [[10_markdown/documents/slide-deck#^p0272]] ^k33
- Existing local order does not yet amount to a shared knowledge base usable across a system. [[10_markdown/documents/slide-deck#^p0276]] ^k34
- Knowledge modelling constructs a knowledge base by identifying the concepts of a domain, representing them formally and making them queryable. [[10_markdown/documents/slide-deck#^p0285]] ^k35
- Personal Information Management concerns the handling of one's own information across formats and locations in the service of goals and roles, with fragmentation as its core problem. [[10_markdown/documents/slide-deck#^p0287]] ^k36
- Knowledge Engineering has two sources, existing documents and data that are prepared and converted into machine-readable and distilled forms, and knowledge that stands in no document and is raised from experts, institutions and projects through interviews, deep dives and requirements elicitation into the same structured form. [[10_markdown/documents/slide-deck#^p0405]] ^k37
- The shift against the classical expert-system reading of Knowledge Engineering lies in the formalisation target, which is no longer logic and ontology but structured natural language with a light metadata component, because the language model supplies the language understanding. [[10_markdown/documents/slide-deck#^p0405]] ^k38
- Context Engineering presupposes Knowledge Engineering, because only a structured holding permits selective loading, which is the demarcation against the short circuit that treats Context Engineering as better prompting. [[10_markdown/documents/slide-deck#^p0406]] ^k39
- The knowledge system serves the derivation of target artefacts such as a concept, a proposal, a specification or a data model rather than storage, and curated condensed knowledge documents serve as the input of the step that produces the artefact. [[10_markdown/documents/slide-deck#^p0407]] ^k40
- The user story forms the bridge between building the holding and providing the context, because it puts a subject-matter requirement into a form that humans understand and an agent can use as context. [[10_markdown/documents/slide-deck#^p0407]] ^k41
- A knowledge management system that stores notes as plain-text files in an ordinary local folder keeps the data on the user's own machine in an open format without a server or a cloud account. [[10_markdown/documents/slide-deck#^p0417]] ^k42
- An external memory organises individual and institutional knowledge, steers operative work and projects, and models and represents knowledge structures. [[10_markdown/documents/slide-deck#^p0418]] ^k43
- An external memory is what an AI agent needs, because its context window is a bounded and volatile working memory while a folder of open text files is the long-term store, and the agent reads and writes the same files a person does. [[10_markdown/documents/slide-deck#^p0419]] ^k44
- An instruction file at the root of a project is loaded automatically into the context at the start of every session, describes how this project works, and can be nested so that a file closer to the working directory overrides the rules of a superordinate one. [[10_markdown/documents/slide-deck#^p0437]] ^k45
- Only the name and description of a skill stay permanently present in the context, which keeps the context window free during unrelated tasks. [[10_markdown/documents/slide-deck#^p0441]] ^k46
- A tool protocol solves the problem that M agents and N tools would otherwise need M times N bespoke connections, because a tool is wrapped in a server that every protocol-speaking agent can use. [[10_markdown/documents/slide-deck#^p0447]] ^k47
- An agent-to-agent standard is characterised by opacity, meaning interaction without disclosing memory, tools or proprietary logic, and by extensibility through formal extensions with a staged promotion procedure that keeps the core stable. [[10_markdown/documents/slide-deck#^p0450]] ^k48
- The subagent pattern has no formal standard and appears in nearly identical form across practically all agent systems, with the two typical cases of a task too large for one context window and a workload that can be parallelised. [[10_markdown/documents/slide-deck#^p0457]] ^k49
- With growing autonomy the bottleneck shifts from the model to the context. [[10_markdown/documents/slide-deck#^p0460]] ^k50
- Three mechanisms explain the weak result of an agent working from an unstructured holding, degradation of model performance well below the nominal window limit, accumulation of noise across a long autonomous run, and a finite reasoning budget spent on navigating disordered material. [[10_markdown/documents/slide-deck#^p0464]] ^k51
- Strong models are robust against untidy context for short single queries, and the problem turns at long-horizon delegation when the agent works with the material independently across many steps. [[10_markdown/documents/slide-deck#^p0465]] ^k52
- Radically shortened context loses provenance and justification and makes the result differently bad rather than better, so the target is dense and sufficient, every statement carrying information, and the architectural answer is a layered base whose minimal core stays permanently loaded while depth is loaded on demand. [[10_markdown/documents/slide-deck#^p0466]] ^k53
- An instruction file holds what would otherwise be retyped, and the four signals for adding an entry are that the agent repeats a mistake, that a review finds something the agent should have known about this codebase, that the same correction is typed as in the previous session, and that a new team member would need the same context. [[10_markdown/documents/slide-deck#^p0505]] ^k54
- A global instruction file holds person-bound policy that is durable and independent of any project, while everything concerning only one project moves one level down. [[10_markdown/documents/slide-deck#^p0512]] ^k55
- A project-specific instruction file holds project-bound facts such as build and test commands, conventions, project structure and domain terms, and in case of contradiction the more specific document applies by convention rather than by mechanism, because the levels are technically only concatenated. [[10_markdown/documents/slide-deck#^p0519]] ^k56
- Cybernetics describes in 1948 how a system steers itself by feeding back information about its own effects, and the agentic execution loop of acting, reading the result and acting again is such a control loop whose feedback runs through tool outputs instead of sensors. [[10_markdown/documents/slide-deck#^p0599]] ^k57
- The four agent properties formulated in 1995, autonomy, reactivity, proactiveness and social ability, map onto contemporary systems as running without query across many steps, processing tool results and errors, pursuing goals beyond the single instruction, and delegating to subagents. [[10_markdown/documents/slide-deck#^p0600]] ^k58
- Language models did not reinvent the agent idea and supplied the missing component, a behavioural module that understands language and can plan actions. [[10_markdown/documents/slide-deck#^p0600]] ^k59
- The Semantic Web vision of 2001 did not aim at machines understanding human language, and machine-understandable documents meant only that a machine solves a well-defined problem on well-defined data, with humans structuring their data for the machine through ontologies and unique identifiers. [[10_markdown/documents/slide-deck#^p0613]] ^k60
- Contemporary language models solve the same task by the reverse route, processing unstructured text directly without the ontological infrastructure the Semantic Web presupposed. [[10_markdown/documents/slide-deck#^p0614]] ^k61
- An AI agent in the narrower taxonomic sense is a modular system driven by a language model for delimited tasks, with tool access, memory and planning around the model as its core. [[10_markdown/documents/slide-deck#^p0626]] ^k62
- Agentic AI is an orchestrated federation of several agents characterised by collaboration, dynamic task decomposition, persistent memory and coordinated autonomy rather than by more autonomy. [[10_markdown/documents/slide-deck#^p0627]] ^k63
- The same tool shows both modes, acting as a single agent in a simple run and moving towards the orchestrated federation once it delegates partial tasks to several coordinated instances working in parallel, so the distinction describes two modes of operation rather than a fixed category. [[10_markdown/documents/slide-deck#^p0628]] ^k64
- Subagents can draw on an epistemic infrastructure of knowledge documents and tools such as schemas and scripts when they verify and validate a generated encoding. [[10_markdown/documents/slide-deck#^p0389]] ^k65
- Model routing separates planning from execution and assigns planning and the review of a change to the strongest available model while execution runs on a model chosen for throughput. [[10_markdown/documents/slide-deck#^p0394]] ^k66
- The specification in a routed workflow is contextualised in the knowledge folder holding data, research and design rather than standing alone. [[10_markdown/documents/slide-deck#^p0398]] ^k67

## Terms

- **AI Agent**: an LLM-based system for multi-step, tool-supported task execution [[10_markdown/documents/slide-deck#^p0056]]
- **AI Harness**: the technical environment in which AI agents receive context, use tools, execute tasks and process feedback [[10_markdown/documents/slide-deck#^p0060]]
- **Agentic Engineering**: the organisation and control of multi-step agentic work, wider than agentic software development [[10_markdown/documents/slide-deck#^p0011]]
- **Knowledge Engineering**: the construction and maintenance of explicit, revisable project knowledge [[10_markdown/documents/slide-deck#^p0269]]
- **Context Engineering**: the selection, organisation and provision of task-relevant information in the context window [[10_markdown/documents/slide-deck#^p0066]]
- **Vault**: the ordinary local folder in which a plain-text knowledge management system stores its notes [[10_markdown/documents/slide-deck#^p0417]]
- **Agentic AI**: an orchestrated federation of several agents with collaboration, dynamic task decomposition, persistent memory and coordinated autonomy [[10_markdown/documents/slide-deck#^p0627]]

## Open questions

- The deck asserts that Context Engineering presupposes Knowledge Engineering without giving a criterion for how structured a holding must be before selective loading becomes possible.
- The layered knowledge base with a permanently loaded minimal core is named as the architectural answer to the context bottleneck, and the deck defers its construction to a later unit that the export does not contain.
- The deck reports the three mechanisms behind context degradation as established without distinguishing which of them rests on the cited measurement and which on practical observation.
- The export carries no heading structure, so a passage can be located only by its slide text, which makes any citation of the deck dependent on the wording remaining stable.

## Appraisal

The deck export is the weakest of the three feeding artefacts as a text and the strongest as a record of the argument's current state, because its speaker notes were written last and contain formulations the lecture notes have not yet absorbed. Two of them carry real weight for this book, the account of Knowledge Engineering as having two sources with a shifted formalisation target, and the reading of the knowledge system as a production system for target artefacts rather than an archive. Against that stands a genre problem. The export mixes finished speaker notes with slide fragments, placeholder lines and bare links, it carries no heading structure, and several passages are notes to self rather than statements. Anything taken from it therefore needs a second anchor in one of the lecture notes wherever the claim is load-bearing, and the deck is used here as a source of formulations rather than as an independent witness.

## Related

- [[20_distillates/documents/lecture-notes-de]]
- [[20_distillates/documents/lecture-notes-en]]
- [[30_assertions/MOC-Grounded-Knowledge]]
- [[30_assertions/MOC-Agentic-Work]]
