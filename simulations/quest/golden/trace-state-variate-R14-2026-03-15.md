# trace-state Variate — Round 14
**Date:** 2026-03-15
**Rubric:** v12 / inner v28 (C-01..C-05 essentials; 29 aspirational criteria; golden: all 5 essential pass AND composite >= 80)

R14 introduces two new aspirational criteria extracted from v12 pairwise evidence:

- **C-36** (Disqualification-condition fusion on structural-format field labels): a field label
  whose criterion prescribes a structural output format (state name vs. description, noun phrase
  vs. verb phrase) co-locates the criterion ID with the specific failing format pattern. Distinct
  from C-34: C-34 covers value-content / quantitative fields; C-36 covers structural output-format
  fields. A C-34-qualifying disqualification on a quantitative floor field does NOT satisfy C-36.

- **C-37** (Section-label criterion-consequence fusion at domain-pass heading tier): the `### Pass N`
  heading itself (or equivalent domain-pass heading — the highest structural navigation node
  below the artifact title) carries a criterion ID + conditional consequence clause. Distinct
  from C-35: C-35 covers sub-section headings (invariant registers, defect logs); C-37 requires
  the annotation on the Pass-N heading. A C-35-qualifying annotation on a sub-section does NOT
  satisfy C-37; C-37 does NOT retroactively satisfy C-35.

R14 builds on R13 V-01 through V-05 (which were clean-slate variations against the v11 rubric
targeting C-34 and C-35). R14 variations graft C-36 and C-37 onto the strongest R13 structural
patterns.

---

## R14 Gap Analysis

From R13 under v12 rubric (29 aspirational criteria):

| Criterion | R13 V-01 | R13 V-02 | R13 V-03 | R13 V-04 | R13 V-05 | R14 Path |
|-----------|----------|----------|----------|----------|----------|----------|
| C-34 (disqualification in value-content labels) | PASS | FAIL | PASS | PASS | PASS | preserved |
| C-35 (sub-section heading consequence clause) | FAIL | PASS | FAIL | PASS | PASS | preserved in V-02 base; graft onto V-01 |
| C-36 (structural-format disqualification in labels) | FAIL | FAIL | FAIL | FAIL | FAIL | primary R14 target — all five variations |
| C-37 (Pass-N heading consequence clause) | FAIL | FAIL | FAIL | FAIL | FAIL | primary R14 target — all five variations |

**All five R13 variations fail C-36 and C-37 because:**
- C-36: R13 column headers carry disqualification conditions on quantitative/behavioral fields (C-17,
  C-28, C-03) but none on structural-format fields (C-01b, C-01c, C-01d). C-34-qualifying labels
  on a floor field ("qualitative 'be thorough' does not satisfy") do not satisfy C-36.
- C-37: R13 Pass headings (`### Pass 1 — Finance Domain`) carry no criterion ID or consequence
  clause. C-35-qualifying sub-section headings (Defect Log, Race Condition) satisfy C-35 but
  not C-37.

**R14 primary ceiling path (V-04):**
Build on R13 V-04 (which had C-34 + C-35 + the largest aspirational set of the five). Graft:
(a) C-36 — add structural-format disqualification conditions to C-01b, C-01c, C-01d column
    headers;
(b) C-37 — annotate every `### Pass N` heading with `[C-05: consequence clause]`.
All R13 V-04 features preserved. Predicted: 29/29 = 100. Ceiling.

**R14 alternate ceiling path (V-05):**
Build on R13 V-05 (conversational phrasing + inertia framing + Finance single pass). Fix both
gaps by the same two grafts. Tests whether the ceiling is achievable in single-pass conversational
register. Predicted: 27/29 (V-05 base had fewer aspirationals; conservative ceiling probe).

---

## Variation Axis Map

| Var | Axis | Domain | Key Probe | Predicted |
|-----|------|--------|-----------|-----------|
| V-01 | Role sequence (Finance→Sales→CS) + C-36 only | All three | C-36 graft onto R13 V-01 base — structural-format disqualification achieves ceiling without C-37? | 27/29 |
| V-02 | Output format (step blocks) + C-37 only | Sales | C-37 graft onto R13 V-02 base — Pass-N consequence clause achieves golden without C-36? | 26/29 |
| V-03 | Lifecycle emphasis (sub-step blocks, CS) + C-36 on sub-element labels | CS | C-36 earned at sub-element level rather than parent column level — does sub-element placement qualify? | 26/29 |
| V-04 | Combined: role sequence (CS→Finance→Sales) + C-36 + C-37 | All three | Both new criteria combined on R13 V-04 base — ceiling? | 29/29 |
| V-05 | Combined: phrasing register + inertia framing (Finance, single pass) + C-36 + C-37 | Finance | Conversational register ceiling — C-36 and C-37 survive soft phrasing? | 27/29 |

---

**V-01 hypothesis:** R13 V-01 held C-34 plus 20 other aspirationals (C-09, C-11, C-12, C-13,
C-15, C-17, C-19, C-20, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32,
C-33) but failed C-35 (deliberately absent) and C-37. Under v12, it also fails C-36. The single
graft: extend C-01b, C-01c, C-01d column headers with structural-format disqualification patterns
(`[C-01b: disqualifies if description written instead of state name]`). C-37 deliberately absent
to isolate C-36's independent contribution. Predicted: 22 from R13 V-01 base + C-36 = 23/29.
C-35 and C-37 deliberately absent = 2 gaps remain. Score is golden if all other 23 pass.

