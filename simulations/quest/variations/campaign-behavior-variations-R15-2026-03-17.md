Written to `simulations/quest/variations/campaign-behavior-variations-R15-2026-03-17.md`.

---

## R15 Variations — Summary

**Baseline:** R14 V-05 (34/34 on v13 rubric, all three C-40/C-41/C-42 criteria integrated).

### Axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis: QL concurrent-boundary gate | Phase 4 combined tables cannot surface concurrent phase-boundary failures (re-entry collisions, recovery-path escalations, cross-phase races); a dedicated QL question forces that reasoning and may surface findings the table skips |
| V-02 | Inertia framing: HIGH-RISK tier + inertia-lead VERDICT | Labeling assumptions that are wide-blast-if-wrong AND uncovered by spec as HIGH-RISK, then opening VERDICT with them before findings, reframes the campaign from "what we found" to "what would have shipped unchallenged" |
| V-03 | Output format: compact two-row card blocks | 7-field numbered blocks require vertical scanning; pipe-separated two-row cards concentrate header fields horizontally at ~40% line count, enabling blast-radius comparison without scrolling — at risk of field compression pressure |
| V-04 | V-01 + V-02 | QL and HIGH-RISK tier are structurally independent; interaction watch at VERDICT if a QL finding and a HIGH-RISK assumption name the same component |
| V-05 | V-01 + V-02 + V-03 | Full integration; compact cards must accept "flow-lifecycle (QL)" as valid src: value; QL fires Q6 → QL → QH → EXECUTIVE SUMMARY |

### Structural notes

- **V-01 ordering:** Q6 → **QL** → QH → EXECUTIVE SUMMARY (VALIDITY RULES) → Q7 → CONSOLIDATE → Q8 → VERDICT. QL findings enter CONSOLIDATE as F-NN blocks tagged `src: flow-lifecycle (QL)`.
- **V-02 VERDICT:** Opens with "Inertia averted" paragraph listing all HIGH-RISK I-NN items before the top finding. Q5 gains risk-triage summary line.
- **V-03 cards:** Two-row format carries all 7 logical fields; Row 1 = 6 identification fields, Row 2 = 3 remediation sub-fields. Q8 audits the same dimensions across both rows.
- **V-05 interaction risk:** QL source tag `"flow-lifecycle (QL)"` must be recognized as valid in Q8's 7-field check. Tested explicitly in Q8 instructions.
dings that survive become
  F-NN blocks in CONSOLIDATE tagged `source: QL`.
- **V-02** modifies Q5 to assign a `HIGH-RISK` tier label to any assumption that is both (a)
  wide blast if wrong AND (b) has no covering spec clause. VERDICT opens with an "Inertia
  averted" paragraph naming the HIGH-RISK tier assumptions before the blast-radius ranking.
- **V-03** replaces the 7-field numbered block with a compact two-row card. Row 1 (header):
  `[F/M-NN] | [name] | [source] | blast:[tier] -> T-NN | sev:[h/m/l] | systemic:[y/n: phases] | [CONFIRMED|RUNTIME ANOMALY|isolated]`
  Row 2 (remediation): `  spec: [...] | contract: [...] | impl: [...]`
  Q8 audits the same seven dimensions across the two-row format.
- **V-05 interaction risk:** QL fires before QH; QH fires before EXECUTIVE SUMMARY. QL findings
  enter CONSOLIDATE as F-NN blocks. Compact card format must accommodate the QL source tag in
  the header row. Ordering: Q6 → QL → QH → EXECUTIVE SUMMARY (VALIDITY RULES) → Q7 →
  CONSOLIDATE → Q8 → VERDICT.

---

## V-01 — Lifecycle Emphasis: QL Concurrent-Boundary Gate
**Axis:** Phase 4 (flow-lifecycle) gains a dedicated calibration question `QL` that audits
concurrent phase-boundary edge cases: transitions that fire while the system is already
mid-transition to another lifecycle phase, recovery-path re-entry collisions, and exception
handlers that trigger a lifecycle change while the original exception is unresolved. QL fires
after Q6 and before QH.
**Hypothesis:** The combined nominal+exception table in Phase 4 evaluates each transition
independently; concurrent conditions (two transitions racing, recovery triggering a third
state) require cross-row reasoning that the table format does not prompt. QL forces that
reasoning explicitly. If QL surfaces no new findings above what the Phase 4 table already
captured, the table format is sufficient. If QL finds missed concurrent-boundary failures,
the gate is load-bearing and belongs in CONSOLIDATE as QL-sourced findings.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
Independent dimensions. Never merge. Report as separate labeled fields in every finding.

Propagation chain = the ordered sequence of Phase 0 census components through which a failure
travels from origin to terminal blast surface.
Format: [origin] -> [component-B] -> [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged: "unresolved chain -- registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
The Phase 0 registry is the single source of truth. No T-NN entry may be added, removed, or
renamed after Phase 0 is locked. Referenced in field 3 of every finding, in EXECUTIVE SUMMARY
bullets, and in chain-to-terminus tracing during Q1.

I-NN = inertia code. Assigned in Phase 0 to every assumption the team would carry into
implementation without this simulation. Inertia inventory is locked at Phase 0 close.

M-NN = meta-finding code. Assigned in Q5 to every I-NN inventory miss: an assumption a finding
overrides that was not declared in Phase 0. M-NN items receive 7-field treatment, are ranked
by blast radius in the META-FINDINGS section, and may appear in EXECUTIVE SUMMARY.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"

H-NN = hypothesis code. Assigned in Phase 0 to every expected finding pattern declared before
phases execute. QH audits outcomes: CONFIRMED, REFUTED, or NO-EVIDENCE.
Hypothesis inventory is locked at Phase 0 close. QH fires between QL and EXECUTIVE SUMMARY.

Remediation tier = the layer at which a fix must be applied.
  spec: add, amend, or clarify a specification clause.
  contract: revise a producer/consumer contract term or interface boundary.
  implementation: code, configuration, or deployment change.
Tiers are not mutually exclusive. At least one must be non-none.
All three sub-fields required in every finding block (F-NN and M-NN).

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state | downstream-caller | role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint. Every propagation chain must terminate
at a T-NN registry code. Chains that cannot resolve = registry miss.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1-5 must resolve to a T-NN entry or be flagged
"unresolved chain -- registry miss: [component name]."
State: "Registry locked: [N] terminus entries. Phase execution may begin."

**Inertia inventory:**

| I-NN | Assumption | Domain | What would happen if wrong |
|------|------------|--------|---------------------------|
| I-01 | [assumption text] | [state | permissions | contract | lifecycle | trigger] | [consequence] |
| ...  | ...        | ...    | ... |

Inertia inventory is now locked. Undeclared-assumption overrides will be assigned M-NN codes in Q5.
State: "Inertia inventory locked: [N] assumptions."

**Hypothesis inventory:**

| H-NN | Hypothesis | Target phase | Expected finding type | Expected blast radius |
|------|------------|-------------|----------------------|----------------------|
| H-01 | [expected finding pattern] | [phase name] | [type] | [wide | medium | narrow | unknown] |
| ...  | ...        | ...          | ...    | ... |

Hypothesis inventory is now locked. QH will audit outcomes after QL fires.
State: "Hypothesis inventory locked: [N] hypotheses. Simulation may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. Pre-classifies blast radius candidates from shared-state topology.
Downstream sub-skills inherit this map; none re-derive it independently.

**Nominal paths:**

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: blast radius candidate = wide. Classification locked for downstream phases.

**Exception paths:**

| Transition | Exception condition | Component that handles it | Blast radius if unhandled | Spec clause covering this? |
|------------|---------------------|---------------------------|--------------------------|---------------------------|

For any exception with no spec clause: spec gap.
For any unhandled wide exception: assign T-NN terminus, record blast radius candidate.

If no violations: "trace-state: clean -- all invariants verified, all exception paths handled."

EXIT CRITERIA: All state transitions and invariants evaluated (nominal and exception). No transitions deferred.
State: "trace-state complete: [N] transitions, [N] violations, [N] pre-classified wide, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Flow violations crossing a privilege
boundary are SYSTEMIC by definition; anchor must precede flow analysis.

**Nominal paths:**

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface + escalation path = wide (compound anchor hit).

**Exception paths:**

| Role-resource pair | Exception condition | Fail-open or fail-closed? | Blast radius if fail-open | Spec clause covering this? |
|--------------------|---------------------|--------------------------|--------------------------|---------------------------|

For any fail-open exception with no spec clause: spec gap.

If clean: "trace-permissions: clean -- all pairs verified, no escalation paths, all exceptions handled."

EXIT CRITERIA: All role-resource pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-permissions complete: [N] pairs, [N] escalation paths, [N] compound anchor hits, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 3 -- trace-contract

**Nominal paths:**

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match: CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].

**Exception paths:**

| Contract term | Exception condition | Recovery contract | Blast radius if recovery absent | Spec clause covering this? |
|---------------|---------------------|-------------------|---------------------------------|---------------------------|

For any exception with no recovery contract: spec gap. Wide + topology match = CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified, all exception paths handled."

EXIT CRITERIA: All producer/consumer pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 4 -- flow-lifecycle

**Nominal and exception paths (combined):**

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag: INIT, ACTIVE, SUSPENDED, TERMINAL, etc.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception sub-cases:**

| Lifecycle phase | Exception sub-case | Blast radius | Spec clause covering this? |
|-----------------|--------------------|--------------|---------------------------|

For each exception sub-case, record the triggering condition and which spec clause addresses it (or marks gap).

If clean: "flow-lifecycle: clean -- all transitions verified, all exception paths and sub-cases enumerated."

EXIT CRITERIA: All lifecycle phases and sub-cases evaluated. No phases deferred.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] sub-cases."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 5 -- flow-trigger

**Nominal paths:**

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception paths:**

| Trigger | Exception condition | Expected behavior | Actual behavior | Blast radius | Spec clause covering this? |
|---------|---------------------|-------------------|-----------------|--------------|---------------------------|

For any exception with no spec clause: spec gap.

If clean: "flow-trigger: clean -- all triggers verified, all exception paths enumerated."

EXIT CRITERIA: All triggers and activating events evaluated (nominal and exception). No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception paths."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## CALIBRATION BLOCK

