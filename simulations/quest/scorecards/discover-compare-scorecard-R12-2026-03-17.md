```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["c28-c29-co-emergence", "c28-name-reference-boundary"]}
```

---

## discover-compare R12 Scorecard

**Rubric**: v10 (/22) | **All projections confirmed**

| Rank | Variation | Composite | Key penalty |
|------|-----------|-----------|-------------|
| 1 | V-01 | **100.00** | None |
| 2 | V-03 | **99.77** | C-28 PARTIAL (name-reference) |
| 3 | V-02 | **99.55** | C-28 + C-29 PARTIAL (compound routing) |
| 4 | V-04 | **99.09** | C-25 PARTIAL + C-28 FAIL + C-29 PARTIAL |
| 5 | V-05 | **98.18** | C-25 + C-27 + C-28 + C-29 FAIL |

**All essential pass**: yes (5/5 variations). All recommended pass.

---

**V-01 excellence signals:**

1. **Standalone unconditional BODY ORDER directive** — `BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` as a separate line after ANCHOR[0], no conditional clauses. One structural element satisfies both C-29 (unconditional) and C-28 (isolatable).

2. **Vocabulary independence** — BODY ORDER uses only body-section names; routing block uses only register values and section names. Neither names the other. Each can be independently varied. This is what C-28 PASS requires: not just physical separation, but no cross-name references.

3. **Body ordering as foundation; routing as deviation-only** — exec safety lives at the body layer; register-sensitive deviation lives at the routing layer. Neither layer depends on the other.

---

**Two new patterns confirmed:**

- **c28-c29-co-emergence**: C-28 PASS and C-29 PASS are necessary conditions for each other — both require the same structural artifact (standalone unconditional BODY ORDER directive). Measurable from V-04 and V-05 (both FAIL together), V-01 (both PASS together), V-02 (both PARTIAL together).

- **c28-name-reference-boundary**: Token-name cross-reference in the routing block (`follow BODY ORDER` / `reverse BODY ORDER`) triggers C-28 PARTIAL even when both elements are physically separate. C-28 PASS requires vocabulary independence — the routing block must not name the body-order element. Physical separation is necessary but not sufficient.
ate | PASS | PASS | PASS | PASS | PASS |
| C-17 output compressed | PASS | PASS | PASS | PASS | PASS |
| C-18 dual-polarity FAULT | PASS | PASS | PASS | PASS | PASS |
| C-19 AMEND self-contained | PASS | PASS | PASS | PASS | PASS |
| C-20 path-scoped TOKEN RECALL | PASS | PASS | PASS | PASS | PASS |
| C-21 FAULT propagates to AMEND | PASS | PASS | PASS | PASS | PASS |
| C-22 phase structure by token positioning | PASS | PASS | PASS | PASS | PASS |
| C-23 exec leads with recommendation | PASS | PASS | PASS | PASS | PASS |
| C-24 AMEND path sub-ledgers | PASS | PASS | PASS | PASS | PASS |
| C-25 register-gated routing block | PASS | PASS | PASS | **PARTIAL** | **FAIL** |
| C-26 body section order exec-safe | PASS | PASS | PASS | PASS | PASS |
| C-27 routing block within LEDGER GATE scope | PASS | PASS | PASS | PASS | **FAIL** |
| **C-28 body-order and routing-scope isolated** | **PASS** | **PARTIAL** | **PARTIAL** | **FAIL** | **FAIL** |
| **C-29 body ordering stated as unconditional directive** | **PASS** | **PARTIAL** | **PASS** | **PARTIAL** | **FAIL** |

**Evidence notes:**

**C-25:**
- V-04: Routing block has only one branch (`if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION`). No exec branch. One register value addressed = PARTIAL per R10 flat band.
- V-05: No routing block present = FAIL. C-23 scoring applies independently (body-first layout preserves C-23 PASS).

**C-26:**
- All variations PASS. V-04 body layout is recommendation-first (C-26 PASS independently of one-sided routing). V-05 body layout recommendation-first (C-26 PASS confirmed per v9-no-routing-penalty-calibration). Body ordering is the foundation; routing is deviation-only.

**C-27:**
- V-05: No routing block = FAIL. C-25 FAIL penalty is independent; no interaction.
- V-04: Routing block appears after LEDGER GATE = PASS.

**C-28:**
- V-01 PASS: `BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` is a standalone unconditional directive. Routing block is a separate conditional construct. Neither references the other's structural vocabulary. Each can be independently varied without touching the other. Two isolated structural elements.
- V-02 PARTIAL: No standalone BODY ORDER. Routing block is the sole ordering specification, co-specifying body section sequence AND register-gated routing scope in one conditional construct. One compound element covering two structural responsibilities.
- V-03 PARTIAL: Standalone BODY ORDER present (C-29 PASS). However, routing block references BODY ORDER by name: `if REG = exec, follow BODY ORDER. If REG = engineering or general, reverse BODY ORDER.` Token-name cross-reference constitutes a structural reference -- routing depends on BODY ORDER's structural property by name. Isolation requires vocabulary independence, not just physical separation. Name-reference = PARTIAL.
- V-04 FAIL: No BODY ORDER directive. No exec routing branch. Exec body ordering is never stated as an independent directive anywhere -- only inferrable from body layout position (implicit, not stated). "Body ordering implied only through body layout" = FAIL per rubric definition.
- V-05 FAIL: No routing block, no BODY ORDER directive. Body ordering derivable only from implicit layout position. Same fail class as V-04: no independent body-order directive of any kind.

