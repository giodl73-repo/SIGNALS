Written to `simulations/quest/variations/discover-compare-variations-R7-2026-03-17.md`.

---

## discover-compare R7 — Summary

**Root problem**: R6 V-05 is the 100/100 candidate under v5. v6 adds C-20 (path-scoped TOKEN RECALL) and C-21 (dual-polarity FAULT at AMEND paths), bumping the aspirational denominator /12 → /14.

**Open questions targeted by R7**:

| Var | Axis | Change from V-01 | C-20 | C-21 | Projected |
|-----|------|------------------|------|------|-----------|
| V-01 | Baseline | R6 V-05 exact | PASS | PASS | **100.00** |
| V-02 | Over-recall diagnostic | Register path recalls ANCHOR[0]+REG (R6 V-04) | PARTIAL | PASS | 99.64 |
| V-03 | Add-C REG recall | REG added to Add-C path | TESTING | PASS | 100.00 or 99.64 |
| V-04 | Weight REG recall | REG added to Weight path | TESTING | PASS | 100.00 or 99.64 |
| V-05 | C-21 FAULT form | Single-polarity FAULT at Weight | PASS | PARTIAL | 99.64 |

**Key discriminating questions**:
- **V-01 C-20**: Does ANCHOR[0]-only at Add-C/Weight satisfy "any register token required for execution," or does V-01 under-recall REG?
- **V-02 C-20**: Does C-20 fire as PARTIAL on R6 V-04's ANCHOR[0] over-recall at register path?
- **V-03/V-04 C-20**: Is REG operationally required at option-addition and weight paths? Answer determines the true minimal spec.
- **V-05 C-21**: Does single-polarity FAULT at one AMEND path score PARTIAL (expected) or FAIL (zero-tolerance)?
 |
| V-03 | Add-C REG recall | REG added to Add-C path | TESTING | PASS | 100.00 or 99.64 |
| V-04 | Weight REG recall | REG added to Weight path | TESTING | PASS | 100.00 or 99.64 |
| V-05 | C-21 FAULT form | Single-polarity FAULT at Weight path | PASS | PARTIAL | **99.64** |

**V-01 is the expected 100/100 candidate.** V-02 confirms C-20 catches over-recall. V-03/V-04 test
whether REG is operationally required at option-addition and weight paths (C-20 PASS or PARTIAL
depending on whether "any register token required for their execution" mandates path-local explicit
recall). V-05 confirms C-21 PARTIAL behavior when one AMEND path carries only a positive-mandate
FAULT.

### Composite scoring under v6 (aspirational /14)

- 4/4 essential = 60.00
- 3/3 recommended = 30.00
- aspirational: partial = 0.5, x/14 * 10
- 14/14 = 10.00 → composite **100.00**
- 13.5/14 = 9.64 → composite **99.64**

---

### Rubric coverage projection (v6 — 21 criteria, aspirational /14)

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
| C-09 audience primary flow | PASS | PASS | PASS | PASS | PASS |
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
| **C-20 path-scoped TOKEN RECALL** | **PASS** | **PARTIAL** | **TESTING** | **TESTING** | **PASS** |
| **C-21 FAULT propagates to AMEND** | **PASS** | **PASS** | **PASS** | **PASS** | **PARTIAL** |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/14) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 13.5/14 = 9.64 | **99.64** | YES |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 13.5/14 = 9.64 | **99.64** | YES |

