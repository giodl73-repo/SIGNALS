Written to `simulations/quest/variations/discover-compare-variations-R9-2026-03-17.md`.

---

## discover-compare R9 -- V-01 through V-05

**Pivot from R8**: v7 adds C-22/C-23/C-24 (/17). R8 V-01 under v7 scores ~98.82 (C-23 FAIL, C-24 FAIL). R9 introduces the first grand composite targeting all 17 criteria, then probes C-24's coverage aggregation model and C-23's register-routing precision.

| Var | Axis | Key criteria | Projected |
|-----|------|--------------|-----------|
| V-01 | Grand composite (R8 V-02 + V-05 + all-path sub-ledgers) | C-22, C-23, C-24 | **100.00** |
| V-02 | Add-C-only sub-ledger (Weight/Override: no blocking gate) | C-24 | ~99.71 |
| V-03 | All-paths bare HALT, no token enumeration | C-24 | ~99.71 |
| V-04 | Register-gated recommendation (exec->reco-first, eng->matrix-first) | C-23, C-09 | **100.00** |
| V-05 | V-02 + V-04 combined | C-23, C-24 | ~99.71 |

**Three discriminating questions:**

1. **V-01 on C-24**: Does all-path mini-ledger+halt achieve C-24 PASS? Confirms 17/17 ceiling.

2. **V-02 vs V-03 on C-24**: "One path full + others absent" vs "all paths bare-halt." Score equality = C-24 aggregation is path-agnostic in the PARTIAL range. Divergence = C-24 rewards either breadth or depth.

3. **V-04 on C-09**: Does register-conditional ordering score C-09 higher than V-01's always-first? If yes: always-first carries a latent C-09 PARTIAL risk on engineering register runs that V-04 eliminates.
s depth
(one path full). If equal: both register as C-24 PARTIAL regardless of coverage pattern. This
pair brackets C-24's aggregation model precisely.

**Secondary question (V-04)**: Does register-conditional recommendation ordering satisfy C-23
identically to always-first (V-01)? Both forms produce recommendation-first for exec register.
V-04 additionally routes engineering to matrix-first -- testing whether C-09 scores differently
when engineering register explicitly gets matrix-first ordering (matching C-09's engineering
requirement) vs V-01's always-first which may be C-09-suboptimal for engineering runs.

**V-05 interaction test**: Combining V-02 (C-24 PARTIAL) with V-04 (C-23 PASS/C-09 gain) confirms
that C-23 and C-24 are orthogonal -- the register-gating instruction does not affect AMEND path
gate scoring.

---

### Rubric coverage projection (v7 -- 24 criteria, aspirational /17)

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
| C-09 audience register | PASS | PASS | PASS | **?** | **?** |
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
| **C-23 exec leads with recommendation** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **C-24 AMEND path sub-ledgers** | **PASS** | **PARTIAL** | **PARTIAL** | **PASS** | **PARTIAL** |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/17) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 17/17 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 16.5/17 = 9.71 | **99.71** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 16.5/17 = 9.71 | **99.71** | TBD |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 17/17 = 10.00 | **100.00** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 16.5/17 = 9.71 | **99.71** | TBD |

*V-02 and V-03 both projected 99.71. Actual outcome may diverge if C-24 rewards breadth (V-03 all-
paths bare-halt) over depth (V-02 one-path full). Score equality confirms C-24 partial is path-
agnostic in the PARTIAL range.*

*C-09 marked ? for V-04 and V-05: register-gated routing explicitly routes engineering to matrix-
first, matching C-09's engineering requirement. If C-09 scores higher for V-04 than V-01: always-
first ordering carries a latent C-09 PARTIAL risk for engineering register runs.*

---

### Key discriminating tests

**V-01 on C-24**: Whether all-path mini-ledger + blocking halt coverage achieves C-24 PASS.
Confirms the "each AMEND path" requirement is satisfiable. Establishes 17/17 = 100.00 ceiling.

**V-02 on C-24**: C-24 requires "each AMEND path." V-02 has Add-C with full mini-ledger + halt;
Weight and Override carry TOKEN RECALL + FAULT but no blocking gate. Does C-24 score PARTIAL
(some path-level compliance exists) or FAIL (criterion is binary -- all paths or nothing)?
Expected PARTIAL. If FAIL: C-24 has no partial state for asymmetric coverage.

