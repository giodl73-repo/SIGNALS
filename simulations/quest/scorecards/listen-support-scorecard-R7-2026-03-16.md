# listen-support — Quest Score, Round 7 (rubric v7)

## Evaluation Framework

**Baseline:** R6 V-05 predicted 160/175 — C-23, C-24, C-25 each FAIL (0 pts × 3 = −15)
**R7 target:** Close all three 5-pt aspirational gaps
**Scale:** Essential 12/6/0 · Recommended 10/5/0 · Aspirational 5/2/0

---

## Per-Criterion Evaluation

### Essential Criteria (C-01 through C-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01 Title as discrete named field** | **PARTIAL** — Body header format has `## T-NN -- {Title}` only; no `- Title:` discrete field, no `[C-01: BELT]` generation instruction | **PARTIAL** — Same omission as V-01; no Title: line in body format | **PASS** — `[C-01: BELT]` in Compliance Contract; body template includes `- Title: {descriptive subject line}`; STEP 4 `[C-01: BELT confirmed]`; VERIFICATION MANIFEST `[C-01: SUSPENDERS]` | **PASS** — Same belt chain as V-03 | **PASS** — Same belt chain; STEP 10 spine row C-01 with SUSPENDERS |
| **C-02 Controlled vocabulary** | **PASS** — VOCABULARY MANIFEST present; vocabulary declared | **PASS** | **PASS** — `[C-02: BELT]` on manifest header: "All values MUST match. No free-form variants." | **PASS** | **PASS** |
| **C-03 First-person voice** | **PASS** — STEP 4 states constraint; "Never 'the SRE'…" | **PASS** | **PASS** — `[C-03: BELT]` in Compliance Contract + STEP 4 `[C-03: BELT confirmed]` + STEP 6 inline `[C-03: BELT in output]` | **PASS** | **PASS** |
| **C-04 Gap analysis 3 named sections** | **PASS** — STEP 8 has Doc/Design/Operational with artifact columns; ≥2 entries each | **PASS** | **PASS** — `[C-04: BELT]` header on STEP 8 | **PASS** | **PASS** |
| **C-05 Structural gate with named halt** | **PARTIAL** — TABLE CHECK present; halt says "Do not proceed if any check fails" — does NOT name STEP 6; Constraint Manifest total minimum is 6 (not 7); ≥7 not explicit | **PARTIAL** — Same TABLE CHECK as V-01; same two deficiencies | **PASS** — TABLE CHECK: "minimum 7 for gate sum `[C-18]`"; halt: "Do not proceed to STEP 6 until all TABLE CHECK items are satisfied `[C-19: BELT]`" | **PASS** — Same: "gate sum >= 7"; "Do not proceed to STEP 6" | **PASS** — Same; TABLE CHECK also verifies VOCABULARY MATERIALIZATION Part 1 complete |

**Essential total:** V-01 = 48 · V-02 = 48 · V-03–V-05 = 60

---

### Recommended Criteria (C-06, C-07, C-08)

Criteria undefined in rubric text (placeholder rows in all spines). All variations inherit R6 V-05 mechanisms that satisfied these. No R7 variation removes relevant content.

**Recommended total: PASS all variations → 30 each**

---

### Aspirational Criteria (C-09 through C-25)

