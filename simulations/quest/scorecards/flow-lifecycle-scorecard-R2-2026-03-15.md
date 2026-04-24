# flow-lifecycle — Round 2 Scoring (v2 Rubric)

**Domain**: Invoice-to-Payment Authorization Lifecycle (mid-market financial services firm)

---

## V-01 — Trace Artifact (Terminal Verification Pass Axis)

---

### ROLE REGISTRY

| R-ID | Role Name (domain-qualified) | Department | Primary Responsibility |
|------|------------------------------|------------|------------------------|
| R-01 | Accounts Payable Coordinator | Finance / AP | Receives, validates, and routes invoices; owns PH-01 |
| R-02 | Department Budget Owner | Requesting Business Unit | Approves spend against allocated budget line |
| R-03 | Senior Controller | Finance / Accounting | Reviews high-value invoices above $50k threshold |
| R-04 | Compliance Review Analyst | Legal / Compliance | Sanctions screening and regulatory clearance |
| R-05 | Treasury Authorization Officer | Treasury | Final authorization and payment release |
| R-06 | Payment Processing Specialist | Finance / Operations | Executes payment and confirms bank receipt |

---

### LIFECYCLE PHASES

| Ph-ID | Phase Name | Entry Trigger | Completion Condition | SLA Envelope |
|-------|-----------|--------------|---------------------|--------------|
| PH-01 | Invoice Receipt and Validation | Vendor submits invoice via portal | All fields validated; PO match confirmed | 1 business day |
| PH-02 | Departmental Approval | AP routes validated invoice | Budget owner submits approve/reject decision | 3 business days |
| PH-03 | Controller Escalation | Invoice amount > $50,000 AND budget owner approved | Controller submits approve/reject | 2 business days |
| PH-04 | Compliance Screening | Invoice approved by all relevant approvers | Automated + manual compliance review completed | 1 business day |
| PH-05 | Treasury Authorization | Compliance clearance received | Treasury officer submits authorization decision | 1 business day |
| PH-06 | Disbursement | Treasury authorization confirmed | Bank confirms payment received | 1 business day |

---

### STATE TRACE