Q1: Trace each finding's propagation chain to its T-NN terminus. Chain reaches Phase 0 shared-state
entry? Upgrade to wide. List all revisions and full chains. Flag unresolvable chains.

Q2: For each Phase 4-5 CONFIRMED finding: verify inline citation format.
"CONFIRMED -- evidence: [source-phase]: [matching-finding-name]." Revise any missing citation.
Also verify: for any finding entering EXECUTIVE SUMMARY as CONFIRMED, inline citation will be used.
List all reclassifications and citations verified or added.

Q3: For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [list]." Binary flags not valid.

Q4: For every finding involving Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any below-wide classification for a pre-classified component.

Q5: For each wide-blast-radius finding: name the I-NN assumption it overrides.
Format: "Finding [N] overrides I-[N]: [assumption text]."
Undeclared assumption override: assign M-NN code.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"
M-NN items rank in META-FINDINGS and may enter EXECUTIVE SUMMARY.

Q6: Did the anchor sequence deliver its pre-classification guarantee?
Zero revisions: "Anchor guarantee delivered."
Any revision: log as anchor violation -- name the finding, the downstream phase, and the Phase 1/2
classification that arrived too late.

QL: Audit Phase 4 (flow-lifecycle) specifically for concurrent phase-boundary edge cases.
For each lifecycle phase transition recorded in Phase 4, evaluate the following concurrent conditions:
1. Re-entry collision: can a transition fire while the system is still executing a prior transition
   for the same lifecycle phase? If yes: name both transitions, the overlapping state, and whether
   the spec addresses the collision.
2. Recovery-path escalation: does the exception handler for a failed transition itself trigger a
   lifecycle change? If yes: trace the secondary transition, its blast radius, and the T-NN it reaches.
3. Cross-phase race: can two lifecycle phase transitions fire simultaneously from different triggers?
   If yes: name the racing transitions, the shared state involved, and blast radius if both commit.
For each concurrent condition found: produce a finding candidate.
Format: "QL-[N]: [concurrent condition] -- phases involved: [list] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN] -- spec clause covering this: [clause or 'none -- spec gap']"
If no concurrent conditions found: "QL: clean -- no concurrent phase-boundary edge cases detected in Phase 4."
Any QL-[N] item with blast radius = wide and no spec clause: record as spec gap and carry forward as F-NN block in CONSOLIDATE with source tag "source: flow-lifecycle (QL)."
State: "QL audit complete: [N] concurrent conditions evaluated, [N] new findings surfaced."

QH: Audit the Phase 0 hypothesis inventory against all findings produced (F-NN and M-NN combined).
For each H-NN item, state one of:
- CONFIRMED: "H-[N] CONFIRMED -- finding [F/M-NN]: [finding name], phase [phase name]"
- REFUTED: "H-[N] REFUTED -- [what phases found instead of the expected pattern]"
- NO-EVIDENCE: "H-[N] NO-EVIDENCE -- target phase [name] produced no findings in the expected domain"
After all H-NN items:
"Hypothesis audit: [N] confirmed, [N] refuted, [N] no-evidence.
Refuted = well-specified behavior in predicted area.
No-evidence = campaign did not surface this domain; review exception path coverage before concluding clean."

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets from the combined F-NN and M-NN pool (including any QL-sourced findings),
ranked by blast radius. M-NN items may appear here; use prefix "M-[N]:" if so.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- [F-NN | M-NN]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY | meta-finding: I-NN inventory miss]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code (e.g., T-04), not a free-form component name.
   Free-form terminus = INVALID. Unresolvable = "unresolved chain -- registry miss: [name]" and exclude.
2. F-NN confirmation slot: CONFIRMED -- evidence: [source-phase]: [finding-name], or RUNTIME ANOMALY.
   Plain [CONFIRMED] token is NOT valid.
   M-NN confirmation slot: "meta-finding: I-NN inventory miss" -- no inline evidence citation required.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit each bullet:
- C-30 check: Chain terminus = T-NN code. Free-form: rewrite. Unresolvable: flag and exclude.
- C-31 check: F-NN = inline evidence format. M-NN = "meta-finding: I-NN inventory miss."
  Plain [CONFIRMED] without citation: rewrite via Q2 or reclassify RUNTIME ANOMALY.

State: "[F/M]-[N]: C-30 PASS (terminal: T-NN), C-31 PASS" or list revision.
All pass: "EXECUTIVE SUMMARY audit complete. Proceeding to CONSOLIDATE."

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY, (3) SYSTEMIC > isolated.
State whether any ties were encountered and how resolved.

**Ranked findings (wide first):**

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name — use "flow-lifecycle (QL)" for QL-sourced findings]
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [finding-name] | RUNTIME ANOMALY | isolated]
7. Remediation: spec: [clause to add/amend, or "none"] | contract: [term to revise, or "none"] | implementation: [change required, or "none"]
---

**META-FINDINGS (ranked by blast radius):**

---
**Meta-finding [M-N]**
1. Name: [undeclared assumption description]
2. Source: Q5 -- I-NN inventory miss
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [list] | no]
6. Classification: meta-finding -- I-NN inventory miss: assumption not declared in Phase 0
7. Remediation: spec: [add to I-NN inventory; add spec clause, or "none"] | contract: [term to revise, or "none"] | implementation: [guard to add, or "none"]
---

If no M-NN items: "META-FINDINGS: none -- all wide findings mapped to declared I-NN assumptions."

**Hypothesis outcomes:** [H-NN CONFIRMED: [N] | H-NN REFUTED: [N] | H-NN NO-EVIDENCE: [N]]
List each H-NN outcome in one line: "H-[N]: [CONFIRMED | REFUTED | NO-EVIDENCE] -- [summary]"

**Spec gaps:** [list each with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases and QL]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block (F-NN and M-NN).

For each block [N]:
- 7-field check: All seven fields present and non-empty. Missing = identify and state required.
- T-NN chain check: Field 3 terminates at T-NN code. Free-form = rewrite. Unresolvable = flag.
- Classification format check:
  F-NN: CONFIRMED inline format, RUNTIME ANOMALY, or isolated. Plain [CONFIRMED] = NOT valid.
  M-NN: "meta-finding -- I-NN inventory miss: assumption not declared in Phase 0."
- Remediation tier check: Field 7 has spec, contract, implementation sub-fields. Each populated
  or "none." At least one non-none. All-none = identify and state required tiers.

State: "[F/M]-[N]: 7-field PASS, T-NN PASS, classification PASS, remediation PASS (tiers: [list])"
or list revision made.
All pass: "CONSOLIDATE audit complete -- all [N] blocks satisfy 7-field, T-NN, classification,
and remediation-tier requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius (F-NN or M-NN, including any
QL-sourced concurrent-boundary finding) by its Phase 0 census component name.
State the propagation chain including T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [finding-name], RUNTIME ANOMALY, or meta-finding status.
If SYSTEMIC, list corroborating phases.
State the I-NN assumption the team would have carried into implementation (or M-NN if meta-finding).
Name the remediation tier(s) where the fix must land.
State H-NN outcomes: "Hypotheses: [N] confirmed, [N] refuted, [N] no-evidence."
State M-NN count: "Meta-findings: [N] undeclared assumptions surfaced."
Note QL contribution: "QL: [N] concurrent phase-boundary findings surfaced, [N] new spec gaps."
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-02 — Inertia Framing: VERDICT Inertia-Lead + Q5 Risk-Tier
**Axis:** Q5 gains a risk-tier classification: any assumption that is both (a) wide blast if wrong
AND (b) has no covering spec clause is labeled `HIGH-RISK`. VERDICT opens with an "Inertia
averted" paragraph naming all HIGH-RISK tier assumptions and the blast radius they would have
produced before naming the top finding by blast radius.
**Hypothesis:** VERDICT currently opens with the top finding, which frames the campaign result
as "what we found." Leading with HIGH-RISK inertia items instead frames it as "what would have
shipped unchallenged" — a stronger signal for engineering decisions. If the HIGH-RISK label adds
no new information beyond what VERDICT already names via I-NN codes, the axis is neutral. If
the explicit risk tier causes reviewers to act on inertia gaps they would otherwise have skipped,
the framing is load-bearing.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
Independent dimensions. Never merge. Report as separate labeled fields in every finding.

