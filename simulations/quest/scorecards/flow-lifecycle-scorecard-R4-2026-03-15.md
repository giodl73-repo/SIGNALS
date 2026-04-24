## flow-lifecycle — Round 4 Scoring

### V-01 — Output Format Axis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | STATE TABLE per phase has Entry Trigger and Exit Trigger columns; inline "Mandatory. 'Then X happens' is a fail" in column headers; ≥6 minimum enforced |
| C-02 | Exception Flow Traces | PASS | EXCEPTION CATALOG with E-ID, Phase, Trigger Condition, Divergence S-ID, Recovery/Terminal; ≥3 spanning ≥2 phases required |
| C-03 | Terminal State Completeness | PASS | TERMINAL DECLARATION with SUCCESS/FAILURE/CANCEL types; SCAN TABLE A/B confirms per-path closure |
| C-04 | Bottleneck and Gap Identification | PASS | BOTTLENECK AND GAP TABLE with B-IDs (cause + impact) and G-IDs (missing step + consequence); ≥2 bottlenecks, ≥1 gap required |
| C-05 | Domain Role Assignment | PASS | ROLE REGISTRY with inline generic-label negation; all decision gates, exception handlers, escalation paths cite R-IDs |
| C-06 | Parallel Path Modeling | PASS | PARALLEL PATH TABLE with fork, branches, join condition, join owner; sequential fallback with rationale |
| C-07 | Decision Point Explicitness | PASS | DECISION TABLE with condition (measurable threshold inline), owner R-ID, Branch A, Branch B, Fallback; ≥3 required |
| C-08 | Edge Case Enumeration | PASS | EDGE CASE TABLE with scenario, gap reason, consequence; ≥2 distinct from exception catalog |
| C-09 | Cross-Lifecycle Dependencies | PASS | CROSS-LIFECYCLE DEPENDENCY table with direction, coupling state, SLA dependency |
| C-10 | SLA and Timing Annotation | FAIL | Per-phase SLA only (LIFECYCLE PHASES + PHASE EXIT GATE); no SLA Window column in STATE TABLE; ≥3 per-state timing annotation not enforced |
| C-11 | Role-First Anchoring | PASS | ROLE REGISTRY before STATE TABLEs; concrete examples in column header ("Senior Credit Analyst," "AP Clerk," "Revenue Accountant") |
| C-12 | Anti-Pattern Negation | PASS | Inline negations in Role Name column ("do not count"), Entry Trigger column ("is a fail"), Decision Condition column ("does not count"), Fallback column ("is a structural fail") |
| C-13 | Sequential Gate Locking | FAIL | No "do not proceed until" language anywhere; sections are ordered but not gated |
| C-14 | Terminal Verification Pass | PASS | SCAN TABLE A (per-state S-ID to T-ID or next S-ID) + SCAN TABLE B (per-exception) with Status CLOSED/OPEN; SCAN SUMMARY |
| C-15 | Decision Fallback Coverage | PASS | Fallback column: "owner unavailable, system down, or configuration missing" — all 3 mechanism failures named |
| C-16 | Phase-Layer Structural Framing | PASS | LIFECYCLE PHASES table with entry trigger, completion condition, SLA envelope, at-risk threshold; per-phase blocks; ≥2 states per phase enforced |
| C-17 | Quantified Decision Boundaries | PASS | Decision Condition column: "Mandatory. Qualitative conditions...do not count — state a measurable threshold: dollar amount, day count, retry limit" |
| C-18 | Schema-Inline Anti-Pattern Placement | PASS | ≥5 inline schema column header negations: Role Name ("do not count"), Entry Trigger ("is a fail"), Exit Trigger ("is a fail"), Condition ("does not count"), Fallback ("is a structural fail"), SLA Impact ("does not count") |
| C-19 | Artifact-Level Production Gate | PASS | SCAN SUMMARY + "Artifact may not be written until Scan Summary shows status CLOSED" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 9/11 (C-10 FAIL, C-13 FAIL)

**Score**: (5/5 × 60) + (3/3 × 30) + (9/11 × 10) = 60 + 30 + 8.18 = **98.18**

---

