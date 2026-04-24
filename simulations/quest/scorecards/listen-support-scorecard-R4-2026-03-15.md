## listen-support — R4 Scoring (rubric v4, 17 criteria)

**Baseline:** R3 V-05 scored 97.8 under v4 (all 15 R3 criteria PASS; C-16/C-17 both FAIL).
**R4 objective:** All five variations fuse the C-16 commitment table with the C-17 role-phase matrix — the two mechanisms R3 developed independently.

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01–C-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| C-01 Ticket inventory | PASS | PASS | PASS | PASS | PASS | All have T-ID/Title/Persona/Volume/Severity/Phase table + TABLE CHECK |
| C-02 Persona attribution | PASS | PASS | PASS | PASS | PASS | Named roles required; TABLE CHECK enforces >= 3 distinct personas; no generic "user" allowed |
| C-03 First-person body voice | PASS | PASS | PASS | PASS | PASS | All have PERFORMANCE MODE; mandate "I/my/we", never "the SRE"; 2-5 sentence body instruction |
| C-04 Gap analysis | PASS | PASS | PASS | PASS | PASS | All three gap categories required with T-NN refs; migration friction sub-section if >= 2 migration tickets |
| C-05 Volume/severity distribution | PASS | PASS | PASS | PASS | PASS | Phase map norms (P2/P3 for Phase 1, P0/P1 for Phase 3); P0 ceiling 25%; high-vol ceiling 50% |

**All essential pass → all variations eligible for golden.**

---

### Recommended Criteria (C-06–C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| C-06 Ticket count 6–12 | PASS | PASS | PASS | PASS | PASS | Explicit >= 6 and <= 12 target with TABLE CHECK enforcement |
| C-07 Cross-persona coverage | PASS | PASS | PASS | PASS | PASS | SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2; no dominant persona > 50% by construction |
| C-08 Gap actionability | PASS | PASS | PASS | PASS | PASS | Gap template requires "specific page/guide", "specific design decision", "runbook/alert/dashboard" |

---

### Aspirational Criteria (C-09–C-17)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| C-09 Ticket clustering + themes | PASS | PASS | PASS | PASS | PASS | Theme declaration step (2–3 named themes, distinct underlying failure, phase distribution) + cross-ticket patterns table |
| C-10 Resolution paths | PASS | PASS | PASS | PASS | PASS | Resolution paths table for all high-vol or P0/P1 tickets; all three fields required; VERIFICATION MANIFEST checks |
| C-11 Multi-stage structural integrity | PASS | PASS | PASS | PASS | PASS | TABLE CHECK before bodies; gap entries require T-NN from inventory; VERIFICATION MANIFEST "broken T-NN refs: 0" row |
| C-12 Role-phase compound coverage | PASS | PASS | PASS | PASS | PASS | Role-phase count matrix with explicit "3+ tickets must span 2+ phases" constraint; verification checks |
| C-13 Phase-calibrated severity | PASS | PASS | PASS | PASS | PASS | Phase map severity norm column; verification requires >= 60% Phase-1 at P2/P3 and >= 1 Phase-3 at P0/P1 |
| C-14 Phase-anchored body voice | PASS | PASS | PASS | PASS | PASS | Commitment table pre-flight checks phase-register match; verification tracks discovery/onboarding vs operational counts |
| C-15 Pre-generation constraint declaration | PASS | PASS | PASS | PASS | PASS | V-01/V-03: Step 1 + dual-pass verification block. V-02/V-04/V-05: CONSTRAINT MANIFEST + VERIFICATION MANIFEST (strongest form) |
| **C-16 Per-ticket vocabulary pre-commitment** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | See detail below |
| **C-17 Role-phase vocabulary matrix** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | See detail below |

---

### C-16 Mechanism Detail

