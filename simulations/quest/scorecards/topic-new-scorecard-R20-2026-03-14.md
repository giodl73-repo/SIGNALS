## Round 20 — Scoring: topic-new (v18 rubric, 51 aspirational criteria)

---

### Criterion Analysis

**Key structural facts established before scoring:**

1. R19 V-05 satisfied C-09–C-57 (49 criteria) + C-59 (already present) = 50/51. Only gap: C-58.
2. C-58 requires IR-NN → instrument class (controlled vocabulary: schema/gate/exit condition), not prose descriptions.
3. C-59 requires PCR header to assert "FER coverage is auditable by structural inspection of this table, not by content inference" — a present-tense property declaration, not a prohibition.

---

### Per-Criterion Differences Between Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **Base** | R19 V-01 (minimal) | R19 V-04 | R19 V-05 | R19 V-04 | R19 V-05 |
| **C-49** — override mission declaration | PASS | PASS | PASS | PASS | PASS |
| **C-54** — BEFORE/AFTER trajectory table per FER | FAIL — flat two-column, no sequential-path rows | PASS — 4-row SEQUENTIAL/INDEPENDENT PATH table | PASS | PASS | PASS |
| **C-55** — PCR cross-cites FER-NN | FAIL — no FER citations in PCR | PASS | PASS | PASS | PASS |
| **C-56** — enumeration sentence in opener | PASS | PASS | PASS | PASS | PASS |
| **C-57** — PCR FER coverage exhaustively declared | FAIL — no no-FER notes | PASS | PASS | PASS | PASS |
| **C-58** — instrument-class mapping table | PASS — two-column replace | FAIL — description column only | PASS — three-column supplement | PASS — two-column replace | PASS — three-column supplement |
| **C-59** — PCR header auditability assertion | FAIL — basic header | PASS — present-tense declaration | PASS | PASS | PASS |

**C-49 note for V-01/V-04 (replace form):** V-01/V-04 opener — "The defaults being overridden by this skill: IR-01, IR-02, IR-03, IR-04, IR-05. Every block that follows exists to prevent these defaults from applying." — satisfies C-49's pass condition (override-mission declaration present) even without a description column. No regression.

**C-54 detail for V-01:** The variation design notes explicitly state "no BEFORE/AFTER." V-01's FER table uses a flat `ID | Phase | wrong | catches` row format — the sequential-treatment TRAJECTORY (row-count-check-PASSES then column-completeness-SKIPPED then Result) is not shown as separate rows. C-54 requires "structural contrast makes the failure-to-correct trajectory visible by column inspection" — this requires the trajectory rows. FAIL.

---

### Full Aspirational Criterion Pass Count

**Criteria shared across all variations (C-09 through C-53, C-56):** All 5 variations carry the full structural apparatus from earlier rounds — command register (C-51, C-53), INERTIA REGISTER with Stakeholder Most Harmed column (C-46), per-phase verbatim exit (C-44), no inline prose constraints (C-45), priority column leftmost (C-31), PCR-NN IDs (C-48), two-tier consequence columns (C-20), pipeline prohibition clause (C-50), schema row IDs at multiple boundaries (C-27), etc. All PASS for all variations.

**Criteria differentiating variations:** C-54, C-55, C-57, C-58, C-59.

---

### Variation Scorecard

**V-01 — C-58 instrument-class only, minimal base (R19 V-01)**

| ID | Result | Evidence |
|----|--------|----------|
| C-54 | FAIL | Flat two-column FER table; no SEQUENTIAL PATH / INDEPENDENT PATH row trajectory; variation design notes confirm "no BEFORE/AFTER" |
| C-55 | FAIL | PCR has no FER-NN citations in consequence column |
| C-56 | PASS | "The defaults being overridden by this skill: IR-01, IR-02, IR-03, IR-04, IR-05" — enumeration sentence present |
| C-57 | FAIL | PCR has no exhaustive "No FER entry" notes; silent omissions structurally indistinguishable from missing citations |
| C-58 | PASS | Two-column table: `IR-NN | Override Instrument Class` with controlled vocabulary (gate/schema) |
| C-59 | FAIL | PCR header is basic — no auditability assertion |
| C-09 through C-53 (excl C-54) | PASS | Command register, INERTIA REGISTER, per-phase overrides, exit gates, schemas, pipeline overview all present |

