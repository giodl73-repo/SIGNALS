# campaign-decide-variate-R20-QU5-simplified-2026-03-17.md

**Quest**: campaign-decide
**Round**: R20 QU5 — Simplification Pass
**Date**: 2026-03-17
**Source**: campaign-decide-variate-R20-2026-03-17.md V-05
**Rubric**: campaign-decide-rubric-v20-2026-03-17.md

---

## Simplified Prompt Body

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**PRE-COMMITMENT** `[WRITE NOW — before loading SCHEMA PREAMBLE, commit priors in plain form]`

Write your three falsifiable hypotheses, a default recommendation with confidence level, and the condition that would flip the recommendation. These values transfer directly into Phase 0 experiment rows and Phase 5 synthesis. Do not revise after reading the schema.

H1 — {first falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
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

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]` `[min: 3 experiments]`
Transfer the hypotheses committed in the PRE-COMMITMENT block into Phase 0 experiment rows. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Fill all `(fill-now)` columns now (hypothesis values come from PRE-COMMITMENT block — do not revise); `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].
Evidence density: [actual experiment count] of 3 — gate clears when actual >= 3.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 1a.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
What do your users do today without `{topic}`? That behavior — the workaround, the spreadsheet, the absence of the feature — is your real first competitor. It has 100% market share and zero switching cost; it does not lose unless the evidence forces it to. Name it, quantify its switching cost, and record it as the primary competitor. Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].
Evidence density: [actual inertia entries] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 1b.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
Name the products your users would switch to. For each rival, the question is not "do they exist" but "how do you win against them specifically?" No entry without a response strategy — if you cannot state how you win, the rival is a blocking risk, not a manageable competitor.

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].
Evidence density: [actual rival count] of 2 — gate clears when actual >= 2.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 2.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
List the barriers where you genuinely do not know today whether they are solvable. Do not list known-solvable problems. Severity: R = blocking / unknown path, Y = known path / uncertain timeline, G = solved or trivially solvable.

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual barrier count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 3.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score and inertia lock-in]`
Score fit numerically and rate inertia lock-in per segment. Inertia Lock-in (H/M/L): H = embedded routine / high re-learning cost / low pain with status quo; M = moderate switching friction; L = unmet pain / low prior investment / motivated to switch. Do not round up for enthusiasm.

| Segment | Signal | Direction | Fit Score (1-10) | Inertia Lock-in (H/M/L) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual segment count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 4.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
At least one item must cite a source and a date. No undated or unsourced entries count toward the minimum.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual web-sourced entry count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 5.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
Fill the Phase 0 deferred columns — confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)]. Then build four structurally distinct sub-tables — one per decision artifact. No merging, no skipping. Each carries a distinct bold label and its own schema.

**Hypothesis resolution:**
Fill the Phase 5 hypothesis resolution schema from the Schema Preamble. Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
State the recommendation with confidence and a rationale that cites the findings that drove it. Compare to the PRE-COMMITMENT default recommendation and confidence — fill the recommendation record schema from the Schema Preamble (which carries the Prior Recommendation Confidence column sourced from PRE-COMMITMENT):
| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

Recommendation calibration delta: Confidence moved from {prior H/M/L} (PRE-COMMITMENT) to {final H/M/L}. Moved {up / down / unchanged} because {cite FIDs — not label alone}.

**Counter-evidence:**
If nothing in the evidence argues against your recommendation, the brief is incomplete. When citing high-lock-in segments from Phase 3, note the Inertia Lock-in rating as a qualifying condition:
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
State the single strongest case for the opposing recommendation and rebut it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation. Cross-reference the PRE-COMMITMENT falsification condition — was the falsification condition encountered in the evidence?

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled.

---

## Simplification Report

**Word count**: 1,943 simplified / 2,440 original — **20.4% reduction**

### What was removed and why

| Removed | Location | Reason |
|---------|----------|--------|
| Decision Stakes block (~96 words) | After role sentence | Pure motivation for Phase 1a. C-29 inertia primacy is structurally encoded in Phase 1a header `[INERTIA IS THE PRIMARY COMPETITOR]`, FINDING REGISTER `F1a-01 (inertia): primary competitor: YES`, and Phase 1a body. |
| Schema architecture intro paragraph (~35 words) | SCHEMA PREAMBLE | Meta-commentary ("Five schemas are defined in this preamble..."). Redundant with the preamble block header `[all schemas committed here, one definition / unlimited propagation]` and the schemas themselves. |
| Schema architecture table (~54 words) | SCHEMA PREAMBLE | Navigation aid listing schema names and phase usage. Not a rubric criterion signal — schemas are defined directly below with their own context labels. |
| PRE-COMMITMENT intro opening clause (~22 words) | PRE-COMMITMENT | "Before reading any schema below," and "the point of this block is that you cannot see the columns yet" are explanatory. The block header `[WRITE NOW — before loading SCHEMA PREAMBLE]` already encodes the timing; "do not revise after reading the schema" retains the lock instruction. |
| Phase 0 experiment schema temporal commit prose (~20 words) | SCHEMA PREAMBLE | "The temporal commit for every column is declared above — no column's fill phase is ambiguous at any downstream gate." The temporal commit is visible in the column header notation (fill-now / defer-to-Phase-5); the "single definition" sentence below it is retained for C-27. |
| FINDING REGISTER middle sentence (~7 words) | FINDING REGISTER | "Finding Summary filled per-phase as evidence completes." Explains what every phase closure directive already states explicitly. |
| Phase 1a FINDING REGISTER explanatory note (~30 words) | FINDING REGISTER | "The Switching Cost column (H / M / L) surfaces the behavioral cost of abandoning the status quo — the structural reason inertia is listed first among all competitors." The column is already in the register schema header; C-31 requires the column, not the explanation. |
| Phase 0 intro motivational clauses (~20 words) | Phase 0 | "Before you look at any competitor, market, or technical data," and "these are the falsifiable claims this campaign will confirm or refute" — removed. The structural instruction (transfer hypotheses from PRE-COMMITMENT, use schema from preamble, fill-now/defer) is retained. |
| Phase 1a "Before you name a single rival product, answer this:" (~9 words) | Phase 1a | Rhetorical opener replaced by the direct question "What do your users do today without `{topic}`?" |
| Phase 1a "See Decision Stakes block above for why this phase is not optional." (~13 words) | Phase 1a | Dangling cross-reference after Decision Stakes block removal. |
| Phase 1b "Now name ... instead of yours" → "Name the products your users would switch to" (~5 words) | Phase 1b | Tightened; "instead of yours" is implicit. |
| Phase 2 "What could stop this from working technically?" (~7 words) | Phase 2 | Rhetorical intro question removed; the barrier table schema is self-explanatory. |
| Phase 2 "Name at least one barrier:" (~5 words) | Phase 2 | Redundant with header `[min: 1 named barrier]`. |
| Phase 3 "Who would buy this, and how well does it fit what they already want?" (~14 words) | Phase 3 | Rhetorical intro; the fit score column header and the inertia lock-in definition carry the structural signal. |
| Phase 3 "— a high-fit, high-lock-in segment is a harder win than the fit score alone suggests." (~18 words) | Phase 3 | Editorial observation; C-52 is satisfied by the Inertia Lock-in column presence and definition, not this note. |
| Phase 3 "List at least one segment:" (~5 words) | Phase 3 | Redundant with header `[min: 1 segment with fit score and inertia lock-in]`. |
| Phase 4 "What does external evidence say — independent of your internal assumptions?" (~11 words) | Phase 4 | Rhetorical intro removed; the minimum requirement sentence immediately follows. |
| Phase 5 "You have the evidence. Now close it." (~7 words) | Phase 5 | Motivational transition removed. |
| Phase 5 "The calibration delta between Prior Confidence ... is now computable." (~20 words) | Phase 5 | Explanatory observation. C-35 is satisfied by the Phase 5 hypothesis resolution schema carrying the Prior Confidence column and the fill-forward directive. |
| Phase 5 "Did the evidence confirm or refute what you committed in the PRE-COMMITMENT block?" (~14 words) | Phase 5 — Hypothesis resolution | Rhetorical question; the fill instruction and schema reference immediately follow. |
| Phase 5 "column temporal commits declared in SCHEMA PREAMBLE," (~6 words) | Phase 5 | Removed from "confirmed here" clause; the bracket notation `[columns: Actual Outcome (fill-now), Status (fill-now)]` already confirms the temporal schema without the cross-reference. |
| Phase 5 Counter Block "This is not a risk list — it is the best argument you lost, and the reason you can still defend your recommendation against it" (~27 words) | Phase 5 — Counter Block | Editorial description of the Counter Block purpose. C-32 requires the Counter Block schema (FID / Counter Claim / Rebuttal); the structural instruction "State the single strongest case for the opposing recommendation and rebut it" is retained. |
| Phase 5 Counter-evidence "What did you find that argues against your recommendation?" (~9 words) | Phase 5 — Counter-evidence | Rhetorical intro; the structural instruction follows immediately. |

### Criteria verification

All 52 criteria (C-01 through C-52) pass in the simplified version:

- **C-01/C-02**: Role sentence + inertia framing retained verbatim — persona and decision question both present.
- **C-29**: Inertia primacy dual-signal retained — Phase 1a header `[INERTIA IS THE PRIMARY COMPETITOR]` and "It has 100% market share and zero switching cost" body signal both present.
- **C-45**: PRE-COMMITMENT block before SCHEMA PREAMBLE — retained. Locking instruction ("do not revise after reading the schema" + "These are locked.") retained.
- **C-28**: Phase 0 experiment lifecycle schema with temporal commits in column headers — retained verbatim. "Fill-now columns are committed at Phase 0 close; deferred columns are committed at Phase 5 close via fill-forward directive" retained.
- **C-27**: "This is the single definition; all downstream closure directives confirm rather than declare" retained. "Table rows only — no prose" retained.
- **C-34**: Confidence calibration scale encoded in evidence entry schema header — retained verbatim.
- **C-35**: Prior Confidence propagation from PRE-COMMITMENT → Phase 0 → Phase 5 — all three anchors retained.
- **C-47**: Recommendation record schema with Prior Recommendation Confidence column — retained verbatim.
- **C-36**: Per-phase FINDING REGISTER closure directives — retained at every phase.
- **C-48**: FINDING REGISTER `[expect: N FIDs]` annotations — retained at every phase.
- **C-31**: Phase 1a FINDING REGISTER extended schema with Switching Cost column — retained. F1a-01 inertia seed retained.
- **C-26**: Response strategy column in Phase 1b table + "with response strategy" FID label — both retained.
- **C-25**: Because block — 6 rows, schema from preamble, slot names fixed — retained verbatim.
- **C-32**: Counter Block schema `| FID | Counter Claim | Rebuttal |` — retained.
- **C-30**: Four distinct bold sub-table labels in Phase 5 — retained ("Hypothesis resolution:", "Recommendation record:", "Counter-evidence:", "Counter Block:").
- **C-46**: Per-phase evidence density annotations — retained at every phase.
- **C-50**: Gate check annotations after each evidence phase — retained at every phase (C-50).
- **C-51**: Recommendation calibration delta sentence — retained verbatim (C-51).
- **C-52**: Phase 3 Inertia Lock-in column with H/M/L definition — retained verbatim (C-52).
- **C-49**: Phase 5 synthesis completeness annotation — retained verbatim.
- **C-33**: Confidence calibration quantified thresholds (H=80%+/M=50-79%/L<50%) — present in evidence entry schema, recommendation record schema.

**All essential criteria pass: YES**

```json
{"simplified_word_count": 1943, "original_word_count": 2440, "all_essential_still_pass": true}
```
