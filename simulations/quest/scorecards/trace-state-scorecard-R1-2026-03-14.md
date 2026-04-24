Scorecard written to `simulations/quest/scorecards/trace-state-scorecard-R1-2026-03-14.md`.

---

## trace-state R1 Results

### Scores

| Rank | Variation | Score | Key gap |
|------|-----------|-------|---------|
| 1 | **V-04** (Format + Role Sequence) | **100** | — |
| 2 | V-03 (Role Sequence) | 97.5 | C-09 partial |
| 2 | V-05 (Lifecycle + Phrasing) | 97.5 | C-09 partial |
| 4 | V-02 (Conversational) | 89 | C-05, C-09, C-10 partial |
| 5 | V-01 (Table-Structured) | 86.5 | C-05, C-08, C-09 partial |

### Key differentiators

**C-05 (domain grounding)** split the field: V-01/V-02 lost 6 points each for using column hints and question phrasing without an explicit gate checklist that rejects generic names. V-03/V-04/V-05 all have explicit checklist items ("no generic placeholders").

**C-08 (race condition)** cost V-01 alone: its race section is optional ("Skip if none"). Every other variation has a dedicated non-optional section or sub-heading.

**C-09 (all four anomaly types)** is where V-04 broke away from V-03/V-05. The sweep table pre-prints all four type rows with mandatory "found / none" verdicts — the model cannot skip a row without leaving a blank cell. V-03 and V-05 use per-type prose sections where "None found" is an easy out.

### Excellence signals

1. **Sweep table with mandatory row-level verdicts** — stronger C-09 gate than prose sections
2. **Op ID cross-referencing** — undeclared operation use becomes a flagged anomaly, not silent drift
3. **Entry Condition column in state machine table** — preconditions declared at state level, not just operation level

