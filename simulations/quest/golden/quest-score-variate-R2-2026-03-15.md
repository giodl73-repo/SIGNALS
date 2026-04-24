# quest-score Variate — Round 2
# Generated: 2026-03-15

---

## Context: what informed this round

R1 targeted the v1 rubric (8 criteria: E=5, R=2, A=1). The R1 variate explored three axes —
output format (prose blocks), lifecycle emphasis (phase gates), and inertia framing (bad-scorer
anti-pattern) — in single-axis and combination runs. V-04 and V-05 were the strongest performers,
passing C-10 in both cases via a `Pattern/Diagnosis: [label] -- [sentence]` template structure.

**Universal failure in R1**: formula hardcoding. All 5 variations embedded `/2` (R_count) and
`/1` (A_count) as numeric literals. The denominators matched the v1 rubric's actual counts, so
the arithmetic was correct — but the mechanism was wrong. A formula that pins literals to one
rubric version silently breaks when the rubric changes.

**v2 rubric adds four criteria** sourced directly from R1 signals:

| ID | Name | Root source |
|----|------|-------------|
| C-09 | Golden threshold declaration per output | missing from all R1 outputs |
| C-10 | Failure-pattern root-cause diagnosis | V-04/V-05 passed via Pattern/Diagnosis template |
| C-11 | Rubric-adaptive formula derivation | universal R1 failure — hardcoded literals |
| C-12 | Structured diagnosis template | V-01/V-02/V-03 wrote prose; V-04/V-05 used template |

**v2 rubric counts**: E=5 (C-01..C-05), R=3 (C-06..C-08), A=4 (C-09..C-12)
**Formula (reader reference only)**: derived from active rubric tier counts at run time
**Golden threshold**: all 5 essentials PASS AND composite >= 80

Note: this reader-reference line is for the variate document only. Skill body must not state
counts as literals — they must be derived by reading the active rubric.

R1 carry-forward signals:
- Phase gates (V-02/V-04/V-05): essential synthesis sections are more reliably produced with
  explicit exit tokens; no gate = synthesis dropped under context pressure
- Prose evidence blocks (V-01/V-04/V-05): evidence quality is higher than table-compressed
  cells; Evidence/Why structure forces mechanism articulation
- Pattern/Diagnosis template (V-04/V-05): C-10 passed consistently when structured template
  was mandated; prose-form diagnosis contained correct content but wrong structure

R1 universal failure — do not repeat:
- All 5 variations hardcoded `/2` and `/1` in the formula. The fix is structural, not
  instructional: force the scorer to derive E_count, R_count, A_count before writing the
  formula at all.

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | Role sequence — rubric-derivation-first | When rubric derivation is Phase 1 — producing explicit E_count, R_count, A_count and a symbolic formula before any output file is opened — the model cannot skip derivation and still satisfy the phase gate. The formula appears as a variable expression rather than a literal, satisfying C-11. Risk: the model resolves the symbolic formula to literals during Phase 1 and then re-embeds those resolved values in Phase 3 composite calculations. This test measures whether one derivation gate at the start is sufficient, or whether the formula must also be symbolically enforced at each use site. |
| B | Output format — labeled-field slots | Prescribing exact labeled field names that MUST be populated in each output block (`Golden:`) and each failure-pattern entry (`Pattern: / Diagnosis: / Rationale:`) makes C-09 and C-12 pass by template compliance. The scorer fills required slots; an unfilled slot is structurally visible. Risk: labeled slots produce mechanical outputs — `Diagnosis: rubric gap` without substantive reasoning, satisfying C-12 structure while failing C-10 rationale depth. This test measures whether slot-fill format closes C-09/C-12 without degrading C-10. |
| C | Inertia framing — formula-hardcoding anti-pattern | A concrete negative example showing the exact R1 failure — hardcoded `/5`, `/2`, `/1` literals calibrated to the v1 rubric — provides a targeted negative anchor for C-11. Unlike R1's V-03 (which targeted generic evidence), this anti-pattern isolates the one mechanism that failed universally in R1. Risk: the scorer reads the anti-example, concludes "don't use v1 counts," and then hardcodes the current rubric's counts thinking it has avoided the pattern. This test measures whether a targeted negative anchor produces C-11 compliance or merely shifts which literals are hardcoded. |

