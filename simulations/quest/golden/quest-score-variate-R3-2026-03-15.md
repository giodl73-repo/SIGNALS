# quest-score Variate -- Round 3
# Generated: 2026-03-15

---

## Context: what informed this round

Round 3 targets the v3 rubric. Three excellence signals from Round 2 were promoted to
aspirational criteria:

- **C-12 -- Phase-separated narrative**: the per-output narrative must inhabit a structurally
  distinct *named phase* from the per-criterion verdict blocks; "after the table" within the
  same section does not qualify. Source: R2-V-01 satisfied this by placing narratives in the
  SYNTHESIS phase, separated from SCORING by a gate token. R2-V-02 was PARTIAL -- "outside
  and after all scoring blocks" is a placement instruction, not a phase boundary.
- **C-13 -- Inline regression annotation**: CHANGE notes must be written at the scoring site
  during the scoring pass; the synthesis regression section must draw from those inline
  annotations rather than performing a fresh BASELINE TABLE lookup. Source: R2-V-02 (E axis)
  introduced inline CHANGE fields, but its Regression Signals section reads "Using the
  BASELINE TABLE from Phase 0" -- a fresh lookup that violates C-13's constraint.
- **C-14 -- Baseline load gate**: prior-round verdict data must be confirmed loaded via a gate
  token before any scoring block begins. Source: R2-V-02 Phase 0 with `[PRIOR ROUND LOAD
  COMPLETE]` already satisfies this; the v3 rubric formalizes it.

**C-13 gap in R2 baseline**: R2-V-02's CHANGE fields fire inline correctly (satisfying C-13's
scoring-site requirement), but the Regression Signals section in synthesis performs a fresh
BASELINE TABLE lookup rather than drawing from collected inline annotations. This is a
structural gap: C-13 requires synthesis to *consume* annotations, not re-derive them from
Phase 0. Round 3 must close this gap.

**C-12 baseline status**: R2-V-01 (D axis) places per-output narratives at the top of Phase 3
SYNTHESIS, after the `[ANALYST COMPLETE]` and `[VERIFIER COMPLETE]` gates -- technically two
gate boundaries separate narratives from scoring blocks, satisfying C-12. However, narratives
share SYNTHESIS with composite scores, leaderboard, failure patterns, and excellence signals.
A scorer who conflates can embed per-output comments into leaderboard entries. Round 3 axis G
tests whether a dedicated NARRATIVE phase adds isolation guarantees beyond what the baseline
already provides.

**Consequence for Round 3**: A+B+C+D+E+F is the established baseline. All Round 3 variations
inherit this baseline so that C-09, C-10, C-11, C-12 (via SYNTHESIS phase), C-14 are
structurally covered. The new axes (G, H, I) test three independent improvements targeting
C-12 hardening, C-13 enforcement, and C-13 synthesis-gap closure.

**v3 rubric counts**: E=5 (C-01..C-05), R=2 (C-06..C-07), A=7 (C-08..C-14)
**Formula**: `(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/7 * 70)`
**Max**: 160
**Golden threshold**: all 5 essentials PASS AND composite >= 80
**N/A rules**:
- C-08: PARTIAL (not FAIL) when scorer explicitly states "no prior round data available"
- C-13: PARTIAL (not FAIL) when no prior round data exists (CHANGE fields cannot fire)
- C-14: PARTIAL (not FAIL) when no prior round data exists and output explicitly states this

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| G | Lifecycle emphasis -- NARRATIVE isolation phase | The baseline satisfies C-12 (narratives in SYNTHESIS, downstream of scoring gate), but narratives share SYNTHESIS with composite scores, leaderboard, and other synthesis sections. A scorer under context pressure can embed per-output comments into leaderboard rows or excellence signal entries and call C-07 satisfied, leaving the dedicated narrative section thin or absent. A dedicated NARRATIVE phase -- between VERIFIER AUDIT and SYNTHESIS, with its own exit token -- makes this conflation structurally detectable: a per-output comment that appears in SYNTHESIS rather than NARRATIVE phase is misplaced. This elevates C-12 from a placement constraint to an isolation constraint. |
| H | Output format -- Mandatory bidirectional CHANGE field | C-13's pass condition requires each criterion block to contain an inline CHANGE slot. The baseline (R2-E) uses a conditional form: `[CHANGE: if verdict differs from baseline]`. A scorer who matches baseline can silently omit the annotation -- the conditional phrasing makes omission look compliant. Making the field mandatory -- requiring either "NO CHANGE" or "CHANGE from [prior]: [reason]" for every criterion block -- removes conditionality: the field must appear even when no change occurred. Omission is now detectable as a structural gap, not a soft miss. |
| I | Role sequence -- CHANGE MANIFEST extraction phase | C-13 requires synthesis to draw from inline annotations, with no fresh baseline lookup in synthesis. The baseline violates this: Regression Signals reads "Using the BASELINE TABLE from Phase 0." A dedicated CHANGE MANIFEST phase -- placed between VERIFIER AUDIT and SYNTHESIS -- sweeps all inline CHANGE entries and builds a structured extraction table. SYNTHESIS Regression Signals then draws from CHANGE MANIFEST and is explicitly prohibited from re-reading BASELINE TABLE. This is the only design where C-13's "no fresh baseline lookup" constraint is enforced by architecture rather than by instruction alone. |

Single-axis runs: V-01 (G), V-02 (H), V-03 (I)
Combinations: V-04 (G+H), V-05 (G+H+I)

Rubric in scope: `simulations/quest/rubrics/quest-score-rubric-v3-2026-03-15.md`
Formula: `(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/7 * 70)`
N_essential=5, N_recommended=2, N_aspirational=7
Golden threshold: all 5 essentials PASS AND composite >= 80

---

## V-01 -- Lifecycle emphasis: NARRATIVE isolation phase

**Axis**: G -- Lifecycle emphasis
**Hypothesis**: The baseline satisfies C-12 technically -- narratives live in SYNTHESIS,
downstream of the `[ANALYST COMPLETE]` and `[VERIFIER COMPLETE]` gates. But SYNTHESIS is a
multi-purpose phase: it also contains composite scores, leaderboard, failure patterns, and
excellence signals. A scorer can embed per-output comments ("V-03 degraded because...")
inside a leaderboard row or excellence signal entry, then write a thin or absent dedicated
narrative section. C-12 is technically violated but structurally invisible because the
phase boundary is between SCORING and SYNTHESIS, not between synthesis sections. A dedicated
NARRATIVE phase -- between VERIFIER AUDIT and SYNTHESIS, closed by `[NARRATIVE COMPLETE]`
before SYNTHESIS opens -- makes the conflation structurally detectable: any per-output
comment that appears in SYNTHESIS phase is misplaced; the NARRATIVE gate is the only valid
container. Round 3 tests whether the isolation gate adds reliable C-12 enforcement beyond
the SCORING-to-SYNTHESIS boundary the baseline already provides.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path (required for regression analysis; if unavailable, state
  "no prior round data" in Phase 0 and proceed)

**INERTIA PATTERN -- read before scoring anything**

The following is what a weak scorer produces. Do not produce output that resembles this.

