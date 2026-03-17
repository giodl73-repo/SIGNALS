## Quest Score — trace-permissions R13, Rubric v12

**Denominator:** 28 criteria (5 essential + 3 recommended + 20 aspirational)
**Point weights:** Essential = 12 pts each | Recommended = 10 pts each | Aspirational = 10/28 ≈ 0.357 pts each

---

### Criteria Evaluation

**Base inheritance:** All R13 variations build on R12-V-05, which passed all 25 criteria except C-34/C-35/C-36. Criteria C-01 through C-33 (those in-scope for v12) are evaluated below with brief evidence; only the R13 axes (C-34/C-35/C-36) vary between variations.

---

#### Essential Criteria (C-01 to C-05) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 Role-operation matrix | PASS | PASS | PASS | PASS | PASS | TABLE_1 with Tier col, 8 operations, all rows required |
| C-02 FLS coverage + null case | PASS | PASS | PASS | PASS | PASS | TABLE_2 with Configured/Not Configured, null case stated |
| C-03 Record scope per role | PASS | PASS | PASS | PASS | PASS | TABLE_3 with OWD Baseline + Effective Scope per role |
| C-04 Privilege escalation detection | PASS | PASS | PASS | PASS | PASS | TABLE_4 all four vectors, Checked?=YES |
| C-05 Security gap inventory | PASS | PASS | PASS | PASS | PASS | TABLE_5 with named gap types, Tier column, Remediation |

All essential criteria: **PASS / 5/5** across all variations.

---

#### Recommended Criteria (C-06 to C-08) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-06 Dataverse-native terminology | PASS | PASS | PASS | PASS | PASS | business units, column security profiles, owner teams, OWD, table permissions used throughout |
| C-07 Sharing rule conflict analysis | PASS | PASS | PASS | PASS | PASS | CS-2 sharing rule table, SE-0 TABLE_4 T4-2 vector, cross-reference protocol |
| C-08 Remediation specificity | PASS | PASS | PASS | PASS | PASS | Three-field block (CS-Expected / SE-Actual / Delta) mandated by SHALL-F |

All recommended criteria: **PASS / 3/3** across all variations.

---

#### Aspirational Criteria — Inherited Base (all in-scope v12 aspirational except C-34/C-35/C-36)

R12-V-05 passed all 25 criteria including C-09..C-25 (17 pre-R12 aspirational) and C-31/C-32/C-33 (R12 trio). All R13 variations inherit this base unchanged.

**C-09 Defense-in-depth layering:** Four-layer sequence in SE-2 defense-in-depth check + SE-0 admin bypass note. **PASS** all variants.

**C-10 Cross-role differential analysis:** SE-1 requires CS vs Admin-tier vs Custom-tier comparison citing TABLE_4 data. **PASS** all variants.

**C-11 Pre-printed tables + blank-cell prohibition:** Schema Registry pre-declares all 7 schemas; blank-cell rule stated globally. **PASS** all variants.

**C-12 SHALL obligations + terminal checklist:** SHALL-A through SHALL-G + CA-1 verdict terminal confirmation. **PASS** all variants.

**C-13 Expert role persona sequencing:** SE (Security Engineer) + CS (Customer Success) + CA (Compliance Auditor) — three named roles with dedicated sub-sections. **PASS** all variants.

**C-14 Criterion-owner attribution in terminal checklist:** CA verdict attributes each CA-1.x result to the CA role; open items named with responsible role. **PASS** all variants.

**C-15 Triple-lock pattern (format + role + SHALL):** Preamble matrix explicitly maps all three for C-01..C-05 with "simultaneously active" rule. **PASS** all variants.

**C-16 Dedicated CA format-compliance auditor role:** CA's sole mandate in Phase 3 is structural verification, entirely separate from SE security analysis. **PASS** all variants.

**C-17 Criterion enforcement preamble matrix:** 5-row × 4-column table (M1/M2/M3/M4) with "simultaneously active" declaration. **PASS** all variants.

**C-18 Quad-lock (C-15 + C-16 + CA M4 column):** M4 pre-assignments CA-1.1..CA-1.8 in preamble, CA-1 rows cross-reference criterion IDs. **PASS** all variants.

**C-19 CA-first authorship model:** Phase 0 mandate explicit; CA authors Registry and preamble before SE/CS execute. **PASS** all variants.

**C-20 Schema Registry + preamble reaffirmation:** Schema Registry section precedes preamble; CA-1 rows quote Registry anchor + Preamble anchor sequentially. **PASS** all variants.

**C-21 Closed authorship loop:** CA authors both Registry (Step 0.1) and preamble (Step 0.2) in single Phase 0 execution. **PASS** all variants.

