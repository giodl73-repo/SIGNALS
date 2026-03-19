**R4 variations written** to `simulations/quest/variations/discover-compare-variations-R4-2026-03-17.md`.

---

## discover-compare — Variations R4 Summary

R3 V-05 scored 100/100. R4 asks: *which parts of that 100/100 prompt are actually load-bearing?*

### Variation axes

| Var | Axis | Change from R3-V05 | C-13 | C-14 | C-15 | C-16 |
|-----|------|--------------------|------|------|------|------|
| V-01 | Inertia framing | Blockquote template `"{insert exact ANCHOR[0] here}"` replaces "reproduce exact sentence — do not paraphrase" directive | PARTIAL | PASS | PASS | PASS |
| V-02 | Phrasing register | `FAULT:` label instead of `VIOLATION:` | PASS | PASS | PASS | PASS |
| V-03 | Lifecycle emphasis | All explanatory prose stripped; operative directives only (~50% word reduction) | PASS | PASS | PASS | PASS |
| V-04 | Output format | Inline Phase 0 (no Part A/Part B split, no "commit first before anchor" label) | PASS | PASS | PASS | PASS |
| V-05 | Combined | V-01+V-02+V-03+V-04 simultaneously | PARTIAL | PASS | PASS | PASS |

### Key discriminating tests

- **V-01/V-05 on C-13**: Is `"insert the exact ANCHOR[0] sentence"` inside a template slot sufficient, or must the no-paraphrase mandate be inside a TOKEN RECALL directive? R3 showed "recall" alone = PARTIAL; "reproduce exact sentence — do not paraphrase" = PASS. "Insert the exact sentence" lands between them.
- **V-02 on C-14**: Does any named failure class co-located with TOKEN RECALL satisfy C-14, or does the specific label word (`VIOLATION` / `SCORING DEFECT`) carry semantic weight?
- **V-03 across all**: If compressed V-05 scores 9/9, V-05's explanatory prose is overhead. Compressed becomes the preferred form.
- **V-04 on C-15**: If inline Phase 0 (no precondition label) passes C-15, physical ordering alone satisfies it — the Part A/Part B split was defensive.

### Projected composites

All five are Golden. V-02/V-03/V-04 projected at **100**; V-01/V-05 at **~99.4** (C-13 PARTIAL). If V-02/V-03/V-04 all confirm at 100, the minimal viable 100/100 prompt becomes: compressed + inline Phase 0 + any named failure label + "do not paraphrase" in the recall directive (not a template slot).
lure class** | PASS | PASS | PASS | PASS | PASS |
| **C-15 register before anchor** | PASS | PASS | PASS | PASS | PASS |
| **C-16 blocking ledger gate** | PASS | PASS | PASS | PASS | PASS |

Key discriminating tests:

- **V-01 on C-13**: "insert the exact ANCHOR[0] sentence" (template instruction) vs "reproduce exact sentence — do not paraphrase" (directive in recall slot). Is "exact sentence" inside a template sufficient, or must the no-paraphrase mandate be inside the TOKEN RECALL directive itself?
- **V-02 on C-14**: `FAULT:` vs `VIOLATION:`. If both pass, C-14 is label-flexible — any named class co-located with TOKEN RECALL suffices.
- **V-03 across all**: if compressed V-05 preserves 9/9, V-05's explanatory prose is overhead, not load-bearing.
- **V-04 on C-15**: if inline Phase 0 (no "commit first before anchor" label) still passes C-15, then physical ordering alone is sufficient — the precondition label in R3-V05 is defensive, not required.
- **V-05 combined**: if C-13 is the only partial, it confirms all other simplifications are independently safe.

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
| C-09 audience primary flow | PASS | PASS | PASS | PASS | PASS |
| C-10 token ledger | PASS | PASS | PASS | PASS | PASS |
| C-11 explicit exclusion rule | PASS | PASS | PASS | PASS | PASS |
| C-12 named anchor before analysis | PASS | PASS | PASS | PASS | PASS |
| **C-13 verbatim anchor recall** | **PARTIAL** | PASS | PASS | PASS | **PARTIAL** |
| **C-14 failure class co-located** | PASS | PASS | PASS | PASS | PASS |
| **C-15 register before anchor** | PASS | PASS | PASS | PASS | PASS |
| **C-16 blocking ledger gate** | PASS | PASS | PASS | PASS | PASS |

