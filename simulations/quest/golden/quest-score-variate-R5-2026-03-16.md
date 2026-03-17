# quest-score Variate — Round 5 (v5 rubric)
# Generated: 2026-03-16

---

## Context: what informed this round

Round 5 (this file) targets the **v5 rubric** (C-01 through C-18, E=5, R=3, A=10).
The prior R5 file (2026-03-15) targeted the v4 rubric with S-axis (`*Why*:` field)
and T-axis (`[SYNTHESIS COMPLETE]` gate). That file is not carried here — this round
re-derives axis selection from the v5 rubric's two new criteria.

**v5 rubric counts**: E=5 (C-01..C-05), R=3 (C-06..C-08), A=10 (C-09..C-18)
**Formula**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)`
**Max**: 100
**Golden threshold**: all 5 essentials PASS AND composite >= 80

---

## What v5 added and what it implies for variation design

**C-17 — Self-referential anti-pattern priming**
Pass condition: at least one anti-pattern entry targets the enforcement mechanisms defined
in C-15 or C-16 themselves (e.g., "do not execute the scan mechanically"), and the entry
is placed in the pre-execution priming section before Phase 1.

Implication: R4 V-05 already contained AF-6 ("scan written but not genuinely checked" —
targets C-15) and AF-7 ("anti-patterns placed after Phase 1" — targets C-16), both in the
BEFORE YOU BEGIN block. R4 V-05 would PASS C-17 without modification. The variation
question for R5: does strengthening the AF-6/AF-7 entries (by explicitly naming C-17 in
their criterion-affected column) improve compliance, and does the *absence* of self-
referential entries produce a clean FAIL that is distinguishable from PARTIAL?

**C-18 — Full-envelope structural coverage**
Pass condition: both (a) pre-Phase-1 priming block satisfying C-16 and (b) post-output
named scan satisfying C-15 present in the same execution unit. H-only variations (C-16
PASS but no scan) FAIL C-18. G-only variations (scan PASS but no priming) FAIL C-18.
Only H+G satisfies C-18.

Implication: C-18 cannot be achieved by any single-axis variation. The combination
structure (H+G) is required. Single-axis variations V-01 through V-03 are designed to
establish the FAIL baselines and partial-envelope conditions; V-04 and V-05 test
combinations that achieve C-17 and C-18.

---

## Axis selection

Prior-round proven axes carried forward:

| Axis | Origin | Mechanism | Criteria targeted |
|------|--------|-----------|-------------------|
| D | R3 | Derivation gate hardening: named-variable self-check before `[DERIVE COMPLETE]` | C-11, C-13 |
| E | R3 | Pre-printed per-output block skeleton: model fills bracketed slots rather than deciding placement | C-14, C-09 |
| G | R4 | Post-scoring completeness scan: cross-output table + `[SCAN COMPLETE]` token | C-15 |
| H | R4 | Pre-execution anti-pattern table in BEFORE YOU BEGIN section | C-16, C-17 (with AF-6/AF-7) |
| S | R5-v4 | `*Why*:` field in every criterion row | C-11 |
| T | R5-v4 | `[SYNTHESIS OPEN]` / `[SYNTHESIS COMPLETE]` gate with pre-close checklist | C-10 |

New axes for this round:

| Axis | Label | Description |
|------|-------|-------------|
| J | Lifecycle: v5 condensed baseline | 3-phase (DERIVE/SCORE/SYNTHESIZE), no H, no G. Carries D-axis and in-block template. Establishes C-15/C-16/C-17/C-18 FAIL baseline for v5. Risk: no mechanism to catch mid-execution omission. |
| K | Output format: per-output inline field check | H axis (BEFORE YOU BEGIN with AF-1..AF-7), no G. After each output block's Golden field, an in-block `#### Field Verification` section confirms that Summary Note, Composite, and Golden are present in THAT block. No named post-scan token. Tests: does H-only satisfy C-17? Does synchronous inline verification satisfy C-15? Risk: inline check runs per output, not "after all output blocks" — C-15 FAIL expected; C-17 PASS expected (AF-6 in pre-execution section). |
| L | Phrasing register: imperative mode | Full second-person imperative throughout. Carries H+G from R4 V-05 (AF-1..AF-7, scan table, `[SCAN COMPLETE]`). Tests whether imperative-command register reduces compliance drift vs specification-register equivalents. Risk: imperative register may reduce nuance in evidence-quality instructions. |

Single-axis: V-01 (J), V-02 (K), V-03 (L)
Combinations: V-04 (H + G + S + T), V-05 (H + G + S + T + AF-8/AF-9 extension)

**Predicted outcomes:**

| Criterion | V-01 (J) | V-02 (K) | V-03 (L) | V-04 (H+G+S+T) | V-05 (H+G+S+T+AF-8/9) |
|-----------|----------|----------|----------|----------------|----------------------|
| C-10 | FAIL | FAIL | FAIL | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | FAIL | FAIL | PASS | PASS | PASS |
| C-16 | FAIL | PASS | PASS | PASS | PASS |
| C-17 | FAIL | PASS | PASS | PASS | PASS |
| C-18 | FAIL | FAIL | PASS | PASS | PASS |

Rubric in scope: v5 (as defined in prompt; `simulations/quest/rubrics/quest-score-rubric-v5-2026-03-16.md`)

---

## V-01 — Lifecycle: condensed 3-phase (v5 C-17/C-18 baseline)

