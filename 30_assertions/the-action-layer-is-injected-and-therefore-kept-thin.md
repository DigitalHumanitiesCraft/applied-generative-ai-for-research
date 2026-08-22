---
type: assertion
topics: ["[[Promptotyping]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/promptotyping-document-templates#^t36]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# The action layer is injected at every session start, which makes drift there more expensive than in any other document

## Statement

Because the action document reaches the agent automatically at every session start, a stale rule in it propagates into every session. Every line derivable from the code or from the knowledge base is therefore deleted rather than maintained, which is the same distillation limit that governs the knowledge documents applied to the instruction layer.

## Support

- [[20_distillates/documents/promptotyping-document-templates#^t36]] — the injection at session start and the deletion rule that follows from it

## Related

- [[30_assertions/MOC-Promptotyping]]
