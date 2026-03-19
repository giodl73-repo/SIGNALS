---

## discover-compare R5 Scorecard

### Scores

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 9.5/10 = 9.50 | **99.50** | YES |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 10/10 = 10.00 | **100.00** | YES |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 9.5/10 = 9.50 | **99.50** | YES |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 9.5/10 = 9.50 | **99.50** | YES |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 10/10 = 10.00 | **100.00** | YES |

---

### Key Testing Resolutions

**C-11 (condensed FAULT)**: **PASS.** `FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.` satisfies C-11. The dual-polarity form (positive: ANCHOR[0] basis; negative: inter-option prohibited) is the complete exclusion rule. V-03 confirms in isolation — condensed FAULT passes C-11 independently. The explanatory clause ("inertia asks whether teams would keep the status quo...") was overhead, not structural.

**C-07 (tokenized AMEND)**: **PASS.** Token slot declarations for all three amendment paths satisfy "concrete instructions." The tokenized form is more actionable than prose path descriptions, not less.

**C-17 delta confirmed**: The three prose elements in V-01 (preamble sentence, Phase 0 framing, FAULT explanatory clause) each cost 0 aspirational points individually but collectively cost the full 0.5 for PARTIAL. Stripping all three (V-02, V-05) closes the gap to 100/100. The Phase 9 prose-style AMEND in V-01/V-02/V-03 does NOT trigger C-17 PARTIAL — it is operative-directive form, not explanatory prose.

---

### Excellence Signals (from V-02/V-05)

