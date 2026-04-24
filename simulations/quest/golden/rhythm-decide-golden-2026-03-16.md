Written to `simulations/quest/golden/campaign-decide-golden-2026-03-16.md`.

The document contains:

1. **Frontmatter** — as specified, with `score: 110.5` and `rubric_final: campaign-decide-rubric-v20`
2. **Prompt body** — verbatim from the QU5 simplified version (1,943 words, 20.4% reduction, all 52 criteria pass), with dashes converted to `--` per ASCII-safe project rules
3. **What Made It Golden** — five patterns:
   - PRE-COMMITMENT before schema (priors locked before columns prime the answer)
   - Inertia as named primary competitor propagated through Phase 3 via the Switching Cost → Inertia Lock-in column chain
   - Temporal commit architecture (single definition at SCHEMA PREAMBLE, confirmed not redeclared downstream)
   - Per-phase gate check binary verdict (three conditions → one auditable Y/N line)
   - Recommendation calibration delta sentence (prior-to-final in one FID-cited scannable line)
4. **Rubric v20 criteria summary** — all 52 criteria listed across Essential / Recommended / Aspirational tiers with the v20 max of 112.0
esult if true = {what you would observe}
H2 — {second falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H3 — {third falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}

Default recommendation before evidence: {COMMIT / PAUSE / PIVOT / ABANDON}
Default recommendation confidence: {H / M / L} — how confident are you in this default, before any evidence?
Falsification condition for recommendation: I would update to {alt-recommendation} if I learned: {condition}
Primary uncertainty: {what is most unknown about `{topic}`?}

These are locked. The schema below governs format; these values govern content. Do not let the schema change what you wrote.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

*Evidence entry schema* — all evidence tables use this schema. Confidence calibration scale encoded in header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — temporal commit encoded in column headers at definition time. Fill-now columns are committed at Phase 0 close; deferred columns are committed at Phase 5 close via fill-forward directive:

| FID (key, fill-now) | Hypothesis (fill-now) | Investigation Method (fill-now) | Prior Confidence (fill-now) | Expected Result (Phase 0, fill-now) | Actual Outcome (Phase 5, defer-to-Phase-5) | Status (defer-to-Phase-5) |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE. This is the single definition; all downstream closure directives confirm rather than declare.

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0 (sourced from PRE-COMMITMENT block — the locked prior cannot be revised after schema loading), enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block). Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema. Prior recommendation confidence sourced from PRE-COMMITMENT block, enabling recommendation calibration delta at Phase 5:

| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, slot names fixed:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases pre-seeded with expected FID counts aligned to phase header minimums. Deferred columns declared in Phase 0 experiment lifecycle schema above; downstream closure directives confirm, not redeclare.

*Phase 0 register [expect: 3 FIDs]:*
| FID | Finding Summary | Phase |

*Phase 1a register [expect: 1 FID] (extended schema):*
| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; adjust with evidence).
All other Phase 1a FIDs: `primary competitor: NO`.

*Phase 1b register [expect: 2+ FIDs]:*
| FID | Finding Summary | Phase | Note |

Phase 1b FID labels include "with response strategy".

*Phase 2 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 3 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 4 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 5 register [expect: 4+ FIDs]:* | FID | Finding Summary | Phase |

---

**Phase 0 -- prove-hypothesis** `[COMPLETE BEFORE PHASE 1]` `[min: 3 experiments]`
Transfer the hypotheses committed in the PRE-COMMITMENT block into Phase 0 experiment rows. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Fill all `(fill-now)` columns now (hypothesis values come from PRE-COMMITMENT block -- do not revise); `(defer-to-Phase-5)` columns left empty. Table rows only -- no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].
Evidence density: [actual experiment count] of 3 -- gate clears when actual >= 3.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] -- gate clears when all Y -- proceed to Phase 1a.

**Phase 1a -- scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
What do your users do today without `{topic}`? That behavior -- the workaround, the spreadsheet, the absence of the feature -- is your real first competitor. It has 100% market share and zero switching cost; it does not lose unless the evidence forces it to. Name it, quantify its switching cost, and record it as the primary competitor. Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].
Evidence density: [actual inertia entries] of 1 -- gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] -- gate clears when all Y -- proceed to Phase 1b.