*V-03 and V-04: TESTING = projected PASS if C-20 scorer reads REG as over-recall at those paths
(V-01's ANCHOR[0]-only form is the correct minimal). If scorer reads REG as required for execution:
V-03/V-04 PASS and V-01 drops to PARTIAL (under-recall at Add-C/Weight) — composites invert.*

---

### Key discriminating tests

**V-01 on C-20**: Primary signal. If PASS: R6 V-05's ANCHOR[0]-only form at Add-C/Weight is the
correct minimal spec. The "any register token required for their execution" clause is satisfied by
inherited Phase 0 context, not path-local explicit recall. If PARTIAL: REG must be explicitly
recalled at REG-framed AMEND paths and V-01 under-recalls.

**V-02 on C-20**: Confirms over-recall fires. Register path recalls ANCHOR[0] unnecessarily.
Expected PARTIAL. If PASS: C-20 does not penalize over-recall — the criterion is only about missing
tokens, not surplus tokens. Would require revising the C-20 pass condition.

**V-03 vs V-04 divergence**: If only one of {Add-C, Weight} requires REG recall, one TESTING result
will be PASS and the other PARTIAL. This would reveal that C-20's operational requirement differs
between path types — option-addition has different recall needs than weight re-scoring.

**V-05 on C-21**: Single-polarity Weight FAULT. Expected PARTIAL (2/3 dual-polarity paths correct).
If FAIL: C-21 applies a zero-tolerance rule — any path with deficient FAULT form collapses the
whole criterion. If PASS: positive mandate alone satisfies C-21 (dual-polarity form is overhead).

---

## V-01 — R6 V-05 Baseline

**Axis**: Baseline — R6 V-05 exact; no changes
**Hypothesis**: R6 V-05 was confirmed C-19 PASS under v5. Under v6, C-20 and C-21 are new. C-21 is
satisfied: all three AMEND paths carry dual-polarity FAULTs. C-20 is the open question: each path
recalls only what its own execution requires — Register=REG, Add-C=ANCHOR[0], Weight=ANCHOR[0].
If "any register token required for their execution" at Add-C/Weight means REG is not required
(it is inherited from Phase 0, not recalled path-locally), V-01 satisfies C-20 → 100/100. If REG
must be explicitly recalled at REG-framed paths, V-01 under-recalls at Add-C and Weight → C-20
PARTIAL → 99.64. This is the R7 baseline and expected 100/100 candidate.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 — FRAME**

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo — one sentence, REG-framed}`

---

**PHASE 1A — FEASIBILITY: OPTION A**

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} — {one sentence}`

**PHASE 1B — FEASIBILITY: OPTION B**

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} — {one sentence}`

---

**PHASE 2A — INERTIA: OPTION A**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} — {mechanism}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism — may differ from Option A's.

Token: `INERT-B: {rating} — {mechanism}`

---

**PHASE 3A — RISK: OPTION A**

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**PHASE 3B — RISK: OPTION B**

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A — COMPETITIVE POSITIONING: OPTION A**

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

**PHASE 4B — COMPETITIVE POSITIONING: OPTION B**

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

**PHASE 5 — LEDGER GATE**

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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce missing token, return here,
verify all pass.

---

**PHASE 6 — DECISION MATRIX**

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

**PHASE 7 — BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or conclude Neither.

---

**PHASE 8 — RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 9 — AMEND**

**Add Option C:**

Token: `FEAS-C: {rating} — {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} — {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`
Add FEAS-C, INERT-C, RISK-C, COMP-C to LEDGER GATE. Add Option C column to Phase 6 matrix.
Update Phase 8 recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: apply multiplier to dimension scores only — do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only — do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 — C-20 Over-Recall Diagnostic (R6 V-04 form)

**Axis**: Lifecycle emphasis — Register override path recalls both REG and ANCHOR[0]; all other V-01
elements preserved verbatim
**Hypothesis**: R6 V-04 was the all-paths fix that passed C-19 under v5. Under v6, C-20 penalizes
over-recall: the register path does not involve status-quo evaluation, so ANCHOR[0] recall there
is spurious. V-02 reproduces R6 V-04 exactly to confirm C-20 fires on this form. Expected C-20
PARTIAL: register path recalls ANCHOR[0] (unnecessary) + REG (correct). If PARTIAL: C-20 correctly
identifies that the register-path recall set includes a token not required for its own execution.
If PASS: C-20 does not treat extra ANCHOR[0] at register path as over-recall — the C-20 pass
condition needs clarification. This variation is a diagnostic only — not a 100/100 candidate.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 — FRAME**

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo — one sentence, REG-framed}`

---

**PHASE 1A — FEASIBILITY: OPTION A**

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} — {one sentence}`

**PHASE 1B — FEASIBILITY: OPTION B**

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} — {one sentence}`

---

**PHASE 2A — INERTIA: OPTION A**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} — {mechanism}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism — may differ from Option A's.

Token: `INERT-B: {rating} — {mechanism}`

---

**PHASE 3A — RISK: OPTION A**

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**PHASE 3B — RISK: OPTION B**

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A — COMPETITIVE POSITIONING: OPTION A**

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

**PHASE 4B — COMPETITIVE POSITIONING: OPTION B**

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

**PHASE 5 — LEDGER GATE**

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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce missing token, return here,
verify all pass.

---

**PHASE 6 — DECISION MATRIX**

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

**PHASE 7 — BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or conclude Neither.

---

**PHASE 8 — RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 9 — AMEND**

**Add Option C:**

Token: `FEAS-C: {rating} — {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} — {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`
Add FEAS-C, INERT-C, RISK-C, COMP-C to LEDGER GATE. Add Option C column to Phase 6 matrix.
Update Phase 8 recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: apply multiplier to dimension scores only — do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: register override re-renders labels and framing only — do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 — Add-C Path REG Recall Added

