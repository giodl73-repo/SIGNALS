Written to `simulations/quest/variations/flow-lifecycle-variations-R5-2026-03-14.md`.

---

## Round 5 Variations -- flow-lifecycle

### Summary

| V | Axis | C-22 | C-23 | Prediction |
|---|------|------|------|------------|
| **V-01** | C-22 isolation -- block-hint-only format contract | block-hint only | global preamble (preserved) | PASS |
| **V-02** | C-22 isolation -- preamble-only concrete named example | preamble only | global preamble (preserved) | PASS |
| **V-03** | C-23 isolation -- section-level anti-embedding only | preamble + per-block (preserved) | CHAIN STATUS section only | PASS |
| **V-04** | Combined minimum -- block-hint C-22 + section-only C-23 | block-hint only | CHAIN STATUS section only | PASS |
| **V-05** | Full R5 synthesis -- dual-location both criteria | preamble (concrete) + per-block (concrete, consistent) | global preamble + section instruction | PASS (golden) |

### What was varied

The two new v5 criteria are purely about **placement** of constraints that already exist in V-05 R4:

**C-22 axis (Evidence format contract location):**
- V-01: removed preamble format rule; added bracket template + fail condition to each per-block hint
- V-02: added concrete named example to preamble; per-block hints become minimal (`[Per format contract in preamble above]`)
- V-05: preamble gets concrete named example; per-block hints get concrete example + format pattern; B-01/B-02 inconsistency from R4 corrected (both blocks now use the same hint form)

**C-23 axis (anti-embedding instruction location):**
- V-03: removed global preamble anti-embedding; added explicit `STRUCTURAL CONSTRAINT: Do not embed chain status inside SLA ANALYSIS` as the opening line of the CHAIN STATUS section instruction
- V-04: same C-23 change as V-03, combined with V-01's C-22 change
- V-05: keeps global preamble anti-embedding AND adds the section-level prohibition for dual enforcement

**Key diagnostic question:** Is per-block proximity or preamble distance the load-bearing enforcement point for C-22? Is section-level or global-preamble placement sufficient for C-23? V-01/V-02/V-03 isolate each question; V-04 tests minimum-viable-form; V-05 provides maximum structural redundancy.
sufficiency.
  C-23 preserved from V-05 R4 (global preamble anti-embedding intact).

- **V-02** -- C-22 single axis: put concrete named example + fail condition in preamble ONLY;
  per-block hints become minimal references. Tests preamble-only sufficiency when preamble uses
  a concrete `S-05: Credit Hold Review` example. C-23 preserved from V-05 R4.

- **V-03** -- C-23 single axis: remove global preamble anti-embedding prohibition; add explicit
  anti-embedding as a named constraint inside the CHAIN STATUS section instruction. Tests
  section-level proximity vs. global preamble distance. C-22 preserved from V-05 R4
  (preamble + per-block format contract intact).

- **V-04** -- Combined minimum: block-hint-only C-22 + section-instruction-only C-23. Neither
  criterion has a preamble-level enforcement point. Tests minimum viable placement for both.

- **V-05** -- Full R5 synthesis: concrete named example in preamble AND per-block hints (C-22
  at both locations); anti-embedding in global preamble AND CHAIN STATUS section instruction
  (C-23 at both locations). Corrects the V-05 R4 inconsistency where B-01 and B-02 had
  different per-block hint styles.

### Predicted scores against v5 rubric

All variations carry forward the full V-05 R4 base: SECTION A/B labels (C-18), constructed-answer
blocks (C-17/C-21), role registry (C-12), phase-scoped exceptions (C-13/C-15), dedicated CHAIN
STATUS section (C-20/C-23 candidate), Evidence field (C-19 candidate). Only the C-22 and C-23
enforcement locations vary.

| V | C-22 form | C-23 form | Both pass? | Notes |
|---|-----------|-----------|------------|-------|
| V-01 | block-hint only | global preamble | Predicted both | Diagnostic: does proximity in block hint = sufficient? |
| V-02 | preamble only (concrete example) | global preamble | Predicted both | Diagnostic: does preamble-only contract propagate? |
| V-03 | preamble + block hints (V-05 R4) | section-instruction only | Predicted both | Diagnostic: is proximate section-level anti-embed sufficient? |
| V-04 | block-hint only | section-instruction only | Predicted both | Diagnostic: minimum form -- no preamble for either |
| V-05 | preamble + block hints (both concrete) | global preamble + section instruction | Predicted both | Full synthesis -- maximum redundancy |

---

## V-01: C-22 Isolation -- Block-Hint-Only Format Contract

**Axis:** Output format -- Evidence format contract (bracket template + fail condition) lives
exclusively in per-block B-NN hints; preamble carries no Evidence format rule.
**Hypothesis:** A per-block Evidence hint that provides (a) the bracket template
`[State name -- S-ID]: AT-RISK, causal source: B-[ID]` and (b) an explicit fail condition for
general references satisfies C-22 at the block level without a preamble-level format instruction.
The rubric allows "in the block hint or a preamble" -- this tests block-hint-only sufficiency.
C-23 preserved (global preamble anti-embedding + dedicated CHAIN STATUS section from V-05 R4).

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: SECTION A -- EXCEPTIONS is always written before SECTION B -- STATES.
  SECTION A is the single structural mechanism for phase-scoped exception generation (C-13),
  exception-first position (C-15), and constructed-answer completeness (C-17).
  Do not introduce any separate mechanism for any of these three requirements outside SECTION A.
Exception flows and edge cases are written as per-item answer blocks, not table rows.
Bottleneck entries are written as per-item answer blocks with mandatory SLA Nodes Affected: and Evidence: fields.
Every blank sub-field in any answer block is a visible incomplete answer -- do not leave any empty.
Every AT-RISK SLA row must cite a B-ID; every B-ID must name its SLA Nodes Affected (bidirectional).
The CHAIN STATUS section is a required top-level section after SLA ANALYSIS.
  It declares CLOSED or OPEN as its first element, then enumerates all verified B-IDs and AT-RISK rows.
  Do not embed chain status as a line or annotation inside the SLA ANALYSIS section.
Do not reorder, rename, or remove any section header, sub-section label, column header, or field label.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before writing any PHASE section. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O        -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P        -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE       -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate:
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- add if the process type supports cancellation]

