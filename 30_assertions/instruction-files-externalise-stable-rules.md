---
type: assertion
topics: ["[[Grounded-Knowledge]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-en#^e116]]"
  - "[[20_distillates/documents/lecture-notes-en#^e117]]"
  - "[[20_distillates/documents/lecture-notes-en#^e119]]"
  - "[[20_distillates/documents/slide-deck#^k45]]"
  - "[[20_distillates/documents/slide-deck#^k54]]"
  - "[[20_distillates/documents/slide-deck#^k55]]"
  - "[[20_distillates/documents/slide-deck#^k56]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# An instruction file externalises the rules that would otherwise be retyped into every prompt

## Statement

A file at the root of a project is loaded into the context at the start of a session and describes how this project works, and files can be nested so that the one closer to the working directory overrides a superordinate one by convention. A global file holds person-bound policy that is durable across projects while project facts stay one level down. The signals for adding an entry are that the agent repeats a mistake, that a review finds something it should have known, that the same correction is typed again, or that a new participant would need the same context.

## Support

- [[20_distillates/documents/lecture-notes-en#^e116]] — states that repeated guidance should not be retyped and what persistent artefacts achieve
- [[20_distillates/documents/lecture-notes-en#^e117]] — states the division between durable global content and project-specific facts
- [[20_distillates/documents/lecture-notes-en#^e119]] — states that such files stay concise and that task-specific procedure belongs in a skill
- [[20_distillates/documents/slide-deck#^k45]] — describes automatic loading at session start and the nesting with precedence
- [[20_distillates/documents/slide-deck#^k54]] — names the four signals for adding an entry
- [[20_distillates/documents/slide-deck#^k55]] — states the selection criterion for the global level
- [[20_distillates/documents/slide-deck#^k56]] — states what the project level holds and that precedence is convention rather than mechanism

## Related

- [[30_assertions/four-artefact-kinds-carry-different-duties]]
- [[30_assertions/instruction-files-are-context-not-enforcement]]
