Written to `simulations/quest/variations/discover-compare-variations-R3-2026-03-17.md`.

---

## discover-compare — Variations R3

Five complete prompts generated, one per new aspirational criterion (single-axis), then combined.

### Variation axes

| Variation | Axis | New criterion targeted | Hypothesis |
|-----------|------|----------------------|------------|
| V-01 | Inertia framing | C-13 — verbatim recall | Copy-here directive (not a TOKEN RECALL placeholder) inside each inertia section forces exact sentence reproduction without full phase machinery |
| V-02 | Phrasing register | C-14 — co-located failure class | `SCORING DEFECT:` label placed immediately after TOKEN RECALL tests whether co-location is the load-bearing element for C-14, independently of verbatim instruction |
| V-03 | Role sequence | C-15 — register before anchor | Phase 0A → Phase 0B ordering with explicit "commit before anchor" rule and REG recall at recommendation; extends R2 V-03 which achieved C-09 but not C-15 |
| V-04 | Output format | C-16 — blocking ledger gate | HALT GATE with "HALT — do not proceed" operative instruction; tests whether the explicit HALT word is the discriminating element vs R2 V-02's framing instruction |
| V-05 | Combined | C-13+C-14+C-15+C-16 | Minimal encoding of all four patterns; 10-token LEDGER GATE scope includes REG and ANCHOR[0] so the HALT also enforces Phase 0 commitment |

### Projected coverage

Each single-axis variation isolates its target criterion and fails the other three new ones:

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-13 verbatim recall** | **PASS** | PARTIAL | FAIL | FAIL | **PASS** |
| **C-14 co-located failure class** | FAIL | **PASS** | FAIL | FAIL | **PASS** |
| **C-15 register before anchor** | FAIL | FAIL | **PASS** | FAIL | **PASS** |
| **C-16 blocking ledger gate** | FAIL | FAIL | FAIL | **PASS** | **PASS** |

Projected composite: V-01 ~93, V-02 = V-03 = V-04 ~95, V-05 = 100. All Golden.

### Key discriminating tests

- **V-01 vs V-02 on C-13** — "copy exactly" (PASS) vs "recall the sentence" (PARTIAL): is the verbatim/exact-sentence instruction the load-bearing word?
- **V-02 vs V-01-R2 on C-14** — `SCORING DEFECT:` immediately after TOKEN RECALL vs "is an error" as a free sentence in the same section: does structural adjacency to TOKEN RECALL matter?
- **V-04 vs V-02-R2 on C-16** — "HALT — do not proceed" vs "Do not assemble with gaps": is the explicit HALT operative word the discriminating element for C-16?
en before ANCHOR[0] in Phase 0, HALT gate at ledger. Tests whether a concise encoding of all four patterns reliably achieves 9/9 aspirational.

---

### Rubric coverage projection (v3 — 16 criteria)

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
| C-09 audience primary flow | FAIL | FAIL | PASS | FAIL | PASS |
| C-10 token ledger | FAIL | FAIL | FAIL | PASS | PASS |
| C-11 explicit exclusion rule | PARTIAL | PASS | PARTIAL | PARTIAL | PASS |
| C-12 named anchor before analysis | PASS | PASS | PASS | PASS | PASS |
| **C-13 verbatim anchor recall** | **PASS** | PARTIAL | FAIL | FAIL | **PASS** |
| **C-14 failure class co-located** | FAIL | **PASS** | FAIL | FAIL | **PASS** |
| **C-15 register before anchor** | FAIL | FAIL | **PASS** | FAIL | **PASS** |
| **C-16 blocking ledger gate** | FAIL | FAIL | FAIL | **PASS** | **PASS** |

Key discriminators:
- V-01 vs V-02 on C-13: copy instruction (PASS) vs recall placeholder without "exact sentence" mandate (PARTIAL) — tests whether the verbatim instruction is the load-bearing element
- V-02 vs V-01-R2 on C-14: SCORING DEFECT at point of use (PASS) vs "is an error" as a free sentence (V-01-R2 C-14 FAIL) — tests whether co-location with TOKEN RECALL is required
- V-03 vs V-03-R2 on C-15: explicit Phase 0A → Phase 0B ordering with REG token recalled at recommendation (PASS) vs register-first without token recall at recommendation (tests whether recall at recommendation phase is required)
- V-04 vs V-02-R2 on C-16: "HALT — do not proceed" blocking instruction (PASS) vs "do not assemble with gaps" as a framing statement without the HALT word (R2 V-02 C-16 status to be determined by scoring)

