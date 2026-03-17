Here is the complete rubric v4:

---

# trace-migration Rubric — v4

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Before/After State** | correctness | essential | For each changed entity (table, column, constraint, index), the output explicitly shows the state before the migration and the state after. "Changed" includes additions, removals, type changes, nullability changes, and constraint changes. An entity described in generic terms without before/after values does not satisfy this criterion. |
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

## Aspirational Criteria (50 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Zero-Downtime Viability** | depth | aspirational | The output assesses whether the migration can be run without downtime using an expand/contract pattern or online DDL, and -- if not -- names the specific step that requires a maintenance window and why. |
| C-10 | **Idempotency Check** | coverage | aspirational | The output evaluates whether each migration step is safe to run twice (idempotent). Any step that would corrupt data or fail on re-run is flagged with the specific failure mode (e.g., duplicate key error, double-applied data transform). |
| C-11 | **Locked Execution Sequence as Named Artifact** | structure | aspirational | The execution order is established once -- as a numbered table or explicitly labeled list -- in the first substantive section. At least two subsequent sections reference steps by those assigned numbers rather than re-describing them. This prevents reordering or regrouping in downstream analysis sections. |
| C-12 | **Domain Section Pre-Positioned Before Verification** | structure | aspirational | The domain/business impact section appears before any summary, verification, or recommendations section -- not deferred to the end. A domain section placed last or second-to-last fails this criterion, because deferral is indistinguishable from omission in practice. |
| C-13 | **Silence-is-Failure Completeness Enforcement** | structure | aspirational | Critical fields (data loss statement, NOT NULL risk flag, rollback viability per step) use binary or enumerated choices -- YES/NO/PARTIAL, checkbox, or a fixed taxonomy -- such that the absence of a choice is structurally detectable. Free-form omittable fields for these critical fields do not satisfy this criterion. |
| C-14 | **Critical Field Type Annotation** | structure | aspirational | At least the three critical fields (data loss statement, NOT NULL risk, rollback viability) carry an explicit type annotation -- e.g., "(BINARY FIELD)", "(BINARY)", "(fixed taxonomy)" -- at every point of definition: section headers, column names, or inline field labels. The annotation names the structural class of the expected value, making non-conformant free-form prose a visible type mismatch rather than an implicit omission. A critical field label without a type annotation does not satisfy this criterion. |
| C-15 | **Forward-Progress Gate with Binary State** | structure | aspirational | At least one dependency gate uses an explicit binary state (e.g., OPEN/BLOCKED, PASS/FAIL) that must be resolved before a downstream phase can proceed. The downstream phase's header or instruction explicitly names the gate state as a prerequisite -- e.g., "VERIFY PHASE: domain gate must be OPEN before writing verify checks." A section that is merely positioned before another section without a resolvable binary state does not satisfy this criterion. |
| C-16 | **Two-Phase Analytical Decoupling** | structure | aspirational | The output explicitly separates an interrogative phase (Phase A) that organizes analytical work by concern, entity, or risk type from a canonical synthesis phase (Phase B) that produces a mandatory step-ordered artifact. Phase B must be labeled as the authoritative output. This decouples analytical depth from chronological output obligation: Phase A can interrogate freely without violating C-05, which is satisfied by Phase B alone. |
| **C-17** | **Gate Field Annotation Compound** | structure | aspirational | At least one C-15 gate state field carries a C-14-style explicit type annotation at its definition site -- e.g., "DOMAIN GATE (BINARY FIELD): OPEN / BLOCKED" or "GATE STATE (BINARY FIELD): OPEN / BLOCKED." This applies C-14 and C-15 enforcement simultaneously at the same field: a non-conformant value triggers both a type mismatch (C-14) and an unresolved phase block (C-15). An output that satisfies C-14 and C-15 independently but leaves gate state fields without type annotations does not satisfy this criterion. |
| **C-18** | **Named Artifact Citation** | structure | aspirational | Citation instructions that require step-number references must name the specific source artifact -- e.g., "Step N from Q1," "step number from SECTION 0 registry," or "step number from PARSE PHASE." The source-artifact suffix prevents implicit re-numbering by anchoring citations to a named location rather than a generic ordinal. In two-phase structures, this instruction must appear in Phase A question text. In single-phase structures, it must appear in at least one analytical section instruction. A citation instruction that says only "reference by step number" or "cite by Step N" without naming the source artifact does not satisfy this criterion. |

---

## Scoring Summary

| Tier | Max Points | Criteria Count |
|------|-----------|----------------|
| Essential | 60 | 5 (C-01 to C-05) |
| Recommended | 30 | 3 (C-06 to C-08) |
| Aspirational | 50 | 10 (C-09 to C-18) |
| **Total** | **140** | **18** |

**Golden**: All of C-01 through C-05 pass AND composite >= 80% (112 pts).

---

## Evaluator Notes

*(all v3 notes carried forward, two new notes added)*

