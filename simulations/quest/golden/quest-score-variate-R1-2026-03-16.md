# quest-score Variations -- Round 1 (2026-03-16 rubric)
**Skill**: quest-score
**Rubric**: v1-2026-03-16 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-10 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=2**
**Date**: 2026-03-16
**Round**: 1

---

## Context: what informed this round

This is Round 1 against the new v1 rubric dated 2026-03-16. No prior champion prompt exists
for this rubric. No prior-round scorecard exists.

Key differences from the 2026-03-15 v1 rubric cycle:

| Change | Prior cycle | New rubric | Design consequence |
|--------|-------------|------------|-------------------|
| C-01 (load verification) | Implied — load was bundled into scoring preamble | **Essential** — 4 sub-elements required before first verdict | Load block omissions now produce C-01 FAIL, not silent PARTIAL on C-02 |
| C-04 (composite score) | Final number sufficient | **Explicit calculation required** — E=X/5, R=X/3, A=X/2 form | Bare scores now produce C-04 PARTIAL regardless of correctness |
| C-06 (leaderboard) | Essential | **Recommended** — reorganizes C-04 data | Missing leaderboard degrades score, does not break golden gate |
| C-07/C-08 split | Excellence + notes conflated | **C-07 excellence signals, C-08 per-output synthesis notes** | Tests two different depth properties separately |
| C-09 (regression) | Was C-08 | **Aspirational** — N/A note earns PARTIAL in round 1 | First-round N/A handling still applies |
| C-10 (arithmetic verification) | Not in prior rubric | **New Aspirational** — pick one output, verify composite independently | Emerges as a reliability signal from prior R4+ |

**v1-2026-03-16 rubric counts**: E=5 (C-01..C-05), R=3 (C-06..C-08), A=2 (C-09..C-10)
**Formula**:
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```
**Golden threshold**: all 5 essentials PASS AND composite >= 80
**N/A condition**: C-09 PARTIAL (not FAIL) when scorer writes the prescribed no-prior-data statement

**Score landmarks:**
- All essential + all recommended + all aspirational: 100
- All essential + all recommended + no aspirational: 90
- All essential + no recommended + no aspirational: 60

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | Output format -- numbered criterion blocks | A rigid per-block template with labeled slots (Evidence slot, Why slot, Verdict slot) forces the scorer to fill each of C-01's four sub-elements and C-04's explicit calculation as checklist items before moving to the next criterion. These are the two most likely new-rubric PARTIALs: C-01 because the four-sub-element pass condition is easy to satisfy 3/4 without noticing the miss, and C-04 because the prior cycle showed "bare final number" as the most common C-04 PARTIAL across R1-R6. |
| B | Lifecycle emphasis -- hard phase gates with STOP tokens | C-05 (failure patterns), C-07 (excellence signals), C-08 (per-output notes), and C-09 (regression N/A) are all synthesis-phase outputs that require cross-output reasoning. Without a gate, the scorer can terminate after the last per-output verdict block and miss every synthesis section. Explicit STOP tokens (required verbatim strings) make a skipped synthesis phase visible as a structural error rather than a soft miss. |
| C | Phrasing register -- worked examples inline | The v1-2026-03-16 rubric adds two new requirements that are precise enough to fail silently: the C-01 four-sub-element load block and the C-04 explicit calculation form. Showing a worked example of each -- a compliant load block, a compliant calculation line -- inline with the instructions gives the scorer a positive anchor to copy, cheaper and more reliable than abstract pass-condition language. |

Single-axis runs: V-01 (A), V-02 (B), V-03 (C)
Combinations: V-04 (A+B), V-05 (A+B+C)

Rubric in scope: `simulations/quest/rubrics/quest-score-rubric-v1-2026-03-16.md`
Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`
N_essential=5, N_recommended=3, N_aspirational=2
Golden threshold: all 5 essentials PASS AND composite >= 80

---

## V-01 -- Output format: numbered criterion blocks

