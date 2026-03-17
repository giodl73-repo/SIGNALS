# Quest Scorecard — campaign-behavior (Round 3)
**Skill:** campaign-behavior
**Rubric:** v3 (C-01–C-14)
**Scoring:** Essential 50 + Recommended 30 + Aspirational (passed/6)×10 = 90 max
**Date:** 2026-03-17

---

## Per-Variation Scoring

### V-01 — Calibration block injected into R2 V-05 base

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 All 5 sub-skills | Essential | PASS | Phases 1–5 named with explicit exit criteria |
| C-02 Ranked by blast radius | Essential | PASS | "Ranked findings (blast radius order, calibrated): Use the calibration table. Wide blast radius first." |
| C-03 Spec gaps | Essential | PASS | CONSOLIDATE: "Spec gaps: List all spec gaps from the census. Write 'none detected' if clean." |
| C-04 Contract violations | Essential | PASS | CONSOLIDATE: "Contract violations: List all producer/consumer mismatches." |
| C-05 Consolidated report | Essential | PASS | "Write ONE report. Not five." |
| C-06 Source attribution | Recommended | PASS | "Sub-skill source: [phase that found it]" per finding |
| C-07 Remediation hint | Recommended | PASS | "What must change: [one clear direction]" per finding |
| C-08 Severity explicit | Recommended | PASS | "Severity at the epicenter: high / med / low" per finding |
| C-09 Systemic cross-ref | Aspirational | PASS | Phase 6 step 4 marks SYSTEMIC; CONSOLIDATE "Cross-skill findings" section |
| C-10 Verdict names component | Aspirational | **FAIL** | Verdict says "Name the highest-blast-radius finding from the calibration table" — no "(using its census component name)" qualifier. Component not explicitly required in verdict sentence. |
| C-11 Blast radius operationalized | Aspirational | PASS | Calibration table column "Census component(s) affected"; CONSOLIDATE: "Blast radius … (name the census component affected)" |
| C-12 Per-sub-skill schema typed | Aspirational | PASS | All 5 phases use explicit pipe-tables with sub-skill vocabulary (Producer/Consumer/Contract; State/Preconditions/Invariant; Role/Resource/Action; Phase/Entry contract; Trigger/Event/Fire order) |
| C-13 Severity × blast radius co-located | Aspirational | PASS | Phase 1 table has separate Severity and Blast radius columns; CONSOLIDATE has both as distinct labeled fields per finding |
| C-14 Calibration block | Aspirational | PASS | "PHASE 6 — CALIBRATION BLOCK" named after Phase 5, before CONSOLIDATE; re-grounds blast radius against actual findings |

**Aspirational passed:** C-09, C-11, C-12, C-13, C-14 = 5/6 → (5/6)×10 = **8**
**Score: 50 + 30 + 8 = 88**

---

### V-02 — Contract-anchor sequence with calibration phased-in

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | PASS | All 5 sub-skills across Steps 1–5 |
| C-02 | Essential | PASS | "Ranked findings (by calibrated blast radius, wide first)" |
| C-03 | Essential | PASS | "Spec gaps: [from calibration audit -- or 'none detected']" |
| C-04 | Essential | PASS | "Contract violations: [CONFIRMED violations from calibration]" |
| C-05 | Essential | PASS | "Write ONE report synthesizing all steps and calibration." |
| C-06 | Recommended | PASS | "Per finding: sub-skill source \| what breaks \| blast radius \| severity \| what must change \| CONFIRMED? \| SYSTEMIC?" |
| C-07 | Recommended | PASS | "what must change" field per finding |
| C-08 | Recommended | PASS | "severity (high/med/low)" in per-finding format |
| C-09 Systemic | Aspirational | PASS | "Cross-step corroboration: Any finding that appears in two or more steps is SYSTEMIC." |
| C-10 Verdict component | Aspirational | **FAIL** | Verdict: "One sentence naming the highest-blast-radius CONFIRMED finding" — no component name required |
| C-11 Blast radius operationalized | Aspirational | **FAIL** | No Phase 0 topology census; calibration table has no "census component" column (`Finding \| Steps \| CONFIRMED? \| SYSTEMIC? \| Blast radius \| Severity`). Component names not mandated in blast radius assessments. |
| C-12 Typed schemas | Aspirational | PASS | All 5 steps have distinctly typed tables: permissions (Role/Resource/Action/Privilege escalation?), state (State/Preconditions/Invariant), contract (Producer/Consumer/Contract term), lifecycle (+Contract match from Step 3?), trigger (+State invariant violated (Step 2)?) |
| C-13 Severity × blast radius | Aspirational | PASS | Calibration table: `Blast radius (calibrated) \| Severity` co-located; CONSOLIDATE per-finding has both as pipe-separated fields |
| C-14 Calibration block | Aspirational | PASS | "CALIBRATION BLOCK" named after Step 5, before CONSOLIDATE; "Re-ground blast radius in what you actually found, not in what you expected to find." |

