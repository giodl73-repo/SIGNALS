Reading the R3 scorecard notes carefully, three structurally distinct excellence patterns emerge across V-01, V-02, and V-03 that are not captured by any existing criterion:

1. **LOCK directive** (V-01) — list immutability as a standalone named obligation, separate from COMPLETENESS/EXCLUSIVITY
2. **In-render verification scan** (V-02) — active procedural scan (COMPLETENESS CHECK / EXCLUSIVITY CHECK) executed *before* writing the sentence, not merely declared
3. **Inline [RULE] annotation style** (V-03) — rule markers embedded at the exact template position they govern; zero-distance enforcement

These become C-15, C-16, C-17. Aspirational max rises from 6 to 9; formula denominator updates accordingly.

---

```markdown
# Rubric: topic-report — v4

**Version**: v4 (updated from Round 3 scorecard — 2026-03-14)
**Skill**: `topic-report`
**Purpose**: Scores whether a `topic-report` skill specification reliably produces a
complete, actionable status report artifact.

**v4 changes**: Added C-15 (BLOCKERS LOCK directive), C-16 (in-render verification
scan), and C-17 (inline [RULE] annotation style) from Round 3 excellence signals.
Aspirational tier expanded from max 6 to max 9; scoring formula updated accordingly.

---

## Design Decisions

- **C-01 (artifact written)** is essential because `topic-report` is specifically the
  *file* variant — if nothing lands on disk, the whole point is missed.
- **C-04 (readiness statement calibrated)** catches the common failure where the
  statement says "ready" but the table shows 3 open signals — the two must agree.
- **C-07 (matches topic-status)** is *recommended* not essential — a slightly stale
  report is still useful; a report with no next step (C-05) is not.
- **C-06 (`--format teams`)** is recommended because it's an explicit flag variant;
  failing it doesn't break the default mode.
- **C-10 (paste-ready)** is aspirational — most Teams clients handle minor markdown
  artifacts, but a truly clean card raises the bar.
- **C-11 (BLOCKERS pre-computation)** is aspirational — only the strongest prompt
  designs emit a named BLOCKERS block before the readiness sentence. Scored separately
  from C-09 because the mechanism (pre-compute then cite) is distinct from the output
  property (sentence names signals).
- **C-12 (character-level Teams validation)** is aspirational — catches the failure
  mode where C-10 passes on structural grounds but the output still contains backticks
  or angle brackets. Round 1 finding: catch-all prohibitions leave this gap open;
  explicit enumeration does not.
- **C-13 (COMPLETENESS/EXCLUSIVITY named invariants)** is aspirational — compound
  phrasing ("every name … and only names") is functionally equivalent for the rubric
  criterion but less reliable in live runs where a model may fail each direction
  independently. Naming COMPLETENESS and EXCLUSIVITY as separate invariants makes each
  direction independently verifiable and closes the "used verbatim" ambiguity gap.
  Scored separately from C-11 because the mechanism (two named sub-rules vs. one
  compound constraint) is structurally distinct.
- **C-14 (branch sealing instruction)** is aspirational — explicit character
  prohibition (C-10) is necessary but not sufficient; a model reading both format
  branches may carry patterns across without a structural isolation directive. Round 2
  finding: the sealed-branches instruction ("do not reference the other branch's format
  descriptions") is the mechanism that makes C-12 achievable reliably, not merely the
  absence of a known contamination source.
- **C-15 (BLOCKERS LOCK directive)** is aspirational — COMPLETENESS and EXCLUSIVITY
  (C-13) constrain how the BLOCKERS list is *used*, but neither prevents the list from
  being silently revised between the pre-computation step and the write step. A
  standalone named LOCK directive ("The BLOCKERS list is now frozen — no additions,
  removals, or revisions permitted in subsequent phases") makes list immutability a
  first-class obligation that cannot be conflated with the bidirectionality rule. Scored
  separately from C-13 because the mechanism (mutation guard vs. citation constraint)
  addresses a different failure mode: drift rather than omission or injection.
- **C-16 (in-render verification scan)** is aspirational — declarative rules
  (C-13, C-14, C-15) tell the model what is required but do not force it to check
  compliance at the moment of generation. An in-render verification scan (explicit
  COMPLETENESS CHECK and EXCLUSIVITY CHECK steps executed *before* writing the
  readiness sentence) converts a passive constraint into an active procedure: the model
  must enumerate BLOCKERS names, confirm each is present in the draft sentence, then
  enumerate draft names and confirm each is present in the BLOCKERS list. Round 3
  finding: the scan is the mechanism that makes C-13 robust across live runs, not merely
  the presence of the named sub-rules.
- **C-17 (inline [RULE] annotation style)** is aspirational — gathering rules into a
  preamble section keeps the specification readable but introduces distance between each
  rule and the template position it governs; a model may skip the preamble or fail to
  map preamble rules to the correct output slot. Embedding [RULE] markers at the exact
  template position they govern reduces this mapping gap to zero. Round 3 finding:
  zero-distance enforcement (rule co-located with governed text) is a distinct
  structural property from branch sealing (C-14) or explicit enumeration (C-10); a
  spec can satisfy either without the other.

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
| C-15 | **BLOCKERS LOCK directive present** | depth | aspirational | The spec contains a standalone named directive that explicitly freezes the BLOCKERS list after its pre-computation step — e.g., "The BLOCKERS list is now frozen. No additions, removals, or revisions are permitted in subsequent phases." — making list immutability a first-class obligation distinct from the COMPLETENESS/EXCLUSIVITY bidirectionality rules (C-13); the embedded clause "this list is closed" within the pre-computation step does not satisfy this criterion because it does not name the directive or assert it as a phase-spanning constraint |
| C-16 | **In-render verification scan present** | depth | aspirational | The spec instructs the model to execute an explicit two-step compliance scan *before* writing the readiness sentence: (1) COMPLETENESS CHECK — enumerate every name in the BLOCKERS list and confirm each appears in the draft sentence; (2) EXCLUSIVITY CHECK — enumerate every name in the draft sentence and confirm each appears in the BLOCKERS list; declarative statements of COMPLETENESS/EXCLUSIVITY (C-13) alone do not satisfy this criterion because they do not require active verification at generation time |
| C-17 | **Rules co-located with governed template positions** | format | aspirational | Constraint rules are embedded as inline markers (e.g., `[RULE ...]`) at the exact template position they govern — not collected in a separate preamble or appendix — so that zero mapping distance exists between each rule and the output slot it constrains; branch isolation achieved by two independently placed seal markers (one at the branch dispatch point, one at the Branch B entry point) rather than a single preamble directive; C-14's sealed-branch requirement and C-17's co-location requirement are independent: a spec can satisfy either without satisfying the other |

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-17 that pass   (max 9)

composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/9 * 10)

golden = (essential_pass == 5) AND (composite >= 80)
```

**Notes**:
- Aspirational criteria are independent — any combination can pass.
- C-15 (LOCK) and C-16 (scan) both address list integrity but via different mechanisms:
  C-15 guards against mutation between steps; C-16 guards against omission or injection
  at write time. A spec can include either without the other.
- C-17 (co-location) and C-14 (sealing) are orthogonal format properties.
  Co-location concerns rule-to-slot distance; sealing concerns branch-to-branch
  contamination. Both can be present, absent, or mixed independently.
```
