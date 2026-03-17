# Quest Score — campaign-evidence (Round 19)

## Scoring Framework

**Points:** Essential 60 pts (4 × 15) | Recommended 30 pts (3 × 10) | Aspirational 10 pts (40 × 0.25)

**Denominator:** C-01 – C-47 (47 criteria, v19 shift from 44 → 47 adds 3 × 0.25 pts)

**Baseline assumption:** All variations implement C-01–C-44 at PASS fidelity (R18 baseline plus C-44 isolation column confirms universal antipattern annotations across all five).

---

## Criteria Evaluation

### Essential Criteria — 60 pts (C-01–C-04)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-01 | PASS | PASS | PASS | PASS | PASS | All five variations execute a declared 5-stage campaign. |
| C-02 | PASS | PASS | PASS | PASS | PASS | Web search and intelligence precede hypothesis declaration in all. |
| C-03 | PASS | PASS | PASS | PASS | PASS | Falsification conditions present from R13+ baseline. |
| C-04 | PASS | PASS | PASS | PASS | PASS | Self-contained titled output across all. |

**Essential subtotal: 60/60 all variations.**

---

### Recommended Criteria — 30 pts (C-05–C-07)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-05 | PASS | PASS | PASS | PASS | PASS | Stage attribution at ≥70% of claims, inherited baseline. |
| C-06 | PASS | PASS | PASS | PASS | PASS | Synthesis consensus/conflict distinction present. |
| C-07 | PASS | PASS | PASS | PASS | PASS | Calibrated confidence (non-uniform) from R07+ baseline. |

**Recommended subtotal: 30/30 all variations.**

---

### Aspirational Criteria — 10 pts (C-08–C-47 = 40 × 0.25 pts each)

#### C-08 – C-44 (baseline aspirational, 37 criteria × 0.25 = 9.25 pts)

All five variations: **PASS** on C-08 through C-44.

Key notes on criteria requiring specific variation behavior:

- **C-43 (SEQUENCING-ORDER names live ordering decisions):** V-01 and V-03 use web-first (default ordering); C-43's condition triggers only on non-default ordering, so these variations satisfy it trivially. V-02, V-04, V-05 use Intel-first and explicitly name "Intel-first as a governed decision" — full C-43 PASS with substance.
- **C-44 (binary cells carry antipattern-absence annotations):** Explicitly present in all five variations per the isolation matrix.

**Baseline aspirational subtotal: 9.25/9.25 all variations.**

---

#### New Criteria — C-45, C-46, C-47 (3 × 0.25 = 0.75 pts maximum)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| **C-45** | Inertia Baseline table as canonical vocab fixture | **PASS** | FAIL | FAIL | **PASS** | **PASS** |
| **C-46** | Checksum extensibility narrative reconstructs architectural history | FAIL | **PASS** | FAIL | **PASS** | **PASS** |
| **C-47** | Antipattern names in N/A declarations | FAIL | FAIL | **PASS** | FAIL | **PASS** |

**Detailed evidence:**

**C-45:**
- V-01 PASS: IB table gains ID column (`IB-ATTR`, `IB-CAL`, …). Vocabulary Contract declared at top of Form Templates. Binary cells shift from ad hoc phrases to IB-ID references. Audit table gains `Antipattern (IB Row)` column. Machine-checkable link is present — drift between a cell name and an IB row is a visible structural violation.
- V-02 FAIL: Explicitly "No IB vocabulary contract." Ad hoc annotations remain; no canonical source fixture.
- V-03 FAIL: Explicitly "No IB table as canonical source." N/A cells gain antipattern names but without IB anchoring; vocabulary is assembled independently, satisfying C-47 but not C-45.
- V-04 PASS: IB table present with ID column; vocabulary contract active; IB rows cross-reference checksum narrative (IB-SEQ-H, IB-SEQ-O visible as decomposition artifacts).
- V-05 PASS: Full IB integration — positive cells carry IB-IDs, N/A cells carry IB-IDs, audit table populated with IB Row values throughout.

**C-46:**
- V-01 FAIL: No checksum narrative described; section not mentioned.
- V-02 PASS: Architectural history paragraph present: names prior state (5 rules → 40 artifacts), decomposition event (SEQUENCING split into SEQUENCING-HYPO + SEQUENCING-ORDER), delta (+7 propagated automatically), and confirms no static integer manually updated. First-time reader can follow the arithmetic and reconstruct the design decision from the checksum section alone.
- V-03 FAIL: No checksum narrative.
- V-04 PASS: Checksum narrative present and cross-references IB fixture — IB's two SEQUENCING rows (IB-SEQ-H, IB-SEQ-O) are grounded in the decomposition event documented in the narrative. The fixture is not arbitrary; its rows reflect the architectural history.
- V-05 PASS: Same as V-04, with full IB-ID apparatus making the checksum narrative independently verifiable.

