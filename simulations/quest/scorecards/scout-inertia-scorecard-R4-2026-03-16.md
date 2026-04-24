## scout-inertia R4 — Scoring Report

### Scoring Weights

| Category | Criteria | Pts each | Max |
|----------|----------|----------|-----|
| Essential | C-01, C-02, C-03, C-04, C-05 | 10 | 50 |
| Recommended | R-01, R-02, R-03 | 10 | 30 |
| Aspirational (new R4) | A-05, A-06, A-07, A-08 | 5 | 20 |
| **Total** | | | **100** |

---

### V-01 — A-05 only (question-primed, standard linear order)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Section 1 has all 5 fields + sentence prompt + A-04 role gate |
| C-02 | **PASS** | "number or range — high/low not accepted" + self-score |
| C-03 | **PASS** | Explicitly stated HIGH with compelling-feature caveat |
| C-04 | **PASS** | Falsifiability check + FM column in DC table + sentence prompt |
| C-05 | **PASS** | Section 3 requires specific trigger + observable symptom + self-score |
| R-01 | **PASS** | DC table has "Team type" column with "specific role or team context" label |
| R-02 | **PASS** | A-04 gate + sentence slot forces role name before table entry |
| R-03 | **PASS** | Self-score R-03 present; Unit column scaffold says "per [role from Section 1]" |
| A-05 | **PASS** | Sentence prompts at all 4 critical tables |
| A-06 | **FAIL** | No inter-section bridges; sections are independent |
| A-07 | **FAIL** | No segmented analysis requiring ID citation |
| A-08 | **FAIL** | Standard linear order: C-01 → C-02 → C-05 → C-04 |

**Score: 85** (C+R all pass = 80; A-05 = +5)

---

### V-02 — A-06 only (cognitive bridges, fail-first inherited from R3)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Section 2 has all fields; Bridge 1→2 names actor-from-symptom constraint |
| C-02 | **PASS** | Quantification required; Bridge 2→3 says "role anchor for every estimate" |
| C-03 | **PASS** | Stated HIGH with full caveat |
| C-04 | **PASS** | Falsifiability check + FM link required + Bridge 3→4 names mechanism |
| C-05 | **PASS** | Section 1 is primary gate; cascade warning on FAIL |
| R-01 | **PASS** | DC table "Team type" column; Bridge 3→4 scopes team to FM context |
| R-02 | **PASS** | A-04 gate; Bridge 1→2: "symptom line reveals the actor" |
| R-03 | **PASS** | Self-score R-03 + Bridge 2→3 says "cost with no role anchor is a cost for nobody" |
| A-05 | **FAIL** | No sentence prompts before tables |
| A-06 | **PASS** | Explicit named bridges at every section boundary; bridges name upstream product and downstream cell constrained |
| A-07 | **FAIL** | No segmented analysis |
| A-08 | **PASS** | Fail-first structure: C-05 Section 1 → C-01 Section 2 → C-02 Section 3 → C-04 Section 4 |

**Score: 90** (C+R all pass = 80; A-06 + A-08 = +10)

---

### V-03 — A-08 only (purest fail-first, no bridges, no priming)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Section 2 has all fields; actor derived from FM symptom column |
| C-02 | **PASS** | Quantification required; self-score present |
| C-03 | **PASS** | Stated HIGH |
| C-04 | **PASS** | Falsifiability check; "each traces to an FM in Section 1" required |
| C-05 | **PASS** | Section 1 is absolute primary gate; "Do not continue" language strongest of all variations |
| R-01 | **PASS** | DC table "Team type" column present |
| R-02 | **PASS** | A-04 gate present; "person affected by failure is the actor" |
| R-03 | **PASS** | Self-score R-03 present |
| A-05 | **FAIL** | No sentence prompts |
| A-06 | **FAIL** | No bridges; no inter-section constraint language |
| A-07 | **FAIL** | No segmented analysis |
| A-08 | **PASS** | Purest fail-first: C-05 absolute primary gate; "Do not continue" blocks all sections until Section 1 passes |

**Score: 85** (C+R all pass = 80; A-08 = +5)

---

### V-04 — A-05 + A-06 + A-08 (fail-first spine + priming + bridges)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Sentence prompt + table + A-04 gate; Bridge 1→2 carries actor from symptom column |
| C-02 | **PASS** | Sentence prompt + table + quantification required; Bridge 2→3: "every Unit cell must name the Section 2 role" |
| C-03 | **PASS** | Stated HIGH with caveat |
| C-04 | **PASS** | Sentence prompt + falsifiability check + FM link required; Bridge 3→4 names FM-as-mechanism |
| C-05 | **PASS** | Section 1 primary gate + sentence prompt; "Revise triggers and symptoms until a valid sentence can be written" |
| R-01 | **PASS** | DC table "Team type" column; Bridge 3→4: "team type experiencing the FM determines who switches first" |
| R-02 | **PASS** | A-04 gate + bridges enforce role from symptom evidence at every section entry |
| R-03 | **PASS** | Self-score + Bridge 2→3: explicit "cost without role is a cost for nobody" |
| A-05 | **PASS** | Sentence prompts at all 4 sections |
| A-06 | **PASS** | Explicit named bridges at all 3 transitions (1→2, 2→3, 3→4) with named upstream product and downstream cell constraint |
| A-07 | **FAIL** | No segmented analysis; ID-referenced synthesis not required |
| A-08 | **PASS** | Fail-first: Section 1=C-05 primary gate, cascade encoded in all bridges |