**Axis**: J — Lifecycle emphasis
**Hypothesis**: A condensed 3-phase structure with derivation gate and in-block labeled
sections but without pre-priming or post-scan produces FAIL on C-15, C-16, C-17, and C-18
simultaneously. This variation is the clean v5 baseline — it carries the accumulated
structural improvements from prior rounds (derivation hardening, in-block template, failure
pattern template) while deliberately omitting both compliance-envelope mechanisms. Scoring
this output against v5 establishes the floor: the C-17 and C-18 FAIL verdicts are directly
attributable to the absence of BEFORE YOU BEGIN and completeness scan respectively, not to
any other structural gap. Risk: without pre-priming, evidence quality (C-02) and mechanism
naming (C-11 via S-axis) may degrade; without the scan, Summary Note and Golden may drift
outside their designated blocks.

---

You are running `quest-score`. Score N skill output variations against the active rubric.

**Inputs**
- Active rubric: [rubric file path, provided by caller]
- Outputs to score: [list of output file paths, provided by caller]
- Prior-round scorecard: [path, or "none"]

---

**DERIVE**

Open the active rubric. For each criterion, record its ID and tier label (Essential,
Recommended, or Aspirational). Count criteria by tier.

Write the derivation block:

```
Rubric derivation:
Essential criteria:    [list IDs]     → E_count = [N]
Recommended criteria:  [list IDs]     → R_count = [N]
Aspirational criteria: [list IDs]     → A_count = [N]

Formula: composite = (essential_pass / E_count × 60)
                   + (recommended_pass / R_count × 30)
                   + (aspirational_pass / A_count × 10)
  [denominator positions hold named variables — do not substitute numeric values into the formula]

Scoring: PASS = 1.0, PARTIAL = 0.5 (Essential and Recommended only); Aspirational PARTIAL = 0.0
Golden threshold: [state verbatim from rubric]
```

Before writing the gate token, confirm:
1. E_count, R_count, and A_count each have a specific number assigned above.
2. All three denominator positions in the formula show named variables, not numeric literals.
3. The golden threshold is quoted verbatim from the rubric — not inferred or paraphrased.

Correct any gap before proceeding.

`[DERIVE COMPLETE]`

**The first output scoring block must not appear before `[DERIVE COMPLETE]`.**

Read all N output files.

```
Outputs loaded: [list IDs]
Prior-round data: [path, or "none"]
```

---

**SCORE**

For each output, produce one scoring block with these labeled sections in the order shown.
`#### Summary Note` and `#### Golden` are required inside this block — do not move them to
SYNTHESIZE.

```
### [Output ID]: [axis label if known]

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
[one row per criterion — total rows = E_count + R_count + A_count; no row may be blank or absent]

Evidence rule: each cell names a specific structural element, section heading, field label, or
direct quote from this output. Criterion restatements are not evidence. Claims that could apply
to any output are not evidence.

#### Summary Note
[1–3 sentences: primary structural differentiator or primary miss for this output — name the
mechanism, not just the verdict label; required here, inside this block]

#### Composite
Formula: (essential_pass / E_count × 60) + (recommended_pass / R_count × 30) + (aspirational_pass / A_count × 10)
  [use named variables from DERIVE — do not substitute numeric values here]
Essential:    [n PASS] + [n PARTIAL × 0.5] = [essential_pass] / E_count × 60 = [pts]
Recommended:  [n PASS] + [n PARTIAL × 0.5] = [recommended_pass] / R_count × 30 = [pts]
Aspirational: [n PASS] = [aspirational_pass] / A_count × 10 = [pts]
Composite: [total]

#### Golden
[complete exactly one — required inside this block]
Golden: YES
Golden: NO — [specific failing condition: which essential is not PASS, or composite < 80]
```

Score all N outputs before opening SYNTHESIZE.

---

**SYNTHESIZE**

Write all five sections in order. Every section is required.

**Ranked Leaderboard**

All N outputs in a single descending list by composite. Standalone — not a reference to
SCORE blocks. Ties broken by essential_pass count then output ID alphabetically; state ties
explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

**Excellence Signals**

Criterion-output pairs where structural differences produced outlier-high scores. Name the
output, criterion, and the structural mechanism that produced the high score.
If none: "No excellence signals detected in this scoring run."

**Regression Signals**

Prior-round degradations (PASS→PARTIAL, PASS→FAIL, PARTIAL→FAIL). State prior verdict,
current verdict, and the structural change that caused the regression.
If no prior data: "No prior round data — regression analysis cannot be performed."
If prior data, no regressions: "No regressions detected."

**Failure Patterns**

For each criterion where no output received PASS across all N scored outputs:

```
Pattern: [criterion ID] — [criterion name]
Diagnosis: [rubric gap | skill design issue]
Rationale: [one sentence]
```

Apply the template to every universal failure. Prose in place of the template fails C-12.
If no universal failures: "No universal failures detected."

**Write scorecard**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-02 — Output format: per-output inline field check (H-only partial envelope)

