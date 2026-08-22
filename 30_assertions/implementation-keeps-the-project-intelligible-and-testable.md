---
type: assertion
topics: ["[[Promptotyping]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/promptotyping-paper#^s042]]"
  - "[[20_distillates/documents/promptotyping-document-templates#^t27]]"
  - "[[20_distillates/documents/promptotyping-document-templates#^t28]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# Agentic implementation requires the project state to remain intelligible and testable as it develops

## Statement

Generated code may require refactoring, and executable checks are added or revised where relevant behaviour can be formalised, because these practices preserve the inspectability of the implementation and make it easier to relate observed behaviour to the documents that guide it. The document that carries the test strategy states its guarantees, its deliberate gaps, and its reproducible run commands, and it tells the agent in which form a new guarantee is to be secured, which lifts a sign-off from an assertion that something holds to a measurement that a check is green.

## Support

- [[20_distillates/documents/promptotyping-paper#^s042]] — the role of refactoring and checks in preserving inspectability
- [[20_distillates/documents/promptotyping-document-templates#^t27]] — what the test document carries and the trigger for keeping it
- [[20_distillates/documents/promptotyping-document-templates#^t28]] — the shift from assertion to measurement that the document enforces

## Related

- [[30_assertions/MOC-Promptotyping]]
