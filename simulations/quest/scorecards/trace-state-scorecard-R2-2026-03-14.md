---

## trace-state R2 Results

### Scores

| Rank | Variation | Score | Key gap |
|------|-----------|-------|---------|
| 1 | **V-04** (Full ID + Min-Found) | **100** | — |
| 2 | V-01 (Min-Found threshold) | **99** | C-12 partial |
| 3 | V-02 (Domain example bank) | **97** | C-09/C-11/C-12 partial |
| 3 | V-03 (Interleave depth) | **97** | C-09/C-11/C-12 partial |
| 3 | V-05 (Entry Condition sep + bank) | **97** | C-09/C-11/C-12 partial |

### Key differentiators

**C-12 (Op ID cross-referencing) split the field**: V-04 is the only variation with a complete undeclared reference mechanism -- dedicated log section, 5th sweep row, and full ID columns in the anomaly register. Every other variation has Op IDs in the trace but lacks the surfacing mechanism. The gap between V-04 (100) and V-01 (99) is entirely C-12.

**C-11 separates V-01 from V-02/V-03/V-05**: V-01 adds the minimum-found threshold (>=2) which blocks easy-path all-negative sweeps. V-02/V-03/V-05 have the sweep table but allow all-none. V-01 earns full C-11 PASS despite missing C-12.

**Single-axis specialists**: V-03 has the strongest C-08 enforcement (3-step labeled interleave with actor/action/field/condition per step). V-02/V-05 have the strongest C-05 enforcement (9-name example bank). V-05 has the strongest C-13 enforcement (Entry Condition structurally active in Compiler). None of these axis wins change the score because C-08/C-05/C-13 already pass in all variations -- they are reliability improvements, not ceiling raises.

### Excellence signals (new in R2, not in R1)

