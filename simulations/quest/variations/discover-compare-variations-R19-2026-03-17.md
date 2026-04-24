**`discover-compare-variations-R19-2026-03-17.md` written.**

---

## R19 design summary

**Target criteria**: C-39 and C-40 — the two v17 additions. Both extend existing criteria from inspection-based to declaration-based enforcement.

| Var | Axis | Key change | Projected |
|-----|------|-----------|-----------|
| V-01 | Baseline at /31 | R18 V-01 carry — no C-39/C-40 implementation | **100.00** |
| V-02 | C-39 only: declaration + token recall | `AMEND-HALT` declared before AMEND; each path uses `{AMEND-HALT}` | **100.00** |
| V-03 | C-39 failure: declaration without token recall | `AMEND-HALT` declared; paths still use literal phrase | **99.69** |
| V-04 | C-40 only: BRANCH-RULE declaration | `BRANCH-RULE` with equivalence sets declared before routing block | **100.00** |
| V-05 | Combined C-39 + C-40 | Both declarations present; full /33 denominator | **100.00** |

**Denominator math under v17 (/33 base):**

| Var | C-39 | C-40 | Denominator |
|-----|------|------|-------------|
| V-01 | N/S (−1) | N/S (−1) | /31 |
| V-02 | PASS | N/S (−1) | /32 |
| V-03 | FAIL | N/S (−1) | /32 |
| V-04 | N/S (−1) | PASS | /32 |
| V-05 | PASS | PASS | /33 |

---

**What each variation adds relative to V-01:**

**V-02** (single-axis C-39): `AMEND-HALT: "any of the above tokens is absent"` declared after the build/no-build gate and before `AMEND:`. Each path HALT line becomes `**HALT -- do not {action} if {AMEND-HALT}.**` — token name, not literal string. Tests declaration-before-use + token-name recall as the C-39 pass mechanism.

**V-03** (C-39 failure probe): Same `AMEND-HALT` declaration added, but each path HALT still reads `**HALT -- do not {action} if any of the above tokens is absent.**` — the literal phrase, not `{AMEND-HALT}`. C-37 PASS (uniform), C-39 FAIL (declaration without recall). The rubric's canonical `c39-declaration-architecture` pattern: uniformity-by-inspection ≠ uniformity-by-declaration.

**V-04** (single-axis C-40): `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER: {DEVIATION: | OVERRIDE:}] + [POSITIONAL-VOCAB: {precedes | before | follows | after}]` inserted between the LEDGER GATE and the ROUTING block. Routing line unchanged. Tests pre-routing pairing contract declaration as the C-40 mechanism; equivalence sets named in the declaration make R18 form-neutrality visible without rubric cross-reference.

**V-05** (combined ceiling probe): Both V-02 and V-04 changes applied. Full /33 denominator. All 33 aspirational criteria scored. Tests that the two declaration mechanisms coexist without interaction effects.

---

**Open discrimination questions:**
1. V-01: Both exclusions active under v17 — denominator /31? Expected: yes, 100.00.
2. V-02: `{AMEND-HALT}` token recall satisfies C-39? Expected: yes, 100.00 on /32.
3. V-03: Declaration present but literal phrase used — C-37 PASS, C-39 FAIL, score 99.69? Confirms token recall is the gate.
4. V-04: BRANCH-RULE with equivalence sets satisfies C-40? Expected: yes, 100.00 on /32.
5. V-05: Both declarations together score 100.00 on /33 with no interaction effects?
S but no BRANCH-RULE declaration before routing block -- C-40 not scoreable -- -1.

---

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational | Composite | Golden |
|-----------|--------------|-----------------|-------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 31/31 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 32/32 = 10.00 | **100.00** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 31/32 = 9.69 | **99.69** | No |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 32/32 = 10.00 | **100.00** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 33/33 = 10.00 | **100.00** | TBD |

---

## V-01 -- Baseline carry at /31

