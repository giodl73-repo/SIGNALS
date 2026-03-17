# Flow-Resilience Skill — Round 11 Scoring (Rubric v11)

## Rubric Structure

| Tier | Criteria | Per-criterion | Tier max (uncapped) |
|------|----------|--------------|---------------------|
| Essential | C-01–C-05 | PASS=12, PARTIAL=6, FAIL=0 | 60 |
| Recommended | C-06–C-08 | PASS=10, PARTIAL=5, FAIL=0 | 30 |
| Aspirational | C-09–C-35 (27 criteria) | PASS=2, PARTIAL=1, FAIL=0 | 54 (capped 10) |

**Composite** = Essential + Recommended + min(Aspirational_uncapped, 10). Max = 100.

---

## Essential Criteria — All Variations

All five variations PASS all five essential criteria (C-01–C-05):
- **C-01** Coverage Accountability Roster commits ≥2 scenarios per class with DS Primitive for impossibility
- **C-02** Four-field Column Contract mandates State, Capability, Data at Risk, Recovery Path per row
- **C-03** Gate 3 typed gap sections (OEG + DCV + MRF) with typed nils and scope rationale
- **C-04** DS Primitive requirement for impossibility; BARRED-CG gate enforced; no invented protocols
- **C-05** ≥4 named commerce operations in Scope Declaration; RULE-COMMERCE-ANCHOR enforced

**Essential total: 60/60 for all variations.**

---

## Recommended Criteria — All Variations

All five variations PASS all three recommended criteria (C-06–C-08):
- **C-06** Severity (`degraded/impaired/down`) + blast radius (fraction/segment) both enforced by Column Contract
- **C-07** Recovery Path: mechanism with named actor required per stage; Gate 4 exit checks minimum two actor-labeled steps
- **C-08** DCV Conflict Resolution + Adequacy columns; RULE-CR-DCV fires on inadequate/undefined; emits DCV-CR-NN

**Recommended total: 30/30 for all variations.**

---

## Aspirational Criteria — Per-Variation Scoring

### C-09 — Chaos Engineering Test Cases (R11 target)

**Pass condition**: At least one runnable chaos scenario with (1) what to inject, (2) expected observable, (3) binary pass/fail signal.

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **PASS (2)** | Gate 2b dedicated gated phase (between Gate 2 and Gate 3): three columns — Inject (fault type + mechanism + parameter), Expected Observable (named in-fault behavior), Pass-Fail Signal (binary named artifact). Trigger Condition Reference links threshold expression from Gate 2. All three C-09 elements enforced by column contract and gate exit postconditions. |
| **V-02** | **FAIL (0)** | No Gate 2b or chaos engineering section. Observable Signal column added to Gate 3 addresses C-10, not C-09. Chaos entirely absent. |
| **V-03** | **PASS (2)** | Step 3 dedicated chaos test step: Trigger Condition Reference, Inject (fault type + mechanism + parameters with valid/invalid examples), Expected Observable (API/log/metric level), Pass-Fail Signal (binary named artifact with example). Done-when condition checks all four. |
| **V-04** | **PASS (2)** | Gate 6 (Chaos Engineering Specification) as dedicated Act 3 output. Four required fields: Trigger Condition Reference, Inject, Expected Observable (named granularity), Pass-Fail Signal (binary named artifact). RULE-CHAOS-INJECT enforces completeness; Gate 6 exit checks all per row. |
| **V-05** | **PASS (2)** | Gate 2b integrated in Act 1 with same structure as V-01, plus RULE-CHAOS-INJECT in Act 1 rule registry with bypass enforcement. Column Contract explicitly notes Gate 2b activation boundary is the same threshold expression as Trigger Condition — strongest enforcement. |

---

### C-10 — Observability Hooks Tied to Named Gaps (R11 target)

**Pass condition**: At least two observability recommendations linked to named gaps with rationale.

| Variation | Score | Evidence |
|-----------|-------|----------|
| **V-01** | **FAIL (0)** | No Observable Signal column. No observability section. Variation axis is chaos engineering only — observability entirely absent. |
| **V-02** | **PASS (2)** | Gate 3 OEG/DCV/MRF tables each have Observable Signal column: (1) named signal (metric/log/trace/alert), (2) rationale sentence. MRF-OBS-NN emitted when no signal exists. Gate 3 exit: "Every named finding has Observable Signal with named signal + rationale sentence." Multiple named-gap linkages enforced by column contract. |
| **V-03** | **PASS (2)** | Step 4 Observable Signal field required for every named finding: (1) named signal, (2) rationale sentence. MRF-OBS-NN emitted for unobservable gaps. Done-when condition checks every finding has Observable Signal with named signal + rationale. Same bidirectional linkage as V-02, conversational register. |
| **V-04** | **PASS (2)** | Gate 7 (Observability Manifest) dedicated Act 3 output. One row per named gap from Gate 3. Required fields: Observable Signal (named to observable granularity), Detection Horizon, Rationale. RULE-OBS-GAP enforces completeness; MRF-OBS-NN emitted for undetectable gaps. Gate 7 exit checks all per row. |
| **V-05** | **PASS (2)** | Gate 3 Observable Signal: three components — named signal, detection horizon, rationale sentence. RULE-OBS-GAP in Act 1 registry with bypass enforcement. MRF-OBS-NN emitted for undetectable gaps. Chaos-Observability Coverage Matrix cross-references observability coverage. Strongest enforcement with detection horizon. |

