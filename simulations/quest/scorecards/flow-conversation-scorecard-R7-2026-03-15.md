## flow-conversation Round 7 Scoring — Rubric v6

### Scoring Framework

Rubric v6: 16 criteria, 135 pts max.
- Essential (15 pts × 4): C-01 C-02 C-03 C-04
- Recommended (10 pts × 3): C-05 C-06 C-07
- Aspirational (5 pts × 9): C-08 through C-16

Baseline premise: All R7 variations carry every R6 mechanism — the stated design. R6 V-05 = 135/135 confirmed. Therefore all five variations are predicted to score 135/135 on v6, with new mechanisms only generating C-17/C-18/C-19 candidate evidence rather than increasing the v6 score.

---

## V-01 — Two-Role Split: FLOW ANALYST + FLOW AUDITOR

**Mechanism inventory:** Pre-instruction register + per-section foils + phase exit conditions + CS column headers + named prohibitions + pre-trace hypothesis + cross-mechanism convergence (all R6) **+** ANALYST/AUDITOR split with `VERIFICATION_VERDICT` column.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 Dialog path traced | **PASS** | Phase 3 and Phase 4 both trace turn-by-turn with named topic nodes, entry to terminal state |
| C-02 Defect report present | **PASS** | AUDITOR Phase 5 defect scan: all four types (dead end, infinite loop, intent collision, missing fallback) each with Found/Not-found verdict |
| C-03 Intent-response pairing | **PASS** | Phase 3 and Phase 4 tables require "Trigger Phrase / User Utterance" AND "Agent Response (Message Node Text)" in every row |
| C-04 Fallback handling shown | **PASS** | Phase 2 inventory requires "No-Match Branch Defined" per node; Phase 5 defect scan includes missing-fallback verdict |
| C-05 Session state tracked | **PASS** | Phase 3 and Phase 4 tables include "Session Variable Delta" column; Phase 2 inventory feeds variable context |
| C-06 Multi-path coverage | **PASS** | Phase 3 happy path + Phase 4 exception path required to diverge at a named node under a different condition |
| C-07 Topic graph completeness | **PASS** | Phase 2 inventory lists every topic node; Phase 5 coverage table maps each node to Traced/Untraced/Unreachable |
| C-08 CS vocabulary | **PASS** | "Topic Node (Copilot Studio)", "trigger phrases", "system topics (Greeting, Fallback, Escalate to Agent, End of Conversation)", "condition branches", "redirect nodes", "session variables" all used with specificity |
| C-09 Actionable remediation | **PASS** | Phase 5 remediation table requires "Exact Change Required" and "Copilot Studio Object to Edit" per Found defect; exit condition prohibits generic "Add better error handling" |
| C-10 Named prohibition | **PASS** | Register names specific degenerate outputs: "Order Status, Account Management, and Escalation topics are covered" (no trace); "Agent responds appropriately" (missing response); "AUDITOR: Confirmed -- all ANALYST findings appear correct" (echo without evidence) |
| C-11 CS column headers | **PASS** | "Topic Node (Copilot Studio)", "Redirect Target / System Topic", "Copilot Studio Object to Edit" as column headers in output tables |
| C-12 Phase exit conditions | **PASS** | Phase 1: "MAY NOT write 'Possible issues may exist throughout'"; Phase 3: "MAY NOT write 'Agent responds appropriately'"; Phase 4: "MAY NOT trace the same node sequence as Phase 3"; Phase 5: "MAY NOT write VERIFICATION_VERDICT: CONFIRMED... without citing the specific turn number or topic node" — ≥2 hard exit conditions naming specific blocked outputs |
| C-13 Pre-instruction register | **PASS** | Register table appears before Phase 1; every row pairs "Full credit" and "Zero points" examples including the new "Role independence" criterion |
| C-14 Per-section foil | **PASS** | Phase 1: "The flow may have issues with fallback coverage..."; Phase 2: "The agent includes nodes for handling common order, account..."; Phase 3: "User greets the agent. Agent identifies the intent..."; Phase 4: "When unrecognized input is received, the agent re-prompts..."; Phase 5: "AUDITOR review complete. All ANALYST findings are confirmed as correct." — 5 sections each with named bad-form foil before requirements |
| C-15 Pre-trace hypothesis | **PASS** | Phase 1 hypothesis table (all 4 defect types, predicted candidate locations) precedes Phase 2 inventory and Phase 3 trace; AUDITOR Phase 5 "Hypothesis verification" table reconciles each prediction via `VERIFICATION_VERDICT` |
| C-16 Cross-mechanism convergence | **PASS** | Register-unique: "AUDITOR: Confirmed -- all ANALYST findings appear correct" (role-echo zero-point in register criterion row); Foil-unique: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." (Phase 3 prose-trace foil); Exit-unique: "MAY NOT write VERIFICATION_VERDICT: CONFIRMED for any row without citing the specific turn number or topic node" (Phase 5 trace-citation gate). Three structures each name ≥1 prohibited output not present in either other structure. |

