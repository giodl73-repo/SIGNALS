# trace-state Variate — Round 15
**Date:** 2026-03-15
**Rubric:** v13 / inner v29 (C-01..C-05 essentials; 31 aspirational criteria C-09..C-39; golden: all 5 essential pass AND composite ≥ 80)

R15 introduces two new aspirational criteria extracted from R14 pairwise evidence (v13 rubric):

- **C-38** — Step-label criterion-instruction fusion: a step label or within-block field
  annotation carries both a criterion ID **and** a behavioral directive. The step-block-format
  analog of C-30. A step label carrying only a criterion ID does not qualify. Achieving C-30
  in tabular format does not cross-satisfy C-38.

- **C-39** — Step-block disqualification-condition fusion: a step label or within-block field
  annotation carries both a criterion ID **and** the specific pattern that *fails* the criterion.
  The step-block-format analog of C-34. C-38 and C-39 are orthogonal axes — a single annotation
  may satisfy both if it carries a directive AND a disqualification condition. Achieving C-34 in
  tabular format does not cross-satisfy C-39.

R15 builds on the strongest structural patterns from R12 (V-01 Finance-first tabular, V-02
step-block annotated, V-03 four-sub-steps, V-05 naive-trace foil) and R13 (C-34/C-35 grafts).
R15 grafts C-38 and C-39 onto those patterns via the field-annotation format
`[C-XX: directive — FAILS if: specific pattern]`.

**Variation axis choices:**
- Single-axis (3): Output format (tabular) / Output format (step-block) / Role sequence
- Combined (2): Output format (step-block) + Lifecycle emphasis / Role sequence + Phrasing register

---

## Round 15 Variation Map

| Var | Axis | Domain | Hypothesis | New Aspirationals Targeted |
|-----|------|--------|------------|---------------------------|
| V-01 | Output format (tabular, Finance → Sales → CS) | All three | Tabular column headers with C-34 (disqualification-condition) and C-36 (structural-format field) fused into same annotation; C-37 at pass headings; C-38/C-39 not achievable here | C-30, C-34, C-35, C-36, C-37 (tabular ceiling) |
| V-02 | Output format (step-block, single-pass) | Sales | Field annotations `[C-XX: directive — FAILS if: pattern]` achieve C-38 and C-39 simultaneously in every field label; this is the direct step-block analog of V-01's tabular ceiling | C-38, C-39 (new R15 ceiling) |
| V-03 | Role sequence (CS → Sales → Finance, tabular) | All three | CS-first surfaces SLA and escalation-path defects before commercial constraints; Finance last validates remediation-to-billing interactions; same column annotation density as V-01 | C-30, C-34, C-35, C-36, C-37 (tabular, CS-first) |
| V-04 | Output format (step-block) + Lifecycle emphasis (four sub-steps) | CS | Four mandatory sub-steps per operation make C-02/C-03 structurally unavoidable; sub-step labels carry C-38 + C-39 dual annotation; C-29 mutation verification forced by Sub-step 4 | C-38, C-39 (from step-block), C-02/C-03 density |
| V-05 | Role sequence (Finance-first) + Phrasing register (conversational + naive-trace foil) | All three | Naive-trace foil enumerates failure modes before instructions begin; Finance-first three-pass step-block with C-38/C-39 throughout; C-37 at pass headings; foil sharpest against Finance's hard numeric rules | C-37, C-38, C-39 |

---

## V-01 — Output Format: Tabular, Finance → Sales → CS

**Variation axis:** Output format (tabular three-pass)
**Hypothesis:** Tabular column headers carrying criterion ID, behavioral directive (C-30), and
specific disqualification condition (C-34) in the same annotation maximizes criterion-saturation
density: filling any cell mechanically satisfies its embedded criterion. Structural-format fields
(Starting State, Ending State) carry C-36 annotations. Pass headings carry C-37
criterion-consequence clauses. C-38 and C-39 are not achievable in tabular format — this
variation tests the tabular ceiling.
**Domain:** Finance / Sales / Customer Service (all three, Finance-first)
**Key criteria targeted beyond essentials:** C-09, C-10, C-11, C-13, C-15, C-16, C-17, C-19, C-20,
C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-34, C-35,
C-36, C-37

---

You are a state transition analyst. Hand-compile state transitions for the feature described above
using three sequential domain passes: **Finance first, then Sales, then Customer Service.**

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Prose is not a valid format for trace data — no prose substitutions [C-16].
- Blank cells are prohibited throughout. Write `none` if a field is genuinely absent — blank is
  never a permitted entry [C-32].
- Minimum 15 transition rows total across all three passes [C-26].
- Column headers are behavioral specifications — do not alter them.

---

### Pass 1 — Finance Domain [C-37: if the invariant registry for this pass is absent, the cross-domain aggregate in Section 4 cannot be completed — consequence: C-25 fails and golden threshold is unreachable]

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved →
Posted → Paid / Voided.

**State Transition Table — minimum 5 rows [C-17: a table with fewer than 5 rows fails C-17; a
narrative listing operations without a table fails C-16]**

**Reference row — template anchor; do not reproduce this row in output [C-24]:**

