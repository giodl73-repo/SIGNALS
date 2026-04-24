---

# campaign-simulate — Round 1 Scoring (2026-03-17)

## Criterion-by-Criterion Verdicts

| C# | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | All five sub-skills execute | PASS | PASS | PASS | PASS | PASS |
| C-02 | Findings ranked by blast radius | PASS | PASS | PASS | PASS | PASS |
| C-03 | System boundary + severity per finding | PASS | PASS | PASS | PASS | PASS |
| C-04 | At least one spec gap or contract violation | PASS | PASS | PASS | PASS | PASS |
| C-05 | Single synthesized report | PASS | PASS | PASS | PASS | PASS |
| C-06 | Exception paths and edge cases (>= 2) | PASS | PASS | PASS | PASS | PASS |
| C-07 | Findings cross-reference sub-skill | PASS | PASS | PASS | PASS | PASS |
| C-08 | State machine anomalies called out | PASS | PASS | PASS | PASS | PASS |
| C-09 | Test scenario baseline (>= 3 scenarios) | PARTIAL | PARTIAL | **FAIL** | **FAIL** | **PASS** |
| C-10 | Finding IDs (F-NN pattern) | PASS | PASS | PASS | PASS | PASS |

## Score Summary

| Rank | Variation | Composite | Essential Pass |
|------|-----------|-----------|----------------|
| 1 | **V-05** | **100.0** | YES |
| 2 | **V-01** | **97.5** | YES |
| 2 | **V-02** | **97.5** | YES |
| 4 | **V-03** | **95.0** | YES |
| 4 | **V-04** | **95.0** | YES |

All five pass the golden threshold (all essential pass AND composite >= 80).

**Predicted vs. actual leaderboard**: V-05 > V-02 > V-01 > V-03 > V-04 (predicted) → V-05 > V-01 = V-02 > V-03 = V-04 (actual). The surprise is V-03 and V-04 tying at the bottom — V-03's exception budgets are its crown jewel but they serve C-06, not C-09, because the output structure has no scenario section.

## Key Failure Pattern

**C-09 is the sole discriminating criterion.** Two structural gaps:

- **Gap A — missing output section** (V-03, V-04): strong findings but no "Test Scenario Baseline" section defined in output structure
- **Gap B — floor not guaranteed** (V-01, V-02): "one scenario per HIGH/CRITICAL finding" exists but no exception severity budgets ensure >= 3 HIGH/CRITICAL findings

## Excellence Signal from V-05