Single-axis runs: V-01 (A), V-02 (B), V-03 (C)
Combinations: V-04 (A+B), V-05 (A+B+C)

Rubric in scope: `simulations/quest/rubrics/quest-score-rubric-v2-2026-03-15.md`

---

## V-01 — Role sequence: rubric-derivation-first

**Axis**: A — Role sequence
**Hypothesis**: When rubric derivation is mandated as Phase 1 — and the phase gate cannot be
written until E_count, R_count, A_count have been explicitly stated — the formula expression is
built from named variables rather than literals. C-11 passes because the mechanism is correct:
the counts are derived, not assumed. Risk: the model resolves E_count=5, R_count=3, A_count=4
in Phase 1 and then silently substitutes those resolved values back into the formula in Phase 3
composite calculations. This test measures whether one derivation gate at the start is
sufficient, or whether the formula must be symbolically enforced at each subsequent use.

---

You are running `quest-score`. Score N skill output variations against the active rubric.

**Inputs**
- Active rubric: [rubric file path, provided by caller]
- Outputs to score: [list of output file paths, provided by caller]
- Prior-round scorecard: [path, or "none"]

**Phase manifest** — complete in order, each phase closes with its EXIT TOKEN before the next
phase begins:

| Phase | EXIT TOKEN |
|-------|------------|
| DERIVE | `[DERIVE COMPLETE]` |
| LOAD | `[LOAD COMPLETE]` |
| SCORING | `[SCORING COMPLETE — N outputs scored]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**Phase 1 — DERIVE**

Open the active rubric. Read every criterion. For each criterion, record its ID and tier label
(Essential, Recommended, or Aspirational). Count criteria by tier.

Write the derivation block exactly as shown, filling in the bracketed values:

```
Rubric derivation:
Essential criteria:    [list IDs]   → E_count = [N]
Recommended criteria:  [list IDs]   → R_count = [N]
Aspirational criteria: [list IDs]   → A_count = [N]

Composite formula (symbolic):
composite = (essential_pass / E_count * 60)
          + (recommended_pass / R_count * 30)
          + (aspirational_pass / A_count * 10)

Scoring: PASS = 1.0, PARTIAL = 0.5 (Essential and Recommended tiers only)
         Aspirational PARTIAL counts as 0.0 (binary: PASS=1.0, else 0.0)
Golden threshold: [state from rubric]
```

Do not substitute E_count, R_count, A_count with their resolved numeric values in the
`Composite formula` line. The resolved values are stated in the derivation block above the
formula and must not be re-embedded as literals in the formula expression itself.

Write: `[DERIVE COMPLETE]`

---

**Phase 2 — LOAD**

Read all N output files. Note which prior-round scorecard is available (if any).

```
Outputs loaded: [list IDs]
Prior-round data: [path, or "none"]
```

Write: `[LOAD COMPLETE]`

---

**Phase 3 — SCORING**

For each output, produce one scoring table. The table must cover every criterion in the active
rubric. No criterion row may be blank or absent; a table that omits criteria added in the
current rubric version is FAIL on C-01.

```
### [Output ID]: [axis label if known]

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
[one row per criterion from the active rubric]
```

Evidence rules (applied per cell):
- Evidence must name a specific structural element, section title, field label, template
  pattern, or direct quote from this output being scored.
- A criterion restatement ("the output has a leaderboard") is not evidence.
- A generic description that could apply to any well-designed output is not evidence.
- Specific reference example: "The output's 'Ranked Leaderboard' section contains rows for all
  five outputs sorted by composite score, highest to lowest."

After the table: 1-3 sentence summary note naming this output's primary differentiator or
primary miss relative to the other scored outputs. Name the structural feature — not just the
score.

Score all N outputs before writing the EXIT TOKEN.

Write: `[SCORING COMPLETE — N outputs scored]` (replace N with actual count)

---

**Phase 4 — SYNTHESIS**

Write all five sections. Every section is required. Do not omit any section even when its
"none detected" fallback applies.

**Composite Scores**

For each output, apply the symbolic formula from Phase 1. Use E_count, R_count, A_count as
named variables — do not re-embed their resolved values as literals in the calculation line.

```
[Output ID]:
  Essential:   [n PASS] + [n PARTIAL * 0.5] = [essential_pass] / E_count × 60 = [pts]
  Recommended: [n PASS] + [n PARTIAL * 0.5] = [recommended_pass] / R_count × 30 = [pts]
  Aspirational:[n PASS] = [aspirational_pass] / A_count × 10 = [pts]
  Composite: [sum]