**V-02 hypothesis:** R13 V-02 held C-35 on step-block section headings plus 17 other aspirationals
(C-09, C-11, C-14, C-15, C-16, C-17, C-19, C-20, C-22, C-24, C-27, C-28, C-29, C-30, C-31,
C-32, C-33) but failed C-34 (deliberately absent) and C-37. The single graft: annotate the
domain section heading (`### Pass 1 — Sales Domain`) with `[C-05: if states and operations are
not recognizable as Sales pipeline vocabulary, C-05 fails]`. C-36 deliberately absent to isolate
C-37's independent contribution. Predicted: 18 from base + C-37 = 19/29. Score is below golden
on its own — confirms C-37 is not sufficient alone; it needs the full aspirational base.

**V-03 hypothesis:** R13 V-03 used a four-sub-step structure per operation with C-34 disqualification
at the sub-element level. The key sub-element labels (`Starting State [C-01b...]`, `Operation
[C-01c...]`) are also the natural C-36 carriers — they prescribe structural formats. Replacing
the existing sub-element annotations with structural-format disqualification conditions (state
name vs. description; imperative verb vs. noun phrase) satisfies C-36 at the most granular
placement. C-37 deliberately absent. Predicted: R13 V-03 base (~17 aspirationals) + C-36 =
18/29. Confirms C-36 at sub-element level is independently satisfiable.

**V-04 hypothesis:** R13 V-04 had the largest aspirational set: C-34, C-35, C-09, C-11, C-12,
C-14, C-15, C-16, C-17, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30,
C-31, C-32, C-33 = 23 aspirationals. Two grafts: (a) add C-36 structural-format disqualification
to C-01b, C-01c, C-01d column headers; (b) annotate each `### Pass N` heading with C-37
consequence clause. All R13 V-04 features preserved exactly. Predicted: 23 + C-36 + C-37 =
25/29. If any of the 23 from R13 V-04 are also independently satisfied by the grafts, score
higher. Ceiling probe.

**V-05 hypothesis:** R13 V-05 (conversational phrasing + "naive trace" foil + Finance single pass)
had C-34, C-35, C-09, C-10, C-12, C-15, C-16, C-18, C-19, C-20, C-21, C-22, C-24, C-27,
C-28, C-29, C-30, C-31, C-32, C-33 = 20 aspirationals. Two grafts: (a) C-36 on C-01b, C-01c,
C-01d labels; (b) C-37 on the domain section heading. Tests whether conversational phrasing
register is compatible with the formal structural annotations required by C-36 and C-37.
Predicted: 20 + C-36 + C-37 = 22/29.

---

## V-01 — Role Sequence: Finance → Sales → CS (C-36 Graft, C-37 Absent)

**Variation axis:** Role sequence (Finance → Sales → CS)
**Hypothesis:** Add C-36 (structural-format disqualification conditions) to C-01b, C-01c, C-01d
column headers on R13 V-01 base. C-37 deliberately absent to isolate C-36's contribution.
Every state-name column now names the specific pattern that fails C-01b/C-01d (writing a
description instead of a state name). Every operation column names the specific pattern that
fails C-01c (using a noun phrase instead of an imperative verb phrase). C-35 also deliberately
absent (as in R13 V-01) to keep the single-axis constraint.
**Domain:** Finance / Sales / Customer Service (three passes)
**Missing criteria (deliberate):** C-35, C-37
**Key criteria targeted:** C-36 (new), C-34, C-09, C-11, C-12, C-13, C-15, C-17, C-19, C-20,
C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are a state transition analyst. Hand-compile state transitions for the feature described
above using three sequential domain passes: **Finance first, then Sales, then Customer Service.**

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- No prose substitutions: every output element IS in its designated schema cell; prose IS NOT a
  valid format for trace data [C-16].
- Blank cells ARE PROHIBITED across every column. Write `none` if a field is genuinely absent —
  blank IS NOT a permitted entry anywhere in this document [C-32].
- Minimum 15 transition rows across all three passes combined [C-26: a per-pass floor alone does
  not satisfy C-26 — this is the cross-pass aggregate floor].

---

### Pass 1 — Finance Domain

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved →
Posted → Paid / Voided.

**State Transition Table** — minimum 5 rows [C-17: qualitative "be thorough" does not satisfy
this criterion — an explicit numeric floor is required; "be comprehensive" does not qualify]

**Reference row — template anchor; do not include this row in output [C-24: reproducing this row
verbatim does not qualify as a completed trace entry — this row is a structural anchor only]:**

| Step [C-01a] | Starting State [C-01b: disqualifies if a description is written instead of a state name — "invoice has been submitted" disqualifies; "Submitted" qualifies] | Operation [C-01c: disqualifies if a noun phrase is used instead of an imperative verb phrase — "Invoice Approval" disqualifies; "Approve Invoice" qualifies] | Ending State [C-01d: disqualifies if a description is written instead of a state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank [C-32]] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — never skip [C-30: single-invariant cell fails C-03]] |
|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver assigned | Status = Pending Approval; audit entry created | INV-F-01: Invoice total must remain positive after any line-item change; INV-F-02: Approver must be set before status leaves Draft |

