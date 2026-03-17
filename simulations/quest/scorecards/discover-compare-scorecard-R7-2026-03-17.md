# discover-compare — Scorecard R7

## Per-Variation Scoring

---

### V-01: audit-recall-parity

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | All four dimensions bilateral | **PASS** | Phase 3 covers feasibility, inertia, risk, competitive for both A and B independently |
| C-02 | Inertia bilateral and independent | **PASS** | INERTIA RULE explicit; Phase 3 checks A vs ANCHOR[0A] and B vs ANCHOR[0B] as separate questions |
| C-03 | Recommendation explicit and structured | **PASS** | Phase 7 named section with {A / B / neither / defer} choice |
| C-04 | Recommendation traceable to matrix | **PASS** | Phase 7: "traceable to Table 2 (Phase 5); if diverges from plurality, state reason explicitly" |
| C-05 | Build/no-build gate explicit | **PASS** | Phase 6 gate fires "build neither is the leading recommendation" if both verdicts = High |
| C-06 | Trade-offs in recommendation | **PASS** | Phase 7 all-registers block: "trade-off (what is given up by not choosing the other option)" |
| C-07 | Competitive position specific | **PASS** | Anti-pattern guard Phase 3 names generic phrases explicitly; four concrete vectors required |
| C-08 | Matrix scannable at a glance | **PASS** | Two-table architecture; TABLE GUIDE with question routing; Table 2 leads to recommendation |
| C-09 | AMEND path responsive | **PASS** | Phase 10: three AMEND types; Type 1 runs full dimension analysis + expands both tables; recommendation updates if evidence changes |
| C-10 | Audience register calibrated | **PASS** | Phase 1 exec/engineering/general with phase-level branching rules; all register-sensitive phases have conditional framing |
| C-11 | Inertia as Option 0 in matrix | **PASS** | Phase 4 Option 0 column with N/A labels; "this IS the anchor" cell explicit |
| C-12 | Anti-pattern guard explicit | **PASS** | Phase 3: "Generic competitive analysis uses phrases such as 'more competitive'... Such phrasing is insufficient" |
| C-13 | Two-table architecture | **PASS** | Table 1 (Phase 4, 3-col) and Table 2 (Phase 5, 2-col) with cross-references; structurally distinct |
| C-14 | AMEND expands both tables coherently | **PASS** | AMEND TYPE 1 steps 3–4 expand Table 1 to 4-col and Table 2 to 3-col with updated cross-references and cross-verification |
| C-15 | Register references at each affected phase | **PASS** | Phases 3, 4, 5, 7, 10 each carry explicit "Register: {applies from Phase 1 -- …}" branching |
| C-16 | Register declaration with upfront phase index | **PASS** | Phase 1 declares: "Phase 3 [risk, competitive], Phase 4 [cell emphasis], Phase 5 [cell emphasis], Phase 7 [lead structure], Phase 10 [framing]" — 5 phases listed |
| C-17 | TABLE GUIDE with bidirectional header annotations | **PASS** | TABLE GUIDE section present; Phase 4 header: "[ -> See Table 2 (Phase 5)… ]"; Phase 5 header: "[ <- Source: Table 1 (Phase 4)… ]" |
| C-18 | Option 0 defined as dedicated phase before analysis | **PASS** | Phase 0 defines ANCHOR[0A]/[0B] before any dimension analysis; all subsequent phases inherit baseline |
| C-19 | ANCHOR token binding rule declared at Phase 0 | **PASS** | Phase 0: "Binding rule: all phases must reference ANCHOR[0A] and ANCHOR[0B] by token name — not prose paraphrase. Print: 'Binding committed.'" |
| C-20 | TOKEN RECALL inline headers at each anchor-sensitive phase | **PASS** | Phases 3, 4, 5, 6, 7, 10 all open with TOKEN RECALL blocks; all 5 register-sensitive phases covered |
| C-21 | Terminal structural audit before artifact write | **PASS** | Phase 8: 14-item checklist; audit fires before Phase 9; failures corrected before artifact write |
| C-22 | Pre-artifact gate (audit fires before artifact write) | **PASS** | "Before writing the artifact in Phase 9, self-verify each item below. If any item fails, correct NOW — before proceeding to Phase 9." |
| C-23 | Bilateral verdict sentences with independence constraint | **PASS** | Phase 6: VERDICT A and VERDICT B as separate labeled sentences; "VERDICT A does not reference Option B. VERDICT B does not reference Option A." Audit item 10 verifies independence |
| C-24 | Audit checklist has one item per required TOKEN RECALL phase | **PASS** | 5 TOKEN RECALL audit items (items 3, 5, 8, 12, 14) matching 5 declared phases {3, 4, 5, 7, 10}. Count: 5/5. C-24 gap from R6 closed. |