Propagation chain = the ordered sequence of Phase 0 census components through which a failure
travels from origin to terminal blast surface.
Format: [origin] -> [component-B] -> [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged: "unresolved chain -- registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
The Phase 0 registry is the single source of truth. No T-NN entry may be added, removed, or
renamed after Phase 0 is locked. Referenced in field 3 of every finding, in EXECUTIVE SUMMARY
bullets, and in chain-to-terminus tracing during Q1.

I-NN = inertia code. Assigned in Phase 0 to every assumption the team would carry into
implementation without this simulation. Inertia inventory is locked at Phase 0 close.

HIGH-RISK inertia assumption = an I-NN assumption satisfying both conditions:
  (a) "What would happen if wrong" column describes a wide blast radius outcome
  (b) No spec clause currently governs the assumption's domain
Assigned in Q5. Listed before findings in VERDICT.

M-NN = meta-finding code. Assigned in Q5 to every I-NN inventory miss: an assumption a finding
overrides that was not declared in Phase 0. M-NN items receive 7-field treatment, are ranked
by blast radius in the META-FINDINGS section, and may appear in EXECUTIVE SUMMARY.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"

H-NN = hypothesis code. Assigned in Phase 0 to every expected finding pattern declared before
phases execute. QH audits outcomes: CONFIRMED, REFUTED, or NO-EVIDENCE.
Hypothesis inventory is locked at Phase 0 close. QH fires between Q6 and EXECUTIVE SUMMARY.

Remediation tier = the layer at which a fix must be applied.
  spec: add, amend, or clarify a specification clause.
  contract: revise a producer/consumer contract term or interface boundary.
  implementation: code, configuration, or deployment change.
Tiers are not mutually exclusive. At least one must be non-none.
All three sub-fields required in every finding block (F-NN and M-NN).

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state | downstream-caller | role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint. Every propagation chain must terminate
at a T-NN registry code. Chains that cannot resolve = registry miss.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1-5 must resolve to a T-NN entry or be flagged
"unresolved chain -- registry miss: [component name]."
State: "Registry locked: [N] terminus entries. Phase execution may begin."

**Inertia inventory:**

| I-NN | Assumption | Domain | What would happen if wrong |
|------|------------|--------|---------------------------|
| I-01 | [assumption text] | [state | permissions | contract | lifecycle | trigger] | [consequence] |
| ...  | ...        | ...    | ... |

Inertia inventory is now locked. Undeclared-assumption overrides will be assigned M-NN codes in Q5.
State: "Inertia inventory locked: [N] assumptions."

**Hypothesis inventory:**

| H-NN | Hypothesis | Target phase | Expected finding type | Expected blast radius |
|------|------------|-------------|----------------------|----------------------|
| H-01 | [expected finding pattern] | [phase name] | [type] | [wide | medium | narrow | unknown] |
| ...  | ...        | ...          | ...    | ... |

Hypothesis inventory is now locked. QH will audit outcomes after Q6.
State: "Hypothesis inventory locked: [N] hypotheses. Simulation may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. Pre-classifies blast radius candidates from shared-state topology.
Downstream sub-skills inherit this map; none re-derive it independently.

**Nominal paths:**

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: blast radius candidate = wide. Classification locked for downstream phases.

**Exception paths:**

| Transition | Exception condition | Component that handles it | Blast radius if unhandled | Spec clause covering this? |
|------------|---------------------|---------------------------|--------------------------|---------------------------|

For any exception with no spec clause: spec gap.
For any unhandled wide exception: assign T-NN terminus, record blast radius candidate.

If no violations: "trace-state: clean -- all invariants verified, all exception paths handled."

EXIT CRITERIA: All state transitions and invariants evaluated (nominal and exception). No transitions deferred.
State: "trace-state complete: [N] transitions, [N] violations, [N] pre-classified wide, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Flow violations crossing a privilege
boundary are SYSTEMIC by definition; anchor must precede flow analysis.

**Nominal paths:**

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface + escalation path = wide (compound anchor hit).

**Exception paths:**

| Role-resource pair | Exception condition | Fail-open or fail-closed? | Blast radius if fail-open | Spec clause covering this? |
|--------------------|---------------------|--------------------------|--------------------------|---------------------------|

For any fail-open exception with no spec clause: spec gap.

If clean: "trace-permissions: clean -- all pairs verified, no escalation paths, all exceptions handled."

EXIT CRITERIA: All role-resource pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-permissions complete: [N] pairs, [N] escalation paths, [N] compound anchor hits, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 3 -- trace-contract

**Nominal paths:**

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match: CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].

**Exception paths:**

| Contract term | Exception condition | Recovery contract | Blast radius if recovery absent | Spec clause covering this? |
|---------------|---------------------|-------------------|---------------------------------|---------------------------|

For any exception with no recovery contract: spec gap. Wide + topology match = CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified, all exception paths handled."

EXIT CRITERIA: All producer/consumer pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 4 -- flow-lifecycle

**Nominal and exception paths (combined):**

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag: INIT, ACTIVE, SUSPENDED, TERMINAL, etc.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception sub-cases:**

| Lifecycle phase | Exception sub-case | Blast radius | Spec clause covering this? |
|-----------------|--------------------|--------------|---------------------------|

If clean: "flow-lifecycle: clean -- all transitions verified, all exception paths and sub-cases enumerated."

EXIT CRITERIA: All lifecycle phases and sub-cases evaluated. No phases deferred.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] sub-cases."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 5 -- flow-trigger

**Nominal paths:**

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception paths:**

| Trigger | Exception condition | Expected behavior | Actual behavior | Blast radius | Spec clause covering this? |
|---------|---------------------|-------------------|-----------------|--------------|---------------------------|

For any exception with no spec clause: spec gap.

If clean: "flow-trigger: clean -- all triggers verified, all exception paths enumerated."

EXIT CRITERIA: All triggers and activating events evaluated (nominal and exception). No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception paths."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## CALIBRATION BLOCK

Q1: Trace each finding's propagation chain to its T-NN terminus. Chain reaches Phase 0 shared-state
entry? Upgrade to wide. List all revisions and full chains. Flag unresolvable chains.

Q2: For each Phase 4-5 CONFIRMED finding: verify inline citation format.
"CONFIRMED -- evidence: [source-phase]: [matching-finding-name]." Revise any missing citation.
Also verify: for any finding entering EXECUTIVE SUMMARY as CONFIRMED, inline citation will be used.
List all reclassifications and citations verified or added.

Q3: For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [list]." Binary flags not valid.

Q4: For every finding involving Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any below-wide classification for a pre-classified component.

Q5: For each wide-blast-radius finding: name the I-NN assumption it overrides.
Format: "Finding [N] overrides I-[N]: [assumption text]."
Undeclared assumption override: assign M-NN code.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"
M-NN items rank in META-FINDINGS and may enter EXECUTIVE SUMMARY.

HIGH-RISK tier classification: For each I-NN assumption in the Phase 0 inventory, evaluate:
  (a) Does the "What would happen if wrong" column describe a wide blast radius outcome?
  (b) Is there no spec clause in the Phase 0 pre-declared contracts covering this assumption's domain?
If both (a) and (b): classify as HIGH-RISK.
Format: "I-[N] HIGH-RISK: [assumption text] -- wide blast if wrong, no spec coverage"
If no assumptions qualify: "No HIGH-RISK inertia assumptions -- all wide-blast assumptions have spec coverage."
State: "Inertia risk triage: [N] HIGH-RISK, [N] standard."

Q6: Did the anchor sequence deliver its pre-classification guarantee?
Zero revisions: "Anchor guarantee delivered."
Any revision: log as anchor violation -- name the finding, the downstream phase, and the Phase 1/2
classification that arrived too late.

QH: Audit the Phase 0 hypothesis inventory against all findings produced (F-NN and M-NN combined).
For each H-NN item, state one of:
- CONFIRMED: "H-[N] CONFIRMED -- finding [F/M-NN]: [finding name], phase [phase name]"
- REFUTED: "H-[N] REFUTED -- [what phases found instead of the expected pattern]"
- NO-EVIDENCE: "H-[N] NO-EVIDENCE -- target phase [name] produced no findings in the expected domain"
After all H-NN items:
"Hypothesis audit: [N] confirmed, [N] refuted, [N] no-evidence.
Refuted = well-specified behavior in predicted area.
No-evidence = campaign did not surface this domain; review exception path coverage before concluding clean."

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets from the combined F-NN and M-NN pool, ranked by blast radius.
M-NN items may appear here; use prefix "M-[N]:" if so.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- [F-NN | M-NN]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY | meta-finding: I-NN inventory miss]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code (e.g., T-04), not a free-form component name.
   Free-form terminus = INVALID. Unresolvable = "unresolved chain -- registry miss: [name]" and exclude.
2. F-NN confirmation slot: CONFIRMED -- evidence: [source-phase]: [finding-name], or RUNTIME ANOMALY.
   Plain [CONFIRMED] token is NOT valid.
   M-NN confirmation slot: "meta-finding: I-NN inventory miss" -- no inline evidence citation required.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit each bullet:
- C-30 check: Chain terminus = T-NN code. Free-form: rewrite. Unresolvable: flag and exclude.
- C-31 check: F-NN = inline evidence format. M-NN = "meta-finding: I-NN inventory miss."
  Plain [CONFIRMED] without citation: rewrite via Q2 or reclassify RUNTIME ANOMALY.

State: "[F/M]-[N]: C-30 PASS (terminal: T-NN), C-31 PASS" or list revision.
All pass: "EXECUTIVE SUMMARY audit complete. Proceeding to CONSOLIDATE."

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY, (3) SYSTEMIC > isolated.
State whether any ties were encountered and how resolved.

**Ranked findings (wide first):**

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name]
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [finding-name] | RUNTIME ANOMALY | isolated]
7. Remediation: spec: [clause to add/amend, or "none"] | contract: [term to revise, or "none"] | implementation: [change required, or "none"]
---

**META-FINDINGS (ranked by blast radius):**

---
**Meta-finding [M-N]**
1. Name: [undeclared assumption description]
2. Source: Q5 -- I-NN inventory miss
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [list] | no]
6. Classification: meta-finding -- I-NN inventory miss: assumption not declared in Phase 0
7. Remediation: spec: [add to I-NN inventory; add spec clause, or "none"] | contract: [term to revise, or "none"] | implementation: [guard to add, or "none"]
---

If no M-NN items: "META-FINDINGS: none -- all wide findings mapped to declared I-NN assumptions."

**Hypothesis outcomes:** [H-NN CONFIRMED: [N] | H-NN REFUTED: [N] | H-NN NO-EVIDENCE: [N]]
List each H-NN outcome in one line: "H-[N]: [CONFIRMED | REFUTED | NO-EVIDENCE] -- [summary]"

