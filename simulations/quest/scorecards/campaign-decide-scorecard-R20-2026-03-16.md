Now I have sufficient data to score all five variations. Let me compose the full evaluation.

---

# campaign-decide — R20 Scoring (Rubric v19)

**Rubric version**: v19 | **Max composite**: 110.5 | **Date**: 2026-03-17

---

## Baseline inheritance analysis

All R20 variations are declared to inherit **R19 V-05 in full** (C-01 through C-49). Before per-variation scoring, the inheritance claim is verified by checking whether any R20 structural additions regress any existing criterion.

| R20 addition | Criteria at risk | Verdict |
|---|---|---|
| V-01 gate check line (`Gate check: [min met? Y/N]...`) | C-27 (prose-free sufficiency), C-46 (density annotation still present) | No conflict — gate check is bracket-notation structural line, not prose |
| V-02 recommendation delta sentence after rec-record table | C-18 (four required columns still present per C-47 rules), C-27 | No conflict — additive structural sentence, does not rename or remove columns |
| V-03 Inertia Lock-in column added to Phase 3 | C-12 (fit score column still present), C-44 (min-count bracket updated to match), C-48 (FINDING REGISTER [expect: 1+ FIDs] unchanged) | No conflict — additive column; Phase 3 header `[min: 1 segment with fit score and inertia lock-in]` still satisfies C-44 bracket requirement |
| V-03 counter-evidence guidance prose ("When citing high-lock-in segments…") | C-27 (covers only C-01..C-26; counter-evidence is C-07/C-19; guidance is prompt instruction, not body criterion) | No conflict |

**Baseline verdict**: No R20 addition regresses any C-01..C-49 criterion. All 5 variations inherit the full R19 V-05 baseline without defect.

---

## Criterion-by-criterion scoring

Because all 5 variations share an identical C-01..C-49 structural baseline, criteria are scored in tier batches with differentiation noted where any variation shows variation-specific behavior.

### Essential criteria (C-01..C-05) — 12 pts each / 60 pts max

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|---|---|---|---|---|---|---|
| C-01 Recommendation stated | PASS | PASS | PASS | PASS | PASS | COMMIT/PAUSE/PIVOT/ABANDON prompt slot present in all Phase 5 recommendation record tables |
| C-02 Confidence stated | PASS | PASS | PASS | PASS | PASS | `Confidence (H=80%+/M=50-79%/L<50%)` column in recommendation record schema — named field, not embedded prose |
| C-03 All six domains covered | PASS | PASS | PASS | PASS | PASS | Phase 0 through Phase 5 all present in all variations; Phase 1a/1b structurally split |
| C-04 Inertia-first ordering | PASS | PASS | PASS | PASS | PASS | `[COMPLETE BEFORE Phase 1b]` gate on Phase 1a header in all five prompts |
| C-05 Evidence-to-recommendation traceability | PASS | PASS | PASS | PASS | PASS | BECAUSE block cites Phase N, F[N]-seq hybrid keys; Recommendation record requires "cite FIDs — not label alone" |

**Essential score: 60.0 / 60.0 — all five variations, all essential pass**

---

### Recommended criteria (C-06..C-08) — 10 pts each / 30 pts max

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|---|---|---|---|---|---|---|
| C-06 Structured brief format | PASS | PASS | PASS | PASS | PASS | FINDING REGISTER header, titled phase sections, Phase 5 sub-tables — structurally encoded in all five |
| C-07 Risk / counter-evidence | PASS | PASS | PASS | PASS | PASS | Counter-evidence table with `Counter-Evidence / Qualifying FID / Recommended Next Step / Condition` columns present in all; V-03/V-04/V-05 add inertia-lock-in qualifying guidance (additive) |
| C-08 Hypothesis disposition | PASS | PASS | PASS | PASS | PASS | Phase 5 hypothesis resolution sub-table with CONFIRMED/REFUTED/INCONCLUSIVE present in all |

**Recommended score: 30.0 / 30.0 — all five variations**

---

### Aspirational criteria (C-09..C-49) — 0.5 pts each / 20.5 pts max

All 41 aspirational criteria scored below. For criteria where all 5 variations share identical structure, the row shows a single evidence note.