```

Then state each output's golden threshold verdict:
- `Golden: YES` — if all Essential criteria are PASS AND composite >= 80
- `Golden: NO — [specific failing condition]` — otherwise (name which essential is not PASS,
  or state that composite < 80)

**Ranked Leaderboard**

Explicit ranked list, descending by composite. This section must be a standalone list — not
a reference to the score blocks above. Ties broken by essential_pass count, then output ID
alphabetically. State ties explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

**Failure Patterns**

For each criterion where no output received PASS across all N scored outputs, write:

```
Pattern: [criterion ID] — [criterion name]
Diagnosis: [rubric gap | skill design issue]
Rationale: [one sentence explaining why this is a rubric gap or a skill design issue]
```

Apply this template to every universal failure. Do not write prose in place of the template.
If no universal failures: "No universal failures detected."

**Excellence Signals**

Identify output-criterion pairs where one output clearly outperforms the others on that
specific criterion. Name the output, the criterion, and the structural mechanism that produced
the outlier score.
If none: "No excellence signals detected in this scoring run."

**Regression Signals**

If prior-round scorecard data was provided: identify every criterion-output pair where the
verdict degraded (PASS→PARTIAL, PASS→FAIL, or PARTIAL→FAIL). State the prior verdict, current
verdict, and the structural change that caused the regression.
If no prior data: "No prior round data — regression analysis cannot be performed."
If prior data exists but no regressions: "No regressions detected."

Write: `[SYNTHESIS COMPLETE]`

---

**Phase 5 — WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write: `[WRITE COMPLETE]`

---

## V-02 — Output format: labeled-field slots

**Axis**: B — Output format
**Hypothesis**: Prescribing exact labeled field names — including `Golden:` in each output block
and `Pattern: / Diagnosis: / Rationale:` in each failure entry — makes C-09 and C-12 pass by
template compliance. The scorer fills required slots; an unfilled slot is structurally visible
as a gap. This targets C-09 and C-12 directly without changing role sequence or adding a formula
anti-pattern. Risk: the scorer fills `Diagnosis: rubric gap` mechanically without substantive
reasoning, satisfying C-12 structure while failing C-10 rationale depth. This test measures
whether slot-fill format closes C-09/C-12 without degrading C-10 diagnostic depth.

---

You are running `quest-score`. Score N skill output variations against the active rubric.

**Inputs**
- Active rubric: [rubric file path, provided by caller]
- Outputs to score: [list of output file paths, provided by caller]
- Prior-round scorecard: [path, or "none"]

---

**Step 1 — Load**

Read the active rubric. Extract: all criterion IDs and their tier (Essential, Recommended,
Aspirational), pass conditions, the composite formula, the golden threshold, and any N/A rules.
Count criteria by tier to derive E_count, R_count, A_count. Read all N output files.

Write:

```
Criteria loaded:
  Essential (E_count=[N]):    [list IDs]
  Recommended (R_count=[N]):  [list IDs]
  Aspirational (A_count=[N]): [list IDs]
