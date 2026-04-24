# Quest Score — trace-permissions Round 15

## Scoring Context

All five variations inherit R14-V-05 as base: 31/31 criteria (C-01 through C-39) all PASS. Under v14 the denominator extends to 34, adding C-40, C-41, C-42. Per-criterion aspirational weight = 10/34 ≈ 0.294 pts.

---

## Inherited Criteria Block (C-01 through C-39) — All Variations

| Block | Criteria | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------|----------|------|------|------|------|------|
| Essential | C-01 Role-operation matrix | PASS | PASS | PASS | PASS | PASS |
| Essential | C-02 FLS coverage + null case | PASS | PASS | PASS | PASS | PASS |
| Essential | C-03 Record scope per role | PASS | PASS | PASS | PASS | PASS |
| Essential | C-04 Privilege escalation paths | PASS | PASS | PASS | PASS | PASS |
| Essential | C-05 Security gap inventory | PASS | PASS | PASS | PASS | PASS |
| Recommended | C-06 Dataverse-native terminology | PASS | PASS | PASS | PASS | PASS |
| Recommended | C-07 Sharing rule conflict analysis | PASS | PASS | PASS | PASS | PASS |
| Recommended | C-08 Remediation specificity | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-09 Defense-in-depth layering | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-10 Cross-role differential | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-11 Pre-printed structural tables | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-12 SHALL-obligation contracts + checklist | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-13 Expert role persona sequencing | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-14 Criterion-owner attribution | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-15 Triple-lock enforcement | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-16 Dedicated CA auditor role | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-17 Criterion enforcement preamble matrix | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-18 Quad-lock (CA as M4) | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-19 CA-first authorship model | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-20 Schema Registry + preamble reaffirmation | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-21 Closed authorship loop | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-22 Output-embedded phase execution attestation | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-23 Registry-preamble double-anchor CA verification | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-24 through C-30 (prior rounds) | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-31 Execution order dimension | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-32 Closure-note format dimension | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-33 CS self-reference dimension | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-34 Preamble axis declaration (non-interference) | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-35 SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot + CA-1.9 | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-36 CA terminal tri-dimensional self-evidence attestation | PASS | PASS | PASS | PASS | PASS |
| Aspirational | C-37 through C-39 (R14 base) | PASS | PASS | PASS | PASS | PASS |

All 31 inherited criteria: **PASS across all five variations.** All essential criteria (C-01–C-05) pass in every variation.

---

## New Criteria Scoring (C-40, C-41, C-42)

### C-40 — CA-1.10 bidirectional label-identity cross-scan

**Pass condition:** (a) preamble axis table has Attestation Row Ref column with A-N → ATTEST-A-N values; (b) attestation table has Preamble Row Ref back-column; (c) CA-1.10 row in preamble supplementary table + Phase 3 performs explicit per-row cross-scan.

| Variation | Attestation Row Ref col | Preamble Row Ref col | CA-1.10 cross-scan row | Verdict |
|-----------|------------------------|----------------------|------------------------|---------|
| V-01 | PASS — Axis Declaration col 6 has ATTEST-A-1/2/3 | PASS — attestation table includes Preamble Row Ref | PASS — CA-1.10 added in preamble supplementary table; Phase 3 CA-1.10 performs explicit per-row scan (A-1↔ATTEST-A-1, A-2↔ATTEST-A-2, A-3↔ATTEST-A-3) | **PASS** |
| V-02 | PASS (inherited) | PASS (inherited) | FAIL — no CA-1.10 in supplementary table; Phase 3 attestation verification not a formally numbered CA-1.10 row | **FAIL** |
| V-03 | PASS (inherited) | PASS (inherited) | FAIL — no CA-1.10 added; V-03 is single-axis C-42 only | **FAIL** |
| V-04 | PASS (inherited) | PASS (inherited) | PASS — CA-1.10 added (supplementary table, CA-1.1 through CA-1.10); Phase 3 CA-1.10 double-anchor cross-scan citing ATTEST-TBL | **PASS** |
| V-05 | PASS (inherited) | PASS (inherited) | PASS — CA-1.10 added with double-anchor (Registry: ATTEST-TBL + Preamble: Phase 0 pre-assignment); explicit per-row cross-scan all three pairs | **PASS** |