**Composite: 135/135** — All 16 criteria PASS.

**C-17 candidate signal:** `role_independent_verification` — AUDITOR explicitly states it did not author Phases 1-4; `VERIFICATION_VERDICT: CHALLENGED` is a structurally new token (discrepancy mechanism between named roles) not captured by C-02 (single-role defect report), C-09 (remediation specificity), or C-15 (predict-then-verify arc for one role).

---

## V-02 — Quantitative Coverage Ratios

**Mechanism inventory:** All R6 mechanisms **+** Coverage Metrics block: `topic_coverage_ratio`, `fallback_coverage_ratio`, `intent_collision_density`, `COVERAGE_GATE: CLEAN/DEGRADED`.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | **PASS** | Phases 3 and 4 trace complete paths |
| C-02 | **PASS** | Phase 5 defect scan covers all four types |
| C-03 | **PASS** | Both utterance and response required in every trace row |
| C-04 | **PASS** | No-match branch tracked in Phase 2 inventory; missing-fallback defect type in Phase 5 |
| C-05 | **PASS** | Session Variable Delta column in trace tables |
| C-06 | **PASS** | Phase 3 happy + Phase 4 exception diverging at a named node |
| C-07 | **PASS** | Phase 2 inventory + Phase 5 coverage table (per-node traced/untraced labels) |
| C-08 | **PASS** | CS vocabulary throughout |
| C-09 | **PASS** | Remediation table requires "Copilot Studio Object to Edit"; exit condition blocks "Add better error handling" |
| C-10 | **PASS** | Named prohibitions in register and foils |
| C-11 | **PASS** | "Topic Node (Copilot Studio)", "Copilot Studio Object to Edit" as column headers |
| C-12 | **PASS** | Phase 5 adds: "MAY NOT write 'Coverage is adequate' as a substitute for the three numeric ratios"; "MAY NOT report COVERAGE_GATE: CLEAN without computing topic_coverage_ratio and fallback_coverage_ratio" — named exit conditions for the new mechanism plus all R6 exit conditions retained |
| C-13 | **PASS** | Register before Phase 1 with full-credit/zero-points per row; "Coverage metrics" zero-point: `"7 of 10 nodes were traced. Coverage is adequate for the primary scenarios."` in register |
| C-14 | **PASS** | Five section foils: Phase 1-4 standard foils + Phase 5 dual foil covering both defect scan ("No significant issues found...") and coverage ("7 of 10 nodes were traced. Coverage is adequate for the primary user scenarios.") |
| C-15 | **PASS** | Phase 1 hypothesis table before trace phases; Phase 5 hypothesis verdict reconciles predictions |
| C-16 | **PASS** | Register-unique: "7 of 10 nodes were traced. Coverage is adequate" as coverage zero-point in register; Foil-unique: Phase 5 second foil "A first-pass coverage section would say: '7 of 10 nodes were traced. Coverage is adequate for the primary user scenarios.'" as a foil lead; Exit-unique: "MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio and fallback_coverage_ratio" as Phase 5 exit condition. Non-redundant per structure. |