**C-29:**
- V-01 PASS: `BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` is an absolute structural specification with no conditional clauses. Universal -- holds without evaluating any register state.
- V-02 PARTIAL: Routing block states body ordering only within the exec-branch conditional (`if REG = exec, produce RECOMMENDATION first`). No independent unconditional directive anywhere.
- V-03 PASS: Same standalone `BODY ORDER` as V-01. Routing references it by name but does not embed the directive inside a conditional. The unconditional statement exists independently = PASS.
- V-04 PARTIAL: Engineering-only routing branch contains explicit ordering (`if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION`). This is a conditional ordering statement, not unconditional. No standalone unconditional directive.
- V-05 FAIL: No explicit body ordering directive anywhere -- not in routing (absent), not as a standalone statement. Body ordering is purely implicit.

---

## Composite Score Computation

**Formula:** Essential: passed/4 x 60. Recommended: passed/3 x 30. Aspirational: points/22 x 10.
**PASS = 1.0 pt, PARTIAL = 0.5 pt, FAIL = 0 pt.**

### V-01

```
Essential passed:    4 / 4   =>  4 * 60 / 4  = 60.00
Recommended passed:  3 / 3   =>  3 * 30 / 3  = 30.00
Aspirational passed: 22 / 22 =>  22 * 10 / 22 = 10.00

Total composite: 100.00
```

Aspirational detail: C-08 through C-29 = 22 PASS x 1.0 = 22.0 / 22.

### V-02

```
Essential passed:    4 / 4   =>  4 * 60 / 4  = 60.00
Recommended passed:  3 / 3   =>  3 * 30 / 3  = 30.00
Aspirational passed: 21 / 22 =>  21 * 10 / 22 = 9.55

Total composite: 99.55
```

Aspirational detail: C-08 through C-27 = 20 PASS x 1.0, C-28 PARTIAL x 0.5, C-29 PARTIAL x 0.5 = 20 + 0.5 + 0.5 = 21.0 / 22. Deduction: -0.45 (two PARTIALs, purely additive).

### V-03

```
Essential passed:    4 / 4   =>  4 * 60 / 4  = 60.00
Recommended passed:  3 / 3   =>  3 * 30 / 3  = 30.00
Aspirational passed: 21.5 / 22 =>  21.5 * 10 / 22 = 9.77

Total composite: 99.77
```

Aspirational detail: C-08 through C-27 = 20 PASS x 1.0, C-28 PARTIAL x 0.5, C-29 PASS x 1.0 = 20 + 0.5 + 1.0 = 21.5 / 22. Deduction: -0.23 (one PARTIAL from C-28 name-reference).

### V-04

```
Essential passed:    4 / 4   =>  4 * 60 / 4  = 60.00
Recommended passed:  3 / 3   =>  3 * 30 / 3  = 30.00
Aspirational passed: 20 / 22 =>  20 * 10 / 22 = 9.09

Total composite: 99.09
```

Aspirational detail: C-08 through C-24 = 17 PASS x 1.0, C-25 PARTIAL x 0.5, C-26 PASS x 1.0, C-27 PASS x 1.0, C-28 FAIL x 0, C-29 PARTIAL x 0.5 = 17 + 0.5 + 1 + 1 + 0 + 0.5 = 20.0 / 22. Deduction: -0.91 (C-25 PARTIAL + C-28 FAIL + C-29 PARTIAL).

### V-05

```
Essential passed:    4 / 4   =>  4 * 60 / 4  = 60.00
Recommended passed:  3 / 3   =>  3 * 30 / 3  = 30.00
Aspirational passed: 18 / 22 =>  18 * 10 / 22 = 8.18

Total composite: 98.18
```

Aspirational detail: C-08 through C-24 = 17 PASS x 1.0, C-25 FAIL x 0, C-26 PASS x 1.0, C-27 FAIL x 0, C-28 FAIL x 0, C-29 FAIL x 0 = 17 + 0 + 1 + 0 + 0 + 0 = 18.0 / 22. Deduction: -1.82 (C-25 FAIL + C-27 FAIL + C-28 FAIL + C-29 FAIL). Delta from v9 no-routing baseline (99.00): -0.82, exactly the cost of C-28 FAIL + C-29 FAIL introduced by v10.

---

## Ranking

