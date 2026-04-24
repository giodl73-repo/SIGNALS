# trace-state Variate — Round 12
**Date:** 2026-03-15
**Rubric:** v26 / outer quest v10 (C-01..C-33; 25 aspirational criteria; golden: all essential pass AND composite >= 80)
**Situation:** R12 introduces two new aspirational criteria extracted from pairwise experiments on the nil-value and blank-cell structural problem:

- **C-32** (Mandatory-fill prohibition on absence-eligible fields): an explicit anti-blank instruction ("never leave blank") must appear IN ADDITION to any nil-value token; nil-value instruction alone does not qualify.
- **C-33** (Sub-element nil-value annotation): nil-value instruction must appear WITHIN a sub-criterion annotation (e.g., `[C-02a — write "none" if genuinely absent]`), not at parent-field level or in a preamble.

These two criteria are designed to coexist: C-33 creates the sub-element annotation slot and C-32 fills it with the anti-blank prohibition. The challenge is distinguishing them from C-22 (nil-value at parent field level) and ensuring neither collapses into the other.

R12 is a clean-slate round against v26. R11 used a different rubric track (HANDOFF/VOCABULARY architecture). These five variations are designed fresh for v26.

---

## Round 12 Variation Map

| Var | Axis | Hypothesis | Key Aspirationals Targeted |
|-----|------|------------|---------------------------|
| V-01 | Role sequence (Finance → Sales → CS) | Finance-first anchors hard numeric invariants; downstream passes inherit and extend, increasing C-25/C-26 density | C-09, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 |
| V-02 | Output format (numbered step blocks + maximum criterion annotation) | Step-block format with criterion IDs in every field label achieves higher C-11/C-14/C-31 saturation than table format | C-09, C-11, C-14, C-15, C-16, C-17, C-19, C-20, C-22, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33 |
| V-03 | Lifecycle emphasis (four explicit sub-steps per operation) | Separating precondition-check, apply-operation, postcondition-check, invariant-verify into mandatory sub-steps forces C-02/C-03/C-29 saturation structurally | C-09, C-10, C-13, C-17, C-19, C-22, C-23, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 |
| V-04 | Role sequence + output format (CS → Finance → Sales, schema-level write-time enforcement) | CS-first surfaces user-facing defects; Finance validates with hard constraints; C-14 schema structure makes compliance mechanically unavoidable | C-09, C-11, C-12, C-14, C-15, C-16, C-17, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 |
| V-05 | Phrasing register + inertia framing (conversational + "naive trace" foil) | Naming failure modes of casual tracing before giving instructions increases defect diversity and race condition depth | C-09, C-10, C-12, C-15, C-16, C-18, C-19, C-20, C-21, C-22, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33 |

---

## V-01 — Role Sequence: Finance → Sales → CS

**Variation axis:** Role sequence
**Hypothesis:** Running Finance first forces the hardest numeric invariant declarations (monetary floors, approval chains, posting rules) before softer relationship-state domains execute. Sales and CS passes can then cross-reference Finance invariants, naturally driving C-25 (cross-domain invariant register) and C-26 (cross-pass aggregate floor) saturation.
**Domain:** Finance / Sales / Customer Service (all three)
**Key criteria targeted beyond essentials:** C-09, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are a state transition analyst. Hand-compile state transitions for the feature described above using three sequential domain passes: **Finance first, then Sales, then Customer Service.**

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- No prose substitutions: every output element appears in its designated schema cell; prose is not a valid format for trace data [C-16].
- Blank cells are prohibited across every column. Write `none` if a field is genuinely absent — blank is not a permitted entry [C-32].
- Minimum 15 transition rows across all three passes combined [C-26].

---

### Pass 1 — Finance Domain

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved → Posted → Paid / Voided.

**State Transition Table** — minimum 5 rows [C-17: explicit row floor; qualitative "be thorough" does not satisfy this]

