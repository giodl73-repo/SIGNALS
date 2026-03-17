# Flow-Trigger Skill — Round 3 Variations (Rubric v3)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v3 (C-01 through C-15)
**Date**: 2026-03-15

---

## Variation Design Notes

### R2 Scorecard Summary (Rubric v2, C-01–C-13)

| Variation | Score | Passed Aspirational | Key Gap |
|-----------|-------|---------------------|---------|
| V-01 | 97 | C-10, C-11, C-12, C-13 | C-08 (no remediation), C-09 (no trigger map) |
| V-02 | 95 | C-09, C-11 | C-08, C-10 (no pre-opened slots), C-12/C-13 partial |
| V-03 | 95 | C-11, C-12, C-13 | C-08, C-09, C-10 |
| V-04 | 96 | C-10, C-11, C-13 | C-08, C-09, C-12 partial |
| V-05 | 98 | C-08, C-10, C-11, C-12, C-13 | C-09 (no trigger map) |

**Root observation**: No R2 variation passed both C-08 (remediation in verdict blocks) AND C-09 (trigger map). V-05 had the most complete aspirational coverage but still missed C-09. V-02 had the trigger map (and is the C-15 source) but missed C-10 and C-08.

### What R3 Must Achieve

New criteria C-14 and C-15 add to the aspirational bucket. The full target:

| Criterion | R2 Best Source | R3 Obligation |
|---|---|---|
| C-08 remediation | V-05 (structural MITIGATION clause) | Carry forward — embed in verdict block |
| C-09 trigger map | V-02 (trigger map appendix) | Combine with C-08 — can't be in separate variations |
| C-10 pre-opened slots | V-01, V-04, V-05 (Section 0 register) | Carry forward |
| C-11 cascade completeness | All R2 (Spawns field) | Carry forward |
| C-12 self-annotating | V-05 (6-tag vocabulary) | Carry forward |
| C-13 evidence-anchored verdicts | V-05 (structural EVIDENCE BLOCK) | Carry forward |
| C-14 denominator declared | New — V-01/V-03/V-04 had pre-scans but C-14 was not a named criterion | Add explicit denominator gate before first entry |
| C-15 trigger map with tier+spawns | New — V-02's trigger map had these columns | Require both columns in the trigger map |

**R3 design imperative**: Every variation must unify C-08 + C-09/C-15. Single-axis variations in R3 explore HOW to achieve that unification; the axes are combinations of structural strategies.

### Variation Axes

| Variation | Primary Axis | Secondary Axis | Hypothesis |
|---|---|---|---|
| V-01 | Output format (trigger map as primary artifact, not appendix) | — | Building the map FIRST makes C-09/C-15 structurally prior; entries POPULATE the map rows |
| V-02 | Role sequence (Scanner → Enumerator → Auditor) | — | Non-overlapping roles separate denominator/pre-scan (Scanner) from enumeration (Enumerator) from map+remediation (Auditor) |
| V-03 | Phrasing register (extend V-05 failure mode catalog to FM-11) | — | Adding FM-10 (map deficiency) and FM-11 (missing denominator) closes the last two untagged defect classes |
| V-04 | Lifecycle emphasis (phase gate model with explicit gate conditions) | — | Making C-14 a Phase 1 gate and C-15 an Appendix gate turns criteria into blocking preconditions |
| V-05 | Inertia framing (each rule introduced as override of named default behavior) | — | Showing WHY the default output fails (not just WHAT to produce) improves comprehension-based compliance |

---

## V-01 — Output Format: Trigger Map as Primary Artifact

**Axis**: Output format
**Hypothesis**: When the trigger map is the organizing artifact (not an appendix), C-09 and C-15 are structurally prior to enumeration. Cascade spawn references (Spawns column with row numbers) enforce C-11. The map's pre-construction requires the denominator count (C-14) as the row allocation step.

---

You are a Power Automate / Copilot Studio domain expert. Analyze which automations fire for the given record change.

**SCENARIO**

{SCENARIO_DESCRIPTION}

---

**STEP 0 — GOVERNANCE SETUP**

Declare the term inventory and open anomaly investigations. This step precedes all analysis.

Platform Term Contract (use ONLY these labels throughout — any other term is a vocabulary violation):

Execution tiers:
- sync plugin step
- async plugin step
- instant flow
- automated flow
- scheduled flow

Connector terms for this scenario: [list relevant connectors — e.g., "Dataverse connector — When a row is added, modified, or deleted", "Office 365 Outlook — Send an email (V2)"]

Anomaly Investigation Register (open all three before STEP 1):

| Investigation | Status | Evidence | Verdict | Mitigation |
|---|---|---|---|---|
| STORM | OPEN | — | — | — |
| MISSING TRIGGER | OPEN | — | — | — |
| CIRCULAR TRIGGER | OPEN | — | — | — |

---

**STEP 1 — CANDIDATE PRE-SCAN**

Before building the trigger map, enumerate all automation candidates that COULD fire for this record change. Scan every automation layer. Do not apply condition filters here — list structural candidates only.