**Axis**: K — Output format (per-output inline verification) + H (BEFORE YOU BEGIN)
**Hypothesis**: Moving field verification inside each output block as a synchronous check
(immediately after Golden, before the next output) differs from the G-axis asynchronous
scan (after ALL output blocks). The inline check confirms fields within the block that just
closed, not across the full output set. C-15 requires verification "after all output blocks"
— the inline format satisfies the spirit of verification but not the positional requirement
of C-15; expected PARTIAL at best (verification instruction present, genuine check per block,
but not a named cross-output audit record after all N outputs). C-16 PASS: BEFORE YOU BEGIN
satisfies pre-Phase-1 priming. C-17 PASS: AF-6 in BEFORE YOU BEGIN explicitly targets C-15's
enforcement mechanism (the scan itself). C-18 FAIL: C-15 not satisfied by inline check.
This variation tests whether inline verification is detectably inferior to a named post-scan
token — a C-15 PARTIAL vs FAIL distinction that sharpens the rubric's positional requirement.

---

You are running `quest-score`. Score N skill output variations against the active rubric.

**Inputs**
- Active rubric: [rubric file path, provided by caller]
- Outputs to score: [list of output file paths, provided by caller]
- Prior-round scorecard: [path, or "none"]

---

**BEFORE YOU BEGIN — Failure Mode Reference**

Read this table before opening the rubric or writing any Phase 1 content. Loading failure
modes before structural work begins enables avoidance; failure modes encountered after Phase 1
starts can only correct in-progress execution.

| Code | Anti-Pattern | Symptom | Criteria Affected |
|------|-------------|---------|-------------------|
| AF-1 | Formula from hardcoded counts, not rubric | Numeric literals `/5`, `/3`, `/10` in formula denominator positions — not matching rubric tier counts | C-03, C-11 |
| AF-2 | Missing verdict rows | Verdict table rows fewer than E_count + R_count + A_count | C-01 |
| AF-3 | Evidence-free verdicts | Evidence cells contain no structural quote — criterion restatements or generic claims only | C-02 |
| AF-4 | Golden or Note deferred outside output block | `#### Golden` or `#### Summary Note` placed in synthesis rather than inside the per-output scoring block | C-09, C-14 |
| AF-5 | Failure patterns unchecked | Patterns section absent, or states "none" without having verified every criterion across all outputs | C-05 |
| AF-6 | Inline field check treated as completeness scan | Per-output inline check accepted as satisfying C-15; C-15 requires verification after ALL output blocks, not per-output verification interleaved with scoring | C-15 |
| AF-7 | Anti-patterns placed after Phase 1 | Failure mode table appears in Phase 2 or later, after first structural decisions are already made | C-16 |

These failure modes are now loaded. Proceed to Phase 1.

---

**Phase 1 — DERIVE**

Open the active rubric. For each criterion, record its ID and tier label. Count by tier.

Write the derivation block:

```
Rubric derivation:
Essential criteria:    [list IDs]     → E_count = [N]
Recommended criteria:  [list IDs]     → R_count = [N]
Aspirational criteria: [list IDs]     → A_count = [N]

Formula: composite = (essential_pass / E_count × 60)
                   + (recommended_pass / R_count × 30)
                   + (aspirational_pass / A_count × 10)
  [denominator positions: named variables only — do not substitute numeric values]

Scoring: PASS = 1.0, PARTIAL = 0.5 (Essential and Recommended only); Aspirational PARTIAL = 0.0
Golden threshold: [state verbatim from rubric]
```

Before writing `[DERIVE COMPLETE]`, confirm:
1. E_count, R_count, and A_count each have a specific number assigned.
2. Denominator positions in the formula show named variables, not numeric literals.
3. Golden threshold is quoted verbatim from the rubric.

Correct any gap before emitting the gate token.

`[DERIVE COMPLETE]`

**The first output scoring block must not appear before `[DERIVE COMPLETE]`.**

Read all N output files.

```
Outputs loaded: [list IDs]
Prior-round data: [path, or "none"]
```

---

**Phase 2 — SCORE**

For each output, produce one scoring block. After `#### Golden`, complete the inline
`#### Field Verification` section for that output before opening the next output block.

```
### [Output ID]: [axis label if known]

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
[one row per criterion — total rows = E_count + R_count + A_count; no row blank or absent]

Evidence rule: cite a specific structural element, section heading, field label, or direct
quote from this output. Not criterion restatements. Not claims applying to any output.

#### Summary Note
[1–3 sentences: primary structural differentiator or primary miss — name the mechanism, not
the verdict label; required here, inside this block]

#### Composite
Formula: (essential_pass / E_count × 60) + (recommended_pass / R_count × 30) + (aspirational_pass / A_count × 10)
  [use named variables from Phase 1 — do not substitute numeric values]
Essential:    [n PASS] + [n PARTIAL × 0.5] = [essential_pass] / E_count × 60 = [pts]
Recommended:  [n PASS] + [n PARTIAL × 0.5] = [recommended_pass] / R_count × 30 = [pts]
Aspirational: [n PASS] = [aspirational_pass] / A_count × 10 = [pts]
Composite: [total]

#### Golden
[complete exactly one — required inside this block]
Golden: YES
Golden: NO — [specific failing condition]

#### Field Verification
Verify that the block above contains each required field. Mark PRESENT or ABSENT.
- Summary Note (in-block, non-empty): [PRESENT | ABSENT]
- Composite (formula shown with named variables): [PRESENT | ABSENT]
- Golden (YES or NO with condition): [PRESENT | ABSENT]
- Verdict rows (count matches E_count + R_count + A_count): [PRESENT | ABSENT — actual count: N]

If any field is ABSENT, correct the block above before proceeding to the next output.
```

Score all N outputs with inline verification before opening Phase 3.

