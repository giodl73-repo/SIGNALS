I have all five variations. Let me now score them against the v13 rubric.

---

## Round 13 Scoring — topic-plan (v13 rubric, C-01 through C-45)

### Structural Summary by Variation

| Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| Gate-0 section header | `Gate-0 -- CONTRACT COMPLETENESS GATE` | `CONTRACT COMPLETENESS GATE` | `CONTRACT COMPLETENESS GATE` | `Gate-0 -- CONTRACT COMPLETENESS GATE` | `Gate-0 -- CONTRACT COMPLETENESS GATE` |
| Gate condition label | `[GATE-0: PASS/STOP ...]` | `[CONTRACT GATE: PASS/STOP ...]` | `[CONTRACT GATE: PASS/STOP ...]` | `[GATE-0: PASS/STOP ...]` | `[GATE-0: PASS/STOP ...]` |
| Phase 2 gate condition | row presence: "all 9 rows present" | cell-exhaustive: `[2a][2b][2c]` named | row presence: "all 9 rows present" | cell-exhaustive: `[2a][2b][2c]` named | cell-exhaustive: `[2a][2b][2c]` named |
| Phase 3 gate condition | structural presence | cell-exhaustive: `[3a][3b][3c][3d]` named | structural presence | cell-exhaustive: `[3a][3b][3c][3d]` named | cell-exhaustive: `[3a][3b][3c][3d]` named |
| Phase 5 gate condition | 4-condition structural | cell-exhaustive: `[5a]–[5f]` named | 4-condition structural | cell-exhaustive: `[5a]–[5f]` named | cell-exhaustive: `[5a]–[5f]` named |
| Schema gate structure | `[A]` compound (8 §IDs bundled) | `[A]` compound (8 §IDs bundled) | `[A1]–[A8]` per-§ID (11 total items) | `[A]` compound (8 §IDs bundled) | `[A1]–[A8]` per-§ID (11 total items) |

---

### Essential Criteria (C-01 through C-05)

**All variations: 5/5 PASS** — no differences on essential criteria across R13 variations.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-01 | PASS | PASS | PASS | PASS | PASS | All: Phase 1 opens strategy.md, extracts STRATEGY DATE, fills §1 Schema A from its content |
| C-02 | PASS | PASS | PASS | PASS | PASS | All: §4 template enumerates all 9 namespaces; Phase 2 fills counts; Phase 4 reads dated artifacts |
| C-03 | PASS | PASS | PASS | PASS | PASS | All: Phase 4 CONFIRMED NEW / PRIOR-ONLY split; STRATEGY DATE extracted in Phase 1 |
| C-04 | PASS | PASS | PASS | PASS | PASS | All: §6 declares ADD/REMOVE/REPRIORITIZE with typed null rows `none -- inertia holds [R-0]` |
| C-05 | PASS | PASS | PASS | PASS | PASS | All: Phase 6 halts explicitly; "Reply YES to proceed, NO to cancel, or REVISED with modifications"; "Stop. Do not write to strategy.md." |

---

### Recommended Criteria (C-06 through C-08)

**All variations: 3/3 PASS** — no differences on recommended criteria.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-06 | PASS | PASS | PASS | PASS | PASS | All: `Evidence artifact [R-3]` mandatory column in §6; Phase 4 reads artifact filenames |
| C-07 | PASS | PASS | PASS | PASS | PASS | All: §6 `Before (from §1 Schema A [R-2])` and `After` columns explicit in template |
| C-08 | PASS | PASS | PASS | PASS | PASS | All: `Why this beats NO CHANGE [R-0]` is a required column; null rows invoke R-0 explicitly |

---

### Aspirational Criteria (C-09 through C-45)

**C-09 through C-42 (34 criteria inherited from R12 ceiling):** All PASS across all variations. No R13 variation removes any structure from R12 V-05. Each variation inherits the full R12 ceiling and adds only the targeted axis. The R12 gap analysis found exactly 3 gaps (G-01, G-02, G-03), meaning R12 V-05 satisfied all 34 of these.

