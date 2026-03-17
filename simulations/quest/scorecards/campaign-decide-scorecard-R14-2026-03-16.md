## campaign-decide — Round 14 Scorecard (Rubric v13)

---

### Evaluation Framework

**Scoring model (v13):**
- Essential C-01..C-05: 12 pts each → 60 pts (any fail = output fails)
- Recommended C-06..C-08: 10 pts each → 30 pts
- Aspirational C-09..C-36: 0.5 pts each → 14 pts
- Max composite: **104.0**

---

### V-01 — C-35 schema preamble propagation

**Variation axis:** Phase 5 hypothesis resolution schema defined in SCHEMA PREAMBLE (before Phase 0).

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Recommendation stated | Essential | PASS | `Recommendation` column in Phase 5 recommendation record sub-table |
| C-02 Confidence stated | Essential | PASS | `Confidence (H=80%+ / M=50-79% / L<50%)` named column in recommendation record |
| C-03 All six domains | Essential | PASS | Phase 0 through Phase 5 all present with explicit headers |
| C-04 Inertia-first ordering | Essential | PASS | Phase 1a carries `[COMPLETE BEFORE Phase 1b]` gate; inertia precedes Phase 1b structurally |
| C-05 Evidence-to-recommendation traceability | Essential | PASS | BECAUSE block Citation column + Confidence Rationale "(cite FIDs — not label alone)" |
| C-06 Structured brief format | Recommended | PASS | FINDING REGISTER header, titled phase sections, 4 bold Phase 5 sub-tables |
| C-07 Risk / counter-evidence | Recommended | PASS | `Counter-Evidence \| Qualifying FID \| Recommended Next Step \| Condition` |
| C-08 Hypothesis disposition | Recommended | PASS | `**Hypothesis resolution:**` sub-table with CONFIRMED/REFUTED/INCONCLUSIVE Status column |
| C-09 Confidence calibration rationale column | Aspirational | PASS | `Confidence Rationale (cite FIDs — not label alone)` in recommendation schema |
| C-10 FID consistency | Aspirational | PASS | Pre-seeded FINDING REGISTER enforces FID universe before evidence phases |
| C-11 Cross-phase citation | Aspirational | PASS | `Citation (Phase N, F[N]-seq)` in Because block schema definition |
| C-12 Segment scoring | Aspirational | PASS | `Fit Score (1-10)` column in Phase 3 scout-market table |
| C-13 Hypothesis-prior anchoring | Aspirational | PASS | Phase 0 schema carries `Prior Confidence` and `Expected Result (Phase 0)` columns |
| C-14 Phase boundaries | Aspirational | PASS | Every phase header carries `[COMPLETE BEFORE PHASE N]` annotation |
| C-15 Feasibility traffic-light | Aspirational | PASS | `Severity (R/Y/G)` column in Phase 2 scout-feasibility table |
| C-16 Pre-seeded FINDING REGISTER | Aspirational | PASS | `[PRE-SEED BEFORE PHASE 0 — all FID placeholders committed here]` at document top |
| C-17 6-slot Because block | Aspirational | PASS | Schema rows: Phase 0/PRIOR, 1a/INERTIA, 1b/RIVALS, 2/FEASIBILITY, 3/MARKET, 4/WEB EVIDENCE |
| C-18 Recommendation record structure | Aspirational | PASS | Four columns: FID, Recommendation, Confidence, Confidence Rationale |
| C-19 Counter-evidence record | Aspirational | PASS | Four columns: Counter-Evidence, Qualifying FID, Recommended Next Step, Condition |
| C-20 Gate annotations in headers | Aspirational | PASS | All phase headers carry gate annotations; Phase 5 `[COMPLETE PHASE 5 LAST]` accepted |
| C-21 Phase 1a/1b gate | Aspirational | PASS | `[COMPLETE BEFORE Phase 1b]` on Phase 1a header, distinct from inter-phase gate |
| C-22 Hybrid citations | Aspirational | PASS | Citation column header reads `Citation (Phase N, F[N]-seq)` — format encoded structurally |
| C-23 Domain-specific column headers | Aspirational | PASS | No generic placeholders; all headers domain-specific |
| C-24 1a/1b synthesis slot split | Aspirational | PASS | Because block schema names Phase 1a/INERTIA and Phase 1b/RIVALS as distinct rows |
| C-25 Because table column schema | Aspirational | PASS | Exactly 4 columns: Phase, Label, Citation, Claim |
| C-26 Per-rival response strategy | Aspirational | PASS | `Response Strategy` column in Phase 1b table; register note "labels include 'with response strategy'" |
| C-27 Prose-free structural sufficiency | Aspirational | PASS | All C-01..C-26 verifiable from column headers, table schemas, gate annotations, register labels |
| C-28 Phase 0 experiment lifecycle schema | Aspirational | PASS | 7-column schema with `Expected Result (Phase 0)` and `Actual Outcome (Phase 5)` temporal encoding |
| C-29 Inertia primacy dual-signal | Aspirational | PASS | Header: `[INERTIA IS THE PRIMARY COMPETITOR]`; register: F1a-01 `primary competitor: YES` |
| C-30 Phase 5 bold sub-table labels | Aspirational | PASS | Four bold labels: **Hypothesis resolution:**, **Recommendation record:**, **Counter-evidence:**, **Counter Block:** |
| C-31 Phase 1a FINDING REGISTER Switching Cost | Aspirational | PASS | 4-column extended schema: FID, Finding Summary, Primary Competitor, Switching Cost |
| C-32 Phase 5 Counter Block schema | Aspirational | PASS | Structurally distinct sub-table: `FID \| Counter Claim \| Rebuttal` |
| C-33 Confidence calibration thresholds | Aspirational | PASS | H=80%+/M=50-79%/L<50% encoded in evidence entry schema column header |
| C-34 Threshold in pre-Phase-0 schema definition | Aspirational | PASS | `Confidence (H=80%+ / M=50-79% / L<50%)` in SCHEMA PREAMBLE evidence entry and recommendation schemas |
| C-35 Prior Confidence in Phase 5 hypothesis resolution | Aspirational | PASS | Phase 5 hypothesis resolution schema defined in SCHEMA PREAMBLE with `Prior Confidence` column; Phase 5 instruction: "Fill the Phase 5 hypothesis resolution schema from the Schema Preamble" — maximum propagation depth |
| C-36 Per-phase FINDING REGISTER closure directives | Aspirational | PASS | `Close FINDING REGISTER Phase N rows` after Phase 0, 1a, 1b, 2, 3, 4, 5 |

