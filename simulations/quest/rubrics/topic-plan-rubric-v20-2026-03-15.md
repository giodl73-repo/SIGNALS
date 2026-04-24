Reading the scorecard carefully to extract the R19 excellence signals before writing the updated rubric.

The scorecard surfaces one new formalizable pattern not yet in the rubric:

**Defense basis temporal audit** — V-03 and V-05 replace the binary PRE-REGISTERED / NEWLY-CONSTRUCTED distinction with a three-way temporal legend (PRE-READ / POST-READ / POST-SIGNAL), making the Defense basis column an epistemic audit trail for when each defense was constructed relative to the evaluation stages. Scored at +0.5 partial credit, not yet a named criterion.

That becomes **C-58**. Aspirational count: 49 → 50. Total: 57 → 58.

---

## Rubric — topic:plan (v20)

**5 essential / 3 recommended / 50 aspirational — 58 criteria total**

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

### Aspirational (C-09 — C-58, 50 total)

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

**New in v17:**

| ID | Criterion | Category |
|----|-----------|----------|
| C-52 | **Pass-threshold count derivation arithmetic exposed** — the schema-phase gate pass-threshold annotation (satisfying C-46) makes the item count N derivable by inspection from an explicit arithmetic decomposition of the form `M declared schemas + K structural checks = N items total`, where M equals the number of §ID schema blocks in Phase −1 and K equals the fixed structural check count (e.g., phase index, constraint index, null annotations); an annotation that states "passes when all 11 confirmed" without exposing the derivation satisfies C-46 but not this criterion; exposing the arithmetic links the gate's item count directly to the Phase −1 schema inventory — adding or removing a schema block in Phase −1 immediately surfaces as a numeric inconsistency in the gate annotation, making the schema inventory and the gate item count auditable as a matched pair; a gate whose N is a stated constant rather than a derived value cannot detect schema-inventory divergence without manual recounting | behavior |
| C-53 | **Procedural pre-proposal step declared as named schema block** — the Phase −1 schema inventory includes at least one procedural evaluation step (e.g., §5b pre-proposal evaluation) as a named schema block with its own §ID and a corresponding Gate-0 checklist item, so that the procedural step participates in the cell-exhaustive gate (C-43), the schema-gate checklist atomicity requirement (C-45), the pass-threshold item count (C-46), the condition-line conjunction (C-47), and the halt declaration (C-48); a pre-proposal evaluation step that appears only as an inline instruction within Phase 5 or as an implied prerequisite to proposal writing does not satisfy this criterion even if the gate otherwise passes; declaring the step as a schema block makes it independently auditable, ensures it cannot be silently skipped without Gate-0 detecting the omission, correctly increases the gate's item count and arithmetic derivation (C-52) when added, and participates in the condition-line semantic category group (C-50) as a named item — the procedural step becomes a first-class gate participant, not a body-level reminder | behavior |

**New in v18:**