---

### Remaining Aspirational Criteria (C-11–C-35)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-11 Confidence-Annotated Catalog | 2 | 2 | 2 | 2 | 2 | Gate 1 Confidence Basis + Disposition; DS Primitive for Argued-Impossible; BARRED → CG-NN |
| C-12 Nil-Finding Norm | 2 | 2 | 2 | 2 | 2 | OEG-NIL-1/DCV-NIL-1/MRF-NIL-1 with scope rationale; Gate 3 exit verifies all three present |
| C-13 Coverage Accountability Roster | 2 | 2 | 2 | 2 | 2 | Pre-analysis table with ≥2 committed per class; DS Primitive for impossibility |
| C-14 Conflict-Resolution → DCV Source | 2 | 2 | 2 | 2 | 2 | Adequacy column in DCV; RULE-CR-DCV inline conditional; DCV-CR-NN emitted |
| **C-15 DS-Primitive Impossibility** | **1** | **1** | **1** | **1** | **1** | DS Primitive named and topic-scope rejection stated across all variations — but no inline VALID/INVALID annotated example block; PARTIAL across all rounds |
| C-16 Named Gate-State Vocabulary | 2 | 2 | 2 | 2 | 2 | Include/BARRED/Argued-Impossible; GATE N OPEN/CLOSED wrappers; reason-if-OPEN field |
| C-17 Permanently Barred → Coverage Gap | 2 | 2 | 2 | 2 | 2 | Gate 1b BARRED Resolution table; CG-NN emitted; Gate 1 exit verifies |
| C-18 Phase Entry + Exit Conditions | 2 | 2 | 2 | 2 | 2 | Every gate has Preconditions citing prior gate IDs + Exit postconditions checklist |
| C-19 Gate Blockage Transparency | 2 | 2 | 2 | 2 | 2 | `CLOSED / OPEN — [reason if open]` format on every gate |
| C-20 Downstream Gate Amendment | 2 | 2 | 2 | 2 | 2 | Gate 4 Amendment Pass table; RULE-NIL-SUPERSEDE; GATE N-bypass: AMENDED sub-gate labels |
| C-21 Pre-Analysis Scope Declaration | 2 | 2 | 2 | 2 | 2 | SCOPE DECLARATION block before Gate 1; ≥4 named operations; SCOPE DECLARATION COMPLETE |
| C-22 Typed Nil Identifiers | 2 | 2 | 2 | 2 | 2 | OEG-NIL-1/DCV-NIL-1/MRF-NIL-1 format shown inline |
| C-23 Scope Declaration Closure Bracket | 2 | 2 | 2 | 2 | 2 | SCOPE DECLARATION COMPLETE opening + terminal Scope Verification table |
| C-24 Template-Embedded Conditional Rules | 2 | 2 | 2 | 2 | 2 | V-01/V-02: 4 rules; V-04/V-05: 6 rules with RULE-CHAOS-INJECT + RULE-OBS-GAP |
| C-25 Nil Supersession Protocol | 2 | 2 | 2 | 2 | 2 | RULE-NIL-SUPERSEDE; Nil Supersession Log; `No supersessions` confirmation |
| C-26 Confidence Triage Resolution Sub-Gate | 2 | 2 | 2 | 2 | 2 | Gate 1b named labeled sub-gate; BARRED Resolution table; `no BARRED entries: Gate 1b: none` |
| C-27 Named Rule Block Registry | 2 | 2 | 2 | 2 | 2 | Discrete RULE REGISTRY section; unique IDs; trigger/action/bypass-owner columns |
| C-28 Post-Analysis Rule Registry Audit | 2 | 2 | 2 | 2 | 2 | Per-act audit tables with invocation status + BYPASS-TRIGGER column; REGISTRY AUDIT COMPLETE |
| C-29 Rule-Bypass Gate Reopening | 2 | 2 | 2 | 2 | 2 | 4-step protocol; amendment sub-gate label convention; COMPLETE blocked by unresolved RULE-BYPASSED |
| C-30 Multi-Act Completion Sign-Off | 2 | 2 | 2 | 2 | 2 | Per-act sign-off (gates CLOSED + scope exhausted + no RULE-BYPASSED); ANALYSIS COMPLETE gate |
| C-31 Pre-Analysis Bypass Chain Declaration | 2 | 2 | 2 | 2 | 2 | Named BYPASS GATE-REOPENING PROTOCOL before Gate 1; all four elements present |
| C-32 Bypass-Trigger Column Scanability | 2 | 2 | 2 | 2 | 2 | BYPASS-TRIGGER column in all registry audit tables; empty cell beside RULE-BYPASSED = audit failure |
| C-33 Intra-Row Column-Group Phase Gate | 2 | 2 | 2 | 2 | 2 | `C-phase complete check` advance-inhibitor embedded in each row descriptor |
| C-34 Trigger Condition: Threshold + Detection Signal | 2 | 2 | 2 | 2 | 2 | Two required components in Column Contract Fill Requirement; V-05 adds cross-reference to Gate 2b activation |
| C-35 Three-Component Recovery Stage | 2 | 2 | 2 | 2 | 2 | Mechanism + SLA target + VS per stage; VS named, observable, distinct from mechanism |

