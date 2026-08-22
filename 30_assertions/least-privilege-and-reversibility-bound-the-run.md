---
type: assertion
topics: ["[[Agentic-Work]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/lecture-notes-de#^s115]]"
  - "[[20_distillates/documents/lecture-notes-de#^s116]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# Least privilege and reversibility are the two bounds a run is given

## Statement

A tool call can change the project state, so access follows the least necessary permission. Source files are read and not overwritten, generated files may change in a working folder, validators may run without confirmation, publication steps need an explicit release, and changes stay versioned and reversible.

## Support

- [[20_distillates/documents/lecture-notes-de#^s115]] — states the principle of least necessary permission and its reason
- [[20_distillates/documents/lecture-notes-de#^s116]] — gives the concrete permission pattern including release and reversibility

## Related

- [[30_assertions/instruction-files-are-context-not-enforcement]]
- [[30_assertions/intervention-points-are-named-in-advance]]
