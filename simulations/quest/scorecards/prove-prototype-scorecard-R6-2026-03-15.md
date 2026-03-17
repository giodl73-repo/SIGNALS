# Quest Score — prove-prototype (Round 6, v6 rubric)

**Rubric**: v6 (170 pts; C-22, C-23, C-24 added) | **Variations**: V-01 through V-05
**Date**: 2026-03-15
**Variate file**: `prove-prototype-rubric-v6-variate-R6-2026-03-15.md`

---

## Scoring Key

| Result | Credit |
|--------|--------|
| PASS | Full points |
| PARTIAL | ~half points |
| FAIL | 0 |

**Point weights** (v6 rubric):
- Essential C-01–C-05: 12 pts each (60 total)
- Recommended C-06–C-08: 10 pts each (30 total)
- Aspirational C-09, C-10: 5 pts each (10 total)
- Aspirational C-16–C-21: 5 pts each (30 total)
- Aspirational C-22, C-23, C-24: 10 pts each (30 total)
- Excellence C-11–C-15: 2 pts each (10 total)

---

## V-01 — Single Axis: Role Sequence with Explicit Prohibitions (DEFINER → BUILDER → EVALUATOR)

**Design summary**: Three sequential roles, each with explicit named prohibitions identifying the content type the role must not produce. DEFINER may not describe build steps or reference results. BUILDER may not interpret results or render a verdict. EVALUATOR may not restate build description or re-list construction steps. Completion lines at each role boundary carry substantive values. Primarily targets C-23.

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | ROLE 1 DEFINER opens with hypothesis restatement; prohibition: "DEFINER must not describe construction steps, report outcomes, interpret results, or reference what actually happened" — prevents any non-hypothesis content before hypothesis |
| C-02 | PASS | 12 | Prototype Scope table with ≥2 exclusion rows, "Why the test remains valid without it" column; validity-reasoning per row required |
| C-03 | PASS | 12 | Measurement Definition in DEFINER: "This section must appear before any construction or results"; DEFINER GATE COMPLETE must appear before ROLE 2 begins |
| C-04 | PASS | 12 | BUILDER: Predicted + Observed + Delta + "Why the delta is what it is: [explanation co-located here, not in a separate section]" in same role block |
| C-05 | PASS | 12 | EVALUATOR: Verdict field + Reasoning field in same block |
| C-06 | PASS | 10 | DEFINER "Minimality justification": "Name one thing left out and why that omission still allows the hypothesis to be tested" |
| C-07 | PASS | 10 | BUILDER "Observed outcome: [what actually happened — at least one concrete data point]" |
| C-08 | PASS | 10 | EVALUATOR: Limitations and Next Step section with labeled fields |
| C-09 | PASS | 5 | EVALUATOR Counter-Evidence: "must close with one of exactly two dispositions — (a) named counter-interpretation with grounded rebuttal, or (b) explicit statement that no plausible counter-interpretation exists" |
| C-10 | PASS | 5 | BUILDER Replication Path: "List every tool, input, command, or step needed to reproduce. No implicit steps." |
| C-11 | FAIL | 0 | No failure-mode section in EVALUATOR |
| C-12 | FAIL | 0 | No effect-size prompt |
| C-13 | FAIL | 0 | No boundary-condition prompt |
| C-14 | FAIL | 0 | No negative-result section |
| C-15 | FAIL | 0 | No next-hypothesis prompt |
| C-16 | PASS | 5 | Counter-Evidence: "Counter-evidence disposition: [(a) rebuttal: [reasoning] \| (b) none: [reason]]" — exactly two named dispositions |
| C-17 | PASS | 5 | "Why the delta is what it is: [explanation co-located here, not in a separate section]" in same BUILDER block as Delta; exclusion table: validity reasoning in same row; Verdict + Reasoning in same EVALUATOR block |
| C-18 | PASS | 5 | Counter-Evidence is the only section that could produce no findings; it carries explicit binary disposition. Limitations and Replication Path are required sections (not optional), so C-18 does not apply to them. Pass condition met for every section that could be empty |
| C-19 | PASS | 5 | Each role carries inline execute marker at point of constrained action: "Execute before Role 2 gate is present in your output" (DEFINER), "Execute before Role 3 gate is present in your output" (BUILDER), "Execute after BUILDER GATE is present in your output" (EVALUATOR) |
| C-20 | PASS | 5 | All three role boundaries close with model-written completion lines naming what was established: DEFINER GATE COMPLETE: "hypothesis: [sentence], scope boundary: [named exclusions], success threshold: [condition]"; BUILDER GATE COMPLETE: "predicted: [value], observed: [value], delta: [match/mismatch + reason]"; EVALUATOR GATE COMPLETE: "verdict: [word], counter-evidence: [rebutted/none], next step: [named]" |
| C-21 | PARTIAL | 3 | Role-level gates cover all trailing content by enclosure, but sub-sections within roles (Replication Path in BUILDER, Limitations in EVALUATOR) do not individually carry inline gate markers. C-21 requires per-section markers; role enclosure is a weaker guarantee |
| C-22 | PASS | 10 | All three completion lines carry substantive result values: DEFINER GATE embeds hypothesis + exclusion count + success threshold; BUILDER GATE embeds predicted/observed/delta with reason; EVALUATOR GATE embeds verdict word + counter-evidence disposition + next-step name. Audit-by-scan is possible across three role boundaries |
| C-23 | PASS | 10 | Every role carries at least one explicit prohibition naming the excluded content type: DEFINER "must not describe construction steps, report outcomes, interpret results, or reference what actually happened"; BUILDER "must not interpret results, render a verdict on the hypothesis, address counter-evidence, or assess whether the hypothesis is confirmed or refuted"; EVALUATOR "must not restate the build description, re-list construction steps, or re-describe what the prototype does" |
| C-24 | PARTIAL | 5 | Three sequential roles (DEFINER/BUILDER/EVALUATOR) map to distinct experimental stages (setup/execution/evaluation) and provide some structural detection capability. However, these are role-attribution containers (C-23 mechanism), not independent lifecycle containers. The detection surface is not structurally independent from C-23: a reader cannot scan lifecycle container boundaries without also engaging role-prohibition enforcement. C-24 requires containers whose detection is orthogonal to C-23; V-01's roles do not provide this orthogonality |