**Essential:** 5/5 PASS (no PARTIAL)
**Recommended:** 3/3 PASS
**Aspirational:** 16/16 = 10.0

**Composite:** 60.0 + 30.0 + 10.0 = **100.0**
**Golden:** YES

---

### V-02: count-assertion-header

Identical to V-01 on all criteria. The RECALL COVERAGE COUNT block at audit header and updated print statement (`"RECALL COVERAGE: {count}/5"`) don't change criterion outcomes — they add at-a-glance verifiability within the already-passing C-24 framework.

One criterion worth noting:

| ID | Criterion | Score | Delta from V-01 |
|----|-----------|-------|----------------|
| C-24 | Audit checklist has one item per TOKEN RECALL phase | **PASS** | Count explicitly stated in audit header ("Required: 5. Present: items 3, 5, 8, 12, 14 (5/5)") — verifiable without counting |

All others: same as V-01.

**Essential:** 5/5 PASS | **Recommended:** 3/3 PASS | **Aspirational:** 16/16 = 10.0
**Composite:** **100.0** | **Golden:** YES

---

### V-03: recall-sequence-labels

All criteria same as V-01, with the following structural additions:

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-16 | Register declaration with upfront phase index | **PASS** | Phase 1 adds: "5 register-sensitive phases total: {3,4,5,7,10}. Each will carry a numbered TOKEN RECALL block: (1/5) through (5/5)." Print statement includes full sequence index. Strongest form of C-16. |
| C-20 | TOKEN RECALL inline headers at each anchor-sensitive phase | **PASS** | Phases 3–5 labeled (1/5)–(3/5); Phase 6 "anchor-sensitive"; Phase 7 (4/5); Phase 10 (5/5). Recall chain traceable by position label. |
| C-24 | Audit checklist has one item per TOKEN RECALL phase | **PASS** | 5 phase-specific recall items (items 3, 5, 8, 12, 14) + count-match item (15). "TOKEN RECALL sequence: labels (1/5) through (5/5) all present = 5/5." |

**Essential:** 5/5 PASS | **Recommended:** 3/3 PASS | **Aspirational:** 16/16 = 10.0
**Composite:** **100.0** | **Golden:** YES

---

### V-04: r7-canonical

Combination of V-01 + V-02 + V-03. 15-item audit. Strongest form of C-16, C-20, and C-24 simultaneously.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-16 | Register declaration with upfront phase index | **PASS** | Phase 1 lists all 5 phases + numbered sequence index "(1/5) at Phase 3 … (5/5) at Phase 10" in print statement |
| C-20 | TOKEN RECALL inline headers | **PASS** | (n/5) labels at all 5 register-sensitive phases; (anchor-sensitive) at Phase 6 |
| C-24 | Audit checklist count parity | **PASS** | RECALL COVERAGE COUNT header + 5 phase-specific items + count-match item. Three-layer contract: declare (Phase 1 index) → label (n/5) → assert (audit header count). |

All other criteria same as V-01: PASS across the board.

**Essential:** 5/5 PASS | **Recommended:** 3/3 PASS | **Aspirational:** 16/16 = 10.0
**Composite:** **100.0** | **Golden:** YES

---

### V-05: lean-c24-aware