### V-02 — Role Sequence Axis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | STATE TRACE table with Entry Trigger, Exit Trigger columns; ≥6 states; columns present though no inline "then X happens" guard |
| C-02 | Exception Flow Traces | PASS | EXCEPTION FLOWS freeform with trigger, divergence, deviation, recovery/terminal; ≥3 spanning ≥2 phases |
| C-03 | Terminal State Completeness | PASS | TERMINAL DECLARATION + TERMINAL VERIFICATION SCAN with per-path CLOSED gate |
| C-04 | Bottleneck and Gap Identification | PASS | BOTTLENECKS AND GAPS freeform with cause, downstream impact, missing step, consequence |
| C-05 | Domain Role Assignment | PASS | ROLE REGISTRY first; inline generic-label negation in Role Name column; all downstream cites R-IDs |
| C-06 | Parallel Path Modeling | PASS | PARALLEL PATHS freeform with join condition, join owner; sequential fallback with rationale |
| C-07 | Decision Point Explicitness | PASS | DECISION POINTS freeform with Owner R-ID, Condition (threshold), Branch A, Branch B, Fallback; ≥3 |
| C-08 | Edge Case Enumeration | PASS | EDGE CASES freeform with scenario, gap reason, consequence; ≥2 distinct |
| C-09 | Cross-Lifecycle Dependencies | PASS | CROSS-LIFECYCLE HANDOFF freeform with direction, partner lifecycle, coupling state |
| C-10 | SLA and Timing Annotation | FAIL | SLA Window column exists in STATE TRACE but ≥3 annotation not explicitly required; AT-RISK Risk column present but bottleneck linkage not enforced |
| C-11 | Role-First Anchoring | PASS | ROLE REGISTRY is absolute first section; "Do not proceed to phases until the Role Registry is complete"; concrete examples ("AP Clerk," "Senior Credit Analyst") |
| C-12 | Anti-Pattern Negation | PASS | Role Name column header: "do not count -- is a fail"; Decision Owner field: "does not count toward the 3-decision minimum" |
| C-13 | Sequential Gate Locking | PASS | "Do not proceed to phases until the Role Registry is complete" — explicit gate, enforces hardest criterion ordering |
| C-14 | Terminal Verification Pass | PASS | TERMINAL VERIFICATION SCAN per-path table (Path, Last Node, Terminal T-ID, Status) + CLOSED gate |
| C-15 | Decision Fallback Coverage | PASS | Fallback field: "(owner unavailable / system down / config missing)" named in field label |
| C-16 | Phase-Layer Structural Framing | PASS | PHASE TABLE with entry trigger, completion condition, SLA envelope, AT-RISK flag, SLA owner; ≥4 phases, ≥2 states per phase |
| C-17 | Quantified Decision Boundaries | PASS | Condition field: "measurable threshold -- e.g., 'Invoice total >= $50,000'; qualitative conditions do not count" |
| C-18 | Schema-Inline Anti-Pattern Placement | PASS | Role Name column header ("is a fail"); Decision Owner field ("does not count"); Condition field ("do not count") — ≥2 inline schema negations in schema section/cell definitions |
| C-19 | Artifact-Level Production Gate | PASS | TERMINAL VERIFICATION SCAN SUMMARY + "Artifact may not be written until Scan Summary shows status CLOSED" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 10/11 (C-10 FAIL)

**Score**: 60 + 30 + 9.09 = **99.09**

---

