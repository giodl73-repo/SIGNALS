Written to `simulations/quest/variations/discover-compare-variations-R6-2026-03-17.md`.

---

## discover-compare R6 — Variations Summary

**Root problem**: R5 V-05 was the 100/100 candidate under v4 (17 criteria). v5 adds C-18 and C-19. C-18 is already satisfied by R5 V-05 (dual-polarity FAULT was the R5 discovery). C-19 is the new gap.

**C-19 gap in R5 V-05**: Only the "Add Option C" amendment path has inline TOKEN RECALL + FAULT. The Weight and Register override paths have neither. C-19 requires *each* amendment path to be self-contained → PARTIAL → composite 99.58 under v5.

### The 5 variations

| Var | Axis | Change | C-19 | Projected |
|-----|------|--------|------|-----------|
| V-01 | Baseline | R5 V-05 exact | PARTIAL | 99.58 |
| V-02 | Lifecycle — Weight path | TOKEN RECALL (ANCHOR[0]) + FAULT added to Weight only | PARTIAL | 99.58 |
| V-03 | Lifecycle — Register path | TOKEN RECALL (REG) + FAULT added to Register only | PARTIAL | 99.58 |
| V-04 | Lifecycle — all paths | TOKEN RECALL + FAULT on all three paths (REG+ANCHOR[0] at register) | **PASS** | **100.00** |
| V-05 | Lifecycle — minimal recall | Same as V-04 but Register path uses TOKEN RECALL of REG only | TESTING | 100.00 or 99.58 |