Projected composite scores (partial = 0.5):

- V-01: 4/4 essential, 3/3 recommended, 8.5/9 aspirational → **~99.4** (Golden)
- V-02: 4/4 essential, 3/3 recommended, 9/9 aspirational → **100** (Golden)
- V-03: 4/4 essential, 3/3 recommended, 9/9 aspirational → **100** (Golden)
- V-04: 4/4 essential, 3/3 recommended, 9/9 aspirational → **100** (Golden)
- V-05: 4/4 essential, 3/3 recommended, 8.5/9 aspirational → **~99.4** (Golden)

If V-01 C-13 is PARTIAL: template "exact text" slot is weaker than co-located "do not paraphrase" —
confirming the no-paraphrase mandate at point of use is required.
If V-01 C-13 is PASS: structural quoting is sufficient and the explicit mandate is redundant.

---

## V-01 — Template Anchor Slot

**Axis**: Inertia framing — structural template quoting (`"{paste exact anchor sentence here}"`) replaces the
explicit "do not paraphrase" directive in the TOKEN RECALL slot
**Hypothesis**: R3 confirmed that "reproduce exact sentence — do not paraphrase" co-located with TOKEN RECALL
achieves C-13. This variation tests whether a structural fill-in template that says "paste exact text"
achieves C-13 without the explicit no-paraphrase mandate. All other R3-V05 patterns preserved: VIOLATION
label, HALT gate, Phase 0A → 0B register-before-anchor. The template is a blockquote slot with the
instruction "paste exact text" inside the fill-in marker.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each phase produces a named token. Use exact token names. The LEDGER GATE before matrix assembly
blocks progression on any gap.

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

Binding rule: every inertia phase below must reproduce `ANCHOR[0]` at the TOKEN RECALL step.
Use the exact text of the anchor sentence — do not rephrase or shorten.

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

TOKEN RECALL — paste exact text of ANCHOR[0]:
> ANCHOR[0]: "{insert the exact ANCHOR[0] sentence here}"

VIOLATION: Comparing Option A against Option B at this phase is an error — the inertia question
is whether teams would keep the status quo pasted above rather than build Option A, not whether
they prefer A over B.

Would teams keep ANCHOR[0] rather than build Option A? Name Option A's specific inertia mechanism.
Rate LOW / MEDIUM / HIGH.