**Spec gaps:** [list each with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block (F-NN and M-NN).

For each block [N]:
- 7-field check: All seven fields present and non-empty. Missing = identify and state required.
- T-NN chain check: Field 3 terminates at T-NN code. Free-form = rewrite. Unresolvable = flag.
- Classification format check:
  F-NN: CONFIRMED inline format, RUNTIME ANOMALY, or isolated. Plain [CONFIRMED] = NOT valid.
  M-NN: "meta-finding -- I-NN inventory miss: assumption not declared in Phase 0."
- Remediation tier check: Field 7 has spec, contract, implementation sub-fields. Each populated
  or "none." At least one non-none. All-none = identify and state required tiers.

State: "[F/M]-[N]: 7-field PASS, T-NN PASS, classification PASS, remediation PASS (tiers: [list])"
or list revision made.
All pass: "CONSOLIDATE audit complete -- all [N] blocks satisfy 7-field, T-NN, classification,
and remediation-tier requirements. Proceeding to VERDICT."

---

## VERDICT

**Inertia averted:** Open with the HIGH-RISK inertia summary before naming any finding.
List each HIGH-RISK tier assumption from Q5 and the blast radius it would have produced if wrong:
"HIGH-RISK averted: I-[N] ([assumption text]) -- would have produced [tier] blast radius without this simulation."
If no HIGH-RISK assumptions were found: "No HIGH-RISK inertia -- all wide-blast assumptions had spec coverage."
State total count: "Inertia averted: [N] HIGH-RISK assumptions surfaced, [N] standard I-NN assumptions evaluated."

**Top finding:** Name the finding with the widest blast radius (F-NN or M-NN) by its Phase 0 census
component name. State the propagation chain including T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [finding-name], RUNTIME ANOMALY, or meta-finding status.
If SYSTEMIC, list corroborating phases.
Name the remediation tier(s) where the fix must land.
State H-NN outcomes: "Hypotheses: [N] confirmed, [N] refuted, [N] no-evidence."
State M-NN count: "Meta-findings: [N] undeclared assumptions surfaced."
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-03 — Output Format: Compact Two-Row Card Blocks
**Axis:** The 7-field numbered prose block in CONSOLIDATE is replaced with a compact two-row
card format. Row 1 (header card) carries six fields in pipe-separated format. Row 2 (remediation
card) carries the three-tier remediation sub-fields. Q8 audits the same seven dimensions across
the two-row representation. The EXECUTIVE SUMMARY format and phase table formats are unchanged.
**Hypothesis:** The 7-field numbered block is verbose; vertical scanning across N findings
requires readers to re-anchor at the numbered label each time. The two-row card concentrates
all identification fields on one line, enabling horizontal comparison of blast radius and
classification across findings without vertical scrolling. If compact cards produce identical
Q8 pass rates as 7-field blocks, the format is neutral. If cards are more frequently missing
fields (field 4 or 5 dropped under compression pressure), the verbose format is load-bearing.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
Independent dimensions. Never merge. Report as separate labeled fields in every finding.

Propagation chain = the ordered sequence of Phase 0 census components through which a failure
travels from origin to terminal blast surface.
Format: [origin] -> [component-B] -> [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged: "unresolved chain -- registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
The Phase 0 registry is the single source of truth. No T-NN entry may be added, removed, or
renamed after Phase 0 is locked. Referenced in finding card field 3 of every finding, in
EXECUTIVE SUMMARY bullets, and in chain-to-terminus tracing during Q1.

I-NN = inertia code. Assigned in Phase 0 to every assumption the team would carry into
implementation without this simulation. Inertia inventory is locked at Phase 0 close.

M-NN = meta-finding code. Assigned in Q5 to every I-NN inventory miss: an assumption a finding
overrides that was not declared in Phase 0. M-NN items receive the same two-row card treatment
as F-NN findings and are ranked by blast radius in the META-FINDINGS section.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"

H-NN = hypothesis code. Assigned in Phase 0 to every expected finding pattern declared before
phases execute. QH audits outcomes: CONFIRMED, REFUTED, or NO-EVIDENCE.
Hypothesis inventory is locked at Phase 0 close. QH fires between Q6 and EXECUTIVE SUMMARY.

Remediation tier = the layer at which a fix must be applied.
  spec: add, amend, or clarify a specification clause.
  contract: revise a producer/consumer contract term or interface boundary.
  implementation: code, configuration, or deployment change.
Tiers are not mutually exclusive. At least one must be non-none.
Both card rows (header + remediation) are required for every finding block (F-NN and M-NN).

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

Finding block format (two-row card):
Row 1 (header): `[F/M-NN] | [name] | src:[phase] | blast:[wide|med|narrow]->[T-NN] | sev:[h|m|l] | sys:[yes: phases / no] | [CONFIRMED -- evidence:[phase]:[finding] | RUNTIME ANOMALY | isolated | meta-finding: I-NN inventory miss]`
Row 2 (remediation): `  rem> spec:[...] | contract:[...] | impl:[...]`
Both rows required. Any missing field in Row 1 = incomplete card. Any missing sub-field in
Row 2 (including "none" for inapplicable tiers) = incomplete remediation card.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state | downstream-caller | role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint. Every propagation chain must terminate
at a T-NN registry code. Chains that cannot resolve = registry miss.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1-5 must resolve to a T-NN entry or be flagged
"unresolved chain -- registry miss: [component name]."
State: "Registry locked: [N] terminus entries. Phase execution may begin."

**Inertia inventory:**

| I-NN | Assumption | Domain | What would happen if wrong |
|------|------------|--------|---------------------------|
| I-01 | [assumption text] | [state | permissions | contract | lifecycle | trigger] | [consequence] |
| ...  | ...        | ...    | ... |

Inertia inventory is now locked. Undeclared-assumption overrides will be assigned M-NN codes in Q5.
State: "Inertia inventory locked: [N] assumptions."

**Hypothesis inventory:**

| H-NN | Hypothesis | Target phase | Expected finding type | Expected blast radius |
|------|------------|-------------|----------------------|----------------------|
| H-01 | [expected finding pattern] | [phase name] | [type] | [wide | medium | narrow | unknown] |
| ...  | ...        | ...          | ...    | ... |

Hypothesis inventory is now locked. QH will audit outcomes after Q6.
State: "Hypothesis inventory locked: [N] hypotheses. Simulation may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. Pre-classifies blast radius candidates from shared-state topology.
Downstream sub-skills inherit this map; none re-derive it independently.

**Nominal paths:**

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: blast radius candidate = wide. Classification locked for downstream phases.

**Exception paths:**

| Transition | Exception condition | Component that handles it | Blast radius if unhandled | Spec clause covering this? |
|------------|---------------------|---------------------------|--------------------------|---------------------------|

For any exception with no spec clause: spec gap.
For any unhandled wide exception: assign T-NN terminus, record blast radius candidate.

If no violations: "trace-state: clean -- all invariants verified, all exception paths handled."

EXIT CRITERIA: All state transitions and invariants evaluated (nominal and exception). No transitions deferred.
State: "trace-state complete: [N] transitions, [N] violations, [N] pre-classified wide, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Flow violations crossing a privilege
boundary are SYSTEMIC by definition; anchor must precede flow analysis.

**Nominal paths:**

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface + escalation path = wide (compound anchor hit).

**Exception paths:**

| Role-resource pair | Exception condition | Fail-open or fail-closed? | Blast radius if fail-open | Spec clause covering this? |
|--------------------|---------------------|--------------------------|--------------------------|---------------------------|

For any fail-open exception with no spec clause: spec gap.

If clean: "trace-permissions: clean -- all pairs verified, no escalation paths, all exceptions handled."

EXIT CRITERIA: All role-resource pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-permissions complete: [N] pairs, [N] escalation paths, [N] compound anchor hits, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 3 -- trace-contract

**Nominal paths:**

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match: CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].

**Exception paths:**

| Contract term | Exception condition | Recovery contract | Blast radius if recovery absent | Spec clause covering this? |
|---------------|---------------------|-------------------|---------------------------------|---------------------------|

For any exception with no recovery contract: spec gap. Wide + topology match = CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified, all exception paths handled."

EXIT CRITERIA: All producer/consumer pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 4 -- flow-lifecycle

**Nominal and exception paths (combined):**

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag: INIT, ACTIVE, SUSPENDED, TERMINAL, etc.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception sub-cases:**

| Lifecycle phase | Exception sub-case | Blast radius | Spec clause covering this? |
|-----------------|--------------------|--------------|---------------------------|

If clean: "flow-lifecycle: clean -- all transitions verified, all exception paths and sub-cases enumerated."

EXIT CRITERIA: All lifecycle phases and sub-cases evaluated. No phases deferred.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] sub-cases."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 5 -- flow-trigger

**Nominal paths:**

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception paths:**

| Trigger | Exception condition | Expected behavior | Actual behavior | Blast radius | Spec clause covering this? |
|---------|---------------------|-------------------|-----------------|--------------|---------------------------|

For any exception with no spec clause: spec gap.

If clean: "flow-trigger: clean -- all triggers verified, all exception paths enumerated."

EXIT CRITERIA: All triggers and activating events evaluated (nominal and exception). No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception paths."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## CALIBRATION BLOCK

Q1: Trace each finding's propagation chain to its T-NN terminus. Chain reaches Phase 0 shared-state
entry? Upgrade to wide. List all revisions and full chains. Flag unresolvable chains.

Q2: For each Phase 4-5 CONFIRMED finding: verify inline citation format.
"CONFIRMED -- evidence: [source-phase]: [matching-finding-name]." Revise any missing citation.
Also verify: for any finding entering EXECUTIVE SUMMARY as CONFIRMED, inline citation will be used.
List all reclassifications and citations verified or added.

Q3: For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [list]." Binary flags not valid.

Q4: For every finding involving Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any below-wide classification for a pre-classified component.

Q5: For each wide-blast-radius finding: name the I-NN assumption it overrides.
Format: "Finding [N] overrides I-[N]: [assumption text]."
Undeclared assumption override: assign M-NN code.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"
M-NN items rank in META-FINDINGS and may enter EXECUTIVE SUMMARY.

Q6: Did the anchor sequence deliver its pre-classification guarantee?
Zero revisions: "Anchor guarantee delivered."
Any revision: log as anchor violation -- name the finding, the downstream phase, and the Phase 1/2
classification that arrived too late.

QH: Audit the Phase 0 hypothesis inventory against all findings produced (F-NN and M-NN combined).
For each H-NN item, state one of:
- CONFIRMED: "H-[N] CONFIRMED -- finding [F/M-NN]: [finding name], phase [phase name]"
- REFUTED: "H-[N] REFUTED -- [what phases found instead of the expected pattern]"
- NO-EVIDENCE: "H-[N] NO-EVIDENCE -- target phase [name] produced no findings in the expected domain"
After all H-NN items:
"Hypothesis audit: [N] confirmed, [N] refuted, [N] no-evidence.
Refuted = well-specified behavior in predicted area.
No-evidence = campaign did not surface this domain; review exception path coverage before concluding clean."

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets from the combined F-NN and M-NN pool, ranked by blast radius.
M-NN items may appear here; use prefix "M-[N]:" if so.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- [F-NN | M-NN]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY | meta-finding: I-NN inventory miss]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code (e.g., T-04), not a free-form component name.
   Free-form terminus = INVALID. Unresolvable = "unresolved chain -- registry miss: [name]" and exclude.
2. F-NN confirmation slot: CONFIRMED -- evidence: [source-phase]: [finding-name], or RUNTIME ANOMALY.
   Plain [CONFIRMED] token is NOT valid.
   M-NN confirmation slot: "meta-finding: I-NN inventory miss" -- no inline evidence citation required.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit each bullet:
- C-30 check: Chain terminus = T-NN code. Free-form: rewrite. Unresolvable: flag and exclude.
- C-31 check: F-NN = inline evidence format. M-NN = "meta-finding: I-NN inventory miss."
  Plain [CONFIRMED] without citation: rewrite via Q2 or reclassify RUNTIME ANOMALY.

State: "[F/M]-[N]: C-30 PASS (terminal: T-NN), C-31 PASS" or list revision.
All pass: "EXECUTIVE SUMMARY audit complete. Proceeding to CONSOLIDATE."

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY, (3) SYSTEMIC > isolated.
State whether any ties were encountered and how resolved.

**Ranked findings (wide first):**

Use the compact two-row card format for every finding block:

`[F/M-NN] | [name] | src:[phase] | blast:[wide|med|narrow]->[T-NN] | sev:[h|m|l] | sys:[yes: phases / no] | [CONFIRMED -- evidence:[phase]:[finding] | RUNTIME ANOMALY | isolated | meta-finding: I-NN inventory miss]`
`  rem> spec:[clause or "none"] | contract:[term or "none"] | impl:[change or "none"]`

Every finding block requires both rows. A single-row card is incomplete and will fail Q8.
At least one rem> sub-field must be non-"none."

For META-FINDINGS (M-NN blocks), the Row 2 remediation card still requires all three
sub-fields: spec (add to I-NN inventory + clause), contract (if applicable), impl (guard if applicable).

If no M-NN items: "META-FINDINGS: none -- all wide findings mapped to declared I-NN assumptions."

**Hypothesis outcomes:** [H-NN CONFIRMED: [N] | H-NN REFUTED: [N] | H-NN NO-EVIDENCE: [N]]
List each H-NN outcome in one line: "H-[N]: [CONFIRMED | REFUTED | NO-EVIDENCE] -- [summary]"

**Spec gaps:** [list each with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding card (F-NN and M-NN).

For each card [N]:
- 7-field check: Row 1 contains all six header fields (finding code, name, source, blast radius
  with T-NN, severity, SYSTEMIC, classification). Row 2 contains all three remediation sub-fields.
  Missing any header field in Row 1 = incomplete. Missing any sub-field in Row 2 = incomplete.
- T-NN chain check: blast field in Row 1 terminates at T-NN code (e.g., blast:wide->T-04).
  Free-form terminus = rewrite. Unresolvable = flag.
- Classification format check:
  F-NN: CONFIRMED -- evidence: inline format, RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without citation = NOT valid.
  M-NN: "meta-finding: I-NN inventory miss" token in classification field.
- Remediation tier check: Row 2 rem> has spec, contract, impl each populated or "none."
  At least one non-none. All-none = identify and state required tiers.

State: "[F/M]-[N]: 7-field PASS, T-NN PASS, classification PASS, remediation PASS (tiers: [list])"
or list revision made.
All pass: "CONSOLIDATE audit complete -- all [N] cards satisfy 7-field, T-NN, classification,
and remediation-tier requirements. Proceeding to VERDICT."

---

## VERDICT

One paragraph. Name the finding with the widest blast radius (F-NN or M-NN) by its Phase 0 census
component name. State the propagation chain including T-NN terminus code.
State CONFIRMED -- evidence: [source-phase]: [finding-name], RUNTIME ANOMALY, or meta-finding status.
If SYSTEMIC, list corroborating phases.
State the I-NN assumption the team would have carried into implementation (or M-NN if meta-finding).
Name the remediation tier(s) where the fix must land.
State H-NN outcomes: "Hypotheses: [N] confirmed, [N] refuted, [N] no-evidence."
State M-NN count: "Meta-findings: [N] undeclared assumptions surfaced."
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-04 — V-01 + V-02: QL Gate + Inertia-Lead VERDICT
**Axis:** QL concurrent-boundary gate (V-01) combined with HIGH-RISK inertia tier and
inertia-lead VERDICT (V-02).
**Hypothesis:** QL and the HIGH-RISK tier are structurally orthogonal: QL operates on Phase 4
concurrent conditions and produces F-NN blocks; the HIGH-RISK tier operates on the Phase 0
I-NN inventory and produces Q5 risk labels. The only potential interaction is at VERDICT: both
axes contribute to the opening paragraph (QL findings may be the widest-blast finding; HIGH-RISK
tier may name the same I-NN assumption). If they name the same assumption from different angles,
VERDICT must cite both the QL finding and the I-NN risk tier without duplication.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
Independent dimensions. Never merge. Report as separate labeled fields in every finding.

Propagation chain = the ordered sequence of Phase 0 census components through which a failure
travels from origin to terminal blast surface.
Format: [origin] -> [component-B] -> [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged: "unresolved chain -- registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
The Phase 0 registry is the single source of truth. No T-NN entry may be added, removed, or
renamed after Phase 0 is locked. Referenced in field 3 of every finding, in EXECUTIVE SUMMARY
bullets, and in chain-to-terminus tracing during Q1.

I-NN = inertia code. Assigned in Phase 0 to every assumption the team would carry into
implementation without this simulation. Inertia inventory is locked at Phase 0 close.

HIGH-RISK inertia assumption = an I-NN assumption satisfying both conditions:
  (a) "What would happen if wrong" column describes a wide blast radius outcome
  (b) No spec clause currently governs the assumption's domain
Assigned in Q5. Listed before findings in VERDICT.

M-NN = meta-finding code. Assigned in Q5 to every I-NN inventory miss: an assumption a finding
overrides that was not declared in Phase 0. M-NN items receive 7-field treatment, are ranked
by blast radius in the META-FINDINGS section, and may appear in EXECUTIVE SUMMARY.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"

H-NN = hypothesis code. Assigned in Phase 0 to every expected finding pattern declared before
phases execute. QH audits outcomes: CONFIRMED, REFUTED, or NO-EVIDENCE.
Hypothesis inventory is locked at Phase 0 close. QH fires between QL and EXECUTIVE SUMMARY.

Remediation tier = the layer at which a fix must be applied.
  spec: add, amend, or clarify a specification clause.
  contract: revise a producer/consumer contract term or interface boundary.
  implementation: code, configuration, or deployment change.
Tiers are not mutually exclusive. At least one must be non-none.
All three sub-fields required in every finding block (F-NN and M-NN).

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state | downstream-caller | role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint. Every propagation chain must terminate
at a T-NN registry code. Chains that cannot resolve = registry miss.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1-5 must resolve to a T-NN entry or be flagged
"unresolved chain -- registry miss: [component name]."
State: "Registry locked: [N] terminus entries. Phase execution may begin."

**Inertia inventory:**

| I-NN | Assumption | Domain | What would happen if wrong |
|------|------------|--------|---------------------------|
| I-01 | [assumption text] | [state | permissions | contract | lifecycle | trigger] | [consequence] |
| ...  | ...        | ...    | ... |

Inertia inventory is now locked. Undeclared-assumption overrides will be assigned M-NN codes in Q5.
State: "Inertia inventory locked: [N] assumptions."

**Hypothesis inventory:**

| H-NN | Hypothesis | Target phase | Expected finding type | Expected blast radius |
|------|------------|-------------|----------------------|----------------------|
| H-01 | [expected finding pattern] | [phase name] | [type] | [wide | medium | narrow | unknown] |
| ...  | ...        | ...          | ...    | ... |

Hypothesis inventory is now locked. QH will audit outcomes after QL fires.
State: "Hypothesis inventory locked: [N] hypotheses. Simulation may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. Pre-classifies blast radius candidates from shared-state topology.
Downstream sub-skills inherit this map; none re-derive it independently.

**Nominal paths:**

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: blast radius candidate = wide. Classification locked for downstream phases.

**Exception paths:**

| Transition | Exception condition | Component that handles it | Blast radius if unhandled | Spec clause covering this? |
|------------|---------------------|---------------------------|--------------------------|---------------------------|

For any exception with no spec clause: spec gap.
For any unhandled wide exception: assign T-NN terminus, record blast radius candidate.

If no violations: "trace-state: clean -- all invariants verified, all exception paths handled."

EXIT CRITERIA: All state transitions and invariants evaluated (nominal and exception). No transitions deferred.
State: "trace-state complete: [N] transitions, [N] violations, [N] pre-classified wide, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Flow violations crossing a privilege
boundary are SYSTEMIC by definition; anchor must precede flow analysis.

**Nominal paths:**

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface + escalation path = wide (compound anchor hit).

**Exception paths:**

| Role-resource pair | Exception condition | Fail-open or fail-closed? | Blast radius if fail-open | Spec clause covering this? |
|--------------------|---------------------|--------------------------|--------------------------|---------------------------|

For any fail-open exception with no spec clause: spec gap.

If clean: "trace-permissions: clean -- all pairs verified, no escalation paths, all exceptions handled."

EXIT CRITERIA: All role-resource pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-permissions complete: [N] pairs, [N] escalation paths, [N] compound anchor hits, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 3 -- trace-contract

**Nominal paths:**

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match: CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].

**Exception paths:**

| Contract term | Exception condition | Recovery contract | Blast radius if recovery absent | Spec clause covering this? |
|---------------|---------------------|-------------------|---------------------------------|---------------------------|

For any exception with no recovery contract: spec gap. Wide + topology match = CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified, all exception paths handled."

EXIT CRITERIA: All producer/consumer pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 4 -- flow-lifecycle

**Nominal and exception paths (combined):**

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag: INIT, ACTIVE, SUSPENDED, TERMINAL, etc.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception sub-cases:**

| Lifecycle phase | Exception sub-case | Blast radius | Spec clause covering this? |
|-----------------|--------------------|--------------|---------------------------|

If clean: "flow-lifecycle: clean -- all transitions verified, all exception paths and sub-cases enumerated."

EXIT CRITERIA: All lifecycle phases and sub-cases evaluated. No phases deferred.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] sub-cases."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 5 -- flow-trigger

**Nominal paths:**

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception paths:**

| Trigger | Exception condition | Expected behavior | Actual behavior | Blast radius | Spec clause covering this? |
|---------|---------------------|-------------------|-----------------|--------------|---------------------------|

For any exception with no spec clause: spec gap.

If clean: "flow-trigger: clean -- all triggers verified, all exception paths enumerated."

