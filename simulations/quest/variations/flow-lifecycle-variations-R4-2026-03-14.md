Written to `simulations/quest/variations/flow-lifecycle-variations-R4-2026-03-14.md`.

---

## Round 4 Variations -- flow-lifecycle

### Summary

| V | Axis | Criteria targeted | C-18 | C-19 | C-20 | C-21 |
|---|------|-------------------|------|------|------|------|
| **V-01** | Output format | C-18 alt -- 1./2. numbered labels | PASS | borderline | borderline | PASS |
| **V-02** | Output format | C-19 -- Evidence field row-ID specificity | PASS | PASS | borderline | PASS |
| **V-03** | Lifecycle emphasis | C-20 -- standalone `## CHAIN STATUS` gate | PASS | borderline | PASS | PASS |
| **V-04** | Axes 1+2 | C-18 + C-19 -- numbered labels + Evidence specificity | PASS | PASS | borderline | PASS |
| **V-05** | Full synthesis | C-18 + C-19 + C-20 + C-21 | PASS | PASS | PASS | PASS |

### What V-05 R3 fails under v4 rubric (and how R4 fixes it)

- **C-19 (borderline-fail):** V-05 R3's `Evidence:` hint says "entries that list 'causal source: B-01'" -- too vague to require row-level IDs. V-02/V-04/V-05 add required format `"[State name -- S-ID]: AT-RISK, causal source: B-[ID]"` with an explicit fail condition for general references.

- **C-20 (borderline-fail):** V-05 R3's `Chain status:` line is the last line of a check block embedded inside SLA ANALYSIS -- the rubric fails "present only as an annotation." V-03/V-05 move it to a dedicated `## CHAIN STATUS` top-level section with `CHAIN STATUS: CLOSED / OPEN` as its first element, plus enumeration of both directions.

- **C-18 already passes** from R3 (SECTION A/B labels). V-01 tests whether 1./2. numbering is equally sufficient.

- **C-21 already passes** in V-05 R3 structurally; V-05 R4 makes the convergence rule explicit in the preamble ("SECTION A is the single mechanism for C-13 + C-15 + C-17 -- do not introduce separate mechanisms").
ticism: if it passes C-18, ordinal style is not SECTION A/B-specific. Diagnostic value -- a failed V-01 would mean the label wording matters, not just the ordinal.

**Why V-02 targets Evidence specificity:** C-19 requires "specific AT-RISK row identifiers or state names" in the Evidence field. V-05 R3's hint ("entries that list 'causal source: B-01'") could be satisfied by a general reference. V-02 adds an example format and explicit failure condition for general references.

**Why V-03 tests standalone CHAIN STATUS:** The C-20 fail condition is "present only as a prose instruction, reader checklist, or annotation without a declared status output." V-05 R3's `Chain status:` line is embedded in the Bidirectional evidence check subsection inside SLA ANALYSIS. A standalone `## CHAIN STATUS` section with CLOSED/OPEN as its first element converts verification from an annotation into a first-class output gate.

**C-21 passes in V-01 through V-05:** All variations preserve constructed-answer SECTION A blocks (or 1. EXCEPTIONS blocks in V-01/V-04) that satisfy C-13 + C-15 + C-17 through a single structural unit. C-21 follows as long as these three constituent criteria pass.

### Predicted scores against v4 rubric

| V | C-18 | C-19 | C-20 | C-21 | Aspirational /13 | Predicted composite |
|---|------|------|------|------|-----------------|---------------------|
| V-01 | PASS | borderline | borderline | PASS | ~11 | ~95 |
| V-02 | PASS | PASS | borderline | PASS | ~12 | ~97 |
| V-03 | PASS | borderline | PASS | PASS | ~12 | ~97 |
| V-04 | PASS | PASS | borderline | PASS | ~12 | ~97 |
| V-05 | PASS | PASS | PASS | PASS | 13 | 100 |

---

## V-01: Output Format -- Numbered Phase Section Labels (C-18 Isolation Test)