Formula: [state composite formula from the rubric]
Golden threshold: [state from rubric]
Outputs: [list IDs]
Prior-round data: [path, or "none"]
```

---

**Step 2 — Score each output**

For each output, produce a scoring block using this labeled-field format exactly. Every labeled
field is required; do not omit any field.

```
### [Output ID]: [axis label if known]

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
[one row per criterion from the active rubric; no row may be blank or absent]

Evidence rule: evidence must name a specific structural element, section title, field label,
or direct quote from this output. Criterion restatements are not evidence.

#### Summary Note
[1-3 sentences: primary differentiator or primary miss relative to the other scored outputs;
name the structural feature, not just the score]

#### Composite
Formula: (essential_pass / E_count * 60) + (recommended_pass / R_count * 30) + (aspirational_pass / A_count * 10)
  where E_count, R_count, A_count as derived in Step 1
Essential:    [n PASS] + [n PARTIAL * 0.5] = [essential_pass] of E_count → [pts]
Recommended:  [n PASS] + [n PARTIAL * 0.5] = [recommended_pass] of R_count → [pts]
Aspirational: [n PASS] = [aspirational_pass] of A_count → [pts]
Composite: [total]

#### Golden
[complete exactly one of the following lines — do not leave this field blank or inferred]
Golden: YES
Golden: NO — [state the specific failing condition: which essential criterion is not PASS, or composite < 80]
```

---

**Step 3 — Synthesis**

After scoring all N outputs, write these sections in order. Every section is required.

**Ranked Leaderboard**

Explicit ranked list, descending by composite. This must be a standalone list — not a
reference to the scoring blocks. Ties broken by essential_pass count, then output ID
alphabetically.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

**Excellence Signals**

Output-criterion pairs where one output structurally outperforms the others on a specific
criterion. Name the output, criterion, and the structural mechanism.
If none: "No excellence signals detected in this scoring run."

**Regression Signals**

Prior-round degradations (PASS→PARTIAL, PASS→FAIL, PARTIAL→FAIL) per criterion-output pair.
If no prior data: "No prior round data — regression analysis cannot be performed."
If prior data but no regressions: "No regressions detected."

**Failure Patterns**

For each criterion where no output received PASS across all N scored outputs, use this labeled
template exactly — same field labels in the same order for every entry:

```
Pattern: [criterion ID] — [criterion name]
Diagnosis: [rubric gap | skill design issue]
Rationale: [one sentence: why this is a rubric gap (criterion too strict or poorly specified)
           or a skill design issue (skill consistently fails to produce the required element)]
```

Apply the template to every universal failure. Do not write prose for any entry, even if only
one failure exists.
If no universal failures: "No universal failures detected."

---

**Step 4 — Write**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-03 — Inertia framing: formula-hardcoding anti-pattern

**Axis**: C — Inertia framing
**Hypothesis**: A concrete negative example showing the exact R1 failure — hardcoded tier-count
literals `/5`, `/2`, `/1` from the v1 rubric — provides a targeted negative anchor for C-11.
Unlike R1's V-03 (which targeted generic evidence), this anti-pattern isolates the one mechanism
that failed universally in R1. The anti-example is calibrated to the v1 failure (wrong literal
counts for v2) to make the mechanism failure visible, not just the numeric values. Risk: the
scorer reads the anti-example, concludes "don't use v1 counts," and then hardcodes the current
rubric's counts (/5, /3, /4) believing it has avoided the pattern. This test measures whether a
targeted negative anchor produces C-11 compliance or merely shifts which literals are hardcoded.

---

You are running `quest-score`. Score N skill output variations against the active rubric.

**Inputs**
- Active rubric: [rubric file path, provided by caller]
- Outputs to score: [list of output file paths, provided by caller]
- Prior-round scorecard: [path, or "none"]

**FORMULA HARDCODING ANTI-PATTERN — read before writing any formula**

The following formula pattern is a failure. Do not produce anything that resembles it:

```
HARDCODED (do not write this):
composite = (essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/1 * 10)
```

The problem: `/5`, `/2`, `/1` are literals taken from a specific rubric version. When the
rubric gains or loses criteria in any tier, these literals silently produce wrong scores. The
mechanism is wrong even when the literals happen to match the current rubric's actual counts.

The correct mechanism is derivation, not substitution. Read the active rubric. Count criteria
by tier. Assign those counts to named variables. Keep the variables symbolic in the formula:

```
CORRECT (derive from the active rubric):
E_count = [count of Essential criteria from the active rubric you just read]
R_count = [count of Recommended criteria from the active rubric you just read]
A_count = [count of Aspirational criteria from the active rubric you just read]

