Now I have everything needed. Let me score all five variations systematically against the full v4 rubric (C-01 through C-18).

---

# Quest Scorecard — campaign-behavior (R5)
**Skill:** campaign-behavior
**Rubric:** v4 (C-01–C-18)
**Round:** 5
**Date:** 2026-03-17

---

## Scoring Reference

| Tier | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01–C-05 (10 pts each) | 50 |
| Recommended | C-06–C-08 (10 pts each) | 30 |
| Aspirational | C-09–C-18 → (passed/10) × 10 | 10 |
| **Total** | | **90** |

Aspirational: binary PASS/FAIL per criterion. Score = (count passed / 10) × 10.

---

## V-01 — Permissions-anchor role sequence

### Essential (50 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 — All 5 sub-skills | PASS | Phases 1-5 cover trace-permissions, trace-state, trace-contract, flow-lifecycle, flow-trigger with full typed tables |
| C-02 — Ranked by blast radius | PASS | CONSOLIDATE: "Ranked findings (calibrated blast radius order, wide first)"; tiebreaker: CONFIRMED > unconfirmed, SYSTEMIC > isolated |
| C-03 — Spec gaps | PASS | CONSOLIDATE has explicit **Spec gaps:** section with "none detected" fallback |
| C-04 — Contract violations | PASS | CONSOLIDATE has **Contract violations:** section and **Privilege escalation paths:** section |
| C-05 — Single consolidated report | PASS | "Write ONE report. Do not concatenate five phase outputs." |

**Essential: 50/50**

### Recommended (30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 — Source attribution | PASS | "**Source:** [phase]" per ranked finding |
| C-07 — Remediation hint | PASS | "**What must change:** [one concrete fix direction]" per ranked finding |
| C-08 — Severity explicit | PASS | "**Severity at epicenter:** high / med / low" per ranked finding |

**Recommended: 30/30**

### Aspirational (C-09–C-18)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-09 — SYSTEMIC elevated | PASS | CALIBRATION: "Mark it SYSTEMIC if it appears in three or more phases." CONSOLIDATE ranks SYSTEMIC > isolated |
| C-10 — Verdict names component | PASS | VERDICT: "naming the finding with the widest blast radius (by census component name)" |
| C-11 — Blast radius via component names | PASS | "A finding that cannot name a census item is not a finding — return to the spec." Enforced throughout all phase tables |
| C-12 — Sub-skill typed schemas | PASS | All five phases use distinct column vocabularies (Role/Resource/Action for Phase 1; State/Invariant for Phase 2; Producer/Consumer for Phase 3; Phase/Entry/Exit for Phase 4; Trigger/Race for Phase 5) |
| C-13 — Severity + blast radius distinct | PASS | Separate fields in ranked findings; "Do not merge blast radius and severity. They are separate fields. Always." |
| C-14 — Calibration block | PASS | Named "CALIBRATION BLOCK" positioned after Phase 5 and before CONSOLIDATE; re-grounds blast radius via access surface inventory and shared state re-assessment |
| C-15 — Phase 0 topology census | PASS | "PHASE 0 -- Topology census" before any sub-skill runs; role-resource inventory for blast radius amplifier identification |
| C-16 — Per-phase exit criteria | PASS | All 5 phases carry explicit "EXIT CRITERIA:" with affirmative clean-state declarations (e.g., "trace-permissions: clean -- no escalation paths detected") |
| C-17 — CONFIRMED distinction | PASS | CALIBRATION has "CONFIRMED classification" section; Phase 3 marks CONFIRMED if connecting to Phase 1/2; Phase 5 marks CONFIRMED for escalated-role triggers; CONSOLIDATE ranks CONFIRMED > unconfirmed |
| C-18 — Q1–Qn interrogative calibration | FAIL | Uses phase-block calibration structure; no Q1–Qn questions |

**Aspirational: 9/10 → score 9**