Token: `INERT-A: {rating} — {mechanism specific to Option A}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL — paste exact text of ANCHOR[0]:
> ANCHOR[0]: "{insert the exact ANCHOR[0] sentence here}"

VIOLATION: Comparing Option B against Option A at this phase is an error — the inertia question
is whether teams would keep the status quo pasted above rather than build Option B, not whether
they prefer B over A.

Would teams keep ANCHOR[0] rather than build Option B? Name Option B's specific mechanism — it
may differ from Option A's.
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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce the missing token, return to
this gate, and verify all pass before advancing.

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

TOKEN RECALL: `ANCHOR[0] = {paste exact anchor sentence from Phase 0}`
TOKEN RECALL: `REG = {restate register from Phase 0}`

Apply REG framing:
- **exec**: open with **Recommendation: Option A / B / Neither** + top business risk from RISK tokens; close with one-line business consequence of not choosing the other option
- **engineering**: open with **Recommendation: Option A / B / Neither** + hardest constraint from FEAS tokens; close with technical trade-off
- **general**: **Recommendation: Option A / B / Neither** + matrix evidence; close with trade-off sentence

If recommendation diverges from matrix plurality, state the override reason explicitly.

---

**PHASE 9 — AMEND**

Three paths:

1. **Add Option C** — Produce tokens FEAS-C, INERT-C (with TOKEN RECALL template of ANCHOR[0] exact text + VIOLATION prohibition for comparing against A or B), RISK-C, COMP-C. Add to LEDGER GATE list. Expand Phase 6 matrix. Update Phase 8 recommendation.
2. **Weight {dimension}** — State dimension and multiplier. Re-score from existing tokens. Show whether recommendation changes.
3. **Override register** — State new register. Print `REG override: {new register}.` Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-02 — FAULT Label

**Axis**: Phrasing register — `FAULT:` label replaces `VIOLATION:` at each inertia phase's exclusion
prohibition; all other R3-V05 patterns preserved verbatim
**Hypothesis**: C-14 requires a named failure class co-located with TOKEN RECALL. R3 confirmed `VIOLATION:`
achieves this; R2 confirmed `SCORING DEFECT:` achieves this. This variation tests label flexibility: if
`FAULT:` also passes C-14, the criterion is label-agnostic — any named class at the right location
suffices. If `FAULT:` fails, the specific word class matters (VIOLATION / SCORING DEFECT > FAULT).
The only change from R3-V05 is the label word at Phases 2A and 2B.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each phase produces a named token. Use exact token names. The LEDGER GATE before matrix assembly
blocks progression on any gap.

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

Binding rule: every inertia phase below must reproduce `ANCHOR[0]` verbatim as a token recall line.
Do not paraphrase or summarize — use the exact sentence committed here.

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
FAULT: Comparing Option A against Option B at this phase is a fault — the inertia question
is whether teams would keep the status quo recalled above rather than build Option A, not
whether they prefer A over B.

Would teams keep ANCHOR[0] rather than build Option A? Name Option A's specific inertia mechanism.
Rate LOW / MEDIUM / HIGH.

Token: `INERT-A: {rating} — {mechanism specific to Option A}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
FAULT: Comparing Option B against Option A at this phase is a fault — the inertia question
is whether teams would keep the status quo recalled above rather than build Option B, not
whether they prefer B over A.

Would teams keep ANCHOR[0] rather than build Option B? Name Option B's specific mechanism — it
may differ from Option A's.
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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce the missing token, return to
this gate, and verify all pass before advancing.

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

1. **Add Option C** — Produce tokens FEAS-C, INERT-C (with TOKEN RECALL of ANCHOR[0] verbatim + FAULT prohibition for comparing against A or B), RISK-C, COMP-C. Add to LEDGER GATE list. Expand Phase 6 matrix. Update Phase 8 recommendation.
2. **Weight {dimension}** — State dimension and multiplier. Re-score from existing tokens. Show whether recommendation changes.
3. **Override register** — State new register. Print `REG override: {new register}.` Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-03 — Compressed V-05

**Axis**: Lifecycle emphasis — V-05 stripped to operative instructions and token slots only; all
explanatory prose removed (register rule descriptions, binding rule sentences, conditional framing
instructions, REG override tables, phase print confirmation)
**Hypothesis**: R3-V05's explanatory prose (the register rule table, the "Binding rule" sentence,
the `Print:` confirmation, the conditional framing guidance in Phase 8, the REG override lists in
Phase 6) may be redundant. The load-bearing elements are: the operative token directives, the
ordering rule (Phase 0A before 0B), the TOKEN RECALL + VIOLATION pair, and the HALT instruction.
If compressed V-05 achieves 9/9, the explanatory prose is defensive overhead. If any criterion
degrades, the prose was structural scaffolding.
Target: approximately 50% word reduction vs R3-V05.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each phase produces a named token. Use exact token names. LEDGER GATE blocks progression on any gap.

---

**PHASE 0 — FRAME**

*Part A — Register (before anchor):*

Token: `REG: {exec / engineering / general}`

*Part B — Anchor (after register, written for REG):*

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
VIOLATION: Comparing Option A against Option B at this phase is an error — inertia asks whether
teams would keep ANCHOR[0] rather than build Option A, not whether they prefer A over B.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} — {mechanism}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
VIOLATION: Comparing Option B against Option A at this phase is an error — inertia asks whether
teams would keep ANCHOR[0] rather than build Option B, not whether they prefer B over A.

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

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation." Name override condition or conclude Neither.

---

**PHASE 8 — RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence — do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 9 — AMEND**

