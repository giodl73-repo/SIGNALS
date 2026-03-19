`discover-compare-variations-R15-2026-03-17.md` written.

---

## R15 summary

**5 variations, 3 single-axis + 2 combined:**

| Var | Axis | Key change | Projected |
|-----|------|-----------|-----------|
| **V-01** | Role sequence | Per-option batching — all A (FEAS/INERT/RISK/COMP), then all B | 100.00 |
| **V-02** | Output format | Uniform 1-5 numeric scale for FEAS + INERT + RISK | 100.00 |
| **V-03** | Lifecycle emphasis | Inertia-first within each option block; Inertia row first in matrix | 100.00 |
| **V-04** | Role sequence + inertia framing | Dedicated Inertia Gate section before all dimensional analysis; build/no-build fires inline at Gate | 100.00 |
| **V-05** | Phrasing register + format | Ceiling structure preserved; AMEND paths compressed to inline paragraph form (no fenced sub-ledger blocks) | **TBD on C-24** |

**Primary discriminating question for R15**: Does C-24 (AMEND path sub-ledgers) require the fenced-code checklist block format, or does an inline `HALT if X / Y absent` declaration with named tokens satisfy it? V-05 is the isolated probe — all 32 other criteria carry from R14 V-01. If C-24 PARTIAL: composite = 99.81, establishing sub-ledger block format as the mechanism. If PASS: inline is sufficient.

Secondary questions (V-01 through V-04):
- Does per-option batching affect C-02 (FAULT at each site is the mechanism, not section grouping)?
- Does numeric rating vocabulary affect C-10 (token name is the mechanism, not fill content)?
- Does a two-clause BODY ORDER satisfy C-29 (both clauses unconditional)?
- Does an early-firing build/no-build gate satisfy C-05 (criterion requires surfacing, not timing)?
R directive updated. DECISION MATRIX row order adjusted. Expected: 100.00.
- **V-04**: Dedicated Inertia Gate section runs both INERT-A and INERT-B immediately after ANCHOR[0], before any FEAS/RISK/COMP tokens. Build/no-build gate fires inline at Gate rather than deferred to end. Tests C-05 gate positioning. Expected: 100.00.
- **V-05**: R14 V-01 ceiling structure with AMEND rewritten to single-line inline path declarations -- TOKEN RECALL + FAULT + slots compressed per path, no separate block sub-ledger tables. Tests whether C-24 (AMEND path sub-ledgers) requires the block format or accepts inline ledger within a blocking instruction.

**Three discriminating questions for the scorecard:**
1. Does per-option batching (V-01) affect C-02 (inertia independence) scoring when INERT-A is physically inside the Option A block with its own FAULT, rather than in a shared inertia section? Expected: no -- explicit FAULT at each phase is the mechanism, not section grouping.
2. Does numeric FEAS/INERT scoring (V-02) affect C-10 (token cross-check at matrix assembly) scoring? Expected: no -- the criterion requires named tokens recalled at matrix, not specific rating vocabulary.
3. Does AMEND inline path format (V-05) satisfy C-24 (AMEND path sub-ledgers) when the blocking gate and token checklist are embedded in the single-line path declaration? Expected: C-24 PARTIAL -- the criterion requires identifiable sub-ledger structure; inline compression may not satisfy the "sub-ledger" form requirement. Key question is whether a blocking instruction on the same line as the ledger items counts.

---

**V-01** (per-option batching): All Option A analysis (FEAS-A, INERT-A, RISK-A, COMP-A) in a single block before all Option B analysis begins. BODY ORDER directive extended: "Option A analysis complete before Option B begins. RECOMMENDATION precedes DECISION MATRIX in all outputs." BODY-ORDER-LAYER: active. Routing: deviation from BODY ORDER only (engineering/general get DECISION MATRIX first). INERT-A appears inside Option A block with its own TOKEN RECALL + dual-polarity FAULT; INERT-B inside Option B block with same. C-02 satisfied by explicit FAULT at each site, not by section proximity. C-28 and C-29 carry: the BODY ORDER unconditional directive covers both option ordering and RECOMMENDATION/MATRIX ordering. Expected: 26/26 = 100.00. Discriminating question: does a two-clause BODY ORDER (option sequence + output order) still satisfy C-29 "unconditional directive"? Expected PASS -- both clauses are stated without register conditions.

