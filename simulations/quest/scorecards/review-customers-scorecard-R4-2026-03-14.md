# /quest:score — review-customers R4

**Scoring basis**: Prompt structural analysis — trace artifact is placeholder, so each variation is evaluated on the mechanisms present to drive each criterion to pass. All five variations inherit the R3 proven baseline (C-14 prose-first, C-15 close-before-advance, C-16 sub-feature rationale in varying degrees).

---

## Point weights

| Weight class | Points each | Count | Max |
|---|---|---|---|
| Essential | 4 | 5 | 20 |
| Recommended | 3 | 3 | 9 |
| Aspirational | 2 | 11 | 22 |
| **Total** | | **19** | **51** |

PARTIAL = half points. Essential failure caps total regardless of other passes.

---

## Per-Variation Criterion Scoring

### V-01: Amendment Scaffolding

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All 12 personas present | PASS | All 12 IDs listed in STOCK PERSONAS; PERSONA BLOCKS requires each C-NN |
| C-02 | Weighted aggregate | PASS | 3x/2x/1x stated; full formula in WEIGHTED AGGREGATE section |
| C-03 | Adoption blockers | PASS | ADOPTION BLOCKERS section with "If none" clause |
| C-04 | Positioning leaks | PASS | POSITIONING LEAKS section with "If none" clause |
| C-05 | Tier assignment | PASS | TIER ASSIGNMENT section requires all 12 before any persona block |
| C-06 | Delight signals | PASS | DELIGHT SIGNALS section present |
| C-07 | Amendment order | PASS | AMEND explicitly orders blockers → leaks → delight |
| C-08 | Per-persona rationale | PASS | Step 3 requires 2-3 sentences per persona |
| C-09 | Cross-persona pattern | PASS | CROSS-PERSONA PATTERNS requires named feature mechanism, bars "scores vary" |
| C-10 | Amend-to-score projection | PASS | "Projected impact" field with composite delta in AMEND template |
| C-11 | Inline flags at scoring | PASS | Step 4 explicit, "You may not write the next persona's header line until Step 4 is complete" |
| C-12 | Hybrid table+prose | PASS | STRUCTURAL RULE 1 enforces prose-first; table follows |
| C-13 | Causal rationale | PASS | Step 3: "Name the specific feature property...produced these scores" |
| C-14 | Prose-first order | PASS | STRUCTURAL RULE 1 explicit |
| C-15 | Flag deferral prohibition | PASS | STRUCTURAL RULE 2 explicit, names the failure mode |
| C-16 | Sub-feature specificity | PARTIAL | Step 3 says "where possible" — introduces escape clause; 6-of-12 threshold unreliable |
| C-17 | Amendment sub-feature targets | PASS | Explicit "Sub-feature to change: [name...]" template with failure-mode examples |
| C-18 | Cross-persona pattern at sub-feature | FAIL | CROSS-PERSONA only requires "feature mechanism" — no sub-feature resolution |
| C-19 | Three-tier chain traversal | FAIL | ADOPTION BLOCKERS has no L1/L2/L3 requirement |

**V-01 score**: 20 + 9 + (8×2 + 1×1 + 0 + 0) = **46 / 51 = 90**

---

