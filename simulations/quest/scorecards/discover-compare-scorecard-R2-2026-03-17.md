## discover-compare — Round 2 Scorecard

### Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 Explicit Exclusion | 4/4 | 3/3 | 2.5/5 | **95** | YES |
| V-02 Token Ledger | 4/4 | 3/3 | 3/5 | **96** | YES |
| V-03 Audience-First | 4/4 | 3/3 | 3/5 | **96** | YES |
| V-04 Minimal Anchor | 4/4 | 3/3 | 2.5/5 | **95** | YES |
| V-05 Combined | 4/4 | 3/3 | 5/5 | **100** | YES |

**Rank: V-05 > V-02 = V-03 > V-01 = V-04**

### Aspirational Profile

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 Option 0 in matrix | PASS | PASS | PASS | PASS | PASS |
| C-09 Audience primary flow | FAIL | FAIL | **PASS** | FAIL | **PASS** |
| C-10 Token ledger | FAIL | **PASS** | FAIL | FAIL | **PASS** |
| C-11 Explicit exclusion rule | **PASS** | PARTIAL | PARTIAL | PARTIAL | **PASS** |
| C-12 Named anchor before analysis | PARTIAL | PARTIAL | PARTIAL | **PASS** | **PASS** |

All 5 variations are Golden (all essential pass, composite ≥ 80). The single-axis variations isolate which aspirational each axis reliably delivers — V-03 proves audience-first alone is sufficient for C-09; V-04 proves the anchor declaration alone is sufficient for C-12.

### Excellence Signals from V-05

1. **Verbatim TOKEN RECALL** — ANCHOR[0] must be reproduced exactly at each inertia phase, not referenced by name. Drift becomes a token mismatch, not a prose-level judgment.
2. **"is an error" co-located with TOKEN RECALL** — Both enforcement mechanisms at the same point in the inertia phase. The exclusion is a named failure class, not a direction.
3. **Audience before anchor** — REG declared as Phase 0 Part A before ANCHOR[0]. The status quo sentence is register-framed; the gate propagates to the recommendation via REG token recall.
4. **Ledger as assembly gate** — "Do not proceed with gaps" converts a missing token from an oversight into a blocked path.

### Key Discriminating Finding

