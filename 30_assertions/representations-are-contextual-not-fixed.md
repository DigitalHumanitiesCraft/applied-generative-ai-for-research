---
type: assertion
topics: ["[[Generative-Models]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-en#^e32]]"
  - "[[20_distillates/documents/lecture-notes-en#^e33]]"
  - "[[20_distillates/documents/lecture-notes-en#^e34]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# Token representations are transformed across the network into contextual representations rather than holding one fixed meaning

## Statement

An embedding maps a discrete identifier into a high-dimensional space in which systematic relations among recurring patterns can emerge. That first mapping is transformed repeatedly, so what the network works with depends on the surrounding tokens and the current task. Two sentences of similar meaning in different registers can therefore condition different internal states.

## Support

- [[20_distillates/documents/lecture-notes-en#^e32]] — defines the embedding as the initial mapping and names the emergence of systematic relations
- [[20_distillates/documents/lecture-notes-en#^e33]] — states that the proximity illustration is incomplete and that representations become contextual
- [[20_distillates/documents/lecture-notes-en#^e34]] — gives the register case and draws the consequence for the effect of wording

## Related

- [[30_assertions/tokenisation-fixes-the-unit-of-computation]]
- [[30_assertions/prompting-intervenes-in-the-current-computation]]