Projected composite scores (aspirational out of 9):
- V-01: 4/4 essential, 3/3 recommended, 2.5/9 aspirational (C-08, C-12, C-13 pass; C-11 partial) → **~93**
- V-02: 4/4 essential, 3/3 recommended, 4.5/9 aspirational (C-08, C-11, C-12, C-14 pass; C-13 partial) → **~95**
- V-03: 4/4 essential, 3/3 recommended, 4.5/9 aspirational (C-08, C-09, C-12, C-15 pass; C-11 partial) → **~95**
- V-04: 4/4 essential, 3/3 recommended, 4.5/9 aspirational (C-08, C-10, C-12, C-16 pass; C-11 partial) → **~95**
- V-05: 4/4 essential, 3/3 recommended, 9/9 aspirational (all pass) → **100**

---

## V-01 — Verbatim-Copy Seal

**Axis**: Inertia framing — anchor committed as a sealed blockquote; inertia sections carry an explicit verbatim copy directive
**Hypothesis**: The C-13 criterion requires each inertia phase to reproduce the exact anchor sentence. This variation tests whether a "copy here exactly" instruction — without full token/phase machinery — is sufficient to produce C-13. The anchor is committed before analysis (C-12). The copy instruction is placed physically inside each inertia section. No token ledger, no register declaration.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

---

**SEALED ANCHOR**

What do teams do today without either option? Write one sentence. This is the baseline for all inertia comparisons.

> **ANCHOR[0]:** {status quo in one sentence}

At each inertia section below, copy this exact sentence — not a paraphrase, not a reference to "the anchor." Verbatim copy only.

---

**OPTION A: {option_a}**

**Feasibility:** Can it be built? Team capability, scope, timeline. Rate GREEN / YELLOW / RED. One sentence reason.

**Inertia:**
Verbatim anchor copy (from SEALED ANCHOR above): *{copy ANCHOR[0] here exactly}*
Compare Option A against ANCHOR[0] only — not against Option B. Would teams keep ANCHOR[0] rather than build Option A? Rate LOW / MEDIUM / HIGH. Name Option A's specific inertia mechanism.

**Risk:** Top 2 risks specific to Option A. Rate each LOW / MEDIUM / HIGH.

**Competitive positioning:** One concrete differentiator for Option A. No generic phrases.

---

**OPTION B: {option_b}**

**Feasibility:** Rate GREEN / YELLOW / RED. Independent of Option A. One sentence reason.

**Inertia:**
Verbatim anchor copy (from SEALED ANCHOR above): *{copy ANCHOR[0] here exactly}*
Compare Option B against ANCHOR[0] only — not against Option A. Would teams keep ANCHOR[0] rather than build Option B? Rate LOW / MEDIUM / HIGH. Name Option B's specific mechanism — it may differ from Option A's.

**Risk:** Top 2 risks specific to Option B. Distinct from Option A's risks, or explain overlap.

**Competitive positioning:** One concrete differentiator for Option B.

---

**DECISION MATRIX**

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | | |
| Inertia | this IS the anchor | | |
| Risk | N/A | | |
| Competitive position | baseline | | |

---

**BUILD / NO-BUILD GATE**

If both inertia ratings are HIGH: state "Build neither is a candidate recommendation." Name the override condition if you still recommend building.

---

**RECOMMENDATION**

**Recommendation: Option A / Option B / Neither / Conditional on {X}**

One sentence: why. One sentence: what is given up.

---

**AMEND**

- **Add Option C** — Analyze {option_c} on all four dimensions. At the inertia step, copy ANCHOR[0] verbatim (same copy instruction as above). Add a matrix column. Update the recommendation.
- **Weight {dimension}** — Specify dimension and multiplier. Re-score. State whether recommendation changes.
- **Audience shift** — Exec: lead with recommendation + business risk. Engineering: lead with feasibility + hardest implementation problem. Re-render.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 — Co-located Failure Class

**Axis**: Phrasing register — named violation class (`SCORING DEFECT:`) placed inside each inertia section immediately after a TOKEN RECALL line
**Hypothesis**: C-14 requires the exclusion prohibition to be a named failure class co-located with TOKEN RECALL — not only in a preamble. V-01 from R2 placed "is an error" inside each inertia phase but as a free sentence, not paired with a TOKEN RECALL. This variation tests whether a dedicated `SCORING DEFECT:` label structurally adjacent to TOKEN RECALL is the load-bearing element for C-14, without requiring full token-ledger or register machinery. C-13 is intentionally partial: TOKEN RECALL is present but the instruction says "recall" rather than "reproduce verbatim exact sentence."

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

