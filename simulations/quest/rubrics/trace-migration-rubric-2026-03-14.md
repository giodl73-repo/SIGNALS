Rubric written to `simulations/quest/rubrics/trace-migration-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

**Essential (C-01–C-05)** — the trace is not useful without these:
- C-01: Before/after state explicitly shown per changed entity
- C-02: Data loss paths named, or explicit "none found" with reasoning
- C-03: Constraint violations assessed — does existing data satisfy new constraints?
- C-04: NOT NULL + no DEFAULT on non-empty table flagged as risk
- C-05: Steps presented in chronological execution order

**Recommended (C-06–C-08)** — raise quality:
- C-06: Performance cliffs identified (lock duration, full-table rewrites, index rebuilds)
- C-07: Each destructive step classified as fully reversible / backup-only / irreversible
- C-08: Domain framing in Commerce/Finance/Operations terms (orders, invoices, ledger entries)

**Aspirational (C-09–C-10)** — bar-raising:
- C-09: Zero-downtime viability via expand/contract or online DDL
- C-10: Idempotency check — safe to run twice?
 old and new types/values/nullability fail. |
| C-02 | **Data Loss Path Identification** | correctness | essential | The output identifies at least one concrete data loss path if one exists, OR explicitly states "no data loss paths found" with reasoning. A data loss path is any migration step that can silently drop rows, truncate values, or discard columns without surfacing an error. |
| C-03 | **Constraint Violation Analysis** | correctness | essential | For each constraint change (NOT NULL, UNIQUE, FK, CHECK), the output identifies whether existing data satisfies the new constraint. If it does not, it names which records violate it and what the migration does about it (fail, skip, backfill). |
| C-04 | **Missing Default Value Detection** | correctness | essential | For any new NOT NULL column added to an existing table, the output checks whether a DEFAULT is provided. If no DEFAULT is present on a non-empty table, this is flagged as a migration risk. |
| C-05 | **Chronological Step Ordering** | format | essential | Migration steps are presented in execution order. The trace follows the actual sequence a database engine would apply them -- not alphabetical by table, not grouped by type. The reader can follow the migration state forward in time. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Performance Cliff Detection** | depth | recommended | The output identifies at least one operation likely to cause a performance cliff on large tables (e.g., full-table rewrite, index rebuild on wide table, type cast requiring row scan). For each, it names the table, estimated row count if knowable, and the specific risk (lock duration, I/O spike, replication lag). |
| C-07 | **Rollback Viability Assessment** | depth | recommended | For each destructive step (DROP COLUMN, DROP TABLE, type narrowing, data truncation), the output assesses whether the step is reversible: (a) fully reversible with down migration, (b) reversible only from backup, or (c) irreversible. At least one step is classified. |
| C-08 | **Domain Expert Framing** | behavior | recommended | The output applies at least one Commerce, Finance, or Operations lens. This means naming a real-world consequence of the migration risk in domain terms -- e.g., "a truncated amount column could silently zero-out refunds over $10k" not just "decimal precision is reduced." |

---

## Aspirational Criteria (10 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Zero-Downtime Viability** | depth | aspirational | The output assesses whether the migration can be run without downtime using an expand/contract pattern or online DDL, and -- if not -- names the specific step that requires a maintenance window and why. |
| C-10 | **Idempotency Check** | coverage | aspirational | The output evaluates whether each migration step is safe to run twice (idempotent). Any step that would corrupt data or fail on re-run is flagged with the specific failure mode (e.g., duplicate key error, double-applied data transform). |

---

## Scoring Summary

| Tier | Max Points | Criteria Count |
|------|-----------|----------------|
| Essential | 60 | 5 (C-01 to C-05) |
| Recommended | 30 | 3 (C-06 to C-08) |
| Aspirational | 10 | 2 (C-09 to C-10) |
| **Total** | **100** | **10** |

**Golden**: All of C-01 through C-05 pass AND composite >= 80.

---

## Evaluator Notes

- **C-02 explicit negative**: If the migration genuinely has no data loss paths, the output must say so with a brief argument -- silence is not a pass.
- **C-03 scope**: Focus on constraint *changes*, not constraints that exist unchanged before and after.
- **C-06 threshold**: Performance cliff detection only applies if the migration touches tables with non-trivial row counts (>10k rows implied or stated). If the schema is empty/new, C-06 auto-passes with a note.
- **C-08 domain lens**: A passing answer names a concrete business object (order, invoice, ledger entry, shipment) -- generic database terminology alone does not satisfy this criterion.