V-01's "is an error" (C-11 PASS) vs V-04's parenthetical "(not against Option A)" (C-11 PARTIAL) cleanly validates the v2 rubric tightening: the error-class framing is structurally different from a direction, and the rubric correctly distinguishes them.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["verbatim token recall at each inertia phase makes baseline drift detectable as token mismatch rather than prose-level judgment", "explicit 'is an error' prohibition co-located inside inertia phase alongside TOKEN RECALL creates two enforcement mechanisms at the point of use", "audience declared before status quo anchor makes register a precondition for all subsequent framing including the anchor sentence itself", "ledger check as assembly gate not just checklist — 'do not proceed with gaps' converts missing score from oversight to structurally blocked path"]}
```
Compare Option A against SQ only." STEP 2B: "Compare Option B against SQ only. Do not reference Option A's inertia here." Each phase emits its own token |
| C-03 decision matrix | PASS | STEP 6 assembled from LEDGER CHECK tokens; "SQ is Option 0" with named column |
| C-04 explicit recommendation | PASS | STEP 8 requires explicit recommendation with token reference justification; override reason required if recommendation diverges from matrix evidence |
| C-05 build/no-build gate | PASS | STEP 7: "If INERT-A = HIGH and INERT-B = HIGH: state 'Build neither is a candidate recommendation.'" Token-keyed threshold check |
| C-06 differentiated risk | PASS | "Must differ from RISK-A, or explain overlap" — named token convention makes identical copy-paste detectable at ledger step |
| C-07 actionable AMEND | PASS | Three concrete paths: Add Option C with full token production (FEAS-C, INERT-C, RISK-C, COMP-C + ledger update), Weight dimension from existing tokens, Shift audience via re-render of STEP 8 only |
| C-08 Option 0 in matrix | PASS | STEP 6 matrix column labeled "Option 0 (SQ)"; both options scored against it; SQ token committed before analysis at STEP 0 |
| C-09 audience in primary flow | FAIL | "Shift audience" is an AMEND path only; primary output has no register declaration |
| C-10 token ledger at assembly | PASS | 9 named tokens (SQ, FEAS-A/B, INERT-A/B, RISK-A/B, COMP-A/B) emitted per phase; STEP 5 LEDGER CHECK requires all listed and marked present before assembly; "Do not assemble the matrix with gaps" |
| C-11 explicit exclusion rule | PARTIAL | STEP 2B: "Do not reference Option A's inertia here" — directional framing, not a stated prohibition with the word "error"; structural separation present, sentence-level rule absent |
| C-12 named anchor before analysis | PARTIAL | `SQ:` token committed at STEP 0 before any option analysis; however no binding rule requires inertia phases to reproduce the SQ token verbatim — phases can say "compare against SQ only" without recalling the sentence |

**Essential: 4/4 → 60 | Recommended: 3/3 → 30 | Aspirational: 3/5 → 6**
**Composite: 96 | Golden: YES**

---

#### V-03 — Audience-First Register

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 bilateral dimensions | PASS | OPTION A and OPTION B sections each require all four dimensions; dimension questions listed identically for both to prevent omission |
| C-02 independent inertia | PASS | "Inertia (vs. status quo — not vs. Option B)" and "Inertia (vs. status quo — not vs. Option A)" — directional markers enforce per-option comparison scope |
| C-03 decision matrix | PASS | DECISION MATRIX section with full table; column labels conditioned on declared register |
| C-04 explicit recommendation | PASS | RECOMMENDATION section with explicit per-register framing; all three register variants require opening with stated recommendation |
| C-05 build/no-build gate | PASS | BUILD/NO-BUILD GATE: "If both inertia ratings are HIGH: state 'Build neither is a candidate recommendation.'" |
| C-06 differentiated risk | PASS | "Top 2 risks specific to Option B, distinct from Option A's risks (or explain overlap)" — distinct mandate enforced |
| C-07 actionable AMEND | PASS | Three concrete paths: Add Option C with same register and status quo, Weight dimension with recalculation, Override register with re-render instruction |
| C-08 Option 0 in matrix | PASS | STATUS QUO section defines baseline before options; matrix column header "Status Quo" with "anchor" label on inertia row |
| C-09 audience in primary flow | PASS | REGISTER DECLARATION is the first section before status quo; register rules apply "throughout this output"; matrix column labels change per register (exec/engineering); recommendation framing branches explicitly per register; "Do not switch register mid-output" — not deferred to AMEND |
| C-10 token ledger at assembly | FAIL | No named output tokens emitted per phase; no LEDGER CHECK before matrix assembly; analysis flows as prose only |
| C-11 explicit exclusion rule | PARTIAL | "(vs. status quo — not vs. Option B)" as parenthetical in section label — directional but not a stated prohibition; direction given, violation class not named |
| C-12 named anchor before analysis | PARTIAL | STATUS QUO section precedes option analysis; matrix inertia row labeled "anchor"; but not committed as a named token (no ANCHOR[0]) and inertia phases reference "status quo" without recalling it by name |

**Essential: 4/4 → 60 | Recommended: 3/3 → 30 | Aspirational: 3/5 → 6**
**Composite: 96 | Golden: YES**

---

#### V-04 — Minimal Anchor Structure

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 bilateral dimensions | PASS | BILATERAL ANALYSIS section lists all four dimensions for Option A before starting Option B; "Complete all four for Option A before starting Option B" prevents partial coverage |
| C-02 independent inertia | PASS | "Inertia vs ANCHOR[0] — Would teams keep ANCHOR[0] rather than build Option B? (Compare against ANCHOR[0], not against Option A.)" — each option has its own inertia verdict scoped to the anchor |
| C-03 decision matrix | PASS | MATRIX + GATE section has a four-row table with ANCHOR[0] as the status quo column |
| C-04 explicit recommendation | PASS | RECOMMENDATION + AMEND requires "Option A / Option B / Neither / Conditional on {X}" |
| C-05 build/no-build gate | PASS | Gate: "if both inertia ratings are HIGH, state whether 'build neither' applies and what condition would change this" |
| C-06 differentiated risk | PASS | "Must differ from Option A's, or explain why they are the same" — differentiation enforced |
| C-07 actionable AMEND | PASS | Three concrete AMEND paths: Option C vs ANCHOR[0] with matrix column, Weight with multiplier and recalculation, Audience shift with re-render instruction |
| C-08 Option 0 in matrix | PASS | "ANCHOR[0]" is the column header for the status quo column in MATRIX + GATE; the label is the token name itself |
| C-09 audience in primary flow | FAIL | "Audience shift" is an AMEND path only; primary output has no register declaration or conditional branching |
| C-10 token ledger at assembly | FAIL | No named output tokens emitted per phase; no LEDGER CHECK step |
| C-11 explicit exclusion rule | PARTIAL | "(Compare against ANCHOR[0], not against Option B.)" as parenthetical — closer than V-03's heading notation, but not an "is an error" level prohibition; direction given, violation not named |
| C-12 named anchor before analysis | PASS | "ANCHOR DECLARATION: Before analysis: ... `ANCHOR[0] = {status quo in one sentence}`. Every inertia assessment below measures pull away from ANCHOR[0]. Reference this token by name in each inertia section." — named token, dedicated pre-analysis phase, explicit binding rule |

**Essential: 4/4 → 60 | Recommended: 3/3 → 30 | Aspirational: 2.5/5 → 5**
**Composite: 95 | Golden: YES**

---

#### V-05 — Combined: Token Ledger + Explicit Exclusion + Named Anchor + Audience-Primary

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 bilateral dimensions | PASS | Phases 1A/1B, 2A/2B, 3A/3B, 4A/4B cover all four dimensions per option; PHASE 5 LEDGER CHECK cross-verifies all 8 analysis tokens |
| C-02 independent inertia | PASS | PHASE 2A: "Comparing Option A against Option B at this phase is an error." PHASE 2B: same prohibition for B. TOKEN RECALL of ANCHOR[0] at each inertia phase makes independent anchoring verifiable |
| C-03 decision matrix | PASS | PHASE 6 matrix assembled from LEDGER CHECK tokens; Option 0 column labeled with ANCHOR[0]; register-conditional dimension labels |
| C-04 explicit recommendation | PASS | PHASE 8 opens with "Recommendation: Option A / B / Neither" per all three register variants; TOKEN RECALL of ANCHOR[0] at recommendation phase |
| C-05 build/no-build gate | PASS | PHASE 7: "If INERT-A = HIGH and INERT-B = HIGH: State: 'Build neither is a candidate recommendation.'" Token-keyed condition |
| C-06 differentiated risk | PASS | "Must be distinct from RISK-A, or explain overlap" — named tokens make copy-paste detectable at ledger |
| C-07 actionable AMEND | PASS | PHASE 9 AMEND: Add Option C with full token production + TOKEN RECALL + same exclusion rule, Weight from existing tokens, Override register with explicit re-render |
| C-08 Option 0 in matrix | PASS | PHASE 0 commits `ANCHOR[0]`; PHASE 6 matrix uses "Option 0: ANCHOR[0]" as column header — status quo is named and anchored to the declared token |
| C-09 audience in primary flow | PASS | PHASE 0 Part A declares `REG:` token BEFORE the anchor; register rules "in effect for all phases"; PHASE 6 matrix dimension labels change per register; PHASE 8 recommendation has explicit per-register framing branches; REG token recalled at output phase — not deferred to AMEND |
| C-10 token ledger at assembly | PASS | 10 named tokens (REG, ANCHOR[0], FEAS-A/B, INERT-A/B, RISK-A/B, COMP-A/B); PHASE 5 LEDGER CHECK lists all with presence markers; "Do not proceed to matrix assembly with gaps" — gap is structurally visible before comparison artifact is produced |
| C-11 explicit exclusion rule | PASS | PHASE 2A: "Comparing Option A against Option B at this phase is an error — the question is whether teams would keep ANCHOR[0] rather than build Option A, not whether they prefer A over B." PHASE 2B: mirror prohibition. "is an error" at sentence level inside each inertia phase |
| C-12 named anchor before analysis | PASS | PHASE 0 Part B commits `ANCHOR[0]` before any option analysis; "Binding rule: every inertia phase below must reproduce ANCHOR[0] verbatim as a token recall line. Do not paraphrase or summarize." PHASES 2A, 2B, and 8 all carry "TOKEN RECALL: `ANCHOR[0] = {reproduce exact sentence from Phase 0}`" |

**Essential: 4/4 → 60 | Recommended: 3/3 → 30 | Aspirational: 5/5 → 10**
**Composite: 100 | Golden: YES**

---

### Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 Explicit Exclusion | 4/4 | 3/3 | 2.5/5 | **95** | YES |
| V-02 Token Ledger | 4/4 | 3/3 | 3/5 | **96** | YES |
| V-03 Audience-First | 4/4 | 3/3 | 3/5 | **96** | YES |
| V-04 Minimal Anchor | 4/4 | 3/3 | 2.5/5 | **95** | YES |
| V-05 Combined | 4/4 | 3/3 | 5/5 | **100** | YES |

**Rank: V-05 > V-02 = V-03 > V-01 = V-04**

Aspirational profile:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 Option 0 in matrix | PASS | PASS | PASS | PASS | PASS |
| C-09 Audience primary flow | FAIL | FAIL | PASS | FAIL | PASS |
| C-10 Token ledger | FAIL | PASS | FAIL | FAIL | PASS |
| C-11 Explicit exclusion rule | PASS | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-12 Named anchor before analysis | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |

---

### Excellence Signals from V-05

**1. Verbatim TOKEN RECALL as drift detection** — ANCHOR[0] is not referenced by name at inertia phases; it is reproduced exactly: "reproduce exact sentence from Phase 0." Baseline drift becomes a token mismatch — structurally detectable before any scoring. V-01 through V-04 reference or imply the status quo; V-05 requires verbatim re-statement, making substitution visible.

**2. "is an error" as named violation class** — The C-11 exclusion rule in V-05 names the violation: "Comparing Option A against Option B at this phase is an error." This elevates the prohibition from a direction ("do not do X") to a stated error class with a checkable condition. Co-located with the TOKEN RECALL, both enforcement mechanisms apply at the same point — the inertia phase — not in separate structural layers.

**3. Audience declared before anchor — register as precondition** — PHASE 0 Part A (REG token) precedes Part B (ANCHOR[0] token). The status quo sentence is framed for the declared register: exec framing ("business problem left unsolved") vs. engineering framing ("technical limitation imposed"). V-03 achieves audience-first, but only V-05 propagates register framing into the anchor sentence itself and recalls REG at the recommendation phase.

**4. Ledger gates assembly, not just confirms** — V-02 requires listing tokens; V-05 adds "Do not proceed to matrix assembly with gaps" as an explicit gate condition. The ledger becomes a blocking guard, not a checklist. With 10 tokens including REG and ANCHOR[0], the gate also enforces that audience and anchor are committed — not just the eight analysis scores.

**5. Three-layer C-02 enforcement** — Declare (ANCHOR[0] committed before analysis), Recall (verbatim TOKEN RECALL at each inertia phase), Constrain ("is an error" prohibition inside each inertia phase). Each layer catches a different slippage mode: forgotten anchor → token missing at ledger; paraphrased anchor → recall mismatch; relative comparison → named error class. No single-axis variation achieves more than one layer.

---

### Discriminating Findings

**V-01 vs V-04 on C-11** — V-01's "is an error" (PASS) vs V-04's parenthetical "(not against Option A)" (PARTIAL). The parenthetical is a direction; the "is an error" sentence is a stated rule. Applied inside the inertia phase, the "is an error" formulation provides a checkable condition rather than a stylistic reminder.

**V-02 on C-11/C-12** — LEDGER CHECK delivers C-10 (visible gaps at assembly) without pulling C-11 or C-12 to full passes. "Do not reference Option A's inertia here" is a framing instruction, not an error prohibition. And `SQ:` without a verbatim-recall binding rule leaves inertia phases free to paraphrase.

**V-03 on C-09** — The only single-axis variation to achieve a full C-09 pass. Audience-before-status-quo (REGISTER DECLARATION first) is sufficient for C-09 without the full phase architecture of V-05. Establishes audience-first ordering as an independently valuable pattern.

**V-04 on C-12** — The only single-axis variation to achieve a full C-12 pass. ANCHOR DECLARATION syntax + "Reference this token by name in each inertia section" binding rule is sufficient for C-12 without ledger or exclusion sentence support. Confirms the anchor naming pattern as the load-bearing element for C-12.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["verbatim token recall at each inertia phase makes baseline drift detectable as token mismatch rather than prose-level judgment", "explicit 'is an error' prohibition co-located inside inertia phase alongside TOKEN RECALL creates two enforcement mechanisms at the point of use", "audience declared before status quo anchor makes register a precondition for all subsequent framing including the anchor sentence itself", "ledger check as assembly gate not just checklist — 'do not proceed with gaps' converts missing score from oversight to structurally blocked path"]}
```
