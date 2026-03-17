# Quest Score — prove-prototype (Round 5, v5 rubric)

**Rubric**: v5 (140 pts; C-20 and C-21 added) | **Variations**: V-01 through V-05
**Date**: 2026-03-15
**Variate file**: `prove-prototype-rubric-v5-variate-R5-2026-03-15.md`

---

## Scoring Key

| Result | Credit |
|--------|--------|
| PASS | Full points |
| PARTIAL | ~half points |
| FAIL | 0 |

**Point weights** (v5 rubric):
- Essential C-01–C-05: 12 pts each (60 total)
- Recommended C-06–C-08: 10 pts each (30 total)
- Aspirational C-09, C-10, C-16–C-21: 5 pts each (40 total)
- Excellence C-11–C-15: 2 pts each (10 total)

---

## V-01 — Single-axis: Role Sequence (DEFINER → EXPERIMENTER → EVALUATOR)

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Phase 1: `*DEFINER. Execute before anything else. This phase must appear as the first element of your output. Nothing precedes it.*`; hypothesis precedes all build/result content |
| C-02 | PASS | 12 | Phase 2 table requires ≥2 exclusions; col 2 is "Why the hypothesis remains testable without it"; "it doesn't matter" phrasing not accepted |
| C-03 | PASS | 12 | Phase 3: "This phase must be complete before Phase 4 begins. The measurement protocol is frozen at the end of this phase — EXPERIMENTER may not modify it." + PHASE 3 COMPLETE completion line before Phase 4 |
| C-04 | PASS | 12 | Phase 5 table: Predicted, Actual, Delta ("do not leave this for the reader to compute"), "Why the delta is what it is" co-located in same block |
| C-05 | PASS | 12 | Phase 7: Verdict + Verdict rationale in same table; rationale "not a restatement of Phase 5" |
| C-06 | PASS | 10 | Phase 2 per-exclusion "Why the hypothesis remains testable without it" inline; "it wasn't needed does not answer this question" |
| C-07 | PASS | 10 | Phase 5 Actual: "include at least one concrete data point: a number, a count, a time, or a direct quote from output" |
| C-08 | PASS | 10 | Phase 8: Limitation + Next Step in table; Disposition A or B terminal |
| C-09 | PASS | 5 | Phase 6 Disposition A: counter-interpretation named + "explain why it does not hold, using evidence from Phase 5" |
| C-10 | PASS | 5 | Phase 9: "No 'etc.' No 'standard setup.' Configuration files named. Environment requirements stated." Numbered list |
| C-11 | PASS | 2 | Role declarations prohibit cross-role content; completion lines require substantive named output before phase advance; table structure enforces populated rows in Phases 2 and 5 |
| C-12 | PASS | 2 | Phase 3 COMPLETE line: "measurement protocol frozen before build: [name the metric and its success condition]"; temporal evidence in output |
| C-13 | PASS | 2 | Phase 5: Delta row: "predicted − actual; do not leave this for the reader to compute; write '0 — prediction confirmed' if they match" |
| C-14 | PASS | 2 | Phase 7: Verdict rationale is "reasoning that connects the observed delta from Phase 5 to the verdict; this is not a restatement of Phase 5; it is the logical step from evidence to conclusion" |
| C-15 | PASS | 2 | Phase 2 col 2 requires test-validity answer per row; "it wasn't needed does not answer this question" explicit |
| C-16 | PASS | 5 | Phase 6: "Write exactly one of the following two lines as the terminal element of this phase, before Phase 7 begins" — A and B defined; no other form permitted |
| C-17 | PASS | 5 | Phase 5 labeled block: "Why the delta is what it is" in same block as Delta; Phase 7 Verdict + rationale in same table row; Phase 6 counter-interpretation + rebuttal in same structural unit |
| C-18 | PASS | 5 | Phases 6, 8, 9 each close with exactly one of two explicit Disposition lines as terminal element before next phase |
| C-19 | PASS | 5 | All 9 phases carry inline execute-before/after markers. Phase 8: `*EVALUATOR. Execute after Phase 7 completion line is present in your output.*`; Phase 9: `*EVALUATOR. Execute after Phase 8 completion line is present in your output.*` — full trailing-section coverage |
| C-20 | PASS | 5 | All 9 phases close with role-attributed completion lines naming what was established. Phase 1: `**PHASE 1 COMPLETE — hypothesis established: [write the hypothesis in one sentence]**`; Phase 3: `**PHASE 3 COMPLETE — measurement protocol frozen before build: [metric and success condition]**`; Phases 6/8/9 disposition-completion lines satisfy C-20 per rubric note on binary-disposition completion |
| C-21 | PASS | 5 | All 9 phases gated including Phases 8 and 9; no subset-scoping of gate coverage; EVALUATOR execute-after markers explicitly present on Phases 8 and 9 |