Exception severity budgets on trace sub-skills (`at least one CRITICAL or HIGH` in trace-contract, trace-permissions, trace-state) collectively guarantee >= 3 HIGH/CRITICAL findings upstream — the test scenario section just derives TS-NN from what the budgets already forced. **Guarantee the inputs, the output floor follows.**

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Exception budgets with explicit severity minimums on trace sub-skills (at least one CRITICAL or HIGH per budget) structurally guarantee the >= 3 HIGH/CRITICAL findings needed for a reliable test scenario floor without requiring an explicit scenario count floor in the Test Scenario Baseline section"]}
```
 transition + missing guard (typically HIGH)
That is >= 3 HIGH/CRITICAL findings → >= 3 named test scenarios. C-09 passes by construction.

### C-06 strength gradient (all pass, but depth varies)

- V-03 and V-05 strongest: explicit exception budget per sub-skill (6-9 named exception types)
- V-02 and V-04 strong: explicit "at least two" floor in dedicated section
- V-01 adequate: "at least one exception path per topic area" across flow sub-skills

### C-03/C-07 format reliability gradient (all pass, but enforcement varies)

- V-02 and V-05 strongest: mandatory table with "No blank cells" rule
- V-01, V-03, V-04: prose-defined requirements (all fields named but no column enforcement)

---

## Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | All Essential |
|-----------|---------------|-----------------|-------------------|-----------|---------------|
| V-01 | 60 | 30 | 7.5 | **97.5** | YES |
| V-02 | 60 | 30 | 7.5 | **97.5** | YES |
| V-03 | 60 | 30 | 5.0 | **95.0** | YES |
| V-04 | 60 | 30 | 5.0 | **95.0** | YES |
| V-05 | 60 | 30 | 10.0 | **100.0** | YES |

---

## Leaderboard

1. **V-05** — 100.0 — Combination: trace-first + mandatory table + exception budgets. Exception budgets with severity minimums structurally guarantee >= 3 HIGH/CRITICAL findings, closing C-09 by construction.
2. **V-01** — 97.5 — Trace-first ordering. Strong on C-08 (state machine context fed into flow sims). C-09 partial: no severity budget floor.
3. **V-02** — 97.5 — Mandatory table format. Strongest format enforcement for C-03/C-07. C-09 partial: same gap as V-01.
4. **V-03** — 95.0 — Best exception coverage of any single-axis variant. C-09 fails: exception budgets exist but no scenario section.
5. **V-04** — 95.0 — Intent-first phrasing reduces silent sub-skill skipping risk. C-09 fails: no scenario section and no exception severity budgets.

All five variations pass the golden threshold (all essential pass AND composite >= 80).

**Predicted leaderboard from variation file**: V-05 > V-02 > V-01 > V-03 > V-04.
**Actual leaderboard**: V-05 > V-01 = V-02 > V-03 = V-04.

Surprise: V-03 and V-04 tie (both fail C-09 entirely). V-03's exception budgets are its strongest differentiator but they serve C-06, not C-09, because the output structure has no scenario section.

---

## Failure Patterns

**C-09 is the discriminating criterion this round.**

All variations pass C-01–C-05, C-06, C-07, C-08 — the rubric discriminates only on whether
the prompt produces a test scenario section with >= 3 scenarios.

Two structural gaps cause C-09 failures:

**Gap type A — missing output section** (V-03, V-04): The prompt runs all sub-skills and
synthesizes findings but the defined output structure never includes a "Test Scenario Baseline"
section. The prompt tells the model what findings to collect but not to derive scenarios from
them. Fix: add an explicit "Test Scenario Baseline" section with format template and floor count.

**Gap type B — floor not guaranteed** (V-01, V-02): The prompt includes "one scenario per
HIGH or CRITICAL finding" but has no mechanism ensuring >= 3 HIGH/CRITICAL findings. Without
exception severity budgets on the trace sub-skills, a run could surface all MEDIUM findings
and produce < 3 scenarios. Fix: add exception severity budgets to trace-contract, trace-state,
or trace-permissions requiring at least one CRITICAL or HIGH finding each.

**Is this a rubric gap or a skill gap?** Skill gap — the rubric correctly identifies >= 3
test scenarios as aspirational. V-05 closes it by combining exception budgets (guaranteeing
severity floor) with an explicit output section. The rubric criterion is sound.

---

## Excellence Signals from V-05

**Signal 1 — Exception severity budgets as test scenario prerequisite**
V-05 closes C-09 not by adding a higher floor count but by guaranteeing the input to the
test scenario section: exception budgets on trace-contract ("at least one CRITICAL or HIGH"),
trace-permissions ("at least one privilege escalation path"), and trace-state (unreachable +
invalid + missing guard) collectively ensure >= 3 HIGH/CRITICAL findings before synthesis.
The test scenario section merely derives TS-NN from what the exception budgets already produced.
Pattern: if a downstream output requires N items of a certain type, add a budget somewhere
upstream that guarantees N items of that type.

**Signal 2 — Trace-first ordering creates a reference context for flow sims**
V-05's execution sequence (trace skills first, flow skills second) allows flow-lifecycle and
flow-conversation to explicitly reference contract violations and state anomalies found in
Round 1. This reduces redundant findings and cross-links findings across sub-skills — a
finding from trace-state can be cited in flow-lifecycle as the root cause. None of the
single-axis variations (V-01 achieves this partially via phase ordering, but V-05 makes the
reference explicit in flow sub-skill instructions).

**Signal 3 — Mandatory table enforces all format criteria at the structural level**
V-05 inherits V-02's "All six columns required per row. No blank cells." rule. This means
C-03 (system boundary + severity) and C-07 (sub-skill citation) pass by table structure, not
by model compliance with prose requirements. Format criteria satisfied structurally > prose.

---

## New Patterns Discovered

**Pattern candidate: Exception budgets need severity minimums to guarantee test scenario floors**
Single-axis exception budget prompts (V-03) can produce strong C-06 coverage without C-09
compliance if the budgets don't include severity labels. Adding "at least one CRITICAL or HIGH"
to one or more trace sub-skill budgets is the minimal change needed to guarantee the scenario floor.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Exception budgets with explicit severity minimums on trace sub-skills (at least one CRITICAL or HIGH per budget) structurally guarantee the >= 3 HIGH/CRITICAL findings needed for a reliable test scenario floor without requiring an explicit scenario count floor in the Test Scenario Baseline section"]}
```
