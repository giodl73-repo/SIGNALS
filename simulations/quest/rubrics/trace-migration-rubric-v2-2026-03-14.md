Rubric v2 written. Here's what changed:

---

## v2 Summary

**3 new aspirational criteria** from Round 1 excellence patterns:

| C-NN | Name | Source Pattern |
|------|------|----------------|
| C-11 | **Locked Execution Sequence as Named Artifact** | Numbered table established once in section 1; downstream sections reference by step number rather than re-describing. More reliable than embedded ordering instructions. |
| C-12 | **Domain Section Pre-Positioned Before Verification** | Domain impact appears between EXECUTE and VERIFY — not last or second-to-last. Deferral is indistinguishable from omission, so position is the check. |
| C-13 | **Silence-is-Failure Completeness Enforcement** | Critical fields (data loss, NOT NULL risk, rollback viability) use YES/NO/PARTIAL or checkbox — structurally detectable absence. Applies only to the three named field types. |

**Scoring changes:**
- Aspirational tier: 10 pts (2 criteria) → 25 pts (5 criteria)
- Total max: 100 → 115
- Golden threshold: unchanged at 80% composite + all essential pass

**One new evaluator note added for C-05:** question-driven formats (Q1=steps, Q2=state...) fail C-05 structurally even if Q1 lists steps correctly — formalizing the V-04 finding so future evaluators don't have to rediscover it.
 does not, it names which records violate it and what the migration does about it (fail, skip, backfill). |
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

## Aspirational Criteria (25 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Zero-Downtime Viability** | depth | aspirational | The output assesses whether the migration can be run without downtime using an expand/contract pattern or online DDL, and -- if not -- names the specific step that requires a maintenance window and why. |
| C-10 | **Idempotency Check** | coverage | aspirational | The output evaluates whether each migration step is safe to run twice (idempotent). Any step that would corrupt data or fail on re-run is flagged with the specific failure mode (e.g., duplicate key error, double-applied data transform). |
| C-11 | **Locked Execution Sequence as Named Artifact** | structure | aspirational | The execution order is established once -- as a numbered table or explicitly labeled list -- in the first substantive section. At least two subsequent sections reference steps by those assigned numbers rather than re-describing them. This prevents reordering or regrouping in downstream analysis sections. |
| C-12 | **Domain Section Pre-Positioned Before Verification** | structure | aspirational | The domain/business impact section appears before any summary, verification, or recommendations section -- not deferred to the end. A domain section placed last or second-to-last fails this criterion, because deferral is indistinguishable from omission in practice. |
| C-13 | **Silence-is-Failure Completeness Enforcement** | structure | aspirational | Critical fields (data loss statement, NOT NULL risk flag, rollback viability per step) use binary or enumerated choices -- YES/NO/PARTIAL, checkbox, or a fixed taxonomy -- such that the absence of a choice is structurally detectable. Free-form omittable fields for these critical fields do not satisfy this criterion. |

---

## Scoring Summary

| Tier | Max Points | Criteria Count |
|------|-----------|----------------|
| Essential | 60 | 5 (C-01 to C-05) |
| Recommended | 30 | 3 (C-06 to C-08) |
| Aspirational | 25 | 5 (C-09 to C-13) |
| **Total** | **115** | **13** |

**Golden**: All of C-01 through C-05 pass AND composite >= 80%.

---

## Evaluator Notes

- **C-02 explicit negative**: If the migration genuinely has no data loss paths, the output must say so with a brief argument -- silence is not a pass.
- **C-03 scope**: Focus on constraint *changes*, not constraints that exist unchanged before and after.
- **C-05 structural conflict**: Question-driven formats (Q1=steps, Q2=state, Q3=data loss...) that organize output by analytical concern rather than execution sequence fail C-05 even if Q1 lists steps correctly -- the reader cannot follow migration state forward in time across later questions.
- **C-06 threshold**: Performance cliff detection only applies if the migration touches tables with non-trivial row counts (>10k rows implied or stated). If the schema is empty/new, C-06 auto-passes with a note.
- **C-08 domain lens**: A passing answer names a concrete business object (order, invoice, ledger entry, shipment) -- generic database terminology alone does not satisfy this criterion.
- **C-11 reference depth**: A section that says "see step 3 above" satisfies the reference requirement; a section that re-describes "the column rename step" without a number does not.
- **C-12 placement test**: Count sections from the end. If the domain section is the last or second-to-last section, it fails. It must have at least one non-trivial section (verification, summary, recommendations) after it.
- **C-13 critical fields only**: This criterion applies only to the three named field types (data loss, NOT NULL risk, rollback viability). Free-form prose is acceptable for non-critical fields such as performance notes or idempotency commentary.

---

## v2 Change Log

Three new aspirational criteria added from Round 1 excellence patterns:

| Pattern (from scorecard) | Criterion Added |
|--------------------------|----------------|
| Pre-position domain section between EXECUTE and VERIFY to prevent deferral -- model cannot skip it before closing | C-12: Domain Section Pre-Positioned Before Verification |
| Locked execution sequence as a named artifact that downstream sections reference by step number -- more reliable than embedded ordering instructions | C-11: Locked Execution Sequence as Named Artifact |
| Role-responsibility mechanism achieves structural equivalence to pre-printed columns when scope is explicit and closed with a silence-is-failure instruction | C-13: Silence-is-Failure Completeness Enforcement |

Aspirational tier expanded from 10 pts (2 criteria) to 25 pts (5 criteria). Total max increased from 100 to 115. Golden threshold unchanged at 80% composite with all essential passing.