**V-01 Total: 140 / 140**

---

## V-02 — Single-axis: Output Format (table-row gate structure)

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Section 1: `**[GATE: first element of output — nothing precedes this section]**` as opening row; hypothesis content follows |
| C-02 | PASS | 12 | Section 2 exclusion rows; "Why test remains valid" in same row; "it wasn't needed does not answer the test-validity question" |
| C-03 | PASS | 12 | Section 3: `**[GATE: execute after Section 2 completion row is present — measurement protocol must be complete before any build content is written]**`; Section 3 COMPLETE row closes measurement before Section 4 |
| C-04 | PASS | 12 | Section 5: Predicted, Actual, Delta, "Why the delta is what it is" all in same table; "do not leave this for the reader to compute" |
| C-05 | PASS | 12 | Section 7: Verdict + Verdict rationale rows; rationale "not a restatement of Section 5; one to three sentences of logical connection" |
| C-06 | PASS | 10 | Section 2 Exclusion rows: "Why test remains valid — reason"; "it wasn't needed does not answer the test-validity question" |
| C-07 | PASS | 10 | Section 5 Actual row: "include at least one concrete data point: number, count, time, or direct quote" |
| C-08 | PASS | 10 | Section 8: Limitation + Next step rows; Disposition row + COMPLETE row |
| C-09 | PASS | 5 | Section 6 Disposition row A: counter-interpretation + "why it does not hold, using Section 5 evidence" |
| C-10 | PASS | 5 | Section 9: Step rows; "No 'etc.' No 'standard setup.' Configuration files named. Environment requirements explicit." |
| C-11 | PASS | 2 | Table structure makes missing rows visually detectable by row-scan; same audit mechanism as content cells; strongest C-11 enforcement of all five variations |
| C-12 | PASS | 2 | `**[SECTION 3 COMPLETE — measurement protocol frozen before build]** [metric name and success condition in one phrase]`; model-written temporal evidence in output |
| C-13 | PASS | 2 | Section 5 Delta row: "predicted − actual; '0 — prediction confirmed' if equal; do not leave this for the reader to compute" |
| C-14 | PASS | 2 | Section 7 Verdict rationale row: "reasoning connecting the Section 5 delta to the verdict; not a restatement of Section 5" |
| C-15 | PASS | 2 | Per-exclusion validity reason in same Exclusion row; "it wasn't needed does not answer the test-validity question" |
| C-16 | PASS | 5 | Section 6 Disposition row: "A: counter-interpretation named and rebutted — OR — B: no plausible counter-interpretation; [reason]"; COMPLETE row verifies selection |
| C-17 | PASS | 5 | Table row co-location throughout: "Why the delta is what it is" in same row as Delta; Verdict rationale in same row as Verdict; Rebuttal in same row as Counter-interpretation |
| C-18 | PASS | 5 | Sections 6, 8, 9 each have Disposition rows terminating with A or B; COMPLETE rows verify selection |
| C-19 | PASS | 5 | All 9 sections have gate rows. Section 8: `**[GATE: execute after Section 7 completion row is present]**`; Section 9: `**[GATE: execute after Section 8 completion row is present]**`; full trailing-section coverage |
| C-20 | PASS | 5 | All 9 sections close with `**[SECTION N COMPLETE — ...]**` rows naming what was established. Section 1: `[restate the hypothesis claim in one phrase]`; Section 3: `[metric name and success condition in one phrase]`; Section 5: `[delta stated in one phrase]`; disposition completion rows in Sections 6/8/9 satisfy C-20 per rubric note |
| C-21 | PASS | 5 | All 9 sections gated; Sections 8 and 9 carry explicit gate rows; no scope-limiting language; complete coverage |