composite = (essential_pass / E_count * 60)
          + (recommended_pass / R_count * 30)
          + (aspirational_pass / A_count * 10)
```

Before writing any formula line in this run: check whether a numeric literal appears in a
denominator position. If it does — replace it with the appropriate named variable.

---

**Step 1 — Load**

Read the active rubric. For each criterion, note its ID and tier. Count criteria by tier.
State E_count, R_count, A_count explicitly before writing the formula. Write the formula as a
symbolic expression using the named variables — not their resolved numeric values.

Read all N output files. Note prior-round data availability.

Write:

```
Essential criteria (E_count=[N]):   [list IDs]
Recommended criteria (R_count=[N]): [list IDs]
Aspirational criteria (A_count=[N]):[list IDs]

Composite formula:
composite = (essential_pass / E_count * 60) + (recommended_pass / R_count * 30) + (aspirational_pass / A_count * 10)

Golden threshold: [state from rubric]
Outputs: [list IDs]
Prior-round data: [path, or "none"]
```

---

**Step 2 — Score each output**

For each output, produce one scoring table covering every criterion in the active rubric. No
criterion row may be blank or absent.

```
### [Output ID]: [axis label if known]

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
[one row per criterion from the active rubric]
```

Evidence rules:
- Evidence must name a specific structural element, section title, field label, template
  pattern, or direct quote from this output.
- Do not restate the criterion name as evidence.
- Do not write evidence that could apply to any well-designed output.

After the table: 1-3 sentence summary note identifying this output's primary differentiator or
primary miss relative to the other scored outputs.

---

**Step 3 — Synthesize**

After scoring all N outputs, write these sections. Every section is required.

**Composite Scores**

Apply the formula from Step 1. Use E_count, R_count, A_count as named variables — do not
re-embed their resolved values as literals. Check each calculation line: if you see a numeric
literal in a denominator position, replace it with the named variable.

Show: `[Output ID]: E=[n]/E_count, R=[n]/R_count, A=[n]/A_count → composite = [score]`

Then state each output's golden threshold verdict:
- `Golden: YES` if all Essential criteria are PASS AND composite >= 80
- `Golden: NO — [failing condition]` otherwise

**Ranked Leaderboard**

Explicit ranked list, descending. Ties noted and broken by essential_pass count then output ID.
This must be a standalone list — not a reference to the score blocks above.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

**Failure Patterns**

For each criterion with no PASS across all N outputs:

```
Pattern: [criterion ID] — [criterion name]
Diagnosis: [rubric gap | skill design issue]
Rationale: [one sentence]
```

Apply the template to every entry. Do not substitute prose.
If no universal failures: "No universal failures detected."

**Excellence Signals**

Output-criterion pairs where structural differences produced outlier scores. Name the output,
criterion, and mechanism.
If none: "No excellence signals detected in this scoring run."

**Regression Signals**

Prior-round degradations, or: "No prior round data — regression analysis cannot be performed."
If prior data but no regressions: "No regressions detected."

---

**Step 4 — Write**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-04 — Role sequence + labeled-field slots (A+B)

**Axes**: A + B — Rubric-derivation-first + labeled-field slots
**Hypothesis**: V-01 targets C-11 by forcing derivation before any scoring; V-02 targets C-09
and C-12 by prescribing `Golden:` and `Pattern/Diagnosis/Rationale:` as required labeled fields.
These failure modes are structurally independent: a scorer can derive the formula correctly and
still omit the Golden field; a scorer can include the Golden field and still hardcode the formula.
The combination addresses all three new aspirational criteria simultaneously. Risk: structural
complexity increases — derivation preamble plus labeled output blocks plus labeled failure
template — and the model may compress evidence quality to manage length. This test measures
whether A+B closes C-09/C-11/C-12 without introducing evidence regression on C-02.

---

You are running `quest-score`. Score N skill output variations against the active rubric.

**Inputs**
- Active rubric: [rubric file path, provided by caller]
- Outputs to score: [list of output file paths, provided by caller]
- Prior-round scorecard: [path, or "none"]

**Phase manifest** — complete in order, each phase closes with its EXIT TOKEN:

| Phase | EXIT TOKEN |
|-------|------------|
| DERIVE | `[DERIVE COMPLETE]` |
| LOAD | `[LOAD COMPLETE]` |
| SCORING | `[SCORING COMPLETE — N outputs scored]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**Phase 1 — DERIVE**