**Trace table (Finance):**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of state name] | Operation [C-01c: disqualifies if noun phrase instead of imperative verb phrase] | Ending State [C-01d: disqualifies if description written instead of state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — "ID is not null" does not qualify; never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**Finance Invariants** — link each to the transition row that generated it [C-13: "implied by the
trace" does not satisfy C-13 — an explicit row reference is required]:

Exclusion list — these patterns do not qualify as domain invariants [C-27]:
- `"ID is not null"`
- `"record exists"`
- `"amount field is populated"`

Valid qualifying example [C-20]: "Invoice amount must remain positive after any line-item
modification before posting."

| Invariant ID | Description | Derived From [C-13: row number — "derived from the trace" without a row reference does not satisfy] |
|---|---|---|
| INV-F-01 | … | Pass 1 Row … |
| INV-F-02 | … | Pass 1 Row … |

**Finance Defect Log [C-04] — silent omissions invalidate this section [C-23]; a happy-path
trace without a defect entry does not constitute a complete trace:**

| Defect ID [C-04a] | Type [C-04b: missing precondition check / invalid state transition / invariant violation / race condition] | Triggering Operation [C-04c — write `none` if not operation-specific; "see above" does not qualify; never leave blank] | Reason [C-04d — write `none` if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 2 — Sales Domain

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal →
Closed Won / Closed Lost.

**State Transition Table** — minimum 5 rows [C-17: qualitative "be thorough" does not satisfy
this criterion]

**Reference row — do not include this row in output [C-24]:**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of state name — use declared lifecycle stage names; "lead has been qualified" disqualifies; "Qualified Lead" qualifies] | Operation [C-01c: disqualifies if noun phrase used — "Lead Qualification" disqualifies; "Qualify Lead" qualifies] | Ending State [C-01d: disqualifies if description written instead of state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — "owner is assigned" without context clause does not qualify; never skip] |
|---|---|---|---|---|---|---|
| 1 | Lead | Qualify Lead | Qualified Lead | Budget confirmed; decision-maker identified | Stage = Qualified Lead; qualification criteria recorded | INV-S-01: Opportunity amount must remain >= 0 after any stage update; INV-S-02: Closing date must be set before status reaches Proposal |

**Trace table (Sales):**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of state name] | Operation [C-01c: disqualifies if noun phrase instead of imperative verb phrase] | Ending State [C-01d: disqualifies if description written instead of state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**Sales Invariants** — same exclusion list and qualifying example apply [C-27][C-20]. Link each
to source row [C-13]:

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 2 Row … |
| INV-S-02 | … | Pass 2 Row … |

**Sales Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write `none` if not op-specific; "see above" does not qualify; never leave blank] | Reason [C-04d — write `none` if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 3 — Customer Service Domain

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved → Closed
/ Reopened.

**State Transition Table** — minimum 5 rows [C-17: qualitative "be thorough" does not satisfy
this criterion]

**Reference row — do not include in output [C-24]:**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of state name — "ticket is currently open" disqualifies; "Open" qualifies] | Operation [C-01c: disqualifies if noun phrase — "Agent Assignment" disqualifies; "Assign to Agent" qualifies] | Ending State [C-01d: disqualifies if description written instead of state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — "ticket ID exists" does not qualify; never skip] |
|---|---|---|---|---|---|---|
| 1 | New | Assign to Agent | Open | Agent capacity available | Agent ID set; SLA clock started | INV-C-01: SLA clock must be active while status is Open or Pending; INV-C-02: Customer ID must be set when status is not Closed |

**Trace table (CS):**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of state name] | Operation [C-01c: disqualifies if noun phrase instead of imperative verb phrase] | Ending State [C-01d: disqualifies if description written instead of state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — "ticket ID exists" does not qualify; never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**CS Invariants** — same exclusion list and qualifying example apply. Link each to source row
[C-13]:

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 3 Row … |
| INV-C-02 | … | Pass 3 Row … |

**CS Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write `none` if not op-specific; "see above" does not qualify; never leave blank] | Reason [C-04d — write `none` if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Cross-Domain Invariant Register [C-25]

Aggregate every invariant from all three passes. Every entry must carry an explicit cross-pass
derivation link — per-domain isolation without a cross-pass reference does not satisfy C-25.

| Invariant ID | Description | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 1 Row … |
| INV-S-01 | … | Pass 2 Row … |
| INV-C-01 | … | Pass 3 Row … |

Verify: total transition rows across all passes >= 15 [C-26].

---

### Race Condition Analysis

Name both concurrent operations explicitly [C-28: naming only the conflict outcome does not
qualify — both Op A and Op B must be identified by name]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 — Op A first, then Op B:**
Describe state before Op A, state after Op A, state after Op B, conflict or resolution.

**Ordering 2 — Op B first, then Op A:**
Describe fully and independently. Do not write "same as above" or cross-reference Ordering 1
[C-21: a reference to Ordering 1 in place of independent description invalidates this ordering].
Write each state transition as if Ordering 1 had not been described.

---

### Negative Path

One rejected operation with all four sub-elements [C-31: C-09a, C-09b, C-09c, C-09d are
independently labeled; parent criterion ID alone does not satisfy C-31]:

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c — write `none` if no state change; never leave blank] | Named Error [C-09d — write `none` if genuinely absent; "operation failed" without a specific error name does not qualify; never leave blank] |
|---|---|---|---|