**V-01 Score: 104.0 / 104.0** — All 36 criteria PASS.
Essential pass: ✓ All 5 essential pass.

---

### V-02 — C-36 directive granularity

**Variation axis:** Close directives name specific columns being committed (column-specific granularity).

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | PASS | Recommendation column in Phase 5 record |
| C-02 | Essential | PASS | Confidence column with H/M/L scale |
| C-03 | Essential | PASS | All phases present |
| C-04 | Essential | PASS | `[COMPLETE BEFORE Phase 1b]` gate on Phase 1a |
| C-05 | Essential | PASS | BECAUSE block Citation + Confidence Rationale cite FIDs |
| C-06 | Recommended | PASS | Structured FINDING REGISTER + phase sections + Phase 5 sub-tables |
| C-07 | Recommended | PASS | 4-column counter-evidence sub-table |
| C-08 | Recommended | PASS | Hypothesis resolution sub-table with Status column |
| C-09 | Aspirational | PASS | `Confidence Rationale (cite FIDs — not label alone)` in recommendation schema |
| C-10 | Aspirational | PASS | Pre-seeded register |
| C-11 | Aspirational | PASS | `Citation (Phase N, F[N]-seq)` in Because block schema |
| C-12 | Aspirational | PASS | `Fit Score (1-10)` in Phase 3 |
| C-13 | Aspirational | PASS | `Prior Confidence` and `Expected Result (Phase 0)` in Phase 0 schema |
| C-14 | Aspirational | PASS | Gate annotations on all phase headers |
| C-15 | Aspirational | PASS | `Severity (R/Y/G)` in Phase 2 |
| C-16 | Aspirational | PASS | `[PRE-SEED BEFORE PHASE 0]` at document top |
| C-17 | Aspirational | PASS | 6-slot Because block schema defined |
| C-18 | Aspirational | PASS | 4-column recommendation record schema |
| C-19 | Aspirational | PASS | 4-column counter-evidence schema |
| C-20 | Aspirational | PASS | Gate annotations on all phases |
| C-21 | Aspirational | PASS | `[COMPLETE BEFORE Phase 1b]` distinct on Phase 1a |
| C-22 | Aspirational | PASS | Citation column header encodes format |
| C-23 | Aspirational | PASS | All column headers domain-specific |
| C-24 | Aspirational | PASS | 1a/INERTIA and 1b/RIVALS as distinct rows |
| C-25 | Aspirational | PASS | Because block: Phase, Label, Citation, Claim |
| C-26 | Aspirational | PASS | `Response Strategy` column + register note per FID |
| C-27 | Aspirational | PASS | All C-01..C-26 structurally verifiable; column-specific directives add no prose load |
| C-28 | Aspirational | PASS | 7-column Phase 0 lifecycle schema with temporal encoding |
| C-29 | Aspirational | PASS | Dual-signal: header annotation + F1a-01 `primary competitor: YES` |
| C-30 | Aspirational | PASS | Four bold Phase 5 sub-table labels |
| C-31 | Aspirational | PASS | 4-column Phase 1a extended schema |
| C-32 | Aspirational | PASS | `FID \| Counter Claim \| Rebuttal` — structurally distinct |
| C-33 | Aspirational | PASS | Thresholds encoded in evidence schema column header |
| C-34 | Aspirational | PASS | Threshold in SCHEMA PREAMBLE pre-Phase-0 |
| C-35 | Aspirational | PASS | Phase 5 `**Hypothesis resolution:**` table carries `Prior Confidence` column; instruction "copy from Phase 0 experiment rows" — C-35 satisfied at Phase 5; not in preamble but criterion does not require it |
| C-36 | Aspirational | PASS | Column-specific close directives: Phase 0 "fill Finding Summary from experiment outcomes"; Phase 1a "fill Finding Summary, Primary Competitor flag, and Switching Cost"; Phase 1b "fill Finding Summary and 'with response strategy' note per FID"; all phases through Phase 5 |

