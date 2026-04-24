# quest-score Variate — Round 1
# Generated: 2026-03-15

---

## Context: what informed this round

Round 1 targets the v1 rubric. This is the first round of `quest-score` variation — no prior
scorecard exists, no champion prompt exists, and no excel signals have been identified yet.

The v1 rubric defines 8 criteria across 3 tiers:

- **Essential (60 pts)**: C-01 verdict matrix, C-02 evidence per verdict, C-03 composite score,
  C-04 ranked leaderboard, C-05 failure patterns
- **Recommended (30 pts)**: C-06 excellence signals, C-07 per-output evidence notes
- **Aspirational (10 pts)**: C-08 regression signals

The design note in the rubric is explicit: C-05 (failure patterns) is classified Essential, not
Recommended — this is the primary diagnostic value of batch scoring, and a report without it
cannot drive rubric evolution. Round 1 must test whether each variation produces this section
reliably, even when no criterion fails across all outputs (the section is required even when empty).

C-08 has a first-round N/A condition: the rubric prescribes PARTIAL (not FAIL) when the scorer
explicitly notes "no prior round data available." Round-1 outputs should not be penalized for
data that cannot exist.

**v1 rubric counts**: E=5 (C-01..C-05), R=2 (C-06..C-07), A=1 (C-08)
**Formula**: `(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/1 * 10)`
**Golden**: all 5 essentials PASS AND composite >= 80
**N/A condition**: C-08 PARTIAL (not FAIL) when scorer states "no prior round data available"

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | Output format — prose blocks | Replacing the compact verdict table with criterion-by-criterion prose blocks forces the scorer to articulate the mechanism behind each verdict rather than reducing it to a table symbol. Each block requires a full evidence sentence with a direct quote and a one-sentence "why." This directly targets C-02 (evidence per verdict) and C-07 (per-output notes), whose pass conditions require mechanism, not presence. |
| B | Lifecycle emphasis — explicit phase gates | Hard STOP tokens between Load, Scoring, and Synthesis phases make synthesis non-optional. Without a gate, the scorer can end after the last per-output table; C-05 (failure patterns) and C-06 (excellence signals) are the most commonly skipped sections because they require cross-output reasoning that appears after per-output work is done. The gate makes omission structurally visible as a missing required token. |
| C | Inertia framing — bad-scorer anti-pattern | Showing a concrete "WEAK SCORER" example at the top — generic evidence, missing failure-patterns section, leaderboard that says "see above" — gives the scorer a real-time negative anchor cheaper than an abstract instruction ("write specific evidence"). This targets C-02 (evidence grounding) by anchoring against the exact failure mode most likely to occur. |

Single-axis runs: V-01 (A), V-02 (B), V-03 (C)
Combinations: V-04 (A+B), V-05 (A+B+C)

Rubric in scope: `simulations/quest/rubrics/quest-score-rubric-v1-2026-03-15.md`
Formula: `(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/1 * 10)`
N_essential=5, N_recommended=2, N_aspirational=1
Golden threshold: all 5 essentials PASS AND composite >= 80

---

## V-01 — Output format: prose blocks

**Axis**: A — Output format
**Hypothesis**: The compact verdict table satisfies C-01 structurally, but its cells compress
evidence to fragments that can pass C-02 with a partial quote and pass C-07 with a count. Prose
blocks raise the floor: each criterion-output combination requires a full sentence with a direct
quote and a one-sentence explanation of why the verdict follows from it. The format naturally
generates C-07 content in-situ (the "why" sentence is the mechanism the rubric requires) rather
than in a separate section that can be deferred and dropped. The risk is verbosity crowding out
the synthesis sections — this round-1 test measures whether format richness trades off against
synthesis completeness.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Step 1 — Load**

Read the rubric. Extract: all criteria IDs, their tier (Essential / Recommended / Aspirational),
their pass conditions, the composite score formula, the golden threshold, and any N/A rules.
Read all N output files.

