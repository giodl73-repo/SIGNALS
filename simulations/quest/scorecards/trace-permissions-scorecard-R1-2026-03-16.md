## Round 13 Scorecard — trace-permissions (v12 Rubric, 28 Criteria)

---

### Criterion-Level Evaluation

All five R13 variations inherit the R12-V-05 base. That base passed C-01 through C-33 (25/28). The only divergence across R13 variations is which of {C-34, C-35, C-36} are added.

#### C-01 through C-33 — All Variations

All five variations carry the full R12-V-05 structural architecture unchanged. Every essential, recommended, and aspirational criterion through C-33 passes in all five variations.

| Range | V-01 | V-02 | V-03 | V-04 | V-05 | Note |
|-------|------|------|------|------|------|------|
| C-01 to C-05 (Essential) | PASS | PASS | PASS | PASS | PASS | Inherited intact — TABLE_1/2/3/4/5, role-operation matrix, FLS, record scope, escalation, gap inventory all present |
| C-06 to C-08 (Recommended) | PASS | PASS | PASS | PASS | PASS | Dataverse terminology, sharing conflict analysis, remediation specificity — all carried from R12-V-05 |
| C-09 to C-16 | PASS | PASS | PASS | PASS | PASS | Defense-in-depth, cross-role differential, pre-printed tables, SHALL-obligations, expert sequencing, criterion-owner attribution, triple-lock, dedicated CA auditor role — all inherited |
| C-17 to C-21 | PASS | PASS | PASS | PASS | PASS | Enforcement preamble matrix, quad-lock, CA-first authorship, Schema Registry with preamble reaffirmation, closed authorship loop — all inherited |
| C-22 to C-30 | PASS | PASS | PASS | PASS | PASS | Phase execution attestation, double-anchor CA verification, Registry-preamble double-anchor, CS-EXPECTATION-VIOLATED three-field block, Tier-column propagation, CA-1.8 CS-0 acknowledgment — all inherited |
| C-31 | PASS | PASS | PASS | PASS | PASS | SE-0 before SE-1 — TABLE_4 at SE-0 position before TABLE_1 at SE-1; ordering explicit in all five |
| C-32 | PASS | PASS | PASS | PASS | PASS | Exact-label two-part closure blocks at SE-2/SE-3/SE-4 — MANUAL GAP [exact label] / STRUCTURED CLOSE format present in all five |
| C-33 | PASS | PASS | PASS | PASS | PASS | CS-0 Registry acknowledgment — CS-0 cites Schema ID: CS-2 and Schema ID: CS-3 by exact labels before CS-1 in all five |

---

#### C-34 — Structural Axis Non-Interference Declaration

**Pass condition:** A dedicated block appears in the preamble (after the C-01-C-05 rows, before analysis sections), naming C-31/C-32/C-33 as three orthogonal structural dimensions with per-axis non-interference statements and a simultaneous-activation mandate. Must be structurally distinct from the mechanism mapping rows.

| Variation | Result | Evidence |
|-----------|--------|---------|
| **V-01** | **PASS** | Lines 184-198: STRUCTURAL AXIS NON-INTERFERENCE DECLARATION block present after SHALL obligations. 3-row table with Axis ID / Criterion / Structural Dimension / Non-Interference Statement. Rows for C-31 (SE execution order), C-32 (closure-note format), C-33 (CS self-reference). Per-axis non-interference statements present: "Activating C-32 does not alter SE execution order" etc. Explicit simultaneous-activation mandate: "All three axes are simultaneously active." Block explicitly stated as "separate from the C-01-C-05 mechanism mapping above." |
| **V-02** | **FAIL** | No axis declaration block in preamble. Step 0.2 contains only the 5-row criterion enforcement matrix and SHALL obligations. No dedicated axis declaration section. |
| **V-03** | **FAIL** | No axis declaration block in preamble. Same as V-02 — Step 0.2 is the enforcement matrix plus SHALL obligations only. |
| **V-04** | **PASS** | Carries V-01's axis declaration block verbatim. Block present at correct location in Step 0.2, structurally distinct from criterion matrix rows, with all three per-axis non-interference statements and simultaneous-activation mandate. |
| **V-05** | **PASS** | Carries V-01/V-04's axis declaration block. Lines 1665-1679: STRUCTURAL AXIS NON-INTERFERENCE DECLARATION present with identical structure. Non-interference statements include explicit parenthetical criterion names ("Activating C-32 (closure-note format) does not alter SE execution order" — the fullest elaboration of any variation). |

