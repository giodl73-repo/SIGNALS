---
skill: flow-trigger
round: 19
rubric_version: 18
new_criteria: [C-57, C-58, C-59]
date: 2026-03-15
---

# flow-trigger -- Round 19 (Rubric v18) Variations

**New criteria this round:**

- **C-57** -- Rule 4's scope declaration uses em-dash two-part structure: assertion clause
  naming the table-only scope restriction + em-dash separator + operational restatement
  explicitly naming the excluded scope (phase-body gate statements) and their governing
  authority (Invariant 2). C-56 requires the scope declaration to exist; C-57 requires it to
  follow the same em-dash two-part architecture as Rule 1's sub-clause (C-50), Rule 3's
  consequence (C-54), and Invariant 3's restatement (C-46). A period-separated form satisfies
  C-56 (declaration present) but fails C-57 because the assertion and restatement are split into
  independent sentences rather than positioned as a structurally bound assertion-restatement
  pair. The em-dash form makes the scope assertion ("Row N conformance does not imply Row N+1
  conformance") and the exclusion restatement structurally inseparable: a reader who internalizes
  the assertion clause must read through the em-dash to find the exclusion boundary and governing
  authority. A period-separated form can be read with each sentence standing alone, making the
  assertion-restatement relationship inferential rather than structural.

- **C-58** -- Rule 2 contains an explicit forward reference to Rule 3 naming it as the
  self-tagging consequence mechanism for non-conforming cells, making Rule 2's
  obligation-to-consequence chain navigable by local inspection of Rule 2 alone without
  sequential reading. The baseline form of Rule 2 ends with "non-conforming under this Rule and
  under Invariant 3" -- the consequence (self-tagging per Rule 3) is discoverable only by reading
  Rule 3 sequentially. A Rule 2 that adds "non-conforming cells are subject to Rule 3's
  self-tagging requirement" closes the forward-reference gap: a reader auditing a gate cell
  against Rule 2 encounters the consequence within Rule 2's own text. Without the forward
  reference, Rule 2 is complete in its obligation statement but silent about its consequence,
  producing a rule that a reader can fully satisfy without knowing that Rule 3 exists or what it
  requires. The forward reference makes the two-rule obligation chain a named structural
  dependency rather than an incidental sequential placement.

- **C-59** -- The STRUCTURAL INVARIANT LAYER declares a named Invariant 6 stating the
  co-authority verification requirement for LIFECYCLE OVERVIEW table gate cells: a verifier SHALL
  check each gate cell against BOTH the FORMAL-GATE ZONE DECLARATION (Rules 1-4) AND Invariant 3
  simultaneously, and partial verification against one authority only is insufficient even when
  that authority's requirements are individually satisfied. Without Invariant 6, the co-authority
  relationship is declared (Rule 1 names both co-authoritative sources) but the verification
  obligation is implicit: a reader who satisfies Rule 1 through Rule 4 and treats verification as
  complete has not violated any stated obligation, because no invariant explicitly requires
  dual-authority checking. Invariant 6 makes dual-authority verification a structural obligation
  with a taggable defect class (FM-26: Co-authority Partial) for partial-verification violations.
  The FM catalog MUST include FM-26 when Invariant 6 is declared; an FM-26 inline tag referencing
  a catalog entry that does not exist is itself an FM-21 violation.

**Round 18 gap analysis:**

- V-01: C-55 FAIL -- Invariant 3's em-dash restatement substitutes "platform-vocabulary
  obligation" for "formal-register obligation"; obligation drift between assertion and restatement
  halves; C-56 FAIL -- Rule 4 ends with no scope declaration
- V-02: C-54 FAIL -- Rule 3 uses flat colon-separated form; double-violation content correct per
  C-52 but em-dash two-part structure absent; C-56 FAIL -- Rule 4 no scope declaration
- V-03: C-54 FAIL -- Rule 3 flat form; C-55 FAIL -- Invariant 3 obligation drift to
  "platform-vocabulary"
- V-04: C-54 FAIL + C-56 FAIL -- Rule 3 flat form and Rule 4 no scope declaration; C-55 PASS
- V-05: C-54 PASS + C-55 PASS + C-56 PASS -- all three properties confirmed independently
  auditable and collectively sufficient

All R19 variations carry **full passes on C-01 through C-56**. The variation axis is the next
structural tier: Rule 4 em-dash architecture (C-57), Rule 2 obligation-to-consequence forward
reference (C-58), and Invariant 6 co-authority verification requirement (C-59).

**Variation axes:**

| Variation | Axis | C-57 | C-58 | C-59 | Hypothesis |
|-----------|------|------|------|------|------------|
| V-01 | Rule 4 em-dash scope declaration present; Rule 2 no forward ref to Rule 3; no Invariant 6 | PASS | FAIL | FAIL | C-57 passes: Rule 4's scope declaration uses em-dash form -- "Row N conformance does not imply Row N+1 conformance" serves as the assertion clause, em-dash introduces the exclusion restatement naming phase-body gate statements and Invariant 2 as governing authority. C-58 fails: Rule 2 ends with "non-conforming under this Rule and under Invariant 3" with no forward reference to Rule 3; the obligation-to-consequence chain requires sequential reading to discover Rule 3's self-tagging requirement. C-59 fails: Invariant 6 absent; co-authority verification is declared (Rule 1 names both sources) but no invariant makes dual-authority checking a structural obligation. |
| V-02 | Rule 4 period-separated scope declaration; Rule 2 with explicit Rule 3 forward reference; no Invariant 6 | FAIL | PASS | FAIL | C-58 passes: Rule 2 ends with "...non-conforming under this Rule and under Invariant 3; non-conforming cells are subject to Rule 3's self-tagging requirement" -- obligation-to-consequence chain navigable from Rule 2 alone. C-57 fails: Rule 4's scope declaration uses period-separated sentences; the assertion ("table only") and the exclusion restatement (Invariant 2 as authority) are two independent sentences, not an em-dash-bound assertion-restatement pair. C-59 fails: no Invariant 6. |
| V-03 | Rule 4 period-separated scope; Rule 2 no forward ref; Invariant 6 present with FM-26 | FAIL | FAIL | PASS | C-59 passes: Invariant 6 declares co-authority verification as a structural obligation; FM-26 tags partial-verification violations; FM catalog includes FM-26. C-57 fails: Rule 4 period-separated form. C-58 fails: Rule 2 no Rule 3 forward reference. |
| V-04 | Rule 4 em-dash form + Rule 2 Rule 3 forward ref; no Invariant 6 | PASS | PASS | FAIL | C-57 and C-58 both pass. C-59 fails: Invariant 6 absent; co-authority verification obligation remains implicit even though co-authority is declared in Rule 1. The two passing properties are independently auditable from C-59. |
| V-05 | All three: Rule 4 em-dash + Rule 2 Rule 3 forward ref + Invariant 6 with FM-26 | PASS | PASS | PASS | All three properties present. Rule 4's scope declaration uses em-dash two-part architecture, making the scope assertion and exclusion restatement structurally bound. Rule 2 names Rule 3 as the self-tagging consequence, closing the obligation-to-consequence forward reference. Invariant 6 declares dual-authority verification as an explicit structural obligation with FM-26 as the taggable defect class for partial verification. Each property is independently verifiable by local inspection of its respective artifact. |

**Scenario used in all variations:** A Dynamics 365 Sales `account` record's `statecode` field
has changed from `Active` (0) to `Inactive` (1) in an environment with Power Automate flows
configured for the account suspension lifecycle.

---

## V-01

**Variation axis:** Rule 4 em-dash scope declaration present; Rule 2 no forward reference to
Rule 3; Invariant 6 absent

**Hypothesis:** C-57 passes: Rule 4's scope declaration uses em-dash two-part form -- the
assertion clause ("Row N conformance does not imply Row N+1 conformance") is followed by an
em-dash separator and an operational restatement naming phase-body gate statements as the
excluded scope and Invariant 2 as their governing authority. A reader who internalizes the
assertion must read through to the restatement to determine the exclusion boundary; the two
halves are structurally bound, not independent sentences. C-58 fails: Rule 2 ends with
"non-conforming under this Rule and under Invariant 3" -- Rule 3 is never named as the
consequence mechanism; a reader auditing Rule 2 cannot determine the self-tagging consequence
without consulting Rule 3 sequentially. C-59 fails: Invariant 6 is absent; Rule 1 declares
co-authority but no invariant makes dual-authority verification a stated structural obligation;
a verifier who satisfies Rules 1-4 alone has not violated any declared obligation.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

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
imply Row N+1 conformance -- phase-body gate-statement verification is governed
separately by Invariant 2 and the individual phase-body specifications, and
Rule 4's independent-row verification requirement does not extend to phase-body
gate statements.
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
| Trigger Storm | Does the account statecode change from Active to Inactive cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this suspension transition that does not appear in the trigger surface? | OPEN |
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

**Variation axis:** Rule 4 period-separated scope declaration; Rule 2 with explicit Rule 3
forward reference; Invariant 6 absent

**Hypothesis:** C-58 passes: Rule 2 ends with "...non-conforming under this Rule and under
Invariant 3; non-conforming cells are subject to Rule 3's self-tagging requirement" -- the
obligation-to-consequence chain is navigable from Rule 2 alone without sequential reading of
Rule 3. A reader auditing a gate cell against Rule 2 encounters the consequence (Rule 3's
self-tagging) within Rule 2's own text. C-57 fails: Rule 4's scope declaration uses
period-separated sentences -- "This Rule governs gate-cell verification within this LIFECYCLE
OVERVIEW table only." is a standalone sentence, and "Phase-body gate-statement verification is
governed separately by Invariant 2..." is a second standalone sentence. The two sentences are
correct in content per C-56 (scope declaration present) but are structurally independent: the
assertion clause and the exclusion restatement are not bound by an em-dash separator and can
each be read in isolation without recognizing that they constitute a two-part assertion-restatement
pair. C-59 fails: Invariant 6 absent.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

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
is presence, not quality; register evaluation not applicable. FM-17 alone: presence satisfied,
register quality fails. Both simultaneously: independently taggable. A single FM ID would
conflate all three cases -- separate IDs make each tag independently informative.*

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
under this Rule and under Invariant 3; non-conforming cells are subject to
Rule 3's self-tagging requirement.

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
| Trigger Storm | Does the account statecode change from Active to Inactive cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this suspension transition that does not appear in the trigger surface? | OPEN |
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

**Variation axis:** Rule 4 period-separated scope declaration; Rule 2 no forward reference to
Rule 3; Invariant 6 present with FM-26

**Hypothesis:** C-59 passes: Invariant 6 is declared in the STRUCTURAL INVARIANT LAYER,
stating that a verifier SHALL check LIFECYCLE OVERVIEW gate cells against BOTH the
FORMAL-GATE ZONE DECLARATION AND Invariant 3 simultaneously; partial-verification violations
are taggable as FM-26 (Co-authority Partial); FM catalog includes FM-26. C-57 fails: Rule 4
uses period-separated sentences for its scope declaration -- the assertion clause ("This Rule
governs gate-cell verification within this LIFECYCLE OVERVIEW table only.") and the exclusion
restatement ("Phase-body gate-statement verification is governed separately by Invariant 2...")
are two independent sentences. Both sentences together satisfy C-56 (scope declaration present)
but the em-dash structural binding required by C-57 is absent. C-58 fails: Rule 2 ends with
"non-conforming under this Rule and under Invariant 3" -- Rule 3 is not named as the consequence
mechanism; the obligation-to-consequence chain requires sequential reading.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

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
| FM-26 | Co-authority partial verification | A LIFECYCLE OVERVIEW gate cell was verified against only one co-authoritative source; Rule 1 requires simultaneous dual-authority checking against both the FORMAL-GATE ZONE DECLARATION and Invariant 3 | `[CO-AUTH PARTIAL: DECLARATION-only / Invariant-3-only \| FM-26]` | All |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is
itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift)
are structurally non-overlapping failure modes requiring separate FM IDs. FM-16 alone: defect
is presence, not quality; register evaluation not applicable. FM-17 alone: presence satisfied,
register quality fails. Both simultaneously: independently taggable. A single FM ID would
conflate all three cases -- separate IDs make each tag independently informative.*

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
formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body
gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails
Invariant 2 even when the phase bodies themselves are conforming.
**Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL
include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1
SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N.
**Violation taggable as: `[RECON MISS | FM-22]`.**

**Invariant 6 -- Co-authority verification requirement:** A verifier assessing conformance of
LIFECYCLE OVERVIEW table gate cells SHALL verify each cell against BOTH the FORMAL-GATE ZONE
DECLARATION (Rules 1-4) AND Invariant 3 simultaneously. Partial verification against one
authority only is INSUFFICIENT -- verifying only against the FORMAL-GATE ZONE DECLARATION
without Invariant 3, or only against Invariant 3 without the FORMAL-GATE ZONE DECLARATION,
fails to satisfy the co-authority obligation declared in Rule 1. A verification pass on one
authority does not imply a verification pass on the co-authority.
**Violation taggable as: `[CO-AUTH PARTIAL: DECLARATION-only / Invariant-3-only | FM-26]`.**

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
| Trigger Storm | Does the account statecode change from Active to Inactive cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this suspension transition that does not appear in the trigger surface? | OPEN |
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

**Variation axis:** Rule 4 em-dash scope declaration + Rule 2 with Rule 3 forward reference;
Invariant 6 absent

**Hypothesis:** C-57 passes: Rule 4's scope declaration uses em-dash two-part form, making the
scope assertion and exclusion restatement structurally bound as an assertion-restatement pair
rather than independent sentences. C-58 passes: Rule 2 ends with "...non-conforming under this
Rule and under Invariant 3; non-conforming cells are subject to Rule 3's self-tagging
requirement" -- the obligation-to-consequence chain navigable from Rule 2 alone. C-59 fails:
Invariant 6 is absent; the co-authority relationship is declared in Rule 1 (both sources named)
but no invariant makes dual-authority verification a structural obligation. A verifier who
satisfies Rules 1-4 of the FORMAL-GATE ZONE DECLARATION has not violated any stated obligation
by not also separately verifying against Invariant 3, because no invariant makes that
simultaneous check a declared requirement. C-57 and C-58 are independently auditable from C-59:
a reader can verify Rule 4's em-dash form and Rule 2's forward reference without consulting the
STRUCTURAL INVARIANT LAYER.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

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
is presence, not quality; register evaluation not applicable. FM-17 alone: presence satisfied,
register quality fails. Both simultaneously: independently taggable. A single FM ID would
conflate all three cases -- separate IDs make each tag independently informative.*

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
under this Rule and under Invariant 3; non-conforming cells are subject to
Rule 3's self-tagging requirement.

Rule 3 (Self-tagging requirement): A non-conforming untagged gate cell
constitutes a double violation -- FM-17 for register drift and FM-21 for the
missing inline FM code -- and SHALL be tagged
[DOUBLE VIOLATION: FM-17 + FM-21 | cell description] inline within that cell.
A tag citing only FM-17 without FM-21 is itself a partial double violation and
SHALL be corrected to include both FM IDs.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance -- phase-body gate-statement verification is governed
separately by Invariant 2 and the individual phase-body specifications, and
Rule 4's independent-row verification requirement does not extend to phase-body
gate statements.
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
| Trigger Storm | Does the account statecode change from Active to Inactive cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this suspension transition that does not appear in the trigger surface? | OPEN |
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

**Variation axis:** Full combination -- Rule 4 em-dash scope declaration, Rule 2 with Rule 3
forward reference, Invariant 6 with FM-26

**Hypothesis:** All three properties present. C-57 passes: Rule 4's scope declaration uses
em-dash two-part form -- the assertion clause and the exclusion restatement naming Invariant 2
as governing authority are structurally bound by an em-dash separator rather than split into
independent sentences. A reader who internalizes the assertion ("Row N conformance does not
imply Row N+1 conformance") must read through to the restatement to determine the exclusion
boundary; neither half is independently complete. C-58 passes: Rule 2 ends with "...non-conforming
under this Rule and under Invariant 3; non-conforming cells are subject to Rule 3's self-tagging
requirement" -- the obligation-to-consequence chain navigable from Rule 2 alone; a reader
auditing a gate cell against Rule 2 finds the consequence (Rule 3) within Rule 2's own text
without sequential reading. C-59 passes: Invariant 6 declares dual-authority verification as an
explicit structural obligation; FM-26 is added to the FM catalog; a verifier who checks only the
FORMAL-GATE ZONE DECLARATION or only Invariant 3 can be tagged FM-26. The three properties are
independently verifiable: C-57 is auditable from Rule 4 text alone, C-58 from Rule 2 text alone,
and C-59 from the STRUCTURAL INVARIANT LAYER alone.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

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
| FM-26 | Co-authority partial verification | A LIFECYCLE OVERVIEW gate cell was verified against only one co-authoritative source; Rule 1 requires simultaneous dual-authority checking against both the FORMAL-GATE ZONE DECLARATION and Invariant 3 | `[CO-AUTH PARTIAL: DECLARATION-only / Invariant-3-only \| FM-26]` | All |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is
itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift)
are structurally non-overlapping failure modes requiring separate FM IDs. FM-16 alone: defect
is presence, not quality; register evaluation not applicable. FM-17 alone: presence satisfied,
register quality fails. Both simultaneously: independently taggable. A single FM ID would
conflate all three cases -- separate IDs make each tag independently informative.*

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
formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body
gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails
Invariant 2 even when the phase bodies themselves are conforming.
**Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL
include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1
SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N.
**Violation taggable as: `[RECON MISS | FM-22]`.**

**Invariant 6 -- Co-authority verification requirement:** A verifier assessing conformance of
LIFECYCLE OVERVIEW table gate cells SHALL verify each cell against BOTH the FORMAL-GATE ZONE
DECLARATION (Rules 1-4) AND Invariant 3 simultaneously. Partial verification against one
authority only is INSUFFICIENT -- verifying only against the FORMAL-GATE ZONE DECLARATION
without Invariant 3, or only against Invariant 3 without the FORMAL-GATE ZONE DECLARATION,
fails to satisfy the co-authority obligation declared in Rule 1. A verification pass on one
authority does not imply a verification pass on the co-authority.
**Violation taggable as: `[CO-AUTH PARTIAL: DECLARATION-only / Invariant-3-only | FM-26]`.**

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
under this Rule and under Invariant 3; non-conforming cells are subject to
Rule 3's self-tagging requirement.

Rule 3 (Self-tagging requirement): A non-conforming untagged gate cell
constitutes a double violation -- FM-17 for register drift and FM-21 for the
missing inline FM code -- and SHALL be tagged
[DOUBLE VIOLATION: FM-17 + FM-21 | cell description] inline within that cell.
A tag citing only FM-17 without FM-21 is itself a partial double violation and
SHALL be corrected to include both FM IDs.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance -- phase-body gate-statement verification is governed
separately by Invariant 2 and the individual phase-body specifications, and
Rule 4's independent-row verification requirement does not extend to phase-body
gate statements.
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
| Trigger Storm | Does the account statecode change from Active to Inactive cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this suspension transition that does not appear in the trigger surface? | OPEN |
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