Write a brief load summary:
```
Criteria: [list IDs and tiers]
Formula: [exact formula text]
Golden threshold: [condition]
N/A rules: [list any criteria with N/A conditions]
N outputs to score: [N]
```

**Step 2 — Score each output**

For each output V-XX, write one prose-block section. Each section contains one prose block per
rubric criterion, in criterion order. Each block follows this exact structure:

```
**C-NN — [criterion short name]** | [PASS / PARTIAL / FAIL]
*Evidence*: [one or more sentences; must include a direct quote from the output or a specific
structural reference — e.g., "The output includes the line: '...' " or "Section X contains...";
generic observations not tied to specific output text do not qualify]
*Why*: [one sentence explaining why this evidence supports the verdict — name the mechanism,
not just the criterion]
```

For C-08 (regression signals): if no prior-round file is provided or available, write:
`PARTIAL — no prior round data available; regression analysis cannot be performed`
Do not write FAIL for this condition.

**Step 3 — Synthesize**

After scoring all N outputs, write four synthesis sections:

**Composite Scores**
For each output, apply the formula to its verdict counts:
- essential_pass = count of PASS verdicts in C-01..C-05 (PARTIAL counts as 0.5)
- recommended_pass = count of PASS verdicts in C-06..C-07 (PARTIAL counts as 0.5)
- aspirational_pass = count of PASS verdicts in C-08 (PARTIAL counts as 0.5)
- composite = (essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/1 * 10)

Show each calculation explicitly: `V-XX: E=X/5, R=X/2, A=X/1 → composite = XX`

**Ranked Leaderboard**
List all outputs in descending composite score order. Ties: list tied outputs together and note
the tie. This section must exist even if all outputs have the same score.

**Failure Patterns**
Identify any criterion where zero outputs received PASS (or 0.5 PARTIAL as a pass). These are
failure patterns — they signal either a rubric gap or a skill design issue.
If no such criterion exists, write: `No failure patterns — all criteria passed in at least one output.`
This section is required. Do not omit it.

**Excellence Signals**
Identify any output-criterion pair where one output clearly leads the field on that criterion —
not just that it scored highest overall, but that one specific criterion shows a specific output
performing structurally differently from others. Name the output, the criterion, and what
structural feature produced the outlier result.
If no clear outlier pair exists, write: `No excellence signals identified in this scoring run.`

**Regression Signals**
If a prior-round scorecard was provided: compare each criterion-output verdict against the prior
round and flag any PASS → FAIL or PASS → PARTIAL regressions.
If no prior-round file was provided: write `No prior round data — regression analysis cannot be performed.`

**Step 4 — Write**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

where `{skill}` is the skill whose outputs were scored, `{round}` is the scoring round number,
and `{date}` is today's date in YYYY-MM-DD format.

---

## V-02 — Lifecycle emphasis: explicit phase gates

**Axis**: B — Lifecycle emphasis
**Hypothesis**: C-05 (failure patterns) and C-06 (excellence signals) are synthesis sections
that require cross-output reasoning — they can only be written after all per-output scoring is
done. Without a structural gate, the scorer can end immediately after the last output table
without producing them, and the prompt's instruction to "write synthesis sections" becomes a
soft suggestion that late-context pressure drops first. An explicit PHASE TOKEN — a required
verbatim string that must appear before the next phase can begin — makes this omission visible
as a structural error rather than a soft miss. The gate does not increase the quality of the
synthesis content; it ensures the content exists. This round-1 test measures whether a presence
gate alone is sufficient for C-05 and C-06, or whether quality enforcement must be added
separately.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** — the following phases must complete in order, each closing with its EXIT TOKEN
before the next phase begins:

| Phase | EXIT TOKEN |
|-------|------------|
| LOAD | `[LOAD COMPLETE]` |
| SCORING | `[SCORING COMPLETE — N outputs scored]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**Phase 1 — LOAD**

Read the rubric. Extract: all criteria IDs and tiers, pass conditions, the composite formula,
the golden threshold, and all N/A rules. Read all N output files.

Write this block verbatim (filled in):

```
Criteria loaded: [IDs and tiers, comma-separated]
Formula: [exact formula]
Golden threshold: [condition]
N/A rules: [list, or "none"]
Outputs loaded: [V-XX list]
```

Write the exact string: `[LOAD COMPLETE]`

---

**Phase 2 — SCORING**

For each output V-XX, produce one scoring table:

```
### V-XX: [axis label]

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Per-criterion verdict matrix | E | PASS/PARTIAL/FAIL | [direct quote or specific structural reference] |
| C-02 | Evidence for every verdict | E | PASS/PARTIAL/FAIL | [direct quote or specific structural reference] |
| C-03 | Composite score per output | E | PASS/PARTIAL/FAIL | [direct quote or specific structural reference] |
| C-04 | Ranked leaderboard | E | PASS/PARTIAL/FAIL | [direct quote or specific structural reference] |
| C-05 | Failure patterns called out | E | PASS/PARTIAL/FAIL | [direct quote or specific structural reference] |
| C-06 | Excellence signals | R | PASS/PARTIAL/FAIL | [direct quote or specific structural reference] |
| C-07 | Per-output evidence notes | R | PASS/PARTIAL/FAIL | [direct quote or specific structural reference] |
| C-08 | Regression signals | A | PASS/PARTIAL/FAIL | [quote, or "PARTIAL — no prior round data available"] |
```

Score all N outputs before writing the EXIT TOKEN.

Write the exact string: `[SCORING COMPLETE — N outputs scored]` (replace N with the actual count)

---

**Phase 3 — SYNTHESIS**

Write all five synthesis sections. Every section is required. Do not skip any section.

**Composite Scores**
For each output:
- Count PASS verdicts per tier (PARTIAL = 0.5)
- Apply: `(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/1 * 10)`
- Show the calculation: `V-XX: E=X/5, R=X/2, A=X/1 → composite = XX`

**Ranked Leaderboard**
List all outputs from highest to lowest composite score. Note ties explicitly.

**Failure Patterns**
List every criterion where NO output received PASS (PARTIAL or FAIL only across all N outputs).
These signal rubric gaps or systematic skill design issues.
If none: write `No failure patterns — all criteria earned PASS in at least one output.`

**Excellence Signals**
Name specific output-criterion pairs where one output clearly outperforms the others on that
criterion. State what structural feature produced the outlier.
If none: write `No excellence signals identified in this scoring run.`

**Regression Signals**
If prior-round data was provided: flag PASS → FAIL or PASS → PARTIAL regressions per criterion.
If not: write `No prior round data — regression analysis cannot be performed.`

Write the exact string: `[SYNTHESIS COMPLETE]`

---

**Phase 4 — WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write the exact string: `[WRITE COMPLETE]`

---

## V-03 — Inertia framing: bad-scorer anti-pattern

**Axis**: C — Inertia framing
**Hypothesis**: C-02 (evidence per verdict) is the criterion most vulnerable to the inertia
pattern: the scorer restates the criterion name instead of quoting the output, because restating
is faster and passes surface inspection. Abstract instructions ("write specific evidence") do not
anchor against the exact failure mode the way a concrete negative example does. When a labeled
"WEAK SCORER" block shows the exact form of bad evidence before any scoring begins, the scorer
has a real-time check: "does my evidence look like this?" This is cheaper than a per-cell
portability question (it fires once, at the top, not per cell) and more specific than a general
instruction. Round-1 tests whether this single anchor measurably improves C-02 compliance
without requiring per-cell mechanical checks.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**INERTIA PATTERN — read before scoring anything**

The following is an example of what a weak scorer produces. Do not produce output that resembles
this pattern.

```
WEAK SCORER EXAMPLE (do not produce this):

