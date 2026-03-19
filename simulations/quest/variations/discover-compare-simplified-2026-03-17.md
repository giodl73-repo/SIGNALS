---

## Simplified prompt body

```
Option A: {option_a}
Option B: {option_b}

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.
Token: `BODY-ORDER-LAYER: active`

---

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-B: {rating} -- {one sentence}`

---

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH.

Token: `INERT-A: {rating} -- {mechanism}`

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH.

Token: `INERT-B: {rating} -- {mechanism}`

---

REG-framed.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

REG-framed.

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

**HALT -- do not proceed if any token is absent.**

---

BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER] + [POSITIONAL-VOCAB]

ROUTING: deviation from BODY ORDER only.
DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.

RECOMMENDATION:

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

DECISION MATRIX:

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | N/A | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."

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

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if {AMEND-HALT}.**
```

---

## Simplification report

**18 removals across three categories:**

**Orientation/redundancy (items 1-2, 16):** Opening skill label, "use exact token names" preview, output artifact path — 28 words. None map to any criterion.

**Flavor/quality hints (items 3-7, 12, 17-18):** "Independent of Option A" on FEAS-B, "from above" in TOKEN RECALLs, "may differ from Option A's", mechanism-naming instructions, "Concrete differentiator", "Top 2 risks", "Rate each" — 30 words. These coach quality but no criterion tests for them; the slot formats already imply the same constraints.

**Redundant execution guidance (items 8-11, 13-15):** Recovery text in HALT, TOKEN RECALL at RECOMMENDATION (not an inertia phase per C-13), build-neither second sentence, matrix Inertia cell prose, Weight/Override post-gate execution instructions — 61 words. The mechanisms (HALT instruction, AMEND slot structure, matrix template) already carry the operative load.

**Verification: all essential criteria still pass.** The FAULT directives (not the flavor instructions) are what enforce C-02 inertia independence. The AMEND slot structure (not execution instructions) is what satisfies C-07. The HALT keyword (not recovery guidance) is what satisfies C-16. No aspirational criterion regresses: C-13 requires the no-paraphrase mandate at point of use, which "do not paraphrase" satisfies without "from above."

```json
{"simplified_word_count": 418, "original_word_count": 537, "all_essential_still_pass": true}
```
s phase; routing block + REG-framed instructions govern register. |
| 11 | `Name override condition or revise RECOMMENDATION above to Neither.` | 9 | C-05 pass = "must surface the question." First sentence surfaces it. Second is post-surfacing guidance. |
| 12 | `Concrete differentiator.` (COMP-A) | 2 | C-01 requires competitive coverage; no criterion requires "concrete" qualifier. |
| 13 | `this IS the anchor` -> `N/A` (matrix Inertia row) | 3 net | C-08 satisfied by column header "Option 0: ANCHOR[0]". Cell content is explanatory prose. |
| 14 | `Re-score from tokens. Update RECOMMENDATION if it changes.` (Weight) | 8 | C-07 passes on slot structure. Post-gate execution instruction. |
| 15 | `Re-render DECISION MATRIX labels and RECOMMENDATION framing.` (Override) | 7 | Same as #14. |
| 16 | `Output artifact: \`simulations/discover/compare/{topic}-compare-{date}.md\`` | 8 | No rubric criterion. Storage instruction. |
| 17 | `Rate each.` (RISK-A) | 2 | `{risk1/rating}, {risk2/rating}` slot implies rating. |
| 18 | `Top 2 risks.` from RISK-A and RISK-B | 6 | No criterion specifies count; slot format implies two. |
| **Total** | | **119** | |

### Essential criteria check (all must pass)

| Criterion | Verdict | Notes |
|-----------|---------|-------|
| C-01 bilateral dimensions | PASS | FEAS/INERT/RISK/COMP tokens for A and B all present. |
| C-02 independent inertia | PASS | FAULT directives at each inertia site enforce independence; "may differ" flavor text was not the mechanism. |
| C-03 decision matrix | PASS | Matrix template unchanged. |
| C-04 explicit recommendation | PASS | "Recommendation: Option A / B / Neither / Conditional on {X}" unchanged. |

### Recommended criteria check

| Criterion | Verdict | Notes |
|-----------|---------|-------|
| C-05 build/no-build gate | PASS | First sentence of build-neither block surfaces the question. Second sentence (removed) was post-surfacing guidance. |
| C-06 differentiated risks | PASS | "Distinct from RISK-A or explain overlap." retained for RISK-B. |
| C-07 actionable AMEND | PASS | All three AMEND paths have token slots + ledger + HALT. Add-C execution instruction retained. |

### Aspirational criteria -- tricky checks

| Criterion | Verdict | Notes |
|-----------|---------|-------|
| C-09 audience register | PASS | BODY ORDER + ROUTING block + REG-framed instructions throughout. TOKEN RECALL at RECOMMENDATION was redundant, not the mechanism. |
| C-13 verbatim anchor recall | PASS | "reproduce exact sentence -- do not paraphrase" retained at all inertia sites. "from above" was positional flavor, not required by C-13. |
| C-16 blocking ledger gate | PASS | "HALT -- do not proceed if any token is absent." retained; recovery instructions removed. |
| C-17 output compressed | PASS | Removing explanatory phrases increases C-17 score. |
| C-39 HALT declared as token | PASS | AMEND-HALT declared before AMEND, recalled as {AMEND-HALT} at all three paths. Unchanged. |
| C-40 pairing contract declared | PASS | BRANCH-RULE with [DEVIATION-MARKER] + [POSITIONAL-VOCAB] unchanged. |

All 33 criteria that scored in V-02 still pass. **all_essential_still_pass: true**