---

**[ANCHOR DECLARATION]**

Before any option analysis, define the status quo.

`ANCHOR[0] = {what teams do today without either option — one sentence}`

Every inertia section below references this anchor by name. Do not redefine the status quo mid-analysis.

---

**[OPTION A: {option_a}]**

**Feasibility:** Team capability, scope, timeline. Rate GREEN / YELLOW / RED.

**Inertia vs ANCHOR[0]:**
TOKEN RECALL: `ANCHOR[0] = {recall the anchor sentence from above}`
SCORING DEFECT: Comparing Option A against Option B at this step is a scoring defect — Option A's inertia question is whether teams would keep the status quo recalled above rather than build Option A, not whether they prefer A over B.
Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

**Risk:** Top 2 risks specific to Option A. Rate each.

**Competitive positioning:** One concrete differentiator. No generic phrases.

---

**[OPTION B: {option_b}]**

**Feasibility:** Rate GREEN / YELLOW / RED. Independent of Option A.

**Inertia vs ANCHOR[0]:**
TOKEN RECALL: `ANCHOR[0] = {recall the anchor sentence from above}`
SCORING DEFECT: Comparing Option B against Option A at this step is a scoring defect — Option B's inertia question is whether teams would keep the status quo recalled above rather than build Option B, not whether they prefer B over A.
Rate LOW / MEDIUM / HIGH. Name Option B's inertia mechanism — it may differ from Option A's.

**Risk:** Top 2 risks specific to Option B. Must differ from Option A's, or explain overlap.

**Competitive positioning:** Distinct from Option A's, or explain overlap.

---

**[DECISION MATRIX]**

| Dimension | Option 0 (ANCHOR[0]) | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | | |
| Inertia | this IS the anchor | | |
| Risk | N/A | | |
| Competitive position | baseline | | |

---

**[BUILD / NO-BUILD GATE]**

If both inertia ratings are HIGH: state "Build neither is a candidate recommendation." Name the condition that would override this.

---

**[RECOMMENDATION]**

**Recommendation: Option A / Option B / Neither / Conditional on {X}**

One sentence: why. One sentence: trade-off.

---

**[AMEND]**

- **Add Option C** — Analyze {option_c} on all four dimensions vs ANCHOR[0]. Apply TOKEN RECALL + SCORING DEFECT at the inertia step. Add matrix column. Update recommendation.
- **Weight {dimension}** — Specify dimension and multiplier. Re-score. Note if recommendation changes.
- **Audience shift** — Exec: lead with recommendation + business risk. Engineering: lead with feasibility + hardest implementation problem.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 — Register-Prime

**Axis**: Role sequence — audience register declared as Phase 0 Part A (named token) before the status quo anchor in Part B; anchor sentence written in declared register; REG token recalled at recommendation
**Hypothesis**: C-15 requires register to be declared as a named token before ANCHOR[0] is committed, so that the anchor sentence is written in the declared register. This extends V-03 from R2 (which achieved C-09 but not C-15) by: (a) requiring the REG token to be explicitly produced before ANCHOR[0], (b) using a two-part Phase 0 structure that makes the ordering rule visible, and (c) recalling REG at the recommendation phase — making register a precondition for the full output. Tests whether this Phase 0A → Phase 0B ordering is sufficient for C-15 without a token ledger or co-located failure class.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

---

**[PHASE 0A — REGISTER]**

Declare the audience before committing any other token.

**Audience:** exec / engineering / general *(fill in, or leave blank for general)*

Register rules in effect for all phases:
- **exec**: lead every section with business impact; compress implementation detail; risk = business consequence
- **engineering**: lead every section with build complexity; expand technical depth; risk = implementation failure mode
- **general**: balanced framing; no emphasis bias

Token: `REG: {exec / engineering / general}`

This token must be committed before the status quo anchor is written. The anchor sentence will be framed for this register.

---

**[PHASE 0B — ANCHOR]**

Now write the status quo framed for the declared register.

- **exec register**: What business problem does the current approach leave unsolved?
- **engineering register**: What technical limitation does the current approach impose?
- **general**: What do teams do today without either option?

Token: `ANCHOR[0]: {status quo — one sentence, framed for REG}`

---

**[OPTION A: {option_a}]**