**New FAULT forms added** (both dual-polarity, consistent with C-18's pattern):
- Weight: `FAULT: apply multiplier to dimension scores only — do not revise token values.`
- Register: `FAULT: register override re-renders labels and framing only — do not revise analysis or ANCHOR[0].`

**V-04 is the expected 100/100 candidate.** V-05 tests whether ANCHOR[0] recall is structurally required at the register path or just REG alone is sufficient — determines the minimal TOKEN RECALL spec for C-19 PASS.
L: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
FAULT: apply multiplier to dimension scores only — do not revise token values.
```

Register override path adds:
```
TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only — do not revise analysis or ANCHOR[0].
```

Both are dual-polarity one-liners (positive mandate + negative prohibition), consistent with C-18's pattern.

### Projected composites (v5 rubric, /12 aspirational)

- V-01: C-18 PASS, C-19 PARTIAL → aspirational 11.5/12 = 9.58 → **composite 99.58**
- V-02: C-18 PASS, C-19 PARTIAL (1 of 3 paths fixed) → aspirational 11.5/12 = 9.58 → **composite 99.58**
- V-03: C-18 PASS, C-19 PARTIAL (1 of 3 paths fixed) → aspirational 11.5/12 = 9.58 → **composite 99.58**
- V-04: C-18 PASS, C-19 PASS → aspirational 12/12 = 10.00 → **composite 100.00**
- V-05: C-18 PASS, C-19 TESTING → aspirational 12/12 or 11.5/12 → **100.00 or 99.58**

### Key discriminating tests

- **V-01 on C-19**: Confirms that R5 V-05 (2 paths without TOKEN RECALL/FAULT) is PARTIAL, not FAIL. Sets the gap baseline.
- **V-02/V-03 on C-19**: Each isolates one path. C-19 requires all paths — adding one path in isolation should not move C-19 to PASS, only to PARTIAL in a different configuration.
- **V-04 on C-19**: All three paths equipped. Expected PASS. If PARTIAL: TOKEN RECALL or FAULT form is insufficient for weight/register paths.
- **V-05 on C-19**: Register path uses TOKEN RECALL of REG only (not ANCHOR[0]). If PASS: ANCHOR[0] recall is not required at register path — REG alone makes it self-contained. If PARTIAL: ANCHOR[0] is required at every path for full coverage.

### Rubric coverage projection (v5 — 19 criteria, aspirational /12)

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
| **C-19 AMEND self-contained** | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PASS** | **TESTING** |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/12) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 11.5/12 = 9.58 | **99.58** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 11.5/12 = 9.58 | **99.58** | YES |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 11.5/12 = 9.58 | **99.58** | YES |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 12/12 = 10.00 | **100.00** | YES |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 12/12 = 10.00 | **100.00** | YES |

*TESTING = projected PASS above. If C-19 PARTIAL in V-05: composite drops to 99.58.*

---

## V-01 — R5 V-05 Baseline

**Axis**: Baseline — exact R5 V-05 minimal viable form; no changes
**Hypothesis**: R5 V-05 was the 100/100 candidate under the v4 rubric. Under v5, C-18 and C-19 are new aspirational criteria. C-18 is already satisfied by V-05's dual-polarity FAULT form. C-19 requires all amendment paths to carry inline TOKEN RECALL + FAULT — but V-05's Weight and Register override paths have neither. Projected C-19 PARTIAL → composite 99.58. This variation establishes the gap baseline.

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

Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update recommendation if it changes.

**Override register:**

Token: `REG override: {new register}`
Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 — C-19 Weight Path Isolation

**Axis**: Lifecycle emphasis — TOKEN RECALL + FAULT added to Weight path only; all other V-01
elements preserved verbatim
**Hypothesis**: C-19 requires all amendment paths to carry inline TOKEN RECALL + FAULT. V-02 equips
only the Weight path. If C-19 remains PARTIAL (expected): partial path coverage is not sufficient.
Confirms that C-19 must be satisfied across all paths simultaneously, not path-by-path. The Weight
path TOKEN RECALL recalls ANCHOR[0] because re-scoring inertia requires the status quo basis.
Weight FAULT: `FAULT: apply multiplier to dimension scores only — do not revise token values.`
This is a dual-polarity directive (positive: apply multiplier to scores; negative: no token revision).
Register override path remains without TOKEN RECALL or FAULT — confirming that gap is still live.

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

Token: `REG override: {new register}`
Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 — C-19 Register Path Isolation

**Axis**: Lifecycle emphasis — TOKEN RECALL + FAULT added to Register override path only; all
other V-01 elements preserved verbatim
**Hypothesis**: V-02 equips only the Weight path. V-03 equips only the Register override path.
Both isolate a single path to confirm that partial coverage leaves C-19 PARTIAL. The Register
override path needs TOKEN RECALL of REG (original register) to be self-contained — knowing what
register was active before the override is required to execute the re-render without reading Phase 0.
Register FAULT: `FAULT: register override re-renders labels and framing only — do not revise
analysis or ANCHOR[0].` This is dual-polarity (positive: re-render labels/framing; negative: no
analysis revision). Weight path remains unequipped — confirming the gap remains at that path.

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

## V-04 — C-19 Full Fix (All Three Paths)

**Axes**: Lifecycle emphasis — TOKEN RECALL + FAULT added to all three amendment paths
**Hypothesis**: V-02 equips Weight only; V-03 equips Register only. V-04 equips all three. Expected
C-19 PASS: every amendment path carries its own inline TOKEN RECALL directives and FAULT
prohibitions. "Add Option C" path: unchanged from R5 V-05 — already had TOKEN RECALL + FAULT.
Weight path gains TOKEN RECALL of ANCHOR[0] + FAULT. Register path gains TOKEN RECALL of REG and
ANCHOR[0] + FAULT. ANCHOR[0] is recalled at Register path because a register override may prompt
re-framing of the anchor sentence — having the exact text inline makes that judgment possible
without returning to Phase 0. Each FAULT is a dual-polarity one-liner. If C-19 PASS: all-paths
coverage is sufficient. If PARTIAL: the TOKEN RECALL or FAULT form at one path is deficient.
This is the R6 100/100 candidate under v5.

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

## V-05 — C-19 Full Fix with Minimal TOKEN RECALL at Register Path

**Axis**: Lifecycle emphasis — same as V-04 but Register override path uses TOKEN RECALL of REG
only; ANCHOR[0] TOKEN RECALL is removed from that path
**Hypothesis**: V-04 recalls both REG and ANCHOR[0] at the Register override path. V-05 recalls
only REG. The question: is ANCHOR[0] recall required at the Register path for C-19 PASS, or is
REG alone sufficient to make the path "executable without re-reading primary phases"? Argument
for REG-only: register override does not involve status quo evaluation — only label and framing
re-render. REG recall is sufficient to know what changed and what to re-render; ANCHOR[0] content
does not drive the re-render. If C-19 PASS: ANCHOR[0] is not required at every path — TOKEN
RECALL requirements are path-specific. If C-19 PARTIAL: ANCHOR[0] must be recalled at every path
for consistent coverage. Impact: defines the minimal TOKEN RECALL spec for C-19-compliant AMEND.

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
| **C-19 AMEND self-contained** | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PASS** | **TESTING** |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/12) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 11.5/12 = 9.58 | **99.58** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 11.5/12 = 9.58 | **99.58** | YES |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 11.5/12 = 9.58 | **99.58** | YES |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 12/12 = 10.00 | **100.00** | YES |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 12/12 = 10.00 | **100.00** | YES |

*TESTING projected PASS. If C-19 PARTIAL in V-05: composite 99.58.*

### Key results to watch

**V-01 C-19**: PARTIAL confirms the gap. R5 V-05 equipped only the "Add Option C" path — Weight
and Register override paths had no TOKEN RECALL or FAULT. 1 of 3 paths equipped = PARTIAL, not PASS.

**V-02/V-03 on C-19 isolation**: Each equips exactly one of the deficient paths. C-19 requires
"each amendment path" — partial path coverage should remain PARTIAL. Confirms coverage must be
complete across all paths simultaneously.

**V-04 on C-19**: All three paths equipped. TOKEN RECALL + FAULT at Option C (unchanged), Weight
(ANCHOR[0] + FAULT), Register (REG + ANCHOR[0] + FAULT). If PASS: full three-path coverage
satisfies C-19. If PARTIAL: the TOKEN RECALL or FAULT form for a specific path is deficient.

**V-05 on C-19**: Register path uses TOKEN RECALL of REG only — ANCHOR[0] recalled at Add-C and
Weight paths but not at Register path. If PASS: TOKEN RECALL requirements are path-scoped —
Register path's self-containedness does not require ANCHOR[0]. If PARTIAL: ANCHOR[0] recall is
required uniformly across all paths regardless of path-specific need.

**V-04 vs V-05 implication**: If both PASS, V-05 is the minimal form (REG-only recall at register
path). If V-04 PASS and V-05 PARTIAL: ANCHOR[0] is structurally required at register path, V-04
is the minimal viable 100/100 prompt under v5.
