# quest-score — Prompt Variations V-01 through V-05

---

## V-01 — Single-axis: Output Format (Table-Dominant Matrix)

**Axis:** Table-dominant output — verdict matrix is the primary artifact; evidence embedded as sub-rows; prose minimized to structured lists throughout.

**Hypothesis:** Dense tabular structure forces complete cell population (C-01) and collapses ambiguity about what "evidence" means (C-02) by requiring a quoted string in every cell — a blank cell is visually obvious; a paraphrase in a cell slot is harder to sneak past.

---

```
Score the provided skill outputs against the active rubric.

## Inputs

- Outputs: all files or content blocks provided above, labeled OUT-01, OUT-02, etc. in order.
- Rubric: read `simulations/quest/rubrics/quest-score-rubric-2026-03-15.md` before scoring.
- Prior round: if a prior score file is provided, read it; otherwise treat as "no prior data."

## Required Output Structure

### 1. Verdict Matrix

Produce a table with criteria as rows (C-01 through C-10) and each output as a column.
Every cell must contain two lines:
- Line 1: PASS / PARTIAL / FAIL
- Line 2: a direct structural quote from that output (in "quotes") that justifies the verdict

Do not leave any cell blank. Do not substitute a paraphrase or a criterion restatement for a quote.

| Criterion | OUT-01 | OUT-02 | (one column per output) |
|-----------|--------|--------|------------------------|
| C-01 Complete verdict matrix | PASS — "…" | FAIL — "…" | … |
| C-02 Evidence per verdict | … | … | … |
| C-03 Formula-correct composite | … | … | … |
| C-04 Ranked leaderboard | … | … | … |
| C-05 Failure patterns identified | … | … | … |
| C-06 Excellence signals | … | … | … |
| C-07 Regression signals | … | … | … |
| C-08 Per-output summary note | … | … | … |
| C-09 Golden threshold declaration | … | … | … |
| C-10 Failure-pattern root-cause | … | … | … |

### 2. Composite Score Table

| Output | E-pass (C-01..05) | R-pass (C-06..08) | A-pass (C-09..10) | Score |
|--------|-------------------|-------------------|-------------------|-------|
| OUT-01 | N.N / 5 | N.N / 3 | N / 2 | XX.X |
| … | … | … | … | … |

PARTIAL = 0.5 for essential and recommended; PARTIAL = 0 (not counted) for aspirational.
Formula: `(E/5 × 60) + (R/3 × 30) + (A/2 × 10)`. Show arithmetic for every output.

### 3. Ranked Leaderboard

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | OUT-XX | XX.X | YES |
| 2 | OUT-XX | XX.X | NO — C-03 FAIL |
| … | … | … | … |

Golden = all C-01..C-05 are PASS AND composite >= 80.
Ties: assign equal rank, label "(tied)".

### 4. Failure Pattern Table

| Criterion | PASS Count | Diagnosis |
|-----------|------------|-----------|
| C-XX | 0 / N | rubric gap / skill design issue — [one sentence] |

If no criterion has zero PASS: single row "No universal failures detected."

### 5. Excellence Signals

| Criterion | Output | Structural Mechanism |
|-----------|--------|----------------------|
| C-XX | OUT-XX | [what this output did that others did not] |

If none: single row "No excellence signals detected."

### 6. Regression Signals

| Criterion | Output | Prior Round | Current Round |
|-----------|--------|-------------|---------------|
| C-XX | OUT-XX | PASS | FAIL |

If no prior data: "No prior round data."
If no regressions: "No regressions detected."

### 7. Per-Output Notes

| Output | Note |
|--------|------|
| OUT-01 | [1-3 sentences: primary differentiator or primary miss — structural content, not a score restatement] |
| … | … |
```

---

## V-02 — Single-axis: Phrasing Register (Conversational Imperative)

**Axis:** Direct "your job is / do X then Y" voice; numbered steps replace section headers; no table templates provided — model generates structure from understanding, not from a filled-in shell.

**Hypothesis:** Imperative register with step-by-step instructions reduces structural drift (missing sections) by framing the output as a checklist of things to do rather than a document template to fill in — each step has a clear completion condition.

---

