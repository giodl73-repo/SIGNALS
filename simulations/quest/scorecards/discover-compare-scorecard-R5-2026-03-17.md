---

## discover-compare Round 5 — Scoring Complete

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 (tie) | V-01 token-bind | **100.0** | YES |
| 1 (tie) | V-02 self-verify | **100.0** | YES |
| 1 (tie) | V-03 inline-token-check | **100.0** | YES |
| 1 (tie) | V-04 full-integration | **100.0** | YES |
| 5 | V-05 lean-anchor | **95.0** | YES |

**Predicted vs actual:** exact match. The hypothesis held: V-01–V-04 all 100.0, V-05 95.0.

**What the R5 mechanisms do, per criterion:**

All four full variations pass all 18 criteria at 100.0. The R5 additions (token binding, TOKEN RECALL, terminal audit) don't create new rubric passes — they harden the same criteria against drift failure modes that the v4 rubric cannot directly test. V-04 is the canonical because it combines all three mechanisms as non-overlapping guards:

- **Token binding** (V-01 base) — prevents silent prose substitution at Phase 0 declaration
- **TOKEN RECALL headers** (V-03, V-04) — catches drift at point-of-use before each sensitive phase
- **Phase 10 terminal audit** (V-02, V-04) — catches structural omissions above the token level before the artifact is written

**V-05** stays at 95.0 because token binding doesn't unlock any of the five by-design gaps (C-09/C-10/C-14/C-15/C-16). The only future discriminator is a v6 criterion: "ANCHOR token name appears literally in 3+ downstream phases."