**Aspirational passed:** C-09, C-12, C-13, C-14 = 4/6 → (4/6)×10 = 6.67 → **7**
**Score: 50 + 30 + 7 = 87**

---

### V-03 — Interrogative calibration (evidence-first phrasing register)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | PASS | All 5 named in sub-skill execution section with explicit report fields |
| C-02 | Essential | PASS | "Ranked findings (calibrated blast radius, wide first)" |
| C-03 | Essential | PASS | "Spec gaps: [list from Q4 evidence -- or 'none detected']" |
| C-04 | Essential | PASS | "Contract violations: [from trace-contract findings -- or 'none detected']" |
| C-05 | Essential | PASS | "Write ONE report." |
| C-06 | Recommended | PASS | "Source: [sub-skill]" per finding in CONSOLIDATE |
| C-07 | Recommended | PASS | "Fix direction: [one clear action]" per finding |
| C-08 | Recommended | PASS | "Severity at epicenter: high / med / low" per finding |
| C-09 Systemic | Aspirational | PASS | Q3: "A finding corroborated by two or more sub-skills is SYSTEMIC." CONSOLIDATE: "SYSTEMIC: yes / no (from Q3)" per finding |
| C-10 Verdict component | Aspirational | PASS | Q5 explicitly: "This is your blast-radius anchor. Name the component from your findings that it touches." VERDICT: "One sentence citing the Q5 anchor finding" — Q5's answer inherently contains the named component, satisfying both (a) finding and (b) component. |
| C-11 Blast radius operationalized | Aspirational | PASS | Q1: "List the component names that appear in the evidence above." Q2: "Name every finding where the affected component is something multiple other components depend on." CONSOLIDATE: "Blast radius: wide / medium / narrow (from calibration -- cite the component from Q1)" |
| C-12 Typed schemas | Aspirational | PASS | All 5 sub-skills use sub-skill-specific field vocabularies: trace-contract (producer/consumer/mismatch type), trace-state (from-state/invariant/violated?), trace-permissions (role/resource/privilege escalation?), flow-lifecycle (phase/entry contract/exit contract), flow-trigger (trigger/fire order/race condition?). No uniform schema; vocabulary clearly sub-skill-typed. |
| C-13 Severity × blast radius | Aspirational | PASS | CONSOLIDATE per-finding: "Blast radius: wide / medium / narrow" and "Severity at epicenter: high / med / low" as distinct labeled fields |
| C-14 Calibration block | Aspirational | PASS | "## Calibration questions (answer before you rank)" — named synthesis phase after execution, before CONSOLIDATE. Rubric text explicitly validates: "C-14 specifically rewards the post-execution calibration variant" and references "V-03 pattern" by name. |

**Aspirational passed:** C-09, C-10, C-11, C-12, C-13, C-14 = 6/6 → (6/6)×10 = **10**
**Score: 50 + 30 + 10 = 90**

---

### V-04 — R2 V-05 base + CALIBRATION BLOCK (structural completion)

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | PASS | All 5 phases named with EXIT CRITERIA gates |
| C-02 | Essential | PASS | "Ranked findings (calibrated blast radius, wide first): Use the calibration table from Phase 6." |
| C-03 | Essential | PASS | "Spec gaps: [from calibration step 6c -- all spec gaps collected across all phases]. Write 'none detected'" |
| C-04 | Essential | PASS | "Contract violations: [from trace-contract findings and any corroborating evidence from other phases]. Write 'none detected' if clean." |
| C-05 | Essential | PASS | "Write ONE report. Do not concatenate five separate outputs." |
| C-06 | Recommended | PASS | "Sub-skill source: [phase]" per finding |
| C-07 | Recommended | PASS | "What must change: [one clear fix direction]" per finding |
| C-08 | Recommended | PASS | "Severity at the epicenter: high / med / low" as distinct field |
| C-09 Systemic | Aspirational | PASS | Phase 6d: "Identify findings that appear in two or more phases. Mark them SYSTEMIC." CONSOLIDATE: "Cross-skill findings" section lists all SYSTEMIC with phase list |
| C-10 Verdict component | Aspirational | PASS | Verdict: "Name the highest-blast-radius finding from the calibration table **(using its census component name)**" — explicit requirement for component name in verdict sentence |
| C-11 Blast radius operationalized | Aspirational | PASS | Phase 0 census + calibration table column "Census component(s)"; CONSOLIDATE: "Blast radius: wide / medium / narrow -- name the census component affected and whether it is a shared state surface" |
| C-12 Typed schemas | Aspirational | PASS | All 5 phases use explicit pipe-tables with sub-skill vocabulary: trace-contract (Producer/Consumer/Contract term/Expected/Actual/Mismatch?), trace-state (State/Preconditions/Invariant/Violated?), trace-permissions (Role/Resource/Action/Privilege escalation?), flow-lifecycle (Phase/Entry contract/Exit contract/Exception path), flow-trigger (Trigger/Event/Side effects/Fire order/Race condition?) |
| C-13 Severity × blast radius | Aspirational | PASS | Phase 1 table: "Severity \| Blast radius (census component)" as separate columns; CONSOLIDATE: both as distinct labeled fields on every finding. "Do not merge blast radius and severity. They are separate labeled fields. Always." |
| C-14 Calibration block | Aspirational | PASS | "PHASE 6 -- CALIBRATION BLOCK" named after Phase 5, before CONSOLIDATE; steps 6a–6d explicitly re-evaluate blast radius from actual findings |