### C-41 — ATTEST-TBL schema in Schema Registry Step 0.1

**Pass condition:** ATTEST-TBL schema entry in Step 0.1 with ≥5 declared columns including Row ID, Preamble Row Ref, Status; at least one CA-1.N verification row touching attestation content opens with double-anchor citing ATTEST-TBL.

| Variation | ATTEST-TBL in Step 0.1 | CA-1.N cites ATTEST-TBL | Verdict |
|-----------|------------------------|------------------------|---------|
| V-01 | FAIL — Step 0.1 declares "seven schemas" (TABLE_1–5, CS-2, CS-3); no ATTEST-TBL entry. V-01's CA-1.10 Registry anchor cites R12 Axis Declaration col 6, not ATTEST-TBL schema. | FAIL | **FAIL** |
| V-02 | PASS — Step 0.1 gains ATTEST-TBL: 6 declared columns (Row ID, R12 Dimension, Axis Label, Evidence Source, Preamble Row Ref, Status); blank-cell rule stated; Row ID values pre-assigned. Phase 3 attestation verification opens with Registry anchor "Schema ID ATTEST-TBL." | PASS — attestation verification section opens with Registry anchor citing ATTEST-TBL (double-anchor pattern, even without CA-1.10 label) | **PASS** |
| V-03 | FAIL — Step 0.1 = seven schemas only (identical to V-01 base). | FAIL | **FAIL** |
| V-04 | PASS — Step 0.1 has ATTEST-TBL entry (8 schemas). CA-1.10 Registry anchor: "Schema ID ATTEST-TBL: declared columns…" — explicitly cites schema in Registry anchor position of double-anchor row. | PASS | **PASS** |
| V-05 | PASS — Step 0.1 has ATTEST-TBL entry (8 schemas, Section A of manifest lists it). CA-1.10 Registry anchor cites ATTEST-TBL; Phase 3 terminal attestation governed by ATTEST-TBL. | PASS | **PASS** |

### C-42 — Phase 0 Artifact Manifest + terminal manifest citation

**Pass condition:** Named Phase 0 Artifact Manifest section before Phase 0 handoff string with all five enumeration categories (Schema IDs by exact ID, criterion rows by C-NN, SHALL letters, CA-1.N rows by ID, A-N axis rows by ID); terminal verdict cites manifest by item counts per category.

| Variation | Step 0.3 manifest present | Five categories complete | Terminal manifest citation | Verdict |
|-----------|--------------------------|-------------------------|---------------------------|---------|
| V-01 | FAIL — no Step 0.3; Phase 0 closes with "Handing to PHASE 1 -- CS" after Step 0.2 | — | FAIL — terminal verdict cites Registry/preamble/Phase 0 label but no manifest item counts | **FAIL** |
| V-02 | FAIL — no Step 0.3 | — | FAIL — terminal verdict cites "eight schemas including ATTEST-TBL" but no structured manifest citation with item counts per category | **FAIL** |
| V-03 | PASS — Step 0.3 Phase 0 Artifact Manifest explicitly present. Section A: 7 Schema IDs listed by exact ID. Section B: C-01–C-05. Section C: SHALL-A through SHALL-G (7). Section D: CA-1.6–CA-1.9 (4). Section E: A-1/A-2/A-3 (3). All five categories. | PASS | PASS — Phase 0 Manifest Citation in terminal verdict: "7 schemas / 5 criterion rows / 7 SHALL obligations / 4 CA-1.N rows / 3 axis rows" with per-schema exercise confirmation. | **PASS** |
| V-04 | FAIL — no Step 0.3; PHASE 0 mandate describes Step 0.1 and 0.2 only | — | FAIL — terminal verdict does not contain manifest item-count citation | **FAIL** |
| V-05 | PASS — Step 0.3 present. Section A: 8 Schema IDs (includes ATTEST-TBL). Section B: 5 criterion rows. Section C: 7 SHALL obligations. Section D: 5 CA-1.N rows (CA-1.6–CA-1.10). Section E: 3 axis rows. Totals explicit. | PASS | PASS — Phase 0 Manifest Citation: "8 schemas / 5 criterion rows / 7 SHALL obligations / 5 CA-1.N rows / 3 axis rows" with per-artifact exercise confirmation. ATTEST-TBL cited as "governs attestation table (CA-1.10)" and CA-1.10 cited in Section D. | **PASS** |

