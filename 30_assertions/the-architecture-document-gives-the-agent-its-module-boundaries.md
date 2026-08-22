---
type: assertion
topics: ["[[Promptotyping]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/promptotyping-document-templates#^t20]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# The architecture document carries the technical realisation and gives the agent the module boundaries it builds against

## Statement

The document records stack, components, data flow, external models and services, and security and accessibility measures. The agent reads it before generating code, and its descriptions of module boundaries are what hold the implementation in place, so a description too vague produces code that ignores the intended layers.

## Support

- [[20_distillates/documents/promptotyping-document-templates#^t20]] — the content of the document, its agent readership, and the consequence of vagueness

## Related

- [[30_assertions/MOC-Promptotyping]]
