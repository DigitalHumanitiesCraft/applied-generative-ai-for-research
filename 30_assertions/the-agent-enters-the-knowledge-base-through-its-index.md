---
type: assertion
topics: ["[[Promptotyping]]"]
status: grounded
checked: {}
grounding:
  - "[[20_distillates/documents/promptotyping-document-templates#^t38]]"
contested-with: []
created: 2026-08-22
updated: 2026-08-22
---

# The agent reads the index, then the open handover points, and then the task-relevant document, from repository-internal sources

## Statement

At every session start the agent reads the index of the knowledge base, then the process inbox of open handover points, and then the declarative or action document relevant to its task, consulting the provenance record where reasons for a decision are needed. The routing must point at repository-internal sources, because a repository whose method knowledge lies only in an external vault is blind in a session without access to that vault.

## Support

- [[20_distillates/documents/promptotyping-document-templates#^t38]] — the reading order at session start and the internality requirement

## Related

- [[30_assertions/MOC-Promptotyping]]
