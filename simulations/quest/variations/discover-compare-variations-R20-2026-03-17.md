**`discover-compare-variations-R20-2026-03-17.md` written.**

---

## R20 design summary

All five variations are at the **full /33 denominator** — unlike R19 where some variations had C-39 or C-40 excluded. Every variation includes both a HALT declaration and a BRANCH-RULE (in some form), so failures are scored at 0, not gated out.

| Var | Axis | Key mutation | C-39 | C-40 | Projected |
|-----|------|-------------|------|------|-----------|
| **V-01** | Lifecycle emphasis | Override path uses literal phrase; Add-C + Weight use `{AMEND-HALT}` | FAIL | PASS | **99.70** |
| **V-02** | Role sequence | BRANCH-RULE without equivalence sets | PASS | PASS (probe) | **100.00** |
| **V-03** | Lifecycle emphasis | AMEND-HALT placed *after* "AMEND:" header | FAIL | PASS | **99.70** |
| **V-04** | Phrasing register | `PATH-HALT` instead of `AMEND-HALT` | PASS | PASS | **100.00** |
| **V-05** | Role sequence | BRANCH-RULE names only `[DEVIATION-MARKER]` | PASS | FAIL | **99.70** |

---

**What each variation discriminates:**

- **V-01** — C-37 PASS vs C-39 FAIL are simultaneously achievable when one path uses the literal value rather than the token name. The "one or more" clause in C-39 applies even to a single non-recall path. Different failure root cause from R19 V-03 (which had all three paths using literal).

- **V-02** — Tests whether equivalence sets (`{DEVIATION: | OVERRIDE:}`, `{precedes | before | follows | after}`) are required for C-40 PASS or just enhance visibility. Expected: C-40 PASS on minimal form, confirming equivalence sets are optional.

- **V-03** — Isolates C-39's two independent conditions: `{AMEND-HALT}` token recall is *present and correct* at all three paths, but the declaration is placed inside the AMEND phase rather than before it. Timing gate fails independently of encoding.

- **V-04** — C-39 is form-neutral on token name. `PATH-HALT` satisfies the declaration architecture just as `AMEND-HALT` does. The rubric's "e.g., AMEND-HALT" is illustrative.

- **V-05** — C-38 PASS (routing line has both elements by inspection) and C-40 FAIL (declaration names only one element) are simultaneously achievable. The two criteria are independently scored — C-40 is not co-scored with C-38.
pline independently).

**V-02** (C-40 minimal declaration): R19 V-04 used the full form with equivalence sets enumerated. V-02 strips the equivalence sets, leaving `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER] + [POSITIONAL-VOCAB]`. C-40 pass condition: "Declaration present and branch satisfies both named elements = pass." Equivalence set enumeration is described as making form-neutrality *visible without rubric cross-reference* — a visibility property, not a pass gate. Expected: C-40 PASS on minimal form. Score: 33/33 = 100.00. Confirms equivalence sets are optional enhancement, not required for C-40.

**V-03** (C-39 declaration timing): C-39 requires the phrase to be declared "before the AMEND phase." V-03 places `AMEND-HALT: "any of the above tokens is absent"` on the line immediately after "AMEND:" — inside the AMEND phase, not before it. All three paths use `{AMEND-HALT}` (token-name recall present and correct). The gate is declaration position, not token-name syntax. C-39 FAIL: before-phase timing unmet. C-37 PASS: all three resolved phrases identical. Score: 32/33 = 99.70. Isolates the two C-39 conditions: before-phase timing AND token-name recall are independently required.

**V-04** (C-39 form-neutral token name): The rubric uses `AMEND-HALT` as an example (`e.g., AMEND-HALT: "..."`). The C-39 mechanism is declaration-before-use architecture: declare a named token, recall it by that name at each path. The specific token name is not the gate. V-04 uses `PATH-HALT: "any of the above tokens is absent"`; all three paths recall `{PATH-HALT}`. Expected: C-39 PASS. Score: 33/33 = 100.00. Confirms form-neutrality extends to the HALT token name itself.

**V-05** (C-40 partial declaration): C-40 requires "naming both required elements." V-05 declares `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER]` — only one of two required elements. C-38: routing line unchanged; both DEVIATION: and "precedes" present on the branch instruction. C-38 PASS. C-40: POSITIONAL-VOCAB absent from declaration — "both required elements" gate not satisfied. C-40 FAIL. Score: 32/33 = 99.70. Establishes that C-38 PASS (line-level coexistence) and C-40 FAIL (incomplete declaration) are simultaneously achievable.

---

**Open discrimination questions:**

