---
type: assertion
topics: ["[[Generative-Models]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-en#^e29]]"
  - "[[20_distillates/documents/lecture-notes-en#^e30]]"
  - "[[20_distillates/documents/lecture-notes-en#^e31]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# Tokenisation fixes the discrete unit over which model computation and context limits operate

## Statement

A tokenizer converts character sequences into discrete units that may correspond to a word, part of a word or punctuation, and each unit becomes a numerical identifier before it enters the network. The boundaries follow an engineering trade-off between vocabulary size, sequence length and the ability to represent unseen strings, so they need not be linguistically intuitive. Context capacity, input cost and output length are measured in these units.

## Support

- [[20_distillates/documents/lecture-notes-en#^e29]] — defines the tokenizer and the mapping of tokens to identifiers
- [[20_distillates/documents/lecture-notes-en#^e30]] — states the engineering trade-off and the lack of linguistic intuition in the boundaries
- [[20_distillates/documents/lecture-notes-en#^e31]] — states that windows, costs and lengths are measured in tokens

## Related

- [[30_assertions/representations-are-contextual-not-fixed]]
- [[30_assertions/the-context-window-is-a-finite-processing-space]]