---

## Score Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| **Essential** (max 60) | 60 | 60 | 60 | 60 | 60 |
| **Recommended** (max 30) | 30 | 30 | 30 | 30 | 30 |
| **Aspirational uncapped** (max 54) | 51 | 51 | 53 | 53 | **54** |
| **Aspirational capped** (max 10) | 10 | 10 | 10 | 10 | 10 |
| **Composite** (max 100) | **100** | **100** | **100** | **100** | **100** |

---

## Tiebreak Ranking (Uncapped Aspirational)

| Rank | Variation | Uncapped | C-09 | C-10 | C-15 | Notes |
|------|-----------|----------|------|------|------|-------|
| 1 | **V-05** | **54/54** | PASS | PASS | PARTIAL | Full integration: Gate 2b + 6-rule registry + Chaos-Observability Coverage Matrix + Detection Horizon. New ceiling. |
| 2 (tie) | **V-03** | 53/54 | PASS | PASS | PARTIAL | Conversational register: Step 3 chaos + Step 4 observable signal. Both C-09 and C-10 cracked. |
| 2 (tie) | **V-04** | 53/54 | PASS | PASS | PARTIAL | Three-act structure: Gate 6 chaos + Gate 7 observability + Operational Readiness Declaration. Both cracked. |
| 4 (tie) | **V-01** | 51/54 | PASS | FAIL | PARTIAL | Gate 2b chaos only; C-10 uncracked. |
| 4 (tie) | **V-02** | 51/54 | FAIL | PASS | PARTIAL | Observable Signal column only; C-09 uncracked. |

**All composites 100/100.** R11 ceiling: **V-05 at 54/54 — first perfect uncapped score across all 27 criteria.**

---

## Persistent Uncracked Criterion

**C-15 (DS-Primitive Impossibility VALID/INVALID Examples)** — PARTIAL across all rounds. Every variation correctly states "topic-scope absence is not a DS Primitive" and requires naming a specific primitive, but none embeds an inline concrete example pair (e.g., `VALID: 'CAP theorem precludes strong consistency under partition' | INVALID: 'topic does not mention distributed caching'`). This annotated pair is the literal pass condition for C-15 and remains the single remaining structural gap.

---

## Excellence Signals (Potential C-36+)

### E-22 — Chaos Test Activation Threshold Linked to Gate 2 Trigger Condition

**Exhibited by**: V-01, V-03 (partially), V-04, V-05

Gate 2b's Trigger Condition Reference column cites — rather than independently invents — the threshold expression already required by the Gate 2 Column Contract. V-05 makes this explicit: *"The threshold expression is also used as the activation condition in Gate 2b."* A chaos test cannot fire at a different boundary than the monitoring spec for the same scenario.

**Gap closed**: C-09 requires the three chaos elements; C-34 requires the two Trigger Condition components. Neither requires that the chaos test activation be the same boundary as the monitoring spec. Without the link, a chaos test at "simulate 60s outage" diverges from an alert at "p99 > 500ms" — both valid by existing criteria, but not falsifying the same condition.

**Proposed C-36**: The chaos test Trigger Condition Reference must be a citation of the Gate 2 Trigger Condition threshold expression, not an independently invented value.

---

### E-23 — MRF-OBS-NN: Observability Absence as Named Missing Recovery Flow

**Exhibited by**: V-02, V-03, V-04, V-05

