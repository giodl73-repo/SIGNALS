Rubric written to `simulations/quest/rubrics/topic-report-rubric-2026-03-14.md`.

**Design decisions:**

- **C-01 (artifact written)** is essential because `topic-report` is specifically the *file* variant — if nothing lands on disk, the whole point is missed.
- **C-04 (readiness statement calibrated)** catches the common failure where the statement says "ready" but the table shows 3 open signals — the two must agree.
- **C-07 (matches topic-status)** is *recommended* not essential — a slightly stale report is still useful; a report with no next step (C-05) is not.
- **C-06 (`--format teams`)** is recommended because it's an explicit flag variant; failing it doesn't break the default mode.
- **C-10 (paste-ready)** is aspirational — most Teams clients handle minor markdown artifacts, but a truly clean card raises the bar.
 a completion percentage or status symbol |
| C-03 | **Open signals listed with owners** | coverage | essential | Every incomplete signal is enumerated with an owner field (even if "unassigned"); no open signal is silently omitted |
| C-04 | **Readiness statement present and calibrated** | correctness | essential | A single sentence or labeled field states whether the topic is ready, not ready, or conditionally ready; the statement is consistent with the signal counts in the progress table |
| C-05 | **Recommended next step present** | depth | essential | Output concludes with one concrete next action (e.g., "run scout-feasibility", "assign owner for prove-analysis"); next step matches the most critical open signal |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **`--format teams` produces compact ASCII card** | format | recommended | When `--format teams` is passed, output is a single ASCII block (no markdown headers, no fenced code) with all four sections (progress, open signals, readiness, next step) compressed into <= 40 lines and <= 80 chars wide |
| C-07 | **Content matches topic-status output** | correctness | recommended | Signal counts, readiness state, and next step in the report are identical to what `topic-status` would produce for the same topic at the same point in time |
| C-08 | **Open signals include signal type and namespace** | coverage | recommended | Each open signal entry names both the namespace (e.g., `prove`) and the signal type (e.g., `prove-analysis`), not just a freeform description |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Readiness statement references blocking signals** | depth | aspirational | The readiness statement names the specific signals that are blocking (e.g., "Not ready — missing prove-analysis and review-design") rather than giving a generic message |
| C-10 | **Teams card is paste-ready** | format | aspirational | The `--format teams` output contains no characters that break Teams rendering (no backticks, no angle brackets, no markdown syntax); every line uses ASCII box-drawing characters or plain text |

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-10 that pass   (max 2)

composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/2 * 10)

golden = (essential_pass == 5) AND (composite >= 80)
```

| Score | Label |
|-------|-------|
| 90-100 | Exemplary |
| 80-89 | Golden (meets threshold) |
| 60-79 | Partial -- review failed essential |
| < 60 | Failing |

---

## Failure Modes

| Failure | Maps to | Impact if missed |
|---------|---------|-----------------|
| File written but path not echoed | C-01 | Essential fail — user cannot locate the artifact |
| Progress table present but counts are wrong | C-02 | Essential fail — corrupts readiness signal |
| Open signals listed but owner field absent | C-03 | Essential fail — document not actionable |
| Readiness statement contradicts progress table | C-04 | Essential fail — report is misleading |
| No next step or next step is generic ("keep going") | C-05 | Essential fail — document doesn't drive action |
| `--format teams` output contains markdown fencing | C-06 | Recommended fail — card breaks when pasted into Teams |
| Report counts differ from topic-status | C-07 | Recommended fail — two sources of truth diverge |
| Open signal entry missing namespace or type | C-08 | Recommended fail — owner can't locate the signal |