| Rank | Variation | Composite | Delta from Ceiling | Key penalty |
|------|-----------|-----------|--------------------|-------------|
| 1 | V-01 | **100.00** | -- | None |
| 2 | V-03 | **99.77** | -0.23 | C-28 PARTIAL (name-reference) |
| 3 | V-02 | **99.55** | -0.45 | C-28 PARTIAL + C-29 PARTIAL (compound routing) |
| 4 | V-04 | **99.09** | -0.91 | C-25 PARTIAL + C-28 FAIL + C-29 PARTIAL (one-sided routing) |
| 5 | V-05 | **98.18** | -1.82 | C-25 FAIL + C-27 FAIL + C-28 FAIL + C-29 FAIL (no routing) |

All projections confirmed. No scoring surprises.

---

## Excellence Signals (V-01)

**Signal 1 -- Standalone unconditional BODY ORDER directive**
`BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` appears as a separate line after ANCHOR[0], before any analysis tokens. It is an absolute structural specification with no conditional clauses -- it does not say "if REG = exec" or "when routing fires." This single design decision simultaneously satisfies C-29 (unconditional directive) and enables C-28 (isolatable structural element). The routing block becomes a pure deviation mechanism rather than the primary ordering authority.

**Signal 2 -- Structural isolation of two independent mechanisms**
BODY ORDER and the routing block have non-overlapping structural vocabularies. BODY ORDER states the universal default using only body-section names. The routing block states conditional overrides using only register values and section names -- it does not reference "BODY ORDER" by name. Each element can be independently varied (added, removed, modified) without touching the other's statement. This is what C-28 PASS requires: not just physical separation, but vocabulary independence.

**Signal 3 -- Body ordering as foundation; routing as deviation-only**
The architectural pattern established in V-01: body section order defines exec-correct behavior by default (C-26 PASS, C-29 PASS). Routing block overrides the default for non-exec registers only. This separates concerns cleanly: exec safety lives at the body layer; register-sensitive deviation lives at the routing layer. Neither layer depends on the other to be correct for its own register case.

---

## New Patterns

**c28-c29-co-emergence** -- C-28 PASS and C-29 PASS co-emerge; each is a necessary condition for the other. A standalone unconditional BODY ORDER directive is required for both to fire simultaneously. Without it: no independent body-order mechanism exists for C-28 to call isolated (caps at PARTIAL at best), and no unconditional directive exists for C-29 to confirm (caps at PARTIAL at best). The co-emergence constraint is measurable from V-04 (both FAIL simultaneously with no standalone directive) and V-05 (both FAIL simultaneously with no routing and no directive). V-01 confirms both PASS simultaneously with one standalone directive. The boundary: one structural element -- BODY ORDER -- produces two PASS verdicts.

**c28-name-reference-boundary** -- C-28 PARTIAL fires when the routing block references the body-order element by token name, even when both elements exist as physically separate structures. V-03 routing: `if REG = exec, follow BODY ORDER. If REG = engineering or general, reverse BODY ORDER.` The routing block depends on BODY ORDER's structural property by name -- it cannot be independently varied without affecting the routing block's semantics. Token-name cross-reference = structural reference. C-28 PASS requires vocabulary independence: each mechanism must use only its own structural vocabulary without naming the other. Physical separation is necessary but not sufficient; name-reference is sufficient to trigger PARTIAL.

---

## Structural Dependencies Confirmed by R12

1. **C-25 PASS implies C-29 >= PARTIAL**: A routing block satisfying C-25 (both branches) must explicitly name section ordering for exec -- which is at minimum a conditional ordering statement. Thus C-25 PASS implies C-29 is not FAIL (reaches PARTIAL via the conditional). Confirmed: V-01 C-25 PASS + C-29 PASS; V-02 C-25 PASS + C-29 PARTIAL.

2. **C-28 PASS iff C-29 PASS (co-emergence)**: Standalone unconditional body-order directive is necessary and sufficient for both. Without it, both cap at PARTIAL or below. Confirmed: V-01 (both PASS), V-04 (both FAIL), V-05 (both FAIL). V-02 confirms symmetric PARTIAL when directive is absent and routing is compound.

3. **C-28 PARTIAL admits two structurally distinct fail modes**:
   - Compound routing (V-02): routing block co-specifies both ordering and routing scope in one element; no independent body-order directive.
   - Name-reference cross-reference (V-03): two physical elements, but routing references body-order by name -- vocabulary dependency breaks isolation.
   Both score identically (PARTIAL), consistent with C-28's flat partial band for all structural cross-reference forms.

---

## Golden Variation

**V-01 is the golden variation for R12.** Composite: 100.00. All 22 aspirational criteria pass. Establishes the v10 ceiling pattern: standalone `BODY ORDER` directive + isolated routing block with both branches after LEDGER GATE.

The golden body adds exactly one line to R11 V-01: `BODY ORDER: RECOMMENDATION precedes DECISION MATRIX in all outputs.` inserted after `ANCHOR[0]` and before the first analysis section. All other structure unchanged. That one line yields two new PASS verdicts (C-28, C-29) and zero regressions.