**Phase 1b -- scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
Name the products your users would switch to. For each rival, the question is not "do they exist" but "how do you win against them specifically?" No entry without a response strategy -- if you cannot state how you win, the rival is a blocking risk, not a manageable competitor.

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now -- include "with response strategy" per FID)].
Evidence density: [actual rival count] of 2 -- gate clears when actual >= 2.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] -- gate clears when all Y -- proceed to Phase 2.

**Phase 2 -- scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
List the barriers where you genuinely do not know today whether they are solvable. Do not list known-solvable problems. Severity: R = blocking / unknown path, Y = known path / uncertain timeline, G = solved or trivially solvable.

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual barrier count] of 1 -- gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] -- gate clears when all Y -- proceed to Phase 3.

**Phase 3 -- scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score and inertia lock-in]`
Score fit numerically and rate inertia lock-in per segment. Inertia Lock-in (H/M/L): H = embedded routine / high re-learning cost / low pain with status quo; M = moderate switching friction; L = unmet pain / low prior investment / motivated to switch. Do not round up for enthusiasm.

| Segment | Signal | Direction | Fit Score (1-10) | Inertia Lock-in (H/M/L) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual segment count] of 1 -- gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] -- gate clears when all Y -- proceed to Phase 4.

**Phase 4 -- prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
At least one item must cite a source and a date. No undated or unsourced entries count toward the minimum.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual web-sourced entry count] of 1 -- gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] -- gate clears when all Y -- proceed to Phase 5.

**Phase 5 -- prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block -- from SCHEMA PREAMBLE]`
Fill the Phase 0 deferred columns -- confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)]. Then build four structurally distinct sub-tables -- one per decision artifact. No merging, no skipping. Each carries a distinct bold label and its own schema.

**Hypothesis resolution:**
Fill the Phase 5 hypothesis resolution schema from the Schema Preamble. Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
State the recommendation with confidence and a rationale that cites the findings that drove it. Compare to the PRE-COMMITMENT default recommendation and confidence -- fill the recommendation record schema from the Schema Preamble (which carries the Prior Recommendation Confidence column sourced from PRE-COMMITMENT):
| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs -- not label alone) |

Recommendation calibration delta: Confidence moved from {prior H/M/L} (PRE-COMMITMENT) to {final H/M/L}. Moved {up / down / unchanged} because {cite FIDs -- not label alone}.

**Counter-evidence:**
If nothing in the evidence argues against your recommendation, the brief is incomplete. When citing high-lock-in segments from Phase 3, note the Inertia Lock-in rating as a qualifying condition:
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
State the single strongest case for the opposing recommendation and rebut it:
| FID | Counter Claim | Rebuttal |

BECAUSE block -- exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation. Cross-reference the PRE-COMMITMENT falsification condition -- was the falsification condition encountered in the evidence?

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] -- gate clears when all four show filled.

---

## What Made It Golden

**1. PRE-COMMITMENT before schema — locks priors before columns are visible**
The PRE-COMMITMENT block commits three falsifiable hypotheses, a default recommendation, and a falsification condition in plain form before the SCHEMA PREAMBLE loads. The model cannot see the column headers when writing its priors. "These are locked. The schema below governs format; these values govern content. Do not let the schema change what you wrote." This prevents schema-induced post-hoc rationalization — the most common failure mode in structured decision prompts, where column headers prime the answer before the question is asked.

**2. Inertia as the named primary competitor — structurally enforced through Phase 3**
Inertia is not framed as context; it is the first competitor. Phase 1a carries `[INERTIA IS THE PRIMARY COMPETITOR]` in the header, FINDING REGISTER seeds `F1a-01 (inertia): primary competitor: YES` before Phase 0, and the Phase 1a extended schema includes a `Switching Cost` column that propagates inertia framing into the market phase via `Inertia Lock-in (H/M/L)` in the Phase 3 segment table. A segment with a fit score of 9 and H inertia lock-in reads differently from the same score at L -- the column makes that difference structural rather than narrative.

**3. Temporal commit architecture — single definition, confirmed not redeclared**
Every schema is defined once in the SCHEMA PREAMBLE with temporal annotations in the column headers: `(fill-now)`, `(defer-to-Phase-5)`. Downstream phases confirm which columns are live -- they never re-specify timing. "This is the single definition; all downstream closure directives confirm rather than declare." The Phase 5 fill-forward directive closes the deferred columns by referencing back to the preamble schema, keeping the temporal contract machine-verifiable at any point in the campaign.