**New v13 criteria — the three differentiating axes:**

#### C-43: Cell-exhaustive gate enumeration

**Criterion**: each in-phase stop gate enumerates every mandatory column by name; a row-presence-only gate fails even if C-12 passes.

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Phase 2: `all 9 namespace rows present; no namespace omitted` — checks row count only; columns namespace, total-artifacts, new are not individually named |
| V-02 | **PASS** | Phase 2: `namespace column [2a] + total-artifacts column [2b] + new column [2c] all non-null across all 9 rows; no blank cells in mandatory columns`; Phase 3: `[3a][3b][3c][3d]`; Phase 5: `[5a]–[5f]` — all three in-phase tabular gates enumerate columns by name |
| V-03 | **FAIL** | Phase 2: `all 9 namespace rows present; no namespace omitted` — row presence only; C-43 not targeted by this axis |
| V-04 | **PASS** | Inherits V-02's Phase 2/3/5 cell-exhaustive column enumeration; same evidence as V-02 |
| V-05 | **PASS** | Inherits V-02's Phase 2/3/5 cell-exhaustive column enumeration; same evidence as V-02 |

#### C-44: Numbered Gate-0 label in block header

**Criterion**: the pre-signal stop gate carries "Gate-0" (or equivalent numbered identifier) in its section header, making it independently scannable as chain-position-zero without reading the body.

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Section header: `Gate-0 -- CONTRACT COMPLETENESS GATE`; condition: `[GATE-0: PASS/STOP ...]`; numbered label present at header level, scannable without reading body |
| V-02 | **FAIL** | Section header: `CONTRACT COMPLETENESS GATE` — no numbered identifier; condition: `[CONTRACT GATE: PASS/STOP ...]`; an auditor scanning headers for "Gate-0" cannot locate the gate |
| V-03 | **FAIL** | Section header: `CONTRACT COMPLETENESS GATE` — no numbered identifier; condition: `[CONTRACT GATE: PASS/STOP ...]`; C-44 not targeted by this axis |
| V-04 | **PASS** | Inherits V-01's `Gate-0 -- CONTRACT COMPLETENESS GATE` header and `[GATE-0: PASS/STOP ...]` condition |
| V-05 | **PASS** | Inherits V-01's `Gate-0 -- CONTRACT COMPLETENESS GATE` header and `[GATE-0: PASS/STOP ...]` condition |

#### C-45: Schema-gate checklist atomicity

**Criterion**: the schema-phase gate is structured as a per-schema checklist where each declared schema is a separate item; item count must equal schema count; a compound single-condition gate fails even if C-38 passes.

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Check `[A]`: "All §ID sections present? §1 Schema A, §2 Verbatim Block, ..." — all 8 §IDs bundled in one compound condition; item count = 4 ([A][B][C][D]) ≠ schema count = 8 |
| V-02 | **FAIL** | Check `[A]`: same compound structure as V-01; 4 items for 8 schemas; C-45 not targeted by this axis |
| V-03 | **PASS** | `[A1]–[A8]` individual items per §ID; `[B][C][D]` structural = 11 total items; annotation: "8 declared schemas + 3 structural checks = 11 items total"; item count (8) equals schema count (8); a missing §ID produces a detectable missing item |
| V-04 | **FAIL** | Check `[A]`: same compound structure as V-01; 4 items for 8 schemas; C-45 not targeted by this axis |
| V-05 | **PASS** | `[A1]–[A8]` per §ID + `[B][C][D]` structural = 11 items; annotation: "8 declared schemas + 3 structural checks = 11 items. Gate-0 passes when all 11 confirmed"; condition names each individually: `schemas [A1][A2]...[A8] all present + phase index [B] + constraint index [C] + null annotations [D]` |

---

### Aspirational Summary (C-09 through C-45)