**C-22 Output-embedded phase execution attestation:** PHASE 0/1/2/3 labels as section headers, handoff strings name next phase, CA-1 rows cite "Phase 0 M4 pre-assignment." **PASS** all variants.

**C-23 Registry-preamble double-anchor CA verification:** Each CA-1 row = Registry anchor (schema ID + columns) + Preamble anchor (C-xx/TABLE/role/SHALL/CA row) as structurally distinct labeled elements. **PASS** all variants.

**C-31 SE-0 tier-first ordering (R12):** SE-0 before SE-1, TABLE_4 at SE-0, Tier column on TABLE_1/TABLE_3, SE-4 cross-tier differential citing SE-0 data. **PASS** all variants.

**C-32 Exact-label two-part closure blocks (R12):** SE-2/SE-3/SE-4 open with `MANUAL GAP [<exact CONTEXT label>]:` + `STRUCTURED CLOSE:` blocks. CA-1.7 verifies. **PASS** all variants.

**C-33 CS-0 Schema Registry self-reference (R12):** CS-0 sub-section echoes CS-2/CS-3 by exact Schema ID before authoring expectation rows. CA-1.8 verifies. **PASS** all variants.

*Note: Criteria C-24..C-30 not in active v12 scope (not yet introduced); C-34..C-36 evaluated below.*

---

#### R13 Aspirational Criteria — Variable (C-34/C-35/C-36)

