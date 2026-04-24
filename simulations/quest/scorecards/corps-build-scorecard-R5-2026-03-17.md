# corps-build — Quest Score R5 (Rubric v3)

**Note on rubric/variate mismatch**: The golden file (`rubric_version: 5`) targets criteria C-09 through C-20, while the provided rubric is v3 (C-01 through C-15). The variations were architected for CONTRACT-SEAL / TRANSCRIPTION-RECEIPT / BUILD-VERIFY-SINGLE-PURPOSE mechanisms — v5 patterns — and do **not** implement v3's INV-N invariant block (C-11), FAILURE MODES pre-step (C-14), or CHECK-OUTPUT PROTOCOL section (C-15). This mismatch drives the scoring uniformly down.

---

## V-01 — Lifecycle: BUILD-VERIFY single-purpose phase

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Role file completeness | **PASS** (12) | TABLE-CLOSED + CROSS-REF `files written: [n] -- MATCH / MISMATCH`; verification mechanism present |
| C-02 | org-chart.md ASCII hierarchy | **PASS** (12) | Phase 7: box-drawing, min 2 nesting levels, verbatim names, headcount in parens |
| C-03 | IA in every team | **PASS** (12) | WRITE-IA phase; per-team IA-WRITTEN gate with YES/NO rewrite loop; IA-PHASE-COMPLETE + CROSS-REF IA check |
| C-04 | org.yaml structural fidelity | **PARTIAL** (6) | Path pattern stated (area-slug from org.yaml) but no explicit "validate path against org.yaml before writing" statement |
| C-05 | Role file typed fields | **PARTIAL** (6) | Uses orientation/lens/expertise/scope/collaboration — not title/role-type/area/lens/expertise; two fields match, three differ |
| C-06 | Headcount table + levels | **PARTIAL** (5) | ARTIFACT-A has Area/Group + Headcount + Standard + Specialized + Levels — missing IA count column |
| C-07 | Standard vs specialized | **PARTIAL** (5) | IA-first paradigm (WRITE-IA before WRITE-ROLES) inverts the C-07 sequence; role-type not in frontmatter |
| C-08 | AMEND with three options | **PASS** (10) | --area (resistance profile + IA + roles + chart row), --levels, --restructure; all three options present |
| C-09 | IA team-contextualized | **PASS** (5) | PROFILE phase: defended-artifact + change-pressure + lens-phrase per team; "no generic stability language" |
| C-10 | Cross-reference integrity | **PASS** (5) | CROSS-REF emits `[n], files written: [n] -- MATCH / MISMATCH` and `IA files: [n of n] -- MATCH / MISMATCH` |
| C-11 | Named invariant block | **FAIL** (0) | Phase gates used (PARSE-PASS, VALIDATE-PASS etc.) but no INV-N declarations before steps |
| C-12 | Auditable check-output | **PASS** (5) | PARSE-PASS/FAIL, VALIDATE-PASS/FAIL, BUILD-VERIFY VERBATIM/DRIFT, CROSS-REF MATCH/MISMATCH — all emitted |
| C-13 | Named failure modes per aspirational | **FAIL** (0) | No FM-N section naming violation examples for C-09/C-10/C-11/C-12 |
| C-14 | Dedicated FAILURE MODES pre-step | **FAIL** (0) | No dedicated named FAILURE MODES block before Step 1 |
| C-15 | Named CHECK-OUTPUT PROTOCOL | **FAIL** (0) | No named protocol section; audit strings scattered inline as phase output, not a first-class section |

**V-01 Composite: 83 / 125** | Essential all-PASS: No (C-04 PARTIAL, C-05 PARTIAL)

---