**Reference row — template anchor; do not include this row in output [C-24]:**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — never skip] |
|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver assigned | Status = Pending Approval; audit entry created | INV-F-01: total > 0; INV-F-02: approver not null |

**Trace table (Finance):**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**Finance Invariants** — link each to the transition row that generated it [C-13]:

Exclusion list — these patterns do not qualify [C-27]:
- "ID is not null"
- "record exists"
- "amount field is populated"

Valid qualifying example [C-20]: "Invoice total must remain positive after any line-item modification."

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 1 Row … |
| INV-F-02 | … | Pass 1 Row … |

**Finance Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 2 — Sales Domain

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal → Closed Won / Closed Lost.

**State Transition Table** — minimum 5 rows [C-17]

**Reference row — do not include in output [C-24]:**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — never skip] |
|---|---|---|---|---|---|---|
| 1 | Lead | Qualify | Qualified Lead | Contact verified; score ≥ threshold | Stage = Qualified; owner assigned | INV-S-01: owner assigned; INV-S-02: close date set |

**Trace table (Sales):**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**Sales Invariants** — same exclusion list and qualifying example apply [C-27][C-20]. Link each to source row [C-13]:

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 2 Row … |
| INV-S-02 | … | Pass 2 Row … |

**Sales Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 3 — Customer Service Domain

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved → Closed / Reopened.

**State Transition Table** — minimum 5 rows [C-17]

**Reference row — do not include in output [C-24]:**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — never skip] |
|---|---|---|---|---|---|---|
| 1 | New | Assign to Agent | Open | Agent capacity available | Agent ID set; SLA clock started | INV-C-01: SLA active; INV-C-02: customer ID not null |

**Trace table (CS):**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**CS Invariants** — exclusion list and qualifying example apply. Link each to source row [C-13]:

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 3 Row … |
| INV-C-02 | … | Pass 3 Row … |

**CS Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Cross-Domain Invariant Register [C-25]

Aggregate every invariant from all three passes. Every entry must carry an explicit cross-pass derivation link. Per-domain isolation does not satisfy C-25.

| Invariant ID | Description | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 1 Row … |
| INV-S-01 | … | Pass 2 Row … |
| INV-C-01 | … | Pass 3 Row … |

Verify: total transition rows across all passes ≥ 15 [C-26].

---

### Race Condition Analysis [C-08]

Name both concurrent operations explicitly — naming only the conflict outcome does not qualify [C-28]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 — Op A first, then Op B:** Describe state before A, state after A, state after B. Name the conflict or resolution.

**Ordering 2 — Op B first, then Op A:** Describe fully and independently. Do not write "same as above" or any cross-reference to Ordering 1 [C-21].

---

### Negative Path [C-09]