**V-03 on C-24**: All three paths carry a blocking HALT but no token enumeration. This satisfies
the rubric's literal partial condition ("blocking instruction present but without token enumeration
= partial") at every path uniformly. Expected PARTIAL at the same score as V-02. If V-03 > V-02:
C-24 rewards breadth of partial coverage over depth of single-path full coverage. If V-03 < V-02:
best-path anchor (V-02's Add-C full) outscores uniform partial. This is R9's primary discrimination.

**V-04 on C-23**: V-04's exec path is recommendation-first (identical to V-01). C-23 fires on exec
register only. The conditional routing instruction adds no C-23 risk. Expected PASS identical to
V-01. If PARTIAL: the routing instruction is visible to C-23 as conditional rather than
unconditional recommendation-first -- unexpected, would require C-23 clarification.

**V-04 on C-09**: C-09 requires "engineering output leads with feasibility and implementation
complexity." V-04 routes engineering register to matrix-first (which shows FEAS-A, FEAS-B in the
first data-bearing section). V-01 always leads with recommendation regardless of register. If V-04
scores C-09 higher than V-01: V-01's always-first form is C-09-suboptimal for engineering register,
and register-gated ordering is the correct approach for C-09 full compliance.

**V-05 interaction test**: C-23 outcome should match V-04 C-23; C-24 outcome should match V-02
C-24. Any deviation in either direction reveals an interaction between phase-ordering instructions
and AMEND path gate structure.

---

## V-01 -- Grand composite (first v7 17/17 candidate)

**Axis**: Synthesis -- combines R8 V-02 (phase-label-free) + R8 V-05 (recommendation-first) +
all-path AMEND sub-ledgers (extending R8 V-04 from Add-C-only to all three AMEND paths)
**Hypothesis**: First prompt form targeting all 17 v7 criteria. C-22 PASS via label-free structure
(confirmed R8 V-02). C-23 PASS via always-recommendation-first ordering (confirmed R8 V-05). C-24
PASS via mini-ledger + blocking halt at every AMEND path -- Add-C, Weight, Override register.
All 14 prior criteria preserved from R8 V-02 and V-05 (both confirmed 100.00 under v6). Expected
composite: 17/17 = 100.00.

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

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

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
Name override condition or revise recommendation above to Neither.

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

Add Option C column to matrix. Update recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`

```
Weight ledger: ANCHOR[0] [ ]  WEIGHT [ ]
```
**HALT -- do not re-score if ledger incomplete.**

Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`

```
Override ledger: REG [ ]  REG-override [ ]
```
**HALT -- do not re-render if ledger incomplete.**

Re-render matrix labels and recommendation framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 -- Add-C-only sub-ledger (C-24 partial diagnostic)

**Axis**: AMEND path coverage -- Add-C path retains mini-ledger + blocking halt from V-01; Weight
and Override paths revert to TOKEN RECALL + FAULT only (no blocking gate, no token enumeration)
**Hypothesis**: C-24 requires "each AMEND path" to have a mini-ledger + blocking halt. V-02 has
one path with full C-24 coverage (Add-C) and two paths with TOKEN RECALL + FAULT but no blocking
gate (Weight, Override). Expected C-24 PARTIAL: criterion not satisfied at "each path" level but
some path-level compliance exists. If C-24 FAIL: criterion is binary -- all paths or nothing; no
partial credit for partial path coverage. If C-24 PASS: criterion fires on any AMEND path having
a mini-ledger (not strictly "each"). This is the primary R9 discriminating test for C-24's coverage
model. All other criteria identical to V-01. Expected 16.5/17 = 99.71.

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

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

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
Name override condition or revise recommendation above to Neither.

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

Add Option C column to matrix. Update recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
Re-render matrix labels and recommendation framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 -- All-paths HALT, no enumeration

**Axis**: AMEND path blocking style -- all three AMEND paths carry a blocking HALT instruction,
but no token-name enumeration precedes any halt
**Hypothesis**: C-24's literal partial condition is "Blocking instruction present but without
token enumeration = partial." V-03 satisfies this per-path partial condition uniformly across all
three AMEND paths -- each path has a blocking halt but lists no token names before it. Expected
C-24 PARTIAL at the same composite as V-02 (99.71). Primary discriminating question vs V-02:
does C-24 reward breadth (V-03: all paths reach partial level) over depth (V-02: one path full,
others absent)? If V-03 > V-02: uniform partial coverage outscores asymmetric coverage -- C-24
aggregates by path-average or breadth. If V-03 = V-02: both PARTIAL regardless of distribution.
If V-03 < V-02: best-path anchor matters -- V-02's Add-C full coverage anchors higher. The
V-02/V-03 pair brackets C-24's aggregation model. Expected 16.5/17 = 99.71.

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

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

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
Name override condition or revise recommendation above to Neither.

