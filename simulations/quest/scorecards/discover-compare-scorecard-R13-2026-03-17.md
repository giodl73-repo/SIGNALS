## discover-compare R13 Scorecard

**Rubric**: v11 (/24) | **All projections confirmed**

| Rank | Variation | Composite | Key penalty |
|------|-----------|-----------|-------------|
| 1 | V-01 | **100.00** | None — v11 ceiling |
| 2 | V-02 | **99.79** | C-30 PARTIAL: redundant exec branch alongside BODY ORDER |
| 3 | V-03 | **99.58** | C-28 + C-31 PARTIAL cascade from "reverse BODY ORDER" name reference |
| 4 | V-04 | **99.57** | C-28 + C-29 PARTIAL; denominator /23 (C-30 excluded) |
| 5 | V-05 | **99.38** | C-28 + C-30 + C-31 PARTIAL compound (-0.63) |

---

### Key findings

**C-30 PARTIAL penalty = 0.21**: A redundant exec branch alongside a standalone BODY ORDER costs exactly 0.21 composite points. One branch removal (V-02 → V-01) is the v11 fix.

**C-31/C-28 cascade confirmed**: The inline positional restatement in V-03 (`reverse BODY ORDER: DECISION MATRIX precedes RECOMMENDATION`) does **not** neutralize the name reference. Label occurrence is the trigger for C-31 PARTIAL regardless of what follows it. C-28 PARTIAL co-fires from the same source.

**Denominator resolved**: C-30 "not scored" = criterion excluded from denominator (/23, not /24). V-04 composite = 99.57, not 99.17. This is now canonical for R13+.

**Compound penalties are strictly additive**: V-05's three-way cascade (C-28 + C-30 + C-31 all PARTIAL) = exactly 3 × (-0.21) = -0.63. No interaction effect.

---

### Two new patterns documented

1. **`deviation-only-routing-ceiling`** — when BODY ORDER is present, the routing block is deviation-only (engineering branch only). Exec branch absence IS the design signal: BODY ORDER owns exec ordering; routing owns only the deviation. One structural decision achieves C-30 PASS + C-31 PASS + C-28 PASS simultaneously.

