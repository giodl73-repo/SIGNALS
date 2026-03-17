## discover-compare Round 6 — Scoring Complete

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 (tie) | V-01 recall-full-coverage | **100.0** | YES |
| 1 (tie) | V-03 bilateral-verdict | **100.0** | YES |
| 1 (tie) | V-04 r6-canonical | **100.0** | YES |
| 4 | V-02 pre-artifact-gate | **99.2** | YES |
| 5 | V-05 lean-c20c21 | **95.4** | YES |

---

**Predicted vs actual:**
- V-01/V-03/V-04: predicted 100.0 — confirmed.
- V-02: predicted 100.0 — actual **99.2**. One miss: C-20 FAIL. V-02 intentionally preserved V-04/R5 TOKEN RECALL coverage (Phases 3, 6, 7) to isolate the position-change axis. Register-sensitive phases are {3, 4, 5, 7, 10} — only 2/5 have TOKEN RECALL. Pre-artifact gate wins C-21 architecturally but loses C-20.
- V-05: predicted ~95.0 — actual **95.4**. C-21 PARTIAL (not FAIL): the 5-item audit covers 5 of 6 applicable minimum items; missing only "recommendation traceable to matrix."

---

**What R6 closed:**
The gap was exact: V-04/R5 had TOKEN RECALL at anchor-sensitive phases 3, 6, 7 — but C-20 requires coverage of all 5 *register-sensitive* phases (3, 4, 5, 7, AMEND). V-01/V-03/V-04 add Phase 4, Phase 5, and AMEND opening recall, achieving full 5/5 coverage. Each new recall phase also gets a corresponding audit checklist item — making completeness verifiable.