**Axis:** Output format -- ordinal label style: numbered (1./2.) instead of lettered (SECTION A/B)
**Hypothesis:** `1. EXCEPTIONS IN THIS PHASE` and `2. STATES IN THIS PHASE` satisfy C-18 equally
to SECTION A/B labels. The rubric accepts "equivalent numbered or lettered designations such as
1./2. or A./B." V-01 tests whether the numbered form is equivalently constraining. C-19 is
borderline (Evidence hint unchanged from V-05 R3). C-20 is borderline (Chain status embedded in
SLA ANALYSIS sub-block). C-21 passes because 1. EXCEPTIONS answer blocks are the single unified
mechanism for C-13 + C-15 + C-17.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: section 1. EXCEPTIONS is always written before section 2. STATES.
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
Within each PHASE block: section 1. EXCEPTIONS is always first, section 2. STATES is always second.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### 1. EXCEPTIONS IN THIS PHASE
[This section is always the first declared output element in every phase block.
Write failure modes specific to this phase before any state detail is available.
Phase context is the scope: only generate exceptions whose trigger condition is plausible in this phase.
Generic exceptions (system error, network timeout) that apply to any phase are not acceptable.
Write each exception as a per-item answer block. A blank sub-field is a visible incomplete answer.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.]

E-[N] -- [Exception Name]:
  Trigger state: S-[ID]: [state name -- must be a state in section 2. STATES of this phase]
  Trigger: [Phase-specific condition -- must be specific to work done in this phase]
  Trace: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

[Add one block per exception specific to this phase. All five sub-fields required per block.]

### 2. STATES IN THIS PHASE
[Written after section 1. Entry Condition and Exits columns required for every row.
Owner column must be an R-ID. Exit format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]".]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks for This Phase
[One block per DECISION-type state in section 2. STATES.
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
A blank SLA Nodes Affected: field is a visible incomplete answer -- do not leave it empty.
The Evidence: field names the SLA ANALYSIS AT-RISK rows that cite this B-ID, closing the
reverse direction of the bidirectional chain.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific operational reason -- not "slow approvals" but the precise bottleneck mechanism]
  Downstream impact: [Concrete effect on states or process timeline downstream]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS whose AT-RISK entry cites this B-ID]
  Evidence: [AT-RISK entries that list "causal source: B-01" in SLA ANALYSIS]

