# trace-state Variate — Round 16
**Date:** 2026-03-15
**Rubric:** v14 / C-01..C-05 essentials; 35 aspirational criteria C-09..C-44; golden: all 5 essential pass AND composite ≥ 80

R16 introduces five new aspirational criteria extracted from R15 pairwise evidence (v14 rubric):

- **C-40** — Per-pass labeled defect: each domain pass carries at least one defect log entry with
  type + triggering operation + reason, independently. Multi-pass-only criterion.
- **C-41** — Cross-domain precondition chain annotation: a postcondition in pass N is explicitly
  named and connected as a precondition feeding into pass N+1 — an explicit labeled bridge, not
  implicit flow. Multi-pass-only criterion.
- **C-42** — Domain-ordering defect-class hypothesis: pass headings name the defect class the
  domain ordering targets; the ordering itself is annotated as the hypothesis vehicle. Multi-pass
  + explicit annotation required.
- **C-43** — Lifecycle-phase state annotation: entity lifecycle phase labels appear at state level,
  enriching before/after fields beyond raw attribute values. Format-neutral.
- **C-44** — Sub-step decomposition within operation block: a single logical operation is
  decomposed into 3 or more sub-steps each carrying an independent before/op/after state triple.
  Format-neutral; minimum 3 sub-steps per decomposed block.

**Variation axis choices:**
- Single-axis (3): Role sequence (ordering hypothesis) / Output format (lifecycle + sub-step) /
  Role sequence (CS-first ordering hypothesis)
- Combined (2): Step-block multi-pass + lifecycle emphasis / All-five-criteria ceiling

---

## Round 16 Variation Map

| Var | Axis | Domain | Hypothesis | New Aspirationals Targeted |
|-----|------|--------|------------|---------------------------|
| V-01 | Role sequence (Finance → Sales → CS) as defect-class hypothesis vehicle | All three | Finance-first ordering annotated as MissingPrecondition-class hypothesis; explicit cross-domain postcondition→precondition bridge annotations surface chain-breaking defects; per-pass defect log enforces independent defect coverage | C-40, C-41, C-42 |
| V-02 | Output format (step-block, single-pass) + Lifecycle emphasis + Sub-step decomposition | Sales | Lifecycle phase labels in Starting State/Ending State fields (C-43) reveal phase-boundary invariant violations; 4 mandatory sub-steps per operation (C-44) force state annotation at sub-step granularity | C-43, C-44 |
| V-03 | Role sequence (CS → Finance → Sales, non-standard) as defect-class hypothesis vehicle | All three | CS-first ordering annotated as SLA/escalation-defect-class hypothesis; per-pass defect log confirms each defect class surfaces independently | C-40, C-42 |
| V-04 | Output format (step-block multi-pass, Sales → CS) + Lifecycle emphasis + Cross-domain chain | Sales / CS | Step-block with lifecycle phase labels in state fields + explicit postcondition→precondition bridge blocks between passes surfaces lifecycle-phase-boundary defects invisible in single-pass analysis | C-41, C-43 |
| V-05 | All five new criteria (ordering hypothesis + chain + per-pass defect + lifecycle labels + sub-step) | Finance / Sales / CS | Ceiling combination: multi-pass ordering hypothesis (C-42) + explicit cross-domain chain (C-41) + per-pass defect coverage (C-40) + lifecycle-phase state annotation (C-43) + sub-step decomposition in Defect Analysis blocks (C-44) | C-40, C-41, C-42, C-43, C-44 |

---

## V-01 — Role Sequence: Finance → Sales → CS, Ordering as Defect-Class Hypothesis (C-40, C-41, C-42)

**Variation axis:** Role sequence (Finance → Sales → CS) as defect-class hypothesis vehicle
**Hypothesis:** Finance-first ordering is explicitly annotated as targeting MissingPrecondition
defects — Finance lifecycle constraints (amount limits, approver assignment, posting rules)
generate precondition gaps that Sales and CS operations unknowingly depend on. Each pass heading
names the defect class the ordering targets (C-42). After each pass, an explicit cross-domain
bridge table names the postconditions in pass N that become required preconditions in pass N+1
(C-41). Each pass's Defect Log must carry at least one entry independently (C-40) — a defect
only in pass 1 does not satisfy C-40.
**Domain:** Finance / Sales / Customer Service (all three, Finance-first)
**Key criteria targeted beyond essentials:** C-09, C-10, C-11, C-13, C-15, C-16, C-17, C-19,
C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-34, C-35, C-36, C-37,
C-38, C-39, C-40, C-41, C-42

---

You are a state transition analyst. Hand-compile state transitions for the feature described above
using three sequential domain passes: **Finance first, then Sales, then Customer Service.**

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Prose is not a valid format for trace data — no prose substitutions [C-16].
- Blank cells are prohibited throughout. Write `none` if a field is genuinely absent [C-32].
- Minimum 15 transition rows total across all three passes [C-26].
- Column headers are behavioral specifications — do not alter them.
- Every pass Defect Log must contain at least one entry carrying Type + Triggering Op + Reason
  [C-40: per-pass defect coverage — a defect only in Pass 1 does not satisfy this rule; FAILS
  if: any pass Defect Log is left empty or contains only a placeholder row].

---

### Pass 1 — Finance Domain [C-42: ordering hypothesis — Finance runs FIRST because Finance lifecycle constraints (amount limits, approval requirements, posting rules) generate **MissingPrecondition** defects; if this ordering hypothesis is correct, Pass 1 Defect Log will surface at least one MissingPrecondition defect before Sales or CS operations are attempted; a different defect class in Pass 1 signals the hypothesis should shift] [C-37: if the invariant registry for this pass is absent, the cross-domain aggregate in Section 4 cannot be completed — consequence: C-25 fails and golden threshold is unreachable]

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved →
Posted → Paid / Voided.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — template anchor; do not reproduce this row in output [C-24]:**

| Step [C-01a: sequential integer 1..N — directive: number rows ascending — FAILS if: non-sequential or alpha label [C-34]] [C-38][C-39] | Starting State [C-01b: declared lifecycle name only — directive: use vocabulary above [C-30]; FAILS FORMAT: descriptive phrase substituted for declared state name, e.g., "invoice awaiting review" fails [C-36]] [C-38][C-39] | Operation [C-01c: one imperative verb phrase [C-30]; FAILS if: two actions joined by "and" or "then" [C-34]] [C-38][C-39] | Ending State [C-01d: declared lifecycle name only — same constraint [C-36]] [C-38][C-39] | Preconditions [C-02a: named attribute; write "none" if absent [C-30]; FAILS if: vague without named attribute [C-34]] [C-38][C-39] | Postconditions [C-02b: changed attribute; write "none" if absent [C-30]; FAILS if: restates ending state [C-34]] [C-38][C-39] | Invariant 1 [C-03: real Finance business rule [C-30]; FAILS if: structural placeholder ("ID not null", "record exists", "amount field present") [C-34]] [C-38][C-39] | Invariant 2 [C-03: second Finance rule — required; FAILS if: restates Invariant 1 [C-34]] [C-38][C-39] |
|---|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver identity assigned | Status = Pending Approval; audit trail entry created | Invoice total must be positive after any line-item modification | Approver identity must be set before status transitions out of Draft |