| Step [C-01a: sequential integer 1..N; FAILS if: non-sequential or alpha label used [C-34]] | Starting State [C-01b: declared lifecycle name only — directive: use vocabulary list above [C-30]; FAILS FORMAT: free-text description instead of declared state name, e.g., "invoice awaiting review" fails [C-36]] | Operation [C-01c: one imperative verb phrase — directive: one action per row, not a sequence [C-30]; FAILS if: two actions joined by "and" or "then" appear in a single cell [C-34]] | Ending State [C-01d: declared lifecycle name only — same structural constraint as Starting State [C-36]] | Preconditions [C-02a: list every condition that must hold; directive: name the specific attribute checked, not the general validity state; write "none" if genuinely absent [C-30]; FAILS if: vague condition stated without naming the attribute, e.g., "valid state" fails [C-34]] | Postconditions [C-02b: list every guarantee after success; write "none" if genuinely absent; directive: assert the changed attribute, not the ending state name [C-30]; FAILS if: postcondition merely restates the ending state in different words [C-34]] | Invariant 1 [C-03: real Finance business rule — directive: encode the operational consequence of violation [C-30]; FAILS if: structural placeholder used ("ID is not null", "record exists", "amount field present") [C-34]] | Invariant 2 [C-03: second Finance business rule — required; FAILS if: restates Invariant 1 in different wording [C-34]] |
|---|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver identity assigned | Status = Pending Approval; audit trail entry created | Invoice total must be positive after any line-item modification | Approver identity must be set before status transitions out of Draft |

**Trace table (Finance — minimum 5 rows) [C-17]:**