B-02 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific cause]
  Downstream impact: [Effect]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS affected]
  Evidence: [AT-RISK entries that cite this B-ID]

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
[3+ nodes annotated. Bidirectional chain rules:
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

Bidirectional evidence check:
  Forward (SLA -> B):  Every AT-RISK row cites a B-ID? [YES: closed | NO: list uncited AT-RISK rows]
  Backward (B -> SLA): Every B-ID's SLA Nodes Affected appears here as AT-RISK?
                        [YES: chain closed | NO: list B-IDs without matching AT-RISK rows]
  Chain status: CLOSED (all forward + backward links verified) / OPEN (list unresolved links)

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-02: Output Format -- Evidence Field Row-ID Specificity (C-19 Isolation Test)

**Axis:** Output format -- Evidence field content requirement: specific AT-RISK row identifiers
**Hypothesis:** Explicitly requiring AT-RISK row identifiers (state name + S-ID) in the Evidence
field, rather than the vague "AT-RISK entries that list 'causal source: B-NN'", reliably produces
the backward lookup result C-19 requires. An example format and explicit failure condition for
general references make incomplete Evidence fields structurally visible. All other structure from
V-05 R3 is preserved: SECTION A/B labels (C-18 pass), Chain status embedded in SLA ANALYSIS
(C-20 borderline).

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: SECTION A -- EXCEPTIONS is always written before SECTION B -- STATES.
Exception flows and edge cases are written as per-item answer blocks, not table rows.
Bottleneck entries are written as per-item answer blocks with mandatory SLA Nodes Affected: and Evidence: fields.
The Evidence: field must list specific AT-RISK row identifiers and state names from SLA ANALYSIS
  that cite this B-ID -- not a general reference to the SLA table.
  A field that says only "see SLA ANALYSIS" or names states without AT-RISK row-level specificity fails.
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
  A field that says only "see SLA ANALYSIS" or lists state names without AT-RISK row-level
  specificity is an incomplete answer -- do not leave it as a general reference.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific operational reason -- not "slow approvals" but the precise bottleneck mechanism]
  Downstream impact: [Concrete effect on states or process timeline downstream]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS whose AT-RISK entry cites this B-ID]
  Evidence: [List each AT-RISK row citing B-01 -- e.g., "S-05: Credit Hold Review -- AT-RISK, causal source: B-01"]

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
[3+ nodes annotated. Bidirectional chain rules:
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

Bidirectional evidence check:
  Forward (SLA -> B):  Every AT-RISK row cites a B-ID? [YES: closed | NO: list uncited AT-RISK rows]
  Backward (B -> SLA): Every B-ID's SLA Nodes Affected appears here as AT-RISK?
                        [YES: chain closed | NO: list B-IDs without matching AT-RISK rows]
  Chain status: CLOSED (all forward + backward links verified) / OPEN (list unresolved links)

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-03: Lifecycle Emphasis -- Standalone CHAIN STATUS Gate Section (C-20 Isolation Test)

**Axis:** Lifecycle emphasis -- CHAIN STATUS as a dedicated top-level section, not an embedded line
**Hypothesis:** A dedicated `## CHAIN STATUS` section after SLA ANALYSIS, with CLOSED/OPEN as its
first element and explicit enumeration of verified B-IDs and AT-RISK rows, satisfies C-20. The
V-05 R3 `Chain status:` line embedded in the Bidirectional evidence check sub-block is borderline
because the rubric fails "present only as an annotation without a declared status output." A
top-level section converts verification into a first-class gate -- omitting it leaves a missing
section, not a missing line. SECTION A/B labels preserved (C-18 pass). Evidence hint unchanged
from V-05 R3 (C-19 borderline).

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: SECTION A -- EXCEPTIONS is always written before SECTION B -- STATES.
Exception flows and edge cases are written as per-item answer blocks, not table rows.
Bottleneck entries are written as per-item answer blocks with mandatory SLA Nodes Affected: and Evidence: fields.
Every blank sub-field in any answer block is a visible incomplete answer -- do not leave any empty.
Every AT-RISK SLA row must cite a B-ID; every B-ID must name its SLA Nodes Affected (bidirectional).
The CHAIN STATUS section is a required top-level section after SLA ANALYSIS.
  It declares CLOSED or OPEN as its first output element, then enumerates all verified links.
  Do not embed chain status as a line inside the SLA ANALYSIS section.
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
A blank SLA Nodes Affected: field is a visible incomplete answer -- do not leave it empty.
The Evidence: field names the SLA ANALYSIS AT-RISK rows that cite this B-ID, closing the
reverse direction of the bidirectional chain.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific operational reason -- not "slow approvals" but the precise bottleneck mechanism]
  Downstream impact: [Concrete effect on states or process timeline downstream]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS whose AT-RISK entry cites this B-ID]
  Evidence: [AT-RISK entries that list "causal source: B-01" in SLA ANALYSIS]

B-02 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific cause]
  Downstream impact: [Effect]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS affected]
  Evidence: [AT-RISK entries that cite this B-ID]

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
Chain status is declared in the CHAIN STATUS section below -- do not write a chain status
line or bidirectional check block here.]

| Phase | State or Transition (S-ID) | SLA Target | Typical Duration | At-Risk? | Bottleneck Cross-Ref |
|-------|---------------------------|------------|------------------|----------|---------------------|
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
| [Phase] | [State -- S-ID] | [N hrs/days] | [N hrs/days] | YES / NO | B-[ID] / -- |
[AT-RISK rows: append below the row: "AT-RISK NOTE: [specific reason typical exceeds SLA] -- causal source: B-[ID]"]

## CHAIN STATUS
[Declare CLOSED or OPEN as the first element of this section.
CLOSED: both forward and backward directions are verified; no orphan entries exist.
  -- Enumerate every AT-RISK row and the B-ID it cites (forward).
  -- Enumerate every B-ID and the AT-RISK rows that name it (backward).
  -- CLOSED is valid only if both enumerations are complete with no gaps.
OPEN: one or both directions are incomplete.
  -- Name the specific direction(s) and the unresolved entries.
  -- An accurate OPEN declaration passes. An incorrect CLOSED declaration fails.
Do not summarize in prose. Declare status first, then enumerate.]

CHAIN STATUS: [CLOSED / OPEN]

Forward (SLA -> B):
  [State name -- S-ID: cites B-[ID] -- confirmed / ORPHAN]
  [Repeat for every AT-RISK row]
  All AT-RISK rows verified: [YES / NO -- if NO: list uncited rows]