One rejected operation with all four elements:

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c — write "none" if no change; never leave blank] | Named Error [C-09d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

After the table: actively verify that [C-09c] is identical to [C-09a] — write an explicit verification statement confirming no mutation occurred. Passively recording the same value in [C-09c] does not satisfy this requirement [C-29].

---

## V-02 — Output Format: Numbered Step Blocks with Maximum Criterion Annotation

**Variation axis:** Output format
**Hypothesis:** Replacing table rows with named step blocks and embedding criterion IDs directly inside every field label achieves C-11 and C-14 simultaneously: every cell filled mechanically satisfies its assigned criterion because the label contains the full directive. C-31 sub-element decomposition is forced at the block level without needing separate decomposition instructions.
**Domain:** Sales (single pass — step-block format is most legible in single-domain context)
**Key criteria targeted beyond essentials:** C-09, C-11, C-14, C-15, C-16, C-17, C-19, C-20, C-22, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are a state transition analyst. Hand-compile state transitions for the feature described above.

**You are acting as a Sales domain expert.** Lifecycle: Lead → Qualified Lead → Opportunity → Proposal → Closed Won / Closed Lost.

**HARD RULES — violation of any rule invalidates the artifact [C-19]:**
- Prose is not a valid output format for trace data — no prose substitutions [C-16].
- Blank fields are prohibited throughout. Write `none` if a field is genuinely absent — blank is never an acceptable entry for any field in any step block [C-32].
- Minimum 5 operation step blocks [C-17].

Output format: one numbered step block per operation. No tables. No prose paragraphs. Every operation gets a block using the field structure below — filling each field mechanically satisfies its embedded criterion.

---

**Reference block — template anchor; do not reproduce this block in output [C-24]:**

```
Step [C-01a: sequential number, 1..N; required]:
  Starting State    [C-01b: name of the lifecycle state the object occupies before this operation — use declared vocabulary only; required]:
  Operation         [C-01c: one imperative verb phrase naming the action; required]:
  Ending State      [C-01d: name of the lifecycle state after the operation completes; required]:
  Preconditions     [C-02a: list every condition that must hold before execution; write "none" if genuinely absent; never leave blank]:
  Postconditions    [C-02b: list every condition that holds immediately after success; write "none" if genuinely absent; never leave blank]:
  Invariant-1       [C-03: first domain invariant — must encode a real Sales business rule, not a structural placeholder; see exclusion list]:
  Invariant-2       [C-03: second domain invariant — required; a block with only one invariant fails C-03; write a second distinct business rule]:
```

---

**Step blocks (Sales — minimum 5) [C-17: if fewer than 5 blocks are present, this section fails C-17]:**

*(generate step blocks here)*

---

**Invariant Summary**

List every distinct invariant from all step blocks.

Exclusion list — patterns that do not qualify as domain invariants [C-27]:
- "ID is not null"
- "record exists"
- "field is populated"

Valid qualifying example [C-20]: "Opportunity amount must remain ≥ 0 at all stages after qualification."

| Invariant ID | Description [C-07: real Sales business rule] | Appears In Step |
|---|---|---|
| INV-01 | … | Step … |

---

**Defect Log [C-04] — at least one entry required:**

```
Defect [C-04a: Defect-ID]:
  Type              [C-04b: missing precondition check / invalid state transition / invariant violation / race condition]:
  Triggering Op     [C-04c: operation name; write "none" if not operation-specific; never leave blank]:
  Reason            [C-04d: business rule violated or state corrupted; write "none" if genuinely absent; never leave blank]:
```

---

**Race Condition Analysis [C-08]**

Name both concurrent operations explicitly [C-28]:
- **Op A:** ___
- **Op B:** ___

```
Ordering 1 (A before B):
  State before A:      …
  State after A:       …
  State after B:       …
  Conflict or result:  …

Ordering 2 (B before A):
  [Describe fully — do not reference Ordering 1; do not write "same as above" [C-21]]
  State before B:      …
  State after B:       …
  State after A:       …
  Conflict or result:  …
```

---

**Negative Path [C-09]**

```
Negative-Step [C-09a — Starting State]:
Negative-Step [C-09b — Blocked Operation]:
Negative-Step [C-09c — State After Rejection (write "none" if no change; never leave blank)]:
Negative-Step [C-09d — Named Error (write "none" if genuinely absent; never leave blank)]:
```

Mutation verification [C-29 — active verification required]: Immediately after the negative-step block, write one explicit confirmation sentence declaring that the state in [C-09c] is identical to [C-09a] and that no field was modified. Recording the same state value in the block column is passive representation — an independent declarative sentence is required.

---

## V-03 — Lifecycle Emphasis: Four Explicit Sub-Steps Per Operation

**Variation axis:** Lifecycle emphasis
**Hypothesis:** Decomposing each operation into four mandatory sub-steps — (1) Check Preconditions, (2) Apply Operation, (3) Check Postconditions, (4) Verify Invariants — makes C-02 and C-03 structurally unavoidable. They cannot be omitted because they are named phases, not optional columns. Sub-step 4 also forces active invariant verification per operation, extending C-29-style confirmation across all operations rather than only the negative path.
**Domain:** Customer Service (single pass — lifecycle emphasis works best with a domain that has a clear remediation arc)
**Key criteria targeted beyond essentials:** C-09, C-10, C-13, C-17, C-19, C-22, C-23, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are a state transition analyst. Hand-compile state transitions for the feature described above.

**You are acting as a Customer Service domain expert.** Lifecycle: New → Open → Pending → Resolved → Closed / Reopened.

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Blank cells are prohibited throughout. Write `none` where a field is genuinely absent — blank is not a permitted response for any labeled field [C-32].
- Minimum 5 complete operation records [C-17].
- Every operation record must include all four sub-steps. An operation record with a missing sub-step invalidates that record.

---

### Operation Records

Produce one complete record per operation. Minimum 5 records [C-17]. Use the structure below for every record — do not reorder, merge, or abbreviate sub-steps.

**Reference record — template anchor; do not reproduce this record in output [C-24]:**

```
--- Operation Record N -----------------------------------------------------------
Starting State [C-01b]:  New
Operation [C-01c]:       Assign to Agent
Ending State [C-01d]:    Open

  Sub-step 1 — Precondition Check
    Preconditions [C-02a: list all; write "none" if genuinely absent; never leave blank]:
      Agent capacity available; customer ID not null

  Sub-step 2 — Apply Operation
    Action taken:  Ticket assigned; status updated to Open
    State after:   Open

  Sub-step 3 — Postcondition Check
    Postconditions [C-02b: list all; write "none" if genuinely absent; never leave blank]:
      Agent ID set; SLA clock running; audit entry created

  Sub-step 4 — Invariant Verification [C-03: min 2 per record — never skip]
    INV-C-01: SLA clock is running while status IN {Open, Pending} — HOLDS
    INV-C-02: Customer ID is not null when status IN {Open, Pending, Resolved} — HOLDS
    Derived: INV-C-01 sourced from this record [C-13]
----------------------------------------------------------------------------------
```

**Operation records (Customer Service — minimum 5):**

*(generate records here)*

---

### Invariant Register [C-25]

Aggregate all invariants declared across Sub-step 4 of all records. Every entry must carry the record number it was derived from [C-13].

Exclusion list — these patterns do not qualify [C-27]:
- "ID is not null"
- "record exists"
- "field is populated"

Valid qualifying example [C-20]: "SLA clock must be running while ticket status is Open or Pending."

| Invariant ID | Description [C-07: real CS business rule] | Derived From [C-13] |
|---|---|---|
| INV-C-01 | … | Record … |
| INV-C-02 | … | Record … |

---

### Reachability Annotation [C-10]

List every state transition NOT covered in the operation records above. For each omitted transition, state the rationale. Silent omissions do not qualify — every reachable but untested path must be explicitly named.

| Omitted Transition | Rationale |
|---|---|
| [From] → [To] via [Op] | … |

---

### Defect Log [C-04] — silent omissions invalidate this section [C-23]

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Race Condition Analysis [C-08]

Name both concurrent operations explicitly [C-28]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 (Op A first):** Use the four-sub-step structure for the interleaving: precondition state; A executes; intermediate state; B executes; final state; conflict or resolution.

**Ordering 2 (Op B first):** Describe fully. Do not write "same as above" or cross-reference Ordering 1 [C-21].

---

### Negative Path [C-09]

One rejected operation. Use the four-sub-step structure:

```
--- Negative Path Record ---------------------------------------------------------
Starting State [C-09a]:     …
Blocked Operation [C-09b]:  …

  Sub-step 1 — Precondition Failure Check
    Preconditions [C-02a — write "none" if no precondition applies; never leave blank]:
      Failed precondition: …

  Sub-step 2 — Operation Rejected
    Action taken: none — operation blocked at precondition gate

  Sub-step 3 — State After Rejection
    State After Rejection [C-09c — write "none" if no change; never leave blank]: …

  Sub-step 4 — Mutation Verification [C-29: active confirmation required]
    Verification: Explicitly confirm that no field was mutated. Declare that
    [C-09c] = [C-09a] and that all field values are identical to pre-operation
    values. Passive recording of the same state value does not satisfy C-29.

Named Error [C-09d — write "none" if genuinely absent; never leave blank]: …
----------------------------------------------------------------------------------
```

---

## V-04 — Role Sequence + Output Format: CS → Finance → Sales with Schema-Level Write-Time Enforcement

**Variation axis:** Role sequence + output format (combined)
**Hypothesis:** Reversing role order to CS → Finance → Sales surfaces user-facing defects first (CS), then Finance validates them with hard monetary and approval constraints, and Sales closes the loop on pipeline-stage invariants. Combined with column headers designed so that filling any cell mechanically satisfies its assigned criterion (C-14), rubric compliance becomes structurally unavoidable — not instruction-dependent.
**Domain:** Customer Service / Finance / Sales (all three, reversed order)
**Key criteria targeted beyond essentials:** C-09, C-11, C-12, C-14, C-15, C-16, C-17, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are a state transition analyst. Hand-compile state transitions for the feature described above across three domain passes: **Customer Service first, then Finance, then Sales.**

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Prose is not a valid format for trace data — no prose substitutions [C-16].
- Blank cells are prohibited. Write `none` if a field is genuinely absent — blank is never a permitted entry [C-32].
- Minimum 15 transition rows total across all three passes [C-26].

**Schema design note:** Every column header below contains the full behavioral directive for that field. Filling a cell mechanically satisfies the embedded criterion — you cannot fill the cell without complying. Do not alter column headers.

---

### Pass 1 — Customer Service Domain

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved → Closed / Reopened.

**State Transition Table** — minimum 5 rows [C-17: fewer than 5 rows fails C-17]

**Reference row — template anchor; do not reproduce in output [C-24]:**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: name the lifecycle state the object occupies before this operation — use declared vocabulary only] | Operation [C-01c: imperative verb phrase naming the single action taken] | Ending State [C-01d: name the lifecycle state the object transitions into] | Preconditions [C-02a — list every condition that must hold before execution; write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — list every condition that holds after success; write "none" if genuinely absent; never leave blank] | Invariant 1 [C-03: first CS business-rule invariant — must encode a real domain constraint, not a structural fact; see exclusion list] | Invariant 2 [C-03: second CS business-rule invariant — required; a row with only one invariant fails C-03] |
|---|---|---|---|---|---|---|---|
| 1 | New | Assign to Agent | Open | Agent capacity available; customer ID present | Agent ID set; SLA clock running; audit entry created | SLA clock is active while status IN {Open, Pending} | Customer ID is not null when status not in {Closed} |

