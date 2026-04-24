Scorecard written to `simulations/quest/scorecards/review-customers-scorecard-R1-2026-03-14.md`.

---

## review-customers R1 Results

**Scores:**

| Variation | Score | Result |
|-----------|-------|--------|
| V-01 Baseline | 80/100 | C-09 FAIL, C-10 FAIL |
| V-02 Table-first | 95/100 | C-08 PARTIAL |
| V-03 Phases | 100/100 | All pass |
| V-04 Conversational | 100/100 | All pass |
| V-05 Combined | 100/100 | All pass |

**Key finding**: The essential floor is already solid across all 5 variations. Every variation passes C-01 through C-05, including both "none" statement requirements (C-03/C-04). The baseline hypothesis that V-01 would fail essentials was incorrect — the inline instructions are sufficient.

The ceiling is determined entirely by C-09 (pattern synthesis) and C-10 (amend projection). V-01 misses both because neither is prompted. V-02 through V-05 all prompt them, so all four score 95+.

**Top variation**: V-05 by tie-break — inline `[BLOCKER]`/`[LEAK]` flags during scoring and composite-anchored C-10 projection are the strongest mechanisms for reliability and auditability. Recommended as the working prompt.

**New patterns for R2:**
- Inline flagging during scoring outperforms post-hoc DETECT phases for C-03/C-04 reliability
- Table-first creates a completeness/depth trade-off on C-08 — hybrid format could recover both
- V-04's reaction-explanation framing ("explain what produced these specific reactions") is more precise than V-03's anti-restate instruction — worth isolating as an axis

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inline-flags-outperform-posthoc-detection", "table-format-creates-completeness-depth-tradeoff", "reaction-explanation-framing-stronger-than-anti-restate-for-C08"]}
```
) and
meets the pass condition.

**Failures confirmed by hypothesis:**
- **C-09 FAIL**: No cross-persona pattern synthesis instruction anywhere. The model has no signal to
  produce named patterns with implications.
- **C-10 FAIL**: AMEND asks "what changes would raise would-adopt" but contains no delta projection
  language. A model following V-01 gives remediation guidance without score estimates.

**Verdict**: Solid essential coverage, no aspirational reach. The baseline hypothesis holds exactly.

---

### V-02 -- 95/100

**Table-first format.** The 12-row table built before any findings prose is the strongest structural
guarantee for C-01 completeness and C-05 tier visibility -- it is structurally impossible to skip a
persona or omit a tier label before the findings sections are reached.

**C-08 PARTIAL**: The table constraint explicitly limits rationale to "1 sentence" per row. The rubric
pass condition requires non-trivial rationale for at least 10 of 12 personas. A single grounded
sentence is non-trivial, but the format cap prevents the depth available in prose formats. This is
the table's core trade-off: completeness and auditability in exchange for rationale depth.

**Strong coverage on C-09 and C-10**: The "CROSS-PERSONA PATTERNS" section requires at least one
named pattern with implication. AMEND projection language ("likely lifts primary weighted W-Adopt
by ~[delta]") is present and explicit.

**Verdict**: Best completeness guarantee; one recoverable weakness on rationale depth. R2 should
test a hybrid -- full table for scores + tier labels, prose block for rationale.

---

### V-03 -- 100/100

**Explicit lifecycle phases.** All 10 criteria pass. The phase gate architecture is the key
differentiator:

- **C-03/C-04 reliability**: DETECT is a mandatory phase with "Each check requires an explicit
  result. Blank or omitted = fail." This is structurally stronger than inline "if none, state X"
  instructions -- the model must enter the phase and explicitly complete each check before proceeding.
- **C-08 depth**: "1-2 sentence rationale grounded in this persona's role, typical workflow, or
  known pain points -- not a restatement of the score" is the clearest anti-template instruction
  across all variations.
- **C-09 quality**: "Generic observations ('scores vary') do not qualify" explicitly disqualifies
  the most common LLM failure mode for pattern synthesis.
- **C-10**: Delta projection per blocker required in AMEND phase.

**Verdict**: Strongest structural enforcement for C-03/C-04. The "blank or omitted = fail" language
makes the "none" statement requirement machine-enforceable rather than model-inferred.

---

### V-04 -- 100/100

**Conversational register.** All 10 criteria pass. Despite the least prescriptive format, every
criterion is explicitly addressed in natural language.

**Strongest instructions per criterion:**
- **C-08**: "Do not restate the numbers -- explain what about the feature (or the gap in it) produced
  these specific reactions from this specific person." The reaction-explanation framing is the most
  specific rationale-depth instruction of all five variations.
- **C-10**: Provides a worked example -- "fixing this would likely lift the primary would-adopt
  average by about 0.4" -- anchoring the model's behavior more concretely than requesting a delta
  without an example.
- **C-03/C-04**: "Do not skip the check. A clean result still needs to be stated." Explicit negative
  reinforcement.

**Trade-off**: Conversational framing means no phase gates and no table structure. The model must
follow ordering through prose instruction alone, which is less structurally enforced than V-03 or
V-05. C-07 passes because the ordering is unambiguous ("address those first... Then... Then"), but
section blending is more likely under this format.

**Verdict**: Highest predicted C-08 rationale quality. Weakest structural enforcement. Best choice
when rich persona reasoning is the primary goal over process compliance.

---

### V-05 -- 100/100

**Combined (tier-first + phases + projection).** All 10 criteria pass. Strongest combined coverage
across criteria requiring both structural completeness and behavioral depth.

**Unique mechanisms:**
- **C-03/C-04 reliability (strongest)**: Inline `[BLOCKER]` and `[LEAK]` flags appended during
  scoring (Phases 2 and 4) mean DETECT becomes a verification pass over already-flagged entries
  rather than a first-pass discovery scan. The model is less likely to miss a blocker or leak
  because it was forced to notice it during scoring.
- **C-10 precision (strongest)**: "'Resolving [ID] blocker likely lifts primary Would-Adopt by
  ~[delta], moving weighted composite from [current] to approximately [current + effect].'" The only
  variation that requests both the current score and post-fix score, making the projection anchored
  rather than directional.
- **C-10 auto-pass encoding**: Explicitly states "(C-10 auto-passes when both blockers and leaks
  are absent -- the score is clean by definition)" -- the only variation that encodes the rubric's
  waiver logic directly in the prompt.
- **Phase sequencing**: Primary-first scoring makes adoption blockers visible before secondary and
  non-target data can dilute the signal.

**Trade-off**: 7-phase structure is the most complex prompt. More phases = more opportunities for
the model to abbreviate later phases. Mitigated by explicit "Do not proceed" gates at every boundary.

**Verdict**: Highest ceiling on C-03/C-04 reliability and C-10 precision. Most likely to produce
the most actionable and auditable output. Recommended as the working version going into R2.

---

## Rankings

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|--------------------|
| 1 | V-05 Combined | 100 | Inline flags + strongest C-10 projection + auto-pass logic |
| 1 | V-03 Phases | 100 | "Blank or omitted = fail" enforcement + anti-generic C-09 rule |
| 1 | V-04 Conversational | 100 | Richest C-08 rationale instruction + worked C-10 example |
| 4 | V-02 Table-first | 95 | Strongest C-01/C-05 completeness guarantee; C-08 depth trade-off |
| 5 | V-01 Baseline | 80 | Clean essential coverage; no aspirational reach |

**Tie-breaking observation**: V-05 edges out V-03 on C-10 precision (composite delta vs. dimension
delta only) and C-03/C-04 reliability (inline flags during scoring vs. phase-gate enforcement
after scoring). V-04 is highest on C-08 rationale depth but has the weakest structural enforcement
overall. For production use, V-05 is the recommended working prompt.

---

## Essential Criterion Pass Analysis

All 5 variations pass all 5 essential criteria (C-01 through C-05). The "none" statement requirement
for C-03 and C-04 is explicitly encoded in every variation. The original hypothesis that V-01 might
fail essentials was not borne out -- V-01's inline "State: 'No adoption blockers.'" and "State: 'No
positioning leaks.'" instructions do satisfy the essential pass conditions.

**Implication for R2**: The essential floor is already solid. R2 focus areas:
1. Resolve the V-02 C-08 depth trade-off (test hybrid: table for scores, prose block for rationale)
2. Test whether V-04's reaction-explanation framing produces measurably richer C-08 output vs.
   V-03's anti-restate instruction on a live topic run
3. Isolate inline-flag mechanism (V-05) as a standalone axis to confirm it outperforms phase-gate
   DETECT (V-03) on C-03/C-04 reliability

---

## Excellence Signals (from top scoring variations)

1. **Inline flags during scoring** ([BLOCKER]/[LEAK] appended at the point of evaluation) are a
   more reliable mechanism for C-03/C-04 than post-hoc section scanning -- the finding is surfaced
   in-situ, not reconstructed from memory during a separate phase.

2. **Score-anchored projection** ("from [current] to approximately [current + effect]") makes C-10
   auditable rather than directional. Including the current composite score in the projection gives
   the reader a concrete improvement target.

3. **Explicit auto-pass encoding** (the rubric's waiver logic stated directly in the prompt) prevents
   hallucinated deltas on clean runs -- the model knows not to fabricate a projection when no
   blockers or leaks exist.

4. **"Blank or omitted = fail" enforcement** at phase boundaries is stronger than conditional inline
   instructions -- it reframes omission as an error rather than an acceptable outcome.

5. **Anti-generic qualification rule** for C-09 ("Generic observations ('scores vary') do not
   qualify") is a binary disqualifier that prevents the most common pattern-synthesis failure mode.

6. **Reaction-explanation framing** for C-08 ("explain what about the feature... produced these
   specific reactions from this specific person") elicits persona-grounded reasoning rather than
   score commentary.

---

## New Patterns

1. **Completeness vs. depth trade-off in table formats**: Table-first structure (V-02) guarantees
   C-01/C-05 but creates a C-08 depth ceiling. A hybrid -- full table for scores + tier, prose block
   for rationale -- could recover both. Test in R2.

2. **In-situ flagging outperforms post-hoc detection**: Inline [BLOCKER]/[LEAK] flags during scoring
   (V-05) vs. phase-gate DETECT (V-03) vs. inline conditional instructions (V-01/V-02/V-04). V-05's
   approach makes detection passive (happens during scoring) rather than active (requires a separate
   check).

3. **Anti-template language for rationale depth**: V-04's "Do not restate the numbers" and V-03's
   "not a restatement of the score" target the same failure mode. V-04's instruction is more
   specific ("explain what about the feature... produced these specific reactions"). Worth testing
   whether specificity produces measurably different C-08 output.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inline-flags-outperform-posthoc-detection", "table-format-creates-completeness-depth-tradeoff", "reaction-explanation-framing-stronger-than-anti-restate-for-C08"]}
```