After the table, write one explicit verification statement confirming that the state in [C-09c]
is identical to [C-09a] and that no field was modified by the rejected operation. A table column
value alone is passive representation — a declarative sentence is required [C-29: passively
recording the same state value in the column does not satisfy C-29].

---

## V-02 — Output Format: Step Blocks + C-37 Graft (C-36 Absent)

**Variation axis:** Output format (numbered step blocks with consequence clause on Pass heading)
**Hypothesis:** Annotate the domain section heading (`### Pass 1 — Sales Domain`) with a C-37
consequence clause (`[C-05: if states and operations are not recognizable as Sales pipeline
vocabulary, C-05 fails]`). C-36 deliberately absent from field labels to isolate C-37's
independent contribution. Tests whether a heading-level consequence annotation is sufficient
for golden without structural-format disqualification in field labels.
**Domain:** Sales (single pass)
**Missing criteria (deliberate):** C-36, C-34 (no disqualification conditions in field labels)
**Key criteria targeted:** C-37 (new), C-35, C-09, C-11, C-14, C-15, C-16, C-17, C-19, C-20,
C-22, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are a state transition analyst. Hand-compile state transitions for the feature described
above.

**You are acting as a Sales domain expert.** Lifecycle: Lead → Qualified Lead → Opportunity →
Proposal → Closed Won / Closed Lost.

**HARD RULES — violation of any rule invalidates the artifact [C-19]:**
- Prose is not a valid output format for trace data — no prose substitutions [C-16].
- Blank fields are prohibited throughout. Write `none` if a field is genuinely absent — blank
  is never an acceptable entry for any field [C-32].
- Minimum 5 operation step blocks [C-17: a qualitative instruction like "be thorough" does not
  satisfy — an explicit numeric floor is required].

Output format: one numbered step block per operation. No tables. No prose paragraphs. Every
operation gets a block using the field structure below.

---

### Pass 1 — Sales Domain [C-05: if the states and operations in this section are not recognizable as Sales pipeline vocabulary by a Sales domain expert, C-05 fails and this pass is invalid]

**Reference block — template anchor; do not reproduce this block in output [C-24: reproducing
this block verbatim does not qualify — it is a structural reference only]:**

```
Step [C-01a: sequential number 1..N; required]:
  Starting State    [C-01b: lifecycle stage name — required; never omit]:
  Operation         [C-01c: imperative verb phrase — required; never omit]:
  Ending State      [C-01d: lifecycle stage name after operation — required; never omit]:
  Preconditions     [C-02a — write `none` if genuinely absent; never leave blank [C-32]]:
  Postconditions    [C-02b — write `none` if genuinely absent; never leave blank]:
  Invariant-1       [C-03: first domain invariant — must encode a real Sales business rule; see exclusion list]:
  Invariant-2       [C-03: second domain invariant — required; single-invariant block fails C-03; write a distinct second rule [C-30: min 2 per block — never skip]]:
```

---

### Invariant Summary [C-35: if this section is omitted or contains fewer distinct invariants than step blocks contain, this section fails and the artifact is incomplete]

List every distinct invariant from all step blocks. Link each to the step that generated it
[C-13: "derived from trace" without a step reference does not satisfy C-13].

Exclusion list — patterns that do not qualify [C-27]:
- `"ID is not null"`
- `"record exists"`
- `"amount field is populated"`

Valid qualifying example [C-20]: "Opportunity amount must remain >= 0 at all stages after
qualification."

| Invariant ID | Description | Appears In Step |
|---|---|---|
| INV-01 | … | Step … |

---

### Defect Log [C-35: if this section contains no defect entry, C-04 fails — the happy path alone does not constitute a complete trace and this section is invalid]

```
Defect [C-04a: Defect-ID — required]:
  Type          [C-04b: missing precondition check / invalid state transition / invariant violation / race condition]:
  Triggering Op [C-04c — write `none` if not operation-specific; "see above" does not qualify; never leave blank [C-32]]:
  Reason        [C-04d — write `none` if genuinely absent; never leave blank]:
```

---

### Race Condition Analysis [C-35: if Ordering 2 cross-references Ordering 1 instead of being independently described, C-08 fails and this section is invalid]

Name both concurrent operations explicitly [C-28: naming only the conflict outcome does not
qualify — Op A and Op B must both be identified]:
- **Op A:** ___
- **Op B:** ___

```
Ordering 1 (A before B):
  State before A:      …
  State after A:       …
  State after B:       …
  Conflict or result:  …

Ordering 2 (B before A):
  [Describe fully and independently — do not write "same as above"; do not reference Ordering 1 [C-21]]
  State before B:      …
  State after B:       …
  State after A:       …
  Conflict or result:  …
```

---

### Negative Path [C-35: if fewer than 4 labeled elements are present — starting state, blocked operation, post-rejection state, named error — C-09 fails and this section is invalid]