**V-02 Score: 104.0 / 104.0** — All 36 criteria PASS.
Essential pass: ✓

---

### V-03 — Phrasing register (descriptive for C-36)

**Variation axis:** Closure directives use documentation/descriptive phrasing rather than imperative commands.

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01..C-05 | Essential | PASS | All structural elements present for full traceability chain |
| C-06..C-08 | Recommended | PASS | Structured brief with FINDING REGISTER, phase headers, 4 Phase 5 sub-tables |
| C-09 | Aspirational | PASS | `Confidence Rationale (cite FIDs — not label alone)` in schema |
| C-10 | Aspirational | PASS | Pre-seeded register at document top |
| C-11 | Aspirational | PASS | `Citation (Phase N, F[N]-seq)` in Because block schema |
| C-12 | Aspirational | PASS | `Fit Score (1-10)` in Phase 3 |
| C-13 | Aspirational | PASS | `Prior Confidence` and `Expected Result (Phase 0)` in Phase 0 schema |
| C-14 | Aspirational | PASS | Gate annotations on all phase headers |
| C-15 | Aspirational | PASS | `Severity (R/Y/G)` in Phase 2 |
| C-16 | Aspirational | PASS | `[PRE-SEED BEFORE PHASE 0]` annotation; preamble note "committed phase-by-phase" |
| C-17 | Aspirational | PASS | 6-slot Because block schema defined |
| C-18..C-22 | Aspirational | PASS | All four sub-table schemas and citation format present structurally |
| C-23 | Aspirational | PASS | Domain-specific headers throughout |
| C-24..C-25 | Aspirational | PASS | 1a/1b split in Because schema; 4-column Because schema |
| C-26 | Aspirational | PASS | `Response Strategy` column + register closure note "each Finding Summary includes 'with response strategy'" |
| C-27 | Aspirational | PASS | All C-01..C-26 verifiable from structural elements; descriptive closure notes act as structural annotations, not prose load-bearing |
| C-28 | Aspirational | PASS | 7-column Phase 0 lifecycle schema with temporal slot encoding |
| C-29 | Aspirational | PASS | Dual-signal present: header `[INERTIA IS THE PRIMARY COMPETITOR]` + F1a-01 `primary competitor: YES` |
| C-30 | Aspirational | PASS | Four bold sub-table labels in Phase 5 |
| C-31 | Aspirational | PASS | 4-column Phase 1a extended schema with Switching Cost |
| C-32 | Aspirational | PASS | Structurally distinct Counter Block with FID/Counter Claim/Rebuttal schema |
| C-33..C-34 | Aspirational | PASS | Confidence thresholds in SCHEMA PREAMBLE column header |
| C-35 | Aspirational | PASS | Phase 5 **Hypothesis resolution:** carries `Prior Confidence` column; prose introduction ("The resolution table carries Prior Confidence forward from Phase 0") is explanatory only — C-35 satisfied by table column header alone |
| C-36 | Aspirational | PASS | Descriptive closure notes satisfy "or equivalent" clause: "*Phase N register rows are committed here before Phase N+1 begins.*" after each of Phase 0 through Phase 5 |