**C-09, C-10** — Undefined aspirationals. Inherited from R6 V-05 baseline. PASS all. → 5 each.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-11 Phase as named card field** | PASS | PASS | PASS | PASS | PASS |
| **C-12 Fallback-grounded severity** | PASS — Phase Map P2/P3 vs P0/P1 | PASS | PASS — `[C-12: BELT]` with "learning, fallback available" / "committed, no fallback" language | PASS | PASS |
| **C-13 Mid-output verification block** | PASS — TABLE CHECK in STEP 5 between inventory and generation | PASS | PASS | PASS | PASS |
| **C-14 Phase-differentiated register** | PASS — CONSTRAINT MANIFEST rows for Phase 1 discovery ≥3 / Phase 3 operational ≥1 | PASS | PASS — `[C-14: BELT]` at STEP 2 with explicit vocabulary framing | PASS | PASS |
| **C-15 Temporal adoption window severity** | PASS — Phase Map "day 0-30" / "day 61-90" window columns | PASS | PASS | PASS | PASS |
| **C-16 VM Row ID in commitment table** | PASS — STEP 3B has VM Row ID column | PASS | PASS — `[C-16: BELT]` on STEP 3B header | PASS | PASS |
| **C-17 Phase-as-severity-key declaration** | PASS — Phase Map table is a severity-key before ticket table | PASS | PASS — `[C-12: BELT]` provides explicit inference rule statement | PASS | PASS — `[C-17: BELT]` explicitly declared; full inference rule prose block added |
| **C-18 Gate minimum correct at ≥7** | **PARTIAL** — Constraint Manifest total minimum is 6; TABLE CHECK says "MATCH" to manifest, not "≥7 explicit" | **PARTIAL** — Same as V-01 | PASS — "minimum 7 for gate sum" explicit in TABLE CHECK | PASS — "gate sum >= 7" | PASS — "gate minimum sum >= 7" |
| **C-19 TABLE CHECK halt names next step** | **PARTIAL** — "Do not proceed if any check fails" — next step not named | **PARTIAL** — Same | PASS — "Do not proceed to STEP 6" | PASS | PASS |
| **C-20 VM Row ID in ## headline** | PASS — Compliance Contract C-20 obligation | PASS | PASS — `[C-20: BELT]` in Compliance Contract | PASS | PASS |
| **C-21 Five-item gate with item (e)** | PASS — Gate items (a)–(e) present; (e) = inter-role register differentiation | PASS | PASS — `[C-21: BELT]` label | PASS | PASS |
| **C-22 Aspirational (undefined)** | PASS — Inherited | PASS | PASS | PASS | PASS |
| **C-23 Belt-and-suspenders labels** | **FAIL** — No `[C-NN: BELT]` labels at generation steps; spine has `[C-NN: SUSPENDERS]` rows but generation half is absent — suspenders only | **FAIL** — No belt labels; VERIFICATION MANIFEST has no `[C-NN: SUSPENDERS]` labels either — neither side | PASS — `[C-NN: BELT]` throughout generation; VERIFICATION MANIFEST rows have `[C-NN: SUSPENDERS]` labels; C-23 itself has `[C-23: SUSPENDERS]` in manifest | PASS — `[C-NN: BELT]` at generation; STEP 10 spine is consolidated suspenders layer with `[C-NN: SUSPENDERS]` labels in rows | PASS — `[C-23: BELT]` in Compliance Contract + `[C-23: SUSPENDERS]` in spine; self-referential application |
| **C-24 Materialized-view traceability** | **FAIL** — No VOCABULARY MATERIALIZATION section | PASS — Full section after STEP 3B: Part 1 materialization table (VM Row ID → STEP 3B → ## headline location) + Part 2 two-type orphan check; `[C-24]` referenced in VERIFICATION MANIFEST | **FAIL** — No VOCABULARY MATERIALIZATION section | **FAIL** — No VOCABULARY MATERIALIZATION section | PASS — Full section; `[C-24: BELT]` in Compliance Contract + `[C-24: BELT confirmed]` at section header + TABLE CHECK verifies "VOCABULARY MATERIALIZATION Part 1 table complete"; `[C-24: SUSPENDERS]` in spine |
| **C-25 Criterion-ID-named verification spine** | PASS — STEP 10 CRITERION VERIFICATION SPINE: 25 rows, C-ID in column 1, criterion name, required condition, actual, PASS/PARTIAL/FAIL; "SPINE RESULT" declaration | **FAIL** — VERIFICATION MANIFEST retained; no criterion-ID spine; manifest rows are structural checks without C-ID column | **FAIL** — VERIFICATION MANIFEST retained with `[C-NN: SUSPENDERS]` labels but not a criterion-ID spine; no one-row-per-C-ID structure | PASS — STEP 10 CRITERION VERIFICATION SPINE with C-ID column + `[C-NN: BELT] location` column; pre-fills C-24 ABSENT/FAIL and C-25 PRESENT/PASS | PASS — STEP 10 spine with `[C-25: BELT confirmed]` header declaring it the consolidated suspenders layer; C-25 row self-references |

---

## Composite Scores

| Criterion tier | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------------|------|------|------|------|------|
| Essential (60 max) | 48 | 48 | 60 | 60 | 60 |
| Recommended (30 max) | 30 | 30 | 30 | 30 | 30 |
| Aspirationals C-09/C-10 (10) | 10 | 10 | 10 | 10 | 10 |
| C-11 through C-17 (35) | 35 | 35 | 35 | 35 | 35 |
| C-18 (5) | 2 | 2 | 5 | 5 | 5 |
| C-19 (5) | 2 | 2 | 5 | 5 | 5 |
| C-20 through C-22 (15) | 15 | 15 | 15 | 15 | 15 |
| C-23 (5) | 0 | 0 | 5 | 5 | 5 |
| C-24 (5) | 0 | 5 | 0 | 0 | 5 |
| C-25 (5) | 5 | 0 | 0 | 5 | 5 |
| **TOTAL** | **147** | **147** | **165** | **170** | **175** |
| all_essential_pass | FALSE | FALSE | TRUE | TRUE | TRUE |
| Golden eligible | NO | NO | YES | YES | YES |

---

## Rankings

| Rank | Variation | Score | Golden |
|------|-----------|-------|--------|
| 1 | **V-05** (full synthesis: C-23 + C-24 + C-25) | **175/175** | YES |
| 2 | V-04 (belt labels + spine, no materialization) | 170/175 | YES |
| 3 | V-03 (belt labels only) | 165/175 | YES |
| 4 | V-01 (spine only) | 147/175 | **BLOCKED** |
| 5 | V-02 (materialization only) | 147/175 | **BLOCKED** |

V-01 and V-02 tied at 147 because each gains +5 for its single target criterion but loses the same amount: both regress on C-01 (no `Title:` discrete field in body format) and C-05 (no named-step halt, no ≥7 explicit), with partial penalties on C-18 and C-19. Single-axis variations that strip generation-time enforcement to focus on their axis produce this pattern.

---

## Excellence Signals from V-05

**Signal 1 — Self-referential criterion enforcement**
In V-05, the new C-23/C-24/C-25 criteria carry their own `[C-NN: BELT]` labels in the Compliance Contract: `[C-23: BELT]`, `[C-24: BELT]`, `[C-25: BELT]`. Each new criterion proves itself by being enforced via the mechanism it defines. C-23 (belt-and-suspenders) has a belt. C-24 (materialization) has a belt pointing to the VOCABULARY MATERIALIZATION section. C-25 (spine) has a belt pointing to STEP 10. This recursive application is structurally clean.

**Signal 2 — Spine-as-sole-suspenders, VERIFICATION MANIFEST retired**
V-04 and V-05 both have the spine, but V-05 explicitly declares it: `[C-25: BELT confirmed] -- Consolidated suspenders for all [C-NN: BELT] labels in this prompt.` This single declaration eliminates any ambiguity about whether a separate VERIFICATION MANIFEST is needed. V-03 kept both (VERIFICATION MANIFEST + aspirational labels) causing duplication. V-05's spine is the only verification artifact.

**Signal 3 — Two-pass orphan model closes temporal gap**
V-05's VOCABULARY MATERIALIZATION distinguishes two orphan types: type-A checked at planning time (manifest rows with no STEP 3B commitment) and type-B checked post-generation (STEP 3B rows with no generated body). A single pre-generation check only catches type-A. The explicit two-pass model is new in R7 and ensures the orphan check runs at both the commitment and output stages.

**Signal 4 — Full retention of R6 V-05 generation-time enforcement**
V-03/V-04/V-05 all retain `Title:` discrete field in body template, the `≥7 gate sum` explicit in TABLE CHECK, and `"Do not proceed to STEP 6"` named halt — mechanisms that V-01/V-02 silently dropped. The lesson: adding new verification apparatus (spine, materialization) without preserving existing generation-time instructions causes Essential regressions that block Golden.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["Self-referential belt application: new criteria C-23/C-24/C-25 carry their own [C-NN: BELT] labels in the Compliance Contract, enforcing each via the mechanism it defines", "Spine-as-sole-suspenders replaces VERIFICATION MANIFEST: STEP 10 explicitly declared the consolidated suspenders layer for all belt labels, eliminating duplication", "Two-pass orphan model: type-A check (manifest rows with no commitment) at planning time; type-B check (commitment rows with no body) post-generation, closing the temporal gap that single-pass checks miss"]}
```