```
Your job: read the outputs, apply the rubric, produce a score report.

Before you write a single word of output, read the rubric at
`simulations/quest/rubrics/quest-score-rubric-2026-03-15.md`.
Know all ten criteria (C-01 through C-10), their tiers, and the composite formula.

---

**Step 1 — Assign IDs**

Label each output OUT-01, OUT-02, etc. in the order you received them.
List them at the top of your output so the reader knows which file is which.

**Step 2 — Score every criterion for every output**

Go criterion by criterion: C-01 first, then C-02, all the way to C-10.
For each criterion-output pair:
- Decide: PASS, PARTIAL, or FAIL.
- Pull a direct quote from the output as your evidence. Not a description — a quote, in
  quotation marks, from that specific output.
- If the output does not have the required element, write FAIL. Quote "[element absent]"
  only after confirming the section genuinely does not exist.

Format this as a verdict matrix table (rows = criteria, columns = outputs).
Every row populated. Every column populated. Every cell has a quote.

**Step 3 — Compute composite scores**

For each output:
- Count essential PASSes (C-01..C-05). A PARTIAL counts as 0.5.
- Count recommended PASSes (C-06..C-08). A PARTIAL counts as 0.5.
- Count aspirational PASSes (C-09..C-10). PARTIAL does not count at all.
- Apply: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/2 × 10)`
- Show the numbers. Don't just give the final score — show what went into it.

**Step 4 — Rank them**

Put all outputs in a list from highest score to lowest.
If two tie, say they tie and give them the same rank.
Each entry: rank, output ID, score, golden (YES or NO — if NO, say exactly why).

Golden means: every one of the five essential criteria is PASS, and composite >= 80.

**Step 5 — Find failure patterns**

A failure pattern is any criterion where zero outputs got PASS.
If you find one: "C-XX failed universally. This looks like a [rubric gap / skill design issue]
because [one sentence]."
If there are none: "No universal failures detected."

**Step 6 — Find excellence signals**

An excellence signal is when one output does noticeably better than the others on a specific
criterion. Name the output, name the criterion, say what structural thing it did that the others
did not. If nothing stands out: "No excellence signals detected."

**Step 7 — Check for regressions**

If you have a prior-round score file: compare each criterion-output verdict against it.
If anything got worse (PASS → PARTIAL, PASS → FAIL, PARTIAL → FAIL), flag it: output,
criterion, what it was before, what it is now.
If no prior data: say so. If no regressions: say so.

**Step 8 — Write a note for each output**

1-3 sentences per output. What was its main strength — the thing that explains its rank?
Or what was its main miss — the gap that cost it the most points?
This is not a restatement of the score. Name the structural feature.
```

---

## V-03 — Single-axis: Lifecycle Emphasis (Explicit Phase Gates)

**Axis:** Multi-phase structure with hard gate checks before proceeding; each phase has an entry condition, specific work, and an exit artifact that feeds the next phase.

**Hypothesis:** Explicit gates prevent the most common failure mode — jumping from partial verdicts to synthesis — which produces hollow evidence quotes (C-02) and skipped synthesis sections (C-05 through C-08). A gate makes the skip visible.

---

```
Score N skill outputs against the quest-score rubric.
Complete each phase in full before proceeding to the next.

---

## Phase 0 — Setup

Read `simulations/quest/rubrics/quest-score-rubric-2026-03-15.md` in full.

Confirm you can state:
- All ten criterion IDs (C-01 through C-10) and their one-line descriptions
- Tier assignments: essential (C-01..C-05), recommended (C-06..C-08), aspirational (C-09..C-10)
- Tier weights: 60 / 30 / 10 points
- PARTIAL counting: 0.5 for essential and recommended; 0 for aspirational
- Formula: `(E/5 × 60) + (R/3 × 30) + (A/2 × 10)`
- Golden threshold: all C-01..C-05 PASS AND composite >= 80

Assign IDs to the inputs: OUT-01, OUT-02, etc.

**Gate check:** Do not proceed until you have read the rubric and assigned IDs.

---

## Phase 1 — Per-Criterion Scoring

For each criterion C-01 through C-10, in order:

1. State the criterion text (one sentence from the rubric pass condition).
2. For each output, assign a verdict: PASS, PARTIAL, or FAIL.
3. For each verdict, provide a direct structural quote — the specific text in that output that
   drove your verdict. The quote must be unique to that output (not a criterion restatement,
   not a paraphrase, not a description that could apply to any output).

Format as a verdict matrix table:

| Criterion | OUT-01 | OUT-02 | … |
|-----------|--------|--------|---|
| C-01 | PASS — "quote" | FAIL — "quote" | … |
| C-02 | … | … | … |
| … | … | … | … |

