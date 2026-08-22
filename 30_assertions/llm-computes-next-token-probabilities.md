---
type: assertion
topics: ["[[Generative-Models]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-de#^s14]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# A large language model produces text by repeatedly computing a probability distribution over the next token

## Statement

The operation of a large language model is autoregressive. From the input sequence available so far it computes probabilities for the next token, and the token it selects becomes part of the context for the following prediction. Everything a reader sees as a finished answer is the accumulated result of that repetition.

## Support

- [[20_distillates/documents/lecture-notes-de#^s14]] — states the autoregressive procedure and the feedback of the selected token into the context

## Related

- [[30_assertions/model-output-stays-probabilistic]]
- [[30_assertions/training-objective-differs-from-acquired-capability]]