| C-01 | Verdict matrix | E | PASS | Output has a verdict matrix. |
| C-02 | Evidence per verdict | E | PASS | Output provides evidence for each verdict. |
| C-05 | Failure patterns | E | PASS | Output addresses failure patterns. |

[Leaderboard section omitted — see scores above]

[No failure patterns section]
```

The inertia failures above are:
1. **Generic evidence**: "Output has a verdict matrix" restates the criterion; it is not evidence.
   Evidence must quote or specifically reference the output: `"The output includes a table with
   rows C-01..C-08 and columns V-01..V-05 — every cell is populated."` is evidence.
2. **Missing required section**: The leaderboard must be an explicit ranked list, not a pointer
   to another section. The failure-patterns section must exist and either name patterns or
   explicitly state their absence — it cannot be omitted.
3. **No synthesis**: The PASS/FAIL table is not the whole output. Synthesis sections exist
   separately and are not optional.

Before writing each evidence cell, ask: "Does this evidence quote or specifically reference the
output, or does it restate the criterion?" If the latter, rewrite.

---

**Step 1 — Load**

Read the rubric. Extract: all criteria IDs and tiers, pass conditions, the composite formula,
the golden threshold, and all N/A rules. Read all N output files.

**Step 2 — Score each output**

For each output V-XX, produce one scoring table:

```
### V-XX: [axis label]

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Per-criterion verdict matrix | E | PASS/PARTIAL/FAIL | [quote or specific reference — not a restatement] |
| C-02 | Evidence for every verdict | E | PASS/PARTIAL/FAIL | [quote or specific reference — not a restatement] |
| C-03 | Composite score per output | E | PASS/PARTIAL/FAIL | [quote or specific reference — not a restatement] |
| C-04 | Ranked leaderboard | E | PASS/PARTIAL/FAIL | [quote or specific reference — not a restatement] |
| C-05 | Failure patterns called out | E | PASS/PARTIAL/FAIL | [quote or specific reference — not a restatement] |
| C-06 | Excellence signals | R | PASS/PARTIAL/FAIL | [quote or specific reference — not a restatement] |
| C-07 | Per-output evidence notes | R | PASS/PARTIAL/FAIL | [quote or specific reference — not a restatement] |
| C-08 | Regression signals | A | PASS/PARTIAL/FAIL | [quote, or "PARTIAL — no prior round data available"] |
```

**Step 3 — Synthesize**

After all N outputs are scored, write these sections:

**Composite Scores**
For each output, apply:
`(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/1 * 10)`
Show: `V-XX: E=X/5, R=X/2, A=X/1 → composite = XX`

**Ranked Leaderboard**
All outputs in descending composite score order. Ties noted explicitly. This section must be
an explicit ranked list — not a pointer to the score table.

**Failure Patterns**
Criteria where no output earned PASS. These signal rubric gaps or skill design issues.
If none: `No failure patterns — all criteria passed in at least one output.`
This section cannot be omitted.

**Excellence Signals**
Specific output-criterion pairs where one output structurally outperforms the others.
Name the output, the criterion, and the structural feature.
If none: `No excellence signals identified in this scoring run.`

**Regression Signals**
Prior-round degradations, or: `No prior round data — regression analysis cannot be performed.`

**Step 4 — Write**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-04 — Output format + lifecycle emphasis (A+B)

**Axes**: A + B — Prose blocks + explicit phase gates
**Hypothesis**: V-01 (prose) targets evidence and mechanism quality; V-02 (phase gates) targets
synthesis completeness. These two failure modes are largely independent: a scorer can write
rich prose per output and still drop the synthesis sections; a scorer can produce all synthesis
sections and still write generic evidence. The combination closes both gaps simultaneously. The
cost is length — prose blocks are longer than table rows, and phase gates add mandatory tokens.
Round-1 tests whether the combination produces outputs that are both evidence-rich (C-02, C-07)
and synthesis-complete (C-05, C-06) without the length increase causing synthesis compression.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** — complete in order, each phase closes with its EXIT TOKEN:

| Phase | EXIT TOKEN |
|-------|------------|
| LOAD | `[LOAD COMPLETE]` |
| SCORING | `[SCORING COMPLETE — N outputs scored]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**Phase 1 — LOAD**

Read the rubric. Extract: all criteria IDs and tiers, pass conditions, the composite formula,
the golden threshold, and all N/A rules. Read all N output files.

Write this block:
```
Criteria: [IDs and tiers]
Formula: [exact text]
Golden threshold: [condition]
N/A rules: [list or "none"]
Outputs: [V-XX list]
```

Write: `[LOAD COMPLETE]`

---

**Phase 2 — SCORING**

For each output V-XX, write one prose-block section. Each section has one block per criterion
in criterion order:

```
### V-XX: [axis label]

**C-01 — Per-criterion verdict matrix** | [PASS / PARTIAL / FAIL]
*Evidence*: [one or more sentences including a direct quote or specific structural reference
from this output — not a restatement of the criterion]
*Why*: [one sentence: what structural property of this output causes this verdict]

**C-02 — Evidence for every verdict** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific reference]
*Why*: [mechanism sentence]

**C-03 — Composite score per output** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific reference]
*Why*: [mechanism sentence]

**C-04 — Ranked leaderboard** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific reference]
*Why*: [mechanism sentence]

**C-05 — Failure patterns called out** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific reference]
*Why*: [mechanism sentence]

**C-06 — Excellence signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific reference]
*Why*: [mechanism sentence]

**C-07 — Per-output evidence notes** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific reference]
*Why*: [mechanism sentence]

**C-08 — Regression signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote, or "PARTIAL — no prior round data available"]
*Why*: [mechanism sentence, or "N/A — no prior data"]
```

Score all N outputs before writing the EXIT TOKEN.

Write: `[SCORING COMPLETE — N outputs scored]` (replace N with actual count)

---

**Phase 3 — SYNTHESIS**

Write all five sections. Every section is required.

**Composite Scores**
Count PASS/PARTIAL/FAIL per tier from the prose blocks above.
Formula: `(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/1 * 10)`
Show: `V-XX: E=X/5, R=X/2, A=X/1 → composite = XX`

**Ranked Leaderboard**
Explicit ranked list, descending. Ties noted.

**Failure Patterns**
Criteria where no output earned PASS across the run. Signal rubric gaps or skill design issues.
If none: `No failure patterns — all criteria passed in at least one output.`

**Excellence Signals**
Specific output-criterion pairs where structural differences produced outlier scores.
If none: `No excellence signals identified in this scoring run.`

**Regression Signals**
Prior-round degradations, or: `No prior round data — regression analysis cannot be performed.`

Write: `[SYNTHESIS COMPLETE]`

---

**Phase 4 — WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write: `[WRITE COMPLETE]`

---

## V-05 — Output format + lifecycle emphasis + inertia framing (A+B+C)

**Axes**: A + B + C — Prose blocks + explicit phase gates + bad-scorer anti-pattern
**Hypothesis**: V-04 (A+B) addresses independent failure modes — evidence quality and synthesis
completeness — but neither axis directly guards against the inertia pattern within prose blocks.
Prose format raises the floor but does not prevent restated evidence; it just makes the
restatement more visible. Adding the inertia anti-pattern block (C) closes the remaining gap:
the scorer has a negative anchor before Phase 2 begins, prose format forces full sentences, and
phase gates enforce synthesis presence. The three axes work at different points in the scoring
lifecycle — before (C), during (A), and between phases (B) — with no overlap. Round-1 tests
whether the combination produces the highest-scoring outputs without compressing synthesis
content under the weight of evidence-rich prose blocks.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** — complete in order, each phase closes with its EXIT TOKEN:

| Phase | EXIT TOKEN |
|-------|------------|
| LOAD | `[LOAD COMPLETE]` |
| SCORING | `[SCORING COMPLETE — N outputs scored]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**INERTIA PATTERN — read before scoring anything**

