Scorecard written to `simulations/quest/scorecards/trace-permissions-scorecard-R2-2026-03-14.md`.

---

## Round 2 Results — trace-permissions

**All 5 variations score 115/115.** Every variation is GOLDEN.

This is the expected outcome when rubric criteria are built into the design from the start rather than discovered by scoring. R1 left C-10/C-11/C-12 as blind spots; R2 explicitly targeted them in every variation.

### The discriminator shifted: pass/fail → bypass resistance

Since rubric v2 can no longer separate the variations numerically, the meaningful comparison is structural guarantee strength:

| Best | V-04, V-05 | Phase gate + pre-printed table — structural mechanisms that a model cannot bypass without producing a visibly broken output |
|------|------------|---|
| Good | V-01 | Phase gate + prose four-vector templates — C-12 slightly weaker (prose can be collapsed) |
| Good | V-03 | RULE + checkboxes — viable lighter-weight alternative; C-11 relies on model applying global RULE per section |
| C-10 risk | V-02 | Instruction-positioned hypothesis section only; no hard phase gate |

**Production candidate: V-04** — all phase gate benefits without V-05's redundant RULE layer overhead.

### Two new patterns

1. **Phase completion gate with checkbox** — `PHASE 1 COMPLETE [ ]` is an action the model must take, not just a constraint. Stronger than section ordering alone.
2. **H-flag column in evidence tables** — tying table cells to specific hypotheses creates a mechanical traceability path that doesn't depend on model recall. Not yet a rubric criterion — candidate for C-13 in v3.

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["Phase completion gate with explicit checkbox ('PHASE 1 COMPLETE [ ]') creates a visible required state transition that prevents phase skipping more robustly than instruction-ordering alone", "H-flag column in evidence tables (role-operation, FLS, scope) mechanically ties individual table cells to pre-committed hypotheses, making hypothesis resolution in findings traceable to exact evidence entries without requiring free recall"]}
```
our-vector table
(C-12 blank row is structurally visible). Lower template overhead than V-05 while covering all
three aspirational criteria with strong structural enforcement. V-05 adds RULE 1/2/3 on top of
V-04's mechanisms, but the RULEs are redundant with the phase gate and table structure already
in V-04.

---

### Per-Variation Criterion Detail

#### V-01: Phase-Gated Lifecycle

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role-Operation Matrix | PASS | 2-A: Y/N/Y* per cell; H-flag column; "Do not skip any operation" |
| C-02 FLS Named | PASS | 2-B: Field/Role/Allow-Deny table; "FLS should be configured without naming fields and roles fails" |
| C-03 Record Access Scope | PASS | 2-C: Own/BU/Parent BU/Org hierarchy; H-flag column |
| C-04 Gap Identified | PASS | Phase 3 gate: minimum one finding; "PHASE 3 COMPLETE" only after finding |
| C-05 Escalation Path | PASS | 2-D: From-Role + mechanism + unintended access gained per vector |
| C-06 Sharing Rule Conflict | PASS | 2-E: named rule, baseline scope, sharing grants, conflict described |
| C-07 Team Membership Gap | PASS | 2-F CUSTOMER SERVICE: scenario, affected users, gap type, impact |
| C-08 Risk-Ranked | PASS | Phase 4 Risk Ranking: H/M/L + justification referencing operation/data sensitivity |
| C-09 Remediation Per Gap | PASS | Phase 4 Remediation: "name the exact change: which field, which role, which configuration" |
| C-10 Hypothesis Pre-commitment | PASS | Hard phase gate: "Do not write evidence tables before Phase 1 is complete"; H1/H2/H3 all required; Phase 3 H-resolution per finding |
| C-11 Null-Finding Accountability | PASS | Null-accountability blocks in 2-B, 2-D, 2-E, 2-F -- all require "Examined: / Justification:" |
| C-12 Four-Vector Escalation Sweep | PASS | 2-D: 4 explicit vector templates (Reassignment, Team Promotion, Sharing Bypass, Impersonation); Status/Path/Cleared per vector |

Score: 115/115

#### V-02: Four-Vector Escalation Table

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role-Operation Matrix | PASS | TABLE 1: complete Y/N/R cells; restrictions section; failure mode stated |
| C-02 FLS Named | PASS | TABLE 2: Field/Role/Allow-Deny/FLS Gap? columns; failure mode stated |
| C-03 Record Access Scope | PASS | TABLE 3: scope per role; Own/BU/Parent BU/Org; Correct? + Notes |
| C-04 Gap Identified | PASS | TABLE 7: "must have at least one row; A trace with zero gaps is not valid" |
| C-05 Escalation Path | PASS | TABLE 4: found path requires From-Role + mechanism + unintended access |
| C-06 Sharing Rule Conflict | PASS | TABLE 5: rule, baseline scope, grants, conflict type; null block |
| C-07 Team Membership Gap | PASS | TABLE 6 CUSTOMER SERVICE: scenario, gap type, operational impact; null block |
| C-08 Risk-Ranked | PASS | TABLE 7: Risk (H/M/L) + Justification columns |
| C-09 Remediation Per Gap | PASS | TABLE 8: "name the exact change -- field, role, configuration location" |
| C-10 Hypothesis Pre-commitment | PASS* | HYPOTHESIS section before TABLE 1; H1/H2 required; "Do not omit or write after evidence tables"; TABLE 7 H-link + H-resolution columns. *Weakest C-10 mechanism -- instruction-positioned only, no phase gate. |
| C-11 Null-Finding Accountability | PASS | TABLE 4 examination-log column; TABLE 2/5/6 null accountability blocks; TABLE 4: "'None identified' without examination log fails C-11 and C-12" |
| C-12 Four-Vector Escalation Sweep | PASS | TABLE 4 pre-printed 4 mandatory rows; "Do not leave any cell blank"; blank row structurally visible |

Score: 115/115

#### V-03: Imperative Checklist

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role-Operation Matrix | PASS | STEP 3: [ ] checkbox; "Do not list roles without tying them to operations (RULE 4 failure mode)" |
| C-02 FLS Named | PASS | STEP 4: "Do not write 'FLS should be configured' -- name the field and the role (RULE 4)" |
| C-03 Record Access Scope | PASS | STEP 5: [ ] checkbox; "Do not use only 'users see their own records' -- that fails C-03" |
| C-04 Gap Identified | PASS | RULE 4 at top; STEP 9: [ ] "Name at least one gap. A trace with no findings fails (RULE 4)" |
| C-05 Escalation Path | PASS | STEP 6: per-vector templates with From-Role / Mechanism / Unintended Access |
| C-06 Sharing Rule Conflict | PASS | STEP 7: [ ] examines widening and contradictions; null protocol if none |
| C-07 Team Membership Gap | PASS | STEP 8 CUSTOMER SERVICE: gap type, impact; null protocol if none |
| C-08 Risk-Ranked | PASS | STEP 10: [ ] rank H/M/L; "Reference operation type or data sensitivity" |
| C-09 Remediation Per Gap | PASS | RULE 5 at top; STEP 10 remediation table: "name the exact change" |
| C-10 Hypothesis Pre-commitment | PASS | RULE 1 + [ ] H1/H2 checkboxes + "Do not advance to Step 3 until all boxes completed"; hypothesis resolution in STEP 9 |
| C-11 Null-Finding Accountability | PASS | RULE 2 globally + "[ ] If no X found, complete null protocol (RULE 2)" with template fields in every section |
| C-12 Four-Vector Escalation Sweep | PASS | RULE 3 + [ ] checkboxes for all 4 vectors individually + "Do not stop after finding one path -- all four vectors MUST be addressed" |

Score: 115/115

#### V-04: Lifecycle + Four-Vector Table

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role-Operation Matrix | PASS | 2-A: complete every cell; "No role listed without an operation"; Y/N/R |
| C-02 FLS Named | PASS | 2-B: FLS Gap? column; "'FLS should be configured' without naming fields and roles fails" |
| C-03 Record Access Scope | PASS | 2-C: Own/BU/Parent BU/Org; Correct? column; "Do not conflate role privileges with record ownership" |
| C-04 Gap Identified | PASS | Phase 3 gate: "Minimum one finding. Do not advance to Phase 4 without at least one finding." |
| C-05 Escalation Path | PASS | 2-D four-vector table: found path requires From-Role + mechanism + unintended access |
| C-06 Sharing Rule Conflict | PASS | 2-E: named rule, baseline scope, grants, conflict; null block |
| C-07 Team Membership Gap | PASS | 2-F CUSTOMER SERVICE: scenario, affected users, gap type, impact; null block |
| C-08 Risk-Ranked | PASS | Phase 4 Risk Ranking: H/M/L + "reference operation type or data sensitivity" |
| C-09 Remediation Per Gap | PASS | Phase 4 Remediation: "Name the exact change. 'Tighten security' fails." |
| C-10 Hypothesis Pre-commitment | PASS | Hard phase gate: "Complete before any evidence table"; findings must address H1/H2 by name; hypothesis resolution summary required |
| C-11 Null-Finding Accountability | PASS | Null-accountability blocks in 2-B, 2-D, 2-E, 2-F; 2-D: "'None identified' without examination log and justification fails C-11 and C-12" |
| C-12 Four-Vector Escalation Sweep | PASS | 2-D pre-printed 4-row TABLE; "Do not leave any cell blank"; examination log + one-sentence justification for Cleared |

Score: 115/115

#### V-05: Full R2 Synthesis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Role-Operation Matrix | PASS | 2-A: H-flag column; [ ] All cells completed; Y/N/R per cell |
| C-02 FLS Named | PASS | 2-B: FLS Gap? + H-flag columns; failure mode stated |
| C-03 Record Access Scope | PASS | 2-C: Own/BU/Parent BU/Org; H-flag; "Do not conflate privilege with record ownership"; [ ] All roles mapped |
| C-04 Gap Identified | PASS | Phase 3: "Minimum one finding required"; [ ] At least one finding with hypothesis resolution |
| C-05 Escalation Path | PASS | 2-D: pre-printed four-row table; found path = named mechanism + unintended access |
| C-06 Sharing Rule Conflict | PASS | 2-E: "[ ] If no conflicts found (RULE 2 -- complete before advancing)" |
| C-07 Team Membership Gap | PASS | 2-F CUSTOMER SERVICE: scenario, gap type, impact, H-flag; "[ ] If no gaps found (RULE 2)" |
| C-08 Risk-Ranked | PASS | Phase 4: H/M/L + "Reference operation type or data sensitivity -- not just the gap category" |
| C-09 Remediation Per Gap | PASS | Phase 4 Remediation; RULE 5: "'Tighten security' or 'review FLS' fails" |
| C-10 Hypothesis Pre-commitment | PASS | Three independent mechanisms: (1) RULE 1; (2) Phase 1 hard gate; (3) [ ] H1/H2 checkboxes; "PHASE 1 COMPLETE [ ]" gate; Phase 3 resolution summary |
| C-11 Null-Finding Accountability | PASS | RULE 2 globally + "[ ] If X (RULE 2 -- complete before advancing):" template slot in 2-B, 2-D, 2-E, 2-F; "PHASE 2 COMPLETE [ ]" gate |
| C-12 Four-Vector Escalation Sweep | PASS | RULE 3 + 2-D pre-printed four-row table + [ ] "All four vectors addressed" checkbox; "One path found does not satisfy the remaining three vectors" |

Score: 115/115

---

### Excellence Signals

**Pattern 1 -- Phase completion gate with explicit checkbox**
`PHASE 1 COMPLETE [ ] -- check this box before starting Phase 2` creates a visible required
state transition. A model cannot advance without producing an artifact that acknowledges the
gate. Structurally different from a section header or instruction -- it is an action the model
must take, not a constraint on what it writes. V-01/V-04/V-05 use this. Strongest C-10
enforcement mechanism across all R1 and R2 variations.

**Pattern 2 -- H-flag column in evidence tables**
Adding H-flag (H1/H2/H3/--) as a column in the role-operation matrix, FLS table, and scope
table creates a mechanical link between pre-committed hypotheses and specific evidence cells.
Hypothesis resolution in Phase 3 is traceable to exact table entries rather than requiring
the model to reconstruct the connection from memory. V-05 and V-01 use this; V-02/V-04/V-03
omit it. Candidate for rubric C-13 in v3 if hypothesis traceability becomes a distinct
criterion separate from hypothesis pre-commitment.

**Pattern 3 -- Null-accountability template slot vs. global RULE**
V-03's RULE 2 applies globally but requires consistent model application per section.
V-01/V-02/V-04/V-05 all have section-specific "Null accountability: Examined: / Justification:"
template slots positioned at the point where null results would appear. Template slot beats
global RULE for C-11 bypass resistance -- compliance requires filling an already-present slot
rather than remembering to apply a rule.

---

### R2 Key Findings

**Design question answered:** All three mechanisms (phase gating, table enforcement, imperative
checklist) individually produce C-10/C-11/C-12-compliant designs. The R1 finding "table
enforcement beats prose ordering for C-04" generalizes to C-12: pre-printed four-vector table
(V-02/V-04/V-05), four-vector prose templates (V-01), and RULE + checkboxes (V-03) all pass
C-12. Table format has lower bypass risk than prose templates; both beat no-structure.

**V-03 verdict:** Phrasing register alone (without phase gates or pre-printed tables) is
sufficient for 115/115 at the design level. Viable lighter-weight production option when
template overhead is a constraint. Structural bypass risk on C-11 and C-12 is moderate rather
than low, making it suitable for length-constrained skills but not preferred when maximum
structural guarantee is required.

**V-04 as production target:** Phase gate (C-10) + null-accountability blocks (C-11) +
pre-printed four-vector table (C-12), without V-05's redundant RULE layer. Minimum-overhead
path to maximum structural guarantee. V-05 adds measurable redundancy but the RULEs do not
change the structural guarantee beyond what the phase gate and tables already enforce.

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["Phase completion gate with explicit checkbox ('PHASE 1 COMPLETE [ ]') creates a visible required state transition that prevents phase skipping more robustly than instruction-ordering alone", "H-flag column in evidence tables (role-operation, FLS, scope) mechanically ties individual table cells to pre-committed hypotheses, making hypothesis resolution in findings traceable to exact evidence entries without requiring free recall"]}
```