```
WEAK SCORER EXAMPLE (do not produce this):

**C-02 -- Evidence for every verdict** | PASS
*Evidence*: The output provides evidence cells for each criterion.
*Why*: Evidence is present throughout the scoring section.

**C-07 -- Per-output evidence notes** | PASS
*Evidence*: Each output includes a narrative explanation inside its scoring block.
*Why*: The prose block covers mechanism and reasoning together.

**C-12 -- Phase-separated narrative** | PASS
*Evidence*: The narrative appears after the verdict table in the scoring section.
*Why*: Placement after the table separates it from the verdict blocks.

[CHANGE notes written in Regression Signals during synthesis, not inline during scoring]

[Regression Signals: Based on reviewing the baseline table again, V-03 regressed on C-07...]

[No Failure Patterns section]
[Leaderboard -- see composite scores above]
```

The inertia failures above:
1. **Criterion restatement**: "provides evidence cells for each criterion" restates C-02.
   Evidence must quote or specifically reference the output: "The V-XX prose blocks each
   contain an `*Evidence*:` line quoting output text directly" is evidence.
2. **C-07/C-12 conflation**: A narrative inside the scoring block does NOT satisfy C-07 or
   C-12. Per C-12, "after the table within the same section" is explicitly excluded. The
   narrative must inhabit a *named phase* downstream of the scoring phase gate.
3. **Deferred CHANGE notes (C-13 violation)**: CHANGE notes written in synthesis from memory
   do not satisfy C-13. The CHANGE slot must fire during the scoring pass, at each criterion
   block. Synthesis draws from those inline annotations -- it does not derive them fresh.
4. **Fresh baseline lookup in synthesis (C-13 violation)**: "Based on reviewing the baseline
   table again" is the exact failure C-13 prohibits. Regression Signals must draw from inline
   CHANGE annotations written during ANALYST SCORING.
5. **Missing required sections**: Failure Patterns and Leaderboard must be explicit sections.
   Pointers to other sections do not satisfy C-04 or C-05.

Before each `*Evidence*:` line: ask "Am I quoting or specifically referencing the output, or
am I restating the criterion?" If the latter, rewrite.

---

**Phase manifest** -- complete in order, each phase closes with its EXIT TOKEN before
the next phase begins:

| Phase | EXIT TOKEN |
|-------|------------|
| PRIOR ROUND LOAD | `[PRIOR ROUND LOAD COMPLETE]` |
| LOAD | `[LOAD COMPLETE]` |
| ANALYST SCORING | `[ANALYST COMPLETE -- N outputs scored]` |
| VERIFIER AUDIT | `[VERIFIER COMPLETE]` |
| NARRATIVE | `[NARRATIVE COMPLETE]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**Phase 0 -- PRIOR ROUND LOAD**

If a prior-round scorecard is provided:
1. Read the file.
2. Extract every output-criterion verdict. Build a BASELINE TABLE:

```
BASELINE TABLE (Round N-1):
| Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 |
|--------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| V-01   | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  |
...
```

3. Note any criteria with universal PARTIAL/FAIL (potential persistent patterns).

If no prior-round scorecard is provided:
Write: `No prior round data available -- C-08, C-13, C-14 will be scored PARTIAL.`

Write: `[PRIOR ROUND LOAD COMPLETE]`

---

**Phase 1 -- LOAD**

Read the rubric. Extract: all criteria IDs and tiers, pass conditions, the composite formula,
the golden threshold, and all N/A rules. Read all N output files.

Write:
```
Criteria: [IDs and tiers, comma-separated]
Formula: [exact formula text]
Golden threshold: [condition]
N/A rules: [list, or "none"]
Outputs loaded: [V-XX list]
```

Write: `[LOAD COMPLETE]`

---

**Phase 2 -- ANALYST SCORING**

ANALYST role: for each output V-XX, write one prose-block section. One block per criterion,
in criterion order:

```
### V-XX: [axis label]

**C-01 -- Per-criterion verdict matrix** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference from this output]
*Why*: [one sentence naming the structural property that causes this verdict]
[CHANGE: if verdict differs from BASELINE TABLE, write "CHANGE from [prior]: [reason]"]
NOTE: Formats vary (table, list, grouped blocks). Every criterion-output cell must have a
stated verdict. Implied verdicts count only if unambiguous.

**C-02 -- Evidence for every verdict** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference -- not a criterion restatement]
*Why*: [mechanism: why does this evidence support the verdict]
[CHANGE: if verdict differs from baseline]
NOTE: Generic notes satisfy C-02 only if the form is narrow and unambiguous. Criterion
restatements ("output provides evidence") never satisfy C-02.

**C-03 -- Composite score per output** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: Any denominator-based or weighted score counts. "X/Y" fractions satisfy if the
formula is documented elsewhere in the output.

**C-04 -- Ranked leaderboard** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: A pointer to a score table ("see above") does NOT satisfy C-04. An explicit ranked
list or unambiguously sorted section is required.

**C-05 -- Failure patterns called out** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: The section must exist and either name patterns or explicitly state their absence.
Omitting the section is FAIL, even when no patterns exist.

**C-06 -- Excellence signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: An excellence signal requires a specific output-criterion pairing, not a general
comment that one output scored highest.

**C-07 -- Per-output evidence notes** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: A narrative inside the scoring block does NOT satisfy C-07. A dedicated section in a
named downstream phase -- specifically the NARRATIVE phase in this prompt -- is required.

**C-08 -- Regression signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [reference to BASELINE TABLE, or "PARTIAL -- no prior round data available"]
*Why*: [mechanism sentence, or "N/A -- no prior data"]
NOTE: N/A condition: score PARTIAL (not FAIL) when no prior round data and output states this.

**C-09 -- Anti-pattern anchor** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: The anchor must precede scoring instructions, not follow them. A post-hoc note fails.

**C-10 -- Structural completion gate** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: Gate must cover all three synthesis sections (failure patterns, leaderboard, excellence
signals). A gate covering only one section is PARTIAL.

**C-11 -- Mechanism prompting** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: A `*Why*` field asking "what structural feature does this demonstrate" satisfies C-11.
A field asking only for "more detail" does not.

**C-12 -- Phase-separated narrative** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: "After the table within the same section" does NOT qualify. A named phase with its
own gate token is required. PARTIAL if narrative is labeled distinctly but shares a phase
heading with scoring blocks or with synthesis sections.

**C-13 -- Inline regression annotation** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline, or "N/A -- no prior data"]
NOTE: Each criterion block must contain an inline CHANGE slot. Synthesis must draw from
those annotations rather than re-reading BASELINE TABLE. PARTIAL when no prior round data.

**C-14 -- Baseline load gate** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline, or "N/A -- no prior data"]
NOTE: A gate token must appear before the first scoring block. PARTIAL when no prior data.
When prior data exists, absence of gate is FAIL.
```

Score all N outputs before writing the EXIT TOKEN.

Write: `[ANALYST COMPLETE -- N outputs scored]` (replace N with the actual count)

---

**Phase 3 -- VERIFIER AUDIT**

VERIFIER role: audit the ANALYST's `*Evidence*:` lines only. Do not re-score verdicts.

For each output V-XX, read every `*Evidence*:` line. Classify each as:
- **SPECIFIC**: quotes or specifically references this output (names a section, quotes a
  string, references a structural element present in this output specifically)
- **RESTATED**: restates the criterion text, describes what the criterion requires, or uses
  language that would apply to any output without modification

For every RESTATED finding:
```
VERIFIER FLAG -- V-XX / C-NN:
RESTATED: "[the restated evidence text]"
REQUIRED: [one sentence describing what a specific reference looks like for this output]
```

If no RESTATED findings for an output:
`VERIFIER: V-XX -- all evidence cells specific.`

Write: `[VERIFIER COMPLETE]`

---

**Phase 4 -- NARRATIVE** *(new in V-01)*

Write one narrative section per output. This phase contains ONLY per-output narratives --
no composite scores, no leaderboard rows, no synthesis content of any kind.

```
### Narrative: V-XX