---

#### C-35 — SE-4 STRUCTURED CLOSE TABLE_4 Row Cross-Reference + CA-1.9

**Pass condition:** SE-4 STRUCTURED CLOSE content (second part of the two-part SHALL-G block) must include a row-level TABLE_4 cross-reference using format "TABLE_4 (filled at SE-0) row [ID] -- [role] privilege ceiling: [pattern]". CA-1.9 must be a pre-assigned Phase 0 verification row for this requirement, distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP exact labels).

| Variation | Result | Evidence |
|-----------|--------|---------|
| **V-01** | **FAIL** | SE-4 STRUCTURED CLOSE (lines 355-361) contains cross-tier differential summary citing "SE-0 TABLE_4 row ID" in prose — but this is analysis content, not a row-level TABLE_4 cross-reference in the format "TABLE_4 (filled at SE-0) row [ID]". No CA-1.9 verification row. CA-1 rows end at CA-1.8. |
| **V-02** | **PASS** | SE-4 STRUCTURED CLOSE (lines 711-719): Contains explicit "Cite: TABLE_4 (filled at SE-0) row [ID] -- [role] privilege ceiling: [pattern that established the admin-tier ceiling]" format instruction with note "CA-1.9 verifies this location specifically." CA-1.9 row (lines 785-788): full double-anchor reaffirmation — Registry anchor quotes TABLE_4 schema, Preamble anchor quotes SHALL-D extension. Verification checks for format match, SE-0 position naming, row-level identifier granularity. SHALL-D (line 578) carries C-35 extension clause. Explicitly distinct from CA-1.4 and CA-1.7. |
| **V-03** | **FAIL** | SE-4 STRUCTURED CLOSE (lines 1067-1073) cites SE-0 data in prose but lacks the explicit TABLE_4 row cross-reference format. No CA-1.9 verification row. CA-1 rows end at CA-1.8. |
| **V-04** | **PASS** | Carries V-02's SE-4 STRUCTURED CLOSE cross-reference (lines 1430-1436). CA-1.9 present (lines 1502-1505). SHALL-D extension clause present (line 1292). Double-anchor structure in CA-1.9: Registry anchor cites TABLE_4 schema; Preamble anchor cites SHALL-D extension. Distinct from CA-1.4/CA-1.7 explicitly stated. |
| **V-05** | **PASS** | Carries full C-35 architecture (lines 1837-1845 for SE-4 STRUCTURED CLOSE; lines 1911-1914 for CA-1.9). SHALL-D extension (line 1660) present with the fullest formulation — includes the full format string, location requirement, and CA-1.9 audit-target mandate. CA-1.9 double-anchor reaffirmation is the most complete of any variation: Registry anchor explicitly notes TABLE_4 is "rows populated at SE-0 before SE-1" and that this verifies "STRUCTURED CLOSE content" specifically. |

---

#### C-36 — Tri-Dimensional Terminal Self-Evidence Attestation

**Pass condition:** CA Format Compliance Verdict contains a named attestation block with a table naming each R12 structural dimension (execution order / closure-note format / CS self-reference) alongside its specific output-body evidence source. Must extend C-22's phase-execution self-evidence to all three R12 dimensions simultaneously. Body-verifiable column confirms each dimension is self-attestable without prompt inspection.

| Variation | Result | Evidence |
|-----------|--------|---------|
| **V-01** | **FAIL** | CA Format Compliance Verdict (line 427-430) lists standard citation items and overall verdict. No TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block. |
| **V-02** | **FAIL** | CA Format Compliance Verdict (lines 790-793) adds CA-1.9 to the standard items. No TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block. |
| **V-03** | **PASS** | Lines 1143-1153: "TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (C-36)" block present. Table with Dimension / Criterion / Output-Body Evidence Source / Body-Verifiable? columns. Row for C-31 names PHASE 2 section header "SE-0 -- Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)" as the body evidence. Row for C-32 names MANUAL GAP / STRUCTURED CLOSE bracket pattern as body-readable structure. Row for C-33 names CS-0's "Schema ID: CS-2" and "Schema ID: CS-3" citations as the CS-to-Registry link. All three marked CONFIRMED. Block appears in CA Verdict as a distinct named section. |
| **V-04** | **FAIL** | CA Format Compliance Verdict (lines 1507-1510) includes CA-1.9 citation. No TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block. |
| **V-05** | **PASS** | Lines 1920-1929: TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block present. Matches V-03's structure with minor elaboration: C-31 evidence source specifies "without prompt inspection" explicitly; C-33 evidence adds "without cross-referencing the Schema Registry entries and CS table schemas independently." Overall compliance verdict present immediately after the attestation table. |