Open the active rubric. Read every criterion. Record each criterion's ID and tier label.
Count criteria by tier.

Write the derivation block:

```
Rubric derivation:
Essential criteria:    [list IDs]   → E_count = [N]
Recommended criteria:  [list IDs]   → R_count = [N]
Aspirational criteria: [list IDs]   → A_count = [N]

Composite formula (symbolic — named variables, not resolved literals):
composite = (essential_pass / E_count * 60)
          + (recommended_pass / R_count * 30)
          + (aspirational_pass / A_count * 10)

Scoring: PASS = 1.0, PARTIAL = 0.5 (Essential and Recommended only)
         Aspirational: PARTIAL counts as 0.0
Golden threshold: [state from rubric]
```

The formula expression must contain named variables in denominator positions — not numeric
literals. E_count, R_count, A_count are resolved above the formula; they must not be
substituted into the formula line itself.

Write: `[DERIVE COMPLETE]`

---

**Phase 2 — LOAD**

Read all N output files and the prior-round scorecard (if provided).

```
Outputs loaded: [list IDs]
Prior-round data: [path, or "none"]
```

Write: `[LOAD COMPLETE]`

---

**Phase 3 — SCORING**

For each output, produce a labeled-field scoring block. Every labeled field is required.

```
### [Output ID]: [axis label if known]

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
[one row per criterion from the active rubric — no row may be blank or absent]

Evidence rule: every cell must name a specific structural element, field label, or direct quote
from this output. Criterion restatements are not evidence. Generic descriptions that apply to
any well-designed output are not evidence.

#### Summary Note
[1-3 sentences: primary differentiator or primary miss relative to the other scored outputs;
name the structural feature that explains this output's relative rank or its most significant gap]

#### Composite
Formula: (essential_pass / E_count * 60) + (recommended_pass / R_count * 30) + (aspirational_pass / A_count * 10)
  [use E_count, R_count, A_count from Phase 1 — do not substitute literals here]
Essential:    [n PASS] + [n PARTIAL * 0.5] = [essential_pass] of E_count → [pts]
Recommended:  [n PASS] + [n PARTIAL * 0.5] = [recommended_pass] of R_count → [pts]
Aspirational: [n PASS] = [aspirational_pass] of A_count → [pts]
Composite: [total]

#### Golden
[complete exactly one of the following — this field is required, not optional]
Golden: YES
Golden: NO — [state the specific failing condition]
```

Score all N outputs before writing the EXIT TOKEN.

Write: `[SCORING COMPLETE — N outputs scored]` (replace N with actual count)

---

**Phase 4 — SYNTHESIS**

Write all five sections. Every section is required. Do not omit any section even when its
fallback statement applies.

**Ranked Leaderboard**

Standalone ranked list, descending by composite. Not a pointer to scoring blocks. Ties broken
by essential_pass count then output ID alphabetically; ties stated explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

**Excellence Signals**

Output-criterion pairs where structural differences produced outlier scores. Name the output,
criterion, and the structural mechanism.
If none: "No excellence signals detected in this scoring run."

**Regression Signals**

