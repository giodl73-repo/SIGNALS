Now I have everything I need. Let me score all five variations.

---

# Quest Scorecard — campaign-behavior (Round 4)
**Skill:** campaign-behavior
**Rubric:** v4 (C-01–C-18)
**Date:** 2026-03-17

---

## Scoring Reference

| Tier | Criteria | Max |
|------|----------|-----|
| Essential | C-01–C-05 (10 pts each) | 50 |
| Recommended | C-06–C-08 (10 pts each) | 30 |
| Aspirational | C-09–C-18 — (passed/10) × 10 | 10 |
| **Total** | | **90** |

Aspirational tier: binary PASS/FAIL per criterion.

---

## V-01 — Prose-block output format

**Structure:** Phase 0 census → Phases 1–5 (labeled-field prose blocks, TC/TS/TP/FL/FT naming) → CALIBRATION BLOCK → CONSOLIDATE.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 All 5 sub-skills | PASS | All five phases present with TC/TS/TP/FL/FT finding blocks |
| C-02 Ranked by blast radius | PASS | "Ranked findings (calibrated blast radius order, wide first)" |
| C-03 Spec gaps | PASS | Labeled "Spec gaps:" section in CONSOLIDATE |
| C-04 Contract violations | PASS | Labeled "Contract violations:" section |
| C-05 Single consolidated report | PASS | "Write ONE report" directive; single CONSOLIDATE |
| C-06 Source attribution | PASS | "Source: [phase name]" field per finding |
| C-07 Remediation hint | PASS | "What must change: [one concrete fix direction]" |
| C-08 Severity explicit | PASS | "Severity at epicenter:" as separate labeled field |
| C-09 Systemic | PASS | CALIBRATION BLOCK: "Cross-phase corroboration... mark it SYSTEMIC" |
| C-10 Verdict names component | PASS | "one sentence naming the finding with the widest blast radius (by its census component name)" |
| C-11 Blast radius via component names | PASS | Phase 0 census is required reference; findings without census component are invalid |
| C-12 Per-sub-skill vocabulary | PASS | Prose blocks use TC schema (Producer/Consumer/Contract term), TS schema (From state/Trigger/Invariant), TP schema (Role/Resource/Action), FL schema (Phase/Entry/Exit/Exception), FT schema (Trigger/Fire order/Race) |
| C-13 Severity ≠ blast radius | PASS | Separate fields in every finding block; "Do not merge blast radius and severity" |
| C-14 Calibration block | PASS | Named "CALIBRATION BLOCK" with evidence inventory, shared state re-assessment, cross-phase corroboration |
| C-15 Pre-execution census | PASS | "PHASE 0 -- Topology census" before any sub-skill; components, shared state surfaces, downstream callers, role-resource inventory |
| C-16 Per-phase exit criteria | PASS | All 5 phases have explicit EXIT CRITERIA with affirmative clean-state declaration |
| C-17 CONFIRMED distinction | **FAIL** | No CONFIRMED/RUNTIME ANOMALY classification anywhere |
| C-18 Interrogative Q1-Qn | **FAIL** | CALIBRATION BLOCK uses phase-block format, not Q1-Q5 questions |

**Aspirational passed:** C-09 through C-16 = 8/10 → 8 pts

**V-01 Total: 50 + 30 + 8 = 88/90**

---

## V-02 — Behavior-first role sequence

