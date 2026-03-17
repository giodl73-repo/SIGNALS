Reading the scorecard summary notes to extract the two new excellence patterns before writing.

**Pattern 1 — V-01's differentiator:** The DERIVE phase gate. Structural checkpoint: the only way to write `[DERIVE COMPLETE]` is to first produce the derivation block. Skipping is visible as an absent marker, not a silent formula error.

**Pattern 2 — V-02's differentiator:** `#### Golden` placed as a labeled slot *inside* the per-output verdict block. Omission becomes structurally visible (empty slot) rather than detectable only by reading the synthesis section. V-01 passed C-09 but placed Golden in Phase 4 synthesis — V-02's placement is structurally stronger.

These map to **C-13** (derivation-complete gate marker) and **C-14** (required fields in primary output block). A_count goes from 4 → 6.

---

```markdown
# quest-score Rubric — v3

**Version:** v3
**Date:** 2026-03-16
**Prior version:** quest-score-rubric-v2-2026-03-15.md

---

## What changed v2 -> v3

**Two new aspirational criteria, sourced directly from R2 excellence signals:**

**C-13 — Derivation-complete gate marker** (from V-01 DERIVE phase gate)
- Root pattern in R2: V-01 uniquely required the scorer to emit a `[DERIVE COMPLETE]`
  marker immediately after the rubric derivation block, before any output could be opened
- The gate converts a procedural instruction into a structural audit trail: a report missing
  the marker is verifiably incomplete; a report with it proves derivation preceded scoring
- Pass condition: the score report contains an explicit completion marker (or equivalent
  handoff token) immediately following the rubric derivation block, confirming
  E_count/R_count/A_count were resolved before the first output verdict was written;
  a report where derivation completeness can only be inferred from the presence of named
  variables does not satisfy this criterion; binary — PARTIAL not applicable

**C-14 — Required fields in primary output block** (from V-02 in-block `#### Golden` placement)
- Root pattern in R2: V-02 placed `#### Golden` as a labeled required slot inside each
  output's verdict block; V-01 placed Golden in Phase 4 synthesis — both passed C-09, but
  V-02's placement made omission structurally visible (empty slot) rather than discoverable
  only by reading the synthesis section
- The principle generalises: any required per-output field placed in a synthesis section can
  be silently absent without breaking the structure of the output block itself
- Pass condition: the `Golden:` field and per-output summary note appear as labeled slots
  within the same structural block as the verdict matrix for each output; placement of either
  field exclusively in a leaderboard, synthesis, or separate aggregation section fails, even
  if C-09 is otherwise satisfied; PARTIAL if some output blocks carry the fields in-block
  but others defer to synthesis

**Formula update:** A_count denominator `/4` → `/6` (6 aspirational criteria now:
C-09, C-10, C-11, C-12, C-13, C-14). Max score and golden threshold unchanged.

---

## Criterion Summary

| ID | Criterion | Tier | Category |
|----|-----------|------|----------|
| C-01 | Complete verdict matrix — one block or row per criterion for each output; no cell blank or omitted | essential | completeness |
| C-02 | Evidence per verdict — each verdict cell cites a specific structural reference from the output | essential | correctness |
| C-03 | Formula-correct composite score — formula, weights, tier counts, and arithmetic applied correctly | essential | correctness |
| C-04 | Ranked leaderboard — all N outputs in a single descending list by composite score | essential | format |
| C-05 | Failure patterns identified — criteria failing across ALL outputs surfaced; absence stated if none | essential | coverage |
| C-06 | Excellence signals — outlier-high criterion-output pairs identified with structural mechanism named | recommended | depth |
| C-07 | Regression signals — degraded criterion-output pairs flagged when prior-round data is available | recommended | depth |
| C-08 | Per-output summary note — 1–3 sentence structural differentiator or miss per output | recommended | depth |
| C-09 | Golden threshold declaration per output — explicit YES/NO field in each output block | aspirational | format |
| C-10 | Failure-pattern root-cause diagnosis — "rubric gap" vs "skill design issue" label on each universal failure | aspirational | depth |
| C-11 | Rubric-adaptive formula derivation — tier counts derived from active rubric, not hardcoded literals | aspirational | correctness |
| C-12 | Structured diagnosis template — failure entries follow a fixed labeled template enforcing parallel structure | aspirational | format |
| C-13 | Derivation-complete gate marker — explicit completion marker after derivation block proves derivation preceded scoring | aspirational | correctness |
| C-14 | Required fields in primary output block — Golden and summary note appear as labeled slots inside the per-output verdict block, not deferred to synthesis | aspirational | format |