- **C-02 explicit negative**: If the migration genuinely has no data loss paths, the output must say so with a brief argument -- silence is not a pass.
- **C-03 scope**: Focus on constraint *changes*, not constraints that exist unchanged before and after.
- **C-05 structural conflict**: Single-phase question-driven formats (Q1=steps, Q2=state, Q3=data loss...) that organize output by analytical concern rather than execution sequence fail C-05 even if Q1 lists steps correctly.
- **C-05 two-phase exception**: Phase B, explicitly labeled as the canonical artifact and strictly ordered by execution sequence, satisfies C-05. The single-phase structural conflict applies only to single-phase outputs.
- **C-06 threshold**: C-06 auto-passes with a note if the schema is empty/new.
- **C-08 domain lens**: Concrete business object required (order, invoice, ledger entry, shipment) -- generic database terminology alone does not satisfy this criterion.
- **C-11 reference depth**: "see step 3 above" satisfies; "the column rename step" without a number does not.
- **C-11 two-phase gap**: Phase A questions do not inherit step-number citation from Phase B tables. Citation must be explicitly stated in Phase A question text.
- **C-12 placement test**: Domain section must have at least one non-trivial section (verification, summary, recommendations) after it.
- **C-13 critical fields only**: Applies only to data loss, NOT NULL risk, and rollback viability fields.
- **C-14 vs C-13**: C-13 requires binary/enumerated values; C-14 requires the type label at the definition site. Not redundant.
- **C-15 vs C-12**: C-12 tests positional placement; C-15 tests whether a resolvable binary state blocks the next phase. Not redundant.
- **C-16 and C-11**: Two-phase structure satisfies C-05 but does not automatically satisfy C-11 in Phase A. Evaluate both phases independently.
- **C-17 vs C-14 + C-15** *(new)*: C-17 only fires at the intersection -- both C-14 and C-15 must be applied to the same gate state field. Satisfying each criterion independently in separate places is not sufficient.
- **C-18 vs C-11** *(new)*: C-11 requires step-number citation; C-18 requires the source artifact name in the citation instruction. Labeling the registry "(AUTHORITATIVE ARTIFACT)" at the registry site does not substitute for naming the source in downstream citation instructions.

---

## v4 Change Log

Two new aspirational criteria added from Round 3 excellence patterns:

| Pattern (from scorecard) | Criterion Added |
|--------------------------|----------------|
| Applying C-14 type annotation to C-15 gate state fields creates double enforcement at phase transitions: type mismatch AND phase block simultaneously at the same field. Neither criterion alone requires this intersection -- it emerges from synthesis. (V-04, V-05 positive cases.) | C-17: Gate Field Annotation Compound |
| "from Q1" suffix in citation instructions names the authoritative source artifact rather than requiring generic step numbers. Prevents implicit re-numbering by anchoring citations to a specific named section. V-01/V-02/V-03/V-05 pass; V-04 ("cite by number" without source name) fails. | C-18: Named Artifact Citation |

**Scoring changes:**
- Aspirational tier: 40 pts (8 criteria) -> 50 pts (10 criteria)
- Total max: 130 -> 140
- Golden threshold: unchanged at 80% composite (now 112 pts) + all essential pass

---

**What v4 predicts for a Round 4 V-05 equivalent:** A variation implementing C-17 + C-18 alongside all 16 prior criteria would score 140/140. C-17 requires annotated gate fields (only V-04 and V-05 had this). C-18 requires named-artifact citation (V-01, V-02, V-03, V-05 had this; V-04 did not). A full-synthesis variation combining both patterns plus all prior criteria closes the last two rationalization paths that v3 left open.
 just generic step numbers. An output can pass C-11 ("cite by step number" repeated in downstream sections) without passing C-18 if no source artifact is named. Labeling the registry as "(AUTHORITATIVE ARTIFACT)" at the registry site does not substitute for naming the source in the citation instruction at downstream analytical sections.

---

## v4 Change Log

Two new aspirational criteria added from Round 3 excellence patterns:

| Pattern (from scorecard) | Criterion Added |
|--------------------------|----------------|
| Applying C-14 type annotation to C-15 gate state fields creates double enforcement at phase transitions: type mismatch AND phase block simultaneously at the same field. Neither criterion alone requires this intersection -- it emerges from synthesis. (V-04, V-05 positive cases; V-01 fails because no gates, V-02 fails because no annotations, V-03 fails because no gates.) | C-17: Gate Field Annotation Compound |
| "from Q1" suffix in citation instructions names the authoritative source artifact rather than requiring generic step numbers. Prevents implicit re-numbering by anchoring citations to a specific named section. V-01 ("from SECTION 0"), V-02 ("from PARSE"), V-03/V-05 ("from Q1") pass; V-04 ("cite by number" without source name) fails. | C-18: Named Artifact Citation |

**Scoring changes:**
- Aspirational tier: 40 pts (8 criteria) -> 50 pts (10 criteria)
- Total max: 130 -> 140
- Golden threshold: unchanged at 80% composite (now 112 pts) + all essential pass

**Two new evaluator notes added:**
- **C-17 vs C-14 + C-15**: Both constituent criteria must fire at the same gate state field site -- satisfying each independently in separate fields is not sufficient.
- **C-18 vs C-11**: Source artifact name must appear in the downstream citation instruction itself, not only at the registry definition site.