1. **Add Option C** — Produce FEAS-C, INERT-C (TOKEN RECALL of ANCHOR[0] verbatim + VIOLATION prohibition), RISK-C, COMP-C. Add to ledger. Expand matrix. Update recommendation.
2. **Weight {dimension}** — Dimension and multiplier. Re-score from tokens. State if recommendation changes.
3. **Override register** — `REG override: {new register}.` Re-render Phase 6 labels and Phase 8 framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

---

## V-04 — Inline Phase 0

**Axis**: Output format — Phase 0 is a single block committing both REG and ANCHOR[0] tokens in
sequence; the Part A / Part B split and the "commit first, before anchor" precondition label are removed;
all other R3-V05 patterns preserved verbatim
**Hypothesis**: C-15 requires register to be declared as a named token before ANCHOR[0] is committed.
R3-V05 satisfies this with an explicit "Part A — Register (commit first, before anchor)" label. This
variation tests whether physical ordering alone — REG token appears before ANCHOR[0] token in the
same Phase 0 block — satisfies C-15 without the precondition label. If PASS, C-15 only requires
ordering, not an explicit ordering rule. If PARTIAL or FAIL, the precondition label or the Part A/Part B
split is structurally required.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Each phase produces a named token. Use exact token names. The LEDGER GATE before matrix assembly
blocks progression on any gap.

---

**PHASE 0 — FRAME**

Declare audience register, then commit status quo anchor framed for that register.

Audience: exec / engineering / general *(fill in, or leave blank for general)*

Register rules in effect for all phases:
- **exec**: lead sections with business impact; compress implementation detail; risk = business consequence
- **engineering**: lead sections with build complexity; expand technical depth; risk = implementation failure mode
- **general**: balanced framing

Token: `REG: {exec / engineering / general}`

Now write the status quo for the declared register:
- **exec**: what business problem does the current approach leave unsolved?
- **engineering**: what technical limitation does the current approach impose?
- **general**: what do teams do today without either option?

Token: `ANCHOR[0]: {status quo — one sentence, REG-framed}`

Binding rule: every inertia phase below must reproduce `ANCHOR[0]` verbatim as a token recall line.
Do not paraphrase or summarize — use the exact sentence committed here.

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
VIOLATION: Comparing Option A against Option B at this phase is an error — the inertia question
is whether teams would keep the status quo recalled above rather than build Option A, not
whether they prefer A over B.

Would teams keep ANCHOR[0] rather than build Option A? Name Option A's specific inertia mechanism.
Rate LOW / MEDIUM / HIGH.

Token: `INERT-A: {rating} — {mechanism specific to Option A}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0 — do not paraphrase}`
VIOLATION: Comparing Option B against Option A at this phase is an error — the inertia question
is whether teams would keep the status quo recalled above rather than build Option B, not
whether they prefer B over A.

Would teams keep ANCHOR[0] rather than build Option B? Name Option B's specific mechanism — it
may differ from Option A's.
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

**HALT — do not proceed to Phase 6 if any token is absent.** Produce the missing token, return to
this gate, and verify all pass before advancing.

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

## V-05 — Combined: Template Quoting + FAULT Label + Compressed + Inline Phase 0

**Axes**: All four R4 simplifications simultaneously — V-01 template quoting, V-02 FAULT label,
V-03 compressed prose, V-04 inline Phase 0
**Hypothesis**: Each single-axis simplification is expected to preserve 9/9 aspirational except V-01
(C-13 PARTIAL). Combined, C-13 is still the expected partial — the other three simplifications do not
help or hurt C-13, which depends solely on whether "insert the exact ANCHOR[0] sentence" in the
template slot satisfies the verbatim mandate. If C-13 remains the only partial, all four simplifications
are independently safe and the combined form is the minimal viable 100/100 candidate (once C-13 is
resolved by the scoring result). If additional criteria degrade, the simplifications interact adversely.

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

TOKEN RECALL — paste exact text of ANCHOR[0]:
> ANCHOR[0]: "{insert the exact ANCHOR[0] sentence here}"

FAULT: Comparing Option A against Option B at this phase is a fault — inertia asks whether
teams would keep the status quo pasted above rather than build Option A, not whether they prefer
A over B.