### V-03 — Phrasing Register Axis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | Step 4 state table with Entry Trigger column: "You must name the actor or system event. 'Then X happens' is a fail" — strongest inline enforcement of any variation |
| C-02 | Exception Flow Traces | PASS | Step 7 freeform with trigger, divergence, owner, deviation, recovery/terminal; ≥3 spanning ≥2 phases |
| C-03 | Terminal State Completeness | PASS | Step 11 terminal table + Step 12 verification scan; SUCCESS/FAILURE required |
| C-04 | Bottleneck and Gap Identification | PASS | Step 9 bottleneck format (cause, downstream impact) + gap format (missing step, consequence); ≥2 + ≥1 |
| C-05 | Domain Role Assignment | PASS | Step 2 role table with inline imperative negation; all later steps require R-ID from Step 2 |
| C-06 | Parallel Path Modeling | PASS | Step 6 with join condition, join owner; sequential fallback with rationale and parallelization proposal |
| C-07 | Decision Point Explicitness | PASS | Step 5 freeform with Decision, Owner R-ID, Condition (measurable), Branch A, Branch B, Fallback; ≥3 |
| C-08 | Edge Case Enumeration | PASS | Step 8 freeform with scenario, gap reason, consequence; ≥2 distinct |
| C-09 | Cross-Lifecycle Dependencies | PASS | Step 10 with partner, direction, coupling state, what passes, coupling risk |
| C-10 | SLA and Timing Annotation | FAIL | SLA Window column in Step 4 state table but no ≥3 annotation count enforced; AT-RISK Risk column present, bottleneck linkage not required inline |
| C-11 | Role-First Anchoring | PASS | Step 2 before all states; "You must complete this table before proceeding to Step 3"; concrete examples ("AP Clerk," "Revenue Accountant") |
| C-12 | Anti-Pattern Negation | PASS | Multiple imperative negations inline: "'Finance team,' 'Approver,' and 'Management' are fails," "'Then X happens' is a fail," "'Needs review' and 'large amount' are fails" |
| C-13 | Sequential Gate Locking | PASS | Multiple explicit gates: "Do not proceed to Step 2 until Step 1 is complete," "You must complete this table before proceeding to Step 3," "Do not proceed to Step 4 until phase table is complete," "Do not skip this step" (Step 12) |
| C-14 | Terminal Verification Pass | PASS | Step 12 per-path table + "Do not write the artifact until every row shows CLOSED and Scan Summary is CLOSED" |
| C-15 | Decision Fallback Coverage | PASS | Step 5 Fallback field: "Cover: owner unavailable, system down, configuration missing. A blank Fallback is a structural fail" |
| C-16 | Phase-Layer Structural Framing | PASS | Step 3 phase table with entry trigger, completion condition, SLA envelope, at-risk threshold; ≥4 phases, ≥2 states each, ≥1 AT-RISK with bottleneck |
| C-17 | Quantified Decision Boundaries | PASS | Step 5 Condition field: "name the measurable threshold -- dollar amount, day count, retry limit. 'Needs review' and 'large amount' are fails" |
| C-18 | Schema-Inline Anti-Pattern Placement | PASS | ≥2 inline negations in schema section/cell definitions: Step 2 Role Title column ("are fails"), Step 4 Entry Trigger column ("is a fail"), Step 5 Condition field ("are fails"), Step 5 Fallback field ("is a structural fail") |
| C-19 | Artifact-Level Production Gate | PASS | Step 12 SCAN SUMMARY + "Do not write the artifact until every row shows CLOSED and Scan Summary is CLOSED. A Scan Summary that is OPEN when the artifact is written is a structural fail" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 10/11 (C-10 FAIL)

**Score**: 60 + 30 + 9.09 = **99.09**

---

### V-04 — Combined: Role Sequence + Output Format

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | STATE TABLE with inline "Mandatory. 'Then X happens' is a fail" on both Entry/Exit Trigger columns; ≥6 states |
| C-02 | Exception Flow Traces | PASS | EXCEPTION CATALOG table with E-ID, phase, trigger, divergence, handling owner, deviation, recovery/terminal; ≥3 |
| C-03 | Terminal State Completeness | PASS | TERMINAL DECLARATION TABLE + SCAN TABLE A/B confirm all paths reach terminals |
| C-04 | Bottleneck and Gap Identification | PASS | Separate BOTTLENECK TABLE (≥2) and PROCESS GAP TABLE (≥1) with cause, impact, consequence |
| C-05 | Domain Role Assignment | PASS | ROLE REGISTRY first; inline negation in Role Name column; "No R-ID may be cited downstream that does not appear here" |
| C-06 | Parallel Path Modeling | PASS | PARALLEL PATH TABLE with join condition, join owner; sequential fallback with rationale |
| C-07 | Decision Point Explicitness | PASS | DECISION TABLE with condition (inline: "Mandatory. Name a measurable threshold"), owner, branches, fallback; ≥3 D-IDs |
| C-08 | Edge Case Enumeration | PASS | EDGE CASE TABLE with scenario, gap reason, consequence; ≥2 distinct |
| C-09 | Cross-Lifecycle Dependencies | PASS | CROSS-LIFECYCLE DEPENDENCY TABLE with direction, coupling state, what passes, SLA dependency |
| C-10 | SLA and Timing Annotation | FAIL | SLA Window column in STATE TABLE but ≥3 annotation not required; PHASE EXIT GATE TABLE has per-phase SLA breach, not per-state |
| C-11 | Role-First Anchoring | PASS | "Domain-qualified roles are the first artifact produced. No phase, state, or decision may be named before the Role Registry is complete"; concrete examples in column header |
| C-12 | Anti-Pattern Negation | PASS | Multiple inline negations in schema column headers across ROLE REGISTRY, STATE TABLE, DECISION TABLE, EXCEPTION CATALOG |
| C-13 | Sequential Gate Locking | PASS | "No phase, state, or decision may be named before the Role Registry is complete" — explicit constraint enforcing hardest ordering |
| C-14 | Terminal Verification Pass | PASS | SCAN TABLE A + SCAN TABLE B + SCAN SUMMARY with "Artifact may not be written until Scan Summary shows status CLOSED" |
| C-15 | Decision Fallback Coverage | PASS | Fallback column: "Mandatory. Name holding state or escalation path for: owner unavailable, system down, config missing. A blank Fallback does not count" |
| C-16 | Phase-Layer Structural Framing | PASS | PHASE TABLE (entry trigger, completion condition, SLA envelope, at-risk threshold, SLA owner) + PHASE EXIT GATE TABLE per phase; ≥2 states per phase enforced |
| C-17 | Quantified Decision Boundaries | PASS | Decision TABLE Condition column: "Mandatory. Name a measurable threshold: dollar amount, day count, retry count. 'Needs review' does not count" |
| C-18 | Schema-Inline Anti-Pattern Placement | PASS | ≥6 inline schema column header negations: Role Name + Decision Authority in ROLE REGISTRY; Entry/Exit Trigger in STATE TABLE; Condition + Fallback in DECISION TABLE; SLA Impact in EXCEPTION CATALOG |
| C-19 | Artifact-Level Production Gate | PASS | SCAN SUMMARY + "Artifact may not be written until Scan Summary shows status CLOSED" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 10/11 (C-10 FAIL)