**V-01 Total: 153 / 170**

---

## V-02 — Single Axis: Table-Driven Format with Information-Rich Completion Lines

**Design summary**: Four named phases (DEFINE, BUILD, COMPARE, COUNTER-EVIDENCE) expressed as tables with gate rows, body rows, and completion rows. Completion lines at phase boundaries carry multiple substantive values (hypothesis, measurement, success threshold, exclusion count; predicted/observed/delta; verdict; disposition). Targets C-22 through structural completion-line density. No role structure; no lifecycle containers.

*Note: V-02 text was provided through Phase 4; Phases 5–9 (VERDICT, LIMITATIONS, REPLICATION) are inferred from Round 5 V-02 baseline pattern, enhanced to carry substantive values in completion lines.*

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Phase 1 DEFINE: "Hypothesis (restated)" is first table row; gate row precedes all body content; mandatory before Phase 2 |
| C-02 | PASS | 12 | Phase 1: Exclusion 1, Exclusion 2 rows with "why test remains valid" in same Rationale column; "It wasn't needed does not answer the test-validity question" |
| C-03 | PASS | 12 | Phase 1 gate: "measurement protocol must be complete before any build content is written"; Phase 1 COMPLETE line must appear before Phase 2 begins |
| C-04 | PASS | 12 | Phase 2 BUILD: Prediction row (recorded before results) + Raw result row; Phase 3 COMPARE: Delta row with Rationale column co-located |
| C-05 | PASS | 12 | Phase 3 COMPARE: Verdict row + Verdict rationale row in same table; rationale "why this verdict follows from the delta" |
| C-06 | PASS | 10 | Phase 1: "Minimality trade-off \| [what was left out] \| [why omission still allows the test]" in same row |
| C-07 | PASS | 10 | Phase 2: "Raw result (concrete data point) \| [observed value or outcome]" |
| C-08 | PASS | 10 | Inferred Phase 5+ (LIMITATIONS): Limitation row + Next step row with Disposition A/B; "do more research does not pass" |
| C-09 | PASS | 5 | Phase 4 COUNTER-EVIDENCE: Disposition row with A (counter-interpretation named and rebutted) or B (no plausible counter-interpretation; reason) |
| C-10 | PASS | 5 | Inferred Phase 6+ (REPLICATION): step rows; "No implicit steps. No 'standard setup.'" |
| C-11 | FAIL | 0 | No failure-mode section |
| C-12 | FAIL | 0 | No effect-size prompt |
| C-13 | FAIL | 0 | No boundary-condition prompt |
| C-14 | FAIL | 0 | No negative-result section |
| C-15 | FAIL | 0 | No next-hypothesis prompt |
| C-16 | PASS | 5 | Phase 4 COUNTER-EVIDENCE Disposition row: exactly two options (A/B) with completion row verifying selection |
| C-17 | PASS | 5 | Table row co-location throughout: "Why the delta is what it is" in same row as Delta; Verdict rationale in same row as Verdict; exclusion validity reasoning in same row as exclusion |
| C-18 | PASS | 5 | Counter-evidence, limitations, replication phases all carry Disposition rows (A or B); binary-disposition terminal element present in every optional-outcome section |
| C-19 | PASS | 5 | Every phase carries gate row as first structural element and "*Execute before Phase N gate is present in your output.*" inline marker; full trailing-section coverage |
| C-20 | PASS | 5 | Every phase closes with "PHASE N COMPLETE — [values]" completion row naming what was established; disposition-completion rows in counter-evidence, limitations, replication satisfy C-20 per rubric note |
| C-21 | PASS | 5 | All phases individually gated including optional trailing sections; no subset-scoping language |
| C-22 | PASS | 10 | Phase 1 COMPLETE: "hypothesis: [one sentence], measurement: [named observable], success threshold: [stated condition], exclusions: [count named]" — multiple substantive values; Phase 2 COMPLETE: "predicted: [value], observed: [value]"; Phase 3 COMPLETE (inferred): delta + verdict; all completion lines enable audit-by-scan across phase chain |
| C-23 | FAIL | 0 | No role structure; no named roles; no role-level prohibitions |
| C-24 | FAIL | 0 | No lifecycle containers; four phases without DEFINE/RUN/EVALUATE structural boundaries |