---

## Per-Variation Composite Scores

### V-01 — Single-Axis C-40

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 through C-39 (inherited) | PASS ×39 | R14-V-05 base |
| C-40 | PASS | CA-1.10 supplementary row in preamble; Phase 3 explicit per-row cross-scan A-1↔ATTEST-A-1, A-2↔ATTEST-A-2, A-3↔ATTEST-A-3 |
| C-41 | FAIL | No ATTEST-TBL in Step 0.1; CA-1.10 Registry anchor cites axis declaration col 6, not a registered schema entry |
| C-42 | FAIL | No Step 0.3 manifest; no terminal manifest citation with item counts |

**Score: 32/34 = 99.4** (100 − 2 × 0.294)

---

### V-02 — Single-Axis C-41

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 through C-39 (inherited) | PASS ×39 | R14-V-05 base |
| C-40 | FAIL | No CA-1.10 row in supplementary table; Phase 3 attestation verification lacks formal CA-1.10 cross-scan designation |
| C-41 | PASS | ATTEST-TBL declared in Step 0.1 (6 columns, blank-cell rule, Row ID pre-assignments); Phase 3 attestation verification opens with Registry anchor citing ATTEST-TBL |
| C-42 | FAIL | No Step 0.3; terminal verdict cites 8 schemas by count but lacks structured manifest with item counts per all five categories |

**Score: 32/34 = 99.4** (100 − 2 × 0.294)

---

### V-03 — Single-Axis C-42

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 through C-39 (inherited) | PASS ×39 | R14-V-05 base |
| C-40 | FAIL | No CA-1.10 row; no label-identity cross-scan |
| C-41 | FAIL | No ATTEST-TBL in Step 0.1 (seven schemas only) |
| C-42 | PASS | Step 0.3 Phase 0 Artifact Manifest present with all five sections (7 schemas, 5 criterion rows, 7 SHALLs, 4 CA-1.N rows, 3 axis rows); terminal verdict Phase 0 Manifest Citation with per-category item counts and per-artifact exercise confirmation |

**Score: 32/34 = 99.4** (100 − 2 × 0.294)

---

### V-04 — C-40 + C-41 Combined

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 through C-39 (inherited) | PASS ×39 | R14-V-05 base |
| C-40 | PASS | CA-1.10 supplementary row in preamble (M4 pre-assigned CA-1.1–CA-1.10); Phase 3 CA-1.10 double-anchor with Registry citing ATTEST-TBL schema + Preamble citing Phase 0 pre-assignment; per-row cross-scan executed |
| C-41 | PASS | ATTEST-TBL in Step 0.1 (8 schemas); CA-1.10 Registry anchor explicitly cites ATTEST-TBL — unifies schema governance and label-identity verification in one double-anchor row |
| C-42 | FAIL | No Step 0.3; Phase 0 closes after Step 0.2; terminal verdict lacks structured manifest citation with item counts per five categories |

**Score: 33/34 = 99.7** (100 − 1 × 0.294)

---