Apply REG framing to all four dimensions.

**Feasibility (REG-framed):** Rate GREEN / YELLOW / RED. One sentence.

**Inertia:** Compare against ANCHOR[0] only — not against Option B. Would teams keep ANCHOR[0] rather than build Option A? Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

**Risk (REG-framed):** Top 2 risks specific to Option A. Rate each. Business consequence for exec; implementation failure mode for engineering.

**Competitive positioning (REG-framed):** One concrete differentiator. Market impact for exec; technical advantage for engineering.

---

**[OPTION B: {option_b}]**

Apply REG framing independently.

**Feasibility (REG-framed):** Rate GREEN / YELLOW / RED. Independent of Option A.

**Inertia:** Compare against ANCHOR[0] only — not against Option A. Would teams keep ANCHOR[0] rather than build Option B? Rate LOW / MEDIUM / HIGH. Name Option B's mechanism — may differ from Option A's.

**Risk (REG-framed):** Top 2 risks specific to Option B, distinct from Option A's (or explain overlap).

**Competitive positioning (REG-framed):** Distinct from Option A's.

---

**[DECISION MATRIX]**

Assemble with REG-conditioned column labels.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | | |
| Inertia | this IS the anchor | | |
| Risk | N/A | | |
| Competitive position | baseline | | |

REG label overrides — exec: "Business Feasibility", "Adoption Risk", "Market Position"
REG label overrides — engineering: "Build Complexity", "Technical Risk", "Technical Differentiation"

---

**[BUILD / NO-BUILD GATE]**

If both inertia ratings are HIGH: state "Build neither is a candidate recommendation." Name the override condition if recommending a build anyway.

---

**[RECOMMENDATION]**

TOKEN RECALL: `REG: {restate register from Phase 0A}`

Apply REG framing:
- **exec**: open with **Recommendation: Option A / B / Neither** + top business risk; close with business consequence of not choosing the other option
- **engineering**: open with **Recommendation: Option A / B / Neither** + hardest feasibility constraint; close with technical trade-off
- **general**: **Recommendation: Option A / B / Neither** + matrix evidence; close with trade-off sentence

---

**[AMEND]**

- **Add Option C** — Analyze {option_c} under the same REG token and against ANCHOR[0]. Expand matrix. Update recommendation.
- **Weight {dimension}** — Specify dimension and multiplier. REG is preserved. Re-score. State if recommendation changes.
- **Override register** — State new register. Print `REG override: {new register}.` Re-render matrix labels and recommendation framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-04 — Halt-Gate Ledger

**Axis**: Output format — each phase emits a named token; the pre-assembly ledger check is a HALT GATE with an explicit blocking instruction
**Hypothesis**: C-16 requires the ledger check to include a blocking instruction ("do not proceed," "halt") that converts a missing token from a checklist item into a halted path. R2's V-02 used "Do not assemble the matrix with gaps" — a framing instruction, not an explicit halt. This variation tests whether adding "HALT — do not proceed" as the operative instruction in an otherwise standard token-ledger structure is sufficient for C-16, without requiring co-located failure class or register machinery. C-11 is intentionally partial (directional "do not reference" framing rather than a named failure class).

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each step emits a named token. Use the exact token names shown. The HALT GATE step must complete before matrix assembly proceeds.

---

**[STEP 0] STATUS QUO**

Define what teams do today without either option. One sentence.

Token: `SQ: {status quo description}`

---

**[STEP 1A] FEASIBILITY — OPTION A**

Can {option_a} be built? Team capability, scope, timeline. Rate GREEN / YELLOW / RED.

Token: `FEAS-A: {rating} — {one sentence reason}`

**[STEP 1B] FEASIBILITY — OPTION B**

Can {option_b} be built? Rate independently. Rate GREEN / YELLOW / RED.

Token: `FEAS-B: {rating} — {one sentence reason}`

---

**[STEP 2A] INERTIA — OPTION A**

Compare Option A against SQ only. Do not reference Option B at this step.
Would teams keep SQ rather than build Option A? Rate LOW / MEDIUM / HIGH. Name the mechanism.

Token: `INERT-A: {rating} — {mechanism}`

**[STEP 2B] INERTIA — OPTION B**

Compare Option B against SQ only. Do not reference Option A's inertia here.
Would teams keep SQ rather than build Option B? Rate LOW / MEDIUM / HIGH. Name Option B's specific mechanism.

Token: `INERT-B: {rating} — {mechanism}`

