Here is the complete updated rubric:

---

# Rubric: topic-report — v2

**Version**: v2 (updated from Round 1 scorecard — 2026-03-14)
**Skill**: `topic-report`
**Purpose**: Scores whether a `topic-report` skill specification reliably produces a complete, actionable status report artifact.

**v2 changes**: Added C-11 and C-12 from Round 1 excellence signals. C-10 pass condition tightened to require explicit character enumeration (not catch-all prohibition). Aspirational tier expanded from max 2 to max 4; scoring formula updated accordingly.

---

## Design Decisions

- **C-01 (artifact written)** is essential because `topic-report` is specifically the *file* variant — if nothing lands on disk, the whole point is missed.
- **C-04 (readiness statement calibrated)** catches the common failure where the statement says "ready" but the table shows 3 open signals — the two must agree.
- **C-07 (matches topic-status)** is *recommended* not essential — a slightly stale report is still useful; a report with no next step (C-05) is not.
- **C-06 (`--format teams`)** is recommended because it's an explicit flag variant; failing it doesn't break the default mode.
- **C-10 (paste-ready)** is aspirational — most Teams clients handle minor markdown artifacts, but a truly clean card raises the bar.
- **C-11 (BLOCKERS pre-computation)** is aspirational — only the strongest prompt designs emit a named BLOCKERS block before the readiness sentence. Scored separately from C-09 because the mechanism (pre-compute then cite) is distinct from the output property (sentence names signals).
- **C-12 (character-level Teams validation)** is aspirational — catches the failure mode where C-10 passes on structural grounds but the output still contains backticks or angle brackets. Round 1 finding: catch-all prohibitions leave this gap open; explicit enumeration does not.

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

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-12 that pass   (max 4)

composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/4 * 10)

golden = (essential_pass == 5) AND (composite >= 80)
```

| Score | Label |
|-------|-------|
| 90-100 | Exemplary |
| 80-89 | Golden (meets threshold) |
| 60-79 | Partial — review failed essential |
| < 60 | Failing |

---

## Failure Modes

| Failure | Maps to | Impact if missed |
|---------|---------|-----------------|
| File written but path not echoed | C-01 | Essential fail |
| Progress table present but counts are wrong | C-02 | Essential fail |
| Open signals listed but owner field absent | C-03 | Essential fail |
| Readiness statement contradicts progress table | C-04 | Essential fail |
| No next step or next step is generic | C-05 | Essential fail |
| `--format teams` output contains markdown fencing | C-06 | Recommended fail |
| Report counts differ from topic-status | C-07 | Recommended fail |
| Open signal entry missing namespace or type | C-08 | Recommended fail |
| Readiness sentence generic, no signal names | C-09 | Aspirational fail |
| Spec uses catch-all "no markdown syntax" | C-10 | Aspirational fail — backticks/angle brackets may still appear |
| No BLOCKERS block before readiness statement | C-11 | Aspirational fail — signal names may drift or be omitted |
| Teams card contains backtick or angle-bracket chars | C-12 | Aspirational fail — breaks Teams even when C-10 passes on spec grounds |

---

## Excellence Patterns (Round 1)

**P-01 — BLOCKERS phase before readiness**: Pre-compute a named, locked list of essential OPEN signals before writing the readiness statement. The readiness sentence must then cite that list by signal-type name. Necessary and sufficient for C-09 + C-11 together. Expected to transfer to any skill with a readiness statement.

**P-02 — Explicit character enumeration over catch-all**: Enumerate prohibited characters by name: "no backtick characters, no angle brackets." Do not rely on "no markdown syntax." Models interpret catch-alls narrowly and may still emit inline code fences or angle-bracket variable notation while believing the prohibition is satisfied. Necessary condition for reliably passing C-10 + C-12.

---

**Key structural changes from v1**: C-10's pass condition is now a specification check (does the prompt enumerate characters?), while C-12 is the corresponding output check (does the actual card scan clean?). They are intentionally separated because a spec can enumerate correctly but a model can still fail the output — and vice versa is also observable. The BLOCKERS block (C-11) is the mechanism that unlocks C-09 at scale; the two criteria are kept distinct because a variation can pass C-09 without a BLOCKERS block (fragile) or have a BLOCKERS block that its readiness sentence doesn't cite (structural fail on C-11, possible pass on C-09).
ritten without locked pre-computation; signal names may drift or be omitted |
| Teams card output contains backtick or angle-bracket characters | C-12 | Aspirational fail — card breaks in Teams even when C-10 passes on specification grounds |

---

## Excellence Patterns (Round 1)

These patterns are necessary and sufficient for reaching C-09 + C-11 and C-10 + C-12. Recorded here for reuse when writing or evaluating future `topic-*` skill specifications.

**P-01 — BLOCKERS phase before readiness**
Pre-compute a named, locked list of essential OPEN signals before writing the readiness statement. The readiness sentence must then cite that list by signal-type name. This is the only design pattern observed to reliably achieve C-09 + C-11 together in Round 1. Expected to transfer to any skill with a readiness statement (e.g., `topic-status`, `draft-proposal`).

**P-02 — Explicit character enumeration over catch-all prohibition**
Enumerate prohibited characters by name: "no backtick characters, no angle brackets (<, >)." Do not rely on "no markdown syntax" or equivalent catch-alls. Models interpret catch-alls narrowly and may still emit inline code fences (backtick-delimited) or angle-bracket variable notation while believing the prohibition is satisfied. Explicit enumeration is the necessary condition for reliably passing C-10 + C-12.
