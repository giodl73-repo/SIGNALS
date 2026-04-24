Saved to `simulations/quest/golden/trace-migration-variate-R1-2026-03-15.md`. Here is the output:

---

# trace-migration Variate — Round 1
**Date:** 2026-03-15
**Rubric:** v1 (C-01 through C-10, new rubric)
**Target criteria:** C-01 (entity enumeration), C-02 (before/after state documentation), C-03 (migration action tracing), C-04 (data loss path identification), C-05 (constraint violation identification)

---

## Round 1 Variation Map

| Variation | Axis | C-01 | C-02 | C-03 | C-04 | C-05 | Notes |
|-----------|------|------|------|------|------|------|-------|
| V-01 | Role sequence | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Operations-first substrate declaration locks entity enumeration before domain roles apply domain filters; all five essentials addressed structurally |
| V-02 | Output format | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Table-first entity registry anchors C-01; BEFORE/AFTER columns enforce C-02; OPERATION column enforces C-03; dedicated DATA LOSS and CONSTRAINT columns enforce C-04/C-05 |
| V-03 | Lifecycle emphasis | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Explicit phase gates with coverage floors prevent silent omission; each phase must close before the next opens |
| V-04 | Role sequence + Phrasing register | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Expected PASS | DIRECTIVE imperatives per role close the domain-filter omission path; approved-verb list eliminates hedged operation descriptions |
| V-05 | Role sequence + Output format + Lifecycle emphasis | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Expected PASS | Three-layer completeness: registry table + phase gate + Operations-first substrate; any entity surviving one omission mechanism is caught by another; inertia frame added as structural bookend |

---

## Design Notes

**Single-axis variations (V-01, V-02, V-03):**

- **V-01 (Role sequence):** Operations runs before Finance and Commerce. Operations produces the entity registry as a locked contract — no entity may appear in domain-role analysis unless it was first registered here. Finance and Commerce are required to flag registry gaps rather than silently skip entities they can't place. This is the core insight: domain experts narrow their view; infrastructure experts see the whole schema.

- **V-02 (Output format):** Nine structured tables replace prose. C-01 is enforced by TABLE 1 (ENTITY REGISTRY) — an empty row is visually obvious in a table; a missing prose section is not. C-02 is enforced by TABLE 2 (BEFORE STATE) and TABLE 4 (AFTER STATE) as separate tables, making merge impossible. C-03 is enforced by the OPERATION column in TABLE 3, which accepts only named DDL/DML verbs. C-04 and C-05 are separate tables (5 and 6), each with their own per-entity rows.

- **V-03 (Lifecycle emphasis):** Five sequential phases with named gates — INVENTORY → BEFORE STATE → MIGRATION ACTIONS → AFTER STATE + RISK → SYNTHESIS. Each phase has a coverage floor and a gate statement before the next phase opens. A migration's four temporal states (before / operation / after / consequence) are enforced as phases rather than allowed to blur together in a single analytical pass.

**Combination variations (V-04, V-05):**

- **V-04 (Role sequence + Phrasing register):** Operations-first sequencing from V-01, combined with DIRECTIVE-capitalized imperatives that name failure modes explicitly: "MODIFIED is not an approved verb," "do not omit entities because they have no domain owner," "REGISTRY GAP — halt until Operations registers this entity." The DIRECTIVE language makes compliance checkable by a reader who can verify each directive was followed.

- **V-05 (Role sequence + Output format + Lifecycle emphasis):** Full combination. Adds an **inertia frame** as a structural bookend — opened before INVENTORY PHASE 1, closed after PHASE 5 risk synthesis — which requires the analyst to compare each identified risk against the ongoing cost of inaction. The five-phase gate structure from V-03, the nine-table format from V-02, and the Operations-first role ordering from V-01 all operate simultaneously. The closing frame produces a migration recommendation per dimension (data integrity / operations / downstream) with CONDITIONAL meaning "recommended only if specific named remediations are completed first."

---

**Rubric coverage analysis:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Entity enumeration | ENTITY REGISTRY as locked contract | TABLE 1 structural anchor | INVENTORY phase gate | DIRECTIVE A-1 + registry gap protocol | TABLE 1 + PHASE 1 gate + Operations substrate |
| C-02 Before/after state | FIELD 1 / FIELD 3 per entity | TABLE 2 / TABLE 4 as separate tables | PHASE 2 / PHASE 3 separate phases | FIELD 1 / FIELD 3 with DIRECTIVE language | TABLE 2 / TABLE 4 + PHASE 2/3 gates |
| C-03 Migration action tracing | FIELD 2 approved-verb list | TABLE 3 OPERATION column | TABLE 3 in PHASE 2 | FIELD 2 DIRECTIVE with approved list | TABLE 3 + PHASE 2 gate |
| C-04 Data loss paths | FIELD 4 per entity, silence prohibited | TABLE 3 dedicated section | TABLE 5 in PHASE 4 | FIELD 4 DIRECTIVE, silence clause explicit | TABLE 5 + PHASE 4 gate |
| C-05 Constraint violations | FIELD 5 per entity | TABLE 4 dedicated section | TABLE 6 in PHASE 4 | FIELD 5 DIRECTIVE with violation types | TABLE 6 + PHASE 4 gate |
| C-06 Default value gap | DEFAULT VALUE ANALYSIS field | TABLE 5 | TABLE 7 in PHASE 4 | DIRECTIVE per field | TABLE 7 + PHASE 4 gate |
| C-07 Performance cliff | PERFORMANCE CLIFF field | TABLE 6 | TABLE 8 in PHASE 4 | PERFORMANCE summary per role | TABLE 8 + PHASE 4 gate |
| C-08 Reversibility | REVERSIBILITY VERDICT field | TABLE 7 | TABLE 9 in PHASE 4 | REVERSIBILITY in summary | TABLE 9 + PHASE 4 gate |
| C-09 Cross-entity cascade | Dedicated cascade section | TABLE 8 | TABLE 10 in PHASE 5 | DIRECTIVE D-1/D-2 minimum two traces | TABLE 10 + PHASE 5 gate |
| C-10 Quantified risk scoring | RISK REGISTER with severity+likelihood+remediation | TABLE 9 | TABLE 11 in PHASE 5 | DIRECTIVE E-1/E-2, CRITICAL enforcement | TABLE 11 + inertia frame close |