**Structure:** Phase 0 census → Phase 1 (flow-lifecycle, behavioral) → diagnostic leads → Phase 2 (flow-trigger, behavioral) → diagnostic leads → Phases 3–5 (contract/state/permissions, diagnostic) → CALIBRATION BLOCK → CONSOLIDATE.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 All 5 sub-skills | PASS | All five present (reordered but all named and executed) |
| C-02 Ranked by blast radius | PASS | "Ranked findings (calibrated blast radius order, wide first)" |
| C-03 Spec gaps | PASS | "Spec gaps:" in CONSOLIDATE |
| C-04 Contract violations | PASS | "Contract violations:" in CONSOLIDATE |
| C-05 Single consolidated report | PASS | "Write ONE report" |
| C-06 Source attribution | PASS | "Source: [phase]" per finding |
| C-07 Remediation hint | PASS | "What must change:" |
| C-08 Severity explicit | PASS | "Severity at epicenter:" distinct field |
| C-09 Systemic | PASS | "Cross-phase corroboration... Mark them SYSTEMIC" in CALIBRATION BLOCK |
| C-10 Verdict names component | PASS | "naming the highest-blast-radius finding from the calibration table (census component name)" |
| C-11 Blast radius via component names | PASS | "All blast radius assessments must name a specific census component. Generic claims are not valid." |
| C-12 Per-sub-skill vocabulary | PASS | Each phase retains correct core vocabulary (Flow-lifecycle: Phase/Entry/Exit; Flow-trigger: Trigger/Activating event/Fire order; TC: Producer/Consumer; TS: State/Invariant; TP: Role/Resource/Action) — "Behavioral lead addressed" is an additive column, not a replacement |
| C-13 Severity ≠ blast radius | PASS | Distinct fields; "Do not merge blast radius and severity" |
| C-14 Calibration block | PASS | Named "CALIBRATION BLOCK" with behavioral root cause resolution, shared state re-assessment, corroboration, clean zones |
| C-15 Pre-execution census | PASS | "PHASE 0 -- Topology census" before any sub-skill |
| C-16 Per-phase exit criteria | PASS | All 5 execution phases have EXIT CRITERIA with affirmative clean-state declarations |
| C-17 CONFIRMED distinction | **FAIL** | "Behavioral root cause resolution" marks unresolved leads as RUNTIME ANOMALY but does not label resolved findings as CONFIRMED. The distinction is explained/unexplained, not CONFIRMED/unconfirmed. No explicit CONFIRMED classification applied to findings that match contract topology entries. |
| C-18 Interrogative Q1-Qn | **FAIL** | CALIBRATION BLOCK is phase-block format; no Q1-Q5 questions |

**Aspirational passed:** C-09 through C-16 = 8/10 → 8 pts

**V-02 Total: 50 + 30 + 8 = 88/90**

---

## V-03 — Inertia framing as recurring phase architecture

**Structure:** Phase 0 census (assumption: "we know what's in scope") → Phases 1–5 each opening with "Assumption being tested" and closing with EXIT CRITERIA "Assumption confirmed/displaced" → CALIBRATION BLOCK (assumption: "blast radius assessments are accurate") → CONSOLIDATE (findings = displaced assumptions, ranked by cost).

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 All 5 sub-skills | PASS | All five present with correct vocabulary |
| C-02 Ranked by blast radius | PASS | "Ranked findings (calibrated blast radius order, wide first)" — "cost of shipping with it undisplaced" maps directly to blast radius |
| C-03 Spec gaps | PASS | "Spec gaps: [displaced completeness assumptions]" |
| C-04 Contract violations | PASS | "Contract violations: [displaced producer/consumer assumptions]" |
| C-05 Single consolidated report | PASS | "One report. Every finding is a displaced assumption" |
| C-06 Source attribution | PASS | "Source: [phase]" per finding |
| C-07 Remediation hint | PASS | "What restores safety: [one concrete action]" — actionable, not a restatement |
| C-08 Severity explicit | PASS | "Severity at epicenter: high / med / low" separate field |
| C-09 Systemic | PASS | "A displaced assumption surfaced by two or more independent phases... Mark these SYSTEMIC" |
| C-10 Verdict names component | PASS | "name the one with the widest blast radius and state what it would cost to ship with it undisplaced" — the finding includes its census component |
| C-11 Blast radius via component names | PASS | "A blast radius claim that cannot name a component from this census is itself an undisplaced assumption — not a finding." Strongest enforcement of any variation. |
| C-12 Per-sub-skill vocabulary | PASS | Standard column schemas per sub-skill (same vocabulary as V-01) |
| C-13 Severity ≠ blast radius | PASS | Distinct fields; "Both appear in every finding. Never merge them." |
| C-14 Calibration block | PASS | Named "CALIBRATION BLOCK" with evidence inventory, shared state amplifier, cross-phase corroboration, clean zones |
| C-15 Pre-execution census | PASS | "PHASE 0 -- Topology census" with components, shared state surfaces, downstream callers, role-resource inventory, before any sub-skill |
| C-16 Per-phase exit criteria | PASS | All 5 phases have EXIT CRITERIA with "Assumption confirmed: [statement]" or "Assumption displaced: [N] violations found" — explicit affirmative clean-state declarations |
| C-17 CONFIRMED distinction | **FAIL** | "Assumption confirmed/displaced" operates per-phase on that phase's findings only; does not cross-reference runtime lifecycle/trigger findings against contract topology findings from separate phases. No CONFIRMED/RUNTIME ANOMALY classification of findings by cross-phase evidence tier. |
| C-18 Interrogative Q1-Qn | **FAIL** | CALIBRATION BLOCK is phase-block format (evidence inventory, shared state amplifier, corroboration, clean zones); no Q1-Q5 interrogative questions |