**V-01 Total: 50 + 30 + 9 = 89**

---

## V-02 — Phrasing register: descriptive/interrogative throughout

### Essential (50 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 — All 5 sub-skills | PASS | All five described with typed tables ("What a complete trace-contract output looks like", etc.) |
| C-02 — Ranked by blast radius | PASS | CONSOLIDATE: "Ranked findings (calibrated blast radius order, wide first)" using 7-field RANKED FINDING scorecard |
| C-03 — Spec gaps | PASS | "**Spec gaps:**" in consolidated report |
| C-04 — Contract violations | PASS | "**Contract violations:**" in consolidated report |
| C-05 — Single consolidated report | PASS | "The consolidated report is one document -- not five phase outputs concatenated." |

**Essential: 50/50**

### Recommended (30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 — Source attribution | PASS | RANKED FINDING field "2. Source phase: [phase name]" |
| C-07 — Remediation hint | PASS | RANKED FINDING field "7. What must change: [one concrete fix direction]" |
| C-08 — Severity explicit | PASS | RANKED FINDING field "5. Severity at epicenter: [high \| med \| low]" |

**Recommended: 30/30**

### Aspirational (C-09–C-18)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-09 — SYSTEMIC elevated | PASS | Calibration identifies SYSTEMIC findings via cross-phase corroboration; RANKED FINDING has "6. SYSTEMIC: [yes -- phases: [list] \| no]" |
| C-10 — Verdict names component | PASS | VERDICT: "Names the finding with the widest blast radius by its census component name and its calibrated rank" |
| C-11 — Blast radius via component names | PASS | "A blast radius claim that cannot name a census component has no evidence basis." Evidence inventory enforces this |
| C-12 — Sub-skill typed schemas | PASS | Each sub-skill has distinct vocabulary: TC uses Producer/Consumer/Contract term; TS uses From state/Invariant/Violated; TP uses Role/Resource/Action; FL uses Phase/Entry/Exit; FT uses Trigger/Race condition |
| C-13 — Severity + blast radius distinct | PASS | RANKED FINDING: fields 4 (Blast radius) and 5 (Severity) are separate; "Do not merge blast radius and severity" |
| C-14 — Calibration block | PASS | "What a complete calibration block looks like" section; four-step structure after sub-skills and before consolidation |
| C-15 — Phase 0 topology census | PASS | "What a topology census looks like" section with four census components before any sub-skill descriptions |
| C-16 — Per-phase exit criteria | FAIL | Descriptive register has "If no X: write 'clean'" statements per sub-skill but no explicit "EXIT CRITERIA:" labeled gate; descriptive form does not constitute the named completion gate C-16 requires |
| C-17 — CONFIRMED distinction | FAIL | Calibration uses SYSTEMIC classification (2+ phases); no CONFIRMED / RUNTIME ANOMALY distinction cross-referencing runtime vs. contract topology specifically |
| C-18 — Q1–Qn interrogative calibration | FAIL | "What a complete calibration block looks like" structure; no Q1–Qn questions |

**Aspirational: 7/10 → score 7**

**V-02 Total: 50 + 30 + 7 = 87**

---

## V-03 — Asymmetric lifecycle emphasis (DEPTH labels)

### Essential (50 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 — All 5 sub-skills | PASS | Phases 1-5: trace-contract [HIGH], trace-state [AS-NEEDED], trace-permissions [MEDIUM], flow-lifecycle [MEDIUM], flow-trigger [HIGH] |
| C-02 — Ranked by blast radius | PASS | CONSOLIDATE: "Ranked findings (calibrated blast radius order, wide first)"; tiebreaker: SYSTEMIC > isolated, DEPTH: HIGH > MEDIUM > AS-NEEDED |
| C-03 — Spec gaps | PASS | "**Spec gaps:**" section in CONSOLIDATE |
| C-04 — Contract violations | PASS | "**Contract violations:**" section in CONSOLIDATE |
| C-05 — Single consolidated report | PASS | "Write ONE report. Do not concatenate five phase outputs." |