## PHASE MAP
| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Last phase Downstream Handoff must reference a TERMINAL state.]

---

[Write one PHASE block for every phase in the PHASE MAP.
Within each PHASE block: SECTION A is always first, SECTION B is always second.
SECTION A is the single unified mechanism for phase-scoped exception generation, exception-first
position, and constructed-answer completeness. Do not add exception content outside SECTION A.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### SECTION A -- EXCEPTIONS IN THIS PHASE
[This section is always the first declared output element in every phase block.
Write failure modes specific to this phase before any state detail is available.
Phase context is the scope: only generate exceptions whose trigger condition is plausible in this phase.
Generic exceptions (system error, network timeout) that apply to any phase are not acceptable.
Write each exception as a per-item answer block. A blank sub-field is a visible incomplete answer.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.]

E-[N] -- [Exception Name]:
  Trigger state: S-[ID]: [state name -- must be a state in SECTION B of this phase]
  Trigger: [Phase-specific condition -- must be specific to work done in this phase]
  Trace: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

[Add one block per exception specific to this phase. All five sub-fields required per block.]

### SECTION B -- STATES IN THIS PHASE
[Written after SECTION A. Entry Condition and Exits columns required for every row.
Owner column must be an R-ID. Exit format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]".]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks for This Phase
[One block per DECISION-type state in SECTION B.
Write "No DECISION-type states in this phase." if none.
Fallback: (required) is a required field -- do not write "n/a".]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule or data threshold -- process and phase specific, not "if approved"]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch condition is met] -> S-[ID]: [destination]
            [If exhaustive: "Exhaustive -- reason: [explain why no unhandled input is possible]"]

### Parallel Work Streams in This Phase
Fork: S-[ID] -> Branch A (R-[N]): [state list] | Branch B (R-[N]): [state list] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver before join fires]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase or TERMINAL:name]

---

[Repeat the PHASE block for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS

[Bottleneck entries are per-item answer blocks.
The SLA Nodes Affected: field is required -- it names the state(s) in SLA ANALYSIS that this
bottleneck causes to go AT-RISK. The state names must appear in the SLA ANALYSIS section below.
The Evidence: field is required -- see the format contract embedded in each B-NN block below.
A blank SLA Nodes Affected: or Evidence: field is a visible incomplete answer.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific operational reason -- not "slow approvals" but the precise bottleneck mechanism]
  Downstream impact: [Concrete effect on states or process timeline downstream]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS whose AT-RISK entry cites this B-ID]
  Evidence: [List each AT-RISK row in SLA ANALYSIS that cites B-01.
    Required format per entry: "[State name -- S-ID]: AT-RISK, causal source: B-01"
    A field containing only "see SLA ANALYSIS" or state names without AT-RISK row-level S-ID
    specificity fails -- every entry must use the format above.]

B-02 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific cause]
  Downstream impact: [Effect]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS affected]
  Evidence: [List each AT-RISK row in SLA ANALYSIS that cites B-02.
    Required format per entry: "[State name -- S-ID]: AT-RISK, causal source: B-02"
    A field containing only "see SLA ANALYSIS" or state names without AT-RISK row-level S-ID
    specificity fails -- every entry must use the format above.]

[Add B-03 onward as needed. All six fields required per block.]

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What it does] | [Why standard practice] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any exception trace (E-ID) from any phase above.
Write each as a per-item answer block. A blank sub-field is a visible incomplete answer.]

EC-01 -- [Edge Case Name]:
  Phase: [Phase where this case surfaces]
  Trigger: [Condition -- must be distinct from every E-ID trigger in all phase sections]
  Why problematic: [Why the current model cannot handle this correctly -- specific to this process]
  Correct response: [What correct handling looks like in practice]

EC-02 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation -- specific to this process]
  Correct response: [Handling]

EC-03 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation]
  Correct response: [Handling]

[Add EC-04 onward as needed. All four sub-fields required per block.]

## CROSS-PROCESS INTERACTIONS
[At least one inter-process handoff with full contract.
If none: "No cross-process interactions. Lifecycle is self-contained. Rationale: [explain]"]

| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process name] | [Data fields] | [Acknowledgment] | R-[N] |

## SLA ANALYSIS
[3+ nodes annotated. Every AT-RISK row must cite a B-ID from BOTTLENECKS.
Chain verification is declared in the CHAIN STATUS section below -- do not write a
chain status line or bidirectional check block inside this section.]

| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row: "AT-RISK NOTE: [specific reason typical exceeds SLA] -- causal source: B-[ID]"]

## CHAIN STATUS
[This section is the single declared gate for bidirectional chain verification.
Declare CLOSED or OPEN as the first output element of this section.
CLOSED: both forward (SLA->B) and backward (B->SLA) directions are complete; no orphan entries.
  -- Enumerate every AT-RISK row and confirm the B-ID it cites (forward direction).
  -- Enumerate every B-ID and confirm the AT-RISK rows that cite it (backward direction).
  -- CLOSED is valid only if all enumerations are complete with no gaps or uncited entries.
OPEN: one or both directions are incomplete.
  -- Name the specific direction(s) and the unresolved entries by ID.
  -- An accurate OPEN declaration passes. An incorrect CLOSED declaration fails.
Do not summarize in prose. Declare status first, then enumerate both directions.]

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA -> B):
  [State name -- S-ID]: cites B-[ID] -- [confirmed / ORPHAN: no matching B-ID]
  [Repeat one line per AT-RISK row]
  All AT-RISK rows accounted for: [YES / NO -- if NO: list uncited rows]

Backward (B -> SLA):
  B-[ID] ([Bottleneck Name]): SLA Nodes Affected -- [state name(s)] -- AT-RISK rows confirmed: [YES / NO]
  [Repeat one line per B-ID]
  All B-IDs have AT-RISK citations: [YES / NO -- if NO: list B-IDs with no matching AT-RISK rows]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-02: C-22 Isolation -- Preamble-Only Concrete Named Example