**V-03 Score: 104.0 / 104.0** — All 36 criteria PASS.
Essential pass: ✓

Note on C-27 in V-03: Descriptive phrasing shifts reading experience but does not make any criterion's verification depend on prose — all 36 criteria remain structurally verifiable from schema headers and structural annotations. C-27 PASS is secure.

---

### V-04 — Combined: C-35/C-36 two-stage architecture note

**Variation axis:** Explicit "Commit architecture" and "Calibration architecture" notes in preamble; Phase 5 hypothesis resolution schema in preamble; Stage-labeled closure directives.

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01..C-05 | Essential | PASS | Full structural chain present |
| C-06..C-08 | Recommended | PASS | Structured format with all required sub-tables |
| C-09..C-34 | Aspirational | PASS | All prior aspirational criteria encoded structurally |
| C-35 | Aspirational | PASS | Phase 5 hypothesis resolution schema in SCHEMA PREAMBLE: `FID \| Hypothesis \| Prior Confidence \| Actual Outcome (Phase 5) \| Status`; "Calibration architecture" note names this explicitly; Phase 5 instruction "Use the Phase 5 hypothesis resolution schema from the Schema Preamble. Prior Confidence copied from Phase 0" |
| C-36 | Aspirational | PASS | Stage-labeled closure directives: "Close FINDING REGISTER Phase N rows. (Stage 2 — Phase N commit complete.)" after all 5 evidence phases through Phase 5; "Commit architecture" preamble note defines the Stage 2 protocol at architecture level |
| C-27 | Aspirational | PASS | "Commit architecture" and "Calibration architecture" are structural notes that add interpretability; they don't create prose load-bearing for any C-01..C-26 criterion |

**V-04 Score: 104.0 / 104.0** — All 36 criteria PASS.
Essential pass: ✓

Excellence note: "Commit architecture" + "Calibration architecture" preamble notes make C-35 and C-36 interpretable at the architectural level before reading any phase instructions — distinctive readability signal.

---

### V-05 — Full Integration (all 36 criteria, targeting 104.0)

