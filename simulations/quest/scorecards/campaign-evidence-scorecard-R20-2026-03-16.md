Now I have everything needed for the full evaluation. Let me score Round 20.

---

# Quest Score — campaign-evidence (Round 20)

## Scoring Framework

**Points:** Essential 60 pts (4 × 15) | Recommended 30 pts (3 × 10) | Aspirational 10.75 pts (43 × 0.25; denominator shift 47 → 50 adds 3 × 0.25)

**Denominator:** C-01 – C-50 (50 criteria, v20 shift from 47 → 50)

**Baseline assumption:** All variations implement C-01 through C-47 at PASS fidelity (R19 baseline fully inherited; C-48/C-49/C-50 isolation matrix is the only axis of variation).

---

## Essential Criteria — 60 pts (C-01–C-04)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-01 | PASS | PASS | PASS | PASS | PASS | All five run a declared 5-stage campaign in order. |
| C-02 | PASS | PASS | PASS | PASS | PASS | Web/Intel stages precede hypothesis in all variations. |
| C-03 | PASS | PASS | PASS | PASS | PASS | Falsification conditions present from R13+ baseline. |
| C-04 | PASS | PASS | PASS | PASS | PASS | Self-contained titled output across all five. |

**Essential subtotal: 60/60 all variations.**

---

## Recommended Criteria — 30 pts (C-05–C-07)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-05 | PASS | PASS | PASS | PASS | PASS | Stage attribution ≥70% of claims, inherited baseline. |
| C-06 | PASS | PASS | PASS | PASS | PASS | Synthesis consensus/conflict distinction present in all. |
| C-07 | PASS | PASS | PASS | PASS | PASS | Calibrated non-uniform confidence from R07+ baseline. |

**Recommended subtotal: 30/30 all variations.**

---

## Aspirational Criteria — Baseline (C-08–C-47, 40 × 0.25 = 10.00 pts)

All five variations: **PASS** on C-08 through C-47.

Key notes on variation-sensitive baseline criteria:

- **C-43 (SEQUENCING-ORDER names live ordering decisions):** V-01/V-02/V-03 use Web-first (default ordering); C-43's condition triggers only on non-default ordering, so these trivially satisfy it. V-04/V-05 use Intel-first and name `[IB-SEQ-O]`; Intel-first ordered as governed decision appears explicitly in FORM-PRE-S1 and FORM-POST-S1 cells — full substance C-43 PASS.
- **C-44 (antipattern-absence annotations in binary cells):** All five have antipattern guards in binary cells. V-01/V-04/V-05 use ID-only format (`[IB-ATTR]`); V-02/V-03 use English+ID suffix (`no attribution collapse [IB-ATTR]`). Both formats satisfy C-44's requirement that a binary cell name the specific failure mode being guarded — PASS across all.
- **C-45 (IB vocabulary fixture with ID column):** All five carry the IB table with IB-ID column (IB-ATTR, IB-CAL, IB-FALS, IB-SEQ-H, IB-SEQ-O, IB-PROV). PASS across all.
- **C-46 (checksum extensibility narrative):** All five include the architectural history: prior monolithic SEQUENCING (5 rules, 40 artifacts), decomposition into SEQUENCING-HYPO + SEQUENCING-ORDER, delta +7 propagated automatically, 40 − 8 + 15 = 47. No static integer manually updated. PASS across all. *(Note: R19's V-01 failed C-46 because it had no narrative; R20 carries C-46 as baseline since V-05 established it in R19.)*
- **C-47 (antipattern names in N/A declarations):** All five carry antipattern names in N/A cells (English name present at minimum). PASS across all.

**Baseline aspirational subtotal: 10.00/10.00 all variations.**

---

## New Aspirational Criteria — C-48, C-49, C-50 (3 × 0.25 = 0.75 pts maximum)

### C-48: Binary invocation cells cite IB rows by typed identifier, not name alone

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Explicit "Cell format contract (C-48)" declared in preamble Form Templates section: `[IB-XXX]` is the sole annotation; no English antipattern name in cell body. All binary cells formatted as `[ Yes / No ] — [IB-ATTR]`, `[ Yes / No ] — [IB-SEQ-H]`, etc. An annotation not parseable as `[IB-XXX]` is declared a structural violation regardless of English-name correctness. |
| V-02 | **FAIL** | Binary cells carry English+IB-ID suffix: `[ Yes / No ] — no attribution collapse [IB-ATTR]` (PRE) and `[ Yes / No ] — attribution-collapse absent [IB-ATTR]` (POST). English name is present alongside the IB-ID. C-48 requires the typed ID as the **sole** annotation — name present fails. |
| V-03 | **FAIL** | Same format as V-02: `[ Yes / No ] — no attribution collapse [IB-ATTR]`. English name present alongside ID. C-48 absent by design per variation plan. |
| V-04 | **PASS** | Explicit "Cell format contract (C-48)" declared; all binary cells use `[ Yes / No ] — [IB-ATTR]` ID-only format. Inherited from V-01 design; Intel-first ordering context does not change cell format. |
| V-05 | **PASS** | Full C-48 enforcement: preamble declares "Binary cells: annotation is `[IB-XXX]` typed identifier only. No English name in cell body." All form templates throughout carry ID-only annotations. Exit conditions at each stage check: "all form annotations typed-ID-only." |

---

### C-49: Audit table antipattern column typed to IB row identifiers (FK column)

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **FAIL** | Audit table Final Output section explicitly states: "Antipattern column uses English names — not IB-ID values (C-49 not targeted in this variation)." Column header is `Antipattern`, values are English antipattern names. |
| V-02 | **PASS** | Audit table column renamed to `Antipattern (IB-ID FK)`; cells populated with IB-ID values only (`IB-ATTR`, `IB-CAL`, etc.). Column contract declared: "The `Antipattern (IB-ID FK)` column contains only IB-ID values drawn from the Inertia Baseline fixture. No English antipattern names appear in this column. Any cell value not matching an IB-ID row is a structural violation detectable by identifier lookup." |
| V-03 | **FAIL** | Audit table Note explicitly states: "Antipattern column uses English+IB-ID format; not FK-typed to IB-IDs only (C-49 not targeted)." English names present. |
| V-04 | **PASS** | Audit table has `Antipattern (IB-ID FK)` column with IB-ID values only. Column contract: "IB-ID values only. No English names. Row count: 47 (derived from coverage map). Binary cells use `[IB-XXX]` typed-ID-only format (C-48). N/A cells carry English names only — third tier not IB-ID cited (C-50 absent)." |
| V-05 | **PASS** | Audit table has `Antipattern (IB-ID FK)` column throughout. Column contract in Final Output section: "`Antipattern (IB-ID FK)`: IB-ID values only. No English names. Join-auditable against IB fixture. (C-49)". N/A rows also carry IB-IDs in the FK column per HOMOGENEITY INVARIANT. |

---

### C-50: Complete three-tier IB-ID homogeneity — PRE binary, POST binary, and N/A all cite IB-IDs uniformly; explicit HOMOGENEITY INVARIANT declaration required

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **FAIL** | N/A cells carry English antipattern names only — no IB-IDs in N/A tier. No HOMOGENEITY INVARIANT declared. Example: `CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable)` — no `[IB-CAL]` present. |
| V-02 | **FAIL** | N/A cells carry English names only: `CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable)`. No IB-IDs in N/A tier. No HOMOGENEITY INVARIANT. |
| V-03 | **PASS** | HOMOGENEITY INVARIANT declared immediately after IB table: "PRE binary cells, POST binary cells, and N/A cells all cite IB-IDs uniformly. Every cell in the invocation apparatus... must reference an IB-ID from this fixture." N/A cells include IB-IDs: `CALIBRATION -- N/A [IB-CAL] (evidence stage; uniform-confidence antipattern not applicable)`. Per-stage timing directives carry "HOMOGENEITY INVARIANT: confirm N/A cells carry IB-IDs." All three tiers verified to carry IB-IDs. |
| V-04 | **FAIL** | N/A cells carry English names only: `CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable)`. No HOMOGENEITY INVARIANT declared. Column contract explicitly notes: "N/A cells carry English names only — third tier not IB-ID cited (C-50 absent)." |
| V-05 | **PASS** | HOMOGENEITY INVARIANT declared with full cell format contracts: "Binary cells: `[ Yes / No ] — [IB-XXX]` (typed-ID-only, no English name in annotation body). N/A cells: `-- N/A [IB-XXX] (structural reason; antipattern name not applicable)`." N/A cells throughout carry IB-IDs: `CALIBRATION -- N/A [IB-CAL]`, `FALSIFICATION -- N/A [IB-FALS]`, etc. Audit table N/A rows also carry IB-IDs in the FK column. Final Output section includes HOMOGENEITY INVARIANT verification statement: "scan all cell annotations for `[IB-XXX]` token — any cell (binary or N/A, forms or table) lacking this token is a C-50 violation detectable by identifier-syntax parsing without interpretation." |

---

## Composite Scores

| Variation | Essential | Recommended | Baseline Asp. (C-08–C-47) | C-48 | C-49 | C-50 | **Total** |
|-----------|-----------|-------------|---------------------------|------|------|------|-----------|
| V-01 | 60.00 | 30.00 | 10.00 | 0.25 | 0.00 | 0.00 | **100.25** |
| V-02 | 60.00 | 30.00 | 10.00 | 0.00 | 0.25 | 0.00 | **100.25** |
| V-03 | 60.00 | 30.00 | 10.00 | 0.00 | 0.00 | 0.25 | **100.25** |
| V-04 | 60.00 | 30.00 | 10.00 | 0.25 | 0.25 | 0.00 | **100.50** |
| V-05 | 60.00 | 30.00 | 10.00 | 0.25 | 0.25 | 0.25 | **100.75** |

---

## Rankings

1. **V-05** — 100.75 — Full integration (C-48 + C-49 + C-50). Complete apparatus machine-verifiability.
2. **V-04** — 100.50 — C-48 + C-49. Binary cells and audit table both FK-typed; N/A tier breaks homogeneity.
3. **V-01, V-02, V-03** — 100.25 (tie) — Single-axis isolation; each satisfies exactly one new criterion.

---

## Excellence Signals from V-05

Three patterns from V-05's integration that may seed future criteria:

**Pattern 1: Universal identifier-syntax scan as a stated verification protocol**
V-05 closes the Final Output section with an explicit scan algorithm: "scan all cell annotations for `[IB-XXX]` token — any cell (binary or N/A, forms or table) lacking this token is a C-50 violation detectable by identifier-syntax parsing without interpretation." This converts the HOMOGENEITY INVARIANT from a property assertion into an executable verification protocol. Future criterion candidate: require this scan protocol to be explicitly stated in the preamble (not only the final output) as an immutable check that can run before and after execution.

**Pattern 2: Audit table N/A rows uniformly FK-typed alongside invocation rows**
In V-05 the FK column carries IB-IDs for ALL rows — both the PRE/POST invocation rows and the N/A rows — making the audit table completely homogeneous by row type. C-49 as written requires the antipattern column to contain only IB-IDs, but it is silent on whether N/A rows qualify. V-05 explicitly addresses this via HOMOGENEITY INVARIANT propagation to the table. Future criterion candidate: require the audit table to carry IB-IDs uniformly across invocation rows and N/A rows — no row is exempt from FK-typing.

**Pattern 3: Cell format contracts declared as a two-tier specification (binary + N/A) in the preamble**
V-05 declares both the binary cell format contract (C-48: `[IB-XXX]` only) and the N/A cell format contract (C-50: `-- N/A [IB-XXX] (structural reason)`) as co-equal preamble declarations under "Cell format contracts." Prior rounds declared only binary-tier contracts. The N/A format contract makes the N/A tier's ID requirement structurally parallel to the binary tier's — both are preamble-declared, both machine-verifiable by the same identifier-syntax scan. Future criterion candidate: require the N/A cell format contract to be declared as a named, peer-tier preamble specification alongside the binary cell format contract.

---

```json
{"top_score": 100.75, "all_essential_pass": true, "new_patterns": ["Universal identifier-syntax scan stated as a verification protocol in the Final Output section — converts HOMOGENEITY INVARIANT from a property assertion into an executable check applicable at any point in the brief lifecycle", "Audit table N/A rows carry IB-IDs uniformly alongside invocation rows via HOMOGENEITY INVARIANT propagation — makes the audit table completely FK-typed with no row type exempt", "Cell format contracts declared as a two-tier co-equal preamble specification (binary + N/A) — N/A format contract structurally parallel to binary cell format contract, making both tiers preamble-governed and independently verifiable"]}
```