---

**Phase 3 — SYNTHESIZE**

Write all five sections in order. Every section is required.

**Ranked Leaderboard**

All N outputs descending by composite. Standalone — not a reference to Phase 2 blocks.
Ties broken by essential_pass count then output ID alphabetically; state ties.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

**Excellence Signals**

Criterion-output pairs where structural differences produced outlier-high scores. Name output,
criterion, and structural mechanism.
If none: "No excellence signals detected in this scoring run."

**Regression Signals**

Prior-round degradations. State prior verdict, current verdict, structural cause.
If no prior data: "No prior round data — regression analysis cannot be performed."
If prior data, no regressions: "No regressions detected."

**Failure Patterns**

```
Pattern: [criterion ID] — [criterion name]
Diagnosis: [rubric gap | skill design issue]
Rationale: [one sentence]
```

Apply the template to every universal failure. Prose in place of template fails C-12.
If no universal failures: "No universal failures detected."

**Write scorecard**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-03 — Phrasing register: imperative mode with H+G full envelope

**Axis**: L — Phrasing register (imperative) + H (BEFORE YOU BEGIN) + G (named scan token)
**Hypothesis**: Converting the entire prompt from specification-register ("For each output,
produce one scoring block...") to second-person imperative-register ("Score each output.
Write one block per output. Every block requires...") reduces the distance between instruction
and execution. The imperative register eliminates the conditional parsing required by phrases
like "if any cell is FAIL, return to the affected block" — the condition becomes a direct
command. Carries H+G from R4 V-05 unchanged to isolate the register effect. Predicted:
C-15/C-16/C-17/C-18 PASS (same structural mechanisms as R4 V-05); variance in C-02 (evidence
specificity) and C-11 (formula derivation) relative to V-03 will indicate whether register
affects evidence quality independent of structural enforcement. Risk: imperative register
compresses nuance in the evidence-rule and failure-diagnosis instructions; the command form
"cite a structural element" may elicit less specific evidence than the longer specification-
mode formulation.

---

You are running `quest-score`. Score N skill output variations against the active rubric.

**Inputs**
- Active rubric: [rubric file path, provided by caller]
- Outputs to score: [list of output file paths, provided by caller]
- Prior-round scorecard: [path, or "none"]

---

**BEFORE YOU BEGIN**

Read this table now. Do not write any Phase 1 content until you have read every row.
Loading failure modes before structural work begins enables avoidance; reading them after
Phase 1 starts can only correct in-progress execution — it cannot prevent the first
structural decisions from being made under uninformed conditions.

| Code | Anti-Pattern | Symptom | Criteria Affected |
|------|-------------|---------|-------------------|
| AF-1 | Hardcoded formula denominators | Numeric literals `/5`, `/3`, `/10` in denominator positions instead of E_count, R_count, A_count | C-03, C-11 |
| AF-2 | Missing verdict rows | Row count less than E_count + R_count + A_count | C-01 |
| AF-3 | Evidence-free verdicts | Evidence cells contain only criterion restatements or blanks | C-02 |
| AF-4 | Golden or Note outside output block | `#### Golden` or `#### Summary Note` deferred to synthesis | C-09, C-14 |
| AF-5 | Failure patterns skipped | Patterns section absent or "none" without checking every criterion across all outputs | C-05 |
| AF-6 | Scan written but not genuinely checked | `[SCAN COMPLETE]` emitted; table cells filled PASS without verifying the output blocks they reference — ticking boxes without reading content | C-15 |
| AF-7 | Anti-pattern table placed after Phase 1 | This table appearing in Phase 2 or later, after first structural decisions are already made | C-16 |

Failure modes loaded. Proceed to Phase 1.

---

**Phase 1 — DERIVE**

Open the rubric. Read every criterion. Record its ID and tier label.

Count criteria by tier and write this block:

```
Rubric derivation:
Essential criteria:    [list IDs]     → E_count = [N]
Recommended criteria:  [list IDs]     → R_count = [N]
Aspirational criteria: [list IDs]     → A_count = [N]

Formula: composite = (essential_pass / E_count × 60)
                   + (recommended_pass / R_count × 30)
                   + (aspirational_pass / A_count × 10)
  [keep named variables in denominator positions — do not replace with numbers]

Scoring: PASS = 1.0, PARTIAL = 0.5 (Essential and Recommended only); Aspirational PARTIAL = 0.0
Golden threshold: [copy verbatim from rubric]
```

Run this check before writing `[DERIVE COMPLETE]`:
1. Does each of E_count, R_count, A_count have a number? If not, assign it now.
2. Do all three denominator positions show variable names, not numbers? If any shows a number, replace it with the variable name.
3. Is the golden threshold copied verbatim? If paraphrased, re-copy it now.

`[DERIVE COMPLETE]`

Do not write the first output scoring block before `[DERIVE COMPLETE]`.

Read all N output files now.

```
Outputs loaded: [list IDs]
Prior-round data: [path, or "none"]
```

---

**Phase 2 — SCORE**

Score each output. Write one block per output. Every block requires these sections in this order.
Do not move `#### Summary Note` or `#### Golden` to Phase 3.

```
### [Output ID]: [axis label if known]

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
[one row per criterion — row count must equal E_count + R_count + A_count; leave no row blank]

For each Evidence cell: name a specific structural element, section heading, field label, or
direct quote from this output. Do not restate the criterion. Do not write something that
could apply to any output.

#### Summary Note
[Write 1–3 sentences here. Name the primary structural differentiator or primary miss.
Name the mechanism — not the verdict label. This field is required here. Do not defer it.]

#### Composite
Formula: (essential_pass / E_count × 60) + (recommended_pass / R_count × 30) + (aspirational_pass / A_count × 10)
  [use named variables from Phase 1 — do not write numbers in the formula line]
Essential:    [n PASS] + [n PARTIAL × 0.5] = [essential_pass] / E_count × 60 = [pts]
Recommended:  [n PASS] + [n PARTIAL × 0.5] = [recommended_pass] / R_count × 30 = [pts]
Aspirational: [n PASS] = [aspirational_pass] / A_count × 10 = [pts]
Composite: [total]

#### Golden
[Write exactly one line. This field is required here. Do not defer it to Phase 3.]
Golden: YES
Golden: NO — [state the specific failing condition: which essential is not PASS, or composite < 80]
```

Score all N outputs. Do not open Phase 3 until `[SCAN COMPLETE]` is written.

---

**Completeness Scan**

After the last output block and before Phase 3, fill this table.
Check what is actually present in each block — not what you intended to write.
Mark a cell PASS only if the field is present, non-empty, and in the correct position.
If any cell is FAIL: return to that block and fix the field. Then re-check.
Do not write `[SCAN COMPLETE]` until every cell shows PASS.

| Output | Verdict Matrix (all rows present) | Evidence (all cells non-empty) | Summary Note in-block | Composite shown | Golden in-block |
|--------|----------------------------------|-------------------------------|-----------------------|----------------|----------------|
| [ID-01] | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL |
| [ID-02] | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL |
[one row per scored output — fill every cell]

`[SCAN COMPLETE]`

---

**Phase 3 — SYNTHESIZE**

Write all five sections. Every section is required.

**Ranked Leaderboard**

List all N outputs in descending composite order. Do not reference Phase 2 blocks — this
table must stand alone. Break ties by essential_pass count then output ID alphabetically.
State ties explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

**Excellence Signals**

Name criterion-output pairs with outlier-high scores. State the output ID, criterion ID,
and the structural mechanism that produced the high score.
If none: "No excellence signals detected in this scoring run."

**Regression Signals**

Name prior-round degradations (PASS→PARTIAL, PASS→FAIL, PARTIAL→FAIL). State prior verdict,
current verdict, and the structural change that caused the regression.
If no prior data: "No prior round data — regression analysis cannot be performed."
If prior data, no regressions: "No regressions detected."

**Failure Patterns**

For every criterion with no PASS across all N outputs, write this template:

```
Pattern: [criterion ID] — [criterion name]
Diagnosis: [rubric gap | skill design issue]
Rationale: [one sentence]
```

Do not use prose in place of this template — prose fails C-12.
If no universal failures: "No universal failures detected."

**Write scorecard**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-04 — Combo: H + G + S (*Why* field) + T (synthesis gate)

**Variation axes**: H (pre-execution priming with AF-1..AF-7) + G (named scan token) +
S (`*Why*:` field in every criterion row) + T (`[SYNTHESIS COMPLETE]` gate with pre-close
checklist)
**Hypothesis**: H+G establishes C-15/C-16/C-17/C-18 coverage (carried from R4 V-05);
the S-axis `*Why*:` field upgrades C-11 from PARTIAL/FAIL by making mechanism-naming a
structural requirement at the scoring site — a scorer who writes "phase gate present" as
a *Why* entry names an architectural property; one who writes "criterion satisfied" names
nothing, and the field makes that distinction visible; the T-axis synthesis gate closes the
structural-completion detection gap in C-10 by enclosing all synthesis sections in a
`[SYNTHESIS OPEN]` / `[SYNTHESIS COMPLETE]` token pair, with a pre-close checklist
confirming all four sections are present before the closing token. Predicted: first
variation achieving simultaneous PASS on C-10, C-11, C-15, C-16, C-17, C-18. Risk: adding
S+T axes increases prompt surface area; the synthesis gate pre-close checklist may be treated
as boilerplate; the `*Why*:` field may produce mechanism-shaped prose that names design
properties superficially without identifying them structurally.

---

You are running `quest-score`. Score N skill output variations against the active rubric.

**Inputs**
- Active rubric: [rubric file path, provided by caller]
- Outputs to score: [list of output file paths, provided by caller]
- Prior-round scorecard: [path, or "none"]

---

**BEFORE YOU BEGIN — Failure Mode Reference**

Read this table before opening the rubric or writing any Phase 1 content. These failure modes
are loaded before structural work begins so avoidance is possible; loading them in Phase 2 or
later can only correct — not prevent — structural decisions already made.

| Code | Anti-Pattern | Symptom | Criteria Affected |
|------|-------------|---------|-------------------|
| AF-1 | Formula from hardcoded counts, not rubric | Numeric literals `/5`, `/3`, `/10` in formula denominator positions | C-03, C-11 |
| AF-2 | Missing verdict rows | Verdict table rows fewer than E_count + R_count + A_count | C-01 |
| AF-3 | Evidence-free verdicts | Evidence cells contain criterion restatements or generic claims only; no structural quote | C-02 |
| AF-4 | Golden or Note deferred | `#### Golden` or `#### Summary Note` placed in synthesis rather than inside the per-output block | C-09, C-14 |
| AF-5 | Failure patterns unchecked | Patterns section absent, or "none" stated without verifying every criterion across all N outputs | C-05 |
| AF-6 | Scan written but not genuinely checked | `[SCAN COMPLETE]` emitted with table cells filled PASS without verifying the output blocks they reference — the scan mechanism executed as ritual rather than as genuine verification | C-15 |
| AF-7 | Anti-pattern table placed after Phase 1 | This failure mode table appearing in Phase 2 or later; by then, the first structural decisions are already made and avoidance is no longer possible | C-16 |

These failure modes are now loaded. Proceed to Phase 1.

---

**Phase 1 — DERIVE**

Open the active rubric. For each criterion, record its ID and tier label. Count by tier.

Write the derivation block:

```
Rubric derivation:
Essential criteria:    [list IDs]     → E_count = [N]
Recommended criteria:  [list IDs]     → R_count = [N]
Aspirational criteria: [list IDs]     → A_count = [N]

Formula: composite = (essential_pass / E_count × 60)
                   + (recommended_pass / R_count × 30)
                   + (aspirational_pass / A_count × 10)
  [E_count, R_count, A_count are named variables — do not substitute their numeric values into
   the formula expression itself]

Scoring: PASS = 1.0, PARTIAL = 0.5 (Essential and Recommended only); Aspirational PARTIAL = 0.0
Golden threshold: [state verbatim from rubric]
```

Before writing the gate token:
1. Confirm each count variable has a specific number assigned.
2. Confirm all three denominator positions show variable names, not numeric literals. If any shows a number, replace it with the variable name now.
3. Confirm the golden threshold is quoted verbatim — not inferred or paraphrased.

`[DERIVE COMPLETE]`

**The first output scoring block must not appear before `[DERIVE COMPLETE]`.**

Read all N output files.

```
Outputs loaded: [list IDs]
Prior-round data: [path, or "none"]
```

---

**Phase 2 — SCORE**

For each output, produce one scoring block. Every labeled section is required in the position
shown. `#### Summary Note` and `#### Golden` may not be deferred to Phase 3. The `*Why*:`
field is required after every Evidence entry in the verdict matrix.

```
### [Output ID]: [axis label if known]

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence | *Why* |
|----|-----------|------|---------|----------|-------|
[one row per criterion — total rows = E_count + R_count + A_count; no row blank or absent]

Evidence rule: each Evidence cell names a specific structural element, section heading, field
label, or direct quote from this output. Not criterion restatements. Not generic claims.

*Why* rule: each *Why* cell names the architectural property, design decision, or structural
mechanism that drives the verdict. Restating the criterion fails this field. Describing the
evidence fails this field. Naming a design property (e.g., "named gate token enforces
sequencing"; "pre-printed slot removes placement decision") satisfies this field.

#### Summary Note
[1–3 sentences: primary structural differentiator or primary miss — name the mechanism;
required here, inside this block; not deferrable to synthesis]

#### Composite
Formula: (essential_pass / E_count × 60) + (recommended_pass / R_count × 30) + (aspirational_pass / A_count × 10)
  [use named variables from Phase 1 — do not substitute numeric values]
Essential:    [n PASS] + [n PARTIAL × 0.5] = [essential_pass] / E_count × 60 = [pts]
Recommended:  [n PASS] + [n PARTIAL × 0.5] = [recommended_pass] / R_count × 30 = [pts]
Aspirational: [n PASS] = [aspirational_pass] / A_count × 10 = [pts]
Composite: [total]

#### Golden
[complete exactly one — required inside this block; do not defer]
Golden: YES
Golden: NO — [specific failing condition: which essential is not PASS, or composite < 80]
```

Score all N outputs. Do not open Phase 3 until `[SCAN COMPLETE]` is written.

---

**Completeness Scan**

After the last output block and before Phase 3:

Verify what is actually present in each output block — not what you intended to write.
A field is PASS only if it is present, non-empty, and in the correct position inside the
per-output block. If any cell is FAIL, return to the affected block and correct it before
writing `[SCAN COMPLETE]`.

| Output | Verdict rows (all present) | Evidence (all non-empty) | *Why* (all non-empty) | Summary Note in-block | Composite shown | Golden in-block |
|--------|---------------------------|-------------------------|-----------------------|-----------------------|----------------|----------------|
| [ID-01] | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL |
| [ID-02] | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL |
[one row per scored output — every cell must be filled]

`[SCAN COMPLETE]`

---

**Phase 3 — SYNTHESIZE**

`[SYNTHESIS OPEN]`

Write all five sections in order. Every section is required. Write the pre-close checklist
before `[SYNTHESIS COMPLETE]`.

**Ranked Leaderboard**

All N outputs descending by composite. Standalone — not a reference to Phase 2 blocks.
Ties broken by essential_pass count then output ID alphabetically; state ties explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

**Excellence Signals**

Outlier-high criterion-output pairs. Name output, criterion ID, and the structural mechanism
that produced the high score.
If none: "No excellence signals detected in this scoring run."

**Regression Signals**

Prior-round degradations (PASS→PARTIAL, PASS→FAIL, PARTIAL→FAIL). State prior verdict,
current verdict, structural cause.
If no prior data: "No prior round data — regression analysis cannot be performed."
If prior data, no regressions: "No regressions detected."

**Failure Patterns**

```
Pattern: [criterion ID] — [criterion name]
Diagnosis: [rubric gap | skill design issue]
Rationale: [one sentence]
```

Apply the template to every universal failure. Prose in place of template fails C-12.
If no universal failures: "No universal failures detected."

**Write scorecard**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

**Pre-close synthesis checklist**

Before writing `[SYNTHESIS COMPLETE]`, confirm each section is present:
- [ ] Ranked Leaderboard: table with all N outputs, composite, golden column
- [ ] Excellence Signals: criterion-output pairs named, or explicit "none" statement
- [ ] Regression Signals: degradations listed, or "no prior data" / "no regressions" statement
- [ ] Failure Patterns: template applied per universal failure, or explicit "none" statement
- [ ] Scorecard write instruction executed

If any section is absent, write it now before proceeding.

`[SYNTHESIS COMPLETE]`

---

## V-05 — Combo: H + G + S + T + AF-8/AF-9 (third-order priming ceiling test)

**Variation axes**: H (pre-execution priming) + G (named scan token) + S (`*Why*:` field) +
T (`[SYNTHESIS COMPLETE]` gate) + AF extension (AF-8 and AF-9 targeting C-17 and C-18
themselves)
**Hypothesis**: V-04 achieves C-17 PASS through AF-6/AF-7 (first-order: AF entries target
C-15/C-16 enforcement mechanisms). Adding AF-8 and AF-9 extends the self-referential chain:
AF-8 targets C-17's enforcement mechanism (the self-referential entry must itself be in the
pre-execution window — misplacing it produces C-17 FAIL, the same failure mode AF-7 describes
for C-16); AF-9 targets C-18's enforcement mechanism (the combination property requires both
H and G in the same execution unit — having one without the other is the failure mode that
C-18 was designed to detect). This creates a third-order compliance structure: the anti-
pattern table primes against failures in the priming mechanism, which primes against failures
in the combination-coverage mechanism. The ceiling test question is whether a model reading
AF-8 and AF-9 internalizes their meaning (producing structurally correct execution) or
processes them as additional boilerplate rows (producing marginally longer but equivalently
mechanical output). Risk: extending the anti-pattern table from 7 to 9 rows may cross the
threshold where the table is processed as a formatting requirement rather than a content
requirement, degrading all AF entries including AF-6/AF-7.

