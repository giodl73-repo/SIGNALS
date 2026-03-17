## flow-lifecycle Round 15 — Scoring Report (Rubric v15)

### Reading Summary

All five variations share the complete R14 V-05 floor (C-01 through C-47 as invariants). The R15 probe is two new criteria: **C-48** (per-field anti-pattern tokens in SQ Declaration field definitions) and **C-49** (mutual-audit relationship named as design principle in Status-Quo Gap column header). Denominator: 49.

---

### Essential Criteria (C-01–C-05) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 State Transition Coverage | PASS | PASS | PASS | PASS | PASS |
| C-02 Exception Flow Traces | PASS | PASS | PASS | PASS | PASS |
| C-03 Terminal State Completeness | PASS | PASS | PASS | PASS | PASS |
| C-04 Bottleneck and Gap Identification | PASS | PASS | PASS | PASS | PASS |
| C-05 Domain Role Assignment | PASS | PASS | PASS | PASS | PASS |

**All essential criteria pass in all variations.**

---

### Floor Criteria C-06–C-26, C-28–C-30, C-32–C-47 (R14 Floor Invariants)

All five variations carry the full R14 V-05 floor for these criteria. **PASS across all variations** — no deviation detected in schema structure, gate coverage, typed escape codes, or the SQ Declaration + Phase Index pairing.

---

### Discriminating Criteria

#### C-19 — Artifact-Level Production Gate (range completeness)

| V-01 | V-02 | V-03 | V-04 | V-05 |
|:----:|:----:|:----:|:----:|:----:|
| PASS | PASS | PASS | PASS | PARTIAL |

**V-05 evidence (partial):** Production gate reads `"Coverage Scan shows PASS for AC-01 through AC-23"` (line 1576) but the V-05 scan contains AC-24 (Group B, Step 2 column header). Gate range is one row short; AC-24 is not formally required to pass before the artifact is written. C-19 pass condition requires "gate text names the scan artifact and the required status condition" covering all verification rows. V-05 fails this for AC-24 specifically. **Score: 0.5**

**All other variations:** V-01 stops at AC-23 (complete for that scan), V-02 explicitly names "AC-01 through AC-24" (line 681) — correct. V-03 and V-04 stop at AC-22 (complete for those scans). No stale-range issue in V-01/V-02/V-03/V-04.

---

#### C-27 — Scan-Table Defect Taxonomy (gate reference by name)

| V-01 | V-02 | V-03 | V-04 | V-05 |
|:----:|:----:|:----:|:----:|:----:|
| PASS | PASS | FAIL | FAIL | PASS |

**V-03 evidence (fail):** Production gate text (lines 976–978): `"Write the artifact only after Coverage Scan shows PASS for AC-01 through AC-22 AND Check V shows CLOSED. An artifact written while any row shows FAIL must be discarded and rerun from the failing step."` — no reference to "Defect Type column" by name. C-27 pass condition requires the gate sentence to name the column. **Score: 0**

**V-04 evidence (fail):** Production gate text (lines 1222–1224): `"Write the artifact only after Coverage Scan PASS for AC-01 through AC-22 AND Check V CLOSED. Artifact written while any row shows FAIL must be discarded and rerun from the failing step."` — same omission. **Score: 0**

**V-01/V-02/V-05:** All contain `"the artifact contains at least one defect named in the Defect Type column above"` — explicit column-name reference. PASS.

---

#### C-48 — Per-Field Anti-Pattern Vocabulary in SQ Declaration

| V-01 | V-02 | V-03 | V-04 | V-05 |
|:----:|:----:|:----:|:----:|:----:|
| PASS | PARTIAL | FAIL | PARTIAL | PASS |

**V-01 evidence (pass):** All four field rows carry inline tokens:
- Incumbent Process: `"writing 'manual process' without naming the specific tool does not count"` ×3 tokens
- FM-01: `"'error-prone,' 'inefficient,' or 'slow' does not count"` + `"does not count"` ×2
- FM-02: `"a failure mode that is a restatement, subcategory, or consequence of FM-01 is a fail"` + `"'same as FM-01 in a different phase' is a fail"`
- Inertia Driver: `"'familiarity' or 'it works well enough' without specificity does not count"` + `"Mandatory"`

