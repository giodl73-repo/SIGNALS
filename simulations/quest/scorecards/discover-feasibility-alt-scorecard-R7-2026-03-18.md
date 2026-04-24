## Round 7 Scorecard — `discover-feasibility-alt` (v5 Rubric)

### Results

| Rank | Variation | Composite | Golden? | Key failure |
|------|-----------|-----------|---------|-------------|
| 1 | **V-01** | **100.000** | Yes | — |
| 2 | **V-02** | **99.000** | Yes | C-17 FAIL (aspirational) |
| 2 | **V-04** | **99.000** | Yes | C-18 FAIL (aspirational) |
| 4 | **V-05** | **98.000** | Yes | C-17 + C-18 FAIL (aspirational) |
| 5 | **V-03** | **87.000** | **No** | C-02 FAIL (essential) + C-17 FAIL |

All hypotheses confirmed against the v5 rubric.

### Key findings

- **C-17/C-18 symmetry**: both cost exactly 1 pt (1/10 × 10). Golden-compatible in isolation and in compound.
- **C-17/C-02 cascade asymmetry**: inference-only guard (V-02) = −1 pt. Guard removed entirely (V-03) = −13 pts. The 13× multiplier comes from C-02 FAIL cascading into the essential tier.
- **V-03 is the only non-golden variation**: essential C-02 FAIL is the disqualifier, not the aspirational C-17 FAIL alone. This isolates the exact mechanism: unconditional rendering → essential failure, not probabilistic suppression.
- **C-18/C-04/C-06 three-surface independence**: V-04's merged instruction satisfies C-04 output (inertia content present) and C-06 output (component/color/delta mentioned) while failing C-18 (template-authoring check). Same AMENDMENTS block, three independently testable failure surfaces.
- **Aspirational-only failure ceiling**: 0/10 aspirational = composite 90.000 — still golden. Essential-tier gating is the only golden predicate.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-17/C-18 aspirational symmetry: each costs 1 pt (1/10 * 10); golden-compatible individually (V-02: 99, V-04: 99) and in compound (V-05: 98)", "C-17/C-02 cascade asymmetry: inference-only guard = -1 pt total; guard removed entirely = -13 pts (1 aspirational + 12 essential) -- 13x multiplier when unconditional rendering triggers C-02 FAIL", "aspirational-only failure ceiling: 0/10 aspirational = composite 90.000, still golden -- essential-tier gating is the only golden predicate, aspirational failures cannot break golden without essential involvement", "C-18/C-04/C-06 three-surface independence: merged instruction satisfies C-04 output and C-06 output while failing C-18 template-authoring check -- same AMENDMENTS block, three independently testable failure surfaces"]}
```

Scorecard written to `simulations/quest/scorecards/discover-feasibility-alt-scorecard-R7-2026-03-18.md`.
rce for ordering. |
| C-15 | aspirational | PASS | C-10 holds via body ordering; C-11 and C-12 reachable by-construction. No preamble-template conflict to degrade to probabilistic. Cascade-safe. |
| C-16 | aspirational | PASS | STRATEGY body contains explicit proceed-gate sentence naming components forward to ARCHITECT; ARCHITECT body contains explicit confirmation sentence citing STRATEGY by name. Both mechanism sentences present as static body text. |
| C-17 | aspirational | PASS | `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` is present as static template body text immediately preceding the prerequisites block. Structural iff-guard authored explicitly. |
| C-18 | aspirational | PASS | AMENDMENTS authors three independently-removable sub-lines per entry: (1) action line `1. [Action for COMPONENT (RED/YELLOW): the specific next step.]`, (2) color-transition line `This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.`, (3) inertia line `Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint].` -- each a separate named obligation. |

```
Essential:    5/5   * 60 = 60.000   (C-05 N/A=1)
Recommended:  3/3   * 30 = 30.000   (C-07 N/A=1)
Aspirational: 10/10 * 10 = 10.000   (C-09 N/A=1, C-13 N/A=1)
Composite: 100.000
```

**Golden. All essential PASS. Composite >= 80. Establishes 100.000 under v5 /10 aspirational denominator.**

---

### V-02 -- C-17 FAIL Only: Inference-Only Prerequisite Guard

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE unchanged from V-01. All required fields present. |
| C-02 | essential | PASS | VERDICT has score/100 and label. Inference-only instruction ("include if analysis requires them (omit when not applicable)") leaves suppression to model inference. C-02 tests output behavior -- instruction tells model to omit when not applicable; probabilistic PASS. Distinct from C-17 (mechanism check). |
| C-03 | essential | PASS | ARCHITECT table unchanged from V-01. |
| C-04 | essential | PASS | All four inertia surfaces unchanged. AMENDMENTS "Inertia saved:" sub-line independently authored and present. |
| C-05 | essential | N/A | No focus. N/A=1. |
| C-06 | recommended | PASS | AMENDMENTS three sub-lines unchanged from V-01. Component, color transition, score-delta all named obligations. |
| C-07 | recommended | N/A | No focus. N/A=1. |
| C-08 | recommended | PASS | STRATEGY section unchanged from V-01. |
| C-09 | aspirational | N/A | No focus. N/A=1. |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT in body. Unchanged. |
| C-11 | aspirational | PASS | Proceed gate unchanged from V-01. |
| C-12 | aspirational | PASS | ARCHITECT back-reference to STRATEGY unchanged. |
| C-13 | aspirational | N/A | No ordering directive. N/A=1. |
| C-14 | aspirational | PASS | Body ordering unchanged. |
| C-15 | aspirational | PASS | Cascade-safe, body enforces ordering. |
| C-16 | aspirational | PASS | Both mechanism sentences (proceed-gate in STRATEGY, confirmation in ARCHITECT) unchanged from V-01. |
| C-17 | aspirational | FAIL | Static iff-guard `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` replaced by inference-only instruction: `Prerequisites -- include these if the analysis requires them (omit when not applicable):`. No explicit conditional guard text authored in template body. Mechanism removed; guarantee shifts from structural to probabilistic. |
| C-18 | aspirational | PASS | AMENDMENTS three independently-authored sub-lines unchanged from V-01. |

```
Essential:    5/5   * 60 = 60.000   (C-05 N/A=1)
Recommended:  3/3   * 30 = 30.000   (C-07 N/A=1)
Aspirational: 9/10  * 10 =  9.000   (C-17 FAIL=0)
Composite: 99.000
```

**Golden. C-17 FAIL is aspirational-tier only -- 1 pt cost, golden-compatible. C-17/C-02 independence confirmed: template lacks guard (C-17 FAIL) while C-02 passes probabilistically by model inference.**

---

### V-03 -- C-17 FAIL + C-02 FAIL Cascade: Guard Removed, Prerequisites Unconditional

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE unchanged. |
| C-02 | essential | FAIL | iff-guard removed entirely. Prerequisites block present unconditionally in template body with no conditional suppression mechanism. Template renders: `Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:` with no preceding condition. Even FEASIBLE outputs and no-RED outputs carry a Prerequisites block (placeholder instructs "write 'None' if no RED components exist" -- block still present regardless). Structural iff condition violated. |
| C-03 | essential | PASS | ARCHITECT unchanged. |
| C-04 | essential | PASS | All four inertia surfaces present. AMENDMENTS unchanged from V-01. |
| C-05 | essential | N/A | No focus. N/A=1. |
| C-06 | recommended | PASS | AMENDMENTS three sub-lines unchanged from V-01. |
| C-07 | recommended | N/A | No focus. N/A=1. |
| C-08 | recommended | PASS | STRATEGY unchanged. |
| C-09 | aspirational | N/A | No focus. N/A=1. |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT. |
| C-11 | aspirational | PASS | Proceed gate unchanged. |
| C-12 | aspirational | PASS | Back-reference unchanged. |
| C-13 | aspirational | N/A | No ordering directive. N/A=1. |
| C-14 | aspirational | PASS | Body ordering unchanged. |
| C-15 | aspirational | PASS | Cascade-safe. |
| C-16 | aspirational | PASS | Both mechanism sentences present. |
| C-17 | aspirational | FAIL | Guard removed entirely -- no static iff-guard text present anywhere in VERDICT prerequisites block. More severe than V-02 (inference-only); here the block is structurally unconditional. C-17 FAIL cascades to C-02 FAIL. |
| C-18 | aspirational | PASS | AMENDMENTS unchanged from V-01. Three sub-lines independently authored. |

```
Essential:    4/5   * 60 = 48.000   (C-02 FAIL=0; C-05 N/A=1)
Recommended:  3/3   * 30 = 30.000   (C-07 N/A=1)
Aspirational: 9/10  * 10 =  9.000   (C-17 FAIL=0)
Composite: 87.000
```

**NOT Golden. C-02 FAIL (essential) disqualifies. V-03 is the canonical cascade case: guard removed (C-17 FAIL) -> unconditional rendering -> C-02 FAIL. Cascade multiplier: 1 aspirational pt becomes 13 pts total (1 aspirational + 12 essential). Confirms v5 floor calculation: 87.000.**

---

### V-04 -- C-18 FAIL Only: AMENDMENTS Merged to Single Combined Instruction

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE unchanged. |
| C-02 | essential | PASS | VERDICT iff-guard unchanged from V-01. `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` present as static body text. |
| C-03 | essential | PASS | ARCHITECT unchanged. |
| C-04 | essential | PASS | All four inertia surfaces present. Surface 4 ("Inertia saved:") content present in merged instruction: "notes the inertia savings recaptured from [Named incumbent]" -- content present even if merged. C-04 tests surface presence, not template structure. PASS. |
| C-05 | essential | N/A | No focus. N/A=1. |
| C-06 | recommended | PASS | Merged instruction covers: specific component, color transition from [COLOR] to [COLOR], score-delta estimate (~[N] pts). All three traceability elements present. C-06 tests output presence. PASS. |
| C-07 | recommended | N/A | No focus. N/A=1. |
| C-08 | recommended | PASS | STRATEGY unchanged. |
| C-09 | aspirational | N/A | No focus. N/A=1. |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT. |
| C-11 | aspirational | PASS | Proceed gate unchanged. |
| C-12 | aspirational | PASS | Back-reference unchanged. |
| C-13 | aspirational | N/A | No ordering directive. N/A=1. |
| C-14 | aspirational | PASS | Body ordering unchanged. |
| C-15 | aspirational | PASS | Cascade-safe. |
| C-16 | aspirational | PASS | Both mechanism sentences unchanged. |
| C-17 | aspirational | PASS | VERDICT iff-guard unchanged from V-01. Static body text present. |
| C-18 | aspirational | FAIL | AMENDMENTS instruction: "write a single entry that: names the specific component and the action to take, states the color transition from [COLOR] to [COLOR] with a score-delta estimate of approximately [N] pts, and notes the inertia savings..." -- one compound sentence, not three independently-authored sub-lines. C-18 requires three separately-removable obligations. Merged instruction fails: removing "inertia savings" phrase doesn't fire C-04 as a PARTIAL on its own line; removing "color transition" phrase doesn't fire C-06 as a FAIL on its own line. Structural orthogonality absent. |

```
Essential:    5/5   * 60 = 60.000   (C-05 N/A=1)
Recommended:  3/3   * 30 = 30.000   (C-07 N/A=1)
Aspirational: 9/10  * 10 =  9.000   (C-18 FAIL=0)
Composite: 99.000
```

**Golden. C-18 FAIL is aspirational-tier only -- 1 pt cost, golden-compatible. Confirms: merged instruction satisfies C-04 (content present) and C-06 (component/color/delta mentioned) while failing C-18 (template-authoring check). Three independently testable failure surfaces from the same AMENDMENTS block.**

---

### V-05 -- Compound: C-17 FAIL + C-18 FAIL (Both Aspirational)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | INFERENCE GATE unchanged. |
| C-02 | essential | PASS | VERDICT uses inference-only guard (from V-02): "include if analysis requires them (omit when not applicable)." Probabilistic PASS -- model can infer the condition; not unconditional rendering (V-03 pattern). |
| C-03 | essential | PASS | ARCHITECT unchanged. |
| C-04 | essential | PASS | Inertia content present in merged AMENDMENTS instruction ("inertia savings recaptured from [Named incumbent]"). Surface 4 present. C-04 PASS. |
| C-05 | essential | N/A | No focus. N/A=1. |
| C-06 | recommended | PASS | Merged instruction names component, color transition, score-delta. C-06 PASS. |
| C-07 | recommended | N/A | No focus. N/A=1. |
| C-08 | recommended | PASS | STRATEGY unchanged. |
| C-09 | aspirational | N/A | No focus. N/A=1. |
| C-10 | aspirational | PASS | STRATEGY before ARCHITECT. |
| C-11 | aspirational | PASS | Proceed gate unchanged. |
| C-12 | aspirational | PASS | Back-reference unchanged. |
| C-13 | aspirational | N/A | No ordering directive. N/A=1. |
| C-14 | aspirational | PASS | Body ordering unchanged. |
| C-15 | aspirational | PASS | Cascade-safe. |
| C-16 | aspirational | PASS | Both mechanism sentences present. |
| C-17 | aspirational | FAIL | Inference-only guard from V-02: `Prerequisites -- include these if the analysis requires them (omit when not applicable):`. No static iff-guard text. C-17 FAIL. |
| C-18 | aspirational | FAIL | Merged instruction from V-04: single combined sentence for action, color-transition, and inertia savings. Not three independently-authored sub-lines. C-18 FAIL. |

```
Essential:    5/5   * 60 = 60.000   (C-05 N/A=1)
Recommended:  3/3   * 30 = 30.000   (C-07 N/A=1)
Aspirational: 8/10  * 10 =  8.000   (C-17 FAIL=0, C-18 FAIL=0)
Composite: 98.000
```

**Golden. Compound aspirational failure (C-17 + C-18) costs 2 pts. Composite 98.000 is well above the 80 threshold. Confirms: aspirational-only failures cannot break golden without essential involvement. Ceiling: 0/10 aspirational = composite 90.000 -- still golden.**

---

### Rankings

| Rank | Variation | Composite | Golden? | Key failure |
|------|-----------|-----------|---------|-------------|
| 1 | V-01 | 100.000 | Yes | -- |
| 2 | V-02 | 99.000 | Yes | C-17 FAIL (aspirational) |
| 2 | V-04 | 99.000 | Yes | C-18 FAIL (aspirational) |
| 4 | V-05 | 98.000 | Yes | C-17 FAIL + C-18 FAIL (aspirational) |
| 5 | V-03 | 87.000 | **No** | C-02 FAIL (essential) + C-17 FAIL (aspirational) |

---

### Excellence Signals (from V-01)

1. **Explicit iff-guard as static body text** -- `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` is authored as a static template instruction, not a runtime instruction to the model. This is the mechanism-level guarantee: the model sees a conditional bracket that is unambiguous, regardless of what label or RED state the output would have. V-03 demonstrates the 13x cascade cost when this guard is removed entirely.

2. **Three independently-authored AMENDMENTS sub-lines** -- the action line, color-transition line, and "Inertia saved:" line are each on separate lines with distinct content, authored as independent obligations. This ensures each output failure surface (C-04, C-06) can fire independently without corrupting the others. V-04 demonstrates that merging them into one compound instruction satisfies C-04 and C-06 while failing C-18 -- confirming the three surfaces are independently testable.

3. **C-17/C-02 cascade asymmetry** -- the 13x multiplier is the critical structural finding this round. An inference-only guard (V-02) costs 1 pt. Guard removed entirely (V-03) costs 13 pts. The essential-tier C-02 failure is the load-bearing factor; aspirational C-17 alone is golden-compatible. Template authors should encode the guard as static body text to prevent this cascade, not weaken it to an inference instruction.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-17/C-18 aspirational symmetry: each costs 1 pt (1/10 * 10); golden-compatible individually (V-02: 99, V-04: 99) and in compound (V-05: 98)", "C-17/C-02 cascade asymmetry: inference-only guard = -1 pt total; guard removed entirely = -13 pts (1 aspirational + 12 essential) -- 13x multiplier when unconditional rendering triggers C-02 FAIL", "aspirational-only failure ceiling: 0/10 aspirational = composite 90.000, still golden -- essential-tier gating is the only golden predicate, aspirational failures cannot break golden without essential involvement", "C-18/C-04/C-06 three-surface independence: merged instruction satisfies C-04 output and C-06 output while failing C-18 template-authoring check -- same AMENDMENTS block, three independently testable failure surfaces"]}
```
