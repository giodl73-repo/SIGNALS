## flow-lifecycle — Round 9 Scoring / Rubric v9

---

### Scoring Notes

All five variations are designed to achieve C-27 and C-28 as invariants and to demonstrate distinct implementations of the two new criteria (C-29 and C-30). All variations carry the complete 13-step schema (V-04/V-05 add Step 0). Evaluation proceeds criterion by criterion.

---

### V-01: Output Format — Threshold-Type Enumeration; Upstream Exception-Catalog Gate

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | State Trace table requires S-ID, State Name, Entry Trigger, Exit Trigger; schema mandates ≥6 rows |
| C-02 | PASS | Exception Catalog with Trigger, Divergence Phase/Step, Recovery/Terminal columns; ≥3 required |
| C-03 | PASS | Terminal Declaration distinguishes T-Type (S/F/C); every S-ID and E-ID must reach a named T-ID |
| C-04 | PASS | Bottleneck Register (cause + impact required) and Gap Register (missing step + consequence required) |
| C-05 | PASS | Role Registry requires domain-qualified names; Decision Table Owner R-ID column; no placeholders |
| C-06 | PASS | Parallel Path Modeling section with named join condition and join owner column |
| C-07 | PASS | Decision Table: D-ID, Decision Condition, Owner R-ID, Branch-Y, Branch-N, Branch-Fallback |
| C-08 | PASS | Edge Case Catalog: Scenario, Gap Reason, Consequence columns; ≥2 required |
| C-09 | PASS | Cross-Lifecycle Handoff table: Direction, Partner Lifecycle, Coupling State columns |
| C-10 | PASS | SLA Annotation table with ≥3 state rows; AT-RISK flag tied to Bottleneck Register reference |
| C-11 | PASS | Role Registry precedes State Trace; column definition includes "e.g., Senior Credit Analyst" concrete example |
| C-12 | PASS | Anti-pattern negation embedded in State Name column header: "generic placeholder is a fail" |
| C-13 | PASS | GATE A locks Phase Map before State Trace; references C-01 as the criterion protected |
| C-14 | PASS | Exception Coverage Audit table audits every S-ID and E-ID path against terminal list; per-path not count-based |
| C-15 | PASS | Branch-Fallback column in Decision Table covers role unavailable / system down / config missing |
| C-16 | PASS | Phase Map above State Trace; entry trigger, completion condition, SLA Envelope columns; phases aggregate ≥2 states |
| C-17 | PASS | Decision Condition column header requires measurable threshold; example cells show "Invoice > $50,000" |
| C-18 | PASS | Handler column header: "Must trace to role with Exception Handler = Y"; State Name header: "generic placeholder is a fail" |
| C-19 | PASS | Production gate names Scan Summary artifact and requires all rows CLOSED before write |
| C-20 | PASS | Gates at role registry (GATE A), phase table (GATE B), exception catalog upstream boundary (GATE C), and production (GATE P) — 4 distributed gates |
| C-21 | PASS | Handler (R-ID) column in Exception Catalog; all exception rows require a domain-qualified owner |
| C-22 | PASS | Production gate: "writing while any row shows OPEN is a structural fail" — inline failure declaration |
| C-23 | PASS | Exception Handler (Y/N) column in Role Registry; handler R-IDs in catalog must trace to Y-flagged roles |
| C-24 | PASS | Gate text: "artifact must be discarded and the scan rerun from SC-01" — remediation named inline |
| C-25 | PASS | Gate text: "produces an incomplete lifecycle trace where at least one path has no named terminal" — causal mechanism inline |
| C-26 | PASS | Handler column header: "Must trace to a role with Exception Handler = Y in the Role Registry" — inline backward-trace rule |
| C-27 | PASS | Scan Summary has Defect Type column; gate sentence references it by name; ≥5 named defect types |
| C-28 | PASS | Handler column header co-locates backward-trace rule AND "Mandatory; blank or uncertified role is a fail" |
| C-29 | PASS | Decision Condition header: "dollar amount, day count, retry count, percentage threshold" — enumeration of ≥2 threshold types at point of use |
| C-30 | PASS | GATE C: upstream boundary (state trace + decision table complete → exception catalog authorship begins) |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 22/22

```
score = (5/5 × 60) + (3/3 × 30) + (22/22 × 10) = 60 + 30 + 10 = 100
```

---

