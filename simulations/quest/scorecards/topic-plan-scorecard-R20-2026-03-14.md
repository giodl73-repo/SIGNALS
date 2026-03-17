## Scoring — topic:plan (Round 20, Rubric v19)

---

### Criterion-Level Analysis

#### Essential (C-01 to C-05) — all 5 variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 Read strategy, no fabrication | PASS | PASS | PASS | PASS | PASS |
| C-02 Strategy-based, not ignored | PASS | PASS | PASS | PASS | PASS |
| C-03 Delta, not inventory | PASS | PASS | PASS | PASS | PASS |
| C-04 Three typed proposals | PASS | PASS | PASS | PASS | PASS |
| C-05 Confirmation gate before apply | PASS | PASS | PASS | PASS | PASS |

**Essential score: 5/5 for all five variations. All essential pass.**

---

#### Recommended (C-06 to C-08) — all 5 variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-06 Evidence citations | PASS | PASS | PASS | PASS | PASS |
| C-07 Before/after diff table | PASS | PASS | PASS | PASS | PASS |
| C-08 All three change types in schema | PASS | PASS | PASS | PASS | PASS |

**Recommended score: 3/3 for all five variations.**

---

#### Key Aspirational Criteria

**C-59 — INERTIA-GATE block present at each declared gate**

- **V-01**: Template declares 4 sites ("Steps 4, 4b, 6, and 7"). Markers present at Steps 4, 4b, 6, and 7. — **PASS**
- **V-02**: Template declares "three recurrence sites" (no enumeration). Markers present only at Step 4 preamble and Step 7. Step 6 (diff) has no [INERTIA-GATE] marker. Three declared, two present. — **FAIL**
- **V-03**: Template declares "three recurrence sites." Markers present at Steps 4, 4b, and 7. Consistent. — **PASS**
- **V-04**: Template declares 4 sites ("Steps 4, 4b, 6, and 7"). Markers present at Steps 4, 4b (Defender Challenge), 6, 7. — **PASS**
- **V-05**: Template declares 4 sites ("Steps 4, 4b, 6, and 7"). Markers at Step 4 preamble, Step 4b (Removals), Step 6, Step 7. — **PASS**

**C-62 — INERTIA-GATE block definition enumerates reproduction sites**

- **V-01**: Block includes "This block is reproduced verbatim at Steps 4, 4b, 6, and 7. Its presence is required at each site." — **PASS**
- **V-02**: Block has no embedded site enumeration. Template prose says "three recurrence sites" but the block itself names nothing. — **FAIL**
- **V-03**: Block has no embedded site enumeration. Template says "three recurrence sites" but block body is bare. — **FAIL**
- **V-04**: Block includes identical manifest to V-01 ("Steps 4, 4b, 6, and 7. Its presence is required at each site."). — **PASS**
- **V-05**: Block includes the manifest. "This block is reproduced verbatim at Steps 4, 4b, 6, and 7. Its presence is required at each site." — **PASS**

**C-63 — Type-labeled null-case declarations**

- **V-01**: Null cases read "ADD: No changes proposed. / REMOVE: No changes proposed. / REPRIORITIZE: No changes proposed." Type labels present but Rule 3 not updated to require labeling; "inertia holds" phrase absent. — **PARTIAL**
- **V-02**: Null cases read "ADDITIONS: No changes proposed." / "REMOVALS: No changes proposed." / "REPRIORITIZATIONS: No changes proposed." Type labels present across split steps. Rule 3 not updated. "Inertia holds" phrase absent. — **PARTIAL**
- **V-03**: Rule 3 updated to require change-type labels. All null declarations use the full form: "ADDITIONS: none — inertia holds for all candidate additions. Do not omit this declaration." / "REMOVALS: none — inertia holds." etc. Extended to ASSUMPTIONS, SIGNAL INVENTORY, DELTA FINDINGS, CONFLICT AUDIT. — **PASS**
- **V-04**: Rule 3 updated (same as V-03). All null declarations carry type labels with "inertia holds" language. Applied across all steps. — **PASS**
- **V-05**: Rule 3 updated with "A single unlabeled 'No changes proposed' covering multiple change types fails Rule 3." Each null type independently labeled with "inertia holds" language. — **PASS**