### JSON

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Sweep table with mandatory row-level verdicts per anomaly type forces explicit negatives -- stronger C-09 gate than per-type prose sections", "Op ID cross-referencing between Domain Expert and Compiler turns undeclared operation invention into a flagged anomaly rather than silent scope expansion", "Entry Condition column in state machine table declares what is required to be in each state at declaration time, complementing per-operation preconditions in the trace"]}
```
**V-04 PASS**: Domain Expert gate checklist states "Entity and domain named with domain vocabulary -- no generic placeholders" plus Domain Description column.
- **V-05 PASS**: GATE 1 requires "Entity named with domain vocabulary (not a generic placeholder)."

### C-08 -- Race Condition
- **V-01 PARTIAL**: Race condition section present but explicitly optional ("Skip with 'No race condition in scope' if none").
- **V-02 through V-05 PASS**: Dedicated section or sub-heading -- not marked optional.

### C-09 -- All Four Anomaly Types
- **V-01 PARTIAL**: Anomaly Type column lists all four as options, "as many as the trace warrants" -- no mandate.
- **V-02 PARTIAL**: All four types listed as bullets in Step 6 with question phrasing only -- structural enforcement absent.
- **V-03 PARTIAL**: Four dedicated prose sections force evaluation, but "None found" valid per section -- all four types not mandated as findings.
- **V-04 PASS**: Sweep table pre-prints all four anomaly type rows, each requiring explicit "found / none" verdict. Model cannot skip a row without leaving a blank cell -- strongest enforcement in the set.
- **V-05 PARTIAL**: Four sub-headings force evaluation, but "None found" valid per heading -- same strength as V-03, weaker than V-04's sweep table.

### C-10 -- Structured Notation
- **V-01 PASS**: State machine table + transitions table pre-printed.
- **V-02 PARTIAL**: Step 3 produces a structured list "op: FROM to TO" -- qualifies as structured list per rubric but weaker than a table.
- **V-03 PASS**: Domain Expert has pre-printed states table and transitions table.
- **V-04 PASS**: State machine table with Entry Condition column + transitions table with Op IDs -- richest surface in the set.
- **V-05 PASS**: PHASE 2 DECLARE produces a structured list; "op: FROM to TO" format qualifies under rubric.

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total (100) |
|-----------|---------------|-----------------|-------------------|-------------|
| V-01 | 54 / 60 | 25 / 30 | 7.5 / 10 | **86.5** |
| V-02 | 54 / 60 | 30 / 30 | 5 / 10 | **89** |
| V-03 | 60 / 60 | 30 / 30 | 7.5 / 10 | **97.5** |
| V-04 | 60 / 60 | 30 / 30 | 10 / 10 | **100** |
| V-05 | 60 / 60 | 30 / 30 | 7.5 / 10 | **97.5** |

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | V-04 | 100 | All essential pass, all recommended pass, all aspirational pass |
| 2 | V-03 | 97.5 | All essential pass, all recommended pass, C-09 partial |
| 2 | V-05 | 97.5 | All essential pass, all recommended pass, C-09 partial -- tied with V-03 |
| 4 | V-02 | 89 | C-05 partial, C-09 partial, C-10 partial |
| 5 | V-01 | 86.5 | C-05 partial, C-08 partial, C-09 partial |

---

## Excellence Signals from V-04

### 1. Sweep Table with Mandatory Row-Level Verdicts
The Anomaly Finder sweep table pre-prints all four anomaly type rows (Invalid state transitions, Missing precondition checks, Invariant violations, Race conditions), each requiring an explicit "found / none" verdict plus Op+State and Production Consequence columns. The model cannot omit a type without leaving a blank cell. This is a stronger C-09 gate than per-type prose sections (V-03/V-05) because an explicit negative verdict requires more cognitive commitment than leaving a section with "None found." The structural gap functions as a forcing function.

### 2. Op ID Cross-Referencing Across Roles
Domain Expert declares Op IDs (OP-01, OP-02, etc.) in the transitions table; Compiler must reference operations by OP-ID. This creates a traceable link between declaration and execution. Any operation the Compiler tries to use that was not declared in the transitions table is immediately visible as an out-of-scope reference -- turning silent scope expansion into an explicit anomaly finding rather than an undetected drift.

### 3. Entry Condition Column in State Machine Table
V-04 adds "Entry Condition" as a required column in the state machine table, making the preconditions for entering each state explicit at declaration time, not just at operation time. This complements the per-operation preconditions in the Compiler trace by establishing what "being in a state" requires before any operation begins. It also enables the Anomaly Finder to identify missing-precondition-check anomalies at two levels: entry to a state and initiation of an operation.

---

## Research Questions for R2

1. **C-09 ceiling**: V-04's sweep table achieves a full PASS on C-09, but "found / none" verdicts still allow all negatives with no friction. Should R2 introduce a minimum-found threshold (e.g., "at least two anomaly types must be confirmed") to force deeper trace coverage?

2. **C-05 gate strength**: V-03/V-04/V-05 pass with a gate checklist item, but a checklist item is still self-reported. Would a concrete example bank (three domain-specific name examples per entity type) produce stronger domain grounding without over-constraining the model?

3. **C-08 interleave specificity**: Race condition sections across variations ask for two concurrent ops and an interleave, but none specify a minimum interleave depth (e.g., "show at least two interleave points"). Should R2 add a minimum interleave depth requirement to distinguish shallow from substantive race condition analysis?

4. **Op ID scope control**: V-04's Op ID cross-referencing is an excellence signal -- should other criteria (e.g., invariant IDs, state IDs) receive the same cross-reference treatment in R2? What is the structural cost of full ID-referencing throughout the trace?

5. **Entry Condition vs. Precondition separation**: V-04 introduces Entry Condition at the state level and Precondition at the operation level. Are these always distinct, or do some domains collapse them? Should R2 rubric C-02 be split into two sub-criteria to capture this distinction explicitly?

6. **Partial on C-10 for V-02**: V-02 produces "op: FROM to TO" structured lists rather than tables. The rubric permits structured lists but scores them lower than tables. Should R2 define a minimum structural threshold (e.g., "at least one table required") to remove ambiguity?

---

## JSON

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Sweep table with mandatory row-level verdicts per anomaly type forces explicit negatives -- stronger C-09 gate than per-type prose sections", "Op ID cross-referencing between Domain Expert and Compiler turns undeclared operation invention into a flagged anomaly rather than silent scope expansion", "Entry Condition column in state machine table declares what is required to be in each state at declaration time, complementing per-operation preconditions in the trace"]}
```
