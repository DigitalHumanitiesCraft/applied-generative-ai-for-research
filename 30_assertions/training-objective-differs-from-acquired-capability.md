---
type: assertion
topics: ["[[Generative-Models]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-en#^e17]]"
  - "[[20_distillates/documents/lecture-notes-en#^e18]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# The training objective of next-token prediction is not identical to the capabilities a model acquires

## Statement

Next-token prediction names the optimisation problem of autoregressive language modelling. Performing it well across heterogeneous data requires representations and transformations associated with syntax, concepts, relations, styles, code and recurring patterns of reasoning, and those structures then support work the objective never named. The objective also asks which continuation is probable rather than whether a proposition is true.

## Support

- [[20_distillates/documents/lecture-notes-en#^e17]] — separates the optimisation problem from the representations acquired while solving it
- [[20_distillates/documents/lecture-notes-en#^e18]] — states that the objective does not ask after truth and that world representations can still arise

## Related

- [[30_assertions/llm-computes-next-token-probabilities]]
- [[30_assertions/parametric-knowledge-carries-no-provenance]]