**Aspirational passed:** C-09 through C-16 = 8/10 → 8 pts

**V-03 Total: 50 + 30 + 8 = 88/90**

---

## V-04 — R3 V-04 architecture + CONFIRMED/RUNTIME ANOMALY (calibration time)

**Structure:** Phase 0 census (with Pre-declared contracts baseline) → Phases 1–3 (trace: contract/state/permissions as topology baselines, each with EXIT CRITERIA) → Phases 4–5 (flow: lifecycle/trigger, each with EXIT CRITERIA) → Phase 6 CALIBRATION BLOCK (6a evidence inventory, 6b CONFIRMED vs RUNTIME ANOMALY, 6c shared state, 6d SYSTEMIC, 6e clean zones) → CONSOLIDATE.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 All 5 sub-skills | PASS | Phases 1–5 each named and executed |
| C-02 Ranked by blast radius | PASS | "Ranked findings (calibrated blast radius order, wide first)"; tiebreaking CONFIRMED > RUNTIME ANOMALY |
| C-03 Spec gaps | PASS | "Spec gaps" section, calibration step 6a |
| C-04 Contract violations | PASS | "Contract violations" including CONFIRMED findings from Phases 4–5 |
| C-05 Single consolidated report | PASS | "Write ONE report. Do not concatenate five phase outputs." |
| C-06 Source attribution | PASS | "Sub-skill source: [phase]" per finding |
| C-07 Remediation hint | PASS | "What must change: [one concrete fix direction]" |
| C-08 Severity explicit | PASS | "Severity at the epicenter: high / med / low" distinct field |
| C-09 Systemic | PASS | Step 6d: "Identify findings that appear in two or more phases... Mark them SYSTEMIC" |
| C-10 Verdict names component | PASS | "Name the highest-blast-radius CONFIRMED finding from the calibration table (using its census component name)" |
| C-11 Blast radius via component names | PASS | "Every finding must name a specific census entry — not a generic description" |
| C-12 Per-sub-skill vocabulary | PASS | Phase 1 (Producer/Consumer), Phase 2 (State/Invariant), Phase 3 (Role/Resource/Action), Phase 4 (Phase/Entry contract/Exit contract), Phase 5 (Trigger/Race condition) |
| C-13 Severity ≠ blast radius | PASS | "Do not merge blast radius and severity. They are separate fields. Always." |
| C-14 Calibration block | PASS | Named "PHASE 6 -- CALIBRATION BLOCK" with full evidence re-grounding in six explicit steps |
| C-15 Pre-execution census | PASS | "PHASE 0 -- Topology census" with components, shared state surfaces, downstream callers, role-resource inventory, AND "Pre-declared contracts" for CONFIRMED baseline |
| C-16 Per-phase exit criteria | PASS | All 5 execution phases (1–5) have EXIT CRITERIA with affirmative "write 'X: clean' if clean" declarations |
| C-17 CONFIRMED distinction | **PASS** | Step 6b explicitly: "CONFIRMED vs RUNTIME ANOMALY classification" for Phases 4–5 findings cross-referenced against Phases 1–3 topology. Classification table with CONFIRMED/RUNTIME ANOMALY column. CONSOLIDATE has "Classification: CONFIRMED / RUNTIME ANOMALY" per finding. CONFIRMED findings rank above RUNTIME ANOMALY at equal blast radius. |
| C-18 Interrogative Q1-Qn | **FAIL** | CALIBRATION BLOCK uses named phase-steps (6a–6e), not Q1–Q5 interrogative questions |

