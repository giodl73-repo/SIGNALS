Written to `simulations/quest/rubrics/quest-score-rubric-v3-2026-03-16.md`.

---

**What changed from v2 to v3:**

Two new Aspirational criteria, N_aspirational bumped 4 → 6.

---

**C-13 — Formula version delta declaration** (correctness)

Source: V-03 Axis F. V-03's FORMULA CHANGE ALERT fires at Phase 1 — the earliest lifecycle point of any R2 mechanism — and names the prior and current denominators before scoring begins. No existing criterion covered this: C-01 checks the current formula was loaded; C-10 checks arithmetic is correct given the formula used. Neither asks *did the scorer confirm they switched versions*.

Pass condition: A delta notice before any composite score names (a) the prior value and (b) the current value — e.g., "N_aspirational=6 (was 4 in v2)". PARTIAL if current formula is correctly loaded but no prior-vs-current comparison exists. FAIL if a version change is in scope and no delta is declared, or if an outdated denominator appears in any computation. N/A rule (mirrors C-09): write "No prior version delta — scoring under v[N] as the baseline version" → PARTIAL.

---

**C-14 — Pre-scoring mechanism placement** (correctness)

Source: V-01 Axis D. The MODEL CELL fires at "Phase 2 entry — the earliest moment the scorer writes any evidence." C-11 already asks *does the positive anchor exist*; C-14 asks *is it placed where it can prevent errors rather than only illustrate them*. An anchor mid-way through Phase 2 can correct future cells but cannot fix cells already written wrong.

Pass condition: The evidence positive anchor appears in the first criterion-output evidence cell of the scoring section (Phase 2 entry). Post-scoring verification mechanisms (arithmetic re-derivation, discrepancy declaration) are exempt — they belong at Phase 3 by design. PARTIAL if the anchor exists (C-11 PASS) but appears after the first three evidence cells. FAIL if no anchor exists in the scored body, or if deferred entirely to Phase 3.

---

