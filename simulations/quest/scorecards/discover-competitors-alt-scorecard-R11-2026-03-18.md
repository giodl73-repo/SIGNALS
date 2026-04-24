## discover-competitors-alt — Round 11 Scoring

### Scoring Framework
- Essential (C-01–C-05): 12 pts each | Recommended (C-06–C-08): 10 pts each | Aspirational (C-09–C-31): 0.435 pts each (23 criteria)
- Formula: `(E/5×60) + (R/3×30) + (A/23×10)`

---

### Per-Criterion Summary

**Essential & Recommended:** All 5 variations pass 5/5 essential and 3/3 recommended — 90 pts each baseline.

**Aspirational — decisive criteria only:**

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 through C-28 | All carry-forward | PASS | PASS | PASS | PASS | PASS |
| **C-29** | Committed value in column header (outcome) | PASS | PASS | PASS | PASS | PASS |
| **C-30** | Bracket notation + explicit substitution instruction (mechanism) | PASS | PASS | **FAIL** | PASS | PASS |
| **C-31** | GATE-0 table retains template form + propagation contract in isolation | **FAIL** | PASS | **FAIL** (dep) | PASS | PASS |

---

### Key Analysis

**C-29 — PASS for all 5:** `[TOKEN]` bracket notation is a universally recognized placeholder convention. Even V-03 (no substitution instruction) achieves the C-29 outcome — bracket syntax signals "substitute committed value here" and capable models honor it. C-29 tests outcome; C-30 tests mechanism.

**C-30 — FAIL for V-03 only:** The "with an explicit substitution instruction" clause is independent of bracket syntax. V-03 uses `[TOKEN]` throughout but is silent on substitution in every location (preamble, gate bodies, table cells). Bracket notation is necessary but not sufficient.

**C-31 — FAIL for V-01 (preamble-only), FAIL for V-03 (dependency):**
- **V-01:** Preamble carries the substitution instruction, but consulting GATE-0's table in isolation yields only the declaration — no propagation contract. C-31's isolation test fails.
- **V-02:** Dedicated third row ("Propagation contract") inside GATE-0 table carries both declaration (row 2) and propagation rule (row 3) — fully self-contained. PASS.
- **V-04:** TOKEN row Yes-cell carries both declaration and propagation in a single cell: "GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ column headers." Compact minimal form. PASS.
- **V-05:** Same table-layer mechanism as V-04 plus preamble + manifest column. PASS.

---

### Composite Scores

| Variation | Asp (A/23) | Composite |
|-----------|------------|-----------|
| V-01 | 22/23 = 9.565 | **99.565** |
| V-02 | 23/23 = 10.000 | **100.000** |
| V-03 | 21/23 = 9.130 | **99.130** |
| V-04 | 23/23 = 10.000 | **100.000** |
| V-05 | 23/23 = 10.000 | **100.000** |

**Ranking:** V-02 = V-04 = V-05 = **100** > V-01 = **99.565** > V-03 = **99.130**