1. V-01: Does C-37 PASS when 2 paths use `{AMEND-HALT}` and 1 uses literal identical value? Expected: yes — C-37 measures resolved-value uniformity, not encoding form. C-39 still FAIL.
2. V-02: Does minimal BRANCH-RULE without equivalence sets satisfy C-40? Expected: PASS — equivalence sets are visibility enhancement only.
3. V-03: Does `{AMEND-HALT}` recall fail C-39 when declaration is placed inside the AMEND phase? Expected: yes — timing condition is independently required.
4. V-04: Does `{PATH-HALT}` token name satisfy C-39 architecture? Expected: yes — token name is form-neutral.
5. V-05: Does BRANCH-RULE naming only [DEVIATION-MARKER] fail C-40? Expected: yes — both elements required in declaration.

---

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational | Composite | Golden |
|-----------|--------------|-----------------|-------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 32/33 = 9.70 | **99.70** | No |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 33/33 = 10.00 | **100.00** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 32/33 = 9.70 | **99.70** | No |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 33/33 = 10.00 | **100.00** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 32/33 = 9.70 | **99.70** | No |

---

## V-01 -- C-39 asymmetric recall failure: Override path uses literal phrase

**Axis**: Lifecycle emphasis (C-39 partial recall -- one-of-three paths omits token-name recall)
**Hypothesis**: `AMEND-HALT: "any of the above tokens is absent"` is declared correctly before AMEND. Add-C and Weight paths recall it by token name (`{AMEND-HALT}`). Override path uses the literal phrase "any of the above tokens is absent" instead of `{AMEND-HALT}`. C-37: all three resolved halt phrases are identical -- the literal on Override and the resolved value of `{AMEND-HALT}` on the other two are the same string. C-37 PASS. C-39: rubric states "Declaration present but one or more paths omit the token reference = C-39 FAIL" -- one path omits token reference. C-39 FAIL. C-40: BRANCH-RULE with both elements + equivalence sets unchanged. C-40 PASS. Denominator: /33. 32 criteria pass. Aspirational: 32/33 x 10 = 9.70. Composite: **99.70**. Discriminates C-37 (resolved-value uniformity) from C-39 (token-encoding discipline); confirms "one or more" applies to single-path failure.

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
**HALT -- do not re-render if any of the above tokens is absent.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 -- C-40 minimal declaration: BRANCH-RULE without equivalence sets

**Axis**: Role sequence (C-40 minimal form -- both elements named, equivalence sets absent)
**Hypothesis**: `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER] + [POSITIONAL-VOCAB]` is declared before the ROUTING block. Both required elements named; equivalence sets (`{DEVIATION: | OVERRIDE:}`, `{precedes | before | follows | after}`) stripped. C-40 pass condition: "Declaration present and branch satisfies both named elements = pass." The rubric describes equivalence set enumeration as making R18 form-neutrality "visible without rubric cross-reference" -- a visibility enhancement, not a pass gate. The routing line satisfies both named elements: DEVIATION: (deviation marker) + "precedes" (positional vocab). C-40 PASS. C-39: AMEND-HALT declared before AMEND; all three paths use `{AMEND-HALT}`. C-39 PASS. Denominator: /33. All 33 criteria pass. Composite: **100.00**. Confirms equivalence sets are optional for C-40 -- the "both elements named" gate does not require the equivalence set enumeration.

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

BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER] + [POSITIONAL-VOCAB]

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

## V-03 -- C-39 declaration timing failure: AMEND-HALT placed inside AMEND phase

**Axis**: Lifecycle emphasis (C-39 timing constraint -- declaration after AMEND phase opens)
**Hypothesis**: `AMEND-HALT: "any of the above tokens is absent"` is placed on the line immediately after the "AMEND:" header -- inside the AMEND phase rather than before it. All three paths use `{AMEND-HALT}` token recall (encoding correct). C-39 requires "declared as a named token before the AMEND phase." The AMEND phase opens at the AMEND: label; declaration placed after that label is inside the phase. C-39 FAIL: timing condition unmet despite correct token-name recall at all three paths. C-37: all three resolved halt phrases are identical. C-37 PASS. C-40: BRANCH-RULE with both elements + equivalence sets before ROUTING, unchanged. C-40 PASS. Denominator: /33. 32 criteria pass. Aspirational: 32/33 x 10 = 9.70. Composite: **99.70**. Isolates C-39's two independent conditions: token-name recall (met) and before-phase timing (failed) -- confirms both are separately required.

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
AMEND-HALT: "any of the above tokens is absent"

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

## V-04 -- C-39 form-neutral token name: PATH-HALT instead of AMEND-HALT

