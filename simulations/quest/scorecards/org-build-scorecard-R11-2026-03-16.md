## org-build — Round 11 Scoring (Rubric v8)

---

### Preamble: R11 Targeting

Both new criteria (C-27, C-28) require precise structural placement:
- **C-27** requires the count-floor binding to live as an explicit Phase 1 conditional inside the instruction body, not as preamble text or Phase 2 default
- **C-28** requires `PHASE-ORDERING-GUARD:` to be the structurally first *field inside* the record block, not a preamble assertion claiming unification

---

### Criterion-by-Criterion Scoring

#### Essential (C-01 – C-05)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-01 | PASS | PASS | PASS | PASS | PASS | org-chart.md with Section 1 ASCII diagram; all 9 sections in every variation |
| C-02 | PASS | PASS | PASS | PASS | PASS | Five fields mandated; FORBIDDEN any missing |
| C-03 | PASS | PASS | PASS | PASS | PASS | Unconditional inclusion; FORBIDDEN omitting |
| C-04 | PASS | PASS | PASS | PASS | PASS | Count bound to T1-COUNT-FLOOR from Phase 1 record |
| C-05 | PASS | PASS | PASS | PASS | PASS | Area \| Headcount \| Key Roles \| Decides \| Escalates; FORBIDDEN missing or merging |

**Essential sub-total: 5/5 all variations**

---

#### Recommended (C-06 – C-08)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-06 | PASS | PASS | PASS | PASS | PASS | Min 2 area subdirs; FORBIDDEN flat layout |
| C-07 | PASS | PASS | PASS | PASS | PASS | 3 rhythm rows (ROB + shiproom + governance); charters with Quorum `N of M` |
| C-08 | PASS | PASS | PASS | PASS | PASS | FLAT-CASE-PRESSURE from closed set; single CAN-OPERATE-FLAT/STRUCTURE-WARRANTED verdict |

**Recommended sub-total: 3/3 all variations**

---

#### Aspirational (C-09 – C-28)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence summary |
|----|------|------|------|------|------|-----------------|
| C-09 | PASS | PASS | PASS | PASS | PASS | Row 1 = headcount threshold; Row 2 = different category; FORBIDDEN two headcount rows |
| C-10 | PASS | PASS | PASS | PASS | PASS | `[element name] (cat-N) --` required; FORBIDDEN plain prose; FORBIDDEN wrong codes |
| C-11 | PASS | PASS | PASS | PASS | PASS | T1-IA-SCOPE-KEY selected in Phase 1 from T1-PRESSURE; consumed by Phase 2 via named gate variable |
| C-12 | PASS | PASS | PASS | PASS | PASS | CAN-OPERATE-FLAT → cat-2/cat-3; STRUCTURE-WARRANTED → cat-1/cat-4; derivation explicit per path |
| C-13 | PASS | PASS | PASS | PASS | PASS | "Only one verdict. Both is an error. Neither is an error." + FORBIDDEN directives in all |
| C-14 | PASS | PASS | PASS | PASS | PASS | Named typed outputs at every gate; downstream phases declare input contracts by variable name |
| C-15 | PASS | PASS | PASS | PASS | PASS | Bidirectional: "Both is an error. Neither is an error." + FORBIDDEN both + FORBIDDEN omitting |
| C-16 | PASS | PASS | PASS | PASS | PASS | MUST contain specific remediation action; FORBIDDEN format instructions in Mitigation cells |
| C-17 | PASS | PASS | PASS | PASS | PASS | Verbatim template text provided per key; FORBIDDEN paraphrase; FORBIDDEN composition |
| C-18 | PASS | PASS | PASS | PASS | PASS | Explicit FORBIDDEN for wrong category set per verdict path in all variations |
| **C-19** | **FAIL** | **FAIL** | **FAIL** | **PASS** | **FAIL** | V-04 only: CONSTRAINT REGISTER declaration + uniform MUST on every phase step. V-01/V-02/V-03/V-05: bare imperatives ("Assign", "Select", "Document") without MUST in Phase 1 steps — no register declaration to establish the requirement |
| C-20 | PASS | PASS | PASS | PASS | PASS | All phase gates declare typed outputs; all consuming phases have explicit input contracts |
| C-21 | PASS | PASS | PASS | PASS | PASS | MUST/FORBIDDEN governs every gate variable in its consuming phase's input contract |
| **C-22** | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** | V-04 and V-05: IA role file skeleton with `{{T1-IA-SCOPE-KEY-TEMPLATE}}` slot directly keyed to Phase 1 gate variable; FORBIDDEN any deviation. V-01/V-02/V-03: no pre-print skeleton |
| C-23 | PASS | PASS | PASS | PASS | PASS | Per-boundary ordering FORBIDDEN in phase instructions at every phase transition |
| C-24 | PASS | PASS | PASS | PASS | PASS | Named record blocks at every gate; filled values materialize checkpoint state |
| C-25 | PASS | PASS | PASS | PASS | PASS | Outbound: FORBIDDEN in phase instructions + PHASE-ORDERING-GUARD in block; Inbound: INBOUND CONTRACT with FORBIDDEN at every consuming phase |
| C-26 | PASS | PASS | PASS | PASS | PASS | PHASE-ORDERING-GUARD structurally first field; gate schema + ordering anchor + materialization all present in one construct (V-05 adds per-block commentary making unification explicit) |
| **C-27** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | All variations encode T1-DEPTH-FLAG → T1-COUNT-FLOOR as explicit Phase 1 conditional inside instruction body; FORBIDDEN placing binding outside Phase 1; FORBIDDEN flat count range — R11 target fully closed |
| **C-28** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | `PHASE-ORDERING-GUARD:` is structurally first field in every `=== RECORD: PHASE-N ===` block in all variations — R11 target fully closed |