Backward (B -> SLA):
  [B-[ID]: SLA Nodes Affected -- [state name(s)] -- AT-RISK rows confirmed: YES / NO]
  [Repeat for every B-ID]
  All B-IDs have AT-RISK citations: [YES / NO -- if NO: list B-IDs with no matching AT-RISK rows]

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-04: Axes 1+2 Combined -- Numbered Labels + Evidence Row-ID Specificity (C-18 + C-19)

**Axes:** Output format (1./2. numbered phase section labels, C-18) + Output format (Evidence field
with specific AT-RISK row identifiers, C-19)
**Hypothesis:** 1./2. numbered labels and row-ID-specific Evidence fields are additive without
structural conflict. C-18 passes via numbered ordinals; C-19 passes via the sharpened Evidence
field requirement. C-20 remains borderline (Chain status embedded in SLA ANALYSIS sub-block).
C-21 passes because 1. EXCEPTIONS answer blocks remain the single unified mechanism for
C-13 + C-15 + C-17.

```
You are running /flow-lifecycle. Fill in this structured template.
All section headers, sub-section labels, table columns, and answer block sub-fields are fixed.
The ROLE REGISTRY must be complete before any PHASE section is written.
Every Owner field must be an R-ID from the ROLE REGISTRY. No generic role names anywhere.
Within each phase: section 1. EXCEPTIONS is always written before section 2. STATES.
Exception flows and edge cases are written as per-item answer blocks, not table rows.
Bottleneck entries are written as per-item answer blocks with mandatory SLA Nodes Affected: and Evidence: fields.
The Evidence: field must list specific AT-RISK row identifiers and state names from SLA ANALYSIS
  that cite this B-ID -- not a general reference to the SLA table.
  A field that says only "see SLA ANALYSIS" or lists state names without row-level AT-RISK specificity fails.
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
Within each PHASE block: section 1. EXCEPTIONS is always first, section 2. STATES is always second.
Phase name must match PHASE MAP exactly.]

---

## PHASE: [PHASE NAME]

Entry trigger: [From PHASE MAP]
Owner: R-[N] -- [Role Name]
Exit condition: [From PHASE MAP]
Downstream handoff: [Artifact or TERMINAL:name]

### 1. EXCEPTIONS IN THIS PHASE
[This section is always the first declared output element in every phase block.
Write failure modes specific to this phase before any state detail is available.
Phase context is the scope: only generate exceptions whose trigger condition is plausible in this phase.
Generic exceptions (system error, network timeout) that apply to any phase are not acceptable.
Write each exception as a per-item answer block. A blank sub-field is a visible incomplete answer.
Write "No plausible exceptions in this phase -- rationale: [explain]" only if genuinely inapplicable.]

E-[N] -- [Exception Name]:
  Trigger state: S-[ID]: [state name -- must be a state in section 2. STATES of this phase]
  Trigger: [Phase-specific condition -- must be specific to work done in this phase]
  Trace: S-[ID] -> S-[ID] -> ... -> TERMINAL:[name]
  Handling role: R-[N] -- [Role Name]
  Terminal: TERMINAL:[name]

[Add one block per exception specific to this phase. All five sub-fields required per block.]

### 2. STATES IN THIS PHASE
[Written after section 1. Entry Condition and Exits columns required for every row.
Owner column must be an R-ID. Exit format: "[condition] -> S-[ID]" or "[condition] -> TERMINAL:[name]".]

| S-ID | State Name | Entry Condition | Owner (R-ID) | Exits (condition -> next) | Type |
|------|------------|-----------------|--------------|---------------------------|------|
| S-[ID] | [Name] | [Entry condition] | R-[N] | [cond] -> S-[ID]; [cond] -> S-[ID] | NORMAL |
[Add rows for all states in this phase. Terminal state rows: Owner = "--", Exits = "--".]

### Decision Supplement Blocks for This Phase
[One block per DECISION-type state in section 2. STATES.
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
The Evidence: field is required -- list each AT-RISK row in SLA ANALYSIS that cites this B-ID,
  identified by state name and S-ID. Required format per entry:
  "[State name -- S-ID]: AT-RISK, causal source: B-[ID]"
  A field that says only "see SLA ANALYSIS" or lists state names without AT-RISK row-level
  specificity is an incomplete answer.
Minimum 2 bottleneck blocks.]

B-01 -- [Bottleneck Name]:
  Phase: State or Transition: [Phase name: state name -- S-ID]
  Cause: [Specific operational reason -- not "slow approvals" but the precise bottleneck mechanism]
  Downstream impact: [Concrete effect on states or process timeline downstream]
  Owner: R-[N] -- [Role Name]
  SLA Nodes Affected: [State name(s) in SLA ANALYSIS whose AT-RISK entry cites this B-ID]
  Evidence: [List each AT-RISK row citing B-01 -- e.g., "S-05: Credit Hold Review -- AT-RISK, causal source: B-01"]

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
[3+ nodes annotated. Bidirectional chain rules:
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

Bidirectional evidence check:
  Forward (SLA -> B):  Every AT-RISK row cites a B-ID? [YES: closed | NO: list uncited AT-RISK rows]
  Backward (B -> SLA): Every B-ID's SLA Nodes Affected appears here as AT-RISK?
                        [YES: chain closed | NO: list B-IDs without matching AT-RISK rows]
  Chain status: CLOSED (all forward + backward links verified) / OPEN (list unresolved links)

---

Write artifact: simulations/flow/lifecycle/{topic}-lifecycle-{date}.md
Frontmatter: skill, topic, date, process_type, roles_count, phase_count, state_count,
exception_count, decision_count, bottleneck_count, gap_count, parallel_paths, terminal_states,
cross_process_count, sla_node_count, at_risk_count.
```