**Essential: 50/50**

### Recommended (30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 — Source attribution | PASS | "**Source:** [phase] [DEPTH label]" per ranked finding |
| C-07 — Remediation hint | PASS | "**What must change:** [one concrete fix direction]" per ranked finding |
| C-08 — Severity explicit | PASS | "**Severity at epicenter:** high / med / low" per ranked finding |

**Recommended: 30/30**

### Aspirational (C-09–C-18)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-09 — SYSTEMIC elevated | PASS | CALIBRATION: "Cross-phase corroboration: Mark SYSTEMIC." Rankings use SYSTEMIC > isolated |
| C-10 — Verdict names component | PASS | VERDICT: "naming the finding with the widest blast radius (by census component name), its source phase DEPTH label, and whether it is SYSTEMIC" |
| C-11 — Blast radius via component names | PASS | "A finding that cannot name a census item is not a finding." Enforced across all phase tables |
| C-12 — Sub-skill typed schemas | PASS | All five phases use distinct column vocabularies including depth-aware additions (Phase 1 adds "Propagation path"; Phase 2 adds "Connected to Phase 1?"; Phase 5 adds "Phase 1 contract affected?") |
| C-13 — Severity + blast radius distinct | PASS | Separate "**Blast radius:**" and "**Severity at epicenter:**" in ranked findings; "Do not merge" |
| C-14 — Calibration block | PASS | Named "CALIBRATION BLOCK" with depth yield review, evidence inventory, shared state re-assessment, cross-phase corroboration |
| C-15 — Phase 0 topology census | PASS | "PHASE 0 -- Topology census" before any sub-skill |
| C-16 — Per-phase exit criteria | PASS | All 5 phases have explicit EXIT CRITERIA with quantified completion declarations (e.g., "flow-trigger complete: [N] triggers evaluated, [N] race conditions found") |
| C-17 — CONFIRMED distinction | FAIL | Uses SYSTEMIC (2+ phases) as primary quality label; Phase 2 uses CONFIRMED for Phase 1-connected findings, but no systematic CONFIRMED / RUNTIME ANOMALY distinction across calibration or consolidation |
| C-18 — Q1–Qn interrogative calibration | FAIL | Uses phase-block structure with "Depth yield review" step; no Q1–Qn |

**Aspirational: 8/10 → score 8**

**V-03 Total: 50 + 30 + 8 = 88**

---

## V-04 — Phrasing register + scorecard output (combination)

### Essential (50 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 — All 5 sub-skills | PASS | All five described with numbered scorecard formats (TC-[N], TS-[N], TP-[N], FL-[N], FT-[N]) |
| C-02 — Ranked by blast radius | PASS | CONSOLIDATE: "Ranked findings (calibrated blast radius order, wide first)" using RANKED FINDING scorecard; SYSTEMIC > isolated |
| C-03 — Spec gaps | PASS | "**Spec gaps:**" section in consolidated report |
| C-04 — Contract violations | PASS | "**Contract violations:**" section in consolidated report |
| C-05 — Single consolidated report | PASS | "The consolidated report contains exactly these sections" — unified structure |

**Essential: 50/50**

### Recommended (30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 — Source attribution | PASS | RANKED FINDING: "2. Source phase: [phase name]" |
| C-07 — Remediation hint | PASS | RANKED FINDING: "7. What must change: [one concrete fix direction]" |
| C-08 — Severity explicit | PASS | RANKED FINDING: "5. Severity at epicenter: [high \| med \| low]" |

**Recommended: 30/30**