[Two to four sentences explaining why this output scored as it did. Reference at least one
specific structural feature -- a section name, a field format, a phase token, a gate ID --
that drove the composite result. If any CHANGE annotations were written for this output
during ANALYST SCORING, explain the change direction and its cause. Do not restate the
verdict counts; explain the mechanism behind them.]
```

Write one section per output. All per-output narratives must appear in this phase. Do not
write per-output narratives in SYNTHESIS.

Write: `[NARRATIVE COMPLETE]`

---

**Phase 5 -- SYNTHESIS**

Write five synthesis sections. All are required. Do not write per-output narratives here --
they belong in the NARRATIVE phase and must not appear in SYNTHESIS.

**Composite Scores**
For each output, apply:
```
essential_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-01..C-05
recommended_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-06..C-07
aspirational_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-08..C-14
composite = (essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/7 * 70)
```
Show each calculation: `V-XX: E=X/5, R=X/2, A=X/7 -> composite = XX`

**Ranked Leaderboard**
Explicit ranked list of all outputs, descending by composite score. Ties noted. This section
is not a pointer to the composite scores section.

**Failure Patterns**
Criteria where no output earned PASS across the full run. These signal rubric gaps or
systematic skill design issues.
If none: `No failure patterns -- all criteria earned PASS in at least one output.`

**Excellence Signals**
Specific output-criterion pairs where one output structurally outperforms the others on that
criterion. Name the output, the criterion, and the structural feature.
If none: `No excellence signals identified in this scoring run.`

**Regression Signals**
Collect all `[CHANGE: ...]` annotations written during ANALYST SCORING. List every
criterion-output pair where the current verdict is lower than baseline (PASS->PARTIAL,
PASS->FAIL, or PARTIAL->FAIL).
If no prior round data: `No prior round data -- regression analysis cannot be performed.`
If no regressions: `No regressions detected -- all verdicts held or improved from prior round.`

Write: `[SYNTHESIS COMPLETE]`

---

**Phase 6 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

where `{skill}` is the skill whose outputs were scored, `{round}` is the scoring round
number, and `{date}` is today's date in YYYY-MM-DD format.

Write: `[WRITE COMPLETE]`

---

## V-02 -- Output format: mandatory bidirectional CHANGE field

**Axis**: H -- Output format
**Hypothesis**: C-13's pass condition requires each criterion block to contain an inline CHANGE
slot. The baseline (R2-E) uses a conditional form: `[CHANGE: if verdict differs from baseline]`.
A scorer who matches baseline on every criterion can silently omit all CHANGE annotations --
the conditional phrasing makes omission look compliant ("no changes, so no annotations needed").
This creates a hidden structural gap: if the baseline verdicts are wrong and the scorer doesn't
notice, the silent omission goes undetected. Making the field mandatory -- requiring either
"NO CHANGE" or "CHANGE from [prior]: [reason]" for every criterion block -- removes
conditionality entirely. The field must appear even when no change occurred. Omission is now
detectable as a structural gap: a criterion block without a `*Change*:` line is visibly
incomplete. Round 3 tests whether the mandatory bidirectional format produces more reliable
C-13 compliance by transforming the CHANGE slot from an opt-in annotation to a required
output field that confirms engagement with the baseline even when no change is detected.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path (required for regression analysis; if unavailable, state
  "no prior round data" in Phase 0 and proceed)

**INERTIA PATTERN -- read before scoring anything**

The following is what a weak scorer produces. Do not produce output that resembles this.

```
WEAK SCORER EXAMPLE (do not produce this):

**C-02 -- Evidence for every verdict** | PASS
*Evidence*: The output provides evidence cells for each criterion.
*Why*: Evidence is present throughout.
[no *Change*: field -- omitted because verdict matched baseline]

**C-07 -- Per-output evidence notes** | PASS
*Evidence*: Each output includes a narrative explanation inside the scoring block.
*Why*: The prose block covers mechanism and reasoning together.
[no *Change*: field -- omitted because verdict matched baseline]

**C-12 -- Phase-separated narrative** | PASS
*Evidence*: Narrative appears after the verdict table in the same scoring section.
*Why*: Placement after the table constitutes separation.
[no *Change*: field]

[Regression Signals: Based on reviewing the baseline table again, V-03 regressed on C-07]

[No Failure Patterns section]
[Leaderboard -- see composite scores above]
```

The inertia failures above:
1. **Criterion restatement**: "provides evidence cells for each criterion" restates C-02.
2. **C-07/C-12 conflation**: Narrative inside the scoring block fails both criteria.
3. **Missing *Change*: fields (C-13 violation)**: Even when the verdict matches baseline, the
   `*Change*:` field must appear and read "NO CHANGE". Omitting it for unchanged criteria
   makes the CHANGE annotation look optional -- it is not. Absence cannot be distinguished
   from a missed comparison.
4. **Fresh baseline lookup in synthesis (C-13 violation)**: "Based on reviewing the baseline
   table again" is the exact failure C-13 prohibits. Regression Signals must draw from the
   inline `*Change*:` fields written during ANALYST SCORING.
5. **Missing required sections**: Failure Patterns and Leaderboard must be explicit sections.

Before each `*Evidence*:` line: check for restatement.
Before each `*Change*:` field: consult BASELINE TABLE. Write "NO CHANGE" or
"CHANGE from [prior]: [reason]". This field is never optional.

---

**Phase manifest** -- complete in order, each phase closes with its EXIT TOKEN:

| Phase | EXIT TOKEN |
|-------|------------|
| PRIOR ROUND LOAD | `[PRIOR ROUND LOAD COMPLETE]` |
| LOAD | `[LOAD COMPLETE]` |
| ANALYST SCORING | `[ANALYST COMPLETE -- N outputs scored]` |
| VERIFIER AUDIT | `[VERIFIER COMPLETE]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**Phase 0 -- PRIOR ROUND LOAD**

If a prior-round scorecard is provided:
1. Read the file.
2. Extract every output-criterion verdict. Build a BASELINE TABLE:

```
BASELINE TABLE (Round N-1):
| Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 |
|--------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| V-01   | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  |
...
```

3. Note any criteria with universal PARTIAL/FAIL.

If no prior-round scorecard:
Write: `No prior round data available -- C-08, C-13, C-14 will be scored PARTIAL.`

Write: `[PRIOR ROUND LOAD COMPLETE]`

---

**Phase 1 -- LOAD**

Read the rubric and all N output files. Write:
```
Criteria: [IDs and tiers, comma-separated]
Formula: [exact formula text]
Golden threshold: [condition]
N/A rules: [list, or "none"]
Outputs loaded: [V-XX list]
```