**Axis:** Output format -- Evidence format contract with concrete named example lives in global
preamble only; per-block Evidence hints are minimal references pointing back to preamble.
**Hypothesis:** A global preamble rule that provides (a) a concrete named example
(`"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`) and (b) an explicit fail condition
for general references satisfies C-22 even when per-block Evidence hints say only
`[Per format contract in preamble above]`. Tests whether preamble-only format contract propagates
reliably to block completion, or whether proximity in the per-block hint is load-bearing.
C-23 preserved (global preamble anti-embedding + dedicated CHAIN STATUS section from V-05 R4).

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: SECTION A -- EXCEPTIONS is always written before SECTION B -- STATES.
  SECTION A is the single structural mechanism for phase-scoped exception generation (C-13),
  exception-first position (C-15), and constructed-answer completeness (C-17).
  Do not introduce any separate mechanism for any of these three requirements outside SECTION A.
Exception flows and edge cases are written as per-item answer blocks, not table rows.
Bottleneck entries are written as per-item answer blocks with mandatory SLA Nodes Affected: and Evidence: fields.
Evidence format contract: each Evidence: field must list AT-RISK rows from SLA ANALYSIS that cite
  this B-ID. Required format per entry: "[State name -- S-ID]: AT-RISK, causal source: B-[ID]".
  Concrete example: "S-05: Credit Hold Review -- AT-RISK, causal source: B-01".
  A field containing only "see SLA ANALYSIS" or state names without AT-RISK row-level S-ID
  specificity fails. Every Evidence: entry must use the format contract above.
Every blank sub-field in any answer block is a visible incomplete answer -- do not leave any empty.
Every AT-RISK SLA row must cite a B-ID; every B-ID must name its SLA Nodes Affected (bidirectional).
The CHAIN STATUS section is a required top-level section after SLA ANALYSIS.
  It declares CLOSED or OPEN as its first element, then enumerates all verified B-IDs and AT-RISK rows.
  Do not embed chain status as a line or annotation inside the SLA ANALYSIS section.
Do not reorder, rename, or remove any section header, sub-section label, column header, or field label.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before writing any PHASE section. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O        -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P        -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE       -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate:
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- add if the process type supports cancellation]

## PHASE MAP
| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Last phase Downstream Handoff must reference a TERMINAL state.]

---

[Write one PHASE block for every phase in the PHASE MAP.
Within each PHASE block: SECTION A is always first, SECTION B is always second.
SECTION A is the single unified mechanism for phase-scoped exception generation, exception-first
position, and constructed-answer completeness. Do not add exception content outside SECTION A.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### SECTION A -- EXCEPTIONS IN THIS PHASE
[This section is always the first declared output element in every phase block.
Write failure modes specific to this phase before any state detail is available.
Phase context is the scope: only generate exceptions whose trigger condition is plausible in this phase.
Generic exceptions (system error, network timeout) that apply to any phase are not acceptable.
Write each exception as a per-item answer block. A blank sub-field is a visible incomplete answer.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.]

E-[N] -- [Exception Name]:
  Trigger state: S-[ID]: [state name -- must be a state in SECTION B of this phase]
  Trigger: [Phase-specific condition -- must be specific to work done in this phase]
  Trace: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

[Add one block per exception specific to this phase. All five sub-fields required per block.]

### SECTION B -- STATES IN THIS PHASE
[Written after SECTION A. Entry Condition and Exits columns required for every row.
Owner column must be an R-ID. Exit format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]".]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks for This Phase
[One block per DECISION-type state in SECTION B.
Write "No DECISION-type states in this phase." if none.
Fallback: (required) is a required field -- do not write "n/a".]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule or data threshold -- process and phase specific, not "if approved"]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch condition is met] -> S-[ID]: [destination]
            [If exhaustive: "Exhaustive -- reason: [explain why no unhandled input is possible]"]

### Parallel Work Streams in This Phase
Fork: S-[ID] -> Branch A (R-[N]): [state list] | Branch B (R-[N]): [state list] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver before join fires]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase or TERMINAL:name]

---

[Repeat the PHASE block for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS

[Bottleneck entries are per-item answer blocks.
The SLA Nodes Affected: field is required -- it names the state(s) in SLA ANALYSIS that this
bottleneck causes to go AT-RISK.
The Evidence: field is required -- populate using the Evidence format contract in the global
preamble above. Do not use general references; the format contract specifies exactly what is required.
A blank SLA Nodes Affected: or Evidence: field is a visible incomplete answer.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific operational reason -- not "slow approvals" but the precise bottleneck mechanism]
  Downstream impact: [Concrete effect on states or process timeline downstream]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS whose AT-RISK entry cites this B-ID]
  Evidence: [Per format contract in preamble: list AT-RISK rows citing B-01 by state name and S-ID]

B-02 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific cause]
  Downstream impact: [Effect]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS affected]
  Evidence: [Per format contract in preamble: list AT-RISK rows citing B-02 by state name and S-ID]

[Add B-03 onward as needed. All six fields required per block.]

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What it does] | [Why standard practice] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any exception trace (E-ID) from any phase above.
Write each as a per-item answer block. A blank sub-field is a visible incomplete answer.]

EC-01 -- [Edge Case Name]:
  Phase: [Phase where this case surfaces]
  Trigger: [Condition -- must be distinct from every E-ID trigger in all phase sections]
  Why problematic: [Why the current model cannot handle this correctly -- specific to this process]
  Correct response: [What correct handling looks like in practice]

EC-02 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation -- specific to this process]
  Correct response: [Handling]

EC-03 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation]
  Correct response: [Handling]

[Add EC-04 onward as needed. All four sub-fields required per block.]

## CROSS-PROCESS INTERACTIONS
[At least one inter-process handoff with full contract.
If none: "No cross-process interactions. Lifecycle is self-contained. Rationale: [explain]"]

| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process name] | [Data fields] | [Acknowledgment] | R-[N] |

## SLA ANALYSIS
[3+ nodes annotated. Every AT-RISK row must cite a B-ID from BOTTLENECKS.
Chain verification is declared in the CHAIN STATUS section below -- do not write a
chain status line or bidirectional check block inside this section.]

| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row: "AT-RISK NOTE: [specific reason typical exceeds SLA] -- causal source: B-[ID]"]