### V-02: Phrasing Register — Threshold-Type via Passing Example; Downstream Exception-Catalog Gate

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Same structural schema; imperative phrasing ("Write the state name") does not reduce coverage |
| C-02 | PASS | Exception Catalog identical structure; "List the triggering condition" covers all required fields |
| C-03 | PASS | Terminal Declaration identical; imperative phrasing ("Name the terminal state") enforces per-path completion |
| C-04 | PASS | Bottleneck Register and Gap Register preserved; imperative phrasing active throughout |
| C-05 | PASS | Role Registry identical; "Write a domain-qualified title" reinforces no-placeholder rule |
| C-06 | PASS | Parallel Path Modeling section present; imperative verbs throughout |
| C-07 | PASS | Decision Table identical; "Name the owner role" phrasing enforces ownership |
| C-08 | PASS | Edge Case Catalog identical; "Name the scenario" phrasing |
| C-09 | PASS | Cross-Lifecycle Handoff identical |
| C-10 | PASS | SLA Annotation identical; AT-RISK designation present |
| C-11 | PASS | Role Registry before State Trace; concrete domain-title example present |
| C-12 | PASS | Anti-pattern negation in schema headers; imperative register reinforces enforcement |
| C-13 | PASS | GATE A before State Trace protecting C-01; references criterion |
| C-14 | PASS | Exception Coverage Audit: per-path terminal verification present |
| C-15 | PASS | Branch-Fallback column; "Name the holding state or escalation path" imperative |
| C-16 | PASS | Phase Map above State Trace; all three required columns present |
| C-17 | PASS | Decision Condition cells require specific values; column header passing example is additive enforcement |
| C-18 | PASS | Handler column and State Name column both carry inline anti-pattern language |
| C-19 | PASS | Production gate with Scan Summary closure requirement |
| C-20 | PASS | Gates at role registry (GATE A), phase table (GATE B), exception catalog downstream boundary (GATE C), and production (GATE P) |
| C-21 | PASS | Handler (R-ID) column with domain-qualified R-ID requirement |
| C-22 | PASS | Production gate: inline failure declaration present |
| C-23 | PASS | Exception Handler (Y/N) column in Role Registry |
| C-24 | PASS | Remediation action inline in gate text |
| C-25 | PASS | Causal mechanism inline in gate text |
| C-26 | PASS | Handler column header: backward-trace rule inline |
| C-27 | PASS | Scan Summary Defect Type column; gate references by name; ≥5 defect categories |
| C-28 | PASS | Handler column header co-locates both rule and fail-declaration |
| C-29 | PASS | Decision Condition header: `(e.g., "Order value > $25,000")` — quoted passing example with comparison operator and unit at point of use |
| C-30 | PASS | GATE C: downstream boundary (exception catalog complete → terminal declaration authorship begins) — prevents forward-reference errors in terminal "Reached From" listings |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 22/22

```
score = (5/5 × 60) + (3/3 × 30) + (22/22 × 10) = 60 + 30 + 10 = 100
```

---

### V-03: Lifecycle Emphasis — Phase-First Framing; Both C-29 Mechanisms; Both C-30 Boundary Gates

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | State Trace is Step 3 (after Phase Map + Role Registry); entry/exit trigger columns intact |
| C-02 | PASS | Exception Catalog at Step 5; all three required fields present |
| C-03 | PASS | Terminal Declaration at Step 6; T-Type distinguishes success/failure terminals |
| C-04 | PASS | Bottleneck Register and Gap Register present; cause + impact + missing-step + consequence all required |
| C-05 | PASS | Role Registry at Step 2 requires domain-qualified names; each role declares Primary Phase |
| C-06 | PASS | Parallel Path Modeling step present |
| C-07 | PASS | Decision Table with all required columns including Branch-Fallback |
| C-08 | PASS | Edge Case Catalog with Scenario, Gap Reason, Consequence |
| C-09 | PASS | Cross-Lifecycle Handoff step present |
| C-10 | PASS | SLA Annotation step; Phase Map includes SLA Envelope column; SLA Risk Declaration block forces AT-RISK identification before state trace |
| C-11 | PASS | Phase Map (Step 1) names phases, not states; Role Registry (Step 2) fully establishes domain-qualified roles before State Trace (Step 3); concrete domain-title example present |
| C-12 | PASS | Anti-pattern language in schema headers; preamble-free design means all rules are at point of use |
| C-13 | PASS | GATE A protects hardest criterion (C-01) — state trace gated behind role registry completion |
| C-14 | PASS | Exception Coverage Audit: per-path confirmation step present |
| C-15 | PASS | Branch-Fallback column in Decision Table covers mechanism-level impairment |
| C-16 | PASS | Phase Map is Step 1 (first section); entry trigger, completion condition, SLA Envelope all required; phases aggregate ≥2 states; SLA Risk Declaration block names AT-RISK phases with causal bottleneck before any state is written — exceeds criterion |
| C-17 | PASS | Decision Condition cells require measurable thresholds; both C-29 mechanisms in column header reinforce |
| C-18 | PASS | Handler column and State Name column carry inline anti-pattern language |
| C-19 | PASS | Production gate with Scan Summary closure requirement present |
| C-20 | PASS | Gates at phase map (GATE A), role registry (GATE B), state trace/decisions upstream to exception catalog (GATE C), exception catalog downstream to terminals (GATE D), and production (GATE P) — 5 distributed gates |
| C-21 | PASS | Handler (R-ID) column with domain-qualified R-ID required |
| C-22 | PASS | Inline failure declaration in production gate |
| C-23 | PASS | Exception Handler (Y/N) in Role Registry; required per-row |
| C-24 | PASS | Remediation action inline in gate text |
| C-25 | PASS | Causal mechanism inline in gate text |
| C-26 | PASS | Handler column header carries backward-trace rule inline |
| C-27 | PASS | Scan Summary Defect Type column present; ≥5 named defect types; gate references column by name |
| C-28 | PASS | Handler column header co-locates both rule and fail-language |
| C-29 | PASS | Decision Condition header uses **both** mechanisms: enumeration of ≥2 threshold-type categories AND quoted passing example with comparison operator and unit |
| C-30 | PASS | GATE C guards upstream boundary (state trace + decisions → exception catalog); GATE D guards downstream boundary (exception catalog → terminal declarations) — both C-30 transitions covered |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 22/22

