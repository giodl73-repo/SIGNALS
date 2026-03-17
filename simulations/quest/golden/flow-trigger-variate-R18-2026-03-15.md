---
skill: flow-trigger
round: 18
rubric_version: 17
new_criteria: [C-54, C-55, C-56]
date: 2026-03-15
---

# flow-trigger -- Round 18 (Rubric v17) Variations

**New criteria this round:**

- **C-54** -- Rule 3's consequence statement uses the em-dash two-part structure --
  assertion clause declaring the double violation plus em-dash separator plus operational
  restatement naming both FM-17 and FM-21 explicitly with their roles. C-52 requires Rule 3
  to name both FM IDs; this criterion requires the structural form to match the em-dash
  two-part architecture C-50 requires for Rule 1's sub-clause. A flat statement naming both
  FM IDs satisfies C-52 but fails C-54: the consequence is correct in content but structurally
  weaker. The em-dash form makes the double-violation structure independently auditable:
  assertion names the class ("double violation"), restatement names the components ("FM-17
  for register drift and FM-21 for the missing FM code"), so neither component can become
  implicit without a visible structural gap.

- **C-55** -- Invariant 3's em-dash restatement names "formal-register" as the obligation in
  both its assertion clause and its em-dash restatement half. A restatement that substitutes
  "platform-vocabulary" for "formal-register" creates an obligation-rationale inconsistency at
  the STRUCTURAL INVARIANT LAYER level, parallel to the C-48 inconsistency at Rule 1's
  sub-clause level. An Invariant 3 whose assertion clause references Invariant 2 (which governs
  formal-register) but whose em-dash restatement names "platform-vocabulary" is internally
  inconsistent: the two halves name different obligations, and a reader cannot determine from
  Invariant 3 alone which obligation governs the LIFECYCLE OVERVIEW table gate cells.

- **C-56** -- Rule 4 contains an explicit scope declaration limiting its independent-row
  verification requirement to gate cells within the LIFECYCLE OVERVIEW table and explicitly
  excluding phase-body gate statements from Rule 4's verification scope. Without this scope
  declaration, Rule 4's "check each gate cell independently" instruction appears to apply to
  all gate cells in the document. A reader must infer table-only scope from placement, which
  requires structural knowledge rather than reading Rule 4 alone. The scope limiter makes
  Rule 4's scope determinate by inspection, parallel to the jurisdictional clarity C-51
  establishes for Rule 1.

**Round 17 gap analysis:**

- V-01: C-51 FAIL -- Rule 1 ends after the formal-register sub-clause with no sentence
  distinguishing table-cell governance from phase-body governance; jurisdiction ambiguous
- V-02: C-52 FAIL -- Rule 3 names FM-17 but not FM-21; double-violation mechanism partially
  implicit; reader must supply FM-21 independently
- V-03: C-53 FAIL -- Invariant 3 restatement uses "summary nature" only, dropping "or
  overview"; overview artifacts arguably exempt from Invariant 3's prohibition
- V-04: C-51 FAIL + C-52 FAIL -- scope ambiguity and incomplete consequence co-occur
- V-05: C-51 PASS + C-52 PASS + C-53 PASS -- all three properties confirmed independently
  auditable and collectively sufficient to make the Rule 1 and Invariant 3 structures
  self-sealing at the R17 level

All R18 variations carry **full passes on C-01 through C-53**. The variation axis is the next
structural tier: Rule 3 em-dash architecture (C-54), Invariant 3 obligation-rationale
consistency (C-55), and Rule 4 jurisdictional scope declaration (C-56).

**Variation axes:**

| Variation | Axis | C-54 | C-55 | C-56 | Hypothesis |
|-----------|------|------|------|------|------------|
| V-01 | Rule 3 em-dash form present; Invariant 3 obligation drifts to "platform-vocabulary" in restatement; Rule 4 no scope declaration | PASS | FAIL | FAIL | C-52 passes: both FM IDs present. C-54 passes: Rule 3 uses assertion + em-dash + restatement matching Rule 1 sub-clause's C-50 architecture. C-55 fails: Invariant 3's assertion references Invariant 2 (formal-register) but restatement names "platform-vocabulary obligation" -- obligation inconsistency between halves, parallel to C-48's V-04 failure in R16. C-56 fails: Rule 4 ends after "Row N conformance does not imply Row N+1 conformance" with no scope limiter. |
| V-02 | Invariant 3 obligation-rationale consistent -- both halves name "formal-register"; Rule 3 flat form; Rule 4 no scope declaration | FAIL | PASS | FAIL | C-55 passes: Invariant 3 assertion and restatement both name "formal-register", no obligation drift. C-54 fails: Rule 3 uses a flat double-colon declaration naming both FM-17 and FM-21 (C-52 passes) but the em-dash two-part form is absent; assertion and operational restatement are merged into one clause. C-56 fails: Rule 4 no scope declaration. |
| V-03 | Rule 4 scope declaration present; Rule 3 flat form; Invariant 3 obligation drift | FAIL | FAIL | PASS | C-56 passes: Rule 4 ends with an explicit scope limiter excluding phase-body gate statements, parallel to Rule 1's C-51 scope limiter. C-54 fails: Rule 3 flat form. C-55 fails: Invariant 3 obligation drift to "platform-vocabulary" in restatement. |
| V-04 | Combined V-01 + V-02: Rule 3 em-dash AND Invariant 3 obligation consistent; Rule 4 no scope declaration | PASS | PASS | FAIL | C-54 and C-55 both pass. C-56 fails: Rule 4 still ends without explicit scope limiter; independent-row verification scope remains inferential rather than declared. The two passing properties are independently auditable from C-56. |
| V-05 | All three: Rule 3 em-dash + Invariant 3 obligation consistent + Rule 4 scope declaration | PASS | PASS | PASS | All three structural properties present. Rule 3 em-dash makes each component of the double violation independently named in the restatement. Invariant 3 is obligation-rationale consistent across both halves. Rule 4 scope declaration makes table-row verification and phase-body verification non-overlapping by declared boundary, not by placement inference. |

**Scenario used in all variations:** A Dataverse `opportunity` record's `statecode` field
has changed from `Open` (0) to `Won` (1) in a Dynamics 365 Sales environment with Power
Automate flows configured for the deal-close lifecycle.

---

## V-01

**Variation axis:** Rule 3 em-dash architecture present; Invariant 3 obligation-rationale
drift -- assertion references Invariant 2 (formal-register) but em-dash restatement names
"platform-vocabulary obligation"; Rule 4 no scope declaration

**Hypothesis:** C-54 passes: Rule 3's consequence uses the assertion + em-dash + operational
restatement form, matching Rule 1 sub-clause's C-50 structure; both FM-17 and FM-21 appear
in the restatement with their roles declared (C-52 also passes). C-55 fails: Invariant 3's
assertion clause correctly references Invariant 2 (which governs formal-register), but the
em-dash restatement substitutes "platform-vocabulary obligation" -- a different obligation
class. A reader auditing only Invariant 3's restatement concludes the LIFECYCLE OVERVIEW
table gate cells are subject to platform-vocabulary constraints rather than formal-register
constraints. This is the exact C-48 analog at the STRUCTURAL INVARIANT LAYER: a restatement
that names the wrong obligation is structurally worse than an absent restatement, because it
provides a definitive but incorrect answer. C-56 fails: Rule 4 ends after "Row N conformance
does not imply Row N+1 conformance" with no scope limiter; a reader scanning Rule 4 cannot
determine whether its independent-row verification requirement applies only to the LIFECYCLE
OVERVIEW table or extends to phase-body gates as well.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `opportunity` record's `statecode` field has changed from `Open` (0) to `Won` (1).
Your task: determine exactly which automations fire, in what order, with what inputs and
outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next
begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*This block is the governing contract layer. It SHALL appear before Phase 1 and SHALL contain
all three contract declarations: Platform Term Contract, FM Catalog, and Entry Schema Contract.*

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin, platform plugin |
| sync plug-in step | synchronous plugin, pre-stage plugin |
| async plug-in step | asynchronous plugin, background plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger, flow connector |

Any term deviating from this list SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is
itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift)
are structurally non-overlapping failure modes requiring separate FM IDs. The independence
covers all three intersection cases:*