**Three new R6 patterns (v7 rubric candidates):**
1. **Pre-artifact gate** — audit fires before artifact write; corrections don't require rewrite
2. **Bilateral verdict sentences with independence constraint** — VERDICT A / VERDICT B as observable separate output tokens; audit verifies no cross-reference
3. **Audit items per TOKEN RECALL phase** — closes the C-20/C-21 loop; each required recall phase has a verifiable audit item

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Pre-artifact gate: structural audit fires between recommendation and artifact write, so corrections happen before the file exists and the artifact always reflects corrected state without a rewrite step", "Bilateral verdict sentences with independence constraint: VERDICT A and VERDICT B as separate named output sentences each grounded only to its own ANCHOR token, with audit verifying no cross-reference between verdicts", "Audit checklist items per TOKEN RECALL phase: each phase required to have TOKEN RECALL gains a corresponding audit checklist item, closing the C-20/C-21 loop so recall completeness is verifiable before artifact write"]}
```
 matrix plurality, state the reason explicitly." Phase 10 audit item 11 verifies. |
| C-05 | PASS | Phase 6 GATE A: "INERTIA GATE: ANCHOR[0A] beats Option A and ANCHOR[0B] beats Option B. Teams will not build either option without a forcing function. 'Build neither' is the leading recommendation." Phase 10 audit item 12 verifies. |
| C-06 | PASS | Phase 7 all registers: trade-off clause present ("what is given up by not choosing the other option"). |
| C-07 | PASS | ANTI-PATTERN GUARD names four concrete vectors (Speed, Cost, Ecosystem, Capability) and explicitly states "Such phrasing is insufficient." |
| C-08 | PASS | TABLE GUIDE routes reader to correct table. Table 2 is 2-column; "Rating + one-phrase signal. No empty cells." |
| C-09 | PASS | Phase 9 AMEND handler covers all 3 types; Type 1 extends both tables with ANCHOR[0C]. |
| C-10 | PASS | exec/engineering/general with per-phase, per-dimension specificity at Phases 3, 4, 5, 7, 9. Phase 1 contract printed. |
| C-11 | PASS | Table 1 (Phase 4) is 3-column A/B/Option 0; N/A cells labeled; Option 0 column header uses ANCHOR token names. |
| C-12 | PASS | Phase 3 competitive: "Generic competitive analysis uses phrases such as 'more competitive,' 'better positioned,' or 'stronger in the market' without specifying the mechanism. Such phrasing is insufficient and will fail this criterion." |
| C-13 | PASS | TABLE GUIDE section with question-keyed routing before Phase 4. Phase 4 header: "[ -> See Table 2 (Phase 5) for A-vs-B decision summary ]". Phase 5 header: "[ <- Source: Table 1 (Phase 4); Option 0 column excluded. Use this table to reach the recommendation. ]". |
| C-14 | PASS | AMEND Type 1 expands Table 1 to 4-column and Table 2 to 3-column A/B/C; both headers updated with cross-references. |
| C-15 | PASS | Phase 3 risk: "Register: {applies from Phase 1 -- risk framing dimension}"; Phase 3 competitive: same; Phase 4: "Register: {applies from Phase 1 -- cell emphasis dimension}"; Phase 5: same; Phase 7: "Register: {applies from Phase 1 -- lead structure dimension}"; Phase 9 AMEND: "Register: apply Phase 1 contract [...]". All 5 register-sensitive phases annotated. |
| C-16 | PASS | Phase 1 print: "Contract: Phase 3 [risk, competitive], Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 9 [framing]." Forward index covers all 5 register-sensitive phases. |
| C-17 | PASS | Dedicated `=== TABLE GUIDE ===` section before Phase 4 with purpose statements. Phase 4 `[ -> ]` and Phase 5 `[ <- ]` provide bidirectional navigation. Both C-17 components present. |
| C-18 | PASS | `=== PHASE 0: STATUS QUO ANCHOR (Option 0) ===` is first phase; commits ANCHOR[0A]/ANCHOR[0B] with binding rule before any analysis. Excellence form of C-11. |
| C-19 | PASS | Phase 0 includes explicit binding rule: "any reference to 'the status quo,' 'current approach,' or 'doing nothing' without the token name violates this binding." Prints "Binding committed." Token + binding rule both present. Excellence form of C-18. |
| C-20 | PASS | TOKEN RECALL at Phase 3 (existing), Phase 4 (NEW), Phase 5 (NEW), Phase 6 (anchor-sensitive), Phase 7 (existing), Phase 9 AMEND opening (NEW). Full coverage of all 5 register-sensitive phases (3, 4, 5, 7, 9). Closes V-04/R5 gap. Phase 10 audit items 5 and 8 verify Phase 4 and Phase 5 TOKEN RECALL explicitly. |
| C-21 | PASS | Phase 10: "Before returning the output, self-verify each item below. If any item fails, correct the affected section first, then return the full corrected output." 12-item checklist covers all 7 minimum required items. "AUDIT COMPLETE -- {N}/12 checks passed." |

**Scores**: Essential 60.0 + Recommended 30.0 + Aspirational (13/13 x 10) 10.0 = **100.0**
**Golden**: YES (all 5 essential PASS, no PARTIAL)

---

## V-02: pre-artifact-gate -- 99.2 / Golden

| ID | Score | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 3 all four dimensions for A and B independently. |
| C-02 | PASS | Phase 3 INERTIA RULE bilateral; A vs ANCHOR[0A], B vs ANCHOR[0B] by token name. Phase 8 audit item 4 verifies bilateral check before artifact write. |
| C-03 | PASS | Phase 7 recommendation with explicit choice; Phases 4+5 tables lead it. |
| C-04 | PASS | Phase 7 traceability rule and divergence-reason requirement. Phase 8 audit item 9 verifies before artifact write. |
| C-05 | PASS | Phase 6 GATE A fires "build neither." Phase 8 audit item 10 verifies before artifact. |
| C-06 | PASS | Phase 7 all registers include trade-off clause. |
| C-07 | PASS | ANTI-PATTERN GUARD with four concrete vectors and named failure phrases. |
| C-08 | PASS | TABLE GUIDE + 2-column Table 2 with "Rating + one-phrase signal." |
| C-09 | PASS | Phase 10 AMEND handler covers all 3 types. |
| C-10 | PASS | exec/engineering/general at Phases 3, 4, 5, 7, 10. Phase 1 contract printed. |
| C-11 | PASS | Table 1 3-column with labeled N/A cells and ANCHOR token names in Option 0 header. |
| C-12 | PASS | ANTI-PATTERN GUARD with named failure phrases. |
| C-13 | PASS | TABLE GUIDE section + bidirectional `[ -> ]` / `[ <- ]` headers. Phase 8 audit items 6-7 verify both. |
| C-14 | PASS | Phase 10 AMEND Type 1 expands both tables coherently. |
| C-15 | PASS | All 5 register-sensitive phases (3, 4, 5, 7, 10) carry inline register annotations. |
| C-16 | PASS | Phase 1 print: "Contract: Phase 3 [risk, competitive], Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 10 [framing]." Phase 8 audit item 2 verifies. |
| C-17 | PASS | TABLE GUIDE section + bidirectional headers. Phase 8 audit items 5-7 verify all three components. |
| C-18 | PASS | Phase 0 dedicated STATUS QUO ANCHOR with binding rule before all analysis. |
| C-19 | PASS | Phase 0 binding rule with token reproduction requirement and "Binding committed." Excellence form of C-18. |
| C-20 | FAIL | V-02's design axis isolates the pre-artifact-gate position change, intentionally preserving V-04/R5 TOKEN RECALL coverage (Phases 3, 6, 7 only). Register-sensitive phases per C-16 contract: {3, 4, 5, 7, 10}. TOKEN RECALL present at Phase 3 and Phase 7 only (2/5). Phase 4: no TOKEN RECALL. Phase 5: no TOKEN RECALL. Phase 10 AMEND: no top-level TOKEN RECALL. C-20 requires all phases scored under C-15. FAIL. |
| C-21 | PASS | Phase 8 "STRUCTURAL AUDIT (pre-artifact gate)" fires BEFORE Phase 9 artifact write: "Before writing the artifact in Phase 9, self-verify each item below. If any item fails, correct the affected section NOW -- before proceeding to Phase 9. The artifact must reflect the corrected state, not the raw output." 10-item checklist covers all 7 minimum required items. "PRE-ARTIFACT AUDIT -- {N}/10 checks passed. Proceeding to artifact write." Architecturally strongest C-21 form: corrections happen before the file exists; no rewrite step required. |

**Note on architectural distinction**: V-02 C-21 is stronger than V-01 C-21 even though both score PASS. In V-01, a Phase 10 correction must also retroactively update the already-written Phase 8 artifact. In V-02, no file exists when the audit runs -- the correction determines what gets written. This distinction is a candidate for v7 C-22.

**Scores**: Essential 60.0 + Recommended 30.0 + Aspirational (12/13 x 10) 9.2 = **99.2**
**Golden**: YES (all 5 essential PASS, no PARTIAL)

---

## V-03: bilateral-verdict -- 100.0 / Golden

| ID | Score | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 3 all four dimensions for A and B independently. |
| C-02 | PASS | Phase 3 INERTIA RULE bilateral (structural). Phase 6 adds VERDICT A and VERDICT B as separate sentences: "Teams would [...] rather than [...] because {specific mechanism}." Constraint: "VERDICT A does not reference Option B. VERDICT B does not reference Option A." Phase 10 audit item 10 verifies independence. Bilateral independence is now an observable output trace. |
| C-03 | PASS | Phase 7 recommendation with explicit choice. |
| C-04 | PASS | Phase 7 traceability rule and divergence-reason requirement. Phase 10 audit item 12 verifies. |
| C-05 | PASS | Phase 6 gate derives from verdicts: "If VERDICT A = High AND VERDICT B = High: INERTIA GATE..." Gate reads from per-option verdicts, not raw ratings. Phase 10 audit item 13 verifies. |
| C-06 | PASS | Phase 7 all registers include trade-off clause. |
| C-07 | PASS | ANTI-PATTERN GUARD with four concrete vectors and named failure phrases. |
| C-08 | PASS | TABLE GUIDE + 2-column Table 2 scannable. |
| C-09 | PASS | Phase 9 AMEND handler covers all 3 types; Type 1 adds VERDICT C ("Issue VERDICT C: same bilateral verdict structure as Phase 6") -- verdict structure extends coherently through AMEND. |
| C-10 | PASS | exec/engineering/general at Phases 3, 4, 5, 7, 9. Phase 1 contract printed. |
| C-11 | PASS | Table 1 3-column with labeled N/A cells and ANCHOR token names. |
| C-12 | PASS | ANTI-PATTERN GUARD with named failure phrases. |
| C-13 | PASS | TABLE GUIDE section + bidirectional `[ -> ]` / `[ <- ]` headers. |
| C-14 | PASS | Phase 9 AMEND Type 1 expands both tables and adds VERDICT C; Phase 6 re-run covers all three options. Both tables updated coherently. |
| C-15 | PASS | All 5 register-sensitive phases (3, 4, 5, 7, 9) annotated at point-of-use. |
| C-16 | PASS | Phase 1 print with forward phase index for all 5 sensitive phases. |
| C-17 | PASS | Dedicated TABLE GUIDE section + bidirectional headers. Phase 10 audit item 6 verifies TABLE GUIDE present. |
| C-18 | PASS | Phase 0 dedicated STATUS QUO ANCHOR with binding rule before all analysis. |
| C-19 | PASS | Phase 0 binding rule with token reproduction requirement and "Binding committed." Excellence form of C-18. |
| C-20 | PASS | TOKEN RECALL at Phase 3 (existing), Phase 4 (NEW), Phase 5 (NEW), Phase 6 (anchor-sensitive), Phase 7 (existing), Phase 9 AMEND opening (NEW). Full 5/5 register-sensitive phase coverage. Phase 10 audit items 5 and 8 verify Phase 4 and Phase 5 TOKEN RECALL. |
| C-21 | PASS | Phase 10: "Before returning the output, self-verify each item below. If any item fails, correct the affected section first, then return the full corrected output." 13-item checklist includes all 7 minimum required items plus bilateral verdict check (new). "AUDIT COMPLETE -- {N}/13 checks passed." |

**Note**: V-03's defining contribution: C-02 becomes an observable output trace. Prior variations passed C-02 via structural guarantees (INERTIA RULE wording). V-03 produces VERDICT A and VERDICT B as separate named sentences, each grounded only to its own ANCHOR. If a model conflates the verdicts, the failure is visible in the output and the audit catches it.

**Scores**: Essential 60.0 + Recommended 30.0 + Aspirational (13/13 x 10) 10.0 = **100.0**
**Golden**: YES (all 5 essential PASS, no PARTIAL)

---

## V-04: r6-canonical -- 100.0 / Golden

| ID | Score | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 3 all four dimensions for A and B independently. |
| C-02 | PASS | Three-layer enforcement: Phase 3 INERTIA RULE bilateral (structural guarantee) + Phase 6 VERDICT A/VERDICT B sentences independently grounded (observable trace) + Phase 8 audit item 10 verifies independence before artifact write. Declaration -> trace -> pre-write verification. |
| C-03 | PASS | Phase 7 recommendation with explicit choice. |
| C-04 | PASS | Phase 7 traceability rule. Phase 8 audit item 12 verifies before artifact write. |
| C-05 | PASS | Phase 6 gate derives from bilateral verdicts. Phase 8 audit item 13 verifies "build neither" before artifact write. |
| C-06 | PASS | Phase 7 all registers include trade-off clause. |
| C-07 | PASS | ANTI-PATTERN GUARD with four concrete vectors and named failure phrases. |
| C-08 | PASS | TABLE GUIDE + 2-column Table 2. Phase 8 audit items 6-9 verify navigation structure before artifact write. |
| C-09 | PASS | Phase 10 AMEND handler covers all 3 types; Type 1 adds VERDICT C; Phase 6 re-run covers all three options. |
| C-10 | PASS | exec/engineering/general at Phases 3, 4, 5, 7, 10. Phase 1 contract printed. |
| C-11 | PASS | Table 1 3-column with labeled N/A cells; ANCHOR token names in Option 0 header and verdict language. |
| C-12 | PASS | ANTI-PATTERN GUARD with named failure phrases. |
| C-13 | PASS | TABLE GUIDE section + bidirectional `[ -> ]` / `[ <- ]` headers. Phase 8 audit items 6-9 verify all navigation components before artifact write. |
| C-14 | PASS | Phase 10 AMEND Type 1 expands both tables with VERDICT C; Phase 6 re-run for all three options. Both tables updated coherently. |
| C-15 | PASS | All 5 register-sensitive phases (3, 4, 5, 7, 10) annotated at point-of-use. |
| C-16 | PASS | Phase 1 print: "Contract: Phase 3 [risk, competitive], Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 10 [framing]." Phase 8 audit item 2 verifies before artifact write. |
| C-17 | PASS | TABLE GUIDE section + bidirectional headers. Phase 8 audit items 6-9 verify all three C-17 components before artifact write. |
| C-18 | PASS | Phase 0 dedicated STATUS QUO ANCHOR with binding rule. ANCHOR tokens appear in verdicts (Phase 6), gate language, recommendation (Phase 7). |
| C-19 | PASS | Phase 0 binding rule with token reproduction requirement and "Binding committed." Phase 8 audit item 1 verifies. Excellence form of C-18. |
| C-20 | PASS | TOKEN RECALL at Phase 3 (existing), Phase 4 (V-01), Phase 5 (V-01), Phase 6 (anchor-sensitive), Phase 7 (existing), Phase 10 AMEND opening (V-01). Full 5/5 register-sensitive phase coverage. Phase 8 audit items 5 and 8 verify Phase 4 and Phase 5 TOKEN RECALL before artifact write. |
| C-21 | PASS | Phase 8 "STRUCTURAL AUDIT (pre-artifact gate)" fires BEFORE Phase 9 artifact write. 13-item checklist (V-01's 12 items + bilateral verdict check from V-03). All 7 minimum required items present. "PRE-ARTIFACT AUDIT -- {N}/13 checks passed. Proceeding to artifact write." Closed-loop contract: declare (C-19) -> use (C-20) -> verify (C-21) -- all three layers verified before file write. Strongest C-21 form. |

**Note**: V-04 combines all three R6 axes independently and non-overlappingly. Full recall (V-01) closes C-20. Pre-artifact gate (V-02) is architecturally strongest C-21. Bilateral verdict (V-03) makes C-02 observable. Three-layer drift defense: token binding prevents silent substitution at declaration; inline recall catches drift at point-of-use; pre-write audit catches structural omissions before the artifact exists. The artifact always reflects the corrected state.

**Scores**: Essential 60.0 + Recommended 30.0 + Aspirational (13/13 x 10) 10.0 = **100.0**
**Golden**: YES (all 5 essential PASS, no PARTIAL)

---

## V-05: lean-c20c21 -- 95.4 / Golden

| ID | Score | Evidence |
|----|-------|---------|
| C-01 | PASS | Phase 2 covers all four dimensions for A and B independently. |
| C-02 | PASS | Phase 2 INERTIA RULE bilateral. Phase 4 adds VERDICT A/VERDICT B independently grounded. Phase 5 audit item 2 verifies bilateral inertia check before recommendation. |
| C-03 | PASS | Phase 6 recommendation with explicit choice {A, B, neither, defer}. |
| C-04 | PASS | Phase 6: "Recommendation traceable to Table 2 (Phase 3) -- do not assert a winner that contradicts the matrix signals without explicit justification. If the recommendation diverges from the matrix plurality, state the reason explicitly." |
| C-05 | PASS | Phase 4 GATE: "If VERDICT A = High AND VERDICT B = High: INERTIA GATE: ANCHOR[0A] beats Option A. ANCHOR[0B] beats Option B. 'Build neither' is the leading recommendation." Phase 5 audit item 5 verifies. |
| C-06 | PASS | Phase 6: "trade-off (what is given up by not choosing the other option) in one paragraph." |
| C-07 | PASS | ANTI-PATTERN GUARD with four concrete vectors in Phase 2. |
| C-08 | PASS | Question-routing before Table 1 in Phase 3; Table 2 is 2-column with "Rating + one-phrase signal." |
| C-09 | FAIL | No AMEND handler. Intentionally omitted for lean form. |
| C-10 | FAIL | No audience parameter / register. Intentionally omitted. |
| C-11 | PASS | Table 1 (Phase 3) is 3-column A/B/Option 0 with labeled N/A cells and ANCHOR token names in Option 0 header. |
| C-12 | PASS | ANTI-PATTERN GUARD with named failure phrases in Phase 2 competitive section. |
| C-13 | PASS | Question-routing block before Table 1 in Phase 3 with purpose statements; Table 1 `[ -> See Table 2 below... ]`; Table 2 `[ <- Source: Table 1 above; Option 0 column excluded. ]`. Bidirectional cross-references present. |
| C-14 | N/A=0 | No AMEND handler; C-09 fails. C-14 untestable. |
| C-15 | FAIL=0 | No audience register; no register-sensitive phases. Fails by design absence. |
| C-16 | FAIL=0 | No register declaration; no phase index. Fails by design absence. |
| C-17 | PASS | "Which question are you answering?" block at top of Phase 3 before Table 1 is dedicated to navigation and names each table's purpose; bidirectional `[ -> ]` / `[ <- ]` headers on both tables. Both C-17 components satisfied. Consistent with R5 scoring of V-05/R5. |
| C-18 | PASS | Phase 0 "STATUS QUO ANCHOR (Option 0)" is first phase; commits ANCHOR[0A]/ANCHOR[0B] with binding rule before Phase 1 (Context) and Phase 2 (Dimension Analysis). |
| C-19 | PASS | Phase 0 includes binding rule requiring token-name reference; prints "Binding committed." Excellence form of C-18. |
| C-20 | PARTIAL | TOKEN RECALL present at Phase 2 inertia sub-section and Phase 4 verdict-and-gate -- the two anchor-sensitive phases in the lean form. However, C-20 pass condition requires TOKEN RECALL at "every phase scored under C-15 (all register-sensitive phases)." V-05 has no register-sensitive phases (C-15 N/A); recall coverage is anchor-sensitive only. PARTIAL: mechanism is correct, scope differs from full-form. |
| C-21 | PARTIAL | Phase 5 "STRUCTURAL AUDIT (pre-recommendation gate)" fires before Phase 6 and Phase 7. 5-item checklist covers 5 of 6 applicable minimum items: anchors committed (item 1), bilateral inertia (item 2), tables + cross-refs (item 3), verdicts + TOKEN RECALL at Phase 4 (item 4), build-neither gate (item 5). Missing minimum item: recommendation traceable to matrix. Phase 6 itself instructs traceability but the audit does not verify it. PARTIAL. |

**Aspirational pass**: C-11 (1) + C-12 (1) + C-13 (1) + C-17 (1) + C-18 (1) + C-19 (1) + C-20 (0.5) + C-21 (0.5) = 7.0/13

**Scores**: Essential 60.0 + Recommended 30.0 + Aspirational (7.0/13 x 10) 5.4 = **95.4**
**Golden**: YES (all 5 essential PASS, no PARTIAL)

---

## Residual Gaps

**V-02 vs V-04**: V-02 wins on C-21 architecture (pre-artifact gate; corrections before file exists) but loses C-20 (2/5 register-sensitive recall; intentional isolation). For production use, V-04 is strictly superior: it has the pre-artifact gate AND full recall coverage.

**V-01 vs V-04**: V-01 has full recall (C-20 PASS) and terminal audit (C-21 PASS) but audit fires after artifact write (Phase 10). V-04 fires before artifact write (Phase 8). Both score C-21 PASS -- the architectural distinction is not captured in v5 but is a v7 C-22 candidate.

**V-03 vs V-04**: V-03 has bilateral verdicts and full recall but post-artifact audit. V-04 adds pre-artifact gate. V-04 preferred.

**V-05 R7 path to 95.8**: Adding "recommendation traceable to Table 2" as audit item 6 would promote C-21 from PARTIAL to PASS (+0.5 -> 7.5/13 = 5.77 aspirational = total ~95.8).

**Pre-artifact gate is not yet a separable criterion**: Both V-02 and V-01 score C-21 PASS despite the architectural difference. v7 C-22 candidate: "Audit fires before artifact write (not merely before return to user)." Would score PASS for V-02/V-04, FAIL for V-01/V-03.

---

## Excellence Signals

**1. Full TOKEN RECALL coverage closes C-20 cleanly (V-01, V-03, V-04)**
The R6 gap was precise: V-04/R5 had TOKEN RECALL at Phases 3, 6, 7 (anchor-sensitive) but not all register-sensitive phases (3, 4, 5, 7, 9 or 10). Adding TOKEN RECALL at Phase 4, Phase 5, and the AMEND phase opening achieves 5/5 register-sensitive coverage. The audit must also gain items for each new recall phase -- V-01's audit adds "Phase 4 TOKEN RECALL (NEW)" and "Phase 5 TOKEN RECALL (NEW)" as explicit items, making recall completeness verifiable. Pattern: every TOKEN RECALL phase added should have a corresponding audit item.

**2. Bilateral verdict structure makes C-02 an observable output trace (V-03, V-04)**
Prior variations passed C-02 via structural guarantees (INERTIA RULE wording forced independent checking). V-03/V-04 produce VERDICT A and VERDICT B as separate named sentences grounded to their own ANCHOR only. "VERDICT A does not reference Option B" is enforced in the prompt and verified in the audit. If a model conflates the verdicts, the failure is visible. The pattern: observable per-option traces + audit independence check is stronger than structural-only enforcement.

**3. Pre-artifact audit gate: corrections before the file exists (V-02, V-04)**
Placing the structural audit between the recommendation phase and the artifact write means: corrections happen before any file is created; the artifact always reflects the corrected state; no retroactive rewrite required. V-01/V-03 require the Phase 10 audit to update an already-written Phase 8 artifact. V-02/V-04 eliminate this by making the artifact the terminal output of a pre-verified state. Pattern: audit as pre-write gate rather than post-write verification.

---

## Three New R6 Patterns (Candidates for v7 rubric)

| # | Pattern | Source | What it tests |
|---|---------|--------|---------------|
| P-01 | Pre-artifact gate: audit fires between recommendation and artifact write | V-02, V-04 | C-21 sub-distinction: pre-write vs pre-return. Corrections don't require artifact rewrite. |
| P-02 | Per-option bilateral verdict sentences with independence constraint | V-03, V-04 | Observable C-02 trace: VERDICT A and VERDICT B as separate output tokens, each grounded only to its own ANCHOR. Audit verifies no cross-reference. |
| P-03 | Audit checklist items per TOKEN RECALL phase | V-01, V-03, V-04 | C-20/C-21 closed loop: every phase required to have TOKEN RECALL has a corresponding audit checklist item. Detects any recall omission before artifact write. |

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Pre-artifact gate: structural audit fires between recommendation and artifact write, so corrections happen before the file exists and the artifact always reflects corrected state without a rewrite step", "Bilateral verdict sentences with independence constraint: VERDICT A and VERDICT B as separate named output sentences each grounded only to its own ANCHOR token, with audit verifying no cross-reference between verdicts", "Audit checklist items per TOKEN RECALL phase: each phase required to have TOKEN RECALL gains a corresponding audit checklist item, closing the C-20/C-21 loop so recall completeness is verifiable before artifact write"]}
```