1. **Dual-polarity FAULT as single operative directive** — encodes both polarities (ANCHOR[0]-only basis + inter-option prohibition) in one line; satisfies C-11 AND removes the last explanatory clause from the inertia phases
2. **Bare token ordering satisfies C-15** — physical `REG:` before `ANCHOR[0]:` in Phase 0 is sufficient; framing sentences are confirmed overhead across C-15, C-09, and C-12
3. **Tokenized AMEND is more actionable than prose AMEND** — slot declarations with inline TOKEN RECALL + FAULT at Phase 9 make the amendment path self-contained; practitioner can execute without re-reading primary phases
4. **V-05 is the R5 minimal viable 100/100 candidate** — ~40% shorter than V-01, all 17 criteria at PASS or better, no interaction effects between the three compression axes

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dual-polarity FAULT directive satisfies C-11 without explanatory clause — positive (ANCHOR[0] basis) plus negative (inter-option prohibited) in one line is the minimal form", "Tokenized AMEND with inline TOKEN RECALL and FAULT prohibitions satisfies C-07 and is more actionable than prose path descriptions", "Bare token ordering in Phase 0 satisfies C-15 register-before-anchor without framing prose — physical declaration sequence is sufficient enforcement"]}
```
s remain: (1) `"Each phase produces a named token."` — preamble framing; (2) `"Declare audience register, then commit status quo anchor framed for that register."` + `"Audience: exec / engineering / general *(fill in, or leave blank for general)*"` — Phase 0 framing; (3) FAULT explanatory clause `"— inertia asks whether teams would keep the status quo recalled above rather than build Option A, not whether they prefer A over B."` — binding rationale |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 9.5/10 = 9.50 | **Composite**: 99.50 | **Golden**: YES

---

### V-02 — C-17 Full Strip

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 bilateral dimensions | PASS | All eight phases (1A/1B through 4A/4B) preserved unchanged |
| C-02 independent inertia | PASS | Phase 2A and 2B each separate |
| C-03 decision matrix | PASS | Phase 6 matrix preserved |
| C-04 explicit recommendation | PASS | Phase 8 recommendation format preserved |
| C-05 build/no-build gate | PASS | Phase 7 preserved |
| C-06 differentiated risk | PASS | Phase 3B constraint preserved |
| C-07 actionable AMEND | PASS | Phase 9 unchanged from V-01; numbered paths with concrete slot instructions |
| C-08 Option 0 in matrix | PASS | Phase 6 preserved |
| C-09 audience primary flow | PASS | REG declared in Phase 0; Phase 8 REG-framed |
| C-10 token ledger cross-check | PASS | Phase 5 HALT + Phase 6 token assembly + Phase 8 TOKEN RECALLs |
| C-11 explicit exclusion rule | **PASS** | Condensed FAULT: `"FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error."` states both polarities: positive (ANCHOR[0] basis = status quo basis) and negative (inter-option comparison prohibited). C-11 requires "explicit 'compare against status quo, not against Option [X]' prohibition." ANCHOR[0] is the named status quo; the dual-polarity form satisfies the exclusion rule without the explanatory clause. The explanatory clause was overhead. |
| C-12 named anchor before analysis | PASS | Phase 0 ANCHOR[0] before Phase 1A |
| C-13 verbatim anchor recall | PASS | TOKEN RECALL + "do not paraphrase" co-located in Phase 2A, 2B, Phase 8 |
| C-14 failure class co-located | PASS | `FAULT:` label co-located with TOKEN RECALL at each inertia phase |
| C-15 register before anchor | PASS | Phase 0: REG token before ANCHOR[0] token; framing prose stripped but bare token ordering satisfies the criterion |
| C-16 blocking ledger gate | PASS | HALT directive preserved |
| C-17 output compressed | **PASS** | All three prose elements stripped: preamble sentence gone, Phase 0 framing sentences gone, FAULT explanatory clause condensed to dual-polarity directive. Remaining text is operative directives only: token declarations, TOKEN RECALL instructions, FAULT prohibitions, HALT gate, assembly directives. Phase 9 prose AMEND is action-directive form (not explanatory prose — no binding rationale, no rule descriptions). |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 10/10 = 10.00 | **Composite**: 100.00 | **Golden**: YES

---

### V-03 — FAULT Condensed (Single-Axis Isolation)

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 bilateral dimensions | PASS | All phases preserved, only FAULT text changed |
| C-02 independent inertia | PASS | Phases 2A/2B separate |
| C-03 decision matrix | PASS | Phase 6 preserved |
| C-04 explicit recommendation | PASS | Phase 8 preserved |
| C-05 build/no-build gate | PASS | Phase 7 preserved |
| C-06 differentiated risk | PASS | Phase 3B: stronger constraint than V-01 ("Top 2 risks specific to Option B. Must differ from RISK-A or explain overlap.") |
| C-07 actionable AMEND | PASS | Phase 9 V-01-style prose with three concrete paths |
| C-08 Option 0 in matrix | PASS | Phase 6 Option 0 column |
| C-09 audience primary flow | PASS | Phase 8 has REG-frame application expanded with exec/engineering/general specific instructions |
| C-10 token ledger cross-check | PASS | Phase 5 HALT + Phase 6 assembly + Phase 8 TOKEN RECALLs |
| C-11 explicit exclusion rule | **PASS** | Condensed FAULT identical to V-02: `"FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error."` C-11 isolation confirmed: the condensed form is independently sufficient. The dual-polarity directive (ANCHOR[0] only + no inter-option) satisfies the exclusion rule without requiring the explanatory clause. |
| C-12 named anchor before analysis | PASS | Phase 0 ANCHOR[0] before analysis phases |
| C-13 verbatim anchor recall | PASS | TOKEN RECALL + no-paraphrase mandate co-located |
| C-14 failure class co-located | PASS | `FAULT:` label co-located at inertia phases |
| C-15 register before anchor | PASS | Phase 0 framing preserved; REG before ANCHOR[0] |
| C-16 blocking ledger gate | PASS | HALT directive preserved |
| C-17 output compressed | **PARTIAL** | FAULT clause condensed but preamble sentence (`"Each phase produces a named token."`) and Phase 0 framing (`"Declare audience register, then commit status quo anchor framed for that register."` + `"Audience: exec / engineering / general *(fill in, or leave blank for general)*"`) are preserved. These two elements constitute explanatory prose co-present with operative content. |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 9.5/10 = 9.50 | **Composite**: 99.50 | **Golden**: YES

---

### V-04 — AMEND Tokenized

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 bilateral dimensions | PASS | Phases 1A/1B through 4A/4B preserved unchanged from V-01 |
| C-02 independent inertia | PASS | Phases 2A/2B separate |
| C-03 decision matrix | PASS | Phase 6 preserved |
| C-04 explicit recommendation | PASS | Phase 8 preserved |
| C-05 build/no-build gate | PASS | Phase 7 preserved |
| C-06 differentiated risk | PASS | Phase 3B constraint preserved |
| C-07 actionable AMEND | **PASS** | Tokenized Phase 9 provides actual token slot declarations for all three paths: Option C expansion with `Token: FEAS-C:`, `TOKEN RECALL: ANCHOR[0] =`, `FAULT: compare against ANCHOR[0] only`, `Token: INERT-C:`, `Token: RISK-C:`, `Token: COMP-C:` — plus `WEIGHT: {dimension} x {multiplier}` and `REG override: {new register}` tokens. Token slot form is more concrete than prose descriptions. C-07 requires "concrete instructions for at least one of: adding a third option..." — all three paths have concrete slot structure. PASS. |
| C-08 Option 0 in matrix | PASS | Phase 6 Option 0 column |
| C-09 audience primary flow | PASS | REG token Phase 0; Phase 8 REG-framed |
| C-10 token ledger cross-check | PASS | Phase 5 HALT + Phase 6 assembly + Phase 8 TOKEN RECALLs |
| C-11 explicit exclusion rule | PASS | V-01's full FAULT form with explanatory clause — unambiguous C-11 PASS |
| C-12 named anchor before analysis | PASS | Phase 0 ANCHOR[0] before analysis |
| C-13 verbatim anchor recall | PASS | TOKEN RECALL + no-paraphrase mandate co-located |
| C-14 failure class co-located | PASS | `FAULT:` label at inertia phases + FAULT in Phase 9 Option C expansion |
| C-15 register before anchor | PASS | REG before ANCHOR[0] in Phase 0 |
| C-16 blocking ledger gate | PASS | HALT directive preserved |
| C-17 output compressed | **PARTIAL** | Three V-01 prose elements preserved: preamble sentence, Phase 0 framing (two sentences), FAULT explanatory clause. Tokenized Phase 9 removes prose path descriptions but the three identified prose elements remain. C-17 PARTIAL — operative directives present alongside explanatory scaffolding. |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 9.5/10 = 9.50 | **Composite**: 99.50 | **Golden**: YES

---

### V-05 — Combined (C-17 Strip + FAULT Condensed + AMEND Tokenized)

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-01 bilateral dimensions | PASS | All bilateral phases preserved |
| C-02 independent inertia | PASS | Phases 2A/2B separate |
| C-03 decision matrix | PASS | Phase 6 preserved |
| C-04 explicit recommendation | PASS | Phase 8 preserved |
| C-05 build/no-build gate | PASS | Phase 7 preserved |
| C-06 differentiated risk | PASS | Phase 3B constraint preserved |
| C-07 actionable AMEND | **PASS** | Tokenized Phase 9 identical to V-04 — all three paths as concrete token slot declarations. No adverse interaction from combining with V-02 stripping; AMEND section is independent of preamble/Phase 0 framing. |
| C-08 Option 0 in matrix | PASS | Phase 6 Option 0 column |
| C-09 audience primary flow | PASS | REG declared as bare token slot; Phase 8 TOKEN RECALL of REG for framing |
| C-10 token ledger cross-check | PASS | Phase 5 HALT + Phase 6 token assembly + Phase 8 dual TOKEN RECALLs |
| C-11 explicit exclusion rule | **PASS** | Condensed FAULT: `"FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error."` No adverse interaction with other V-02 stripping — C-11 confirmed by V-03 isolation: condensed form passes independently. V-05 confirms the same result with all other prose stripped. |
| C-12 named anchor before analysis | PASS | Phase 0 ANCHOR[0] as bare token before Phase 1A |
| C-13 verbatim anchor recall | PASS | TOKEN RECALL + "do not paraphrase" co-located at Phase 2A, 2B, Phase 8 |
| C-14 failure class co-located | PASS | `FAULT:` label co-located at inertia phases (Phase 2A, 2B) and in Phase 9 Option C expansion |
| C-15 register before anchor | PASS | Bare token ordering in Phase 0: `REG:` before `ANCHOR[0]:` — framing stripped but physical ordering satisfies C-15 (confirmed by R4 V-04) |
| C-16 blocking ledger gate | PASS | HALT directive preserved |
| C-17 output compressed | **PASS** | No explanatory prose remains: preamble sentence stripped, Phase 0 framing stripped, FAULT explanatory clause condensed, Phase 9 prose path descriptions replaced by token slot declarations. All content is operative directives: token declarations, TOKEN RECALL instructions, FAULT prohibitions, HALT gate, assembly directives, conditional logic. |

**Essential**: 4/4 = 60.00 | **Recommended**: 3/3 = 30.00 | **Aspirational**: 10/10 = 10.00 | **Composite**: 100.00 | **Golden**: YES

---

## Ranking

| Rank | Variation | Composite | Delta from V-01 |
|------|-----------|-----------|-----------------|
| 1 | V-02 | 100.00 | +0.50 |
| 1 | V-05 | 100.00 | +0.50 |
| 3 | V-01 | 99.50 | — (baseline) |
| 3 | V-03 | 99.50 | 0.00 |
| 3 | V-04 | 99.50 | 0.00 |

V-02 and V-05 tie at 100/100. V-05 is preferred for production as it combines all improvements (compressed + tokenized AMEND), but both are equivalent on composite.

---

## Key Testing Resolutions

### C-11: PASS for condensed dual-polarity FAULT

**Question**: Does `FAULT: compare against ANCHOR[0] only — Option A vs Option B comparison is an error.` satisfy C-11 without the explanatory clause?

**Verdict**: **PASS.** C-11 requires "explicit 'compare against status quo, not against Option [X]' prohibition stated as a rule." The condensed form maps: `ANCHOR[0]` = status quo, `"Option A vs Option B comparison is an error"` = prohibition of relative comparison. Both polarities are present as a named directive. V-03 confirms this in isolation (only FAULT condensed, all other prose preserved) — C-11 passes even without the explanatory clause. The clause `"— inertia asks whether teams would keep the status quo recalled above rather than build Option A, not whether they prefer A over B"` was binding rationale overhead, not structural for C-11.

**Impact**: V-02 and V-05 can condense FAULT without losing C-11. The dual-polarity one-liner is the minimal form that satisfies both C-11 and C-17.

### C-07: PASS for tokenized AMEND

**Question**: Does Phase 9 as pure token expansion satisfy C-07's "concrete instructions" requirement?

**Verdict**: **PASS.** C-07 requires "concrete instructions for at least one of: adding a third option, weighting a specific dimension, adjusting for exec vs engineering audience." Token slot declarations are maximally concrete — they give the exact token names, TOKEN RECALL directives, FAULT prohibitions, and action instructions. V-04 confirms in isolation; V-05 confirms no interaction effects. The prose path descriptions in V-01/V-02/V-03 Phase 9 were structurally equivalent overhead.

**Impact**: V-04 and V-05 tokenized AMEND satisfies C-07. Prose descriptions of what tokens to produce are confirmed overhead.

### C-15: PASS for bare token ordering without framing prose

**Confirmed**: Stripping `"Declare audience register, then commit status quo anchor framed for that register."` and `"Audience: exec / engineering / general"` does not affect C-15. Physical `REG:` before `ANCHOR[0]:` ordering in Phase 0 is sufficient. (Consistent with R4 V-04 finding carried forward.)

---

## Excellence Signals (from V-02 and V-05)

**Signal 1: Dual-polarity FAULT as single operative directive**
`FAULT: compare against ANCHOR[0] only — Option X vs Option Y comparison is an error.` encodes both the positive constraint (compare against status quo named token) and the negative prohibition (no inter-option) in one directive line. Satisfies C-11 AND contributes to C-17 by eliminating rationale prose. The explanatory clause ("inertia asks whether teams would keep the status quo...") was overhead — the polarity pair is self-sufficient.

**Signal 2: Bare token slot ordering satisfies register-before-anchor (C-15)**
Phase 0 needs only:
```
Token: `REG: {exec / engineering / general}`
Token: `ANCHOR[0]: {status quo — one sentence, REG-framed}`
```
The physical token declaration order is the constraint enforcement. No framing sentence required. Stripping the framing sentences does not break C-15, C-09, or any other criterion that depends on register handling.

**Signal 3: Tokenized AMEND is more concrete than prose AMEND**
Phase 9 with actual token slot declarations (`Token: FEAS-C:`, `TOKEN RECALL: ANCHOR[0] =`, `FAULT: compare against ANCHOR[0] only`, etc.) provides more actionable structure than prose path descriptions. The tokenized form makes the amendment path self-contained — a practitioner can execute the amendment without re-reading the primary phases. This satisfies C-07 and improves usability independent of rubric score.

**Signal 4: V-05 is the minimal viable 100/100 prompt under v4**
V-05 achieves 100/100 at approximately 40% fewer words than V-01 (R4 canonical). Every operative mechanism is preserved; every explanatory element is removed. No interaction effects between the three compression axes (preamble strip, FAULT condensation, AMEND tokenization). This is the R5 production candidate.

---

## Scorecard Worksheet

```
V-01:
  Essential passed:    4 / 4   =>  4 * 60 / 4  = 60.00
  Recommended passed:  3 / 3   =>  3 * 30 / 3  = 30.00
  Aspirational passed: 9.5/10  =>  9.5 * 10/10 = 9.50
  Composite: 99.50 — GOLDEN

V-02:
  Essential passed:    4 / 4   =>  4 * 60 / 4  = 60.00
  Recommended passed:  3 / 3   =>  3 * 30 / 3  = 30.00
  Aspirational passed: 10/10   =>  10 * 10/10  = 10.00
  Composite: 100.00 — GOLDEN

V-03:
  Essential passed:    4 / 4   =>  4 * 60 / 4  = 60.00
  Recommended passed:  3 / 3   =>  3 * 30 / 3  = 30.00
  Aspirational passed: 9.5/10  =>  9.5 * 10/10 = 9.50
  Composite: 99.50 — GOLDEN

V-04:
  Essential passed:    4 / 4   =>  4 * 60 / 4  = 60.00
  Recommended passed:  3 / 3   =>  3 * 30 / 3  = 30.00
  Aspirational passed: 9.5/10  =>  9.5 * 10/10 = 9.50
  Composite: 99.50 — GOLDEN

V-05:
  Essential passed:    4 / 4   =>  4 * 60 / 4  = 60.00
  Recommended passed:  3 / 3   =>  3 * 30 / 3  = 30.00
  Aspirational passed: 10/10   =>  10 * 10/10  = 10.00
  Composite: 100.00 — GOLDEN
```