**V-02** (numeric scale): R14 V-01 body with FEAS ratings changed from GREEN/YELLOW/RED to 1(lowest)..5(highest) and INERT ratings changed from LOW/MEDIUM/HIGH to 1(lowest)..5(highest). RISK tokens gain a numeric severity suffix: `RISK-A: {risk1/severity-1..5}, {risk2/severity-1..5}`. COMP tokens remain qualitative text. LEDGER GATE, ROUTING block, RECOMMENDATION, DECISION MATRIX, AMEND all unchanged from R14 V-01. Tests whether numeric token vocabulary is neutral to all criteria. Expected: 26/26 = 100.00. If any criterion penalizes numeric vs. qualitative rating vocabulary, it will appear here vs. V-01.

**V-03** (inertia-first per-option): Within each option block, INERTIA analysis runs before FEASIBILITY, RISK, and COMPETITIVE. BODY ORDER updated: "INERTIA precedes FEASIBILITY/RISK/COMPETITIVE for each option. RECOMMENDATION precedes DECISION MATRIX in all outputs." DECISION MATRIX row order updated: Inertia row is first data row (after header). BODY-ORDER-LAYER: active. ROUTING block unchanged (deviation handles engineering/general matrix-first). All TOKEN RECALL + FAULT mechanisms unchanged. Expected: 26/26 = 100.00. Discriminating question: does the change in intra-option dimension order (INERT before FEAS) affect C-29 (BODY ORDER as unconditional directive)? Expected PASS -- the BODY ORDER directive states the ordering without conditions.

**V-04** (Inertia Gate pattern): Dedicated Inertia Gate section immediately after ANCHOR[0] and before any dimensional analysis. Gate runs INERT-A (with TOKEN RECALL + FAULT) then INERT-B (with TOKEN RECALL + FAULT). Build/no-build gate fires inline at the Inertia Gate: "If INERT-A = HIGH and INERT-B = HIGH, state build-neither is a candidate recommendation before continuing." Remaining analysis (FEAS/RISK/COMP for both) follows in standard dimension-batched order. BODY ORDER updated: "INERTIA GATE (both options) before all other analysis. RECOMMENDATION precedes DECISION MATRIX in all outputs." BODY-ORDER-LAYER: active. Tests C-05 gate placement (gate fires before dimensional analysis rather than after LEDGER GATE). Expected: 26/26 = 100.00.

