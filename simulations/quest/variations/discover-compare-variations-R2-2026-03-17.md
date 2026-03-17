Written to `simulations/quest/variations/discover-compare-variations-R2-2026-03-17.md`.

---

## discover-compare — Variations R2

Five complete prompts targeting the three new v2 aspirational criteria.

---

### Variation axes and hypotheses

**V-01 — Explicit Exclusion Rule** (C-11 target, single-axis)
Axis: inertia framing. Places an explicit "this is an error" prohibition sentence inside each inertia section rather than relying on structural separation alone. Tests whether a stated rule at the sentence level makes relative A-vs-B inertia detectable before it reaches the matrix.

**V-02 — Token Ledger at Matrix Assembly** (C-10 target, single-axis)
Axis: output format. Every phase emits a named token (FEAS-A, INERT-B, etc.); a LEDGER CHECK step before matrix assembly requires all 9 tokens to be listed and marked present. A gap in the ledger is structurally visible without re-reading prose.

**V-03 — Audience-First Register** (C-09 target, single-axis)
Axis: role sequence. Audience register is declared as the very first step — before status quo — and conditions all subsequent section framing. Tests whether audience-before-anchor is more reliable than audience-alongside-anchor (V-05 pattern) for preventing the "deferred to AMEND" failure mode.

**V-04 — Minimal Anchor Structure** (C-12 target, single-axis lean)
Axis: lifecycle emphasis. Four phases instead of eight. The named ANCHOR[0] is the sole structural spine — no ledger, no exclusion sentence. Tests whether the anchor commitment alone is sufficient to pass C-02 and C-05, isolating how much of V-05's complexity is load-bearing.

**V-05 — Combined: Token Ledger + Explicit Exclusion + Named Anchor + Audience-Primary** (all four new aspirational, combined)
Axes: C-10 + C-11 + C-12 + C-09. The anchor becomes a recalled token at every inertia phase (making drift a token mismatch); exclusion is stated as "is an error" at the sentence level; ledger verifies all tokens before assembly; audience is Phase 0 Part A before the anchor.

---

### Rubric coverage projection (v2 — 12 criteria)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 audience primary flow | — | — | PASS | — | PASS |
| C-10 token ledger | — | PASS | — | — | PASS |
| C-11 explicit exclusion rule | PASS | partial | — | partial | PASS |
| C-12 named anchor before analysis | partial | partial | — | PASS | PASS |

Key discriminator: V-01 vs V-04 tests whether "is an error" (V-01) outperforms a parenthetical "(not against Option B)" (V-04) for C-11. V-04's minimal structure tests whether C-12 alone can hold C-02 without ledger or exclusion sentence support.
 RED and give a one-sentence reason.

**Inertia:**
> Exclusion rule: compare Option B only against the status quo you defined in Step 0. Comparing Option B against Option A at this step is an error — the question is whether teams would keep the status quo rather than build Option B, not whether they would prefer B or A.

Would teams keep the status quo rather than build Option B? Rate LOW / MEDIUM / HIGH inertia risk. Name Option B's specific inertia mechanism — it may differ from Option A's.

**Risk:** Name the two biggest risks specific to Option B. These must be distinct from Option A's risks, or explain why they are the same.

**Competitive positioning:** Name at least one concrete differentiator for Option B distinct from Option A's positioning. If positioning overlaps, state the implication.

---

### STEP 3 — DECISION MATRIX

| Dimension | Status Quo (Option 0) | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | | |
| Inertia | anchor | | |
| Risk | N/A | | |
| Competitive position | baseline | | |

---

### STEP 4 — BUILD / NO-BUILD GATE

Review the inertia ratings from Steps 1 and 2. If both options face HIGH inertia, state explicitly: "Build neither is a candidate recommendation." If you still recommend building, name the condition that overrides inertia for both options.

---

### STEP 5 — RECOMMENDATION

**Recommendation: Option A / Option B / Neither / Conditional on {X}**

State the recommendation explicitly. Then:
- One sentence: why this option (reference the matrix)
- One sentence: what is given up by not choosing the other option