## CHAIN STATUS
[This section is the single declared gate for bidirectional chain verification.
Declare CLOSED or OPEN as the first output element of this section.
CLOSED: both forward (SLA->B) and backward (B->SLA) directions are complete; no orphan entries.
  -- Enumerate every AT-RISK row and confirm the B-ID it cites (forward direction).
  -- Enumerate every B-ID and confirm the AT-RISK rows that cite it (backward direction).
  -- CLOSED is valid only if all enumerations are complete with no gaps or uncited entries.
OPEN: one or both directions are incomplete.
  -- Name the specific direction(s) and the unresolved entries by ID.
  -- An accurate OPEN declaration passes. An incorrect CLOSED declaration fails.
Do not summarize in prose. Declare status first, then enumerate both directions.]

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA -> B):
  [State name -- S-ID]: cites B-[ID] -- [confirmed / ORPHAN: no matching B-ID]
  [Repeat one line per AT-RISK row]
  All AT-RISK rows accounted for: [YES / NO -- if NO: list uncited rows]

Backward (B -> SLA):
  B-[ID] ([Bottleneck Name]): SLA Nodes Affected -- [state name(s)] -- AT-RISK rows confirmed: [YES / NO]
  [Repeat one line per B-ID]
  All B-IDs have AT-RISK citations: [YES / NO -- if NO: list B-IDs with no matching AT-RISK rows]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-03: C-23 Isolation -- Section-Level Anti-Embedding Only

**Axis:** Lifecycle emphasis -- the anti-embedding prohibition for CHAIN STATUS lives inside the
CHAIN STATUS section instruction (proximate, immediate), not in the global preamble (distal).
**Hypothesis:** An anti-embedding prohibition placed as the FIRST instruction line of the CHAIN
STATUS section -- "Do not embed chain status inside the SLA ANALYSIS section. This section is a
dedicated top-level artifact." -- satisfies C-23 without a global preamble prohibition. The
constraint is proximate to the structural element it governs: violating it leaves a visible
missing section instruction. C-22 is preserved at full V-05 R4 strength (preamble format contract
+ per-block concrete examples intact).

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: SECTION A -- EXCEPTIONS is always written before SECTION B -- STATES.
  SECTION A is the single structural mechanism for phase-scoped exception generation (C-13),
  exception-first position (C-15), and constructed-answer completeness (C-17).
  Do not introduce any separate mechanism for any of these three requirements outside SECTION A.
Exception flows and edge cases are written as per-item answer blocks, not table rows.
Bottleneck entries are written as per-item answer blocks with mandatory SLA Nodes Affected: and Evidence: fields.
The Evidence: field must list specific AT-RISK row identifiers and state names from SLA ANALYSIS
  that cite this B-ID -- not a general reference to the SLA table.
  Required format: "[State name -- S-ID]: AT-RISK, causal source: B-[ID]"
  A field that says only "see SLA ANALYSIS" or names states without row-level specificity fails.
Every blank sub-field in any answer block is a visible incomplete answer -- do not leave any empty.
Every AT-RISK SLA row must cite a B-ID; every B-ID must name its SLA Nodes Affected (bidirectional).
Do not reorder, rename, or remove any section header, sub-section label, column header, or field label.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before writing any PHASE section. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O        -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P        -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE       -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate:
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- add if the process type supports cancellation]

## PHASE MAP
| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Last phase Downstream Handoff must reference a TERMINAL state.]

---

[Write one PHASE block for every phase in the PHASE MAP.
Within each PHASE block: SECTION A is always first, SECTION B is always second.
SECTION A is the single unified mechanism for phase-scoped exception generation, exception-first
position, and constructed-answer completeness. Do not add exception content outside SECTION A.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### SECTION A -- EXCEPTIONS IN THIS PHASE
[This section is always the first declared output element in every phase block.
Write failure modes specific to this phase before any state detail is available.
Phase context is the scope: only generate exceptions whose trigger condition is plausible in this phase.
Generic exceptions (system error, network timeout) that apply to any phase are not acceptable.
Write each exception as a per-item answer block. A blank sub-field is a visible incomplete answer.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.]

E-[N] -- [Exception Name]:
  Trigger state: S-[ID]: [state name -- must be a state in SECTION B of this phase]
  Trigger: [Phase-specific condition -- must be specific to work done in this phase]
  Trace: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

[Add one block per exception specific to this phase. All five sub-fields required per block.]

### SECTION B -- STATES IN THIS PHASE
[Written after SECTION A. Entry Condition and Exits columns required for every row.
Owner column must be an R-ID. Exit format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]".]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks for This Phase
[One block per DECISION-type state in SECTION B.
Write "No DECISION-type states in this phase." if none.
Fallback: (required) is a required field -- do not write "n/a".]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule or data threshold -- process and phase specific, not "if approved"]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch condition is met] -> S-[ID]: [destination]
            [If exhaustive: "Exhaustive -- reason: [explain why no unhandled input is possible]"]

### Parallel Work Streams in This Phase
Fork: S-[ID] -> Branch A (R-[N]): [state list] | Branch B (R-[N]): [state list] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver before join fires]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase or TERMINAL:name]

---

[Repeat the PHASE block for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS

[Bottleneck entries are per-item answer blocks.
The SLA Nodes Affected: field is required -- it names the state(s) in SLA ANALYSIS that this
bottleneck causes to go AT-RISK. The state names must appear in the SLA ANALYSIS section below.
The Evidence: field is required -- list each AT-RISK row in SLA ANALYSIS that cites this B-ID,
  identified by state name and S-ID. Required format per entry:
  "[State name -- S-ID]: AT-RISK, causal source: B-[ID]"
  A general reference ("see SLA ANALYSIS") or state name without AT-RISK row-level specificity fails.
A blank SLA Nodes Affected: or Evidence: field is a visible incomplete answer.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific operational reason -- not "slow approvals" but the precise bottleneck mechanism]
  Downstream impact: [Concrete effect on states or process timeline downstream]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS whose AT-RISK entry cites this B-ID]
  Evidence: [e.g., "S-05: Credit Hold Review -- AT-RISK, causal source: B-01"; list all rows]

B-02 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific cause]
  Downstream impact: [Effect]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS affected]
  Evidence: [List each AT-RISK row citing B-02 -- format: "[State name -- S-ID]: AT-RISK, causal source: B-02"]

[Add B-03 onward as needed. All six fields required per block.]

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What it does] | [Why standard practice] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any exception trace (E-ID) from any phase above.
Write each as a per-item answer block. A blank sub-field is a visible incomplete answer.]

EC-01 -- [Edge Case Name]:
  Phase: [Phase where this case surfaces]
  Trigger: [Condition -- must be distinct from every E-ID trigger in all phase sections]
  Why problematic: [Why the current model cannot handle this correctly -- specific to this process]
  Correct response: [What correct handling looks like in practice]