**Gaps: C-54, C-55, C-57, C-59 = 4 failures**
**Passes: 47/51**
**Score: 47/51 × 10 = 9.22**

---

**V-02 — C-59 auditability declaration only (R19 V-04 base)**

| ID | Result | Evidence |
|----|--------|----------|
| C-54 | PASS | FER-01/FER-02 each use 4-row SEQUENTIAL PATH / INDEPENDENT PATH comparison table showing output state, row-count check, column-completeness, result |
| C-55 | PASS | PCR-01 cites FER-01, PCR-02 cites FER-02 |
| C-56 | PASS | Enumeration sentence present in opener |
| C-57 | PASS | PCR-03 and PCR-04 carry explicit "No FER entry ([reason])" notes |
| C-58 | FAIL | OVERRIDE MISSION table has description column only ("What This Skill Overrides It With") — no instrument-class column |
| C-59 | PASS | PCR header: "FER coverage is auditable by structural inspection of this table, not by content inference. Every entry either cites a FER-NN ID... Silent omission is not permitted." Present-tense structural-property declaration present |
| C-09 through C-57 excl C-58 | PASS | R19 V-04 base carries all 49 criteria; C-59 added |

**Gaps: C-58 = 1 failure**
**Passes: 50/51**
**Score: 50/51 × 10 = 9.80**

---

**V-03 — C-58 as third column supplement (R19 V-05 base)**

| ID | Result | Evidence |
|----|--------|----------|
| C-49 | PASS | "These are the defaults this skill overrides: IR-01...IR-05. Every block that follows exists to prevent these defaults from applying." |
| C-54 | PASS | BEFORE/AFTER 4-row trajectory table per FER entry |
| C-55 | PASS | PCR FER-NN citations present |
| C-56 | PASS | Enumeration sentence present |
| C-57 | PASS | Exhaustive "No FER entry" notes on PCR-03/PCR-04 |
| C-58 | PASS | Three-column table: `IR-NN | What This Skill Overrides It With | Override Instrument Class` — instrument-class column uses controlled vocabulary (gate/schema); C-58 requires a structured mapping of IR-NN to instrument class, satisfied by column 3 regardless of whether column 2 (description) also exists |
| C-59 | PASS | PCR header: "Silent omission is not permitted — FER coverage is auditable by structural inspection of this table, not by content inference." Auditability assertion present |
| C-09 through C-57 + C-59 | PASS | R19 V-05 base carries all 50; C-58 added via third column |

**Gaps: none**
**Passes: 51/51**
**Score: 51/51 × 10 = 10.0**

---

**V-04 — C-58 (replace) + C-59 (R19 V-04 base)**

| ID | Result | Evidence |
|----|--------|----------|
| C-49 | PASS | "The defaults being overridden by this skill: IR-01...IR-05. Every block that follows exists to prevent these defaults from applying." — override-mission declaration present; description column not required for C-49 pass |
| C-54 | PASS | BEFORE/AFTER 4-row table per FER (R19 V-04 base carries C-54) |
| C-55 | PASS | PCR FER-NN citations present |
| C-56 | PASS | Enumeration sentence present |
| C-57 | PASS | Exhaustive "No FER entry" notes on PCR-03/PCR-04 |
| C-58 | PASS | Two-column replace-form table: `IR-NN | Override Instrument Class` — controlled vocabulary (gate/schema) |
| C-59 | PASS | PCR header: "FER coverage is auditable by structural inspection of this table, not by content inference...Silent omission is not permitted." |

**Gaps: none**
**Passes: 51/51**
**Score: 51/51 × 10 = 10.0**

---

**V-05 — Full integration (R19 V-05 + C-58 three-column supplement)**