**V-02 evidence (partial):** Incumbent Process and FM-01 carry inline tokens (`"does not count"`). FM-02: `"must not overlap or be a consequence of FM-01"` — positive constraint framing, no explicit "does not count" / "Mandatory" / "is a fail" token. Inertia Driver: `"the organizational, systemic, or economic reason the incumbent persists despite FM-01 and FM-02"` — pure description, no anti-pattern token. **One enforcement gap (Inertia Driver). Score: 0.5**

**V-03 evidence (fail):** SQ Declaration is a prose block above a bare table (`| Incumbent Process | |`, `| FM-01 | |` etc). Anti-pattern instructions appear in imperative directives before the table (`"Do not write 'manual process'"`) but the field definition cells themselves carry no inline tokens. C-48 pass condition requires anti-pattern vocabulary embedded inside the field definition cell. **Score: 0**

**V-04 evidence (partial):** FM-01 has `"'error-prone' or 'inefficient' does not count"` ✓. FM-02 missing explicit token. Inertia Driver: `"the organizational or economic reason the incumbent persists"` — no token. **One gap (Inertia Driver, potentially FM-02). Score: 0.5**

**V-05 evidence (pass):** All four fields carry multiple tokens:
- Incumbent Process: `"does not count"` ×3 + `"Mandatory"`
- FM-01: `"does not count"` ×2 + `"duplicate...is a fail"`
- FM-02: `"is a fail"` ×2 + explicit identifier requirement
- Inertia Driver: `"does not count"` ×2 + `"Mandatory"`

---

#### C-49 — Mutual-Audit Relationship Named as Design Principle

| V-01 | V-02 | V-03 | V-04 | V-05 |
|:----:|:----:|:----:|:----:|:----:|
| FAIL | PASS | PARTIAL | PARTIAL | PASS |

**V-01 evidence (fail):** Status-Quo Gap column header (line 174): `"these two columns audit each other: a cell with no FM-ID reference is structurally unanchored and is a fail"` — structural observation, no "design principle" / "design intent" / "by design" designation. C-49 pass condition requires framing the co-auditing behavior as intentional architectural decision, not merely describing it. **Score: 0**

**V-02 evidence (pass):** Column header (line 516): `"mutual-audit design principle: the Entry Trigger and this column are co-designed as a mutual-audit pair -- a generic DERIVED:rationale in Entry Trigger simultaneously produces a vague gap here with no FM-ID reference, making the incompleteness visible as a co-occurring defect in a single row scan; this mutual exposure is the design intent, not a coincidence of column placement"` — "mutual-audit design principle" named + "co-designed as mutual-audit pair" + "design intent" all present. **Score: 1.0**

**V-03 evidence (partial):** Introductory text before Phase Index table (lines 811–812): `"The Entry Trigger and Status-Quo Gap columns are designed to audit each other: a vague DERIVED:rationale in Entry Trigger will simultaneously produce an FM-ID-free gap in the adjacent column"` — "designed to" implies intentional architecture. But C-49 requires the column header itself to carry the designation; V-03's column header says only `"(FM-ID from SQ Declaration; prose without FM-ID is a fail)"`. Relationship noted near the table but not in the header. **Score: 0.5**

**V-04 evidence (partial):** Gate B caption (lines 1092–1094): `"The Entry Trigger and Status-Quo Gap columns form a mutual-audit pair"` — "mutual-audit pair" named in prose above the table. Column header: `"Status-Quo Gap (FM-ID from STATUS-QUO PROCESS DECLARATION; cell with no FM-ID is structurally unanchored and is a fail)"` — no design-principle designation in the header. Caption language is present but C-49 requires the header specifically. **Score: 0.5**

**V-05 evidence (pass):** Column header (lines 1332–1333): `"mutual-audit design principle: the Entry Trigger and this column are architected as a mutual-audit pair -- ... this co-exposure is the design intent of their adjacency, not a coincidence of table layout"` — "mutual-audit design principle" named; "architected as a mutual-audit pair"; "design intent of their adjacency"; "not a coincidence of table layout" (negative contrast). Three-phrase reinforcement. **Score: 1.0**

---

### Composite Scores

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01–C-18 (essential + recommended + aspirational) | 18.0 | 18.0 | 18.0 | 18.0 | 18.0 |
| C-19 Artifact-Level Production Gate | 1.0 | 1.0 | 1.0 | 1.0 | **0.5** |
| C-20–C-26 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 |
| **C-27** Scan Defect Taxonomy (gate reference) | 1.0 | 1.0 | **0.0** | **0.0** | 1.0 |
| C-28–C-47 (remaining floor) | 20.0 | 20.0 | 20.0 | 20.0 | 20.0 |
| **C-48** Per-Field Anti-Pattern Vocabulary | **1.0** | **0.5** | **0.0** | **0.5** | **1.0** |
| **C-49** Mutual-Audit Design Principle | **0.0** | **1.0** | **0.5** | **0.5** | **1.0** |
| **Total (/ 49)** | **48.0** | **48.5** | **46.5** | **47.0** | **48.5** |
| **Score (%)** | **98** | **99** | **95** | **96** | **99** |

