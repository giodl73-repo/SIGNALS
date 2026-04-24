Reading the R15 scorecard to extract the two new excellence patterns before writing.

**Two new patterns visible:**

1. **Semantic category grouping in condition line** — V-02 and V-04 use a grouped format (`schemas [A1]...[A8] all present + phase index [B] + constraint index [C] + null annotations [D]`) that satisfies C-47 while adding a second auditing dimension: completeness is verifiable at both the category level and the item level. V-01/V-03/V-05 use flat AND-conjunction (satisfies C-47, no category structure).

2. **Pass/halt co-located in dedicated labeled field** — V-03 and V-04 use `GATE-0 PASS THRESHOLD:` as a single named structural field housing both the pass threshold (C-46) and halt trigger (C-48). V-01/V-02/V-05 distribute threshold and halt across separate inline locations; each satisfies C-46 and C-48 independently but the two-sided specification requires reading across multiple loci.

Those become C-50 and C-51. Aspirational count: 41 → 43. Total: 49 → 51.

---

## Rubric — topic:plan (v16)

**5 essential / 3 recommended / 43 aspirational — 51 criteria total**

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

### Aspirational (C-09 — C-51, 43 total)

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

**New in v15:**

| ID | Criterion | Category |
|----|-----------|----------|
| C-48 | **Schema-gate single-STOP halt declaration** — the schema-phase gate annotation (satisfying C-46) explicitly states that any single STOP result among the checklist items is sufficient to halt the phase (e.g., "one STOP result halts Phase 1", "blocked by any single STOP result"); an annotation that states only the pass condition ("Gate-0 passes when all N confirmed") without declaring the corresponding halt trigger does not satisfy this criterion even if C-46 passes; the halt declaration converts the gate specification from a one-sided pass-threshold statement into a complete pass/halt specification, making the fail behavior explicit rather than requiring a reader to infer it from the pass condition; a gate specification with an implicit fail condition — "all items must pass" implies "any failure stops" but does not state it — does not satisfy this criterion | behavior |
| C-49 | **Condition-line self-containment attestation** — the schema-phase gate PASS/STOP condition line (satisfying C-47) includes an explicit attestation that reading the condition line alone enumerates all required items and that no item may be inferred by range or count (e.g., "reading this condition line enumerates all N items required; no item may be inferred by range"); a condition line that names all items individually (satisfying C-47) but does not explicitly prohibit range inference or attest to its own completeness does not satisfy this criterion; the attestation closes the gap between a condition that happens to enumerate all items and one that declares its own completeness as a structural property — without the attestation, a future edit substituting `[A1]–[A8]` for individual labels would still satisfy C-47's surface requirement (all items appear) while silently degrading the condition's auditing guarantee; the attestation prevents that regression by making completeness a declared invariant of the condition line itself | behavior |

**New in v16:**

| ID | Criterion | Category |
|----|-----------|----------|
| C-50 | **Condition-line semantic category grouping** — the schema-phase gate PASS/STOP condition line (satisfying C-47 and C-49) organizes the individually-named check items into labeled semantic category groups, where each category appears as a named unit and each item within the category retains its individual label (e.g., `schemas [A1][A2][A3][A4][A5][A6][A7][A8] all present + phase index [B] + constraint index [C] + null annotations [D]`); a flat AND-conjunction that lists all items without categorical grouping satisfies C-47 but not this criterion; semantic grouping adds a second auditing dimension to the condition line — a reader can verify completeness both at the category level (are all expected categories present?) and at the item level (are all items within each category present?) — making the condition line resistant to silent item omission as the schema inventory grows, and enabling targeted verification when a specific category is under review without scanning the full conjunction | behavior |
| C-51 | **Pass/halt specification co-location in dedicated labeled field** — the pass-threshold annotation (satisfying C-46) and halt declaration (satisfying C-48) both appear within a single dedicated labeled structural field (e.g., `GATE-0 PASS THRESHOLD: passes when all 11 confirmed; blocked by any single STOP result`) that is independently locatable by field-name scan without reading the checklist body or the condition line; a gate where pass threshold appears in one annotation and halt declaration appears in a separate annotation, condition-line suffix, or body text satisfies C-46 and C-48 independently but does not satisfy this criterion; co-location in a labeled field makes the complete two-sided gate specification — what it takes to pass and what it takes to halt — available from a single structural locus; a reader who finds the field immediately sees both sides of the specification, and a writer who modifies the threshold is immediately adjacent to the halt trigger, making the pass/halt pair structurally indivisible | behavior |

---