```
score = (5/5 × 60) + (3/3 × 30) + (22/22 × 10) = 60 + 30 + 10 = 100
```

---

### V-04: Role Sequence + Inertia Framing — Lifecycle-Class Derivation + AS-IS Baseline; Enumeration; Upstream Gate

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | State Trace intact; AS-IS scan (Step 0) documents current-state states separately, not as TO-BE |
| C-02 | PASS | Exception Catalog with AS-IS FM-ID column; Trigger, Divergence, Recovery/Terminal all required |
| C-03 | PASS | Terminal Declaration present; every path must reach a named T-ID |
| C-04 | PASS | Bottleneck Register (with AS-IS FM-ID column linking to Step 0 failure modes) + Gap Register (with AS-IS Gap-ID); cause + impact + missing-step all required — AS-IS anchor grounds identification beyond internal consistency |
| C-05 | PASS | Lifecycle Context Declaration seeds domain-qualified role vocabulary by class before any registry entry; no generic placeholders |
| C-06 | PASS | Parallel Path Modeling step present |
| C-07 | PASS | Decision Table present; domain-anchored threshold vocabulary from Lifecycle Context Declaration enriches Decision Condition cells |
| C-08 | PASS | Edge Case Catalog present |
| C-09 | PASS | Cross-Lifecycle Handoff step present |
| C-10 | PASS | SLA Annotation step present; AT-RISK designation present |
| C-11 | PASS | Role Registry precedes State Trace; Lifecycle Context Declaration provides domain-title vocabulary anchoring (e.g., "Senior Credit Analyst for L2O; Accounts Payable Clerk for P2P"); concrete domain-title examples present |
| C-12 | PASS | Anti-pattern language in schema headers |
| C-13 | PASS | Gate locks hardest criterion; references criterion |
| C-14 | PASS | Exception Coverage Audit per-path verification present |
| C-15 | PASS | Branch-Fallback column present |
| C-16 | PASS | Phase Map above State Trace; all required columns; SLA envelope present |
| C-17 | PASS | Decision Condition column header enumerates domain-class-specific threshold types; cells require specific measurable values |
| C-18 | PASS | Handler column and State Name column carry inline anti-pattern language |
| C-19 | PASS | Production gate with Scan Summary closure requirement |
| C-20 | PASS | Gates distributed across role registry, phase table, exception catalog upstream boundary (GATE C), and production — 4 gates |
| C-21 | PASS | Handler (R-ID) in Exception Catalog; domain-qualified; traces to Role Registry |
| C-22 | PASS | Inline failure declaration in gate text |
| C-23 | PASS | Exception Handler (Y/N) column in Role Registry |
| C-24 | PASS | Remediation action inline in gate text |
| C-25 | PASS | Causal mechanism inline in gate text |
| C-26 | PASS | Handler column header backward-trace rule inline |
| C-27 | PASS | Scan Summary Defect Type column; ≥5 defect types including "unanchored lifecycle" as V-04-specific entry; gate references column by name |
| C-28 | PASS | Handler column header co-locates both rule and fail-language |
| C-29 | PASS | Decision Condition header enumerates threshold types anchored to declared lifecycle class (e.g., P2P: "invoice amount, payment terms day count, receipt variance percentage"); domain vocabulary from Lifecycle Context Declaration operationalizes the requirement in class-specific terms |
| C-30 | PASS | GATE C: upstream boundary (state trace + decision table → exception catalog); single gate satisfies criterion minimum |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 22/22

