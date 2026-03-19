R14 variations written to `simulations/quest/variations/discover-compare-variations-R14-2026-03-17.md`.

---

## R14 summary

**Pivot**: v12 exposes two gaps in the R13 V-01 ceiling. Under /26 denominator, R13 V-01 scores C-32 PARTIAL (deviation-only routing block but no scope header) and C-33 PARTIAL (BODY ORDER present but no BODY-ORDER-LAYER token). The fixes are additive and independent.

| Var | Axis | C-32 | C-33 | Projected |
|-----|------|------|------|-----------|
| **V-01** | v12 ceiling: both token + scope header | PASS | PASS | **100.00** |
| **V-02** | C-32 PARTIAL probe: token only, no scope header | PARTIAL | PASS | **99.81** |
| **V-03** | C-33 PARTIAL probe: scope header only, no token | PASS | PARTIAL | **99.81** |
| **V-04** | R13 V-01 rescored verbatim (no additions) | PARTIAL | PARTIAL | **99.62** |
| **V-05** | `BODY-ORDER-LAYER: none` probe on no-BODY-ORDER base | N/A | PASS | **99.58** |

**Key structural changes:**

- **V-01**: Adds `Token: BODY-ORDER-LAYER: active` after BODY ORDER + `ROUTING: deviation from BODY ORDER only.` as routing block header
- **V-02**: Adds token only; routing block unchanged from R13 V-01
- **V-03**: Adds scope header only; no token
- **V-04**: R13 V-01 verbatim -- establishes 0.38-point v12 cost on the prior ceiling
- **V-05**: R13 V-04 base (no BODY ORDER) + `BODY-ORDER-LAYER: none` token; D = /24 (C-30 + C-32 both not scored)

**Three discriminating questions for the scorecard:**
1. Does `Routing: if REG = engineering or general...` alone count as a scope declaration (C-32 PASS)? Expected: no.
2. Does the `BODY ORDER:` prose directive count as a named token (C-33 PASS)? Expected: no.
3. Does `BODY-ORDER-LAYER: none` satisfy C-33 PASS? Expected: yes -- rubric body explicitly lists `none` as an example.
rbatim. Both C-32 and C-33 PARTIAL. Establishes v12 penalty for R13 V-01 ceiling.
- **V-05**: R13 V-04 body (no BODY ORDER, two-branch routing) + `Token: BODY-ORDER-LAYER: none -- routing is sole ordering mechanism` before routing block. C-30 not scored, C-32 not scored (no BODY ORDER). D = /24. C-33 PASS from explicit none declaration.

---

**V-01** (ceiling): R13 V-01 body with two additions -- BODY-ORDER-LAYER: active token placed immediately after BODY ORDER directive; routing block opened with explicit scope header `ROUTING: deviation from BODY ORDER only.` C-32 PASS: deviation-only routing block with explicit scope declaration at header. C-33 PASS: named BODY-ORDER-LAYER token present before routing block. All 24 prior criteria carry from R13 V-01 PASS. Aspirational: 26/26 = 10.00. Expected composite: 100.00. Establishes v12 ceiling.

**V-02** (C-32 PARTIAL probe): R13 V-01 body + BODY-ORDER-LAYER: active token; routing block unchanged (no scope header at entry). C-32 PARTIAL: deviation-only routing block exists but opens without explicit scope declaration -- intent reconstructable from branch absence, not declared. C-33 PASS: named token present. All other criteria carry from R13 V-01. Expected: 25.5/26 = 9.808 -> composite 99.81. Establishes isolated C-32 PARTIAL penalty = 0.19 composite points.

**V-03** (C-33 PARTIAL probe): R13 V-01 body + routing scope header `ROUTING: deviation from BODY ORDER only.`; no BODY-ORDER-LAYER token added. C-32 PASS: explicit scope declaration present. C-33 PARTIAL: BODY ORDER layer presence implied by the BODY ORDER directive's existence but not declared as a named token -- evaluator must inspect for BODY ORDER to determine C-30 applicability. All other criteria carry from R13 V-01. Expected: 25.5/26 = 9.808 -> composite 99.81. Symmetric penalty with V-02; confirms C-32 and C-33 are independent and equally weighted.

**V-04** (R13 V-01 rescored against v12): R13 V-01 body verbatim -- no changes. C-32 PARTIAL: deviation-only routing block (`Routing: if REG = engineering or general...`) without scope header. C-33 PARTIAL: BODY ORDER present but no BODY-ORDER-LAYER token. Both penalties fire simultaneously. Expected: 25/26 = 9.615 -> composite 99.62. Establishes total v12 exposure on R13 ceiling = 0.38 composite points. Discriminating question: are C-32 and C-33 strictly additive (2 x 0.19) or is there a compound interaction? If actual = 99.62 exactly: additive. Any deviation signals interaction effect.

