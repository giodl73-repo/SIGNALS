Written to `simulations/quest/variations/discover-compare-variations-R12-2026-03-17.md`.

---

## R12 design summary

**Pivot**: v10 adds C-28 and C-29, bumping denominator to /22. R12 maps their state spaces.

| Var | Axis | C-28 | C-29 | Delta | Projected |
|-----|------|------|------|-------|-----------|
| V-01 | v10 ceiling: standalone `BODY ORDER` + isolated routing block | PASS | PASS | -- | **100.00** |
| V-02 | R11 V-01 body re-scored against v10 (routing as compound) | PARTIAL | PARTIAL | -- | **99.55** |
| V-03 | `BODY ORDER` + routing references it by name | PARTIAL | PASS | -- | **99.77** |
| V-04 | Engineering-only routing, no `BODY ORDER` | FAIL | PARTIAL | C-25 PARTIAL | **99.09** |
| V-05 | R11 V-05 body re-scored against v10 (no routing, no `BODY ORDER`) | FAIL | FAIL | C-25 FAIL, C-27 FAIL | **98.18** |

---

**V-01** (ceiling): Adds one line after `ANCHOR[0]` — `BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` — as a standalone unconditional directive. Routing block unchanged from R11 V-01 (both branches, after LEDGER GATE). Two separate structural elements = C-28 PASS. Explicit unconditional directive = C-29 PASS.

**V-02** (v10 baseline): R11 V-01 body verbatim, re-scored against v10 denominator. Routing block is the sole ordering specification — co-specifies body ordering AND routing scope in one conditional construct. Hypothesis: C-28 PARTIAL + C-29 PARTIAL = -0.45. Watch: if actual = 99.77, compound routing block doesn't trigger C-28 (only C-29 fires).

**V-03** (C-28 name-reference probe): Same `BODY ORDER` as V-01. Routing modified to reference it by name: `if REG = exec, follow BODY ORDER. If REG = engineering or general, reverse BODY ORDER: DECISION MATRIX precedes RECOMMENDATION.` Discriminating question: does referencing another element by name constitute a C-28 structural cross-reference? Expected PARTIAL; if actual = 100.00, token-name references are transparent to isolation.

**V-04** (engineering-only routing): No `BODY ORDER`. Routing block has only one branch: `if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` No exec branch, no standalone directive. C-25 PARTIAL (one branch, per R10). C-28 FAIL: exec ordering never stated anywhere — only inferrable from body layout. C-29 PARTIAL: engineering conditional contains explicit ordering but no unconditional directive.

**V-05** (v10 no-routing baseline): R11 V-05 body verbatim (no routing, recommendation-first layout), re-scored against /22. Four criteria penalized: C-25 FAIL + C-27 FAIL (v9) + C-28 FAIL + C-29 FAIL (v10). Delta vs R11 V-05 composite (99.00) = 0.82 — the exact cost of C-28 and C-29 being absent.

---

**Structural dependency surfaced by R12**: C-25 PASS implies C-29 >= PARTIAL (a routing block satisfying C-25 must name sections, which is an explicit ordering statement — at least conditional). C-28 PASS requires C-29 PASS (no independent body-order directive means C-28 cannot pass). These two co-emergence constraints are measurable from V-01 vs V-04 vs V-05.
S requires an independent body-order directive. An independent body-order directive is also what C-29 needs for PASS. No independent directive -> C-28 at most PARTIAL; C-29 at most PARTIAL. C-28 PASS is a necessary condition for C-29 PASS and vice versa (they co-emerge).

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/22) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 22/22 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 21/22 = 9.55 | **99.55** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 21.5/22 = 9.77 | **99.77** | TBD |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 20/22 = 9.09 | **99.09** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 18/22 = 8.18 | **98.18** | TBD |

### Key structural differences per variation

- **V-01**: Adds `BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` as a standalone directive after ANCHOR[0]. Routing block unchanged from R11 V-01 (both branches, after LEDGER GATE). Two isolated elements: BODY ORDER handles the default; routing block handles conditional overrides.
- **V-02**: R11 V-01 body unchanged. Routing block = compound: co-specifies body ordering AND routing scope in one conditional construct. No standalone BODY ORDER. Re-scored against v10.
- **V-03**: Same standalone BODY ORDER as V-01. Routing block modified to reference BODY ORDER by name: exec branch says "BODY ORDER applies"; engineering branch says "reverse BODY ORDER." Test: does name-referencing trigger C-28 PARTIAL?
- **V-04**: No BODY ORDER directive. Routing block has engineering-only branch: "if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION." Exec branch absent. Body layout recommendation-first (C-26 PASS). C-25 PARTIAL (one branch). C-28 FAIL (exec ordering never stated as independent directive; implied through body layout only). C-29 PARTIAL (engineering-branch conditional contains explicit ordering, but no unconditional directive).
- **V-05**: R11 V-05 body (routing block removed entirely, body layout recommendation-first). Same prompt re-scored against v10 denominator /22. All four new-from-v9-and-v10 criteria penalized: C-25 FAIL, C-27 FAIL, C-28 FAIL, C-29 FAIL.