EC-02 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation -- specific to this process]
  Correct response: [Handling]

EC-03 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation]
  Correct response: [Handling]

[Add EC-04 onward as needed. All four sub-fields required per block.]

## CROSS-PROCESS INTERACTIONS
[At least one inter-process handoff with full contract.
If none: "No cross-process interactions. Lifecycle is self-contained. Rationale: [explain]"]

| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process name] | [Data fields] | [Acknowledgment] | R-[N] |

## SLA ANALYSIS
[3+ nodes annotated. Every AT-RISK row must cite a B-ID from BOTTLENECKS.
Bidirectional chain rules:
  Forward (SLA -> B): every AT-RISK row must cite a B-ID from BOTTLENECKS.
  Backward (B -> SLA): every B-ID's SLA Nodes Affected field must name a state appearing here as AT-RISK.
  No orphan at-risk entries (AT-RISK without a B-ID).
  No orphan bottleneck IDs (B-ID without an AT-RISK SLA row citing it).]

| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row: "AT-RISK NOTE: [specific reason typical exceeds SLA] -- causal source: B-[ID]"]

## CHAIN STATUS
[STRUCTURAL CONSTRAINT: Do not embed chain status inside the SLA ANALYSIS section. Do not add a
"Chain status:" line or "Bidirectional evidence check:" block inside SLA ANALYSIS. Chain status
is declared exclusively in this dedicated top-level section. Writing chain status inside SLA
ANALYSIS instead of here is a structural violation of this template.
Declare CLOSED or OPEN as the first output element of this section.
CLOSED: both forward (SLA->B) and backward (B->SLA) directions are complete; no orphan entries.
  -- Enumerate every AT-RISK row and confirm the B-ID it cites (forward direction).
  -- Enumerate every B-ID and confirm the AT-RISK rows that cite it (backward direction).
  -- CLOSED is valid only if all enumerations are complete with no gaps or uncited entries.
OPEN: one or both directions are incomplete.
  -- Name the specific direction(s) and the unresolved entries by ID.
  -- An accurate OPEN declaration passes. An incorrect CLOSED declaration fails.
Do not summarize in prose. Declare status first, then enumerate both directions.]

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA -> B):
  [State name -- S-ID]: cites B-[ID] -- [confirmed / ORPHAN: no matching B-ID]
  [Repeat one line per AT-RISK row]
  All AT-RISK rows accounted for: [YES / NO -- if NO: list uncited rows]

Backward (B -> SLA):
  B-[ID] ([Bottleneck Name]): SLA Nodes Affected -- [state name(s)] -- AT-RISK rows confirmed: [YES / NO]
  [Repeat one line per B-ID]
  All B-IDs have AT-RISK citations: [YES / NO -- if NO: list B-IDs with no matching AT-RISK rows]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-04: Combined Minimum Form -- Block-Hint Format Contract + Section-Level Anti-Embedding

**Axes:** C-22 (block-hint-only format contract, no preamble format rule) + C-23 (CHAIN STATUS
section-level anti-embedding only, no global preamble prohibition)
**Hypothesis:** The minimum viable form for both C-22 and C-23 satisfies both criteria without
any preamble-level enforcement for either. The format contract appears only in per-block
Evidence hints; the anti-embedding prohibition appears only in the CHAIN STATUS section
instruction. This is the minimum-instruction design: no global preamble overhead for C-22 or
C-23, but each criterion has its constraint at the most proximate structural location.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: SECTION A -- EXCEPTIONS is always written before SECTION B -- STATES.
  SECTION A is the single structural mechanism for phase-scoped exception generation (C-13),
  exception-first position (C-15), and constructed-answer completeness (C-17).
  Do not introduce any separate mechanism for any of these three requirements outside SECTION A.
Exception flows and edge cases are written as per-item answer blocks, not table rows.
Bottleneck entries are written as per-item answer blocks with mandatory SLA Nodes Affected: and Evidence: fields.
Every blank sub-field in any answer block is a visible incomplete answer -- do not leave any empty.
Every AT-RISK SLA row must cite a B-ID; every B-ID must name its SLA Nodes Affected (bidirectional).
Do not reorder, rename, or remove any section header, sub-section label, column header, or field label.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before writing any PHASE section. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O        -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P        -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE       -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate:
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- add if the process type supports cancellation]

## PHASE MAP
| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Last phase Downstream Handoff must reference a TERMINAL state.]

---

[Write one PHASE block for every phase in the PHASE MAP.
Within each PHASE block: SECTION A is always first, SECTION B is always second.
SECTION A is the single unified mechanism for phase-scoped exception generation, exception-first
position, and constructed-answer completeness. Do not add exception content outside SECTION A.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### SECTION A -- EXCEPTIONS IN THIS PHASE
[This section is always the first declared output element in every phase block.
Write failure modes specific to this phase before any state detail is available.
Phase context is the scope: only generate exceptions whose trigger condition is plausible in this phase.
Generic exceptions (system error, network timeout) that apply to any phase are not acceptable.
Write each exception as a per-item answer block. A blank sub-field is a visible incomplete answer.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.]

E-[N] -- [Exception Name]:
  Trigger state: S-[ID]: [state name -- must be a state in SECTION B of this phase]
  Trigger: [Phase-specific condition -- must be specific to work done in this phase]
  Trace: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

[Add one block per exception specific to this phase. All five sub-fields required per block.]

### SECTION B -- STATES IN THIS PHASE
[Written after SECTION A. Entry Condition and Exits columns required for every row.
Owner column must be an R-ID. Exit format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]".]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks for This Phase
[One block per DECISION-type state in SECTION B.
Write "No DECISION-type states in this phase." if none.
Fallback: (required) is a required field -- do not write "n/a".]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule or data threshold -- process and phase specific, not "if approved"]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch condition is met] -> S-[ID]: [destination]
            [If exhaustive: "Exhaustive -- reason: [explain why no unhandled input is possible]"]

### Parallel Work Streams in This Phase
Fork: S-[ID] -> Branch A (R-[N]): [state list] | Branch B (R-[N]): [state list] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver before join fires]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase or TERMINAL:name]

---