---

You are running `quest-score`. Score N skill output variations against the active rubric.

**Inputs**
- Active rubric: [rubric file path, provided by caller]
- Outputs to score: [list of output file paths, provided by caller]
- Prior-round scorecard: [path, or "none"]

---

**BEFORE YOU BEGIN — Failure Mode Reference**

Read every row of this table before opening the rubric or writing any Phase 1 content.
Failure modes loaded before structural work begins can be avoided; failure modes encountered
after structural decisions are made can only be corrected — often at the cost of reopening
completed sections.

| Code | Anti-Pattern | Symptom | Criteria Affected |
|------|-------------|---------|-------------------|
| AF-1 | Formula from hardcoded counts, not rubric | Numeric literals `/5`, `/3`, `/10` in formula denominator positions — not derived from rubric tier counts | C-03, C-11 |
| AF-2 | Missing verdict rows | Verdict table row count less than E_count + R_count + A_count | C-01 |
| AF-3 | Evidence-free verdicts | Evidence cells contain only criterion restatements or generic claims; no structural quote from the output being scored | C-02 |
| AF-4 | Golden or Note deferred outside output block | `#### Golden` or `#### Summary Note` placed in synthesis rather than inside the per-output scoring block | C-09, C-14 |
| AF-5 | Failure patterns unchecked | Patterns section absent, or "none" stated without having verified every criterion across all N outputs | C-05 |
| AF-6 | Scan executed mechanically without genuine verification | `[SCAN COMPLETE]` emitted; scan table cells filled PASS by recalling intent rather than by reading the output blocks — the C-15 enforcement mechanism executed as ritual | C-15 |
| AF-7 | Anti-pattern table placed after Phase 1 begins | This table placed in Phase 2 or later; structural decisions made before failure modes were loaded — C-16 requires pre-Phase-1 placement, which this entry itself demonstrates by appearing in BEFORE YOU BEGIN | C-16 |
| AF-8 | Self-referential entry misplaced | An anti-pattern entry targeting C-15 or C-16 enforcement mechanisms (such as AF-6 or AF-7 above) placed in the Completeness Scan section or after any phase marker rather than in this BEFORE YOU BEGIN block — satisfies the AF entry requirement but not the pre-execution placement requirement of C-17 | C-17 |
| AF-9 | Half-envelope execution | BEFORE YOU BEGIN present without a `[SCAN COMPLETE]` token, or `[SCAN COMPLETE]` present without a BEFORE YOU BEGIN block — one end of the compliance envelope closed, the other open; C-18 requires both in the same execution unit | C-18 |