"It depends" without resolution is not a recommendation.

---

### AMEND

- **Add Option C** — Evaluate {option_c} on all four dimensions using the same status quo baseline and the same exclusion rule at inertia. Add a column to the matrix. Update the recommendation.
- **Weight a dimension** — Specify which dimension matters most and by what factor. Re-score both options under the new weighting. State whether the recommendation changes.
- **Shift audience** — Exec: re-open with recommendation + business risk gap. Engineering: re-open with feasibility + hardest implementation problem. Re-render the output in the specified register.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 — Token Ledger at Matrix Assembly

**Axis**: Output format — each phase emits a named token; a ledger step before matrix assembly cross-checks all tokens for gaps
**Hypothesis**: Requiring each analysis phase to emit a named output token (FEAS-A, INERT-A, RISK-A, COMP-A, etc.) and then requiring an explicit "LEDGER CHECK" step before matrix assembly makes missing scores structurally visible. The model cannot silently skip a dimension — a gap in the ledger is detectable without re-reading all prose. This targets C-10 directly while also reinforcing C-01 (bilateral coverage) and C-02 independence through the token naming convention.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each step below emits a named token. Use exactly the token names shown. The LEDGER CHECK step before matrix assembly will verify all tokens are present.

---

**[STEP 0] STATUS QUO**

Define what teams do today without either option. One sentence.

Token: `SQ: {status quo description}`

---

**[STEP 1A] FEASIBILITY — OPTION A**

Can {option_a} be built? Team capability, scope, timeline. Rate: GREEN / YELLOW / RED.

Token: `FEAS-A: {rating} — {one sentence reason}`

**[STEP 1B] FEASIBILITY — OPTION B**

Can {option_b} be built? Rate independently. Rate: GREEN / YELLOW / RED.

Token: `FEAS-B: {rating} — {one sentence reason}`

---

**[STEP 2A] INERTIA — OPTION A**

Compare Option A against SQ only. Would teams keep SQ rather than build Option A?
Rate: LOW / MEDIUM / HIGH.

Token: `INERT-A: {rating} — {mechanism}`

**[STEP 2B] INERTIA — OPTION B**

Compare Option B against SQ only. Do not reference Option A's inertia here.
Would teams keep SQ rather than build Option B? Rate: LOW / MEDIUM / HIGH.

Token: `INERT-B: {rating} — {mechanism}`

---

**[STEP 3A] RISK — OPTION A**

Name the top 2 risks specific to Option A. Rate each: LOW / MEDIUM / HIGH.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**[STEP 3B] RISK — OPTION B**

Name the top 2 risks specific to Option B. Must differ from RISK-A, or explain overlap.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**[STEP 4A] COMPETITIVE POSITIONING — OPTION A**

Concrete differentiator(s) for Option A. No generic phrases.

Token: `COMP-A: {positioning}`

**[STEP 4B] COMPETITIVE POSITIONING — OPTION B**

Concrete differentiator(s) for Option B. Distinct from COMP-A unless overlap is explained.

Token: `COMP-B: {positioning}`

---

**[STEP 5] LEDGER CHECK**

Verify all 9 tokens are present before assembling the matrix. List them:

```
SQ:      [ ]
FEAS-A:  [ ]
FEAS-B:  [ ]
INERT-A: [ ]
INERT-B: [ ]
RISK-A:  [ ]
RISK-B:  [ ]
COMP-A:  [ ]
COMP-B:  [ ]
```

If any token is missing, produce it now before proceeding. Do not assemble the matrix with gaps.

---

**[STEP 6] DECISION MATRIX**

Assemble from LEDGER CHECK tokens. SQ is Option 0.

| Dimension | Option 0 (SQ) | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

---

**[STEP 7] BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation." Name the override condition if still recommending a build.

---

**[STEP 8] RECOMMENDATION**

**Option A / Option B / Neither / Conditional on {X}**

- Why (reference a specific token or matrix cell)
- What is given up
- If recommendation diverges from strongest matrix evidence, state the override reason