**V-02 Total: 140 / 140**

---

## V-03 — Single-axis: Phrasing Register (formal/structural)

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Phase 1: "The following must be established before any other phase content is produced: the hypothesis to be tested. No build description, result, or observation may precede this phase." |
| C-02 | PASS | 12 | Phase 2 exclusion table; per-row answer to "without this exclusion, can the prototype still test the hypothesis?"; "it wasn't needed is not an explanation" |
| C-03 | PASS | 12 | Phase 3: "The measurement protocol established here is frozen — it may not be modified after Phase 3 closes." + Phase 3 establishment record present before Phase 4 |
| C-04 | PASS | 12 | Phase 5 labeled pairs: Predicted, Actual, Delta ("computed and stated explicitly; the reader does not compute it"), "Why the delta is what it is" in same structural unit |
| C-05 | PASS | 12 | Phase 7: Verdict + Verdict rationale labeled pair; rationale not a restatement of Phase 5 |
| C-06 | PASS | 10 | Phase 2 per-exclusion "The answer must explain which aspect of the test the excluded item does not affect"; "it wasn't needed is not an explanation" |
| C-07 | PASS | 10 | Phase 5 Actual: "at least one concrete data point must be present — a number, a count, a time, or a direct quote from output" |
| C-08 | PASS | 10 | Phase 8: Limitation + Next step labeled pairs; establishment record A or B; "do more research does not establish a next step" |
| C-09 | PASS | 5 | Phase 6: counter-interpretation + "explanation of why the counter-interpretation does not hold, grounded in Phase 5 evidence" |
| C-10 | PASS | 5 | Phase 9: "Every tool, input, command, and configuration is named. No implicit steps. Configuration files named. Environment requirements stated." |
| C-11 | PASS | 2 | Establishment records require naming what was established (not asserting section done); formal language "this record certifies that X was established" enforces non-empty completion artifacts |
| C-12 | PASS | 2 | Phase 3 establishment record: "measurement protocol frozen — metric: [name], confirmation condition: [value]; this record certifies that the measurement protocol was established before any build activity" |
| C-13 | PASS | 2 | Phase 5: "this field is computed and stated explicitly; the reader does not compute it; write '0 — prediction confirmed' if predicted and actual are equal" |
| C-14 | PASS | 2 | Phase 7: verdict rationale "not a restatement of Phase 5; it is the logical step from evidence to conclusion" |
| C-15 | PASS | 2 | Phase 2: per-exclusion answer "in the same structural unit" required; "it wasn't needed is not an explanation" |
| C-16 | PASS | 5 | Phase 6: "The terminal element of Phase 6 is one of the following establishment records — no other closing form is permitted" — A and B both defined |
| C-17 | PASS | 5 | Labeled pairs in Phase 5: "Why the delta is what it is" in same block as Delta; Phase 7: Verdict rationale in same block as Verdict; formal register enforces structural unit co-location throughout |
| C-18 | PASS | 5 | Phases 6, 8, 9: "The terminal element of Phase N is one of the following establishment records — no other closing form is permitted" |
| C-19 | PASS | 5 | All 9 phases carry inline "may not be produced until" constraints. Phase 8: "Phase 8 may not be produced until the Phase 7 establishment record is present." Phase 9: "Phase 9 may not be produced until the Phase 8 establishment record is present." Co-located at the constrained action point; full trailing-section coverage |
| C-20 | PASS | 5 | All 9 phases close with `*Establishment record — Phase N: [what was established; this record certifies...]*`. Phase 1: "hypothesis [state the claim in one phrase; this record certifies...]"; Phase 3: "measurement protocol frozen — metric: [name], confirmation condition: [value]; this record certifies..."; Phases 6/8/9 establishment records are binary dispositions that name the determination reached |
| C-21 | PASS | 5 | All 9 phases carry "may not be produced until" inline constraints including Phases 8 and 9; no subset-scoping; complete coverage |