```
Negative-Step [C-09a — Starting State]:
Negative-Step [C-09b — Blocked Operation]:
Negative-Step [C-09c — State After Rejection (write `none` if no change; never leave blank [C-32])]:
Negative-Step [C-09d — Named Error (write `none` if genuinely absent; never leave blank)]:
```

Mutation verification [C-29]: Immediately after the block, write one explicit confirmation
sentence declaring that the state in [C-09c] is identical to [C-09a] and that no field was
modified. A passive column value does not satisfy this requirement — a declarative sentence is
required.

---

## V-03 — Lifecycle Emphasis: Sub-Step Blocks with C-36 on Structural-Format Labels (CS)

**Variation axis:** Lifecycle emphasis (four explicit sub-step labels per operation, with C-36
structural-format disqualification embedded in sub-step labels for C-01b and C-01c)
**Hypothesis:** Sub-step labels in a four-label block structure are the natural carriers for
C-36 because they already prescribe the output format (state name, imperative verb phrase). Co-
locating `[C-01b: disqualifies if description written instead of state name]` directly within
the sub-label earns C-36 at the most granular placement possible. C-37 deliberately absent to
isolate C-36's independent contribution at sub-element level.
**Domain:** Customer Service (single pass)
**Missing criteria (deliberate):** C-35, C-37
**Key criteria targeted:** C-36 (new), C-34, C-09, C-13, C-17, C-19, C-22, C-23, C-25, C-26,
C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are a state transition analyst. Hand-compile state transitions for the feature described
above using a sub-step structured block per operation.

**You are acting as a Customer Service domain expert.** Lifecycle: New → Open → Pending →
Resolved → Closed / Reopened.

**HARD RULES — any violation invalidates the artifact [C-19]:**
- No prose substitutions — every element IS in its designated sub-step label slot [C-16].
- Blank sub-step slots ARE PROHIBITED. Write `none` for any sub-step where the value is
  genuinely absent — blank IS NOT equivalent to `none` [C-32].
- Minimum 5 operation blocks [C-17: "cover all transitions" does not satisfy — an explicit
  numeric floor is required; this floor IS not satisfied by prose instruction alone].

---

**Reference block — template anchor; do not include in output [C-24: reproducing this block
verbatim does not qualify — this is a reference anchor, not a trace entry]:**

```
--- Op Block ---
  Starting State [C-01b: disqualifies if a workflow description is written instead of a lifecycle
                  state label — "ticket is waiting for a response" disqualifies; "Pending" qualifies]:
  Operation      [C-01c: disqualifies if a noun phrase is used instead of an imperative verb phrase
                  — "Agent Assignment" disqualifies; "Assign to Agent" qualifies]:
  Ending State   [C-01d: disqualifies if a description is written instead of a state name]:
  Preconditions  [C-02a — write `none` if genuinely absent; never leave blank — blank is prohibited
                  even when preconditions are absent [C-33]]:
  Postconditions [C-02b — write `none` if genuinely absent; never leave blank]:
  Invariants     [C-03: min 2 per block — "ticket ID exists" does not qualify; write two distinct
                  CS business rules per block [C-30]]:
  Defect Notes   [C-04: write `none` if no defect applies to this operation; "see above" does not
                  qualify [C-34: "see above" does not qualify for C-04c — never leave blank]; never
                  leave blank]:
  Derived Inv    [C-13: name the invariant ID(s) derived from this block's observed transitions;
                  write `none` if no new invariant is derived here; "implied" does not satisfy]:
```

---

### CS Operation Blocks [C-26: cross-pass aggregate minimum of 5 blocks; fewer than 5 CS blocks fails C-17; write at least 5 complete blocks below]

*(generate operation blocks here — minimum 5; reference block excluded from count [C-24])*

---

### CS Invariant Register [C-23: silent omissions invalidate this section — every distinct invariant observed across blocks must appear here]

Exclusion list — patterns that do not qualify [C-27]:
- `"ID is not null"`
- `"record exists"`
- `"status field is not empty"`

Valid qualifying example [C-20]: "SLA clock must remain active while ticket status is Open or
Pending."

| Invariant ID | Description | Derived From Block [C-13: block number — "from the trace" without a block reference does not satisfy] |
|---|---|---|
| INV-C-01 | … | Block … |
| INV-C-02 | … | Block … |

---

### Cross-Pass Register [C-25]

Aggregate all invariants above with explicit derivation linkage. Even in a single-pass artifact,
this section aggregates across the internal lifecycle blocks with cross-block traceability.

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-C-01 | … | CS Block … |

---

### Race Condition Analysis

Name both concurrent operations explicitly [C-28: naming only the conflict outcome does not
qualify — both Op A and Op B must be named]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 — Op A first, then Op B:**
Describe state before A, state after A, state after B. Name the conflict or resolution.

**Ordering 2 — Op B first, then Op A:**
Describe fully and independently. Do not write "same as above" or reference Ordering 1 [C-21:
a cross-reference to Ordering 1 in place of independent description invalidates this ordering].

---

### Negative Path

One rejected operation with all four labeled sub-elements [C-31]:

```
Starting State  [C-09a — state name; disqualifies if description written instead of state name]:
Blocked Op      [C-09b — operation name; disqualifies if noun phrase instead of imperative verb]:
Post-Rejection  [C-09c — write `none` if no change; never leave blank [C-32]]:
Named Error     [C-09d — write `none` if genuinely absent; "operation failed" without a specific
                 error name does not qualify [C-34]; never leave blank]:
```

