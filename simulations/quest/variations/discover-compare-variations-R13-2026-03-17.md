R13 variations written to `simulations/quest/variations/discover-compare-variations-R13-2026-03-17.md`.

---

## R13 design summary

**Pivot**: v11 adds C-30 and C-31 (/24 denominator). R12 V-01 (the v10 ceiling) scores C-30 PARTIAL under v11 — its two-branch routing re-states exec ordering alongside a standalone BODY ORDER. The fix is deviation-only routing.

| Var | Axis | C-30 | C-31 | C-28 | C-29 | Projected |
|-----|------|------|------|------|------|-----------|
| V-01 | v11 ceiling: BODY ORDER + deviation-only routing + positional | PASS | PASS | PASS | PASS | **100.00** |
| V-02 | C-30 PARTIAL probe: R12 V-01 body rescored (two-branch + positional) | PARTIAL | PASS | PASS | PASS | **99.79** |
| V-03 | C-31/C-28 cascade: deviation-only + name reference ("reverse BODY ORDER") | PASS | PARTIAL | PARTIAL | PASS | **99.58** |
| V-04 | R12 V-02 rescored (no BODY ORDER, C-30 not scored, C-31 PASS) | N/A | PASS | PARTIAL | PARTIAL | **99.57** |
| V-05 | Compound: BODY ORDER + two-branch + name refs on both branches | PARTIAL | PARTIAL | PARTIAL | PASS | **99.38** |

**Key structural changes per variation:**

- **V-01**: Remove exec branch from routing. Deviation-only: `Routing: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.`
- **V-02**: R12 V-01 body verbatim (two-branch positional routing + BODY ORDER). C-30 PARTIAL fires.
- **V-03**: BODY ORDER + deviation-only routing with name reference: `reverse BODY ORDER: DECISION MATRIX precedes RECOMMENDATION`. C-31/C-28 cascade from same name reference.
- **V-04**: R12 V-02 body (no BODY ORDER). C-30 not scored. Key question: does "not scored" exclude from denominator (/23) or zero-penalize (/24)?
- **V-05**: BODY ORDER + both branches use name refs: `follow BODY ORDER` / `reverse BODY ORDER`. Maximum-redundancy compound probe.
L | PASS | PARTIAL | PARTIAL | **99.38** |

---

**V-01** (ceiling): R12 V-01 body with one change -- exec branch removed from routing block. Routing block is now deviation-only: only the engineering/general branch is present. BODY ORDER is the sole specification for exec (recommendation-first by default). C-30 PASS: no exec branch to re-state alongside BODY ORDER. C-31 PASS: positional vocabulary in the single branch. C-28 PASS: isolated. C-29 PASS: unconditional. Expected: 24/24 = 100.00.

**V-02** (C-30 PARTIAL probe): R12 V-01 body verbatim, rescored against v11. Two-branch routing (exec + engineering) coexists with standalone BODY ORDER. Exec branch says "produce RECOMMENDATION first" -- a conditional re-statement of what BODY ORDER already declares unconditionally. C-30 PARTIAL: redundant exec branch. C-31 PASS: positional vocabulary. C-28 PASS (confirmed R12 V-01). C-29 PASS. Expected: 23.5/24 = 9.79 -> composite 99.79. Establishes v11 C-30 PARTIAL penalty = 0.21 composite points.

**V-03** (C-31/C-28 cascade): BODY ORDER present (C-29 PASS). Routing is deviation-only -- one branch only -- but uses name reference: "if REG = engineering or general, reverse BODY ORDER: DECISION MATRIX precedes RECOMMENDATION." C-30 PASS: deviation-only. C-31 PARTIAL: names BODY ORDER in the branch. C-28 PARTIAL: per R12 V-03 precedent, naming BODY ORDER in the routing block constitutes vocabulary-level coupling (lexical independence violated). C-28 PARTIAL + C-31 PARTIAL co-emerge from the same name reference. Expected: 23/24 = 9.58 -> composite 99.58.

**V-04** (R12 V-02 rescored): No standalone BODY ORDER. Full two-branch routing, positional vocabulary. C-30: not scored (no BODY ORDER; denominator = /23). C-31 PASS: positional. C-28 PARTIAL + C-29 PARTIAL (same as R12 V-02). From R12: 20 full aspirational passes + C-28 0.5 + C-29 0.5 = 21 out of 22. Now v11: +C-31 PASS = 22/23 = 9.565 -> composite 99.57. Discriminating question: does "not scored" exclude from the denominator (22/23) or count as zero (22/24)? If zero-penalized: 22/24 = 9.17 -> composite 99.17. Watch.