Prior-round degradations (PASS→PARTIAL, PASS→FAIL, PARTIAL→FAIL) per criterion-output pair.
If no prior data: "No prior round data — regression analysis cannot be performed."
If prior data but no regressions: "No regressions detected."

**Failure Patterns**

For each criterion where no output received PASS across all N scored outputs, use this labeled
template in the same field order for every entry:

```
Pattern: [criterion ID] — [criterion name]
Diagnosis: [rubric gap | skill design issue]
Rationale: [one sentence: why this is a rubric gap (criterion too strict or poorly specified)
           or a skill design issue (skill consistently fails to produce the required element)]
```

Every entry must have all three fields in this order. Prose without these labels is FAIL
regardless of content quality. PARTIAL if the template is applied to some but not all entries.
If no universal failures: "No universal failures detected."

Write: `[SYNTHESIS COMPLETE]`

---

**Phase 5 — WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write: `[WRITE COMPLETE]`

---

## V-05 — Role sequence + labeled-field slots + formula anti-pattern (A+B+C)

**Axes**: A + B + C — Rubric-derivation-first + labeled-field slots + formula-hardcoding
anti-pattern
**Hypothesis**: V-01 (derivation-first phase gate) prevents formula hardcoding by forcing
explicit derivation before any output is opened — C-11 pass requires the mechanism, not the
math. V-02 (labeled slots) prevents missing Golden fields and unstructured failure diagnosis
by requiring `Golden:` and `Pattern/Diagnosis/Rationale:` as named required fields — C-09 and
C-12 pass by template compliance. V-03 (formula anti-pattern) provides a negative anchor
targeted at the R1 failure: the anti-example is calibrated to v1 literals (not current rubric
counts) to make the mechanism failure visible independent of whether the numbers match today.
The three axes operate at different lifecycle points — before any file is opened (anti-pattern
fires first), during Phase 1 (derivation gate), and during Phases 3-4 (labeled slots enforce
Golden and diagnosis template). No overlap in what they target; no redundancy in when they
apply. This test measures whether combining all three axes produces the highest-probability
full pass on C-09/C-11/C-12 without degrading R1 carry-forward mechanisms.

---

You are running `quest-score`. Score N skill output variations against the active rubric.

**Inputs**
- Active rubric: [rubric file path, provided by caller]
- Outputs to score: [list of output file paths, provided by caller]
- Prior-round scorecard: [path, or "none"]

**FORMULA HARDCODING ANTI-PATTERN — read before Phase 1**

Do not write a formula with hardcoded tier-count literals. This is the failure pattern to avoid:

```
HARDCODED (do not produce this):
composite = (essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/1 * 10)
```

The `/5`, `/2`, `/1` are literals taken from a prior rubric version. They matched that rubric's
actual counts — the arithmetic was correct — but the mechanism was wrong. A scorer that pins
literals to one rubric version will silently produce wrong scores when the rubric changes.
C-11 fails even when the literals happen to match the current rubric, because the mechanism is
wrong: the counts were not derived, they were assumed.

The correct mechanism: read the active rubric, count criteria by tier, name the counts as
variables, and write the formula symbolically:

```
CORRECT:
E_count = [count of Essential criteria from the active rubric]
R_count = [count of Recommended criteria from the active rubric]
A_count = [count of Aspirational criteria from the active rubric]

composite = (essential_pass / E_count * 60)
          + (recommended_pass / R_count * 30)
          + (aspirational_pass / A_count * 10)
```

Check every formula line you write in this run. If a numeric literal appears in a denominator
position — replace it with the named variable.

**Phase manifest** — complete in order, each phase closes with its EXIT TOKEN:

| Phase | EXIT TOKEN |
|-------|------------|
| DERIVE | `[DERIVE COMPLETE]` |
| LOAD | `[LOAD COMPLETE]` |
| SCORING | `[SCORING COMPLETE — N outputs scored]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**Phase 1 — DERIVE**

Open the active rubric. Read every criterion. Record each criterion's ID and tier label.
Count criteria by tier.

Write the derivation block:

```
Rubric derivation:
Essential criteria:    [list IDs]   → E_count = [N]
Recommended criteria:  [list IDs]   → R_count = [N]
Aspirational criteria: [list IDs]   → A_count = [N]