| Variation | Mechanism | Body enforcement | Auditability |
|-----------|-----------|-----------------|--------------|
| **V-01** | STEP 2B: table with T-ID + Role + Phase + **Cell ID** + committed phrase; drawn from STEP 2 matrix cells | STEP 4 PERFORMANCE MODE + STEP 6 body instruction: "Begin with committed phrase from STEP 2B" | Pre-flight check 4 items; STEP 9 verification checks count + conformance |
| **V-02** | STEP 3: table with T-ID + **VM Row ID** + Phase + committed phrase; references VOCABULARY MANIFEST rows | STEP 7 body template header "VM Row: ... \| Committed phrase: ..." | VERIFICATION MANIFEST rows: "Commitment table rows = total ticket count" and "Bodies beginning with committed phrase" |
| **V-03** | Per-role commitment sub-tables (one per active role block), each before that role's bodies | Body template within each role block: "Begin with committed phrase — expanded" | STEP 8 verification: "Commitment sub-tables present in all active role blocks: Y/N" + spot-check |
| **V-04** | STEP 5: table with T-ID + **VM Row ID** + Phase + committed phrase (V-02 structure) | STEP 6 PERFORMANCE MODE + body instruction: "Begin with the committed phrase from STEP 5. Register must match the VM row." | VERIFICATION MANIFEST rows (same as V-02) |
| **V-05** | STEP 3B: table with T-ID + **VM Row ID** + Phase + committed phrase; pre-flight check (5 items) | STEP 4 PERFORMANCE MODE (migration backstory) + STEP 6 dual-mechanism: "OPENING: committed phrase from STEP 3B. REGISTER: use VM Row vocabulary." | VERIFICATION MANIFEST rows; pre-flight check covers C-14/C-16/C-17 simultaneously |

---

### C-17 Mechanism Detail

| Variation | Matrix form | Role differentiation | Body traceability |
|-----------|-------------|---------------------|-------------------|
| **V-01** | STEP 2: unified 5-role × 3-phase table with Cell IDs; each cell: register description + example template phrase | Phase 1 row explicitly shows SRE (setup-oriented), Support (recurring-frustration), PM (metric concern), UX (session-friction), C-xx (migration-surprise) — 5 distinct registers in one row | STEP 6 body header: "Matrix cell: {cell ID from STEP 2B}" — O(1) traceability by cell ID |
| **V-02** | VOCABULARY MANIFEST: named top-level section, 15 rows (VM-SRE-P1 through VM-Cxx-P3); Row ID + Role + Phase + Register + Template phrase | Phase 1 rows: VM-SRE-P1 ≠ VM-Sup-P1 ≠ VM-PM-P1 ≠ VM-UX-P1 ≠ VM-Cxx-P1 — registers distinct by inspection | STEP 7 body header: "VM Row: {row ID}" — VERIFICATION MANIFEST checks "Phase 1 cells show role differentiation (C-17)" |
| **V-03** | Distributed: 5 per-role vocabulary declaration tables (each: Phase \| Register \| Example phrase), one per role block | STEP 8 explicitly checks: "Phase 1 register differs between at least two roles (cross-check SRE vs C-xx): Y / N" | Body header: "Register: {Phase row from [Role] Vocabulary Declaration} \| Committed: {phrase}" — traceability via named role block |
| **V-04** | VOCABULARY MANIFEST (identical to V-02) | Same as V-02 | Same as V-02 + VERIFICATION MANIFEST |
| **V-05** | VOCABULARY MANIFEST (identical to V-02) + STEP 6 body instruction: **"Registers must differ between roles in the same phase"** | C-17 enforced at both planning level (VOCABULARY MANIFEST) and body-writing level (body instruction rule) — strongest double guarantee | Same as V-02/V-04 + explicit inter-role differentiation rule in generation step |

**C-17 note on V-03:** The distributed per-role tables technically satisfy "or equivalent register table" — each cell contains a distinct register/example, and STEP 8 verification explicitly cross-checks Phase 1 differentiation between roles. The weakness: a scorer must read 5 separate blocks to verify inter-role differentiation rather than reading one 2D matrix. This is an auditability concern, not a pass-condition failure.

---

## Score Computation

```
Formula:
  essential_pass    = pass_count / 5  * 60
  recommended_pass  = pass_count / 3  * 30
  aspirational_pass = (pass_count + 0.5 * partial_count) / 9 * 10
```

| Variation | Essential (5/5) | Recommended (3/3) | Aspirational | Composite | Golden? |
|-----------|-----------------|-------------------|--------------|-----------|---------|
| **V-01** | 5/5 → 60.0 | 3/3 → 30.0 | 9/9 → 10.0 | **100.0** | YES |
| **V-02** | 5/5 → 60.0 | 3/3 → 30.0 | 9/9 → 10.0 | **100.0** | YES |
| **V-03** | 5/5 → 60.0 | 3/3 → 30.0 | 9/9 → 10.0 | **100.0** | YES |
| **V-04** | 5/5 → 60.0 | 3/3 → 30.0 | 9/9 → 10.0 | **100.0** | YES |
| **V-05** | 5/5 → 60.0 | 3/3 → 30.0 | 9/9 → 10.0 | **100.0** | YES |

**All five variations reach composite 100 under v4.** The R4 objective is fully achieved: C-16 and C-17 closed in every variation.

---

## Variation Ranking (all tied at 100 — ranked by structural guarantee strength)