**Three new patterns confirmed for the record.**

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["ANCHOR token binding with explicit binding rule makes Option 0 prose drift detectable by requiring literal token reproduction downstream", "TOKEN RECALL inline headers at Phases 3/6/7 force value reproduction at point-of-use before each anchor-sensitive output", "Terminal structural audit (Phase 10) creates closed-loop contract: declare -> use -> verify; catches structural omissions that token binding cannot prevent"]}
```
ding + inline recall + terminal audit). Three non-overlapping drift guards across the full output lifecycle: silent substitution prevented at declaration, caught at point-of-use, verified at terminal audit. No criteria regress vs V-04/R4; all three R5 mechanisms complement each other without overlap.

---

## V-01: token-bind -- 100.0 / Golden

| ID | Score | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 3 covers all four dimensions for A and B independently before moving to next dimension. |
| C-02 | PASS | INERTIA RULE: "The question for A: would teams keep using ANCHOR[0A] INSTEAD OF building Option A?" and same for B vs ANCHOR[0B]. Both independently grounded by token name. |
| C-03 | PASS | Phase 4 (3-col Table 1) + Phase 5 (2-col Table 2); Phase 7 recommendation states explicit choice from {A/B/neither/defer}. |
| C-04 | PASS | Phase 7: "Recommendation traceable to Table 2 (Phase 5) -- do not assert a winner that contradicts the matrix signals without explicit justification. If the recommendation diverges from the matrix plurality, state the reason explicitly." |
| C-05 | PASS | Phase 6 GATE A: "INERTIA GATE: ANCHOR[0A] beats Option A and ANCHOR[0B] beats Option B. Teams will not build either option without a forcing function. 'Build neither' is the leading recommendation." Token names used in gate language. |
| C-06 | PASS | Phase 7 all registers include trade-off: "what is given up by not choosing the other option." |
| C-07 | PASS | ANTI-PATTERN GUARD names four concrete vectors (speed, cost, ecosystem, capability) with "what ANCHOR[0A]/ANCHOR[0B] cannot do" framing. |
| C-08 | PASS | Table 2 is 2-column; "Rating + one-phrase signal. No empty cells." Reader reaches recommendation without re-reading Phase 3 or 4. |
| C-09 | PASS | Phase 9 handles all 3 AMEND types; ANCHOR[0C] token defined on Type 1 with binding extension. |
| C-10 | PASS | exec/engineering/general with per-phase, per-dimension specificity; Phase 7 has distinct lead structures per register. |
| C-11 | PASS | Table 1 (Phase 4) is 3-column A/B/Option 0; N/A cells labeled "N/A (no build required)" and "N/A (this IS the anchor)". Option 0 column header uses ANCHOR[0A]/ANCHOR[0B] token names. |
| C-12 | PASS | ANTI-PATTERN GUARD explicitly names failure phrases: "Generic competitive analysis uses phrases such as 'more competitive,' 'better positioned,' or 'stronger in the market'..." |
| C-13 | PASS | `=== TABLE GUIDE ===` section with purpose statements before Phase 4; Phase 4 header `[ -> See Table 2 (Phase 5) for A-vs-B decision summary ]`; Phase 5 header `[ <- Source: Table 1 (Phase 4); Option 0 column excluded. ]`. Full bidirectional. |
| C-14 | PASS | AMEND Type 1 expands both tables: Table 1 grows to 4-column, Table 2 grows to 3-column A/B/C; both headers updated with cross-references; Option 0 column header extended to ANCHOR[0A]/[0B]/[0C]. |
| C-15 | PASS | Phase 3 risk: "Register: {applies from Phase 1 -- risk framing dimension}"; Phase 3 competitive: "Register: {applies from Phase 1 -- competitive framing dimension}"; Phase 4: "Register: {applies from Phase 1 -- cell emphasis dimension}"; Phase 5: same; Phase 7: "Register: {applies from Phase 1 -- lead structure dimension}". All 5 sensitive phases annotated at point-of-use. |
| C-16 | PASS | Phase 1 print: "Contract: Phase 3 [risk, competitive], Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 9 [framing]." Dimension-level phase index -- strongest form, inherited from V-04/R4. |
| C-17 | PASS | Dedicated `=== TABLE GUIDE ===` section with purpose statements + Phase 4 `[ -> ]` header + Phase 5 `[ <- ]` header. Both C-17 components satisfied. |
| C-18 | PASS | `=== PHASE 0: STATUS QUO ANCHOR (Option 0) ===` is the first phase; commits ANCHOR[0A]/ANCHOR[0B] with binding rule before Phase 1 register, Phase 2 context, Phase 3 analysis. Binding rule is new R5 addition; strongest C-18 form yet. |

**Scores**: Essential 60.0 + Recommended 30.0 + Aspirational (10/10 x 10) 10.0 = **100.0**
**Golden**: YES (all 5 essential PASS, no PARTIAL)

---

## V-02: self-verify -- 100.0 / Golden

| ID | Score | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 3 all four dimensions for A and B. |
| C-02 | PASS | INERTIA RULE: bilateral independent check; A vs ANCHOR[0A], B vs ANCHOR[0B] by token name. |
| C-03 | PASS | Phase 4 (3-col) + Phase 5 (2-col); Phase 7 explicit recommendation with choice set. |
| C-04 | PASS | Phase 7: explicit traceability rule and divergence-reason requirement. Phase 10 audit verifies this before output is returned. |
| C-05 | PASS | Phase 6 GATE A raises "build neither." Phase 10 audit item 9 verifies: "If GATE A fired: 'build neither' named OR forcing function named in Phase 7." |
| C-06 | PASS | Phase 7 all registers include trade-off clause. |
| C-07 | PASS | ANTI-PATTERN GUARD with four concrete vector types and named failure phrases. |
| C-08 | PASS | Table 2 is 2-column scannable. Phase 10 audit items 5-6 verifies bidirectional headers present. |
| C-09 | PASS | Phase 9 handles all 3 AMEND types. |
| C-10 | PASS | exec/engineering/general with per-phase, per-dimension specificity. Phase 10 audit item 2 verifies register contract printed with phase index. |
| C-11 | PASS | Table 1 3-column with labeled N/A cells. Option 0 column header uses ANCHOR token names. |
| C-12 | PASS | ANTI-PATTERN GUARD named in Phase 3 competitive section. |
| C-13 | PASS | TABLE GUIDE section + bidirectional `[ -> ]` / `[ <- ]` headers. Phase 10 audit items 4-6 verify: "TABLE GUIDE present before Phase 4? Phase 4 header carries `[ -> ]`? Phase 5 header carries `[ <- ]`?" |
| C-14 | PASS | AMEND Type 1 expands both tables coherently with updated cross-references. |
| C-15 | PASS | All 5 register-sensitive phases annotated at point-of-use (same as V-01). |
| C-16 | PASS | Phase 1 print with dimension-level phase index. Phase 10 audit item 2 verifies: "register contract printed with dimension-level phase index." |
| C-17 | PASS | TABLE GUIDE section + bidirectional headers. Phase 10 audit independently verifies both structural components. |
| C-18 | PASS | Phase 0 dedicated STATUS QUO ANCHOR before all analysis. ANCHOR binding rule present. |

**Note**: Phase 10 adds a 9-item pre-return audit that verifies all structural criteria before output. Catches structural omissions (missing TABLE GUIDE, one-sided inertia, untraceable recommendation) that token binding alone cannot prevent. Correction opportunity before artifact write.

**Scores**: Essential 60.0 + Recommended 30.0 + Aspirational (10/10 x 10) 10.0 = **100.0**
**Golden**: YES (all 5 essential PASS, no PARTIAL)

---

## V-03: inline-token-check -- 100.0 / Golden

| ID | Score | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 3 all four dimensions for A and B. |
| C-02 | PASS | INERTIA RULE: bilateral independent check vs ANCHOR tokens. TOKEN RECALL at Phase 3 forces model to reproduce "ANCHOR[0A] = {value}" before running inertia dimension -- strongest C-02 enforcement mechanism in R5. |
| C-03 | PASS | Phase 4 (3-col) + Phase 5 (2-col); Phase 7 with TOKEN RECALL before recommendation output. |
| C-04 | PASS | Phase 7 traceability rule + TOKEN RECALL ensures recommendation is written after explicitly recalling committed anchor values. |
| C-05 | PASS | Phase 6 GATE A with ANCHOR token names + TOKEN RECALL before gate logic ensures anchor values are current at point of gate evaluation. |
| C-06 | PASS | Phase 7 all registers include trade-off. |
| C-07 | PASS | ANTI-PATTERN GUARD with four concrete vectors. |
| C-08 | PASS | Table 2 is 2-column scannable. |
| C-09 | PASS | Phase 9 handles all 3 AMEND types; Option C TOKEN RECALL sub-section in AMEND Type 1 and Type 3. |
| C-10 | PASS | exec/engineering/general with per-phase, per-dimension contract (same as V-01). |
| C-11 | PASS | Table 1 3-column with labeled N/A cells; Option 0 header uses ANCHOR token names. |
| C-12 | PASS | ANTI-PATTERN GUARD named in Phase 3. |
| C-13 | PASS | TABLE GUIDE section + bidirectional headers. |
| C-14 | PASS | AMEND Type 1 expands both tables; TOKEN RECALL in Option C sub-section maintains token contract in amended output. |
| C-15 | PASS | All 5 register-sensitive phases annotated at point-of-use. TOKEN RECALL at Phase 3 pairs with register branching for dual-layer annotation. |
| C-16 | PASS | Phase 1 print with dimension-level phase index. TOKEN RECALL at Phase 3 reproduces anchor values alongside register contract enforcement. |
| C-17 | PASS | TABLE GUIDE section + bidirectional headers. |
| C-18 | PASS | Phase 0 dedicated STATUS QUO ANCHOR with binding rule; TOKEN RECALL in Phases 3, 6, 7 makes Phase 0 commitment visible at every point-of-use. |

**Note**: TOKEN RECALL headers ("TOKEN RECALL: ANCHOR[0A] = {reproduce committed value from Phase 0}.") appear at Phase 3, 6, 7 -- the three phases with highest option-0 drift risk. Model must write the token value before producing anchor-sensitive output; any substitution becomes visibly wrong.

**Scores**: Essential 60.0 + Recommended 30.0 + Aspirational (10/10 x 10) 10.0 = **100.0**
**Golden**: YES (all 5 essential PASS, no PARTIAL)

---

## V-04: full-integration -- 100.0 / Golden

| ID | Score | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 3 all four dimensions for A and B. |
| C-02 | PASS | INERTIA RULE: bilateral independent check vs ANCHOR tokens. TOKEN RECALL at Phase 3 forces value reproduction before inertia dimension. Phase 10 audit item 4 verifies bilateral check. Three-layer enforcement: declaration binding + inline recall + terminal audit. |
| C-03 | PASS | Phase 4 (3-col) + Phase 5 (2-col); Phase 7 recommendation with TOKEN RECALL before output. |
| C-04 | PASS | Phase 7 traceability rule + TOKEN RECALL + Phase 10 audit item 9 (recommendation traceable, divergence reason explicit). Three-layer enforcement. |
| C-05 | PASS | Phase 6 GATE A with TOKEN RECALL + Phase 10 audit item 10 (GATE A check). Strongest "build neither" gate enforcement in R5. |
| C-06 | PASS | Phase 7 all registers include trade-off. |
| C-07 | PASS | ANTI-PATTERN GUARD with four concrete vectors and named failure phrases. |
| C-08 | PASS | Table 2 is 2-column scannable. Phase 10 audit items 5-6 verify both directional headers. |
| C-09 | PASS | Phase 9 handles all 3 AMEND types; TOKEN RECALL maintained in Option C AMEND Type 1 sub-sections. |
| C-10 | PASS | exec/engineering/general with per-phase, per-dimension contract. Phase 10 audit item 2 verifies dimension-level phase index printed. |
| C-11 | PASS | Table 1 3-column with labeled N/A cells; Option 0 header uses ANCHOR token names. Phase 10 audit item 5 verifies TABLE GUIDE present. |
| C-12 | PASS | ANTI-PATTERN GUARD named in Phase 3 competitive section. |
| C-13 | PASS | TABLE GUIDE section + bidirectional `[ -> ]` / `[ <- ]` headers. Phase 10 audit items 5-7 verify all three components. |
| C-14 | PASS | AMEND Type 1 expands both tables with TOKEN RECALL in Option C sub-section; Phase 10 audit covers structural coherence across both tables. |
| C-15 | PASS | All 5 register-sensitive phases annotated at point-of-use. TOKEN RECALL at Phase 3 adds parallel enforcement on top of register branching. Phase 10 audit item 3 verifies TOKEN RECALL at Phase 3 present. |
| C-16 | PASS | Phase 1 print with dimension-level phase index (strongest form, same as V-01/R4 canonical). Phase 10 audit item 2 verifies. |
| C-17 | PASS | TABLE GUIDE section + bidirectional headers. Phase 10 audit items 5-7 verify all three C-17 components: dedicated section, Phase 4 `[ -> ]`, Phase 5 `[ <- ]`. |
| C-18 | PASS | Phase 0 dedicated STATUS QUO ANCHOR with binding rule. TOKEN RECALL at Phases 3, 6, 7 makes Phase 0 commitment visible at all downstream anchor-sensitive points. Phase 10 audit item 1 verifies ANCHOR committed before Phase 1. |

**Note**: Full-integration combines all three R5 mechanisms simultaneously: token binding (V-01), inline TOKEN RECALL (V-03), terminal structural audit (V-02). Each guards a different failure mode: binding prevents silent prose substitution at declaration; recall catches drift at point-of-use; audit catches structural omissions above the token level. Non-overlapping guards; no criterion conflicts.

**Scores**: Essential 60.0 + Recommended 30.0 + Aspirational (10/10 x 10) 10.0 = **100.0**
**Golden**: YES (all 5 essential PASS, no PARTIAL)

---

## V-05: lean-anchor -- 95.0 / Golden

| ID | Score | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 2 covers all four dimensions for A and B independently. |
| C-02 | PASS | INERTIA RULE: "Option A: would teams keep using ANCHOR[0A] instead of building Option A? Name the specific mechanism." Both A and B independently grounded by token name -- stronger than V-05/R4 prose form. |
| C-03 | PASS | Phase 3 has Table 1 (3-col) and Table 2 (2-col); Phase 5 recommendation explicit. |
| C-04 | PASS | Phase 5: "Recommendation traceable to Table 2 -- do not assert a winner that contradicts the matrix signals without explicit justification. If the recommendation diverges from the matrix plurality, state the reason explicitly." |
| C-05 | PASS | Phase 4 GATE A: "INERTIA GATE: ANCHOR[0A] beats Option A and ANCHOR[0B] beats Option B. 'Build neither' is the leading recommendation." ANCHOR token names in gate language. |
| C-06 | PASS | Phase 5: "Recommendation, primary reason, trade-off (what is given up by not choosing the other option) in one paragraph." |
| C-07 | PASS | ANTI-PATTERN GUARD with four concrete vector types and "what ANCHOR[0A]/ANCHOR[0B] cannot do" framing. |
| C-08 | PASS | Table 2 is 2-column; "A reader should reach the recommendation from Table 2 without re-reading Phase 2." |
| C-09 | FAIL | No AMEND handler. Intentionally omitted for lean form. |
| C-10 | FAIL | No audience parameter. Intentionally omitted. |
| C-11 | PASS | Table 1 3-column A/B/Option 0 with labeled N/A cells. Option 0 header uses ANCHOR[0A]/ANCHOR[0B] token names. |
| C-12 | PASS | ANTI-PATTERN GUARD with named failure phrases in Phase 2 competitive section. |
| C-13 | PASS | "Which question are you answering?" block in Phase 3 before Table 1; Table 1 `[ -> See Table 2 below for A-vs-B decision summary. ]`; Table 2 `[ <- Source: Table 1 above; Option 0 column excluded. ]`. Bidirectional within single phase. |
| C-14 | N/A=0 | No AMEND handler; C-09 prerequisite fails. C-14 untestable. |
| C-15 | FAIL=0 | No audience register; no register-sensitive phases to annotate. Fails by design absence. |
| C-16 | FAIL=0 | No register declaration; no phase index to print. Fails by design absence. |
| C-17 | PASS | "Which question are you answering?" block (question-keyed, embedded at top of PHASE 3: MATRICES) appears before Table 1 with reader-intent routing; Table 1 and Table 2 headers carry bidirectional `[ -> ]` / `[ <- ]` annotations. Both C-17 components present. Embedded rather than separately-labeled section -- passes because routing block is dedicated to navigation and precedes the first matrix. |
| C-18 | PASS | `=== PHASE 0: STATUS QUO ANCHOR (Option 0) ===` is the first phase; commits ANCHOR[0A]/ANCHOR[0B] with binding rule before Phase 1 (Context), Phase 2 (Dimension Analysis), and all matrices. ANCHOR tokens used downstream -- stronger than V-05/R4's prose reference. |

**Aspirational pass**: C-11, C-12, C-13, C-17, C-18 = 5/10

**Scores**: Essential 60.0 + Recommended 30.0 + Aspirational (5/10 x 10) 5.0 = **95.0**
**Golden**: YES (all 5 essential PASS, no PARTIAL)

---

## Residual Gaps

**V-01 vs V-04**: V-01 has token binding but no inline TOKEN RECALL and no terminal audit. No scoring difference under v4. V-04 provides three-layer drift defense vs V-01's one layer.

**V-02 vs V-04**: V-02 adds terminal audit (9 items) but lacks inline TOKEN RECALL. V-04's Phase 10 includes TOKEN RECALL checks (item 3: "Phase 3 TOKEN RECALL present?"; items 8-9: "Phase 6/7 TOKEN RECALL reproduced correctly?") -- V-02 cannot self-verify TOKEN RECALL because it was never added. No scoring difference; V-04 more complete.

**V-03 vs V-04**: V-03 adds TOKEN RECALL at Phases 3, 6, 7 but lacks terminal audit. V-04 provides belt-and-suspenders. No scoring difference.

**V-05 intentional gaps**: C-09/C-10/C-14/C-15/C-16 = 0 by design. ANCHOR token binding added vs V-05/R4 (prose). A v6 criterion testing "ANCHOR token name appears by literal token syntax in 3+ downstream phases" would score 1 for lean-anchor and 0 for lean-prose -- the only distinguishing v6 candidate currently visible.

**Cross-round drift gap closed**: V-04/R4 was identified as using prose downstream references to Option 0. All R5 full variations now use ANCHOR[0A]/ANCHOR[0B] token syntax throughout -- binding at declaration, inline recall at point-of-use (V-03/V-04), terminal verification (V-02/V-04). The full drift lifecycle is now instrumented.

---

## Excellence Signals

**1. Three-layer drift defense architecture is the R5 canonical pattern** (V-04)
Token binding prevents silent prose substitution at Phase 0 declaration. Inline TOKEN RECALL catches substitution at point-of-use in Phases 3, 6, 7. Terminal structural audit catches omissions above the token level before the artifact is written. Three distinct failure modes; three non-overlapping guards. Each layer adds real value the other two cannot provide alone.

**2. Terminal audit creates a closed-loop contract** (V-02, V-04)
The audit checklist (9 items in V-02, 10 in V-04) verifies every structural criterion the rubric tests: Phase 0 commitment, register contract with phase index, bilateral inertia, TABLE GUIDE presence, bidirectional headers, ANCHOR token use in gate, recommendation traceability, "build neither" gate response. For models that follow the prompt structure but skip one item, the audit creates a correction opportunity before the artifact is written.

**3. Inline TOKEN RECALL makes commitment visible at every sensitive phase** (V-03, V-04)
Placing "TOKEN RECALL: ANCHOR[0A] = {reproduce committed value}" at the top of each anchor-sensitive phase (3, 6, 7) requires the model to write the exact committed value before producing output. If a model would write "the current approach" in Phase 6, the TOKEN RECALL header makes the substitution visible before gate logic runs. No equivalent mechanism exists for structural omissions -- only the terminal audit catches those.

**4. Lean floor stable at 95.0; token grounding is the only R5 change** (V-05)
V-05/R5 matches V-05/R4's 95.0 exactly. Token binding strengthens real-world drift resistance without changing any rubric criterion. The lean-prose vs lean-anchor distinction is invisible under v4 -- requires a v6 criterion. Lean form remains correct template for use cases without AMEND or audience routing.
