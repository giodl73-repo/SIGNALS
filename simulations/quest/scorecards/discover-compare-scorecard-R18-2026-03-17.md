**Scorecard written** to `simulations/quest/scorecards/discover-compare-scorecard-R18-2026-03-17.md`.

---

## discover-compare R18 — Scoring Results

### Composite Scores

| Var | Composite | Projected | Delta | Golden |
|-----|-----------|-----------|-------|--------|
| V-01 | **100.00** | 100.00 | 0 | Yes |
| V-02 | **99.84** | 99.84 | 0 | No |
| V-03 | **99.35** | 99.68 | **−0.33** | No |
| V-04 | **100.00** | 100.00 | 0 | Yes |
| V-05 | **100.00** | 100.00 | 0 | Yes |

### Discrimination Results

| Question | Resolved |
|----------|----------|
| C-37 PARTIAL = 0.5? | **Yes** — V-02 = 99.84 |
| "before" ≡ "precedes" for C-38? | **Yes** — V-04 = 100.00 |
| OVERRIDE: satisfies C-38? | **Yes** — V-05 = 100.00 |
| V-03 actual vs projected? | **99.35 vs 99.68 — projection error** |

### Key Finding — V-03 Projection Error

The design projected 99.68 (30/31) but the actual score is **99.35 (29/31)**. Both C-31 and C-38 fail independently when the routing branch uses non-positional vocabulary ("engineer-first layout applies"). The design text and coverage table both document both failures — the projection math treated them as one unit. Rule added to watch list: `c38-marker-only-double-failure`.

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["c38-marker-only-double-failure: non-positional routing vocabulary causes C-31 FAIL + C-38 FAIL as two independent aspirational failures -- shared root cause does not collapse them; projection errors arise when treated as one unit", "c37-partial-weight-confirmed: C-37 PARTIAL = 0.5; mixed positional phrases across AMEND paths produces 99.84 not 99.68", "c38-vocabulary-neutral-confirmed: before is equivalent to precedes within rubric-listed positional vocabulary set for C-38; OVERRIDE: equivalent to DEVIATION: -- form-neutrality extends to both elements of the pairing"]}
```
8 to C-30 | Prior aspirational | PASS (23/23) | All carry from R17 |
| C-31 | Positional routing vocabulary | PASS | "precedes" is rubric-listed positional vocabulary |
| C-32 | Routing scope deviation-only | PASS | "ROUTING: deviation from BODY ORDER only" |
| C-33 | BODY-ORDER-LAYER token | PASS | Token: `BODY-ORDER-LAYER: active` present |
| C-34 | Token enumeration separable | PASS | Fenced-code block form at each AMEND gate |
| C-35 | HALT uses positional reference | PASS | "any of the above tokens is absent" -- no inline token names |
| C-36 | Deviation marker at branch level | PASS | DEVIATION: at branch instruction line |
| **C-37** | **HALT phrase uniform** | **PASS** | Identical phrase across all three AMEND paths |
| **C-38** | **Paired marker + vocabulary** | **PASS** | DEVIATION: + "precedes" coexist on same routing line |

**Aspirational**: 31/31 x 10 = 10.00
**Composite**: 100.00
**Golden**: Yes

---

### V-02 -- C-37 non-uniformity: mixed positional phrases across AMEND paths

**Routing**: `DEVIATION: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.`
**AMEND HALTs**:
- Add-C: "any of the above tokens is absent"
- Weight: "any listed token is absent" (differs)
- Override: "any of the above tokens is absent"

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 to C-07 | Essential + Recommended | PASS (7/7) | All carry |
| C-08 to C-30 | Prior aspirational | PASS (23/23) | All carry |
| C-31 | Positional routing vocabulary | PASS | "precedes" |
| C-32 to C-34 | Routing structure + enumeration | PASS | All carry |
| C-35 | HALT uses positional reference | PASS | Both phrases are positional reference -- no inline token names on any path |
| C-36 | Deviation marker | PASS | DEVIATION: at branch level |
| **C-37** | **HALT phrase uniform** | **PARTIAL** | Two distinct C-35-valid phrases: "any of the above tokens" (Add-C + Override) vs "any listed token" (Weight). PARTIAL is flat -- distribution across paths creates no sub-grades |
| C-38 | Paired marker + vocabulary | PASS | DEVIATION: + "precedes" on same line -- unchanged from V-01 |

**Aspirational**: 30.5/31 x 10 = 9.84 (PARTIAL = 0.5)
**Composite**: 99.84
**Golden**: No

**Discrimination resolved**: C-37 PARTIAL = 0.5. Score 99.84 confirms the distinct scored state between C-37 FAIL (99.68) and C-37 PASS (100.00).

---

### V-03 -- C-38 marker-only: deviation marker without positional vocabulary

**Routing**: `DEVIATION: if REG = engineering or general, engineer-first layout applies.`
**AMEND HALTs**: All three use "any of the above tokens is absent" uniformly.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 to C-07 | Essential + Recommended | PASS (7/7) | All carry |
| C-08 to C-30 | Prior aspirational | PASS (23/23) | All carry |
| **C-31** | **Positional routing vocabulary** | **FAIL** | "engineer-first layout applies" is an outcome phrase -- not in rubric-listed positional vocabulary set ("precedes," "before," "follows," "after") |
| C-32 | Routing scope deviation-only | PASS | Scope declaration unchanged |
| C-33 | BODY-ORDER-LAYER token | PASS | Token present |
| C-34 to C-35 | Token enumeration + HALT reference | PASS | Unchanged |
| C-36 | Deviation marker at branch level | PASS | DEVIATION: present at branch instruction level |
| C-37 | HALT phrase uniform | PASS | All three AMEND paths use "any of the above tokens is absent" -- identical |
| **C-38** | **Paired marker + vocabulary** | **FAIL** | C-36 PASS (marker present), but no positional vocabulary in branch line -- pairing is the mechanism; marker alone is insufficient |

**Two independent failures**: C-31 and C-38 share a root cause (absent positional vocabulary) but are independent scored criteria in the aspirational tier.

**Aspirational**: 29/31 x 10 = 9.35
**Composite**: 99.35
**Golden**: No

**Projection discrepancy**: R18 design projected 99.68 (30/31). Actual: 99.35 (29/31). The design text correctly documents both C-31 FAIL and C-38 FAIL (coverage table confirms both) -- the projected composite math counted only one failure. Root cause: C-31 and C-38 were treated as a single unit when they are two independent aspirational criteria.

---

### V-04 -- C-38 vocabulary-form probe: "before" replaces "precedes"

**Routing**: `DEVIATION: if REG = engineering or general, DECISION MATRIX before RECOMMENDATION.`
**AMEND HALTs**: All three use "any of the above tokens is absent" uniformly.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 to C-07 | Essential + Recommended | PASS (7/7) | All carry |
| C-08 to C-30 | Prior aspirational | PASS (23/23) | All carry |
| **C-31** | **Positional routing vocabulary** | **PASS** | "before" is rubric-listed positional vocabulary -- equivalent to "precedes" |
| C-32 to C-36 | Routing structure | PASS | All carry |
| C-37 | HALT phrase uniform | PASS | Identical phrase "any of the above tokens is absent" x 3 |
| **C-38** | **Paired marker + vocabulary** | **PASS** | DEVIATION: (marker) + "before" (positional vocabulary) coexist on same line -- rubric lists "before" alongside "precedes" as valid |

**Aspirational**: 31/31 x 10 = 10.00
**Composite**: 100.00
**Golden**: Yes

**Discrimination resolved**: "before" is vocabulary-neutral equivalent to "precedes" for C-38. C-38 vocabulary-neutrality confirmed within the rubric-listed set.

---

### V-05 -- Form-neutrality carry: uniform "any listed token" + OVERRIDE:

**Routing**: `OVERRIDE: if REG = engineering or general, DECISION MATRIX precedes RECOMMENDATION.`
**AMEND HALTs**: "any listed token is absent" -- identical across Add-C, Weight, Override.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 to C-07 | Essential + Recommended | PASS (7/7) | All carry |
| C-08 to C-30 | Prior aspirational | PASS (23/23) | All carry |
| C-31 | Positional routing vocabulary | PASS | "precedes" |
| C-32 | Routing scope deviation-only | PASS | Scope declaration present |
| C-33 | BODY-ORDER-LAYER token | PASS | Token present |
| C-34 to C-35 | Token enumeration + HALT reference | PASS | "any listed token is absent" is positional reference |
| C-36 | Deviation marker at branch level | PASS | OVERRIDE: confirmed equivalent to DEVIATION: (R17 anchor) |
| **C-37** | **HALT phrase uniform** | **PASS** | "any listed token is absent" used identically across all three AMEND paths -- internally uniform within V-05 |
| **C-38** | **Paired marker + vocabulary** | **PASS** | OVERRIDE: (marker) + "precedes" (positional vocabulary) coexist on same line |

**Aspirational**: 31/31 x 10 = 10.00
**Composite**: 100.00
**Golden**: Yes

**Confirmed**: Both R17 form variants (OVERRIDE: and "any listed token") satisfy the full v16 ceiling together without interaction effects.

---

## Discrimination Summary

| Open Question | Resolution |
|---------------|------------|
| Does R17 V-04 satisfy C-37 and C-38 under v16 without modification? | **Yes** -- V-01 = 100.00 |
| What is the numeric weight of C-37 PARTIAL? | **0.5** -- V-02 = 99.84, confirming PARTIAL = 0.5 |
| Is "before" equivalent to "precedes" for C-38? | **Yes** -- V-04 = 100.00 |
| V-03 actual vs projected score? | **99.35 vs 99.68** -- projection error; two independent failures |

---

## Projection Error Analysis -- V-03

The R18 design text states both "C-31 also affected: branch instruction lacks positional ordering vocabulary -- FAIL" and "C-38 FAIL" but then writes "Expected: 30/31 x 10 + 90 = 99.68."

The math (30/31) counts only one failure. Both C-31 and C-38 are independent aspirational criteria (C-08 through C-38 = 31 scoreable aspirational criteria). They share a root cause -- absent positional vocabulary in the routing branch -- but each is an independent entry in the aspirational denominator. Two failures: 29/31 -> 99.35.

The design's coverage table correctly marks both C-31 and C-38 as FAIL for V-03. The error was in computing the composite from the coverage data.

---

## Excellence Signals

### Signal 1 -- Uniform identical HALT phrase (C-37)
Any C-35-valid positional phrase satisfies C-37 when used identically across all three AMEND paths. The criterion is identity-within-output, not identity-across-outputs. V-01/V-04 use "any of the above tokens is absent"; V-05 uses "any listed token is absent" -- both satisfy C-37 within their respective outputs. The specific phrase is form-neutral; uniformity is the mechanism.

### Signal 2 -- Paired deviation marker + positional vocabulary (C-38)
DEVIATION: or OVERRIDE: marker paired with "precedes" or "before" in one directive line satisfies C-38. Both elements are additive: marker labels the branch role; vocabulary describes the ordering effect. Neither substitutes for the other. V-03 confirms: marker alone (DEVIATION: + non-positional outcome phrase) is C-36 PASS but C-38 FAIL.

### Signal 3 -- Vocabulary neutrality within rubric-listed sets
C-38: "before" is equivalent to "precedes" (V-04). C-36/C-38: OVERRIDE: is equivalent to DEVIATION: (V-05). Any form within the rubric-listed vocabulary set satisfies the criterion. Form variants do not create sub-grades.

### Signal 4 -- Independent failure counting when root cause is shared
C-31 and C-38 both fail when the routing branch uses non-positional vocabulary. They share a root cause but are independent criteria in the aspirational denominator. Two failures must be counted separately. Projection errors arise when shared-root-cause failures are treated as one unit.

---

## Watch List Updates

| Key | Rule |
|-----|------|
| `c37-partial-weight-confirmed` | C-37 PARTIAL = 0.5; non-uniformity produces 99.84, not 99.68 (V-02) |
| `c38-marker-only-double-failure` | When routing branch uses non-positional vocabulary: C-31 FAIL + C-38 FAIL = two independent aspirational failures; shared root cause does not collapse them to one failure unit |
| `c38-vocabulary-neutral-confirmed` | "before" satisfies C-38 positional vocabulary requirement; equivalent to "precedes" within rubric-listed set (V-04) |
| `override-equivalent-c38-confirmed` | OVERRIDE: satisfies C-38 deviation marker requirement; equivalent to DEVIATION: within rubric-listed set (V-05) |

---

## Golden Variations

| Variation | Form | Notes |
|-----------|------|-------|
| V-01 | Uniform "any of the above tokens is absent" + DEVIATION: + "precedes" | Canonical form -- R17 V-04 carry |
| V-04 | Uniform "any of the above tokens is absent" + DEVIATION: + "before" | Vocabulary-neutral form -- "before" confirmed equivalent |
| V-05 | Uniform "any listed token is absent" + OVERRIDE: + "precedes" | Alternate-form pair -- both R17 variants satisfy v16 ceiling |