**Aspirational passed:** C-09 through C-17 = 9/10 → 9 pts

**V-04 Total: 50 + 30 + 9 = 89/90**

---

## V-05 — All four new criteria simultaneously

**Structure:** Phase 0 census (dual-purpose: blast radius vocabulary AND CONFIRMED baseline) → Phases 1–3 (topology baselines, EXIT CRITERIA) → Phases 4–5 (runtime execution with CONFIRMED/RUNTIME ANOMALY inline per finding, EXIT CRITERIA) → Q1–Q5 calibration questions answered from evidence → Calibration summary paragraph → CONSOLIDATE.

| Criterion | Score | Evidence |
|-----------|-------|----------|
| C-01 All 5 sub-skills | PASS | Phases 1–5 all named and executed |
| C-02 Ranked by blast radius | PASS | "Ranked findings (calibrated blast radius order, wide first)"; four-tier tiebreaking (CONFIRMED+SYSTEMIC > CONFIRMED > RUNTIME ANOMALY+SYSTEMIC > RUNTIME ANOMALY) |
| C-03 Spec gaps | PASS | "Spec gaps:" section |
| C-04 Contract violations | PASS | "Contract violations: CONFIRMED violations from trace-contract and Phases 4–5" |
| C-05 Single consolidated report | PASS | "Write ONE report. Do not concatenate five sub-skill outputs." |
| C-06 Source attribution | PASS | "Sub-skill source: [phase]" per finding |
| C-07 Remediation hint | PASS | "What must change: [one concrete fix direction]" |
| C-08 Severity explicit | PASS | "Severity at epicenter: high / med / low" distinct field |
| C-09 Systemic | PASS | Q4: "Which findings appear in two or more phases? Mark as SYSTEMIC"; CONSOLIDATE has SYSTEMIC field with phase corroboration list |
| C-10 Verdict names component | PASS | Q5 produces explicit named anchor: "Name the finding, its census component, its CONFIRMED/RUNTIME status, its blast radius." Verdict cites Q5 anchor. |
| C-11 Blast radius via component names | PASS | Phase 0 census; all phase tables require "(census component)" in blast radius column; Q1 asks "Which specific census components actually showed up in your findings?" |
| C-12 Per-sub-skill vocabulary | PASS | Phase 1 (Producer/Consumer/Contract term), Phase 2 (State/Preconditions/Invariant), Phase 3 (Role/Resource/Action), Phase 4 (Phase/Entry/Exit contract + CONFIRMED column), Phase 5 (Trigger/Fire order/Race + CONFIRMED column) — core vocabularies intact with CONFIRMED column added |
| C-13 Severity ≠ blast radius | PASS | "Do not merge blast radius and severity. They are separate fields." Two distinct labeled fields per finding. |
| C-14 Calibration block | PASS | Rubric explicitly states: "The interrogative calibration variant (Q1–Q5 questions) satisfies this criterion equally with the phase-block variant." V-05 has Q1–Q5 positioned after all sub-skills and before CONSOLIDATE with explicit blast-radius re-grounding. |
| C-15 Pre-execution census | PASS | Phase 0 before any sub-skill; components, shared state surfaces, downstream callers, role-resource inventory; explicitly declares both its census and CONFIRMED-baseline functions |
| C-16 Per-phase exit criteria | PASS | All 5 execution phases have EXIT CRITERIA with "X: clean" affirmative clean-state declarations |
| C-17 CONFIRMED distinction | **PASS** | CONFIRMED/RUNTIME ANOMALY classification inline in Phase 4 and Phase 5 tables ("Phase 1-3 match?" column + "CONFIRMED / RUNTIME ANOMALY" column); Q3 asks "Which findings are CONFIRMED?" listing matches; CONSOLIDATE has "Classification: CONFIRMED / RUNTIME ANOMALY" per finding. Two-layer coverage: inline at execution + Q3 synthesis. |
| C-18 Interrogative Q1-Qn | **PASS** | Explicit Q1–Q5 covering all four required elements: Q1 (component identification from findings), Q2 (shared state identification + blast radius upgrade), Q3 (CONFIRMED findings listed with matching entries), Q4 (SYSTEMIC findings with phase list), Q5 (named blast-radius anchor). Five questions, all answered from sub-skill evidence, before CONSOLIDATE. |

