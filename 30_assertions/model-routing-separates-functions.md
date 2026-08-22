---
type: assertion
topics: ["[[Agentic-Work]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-en#^e130]]"
  - "[[20_distillates/documents/lecture-notes-en#^e131]]"
  - "[[20_distillates/documents/lecture-notes-en#^e132]]"
  - "[[20_distillates/documents/slide-deck#^k66]]"
  - "[[20_distillates/documents/slide-deck#^k67]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# Model routing separates the functions of a workflow rather than fixing a provider combination

## Statement

Planning, implementation and review need neither the same model nor the same inference budget, so planning and review can run on a model chosen for reasoning while implementation runs on one chosen for throughput. The specification produced stays contextualised by the maintained project knowledge, and the routing itself is an engineering decision that changes as models change.

## Support

- [[20_distillates/documents/lecture-notes-en#^e130]] — states that phases can be routed to different models with different inference budgets
- [[20_distillates/documents/lecture-notes-en#^e131]] — gives the concrete assignment of planning and review against implementation
- [[20_distillates/documents/lecture-notes-en#^e132]] — states that routing is an engineering decision and names the durable abstraction
- [[20_distillates/documents/slide-deck#^k66]] — gives the separation of planning from execution and the assignment by model strength
- [[20_distillates/documents/slide-deck#^k67]] — states that the specification is contextualised in the knowledge holding

## Related

- [[30_assertions/the-mechanisms-are-not-interchangeable]]
- [[30_assertions/specification-precedes-implementation]]