**Score: 95** (C+R all pass = 80; A-05 + A-06 + A-08 = +15)

---

### V-05 — All four (A-05 + A-06 + A-07 + A-08 with segmented two-pass)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | A2 and B2 each have all fields with ACTOR-A/B labels; sentence prompts; bridge constrains actor from FM symptom |
| C-02 | **PASS** | A3 and B3 with quantification required; sentence prompts; bridges anchor to ACTOR-A/B and tool type |
| C-03 | **PASS** | Dedicated "Inertia Threat Score" section covering both team types explicitly |
| C-04 | **PASS** | Synthesis gate (SDC-01, SDC-02) is the definitive C-04 gate; segment-level A4/B4 are necessary but not sufficient |
| C-05 | **PASS** | A1 and B1 are primary gates within each pass; "Do not enter A2 / B2" blocking language |
| R-01 | **PASS** | Structurally satisfied: SDC rows must cite DC-A and DC-B IDs, which are team-scoped by construction |
| R-02 | **PASS** | ACTOR-A/B declared IDs throughout; R-02 check spans A2, B2, A4, B4 in composite gate |
| R-03 | **PASS** | Bridges in A2→A3 and B2→B3 explicitly say "every estimate anchored to ACTOR-A/B"; self-score per pass |
| A-05 | **PASS** | Sentence prompts at all critical tables in both passes (A1, A2, A3, A4, B1, B2, B3, B4) |
| A-06 | **PASS** | Bridges at every section boundary and at the Pass A→B boundary; bridge text names specific upstream product and downstream cell constrained |
| A-07 | **PASS** | Synthesis table COLUMNS require FM and DC IDs — structurally impossible to produce free-prose synthesis; "free-prose summaries without IDs do not pass A-07" |
| A-08 | **PASS** | Fail-first within each pass: A1/B1 (FM discovery) precede A2/B2 (workaround identity) in both passes |

**Score: 100** (C+R all pass = 80; A-05 + A-06 + A-07 + A-08 = +20)

---

### Summary

| Variation | Axis | Essential | Recommended | Aspirational | **Score** |
|-----------|------|-----------|-------------|--------------|-----------|
| V-05 | A-05 + A-06 + A-07 + A-08 | 5/5 PASS | 3/3 PASS | 4/4 PASS | **100** |
| V-04 | A-05 + A-06 + A-08 | 5/5 PASS | 3/3 PASS | 3/4 PASS | **95** |
| V-02 | A-06 only | 5/5 PASS | 3/3 PASS | 2/4 PASS | **90** |
| V-01 | A-05 only | 5/5 PASS | 3/3 PASS | 1/4 PASS | **85** |
| V-03 | A-08 only | 5/5 PASS | 3/3 PASS | 1/4 PASS | **85** |

**Ranking**: V-05 > V-04 > V-02 > V-01 = V-03

---

### Excellence Signals from V-05

**1. Step 0 pre-declaration of team types**
Before any table is touched, the analyst must name the primary (highest friction) and secondary (lowest friction) team types. Team scoping cannot be deferred to a DC column — it is forced at the analysis entry point.

**2. ACTOR-A / ACTOR-B as declared IDs that propagate through an entire pass**
The actor role is named and labeled once (as ACTOR-A or ACTOR-B) at the point it first emerges from the FM symptom column, then carried as a literal ID through every cost estimate, defeat condition, and synthesis row. Role drift becomes structurally detectable: any cell that doesn't reference the ID is visibly inconsistent, without requiring the analyst to cross-check sections.

**3. Synthesis as definitive C-04 gate with structurally required ID citation**
Segment-level C-04 passes (A4 and B4) are explicitly necessary but not sufficient. The synthesis table has ID-citation columns — it is structurally impossible to complete the synthesis without citing FM-A, FM-B, DC-A, DC-B IDs. Free-prose summaries that omit IDs cannot satisfy the column structure; the gap is visible before submission.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Step 0 pre-declaration of team types forces team scoping before analysis begins rather than discovering it post-hoc in a DC column", "ACTOR-A/B as declared IDs propagated through an entire pass — role precision enforced at first naming, drift detectable without cross-section comparison", "Synthesis as definitive C-04 gate with ID-citation columns — segment-level passes are necessary but not sufficient; the table structure makes FM and DC evidence anchoring structurally required, not advisory"]}
```
