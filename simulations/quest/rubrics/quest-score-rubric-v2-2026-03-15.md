Written to `simulations/quest/rubrics/quest-score-rubric-v2-2026-03-15.md`.

---

## What changed v1 -> v2

**Two new aspirational criteria, sourced directly from R1 signals:**

**C-11 — Rubric-adaptive formula derivation** (from the formula-hardcoding universal failure)
- Root cause in R1: all 5 variations hardcoded `/2` and `/1` as tier denominators, matching the old 8-criterion rubric rather than deriving from the active one
- The excellence signal on C-01 showed the right instinct (open-ended "per rubric criterion") but didn't carry it through to the formula
- Pass condition: denominator must be derived from the active rubric's criterion count, not a literal; even if the literal happens to match today, FAIL — the mechanism is wrong

**C-12 — Structured diagnosis template** (from V-04/V-05 excellence on C-10)
- V-04/V-05 passed C-10 specifically because they used `Pattern/Diagnosis: [label] -- [sentence]` as a fixed template across every failure entry
- V-01/V-02/V-03 wrote prose — correct content, wrong structure
- Pass condition: every failure entry uses the same field labels in the same order; prose without a template is FAIL regardless of content quality

**Formula update:** aspirational denominator `/2` -> `/4` (4 aspirational criteria now: C-09, C-10, C-11, C-12). Max score and golden threshold unchanged.
n threshold declaration per output -- explicit YES/NO field in each output block | format |
| C-10 | Failure-pattern root-cause diagnosis -- "rubric gap" vs "skill design issue" label on each universal failure | depth |
| C-11 | Rubric-adaptive formula derivation -- tier counts derived from active rubric, not hardcoded literals | correctness |
| C-12 | Structured diagnosis template -- failure entries follow a fixed labeled template enforcing parallel structure | format |