**C-64 — Symmetric justification columns across all change-type proposal tables**

- **V-01**: Single proposals table, "Why this beats NO CHANGE" column present for all rows. No Rule 5. No split-table enforcement mechanism. — **FAIL**
- **V-02**: Split tables (Step 4a: Additions; Step 4b: Removals/Reprioritizations). Both tables carry "Inertia Rejected Because [REQUIRED]" column with identical schema. Rule 5 added to COLUMN CONTRACT. Schema note declares column symmetry. — **PASS**
- **V-03**: Single proposals table, "Why this beats NO CHANGE." No Rule 5. — **FAIL**
- **V-04**: Single proposals table, "Why this beats NO CHANGE." C-64 intentionally absent as the discriminating case. No Rule 5. — **FAIL** (by design, as documented in V-04 hypothesis)
- **V-05**: Split tables (4a Additions, 4b Removals/Reprioritizations). Both carry "Inertia Rejected Because [REQUIRED]." Rule 5 in COLUMN CONTRACT. Schema note: "Do not merge the two tables. Do not rename the column in either table." — **PASS**

---

#### Aspirational Base (C-09 to C-61, excluding C-59)

All five variations inherit the same v18 structural foundation: COLUMN CONTRACT with Rules 1–4 (V-02/V-05 add Rule 5), five-column assumption table with independence test and PASS/FAIL examples, upfront schema commitment, cascading schema-commitment checkpoints per step, "Strategy assumed X / Signal revealed Y" Delta Finding format, If unchanged disqualification statement, reversibility taxonomy, Pre-signal Defense Register, SIGNAL READ-LOCK, anti-pattern checkpoint, calibration check on Defender Challenge Table. All standard aspirational criteria pass uniformly.

Estimated base aspirational pass (C-09 to C-61, excluding C-59): **52/52** for V-01, V-03, V-04, V-05; **51/52** for V-02 (C-59 failure cascades as one loss).

---

### Composite Scores