Write: `[LOAD COMPLETE]`

---

**Phase 2 -- ANALYST SCORING**

ANALYST role: for each output V-XX, write one prose-block section. The `*Change*:` field is
ALWAYS REQUIRED -- write "NO CHANGE" or "CHANGE from [prior]: [reason]" for every block:

```
### V-XX: [axis label]

**C-01 -- Per-criterion verdict matrix** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [structural property sentence]
*Change*: [NO CHANGE | CHANGE from [prior verdict]: [reason] -- always fill this field]
NOTE: Formats vary. Every criterion-output cell must have a stated verdict.

**C-02 -- Evidence for every verdict** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference -- not a restatement]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Criterion restatements never satisfy C-02.

**C-03 -- Composite score per output** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Any denominator-based score counts. "X/Y" fractions satisfy if formula is documented.

**C-04 -- Ranked leaderboard** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Pointer to score table does NOT satisfy C-04. Explicit ranked list required.

**C-05 -- Failure patterns called out** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Section must exist even when empty. Omitting is FAIL.

**C-06 -- Excellence signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Specific output-criterion pairing required.

**C-07 -- Per-output evidence notes** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Narrative inside scoring block does NOT satisfy C-07. Dedicated section in a named
downstream phase is required.

**C-08 -- Regression signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [reference to BASELINE TABLE, or "PARTIAL -- no prior round data available"]
*Why*: [mechanism sentence, or "N/A -- no prior data"]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- or "N/A -- no prior data"]
NOTE: PARTIAL (not FAIL) when no prior round data and output explicitly states this.

**C-09 -- Anti-pattern anchor** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Anchor must precede scoring instructions.

**C-10 -- Structural completion gate** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Gate must cover all three synthesis sections.

**C-11 -- Mechanism prompting** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: `*Why*` field asking "what structural feature" satisfies C-11.

**C-12 -- Phase-separated narrative** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: "After the table within the same section" does NOT qualify. Named phase with gate
token required. PARTIAL if narrative shares a phase heading with scoring or synthesis.

**C-13 -- Inline regression annotation** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- or "N/A -- no prior data"]
NOTE: Mandatory `*Change*:` in every block (not conditional) is the key property. Synthesis
must draw from these fields, not re-read BASELINE TABLE. PARTIAL when no prior data.

**C-14 -- Baseline load gate** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- or "N/A -- no prior data"]
NOTE: Gate token before first scoring block required. PARTIAL when no prior data.
When prior data exists, absence of gate is FAIL.
```

Score all N outputs, then write: `[ANALYST COMPLETE -- N outputs scored]`

---

**Phase 3 -- VERIFIER AUDIT**

VERIFIER role: audit `*Evidence*:` lines for criterion restatement. Do not re-score.

For every RESTATED finding:
```
VERIFIER FLAG -- V-XX / C-NN:
RESTATED: "[restated evidence text]"
REQUIRED: [what a specific reference looks like for this output]
```

If none: `VERIFIER: V-XX -- all evidence cells specific.`

Write: `[VERIFIER COMPLETE]`

---

**Phase 4 -- SYNTHESIS**

Write a per-output narrative section first. Each narrative is outside and after all scoring
blocks and the VERIFIER AUDIT:

```
### Narrative: V-XX

[Two to four sentences explaining why this output scored as it did. Reference at least one
specific structural feature. If any `*Change*:` entries for this output read "CHANGE from
[prior]", explain the change direction and cause. Do not restate verdict counts.]
```

Then write five synthesis sections. All are required.

**Composite Scores**
For each output, apply:
```
essential_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-01..C-05
recommended_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-06..C-07
aspirational_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-08..C-14
composite = (essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/7 * 70)
```
Show: `V-XX: E=X/5, R=X/2, A=X/7 -> composite = XX`

**Ranked Leaderboard**
Explicit ranked list, descending. Ties noted. Not a pointer to composite scores.

**Failure Patterns**
Criteria where no output earned PASS. If none: `No failure patterns -- all criteria earned
PASS in at least one output.`

**Excellence Signals**
Specific output-criterion pairs with structural outliers. Name output, criterion, feature.
If none: `No excellence signals identified in this scoring run.`

**Regression Signals**
Collect all `*Change*:` fields written during ANALYST SCORING. List every criterion-output
pair where a "CHANGE from [prior]" entry shows current verdict < prior verdict
(PASS->PARTIAL, PASS->FAIL, PARTIAL->FAIL). Do not re-read the BASELINE TABLE in this section.
If no prior data: `No prior round data -- regression analysis cannot be performed.`
If no regressions: `No regressions detected -- all verdicts held or improved.`

Write: `[SYNTHESIS COMPLETE]`

---

**Phase 5 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write: `[WRITE COMPLETE]`

---

## V-03 -- Role sequence: CHANGE MANIFEST extraction phase

**Axis**: I -- Role sequence
**Hypothesis**: C-13 requires two properties: (1) CHANGE notes written at the scoring site,
and (2) synthesis draws from those notes rather than re-reading BASELINE TABLE. The baseline
achieves (1) with inline conditional CHANGE fields. It fails (2): Regression Signals says
"Collect all `[CHANGE: ...]` annotations" -- an informal instruction that relies on the scorer
scanning back through all scoring blocks under late-context pressure. Under that pressure, some
CHANGE fields are missed or misread, and the scorer falls back on re-reading BASELINE TABLE.
A dedicated CHANGE MANIFEST phase -- between VERIFIER AUDIT and SYNTHESIS -- sweeps all inline
CHANGE entries and builds a structured table before synthesis begins. SYNTHESIS Regression
Signals explicitly references CHANGE MANIFEST and is explicitly prohibited from re-reading
BASELINE TABLE. This is the only design where C-13's "no fresh baseline lookup in synthesis"
is enforced by architecture (the MANIFEST is a structural intermediary) rather than by
instruction alone. Round 3 tests whether the CHANGE MANIFEST phase produces structurally
reliable C-13 synthesis compliance without adding enough phase overhead to compress
the SYNTHESIS sections.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path (required for regression analysis; if unavailable, state
  "no prior round data" in Phase 0 and proceed)

**INERTIA PATTERN -- read before scoring anything**

The following is what a weak scorer produces. Do not produce output that resembles this.

```
WEAK SCORER EXAMPLE (do not produce this):

**C-02 -- Evidence for every verdict** | PASS
*Evidence*: The output provides evidence cells for each criterion.
*Why*: Evidence is present throughout.

**C-07 -- Per-output evidence notes** | PASS
*Evidence*: Each output includes a narrative explanation inside the scoring block.
*Why*: The prose block covers mechanism and reasoning together.

**C-12 -- Phase-separated narrative** | PASS
*Evidence*: Narrative appears after the verdict table in the same section.
*Why*: Placement after the table constitutes separation.

[No CHANGE MANIFEST phase -- inline CHANGE fields present but not extracted]

[Regression Signals: Based on reviewing the baseline table again, V-03 regressed on C-07...]

[No Failure Patterns section]
[Leaderboard -- see composite scores above]
```