---

**AMEND**

- **Add Option C** — Produce tokens FEAS-C, INERT-C, RISK-C, COMP-C using the same SQ baseline. Add them to the LEDGER CHECK list. Expand the matrix. Update the recommendation.
- **Weight a dimension** — Specify dimension and multiplier. Re-score from existing tokens. Show if recommendation changes.
- **Shift audience** — Exec: re-render Step 8 leading with recommendation + business risk. Engineering: re-render Step 8 leading with feasibility + implementation complexity. The token ledger does not change — only framing changes.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 — Audience-First Register

**Axis**: Role sequence — audience register declared as the first step, before status quo; conditions all subsequent output
**Hypothesis**: Placing audience declaration before any analysis (not in AMEND) prevents the "audience deferred to AMEND" failure mode (C-09). When audience is the first thing committed, subsequent phases can branch based on it — exec phases compress feasibility detail and expand business risk language; engineering phases do the reverse. This is a pure single-axis test of C-09 in the primary flow without relying on the full phase complexity of V-05 from R1.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

---

### REGISTER DECLARATION

Before analysis begins, declare the audience:

**Audience:** exec / engineering / general  *(fill in, or leave blank for general)*

Register rules that apply throughout this output:
- **exec**: lead every section with business impact and recommendation signal; compress implementation detail; end the recommendation with a one-line business risk statement
- **engineering**: lead every section with feasibility and technical complexity; include implementation approach options; end the recommendation with the hardest unsolved problem
- **general**: balanced framing; no emphasis bias

Print: `REGISTER: {exec / engineering / general}`

This register applies to all sections below. Do not switch register mid-output.

---

### STATUS QUO

What do teams do today without either option? One sentence, framed for the declared register.

- Exec framing: what business problem does the current approach leave unsolved?
- Engineering framing: what technical limitation does the current approach impose?
- General: what is the current state?

---

### OPTION A: {option_a}

Apply the register to all four dimensions.

**Feasibility:**
- Exec: can the team ship this in a timeframe that matters to the business? What is the capacity or funding constraint?
- Engineering: what is the hardest technical problem? What skills or infrastructure are missing?
- General: is the team capable, timeline realistic, scope manageable?

**Inertia (vs. status quo — not vs. Option B):** Would teams keep the status quo rather than build Option A? Name the specific mechanism. Rate LOW / MEDIUM / HIGH.

**Risk:** Top 2 risks specific to Option A, framed per register (business risks for exec, technical risks for engineering). Rate each.

**Competitive positioning:** Concrete differentiator for Option A, framed per register (market impact for exec, technical advantage for engineering).

---

### OPTION B: {option_b}

Apply the same register to all four dimensions independently.

**Feasibility:** (register-framed, as above)

**Inertia (vs. status quo — not vs. Option A):** Would teams keep the status quo rather than build Option B? Rate LOW / MEDIUM / HIGH with mechanism. Assess independently of Option A.

**Risk:** Top 2 risks specific to Option B, distinct from Option A's risks (or explain overlap). Register-framed.

**Competitive positioning:** Concrete differentiator for Option B, distinct from Option A's. Register-framed.

---

### DECISION MATRIX

| Dimension | Status Quo | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | | |
| Inertia | anchor | | |
| Risk | N/A | | |
| Competitive position | baseline | | |

Label column headers per register if exec or engineering:
- Exec: "Business Feasibility", "Adoption Risk", "Delivery Risk", "Market Position"
- Engineering: "Build Complexity", "Inertia Risk", "Technical Risk", "Technical Differentiation"

---

### BUILD / NO-BUILD GATE

If both inertia ratings are HIGH: state "Build neither is a candidate recommendation." Override condition if recommending build anyway.

---

### RECOMMENDATION

Apply register to the recommendation frame:

**Exec:** Open with: **Recommendation: Option A / B / Neither** — then one sentence on business risk, one sentence on what is given up.

