Scorecard written to `simulations/quest/scorecards/trace-state-scorecard-R5-2026-03-14.md`.

---

## Summary

**Top score: 99** (V-03 and V-04, tied) | **All essential pass: true**

| Rank | Variation | Score | Deciding factor |
|------|-----------|-------|-----------------|
| 1T | V-03 Workshop / Score-Aloud | 99 | C-08 PASS; C-21 richer (C/FP/FN + calibration score) |
| 1T | V-04 Phase Gates | 99 | C-08 PASS; C-20/C-21/C-22 as hard exit checkboxes |
| 3T | V-01 Role Sequence | 95 | C-08 PARTIAL (setup without conflict outcome) |
| 3T | V-05 Doc-vs-Trace | 95 | C-08 PARTIAL (no concurrent scenario in trace) |
| 5 | V-02 Tabular Compact | 78 | C-01/C-02 PARTIAL (compressed table loses field values and named preconditions) |

**The R5 gap that kept every variation from 100**: C-09 (all four anomaly types required to be found). No variation mandates all four types — the quality gate requires ≥2 found, not all four. This is the ceiling to target in R6.

**New patterns:**
1. **Score-aloud verbal protocol** (V-03) — C-22 as spoken cognitive discipline with self-correction ("stop. Go back."), not a table cell to fill at end of sweep
2. **Phase exit gate checkboxes** (V-04) — C-20/C-21/C-22 as hard completion gates per phase, preventing optional-boilerplate treatment

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["score-aloud verbal protocol -- frames C-22 as a spoken cognitive discipline with a self-correction instruction ('stop. Go back.'), making anti-retroactive scoring a behavioral checkpoint rather than a table-filling task that can be satisfied in a single editing pass", "phase exit gate checkboxes listing C-20/C-21/C-22 as explicit completion criteria -- converts new aspirational criteria from optional boilerplate to hard gates the model must check before advancing to the next phase"]}
```
2 found, not all four; no explicit requirement to produce all four |
| C-10 | Aspirational | PASS | Full declaration tables 2A-2C for states, operations, invariants |
| C-11 | Aspirational | PASS | ANOMALY FINDER Pass 2: 5-row sweep table; all rows require explicit verdict |
| C-12 | Aspirational | PASS | OP-IDs declared in 2B; trace template uses OP-IDs; undeclared use surfaces in 5th sweep row |
| C-13 | Aspirational | PASS | Section 2A Entry Condition column; "data is valid" rejected; anomaly detection enabled at two levels |
| C-14 | Aspirational | PASS | Quality gate text states "PASS requires >=2 rows 'Found'" explicitly |
| C-15 | Aspirational | PASS | S-ID, OP-ID, INV-ID all declared; all references downstream use declared IDs; undeclared reference is a finding |
| C-16 | Aspirational | PASS | 5th sweep row "Undeclared ID reference" with required verdict |
| C-17 | Aspirational | PASS | Register columns include OP-ID, S-ID, INV-ID; "no blank cells in a found-verdict row; use N/A: [reason]" |
| C-18 | Aspirational | PASS | Pass 1 reads declaration tables only and predicts; Pass 2 reads full trace; reconciliation table present |
| C-19 | Aspirational | PASS | Strength column in sweep; gate requires >=1 Found row with Strength >=2 |
| C-20 | Aspirational | PASS | Role 1B falsification test column; gate text: "Analyst may not start Section 2 until this table has >=2 rows with non-blank Falsification Tests referencing specific thresholds, ratios, or date constraints" |
| C-21 | Aspirational | PASS | Reconciliation table has Surprise column labeled "Expected / Surprising" with one sentence explanation required |
| C-22 | Aspirational | PASS | "Assign Strength at the moment you identify each finding -- do not adjust scores after completing the sweep" in sweep header |

**Subtotals**:
- Essential: 5/5 x 60% = **60.0%**
- Recommended: (2 + 0.5)/3 x 30% = **25.0%**
- Aspirational: 13.5 x 0.714% = **9.64%**

**V-01 Total: 94.64 -> 95**

---

## V-02 — Output Format (Three-Value Surprise Taxonomy + Calibration Score)

| ID | Tier | Verdict | Evidence |
|----|------|---------|---------|
| C-01 | Essential | PARTIAL | Section 6 trace table has Before S-ID and After S-ID columns -- state IDs only, no key field values; "full entity state" not captured |
| C-02 | Essential | PARTIAL | "Preconditions Met?" column is binary Y/N; naming the precondition only required for Reject rows via footnote, not all rows; pass condition requires state-specific preconditions on every operation |
| C-03 | Essential | PASS | Section 2 pre-declares numeric/temporal invariants with Falsification Test; Section 5 merges all invariants with INV-IDs |
| C-04 | Essential | PASS | Section 8 sweep table; quality gate Gates A-C; >=2 Found required |
| C-05 | Essential | PASS | Finance domain; entity chosen from Finance list |
| C-06 | Recommended | PASS | Section 6 requires "at least one Reject row (negative path)" with Rejection reason footnote naming failing precondition |
| C-07 | Recommended | PARTIAL | Section 6 is a compressed table (Step / OP-ID / Before S-ID / After S-ID / Result); before/after are state IDs only; reader cannot follow full entity state without inference |
| C-08 | Recommended | PARTIAL | Section 6 requires "one concurrent scenario setup" with Race scenario footnote; conflicting outcome named but resolution/detection mechanism not explicitly required |
| C-09 | Aspirational | PARTIAL | Sweep has all 5 types; quality gate only requires >=2 Found; all four anomaly types not required to be found |
| C-10 | Aspirational | PASS | Sections 3-5 are full declaration tables for states, operations, invariants |
| C-11 | Aspirational | PASS | Section 8 sweep table; 5 pre-printed rows; all rows require explicit verdict; Gate C requires no blank cells |
| C-12 | Aspirational | PASS | OP-IDs declared in Section 4; all trace/sweep/register references use OP-IDs |
| C-13 | Aspirational | PASS | Section 3 Entry Condition column; "specific field values, amounts, or actor roles" required; generic validity rejected |
| C-14 | Aspirational | PASS | "Gate A: >= 2 rows 'Found'" stated explicitly |
| C-15 | Aspirational | PASS | S-ID, OP-ID, INV-ID all declared; all downstream references use declared IDs |
| C-16 | Aspirational | PASS | "Undeclared ID reference" as 5th sweep row with required verdict |
| C-17 | Aspirational | PASS | Section 10 register has OP-ID, S-ID, INV-ID, Reachability Path columns; "Strength must match Section 8 -- no revision permitted" |
| C-18 | Aspirational | PASS | Section 7 pre-sweep hypothesis (scans Sections 2-5 only); Section 8 full trace sweep; dual-pass structure present |
| C-19 | Aspirational | PASS | Strength column in Section 8; "Score Strength at point of discovery"; Gate B requires >=1 Strength >=2 |
| C-20 | Aspirational | PASS | Section 2 gate: "Do not start Section 3 until both rows have a non-blank Falsification Test referencing a specific value, not a generic condition" |
| C-21 | Aspirational | PASS | Section 9 uses C/FP/FN three-value taxonomy with calibration score; exceeds binary requirement; <60% triggers structural diagnosis |
| C-22 | Aspirational | PASS | Top-of-prompt constraint: "Score at point of discovery -- assign evidence Strength when you first identify each finding, not after the full sweep is complete. Do not revise scores retroactively." |

**Subtotals**:
- Essential: (3 + 1) x 12% = **48.0%** (C-01, C-02 each PARTIAL)
- Recommended: (1 + 0.5 + 0.5) x 10% = **20.0%**
- Aspirational: 13.5 x 0.714% = **9.64%**

**V-02 Total: 77.64 -> 78**

---

## V-03 — Phrasing Register (Workshop Voice / Score-Aloud Protocol)

| ID | Tier | Verdict | Evidence |
|----|------|---------|---------|
| C-01 | Essential | PASS | Step template: "Before: [S-ID], key field values" and "After: [S-ID], key field values that changed" -- full entity state with field values |
| C-02 | Essential | PASS | "Preconditions (name the field and value -- 'preconditions met' doesn't count)" -- explicit naming requirement; Postconditions listed per step |
| C-03 | Essential | PASS | Step 1 invariant table; Step 2 invariant declaration with INV-IDs inherited from Step 1 |
| C-04 | Essential | PASS | Step 5 sweep with Found/None; gate requires >=2 Found |
| C-05 | Essential | PASS | Customer Service domain; entity chosen from Support Ticket, Escalation Case, etc. |
| C-06 | Recommended | PASS | Step 3 requires "at least one step that gets rejected: name exactly which precondition fails and what the system does" |
| C-07 | Recommended | PASS | Step N template with numbered steps, before/after, preconditions named; mechanical replay supported |
| C-08 | Recommended | PASS | Step 3 requires "at least one step that sets up a race: name the two operations that could collide and what state conflict results" -- two operations AND conflicting outcome named = detection satisfied |
| C-09 | Aspirational | PARTIAL | Sweep has all 5 types; gate requires >=2 Found; trace requires negative path + race setup = 2 types likely, not all four explicitly required |
| C-10 | Aspirational | PASS | Step 2 declaration tables for states (5+), operations (7+), invariants -- formal structured artifact |
| C-11 | Aspirational | PASS | Step 5 sweep: 5-row table; all rows require Found/None verdict |
| C-12 | Aspirational | PASS | "Every state gets an S-ID, every operation an OP-ID, every invariant an INV-ID. Using one without declaring it is a finding." |
| C-13 | Aspirational | PASS | Step 2 states table: Entry Condition column; "Ticket is assigned to an agent" passes; "System is online" rejected |
| C-14 | Aspirational | PASS | "Gate check: you need at least 2 'Found' rows" explicitly stated |
| C-15 | Aspirational | PASS | S-ID, OP-ID, INV-ID all declared in Step 2; all references use declared IDs |
| C-16 | Aspirational | PASS | "Undeclared ID reference" as 5th sweep row |
| C-17 | Aspirational | PASS | Step 6 register: A-ID, Type, OP-ID, S-ID, INV-ID, What breaks, Severity, Strength; "No blank cells -- use N/A: [reason]"; Strength must match Step 5 |
| C-18 | Aspirational | PASS | Step 4 (tables only, predictions) + Step 5 (full trace sweep) = dual-pass; Step 7 reconciliation |
| C-19 | Aspirational | PASS | Strength scale at Step 5; gate requires >=2 Found + >=1 at Strength >=2 |
| C-20 | Aspirational | PASS | Step 1: "If both rows say 'No' in the numeric/temporal column: revise at least one before moving on. This gate must close before you build any tables." |
| C-21 | Aspirational | PASS | Step 7 uses C/FP/FN three-value taxonomy + calibration score; <60% threshold triggers diagnosis sentence; richer than binary |
| C-22 | Aspirational | PASS | Rule 1 at top: "score its Strength (1/2/3) before writing anything else. If you catch yourself filling in Strength cells at the end of the sweep, stop. Go back." Score-aloud protocol + self-correction instruction |

**Subtotals**:
- Essential: 5/5 x 60% = **60.0%**
- Recommended: 3/3 x 30% = **30.0%**
- Aspirational: 13.5 x 0.714% = **9.64%**

**V-03 Total: 99.64 -> 99**

---

## V-04 — Role Sequence + Lifecycle Emphasis (Phase Gates with Hard Exit Criteria)

| ID | Tier | Verdict | Evidence |
|----|------|---------|---------|
| C-01 | Essential | PASS | Phase 3 step template: "Before: [S-ID] -- [State Name] | [relevant field values]" and matching "After:" -- full entity state with field values |
| C-02 | Essential | PASS | "Preconditions (name the field and value)" required per step; Postconditions listed; "field and value" framing prevents vague statements |
| C-03 | Essential | PASS | Phase 2C invariant table; at least one INV-ID must have Source = Expert (traces to Phase 1B) |
| C-04 | Essential | PASS | Phase 4B sweep quality gate: >=2 Found; Remediation note required if gate fails |
| C-05 | Essential | PASS | Finance domain; entity from Finance list |
| C-06 | Recommended | PASS | Phase 3 requires "Negative path: operation attempted from invalid state, precondition failure named, rejection behavior documented" |
| C-07 | Recommended | PASS | Phase 3 numbered steps "Step N -- [OP-ID]: [Operation Name]" with full before/after template |
| C-08 | Recommended | PASS | Phase 3 requires "Concurrent scenario: two operations that could interleave on the same entity, with the conflicting outcome described" -- conflicting outcome = detection mechanism satisfied |
| C-09 | Aspirational | PARTIAL | Quality gate requires >=2 Found; trace requires negative path + concurrent scenario = 2 types; not all four explicitly required |
| C-10 | Aspirational | PASS | Phases 2A-2C are full structured declaration tables |
| C-11 | Aspirational | PASS | Phase 4B sweep: 5 pre-printed rows; all rows require explicit verdict; Gate C forbids blank cells |
| C-12 | Aspirational | PASS | OP-IDs declared in 2B; all trace, sweep, and register references use OP-IDs |
| C-13 | Aspirational | PASS | Phase 2A Entry Condition column; "Amount field is non-null and > 0" passes; "Data is valid" does not |
| C-14 | Aspirational | PASS | "Quantity: >= 2 rows 'Found'" as named condition in quality gate |
| C-15 | Aspirational | PASS | S-ID, OP-ID, INV-ID declared; Phase 2D ID Coverage Check; undeclared references flagged |
| C-16 | Aspirational | PASS | "Undeclared ID reference" as 5th sweep row with explicit verdict |
| C-17 | Aspirational | PASS | Phase 4D register: OP-ID, S-ID, INV-ID, Reachability columns; "no blank cells in any found-verdict row" |
| C-18 | Aspirational | PASS | Phase 4A Pass 1 (scans Phases 1B/2A-2C only) + Phase 4B Pass 2 (reads Phase 3); Phase 4C reconciliation |
| C-19 | Aspirational | PASS | Strength scale in Phase 4B; Quality Gate condition 2: >=1 Found row with Strength >=2 |
| C-20 | Aspirational | PASS | Phase 1 exit gate checkbox: "At least one invariant in 1B has a non-blank Falsification Test referencing a specific threshold, percentage, count, or date constraint" -- checkbox must be checked before Phase 2 |
| C-21 | Aspirational | PASS | Phase 4C reconciliation: Surprise = Expected / Surprising column; binary but with explanation required; Phase 4 exit gate: "Surprise column complete in 4C" |
| C-22 | Aspirational | PASS | Non-negotiable constraint at top: "Score at point of discovery: Strength (1/2/3) must be written when each finding is first recorded in Phase 4. No retroactive revision is permitted." Phase 4 exit gate: "Strength values in register match Phase 4B sweep table" |

**Subtotals**:
- Essential: 5/5 x 60% = **60.0%**
- Recommended: 3/3 x 30% = **30.0%**
- Aspirational: 13.5 x 0.714% = **9.64%**

**V-04 Total: 99.64 -> 99**

---

## V-05 — Inertia Framing + Output Format (Documentation-vs-Trace / Calibration Report)

| ID | Tier | Verdict | Evidence |
|----|------|---------|---------|
| C-01 | Essential | PASS | Part 4 step table has "Before state" row (Documentation Claims vs Trace Shows), both with S-ID and field values |
| C-02 | Essential | PASS | Preconditions row compares "what doc says must hold" vs "what trace actually checks -- or fails to check"; comparison format names preconditions explicitly |
| C-03 | Essential | PASS | Part 1 requires >=3 documented invariants including >=1 numeric/temporal; Part 2C assigns INV-IDs; gate check embedded |
| C-04 | Essential | PASS | Part 5 sweep + quality gate: >=2 Found and >=1 Strength >=2 |
| C-05 | Essential | PASS | Sales domain; entity from Sales list (Deal, Quote, Sales Order, etc.) |
| C-06 | Recommended | PASS | Part 4 requires "One negative path step: documentation claims rejection occurs -- confirm whether trace does too" |
| C-07 | Recommended | PASS | Part 4 numbered steps with full two-column (doc/trace) table per step; reader can replay and see divergence |
| C-08 | Recommended | PARTIAL | Part 5 sweep has Race condition row; no concurrent scenario setup required in Part 4 trace -- only 3 required step types (happy path, negative path, invariant-gap); race condition may produce "None" verdict without finding |
| C-09 | Aspirational | PARTIAL | Sweep has all 5 types; quality gate only requires >=2 Found; not all four types required explicitly |
| C-10 | Aspirational | PASS | Part 2 declaration tables for states (2A), operations (2B), invariants (2C) |
| C-11 | Aspirational | PASS | Part 5 sweep: 5 pre-printed rows; explicit verdict per row; quality gate enforces >=2 Found |
| C-12 | Aspirational | PASS | OP-IDs declared in Part 2B; trace steps reference OP-IDs; Doc Reference column adds documentation traceability |
| C-13 | Aspirational | PASS | Part 2A Entry Condition column; undocumented states flagged as a finding class |
| C-14 | Aspirational | PASS | "Quality gate: PASS requires >= 2 'Found' rows" |
| C-15 | Aspirational | PASS | S-ID, OP-ID, INV-ID declared; all references downstream use declared IDs |
| C-16 | Aspirational | PASS | "Undeclared ID reference" as 5th sweep row with Step N column for location |
| C-17 | Aspirational | PASS | Part 6 register: OP-ID, S-ID, INV-ID, Documentation Claim, What Trace Found, Delta, Severity, Strength; "Strength must match Part 5 -- no revision permitted" |
| C-18 | Aspirational | PASS | Part 3 pre-sweep hypothesis (reads Parts 1-2 only) + Part 5 full sweep; reconciliation in Part 7A |
| C-19 | Aspirational | PASS | Strength scale in Part 5; quality gate requires >=2 Found + >=1 Strength >=2 |
| C-20 | Aspirational | PASS | Part 1 invariant gate check: "If none reference a specific numeric cap, percentage, dollar amount, or date constraint, add one here before continuing" -- inline repair instruction |
| C-21 | Aspirational | PASS | Part 7A reconciliation: C/FP/FN three-value taxonomy + calibration score; <60% triggers diagnosis; "What the documentation hid -- or correctly predicted" column |
| C-22 | Aspirational | PASS | Top structural constraint: "Score at point of discovery: assign Strength to each anomaly the moment you identify it." Part 4: "Assign Strength immediately when you identify any discrepancy." Part 5: "Score Strength at point of discovery -- not afterward." Three-location reinforcement |

**Subtotals**:
- Essential: 5/5 x 60% = **60.0%**
- Recommended: (2 + 0.5)/3 x 30% = **25.0%**
- Aspirational: 13.5 x 0.714% = **9.64%**

**V-05 Total: 94.64 -> 95**

---

## Rankings

| Rank | Variation | Score | All Essential Pass | C-08 | C-21 Implementation |
|------|-----------|-------|--------------------|------|---------------------|
| 1 (tie) | V-03 Workshop / Score-Aloud | **99** | Yes | PASS | C/FP/FN + calibration score + verbal discipline |
| 1 (tie) | V-04 Phase Gates | **99** | Yes | PASS | Binary Expected/Surprising + phase exit checkbox |
| 3 (tie) | V-01 Role Sequence (R4 baseline) | **95** | Yes | PARTIAL | Binary Expected/Surprising |
| 3 (tie) | V-05 Doc-vs-Trace / Calibration Report | **95** | Yes | PARTIAL | C/FP/FN + calibration score + Documentation Verdict |
| 5 | V-02 Three-Value Taxonomy (tabular) | **78** | Yes* | PARTIAL | C/FP/FN + calibration score + numeric gate |

*V-02 Essential criteria are PARTIAL (C-01, C-02), not FAIL -- the essential bar is set but not fully met.

---

## Tiebreaker: V-03 vs V-04

| Dimension | V-03 | V-04 |
|-----------|------|------|
| C-21 depth | C/FP/FN + calibration score (richer than binary) | Binary Expected/Surprising |
| C-22 enforcement | Verbal "score-aloud" protocol with self-correction ("stop. Go back.") | Non-negotiable constraint at top + phase exit checkbox |
| C-20 enforcement | Inline gate with revise instruction | Phase exit checkbox -- cannot advance without checking |
| Structure | 7 sequential workshop steps | 4 phases with entry/exit criteria |

V-03 has the richer C-21 implementation. V-04 has stronger structural enforcement of all three new criteria via phase exit checkboxes. Both are genuine top-tier outputs at identical scores.

---

## Excellence Signals from R5

**Signal 1 -- Score-aloud verbal protocol (V-03)**
Rule 1 of V-03 frames Strength scoring as a spoken cognitive discipline: "score its Strength (1/2/3) before writing anything else. Say it to yourself: 'this is a 2 -- reachable in normal workflows.' Then write it down." Adding "If you catch yourself filling in Strength cells at the end of the sweep, stop. Go back." creates a self-correction protocol. This is different from a tabular requirement -- it makes C-22 a behavioral checkpoint rather than a form field, which is harder to satisfy retroactively by filling in cells in a single editing pass.

**Signal 2 -- Phase exit gate checkboxes for C-20/C-21/C-22 (V-04)**
V-04 lists C-20, C-21, and C-22 as explicit checkbox exit conditions for the phases where they apply -- Phase 1 cannot close until the numeric/temporal invariant gate is satisfied; Phase 4 cannot close until the Surprise column is complete and Strength values match the sweep table. Making them checkboxes rather than requirements in running text forces the model to treat them as hard gates. Without this structure, C-20/C-21/C-22 can be satisfied with minimal compliance (one vague threshold, one all-"Expected" column, one retroactive score fill).

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["score-aloud verbal protocol -- frames C-22 as a spoken cognitive discipline with a self-correction instruction ('stop. Go back.'), making anti-retroactive scoring a behavioral checkpoint rather than a table-filling task that can be satisfied in a single editing pass", "phase exit gate checkboxes listing C-20/C-21/C-22 as explicit completion criteria -- converts new aspirational criteria from optional boilerplate to hard gates the model must check before advancing to the next phase"]}
```
