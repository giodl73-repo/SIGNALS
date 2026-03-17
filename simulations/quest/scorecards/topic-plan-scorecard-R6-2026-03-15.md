## Round 6 — topic:plan Scorecard (rubric v6, C-01–C-26)

**Variations read**: V-01 through V-05. Trace artifact: placeholder (scoring from structural analysis of skill text).

---

### Per-Criterion Analysis

#### Essential (C-01–C-05)

All five variations inherit the R5 V-05 base. Every essential criterion is structurally present across all variations.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-01 | PASS | PASS | PASS | PASS | PASS | Phase 0 reads `simulations/TOPICS.md` to find strategy file; Phase 1 reads strategy.md with VERBATIM EVIDENCE BLOCK |
| C-02 | PASS | PASS | PASS | PASS | PASS | Schema C mandates all 9 namespace rows; zero-counts; NEVER ABSENT |
| C-03 | PASS | PASS | PASS | PASS | PASS | PROPOSAL SCOPE block + delta count sentence; PRIOR artifacts blocked from proposals |
| C-04 | PASS | PASS | PASS | PASS | PASS | Schemas E and F; labeled null declarations per type (ADDITIONS/REMOVALS/REPRIORITIZATIONS) |
| C-05 | PASS | PASS | PASS | PASS | PASS | Phase 6 PENDING CONFIRMATION block with YES/NO/REVISED; Gate 6 holds until user replies |

**Essential: 5/5 all variations.**

---

#### Recommended (C-06–C-08)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-06 | PASS | PASS | PASS | PASS | PASS | "Evidence artifact" column in Schemas E and F; required per proposal row |
| C-07 | PASS | PASS | PASS | PASS | PASS | Schema G: Before/After/Schema A ref/Proposal ref |
| C-08 | PASS | PASS | PASS | PASS | PASS | `vs. NO CHANGE -- MANDATORY` column in Schemas E and F; "name a specific consequence" |

**Recommended: 3/3 all variations.**

---

#### Aspirational (C-09–C-26)

| ID | Criterion summary | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-------------------|------|------|------|------|------|
| C-09 | Type-labeled null declarations | PASS | PASS | PASS | PASS | PASS |
| C-10 | Conflict detection in own numbered phase | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-11 | Required-cell table schemas | PASS | PASS | PASS | PASS | PASS |
| C-12 | In-phase stop gates | PASS | PASS | PASS | PASS | PASS |
| C-13 | Mandatory column header label | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-14 | Explicit placeholder tokens `??`/`--` | PASS | PASS | PASS | PASS | PASS |
| C-15 | Counted-total delta summary | PASS | PASS | PASS | PASS | PASS |
| C-16 | Hedge-phrase disqualification | PASS | PASS | PASS | PASS | PASS |
| C-17 | Two-tier sentinel vocabulary | PASS | PASS | PASS | PASS | PASS |
| C-18 | Pre-signal defense register | PASS | PASS | PASS | PASS | PASS |
| C-19 | Integer-enforcement gate language | PASS | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-20 | Sequential phase-linked stop gates | PASS | PASS | PASS | PASS | PASS |
| C-21 | Vocabulary contract violation enumeration | PASS | PASS | PASS | PASS | PASS |
| C-22 | Row-number anchor citation | PASS | PASS | PASS | PASS | PASS |
| C-23 | Verbatim-quoted banned forms | PASS | PASS | PASS | PASS | PASS |
| C-24 | Cell-level banned-forms check instruction | **PASS** | **FAIL** | **FAIL** | **PASS** | **PASS** |
| C-25 | Banned-forms scope propagation | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| C-26 | Gate-0 pre-signal stop gate | **FAIL** | **FAIL** | **PASS** | **FAIL** | **PASS** |

**Evidence notes for new criteria:**

**C-10 PARTIAL all**: Schema H is embedded in Phase 5 body, not its own numbered phase; typed null form (`CONFLICT DETECTION -- NULL`) present. Both halves of C-10 don't satisfy.

**C-13 PARTIAL all**: `vs. NO CHANGE -- MANDATORY` header ✓ in Schemas E/F. "Defense defeated (Row D-R-N)" header does not carry `MANDATORY`. Enforcement is in a post-header paragraph ("A named defense without a row number does not satisfy that column"), not in the column header itself. Pre-existing gap from R5.

**C-19 PARTIAL in V-02/V-03/V-04**: Phase 2 says "Non-integer values are a gate failure" without naming the specific banned forms inline. BANNED OUTPUT FORMS preamble lists "a few", "several", "some" etc. but the gate-failure rule and the named forms are separated. V-01 and V-05 have "Writing 'a few', 'several', 'some', or any non-integer value is a gate failure" as a unified inline rule — C-19 requires the rule itself to name the forms.