EXIT CRITERIA: All triggers and activating events evaluated (nominal and exception). No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception paths."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## CALIBRATION BLOCK

Q1: Trace each finding's propagation chain to its T-NN terminus. Chain reaches Phase 0 shared-state
entry? Upgrade to wide. List all revisions and full chains. Flag unresolvable chains.

Q2: For each Phase 4-5 CONFIRMED finding: verify inline citation format.
"CONFIRMED -- evidence: [source-phase]: [matching-finding-name]." Revise any missing citation.
Also verify: for any finding entering EXECUTIVE SUMMARY as CONFIRMED, inline citation will be used.
List all reclassifications and citations verified or added.

Q3: For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [list]." Binary flags not valid.

Q4: For every finding involving Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any below-wide classification for a pre-classified component.

Q5: For each wide-blast-radius finding: name the I-NN assumption it overrides.
Format: "Finding [N] overrides I-[N]: [assumption text]."
Undeclared assumption override: assign M-NN code.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"
M-NN items rank in META-FINDINGS and may enter EXECUTIVE SUMMARY.

HIGH-RISK tier classification: For each I-NN assumption in the Phase 0 inventory, evaluate:
  (a) Does the "What would happen if wrong" column describe a wide blast radius outcome?
  (b) Is there no spec clause in the Phase 0 pre-declared contracts covering this assumption's domain?
If both (a) and (b): classify as HIGH-RISK.
Format: "I-[N] HIGH-RISK: [assumption text] -- wide blast if wrong, no spec coverage"
If no assumptions qualify: "No HIGH-RISK inertia assumptions -- all wide-blast assumptions have spec coverage."
State: "Inertia risk triage: [N] HIGH-RISK, [N] standard."

Q6: Did the anchor sequence deliver its pre-classification guarantee?
Zero revisions: "Anchor guarantee delivered."
Any revision: log as anchor violation.

QL: Audit Phase 4 (flow-lifecycle) for concurrent phase-boundary edge cases.
For each lifecycle phase transition, evaluate:
1. Re-entry collision: can a transition fire while executing a prior transition for the same phase?
2. Recovery-path escalation: does the exception handler itself trigger a lifecycle change?
3. Cross-phase race: can two lifecycle phase transitions fire simultaneously from different triggers?
For each concurrent condition found:
"QL-[N]: [concurrent condition] -- phases involved: [list] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN] -- spec clause covering this: [clause or 'none -- spec gap']"
If no concurrent conditions: "QL: clean -- no concurrent phase-boundary edge cases detected."
QL-[N] with wide blast and no spec clause: record as spec gap, carry as F-NN block
(source: "flow-lifecycle (QL)").
State: "QL audit complete: [N] concurrent conditions evaluated, [N] new findings surfaced."

QH: Audit the Phase 0 hypothesis inventory against all findings produced (F-NN and M-NN combined,
including QL-sourced findings).
For each H-NN item, state one of:
- CONFIRMED: "H-[N] CONFIRMED -- finding [F/M-NN]: [finding name], phase [phase name]"
- REFUTED: "H-[N] REFUTED -- [what phases found instead of the expected pattern]"
- NO-EVIDENCE: "H-[N] NO-EVIDENCE -- target phase [name] produced no findings in the expected domain"
After all H-NN items:
"Hypothesis audit: [N] confirmed, [N] refuted, [N] no-evidence.
Refuted = well-specified behavior in predicted area.
No-evidence = campaign did not surface this domain; review exception path coverage before concluding clean."

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets from the combined F-NN and M-NN pool (including QL-sourced findings),
ranked by blast radius. M-NN items may appear here; use prefix "M-[N]:" if so.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- [F-NN | M-NN]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY | meta-finding: I-NN inventory miss]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code (e.g., T-04), not a free-form component name.
   Free-form terminus = INVALID. Unresolvable = "unresolved chain -- registry miss: [name]" and exclude.
2. F-NN confirmation slot: CONFIRMED -- evidence: [source-phase]: [finding-name], or RUNTIME ANOMALY.
   Plain [CONFIRMED] token is NOT valid.
   M-NN confirmation slot: "meta-finding: I-NN inventory miss" -- no inline evidence citation required.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit each bullet:
- C-30 check: Chain terminus = T-NN code. Free-form: rewrite. Unresolvable: flag and exclude.
- C-31 check: F-NN = inline evidence format. M-NN = "meta-finding: I-NN inventory miss."
  Plain [CONFIRMED] without citation: rewrite via Q2 or reclassify RUNTIME ANOMALY.

State: "[F/M]-[N]: C-30 PASS (terminal: T-NN), C-31 PASS" or list revision.
All pass: "EXECUTIVE SUMMARY audit complete. Proceeding to CONSOLIDATE."

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY, (3) SYSTEMIC > isolated.
State whether any ties were encountered and how resolved.

**Ranked findings (wide first):**

---
**Finding [N]**
1. Name: [finding name or short description]
2. Source phase: [phase name -- use "flow-lifecycle (QL)" for QL-sourced findings]
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [list] | no]
6. Classification: [CONFIRMED -- evidence: [source-phase]: [finding-name] | RUNTIME ANOMALY | isolated]
7. Remediation: spec: [clause to add/amend, or "none"] | contract: [term to revise, or "none"] | implementation: [change required, or "none"]
---

**META-FINDINGS (ranked by blast radius):**

---
**Meta-finding [M-N]**
1. Name: [undeclared assumption description]
2. Source: Q5 -- I-NN inventory miss
3. Blast radius: [wide | medium | narrow] -- propagation chain: [origin] -> [component] -> [terminal: T-NN]
4. Severity at epicenter: [high | med | low]
5. SYSTEMIC: [yes -- phases: [list] | no]
6. Classification: meta-finding -- I-NN inventory miss: assumption not declared in Phase 0
7. Remediation: spec: [add to I-NN inventory; add spec clause, or "none"] | contract: [term to revise, or "none"] | implementation: [guard to add, or "none"]
---

If no M-NN items: "META-FINDINGS: none -- all wide findings mapped to declared I-NN assumptions."

**Hypothesis outcomes:** [H-NN CONFIRMED: [N] | H-NN REFUTED: [N] | H-NN NO-EVIDENCE: [N]]
List each H-NN outcome in one line: "H-[N]: [CONFIRMED | REFUTED | NO-EVIDENCE] -- [summary]"

**Spec gaps:** [list each with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases and QL]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding block (F-NN and M-NN).

For each block [N]:
- 7-field check: All seven fields present and non-empty. Missing = identify and state required.
- T-NN chain check: Field 3 terminates at T-NN code. Free-form = rewrite. Unresolvable = flag.
- Classification format check:
  F-NN: CONFIRMED inline format, RUNTIME ANOMALY, or isolated. Plain [CONFIRMED] = NOT valid.
  M-NN: "meta-finding -- I-NN inventory miss: assumption not declared in Phase 0."
- Remediation tier check: Field 7 has spec, contract, implementation sub-fields. Each populated
  or "none." At least one non-none. All-none = identify and state required tiers.

State: "[F/M]-[N]: 7-field PASS, T-NN PASS, classification PASS, remediation PASS (tiers: [list])"
or list revision made.
All pass: "CONSOLIDATE audit complete -- all [N] blocks satisfy 7-field, T-NN, classification,
and remediation-tier requirements. Proceeding to VERDICT."

---

## VERDICT

**Inertia averted:** List each HIGH-RISK tier assumption before naming any finding.
"HIGH-RISK averted: I-[N] ([assumption text]) -- would have produced [tier] blast radius without this simulation."
If no HIGH-RISK assumptions: "No HIGH-RISK inertia -- all wide-blast assumptions had spec coverage."
State: "Inertia averted: [N] HIGH-RISK assumptions surfaced, [N] standard I-NN assumptions evaluated."

**Top finding:** Name the finding with the widest blast radius (F-NN or M-NN, including
QL-sourced concurrent-boundary findings) by its Phase 0 census component name. State the
propagation chain including T-NN terminus code. State CONFIRMED evidence, RUNTIME ANOMALY,
or meta-finding status. If SYSTEMIC, list corroborating phases. Name remediation tier(s).
State H-NN outcomes: "Hypotheses: [N] confirmed, [N] refuted, [N] no-evidence."
State M-NN count: "Meta-findings: [N] undeclared assumptions surfaced."
Note QL contribution: "QL: [N] concurrent phase-boundary findings surfaced, [N] new spec gaps."
Conclude: proceed, proceed with conditions, or halt.
```

---

## V-05 — Full R15 Integration: V-01 + V-02 + V-03
**Axis:** All three R15 axes combined: QL concurrent-boundary gate (V-01), HIGH-RISK inertia
tier and inertia-lead VERDICT (V-02), and compact two-row card blocks (V-03).
**Hypothesis:** All three axes are structurally independent. V-01 adds QL between Q6 and QH.
V-02 modifies Q5 (risk tier) and VERDICT (inertia-lead). V-03 replaces finding block format
throughout CONSOLIDATE. The only integration risk: compact cards must carry QL-sourced findings
(which have the source tag "flow-lifecycle (QL)") and HIGH-RISK tier labels are surfaced in
VERDICT, not in the finding card format. These touch different parts of the output. If V-05
scores identically to V-01 + V-02 + V-03 individually, all three axes are composable.
Interaction watch: QL fires between Q6 and QH; QH fires between QL and EXECUTIVE SUMMARY.
Card format audit in Q8 must recognize "flow-lifecycle (QL)" as a valid source value in the
src: field of Row 1 cards.

```
Simulate the technical behavior of: {{topic}}

---

## DEFINITIONS

Blast radius = how broadly a failure propagates through the system.
Wide: corrupts shared state, breaks downstream callers, or blocks multiple user roles simultaneously.
Medium: two or more components affected; no shared state surface reached.
Narrow: failure contained within one component boundary.

Severity = damage depth at the epicenter (high / med / low).
Independent dimensions. Never merge. Report as separate labeled fields in every finding.

Propagation chain = the ordered sequence of Phase 0 census components through which a failure
travels from origin to terminal blast surface.
Format: [origin] -> [component-B] -> [terminal: T-NN]
The terminal must resolve to a T-NN entry in the Phase 0 terminus registry.
Chains that cannot resolve to a T-NN entry must be flagged: "unresolved chain -- registry miss."