**V-03 Total: 140 / 140**

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing (B-00)

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Phase 1: "Execute before anything else. This phase must appear as the first element of your output. Nothing precedes it." DEFINE lifecycle container also constrains Phase 1 scope |
| C-02 | PASS | 12 | Phase 2 exclusion table; "Why the hypothesis remains testable without it"; "It wasn't needed does not answer the test-validity question" |
| C-03 | PASS | 12 | Phase 3: "Execute after Phase 2 completion line is present in your output. Measurement protocol must be complete and this completion line present before Phase 4 begins." + PHASE 3 COMPLETE names metric/E/B-00 before build |
| C-04 | PASS | 12 | Phase 5 table: E (predicted), Actual ("at least one concrete data point"), E vs. Actual (delta, "do not leave for reader to compute"), "Why the delta is what it is" co-located in same table |
| C-05 | PASS | 12 | Phase 7: Verdict + Verdict rationale + B-00 calibration in same table; rationale not a restatement of Phase 5 |
| C-06 | PASS | 10 | Phase 2 per-exclusion validity; "It wasn't needed does not answer the test-validity question" |
| C-07 | PASS | 10 | Phase 5 Actual: "at least one concrete data point: number, count, time, or direct quote" |
| C-08 | PASS | 10 | Phase 8: Limitation + Next step; "do more research does not pass; name what to build, test, or change" |
| C-09 | PASS | 5 | Phase 6 Disposition A: counter-interpretation + "why it does not hold, using Phase 5 evidence" |
| C-10 | PASS | 5 | Phase 9: numbered steps; "No implicit steps. Configuration files named." |
| C-11 | PASS | 2 | Lifecycle containers provide detection at two structural levels; completion lines carry named values (E, B-00) preventing category-assertion-only artifacts; table structure in Phase 5 enforces populated rows |
| C-12 | PASS | 2 | Phase 3 completion: "PHASE 3 COMPLETE — measurement protocol and B-00 threshold frozen before build: metric = [name], E = [value], B-00 = [value]"; most information-dense C-12 artifact across all five variations |
| C-13 | PASS | 2 | Phase 5 E vs. Actual row: "E − actual; '0 — prediction confirmed' if equal; do not leave for reader to compute" |
| C-14 | PASS | 2 | Phase 7: Verdict rationale row; "reasoning connecting Phase 5 delta to the verdict — not a restatement of Phase 5"; B-00 calibration row adds additional evaluative dimension |
| C-15 | PASS | 2 | Phase 2: per-exclusion validity in same row; "It wasn't needed does not answer the test-validity question" |
| C-16 | PASS | 5 | Phase 6: "Write exactly one of the following as the terminal element" — Disposition A or B; no other form |
| C-17 | PASS | 5 | Phase 5: "Why the delta is what it is" in same table row as Delta; Phase 7: B-00 calibration and verdict rationale co-located in same table as Verdict; Phase 6: counter-interpretation + rebuttal in same structural unit |
| C-18 | PASS | 5 | Phases 6, 8, 9: "Write exactly one of the following as the terminal element" — binary dispositions; no other form |
| C-19 | PASS | 5 | All 9 phases carry inline "Execute after Phase N completion line is present in your output." Phase 8: "Execute after Phase 7 completion line is present in your output." Phase 9: "Execute after Phase 8 completion line is present in your output." Lifecycle containers additionally bound phase scope at container level |
| C-20 | PASS | 5 | All 9 phases close with `**PHASE N COMPLETE — [...]**` naming what was established. Phases 1, 3, 5, 7 carry B-00 values in completion lines ("E = [...], B-00 = [...]"; "metric = [...], E = [...], B-00 = [...]"; "E vs. Actual = [...], actual vs. B-00 = [...]"; "B-00 calibration: [...]") — richer than any other variation; Phases 6/8/9 binary disposition completions satisfy C-20 per rubric note |
| C-21 | PASS | 5 | All 9 phases gated including Phases 8 and 9; lifecycle container boundary (EVALUATE: Phases 6, 7, 8, 9) provides a second structural guarantee; no subset-scoping language |