**V-05** (C-30+C-31 compound): BODY ORDER present. Two-branch routing with name references on both branches: "if REG = exec, follow BODY ORDER. If REG = engineering or general, reverse BODY ORDER." C-30 PARTIAL: exec branch present alongside BODY ORDER. C-31 PARTIAL: both branches name BODY ORDER. C-28 PARTIAL: name reference = vocab coupling (R12 V-03 precedent applies). C-29 PASS: standalone BODY ORDER is unconditional. All three affected criteria PARTIAL simultaneously. Expected: 22.5/24 = 9.38 -> composite 99.38. Establishes compound C-28+C-30+C-31 penalty.

---

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational | Composite | Golden |
|-----------|--------------|-----------------|-------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 24/24 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 23.5/24 = 9.79 | **99.79** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 23/24 = 9.58 | **99.58** | TBD |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 22/23 = 9.57 | **99.57** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 22.5/24 = 9.38 | **99.38** | TBD |

---

## V-01 -- v11 ceiling: BODY ORDER + deviation-only routing + positional vocabulary

**Axis**: Single-axis -- routing block trimmed to deviation-only (engineering/general branch only); BODY ORDER unchanged from R12 V-01; vocabulary stays positional
**Hypothesis**: BODY ORDER is unconditional standalone directive -> C-29 PASS. BODY ORDER and routing block are physically separate, lexically independent -> C-28 PASS. Routing block has only the engineering/general deviation branch; exec branch absent (BODY ORDER handles exec by default) -> C-30 PASS. Routing branch uses positional vocabulary only; BODY ORDER not named -> C-31 PASS. All 22 R12 criteria carry over at PASS. Aspirational: 24/24 = 10.00. Expected composite: 100.00. Establishes v11 ceiling.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.

---

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

---

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

---

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

LEDGER GATE:

```
REG:       [ ]
ANCHOR[0]: [ ]
FEAS-A:    [ ]
FEAS-B:    [ ]
INERT-A:   [ ]
INERT-B:   [ ]
RISK-A:    [ ]
RISK-B:    [ ]
COMP-A:    [ ]
COMP-B:    [ ]
```

**HALT -- do not proceed if any token is absent.** Produce missing token, return here, verify all pass.

---

Routing: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.

RECOMMENDATION:

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

DECISION MATRIX:

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or revise RECOMMENDATION above to Neither.

---

AMEND:

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`

```
Add-C ledger: FEAS-C [ ]  INERT-C [ ]  RISK-C [ ]  COMP-C [ ]
```
**HALT -- do not extend matrix if any Add-C token is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if ledger incomplete.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if ledger incomplete.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 -- R12 V-01 body rescored against v11: C-30 PARTIAL probe

**Axis**: Reference -- R12 V-01 body verbatim; rescored against v11 rubric (C-30 and C-31 scored, denominator /24)
**Hypothesis**: Standalone BODY ORDER present -> C-29 PASS. BODY ORDER and routing block physically separate, lexically independent -> C-28 PASS. Routing block has exec branch re-confirming "produce RECOMMENDATION first" alongside a standalone BODY ORDER that already declares the same thing unconditionally -> C-30 PARTIAL. Routing branches use positional vocabulary; BODY ORDER not named -> C-31 PASS. All 22 R12 criteria carry over at PASS. Aspirational: 23.5/24 = 9.79 -> composite 99.79. Establishes v11 C-30 PARTIAL penalty = 0.21 composite points vs V-01 ceiling.

If actual = 100.00: exec branch alongside BODY ORDER does not constitute redundancy for C-30 purposes -- the criterion requires stronger co-specification than mere presence of both. Revises C-30 threshold.
If actual = 99.79 (as projected): exec branch re-statement confirmed as C-30 PARTIAL.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.

---

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

---

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

---

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

LEDGER GATE:

```
REG:       [ ]
ANCHOR[0]: [ ]
FEAS-A:    [ ]
FEAS-B:    [ ]
INERT-A:   [ ]
INERT-B:   [ ]
RISK-A:    [ ]
RISK-B:    [ ]
COMP-A:    [ ]
COMP-B:    [ ]
```

**HALT -- do not proceed if any token is absent.** Produce missing token, return here, verify all pass.

---

Routing: if REG = exec, produce RECOMMENDATION first, then DECISION MATRIX.
If REG = engineering or general, produce DECISION MATRIX first, then RECOMMENDATION.

RECOMMENDATION:

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

DECISION MATRIX:

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or revise RECOMMENDATION above to Neither.

---

AMEND:

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`

