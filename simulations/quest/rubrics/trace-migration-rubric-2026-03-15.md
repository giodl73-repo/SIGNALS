Written to `simulations/quest/rubrics/trace-migration-rubric-2026-03-15.md`.

---

**Rubric: trace-migration** — 10 criteria across 3 tiers:

**Essential (5, 60 pts)** — the output is useless without these:
- **C-01** Entity enumeration — every changed entity appears, none silently omitted
- **C-02** Before/after state documentation — each entity has labeled before/after blocks
- **C-03** Migration action tracing — named operations per entity (ADD COLUMN, ALTER TYPE, etc.)
- **C-04** Data loss path identification — explicit analysis of drops, type narrowing, lossy casts, cascades
- **C-05** Constraint violation identification — nullable/unique/check constraint analysis against pre-migration state

**Recommended (3, 30 pts)** — meaningfully better with these:
- **C-06** Default value gap analysis — backfill value correctness for new NOT NULL columns
- **C-07** Performance cliff identification — lock escalations, full-table backfills, reindex costs with risk levels
- **C-08** Reversibility and rollback assessment — per-entity verdict: reversible / conditional / irreversible

**Aspirational (2, 10 pts)** — raises the bar:
- **C-09** Cross-entity dependency cascade — FK cascades, invalidated views, broken ETL queries
- **C-10** Quantified risk scoring — severity + likelihood + remediation for every identified issue
 fields. | correctness | essential | Each entity has a clear "before" block and a clear "after" block. Merged or ambiguous descriptions do not pass. |
| C-03 | **Migration action tracing** -- For each changed entity, the output describes the specific operation the migration performs (e.g., ADD COLUMN, ALTER TYPE, DROP NOT NULL, backfill via UPDATE, reindex). | correctness | essential | Every entity entry contains at least one named migration operation. Generic statements like "column changes" do not pass. |
| C-04 | **Data loss path identification** -- The output explicitly identifies every path where existing data could be destroyed or silently truncated: column drops, type narrowing (e.g., TEXT -> VARCHAR(64)), lossy casts, cascaded deletes, overwrite backfills. | correctness | essential | At least one data loss analysis section exists. If no loss paths exist, the output states that explicitly with reasoning. Silence on this dimension does not pass. |
| C-05 | **Constraint violation identification** -- The output identifies nullable violations (adding NOT NULL to a column with existing NULLs), unique constraint violations (deduplication not handled), and check constraint failures that could cause the migration to fail or silently corrupt rows. | correctness | essential | Every new or tightened constraint is analyzed against the pre-migration data state. Missing constraint analysis does not pass. |

---

## Recommended Criteria (30 pts total -- output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Default value gap analysis** -- For every new NOT NULL column or column with a changed default, the output identifies whether a safe default exists, what value will be written to existing rows during backfill, and whether that value is semantically correct for the domain (Commerce / Finance / Operations context). | depth | recommended | Each new NOT NULL column has an explicit default-value analysis entry. Missing or assumed defaults are flagged. |
| C-07 | **Performance cliff identification** -- The output identifies operations that could cause table scans, lock escalations, or index rebuilds on large tables: full-table UPDATE backfills, DROP INDEX / CREATE INDEX pairs, ALTER COLUMN type changes requiring rewrites, and foreign key constraint additions without concurrent index. | depth | recommended | At least one performance section exists. Each high-risk operation (backfill, reindex, lock) is annotated with a risk level (low / medium / high) and a recommended mitigation (batching, online DDL flag, maintenance window). |
| C-08 | **Reversibility and rollback assessment** -- For each entity change, the output states whether the operation is reversible (e.g., ADD COLUMN is reversible by DROP COLUMN; column rename may require data copy; type narrowing may be irreversible if data was truncated). | behavior | recommended | Each entity entry includes a reversibility verdict (reversible / conditional / irreversible) with a brief rationale. |

---

## Aspirational Criteria (10 pts total -- raise the bar)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Cross-entity dependency cascade** -- The output traces second-order effects: foreign key cascades triggered by the migration, views or stored procedures invalidated by column changes, application-layer code assumptions broken by type or nullability changes, downstream ETL or reporting queries affected by renamed or dropped columns. | depth | aspirational | At least two cross-entity or cross-layer dependency paths are traced end-to-end with source -> impact -> mitigation. |
| C-10 | **Quantified risk scoring** -- Each identified issue (data loss path, constraint violation, performance cliff, irreversible operation) is assigned a structured risk entry with: severity (critical / high / medium / low), likelihood (certain / probable / possible), and a recommended remediation action before the migration runs. | format | aspirational | A risk register section exists with at least one entry per identified issue. Each entry has all three fields populated. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 |
| Recommended | C-06, C-07, C-08 | 30 |
| Aspirational | C-09, C-10 | 10 |
| **Total** | | **100** |

**Golden**: all of C-01 through C-05 pass + composite >= 80.