**V-04 Total: 140 / 140**

---

## V-05 — Combined: Role Sequence (DESIGNER + ANALYST) + Labeled-Pair Block Format

### Criterion-by-Criterion

| ID | Result | Points | Evidence |
|----|--------|--------|---------|
| C-01 | PASS | 12 | Phase 1: "DESIGNER. Execute before anything else. This phase is the first element of your output." |
| C-02 | PASS | 12 | Phase 2 labeled-pair blocks; per-exclusion "Why test remains valid without it" in same labeled-pair block; "it wasn't needed does not answer this" |
| C-03 | PASS | 12 | Phase 3: "This phase must close and its completion line must appear before Phase 4 begins." + PHASE 3 COMPLETE names metric and success condition |
| C-04 | PASS | 12 | Phase 5 labeled pairs: Predicted, Actual ("at least one concrete data point"), Delta ("computed and stated explicitly"), "Why the delta is what it is" (in same block as Delta per role instructions) |
| C-05 | PASS | 12 | Phase 7: Verdict + Verdict rationale labeled pair; rationale "not a restatement of Phase 5; one to three sentences of logical connection; must appear in the same block as Verdict" |
| C-06 | PASS | 10 | Phase 2 per-exclusion "Why test remains valid without it" in same labeled-pair block; "it wasn't needed does not answer this" |
| C-07 | PASS | 10 | Phase 5 Actual: "at least one concrete data point: number, count, time, or direct quote" |
| C-08 | PASS | 10 | Phase 8 ANALYST: Limitation + Next step labeled pairs; Disposition A or B terminal; "do more research does not pass" |
| C-09 | PASS | 5 | Phase 6 ANALYST Disposition A: Counter-interpretation + Rebuttal in same block |
| C-10 | PASS | 5 | Phase 9 ANALYST: step-labeled pairs; "No implicit steps. Configuration files named. Environment requirements stated." |
| C-11 | PASS | 2 | Role declarations require ANALYST phases to not restate results, prohibit DESIGNER from rendering verdict; completion lines per phase enforce substantive content naming; labeled-pair format makes missing fields visible |
| C-12 | PASS | 2 | Phase 3 completion: "PHASE 3 COMPLETE — DESIGNER: measurement protocol frozen before build — metric: [name], success condition: [value in one phrase]" |
| C-13 | PASS | 2 | Phase 5: "Delta: [predicted − actual; computed and stated explicitly; '0 — prediction confirmed' if equal; do not leave for the reader to compute]" |
| C-14 | PASS | 2 | Phase 7 ANALYST: Verdict rationale "must appear in the same block as Verdict"; "not a restatement of Phase 5" |
| C-15 | PASS | 2 | Phase 2: per-exclusion validity in same labeled-pair block; "it wasn't needed does not answer this" |
| C-16 | PASS | 5 | Phase 6: "Write exactly one of the following as the terminal element of Phase 6" — ANALYST Disposition A or B; no other form |
| C-17 | PASS | 5 | Labeled-pair blocks: "Why the delta is what it is" in same block as Delta (explicitly stated: "must appear in the same block as Delta"); Verdict rationale "must appear in the same block as Verdict"; Counter-interpretation + Rebuttal in same block |
| C-18 | PASS | 5 | Phases 6, 8, 9: "Write exactly one of the following as the terminal element" — binary dispositions; bold-formatted to distinguish from body content |
| C-19 | PASS | 5 | All 9 phases carry inline ANALYST execute-after markers. Phase 8: "ANALYST. Execute after Phase 7 completion line is present in your output." Phase 9: "ANALYST. Execute after Phase 8 completion line is present in your output." Complete trailing-section coverage |
| C-20 | PASS | 5 | All 9 phases close with role-attributed bold completion lines naming what was established. Phase 1: `**PHASE 1 COMPLETE — DESIGNER: hypothesis declared — [hypothesis in one phrase]**`; Phase 3: `**PHASE 3 COMPLETE — DESIGNER: measurement protocol frozen before build — metric: [...], success condition: [...]**`; Phase 5: `**PHASE 5 COMPLETE — DESIGNER: results recorded — delta: [gap in one phrase]**`; Phases 6/8/9 ANALYST disposition completions satisfy C-20 per rubric note |
| C-21 | PASS | 5 | All 9 phases gated including Phases 8 and 9 with ANALYST execute-after markers; no subset-scoping; role declarations additionally identify Phases 6–9 as ANALYST scope |