## V-02 — Output format: TRANSCRIPTION-RECEIPT with phase-exit guard

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Role file completeness | **PASS** (12) | ROLES-COMPLETE + CROSS-REF MATCH/MISMATCH |
| C-02 | org-chart.md ASCII hierarchy | **PASS** (12) | Phase 6b: box-drawing, minimum two nesting levels |
| C-03 | IA in every team | **PASS** (12) | Phase 6a IA-first; per-team IA-WRITTEN gate with YES/NO rewrite; IA-PHASE-COMPLETE |
| C-04 | org.yaml structural fidelity | **PARTIAL** (6) | Path pattern given, no explicit pre-write path validation statement |
| C-05 | Role file typed fields | **PARTIAL** (6) | Phase 6a/6c: orientation/lens/expertise/scope/collaboration — not title/role-type/area/lens/expertise |
| C-06 | Headcount table + levels | **PARTIAL** (5) | ARTIFACT-A: Area/Group + Headcount + Standard + Specialized + Levels — no IA count column |
| C-07 | Standard vs specialized | **PARTIAL** (5) | IA-first write order (Phase 6a before 6c); no role-type frontmatter field |
| C-08 | AMEND with three options | **PASS** (10) | Phase 6b: --area, --levels, --restructure with specific values from org.yaml |
| C-09 | IA team-contextualized | **PASS** (5) | Phase 5 PROFILE: specific named artifact + specific named initiative; "not a generic force" |
| C-10 | Cross-reference integrity | **PASS** (5) | CROSS-REF: `org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH` emitted |
| C-11 | Named invariant block | **FAIL** (0) | No INV-N block at entry point |
| C-12 | Auditable check-output | **PASS** (5) | TRANSCRIPTION-RECEIPT: VERBATIM/REVISED per artifact; CROSS-REF: MATCH/MISMATCH |
| C-13 | Named failure modes per aspirational | **FAIL** (0) | No section naming violation examples for C-09/C-10/C-11/C-12 |
| C-14 | Dedicated FAILURE MODES pre-step | **FAIL** (0) | No dedicated FAILURE MODES block |
| C-15 | Named CHECK-OUTPUT PROTOCOL | **FAIL** (0) | TRANSCRIPTION-RECEIPT is a named output block but not a CHECK-OUTPUT PROTOCOL section with enumerated rules |

**V-02 Composite: 83 / 125** | Essential all-PASS: No (C-04 PARTIAL, C-05 PARTIAL)

---

## V-03 — Phrasing register: declarative output-forward

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Role file completeness | **PASS** (12) | CROSS-REF: `org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH` |
| C-02 | org-chart.md ASCII hierarchy | **PASS** (12) | Stage 6b: box-drawing, minimum two nesting levels; "group names match org.yaml exactly" |
| C-03 | IA in every team | **PASS** (12) | Stage 6: IA before standard; per-team IA-WRITTEN YES/NO gate; IA-COMPLETE |
| C-04 | org.yaml structural fidelity | **PARTIAL** (6) | Path stated; no pre-write validation statement |
| C-05 | Role file typed fields | **PARTIAL** (6) | Stage 6: five fields with quality bars but orientation/lens/expertise/scope/collaboration |
| C-06 | Headcount table + levels | **PARTIAL** (5) | ARTIFACT-A described by token count only in Stage 3; column structure not explicitly enumerated |
| C-07 | Standard vs specialized | **PARTIAL** (5) | Stage 7 "standard and specialized role files" after IA; no role-type frontmatter |
| C-08 | AMEND with three options | **PARTIAL** (5) | Stage 6b names AMEND as a section but does not describe the three repair options |
| C-09 | IA team-contextualized | **PASS** (5) | Stage 5: "A correct lens-phrase cannot be produced without knowing both defended-artifact and change-pressure" |
| C-10 | Cross-reference integrity | **PASS** (5) | Stage 9 CROSS-REF: `org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH` |
| C-11 | Named invariant block | **FAIL** (0) | No INV-N block |
| C-12 | Auditable check-output | **PASS** (5) | BUILD-VERIFY-PASS, CROSS-REF MATCH/MISMATCH emitted; VALIDATE names anomalies |
| C-13 | Named failure modes per aspirational | **FAIL** (0) | No FAILURE MODES section |
| C-14 | Dedicated FAILURE MODES pre-step | **FAIL** (0) | Declarative framing names wrong-output shapes inline (weak/strong examples), not a dedicated named block |
| C-15 | Named CHECK-OUTPUT PROTOCOL | **FAIL** (0) | No named CHECK-OUTPUT PROTOCOL section |

**V-03 Composite: 78 / 125** | Essential all-PASS: No | C-08 PARTIAL is the distinguishing gap vs. V-01/V-02/V-04/V-05

---