| # | Criterion | All V-01..V-05 | Evidence note |
|---|---|---|---|
| C-09 | Confidence calibration | PASS | "Confidence Rationale (cite FIDs — not label alone)" in recommendation record header |
| C-10 | FID consistency | PASS | Pre-seeded FINDING REGISTER before Phase 0 — all FID placeholders committed; cross-phase citations via FINDING REGISTER |
| C-11 | Cross-phase citation | PASS | Because block Citation column: "Citation (Phase N, F[N]-seq)" — hybrid key format in column header |
| C-12 | Segment scoring | PASS | Phase 3 table carries `Fit Score (1-10)` column in all variations; V-03/V-04/V-05 add Inertia Lock-in without removing it |
| C-13 | Hypothesis-prior anchoring | PASS | Phase 0 experiment lifecycle schema includes `Prior Confidence (fill-now)` column before any evidence phase |
| C-14 | Phase boundaries | PASS | `[COMPLETE BEFORE PHASE N]` gate annotations on all phase headers |
| C-15 | Feasibility traffic-light | PASS | Phase 2 table: `Severity (R/Y/G)` column |
| C-16 | Pre-seeded FINDING REGISTER | PASS | FINDING REGISTER appears under `[PRE-SEED BEFORE PHASE 0]` annotation, before Phase 0 section |
| C-17 | 6-slot Because block | PASS | Exactly 6 rows specified: Phase 0/PRIOR, Phase 1a/INERTIA, Phase 1b/RIVALS, Phase 2/FEASIBILITY, Phase 3/MARKET, Phase 4/WEB EVIDENCE |
| C-18 | Recommendation record structure | PASS | 4 required columns (FID, Recommendation, Confidence, Confidence Rationale) all present; C-47 adds 5th column — C-18 not triggered per its interaction note |
| C-19 | Counter-evidence record | PASS | Counter-evidence table: `Counter-Evidence / Qualifying FID / Recommended Next Step / Condition` columns present |
| C-20 | Gate annotations in headers | PASS | Every phase section header (0 through 5) carries `[COMPLETE BEFORE PHASE N]` or equivalent |
| C-21 | Phase 1a/1b gate | PASS | Phase 1a header: `[COMPLETE BEFORE Phase 1b]` distinct from Phase 2 gate |
| C-22 | Hybrid citations | PASS | Because block Citation column header encodes format: "Citation (Phase N, F[N]-seq)" |
| C-23 | Domain-specific column headers | PASS | No generic "Field/Value/Item/Note" placeholders — all column names domain-specific across all tables |
| C-24 | 1a/1b synthesis slot split | PASS | Because block has distinct "Phase 1a / INERTIA" and "Phase 1b / RIVALS" rows |
| C-25 | Because table column schema | PASS | 4 named columns: Phase, Label, Citation, Claim |
| C-26 | Per-rival response strategy | PASS | Phase 1b table includes `Response Strategy` column; FINDING REGISTER labels include "with response strategy" per Phase 1b FID |
| C-27 | Prose-free structural sufficiency | PASS | All C-01..C-26 verifiable from headers, table structure, gate annotations, FINDING REGISTER — no prose load-bearing for those criteria |
| C-28 | Phase 0 experiment lifecycle schema | PASS | Phase 0 schema: 7 columns including `Expected Result (Phase 0, fill-now)` and `Actual Outcome (Phase 5, defer-to-Phase-5)` |
| C-29 | Inertia primacy dual-signal | PASS | Phase 1a header: `[INERTIA IS THE PRIMARY COMPETITOR]` sub-annotation; FINDING REGISTER F1a-01: "`primary competitor: YES`" |
| C-30 | Phase 5 bold sub-table labels | PASS | **Hypothesis resolution:**, **Recommendation record:**, **Counter-evidence:**, **Counter Block:** — all four bold labels present |
| C-31 | Phase 1a Switching Cost column | PASS | FINDING REGISTER Phase 1a: 4-column extended schema with `Switching Cost` column; Switching Cost prose definition included |
| C-32 | Phase 5 Counter Block schema | PASS | Dedicated **Counter Block:** sub-table with `FID / Counter Claim / Rebuttal` columns |
| C-33 | Confidence calibration quantified thresholds | PASS | H=80%+, M=50-79%, L<50% encoded in confidence column headers |
| C-34 | Confidence threshold propagated via top-level schema | PASS | `Confidence (H=80%+ / M=50-79% / L<50%)` in evidence entry schema at SCHEMA PREAMBLE — pre-Phase-0 definition |
| C-35 | Prior Confidence into Phase 5 hypothesis resolution | PASS | Phase 5 hypothesis resolution schema: `FID / Hypothesis / Prior Confidence / Actual Outcome (Phase 5) / Status` |
| C-36 | Per-phase FINDING REGISTER closure directives | PASS | "Close FINDING REGISTER Phase N rows" directive after each evidence phase |
| C-37 | Hypothesis resolution schema pre-defined in SCHEMA PREAMBLE | PASS | Phase 5 hypothesis resolution schema defined in SCHEMA PREAMBLE; Phase 5 carries "Fill the Phase 5 hypothesis resolution schema from the Schema Preamble" directive |
| C-38 | Column-specific FINDING REGISTER closure directives | PASS | "[columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)]" bracket enumeration in all closure directives |
| C-39 | Fill-forward directive as Phase 5 header annotation | PASS | Phase 5 section header: `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]` |
| C-40 | Bracket notation for closure directives | PASS | `[columns: ...]` bracket notation in all FINDING REGISTER closure directives |
| C-41 | Named-schema enumeration in Phase 5 fill-forward | PASS | Phase 5 header names each schema individually: "hypothesis-resolution, recommendation-record, because-block" |
| C-42 | Per-column temporal commit annotation | PASS | Closure directives annotate each column: `(key, fill-now)`, `(fill-now)`, `(defer-to-Phase-5)` per column |
| C-43 | Temporal commit encoded at SCHEMA PREAMBLE definition time | PASS | Phase 0 schema column headers in SCHEMA PREAMBLE carry `(fill-now)` and `(defer-to-Phase-5)` annotations at definition time |
| C-44 | Per-phase minimum evidence count annotations | PASS | All phase headers carry `[min: N ...]` brackets: `[min: 3 experiments]`, `[min: 1 inertia entry]`, `[min: 2 named rivals]`, `[min: 1 named barrier]`, `[min: 1 segment...]`, `[min: 1 web-sourced entry...]` |
| C-45 | PRE-COMMITMENT block before SCHEMA PREAMBLE | PASS | PRE-COMMITMENT block appears before SCHEMA PREAMBLE in all five variations — hypotheses and default recommendation committed in plain form before schema columns visible |
| C-46 | Evidence density closure annotation | PASS | "Evidence density: [actual count] of [min] — gate clears when actual >= min" present after each evidence phase (0-4) in all variations |
| C-47 | PRE-COMMITMENT recommendation confidence with falsification condition | PASS | PRE-COMMITMENT includes "Default recommendation confidence: {H/M/L}" and "Falsification condition for recommendation: I would update to..."; recommendation record schema carries `Prior Recommendation Confidence (from PRE-COMMITMENT)` column |
| C-48 | FINDING REGISTER expected FID count annotations | PASS | All phase-group headers in FINDING REGISTER carry `[expect: N FIDs]` annotations: e.g., `*Phase 0 register [expect: 3 FIDs]:*`, `*Phase 1b register [expect: 2+ FIDs]:*` |
| C-49 | Phase 5 synthesis completeness exit annotation | PASS | "Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty]" present in all |

