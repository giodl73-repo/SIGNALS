## discover-compare R8 — Scorecard

### Summary

| Variation | Axis | C-12 | C-17 | Composite | Golden |
|-----------|------|------|------|-----------|--------|
| V-01 | Baseline | PASS | PASS | **100.00** | YES |
| V-02 | Phase-label-free | **PASS** | PASS | **100.00** | YES |
| V-03 | Inline-frame | **FAIL** | PASS | **99.29** | YES |
| V-04 | AMEND sub-ledger | PASS | PASS | **100.00** | YES |
| V-05 | Recommendation-first | PASS | PASS | **100.00** | YES |

### Key Resolutions

**V-02 C-12: PASS** (upper branch confirmed) — "Dedicated phase" = structurally separate block, not a labeled block. The `---` divider between ANCHOR[0] and the first FEAS directive is the structural boundary. Phase labels are cosmetic, not operative.

**V-03 C-12: FAIL** (confirmed) — Token ordering within a single phase satisfies C-15 but not C-12. Structural separation is required. V-02/V-03 together bracket the definition precisely.

**V-04 C-20: PASS** — Token-name listing in a mini-ledger is structural verification, not TOKEN RECALL. The sub-ledger is invisible to C-20.

**V-05: 100.00** — Recommendation-before-matrix satisfies all 21 criteria unchanged. No criterion encodes phase-ordering constraints on recommendation vs. matrix.

### Projected vs. Actual

5/5 hypotheses confirmed. V-02 resolves to upper branch (phase labels fully inert).

### Three New Patterns

1. **phase-labels-inert** — structural separation (token block + divider) satisfies C-12 without a labeled header
2. **recommendation-first-valid** — reordering recommendation before matrix scores identically; no criterion is phase-order-sensitive
3. **sub-ledger-benign** — token-name listing in a blocking gate does not fire C-20 over-recall

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase-labels-inert: removing PHASE N -- NAME headers while preserving structural separation (token declarations + section divider before analysis tokens) satisfies C-12 dedicated-phase without a labeled header -- phase labels are cosmetic, not operative (confirmed V-02)", "recommendation-first-valid: reordering recommendation before decision matrix satisfies all 21 criteria unchanged; no criterion specifies phase ordering; exec-register-aligned natively (confirmed V-05)", "sub-ledger-benign: blocking mini-ledger listing token names inside Add-C path is a structural verification gate, not TOKEN RECALL -- does not fire C-20 over-recall (confirmed V-04)"]}
```
ion A vs Option B comparison is an error" |
| C-12 | Named anchor before analysis | PASS | PHASE 0 (FRAME) is a dedicated phase declaring ANCHOR[0] before PHASE 1A |
| C-13 | Verbatim anchor recall | PASS | TOKEN RECALL with "reproduce exact sentence from Phase 0 -- do not paraphrase" co-located at PHASE 2A and 2B |
| C-14 | Failure class co-located | PASS | "FAULT:" label appears immediately after TOKEN RECALL in each inertia phase |
| C-15 | Register before anchor | PASS | PHASE 0: REG declared, then ANCHOR[0] declared |
| C-16 | Blocking ledger gate | PASS | "HALT -- do not proceed to Phase 6 if any token is absent" |
| C-17 | Output compressed | PASS | All content is token declarations, recall instructions, directives, verdict slots; no rule tables or rationale prose |
| C-18 | Dual-polarity FAULT | PASS | "compare against ANCHOR[0] only -- Option A vs Option B comparison is an error" encodes positive mandate + negative prohibition in one line |
| C-19 | AMEND self-contained | PASS | Each AMEND path has inline TOKEN RECALL + FAULT: Add-C (ANCHOR[0] + FAULT), Weight (ANCHOR[0] + FAULT), Override (REG + FAULT) |
| C-20 | Path-scoped TOKEN RECALL | PASS | Add-C recalls ANCHOR[0] only; Weight recalls ANCHOR[0] only; Override recalls REG only -- each path recalls its operational minimum |
| C-21 | FAULT propagates to AMEND | PASS | Add-C: dual-polarity; Weight: dual-polarity; Override: dual-polarity -- all three paths carry C-18 form |

**Essential: 4/4 = 60.00 | Recommended: 3/3 = 30.00 | Aspirational: 14/14 = 10.00 | Composite: 100.00**

---

#### V-02 — Phase-label-free

Identical to V-01 except all **PHASE N -- NAME** headers removed. Token ordering, dividers, and operative content preserved verbatim.

**C-12 resolution (primary R8 question): PASS**

Pass condition: "defined as a named anchor in a dedicated phase before any option analysis begins."

V-02 frame block:
```
Token: `REG: {exec / engineering / general}`
Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

---

