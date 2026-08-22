---
type: assertion
topics: ["[[Generative-Models]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-en#^e114]]"
  - "[[20_distillates/documents/lecture-notes-en#^e115]]"
  - "[[20_distillates/documents/lecture-notes-de#^s114]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# Tool use changes the epistemic structure of a workflow because the system can obtain observations that constrain it

## Statement

Tools extend a text generator into a system that can act on an environment through file access, terminals, code execution, search, databases, browsers, validators and interfaces. They matter most where they return evidence about the consequences of an action, since a compiler, a test suite or a schema validator answers a question the model would otherwise answer about itself.

## Support

- [[20_distillates/documents/lecture-notes-en#^e114]] — states that tools matter especially where they return deterministic evidence about consequences
- [[20_distillates/documents/lecture-notes-en#^e115]] — states that the system no longer relies only on generated text and can obtain constraining observations
- [[20_distillates/documents/lecture-notes-de#^s114]] — lists the tool classes through which a model can act on an environment

## Related

- [[30_assertions/probabilistic-and-deterministic-operations-combine]]
- [[30_assertions/the-harness-is-the-technical-layer-of-action]]
