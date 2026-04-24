## Quest Score — campaign-decide / Round 8 / Rubric v7

### Scoring Model

- **Essential** (C-01..C-05): 12 pts each × 5 = 60 pts — all must pass or output fails
- **Recommended** (C-06..C-08): 10 pts each × 3 = 30 pts
- **Aspirational** (C-09..C-24): 0.625 pts each × 16 = 10 pts
- **Max composite**: 100.0

---

### V-01 R8 — Because block as named-column table

Base: V-04 R7 (strict C-23, C-24). Single axis: Because block converted from 6-slot bullet list to 4-column named-column table (Phase | Label | Citation | Claim).

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 Recommendation stated | PASS | F5-02 table has COMMIT/PAUSE/PIVOT/ABANDON column |
| C-02 Confidence stated | PASS | Confidence (H/M/L) column in F5-02 |
| C-03 All six domains | PASS | Phase 0 (prove-hypothesis), 1a/1b (scout-competitors), 2 (scout-feasibility), 3 (scout-market), 4 (prove-websearch), 5 (prove-synthesize) |
| C-04 Inertia-first | PASS | Phase 1a header precedes Phase 1b; gate annotation `[COMPLETE BEFORE PHASE 1b]` |
| C-05 Evidence-to-rec traceability | PASS | Because table has explicit "Citation (Phase N, F[N]-seq)" column per row |
| C-06 Structured brief format | PASS | FINDING REGISTER + titled phase sections + Phase 5 recommendation block |
| C-07 Risk/counter-evidence | PASS | F5-03 Counter-Evidence row with Qualifying FID column |
| C-08 Hypothesis disposition | PASS | F5-01 "Outcome (Confirmed / Refuted / Inconclusive)" column |
| C-09 Confidence calibration narrative | PASS | "Confidence Rationale (cite FIDs — not label alone)" column in F5-02 |
| C-10 Actionable next steps | PASS | F5-04 Condition column: `[COMMIT: concrete action \| no-build: exit trigger]` |
| C-11 Per-phase required-field schema | PASS | Every phase has domain-specific named-column tables |
| C-12 Templated citation syntax | PASS | Because table "Citation" column enforces `Phase N, F[N]-seq` format |
| C-13 Hypothesis-prior anchoring | PASS | F0-01 hypothesis record at Phase 0 before any evidence phase; "Hypothesis Claim" column makes prior commitment structurally identifiable |
| C-14..C-22 (inherited V-04 R7) | PASS | Full structure carried unchanged from V-04 R7 |
| C-23 Column-header schema enforcement | PASS strict | Because table has column headers (Phase, Label, Citation, Claim); synthesis layer now matches evidence layer's column-schema discipline; no `\| Field \| Value \|` anywhere |
| C-24 Sub-phase synthesis slot alignment | PASS | Phase 1a (INERTIA) and Phase 1b (RIVALS) as separately labeled rows in the Because table; column "Phase" cell shows "Phase 1a" and "Phase 1b" distinctly |

**Essential pass**: YES (all 5)
**Aspirational**: 16/16
**Composite**: 60 + 30 + 10.0 = **100.0**

---

### V-02 R8 — Phase 1b response-strategy column

Base: V-04 R7. Single axis: Phase 1b rivals table gains fifth column "Response Strategy (how we win vs. this rival)". Because block remains 6-slot bullet list.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 | PASS | F5-02 recommendation table present |
| C-02 | PASS | Confidence column in F5-02 |
| C-03 | PASS | All six domains covered |
| C-04 Inertia-first | PASS | Phase 1a gate annotation unchanged; inertia block precedes rivals |
| C-05 | PASS | 6-slot Because block with hybrid Phase+FID citations |
| C-06 | PASS | Document structure identical to V-04 R7 |
| C-07 | PASS | F5-03 counter-evidence present |
| C-08 | PASS | F5-01 outcome column present |
| C-09 | PASS | Confidence Rationale column |
| C-10 | PASS | F5-04 conditioned next step |
| C-11 | PASS | Per-phase schema intact |
| C-12 | PASS | Because bullet format: `[claim] because Phase N, F[N]-seq` |
| C-13 | PASS | F0-01 hypothesis record at Phase 0 |
| C-14..C-22 | PASS | V-04 R7 base unchanged |
| C-23 strict | PASS | Phase 1b now has 5 domain-specific column headers including "Response Strategy"; addition strengthens not weakens schema compliance |
| C-24 | PASS | 6-slot Because with 1a/1b labeled slots |