### V-02: Pattern Synthesis Worked Example

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All 12 personas present | PASS | All 12 listed; persona block structure complete |
| C-02 | Weighted aggregate | PASS | 3x/2x/1x; full calculation required |
| C-03 | Adoption blockers | PASS | ADOPTION BLOCKERS with "If none" |
| C-04 | Positioning leaks | PASS | POSITIONING LEAKS with "If none" |
| C-05 | Tier assignment | PASS | TIER ASSIGNMENT before persona blocks |
| C-06 | Delight signals | PASS | DELIGHT SIGNALS section present |
| C-07 | Amendment order | PASS | AMEND: blockers → leaks → delight |
| C-08 | Per-persona rationale | PASS | 2-3 sentences required in persona block |
| C-09 | Cross-persona pattern | PASS | CROSS-PERSONA has worked example; requirement present |
| C-10 | Amend-to-score projection | PASS | Projection template in AMEND |
| C-11 | Inline flags at scoring | PASS | Flag resolution mandatory before advancing, all checks listed |
| C-12 | Hybrid table+prose | PASS | Prose blocks before table enforced |
| C-13 | Causal rationale | PASS | CAUSAL PRECISION section explicitly requires sub-feature property naming |
| C-14 | Prose-first order | PASS | STRUCTURAL RULE 1 explicit |
| C-15 | Flag deferral prohibition | PASS | STRUCTURAL RULE 2 explicit |
| C-16 | Sub-feature specificity | PASS | CAUSAL PRECISION section is mandatory (not "where possible") with anti-example |
| C-17 | Amendment sub-feature targets | PARTIAL | AMEND says "specific sub-feature change" but no explicit per-item field or failure-mode example |
| C-18 | Cross-persona pattern at sub-feature | PASS | Full worked contrast: feature-level vs sub-feature-level with "why it fails" / "why it works" analysis |
| C-19 | Three-tier chain traversal | FAIL | ADOPTION BLOCKERS only requires "[sub-feature property blocking adoption]" — no L1/L2/L3 |

**V-02 score**: 20 + 9 + (9×2 + 1×1 + 0) = **48 / 51 = 94**

---

### V-03: Three-Tier Blocker Traversal

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All 12 personas present | PASS | All 12 listed; persona block structure complete |
| C-02 | Weighted aggregate | PASS | 3x/2x/1x; full calculation required |
| C-03 | Adoption blockers | PASS | ADOPTION BLOCKERS with "If none" |
| C-04 | Positioning leaks | PASS | POSITIONING LEAKS with "If none" |
| C-05 | Tier assignment | PASS | TIER ASSIGNMENT before persona blocks |
| C-06 | Delight signals | PASS | DELIGHT SIGNALS section present |
| C-07 | Amendment order | PASS | AMEND orders: blockers → leaks → delight |
| C-08 | Per-persona rationale | PASS | 2-3 sentences, framing instruction present |
| C-09 | Cross-persona pattern | PASS | "Named cross-cutting pattern that names a feature mechanism" required |
| C-10 | Amend-to-score projection | PASS | Projection template in AMEND |
| C-11 | Inline flags at scoring | PASS | Flag resolution mandatory before advancing |
| C-12 | Hybrid table+prose | PASS | STRUCTURAL RULE 1; table after all 12 prose blocks |
| C-13 | Causal rationale | PASS | Rationale framing: "the feature's [X] produced this reaction" |
| C-14 | Prose-first order | PASS | STRUCTURAL RULE 1 explicit |
| C-15 | Flag deferral prohibition | PASS | STRUCTURAL RULE 2 explicit |
| C-16 | Sub-feature specificity | PARTIAL | "where possible" escape clause present — same as V-01; no mandatory CAUSAL PRECISION block |
| C-17 | Amendment sub-feature targets | PARTIAL | AMEND says "specific sub-feature change" but no explicit field template or failure-mode description |
| C-18 | Cross-persona pattern at sub-feature | FAIL | CROSS-PERSONA only requires "feature mechanism" — no sub-feature worked example |
| C-19 | Three-tier chain traversal | PASS | Explicit L1/L2/L3 label requirement with chain definition, non-traversal failure modes named ("L1+L3 without L2 skips bridge") |

**V-03 score**: 20 + 9 + (8×2 + 2×1 + 0) = **47 / 51 = 92**

---