These failure modes are now loaded. Proceed to Phase 1.

---

**Phase 1 — DERIVE**

Open the active rubric. For each criterion, record its ID and tier label. Count by tier.

Write the derivation block exactly as shown, filling every bracketed value:

```
Rubric derivation:
Essential criteria:    [list IDs]     → E_count = [N]
Recommended criteria:  [list IDs]     → R_count = [N]
Aspirational criteria: [list IDs]     → A_count = [N]

Formula: composite = (essential_pass / E_count × 60)
                   + (recommended_pass / R_count × 30)
                   + (aspirational_pass / A_count × 10)
  [E_count, R_count, A_count are named variables — do not substitute their numeric values
   into the formula expression]

Scoring: PASS = 1.0, PARTIAL = 0.5 (Essential and Recommended only); Aspirational PARTIAL = 0.0
Golden threshold: [state verbatim from rubric]
```

Before writing `[DERIVE COMPLETE]`, run the self-check:
1. Does each of E_count, R_count, A_count have a specific number? If not, assign it now.
2. Do all three denominator positions show variable names, not numeric literals? If any position shows a number, replace it with the variable name before proceeding.
3. Is the golden threshold copied verbatim from the rubric — not inferred or paraphrased?

Correct any failing item.

`[DERIVE COMPLETE]`