## V-04 — Combination: C-19 + C-20 together

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Role file completeness | **PASS** (12) | CROSS-REF MATCH/MISMATCH + ROLES-COMPLETE |
| C-02 | org-chart.md ASCII hierarchy | **PASS** (12) | STEP 7: ASCII hierarchy, minimum two nesting levels |
| C-03 | IA in every team | **PASS** (12) | STEP 6 WRITE-IA all before standard; IA-WRITTEN per-team YES/NO gate; IA-PHASE-COMPLETE |
| C-04 | org.yaml structural fidelity | **PARTIAL** (6) | Path pattern given; no explicit pre-write validation against org.yaml |
| C-05 | Role file typed fields | **PARTIAL** (6) | STEP 6/8: orientation/lens/expertise/scope/collaboration — not C-05 field names |
| C-06 | Headcount table + levels | **PARTIAL** (5) | ARTIFACT-A: Area/Group + Headcount + Standard + Specialized + Levels — no IA count |
| C-07 | Standard vs specialized | **PARTIAL** (5) | IA-first write order; no role-type frontmatter |
| C-08 | AMEND with three options | **PASS** (10) | STEP 7: --area, --levels, --restructure with specific available values |
| C-09 | IA team-contextualized | **PASS** (5) | STEP 5 PROFILE: specific defended-artifact + change-pressure; lens-phrase "cannot be written without knowing both fields" |
| C-10 | Cross-reference integrity | **PASS** (5) | STEP 10 CROSS-REF: `org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH` |
| C-11 | Named invariant block | **FAIL** (0) | No INV-N block |
| C-12 | Auditable check-output | **PASS** (5) | VALIDATE PASS/FAIL, TRANSCRIPTION-RECEIPT VERBATIM/REVISED, CROSS-REF MATCH/MISMATCH |
| C-13 | Named failure modes per aspirational | **FAIL** (0) | No failure mode section for C-09/C-10/C-11/C-12 |
| C-14 | Dedicated FAILURE MODES pre-step | **FAIL** (0) | No dedicated FAILURE MODES block |
| C-15 | Named CHECK-OUTPUT PROTOCOL | **FAIL** (0) | TRANSCRIPTION-RECEIPT + BUILD-VERIFY are output blocks, not a named CHECK-OUTPUT PROTOCOL with rules |

**V-04 Composite: 83 / 125** | Essential all-PASS: No (C-04 PARTIAL, C-05 PARTIAL)

---

## V-05 — Full integration: all 12 aspirational criteria C-09 through C-20

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Role file completeness | **PASS** (12) | TABLE-CLOSED: "File generation must produce exactly [n] .roles/ files" + CROSS-REF MATCH/MISMATCH |
| C-02 | org-chart.md ASCII hierarchy | **PASS** (12) | PHASE 8: box-drawing, min 2 nesting, verbatim names, headcount in parens |
| C-03 | IA in every team | **PASS** (12) | "IA omission is structurally impossible: an unstarted IA file means the team's entire role set has not begun"; per-team IA-WRITTEN gate; IA-PHASE-COMPLETE |
| C-04 | org.yaml structural fidelity | **PARTIAL** (6) | Paths are org.yaml-derived; no explicit pre-write path validation statement |
| C-05 | Role file typed fields | **PARTIAL** (6) | PHASE 6/7: orientation/lens/expertise/scope/collaboration with strong/weak examples; field names don't match title/role-type/area/lens/expertise |
| C-06 | Headcount table + levels | **PARTIAL** (5) | ARTIFACT-A: Area/Group + Headcount + Standard + Specialized + Levels — no IA count column |
| C-07 | Standard vs specialized | **PARTIAL** (5) | IA-first (WRITE-IA phase before WRITE-ROLES); no role-type frontmatter |
| C-08 | AMEND with three options | **PASS** (10) | PHASE 8: --area (resistance profile + IA + roles + chart row), --levels, --restructure with org.yaml values |
| C-09 | IA team-contextualized | **PASS** (5) | Strong/weak examples for lens; "specific tension, not the general concept"; lens-phrase from PROFILE cannot be generic |
| C-10 | Cross-reference integrity | **PASS** (5) | CROSS-REF: `org.yaml slots: [n], files written: [n] -- MATCH / MISMATCH` emitted |
| C-11 | Named invariant block | **FAIL** (0) | Phase gate architecture (PARSE-PASS, VALIDATE-PASS) used instead of INV-N block |
| C-12 | Auditable check-output | **PASS** (5) | TRANSCRIPTION-RECEIPT VERBATIM/REVISED per artifact; BUILD-VERIFY VERBATIM/DRIFT; CROSS-REF MATCH/MISMATCH |
| C-13 | Named failure modes per aspirational | **FAIL** (0) | No FAILURE MODES section naming violation patterns for C-09/C-10/C-11/C-12 |
| C-14 | Dedicated FAILURE MODES pre-step | **FAIL** (0) | No dedicated named FAILURE MODES block before Phase 1 |
| C-15 | Named CHECK-OUTPUT PROTOCOL | **FAIL** (0) | TRANSCRIPTION-RECEIPT and BUILD-VERIFY are inline phase blocks; no named protocol section with enumerated rules |