**V-05** (C-33-declared-none probe): R13 V-04 body (no BODY ORDER, two-branch routing, positional vocabulary) + `Token: BODY-ORDER-LAYER: none -- routing is sole ordering mechanism` declared before routing block. C-30: not scored (no BODY ORDER; D loses 1). C-32: not scored (no BODY ORDER; D loses 1). D = /24. C-33 PASS: explicit none token present before routing block. C-28 PARTIAL + C-29 PARTIAL carry from R13 V-04. C-31 PASS (positional vocabulary). Pass-weight: C-08..C-27 = 20 PASS + C-28 0.5 + C-29 0.5 + C-31 1.0 + C-33 1.0 = 23/24 = 9.583 -> composite 99.58. Discriminating question: does `BODY-ORDER-LAYER: none` satisfy C-33 PASS? Rubric body text gives `none` as an explicit example. Expected PASS. If actual = PARTIAL: criterion reads "presence" strictly, requiring `active` status only. Watch.

---

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational | Composite | Golden |
|-----------|--------------|-----------------|-------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 26/26 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 25.5/26 = 9.81 | **99.81** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 25.5/26 = 9.81 | **99.81** | TBD |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 25/26 = 9.62 | **99.62** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 23/24 = 9.58 | **99.58** | TBD |

---

## V-01 -- v12 ceiling: BODY-ORDER-LAYER token + routing scope header + deviation-only + positional

**Axis**: Single-axis (two additive additions) -- BODY-ORDER-LAYER: active token added after BODY ORDER directive; routing block opened with explicit scope declaration header. All other structure identical to R13 V-01.
**Hypothesis**: BODY ORDER unconditional -> C-29 PASS. Standalone BODY ORDER + routing block physically + lexically separate -> C-28 PASS. Deviation-only routing block (engineering branch only) -> C-30 PASS. Routing branch positional vocabulary, no name reference -> C-31 PASS. BODY-ORDER-LAYER: active token positioned before routing block -> C-33 PASS. Routing block opens with `ROUTING: deviation from BODY ORDER only.` -> C-32 PASS. All 24 R13 criteria carry at PASS. Aspirational: 26/26 = 10.00. Expected composite: 100.00. Establishes v12 ceiling.

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

## V-02 -- C-32 PARTIAL probe: BODY-ORDER-LAYER token only, no routing scope header

**Axis**: Single-axis -- BODY-ORDER-LAYER: active token added (C-33 target: PASS); routing block remains as R13 V-01 (no scope declaration header at entry, C-32 target: PARTIAL)
**Hypothesis**: BODY-ORDER-LAYER: active token present before routing block -> C-33 PASS. Deviation-only routing block opens directly with branch condition rather than scope declaration -> C-32 PARTIAL: the routing structure is correct (deviation-only) but the design intent is reconstructable only from branch absence, not from a declared scope header. All other criteria carry from R13 V-01. Expected: C-32 0.5 + C-33 1.0 out of 2 new criteria = 25.5/26 = 9.808 -> composite 99.81. Establishes isolated C-32 PARTIAL penalty = 0.19 composite points vs V-01 ceiling.

Discriminating question: does the routing prefix `Routing:` alone satisfy the "scope declaration at header" requirement? The rubric requires content identifying the block as handling only non-default cases (e.g., "deviation from BODY ORDER only", "non-exec registers"). The label `Routing:` alone carries no scope content. Expected C-32 PARTIAL. If actual = PASS: criterion accepts presence of any block header as sufficient.

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

## V-03 -- C-33 PARTIAL probe: routing scope header only, no BODY-ORDER-LAYER token

**Axis**: Single-axis -- routing block opened with explicit scope declaration `ROUTING: deviation from BODY ORDER only.` (C-32 target: PASS); no BODY-ORDER-LAYER token added (C-33 target: PARTIAL)
**Hypothesis**: BODY ORDER present and routing block deviation-only with explicit scope header at entry -> C-32 PASS. No BODY-ORDER-LAYER token declared -- BODY ORDER layer presence implied by the BODY ORDER directive in the preamble but not stated as a named token before the routing block -> C-33 PARTIAL: evaluator must locate the BODY ORDER directive to determine C-30 applicability, rather than reading a structural token. All other criteria carry from R13 V-01. Expected: C-32 1.0 + C-33 0.5 out of 2 new criteria = 25.5/26 = 9.808 -> composite 99.81. Symmetric with V-02; confirms each criterion independently contributes 0.19.

Discriminating question: does the presence of `BODY ORDER: ...` directive in the prompt preamble constitute "implied by layout" (C-33 PARTIAL) rather than "not declared as a token"? The rubric requires a named token in `Token: KEY: value` format. A prose directive is an instruction, not a token declaration. Implied-by-layout = PARTIAL.

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

## V-04 -- R13 V-01 rescored against v12: both C-32 and C-33 PARTIAL

**Axis**: Reference -- R13 V-01 body verbatim; rescored against v12 rubric (C-32 and C-33 scored, denominator /26)
**Hypothesis**: BODY ORDER present + deviation-only routing -> C-30 PASS. Positional vocabulary -> C-31 PASS. Lexical + physical isolation -> C-28 PASS. Unconditional directive -> C-29 PASS. All 24 R13 criteria carry at PASS. C-32: deviation-only routing block (`Routing: if REG = engineering or general...`) opens with the branch condition, not a scope declaration -- PARTIAL. C-33: BODY ORDER directive present but no `BODY-ORDER-LAYER:` token declared -- PARTIAL. Expected: 25/26 = 9.615 -> composite 99.62. Establishes total v12 exposure on R13 ceiling = 0.38 composite points. Confirms whether C-32 and C-33 penalties are strictly additive (each 0.19) or interact. If actual = 99.62 exactly: additive. Any deviation signals interaction effect. Watch.

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