**The first output scoring block must not appear before `[DERIVE COMPLETE]`.**

Read all N output files.

```
Outputs loaded: [list IDs]
Prior-round data: [path, or "none"]
```

---

**Phase 2 — SCORE**

For each output, copy this template in full and fill every bracketed field. Do not rename,
remove, or relocate any labeled section. `#### Summary Note` and `#### Golden` are fixed-
position fields inside this block — they may not appear in Phase 3. The `*Why*:` field is
required for every row in the verdict matrix.

```
### [Output ID]: [axis label if known]

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence | *Why* |
|----|-----------|------|---------|----------|-------|
[one row per criterion from the active rubric — total rows must equal E_count + R_count + A_count;
no row may be blank or absent]

Evidence rule: each Evidence cell names a specific structural element, section heading, field
label, or direct quote from this output. Criterion restatements are not evidence. Generic
claims that could apply to any output are not evidence.

*Why* rule: each *Why* cell names the architectural property or structural mechanism that
drives the verdict — e.g., "named gate token enforces phase sequencing," "pre-printed slot
eliminates placement decision," "rubric-derived variable prevents formula hardcoding."
Restating the criterion fails this field. Describing the evidence fails this field.

#### Summary Note
[1–3 sentences: primary structural differentiator or primary miss for this output relative
to the others — name the structural feature or mechanism; required here, inside this block;
"see leaderboard" or equivalent deferrals are not acceptable]

#### Composite
Formula: (essential_pass / E_count × 60) + (recommended_pass / R_count × 30) + (aspirational_pass / A_count × 10)
  [reference named variables from Phase 1; do not substitute numeric values into this line]
Essential:    [n PASS] + [n PARTIAL × 0.5] = [essential_pass] / E_count × 60 = [pts]
Recommended:  [n PASS] + [n PARTIAL × 0.5] = [recommended_pass] / R_count × 30 = [pts]
Aspirational: [n PASS] = [aspirational_pass] / A_count × 10 = [pts]
Composite: [total]

#### Golden
[complete exactly one line — this field is required inside this block; do not move to synthesis]
Golden: YES
Golden: NO — [state the specific failing condition: which essential criterion is not PASS, or
composite < 80]
```