**C-24 PASS V-01/V-04/V-05**: Labeled `(CELL-LEVEL CHECK: before writing each vs. NO CHANGE cell in Schema E or F, check it against the BANNED OUTPUT FORMS list above. Any match disqualifies the row. Do not present the cell before completing the check.)` block placed between Schema D and Schema E headers — instruction is at the schema boundary, not buried in phase fill list. V-02 and V-03 have per-row fill instructions in Phase 5 body ("check against BANNED OUTPUT FORMS before presenting") but no labeled block at the schema boundary.

**C-25 PASS V-02/V-04/V-05**: Each null declaration template carries inline banned-forms check instruction with verbatim banned strings: "check this reason against BANNED OUTPUT FORMS before writing; 'no new signals', 'nothing to add', 'no changes needed', 'not applicable' are banned; any match fails this declaration." V-01 and V-03 list banned phrases for null cells in the preamble but null declaration templates are plain ("ADDITIONS: none -- [reason]") with no inline check.

**C-26 PASS V-03/V-05**: Both have PRE-COMMIT BLOCK reproduced before Phase 0 action: "No artifact may be read — not strategy.md, not any signal file in simulations/ — until Schema DR is committed in writing and Gate 0 passes with STATUS: PASS." Gate 0 closes with "Do not advance to Phase 1 and do not read any signal artifact until this gate shows STATUS: PASS." V-01, V-02, V-04 have Gate 0 linked in the sequential chain but no read-barrier declaration before Phase 0 actions.

---

### Composite Scores

Formula: `(5/5 × 60) + (3/3 × 30) + (aspirational/18 × 10)` | PARTIAL = 0.5

| Variation | Aspirational full | Aspirational ×0.5 | Aspirational ×0 | Asp. equiv. | Asp. (/18×10) | Total |
|-----------|------------------|-------------------|-----------------|-------------|---------------|-------|
| V-01 | 14 (C-09,11,12,14,15,16,17,18,19,20,21,22,23,24) | 2 (C-10,13) | 2 (C-25,26) | 15.0 | 8.33 | **98.33** |
| V-02 | 13 (C-09,11,12,14,15,16,17,18,20,21,22,23,25) | 3 (C-10,13,19) | 2 (C-24,26) | 14.5 | 8.06 | **98.06** |
| V-03 | 13 (C-09,11,12,14,15,16,17,18,20,21,22,23,26) | 3 (C-10,13,19) | 2 (C-24,25) | 14.5 | 8.06 | **98.06** |
| V-04 | 14 (C-09,11,12,14,15,16,17,18,20,21,22,23,24,25) | 3 (C-10,13,19) | 1 (C-26) | 15.5 | 8.61 | **98.61** |
| V-05 | 16 (C-09,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26) | 2 (C-10,13) | 0 | 17.0 | 9.44 | **99.44** |

**Ranking**: V-05 (99.44) > V-04 (98.61) > V-01 (98.33) > V-02 = V-03 (98.06)

---

### Excellence Signals — V-05

**1. Three standing contracts, each self-enforcing at their point of production**
V-05 is the only variation where all three enforcement mechanisms fire before the cell is written rather than at a downstream gate:
- Gate 0 read barrier (PRE-COMMIT BLOCK) fires before any Phase 0 action
- Proposal column check (CELL-LEVEL CHECK block) fires before Schema E/F fill
- Null declaration reason check (inline template instruction) fires inside each declaration template

The architectural shift: violations can't be produced and then caught — they're blocked at the write surface.

**2. PRE-COMMIT BLOCK as a reproduced output artifact**
The model must reproduce the PHASE 0 PRE-COMMIT block verbatim before taking any action. This makes the constraint auditable in the output — a reviewer can confirm the commitment was made without reading prose for intent. The block is a structured deliverable, not a guideline.

**3. Defense argument escape hatch closed at Phase 0**
V-05 Phase 0 adds: "check each defense argument against the BANNED OUTPUT FORMS list before writing." This extends the banned-forms check into the defense register argument cells. No prior criterion covers this: C-24 covers proposal columns, C-25 covers null declaration reason cells, but defense arguments in Schema DR are pre-committed free text that could contain hedge phrases without any criterion blocking them. V-05 closes this gap in the pre-commit phase itself.

---

### New Pattern Not Captured by C-01–C-26

V-05 applies the banned-forms check instruction to **Phase 0 defense argument cells** — the free-text "Current defense argument" cells in Schema DR. This is structurally distinct from:
- C-24: covers proposal columns (Schema E/F vs. NO CHANGE cells)
- C-25: covers null declaration reason cells (Phase 5 typed nulls)
- C-26: covers the Gate 0 read barrier itself

A defense register argument containing "no compelling reason to change" would pass C-24 and C-25 without violation, but would contaminate the pre-commitment that proposals must defeat. V-05 closes this by requiring defense arguments to pass the banned-forms check at fill time.

---

```json
{"top_score": 99.44, "all_essential_pass": true, "new_patterns": ["Phase 0 defense register argument cells subject to banned-forms check instruction at fill time — banned-forms scope extended to pre-committed defense arguments in Schema DR, closing the free-text escape hatch not covered by C-24 (proposal columns) or C-25 (null declaration reason cells)"]}
```
