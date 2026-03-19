Written to `simulations/quest/variations/discover-compare-variations-R11-2026-03-17.md`.

---

## R11 design summary

**Pivot**: v9 adds C-26 and C-27, bumping the denominator to /20. R10 V-01 already satisfies both. R11 maps their state spaces and establishes the v9 no-routing penalty.

| Var | Axis | C-26 | C-27 | C-25 | Projected |
|-----|------|------|------|------|-----------|
| V-01 | v9 ceiling reference | PASS | PASS | PASS | **100.00** |
| V-02 | C-27 partial: routing block before LEDGER GATE | PASS | PARTIAL | PASS | **99.75** |
| V-03 | C-26 partial: matrix-first body, routing overrides exec | PARTIAL | PASS | PASS | **99.75** |
| V-04 | C-26 + C-27 compound partial | PARTIAL | PARTIAL | PASS | **99.50** |
| V-05 | No routing construct (C-25 + C-27 fail baseline) | PASS | FAIL | FAIL | **99.00** |

**Four discriminating questions:**

1. **V-01**: Confirms 20/20 = 100.00 is attainable under v9.
2. **V-02**: Isolates C-27 PARTIAL — routing block before gate but construct otherwise intact. Establishes C-27 PARTIAL = 0.25 penalty.
3. **V-03**: Primary orthogonality test — C-26 PARTIAL (matrix-first body) vs C-23 independence. Exec register still gets recommendation-first via routing override. Expected C-23 PASS; if C-23 FAIL, it reveals an undocumented C-26/C-23 coupling.
4. **V-05**: Establishes v9 no-routing penalty = **1.00 composite points** (vs 0.56 under v8). The extra 0.44 = C-27 FAIL now penalized independently.

Key structural difference per variation:
- **V-02**: routing block moved above the LEDGER GATE block
- **V-03**: DECISION MATRIX and RECOMMENDATION sections swapped in body; routing construct stays after gate
- **V-04**: both V-02 and V-03 mutations applied simultaneously
- **V-05**: routing block removed entirely; body remains recommendation-first (C-26 stays PASS by default)
PASS | PASS | PASS | PASS |
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
| C-23 exec leads with recommendation | PASS | PASS | **PASS** | **PASS** | PASS |
| C-24 AMEND path sub-ledgers | PASS | PASS | PASS | PASS | PASS |
| C-25 register-gated routing block | PASS | PASS | PASS | PASS | **FAIL** |
| **C-26 body section order exec-safe** | **PASS** | **PASS** | **PARTIAL** | **PARTIAL** | **PASS** |
| **C-27 routing block within LEDGER GATE scope** | **PASS** | **PARTIAL** | **PASS** | **PARTIAL** | **FAIL** |

*V-03 C-23 marked PASS (expected): exec register gets recommendation first via routing override, which is routing-construct-independent per v9 rubric update. C-26 and C-23 are orthogonal -- C-26 PARTIAL does not create a C-23 gap. V-03 is this round's primary orthogonality confirmation.*

*V-05 C-26 marked PASS: body section order is recommendation-first by default (no routing block to redirect); exec-safe without needing a routing construct. C-25 FAIL + C-27 FAIL together remove 2.0 aspirational units from /20 -> 18/20 = 9.00 -> composite 99.00.*

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/20) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 20/20 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 19.5/20 = 9.75 | **99.75** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 19.5/20 = 9.75 | **99.75** | TBD |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 19/20 = 9.50 | **99.50** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 18/20 = 9.00 | **99.00** | TBD |

*V-02 and V-03 project equal at 99.75 despite hitting different criteria (C-27 PARTIAL vs C-26 PARTIAL). Score equality confirms both aspirational criteria carry identical weight (1/20 each) and PARTIAL = 0.5 within the PARTIAL band.*

*V-04 at 99.50 confirms compound partial is purely additive: C-26 PARTIAL + C-27 PARTIAL = 2 x 0.25 deduction. No interaction penalty.*

*V-05 at 99.00 establishes the v9 no-routing-construct penalty: 1.00 composite points (vs 0.56 under v8). The additional 0.44 deduction comes from C-27 FAIL being newly penalized in v9. C-26 stays PASS because body section order is recommendation-first by design when no routing construct is present.*

---