**V-05 Total: 140 / 140**

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
| C-11 (2) | 2 | 2 | 2 | 2 | 2 |
| C-12 (2) | 2 | 2 | 2 | 2 | 2 |
| C-13 (2) | 2 | 2 | 2 | 2 | 2 |
| C-14 (2) | 2 | 2 | 2 | 2 | 2 |
| C-15 (2) | 2 | 2 | 2 | 2 | 2 |
| C-16 (5) | 5 | 5 | 5 | 5 | 5 |
| C-17 (5) | 5 | 5 | 5 | 5 | 5 |
| C-18 (5) | 5 | 5 | 5 | 5 | 5 |
| C-19 (5) | **5** | **5** | **5** | **5** | **5** |
| C-20 (5) | **5** | **5** | **5** | **5** | **5** |
| C-21 (5) | **5** | **5** | **5** | **5** | **5** |
| **Total** | **140** | **140** | **140** | **140** | **140** |

**Rank**: All five variations — 140 / 140 (ceiling achieved)

---

## Ceiling Analysis

All five variations achieve the 140-point ceiling. This is the direct consequence of the Round 5 design intent: every variation was architected to close the three specific gaps that separated V-02 (130/130) from V-01, V-03, V-04, V-05 in Round 4. The C-19 gap (trailing-section gate coverage) and the new C-20/C-21 criteria were the entire variance surface in Round 4. With all five variations explicitly closing those gaps, the rubric's discrimination ceiling was reached.

**Structural confirmation that the Round 4 gaps are closed in every variation**:

| Variation | Round 4 C-19 | Round 5 C-19 | C-20 mechanism | C-21 coverage |
|-----------|-------------|-------------|----------------|---------------|
| V-01 | PARTIAL (3) — Phases 8–9 ungated | PASS (5) | EVALUATOR execute-after markers on Phases 8–9 + role-attributed completion lines | All 9 phases including EVALUATOR scope |
| V-02 | n/a (new variation) | PASS (5) | Table-row gate + completion rows in all 9 sections | All 9 sections including Sections 8–9 |
| V-03 | n/a (new variation) | PASS (5) | "may not be produced until" constraints + establishment records on all 9 phases | All 9 phases including Phases 8–9 |
| V-04 | n/a (new variation) | PASS (5) | Execute-after on all 9 phases + lifecycle container boundary (EVALUATE covers Phases 6–9) | All 9 phases + lifecycle container framing |
| V-05 | n/a (new variation) | PASS (5) | ANALYST execute-after markers on Phases 8–9 + role-attributed completion lines | All 9 phases including ANALYST scope |

