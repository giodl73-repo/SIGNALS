---

# discover-competitors-alt — R8 Scorecard

## Scoring Methodology

Criteria evaluated against each variation as a skill instruction: does the instruction **guarantee** the behavior specified in the pass condition? PARTIAL when the instruction requires the behavior but the structural enforcement is weaker than the pass condition strictly demands.

---

## Universal Pass Inventory

The following criteria are satisfied identically and strongly across all 5 variations. Evidence summary follows.

| Criterion | Pass evidence (universal) |
|-----------|--------------------------|
| **C-01** Inertia assessed first | GATE 4 executes before Phase 1. C0 enters as Row C0 (first row) in Phase 2. Structural position enforced. |
| **C-02** Focus woven, not appended | Focus column embedded in competitor table (Phase 2) and findings table (Phase 5). FOCUS CHECK enables vacuous satisfaction when no focus is supplied. |
| **C-03** Threat level per competitor | "Threat" column present in Phase 2 competitor table for all rows including C0. |
| **C-04** Whitespace identified | Phase 3 WHITESPACE produces per-attribute absence evidence and "Gap confirmed" statement. |
| **C-05** Auto-detect without prompting | Phase 1 infers TOPIC and FOCUS from repo context (README, CLAUDE.md, package.json). |
| **C-06** Inertia stickiness reasoning | GATE 4 row 1 explicitly requires "concrete mechanism: switching cost, habit lock-in, or workaround satisfaction… not a category label." |
| **C-07** Web-verified competitive claim | GATE 1 requires inline URL citation per row; Phase 2 requires WebSearch before each competitor row. |
| **C-08** AMEND with 3 actionable adjustments | AMEND lists exactly 3 adjustments; each names what the user changes and what changes in the output (competitor row, whitespace, or inertia). |
| **C-09** Cross-dimensional whitespace finding | Phase 4 + GATE 3 enforce both reductions answering NO before THEREFORE is written. Focus required to produce the gap. |
| **C-10** Table-stakes grounding per finding | Anchor column coercion `Row C{N}, {attribute}: "{value}"` + NOT ACCEPTABLE examples prevent free-floating findings. |
| **C-11** Fully-cited competitor table | GATE 1 applied per row to ALL external competitors ("Apply GATE 1 and GATE 2 per row"). |
| **C-12** Self-negating cross-dimensional finding | GATE 3 checks both reductions present and both answer NO; both must appear in Phase 4 output before THEREFORE. |
| **C-13** Claim-level finding anchors | Structural coercion `Row C{N}, {attribute}: "{value}"` requires attribute-level reference, not name-only. |
| **C-14** AMEND as proof validator | AMEND adj 1 in all variations explicitly requires rebuilding both REDUCTION-1 and REDUCTION-2; "proof rerun failure" named. |
| **C-15** Inline anchor tag before proof block | SOURCE declared before any reduction argument — code-block order (V-01/V-02) or first table row (V-03/V-04/V-05). |
| **C-16** Gate failure naming | All gates name failure states explicitly: Citation gate failure, Anchor gate failure, Proof structure failure, Inertia write failure, etc. |
| **C-17** WHITESPACE grounded by attribute absence | Phase 3 per-row evidence `Row C{N} — {attribute}: {absent/None/N/A/uncontested}` required; bare assertions blocked. |
| **C-18** NOT ACCEPTABLE examples for anchoring | NOT ACCEPTABLE examples naming "Competitor N reveals that…" present in GATE 2, Phase 3, and Phase 5 in all variations. |
| **C-19** Synthesis-first output contracts | Producing phases name their output slot before execution: Phase 2 "fills slot 2 — Anchor column value, PREFLIGHT > OUTPUT CONTRACTS"; Phase 3 names slot 3. |
| **C-20** Structural column coercion for anchoring | Anchor column declared with format shape `Row C{N}, {attribute}: "{value}"` making name-only entries syntactically malformed. |
| **C-21** Gate-as-section with PASS/FAIL table | GATE 1, 2, 3, 4 all have named section headings with 3-column (Check / Pass condition / Failure state) tables with ≥ 2 rows each. |
| **C-22** INERTIA-REF per-finding citation | INERTIA-REF token defined in GATE 4 write row; GATE 4 row 3 requires per-finding citation in INERTIA-REF-DELTA column. |
| **C-23** Output contract slot format specification | All slots in OUTPUT CONTRACTS include both label and format template; slots 1–4, 6 use explicit syntax templates in all variations. |
| **C-24** Phase-to-contract back-references | All producing phases name slot by number and label plus back-path "PREFLIGHT > OUTPUT CONTRACTS" — bidirectional. |
| **C-25** Cross-table structural coercion | Anchor column coercion applied independently in Phase 2 (competitor table) and Phase 5 (findings table); INERTIA-REF-DELTA column adds a third coercion in Phase 5. |
| **C-26** Consolidated PREFLIGHT gate block | All 4 gates are subsections within PREFLIGHT, before Phase 1. No gate outside PREFLIGHT. |
| **C-27** Machine-readable phase assignment in output contract | "Filled by phase" is a dedicated column in OUTPUT CONTRACTS in all variations. |
| **C-28** OUTPUT CONTRACTS co-located within PREFLIGHT | OUTPUT CONTRACTS is a named subsection within PREFLIGHT in all variations. |
| **C-29** Full-path back-reference labels in producing phases | All back-references use "PREFLIGHT > OUTPUT CONTRACTS" (full path), not just "OUTPUT CONTRACTS." |
| **C-30** Write-token instruction within INERTIA-REF gate | GATE 4 write row contains explicit directive `Write at this step: INERTIA-REF = [C0 name]: [specific mechanism phrase]`. |
| **C-31** Write-token encoded as structural gate row | Write directive is a dedicated table row in GATE 4 with distinct Check / Pass condition (containing directive + token format) / Failure state ("Inertia write failure"). |
| **C-32** OUTPUT CONTRACTS declared first within PREFLIGHT | OUTPUT CONTRACTS appears before GATE 1 in all 5 PREFLIGHT blocks. |
| **C-33** Forward-declared cross-dimensional proof slot in output contract | Slot 5 "Focus-scope evidence" appears in OUTPUT CONTRACTS table by name before Phase 4 runs in all variations. |

