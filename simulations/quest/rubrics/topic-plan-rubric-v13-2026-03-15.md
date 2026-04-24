Here is the complete updated rubric:

---

## Rubric — topic:plan (v13)

**5 essential / 3 recommended / 37 aspirational — 45 criteria total**

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

### Aspirational (C-09 — C-45, 37 total)

*(C-09 through C-42 unchanged from v12)*

**New in v13:**

| ID | Criterion | Category |
|----|-----------|----------|
| C-43 | **Cell-exhaustive gate enumeration** — each in-phase stop gate enumerates every mandatory column by name in its pass condition, requiring each named column to be non-null before the phase may advance; a gate whose pass condition checks only row count, block count, or structural presence without naming each mandatory column individually does not satisfy this criterion even if C-12 passes; a gate that fires when "all rows are present" but does not verify "all cells in mandatory columns are filled" is a structural presence gate, not a cell-exhaustive gate | behavior |
| C-44 | **Numbered Gate-0 label in block header** — the pre-signal stop gate (satisfying C-26) carries the explicit label "Gate-0" (or equivalent numbered identifier, e.g., "Gate-(-1)", "Gate-S") in its block section header, making it independently scannable as the first link in the numbered sequential gate chain without reading the gate body; a pre-signal gate that uses only a descriptive name (e.g., "CONTRACT COMPLETENESS GATE") without a numbered gate identifier in the header does not satisfy this criterion even if C-26 passes and the gate fires at the correct site; the numbered label is a header-level scannable property, not a body-level description | format |
| C-45 | **Schema-gate checklist atomicity** — the schema-phase gate (satisfying C-38) is structured as an explicitly numbered or labeled checklist where each schema block declared in Phase −1 appears as a separately identified check item with its own independent PASS/FAIL condition; a gate that references "all schema sections" or "all §ID blocks" in a single compound condition without enumerating each declared schema as a named line item does not satisfy this criterion; the number of check items must equal the number of schemas declared in Phase −1 — gate completeness is verifiable by counting items, not by reading the compound condition | behavior |

**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/37 × 10)`
**Golden**: all essential pass + composite ≥ 80 (requires ≥ 2/3 recommended)
**Max**: 100

---

**What C-43 adds over C-12:** C-12 establishes that a stop gate *exists* with cell-fill intent. C-43 requires the gate's pass condition to *name each mandatory column individually*. Round 12 showed all variations had gate language but gated on row/block presence ("all 9 namespace rows present; no namespace omitted") — a gate can satisfy C-12's wording while passing when mandatory cells are blank. C-43 closes that gap.

**What C-44 adds over C-26:** C-26 tests that the pre-signal gate blocks artifact reads *structurally*. C-44 tests that the numbered label "Gate-0" appears in the *section header*, making it scannable without reading the gate body. Round 12 showed V-01 and V-05 satisfying C-26 via "CONTRACT COMPLETENESS GATE" but failing to carry a numbered identifier — the gate cannot be found by scanning headers for "Gate-0" or confirmed as chain-position-0 without reading content.

**What C-45 adds over C-38:** C-38 tests that the schema-phase gate exists in the numbered sequential chain. C-45 tests that it is structured as a *per-schema checklist* — one item per declared schema, each with its own PASS/FAIL — rather than a compound single condition. Passing variations in Round 12 (V-01, V-05) achieved C-38 via a four-item checklist ([A][B][C][D]) where each item corresponded to a specific schema. A compound gate satisfies C-38 but cannot be audited by item count; a missing schema produces a silently incomplete compound condition rather than a detectable missing check item.

---

File written to `simulations/quest/golden/quest-rubric-variate-v13-R12-2026-03-15.md`.