**Score**: 60 + 30 + 9.09 = **99.09**

---

### V-05 — Combined: Role Sequence + Schema-Inline Anti-Patterns + Scan Tables + Artifact Gate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | PASS | STATE TRACE per phase with inline "Mandatory. 'Then X happens' is a fail — name the actor or system event. Describing the action in prose without naming a specific actor or event does not count toward the 6-state minimum" — strongest count-enforcement phrasing of any variation |
| C-02 | Exception Flow Traces | PASS | EXCEPTION CATALOG freeform with triggering condition, divergence, handling owner R-ID, deviation, recovery/terminal; ≥3 spanning ≥2 phases |
| C-03 | Terminal State Completeness | PASS | TERMINAL DECLARATION ("every terminal must have at least one Reached From entry") + SCAN TABLE A/B per-path closure |
| C-04 | Bottleneck and Gap Identification | PASS | BOTTLENECK AND GAP REGISTER freeform with cause, downstream impact, missing step, consequence; ≥2 + ≥1 |
| C-05 | Domain Role Assignment | PASS | ROLE REGISTRY before phases; inline negation in Role Name column ("do not count -- is a fail"); all downstream R-ID citations validated against registry |
| C-06 | Parallel Path Modeling | PASS | PARALLEL PATH BLOCK with fork, branches, join condition, join owner; sequential fallback with rationale |
| C-07 | Decision Point Explicitness | PASS | DECISION POINTS freeform per phase with Decision, Owner R-ID, Condition (measurable, inline negation), Branch A/B, Fallback; ≥3 |
| C-08 | Edge Case Enumeration | PASS | EDGE CASE CATALOG freeform with scenario, gap reason, consequence; ≥2 distinct |
| C-09 | Cross-Lifecycle Dependencies | PASS | CROSS-LIFECYCLE DEPENDENCY freeform with direction, partner lifecycle, coupling state, what passes, coupling risk |
| C-10 | SLA and Timing Annotation | FAIL | SLA Window column in per-phase STATE TRACE; EXIT GATE has per-phase SLA at-risk threshold + breach verdict; however ≥3 per-state annotation count not explicitly required as a minimum |
| C-11 | Role-First Anchoring | PASS | SCOPE DECLARATION first (context), ROLE REGISTRY second before any phase/state; "Do not proceed to phases until the Role Registry is complete"; concrete examples ("AP Clerk," "Senior Credit Analyst," "Case Resolution Specialist") |
| C-12 | Anti-Pattern Negation | PASS | Multiple inline negations: Role Name ("is a fail"), Phase Entry Trigger ("does not count"), Completion Condition ("does not count"), State Trigger ("is a fail"), Decision Condition ("do not count -- is a fail"), Fallback ("alone does not count") |
| C-13 | Sequential Gate Locking | PASS | Two explicit gates: "Do not proceed to phases until the Role Registry is complete" + "Do not proceed to Phase Delta blocks until the Phase Table is complete" — cascading gate hierarchy |
| C-14 | Terminal Verification Pass | PASS | SCAN TABLE A (per-state, with Phase column and CLOSED/OPEN status) + SCAN TABLE B (per-exception) + SCAN SUMMARY with per-table row counts |
| C-15 | Decision Fallback Coverage | PASS | Fallback field: "Mandatory. 'Escalate' alone does not count — name the holding state (S-ID) or escalation role (R-ID) and path. Covers: owner unavailable, system down, configuration missing" |
| C-16 | Phase-Layer Structural Framing | PASS | LIFECYCLE PHASE TABLE with inline negations on Entry Trigger + Completion Condition columns; per-phase Delta blocks (ENTRY CONTRACT + STATE TRACE + DECISION POINTS + EXIT GATE); ≥2 states per phase ("1:1 phase-to-state mapping does not count") |
| C-17 | Quantified Decision Boundaries | PASS | Decision Condition field: "Mandatory. Name a measurable threshold: dollar amount, day count, retry count, policy code. Qualitative conditions...do not count -- is a fail" |
| C-18 | Schema-Inline Anti-Pattern Placement | PASS | ≥8 inline schema negations at 4 schema locations: ROLE REGISTRY column header; LIFECYCLE PHASE TABLE two column headers (entry trigger + completion condition); STATE TRACE two column headers; DECISION POINTS two field labels; ENTRY CONTRACT field label |
| C-19 | Artifact-Level Production Gate | PASS | SCAN SUMMARY + "Artifact may not be written until Scan Summary shows status CLOSED across all rows in Scan Table A and Scan Table B" + pre-write checklist item "[ ] Scan Summary: Overall Status = CLOSED" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 10/11 (C-10 FAIL)

