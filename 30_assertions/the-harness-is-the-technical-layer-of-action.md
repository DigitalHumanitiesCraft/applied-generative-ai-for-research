---
type: assertion
topics: ["[[Generative-Models]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-de#^s23]]"
  - "[[20_distillates/documents/lecture-notes-de#^s24]]"
  - "[[20_distillates/documents/lecture-notes-en#^e111]]"
  - "[[20_distillates/documents/slide-deck#^k9]]"
  - "[[20_distillates/documents/slide-deck#^k11]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# The AI harness is the technical layer through which a model receives context, calls tools, acts and processes feedback

## Statement

The harness gives access to files, tools and execution environments and manages state, permissions and control flow. It fixes which folders may be read or changed, which commands run without confirmation, how tool outputs return into the context, how long a run continues, when a person must be involved and how intermediate results are stored, and by doing so it determines what a trajectory can later be checked against.

## Support

- [[20_distillates/documents/lecture-notes-de#^s23]] — defines the harness as the technical software layer for context, tools, files, execution and feedback
- [[20_distillates/documents/lecture-notes-de#^s24]] — lists the concrete decisions a harness fixes for a run
- [[20_distillates/documents/lecture-notes-en#^e111]] — names what a harness manages and draws the consequence for what should be evaluated
- [[20_distillates/documents/slide-deck#^k9]] — gives the compact definition of the harness as the technical environment of agentic work
- [[20_distillates/documents/slide-deck#^k11]] — states that the harness manages state, access rights and control flow

## Related

- [[30_assertions/agentic-capability-arises-from-the-compound-system]]
- [[30_assertions/the-harness-supplies-no-scholarly-authority]]