## V-05 -- BODY-ORDER-LAYER: none probe: R13 V-04 + declared absence token

**Axis**: Single-axis -- R13 V-04 body (no standalone BODY ORDER, two-branch routing, positional vocabulary) + `Token: BODY-ORDER-LAYER: none -- routing is sole ordering mechanism` declared before routing block. C-33 target: PASS via declared absence.
**Hypothesis**: No standalone BODY ORDER -> C-29 PARTIAL (body ordering stated only inside routing conditionals, no unconditional directive). C-28 PARTIAL (per R13 V-04 precedent: no standalone BODY ORDER; body ordering implied only through routing block content). C-30 not scored (no BODY ORDER -> D loses 1). C-32 not scored (no BODY ORDER -> D loses 1). D = /24. BODY-ORDER-LAYER: none token present before routing block -> C-33 PASS. C-31 PASS (positional vocabulary in two-branch routing). All other C-08..C-27 criteria PASS. Pass-weight: 20 (C-08..C-27) + C-28 0.5 + C-29 0.5 + C-31 1.0 + C-33 1.0 = 23/24 = 9.583 -> composite 99.58.

Discriminating question 1: does `BODY-ORDER-LAYER: none` satisfy C-33 PASS? Rubric body text gives `BODY-ORDER-LAYER: none -- routing is sole ordering mechanism` as an explicit example and states "status declared." Declared absence = declared status = expected PASS. If actual = PARTIAL: criterion reads "presence is declared" in title strictly, requiring `active` status. Watch.

Discriminating question 2: does the explicit `BODY-ORDER-LAYER: none` declaration affect C-28 scoring? C-28 concerns isolation between body-order and routing-scope mechanisms. With no body-order layer, the declared `none` token identifies routing as sole mechanism -- this is a declaration of structural absence, not a coupling of the two mechanisms. Per R13 V-04 precedent, C-28 PARTIAL fires when body ordering is implied only through routing block content. The `none` declaration explicitly confirms this structure; it does not introduce a new body-order element. Expected C-28 PARTIAL to carry. Watch.

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

Token: `BODY-ORDER-LAYER: none -- routing is sole ordering mechanism`

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
| C-28 body-order and routing-scope isolated | PASS | PASS | PASS | PASS | **PARTIAL** |
| C-29 body ordering stated as unconditional directive | PASS | PASS | PASS | PASS | **PARTIAL** |
| C-30 routing block handles only deviation case | PASS | PASS | PASS | PASS | N/A |
| C-31 routing vocabulary positionally descriptive | PASS | PASS | PASS | PASS | PASS |
| **C-32 routing block scope declared deviation-only at header** | **PASS** | **PARTIAL** | **PASS** | **PARTIAL** | N/A |
| **C-33 body-ordering layer presence declared as token** | **PASS** | **PASS** | **PARTIAL** | **PARTIAL** | **PASS** |

### Key results to watch

**V-01 on C-32 and C-33 ceiling**: Two additive structural declarations -- `BODY-ORDER-LAYER: active` token + `ROUTING: deviation from BODY ORDER only.` scope header -- each independently satisfies one criterion without affecting any prior criterion. Confirms /26 ceiling at 100.00.

**V-02 on C-32 PARTIAL threshold**: BODY-ORDER-LAYER token present but no scope header. Key question: is `Routing: if REG = engineering or general...` a scope declaration? The branch condition states the triggering case but does not frame the block as handling only non-default cases. Expected C-32 PARTIAL. If actual = PASS: branch condition alone satisfies scope declaration -- C-32 threshold is lower than rubric examples suggest.

**V-03 on C-33 PARTIAL threshold**: Scope header present but no token. The `BODY ORDER: ...` directive is a prose instruction. Key question: does prose satisfy "declared as a named token"? Expected C-33 PARTIAL. If actual = PASS: criterion is form-agnostic (prose directive = token declaration) -- C-33 threshold is significantly looser than rubric implies.

**V-04 on C-32+C-33 additivity**: Both PARTIAL simultaneously. If strictly additive: V-04 = 99.62 exactly (V-02 = V-03 = 99.81, each 0.19 below V-01). Any deviation from 99.62 signals an interaction effect between C-32 and C-33 scoring.

**V-05 on BODY-ORDER-LAYER: none as C-33 PASS**: Declared absence token present. Key question: does declaring `none` satisfy "presence is declared"? Rubric body text gives `none` as an explicit example. Expected PASS. If actual = PARTIAL: the criterion title word "presence" overrides the body examples; `none` satisfies only "implied by layout." This is the highest-stakes discriminating question in R14 -- it determines whether the declared-absence path is a full C-33 pass or a structural ceiling at PARTIAL.