**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/4 * 10)`, max 100.
**Golden threshold:** all 5 essentials PASS + composite >= 80.

---

## Criterion Definitions

### ESSENTIAL -- output fails without these

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | **Complete verdict matrix** -- the score report contains one block or row per criterion for each output being scored; no criterion-output cell is left blank or omitted | essential | completeness | A verdict matrix or equivalent table exists; every criterion defined in the active rubric appears as a row (or block); every output being scored appears as a column (or block); no cell is blank, absent, or marked "N/A" without a stated reason; a matrix that lists only a subset of criteria (e.g., stops at C-08 when the rubric has C-10) is FAIL; PARTIAL if the structure exists but one or two cells are missing |
| C-02 | **Evidence per verdict** -- each verdict cell contains a specific structural reference from the output being scored; generic descriptions not tied to concrete output text do not qualify | essential | correctness | Every verdict cell contains an evidence field; the evidence field names a specific structural element, section title, field label, template pattern, or direct quote from the output being scored; the evidence must be uniquely referencing a concrete structural feature of the specific output being scored; a criterion restatement, a blank, or a generic description that could apply to any well-designed output does not satisfy this criterion |
| C-03 | **Formula-correct composite score** -- each output receives a composite score computed from the rubric's stated formula; weights, tier counts, and arithmetic are applied correctly | essential | correctness | The composite formula matches the rubric's weight table; PASS/PARTIAL/FAIL counts are tallied correctly per tier; the arithmetic for each output's composite is verifiable from its verdict matrix row; a score that is internally self-consistent but uses a different formula is FAIL |
| C-04 | **Ranked leaderboard** -- all N outputs appear in a single ranked list ordered by composite score, highest to lowest | essential | format | A leaderboard section exists; every scored output appears exactly once; outputs are sorted descending by composite score; ties are explicitly broken by a stated rule or marked as ties; absence of the leaderboard section is FAIL |
| C-05 | **Failure patterns identified** -- criteria that received FAIL (or no PASS) across ALL scored outputs are explicitly surfaced; if no such criterion exists, that is stated | essential | coverage | A "failure patterns" section or equivalent exists; any criterion with zero PASS across all N outputs is named as a failure pattern with a note on whether this indicates a rubric gap or skill design issue; if no criteria fail universally, the section states "no universal failures detected"; silent omission of the section is FAIL |

---

### RECOMMENDED -- output is better with these

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | **Excellence signals** -- outputs scoring unusually high on a specific criterion are identified; the structural mechanism behind the outlier is named | recommended | depth | An "excellence signals" section or equivalent exists; at least one output-criterion pair is called out as an outlier high performer with the structural mechanism that produced it; if no outlier exists, the section states "no excellence signals detected"; omitting the section entirely is FAIL |
| C-07 | **Regression signals** -- when prior-round score data is available, criterion-output pairs where the verdict degraded from the prior round are explicitly flagged | recommended | depth | A regression section exists; when prior-round data is available, any criterion-output pair that degraded (PASS -> PARTIAL or FAIL; PARTIAL -> FAIL) is named with the prior and current verdict; when no prior data is available, the section states "no prior round data"; when no regressions occurred, the section states "no regressions detected"; silently omitting the section when prior data exists is FAIL |
| C-08 | **Per-output summary note** -- each scored output has a brief (1-3 sentence) narrative note identifying its primary differentiator or primary miss relative to the field | recommended | depth | Each output in the verdict matrix is followed by or accompanied by a narrative note; the note names either the structural feature that explains the output's relative rank or the most significant missing mechanism; a score table with no notes is FAIL; a note that merely restates the composite score without structural content is PARTIAL |

---

### ASPIRATIONAL -- raise the bar once essential/recommended are stable

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | **Golden threshold declaration per output** -- each output's result block includes an explicit golden-threshold verdict field stating YES (all essentials PASS and composite >= 80) or NO with the specific failing condition | aspirational | format | Each output block contains a `Golden: YES` or `Golden: NO -- [reason]` field; the field is a required structural element, not inferred from the score table; a score report where the reader must deduce golden status from the table does not satisfy this criterion; PARTIAL if some but not all output blocks carry the field |
| C-10 | **Failure-pattern root-cause diagnosis** -- each identified failure pattern includes a diagnosis classifying it as either (a) a rubric gap (the criterion is too strict or poorly worded for this skill) or (b) a skill design issue (the skill consistently fails to produce the required output element) | aspirational | depth | The failure patterns section annotates each universal failure with a diagnosis label: "rubric gap" or "skill design issue", with a one-sentence rationale; a failure pattern entry that names the criterion without classifying the root cause does not satisfy this criterion; if there are no universal failures, C-10 is vacuously PASS |
| C-11 | **Rubric-adaptive formula derivation** -- the composite score section derives tier criterion counts (R count, A count) from the active rubric's tier table at score-time rather than embedding numeric literals; a formula with hardcoded denominators that would silently produce wrong scores if the rubric gained or lost criteria fails this criterion | aspirational | correctness | The scoring instructions or formula section explicitly reads or states tier counts from the active rubric's criterion list (e.g., "R = count of recommended criteria in the rubric being applied"); a formula embedding numeric literals such as /2 or /3 for tier denominators without deriving them from the rubric fails; if the denominator literals happen to match the current rubric but are hardcoded, the criterion is FAIL because the mechanism is wrong; PARTIAL is not applicable -- this criterion is binary |
| C-12 | **Structured diagnosis template** -- each failure pattern entry uses a consistent fixed-format labeled template (e.g., `Pattern: [criterion ID] -- Diagnosis: [rubric gap/skill design issue] -- [one-sentence rationale]`) enforcing parallel structure across all entries in the failure patterns section | aspirational | format | The failure patterns section uses a consistent labeled template for every entry; each entry has the same field labels in the same order; prose-form diagnosis without a required template does not satisfy this criterion even if the content is correct; if there is only one failure pattern entry, the template must still be applied; if there are no universal failures, C-12 is vacuously PASS; PARTIAL if the template is applied to some but not all entries |

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
| Aspirational | C-09, C-10, C-11, C-12 | 10 | not counted |
| **Total** | | **100** | |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-15 | Added C-11 (rubric-adaptive formula derivation) and C-12 (structured diagnosis template) from R1 excellence signals; aspirational denominator /2 -> /4 |
