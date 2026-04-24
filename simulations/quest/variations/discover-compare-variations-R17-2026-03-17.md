`discover-compare-variations-R17-2026-03-17.md` written.

---

## R17 design summary

**Three single-axis, two combined — targeting v15's two new criteria:**

| Var | Axis | Change | Projected |
|-----|------|--------|-----------|
| V-01 | Baseline carry at /29 | R16 V-01 unchanged | 99.31 |
| V-02 | Output format (C-35 only) | AMEND HALTs → "any of the above tokens is absent" | 99.66 |
| V-03 | Routing form (C-36 only) | `DEVIATION:` prefix on engineering branch | 99.66 |
| V-04 | Combined (C-35 + C-36) | Both changes — primary golden candidate | 100.00 |
| V-05 | Combined form variant | "any listed token" + `OVERRIDE:` — form-neutrality probe | 100.00 |

**What changed and why:**

**V-01** carries the R16 V-01 body verbatim. Under v15, both new criteria fire: the AMEND HALTs use category references ("any Add-C token is absent," "ledger incomplete") not positional references, and the routing branch has no deviation marker. Expected: C-35 FAIL + C-36 FAIL = 27/29 = **99.31**. Establishes the actual v15 gap above R16 ceiling.

**V-02** (single-axis C-35): changes all three AMEND path HALTs to `"any of the above tokens is absent"`. The fenced-code enumeration block is unchanged — the HALT now links to it via the positional anchor "above" rather than naming a category. Primary probe for C-35 mechanism.

**V-03** (single-axis C-36): adds `DEVIATION:` as a prefix to the engineering routing branch. C-31 preserved ("precedes" is the positional vocabulary; DEVIATION: is a role label). C-32 preserved (scope declaration unchanged). C-30 preserved (no exec branch added). Primary probe for C-36 orthogonality claims.

**V-04** (combined): V-03 + C-35 additions. Both changes applied. No structural overlap — AMEND changes and routing changes are independent mechanisms. Should produce 29/29 = **100.00**.

**V-05** (form-neutrality): V-04 with `"any listed token is absent"` (vs "any of the above") and `OVERRIDE:` (vs `DEVIATION:`). Tests whether the rubric's stated equivalent forms actually score equivalently.
non-interfering and that C-35 + C-36 are the sole gap between R16 ceiling and v15 ceiling.

5. **V-05 on C-35/C-36 form-neutrality**: Does "any listed token is absent" satisfy C-35 (vs "any of the above")? Does OVERRIDE: satisfy C-36 (vs DEVIATION:)? Rubric cites both as explicitly equivalent forms. Expected: 29/29 = 100.00. If actual = 28/29: one alternative form fails, establishing a narrower boundary for that criterion.

---

**V-01** (baseline carry at /29): R16 V-01 body verbatim. Under v15, C-35 is a new scored criterion when C-34 PASS. C-35: all three AMEND path HALTs use category or completeness reference ("any Add-C token is absent," "ledger incomplete") rather than positional reference ("any of the above," "any listed"). C-35 FAIL. C-36: engineering routing branch uses `if REG = engineering or general,` with no deviation marker label. C-36 FAIL. All 27 prior criteria carry at PASS. Denominator /29. Expected: 27/29 x 10 + 90 = 9.31 + 90 = 99.31. Establishes v15 gap: R16 golden ceiling is 99.31 under v15 scoring.

**V-02** (C-35 addition only): R16 V-01 body with all three AMEND path HALT instructions updated to positional reference form. Add-C: "any of the above tokens is absent." Weight: "any of the above tokens is absent." Override: "any of the above tokens is absent." C-34 unchanged (fenced-code block still present and separable). C-35: each HALT uses "above" as positional anchor, no token names inline. Expected: C-35 PASS. C-36: routing branch unchanged -- no marker. Expected: C-36 FAIL. All 27 prior criteria carry. Denominator /29. Expected: 28/29 x 10 + 90 = 9.655 + 90 = 99.66. Establishes C-35 as independently achievable.

**V-03** (C-36 addition only): R16 V-01 body with engineering routing branch prefixed by DEVIATION: marker. Routing block becomes: `ROUTING: deviation from BODY ORDER only. / DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` C-31 PASS preserved: "precedes" is positional vocabulary; "DEVIATION:" is a role label, not a structural layer reference. C-32 PASS preserved: scope declaration header unchanged. C-30 PASS preserved: no exec branch added. C-36: deviation marker present at branch-instruction level. Expected: C-36 PASS. C-35: AMEND HALTs unchanged -- no positional reference. Expected: C-35 FAIL. All 27 prior criteria carry. Denominator /29. Expected: 28/29 x 10 + 90 = 99.66. Establishes C-36 as independently achievable.

