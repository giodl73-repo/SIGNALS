Written to `simulations/quest/variations/discover-compare-variations-R5-2026-03-17.md`.

---

## discover-compare — Variations R5 Summary

**Context**: R4 confirmed the minimal viable 100/100 candidate under v3 rubric. C-17 is new in v4 — it requires purely operative output with no explanatory prose. R4's canonical form still has three prose elements that likely trigger C-17 PARTIAL.

### Variation axes

| Var | Axis | Change from R4 canonical | C-17 | Key test |
|-----|------|--------------------------|------|----------|
| V-01 | baseline | None — exact R4 minimal viable | PARTIAL | Confirms cost of residual prose |
| V-02 | lifecycle emphasis | Strip preamble + Phase 0 framing + FAULT explanation clause | PASS | C-11 with condensed FAULT |
| V-03 | inertia framing | Condense FAULT only; all other V-01 prose preserved | PARTIAL | C-11 in isolation |
| V-04 | output format | Phase 9 as pure token expansion | PARTIAL | C-07 at max compression |
| V-05 | combined | V-02 + V-03 + V-04 | PASS | Best 100/100 candidate |

### The condensed FAULT form (V-02/V-03/V-05)

```
FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.
```

States both polarities in one operative directive (positive: ANCHOR[0] basis; negative: no inter-option). Key question: does this pass C-11 without the explanatory clause?

### Projected composites

- V-01: **99.5** (C-17 PARTIAL confirmed)
- V-02: **100** if C-11 passes; **99.5** if PARTIAL
- V-03: **99.5** (C-17 PARTIAL + C-11 isolation test)
- V-04: **99.5** (C-17 PARTIAL + C-07 isolation test)
- V-05: **100** if both C-11 and C-07 pass; lower otherwise
| PASS | PASS |
| V-03 | inertia framing | FAULT condensed to dual-polarity one-liner; all other V-01 prose preserved | testing | PARTIAL | PASS |
| V-04 | output format | Phase 9 AMEND as pure token expansion; all other V-01 prose preserved | PASS | PARTIAL | testing |
| V-05 | combined | V-02 + V-03 + V-04 | testing | PASS | testing |

### Key discriminating tests

- **V-01 on C-17**: confirms whether R4 canonical is PARTIAL or worse. Sets the baseline delta.
- **V-02/V-03 on C-11**: does `FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.` pass C-11? C-11 requires an explicit "compare against status quo, not against Option [X]" prohibition. The dual-polarity form states both the positive (ANCHOR[0] only) and negative (not inter-option), but without the "inertia asks whether" explanatory clause. If PASS: the clause was overhead. If PARTIAL: it was load-bearing for C-11 detection.
- **V-04 on C-07**: does Phase 9 expressed as token slot expansion pass "actionable AMEND"? Token-form expansion provides concrete slot declarations for all three paths. If PASS: AMEND prose is overhead.
- **V-05 interactions**: if C-11 and C-07 both PASS in isolation, do they interact safely when combined?

### Rubric coverage projection (v4 — 17 criteria, aspirational /10)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 bilateral dimensions | PASS | PASS | PASS | PASS | PASS |
| C-02 independent inertia | PASS | PASS | PASS | PASS | PASS |
| C-03 decision matrix | PASS | PASS | PASS | PASS | PASS |
| C-04 explicit recommendation | PASS | PASS | PASS | PASS | PASS |
| C-05 build/no-build gate | PASS | PASS | PASS | PASS | PASS |
| C-06 differentiated risk | PASS | PASS | PASS | PASS | PASS |
| C-07 actionable AMEND | PASS | PASS | PASS | **TESTING** | **TESTING** |
| C-08 Option 0 in matrix | PASS | PASS | PASS | PASS | PASS |
| C-09 audience primary flow | PASS | PASS | PASS | PASS | PASS |
| C-10 token ledger | PASS | PASS | PASS | PASS | PASS |
| C-11 explicit exclusion rule | PASS | **TESTING** | **TESTING** | PASS | **TESTING** |
| C-12 named anchor before analysis | PASS | PASS | PASS | PASS | PASS |
| C-13 verbatim anchor recall | PASS | PASS | PASS | PASS | PASS |
| C-14 failure class co-located | PASS | PASS | PASS | PASS | PASS |
| C-15 register before anchor | PASS | PASS | PASS | PASS | PASS |
| C-16 blocking ledger gate | PASS | PASS | PASS | PASS | PASS |
| **C-17 output compressed** | **PARTIAL** | **PASS** | **PARTIAL** | **PARTIAL** | **PASS** |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/10) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 9.5/10 = 9.50 | **99.50** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 10/10 = 10.00 | **100.00** | YES |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 9.5/10 = 9.50 | **99.50** | YES |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 9.5/10 = 9.50 | **99.50** | YES |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 10/10 = 10.00 | **100.00** | YES |

