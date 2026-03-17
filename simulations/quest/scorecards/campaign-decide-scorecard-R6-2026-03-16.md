## Scorecard — campaign-decide / Round 6

### Scoring Setup

| Band | Points | Formula |
|------|--------|---------|
| Essential | 60 | pass_count/5 × 60 |
| Recommended | 30 | pass_count/3 × 30 |
| Aspirational | 10 | pass_count/14 × 10 (0.71 pts each) |

---

### V-01 — Canonical 22/22 Convergence

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Recommendation stated | **PASS** | F5-02 labeled COMMIT/PAUSE/PIVOT/ABANDON |
| C-02 | Confidence level stated | **PASS** | F5-03 confidence field |
| C-03 | All six domains | **PASS** | Phase 0 (hypothesis), Phase 1a+1b (competitors), Phase 2 (feasibility), Phase 3 (market), Phase 4 (websearch), Phase 5 (synthesis) |
| C-04 | Inertia-first | **PASS** | Phase 1a (Inertia) is a separate sub-section before Phase 1b (Rivals) |
| C-05 | Traceability | **PASS** | Because block: 5 labeled slots with phase+FID citations |
| C-06 | Structured format | **PASS** | Section headers per phase + labeled FID rows |
| C-07 | Risk acknowledged | **PASS** | F5-05 counter-evidence field with FID citation requirement |
| C-08 | Hypothesis disposition | **PASS** | F5-01 resolves F0-01 explicitly |
| C-09 | Confidence calibration | **PASS** | F5-04 cites specific FIDs driving the rating |
| C-10 | Conditioned next steps | **PASS** | F5-06: COMMIT → concrete action; no-build → exit/revisit |
| C-11 | Per-phase field schema | **PASS** | FID-labeled required rows per phase |
| C-12 | Templated citation | **PASS** | "because Phase N, F[N]-seq" — matches rubric example + FID key |
| C-13 | Hypothesis-prior anchoring | **PASS** | FINDING REGISTER before Phase 0; Phase 0 before Phase 1 |
| C-14 | Cross-phase citation span | **PASS** | 5 distinct phase labels in Because block |
| C-15 | Per-finding unique keys | **PASS** | FINDING REGISTER: 29 unique FIDs pre-assigned |
| C-16 | Finding register pre-seeded | **PASS** | Skeleton "--" rows before Phase 0, strict and liberal |
| C-17 | Per-phase Because slot | **PASS** | 5 slots for 5 evidence skill-phases; one slot for Phase 1 regardless of 1a/1b split |
| C-18 | Counter-evidence FID-pinned | **PASS** | F5-05 cites the FID it qualifies |
| C-19 | Hypothesis resolution FID-anchored | **PASS** | F5-01 "resolves F0-01" by FID reference |
| C-20 | Phase gate in headers | **PASS** | 7 gate-annotated headers: FINDING REGISTER, Phase 0, Phase 1, Phase 1a, Phase 2, Phase 3, Phase 4 |
| C-21 | Inertia-rivals structural isolation | **PASS** | `### Phase 1a [COMPLETE BEFORE Phase 1b]` — boundary enforced at section level |
| C-22 | Dual-axis citation | **PASS** | Phase prefix + FID key in every Because slot; no scorer ambiguity |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 14/14 = 10
**Composite: 100.0**

---

### V-02 — All-Table Content Format

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Recommendation stated | **PASS** | F5-02 row in Phase 5 table |
| C-02 | Confidence level stated | **PASS** | F5-03 row in Phase 5 table |
| C-03 | All six domains | **PASS** | Same domain coverage as V-01; tables replace inline rows, not sections |
| C-04 | Inertia-first | **PASS** | Phase 1a table precedes Phase 1b table; gate preserved |
| C-05 | Traceability | **PASS** | Because block unchanged from V-01 |
| C-06 | Structured format | **PASS** | Table column headers make schema explicit at column level (stronger than V-01) |
| C-07 | Risk acknowledged | **PASS** | F5-05 row with FID citation |
| C-08 | Hypothesis disposition | **PASS** | F5-01 row |
| C-09 | Confidence calibration | **PASS** | F5-04 cites FIDs |
| C-10 | Conditioned next steps | **PASS** | F5-06 row |
| C-11 | Per-phase field schema | **PASS** | Column headers (`| Dimension | Rating (R/Y/G) | Reason |`) make schema explicit — stronger C-11 evidence than inline labels |
| C-12 | Templated citation | **PASS** | Because block identical to V-01 |
| C-13 | Hypothesis-prior anchoring | **PASS** | Structure unchanged; Phase 0 table before Phase 1 |
| C-14 | Cross-phase citation span | **PASS** | 5 distinct phase slots |
| C-15 | Per-finding unique keys | **PASS** | FINDING REGISTER unchanged |
| C-16 | Finding register pre-seeded | **PASS** | FINDING REGISTER with "--" skeleton rows |
| C-17 | Per-phase Because slot | **PASS** | 5 slots; table format does not alter slot count |
| C-18 | Counter-evidence FID-pinned | **PASS** | F5-05 table cell requires FID |
| C-19 | Hypothesis resolution FID-anchored | **PASS** | F5-01 table cell "resolves F0-01" |
| C-20 | Phase gate in headers | **PASS** | 7 gate-annotated headers unchanged |
| C-21 | Inertia-rivals structural isolation | **PASS** | Section boundary and gate annotation unchanged; content format inside sub-sections (table vs inline) is irrelevant to C-21 |
| C-22 | Dual-axis citation | **PASS** | Because block identical to V-01 |