2. **`v04-not-scored-denominator-exclusion`** — C-30 "not scored" excludes the criterion from the denominator (D = /23). Canonical for R13+.

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["deviation-only-routing-ceiling", "v04-not-scored-denominator-exclusion"]}
```
 each (20 total) | R12 baseline; no change |
| C-28 | **PASS** (1) | BODY ORDER and routing block physically separate and lexically independent; neither names the other |
| C-29 | **PASS** (1) | `BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` -- standalone, unconditional, no conditional clause |
| C-30 | **PASS** (1) | Routing block is deviation-only: `if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.` Exec branch absent; BODY ORDER is the sole exec ordering mechanism |
| C-31 | **PASS** (1) | Routing branch uses positional vocabulary only: "DECISION MATRIX precedes RECOMMENDATION" -- BODY ORDER not named |

```
Essential:    4/4   * 60 = 60.00
Recommended:  3/3   * 30 = 30.00
Aspirational: 24/24 * 10 = 10.00
Composite: 100.00
```

---

#### V-02 -- R12 V-01 body rescored: C-30 PARTIAL probe

| ID | Score | Evidence |
|----|-------|---------|
| C-01 to C-27 | 1 each (20 total) | R12 baseline; no change |
| C-28 | **PASS** (1) | BODY ORDER and routing block physically separate, lexically independent; routing branches use positional vocabulary; no cross-name reference |
| C-29 | **PASS** (1) | Standalone unconditional BODY ORDER present |
| C-30 | **PARTIAL** (0.5) | Routing block has exec branch (`if REG = exec, produce RECOMMENDATION first`) alongside standalone BODY ORDER that already declares the same unconditionally; exec branch is a second, conditional source of the same specification |
| C-31 | **PASS** (1) | Both routing branches use positional vocabulary: "produce RECOMMENDATION first" / "produce DECISION MATRIX first" -- BODY ORDER not named |

**C-30 PARTIAL penalty established**: 0.21 composite points per redundant exec branch alongside standalone BODY ORDER.

```
Essential:    4/4    * 60 = 60.00
Recommended:  3/3    * 30 = 30.00
Aspirational: 23.5/24 * 10 = 9.79
Composite: 99.79
```

---

#### V-03 -- BODY ORDER + deviation-only routing + name reference

| ID | Score | Evidence |
|----|-------|---------|
| C-01 to C-27 | 1 each (20 total) | R12 baseline; no change |
| C-28 | **PARTIAL** (0.5) | Routing block names BODY ORDER: "reverse BODY ORDER" constitutes vocabulary-level coupling; per c28-name-reference-boundary, lexical independence required for C-28 PASS; physical separation alone insufficient |
| C-29 | **PASS** (1) | Standalone unconditional BODY ORDER present |
| C-30 | **PASS** (1) | Routing block is deviation-only: single engineering branch only; exec branch absent |
| C-31 | **PARTIAL** (0.5) | Routing branch names BODY ORDER by label: `reverse BODY ORDER: DECISION MATRIX precedes RECOMMENDATION` -- inline positional restatement does not neutralize the name reference; label occurrence is the trigger regardless of positional codicil |

**C-31/C-28 cascade confirmed**: both fire from the same structural root (name reference in routing branch). Inline positional restatement ": DECISION MATRIX precedes RECOMMENDATION" does not neutralize C-31 PARTIAL. Label occurrence = trigger.

```
Essential:    4/4  * 60 = 60.00
Recommended:  3/3  * 30 = 30.00
Aspirational: 23/24 * 10 = 9.58
Composite: 99.58
```

---

#### V-04 -- R12 V-02 body rescored: C-30 not scored

| ID | Score | Evidence |
|----|-------|---------|
| C-01 to C-27 | 1 each (20 total) | R12 baseline; no change |
| C-28 | **PARTIAL** (0.5) | No standalone BODY ORDER; routing block is the body-ordering mechanism; body ordering not stated as an independent directive; same as R12 V-02 |
| C-29 | **PARTIAL** (0.5) | No standalone BODY ORDER; exec ordering expressed only inside exec-branch conditional routing; no unconditional directive elsewhere; same as R12 V-02 |
| C-30 | **N/A** | No standalone BODY ORDER present; criterion not scored per C-30 condition |
| C-31 | **PASS** (1) | Two-branch routing uses positional vocabulary throughout: "produce RECOMMENDATION first" / "produce DECISION MATRIX first" -- no BODY ORDER label named |

**Denominator resolution**: C-30 "not scored" = criterion excluded from denominator. D = 23. Canonical interpretation for R13+. Model (a): 22/23 = 9.565 -> composite 99.57. Model (b) zero-penalty: 22/24 = 9.17 -> composite 99.17. R13 applies model (a). Difference = 0.40 composite points.

```
Essential:    4/4  * 60 = 60.00
Recommended:  3/3  * 30 = 30.00
Aspirational: 22/23 * 10 = 9.57
Composite: 99.57
```

---

#### V-05 -- C-30+C-31 compound: BODY ORDER + two-branch naming

| ID | Score | Evidence |
|----|-------|---------|
| C-01 to C-27 | 1 each (20 total) | R12 baseline; no change |
| C-28 | **PARTIAL** (0.5) | Both routing branches name BODY ORDER; vocabulary-level coupling per c28-name-reference-boundary; physical separation insufficient |
| C-29 | **PASS** (1) | Standalone unconditional BODY ORDER present |
| C-30 | **PARTIAL** (0.5) | Exec branch alongside BODY ORDER: `if REG = exec, follow BODY ORDER` re-states exec ordering conditionally; BODY ORDER already covers this unconditionally |
| C-31 | **PARTIAL** (0.5) | Both routing branches name BODY ORDER: `follow BODY ORDER` / `reverse BODY ORDER` -- neither uses positional vocabulary |

**Compound cascade confirmed**: C-28 + C-30 + C-31 PARTIAL co-emerge from the same structural root (naming BODY ORDER in two-branch routing). Penalties are strictly additive. No interaction effect: 3 x (-0.21) = -0.63 vs V-01 ceiling.

```
Essential:    4/4    * 60 = 60.00
Recommended:  3/3    * 30 = 30.00
Aspirational: 22.5/24 * 10 = 9.38
Composite: 99.38
```

---

### Penalty calibration table

| Failure mode | Criteria affected | Composite penalty vs V-01 |
|---|---|---|
| Redundant exec branch alongside BODY ORDER | C-30 PARTIAL | -0.21 |
| Name reference in deviation-only routing | C-31 + C-28 PARTIAL | -0.42 |
| No BODY ORDER (two-branch, positional); /23 denom | C-28 + C-29 PARTIAL | -0.43 |
| Name reference in two-branch routing + exec branch | C-28 + C-30 + C-31 PARTIAL | -0.63 |

---

### V-01 excellence signals

1. **Deviation-only routing as the exec-safety mechanism** -- the exec branch is absent from the routing block by design. Its absence IS the signal: BODY ORDER owns exec ordering exclusively. Removing the exec branch from routing achieves C-30 PASS + C-31 PASS + C-28 PASS simultaneously from a single structural decision. One change resolves three criteria.

2. **Positional vocabulary in the single routing branch** -- `if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION` uses section names and sequence terms only. No reference to BODY ORDER's label. Lexical independence is maintained. The routing branch is self-describing: no reader needs to know what BODY ORDER says to understand the routing instruction.

3. **Two-layer ownership model** -- BODY ORDER owns exec ordering (unconditional, body-layer). Routing block owns engineering deviation (conditional, routing-layer). Each layer is the sole owner of its specification. Neither layer references the other. Clean ownership is the structural property that makes all four of C-28, C-29, C-30, C-31 simultaneously PASS.

---

### New patterns

**deviation-only-routing-ceiling** (C-30, C-31, C-28)
When BODY ORDER is present, the routing block is deviation-only (engineering/general branch only). The exec branch absence is intentional: BODY ORDER covers exec unconditionally; the routing block covers only the deviation from that default. This achieves C-30 PASS (no redundant exec branch), C-31 PASS (single branch; positional vocabulary sufficient), C-28 PASS (layers cleanly isolated; no coupling). Deviation-only routing + BODY ORDER = the v11 ceiling architecture.

**v04-not-scored-denominator-exclusion** (C-30)
When C-30 is "not scored" (no standalone BODY ORDER), the criterion is excluded from the denominator (D = /23, not /24). Exclusion model is canonical for R13+. Zero-penalty model (22/24 = 9.17 -> 99.17) is rejected. Practical consequence: V-04 composite = 99.57, not 99.17. Any future variation without BODY ORDER uses D = /23 for C-30 exclusion.

---

### Cumulative discrimination map (R13)

| Composite band | Variation | Structural signature |
|---|---|---|
| 100.00 | V-01 | BODY ORDER + deviation-only routing + positional |
| 99.79 | V-02 | BODY ORDER + two-branch + positional; redundant exec branch |
| 99.58 | V-03 | BODY ORDER + deviation-only + name reference cascade |
| 99.57 | V-04 | No BODY ORDER + two-branch + positional; /23 denominator |
| 99.38 | V-05 | BODY ORDER + two-branch + name refs on both branches |