| ID | Result | Evidence |
|----|--------|----------|
| C-49 | PASS | "These are the defaults this skill overrides: IR-01...IR-05. Every block that follows exists to prevent these defaults from applying." |
| C-54 | PASS | BEFORE/AFTER 4-row table per FER |
| C-55 | PASS | PCR FER-NN citations present |
| C-56 | PASS | Enumeration sentence present |
| C-57 | PASS | Exhaustive "No FER entry" notes present |
| C-58 | PASS | Three-column table identical to V-03: description + instrument class |
| C-59 | PASS | PCR header: "Silent omission is not permitted — FER coverage is auditable by structural inspection of this table, not by content inference." Carried unchanged from R19 V-05 |
| All other criteria | PASS | R19 V-05 base + C-58 = full 51/51 |

**Gaps: none**
**Passes: 51/51**
**Score: 51/51 × 10 = 10.0**

---

### Composite Scores and Ranking

| Variation | Aspirational Passes | Score | Essential PASS |
|-----------|---------------------|-------|----------------|
| V-05 | 51/51 | **10.00** | YES |
| V-04 | 51/51 | **10.00** | YES |
| V-03 | 51/51 | **10.00** | YES |
| V-02 | 50/51 | **9.80** | YES |
| V-01 | 47/51 | **9.22** | YES |

**All five variations pass the five essential criteria (C-01 through C-05):** artifact paths, signal fields, priority vocabulary, essential signal presence — all satisfied by the prompt template structure.

---

### Excellence Signals from Top-Scoring Variations

V-03, V-04, and V-05 all achieve 51/51. The two patterns that elevated them to ceiling:

**Pattern A — OVERRIDE MISSION three-layer completion (V-03/V-05 specific):** The three-column supplement form activates C-56 (enumeration sentence: what defaults exist), C-49 (description column: why each override is needed), and C-58 (instrument-class column: how each override is enforced) simultaneously in a single table. Description and instrument class serve distinct cognitive functions — the description answers "what does the override produce?" (narrative purpose frame); the instrument class answers "what structural mechanism enforces it?" (navigable structural map). These are additive, not substitutable: V-04 (replace form) achieves 51/51 by satisfying C-58, but loses the C-49 narrative depth that the description column carries. The three-column form is structurally complete at the OVERRIDE MISSION layer.

**Pattern B — OVERRIDE MISSION meta-closing sentence (V-03/V-05, absent in V-04):** V-03 and V-05 add a closing sentence absent from V-04: "Every schema, every gate, and every exit condition in this document is an override instrument." This generalizes C-58's instrument-class vocabulary from row-level IR-NN mapping to a document-wide blanket declaration — making "override instrument" an attribute of the entire structural apparatus, not just the five named IR-NN defaults. This is not captured by any v18 criterion (it goes beyond what C-58 requires) and is a C-60 candidate: the OVERRIDE MISSION block closes with a document-level instrument-class meta-statement that classifies all structural elements by their role type.

**V-02 vs V-01 gap confirms C-54 importance:** V-01's loss of 3 points (C-54 + C-55 + C-57 + C-59) vs V-02's loss of 1 point (C-58 only) demonstrates that the BEFORE/AFTER trajectory table (C-54) and exhaustive PCR FER coverage (C-55, C-57) are load-bearing criteria that minimal bases do not satisfy. Instrument-class-only on a minimal base is not sufficient for high scores.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Three-column OVERRIDE MISSION supplement form (IR-NN + description + instrument class) activates C-56/C-49/C-58 simultaneously without displacement — description column (narrative why) and instrument-class column (structural how) serve distinct cognitive functions and are additive; replace form satisfies C-58 but loses C-49 narrative depth; supplement form is the structurally complete OVERRIDE MISSION configuration", "OVERRIDE MISSION block closing meta-statement generalizes instrument-class vocabulary to document scope: 'Every schema, every gate, and every exit condition in this document is an override instrument' converts instrument-class from IR-NN-level row mapping to a document-level blanket classification — making override-instrument a property of the entire structural apparatus rather than a property of individual IR-NN defaults; C-60 candidate"]}
```
