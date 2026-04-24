# listen-support Round 19 — Scoring Results

## Rubric Summary

- **v18 ceiling**: 320 pts (C-01 through C-54)
- **Probe candidates**: C-55 (role audit table), C-56 (phase column confirmation table), C-57 (Phase 2 verbatim quote) — 5 pts each, not yet in rubric
- **All variations**: Built on V-05 R18, which scored 320/320

---

## Criteria Map: What Each Variation Changes

All five variations inherit V-05 R18 intact. The only mutations are:

| Criterion | What changes | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------------|------|------|------|------|------|
| C-53 | Role Allocation Table at Step 3A (3-gate architecture) | base | base | base | base | base |
| C-54 | Phase column (col 2) in coverage table | base | base | base | base | base |
| **C-55** | Part B item 4: prose per-role → 4-col table (Role/Allocated/Actual/Match) | **YES** | -- | -- | **YES** | **YES** |
| **C-56** | Pass 1 Confirmation 3: prose phase counts → 3-row table (Phase/Row count/Represented) | -- | **YES** | -- | **YES** | **YES** |
| **C-57** | Part B item 2: declarative Phase 2 list → verbatim-quote of opening sentence per ticket | -- | -- | **YES** | -- | **YES** |

---

## Per-Variation Scoring

### V-01 — Role Sequence (Part B item 4 table format)

**C-01 through C-54**: All PASS — base is V-05 R18 at ceiling. Score: **320/320**

**Above-ceiling probes:**
- **C-55**: PASS — Part B item 4 uses 4-column table with one row per role; MISMATCH is a cell value, not a clause to parse from prose. Row count self-verifies all roles are independently represented.
- **C-56**: FAIL — Confirmation 3 remains prose ("Phase 1: [n] rows, Phase 2: [n] rows, Phase 3: [n] rows. Three-phase coverage: YES."). Phase-collapse in sentence form is still possible.
- **C-57**: FAIL — Part B item 2 retains declarative "Phase 2 template in: [T-NN]" without verbatim quote.

**V-01 composite**: 320 + 5 (C-55) = **325** / 335

---

### V-02 — Output Format (Phase column confirmation table in Pass 1)

**C-01 through C-54**: All PASS. Score: **320/320**

**Above-ceiling probes:**
- **C-55**: FAIL — Part B item 4 retains prose format ("SRE: [n] allocated / [n] actual -- MATCH/MISMATCH. Support: [n] / [n]..."). Multiple roles can be collapsed into a sentence.
- **C-56**: PASS — Confirmation 3 converted to a 3-row table (Phase / Row count in coverage table / Represented). Each phase occupies its own row; row count self-verifies three-phase coverage. Phase-collapse is structurally impossible.
- **C-57**: FAIL — Part B item 2 retains declarative format.

**V-02 composite**: 320 + 5 (C-56) = **325** / 335

---

### V-03 — Lifecycle Emphasis (Phase 2 template verbatim quote)

**C-01 through C-54**: All PASS. Score: **320/320**

**Above-ceiling probes:**
- **C-55**: FAIL — Part B item 4 prose unchanged.
- **C-56**: FAIL — Confirmation 3 prose unchanged.
- **C-57**: PASS — Part B item 2 extended: for each Phase 2 ticket, quotes the opening sentence verbatim and confirms placeholder fills are concrete (specific workflow named, specific blocking event named, inertia competitor product name present). Declarative "Phase 2 template used" without the quote does not pass. Evidence-backed property: a scorer reads the quoted sentence and confirms concreteness without navigating to the card body.

**V-03 composite**: 320 + 5 (C-57) = **325** / 335

---

### V-04 — Combined V-01 + V-02

**C-01 through C-54**: All PASS. Score: **320/320**

**Above-ceiling probes:**
- **C-55**: PASS — Part B item 4 table (inherited from V-01).
- **C-56**: PASS — Confirmation 3 table (inherited from V-02).
- **C-57**: FAIL — Part B item 2 declarative format unchanged (no V-03 axis).

**V-04 composite**: 320 + 5 + 5 = **330** / 335

