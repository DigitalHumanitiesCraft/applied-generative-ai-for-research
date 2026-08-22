---
type: assertion
topics: ["[[Generative-Models]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-en#^e24]]"
  - "[[20_distillates/documents/lecture-notes-en#^e78]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# A model adapts strongly to what stands in its context without any change of its weights

## Statement

Ordinary inference does not update parameters. The behaviour a user observes can nevertheless change substantially with the instructions, examples and information supplied in the current context, and that adaptation is what makes context a design surface rather than a convenience.

## Support

- [[20_distillates/documents/lecture-notes-en#^e24]] — states that inference does not update weights while adaptation to the context can be strong
- [[20_distillates/documents/lecture-notes-en#^e78]] — separates the technical capacity of the window from the information inside it and names in-context learning

## Related

- [[30_assertions/prompting-intervenes-in-the-current-computation]]
- [[30_assertions/the-context-window-is-a-finite-processing-space]]