**Engineering:** Open with: **Recommendation: Option A / B / Neither** — then one sentence on the hardest implementation constraint that supports this choice, one sentence on what is given up.

**General:** **Recommendation: Option A / B / Neither** — why, and trade-off.

---

### AMEND

- **Add Option C** — Analyze {option_c} using the same register and same status quo. Expand the matrix. Update the recommendation.
- **Weight a dimension** — Specify dimension and weight. Recalculate. State if recommendation changes. Register is preserved.
- **Override register** — State the new register. Re-render the recommendation section and dimension labels with the new framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-04 — Minimal Anchor Structure

**Axis**: Lifecycle emphasis — minimal phases (4 instead of 8), named anchor as the sole structural spine
**Hypothesis**: A lean prompt that commits a named ANCHOR before analysis tests whether the anchor commitment alone (C-12) is sufficient to prevent baseline drift and support independent inertia verdicts (C-02), without requiring the full eight-phase scaffolding of V-05 from R1. If this variant reliably passes C-01 through C-08 with fewer instructions, it suggests phase complexity in V-05 is over-specified. If it fails C-02 or C-05, that isolates which criteria require explicit structural enforcement beyond the anchor.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

---

**ANCHOR DECLARATION**

Before analysis: what do teams do today without either option?

`ANCHOR[0] = {status quo in one sentence}`

Every inertia assessment below measures pull away from ANCHOR[0]. Reference this token by name in each inertia section.

---

**BILATERAL ANALYSIS**

For Option A, then Option B, cover each of these four dimensions. Complete all four for Option A before starting Option B.

**Option A: {option_a}**

1. **Feasibility** — Can it be built? Team, scope, timeline. Rate GREEN / YELLOW / RED.
2. **Inertia vs ANCHOR[0]** — Would teams keep ANCHOR[0] rather than build Option A? (Compare against ANCHOR[0], not against Option B.) Rate LOW / MEDIUM / HIGH. Name the mechanism.
3. **Risk** — Top 2 risks specific to Option A. Rate each.
4. **Competitive positioning** — One concrete differentiator. No generic phrases.

**Option B: {option_b}**

1. **Feasibility** — Rate GREEN / YELLOW / RED.
2. **Inertia vs ANCHOR[0]** — Would teams keep ANCHOR[0] rather than build Option B? (Compare against ANCHOR[0], not against Option A.) Rate LOW / MEDIUM / HIGH. Name Option B's specific mechanism.
3. **Risk** — Top 2 risks specific to Option B. Must differ from Option A's, or explain why they are the same.
4. **Competitive positioning** — One concrete differentiator distinct from Option A's.

---

**MATRIX + GATE**

| Dimension | ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | | |
| Inertia | this IS the anchor | | |
| Risk | N/A | | |
| Competitive position | baseline | | |

Gate: if both inertia ratings are HIGH, state whether "build neither" applies and what condition would change this.

---

**RECOMMENDATION + AMEND**

**Recommendation: Option A / Option B / Neither / Conditional on {X}**

One sentence: why. One sentence: trade-off.

Amend paths:
- **Option C** — Analyze {option_c} on all four dimensions vs ANCHOR[0]. Add a column to the matrix.
- **Weight {dimension}** — Apply the specified multiplier. Show recalculated outcome.
- **Audience shift** — Exec: lead with recommendation + business risk. Engineering: lead with feasibility + hardest problem. Re-render.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-05 — Combined: Token Ledger + Explicit Exclusion + Named Anchor + Audience-Primary

**Axes**: C-10 token ledger + C-11 explicit exclusion rule + C-12 named anchor + C-09 audience in primary flow
**Hypothesis**: Stacking all four new aspirational mechanisms into one prompt maximizes coverage of C-09 through C-12 simultaneously. The key interaction hypothesis: the token ledger (C-10) and named anchor (C-12) reinforce each other — the anchor becomes a token that is recalled by name at each inertia phase, making baseline drift detectable as a token mismatch. The explicit exclusion rule (C-11) is placed at the sentence level inside each inertia section, not just as structural separation. Audience register (C-09) is declared at Phase 0 before the anchor, making it a precondition for all subsequent output — not a post-hoc amend slot.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each phase emits a named token. Use the exact token names shown. The LEDGER step before matrix assembly verifies all tokens are present.