**Axis**: A -- Output format
**Hypothesis**: Compact verdict tables reduce the evidence slot to a table cell, which passes
C-03 with a sentence fragment and C-04 with a final number. A per-criterion numbered block with
explicit labeled slots (VERDICT, EVIDENCE, WHY, CALC for C-04, SUBELEMENTS for C-01) makes
omissions structurally visible -- an empty slot is a missing field, not an implied pass. The C-01
four-sub-element block forces the scorer to list all four items (criteria IDs+tiers, formula text,
golden threshold, output count) rather than writing a vague "rubric loaded" header. The C-04 calc
slot forces the E/R/A breakdown form rather than a bare number. Risk: block verbosity slows the
scorer and produces long outputs that lose synthesis sections to context compression.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

---

**Step 1 -- Load**

Read the rubric file. Read all N output files.

Produce a numbered load block. Every field is required:

```
LOAD BLOCK
1. Criteria (ID + tier):
   - C-01: Essential
   - C-02: Essential
   - C-03: Essential
   - C-04: Essential
   - C-05: Essential
   - C-06: Recommended
   - C-07: Recommended
   - C-08: Recommended
   - C-09: Aspirational
   - C-10: Aspirational
2. Formula (exact text from rubric):
   [paste formula here]
3. Golden threshold (exact text):
   [paste threshold here]
4. N/A rules:
   [list, or "none"]
5. Outputs loaded:
   [V-XX list, with N count]
```

Do not begin scoring until this block is complete.

---

**Step 2 -- Score each output**

For each output V-XX, write one numbered-block section. Each section contains one numbered block
per criterion, in criterion order C-01 through C-10. Each block uses this exact structure:

```
[V-XX / C-NN -- criterion short name]
VERDICT: [PASS | PARTIAL | FAIL]
EVIDENCE: [Sentence(s) referencing specific output content -- quote a phrase, name a section,
           or describe a structural feature. Generic observations not tied to specific output
           text do not qualify. Do not restate the criterion.]
WHY: [One sentence: why does this evidence support the verdict? Name the mechanism.]
```

For C-01, add a SUBELEMENTS field:
```
SUBELEMENTS:
  (a) criteria IDs + tiers: [present | missing]
  (b) formula text: [present | missing]
  (c) golden threshold: [present | missing]
  (d) output count or list: [present | missing]
```
C-01 PASS requires all four present. PARTIAL if one is absent. FAIL if rubric not referenced.

For C-04, add a CALC field:
```
CALC: [Reproduce or paraphrase the calculation as written in the output -- e.g.,
       "E=4/5, R=2/3, A=1/2 -> composite = 76.7". If absent: "calculation not shown."]
```
C-04 PASS requires the E/R/A breakdown before the final number. PARTIAL if only the final number
is given. FAIL if no score is present.

For C-09 (regression signals): if no prior-round file is provided or available, write:
```
VERDICT: PARTIAL
EVIDENCE: No prior-round scorecard was provided.
WHY: The rubric N/A rule prescribes PARTIAL (not FAIL) when no prior data exists, provided the
     output explicitly states the no-prior-data condition.
```

---

**Step 3 -- Synthesize**

After scoring all N outputs, write five synthesis blocks in this order:

**COMPOSITE SCORES**
For each output, compute the score. Show the breakdown before the number:
```
V-XX: E=[count]/5, R=[count]/3, A=[count]/2
      composite = ([E_count]/5 * 60) + ([R_count]/3 * 30) + ([A_count]/2 * 10) = [score]
      Golden: [YES -- all 5 essential PASS and composite >= 80 | NO -- reason]
```
PARTIAL counts as 0.5. Show it explicitly: "E=3.5/5" not "E=3/5" when a PARTIAL exists.

**RANKED LEADERBOARD**
Rank all outputs highest to lowest composite. Ties noted explicitly.

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-XX | XX.X | YES/NO |

**FAILURE PATTERNS**
List any criterion receiving zero PASS across all N outputs (PARTIAL is not PASS).
If none: write exactly: `No failure patterns -- all criteria passed in at least one output.`
This section is required even when empty.

