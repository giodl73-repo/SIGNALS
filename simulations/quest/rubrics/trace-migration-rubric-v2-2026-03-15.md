Written to `simulations/quest/rubrics/trace-migration-rubric-v2-2026-03-15.md`.

---

**Rubric: trace-migration v2** — 12 criteria across 3 tiers:

**Essential (5, 60 pts)** — unchanged from v1

**Recommended (3, 30 pts)** — unchanged from v1

**Aspirational (4, 20 pts)** — two new criteria added:

- **C-11 Admission-gate vocabulary enforcement** — the output defines an explicit approved-verb list AND a disallowed-phrase list (at least three forbidden generics: "changes," "modified," "updated"). Any entity entry using a disallowed phrase is flagged at admission; rejection is stated not implied. Pass requires: 5+ approved verbs enumerated, 3+ forbidden phrases named, at least one enforcement example shown.

- **C-12 Halt-on-gap escalation protocol** — when any coverage gap is detected, the output includes a named halt block: gap identified → named responsible role → acknowledgment gate before analysis continues. Pass requires: a halt-protocol block exists (even if no gaps fire), it names the gap condition, responsible role, and acknowledgment gate. Flagging-only does not pass.

**Scoring changes:**
- Aspirational: 10 pts → 20 pts (5 pts each × 4 criteria)
- Total: 100 → 110
- Golden threshold: >= 80 → >= 85

**C-09 pass condition tightened:** "at least two cross-entity paths" was implicit before — now explicit that single-entry cascade sections do not pass (this is what separated V-04 PASS from V-01/V-03 PARTIAL).
g., ADD COLUMN, ALTER TYPE, DROP NOT NULL, backfill via UPDATE, reindex). | correctness | essential | Every entity entry contains at least one named migration operation. Generic statements like "column changes" do not pass. |
| C-04 | **Data loss path identification** -- The output explicitly identifies every path where existing data could be destroyed or silently truncated: column drops, type narrowing (e.g., TEXT -> VARCHAR(64)), lossy casts, cascaded deletes, overwrite backfills. | correctness | essential | At least one data loss analysis section exists. If no loss paths exist, the output states that explicitly with reasoning. Silence on this dimension does not pass. |
| C-05 | **Constraint violation identification** -- The output identifies nullable violations (adding NOT NULL to a column with existing NULLs), unique constraint violations (deduplication not handled), and check constraint failures that could cause the migration to fail or silently corrupt rows. | correctness | essential | Every new or tightened constraint is analyzed against the pre-migration data state. Missing constraint analysis does not pass. |

---

## Recommended Criteria (30 pts total — output is meaningfully better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Default value gap analysis** -- For every new NOT NULL column or column with a changed default, the output identifies whether a safe default exists, what value will be written to existing rows during backfill, and whether that value is semantically correct for the domain (Commerce / Finance / Operations context). | depth | recommended | Each new NOT NULL column has an explicit default-value analysis entry. Missing or assumed defaults are flagged. |
| C-07 | **Performance cliff identification** -- The output identifies operations that could cause table scans, lock escalations, or index rebuilds on large tables: full-table UPDATE backfills, DROP INDEX / CREATE INDEX pairs, ALTER COLUMN type changes requiring rewrites, and foreign key constraint additions without concurrent index. | depth | recommended | At least one performance section exists. Each high-risk operation (backfill, reindex, lock) is annotated with a risk level (low / medium / high) and a recommended mitigation (batching, online DDL flag, maintenance window). |
| C-08 | **Reversibility and rollback assessment** -- For each entity change, the output states whether the operation is reversible (e.g., ADD COLUMN is reversible by DROP COLUMN; column rename may require data copy; type narrowing may be irreversible if data was truncated). | behavior | recommended | Each entity entry includes a reversibility verdict (reversible / conditional / irreversible) with a brief rationale. |

---

## Aspirational Criteria (20 pts total — raises the bar)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Cross-entity dependency cascade** -- The output traces second-order effects: foreign key cascades triggered by the migration, views or stored procedures invalidated by column changes, application-layer code assumptions broken by type or nullability changes, downstream ETL or reporting queries affected by renamed or dropped columns. | depth | aspirational | At least two cross-entity or cross-layer dependency paths are traced end-to-end with source -> impact -> mitigation. Single-entry cascade sections do not pass. |
| C-10 | **Quantified risk scoring** -- Each identified issue (data loss path, constraint violation, performance cliff, irreversible operation) is assigned a structured risk entry with: severity (critical / high / medium / low), likelihood (certain / probable / possible), and a recommended remediation action before the migration runs. | format | aspirational | A risk register section exists with at least one entry per identified issue. Each entry has all three fields populated. |
| C-11 | **Admission-gate vocabulary enforcement** -- The output defines an explicit approved-verb list for migration operations AND names at least three disallowed generic phrases (e.g., "changes," "modified," "updated"). Any entity entry using a disallowed phrase is flagged as non-compliant at admission -- rejection is stated, not implied. The disallowed list makes compliance spot-checkable without re-reading the full output. | correctness | aspirational | An approved-verb list exists with at least five named DDL/DML verbs. A disallowed-phrase list exists with at least three named forbidden terms. At least one enforcement example is shown (e.g., "MODIFIED is not an approved verb -- use ALTER TYPE or ALTER COLUMN"). |
| C-12 | **Halt-on-gap escalation protocol** -- When any coverage gap is detected during entity enumeration, constraint analysis, or cascade tracing, the output includes a named halt protocol: gap identified -> named responsible role -> explicit acknowledgment required before analysis continues. The protocol prevents silent omission at the structural level; the analysis does not advance past an unresolved gap. | behavior | aspirational | At least one halt-protocol block is defined (even if no gaps are triggered in the current migration). The block names the gap condition, the responsible role, and the acknowledgment gate. An output that only flags gaps without halting does not pass. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 |
| Recommended | C-06, C-07, C-08 | 30 |
| Aspirational | C-09, C-10, C-11, C-12 | 20 |
| **Total** | | **110** |

**Points per criterion:** Essential = 12 each | Recommended = 10 each | Aspirational = 5 each

**Golden**: all of C-01 through C-05 pass + composite >= 85.

---

## v2 Change Log

| Signal Source | Pattern Observed | New Criterion |
|---------------|-----------------|---------------|
| V-04 C-03 -- "MODIFIED is not an approved verb; approved-verb list is enumerated; compliance is spot-checkable by a reader" | Disallowed-phrase enumeration makes vocabulary enforcement verifiable without re-reading | C-11 |
| V-04 C-01 -- "REGISTRY GAP -- halt protocol forces Operations acknowledgment; domain roles cannot proceed without named-role sign-off" | Gap detection alone is insufficient; halt + named escalation prevents silent omission structurally | C-12 |
| V-04 C-09 -- PASS vs PARTIAL in V-01/V-03 due to DIRECTIVE D-1/D-2 enforcing minimum two traces | Tightened C-09 pass condition: single-entry cascades no longer pass (was implicit; now explicit) | C-09 pass condition updated |
| V-04 general -- "DIRECTIVE-capitalized imperatives; compliance spot-checkable by a reader" | Underlying pattern behind C-11 and C-12; verifiability is an architectural property, not a review step | Informs both C-11 and C-12 |
