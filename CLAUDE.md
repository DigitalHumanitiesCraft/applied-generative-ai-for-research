# Applied Generative AI for Research — Agent Action Layer

This vault is a Grounded Vault instance. Every substantive statement you produce here must carry a grounding anchor; the rules live in `knowledge/`, and this file only routes you there. Do not duplicate rules here.

## Session start

Read in this order: `knowledge/index.md` (terminology), `knowledge/state.md` (where work stands), then the document your task routes to below.

## Task routing

| Task | Read first | Chain |
|---|---|---|
| Instantiate the vault | `SETUP.md` | setup |
| Add a source | `knowledge/operations.md` § Acquire, Ingest | acquire → ingest |
| Distill a source | `knowledge/schema.md` § Distillate, `operations.md` § Distill | three-stage chain |
| Build or revise assertions | `schema.md` § Assertion, `operations.md` § Build assertions | assertions |
| Write a chapter | `schema.md` § Chapter, `operations.md` § Write chapters | chapters |
| Answer a question | `operations.md` § Query | query |
| Check the vault | `operations.md` § Check | validate → review |

## Hard rules

- Anchors are minted only at their own layer; never invent a block or statement ID that does not exist.
- A Markdown representation is never edited after ingest; a revised source enters as a new file with a date-suffixed slug.
- A status is set only after its check ran; record the date in `checked`. Never set `verified`; that is the human verification role's alone.
- Own conclusions become posits in the output, never assertions.
- Run `python tools/validate.py .` before reporting any production task as done. Zero errors alone is not the criterion; every warning is a finding to act on.
- Volatile state goes to `knowledge/state.md`, decisions to `knowledge/journal.md` (append-only).
- Working language of content: English leads for output, assertions and distillates; German is a complete parallel version of the output alone, in `40_output/de/`. This action layer and `knowledge/` stay English.

## Harness block (exchangeable)

This block is specific to Claude Code and may be replaced for another harness. For Claude Code the three skills `ingest-source`, `distill-source` and `build-assertions` live under `.claude/skills/` and route to the corresponding sections of `knowledge/operations.md`, which stays the single place the rules are written down. The project page generator `tools/build_docs.py` renders both language routes into `docs/`, so run it after a chapter milestone and hold to `knowledge/design.md`, which is binding for the reading view.

- Commit at milestones with concise English imperative messages; stage explicit paths.
- Run the vault's own check and build tools and the test suite unasked: `python tools/validate.py .`, `python tools/inventory.py . --write`, `python -m pytest tests`, `ruff check .`.
- Stage explicit paths and never the whole tree. A commit subject is English, imperative and at most 72 characters.
- Never push generated bulk artefacts, and never commit an original from `00_sources/` whose rights the project does not hold.
- External, identity-bearing and destructive actions need operator authority: publishing, releases, tags, repository settings, GitHub Pages, force pushes, history rewrites, and any write outside this repository.
- Read `knowledge/project.md` for the sub-goals and the feeding map, `knowledge/outline.md` for the chapter the task names, and `knowledge/sources.md` before treating any material as a source.