Rate GREEN / YELLOW / RED. REG-framed.
Token: `FEAS-A: {rating} -- {one sentence}`
```

The REG and ANCHOR[0] declarations form a structurally separate block (bounded by a `---` divider) before any analysis tokens. The anchor is explicitly declared as a named token. The fail condition targets "baseline defined inline during inertia phases, or implied rather than declared" -- neither applies. The label **PHASE 0 -- FRAME** was organizing, not operative. Structural separation via section divider satisfies "dedicated phase." PASS.

**C-17 resolution: PASS**

Phase headers (**PHASE N -- NAME**) are section labels, not explanatory prose. C-17 targets "rule description tables, binding rationale sentences, Print: confirmations, preamble framing." Phase labels do not fall in these categories. Removing them is neutral to C-17. PASS.

All other criteria: operative content identical to V-01. PASS for all.

**Essential: 4/4 = 60.00 | Recommended: 3/3 = 30.00 | Aspirational: 14/14 = 10.00 | Composite: 100.00**

---

#### V-03 — Inline-frame

REG and ANCHOR[0] merged into the top of PHASE 1A. All other V-01 elements preserved.

**C-12: FAIL**

Pass condition: "defined as a named anchor in a dedicated phase before any option analysis begins."

V-03 structure:
```
**PHASE 1A -- FEASIBILITY: OPTION A**

Token: `REG: {exec / engineering / general}`
Token: `ANCHOR[0]: {status quo -- one sentence, REG-framed}`