**Axis**: Baseline (denominator shift from /31 to /33 base, both gate exclusions active)
**Hypothesis**: R18 V-01 body verbatim. Under v17, C-39 and C-40 are newly defined. C-39 gate: C-37 PASS (uniform "any of the above tokens is absent" across all three AMEND paths) but no AMEND-HALT declaration token present -- C-39 N/S -- -1 from denominator. C-40 gate: C-38 PASS (DEVIATION: + "precedes" on same routing line) but no BRANCH-RULE declaration before routing block -- C-40 N/S -- -1 from denominator. Effective denominator: /33 - 2 = /31. All 31 prior criteria carry at PASS. Expected: 31/31 = 100.00. Establishes R18 V-01 golden body satisfies v17 scoring without modification at denominator /31.

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

## V-02 -- C-39 only: AMEND-HALT declaration + token recall at each path

**Axis**: Lifecycle emphasis (single-axis -- C-39 declaration architecture)
**Hypothesis**: `AMEND-HALT: "any of the above tokens is absent"` is declared as a canonical token immediately before the AMEND block opens. Each of the three AMEND path HALT instructions references it by token name (`{AMEND-HALT}`) rather than reproducing the literal phrase. C-37: all three paths enforce uniformity via the single AMEND-HALT token -- uniformity is by declaration, not by per-path inspection. C-37 PASS. C-39: declaration present before AMEND, token name recalled at each path -- both conditions satisfied. C-39 PASS. C-40: no BRANCH-RULE declaration before routing block -- C-40 N/S -- -1 from denominator. Effective denominator: /32. All 31 prior criteria carry unchanged. Expected: 32/32 = 100.00. Primary C-39 mechanism probe: confirms declaration-before-use + token-name recall satisfies C-39.

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

AMEND-HALT: "any of the above tokens is absent"

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
**HALT -- do not extend matrix if {AMEND-HALT}.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if {AMEND-HALT}.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if {AMEND-HALT}.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 -- C-39 failure: AMEND-HALT declared but paths use literal phrase

**Axis**: Lifecycle emphasis (single-axis -- C-39 declaration-without-recall failure probe)
**Hypothesis**: `AMEND-HALT: "any of the above tokens is absent"` is declared before the AMEND block (declaration present, before-phase condition met). Each path HALT instruction uses the literal phrase "any of the above tokens is absent" -- identical to the declared value, but referenced as a typed string rather than the token name `{AMEND-HALT}`. C-37: all three paths use identical literal phrase -- uniformity-by-inspection satisfied. C-37 PASS. C-39: rubric requires each path to reference the declared token "by token name"; literal phrase reproduction, even when identical to the declaration value, is not token-name recall. C-39 FAIL. C-37 PASS + C-39 FAIL is the `c39-declaration-architecture` watch list pattern: uniformity-by-inspection (C-37) and uniformity-by-declaration (C-39) are distinct scored states. C-40: no BRANCH-RULE declaration -- N/S -- -1. Denominator: /32. Pass count: 31. Aspirational: 31/32 x 10 = 9.69. Composite: **99.69**. Confirms token-name recall at each path is the C-39 gate mechanism, not declaration presence alone.

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

AMEND-HALT: "any of the above tokens is absent"

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

## V-04 -- C-40 only: BRANCH-RULE declaration before routing block

**Axis**: Role sequence (single-axis -- C-40 pairing contract declaration)
**Hypothesis**: A `BRANCH-RULE` declaration is added immediately before the ROUTING block. The declaration names both required elements of the C-38 pairing contract and their equivalence sets: `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER: {DEVIATION: | OVERRIDE:}] + [POSITIONAL-VOCAB: {precedes | before | follows | after}]`. C-38: routing line unchanged (`DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.`) -- DEVIATION: (deviation marker) + "precedes" (positional vocabulary) coexist on same line. C-38 PASS. C-40: pairing contract declared as structural rule before the routing block fires; both named elements present with equivalence sets; R18-confirmed form-neutrality (OVERRIDE: = DEVIATION:, "before" = "precedes") is visible without rubric cross-reference because the declaration enumerates the equivalence sets. C-40 PASS. C-39: no AMEND-HALT declaration -- N/S -- -1. Denominator: /32. All 31 prior criteria carry. Expected: 32/32 = 100.00. Confirms BRANCH-RULE pre-routing declaration as C-40 mechanism; tests that named equivalence sets in declaration satisfy the form-neutrality visibility condition.

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

BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER: {DEVIATION: | OVERRIDE:}] + [POSITIONAL-VOCAB: {precedes | before | follows | after}]

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

## V-05 -- Combined C-39 + C-40: full /33 denominator ceiling probe