```
score = (5/5 × 60) + (3/3 × 30) + (22/22 × 10) = 60 + 30 + 10 = 100
```

---

### V-05: All Axes Combined — Phase-First + Lifecycle-Class Derivation + AS-IS Anchor + Maximum Schema Density + Both C-29 Mechanisms + Both C-30 Gates

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | State Trace at Step 3; entry/exit trigger columns required; minimum 6 states enforced |
| C-02 | PASS | Exception Catalog at Step 5 with Trigger, Divergence Phase/Step, Recovery/Terminal, Handler R-ID, AS-IS FM-ID |
| C-03 | PASS | Terminal Declaration at Step 6; T-Type required; GATE D enforces exception catalog completeness before authorship begins |
| C-04 | PASS | Bottleneck Register (AS-IS FM-ID column) and Gap Register (AS-IS Gap-ID column) ground ≥2 bottlenecks and ≥1 gap in Step 0 observed failure modes |
| C-05 | PASS | Lifecycle Context Declaration seeds vocabulary; Role Registry requires domain-qualified names tracing to ≥1 Phase in Step 1 |
| C-06 | PASS | Parallel Path Modeling present; maximum schema density enforces join condition and join owner inline |
| C-07 | PASS | Decision Table with all required columns; imperative phrasing throughout |
| C-08 | PASS | Edge Case Catalog present |
| C-09 | PASS | Cross-Lifecycle Handoff present |
| C-10 | PASS | Phase Map (Step 1) requires SLA Envelope column and SLA Risk Declaration block that forces AT-RISK phase identification before Step 2; SLA Annotations (Step 8) with state-level timing |
| C-11 | PASS | Phase Map → Role Registry → State Trace ordering; roles established (and phase-linked) before any state is named; Lifecycle Context Declaration provides concrete domain-title examples by class |
| C-12 | PASS | Anti-pattern language in schema column headers throughout; no standalone preamble blocks |
| C-13 | PASS | GATE A locks phase map → role registry; references C-11 as protected criterion |
| C-14 | PASS | Scan Summary SC-05 performs per-path terminal verification (all S-IDs and E-IDs reach named T-IDs) |
| C-15 | PASS | Branch-Fallback column in Decision Table; imperative: "Name the holding state or escalation path" |
| C-16 | PASS | Phase Map is Step 1 (first schema section); SLA Envelope column required; SLA Risk Declaration block identifies AT-RISK phases with causal bottleneck before role registry is populated; ≥3 phases aggregating ≥2 states required |
| C-17 | PASS | Decision Condition cells require specific values; Lifecycle Context Declaration provides class-specific threshold vocabulary; both C-29 mechanisms in column header enforce type at definition |
| C-18 | PASS | Handler column header, State Name column header, Decision Condition column header, and Phase Name column all carry inline anti-pattern language — exceeds minimum of ≥2 |
| C-19 | PASS | Production gate: all 6 Scan Summary rows must show CLOSED; gate names artifact and required status condition |
| C-20 | PASS | GATE A (phase map → role registry), GATE B (role registry → state trace), GATE C (state trace/decisions → exception catalog), GATE D (exception catalog → terminal declarations), GATE P (production) — 5 distributed gates across full schema |
| C-21 | PASS | Handler (R-ID) in Exception Catalog; AS-IS FM-ID column is additive; all handler assignments require domain-qualified R-ID from registry |
| C-22 | PASS | Production gate inline failure declaration: "writing while any row shows OPEN is a structural fail" |
| C-23 | PASS | Exception Handler (Y/N) column in Role Registry; required per-row |
| C-24 | PASS | Gate text: "artifact must be discarded and scan rerun from SC-01" — remediation inline |
| C-25 | PASS | Gate text names causal defect types inline: "unanchored lifecycle, unenveloped phase, generic role, uncertified exception handler, unterminated path, or breach analysis disconnected from SLA evidence" |
| C-26 | PASS | Handler column header: backward-trace authority rule at point of column definition |
| C-27 | PASS | Scan Summary Defect Type column; 6 named defect types (most complete of all variations); gate sentence references column by name |
| C-28 | PASS | Handler column header co-locates rule and "Mandatory; blank or uncertified role is a fail" |
| C-29 | PASS | Decision Condition header: both enumeration (lifecycle-class-anchored threshold categories) AND quoted passing example with comparison operator and unit — belt-and-suspenders at point of column definition |
| C-30 | PASS | GATE C (upstream: state trace/decisions → exception catalog) + GATE D (downstream: exception catalog → terminal declarations) — both exception-catalog boundaries gated |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 22/22

