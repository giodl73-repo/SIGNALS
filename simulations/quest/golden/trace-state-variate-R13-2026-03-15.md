# trace-state Variate — Round 13
**Date:** 2026-03-15
**Rubric:** v27 / outer quest v11 (C-01..C-35; 27 aspirational criteria; golden: all essential pass AND composite >= 80)
**Situation:** R13 introduces two new aspirational criteria extracted from R12 pairwise evidence:

- **C-34** (Disqualification-condition fusion in field labels): a field label or inline annotation co-locates the criterion ID with the *specific pattern that fails* that criterion — not a behavioral directive (C-30) but the exact disqualifying pattern. C-30 and C-34 are orthogonal axes; a single annotation may earn both if it carries a directive AND a disqualification condition.
- **C-35** (Section-label criterion-consequence fusion): a section heading co-locates a criterion ID with a conditional consequence clause, making enforcement visible at structural navigation level *before* any field in the section is read. Distinct from C-23 (consequence in section prose) and C-19 (artifact-level consequence).

R13 builds on R12 V-01 through V-05 (which were clean-slate variations against the v26 rubric). R13 variations graft C-34 and C-35 onto the strongest R12 structural patterns.

**Variation axis choices:**
- Single-axis (3): Role sequence / Output format / Lifecycle emphasis
- Combined (2): Role sequence + Output format / Phrasing register + Inertia framing

---

## Round 13 Variation Map

| Var | Axis | Domain | Hypothesis | New Aspirationals Targeted |
|-----|------|--------|------------|---------------------------|
| V-01 | Role sequence (Finance → Sales → CS) | All three | Finance-first disqualification conditions in column-header annotations make the scoring bar self-documenting at field level (C-34); C-35 absent to isolate C-34's contribution | C-34, C-09, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 |
| V-02 | Output format (step blocks + C-35 section labels) | Sales | Consequence clauses embedded in section headings achieve C-35 at navigation level; C-34 absent from field labels to isolate C-35 contribution | C-35, C-09, C-11, C-14, C-15, C-16, C-17, C-19, C-20, C-22, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33 |
| V-03 | Lifecycle emphasis (four sub-steps per op, C-34 on sub-element labels) | Customer Service | Sub-step labels are natural C-34 carriers — each already names the criterion it serves; appending the disqualifying pattern makes enforcement granular to the sub-element level; C-35 absent | C-34, C-09, C-10, C-13, C-17, C-19, C-22, C-23, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 |
| V-04 | Role sequence + output format (CS → Finance → Sales, C-34 + C-35 combined) | All three | CS-first surfaces user-facing defects; Finance validates with hard constraints; C-34 in field labels + C-35 in section headings creates dual-layer enforcement: what fails at the field AND what fails at the section | C-34, C-35, C-09, C-11, C-12, C-14, C-15, C-16, C-17, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33 |
| V-05 | Phrasing register + inertia framing (conversational + "naive trace" foil, C-34 + C-35 combined) | Finance | Conversational foil primes against failure modes before instructions begin; section labels carry C-35 consequence clauses (enforcement visible at navigation level); field labels carry C-34 disqualification conditions (exact failing pattern named at the cell) | C-34, C-35, C-09, C-10, C-12, C-15, C-16, C-18, C-19, C-20, C-21, C-22, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33 |

---

## V-01 — Role Sequence: Finance → Sales → CS (C-34: Disqualification Conditions in Field Labels)

**Variation axis:** Role sequence (Finance → Sales → CS)
**Hypothesis:** Finance-first ordering places the hardest numeric disqualification conditions in field labels before softer relational domains run. Every column header that carries a criterion ID also names the specific pattern that fails that criterion (C-34). Sales and CS passes inherit the same disqualification vocabulary. C-35 is deliberately absent from section labels in this variation to isolate C-34's independent contribution.
**Domain:** Finance / Sales / Customer Service (all three)
**Key criteria targeted beyond essentials:** C-34 (new), C-09, C-11, C-12, C-13, C-15, C-17, C-19, C-20, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are a state transition analyst. Hand-compile state transitions for the feature described above using three sequential domain passes: **Finance first, then Sales, then Customer Service.**

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- No prose substitutions: every output element appears in its designated schema cell; prose is not a valid format for trace data [C-16].
- Blank cells are prohibited across every column. Write `none` if a field is genuinely absent — blank is not a permitted entry [C-32].
- Minimum 15 transition rows across all three passes combined [C-26].

