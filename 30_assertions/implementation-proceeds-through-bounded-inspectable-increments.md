---
type: assertion
topics: ["[[Promptotyping]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/promptotyping-paper#^s040]]"
  - "[[20_distillates/documents/promptotyping-paper#^s041]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# Implementation consists of bounded tasks and proceeds through inspectable, versioned increments

## Statement

Implementation makes maintained project knowledge actionable through language-model-supported development, either through iterative chat-based interaction or, where the agent must work directly with project files and continue across several steps, through an AI harness. Each increment should establish a runnable state that can be compared with the maintained project knowledge before further assumptions become embedded in the implementation.

## Support

- [[20_distillates/documents/promptotyping-paper#^s040]] — the two arrangements of implementation work and its bounded character
- [[20_distillates/documents/promptotyping-paper#^s041]] — the requirement that each increment reach a comparable runnable state

## Related

- [[30_assertions/MOC-Promptotyping]]
