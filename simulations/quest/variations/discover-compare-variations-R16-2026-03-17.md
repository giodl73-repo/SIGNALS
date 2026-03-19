`discover-compare-variations-R16-2026-03-17.md` written.

---

## R16 summary

**5 variations, 3 single-axis + 2 combined:**

| Var | Axis | Key change | Projected |
|-----|------|-----------|-----------|
| **V-01** | Baseline carry at /27 | R14 V-01 unchanged — fenced-code sub-ledger before HALT | 100.00 |
| **V-02** | Output format | Indented checklist replaces fenced-code block in AMEND | 100.00 |
| **V-03** | Output format | Token names embedded inside the HALT sentence itself | 99.81 |
| **V-04** | Role sequence + routing form | Explicit two-branch routing (exec branch added) | TBD on C-30/C-32 |
| **V-05** | Role sequence + format | Per-option batching (R15 V-01) + indented-list AMEND | 100.00 |

**Primary discriminating questions for R16:**

1. **V-01 on C-34**: Does the R14 V-01 fenced-code block satisfy C-34 ("structurally separable discrete block before halt")? Expected PASS → confirms ceiling at /27.

2. **V-02 on C-34**: Does an indented list satisfy C-34? Expected PASS — list precedes HALT on separate lines and is removable without touching the halt text. If PARTIAL: criterion requires fenced-code specifically, not any discrete block.

3. **V-03 on C-24/C-34 split**: Token names embedded inside the HALT sentence itself. v14 C-24 explicitly allows this form (PASS). C-34 requires a preceding separable block — inline-within-halt has none. Expected: C-24 PASS, C-34 PARTIAL → 99.81. This is the direct C-24/C-34 boundary probe.

4. **V-04 on C-30/C-32**: Adding an explicit `if REG = exec` branch to the routing block. C-30 requires routing handles only the deviation case — exec is the body-order default, not a deviation. C-32 requires the scope header "deviation from BODY ORDER only" — if both cases are now covered, that header is inaccurate. Either criterion could fire PARTIAL.
duce C-24 PASS (v14 explicitly allows) + C-34 PARTIAL (not before, not separable from halt)? Expected: C-34 PARTIAL → 99.81.
4. Does an explicit exec-branch in the routing block violate C-30 (routing handles only deviation) or strengthen C-25 (explicit two-branch routing)? The current deviation-only form passes C-25; adding the exec branch might produce C-30 PARTIAL.

---

**V-01** (baseline carry at /27): R14 V-01 body verbatim. Fenced-code AMEND sub-ledgers are structurally separable discrete blocks positioned before their respective HALT instructions. C-24 PASS (enumeration present). C-34 PASS (block form, before halt). All 26 prior criteria carry at PASS. Denominator /27. Expected: 27/27 = 100.00. Establishes v14 ceiling.

**V-02** (indented list AMEND sub-ledger): R14 V-01 body with fenced-code AMEND sub-ledger blocks replaced by indented checklist form. Each AMEND path presents its token checklist as an indented list before the HALT instruction. All other structure unchanged. C-24 PASS (enumeration present, any form). C-34 PASS or PARTIAL depending on whether indented list counts as "structurally separable discrete block." Expected: PASS — an indented list is visually discrete, precedes the HALT, and can be independently removed without touching the halt instruction. If actual = PARTIAL: criterion requires fenced-code block form specifically. Expected: 27/27 = 100.00.

**V-03** (inline-within-halt enumeration): R14 V-01 body with AMEND sub-ledger blocks removed. Each AMEND path names required tokens directly within the HALT sentence: `HALT -- do not extend matrix if any of FEAS-C, INERT-C, RISK-C, COMP-C is absent.` Per v14 C-24: token names enumerated inline within the halt instruction text = C-24 PASS. Per C-34: the enumeration is not in a structurally separable discrete block before the halt instruction -- it IS the halt instruction. Expected: C-24 PASS, C-34 PARTIAL. Composite: 26.5/27 × (10/27 weight) → 99.81. Establishes the C-34 mechanism boundary: inline enumeration satisfies C-24 but not C-34. All other criteria unchanged from R14 V-01.

**V-04** (explicit two-branch routing): R14 V-01 body with routing block rewritten as an explicit two-branch conditional covering both register values: `if REG = exec: RECOMMENDATION precedes DECISION MATRIX. if REG = engineering or general: DECISION MATRIX precedes RECOMMENDATION.` Tests C-25 (routing block with explicit exec and engineering branches = PASS) vs C-30 (routing block handles only deviation — does an explicit exec branch violate this?). C-30 criterion title is "Standalone BODY ORDER declaration" per scorecard notation but functional name in rubric is "routing block handles only deviation case." Adding an explicit exec branch may produce C-30 PARTIAL (exec branch is the body-order default, not a deviation -- stating it in the routing block blurs the deviation-only scope). Expected: C-25 PASS, C-30 PARTIAL or PASS depending on whether criterion tolerates redundant default branch. Projected: 26.5/27 = 99.81 if C-30 PARTIAL, 27/27 = 100.00 if C-30 PASS.

