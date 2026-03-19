Now I have all the information needed. Let me score each variation.

---

## discover-compare R19 — Scoring Results

### Rubric Version: v17 | Base Denominator: /33 | Target Criteria: C-39, C-40

---

### Per-Variation Criterion Scoring

#### V-01 — Baseline carry at /31

**Essential Criteria** (all PASS):

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | FEAS-A/B, INERT-A/B, RISK-A/B, COMP-A/B all present for both options |
| C-02 | PASS | Separate INERT-A and INERT-B with independent FAULT directives at each site |
| C-03 | PASS | Explicit 4×4 matrix with ANCHOR[0] column |
| C-04 | PASS | `**Recommendation: Option A / B / Neither / Conditional on {X}**` |

**Recommended Criteria** (all PASS):

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | `If INERT-A = HIGH and INERT-B = HIGH: state "Build neither is a candidate recommendation."` |
| C-06 | PASS | RISK-B instructs "Distinct from RISK-A or explain overlap" |
| C-07 | PASS | Three concrete AMEND paths with slot structure |

**Aspirational Criteria** — Denominator: /33 − C-39 N/S − C-40 N/S = **/31**

| ID | Verdict | Evidence |
|----|---------|----------|
| C-08 | PASS | `Option 0: ANCHOR[0]` column present in matrix |
| C-09 | PASS | REG token declared; routing deviation for engineering; TOKEN RECALL: REG at recommendation |
| C-10 | PASS | `Assemble from LEDGER GATE tokens` with named token references in matrix cells |
| C-11 | PASS | FAULT: compare against ANCHOR[0] only — inter-option comparison named as error at each inertia site |
| C-12 | PASS | ANCHOR[0] declared as named token before any analysis token in structural order |
| C-13 | PASS | TOKEN RECALL with `reproduce exact sentence from above -- do not paraphrase` co-located at each inertia phase |
| C-14 | PASS | FAULT: label co-located with TOKEN RECALL at each inertia phase |
| C-15 | PASS | REG declared before ANCHOR[0] in token sequence |
| C-16 | PASS | `**HALT -- do not proceed if any token is absent.**` blocking instruction present |
| C-17 | PASS | Pure directives: token declarations, recall instructions, FAULT prohibitions, blocking gates, verdict labels only |
| C-18 | PASS | `FAULT: compare against ANCHOR[0] only -- Option A vs Option B comparison is an error.` — positive mandate + negative prohibition in one line |
| C-19 | PASS | All three AMEND paths carry inline TOKEN RECALL + FAULT |
| C-20 | PASS | Add-C/Weight recall ANCHOR[0]; Override register recalls REG only — path-scoped correctly |
| C-21 | PASS | All three AMEND path FAULTs encode dual-polarity: positive mandate + negative prohibition |
| C-22 | PASS | Phase separation via `---` dividers and operative token positioning; no PHASE N headers |
| C-23 | PASS | RECOMMENDATION section precedes DECISION MATRIX in body; BODY ORDER unconditional |
| C-24 | PASS | Fenced-code ledger block at each AMEND path before HALT instruction |
| C-25 | PASS | ROUTING: deviation-only scope + DEVIATION: engineering branch; exec ordering established by BODY ORDER; combined construct covers both register values |
| C-26 | PASS | RECOMMENDATION precedes DECISION MATRIX in body by design; exec-safe without routing |
| C-27 | PASS | Routing block appears after LEDGER GATE |
| C-28 | PASS | BODY ORDER directive and routing block are structurally isolated; each self-contained |
| C-29 | PASS | `BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` — unconditional form |
| C-30 | PASS | Routing block contains only engineering deviation branch; exec not re-specified |
| C-31 | PASS | `DECISION MATRIX precedes RECOMMENDATION` — positional vocabulary, no layer-name reference |
| C-32 | PASS | `ROUTING: deviation from BODY ORDER only.` scope declaration present |
| C-33 | PASS | `Token: BODY-ORDER-LAYER: active` standalone declaration present |
| C-34 | PASS | Fenced-code block form at each AMEND path; enumeration separable from HALT instruction |
| C-35 | PASS | `any of the above tokens is absent` — positional reference language at all three paths |
| C-36 | PASS | `DEVIATION:` marker on engineering branch instruction |
| C-37 | PASS | Identical phrase `any of the above tokens is absent` at all three AMEND path HALTs |
| C-38 | PASS | `DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION` — deviation marker + positional vocabulary paired in same line |
| C-39 | **N/S** | C-37 PASS, but no `AMEND-HALT:` declaration token present → gate condition not met → −1 denominator |
| C-40 | **N/S** | C-38 PASS, but no `BRANCH-RULE:` declaration before routing block → gate condition not met → −1 denominator |

