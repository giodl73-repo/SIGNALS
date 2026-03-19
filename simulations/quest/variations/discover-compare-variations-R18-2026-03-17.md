**`discover-compare-variations-R18-2026-03-17.md` written.**

---

## R18 design summary

**Target criteria**: C-37 (HALT phrase uniformity across AMEND paths) and C-38 (routing branch pairs deviation marker + positional vocabulary in same line)

| Var | Axis | Key change | Projected |
|-----|------|-----------|-----------|
| V-01 | Baseline at /31 | R17 V-04 carry — uniform "any of the above" + `DEVIATION:` + "precedes" | **100.00** |
| V-02 | C-37 non-uniformity | Mix "any of the above" (Add-C, Override) + "any listed" (Weight) | **99.84 / 99.68** |
| V-03 | C-38 marker-only | `DEVIATION:` kept; "precedes" replaced with "engineer-first layout applies" | **99.68** |
| V-04 | C-38 "before" form | `DEVIATION: ... DECISION MATRIX before RECOMMENDATION` | **100.00** |
| V-05 | Form-neutrality carry | R17 V-05 verbatim — uniform "any listed" + `OVERRIDE:` + "precedes" | **100.00** |

**Three open discrimination questions for scoring:**

1. **V-01**: Does R17 V-04 satisfy both C-37 and C-38 under v16 without modification? Expected: yes (100.00).

2. **V-02**: What is the numeric weight of C-37 PARTIAL? The "any of the above" / "any listed" mix is C-35-valid on all paths but C-37-non-uniform. If PARTIAL = 0.5 → 99.84; if PARTIAL = 0 → 99.68.

3. **V-04**: Is "before" equivalent to "precedes" for C-38? Rubric lists both in its positional vocabulary set — expected PASS confirming vocabulary-neutrality.

**V-03** is the canonical marker-only probe: `DEVIATION:` present (C-36 PASS) but no positional vocabulary — C-38 FAIL. Establishes pairing is the mechanism, marker alone is insufficient.
ight uses "any listed token is absent"; Override uses "any of the above tokens is absent." C-35 PASS (all three use positional reference -- no token names inline). C-37: two distinct phrases used across three paths -- rubric specifies PARTIAL regardless of distribution (two-of-three uniform scores identically to three-of-three with two distinct phrases). C-38 unchanged from V-01 -- PASS. Primary probe for C-37 PARTIAL boundary and numeric weight. Expected: C-37 PARTIAL. Composite: **99.84** (PARTIAL = 0.5) or **99.68** (PARTIAL = 0). Establishes C-37 non-uniformity as a scorable distinct state above C-35 FAIL and below C-37 PASS.

**V-03** (single-axis C-38): routing branch retains DEVIATION: marker (C-36 PASS) but replaces positional ordering vocabulary with a non-positional outcome phrase: `DEVIATION: if REG = engineering or general, engineer-first layout applies.` C-36 PASS (marker present at branch-instruction level). C-38 FAIL (no "precedes"/"before"/"follows"/"after" positional vocabulary in branch line -- pairing absent). C-31 also affected: branch instruction lacks positional ordering vocabulary. AMEND HALTs unchanged (uniform "any of the above tokens is absent" -- C-35 PASS + C-37 PASS). All other 27 prior criteria carry. Denominator /31. Expected: 30/31 x 10 + 90 = **99.68**. Establishes that deviation marker alone is insufficient for C-38; positional vocabulary pairing is the mechanism.

**V-04** (C-38 vocabulary-form probe): routing branch uses "before" instead of "precedes": `DEVIATION: if REG = engineering or general, DECISION MATRIX before RECOMMENDATION.` C-38 rubric lists "precedes," "before," "follows," "after" as valid positional vocabulary. Both required elements coexist on same line: DEVIATION: (marker) + "before" (vocabulary). C-38 PASS expected. C-31: "before" is positional vocabulary -- PASS. C-36: DEVIATION: marker at branch line -- PASS. C-37: AMEND HALTs unchanged (uniform "any of the above tokens is absent") -- PASS. All 29 prior criteria carry. Denominator /31. Expected: 31/31 = **100.00**. Confirms C-38 is vocabulary-neutral within the rubric-listed set.