### V-05 — Full Canonical: C-40 + C-41 + C-42

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 through C-39 (inherited) | PASS ×39 | R14-V-05 base |
| C-40 | PASS | CA-1.10 double-anchor cross-scan; preamble Attestation Row Ref and attestation Preamble Row Ref bidirectional label consistency verified per row; all three pairs confirmed |
| C-41 | PASS | ATTEST-TBL in Step 0.1 (8 schemas); manifest Section A lists ATTEST-TBL; CA-1.10 Registry anchor cites ATTEST-TBL; Phase 3 attestation governed by ATTEST-TBL |
| C-42 | PASS | Step 0.3 Phase 0 Artifact Manifest with 8/5/7/5/3 items across five categories; terminal Phase 0 Manifest Citation names all 8 schemas with exercise locations, 5 CA-1.N rows including CA-1.10, confirming all declared artifacts exercised |

**Score: 34/34 = 100.0**

---

## Ranking Summary

| Rank | Variation | Score | Criteria Passed | Open |
|------|-----------|-------|-----------------|------|
| 1 | V-05 | **100.0** | 34/34 | — |
| 2 | V-04 | **99.7** | 33/34 | C-42 |
| 3 | V-01 | **99.4** | 32/34 | C-41, C-42 |
| 3 | V-02 | **99.4** | 32/34 | C-40, C-42 |
| 3 | V-03 | **99.4** | 32/34 | C-40, C-41 |

V-01/V-02/V-03 are tied at 99.4 — all correctly isolated their single target criterion. V-04's combined C-40+C-41 integration demonstrates that CA-1.10 becomes a stronger artifact when its Registry anchor governs the very table it cross-scans.

---

## Excellence Signals from V-05

**1. CA-1.10 as dual-purpose governance row.** A single CA-1.N row simultaneously closes the ATTEST-TBL schema governance chain (C-41) and performs the bidirectional label-identity cross-scan (C-40). No other CA-1.N row in the history of this rubric has been assigned two independent non-overlapping audit targets at once.

**2. ATTEST-TBL elevates the attestation table to first-class citizen.** By registering the terminal attestation table in the Schema Registry, V-05 makes it subject to the same blank-cell prohibition, column structure declaration, and CA verification as every other output table. The attestation is no longer narrative — it is governed output.

**3. Phase 0 Artifact Manifest makes CA authorship machine-verifiable.** Step 0.3 creates a concrete item-count record (8 schemas / 5 criterion rows / 7 SHALLs / 5 CA-1.N rows / 3 axis rows) that the terminal verdict can cite with specific exercise confirmations per artifact. The manifest is not a summary — it is a contract that the terminal verdict must close.

**4. Mutual reinforcement triangle across C-40/C-41/C-42.** C-41 (ATTEST-TBL in Registry) + C-40 (CA-1.10 cites ATTEST-TBL) + C-42 (manifest catalogs ATTEST-TBL as Schema ID 8 and CA-1.10 as supplementary row 5) — each new criterion strengthens the other two. The manifest count "5 CA-1.N rows" only reaches 5 because CA-1.10 exists (C-40). The manifest's Schema section only reaches 8 because ATTEST-TBL was registered (C-41).

**5. Manifest Section D self-documents the C-40 addition.** The manifest explicitly lists CA-1.6 through CA-1.10 with "Total supplementary CA-1.N rows authored: 5." A future auditor can verify CA-1.10 was pre-declared and exercised without reading the full Phase 3 output.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["CA-1.10 as dual-purpose governance row: single CA-1.N row simultaneously closes two independent non-overlapping audit targets (ATTEST-TBL schema compliance + bidirectional label-identity cross-scan)", "Registering the terminal attestation table (ATTEST-TBL) in the Schema Registry elevates it to first-class governed output subject to blank-cell prohibition and CA verification", "Phase 0 Artifact Manifest produces machine-verifiable item-count record that the terminal verdict must close by per-artifact exercise confirmation", "Mutual reinforcement triangle: C-40 depends on C-41 for the ATTEST-TBL Registry anchor, C-42 depends on both for accurate manifested counts -- adding all three simultaneously creates cross-criterion structural binding that any partial combination cannot achieve"]}
```