Note on C-04 interaction: Response Strategy column addresses product rivals, not inertia — no contamination of inertia-first ordering.

**Essential pass**: YES
**Aspirational**: 16/16
**Composite**: 60 + 30 + 10.0 = **100.0**

---

### V-03 R8 — Minimal prompt (structural scaffolding only, no prose)

Base: V-04 R7. Single axis: all instructional prose stripped — FINDING REGISTER preamble compressed to one line; Phase 0 and Phase 5 sub-table labels removed. Gate annotations, phase tables, domain column headers, and Because block retained identical to V-04 R7.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 | PASS | F5-02 recommendation table; COMMIT/PAUSE/PIVOT/ABANDON in column header |
| C-02 | PASS | Confidence (H/M/L) column header present |
| C-03 | PASS | All six phase sections present by section header |
| C-04 | PASS | Phase 1a header gate annotation `[COMPLETE BEFORE PHASE 1b]` retained |
| C-05 | PASS | Because block with hybrid citations retained |
| C-06 | PASS | Section structure intact; phase hierarchy visible by headers |
| C-07 | PASS | F5-03 counter-evidence row with column schema |
| C-08 | PASS | "Outcome (Confirmed / Refuted / Inconclusive)" column header in Phase 5 first table — prose label removed but column header carries the semantic requirement |
| C-09 | PASS | "Confidence Rationale (cite FIDs — not label alone)" column header; prose wrapper was not needed |
| C-10 | PASS | F5-04 Condition column with COMMIT/no-build trigger |
| C-11 | PASS | Domain-specific column headers per phase intact |
| C-12 | PASS | Because block citation format template retained |
| C-13 | PASS | F0-01 "Hypothesis Claim" column header at Phase 0 carries prior-commitment semantics; prose "commit prior before any evidence phase runs" was instructional redundancy — the structural position (Phase 0 before Phase 1) and column header are sufficient |
| C-14..C-22 | PASS | All structural criteria independent of prose |
| C-23 strict | PASS | Column headers unchanged; schema visible in header rows |
| C-24 | PASS | 6-slot Because with 1a/1b labels |

**Compressibility verdict**: No criterion fails when prose is removed. All 24 v7 criteria are purely structural — they score column headers, gate annotations, section ordering, citation format, and slot counts. Minimum passing template confirmed as structural scaffolding alone.

**Essential pass**: YES
**Aspirational**: 16/16
**Composite**: 60 + 30 + 10.0 = **100.0**

---

### V-04 R8 — Because table + Phase 1b response strategy (combined)

Base: V-04 R7. Combined: V-01 R8 Because table + V-02 R8 Response Strategy column.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01..C-05 (essential) | PASS × 5 | Recommendation, confidence, all domains, inertia-first, traceable citations — all structural elements from V-04 R7 intact |
| C-06..C-08 (recommended) | PASS × 3 | Structure, counter-evidence, hypothesis disposition — unchanged |
| C-09..C-22 (aspirational 1-14) | PASS × 14 | V-04 R7 base; no regression from either axis addition |
| C-23 strict | PASS | Evidence phases: all domain-specific column headers. Phase 1b: 5 columns. Because table: Phase/Label/Citation/Claim headers. Synthesis layer now full column-schema compliant. Strongest C-23 evidence in R8 set |
| C-24 | PASS | Because table "Phase" column shows "Phase 1a" and "Phase 1b" as distinct cell values — more visually explicit than bullet prefix format; C-24 evidence stronger than V-02 R8 |

**Interaction notes**: Because table (V-01 axis) and Response Strategy column (V-02 axis) are structurally independent — different phases, different schema layers. No criterion interaction risk. C-24 is actually stronger here than in V-02 R8 because row separation in a table column is more mechanically auditable than label prefixes in a bullet list.

**Forward compatibility**: Only template in R8 set that passes both C-25 and C-26 v8 candidates.

**Essential pass**: YES
**Aspirational**: 16/16
**Composite**: 60 + 30 + 10.0 = **100.0**

---

### V-05 R8 — Hypothesis lifecycle (Phase 0 outcome columns) + Because table