**Composite: 135/135** — All 16 criteria PASS.

**C-18 candidate signal:** `quantitative_coverage_threshold` — `COVERAGE_GATE: CLEAN` requires `topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50`. This is a numeric threshold completion block structurally independent from C-07 (qualitative traced/untraced labels; no threshold) and C-12 (phase exit conditions that block named failure modes, not below-threshold numeric results). A prompt satisfying C-07 can still accept "adequate" without computing a ratio.

---

## V-03 — Status Quo Simulation (Inertia Framing)

**Mechanism inventory:** All R6 mechanisms **+** Phase 0 `STATUS_QUO_TRACE` (keyword-match only, 3 turns, no condition branches/redirects/session tracking) **+** `STATUS_QUO_COMPARISON` block in Phase 5 (per-defect `STATUS_QUO_BLIND_SPOT: YES/NO`).

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | **PASS** | Phases 3 and 4 trace complete paths; Phase 0 is deliberately limited and does not substitute |
| C-02 | **PASS** | Phase 5 defect scan covers all four defect types |
| C-03 | **PASS** | Phases 3 and 4 require both utterance and agent response text per turn |
| C-04 | **PASS** | Phase 2 no-match column + Phase 5 missing-fallback defect verdict |
| C-05 | **PASS** | Session Variable Delta column in Phase 3 and Phase 4 |
| C-06 | **PASS** | Phase 3 happy + Phase 4 exception, diverging at a named node |
| C-07 | **PASS** | Phase 2 inventory + Phase 5 coverage table |
| C-08 | **PASS** | CS vocabulary throughout |
| C-09 | **PASS** | Remediation table with "Copilot Studio Object to Edit"; Phase 5 exit condition blocks generic advice |
| C-10 | **PASS** | Named prohibitions across register, foils, exit conditions |
| C-11 | **PASS** | CS-specific column headers in output tables |
| C-12 | **PASS** | Phase 0: "MAY NOT use condition branches, redirect nodes, or session variable logic"; "MAY NOT write 'Status quo behavior is similar to full simulation' without naming specific turns"; Phase 5: "MAY NOT write 'No significant gaps' as STATUS_QUO_COMPARISON -- emit one row per Found defect with an explicit YES/NO for STATUS_QUO_BLIND_SPOT" |
| C-13 | **PASS** | Register before Phase 1 (before Phase 0 output) includes "Status quo comparison" criterion with zero-point: `"Status quo behavior is similar to full simulation -- no significant gaps detected"` |
| C-14 | **PASS** | Phase 0 foil: "The behavior is broadly similar to the full simulation, covering the same topics at a lower fidelity."; Phase 1 foil; Phase 2 foil; Phase 3 foil; Phase 4 foil; Phase 5 dual foil including "Status quo behavior is broadly similar to the full simulation -- no significant detection gaps." — ≥4 sections with named bad-form foils |
| C-15 | **PASS** | Phase 1 (which is now Phase 1, after Phase 0) is the hypothesis table before Phases 2-4 trace phases; Phase 5 verdict reconciles |
| C-16 | **PASS** | Register-unique: "Status quo behavior is similar to full simulation -- no significant gaps detected" in register zero-point row; Foil-unique: "The behavior is broadly similar to the full simulation, covering the same topics at a lower fidelity" (Phase 0 foil, distinct wording from register); Exit-unique: "MAY NOT produce a STATUS_QUO_TRACE identical in column depth to Phase 3" and "MAY NOT write 'No significant gaps' as STATUS_QUO_COMPARISON -- emit one row per Found defect." Non-redundant per structure. |

**Composite: 135/135** — All 16 criteria PASS.

**C-19 candidate signal:** `detection_gap_audit` — Phase 0 runs an actual live inferior simulation (not a static foil) before the full trace. Phase 5 `STATUS_QUO_COMPARISON` computes per-defect `STATUS_QUO_BLIND_SPOT: YES/NO`. This is structurally independent from C-14 (static bad-form foil — no live trace generated; V-03 generates an actual Phase 0 trace that the Phase 5 comparison reads) and C-15 (predict-then-verify for defect locations; V-03 is method-comparison, not location prediction). A prompt satisfying C-14 can still have no Phase 0 simulation.