### V-04: C-17 + C-18 Combined (Formal)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All 12 personas present | PASS | All 12 in PERSONA BLOCKS |
| C-02 | Weighted aggregate | PASS | 3x/2x/1x; full formula |
| C-03 | Adoption blockers | PASS | ADOPTION BLOCKERS with "If none" |
| C-04 | Positioning leaks | PASS | POSITIONING LEAKS with "If none" |
| C-05 | Tier assignment | PASS | TIER ASSIGNMENT before persona blocks |
| C-06 | Delight signals | PASS | DELIGHT SIGNALS section present |
| C-07 | Amendment order | PASS | AMEND explicitly: blockers → leaks → delight |
| C-08 | Per-persona rationale | PASS | Step 3: 2-3 sentences |
| C-09 | Cross-persona pattern | PASS | CROSS-PERSONA PATTERNS requires sub-feature mechanism; pattern implication stated |
| C-10 | Amend-to-score projection | PASS | Projection template in AMEND |
| C-11 | Inline flags at scoring | PASS | Step 4 explicit, "You may not write the next persona's header line until Step 4 is complete" |
| C-12 | Hybrid table+prose | PASS | STRUCTURAL RULE 1 and 2 enforced |
| C-13 | Causal rationale | PASS | Step 3: "the feature's [X] produced this reaction" |
| C-14 | Prose-first order | PASS | STRUCTURAL RULE 1 explicit with failure-mode named |
| C-15 | Flag deferral prohibition | PASS | STRUCTURAL RULE 2 explicit, failure mode named |
| C-16 | Sub-feature specificity | PASS | Step 3: "the specific capability, threshold, design decision, or workflow step -- not the feature generically" — no "where possible" weakening |
| C-17 | Amendment sub-feature targets | PASS | "Sub-feature amendment target: [name...]" field with explicit failure-mode description and examples of what generic looks like |
| C-18 | Cross-persona pattern at sub-feature | PASS | Three-level contrast (segment-only / feature-level / sub-feature-level) with "why it fails" analysis for each level; "Name the sub-feature mechanism" as explicit close |
| C-19 | Three-tier chain traversal | FAIL | ADOPTION BLOCKERS only requires "[sub-feature property blocking adoption]" — L1/L2/L3 requirement absent |

**V-04 score**: 20 + 9 + (10×2 + 0) = **49 / 51 = 96**

---

### V-05: Full R4 Conversational

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | All 12 personas present | PASS | All 12 in panel seats, tier assignment required for all before reasoning |
| C-02 | Weighted aggregate | PASS | "Primary personas carry 3x... Show how you weighted it" in WHAT DO THE NUMBERS SAY? |
| C-03 | Adoption blockers | PASS | IS ADOPTION BLOCKED? section; "If no primary persona scored below 3: 'No adoption blockers.'" |
| C-04 | Positioning leaks | PASS | IS THE POSITIONING LEAKING? section; "If no leaks: 'No positioning leaks.'" |
| C-05 | Tier assignment | PASS | WHO IS THIS FEATURE FOR? requires tier for all 12 before any individual reasoning |
| C-06 | Delight signals | PASS | WHO IS DELIGHTED? section with "If there are no 5s" clause |
| C-07 | Amendment order | PASS | WHAT SHOULD CHANGE? orders: blockers → leaks → delight amplification |
| C-08 | Per-persona rationale | PASS | 2-3 sentences; Level 3 required for every persona |
| C-09 | Cross-persona pattern | PASS | WHAT DO THE NUMBERS SAY? requires "named causal finding" with sub-feature cause — bars distribution observation |
| C-10 | Amend-to-score projection | PASS | "Fixing [sub-feature] for [ID] likely lifts primary Would-Adopt by ~[delta]..." template |
| C-11 | Inline flags at scoring | PASS | "You may not write the next person's name until the current person's flags are resolved" — three explicit flag checks |
| C-12 | Hybrid table+prose | PASS | "Write all twelve prose entries before writing any part of the table" |
| C-13 | Causal rationale | PASS | Three-level worked example (LEVEL 1/2/3) makes Level 3 the stated requirement |
| C-14 | Prose-first order | PASS | "The prose comes before the table -- always" in opening framing |
| C-15 | Flag deferral prohibition | PASS | "A flag that only appears in a summary section later...was deferred, not applied. Deferral is not the same as inline flagging." |
| C-16 | Sub-feature specificity | PASS | Three-level worked example + "Write Level 3 for every persona" — mandatory, no escape clause |
| C-17 | Amendment sub-feature targets | PASS | "The amendment target must be the sub-feature mechanism, not a restatement of the feature-level gap" + explicit anti-example ("improve offline support" as failure case) |
| C-18 | Cross-persona pattern at sub-feature | PASS | Distribution vs pattern vs sub-feature-cause three-level example with "why" for each; "Name the sub-feature mechanism" as close |
| C-19 | Three-tier chain traversal | PASS | IS ADOPTION BLOCKED? explicitly requires three-part chain for at least one blocker: "First, the stakes... Then, the feature-level gap... Then, the sub-feature mechanism" — narrative form forces traversal; non-traversal failure mode named ("named mechanism without context") |