**EXCELLENCE SIGNALS**
List any output-criterion pair where one output clearly leads the field on that criterion.
Each signal must name: (1) the output, (2) the criterion, (3) the structural feature that produced
the outlier. "V-XX scored highest overall" is not an excellence signal.
If none: write exactly: `No excellence signals identified in this scoring run.`

**REGRESSION SIGNALS**
If prior-round data was provided: flag any PASS -> FAIL or PASS -> PARTIAL regressions by criterion
and output.
If not: write exactly: `No prior round data -- regression analysis cannot be performed.`

---

**Step 4 -- Arithmetic verification**

Pick one output. Independently verify its composite score using the stated E/R/A counts and the
formula. Write:
```
Verification: [output ID]
  E counts: [list verdicts and total]
  R counts: [list verdicts and total]
  A counts: [list verdicts and total]
  Computed: ([E]/5 * 60) + ([R]/3 * 30) + ([A]/2 * 10) = [result]
  Matches stated score: [YES | NO -- discrepancy: stated X, computed Y]
```

---

**Step 5 -- Write**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

where `{skill}` is the skill whose outputs were scored, `{round}` is the scoring round number,
and `{date}` is today's date in YYYY-MM-DD format.

---

## V-02 -- Lifecycle emphasis: hard phase gates with STOP tokens

**Axis**: B -- Lifecycle emphasis
**Hypothesis**: The four synthesis sections required after per-output scoring (C-05 failure
patterns, C-07 excellence signals, C-08 per-output notes, C-09 regression N/A) are the sections
most likely to be dropped under context pressure, because per-output work feels complete and
there is no structural signal that synthesis is pending. A hard STOP token -- a required verbatim
string that must appear in the output before the next phase can begin -- makes a skipped section
visible as a missing token rather than a soft omission. The gate enforces presence, not quality.
This round-1 test measures whether a presence gate alone is sufficient to surface C-05 and C-09
reliably, or whether quality enforcement must be layered on top.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** -- complete all phases in order; each phase closes with its required EXIT TOKEN:

| Phase | EXIT TOKEN (write verbatim) |
|-------|-----------------------------|
| LOAD | `=== LOAD COMPLETE ===` |
| SCORING | `=== SCORING COMPLETE — [N] outputs scored ===` |
| SYNTHESIS | `=== SYNTHESIS COMPLETE ===` |
| WRITE | `=== WRITE COMPLETE ===` |

Do not begin a phase until the previous phase's EXIT TOKEN appears in your output.

---

**Phase 1 -- LOAD**

Read the rubric file. Extract all criteria IDs and tiers, pass conditions, the composite formula,
the golden threshold, and all N/A rules. Read all N output files.

Write a load summary containing all four of the following; omitting any one makes C-01 PARTIAL:

```
Criteria: [each ID with its tier label -- Essential/Recommended/Aspirational]
Formula: [exact composite formula text from rubric]
Golden threshold: [exact condition text]
N/A rules: [each criterion that has a special N/A handling, or "none"]
Outputs: [list V-XX identifiers, count = N]
```

Write `=== LOAD COMPLETE ===` before proceeding.

---

**Phase 2 -- SCORING**

For each output V-XX, write a verdict table followed by a per-criterion evidence row.

**Verdict table** (one row per criterion):
| Criterion | Tier | Verdict | Evidence |
|-----------|------|---------|----------|
| C-01 | Essential | [PASS/PARTIAL/FAIL] | [direct quote or specific structural reference] |
| C-02 | Essential | ... | ... |
| C-03 | Essential | ... | ... |
| C-04 | Essential | ... | [must include the calculation form if PASS, or note its absence if PARTIAL/FAIL] |
| C-05 | Essential | ... | ... |
| C-06 | Recommended | ... | ... |
| C-07 | Recommended | ... | ... |
| C-08 | Recommended | ... | ... |
| C-09 | Aspirational | ... | [if no prior-round data: "PARTIAL -- no prior round data available"] |
| C-10 | Aspirational | ... | ... |