---

## V-01 -- v10 ceiling: explicit BODY ORDER + isolated routing block

**Axis**: Single-axis -- adds standalone `BODY ORDER` directive after ANCHOR[0]; routing block unchanged from R11 V-01
**Hypothesis**: BODY ORDER is an explicit unconditional body-ordering directive -> C-29 PASS. BODY ORDER is a standalone structural element; routing block is a separate standalone structural element; neither is a compound directive -> C-28 PASS. Routing block has both branches -> C-25 PASS. Routing after LEDGER GATE -> C-27 PASS. Body layout recommendation-first -> C-26 PASS. All 20 R11 criteria carry over. Aspirational: 22/22 = 10.00. Expected composite: 100.00. Establishes v10 ceiling.

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

## V-02 -- R11 V-01 body re-scored against v10 (routing as compound directive)

**Axis**: Reference -- R11 V-01 body unchanged; re-scored against v10 rubric (C-28 and C-29 scored, denominator /22)
**Hypothesis**: No standalone BODY ORDER directive. Routing block co-specifies body ordering AND routing scope in one conditional construct -> C-28 PARTIAL (compound directive). Routing block states body ordering only within a conditional ("if exec, RECOMMENDATION first") -> C-29 PARTIAL (no independent unconditional directive). All 20 R11 criteria carry over at PASS. Aspirational: 21/22 = 9.55 -> composite 99.55. Establishes v10 baseline penalty for R11 V-01 body: -0.45 composite points (C-28 PARTIAL = -0.23 + C-29 PARTIAL = -0.23).

If actual composite = 99.77: only C-29 PARTIAL fires; routing compound does not trigger C-28 PARTIAL -- compound routing is classified as isolated for C-28 purposes, and the penalty comes solely from missing unconditional directive (C-29). This would revise the C-28 threshold: PARTIAL requires a literal single merged statement, not just a routing block that handles ordering.

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

## V-03 -- C-28 partial probe: BODY ORDER + routing references it by name

**Axis**: Single-axis -- BODY ORDER directive added (same as V-01); routing block modified to reference BODY ORDER by token name rather than re-stating section sequence independently
**Hypothesis**: BODY ORDER is an explicit unconditional directive -> C-29 PASS. Routing block references BODY ORDER by name ("follow BODY ORDER" / "reverse BODY ORDER") -> C-28 PARTIAL: routing block references the body-order structural property by name, which constitutes a structural reference per C-28. If actual composite = 100.00: token-name references are transparent to C-28; isolated elements that point to each other still satisfy the isolation criterion. If actual composite = 99.77 (as projected): name-referencing is sufficient to trigger C-28 PARTIAL, and true C-28 PASS requires each element to use only its own structural vocabulary without referencing the other by name. Expected: 21.5/22 = 9.77 -> composite 99.77.

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

## V-04 -- Engineering-only routing, no BODY ORDER: C-25 PARTIAL + C-28 FAIL + C-29 PARTIAL

**Axis**: Single-axis -- routing block reduced to engineering-only branch (no exec branch); BODY ORDER directive absent
**Hypothesis**: No standalone BODY ORDER directive. No exec routing branch specifying section ordering. Engineering-only routing branch: "if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION." C-25 PARTIAL: register-sensitive ordering present but only one register value addressed in the routing block (R10 confirmed engineering-only = PARTIAL). C-28 FAIL: exec body ordering never stated as an independent directive anywhere; routing block covers only the engineering case; exec body ordering derivable only from implicit body layout position (recommendation-first). "Body ordering implied only through... body layout" -> FAIL. C-29 PARTIAL: engineering routing branch is an explicit conditional ordering statement, but no unconditional directive exists. C-26 PASS: body layout is recommendation-first (exec-safe by default). C-23 PASS: exec register sees recommendation-first by body position. C-27 PASS: routing after gate. Expected: 20/22 = 9.09 -> composite 99.09.

Structural dependency confirmed by V-04: C-28 FAIL fires when exec body ordering is inferrable only from body layout, not from any explicit statement (neither standalone directive nor routing-exec-branch). The one-sided routing block covers the engineering deviation only; it provides no explicit statement for the exec default case.

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

## V-05 -- R11 V-05 body re-scored against v10: no routing, no BODY ORDER