**C-34: Preamble structural axis declaration (non-interference contract)**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | "R12 Structural Axis Declaration (C-34 contract)" block present in Step 0.2 after SHALL-G; names Axis 1 (C-31/execution order), Axis 2 (C-32/closure-note format), Axis 3 (C-33/CS self-reference); explicit non-interference declaration: "satisfying any one axis neither enables nor precludes satisfying either of the others" |
| V-02 | FAIL | Step 0.2 has no axis declaration block; only the standard SHALL obligations and the CA-1.9 additional M4 pre-assignment note |
| V-03 | FAIL | Step 0.2 identical to V-01 base minus axis declaration; no orthogonality contract |
| V-04 | **PASS** | Axis declaration present (identical mechanism to V-01); additionally more specific: Axis 1 description includes "SE-4 STRUCTURED CLOSE cites SE-0 TABLE_4 row IDs T4-1 through T4-4" (upgraded from V-01's "SE-0 TABLE_4 data") |
| V-05 | **PASS** | Axis declaration present with full specificity including T4-1..T4-4 in Axis 1 description; all three axes named with non-interference declaration |

**C-35: SE-4 STRUCTURED CLOSE TABLE_4 SE-0 row cross-reference + CA-1.9**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | SE-4 STRUCTURED CLOSE mentions "citing the SE-0 TABLE_4 row ID" (singular, generic) — not named T4-1..T4-4; no CA-1.9 row; Schema Registry TABLE_4 entry has no row ID assignment |
| V-02 | **PASS** | Schema Registry TABLE_4 declares T4-1..T4-4 with SE-4 cross-reference mandate; SE-4 STRUCTURED CLOSE names "T4-1 (Team inheritance), T4-2 (Sharing rules), T4-3 (Impersonation), and T4-4" by ID; CA-1.9 present as distinct anchor-reaffirmation row with explicit distinctness from CA-1.4 and CA-1.7 |
| V-03 | FAIL | Schema Registry TABLE_4 has no row IDs; SE-4 STRUCTURED CLOSE generic; no CA-1.9 |
| V-04 | **PASS** | Same T4-1..T4-4 mechanism as V-02; CA-1.9 present; Schema Registry pre-registration intact |
| V-05 | **PASS** | Same as V-04 — TABLE_4 Registry row IDs, SE-4 STRUCTURED CLOSE names T4-2 and T4-4 by ID in attribution, CA-1.9 verifies distinctness from CA-1.4/CA-1.7 |

**C-36: CA terminal verdict tri-dimensional self-evidence attestation**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | CA verdict ends after CA-1.8 result summary; no R12 Tri-Dimensional Attestation block |
| V-02 | FAIL | CA verdict includes CA-1.9 result (C-35) but no tri-dimensional attestation block |
| V-03 | **PASS** | "R12 Tri-Dimensional Self-Evidence Attestation (C-36 contract)" block present; Dimension 1 cites "SE-0 — Admin-Tier Inventory and Escalation Vectors" section header + TABLE_4 row position; Dimension 2 cites exact MANUAL GAP block strings; Dimension 3 cites "CS-0 — Schema Registry Acknowledgment" sub-section and CA-1.8 verification; terminal attestation: "All three R12 dimensions are simultaneously self-evident from the output body without reference to prompt instructions" |
| V-04 | FAIL | CA verdict includes CA-1.9 result but no tri-dimensional attestation |
| V-05 | **PASS** | Tri-dimensional attestation block present; Dimension 1 additionally cites "TABLE_4 rows T4-1 through T4-4" (more specific than V-03 because C-35 mechanism is also present); CA-1.8 verification cited for Dimension 3 |

---

### Composite Scores

| Variation | C-01..C-05 | C-06..C-08 | Base Asp. (17) | C-31..C-33 | C-34 | C-35 | C-36 | Criteria Passed | Score |
|-----------|-----------|-----------|---------------|-----------|------|------|------|-----------------|-------|
| V-01 | 5/5 | 3/3 | 17/17 | 3/3 | PASS | FAIL | FAIL | **26/28** | **99.3** |
| V-02 | 5/5 | 3/3 | 17/17 | 3/3 | FAIL | PASS | FAIL | **26/28** | **99.3** |
| V-03 | 5/5 | 3/3 | 17/17 | 3/3 | FAIL | FAIL | PASS | **26/28** | **99.3** |
| V-04 | 5/5 | 3/3 | 17/17 | 3/3 | PASS | PASS | FAIL | **27/28** | **99.6** |
| V-05 | 5/5 | 3/3 | 17/17 | 3/3 | PASS | PASS | PASS | **28/28** | **100.0** |

Score formula: `100.0 - (criteria_failed × 10/28)`. Each aspirational failure = 0.357 pts deducted.

---

### Ranking

1. **V-05** — 100.0 (28/28) — C-34 + C-35 + C-36 all present; confirmed 100% candidate
2. **V-04** — 99.6 (27/28) — C-34 + C-35 present; fails only C-36 (no tri-dimensional verdict)
3. **V-01** — 99.3 (26/28) — C-34 only; axis declaration without row-ID cross-reference or attestation
4. **V-02** — 99.3 (26/28) — C-35 only; row-ID cross-reference without axis declaration or attestation
5. **V-03** — 99.3 (26/28) — C-36 only; tri-dimensional attestation without axis contract or CA-1.9

V-01/V-02/V-03 are tied at 99.3 with different single-axis contributions. None is strictly better than the others by score; they are directionally orthogonal improvements.

---

### Excellence Signals from V-05

**Pattern 1 — Preamble orthogonality contract as a non-interference binding declaration.**
Rather than asserting that three mechanisms are co-active, V-05 adds an explicit non-interference statement ("satisfying any one axis neither enables nor precludes satisfying either of the others"). This converts the empirical observation from R12 (the three axes composed without interference) into a structural contract that an executor is obligated to honor. The declaration is placed as a preamble element — before any analysis phase — so it governs execution from the start, not as a retrospective observation.

**Pattern 2 — Schema Registry row-ID pre-registration for named cross-section references.**
By declaring T4-1..T4-4 as named row IDs inside the Schema Registry entry (not just in the TABLE_4 template), V-05 creates a named forward-reference contract: SE-4's STRUCTURED CLOSE is obligated to cite those names, and CA-1.9 can verify the citation by name, not just by position. This makes a cross-section reference auditable at schema-registration time — a new pattern for intra-prompt traceability.

**Pattern 3 — Third audit sub-row for a section with multiple independently verifiable structural properties.**
SE-4 previously had two CA audit targets: CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP exact-label compliance). V-05 adds CA-1.9 as a third independently verifiable structural property of SE-4 (the TABLE_4 row ID cross-reference in STRUCTURED CLOSE). The distinctness is declared explicitly in both the preamble additional M4 assignment and in the CA-1.9 row itself ("not subsumed by CA-1.4 or CA-1.7 scope"). This "enumerate all independently auditable structural properties per section" pattern generalizes.

**Pattern 4 — Attestation blocks using named output-body section headers as evidence sources.**
V-05's tri-dimensional attestation cites specific section header strings as evidence — e.g., `"SE-0 — Admin-Tier Inventory and Escalation Vectors" section header in document body precedes "SE-1" section header`. By naming the exact section headers, the execution order is verifiable from the output text alone without prompt inspection. This is distinct from citing the mechanism (the prompt instruction) — it cites the output artifact (the section header string). This pattern makes any structural claim independently verifiable from the output document.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Preamble orthogonality contract: explicit non-interference declaration converts empirical composability into a binding structural obligation before analysis begins", "Schema Registry row-ID pre-registration creates named forward references that cross-section citations must honor by ID, enabling schema-registration-time audit contracts", "Third CA audit sub-row (CA-1.9) as independently verifiable structural property of SE-4, distinct from SE-0 ordering (CA-1.4) and exact-label compliance (CA-1.7)", "Tri-dimensional attestation cites named output-body section header strings as evidence sources, making execution sequence self-verifiable from the output text without prompt inspection"]}
```