Rate LOW / MEDIUM / HIGH. Name Option A's inertia mechanism.

Token: `INERT-A: {rating} — {mechanism}`

**PHASE 2B — INERTIA: OPTION B**

TOKEN RECALL — paste exact text of ANCHOR[0]:
> ANCHOR[0]: "{insert the exact ANCHOR[0] sentence here}"

FAULT: Comparing Option B against Option A at this phase is a fault — inertia asks whether
teams would keep the status quo pasted above rather than build Option B, not whether they prefer
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

If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation." Name override or conclude Neither.

---

**PHASE 8 — RECOMMENDATION**

TOKEN RECALL: `ANCHOR[0] = {paste exact anchor sentence — do not paraphrase}`
TOKEN RECALL: `REG = {restate register}`

**Recommendation: Option A / B / Neither / Conditional on {X}**

REG-framed. One sentence: why. One sentence: trade-off.

---

**PHASE 9 — AMEND**

1. **Add Option C** — Produce FEAS-C, INERT-C (TOKEN RECALL template of ANCHOR[0] exact text + FAULT prohibition), RISK-C, COMP-C. Add to ledger. Expand matrix. Update recommendation.
2. **Weight {dimension}** — Dimension and multiplier. Re-score from tokens. State if recommendation changes.
3. **Override register** — `REG override: {new register}.` Re-render Phase 6 labels and Phase 8 framing.

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
| **C-13 verbatim anchor recall** | **PARTIAL** | PASS | PASS | PASS | **PARTIAL** |
| **C-14 failure class co-located** | PASS | PASS | PASS | PASS | PASS |
| **C-15 register before anchor** | PASS | PASS | PASS | PASS | PASS |
| **C-16 blocking ledger gate** | PASS | PASS | PASS | PASS | PASS |

### Projected composite scores

| Variation | Essential (4) | Recommended (3) | Aspirational (/9) | Composite | Golden |
|-----------|--------------|-----------------|-------------------|-----------|--------|
| V-01 | 4/4 = 60 | 3/3 = 30 | 8.5/9 = 9.44 | **99.44** | YES |
| V-02 | 4/4 = 60 | 3/3 = 30 | 9/9 = 10.00 | **100.00** | YES |
| V-03 | 4/4 = 60 | 3/3 = 30 | 9/9 = 10.00 | **100.00** | YES |
| V-04 | 4/4 = 60 | 3/3 = 30 | 9/9 = 10.00 | **100.00** | YES |
| V-05 | 4/4 = 60 | 3/3 = 30 | 8.5/9 = 9.44 | **99.44** | YES |

*Partial = 0.5. Aspirational normalized: passed * 10 / 9.*

### Key discriminating results to watch

**V-01 and V-05 on C-13**: The blockquote template `"{insert the exact ANCHOR[0] sentence here}"` uses
"exact sentence" as the instruction. R3 showed that "recall the anchor sentence" (without "exact") is
PARTIAL; "reproduce exact sentence — do not paraphrase" is PASS. "Insert the exact sentence" lands
between these two. The scoring result will show whether "exact" in the fill-in instruction is sufficient,
or whether the no-paraphrase mandate co-located with a TOKEN RECALL directive (not a template slot) is
the discriminating element.

**V-02 on C-14**: `FAULT:` is a named class label co-located with TOKEN RECALL. If PASS, C-14 accepts
any named class label. If FAIL, `VIOLATION:` / `SCORING DEFECT:` carry semantic weight beyond bare
labeling — stronger failure-class words may be required.

**V-03 across all criteria**: If 9/9 aspirational, V-05's explanatory prose is confirmed overhead.
Compressed V-05 becomes the preferred form: simpler, same coverage.

**V-04 on C-15**: If PASS, the Part A/Part B split in R3-V05 is confirmed defensive (not required).
Inline Phase 0 with register-before-anchor ordering is sufficient.

**V-02 + V-03 + V-04 convergence**: If all three achieve 100/100, the minimal viable prompt is
V-05 of R4 (compressed + inline Phase 0 + FAULT label) minus the C-13 partial — resolved by keeping
the "do not paraphrase" mandate inside the recall slot rather than in a template instruction.