Evidence rules:
- Each evidence cell must reference specific output content: a quoted phrase, a named section,
  or a structural observation. Restating the criterion does not qualify.
- C-04 evidence must note whether the E/R/A breakdown was shown or only the final number.
- C-01 evidence must confirm which of the four sub-elements (IDs+tiers, formula, threshold,
  output count) are present.

After the last output's verdict table, write `=== SCORING COMPLETE — [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all six synthesis sections. Do not skip any.

**3a. Composite Scores**
For each output, show the tier breakdown and calculation explicitly:
`V-XX: E=[n]/5, R=[n]/3, A=[n]/2 -> composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/2 * 10) = [score]`
PARTIAL counts as 0.5. Golden: YES if all 5 essential PASS and composite >= 80.

**3b. Ranked Leaderboard**
All N outputs, descending by composite score. Ties stated explicitly.

**3c. Failure Patterns**
Any criterion with zero PASS across all N outputs (PARTIAL is not PASS for this purpose).
Required even when empty: write `No failure patterns -- all criteria passed in at least one output.`

**3d. Excellence Signals**
Any output-criterion pair where one output clearly leads the field structurally.
Each signal: name the output, criterion, and structural feature. Overall "scored highest" does not qualify.
Required even when empty: write `No excellence signals identified in this scoring run.`

**3e. Per-Output Synthesis Notes**
One paragraph per output explaining what it did structurally that raised or lowered its score
relative to the other outputs. Do not restate verdict counts -- explain the mechanism.

**3f. Regression Signals**
If prior-round data provided: flag PASS->FAIL or PASS->PARTIAL regressions by criterion and output.
If not: write `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all six sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.

---

## V-03 -- Phrasing register: worked examples inline

**Axis**: C -- Phrasing register
**Hypothesis**: The two most precise new requirements in v1-2026-03-16 -- C-01's four-sub-element
load block and C-04's explicit E/R/A calculation form -- are easy to satisfy partially without
noticing the miss. Abstract pass-condition language ("list all four sub-elements") is less reliable
than a positive anchor showing exactly what compliance looks like. Embedding a single compliant
example for C-01 and a single compliant example for C-04 inline with the instructions lets the
scorer copy the pattern rather than interpret the criterion. This approach trades prompt length
for precision targeting of the two most likely new-rubric PARTIALs.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

---

**Step 1 -- Load and verify**

Read the rubric. Read all N output files.

Write a load summary. The rubric for this task defines 10 criteria across 3 tiers.
Your load summary must contain all four of the following items -- if any one is missing, C-01
will score PARTIAL:

  (a) All criteria IDs with their tier labels (Essential / Recommended / Aspirational)
  (b) The exact composite formula text
  (c) The golden threshold condition
  (d) The number or list of outputs you will score

**Example of a compliant load summary:**
```
Criteria loaded:
  Essential: C-01, C-02, C-03, C-04, C-05
  Recommended: C-06, C-07, C-08
  Aspirational: C-09, C-10