[Repeat the PHASE block for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS

[Bottleneck entries are per-item answer blocks.
The SLA Nodes Affected: field is required -- it names the state(s) in SLA ANALYSIS that this
bottleneck causes to go AT-RISK.
The Evidence: field is required -- see the format contract embedded in each B-NN block below.
A blank SLA Nodes Affected: or Evidence: field is a visible incomplete answer.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific operational reason -- not "slow approvals" but the precise bottleneck mechanism]
  Downstream impact: [Concrete effect on states or process timeline downstream]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS whose AT-RISK entry cites this B-ID]
  Evidence: [List each AT-RISK row in SLA ANALYSIS that cites B-01.
    Required format per entry: "[State name -- S-ID]: AT-RISK, causal source: B-01"
    A field containing only "see SLA ANALYSIS" or state names without AT-RISK row-level S-ID
    specificity fails -- every entry must use the bracketed format above.]

B-02 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific cause]
  Downstream impact: [Effect]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS affected]
  Evidence: [List each AT-RISK row in SLA ANALYSIS that cites B-02.
    Required format per entry: "[State name -- S-ID]: AT-RISK, causal source: B-02"
    A field containing only "see SLA ANALYSIS" or state names without AT-RISK row-level S-ID
    specificity fails -- every entry must use the bracketed format above.]

[Add B-03 onward as needed. All six fields required per block.]

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What it does] | [Why standard practice] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any exception trace (E-ID) from any phase above.
Write each as a per-item answer block. A blank sub-field is a visible incomplete answer.]

EC-01 -- [Edge Case Name]:
  Phase: [Phase where this case surfaces]
  Trigger: [Condition -- must be distinct from every E-ID trigger in all phase sections]
  Why problematic: [Why the current model cannot handle this correctly -- specific to this process]
  Correct response: [What correct handling looks like in practice]

EC-02 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation -- specific to this process]
  Correct response: [Handling]

EC-03 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation]
  Correct response: [Handling]

[Add EC-04 onward as needed. All four sub-fields required per block.]

## CROSS-PROCESS INTERACTIONS
[At least one inter-process handoff with full contract.
If none: "No cross-process interactions. Lifecycle is self-contained. Rationale: [explain]"]

| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process name] | [Data fields] | [Acknowledgment] | R-[N] |

## SLA ANALYSIS
[3+ nodes annotated. Every AT-RISK row must cite a B-ID from BOTTLENECKS.
Bidirectional chain rules:
  Forward (SLA -> B): every AT-RISK row must cite a B-ID from BOTTLENECKS.
  Backward (B -> SLA): every B-ID's SLA Nodes Affected field must name a state appearing here as AT-RISK.
  No orphan at-risk entries (AT-RISK without a B-ID).
  No orphan bottleneck IDs (B-ID without an AT-RISK SLA row citing it).]

| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row: "AT-RISK NOTE: [specific reason typical exceeds SLA] -- causal source: B-[ID]"]

## CHAIN STATUS
[STRUCTURAL CONSTRAINT: Do not embed chain status inside the SLA ANALYSIS section. Do not add a
"Chain status:" line or "Bidirectional evidence check:" block inside SLA ANALYSIS. This section
is a dedicated top-level section independent of SLA ANALYSIS. Placing CHAIN STATUS as an embedded
annotation inside SLA ANALYSIS instead of here is a structural violation of this template.
Declare CLOSED or OPEN as the first output element of this section.
CLOSED: both forward (SLA->B) and backward (B->SLA) directions are complete; no orphan entries.
  -- Enumerate every AT-RISK row and confirm the B-ID it cites (forward direction).
  -- Enumerate every B-ID and confirm the AT-RISK rows that cite it (backward direction).
  -- CLOSED is valid only if all enumerations are complete with no gaps or uncited entries.
OPEN: one or both directions are incomplete.
  -- Name the specific direction(s) and the unresolved entries by ID.
  -- An accurate OPEN declaration passes. An incorrect CLOSED declaration fails.
Do not summarize in prose. Declare status first, then enumerate both directions.]

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA -> B):
  [State name -- S-ID]: cites B-[ID] -- [confirmed / ORPHAN: no matching B-ID]
  [Repeat one line per AT-RISK row]
  All AT-RISK rows accounted for: [YES / NO -- if NO: list uncited rows]

Backward (B -> SLA):
  B-[ID] ([Bottleneck Name]): SLA Nodes Affected -- [state name(s)] -- AT-RISK rows confirmed: [YES / NO]
  [Repeat one line per B-ID]
  All B-IDs have AT-RISK citations: [YES / NO -- if NO: list B-IDs with no matching AT-RISK rows]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-05: Full R5 Synthesis -- Dual-Location Format Contract + Dual Anti-Embedding

**Axes:** Full synthesis -- maximum structural redundancy for both C-22 and C-23.
C-22: concrete named example in preamble AND concrete named example in per-block hints (both
locations carry the full contract; inconsistency between B-01 and B-02 from V-05 R4 corrected
-- all B-NN blocks now use the same concrete-example hint form).
C-23: anti-embedding prohibition in global preamble AND inside the CHAIN STATUS section
instruction (both locations independently enforce the structural constraint).
Also carries the explicit C-21 convergence rule from V-05 R4.
**Hypothesis:** Dual-location enforcement for both criteria makes non-compliance visible at two
independent structural points. A model that misses the preamble rule will encounter the
proximate section-level constraint; a model that ignores the section-level constraint will have
been warned by the preamble. Golden candidate for Round 5.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: SECTION A -- EXCEPTIONS is always written before SECTION B -- STATES.
  SECTION A is the single structural mechanism for phase-scoped exception generation (C-13),
  exception-first position (C-15), and constructed-answer completeness (C-17).
  Do not introduce any separate mechanism for any of these three requirements outside SECTION A.
Exception flows and edge cases are written as per-item answer blocks, not table rows.
Bottleneck entries are written as per-item answer blocks with mandatory SLA Nodes Affected: and Evidence: fields.
Evidence format contract: each Evidence: field must list AT-RISK rows from SLA ANALYSIS that cite
  this B-ID using the following format: "[State name -- S-ID]: AT-RISK, causal source: B-[ID]".
  Concrete example: "S-05: Credit Hold Review -- AT-RISK, causal source: B-01".
  A field containing only "see SLA ANALYSIS" or state names without AT-RISK row-level S-ID
  specificity fails. Every Evidence: entry must conform to the format contract above.