**Gate check:** Every cell in the matrix must be populated with a verdict AND a quote
before you proceed to Phase 2.

---

## Phase 2 — Composite Scoring

For each output, compute the composite score:

1. E = sum of PASS-equivalents for C-01..C-05 (PASS=1, PARTIAL=0.5, FAIL=0)
2. R = sum of PASS-equivalents for C-06..C-08 (PASS=1, PARTIAL=0.5, FAIL=0)
3. A = count of PASSes for C-09..C-10 (PARTIAL does not count)
4. Score = (E/5 × 60) + (R/3 × 30) + (A/2 × 10)

Show a table with columns: Output | E | R | A | Score.
Show the arithmetic for each row.

**Gate check:** Verify no score exceeds 100 or is negative. Recompute if so.

---

## Phase 3 — Leaderboard

Rank all outputs by composite score, descending.
Declare golden status for each output explicitly.

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | OUT-XX | XX.X | YES |
| 2 | OUT-XX | XX.X | NO — [specific failing condition] |
| … | … | … | … |

Ties: assign equal rank, label "(tied)".

**Gate check:** Every output assigned in Phase 0 appears exactly once.

---

## Phase 4 — Failure Pattern Analysis

Inspect the Phase 1 verdict matrix. Identify any criterion where PASS count = 0.

For each universal failure:
- Name the criterion
- State PASS count (0 out of N)
- Classify: rubric gap (criterion is misspecified or unreachable for this skill class) or
  skill design issue (the skill reliably fails to produce this output element)
- One sentence of rationale

If no universal failures: "No universal failures detected."

---

## Phase 5 — Excellence and Regression Signals

**Excellence signals**

For each criterion: did one output score meaningfully above the field?
If yes: name the output, name the criterion, describe the structural mechanism in 1-2 sentences.
If none: "No excellence signals detected."

**Regression signals**

If prior-round score data is available:
Compare current verdicts to prior-round verdicts for each criterion-output pair.
Flag any degradation: PASS→PARTIAL, PASS→FAIL, or PARTIAL→FAIL.
For each: output ID, criterion, prior verdict, current verdict.

If no prior data: "No prior round data available."
If no regressions: "No regressions detected."

---

## Phase 6 — Per-Output Summary Notes

Write 1-3 sentences for each output. Each note must name either:
- The structural feature that explains its rank (differentiator), OR
- The most significant missing mechanism (primary miss)

Do not restate the composite score. Do not write a note that could apply to any output.
Structural content only.
```

---

## V-04 — Combination: Role Sequence + Prose-First Output Format

**Axes:**
1. **Role sequence** — two named roles run sequentially: SCORER (verdicts only) then ANALYST (synthesis only)
2. **Output format** — prose-first with a compact summary table at the end; no table templates for the scoring phase

**Hypothesis:** Separating the scoring act from the synthesis act improves evidence quote quality (SCORER is not yet anticipating rankings, reducing motivated reasoning in quote selection) and sharpens excellence/regression signals (ANALYST reads a complete matrix before writing, avoiding premature pattern identification).

---

```
Two roles execute in sequence. SCORER runs first and may not skip ahead to synthesis.
ANALYST runs second and reads SCORER's complete output before writing anything.

---

## ROLE: SCORER

Your only job: produce verdicts with evidence. Do not compute composite scores. Do not rank.
Do not synthesize. Look at the outputs, apply the criteria, write the matrix.

**Before scoring**

Read `simulations/quest/rubrics/quest-score-rubric-2026-03-15.md`.
Note the pass condition for each of the ten criteria — especially what counts as genuine
evidence versus a restatement or generic description.
Assign IDs to the outputs: OUT-01, OUT-02, etc.

**Verdict Matrix**

For each criterion C-01 through C-10, for each output:
- Assign a verdict: PASS, PARTIAL, or FAIL
- Immediately below the verdict, write the evidence: a structural quote from that specific
  output, in quotation marks, that is your single strongest justification

Write every row. Write every column. Do not move on until the full matrix is populated.