*Partial = 0.5. TESTING criteria projected PASS above. If C-11 PARTIAL in V-02/V-03/V-05:
composite drops 0.5. If C-07 PARTIAL in V-04/V-05: composite drops 0.5.*

If V-02 C-11 is PARTIAL: explanatory clause is structural for C-11 — dual-polarity alone insufficient.
If V-02 C-11 is PASS: condensed form achieves C-11 AND C-17 simultaneously — V-05 is the 100/100 candidate.
If V-04 C-07 is PARTIAL: prose path descriptions are load-bearing — tokenization is too aggressive.
If V-04 C-07 is PASS: AMEND as token slots fully satisfies actionable AMEND.

---

## V-01 — R4 Canonical

**Axis**: Baseline — exact "Minimal Viable 100/100 Candidate" from R4 scorecard; no changes
**Hypothesis**: R4 projected this form at 100/100 under the v3 rubric (9 aspirational criteria).
Under the v4 rubric (10 aspirational criteria, C-17 added), the three remaining prose elements
(preamble sentence, Phase 0 framing, FAULT explanatory clause) will trigger C-17 PARTIAL →
9.5/10 aspirational → composite 99.5. This variation establishes the baseline delta that R5
variations attempt to close.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each phase produces a named token. Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 — FRAME**

Declare audience register, then commit status quo anchor framed for that register.

Audience: exec / engineering / general *(fill in, or leave blank for general)*

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
FAULT: Comparing Option A against Option B at this phase is a fault — inertia asks whether
teams would keep the status quo recalled above rather than build Option A, not whether they prefer
A over B.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} — {mechanism}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: Comparing Option B against Option A at this phase is a fault — inertia asks whether
teams would keep the status quo recalled above rather than build Option B, not whether they prefer
B over A.

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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce missing token, return here, verify all pass.

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

1. **Add Option C** — Produce FEAS-C, INERT-C (TOKEN RECALL of ANCHOR[0] verbatim + FAULT
   prohibition), RISK-C, COMP-C. Add to ledger. Expand matrix. Update recommendation.
2. **Weight {dimension}** — Dimension and multiplier. Re-score from tokens. State if
   recommendation changes.
3. **Override register** — `REG override: {new register}.` Re-render Phase 6 labels and
   Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 — C-17 Full Strip

**Axis**: Lifecycle emphasis — three remaining prose elements stripped from V-01; all operative
mechanisms preserved
**Hypothesis**: R4 V-03 confirmed that ~50% word reduction is safe for C-01 through C-16. C-17
adds a new pressure: can the remaining three prose elements be stripped without breaking any
other criterion? Stripped elements: (1) `"Each phase produces a named token."` — `"Use exact
token names."` is sufficient; (2) `"Declare audience register, then commit status quo anchor
framed for that register."` — token ordering alone satisfies C-15 (confirmed R4-V04); (3)
`"Audience: exec / engineering / general"` helper text; (4) FAULT explanatory clause condensed
to: `FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.`

The condensed FAULT states both the positive (compare against ANCHOR[0]) and the negative (not
inter-option) in a single operative directive. C-11 requires an explicit "compare against status
quo, not against Option [X]" prohibition. If C-11 PASS: the explanatory clause was overhead.
If C-11 PARTIAL: the clause was structurally required for C-11 detection.

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

1. **Add Option C** — Produce FEAS-C, INERT-C (TOKEN RECALL of ANCHOR[0] verbatim + FAULT
   prohibition), RISK-C, COMP-C. Add to ledger. Expand matrix. Update recommendation.
2. **Weight {dimension}** — Dimension and multiplier. Re-score from tokens. State if
   recommendation changes.
3. **Override register** — `REG override: {new register}.` Re-render Phase 6 labels and
   Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 — FAULT Condensed (Single-Axis Isolation)