---

### Composite Scores

Each R12 criterion (C-31/C-32/C-33) = 0.40 pts. Each R13 criterion (C-34/C-35/C-36) = 0.36 pts.
Base from R12-V-05 = 98.9 (25/28).

| Variation | C-34 | C-35 | C-36 | Pts Added | Score | Points |
|-----------|------|------|------|-----------|-------|--------|
| V-01 | PASS | FAIL | FAIL | +0.36 | **99.3** | 26/28 |
| V-02 | FAIL | PASS | FAIL | +0.36 | **99.3** | 26/28 |
| V-03 | FAIL | FAIL | PASS | +0.36 | **99.3** | 26/28 |
| V-04 | PASS | PASS | FAIL | +0.72 | **99.6** | 27/28 |
| **V-05** | PASS | PASS | PASS | +1.08 | **100.0** | 28/28 |

**Ranking:** V-05 > V-04 > (V-01 = V-02 = V-03)

---

### Essential Criteria Verification (C-01 through C-05)

All five variations: **all essential criteria PASS**. The R12-V-05 base carries complete TABLE_1 role-operation matrix, TABLE_2 FLS coverage with explicit null case, TABLE_3 record scope per role, TABLE_4 privilege escalation vectors at SE-0, and TABLE_5 gap inventory. None of the R13 axis additions touch the essential criterion mechanisms.

---

### Excellence Signals from V-05

**What made V-05 uniquely strong:**

1. **Non-interference contractualization over empirical composability.** The STRUCTURAL AXIS NON-INTERFERENCE DECLARATION converts R12-V-05's observed composability (axes coexist without interference) into an explicit binding contract. The parenthetical criterion names in the non-interference statements ("Activating C-32 (closure-note format) does not alter SE execution order") are the most elaborated of any variation — the criterion ID and dimension name are co-located in the contract statement, making the contract self-annotating.

2. **Audit hook isolation at SE-4 STRUCTURED CLOSE.** The TABLE_4 row cross-reference inside the STRUCTURED CLOSE content (not just in analysis prose above the block) creates a new audit-addressable surface. CA-1.9 is a dedicated Phase 0 pre-assigned verification row for this content — making the cross-reference a formal contract obligation rather than a quality suggestion. The triple distinction from CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels), and now CA-1.9 (STRUCTURED CLOSE row cross-reference) demonstrates surgical audit target isolation.

3. **Tri-dimensional body-completeness attestation closes the self-evidence loop.** The TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION in the CA verdict means the output can attest to its own structural compliance for all three R12 dimensions without external reference to prompt instructions. The Body-Verifiable? column forces the attestation to name the specific output-body evidence source for each dimension — not just claim compliance but locate the evidence. V-05 adds "without prompt inspection" and "without cross-referencing... independently" to the evidence source descriptions, making the attestation claim precise about what the reader does not need to do.

4. **Structural isolation across three independent locations.** Each R13 axis touches exactly one location: C-34 touches only the preamble; C-35 touches SE-4 STRUCTURED CLOSE + CA-1.9; C-36 touches only the CA verdict. The three additions are fully non-overlapping in the output structure — confirming that the orthogonality declared in C-34 is architecturally grounded, not merely asserted.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Structural axis non-interference declaration converts empirical composability into a binding contract by naming orthogonal dimensions with per-axis non-interference guarantees in a dedicated pre-analysis block, distinct from the criterion-enforcement matrix rows", "SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference creates an auditable cross-section between threat vector inventory and escalation resolution narrative, with CA-1.9 as a dedicated Phase 0 pre-assigned verification row distinct from CA-1.4 and CA-1.7", "Tri-dimensional terminal self-evidence attestation closes the output structural compliance loop by naming each R12 dimension's specific output-body evidence source, enabling evaluators to verify compliance without prompt inspection"]}
```