**Aspirational score: 20.5 / 20.5 — all five variations**

---

## Per-variation composite scores

| Variation | Essential | Recommended | Aspirational | **Composite** | R20 candidates demonstrated |
|---|---|---|---|---|---|
| V-01 | 60.0 | 30.0 | 20.5 | **110.5 / 110.5** | C-50 (gate check) |
| V-02 | 60.0 | 30.0 | 20.5 | **110.5 / 110.5** | C-51 (rec delta sentence) |
| V-03 | 60.0 | 30.0 | 20.5 | **110.5 / 110.5** | C-52 (inertia lock-in column) |
| V-04 | 60.0 | 30.0 | 20.5 | **110.5 / 110.5** | C-50 + C-51 |
| V-05 | 60.0 | 30.0 | 20.5 | **110.5 / 110.5** | C-50 + C-51 + C-52 |

**All variations: 110.5/110.5. All essential criteria pass across all five.**

---

## Ranking

Within rubric v19 all variations are tied at the maximum. Rank is therefore determined by number of next-rubric candidates demonstrated — a measure of structural density beyond current rubric ceiling:

| Rank | Variation | Rubric v19 Score | R20 candidates |
|---|---|---|---|
| 1 | **V-05** | 110.5 | 3 (C-50, C-51, C-52) |
| 2 | **V-04** | 110.5 | 2 (C-50, C-51) |
| 3 | **V-01** | 110.5 | 1 (C-50) |
| 3 | **V-02** | 110.5 | 1 (C-51) |
| 3 | **V-03** | 110.5 | 1 (C-52) |