**C-47:**
- V-01 FAIL: N/A cells described as structural-reason-only in V-04's isolation notes; V-01 does not introduce C-47 changes.
- V-02 FAIL: No N/A antipattern grounding described.
- V-03 PASS: Every N/A declaration gains the excluded antipattern name — e.g., `CALIBRATION — N/A (evidence stage; uniform-confidence antipattern not applicable here)`. Applied to PRE forms, POST forms, and audit table N/A rows. Apparatus homogeneity achieved independently of IB vocabulary anchoring.
- V-04 FAIL: Explicitly "N/A cells: structural reason only." C-45 and C-46 present but C-47 absent.
- V-05 PASS: N/A cells carry IB-IDs — e.g., `CALIBRATION — N/A [IB-CAL] (evidence stage; uniform-confidence antipattern not applicable)`. Complete homogeneity: every cell tier (PRE binary, POST binary, N/A) cites an IB antipattern by identifier.

---

## Composite Scores

| Variation | Essential | Recommended | Baseline Asp. | C-45 | C-46 | C-47 | **Total** |
|-----------|-----------|-------------|---------------|------|------|------|-----------|
| V-01 | 60.00 | 30.00 | 9.25 | 0.25 | 0.00 | 0.00 | **99.50** |
| V-02 | 60.00 | 30.00 | 9.25 | 0.00 | 0.25 | 0.00 | **99.50** |
| V-03 | 60.00 | 30.00 | 9.25 | 0.00 | 0.00 | 0.25 | **99.50** |
| V-04 | 60.00 | 30.00 | 9.25 | 0.25 | 0.25 | 0.00 | **99.75** |
| V-05 | 60.00 | 30.00 | 9.25 | 0.25 | 0.25 | 0.25 | **100.00** |

---

## Rankings

1. **V-05** — 100.00 (C-45 + C-46 + C-47)
2. **V-04** — 99.75 (C-45 + C-46)
3. **V-01 / V-02 / V-03** — 99.50 (one new criterion each; tied)

---

## Excellence Signals (from V-05)

### Signal 1: Cross-referential structural integrity — fixture, narrative, and cells form a closed system

V-05's distinguishing property is not merely that each new criterion passes in isolation, but that the three mechanisms **reference each other without external lookup required**. The IB fixture's row count (six rows, including IB-SEQ-H and IB-SEQ-O) is explained by the checksum narrative's decomposition event. The checksum narrative's arithmetic is verifiable against the fixture's row structure. Every N/A cell's IB-ID is traceable to a fixture row. Remove any one element and a gap appears in the other two; all three present, the system is closed. V-04 achieves fixture + narrative cross-reference but leaves N/A cells uncited, breaking homogeneity. V-05 is the first configuration where the complete apparatus is self-documenting.

### Signal 2: Homogeneous cell vocabulary across all tiers eliminates asymmetric density

Every cell in the invocation apparatus — PRE binary, POST binary, N/A — carries an IB-ID. The audit table has one vocabulary for positive ("IB-ATTR, guarding"), binary-verified, and excluded ("IB-CAL, excluded") rows. A reader verifying completeness scans one list, not three separate rule declarations. Prior rounds (including V-04) had a structural asymmetry: positive cells were grounded (C-44), N/A cells were not (C-47 absent). V-05 resolves the asymmetry — both tiers carry the same informational density, and cell type becomes the only structural distinction.

### Signal 3: Extensibility demonstrated as observable arithmetic, not asserted as design property

V-04's checksum narrative describes the decomposition event. V-05 adds the IB-ID apparatus, making the decomposition event **observable in the fixture itself** — the two SEQUENCING rows (IB-SEQ-H, IB-SEQ-O) are visible proof that C-42's decomposition happened and propagated into the vocabulary layer without manual integer updates. C-29 (extensibility) is satisfied in all variations; V-05 is the first where extensibility is demonstrable by inspection of the fixture structure, not only asserted in narrative prose.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["cross-referential structural integrity — IB fixture, checksum narrative, and cell vocabulary form a closed self-documenting system where each element grounds the others", "homogeneous cell vocabulary across all invocation tiers — positive, binary-verified, and N/A cells carry identical antipattern-ID density, eliminating asymmetric grounding between tiers"]}
```