---
[SCORER's complete verdict matrix appears here before ANALYST begins]
---

## ROLE: ANALYST

Read the SCORER's complete verdict matrix. Now write the score report.

**Section A — Composite Scores**

For each output, apply: `(E/5 × 60) + (R/3 × 30) + (A/2 × 10)`
where E = PASS-equivalents in C-01..C-05, R = PASS-equivalents in C-06..C-08,
A = PASSes (not PARTIALs) in C-09..C-10.

Write this in prose, showing the arithmetic: "OUT-01 has 4 essential passes (including one
PARTIAL worth 0.5), 2 recommended passes, and 1 aspirational pass, giving
(4.5/5 × 60) + (2/3 × 30) + (1/2 × 10) = 54 + 20 + 5 = 79."

**Section B — Ranked Leaderboard**

List all outputs highest to lowest. For each: output ID, score, golden status.
Golden = all C-01..C-05 PASS AND composite >= 80.
If NO, state the specific failing condition. Ties noted explicitly.

**Section C — Failure Patterns**

A failure pattern is any criterion with zero PASS across all outputs.
For each universal failure, write two sentences:
(1) What the criterion requires that no output provided.
(2) Whether this is a rubric gap or a skill design issue, and why.

If no universal failures: "No universal failures detected."

**Section D — Excellence Signals**

Scan the verdict matrix for outlier high performance: a criterion where one output's structural
approach clearly outperformed the others. For each: name the output, name the criterion, and
in 1-2 sentences describe the mechanism — what did this output do structurally that others
did not? If no outliers: "No excellence signals detected."

**Section E — Regression Signals**

If prior-round data is provided: for each verdict that degraded (PASS→PARTIAL, PASS→FAIL,
PARTIAL→FAIL), write one sentence naming the degradation and what is now absent that was
present before. If no prior data: "No prior round data." If no regressions: "No regressions
detected."

**Section F — Per-Output Notes**

For each output, 1-3 sentences. Do not restate the score. Name the structural feature that
best explains this output's rank, or the single most significant gap relative to golden.

**Section G — Summary Table**

| Output | Score | Golden | Key Signal |
|--------|-------|--------|------------|
| OUT-01 | XX.X | YES / NO | [one phrase: differentiator or miss] |
| … | … | … | … |
```

---

## V-05 — Combination: Lifecycle + Formal/Technical Register + Inertia Framing

**Axes:**
1. **Lifecycle emphasis** — explicit numbered phases with defined entry conditions and exit artifacts
2. **Phrasing register** — formal/technical language; passive-voice framing for procedures; precision vocabulary from the rubric spec
3. **Inertia framing** — excellence and regression sections anchor observations against what an informal (status-quo) reviewer would and would not detect, making the structured scoring valuable beyond "a human could have noticed this"

**Hypothesis:** Inertia framing in the signal sections (excellence, regressions) produces more diagnostic observations — not just "output X did well on C-06" but "this mechanism would be invisible to informal review, which is where this rubric earns its keep." This makes the score report useful to someone deciding whether the rubric is worth maintaining.

---

```
TASK: Structured evaluation of N skill outputs against the quest-score rubric (v2026-03-15).

This evaluation follows a defined lifecycle. Each phase produces a mandatory artifact.
Phases are sequential. Artifacts from prior phases are inputs to subsequent phases.

---

### Phase 1: Instrument Calibration

Read `simulations/quest/rubrics/quest-score-rubric-2026-03-15.md` in full. Internalize:
- Criteria C-01 through C-10 with their tier assignments and formal pass conditions
- Tier weights: essential (C-01..C-05) = 60 pts, recommended (C-06..C-08) = 30 pts,
  aspirational (C-09..C-10) = 10 pts
- PARTIAL scoring: 0.5 pass-equivalent for essential and recommended; 0 for aspirational
- Composite formula: `score = (E/5 × 60) + (R/3 × 30) + (A/2 × 10)`
  where E, R, A are PASS-equivalent counts for each tier
- Golden threshold: all C-01..C-05 rated PASS AND composite score >= 80

Phase 1 artifact: internal calibration. No written output required.

---

### Phase 2: Verdict Matrix Construction

Assign identifiers to all provided outputs: OUT-01, OUT-02, etc.

For each criterion C-01 through C-10, evaluate each output and record:
- A verdict: PASS | PARTIAL | FAIL
- A verbatim structural quote drawn from the specific output under evaluation that constitutes
  the primary justification for the verdict

The quote must be drawn from that output's text (not from the rubric criterion, not from
another output). If the required structural element is absent, record FAIL with the notation
"[element absent — section not present in output]".

No cell in the resulting matrix may be left blank.