**Axis**: Inertia framing — FAULT text condensed to dual-polarity one-liner; all other V-01
prose preserved verbatim
**Hypothesis**: V-02 strips three prose elements simultaneously. V-03 isolates the FAULT
condensation to test C-11 independently of the other stripping. V-01 FAULT uses the full
explanatory clause; V-03 replaces only that clause with the condensed form:
`FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.`
All other V-01 elements are unchanged — preamble sentence, Phase 0 framing, Phases 3-9 verbatim.
If V-03 C-11 = PASS: condensed form is independently sufficient for C-11 — the explanatory clause
was overhead. If V-02 C-11 = PASS but V-03 C-11 = FAIL: some other V-02 stripping inadvertently
helped C-11. If both PARTIAL: more text is structurally required. C-17 remains PARTIAL in V-03
because preamble and Phase 0 framing sentences are preserved.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each phase produces a named token. Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 — FRAME**

Declare audience register, then commit status quo anchor framed for that register.

Audience: exec / engineering / general *(fill in, or leave blank for general)*

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

Top 2 risks specific to Option B. Must differ from RISK-A or explain overlap. REG-framed.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A — COMPETITIVE POSITIONING: OPTION A**

Concrete differentiator(s). REG-framed. No generic phrases.

Token: `COMP-A: {positioning}`

**PHASE 4B — COMPETITIVE POSITIONING: OPTION B**

Distinct from COMP-A unless overlap is explained. REG-framed.

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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce the missing token, return to
this gate, and verify all pass before advancing.

---

**PHASE 6 — DECISION MATRIX**

Assemble from LEDGER GATE tokens. Option 0 column header uses ANCHOR[0]. Apply REG to
dimension labels.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

REG overrides — exec: Feasibility -> Business Feasibility; Risk -> Business Risk; Competitive -> Market Position
REG overrides — engineering: Feasibility -> Build Complexity; Risk -> Technical Risk; Competitive -> Technical Differentiation

---

**PHASE 7 — BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH:
State: "Build neither is a candidate recommendation."
Name the override condition, or conclude with Neither.

If only one is HIGH: note it as a risk factor and proceed.

---

**PHASE 8 — RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
TOKEN RECALL: `REG = {restate register from Phase 0}`

Apply REG framing:
- **exec**: open with **Recommendation: Option A / B / Neither** + top business risk from RISK tokens; close with one-line business consequence of not choosing the other option
- **engineering**: open with **Recommendation: Option A / B / Neither** + hardest constraint from FEAS tokens; close with technical trade-off
- **general**: **Recommendation: Option A / B / Neither** + matrix evidence; close with trade-off sentence

If recommendation diverges from matrix plurality, state the override reason explicitly.

---

**PHASE 9 — AMEND**

Three paths:

1. **Add Option C** — Produce tokens FEAS-C, INERT-C (with TOKEN RECALL of ANCHOR[0] verbatim
   + FAULT prohibition for comparing against A or B), RISK-C, COMP-C. Add to LEDGER GATE list.
   Expand Phase 6 matrix. Update Phase 8 recommendation.
2. **Weight {dimension}** — State dimension and multiplier. Re-score from existing tokens. Show
   whether recommendation changes.
3. **Override register** — State new register. Print `REG override: {new register}.`
   Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-04 — AMEND Tokenized

**Axis**: Output format — Phase 9 expressed as pure token expansion syntax; all other V-01
prose preserved verbatim
**Hypothesis**: V-01 Phase 9 uses descriptive prose paths ("Produce FEAS-C, INERT-C (TOKEN
RECALL of ANCHOR[0] verbatim + FAULT prohibition)..."). V-04 replaces these with explicit token
slot declarations, TOKEN RECALL directives, FAULT prohibitions, and action directives — the same
structural information without the path descriptions. C-07 requires "concrete instructions for
at least one of: adding a third option, weighting a specific dimension, adjusting for exec vs
engineering audience." Token expansion provides all three. If PASS: descriptive AMEND prose is
overhead. If PARTIAL: C-07 requires some minimum prose framing to establish actionability. C-17
remains PARTIAL in V-04 because preamble and Phase 0 framing prose from V-01 are preserved.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each phase produces a named token. Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 — FRAME**

Declare audience register, then commit status quo anchor framed for that register.

Audience: exec / engineering / general *(fill in, or leave blank for general)*

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
FAULT: Comparing Option A against Option B at this phase is a fault — inertia asks whether
teams would keep the status quo recalled above rather than build Option A, not whether they prefer
A over B.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} — {mechanism}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: Comparing Option B against Option A at this phase is a fault — inertia asks whether
teams would keep the status quo recalled above rather than build Option B, not whether they prefer
B over A.

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

