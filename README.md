# Applied Generative AI for Research

**Knowledge, Context, Agents, and Verifiable Research Artefacts**

This repository holds a book manuscript on the controlled use of generative models and agentic systems in research, together with the source material it is written from and the machinery that checks it. The book develops applied generative AI for research as a methodological field, running the argument from prompting through context engineering and knowledge engineering to agentic engineering, and it develops two constructs at length, the Grounded Vault as a persistent knowledge environment and Promptotyping as a document-driven method for deriving research artefacts from structured research data.

The repository is itself a [Grounded Vault](https://github.com/DigitalHumanitiesCraft/grounded-vault) instance, so the book applies the method it describes to its own genesis. Every substantive sentence of the finished manuscript resolves through a chain of machine-checkable anchors to a passage in a registered source, and the checking state of every statement is readable at the statement itself.

## Bilingual structure

English is the leading language. German is a complete parallel version of the manuscript, not a summary and not a subset. The split lives in the output layer alone, `40_output/en/` and `40_output/de/`, one file per chapter under the same slug in both folders. The layers below the output stay English, so both language versions rest on the same assertions and cite the same source passages. German chapter titles carry `working-title: true` until the German version is written.

The manuscript runs to an introduction, six parts with twenty-four chapters, and a conclusion. The canonical outline is `knowledge/outline.md`; the current writing state per chapter is in the chapter register of `knowledge/state.md`.

## The vault layers

The production chain runs `00_sources → 10_markdown → 20_distillates → 30_assertions → 40_output`, and each layer is checkable on its own. Anchors are minted only at the layer they belong to, and each layer references only the layer directly beneath it.

- `00_sources/` holds the originals of the feeding material exactly as they arrived. Provenance, rights and the commit each source was taken at are recorded in `knowledge/sources.md`.
- `10_markdown/` holds the Markdown representation of each source with a block ID on every anchor-relevant passage. A representation is never edited after ingest.
- `20_distillates/` holds one distillate per source, meaning the statements of that source alone, each anchored to the block it was taken from and carrying its own statement ID.
- `30_assertions/` holds the atomic cross-source statements, each grounded in at least one distillate statement, together with one topic map per part of the book.
- `40_output/` holds the manuscript, one file per chapter, in which every load-bearing sentence carries a footnote to an assertion and every own conclusion is marked as a posit.

Across the chain lie the governance and support folders. `knowledge/` is the Promptotyping knowledge base that governs production, entered through `knowledge/index.md`. `references/` holds the bibliographic records of citable-only sources as CSL JSON. `glossary/` holds one file per central technical term. `tools/` holds the validator, the source inventory generator, the reference implementation of the machine review and a static-page generator. `tests/` holds the validator's own test suite with its fixture vaults.

Humans enter at `HOME.md` and read the vault in Obsidian, following wikilinks from an output footnote down to the supporting passage. Agents enter at `CLAUDE.md`, which routes every task onto the rule documents in `knowledge/`.

## Checking

Three instances check the vault with strictly separated authority. Validation is deterministic conformance checking against the vault's own schema. Machine review is adversarial checking by a language model under anti-anchoring, judging per pair whether a source location supports the statement built on it. Verification is human expert review by the Critical Expert, alone authorised to establish evidence. Statuses progress `grounded` to `validated` to `verified`, and a document never stands higher than the anchors it rests on.

```
uv sync                          # or: pip install pyyaml pytest
python tools/validate.py .       # conformance check of the whole vault
python tools/inventory.py .      # the source inventory as it would be written
python -m pytest tests           # the validator's own test suite
```

A chapter is judged for acceptance on its own with `python tools/validate.py . --chapter 40_output/en/<slug>`, which walks the chain that chapter hangs on and fails on any warning inside that scope. Over the whole vault a warning never fails the run, and every warning is still a finding to act on. While the manuscript is a skeleton, the run reports one `W-UNANCHORED` per chapter file, which names exactly the work that is outstanding.

`.github/workflows/checks.yml` runs the validator and the test suite on every push.

## Licence

The manuscript text, the knowledge base and the documentation are licensed under [CC BY 4.0](LICENSE). The code and tooling under `tools/` and `tests/` are licensed under the [MIT License](LICENSE-CODE). Third-party research material under `00_sources/` is excluded from these terms, and the rights to each source are recorded in the metadata block of its Markdown representation.

Christopher Pollin, [Digital Humanities Craft](https://dhcraft.org)