*Note: Phase 4 multi-line source/quote block is compressed into a table row — quote fidelity may suffer under cell-width pressure. Non-criterion risk.*

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 14/14 = 10
**Composite: 100.0**

---

### V-03 — Phase 1 Because Slot Split (6-slot synthesis)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Recommendation stated | **PASS** | F5-02 |
| C-02 | Confidence level stated | **PASS** | F5-03 |
| C-03 | All six domains | **PASS** | Unchanged |
| C-04 | Inertia-first | **PASS** | Phase 1a sub-section preserved |
| C-05 | Traceability | **PASS** | 6 labeled Because slots with citations |
| C-06 | Structured format | **PASS** | |
| C-07 | Risk acknowledged | **PASS** | F5-05 |
| C-08 | Hypothesis disposition | **PASS** | F5-01 |
| C-09 | Confidence calibration | **PASS** | F5-04 cites FIDs |
| C-10 | Conditioned next steps | **PASS** | F5-06 |
| C-11 | Per-phase field schema | **PASS** | FID rows per phase unchanged |
| C-12 | Templated citation | **PASS** | "because Phase 1a, F1-[seq]" — phase prefix + FID; "Phase 1a" satisfies phase token |
| C-13 | Hypothesis-prior anchoring | **PASS** | FINDING REGISTER + Phase 0 position unchanged |
| C-14 | Cross-phase citation span | **PASS** | 6 slots from 6 labeled phases; satisfies ≥3 distinct phases by construction |
| C-15 | Per-finding unique keys | **PASS** | FINDING REGISTER unchanged |
| C-16 | Finding register pre-seeded | **PASS** | Unchanged |
| **C-17** | **Per-phase Because slot** | **FAIL** | 6 slots vs 5 evidence skill-phases. Rubric counts skills (competitors, feasibility, market, hypothesis, websearch = 5), not structural sub-phases. Phase 1a and 1b are sub-phases of ONE skill. 6 ≠ 5. |
| C-18 | Counter-evidence FID-pinned | **PASS** | F5-05 unchanged |
| C-19 | Hypothesis resolution FID-anchored | **PASS** | F5-01 unchanged |
| C-20 | Phase gate in headers | **PASS** | 7 gate-annotated headers unchanged |
| C-21 | Inertia-rivals structural isolation | **PASS** | Phase 1a/1b split and gate preserved |
| C-22 | Dual-axis citation | **PASS** | "because Phase 1a, F1-[seq]" carries both axes |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 13/14 = 9.29
**Composite: 99.3**

---

### V-04 — Lifecycle Emphasis (Purpose Labels on Headers)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-08 | (all essential + recommended) | **PASS** | Structure identical to V-01; labels are appended to headers, not substituted |
| C-09 | Confidence calibration | **PASS** | F5-04 |
| C-10 | Conditioned next steps | **PASS** | F5-06 |
| C-11 | Per-phase field schema | **PASS** | FID rows per phase |
| C-12 | Templated citation | **PASS** | Because block unchanged |
| C-13 | Hypothesis-prior anchoring | **PASS** | FINDING REGISTER + Phase 0 before Phase 1 |
| C-14 | Cross-phase citation span | **PASS** | 5 slots |
| C-15 | Per-finding unique keys | **PASS** | FINDING REGISTER unchanged |
| C-16 | Finding register pre-seeded | **PASS** | Unchanged |
| C-17 | Per-phase Because slot | **PASS** | 5 slots |
| C-18 | Counter-evidence FID-pinned | **PASS** | F5-05 |
| C-19 | Hypothesis resolution FID-anchored | **PASS** | F5-01 |
| C-20 | Phase gate in headers | **PASS** | Gate brackets `[COMPLETE BEFORE ...]` coexist with purpose labels — bracket is the gate; label is cosmetic. 7 gate positions intact. |
| C-21 | Inertia-rivals structural isolation | **PASS** | `### Phase 1a -- Inertia Analysis: why people don't change [COMPLETE BEFORE Phase 1b]` — gate annotation present in header |
| C-22 | Dual-axis citation | **PASS** | Because block unchanged |

*Purpose labels (`: commit prior belief`, `: inertia then rivals`) are usability improvements, not structural changes. They do not introduce or remove any criterion risk.*

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 14/14 = 10
**Composite: 100.0**

---