**V-04** (combined -- C-35 + C-36, primary golden candidate): V-03 body with C-35 additions applied. All three AMEND path HALTs updated to "any of the above tokens is absent." Engineering branch carries DEVIATION: marker. C-35 PASS + C-36 PASS + all 27 prior criteria carry. Denominator /29. Expected: 29/29 x 10 + 90 = 100.00. Primary golden candidate for v15. Confirms C-35 and C-36 are the complete delta between R16 and v15 ceilings.

**V-05** (combined form variant -- "any listed token" + OVERRIDE:): V-04 body with alternative phrasings at both new criteria. AMEND HALTs: "any listed token is absent" replaces "any of the above tokens is absent." Engineering branch: OVERRIDE: replaces DEVIATION:. Tests C-35 form-neutrality (rubric cites "any listed token is missing" as equivalent to "any of the above") and C-36 marker-label neutrality (rubric lists OVERRIDE: as equivalent to DEVIATION:). Expected: 29/29 = 100.00. If actual = 28/29: one alternative form is narrower than rubric specifies.

---

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational | Composite | Golden |
|-----------|--------------|-----------------|-------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 27/29 = 9.31 | **99.31** | No |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 28/29 = 9.66 | **99.66** | No |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 28/29 = 9.66 | **99.66** | No |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 29/29 = 10.00 | **100.00** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 29/29 = 10.00 | **100.00** | TBD |

---

## V-01 -- Baseline carry at /29

**Axis**: Baseline (single-axis -- denominator change only)
**Hypothesis**: R16 V-01 body is unchanged. Under v15, two new criteria are scored: C-35 (HALT uses positional reference) and C-36 (engineering branch carries deviation marker). C-35: the AMEND HALTs use "any Add-C token is absent" and "ledger incomplete" -- category and completeness references, not positional references to the preceding enumeration block. C-35 FAIL. C-36: the routing branch reads `if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` with no DEVIATION:/OVERRIDE:/EXCEPTION: prefix. C-36 FAIL. All 27 prior criteria carry at PASS. Denominator /29. Expected: 27/29 = 99.31. Establishes that the R16 golden body does not satisfy the v15 ceiling.

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
if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.

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

## V-02 -- Output format: positional reference HALT (C-35 only)

**Axis**: Output format (single-axis)
**Hypothesis**: All three AMEND path HALT instructions updated to positional reference form. Add-C HALT: "any of the above tokens is absent" replaces "any Add-C token is absent." Weight HALT: "any of the above tokens is absent" replaces "ledger incomplete." Override HALT: "any of the above tokens is absent" replaces "ledger incomplete." The phrase "any of the above tokens" uses "above" as positional anchor explicitly linking the HALT to the preceding fenced-code enumeration block. C-34 unchanged: fenced-code blocks still present and separable -- HALT does not name tokens inline. C-35: each HALT uses positional reference with no inline token names. Expected: C-35 PASS. C-36: routing branch unchanged -- no DEVIATION: marker. Expected: C-36 FAIL. All 27 prior criteria carry. Denominator /29. Expected: 28/29 = 99.66. Establishes C-35 as independently achievable; confirms "above" positional anchor satisfies the positional-reference requirement.

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
if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.

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

## V-03 -- Routing form: DEVIATION: marker on engineering branch (C-36 only)

**Axis**: Routing form (single-axis)
**Hypothesis**: Engineering routing branch prefixed with DEVIATION: marker. Current form: `if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` New form: `DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` The marker identifies the branch as a structural deviation from body-order default at branch-instruction level. C-31 PASS preserved: "precedes" remains the positional vocabulary; "DEVIATION:" is a role label, not a structural layer reference. C-32 PASS preserved: scope declaration "ROUTING: deviation from BODY ORDER only." is unchanged. C-30 PASS preserved: routing block still handles only the engineering deviation case. C-36: named deviation marker present on engineering branch instruction. Expected: C-36 PASS. C-35: AMEND HALTs unchanged -- "any Add-C token is absent" / "ledger incomplete." Expected: C-35 FAIL. All 27 prior criteria carry. Denominator /29. Expected: 28/29 = 99.66. Establishes C-36 as independently achievable; confirms DEVIATION: orthogonality with C-31 and C-32.

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

## V-04 -- Combined: positional reference HALT + DEVIATION: marker (C-35 + C-36)