Phase 2 artifact: verdict matrix (table, rows = C-01..C-10, columns = OUT-01..OUT-N).

---

### Phase 3: Quantitative Scoring

For each output, compute the composite score from the Phase 2 verdict matrix.

Show work in tabular form:
1. E = sum of PASS-equivalents across C-01..C-05
2. R = sum of PASS-equivalents across C-06..C-08
3. A = count of PASSes (not PARTIALs) across C-09..C-10
4. Score = (E/5 × 60) + (R/3 × 30) + (A/2 × 10)
5. Golden evaluation: YES if all of C-01..C-05 are PASS AND score >= 80;
   otherwise NO with the specific failing condition stated

Phase 3 artifact: scoring table (columns: Output | E | R | A | Score | Golden).

---

### Phase 4: Leaderboard Generation

Rank all evaluated outputs by composite score, descending. Ties assigned equal rank with
"(tied)" notation. Each leaderboard entry includes: rank, output ID, composite score,
golden status.

Phase 4 artifact: ranked leaderboard.

---

### Phase 5: Pattern and Signal Extraction

This phase produces three analytical artifacts. In each, observations are evaluated against
two reference baselines:

- **Rubric baseline**: the criterion's formal pass condition as written
- **Status-quo baseline**: what an attentive but unstructured reader, reviewing these outputs
  without rubric criteria, would likely notice or fail to notice

The status-quo baseline question is: *does this observation require structured scoring to
detect, or would informal review surface it anyway?* Observations that are only detectable
via structured scoring represent the highest-value findings.

**5a — Failure Patterns**

Identify all criteria for which no output received PASS. For each:
- State PASS count (0 of N)
- Classify root cause:
  - *rubric gap*: the criterion is misspecified, inapplicable, or unreachable for this
    skill class; the criterion itself should be revised
  - *skill design issue*: the criterion is sound, but the skill consistently fails to
    generate the required output element; the skill definition should be revised
- State whether the failure is detectable via informal review or only via rubric application

If no universal failures: "No universal failures detected."

**5b — Excellence Signals**

Identify criterion-output pairs where one output's execution substantially exceeds the field.
For each:
- Name the criterion and output
- Describe the structural mechanism in 1-2 sentences
- Classify detectability: would an informal reader notice this advantage, or does it require
  rubric-level criterion comparison to see?

Prioritize signals in the second category — they represent unique value added by structured
scoring over informal review.

If no signals: "No excellence signals detected."

**5c — Regression Signals**

If prior-round score data is available, compare Phase 2 verdicts against prior-round verdicts
for each criterion-output pair. For each degradation (PASS→PARTIAL, PASS→FAIL, PARTIAL→FAIL):
- State prior verdict, current verdict
- Identify the structural element now absent that was previously present
- Note whether the regression would be caught by an informal re-read or requires verdict
  comparison to detect

If no prior data: "No prior round data available."
If no regressions: "No regressions detected."

---

### Phase 6: Per-Output Narrative

For each output, produce a 1-3 sentence narrative note. Requirements:
- Must reference a specific structural feature of that output (not a score restatement)
- Must identify either the primary differentiator (the structural mechanism that explains
  its rank relative to the field) or the primary miss (the structural gap with the greatest
  composite score impact)
- Must be individuated — the note must not be applicable to any other output in the set

Phase 6 artifact: one narrative note per output.

---

### Phase 7: Report Assembly

Assemble all phase artifacts into a single ordered report in the following sequence:
1. Verdict Matrix (Phase 2)
2. Composite Score Table (Phase 3)
3. Leaderboard (Phase 4)
4. Failure Patterns (Phase 5a)
5. Excellence Signals (Phase 5b)
6. Regression Signals (Phase 5c)
7. Per-Output Notes (Phase 6)
```

---

## Variation Summary

| ID | Axis | Key Bet |
|----|------|---------|
| V-01 | Output format (table-dominant) | Blank cell is visually obvious; forces C-01 + C-02 compliance |
| V-02 | Phrasing register (imperative) | Step-checklist framing reduces section omissions |
| V-03 | Lifecycle emphasis (phase gates) | Hard gates prevent jumping to synthesis before matrix is complete |
| V-04 | Role sequence + prose-first format | Scoring/synthesis split improves evidence quote quality and signal depth |
| V-05 | Lifecycle + formal register + inertia framing | Status-quo baseline makes excellence/regression sections diagnostic, not descriptive |