The inertia failures above:
1. **Criterion restatement**: "provides evidence cells" restates C-02.
2. **C-07/C-12 conflation**: Narrative inside scoring block fails both criteria.
3. **No CHANGE MANIFEST phase (C-13 violation)**: Inline CHANGE fields without a CHANGE
   MANIFEST extraction phase forces synthesis to re-scan scoring blocks or re-read BASELINE
   TABLE. The MANIFEST phase is the structural intermediary that eliminates fresh lookup.
4. **Fresh baseline lookup in synthesis (C-13 violation)**: "Based on reviewing the baseline
   table again" is the exact path CHANGE MANIFEST eliminates by construction.
5. **Missing required sections**: Failure Patterns and Leaderboard must be explicit.

---

**Phase manifest** -- complete in order, each phase closes with its EXIT TOKEN:

| Phase | EXIT TOKEN |
|-------|------------|
| PRIOR ROUND LOAD | `[PRIOR ROUND LOAD COMPLETE]` |
| LOAD | `[LOAD COMPLETE]` |
| ANALYST SCORING | `[ANALYST COMPLETE -- N outputs scored]` |
| VERIFIER AUDIT | `[VERIFIER COMPLETE]` |
| CHANGE MANIFEST | `[CHANGE MANIFEST COMPLETE]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**Phase 0 -- PRIOR ROUND LOAD**

If a prior-round scorecard is provided:
1. Read the file.
2. Build a BASELINE TABLE:

```
BASELINE TABLE (Round N-1):
| Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 |
|--------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| V-01   | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  | [v]  |
...
```

3. Note criteria with universal PARTIAL/FAIL.

If no prior-round scorecard:
Write: `No prior round data available -- C-08, C-13, C-14 will be scored PARTIAL.`

Write: `[PRIOR ROUND LOAD COMPLETE]`

---

**Phase 1 -- LOAD**

Read the rubric and all N output files. Write:
```
Criteria: [IDs and tiers]
Formula: [exact text]
Golden threshold: [condition]
N/A rules: [list, or "none"]
Outputs loaded: [V-XX list]
```

Write: `[LOAD COMPLETE]`

---

**Phase 2 -- ANALYST SCORING**

ANALYST role: for each output V-XX, write one prose-block section. One block per criterion:

```
### V-XX: [axis label]

**C-01 -- Per-criterion verdict matrix** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [structural property sentence]
[CHANGE: if verdict differs from BASELINE TABLE, write "CHANGE from [prior]: [reason]"]
NOTE: Formats vary. Every criterion-output cell must have a stated verdict.

**C-02 -- Evidence for every verdict** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference -- not a restatement]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: Criterion restatements never satisfy C-02.

**C-03 -- Composite score per output** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]

**C-04 -- Ranked leaderboard** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: Pointer to score table does NOT satisfy C-04.

**C-05 -- Failure patterns called out** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: Section must exist even when empty.

**C-06 -- Excellence signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]

**C-07 -- Per-output evidence notes** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: Narrative inside scoring block does NOT satisfy C-07. Named downstream phase required.

**C-08 -- Regression signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [reference to BASELINE TABLE, or "PARTIAL -- no prior round data available"]
*Why*: [mechanism sentence, or "N/A -- no prior data"]

**C-09 -- Anti-pattern anchor** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: Anchor must precede scoring instructions.

**C-10 -- Structural completion gate** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: Gate must cover all three synthesis sections.

**C-11 -- Mechanism prompting** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]

**C-12 -- Phase-separated narrative** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline]
NOTE: "After the table within the same section" does NOT qualify. Named phase with gate
token required. PARTIAL if narrative shares a phase heading with scoring blocks.

**C-13 -- Inline regression annotation** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline, or "N/A -- no prior data"]
NOTE: Inline CHANGE slots in each criterion block required. CHANGE MANIFEST phase then
extracts those slots so synthesis never re-reads BASELINE TABLE. PARTIAL when no prior data.

**C-14 -- Baseline load gate** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
[CHANGE: if verdict differs from baseline, or "N/A -- no prior data"]
NOTE: Gate before first scoring block required. PARTIAL when no prior data.
```

Score all N outputs, then write: `[ANALYST COMPLETE -- N outputs scored]`

---

**Phase 3 -- VERIFIER AUDIT**

VERIFIER role: audit `*Evidence*:` lines for criterion restatement only. Do not re-score.

For every RESTATED finding:
```
VERIFIER FLAG -- V-XX / C-NN:
RESTATED: "[text]"
REQUIRED: [what a specific reference looks like]
```

If none: `VERIFIER: V-XX -- all evidence cells specific.`

Write: `[VERIFIER COMPLETE]`

---

**Phase 4 -- CHANGE MANIFEST** *(new in V-03)*

Read every `[CHANGE: ...]` annotation written during ANALYST SCORING. For each entry where
a change was noted, extract it into the CHANGE MANIFEST:

```
CHANGE MANIFEST:
| Output | Criterion | Prior verdict | Current verdict | Reason |
|--------|-----------|--------------|----------------|--------|
[one row per CHANGE entry; NO CHANGE and absent entries omitted]
```

Rows where no CHANGE annotation was written (because the baseline matched) are not included.
If no CHANGE entries exist across all outputs: `CHANGE MANIFEST: No changes detected.`

Write: `[CHANGE MANIFEST COMPLETE]`

---

**Phase 5 -- SYNTHESIS**

Write a per-output narrative section first:

```
### Narrative: V-XX

[Two to four sentences. Reference at least one specific structural feature. If this output
appears in the CHANGE MANIFEST, explain the change direction and cause. Do not restate
verdict counts or copy table rows from the CHANGE MANIFEST -- explain the mechanism.]
```

Then write five synthesis sections. All are required.

**Composite Scores**
```
essential_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-01..C-05
recommended_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-06..C-07
aspirational_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-08..C-14
composite = (essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/7 * 70)
```
Show: `V-XX: E=X/5, R=X/2, A=X/7 -> composite = XX`

**Ranked Leaderboard**
Explicit ranked list, descending. Ties noted. Not a pointer to composite scores.

**Failure Patterns**
Criteria where no output earned PASS. If none: `No failure patterns -- all criteria earned
PASS in at least one output.`

**Excellence Signals**
Specific output-criterion pairs with structural outliers. Name output, criterion, feature.
If none: `No excellence signals identified in this scoring run.`

**Regression Signals**
Draw from the CHANGE MANIFEST above. List all rows where Current verdict < Prior verdict
(PASS->PARTIAL, PASS->FAIL, PARTIAL->FAIL). Do NOT re-read the BASELINE TABLE in this
section -- CHANGE MANIFEST is the only permitted data source.
If CHANGE MANIFEST is empty or shows no regressions: `No regressions detected -- all
verdicts held or improved from prior round.`
If no prior round data: `No prior round data -- regression analysis cannot be performed.`

Write: `[SYNTHESIS COMPLETE]`

---

**Phase 6 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write: `[WRITE COMPLETE]`

---

## V-04 -- Lifecycle emphasis + output format (G+H)

**Axes**: G + H -- NARRATIVE isolation phase + mandatory bidirectional CHANGE field
**Hypothesis**: V-01 (G) isolates per-output narratives in a dedicated NARRATIVE phase,
closing the C-12 gap where narratives can bleed into leaderboard or excellence signal entries.
V-02 (H) makes the CHANGE field mandatory, closing the C-13 tracking gap where conditional
CHANGE fields can be silently omitted for unchanged criteria. These two failure modes target
different structural layers: G enforces narrative placement across phase boundaries; H enforces
annotation completeness within the scoring block. They are independent -- a prompt can have
phase-isolated narratives and still have conditional CHANGE fields; a prompt can have mandatory
CHANGE fields and still conflate narratives into synthesis sections. The combination closes
both gaps without structural overlap. The remaining C-13 synthesis gap (Regression Signals
informally collecting annotations vs. reading BASELINE TABLE) is addressed by instruction but
not by architecture -- that remains the axis I contribution, reserved for V-05.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path (required for regression analysis; if unavailable, state
  "no prior round data" in Phase 0 and proceed)

**INERTIA PATTERN -- read before scoring anything**

The following is what a weak scorer produces. Do not produce output that resembles this.

```
WEAK SCORER EXAMPLE (do not produce this):