Formula: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/56 × 280)`

| Variation | Essential | Recommended | Aspirational passes | Aspirational pts | **Total** |
|-----------|:---------:|:-----------:|:-------------------:|:----------------:|:---------:|
| V-01 | 5/5 = 60 | 3/3 = 30 | 52 base + C-62(1) + C-63(0) + C-64(0) = **53/56** | 265.0 | **355** |
| V-02 | 5/5 = 60 | 3/3 = 30 | 51 base + C-62(0) + C-63(0.5) + C-64(1) = **52.5/56** | 262.5 | **352** |
| V-03 | 5/5 = 60 | 3/3 = 30 | 52 base + C-62(0) + C-63(1) + C-64(0) = **53/56** | 265.0 | **355** |
| V-04 | 5/5 = 60 | 3/3 = 30 | 52 base + C-62(1) + C-63(1) + C-64(0) = **54/56** | 270.0 | **360** |
| V-05 | 5/5 = 60 | 3/3 = 30 | 52 base + C-62(1) + C-63(1) + C-64(1) = **55/56** | 275.0 | **365** |

**Ranking**: V-05 (365) > V-04 (360) > V-01 = V-03 (355) > V-02 (352)

All variations exceed the golden threshold of 220.

---

### Discrimination Analysis

The discriminating pair is exactly as predicted: **V-04 vs V-02**.

- V-04 has C-62 + C-63 but not C-64 (single table, no Rule 5). Score: 360.
- V-02 has C-64 but not C-62 or C-63 (and fails C-59). Score: 352.

V-04 outscores V-02 despite missing C-64 because V-02's regression on C-59 costs more than the gain from C-64. The C-59 hit is a structural regression: the diff step (Step 6) loses its inertia reminder. Combined with missing C-62, V-02 scores 8 points below V-04.

**V-02 design gap**: The redesign to split tables introduced a structural inconsistency — the INERTIA-GATE template declared "three recurrence sites" but the actual steps place markers at only two sites. The Step 6 marker was present in v18 and was lost in the split-table refactor. This is a compositional risk: C-64's architectural change can silently remove C-59's coverage if the gate placement isn't explicitly re-audited after restructuring.

**V-01 vs V-03 tie**: Both score 355 on different axes. V-01 delivers C-62 (manifest in block definition), V-03 delivers C-63 (type-labeled nulls with Rule 3 update). Neither delivers C-64. The paths to the same score are structurally independent.

---

### Excellence Signals — V-05

Two patterns in V-05 go beyond what C-62/C-63/C-64 individually required:

**Pattern 1: Cross-table structural rule in COLUMN CONTRACT (Rule 5)**
Prior rules in the COLUMN CONTRACT governed column-level requirements (enumerated values, independence, null form, Delta Finding format). Rule 5 is the first rule that governs a structural relationship *between* tables: "Schema: identical column name, identical REQUIRED status, identical prose-prohibition rule across both tables." This is a meta-structural rule — not "what goes in a cell" but "what structural contract must hold between two output tables." The rule is discoverable before any step runs because it lives in the COLUMN CONTRACT preamble, not in the per-step instructions. A model that commits to the schema before Step 1 is bound by Rule 5 before ever reaching Step 4a.

**Pattern 2: Schema note with explicit forbidden-mutation list**
The upfront schema block in V-05 adds: "Note: 'Inertia Rejected Because [REQUIRED]' carries identical schema in both Step 4a and Step 4b per Rule 5. Do not merge the two tables. Do not rename the column in either table." This names two specific structural mutations that would silently satisfy the surface schema while violating the enforcement contract. Prior schema notes stated what must be present; this note states what transformations are forbidden. The forbidden-mutation list pattern extends schema commitment from "here is the shape you must produce" to "here are the shapes that superficially resemble but do not satisfy the requirement." This is the same logical move as C-34's PASS/FAIL examples on enumerated columns, applied at the table-structure level.

---

### Round 20 Summary

| | C-62 | C-63 | C-64 | C-59 | Score |
|---|:---:|:---:|:---:|:---:|:---:|
| V-01 | PASS | FAIL | FAIL | PASS | **355** |
| V-02 | FAIL | PARTIAL | PASS | FAIL | **352** |
| V-03 | FAIL | PASS | FAIL | PASS | **355** |
| V-04 | PASS | PASS | FAIL | PASS | **360** |
| V-05 | PASS | PASS | PASS | PASS | **365** |

All essential criteria pass across all five variations. V-05 is the top-scoring variation and the first to satisfy all three new R20 criteria simultaneously. The V-02 regression on C-59 is a structural risk signal for split-table refactors: architectural changes to step numbering must explicitly re-audit all declared INERTIA-GATE sites.

---

```json
{"top_score": 365, "all_essential_pass": true, "new_patterns": ["Cross-table meta-structural rule in COLUMN CONTRACT: Rule 5 governs table-to-table column symmetry (identical column name, REQUIRED status, prose-prohibition rule across both tables), making it discoverable at schema-commitment time before any step runs — the first rule that constrains structural relationships between output tables rather than column content.", "Schema note with explicit forbidden-mutation list: the upfront schema block names specific structural mutations that would superficially satisfy the schema but violate the enforcement contract ('Do not merge the two tables. Do not rename the column in either table.') — extends schema commitment from declaring required shape to declaring forbidden near-matches, parallel to the PASS/FAIL examples pattern applied at table-structure level."]}
```
