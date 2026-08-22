---
type: assertion
topics: ["[[Generative-Models]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-en#^e21]]"
  - "[[20_distillates/documents/lecture-notes-de#^s48]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# A prompt intervenes in the computation the model is currently performing rather than wrapping a fixed answer

## Statement

Prompts and context alter the token sequence supplied to the model, and that sequence conditions the distributed computation from which the next tokens follow. Different formulations change the internal activations from which the output distribution arises, which is why wording has effects that no theory of a fixed answer would predict.

## Support

- [[20_distillates/documents/lecture-notes-en#^e21]] — states that the supplied sequence conditions the computation and that prompting is an intervention on it
- [[20_distillates/documents/lecture-notes-de#^s48]] — states that different formulations change the internal activations behind the output distribution

## Related

- [[30_assertions/attention-relates-positions-across-layers]]
- [[30_assertions/the-latent-program-space-models-prompt-effects]]