Formula: (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 2 * 10)
Golden threshold: all 5 essentials PASS AND composite >= 80
Outputs: V-01, V-02, V-03, V-04, V-05 (N=5)
```
Use this format or an equivalent that contains all four items.

---

**Step 2 -- Score each output**

For each output V-XX, produce a verdict for every criterion (C-01 through C-10).

Format your scoring however you prefer (table or prose), but each verdict must include:
- The verdict (PASS / PARTIAL / FAIL)
- A specific evidence reference: a quoted phrase from the output, a named section, or a structural
  observation. Generic restatements of the criterion do not qualify as evidence.

**For C-04 specifically:** the pass condition requires you to show the explicit calculation, not
just the final number.

**Example of a compliant C-04 evidence note:**
```
C-04: PASS
Evidence: The output shows "V-03: E=4/5, R=3/3, A=1/2 -> composite = (4/5*60)+(3/3*30)+(1/2*10) = 83"
Why: the tier breakdown precedes the final number, satisfying the explicit-calculation requirement.
```

**Example of a C-04 PARTIAL (do not make this error):**
```
C-04: PASS
Evidence: V-03 composite score is 83.
```
The second form is PARTIAL because the tier counts are absent -- the score cannot be independently
verified from the stated evidence.

**For C-09 (regression signals):** if no prior-round scorecard was provided, write:
```
C-09: PARTIAL -- no prior round data available; regression analysis cannot be performed.
```
Do not write FAIL for this condition in round 1.

---

**Step 3 -- Synthesize**

After scoring all outputs, write these five sections:

**Composite Scores**
For each output, show the calculation explicitly before the final score:
```
V-XX: E=[n]/5, R=[n]/3, A=[n]/2
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/2 * 10) = [score]
```
PARTIAL counts as 0.5 toward the pass count. State golden status (YES/NO + reason).

**Ranked Leaderboard**
All outputs, descending by composite score. Ties noted.

**Failure Patterns**
Any criterion that received zero PASS across all N outputs is a failure pattern -- it signals a
rubric gap or skill design issue. If no criterion failed universally:
write exactly: `No failure patterns -- all criteria passed in at least one output.`
This section is required even when empty. Do not omit it.

**Excellence Signals**
Any output-criterion pair where one output clearly leads structurally on that criterion.
Each signal names: the output, the criterion, and the structural feature that produced the outlier.
"V-XX scored highest overall" is not an excellence signal.
If none: write exactly: `No excellence signals identified in this scoring run.`

**Per-Output Synthesis Notes**
One short paragraph per output: what did it do structurally that drove its score up or down?
Do not list verdict counts -- explain the mechanism.

---

**Step 4 -- Write**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-04 -- Combination: numbered blocks + phase gates (A+B)

**Axis**: A + B -- Output format + Lifecycle emphasis
**Hypothesis**: V-01's numbered blocks ensure C-01 four-sub-element compliance and C-04 explicit
calculation compliance but do not force synthesis sections to exist. V-02's phase gates force
synthesis sections to exist but do not enforce the slot-level precision that prevents C-01 and C-04
PARTIALs. Combining them layers a quality floor (per-slot templates) on top of a presence gate
(STOP tokens), addressing both the slot-precision failures and the synthesis-omission failures
simultaneously. The expected risk is prompt length: long prompts can cause the scorer to skim
instructions and satisfy templates superficially. This run measures whether the combination is
additive or whether one axis dominates.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** -- complete in order; each phase closes with its EXIT TOKEN:

| Phase | EXIT TOKEN (write verbatim) |
|-------|-----------------------------|
| LOAD | `=== LOAD COMPLETE ===` |
| SCORING | `=== SCORING COMPLETE — [N] outputs scored ===` |
| SYNTHESIS | `=== SYNTHESIS COMPLETE ===` |
| WRITE | `=== WRITE COMPLETE ===` |

---

**Phase 1 -- LOAD**

Read the rubric file. Read all N output files.

Write a numbered load block. Every field is required:

```
LOAD BLOCK
1. Criteria (ID + tier):
   Essential: C-01, C-02, C-03, C-04, C-05
   Recommended: C-06, C-07, C-08
   Aspirational: C-09, C-10
2. Formula (exact text from rubric):
   [paste here]
3. Golden threshold (exact text):
   [paste here]
4. N/A rules:
   [list, or "none"]
5. Outputs:
   [V-XX list, N=[count]]
```

All five fields must be present before LOAD COMPLETE.
Write `=== LOAD COMPLETE ===`

---

**Phase 2 -- SCORING**

For each output V-XX, write one numbered-block section containing one block per criterion (C-01
through C-10 in order). Block structure:

```
[V-XX / C-NN -- criterion short name]
VERDICT: [PASS | PARTIAL | FAIL]
EVIDENCE: [Direct quote or specific structural reference to this output's content.
           Generic criterion restatements do not qualify.]