---

### Pass 1 — Finance Domain

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved → Posted → Paid / Voided.

**State Transition Table** — minimum 5 rows [C-17: qualitative "be thorough" does not satisfy this criterion — an explicit numeric floor is required]

**Reference row — template anchor; do not include this row in output [C-24: reproducing this row verbatim in output does not qualify as a completed trace row]:**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify — blank is not equivalent to "none"; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify — blank is not equivalent to "none"; never leave blank] | Invariants Checked [C-03: min 2 per pass — "ID is not null" does not qualify for C-03; never skip] |
|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver assigned | Status = Pending Approval; audit entry created | INV-F-01: Invoice total must remain positive after any line-item change; INV-F-02: Approver must be set before status leaves Draft |

**Trace table (Finance):**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify — blank is not "none"; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify — blank is not "none"; never leave blank] | Invariants Checked [C-03: min 2 per pass — "ID is not null" does not qualify; never skip] |
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

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; "see above" does not qualify — name the specific operation; never leave blank] | Reason [C-04d — write "none" if genuinely absent; "operation blocked" without naming the violated rule does not qualify; never leave blank] |
|---|---|---|---|

---

### Pass 2 — Sales Domain

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal → Closed Won / Closed Lost.

**State Transition Table** — minimum 5 rows [C-17: qualitative "be thorough" does not satisfy this criterion]

**Reference row — do not include in output [C-24: reproducing this row verbatim does not qualify as a completed trace row]:**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariants Checked [C-03: min 2 per pass — "owner is assigned" as a bare fact without a context clause does not qualify; never skip] |
|---|---|---|---|---|---|---|
| 1 | Lead | Qualify | Qualified Lead | Contact verified; score >= threshold | Stage = Qualified; owner assigned | INV-S-01: Owner must be assigned before stage advances past Qualified; INV-S-02: Close date must be set before stage reaches Proposal |