**Axis**: Reference -- R11 V-05 body unchanged; re-scored against v10 rubric (C-28 and C-29 scored, denominator /22)
**Hypothesis**: No routing construct. No BODY ORDER directive. Body layout recommendation-first. Under v10: C-25 FAIL (no routing construct -- same as R11). C-27 FAIL (no routing block = fail per rubric -- same as R11). C-28 FAIL: no independent body-order directive; routing block absent; body ordering only derivable from body layout position (implied, never stated). C-29 FAIL: no explicit body ordering directive anywhere -- not in routing (absent), not as a standalone statement. C-26 PASS: body layout is recommendation-first (preserved -- V-05 pattern from R11). All 18 R11 passing criteria maintained. Aspirational: 18/22 = 8.18 -> composite 98.18. Establishes v10 no-routing compound penalty: 1.82 composite points (vs 1.00 under v9). Delta increment = 0.82 = the C-28 FAIL + C-29 FAIL contribution added by v10 new criteria.

Note: Under v9 /20 denominator, this body scored 18/20 = 9.00 -> composite 99.00. Under v10 /22, same body scores 18/22 = 8.18 -> composite 98.18. The 0.82 delta is the price of adding two new criteria (C-28 and C-29) that this no-routing body cannot satisfy: no independent body-order directive means both new criteria fail simultaneously.

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
| C-23 exec leads with recommendation | PASS | PASS | PASS | PASS | PASS |
| C-24 AMEND path sub-ledgers | PASS | PASS | PASS | PASS | PASS |
| C-25 register-gated routing block | PASS | PASS | PASS | **PARTIAL** | **FAIL** |
| C-26 body section order exec-safe | PASS | PASS | PASS | PASS | PASS |
| C-27 routing block within LEDGER GATE scope | PASS | PASS | PASS | PASS | **FAIL** |
| **C-28 body-order and routing-scope isolated** | **PASS** | **PARTIAL** | **PARTIAL** | **FAIL** | **FAIL** |
| **C-29 body ordering stated as unconditional directive** | **PASS** | **PARTIAL** | **PASS** | **PARTIAL** | **FAIL** |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/22) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 22/22 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 21/22 = 9.55 | **99.55** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 21.5/22 = 9.77 | **99.77** | TBD |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 20/22 = 9.09 | **99.09** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 18/22 = 8.18 | **98.18** | TBD |

### Key results to watch

**V-01 on C-28 and C-29**: Standalone `BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` + unmodified routing block. Two structurally separate elements: neither is a compound directive. Confirms 22/22 = 100.00 as v10 ceiling. Key structural claim: BODY ORDER is an unconditional standalone specification; routing block independently specifies conditional ordering without embedding body-ordering inside a compound directive.

**V-02 on C-28 and C-29 compound penalty**: R11 V-01 body unchanged. Routing block = sole ordering specification, co-specifying body section order AND routing scope within one conditional construct. C-28 PARTIAL (compound) + C-29 PARTIAL (conditional-only) -> -0.45 composite. If actual = 99.77: compound routing block does not trigger C-28 PARTIAL -- only C-29 penalty fires. This would revise C-28: PARTIAL requires a physically merged element (single statement), not just the routing block acting as the ordering spec.

**V-03 on C-28 name-reference sensitivity**: BODY ORDER directive present (C-29 PASS guaranteed). Routing references BODY ORDER by name: "follow BODY ORDER" / "reverse BODY ORDER." Discriminating question: is naming another element in the routing block a "structural reference" that triggers C-28 PARTIAL? Expected PARTIAL (name-reference = structural cross-reference). If actual = PASS (100.00): tokenized cross-references are transparent; isolation is satisfied by structural separability, not by vocabulary independence.

**V-04 on C-28 FAIL vs C-28 PARTIAL boundary**: Engineering-only routing branch. No standalone BODY ORDER. Exec body ordering is never explicitly stated -- derivable only from body layout position. C-28 FAIL: body ordering is purely implied, never stated as an independent directive (explicit or otherwise). Contrasts with V-02 where the routing block at least explicitly states section ordering for both cases (compound but explicit = PARTIAL). V-04 has no explicit exec ordering statement anywhere = FAIL.

**V-05 v10 no-routing compound baseline**: 4 penalties in aspirational: C-25 FAIL + C-27 FAIL (from v9) + C-28 FAIL + C-29 FAIL (new in v10). 18/22 = 98.18. Delta vs R11 V-05 under v9 (99.00) = 0.82 composite points. Delta vs V-01 ceiling = 1.82. Establishes that v10 adds 0.82 to the no-routing penalty vs v9, entirely from C-28 and C-29 now requiring explicit structural specification that a no-routing body cannot provide.