Mutation verification: After the block, write one explicit confirmation sentence declaring that
[C-09c] is identical to [C-09a] and that no field was modified. A sub-step slot value alone
is passive — a declarative sentence is required [C-29: passive representation does not satisfy
C-29].

---

## V-04 — Combined: Role Sequence (CS → Finance → Sales) + C-36 + C-37 [CEILING]

**Variation axis:** Combined (role sequence + C-36 structural-format disqualification in field
labels + C-37 Pass-N heading consequence clause)
**Hypothesis:** R13 V-04 (CS→Finance→Sales) had the largest aspirational set. Graft (a) C-36
structural-format disqualification onto every C-01b, C-01c, C-01d column header, and (b) C-37
consequence clause onto every `### Pass N` heading. All 23 R13 V-04 features preserved. The
two grafts are additive and non-conflicting — each targets a different structural layer (field
label vs. heading). Predicted: 23 from R13 V-04 base + C-36 + C-37 = 25/29. CEILING probe.
**Domain:** Customer Service / Finance / Sales (three passes, CS first)
**Missing criteria (deliberate):** None — ceiling attempt
**Key criteria targeted:** C-36 (new), C-37 (new), C-34, C-35, C-09, C-11, C-12, C-14, C-15,
C-16, C-17, C-19, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

You are a state transition analyst. Hand-compile state transitions for the feature described
above using three sequential domain passes: **Customer Service first, then Finance, then Sales.**

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- No prose substitutions: every output element IS in its designated schema cell; prose IS NOT a
  valid format for trace data [C-16].
- Blank cells ARE PROHIBITED across every column. Write `none` if a field is genuinely absent —
  blank IS NOT a permitted entry anywhere in this document [C-32].
- Minimum 15 transition rows across all three passes combined [C-26: per-pass floor does not
  satisfy C-26 — this is the aggregate cross-pass floor; "at least a few per pass" does not
  qualify for C-26].

---

### Pass 1 — Customer Service Domain [C-05: if the states and operations in this pass are not recognizable as Customer Service ticket lifecycle vocabulary by a CS expert, C-05 fails for this pass and the pass is invalid — generic states such as "Active" or "Inactive" without domain framing do not qualify]

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved → Closed
/ Reopened.

**State Transition Table** — minimum 5 rows [C-17: "be thorough" does not satisfy this criterion
— an explicit numeric floor is required; qualitative completeness instructions do not qualify]

**Reference row — template anchor; do not include this row in output [C-24: reproducing this
row verbatim does not qualify as a completed trace entry]:**

| Step [C-01a] | Starting State [C-01b: disqualifies if a description is written instead of a state name — "ticket is waiting for agent response" disqualifies; "Pending" qualifies] | Operation [C-01c: disqualifies if a noun phrase is used instead of an imperative verb phrase — "Ticket Resolution" disqualifies; "Resolve Ticket" qualifies] | Ending State [C-01d: disqualifies if a description is written instead of a state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank [C-33]] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank [C-33]] | Invariants Checked [C-03: min 2 per pass — "ticket ID exists" does not qualify; never skip [C-30]] |
|---|---|---|---|---|---|---|
| 1 | New | Assign to Agent | Open | Agent capacity available; customer ID set | Agent ID assigned; SLA clock started | INV-C-01: SLA clock must be active while ticket status is Open or Pending; INV-C-02: Customer ID must be set on all non-terminal tickets |