---

**PHASE 0 — REGISTER + ANCHOR**

*Part A — Audience register (declare first):*
Audience: exec / engineering / general  *(fill in, or leave blank for general)*

Register rules in effect for all phases:
- **exec**: lead sections with business impact; compress implementation detail; risk = business consequence
- **engineering**: lead sections with build complexity; expand technical feasibility; risk = implementation failure mode
- **general**: balanced framing

Token: `REG: {exec / engineering / general}`

*Part B — Status quo anchor:*
What do teams do today without either option? One sentence framed for the declared register.

Token: `ANCHOR[0]: {status quo description}`

Binding rule: every inertia phase below must reproduce `ANCHOR[0]` verbatim as a token recall line. Do not paraphrase or summarize — use the exact sentence committed here. If the status quo changes during analysis, that signals a scoping error, not an update.

Print: `Phase 0 complete. REG committed. ANCHOR[0] committed.`

---

**PHASE 1A — FEASIBILITY: OPTION A**
Evaluate {option_a} for buildability. Apply REG framing.
Rating: GREEN / YELLOW / RED

Token: `FEAS-A: {rating} — {one sentence, REG-framed}`

**PHASE 1B — FEASIBILITY: OPTION B**
Evaluate {option_b} for buildability. Apply REG framing. Independent of Option A.
Rating: GREEN / YELLOW / RED

Token: `FEAS-B: {rating} — {one sentence, REG-framed}`

---

**PHASE 2A — INERTIA: OPTION A vs ANCHOR[0]**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0}`

Exclusion rule: compare Option A only against ANCHOR[0]. Comparing Option A against Option B at this phase is an error — the question is whether teams would keep ANCHOR[0] rather than build Option A, not whether they prefer A over B.

Would teams keep ANCHOR[0] rather than build Option A? Name the specific mechanism.
Rating: LOW / MEDIUM / HIGH

Token: `INERT-A: {rating} — {mechanism specific to Option A}`

**PHASE 2B — INERTIA: OPTION B vs ANCHOR[0]**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0}`

Exclusion rule: compare Option B only against ANCHOR[0]. Comparing Option B against Option A at this phase is an error — the question is whether teams would keep ANCHOR[0] rather than build Option B, not whether they prefer B over A.

Would teams keep ANCHOR[0] rather than build Option B? Name Option B's specific mechanism — it may differ from Option A's.
Rating: LOW / MEDIUM / HIGH

Token: `INERT-B: {rating} — {mechanism specific to Option B}`

---

**PHASE 3A — RISK: OPTION A**
Top 2 risks specific to Option A. REG-framed (business consequence for exec; implementation failure for engineering). Rate each.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**PHASE 3B — RISK: OPTION B**
Top 2 risks specific to Option B. Must be distinct from RISK-A, or explain overlap.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A — COMPETITIVE POSITIONING: OPTION A**
Concrete differentiator(s) for Option A. REG-framed. No generic phrases.

Token: `COMP-A: {positioning}`

**PHASE 4B — COMPETITIVE POSITIONING: OPTION B**
Concrete differentiator(s) for Option B. Must be distinct from COMP-A unless overlap is explained.

Token: `COMP-B: {positioning}`

---

**PHASE 5 — LEDGER CHECK**

List all tokens before assembling the matrix. Mark each present or missing:

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

If any token is missing, produce it now. Do not proceed to matrix assembly with gaps.

---

**PHASE 6 — DECISION MATRIX**

Assemble from LEDGER CHECK tokens. Column header for Option 0 uses ANCHOR[0] label. Apply REG to dimension labels if exec or engineering.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

REG label overrides — exec: Feasibility → Business Feasibility; Risk → Business Risk; Competitive → Market Position
REG label overrides — engineering: Feasibility → Build Complexity; Risk → Technical Risk; Competitive → Technical Differentiation

