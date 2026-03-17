Reading the scorecard's `new_patterns` JSON and the key findings, two new patterns emerge:

1. **COMPLETENESS/EXCLUSIVITY naming** — bidirectionality stated as two separately named invariants (one per direction), not compound phrasing
2. **Branch sealing instruction** — structural isolation between rendering branches; explicit character prohibition alone is insufficient

These become C-13 and C-14. Aspirational max goes from 4 to 6; scoring formula updates accordingly.

---

# Rubric: topic-report — v3

**Version**: v3 (updated from Round 2 scorecard — 2026-03-14)
**Skill**: `topic-report`
**Purpose**: Scores whether a `topic-report` skill specification reliably produces a complete, actionable status report artifact.

**v3 changes**: Added C-13 (COMPLETENESS/EXCLUSIVITY named invariants) and C-14 (branch sealing instruction) from Round 2 excellence signals. Aspirational tier expanded from max 4 to max 6; scoring formula updated accordingly.

---

## Design Decisions

- **C-01 (artifact written)** is essential because `topic-report` is specifically the *file* variant — if nothing lands on disk, the whole point is missed.
- **C-04 (readiness statement calibrated)** catches the common failure where the statement says "ready" but the table shows 3 open signals — the two must agree.
- **C-07 (matches topic-status)** is *recommended* not essential — a slightly stale report is still useful; a report with no next step (C-05) is not.
- **C-06 (`--format teams`)** is recommended because it's an explicit flag variant; failing it doesn't break the default mode.
- **C-10 (paste-ready)** is aspirational — most Teams clients handle minor markdown artifacts, but a truly clean card raises the bar.
- **C-11 (BLOCKERS pre-computation)** is aspirational — only the strongest prompt designs emit a named BLOCKERS block before the readiness sentence. Scored separately from C-09 because the mechanism (pre-compute then cite) is distinct from the output property (sentence names signals).
- **C-12 (character-level Teams validation)** is aspirational — catches the failure mode where C-10 passes on structural grounds but the output still contains backticks or angle brackets. Round 1 finding: catch-all prohibitions leave this gap open; explicit enumeration does not.
- **C-13 (COMPLETENESS/EXCLUSIVITY named invariants)** is aspirational — compound phrasing ("every name … and only names") is functionally equivalent for the rubric criterion but less reliable in live runs where a model may fail each direction independently. Naming COMPLETENESS and EXCLUSIVITY as separate invariants makes each direction independently verifiable and closes the "used verbatim" ambiguity gap. Scored separately from C-11 because the mechanism (two named sub-rules vs. one compound constraint) is structurally distinct.
- **C-14 (branch sealing instruction)** is aspirational — explicit character prohibition (C-10) is necessary but not sufficient; a model reading both format branches may carry patterns across without a structural isolation directive. Round 2 finding: the sealed-branches instruction ("do not reference the other branch's format descriptions") is the mechanism that makes C-12 achievable reliably, not merely the absence of a known contamination source.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Artifact written and path echoed** | completeness | essential | Output includes a write instruction that lands the report at a deterministic path and echoes that path after write; artifact must exist on disk |
| C-02 | **Progress table present with accurate counts** | correctness | essential | Table with one row per namespace, total/complete/open columns, counts from actual discovered signals, includes a completion percentage or status symbol |
| C-03 | **Open signals listed with owners** | coverage | essential | Every incomplete signal enumerated with an owner field (even if "unassigned"); no open signal silently omitted |
| C-04 | **Readiness statement present and calibrated** | correctness | essential | Single sentence or labeled field states ready/not ready/conditionally ready; consistent with signal counts in the progress table |
| C-05 | **Recommended next step present** | depth | essential | Output concludes with one concrete next action; next step matches the most critical open signal |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **`--format teams` produces compact ASCII card** | format | recommended | Single ASCII block, all four sections, <= 40 lines and <= 80 chars wide |
| C-07 | **Content matches topic-status output** | correctness | recommended | Signal counts, readiness state, and next step identical to `topic-status` for the same topic at the same point in time |
| C-08 | **Open signals include signal type and namespace** | coverage | recommended | Each open signal entry names both namespace and signal type, not just a freeform description |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Readiness statement references blocking signals** | depth | aspirational | Readiness statement names the specific signals that are blocking (e.g., "Not ready — missing prove-analysis and review-design") rather than a generic message |
| C-10 | **Teams card prohibition is explicitly enumerated** | format | aspirational | The spec explicitly prohibits backtick characters, angle brackets (`<`, `>`), and markdown emphasis markers *by name* — not satisfied by a catch-all phrase such as "no markdown syntax" |
| C-11 | **Output includes BLOCKERS pre-computation block** | depth | aspirational | Before the readiness statement, the output contains an explicit enumeration of essential OPEN signals (a BLOCKERS block); the readiness sentence references signal-type names drawn from that block and cannot introduce new names or omit names present in the block |
| C-12 | **Teams card passes character-level scan** | format | aspirational | Independent of C-10's specification check, the `--format teams` output contains zero backtick characters and zero angle-bracket characters when scanned character by character |
| C-13 | **Bidirectionality stated as two named invariants** | depth | aspirational | The BLOCKERS constraint is expressed as two separately named sub-rules — COMPLETENESS (the readiness sentence must cite every name in the BLOCKERS block) and EXCLUSIVITY (the readiness sentence must not introduce any name absent from the BLOCKERS block) — each verifiable independently; compound phrasing such as "every name … and only names" does not satisfy this criterion |
| C-14 | **Branch sealing instruction present** | format | aspirational | The spec contains an explicit directive that separates the default and `--format teams` rendering paths — e.g., "the branches are sealed; do not reference the other branch's format descriptions when executing" — so that format patterns cannot bleed across branches even when a model processes both in a single pass; explicit character prohibition (C-10) alone does not satisfy this criterion |

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-14 that pass   (max 6)

composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/6 * 10)

golden = (essential_pass == 5) AND (composite >= 80)
```

| Score | Label |
|-------|-------|
| 90-100 | Exemplary |
| 80-89 | Golden (meets threshold) |
| 60-79 | Partial — review failed essential |
| < 60 | Failing |