When a named gap has no known observable signal, instead of silently omitting the observability recommendation, these variations emit `MRF-OBS-NN` — a Missing Recovery Flow entry whose absent mechanism is "no production observability for [gap ID]." Treated as a first-class gap finding with Status-Quo Carrying Cost and Actionable Recommendation requirements.

**Gap closed**: C-10 requires observability recommendations when signals exist; C-12 handles nil findings for gap types. Neither requires that undetectability be named and costed as a recovery-flow deficiency. A gap the system cannot detect is one it cannot recover from — this makes that dependency structural.

**Proposed C-37**: When no observable signal exists for a named gap, emit MRF-OBS-NN in the MRF table as a first-class finding subject to Status-Quo Carrying Cost.

---

### E-24 — Chaos-Observability Coverage Matrix

**Exhibited by**: V-05 only

A terminal section in Act 1: one row per Include scenario, columns for Chaos Test Written? (with gate citation), Gap ID(s) Produced, Observable Signal Written? (with gate citation). Summary row counting scenarios with both, chaos-only, observable-only, neither.

**Gap closed**: C-09 and C-10 are independently satisfied per finding. No existing criterion requires joint coverage verification per scenario. A scenario is operationally ready only when it has *both* a chaos test and an observability hook for its gap(s) — the matrix makes that jointly verifiable in O(1).

**Proposed C-38**: A joint-coverage cross-reference table confirming chaos and observability coverage per scenario, with a summary statement quantifying scenarios achieving both.

---

### E-25 — Detection Horizon per Observable Signal

**Exhibited by**: V-04 (Gate 7), V-05 (Gate 3)

Each Observable Signal recommendation carries a Detection Horizon: "estimated time from gap onset to signal firing (e.g., `< 30s if sampled at 15s interval`; `session-scoped — fires at next cart load`)."

**Gap closed**: C-10 requires named signal + rationale. An alert firing in 15 seconds and one firing in 10 minutes both satisfy C-10 — but they are operationally different. The Detection Horizon makes the time-to-detection commitment explicit, enabling comparison with recovery SLA targets.

**Proposed C-39**: Each observability recommendation must carry an estimated time-to-detection expressed as a named time window relative to gap onset.

---

### E-26 — Operational Readiness Declaration Pre-Operational Act

**Exhibited by**: V-04 only

A `Pre-Act 3: Operational Readiness Declaration` block before Gate 6 (Chaos) and Gate 7 (Observability) open. Commits to: (1) chaos test coverage — one row per Include scenario with FS-IDs; (2) scenarios where chaos is architecturally impossible (DS Primitive required); (3) observability coverage — one signal per named gap; (4) gaps where signal is unknown (MRF-OBS-NN required). Closes with `OPERATIONAL READINESS DECLARATION COMPLETE`.

**Gap closed**: C-13 commits to scenario coverage before Gate 1; C-31 declares the bypass chain before Gate 1. No analogous declaration exists for operational coverage (chaos + observability). Without it, RULE-CHAOS-INJECT and RULE-OBS-GAP are the only enforcement, and those fire reactively on violations rather than committing coverage upfront.

**Proposed C-40**: Before the operational act (Gate 6 or equivalent) opens, a named Operational Readiness Declaration commits per-scenario chaos coverage and per-gap observability coverage, with impossibility provisions for each uncoverable item.

---

## Excellence Signal Summary

| Tag | Signal | Exhibited By | Proposed | Cracked by |
|-----|--------|-------------|----------|-----------|
| E-22 | Chaos threshold linked to Gate 2 Trigger Condition | V-01, V-03 (partial), V-04, V-05 | C-36 | V-01, V-05 |
| E-23 | MRF-OBS-NN: observability absence as named MRF finding | V-02, V-03, V-04, V-05 | C-37 | V-02, V-03, V-04, V-05 |
| E-24 | Chaos-Observability Coverage Matrix | V-05 | C-38 | V-05 |
| E-25 | Detection Horizon per Observable Signal | V-04, V-05 | C-39 | V-04, V-05 |
| E-26 | Operational Readiness Declaration pre-operational act | V-04 | C-40 | V-04 |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Chaos test activation threshold linked to Gate 2 Trigger Condition threshold expression — same boundary serves both test and alert (C-36)", "MRF-OBS-NN: observability absence as named first-class missing recovery flow with Status-Quo Carrying Cost (C-37)", "Chaos-Observability Coverage Matrix: joint per-scenario falsifiability view confirming both chaos test and observable signal present (C-38)", "Detection Horizon per Observable Signal: estimated time-to-detection making observability SLA comparable to recovery SLA targets (C-39)", "Operational Readiness Declaration pre-operational act: upfront per-scenario chaos coverage and per-gap observability coverage commitment before gates open, parallel to Coverage Accountability Roster (C-40)"]}
```