---

## V-05: Full Synthesis -- All Four R4 Criteria (C-18 + C-19 + C-20 + C-21)

**Axes:** All four: lifecycle emphasis (SECTION A/B ordinal labels, C-18, inherited from V-05 R3)
+ output format (Evidence field with specific AT-RISK row identifiers, C-19) + lifecycle emphasis
(standalone CHAIN STATUS gate, C-20) + unified architecture (C-21, explicit preamble rule)
**Hypothesis:** All four R4 criteria can be satisfied simultaneously without structural conflict.
SECTION A/B labels (C-18) and constructed-answer SECTION A blocks (C-21 mechanism) are co-located
in the phase template. Row-ID-specific Evidence fields (C-19) are in the BOTTLENECKS section.
The standalone CHAIN STATUS gate (C-20) is a dedicated top-level section after SLA ANALYSIS.
An explicit preamble rule names C-21's convergence requirement -- SECTION A is the single mechanism
for C-13 + C-15 + C-17; no separate structures are introduced for any constituent. Full V-05 R3
base preserved. Golden candidate for Round 4.

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

## Round 4 Design Notes

### Variation axis selection rationale

V-01 tests C-18 alternate ordinal format (1./2.) -- confirms rubric format-agnosticism; diagnostic
if it fails (would mean SECTION A/B wording matters, not just ordinal structure).

V-02 tests C-19 in isolation -- sharpened Evidence field with required format and explicit failure
condition for general references. C-18 passes from R3 SECTION A/B; C-20 borderline (embedded).

V-03 tests C-20 in isolation -- standalone CHAIN STATUS gate. C-18 passes from R3; C-19 borderline
(Evidence hint unchanged). The move from embedded `Chain status:` line to dedicated `## CHAIN STATUS`
section is the minimum structural change needed to clear the C-20 annotation failure condition.

V-04 combines V-01 + V-02: numbered labels + specific Evidence. Tests C-18 alt format + C-19
together. C-20 still borderline. Shows whether the two format changes compose without interference.

V-05 is the full golden candidate: V-03 (standalone CHAIN STATUS) + V-02 (Evidence specificity) +
SECTION A/B labels from R3 (C-18) + explicit C-21 preamble rule naming the convergence constraint.
The preamble rule is new: it states that SECTION A is the single mechanism for C-13 + C-15 + C-17,
not just an ordering instruction. This converts C-21 from an inferred architectural property into a
declared structural rule.

### What changed from V-05 R3 to V-05 R4

| Element | V-05 R3 | V-05 R4 |
|---------|---------|---------|
| Phase labels | SECTION A/B (C-18 pass) | SECTION A/B -- unchanged |
| Evidence field | Vague hint -- "entries that cite B-01" | Required format with state name + S-ID; explicit fail condition |
| Chain status | Embedded `Chain status:` line in SLA ANALYSIS check block | Dedicated `## CHAIN STATUS` top-level section |
| C-21 preamble | Absent | Explicit rule: "SECTION A is the single mechanism for C-13 + C-15 + C-17" |