| Rank | Variation | Distinguishing property |
|------|-----------|------------------------|
| **1** | **V-05** | Both C-16 and C-17 satisfied by **architectural form** (VOCABULARY MANIFEST required top-level section) **and** enforced at body-writing level ("Registers must differ between roles in the same phase"); PERFORMANCE MODE with migration backstory; all three manifests present; pre-flight check before body generation |
| **2** | **V-04** | VOCABULARY MANIFEST (C-17 by form) + commitment table with VM Row IDs (C-16 by structure) + three manifests; same manifest architecture as V-05 minus the inter-role differentiation rule in the body instruction |
| **3** | **V-02** | VOCABULARY MANIFEST as named top-level section + VM-referenced commitment table + CONSTRAINT and VERIFICATION MANIFESTs; C-15/C-16/C-17 all satisfiable by named-section lookup |
| **4** | **V-01** | Unified 2D matrix with cell IDs in STEP 2 + matrix-derived commitment table in STEP 2B; cell ID column in commitment table makes body-to-matrix traceability O(1); single pre-flight check covers C-14/C-16/C-17 simultaneously |
| **5** | **V-03** | Per-role vocabulary declarations physically collocate vocabulary and bodies (reduces vocabulary-to-body distance); achieves C-17 compliance through the "or equivalent" language; distributed structure makes cross-role C-17 audit slightly harder than a single 2D matrix |

---

## Excellence Signals (from V-05 — top-scoring pattern)

**Signal 1 — Vocabulary matrix as a named top-level section (VOCABULARY MANIFEST) makes C-17 satisfiable by form**
V-02/V-04/V-05 elevate the role-phase matrix from a generation step to a named required section that precedes all other generation. A scorer verifies C-17 by reading one named section, not by inspecting all body texts. V-01/V-03 keep the matrix inside a generation step — still PASS, but the audit path is longer.

**Signal 2 — Commitment table rows reference manifest Row IDs, making C-16→C-17 connection machine-auditable**
V-02/V-04/V-05 commit table rows carry VM Row IDs (VM-SRE-P1, etc.). A scorer can verify that every commitment cites a valid manifest row (C-17 source) and that every body begins with the committed phrase (C-16 outcome) by reading two sections with a row-ID join. V-01 uses Cell IDs (equivalent structure). V-03 distributes this across role blocks (harder to join).

**Signal 3 — Explicit inter-role differentiation rule in body instruction (V-05 only)**
V-05 STEP 6 adds: "REGISTER: Registers must differ between roles in the same phase." This encodes C-17's core requirement at body-generation time — not only declared in a manifest, but actively instructed during writing. No earlier variation or round had this.

**Signal 4 — Pre-flight check before body generation covers C-14/C-16/C-17 simultaneously**
V-01 and V-05 both have a pre-flight check immediately before body generation: phase-register match, discovery phrase verification, operational phrase presence, VM Row ID validity. This prevents constraint drift between planning and execution — the model cannot enter the body-writing phase with unresolved C-14/C-16/C-17 failures.

**Signal 5 — VERIFICATION MANIFEST rows labeled by criterion ID (C-16, C-17)**
V-02/V-04/V-05 have VERIFICATION MANIFEST rows that explicitly name C-16 and C-17: "Commitment table rows = total ticket count (C-16)", "VM distinct roles (C-17)", "Phase 1 cells show role differentiation (C-17)". A reviewer auditing the output for v4 compliance reads the VERIFICATION MANIFEST row labeled with the criterion, rather than cross-checking body text. Audit path is O(1) per criterion.

---

## Summary

R4 closes both v4 gaps in all five variations. The R3 divide (V-01 had C-16 but not C-17; V-03 had C-17 but not C-16) is resolved across the board by fusing the commitment table mechanism with the role-phase matrix mechanism. V-05 is the composite-100 candidate and the strongest structural guarantee: all three mechanisms (VOCABULARY MANIFEST, commitment table with VM Row IDs, inter-role differentiation body rule) are present, and all three can be verified by named-section lookup.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["VOCABULARY MANIFEST as named top-level section makes C-17 satisfiable by form — scorer verifies in O(1) by section lookup rather than body inspection", "Commitment table rows carry manifest Row IDs creating a machine-auditable C-16/C-17 join: valid source row (C-17) + body opening conformance (C-16) verified by two-section cross-reference", "Inter-role differentiation rule added to body instruction ('Registers must differ between roles in the same phase') — C-17 enforced at generation time, not only at planning time", "Pre-flight check before body generation covers C-14/C-16/C-17 simultaneously, preventing constraint drift between the planning and writing phases"]}
```
