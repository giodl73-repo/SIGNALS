## roles-create R15 Scorecard

### Results

| Rank | Variation | Score | Failing Criteria |
|------|-----------|-------|-----------------|
| 1 | **V-05** | **100.00** | -- |
| 2 | V-01 | 99.58 | C-31 only |
| 3 (tie) | V-02 | 99.17 | C-31 + C-30 |
| 3 (tie) | V-04 | 99.17 | C-31 + C-26 |
| 5 | V-03 | 98.75 | C-31 + C-29 + C-30 |

All essential pass. Top score: 100.

---

### Key R15 Findings

**C-31 isolation confirmed (V-01 = 23/24).** C-31 fires on verbose gate conditions without cascading to C-23. Gate condition text is structural scaffolding — outside the three canonical rule locations that C-23 governs. C-31 is the fully independent criterion for this surface. Primary open question resolved: V-01 scores 99.58, not 99.17.

**C-23 non-cascade confirmed.** Verbose gate conditions do not trigger C-23. C-31 was added precisely because C-23 does not govern gate condition text. One criterion, one surface.

**C-29 → C-30 cascade confirmed (V-03 = 21/24, below design estimate).** The variation predicted 22/24 (C-31 + C-29 only). Actual: 21/24. The rule "C-30 implies C-29; if C-29 fails, C-30 fails" is a hard cascade — bare PASS branches cannot rescue C-30 when FAIL branches carry correction directives. V-03 loses 3 criteria, not 2.