```
score = (5/5 × 60) + (3/3 × 30) + (22/22 × 10) = 60 + 30 + 10 = 100
```

---

## Composite Scores and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Score | Notes |
|------|-----------|-----------|-------------|--------------|-------|-------|
| 1 | **V-05** | 5/5 | 3/3 | 22/22 | **100** | All axes; 5 gates; 6 scan rows; AS-IS traceability; both C-29+C-30; maximum density |
| 2 | **V-03** | 5/5 | 3/3 | 22/22 | **100** | Phase-first; both C-29+C-30; SLA Risk Declaration block; role-phase linkage |
| 3 | **V-04** | 5/5 | 3/3 | 22/22 | **100** | Lifecycle-class derivation; AS-IS anchor; FM-ID traceability; domain-anchored C-29 |
| 4 | **V-01** | 5/5 | 3/3 | 22/22 | **100** | Single C-29 mechanism (enumeration); upstream C-30 gate only |
| 5 | **V-02** | 5/5 | 3/3 | 22/22 | **100** | Single C-29 mechanism (example); downstream C-30 gate only |

All five variations score 100. V-05 ranks first on structural richness: it carries the greatest defect-type coverage in the Scan Summary (6 rows, 6 defect categories), the only schema where both exception-catalog boundaries are gated AND the causal mechanism gate sentence enumerates all 6 defect types inline, and the only schema where lifecycle-class vocabulary seeding, AS-IS traceability, and maximum column-header schema density operate simultaneously.

---

## Excellence Signals

Two structural patterns appear in V-05 (and partly in V-04) that are not captured by any criterion in the current rubric:

**Signal 1 — Lifecycle-Class Pre-Declaration with Domain Vocabulary Seeding**

V-04 and V-05 open with a LIFECYCLE CONTEXT DECLARATION that selects a lifecycle class (L2O, P2P, Period Close, Case Lifecycle) and surfaces domain-specific role titles and threshold-type categories for that class before any schema row is populated. This grounds the Role Registry vocabulary (so roles are drawn from a class-specific list, not invented ad hoc), the Decision Condition enumeration (so threshold types match the domain), and the Phase structure (phases are class-typical, not generic). No current criterion requires this class-based pre-population — C-11 requires concrete role examples and C-17 requires measurable thresholds, but neither requires that the vocabulary itself be derived from a declared domain class before the schema begins. A rubric can pass both without anchoring its vocabulary to a declared class; the class declaration enables backward verification (every role and threshold type must be traceable to the declared class or explicitly marked "Other") that no current criterion enforces.

**Signal 2 — AS-IS-to-Exception-Catalog Backward Traceability**

V-04 and V-05 add an AS-IS FM-ID column to the Exception Catalog, Bottleneck Register, and Gap Register, linking each designed exception flow and bottleneck to an observed failure mode from the Step 0 AS-IS scan (FM-1, FM-2, etc.) or marking it "new." This creates a backward trace from exception design to observed evidence: every exception flow that does not appear in the current-state failure mode list must be justified as a net-new design decision. No current criterion requires this linkage — C-02 requires exception flows with triggering condition and recovery path; C-04 requires bottleneck identification with cause and impact; neither requires that identified exceptions or bottlenecks be traceable to observed current-state evidence. The AS-IS FM-ID column operationalizes the question "where did this exception come from?" at the point of exception catalog authorship, adding a verifiability layer that the current rubric leaves open.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Lifecycle-class pre-declaration seeds domain vocabulary (role titles, threshold types, phase structure) from a selected class (L2O, P2P, Period Close, Case Lifecycle) before any schema row is populated — enabling backward verification that all role names and threshold types trace to the declared class", "AS-IS-to-exception-catalog backward traceability via FM-ID column in Exception Catalog and Bottleneck Register links each designed exception flow to an observed current-state failure mode from Step 0 scan, making exception presence verifiable against evidence rather than only internally consistent"]}
```