WHY: [One sentence: name the mechanism behind the verdict.]
```

Extended fields for C-01:
```
SUBELEMENTS:
  (a) criteria IDs + tiers: [present | missing]
  (b) formula text: [present | missing]
  (c) golden threshold: [present | missing]
  (d) output count or list: [present | missing]
```
C-01 PASS = all four present. PARTIAL = one absent. FAIL = rubric not referenced.

Extended field for C-04:
```
CALC: [Reproduce the E/R/A breakdown as written in the output, e.g. "E=4/5, R=2/3, A=1/2 -> 76.7".
       If no breakdown shown: "calculation not shown -- PARTIAL".]
```
C-04 PASS = E/R/A breakdown present. PARTIAL = final number only. FAIL = no score.

For C-09: if no prior-round file was provided, use:
```
VERDICT: PARTIAL
EVIDENCE: No prior-round scorecard provided.
WHY: Rubric N/A rule: PARTIAL (not FAIL) when scorer states the no-prior-data condition.
```

After the last output's blocks, write `=== SCORING COMPLETE — [N] outputs scored ===`

---

**Phase 3 -- SYNTHESIS**

Write all six synthesis sections. Each is required; a missing section is a structural error.

**3a. Composite Scores**
```
V-XX: E=[n]/5 ([verdict list]), R=[n]/3, A=[n]/2
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/2 * 10) = [score]
      Golden: YES | NO ([reason])
```
PARTIAL = 0.5 toward pass count. Show it as a decimal (E=3.5/5 not E=3/5).

**3b. Ranked Leaderboard**
All N outputs descending. Ties noted.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|
| 1 | V-XX | XX.X | YES/NO |

**3c. Failure Patterns**
Criteria with zero PASS across all N outputs. PARTIAL is not PASS for this test.
If none: `No failure patterns -- all criteria passed in at least one output.`
Required even when empty.

**3d. Excellence Signals**
Output-criterion pairs where one output structurally leads the field. Each entry:
- Output ID, Criterion ID
- Structural feature that produced the outlier
Overall ranking ("scored highest") does not qualify.
If none: `No excellence signals identified in this scoring run.`

**3e. Per-Output Synthesis Notes**
One paragraph per output: what structural choices drove its score? Do not recount verdicts.

**3f. Regression Signals**
Prior round provided: flag PASS->FAIL or PASS->PARTIAL regressions.
No prior round: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===`

---

**Phase 4 -- WRITE**

Write the scorecard to `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`.
Write `=== WRITE COMPLETE ===`

---

## V-05 -- Combination: numbered blocks + phase gates + worked examples (A+B+C)

**Axis**: A + B + C -- Output format + Lifecycle emphasis + Phrasing register
**Hypothesis**: V-04 combines slot precision with presence gates but provides no positive anchor
for the two hardest new-rubric requirements (C-01 four-sub-element block, C-04 E/R/A form). V-03's
worked examples show compliance patterns at the point of instruction rather than abstractly. Adding
V-03's inline examples to V-04's template+gate structure should eliminate the new-rubric PARTIALs
most likely to appear in R1 (C-01 incomplete load, C-04 bare-number score) while preserving the
phase-gate protection for synthesis sections. This is the maximal variation and tests whether the
three axes are fully additive or whether one axis's mechanism is redundant when the others are
present.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** -- complete in order; each phase closes with its EXIT TOKEN:

| Phase | EXIT TOKEN (write verbatim) |
|-------|-----------------------------|
| LOAD | `=== LOAD COMPLETE ===` |
| SCORING | `=== SCORING COMPLETE — [N] outputs scored ===` |
| SYNTHESIS | `=== SYNTHESIS COMPLETE ===` |
| WRITE | `=== WRITE COMPLETE ===` |

---

**Phase 1 -- LOAD**

Read the rubric file. Read all N output files.

Write a numbered load block. Every field is required. C-01 is Essential and requires all four
sub-elements to be present in your load block to score PASS.