---

**PHASE 7 — BUILD / NO-BUILD GATE**

If INERT-A = HIGH and INERT-B = HIGH:
State: "Build neither is a candidate recommendation."
Name the override condition that would change this, or conclude with Neither.

If only one is HIGH: note it as a risk factor but proceed.

---

**PHASE 8 — RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0}`

Apply REG to recommendation framing:
- **exec**: open with **Recommendation: Option A / B / Neither** + top business risk gap from RISK tokens; close with one-line business consequence of not choosing the other option
- **engineering**: open with **Recommendation: Option A / B / Neither** + hardest implementation constraint from FEAS tokens; close with one-line technical trade-off
- **general**: open with **Recommendation: Option A / B / Neither** + matrix evidence; close with trade-off sentence

If recommendation diverges from matrix plurality, state the override reason explicitly.

---

**PHASE 9 — AMEND**

Three paths:

1. **Add Option C** — Produce tokens FEAS-C, INERT-C (with TOKEN RECALL of ANCHOR[0] and same exclusion rule), RISK-C, COMP-C. Add to LEDGER CHECK. Expand Phase 6 matrix. Update Phase 8 recommendation.
2. **Weight {dimension}** — State dimension and multiplier. Re-score from existing tokens. Show whether recommendation changes.
3. **Override register** — State new register. Re-render Phase 6 labels and Phase 8 framing. Print: `REG override: {new register}.`

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## Rubric coverage projection (v2 — 12 criteria)

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
| C-09 audience in primary flow | — | — | PASS | — | PASS |
| C-10 token ledger at assembly | — | PASS | — | — | PASS |
| C-11 explicit exclusion rule | PASS | partial | — | partial | PASS |
| C-12 named anchor before analysis | partial | partial | — | PASS | PASS |

**Notes on partials:**
- V-01 C-12: status quo defined in Step 0, but not committed as a named token with an explicit binding rule — the anchor exists but is not token-named, so inertia phases can paraphrase it
- V-02 C-11: inertia phases say "do not reference Option A" but phrased as framing, not as a stated rule with the word "error" — partial at sentence-level prohibition
- V-02 C-12: `SQ:` token committed before analysis, but no binding rule tying inertia phases to that token by name — they can paraphrase rather than recall
- V-04 C-11: each inertia section includes "(Compare against ANCHOR[0], not against Option B)" as a parenthetical — closer than V-01 but not the full "is an error" prohibition

**Projected composite scores:**
- V-01: 4/4 essential, 3/3 recommended, 1/5 aspirational (C-11 full, C-12 partial, C-08 pass) — ~72 (passing)
- V-02: 4/4 essential, 3/3 recommended, 2/5 aspirational (C-10 full, C-08 pass, C-11/C-12 partial) — ~74 (passing)
- V-03: 4/4 essential, 3/3 recommended, 2/5 aspirational (C-09 full, C-08 pass) — ~72 (passing)
- V-04: 4/4 essential, 3/3 recommended, 2/5 aspirational (C-12 full, C-08 pass, C-11 partial) — ~72 (passing)
- V-05: 4/4 essential, 3/3 recommended, 5/5 aspirational (all pass) — ~100 (golden candidate)

**Key interactions to watch in scoring:**
- V-01 vs V-04: tests whether the "is an error" framing (V-01) outperforms a parenthetical "(not against Option B)" (V-04) for C-11
- V-02 LEDGER CHECK: tests whether explicit token enumeration before assembly prevents invisible omission without requiring full phase structure
- V-03 register-as-first-step: tests whether audience before status quo is more reliable than audience alongside anchor (V-05 pattern)
- V-04 minimal anchor: tests whether C-12 alone (no ledger, no exclusion sentence) is sufficient to pass C-02 and C-05, or whether those require more structural scaffolding
- V-05 interaction: anchor becomes a recalled token at every inertia phase — tests whether token recall of the anchor text is a stronger baseline-drift prevention than a named reference alone
