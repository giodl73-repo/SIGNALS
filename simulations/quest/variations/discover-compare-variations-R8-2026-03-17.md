Written to `simulations/quest/variations/discover-compare-variations-R8-2026-03-17.md`.

---

## discover-compare R8 -- Summary

**Pivot from R7**: v6 rubric fully calibrated, V-01 confirmed 100/100. R8 shifts to structural diversity -- five axes testing whether alternative structural arrangements reach 100/100 or break specific criteria.

| Var | Axis | Change from V-01 | Key criterion | Projected |
|-----|------|------------------|---------------|-----------|
| V-01 | Baseline | R7 V-01 exact | -- | **100.00** |
| V-02 | Phase-label-free | All `**PHASE N -- NAME**` headers removed | C-12, C-17 | 99.29--100.00 |
| V-03 | Inline-frame | REG+ANCHOR[0] merged into Phase 1A | C-12 | ~99.29 |
| V-04 | AMEND sub-ledger | Add-C path gets blocking mini-ledger | C-19, C-20 | **100.00** |
| V-05 | Recommendation-first | Phase 8 moved before Phase 6 | C-04, C-09 | **100.00** |

**Primary discriminating question (V-02 vs V-03 together)**: Does C-12's "dedicated phase" mean (a) a labeled phase header, (b) a structurally separate block without a label, or (c) token ordering before analysis tokens? V-02 removes labels but keeps structural separation; V-03 removes structural separation entirely. Their C-12 outcomes bracket the definition precisely.

**Secondary questions**: V-04 tests whether a token-name checklist (blocking gate) triggers C-20 token-recall logic. V-05 tests whether recommendation-before-matrix is a valid exec-register form that scores identically to V-01.
on-first | Phase 8 moved before Phase 6 | PASS | PASS | **100.00** |

**Key discriminating questions**:
- **V-02 C-12**: Does "dedicated phase" in C-12 require a labeled phase header, or does the
  structural separation of frame-content (token declarations before analysis tokens) satisfy it
  even without a header? If PASS: phase labels are inert to C-12 and C-17. If FAIL/PARTIAL:
  phase labels are load-bearing for C-12.
- **V-02 C-17**: Are phase headers (**PHASE N -- NAME**) considered "explanatory scaffolding"
  (= overhead, PARTIAL) or structural labels (= operative, neutral)? V-01 currently scores PASS
  on C-17 with headers; removing them may improve or be neutral to C-17.
- **V-03 C-12**: Does declaring ANCHOR[0] at the TOP of Phase 1A (before FEAS-A) satisfy
  "dedicated phase before any option analysis begins"? Expected FAIL -- "dedicated phase" implies
  structural separation, not just token ordering within an analysis phase.
- **V-04 C-20**: Does an in-path blocking mini-ledger (listing token names, not recalling token
  values) trigger C-20? Expected: no -- TOKEN RECALL reclaims token VALUES; a ledger checklist
  is a structural gate, not a recall.
- **V-05 all criteria**: Does recommendation-before-matrix satisfy all 21 criteria unchanged?
  Expected PASS -- no criterion specifies relative ordering of recommendation and matrix phases.

---

### Rubric coverage projection (v6 -- 21 criteria, aspirational /14)

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
| **C-12 named anchor before analysis** | **PASS** | **?** | **FAIL** | **PASS** | **PASS** |
| C-13 verbatim anchor recall | PASS | PASS | PASS | PASS | PASS |
| C-14 failure class co-located | PASS | PASS | PASS | PASS | PASS |
| C-15 register before anchor | PASS | PASS | PASS | PASS | PASS |
| C-16 blocking ledger gate | PASS | PASS | PASS | PASS | PASS |
| **C-17 output compressed** | **PASS** | **?** | **PASS** | **PASS** | **PASS** |
| C-18 dual-polarity FAULT | PASS | PASS | PASS | PASS | PASS |
| C-19 AMEND self-contained | PASS | PASS | PASS | PASS | PASS |
| C-20 path-scoped TOKEN RECALL | PASS | PASS | PASS | PASS | PASS |
| C-21 FAULT propagates to AMEND | PASS | PASS | PASS | PASS | PASS |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/14) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 13-14/14 = 9.29-10.00 | **99.29-100.00** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 13/14 = 9.29 | **99.29** | YES |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |

*V-02 outcome depends on C-12/C-17 scoring of label-free form. Three branches: PASS on both
(100.00, phase labels are fully inert); C-12 FAIL only (99.29); C-12 PARTIAL only (99.64).*

*V-03 C-12 FAIL projected (13/14 = 9.29 -> 99.29). If C-12 PARTIAL: 13.5/14 = 9.64 -> 99.64.
If C-12 PASS: inline-frame satisfies "dedicated phase" -- rubric C-12 needs clarification.*

---

### Key discriminating tests

**V-02 on C-12**: The primary R8 signal. C-12 pass condition: "defined as a named anchor in a
dedicated phase before any option analysis begins." V-02 removes the **PHASE 0 -- FRAME** header
but preserves the token ordering: REG declaration, then ANCHOR[0] declaration, then FEAS-A. If the
structural separation (two token declarations followed by analysis tokens, with no phase label)
satisfies "dedicated phase" -- C-12 PASS. If "dedicated phase" requires a labeled phase boundary --
C-12 FAIL. This determination also clarifies whether phase headers are operative mechanism or
explanatory scaffold for C-17.

**V-02 on C-17**: Phase headers **PHASE N -- NAME** are structural labels that organize sections
but carry no operative directive. C-17 targets "rule description tables, binding rationale sentences,
Print: confirmations, preamble framing." Phase labels do not fall into these categories -- expected
C-17 PASS with or without them. If removing headers improves C-17 score: phase labels were overhead.
If removing headers harms score: unexpected and reveals C-17 cares about structural clarity.

**V-03 on C-12**: Strongest test of C-12's "dedicated phase" language. ANCHOR[0] declared inline
with FEAS-A in the same section. Even with REG->ANCHOR[0]->FEAS-A token ordering (satisfying C-15),
there is no structurally separate frame block. Expected FAIL on C-12. If PASS: "dedicated phase"
is equivalent to "token ordering before first analysis token" -- would require rubric clarification.
If PARTIAL: C-12 has a partial grading path (anchor before analysis tokens but not its own section).

**V-04 on C-19/C-20**: In-path Add-C mini-ledger. C-19 checks self-containment via inline TOKEN
RECALL + FAULT. The mini-ledger is a blocking gate, not a TOKEN RECALL (no token values recalled,
just token names listed for verification). Expected: benign to C-19 (possibly strengthens it) and
invisible to C-20 (no extra recall). If C-20 fires PARTIAL: the rubric interprets ledger token-name
listing as a form of recall -- would require C-20 clarification distinguishing recall from
verification.

**V-05 on all criteria**: No criterion specifies that recommendation must follow matrix. C-09 (exec
primary flow) states exec output "leads with recommendation and business risk" -- recommendation-
first format is natively exec-register-aligned. Expected 100/100. If any criterion fails: reveals
an implicit phase-ordering assumption that the rubric should make explicit.

---

## V-01 -- Baseline (R7 V-01)

**Axis**: Baseline -- R7 V-01 exact; no changes
**Hypothesis**: Stable 100/100 reference under v6. Confirms rubric consistency round-to-round.
All 21 criteria pass. C-20 and C-21 calibrated by R7. No structural changes.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 -- FRAME**

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

---

**PHASE 1A -- FEASIBILITY: OPTION A**

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

**PHASE 1B -- FEASIBILITY: OPTION B**

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

---

**PHASE 2A -- INERTIA: OPTION A**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

**PHASE 2B -- INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

---

**PHASE 3A -- RISK: OPTION A**

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**PHASE 3B -- RISK: OPTION B**

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A -- COMPETITIVE POSITIONING: OPTION A**

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

**PHASE 4B -- COMPETITIVE POSITIONING: OPTION B**

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

**PHASE 5 -- LEDGER GATE**

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

**HALT -- do not proceed to Phase 6 if any token is absent.** Produce missing token, return here,
verify all pass.

---

**PHASE 6 -- DECISION MATRIX**

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

**PHASE 7 -- BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or conclude Neither.

---