**All 33 criteria: PASS across all 5 variations.**

---

## Per-Variation Evaluation

### V-01 — Inertia framing ("Required by" column)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 to C-33 | **PASS** | All essential, recommended, aspirational criteria satisfied. See universal table above. |
| **Differentiating feature** | — | 5-column OUTPUT CONTRACTS with "Required by" column makes dependency chain (root → slot 5 → slot 6) readable at contract time. Phase 4 uses code-block proof format; slot 5 format = `SOURCE + REDUCTION-1 NO + REDUCTION-2 NO + THEREFORE` (structural description, satisfies C-23 as format shape). |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 25/25**
**Composite: (5/5 × 60) + (3/3 × 30) + (25/25 × 125) = 60 + 30 + 125 = 215**

---

### V-02 — Output format (pipe-delimited format template for slot 5)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 to C-33 | **PASS** | All criteria satisfied. |
| **Differentiating feature** | — | 4-column OUTPUT CONTRACTS; slot 5 has full pipe-delimited format template `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]`. C-23 satisfaction for slot 5 is strongest of V-01/V-02/V-03 single-axis variations. C-33 slot has syntactically checkable format. No "Required by" column. Phase 4 uses code-block. |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 25/25**
**Composite: 215**

---

### V-03 — Lifecycle emphasis (Phase 4 as 4-row PASS/FAIL proof table)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 to C-33 | **PASS** | All criteria satisfied. |
| **Differentiating feature** | — | 4-column OUTPUT CONTRACTS; slot 5 format = "Phase 4 proof table: SOURCE row + REDUCTION-1 row (NO) + REDUCTION-2 row (NO) + THEREFORE row — all four rows required" (structural description). Phase 4 restructured as a 4-row PASS/FAIL table — SOURCE row position is unambiguous (first table row, not prose-instructed); each row has required value format and named failure state. C-15 (inline anchor before proof) is structurally enforced by table position, not prose instruction. |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 25/25**
**Composite: 215**

---

### V-04 — Combined: Inertia framing + Lifecycle emphasis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 to C-33 | **PASS** | All criteria satisfied. |
| **Differentiating feature** | — | 5-column OUTPUT CONTRACTS ("Required by" column) + Phase 4 as 4-row proof table. Slot 5 "Required by: slot 4 (SOURCE) and slot 1 (INERTIA-REF)" + "Phase 4 proof table" description for format. GATE 4 write row names both slot number and dependent slots: "fills slot 1 (INERTIA-REF, root slot, PREFLIGHT > OUTPUT CONTRACTS above); slots 5 and 6 depend on this token per 'Required by' column." Bidirectional enforcement: provenance visible at contract time (V-01 axis) + proof output verifiable at phase level (V-03 axis). Slot 5 format = description, not full template. |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 25/25**
**Composite: 215**

---