*FM-16 alone: A phase has no entry condition. Defect is presence, not quality. Register
evaluation is not applicable -- no condition text exists to evaluate.
Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition stated descriptively rather than with formal
obligation language. Presence satisfied; only register quality fails.
Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern
indicates that a condition, if present, would also be stated descriptively. Both defects
co-occur and are independently taggable: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND
`[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three
cases -- separate IDs make each tag independently informative.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a
schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
Side Effects:       [field writes produced beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire in this scenario]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

*Distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and
schema contracts. This INVARIANT LAYER declares cross-phase structural obligations holding
simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites
the FM catalog ID whose inline tag signals a violation.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control
artifacts: entry condition, job description, and exit condition.
**Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase
bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position.
**Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW
table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL
satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The
LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function --
the summary or overview nature of an artifact does not confer exemption from the
platform-vocabulary obligation. A reader verifying Invariant 2 SHALL verify both phase-body
gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails
Invariant 2 even when the phase bodies themselves are conforming.
**Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL
include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1
SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N.
**Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
No artifact surface is exempt from this co-authority's formal-register
obligation, including any artifact whose nature is summary or overview -- the
summary or overview nature of an artifact does not confer exemption from the
formal-register obligation.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating a condition without an obligation verb is non-conforming
under this Rule and under Invariant 3.

Rule 3 (Self-tagging requirement): A non-conforming untagged gate cell
constitutes a double violation -- FM-17 for register drift and FM-21 for the
missing inline FM code -- and SHALL be tagged
[DOUBLE VIOLATION: FM-17 + FM-21 | cell description] inline within that cell.
A tag citing only FM-17 without FM-21 is itself a partial double violation and
SHALL be corrected to include both FM IDs.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been
received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1)
identify all candidate triggers without condition filtering and declare denominator N; (2) open
all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing
register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the opportunity statecode change from Open to Won cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this win transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly
question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1
is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute
`[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from
Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted
without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included.
[FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step
pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a
resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger
Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL
resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority.
[FM-02] Annotate latency tier (near-real-time / standard / batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step;
automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a
resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both
trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain originating from side-effect field writes to
its terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked
[TERMINAL]. [FM-20] Back-edge detection SHALL be applied to the adjacency structure to
identify any cycles. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes are
evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains
carry Chain-Status.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes.
Each verdict SHALL cite evidence from prior phases. Bare assertions SHALL be marked
`[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at
least one remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts are issued
with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts
are issued.

**Job:** Phase 6 SHALL produce a trigger map with execution-tier and Spawns columns covering
all triggers. Denominator closure SHALL be performed: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N ->
CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers
with all required columns and denominator closure is stated with CLOSED or GAP DETECTED.

---

## V-02

**Variation axis:** Invariant 3 obligation-rationale consistent -- assertion and em-dash
restatement both name "formal-register"; Rule 3 flat declaration form (no em-dash); Rule 4
no scope declaration

**Hypothesis:** C-55 passes: Invariant 3's assertion references Invariant 2 (formal-register)
and the em-dash restatement says "formal-register obligation" -- obligation consistent across
both halves, no drift. C-54 fails: Rule 3 states the double-violation consequence as a flat
declaration naming both FM IDs (C-52 passes) but no em-dash structural split; the assertion
clause and operational restatement naming each FM ID's role are merged into one clause rather
than separated by an em-dash. A flat statement is correct in content but does not independently
expose the two-component structure. C-56 fails: Rule 4 ends without scope declaration.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `opportunity` record's `statecode` field has changed from `Open` (0) to `Won` (1).
Your task: determine exactly which automations fire, in what order, with what inputs and
outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next
begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*This block is the governing contract layer. It SHALL appear before Phase 1 and SHALL contain
all three contract declarations: Platform Term Contract, FM Catalog, and Entry Schema Contract.*

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin, platform plugin |
| sync plug-in step | synchronous plugin, pre-stage plugin |
| async plug-in step | asynchronous plugin, background plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger, flow connector |

Any term deviating from this list SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is
itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift)
are structurally non-overlapping failure modes requiring separate FM IDs. FM-16 alone: defect
is presence, not quality. FM-17 alone: presence satisfied, only register quality fails. Both
simultaneously: independently taggable. A single FM ID would conflate all three cases.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a
schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
Side Effects:       [field writes produced beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire in this scenario]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control
artifacts: entry condition, job description, and exit condition.
**Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase
bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position.
**Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW
table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL
satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The
LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function --
the summary or overview nature of an artifact does not confer exemption from the
formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body
gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails
Invariant 2 even when the phase bodies themselves are conforming.
**Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL
include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1
SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N.
**Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
No artifact surface is exempt from this co-authority's formal-register
obligation, including any artifact whose nature is summary or overview -- the
summary or overview nature of an artifact does not confer exemption from the
formal-register obligation.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating a condition without an obligation verb is non-conforming
under this Rule and under Invariant 3.

Rule 3 (Self-tagging requirement): Any entry-condition or exit-condition cell
using descriptive state language SHALL be tagged [FM-17: Gate Register Drift]
inline within that cell. A non-conforming untagged cell carries a double
violation: FM-17 for register drift and FM-21 for the missing inline FM code.
Both FM IDs SHALL appear in the inline tag:
[DOUBLE VIOLATION: FM-17 + FM-21 | cell description].

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been
received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1)
identify all candidate triggers without condition filtering and declare denominator N; (2) open
all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing
register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the opportunity statecode change from Open to Won cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this win transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly
question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1
is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute
`[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from
Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted
without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included.
[FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step
pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a
resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger
Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL
resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority.
[FM-02] Annotate latency tier (near-real-time / standard / batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step;
automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a
resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both
trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain originating from side-effect field writes to
its terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked
[TERMINAL]. [FM-20] Back-edge detection SHALL be applied to the adjacency structure to
identify any cycles. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes are
evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains
carry Chain-Status.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes.
Each verdict SHALL cite evidence from prior phases. Bare assertions SHALL be marked
`[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at
least one remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts are issued
with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts
are issued.

**Job:** Phase 6 SHALL produce a trigger map with execution-tier and Spawns columns covering
all triggers. Denominator closure SHALL be performed: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N ->
CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers
with all required columns and denominator closure is stated with CLOSED or GAP DETECTED.

---

## V-03

**Variation axis:** Rule 4 scope declaration present; Rule 3 flat form; Invariant 3
obligation drift to "platform-vocabulary" in em-dash restatement

**Hypothesis:** C-56 passes: Rule 4 ends with an explicit scope declaration limiting its
independent-row verification to gate cells within this LIFECYCLE OVERVIEW table and
explicitly excluding phase-body gate statements. A reader scanning Rule 4 can determine
its scope from Rule 4 alone without inferring from document placement. C-54 fails: Rule 3
flat form -- both FM IDs present (C-52 passes) but no em-dash two-part structure. C-55
fails: Invariant 3 obligation drift -- the em-dash restatement names "platform-vocabulary
obligation" while the assertion references Invariant 2 (formal-register), creating
obligation inconsistency between halves.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `opportunity` record's `statecode` field has changed from `Open` (0) to `Won` (1).
Your task: determine exactly which automations fire, in what order, with what inputs and
outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next
begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*This block is the governing contract layer. It SHALL appear before Phase 1 and SHALL contain
all three contract declarations: Platform Term Contract, FM Catalog, and Entry Schema Contract.*

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin, platform plugin |
| sync plug-in step | synchronous plugin, pre-stage plugin |
| async plug-in step | asynchronous plugin, background plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger, flow connector |

Any term deviating from this list SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is
itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*FM-16 alone: presence defect; register evaluation not applicable. FM-17 alone: presence
satisfied, register quality fails. Both: independently taggable. Separate IDs make each
tag independently informative.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a
schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
Side Effects:       [field writes produced beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire in this scenario]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control
artifacts: entry condition, job description, and exit condition.
**Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase
bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position.
**Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW
table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL
satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The
LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function --
the summary or overview nature of an artifact does not confer exemption from the
platform-vocabulary obligation. A reader verifying Invariant 2 SHALL verify both phase-body
gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails
Invariant 2 even when the phase bodies themselves are conforming.
**Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL
include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1
SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N.
**Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
No artifact surface is exempt from this co-authority's formal-register
obligation, including any artifact whose nature is summary or overview -- the
summary or overview nature of an artifact does not confer exemption from the
formal-register obligation.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating a condition without an obligation verb is non-conforming
under this Rule and under Invariant 3.

Rule 3 (Self-tagging requirement): Any entry-condition or exit-condition cell
using descriptive state language SHALL be tagged [FM-17: Gate Register Drift]
inline within that cell. A non-conforming untagged cell carries a double
violation: FM-17 for register drift and FM-21 for the missing inline FM code.
Both FM IDs SHALL appear in the inline tag:
[DOUBLE VIOLATION: FM-17 + FM-21 | cell description].

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance. This Rule governs gate-cell verification within this
LIFECYCLE OVERVIEW table only. Phase-body gate-statement verification is governed
separately by Invariant 2 and the individual phase-body specifications; Rule 4's
independent-row verification requirement does not extend to phase-body gate
statements.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been
received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1)
identify all candidate triggers without condition filtering and declare denominator N; (2) open
all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing
register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the opportunity statecode change from Open to Won cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this win transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly
question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1
is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute
`[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from
Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted
without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included.
[FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step
pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a
resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger
Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL
resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority.
[FM-02] Annotate latency tier (near-real-time / standard / batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step;
automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a
resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both
trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain originating from side-effect field writes to
its terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked
[TERMINAL]. [FM-20] Back-edge detection SHALL be applied to the adjacency structure to
identify any cycles. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes are
evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains
carry Chain-Status.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes.
Each verdict SHALL cite evidence from prior phases. Bare assertions SHALL be marked
`[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at
least one remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts are issued
with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts
are issued.

**Job:** Phase 6 SHALL produce a trigger map with execution-tier and Spawns columns covering
all triggers. Denominator closure SHALL be performed: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N ->
CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers
with all required columns and denominator closure is stated with CLOSED or GAP DETECTED.

---

## V-04

**Variation axis:** Combined V-01 + V-02 -- Rule 3 em-dash form AND Invariant 3
obligation-rationale consistent ("formal-register" in both halves); Rule 4 no scope
declaration

**Hypothesis:** C-54 passes: Rule 3 uses assertion + em-dash + operational restatement, both
FM IDs named with their roles in the restatement. C-55 passes: Invariant 3 assertion and
em-dash restatement both name "formal-register", no drift. C-56 fails: Rule 4 ends after
"Row N conformance does not imply Row N+1 conformance" with no scope limiter. A document
can have a structurally complete Rule 3 and an obligation-consistent Invariant 3 while
leaving Rule 4's verification scope inferential rather than declared.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `opportunity` record's `statecode` field has changed from `Open` (0) to `Won` (1).
Your task: determine exactly which automations fire, in what order, with what inputs and
outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next
begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*This block is the governing contract layer. It SHALL appear before Phase 1 and SHALL contain
all three contract declarations: Platform Term Contract, FM Catalog, and Entry Schema Contract.*

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin, platform plugin |
| sync plug-in step | synchronous plugin, pre-stage plugin |
| async plug-in step | asynchronous plugin, background plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger, flow connector |

Any term deviating from this list SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is
itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*FM-16 alone: presence defect; register evaluation not applicable. FM-17 alone: presence
satisfied, register quality fails. Both: independently taggable. Separate IDs make each
tag independently informative.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a
schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
Side Effects:       [field writes produced beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire in this scenario]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control
artifacts: entry condition, job description, and exit condition.
**Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase
bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position.
**Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW
table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL
satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The
LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function --
the summary or overview nature of an artifact does not confer exemption from the
formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body
gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails
Invariant 2 even when the phase bodies themselves are conforming.
**Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL
include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1
SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N.
**Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
No artifact surface is exempt from this co-authority's formal-register
obligation, including any artifact whose nature is summary or overview -- the
summary or overview nature of an artifact does not confer exemption from the
formal-register obligation.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating a condition without an obligation verb is non-conforming
under this Rule and under Invariant 3.

Rule 3 (Self-tagging requirement): A non-conforming untagged gate cell
constitutes a double violation -- FM-17 for register drift and FM-21 for the
missing inline FM code -- and SHALL be tagged
[DOUBLE VIOLATION: FM-17 + FM-21 | cell description] inline within that cell.
A tag citing only FM-17 without FM-21 is itself a partial double violation and
SHALL be corrected to include both FM IDs.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been
received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1)
identify all candidate triggers without condition filtering and declare denominator N; (2) open
all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing
register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the opportunity statecode change from Open to Won cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this win transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly
question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1
is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute
`[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from
Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted
without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included.
[FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step
pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a
resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger
Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL
resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority.
[FM-02] Annotate latency tier (near-real-time / standard / batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step;
automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a
resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both
trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain originating from side-effect field writes to
its terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked
[TERMINAL]. [FM-20] Back-edge detection SHALL be applied to the adjacency structure to
identify any cycles. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes are
evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains
carry Chain-Status.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes.
Each verdict SHALL cite evidence from prior phases. Bare assertions SHALL be marked
`[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at
least one remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts are issued
with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts
are issued.

**Job:** Phase 6 SHALL produce a trigger map with execution-tier and Spawns columns covering
all triggers. Denominator closure SHALL be performed: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N ->
CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers
with all required columns and denominator closure is stated with CLOSED or GAP DETECTED.

---

## V-05

**Variation axis:** Full combination -- Rule 3 em-dash form, Invariant 3 obligation-rationale
consistent ("formal-register" in both halves), Rule 4 scope declaration present

**Hypothesis:** All three properties present. C-54 passes: Rule 3 uses assertion + em-dash +
operational restatement naming FM-17 and FM-21 with their roles explicitly stated in the
restatement half. C-55 passes: Invariant 3's assertion references Invariant 2 and the em-dash
restatement names "formal-register obligation" -- no drift, both halves name the same
obligation. C-56 passes: Rule 4 ends with an explicit scope declaration limiting its
independent-row verification to gate cells within this LIFECYCLE OVERVIEW table and excluding
phase-body gate statements. The three properties are independently auditable and collectively
sufficient: a reader can verify each of Rule 3's em-dash structure, Invariant 3's obligation
consistency, and Rule 4's scope boundary by local inspection of each artifact alone, without
cross-referencing other sections or consulting the rubric.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `opportunity` record's `statecode` field has changed from `Open` (0) to `Won` (1).
Your task: determine exactly which automations fire, in what order, with what inputs and
outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next
begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*This block is the governing contract layer. It SHALL appear before Phase 1 and SHALL contain
all three contract declarations: Platform Term Contract, FM Catalog, and Entry Schema Contract.*

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin, platform plugin |
| sync plug-in step | synchronous plugin, pre-stage plugin |
| async plug-in step | asynchronous plugin, background plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger, flow connector |

Any term deviating from this list SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is
itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*FM-16 alone: presence defect; register evaluation not applicable. FM-17 alone: presence
satisfied, register quality fails. Both: independently taggable. Separate IDs make each
tag independently informative.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a
schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
Side Effects:       [field writes produced beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire in this scenario]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control
artifacts: entry condition, job description, and exit condition.
**Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase
bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position.
**Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW
table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL
satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The
LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function --
the summary or overview nature of an artifact does not confer exemption from the
formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body
gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails
Invariant 2 even when the phase bodies themselves are conforming.
**Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL
include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1
SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N.
**Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
No artifact surface is exempt from this co-authority's formal-register
obligation, including any artifact whose nature is summary or overview -- the
summary or overview nature of an artifact does not confer exemption from the
formal-register obligation.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating a condition without an obligation verb is non-conforming
under this Rule and under Invariant 3.

Rule 3 (Self-tagging requirement): A non-conforming untagged gate cell
constitutes a double violation -- FM-17 for register drift and FM-21 for the
missing inline FM code -- and SHALL be tagged
[DOUBLE VIOLATION: FM-17 + FM-21 | cell description] inline within that cell.
A tag citing only FM-17 without FM-21 is itself a partial double violation and
SHALL be corrected to include both FM IDs.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance. This Rule governs gate-cell verification within this
LIFECYCLE OVERVIEW table only. Phase-body gate-statement verification is governed
separately by Invariant 2 and the individual phase-body specifications; Rule 4's
independent-row verification requirement does not extend to phase-body gate
statements.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been
received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1)
identify all candidate triggers without condition filtering and declare denominator N; (2) open
all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing
register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the opportunity statecode change from Open to Won cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this win transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly
question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1
is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute
`[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from
Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted
without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included.
[FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step
pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a
resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger
Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL
resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority.
[FM-02] Annotate latency tier (near-real-time / standard / batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step;
automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a
resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both
trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain originating from side-effect field writes to
its terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked
[TERMINAL]. [FM-20] Back-edge detection SHALL be applied to the adjacency structure to
identify any cycles. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes are
evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains
carry Chain-Status.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes.
Each verdict SHALL cite evidence from prior phases. Bare assertions SHALL be marked
`[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at
least one remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts are issued
with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts
are issued.

**Job:** Phase 6 SHALL produce a trigger map with execution-tier and Spawns columns covering
all triggers. Denominator closure SHALL be performed: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N ->
CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers
with all required columns and denominator closure is stated with CLOSED or GAP DETECTED.