**Formula update:**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)   ← was /4
```
c re-derivation, discrepancy declaration) are exempt — they belong at Phase 3 by design. PARTIAL if a positive anchor exists (C-11 PASS) but is placed after the first few evidence cells rather than at Phase 2 entry. FAIL if no positive anchor exists (implies C-11 FAIL) or if the anchor is deferred entirely to Phase 3 or a post-scoring summary.
- Distinction from C-11: C-11 asks *does a positive evidence model exist in the scored body*; C-14 asks *is it placed at the earliest viable lifecycle phase* (Phase 2 entry) *so it can prevent errors rather than only illustrate them*.

**Formula impact:** N_aspirational bumped from 4 → 6. Full score still 100; golden threshold unchanged.

---

## Composite Score Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

PARTIAL counts as 0.5 toward pass count.
FAIL counts as 0.
Golden threshold: all essential PASS + composite >= 80.

N_essential = 5, N_recommended = 3, N_aspirational = 6.

---

## Criteria

### ESSENTIAL -- must all pass

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Rubric load verification** -- the output confirms the rubric was read; lists all criteria IDs and tiers, states the formula, and names the golden threshold before scoring begins | correctness | A load summary block exists (table, list, or prose) that names: (a) all criteria IDs with their tier labels, (b) the exact composite formula text, (c) the golden threshold condition, and (d) the count or list of outputs being scored. PARTIAL if any one of the four is missing. FAIL if the rubric is not referenced at all. |
| C-02 | **Per-criterion verdict matrix** -- every rubric criterion has a PASS/PARTIAL/FAIL verdict for every scored output | correctness | A table, prose block set, or equivalent structure exists where each criterion-output pair has an explicit verdict. No criterion-output cell is blank, merged-without-explanation, or implied. PARTIAL if verdicts exist for all criteria but one or more outputs are absent. FAIL if any criterion row is missing entirely. |
| C-03 | **Evidence for every verdict** -- every PASS/PARTIAL/FAIL verdict is backed by a direct quote, paraphrase, or specific structural reference to the scored output | correctness | No verdict stands alone as a label. Each criterion-output verdict is accompanied by text that references the output specifically -- either a quoted passage, a named section or line, or a structural observation about the output's format or content. PARTIAL if evidence exists for most verdicts but one or more are bare labels without reference. FAIL if a majority of verdicts lack evidence, or if evidence is present but consistently restates the criterion rather than quoting or referencing the output. |
| C-04 | **Composite score per output** -- each scored output has a numeric composite score computed from its verdict counts, shown with explicit calculation | correctness | A score is present for every output. The score is derived from a weighted formula (essential/recommended/aspirational tier counts). The calculation is shown explicitly -- e.g., "V-XX: E=X/5, R=X/3, A=X/6 -> composite = YY" -- not just the final number. PARTIAL if scores are present but calculations are omitted or partial. FAIL if scores are absent for any output. |
| C-05 | **Failure patterns section** -- criteria that receive zero PASS across all scored outputs are identified as failure patterns, or their absence is explicitly stated | coverage | A section labeled "Failure Patterns" (or equivalent) exists. Any criterion receiving no PASS across all N outputs is named. If no such criterion exists, the output states that explicitly (e.g., "No failure patterns -- all criteria passed in at least one output"). FAIL if the section is omitted entirely or if a criterion that failed across all outputs is not surfaced. |

### RECOMMENDED -- output is better with these

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Ranked leaderboard** -- all scored outputs are listed in descending composite score order; ties are noted explicitly | format | A leaderboard or ranking section exists. All N outputs appear, ordered from highest to lowest composite score. Ties are broken (with stated rule) or explicitly noted as tied. PARTIAL if the leaderboard exists but some outputs are absent or the order cannot be verified from stated scores. FAIL if the section is absent or ordering is implicit ("see scores above"). |
| C-07 | **Excellence signals** -- outputs scoring unusually high on a specific criterion are identified; any criterion where one output clearly leads the field is named with the structural feature that produced the outlier | depth | An "excellence signals" section exists. At least one specific output-criterion pair is highlighted with an explanation of what structural feature in that output produced the higher score. Generic comments ("V-05 scored highest overall") do not satisfy this criterion -- the signal must name the criterion and the mechanism. If no outlier pair exists, that is stated explicitly. |
| C-08 | **Per-output synthesis notes** -- each scored output has a brief narrative note explaining its key score drivers: what it did structurally that raised or lowered its score relative to other outputs | depth | A narrative note exists for each output beyond its verdict table or prose blocks. Each note explains at least one structural feature of the output that differentiates its score -- not a restatement of the verdict counts. PARTIAL if notes exist for most but not all outputs, or if notes only list counts without explaining mechanism. |

### ASPIRATIONAL -- raise the bar once essential/recommended are stable

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Regression signals** -- if a prior-round scorecard is provided, any criterion-output pair that degraded from PASS (or PARTIAL) to a lower verdict since the prior round is flagged | behavior | A regression section exists. If prior-round data was provided, any PASS->FAIL or PASS->PARTIAL degradation is named with the criterion ID, output ID, and prior verdict. If no regressions occurred, that is stated. If no prior-round file was provided or available, the output writes "No prior round data -- regression analysis cannot be performed" and the criterion receives PARTIAL (not FAIL). |
| C-10 | **Score arithmetic verification** -- the composite scores in the output are arithmetically correct given the stated verdict counts and formula | correctness | At least one composite score in the output can be independently verified from the stated PASS/PARTIAL/FAIL counts and formula. Arithmetic errors are absent or flagged. PARTIAL if scores are stated without enough detail to verify. FAIL if a score is demonstrably wrong given the stated counts. |
| C-11 | **Evidence positive anchor** -- the scoring output includes at least one worked example demonstrating what constitutes acceptable evidence for a criterion, showing the difference between criterion restatement and genuine output reference | depth | At least one criterion-output pair in the body of the scoring output includes a worked positive example: a model evidence cell that references a specific quote, named section, or locatable structural feature in the scored output. Anti-anchor text alone ("generic observations not tied to specific output text do not qualify") does not satisfy this criterion -- a positive model must exist. PARTIAL if a positive example exists but it is confined to the instructions rather than demonstrated within the scored body. FAIL if no positive evidence model appears anywhere in the output. |
| C-12 | **Discrepancy declaration** -- the arithmetic verification section includes an explicit match/mismatch declaration rather than an implicit pass-through | correctness | The arithmetic verification includes a labeled declaration field -- e.g., "Matches stated score: YES" or "Matches stated score: NO -- discrepancy: stated X, computed Y" -- that requires the scorer to affirm a match or name the exact discrepancy. Narrative statements like "the score checks out" or "verification performed" do not satisfy this criterion. PARTIAL if the match/mismatch is stated clearly in prose but without a labeled declaration field. FAIL if no explicit match/mismatch statement exists in the verification section, or if C-10 was not attempted. |
| C-13 | **Formula version delta declaration** -- when the applied rubric version introduces formula parameter changes from a known prior version, the scoring output explicitly names what changed before any score is computed | correctness | A delta notice appears before or within the Phase 1 LOAD block that names: (a) the prior rubric version or formula parameter value, and (b) the current value -- e.g., "N_aspirational=6 (was 4 in v2)" or "Aspirational denominator changed: 4 -> 6". The notice must appear in the scoring output, not only in the prompt instructions. PARTIAL if the current formula is correctly loaded (C-01 PASS) but no prior-vs-current comparison is made and a version change is in scope. FAIL if a formula version change is in scope and no delta is declared, or if an outdated denominator appears in any computation. When no rubric version change is in scope (first-ever scoring of this rubric, or scorer cannot determine prior version), write "No prior version delta -- scoring under v[N] as the baseline version" and the criterion receives PARTIAL (not FAIL). |
| C-14 | **Pre-scoring mechanism placement** -- the evidence positive anchor is positioned at Phase 2 entry, the earliest viable point, so it prevents evidence restatement before it can occur rather than correcting it afterward | correctness | The evidence positive anchor (MODEL CELL or equivalent) appears at or before Phase 2 entry -- in the first criterion-output evidence cell of the scoring section. If the anchor appears mid-way through Phase 2 or later, it cannot prevent earlier cells from containing criterion restatement. Post-scoring verification mechanisms (arithmetic re-derivation, discrepancy declaration field) are exempt from this criterion -- by design they belong at Phase 3. PARTIAL if a positive anchor exists (C-11 PASS) but is placed after the first three evidence cells of Phase 2. FAIL if no positive anchor exists in the scored body (implies C-11 FAIL), or if the anchor is deferred entirely to Phase 3 or a post-scoring summary. |

---

## Weight Summary

| Tier | Criteria | N | Weight |
|------|----------|---|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 |
| Recommended | C-06, C-07, C-08 | 3 | 30 |
| Aspirational | C-09, C-10, C-11, C-12, C-13, C-14 | 6 | 10 |

**Formula (explicit):**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

Score at all essential + all recommended + all aspirational: 100.
Score at all essential + all recommended + no aspirational: 90.
Score at all essential + no recommended + no aspirational: 60.
Golden threshold: all 5 essentials PASS AND composite >= 80.

---

## Scoring Notes

**C-01 (load verification):** The load summary can appear anywhere before the first output
is scored -- preamble, header block, or first phase. What matters is that it precedes scoring,
not that it appears in a specific format.

**C-02 (verdict matrix):** Formats vary -- table cells, prose blocks labeled by output, or
grouped criterion blocks -- as long as every criterion-output combination has a stated verdict.
Implied verdicts ("all PASS") count only when the N is small and the claim is unambiguous.

**C-03 (evidence):** Evidence that restates the criterion ("the output has a leaderboard")
does not satisfy C-03. Evidence must refer to the output's specific content: a quoted phrase,
a section title, a structural observation about the output's layout, or a line-level reference.
The test: could you find the referenced feature in the output using only the evidence text?

**C-04 (composite score):** "Explicit calculation" means the tier counts are stated before the
final score is given (e.g., "E=4/5, R=2/3, A=3/6"). A final number alone is PARTIAL.

**C-05 (failure patterns):** The section is required even when empty. The correct empty-section
text is: "No failure patterns -- all criteria passed in at least one output." Omitting the
section entirely is FAIL even when the scoring otherwise looks complete.

**C-06 (leaderboard):** A table that happens to be sorted by score satisfies C-06 only if the
sort order is unambiguous. "See scores above" or a pointer to the composite score table does
not satisfy C-06 -- the ranking must be restated as a ranked list or explicitly sorted table.

**C-07 (excellence signals):** "V-05 scored highest overall" is not an excellence signal. An
excellence signal requires a specific output-criterion pairing with a structural explanation.
Example: "V-03 leads on C-02 because it names the line number of the evidence quote in each
cell, making every verdict independently verifiable without re-reading the output."

**C-08 (per-output notes):** Notes that only list "PASS x4, PARTIAL x1" do not satisfy C-08.
The note must explain what the output did structurally that drove its result.

**C-09 (regression):** Round N/A rule: if no prior-round file exists, writing the prescribed
N/A statement earns PARTIAL. Omitting the section entirely earns FAIL.

**C-10 (arithmetic):** Score this criterion by picking one output and verifying its composite
from the stated counts and formula. PARTIAL if counts are absent (cannot verify). FAIL only
if a demonstrable arithmetic error exists.

**C-11 (evidence positive anchor):** The distinction between C-03 and C-11 is level of
demonstration. C-03 asks: does evidence exist? C-11 asks: does the scoring output model what
good evidence looks like? An output can pass C-03 (evidence is present) while failing C-11
(the scorer never showed what a well-formed evidence cell looks like, so borderline cells
recur across criteria). The positive anchor need not be a separate section -- a criterion-output
cell that is demonstrably complete (specific quote, locatable structural reference) satisfies
C-11 as a model, provided it is not the only non-trivial cell.

**C-12 (discrepancy declaration):** C-12 is a tightening of C-10. C-10 asks: is the arithmetic
correct? C-12 asks: did the scorer declare the result explicitly, in a form that forces a
binary choice? A scorer who writes "the formula gives 82, matching the stated score" satisfies
C-12 at PARTIAL level. A scorer who uses a labeled declaration field with an explicit YES/NO
and discrepancy slot satisfies C-12 at PASS level. The distinction matters because implicit
pass-throughs allow silent errors to propagate when scorers are rushed.

**C-13 (formula version delta):** The N/A rule mirrors C-09: if no prior rubric version is
identifiable from context, write the prescribed baseline statement ("No prior version delta --
scoring under v[N] as the baseline version") to earn PARTIAL. The goal is to force scorers to
think explicitly about whether they are applying the right formula version, even when the answer
is "I cannot check." Omitting all version-delta reasoning earns FAIL when a version bump is
in scope, PARTIAL when baseline status cannot be determined.

**C-14 (pre-scoring mechanism placement):** "Phase 2 entry" means the first evidence cell
written in the scoring section -- before any verdicts have been rendered. The MODEL CELL or
equivalent anchor must appear at this position because once the first few cells are written,
the scoring pattern is established and later anchors can correct but not prevent. The three-cell
grace window in the PARTIAL condition exists to accommodate prompt designs that use a brief
preamble before the first full-model cell; this window should not be used to justify deferring
the anchor to mid-scoring.

---

## Design Notes

**Why C-01 (load verification) is Essential, not Recommended:**
The prior cycle showed that scorers who skip or abbreviate the load step produce verdict
matrices with incorrect criterion counts, missing N/A rules, and wrong formula denominators.
A missing load summary is a leading indicator of downstream errors in C-02 through C-04.
Making it Essential surfaces this class of error early.

**Why C-03 (evidence) requires explicit output reference, not restatement:**
The highest-frequency failure mode in the prior cycle (observed across Rounds 1-6) was
scorers writing evidence that restates the criterion name instead of quoting the output.
"The output provides evidence for each verdict" is not evidence; it is circular. The pass
condition is written to force a specific reference because generic observations consistently
produced scorecards that could not drive rubric evolution -- they had no diagnostic content.

**Why C-05 (failure patterns) is Essential:**
Failure patterns are the primary value of batch scoring over single-output scoring. A score
report that does not surface criteria failing across all outputs cannot tell you whether the
rubric has a gap or the skill has a design issue. Without this section, the scoring exercise
cannot produce actionable output. Demoting it to Recommended would allow outputs to pass
golden threshold while omitting the analysis that makes batch scoring useful.

**Why C-06 (leaderboard) is Recommended, not Essential:**
The leaderboard is a navigation aid, not a primary output. The composite scores in C-04
contain the same information; the leaderboard reorganizes them for readability. A scoring
output missing only the leaderboard is still useful for rubric evolution -- it is degraded,
not broken.

**Why C-11 (evidence positive anchor) is Aspirational, not Recommended:**
C-03 already requires that evidence exists and references the output. C-11 is a quality
multiplier: it asks whether the scoring output itself teaches correct evidence behavior by
demonstrating a complete positive example. This is a higher bar because it requires the
scorer to internalize the distinction between restatement and reference well enough to
model it -- not just to avoid the worst case. This behavior emerged once in Round 1 (V-01,
C-04 CALC slot) as an excellence signal; it is not yet the norm across variations.

**Why C-12 (discrepancy declaration) is Aspirational, not part of C-10:**
C-10 at PASS level already requires arithmetic correctness. C-12 is a structural discipline
criterion: it asks whether the output forces an explicit declaration rather than allowing
a silent pass-through. The Round 1 V-01 excellence signal was the [YES | NO -- discrepancy:]
field, which makes arithmetic errors visible even when the scorer is not looking for them.
This property -- making errors structurally visible -- is aspirational because it requires
intentional output design beyond what C-10 mandates.

**Why C-13 (formula version delta) is Aspirational, not Essential:**
C-01 already requires that the current formula is loaded correctly. C-13 is a versioning
discipline criterion: it asks whether the scorer consciously confirmed they upgraded from the
prior formula parameters. This matters most during rubric evolution (when N values change)
and least when a rubric is applied for the first time. Because most scorecards are not the
first application of a new rubric version, the failure mode C-13 addresses -- silent carry-over
of an outdated denominator -- is real and recurring. The R2 FORMULA CHANGE ALERT signal (V-03)
is the first observed prompt mechanism to address it proactively rather than reactively.
The criterion is Aspirational rather than Essential because a scorecard missing this delta
notice can still be correct if the scorer happened to use the right denominator; the risk
is elevated but the failure is not structural.

**Why C-14 (pre-scoring mechanism placement) is Aspirational, not part of C-11:**
C-11 requires that a positive evidence anchor exists somewhere in the scored body. C-14
asks whether that anchor is placed at Phase 2 entry -- the earliest point it can prevent
errors rather than only illustrate them. A positive anchor that appears mid-way through
scoring can model correct behavior for future cells but cannot retroactively correct earlier
ones. The R2 V-01 excellence signal was the MODEL CELL INSTRUCTION firing at Phase 2 entry
as the first cell written, before any borderline restatement could occur. This temporal
property is separable from C-11's existence property: an output can pass C-11 (anchor
exists) while failing C-14 (anchor fires too late). The criterion is Aspirational because
it requires deliberate lifecycle design -- knowing not just to include the anchor, but to
place it where it has maximum preventive effect.