```
Add-C ledger: FEAS-C [ ]  INERT-C [ ]  RISK-C [ ]  COMP-C [ ]
```
**HALT -- do not extend matrix if any Add-C token is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if ledger incomplete.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if ledger incomplete.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 -- C-31/C-28 cascade: BODY ORDER + deviation-only routing + name reference

**Axis**: Single-axis -- routing block is deviation-only (C-30 target: PASS); routing branch names BODY ORDER by label ("reverse BODY ORDER") rather than restating positional sequence independently (C-31 target: PARTIAL; C-28 cascade: PARTIAL)
**Hypothesis**: BODY ORDER present, unconditional -> C-29 PASS. Routing block deviation-only -> C-30 PASS. Routing branch uses "reverse BODY ORDER" name reference -> C-31 PARTIAL: at least one branch names the body-order directive by label. C-28 PARTIAL: per R12 V-03 precedent, a name reference in the routing block to the body-order directive constitutes vocabulary-level coupling even with physical separation -- lexical independence is the additional requirement that C-28 PASS demands. C-31 PARTIAL and C-28 PARTIAL co-emerge from the same structural choice. Expected: C-28 0.5 + C-29 1 + C-30 1 + C-31 0.5 = 23/24 = 9.58 -> composite 99.58.

Discriminating question: does "reverse BODY ORDER" trigger C-31 PARTIAL if the branch also restates the section sequence explicitly ("DECISION MATRIX precedes RECOMMENDATION")? The inline restatement provides positional vocabulary alongside the name reference. If actual C-31 = PASS despite name reference: positional restatement neutralizes the name reference; isolation is vocabulary-dominant not label-occurrence-dominant. Watch.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.

---

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

---

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

---

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

LEDGER GATE:

```
REG:       [ ]
ANCHOR[0]: [ ]
FEAS-A:    [ ]
FEAS-B:    [ ]
INERT-A:   [ ]
INERT-B:   [ ]
RISK-A:    [ ]
RISK-B:    [ ]
COMP-A:    [ ]
COMP-B:    [ ]
```

**HALT -- do not proceed if any token is absent.** Produce missing token, return here, verify all pass.

---

Routing: if REG = engineering or general, reverse BODY ORDER: DECISION MATRIX precedes RECOMMENDATION.

RECOMMENDATION:

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

DECISION MATRIX:

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or revise RECOMMENDATION above to Neither.

---

AMEND:

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`

```
Add-C ledger: FEAS-C [ ]  INERT-C [ ]  RISK-C [ ]  COMP-C [ ]
```
**HALT -- do not extend matrix if any Add-C token is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if ledger incomplete.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if ledger incomplete.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-04 -- R12 V-02 body rescored against v11: C-30 not scored, C-31 PASS

**Axis**: Reference -- R12 V-02 body verbatim (no BODY ORDER; two-branch routing; positional vocabulary); rescored against v11 rubric
**Hypothesis**: No standalone BODY ORDER -> C-30 not scored (denominator = /23). Two-branch routing with positional vocabulary -> C-31 PASS. C-28 PARTIAL + C-29 PARTIAL (same as R12 V-02, confirmed). From R12 baseline: 20 full aspirational passes (C-08 through C-27 excluding the two PARTIAL) + C-28 0.5 + C-29 0.5 = 21/22. Now v11: +C-31 PASS = 22 pass-weight; denominator adjusts to /23 (C-30 excluded). 22/23 = 9.565 -> composite 99.57. All essential and recommended pass.

Watch: denominator interpretation. If "not scored" means zero in a fixed /24 denominator rather than exclusion: 22/24 = 9.17 -> composite 99.17. Difference = 0.40. R13 scorecard will resolve which interpretation the rubric applies. This is the discriminating question for V-04.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

---

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

---

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

---

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

LEDGER GATE:

```
REG:       [ ]
ANCHOR[0]: [ ]
FEAS-A:    [ ]
FEAS-B:    [ ]
INERT-A:   [ ]
INERT-B:   [ ]
RISK-A:    [ ]
RISK-B:    [ ]
COMP-A:    [ ]
COMP-B:    [ ]
```

**HALT -- do not proceed if any token is absent.** Produce missing token, return here, verify all pass.

---

Routing: if REG = exec, produce RECOMMENDATION first, then DECISION MATRIX.
If REG = engineering or general, produce DECISION MATRIX first, then RECOMMENDATION.

RECOMMENDATION:

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

DECISION MATRIX:

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or revise RECOMMENDATION above to Neither.

---

AMEND:

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`