Every blank sub-field in any answer block is a visible incomplete answer -- do not leave any empty.
Every AT-RISK SLA row must cite a B-ID; every B-ID must name its SLA Nodes Affected (bidirectional).
The CHAIN STATUS section is a required top-level section after SLA ANALYSIS.
  It declares CLOSED or OPEN as its first element, then enumerates all verified B-IDs and AT-RISK rows.
  Do not embed chain status as a line or annotation inside the SLA ANALYSIS section.
Do not reorder, rename, or remove any section header, sub-section label, column header, or field label.

---

## PROCESS DETECTION
Process type: [L2O / P2P / PERIOD-CLOSE / CASE]
Trigger event: [Single sentence: what initiates this lifecycle?]
Domain: [Sales / Procurement / Finance / Support]

## ROLE REGISTRY
[Complete fully before writing any PHASE section. Minimum 3 roles. All domain-specific.
Auto-select matching process type:
  L2O        -> Sales Rep, Sales Manager, Credit Analyst, Inventory Controller, AR Specialist
  P2P        -> Purchase Requestor, Procurement Officer, AP Specialist, Receiving Clerk, Controller
  PERIOD-CLOSE -> Staff Accountant, Controller, CFO, External Auditor, Tax Analyst
  CASE       -> Support Agent, Case Manager, Ops Lead, Escalation Specialist, Legal Counsel]

| R-ID | Role Name | Domain | Decision Authority | Active Phases | Anti-Generic Check |
|------|-----------|--------|--------------------|---------------|--------------------|
| R-01 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-02 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
| R-03 | [Name] | [Domain] | [Decisions] | [Phases] | Not "Approver"/"Manager"/"Owner" |
[Add R-04, R-05 as needed.]

Registry gate:
  [ ] All R-IDs have domain-specific names (Anti-Generic Check column shows no violations)
  [ ] All approval gates and decision points in this process are covered by a named R-ID
  [ ] Minimum 3 roles registered
  [If any item is unchecked: fix before writing phase sections.]

## TERMINAL STATES
SUCCESS: [Name] -- [Condition that ends the lifecycle successfully]
FAILURE: [Name] -- [Condition that ends the lifecycle in a failure state]
[CANCEL: [Name] -- add if the process type supports cancellation]

## PHASE MAP
| Phase | Entry Trigger | Owner (R-ID) | Exit Condition | Downstream Handoff |
|-------|--------------|--------------|----------------|--------------------|
| [Name] | [Trigger] | R-[N] | [Exit condition] | [Artifact or TERMINAL:name] |
[Minimum 3 phases. Last phase Downstream Handoff must reference a TERMINAL state.]

---

[Write one PHASE block for every phase in the PHASE MAP.
Within each PHASE block: SECTION A is always first, SECTION B is always second.
SECTION A is the single unified mechanism for phase-scoped exception generation, exception-first
position, and constructed-answer completeness. Do not add exception content outside SECTION A.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### SECTION A -- EXCEPTIONS IN THIS PHASE
[This section is always the first declared output element in every phase block.
Write failure modes specific to this phase before any state detail is available.
Phase context is the scope: only generate exceptions whose trigger condition is plausible in this phase.
Generic exceptions (system error, network timeout) that apply to any phase are not acceptable.
Write each exception as a per-item answer block. A blank sub-field is a visible incomplete answer.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.]

E-[N] -- [Exception Name]:
  Trigger state: S-[ID]: [state name -- must be a state in SECTION B of this phase]
  Trigger: [Phase-specific condition -- must be specific to work done in this phase]
  Trace: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

[Add one block per exception specific to this phase. All five sub-fields required per block.]

### SECTION B -- STATES IN THIS PHASE
[Written after SECTION A. Entry Condition and Exits columns required for every row.
Owner column must be an R-ID. Exit format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]".]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks for This Phase
[One block per DECISION-type state in SECTION B.
Write "No DECISION-type states in this phase." if none.
Fallback: (required) is a required field -- do not write "n/a".]

D-[S-ID] ([State Name]):
  Condition evaluated: [Exact rule or data threshold -- process and phase specific, not "if approved"]
  Owner: R-[N] -- [Role Name]
  Branch YES: [condition] -> S-[ID]: [state name]
  Branch NO:  [condition] -> S-[ID]: [state name or TERMINAL:name]
  Fallback: (required) [what happens when no branch condition is met] -> S-[ID]: [destination]
            [If exhaustive: "Exhaustive -- reason: [explain why no unhandled input is possible]"]

### Parallel Work Streams in This Phase
Fork: S-[ID] -> Branch A (R-[N]): [state list] | Branch B (R-[N]): [state list] -> Join: S-[ID]
Join type: AND-join / OR-join
Join condition: [What all branches must deliver before join fires]
[If sequential: "Sequential -- no concurrent branches in this phase."]

Phase end: [Exit condition] -> [Next phase or TERMINAL:name]

---

[Repeat the PHASE block for every phase in the PHASE MAP]

---

## BOTTLENECKS AND GAPS

[Bottleneck entries are per-item answer blocks.
The SLA Nodes Affected: field is required -- it names the state(s) in SLA ANALYSIS that this
bottleneck causes to go AT-RISK. The state names must appear in the SLA ANALYSIS section below.
The Evidence: field is required -- list each AT-RISK row in SLA ANALYSIS that cites this B-ID,
  identified by state name and S-ID. Required format per entry:
  "[State name -- S-ID]: AT-RISK, causal source: B-[ID]"
  Concrete example: "S-05: Credit Hold Review -- AT-RISK, causal source: B-01"
  A general reference ("see SLA ANALYSIS") or state name without AT-RISK row-level S-ID
  specificity fails -- every entry must use the format contract above.
A blank SLA Nodes Affected: or Evidence: field is a visible incomplete answer.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific operational reason -- not "slow approvals" but the precise bottleneck mechanism]
  Downstream impact: [Concrete effect on states or process timeline downstream]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS whose AT-RISK entry cites this B-ID]
  Evidence: [e.g., "S-05: Credit Hold Review -- AT-RISK, causal source: B-01"
    Format: "[State name -- S-ID]: AT-RISK, causal source: B-01" -- list all rows, no general references]

B-02 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific cause]
  Downstream impact: [Effect]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS affected]
  Evidence: [e.g., "S-08: Invoice Approval -- AT-RISK, causal source: B-02"
    Format: "[State name -- S-ID]: AT-RISK, causal source: B-02" -- list all rows, no general references]

