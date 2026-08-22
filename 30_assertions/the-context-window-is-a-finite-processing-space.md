---
type: assertion
topics: ["[[Grounded-Knowledge]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-de#^s57]]"
  - "[[20_distillates/documents/lecture-notes-de#^s58]]"
  - "[[20_distillates/documents/slide-deck#^k20]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# The context window is the finite processing space that holds everything a run can use

## Statement

A model processes only what is actually supplied within a run, including system and project instructions, the current input, the working history, document excerpts, tool descriptions, tool outputs, intermediate results and the generated answer. When input and output together exceed the limit the system must shorten the sequence through truncation or compaction or reject the request.

## Support

- [[20_distillates/documents/lecture-notes-de#^s57]] — lists what a run can hold in its context
- [[20_distillates/documents/lecture-notes-de#^s58]] — defines the window and states what its nominal size does and does not say
- [[20_distillates/documents/slide-deck#^k20]] — gives the arithmetic case in which input and output exceed the limit and names the consequences

## Related

- [[30_assertions/nominal-capacity-is-no-guarantee-of-use]]
- [[30_assertions/tokenisation-fixes-the-unit-of-computation]]