**Axis**: Lifecycle emphasis — Add Option C path gains explicit TOKEN RECALL of REG; all other V-01
elements preserved verbatim
**Hypothesis**: V-01's Add-C path recalls ANCHOR[0] only. C-20 says option-addition paths recall
"ANCHOR[0] and any register token required for their execution." The Add-C path produces REG-framed
tokens (FEAS-C, INERT-C, etc.) — does producing these require explicit REG recall, or is the
inherited Phase 0 register sufficient? V-03 adds `TOKEN RECALL: REG = {restate original register}`
to the Add-C path (before ANCHOR[0]). If C-20 PASS: REG IS required for Add-C execution and V-01
was under-recalling at this path. If C-20 PARTIAL: adding REG here = over-recall (not operationally
required at option-addition) and V-01's ANCHOR[0]-only form was already correct. Determines whether
C-20's "and any register token required for execution" mandates path-local explicit REG recall at
option-addition paths.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 — FRAME**

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo — one sentence, REG-framed}`

---

**PHASE 1A — FEASIBILITY: OPTION A**

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} — {one sentence}`

**PHASE 1B — FEASIBILITY: OPTION B**

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} — {one sentence}`

---

**PHASE 2A — INERTIA: OPTION A**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} — {mechanism}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism — may differ from Option A's.

Token: `INERT-B: {rating} — {mechanism}`

---

**PHASE 3A — RISK: OPTION A**

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**PHASE 3B — RISK: OPTION B**

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A — COMPETITIVE POSITIONING: OPTION A**

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

**PHASE 4B — COMPETITIVE POSITIONING: OPTION B**

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

**PHASE 5 — LEDGER GATE**

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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce missing token, return here,
verify all pass.

---

**PHASE 6 — DECISION MATRIX**

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

**PHASE 7 — BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or conclude Neither.

---

**PHASE 8 — RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 9 — AMEND**

**Add Option C:**

TOKEN RECALL: `REG = {restate original register}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option C vs A or B comparison is an error.
Token: `FEAS-C: {rating} — {one sentence}`
Token: `INERT-C: {rating} — {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`
Add FEAS-C, INERT-C, RISK-C, COMP-C to LEDGER GATE. Add Option C column to Phase 6 matrix.
Update Phase 8 recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: apply multiplier to dimension scores only — do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only — do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-04 — Weight Path REG Recall Added

**Axis**: Lifecycle emphasis — Weight path gains explicit TOKEN RECALL of REG; all other V-01
elements preserved verbatim
**Hypothesis**: Mirrors V-03 but isolated to the Weight path. V-01's Weight path recalls ANCHOR[0]
only. C-20 says weight paths recall "ANCHOR[0] and any register token required for their execution."
Weight re-scoring re-ranks dimension scores — but the final recommendation update is REG-framed.
Does weight execution require REG to be operationally self-contained? V-04 adds
`TOKEN RECALL: REG = {restate original register}` to the Weight path (before ANCHOR[0]). If C-20
PASS: REG recall is correct here (the weight path must update the REG-framed recommendation —
explicit recall is required for self-containedness). If C-20 PARTIAL: this is over-recall — weight
re-scoring operates on numeric/rating tokens only, register framing is not a path-local concern.
V-03 and V-04 together bracket whether REG recall is needed at neither, one, or both of the non-
register AMEND paths — determining the exact minimal form that satisfies C-20.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 — FRAME**

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo — one sentence, REG-framed}`

---

**PHASE 1A — FEASIBILITY: OPTION A**

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} — {one sentence}`