**Score:**
- Essential: 4/4 × 60 = **60.00**
- Recommended: 3/3 × 30 = **30.00**
- Aspirational: 31/31 × 10 = **10.00**
- **Composite: 100.00** | Golden: **Yes**

---

#### V-02 — C-39 only: AMEND-HALT declaration + token recall at each path

**Essential / Recommended**: Identical to V-01 — all PASS → **60.00 + 30.00**

**Aspirational** — Denominator: /33 − C-40 N/S = **/32**

Changes from V-01:

| ID | Verdict | Evidence |
|----|---------|----------|
| C-37 | PASS | All three AMEND paths use identical token reference `{AMEND-HALT}` — uniform by declaration |
| C-39 | **PASS** | `AMEND-HALT: "any of the above tokens is absent"` declared before AMEND block; each path HALT uses `{AMEND-HALT}` by token name — declaration-before-use + token-name recall both satisfied |
| C-40 | **N/S** | C-38 PASS but no `BRANCH-RULE:` declaration → gate not met → −1 denominator |

All other 29 aspirational criteria carry from V-01 at PASS.

**Score:**
- Essential: 4/4 × 60 = **60.00**
- Recommended: 3/3 × 30 = **30.00**
- Aspirational: 32/32 × 10 = **10.00**
- **Composite: 100.00** | Golden: **Yes**

---

#### V-03 — C-39 failure: AMEND-HALT declared, paths use literal phrase

**Essential / Recommended**: Identical to V-01 — all PASS → **60.00 + 30.00**

**Aspirational** — Denominator: /33 − C-40 N/S = **/32**

Changes from V-01:

| ID | Verdict | Evidence |
|----|---------|----------|
| C-37 | PASS | All three paths use identical literal phrase `any of the above tokens is absent` — uniform by inspection |
| C-39 | **FAIL** | `AMEND-HALT:` declaration present before AMEND block — declaration condition met. BUT each path HALT reads `**HALT -- do not {action} if any of the above tokens is absent.**` — literal string, not token-name recall (`{AMEND-HALT}`). Rubric: "each path's halt instruction references it by token name... rather than reproducing a manually-typed copy." Literal reproduction of declared value ≠ token-name recall. `c39-declaration-architecture` watch list pattern: C-37 PASS (uniformity-by-inspection) + C-39 FAIL (no uniformity-by-declaration) are distinct scored states |
| C-40 | **N/S** | C-38 PASS but no `BRANCH-RULE:` declaration → gate not met → −1 denominator |

All other 29 aspirational criteria carry from V-01 at PASS.

**Score:**
- Essential: 4/4 × 60 = **60.00**
- Recommended: 3/3 × 30 = **30.00**
- Aspirational: 31/32 × 10 = **9.69**
- **Composite: 99.69** | Golden: **No**

---

#### V-04 — C-40 only: BRANCH-RULE declaration before routing block

**Essential / Recommended**: Identical to V-01 — all PASS → **60.00 + 30.00**

**Aspirational** — Denominator: /33 − C-39 N/S = **/32**

Changes from V-01:

| ID | Verdict | Evidence |
|----|---------|----------|
| C-38 | PASS | Routing line unchanged: `DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` — DEVIATION: marker + "precedes" positional vocabulary paired in same line |
| C-39 | **N/S** | C-37 PASS but no `AMEND-HALT:` declaration → gate not met → −1 denominator |
| C-40 | **PASS** | `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER: {DEVIATION: \| OVERRIDE:}] + [POSITIONAL-VOCAB: {precedes \| before \| follows \| after}]` declared immediately before ROUTING block. Pairing contract declared as structural rule before routing fires. Both required elements named with equivalence sets — R18-confirmed form-neutrality (OVERRIDE: ≡ DEVIATION:, "before" ≡ "precedes") visible at declaration site without rubric cross-reference. `c40-pairing-contract-declared` mechanism confirmed |

All other 29 aspirational criteria carry from V-01 at PASS.

**Score:**
- Essential: 4/4 × 60 = **60.00**
- Recommended: 3/3 × 30 = **30.00**
- Aspirational: 32/32 × 10 = **10.00**
- **Composite: 100.00** | Golden: **Yes**

---

#### V-05 — Combined C-39 + C-40: full /33 denominator ceiling probe

**Essential / Recommended**: Identical to V-01 — all PASS → **60.00 + 30.00**

**Aspirational** — Denominator: **/33** (no exclusions — both gate conditions met)

Changes from V-01:

| ID | Verdict | Evidence |
|----|---------|----------|
| C-37 | PASS | All three AMEND paths use `{AMEND-HALT}` — uniform by declaration architecture |
| C-38 | PASS | `DEVIATION:` + "precedes" paired on routing line; unchanged from V-01 |
| C-39 | **PASS** | `AMEND-HALT: "any of the above tokens is absent"` declared before AMEND; each path HALT uses `{AMEND-HALT}` by token name. Declaration-before-use + token-name recall both satisfied. No interaction with C-40 mechanism |
| C-40 | **PASS** | `BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER: {DEVIATION: \| OVERRIDE:}] + [POSITIONAL-VOCAB: {precedes \| before \| follows \| after}]` before ROUTING block. Pairing contract declared with named elements and equivalence sets. No interaction with C-39 mechanism — two declaration sites operate independently |

All other 29 aspirational criteria carry from V-01 at PASS.

**Score:**
- Essential: 4/4 × 60 = **60.00**
- Recommended: 3/3 × 30 = **30.00**
- Aspirational: 33/33 × 10 = **10.00**
- **Composite: 100.00** | Golden: **Yes**

---

### Composite Score Summary

| Var | Essential | Recommended | Aspirational | Denominator | Composite | Projected | Delta | Golden |
|-----|-----------|-------------|-------------|------------|-----------|-----------|-------|--------|
| V-01 | 60.00 | 30.00 | 10.00 | /31 | **100.00** | 100.00 | 0 | Yes |
| V-02 | 60.00 | 30.00 | 10.00 | /32 | **100.00** | 100.00 | 0 | Yes |
| V-03 | 60.00 | 30.00 | 9.69 | /32 | **99.69** | 99.69 | 0 | No |
| V-04 | 60.00 | 30.00 | 10.00 | /32 | **100.00** | 100.00 | 0 | Yes |
| V-05 | 60.00 | 30.00 | 10.00 | /33 | **100.00** | 100.00 | 0 | Yes |

---

### Discrimination Results

| Question | Resolved |
|----------|----------|
| V-01: Both C-39 and C-40 N/S → denominator /31? | **Yes** — 31/31 = 100.00 confirmed |
| V-02: `{AMEND-HALT}` token recall satisfies C-39? | **Yes** — V-02 = 100.00 on /32 |
| V-03: Declaration present + literal phrase → C-37 PASS, C-39 FAIL? | **Yes** — 31/32 = 99.69; token-name recall is the gate, not declaration presence alone |
| V-04: BRANCH-RULE with equivalence sets satisfies C-40? | **Yes** — V-04 = 100.00 on /32 |
| V-05: Both declarations coexist with no interaction effects? | **Yes** — 33/33 = 100.00; mechanisms operate independently |

---

### Ranking

1. **V-01, V-02, V-04, V-05** — 100.00 (tied ceiling)
2. **V-03** — 99.69 (C-39 failure probe)

V-05 is the architectural ceiling at the full /33 denominator. V-01 is the established minimal golden (R18 carry). V-02 and V-04 confirm single-axis C-39/C-40 mechanisms respectively.

---

### Excellence Signals (from V-05)

**1. Declaration-before-use architecture for HALT phrases**
`AMEND-HALT: "any of the above tokens is absent"` declared as a canonical token before the AMEND block opens. Each path's HALT uses `{AMEND-HALT}` by token name — not a typed copy of the phrase. A deviation is detectable as a token mismatch at one point; revising the convention requires changing one declaration site, not three path sites. This is the C-39 ceiling over C-37: uniformity-by-declaration vs. uniformity-by-inspection.

**2. Token-name recall distinguishes architectural enforcement from coincidental uniformity**
V-03 demonstrates that declaration presence alone is insufficient. Even when the literal phrase is identical to the declared value, using it as a typed string (not `{AMEND-HALT}`) leaves the architecture as inspection-dependent. C-37 and C-39 score the same surface form differently because the enforcement mechanism differs.

**3. Pre-routing pairing contract with named equivalence sets**
`BRANCH-RULE: deviation branch must carry [DEVIATION-MARKER: {DEVIATION: | OVERRIDE:}] + [POSITIONAL-VOCAB: {precedes | before | follows | after}]` before the routing block. Both required elements named; equivalence sets enumerated. Form-neutrality (OVERRIDE: ≡ DEVIATION:, "before" ≡ "precedes") becomes visible at the declaration site — a reviewer no longer needs the rubric to confirm compliance. This is the C-40 ceiling over C-38: coexistence-by-declaration vs. coexistence-by-inspection.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["declaration-before-use-halt: AMEND-HALT phrase declared as canonical token before AMEND block; each path recalls by token name {AMEND-HALT} rather than reproducing literal string; uniformity enforced by declaration architecture not per-path inspection", "pre-routing-pairing-contract: BRANCH-RULE with named elements and equivalence sets declared before routing fires; coexistence property and form-neutrality visible at declaration site without rubric cross-reference"]}
```
