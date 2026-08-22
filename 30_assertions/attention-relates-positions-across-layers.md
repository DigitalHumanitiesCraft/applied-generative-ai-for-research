---
type: assertion
topics: ["[[Generative-Models]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-en#^e19]]"
  - "[[20_distillates/documents/lecture-notes-en#^e20]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# The Transformer architecture lets information at different positions of a sequence influence one another across repeated layers

## Statement

Most contemporary large language models are Transformers. Attention mechanisms in repeated layers allow positions to condition one another, so the probability assigned to a continuation results from transformations across many layers and high-dimensional representations rather than from a lookup.

## Support

- [[20_distillates/documents/lecture-notes-en#^e19]] — names the architecture and the role of attention across repeated layers
- [[20_distillates/documents/lecture-notes-en#^e20]] — states that self-attention builds context-dependent representations and that the output probability follows from many layers

## Related

- [[30_assertions/representations-are-contextual-not-fixed]]
- [[30_assertions/prompting-intervenes-in-the-current-computation]]