### Key discriminating tests

**V-01 on C-26 and C-27**: R10 V-01 body has routing block after LEDGER GATE and RECOMMENDATION section before DECISION MATRIX. Both new criteria satisfied. Confirms 20/20 = 100.00 as v9 ceiling.

**V-02 on C-27**: Routing block moved to before LEDGER GATE (between COMP-B and LEDGER GATE). REG token is declared but not yet verified when routing fires -- absent REG reaches routing logic unguarded. C-27 PARTIAL. C-25 still PASS (both branches present, construct still exists). C-26 still PASS (body order recommendation-first). Establishes C-27 PARTIAL penalty = 0.25 composite points.

**V-03 on C-26 and C-23 orthogonality**: Body section order inverted -- DECISION MATRIX appears before RECOMMENDATION in body. Routing block (both branches, after gate) explicitly overrides exec to recommendation-first. C-26 PARTIAL: body is matrix-first; exec correctness depends on routing override rather than body default. C-23: exec still gets recommendation first (routing override is explicit) -> C-23 PASS. C-26 PARTIAL does not create C-23 gap (orthogonal per v9 C-23 update). This is R11's primary orthogonality confirmation: C-23 reads effective output position; C-26 reads body-section default ordering. The two criteria fire on different structural properties. Expected composite: 19.5/20 = 99.75.

**V-04 on compound partial**: Additivity confirmed if composite = 99.50. Matrix-first body + routing before gate. Neither interaction creates a new failure mode -- both criteria remain independent. Any deviation from 99.50 indicates a non-additive interaction between C-26 and C-27.

**V-05 baseline under v9**: No routing construct; recommendation-first body. C-25 FAIL (no construct). C-27 FAIL (no routing block = fail per rubric, C-25 scoring independent). C-26 PASS (body is recommendation-first by design; exec-safe without routing = pass condition). Composite = 18/20 = 9.00 -> 99.00. Delta vs V-01 = 1.00. Delta vs v8 V-05 baseline (99.44) = 0.44 -- exactly the C-27 FAIL contribution newly added in v9.

---

## V-01 -- v9 ceiling reference (R10 V-01 body unchanged)

**Axis**: Reference -- R10 V-01 body unchanged; re-scored against v9 rubric (C-26 and C-27 scored, denominator /20)
**Hypothesis**: Body section order is recommendation-first; routing block is after LEDGER GATE. Both new v9 criteria pass. All 18 prior criteria confirmed PASS under v8. Aspirational: 20/20 = 10.00. Expected composite: 100.00. Establishes v9 ceiling.

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

## V-02 -- C-27 partial: routing block before LEDGER GATE

**Axis**: Single-axis -- routing block moved to before LEDGER GATE; all else identical to V-01
**Hypothesis**: C-27 requires routing block to appear after LEDGER GATE. V-02 places the routing block between COMP-B and LEDGER GATE -- routing fires before REG has been verified present. C-27 PARTIAL. C-25 PASS: both branches still present in single conditional construct (construct exists, only positioning is wrong). C-26 PASS: body section order remains recommendation-first; exec-safe by positional default. C-23 PASS: exec still gets recommendation first (routing instruction unchanged). All other criteria identical to V-01. Expected 19.5/20 = 9.75 -> composite 99.75. Establishes C-27 PARTIAL = 0.25 composite point deduction.

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

Routing: if REG = exec, produce RECOMMENDATION first, then DECISION MATRIX.
If REG = engineering or general, produce DECISION MATRIX first, then RECOMMENDATION.

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

## V-03 -- C-26 partial: matrix-first body, routing overrides exec register

**Axis**: Single-axis -- body section order inverted (DECISION MATRIX before RECOMMENDATION); routing block (both branches, after gate) overrides exec to recommendation-first
**Hypothesis**: C-26 reads body section order independent of routing. Body is matrix-first -> exec correctness depends on routing block firing -> C-26 PARTIAL. C-23: exec still gets recommendation first (routing override is explicit) -> C-23 PASS. C-26 PARTIAL does not create a C-23 gap (orthogonal per v9 C-23 update). C-25 PASS (both branches in single construct). C-27 PASS (routing after gate). This is R11's primary orthogonality confirmation: C-23 reads effective output position; C-26 reads body-section default ordering. Expected 19.5/20 = 9.75 -> composite 99.75.

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
Name override condition or revise RECOMMENDATION below to Neither.