### V-05 — Combined maximum (all three axes + AMEND + GATE 3 NOT ACCEPTABLE)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 to C-33 | **PASS** | All criteria satisfied. |
| **Differentiating features** | — | **"Required by" column** (V-01 axis): slot 5 "Requires slot 4 (SOURCE) and slot 1 (INERTIA-REF)"; slot 6 "Derived from slot 1 (root)". **Full slot 5 format template** (V-02 axis): `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` in OUTPUT CONTRACTS — syntactically checkable before Phase 4 runs. **4-row Phase 4 proof table** (V-03 axis): SOURCE/REDUCTION-1/REDUCTION-2/THEREFORE each a table row with required value format and named failure state. **AMEND slot 5 refill obligation**: AMEND adj 1 explicitly names slot 5 as the target to be refilled; "slot 5 explicitly refilled" is a named success condition — not just "rebuild the proof." **GATE 3 NOT ACCEPTABLE examples**: retroactive THEREFORE construction named as a failure pattern (`NOT ACCEPTABLE: Writing THEREFORE first and then adding REDUCTION-1 and REDUCTION-2 rows to justify it retroactively`), applying GATE 3 NOT ACCEPTABLE to AMEND updates explicitly. |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 25/25**
**Composite: 215**

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Grade |
|-----------|-----------|-------------|--------------|-----------|-------|
| **V-05** | 60/60 | 30/30 | 125/125 | **215** | Exceptional |
| **V-04** | 60/60 | 30/30 | 125/125 | **215** | Exceptional |
| **V-02** | 60/60 | 30/30 | 125/125 | **215** | Exceptional |
| **V-03** | 60/60 | 30/30 | 125/125 | **215** | Exceptional |
| **V-01** | 60/60 | 30/30 | 125/125 | **215** | Exceptional |

All 5 variations achieve 215/215. All criteria pass without PARTIAL.

---

## Ranking (by structural comprehensiveness and enforcement depth)

All variations are grade-equivalent at 215. Rank by secondary axis: number of active enforcement surfaces and self-reinforcing properties.

| Rank | Variation | Axis count | Enforcement surfaces active |
|------|-----------|-----------|---------------------------|
| 1 | **V-05** | 3 + 2 | Required-by provenance + slot 5 pipe template + 4-row proof table + AMEND slot obligation + GATE 3 NOT ACCEPTABLE |
| 2 | **V-04** | 2 | Required-by provenance + 4-row proof table |
| 3 | **V-02** | 1 (strongest) | Pipe-delimited format template for slot 5 (most syntactically precise) |
| 4 | **V-03** | 1 (structural) | 4-row proof table (proof output-verifiable, C-15 structurally enforced) |
| 5 | **V-01** | 1 (relational) | Required-by provenance (dependency graph visible at contract time) |

---

## Excellence Signals from V-05

**1. Dependency provenance column ("Required by") in OUTPUT CONTRACTS**
The "Required by" column makes the execution dependency graph readable at contract-read time without reading any gate. A reader knows before encountering GATE 4 that slot 5 cannot be filled until slots 1 and 4 exist. This converts an implicit execution convention (inertia-first) into a machine-readable contract property. No existing criterion (C-27 captures phase assignment; none captures dependency assignment) rewards this pattern — it is a candidate C-34.

**2. Pipe-delimited format template applied to a compound proof slot**
Slots 1, 2, 3, 4, 6 have atomic format templates (`Row C{N}, {attribute}: "{value}"`). Slot 5 is a compound output (three sentences with structural roles). V-02 and V-05 apply a pipe-delimited template `REDUCTION-1 NO: [...] | REDUCTION-2 NO: [...] | THEREFORE: [...]` that makes the compound slot syntactically checkable without invoking GATE 3. This extends C-23's format-specification standard to compound multi-component slots — the same syntactic enforcement that works for atomic slots.

**3. GATE 3 NOT ACCEPTABLE examples for retroactive proof construction**
C-18 covers NOT ACCEPTABLE examples for anchoring. V-05 extends this to GATE 3 — naming the retroactive THEREFORE escape hatch ("Writing THEREFORE first and then adding REDUCTION-1 and REDUCTION-2 rows to justify it retroactively"). This closes a failure mode unique to proof construction that code-block formats cannot structurally prevent: a model can satisfy the table structure by row count while constructing reductions backward from the desired conclusion. NOT ACCEPTABLE examples are the only enforcement mechanism that addresses this particular failure mode.

**4. Slot-named AMEND rerun obligation**
C-14 requires AMEND to prescribe an explicit rerun of both reductions. V-01–V-04 satisfy this at the reduction level. V-05 adds that slot 5 (Focus-scope evidence) must be explicitly named as the slot being refilled — "slot 5 explicitly refilled" is a success condition, not just "proof rebuilt." This prevents partial AMEND updates where both reductions are technically rerun but the contract slot is not explicitly closed.

---

```json
{"top_score": 215, "all_essential_pass": true, "new_patterns": ["Dependency provenance column ('Required by') in OUTPUT CONTRACTS encodes the execution graph as a machine-readable contract column — distinct from 'Filled by phase' (C-27); candidate for C-34", "Pipe-delimited multi-component format template for compound proof slots extends C-23 format specification to slots with three required structural components rather than a single atomic value", "GATE 3 NOT ACCEPTABLE examples for retroactive proof construction close the backward-THEREFORE escape hatch that structured tables alone cannot prevent — extends C-18 from anchoring to proof construction"]}
```