---

## Excellence Signals

With all five variations at ceiling, the excellence signals are differentiation *above* the ceiling — patterns that produce structurally richer outputs than the minimum required by C-19/C-20/C-21:

**1. Information-rich completion lines (V-04)**

V-04's completion lines carry measurable values, not just category labels:
- Phase 1: `E = [experimental claim], B-00 = [baseline]`
- Phase 3: `metric = [name], E = [value], B-00 = [value]`
- Phase 5: `E vs. Actual = [delta], actual vs. B-00 = [relationship]`
- Phase 7: `verdict: [word]; B-00 calibration: [above/below/at B-00]`

This creates a B-00 thread — a verifiable chain from the Phase 1 baseline declaration through to the Phase 7 calibration. Any reader can audit whether the Phase 7 B-00 calibration is consistent with the Phase 3 B-00 threshold and Phase 5 actual by scanning completion lines alone without reading the phase bodies. No other variation creates an equivalent audit-by-completion-scan capability.

**2. Role-attribution as contamination guard (V-01, V-05)**

V-01's three-role architecture prohibits cross-role content explicitly: EVALUATOR "does not describe build activity" and "does not restate results"; EXPERIMENTER "does not redefine metrics." V-05's two-role architecture prohibits ANALYST from describing build activity or restating results. This is a structural prohibition at the role level, independent of and in addition to phase-level ordering gates. A completion line written under the wrong role (e.g., EVALUATOR closing a DEFINE-phase with a build description) is detectable by role-scan before examining section content. Gate-completion enforcement and role-contamination enforcement are orthogonal detection mechanisms; V-01 and V-05 provide both.

**3. Two-level structural hierarchy (V-04)**

V-04's DEFINE/RUN/EVALUATE lifecycle containers create a second structural level above the phase gates. A violation detectable at container level (DEFINE content in RUN, build description in EVALUATE) can be caught without phase-level inspection. This makes the most severe violations (lifecycle-order failures, not just phase-order failures) detectable by document structure scan alone. No other variation provides this dual-level detection.

---

## New Patterns

Three patterns emerge that are not captured by existing criteria C-01 through C-21:

**`completion-line-as-audit-by-scan`**
When completion lines carry measurable values (E, B-00, delta, calibration) rather than category labels, the completion-line sequence becomes an independent audit path: a reviewer can verify cross-phase consistency — e.g., whether the Phase 7 B-00 calibration matches the Phase 3 B-00 threshold — by scanning only the bold completion lines without reading section bodies. This is structurally distinct from C-20 (proof of gate passage) and from C-12 (temporal evidence of measurement-before-build). It is a property that emerges only when completion lines are information-dense. V-04 is the only variation that achieves this. Candidate for C-22 in v6.

**`role-attribution-as-contamination-guard`**
V-01 and V-05 demonstrate that role declarations with explicit cross-role prohibitions add a detection layer orthogonal to phase-gate ordering. Phase gates prevent out-of-order sections; role prohibitions prevent in-order but out-of-role content (e.g., an EVALUATOR section that describes what was built, or an ANALYST section that restates Phase 5 results). These two failure modes are structurally independent. A prompt that has complete phase-gate coverage (C-19) but no role-attribution mechanism cannot detect the second class of failure. Candidate for C-23 in v6.

**`lifecycle-container-as-second-detection-level`**
V-04's DEFINE/RUN/EVALUATE containers create a two-level hierarchy where violations are detectable at the container level before descending to phase-level inspection. This is especially valuable for detecting the most severe category of failure — lifecycle inversions (e.g., evaluation content appearing before build content) — which phase-level gates alone cannot prevent if the phases themselves are correctly labeled but structurally misplaced. No existing criterion (C-19 through C-21) captures this second-level detection capability. Candidate for C-24 in v6.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["completion-line-as-audit-by-scan", "role-attribution-as-contamination-guard", "lifecycle-container-as-second-detection-level"]}
```