**Score**: 60 + 30 + 9.09 = **99.09**

---

### Composite Scores and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 (tie) | V-02 | 5/5 | 3/3 | 10/11 | 99.09 | YES |
| 1 (tie) | V-03 | 5/5 | 3/3 | 10/11 | 99.09 | YES |
| 1 (tie) | V-04 | 5/5 | 3/3 | 10/11 | 99.09 | YES |
| 1 (tie) | V-05 | 5/5 | 3/3 | 10/11 | 99.09 | YES |
| 5 | V-01 | 5/5 | 3/3 | 9/11 | 98.18 | YES |

**Failing criterion across all variations**: C-10 (SLA and Timing Annotation) — no variation explicitly requires ≥3 states to have populated SLA Windows; the column exists in V-02–V-05 but the count threshold is not enforced as a named minimum.

**V-01 additional failure**: C-13 (Sequential Gate Locking) — no "do not proceed until" language anywhere; sections are ordered but not gated. All other variations have at least one explicit gate.

---

### Excellence Signals (V-05)

V-05 ties at 99.09 but carries two structural patterns not captured in C-01–C-19:

**Signal 1 — Pre-Write Multi-Criterion Checklist**
V-05's OUTPUT block ends with a 9-item checklist ("all must be confirmed before writing") that names each quality requirement by category: role registry completeness, Phase Delta block completeness, trigger quality, decision quality, exception completeness, terminal completeness, Scan Table A closure, Scan Table B closure, Scan Summary CLOSED status. This operates AFTER the artifact-level production gate (C-19 scans must be closed) as a second quality sweep that confirms criterion-level compliance across all dimensions simultaneously — not just scan closure, but role quality, trigger quality, decision quality, and terminal completeness. Distinct from C-13 (gates step ordering) and C-19 (gates on scan closure alone). A reader who passes Scan Tables but has blank Fallbacks would be caught here; C-19 alone would not catch that.

**Signal 2 — Scope Declaration as Mandatory Gated First Block**
V-05 opens with a SCOPE DECLARATION block (lifecycle name, scenario, variant framing, rationale) marked "This block is Mandatory. A missing Scope Declaration is a fail" — the inline negation pattern applied at the block level rather than the column level. This gates all subsequent content on simulation context: an author cannot reach roles, phases, or states without declaring what lifecycle they are modeling and why variant comparison does not apply. Prevents context-free state traces and role registries that are structurally complete but domain-free. No other variation has a gated context-setting block before roles.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["pre-write multi-criterion checklist — a 9-item quality gate in the OUTPUT block that confirms criterion-level compliance across all dimensions (role quality, trigger quality, decision quality, terminal completeness, scan closure) simultaneously before artifact is written; distinct from C-19 which gates only on scan closure", "scope declaration as mandatory gated first block — a context-setting block (lifecycle name, scenario, variant framing, rationale) marked 'Mandatory. A missing Scope Declaration is a fail' that must be completed before roles or states are authored; prevents context-free simulations; operates at the block level using the C-18 inline-negation placement pattern"]}
```