Base: V-04 R7. Combined: Phase 0 experiment table extended with "Expected Result (fill now)" and "Actual Outcome (fill at Phase 5)" columns + V-01 R8 Because table.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01..C-05 (essential) | PASS × 5 | All from V-04 R7 base; lifecycle columns do not displace any structural requirement |
| C-06..C-08 (recommended) | PASS × 3 | F5-01 hypothesis resolution table retained as authoritative disposition record |
| C-09..C-22 | PASS × 14 | V-04 R7 base; no regression |
| C-13 Hypothesis-prior anchoring | PASS (strengthened) | "Expected Result (fill now)" column makes pre-evidence prediction explicit — stronger C-13 evidence than bare experiment design columns; analyst commits both claim (F0-01) and expected experimental outcome before Phase 1 runs |
| C-23 strict | PASS | Phase 0 experiment table now has 5 domain-specific column headers: FID, Experiment Name, Investigation Method, Expected Result (fill now), Actual Outcome (fill at Phase 5); timing parentheticals additive to domain-specific field names |
| C-24 | PASS | 6-slot Because table with Phase 1a/1b row separation |

**Dual-table concern addressed**: Phase 0 lifecycle table (F0-02, F0-03) and Phase 5 resolution table (F5-01) track distinct record types — experiment design/outcome vs. hypothesis claim disposition. No FID ambiguity; C-08 scores F5-01 only.

**Essential pass**: YES
**Aspirational**: 16/16
**Composite**: 60 + 30 + 10.0 = **100.0**

---

### Rankings

| Rank | Variant | Composite | Distinguishing feature |
|------|---------|-----------|------------------------|
| T-1 | V-04 R8 | **100.0** | Most forward-compatible: passes C-25 + C-26 v8 candidates |
| T-1 | V-05 R8 | **100.0** | Passes C-25 + C-27; C-13 evidence strengthened by expected-result column |
| T-1 | V-01 R8 | **100.0** | First template where synthesis Because layer is column-schema compliant (C-25) |
| T-1 | V-02 R8 | **100.0** | Competitor analysis becomes actionable via Response Strategy column (C-26) |
| T-1 | V-03 R8 | **100.0** | Minimum token cost; confirms no criterion requires prose |

All five variants tie at 100.0 strict. The v7 ceiling is stable.

---

### Excellence Signals (from V-04 R8 as most structurally complete)

**1. Full schema symmetry across all layers.** V-04 R8 extends column-header schema from evidence phases (C-23) to the synthesis Because block (C-25 candidate) and to the rivals table (C-26 candidate). Every layer of the template now enforces compliance via header rows. Violation is visible as a column gap, not a content omission.

**2. Because-as-table closes the last format asymmetry.** In R7, evidence phases used named-column tables while synthesis used a labeled bullet list. Converting the Because block to a 4-column table (Phase | Label | Citation | Claim) means the synthesis layer is now as mechanically auditable as the evidence layers. The "Citation" column header enforces `Phase N, F[N]-seq` format structurally rather than by example syntax.

**3. Competitive analysis becomes actionable.** The Response Strategy column forces the analyst to state how to win against each rival at fill time — not as a downstream synthesis step. This converts Phase 1b from a diagnostic table (what rivals do) to a decision table (what we do about them). The column header makes the requirement structurally mandatory.

**4. Structural compressibility confirmed (V-03).** The 24-criterion ceiling is reachable at minimum prompt length. No criterion silently requires instructional prose. This defines the canonical minimal template for automated/API-driven use: FINDING REGISTER + domain-column phase tables + gate-annotated headers + 6-slot Because block.

**5. Experiment lifecycle as continuous record (V-05).** Embedding "Expected Result (fill now)" and "Actual Outcome (fill at Phase 5)" in the Phase 0 table makes the experimental chain visible as a single row per experiment, rather than requiring cross-reference between Phase 0 and Phase 5. This is the strongest C-13 evidence pattern produced in any round.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Because block as named-column table creates full schema symmetry between evidence and synthesis layers", "Competitive Response Strategy column makes Phase 1b actionable rather than only diagnostic", "Minimum passing template confirmed as structural scaffolding alone — no criterion requires instructional prose", "Experiment lifecycle columns in Phase 0 table create continuous design-to-outcome record without cross-table reference"]}
```