**PHASE 8 -- RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 9 -- AMEND**

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`
Add FEAS-C, INERT-C, RISK-C, COMP-C to LEDGER GATE. Add Option C column to Phase 6 matrix.
Update Phase 8 recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 -- Phase-label-free

**Axis**: Phase labels removed -- all **PHASE N -- NAME** headers deleted; all operative content
from V-01 preserved verbatim in identical token ordering
**Hypothesis**: Phase headers are structural labels that organize sections but contain no operative
directive. C-17 targets explanatory prose (rule tables, rationale sentences, preamble framing), not
section labels -- removing headers should leave C-17 unaffected. C-12 ("dedicated phase before any
option analysis begins") is the open question: does a labeled phase header constitute the "dedicated"
qualifier, or does structural separation (REG and ANCHOR[0] tokens appearing before any feasibility
or inertia tokens) satisfy C-12 without a header? If C-12 PASS: phase labels are inert to C-12,
and V-01's headers are cosmetic. If C-12 FAIL or PARTIAL: the label is load-bearing -- C-12 requires
a named phase boundary, not just token ordering. V-02 is the primary discriminating test for R8.

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
Name override condition or conclude Neither.

---

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
Add FEAS-C, INERT-C, RISK-C, COMP-C to LEDGER GATE. Add Option C column to matrix.
Update recommendation.

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

## V-03 -- Inline-frame

**Axis**: Frame collapsed -- REG and ANCHOR[0] declared inline at the top of the feasibility
section, no separate FRAME section; all other V-01 elements preserved verbatim
**Hypothesis**: V-01 satisfies C-12 through a dedicated Phase 0 (FRAME) that precedes all analysis
phases. C-15 explicitly notes "Physical token ordering in a single inline phase satisfies this
criterion" -- but this clause applies to C-15 (register before anchor), not C-12. C-12 requires
"a dedicated phase before any option analysis begins." Merging REG and ANCHOR[0] into the top of
the feasibility phase means ANCHOR[0] is declared in the same structural block as FEAS-A. Even with
token ordering preserved (REG -> ANCHOR[0] -> FEAS-A), there is no structurally separate dedicated
frame. Expected C-12 FAIL: the "dedicated phase" language is strict; structural separation is
required, not just token ordering. C-15 PASS: REG declared before ANCHOR[0] within the same inline
section satisfies C-15's explicit ordering criterion. If C-12 PARTIAL (not FAIL): some partial
credit exists for token-ordering-only frame commitment. If C-12 PASS: "dedicated phase" means
"appears before analysis" and inline declaration fully satisfies the criterion -- would require
rubric clarification to add the structural separation requirement explicitly.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 1A -- FEASIBILITY: OPTION A**

Token: `REG: {exec / engineering / general}`
Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

**PHASE 1B -- FEASIBILITY: OPTION B**

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

---

**PHASE 2A -- INERTIA: OPTION A**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 1A -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

**PHASE 2B -- INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 1A -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

---

**PHASE 3A -- RISK: OPTION A**

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**PHASE 3B -- RISK: OPTION B**

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A -- COMPETITIVE POSITIONING: OPTION A**

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

**PHASE 4B -- COMPETITIVE POSITIONING: OPTION B**

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

**PHASE 5 -- LEDGER GATE**

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

**HALT -- do not proceed to Phase 6 if any token is absent.** Produce missing token, return here,
verify all pass.

---

**PHASE 6 -- DECISION MATRIX**

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

**PHASE 7 -- BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or conclude Neither.

---

**PHASE 8 -- RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 9 -- AMEND**

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`
Add FEAS-C, INERT-C, RISK-C, COMP-C to LEDGER GATE. Add Option C column to Phase 6 matrix.
Update Phase 8 recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-04 -- AMEND Secondary Ledger

**Axis**: AMEND sub-ledger -- Add Option C path gains an inline blocking mini-ledger for C tokens;
all other V-01 elements preserved verbatim
**Hypothesis**: C-19 requires AMEND paths to be self-contained via inline TOKEN RECALL and FAULT
prohibitions. V-01's Add-C path already satisfies C-19. V-04 adds a blocking verification gate
after all four C tokens are produced, before extending the Phase 6 matrix. This strengthens path
self-containment: a missing INERT-C or FEAS-C token is caught and blocked inline, not requiring
re-reading Phase 5. The critical question is whether this affects C-20 (path-scoped TOKEN RECALL):
the mini-ledger lists token names (FEAS-C, INERT-C, RISK-C, COMP-C) but does not recall their
values -- no TOKEN RECALL: FEAS-C = {...} syntax. Expected: mini-ledger is a blocking gate
(structural verification), not TOKEN RECALL (value recall); C-20 unaffected. C-19: same or
stronger (more self-contained). Projected 100/100. If C-20 PARTIAL: the rubric conflates token-
name presence in a ledger with token-value recall -- would require C-20 clarification distinguishing
the two mechanisms.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 -- FRAME**

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