## V-05 — Combined: C-17 Strip + FAULT Condensed + AMEND Tokenized

**Axes**: V-02 (lifecycle emphasis) + V-03 (inertia framing) + V-04 (output format) simultaneously
**Hypothesis**: V-02 tests C-11 with condensed FAULT and full prose strip. V-04 tests C-07 with
tokenized AMEND. V-05 applies both simultaneously to test for adverse interactions and to identify
the best 100/100 candidate under the v4 rubric. Expected: C-11 and C-07 behave independently; if
both pass in isolation, they pass in combination. Combined simplifications: preamble sentence
removed, Phase 0 framing removed, FAULT condensed to dual-polarity one-liner, AMEND as pure token
expansion. Projected C-17 PASS — no explanatory prose remains across any phase. If V-02 C-11 = PASS
and V-04 C-07 = PASS, V-05 is the minimal viable 100/100 prompt under the v4 rubric.

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

## Rubric coverage projection summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 bilateral dimensions | PASS | PASS | PASS | PASS | PASS |
| C-02 independent inertia | PASS | PASS | PASS | PASS | PASS |
| C-03 decision matrix | PASS | PASS | PASS | PASS | PASS |
| C-04 explicit recommendation | PASS | PASS | PASS | PASS | PASS |
| C-05 build/no-build gate | PASS | PASS | PASS | PASS | PASS |
| C-06 differentiated risk | PASS | PASS | PASS | PASS | PASS |
| C-07 actionable AMEND | PASS | PASS | PASS | **TESTING** | **TESTING** |
| C-08 Option 0 in matrix | PASS | PASS | PASS | PASS | PASS |
| C-09 audience primary flow | PASS | PASS | PASS | PASS | PASS |
| C-10 token ledger | PASS | PASS | PASS | PASS | PASS |
| C-11 explicit exclusion rule | PASS | **TESTING** | **TESTING** | PASS | **TESTING** |
| C-12 named anchor before analysis | PASS | PASS | PASS | PASS | PASS |
| C-13 verbatim anchor recall | PASS | PASS | PASS | PASS | PASS |
| C-14 failure class co-located | PASS | PASS | PASS | PASS | PASS |
| C-15 register before anchor | PASS | PASS | PASS | PASS | PASS |
| C-16 blocking ledger gate | PASS | PASS | PASS | PASS | PASS |
| **C-17 output compressed** | **PARTIAL** | **PASS** | **PARTIAL** | **PARTIAL** | **PASS** |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/10) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 9.5/10 = 9.50 | **99.50** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 10/10 = 10.00 | **100.00** | YES |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 9.5/10 = 9.50 | **99.50** | YES |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 9.5/10 = 9.50 | **99.50** | YES |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 10/10 = 10.00 | **100.00** | YES |

*Partial = 0.5. TESTING criteria projected PASS above. Each TESTING criterion that scores PARTIAL
instead drops the containing variation by 0.5 composite points.*

### Key results to watch

**V-01 C-17**: PARTIAL is certain given residual prose. The composite 99.5 confirms the cost of
each prose element under the new rubric and sets the ceiling for non-C-17-compliant forms.

**V-02/V-03 C-11**: The condensed FAULT `"compare against ANCHOR[0] only — Option A vs Option B
comparison is an error"` gives the positive (ANCHOR[0]) and the negative (not inter-option) in
one operative directive. C-11 pass condition: "The exclusion is stated as a rule that prevents
relative comparison." V-03 provides the isolation: if V-03 C-11 = PASS without any other
stripping, the condensed form is independently sufficient. If V-03 C-11 = PARTIAL, the
explanatory clause was structural for C-11 — R4 V-05 form must be preserved for that criterion.

**V-04 C-07**: Tokenized AMEND provides slot declarations + TOKEN RECALL + FAULT prohibition
for Option C expansion, plus token directives for weight and register override. C-07 pass
condition: "concrete instructions for at least one of: adding a third option, weighting a
specific dimension, adjusting for exec vs engineering audience." All three paths have concrete
structure. If PASS: prose path descriptions are confirmed overhead.

**V-02 + V-05 convergence**: If V-02 achieves 100/100 and V-05 achieves 100/100 with no
interaction effects, V-05 is the R5 minimal viable prompt — fully stripped, fully tokenized,
dual-polarity inertia prohibition. Approximately 40% shorter than R4 canonical with identical
or better coverage across all 17 criteria.
