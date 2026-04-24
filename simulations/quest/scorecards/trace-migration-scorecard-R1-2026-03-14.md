Scorecard written to `simulations/quest/scorecards/trace-migration-scorecard-R1-2026-03-14.md`.

---

## Round 1 Results — trace-migration

**4 of 5 variations reach Golden.** Ranking: V-01 = V-02 = V-03 = V-05 (100) > V-04 (92)

| Variation | C-05 | Total | Golden |
|-----------|------|-------|--------|
| V-01 Role sequence | PASS | **100** | YES |
| V-02 Table-heavy | PASS | **100** | YES |
| V-03 Phase gates | PASS | **100** | YES |
| V-04 Investigative | **PARTIAL (6)** | **92** | NO |
| V-05 Full synthesis | PASS | **100** | YES |

**Only failure:** V-04's question-driven structure organizes output by analytical concern (Q1=steps, Q2=state, Q3=data loss…), not execution sequence — the reader cannot follow migration state forward in time across Q2–Q10. Structural conflict with C-05 is intrinsic to the format.

**What trace-migration has that scout/prove skills don't:** All criteria already have structural homes in every well-designed variation. The rubric is tighter (10 criteria with specific before/after, explicit negative, chronological order) but the variation designs were comprehensive enough to satisfy all of them.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-position domain section between EXECUTE and VERIFY to prevent deferral -- model cannot skip it before closing", "locked execution sequence as a named artifact that downstream sections reference by step number -- more reliable than embedded ordering instructions", "role-responsibility mechanism achieves structural equivalence to pre-printed columns when scope is explicit and closed with a silence-is-failure instruction"]}
```
-|----------|
| C-01 | PASS | 12/12 | Step 2 Entity State Changes table: Before/After type, nullable, default -- one row per changed entity |
| C-02 | PASS | 12/12 | DATA LOSS STATEMENT checkbox; exactly one must be checked; silence structurally impossible |
| C-03 | PASS | 12/12 | Step 3 Risk Matrix: Constraint Change, Existing Data Satisfies, Migration Handles Violation As |
| C-04 | PASS | 12/12 | Step 3 Risk Matrix: NOT NULL Added, DEFAULT Provided, NOT NULL Risk FLAG/CLEAR -- pre-printed, cannot skip |
| C-05 | PASS | 12/12 | Step 1 Execution Order table; "Do not reorder or group by type" |
| C-06 | PASS | 10/10 | Step 4 Operational Risk table: Full-Table Rewrite, Index Rebuild, Performance Cliff, Row Count |
| C-07 | PASS | 10/10 | Step 5 Rollback Viability table: REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE per destructive step |
| C-08 | PASS | 10/10 | Step 6 Domain Impact table; VERDICT unconditionally requires highest-severity business risk sentence |
| C-09 | PASS |  5/5  | Step 7: Can migrate without downtime YES/NO/PARTIAL with alternative pattern field |
| C-10 | PASS |  5/5  | Step 7 Idempotency table: Failure Mode on Re-Run per non-idempotent step |

**V-02 Total: 100/100 -- GOLDEN**

---

## V-03: Lifecycle Emphasis -- Explicit Phase Gates

| ID | Result | Score | Evidence |
|----|--------|-------|----------|
| C-01 | PASS | 12/12 | PRE-FLIGHT before-state snapshot per entity + EXECUTE per-step after-state fields |
| C-02 | PASS | 12/12 | EXECUTE SUMMARY: YES/NO with per-step reasoning required for NO |
| C-03 | PASS | 12/12 | EXECUTE SUMMARY: name violating records and migration handling per new constraint |
| C-04 | PASS | 12/12 | PRE-FLIGHT NOT NULL + DEFAULT check: RISK format with row count per column |
| C-05 | PASS | 12/12 | Strongest enforcer: PHASE 0 PARSE authoritative; "Steps may not be grouped by type or table" |
| C-06 | PASS | 10/10 | EXECUTE: per-step Performance cliff NONE/PRESENT with lock, rewrite scope, row count |
| C-07 | PASS | 10/10 | ROLLBACK PHASE: per-step REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE with down-migration DDL |
| C-08 | PASS | 10/10 | EXECUTE: per-step mandatory Domain note; "N/A only if no business data touches this column -- explain why" |
| C-09 | PASS |  5/5  | ZERO-DOWNTIME section: Viable YES/NO/PARTIAL with blocking step and engine-specific alternative |
| C-10 | PASS |  5/5  | Same section: Non-idempotent steps with failure mode per step |

**V-03 Total: 100/100 -- GOLDEN**

---

## V-04: Phrasing Register -- Investigative/Conversational

| ID | Result | Score | Evidence |
|----|--------|-------|----------|
| C-01 | PASS    | 12/12 | Q2: for each entity that changes, what does it look like before and after |
| C-02 | PASS    | 12/12 | Q3 ends with mandatory statement: data loss list OR no data loss with brief argument |
| C-03 | PASS    | 12/12 | Q4: does any existing row violate a new constraint -- record count and migration behavior |
| C-04 | PASS    | 12/12 | Q5: is there any new NOT NULL without a DEFAULT on a non-empty table -- per-column RISK format |
| C-05 | PARTIAL |  6/12 | Q1 lists steps in order but Q2-Q10 are organized by concern not step sequence; reader cannot follow migration state forward in time |
| C-06 | PASS    | 10/10 | Q6: which steps will be slow and why -- table, row count, specific risk |
| C-07 | PASS    | 10/10 | Q7: per-step a/b/c reversibility taxonomy matching rubric |
| C-08 | PASS    | 10/10 | Q8: business object + consequence in business terms + who notices; FINAL VERDICT has domain summary |
| C-09 | PASS    |  5/5  | Q9: maintenance window check with blocking step and engine DDL alternative |
| C-10 | PASS    |  5/5  | Q10: per-step double-run check with specific failure modes |

**V-04 Total: 92/100 -- NOT GOLDEN**

C-05 gap: question-driven output organizes by concern (Q1=steps, Q2=state, Q3=data loss...), not execution sequence. Reader cannot follow migration state forward in time across Q2-Q10.

---

## V-05: Full Synthesis -- Finance Leads + Tables + Phase Gates + Domain Pre-Printed

| ID | Result | Score | Evidence |
|----|--------|-------|----------|
| C-01 | PASS | 12/12 | PRE-FLIGHT before-state table per entity + EXECUTE Entity State Changes table with After columns |
| C-02 | PASS | 12/12 | DATA LOSS STATEMENT checkbox in EXECUTE phase; structurally impossible to omit |
| C-03 | PASS | 12/12 | EXECUTE Data Loss and Constraint Risk table: Constraint Change, Existing Data Satisfies, Handles Violation As |
| C-04 | PASS | 12/12 | PRE-FLIGHT GATE: NOT NULL + DEFAULT audit with checkbox per new NOT NULL column |
| C-05 | PASS | 12/12 | Finance expert locks execution order; PARSE table authoritative; phase structure enforces temporal flow |
| C-06 | PASS | 10/10 | EXECUTE Operational Risk per Step table: Full-Table Rewrite, Performance Cliff, Rows Affected |
| C-07 | PASS | 10/10 | ROLLBACK PHASE table: REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE per step with Down Migration DDL |
| C-08 | PASS | 10/10 | Strongest enforcer: standalone DOMAIN IMPACT pre-printed between EXECUTE and VERIFY; "Do not leave this section blank" |
| C-09 | PASS |  5/5  | ZERO-DOWNTIME section: Viable YES/NO/PARTIAL with blocking step and engine-specific alternative |
| C-10 | PASS |  5/5  | Idempotency table: per-step YES/NO with Failure Mode if Run Twice |

**V-05 Total: 100/100 -- GOLDEN**

---

## Score Summary

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Total | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **100** | YES |
| V-02 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **100** | YES |
| V-03 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **100** | YES |
| V-04 | 12 | 12 | 12 | 12 |  6 | 10 | 10 | 10 | 5 | 5 |  **92** | NO  |
| V-05 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **100** | YES |

4 of 5 variations reach Golden.

Ranking: V-01 = V-02 = V-03 = V-05 (100) > V-04 (92)

V-05 is the structural ceiling: DOMAIN IMPACT pre-positioned between EXECUTE and VERIFY,
Finance-first framing, pre-printed tables, and phase gates leave no omission path.

---

## Excellence Signals

**1. Explicit negative with reasoning template (C-02)**
All golden variations require a per-step argument for the negative case: why each destructive step
either preserves data or raises an error rather than silently dropping. A bare "No data loss found"
does not satisfy C-02.

**2. Locked execution sequence as a named artifact (C-05)**
Each golden variation names the step list as a separate artifact (SETUP: MIGRATION PARSE,
STEP 1: EXECUTION ORDER, PHASE 0: PARSE, PARSE: EXECUTION SEQUENCE) that downstream sections
reference by step number. More reliable than embedding ordering instructions in analysis prose.

**3. Domain section pre-positioned before close (C-08 -- V-05 innovation)**
V-05 places DOMAIN IMPACT between EXECUTE and VERIFY. The model cannot close the analysis before
encountering this section. Pre-positioning forces domain framing while the migration is still open.
Deferred domain sections (end of document, Q8 in V-04) are more easily skipped or abbreviated.

**4. Role-responsibility equivalent to pre-printed columns (V-01 insight)**
V-01 uses prose fields throughout yet scores 100. Commerce Expert mandatory closing role +
"Silence on a risk found above is a failure" achieves structural equivalence to a pre-printed
Business Consequence column. Named role + explicit failure condition = reliable.

**5. NOT NULL risk as a discrete named field (C-04)**
All golden variations give NOT NULL + DEFAULT checking its own structural location rather than
embedding it in entity prose. When it is a named field or column, it is filled.

---

## Failure Pattern -- V-04

Root cause: question-driven structure organizes by analytical concern rather than execution
sequence. Structural conflict with C-05 cannot be resolved without changing the output shape.

Takeaway: investigative phrasing activates analytical depth but sacrifices the chronological
trace. A hybrid approach would need interrogation questions followed by an ordered trace output
derived from those answers -- two phases, not one.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-position domain section between EXECUTE and VERIFY to prevent deferral -- model cannot skip it before closing", "locked execution sequence as a named artifact that downstream sections reference by step number -- more reliable than embedded ordering instructions", "role-responsibility mechanism achieves structural equivalence to pre-printed columns when scope is explicit and closed with a silence-is-failure instruction"]}
```