```
Add-C ledger: FEAS-C [ ]  INERT-C [ ]  RISK-C [ ]  COMP-C [ ]
```
**HALT -- do not extend matrix if any Add-C token is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if ledger incomplete.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if ledger incomplete.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-05 -- C-30+C-31 compound: BODY ORDER + two-branch routing + name references on both branches

**Axis**: Compound -- BODY ORDER present; routing block has two branches; both branches use name references to BODY ORDER ("follow BODY ORDER" / "reverse BODY ORDER")
**Hypothesis**: BODY ORDER present, unconditional -> C-29 PASS. Routing block exec branch alongside BODY ORDER -> C-30 PARTIAL. Both routing branches name BODY ORDER -> C-31 PARTIAL. Name reference in routing block -> C-28 PARTIAL (per R12 V-03 precedent). Three criteria PARTIAL simultaneously. Expected: 20 (base C-08..C-27 excl C-28) + C-28 0.5 + C-29 1.0 + C-30 0.5 + C-31 0.5 = 22.5/24 = 9.375 -> composite 99.38. Establishes compound C-28+C-30+C-31 penalty = 0.63 composite points vs V-01 ceiling.

Structural relationship: C-30 PARTIAL fires because exec branch is present alongside BODY ORDER. C-31 PARTIAL fires because branches name BODY ORDER. C-28 PARTIAL fires because C-31 PARTIAL implies name-reference coupling (per R12 V-03). These three co-emerge from the same structural choice. V-05 is the maximum-redundancy probe.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.

---

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

---

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

---

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

LEDGER GATE:

```
REG:       [ ]
ANCHOR[0]: [ ]
FEAS-A:    [ ]
FEAS-B:    [ ]
INERT-A:   [ ]
INERT-B:   [ ]
RISK-A:    [ ]
RISK-B:    [ ]
COMP-A:    [ ]
COMP-B:    [ ]
```

**HALT -- do not proceed if any token is absent.** Produce missing token, return here, verify all pass.

---

Routing: if REG = exec, follow BODY ORDER.
If REG = engineering or general, reverse BODY ORDER: DECISION MATRIX precedes RECOMMENDATION.

RECOMMENDATION:

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

DECISION MATRIX:

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or revise RECOMMENDATION above to Neither.

---