Lean form (no audience register). R7 adds: (1) audit item 6 for recommendation traceability (C-21 PARTIAL → PASS), (2) explicit independence constraint language in verdict and audit (C-23 PARTIAL → PASS). C-24 remains N/A (C-20 is PARTIAL since C-15 fails).

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | All four dimensions bilateral | **PASS** | Phase 2 covers all four dimensions for A and B |
| C-02 | Inertia bilateral and independent | **PASS** | Phase 2 INERTIA RULE: separate questions per anchor |
| C-03 | Recommendation explicit and structured | **PASS** | Phase 6 named with {A/B/neither/defer} |
| C-04 | Recommendation traceable | **PASS** | Phase 6: "traceable to Table 2 (Phase 3); if diverges, state reason explicitly"; audit item 6 verifies |
| C-05 | Build/no-build gate | **PASS** | Phase 4 gate fires |
| C-06 | Trade-offs | **PASS** | Phase 6 includes trade-off sentence |
| C-07 | Competitive specific | **PASS** | Anti-pattern guard with four concrete vectors |
| C-08 | Matrix scannable | **PASS** | Two tables in Phase 3 with TABLE GUIDE and cross-reference arrows |
| C-09 | AMEND responsive | **FAIL** | No AMEND handler in lean form |
| C-10 | Audience register calibrated | **FAIL** | No audience register in lean form |
| C-11 | Option 0 in matrix | **PASS** | Table 1 has Option 0 column with N/A labels |
| C-12 | Anti-pattern guard | **PASS** | "Such phrasing is insufficient" present |
| C-13 | Two-table architecture | **PASS** | Table 1 (3-col) and Table 2 (2-col) with bidirectional cross-references in Phase 3 |
| C-14 | AMEND expands both tables | **FAIL** | No AMEND handler (two-table exists, so N/A condition doesn't apply → FAIL) |
| C-15 | Register references at each phase | **FAIL** | No register mechanism |
| C-16 | Register declaration with phase index | **FAIL** | No register section |
| C-17 | TABLE GUIDE with bidirectional headers | **PASS** | Phase 3 TABLE GUIDE question block + "[ -> See Table 2 ]" / "[ <- Source: Table 1 ]" on both table headers |
| C-18 | Option 0 as dedicated phase | **PASS** | Phase 0 defines ANCHOR[0A]/[0B] before any analysis |
| C-19 | ANCHOR binding rule at Phase 0 | **PASS** | Phase 0 binding rule with "not by prose paraphrase" and "Binding committed." print |
| C-20 | TOKEN RECALL at each anchor-sensitive phase | **PARTIAL** | TOKEN RECALL present in Phase 2 (inertia) and Phase 4 (verdict) but not structured under C-15 register-sensitive framework; no (n/N) labels; not every anchor-sensitive phase covered |
| C-21 | Terminal structural audit before artifact write | **PASS** | Phase 5 audit: 6 items covering all applicable minimums (items 1–7 from C-21 spec; item 2 "register contract" is N/A for lean form and absent by design). Item 6 (recommendation traceable) added in R7: PARTIAL → PASS |
| C-22 | Pre-artifact gate | **PASS** | "Before writing the recommendation (Phase 6) and the artifact (Phase 7), self-verify... correct NOW — before proceeding to Phase 6." |
| C-23 | Bilateral verdict sentences with independence constraint | **PASS** | Phase 4: "Independence constraint: VERDICT A does not reference Option B or ANCHOR[0B]. VERDICT B does not reference Option A or ANCHOR[0A]." Audit item 4 verifies. R7: PARTIAL → PASS |
| C-24 | Audit checklist count parity | **N/A (0)** | C-20 is PARTIAL → C-24 scores N/A per rubric |

**Aspirational tally:**
- PASS (1.0 each): C-11, C-12, C-13, C-17, C-18, C-19, C-21, C-22, C-23 = 9.0
- PARTIAL (0.5): C-20 = 0.5
- FAIL/N/A (0): C-09, C-10, C-14, C-15, C-16, C-24 = 0

Total aspirational: 9.5 / 16

**Essential:** 5/5 PASS (no PARTIAL)
**Recommended:** 3/3 PASS
**Aspirational:** 9.5/16 × 10 = 5.9375

**Composite:** 60.0 + 30.0 + 5.94 = **95.9**
**Golden:** YES (all essential PASS, no PARTIAL, composite ≥ 80)

---

## Summary and Ranking

| Rank | Variation | Composite | Golden | C-22 | C-23 | C-24 | Aspirational |
|------|-----------|-----------|--------|------|------|------|-------------|
| 1 (tied) | V-04 r7-canonical | **100.0** | YES | PASS | PASS | PASS | 16/16 |
| 1 (tied) | V-03 recall-sequence-labels | **100.0** | YES | PASS | PASS | PASS | 16/16 |
| 1 (tied) | V-02 count-assertion-header | **100.0** | YES | PASS | PASS | PASS | 16/16 |
| 1 (tied) | V-01 audit-recall-parity | **100.0** | YES | PASS | PASS | PASS | 16/16 |
| 5 | V-05 lean-c24-aware | **95.9** | YES | PASS | PASS | N/A | 9.5/16 |

All 5 variations are Golden. V-01 through V-04 reach 100.0 — the first perfect score in discover-compare history.

**Sub-ranking within the 100.0 group** (by C-24 verifiability architecture):
- **V-04** is the canonical form: three-layer contract (Phase 1 sequence index → (n/5) labels → count-assertion audit header)
- **V-02** is the strongest at-a-glance form: count header makes C-24 verifiable in one line
- **V-03** is the strongest trace form: (n/5) labels make each recall block locatable by position
- **V-01** is minimum viable: Phase 10 structural commitment item closes the gap with no other changes

---

## Excellence Signals (from V-04, top-scoring)

Three patterns elevated V-01–V-04 above V-04/R6 (which scored 99.7 with C-24 PARTIAL):

**1. Phase 10 structural commitment audit item**
The audit checks Phase 10 AMEND TOKEN RECALL as a *structural property of the prompt text* rather than a runtime execution state. The item reads: "verify that Phase 10 as written opens with TOKEN RECALL before any AMEND TYPE label. Runtime verified at invocation." This is the canonical way to audit a post-artifact phase from a pre-artifact audit position — architectural, not runtime.

**2. RECALL COVERAGE COUNT block at audit header**
A declaration at the top of the audit that names the required count, the item numbers where each recall check appears, and the verify condition: `{count} == 5 before proceeding`. This makes C-24 compliance verifiable in O(1) scan rather than O(n) item count. The count-assertion header pairs the C-16 forward index (which declares which phases require recall) with the audit (which verifies them) into a closed, two-pointer contract.

**3. Numbered (n/N) TOKEN RECALL sequence labels**
Labeling each TOKEN RECALL block as "(1/5 register-sensitive)" through "(5/5 register-sensitive)" gives each block a positional identity. An evaluator verifying C-20 coverage scans for five labels in sequence rather than searching for unlabeled occurrences. Phase 1 includes a sequence index mapping each label position to its phase number. This creates a traceable recall chain analogous to how C-19's binding rule makes anchor drift detectable.

**Structural observation:** These three mechanisms form a three-layer C-24 contract — `declare (Phase 1 sequence index) → label (n/5 blocks) → assert (audit count header)` — directly parallel to the three-layer anchor-drift defense established in earlier rounds: `declare (C-19 binding rule) → use (C-20 TOKEN RECALL) → verify (C-21 audit)`. The R7 patterns may be candidates for C-25/C-26 in a v8 rubric targeting RECALL COVERAGE COUNT header and numbered sequence label verifiability as independent aspirational properties.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["RECALL COVERAGE COUNT block at audit header — names required recall count and item positions; C-24 verifiable in one line without re-reading phases", "Numbered (n/N) TOKEN RECALL sequence labels — positional identity for each recall block; Phase 1 sequence index maps label to phase number; creates traceable recall chain parallel to anchor-drift defense", "Three-layer C-24 contract: declare (Phase 1 sequence index) -> label (n/N blocks) -> assert (audit count header) — mirrors C-19/C-20/C-21 structural pattern for a new dimension of verifiability"]}
```