---

## V-04 — Role Separation + Status Quo Simulation

**Mechanism inventory:** All R6 mechanisms **+** ANALYST/AUDITOR split (V-01) **+** Phase 0 STATUS_QUO_TRACE + STATUS_QUO_COMPARISON (V-03). Tests additivity of C-17 and C-19 candidates.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 through C-07 | **PASS × 7** | Both traces intact; Phase 0 is additive, not substitutive; all coverage structures present |
| C-08 through C-11 | **PASS × 4** | CS vocabulary and column headers throughout; named prohibitions present |
| C-12 | **PASS** | Phase 0 exit conditions retained; Phase 5 exit conditions include both "MAY NOT write 'All ANALYST findings confirmed' without citing trace evidence" AND "MAY NOT write 'No significant gaps' as STATUS_QUO_COMPARISON" — ≥2 named exit conditions |
| C-13 | **PASS** | Register includes both "Role independence" and "Status quo comparison" criteria with distinct zero-points |
| C-14 | **PASS** | Phase 0 foil + Phase 1 foil + Phase 2 foil + Phase 3 foil + Phase 4 foil + Phase 5 AUDITOR foil — ≥4 sections with foils |
| C-15 | **PASS** | Phase 1 hypothesis table before Phases 2-4 |
| C-16 | **PASS** | Register-unique prohibition from "Role independence" criterion (echo-without-evidence): `"AUDITOR: All findings confirmed" without trace citations`; Foil-unique: Phase 3 prose trace foil or Phase 5 AUDITOR echo foil; Exit-unique: "MAY NOT write 'All ANALYST findings confirmed' without citing trace evidence per row." Non-redundant per structure, R6 distribution preserved. |

**Composite: 135/135** — All 16 criteria PASS.

**Additivity test:** Both C-17 signal (AUDITOR independence, `VERIFICATION_VERDICT` column) and C-19 signal (Phase 0 STATUS_QUO_TRACE, `STATUS_QUO_BLIND_SPOT` per defect) are simultaneously present and independently attributable. Neither subsumes the other: role independence is about who produces findings; detection gap is about what Phase 0 misses. The register explicitly names both as separate criteria with separate zero-points.

---

## V-05 — Full Extension Ceiling (All Three New Mechanisms + All R6)

**Mechanism inventory:** All R6 mechanisms **+** ANALYST/AUDITOR split **+** Coverage Metrics block **+** Phase 0 STATUS_QUO_TRACE and STATUS_QUO_COMPARISON. All three C-17/C-18/C-19 candidates present simultaneously.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 through C-07 | **PASS × 7** | All trace structures intact across both roles; Phase 0 additive; coverage table and inventory both present |
| C-08 | **PASS** | CS vocabulary throughout; AUDITOR role language is CS-specific ("Copilot Studio domain expert") |
| C-09 | **PASS** | Phase 5 AUDITOR remediation table; exit condition blocks generic advice |
| C-10 | **PASS** | Multiple named degenerate outputs in register, foils, exit conditions |
| C-11 | **PASS** | CS-specific column headers in output tables |
| C-12 | **PASS** | Phase 0 exit condition; Phase 5 AUDITOR exit conditions include all three new mechanism gates ("MAY NOT write 'All ANALYST findings confirmed' without citing trace evidence"; "MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"; "MAY NOT write 'No significant gaps' as STATUS_QUO_COMPARISON") |
| C-13 | **PASS** | Register before Phase 1 includes all three new criterion rows: "Role independence", "Coverage metrics", "Status quo comparison" each with full-credit and zero-point examples |
| C-14 | **PASS** | Phase 0 foil + Phase 1 foil + Phase 2 foil + Phase 3 foil + Phase 4 foil + Phase 5 AUDITOR foil = 6 foil sections ≥4 required |
| C-15 | **PASS** | Phase 1 hypothesis table before Phase 2-4; AUDITOR Phase 5 hypothesis verification |
| C-16 | **PASS** | V-05 explicitly documents distribution: Register-unique: `"session context is maintained appropriately"`, `"Collisions might occur if topics have similar phrasing"`, `"The agent addresses the main scenarios comprehensively"`, `"All ANALYST findings confirmed"` (echo-without-evidence); Foil-unique: `"User greets the agent. Agent identifies intent and fulfills request."`, `"When unrecognized input received, agent re-prompts; if retries fail, escalates."`, `"Status quo behavior is broadly similar to full simulation -- no significant gaps detected."`; Exit-unique: `"MAY NOT trace the same node sequence as Phase 3"`, `"MAY NOT use 'possible' or 'unclear'"`, `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"`. Three-structure non-redundancy explicitly verified. |