### Aspirational (C-09–C-18)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-09 — SYSTEMIC elevated | PASS | Calibration produces SYSTEMIC FINDING S-[N] scorecards with "2. Phases" and "5. Why it would have shipped" fields; consolidated findings include "6. SYSTEMIC: [yes -- phases]" |
| C-10 — Verdict names component | PASS | VERDICT: "Names the finding with the widest blast radius by its census component name and its calibrated rank" |
| C-11 — Blast radius via component names | PASS | Evidence inventory in calibration checks that each finding scorecard names a census component in blast radius field |
| C-12 — Sub-skill typed schemas | PASS | All five sub-skills use distinct numbered scorecard vocabularies: TC uses Producer/Consumer/Contract term; TS uses From state/To state/Invariant; TP uses Role/Resource/Privilege escalation; FL uses Phase/Entry contract/Exception path; FT uses Trigger/Fire order/Race condition |
| C-13 — Severity + blast radius distinct | PASS | RANKED FINDING fields 4 and 5 are separate; "Do not merge blast radius and severity. They are separate scorecard fields." |
| C-14 — Calibration block | PASS | "What a complete calibration block looks like" section with four-step process (evidence inventory, shared state re-assessment, corroboration check, clean zones) |
| C-15 — Phase 0 topology census | PASS | "What the topology census contains" with four census sections before any sub-skill descriptions |
| C-16 — Per-phase exit criteria | FAIL | Descriptive register provides clean-state declarations ("If no X: write 'clean'") per sub-skill but without explicit EXIT CRITERIA labels; same gap as V-02 |
| C-17 — CONFIRMED distinction | FAIL | SYSTEMIC FINDING S-[N] scorecard does not include CONFIRMED / RUNTIME ANOMALY field; ranked findings use SYSTEMIC yes/no but no CONFIRMED distinction |
| C-18 — Q1–Qn interrogative calibration | FAIL | Uses structured descriptive calibration; no Q1–Qn questions |

**Aspirational: 7/10 → score 7**

**V-04 Total: 50 + 30 + 7 = 87**

---

## V-05 — Permissions-anchor + asymmetric depth + inertia at VERDICT (combination)

### Essential (50 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 — All 5 sub-skills | PASS | Phases 1-5: trace-permissions [HIGH], trace-state [AS-NEEDED], trace-contract [MEDIUM], flow-lifecycle [MEDIUM], flow-trigger [HIGH] |
| C-02 — Ranked by blast radius | PASS | CONSOLIDATE: "Ranked findings (calibrated blast radius order, wide first)"; tiebreaker: SYSTEMIC > CONFIRMED > RUNTIME ANOMALY |
| C-03 — Spec gaps | PASS | "**Spec gaps:**" in CONSOLIDATE |
| C-04 — Contract violations | PASS | "**Contract violations:**" and "**Privilege escalation paths:**" in CONSOLIDATE |
| C-05 — Single consolidated report | PASS | "Write ONE report. Do not concatenate five phase outputs." |

**Essential: 50/50**

### Recommended (30 pts)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-06 — Source attribution | PASS | "**Source:** [phase] [DEPTH label]" per ranked finding |
| C-07 — Remediation hint | PASS | "**What must change:** [one concrete fix direction]" per ranked finding |
| C-08 — Severity explicit | PASS | "**Severity at epicenter:** high / med / low" per ranked finding |

**Recommended: 30/30**

