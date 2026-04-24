Written to `simulations/quest/rubrics/quest-score-rubric-2026-03-15.md`.

---

## Rubric summary

**5 essential** (all must PASS):

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | Complete verdict matrix — every criterion × output cell populated | completeness |
| C-02 | Evidence per verdict — specific structural quote, not a restatement | correctness |
| C-03 | Formula-correct composite — arithmetic verifiable from PASS/PARTIAL/FAIL counts | correctness |
| C-04 | Ranked leaderboard — all outputs sorted descending, ties noted | format |
| C-05 | Failure patterns identified — universal FAILs surfaced or "none" stated | coverage |

**3 recommended**:

| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | Excellence signals — outlier high-performer per criterion named with mechanism | depth |
| C-07 | Regression signals — prior-round degradations flagged, or absence stated | depth |
| C-08 | Per-output summary note — primary differentiator or primary miss in 1-3 sentences | depth |

**2 aspirational**:

| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | Golden threshold declaration per output — explicit YES/NO field in each output block | format |
| C-10 | Failure-pattern root-cause diagnosis — "rubric gap" vs "skill design issue" label on each universal failure | depth |

**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`, max 100. Golden threshold: all essentials PASS + composite >= 80.
nce referencing a concrete structural feature of the specific output being scored; a criterion restatement, a blank, or a generic description that could apply to any well-designed output does not satisfy this criterion |
| C-03 | **Formula-correct composite score** — each output receives a composite score computed from the rubric's stated formula; weights, tier counts, and arithmetic are applied correctly | essential | correctness | The composite formula matches the rubric's weight table; PASS/PARTIAL/FAIL counts are tallied correctly per tier; the arithmetic for each output's composite is verifiable from its verdict matrix row; a score that is internally self-consistent but uses a different formula is FAIL |
| C-04 | **Ranked leaderboard** — all N outputs appear in a single ranked list ordered by composite score, highest to lowest | essential | format | A leaderboard section exists; every scored output appears exactly once; outputs are sorted descending by composite score; ties are explicitly broken by a stated rule or marked as ties; absence of the leaderboard section is FAIL |
| C-05 | **Failure patterns identified** — criteria that received FAIL (or no PASS) across ALL scored outputs are explicitly surfaced; if no such criterion exists, that is stated | essential | coverage | A "failure patterns" section or equivalent exists; any criterion with zero PASS across all N outputs is named as a failure pattern with a note on whether this indicates a rubric gap or skill design issue; if no criteria fail universally, the section states "no universal failures detected"; silent omission of the section is FAIL |

---

### RECOMMENDED — output is better with these

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | **Excellence signals** — outputs scoring unusually high on a specific criterion are identified; the structural mechanism behind the outlier is named | recommended | depth | An "excellence signals" section or equivalent exists; at least one output-criterion pair is called out as an outlier high performer with the structural mechanism that produced it; if no outlier exists, the section states "no excellence signals detected"; omitting the section entirely is FAIL |
| C-07 | **Regression signals** — when prior-round score data is available, criterion-output pairs where the verdict degraded from the prior round are explicitly flagged | recommended | depth | A regression section exists; when prior-round data is available, any criterion-output pair that degraded (PASS -> PARTIAL or FAIL; PARTIAL -> FAIL) is named with the prior and current verdict; when no prior data is available, the section states "no prior round data"; when no regressions occurred, the section states "no regressions detected"; silently omitting the section when prior data exists is FAIL |
| C-08 | **Per-output summary note** — each scored output has a brief (1-3 sentence) narrative note identifying its primary differentiator or primary miss relative to the field | recommended | depth | Each output in the verdict matrix is followed by or accompanied by a narrative note; the note names either the structural feature that explains the output's relative rank or the most significant missing mechanism; a score table with no notes is FAIL; a note that merely restates the composite score without structural content is PARTIAL |

---

### ASPIRATIONAL — raise the bar once essential/recommended are stable

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | **Golden threshold declaration per output** — each output's result block includes an explicit golden-threshold verdict field stating YES (all essentials PASS and composite >= 80) or NO with the specific failing condition | aspirational | format | Each output block contains a `Golden: YES` or `Golden: NO -- [reason]` field; the field is a required structural element, not inferred from the score table; a score report where the reader must deduce golden status from the table does not satisfy this criterion; PARTIAL if some but not all output blocks carry the field |
| C-10 | **Failure-pattern root-cause diagnosis** — each identified failure pattern includes a diagnosis classifying it as either (a) a rubric gap (the criterion is too strict or poorly worded for this skill) or (b) a skill design issue (the skill consistently fails to produce the required output element) | aspirational | depth | The failure patterns section annotates each universal failure with a diagnosis label: "rubric gap" or "skill design issue", with a one-sentence rationale; a failure pattern entry that names the criterion without classifying the root cause does not satisfy this criterion; if there are no universal failures, C-10 is vacuously PASS |

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
| Aspirational | C-09, C-10 | 10 | not counted |
| **Total** | | **100** | |