T-NN = terminus registry code. Assigned in Phase 0 to every unique propagation chain endpoint
(shared state surface, downstream caller boundary, or role-boundary that terminates blast).
The Phase 0 registry is the single source of truth. No T-NN entry may be added, removed, or
renamed after Phase 0 is locked. Referenced in finding card Row 1, in EXECUTIVE SUMMARY bullets,
and in chain-to-terminus tracing during Q1.

I-NN = inertia code. Assigned in Phase 0 to every assumption the team would carry into
implementation without this simulation. Inertia inventory is locked at Phase 0 close.

HIGH-RISK inertia assumption = an I-NN assumption satisfying both:
  (a) "What would happen if wrong" describes a wide blast radius outcome
  (b) No spec clause governs the assumption's domain
Assigned in Q5. Listed before findings in VERDICT.

M-NN = meta-finding code. Assigned in Q5 to every I-NN inventory miss: an assumption a finding
overrides that was not declared in Phase 0. M-NN items receive the same two-row card treatment
as F-NN findings, are ranked by blast radius in the META-FINDINGS section, and may appear in
EXECUTIVE SUMMARY.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"

H-NN = hypothesis code. Assigned in Phase 0 to every expected finding pattern declared before
phases execute. QH audits outcomes: CONFIRMED, REFUTED, or NO-EVIDENCE.
Hypothesis inventory is locked at Phase 0 close. QH fires between QL and EXECUTIVE SUMMARY.

Remediation tier = the layer at which a fix must be applied.
  spec: add, amend, or clarify a specification clause.
  contract: revise a producer/consumer contract term or interface boundary.
  implementation: code, configuration, or deployment change.
Tiers are not mutually exclusive. At least one must be non-none.
Both card rows required for every finding block (F-NN and M-NN).

SYSTEMIC = a finding corroborated across three or more phases.
Required format: "SYSTEMIC: yes -- phases: [phase-name-1], [phase-name-2], [phase-name-3]"
Binary "SYSTEMIC: yes" without a phase list is not valid and will be rejected.

CONFIRMED = a Phase 4 or Phase 5 finding that matches a topology violation from Phases 1-3.
Required format: "CONFIRMED -- evidence: [source-phase]: [matching-finding-name]"
Omitting the evidence citation invalidates the CONFIRMED classification.

RUNTIME ANOMALY = a Phase 4 or Phase 5 finding with no matching topology violation in Phases 1-3.

Tiebreaker protocol:
1. Blast radius descending (wide > medium > narrow)
2. CONFIRMED > RUNTIME ANOMALY
3. SYSTEMIC > isolated
State this protocol before the consolidated ranking. If no ties exist, state that explicitly.

Finding block format (two-row card):
Row 1 (header): `[F/M-NN] | [name] | src:[phase] | blast:[wide|med|narrow]->[T-NN] | sev:[h|m|l] | sys:[yes: phases / no] | [CONFIRMED -- evidence:[phase]:[finding] | RUNTIME ANOMALY | isolated | meta-finding: I-NN inventory miss]`
Row 2 (remediation): `  rem> spec:[...] | contract:[...] | impl:[...]`
Valid src: values include "flow-lifecycle (QL)" for QL-sourced concurrent-boundary findings.
Both rows required. Any missing field in Row 1 = incomplete. Any missing sub-field in Row 2 = incomplete.
At least one rem> sub-field must be non-"none."

---

## PHASE 0 -- Topology census

Before any sub-skill runs, record the system vocabulary explicitly.

**Components in scope:** [every named service, module, API, schema, queue from the spec]

**Shared state surfaces:** [databases, caches, event buses, config objects read or written by
multiple components -- blast-radius amplifiers; any propagation chain reaching these = wide]

**Downstream callers:** [every component that depends on outputs from this system]

**Role-resource inventory:** [every role and the resources it may access]

**Pre-declared contracts:** [every producer/consumer contract term the spec commits to --
the CONFIRMED classification baseline for Phases 4-5]

**Terminus registry:**

| T-NN | Terminus component | Type |
|------|--------------------|------|
| T-01 | [component name]   | [shared-state | downstream-caller | role-boundary] |
| ...  | ...                | ... |

Assign a T-NN code to every unique blast-surface endpoint. Every propagation chain must terminate
at a T-NN registry code. Chains that cannot resolve = registry miss.

**Registry lock:** The terminus registry is now complete.
No terminus component may be added, removed, or renamed after this point.
All propagation chains in Phases 1-5 must resolve to a T-NN entry or be flagged
"unresolved chain -- registry miss: [component name]."
State: "Registry locked: [N] terminus entries. Phase execution may begin."

**Inertia inventory:**

| I-NN | Assumption | Domain | What would happen if wrong |
|------|------------|--------|---------------------------|
| I-01 | [assumption text] | [state | permissions | contract | lifecycle | trigger] | [consequence] |
| ...  | ...        | ...    | ... |

Inertia inventory is now locked. Undeclared-assumption overrides will be assigned M-NN codes in Q5.
State: "Inertia inventory locked: [N] assumptions."

**Hypothesis inventory:**

| H-NN | Hypothesis | Target phase | Expected finding type | Expected blast radius |
|------|------------|-------------|----------------------|----------------------|
| H-01 | [expected finding pattern] | [phase name] | [type] | [wide | medium | narrow | unknown] |
| ...  | ...        | ...          | ...    | ... |

Hypothesis inventory is now locked. QH will audit outcomes after QL fires.
State: "Hypothesis inventory locked: [N] hypotheses. Simulation may begin."

---

## PHASE 1 -- trace-state [ANCHOR: state topology pre-classifies blast radius candidates for all downstream phases]

trace-state runs first. Pre-classifies blast radius candidates from shared-state topology.
Downstream sub-skills inherit this map; none re-derive it independently.

**Nominal paths:**

| From state | To state | Trigger | Invariant | Invariant holds? | Shared state surface? | Blast radius candidate |
|------------|----------|---------|-----------|------------------|-----------------------|------------------------|

For each shared state surface = yes: blast radius candidate = wide. Classification locked for downstream phases.

**Exception paths:**

| Transition | Exception condition | Component that handles it | Blast radius if unhandled | Spec clause covering this? |
|------------|---------------------|---------------------------|--------------------------|---------------------------|

For any exception with no spec clause: spec gap.
For any unhandled wide exception: assign T-NN terminus, record blast radius candidate.

If no violations: "trace-state: clean -- all invariants verified, all exception paths handled."

EXIT CRITERIA: All state transitions and invariants evaluated (nominal and exception). No transitions deferred.
State: "trace-state complete: [N] transitions, [N] violations, [N] pre-classified wide, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 2 -- trace-permissions [ANCHOR: privilege boundary classification anchors flow blast radius assessment]

trace-permissions runs second, before all flow sub-skills. Flow violations crossing a privilege
boundary are SYSTEMIC by definition; anchor must precede flow analysis.

**Nominal paths:**

| Role | Resource | Action | Permitted? | Escalation path? | Phase 1 state surface involved? | Blast radius ceiling |
|------|----------|--------|------------|------------------|---------------------------------|----------------------|

Phase 1 state surface + escalation path = wide (compound anchor hit).

**Exception paths:**

| Role-resource pair | Exception condition | Fail-open or fail-closed? | Blast radius if fail-open | Spec clause covering this? |
|--------------------|---------------------|--------------------------|--------------------------|---------------------------|

For any fail-open exception with no spec clause: spec gap.

If clean: "trace-permissions: clean -- all pairs verified, no escalation paths, all exceptions handled."

EXIT CRITERIA: All role-resource pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-permissions complete: [N] pairs, [N] escalation paths, [N] compound anchor hits, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 3 -- trace-contract

**Nominal paths:**

| Producer | Consumer | Contract term | Expected | Actual | Mismatch? | Phase 1/2 topology match? |
|----------|----------|---------------|----------|--------|-----------|--------------------------|

Phase 1/2 topology match: CONFIRMED -- evidence: [phase-1|phase-2]: [matching-finding-name].

**Exception paths:**

| Contract term | Exception condition | Recovery contract | Blast radius if recovery absent | Spec clause covering this? |
|---------------|---------------------|-------------------|---------------------------------|---------------------------|

For any exception with no recovery contract: spec gap. Wide + topology match = CONFIRMED.

If clean: "trace-contract: clean -- all contracts verified, all exception paths handled."

EXIT CRITERIA: All producer/consumer pairs evaluated (nominal and exception). No pairs deferred.
State: "trace-contract complete: [N] pairs, [N] mismatches, [N] CONFIRMED, [N] exception paths, [N] exception spec gaps."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 4 -- flow-lifecycle

**Nominal and exception paths (combined):**

| Phase | Entry contract | Exit contract | Exception path | Exception handled? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|-------|----------------|---------------|----------------|--------------------|-----------|-----------------------------|

Phase tag: INIT, ACTIVE, SUSPENDED, TERMINAL, etc.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception sub-cases:**

| Lifecycle phase | Exception sub-case | Blast radius | Spec clause covering this? |
|-----------------|--------------------|--------------|---------------------------|

If clean: "flow-lifecycle: clean -- all transitions verified, all exception paths and sub-cases enumerated."

EXIT CRITERIA: All lifecycle phases and sub-cases evaluated. No phases deferred.
State: "flow-lifecycle complete: [N] phases, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] sub-cases."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## PHASE 5 -- flow-trigger

**Nominal paths:**

| Trigger | Expected fire order | Actual fire order | Race condition? | Phase 2 escalation role? | Phase tag | CONFIRMED / RUNTIME ANOMALY |
|---------|---------------------|-------------------|-----------------|--------------------------|-----------|------------------------------|

Phase 2 escalation role = yes: blast radius = wide.
CONFIRMED: CONFIRMED -- evidence: [source-phase]: [matching-finding-name]

**Exception paths:**

| Trigger | Exception condition | Expected behavior | Actual behavior | Blast radius | Spec clause covering this? |
|---------|---------------------|-------------------|-----------------|--------------|---------------------------|

For any exception with no spec clause: spec gap.

If clean: "flow-trigger: clean -- all triggers verified, all exception paths enumerated."