### Aspirational (C-09–C-18)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-09 — SYSTEMIC elevated | PASS | Calibration Step 4: "Cross-phase corroboration (SYSTEMIC)"; calibration table has SYSTEMIC? column; CONSOLIDATE ranks SYSTEMIC > CONFIRMED |
| C-10 — Verdict names component | PASS | VERDICT: "naming the highest-blast-radius finding (SYSTEMIC CONFIRMED finding preferred over isolated findings), its census component, and its classification" |
| C-11 — Blast radius via component names | PASS | "Every blast radius claim below names a specific census entry. Generic claims are not valid." Calibration Step 1 enforces revision of any finding that cannot name a census component |
| C-12 — Sub-skill typed schemas | PASS | All five phases have distinct typed tables; Phase 4 and Phase 5 include unique "CONFIRMED / RUNTIME ANOMALY" classification column alongside sub-skill-specific vocabulary |
| C-13 — Severity + blast radius distinct | PASS | "**Blast radius:**" and "**Severity at epicenter:**" as separate ranked-finding fields; "Do not merge blast radius and severity. They are separate fields. Always." |
| C-14 — Calibration block | PASS | Named "CALIBRATION BLOCK" with explicit Steps 1-5 (evidence inventory → blast radius ceiling check → CONFIRMED/RUNTIME ANOMALY review → SYSTEMIC identification → clean zones) |
| C-15 — Phase 0 topology census | PASS | "PHASE 0 -- Topology census" before all sub-skills; includes unique **Pre-declared contracts:** field establishing the baseline for CONFIRMED classification |
| C-16 — Per-phase exit criteria | PASS | All 5 phases carry explicit EXIT CRITERIA with affirmative quantified statements (e.g., "trace-permissions complete: [N] pairs evaluated, [N] escalation paths found, [N] involving shared state surfaces") |
| C-17 — CONFIRMED distinction | PASS | Phase 0 defines: "Findings in Phases 4-5 that match violations from Phases 1-3 are CONFIRMED. Findings in Phases 4-5 with no matching topology violation are RUNTIME ANOMALY." Phases 4-5 tables include CONFIRMED/RUNTIME ANOMALY column. Calibration Step 3 reviews each classification. Consolidated findings include "**Classification:** CONFIRMED / RUNTIME ANOMALY" |
| C-18 — Q1–Qn interrogative calibration | FAIL | Uses numbered step calibration (Step 1-5), not Q1–Qn interrogative form |

**Aspirational: 9/10 → score 9**

**V-05 Total: 50 + 30 + 9 = 89**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | Aspirational pass count |
|-----------|-----------|-------------|--------------|-------|------------------------|
| V-01 | 50 | 30 | 9 | **89** | 9/10 |
| V-02 | 50 | 30 | 7 | 87 | 7/10 |
| V-03 | 50 | 30 | 8 | 88 | 8/10 |
| V-04 | 50 | 30 | 7 | 87 | 7/10 |
| V-05 | 50 | 30 | 9 | **89** | 9/10 |

**Top score: 89** (tied: V-01 and V-05). The single criterion that prevented a perfect 90 across all variations: **C-18 (Q1–Qn interrogative calibration)** — no R5 variation used the interrogative register.

---

## Variation Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 (tie) | **V-05** | 89 | Permissions-anchor + asymmetric depth + explicit CONFIRMED/RUNTIME ANOMALY throughout all runtime phases; richest C-17 implementation |
| 1 (tie) | **V-01** | 89 | Permissions-anchor + Phase 0 with role-resource inventory; CONFIRMED classification in calibration; all exit criteria present |
| 3 | V-03 | 88 | Asymmetric depth (DEPTH: HIGH/MEDIUM/AS-NEEDED) with minimum finding counts; deepest phase-quality enforcement |
| 4 (tie) | V-02 | 87 | Descriptive register activates self-evaluation; strongest per-finding scorecard structure; falls on C-16, C-17 |
| 4 (tie) | V-04 | 87 | Descriptive + scorecard combination; SYSTEMIC S-[N] scorecard innovation; falls on same C-16, C-17 as V-02 |

**Tiebreaker (V-01 vs V-05):** V-05 is the stronger variation. Its CONFIRMED/RUNTIME ANOMALY implementation is more complete — defined in Phase 0, tracked per-finding in Phases 4-5 table columns, reviewed in a dedicated calibration step, and surfaced in the consolidated findings field. V-01's CONFIRMED mechanism operates, but RUNTIME ANOMALY as the explicit counterpart is absent, meaning the evidence-tier distinction is partial.