**V-03 vs V-02 asymmetry.** FAIL-branch correction (C-29 fail + C-30 cascade = 2 hits) is more costly than PASS-branch affirmation (C-30 fail only = 1 hit). The cascade is directional: annotated FAIL pulls C-30 down; annotated PASS does not pull C-29 down.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-31 fires in isolation without C-23 cascade -- gate condition text is structural scaffolding exempt from C-23 scope; C-31 is the specific governing criterion for that surface", "C-29 fail cascades to C-30 fail regardless of PASS branch content -- bare PASS branches cannot rescue C-30 when FAIL branches carry correction directives; the cascade is directional (C-29 fail implies C-30 fail, not the reverse)", "verbose gate conditions supply the semantic substrate for PASS-branch affirmation restatements -- thin CONTRACT-citation conditions eliminate this substrate, making C-30 violations structurally unmotivated; C-31 and C-30 are causally linked but independently scored"]}
```
ASS | PASS | PASS | PASS | PASS | Phase 2 generates full companion file when absent |
| C-12 | PASS | PASS | PASS | PASS | PASS | INTERACTIVE-HOLD contract prohibits partial generation before all three answers |
| C-13 | PASS | PASS | PASS | PASS | PASS | Phase 5 pre-write confirmation with explicit YES/NO checklist |
| C-14 | PASS | PASS | PASS | PASS | PASS | Phase 0 INPUT-ROUTING-RULES classifies all malformed inputs before mode detection |
| C-15 | PASS | PASS | PASS | PASS | PASS | In-phase gates at Phases 0, 1, 2, 3, 4; Phase 5 is final confirmation |
| C-16 | PASS | PASS | PASS | PASS | PASS | CONTRACT: AUDIT-CHECKLIST defined before any phase |
| C-17 | PASS | PASS | PASS | PASS | PASS | Six named CONTRACT blocks at top level in all variations |
| C-18 | PASS | PASS | PASS | PASS | PASS | Checklist rows have "Gated At" column; phase gates carry `[G]`, `[H]`, `[B]`-`[F]` backward citations |
| C-19 | PASS | PASS | PASS | PASS | PASS | Phase bodies cite CONTRACT by name; no rule restatement across all variations |
| C-20 | PASS | PASS | PASS | PASS | PASS | Checklist items name CONTRACT block + scope only; no rule enumeration |
| C-21 | PASS | PASS | PASS | PASS | PASS | All cited CONTRACTs covered by checklist items; Phase 1/INTERACTIVE-HOLD is routing, not content-producing |
| C-22 | PASS | PASS | PASS | PASS | PASS | AUDIT-CHECKLIST header: "Items name the CONTRACT block and validation scope only -- no rule enumeration." |
| C-23 | PASS | PASS | PASS | PASS | PASS | **C-31 isolation confirmed**: verbose gate condition text is structural scaffolding, not a phase step, checklist item, or CONTRACT block. C-23's exclusion list ("structural annotations") does not absorb gate condition text -- gate annotations are structural scaffolding exempt from C-23 scope. C-31 is the specific governing criterion for this surface; C-23 does not cascade. Rule content remains confined to its three canonical locations in all variations. |
| C-24 | PASS | PASS | PASS | PASS | PASS | All gates use inline annotation form `-> Gate N [ID]: ... PASS / FAIL` throughout all five variations |

**Discriminating criteria:**

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-25 | PASS | PASS | PASS | PASS | PASS | All phase bodies citation-only; no body surface excess in any R15 variation |
| C-26 | PASS | PASS | PASS | **FAIL** | PASS | V-04: COLUMN-HEADER defined 3rd (before FIELD-REGISTER which is defined 4th) -- inverts Phase 3/Phase 4 first-citation order. All others maintain canonical sequence (INPUT-ROUTING-RULES -> INTERACTIVE-HOLD -> FIELD-REGISTER -> COLUMN-HEADER -> INERTIA-ADVOCATE-TEMPLATE -> AUDIT-CHECKLIST) |
| C-27 | PASS | PASS | PASS | PASS | PASS | All phase bodies open with CONTRACT citation; no opener prose before citation in any variation |
| C-28 | PASS | PASS | PASS | PASS | PASS | No correction logic in phase body narrative in any variation; FAIL branches are the correction surface for V-03 |
| C-29 | PASS | PASS | **FAIL** | PASS | PASS | V-03 FAIL branches carry correction directives: "FAIL: Apply the correction action from the INPUT-ROUTING-RULES classification table before continuing.", "FAIL: Re-prompt for area and subrole before advancing.", "FAIL: Resolve all remaining literal `{area}` slots before advancing.", "FAIL: Add any missing fields before advancing.", "FAIL: Rewrite orientation.frame to first-person observational register before advancing.", etc. V-01/V-02/V-04 FAIL branches are bare `PASS / FAIL`. V-05 canonical bare. |
| C-30 | PASS | **FAIL** | **FAIL** | PASS | PASS | V-02: PASS branches carry affirmation summaries restating the verbose gate condition in confirmation form: "PASS: Input pattern identified and classified as clean or resolved.", "PASS: All 12 frontmatter fields confirmed present.", "PASS: orientation.frame confirmed in first-person observational register.", "PASS: lens.verify confirms >= 4 boolean items.", etc. V-03: **C-30 fails by cascade from C-29** -- the implication "C-30 implies C-29; if C-29 fails, C-30 fails" is explicit; V-03's bare PASS branches cannot override the cascade. V-01/V-04: bare PASS branches with verbose conditions, C-30 passes independently. V-05 canonical bare. |
| C-31 | **FAIL** | **FAIL** | **FAIL** | **FAIL** | PASS | V-01/V-02/V-03/V-04: gate conditions enumerate rule-level field specifics inline -- "All 12 frontmatter fields are present: name, version, archetype, orientation.frame, orientation.serves, lens.verify (list), lens.simplify (list), expertise.depth, expertise.relevance, scope, collaborates_with, artifacts, and workflow.", "orientation.frame is written in first-person observational register: opens with a first-person lens verb (Sees, Treats, Reads, Approaches) and describes how the role perceives its domain...", "lens.verify contains >= 4 items; every item is a yes/no boolean question that names a specific artifact, config file, system state, or threshold...", etc. All enumerate rule content from CONTRACT blocks in the condition line -- fail. V-05: gate conditions are pure CONTRACT-citation expressions -- "INPUT-ROUTING-RULES -- input classification and resolution", "FIELD-REGISTER -- frontmatter completeness", "FIELD-REGISTER -- orientation.frame register", "FIELD-REGISTER -- orientation.serves beneficiary", "COLUMN-HEADER -- body table domain vocabulary", etc. CONTRACT name + scope, nothing more. PASS. |

---

### Composite Scores

| | Essential (max 60) | Recommended (max 30) | Aspirational (max 10) | **Total** |
|--|---|---|---|---|
| **V-01** | 5/5 -> 60 | 2/2 -> 30 | 23/24 -> 9.583 | **99.58** |
| **V-02** | 5/5 -> 60 | 2/2 -> 30 | 22/24 -> 9.167 | **99.17** |
| **V-03** | 5/5 -> 60 | 2/2 -> 30 | 21/24 -> 8.750 | **98.75** |
| **V-04** | 5/5 -> 60 | 2/2 -> 30 | 22/24 -> 9.167 | **99.17** |
| **V-05** | 5/5 -> 60 | 2/2 -> 30 | 24/24 -> 10.000 | **100.00** |

---

### Ranking

| Rank | Variation | Score | Failing Criteria |
|------|-----------|-------|-----------------|
| 1 | V-05 | 100.00 | -- |
| 2 | V-01 | 99.58 | C-31 only |
| 3 (tie) | V-02 | 99.17 | C-31 + C-30 |
| 3 (tie) | V-04 | 99.17 | C-31 + C-26 |
| 5 | V-03 | 98.75 | C-31 + C-29 + C-30 |

---

### R15 Discrimination Results

**C-31 isolation confirmed (V-01, 23/24):** C-31 fires on rule-enumerating gate condition text in isolation -- 1 deduction, no C-23 cascade. Gate condition text is structural scaffolding; C-23's exclusion list does not absorb it. C-31 is the fully independent governing criterion for this surface. V-01 scores 23/24 = 99.58, resolving the primary R15 open question.

**C-23 non-cascade confirmed (V-01):** Verbose gate conditions do not trigger C-23 ("rule content outside the three canonical locations"). Gate annotations are structural scaffolding, not phase steps or checklist items. The three canonical rule locations remain: CONTRACT block, thin phase citation, thin checklist item. C-31 was added precisely because C-23 does not govern this surface. One criterion, one surface.

**C-31 + C-30 orthogonality confirmed (V-02, 22/24):** C-31 and C-30 are independent additive deductions on two distinct gate surfaces -- gate condition text and PASS branch text. Verbose conditions supply the semantic substrate for PASS affirmation restatements; both fire together but neither triggers the other. The causal story from v13 is confirmed: 2 independent scored violations when the full pattern is instantiated.

**C-31 + C-26 orthogonality confirmed (V-04, 22/24):** C-31 (gate condition surface) and C-26 (CONTRACT definition ordering) are orthogonal across entirely different structural dimensions. Two deductions, no cascade. Gate condition verbosity has no effect on CONTRACT block ordering; ordering violations have no effect on gate condition form.

**C-29 -> C-30 cascade confirmed (V-03, 21/24 -- below design estimate):** The variation design predicted 2 deductions (C-31 + C-29 = 22/24 = 99.17). Actual: 3 deductions (C-31 + C-29 + C-30 = 21/24 = 98.75). The implication "C-30 implies C-29; if C-29 fails, C-30 fails" is a hard scoring rule: C-30 automatically fails when C-29 fails, regardless of whether PASS branches are bare. Bare PASS branches cannot rescue C-30 once FAIL branches carry correction directives. This distinguishes V-03 from the design prediction and from V-02.

**V-03 vs V-02 asymmetry:** V-03 (C-31 + C-29 + C-30 = 3 deductions = 98.75) scores BELOW V-02 (C-31 + C-30 = 2 deductions = 99.17). A FAIL-branch correction directive is more costly than a PASS-branch affirmation summary -- it triggers a cascade while PASS-branch annotation does not. The C-29 -> C-30 cascade is directional: annotated FAIL branches pull C-30 down; annotated PASS branches do not pull C-29 down.

**Cascade directionality confirmed:** C-30 fails when C-29 fails (cascade). C-29 does NOT fail when C-30 fails (no reverse cascade). V-02 demonstrates this: annotated PASS branches (C-30 fail) with bare FAIL branches (C-29 pass). The asymmetry is structural -- C-30 is strictly stronger than C-29.

---

### Excellence Signals (V-05)

1. **Gate conditions as CONTRACT-citation expressions eliminate annotation substrate** -- "FIELD-REGISTER -- frontmatter completeness" contains no field enumeration, register description, or count threshold; there is no semantic material for a PASS branch to restate in confirmation form. Thin conditions make C-30 violations structurally unmotivated
2. **Full gate purity: three surfaces clean simultaneously** -- thin condition (C-31), bare FAIL (C-29), bare PASS (C-30) all pass together; a gate of the form `-> Gate N [ID]: {CONTRACT-reference} -- PASS / FAIL` has no annotation prose in any position
3. **The no-restatement convergence is complete** -- C-31 joins C-19 (phase body) and C-20 (checklist items) as the third thin-reference criterion; a skill passing all three has a single canonical rule location for every CONTRACT constraint: the CONTRACT block itself

---

### R15 Confirmation Summary

- **C-31 isolation confirmed**: verbose gate condition text triggers exactly 1 deduction (C-31 only). C-23 does not cascade. Gate condition text is structural scaffolding outside C-23's scope. V-01: 23/24 = 99.58.
- **C-23 non-cascade confirmed**: C-31 is the specific governing criterion for gate condition text. Rule content in gate conditions is governed by C-31 alone. The three canonical rule locations (CONTRACT block, thin phase citation, thin checklist item) are confirmed as a complete partition.
- **C-31 + C-30 orthogonality confirmed**: V-02 scores 22/24. Two independent deductions. Verbose conditions supply the affirmation substrate; both C-31 and C-30 fire without cascading to C-29 or C-23.
- **C-29 -> C-30 cascade confirmed**: V-03 scores 21/24 (below design estimate of 22/24). FAIL-branch correction directives trigger C-30 by implication; bare PASS branches cannot override the cascade. The cascade is directional.
- **C-31 + C-26 orthogonality confirmed**: V-04 scores 22/24. Gate condition surface and CONTRACT ordering surface are independent; two deductions, no cascade.
- **No-restatement convergence complete**: With C-31 confirmed discriminating, the no-restatement principle covers all three thin-reference surfaces -- phase bodies (C-19), checklist items (C-20), gate conditions (C-31). A skill passing all three has a single canonical rule location for every CONTRACT constraint.
- **R15 ranking**: V-05 (100.00, 24/24) > V-01 (99.58, 23/24, C-31 only) > V-02 = V-04 (99.17, 22/24) > V-03 (98.75, 21/24, C-31+C-29+C-30).
- **Denominator**: 24. V-05 (canonical form) confirmed at 24/24 = 100.00 under v13.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-31 fires in isolation without C-23 cascade -- gate condition text is structural scaffolding exempt from C-23 scope; C-31 is the specific governing criterion for that surface", "C-29 fail cascades to C-30 fail regardless of PASS branch content -- bare PASS branches cannot rescue C-30 when FAIL branches carry correction directives; the cascade is directional (C-29 fail implies C-30 fail, not the reverse)", "verbose gate conditions supply the semantic substrate for PASS-branch affirmation restatements -- thin CONTRACT-citation conditions eliminate this substrate, making C-30 violations structurally unmotivated; C-31 and C-30 are causally linked but independently scored"]}
```