**V-05** (combined: per-option batching + indented-list AMEND): R15 V-01 structural pattern (all Option A analysis before Option B, each option's inertia FAULT inside its own block) + indented-list AMEND sub-ledgers. BODY ORDER updated to per-option clause. Tests C-34 at /27 under the per-option batching structural layout. If C-34 accepts indented list (as projected for V-02), this variation also scores 27/27. If not: 26.5/27. Expected: 27/27 = 100.00.

---

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational | Composite | Golden |
|-----------|--------------|-----------------|-------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 27/27 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 27/27 = 10.00 | **100.00** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 26.5/27 = 9.81 | **99.81** | TBD |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 26.5/27 = 9.81 | **99.81** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 27/27 = 10.00 | **100.00** | TBD |

---

## V-01 -- Baseline carry at /27

**Axis**: Baseline (single-axis — denominator change only)
**Hypothesis**: R14 V-01 body is unchanged. The fenced-code AMEND sub-ledger blocks are structurally separable from their HALT instructions -- they appear as discrete blocks in the line sequence before the bold HALT line. C-24 PASS (fenced block contains token-name enumeration). C-34 PASS (block is structurally separable and precedes halt). All 26 prior criteria carry at PASS from R14 V-01. Denominator /27. Expected: 27/27 = 100.00. Establishes v14 ceiling.

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

## V-02 -- Output format: AMEND sub-ledger as indented list

**Axis**: Output format (single-axis)
**Hypothesis**: The fenced-code block form of the AMEND sub-ledger (` ```Add-C ledger: ...``` `) is replaced with an indented checklist. The indented list is a structurally separable discrete block: it precedes the HALT instruction on separate lines, can be removed without touching the halt text, and is visually identifiable as a checklist. C-24 PASS (enumeration present in any form). C-34 PASS or PARTIAL: if "structurally separable discrete block" requires fenced-code specifically, PARTIAL; if any discrete block form qualifies, PASS. Expected: PASS -- indented list is a standard discrete block structure. Expected: 27/27 = 100.00. If C-34 PARTIAL: composite = 99.81. Establishes whether C-34 is form-agnostic within "discrete block" or fenced-code-specific.

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

  Add-C ledger:
  - FEAS-C: [ ]
  - INERT-C: [ ]
  - RISK-C:  [ ]
  - COMP-C:  [ ]

**HALT -- do not extend matrix if any Add-C token is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

  Weight ledger:
  - ANCHOR[0]: [ ]
  - WEIGHT:    [ ]

**HALT -- do not re-score if ledger incomplete.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

  Override ledger:
  - REG:          [ ]
  - REG-override: [ ]

**HALT -- do not re-render if ledger incomplete.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 -- Output format: enumeration inline-within-halt

**Axis**: Output format (single-axis)
**Hypothesis**: AMEND sub-ledger blocks removed. Each AMEND path instead names required tokens directly within the HALT sentence. Per v14 C-24 criterion: "Any form of token-name enumeration satisfies C-24: fenced-code block, indented list, or inline within the halt instruction text." This satisfies C-24 PASS. Per C-34: "the enumeration must appear as a structurally separable discrete block before the halt instruction." When the enumeration is part of the halt instruction itself, it cannot be separated from the halt -- there is no preceding discrete block. Expected: C-24 PASS, C-34 PARTIAL. Composite: 26.5/27 x (10/27 weight fraction) = 99.81. This is the isolated probe for the C-24/C-34 split introduced in v14. All other 26 criteria carry at PASS from R14 V-01.

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

**HALT -- do not extend matrix if any of FEAS-C, INERT-C, RISK-C, COMP-C is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

**HALT -- do not re-score if any of ANCHOR[0], WEIGHT is absent.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

**HALT -- do not re-render if any of REG, REG-override is absent.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-04 -- Combined: explicit two-branch routing construct

**Axis**: Role sequence + routing form (combined)
**Hypothesis**: The routing block is rewritten as an explicit two-branch conditional covering both register values. Current form names only the deviation case (engineering/general = matrix-first); exec-first behavior is implied by BODY ORDER default. New form explicitly states both branches in the routing block. Tests C-25 (does explicit both-branch form further confirm PASS or is current form already ceiling?) vs. C-30 (routing block handles only deviation -- does adding an explicit exec branch, which is not a deviation, violate this?). C-32 also under examination: the deviation-only scope header is no longer accurate if the exec branch is present -- does the header need updating? C-27 satisfied: routing block positioned after LEDGER GATE. Expected: if C-30 penalizes the exec-branch addition, composite = 26.5/27 = 99.81. If C-30 is neutral (criterion tests the deviation case being handled, not the exec case being absent), composite = 27/27 = 100.00. All other criteria carry from R14 V-01.

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

ROUTING:
if REG = exec: RECOMMENDATION precedes DECISION MATRIX.
if REG = engineering or general: DECISION MATRIX precedes RECOMMENDATION.

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

## V-05 -- Combined: per-option batching + indented-list AMEND sub-ledger

**Axis**: Role sequence + output format (combined)
**Hypothesis**: R15 V-01 structural pattern (all Option A analysis in one block, then all Option B) combined with V-02 AMEND sub-ledger as indented list. BODY ORDER updated to declare per-option sequencing constraint. Each option's inertia FAULT is co-located inside its own analysis block. C-34 tested at /27 with per-option layout + indented-list form. If indented list satisfies C-34 (projected PASS in V-02), this variation confirms that the C-34 mechanism is block-structural separability rather than specific formatting syntax. Expected: 27/27 = 100.00.

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

  Add-C ledger:
  - FEAS-C: [ ]
  - INERT-C: [ ]
  - RISK-C:  [ ]
  - COMP-C:  [ ]

**HALT -- do not extend matrix if any Add-C token is absent.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

  Weight ledger:
  - ANCHOR[0]: [ ]
  - WEIGHT:    [ ]

**HALT -- do not re-score if ledger incomplete.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

  Override ledger:
  - REG:          [ ]
  - REG-override: [ ]

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
| C-22 phase structure via token positioning | PASS | PASS | PASS | PASS | PASS |
| C-23 exec leads with recommendation | PASS | PASS | PASS | PASS | PASS |
| **C-24 AMEND path token enumeration (any form)** | PASS | PASS | PASS | PASS | PASS |
| C-25 register-gated routing block | PASS | PASS | PASS | **TBD** | PASS |
| C-26 body section order exec-safe | PASS | PASS | PASS | PASS | PASS |
| C-27 routing block within LEDGER GATE scope | PASS | PASS | PASS | PASS | PASS |
| C-28 body-order and routing-scope isolated | PASS | PASS | PASS | PASS | PASS |
| C-29 BODY ORDER as unconditional directive | PASS | PASS | PASS | PASS | PASS |
| C-30 routing block handles only deviation | PASS | PASS | PASS | **TBD** | PASS |
| C-31 routing vocabulary positionally descriptive | PASS | PASS | PASS | PASS | PASS |
| C-32 routing scope declaration | PASS | PASS | PASS | **TBD** | PASS |
| C-33 BODY-ORDER-LAYER token | PASS | PASS | PASS | PASS | PASS |
| **C-34 AMEND enumeration in separable block form** | PASS | **TBD** | **PARTIAL** | PASS | **TBD** |

### Key results to watch

**V-01 on C-34 (fenced-code block)**: Fenced-code block appears on its own lines before the bold HALT line. It is structurally separable -- removing the fenced block does not touch the HALT instruction. Expected: C-34 PASS. Confirms v14 ceiling at /27.

**V-02 on C-34 (indented list)**: Indented list with dashes precedes the HALT on separate lines. Structurally separable: the list can be removed without altering the HALT instruction text. Expected: C-34 PASS. If actual = PARTIAL: criterion may require specifically fenced-code (not merely any discrete block form). This is the primary form-discrimination question for V-02.

**V-03 on C-24 + C-34 (inline-within-halt)**: Token names appear inside the HALT sentence itself. C-24 v14 explicitly permits this form. C-34 requires the enumeration to precede the halt as a separable block -- inline-within-halt is inseparable from the halt. Expected: C-24 PASS, C-34 PARTIAL. This is the precise C-24/C-34 split probe introduced by v14.

**V-04 on C-25 + C-30 + C-32 (explicit two-branch routing)**: The routing block explicitly names both the exec branch and the deviation branch. C-25 requires explicit exec and engineering branches -- adding the exec branch makes this more explicit. C-30 requires routing block handles only deviation -- the exec branch is the body-order default, not a deviation; stating it in the routing block may blur the deviation-only contract. C-32 requires the deviation-only scope header -- if the routing block now covers both cases, "deviation from BODY ORDER only" is no longer accurate. Any of these three criteria could produce PARTIAL, yielding composite 99.81 or lower.