**Trace table (CS — minimum 5 rows) [C-17]:**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only] | Operation [C-01c: imperative verb phrase] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariant 1 [C-03: real CS business constraint — see exclusion list] | Invariant 2 [C-03: second CS business constraint — required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**CS Invariant Register:**

Exclusion list [C-27] — minimum two disqualifying patterns:
- "ID is not null"
- "record exists"
- "field is populated"

Valid qualifying example [C-20]: "SLA clock must be running throughout the Open and Pending states."

| Invariant ID | Description [C-07] | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 1 Row … |
| INV-C-02 | … | Pass 1 Row … |

**CS Defect Log — at least one entry required; silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b: missing precondition check / invalid transition / invariant violation / race condition] | Triggering Operation [C-04c — write "none" if not op-specific; never leave blank] | Reason [C-04d — explain business rule violated; write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 2 — Finance Domain

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved → Posted → Paid / Voided.

**State Transition Table** — minimum 5 rows [C-17]

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only] | Operation [C-01c: imperative verb phrase] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariant 1 [C-03: real Finance business constraint — see exclusion list] | Invariant 2 [C-03: second Finance business constraint — required] |
|---|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver assigned | Status = Pending Approval; audit entry created | Invoice total must be positive after any line-item change | Approver must be set before status leaves Draft |