---

RECOMMENDATION:

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

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

## V-04 -- C-26 + C-27 compound partial: matrix-first body + routing before gate

**Axis**: Two-axis combination -- V-02 routing-before-gate + V-03 matrix-first body simultaneously
**Hypothesis**: C-26 PARTIAL (matrix-first body, exec depends on routing). C-27 PARTIAL (routing before gate). C-25 PASS (both branches in single construct -- construct exists, position is wrong, branch coverage is complete). C-23 PASS (routing override makes exec recommendation-first; C-26 PARTIAL does not create C-23 gap). Score = 19/20 = 9.50 -> composite 99.50. Confirms compound partial is purely additive: no interaction penalty between C-26 and C-27.

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

Routing: if REG = exec, produce RECOMMENDATION first, then DECISION MATRIX.
If REG = engineering or general, produce DECISION MATRIX first, then RECOMMENDATION.

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
Name override condition or revise RECOMMENDATION below to Neither.

---

RECOMMENDATION:

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

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

## V-05 -- No routing construct: C-25 + C-27 fail baseline (v9 denominator)

**Axis**: Single-axis -- routing block removed entirely; body section order recommendation-first (C-26-safe by default)
**Hypothesis**: C-25 FAIL (no routing construct). C-27 FAIL (no routing block = fail per rubric; C-25 scoring applies independently). C-26 PASS: body is recommendation-first by design; exec-safe without routing = pass condition. C-23 PASS: body order recommendation-first satisfies C-23 independently of routing (confirmed R10 V-05 and C-23 positional-independence). All 18 prior passing criteria maintained. Aspirational: 18/20 = 9.00 -> composite 99.00. Establishes v9 no-routing penalty: 1.00 composite points (vs 0.56 under v8). Delta increment = 0.44 = the C-27 FAIL contribution newly added in v9.

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
| C-23 exec leads with recommendation | PASS | PASS | **PASS** | **PASS** | PASS |
| C-24 AMEND path sub-ledgers | PASS | PASS | PASS | PASS | PASS |
| C-25 register-gated routing block | PASS | PASS | PASS | PASS | **FAIL** |
| **C-26 body section order exec-safe** | **PASS** | **PASS** | **PARTIAL** | **PARTIAL** | **PASS** |
| **C-27 routing block within LEDGER GATE scope** | **PASS** | **PARTIAL** | **PASS** | **PARTIAL** | **FAIL** |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/20) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 20/20 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 19.5/20 = 9.75 | **99.75** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 19.5/20 = 9.75 | **99.75** | TBD |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 19/20 = 9.50 | **99.50** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 18/20 = 9.00 | **99.00** | TBD |

### Key results to watch

**V-01 on C-26 and C-27**: Confirms recommendation-first body + routing-after-gate satisfies both new v9 criteria. 20/20 = 100.00. V9 ceiling verified.

**V-02 on C-27**: Routing block before gate -> C-27 PARTIAL. Routing construct still complete (both branches) -> C-25 PASS. Body order unchanged -> C-26 PASS. Composite 99.75 establishes C-27 PARTIAL = 0.25 penalty.

**V-03 on C-26 and C-23 orthogonality**: Matrix-first body -> C-26 PARTIAL. Routing override makes exec recommendation-first -> C-23 PASS. Key result: C-26 PARTIAL and C-23 PASS coexist -- C-26 reads body default ordering; C-23 reads effective exec output position. If V-03 C-23 scores FAIL, it would mean C-23 cannot be satisfied when C-26 is PARTIAL -- an undocumented criterion coupling. Expected orthogonality (C-23 PASS); marked for watch.

**V-04 on compound partial**: Additivity confirmed if composite = 99.50. Any deviation indicates a non-additive interaction between C-26 and C-27.

**V-05 under v9**: No routing construct. C-25 FAIL + C-27 FAIL. C-26 PASS (body recommendation-first). Composite 99.00. Delta vs V-01 = 1.00. Delta vs v8 V-05 (99.44) = 0.44 -- the C-27 FAIL contribution. Confirms C-27 adds its own independent penalty on top of C-25 when no routing construct is present.