**Trace table (Finance — minimum 5 rows) [C-17]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b [C-36][C-38][C-39]] | Operation [C-01c [C-38][C-39]] | Ending State [C-01d [C-36][C-38][C-39]] | Preconditions [C-02a [C-38][C-39]] | Postconditions [C-02b [C-38][C-39]] | Invariant 1 [C-03 [C-38][C-39]] | Invariant 2 [C-03 [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Finance Invariant Registry [C-35: this sub-section heading is load-bearing — absent table fails C-25; consequence: cross-domain aggregate cannot be completed]:**

Exclusion list — patterns that do not qualify as domain invariants [C-27]:
- "ID is not null"
- "record exists"
- "amount field is populated"

Valid qualifying example [C-20]: "Invoice total must remain positive after any line-item modification."

| Invariant ID | Description [C-07: real Finance business rule] | Derived From (Pass 1 Row #) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 1 Row … |
| INV-F-02 | … | Pass 1 Row … |

**Finance Defect Log [C-40: this pass must carry at least one entry with Type + Triggering Op + Reason independently — FAILS if: this section is empty even if Pass 2 or Pass 3 carry defects] [C-23: silent omissions invalidate this section; consequence: C-04 fails and golden threshold is unreachable]:**

| Defect ID [C-04a] | Type [C-04b: MissingPrecondition / InvalidTransition / InvariantViolation / RaceCondition — FAILS if: omitted or "other" [C-38][C-39]] | Triggering Op [C-04c: name the operation; write "none" if not op-specific — FAILS if: blank [C-38][C-39]] | Reason [C-04d: specific rule violated; write "none" if absent — FAILS if: vague [C-38][C-39]] |
|---|---|---|---|

**Pass 1 → Pass 2 Cross-Domain Bridge [C-41: this bridge table is the explicit cross-domain precondition chain annotation — FAILS if: absent; FAILS if: entries are generic rather than traceable to specific Pass 1 rows and specific Pass 2 precondition fields; FAILS if: fewer than two named postcondition-to-precondition links]:**

For each Finance postcondition that becomes a required precondition in the Sales pass, record
the explicit link here. A Sales operation compiled without tracing these Finance postconditions
is implicitly relying on this chain without making it testable.

| Finance Postcondition (Pass 1 Row #) [C-41: cite specific row] | Seeded Sales Precondition (Pass 2 field) [C-41: name the exact precondition field and condition] | Bridge Type [C-41: PreconditionSeed / InvariantPropagation / StateConstraintForward] |
|---|---|---|
| … (e.g., Status = Posted from Row 4) | … (e.g., Pass 2 Row N Preconditions: invoice_status = Posted required before commission release) | PreconditionSeed |
| … | … | … |

---

### Pass 2 — Sales Domain [C-42: ordering hypothesis — Sales runs SECOND because Sales stage advancement depends on Finance invoice state as upstream preconditions; this ordering targets **InvalidTransition** defects that occur when Sales operations proceed without Finance authorization states being satisfied; if the cross-domain bridge (above) is correct, Pass 2 Defect Log will contain at least one InvalidTransition traceable to a Finance precondition gap] [C-37: invariant registry absent from this pass fails C-25 — consequence: cross-domain aggregate is incomplete]

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal →
Closed Won / Closed Lost.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b [C-36][C-38][C-39]] | Operation [C-01c; FAILS if: compound [C-34][C-38][C-39]] | Ending State [C-01d [C-36][C-38][C-39]] | Preconditions [C-02a; FAILS if: vague [C-34][C-38][C-39]] | Postconditions [C-02b; FAILS if: restates ending state [C-34][C-38][C-39]] | Invariant 1 [C-03; FAILS if: structural [C-34][C-38][C-39]] | Invariant 2 [C-03: second required [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| 1 | Lead | Qualify Lead | Qualified Lead | Contact verified; lead score ≥ qualification threshold | Stage = Qualified Lead; owner assigned; close date set | Opportunity owner must be assigned before stage advances past Qualified Lead | Close date must be set before stage reaches Proposal |

**Trace table (Sales — minimum 5 rows) [C-17]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b [C-36][C-38][C-39]] | Operation [C-01c [C-38][C-39]] | Ending State [C-01d [C-36][C-38][C-39]] | Preconditions [C-02a [C-38][C-39]] | Postconditions [C-02b [C-38][C-39]] | Invariant 1 [C-03 [C-38][C-39]] | Invariant 2 [C-03 [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Sales Invariant Registry [C-35: consequence — omission fails C-25]:**

Same exclusion list applies [C-27]. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From (Pass 2 Row #) [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 2 Row … |
| INV-S-02 | … | Pass 2 Row … |

**Sales Defect Log [C-40: Pass 2 must carry at least one entry independently — FAILS if: empty] [C-23]:**

| Defect ID [C-04a] | Type [C-04b [C-38][C-39]] | Triggering Op [C-04c; never blank [C-38][C-39]] | Reason [C-04d; never blank [C-38][C-39]] |
|---|---|---|---|

**Pass 2 → Pass 3 Cross-Domain Bridge [C-41: explicit postcondition-to-precondition chain from Sales to CS — FAILS if: absent or fewer than two named entries]:**

| Sales Postcondition (Pass 2 Row #) [C-41] | Seeded CS Precondition (Pass 3 field) [C-41] | Bridge Type [C-41: PreconditionSeed / InvariantPropagation / StateConstraintForward] |
|---|---|---|
| … | … | … |
| … | … | … |

---

### Pass 3 — Customer Service Domain [C-42: ordering hypothesis — CS runs LAST because CS lifecycle operations (ticket escalation, resolution, SLA enforcement) depend on Sales opportunity state and Finance invoice state as upstream constraints; this ordering targets **InvariantViolation** defects that occur when CS resolution states conflict with Finance billing invariants; three distinct defect types across three passes confirms the ordering hypothesis] [C-37: invariant registry absent fails C-25 — consequence: cross-domain aggregate incomplete]

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved →
Closed / Reopened.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b [C-36][C-38][C-39]] | Operation [C-01c; FAILS if: compound [C-34][C-38][C-39]] | Ending State [C-01d [C-36][C-38][C-39]] | Preconditions [C-02a; FAILS if: vague [C-34][C-38][C-39]] | Postconditions [C-02b; FAILS if: restates ending state [C-34][C-38][C-39]] | Invariant 1 [C-03; FAILS if: structural [C-34][C-38][C-39]] | Invariant 2 [C-03: second required [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| 1 | New | Assign to Agent | Open | Agent capacity available; customer ID present | Agent ID set; SLA clock running; audit entry created | SLA clock must be active while status is Open or Pending | Customer ID must be non-null for any non-Closed status |

**Trace table (CS — minimum 5 rows) [C-17]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b [C-36][C-38][C-39]] | Operation [C-01c [C-38][C-39]] | Ending State [C-01d [C-36][C-38][C-39]] | Preconditions [C-02a [C-38][C-39]] | Postconditions [C-02b [C-38][C-39]] | Invariant 1 [C-03 [C-38][C-39]] | Invariant 2 [C-03 [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**CS Invariant Registry [C-35: consequence — omission fails C-25]:**

Same exclusion list [C-27]. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From (Pass 3 Row #) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 3 Row … |
| INV-C-02 | … | Pass 3 Row … |

**CS Defect Log [C-40: Pass 3 must carry at least one entry independently — FAILS if: empty] [C-23]:**

| Defect ID [C-04a] | Type [C-04b [C-38][C-39]] | Triggering Op [C-04c; never blank [C-38][C-39]] | Reason [C-04d; never blank [C-38][C-39]] |
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

**Ordering 1 — Op A first, then Op B:** State before A; state after A; state after B; conflict
or resolution named.

**Ordering 2 — Op B first, then Op A:** Describe fully and independently. Do not write "same as
above" or any cross-reference to Ordering 1 [C-21].

---

### Section 6 — Negative Path [C-09]

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c — write "none" if no change; never blank] | Named Error [C-09d — write "none" if absent; never blank] |
|---|---|---|---|

**Mutation verification [C-29]:** Below the table, write an explicit confirmation sentence
declaring that [C-09c] = [C-09a] and that no field values were modified. Passive recording of
the same state value in the column does not satisfy C-29 — an independent declarative sentence
is required.

---

## V-02 — Step-Block + Lifecycle-Phase State Annotation + Sub-Step Decomposition (C-43, C-44)

**Variation axis:** Output format (step-block, single-pass) + Lifecycle emphasis + Sub-step
decomposition
**Hypothesis:** Embedding lifecycle phase labels directly inside Starting State and Ending State
field annotations (C-43) — e.g., `Lead [phase: Acquisition]`, `Opportunity [phase: Active
Pipeline]` — reveals phase-boundary invariant violations that raw attribute tracing skips:
an operation that looks valid in raw state terms may cross a phase boundary with unmet phase
invariants. Decomposing each operation into four mandatory sub-steps (C-44) — Precondition Check,
Pre-State Snapshot, Apply Operation, Post-State Snapshot — forces before/op/after state
annotation at sub-step granularity, surfacing intermediate-state defects invisible at
operation-level. Both C-43 and C-44 are format-neutral and apply to any single-pass step-block.
**Domain:** Sales (single pass — Lead → Closed Won lifecycle maps clearly to acquisition-phase
labeling)
**Key criteria targeted beyond essentials:** C-09, C-10, C-13, C-15, C-16, C-17, C-19, C-22,
C-23, C-24, C-25, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-38, C-39, C-43, C-44

---

You are a state transition analyst. Hand-compile state transitions for the feature described above.

**You are acting as a Sales domain expert.**

**Declared lifecycle phases [C-43: these phase labels must appear in every Starting State and
Ending State annotation throughout this artifact — raw state names without phase labels do not
satisfy C-43; FAILS if: any state field contains a state name without a phase label]:**
- Lead [phase: Acquisition] → Qualified Lead [phase: Qualification] → Opportunity
  [phase: Active Pipeline] → Proposal [phase: Commit Stage] → Closed Won [phase: Post-Sale]
  / Closed Lost [phase: Disqualified]

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Blank fields are prohibited throughout. Write `none` if a field is genuinely absent [C-32].
- Minimum 5 complete operation records [C-17].
- Every operation record must include all four sub-steps. A record missing any sub-step is invalid.
- Starting State and Ending State must include lifecycle phase labels [C-43: FAILS if: state
  name is given without a phase label; e.g., "Opportunity" alone fails; "Opportunity [phase:
  Active Pipeline]" satisfies C-43].
- Each operation record must contain at least 3 sub-steps, each with an independent state
  annotation [C-44: FAILS if: fewer than 3 sub-steps appear in any record; FAILS if: any
  sub-step lacks its own state reference].
- Prose is not a valid format for trace data [C-16].

---

**Reference operation record — template anchor; do not reproduce this record in output [C-24]:**

```
=== Operation Record N ===

Starting State [C-01b: declared Sales state name + lifecycle phase label in brackets —
  directive: always include phase label — FAILS if: phase label absent, e.g., "Opportunity"
  alone fails; must be "Opportunity [phase: Active Pipeline]"]
  [C-43: lifecycle-phase annotation required at state level] [C-38][C-39]:

Operation      [C-01c: one imperative verb phrase — directive: one Sales action per record —
  FAILS if: compound action joined by "and" or "then"] [C-38][C-39]:

Ending State   [C-01d: declared state name + phase label — same constraint as Starting State;
  FAILS if: phase label absent or state described rather than named]
  [C-43] [C-38][C-39]:

  Sub-step 1 — Precondition Check [C-44: mandatory sub-step — FAILS if absent — directive:
    verify all preconditions before sub-step 2; record state snapshot before operation]
    [C-38][C-39]:
    State before:   Lead [phase: Acquisition]
    Preconditions [C-02a: list every condition — directive: name the specific attribute
      checked; write "none" if absent — FAILS if: vague condition without named attribute]
      [C-38][C-39]:
      Contact verified; lead score ≥ qualification threshold

  Sub-step 2 — Apply Operation [C-44: mandatory sub-step — FAILS if absent — directive:
    record action taken and intermediate state] [C-38][C-39]:
    State entering: Lead [phase: Acquisition]
    Action:         Qualify Lead
    State exiting:  Qualified Lead [phase: Qualification]

  Sub-step 3 — Postcondition Check [C-44: mandatory sub-step — FAILS if absent — directive:
    assert every guarantee; do not restate ending state name alone] [C-38][C-39]:
    State after:    Qualified Lead [phase: Qualification]
    Postconditions [C-02b: assert the changed attribute — directive: name the attribute
      changed, not the stage name — FAILS if: restates ending state without changed attribute]
      [C-38][C-39]:
      Stage = Qualified Lead; owner assigned; close date set

  Sub-step 4 — Invariant Verification [C-44: fourth mandatory sub-step — FAILS if absent —
    directive: verify both invariants hold after sub-step 3 completes] [C-38][C-39]:
    Invariant-1 [C-03: real Sales business rule — directive: encode operational consequence
      of violation — FAILS if: structural placeholder ("owner field not null", "record exists")]
      [C-38][C-39]:
      Opportunity owner must be assigned before stage advances past Qualified Lead
    Invariant-2 [C-03: second real Sales rule — required — FAILS if: restates Invariant-1]
      [C-38][C-39]:
      Close date must be set before stage reaches Proposal
```

---

**Operation records (Sales — minimum 5) [C-17: fewer than 5 complete records fails C-17]:**

*(generate operation records here — each must include all four sub-steps; Starting State and
Ending State must carry lifecycle phase labels [C-43]; at least 3 sub-steps per record [C-44])*

---

**Sales Invariant Summary [C-35]:**

List every distinct invariant declared across all operation records.

Exclusion list — patterns that do not qualify [C-27]:
- "ID is not null"
- "owner field present"
- "record exists"

Valid qualifying example [C-20]: "Opportunity amount must remain ≥ 0 at all stages after
qualification."

| Invariant ID | Description [C-07] | Derived From Record # [C-13] |
|---|---|---|
| INV-S-01 | … | Record … |
| INV-S-02 | … | Record … |

---

**Defect Log [C-04] — silent omissions invalidate this section [C-23]: consequence — C-04 fails if empty:**

```
Defect [C-04a: sequential ID — directive: identify edge-case or race-condition defect if
  happy path has no violations — FAILS if: section left empty] [C-38][C-39]:
  Type           [C-04b: MissingPrecondition / InvalidTransition / InvariantViolation /
                  RaceCondition — FAILS if: omitted or "other"] [C-38][C-39]:
  Triggering Op  [C-04c: operation name; write "none" if not op-specific — FAILS if: blank]
                  [C-38][C-39]:
  Reason         [C-04d: specific rule violated; write "none" if absent — FAILS if: vague
                  like "system error" without naming the rule] [C-38][C-39]:
```

---

**Race Condition Analysis [C-08]:**

Name both concurrent operations explicitly [C-28]:
- **Op A:** ___
- **Op B:** ___

```
Ordering 1 (A before B):
  State before A [C-01b — declared name + phase label [C-43]]:
  State after A  [C-01d — declared name + phase label [C-43]]:
  State after B  [C-01d — declared name + phase label [C-43]]:
  Conflict/result:

Ordering 2 (B before A):
  [Describe fully — do not reference Ordering 1; do not write "same as above" [C-21]]
  State before B [phase label required [C-43]]:
  State after B  [phase label required [C-43]]:
  State after A  [phase label required [C-43]]:
  Conflict/result:
```

---

**Negative Path [C-09]:**

```
Negative-Step:
  Starting State     [C-09a: declared state name + phase label — FAILS if: phase absent [C-43]]
                     [C-38][C-39]:
  Blocked Operation  [C-09b: imperative verb phrase — FAILS if: blank] [C-38][C-39]:
  State After Rejection [C-09c: declared name + phase label; write "none" if no change —
                     FAILS if: blank [C-43]] [C-38][C-39]:
  Named Error        [C-09d: specific constraint violated; write "none" if absent —
                     FAILS if: blank] [C-38][C-39]:
```

**Mutation verification [C-29]:** Immediately after the negative-step block, write one explicit
confirmation sentence declaring that [C-09c] = [C-09a] and that no field was modified. Passive
recording of the same state value is not sufficient — an independent declarative sentence is
required.

---

## V-03 — Role Sequence: CS → Finance → Sales, Non-Standard Ordering as Defect-Class Hypothesis (C-40, C-42)

**Variation axis:** Role sequence (CS → Finance → Sales, non-standard ordering) as defect-class
hypothesis vehicle
**Hypothesis:** CS-first is explicitly annotated as targeting InvariantViolation defect class —
CS ticket lifecycle constraints (SLA clock, escalation routes, resolution-state purity) generate
invariant violations before billing or commercial constraints are layered. Finance-second targets
MissingPrecondition defect class — invoice state interactions with CS refund workflows surface
precondition chains invisible in Finance-first ordering. Sales-last targets InvalidTransition
defect class — commercial constraint interactions with CS resolution states reveal invalid
stage advances. Each pass heading carries the ordering rationale and targeted defect class (C-42).
Per-pass defect logs confirm each class surfaces independently (C-40). V-03 tests whether a
different ordering exposes a distinct defect-class profile from V-01.
**Domain:** Customer Service / Finance / Sales (all three, CS-first)
**Key criteria targeted beyond essentials:** C-09, C-10, C-11, C-13, C-15, C-16, C-17, C-19,
C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-34, C-35, C-36, C-37,
C-38, C-39, C-40, C-42

---

You are a state transition analyst. Hand-compile state transitions for the feature described above
using three sequential domain passes: **Customer Service first, then Finance, then Sales.**

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Prose is not a valid format for trace data [C-16].
- Blank cells are prohibited. Write `none` if genuinely absent [C-32].
- Minimum 15 transition rows total across all three passes [C-26].
- Column headers are behavioral specifications — do not alter them.
- Every pass Defect Log must contain at least one entry independently [C-40: FAILS if: any
  pass's Defect Log is empty or placeholder, even if other passes have defects].

---

### Pass 1 — Customer Service Domain [C-42: ordering hypothesis — CS runs FIRST because CS lifecycle constraints (SLA clock, escalation-path completeness, resolution-state purity) generate **InvariantViolation** defects; if this hypothesis is correct, Pass 1 Defect Log surfaces at least one InvariantViolation defect — a MissingPrecondition defect instead signals the hypothesis should be reclassified as V-01 Finance-first] [C-37: invariant registry absent fails C-25; consequence: golden threshold unreachable]

You are a Customer Service domain expert. Lifecycle: New → Open → Pending → Resolved →
Closed / Reopened.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — template anchor; do not reproduce in output [C-24]:**

| Step [C-01a: sequential 1..N; FAILS if: non-sequential [C-34]] [C-38][C-39] | Starting State [C-01b: declared CS lifecycle name only [C-30]; FAILS FORMAT: descriptive phrase [C-36]] [C-38][C-39] | Operation [C-01c: one imperative verb phrase [C-30]; FAILS if: compound [C-34]] [C-38][C-39] | Ending State [C-01d: declared name only [C-36]] [C-38][C-39] | Preconditions [C-02a: named attribute; write "none" if absent [C-30]; FAILS if: vague [C-34]] [C-38][C-39] | Postconditions [C-02b: changed attribute; write "none" if absent [C-30]; FAILS if: restates ending state [C-34]] [C-38][C-39] | Invariant 1 [C-03: real CS rule; FAILS if: structural placeholder [C-34]] [C-38][C-39] | Invariant 2 [C-03: second required; FAILS if: restates Inv 1 [C-34]] [C-38][C-39] |
|---|---|---|---|---|---|---|---|
| 1 | New | Assign to Agent | Open | Agent capacity available; customer ID present | Agent ID set; SLA clock running; audit entry created | SLA clock must be active while status is Open or Pending | Customer ID must be non-null for any non-Closed status |

**Trace table (CS — minimum 5 rows) [C-17]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b [C-36][C-38][C-39]] | Operation [C-01c [C-38][C-39]] | Ending State [C-01d [C-36][C-38][C-39]] | Preconditions [C-02a [C-38][C-39]] | Postconditions [C-02b [C-38][C-39]] | Invariant 1 [C-03 [C-38][C-39]] | Invariant 2 [C-03 [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**CS Invariant Registry [C-35: load-bearing sub-section — absent table fails C-25]:**

Exclusion list [C-27]: "ID is not null" / "record exists" / "field is populated"

Valid qualifying example [C-20]: "SLA clock must be running throughout Open and Pending states."

| Invariant ID | Description [C-07] | Derived From (Pass 1 Row #) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 1 Row … |
| INV-C-02 | … | Pass 1 Row … |

**CS Defect Log [C-40: Pass 1 must carry at least one entry independently — annotate defect type against C-42 hypothesis; if not InvariantViolation, note hypothesis reclassification signal] [C-23]:**

| Defect ID [C-04a] | Type [C-04b: MissingPrecondition / InvalidTransition / InvariantViolation / RaceCondition — if InvariantViolation, C-42 CS-first hypothesis is confirmed; if different, annotate hypothesis signal [C-42]] [C-38][C-39] | Triggering Op [C-04c; never blank [C-38][C-39]] | Reason [C-04d; never blank [C-38][C-39]] |
|---|---|---|---|

---

### Pass 2 — Finance Domain [C-42: ordering hypothesis — Finance runs SECOND because Finance billing constraints interact with CS refund workflows; this ordering targets **MissingPrecondition** defects in Finance operations that depend on CS resolution state being established first; if CS-first hypothesis holds, Finance defects will be of a different class than CS defects, broadening defect coverage] [C-37: consequence — invariant registry absent fails C-25]

You are a Finance domain expert. Lifecycle: Draft → Submitted → Pending Approval → Approved →
Posted → Paid / Voided.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b [C-36][C-38][C-39]] | Operation [C-01c; FAILS if: compound [C-34][C-38][C-39]] | Ending State [C-01d [C-36][C-38][C-39]] | Preconditions [C-02a; FAILS if: vague [C-34][C-38][C-39]] | Postconditions [C-02b; FAILS if: restates ending state [C-34][C-38][C-39]] | Invariant 1 [C-03; FAILS if: structural [C-34][C-38][C-39]] | Invariant 2 [C-03: second required [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| 1 | Draft | Submit for Approval | Pending Approval | Amount > 0; approver assigned | Status = Pending Approval; audit entry created | Invoice total positive after any line-item modification | Approver set before status transitions out of Draft |

**Trace table (Finance — minimum 5 rows) [C-17]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b [C-36][C-38][C-39]] | Operation [C-01c [C-38][C-39]] | Ending State [C-01d [C-36][C-38][C-39]] | Preconditions [C-02a [C-38][C-39]] | Postconditions [C-02b [C-38][C-39]] | Invariant 1 [C-03 [C-38][C-39]] | Invariant 2 [C-03 [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Finance Invariant Registry [C-35: consequence — omission fails C-25]:**

Same exclusion list [C-27]. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From (Pass 2 Row #) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 2 Row … |
| INV-F-02 | … | Pass 2 Row … |

**Finance Defect Log [C-40: Pass 2 must carry at least one entry independently — annotate type against C-42 ordering hypothesis; distinct type from Pass 1 confirms hypothesis broadens defect coverage] [C-23]:**

| Defect ID [C-04a] | Type [C-04b [C-38][C-39]] | Triggering Op [C-04c; never blank [C-38][C-39]] | Reason [C-04d; never blank [C-38][C-39]] |
|---|---|---|---|

---

### Pass 3 — Sales Domain [C-42: ordering hypothesis — Sales runs LAST because Sales commercial constraints (close-date enforcement, commission triggers, quota attribution) depend on both CS resolution state and Finance invoice state; this ordering targets **InvalidTransition** defects generated when Sales operations proceed without upstream CS or Finance state preconditions satisfied; three distinct defect types across three passes confirms the ordering hypothesis] [C-37: consequence — invariant registry absent fails C-25]

You are a Sales domain expert. Lifecycle: Lead → Qualified Lead → Opportunity → Proposal →
Closed Won / Closed Lost.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b [C-36][C-38][C-39]] | Operation [C-01c [C-38][C-39]] | Ending State [C-01d [C-36][C-38][C-39]] | Preconditions [C-02a [C-38][C-39]] | Postconditions [C-02b [C-38][C-39]] | Invariant 1 [C-03 [C-38][C-39]] | Invariant 2 [C-03 [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| 1 | Lead | Qualify Lead | Qualified Lead | Contact verified; score ≥ threshold | Stage = Qualified Lead; owner assigned | Owner assigned before stage advances past Qualified Lead | Close date set before stage reaches Proposal |

**Trace table (Sales — minimum 5 rows) [C-17]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b [C-36][C-38][C-39]] | Operation [C-01c [C-38][C-39]] | Ending State [C-01d [C-36][C-38][C-39]] | Preconditions [C-02a [C-38][C-39]] | Postconditions [C-02b [C-38][C-39]] | Invariant 1 [C-03 [C-38][C-39]] | Invariant 2 [C-03 [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Sales Invariant Registry [C-35: consequence — omission fails C-25]:**

Same exclusion list [C-27]. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From (Pass 3 Row #) [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 3 Row … |
| INV-S-02 | … | Pass 3 Row … |

**Sales Defect Log [C-40: Pass 3 must carry at least one entry independently — FAILS if: empty] [C-23]:**

| Defect ID [C-04a] | Type [C-04b [C-38][C-39]] | Triggering Op [C-04c; never blank [C-38][C-39]] | Reason [C-04d; never blank [C-38][C-39]] |
|---|---|---|---|

---

### Section 4 — Cross-Domain Invariant Register [C-25]

Aggregate every invariant from all three passes. Every entry must carry explicit cross-pass
derivation linkage.

| Invariant ID | Description | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 1 Row … |
| INV-F-01 | … | Pass 2 Row … |
| INV-S-01 | … | Pass 3 Row … |

Verify: total transition rows across all three passes ≥ 15 [C-26].

---

### Section 5 — Race Condition Analysis [C-08]

- **Op A:** ___
- **Op B:** ___

**Ordering 1 (Op A first):** State before A; state after A; state after B; conflict or resolution.

**Ordering 2 (Op B first):** Describe fully and independently — do not write "same as above"
or cross-reference Ordering 1 [C-21].

---

### Section 6 — Negative Path [C-09]

| Starting State [C-09a] | Blocked Operation [C-09b] | State After Rejection [C-09c; never blank] | Named Error [C-09d; never blank] |
|---|---|---|---|

**Mutation verification [C-29]:** After the table, write an explicit confirmation sentence
declaring that [C-09c] = [C-09a] and that no field was modified.

---

## V-04 — Step-Block Multi-Pass (Sales → CS) + Lifecycle-Phase Labels + Cross-Domain Chain (C-41, C-43)

**Variation axis:** Output format (step-block multi-pass) + Lifecycle emphasis + Cross-domain
precondition chain
**Hypothesis:** A two-pass step-block format with lifecycle phase labels embedded in Starting
State / Ending State field annotations (C-43) surfaces phase-boundary invariant violations more
clearly than tabular format because each operation block renders the full lifecycle arc visually.
An explicit cross-domain bridge block between the Sales pass and CS pass (C-41) — naming Sales
postconditions that become required CS preconditions — surfaces chain-breaking defects that
within-pass analysis misses entirely. The bridge is a load-bearing structure: its absence makes
the pass 1 → pass 2 dependency implicit and untestable.
**Domain:** Sales (pass 1) / Customer Service (pass 2)
**Key criteria targeted beyond essentials:** C-09, C-10, C-13, C-15, C-16, C-17, C-19, C-22,
C-23, C-24, C-25, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-35, C-38, C-39, C-41, C-43

---

You are a state transition analyst. Hand-compile state transitions for the feature described above
using two sequential domain passes: **Sales first, then Customer Service.**

**Declared lifecycle phases — must appear in every Starting State and Ending State field [C-43:
FAILS if: any state field in any pass contains a state name without its phase label]:**
- Sales: Lead [phase: Acquisition] → Qualified Lead [phase: Qualification] → Opportunity
  [phase: Active Pipeline] → Proposal [phase: Commit Stage] → Closed Won [phase: Post-Sale]
  / Closed Lost [phase: Disqualified]
- CS: New [phase: Intake] → Open [phase: Active Resolution] → Pending [phase: Awaiting Customer]
  → Resolved [phase: Remediation Complete] → Closed [phase: Archived] / Reopened [phase: Re-Active]

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Blank fields are prohibited throughout. Write `none` if a field is genuinely absent [C-32].
- Minimum 5 step blocks per pass [C-17].
- Starting State and Ending State must include lifecycle phase labels in brackets [C-43: FAILS
  if: state name given without a phase label; e.g., "Opportunity" alone fails].
- Field labels are behavioral specifications — do not alter them.
- Prose is not a valid format for trace data [C-16].

---

### Pass 1 — Sales Domain

One step block per operation. No tables. Use the field structure below.

**Reference block — template anchor; do not reproduce in output [C-24]:**

```
Step N [C-01a: sequential 1..N — FAILS if: non-sequential [C-34]] [C-38][C-39]:
  Starting State  [C-01b: declared state name + phase label — directive: always include
                   phase label in brackets — FAILS if: phase label absent; e.g., "Lead"
                   alone fails; must be "Lead [phase: Acquisition]"] [C-43][C-38][C-39]:
                   Lead [phase: Acquisition]
  Operation       [C-01c: one imperative verb phrase — FAILS if: compound] [C-38][C-39]:
                   Qualify Lead
  Ending State    [C-01d: declared state name + phase label — same constraint — FAILS if:
                   phase label absent] [C-43][C-38][C-39]:
                   Qualified Lead [phase: Qualification]
  Preconditions   [C-02a: named attribute; write "none" if absent — FAILS if: vague]
                  [C-38][C-39]:
                  Contact verified; lead score ≥ qualification threshold
  Postconditions  [C-02b: changed attribute; write "none" if absent — FAILS if: restates
                   ending state only] [C-38][C-39]:
                   Stage = Qualified Lead; owner assigned; close date set
  Invariant-1     [C-03: real Sales rule — FAILS if: structural placeholder] [C-38][C-39]:
                   Opportunity owner must be assigned before stage advances past Qualified Lead
  Invariant-2     [C-03: second required — FAILS if: restates Invariant-1] [C-38][C-39]:
                   Close date must be set before stage reaches Proposal
```

**Sales step blocks (minimum 5) [C-17]:**

*(generate Sales step blocks here — Starting State and Ending State must carry lifecycle phase
labels [C-43])*

---

**Sales Invariant Registry [C-35: load-bearing — absent fails C-25]:**

Exclusion list [C-27]: "ID is not null" / "record exists" / "field populated"

| Invariant ID | Description [C-07] | Derived From Block # [C-13] |
|---|---|---|
| INV-S-01 | … | Block … |
| INV-S-02 | … | Block … |

---

**Pass 1 → Pass 2 Cross-Domain Bridge [C-41: this bridge block is the explicit cross-domain
precondition chain annotation — FAILS if: absent; FAILS if: entries are generic rather than
traceable to specific Pass 1 blocks and specific Pass 2 precondition fields; FAILS if:
fewer than two named postcondition-to-precondition links are provided]:**

A CS step block that lists preconditions without tracing them to Sales postconditions is
implicitly relying on this chain without making it testable.

```
Bridge Entry 1 [C-41]:
  Pass 1 source   [cite specific Sales block and postcondition field]:
  Pass 2 consumer [name the CS step block number and precondition field it feeds]:
  Bridge type     [C-41: PreconditionSeed / InvariantPropagation / StateConstraintForward]:

Bridge Entry 2 [C-41]:
  Pass 1 source   [cite specific Sales block and postcondition field]:
  Pass 2 consumer [name the CS step block number and precondition field]:
  Bridge type     [C-41]:
```

---

### Pass 2 — Customer Service Domain

**Reference block — do not reproduce in output [C-24]:**

```
Step N [C-01a; FAILS if: non-sequential [C-34]] [C-38][C-39]:
  Starting State  [C-01b + phase label; FAILS if: phase absent [C-43]] [C-38][C-39]:
  Operation       [C-01c; FAILS if: compound [C-38][C-39]]:
  Ending State    [C-01d + phase label; FAILS if: phase absent [C-43]] [C-38][C-39]:
  Preconditions   [C-02a; named attribute; "none" if absent; FAILS if: vague [C-38][C-39]]:
  Postconditions  [C-02b; changed attribute; "none" if absent; FAILS if: restates ending
                   state [C-38][C-39]]:
  Invariant-1     [C-03; real CS rule; FAILS if: structural placeholder [C-38][C-39]]:
  Invariant-2     [C-03; second required; FAILS if: restates Invariant-1 [C-38][C-39]]:
```

**CS step blocks (minimum 5) [C-17]:**

*(generate CS step blocks here — Starting State and Ending State must carry lifecycle phase
labels [C-43]; preconditions that trace to Pass 1 via the bridge must be annotated
"[Bridge: Pass 1 Block N]")*

---

**CS Invariant Registry [C-35: consequence — omission fails C-25]:**

Same exclusion list [C-27]. Link each to source block [C-13].

| Invariant ID | Description [C-07] | Derived From Block # [C-13] |
|---|---|---|
| INV-C-01 | … | Block … |
| INV-C-02 | … | Block … |

---

**Cross-Domain Invariant Register [C-25]:**

Aggregate all invariants from both passes. Every entry must carry cross-pass derivation linkage.

| Invariant ID | Description | Derived From (Pass + Block) [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 1 Block … |
| INV-C-01 | … | Pass 2 Block … |

Verify: total step blocks across both passes ≥ 10 [C-26].

---

**Defect Log [C-04] — silent omissions invalidate this section [C-23]:**

```
Defect [C-04a] [C-38][C-39]:
  Type           [C-04b: MissingPrecondition / InvalidTransition / InvariantViolation /
                  RaceCondition; FAILS if: omitted] [C-38][C-39]:
  Triggering Op  [C-04c; write "none" if not op-specific; never blank] [C-38][C-39]:
  Reason         [C-04d; specific rule violated; "none" if absent; never blank] [C-38][C-39]:
```

---

**Race Condition Analysis [C-08]:**

Name both operations explicitly [C-28]:
- **Op A:** ___
- **Op B:** ___

```
Ordering 1 (A before B):
  State before A [declared name + phase label [C-43]]:
  State after A  [declared name + phase label [C-43]]:
  State after B  [declared name + phase label [C-43]]:
  Conflict/result:

Ordering 2 (B before A):
  [Describe fully — no cross-references to Ordering 1 [C-21]]
  State before B [phase label required [C-43]]:
  State after B  [phase label required [C-43]]:
  State after A  [phase label required [C-43]]:
  Conflict/result:
```

---

**Negative Path [C-09]:**

```
Negative-Step:
  Starting State     [C-09a + phase label; FAILS if: phase absent [C-43]] [C-38][C-39]:
  Blocked Operation  [C-09b; FAILS if: blank] [C-38][C-39]:
  State After Rejection [C-09c + phase label; "none" if no change; FAILS if: blank [C-43]]
                     [C-38][C-39]:
  Named Error        [C-09d; "none" if absent; FAILS if: blank] [C-38][C-39]:
```

**Mutation verification [C-29]:** After the block, write one explicit confirmation sentence
declaring that [C-09c] = [C-09a] and that no field was modified.

---

## V-05 — All-New-Criteria Ceiling: C-40 + C-41 + C-42 + C-43 + C-44

**Variation axis:** All five new R16 criteria combined
**Hypothesis:** The ceiling combination is: multi-pass tabular with domain ordering as explicit
defect-class hypothesis (C-42) + per-pass labeled defect coverage (C-40) + explicit cross-domain
postcondition-to-precondition bridge annotations (C-41) + lifecycle-phase state annotation at
state field level (C-43) + sub-step decomposition within Defect Analysis blocks (C-44). C-43
and C-44 are format-neutral — inserting them into a multi-pass tabular format that already
carries C-40/C-41/C-42 achieves all five new criteria without format conflict. C-44 is achieved
by decomposing each Defect Analysis entry into 3 mandatory sub-steps (pre-defect state / triggering
operation / post-defect state), each with its own state triple — this is the tabular analog of
V-02's sub-step decomposition.
**Domain:** Finance / Sales / Customer Service (Finance-first, three passes)
**Key criteria targeted beyond essentials:** C-09, C-10, C-11, C-13, C-15, C-16, C-17, C-19,
C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-34, C-35, C-36, C-37,
C-38, C-39, C-40, C-41, C-42, C-43, C-44

---

You are a state transition analyst. Hand-compile state transitions for the feature described above
using three sequential domain passes: **Finance first, then Sales, then Customer Service.**

**Declared lifecycle phases — must appear in every Starting State and Ending State cell [C-43:
FAILS if: any cell contains a state name without the "[phase: ...]" annotation]:**
- Finance: Draft [phase: Authoring] → Submitted [phase: Under Review] → Pending Approval
  [phase: Approval Queue] → Approved [phase: Authorized] → Posted [phase: Ledger Entry] →
  Paid [phase: Settled] / Voided [phase: Cancelled]
- Sales: Lead [phase: Acquisition] → Qualified Lead [phase: Qualification] → Opportunity
  [phase: Active Pipeline] → Proposal [phase: Commit Stage] → Closed Won [phase: Post-Sale]
  / Closed Lost [phase: Disqualified]
- CS: New [phase: Intake] → Open [phase: Active Resolution] → Pending [phase: Awaiting Customer]
  → Resolved [phase: Remediation Complete] → Closed [phase: Archived] / Reopened [phase: Re-Active]

**HARD RULES — any violation invalidates the entire artifact [C-19]:**
- Prose is not a valid format for trace data [C-16].
- Blank cells are prohibited. Write `none` if genuinely absent [C-32].
- Minimum 15 transition rows total across all three passes [C-26].
- Starting State and Ending State cells must carry lifecycle phase labels [C-43: FAILS if: any
  cell contains a state name without the "[phase: ...]" annotation].
- Every pass Defect Analysis block must contain at least one entry with Type + Triggering Op +
  Reason [C-40: FAILS if: any pass block is empty or placeholder].
- Each Defect Analysis entry must include all three mandatory sub-steps (pre-defect state /
  triggering operation / post-defect state), each with an independent state triple [C-44: FAILS
  if: fewer than 3 sub-steps per defect entry; FAILS if: any sub-step lacks its own state reference].
- Column headers are behavioral specifications — do not alter them.

---

### Pass 1 — Finance Domain [C-42: ordering hypothesis — Finance runs FIRST to target **MissingPrecondition** defect class; Finance amount constraints, approval-chain requirements, and posting rules are foundational preconditions for Sales and CS operations; if this hypothesis is correct, Pass 1 Defect Analysis will contain at least one MissingPrecondition entry — a different defect class here signals the hypothesis should shift to V-03 CS-first ordering] [C-37: invariant registry absent fails C-25; consequence: golden threshold unreachable]

You are a Finance domain expert.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — template anchor; do not reproduce in output [C-24]:**

| Step [C-01a: sequential 1..N; FAILS if: non-sequential [C-34]] [C-38][C-39] | Starting State [C-01b: declared name + phase label required — e.g., "Draft [phase: Authoring]" — FAILS FORMAT: no phase label [C-36][C-43]] [C-38][C-39] | Operation [C-01c: one imperative verb phrase; FAILS if: compound [C-34]] [C-38][C-39] | Ending State [C-01d: declared name + phase label; FAILS FORMAT: no phase label [C-36][C-43]] [C-38][C-39] | Preconditions [C-02a: named attribute; "none" if absent; FAILS if: vague [C-34]] [C-38][C-39] | Postconditions [C-02b: changed attribute; "none" if absent; FAILS if: restates ending state [C-34]] [C-38][C-39] | Invariant 1 [C-03: real Finance rule; FAILS if: structural placeholder [C-34]] [C-38][C-39] | Invariant 2 [C-03: second required; FAILS if: restates Inv 1 [C-34]] [C-38][C-39] |
|---|---|---|---|---|---|---|---|
| 1 | Draft [phase: Authoring] | Submit for Approval | Pending Approval [phase: Approval Queue] | Amount > 0; approver identity assigned | Status = Pending Approval; audit entry created | Invoice total must be positive after any line-item modification | Approver identity must be set before status transitions out of Draft |

**Trace table (Finance — minimum 5 rows) [C-17]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b + phase [C-43][C-38][C-39]] | Operation [C-01c [C-38][C-39]] | Ending State [C-01d + phase [C-43][C-38][C-39]] | Preconditions [C-02a [C-38][C-39]] | Postconditions [C-02b [C-38][C-39]] | Invariant 1 [C-03 [C-38][C-39]] | Invariant 2 [C-03 [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Finance Invariant Registry [C-35: load-bearing — absent fails C-25]:**

Exclusion list [C-27]: "ID is not null" / "record exists" / "amount field populated"

Valid example [C-20]: "Invoice total must remain positive after any line-item modification."

| Invariant ID | Description [C-07] | Derived From (Pass 1 Row #) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 1 Row … |
| INV-F-02 | … | Pass 1 Row … |

**Finance Defect Analysis [C-40: at least one entry required for Pass 1 independently — FAILS if: empty] [C-44: each entry must include all three sub-steps each with an independent state triple — FAILS if: fewer than 3 sub-steps] [C-23]:**

```
Defect D-F-01 [C-04a] [C-40][C-44]:
  Type  [C-04b: MissingPrecondition / InvalidTransition / InvariantViolation / RaceCondition
         — annotate against C-42 ordering hypothesis; if not MissingPrecondition, note
         hypothesis-shift signal] [C-38][C-39]:

  Sub-step 1 — Pre-Defect State [C-44: independent before-state — FAILS if absent]:
    State:       [declared Finance state name + phase label [C-43]]
    Observation: [what was true immediately before the defect-triggering operation]

  Sub-step 2 — Triggering Operation [C-44: independent op-state — FAILS if absent]:
    Triggering Op [C-04c: operation name; "none" if not op-specific; never blank [C-38][C-39]]:
    State entering: [declared name + phase label [C-43]]
    State exiting:  [declared name + phase label [C-43]] — or "unchanged" if no transition

  Sub-step 3 — Post-Defect State + Reason [C-44: independent after-state — FAILS if absent]:
    State after:    [declared name + phase label [C-43]]
    Reason [C-04d: specific rule violated; "none" if absent; never blank [C-38][C-39]]:
    Invariant violated: [cite INV-F-NN or "none"]
```

**Pass 1 → Pass 2 Cross-Domain Bridge [C-41: explicit chain — FAILS if: absent; FAILS if:
fewer than 2 named entries; FAILS if: entries not traceable to specific Pass 1 rows and
Pass 2 precondition fields]:**

| Finance Postcondition (Pass 1 Row #) [C-41] | Seeded Sales Precondition (Pass 2 field) [C-41] | Bridge Type [C-41: PreconditionSeed / InvariantPropagation / StateConstraintForward] |
|---|---|---|
| … | … | … |
| … | … | … |

---

### Pass 2 — Sales Domain [C-42: ordering hypothesis — Sales runs SECOND to target **InvalidTransition** defect class; Sales stage advancement depends on Finance authorization state; if Finance-first hypothesis holds, Pass 2 Defect Analysis will contain at least one InvalidTransition traceable to a Finance precondition gap via the Pass 1 → Pass 2 bridge above] [C-37: consequence — invariant registry absent fails C-25]

You are a Sales domain expert.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b + phase [C-43]; FAILS FORMAT: no phase [C-36][C-38][C-39]] | Operation [C-01c; FAILS if: compound [C-34][C-38][C-39]] | Ending State [C-01d + phase [C-43] [C-36][C-38][C-39]] | Preconditions [C-02a; FAILS if: vague [C-34][C-38][C-39]] | Postconditions [C-02b; FAILS if: restates ending state [C-34][C-38][C-39]] | Invariant 1 [C-03; FAILS if: structural [C-34][C-38][C-39]] | Invariant 2 [C-03: second required [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| 1 | Lead [phase: Acquisition] | Qualify Lead | Qualified Lead [phase: Qualification] | Contact verified; score ≥ threshold | Stage = Qualified Lead; owner assigned; close date set | Owner assigned before stage advances past Qualified Lead | Close date set before stage reaches Proposal |

**Trace table (Sales — minimum 5 rows) [C-17]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b + phase [C-43][C-38][C-39]] | Operation [C-01c [C-38][C-39]] | Ending State [C-01d + phase [C-43][C-38][C-39]] | Preconditions [C-02a [C-38][C-39]] | Postconditions [C-02b [C-38][C-39]] | Invariant 1 [C-03 [C-38][C-39]] | Invariant 2 [C-03 [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Sales Invariant Registry [C-35: consequence — omission fails C-25]:**

Same exclusion list [C-27]. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From (Pass 2 Row #) [C-13] |
|---|---|---|
| INV-S-01 | … | Pass 2 Row … |
| INV-S-02 | … | Pass 2 Row … |

**Sales Defect Analysis [C-40: Pass 2 must carry at least one entry independently — FAILS if: empty] [C-44: 3 sub-steps required] [C-23]:**

```
Defect D-S-01 [C-04a] [C-40][C-44]:
  Type  [C-04b; annotate against C-42 ordering hypothesis] [C-38][C-39]:

  Sub-step 1 — Pre-Defect State [C-44; FAILS if absent]:
    State:       [declared Sales state name + phase label [C-43]]
    Observation: [what was true before triggering op]

  Sub-step 2 — Triggering Operation [C-44; FAILS if absent]:
    Triggering Op [C-04c; never blank [C-38][C-39]]:
    State entering: [declared name + phase [C-43]]
    State exiting:  [declared name + phase [C-43]] — or "unchanged"

  Sub-step 3 — Post-Defect State + Reason [C-44; FAILS if absent]:
    State after:    [declared name + phase [C-43]]
    Reason [C-04d; never blank [C-38][C-39]]:
    Bridge dependency: [cite Pass 1 → Pass 2 bridge entry if defect traces to Finance
                        postcondition — "none" if standalone Sales defect]
```

**Pass 2 → Pass 3 Cross-Domain Bridge [C-41: explicit chain from Sales to CS — FAILS if: absent or fewer than 2 named entries]:**

| Sales Postcondition (Pass 2 Row #) [C-41] | Seeded CS Precondition (Pass 3 field) [C-41] | Bridge Type [C-41] |
|---|---|---|
| … | … | … |
| … | … | … |

---

### Pass 3 — Customer Service Domain [C-42: ordering hypothesis — CS runs LAST to target **InvariantViolation** defect class; CS resolution states interact with Finance billing invariants and Sales opportunity states; this is the highest-risk convergence point; three distinct defect types across three passes confirms the ordering hypothesis and achieves maximum defect-class coverage] [C-37: consequence — invariant registry absent fails C-25]

You are a Customer Service domain expert.

**State Transition Table — minimum 5 rows [C-17]**

**Reference row — do not reproduce in output [C-24]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b + phase [C-43]; FAILS FORMAT: no phase [C-36][C-38][C-39]] | Operation [C-01c; FAILS if: compound [C-34][C-38][C-39]] | Ending State [C-01d + phase [C-43] [C-36][C-38][C-39]] | Preconditions [C-02a; FAILS if: vague [C-34][C-38][C-39]] | Postconditions [C-02b; FAILS if: restates ending state [C-34][C-38][C-39]] | Invariant 1 [C-03; FAILS if: structural [C-34][C-38][C-39]] | Invariant 2 [C-03: second required [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| 1 | New [phase: Intake] | Assign to Agent | Open [phase: Active Resolution] | Agent capacity available; customer ID present | Agent ID set; SLA clock running; audit entry created | SLA clock must be active while status is Open or Pending | Customer ID must be non-null for any non-Closed status |

**Trace table (CS — minimum 5 rows) [C-17]:**

| Step [C-01a [C-38][C-39]] | Starting State [C-01b + phase [C-43][C-38][C-39]] | Operation [C-01c [C-38][C-39]] | Ending State [C-01d + phase [C-43][C-38][C-39]] | Preconditions [C-02a [C-38][C-39]] | Postconditions [C-02b [C-38][C-39]] | Invariant 1 [C-03 [C-38][C-39]] | Invariant 2 [C-03 [C-38][C-39]] |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**CS Invariant Registry [C-35: consequence — omission fails C-25]:**

Same exclusion list [C-27]. Link each to source row [C-13].

| Invariant ID | Description [C-07] | Derived From (Pass 3 Row #) [C-13] |
|---|---|---|
| INV-C-01 | … | Pass 3 Row … |
| INV-C-02 | … | Pass 3 Row … |

**CS Defect Analysis [C-40: Pass 3 must carry at least one entry independently — FAILS if: empty] [C-44: 3 sub-steps required] [C-23]:**

```
Defect D-C-01 [C-04a] [C-40][C-44]:
  Type  [C-04b; annotate against C-42 hypothesis — InvariantViolation confirms Finance-first
         hypothesis; different type signals cross-domain bridge gap] [C-38][C-39]:

  Sub-step 1 — Pre-Defect State [C-44; FAILS if absent]:
    State:       [declared CS state name + phase label [C-43]]
    Observation: [what was true before triggering op]

  Sub-step 2 — Triggering Operation [C-44; FAILS if absent]:
    Triggering Op [C-04c; never blank [C-38][C-39]]:
    State entering: [declared name + phase [C-43]]
    State exiting:  [declared name + phase [C-43]] — or "unchanged"

  Sub-step 3 — Post-Defect State + Reason [C-44; FAILS if absent]:
    State after:    [declared name + phase [C-43]]
    Reason [C-04d; never blank [C-38][C-39]]:
    Bridge dependency: [cite Pass 1→2 or Pass 2→3 bridge entry if traceable — "none"
                        if standalone CS defect]
```

---

### Section 4 — Cross-Domain Invariant Register [C-25]

Aggregate every invariant from all three passes. Every entry must carry explicit cross-pass
derivation linkage.

| Invariant ID | Description | Derived From (Pass + Row) [C-13] |
|---|---|---|
| INV-F-01 | … | Pass 1 Row … |
| INV-S-01 | … | Pass 2 Row … |
| INV-C-01 | … | Pass 3 Row … |

Verify: total transition rows across all three passes ≥ 15 [C-26].

---

### Section 5 — Race Condition Analysis [C-08]

Name both concurrent operations explicitly [C-28]:
- **Op A:** ___
- **Op B:** ___

**Ordering 1 (Op A first):**
State before A [declared name + phase label [C-43]]; state after A [+ phase]; state after B
[+ phase]; conflict or resolution named.

**Ordering 2 (Op B first):**
Describe fully and independently — do not write "same as above" or cross-reference Ordering 1
[C-21]. All state references must carry phase labels [C-43].

---

### Section 6 — Negative Path [C-09]

| Starting State [C-09a + phase label [C-43]] | Blocked Operation [C-09b] | State After Rejection [C-09c + phase label; "none" if no change; never blank [C-43]] | Named Error [C-09d; "none" if absent; never blank] |
|---|---|---|---|

**Mutation verification [C-29]:** After the table, write an explicit confirmation sentence
declaring that [C-09c] = [C-09a] and that no field was modified. Passive recording in the
column does not satisfy C-29 — an independent declarative sentence is required.

---

## Scoring Projection Under v14

| Var | New Criteria Expected PASS | Expected FAIL | Notes |
|-----|---------------------------|---------------|-------|
| V-01 | C-40, C-41, C-42 | C-43, C-44 | No phase labels or sub-step decomposition in tabular trace format |
| V-02 | C-43, C-44 | C-40, C-41, C-42 | Single-pass only; no ordering hypothesis or cross-domain bridge |
| V-03 | C-40, C-42 | C-41, C-43, C-44 | No bridge table; no phase labels; no sub-step decomposition |
| V-04 | C-41, C-43 | C-40, C-42, C-44 | Two-pass but no per-pass defect requirement; no ordering hypothesis; no sub-steps |
| V-05 | C-40, C-41, C-42, C-43, C-44 | none | All five new criteria; new ceiling |

**V-05 ceiling projection (v14):**
Inherits prior-round aspirational pass profile (C-09..C-39 from R15 ceiling) + all five new
criteria PASS → 35/35 aspirationals if all prior criteria also pass → aspirational score = 10.0
→ composite ceiling = 50 + 30 + 10 = **90.0**

**Persistent uncracked block:** C-09 through C-16 (8 criteria) remain unaddressed across all
rounds. No variation in R16 specifically targets this block.