AMEND:

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`

```
Add-C ledger: FEAS-C [ ]  INERT-C [ ]  RISK-C [ ]  COMP-C [ ]
```
**HALT -- do not extend matrix if any Add-C token is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if ledger incomplete.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if ledger incomplete.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## Rubric coverage projection summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 bilateral dimensions | PASS | PASS | PASS | PASS | PASS |
| C-02 independent inertia | PASS | PASS | PASS | PASS | PASS |
| C-03 decision matrix | PASS | PASS | PASS | PASS | PASS |
| C-04 explicit recommendation | PASS | PASS | PASS | PASS | PASS |
| C-05 build/no-build gate | PASS | PASS | PASS | PASS | PASS |
| C-06 differentiated risk | PASS | PASS | PASS | PASS | PASS |
| C-07 actionable AMEND | PASS | PASS | PASS | PASS | PASS |
| C-08 Option 0 in matrix | PASS | PASS | PASS | PASS | PASS |
| C-09 audience register | PASS | PASS | PASS | PASS | PASS |
| C-10 token ledger | PASS | PASS | PASS | PASS | PASS |
| C-11 explicit exclusion rule | PASS | PASS | PASS | PASS | PASS |
| C-12 named anchor before analysis | PASS | PASS | PASS | PASS | PASS |
| C-13 verbatim anchor recall | PASS | PASS | PASS | PASS | PASS |
| C-14 failure class co-located | PASS | PASS | PASS | PASS | PASS |
| C-15 register before anchor | PASS | PASS | PASS | PASS | PASS |
| C-16 blocking ledger gate | PASS | PASS | PASS | PASS | PASS |
| C-17 output compressed | PASS | PASS | PASS | PASS | PASS |
| C-18 dual-polarity FAULT | PASS | PASS | PASS | PASS | PASS |
| C-19 AMEND self-contained | PASS | PASS | PASS | PASS | PASS |
| C-20 path-scoped TOKEN RECALL | PASS | PASS | PASS | PASS | PASS |
| C-21 FAULT propagates to AMEND | PASS | PASS | PASS | PASS | PASS |
| C-22 phase structure by token positioning | PASS | PASS | PASS | PASS | PASS |
| C-23 exec leads with recommendation | PASS | PASS | PASS | PASS | PASS |
| C-24 AMEND path sub-ledgers | PASS | PASS | PASS | PASS | PASS |
| C-25 register-gated routing block | PASS | PASS | PASS | PASS | PASS |
| C-26 body section order exec-safe | PASS | PASS | PASS | PASS | PASS |
| C-27 routing block within LEDGER GATE scope | PASS | PASS | PASS | PASS | PASS |
| C-28 body-order and routing-scope isolated | PASS | PASS | **PARTIAL** | **PARTIAL** | **PARTIAL** |
| C-29 body ordering stated as unconditional directive | PASS | PASS | PASS | **PARTIAL** | PASS |
| **C-30 routing block handles only deviation case** | **PASS** | **PARTIAL** | **PASS** | N/A | **PARTIAL** |
| **C-31 routing vocabulary positionally descriptive** | **PASS** | **PASS** | **PARTIAL** | **PASS** | **PARTIAL** |

### Key results to watch

**V-01 on C-30 and C-31 ceiling**: Deviation-only routing (engineering branch only) + positional vocabulary. The exec branch is absent -- BODY ORDER is the sole exec ordering mechanism. C-30 PASS requires only that the exec branch be absent; C-31 PASS requires only positional vocabulary. Both conditions satisfied by the same structural choice: remove the exec branch and do not name BODY ORDER. Confirms /24 ceiling at 100.00.

**V-02 on C-30 PARTIAL threshold**: Two-branch routing (exec + engineering) alongside a standalone BODY ORDER. The exec branch re-states "produce RECOMMENDATION first" -- the same ordering BODY ORDER already declares unconditionally. C-30 PARTIAL: the exec branch constitutes a second, conditional source of the same specification. Key question: is mere presence of an exec branch alongside BODY ORDER sufficient for C-30 PARTIAL, or does the branch content need to be semantically redundant? V-02 tests the former interpretation.

**V-03 on C-31 PARTIAL + C-28 cascade**: Deviation-only routing branch (engineering only) names BODY ORDER: "reverse BODY ORDER." The inline positional restatement ": DECISION MATRIX precedes RECOMMENDATION" follows the name reference. Does the positional codicil neutralize the name reference for C-31 purposes? If C-31 = PASS despite "reverse BODY ORDER": name references with immediate positional disambiguation are transparent. If C-31 = PARTIAL: the label occurrence is the trigger regardless of accompanying positional restatement.

**V-04 on C-30 denominator interpretation**: No BODY ORDER. C-30 "not scored." Does "not scored" mean: (a) criterion excluded, denominator = /23; or (b) criterion scores zero in fixed /24 denominator? Model (a): 22/23 = 9.57, composite 99.57. Model (b): 22/24 = 9.17, composite 99.17. Composite difference = 0.40. R13 scorecard will establish the canonical interpretation for future rounds.

**V-05 on C-28+C-30+C-31 compound cascade**: All three affected criteria PARTIAL simultaneously from the same structural root (naming BODY ORDER in a two-branch routing block). Total penalty vs V-01: C-28 PARTIAL (-0.21) + C-30 PARTIAL (-0.21) + C-31 PARTIAL (-0.21) = -0.63. Confirms whether the three penalties are strictly additive or whether compound co-emergence produces any interaction effect.