---

**PHASE 1A -- FEASIBILITY: OPTION A**

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

**PHASE 1B -- FEASIBILITY: OPTION B**

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

---

**PHASE 2A -- INERTIA: OPTION A**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

**PHASE 2B -- INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

---

**PHASE 3A -- RISK: OPTION A**

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**PHASE 3B -- RISK: OPTION B**

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A -- COMPETITIVE POSITIONING: OPTION A**

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

**PHASE 4B -- COMPETITIVE POSITIONING: OPTION B**

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

**PHASE 5 -- LEDGER GATE**

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

**HALT -- do not proceed to Phase 6 if any token is absent.** Produce missing token, return here,
verify all pass.

---

**PHASE 6 -- DECISION MATRIX**

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

**PHASE 7 -- BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or conclude Neither.

---

**PHASE 8 -- RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 9 -- AMEND**

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
**HALT -- do not extend Phase 6 matrix if any Add-C token is absent.**

Add Option C column to Phase 6 matrix. Update Phase 8 recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-05 -- Recommendation-first

**Axis**: Recommendation-first ordering -- Phase 8 (RECOMMENDATION) surfaced immediately after
Phase 5 (LEDGER GATE), before Phase 6 (DECISION MATRIX); all operative content from V-01 preserved
verbatim with phases renumbered
**Hypothesis**: V-01 follows the order: LEDGER GATE -> MATRIX -> BUILD/NO-BUILD GATE ->
RECOMMENDATION. V-05 reorders to: LEDGER GATE -> RECOMMENDATION -> MATRIX -> BUILD/NO-BUILD GATE.
The matrix becomes supporting evidence for the stated recommendation rather than its precursor.
This is a native exec-register form: exec output "leads with recommendation and business risk"
(C-09). All 21 criteria should be satisfied regardless of phase ordering -- no criterion specifies
that recommendation must follow matrix. C-04 (explicit recommendation): PASS. C-03 (decision matrix
present): PASS. C-09 (audience primary flow): PASS or stronger for exec register. C-10 (tokens
cross-checked at matrix assembly): PASS -- matrix assembles from LEDGER GATE tokens regardless of
whether recommendation preceded or followed assembly. If any criterion fails with recommendation-
first ordering: reveals an implicit phase-ordering assumption that the rubric should make explicit.
Expected 100/100.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 -- FRAME**

Token: `REG: {exec / engineering / general}`

Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

---

**PHASE 1A -- FEASIBILITY: OPTION A**

Rate GREEN / YELLOW / RED. REG-framed.

Token: `FEAS-A: {rating} -- {one sentence}`

**PHASE 1B -- FEASIBILITY: OPTION B**

Rate GREEN / YELLOW / RED. REG-framed. Independent of Option A.

Token: `FEAS-B: {rating} -- {one sentence}`

---

**PHASE 2A -- INERTIA: OPTION A**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} -- {mechanism}`

**PHASE 2B -- INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option B vs Option A comparison is an error.

Rate LOW / MEDIUM / HIGH. Name Option B's mechanism -- may differ from Option A's.

Token: `INERT-B: {rating} -- {mechanism}`

---

**PHASE 3A -- RISK: OPTION A**

Top 2 risks. REG-framed. Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**PHASE 3B -- RISK: OPTION B**

Top 2 risks. Distinct from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A -- COMPETITIVE POSITIONING: OPTION A**

Concrete differentiator. REG-framed.

Token: `COMP-A: {positioning}`

**PHASE 4B -- COMPETITIVE POSITIONING: OPTION B**

Distinct from COMP-A or explain overlap. REG-framed.

Token: `COMP-B: {positioning}`

---

**PHASE 5 -- LEDGER GATE**

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

**HALT -- do not proceed to Phase 6 if any token is absent.** Produce missing token, return here,
verify all pass.

---

**PHASE 6 -- RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 7 -- DECISION MATRIX**

Assemble from LEDGER GATE tokens.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

Apply REG column-label overrides if exec or engineering.

---

**PHASE 8 -- BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."
Name override condition or revise Phase 6 recommendation to Neither.

---

**PHASE 9 -- AMEND**

**Add Option C:**

Token: `FEAS-C: {rating} -- {one sentence}`
TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: compare against ANCHOR[0] only -- Option C vs A or B comparison is an error.
Token: `INERT-C: {rating} -- {mechanism}`
Token: `RISK-C: {risk1/rating}, {risk2/rating}`
Token: `COMP-C: {positioning}`
Add FEAS-C, INERT-C, RISK-C, COMP-C to LEDGER GATE. Add Option C column to Phase 7 matrix.
Update Phase 6 recommendation.

**Weight {dimension}:**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence -- do not paraphrase}`
FAULT: apply multiplier to dimension scores only -- do not revise token values.
Token: `WEIGHT: {dimension} x {multiplier}`
Re-score from tokens. Update Phase 6 recommendation if it changes.