**Variation axis:** Phase 5 hypothesis resolution schema in SCHEMA PREAMBLE (V-01 axis) + column-specific close directives (V-02 axis) + full structural encoding with no prose load-bearing.

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | PASS | `Recommendation` column in pre-seeded Phase 5 recommendation record |
| C-02 | Essential | PASS | `Confidence (H=80%+ / M=50-79% / L<50%)` named column |
| C-03 | Essential | PASS | Phase 0 through Phase 5, all with titled headers and structural content |
| C-04 | Essential | PASS | Phase 1a `[COMPLETE BEFORE Phase 1b]`; Phase 1b follows structurally |
| C-05 | Essential | PASS | BECAUSE block Citation column + Confidence Rationale FID requirement |
| C-06 | Recommended | PASS | FINDING REGISTER + 6 titled phase sections + 4 Phase 5 sub-tables |
| C-07 | Recommended | PASS | `Counter-Evidence \| Qualifying FID \| Recommended Next Step \| Condition` |
| C-08 | Recommended | PASS | `**Hypothesis resolution:**` sub-table with Status column |
| C-09 | Aspirational | PASS | `Confidence Rationale (cite FIDs — not label alone)` in recommendation schema preamble |
| C-10 | Aspirational | PASS | Pre-seeded FINDING REGISTER guarantees all FIDs registered before use |
| C-11 | Aspirational | PASS | `Citation (Phase N, F[N]-seq)` in Because block column header |
| C-12 | Aspirational | PASS | `Fit Score (1-10)` column in Phase 3 |
| C-13 | Aspirational | PASS | `Prior Confidence` + `Expected Result (Phase 0)` in Phase 0 experiment lifecycle schema |
| C-14 | Aspirational | PASS | Gate annotations on all phase headers Phase 0..Phase 5 |
| C-15 | Aspirational | PASS | `Severity (R/Y/G)` in Phase 2 feasibility table |
| C-16 | Aspirational | PASS | `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]` at document top |
| C-17 | Aspirational | PASS | 6-slot Because block with fixed slot names in schema |
| C-18 | Aspirational | PASS | Exactly 4 columns: FID, Recommendation, Confidence, Confidence Rationale |
| C-19 | Aspirational | PASS | Exactly 4 columns: Counter-Evidence, Qualifying FID, Recommended Next Step, Condition |
| C-20 | Aspirational | PASS | Gate annotations on all phase headers Phase 0..5 |
| C-21 | Aspirational | PASS | `[COMPLETE BEFORE Phase 1b]` distinct on Phase 1a header |
| C-22 | Aspirational | PASS | `Citation (Phase N, F[N]-seq)` encodes format in column header |
| C-23 | Aspirational | PASS | All column headers domain-specific; no generic placeholders |
| C-24 | Aspirational | PASS | Because schema distinguishes Phase 1a/INERTIA and Phase 1b/RIVALS |
| C-25 | Aspirational | PASS | Because table: Phase, Label, Citation, Claim — exactly 4 columns |
| C-26 | Aspirational | PASS | `Response Strategy` column in Phase 1b; register "Phase 1b FID labels include 'with response strategy'" |
| C-27 | Aspirational | PASS | No prose load-bearing for any criterion C-01..C-26; all verifiable from schemas, gate annotations, and register labels; column-specific close directives are structural — strongest C-27 compliance of all five variations |
| C-28 | Aspirational | PASS | 7-column Phase 0 schema: FID, Hypothesis, Investigation Method, Prior Confidence, Expected Result (Phase 0), Actual Outcome (Phase 5), Status — temporal encoding explicit |
| C-29 | Aspirational | PASS | Header `[INERTIA IS THE PRIMARY COMPETITOR]` + F1a-01 `primary competitor: YES` / Switching Cost = H in register |
| C-30 | Aspirational | PASS | Four distinct bold labels: **Hypothesis resolution:**, **Recommendation record:**, **Counter-evidence:**, **Counter Block:** |
| C-31 | Aspirational | PASS | Phase 1a register 4-column extended schema: FID, Finding Summary, Primary Competitor, Switching Cost |
| C-32 | Aspirational | PASS | Counter Block structurally distinct: `FID \| Counter Claim \| Rebuttal`; labeled differently from Counter-evidence |
| C-33 | Aspirational | PASS | H=80%+/M=50-79%/L<50% in evidence entry schema column header |
| C-34 | Aspirational | PASS | Threshold in SCHEMA PREAMBLE evidence entry schema and recommendation schema column headers |
| C-35 | Aspirational | PASS | Phase 5 hypothesis resolution schema in SCHEMA PREAMBLE: `FID \| Hypothesis \| Prior Confidence \| Actual Outcome (Phase 5) \| Status`; Phase 5 instruction "Copy Prior Confidence values from Phase 0 experiment rows" — C-35 verifiable from preamble alone before Phase 5 executes |
| C-36 | Aspirational | PASS | Column-specific close directives after all evidence phases: Phase 0 "fill Finding Summary from experiment outcomes"; Phase 1a "fill Finding Summary, Primary Competitor flag, and Switching Cost"; Phase 1b "fill Finding Summary with 'with response strategy' note per FID"; Phase 2 "fill Finding Summary from barrier assessments"; Phase 3 "fill Finding Summary from segment signals"; Phase 4 "fill Finding Summary from web evidence items"; Phase 5 "fill Finding Summary for all synthesis sub-table entries" |