**Axis**: Phrasing register (C-39 form-neutral token naming -- alternative canonical token name)
**Hypothesis**: The rubric gives `AMEND-HALT: "any of the above tokens is absent"` as an example (`e.g., AMEND-HALT: "..."`). The C-39 mechanism is declaration-before-use architecture: declare a named token before the AMEND phase, recall it by that name at each path. The specific token name is not the gate. V-04 uses `PATH-HALT: "any of the above tokens is absent"` as the declaration token before AMEND; all three paths recall it as `{PATH-HALT}`. C-39 architecture fully satisfied: declaration before AMEND phase (timing met), token-name recall at all three paths (recall met). C-39 PASS. C-40: BRANCH-RULE with both elements + equivalence sets before ROUTING, unchanged. C-40 PASS. Denominator: /33. All 33 criteria pass. Composite: **100.00**. Confirms C-39 form-neutrality extends to the token name itself -- the declaration architecture satisfies C-39 regardless of whether the declared name is `AMEND-HALT`, `PATH-HALT`, or another identifier.

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

PATH-HALT: "any of the above tokens is absent"

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
**HALT -- do not extend matrix if {PATH-HALT}.**

Add Option C column to DECISION MATRIX. Update RECOMMENDATION.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if {PATH-HALT}.**

Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if {PATH-HALT}.**

Re-render DECISION MATRIX labels and RECOMMENDATION framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-05 -- C-40 partial declaration: BRANCH-RULE names only DEVIATION-MARKER

**Axis**: Role sequence (C-40 partial element declaration -- one of two required elements absent from declaration)
**Hypothesis**: `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER]` is declared before the ROUTING block -- only one of two required elements named; POSITIONAL-VOCAB absent. C-38: routing line unchanged (`DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.`). DEVIATION: (deviation marker) + "precedes" (positional vocabulary) both present on the routing line. C-38 PASS. C-40: rubric requires "Declaration present and branch satisfies both named elements = pass" -- but the pass condition requires the declaration itself to name both elements. A declaration naming only [DEVIATION-MARKER] does not satisfy "names both required elements as a structural rule." C-40 FAIL. C-39: AMEND-HALT declared before AMEND; all three paths use `{AMEND-HALT}`. C-39 PASS. Denominator: /33. 32 criteria pass. Aspirational: 32/33 x 10 = 9.70. Composite: **99.70**. Establishes that C-38 PASS (line-level coexistence by inspection) and C-40 FAIL (incomplete declaration) are simultaneously achievable -- C-40 extends C-38 independently and is not co-scored with it.

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

BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER]

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
| **C-39 HALT phrase declared as canonical token, recalled by name** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-40 pairing contract declared before routing block** | **PASS** | **PASS** | **PASS** | **PASS** | **FAIL** |

### Key results to watch

**V-01 on C-39 (one-of-three asymmetric recall failure)**: Add-C and Weight paths use `{AMEND-HALT}`; Override path uses literal phrase identical in value. C-37: resolved values all identical -- C-37 PASS. C-39: "one or more paths omit the token reference" -- C-39 FAIL. Score: 32/33 = 99.70. Confirms C-37 measures resolved-value uniformity while C-39 measures encoding discipline; a single non-recall path satisfies the "one or more" failure clause.

**V-02 on C-40 (minimal BRANCH-RULE without equivalence sets)**: Both required elements named in declaration; equivalence sets stripped. C-40 pass condition is declaration-present + both-named. Expected: C-40 PASS. Score: 33/33 = 100.00. Confirms equivalence sets are an optional visibility enhancement, not a C-40 gate requirement.

**V-03 on C-39 (declaration inside AMEND phase)**: AMEND-HALT placed after "AMEND:" header. All three paths use `{AMEND-HALT}` (token recall present and correct). C-39 FAIL: "before the AMEND phase" timing condition unmet despite correct encoding. Score: 32/33 = 99.70. Isolates C-39's two independent conditions: before-phase timing (failed here) and token-name recall (met here). Both are independently required.

**V-04 on C-39 (PATH-HALT token name)**: Alternative token name `PATH-HALT` used instead of `AMEND-HALT`. All three paths recall `{PATH-HALT}`. Expected: C-39 PASS. Score: 33/33 = 100.00. Confirms C-39 form-neutrality on token name -- the "e.g., AMEND-HALT" in the rubric is illustrative, not prescriptive.

**V-05 on C-40 (partial BRANCH-RULE, one element only)**: `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER]` -- POSITIONAL-VOCAB absent. C-38: routing line satisfies both elements by inspection. C-38 PASS. C-40: declaration does not name both required elements. C-40 FAIL. Score: 32/33 = 99.70. Establishes C-38 PASS + C-40 FAIL as simultaneously achievable -- the two criteria are independently scored; C-40 extends C-38 without being co-scored.