**Formula**: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/43 × 10)`
**Golden**: all essential pass + composite ≥ 80 (requires ≥ 2/3 recommended)
**Max**: 100

---

**What C-46 adds over C-45:** C-45 establishes that the schema gate is structured as a per-schema checklist (one item per declared schema). C-46 requires the gate to also include an annotation that explicitly states the gate-pass threshold as a function of that item count. Round 13 showed V-03 passing C-45 with `[A1]–[A8]` per-§ID items and an arithmetic annotation ("8 declared schemas + 3 structural checks = 11 items total") without stating when the gate passes. A checklist with N items but no stated threshold leaves the gate-pass condition implicit — a reader must infer that all items must pass. V-05's annotation ("Gate-0 passes when all 11 confirmed") makes the threshold explicit and links it to the gate label, enabling threshold verification without reading each item.

**What C-47 adds over C-45 and C-46:** C-45 requires per-schema enumeration in the checklist body; C-46 requires the annotation to state the pass threshold. C-47 requires the PASS/STOP condition label itself — the single line an auditor reads to determine gate outcome — to reproduce all item labels as a named conjunction. V-03 satisfies C-45 and the arithmetic-annotation aspect of C-46 but its condition line does not name individual items. V-05's condition (`schemas [A1][A2]...[A8] all present + phase index [B] + constraint index [C] + null annotations [D]`) makes the full pass condition self-contained: an auditor reading only the condition line can enumerate all items that must be satisfied, independent of the checklist body. A condition that passes by counting items rather than naming them cannot detect a renamed or reordered item without re-reading the body.

**What C-48 adds over C-46 and C-47:** C-46 requires the annotation to state the pass threshold; C-47 requires the condition line to name all items. Neither requires the gate to declare what a failure does. Round 14 showed V-02 satisfying both C-46 ("Gate-0 passes when all 11 confirmed") and C-47 (flat AND-conjunction of all 11 labels) while omitting the halt consequence entirely. A gate specification that states only "passes when all N confirmed" is a one-sided specification: the fail path — that any single STOP result halts the phase — must be inferred. V-01/V-03/V-04/V-05's explicit halt declaration ("one STOP result halts Phase 1" / "blocked by any single STOP result") makes the fail behavior a stated property of the gate, not a deduction from the pass condition. C-48 requires that explicit symmetry.

**What C-49 adds over C-47 and C-48:** C-47 requires all item labels to appear individually in the condition line; C-48 requires the halt declaration. Neither prevents a future edit from substituting range notation for individual labels while maintaining surface compliance. V-05 alone adds an explicit attestation within the condition line that the line enumerates all items and that no item may be inferred by range. This attestation is a declared structural invariant: it converts the condition line's completeness from an observable property (all items happen to be listed) into a design rule (all items must be listed; ranges are prohibited). A condition line satisfying C-47 and C-48 but lacking this attestation does not satisfy C-49 — the two properties are independent, because an individually-enumerated condition line can be degraded to a range without violating C-47 until the degradation is noticed.

**What C-50 adds over C-47 and C-49:** C-47 requires all items to be named individually in the condition line; C-49 requires an attestation that the line enumerates everything and prohibits range inference. Both operate on a flat list: items appear as an undifferentiated conjunction. C-50 requires that conjunction to carry semantic category structure — items are grouped by type, each group is labeled, and items within each group are individually identified. R15 showed V-02 and V-04 satisfying C-47 and C-49 with grouped format (`schemas [A1]...[A8] all present + phase index [B] + constraint index [C] + null annotations [D]`), while V-01 and V-05 satisfy the same criteria with flat AND-conjunction. The categorical structure is an orthogonal property: it provides a second verification axis (category completeness + item completeness within category) that a flat list cannot provide. As item counts grow, a flat conjunction can be exhaustive but not scannable by category; a grouped conjunction is both. C-50 requires that two-level structure.

**What C-51 adds over C-46 and C-48:** C-46 requires a pass-threshold annotation; C-48 requires a halt declaration. Both can be satisfied with these two pieces of information distributed across separate structural locations — threshold in an inline annotation adjacent to the item count, halt trigger as a condition-line suffix or body footnote. R15 showed V-03 and V-04 housing both pieces in a single `GATE-0 PASS THRESHOLD:` labeled field, while V-01, V-02, and V-05 satisfy C-46 and C-48 with distributed placement. The labeled-field structure is a co-location property independent of content: a reader who locates the field by name immediately sees both the pass threshold and the halt trigger without scanning the condition line or the checklist header. A writer who modifies the threshold is structurally adjacent to the halt trigger and cannot update one without seeing the other. Distributed placement satisfies C-46 and C-48 independently but does not make the two-sided specification locatable from a single locus — C-51 requires that structural indivisibility.