**Aspirational passed:** C-09, C-10, C-11, C-12, C-13, C-14 = 6/6 → (6/6)×10 = **10**
**Score: 50 + 30 + 10 = 90**

---

### V-05 — Full integration: census + schemas + calibration + phase gates + anti-conflation + inertia framing

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01–C-05 | Essential | PASS (all) | Same structure as V-04; inertia framing doesn't affect execution coverage |
| C-06–C-08 | Recommended | PASS (all) | Same per-finding format as V-04 |
| C-09 Systemic | Aspirational | PASS | Phase 6d + CONSOLIDATE "Cross-skill findings" with phase list |
| C-10 Verdict component | Aspirational | **FAIL** | Verdict: "Name the finding from the calibration table with the widest blast radius and highest corroboration" — unlike V-04, no "(using its census component name)" qualifier. Component name not mandated in verdict sentence despite being in calibration table columns. |
| C-11 Blast radius operationalized | Aspirational | PASS | Phase 0 census + calibration table "Census component \| Shared state surface?"; CONSOLIDATE: "name the census component and whether it is a shared state surface" |
| C-12 Typed schemas | Aspirational | PASS | All 5 phases use explicit pipe-tables with sub-skill vocabulary (same quality as V-04; Phase 5 adds "Shared state hit?" column beyond V-04) |
| C-13 Severity × blast radius | Aspirational | PASS | Calibration table: separate Blast radius and Severity columns; CONSOLIDATE: distinct labeled fields per finding; "Do not merge blast radius and severity. They are separate fields. This is not optional." |
| C-14 Calibration block | Aspirational | PASS | "PHASE 6 -- CALIBRATION BLOCK" named after Phase 5, before CONSOLIDATE; 6a–6d re-evaluate blast radius against findings. Adds: "The census described what you expected to find. The findings describe what you actually found. Calibration reconciles the two." |

**Aspirational passed:** C-09, C-11, C-12, C-13, C-14 = 5/6 → (5/6)×10 = 8.33 → **8**
**Score: 50 + 30 + 8 = 88**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Total | Fails |
|-----------|-----------|-------------|--------------|-------|-------|
| V-01 | 50 | 30 | 8 | **88** | C-10 |
| V-02 | 50 | 30 | 7 | **87** | C-10, C-11 |
| **V-03** | **50** | **30** | **10** | **90** | none |
| **V-04** | **50** | **30** | **10** | **90** | none |
| V-05 | 50 | 30 | 8 | **88** | C-10 |

**Ranking:** V-03 = V-04 (90) > V-01 = V-05 (88) > V-02 (87)

---

## Prediction vs. Actuals

Predicted: V-04 >= V-05 > V-01 > V-02 > V-03
Actual: V-03 = V-04 > V-01 = V-05 > V-02

The prediction inverted V-03 (expected last, tied first). The rubric writer who authored v3 validated "V-03 pattern" as the named source for C-14, and Q5's component naming instruction provides a reliable C-10 path without a formal census. V-03's risk was assessed as C-14 uncertainty, but the rubric explicitly closes that uncertainty. V-05 was predicted above V-01 but they tie — V-05's inertia framing adds no rubric-scorable signal, and V-05 shares V-01's C-10 gap (missing the census-component verdict qualifier that V-04 nails).

---

## Excellence Signals (V-03 and V-04)

**V-04: Explicit census component name in verdict instruction**
The "(using its census component name)" qualifier in the verdict line is a one-phrase patch that closes C-10 cleanly. V-01 and V-05 have nearly identical structure but omit this qualifier, costing them 2 aspirational points. Lesson: the verdict instruction must name both what to cite (the finding) and what to name (the component).

**V-03: Interrogative calibration as a path to C-10 via Q5**
By embedding "Name the component from your findings that it touches" directly into Q5, V-03 forces component identification before the verdict is written — without a formal census. The interrogative register achieves C-14 compliance (named calibration phase) and C-10 compliance (Q5 anchors the verdict) simultaneously through question structure rather than phase architecture.

**V-04/V-05 Phase 6c: Clean zone identification**
Step 6c ("Identify census components that appear in zero findings. These are clean zones. Note them explicitly — absence of evidence is evidence of absence for those components") inverts the finding direction. The usual signal is "here is what's wrong." Clean zones add "here is what is confirmed safe." V-05 elevates this to a dedicated CONSOLIDATE section. No current criterion rewards this pattern — it is a candidate for C-15.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Clean zone identification: explicitly listing census components with zero findings provides proof-of-absence alongside blast radius ranking, enabling implementation teams to know which components are cleared for development (V-04 Phase 6c, V-05 CONSOLIDATE section)"]}
```