**V-05** (AMEND inline path compression): R14 V-01 ceiling structure with one targeted change: AMEND paths compressed to inline single-paragraph form. Each path declares TOKEN RECALL + FAULT + slot + blocking halt in prose flow rather than as a block sub-ledger table. No separate fenced-code sub-ledger blocks. Tests C-24 (AMEND path sub-ledgers) and C-19 (AMEND self-contained). If C-24 requires identifiable tabular/list sub-ledger structure, inline compression fires a PARTIAL. If C-19 requires structured slot declarations, inline prose may also partial. Expected: C-24 PARTIAL (or FAIL depending on rubric's "sub-ledger" minimum form) -> composite 99.81 or lower. All other 25 criteria carry at PASS from R14 V-01.

---

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational | Composite | Golden |
|-----------|--------------|-----------------|-------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 26/26 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 26/26 = 10.00 | **100.00** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 26/26 = 10.00 | **100.00** | TBD |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 26/26 = 10.00 | **100.00** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 25.5/26 = 9.81 | **99.81** | TBD |

---

## V-01 -- Role sequence: per-option batching

**Axis**: Role sequence (single-axis)
**Hypothesis**: Grouping all four dimensions for Option A in one block before all four for Option B (vs. R14 V-01's dimension-batched pairing of FEAS-A/FEAS-B, then INERT-A/INERT-B, etc.) keeps each option's inertia FAULT physically isolated within its own analysis block. Per-option grouping may strengthen C-02 signal. BODY ORDER updated to declare option-sequence constraint. All C-32/C-33 mechanisms preserved. Expected: 26/26 = 100.00.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: Option A analysis complete before Option B analysis begins. RECOMMENDATION precedes DECISION MATRIX in all outputs.
Token: `BODY-ORDER-LAYER: active`

---

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

---

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

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

## V-02 -- Output format: uniform numeric scale (1-5)

**Axis**: Output format (single-axis)
**Hypothesis**: Replacing qualitative rating vocabulary (GREEN/YELLOW/RED for FEAS, LOW/MEDIUM/HIGH for INERT) with a uniform 1-5 numeric scale eliminates vocabulary switching between dimensions. RISK tokens gain a numeric severity suffix. COMP remains qualitative text (positioning is inherently non-numeric). All structural mechanisms unchanged from R14 V-01. Tests whether C-10 (token cross-check at matrix assembly) is neutral to numeric vs. qualitative rating vocabulary. Expected: 26/26 = 100.00.

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

Rate 1 (lowest feasibility) to 5 (highest). REG-framed.

Token: `FEAS-A: {1..5} -- {one sentence}`

Rate 1 (lowest feasibility) to 5 (highest). REG-framed. Independent of Option A.

Token: `FEAS-B: {1..5} -- {one sentence}`

---

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate 1 (lowest inertia, teams would readily adopt) to 5 (highest inertia, teams would do nothing). Name Option A's inertia mechanism.

Token: `INERT-A: {1..5} -- {mechanism}`

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate 1 to 5. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {1..5} -- {mechanism}`

---

Top 2 risks. Rate each 1 (low severity) to 5 (high). REG-framed.

Token: `RISK-A: {risk1/1..5}, {risk2/1..5}`

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/1..5}, {risk2/1..5}`

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

If INERT-A >= 4 and INERT-B >= 4: state "Build neither is a candidate recommendation."
Name override condition or revise RECOMMENDATION above to Neither.

---

AMEND:

**Add Option C:**

Token: `FEAS-C: {1..5} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {1..5} -- {mechanism}`
Token: `RISK-C: {risk1/1..5}, {risk2/1..5}`
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

## V-03 -- Lifecycle emphasis: inertia-first within each option block

**Axis**: Lifecycle emphasis (single-axis)
**Hypothesis**: Moving INERTIA to the first dimension analyzed within each option block (before FEASIBILITY, RISK, COMPETITIVE) makes the status quo the immediate referent before any build-side analysis. BODY ORDER directive updated to declare INERTIA-first ordering. DECISION MATRIX reorders rows accordingly (Inertia row first). All TOKEN RECALL + FAULT mechanisms unchanged. Tests whether intra-option dimension reordering affects C-29 (unconditional BODY ORDER directive) or C-03 (matrix format). Expected: 26/26 = 100.00.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: INERTIA precedes FEASIBILITY, RISK, and COMPETITIVE for each option. RECOMMENDATION precedes DECISION MATRIX in all outputs.
Token: `BODY-ORDER-LAYER: active`

---

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

---

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

LEDGER GATE:

```
REG:       [ ]
ANCHOR[0]: [ ]
INERT-A:   [ ]
INERT-B:   [ ]
FEAS-A:    [ ]
FEAS-B:    [ ]
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
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Feasibility | N/A | FEAS-A | FEAS-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or revise RECOMMENDATION above to Neither.

---

AMEND:

**Add Option C:**

Token: `INERT-C: {rating} -- {mechanism}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `FEAS-C: {rating} -- {one sentence}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`

```
Add-C ledger: INERT-C [ ]  FEAS-C [ ]  RISK-C [ ]  COMP-C [ ]
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

## V-04 -- Combined: role sequence + inertia framing -- Inertia Gate pattern

**Axis**: Role sequence + inertia framing (combined)
**Hypothesis**: A dedicated Inertia Gate section runs INERT-A and INERT-B immediately after ANCHOR[0], before any FEAS/RISK/COMP tokens. Build/no-build gate fires inline at the Gate rather than deferred to post-LEDGER-GATE. This makes the status quo verdict structurally prior to all dimensional analysis -- teams see whether the build case clears the inertia bar before investing in full analysis. BODY ORDER updated. Tests C-05 gate timing and C-12 anchor-before-analysis positioning under a two-section analysis structure. Expected: 26/26 = 100.00.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: INERTIA GATE (both options) before all dimensional analysis. RECOMMENDATION precedes DECISION MATRIX in all outputs.
Token: `BODY-ORDER-LAYER: active`

---

INERTIA GATE:

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from above -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation." Name override condition or continue only if a build case can be stated.

---

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

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
INERT-A:   [ ]
INERT-B:   [ ]
FEAS-A:    [ ]
FEAS-B:    [ ]
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
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Feasibility | N/A | FEAS-A | FEAS-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

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

## V-05 -- Combined: phrasing register + format -- AMEND inline path compression

**Axis**: Phrasing register + output format (combined)
**Hypothesis**: R14 V-01 ceiling structure preserved in full -- all token declarations, TOKEN RECALL + FAULT discipline, LEDGER GATE, ROUTING block, BODY-ORDER-LAYER: active, RECOMMENDATION, DECISION MATRIX unchanged. Single targeted change: AMEND paths rewritten as inline single-paragraph declarations with no separate fenced-code block sub-ledger tables. Each path carries TOKEN RECALL + FAULT + slot tokens + blocking halt compressed into flowing inline form. Tests whether C-24 (AMEND path sub-ledgers) requires identifiable tabular/list sub-ledger structure or accepts inline blocking halt + token checklist as equivalent. C-19 (AMEND self-contained via inline TOKEN RECALL + FAULT) should still PASS -- inline form still carries TOKEN RECALL and FAULT at each path. If C-24 PARTIAL: composite = 99.81. Establishes whether block sub-ledger format is the C-24 mechanism or whether inline ledger content is sufficient.

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

**Add Option C:** TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}` FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error. Produce tokens FEAS-C, INERT-C, RISK-C, COMP-C. **HALT if any of FEAS-C / INERT-C / RISK-C / COMP-C is absent before extending matrix.** Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:** TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}` FAULT: apply multiplier to dimension scores only -- do not revise token values. Produce token WEIGHT: {dimension} x {multiplier}. **HALT if ANCHOR[0] or WEIGHT token is absent before re-scoring.** Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:** TOKEN RECALL: `REG = {restate original register}` FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0]. Produce token REG override: {new register}. **HALT if REG or REG-override token is absent before re-rendering.** Re-render DECISION MATRIX labels and RECOMMENDATION framing.

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
| **C-24 AMEND path sub-ledgers** | PASS | PASS | PASS | PASS | **TBD** |
| C-25 register-gated routing block | PASS | PASS | PASS | PASS | PASS |
| C-26 body section order exec-safe | PASS | PASS | PASS | PASS | PASS |
| C-27 routing block within LEDGER GATE scope | PASS | PASS | PASS | PASS | PASS |
| C-28 body-order and routing-scope isolated | PASS | PASS | PASS | PASS | PASS |
| C-29 body ordering stated as unconditional directive | PASS | PASS | PASS | PASS | PASS |
| C-30 routing block handles only deviation case | PASS | PASS | PASS | PASS | PASS |
| C-31 routing vocabulary positionally descriptive | PASS | PASS | PASS | PASS | PASS |
| C-32 routing block scope declared deviation-only at header | PASS | PASS | PASS | PASS | PASS |
| C-33 body-ordering layer presence declared as token | PASS | PASS | PASS | PASS | PASS |

### Key results to watch

**V-01 on C-02 per-option batching**: Each option's inertia FAULT is physically inside the option block (INERT-A in the Option A block, INERT-B in the Option B block). C-02 requires independent inertia assessment -- the FAULT mechanism (explicit exclusion at point of use) is the operative criterion, not section grouping. If actual = PASS: per-option batching is neutral to C-02. If actual = PARTIAL: criterion is sensitive to section grouping, not just FAULT presence.

**V-02 on C-10 numeric vocabulary**: FEAS and INERT tokens carry 1-5 integers. The LEDGER GATE checks tokens by name; the matrix assembles by token reference. C-10 requires named tokens cross-checked at assembly -- rating vocabulary is the fill content, not the mechanism. Expected neutral. If any criterion scores differently on V-02 vs. V-01: isolate to the numeric change (only structural delta).

**V-03 on C-29 multi-clause BODY ORDER**: BODY ORDER reads "INERTIA precedes FEASIBILITY, RISK, and COMPETITIVE for each option. RECOMMENDATION precedes DECISION MATRIX in all outputs." Two clauses, both unconditional. C-29 requires body ordering stated as unconditional directive. Both clauses qualify. Expected PASS. If actual = PARTIAL: criterion may read multi-clause BODY ORDER as mixed-scope (intra-option ordering vs. output ordering), requiring single-scope statement.

**V-04 on C-05 gate placement**: Build/no-build gate fires at the Inertia Gate section (before FEAS/RISK/COMP tokens exist) rather than post-LEDGER-GATE. C-05 requires the gate to be surfaced -- it does not specify where. Expected PASS. If actual = PARTIAL: criterion may require the gate to follow from full token analysis before firing.

**V-05 on C-24 sub-ledger form**: AMEND paths carry `HALT if X or Y token absent` inline rather than as a fenced-code checklist block. The blocking instruction and the token enumeration are present but not formatted as a tabular/list sub-ledger. C-24 title is "AMEND path sub-ledgers." If the criterion requires identifiable sub-ledger structure (checklist or table form), inline HALT with named tokens = PARTIAL. If inline HALT + token names = PASS: C-24 is form-agnostic. This is the primary discriminating question in R15.