**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/6 * 10)`, max 100.
**Golden threshold:** all 5 essentials PASS + composite >= 80.

---

## Criterion Definitions

### ESSENTIAL — output fails without these

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | **Complete verdict matrix** — the score report contains one block or row per criterion for each output being scored; no criterion-output cell is left blank or omitted | essential | completeness | A verdict matrix or equivalent table exists; every criterion defined in the active rubric appears as a row (or block); every output being scored appears as a column (or block); no cell is blank, absent, or marked "N/A" without a stated reason; a matrix that lists only a subset of criteria (e.g., stops at C-08 when the rubric has C-14) is FAIL; PARTIAL if the structure exists but one or two cells are missing |
| C-02 | **Evidence per verdict** — each verdict cell contains a specific structural reference from the output being scored; generic descriptions not tied to concrete output text do not qualify | essential | correctness | Every verdict cell contains an evidence field; the evidence field names a specific structural element, section title, field label, template pattern, or direct quote from the output being scored; the evidence must be uniquely referencing a concrete structural feature of the specific output being scored; a criterion restatement, a blank, or a generic description that could apply to any well-designed output does not satisfy this criterion |
| C-03 | **Formula-correct composite score** — each output receives a composite score computed from the rubric's stated formula; weights, tier counts, and arithmetic are applied correctly | essential | correctness | The composite formula matches the rubric's weight table; PASS/PARTIAL/FAIL counts are tallied correctly per tier; the arithmetic for each output's composite is verifiable from its verdict matrix row; a score that is internally self-consistent but uses a different formula is FAIL |
| C-04 | **Ranked leaderboard** — all N outputs appear in a single ranked list ordered by composite score, highest to lowest | essential | format | A leaderboard section exists; every scored output appears exactly once; outputs are sorted descending by composite score; ties are explicitly broken by a stated rule or marked as ties; absence of the leaderboard section is FAIL |
| C-05 | **Failure patterns identified** — criteria that received FAIL (or no PASS) across ALL scored outputs are explicitly surfaced; if no such criterion exists, that is stated | essential | coverage | A "failure patterns" section or equivalent exists; any criterion with zero PASS across all N outputs is named as a failure pattern with a note on whether this indicates a rubric gap or skill design issue; if no criteria fail universally, the section states "no universal failures detected"; silent omission of the section is FAIL |

---

### RECOMMENDED — output is better with these

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | **Excellence signals** — outputs scoring unusually high on a specific criterion are identified; the structural mechanism behind the outlier is named | recommended | depth | An "excellence signals" section or equivalent exists; at least one output-criterion pair is called out as an outlier high performer with the structural mechanism that produced it; if no outlier exists, the section states "no excellence signals detected"; omitting the section entirely is FAIL |
| C-07 | **Regression signals** — when prior-round score data is available, criterion-output pairs where the verdict degraded from the prior round are explicitly flagged | recommended | depth | A regression section exists; when prior-round data is available, any criterion-output pair that degraded (PASS → PARTIAL or FAIL; PARTIAL → FAIL) is named with the prior and current verdict; when no prior data is available, the section states "no prior round data"; when no regressions occurred, the section states "no regressions detected"; silently omitting the section when prior data exists is FAIL |
| C-08 | **Per-output summary note** — each scored output has a brief (1–3 sentence) narrative note identifying its primary differentiator or primary miss relative to the field | recommended | depth | Each output in the verdict matrix is followed by or accompanied by a narrative note; the note names either the structural feature that explains the output's relative rank or the most significant missing mechanism; a score table with no notes is FAIL; a note that merely restates the composite score without structural content is PARTIAL |

---

### ASPIRATIONAL — raise the bar once essential/recommended are stable

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | **Golden threshold declaration per output** — each output's result block includes an explicit golden-threshold verdict field stating YES (all essentials PASS and composite >= 80) or NO with the specific failing condition | aspirational | format | Each output block contains a `Golden: YES` or `Golden: NO — [reason]` field; the field is a required structural element, not inferred from the score table; a score report where the reader must deduce golden status from the table does not satisfy this criterion; PARTIAL if some but not all output blocks carry the field |
| C-10 | **Failure-pattern root-cause diagnosis** — each identified failure pattern includes a diagnosis classifying it as either (a) a rubric gap (the criterion is too strict or poorly worded for this skill) or (b) a skill design issue (the skill consistently fails to produce the required output element) | aspirational | depth | The failure patterns section annotates each universal failure with a diagnosis label: "rubric gap" or "skill design issue", with a one-sentence rationale; a failure pattern entry that names the criterion without classifying the root cause does not satisfy this criterion; if there are no universal failures, C-10 is vacuously PASS |
| C-11 | **Rubric-adaptive formula derivation** — the composite score section derives tier criterion counts (E count, R count, A count) from the active rubric's tier table at score-time rather than embedding numeric literals; a formula with hardcoded denominators that would silently produce wrong scores if the rubric gained or lost criteria fails this criterion | aspirational | correctness | The scoring instructions or formula section explicitly reads or states tier counts from the active rubric's criterion list (e.g., "R = count of recommended criteria in the rubric being applied"); a formula embedding numeric literals such as `/3` or `/4` for tier denominators without deriving them from the rubric fails; if the denominator literals happen to match the current rubric but are hardcoded, the criterion is FAIL because the mechanism is wrong; PARTIAL is not applicable — binary |
| C-12 | **Structured diagnosis template** — each failure pattern entry uses a consistent fixed-format labeled template (e.g., `Pattern: [criterion ID] — Diagnosis: [rubric gap/skill design issue] — [one-sentence rationale]`) enforcing parallel structure across all entries in the failure patterns section | aspirational | format | The failure patterns section uses a consistent labeled template for every entry; each entry has the same field labels in the same order; prose-form diagnosis without a required template does not satisfy this criterion even if the content is correct; if there is only one failure pattern entry, the template must still be applied; if there are no universal failures, C-12 is vacuously PASS; PARTIAL if the template is applied to some but not all entries |
| C-13 | **Derivation-complete gate marker** — the score report contains an explicit completion marker (or equivalent handoff token) immediately following the rubric derivation block, confirming that E_count/R_count/A_count were resolved before the first output verdict was written | aspirational | correctness | A visible completion marker (e.g., `[DERIVE COMPLETE]` or equivalent) appears immediately after the rubric derivation block and before the first per-output verdict matrix; the marker must be a structural element of the report, not a prose statement; a report where derivation completeness can only be inferred from the presence of named variables in the formula does not satisfy this criterion; a report that interleaves derivation with scoring (no clean gate boundary) does not satisfy this criterion; PARTIAL is not applicable — binary |
| C-14 | **Required fields in primary output block** — the `Golden:` field and per-output summary note appear as labeled slots within the same structural block as the verdict matrix for each output, not deferred to a synthesis or leaderboard section | aspirational | format | For every scored output, both the `Golden:` field and the summary note are present as labeled fields inside the output's primary verdict block (the same section that contains the criterion-by-criterion verdict matrix); placement of either field exclusively in a leaderboard, synthesis, or aggregation section fails this criterion even if C-09 is otherwise satisfied; the key test: removing the synthesis section should leave the Golden field and summary note still visible for every output; PARTIAL if some output blocks carry both fields in-block but others defer one or both to synthesis |

---

## Golden Threshold

An output meets the golden threshold if:
1. All 5 essential criteria are PASS (no PARTIAL, no FAIL on any essential)
2. Composite score >= 80

---

## Composite Score Reference Table

| Tier | Criteria | Max Points | PARTIAL |
|------|----------|------------|---------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 | 0.5 pass |
| Recommended | C-06, C-07, C-08 | 30 | 0.5 pass |
| Aspirational | C-09, C-10, C-11, C-12, C-13, C-14 | 10 | not counted |
| **Total** | | **100** | |

Formula (symbolic):
```
composite = (essential_pass / E_count * 60)
          + (recommended_pass / R_count * 30)
          + (aspirational_pass / A_count * 10)

where:
  E_count = 5   (C-01 through C-05)
  R_count = 3   (C-06 through C-08)
  A_count = 6   (C-09 through C-14)

Scoring: PASS = 1.0, PARTIAL = 0.5 (Essential and Recommended tiers only)
         Aspirational PARTIAL counts as 0.0 (binary)
```
```

---

**Two new criteria added:**

- **C-13** — Derivation-complete gate marker: the `[DERIVE COMPLETE]` pattern from V-01 is now a scorable structural requirement. A report where derivation completeness can only be *inferred* from named variables fails. Binary.

- **C-14** — Required fields in primary output block: the V-02 placement insight — `Golden:` and summary note as labeled slots *inside* the per-output block. The test: removing the synthesis section should still leave both fields visible. V-01 would fail C-14 (Golden was in Phase 4 synthesis). V-02 would pass.

**Formula impact:** A_count `4 → 6`, so each aspirational criterion now contributes `10/6 ≈ 1.67 pts` vs the prior `10/4 = 2.5 pts`. Maximum and golden threshold unchanged.