**Axis**: Lifecycle emphasis + role sequence (combined -- C-39 declaration architecture + C-40 pairing contract)
**Hypothesis**: Both declarations present. `AMEND-HALT: "any of the above tokens is absent"` declared before AMEND; each path recalls it by token name (`{AMEND-HALT}`). `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER: {DEVIATION: | OVERRIDE:}] + [POSITIONAL-VOCAB: {precedes | before | follows | after}]` declared before the ROUTING block. C-37 PASS (uniform via declaration). C-39 PASS (declaration + token recall at all three paths). C-38 PASS (DEVIATION: + "precedes" on routing line, unchanged). C-40 PASS (BRANCH-RULE declared before routing fires, equivalence sets named). All 31 prior criteria carry. Both gate exclusions absent: full /33 denominator. Expected: 33/33 = 100.00. Full v17 ceiling probe. Tests that adding both declaration mechanisms simultaneously produces no unexpected criterion interactions.

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

BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER: {DEVIATION: | OVERRIDE:}] + [POSITIONAL-VOCAB: {precedes | before | follows | after}]

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

AMEND-HALT: "any of the above tokens is absent"

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
**HALT -- do not extend matrix if {AMEND-HALT}.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if {AMEND-HALT}.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if {AMEND-HALT}.**

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
| C-31 routing vocabulary positionally descriptive | PASS | PASS | PASS | PASS | PASS |
| C-32 routing scope declared deviation-only | PASS | PASS | PASS | PASS | PASS |
| C-33 BODY-ORDER-LAYER token | PASS | PASS | PASS | PASS | PASS |
| C-34 AMEND enumeration in separable block | PASS | PASS | PASS | PASS | PASS |
| C-35 HALT uses positional reference | PASS | PASS | PASS | PASS | PASS |
| C-36 engineering branch carries deviation marker | PASS | PASS | PASS | PASS | PASS |
| C-37 HALT phrase uniform across AMEND paths | PASS | PASS | PASS | PASS | PASS |
| C-38 branch pairs deviation marker + positional vocabulary | PASS | PASS | PASS | PASS | PASS |
| **C-39 HALT phrase declared as canonical token, recalled by name** | **N/S** | **PASS** | **FAIL** | **N/S** | **PASS** |
| **C-40 pairing contract declared before routing block** | **N/S** | **N/S** | **N/S** | **PASS** | **PASS** |

### Key results to watch

**V-01 on C-39 and C-40 (both N/S)**: No declaration tokens present. Both gates excluded -- denominator /31. Establishes v17 /33 base - 2 = /31 as the R18 carry-forward denominator. All 31 criteria PASS -- 100.00.

**V-02 on C-39 (AMEND-HALT declared + {AMEND-HALT} recalled at each path)**: Declaration before AMEND, token-name recall at all three paths. C-37 PASS (declaration-enforced uniformity). C-39 PASS. Denominator /32. Expected: 100.00. Primary C-39 mechanism confirmation.

**V-03 on C-39 (AMEND-HALT declared + literal phrase at each path)**: Declaration present before AMEND. Paths use "any of the above tokens is absent" as a literal string. C-37 PASS (uniform literal phrase). C-39 FAIL (token-name recall absent -- literal reproduction of declared value is not token recall). Denominator /32. Pass count: 31. Expected: 99.69. Canonical `c39-declaration-architecture` failure probe: declaration presence alone is insufficient; token-name recall at each path is the gate.

**V-04 on C-40 (BRANCH-RULE declared before routing block)**: BRANCH-RULE names [DEVIATION-MARKER] and [POSITIONAL-VOCAB] with equivalence sets before ROUTING fires. C-38 PASS (routing line unchanged). C-40 PASS. Denominator /32. Expected: 100.00. Confirms pre-routing declaration with named pairing contract satisfies C-40; equivalence set enumeration makes form-neutrality visible without rubric cross-reference.

**V-05 on C-39 + C-40 (both declared)**: Full /33 denominator. AMEND-HALT + BRANCH-RULE both present. C-37 PASS, C-39 PASS, C-38 PASS, C-40 PASS. 33/33 -- 100.00. Full v17 ceiling. Interaction test: two declaration mechanisms introduced simultaneously; each must independently satisfy its criterion without corrupting the other.