**Trace table (Finance — minimum 5 rows) [C-17]:**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only] | Operation [C-01c: imperative verb phrase] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariant 1 [C-03: real Finance business constraint] | Invariant 2 [C-03: second Finance business constraint — required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Finance Invariant Register:**

Same exclusion list [C-27] and qualifying example [C-20] apply. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 2 Row … |

**Finance Defect Log — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 3 — Sales Domain

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal → Closed Won / Closed Lost.

**State Transition Table** — minimum 5 rows [C-17]

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only] | Operation [C-01c: imperative verb phrase] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariant 1 [C-03: real Sales business constraint — see exclusion list] | Invariant 2 [C-03: second Sales business constraint — required] |
|---|---|---|---|---|---|---|---|
| 1 | Lead | Qualify | Qualified Lead | Contact verified; score ≥ threshold | Stage = Qualified; owner assigned | Opportunity owner must be set before stage advances past Qualified | Close date must be set before stage reaches Proposal |

**Trace table (Sales — minimum 5 rows) [C-17]:**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only] | Operation [C-01c: imperative verb phrase] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariant 1 [C-03: real Sales business constraint] | Invariant 2 [C-03: second Sales business constraint — required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Sales Invariant Register:**

Same exclusion list and qualifying example apply. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 3 Row … |

**Sales Defect Log — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Cross-Domain Invariant Register [C-25]

Aggregate every invariant from all three passes. Every entry must carry explicit cross-pass derivation linkage — per-domain isolation does not satisfy C-25.

| Invariant ID | Description | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 1 Row … |
| INV-F-01 | … | Pass 2 Row … |
| INV-S-01 | … | Pass 3 Row … |

Verify: total transition rows across all passes ≥ 15 [C-26].

---

### Race Condition Analysis [C-08]

Name both concurrent operations explicitly [C-28]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 (Op A → Op B):** State before A; state after A; state after B; conflict or resolution.

**Ordering 2 (Op B → Op A):** Describe fully and independently. Do not write "same as above" or any cross-reference to Ordering 1 [C-21]. Both orderings must be independently described — asymmetric conflict outcomes require it.

---

### Negative Path [C-09]

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c — write "none" if no change; never leave blank] | Named Error [C-09d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

**Mutation verification [C-29]:** Below the table, write an explicit confirmation statement: declare that the state in [C-09c] is identical to [C-09a] and that no field values were modified. Passive recording of the unchanged state in the column does not satisfy C-29 — an active verification directive is required.

---

## V-05 — Phrasing Register + Inertia Framing: Conversational with "Naive Trace" Foil

**Variation axis:** Phrasing register + inertia framing (combined)
**Hypothesis:** Opening with a concrete description of what a naive hand-compilation fails to capture — blank cells, single-direction race analysis, passive state recording, structural "invariants" — primes the model to actively avoid those failure modes. A conversational register achieves higher C-16/C-19/C-21/C-29 saturation than formal prohibitions alone, because the foil makes the failure modes concrete before the instructions begin.
**Domain:** Finance (single pass — inertia framing is sharpest when the domain has hard numeric rules that naive traces underspecify)
**Key criteria targeted beyond essentials:** C-09, C-10, C-12, C-15, C-16, C-18, C-19, C-20, C-21, C-22, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are going to hand-compile state transitions for the feature described above, acting as a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved → Posted → Paid / Voided.

Before you start, here is what a naive trace looks like — and why it fails:

> A naive trace writes "starting state → operation → ending state" in prose, leaves precondition cells blank when nothing obvious comes to mind, declares invariants like "ID is not null," and describes a race condition in one direction only with a note that "the reverse is symmetric." It feels complete because it covers the happy path. It is not complete. It will not catch the defects that matter.

Your trace will be different. Here is what you will produce.

---

**Hard constraint:** Blank cells are prohibited — this is not a stylistic preference. If you are about to leave a cell blank, write `none` instead. A blank cell and a missing value are indistinguishable to a reviewer, so blank is never acceptable [C-32]. Violating this constraint invalidates the artifact [C-19].

---

### State Transition Table

Minimum 5 rows [C-17]. No prose — every operation gets its own row, not a paragraph. If you find yourself writing a sentence instead of filling a cell, stop and restructure.

**Reference row — template only; do not copy this row into your output [C-24]:**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariant 1 [C-03: a real Finance business rule — see exclusion list below] | Invariant 2 [C-03: second real Finance business rule — required; a row with one invariant fails C-03] |
|---|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver assigned | Status = Pending Approval; audit entry created | Invoice total must be positive after any line-item change | Approver identity must be set before status leaves Draft |

**Trace rows (Finance — minimum 5) [C-17]:**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; never leave blank] | Invariant 1 [C-03: real Finance business rule] | Invariant 2 [C-03: second real Finance business rule — required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

---

### Invariant Summary

List every distinct invariant from the trace table.

Here is what does NOT qualify [C-27] — name at least two disqualifying patterns explicitly:
- "ID is not null" — structural, not a business rule
- "record exists" — a database constraint, not a Finance rule
- "status field is populated" — a schema constraint, not a domain rule

Here is what DOES qualify [C-20]: "Invoice total must remain positive after any line-item modification." This encodes a Finance business rule that would matter to a controller, not just a schema validator.

| Invariant ID | Description [C-07: real Finance business rule] | Source Step |
|---|---|---|
| INV-01 | … | Step … |

---

### Defect Log [C-04]

At least one entry. If you are tempted to leave this empty because the happy path has no defects — that is exactly the thinking the naive trace uses. Look for missing precondition checks, invalid transitions on edge cases, invariant violations on concurrent writes.

| Defect ID [C-04a] | Type [C-04b — choose one: missing precondition check / invalid state transition / invariant violation / race condition] | Triggering Operation [C-04c — write "none" if not operation-specific; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Reachability Annotation [C-10]

The naive trace silently omits the paths it does not test. Here, explicitly name every state transition NOT included in the table above, and say why you left it out. A transition is only considered covered if it appears as a row. If it is not a row, it belongs here. Silent omissions do not satisfy this section.

| Omitted Transition | Rationale |
|---|---|
| [From State] → [To State] via [Operation] | … |

---

### Race Condition Analysis [C-08]

The naive trace describes one direction and notes "the reverse is symmetric." That is avoidance, not analysis. Two orderings of the same concurrent operation pair often produce asymmetric outcomes — that asymmetry is exactly what this section exists to surface.

Name both concurrent operations explicitly — do not name only the conflict [C-28]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 (Op A first, then Op B):**
Describe: state before A; state after A; state after B; what conflict or resolution results.

**Ordering 2 (Op B first, then Op A):**
Describe in full. Do not write "same as above," "symmetric," or any reference to Ordering 1 [C-21]. Write it out completely as if Ordering 1 did not exist. If outcomes are genuinely identical, demonstrate it by producing the identical text — do not assert it.

---

### Negative Path [C-09]

One rejected operation. The naive trace often writes "the operation fails" in prose. That does not qualify.

| Starting State [C-09a — the state before the attempt is made] | Blocked Operation [C-09b — the operation that is rejected] | State After Rejection [C-09c — write "none" if no change; never leave blank] | Named Error [C-09d — the specific error raised; write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

**Active mutation verification [C-29]:** After the table, write one sentence that explicitly confirms no state mutation occurred — confirm that [C-09c] = [C-09a] and that all field values are identical before and after the rejected operation attempt. Writing the same state in both columns is passive recording. The naive trace omits this sentence entirely. Write it.