**V-05 Composite: 83 / 125** | Essential all-PASS: No (C-04 PARTIAL, C-05 PARTIAL)

---

## Rankings

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | V-01 | 83 | PROFILE pipeline + BUILD-VERIFY SINGLE-PURPOSE GATE |
| 1 | V-02 | 83 | TRANSCRIPTION-RECEIPT + PHASE-EXIT GUARD (strongest C-19 coverage) |
| 1 | V-04 | 83 | C-19 + C-20 combined; both mechanisms present without redundancy |
| 1 | V-05 | 83 | Full architecture; strongest C-03 framing ("omission structurally impossible") |
| 5 | V-03 | 78 | C-08 PARTIAL (AMEND section underdescribed) drops it below the four-way tie |

**Threshold**: Golden requires all 5 essential PASS + composite ≥ 103. No variation reaches this. Root cause: all 5 variations systematically miss C-11 (INV-N block), C-13 (named failure modes for aspirational criteria), C-14 (dedicated FAILURE MODES pre-step), and C-15 (CHECK-OUTPUT PROTOCOL section) — exactly the rubric v3 structural requirements that distinguish it from the v5 criteria these variations were architected to satisfy.

---

## Excellence Signals (V-05 as representative top scorer)

**Signal 1 — Resistance profile as IA derivation contract**: The PROFILE phase computes `defended-artifact + change-pressure → lens-phrase` per team before any file is written. The lens-phrase is both the IA file's opening text (verbatim) and the BUILD-VERIFY comparison anchor. This creates a closed loop: profile → write → verify all reference the same token. Generic IA is structurally prevented because the lens-phrase cannot be produced without knowing both specific fields.

**Signal 2 — TRANSCRIPTION-CLEAR phase-exit guard**: After TRANSCRIPTION-RECEIPT, a distinct TRANSCRIPTION-CLEAR step re-audits all three artifact verdicts before CHART-WRITTEN is authorized. CHART-WRITTEN is contingent on TRANSCRIPTION-CLEAR, not on the receipt itself. This means the phase cannot exit in REVISED state — any REVISED verdict triggers rewrite and a receipt line update before the guard runs again. The guard is the enforcement; the receipt is the audit trail.

**Signal 3 — SINGLE-PURPOSE GATE as structural prohibition**: BUILD-VERIFY declares at phase entry: "This phase contains NO file writes, NO structural file-count checks, NO directory comparisons... Any content beyond per-team VERBATIM/DRIFT verdicts is a build error." This is a content-type constraint on the phase block, not a behavioral instruction. The model cannot accumulate adjacent checks because doing so is named as a build error in the phase header.

---

```json
{"top_score": 83, "all_essential_pass": false, "new_patterns": ["Resistance profile derivation pipeline: pre-compute defended-artifact + change-pressure + lens-phrase per team before writing any IA file; lens-phrase becomes both IA verbatim opening and BUILD-VERIFY anchor, creating a closed derivation loop that structurally prevents generic IA", "TRANSCRIPTION-CLEAR phase-exit guard: a named re-audit step after TRANSCRIPTION-RECEIPT confirms all artifact verdicts show VERBATIM before CHART-WRITTEN is authorized — CHART-WRITTEN is contingent on TRANSCRIPTION-CLEAR, not the receipt, making chart-write self-correcting", "SINGLE-PURPOSE GATE at BUILD-VERIFY entry: declares the phase produces exactly one output type per team (VERBATIM/DRIFT verdict) and designates all other content as a named build error — a content-type constraint that prevents verification-phase scope accumulation"]}
```