**V-05 score**: 20 + 9 + (11×2 + 0) = **51 / 51 = 100**

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Total | Score | All Essential Pass |
|-----------|-----------|-------------|--------------|-------|-------|--------------------|
| V-01 | 20/20 | 9/9 | 17/22 | 46/51 | **90** | YES |
| V-02 | 20/20 | 9/9 | 19/22 | 48/51 | **94** | YES |
| V-03 | 20/20 | 9/9 | 18/22 | 47/51 | **92** | YES |
| V-04 | 20/20 | 9/9 | 20/22 | 49/51 | **96** | YES |
| V-05 | 20/20 | 9/9 | 22/22 | 51/51 | **100** | YES |

**Ranking**: V-05 > V-04 > V-02 > V-03 > V-01

---

## Excellence Signals from V-05

**1. Narrative three-part chain description outperforms labeled L1/L2/L3 for C-19**
V-03 uses explicit labels (L1/L2/L3) which force presence but can become checklist compliance. V-05 describes the chain structure as a reader narrative: "First, the stakes... Then, the feature-level gap... Then, the sub-feature mechanism" — framing it as something a reader must be able to follow from start to finish. The narrative framing tests traversability rather than just label presence. The closing instruction ("An entry that names only the sub-feature (the third part) without establishing stakes and feature-level gap is not a causal chain -- it is a named mechanism without context") makes the failure mode concrete.

**2. Integrated aggregate + pattern synthesis in one section eliminates the cognitive task switch**
V-04 and V-02 treat WEIGHTED AGGREGATE and CROSS-PERSONA PATTERNS as separate sections. V-05 combines both into WHAT DO THE NUMBERS SAY? — computing the aggregate first, then pivoting directly to "Now look across all twelve explanations for a pattern that names a sub-feature mechanism." This sequencing keeps the sub-feature specificity requirement active during pattern synthesis, reducing the risk of falling back to feature-level when switching sections.

**3. Amendment chain parity via anti-example**
V-05 closes C-17 not with a template field but with an explicit anti-example in the amendment instruction: "If the chain said 'the sync architecture's hard write-connection requirement,' the amendment is 'add a local-cache mode to the sync step' — not 'improve offline support.'" The anti-example names the exact failure mode (the feature-level restatement) and the correct form side by side, which is the same mechanism that drove C-16 compliance in R3 V-02.

**4. Conversational framing sustains depth through 12 persona blocks**
"Work through this as a customer advisory panel" and "Take each person through the feature one at a time" set a social reasoning frame that resists the compression that tends to flatten later persona entries. R3 confirmed conversational register as the strongest depth predictor; V-05 extends that register to cover all three R4 sections without displacing R3's per-persona mechanisms.

**5. Three-level per-persona worked example (LEVEL 1/2/3) makes sub-feature the named floor**
Rather than describing what sub-feature specificity looks like, V-05 shows it at all three levels with "why it fails" analysis for LEVEL 1 and LEVEL 2. The close "Write Level 3 for every persona" makes it mandatory. This is the same mechanism that drove C-16 in R3; V-05 carries it forward without modification, confirming it is stable across rounds.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["three-part causal chain in narrative framing (stakes-gap-mechanism) tests traversability more completely than explicit L1/L2/L3 labels by requiring the reader to follow the chain rather than confirm label presence", "integrating aggregate computation and sub-feature pattern synthesis in a single section (WHAT DO THE NUMBERS SAY?) prevents sub-feature specificity from decaying during the cognitive task switch from scoring to pattern analysis"]}
```