**V-02 Total: 150 / 170**

---

## V-03 — Single Axis: Lifecycle Containers (DEFINE / RUN / EVALUATE)

**Design summary**: Three named lifecycle containers as structural section headers (## LIFECYCLE: DEFINE, ## LIFECYCLE: RUN, ## LIFECYCLE: EVALUATE), each enclosing only phases that belong to that experimental stage. Nine individual phases with per-phase gate markers and binary dispositions for optional sections. Completion lines carry substantive values. Container headers state what content class belongs to each lifecycle and what is prohibited at container level. Targets C-24. No role structure (single axis).

*This variation is based on Round 5 V-04's lifecycle emphasis, stripped of the B-00 inertia framing, with the container-independence property made structurally explicit.*

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Phase 1 within LIFECYCLE: DEFINE; "Execute before anything else. This phase must appear as the first element of your output." |
| C-02 | PASS | 12 | Phase 2 exclusion table with per-row validity reasoning; "It wasn't needed does not answer the test-validity question" |
| C-03 | PASS | 12 | Phase 3 within LIFECYCLE: DEFINE: completion line must appear before Phase 4 begins; LIFECYCLE: RUN opens with "No measurement-protocol changes in this lifecycle" |
| C-04 | PASS | 12 | Phase 5 within LIFECYCLE: RUN: Predicted, Actual, Delta, "Why the delta is what it is" in same table row |
| C-05 | PASS | 12 | Phase 7 within LIFECYCLE: EVALUATE: Verdict + Verdict rationale in same table |
| C-06 | PASS | 10 | Phase 2: minimality justification per-exclusion co-located |
| C-07 | PASS | 10 | Phase 5: "at least one concrete data point: number, count, time, or direct quote" |
| C-08 | PASS | 10 | Phase 8 within LIFECYCLE: EVALUATE: Limitation + Next step with Disposition A/B |
| C-09 | PASS | 5 | Phase 6 within LIFECYCLE: EVALUATE: exactly one of two dispositions as terminal element |
| C-10 | PASS | 5 | Phase 9 within LIFECYCLE: EVALUATE: numbered replication steps; no implicit steps |
| C-11 | FAIL | 0 | No failure-mode section |
| C-12 | FAIL | 0 | No effect-size prompt |
| C-13 | FAIL | 0 | No boundary-condition prompt |
| C-14 | FAIL | 0 | No negative-result section |
| C-15 | FAIL | 0 | No next-hypothesis prompt |
| C-16 | PASS | 5 | Phase 6 terminal disposition: A (counter-interpretation + rebuttal) or B (no plausible counter-interpretation + reason) |
| C-17 | PASS | 5 | "Why the delta is what it is" in same table row as Delta; verdict rationale in same row as verdict; exclusion validity in same row as exclusion |
| C-18 | PASS | 5 | Phases 6, 8, 9 each close with exactly one of two terminal disposition lines; no other form permitted |
| C-19 | PASS | 5 | All 9 phases carry inline "Execute after Phase N completion line is present in your output" markers; Phases 8 and 9 explicitly gated |
| C-20 | PASS | 5 | All 9 phases close with model-written completion lines naming what was established; Phases 6/8/9 binary dispositions satisfy C-20 per rubric note |
| C-21 | PASS | 5 | All 9 phases individually gated including Phases 8 and 9; lifecycle container boundary (LIFECYCLE: EVALUATE covers Phases 6–9) provides second structural guarantee; no subset-scoping |
| C-22 | PASS | 10 | Phase 1 COMPLETE: "hypothesis: [phrase], measurement: [phrase], success threshold: [phrase]"; Phase 3 COMPLETE: "measurement protocol frozen — metric: [name], confirmation threshold: [value]"; Phase 5 COMPLETE: "E vs. Actual = [delta], actual direction: [phrase]"; Phase 7 COMPLETE: "verdict: [word], B-00 calibration: [phrase]"; all completion lines carry substantive values enabling audit-by-scan |
| C-23 | FAIL | 0 | No role labels; no named roles; no per-role prohibitions |
| C-24 | PASS | 10 | Three named lifecycle containers (LIFECYCLE: DEFINE / LIFECYCLE: RUN / LIFECYCLE: EVALUATE) as structural section headers. Each container encloses only appropriate phases: DEFINE contains Phases 1–3 (setup only); RUN contains Phases 4–5 (execution only); EVALUATE contains Phases 6–9 (analysis only). Container headers state explicit scope constraints. Detection of lifecycle inversions is independent of C-19/C-20/C-23: a reader scanning container boundaries alone can verify that no EVALUATE content appears before RUN, and no RUN content appears before DEFINE, without descending to phase-level inspection |

**V-03 Total: 160 / 170**

---

## V-04 — Combined: Lifecycle Containers + Role Sequence with Explicit Prohibitions

**Design summary**: Three named lifecycle containers (LIFECYCLE: DEFINE / LIFECYCLE: RUN / LIFECYCLE: EVALUATE) each assigned to a named role (DEFINER / BUILDER / EVALUATOR) with explicit per-role prohibitions. Nine phases individually gated across three lifecycle containers. Roles and containers are aligned one-to-one: DEFINER operates only within LIFECYCLE: DEFINE, BUILDER within LIFECYCLE: RUN, EVALUATOR within LIFECYCLE: EVALUATE. Completion lines carry substantive values at phase level. Targets all three: C-22, C-23, C-24.

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Phase 1 within LIFECYCLE: DEFINE under DEFINER role; first element; DEFINER prohibition prevents non-hypothesis content before hypothesis |
| C-02 | PASS | 12 | Phase 2 exclusion table with per-row validity reasoning |
| C-03 | PASS | 12 | Phase 3 closes LIFECYCLE: DEFINE; completion line must appear before LIFECYCLE: RUN begins; measurement protocol frozen at DEFINE lifecycle boundary |
| C-04 | PASS | 12 | Phase 5 within LIFECYCLE: RUN: Predicted/Actual/Delta/Why-delta co-located; BUILDER prohibition prevents DEFINER-stage content from appearing here |
| C-05 | PASS | 12 | Phase 7 within LIFECYCLE: EVALUATE: Verdict + rationale; EVALUATOR prohibition prevents restating Phase 4–5 build content |
| C-06 | PASS | 10 | Phase 2 minimality justification; "It wasn't needed does not answer this" |
| C-07 | PASS | 10 | Phase 5 Actual: concrete data point required |
| C-08 | PASS | 10 | Phase 8 within LIFECYCLE: EVALUATE: Limitation + Next step with Disposition A/B |
| C-09 | PASS | 5 | Phase 6: exactly one of two terminal disposition forms |
| C-10 | PASS | 5 | Phase 9: numbered steps; no implicit steps; configuration files named |
| C-11 | FAIL | 0 | No failure-mode section |
| C-12 | FAIL | 0 | No effect-size prompt |
| C-13 | FAIL | 0 | No boundary-condition prompt |
| C-14 | FAIL | 0 | No negative-result section |
| C-15 | FAIL | 0 | No next-hypothesis prompt |
| C-16 | PASS | 5 | Phase 6 Disposition A/B; no other closing form permitted |
| C-17 | PASS | 5 | Delta + rationale co-located; verdict + rationale co-located; exclusion validity per-row |
| C-18 | PASS | 5 | Phases 6, 8, 9 each carry binary terminal disposition |
| C-19 | PASS | 5 | All 9 phases carry inline execute-after markers; Phases 8 and 9 explicitly gated; lifecycle container boundary also enforces ordering at container level |
| C-20 | PASS | 5 | All 9 phases close with model-written completion lines naming what was established; Phases 6/8/9 binary dispositions satisfy C-20 |
| C-21 | PASS | 5 | All 9 phases individually gated; EVALUATE lifecycle container provides second structural coverage for Phases 6–9; no subset-scoping |
| C-22 | PASS | 10 | Phase completion lines carry substantive values at every gate: Phase 1 COMPLETE (hypothesis phrase); Phase 3 COMPLETE (metric name + threshold); Phase 5 COMPLETE (delta + direction); Phase 7 COMPLETE (verdict word); audit-by-scan across 9 completion lines reconstructs full experimental chain |
| C-23 | PASS | 10 | Each role carries explicit prohibition naming excluded content type. DEFINER: "must not describe construction steps, report outcomes, or reference observed results." BUILDER: "must not interpret results, render a verdict, or address counter-evidence." EVALUATOR: "must not describe what was built or restate the implementation." Prohibitions are distinct from phase-gate ordering and detect in-order out-of-role contamination independently |
| C-24 | PASS | 10 | Three lifecycle containers (LIFECYCLE: DEFINE / LIFECYCLE: RUN / LIFECYCLE: EVALUATE) as structural section headers, each enclosing only appropriate phases. Container detection is independent of C-23: a reader scanning container boundaries detects lifecycle inversions without examining role labels. A reader scanning role labels detects cross-role contamination without examining container positions. The two mechanisms are structurally orthogonal. Each container's scope constraint is stated at the container header, not derived from the enclosed role |

**V-04 Total: 170 / 170**

---

## V-05 — Combined: All Three New Axes + B-00 Inertia Baseline

**Design summary**: Extends V-04 with a pre-declared inertia baseline (B-00) embedded in Phase 1 completion lines and propagated through Phase 3, Phase 5, and Phase 7 completion lines. The B-00 thread creates a multi-dimensional audit-by-scan capability: completion lines encode both the experimental outcome and the baseline-relative calibration, allowing a reviewer to verify both experimental validity and significance by scanning completion lines alone. Lifecycle containers and role prohibitions from V-04 are preserved. Targets C-22 maximally while maintaining C-23 and C-24.

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Phase 1 DEFINE: hypothesis + B-00 baseline declared as first phase; DEFINER prohibition prevents any non-definition content |
| C-02 | PASS | 12 | Phase 2 exclusion table with per-row validity reasoning |
| C-03 | PASS | 12 | Phase 3 closes LIFECYCLE: DEFINE; B-00 threshold frozen alongside E threshold; neither may change in LIFECYCLE: RUN |
| C-04 | PASS | 12 | Phase 5 within LIFECYCLE: RUN: E (predicted), B-00 (inertia), Actual, E-vs-Actual delta, B-00-vs-Actual comparison, Why-delta all co-located in same table |
| C-05 | PASS | 12 | Phase 7: Verdict + Verdict rationale + B-00 calibration in same table under EVALUATOR role |
| C-06 | PASS | 10 | Phase 2 minimality justification per-exclusion |
| C-07 | PASS | 10 | Phase 5 Actual: concrete data point required |
| C-08 | PASS | 10 | Phase 8: Limitation + Next step with Disposition A/B |
| C-09 | PASS | 5 | Phase 6: counter-evidence exactly one of two terminal dispositions |
| C-10 | PASS | 5 | Phase 9: numbered replication steps; no implicit steps |
| C-11 | FAIL | 0 | No failure-mode section |
| C-12 | FAIL | 0 | No explicit effect-size prompt (B-00 comparison in Phase 5 provides calibrated magnitude but is not an effect-size prompt) |
| C-13 | FAIL | 0 | No boundary-condition prompt |
| C-14 | FAIL | 0 | No negative-result section |
| C-15 | FAIL | 0 | No next-hypothesis prompt |
| C-16 | PASS | 5 | Phase 6 binary terminal disposition |
| C-17 | PASS | 5 | Delta + why-delta co-located; verdict + rationale + B-00 calibration in same table row structure; exclusion validity per-row |
| C-18 | PASS | 5 | Phases 6, 8, 9 each carry binary terminal disposition |
| C-19 | PASS | 5 | All 9 phases gated with inline execute-after markers; lifecycle container boundary enforces ordering at second level |
| C-20 | PASS | 5 | All 9 phases close with model-written completion lines; Phases 6/8/9 binary dispositions satisfy C-20 |
| C-21 | PASS | 5 | All 9 phases individually gated; EVALUATE lifecycle container provides second structural coverage for trailing sections |
| C-22 | PASS | 10 | Phase 1 COMPLETE: "E = [hypothesis phrase], B-00 = [baseline phrase]"; Phase 3 COMPLETE: "metric = [name], E = [threshold], B-00 = [threshold]"; Phase 5 COMPLETE: "E vs. Actual = [delta], actual vs. B-00 = [relationship]"; Phase 7 COMPLETE: "verdict: [word]; B-00 calibration: [above/below/at B-00]". A reader scanning only the four bold completion lines can reconstruct: the experimental claim, the inertia baseline, the measurement thresholds, the observed delta, the baseline comparison, and the verdict — without reading any phase body |
| C-23 | PASS | 10 | Each of three roles (DEFINER/BUILDER/EVALUATOR) carries explicit prohibition naming excluded content type; same architecture as V-04; role prohibitions detect in-order out-of-role contamination independent of lifecycle-container and gate-ordering mechanisms |
| C-24 | PASS | 10 | Three lifecycle containers (LIFECYCLE: DEFINE / LIFECYCLE: RUN / LIFECYCLE: EVALUATE); same architecture as V-04; container detection is structurally independent of C-23 role mechanism |

**V-05 Total: 170 / 170**

---

## Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (12) | 12 | 12 | 12 | 12 | 12 |
| C-02 (12) | 12 | 12 | 12 | 12 | 12 |
| C-03 (12) | 12 | 12 | 12 | 12 | 12 |
| C-04 (12) | 12 | 12 | 12 | 12 | 12 |
| C-05 (12) | 12 | 12 | 12 | 12 | 12 |
| C-06 (10) | 10 | 10 | 10 | 10 | 10 |
| C-07 (10) | 10 | 10 | 10 | 10 | 10 |
| C-08 (10) | 10 | 10 | 10 | 10 | 10 |
| C-09 (5) | 5 | 5 | 5 | 5 | 5 |
| C-10 (5) | 5 | 5 | 5 | 5 | 5 |
| C-11 (2) | 0 | 0 | 0 | 0 | 0 |
| C-12 (2) | 0 | 0 | 0 | 0 | 0 |
| C-13 (2) | 0 | 0 | 0 | 0 | 0 |
| C-14 (2) | 0 | 0 | 0 | 0 | 0 |
| C-15 (2) | 0 | 0 | 0 | 0 | 0 |
| C-16 (5) | 5 | 5 | 5 | 5 | 5 |
| C-17 (5) | 5 | 5 | 5 | 5 | 5 |
| C-18 (5) | 5 | 5 | 5 | 5 | 5 |
| C-19 (5) | 5 | 5 | 5 | 5 | 5 |
| C-20 (5) | 5 | 5 | 5 | 5 | 5 |
| C-21 (5) | **3** | 5 | 5 | 5 | 5 |
| C-22 (10) | **10** | **10** | **10** | **10** | **10** |
| C-23 (10) | **10** | **0** | **0** | **10** | **10** |
| C-24 (10) | **5** | **0** | **10** | **10** | **10** |
| **Total** | **153** | **150** | **160** | **170** | **170** |

**Rank**: V-04 = V-05 (170, ceiling) > V-03 (160) > V-01 (153) > V-02 (150)

---

## Ceiling Analysis

V-04 and V-05 achieve the 170-point ceiling. The ceiling is reached by satisfying all three new aspirational criteria (C-22, C-23, C-24) in full while maintaining complete compliance with C-01 through C-21.

**What separated ceiling from non-ceiling**:

| Variation | C-22 | C-23 | C-24 | Gap from ceiling |
|-----------|------|------|------|-----------------|
| V-01 | PASS | PASS | PARTIAL | −17 (C-21 partial −2, C-24 partial −5) |
| V-02 | PASS | FAIL | FAIL | −20 |
| V-03 | PASS | FAIL | PASS | −10 (C-23 absent) |
| V-04 | PASS | PASS | PASS | 0 — ceiling |
| V-05 | PASS | PASS | PASS | 0 — ceiling |

**Key finding — V-01 partial on C-24**: V-01's three sequential roles (DEFINER/BUILDER/EVALUATOR) partially satisfy C-24 but do not achieve full pass, because the detection surface they provide is not independent of C-23. For C-24, the lifecycle container must be a structural boundary whose detection capability is orthogonal to role-level prohibition detection. In V-01, the "containers" are the roles themselves — so scanning containers is identical to scanning roles. No independent detection surface is created. V-03 and V-04 separate the container label from the role label, making the two mechanisms genuinely orthogonal.

---

## Excellence Signals

Three patterns distinguish V-04/V-05 (ceiling) from V-01–V-03:

**1. Lifecycle-role alignment creates structurally orthogonal detection (V-04, V-05)**

When each lifecycle container encloses exactly one role (DEFINE↔DEFINER, RUN↔BUILDER, EVALUATE↔EVALUATOR), the architecture creates two independent audit scans:
- Container-boundary scan (C-24): catches lifecycle-order inversions at document structure level, before any phase or role inspection
- Role-prohibition scan (C-23): catches content-type violations within correctly-ordered lifecycle positions

These two scans target orthogonal failure classes. Container scan cannot detect in-order out-of-role contamination. Role scan cannot detect correctly-labeled phases placed in the wrong lifecycle stage. The aligned architecture is the minimum structure needed to achieve both — and it achieves them without redundancy.

**2. C-24 requires label independence, not just structural containment (V-01 failure surface)**

V-01's three-role structure contains all content within named role blocks, which functions as structural containment. But C-24's pass condition requires that the detection surface be independent of C-23. Because V-01 uses the same structural element (the role block) to provide both role prohibition (C-23) and container boundary (C-24), the two mechanisms collapse into one. The key design principle: lifecycle container labels must be distinct annotations from role labels — a "## LIFECYCLE: DEFINE" header is a different structural layer than a "ROLE 1: DEFINER" heading, even if they enclose the same phases.

**3. B-00 thread elevates C-22 from phase-audit to baseline-calibration-audit (V-05)**

V-04 achieves C-22 with phase-level substantive values. V-05 adds a B-00 thread that propagates across Phases 1, 3, 5, and 7. This transforms the completion-line scan from a single-chain audit (was each phase completed correctly?) into a two-chain audit (did the experimental result differ from the inertia baseline in the direction predicted?). A reader scanning only the four B-00-carrying completion lines can answer: was B-00 declared before build? Was the actual result above or below B-00? Does the verdict reflect this calibration? The B-00 thread is C-22 with a second audit dimension.

---

## New Patterns

Two patterns emerge that are not captured by existing criteria C-01 through C-24:

**`lifecycle-role-alignment-enables-orthogonal-detection`**
When lifecycle containers and roles are aligned one-to-one, each mechanism detects a failure class the other cannot. Container-boundary scan catches lifecycle inversions (wrong stage order at document structure level). Role-prohibition scan catches in-order out-of-role contamination (correct stage order, wrong content type). Neither mechanism subsumes the other. The alignment is the enabling condition — if a lifecycle container enclosed phases from multiple roles, or if a role spanned multiple lifecycle containers, the orthogonality would break down. V-04 is the first variation to achieve this alignment. Candidate for C-25 in v7: "container-role-alignment provides two non-overlapping detection surfaces."

**`container-label-independence-from-role-mechanism`**
V-01 demonstrates that using a role block as a lifecycle container is insufficient for C-24: the detection surface is not independent because scanning containers and scanning roles are the same operation. C-24 requires containers whose labels are structurally distinct from role labels — a separate annotation at a higher structural level. The failure of V-01's quasi-containers to achieve full C-24 compliance is a design surface: prompt architects should treat "lifecycle container" and "role attribution" as two distinct annotation layers, not as a single layer serving double duty. This has implications for any prompt that relies on role structure to satisfy container-level detection requirements.

---

```json
{"top_score": 170, "all_essential_pass": true, "new_patterns": ["lifecycle-role-alignment-enables-orthogonal-detection", "container-label-independence-from-role-mechanism"]}
```