**PHASE 1B — FEASIBILITY: OPTION B**

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} — {one sentence}`

---

**PHASE 2A — INERTIA: OPTION A**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} — {mechanism}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism — may differ from Option A's.

Token: `INERT-B: {rating} — {mechanism}`

---

**PHASE 3A — RISK: OPTION A**

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**PHASE 3B — RISK: OPTION B**

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A — COMPETITIVE POSITIONING: OPTION A**

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

**PHASE 4B — COMPETITIVE POSITIONING: OPTION B**

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

**PHASE 5 — LEDGER GATE**

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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce missing token, return here,
verify all pass.

---

**PHASE 6 — DECISION MATRIX**

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

**PHASE 7 — BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or conclude Neither.

---

**PHASE 8 — RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 9 — AMEND**

**Add Option C:**

Token: `FEAS-C: {rating} — {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} — {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`
Add FEAS-C, INERT-C, RISK-C, COMP-C to LEDGER GATE. Add Option C column to Phase 6 matrix.
Update Phase 8 recommendation.

**Weight {dimension}:**

TOKEN RECALL: `REG = {restate original register}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: apply multiplier to dimension scores only — do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only — do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-05 — C-21 FAULT Form Sensitivity (Single-Polarity at Weight)

**Axis**: Lifecycle emphasis — Weight path FAULT reduced to positive mandate only; all other V-01
elements preserved verbatim
**Hypothesis**: V-01 carries dual-polarity FAULTs at all three AMEND paths. C-21 requires each
amendment path to carry "a one-line FAULT encoding positive mandate + negative prohibition." V-05
changes the Weight path FAULT from:
  `FAULT: apply multiplier to dimension scores only — do not revise token values.`
to:
  `FAULT: apply multiplier to dimension scores only.`
This removes the negative prohibition leaving only the positive mandate. Add-C and Register paths
retain full dual-polarity form. C-21 pass condition: "All AMEND paths with dual-polarity FAULT =
pass. Some paths with dual-polarity FAULT, others with single-polarity or none = partial." Expected
C-21 PARTIAL: 2 of 3 paths correct. If PARTIAL: C-21 distinguishes full dual-polarity from single-
polarity at the path level — expected result. If FAIL: any single-polarity path triggers a zero-
tolerance failure on C-21 (not a partial) — would require revising the C-21 pass condition. If PASS:
positive mandate alone satisfies C-21 and the negative prohibition is optional overhead.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 — FRAME**

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo — one sentence, REG-framed}`

---

**PHASE 1A — FEASIBILITY: OPTION A**

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} — {one sentence}`

**PHASE 1B — FEASIBILITY: OPTION B**

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} — {one sentence}`

---

**PHASE 2A — INERTIA: OPTION A**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} — {mechanism}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism — may differ from Option A's.

Token: `INERT-B: {rating} — {mechanism}`

---

**PHASE 3A — RISK: OPTION A**

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**PHASE 3B — RISK: OPTION B**

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A — COMPETITIVE POSITIONING: OPTION A**

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

**PHASE 4B — COMPETITIVE POSITIONING: OPTION B**

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

**PHASE 5 — LEDGER GATE**

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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce missing token, return here,
verify all pass.

---

**PHASE 6 — DECISION MATRIX**

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

**PHASE 7 — BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or conclude Neither.

---

**PHASE 8 — RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 9 — AMEND**

**Add Option C:**

Token: `FEAS-C: {rating} — {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: compare against ANCHOR[0] only — Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} — {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`
Add FEAS-C, INERT-C, RISK-C, COMP-C to LEDGER GATE. Add Option C column to Phase 6 matrix.
Update Phase 8 recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: apply multiplier to dimension scores only.
Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only — do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
Re-render Phase 6 labels and Phase 8 framing.

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
| C-09 audience primary flow | PASS | PASS | PASS | PASS | PASS |
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
| **C-20 path-scoped TOKEN RECALL** | **PASS** | **PARTIAL** | **TESTING** | **TESTING** | **PASS** |
| **C-21 FAULT propagates to AMEND** | **PASS** | **PASS** | **PASS** | **PASS** | **PARTIAL** |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/14) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 13.5/14 = 9.64 | **99.64** | YES |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 13.5/14 = 9.64 | **99.64** | YES |

*V-03 and V-04: TESTING projected PASS (over-recall interpretation). If C-20 scorer reads REG as
required at those paths: V-01 drops to PARTIAL (under-recall) and V-03/V-04 become the 100/100 form.*

### Key results to watch

**V-01 on C-20**: Determines whether R6 V-05's ANCHOR[0]-only form at Add-C/Weight is the correct
minimal spec. If PASS: confirms V-01 as the R7 100/100 form. If PARTIAL: REG must be path-locally
recalled at option-addition and weight paths — V-03/V-04 are the candidates.

**V-02 on C-20**: Diagnostic. Expected PARTIAL (ANCHOR[0] over-recalled at register path). Confirms
C-20 fires correctly on R6 V-04. If PASS: C-20 does not penalize over-recall and the criterion
description needs revision.

**V-03 vs V-04 asymmetry**: If both TESTING, the question is whether Add-C and Weight have the same
operational recall requirements. If they differ: C-20 is path-type-specific rather than uniform
across non-register AMEND paths. One PASS + one PARTIAL would reveal the asymmetry.

**V-05 on C-21**: Confirms C-21 grading behavior for single-polarity FAULT. Expected PARTIAL.
If FAIL: C-21 applies zero-tolerance (any deficient path = full criterion failure). This would
tighten the pass condition description for R8.