| Step [C-01a: sequential; FAILS if: non-sequential [C-34]] | Starting State [C-01b: declared name only [C-36]] | Operation [C-01c: one imperative phrase; FAILS if: compound [C-34]] | Ending State [C-01d: declared name only [C-36]] | Preconditions [C-02a: named attribute; write "none" if absent; FAILS if: vague [C-34]] | Postconditions [C-02b: changed attribute; write "none" if absent; FAILS if: restates ending state [C-34]] | Invariant 1 [C-03: real Finance rule; FAILS if: structural placeholder [C-34]] | Invariant 2 [C-03: second Finance rule — required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Finance Invariant Registry [C-35: this sub-section heading is load-bearing — if this table is absent, the cross-domain aggregate in Section 4 is incomplete; consequence: C-25 fails]**

Exclusion list — patterns that do not qualify as domain invariants [C-27]:
- "ID is not null"
- "record exists"
- "amount field is populated"

Valid qualifying example [C-20]: "Invoice total must remain positive after any line-item modification."

| Invariant ID | Description [C-07: real Finance business rule] | Derived From (Pass 1 Row #) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 1 Row … |
| INV-F-02 | … | Pass 1 Row … |

**Finance Defect Log — silent omissions invalidate this section [C-23: consequence: if no defect is logged, C-04 fails and composite cannot reach golden threshold]:**

| Defect ID [C-04a] | Type [C-04b: MissingPrecondition / InvalidTransition / InvariantViolation / RaceCondition] | Triggering Operation [C-04c — write "none" if not op-specific; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 2 — Sales Domain [C-37: invariant registry absent from this pass fails C-25 — consequence: cross-domain aggregate is incomplete]

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal →
Closed Won / Closed Lost.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a: sequential; FAILS if: non-sequential [C-34]] | Starting State [C-01b: declared name only [C-36]] | Operation [C-01c: one imperative phrase; FAILS if: compound [C-34]] | Ending State [C-01d: declared name only [C-36]] | Preconditions [C-02a: named attribute; write "none" if absent; FAILS if: vague [C-34]] | Postconditions [C-02b: changed attribute; write "none" if absent; FAILS if: restates ending state [C-34]] | Invariant 1 [C-03: real Sales rule; FAILS if: structural placeholder [C-34]] | Invariant 2 [C-03: second Sales rule — required] |
|---|---|---|---|---|---|---|---|
| 1 | Lead | Qualify Lead | Qualified Lead | Contact verified; lead score ≥ qualification threshold | Stage = Qualified Lead; owner assigned; close date set | Opportunity owner must be assigned before stage advances past Qualified Lead | Close date must be set before stage reaches Proposal |

**Trace table (Sales — minimum 5 rows) [C-17]:**

| Step [C-01a] | Starting State [C-01b [C-36]] | Operation [C-01c; FAILS if: compound [C-34]] | Ending State [C-01d [C-36]] | Preconditions [C-02a; FAILS if: vague [C-34]] | Postconditions [C-02b; FAILS if: restates ending state [C-34]] | Invariant 1 [C-03; FAILS if: structural [C-34]] | Invariant 2 [C-03: second required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Sales Invariant Registry [C-35: consequence — omission fails C-25]**

Same exclusion list applies [C-27]. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From (Pass 2 Row #) [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 2 Row … |
| INV-S-02 | … | Pass 2 Row … |

**Sales Defect Log — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 3 — Customer Service Domain [C-37: consequence — invariant registry absent fails C-25]

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved →
Closed / Reopened.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a] | Starting State [C-01b [C-36]] | Operation [C-01c; FAILS if: compound [C-34]] | Ending State [C-01d [C-36]] | Preconditions [C-02a; FAILS if: vague [C-34]] | Postconditions [C-02b; FAILS if: restates ending state [C-34]] | Invariant 1 [C-03; FAILS if: structural [C-34]] | Invariant 2 [C-03: second required] |
|---|---|---|---|---|---|---|---|
| 1 | New | Assign to Agent | Open | Agent capacity available; customer ID present | Agent ID set; SLA clock running; audit entry created | SLA clock must be active while status is Open or Pending | Customer ID must be non-null for any status other than Closed |

**Trace table (CS — minimum 5 rows) [C-17]:**

| Step [C-01a] | Starting State [C-01b [C-36]] | Operation [C-01c; FAILS if: compound [C-34]] | Ending State [C-01d [C-36]] | Preconditions [C-02a; FAILS if: vague [C-34]] | Postconditions [C-02b; FAILS if: restates ending state [C-34]] | Invariant 1 [C-03; FAILS if: structural [C-34]] | Invariant 2 [C-03: second required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**CS Invariant Registry [C-35: consequence — omission fails C-25]**

Same exclusion list [C-27]. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From (Pass 3 Row #) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 3 Row … |
| INV-C-02 | … | Pass 3 Row … |

**CS Defect Log — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Section 4 — Cross-Domain Invariant Register [C-25]

Aggregate every invariant from all three passes. Every entry must carry explicit cross-pass
derivation linkage — per-domain isolation without cross-pass links does not satisfy C-25.

| Invariant ID | Description | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 1 Row … |
| INV-S-01 | … | Pass 2 Row … |
| INV-C-01 | … | Pass 3 Row … |

Verify: total transition rows across all three passes ≥ 15 [C-26].

---

### Section 5 — Race Condition Analysis [C-08]

Name both concurrent operations explicitly — naming only the conflict outcome does not
qualify [C-28]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 — Op A first, then Op B:** State before A; state after A; state after B; conflict or
resolution named.

**Ordering 2 — Op B first, then Op A:** Describe fully and independently. Do not write "same as
above" or any cross-reference to Ordering 1 [C-21].

---

### Section 6 — Negative Path [C-09]

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c — write "none" if no change; never leave blank] | Named Error [C-09d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

**Mutation verification [C-29]:** Below the table, write an explicit confirmation sentence
declaring that [C-09c] = [C-09a] and that no field values were modified. Passive recording of the
same state value in the column does not satisfy C-29 — an independent declarative sentence is
required.

---

## V-02 — Output Format: Step-Block with C-38 + C-39 Dual Annotation

**Variation axis:** Output format (step-block single-pass)
**Hypothesis:** Field-level annotations carrying criterion ID, behavioral directive, AND specific
disqualification condition in the same label — format: `[C-XX: directive — FAILS if: pattern]` —
simultaneously satisfies C-38 (criterion-instruction fusion in step-block) and C-39
(disqualification-condition fusion in step-block). This is the step-block structural analog of
tabular V-01's C-30+C-34 column-header fusion. C-38 and C-39 are the two criteria only this
format can reach.
**Domain:** Sales (single pass — step-block is clearest in single-domain context)
**Key criteria targeted beyond essentials:** C-09, C-11, C-14, C-15, C-16, C-17, C-19, C-20,
C-21, C-22, C-23, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-38, C-39

---

You are a state transition analyst. Hand-compile state transitions for the feature described above.

**You are acting as a Sales domain expert.** Lifecycle: Lead → Qualified Lead → Opportunity →
Proposal → Closed Won / Closed Lost.

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Prose is not a valid format for trace data — no prose substitutions [C-16].
- Blank fields are prohibited throughout. Write `none` if a field is genuinely absent — blank is
  never a permitted entry [C-32].
- Minimum 5 step blocks [C-17].
- Field labels are behavioral specifications — do not alter them.

Output format: one numbered step block per operation. No tables. No prose paragraphs. Every
operation gets a block using the field structure below — filling each field label mechanically
satisfies its embedded criterion, directive, and disqualification guard simultaneously.

---

**Reference block — template anchor; do not reproduce this block in output [C-24]:**

```
Step [C-01a: sequential integer 1..N — directive: number blocks in ascending order — FAILS if: non-sequential number or alphabetic label used] [C-38][C-39]:
  Starting State   [C-01b: declared lifecycle name only — directive: use vocabulary list above — FAILS if: free-text description substituted for declared state name, e.g., "customer browsing opportunities" fails; must be "Lead" or declared equivalent] [C-38][C-39]:
  Operation        [C-01c: one imperative verb phrase — directive: one Sales action per block, not a sequence — FAILS if: two actions joined by "and" or "then" appear, e.g., "qualify and assign" fails; split into separate blocks] [C-38][C-39]:
  Ending State     [C-01d: declared lifecycle name only — directive: use vocabulary list above — FAILS if: ending state described rather than named, e.g., "moved to next stage" fails] [C-38][C-39]:
  Preconditions    [C-02a: list every condition that must hold before execution — directive: name the specific attribute checked; write "none" only if genuinely absent — FAILS if: vague condition without named attribute, e.g., "valid state" fails; must name the attribute, e.g., "lead score ≥ qualification threshold"] [C-38][C-39]:
  Postconditions   [C-02b: list every guarantee after success — directive: assert the changed attribute; write "none" if genuinely absent — FAILS if: postcondition merely restates the ending state, e.g., "now Qualified Lead" fails; must name the attribute changed, e.g., "owner assigned; close date set"] [C-38][C-39]:
  Invariant-1      [C-03: real Sales business rule — directive: encode the operational consequence of violation — FAILS if: structural placeholder used ("owner field not null", "record exists", "ID is populated")] [C-38][C-39]:
  Invariant-2      [C-03: second real Sales business rule — required; one invariant per block fails C-03 — FAILS if: Invariant-2 restates Invariant-1 in different wording] [C-38][C-39]:
```

Example reference block (do not copy into output):

```
Step 1:
  Starting State:   Lead
  Operation:        Qualify Lead
  Ending State:     Qualified Lead
  Preconditions:    Contact verified; lead score ≥ qualification threshold
  Postconditions:   Stage = Qualified Lead; owner assigned; close date set
  Invariant-1:      Opportunity owner must be assigned before stage advances past Qualified Lead
  Invariant-2:      Close date must be set before stage reaches Proposal
```

---

**Step blocks (Sales — minimum 5) [C-17: fewer than 5 complete blocks fails C-17]:**

*(generate step blocks here)*

---

**Invariant Summary**

List every distinct invariant declared across all step blocks.

Exclusion list — patterns that do not qualify [C-27]:
- "ID is not null"
- "owner field present"
- "record exists"

Valid qualifying example [C-20]: "Opportunity amount must remain ≥ 0 at all stages after
qualification."

| Invariant ID | Description [C-07: real Sales business rule] | Derived From Block # [C-13] |
|---|---|---|
| INV-S-01 | … | Block … |
| INV-S-02 | … | Block … |

---

**Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

```
Defect [C-04a: Defect-ID — directive: assign sequential ID — FAILS if: section is empty because happy path has no violations; identify edge-case or concurrent-write defect] [C-38][C-39]:
  Type           [C-04b: MissingPrecondition / InvalidTransition / InvariantViolation / RaceCondition — directive: choose the most specific type — FAILS if: type is omitted or set to "other"] [C-38][C-39]:
  Triggering Op  [C-04c: operation name — directive: name the operation that exposes the defect; write "none" if not op-specific — FAILS if: blank] [C-38][C-39]:
  Reason         [C-04d: business rule violated — directive: name the specific rule and how it breaks; write "none" if genuinely absent — FAILS if: vague reason like "system error" without naming the rule] [C-38][C-39]:
```

---

**Race Condition Analysis [C-08]**

Name both concurrent operations explicitly [C-28]:
- **Op A:** ___
- **Op B:** ___

```
Ordering 1 (A before B):
  State before A [C-01b — declared name]:
  State after A  [C-01d — declared name]:
  State after B  [C-01d — declared name]:
  Conflict/result:

Ordering 2 (B before A):
  [Describe fully — do not reference Ordering 1; do not write "same as above" [C-21]]
  State before B:
  State after B:
  State after A:
  Conflict/result:
```

---

**Negative Path [C-09]**

```
Negative-Step:
  Starting State     [C-09a: declared state name — directive: name the state before the attempt — FAILS if: described rather than named] [C-38][C-39]:
  Blocked Operation  [C-09b: imperative verb phrase — directive: name the specific operation rejected — FAILS if: blank] [C-38][C-39]:
  State After Rejection [C-09c: declared state name — directive: write "none" if no change — FAILS if: blank] [C-38][C-39]:
  Named Error        [C-09d: specific error or constraint violated — directive: name the rule; write "none" if genuinely absent — FAILS if: blank] [C-38][C-39]:
```

**Mutation verification [C-29]:** Immediately after the negative-step block, write one explicit
confirmation sentence declaring that [C-09c] = [C-09a] and that no field was modified. Passive
recording of the same state value in the block is not sufficient — an independent declarative
sentence is required.

---

## V-03 — Role Sequence: CS → Sales → Finance (Tabular)

**Variation axis:** Role sequence
**Hypothesis:** Customer Service first surfaces SLA violations, escalation-path defects, and
resolution-state inconsistencies before commercial constraints are layered. Finance last verifies
whether CS remediation states interact correctly with billing flows — a dependency direction
less often tested in Finance-first ordering and likely to expose different defect classes. Same
column annotation density as V-01 (C-30, C-34, C-36, C-37) but all three passes in reversed
order.
**Domain:** Customer Service / Sales / Finance (all three, CS-first)
**Key criteria targeted beyond essentials:** C-09, C-10, C-11, C-13, C-15, C-16, C-17, C-19,
C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-34,
C-35, C-36, C-37

---

You are a state transition analyst. Hand-compile state transitions for the feature described above
using three sequential domain passes: **Customer Service first, then Sales, then Finance.**

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Prose is not a valid format for trace data [C-16].
- Blank cells are prohibited. Write `none` if genuinely absent [C-32].
- Minimum 15 transition rows total across all three passes [C-26].
- Column headers are behavioral specifications — do not alter them.

---

### Pass 1 — Customer Service Domain [C-37: if the invariant registry for this pass is absent, the cross-domain aggregate in Section 4 cannot be completed — consequence: C-25 fails and golden threshold is unreachable]

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved →
Closed / Reopened.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — template anchor; do not reproduce in output [C-24]:**

| Step [C-01a: sequential 1..N; FAILS if: non-sequential [C-34]] | Starting State [C-01b: declared lifecycle name only — directive: use vocabulary above [C-30]; FAILS FORMAT: descriptive phrase used instead of declared state name [C-36]] | Operation [C-01c: one imperative verb phrase [C-30]; FAILS if: compound action joined by "and" or "then" [C-34]] | Ending State [C-01d: declared lifecycle name only — same structural constraint [C-36]] | Preconditions [C-02a: list every condition; directive: name the specific attribute [C-30]; write "none" if absent; FAILS if: vague without named attribute [C-34]] | Postconditions [C-02b: list every guarantee; write "none" if absent; directive: assert changed attribute [C-30]; FAILS if: restates ending state only [C-34]] | Invariant 1 [C-03: real CS business rule — directive: encode operational consequence [C-30]; FAILS if: structural placeholder used [C-34]] | Invariant 2 [C-03: second real CS rule — required; FAILS if: restates Invariant 1 [C-34]] |
|---|---|---|---|---|---|---|---|
| 1 | New | Assign to Agent | Open | Agent capacity available; customer ID present | Agent ID set; SLA clock running; audit entry created | SLA clock must be active while status is Open or Pending | Customer ID must be non-null for any non-Closed status |

**Trace table (CS — minimum 5 rows) [C-17]:**

| Step [C-01a] | Starting State [C-01b [C-36]] | Operation [C-01c; FAILS if: compound [C-34]] | Ending State [C-01d [C-36]] | Preconditions [C-02a; FAILS if: vague [C-34]] | Postconditions [C-02b; FAILS if: restates ending state [C-34]] | Invariant 1 [C-03; FAILS if: structural [C-34]] | Invariant 2 [C-03: second required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**CS Invariant Registry [C-35: this sub-section heading is load-bearing — if this table is absent, cross-domain aggregate cannot be completed; consequence: C-25 fails]**

Exclusion list [C-27]:
- "ID is not null"
- "record exists"
- "field is populated"

Valid qualifying example [C-20]: "SLA clock must be running throughout the Open and Pending states."

| Invariant ID | Description [C-07] | Derived From (Pass 1 Row #) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 1 Row … |
| INV-C-02 | … | Pass 1 Row … |

**CS Defect Log — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Op [C-04c — write "none" if not op-specific; never blank] | Reason [C-04d — write "none" if absent; never blank] |
|---|---|---|---|

---

### Pass 2 — Sales Domain [C-37: consequence — invariant registry absent from this pass fails C-25]

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal →
Closed Won / Closed Lost.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a] | Starting State [C-01b [C-36]] | Operation [C-01c; FAILS if: compound [C-34]] | Ending State [C-01d [C-36]] | Preconditions [C-02a; FAILS if: vague [C-34]] | Postconditions [C-02b; FAILS if: restates ending state [C-34]] | Invariant 1 [C-03; FAILS if: structural [C-34]] | Invariant 2 [C-03: second required] |
|---|---|---|---|---|---|---|---|
| 1 | Lead | Qualify Lead | Qualified Lead | Contact verified; score ≥ threshold | Stage = Qualified; owner assigned | Owner assigned before stage advances past Qualified Lead | Close date set before stage reaches Proposal |

**Trace table (Sales — minimum 5 rows) [C-17]:**

| Step [C-01a] | Starting State [C-01b [C-36]] | Operation [C-01c; FAILS if: compound [C-34]] | Ending State [C-01d [C-36]] | Preconditions [C-02a; FAILS if: vague [C-34]] | Postconditions [C-02b; FAILS if: restates ending state [C-34]] | Invariant 1 [C-03; FAILS if: structural [C-34]] | Invariant 2 [C-03: second required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Sales Invariant Registry [C-35: consequence — omission fails C-25]**

Same exclusion list [C-27]. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From (Pass 2 Row #) [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 2 Row … |
| INV-S-02 | … | Pass 2 Row … |

**Sales Defect Log — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Op [C-04c; never blank] | Reason [C-04d; never blank] |
|---|---|---|---|

---

### Pass 3 — Finance Domain [C-37: consequence — invariant registry absent fails C-25]

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved →
Posted → Paid / Voided.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a] | Starting State [C-01b [C-36]] | Operation [C-01c; FAILS if: compound [C-34]] | Ending State [C-01d [C-36]] | Preconditions [C-02a; FAILS if: vague [C-34]] | Postconditions [C-02b; FAILS if: restates ending state [C-34]] | Invariant 1 [C-03; FAILS if: structural [C-34]] | Invariant 2 [C-03: second required] |
|---|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver assigned | Status = Pending Approval; audit entry created | Invoice total positive after any line-item change | Approver set before status leaves Draft |

**Trace table (Finance — minimum 5 rows) [C-17]:**

| Step [C-01a] | Starting State [C-01b [C-36]] | Operation [C-01c; FAILS if: compound [C-34]] | Ending State [C-01d [C-36]] | Preconditions [C-02a; FAILS if: vague [C-34]] | Postconditions [C-02b; FAILS if: restates ending state [C-34]] | Invariant 1 [C-03; FAILS if: structural [C-34]] | Invariant 2 [C-03: second required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Finance Invariant Registry [C-35: consequence — omission fails C-25]**

Same exclusion list [C-27]. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From (Pass 3 Row #) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 3 Row … |
| INV-F-02 | … | Pass 3 Row … |

**Finance Defect Log — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Op [C-04c; never blank] | Reason [C-04d; never blank] |
|---|---|---|---|

---

### Section 4 — Cross-Domain Invariant Register [C-25]

Aggregate every invariant from all three passes. Every entry must carry explicit cross-pass
derivation linkage — per-domain isolation without cross-pass links does not satisfy C-25.

| Invariant ID | Description | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 1 Row … |
| INV-S-01 | … | Pass 2 Row … |
| INV-F-01 | … | Pass 3 Row … |

Verify: total rows ≥ 15 [C-26].

---

### Section 5 — Race Condition Analysis [C-08]

Name both concurrent operations explicitly [C-28]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 (Op A first):** State before A; state after A; state after B; conflict or resolution.

**Ordering 2 (Op B first):** Describe fully and independently — do not write "same as above" or
cross-reference Ordering 1 [C-21].

---

### Section 6 — Negative Path [C-09]

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c — write "none" if no change; never blank] | Named Error [C-09d — write "none" if absent; never blank] |
|---|---|---|---|

**Mutation verification [C-29]:** After the table, write an explicit confirmation sentence
declaring that [C-09c] = [C-09a] and that no field was modified. Passive recording does not
satisfy C-29 — an active declarative sentence is required.

---

## V-04 — Output Format (Step-Block) + Lifecycle Emphasis (Four Mandatory Sub-Steps)

**Variation axis:** Output format (step-block) + Lifecycle emphasis (four explicit sub-steps per
operation)
**Hypothesis:** Decomposing each operation into four mandatory sub-steps — (1) Precondition Check,
(2) Apply Operation, (3) Postcondition Check, (4) Invariant Verification — makes C-02 and C-03
structurally unavoidable: they cannot be omitted because they are named phases, not optional
columns. Sub-step labels carry C-38 + C-39 dual annotations throughout, achieving the new ceiling
criteria at every field. Sub-step 4 also forces active invariant verification per operation,
extending C-29-style confirmation structurally across all operations.
**Domain:** Customer Service (single pass — CS has the clearest SLA-arc for four-sub-step
lifecycle emphasis)
**Key criteria targeted beyond essentials:** C-09, C-10, C-13, C-15, C-16, C-17, C-19, C-22,
C-23, C-24, C-25, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-38, C-39

---

You are a state transition analyst. Hand-compile state transitions for the feature described above.

**You are acting as a Customer Service domain expert.** Lifecycle: New → Open → Pending →
Resolved → Closed / Reopened.

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Blank fields are prohibited throughout. Write `none` if a field is genuinely absent [C-32].
- Minimum 5 complete operation records [C-17].
- Every operation record must include all four sub-steps. An operation record with a missing
  sub-step invalidates that record.
- Prose is not a valid format for trace data [C-16].

---

### Operation Records

One complete record per operation. Minimum 5 records [C-17]. Use the structure below for every
record — do not reorder, merge, or abbreviate sub-steps.

**Reference record — template anchor; do not reproduce in output [C-24]:**

```
--- Operation Record N ---------------------------------------------------------------
Header:
  Starting State  [C-01b: declared CS lifecycle name only — directive: use vocabulary above
                   — FAILS if: free-text description substituted for declared state name,
                   e.g., "customer waiting for agent" fails; use "New" or declared equivalent]
                   [C-38][C-39]:
  Operation       [C-01c: one imperative verb phrase — directive: one CS action per record
                   — FAILS if: compound action joined by "and" or "then" appears, e.g.,
                   "assign and open" fails; split into separate records] [C-38][C-39]:
  Ending State    [C-01d: declared CS lifecycle name only — directive: use vocabulary above
                   — FAILS if: ending state described rather than named, e.g., "now assigned"
                   fails] [C-38][C-39]:

  Sub-step 1 — Precondition Check [C-02a: directive: verify all listed conditions before
  advancing to Sub-step 2 — FAILS if: conditions are vague ("valid state") without naming
  the specific attribute checked] [C-38][C-39]:
    Preconditions [C-02a — list every condition; write "none" if genuinely absent; never blank]:
      Agent capacity available; customer ID present

  Sub-step 2 — Apply Operation [C-01c: directive: record the action taken and intermediate
  state produced — FAILS if: sub-step is omitted entirely or replaced with prose] [C-38][C-39]:
    Action taken:    Ticket assigned to agent
    State after:     Open

  Sub-step 3 — Postcondition Check [C-02b: directive: verify each guarantee is asserted;
  assert the changed attribute — FAILS if: postcondition merely restates the ending state
  without naming the changed attribute] [C-38][C-39]:
    Postconditions [C-02b — list every guarantee; write "none" if genuinely absent; never blank]:
      Agent ID set; SLA clock running; audit entry created

  Sub-step 4 — Invariant Verification [C-03: directive: check every declared invariant;
  minimum 2 domain-meaningful invariants per record — FAILS if: fewer than 2 checked;
  FAILS if: structural placeholder ("ID is not null") substituted for real CS business rule]
  [C-38][C-39]:
    INV-C-01: SLA clock must be active while status is Open or Pending — HOLDS / VIOLATED
    INV-C-02: Customer ID must be non-null while status not in {Closed} — HOLDS / VIOLATED
    Derivation: INV-C-01 and INV-C-02 sourced from this record [C-13]

--- End of Record -------------------------------------------------------------------
```

**Operation records (CS — minimum 5) [C-17]:**

*(generate operation records here)*

---

### Invariant Register [C-25]

Aggregate all invariants declared in Sub-step 4 across all records. Every entry must carry the
record number it was derived from [C-13].

Exclusion list — patterns that do not qualify [C-27]:
- "ID is not null"
- "record exists"
- "field is populated"

Valid qualifying example [C-20]: "SLA clock must be running while ticket status is Open or Pending."

| Invariant ID | Description [C-07: real CS business rule] | Derived From Record # [C-13] |
|---|---|---|
| INV-C-01 | … | Record … |
| INV-C-02 | … | Record … |

---

### Reachability Annotation [C-10]

List every state transition NOT covered in the operation records above. For each omitted
transition, state the rationale. Silent omissions do not qualify — every reachable but untested
path must be explicitly named.

| Omitted Transition | Rationale |
|---|---|
| [From] → [To] via [Op] | … |

---

### Defect Log [C-04] — silent omissions invalidate this section [C-23]

```
Defect [C-04a: Defect-ID — directive: assign sequential ID; at least one entry required
        — FAILS if: section is empty] [C-38][C-39]:
  Type           [C-04b: MissingPrecondition / InvalidTransition / InvariantViolation /
                  RaceCondition — directive: choose most specific type — FAILS if: blank or
                  "other"] [C-38][C-39]:
  Triggering Op  [C-04c: operation name — directive: name the operation; write "none" if
                  not op-specific — FAILS if: blank] [C-38][C-39]:
  Reason         [C-04d: business rule violated — directive: name the specific rule; write
                  "none" if genuinely absent — FAILS if: vague reason without named rule]
                  [C-38][C-39]:
```

---

### Race Condition Analysis [C-08]

Name both concurrent operations explicitly [C-28]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 (Op A first):** Apply the four-sub-step structure: precondition state; A executes;
intermediate state; B executes; final state; conflict or resolution named.

**Ordering 2 (Op B first):** Describe fully and independently. Do not write "same as above" or
cross-reference Ordering 1 [C-21].

---

### Negative Path [C-09]

One rejected operation using the four-sub-step structure:

```
--- Negative Path Record ----------------------------------------------------------
Header:
  Starting State     [C-09a: declared state name — directive: name before the attempt
                      — FAILS if: described rather than named] [C-38][C-39]:
  Blocked Operation  [C-09b: imperative verb phrase — directive: name the rejected op
                      — FAILS if: blank] [C-38][C-39]:

  Sub-step 1 — Precondition Failure Check [C-02a — directive: name the failed precondition
  — FAILS if: vague] [C-38][C-39]:
    Failed precondition: …

  Sub-step 2 — Operation Rejected [C-01c — directive: confirm rejection at gate]:
    Action taken: none — operation blocked at precondition gate

  Sub-step 3 — State After Rejection [C-09c — directive: name the state; write "none" if
  no change — FAILS if: blank] [C-38][C-39]:
    State After Rejection: …

  Sub-step 4 — Mutation Verification [C-29: directive: write an explicit sentence confirming
  no field was mutated; declare that [C-09c] = [C-09a] and all field values are unchanged
  — FAILS if: only the same state value is recorded without an independent declarative
  sentence] [C-38][C-39]:
    Verification: [write explicit confirmation sentence here]

Named Error [C-09d: specific error raised; write "none" if absent — FAILS if: blank]
            [C-38][C-39]: …

--- End of Negative Path ----------------------------------------------------------
```

---

## V-05 — Role Sequence (Finance-First) + Phrasing Register (Conversational + Naive-Trace Foil)

**Variation axis:** Role sequence (Finance-first three-pass) + Phrasing register (conversational
+ naive-trace foil)
**Hypothesis:** Opening with a concrete description of what a naive hand-compilation fails to
capture — vague preconditions, structural invariants, single-direction race analysis, passive
mutation recording — primes the model to avoid those failure modes before any instruction is
given. Finance-first maximizes invariant depth. Three-pass step-block format with
`[C-XX: directive — FAILS if: pattern]` annotations achieves C-38 + C-39 throughout. Pass
headings carry C-37 criterion-consequence annotations. The foil is sharpest with Finance because
hard numeric rules make naive placeholders immediately recognizable.
**Domain:** Finance / Sales / Customer Service (Finance-first)
**Key criteria targeted beyond essentials:** C-09, C-10, C-15, C-16, C-17, C-19, C-21, C-22,
C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-31, C-32, C-33, C-35, C-37, C-38, C-39

---

You are going to hand-compile state transitions for the feature described above, acting as three
sequential domain experts: **Finance first, then Sales, then Customer Service.**

Before you start, here is what a naive trace looks like — and why it fails:

> A naive trace writes "starting state → operation → ending state" in three columns, leaves
> precondition fields blank when nothing obvious comes to mind, declares invariants like
> "ID is not null" or "record exists," describes one direction of a concurrent operation and
> notes "the reverse is symmetric," and records the same state value in Starting State and
> State After Rejection without writing a verification sentence. It covers the happy path. It
> does not catch the defects that matter to domain experts.

Your trace will be different. Here is the contract.

**Hard constraints — any violation invalidates the artifact [C-19]:**
- Blank fields are prohibited. If you are about to leave a field blank, write `none` instead —
  blank and missing are indistinguishable to a reviewer [C-32].
- Minimum 5 step blocks per pass [C-17].
- No prose substituted for trace data [C-16].

---

### Pass 1 — Finance Domain [C-37: if the invariant registry for this pass is absent or contains only structural placeholders, the cross-domain aggregate cannot be completed — consequence: C-25 fails and golden threshold is unreachable]

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved →
Posted → Paid / Voided.

One thing the naive trace always does: writes "status = valid" as a precondition and "ID is not
null" as an invariant. Both are structural — they tell a Finance controller nothing. A real
Finance invariant names the constraint that would trigger an audit finding: "Invoice total must
remain positive after any line-item modification." Start there.

**Reference block — template only; do not reproduce in output [C-24]:**

```
Step [C-01a: sequential 1..N — directive: number blocks sequentially
      — FAILS if: non-sequential or alpha label] [C-38][C-39]:
  Starting State  [C-01b: declared Finance lifecycle name — directive: use vocabulary above
                   — FAILS if: free-text description substituted for declared state name]
                   [C-38][C-39]:
  Operation       [C-01c: one imperative verb phrase — directive: one Finance action per block
                   — FAILS if: compound action ("submit and notify") appears] [C-38][C-39]:
  Ending State    [C-01d: declared Finance lifecycle name — FAILS if: described rather than
                   named] [C-38][C-39]:
  Preconditions   [C-02a: every condition that must hold — directive: name the specific
                   attribute checked; write "none" if absent — FAILS if: vague ("valid state")
                   without specific attribute] [C-38][C-39]:
  Postconditions  [C-02b: every guarantee after success — directive: assert the changed
                   attribute; write "none" if absent — FAILS if: postcondition restates ending
                   state name without identifying the changed attribute] [C-38][C-39]:
  Invariant-1     [C-03: real Finance business rule — directive: encode what breaks in the
                   Finance flow if violated — FAILS if: structural placeholder ("ID is not null",
                   "amount present") used] [C-38][C-39]:
  Invariant-2     [C-03: second Finance business rule — required — FAILS if: restates
                   Invariant-1] [C-38][C-39]:
```

**Finance step blocks (minimum 5) [C-17]:**

*(generate Finance step blocks here)*

---

**Finance Invariant Registry [C-35: consequence — if this registry is absent or contains only structural placeholders, Pass 1 contributes nothing to the cross-domain aggregate and C-25 fails]**

Exclusion list [C-27]:
- "ID is not null"
- "record exists"
- "amount field populated"

Valid qualifying example [C-20]: "Invoice total must remain positive after any line-item modification."

| Invariant ID | Description [C-07] | Derived From Block # [C-13] |
|---|---|---|
| INV-F-01 | … | Block … |
| INV-F-02 | … | Block … |

**Finance Defect Log — the naive trace omits this section because "nothing is wrong on the happy path" — that is not analysis [C-23]:**

```
Finance-Defect:
  Defect ID    [C-04a: sequential ID — at least one required]:
  Type         [C-04b: MissingPrecondition / InvalidTransition / InvariantViolation / RaceCondition]:
  Triggering Op [C-04c: operation name; write "none" if not op-specific; never blank]:
  Reason       [C-04d: business rule violated; write "none" if absent; never blank]:
```

---

### Pass 2 — Sales Domain [C-37: consequence — invariant registry absent from this pass fails C-25]

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal →
Closed Won / Closed Lost.

The naive Sales trace consistently misses: (1) close-date preconditions absent for late-stage
transitions, (2) ownership assignment skipped after qualification, (3) re-opening a Closed Won
opportunity without manager approval. These are the defect classes to look for.

**Reference block — do not reproduce in output [C-24]:**

```
Step [C-01a: sequential — FAILS if: non-sequential] [C-38][C-39]:
  Starting State  [C-01b: declared Sales state — directive: use vocabulary above — FAILS if:
                   free-text] [C-38][C-39]:
  Operation       [C-01c: one Sales action — directive: one action per block — FAILS if:
                   compound] [C-38][C-39]:
  Ending State    [C-01d: declared Sales state — FAILS if: described] [C-38][C-39]:
  Preconditions   [C-02a: specific attribute; write "none" if absent — FAILS if: vague]
                   [C-38][C-39]:
  Postconditions  [C-02b: changed attribute; write "none" if absent — FAILS if: restates
                   ending state] [C-38][C-39]:
  Invariant-1     [C-03: real Sales rule — FAILS if: structural placeholder] [C-38][C-39]:
  Invariant-2     [C-03: second required — FAILS if: restates Invariant-1] [C-38][C-39]:
```

**Sales step blocks (minimum 5) [C-17]:**

*(generate Sales step blocks here)*

---

**Sales Invariant Registry [C-35: consequence — missing registry fails C-25]**

Same exclusion list [C-27]. Link each to source block [C-13].

| Invariant ID | Description [C-07] | Derived From Block # [C-13] |
|---|---|---|
| INV-S-01 | … | Block … |
| INV-S-02 | … | Block … |

**Sales Defect Log [C-23]:**

```
Sales-Defect:
  Defect ID    [C-04a]:
  Type         [C-04b]:
  Triggering Op [C-04c — never blank]:
  Reason       [C-04d — never blank]:
```

---

### Pass 3 — Customer Service Domain [C-37: consequence — invariant registry absent fails C-25]

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved →
Closed / Reopened.

The naive CS trace misses: (1) SLA clock not starting on assignment, (2) re-opening a Closed
ticket without verifying the resolution was incomplete, (3) escalation status not resetting when
a ticket is reassigned to a new agent. Keep these in view.

**Reference block — do not reproduce in output [C-24]:**

```
Step [C-01a: sequential — FAILS if: non-sequential] [C-38][C-39]:
  Starting State  [C-01b: declared CS state — FAILS if: free-text] [C-38][C-39]:
  Operation       [C-01c: one CS action — FAILS if: compound] [C-38][C-39]:
  Ending State    [C-01d: declared CS state — FAILS if: described] [C-38][C-39]:
  Preconditions   [C-02a: specific attribute; write "none" if absent — FAILS if: vague]
                   [C-38][C-39]:
  Postconditions  [C-02b: changed attribute; write "none" if absent — FAILS if: restates
                   ending state] [C-38][C-39]:
  Invariant-1     [C-03: real CS rule — FAILS if: structural] [C-38][C-39]:
  Invariant-2     [C-03: second required — FAILS if: restates Invariant-1] [C-38][C-39]:
```

**CS step blocks (minimum 5) [C-17]:**

*(generate CS step blocks here)*

---

**CS Invariant Registry [C-35: consequence — missing fails C-25]**

Same exclusion list [C-27]. Link each to source block [C-13].

| Invariant ID | Description [C-07] | Derived From Block # [C-13] |
|---|---|---|
| INV-C-01 | … | Block … |
| INV-C-02 | … | Block … |

**CS Defect Log [C-23]:**

```
CS-Defect:
  Defect ID    [C-04a]:
  Type         [C-04b]:
  Triggering Op [C-04c — never blank]:
  Reason       [C-04d — never blank]:
```

---

### Section 4 — Cross-Domain Invariant Register [C-25]

Aggregate every invariant from all three passes. Every entry must carry explicit cross-pass
derivation linkage — per-domain isolation does not satisfy C-25.

| Invariant ID | Description | Derived From (Pass + Block) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 1 Block … |
| INV-S-01 | … | Pass 2 Block … |
| INV-C-01 | … | Pass 3 Block … |

The naive trace stops here. It does not verify cross-pass totals. Verify: total step blocks
across all three passes ≥ 15 [C-26].

---

### Section 5 — Race Condition Analysis [C-08]

The naive trace describes one interleaving direction and notes "the reverse is symmetric." That
is avoidance — symmetry is an assertion, not analysis. Two orderings of the same concurrent pair
often produce asymmetric outcomes; that asymmetry is what this section exists to surface.

Name both concurrent operations explicitly [C-28]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 (A then B):**

```
State before A:
State after A:
State after B:
Conflict/resolution:
```

**Ordering 2 (B then A):**

Do not write "same as above," "symmetric," or any reference to Ordering 1 [C-21]. Write it
out completely. If outcomes are genuinely identical, demonstrate it by producing the identical
text — do not assert it.

```
State before B:
State after B:
State after A:
Conflict/resolution:
```

---

### Section 6 — Negative Path [C-09]

One rejected operation. The naive trace writes "the operation fails" in prose. That does not
qualify.

```
Negative Step:
  Starting State     [C-09a: declared state name — directive: name the state before the
                      attempt — FAILS if: described rather than named] [C-38][C-39]:
  Blocked Operation  [C-09b: imperative verb phrase — directive: name the specific op
                      rejected — FAILS if: blank] [C-38][C-39]:
  State After Rejection [C-09c: declared state name — directive: write "none" if no change
                         — FAILS if: blank] [C-38][C-39]:
  Named Error        [C-09d: specific error raised — directive: name the rule violated;
                      write "none" if genuinely absent — FAILS if: blank] [C-38][C-39]:
```

**Active mutation verification [C-29]:** After the block, write one sentence: explicitly confirm
that [C-09c] = [C-09a] and that no field was modified. Writing the same state value in both
fields is passive recording — the naive trace does exactly that and calls it verification. Write
the independent declarative sentence.