| S-ID | Phase | State Name | Owner | Entry Condition | Exit Condition | Exits To |
|------|-------|-----------|-------|-----------------|----------------|---------|
| S-01 | PH-01 | Invoice Received | R-01 | Vendor submits invoice via AP portal | R-01 opens and logs invoice with ERP timestamp | S-02 |
| S-02 | PH-01 | Validation In Progress | R-01 | Invoice logged and assigned to AP queue | All fields (vendor ID, PO#, line amounts, tax) validated against PO; duplicate check cleared | S-03 (pass) or T-02 (validation failure) |
| S-03 | PH-02 | Pending Budget Owner Approval | R-02 | AP routes validated invoice to budget owner task queue | Budget owner opens review task | S-04 |
| S-04 | PH-02 | Budget Owner Review Active | R-02 | Review task opened | Budget owner submits approve/reject/escalate decision | S-05 (>$50k, approved) or S-06 (≤$50k, approved) or T-02 (rejected) |
| S-05 | PH-03 | Controller Escalation Review | R-03 | Invoice amount > $50,000 and budget owner approved | Controller submits approve/reject decision | S-06 (approved) or T-02 (rejected) |
| S-06 | PH-04 | Compliance Screening In Progress | R-04 | Invoice approved by all required approvers | Automated sanctions check AND manual vendor verification both complete | S-07 (clear) or T-04 (sanctions hit) |
| S-07 | PH-05 | Treasury Authorization Pending | R-05 | Compliance clearance logged | Treasury officer submits authorize/hold decision | S-08 (authorized) or T-02 (held/rejected) |
| S-08 | PH-06 | Payment Queued | R-06 | Treasury authorization confirmed | Payment file accepted by bank interface system | S-09 |
| S-09 | PH-06 | Payment Initiated | R-06 | Payment file submitted to bank | Bank returns confirmation ACK or timeout threshold exceeded | T-01 (confirmed) or T-03 (cancelled after 3 timeout cycles) |

---

### DECISION POINTS

```
Decision:   Is the invoice complete and PO-matched?
Owner:      R-01
Condition:  All required fields present; invoice amount matches PO line totals within tolerance; vendor ID active in master data
Branch A:   Pass → S-03
Branch B:   Fail → T-02 (return to vendor with deficiency notice)
Fallback:   If PO cannot be located, R-01 escalates to R-02 for PO retrieval; 2-day hold before return to vendor
```

```
Decision:   Does the invoice amount exceed the department controller threshold ($50,000)?
Owner:      R-02
Condition:  Total invoice amount compared to department-configured threshold; multi-line invoices use aggregate total
Branch A:   Exceeds → S-05 (controller escalation)
Branch B:   Within threshold → S-06 (compliance screening)
Fallback:   If department threshold is unconfigured, default to controller review (conservative path)
```

```
Decision:   Is the vendor compliance-cleared?
Owner:      R-04
Condition:  Automated OFAC/EU sanctions screening result AND manual vendor master verification (both required)
Branch A:   Clear → S-07
Branch B:   Flagged → T-04
Fallback:   If screening API unavailable > 4 hours, R-05 notified; invoice held at S-06 pending system recovery
```

```
Decision:   Does Treasury authorize payment release?
Owner:      R-05
Condition:  Available cash balance, vendor payment terms, strategic hold flags, and dispute register check
Branch A:   Authorized → S-08
Branch B:   Held or rejected → T-02
Fallback:   If R-05 unavailable, secondary Treasury Authorization Officer covers under Business Continuity protocol
```

---

### PARALLEL PATHS

```
Fork state:     S-06 (Compliance Screening In Progress)
Branch A:       Automated sanctions screening — OFAC/EU list check (R-04 automated tooling)
Branch B:       Manual vendor master verification — address, bank account, ownership chain (R-04 manual review)
Join condition: Automated result returned AND manual verification logged; neither branch can be skipped
Join owner:     R-04
Downstream:     S-07 (if both clear) or T-04 (if either flags)
```

---

### EXCEPTION FLOW CATALOG

```
E-ID:        E-01
Name:        Duplicate Invoice Detected
Origin:      S-02
Trigger:     ERP duplicate check matches invoice number or amount+vendor combination against payments in the prior 90 days
Phase:       PH-01
Divergence:  At S-02, instead of routing to S-03, AP triggers the Duplicate Invoice Review workflow; vendor is notified and asked to confirm uniqueness or void the duplicate
Recovery:    T-02 — invoice returned to vendor (recoverable if vendor issues a corrected invoice with new invoice number; corrected invoice re-enters at S-01)
```

```
E-ID:        E-02
Name:        Budget Exhausted
Origin:      S-04
Trigger:     Budget owner confirms invoice is valid but the budget line is fully consumed for the fiscal period
Phase:       PH-02
Divergence:  At S-04, budget owner rejects with reason code "Budget Exhausted"; this triggers a Budget Reallocation Request subprocess (outside this lifecycle); if reallocation is approved within 5 business days, invoice re-enters at S-03
Recovery:    S-03 (re-entry on reallocation approval) or T-02 (terminal if reallocation denied or expires)
```

```
E-ID:        E-03
Name:        Sanctions Hit
Origin:      S-06
Trigger:     Automated screening returns positive match against OFAC Specially Designated Nationals list or EU Consolidated Sanctions List
Phase:       PH-04
Divergence:  At S-06, R-04 escalates to Legal Counsel rather than clearing to S-07; a Regulatory Hold notice is issued; legal hold duration is indefinite pending government guidance
Recovery:    T-04 — Invoice Voided (compliance block; not recoverable within this lifecycle)
```

```
E-ID:        E-04
Name:        Payment System Timeout
Origin:      S-09
Trigger:     Bank interface returns no confirmation ACK within 24 hours of file submission
Phase:       PH-06
Divergence:  At S-09, R-06 initiates bank trace request; if bank confirms non-receipt, payment file is re-submitted (retry cycle); maximum 3 retry attempts before cancel
Recovery:    S-09 retry (if bank confirms non-receipt and re-submission succeeds) → T-01; or T-03 (cancelled after 3 failed attempts)
```

---

### BOTTLENECK AND GAP REGISTER

| B-ID | Type | Name | Cause | Downstream Impact |
|------|------|------|-------|-------------------|
| B-01 | bottleneck | Controller Escalation Queue Depth | R-03 is a single point of review for all invoices > $50k across all departments; queue reaches 40+ items during month-end close | High-value invoices held 2–5 days beyond SLA; vendor payment terms violated; early-pay discount windows missed |
| B-02 | bottleneck | Compliance Screening API Availability | Automated sanctions screening depends on a single-vendor API; planned maintenance windows and unplanned outages pause all invoices at S-06 | Compliance holds accumulate; invoice aging increases; treasury cannot act on held items |
| G-01 | gap | No Milestone Payment Workflow | The lifecycle has no sub-phase for partial or milestone-based payments on phased vendor contracts; missing: split payment authorization with per-milestone controller sign-off | Full invoice amount authorized before deliverables are complete; contract terms violated; vendor overpaid relative to work product received |

---

### EDGE CASE REGISTER

```
Edge case:    Foreign Currency Invoice
Scenario:     Vendor invoices in EUR but the corresponding PO is denominated in USD; validation at S-02 compares numeric amounts only
Gap reason:   Validation module has no currency normalization step; FX rate is not applied before PO-match comparison
Consequence:  Invoices rejected incorrectly due to apparent amount mismatch; or approved with FX exposure unquantified and unhedged
```

```
Edge case:    Vendor Remittance Address Changed Mid-Lifecycle
Scenario:     Vendor requests new bank routing details after S-07 (Treasury Authorization Pending) but before S-08 (Payment Queued)
Gap reason:   No re-verification step exists between treasury authorization and payment queueing; vendor master updates take effect immediately in ERP
Consequence:  Payment sent to stale account; vendor dispute raised; potential regulatory exposure for misdirected funds in jurisdictions with payment finality rules
```

---

### SLA AND TIMING ANNOTATION

| S-ID | Expected Duration | At-Risk Threshold | AT-RISK? | Bottleneck Reference |
|------|------------------|-------------------|----------|-----------------------|
| S-05 | 2 business days | > 3 business days | Y | B-01 — Controller queue depth during month-end close |
| S-06 | 4 hours (automated) + 4 hours (manual) | > 1 business day total | Y | B-02 — Screening API outage causes indefinite hold |
| S-09 | 4 business hours | > 24 hours with no ACK | Y | External (bank interface latency; no internal bottleneck owner) |

---

### CROSS-LIFECYCLE HANDOFF

| T-ID | Recipient Lifecycle | Handoff Trigger | Fields Passed | Coupling State |
|------|---------------------|-----------------|---------------|----------------|
| T-01 | Vendor Account Management Lifecycle | Bank payment confirmation ACK received | Payment reference, vendor ID, PO#, disbursed amount, payment date, bank trace ID | Loose — downstream lifecycle reads payment record; no callback required |

---

### TERMINAL DECLARATION

| T-ID | Terminal Name | Type | Last Owner |
|------|--------------|------|------------|
| T-01 | Payment Disbursed | success | R-06 |
| T-02 | Invoice Rejected | failure | R-01 (validation), R-02 (budget reject), R-03 (controller reject), R-05 (treasury hold) |
| T-03 | Payment Cancelled | cancel | R-06 |
| T-04 | Invoice Voided — Compliance Block | failure | R-04 |

---

### TERMINAL VERIFICATION PASS

For every traced path — happy path and each named exception — declare which terminal it reaches. Any row marked OPEN is an incomplete trace.

| Path | Type | Final State Before Terminal | Terminal Reached | Verified? |
|------|------|-----------------------------|-----------------|-----------|
| Happy path | happy | S-09 (Payment Initiated → bank ACK received) | T-01 | Y |
| E-01: Duplicate Invoice Detected | exception | S-02 (Validation In Progress → duplicate match) | T-02 | Y |
| E-02: Budget Exhausted (reallocation denied) | exception | S-04 (Budget Owner Review Active → reallocation expires) | T-02 | Y |
| E-02: Budget Exhausted (reallocation approved) | exception | S-09 (re-enters S-03 → completes happy path) | T-01 | Y |
| E-03: Sanctions Hit | exception | S-06 (Compliance Screening → legal hold issued) | T-04 | Y |
| E-04: Payment Timeout (cancelled) | exception | S-09 (3rd retry exhausted) | T-03 | Y |
| E-04: Payment Timeout (resolved) | exception | S-09 (retry succeeds → bank ACK) | T-01 | Y |
| Parallel join failure (compliance screening — one branch flags) | exception | S-06 (one branch of parallel fails) | T-04 | Y |

**Verification rule applied:** All E-IDs present. All S-IDs with no outbound transition confirmed as final states before terminal. No OPEN rows.

---

## V-02 — Structural Delta: Role-First Anchoring

**Variation axis:** C-11 — Roles are the first substantive section; includes a concrete domain-title anchor statement that gates all downstream vocabulary.

**Structural innovation added above the Phase table:**

---

> **ROLE ANCHOR DECLARATION** — All roles in this artifact are domain-qualified titles. No generic placeholders ("Approver," "Reviewer," "Owner") appear anywhere in this document. Roles established here are the only valid role identifiers for states, decision points, and exception flows. Any reference to a role not in this table is a structural error.
>
> Anchor example: **R-03 is "Senior Controller"** — not "Finance Approver," not "Controller," not "Finance Team." The domain-qualified title signals: this person carries professional certification, is accountable to the CFO, and has legal sign-off authority on disbursements. This distinction matters because C-05 failures occur when generic titles obscure accountability at decision gates.

---

**Identical content thereafter** (same phases, states, decision points, exceptions, terminals as V-01).

**C-13 HOLD materialization:** V-02 includes implicit sequential dependency language within the State Trace ("S-05 cannot be reached unless S-04 approves") but does not name it as a **gate** — partial rather than full C-13 pass.

**No TERMINAL VERIFICATION PASS section** (C-14 not targeted in V-02).

---

## V-03 — Structural Delta: Anti-Pattern Negation

**Variation axis:** C-12 — Named failure modes with concrete counter-examples block the most common rubric misses.

**Structural innovation — ANTI-PATTERN NEGATION section prepended:**

---

> **ANTI-PATTERN NEGATION**
>
> **Failure Mode 1 — Vague Transition Language**
> Weak: "Once the Controller reviews, the invoice moves to Compliance."
> Correct (this artifact): "At S-05, the exit condition is **Controller submits approve/reject decision**; approval routes to S-06, rejection routes to T-02."
> Why it matters: "moves to" hides what event triggers the transition and who owns it, making the trace non-executable.
>
> **Failure Mode 2 — Generic Role Names**
> Weak: "Approver," "Reviewer," "Finance Team"
> Correct (this artifact): "R-03: Senior Controller" — a specific title carrying legal sign-off authority.
> Why it matters: generic role names pass a count check on C-05 while leaving decision ownership ambiguous at every gate.
>
> **Failure Mode 3 — Terminal Count Without Path Verification**
> Weak: Declaring "T-01: success, T-02: failure" without confirming which exception paths reach which terminal.
> Correct (this artifact): Each exception flow (E-01 through E-04) explicitly names its recovery or terminal state, not just a list.
> Why it matters: a count of two terminals can be satisfied while leaving exception branches dangling.

---

**No TERMINAL VERIFICATION PASS table** (C-14 not targeted in V-03).
**No ROLE ANCHOR DECLARATION** (C-11 not targeted).
**No gate-locking language** (C-13 not targeted).

---

## V-04 — Structural Delta: Role-First + Sequential Gate Locking

**Variation axes:** C-11 (role-first anchoring) + C-13 (sequential gate locking).

**Additions above and within the Phase table:**

**ROLE ANCHOR DECLARATION** (same as V-02 — see above).

**SEQUENTIAL GATE DECLARATIONS** — embedded at critical sequence boundaries:

---

> **GATE G-1 (protects C-01 — State Transition Coverage):**
> Do not assign a state owner until the Role Registry is complete and all R-IDs are finalized. Any state referencing an R-ID not present in the registry is a structural error. Complete the Role Registry before writing a single state row.

> **GATE G-2 (protects C-03 — Terminal State Completeness):**
> Do not trace exception flows until the Terminal Declaration table is written. Every exception flow must name a T-ID from the terminal table as its recovery or terminal state. A T-ID referenced in an exception flow that does not appear in the terminal table is an open path.

> **GATE G-3 (protects C-02 — Exception Flow Traces):**
> Do not complete the artifact until all three required exception flows have named: (1) triggering condition, (2) divergence phase/state, and (3) recovery S-ID or terminal T-ID. Partial exception flows (trigger only, or divergence only) do not count toward the C-02 minimum.

---

**No TERMINAL VERIFICATION PASS table** (C-14 not targeted).
**No ANTI-PATTERN NEGATION** (C-12 not targeted).

---

## V-05 — Structural Delta: Full v2 Aspirational Ceiling

**Variation axes:** C-11 + C-12 + C-13 + C-14 (all four).

Combines:
- **ROLE ANCHOR DECLARATION** (from V-02/V-04)
- **ANTI-PATTERN NEGATION** section (from V-03)
- **SEQUENTIAL GATE DECLARATIONS G-1, G-2, G-3** (from V-04)
- **TERMINAL VERIFICATION PASS** table (from V-01), fully populated

The anti-pattern negation adds a **fourth failure mode** not present in V-03:

> **Failure Mode 4 — Gate Sequence Violation**
> Weak: Writing exception flows that reference a terminal (e.g., T-04) before the terminal table is defined, leaving the terminal provisional.
> Correct (this artifact): Gate G-2 enforces that the terminal table is finalized before any exception flow references a T-ID. The terminal verification pass then confirms all exception flows land.

---

## Scoring

### V-01 — Terminal Verification Pass

| Criterion | Category | Result | Evidence |
|-----------|----------|--------|---------|
| C-01 State Transition Coverage | correctness | **PASS** | 9 named states; every state has explicit entry trigger and exit trigger referencing event names (e.g., "R-03 submits decision", "Bank returns ACK") |
| C-02 Exception Flow Traces | coverage | **PASS** | 4 exception flows (E-01–E-04); each names triggering condition, phase, divergence step, and recovery/terminal |
| C-03 Terminal State Completeness | correctness | **PASS** | T-01 success + T-02/T-03/T-04 failure/cancel; all traced paths in state trace exit to a named terminal |
| C-04 Bottleneck and Gap | depth | **PASS** | B-01 (queue depth + SLA impact), B-02 (API availability + hold accumulation), G-01 (milestone payments — missing step named + overpayment consequence) |
| C-05 Domain Role Assignment | correctness | **PASS** | 6 domain-qualified roles; every decision point names owner R-ID; no generic placeholders |
| C-06 Parallel Path Modeling | depth | **PASS** | S-06 parallel: automated sanctions + manual vendor verification; join condition explicit; join owner R-04 |
| C-07 Decision Point Explicitness | format | **PASS** | 4 decision points; each has condition, owner R-ID, Branch A/B, and fallback |
| C-08 Edge Case Enumeration | coverage | **PASS** | EC-01 (FX mismatch) and EC-02 (remittance change mid-lifecycle); both distinct from E-01–E-04; gap reason and consequence stated |
| C-09 Cross-Lifecycle Dependencies | depth | **PASS** | T-01 → Vendor Account Management Lifecycle; direction, fields passed, coupling state all named |
| C-10 SLA and Timing Annotation | depth | **PASS** | S-05, S-06, S-09 annotated; S-05 and S-06 AT-RISK with B-01 and B-02 references |
| C-11 Role-First Anchoring | structure | **PARTIAL** | Role Registry appears before State Trace (table order satisfies intent); no explicit ROLE ANCHOR DECLARATION section; no anti-generic statement |
| C-12 Anti-Pattern Negation | clarity | **FAIL** | No anti-pattern section; failure modes not named; rubric misses not blocked explicitly |
| C-13 Sequential Gate Locking | structure | **FAIL** | No explicit gate declarations; no "do not proceed until X" language |
| C-14 Terminal Verification Pass | correctness | **PASS** | Per-path table present; 8 paths covered; E-01–E-04 all appear; no OPEN rows; verification rule stated and applied |

**Aspirational passes:** C-09 (1), C-10 (1), C-11 (0.5), C-12 (0), C-13 (0), C-14 (1) = **3.5 / 6**

```
score = (5/5 × 60) + (3/3 × 30) + (3.5/6 × 10)
      = 60 + 30 + 5.83
      = 95.8 → 96
```

---

### V-02 — Role-First Anchoring

| Criterion | Category | Result | Evidence |
|-----------|----------|--------|---------|
| C-01 | correctness | **PASS** | Same trace as V-01 |
| C-02 | coverage | **PASS** | Same trace |
| C-03 | correctness | **PASS** | Same terminals |
| C-04 | depth | **PASS** | Same register |
| C-05 | correctness | **PASS** | Same roles |
| C-06 | depth | **PASS** | Same parallel path |
| C-07 | format | **PASS** | Same decision points |
| C-08 | coverage | **PASS** | Same edge cases |
| C-09 | depth | **PASS** | Same handoff |
| C-10 | depth | **PASS** | Same SLA annotation |
| C-11 Role-First Anchoring | structure | **PASS** | Explicit ROLE ANCHOR DECLARATION section; "Senior Controller" vs "Finance Approver" example; anti-generic statement present; roles appear before phases and states |
| C-12 | clarity | **FAIL** | No anti-pattern section |
| C-13 | structure | **PARTIAL** | Implicit sequential dependency language in state trace ("S-05 cannot be reached unless S-04 approves") but no named gates or explicit "do not proceed" declarations |
| C-14 | correctness | **FAIL** | No terminal verification pass table |

**Aspirational passes:** C-09 (1), C-10 (1), C-11 (1), C-12 (0), C-13 (0.5), C-14 (0) = **3.5 / 6**

```
score = 60 + 30 + (3.5/6 × 10) = 60 + 30 + 5.83 = 95.8 → 96
```

---

### V-03 — Anti-Pattern Negation

| Criterion | Category | Result | Evidence |
|-----------|----------|--------|---------|
| C-01 | correctness | **PASS** | Same trace |
| C-02 | coverage | **PASS** | Same exceptions |
| C-03 | correctness | **PASS** | Same terminals |
| C-04 | depth | **PASS** | Same register |
| C-05 | correctness | **PASS** | Same roles |
| C-06 | depth | **PASS** | Same parallel path |
| C-07 | format | **PASS** | Same decision points |
| C-08 | coverage | **PASS** | Same edge cases |
| C-09 | depth | **PASS** | Same handoff |
| C-10 | depth | **PASS** | Same SLA annotation |
| C-11 | structure | **PARTIAL** | Role Registry appears before states (table order); no ROLE ANCHOR DECLARATION; anti-generic pattern named in anti-pattern section but not as a role-anchor gate |
| C-12 Anti-Pattern Negation | clarity | **PASS** | Three named failure modes, each with weak/correct contrast, each blocking a specific rubric miss (vague transitions, generic roles, terminal count without path check) |
| C-13 | structure | **FAIL** | No gate declarations |
| C-14 | correctness | **FAIL** | No terminal verification pass table |

**Aspirational passes:** C-09 (1), C-10 (1), C-11 (0.5), C-12 (1), C-13 (0), C-14 (0) = **3.5 / 6**

```
score = 60 + 30 + (3.5/6 × 10) = 60 + 30 + 5.83 = 95.8 → 96
```

---

### V-04 — Role-First + Sequential Gate Locking

| Criterion | Category | Result | Evidence |
|-----------|----------|--------|---------|
| C-01 | correctness | **PASS** | Same trace |
| C-02 | coverage | **PASS** | Same exceptions |
| C-03 | correctness | **PASS** | Same terminals |
| C-04 | depth | **PASS** | Same register |
| C-05 | correctness | **PASS** | Same roles |
| C-06 | depth | **PASS** | Same parallel path |
| C-07 | format | **PASS** | Same decision points |
| C-08 | coverage | **PASS** | Same edge cases |
| C-09 | depth | **PASS** | Same handoff |
| C-10 | depth | **PASS** | Same SLA annotation |
| C-11 Role-First Anchoring | structure | **PASS** | ROLE ANCHOR DECLARATION present; "Senior Controller" example; roles finalized before any state row |
| C-12 | clarity | **FAIL** | No anti-pattern section |
| C-13 Sequential Gate Locking | structure | **PASS** | Three named gates: G-1 (role registry before states, protects C-01), G-2 (terminals before exception flows, protects C-03), G-3 (exception flow completeness check, protects C-02); each references the criterion it protects |
| C-14 | correctness | **FAIL** | No terminal verification pass table |

**Aspirational passes:** C-09 (1), C-10 (1), C-11 (1), C-12 (0), C-13 (1), C-14 (0) = **4 / 6**

```
score = 60 + 30 + (4/6 × 10) = 60 + 30 + 6.67 = 96.67 → 97
```

---

### V-05 — Full Aspirational Ceiling

| Criterion | Category | Result | Evidence |
|-----------|----------|--------|---------|
| C-01 | correctness | **PASS** | Same trace |
| C-02 | coverage | **PASS** | Same exceptions |
| C-03 | correctness | **PASS** | Same terminals |
| C-04 | depth | **PASS** | Same register |
| C-05 | correctness | **PASS** | Same roles |
| C-06 | depth | **PASS** | Same parallel path |
| C-07 | format | **PASS** | Same decision points |
| C-08 | coverage | **PASS** | Same edge cases |
| C-09 | depth | **PASS** | Same handoff |
| C-10 | depth | **PASS** | Same SLA annotation |
| C-11 Role-First Anchoring | structure | **PASS** | ROLE ANCHOR DECLARATION; "Senior Controller" example; roles gate downstream vocabulary |
| C-12 Anti-Pattern Negation | clarity | **PASS** | Four failure modes; each names weak form, correct form, and why the distinction matters; Failure Mode 4 cross-references G-2 (gate sequence violation) |
| C-13 Sequential Gate Locking | structure | **PASS** | Gates G-1, G-2, G-3 each name the criterion they protect and the "do not proceed" dependency |
| C-14 Terminal Verification Pass | correctness | **PASS** | Per-path table with 8 rows; all E-IDs present; no OPEN rows; verification rule stated and applied; structural confirmation not a count check |

**Aspirational passes:** C-09 (1), C-10 (1), C-11 (1), C-12 (1), C-13 (1), C-14 (1) = **6 / 6**

```
score = 60 + 30 + (6/6 × 10) = 60 + 30 + 10 = 100
```

---

## Summary Ranking

| Rank | Variation | Score | All Essential | New Aspirational Passed |
|------|-----------|-------|:-------------:|-------------------------|
| 1 | **V-05** | **100** | Y | C-11, C-12, C-13, C-14 |
| 2 | **V-04** | **97** | Y | C-11, C-13 |
| 3 (tie) | **V-01** | **96** | Y | C-14 |
| 3 (tie) | **V-02** | **96** | Y | C-11 |
| 3 (tie) | **V-03** | **96** | Y | C-12 |

**Golden threshold met:** All variations — all essential pass AND composite ≥ 80.

---

## Excellence Signals

**V-05 patterns that drove the ceiling:**

1. **Gate-criterion binding**: Each sequential gate (G-1/G-2/G-3) explicitly references the rubric criterion it protects (`"do not proceed until X — this gate enforces C-03"`). The gate is not a stylistic note; it is a structural enforcer with a named accountability target.

2. **Anti-pattern negation amplifies gate locking**: Failure Mode 4 in V-05's anti-pattern section names the specific way gate sequence violations manifest (referencing a T-ID before the terminal table exists). Anti-pattern + gate works better than either alone — the anti-pattern explains *why* the gate exists; the gate enforces *when* the rule applies.

3. **Per-path terminal verification vs. count-based terminal declaration**: The TERMINAL VERIFICATION PASS table makes dangling exception branches visible as blank rows rather than invisible omissions. The critical design is the **verification rule statement** — "any row marked OPEN is an incomplete trace" — which turns a reviewer check into a structural invariant.

4. **Role-first anchoring as vocabulary gate, not just formatting order**: The strength of C-11 in V-02/V-04/V-05 is not that the role table appears first, but that the ROLE ANCHOR DECLARATION explicitly states that all downstream content is invalid without it. This transforms a table ordering convention into a dependency declaration.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["gate-criterion binding: each sequential gate names the rubric criterion it protects, making enforcement traceable", "anti-pattern + gate synergy: anti-pattern section explains why a gate exists; gate enforces when the rule applies — neither alone achieves both", "per-path terminal verification converts count-check into structural invariant via OPEN-row visibility rule", "role-first anchoring works as a vocabulary gate when paired with an explicit dependency declaration, not just as table ordering"]}
```