**C-02 -- Evidence for every verdict** | PASS
*Evidence*: The output provides evidence cells for each criterion.
*Why*: Evidence is present throughout.
[*Change*: field absent -- omitted because verdict matched baseline]

**C-07 -- Per-output evidence notes** | PASS
*Evidence*: Each output includes a narrative explanation inside the scoring block.
*Why*: The prose block covers mechanism and reasoning together.
[*Change*: field absent]

**C-12 -- Phase-separated narrative** | PASS
*Evidence*: Narrative appears after the verdict table in the same section.
*Why*: Placement after the table constitutes separation.
[*Change*: field absent]

[Regression Signals: Based on reviewing the baseline table again, V-03 regressed on C-07...]

[No Failure Patterns section]
[Leaderboard -- see composite scores above]
```

The inertia failures above:
1. **Criterion restatement**: "provides evidence cells" restates C-02.
2. **C-07/C-12 conflation**: Narrative inside scoring block fails both. The NARRATIVE phase
   gate makes this detectable by construction.
3. **Missing *Change*: fields (C-13 violation)**: "NO CHANGE" must appear even for unchanged
   criteria. Silent omission makes the CHANGE annotation look optional.
4. **Fresh baseline lookup in synthesis (C-13 violation)**: Regression Signals must draw
   from inline `*Change*:` fields, not re-read Phase 0 data.
5. **Missing required sections**: Failure Patterns and Leaderboard must be explicit.

Before each `*Evidence*:` line: check for restatement.
Before each `*Change*:` field: consult BASELINE TABLE and write "NO CHANGE" or
"CHANGE from [prior]: [reason]". This field is never optional.

---

**Phase manifest** -- complete in order, each phase closes with its EXIT TOKEN:

| Phase | EXIT TOKEN |
|-------|------------|
| PRIOR ROUND LOAD | `[PRIOR ROUND LOAD COMPLETE]` |
| LOAD | `[LOAD COMPLETE]` |
| ANALYST SCORING | `[ANALYST COMPLETE -- N outputs scored]` |
| VERIFIER AUDIT | `[VERIFIER COMPLETE]` |
| NARRATIVE | `[NARRATIVE COMPLETE]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**Phase 0 -- PRIOR ROUND LOAD**

If prior-round scorecard provided: read and build BASELINE TABLE (all outputs x C-01..C-14).
If not: write `No prior round data available -- C-08, C-13, C-14 will be scored PARTIAL.`

Write: `[PRIOR ROUND LOAD COMPLETE]`

---

**Phase 1 -- LOAD**

Read rubric and all N output files. Write:
```
Criteria: [IDs and tiers]
Formula: (essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/7 * 70)
Golden threshold: all 5 essentials PASS AND composite >= 80
N/A rules: C-08/C-13/C-14 PARTIAL when no prior data and explicitly stated
Outputs loaded: [V-XX list]
```

Write: `[LOAD COMPLETE]`

---

**Phase 2 -- ANALYST SCORING**

ANALYST role: for each output V-XX, one prose-block section. The `*Change*:` field is ALWAYS
REQUIRED -- write "NO CHANGE" or "CHANGE from [prior]: [reason]" for every block:

```
### V-XX: [axis label]

**C-01 -- Per-criterion verdict matrix** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [structural property sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always fill this field]
NOTE: Formats vary. Every criterion-output cell must have a stated verdict.

**C-02 -- Evidence for every verdict** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference -- not a restatement]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Criterion restatements never satisfy C-02.

**C-03 -- Composite score per output** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]

**C-04 -- Ranked leaderboard** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Pointer to score table does NOT satisfy C-04.

**C-05 -- Failure patterns called out** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Section must exist even when empty.

**C-06 -- Excellence signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]

**C-07 -- Per-output evidence notes** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Narrative inside scoring block does NOT satisfy C-07. NARRATIVE phase required.

**C-08 -- Regression signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [reference to BASELINE TABLE, or "PARTIAL -- no prior round data available"]
*Why*: [mechanism sentence, or "N/A -- no prior data"]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- or "N/A -- no prior data"]

**C-09 -- Anti-pattern anchor** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Anchor must precede scoring instructions.

**C-10 -- Structural completion gate** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Gate must cover all three synthesis sections.

**C-11 -- Mechanism prompting** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]

**C-12 -- Phase-separated narrative** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: NARRATIVE phase gate makes conflation structurally detectable. PARTIAL if narrative
shares a phase heading with scoring or is embedded in another synthesis section.

**C-13 -- Inline regression annotation** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- or "N/A -- no prior data"]
NOTE: Mandatory `*Change*:` in every block (not conditional) satisfies the inline slot
requirement. Synthesis collects these fields to build Regression Signals. PARTIAL when no
prior data.

**C-14 -- Baseline load gate** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- or "N/A -- no prior data"]
NOTE: Gate token before first scoring block required. PARTIAL when no prior data.
```

Score all N outputs, then write: `[ANALYST COMPLETE -- N outputs scored]`

---

**Phase 3 -- VERIFIER AUDIT**

VERIFIER role: audit `*Evidence*:` lines for criterion restatement only.

For every RESTATED finding:
```
VERIFIER FLAG -- V-XX / C-NN:
RESTATED: "[text]"
REQUIRED: [what a specific reference looks like]
```

If none: `VERIFIER: V-XX -- all evidence cells specific.`

Write: `[VERIFIER COMPLETE]`

---

**Phase 4 -- NARRATIVE** *(G axis)*

Write one narrative section per output. This phase contains ONLY per-output narratives.
No composite scores, no leaderboard rows, no synthesis content of any kind appears here.

```
### Narrative: V-XX

[Two to four sentences explaining why this output scored as it did. Reference at least one
specific structural feature. If any `*Change*:` entries for this output read "CHANGE from
[prior]", explain the change direction and cause. Do not restate verdict counts.]
```

Write one section per output. All narratives must appear in this phase. Do not write
per-output narratives in SYNTHESIS.

Write: `[NARRATIVE COMPLETE]`

---

**Phase 5 -- SYNTHESIS**

Write five synthesis sections. All are required. Do not write per-output narratives here.

**Composite Scores**
```
essential_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-01..C-05
recommended_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-06..C-07
aspirational_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-08..C-14
composite = (essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/7 * 70)
```
Show: `V-XX: E=X/5, R=X/2, A=X/7 -> composite = XX`