### V-05 — Conversational Phrasing Register

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Recommendation stated | **PASS** | F5-02 |
| C-02 | Confidence level stated | **PASS** | F5-03 |
| C-03 | All six domains | **PASS** | All phase sections present |
| C-04 | Inertia-first | **PASS** | Phase 1a sub-section gated before Phase 1b; explanatory paragraph in body doesn't alter section order |
| C-05 | Traceability | **PASS** | Because block with hybrid citations |
| C-06 | Structured format | **PASS** | Headers + structure preserved |
| C-07 | Risk acknowledged | **PASS** | F5-05 |
| C-08 | Hypothesis disposition | **PASS** | F5-01 |
| C-09 | Confidence calibration | **PASS** | F5-04 |
| C-10 | Conditioned next steps | **PASS** | F5-06 |
| C-11 | Per-phase field schema | **PASS** | FID rows per phase; prose paragraphs are body text, not field replacements |
| C-12 | Templated citation | **PASS** | Because block: "because Phase N, F[N]-seq" |
| C-13 | Hypothesis-prior anchoring | **PASS** | FINDING REGISTER before Phase 0; prose note "State what you believe before you look at anything" reinforces but does not replace the structural position |
| C-14 | Cross-phase citation span | **PASS** | 5 distinct phase labels |
| C-15 | Per-finding unique keys | **PASS** | FINDING REGISTER unchanged |
| C-16 | Finding register pre-seeded | **PASS** | Pre-seeded skeleton with prose explanation of WHY |
| C-17 | Per-phase Because slot | **PASS** | 5 slots; Phase 5 note "Five evidence phases = exactly five slots" makes the count intentional |
| C-18 | Counter-evidence FID-pinned | **PASS** | F5-05 |
| C-19 | Hypothesis resolution FID-anchored | **PASS** | F5-01 |
| C-20 | Phase gate in headers | **PASS** | All 7 bracket annotations preserved — V-05 R5 failure repaired. Prose in body does not substitute for header gate. |
| C-21 | Inertia-rivals structural isolation | **PASS** | `### Phase 1a -- Inertia Analysis [COMPLETE BEFORE Phase 1b]` gate intact. Phase 1a explanatory paragraph ("The most important competitor is not a named product...") is body text — the gate is in the header. |
| C-22 | Dual-axis citation | **PASS** | Hybrid citation preserved. V-05 R5 FID-only repaired. |

*V-05 R5 failures: Phase 0 and Phase 1a gate annotations dropped; FID-only citation. All three repaired in V-05 R6.*

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 14/14 = 10
**Composite: 100.0**

---

### Final Rankings

| Rank | Variant | Composite | C-17 | C-21 | C-22 | All Essential |
|------|---------|-----------|------|------|------|---------------|
| 1 | **V-01** (canonical reference) | **100.0** | PASS | PASS | PASS | YES |
| 1 | **V-02** (all-table format) | **100.0** | PASS | PASS | PASS | YES |
| 1 | **V-04** (lifecycle emphasis) | **100.0** | PASS | PASS | PASS | YES |
| 1 | **V-05** (conversational register) | **100.0** | PASS | PASS | PASS | YES |
| 5 | **V-03** (6-slot Because split) | **99.3** | FAIL | PASS | PASS | YES |

Four variants reach 100.0. V-03 isolates the C-17 trap precisely.

---

### Excellence Signals (from top-scoring variants)

**From V-01 (canonical):**
- The Phase 1a/1b section boundary + gate annotation is the canonical enforcement mechanism for C-04: inertia ordering is unbreakable, not instructed
- One synthesis slot per evidence *skill* (not per structural sub-phase) is the correct C-17 target — "5 skill-phases → 5 slots" regardless of internal sub-phase splits

**From V-02 (table format):**
- Table column headers (`| Dimension | Rating (R/Y/G) | Reason |`) make C-11's required-field schema explicit at the column level — stronger structural evidence than inline field labels; pure format substitution, no scoring trade-off

**From V-04 (lifecycle emphasis):**
- Purpose labels coexist with gate annotations without diluting them — bracket gate is enforcement; colon label is intent — templates can be simultaneously structurally rigorous and self-describing

**From V-05 (conversational):**
- Explanatory prose *explaining why* a constraint exists is additive to the bracket gate that *enforces* it — V-05 R5's error was prose-as-substitute; V-05 R6's insight is prose-as-companion
- "Prose explains, gate enforces" is a new composable pattern: any constraint can be paired with a "why" paragraph without weakening the structural enforcement

**From V-03 (boundary probe):**
- C-17 and C-21 measure different units: C-21 counts structural sub-phases (1a/1b split is correct); C-17 counts evidence skill-phases (split does not create a new skill). The canonical answer is always one synthesis slot per skill regardless of internal section structure.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["table-column-headers-as-field-schema: phase tables with explicit column headers (| Dimension | Rating | Reason |) make C-11 required-field schema structurally explicit at the column level, stronger than inline FID field labels", "prose-explains-gate-enforces: explanatory prose stating WHY a constraint exists can coexist with bracket gate annotations; prose is additive (usability) not substitutive (enforcement); V-05 R5 failed by substituting prose for brackets; V-05 R6 passes by using both", "lifecycle-labels-scoring-neutral: purpose annotations appended to phase headers (': commit prior belief', ': inertia then rivals') improve fillability and template self-description without affecting any of the 22 criteria — pure usability signal with zero score risk"]}
```