**Trace table (CS):**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of state name] | Operation [C-01c: disqualifies if noun phrase instead of imperative verb phrase] | Ending State [C-01d: disqualifies if description written instead of state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — "ticket ID exists" does not qualify; never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**CS Invariants** — link each to the transition row that generated it [C-13: "derived from
trace" without a row reference does not satisfy C-13]:

Exclusion list — patterns that do not qualify [C-27]:
- `"ID is not null"`
- `"record exists"`
- `"field is populated"`

Valid qualifying example [C-20]: "SLA clock must remain active while ticket status is Open or
Pending, regardless of agent reassignment."

| Invariant ID | Description | Derived From [C-13: row reference required] |
|---|---|---|
| INV-C-01 | … | Pass 1 Row … |
| INV-C-02 | … | Pass 1 Row … |

**CS Defect Log [C-04] — silent omissions invalidate this section [C-23]; listing only happy-
path transitions does not constitute a complete trace without at least one defect entry:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write `none` if not op-specific; "see above" does not qualify [C-34: "see above" does not qualify for C-04c]; never leave blank] | Reason [C-04d — write `none` if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 2 — Finance Domain [C-05: if the states and operations in this pass are not recognizable as Finance invoice or payment lifecycle vocabulary by a Finance expert, C-05 fails for this pass]

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved →
Posted → Paid / Voided.

**State Transition Table** — minimum 5 rows [C-17: qualitative "be thorough" does not satisfy
this criterion — a numeric floor is required]

**Reference row — do not include in output [C-24]:**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of state name — "invoice has been submitted for approval" disqualifies; "Submitted" qualifies] | Operation [C-01c: disqualifies if noun phrase used — "Invoice Approval" disqualifies; "Approve Invoice" qualifies] | Ending State [C-01d: disqualifies if description written instead of state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — "ID is not null" does not qualify; never skip] |
|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Submitted | Amount > 0; cost center assigned | Status = Submitted; submission timestamp recorded | INV-F-01: Invoice amount must remain positive after any line-item modification; INV-F-02: Cost center must be set before invoice leaves Draft |

**Trace table (Finance):**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of state name] | Operation [C-01c: disqualifies if noun phrase instead of imperative verb phrase] | Ending State [C-01d: disqualifies if description written instead of state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**Finance Invariants** — same exclusion list and qualifying example apply [C-27][C-20]. Link
each to source row [C-13]:

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 2 Row … |
| INV-F-02 | … | Pass 2 Row … |

**Finance Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write `none` if not op-specific; "see above" does not qualify; never leave blank] | Reason [C-04d — write `none` if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Pass 3 — Sales Domain [C-05: if the states and operations in this pass are not recognizable as Sales pipeline stages and operations by a Sales expert, C-05 fails for this pass]

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal →
Closed Won / Closed Lost.

**State Transition Table** — minimum 5 rows [C-17: qualitative "be thorough" does not satisfy
this criterion]

**Reference row — do not include in output [C-24]:**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of state name — "lead is now qualified" disqualifies; "Qualified Lead" qualifies] | Operation [C-01c: disqualifies if noun phrase — "Proposal Submission" disqualifies; "Submit Proposal" qualifies] | Ending State [C-01d: disqualifies if description written instead of state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — "owner is set" without context clause does not qualify; never skip] |
|---|---|---|---|---|---|---|
| 1 | Lead | Qualify Lead | Qualified Lead | Budget confirmed; decision-maker identified | Stage = Qualified Lead; BANT criteria recorded | INV-S-01: Opportunity amount must remain >= 0 after any stage update; INV-S-02: Closing date must be set before status reaches Proposal |

**Trace table (Sales):**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of state name] | Operation [C-01c: disqualifies if noun phrase instead of imperative verb phrase] | Ending State [C-01d: disqualifies if description written instead of state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 per pass — never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

**Sales Invariants** — same exclusion list and qualifying example apply. Link each to source
row [C-13]:

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 3 Row … |
| INV-S-02 | … | Pass 3 Row … |

**Sales Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write `none` if not op-specific; "see above" does not qualify; never leave blank] | Reason [C-04d — write `none` if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Cross-Domain Invariant Register [C-25]

Aggregate every invariant from all three passes with explicit cross-pass derivation linkage.
Per-domain isolation without cross-pass reference does not satisfy C-25.

| Invariant ID | Description | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 1 Row … |
| INV-F-01 | … | Pass 2 Row … |
| INV-S-01 | … | Pass 3 Row … |

Verify: total transition rows across all passes >= 15 [C-26].

---

### Race Condition Analysis [C-35: if Ordering 2 cross-references Ordering 1 instead of being independently and fully described, C-08 fails and this section is invalid]

Name both concurrent operations explicitly [C-28: naming only the conflict outcome does not
qualify — both Op A and Op B must be named]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 — Op A first, then Op B:**
Describe state before Op A, state after Op A, state after Op B, conflict or resolution.

**Ordering 2 — Op B first, then Op A:**
Describe fully and independently. Do not write "same as above" or cross-reference Ordering 1
[C-21: a reference to Ordering 1 in place of independent description invalidates this ordering].

---

### Negative Path [C-35: if fewer than four labeled sub-elements are present, C-09 fails and this section is invalid]

One rejected operation with all four sub-elements [C-31]:

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c — write `none` if no change; never leave blank [C-33]] | Named Error [C-09d — write `none` if genuinely absent; "operation rejected" without a named error does not qualify [C-34]; never leave blank] |
|---|---|---|---|

Mutation verification: Write one explicit confirmation sentence declaring that the state in
[C-09c] is identical to [C-09a] and no field was modified. A column value alone is passive
representation [C-29: passive representation does not satisfy C-29 — a declarative sentence
is required].

---

## V-05 — Combined: Phrasing Register + Inertia Framing + C-36 + C-37 (Finance, Single Pass)

**Variation axis:** Combined (phrasing register + inertia framing + C-36 structural-format
disqualification + C-37 Pass-N heading consequence clause)
**Hypothesis:** R13 V-05 used a "naive trace" foil in conversational register that named common
failure modes before instructions began. Graft (a) C-36 structural-format disqualification
onto C-01b, C-01c, C-01d column headers — tests whether formal annotations survive inside a
conversational framing; (b) C-37 consequence clause onto the domain section heading. If
conversational framing degrades structural annotation precision, C-36 and C-37 will score
PARTIAL. The foil primes against exactly the failure modes C-36 targets (description instead
of state name; noun phrase instead of verb phrase), making the graft semantically reinforced.
**Domain:** Finance (single pass)
**Missing criteria (deliberate):** C-14, C-21, C-25, C-26 (single-pass scope limits multi-pass
criteria)
**Key criteria targeted:** C-36 (new), C-37 (new), C-34, C-35, C-09, C-12, C-15, C-16, C-18,
C-19, C-20, C-22, C-24, C-27, C-28, C-29, C-30, C-31, C-32, C-33