EXIT CRITERIA: All triggers and activating events evaluated (nominal and exception). No triggers deferred.
State: "flow-trigger complete: [N] triggers, [N] failures, [N] CONFIRMED, [N] RUNTIME ANOMALY, [N] exception paths."
T-NN resolution check: "[N] chains produced, [N] resolved to T-NN, [N] registry miss."
If any registry miss: flag and carry to Q1.

---

## CALIBRATION BLOCK

Q1: Trace each finding's propagation chain to its T-NN terminus. Chain reaches Phase 0 shared-state
entry? Upgrade to wide. List all revisions and full chains. Flag unresolvable chains.

Q2: For each Phase 4-5 CONFIRMED finding: verify inline citation format.
"CONFIRMED -- evidence: [source-phase]: [matching-finding-name]." Revise any missing citation.
Also verify: for any finding entering EXECUTIVE SUMMARY as CONFIRMED, inline citation will be used.
List all reclassifications and citations verified or added.

Q3: For every SYSTEMIC finding: "SYSTEMIC: yes -- phases: [list]." Binary flags not valid.

Q4: For every finding involving Phase 2 escalation role or Phase 1 state surface: verify wide.
Revise and explain any below-wide classification for a pre-classified component.

Q5: For each wide-blast-radius finding: name the I-NN assumption it overrides.
Format: "Finding [N] overrides I-[N]: [assumption text]."
Undeclared assumption override: assign M-NN code.
Format: "M-[N]: [undeclared assumption] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN]"
M-NN items rank in META-FINDINGS and may enter EXECUTIVE SUMMARY.

HIGH-RISK tier classification: For each I-NN assumption in the Phase 0 inventory, evaluate:
  (a) Does the "What would happen if wrong" column describe a wide blast radius outcome?
  (b) Is there no spec clause in the Phase 0 pre-declared contracts covering this assumption's domain?
If both (a) and (b): classify as HIGH-RISK.
Format: "I-[N] HIGH-RISK: [assumption text] -- wide blast if wrong, no spec coverage"
If no assumptions qualify: "No HIGH-RISK inertia assumptions -- all wide-blast assumptions have spec coverage."
State: "Inertia risk triage: [N] HIGH-RISK, [N] standard."

Q6: Did the anchor sequence deliver its pre-classification guarantee?
Zero revisions: "Anchor guarantee delivered."
Any revision: log as anchor violation.

QL: Audit Phase 4 (flow-lifecycle) for concurrent phase-boundary edge cases.
For each lifecycle phase transition, evaluate:
1. Re-entry collision: can a transition fire while executing a prior transition for the same phase?
2. Recovery-path escalation: does the exception handler itself trigger a lifecycle change?
3. Cross-phase race: can two lifecycle phase transitions fire simultaneously from different triggers?
For each concurrent condition found:
"QL-[N]: [concurrent condition] -- phases involved: [list] -- blast radius: [tier] -- chain: [origin] -> [terminal: T-NN] -- spec clause covering this: [clause or 'none -- spec gap']"
If no concurrent conditions: "QL: clean -- no concurrent phase-boundary edge cases detected."
QL-[N] with wide blast and no spec clause: record as spec gap, carry as F-NN block
(source: "flow-lifecycle (QL)").
State: "QL audit complete: [N] concurrent conditions evaluated, [N] new findings surfaced."

QH: Audit the Phase 0 hypothesis inventory against all findings produced (F-NN and M-NN combined,
including QL-sourced findings).
For each H-NN item, state one of:
- CONFIRMED: "H-[N] CONFIRMED -- finding [F/M-NN]: [finding name], phase [phase name]"
- REFUTED: "H-[N] REFUTED -- [what phases found instead of the expected pattern]"
- NO-EVIDENCE: "H-[N] NO-EVIDENCE -- target phase [name] produced no findings in the expected domain"
After all H-NN items:
"Hypothesis audit: [N] confirmed, [N] refuted, [N] no-evidence.
Refuted = well-specified behavior in predicted area.
No-evidence = campaign did not surface this domain; review exception path coverage before concluding clean."

---

## EXECUTIVE SUMMARY

Write exactly 3 bullets from the combined F-NN and M-NN pool (including QL-sourced findings),
ranked by blast radius. M-NN items may appear here; use prefix "M-[N]:" if so.
If fewer than 3 findings exist, write the available count and note the shortfall.

Use this format for each bullet exactly:
- [F-NN | M-NN]: [finding name] | blast-radius: [wide|medium|narrow] | chain: [origin] -> [component] -> [terminal: T-NN] | [CONFIRMED -- evidence: [phase]: [finding] | RUNTIME ANOMALY | meta-finding: I-NN inventory miss]

VALIDITY RULES for this section:
1. Chain terminus must use a T-NN code (e.g., T-04), not a free-form component name.
   Free-form terminus = INVALID. Unresolvable = "unresolved chain -- registry miss: [name]" and exclude.
2. F-NN confirmation slot: CONFIRMED -- evidence: [source-phase]: [finding-name], or RUNTIME ANOMALY.
   Plain [CONFIRMED] token is NOT valid.
   M-NN confirmation slot: "meta-finding: I-NN inventory miss" -- no inline evidence citation required.

Do not summarize. Do not add prose. Three structured bullets, then stop.

---

## Q7 -- EXECUTIVE SUMMARY structural audit

Before writing CONSOLIDATE, audit each bullet:
- C-30 check: Chain terminus = T-NN code. Free-form: rewrite. Unresolvable: flag and exclude.
- C-31 check: F-NN = inline evidence format. M-NN = "meta-finding: I-NN inventory miss."
  Plain [CONFIRMED] without citation: rewrite via Q2 or reclassify RUNTIME ANOMALY.

State: "[F/M]-[N]: C-30 PASS (terminal: T-NN), C-31 PASS" or list revision.
All pass: "EXECUTIVE SUMMARY audit complete. Proceeding to CONSOLIDATE."

---

## CONSOLIDATE

Write ONE report. Do not concatenate five phase outputs.

Tiebreaker: (1) Blast radius descending, (2) CONFIRMED > RUNTIME ANOMALY, (3) SYSTEMIC > isolated.
State whether any ties were encountered and how resolved.

**Ranked findings (wide first):**

Use the compact two-row card format for every finding block:

`[F/M-NN] | [name] | src:[phase] | blast:[wide|med|narrow]->[T-NN] | sev:[h|m|l] | sys:[yes: phases / no] | [CONFIRMED -- evidence:[phase]:[finding] | RUNTIME ANOMALY | isolated | meta-finding: I-NN inventory miss]`
`  rem> spec:[clause or "none"] | contract:[term or "none"] | impl:[change or "none"]`

Valid src: values: [phase name] or "flow-lifecycle (QL)" for QL-sourced concurrent-boundary findings.
Every finding block requires both rows. Single-row card = incomplete, will fail Q8.
At least one rem> sub-field must be non-"none."

For META-FINDINGS (M-NN blocks), apply the same two-row card format. Row 2 remediation card
requires all three sub-fields: spec (add to I-NN inventory + clause), contract (if applicable),
impl (guard if applicable).

If no M-NN items: "META-FINDINGS: none -- all wide findings mapped to declared I-NN assumptions."

**Hypothesis outcomes:** [H-NN CONFIRMED: [N] | H-NN REFUTED: [N] | H-NN NO-EVIDENCE: [N]]
List each H-NN outcome in one line: "H-[N]: [CONFIRMED | REFUTED | NO-EVIDENCE] -- [summary]"

**Spec gaps:** [list each with missing-clause citation, or "none detected"]

**Contract violations:** [list each with producer and consumer named, or "none detected"]

**Privilege escalation paths:** [list each, or "none detected"]

**Clean zones:** [Phase 0 census components with no findings across all five phases and QL]

---

## Q8 -- CONSOLIDATE finding block completeness gate

Before writing VERDICT, audit every finding card (F-NN and M-NN).

For each card [N]:
- 7-field check: Row 1 contains all six header fields (finding code, name, source, blast radius
  with T-NN, severity, SYSTEMIC, classification). Row 2 contains all three remediation sub-fields.
  Missing any header field in Row 1 = incomplete. Missing any sub-field in Row 2 = incomplete.
  "flow-lifecycle (QL)" is a valid source value for QL-sourced findings.
- T-NN chain check: blast field in Row 1 terminates at T-NN code (e.g., blast:wide->T-04).
  Free-form terminus = rewrite. Unresolvable = flag.
- Classification format check:
  F-NN: CONFIRMED -- evidence: inline format, RUNTIME ANOMALY, or isolated.
  Plain [CONFIRMED] without citation = NOT valid.
  M-NN: "meta-finding: I-NN inventory miss" token in classification field.
- Remediation tier check: Row 2 rem> has spec, contract, impl each populated or "none."
  At least one non-none. All-none = identify and state required tiers.

State: "[F/M]-[N]: 7-field PASS, T-NN PASS, classification PASS, remediation PASS (tiers: [list])"
or list revision made.
All pass: "CONSOLIDATE audit complete -- all [N] cards satisfy 7-field, T-NN, classification,
and remediation-tier requirements. Proceeding to VERDICT."

---

## VERDICT

**Inertia averted:** List each HIGH-RISK tier assumption before naming any finding.
"HIGH-RISK averted: I-[N] ([assumption text]) -- would have produced [tier] blast radius without this simulation."
If no HIGH-RISK assumptions: "No HIGH-RISK inertia -- all wide-blast assumptions had spec coverage."
State: "Inertia averted: [N] HIGH-RISK assumptions surfaced, [N] standard I-NN assumptions evaluated."

**Top finding:** Name the finding with the widest blast radius (F-NN or M-NN, including
QL-sourced concurrent-boundary findings) by its Phase 0 census component name. State the
propagation chain including T-NN terminus code. State CONFIRMED evidence, RUNTIME ANOMALY,
or meta-finding status. If SYSTEMIC, list corroborating phases. Name the I-NN assumption the
team would have carried (or M-NN if meta-finding). Name remediation tier(s) where fix must land.
State H-NN outcomes: "Hypotheses: [N] confirmed, [N] refuted, [N] no-evidence."
State M-NN count: "Meta-findings: [N] undeclared assumptions surfaced."
Note QL contribution: "QL: [N] concurrent phase-boundary findings surfaced, [N] new spec gaps."
Conclude: proceed, proceed with conditions, or halt.
```