**4. Per-phase gate check — binary go/no-go after every evidence phase**
After each evidence phase's density annotation, a three-field gate check converts the three close conditions (minimum met, FINDING REGISTER closed, density written) into a single auditable verdict: `[min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] -- gate clears when all Y`. Phases cannot silently bleed into each other. A model that skips Phase 1a closure cannot satisfy the gate check without explicitly writing `N`, which is a visible failure state rather than a silent omission.

**5. Recommendation calibration delta — prior-to-final in one scannable sentence**
Immediately after the Phase 5 recommendation record table, a standalone sentence names the movement: "Confidence moved from {prior H/M/L} (PRE-COMMITMENT) to {final H/M/L}. Moved {up / down / unchanged} because {cite FIDs -- not label alone}." The PRE-COMMITMENT prior and the post-evidence recommendation are now one sentence apart, FID-cited, with direction made explicit. The calibration delta is the structural test of whether the evidence campaign changed anything.

---

## Rubric v20 — Criteria Summary

**Max composite: 112.0 | Golden: all essential pass + composite = 112.0**

### Essential (12 pts each — 60 pts total)

| ID | Criterion |
|----|-----------|
| C-01 | Recommendation stated — COMMIT / PAUSE / PIVOT / ABANDON prompt slot present in Phase 5 recommendation record |
| C-02 | Confidence stated — named confidence column in recommendation record schema, not embedded prose |
| C-03 | All six domains covered — Phase 0 through Phase 5 present; Phase 1a/1b structurally split |
| C-04 | Inertia-first ordering — `[COMPLETE BEFORE Phase 1b]` gate on Phase 1a header |
| C-05 | Evidence-to-recommendation traceability — BECAUSE block cites Phase N, F[N]-seq hybrid keys; Recommendation record requires "cite FIDs -- not label alone" |

### Recommended (10 pts each — 30 pts total)

| ID | Criterion |
|----|-----------|
| C-06 | Structured brief format — FINDING REGISTER header, titled phase sections, Phase 5 sub-tables structurally encoded |
| C-07 | Risk / counter-evidence — Counter-evidence table with Counter-Evidence / Qualifying FID / Recommended Next Step / Condition columns |
| C-08 | Hypothesis disposition — Phase 5 hypothesis resolution sub-table with CONFIRMED / REFUTED / INCONCLUSIVE |

### Aspirational (0.5 pts each — 22.0 pts total)