| Variation | C-09–C-42 (34) | C-43 | C-44 | C-45 | Aspirational Total |
|-----------|----------------|------|------|------|--------------------|
| V-01 | 34 PASS | FAIL | PASS | FAIL | **35/37** |
| V-02 | 34 PASS | PASS | FAIL | FAIL | **35/37** |
| V-03 | 34 PASS | FAIL | FAIL | PASS | **35/37** |
| V-04 | 34 PASS | PASS | PASS | FAIL | **36/37** |
| V-05 | 34 PASS | PASS | PASS | PASS | **37/37** |

---

### Composite Scores

Formula: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/37 × 10)`

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 5/5 → 60 | 3/3 → 30 | 35/37 → 9.46 | **99.46** |
| V-02 | 5/5 → 60 | 3/3 → 30 | 35/37 → 9.46 | **99.46** |
| V-03 | 5/5 → 60 | 3/3 → 30 | 35/37 → 9.46 | **99.46** |
| V-04 | 5/5 → 60 | 3/3 → 30 | 36/37 → 9.73 | **99.73** |
| V-05 | 5/5 → 60 | 3/3 → 30 | 37/37 → 10.00 | **100.00** |

**All variations are golden** (all essential pass, composite ≥ 80).

---

### Ranking

| Rank | Variation | Score | New criteria satisfied |
|------|-----------|-------|------------------------|
| 1 | **V-05** | 100.00 | C-43, C-44, C-45 |
| 2 | **V-04** | 99.73 | C-43, C-44 |
| 3 (tie) | **V-01** | 99.46 | C-44 only |
| 3 (tie) | **V-02** | 99.46 | C-43 only |
| 3 (tie) | **V-03** | 99.46 | C-45 only |

---

### Excellence Signals from V-05

V-05 is the top variation. Four structural patterns explain its superiority:

**1. Header-level gate identity** — Placing "Gate-0" in the section header (`Gate-0 -- CONTRACT COMPLETENESS GATE`) makes the pre-signal gate findable by header scan alone. An auditor does not need to read the gate body to confirm chain-position-zero. This is a scannable rather than content-dependent property.

**2. Condition label alignment** — `[GATE-0: PASS/STOP ...]` in the condition label matches the header numbering, creating a two-surface identity: the gate is named as Gate-0 in the header AND self-declares as GATE-0 in its condition. This makes the numbered chain independently auditable at both levels.

**3. Mandatory-column enumeration in inventory gates** — Phase 2 and Phase 3 gates name each column (`namespace [2a]`, `total-artifacts [2b]`, `new [2c]`) and explicitly state "A row with any blank cell in columns [2a][2b][2c] does not count as a checked namespace." This closes the gap where a row with blank cells could satisfy a row-presence gate. Same column-by-name pattern propagates to Phase 5's 6-column check `[5a]–[5f]`.

**4. Item-count == schema-count atomicity** — `[A1]–[A8]` with the annotation "8 declared schemas + 3 structural checks = 11 items. Gate-0 passes when all 11 confirmed" means completeness is mechanically verifiable by counting: 11 items present = all schemas checked. A missing §ID produces a missing line item, not a silently incomplete compound condition. Item count becomes the completeness proof.

**5. Additive independence** — The three structural improvements (header label, column enumeration, schema atomicity) address orthogonal properties and impose no conflicts. V-05 demonstrates that all three can coexist without degrading any R12-satisfied criterion.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Gate-0 numbered label in section header makes pre-signal gate independently scannable as chain-position-zero without reading body — header-level identity separable from gate condition", "Cell-exhaustive column enumeration in inventory gates names each mandatory column individually with explicit blank-cell rejection rule, closing row-presence loophole that allowed blank-celled rows to satisfy prior gates", "Per-§ID schema gate atomicity where item count equals schema count enables mechanical completeness verification by counting — a missing schema produces a detectable missing item rather than a silent compound failure"]}
```