**Compliant load block (copy this format):**
```
LOAD BLOCK
1. Criteria (ID + tier):
   Essential: C-01, C-02, C-03, C-04, C-05
   Recommended: C-06, C-07, C-08
   Aspirational: C-09, C-10
2. Formula (exact):
   composite = (essential_pass / 5 * 60)
             + (recommended_pass / 3 * 30)
             + (aspirational_pass / 2 * 10)
3. Golden threshold:
   all 5 essentials PASS AND composite >= 80
4. N/A rules:
   C-09: PARTIAL (not FAIL) when scorer writes "no prior round data available"
5. Outputs:
   V-01, V-02, V-03, V-04, V-05 (N=5)  [replace with actual list]
```

The load block without any one of fields 1-5 will score C-01 PARTIAL.
Write `=== LOAD COMPLETE ===`

---

**Phase 2 -- SCORING**

For each output V-XX, write one numbered-block section (C-01 through C-10 in order).

Block structure:
```
[V-XX / C-NN -- criterion short name]
VERDICT: [PASS | PARTIAL | FAIL]
EVIDENCE: [specific reference to this output -- quote, section name, or structural observation;
           restating the criterion does not qualify]
WHY: [one sentence: name the mechanism behind the verdict]
```

**C-01 extended block** -- add SUBELEMENTS:
```
SUBELEMENTS:
  (a) criteria IDs + tiers: [present | missing]
  (b) formula text: [present | missing]
  (c) golden threshold: [present | missing]
  (d) output count or list: [present | missing]
```

**C-04 extended block** -- add CALC:
```
CALC: [the E/R/A breakdown from this output, e.g., "E=4/5, R=2/3, A=1/2 -> composite = 76.7"]
```

**Compliant C-04 block (this is PASS):**
```
[V-03 / C-04 -- composite score]
VERDICT: PASS
EVIDENCE: Output states "V-03: E=4/5, R=3/3, A=1/2 -> composite = (4/5*60)+(3/3*30)+(1/2*10) = 83"
WHY: The tier counts precede the final number; score is independently verifiable from stated verdicts.
CALC: E=4/5, R=3/3, A=1/2 -> 83
```

**Non-compliant C-04 block (this is PARTIAL -- do not produce this):**
```
[V-03 / C-04 -- composite score]
VERDICT: PASS
EVIDENCE: Output shows composite score of 83.
WHY: Score is present.
CALC: 83 [no breakdown]
```
The second form is PARTIAL: the breakdown is absent and the score cannot be independently verified.

**For C-09 (no prior round):**
```
[V-XX / C-09 -- regression signals]
VERDICT: PARTIAL
EVIDENCE: No prior-round scorecard was provided or available.
WHY: Rubric N/A rule prescribes PARTIAL when scorer states the no-prior-data condition.
```

After the last output, write `=== SCORING COMPLETE — [N] outputs scored ===`

---

**Phase 3 -- SYNTHESIS**

All six sections required. Do not skip any. Write them in order.

**3a. Composite Scores**
Show tier breakdown before the final number. PARTIAL = 0.5.
```
V-XX: E=[n]/5, R=[n]/3, A=[n]/2
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/2 * 10) = [score]
      Golden: YES | NO
```

**3b. Ranked Leaderboard** -- all outputs descending; ties noted.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|

**3c. Failure Patterns**
Criteria with zero PASS across all N outputs (PARTIAL is not PASS for this check).
Required even when empty: `No failure patterns -- all criteria passed in at least one output.`

**3d. Excellence Signals**
Output-criterion pairs where one output structurally leads. Each entry: output, criterion, mechanism.
"V-XX scored highest" is not sufficient.
Required even when empty: `No excellence signals identified in this scoring run.`

**3e. Per-Output Synthesis Notes**
One paragraph per output: structural choices that drove its score. Do not recount verdicts.

**3f. Regression Signals**
`No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===`

---

**Phase 4 -- WRITE**

Write `=== WRITE COMPLETE ===` after saving to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`