**Trace table (Sales):**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariants Checked [C-03: min 2 per pass — "owner is assigned" without a context clause does not qualify; never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**Sales Invariants** — same exclusion list and qualifying example apply [C-27][C-20]. Link each to source row [C-13]:

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 2 Row … |
| INV-S-02 | … | Pass 2 Row … |

**Sales Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; "see above" does not qualify; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 3 — Customer Service Domain

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved → Closed / Reopened.

**State Transition Table** — minimum 5 rows [C-17: qualitative "be thorough" does not satisfy this criterion]

**Reference row — do not include in output [C-24: reproducing this row verbatim does not qualify]:**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariants Checked [C-03: min 2 per pass — "ticket ID exists" does not qualify for C-03; never skip] |
|---|---|---|---|---|---|---|
| 1 | New | Assign to Agent | Open | Agent capacity available | Agent ID set; SLA clock started | INV-C-01: SLA clock must be active while status is Open or Pending; INV-C-02: Customer ID must be set when status is not Closed |

**Trace table (CS):**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariants Checked [C-03: min 2 per pass — "ticket ID exists" does not qualify; never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**CS Invariants** — same exclusion list and qualifying example apply. Link each to source row [C-13]:

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 3 Row … |
| INV-C-02 | … | Pass 3 Row … |

**CS Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; "see above" does not qualify; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Cross-Domain Invariant Register [C-25]

Aggregate every invariant from all three passes. Every entry must carry an explicit cross-pass derivation link — per-domain isolation does not satisfy C-25.

| Invariant ID | Description | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 1 Row … |
| INV-S-01 | … | Pass 2 Row … |
| INV-C-01 | … | Pass 3 Row … |

Verify: total transition rows across all passes >= 15 [C-26].

---

### Race Condition Analysis [C-08]

Name both concurrent operations explicitly — naming only the conflict outcome does not qualify [C-28: naming only the conflict outcome does not qualify — both Op A and Op B must be explicitly identified]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 — Op A first, then Op B:** Describe state before A, state after A, state after B. Name the conflict or resolution.

**Ordering 2 — Op B first, then Op A:** Describe fully and independently. Do not write "same as above" or any cross-reference to Ordering 1 [C-21].

---

### Negative Path [C-09]

One rejected operation with all four elements:

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c — write "none" if no change; leaving blank does not qualify; never leave blank] | Named Error [C-09d — write "none" if genuinely absent; "operation failed" without naming the specific error does not qualify for C-34; never leave blank] |
|---|---|---|---|

After the table: actively verify that [C-09c] is identical to [C-09a] — write an explicit verification statement confirming no mutation occurred. Passively recording the same value in [C-09c] does not satisfy this requirement [C-29: passively recording the same state value in the column does not satisfy C-29 — an active declarative sentence is required].

---

## V-02 — Output Format: Numbered Step Blocks with C-35 Section Labels

**Variation axis:** Output format (numbered step blocks with consequence clauses embedded in section headings)
**Hypothesis:** Moving consequence clauses INTO the section heading itself — as `[C-ID: consequence clause]` fused annotations — achieves C-35 at structural navigation level. A reader scanning section headers encounters the enforcement consequence before reading any field content. C-34 (disqualification conditions in field labels) is deliberately absent from column annotations to isolate C-35's independent contribution.
**Domain:** Sales (single pass)
**Key criteria targeted beyond essentials:** C-35 (new), C-09, C-11, C-14, C-15, C-16, C-17, C-19, C-20, C-22, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33

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

### Step Blocks (Sales) [C-17: if fewer than 5 complete step blocks are present, C-17 fails — an explicit numeric floor cannot be satisfied qualitatively]

*(generate step blocks here)*

---

### Invariant Summary [C-27: if every listed invariant matches an exclusion-list pattern, this section fails C-27]

List every distinct invariant from all step blocks.

Exclusion list — patterns that do not qualify as domain invariants:
- "ID is not null"
- "record exists"
- "field is populated"

Valid qualifying example [C-20]: "Opportunity amount must remain >= 0 at all stages after qualification."

| Invariant ID | Description [C-07: real Sales business rule] | Appears In Step |
|---|---|---|
| INV-01 | … | Step … |

---

### Defect Log [C-04: if no defect entry is present, C-04 fails — the happy path alone does not constitute a complete trace]

```
Defect [C-04a: Defect-ID]:
  Type              [C-04b: missing precondition check / invalid state transition / invariant violation / race condition]:
  Triggering Op     [C-04c: operation name; write "none" if not operation-specific; never leave blank]:
  Reason            [C-04d: business rule violated or state corrupted; write "none" if genuinely absent; never leave blank]:
```

---

### Race Condition Analysis [C-08: if Ordering 2 cross-references Ordering 1 instead of being independently described, C-08 fails]

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

### Negative Path [C-09: if fewer than 4 elements are present — starting state, blocked operation, post-rejection state, named error — C-09 fails]

```
Negative-Step [C-09a — Starting State]:
Negative-Step [C-09b — Blocked Operation]:
Negative-Step [C-09c — State After Rejection (write "none" if no change; never leave blank)]:
Negative-Step [C-09d — Named Error (write "none" if genuinely absent; never leave blank)]:
```

Mutation verification [C-29 — active verification required]: Immediately after the negative-step block, write one explicit confirmation sentence declaring that the state in [C-09c] is identical to [C-09a] and that no field was modified. Recording the same state value in the block column is passive representation — an independent declarative sentence is required.

---

## V-03 — Lifecycle Emphasis: Four Sub-Steps with C-34 on Sub-Element Labels (CS)

**Variation axis:** Lifecycle emphasis (four explicit sub-steps per operation, with C-34 disqualification conditions embedded in sub-step labels)
**Hypothesis:** Each sub-step label in the four-sub-step decomposition is a natural C-34 carrier — it already names the criterion for that sub-step's output, so appending the disqualifying pattern co-locates ID + disqualification at the most granular enforcement level (sub-element, not parent column). C-35 is deliberately absent from section headings to isolate C-34's contribution at the sub-element level.
**Domain:** Customer Service (single pass)
**Key criteria targeted beyond essentials:** C-34 (new), C-09, C-10, C-13, C-17, C-19, C-22, C-23, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33

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
    Preconditions [C-02a — write "none" if genuinely absent; never leave blank;
    "data is valid" as a precondition does not qualify for C-34 — list specific
    conditions, not generic assertions]:
      Agent capacity available; customer ID not null

  Sub-step 2 — Apply Operation
    Action taken:  Ticket assigned; status updated to Open
    State after:   Open

  Sub-step 3 — Postcondition Check
    Postconditions [C-02b — write "none" if genuinely absent; never leave blank]:
      Agent ID set; SLA clock running; audit entry created

  Sub-step 4 — Invariant Verification [C-03: min 2 per record — "ticket ID exists"
  does not qualify for C-03; structural facts are not domain invariants; never skip]
    INV-C-01: SLA clock is running while status IN {Open, Pending} — HOLDS
    INV-C-02: Customer ID is not null when status IN {Open, Pending, Resolved} — HOLDS
    Derived: INV-C-01 sourced from this record [C-13]
----------------------------------------------------------------------------------
```

**Operation records (Customer Service — minimum 5) [C-17]:**

*(generate records here)*

---

### Invariant Register [C-25] — silent omissions invalidate this section [C-23]

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
| [From] -> [To] via [Op] | … |

---

### Defect Log [C-04] — silent omissions invalidate this section [C-23]

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; "see above" does not qualify for C-34 — name the specific operation; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Race Condition Analysis [C-08]

Name both concurrent operations explicitly [C-28: naming only the conflict outcome does not qualify — both Op A and Op B must be identified]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 (Op A first):** Use the four-sub-step structure for the interleaving: precondition state; A executes; intermediate state; B executes; final state; conflict or resolution.

**Ordering 2 (Op B first):** Describe fully and independently. Do not write "same as above" or cross-reference Ordering 1 [C-21].

---

### Negative Path [C-09]

One rejected operation. Use the four-sub-step structure:

```
--- Negative Path Record ---------------------------------------------------------
Starting State [C-09a]:     …
Blocked Operation [C-09b]:  …

  Sub-step 1 — Precondition Failure Check
    Preconditions [C-02a — write "none" if no precondition applies; never leave blank;
    "invalid data" as a failing precondition does not qualify for C-34 — name the
    specific condition that failed]:
      Failed precondition: …

  Sub-step 2 — Operation Rejected
    Action taken: none — operation blocked at precondition gate

  Sub-step 3 — State After Rejection
    State After Rejection [C-09c — write "none" if no change; leaving blank does not
    qualify; never leave blank]: …

  Sub-step 4 — Mutation Verification [C-29: passively recording the same state value
  does not satisfy C-29 — an active declarative sentence is required]
    Verification: Explicitly confirm that no field was mutated. Declare that
    [C-09c] = [C-09a] and that all field values are identical to pre-operation values.
    Passive recording of the same state value does not satisfy C-29.

Named Error [C-09d — write "none" if genuinely absent; "operation failed" without
naming the specific error does not qualify for C-34; never leave blank]: …
----------------------------------------------------------------------------------
```

---

## V-04 — Role Sequence + Output Format: CS → Finance → Sales with C-34 and C-35 Combined

**Variation axis:** Role sequence (CS → Finance → Sales) + output format (table with dual-layer annotation)
**Hypothesis:** CS-first surfaces user-facing defects; Finance validates with hard monetary and approval constraints; Sales closes on pipeline invariants. Combined with C-34 (disqualification conditions in column headers) AND C-35 (consequence clauses in section headings), every structural element carries dual enforcement: what pattern fails the criterion at the field level, and what happens to the section if the criterion is not met at the navigation level.
**Domain:** Customer Service / Finance / Sales (all three, CS first)
**Key criteria targeted beyond essentials:** C-34 + C-35 (both new), C-09, C-11, C-12, C-14, C-15, C-16, C-17, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are a state transition analyst. Hand-compile state transitions for the feature described above across three domain passes: **Customer Service first, then Finance, then Sales.**

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Prose is not a valid format for trace data — no prose substitutions [C-16].
- Blank cells are prohibited. Write `none` if a field is genuinely absent — blank is never a permitted entry [C-32].
- Minimum 15 transition rows total across all three passes [C-26].

**Schema design note:** Every column header below contains the full behavioral directive AND the disqualifying pattern for that field. Filling a cell mechanically satisfies the embedded criterion — you cannot fill the cell without complying. Do not alter column headers.

---

### Pass 1 — Customer Service Domain [C-05: if states and operations are not recognizable in the CS domain, C-05 fails]

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved → Closed / Reopened.

#### State Transition Table (CS) [C-17: if fewer than 5 rows are present, C-17 fails for this pass]

**Reference row — template anchor; do not reproduce in output [C-24: reproducing this row verbatim does not qualify as a completed trace row]:**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only — a description instead of a state name does not qualify] | Operation [C-01c: imperative verb phrase — a noun phrase does not qualify] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify — blank is not "none"; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariant 1 [C-03: first CS business-rule invariant — "ticket ID exists" does not qualify for C-03; see exclusion list] | Invariant 2 [C-03: second CS business-rule invariant — required; a row with only one invariant fails C-03] |
|---|---|---|---|---|---|---|---|
| 1 | New | Assign to Agent | Open | Agent capacity available; customer ID present | Agent ID set; SLA clock running; audit entry created | SLA clock is active while status IN {Open, Pending} | Customer ID is not null when status not in {Closed} |

**Trace table (CS — minimum 5 rows):**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only — a description does not qualify] | Operation [C-01c: imperative verb phrase] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariant 1 [C-03: real CS business constraint — "ticket ID exists" does not qualify] | Invariant 2 [C-03: second CS business constraint — required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

#### CS Invariant Register [C-13: if derivation links are absent, every unlabeled invariant fails C-13]

Exclusion list [C-27] — minimum two disqualifying patterns:
- "ID is not null"
- "record exists"
- "field is populated"

Valid qualifying example [C-20]: "SLA clock must be running throughout the Open and Pending states."

| Invariant ID | Description [C-07] | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 1 Row … |
| INV-C-02 | … | Pass 1 Row … |

#### CS Defect Log [C-04: if this section is empty, C-04 fails — silent omissions also invalidate this section]

| Defect ID [C-04a] | Type [C-04b: one of — missing precondition check / invalid transition / invariant violation / race condition] | Triggering Operation [C-04c — write "none" if not op-specific; "see above" does not qualify; never leave blank] | Reason [C-04d — write "none" if genuinely absent; "error occurred" without naming the violated rule does not qualify; never leave blank] |
|---|---|---|---|

---

### Pass 2 — Finance Domain [C-05: if states and operations are not recognizable in the Finance domain, C-05 fails]

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved → Posted → Paid / Voided.

#### State Transition Table (Finance) [C-17: if fewer than 5 rows are present, C-17 fails for this pass]

**Reference row — do not reproduce in output [C-24: reproducing this row verbatim does not qualify]:**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only] | Operation [C-01c: imperative verb phrase] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariant 1 [C-03: real Finance business constraint — "amount field is populated" does not qualify for C-03; see exclusion list] | Invariant 2 [C-03: second Finance business constraint — required] |
|---|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver assigned | Status = Pending Approval; audit entry created | Invoice total must be positive after any line-item change | Approver must be set before status leaves Draft |

**Trace table (Finance — minimum 5 rows):**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only] | Operation [C-01c: imperative verb phrase] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariant 1 [C-03: real Finance business constraint — "amount field is populated" does not qualify] | Invariant 2 [C-03: second Finance business constraint — required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

#### Finance Invariant Register [C-13: if derivation links are absent, every unlabeled invariant fails C-13]

Same exclusion list [C-27] and qualifying example [C-20] apply. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 2 Row … |

#### Finance Defect Log [C-04: if this section is empty, C-04 fails — silent omissions invalidate this section]

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; "see above" does not qualify; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 3 — Sales Domain [C-05: if states and operations are not recognizable in the Sales domain, C-05 fails]

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal → Closed Won / Closed Lost.

#### State Transition Table (Sales) [C-17: if fewer than 5 rows are present, C-17 fails for this pass]

**Reference row — do not reproduce in output [C-24: reproducing this row verbatim does not qualify]:**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only] | Operation [C-01c: imperative verb phrase] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariant 1 [C-03: real Sales business constraint — "owner is assigned" as a bare fact without a context clause does not qualify] | Invariant 2 [C-03: second Sales business constraint — required] |
|---|---|---|---|---|---|---|---|
| 1 | Lead | Qualify | Qualified Lead | Contact verified; score >= threshold | Stage = Qualified; owner assigned | Opportunity owner must be set before stage advances past Qualified | Close date must be set before stage reaches Proposal |

**Trace table (Sales — minimum 5 rows):**

| Step [C-01a: sequential 1..N] | Starting State [C-01b: lifecycle state name only] | Operation [C-01c: imperative verb phrase] | Ending State [C-01d: lifecycle state name only] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariant 1 [C-03: real Sales business constraint] | Invariant 2 [C-03: second Sales business constraint — required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

#### Sales Invariant Register [C-13: if derivation links are absent, every unlabeled invariant fails C-13]

Same exclusion list and qualifying example apply. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 3 Row … |

#### Sales Defect Log [C-04: if this section is empty, C-04 fails — silent omissions invalidate this section]

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write "none" if not op-specific; "see above" does not qualify; never leave blank] | Reason [C-04d — write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Cross-Domain Invariant Register [C-25: if entries lack cross-pass derivation links, C-25 fails — per-domain isolation does not satisfy this criterion]

Aggregate every invariant from all three passes. Every entry must carry explicit cross-pass derivation linkage.

| Invariant ID | Description | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 1 Row … |
| INV-F-01 | … | Pass 2 Row … |
| INV-S-01 | … | Pass 3 Row … |

Verify: total transition rows across all passes >= 15 [C-26].

---

### Race Condition Analysis [C-08: if Ordering 2 cross-references Ordering 1 instead of being independently described, C-08 fails]

Name both concurrent operations explicitly [C-28: naming only the conflict outcome does not qualify — both Op A and Op B must be explicitly named]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 (Op A → Op B):** State before A; state after A; state after B; conflict or resolution.

**Ordering 2 (Op B → Op A):** Describe fully and independently. Do not write "same as above" or any cross-reference to Ordering 1 [C-21]. Both orderings must be independently described — asymmetric conflict outcomes require it.

---

### Negative Path [C-09: if fewer than 4 elements are present — starting state, blocked operation, post-rejection state, named error — C-09 fails]

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c — write "none" if no change; leaving blank does not qualify; never leave blank] | Named Error [C-09d — write "none" if genuinely absent; "operation blocked" without a specific error name does not qualify for C-34; never leave blank] |
|---|---|---|---|

**Mutation verification [C-29: passively recording the same state value in the column does not satisfy C-29]:** Below the table, write an explicit confirmation statement: declare that the state in [C-09c] is identical to [C-09a] and that no field values were modified. Passive recording of the unchanged state in the column does not satisfy C-29 — an active verification directive is required.

---

## V-05 — Phrasing Register + Inertia Framing: Conversational with "Naive Trace" Foil (C-34 + C-35 Combined)

**Variation axis:** Phrasing register (conversational) + Inertia framing ("naive trace" foil)
**Hypothesis:** The conversational foil names concrete failure modes before instructions begin, priming against the exact patterns that fail each criterion. Section headings carry C-35 consequence clauses so enforcement is encountered before entering any section. Field labels carry C-34 disqualification conditions so the exact failing pattern is visible at the cell. Together, the reader approaches each section knowing what it costs to shortchange it, and each field knowing exactly what output fails it.
**Domain:** Finance (single pass)
**Key criteria targeted beyond essentials:** C-34 + C-35 (both new), C-09, C-10, C-12, C-15, C-16, C-18, C-19, C-20, C-21, C-22, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are going to hand-compile state transitions for the feature described above, acting as a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved → Posted → Paid / Voided.

Before you start, here is what a naive trace looks like — and why it fails:

> A naive trace writes "starting state → operation → ending state" in prose, leaves precondition cells blank when nothing obvious comes to mind, declares invariants like "ID is not null," and describes a race condition in one direction only with a note that "the reverse is symmetric." It feels complete because it covers the happy path. It is not complete. It will not catch the defects that matter.

Your trace will be different. Here is what you will produce.

---

**Hard constraint:** Blank cells are prohibited — this is not a stylistic preference. If you are about to leave a cell blank, write `none` instead. A blank cell and a missing value are indistinguishable to a reviewer, so blank is never acceptable [C-32]. Violating this constraint invalidates the artifact [C-19].

---

### State Transition Table [C-17: if fewer than 5 rows are present, C-17 fails — "be thorough" is not a measurable floor and does not satisfy this criterion]

Minimum 5 rows. No prose — every operation gets its own row, not a paragraph. If you find yourself writing a sentence instead of filling a cell, stop and restructure.

**Reference row — template only; do not copy this row into your output [C-24: reproducing this row verbatim does not qualify as a completed trace row]:**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify — blank is not the same as "none"; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariant 1 [C-03: a real Finance business rule — "amount field is populated" does not qualify for C-03; see exclusion list below] | Invariant 2 [C-03: second real Finance business rule — required; a row with only one invariant fails C-03] |
|---|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver assigned | Status = Pending Approval; audit entry created | Invoice total must be positive after any line-item change | Approver identity must be set before status leaves Draft |

**Trace rows (Finance — minimum 5) [C-17]:**

| Step [C-01a] | Starting State [C-01b] | Operation [C-01c] | Ending State [C-01d] | Preconditions [C-02a — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Postconditions [C-02b — write "none" if genuinely absent; leaving blank does not qualify; never leave blank] | Invariant 1 [C-03: real Finance business rule — "amount field is populated" does not qualify] | Invariant 2 [C-03: second real Finance business rule — required] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

---

### Invariant Summary [C-27: if all listed invariants match the exclusion-list patterns below, C-27 fails]

List every distinct invariant from the trace table.

Here is what does NOT qualify — name at least two disqualifying patterns explicitly [C-27]:
- "ID is not null" — structural, not a business rule
- "record exists" — a database constraint, not a Finance rule
- "status field is populated" — a schema constraint, not a domain rule

Here is what DOES qualify [C-20]: "Invoice total must remain positive after any line-item modification." This encodes a Finance business rule that would matter to a controller, not just a schema validator.

| Invariant ID | Description [C-07: real Finance business rule] | Source Step |
|---|---|---|
| INV-01 | … | Step … |

---

### Defect Log [C-04: if no defect entry is present, C-04 fails — the happy path alone does not constitute a complete trace]

At least one entry. If you are tempted to leave this empty because the happy path has no defects — that is exactly the thinking the naive trace uses. Look for missing precondition checks, invalid transitions on edge cases, invariant violations on concurrent writes.

| Defect ID [C-04a] | Type [C-04b — choose one: missing precondition check / invalid state transition / invariant violation / race condition] | Triggering Operation [C-04c — write "none" if not operation-specific; "see above" does not qualify for C-34 — name the specific operation; never leave blank] | Reason [C-04d — write "none" if genuinely absent; "error occurred" without naming the specific rule violated does not qualify for C-34; never leave blank] |
|---|---|---|---|

---

### Reachability Annotation [C-10: if any reachable transition is silently omitted, C-10 fails]

The naive trace silently omits the paths it does not test. Explicitly name every state transition NOT included in the table above, and state why you left it out. A transition is only considered covered if it appears as a row. Silent omissions do not satisfy this section.

| Omitted Transition | Rationale |
|---|---|
| [From State] -> [To State] via [Operation] | … |

---

### Race Condition Analysis [C-08: if Ordering 2 is described by reference to Ordering 1 rather than independently, C-08 fails]

The naive trace describes one direction and notes "the reverse is symmetric." That is avoidance, not analysis. Two orderings of the same concurrent operation pair often produce asymmetric outcomes — that asymmetry is exactly what this section exists to surface.

Name both concurrent operations explicitly — do not name only the conflict [C-28: naming only the conflict outcome does not qualify — both Op A and Op B must be explicitly named]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 (Op A first, then Op B):**
Describe: state before A; state after A; state after B; what conflict or resolution results.

**Ordering 2 (Op B first, then Op A):**
Describe in full. Do not write "same as above," "symmetric," or any reference to Ordering 1 [C-21]. Write it out completely as if Ordering 1 did not exist. If outcomes are genuinely identical, demonstrate it by producing the identical text — do not assert it.

---

### Negative Path [C-09: if fewer than 4 elements are present — starting state, blocked operation, post-rejection state, named error — C-09 fails]

One rejected operation. The naive trace often writes "the operation fails" in prose. That does not qualify.

| Starting State [C-09a — the state before the attempt is made] | Blocked Operation [C-09b — the operation that is rejected] | State After Rejection [C-09c — write "none" if no change; leaving blank does not qualify; never leave blank] | Named Error [C-09d — the specific error raised; "operation failed" without a specific error name does not qualify for C-34; write "none" if genuinely absent; never leave blank] |
|---|---|---|---|

**Active mutation verification [C-29: passively recording the same state value in both columns does not satisfy C-29 — an active declarative sentence is required]:** After the table, write one sentence that explicitly confirms no state mutation occurred — confirm that [C-09c] = [C-09a] and that all field values are identical before and after the rejected operation attempt. Writing the same state in both columns is passive recording. The naive trace omits this sentence entirely. Write it.