---

Here is what a naive trace of {{topic}} looks like — not what you should produce, but what this
prompt is designed to prevent:

> The invoice starts in some kind of draft state. The user submits it. Someone approves it.
> Then it gets posted and eventually paid. Invalid transitions probably involve trying to pay
> an unapproved invoice. Invariants are things like "the ID should exist" and "the amount should
> be set." Defects are probably edge cases around the approval flow.

That naive trace fails every rubric criterion. It writes descriptions instead of state names.
It uses passive constructions instead of imperative operations. Its invariants are structural
placeholders, not business rules. The trace table is implied, not compiled. The prompt below
exists to replace that naive trace with a hand-compiled state machine.

---

### Pass 1 — Finance Domain [C-05: if the states and operations produced in this section cannot be identified as Finance invoice lifecycle vocabulary by a Finance domain expert — not generic workflow states, not placeholder labels — C-05 fails and the entire pass is invalid]

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved →
Posted → Paid / Voided.

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- No prose substitutions: every output element is in its designated table cell; prose is not a
  valid format for trace data [C-16].
- Blank cells are prohibited throughout. Write `none` if a field is genuinely absent — blank is
  not an acceptable entry for any field in any row [C-32].

**State Transition Table** — minimum 5 rows [C-17: "cover all transitions" does not satisfy
this criterion — a numeric floor is required; qualitative scope instructions do not qualify]

**Reference row — template anchor; do not reproduce this row in output [C-24: reproducing this
row verbatim does not qualify as a completed trace row — it is a reference anchor only]:**

| Step [C-01a] | Starting State [C-01b: disqualifies if a workflow description is written instead of a Finance state name — "invoice is in the draft stage" disqualifies; "Draft" qualifies] | Operation [C-01c: disqualifies if a noun phrase is used instead of an imperative verb phrase — "Invoice Submission" disqualifies; "Submit Invoice" qualifies] | Ending State [C-01d: disqualifies if a description is written instead of a Finance state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank [C-32]] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 — never skip [C-30]; "ID is not null" does not qualify [C-18]] |
|---|---|---|---|---|---|---|
| 1 | Draft | Submit Invoice | Submitted | Amount > 0; GL account assigned | Status = Submitted; submission timestamp recorded | INV-01: Invoice amount must remain positive after any line-item modification; INV-02: GL account must be assigned before invoice leaves Draft |

**Trace table (Finance):**

| Step [C-01a] | Starting State [C-01b: disqualifies if description written instead of Finance state name] | Operation [C-01c: disqualifies if noun phrase instead of imperative verb phrase] | Ending State [C-01d: disqualifies if description written instead of Finance state name] | Preconditions [C-02a — write `none` if genuinely absent; never leave blank] | Postconditions [C-02b — write `none` if genuinely absent; never leave blank] | Invariants Checked [C-03: min 2 — never skip] |
|---|---|---|---|---|---|---|
| | | | | | | |

---

### Finance Invariants [C-35: if the invariant list contains only exclusion-list patterns, this section fails — invariants written as "ID is not null" or "record exists" invalidate this section]

Link each invariant to the row that generated it [C-13: "derived from the trace" without a
row reference does not satisfy C-13].

Exclusion list — patterns that do not qualify as Finance invariants [C-27]:
- `"ID is not null"`
- `"record exists"`
- `"amount field is populated"`

Valid qualifying example [C-20]: "Invoice amount must remain positive after any line-item
modification before the invoice is posted."

| Invariant ID | Description | Derived From [C-13] |
|---|---|---|
| INV-01 | … | Row … |
| INV-02 | … | Row … |

---

### Finance Defect Log [C-35: if this section is omitted or contains no defect entry, C-04 fails and this section is invalid — the naive trace above named no defects; this section must name at least one]

| Defect ID [C-04a] | Type [C-04b] | Triggering Operation [C-04c — write `none` if not op-specific; "see above" does not qualify [C-34]; never leave blank] | Reason [C-04d — write `none` if genuinely absent; never leave blank] |
|---|---|---|---|

---

### Race Condition Analysis

Name both concurrent Finance operations explicitly [C-28: naming only the conflict outcome does
not qualify — both Op A and Op B must be identified; this is one of the patterns the naive trace
above failed to name]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 — Op A first, then Op B:**
Describe state before A, state after A, state after B, conflict or resolution.

**Ordering 2 — Op B first, then Op A:**
Describe fully and independently — do not write "same as above" and do not cross-reference
Ordering 1 [C-21: the naive trace pattern of saying "same conflict applies" does not satisfy
C-12; independent description is required].

---

### Negative Path

One rejected Finance operation with all four labeled sub-elements [C-31]:

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c — write `none` if no change; never leave blank [C-33]] | Named Error [C-09d — write `none` if genuinely absent; "operation failed" without a named Finance error does not qualify [C-34]; never leave blank] |
|---|---|---|---|

Mutation verification: Write one explicit confirmation sentence declaring that the Finance
record state in [C-09c] is identical to [C-09a] and that no field was modified by the rejected
operation. Recording the same state value in the table is passive — a declarative sentence is
required [C-29: passive column value does not satisfy C-29].