**Axis**: Output format + routing form (combined)
**Hypothesis**: V-03 body with C-35 additions applied. All three AMEND path HALTs updated to "any of the above tokens is absent." Engineering branch carries DEVIATION: marker. C-35 PASS: each HALT uses "above" as positional anchor, no token names inline, enumeration block independently revisable. C-36 PASS: DEVIATION: marker at branch-instruction level, orthogonal to C-31 positional vocabulary and C-32 scope declaration. All 27 prior criteria carry. Denominator /29. Expected: 29/29 x 10 + 90 = 100.00. Primary golden candidate for v15. Confirms C-35 and C-36 are the complete and sufficient delta between R16 golden ceiling and v15 ceiling.

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

## V-05 -- Combined form variant: "any listed token" + OVERRIDE:

**Axis**: Output format + routing form (combined form variant)
**Hypothesis**: V-04 body with alternative phrasings at both new criteria. AMEND HALTs: "any listed token is absent" replaces "any of the above tokens is absent." Engineering branch: OVERRIDE: replaces DEVIATION:. Tests C-35 form-neutrality: rubric cites "do not proceed if any listed token is missing" as equivalent to "any of the above" -- both use a positional anchor ("listed" refers to the preceding enumeration list; "above" refers to its position). Tests C-36 marker-label neutrality: rubric explicitly lists OVERRIDE: as equivalent to DEVIATION:. If both forms satisfy their respective criteria: 29/29 = 100.00 -- confirms rubric form-neutrality claims. If one form produces PARTIAL or FAIL: boundary for that criterion is narrower than specified, establishing a watch-list entry for R18.

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
| C-24 AMEND path token enumeration (any form) | PASS | PASS | PASS | PASS | PASS |
| C-25 register-gated routing block | PASS | PASS | PASS | PASS | PASS |
| C-26 body section order exec-safe | PASS | PASS | PASS | PASS | PASS |
| C-27 routing block within LEDGER GATE scope | PASS | PASS | PASS | PASS | PASS |
| C-28 body-order and routing-scope isolated | PASS | PASS | PASS | PASS | PASS |
| C-29 BODY ORDER as unconditional directive | PASS | PASS | PASS | PASS | PASS |
| C-30 routing handles only deviation | PASS | PASS | PASS | PASS | PASS |
| C-31 routing vocabulary positionally descriptive | PASS | PASS | PASS | PASS | PASS |
| C-32 routing scope declared as deviation-only | PASS | PASS | PASS | PASS | PASS |
| C-33 BODY-ORDER-LAYER token | PASS | PASS | PASS | PASS | PASS |
| C-34 AMEND enumeration in separable block form | PASS | PASS | PASS | PASS | PASS |
| **C-35 HALT uses positional reference to block** | **FAIL** | **TBD** | **FAIL** | **TBD** | **TBD** |
| **C-36 engineering branch carries deviation marker** | **FAIL** | **FAIL** | **TBD** | **TBD** | **TBD** |

### Key results to watch

**V-01 on C-35 (category reference)**: "any Add-C token is absent" names a token category. "ledger incomplete" names a completion state. Neither uses a positional anchor ("above," "listed") to link the HALT to the preceding enumeration block. Expected: C-35 FAIL for all three AMEND paths. Confirms the R16 golden body does not satisfy C-35 under v15.

**V-01 on C-36 (no marker)**: `if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` -- branch role is legible only from the C-32 scope header, not from the branch instruction itself. Expected: C-36 FAIL. Confirms that C-32 scope-level declaration is necessary but not sufficient for C-36.

**V-02 on C-35 ("any of the above")**: "any of the above tokens is absent" uses "above" as positional anchor linking the HALT to the preceding fenced-code block. No token names appear inline in the HALT. Enumeration block remains independently revisable. Expected: C-35 PASS. Primary mechanism probe.

**V-03 on C-36 (DEVIATION: prefix)**: `DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` -- marker labels the branch at branch-instruction level. C-31: "precedes" is positional vocabulary; DEVIATION: is a role descriptor not a structural layer reference. C-32: scope declaration unchanged. C-30: no exec branch added. Expected: C-36 PASS. Orthogonality probe.

**V-04 on C-35 + C-36 jointly**: Both criteria applied; no structural overlap between AMEND HALT changes and routing branch changes. Expected: 29/29 = 100.00. Confirms two additions are sufficient for v15 ceiling.

**V-05 on C-35 "any listed token"**: "listed" references the preceding enumeration block as a listing artifact rather than by position. Rubric cites this form as equivalent. Expected: C-35 PASS. If PARTIAL: "above" is required; "listed" alone is insufficient.

**V-05 on C-36 OVERRIDE:**: Rubric lists OVERRIDE: alongside DEVIATION: as equivalent marker labels. Expected: C-36 PASS. If PARTIAL: DEVIATION: is required; OVERRIDE: alone is insufficient.