| ID | Criterion |
|----|-----------|
| C-09 | Confidence calibration — "Confidence Rationale (cite FIDs -- not label alone)" in recommendation record |
| C-10 | FID consistency — pre-seeded FINDING REGISTER before Phase 0; all FID placeholders committed |
| C-11 | Cross-phase citation — Because block Citation column: "Citation (Phase N, F[N]-seq)" hybrid key format |
| C-12 | Segment scoring — Phase 3 table carries Fit Score (1-10) column |
| C-13 | Hypothesis-prior anchoring — Phase 0 experiment schema includes Prior Confidence (fill-now) column before any evidence |
| C-14 | Phase boundaries — `[COMPLETE BEFORE PHASE N]` gate annotations on all phase headers |
| C-15 | Feasibility traffic-light — Phase 2 table: Severity (R/Y/G) column |
| C-16 | Pre-seeded FINDING REGISTER — appears under `[PRE-SEED BEFORE PHASE 0]` annotation |
| C-17 | 6-slot Because block — exactly 6 rows: Phase 0/PRIOR, Phase 1a/INERTIA, Phase 1b/RIVALS, Phase 2/FEASIBILITY, Phase 3/MARKET, Phase 4/WEB EVIDENCE |
| C-18 | Recommendation record structure — 4 required columns (FID, Recommendation, Confidence, Confidence Rationale) |
| C-19 | Counter-evidence record — Counter-Evidence / Qualifying FID / Recommended Next Step / Condition |
| C-20 | Gate annotations in headers — every phase header (0 through 5) carries `[COMPLETE BEFORE PHASE N]` |
| C-21 | Phase 1a/1b gate — Phase 1a header: `[COMPLETE BEFORE Phase 1b]` distinct from Phase 2 gate |
| C-22 | Hybrid citations — Because block Citation column header encodes format: "Citation (Phase N, F[N]-seq)" |
| C-23 | Domain-specific column headers — no generic "Field/Value/Item/Note" placeholders |
| C-24 | 1a/1b synthesis slot split — Because block has distinct "Phase 1a / INERTIA" and "Phase 1b / RIVALS" rows |
| C-25 | Because table column schema — 4 named columns: Phase, Label, Citation, Claim |
| C-26 | Per-rival response strategy — Phase 1b table includes Response Strategy column; FINDING REGISTER labels include "with response strategy" |
| C-27 | Prose-free structural sufficiency — all C-01..C-26 verifiable from headers, table structure, gate annotations, FINDING REGISTER |
| C-28 | Phase 0 experiment lifecycle schema — 7 columns including Expected Result (Phase 0, fill-now) and Actual Outcome (Phase 5, defer-to-Phase-5) |
| C-29 | Inertia primacy dual-signal — Phase 1a header: `[INERTIA IS THE PRIMARY COMPETITOR]`; FINDING REGISTER F1a-01: "primary competitor: YES" |
| C-30 | Phase 5 bold sub-table labels — Hypothesis resolution, Recommendation record, Counter-evidence, Counter Block all bold |
| C-31 | Phase 1a Switching Cost column — FINDING REGISTER Phase 1a: 4-column extended schema with Switching Cost |
| C-32 | Phase 5 Counter Block schema — FID / Counter Claim / Rebuttal columns |
| C-33 | Confidence calibration quantified thresholds — H=80%+, M=50-79%, L<50% encoded in confidence column headers |
| C-34 | Confidence threshold propagated via top-level schema — in evidence entry schema at SCHEMA PREAMBLE |
| C-35 | Prior Confidence into Phase 5 hypothesis resolution — schema: FID / Hypothesis / Prior Confidence / Actual Outcome / Status |
| C-36 | Per-phase FINDING REGISTER closure directives — "Close FINDING REGISTER Phase N rows" after each evidence phase |
| C-37 | Hypothesis resolution schema pre-defined in SCHEMA PREAMBLE — Phase 5 fills via fill-forward directive |
| C-38 | Column-specific FINDING REGISTER closure directives — "[columns: FID (key, fill-now), ...]" bracket enumeration |
| C-39 | Fill-forward directive as Phase 5 header annotation — `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block -- from SCHEMA PREAMBLE]` |
| C-40 | Bracket notation for closure directives — `[columns: ...]` bracket notation in all FINDING REGISTER closure directives |
| C-41 | Named-schema enumeration in Phase 5 fill-forward — Phase 5 header names each schema individually |
| C-42 | Per-column temporal commit annotation — closure directives annotate each column: (key, fill-now), (fill-now), (defer-to-Phase-5) |
| C-43 | Temporal commit encoded at SCHEMA PREAMBLE definition time — Phase 0 schema column headers carry (fill-now) and (defer-to-Phase-5) at definition time |
| C-44 | Per-phase minimum evidence count annotations — all phase headers carry `[min: N ...]` brackets |
| C-45 | PRE-COMMITMENT block before SCHEMA PREAMBLE — hypotheses and default recommendation committed before schema columns visible |
| C-46 | Evidence density closure annotation — "Evidence density: [actual count] of [min] -- gate clears when actual >= min" after each evidence phase |
| C-47 | PRE-COMMITMENT recommendation confidence with falsification condition — Default recommendation confidence field and Falsification condition; recommendation record carries Prior Recommendation Confidence column |
| C-48 | FINDING REGISTER [expect: N FIDs] annotations — present at every phase |
| C-49 | Phase 5 synthesis completeness annotation — [hypothesis-resolution: filled/empty] ... gate clears when all four show filled |
| C-50 | Phase gate check status annotation — three-field go/no-go verdict `[min met? Y/N] \| [FIDs closed? Y/N] \| [Proceed? Y/N]` after density annotation at each evidence phase |
| C-51 | Recommendation delta sentence after recommendation record table — "Confidence moved from {prior} to {final} because {FIDs}" immediately after Phase 5 recommendation record |
| C-52 | Phase 3 Inertia Lock-in column — `Inertia Lock-in (H/M/L)` in Phase 3 segment table alongside Fit Score column, with H/M/L definition |