Score all N outputs. Do not open Phase 3 until `[SCAN COMPLETE]` is written.

---

**Completeness Scan**

After the last output block, before Phase 3:

Fill this table based on what is actually present in each output block — not what you intended
to write. A field is PASS only if it is present, non-empty, and in the correct position inside
the per-output block.

| Output | Verdict rows (all present) | Evidence (all non-empty) | *Why* (all non-empty) | Summary Note in-block | Composite shown | Golden in-block |
|--------|---------------------------|-------------------------|-----------------------|-----------------------|----------------|----------------|
| [ID-01] | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL |
| [ID-02] | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL |
[one row per scored output; every cell must be filled before proceeding]

For any FAIL cell: return to that output block and correct the missing or misplaced field
before proceeding. Do not write `[SCAN COMPLETE]` until the table contains no FAIL cells.

`[SCAN COMPLETE]`

---

**Phase 3 — SYNTHESIZE**

`[SYNTHESIS OPEN]`

Write all five sections in order. Every section is required.

**Ranked Leaderboard**

All N outputs descending by composite. Standalone — not a reference to Phase 2 blocks.
Ties broken by essential_pass count then output ID alphabetically; state ties explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

**Excellence Signals**

Criterion-output pairs with outlier-high scores. Name output, criterion ID, and the structural
mechanism that produced the high score.
If none: "No excellence signals detected in this scoring run."

**Regression Signals**

Prior-round degradations (PASS→PARTIAL, PASS→FAIL, PARTIAL→FAIL). State prior verdict,
current verdict, and the structural change that caused the regression.
If no prior data: "No prior round data — regression analysis cannot be performed."
If prior data, no regressions: "No regressions detected."

**Failure Patterns**

```
Pattern: [criterion ID] — [criterion name]
Diagnosis: [rubric gap | skill design issue]
Rationale: [one sentence]
```

Apply the template to every universal failure. Prose in place of the template fails C-12.
If no universal failures: "No universal failures detected."

**Write scorecard**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

**Pre-close synthesis checklist**

Before writing `[SYNTHESIS COMPLETE]`, confirm:
- [ ] Ranked Leaderboard present with all N outputs, composite scores, and Golden column
- [ ] Excellence Signals present (named pairs or explicit "none" statement)
- [ ] Regression Signals present (named degradations, "no prior data," or "no regressions")
- [ ] Failure Patterns present (template applied per universal failure, or explicit "none")
- [ ] Scorecard write instruction executed

If any section is absent, write it now.

`[SYNTHESIS COMPLETE]`