**V-05** (form-neutrality carry): R17 V-05 body verbatim. AMEND HALTs: "any listed token is absent" uniformly across all three paths -- C-37 PASS (uniform phrase, distinct from V-01's "any of the above" but identical within V-05). Routing: `OVERRIDE: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` -- C-38 PASS (OVERRIDE: marker + "precedes" vocabulary on same line). Tests that the two confirmed R17 form variants together satisfy both new v16 criteria without interaction effects. All 29 prior criteria carry. Denominator /31. Expected: 31/31 = **100.00**.

---

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational | Composite | Golden |
|-----------|--------------|-----------------|-------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 31/31 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 30.5/31 = 9.84 (PARTIAL=0.5) | **99.84** | No |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 30/31 = 9.68 | **99.68** | No |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 31/31 = 10.00 | **100.00** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 31/31 = 10.00 | **100.00** | TBD |

---

## V-01 -- Baseline carry at /31

**Axis**: Baseline (denominator change from /29 to /31)
**Hypothesis**: R17 V-04 body verbatim. Under v16, C-37 and C-38 are newly scored. C-37: AMEND paths use "any of the above tokens is absent" uniformly across all three -- identical phrase, C-37 PASS. C-38: routing branch is `DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` -- DEVIATION: is the deviation marker (C-36 PASS); "precedes" is positional vocabulary (C-31 PASS); both coexist on same line (C-38 PASS). All 29 prior criteria carry at PASS. Denominator /31. Expected: 31/31 = 100.00. Establishes R17 V-04 golden body satisfies v16 ceiling without modification.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.
Token: `BODY-ORDER-LAYER: active`

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

ROUTING: deviation from BODY ORDER only.
DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.

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
**HALT -- do not extend matrix if any of the above tokens is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if any of the above tokens is absent.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if any of the above tokens is absent.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 -- C-37 only: mixed positional forms across AMEND paths

**Axis**: Output format (single-axis -- HALT phrase non-uniformity)
**Hypothesis**: All three AMEND path HALTs use positional reference (C-35 PASS), but two distinct positional phrases appear across the three paths: Add-C and Override use "any of the above tokens is absent"; Weight uses "any listed token is absent." C-37 requires the identical phrase across all three paths -- not merely C-35-equivalent phrases. "any of the above tokens" and "any listed token" are each individually valid under C-35 (confirmed R17) but are non-uniform under C-37 when mixed in the same output. Rubric specifies PARTIAL is flat: two-of-three uniform (Add-C + Override share one phrase; Weight differs) scores identically to three-of-three with two distinct phrases. C-38 unchanged from V-01 (DEVIATION: + "precedes" on same line -- PASS). Primary C-37 PARTIAL probe. Expected: C-37 PARTIAL. Establishes non-uniformity as a distinct scored state.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.
Token: `BODY-ORDER-LAYER: active`

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

ROUTING: deviation from BODY ORDER only.
DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.

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
**HALT -- do not extend matrix if any of the above tokens is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if any listed token is absent.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if any of the above tokens is absent.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 -- C-38 only: deviation marker without positional vocabulary

**Axis**: Routing form (single-axis -- C-38 marker-only probe)
**Hypothesis**: The routing branch retains DEVIATION: at branch-instruction level (C-36 PASS) but replaces the positional ordering vocabulary with a non-positional outcome phrase: `DEVIATION: if REG = engineering or general, engineer-first layout applies.` C-36: DEVIATION: marker present at branch-instruction level -- PASS. C-38: requires BOTH the deviation marker AND positional vocabulary ("precedes," "before," "follows," "after") on the same line. "engineer-first layout applies" is an outcome description -- not a member of the rubric-listed positional vocabulary set. C-38 FAIL. C-31 also affected: branch instruction lacks positional ordering vocabulary -- FAIL. AMEND HALTs unchanged (uniform "any of the above tokens is absent" -- C-35 PASS + C-37 PASS). C-32 preserved (scope declaration unchanged). C-30 preserved (deviation-only). All other criteria carry. Denominator /31. Expected: 30/31 x 10 + 90 = 99.68. Establishes that marker alone is insufficient for C-38; the positional vocabulary pairing is the mechanism.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.
Token: `BODY-ORDER-LAYER: active`

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

ROUTING: deviation from BODY ORDER only.
DEVIATION: if REG = engineering or general, engineer-first layout applies.

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
**HALT -- do not extend matrix if any of the above tokens is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if any of the above tokens is absent.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if any of the above tokens is absent.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-04 -- C-38 vocabulary-form probe: "before" replaces "precedes"

**Axis**: Routing form (single-axis -- C-38 positional vocabulary form)
**Hypothesis**: The routing branch uses "before" instead of "precedes": `DEVIATION: if REG = engineering or general, DECISION MATRIX before RECOMMENDATION.` C-38 rubric lists "precedes," "before," "follows," "after" as valid positional vocabulary -- all four are equivalent. Both required elements coexist on same line: DEVIATION: (deviation marker, per C-36) + "before" (positional vocabulary, per C-31). C-38 PASS expected. C-31: "before" is positional vocabulary -- PASS. C-36: DEVIATION: marker at branch-instruction level -- PASS. C-37: AMEND HALTs unchanged (uniform "any of the above tokens is absent" across all three paths) -- C-37 PASS. C-32 preserved (scope declaration unchanged). C-30 preserved (deviation-only branch). All 29 prior criteria carry. Denominator /31. Expected: 31/31 = 100.00. Tests C-38 vocabulary-neutrality within the rubric-listed set; confirms "before" is equivalent to "precedes" for C-38.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.
Token: `BODY-ORDER-LAYER: active`

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

ROUTING: deviation from BODY ORDER only.
DEVIATION: if REG = engineering or general, DECISION MATRIX before RECOMMENDATION.

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
**HALT -- do not extend matrix if any of the above tokens is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if any of the above tokens is absent.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if any of the above tokens is absent.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-05 -- Form-neutrality carry: uniform "any listed token" + OVERRIDE:

**Axis**: Output format + routing form (combined form-neutrality carry)
**Hypothesis**: R17 V-05 body verbatim. Under v16, C-37 and C-38 are scored for the first time against this body. C-37: AMEND HALTs use "any listed token is absent" uniformly across all three paths (Add-C, Weight, Override) -- identical phrase within V-05, C-37 PASS. C-38: routing branch is `OVERRIDE: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` -- OVERRIDE: is the deviation marker (rubric-listed equivalent to DEVIATION:, C-36 PASS confirmed R17); "precedes" is positional vocabulary; both coexist on same line -- C-38 PASS. Tests that the two R17 form variants (OVERRIDE: and "any listed token") together satisfy both new v16 criteria without interaction effects. All 29 prior criteria carry at PASS. Denominator /31. Expected: 31/31 = 100.00. If actual < 100.00: one R17-confirmed equivalent form produces a non-equivalence under the new v16 criteria -- boundary narrower than specified.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.
Token: `BODY-ORDER-LAYER: active`

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

ROUTING: deviation from BODY ORDER only.
OVERRIDE: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.

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
**HALT -- do not extend matrix if any listed token is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if any listed token is absent.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if any listed token is absent.**

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
| C-10 token ledger cross-check | PASS | PASS | PASS | PASS | PASS |
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
| C-22 phase structure via tokens | PASS | PASS | PASS | PASS | PASS |
| C-23 exec leads with recommendation | PASS | PASS | PASS | PASS | PASS |
| C-24 AMEND path token enumeration | PASS | PASS | PASS | PASS | PASS |
| C-25 register-gated routing block | PASS | PASS | PASS | PASS | PASS |
| C-26 body section order exec-safe | PASS | PASS | PASS | PASS | PASS |
| C-27 routing block within LEDGER GATE scope | PASS | PASS | PASS | PASS | PASS |
| C-28 body-order and routing-scope isolated | PASS | PASS | PASS | PASS | PASS |
| C-29 BODY ORDER unconditional | PASS | PASS | PASS | PASS | PASS |
| C-30 routing handles only deviation | PASS | PASS | PASS | PASS | PASS |
| C-31 routing vocabulary positionally descriptive | PASS | PASS | FAIL | PASS | PASS |
| C-32 routing scope declared deviation-only | PASS | PASS | PASS | PASS | PASS |
| C-33 BODY-ORDER-LAYER token | PASS | PASS | PASS | PASS | PASS |
| C-34 AMEND enumeration in separable block | PASS | PASS | PASS | PASS | PASS |
| C-35 HALT uses positional reference | PASS | PASS | PASS | PASS | PASS |
| C-36 engineering branch carries deviation marker | PASS | PASS | PASS | PASS | PASS |
| **C-37 HALT phrase uniform across AMEND paths** | **PASS** | **PARTIAL** | **PASS** | **PASS** | **PASS** |
| **C-38 branch pairs deviation marker + positional vocabulary** | **PASS** | **PASS** | **FAIL** | **TBD** | **PASS** |

### Key results to watch

**V-01 on C-37 (uniform "any of the above tokens is absent")**: All three AMEND path HALTs use identical phrase. C-37 requires identity, not mere C-35-equivalence. Uniform single phrase = PASS. Expected: C-37 PASS. Establishes R17 golden body satisfies v16 ceiling.

**V-01 on C-38 (DEVIATION: + "precedes" on same line)**: Both required elements present in canonical form. Expected: C-38 PASS. Confirms canonical form satisfies C-38.

**V-02 on C-37 (mixed "any of the above" and "any listed")**: Two distinct C-35-valid positional phrases across three AMEND paths. C-35 PASS (all positional). C-37: mixed = PARTIAL. The rubric's PARTIAL band is flat -- two-of-three matching does not produce a higher sub-grade than all-three with two distinct phrases. Primary C-37 PARTIAL boundary probe. Numeric weight of PARTIAL (0.5 vs 0) is the open discrimination question.

**V-03 on C-38 (marker without positional vocabulary)**: `DEVIATION: if REG = engineering or general, engineer-first layout applies.` DEVIATION: present (C-36 PASS). No positional vocabulary (C-38 FAIL + C-31 FAIL). Establishes that C-36 PASS is necessary but not sufficient for C-38. Pairing is the mechanism.

**V-04 on C-38 ("before" vocabulary)**: `DEVIATION: if REG = engineering or general, DECISION MATRIX before RECOMMENDATION.` Rubric lists "before" alongside "precedes" as valid. Both elements present on same line. Expected: C-38 PASS. Confirms vocabulary-neutrality within the rubric-listed set for C-38.

**V-05 on C-37 (uniform "any listed token is absent")**: Uniform within V-05 but distinct phrase from V-01. C-37 requires identity across paths within an output, not across outputs. V-05 is internally uniform -- C-37 PASS. Expected: C-37 PASS. Confirms that any uniform C-35-valid phrase satisfies C-37.

**V-05 on C-38 (OVERRIDE: + "precedes")**: OVERRIDE: confirmed equivalent to DEVIATION: under C-36 (R17). "precedes" is canonical positional vocabulary. Both on same line. Expected: C-38 PASS. Tests that R17's confirmed OVERRIDE: form also satisfies C-38 (pairing criterion, first scored in R18).