---

### Ranking

| Rank | Variation | Score | Key Differentiators |
|------|-----------|:-----:|---------------------|
| 1 | **V-02** | 99 | C-49 PASS (design principle named) + production gate covers AC-01 through AC-24 (no C-19 partial) |
| 1 | **V-05** | 99 | C-48 PASS (all 4 fields) + C-49 PASS (three-phrase reinforcement); C-19 partial (gate range stale at AC-23) |
| 3 | **V-04** | 96 | C-27 FAIL (no gate-level Defect Type reference) + C-48/C-49 both partial |
| 4 | **V-01** | 98 | C-49 FAIL (structural observation, not design principle) |
| 5 | **V-03** | 95 | C-27 FAIL + C-48 FAIL (prose-only enforcement) + C-49 only partial |

---

### Excellence Signals from V-02 and V-05

**Signal 1 — Three-phrase design principle reinforcement (V-05):** The strongest C-49 formulation uses three distinct framings in a single column header: (1) principle name (`"mutual-audit design principle"`), (2) architectural metaphor (`"architected as a mutual-audit pair"`), (3) negative contrast (`"not a coincidence of table layout"`). V-02 uses two framings. The triple form closes both ambiguous-description failure and single-phrase-only enforcement simultaneously.

**Signal 2 — Production gate AC-ID range completeness (V-02 advantage over V-05):** V-02 explicitly names `"AC-01 through AC-24"` in the production gate, matching the actual scan row count. V-05 names `"AC-01 through AC-23"` after AC-24 was added — a stale upper bound that silently excludes the newest check from the gate's enforcement. The practice of explicitly naming the highest AC-ID and updating it when new checks are added is the excellence signal: gate range must track scan row count.

**Signal 3 — Inertia Driver as highest-priority C-48 target (gap in V-02 and V-04):** Both V-02 and V-04 pass C-48 partially because the Inertia Driver field lacks anti-pattern vocabulary, while FM-01 and FM-02 have it. The Inertia Driver is the field most susceptible to vague content ("familiarity," "it works well enough"). V-05 closes this by requiring both category exclusion (`"'familiarity'...does not count"`) and universality exclusion (`"a reason that applies equally to all legacy processes does not count"`) in the Inertia Driver field definition — the only field needing two distinct anti-pattern vectors to close its ambiguity surface.

---

### New Patterns Not Yet Encoded as Criteria

**Pattern 1 — Production gate AC-ID range staleness:** When a new coverage scan row (AC-N+1) is added beyond the existing gate's declared range (`"AC-01 through AC-N"`), the gate silently excludes the new check. The gate exists, the scan row exists, but the gate does not require the new row to pass. This produces a C-19 partial even when all other gate elements are well-formed. The fix is either to update the explicit upper bound to the new highest AC-ID or to replace the numeric range with group-level language (`"all Coverage Scan rows"`). V-05 demonstrates this defect; V-02 demonstrates the fix.

**Pattern 2 — Inertia Driver dual-vector anti-pattern requirement:** The Inertia Driver field has a two-surface ambiguity: authors may write vague motivation descriptions (`"familiarity"`) or accurate-but-generic statements that apply universally (`"change management overhead"`). A single "does not count" token closes only one surface. The Inertia Driver specifically requires two tokens: one excluding named vague motivators and one excluding statements that would apply to any legacy process replacement. V-01 and V-05 achieve this dual-vector enforcement; V-02 and V-04 leave the Inertia Driver partially exposed. This is a field-specific sub-criterion within C-48 that may warrant a dedicated criterion.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Production gate AC-ID range staleness: when a new coverage scan row is added beyond a gate's declared upper-bound range, the gate silently excludes the new check — gate ranges must track the actual highest AC-ID or use group-level language", "Inertia Driver dual-vector anti-pattern requirement: the Inertia Driver field requires two distinct anti-pattern tokens — one excluding named vague motivators and one excluding universally-applicable statements — because a single token closes only one ambiguity surface"]}
```