| ID | Criterion | Category |
|----|-----------|----------|
| C-54 | **Arithmetic decomposition uses typed component labels** — the arithmetic decomposition in the pass-threshold annotation (satisfying C-52) labels each addend with a type descriptor that names the class of items it counts (e.g., "9 declared schemas + 3 structural checks = 12 items total"), such that the M-component and K-component are distinguishable by type without reading the Phase −1 schema inventory; an arithmetic statement that uses positional or type-free counts (e.g., "9 + 3 = 12 items total") provides a derivable N (satisfying C-52) but does not satisfy this criterion; typed labels make the arithmetic a self-describing classification claim — a reader can verify not only that M + K = N but that each component counts the right class of items, enabling detection of classification errors (e.g., a procedural step promoted per C-53 miscounted in K rather than M) without cross-referencing Phase −1; a gate satisfying C-53 but counting the promoted step in K rather than M contradicts C-54 because the type label "declared schemas" for M would be numerically inconsistent with Phase −1's schema block count, surfacing the misclassification as a label-count mismatch rather than a silent arithmetic error | behavior |
| C-55 | **Attestation clause cross-references arithmetic item count** — the attestation clause in the condition line (satisfying C-49) explicitly states the same item count N that the arithmetic decomposition in the pass-threshold annotation (satisfying C-52) derives, creating a numeric cross-reference between the two self-describing claims (e.g., "reading this condition line enumerates all 12 items required; no item may be inferred by range" when C-52's arithmetic yields N=12); an attestation that declares completeness in generic or count-free terms ("enumerates all required items", "no item may be inferred by range") satisfies C-49 but not this criterion; an attestation that names a count differing from C-52's N satisfies neither this criterion nor C-49; naming N in the attestation makes the two specifications mutually verifying — a reader who finds N=12 in the threshold field and "all 12 items" in the attestation can detect a numeric discrepancy (e.g., a schema block added in Phase −1 increments C-52's arithmetic to N=13 but the attestation still reads "all 12 items") as an immediately visible inconsistency between adjacent claims, rather than trusting each field in isolation; the cross-reference converts the attestation from a structural declaration into a consistency checkpoint that fires on any schema-inventory change that updates arithmetic without propagating to the attestation | behavior |

**New in v19:**

| ID | Criterion | Category |
|----|-----------|----------|
| C-56 | **Downstream inertia recurrence as named labeled blocks** — each decision site where inertia recurs after the initial declaration (satisfying C-08) carries an explicit named block label (e.g., "INERTIA-GATE") in its section header, making each recurrence point independently scannable by block label without reading the surrounding protocol; a protocol that restates the inertia option at Steps 4, 4b, and 7 via inline "Recall:" sentences achieves inertia coverage but not structural anchoring — each recurrence is locatable only by reading step bodies, not by label scan; a protocol satisfying this criterion must place the block label in the header, not the body, of each recurrence site, such that a reader performing a label-only scan of the document can enumerate all inertia decision sites and verify their count against the expected recurrence structure without reading any step body | format |
| C-57 | **Per-step analytical purpose declaration** — each protocol step carries an explicit "This step exists so that…" preamble (or equivalent labeled purpose field) that states the analytical function the step performs, converting each step from a procedural instruction into a self-describing analytical unit auditable for purpose-fitness without reading the surrounding protocol; a step whose purpose is implied by its title (e.g., "Step 3: Signal inventory") or derivable from its body content does not satisfy this criterion — the purpose must be explicitly declared in a labeled preamble at the step level, not inferred; the presence of a purpose preamble at every step enables a reader to audit the protocol by comparing stated purposes against actual step content without executing the protocol, surfacing steps whose declared purpose does not match their instructed behavior as an immediately visible inconsistency | behavior |

**New in v20:**

| ID | Criterion | Category |
|----|-----------|----------|
| C-58 | **Defense basis three-way temporal classification** — the Defender Challenge Table's "Defense basis" column carries an explicit three-way temporal legend classifying each entry as PRE-READ (defense existed before strategy.md was read), POST-READ (defense constructed after reading strategy.md but before completing the signal inventory), or POST-SIGNAL (defense constructed after the full signal inventory was complete); a table that uses only a binary classification ("pre-registered" / "newly constructed", or "D-ID" / "newly constructed") satisfies the baseline Defense basis requirement but not this criterion; the three-way legend converts the Defense basis column from a provenance tag into an epistemic audit trail — PRE-READ defenses are least influenced by the current evaluation's signals, POST-SIGNAL defenses are most influenced, and the classification makes that ordering independently verifiable from the table without reading external documentation; the legend must appear as a named header annotation or key block adjacent to the table, and each Defense basis cell must carry one of the three labeled values — a table that introduces temporal language in row cells without a corresponding legend definition does not satisfy this criterion because legend completeness is independently verifiable only by matching legend entries against the distinct values present in the Defense basis column | behavior |