**Ranked Leaderboard**
Explicit ranked list, descending. Ties noted.

**Failure Patterns**
Criteria where no output earned PASS. If none: `No failure patterns -- all criteria earned
PASS in at least one output.`

**Excellence Signals**
Specific output-criterion pairs. Name output, criterion, structural feature.
If none: `No excellence signals identified in this scoring run.`

**Regression Signals**
Collect all `*Change*:` fields from ANALYST SCORING. List every criterion-output pair where
"CHANGE from [prior]" shows current verdict < prior verdict. Do not re-read BASELINE TABLE.
If no prior data: `No prior round data -- regression analysis cannot be performed.`
If no regressions: `No regressions detected -- all verdicts held or improved.`

Write: `[SYNTHESIS COMPLETE]`

---

**Phase 6 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write: `[WRITE COMPLETE]`

---

## V-05 -- All axes: NARRATIVE isolation + mandatory CHANGE + CHANGE MANIFEST (G+H+I)

**Axes**: G + H + I
**Hypothesis**: V-04 (G+H) closes C-12 (NARRATIVE phase isolation) and the C-13 field
completeness gap (mandatory CHANGE field). It leaves one C-13 gap open: Regression Signals
in SYNTHESIS must collect `*Change*:` fields informally from memory -- under late-context
pressure, this informal collection can miss entries or misread them, and the scorer may
silently fall back on re-reading BASELINE TABLE. V-03's CHANGE MANIFEST phase closes this
remaining gap: it is a dedicated extraction step between VERIFIER AUDIT and NARRATIVE that
builds a structured CHANGE table before synthesis begins. SYNTHESIS Regression Signals
draws from CHANGE MANIFEST with an explicit prohibition on BASELINE TABLE re-reads.

The three axes operate at three distinct structural layers with no overlap:
- **G** (NARRATIVE phase): enforces per-output narrative placement across phase boundaries
- **H** (mandatory `*Change*:` field): enforces annotation completeness within scoring blocks
- **I** (CHANGE MANIFEST): enforces synthesis draw-from-annotations rather than fresh lookup

V-05 closes all three C-12/C-13 structural gaps simultaneously. The expected cost is phase
count: V-05 adds two new phases (CHANGE MANIFEST, NARRATIVE) for a total of 8 phases.
Round 3 tests whether the structural completeness gain across C-12 and C-13 compounds
without introducing phase overhead that compresses the SYNTHESIS sections.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path (required for regression analysis; if unavailable, state
  "no prior round data" in Phase 0 and proceed)

**INERTIA PATTERN -- read before scoring anything**

The following is what a weak scorer produces. Do not produce output that resembles this.

```
WEAK SCORER EXAMPLE (do not produce this):

**C-02 -- Evidence for every verdict** | PASS
*Evidence*: The output provides evidence cells for each criterion.
*Why*: Evidence is present throughout.
[*Change*: field absent -- omitted for unchanged criteria]

**C-07 -- Per-output evidence notes** | PASS
*Evidence*: Each output includes a narrative explanation inside the scoring block.
*Why*: The prose block covers mechanism and reasoning together.
[*Change*: field absent]

**C-12 -- Phase-separated narrative** | PASS
*Evidence*: Narrative appears after the verdict table in the same section.
*Why*: Placement after the table constitutes separation.
[*Change*: field absent]

[No CHANGE MANIFEST phase -- inline CHANGE fields present but not extracted]

[Regression Signals: Based on reviewing the baseline table again, V-03 regressed on C-07...]

[No Failure Patterns section]
[Leaderboard -- see composite scores above]
```

The inertia failures above:
1. **Criterion restatement**: "provides evidence cells" restates C-02.
2. **C-07/C-12 conflation**: Narrative inside scoring block fails both. NARRATIVE phase gate
   makes this structurally detectable.
3. **Missing *Change*: fields (C-13 violation)**: "NO CHANGE" must appear even for unchanged
   criteria. Absent field cannot be distinguished from a missed comparison.
4. **No CHANGE MANIFEST phase (C-13 violation)**: Without the MANIFEST phase, synthesis must
   either re-scan scoring blocks under context pressure or fall back on re-reading BASELINE
   TABLE -- both violate C-13's constraint. MANIFEST is the architectural solution.
5. **Fresh baseline lookup in synthesis (C-13 violation)**: "Based on reviewing the baseline
   table again" is the exact path CHANGE MANIFEST eliminates. SYNTHESIS must draw from
   CHANGE MANIFEST only.
6. **Missing required sections**: Failure Patterns and Leaderboard must be explicit.

Before each `*Evidence*:` line: check for restatement. Before each `*Change*:` field:
consult BASELINE TABLE and write "NO CHANGE" or "CHANGE from [prior]: [reason]".
This field is never optional.

---

**Phase manifest** -- complete in order, each phase closes with its EXIT TOKEN:

| Phase | EXIT TOKEN |
|-------|------------|
| PRIOR ROUND LOAD | `[PRIOR ROUND LOAD COMPLETE]` |
| LOAD | `[LOAD COMPLETE]` |
| ANALYST SCORING | `[ANALYST COMPLETE -- N outputs scored]` |
| VERIFIER AUDIT | `[VERIFIER COMPLETE]` |
| CHANGE MANIFEST | `[CHANGE MANIFEST COMPLETE]` |
| NARRATIVE | `[NARRATIVE COMPLETE]` |
| SYNTHESIS | `[SYNTHESIS COMPLETE]` |
| WRITE | `[WRITE COMPLETE]` |

---

**Phase 0 -- PRIOR ROUND LOAD**

If prior-round scorecard provided: read and build BASELINE TABLE (all outputs x C-01..C-14):
```
BASELINE TABLE (Round N-1):
| Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 |
|--------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| V-01   |      |      |      |      |      |      |      |      |      |      |      |      |      |      |
...
```
Note criteria with universal PARTIAL/FAIL.

If no prior-round scorecard:
Write: `No prior round data available -- C-08, C-13, C-14 will be scored PARTIAL.`

Write: `[PRIOR ROUND LOAD COMPLETE]`

---

**Phase 1 -- LOAD**

Read the rubric and all N output files. Write:
```
Criteria: [IDs and tiers]
Formula: (essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/7 * 70)
Golden threshold: all 5 essentials PASS AND composite >= 80
N/A rules: C-08/C-13/C-14 PARTIAL when no prior data and explicitly stated
Outputs loaded: [V-XX list]
```

Write: `[LOAD COMPLETE]`

---

**Phase 2 -- ANALYST SCORING**

ANALYST role: for each output V-XX, write one prose-block section. The `*Change*:` field is
ALWAYS REQUIRED -- write "NO CHANGE" or "CHANGE from [prior]: [reason]" for every block:

```
### V-XX: [axis label]

**C-01 -- Per-criterion verdict matrix** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [structural property sentence]
*Change*: [NO CHANGE | CHANGE from [prior verdict]: [reason] -- always fill this field]
NOTE: Formats vary. Every criterion-output cell must have a stated verdict.

**C-02 -- Evidence for every verdict** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference -- not a restatement]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Criterion restatements never satisfy C-02.

**C-03 -- Composite score per output** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]

**C-04 -- Ranked leaderboard** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Pointer to score table does NOT satisfy C-04.

**C-05 -- Failure patterns called out** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Section must exist even when empty.

**C-06 -- Excellence signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]

**C-07 -- Per-output evidence notes** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Narrative inside scoring block does NOT satisfy C-07. A verdict note inside a
leaderboard row does NOT satisfy C-07. NARRATIVE phase is the only valid container.

**C-08 -- Regression signals** | [PASS / PARTIAL / FAIL]
*Evidence*: [reference to BASELINE TABLE, or "PARTIAL -- no prior round data available"]
*Why*: [mechanism sentence, or "N/A -- no prior data"]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- or "N/A -- no prior data"]
NOTE: PARTIAL when no prior round data and output explicitly states this.

**C-09 -- Anti-pattern anchor** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Anchor must precede scoring instructions.

**C-10 -- Structural completion gate** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: Gate must cover all three synthesis sections.

**C-11 -- Mechanism prompting** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]

**C-12 -- Phase-separated narrative** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- always required]
NOTE: NARRATIVE phase gate makes narrative-into-synthesis conflation structurally
detectable. CHANGE MANIFEST phase provides an additional boundary between scoring context
and NARRATIVE phase. PARTIAL if narrative shares a phase heading with any other content.

**C-13 -- Inline regression annotation** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- or "N/A -- no prior data"]
NOTE: Mandatory `*Change*:` in every block satisfies the inline slot requirement. CHANGE
MANIFEST phase extracts those fields so synthesis draws from MANIFEST only, never from
BASELINE TABLE. PARTIAL when no prior round data.

**C-14 -- Baseline load gate** | [PASS / PARTIAL / FAIL]
*Evidence*: [direct quote or specific structural reference]
*Why*: [mechanism sentence]
*Change*: [NO CHANGE | CHANGE from [prior]: [reason] -- or "N/A -- no prior data"]
NOTE: Gate before first scoring block required. PARTIAL when no prior data. FAIL when
prior data exists but gate is absent.
```

Score all N outputs, then write: `[ANALYST COMPLETE -- N outputs scored]`

---

**Phase 3 -- VERIFIER AUDIT**

VERIFIER role: audit `*Evidence*:` lines for criterion restatement only. Do not re-score.

For every RESTATED finding:
```
VERIFIER FLAG -- V-XX / C-NN:
RESTATED: "[text]"
REQUIRED: [what a specific reference looks like]
```

If none: `VERIFIER: V-XX -- all evidence cells specific.`

Write: `[VERIFIER COMPLETE]`

---

**Phase 4 -- CHANGE MANIFEST** *(I axis)*

Read every `*Change*:` field written during ANALYST SCORING. Extract all entries that contain
"CHANGE from" (entries reading "NO CHANGE" or "N/A -- no prior data" are omitted):

```
CHANGE MANIFEST:
| Output | Criterion | Prior verdict | Current verdict | Reason |
|--------|-----------|--------------|----------------|--------|
[one row per CHANGE entry]
```

If no CHANGE entries exist: `CHANGE MANIFEST: No changes detected -- all verdicts held.`

Write: `[CHANGE MANIFEST COMPLETE]`

---

**Phase 5 -- NARRATIVE** *(G axis)*

Write one narrative section per output. This phase contains ONLY per-output narratives.
No composite scores, leaderboard entries, failure pattern discussion, or synthesis content
of any kind appears in this phase.

```
### Narrative: V-XX

[Two to four sentences. Reference at least one specific structural feature -- a section
name, a field format, a phase token, a gate ID -- that drove the composite result. If this
output appears in the CHANGE MANIFEST, explain the change direction and cause. Do not
restate verdict counts or quote CHANGE MANIFEST rows -- explain the mechanism.]
```

Write one section per output. All narratives must appear in this phase.

Write: `[NARRATIVE COMPLETE]`

---

**Phase 6 -- SYNTHESIS**

Write five synthesis sections. All are required. Do not write per-output narratives here.

**Composite Scores**
```
essential_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-01..C-05
recommended_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-06..C-07
aspirational_pass = sum(PASS=1, PARTIAL=0.5, FAIL=0) for C-08..C-14
composite = (essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/7 * 70)
```
Show: `V-XX: E=X/5, R=X/2, A=X/7 -> composite = XX`

**Ranked Leaderboard**
Explicit ranked list, descending. Ties noted. Not a pointer to composite scores.

**Failure Patterns**
Criteria where no output earned PASS. If none: `No failure patterns -- all criteria earned
PASS in at least one output.`

**Excellence Signals**
Specific output-criterion pairs. Name output, criterion, structural feature.
If none: `No excellence signals identified in this scoring run.`

**Regression Signals**
Draw from the CHANGE MANIFEST above. List all rows where Current verdict < Prior verdict
(PASS->PARTIAL, PASS->FAIL, PARTIAL->FAIL). Do NOT re-read the BASELINE TABLE in this
section -- CHANGE MANIFEST is the only permitted data source for this section.
If CHANGE MANIFEST shows no regressions: `No regressions detected -- all verdicts held.`
If no prior round data: `No prior round data -- regression analysis cannot be performed.`

Write: `[SYNTHESIS COMPLETE]`

---

**Phase 7 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write: `[WRITE COMPLETE]`

---

## Axis summary

| Axis | Label | Criteria targeted | Mechanism | Gap closed |
|------|-------|-------------------|-----------|------------|
| G | NARRATIVE isolation phase | C-12 (hardening), C-07 (reliability) | Dedicated NARRATIVE phase with `[NARRATIVE COMPLETE]` gate; all per-output narratives isolated; per-output comments in leaderboard/excellence signal entries are structurally detectable as misplaced | C-12 baseline satisfies by placement; G satisfies by isolation |
| H | Mandatory bidirectional *Change*: field | C-13 (field completeness) | `*Change*:` required in every criterion block; "NO CHANGE" for unchanged criteria; conditional omission gap eliminated | C-13 baseline uses conditional CHANGE; H eliminates conditionality |
| I | CHANGE MANIFEST extraction phase | C-13 (synthesis) | Dedicated CHANGE MANIFEST phase between VERIFIER and NARRATIVE/SYNTHESIS; structured CHANGE table built before synthesis; explicit BASELINE TABLE lookup prohibition in Regression Signals | C-13 baseline Regression Signals informally collects or re-reads BASELINE TABLE; I eliminates fresh lookup by construction |

| Variation | Axes | New phases | Expected C-12 | Expected C-13 |
|-----------|------|-----------|---------------|---------------|
| V-01 | G | NARRATIVE | PASS (isolation gate) | PARTIAL (conditional CHANGE; informal synthesis collection) |
| V-02 | H | none | PARTIAL (SYNTHESIS placement only) | PASS (mandatory field; synthesis collects informally) |
| V-03 | I | CHANGE MANIFEST | PARTIAL (SYNTHESIS placement only) | PASS (MANIFEST eliminates fresh lookup) |
| V-04 | G+H | NARRATIVE | PASS (isolation gate) | PASS (mandatory field; informal synthesis collection) |
| V-05 | G+H+I | CHANGE MANIFEST + NARRATIVE | PASS (isolation gate) | PASS (mandatory field + MANIFEST extraction) |