Rate GREEN / YELLOW / RED. REG-framed.
Token: `FEAS-A: {rating} -- {one sentence}`
```

ANCHOR[0] is declared inside PHASE 1A -- the same labeled phase as FEAS-A. There is no structurally separate frame block. Token ordering satisfies C-15 (REG before ANCHOR[0]) but not C-12 ("dedicated phase" requires its own structural block, separate from the first analysis phase). The anchor is declared within an analysis phase. FAIL.

**C-15: PASS** -- "Physical token ordering in a single inline phase satisfies this criterion." REG declared before ANCHOR[0] within Phase 1A. PASS.

All other criteria: PHASE 1B through PHASE 9 preserved identical to V-01. PASS for all.

**Essential: 4/4 = 60.00 | Recommended: 3/3 = 30.00 | Aspirational: 13/14 = 9.29 | Composite: 99.29**

---

#### V-04 — AMEND Sub-ledger

Identical to V-01 except Add-C path gains a blocking mini-ledger after the four C tokens:
```
Add-C ledger: FEAS-C [ ]  INERT-C [ ]  RISK-C [ ]  COMP-C [ ]
```
**HALT -- do not extend Phase 6 matrix if any Add-C token is absent.**

**C-19: PASS (strengthened)** -- Add-C path now has inline TOKEN RECALL + FAULT + blocking sub-ledger. More self-contained than V-01. Weight and Override paths unchanged. PASS.

**C-20: PASS** -- Mini-ledger lists token names (FEAS-C, INERT-C, RISK-C, COMP-C) for structural verification. This is a blocking gate, not TOKEN RECALL. TOKEN RECALL reclaims token values via `TOKEN RECALL: X = {value}` syntax. No token values recalled in the ledger; no over-recall introduced. Add-C still recalls ANCHOR[0] only for its inertia execution. PASS.

**C-16: PASS** -- Two blocking gates now present: Phase 5 primary LEDGER GATE and Add-C sub-ledger. Both have HALT instructions. C-16 is satisfied and additive.

All other criteria: identical to V-01. PASS for all.

**Essential: 4/4 = 60.00 | Recommended: 3/3 = 30.00 | Aspirational: 14/14 = 10.00 | Composite: 100.00**

---

#### V-05 — Recommendation-first

Identical to V-01 except RECOMMENDATION moved before DECISION MATRIX. Phase renumbering:
- Phase 5: LEDGER GATE (unchanged)
- Phase 6: RECOMMENDATION (was Phase 8)
- Phase 7: DECISION MATRIX (was Phase 6)
- Phase 8: BUILD/NO-BUILD GATE (was Phase 7)
- Phase 9: AMEND (unchanged, references updated to Phase 7 matrix and Phase 6 recommendation)

**C-04: PASS** -- Recommendation (now Phase 6) remains explicit: "Recommendation: Option A / B / Neither / Conditional on {X}". PASS.

**C-03: PASS** -- Decision matrix (now Phase 7) still present as structured table. PASS.

**C-05: PASS** -- Build/no-build gate (now Phase 8) fires on dual-HIGH inertia and can "revise Phase 6 recommendation to Neither." PASS.

**C-09: PASS** -- C-09 states exec output "leads with recommendation and business risk." Moving recommendation before the matrix is natively exec-register-aligned. PASS.

**C-10: PASS** -- Matrix assembly (Phase 7) still "Assemble from LEDGER GATE tokens." LEDGER GATE (Phase 5) validates all tokens before both recommendation and matrix. PASS.

No criterion specifies that recommendation must follow the decision matrix. All 21 criteria are phase-order-agnostic with respect to recommendation vs. matrix ordering.

All other criteria: operative content identical to V-01. PASS for all.

**Essential: 4/4 = 60.00 | Recommended: 3/3 = 30.00 | Aspirational: 14/14 = 10.00 | Composite: 100.00**

---

### Scoring Worksheet

Aspirational: PASS=1.0, PARTIAL=0.5; denominator=14; weight=10

| Variation | Essential 4/4 | Recommended 3/3 | Aspirational /14 | Composite |
|-----------|--------------|-----------------|-----------------|-----------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 13/14 = 9.29  | **99.29**  |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 14/14 = 10.00 | **100.00** |

---

### Projected vs. Actual

| Hypothesis | Projected | Actual | Match |
|------------|-----------|--------|-------|
| V-01 stable 100.00 | 100.00 | 100.00 | YES |
| V-02 C-12: PASS (structural separation without label) | 99.29-100.00 | 100.00 | YES -- upper branch |
| V-02 C-17: PASS (headers are not explanatory prose) | PASS | PASS | YES |
| V-03 C-12: FAIL (inline-frame breaks dedicated phase) | 99.29 | 99.29 | YES |
| V-04 C-20: PASS (sub-ledger is gate, not TOKEN RECALL) | 100.00 | 100.00 | YES |
| V-05 all criteria: PASS (phase ordering not constrained) | 100.00 | 100.00 | YES |

5 of 5 primary hypotheses confirmed. V-02 resolves to the upper branch: phase labels are fully inert.

---

### Key Resolutions

**V-02 C-12: PASS** -- "Dedicated phase" means a structurally separate block, not a labeled block. The `---` divider between ANCHOR[0] and the first FEAS directive is the structural boundary. Phase labels (**PHASE 0 -- FRAME**) are cosmetic organizers, not load-bearing for C-12 compliance.

**V-03 C-12: FAIL** -- Confirmed. Merging REG and ANCHOR[0] into PHASE 1A (the feasibility phase) fails the "dedicated phase" requirement. Token ordering within a single phase satisfies C-15 but not C-12. Structural separation is required; token ordering alone is insufficient.

**V-02/V-03 bracket C-12's definition** -- V-02 preserves structural separation without labels (PASS); V-03 removes structural separation entirely (FAIL). "Dedicated phase" = structurally separate block before the first analysis section. Label presence is inert.

**V-04 C-20: PASS** -- Token-name listing in a blocking mini-ledger is structural verification, not TOKEN RECALL. C-20 over-recall requires `TOKEN RECALL: X = {value}` syntax adding tokens beyond operational need. The sub-ledger is invisible to C-20.

**V-05: 100.00** -- Recommendation-before-matrix is a valid alternative ordering. C-09's exec-register framing ("leads with recommendation") is natively satisfied. No criterion encodes phase-ordering constraints on recommendation vs. matrix.

---

### Excellence Signals (from 100.00 variations: V-01, V-02, V-04, V-05)

1. **Phase labels are cosmetic** -- the operative mechanism for C-12 is structural separation (a block of frame tokens before the first analysis section, bounded by a divider), not a labeled phase header. Label-free prompts reach 100/100.
2. **Recommendation-first is a valid alternative form** -- no criterion is phase-order-sensitive with respect to recommendation vs. matrix. Moving recommendation before matrix is natively exec-register-aligned and scores identically to recommendation-after-matrix.
3. **Sub-ledger strengthens self-containment without side effects** -- a blocking mini-ledger inside an AMEND path adds structural verification (C-19) without introducing C-20 over-recall. Token-name presence in a ledger is structurally distinct from TOKEN RECALL value recall.

---

### Key Decisions for R9

1. **C-12 settled** -- "Dedicated phase" = structurally separate block. Phase labels are inert. V-02/V-03 pair fully brackets this definition. No further tests needed on this axis.
2. **Phase ordering proven inert** -- V-05 confirms rubric is phase-order-agnostic for recommendation vs. matrix. No open questions.
3. **Sub-ledger proven benign** -- V-04 closes the C-20 over-recall question for blocking verification gates.
4. **R9 pivot options**: All R8 axes resolved. Candidates: (a) multi-option extension -- Add-C path fully executed with concrete tokens; (b) audience-register differentiation -- exec vs. engineering register in same output; (c) edge cases in C-13 verbatim recall -- paraphrase drift detection under high inertia framing.