1. **Minimum-found threshold as depth gate** -- converts C-11 from coverage gate to findings gate
2. **Full ID ecosystem** -- S-IDs, OP-IDs, INV-IDs all cross-referenced; any gap = mechanical failure not prose gap
3. **Undeclared reference as named anomaly class** -- 5th sweep row with verdict + production consequence
4. **Anomaly register with full ID columns** -- blank in found row = detectable cross-reference gap

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Minimum-found threshold converts sweep table from coverage gate to depth gate -- >=2 found rows required blocks easy-path all-negative completions and forces genuine anomaly construction", "Full ID ecosystem extends Op ID discipline to state IDs and invariant IDs -- every reference in the trace body has a declared counterpart, and any gap is a mechanical cross-reference failure rather than a prose judgment call", "Undeclared reference elevated to a named 5th anomaly class in the sweep table -- makes ID-discipline violations visible with the same structure as domain anomalies including sweep row and production consequence", "Anomaly register with separate OP-ID S-ID INV-ID columns -- blank in any found-verdict row is a detectable mechanical gap applying the anti-generic constraint from C-04 to the anomaly register itself"]}
```
ing. Third pass condition not structurally enforced. |
| C-13 | Entry Condition column | PASS | State machine table includes Entry Condition column; Domain Expert gate checks "All states have entry conditions." |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 9/10 (C-12 PARTIAL = 1)

**Total: 99**

---

## V-02: C-05 Domain Example Bank

**Axis**: Domain Expert gate prefaced with 9 concrete entity name examples (3 per domain). Affirmative anchor replaces rejection-only language.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Before/after state per operation | PASS | Trace table columns same as V-04-R1 baseline. |
| C-02 | Preconditions and postconditions | PASS | Preconditions and Postconditions columns per step; state-specific entries required. |
| C-03 | Invariant declaration | PASS | INV table with INV-ID, Scope, Violation Consequence. |
| C-04 | Anomaly identification | PASS | Anomaly register min 1 row; sweep table rows require op+state reference when found. |
| C-05 | Domain grounding | PASS | Strongest C-05 enforcement: (1) 9-name example bank shows exact specificity required; (2) gate checks entity name, state labels, operation names at specificity level; (3) inline hints on naming ("status field vocabulary, not architectural labels"). |
| C-06 | Negative path coverage | PASS | Rejected transitions table min 1 row. |
| C-07 | Step-by-step trace format | PASS | Numbered step table with before/after state. |
| C-08 | Race condition analysis | PASS | Race condition detail section (complete if verdict = found) -- not optional. |
| C-09 | All four anomaly types | PARTIAL | Sweep table forces evaluation of all 4 types (each row requires verdict). No min-found requirement -- all-negative sweep valid ("None found is a valid verdict"). Structural evaluation forced, findings not forced. |
| C-10 | Structured notation | PASS | State machine table + transitions table. |
| C-11 | Sweep table with mandatory verdicts | PARTIAL | Sweep table present with mandatory row-level verdicts -- blocks omission. But no min-found requirement: "A fully-negative table does not pass" from C-11 rubric is not enforced. V-02 explicitly allows all-none. |
| C-12 | Op ID cross-referencing | PARTIAL | Op IDs declared and referenced; no undeclared reference log section, no sweep row for undeclared references. Same gap as V-01. |
| C-13 | Entry Condition column | PASS | State machine table includes Entry Condition column. |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 7/10 (C-09 PARTIAL=1, C-11 PARTIAL=1, C-12 PARTIAL=1)

**Total: 97**

---

## V-03: C-08 Minimum Interleave Depth

**Axis**: Race condition analysis requires minimum 3 interleave steps, each labeled I-1/I-2/I-3+ with actor, action, field, and resulting condition.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Before/after state per operation | PASS | Trace table columns same as baseline. |
| C-02 | Preconditions and postconditions | PASS | Preconditions + Postconditions columns per step. |
| C-03 | Invariant declaration | PASS | INV table with INV-ID, Scope, Violation Consequence. |
| C-04 | Anomaly identification | PASS | Anomaly register min 1 row with op+state reference. |
| C-05 | Domain grounding | PASS | Gate item "no generic placeholders" -- same enforcement as V-04-R1. |
| C-06 | Negative path coverage | PASS | Rejected transitions table min 1 row. |
| C-07 | Step-by-step trace format | PASS | Numbered step table. |
| C-08 | Race condition analysis | PASS | Strongest C-08 enforcement in the set: 3-step labeled interleave (I-1, I-2, I-3) required; each step names actor (OP-A/B), action (reads/writes), field or state attribute, resulting condition; conflict must be identified at a specific interleave step, not just summarized; interleave gate checklist enforces all three conditions. |
| C-09 | All four anomaly types | PARTIAL | Sweep table forces evaluation; no min-found, allows all-none. Same as V-02. |
| C-10 | Structured notation | PASS | State machine table + transitions table. |
| C-11 | Sweep table with mandatory verdicts | PARTIAL | Mandatory row verdicts present, no min-found block on all-negative. Same as V-02. |
| C-12 | Op ID cross-referencing | PARTIAL | Same gap as V-01/V-02 -- no undeclared reference log. |
| C-13 | Entry Condition column | PASS | Entry Condition column present in state machine table. |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 7/10 (C-09 PARTIAL=1, C-11 PARTIAL=1, C-12 PARTIAL=1)

**Total: 97**

---

## V-04: Full ID Referencing + Minimum-Found Threshold

**Axes**: Full ID ecosystem (S-IDs, OP-IDs, INV-IDs all declared once, referenced everywhere; undeclared reference = anomaly type) + minimum-found >=2 requirement.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Before/after state per operation | PASS | Before-State (S-ID: Name) + After-State (S-ID: Name) columns; S-IDs required, undeclared S-ID is anomaly candidate. |
| C-02 | Preconditions and postconditions | PASS | Preconditions reference S-ID or OP-ID where relevant; INV Check column references INV-ID by name. State-specific by construction. |
| C-03 | Invariant declaration | PASS | INV table with INV-IDs; Scope column uses S-IDs ("S-01, S-02 or all states"). No duplicate IDs gate item. |
| C-04 | Anomaly identification | PASS | Min 2 anomaly rows; each row has A-ID, OP-ID, S-ID, INV-ID columns -- generic entries visible as blank-ID gaps. |
| C-05 | Domain grounding | PASS | Gate item "no generic placeholders"; same enforcement as V-04-R1. |
| C-06 | Negative path coverage | PASS | Rejected transitions with undeclared prefix support ("undeclared: [name]"). Undeclared operations in rejected transitions become anomaly candidates. |
| C-07 | Step-by-step trace format | PASS | Numbered step table; S-IDs and OP-IDs in every row. |
| C-08 | Race condition analysis | PASS | Race condition detail section with concurrent ops (OP-ID), S-ID, INV-ID in sweep row, interleave, resolution. |
| C-09 | All four anomaly types | PASS | Sweep table + min-found >=2 ensures at least 2 types found. 5th sweep row (Undeclared reference) extends anomaly surface. (C-11 supersedes; independently passes.) |
| C-10 | Structured notation | PASS | State machine table (S-IDs), valid transitions table (OP-IDs), invariants table (INV-IDs), anomaly sweep table -- richest tabular surface in the set. |
| C-11 | Sweep table with mandatory verdicts | PASS | 4 anomaly-type rows + 1 undeclared-reference row, each requiring explicit found/none verdict; min-found check blocks all-negative table (>=2 rows required); checklist boxes enforce review. Passes and exceeds C-11 threshold. |
| C-12 | Op ID cross-referencing | PASS | Full ID ecosystem: (1) all OP-IDs declared in transitions table; (2) every trace step references OP-ID; (3) INV Check references INV-ID; (4) anomaly sweep has OP-ID + INV-ID columns; (5) explicit undeclared reference log section; (6) 5th sweep row "Undeclared reference" makes ID gaps visible as a named anomaly class with production consequence; (7) anomaly register has separate OP-ID/S-ID/INV-ID columns -- blank in found row = mechanical cross-reference gap. All three pass conditions met. |
| C-13 | Entry Condition column | PASS | Entry Condition column in state machine table; Scope column uses S-IDs; Compiler INV Check references INV-IDs throughout. |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 10/10

**Total: 100**

---

## V-05: Entry Condition Separation + Domain Example Bank

**Axes**: Entry Condition structurally active in Compiler (two-level check: state-entry condition at every transition + operation precondition at every initiation, always distinct) + domain example bank.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Before/after state per operation | PASS | Verbose per-step block format; Before-State and After-State fields required per step. |
| C-02 | Preconditions and postconditions | PASS | Two-level model explicitly separates Operation Precondition (initiation) from Entry Condition (state entry); both required at each step. Strongest C-02 enforcement. |
| C-03 | Invariant declaration | PASS | INV table with INV-IDs, Scope, Violation Consequence. |
| C-04 | Anomaly identification | PASS | Anomaly register min 1 row with Level column (operation-precondition vs state-entry-condition). Entry Condition anomaly summary table adds second anomaly surface. |
| C-05 | Domain grounding | PASS | Domain example bank (same 9 names as V-02) + gate checks entity name AND state names ("practitioner-facing vocabulary") AND entry condition specificity ("distinct from 'record exists'"). Tied with V-02 for strongest C-05. |
| C-06 | Negative path coverage | PASS | Rejected transitions section with Type field distinguishing operation-precondition from state-entry-condition failure. Richer than baseline. |
| C-07 | Step-by-step trace format | PASS | Step-by-step block format; each step has Before-State, Operation, Preconditions, After-State, Entry Condition check, Postconditions, Invariant check. |
| C-08 | Race condition analysis | PASS | Race condition section (when found); not marked optional. |
| C-09 | All four anomaly types | PARTIAL | Sweep table with two-level questions per row (operation-initiation AND state-entry). All 4 rows require verdict. No min-found requirement -- all-none still valid. |
| C-10 | Structured notation | PASS | State machine table + transitions table + Entry Condition anomaly summary table. Three structured artifacts. |
| C-11 | Sweep table with mandatory verdicts | PARTIAL | Sweep table with mandatory row verdicts + two-level questions strengthen the gate. No min-found block on all-negative. |
| C-12 | Op ID cross-referencing | PARTIAL | Op IDs declared and referenced. No undeclared reference log section; undeclared use not surfaced as a dedicated anomaly finding. Same gap as V-01/V-02/V-03. |
| C-13 | Entry Condition column | PASS | Strongest C-13 enforcement: (1) Entry Condition column in state machine table with specificity gate; (2) Compiler checks entry condition at every state-changing step (active, not just declared); (3) Entry Condition anomaly summary table captures all violations; (4) Anomaly register Level column distinguishes operation-precondition from state-entry-condition findings; (5) rejected transitions include Type field. Two-level model fully activates C-13. |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 7/10 (C-09 PARTIAL=1, C-11 PARTIAL=1, C-12 PARTIAL=1)

**Total: 97**

---

## Composite Scores

| Rank | Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total |
|------|-----------|---------------|-----------------|-------------------|-------|
| 1 | **V-04** (Full ID + Min-Found) | 60 / 60 | 30 / 30 | 10 / 10 | **100** |
| 2 | V-01 (Min-Found threshold) | 60 / 60 | 30 / 30 | 9 / 10 | **99** |
| 3 | V-02 (Domain example bank) | 60 / 60 | 30 / 30 | 7 / 10 | **97** |
| 3 | V-03 (Interleave depth) | 60 / 60 | 30 / 30 | 7 / 10 | **97** |
| 3 | V-05 (Entry Condition sep + bank) | 60 / 60 | 30 / 30 | 7 / 10 | **97** |

**All variations pass all essential criteria. All variations pass all recommended criteria.**

---

## Key Differentiators

**C-12 (Op ID cross-referencing) split the field**: V-04 is the only variation with a complete undeclared reference mechanism -- log section, 5th sweep row, and full ID columns in the anomaly register. V-01/V-02/V-03/V-05 all have Op IDs in the trace but lack the surfacing mechanism. The gap between V-04 (100) and V-01 (99) is entirely C-12.

**C-11 (sweep table + min-found) separates V-01 from V-02/V-03/V-05**: V-01 adds the minimum-found threshold (>=2) to the sweep table, blocking the easy-path all-negative completion. V-02/V-03/V-05 have the sweep table but allow all-none. V-01 earns a full PASS on C-11 despite lacking C-12.

**C-08 best enforcement is in V-03**: Three labeled interleave steps with actor/action/field/condition per step substantially raise the bar for race condition analysis. Single-axis gain that doesn't affect other criteria -- V-03 is the specialist pick for race condition depth.

**C-05 best enforcement is in V-02/V-05**: The 9-name example bank is an affirmative anchor that V-04 lacks. Domain grounding is least likely to regress in V-02/V-05. However C-05 passes in all variations -- this is a reliability improvement, not a ceiling raise.

**C-13 best enforcement is in V-05**: The two-level model makes Entry Condition structurally active during the Compiler trace rather than a static declaration column. Most architecturally novel change in R2, but doesn't move the score because C-13 already passes at declaration-level. R3 research question: does activation produce new findings not visible in V-04?

---

## Excellence Signals from V-04-R2

### 1. Minimum-Found Threshold as Depth Gate
The minimum-found requirement (>=2 "found" rows) converts C-11 from a coverage gate (were all four types evaluated?) to a depth gate (were at least two types actually found?). A model satisfying R1 V-04 could fill four "none" verdicts with minimal effort. The minimum-found threshold blocks that path -- the trace scenario must surface at least two distinct anomaly types, or the trace must be enriched before closing.

### 2. Full ID Ecosystem: State IDs + Invariant IDs Added to Op ID Discipline
V-04-R2 extends the R1 excellence signal (Op ID cross-referencing) to state IDs and invariant IDs. Every reference in the trace body can be traced to a declaration row. The INV Check column uses INV-IDs, the anomaly sweep has separate OP-ID + INV-ID columns, and the anomaly register has A-ID/OP-ID/S-ID/INV-ID as separate columns. A blank in any "found" row is a mechanical cross-reference failure rather than a prose judgment call.

### 3. Undeclared Reference as a Named Anomaly Class
The 5th sweep row "Undeclared reference" elevates ID discipline violations from an informal instruction to a typed anomaly class with a sweep question, verdict slot, and production consequence (scope creep / silent drift). ID gaps are visible in the same register as domain anomalies.

### 4. Anomaly Register with Full ID Columns
The anomaly register (A-ID, OP-ID, S-ID, INV-ID, Description, Severity) applies the anti-generic constraint from C-04 to the register itself. Any "found" verdict with a blank ID column is a detectable cross-reference gap -- mechanical rather than prose enforcement.

---

## Research Questions for R3

1. **Minimum-found fabrication risk** (V-01, V-04): Do the >=2 "found" rows contain genuine trace-supported findings or are thin anomalies invented to satisfy the count? Measure: are "found" verdicts independently verifiable from the specific trace steps they cite?

2. **C-12 gap in V-01/V-02/V-03/V-05**: A minimal undeclared reference log ("None -- all references resolved") might close the C-12 gap without V-04's overhead. Test: V-01+log variant -- does the log alone achieve the C-12 pass condition, or is the 5th sweep row also required?

3. **C-13 activation cost** (V-05): Does the two-level check surface new findings that declaration-only (V-04) misses? Measure: count Entry Condition anomaly summary entries in V-05 outputs that are absent from matched V-04 outputs. If zero, activation adds overhead without signal.

4. **C-08 interleave depth vs. accuracy** (V-03): Does the 3-step requirement produce accurate temporal sequences or verbose setup? Measure: count interleave steps in V-03 outputs that identify the actual conflict point vs. setup steps that merely establish preconditions.

5. **V-04 ID column overhead**: 7-column anomaly register vs. 5-column in V-01. Does the additional columns improve anomaly traceability or degrade scanning? Compare reviewer verification time across matched V-04 and V-01 outputs.

---

## JSON

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Minimum-found threshold converts sweep table from coverage gate to depth gate -- >=2 found rows required blocks easy-path all-negative completions and forces genuine anomaly construction", "Full ID ecosystem extends Op ID discipline to state IDs and invariant IDs -- every reference in the trace body has a declared counterpart, and any gap is a mechanical cross-reference failure rather than a prose judgment call", "Undeclared reference elevated to a named 5th anomaly class in the sweep table -- makes ID-discipline violations visible with the same structure as domain anomalies including sweep row and production consequence", "Anomaly register with separate OP-ID S-ID INV-ID columns -- blank in any found-verdict row is a detectable mechanical gap applying the anti-generic constraint from C-04 to the anomaly register itself"]}
```