---

**[STEP 3A] RISK — OPTION A**

Top 2 risks specific to Option A. Rate each LOW / MEDIUM / HIGH.

Token: `RISK-A: {risk1/rating}, {risk2/rating}`

**[STEP 3B] RISK — OPTION B**

Top 2 risks specific to Option B. Must differ from RISK-A, or explain overlap.

Token: `RISK-B: {risk1/rating}, {risk2/rating}`

---

**[STEP 4A] COMPETITIVE POSITIONING — OPTION A**

Concrete differentiator(s) for Option A. No generic phrases.

Token: `COMP-A: {positioning}`

**[STEP 4B] COMPETITIVE POSITIONING — OPTION B**

Concrete differentiator(s) for Option B. Distinct from COMP-A unless overlap is explained.

Token: `COMP-B: {positioning}`

---

**[STEP 5] HALT GATE**

Scan the output above. Locate each token. Mark present (✓) or absent (✗):

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

**HALT — If any token is marked absent, do not proceed to Step 6.** Produce the missing token now. Return to this gate. Verify all pass before advancing to matrix assembly.

---

**[STEP 6] DECISION MATRIX**

Assemble from HALT GATE tokens. SQ is Option 0.

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

One sentence: why (reference a specific token). One sentence: trade-off.

---

**[AMEND]**

- **Add Option C** — Produce FEAS-C, INERT-C, RISK-C, COMP-C against the same SQ baseline. Add to HALT GATE checklist. Expand matrix. Update recommendation.
- **Weight {dimension}** — Specify dimension and multiplier. Re-score from existing tokens. Note if recommendation changes.
- **Audience shift** — Exec: re-render Step 8 leading with recommendation + business risk. Engineering: re-render Step 8 leading with feasibility + hardest implementation problem.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-05 — Tight Combined: Verbatim Recall + Co-located Failure Class + Register-Before-Anchor + Halt Gate

**Axes**: C-13 verbatim recall + C-14 co-located failure class + C-15 register before anchor + C-16 halting ledger gate — minimal encoding
**Hypothesis**: Combining all four new aspirational patterns into the tightest possible prompt maximizes the chances of a 9/9 aspirational score without over-specifying. The key interactions: REG token in Phase 0A preconditions the anchor sentence in Part B (C-15); TOKEN RECALL with "reproduce exact sentence — do not paraphrase" at each inertia phase makes drift a detectable mismatch (C-13); VIOLATION label immediately after TOKEN RECALL names the failure class at point of use (C-14); "HALT — do not proceed" at the ledger makes any gap a blocked path (C-16). Each mechanism reinforces the others: the verbatim recall also ties the anchor to the ledger; the HALT gate also enforces REG commitment.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each phase produces a named token. Use exact token names. The LEDGER GATE before matrix assembly blocks progression on any gap.

---

**PHASE 0 — FRAME**

*Part A — Register (commit first, before anchor):*

Audience: exec / engineering / general *(fill in, or leave blank for general)*

Register rules in effect for all phases:
- **exec**: lead sections with business impact; compress implementation detail; risk = business consequence
- **engineering**: lead sections with build complexity; expand technical depth; risk = implementation failure mode
- **general**: balanced framing

Token: `REG: {exec / engineering / general}`

*Part B — Anchor (commit after register; write in the declared register):*

- **exec**: what business problem does the current approach leave unsolved?
- **engineering**: what technical limitation does the current approach impose?
- **general**: what do teams do today without either option?

Token: `ANCHOR[0]: {status quo — one sentence, REG-framed}`

Binding rule: every inertia phase below must reproduce `ANCHOR[0]` verbatim as a token recall line. Do not paraphrase or summarize — use the exact sentence committed here.

Print: `Phase 0 complete. REG = {register}. ANCHOR[0] = {anchor sentence}.`

---

**PHASE 1A — FEASIBILITY: OPTION A**

Evaluate {option_a}. Apply REG framing. Rate GREEN / YELLOW / RED.

Token: `FEAS-A: {rating} — {one sentence, REG-framed}`

**PHASE 1B — FEASIBILITY: OPTION B**

Evaluate {option_b}. Apply REG framing. Independent of Option A. Rate GREEN / YELLOW / RED.

Token: `FEAS-B: {rating} — {one sentence, REG-framed}`

---

**PHASE 2A — INERTIA: OPTION A**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
VIOLATION: Comparing Option A against Option B at this phase is an error — the inertia question is whether teams would keep the status quo recalled above rather than build Option A, not whether they prefer A over B.