**Aspirational passed:** C-09 through C-18 = 10/10 → 10 pts

**V-05 Total: 50 + 30 + 10 = 90/90**

---

## Round 4 Rankings

| Rank | Variation | Score | Aspirational (passed) |
|------|-----------|-------|-----------------------|
| 1 | V-05 — All four new criteria | **90/90** | 10/10 |
| 2 | V-04 — R3 V-04 + CONFIRMED (calibration time) | **89/90** | 9/10 |
| 3 | V-01 — Prose-block output format | **88/90** | 8/10 |
| 3 | V-02 — Behavior-first role sequence | **88/90** | 8/10 |
| 3 | V-03 — Inertia framing recurring | **88/90** | 8/10 |

**Predicted:** V-05 >= V-04 > V-03 > V-01 > V-02
**Actual:** V-05 > V-04 > V-01 = V-02 = V-03

The predicted differentiation between V-03, V-01, and V-02 did not materialize. All three share the same aspirational profile (C-09–C-16 pass, C-17–C-18 fail) because none targets CONFIRMED classification. The behavioral-leads mechanism in V-02 was not penalized (C-01 passes on any execution order) and was not rewarded (RUNTIME ANOMALY without CONFIRMED = C-17 FAIL).

---

## Excellence Signals (V-05)

**1. Dual-layer CONFIRMED classification (inline + calibration)**
V-05 classifies CONFIRMED/RUNTIME ANOMALY both *inline* during Phase 4 and Phase 5 execution (via "Phase 1-3 match?" and "CONFIRMED / RUNTIME ANOMALY" columns in those tables) AND retrospectively via Q3. This double coverage means the classification survives context window drift: if the model forgets the Phase 0 contract baseline by Phase 5, Q3 forces it to re-examine. V-04's calibration-only classification is a single-point mechanism; V-05's inline + Q3 structure is redundant by design.

**2. Q5 as a pre-committed verdict anchor**
Q5 ("What is the single finding whose failure would propagate furthest in production?") forces the model to name and defend its verdict anchor *before* writing the ranked list. This separates the choice of anchor from the act of ranking — the verdict is not derived from the ranked list, it is declared first and the list is organized around it. This eliminates the common failure mode where the verdict says "conditional go" but the highest-ranked finding is low severity.

**3. Four-tier ranking hierarchy**
V-05 explicitly defines: CONFIRMED+SYSTEMIC > CONFIRMED > RUNTIME ANOMALY+SYSTEMIC > RUNTIME ANOMALY. This 2×2 matrix (evidence tier × corroboration) makes tiebreaking deterministic at any blast radius level. Prior variations (including V-04) only partially specified this — V-04 had "CONFIRMED > RUNTIME ANOMALY, SYSTEMIC > isolated" but didn't define the interaction when a finding is CONFIRMED but not SYSTEMIC vs. one that is SYSTEMIC but only RUNTIME ANOMALY.

**4. Phase 0 dual-purpose declaration**
V-05's Phase 0 explicitly declares both its functions: (1) census vocabulary for blast radius claims, and (2) contract topology baseline for CONFIRMED classification. By naming the CONFIRMED function at Phase 0, the model cannot "forget" the classification contract before reaching Phases 4-5. V-04's Phase 0 has "Pre-declared contracts" but the dual-purpose framing is less explicit.

---

## No New Patterns for Rubric Update

All excellence signals above are implementations of existing criteria (C-14, C-15, C-17, C-18) rather than structurally independent patterns. The four-tier ranking hierarchy is a consequence of combining C-09 and C-17, not a new mechanism. No new aspirational criteria are warranted from Round 4.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": []}
```