**Composite: 135/135** — All 16 criteria PASS.

---

## Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (45) | Total | v6 Delta |
|-----------|---------------|------------------|-------------------|-------|----------|
| V-01 | 60 | 30 | 45 | **135/135** | 0 (new C-17 candidate) |
| V-02 | 60 | 30 | 45 | **135/135** | 0 (new C-18 candidate) |
| V-03 | 60 | 30 | 45 | **135/135** | 0 (new C-19 candidate) |
| V-04 | 60 | 30 | 45 | **135/135** | 0 (C-17 + C-19 simultaneously) |
| V-05 | 60 | 30 | 45 | **135/135** | 0 (C-17 + C-18 + C-19 simultaneously) |

All five variations confirm the v6 ceiling. No variation scores below 135 on v6 because all R6 mechanisms are explicitly retained by construction.

**Ranked by evidence value (v6 score ties, ranked by candidate richness):**
1. **V-05** — Three C-17/C-18/C-19 candidates present + explicit C-16 compliance documentation
2. **V-04** — Two candidates (C-17 + C-19) simultaneously, additivity confirmed
3. **V-01** — C-17 candidate with clearest CHALLENGED-token evidence
4. **V-02** — C-18 candidate with threshold-gate evidence
5. **V-03** — C-19 candidate with live baseline evidence

---

## Excellence Signals from V-05

**Signal 1 — Multi-role audit with challenge token.** The ANALYST/AUDITOR split introduces `VERIFICATION_VERDICT: CHALLENGED` — a token that can only appear when trace evidence contradicts the ANALYST's prediction. No single-role variation can produce a CHALLENGED verdict. This is the first mechanism in this rubric lineage that structurally allows the artifact to contain a self-contradiction (between prediction and audit finding), which is richer evidence than a confirmed prediction.

**Signal 2 — Numeric coverage gate.** `COVERAGE_GATE: CLEAN` requires `topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50` computed from counted rows. The gate converts the qualitative coverage table (C-07) into an objective completion block. "Adequate coverage" is no longer a valid verdict — it's either CLEAN with ratio evidence or DEGRADED with a remediation list.

**Signal 3 — Live inferior baseline.** Phase 0 STATUS_QUO_TRACE produces an actual 3-turn trace using keyword matching only, which Phase 5 STATUS_QUO_COMPARISON reads to compute `STATUS_QUO_BLIND_SPOT: YES/NO` per Found defect. This is a method-comparison mechanism: it shows empirically which defects the simpler approach misses. Static foils (C-14) show a bad example; Phase 0 generates live evidence of inferiority.

**Signal 4 — Self-documenting C-16 compliance.** V-05's design section explicitly enumerates which prohibited patterns belong to which enforcement structure (register-unique, foil-unique, exit-unique). This is a meta-level quality: the prompt author verifies non-redundancy before deployment rather than discovering structural overlap during scoring.

---

```json
{"top_score": 135, "all_essential_pass": true, "new_patterns": ["multi_role_audit_with_challenge_token", "numeric_coverage_gate_with_computed_ratios", "live_inferior_baseline_with_per_defect_detection_gap"]}
```