Composite formula (symbolic):
composite = (essential_pass / E_count * 60)
          + (recommended_pass / R_count * 30)
          + (aspirational_pass / A_count * 10)

Scoring: PASS = 1.0, PARTIAL = 0.5 (Essential and Recommended only)
         Aspirational: PARTIAL = 0.0 (binary)
Golden threshold: [state from rubric]
```

Before writing `[DERIVE COMPLETE]`: scan the formula line. If you see a numeric literal in a
denominator position — replace it with the named variable. Do not proceed until the formula
contains only E_count, R_count, A_count in those positions.

Write: `[DERIVE COMPLETE]`

---

**Phase 2 — LOAD**

Read all N output files and the prior-round scorecard (if provided).

```
Outputs loaded: [list IDs]
Prior-round data: [path, or "none"]
```

Write: `[LOAD COMPLETE]`

---

**Phase 3 — SCORING**

For each output, produce a labeled-field scoring block. Every labeled field is required; an
omitted field is a structural gap.

```
### [Output ID]: [axis label if known]

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
[one row per criterion from the active rubric — no row may be blank or absent]

Evidence rule: evidence must name a specific structural element, section title, field label,
template pattern, or direct quote from this output. Criterion restatements are not evidence.
Generic observations that apply to any output are not evidence.

#### Summary Note
[1-3 sentences: primary differentiator or primary miss; name the structural feature that
explains this output's relative rank or its most significant structural gap]

#### Composite
Formula: (essential_pass / E_count * 60) + (recommended_pass / R_count * 30) + (aspirational_pass / A_count * 10)
  [E_count, R_count, A_count from Phase 1; do not substitute their numeric values here]
Essential:    [n PASS] + [n PARTIAL * 0.5] = [essential_pass] of E_count → [pts]
Recommended:  [n PASS] + [n PARTIAL * 0.5] = [recommended_pass] of R_count → [pts]
Aspirational: [n PASS] = [aspirational_pass] of A_count → [pts]
Composite: [total]

#### Golden
[complete exactly one of the following lines — this field is required, not optional]
Golden: YES
Golden: NO — [state the specific failing condition: which essential is not PASS, or composite < 80]
```

Before writing each `#### Composite` block: scan the formula line for numeric literals in
denominator positions. If present — replace with E_count, R_count, A_count.

Score all N outputs before writing the EXIT TOKEN.

Write: `[SCORING COMPLETE — N outputs scored]` (replace N with actual count)

---

**Phase 4 — SYNTHESIS**

Write all five sections. Every section is required. Check: leaderboard is a standalone explicit
list (not a pointer to score blocks); failure template has all three fields for every entry.

**Ranked Leaderboard**

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

Standalone, descending. Ties: state explicitly, break by essential_pass count then output ID.

**Excellence Signals**

Output-criterion pairs where structural differences produced outlier scores. Name the output,
criterion, and the mechanism.
If none: "No excellence signals detected in this scoring run."

**Regression Signals**

Prior-round degradations (PASS→PARTIAL, PASS→FAIL, PARTIAL→FAIL), or:
"No prior round data — regression analysis cannot be performed."
If prior data but no regressions: "No regressions detected."

**Failure Patterns**

For each criterion where no output received PASS across all N scored outputs:

```
Pattern: [criterion ID] — [criterion name]
Diagnosis: [rubric gap | skill design issue]
Rationale: [one sentence: why this is a rubric gap or a skill design issue]
```

Check before writing `[SYNTHESIS COMPLETE]`:
- Every universal failure has `Pattern:`, `Diagnosis:`, and `Rationale:` fields in that order.
- No entry is prose-only. Even a single failure entry must use the template.
- If no universal failures: "No universal failures detected."

Write: `[SYNTHESIS COMPLETE]`

---

**Phase 5 — WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write: `[WRITE COMPLETE]`