**Aspirational sub-totals:**

| Variation | Failures | Aspirational Pass |
|-----------|----------|-------------------|
| V-01 | C-19, C-22 | 18/20 |
| V-02 | C-19, C-22 | 18/20 |
| V-03 | C-19, C-22 | 18/20 |
| V-04 | none | 20/20 |
| V-05 | C-19 | 19/20 |

---

### Composite Scores

Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/20 × 10)`

| Variation | Essential | Recommended | Aspirational | **Score** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60.0 | 30.0 | 9.0 | **99.0** |
| V-02 | 60.0 | 30.0 | 9.0 | **99.0** |
| V-03 | 60.0 | 30.0 | 9.0 | **99.0** |
| **V-04** | 60.0 | 30.0 | **10.0** | **100.0** |
| V-05 | 60.0 | 30.0 | 9.5 | **99.5** |

**Ranking: V-04 (100.0) > V-05 (99.5) > V-01 = V-02 = V-03 (99.0)**

---

### C-27 / C-28 Closure Verification

Both new criteria pass across all five variations. The R11 hypothesis held:

| Criterion | Mechanism | Status |
|-----------|-----------|--------|
| C-27 | Phase 1 conditional binding T1-DEPTH-FLAG → T1-COUNT-FLOOR with explicit FORBIDDEN placement guards | Fully closed in all 5 |
| C-28 | `PHASE-ORDERING-GUARD:` as structurally first field inside every record block | Fully closed in all 5 |

R11 closes the R10 ceiling for both criteria.

---

### Why V-01 = V-02 = V-03 (99.0)

The three single-axis variations achieve identical scores. Their differentiating features:
- **V-02** adds a prompt-open RECORD BLOCK ARCHITECTURE declaration explaining *why* the guard is first (makes C-28 a schema property, not just an instance property)
- **V-03** adds T1-NAMED-FAILURE as a gate variable (grounds the assessment in a concrete coordination failure) and T4-KEY-MATCH verification (traces template key application end-to-end)

Neither addition closes C-19 (no uniform MUST register) or C-22 (no pre-print skeleton), leaving all three tied at 99.0.

---

### Why V-05 Outscores V-01/V-02/V-03 (99.5)

V-05 adds the IA role file skeleton with `{{T1-IA-SCOPE-KEY-TEMPLATE}}` — a slot directly keyed to a Phase 1 gate variable, closing C-22. This gains 0.5 points. V-05 does not declare a CONSTRAINT REGISTER, leaving bare imperatives ("Assign", "Select", "Document") in Phase 1 without MUST prefixes — C-19 fails.

---

### Why V-04 Is the Top Scorer (100.0)

V-04 closes both C-19 and C-22 that no other variation closes simultaneously:

**C-19 closure mechanism (CONSTRAINT REGISTER):** "Every rule in this prompt uses MUST (required) or FORBIDDEN (prohibited). Advisory language — 'should', 'prefer', 'typically', 'consider' — does not appear in constraint contexts." This declaration, combined with `MUST classify:`, `MUST bind count floor:`, `MUST assign from the closed set:`, `MUST write exactly one verdict:`, `MUST select the verbatim template:` throughout, achieves uniform imperative register across all phase instructions. The register is declared once architecturally and verified per-instruction.

**C-22 closure mechanism (IA skeleton with gate-variable slots):** Pre-print IA role file skeleton with `{{T1-IA-SCOPE-KEY-TEMPLATE}}` slot explicitly keyed to T1-IA-SCOPE-KEY, plus `FORBIDDEN: any deviation from the verbatim template text when filling this slot.` A reader who knows only T1-IA-SCOPE-KEY can fill the scope slot without ambiguity — the pass condition is satisfied exactly.

**Additional architectural strength:** V-04 adds a schema-level FORBIDDEN on the record block format itself: "FORBIDDEN: any record block that does not begin with PHASE-ORDERING-GUARD as its first field." This converts C-28 from a per-instance instruction to a structural invariant declared at the architecture level.

---

### Excellence Signals (from V-04)

1. **CONSTRAINT REGISTER pattern**: Declaring the register once at prompt open (`CONSTRAINT REGISTER: Every rule in this prompt uses MUST or FORBIDDEN`) unifies C-19 compliance at the schema level — the register is the architectural contract, individual MUST directives are evidence of compliance. This is more reliable than per-instruction advisory-language audits.

2. **Pre-print skeleton with gate-variable slot**: The IA skeleton printed after Phase 1's gate output makes the template selection concrete before Phase 2 executes — `{{T1-IA-SCOPE-KEY-TEMPLATE}}` is the named slot, the verbatim map is the slot vocabulary, the FORBIDDEN on deviation is the enforcement. C-22 is satisfied by showing the artifact shape, not just asserting verbatim requirements.

3. **Schema-level architectural FORBIDDEN**: Adding "FORBIDDEN: any record block that does not begin with PHASE-ORDERING-GUARD as its first field" in the prompt-open RECORD BLOCK ARCHITECTURE converts C-28 from "each block happens to have the guard first" to "the format itself requires it" — architectural constraint, not instance-level guidance.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