---

AMEND:

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`
**HALT -- do not extend matrix if any Add-C token is absent.**
Add Option C column to matrix. Update recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`
**HALT -- do not re-score if ANCHOR[0] or WEIGHT token is absent.**
Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
**HALT -- do not re-render if REG or REG-override token is absent.**
Re-render matrix labels and recommendation framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-04 -- Register-gated recommendation ordering

**Axis**: Conditional phase ordering -- recommendation placement is routed by REG value: exec
register produces recommendation before matrix; engineering and general registers produce matrix
before recommendation
**Hypothesis**: V-01 always places recommendation before matrix (C-23 PASS confirmed via R8 V-05).
V-04 makes the ordering conditional on REG. For exec: recommendation precedes matrix (C-23 pass
condition unchanged). For engineering/general: matrix precedes recommendation (aligns with C-09's
"engineering output leads with feasibility" requirement). C-23 fires on exec register only; the
engineering path does not affect C-23 scoring -- expected PASS identical to V-01. C-09 may score
higher: V-04 explicitly routes engineering to matrix-first, matching the C-09 engineering framing
requirement; V-01's always-first may be C-09 PARTIAL for engineering register. All other criteria
identical to V-01 (all-path sub-ledgers preserved). Expected 17/17 = 100.00. Key open question:
does V-04 score C-09 higher than V-01?

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

## V-05 -- Combination: Add-C-only sub-ledger + register-gated recommendation

**Axis**: V-02 + V-04 combined -- Add-C-only sub-ledger (C-24 partial) and register-gated
recommendation ordering (C-23 pass); Weight and Override paths have no blocking gate; exec
register gets recommendation-first, engineering/general gets matrix-first
**Hypothesis**: C-23 and C-24 are orthogonal criteria. V-05 combines a C-23 PASS element
(register-gated ordering from V-04) with a C-24 PARTIAL element (Add-C-only sub-ledger from V-02).
Expected: C-23 PASS (exec path recommendation-first, satisfying C-23 pass condition), C-24 PARTIAL
(Add-C full, Weight/Override no blocking gate -- same as V-02). Composite 16.5/17 = 99.71. If
V-05 differs from V-02's C-24 score: the routing instruction introduces structural complexity
that the rubric reads as affecting AMEND path gate scoring -- unexpected interaction. If V-05
differs from V-04's C-23 score: the Add-C-only sub-ledger structure interferes with C-23
assessment -- also unexpected. Expected no interaction on either axis.

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
Re-score from tokens. Update RECOMMENDATION if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
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
| C-09 audience register | PASS | PASS | PASS | ? | ? |
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
| C-24 AMEND path sub-ledgers | PASS | PARTIAL | PARTIAL | PASS | PARTIAL |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/17) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 17/17 = 10.00 | **100.00** | TBD |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 16.5/17 = 9.71 | **99.71** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 16.5/17 = 9.71 | **99.71** | TBD |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 17/17 = 10.00 | **100.00** | TBD |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 16.5/17 = 9.71 | **99.71** | TBD |

*C-09 marked ? for V-04 and V-05. Both are projected PASS (R8 V-05 established C-09 PASS with
always-first; register-gated should not regress). If V-04 scores C-09 higher than V-01: always-
first ordering carries a latent C-09 PARTIAL risk on engineering register runs, and V-04's register-
routing eliminates it.*

*V-02 and V-03 projected equal at 99.71 (both C-24 PARTIAL). If actual scores diverge: C-24
has an aggregation model that prefers breadth (V-03) or depth (V-02).*

### Key results to watch

**V-01 on C-24**: Confirms all-path mini-ledger + halt achieves C-24 PASS. Establishes 17/17 =
100.00 as the attainable ceiling under v7.

**V-02 vs V-03 on C-24**: Primary R9 discrimination. Score equality confirms C-24 partial is
path-agnostic. Score divergence reveals C-24's aggregation model (breadth vs depth).

**V-04 on C-09**: Whether register-gated ordering scores higher on C-09 than V-01's always-first.
Determines whether always-first carries a latent C-09 risk for engineering register.

**V-05 interaction test**: Confirms C-23 and C-24 are orthogonal. V-05 C-24 should match V-02;
V-05 C-23 should match V-04. Deviation on either axis reveals an unexpected structural interaction.