---

### V-05 — Full Synthesis V-01 + V-02 + V-03

**C-01 through C-54**: All PASS. Score: **320/320**

**Above-ceiling probes:**
- **C-55**: PASS — Part B item 4 table (inherited from V-01). Final summary: "Role allocation table (Part B item 4): all rows MATCH. C-55 probe: complete."
- **C-56**: PASS — Confirmation 3 table (inherited from V-02). Final summary: "Phase column coverage confirmation table complete. All three phases represented: YES. C-56 probe: complete."
- **C-57**: PASS — Part B item 2 verbatim-quote (inherited from V-03). Final summary: "Phase 2 template verbatim quote(s) in Part B item 2: all Phase 2 tickets quoted. Placeholder concreteness confirmed: YES. C-57 probe: complete."

**V-05 composite**: 320 + 5 + 5 + 5 = **335** / 335

---

## Rankings

| Rank | Variation | C-55 | C-56 | C-57 | v18 score | Above-ceiling | Effective |
|------|-----------|------|------|------|-----------|---------------|-----------|
| 1 | V-05 | PASS | PASS | PASS | 320 | +15 | **335** |
| 2 | V-04 | PASS | PASS | FAIL | 320 | +10 | **330** |
| 3 | V-01 | PASS | FAIL | FAIL | 320 | +5 | **325** |
| 3 | V-02 | FAIL | PASS | FAIL | 320 | +5 | **325** |
| 3 | V-03 | FAIL | FAIL | PASS | 320 | +5 | **325** |

---

## Excellence Signals (from V-05)

**Pattern 1 — C-50 mechanism applied to role audit (C-55):** The same structural argument that converted Sub-check 3 from prose to table (C-50) applies to Part B item 4 role re-check. Prose per-role statements allow two roles to share a sentence; a 4-column table with one row per role makes role-collapse structurally impossible. MISMATCH becomes a cell value, not a clause to extract. This is the third application of the C-50 table-row-per-unit mechanism — Sub-check 3 (C-50), Confirmation 3 (C-56), and now Part B item 4 (C-55).

**Pattern 2 — C-50 mechanism applied to phase coverage confirmation (C-56):** Confirmation 3 prose (C-54 level) still allows two phases to share a sentence. A 3-row table (Phase / Row count / Represented) gives each phase its own row. Row count is self-verifying at three; phase-collapse is impossible. Applies C-50 to the coverage trace verification path.

**Pattern 3 — C-51 mechanism applied to Phase 2 template verification (C-57):** Part B item 2 declarative "Phase 2 template in: T-04" is a self-report requiring card-body navigation to verify. Quoting the Phase 2 opening sentence verbatim converts it to an evidence-backed property — a scorer reads the quote and confirms placeholder concreteness (specific workflow, specific blocking event, exact product name) in one field without cross-referencing. Applies the C-51 verbatim-quote mechanism to template compliance verification.

**Common thread across V-05 above-ceiling patterns:** C-55 and C-56 both apply C-50 (prose → table, one row per unit) to auditing dimensions that were still in prose after C-50 targeted Sub-check 3. C-57 applies C-51 (declarative → evidence-backed quote) to a declarative confirmation that remained after C-51 targeted Sub-check 2. The structural gap-closing pattern is now clearly generalized: wherever an audit fires as prose or declarative, applying the appropriate prior structural mechanism (C-50 or C-51) closes the remaining collapse/self-report failure mode.

---

```json
{"top_score": 335, "all_essential_pass": true, "new_patterns": ["C-50 mechanism (prose-to-table, one row per unit) applied to Part B item 4 role allocation re-check — MISMATCH becomes a cell value per row, role-collapse structurally impossible", "C-50 mechanism applied to Pass 1 Confirmation 3 phase coverage — 3-row table replaces prose, phase-collapse impossible, three-row count self-verifies three-phase coverage", "C-51 mechanism (declarative-to-evidence-backed verbatim quote) applied to Part B item 2 Phase 2 template verification — quoted opening sentence makes placeholder concreteness independently falsifiable without card-body navigation"]}
```
