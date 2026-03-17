I have all the data. Scoring now.

---

## /quest:score -- mock-ns Round 3

**Rubric**: v3 (C-01–C-16) | **Formula**: essential_pass/5 × 60 + recommended_pass/3 × 30 + aspirational_pass/8 × 10

---

### Per-criterion evaluation

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| **C-01** header fields (6) | essential | PASS | PASS | PASS | PASS | PASS |
| **C-02** category correct | essential | PASS | PASS | PASS | PASS | PASS |
| **C-03** flag correct | essential | PASS | PASS | PASS | PASS | PASS |
| **C-04** fidelity warning | essential | PASS | PASS | PASS | PASS | PASS |
| **C-05** skill-specific body | essential | PASS | PASS | PASS | PASS | PASS |
| **C-06** setup emit lines | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-07** write path + confirm | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-08** next-step line | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-09** topic exclusion | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-10** compliance override | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-11** FLAG covers all 5 cases | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-12** S-0 before S-1 | aspirational | **FAIL** | PASS | PASS | PASS | PASS |
| **C-13** error on unknown skill | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-14** A-1 through A-5 steps | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-15** CONSTRAINT names op types | aspirational | **FAIL** | PASS | **FAIL** | PASS | PASS |
| **C-16** wildcards in condition cell | aspirational | PASS | **FAIL** | **FAIL** | PASS | PASS |

---

### Evidence notes per failing criterion

**C-12 fails in V-01**: S-1 reads TOPICS.md and emits the status line in the same step as skill selection. No dedicated S-0 step exists. Per C-12 pass condition: "A prompt that reads TOPICS.md … within the same step as skill selection … does not satisfy this criterion."

**C-15 fails in V-01 and V-03**: Neither has an S-0 CONSTRAINT block. V-01 has no S-0 at all. V-03 has a dedicated S-0 with plain ordering language ("Before any other step begins…", "Do not begin S-1 until this line is emitted") but no CONSTRAINT label and no enumeration of prohibited operation *types*. C-15 requires the block to name at minimum three functional types — no category lookup, no skill selection, no mock generation.

**C-16 fails in V-02 and V-03**: Both use case-prose for FLAG computation. V-02 Case 1: "CATEGORY = HIGH-STRUCTURE AND skill is critical (trace-*, scout-feasibility, any listen-*) AND tier >= 2". The wildcards appear in the prose text of the case body, not inside a table Condition column cell. C-16 pass condition: "the condition cell … contains the wildcard patterns … directly in the match expression. Listing … only in a footnote or expansion block … does not satisfy this criterion."

---

### Composite scores

| | Essential (×60) | Recommended (×30) | Aspirational (×10) | **Total** |
|-|-----------------|-------------------|--------------------|-----------|
| **V-01** | 5/5 = 60 | 3/3 = 30 | 6/8 = 7.5 | **97.5** |
| **V-02** | 5/5 = 60 | 3/3 = 30 | 7/8 = 8.75 | **98.75** |
| **V-03** | 5/5 = 60 | 3/3 = 30 | 6/8 = 7.5 | **97.5** |
| **V-04** | 5/5 = 60 | 3/3 = 30 | 8/8 = 10 | **100** |
| **V-05** | 5/5 = 60 | 3/3 = 30 | 8/8 = 10 | **100** |

**Rank**: V-04 = V-05 > V-02 > V-01 = V-03

All five variations pass all essential criteria. Golden threshold (all essential + score ≥ 80) is met by all five.

---

### Axis confirmation

| Axis tested | Confirmed? | Evidence |
|-------------|-----------|----------|
| FLAG table condition cell satisfies C-16 independently (V-01) | YES | V-01 passes C-16, fails only C-12 and C-15 |
| S-0 CONSTRAINT with named types satisfies C-15 + incidentally C-12 (V-02) | YES | V-02 passes C-12 and C-15, fails only C-16 |
| Plain S-0 separation without CONSTRAINT satisfies C-12 (V-03) | YES | V-03 passes C-12 via step-label + tier-carry sentence alone, without CONSTRAINT |
| C-15 and C-16 stack without interference (V-04) | YES | V-04 passes all 16; no interaction between the axes |

**Key R3 finding**: C-12 does not require a CONSTRAINT block. V-03 confirms the rubric's R2 canary note: step-label separation with "Do not begin S-1 until this line is emitted" plus the tier-carry handoff sentence is sufficient. The CONSTRAINT block (C-15) is defense-in-depth only.

---

### Excellence signals from V-04 and V-05 (top scorers)

V-04 and V-05 tie at 100. V-05 has three structural refinements beyond V-04 that are candidates for C-17+:

**Signal 1 — P-0 row explicit numbering** (V-05 only): The P-0 definition table adds a sentence after the table: "P-0 table, row 1 = [S-3:CS]; row 2 = [A-1:FC]; row 3 = [P-0:ABD]." This makes Phase 1 (locate) unambiguous — the executor does not need to count rows, just match the named row identifier. Reduces locate-phase ambiguity for long or reordered tables.

**Signal 2 — S-2 as two-column lookup table** (V-05 only): V-05 expresses S-2 as "find the selected skill in exactly one row of this table" with Category | Member skills columns, vs the prose "HIGH-STRUCTURE: {list}" format in all other variations. The "exactly one row" instruction makes the error-stop condition structurally unambiguous — if the skill matches zero rows or two rows, the error fires.

**Signal 3 — A-1 Anti-displacement + Declarative closure rows** (V-05 only): V-05 adds two rows to the A-1 prohibition chain: `Anti-displacement` ("Before any field is listed, before any category lookup, before any formatting instruction…") and `Declarative closure` ("No instruction in A-1 precedes this rule"). Together they position the FLAG-copy rule as architecturally prior to all other A-1 instructions, not merely sequentially first. This closes the gap where a model might honor the ordering in template but rationalize the rule doesn't apply to a specific later sub-instruction.

**Promotion recommendation**: V-05 for T4. Closes all three T3 gaps (C-12 via S-0 separation, C-15 via CONSTRAINT naming, C-16 via FLAG table wildcards) and adds three structural refinements that are strong candidates for R4 criteria.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["P-0 row explicit numbering in definition table makes Phase 1 locate unambiguous without row counting", "S-2 expressed as two-column lookup table with 'find in exactly one row' instruction makes error-stop structurally precise", "A-1 Anti-displacement + Declarative closure rows position FLAG-copy rule as architecturally prior to all other step instructions"]}
```