**V-05 Score: 104.0 / 104.0** — All 36 criteria PASS.
Essential pass: ✓

---

### Composite Scoreboard

| Variation | Essential (60) | Recommended (30) | Aspirational (14) | Total | Rank |
|-----------|---------------|-----------------|------------------|-------|------|
| V-01 | 60.0 | 30.0 | 14.0 | **104.0** | T-1 |
| V-02 | 60.0 | 30.0 | 14.0 | **104.0** | T-1 |
| V-03 | 60.0 | 30.0 | 14.0 | **104.0** | T-1 |
| V-04 | 60.0 | 30.0 | 14.0 | **104.0** | T-1 |
| V-05 | 60.0 | 30.0 | 14.0 | **104.0** | T-1 |

All five variations achieve the maximum 104.0/104.0. The scoring model has no remaining headroom — all 36 criteria pass across all variations.

---

### Excellence Signals (from V-05 as canonical full-integration variation)

**1. Phase 5 hypothesis resolution schema pre-committed in SCHEMA PREAMBLE (C-35 at maximum propagation depth)**

V-01, V-04, and V-05 all define the Phase 5 hypothesis resolution schema (`FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status`) in the SCHEMA PREAMBLE before Phase 0, rather than first introducing it at Phase 5. This means C-35 is verifiable at document-top — a reader can confirm the before/after calibration architecture exists before any evidence phase executes. V-05's phrasing: "pre-committed here so Prior Confidence is architecturally visible before evidence runs." The Phase 5 instruction then just says "Use the Phase 5 hypothesis resolution schema from the Schema Preamble" — a structural reference, not a new introduction.

**2. Column-specific close directives (C-36 hardened to fill discipline)**

V-02 and V-05 name the specific columns being committed at each phase closure: "fill Finding Summary, Primary Competitor flag, and Switching Cost" (Phase 1a); "fill Finding Summary with 'with response strategy' note per FID" (Phase 1b). The generic `Close FINDING REGISTER Phase N rows` satisfies C-36 minimally; column-named directives make the two-stage commit self-documenting at each boundary and reduce the risk of agents deferring column fills. V-05 applies this consistently across all 6 phases.

**3. Named architecture notes in preamble make criteria interpretable at design level (V-04 distinctive)**

V-04's "Commit architecture" and "Calibration architecture" notes in the SCHEMA PREAMBLE name both disciplines at the structural top: Stage 1 (pre-seed) / Stage 2 (per-phase closure) and Prior-confidence-at-Phase-0 / Actual-outcome-at-Phase-5. This makes C-35 and C-36 interpretable from the architectural description alone, before reading any phase instruction. While all variations pass C-35 and C-36, V-04 makes the _intent_ of both criteria visible at the preamble level without requiring the reader to parse per-phase directives.

---

### Round Summary

R14 achieves the theoretical ceiling: **all five variations score 104.0/104.0**. The rubric v13 has no remaining discriminating power over well-formed variations that encode C-35 and C-36. The exploration axes confirm:

- C-35 is robust to encoding location (preamble vs Phase 5 inline) — either satisfies the criterion
- C-36 is robust to phrasing register (imperative, descriptive, stage-labeled, or column-specific) — all forms satisfy "or equivalent"
- C-27 passes in all five variations, including V-03 (descriptive phrasing), confirming the structural encoding is complete

The rubric v13 is at maximum coverage. Future rounds would require new criteria to extract from edge-case failures, or a variation that deliberately omits a current criterion to verify discrimination.

---

```json
{"top_score": 104.0, "all_essential_pass": true, "new_patterns": ["Phase 5 hypothesis resolution schema pre-committed in SCHEMA PREAMBLE — C-35 verifiable at document-top before any evidence phase executes, enabling architectural audit independent of Phase 5 completion", "Column-specific close directives naming the columns being committed at each phase boundary — two-stage commit discipline self-documenting per phase, reducing deferred-fill risk beyond generic Close Phase N rows", "Named Commit architecture and Calibration architecture notes in SCHEMA PREAMBLE — C-35 and C-36 interpretable at the structural-design level from preamble alone, without reading per-phase instructions"]}
```