**Override register:**

TOKEN RECALL: `REG = {restate original register}`
FAULT: register override re-renders labels and framing only -- do not revise analysis or ANCHOR[0].
Token: `REG override: {new register}`
Re-render Phase 7 labels and Phase 6 framing.

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
| **C-12 named anchor before analysis** | **PASS** | **?** | **FAIL** | **PASS** | **PASS** |
| C-13 verbatim anchor recall | PASS | PASS | PASS | PASS | PASS |
| C-14 failure class co-located | PASS | PASS | PASS | PASS | PASS |
| C-15 register before anchor | PASS | PASS | PASS | PASS | PASS |
| C-16 blocking ledger gate | PASS | PASS | PASS | PASS | PASS |
| **C-17 output compressed** | **PASS** | **?** | **PASS** | **PASS** | **PASS** |
| C-18 dual-polarity FAULT | PASS | PASS | PASS | PASS | PASS |
| C-19 AMEND self-contained | PASS | PASS | PASS | PASS | PASS |
| C-20 path-scoped TOKEN RECALL | PASS | PASS | PASS | PASS | PASS |
| C-21 FAULT propagates to AMEND | PASS | PASS | PASS | PASS | PASS |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/14) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 13-14/14 = 9.29-10.00 | **99.29-100.00** | TBD |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 13/14 = 9.29 | **99.29** | YES |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** | YES |

*V-02 outcome depends on C-12/C-17 scoring of label-free form. Three branches: PASS on both
(100.00, phase labels are fully inert); C-12 FAIL only (99.29); C-12 PARTIAL only (99.64).*

*V-03 C-12 FAIL projected (13/14 = 9.29 -> 99.29). If C-12 PARTIAL: 13.5/14 = 9.64 -> 99.64.
If C-12 PASS: inline-frame satisfies "dedicated phase" -- rubric C-12 needs clarification.*

### Key results to watch

**V-02 on C-12**: Whether phase labels are load-bearing for "dedicated phase." If PASS: V-02 is an
alternative 100/100 form -- label-free prompts satisfy all 21 criteria. If FAIL/PARTIAL: phase
labels are structurally required for C-12 compliance, not cosmetic.

**V-02 on C-17**: Whether removing phase headers improves, preserves, or harms C-17 score. Since
headers are structural labels (not explanatory prose), expected neutral. If PARTIAL: headers are
considered preamble framing by the rubric -- surprising and would require C-17 clarification.

**V-03 on C-12**: Establishes whether "dedicated phase" means (a) structurally separate block or
(b) token ordering before analysis tokens. V-03 (FAIL) vs V-02 (PASS or PARTIAL) together bracket
this definition precisely: V-02 preserves structural separation without labels; V-03 removes
structural separation entirely.

**V-04 on C-19/C-20**: Whether in-path blocking sub-ledger is benign (C-20 PASS -- not TOKEN RECALL)
or spurious (C-20 PARTIAL -- token-name listing misread as recall). If C-20 fires: this would be
a C-20 over-sensitivity that the rubric description should address.

**V-05 on all criteria**: Confirms recommendation-first is a valid alternative ordering. If 100/100:
the rubric is phase-order-agnostic for recommendation vs matrix. If any criterion fails: implicit
ordering assumption needs to be made explicit.