Layers to scan (in order):
1. Dataverse synchronous plugin steps
2. Dataverse asynchronous plugin steps
3. Power Automate automated flows (Dataverse connector)
4. Power Automate instant flows
5. Power Automate scheduled flows
6. Copilot Studio topic triggers

| # | Candidate Name | Layer | Why It Is a Candidate |
|---|---|---|---|
| 1 | [name] | [layer] | [reason] |
| ... | | | |

**CANDIDATE DENOMINATOR: [N] candidates identified.**

This number is the audit baseline. The trigger map in STEP 2 must resolve exactly N candidates — each as a firing row (YES) or a non-firing exclusion row (NO). If the map resolves fewer than N, missing candidates are tagged [UNRESOLVED CANDIDATE: {name}].

---

**STEP 2 — TRIGGER MAP CONSTRUCTION**

Build the trigger map row-by-row. The map is the primary output artifact. Numbered entries are built to fill it, not summarized after the fact.

**Construction rules:**
1. Sync-before-async ordering: sync plugin steps first, async plugin steps second, automated flows third, instant flows fourth, scheduled flows fifth.
2. Every candidate from STEP 1 becomes either a YES row or a NO row. The denominator must close.
3. If a YES row's Side Effects column contains a field write that has automation potential, the Spawns cell MUST reference the next row number (Row #[N+1]) and that row MUST exist. If it does not: [CASCADE GAP: {trigger name} write not continued].
4. Use only terms from the STEP 0 Platform Term Contract. Any other term → [VOCAB FAIL: {term}].

**Trigger Map:**

| # | Trigger Name | Tier | Fires? | Condition | Reads | Produces | Side Effects | Spawns | Anomaly Flag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [name] | [tier from contract] | YES | [condition that must be true to fire] | [fields/payload consumed] | [primary output] | [notifications, record writes, API calls — or "none"] | Row #[N+1] / none | none / storm / cycle / missing |
| 2 | [name] | ... | YES | ... | ... | ... | ... | ... | ... |
| — | [non-firing candidate name] | — | NO | [why this candidate does not fire] | — | — | — | — | — |

**DENOMINATOR CLOSE:** After completing the map: (YES rows + NO rows) must equal N from STEP 1. Any candidate not present: [UNRESOLVED CANDIDATE: {name}].

**Inline annotation rules (apply throughout — do not defer to summary):**
- [VOCAB FAIL: {term}] — term not in STEP 0 contract used in any cell
- [INSUFFICIENT] — Reads, Produces, or Condition cell is empty for a YES row
- [CASCADE GAP: {trigger name}] — Spawns row reference exists but the referenced row is absent from the map
- [BARE ASSERTION: {verdict}] — verdict stated in STEP 3 without a preceding Evidence section
- [UNRESOLVED CANDIDATE: {name}] — STEP 1 candidate not present in map

---

**STEP 3 — ANOMALY INVESTIGATION CLOSURES**

Close all three investigations from the STEP 0 register. For each investigation:

**STORM INVESTIGATION**
EVIDENCE (cite specific row numbers and tier labels from the trigger map):
- [Row #, trigger name, observation — e.g., "Rows 2 and 3 are both automated flows that fire on the same Dataverse row-modified event with no filter differentiation"]
VERDICT: [STORM DETECTED / NOT DETECTED]
MITIGATION (required if STORM DETECTED):
- [specific actionable fix: debounce strategy / condition filter addition / flow consolidation / re-sequencing]
Register update: STATUS → CLOSED

**MISSING TRIGGER INVESTIGATION**
EVIDENCE (cite NO rows or gaps in the map):
- [Row — entries or UNRESOLVED CANDIDATE tags, e.g., "Expected CRM sync flow appears as a non-firing candidate because the connector trigger condition is not met"]
VERDICT: [MISSING TRIGGER DETECTED / NOT DETECTED]
MITIGATION (required if MISSING TRIGGER DETECTED):
- [specific fix: trigger registration / condition correction / flow creation]
Register update: STATUS → CLOSED

**CIRCULAR TRIGGER INVESTIGATION**
EVIDENCE (trace any Spawns chain that loops back — e.g., "Row 3 Spawns Row 4; Row 4 Spawns Row 3"):
- [chain trace or "No Spawns chain in the map closes back on a prior row"]
VERDICT: [CIRCULAR TRIGGER DETECTED / NOT DETECTED]
MITIGATION (required if CIRCULAR TRIGGER DETECTED):
- [specific fix: update-check flag / cycle-break condition / re-sequencing]
Register update: STATUS → CLOSED

Update the STEP 0 Anomaly Investigation Register with evidence citations, verdicts, and mitigations for all three rows.

---

## V-02 — Role Sequence: Three-Role Pipeline (Scanner → Enumerator → Auditor)

**Axis**: Role sequence
**Hypothesis**: Strict role segregation separates the denominator/governance work (Scanner) from trigger documentation (Enumerator) from map construction and verdict closure (Auditor). The Auditor cannot skip C-08 or C-15 because those are the Auditor's only job.

---

You are running a three-role pipeline for Power Automate / Copilot Studio trigger simulation. Execute each role in sequence. Roles have non-overlapping responsibilities — the Scanner does not enumerate trigger details; the Enumerator does not assess anomalies; the Auditor does not add new trigger entries.

**SCENARIO**

{SCENARIO_DESCRIPTION}

---

**ROLE A — SCANNER**

Job: Find candidates. Declare the denominator. Open anomaly investigations. Declare the platform term contract. Do NOT document trigger inputs, outputs, or conditions — that is Role B's job.

**A.1 — Anomaly Investigation Register**

Open all three slots now. These slots will be closed by Role C.

| Investigation | Status |
|---|---|
| STORM | OPEN |
| MISSING TRIGGER | OPEN |
| CIRCULAR TRIGGER | OPEN |

**A.2 — Platform Term Contract**

Declare all platform terms that Roles B and C are bound to use:

Execution tiers (exact labels only):
- sync plugin step
- async plugin step
- instant flow
- automated flow
- scheduled flow

Connector types relevant to this scenario:
- [list — e.g., "Dataverse connector trigger", "Office 365 Outlook connector"]

Any term used in Roles B or C not on this list is a vocabulary violation: [VOCAB FAIL: {term}].

**A.3 — Candidate Pre-Scan**

Scan all automation layers. List every automation that COULD fire for this change. Do not filter by conditions — list structural candidates.

Layers (scan in order):
1. Dataverse synchronous plugin steps
2. Dataverse asynchronous plugin steps
3. Power Automate automated flows (Dataverse connector trigger)
4. Power Automate instant flows
5. Power Automate scheduled flows
6. Copilot Studio topic triggers

| # | Candidate Name | Layer | Why It Is a Candidate |
|---|---|---|---|
| 1 | [name] | [layer] | [reason] |
| ... | | | |

**DENOMINATOR: [N] candidates identified.**

Role A is complete. Hand off to Role B with: candidate list (N items), platform term contract, anomaly register.

---

**ROLE B — ENUMERATOR**

Input from Role A: [N] candidates, platform term contract, anomaly register (all OPEN).
Job: Resolve every candidate — document inputs, outputs, side effects, cascade obligations. Do NOT assess anomaly verdicts — flag candidate anomalies and leave verdicts to Role C.

**Enumeration rules:**
1. Use ONLY terms from the Role A contract. Non-contract term → [VOCAB FAIL: {term}].
2. Sync-before-async ordering (sync plugin steps first).
3. Resolve all N candidates from Role A — each becomes a firing ENTRY or a NON-FIRING entry.
4. Cascade obligation: if a Side-effect writes cell names a field write that a subsequent automation candidate monitors, that automation MUST be the immediately following numbered ENTRY. If not continued: [CASCADE GAP: {trigger name} — write to {field} not continued as next entry].

For each firing candidate:

**ENTRY #[N] — [Trigger Name]**
- Tier: [Role A contract term]
- Condition (Taken): [specific condition that caused this trigger to fire]
- Condition (Skipped): [condition under which this trigger would NOT fire]
- Reads: [record field(s) or payload consumed — [INSUFFICIENT] if empty]
- Produces: [primary output action — [INSUFFICIENT] if empty]
- Side-effect writes: [downstream writes — e.g., "Creates Task record with Subject = 'Follow up'"; or "none confirmed"]
- Cascade: [if Side-effect writes has automation potential: MUST be ENTRY #[N+1] = {downstream trigger name}; else "none" or [CASCADE GAP: {name}]]
- Anomaly flag: [none / STORM CANDIDATE / CYCLE CANDIDATE / MISSING CANDIDATE — Role C renders verdict]

Non-firing candidates:

| Candidate # | Name | Layer | Reason Not Firing |
|---|---|---|---|
| [A-#] | [name] | [layer] | [condition not met / not registered / filtered out] |

**DENOMINATOR CLOSE:** (firing entries) + (non-firing entries) = [sum]. Must equal [N from Role A]. Any gap: [UNRESOLVED CANDIDATE: {name}].

Role B is complete. Hand off to Role C with: all ENTRY records, non-firing table, denominator close result.

---

**ROLE C — AUDITOR**

Input from Roles A and B: anomaly register, term contract, ENTRY records, non-firing table, denominator close.
Job: (1) Build the trigger map with tier and spawn columns. (2) Close all three anomaly investigations with evidence citations and remediations. (3) Verify denominator closure. Do NOT add new trigger entries.

**C.1 — Trigger Map**

Build from Role B ENTRY records.

| # | Trigger Name | Tier | Fires? | Spawns (row ref) | Anomaly Flag |
|---|---|---|---|---|---|
| [B entry #] | [name] | [Role A contract term] | YES/NO | Row #[ref] or none | none/storm/cycle/missing |

Column rules:
- Tier: use Role A contract labels only — [VOCAB FAIL: {term}] if not.
- Spawns: for any Role B ENTRY where Cascade = YES, reference the spawned entry's row number. If the referenced row is absent: [CASCADE GAP: {name}].
- Include non-firing candidates from Role B as NO rows.

**C.2 — Anomaly Investigation Closures**

Close each slot in the Role A anomaly register. For each:

[INVESTIGATION TYPE] CLOSURE
EVIDENCE (cite Role B entry numbers):
- [specific observation from Role B entries — e.g., "Entry #2 and Entry #3 both fire on the same Dataverse row-modified trigger with no filter differentiation"]
If no evidence cited: [BARE ASSERTION: {investigation type} — evidence block absent]
VERDICT: [DETECTED / NOT DETECTED]
MITIGATION (required if DETECTED):
- [specific actionable fix — debounce strategy / trigger registration / cycle-break condition]
Register status: CLOSED

**C.3 — Denominator Audit**

| | Count |
|---|---|
| Role A denominator | [N] |
| Role B firing entries | [count] |
| Role B non-firing entries | [count] |
| Total resolved | [sum] |
| Match | YES / GAP |

Any unresolved candidate: [UNRESOLVED CANDIDATE: {name}].

Role C is complete.

---

## V-03 — Phrasing Register: Extended Failure Mode Catalog (FM-01 through FM-11)

**Axis**: Phrasing register (SHALL/MUST language + named failure modes)
**Hypothesis**: V-05 in R2 used FM-01 through FM-09, achieving C-08/C-10/C-11/C-12/C-13 but missing C-09 (no trigger map). Adding FM-10 (trigger map deficiency) and FM-11 (missing denominator) closes the last two untagged defect classes and compels the model to produce both the map and the denominator as named failure-mode-avoidance obligations.

---

You are a Power Automate / Copilot Studio domain expert conducting a governed trigger simulation.

**SCENARIO**

{SCENARIO_DESCRIPTION}

---

**FAILURE MODE CATALOG**

Read and internalize all 11 failure modes before executing the protocol. Each failure mode names a defect that prior unguided analyses produced. Every protocol rule below prevents a named failure mode. When a failure mode is detected in the output, apply its tag inline — do not defer detection to a summary.

| FM | Name | What Goes Wrong | Inline Tag |
|---|---|---|---|
| FM-01 | Ad-Hoc Enumeration | Triggers listed without scanning all automation layers; candidates silently missed | [UNRESOLVED CANDIDATE: {name}] |
| FM-02 | Order Inversion | Async trigger listed before sync in the firing sequence; sequence is architecturally wrong | [ORDER INVERSION: entry #{N} is async but precedes sync entry #{M}] |
| FM-03 | Empty Entry Slot | Trigger entry has no Reads, or no Produces, or no Condition — analysis cannot be verified | [INSUFFICIENT: {entry name} missing {field}] |
| FM-04 | Anomaly Silence | One or more anomaly classes (storm / missing / circular) not addressed anywhere in the output | [ANOMALY SILENCE: {class} not assessed] |
| FM-05 | Dangling Side Effect | A side-effect field write with downstream automation potential is annotated but not continued as the next numbered entry | [CASCADE GAP: {trigger name} — write to {field} not continued] |
| FM-06 | Branch Blindness | Condition documented for taken path only; skipped path absent | [BRANCH BLIND: {entry name} — skipped condition absent] |
| FM-07 | Vocabulary Drift | Platform term used that was not in the declared term contract | [VOCAB FAIL: {term used}] |
| FM-08 | Post-Hoc Anomaly Assembly | Anomaly findings appear only in a closing section; no anomaly question slots opened before enumeration began | [POST-HOC: anomaly section appeared after enumeration without pre-opened slots] |
| FM-09 | Bare Verdict | Anomaly verdict stated without citing specific trigger entries as evidence | [BARE ASSERTION: {verdict type} — entry citations absent] |
| FM-10 | Trigger Map Deficiency | Trigger map present but missing execution-tier column, or Spawns column with row references, or both | [MAP DEFICIENCY: trigger map missing {tier column / spawns column / both}] |
| FM-11 | Missing Denominator | Trigger enumeration begins without first declaring the candidate count from a pre-scan | [MISSING DENOMINATOR: enumeration began before candidate count declared] |

---

**SECTION 0 — GOVERNANCE** *(prevents FM-07, FM-08)*

Declare before any analysis begins.

**Platform Term Contract** — use ONLY these terms throughout:

Execution tiers:
- sync plugin step
- async plugin step
- instant flow
- automated flow
- scheduled flow

Connector terms for this scenario (list relevant connectors): [e.g., "Dataverse connector — When a row is added, modified, or deleted"]

**Anomaly Investigation Register** — open all three slots NOW (prevents FM-08):

| Investigation | Status | Evidence Citation | Verdict | Mitigation |
|---|---|---|---|---|
| STORM | OPEN | — | — | — |
| MISSING TRIGGER | OPEN | — | — | — |
| CIRCULAR TRIGGER | OPEN | — | — | — |

FM-08 gate: All three slots are OPEN before any trigger entry exists. If Section 0 is absent or the slots appear after Section 1: [POST-HOC] applies to the entire analysis.

---

**SECTION 1 — CANDIDATE PRE-SCAN** *(prevents FM-01, FM-11)*

Scan all automation layers. List every automation that COULD fire. Do not apply condition filters — list structural candidates.

Layers (scan in order): Dataverse sync plugin steps → async plugin steps → Power Automate automated flows → instant flows → scheduled flows → Copilot Studio topic triggers.

| # | Candidate Name | Layer | Why It Is a Candidate |
|---|---|---|---|
| 1 | [name] | [layer] | [reason] |
| ... | | | |

**CANDIDATE DENOMINATOR: [N] candidates identified.**

FM-11 gate: If this denominator is absent, append [MISSING DENOMINATOR] to the first entry in Section 2 — FM-11 is active.

---

**SECTION 2 — TRIGGER ENUMERATION** *(prevents FM-02, FM-03, FM-05, FM-06, FM-07)*

Process all N candidates in sync-before-async order (FM-02). Use only contract terms (FM-07).

For each firing candidate:

**ENTRY #[N] — [Trigger Name]**
- Tier: [contract term — FM-07 if not from contract]
- Condition (Taken): [specific condition — FM-06 if absent]
- Condition (Skipped): [condition under which this would NOT fire — FM-06 if absent]
- Reads: [field(s) or payload — FM-03 if absent]
- Produces: [primary output — FM-03 if absent]
- Side-effect writes: [downstream writes, or "none confirmed"]
- Cascade continuation: [if Side-effect writes names a field that a candidate automation monitors: MUST produce ENTRY #[N+1] = {downstream trigger}. If not continued: [CASCADE GAP: {name}] — FM-05 active]
- Anomaly flag: [none / STORM / CYCLE / MISSING]

Non-firing candidates:

| Candidate # | Name | Layer | Reason Not Firing |
|---|---|---|---|

**DENOMINATOR CLOSURE CHECK:** (firing entries) + (non-firing entries) SHALL equal [N]. Any unresolved candidate: [UNRESOLVED CANDIDATE: {name}] — FM-01 active.

---

**SECTION 3 — PATHOLOGY ASSESSMENT** *(prevents FM-04, FM-08, FM-09)*

Close all three Section 0 investigations. For each:

**[INVESTIGATION TYPE] — [STORM / MISSING TRIGGER / CIRCULAR TRIGGER]**
EVIDENCE BLOCK (cite Section 2 entry numbers — FM-09 if absent):
- [entry name, entry number, specific observation]
- [or: "No evidence of this anomaly class found in Section 2 entries"]
If EVIDENCE BLOCK is absent before the verdict: [BARE ASSERTION: {investigation type} — FM-09 active]
VERDICT: [DETECTED / NOT DETECTED]
MITIGATION (required if DETECTED — absence when detected = structural gap in this block):
- [specific actionable fix: debounce / registration / cycle-break / re-sequencing]
Register update: STATUS → CLOSED

Update Section 0 register with evidence, verdict, and mitigation for all three rows.

---

**SECTION 4 — TRIGGER MAP** *(prevents FM-10)*

Build the trigger map from Section 2 entries. This map is a required output — its absence or deficiency is FM-10.

| # | Trigger Name | Tier | Fires? | Spawns (row ref) | Anomaly Flag |
|---|---|---|---|---|---|
| [Section 2 entry #] | [name] | [contract term] | YES/NO | Row #[ref] or none | none/storm/cycle/missing |

**Column requirements (FM-10 if missing):**
- Tier column: populated from contract terms only — [VOCAB FAIL: {term}] for deviations.
- Spawns column: for any entry where Cascade continuation = YES in Section 2, reference the spawned entry's row number. If referenced row absent: [CASCADE GAP: {name}].

FM-10 gate: After completing the map, verify: (a) Tier column present with contract labels, (b) Spawns column present with row references. If either is absent: [MAP DEFICIENCY: trigger map missing {tier column / spawns column}].

---

## V-04 — Lifecycle Emphasis: Phase Gate Model

**Axis**: Lifecycle emphasis (explicit acceptance gates between phases)
**Hypothesis**: Making C-14 a Phase 1 gate condition (Phase 2 cannot begin without a declared denominator) and C-15 an Appendix gate condition (Appendix cannot pass without tier and spawns columns) turns criteria into blocking preconditions rather than advisory requirements. Gate failure is structurally visible.

---

You are a Power Automate / Copilot Studio domain expert. Execute the trigger simulation protocol below using a phase gate model. Each phase has an acceptance gate. The next phase begins only when the current gate is met. If a gate fails, tag the failure inline and state why the gate failed before proceeding.

**SCENARIO**

{SCENARIO_DESCRIPTION}

---

**PHASE 0 — GOVERNANCE**
*Gate condition: Anomaly register has three OPEN slots AND term contract is declared.*

**Anomaly Investigation Register:**

| Investigation | Status | Gate |
|---|---|---|
| STORM | OPEN | [closes in Phase 3] |
| MISSING TRIGGER | OPEN | [closes in Phase 3] |
| CIRCULAR TRIGGER | OPEN | [closes in Phase 3] |

**Platform Term Contract** — use ONLY these terms in all phases:

Execution tiers:
- sync plugin step
- async plugin step
- instant flow
- automated flow
- scheduled flow

Connector terms for this scenario: [list relevant connectors]

**PHASE 0 GATE:** [PASS — register has 3 OPEN slots and contract is declared / FAIL — {describe what is missing}]

*Proceed to Phase 1 only if Phase 0 gate = PASS.*

---

**PHASE 1 — CANDIDATE SCAN**
*Gate condition: Candidate count N is explicitly stated before Phase 2 begins.*

Scan all automation layers for candidates that COULD fire. Do not filter by conditions here — list structural candidates only.

Layers (scan in order):
1. Dataverse synchronous plugin steps — fire before the record is committed
2. Dataverse asynchronous plugin steps — fire after commit, run in background
3. Power Automate automated flows (Dataverse connector trigger) — fire on Dataverse row events
4. Power Automate instant flows — fire on demand; include if scenario involves a manual component
5. Power Automate scheduled flows — fire on time; include only if this record change activates a schedule condition
6. Copilot Studio topic triggers — fire if a bot topic monitors Dataverse events

Candidate list:

| # | Candidate Name | Layer | Why It Is a Candidate |
|---|---|---|---|
| 1 | [name] | [layer] | [reason] |
| ... | | | |

**CANDIDATE COUNT: N = [number]**

**PHASE 1 GATE:** [PASS — N is declared / FAIL — [MISSING DENOMINATOR: no candidate count declared before Phase 2]]

*Proceed to Phase 2 only if Phase 1 gate = PASS.*

---

**PHASE 2 — TRIGGER ENUMERATION**
*Gate condition: All N candidates are resolved (firing or non-firing). (firing entries + non-firing entries) = N.*

**Enumeration rules:**
1. Sync-before-async ordering (sync plugin steps before automated flows before scheduled flows).
2. Use only Phase 0 contract terms — [VOCAB FAIL: {term}] for deviations.
3. If a Side-effect writes entry names a field that a subsequent candidate automation monitors, that automation MUST be the immediately following numbered entry. Non-continuation: [CASCADE GAP: {trigger name}].

For each firing candidate:

**ENTRY #[N] — [Trigger Name]**
- Tier: [Phase 0 contract term]
- Condition (Taken): [specific condition]
- Condition (Skipped): [condition under which this would NOT fire]
- Reads: [field(s) or payload — [INSUFFICIENT] if empty]
- Produces: [primary output — [INSUFFICIENT] if empty]
- Side-effect writes: [downstream writes, or "none"]
- Cascade: [if automation potential: MUST be ENTRY #[N+1] = {name}; else "none" or [CASCADE GAP]]

Non-firing candidates:

| # | Candidate Name | Layer | Reason Not Firing |
|---|---|---|---|

**PHASE 2 DENOMINATOR AUDIT:**

| | |
|---|---|
| N from Phase 1 | [N] |
| Firing entries | [count] |
| Non-firing entries | [count] |
| Total resolved | [sum] |

**PHASE 2 GATE:** [PASS — total = N / FAIL — [UNRESOLVED CANDIDATE: {name}] for each gap]

*Proceed to Phase 3 only if Phase 2 gate = PASS.*

---

**PHASE 3 — PATHOLOGY ASSESSMENT**
*Gate condition: All three Phase 0 anomaly slots are CLOSED with evidence citations, and any detected anomaly has a mitigation.*

For each investigation:

**STORM ASSESSMENT**
Evidence (cite Phase 2 entry numbers):
- [specific observations]
Verdict: [STORM DETECTED / NOT DETECTED]
Mitigation (required if DETECTED — absence = gate failure):
- [debounce strategy / condition filter / flow consolidation]
If verdict stated without evidence: [BARE ASSERTION: STORM verdict]
Register update: STATUS → CLOSED

**MISSING TRIGGER ASSESSMENT**
Evidence (cite Phase 2 non-firing entries or candidate gaps):
- [specific observations]
Verdict: [MISSING TRIGGER DETECTED / NOT DETECTED]
Mitigation (required if DETECTED):
- [registration fix / condition correction / flow creation]
If verdict stated without evidence: [BARE ASSERTION: MISSING TRIGGER verdict]
Register update: STATUS → CLOSED

**CIRCULAR TRIGGER ASSESSMENT**
Evidence (trace any Phase 2 Spawns chain that loops back):
- [chain trace or "No Spawns chain loops back"]
Verdict: [CIRCULAR TRIGGER DETECTED / NOT DETECTED]
Mitigation (required if DETECTED):
- [update-check flag / cycle-break condition / re-sequencing]
If verdict stated without evidence: [BARE ASSERTION: CIRCULAR TRIGGER verdict]
Register update: STATUS → CLOSED

**PHASE 3 GATE:** [PASS — all 3 slots CLOSED, evidence cited for each, mitigations present where required / FAIL — list unsatisfied conditions]

*Proceed to Appendix only if Phase 3 gate = PASS.*

---

**APPENDIX — TRIGGER MAP**
*Gate condition: Map includes execution-tier column with contract labels AND Spawns column with row references.*

| # | Trigger Name | Tier | Fires? | Spawns (row ref) | Anomaly Flag |
|---|---|---|---|---|---|
| [Phase 2 entry #] | [name] | [Phase 0 contract term] | YES/NO | Row #[N] or none | none/storm/cycle/missing |

Column requirements:
- Tier: Phase 0 contract terms only — [VOCAB FAIL: {term}] for deviations.
- Spawns: for any entry where Phase 2 Cascade = YES, reference the spawned entry's row number. If referenced row absent: [CASCADE GAP: {name}].

**APPENDIX GATE:** [PASS — Tier column present with contract terms AND Spawns column present with row references / FAIL — [MAP DEFICIENCY: missing {tier column / spawns column}]]

---

## V-05 — Inertia Framing: Status-Quo Override Protocol

**Axis**: Inertia framing
**Hypothesis**: When each structural requirement is introduced as an explicit override of a named default behavior — showing WHY the default fails before stating WHAT to do instead — the model acquires causal understanding rather than mechanical compliance. Causal understanding produces structurally robust output across all 15 criteria.

---

You are a Power Automate / Copilot Studio domain expert. You are running a trigger simulation that OVERRIDES six known failure patterns from unguided analysis. Each section below names the default behavior it replaces and explains why that default is insufficient.

**SCENARIO**

{SCENARIO_DESCRIPTION}

---

**SECTION 0 — ANOMALY REGISTER**

DEFAULT BEHAVIOR: Analyze triggers first, then note anomalies at the end.
WHY IT FAILS: Post-hoc anomaly checking is biased by the enumeration that preceded it. A class not mentally flagged during enumeration is silently skipped in a closing summary. An analyst who did not spot a storm during enumeration is unlikely to discover it by reviewing the list afterward.
OVERRIDE: Open all three anomaly investigation slots NOW — before any trigger work — so they function as live checklists, not retrospective additions.

| Investigation | Status | Evidence (fill during Section 2) | Verdict (fill in Section 3) | Mitigation (fill in Section 3) |
|---|---|---|---|---|
| STORM | OPEN | — | — | — |
| MISSING TRIGGER | OPEN | — | — | — |
| CIRCULAR TRIGGER | OPEN | — | — | — |

These slots are OPEN. Any analysis that answers anomaly questions only in a closing section — without having opened them here — is a post-hoc assembly defect: [POST-HOC: anomaly section appeared after enumeration without pre-opened slots].

---

**SECTION 1 — PLATFORM TERM CONTRACT**

DEFAULT BEHAVIOR: Use informal terms ("trigger," "webhook," "automation") interchangeably.
WHY IT FAILS: Informal vocabulary obscures execution architecture. Whether an automation is a sync plugin step or an automated flow determines: execution order (sync fires before the database commit; automated flows fire after), transaction scope (sync can roll back; automated flows cannot), retry behavior, and error surface. Blurring these makes the output unreliable for engineers diagnosing production incidents.
OVERRIDE: Declare exact terms before analysis. Any deviation is tagged inline.

Execution tiers (use ONLY these labels throughout):
- sync plugin step
- async plugin step
- instant flow
- automated flow
- scheduled flow

Connector terms for this scenario (list the specific connectors you will reference):
- [e.g., "Dataverse connector — When a row is added, modified, or deleted"]
- [e.g., "Office 365 Outlook connector — Send an email (V2)"]

Any term used in Sections 2–4 that is not on this list: [VOCAB FAIL: {term used}].

---

**SECTION 2 — CANDIDATE PRE-SCAN**

DEFAULT BEHAVIOR: Begin listing triggers immediately from memory or from "what flows exist."
WHY IT FAILS: Memory-first enumeration misses automation layers not immediately salient to the analyst. Dataverse plugin steps are routinely missed when the analyst starts from "what Power Automate flows are registered." Scheduled flows are missed when the analyst focuses on event-driven triggers only. Without a candidate list and a declared count, a reader cannot distinguish a thorough analysis from a partial one.
OVERRIDE: Scan each automation layer systematically. Declare the candidate count before enumeration begins. The count is the audit baseline.

Scan order (cover every layer before proceeding to Section 3):
1. Dataverse synchronous plugin steps — fire before database commit, in the same transaction
2. Dataverse asynchronous plugin steps — fire after commit, outside the transaction
3. Power Automate automated flows with a Dataverse connector trigger — fire on Dataverse row events
4. Power Automate instant flows — fire on demand; include if scenario has a manual trigger component
5. Power Automate scheduled flows — fire on time; include only if this record change satisfies a schedule condition
6. Copilot Studio topic triggers — fire if a bot topic is configured to respond to this Dataverse event

| # | Candidate Name | Layer | Why It Is a Candidate |
|---|---|---|---|
| 1 | [name] | [layer] | [reason] |
| ... | | | |

**CANDIDATE DENOMINATOR DECLARED: [N] candidates.**

This number is the audit baseline. Section 3 must resolve exactly N candidates. If (firing entries + non-firing entries) ≠ N, the gap is a completeness defect: [UNRESOLVED CANDIDATE: {name}] for each missing candidate.

---

**SECTION 3 — TRIGGER ENUMERATION**

DEFAULT BEHAVIOR: List trigger name and primary output. Leave side effects implicit.
WHY IT FAILS: Implicit side effects cannot be audited. A field write that a downstream flow monitors creates a trigger that the enumeration silently misses. The cascade gap is invisible because it was never recorded as a side effect in the first place. This is how a 3-trigger analysis becomes a 5-trigger production incident.
OVERRIDE: Explicit entry structure with cascade obligation. A side-effect field write with automation potential MUST spawn the immediately following numbered entry.

DEFAULT BEHAVIOR (secondary): Document only the condition under which a trigger fires.
WHY IT FAILS: A reader cannot predict when a trigger would NOT fire — they cannot distinguish "this trigger fired" from "this trigger always fires." Without the skipped branch, the analysis cannot support debugging or scenario variation.
OVERRIDE: Every condition slot requires both a Taken branch and a Skipped branch.

Enumeration rules:
- Sync-before-async ordering (FM-02 prevention: sync plugin steps before automated flows).
- Use ONLY Section 1 contract terms — [VOCAB FAIL: {term}] for any deviation.

For each candidate, produce a numbered entry:

**ENTRY #[N] — [Trigger Name]**
- Tier: [Section 1 contract term]
- Fires?: YES / NO (if NO, record in non-firing table below and do not number)
- Condition (Taken): [specific condition that caused this trigger to fire — field value, record state, role filter, connector event type]
- Condition (Skipped): [condition under which this trigger would NOT fire — e.g., "Does not fire when the initiating user is a system account"]
- Reads: [record field(s) or payload consumed by this trigger — [INSUFFICIENT] if empty]
- Produces: [primary output action — record update, email, queue message, API call — [INSUFFICIENT] if empty]
- Side-effect writes: [explicit list — e.g., "Creates Task record with Subject = 'Follow up'; sets CloseDate on parent Account"; or "none confirmed"]
- Cascade: [if any side-effect write is monitored by a subsequent automation candidate: MUST produce ENTRY #[N+1] naming that downstream automation. If the write's downstream automation is not the next entry: [CASCADE GAP: {this trigger's name} — write to {field} not continued as next entry]]
- Anomaly flag: [none / STORM / CYCLE / MISSING — update Section 0 register Evidence column when flagging]

Non-firing candidates:

| Candidate # | Name | Layer | Why Not Firing |
|---|---|---|---|

**DENOMINATOR CLOSE:** (firing entries) + (non-firing entries) = [sum]. Must equal [N from Section 2]. Any gap: [UNRESOLVED CANDIDATE: {name}].

---

**SECTION 4 — PATHOLOGY ASSESSMENT**

DEFAULT BEHAVIOR: State anomaly verdict based on overall impression — "No storm detected."
WHY IT FAILS: Impression-based verdicts cannot be audited. A verdict of "not detected" with no cited evidence could mean "not present" or "not checked." When a storm or circular trigger IS detected, an impression-based output leaves the engineer with a named problem but no path to resolution.
OVERRIDE: Evidence-before-verdict (EBV) protocol. Evidence block is required before every verdict. Mitigation is a required clause for any detected anomaly. An EBV block with no evidence is tagged as a bare assertion.

For each Section 0 investigation:

**[INVESTIGATION TYPE] — [STORM / MISSING TRIGGER / CIRCULAR TRIGGER]**
DEFAULT for this class (state what an unguided analyst would typically write):
- Storm: "No excessive triggers detected" — one line, no evidence
- Missing trigger: Often skipped entirely
- Circular trigger: "No circular dependencies" — one line, no evidence

EVIDENCE BLOCK (cite Section 3 entry numbers — [BARE ASSERTION: {investigation type} verdict] if block is absent):
- Entry #[N]: [relevant behavior or relationship — e.g., "Entry #2 and Entry #3 are both automated flows that fire on the same Dataverse row-modified event with no filter differentiation"]
- [additional observations or "No evidence of this anomaly class found in Section 3 entries"]
VERDICT: [DETECTED / NOT DETECTED]
MITIGATION (required if DETECTED — absence is a structural gap in this block, not an advisory omission):
- [specific actionable fix: debounce strategy / trigger registration / cycle-break condition / flow consolidation / re-sequencing]
Section 0 register update: STATUS → CLOSED

---

**SECTION 5 — TRIGGER MAP**

DEFAULT BEHAVIOR: Produce a name/order list or a simple table with trigger name and anomaly flag.
WHY IT FAILS: A name/order list cannot cross-validate platform grounding (are the tier labels correct?) or cascade completeness (do spawn references resolve to actual rows?). Without an execution-tier column, the map cannot verify whether sync and async ordering in Section 3 was correct. Without a Spawns column with row references, cascade chain completeness cannot be checked in one pass.
OVERRIDE: Trigger map with mandatory execution-tier column (cross-validates Section 1 contract) and mandatory Spawns column with row references (cross-validates Section 3 cascade obligations).

| # | Trigger Name | Tier | Fires? | Spawns (row ref) | Anomaly Flag |
|---|---|---|---|---|---|
| [Section 3 entry #] | [name] | [Section 1 contract term] | YES/NO | Row #[ref] / none | none/storm/cycle/missing |

Column rules:
- Tier: populated from Section 1 contract terms only — [VOCAB FAIL: {term}] if a non-contract label appears.
- Spawns: for any Section 3 entry where Cascade = YES, reference the spawned entry's row number. If that row number is absent from the map: [CASCADE GAP: {name}].
- Include non-firing candidates from Section 3 as NO rows.

Map completeness check: (YES rows + NO rows) = [N]. Any gap: [UNRESOLVED CANDIDATE: {name}].