---

## Excellence Signals from Top Variation (V-05)

**1. Pre-declared contracts in Phase 0**
V-05 adds a fifth Phase 0 field — **Pre-declared contracts** — to the topology census. This creates the contract topology baseline that makes the CONFIRMED/RUNTIME ANOMALY classification semantically rigorous. The classification isn't about two phases happening to agree; it's about a runtime observation matching a pre-existing structural expectation. Without this field, CONFIRMED degrades to SYSTEMIC (same thing said twice vs. prediction-plus-observation).

**2. Blast radius ceiling as the first finding, not a late discovery**
Running trace-permissions first (Phase 1) means the blast radius ceiling is established before any contract or lifecycle analysis runs. Every subsequent finding inherits a pre-classified access surface context. A trigger race in Phase 5 involving a Phase 1 escalation role is CONFIRMED immediately — the connection is mechanical, not retrospective.

**3. CONFIRMED/RUNTIME ANOMALY distinction threaded through all five phases**
V-05 doesn't just classify CONFIRMED in calibration — it classifies at the point of finding in Phases 4 and 5, using a dedicated column. Calibration then reviews those classifications, not creates them. This catches over-classification (a finding marked CONFIRMED that doesn't actually match a Phase 1-3 topology entry) before consolidation.

**4. Inertia framing concentrated at VERDICT only**
Rather than distributing assumption-displacement questions across phases (earlier R4 pattern), V-05 concentrates assumption framing in a pre-VERDICT block. The pattern: state what teams assumed about access surface, trigger ordering, and lifecycle contracts — then state what was found. The verdict then names the displacement, not just the finding. This makes the verdict do more work than a simple go/no-go label.

**5. Depth asymmetry (from V-03, carried into V-05)**
Assigning DEPTH: HIGH to trace-permissions and flow-trigger creates explicit execution asymmetry. Minimum expectation statements ("every trigger and every activating event is evaluated") for HIGH phases enforce that the most blast-radius-dense phases don't get abbreviated treatment.

---

## New Patterns Not Captured by C-01–C-18

**Candidate C-19 — Permissions-anchor sub-skill sequence**
Running trace-permissions as Phase 1 (before trace-contract, trace-state, flow-lifecycle, flow-trigger) to establish the access surface ceiling before any contract or state analysis begins. This is structurally distinct from C-15 (Phase 0 census, which is pre-execution vocabulary) and from C-17 (CONFIRMED distinction, which is calibration-phase classification). The permissions-anchor is an execution-order mechanism: blast radius is pre-classified from the access surface before any runtime behavior is observed. Any Phase 3-5 finding involving a Phase 1-escalated role inherits wide blast radius mechanically, not retrospectively.

**Candidate C-20 — Per-phase depth asymmetry (DEPTH labels with minimum finding counts)**
Explicit DEPTH: HIGH / MEDIUM / AS-NEEDED labels per phase, where HIGH phases carry a minimum execution expectation (e.g., "evaluate every trigger; if fewer than three exist, document all of them") and the calibration block explicitly verifies that HIGH phases produced at least one finding or a documented "clean" result. This is structurally distinct from C-01 (all 5 sub-skills present) and C-16 (exit criteria per phase). C-01 asks "did all five run?"; C-16 asks "did each phase complete?"; C-20 asks "did the high-yield phases execute at sufficient depth?" — a quality criterion, not a completion criterion.

---

```json
{"top_score": 89, "all_essential_pass": true, "new_patterns": ["permissions-anchor sub-skill sequence: trace-permissions runs first to establish the access surface ceiling before any contract or lifecycle analysis, pre-classifying blast radius from role-resource topology before runtime findings exist", "per-phase depth asymmetry: DEPTH labels (HIGH/MEDIUM/AS-NEEDED) with minimum finding count requirements and calibration-enforced depth yield review for high-blast-radius phases"]}
```