Predictions confirmed exactly. Three decisive questions resolved:
1. Preamble-only fails C-31 — propagation contract must be inside the table.
2. Bracket notation without instruction fails C-30 — mechanism must be declared.
3. V-04 = V-02 = 100 — "row or cell" is non-ranking; compact cell is the minimal compliant form.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["compact TOKEN row cell as minimal C-31 compliant pattern -- declaration and propagation co-located in single Yes-cell without dedicated third row; V-04 is the preferred minimal form over V-02 verbose row", "manifest TOKEN propagation column declaring per-gate TOKEN inheritance state at architecture level -- additive quality layer beyond per-gate tables; candidate for C-32"]}
```
ucturally first; no focus detection, headers, or branching before it; C-15 passes |
| C-20 | PASS | PASS | PASS | PASS | PASS | All: AMEND schema names all four components: Input change, Output effect, Stability verdict, Evidence; C-16 passes |
| C-21 | PASS | PASS | PASS | PASS | PASS | All: GATE-0 header + EXECUTION PLAN both declare GATE-0 unconditional and GATE-1 as first conditional; C-19 passes |
| C-22 | PASS | PASS | PASS | PASS | PASS | All: four schema labels domain-neutral; naive reader can match each to function; C-20 passes |
| C-23 | PASS | PASS | PASS | PASS | PASS | All 5 gates enumerated with UNCONDITIONAL/CONDITIONAL labels in manifest before GATE-0 executes; C-21 passes |
| C-24 | PASS | PASS | PASS | PASS | PASS | All: manifest is native pipe-and-hyphen table outside code fences; C-23 passes |
| C-25 | PASS | PASS | PASS | PASS | PASS | All: TOKEN marked as required in REQUIRED OUTPUTS block of every gate by committed value; C-13 passes |
| C-26 | PASS | PASS | PASS | PASS | PASS | All: every gate has `**REQUIRED OUTPUTS:**` heading with extractable structured block; TOKEN appears within; C-25 passes |
| C-27 | PASS | PASS | PASS | PASS | PASS | All: no completion conditions in any gate; REQUIRED OUTPUTS block is sole output specification; C-26 passes |
| C-28 | PASS | PASS | PASS | PASS | PASS | All: every REQUIRED OUTPUTS block is native pipe-and-hyphen table outside code fences; C-26 passes |
| **C-29** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **All: see C-29 analysis below** |
| **C-30** | **PASS** | **PASS** | **FAIL** | **PASS** | **PASS** | **Decisive criterion -- see C-30 analysis below** |
| **C-31** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** | **Decisive criterion -- see C-31 analysis below** |

---

### C-29 Decisive Analysis

**C-29 test:** "explicitly declares TOKEN as required by its committed value -- making TOKEN's required status machine-verifiable from the block alone."

R10 resolved the failing pattern: `TOKEN required?` (abstract word, no brackets) left the committed identifier absent from the column header. All R11 variations advance to `[TOKEN] required?` bracket-notation throughout.

**All R11 variations (V-01 through V-05):** Column header is `[TOKEN] required?`.

`[TOKEN]` bracket notation functions as a universally recognized template placeholder -- after GATE-0 commits a value (e.g., `SIGNAL-LOCK`), GATE-1+ column headers resolve to `SIGNAL-LOCK required?`. This holds even for V-03 (no substitution instruction): bracket convention signals "substitute the committed value here," achieving the C-29 outcome through convention rather than explicit directive. The OUTCOME (committed value in header) is achieved for all 5 variations.

C-30 -- which tests the mechanism (explicit instruction declared) rather than the outcome -- is where V-03 diverges.

**C-29: PASS for all 5 variations.**

---

### C-30 Decisive Analysis

**C-30 test:** `[TOKEN]` bracket-notation syntax WITH an explicit substitution instruction. Bracket notation is necessary but not sufficient -- "with" is an independent requirement, not implied by the syntax.

**V-01:** Bracket notation + preamble instruction: "After GATE-0 declares `TOKEN: [identifier]`, substitute the committed value for `[TOKEN]` in all REQUIRED OUTPUTS column headers from GATE-1 through GATE-4." Instruction is explicitly declared in the preamble. **PASS.**

**V-02:** Bracket notation + dedicated Propagation contract row in GATE-0 table: "committed declared value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers (e.g., TOKEN = SIGNAL-LOCK -> GATE-1 through GATE-4 produce `SIGNAL-LOCK required?` as column header)." The row body is the explicit instruction. **PASS.**

**V-03:** Bracket notation throughout -- NO substitution instruction anywhere. Preamble, gate bodies, and table cells are all silent on substitution. Bracket notation is structural decoration only; the "with an explicit substitution instruction" clause is unmet. **FAIL.**

**V-04:** Bracket notation + TOKEN row Yes-cell contains explicit inline instruction: "Yes -- GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers." The cell body is the explicit instruction. **PASS.**

**V-05:** Same as V-04 in the table layer, plus preamble instruction and manifest TOKEN propagation column. Maximum redundancy -- all three declaration locations carry the instruction. **PASS.**

---

### C-31 Decisive Analysis

**C-31 test:** Consulting ONLY GATE-0's REQUIRED OUTPUTS table in isolation, a reader can identify: (1) declaration -- TOKEN is committed in this gate, and (2) propagation contract -- committed value substitutes `[TOKEN]` in GATE-1+ column headers.

**V-01:** GATE-0 table has 2 rows: DOMAIN-TERMS (No) and TOKEN ("Yes -- committed value declared here"). Declaration present. Propagation contract: absent from table -- the substitution rule is in the preamble only. Consulting the table in isolation yields declaration but not propagation. The table is incomplete as a standalone contract. **FAIL.**

**V-02:** GATE-0 table has 3 rows: DOMAIN-TERMS (No), TOKEN ("Yes -- committed value declared in this gate"), and a dedicated Propagation contract row ("Contract -- readable from this table in isolation" with full substitution rule and before->after example). Declaration in row 2; propagation contract in row 3 -- both readable from GATE-0's table without reading any prose. **PASS.**

**V-03:** C-30 fails -> C-31 is scored 0 by dependency. **FAIL (dependency).**

**V-04:** GATE-0 table has 2 rows: DOMAIN-TERMS (No) and TOKEN with full propagation in Yes-cell: "Yes -- GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers." A single cell co-locates both declaration ("GATE-0 commits declared value") and propagation contract ("committed value substitutes `[TOKEN]` in all GATE-1+"). C-31 says "row or cell" -- both forms satisfy. Compact form is the minimal compliant pattern. **PASS.**

**V-05:** GATE-0 table TOKEN row Yes-cell identical to V-04. Same mechanism, same result. Preamble instruction and manifest column are additive but the table layer alone satisfies C-31. **PASS.**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational (A/23) | Composite |
|-----------|-----------|-------------|---------------------|-----------|
| V-01 | 60 | 30 | 22/23 = 9.565 | **99.565** |
| V-02 | 60 | 30 | 23/23 = 10.000 | **100.000** |
| V-03 | 60 | 30 | 21/23 = 9.130 | **99.130** |
| V-04 | 60 | 30 | 23/23 = 10.000 | **100.000** |
| V-05 | 60 | 30 | 23/23 = 10.000 | **100.000** |

**Ranking:** V-02 = V-04 = V-05 = **100** > V-01 = **99.565** > V-03 = **99.130**

All variations meet the golden threshold (5/5 essential pass, composite >= 90).

---

## Excellence Signals

**Top-scoring variations: V-02, V-04, V-05**

The decisive patterns separating 100 from sub-100:

**Signal 1 -- Propagation contract inside GATE-0's REQUIRED OUTPUTS table (C-31)**
C-31's "from the table in isolation" clause is a structural isolation test: the propagation contract must be physically inside the table. Preamble placement (V-01) satisfies C-30 (mechanism declared somewhere) but fails C-31 (table cannot be consulted in isolation to find the contract). Two compliant table forms confirmed: dedicated propagation row (V-02, verbose) and TOKEN row Yes-cell with inline contract (V-04/V-05, compact). The "row or cell" formulation is a non-ranking disjunction -- both forms pass C-31 equally.

**Signal 2 -- Compact form: TOKEN row cell as minimal C-31 compliant pattern (V-04)**
V-04 confirms a single Yes-cell can carry both declaration ("GATE-0 commits declared value") and propagation contract ("committed value substitutes `[TOKEN]` in all GATE-1+") without a dedicated third row. The compact form adds zero rows while fully satisfying C-31. Preferred over the verbose form when minimalism is valued; V-02's dedicated row form is equally valid and structurally clearer for human inspection.

**Signal 3 -- Bracket notation is necessary but not sufficient for C-30 (V-03 failure mode)**
V-03 isolates the "with an explicit substitution instruction" clause as an independent gate. `[TOKEN]` achieves the C-29 outcome (model substitutes on execution via convention) but does not constitute a declaration. A template using `[TOKEN]` throughout while silent on mechanism is structurally plausible but declaratively incomplete -- the "why" of substitution is absent. C-30 requires the mechanism to be stated, not merely implied by convention.

**Signal 4 -- Manifest TOKEN propagation column as additive quality layer beyond C-31 (V-05)**
V-05's manifest `TOKEN propagation` column specifies per-gate TOKEN inheritance state at the architecture level. A reader consulting only the manifest sees the full TOKEN propagation chain before reading any gate. No current criterion scores this pattern, but it represents a candidate for a future C-32: "Execution manifest declares per-gate TOKEN propagation state as a dedicated manifest column -- architecture-level TOKEN contract visible before any gate executes."

**R11 decisive learnings:**
1. C-31 boundary confirmed: preamble placement of the substitution instruction satisfies C-30 but not C-31. The table must be a self-contained specification -- declaration AND propagation contract, both readable from the table in isolation.
2. V-04 = V-02 = 100 confirmed: compact TOKEN row cell and verbose dedicated propagation row satisfy C-31 equally. "Row or cell" is not a ranking.
3. V-03 isolation confirmed: `[TOKEN]` bracket notation without instruction fails C-30. Bracket syntax is necessary but not sufficient -- "with an explicit substitution instruction" is independently required.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["compact TOKEN row cell as minimal C-31 compliant pattern -- declaration and propagation co-located in single Yes-cell without dedicated third row; V-04 is the preferred minimal form over V-02 verbose row", "manifest TOKEN propagation column declaring per-gate TOKEN inheritance state at architecture level -- additive quality layer beyond per-gate tables; candidate for C-32"]}
```