Would teams keep ANCHOR[0] rather than build Option A? Name Option A's specific inertia mechanism.
Rate LOW / MEDIUM / HIGH.

Token: `INERT-A: {rating} — {mechanism specific to Option A}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
VIOLATION: Comparing Option B against Option A at this phase is an error — the inertia question is whether teams would keep the status quo recalled above rather than build Option B, not whether they prefer B over A.

Would teams keep ANCHOR[0] rather than build Option B? Name Option B's specific mechanism — it may differ from Option A's.
Rate LOW / MEDIUM / HIGH.

Token: `INERT-B: {rating} — {mechanism specific to Option B}`

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

Mark each token present (✓) or absent (✗):

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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce the missing token, return to this gate, and verify all pass before advancing.

---

**PHASE 6 — DECISION MATRIX**

Assemble from LEDGER GATE tokens. Option 0 column header uses ANCHOR[0]. Apply REG to dimension labels.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEAS-A | FEAS-B |
| Inertia | this IS the anchor | INERT-A | INERT-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive | baseline | COMP-A | COMP-B |

REG overrides — exec: Feasibility → Business Feasibility; Risk → Business Risk; Competitive → Market Position
REG overrides — engineering: Feasibility → Build Complexity; Risk → Technical Risk; Competitive → Technical Differentiation

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

1. **Add Option C** — Produce tokens FEAS-C, INERT-C (with TOKEN RECALL of ANCHOR[0] verbatim + VIOLATION prohibition for comparing against A or B), RISK-C, COMP-C. Add to LEDGER GATE list. Expand Phase 6 matrix. Update Phase 8 recommendation.
2. **Weight {dimension}** — State dimension and multiplier. Re-score from existing tokens. Show whether recommendation changes.
3. **Override register** — State new register. Print `REG override: {new register}.` Re-render Phase 6 labels and Phase 8 framing.

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
| C-09 audience primary flow | FAIL | FAIL | PASS | FAIL | PASS |
| C-10 token ledger | FAIL | FAIL | FAIL | PASS | PASS |
| C-11 explicit exclusion rule | PARTIAL | PASS | PARTIAL | PARTIAL | PASS |
| C-12 named anchor before analysis | PASS | PASS | PASS | PASS | PASS |
| C-13 verbatim anchor recall | PASS | PARTIAL | FAIL | FAIL | PASS |
| C-14 failure class co-located | FAIL | PASS | FAIL | FAIL | PASS |
| C-15 register before anchor | FAIL | FAIL | PASS | FAIL | PASS |
| C-16 blocking ledger gate | FAIL | FAIL | FAIL | PASS | PASS |

**Notes on partials:**
- V-01 C-11: "Compare against ANCHOR[0] only — not against Option B" is a direction, not a named failure class; structural separation present, violation class absent
- V-02 C-13: TOKEN RECALL with "recall the anchor sentence from above" — present and named, but no "reproduce exact sentence" or "do not paraphrase" mandate; model may paraphrase
- V-03 C-11: "(Compare against ANCHOR[0] only — not against Option B)" as inline direction in each inertia section — same partial pattern as V-01
- V-04 C-11: "Do not reference Option A's inertia here" as inline direction — directional framing, no named failure class

**Key interactions to watch in scoring:**
- V-01 vs V-02 on C-13: "verbatim copy exactly" (V-01) vs "recall the anchor sentence" (V-02) — tests whether the verbatim/exact-sentence instruction is required to produce C-13, or whether a TOKEN RECALL placeholder is sufficient
- V-02 vs V-01-R2 on C-14: V-01-R2 placed "is an error" as a free sentence inside the inertia phase; V-02 places "SCORING DEFECT:" immediately after TOKEN RECALL — tests whether co-location with a recall step is the discriminating element
- V-03 on C-15: Phase 0A → Phase 0B ordering with explicit "commit register before anchor" instruction and REG recall at recommendation — tests whether the two-part Phase 0 structure alone is sufficient, without the "anchor sentence is written in the declared register" framing instruction
- V-04 on C-16: "HALT — do not proceed" as operative instruction vs R2-V-02's "Do not assemble the matrix with gaps" — tests the specific word HALT as the blocking mechanism
- V-05 interaction: 10-token ledger including REG and ANCHOR[0] means the HALT gate also enforces Phase 0 commitment — tests whether the gate scope (not just analysis tokens) affects reliability