V-05 is the top-scoring variation by structural density.

---

## Excellence signals from V-05

**ES-1 — Phase boundary binary gate check (C-50 pattern)**
Each evidence phase (0 through 4) closes with a three-condition binary gate check annotation in bracket notation:
```
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase N+1.
```
This consolidates three previously independent close conditions (C-44 minimum count, C-36 register closure, C-46 density annotation) into a single scannable line. A reviewer verifying phase compliance previously had to check three structural locations; the gate check reduces that to one binary artifact. The `proceed to Phase N+1` qualifier makes the gate directional — it names the next phase explicitly, preventing ambiguity about which phase follows.

**ES-2 — Recommendation calibration delta as explicit sentence (C-51 pattern)**
Immediately after the recommendation record table in Phase 5, V-05 adds:
```
Recommendation calibration delta: Confidence moved from {prior H/M/L} (PRE-COMMITMENT) to {final H/M/L}. Moved {up / down / unchanged} because {cite FIDs — not label alone}.
```
C-47 creates two columns in the recommendation record table (Prior Recommendation Confidence and final Confidence) that contain the same before/after data — but the delta direction and FID-cited reason are implicit in the table and require column comparison to extract. The delta sentence makes the movement explicit as a structural artifact parallel in form to the BECAUSE block's phase-by-phase contribution narrative. The FID citation requirement ("not label alone") in the sentence directly mirrors the column-level citation requirement from C-09/C-47.

**ES-3 — Phase 3 inertia through-line column (C-52 pattern)**
Phase 3 segment table gains `Inertia Lock-in (H/M/L)` as a sixth column:
```
| Segment | Signal | Direction | Fit Score (1-10) | Inertia Lock-in (H/M/L) | FID |
```
with a tripartite definition: "H = embedded routine / high re-learning cost / low pain with status quo; M = moderate switching friction; L = unmet pain / low prior investment / motivated to switch." This closes a structural gap between Phase 1a (product-level switching cost — C-31's Switching Cost column) and Phase 5 counter-evidence (where high-lock-in segments are named as the reason inertia may still win for a high-fit product). The column definition mirrors C-31's H/M/L scale semantically, creating an explicit inertia through-line: Phase 1a quantifies product-level inertia → Phase 3 quantifies per-segment inertia → Phase 5 counter-evidence can cite specific high-lock-in segments by FID. V-05 also updates the Phase 5 counter-evidence prompt: "When citing high-lock-in segments from Phase 3, note the Inertia Lock-in rating as a qualifying condition," closing the data-flow from Phase 3 column to Phase 5 counter-evidence table.

---

## Summary table

| Metric | Value |
|---|---|
| Top variation | V-05 |
| Top score | 110.5 / 110.5 |
| All essential pass | Yes (all 5 variations) |
| New patterns demonstrated (V-05) | 3 (C-50, C-51, C-52) |
| Structural gaps closed by V-05 | Phase boundary enforcement, recommendation delta visibility, inertia through-line Phase 1a→3→5 |

```json
{"top_score": 110.5, "all_essential_pass": true, "new_patterns": ["Phase gate binary check consolidates min/register/density into single bracket-notation line at each evidence phase boundary — C-50 candidate", "Recommendation calibration delta sentence after Phase 5 recommendation record table makes C-47 before/after confidence movement explicit with FID-cited reason — C-51 candidate", "Phase 3 Inertia Lock-in column (H/M/L) creates structural Phase 1a→Phase 3→Phase 5 inertia through-line connecting product-level switching cost to per-segment behavioral resistance to counter-evidence — C-52 candidate"]}
```