[Add B-03 onward as needed. All six fields required per block.]

Missing steps (minimum 1):
| G-ID | Label | Phase | Placement | Description | Rationale | Would-Own (R-ID) |
|------|-------|-------|-----------|-------------|-----------|-----------------|
| G-01 | MISSING: [Name] | [Phase] | S-[ID] -> here -> S-[ID] | [What it does] | [Why standard practice] | R-[N] |

## EDGE CASES
[3+ cases. Must not overlap with any exception trace (E-ID) from any phase above.
Write each as a per-item answer block. A blank sub-field is a visible incomplete answer.]

EC-01 -- [Edge Case Name]:
  Phase: [Phase where this case surfaces]
  Trigger: [Condition -- must be distinct from every E-ID trigger in all phase sections]
  Why problematic: [Why the current model cannot handle this correctly -- specific to this process]
  Correct response: [What correct handling looks like in practice]

EC-02 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation -- specific to this process]
  Correct response: [Handling]

EC-03 -- [Edge Case Name]:
  Phase: [Phase]
  Trigger: [Condition -- distinct from all E-IDs]
  Why problematic: [Explanation]
  Correct response: [Handling]

[Add EC-04 onward as needed. All four sub-fields required per block.]

## CROSS-PROCESS INTERACTIONS
[At least one inter-process handoff with full contract.
If none: "No cross-process interactions. Lifecycle is self-contained. Rationale: [explain]"]

| Sending Phase: S-ID | Receiving Process | Data Payload | Expected Acknowledgment | Owner (R-ID) |
|--------------------|-------------------|--------------|------------------------|--------------|
| [Phase]: S-[ID] | [Process name] | [Data fields] | [Acknowledgment] | R-[N] |

## SLA ANALYSIS
[3+ nodes annotated. Every AT-RISK row must cite a B-ID from BOTTLENECKS.
Chain verification is declared in the CHAIN STATUS section below -- do not write a
chain status line or bidirectional check block inside this section.]

| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row: "AT-RISK NOTE: [specific reason typical exceeds SLA] -- causal source: B-[ID]"]

## CHAIN STATUS
[STRUCTURAL CONSTRAINT: Do not embed chain status inside the SLA ANALYSIS section. Do not add a
"Chain status:" line, "Bidirectional evidence check:" block, or any chain verification element
inside SLA ANALYSIS. This section is a dedicated top-level section that is independent of SLA
ANALYSIS. Placing chain status inside SLA ANALYSIS instead of here violates this template.
Declare CLOSED or OPEN as the first output element of this section.
CLOSED: both forward (SLA->B) and backward (B->SLA) directions are complete; no orphan entries.
  -- Enumerate every AT-RISK row and confirm the B-ID it cites (forward direction).
  -- Enumerate every B-ID and confirm the AT-RISK rows that cite it (backward direction).
  -- CLOSED is valid only if all enumerations are complete with no gaps or uncited entries.
OPEN: one or both directions are incomplete.
  -- Name the specific direction(s) and the unresolved entries by ID.
  -- An accurate OPEN declaration passes. An incorrect CLOSED declaration fails.
Do not summarize in prose. Declare status first, then enumerate both directions.]

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA -> B):
  [State name -- S-ID]: cites B-[ID] -- [confirmed / ORPHAN: no matching B-ID]
  [Repeat one line per AT-RISK row]
  All AT-RISK rows accounted for: [YES / NO -- if NO: list uncited rows]

Backward (B -> SLA):
  B-[ID] ([Bottleneck Name]): SLA Nodes Affected -- [state name(s)] -- AT-RISK rows confirmed: [YES / NO]
  [Repeat one line per B-ID]
  All B-IDs have AT-RISK citations: [YES / NO -- if NO: list B-IDs with no matching AT-RISK rows]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## Round 5 Design Notes

### What changed from V-05 R4

| Element | V-05 R4 | V-01 R5 | V-02 R5 | V-03 R5 | V-04 R5 | V-05 R5 |
|---------|---------|---------|---------|---------|---------|---------|
| Preamble Evidence format rule | Bracket template + fail condition | REMOVED | Concrete example + fail condition | Unchanged | REMOVED | Concrete example + fail condition |
| Per-block Evidence hints | B-01: concrete example; B-02: bracket template (inconsistent) | Per-block: bracket template + fail condition | Minimal: "per format contract above" | B-01: concrete; B-02: bracket (unchanged) | Per-block: bracket template + fail condition | Both: concrete example + format pattern (consistent) |
| Global preamble anti-embedding | Present | Present | Present | REMOVED | REMOVED | Present |
| CHAIN STATUS section instruction | No anti-embedding in section | No anti-embedding in section | No anti-embedding in section | Explicit anti-embedding in section | Explicit anti-embedding in section | Explicit anti-embedding in section |
| C-22 target | Passes | Block-hint-only isolation test | Preamble-only isolation test | Unchanged | Block-hint minimum | Dual-location synthesis |
| C-23 target | Passes | Unchanged | Unchanged | Section-only isolation test | Section-only minimum | Dual-location synthesis |

### Diagnostic predictions

- **V-01 vs V-02:** If both pass C-22, either location is independently sufficient. If V-02 fails
  (preamble-only without per-block example), it confirms that per-block proximity is load-bearing
  for format contract enforcement. If V-01 fails (block-hint-only), it confirms that the preamble
  role is critical for priming the Evidence field format before the bottleneck section is reached.

- **V-03:** If it passes C-23, the anti-embedding constraint is enforceable by proximate section
  instruction alone, without global preamble overhead. This matters for prompt minimalism: the
  preamble anti-embedding line in V-05 R4 can be removed without risk.

- **V-04 (minimum form):** If it passes both C-22 and C-23, the minimum viable design for R5 is
  confirmed: no preamble-level rules needed for either criterion. If it fails either, the minimum
  form is insufficient and preamble reinforcement is load-bearing.

- **V-05 (full synthesis):** Expected golden candidate. Both criteria have enforcement at two
  independent structural locations. The per-block Evidence hints are now consistent across all
  B-NN blocks (both use concrete example + format pattern), fixing the B-01/B-02 inconsistency
  from V-05 R4. The CHAIN STATUS section instruction explicitly names the anti-embedding
  constraint in addition to the global preamble.