The following is what a weak scorer produces. Do not produce output that resembles this.

```
WEAK SCORER EXAMPLE (do not produce this):

**C-02 — Evidence for every verdict** | PASS
*Evidence*: The output provides evidence for each criterion verdict.
*Why*: Evidence is present throughout the output.

[No failure patterns section present]

[No leaderboard — scores can be inferred from the tables above]
```

The inertia failures:
1. **Restated evidence**: "The output provides evidence" restates the criterion. Evidence must
   quote or specifically reference the output text: the sentence, section header, or structural
   feature that causes the verdict.
2. **Missing failure patterns**: The section must exist. "No failure patterns" is a valid answer;
   omitting the section entirely is not.
3. **Implicit leaderboard**: The leaderboard must be an explicit ranked list. "Infer from above"
   does not satisfy C-04.

Before writing each *Evidence* line, ask: "Am I quoting or specifically referencing the output,
or am I restating the criterion?" If the latter, rewrite.

---

**Phase 1 — LOAD**

Read the rubric. Extract: all criteria IDs and tiers, pass conditions, the composite formula,
the golden threshold, and all N/A rules. Read all N output files.

Write this block:
```
Criteria: [IDs and tiers]
Formula: [exact text]
Golden threshold: [condition]
N/A rules: [list or "none"]
Outputs: [V-XX list]
```

Write: `[LOAD COMPLETE]`

---

**Phase 2 — SCORING**

For each output V-XX, write one prose-block section. One block per criterion, in order:

```
### V-XX: [axis label]

**C-01 — Per-criterion verdict matrix** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific structural reference — not a restatement]
*Why*: [mechanism: what structural property causes this verdict]

**C-02 — Evidence for every verdict** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific structural reference — not a restatement]
*Why*: [mechanism sentence]

**C-03 — Composite score per output** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific structural reference — not a restatement]
*Why*: [mechanism sentence]

**C-04 — Ranked leaderboard** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific structural reference — not a restatement]
*Why*: [mechanism sentence]

**C-05 — Failure patterns called out** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific structural reference — not a restatement]
*Why*: [mechanism sentence]

**C-06 — Excellence signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific structural reference — not a restatement]
*Why*: [mechanism sentence]

**C-07 — Per-output evidence notes** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote or specific structural reference — not a restatement]
*Why*: [mechanism sentence]

**C-08 — Regression signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [quote, or "PARTIAL — no prior round data available"]
*Why*: [mechanism sentence, or "N/A — no prior data"]
```

Before each *Evidence* line: check against the INERTIA PATTERN. If your evidence resembles
"output has/provides/includes [criterion name]" — rewrite with a quote or reference.

Score all N outputs before writing the EXIT TOKEN.

Write: `[SCORING COMPLETE — N outputs scored]` (replace N with actual count)

---

**Phase 3 — SYNTHESIS**

Write all five sections. Every section is required. Check against the INERTIA PATTERN: the
leaderboard must be explicit, the failure-patterns section must exist even when empty.

**Composite Scores**
Count PASS/PARTIAL/FAIL per tier from Phase 2 blocks.
Formula: `(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/1 * 10)`
Show: `V-XX: E=X/5, R=X/2, A=X/1 → composite = XX`

**Ranked Leaderboard**
Explicit ranked list, descending. Ties noted. Not a pointer to the score table.

**Failure Patterns**
Criteria where no output earned PASS. These signal rubric gaps or skill design issues.
If none: `No failure patterns — all criteria passed in at least one output.`

**Excellence Signals**
Specific output-criterion pairs with structural outliers. Name output, criterion, feature.
If none: `No excellence signals identified in this scoring run.`

**Regression Signals**
Prior-round degradations, or: `No prior round data — regression analysis cannot be performed.`

Write: `[SYNTHESIS COMPLETE]`

---

**Phase 4 — WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write: `[WRITE COMPLETE]`
