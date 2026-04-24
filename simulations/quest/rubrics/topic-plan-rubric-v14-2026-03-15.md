Looking at the R13 scorecard, the differentiating evidence is in V-05 vs V-03 — both pass C-45 (per-schema items), but V-05 adds two properties V-03 lacks:

1. The annotation states the gate-pass threshold, not just the item count arithmetic
2. The PASS condition line itself enumerates all item labels as a named conjunction

Those are the two new criteria for v14.

---

## Rubric — topic:plan (v14)

**5 essential / 3 recommended / 39 aspirational — 47 criteria total**

### Essential (must all pass)

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | **Read strategy.md** — output cites at least one concrete reference to existing strategy structure | correctness |
| C-02 | **Signal inventory** — all 9 namespaces explicitly assessed with artifact filenames + dates | coverage |
| C-03 | **Delta detection** — NEW vs PRIOR split, only NEW drives proposals, strategy date named | correctness |
| C-04 | **Typed change proposals** — ADD / REMOVE / REPRIORITIZE; silence is not a null declaration | behavior |
| C-05 | **Confirmation gate** — stops before modifying strategy.md, presents visible YES/NO/REVISED gate | behavior |

### Recommended (need 2/3 for golden)

| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | **Evidence citation** — artifact filename in every non-null proposal row | depth |
| C-07 | **Before/after diff** — Before/After structure present for each proposal | format |
| C-08 | **Inertia justification** — per-row reason why NO CHANGE is insufficient | depth |

### Aspirational (C-09 — C-47, 39 total)

*(C-09 through C-42 unchanged from v12)*

**New in v13:**

| ID | Criterion | Category |
|----|-----------|----------|
| C-43 | **Cell-exhaustive gate enumeration** — each in-phase stop gate enumerates every mandatory column by name in its pass condition, requiring each named column to be non-null before the phase may advance; a gate whose pass condition checks only row count, block count, or structural presence without naming each mandatory column individually does not satisfy this criterion even if C-12 passes; a gate that fires when "all rows are present" but does not verify "all cells in mandatory columns are filled" is a structural presence gate, not a cell-exhaustive gate | behavior |
| C-44 | **Numbered Gate-0 label in block header** — the pre-signal stop gate (satisfying C-26) carries the explicit label "Gate-0" (or equivalent numbered identifier, e.g., "Gate-(-1)", "Gate-S") in its block section header, making it independently scannable as the first link in the numbered sequential gate chain without reading the gate body; a pre-signal gate that uses only a descriptive name (e.g., "CONTRACT COMPLETENESS GATE") without a numbered gate identifier in the header does not satisfy this criterion even if C-26 passes and the gate fires at the correct site; the numbered label is a header-level scannable property, not a body-level description | format |
| C-45 | **Schema-gate checklist atomicity** — the schema-phase gate (satisfying C-38) is structured as an explicitly numbered or labeled checklist where each schema block declared in Phase −1 appears as a separately identified check item with its own independent PASS/FAIL condition; a gate that references "all schema sections" or "all §ID blocks" in a single compound condition without enumerating each declared schema as a named line item does not satisfy this criterion; the number of check items must equal the number of schemas declared in Phase −1 — gate completeness is verifiable by counting items, not by reading the compound condition | behavior |

**New in v14:**

| ID | Criterion | Category |
|----|-----------|----------|
| C-46 | **Schema-gate pass-threshold annotation** — the schema-phase gate (satisfying C-45) includes an explicit annotation stating that the gate passes when ALL N items are confirmed (e.g., "Gate-0 passes when all 11 confirmed"), where N equals the total item count derivable from the arithmetic decomposition; an annotation that states item count arithmetic ("8 declared schemas + 3 structural checks = 11 items total") without additionally stating the corresponding gate-pass threshold does not satisfy this criterion; the annotation must name the gate and declare the threshold, not merely enumerate the items — a reader must be able to determine the pass condition from the annotation alone without counting checklist items | behavior |
| C-47 | **Gate-pass condition exhaustive item cross-reference** — the schema-phase gate's PASS/STOP condition line explicitly enumerates all check items by label as a named conjunction, so that reading the condition line alone is sufficient to identify every item that must be satisfied; a condition that states "all items pass", "all N items confirmed", or names only categories or ranges (e.g., "[A1]–[A8]") without naming each item individually does not satisfy this criterion even if C-45 and C-46 pass; the condition must explicitly list all item labels as a compound expression (e.g., `schemas [A1][A2][A3][A4][A5][A6][A7][A8] all present + phase index [B] + constraint index [C] + null annotations [D]`), making the complete pass condition auditable from the condition line without reading the checklist body | behavior |

**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/39 × 10)`
**Golden**: all essential pass + composite ≥ 80 (requires ≥ 2/3 recommended)
**Max**: 100

---

**What C-46 adds over C-45:** C-45 establishes that the schema gate is structured as a per-schema checklist (one item per declared schema). C-46 requires the gate to also include an annotation that explicitly states the gate-pass threshold as a function of that item count. Round 13 showed V-03 passing C-45 with `[A1]–[A8]` per-§ID items and an arithmetic annotation ("8 declared schemas + 3 structural checks = 11 items total") without stating when the gate passes. A checklist with N items but no stated threshold leaves the gate-pass condition implicit — a reader must infer that all items must pass. V-05's annotation ("Gate-0 passes when all 11 confirmed") makes the threshold explicit and links it to the gate label, enabling threshold verification without reading each item.

**What C-47 adds over C-45 and C-46:** C-45 requires per-schema enumeration in the checklist body; C-46 requires the annotation to state the pass threshold. C-47 requires the PASS/STOP condition label itself — the single line an auditor reads to determine gate outcome — to reproduce all item labels as a named conjunction. V-03 satisfies C-45 and the arithmetic-annotation aspect of C-46 but its condition line does not name individual items. V-05's condition (`schemas [A1][A2]...[A8] all present + phase index [B] + constraint index [C] + null annotations [D]`) makes the full pass condition self-contained: an auditor reading only the condition line can enumerate all items that must be satisfied, independent of the checklist body. A condition that passes by counting items rather than naming them cannot detect a renamed or reordered item without re-reading the body.
