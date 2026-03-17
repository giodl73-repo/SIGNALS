## campaign-decide — Quest Score R13 (Rubric v12)

**Skill**: campaign-decide
**Round**: R13
**Rubric**: v12 (denominator /26 aspirational, max 103.0)
**New criterion under test**: C-34 — confidence threshold propagated via pre-Phase-0 schema definition

---

## Criterion-by-Criterion Evaluation

### V-01 — Single axis: Phrasing register (descriptive)

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01 | Essential | PASS | `Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON}` present |
| C-02 | Essential | PASS | `Confidence: {H / M / L} — H = 80%+...` present |
| C-03 | Essential | PASS | All 7 phase sections present |
| C-04 | Essential | PASS | Phase 1a precedes 1b; `[COMPLETE BEFORE Phase 1b]` gate present |
| C-05 | Essential | PASS | `Confidence Rationale (cite FIDs — not label alone)` present |
| C-06 | Recommended | PASS | FINDING REGISTER, titled phases, Phase 5 sub-tables with bold labels |
| C-07 | Recommended | PASS | Counter Block `\| FID \| Counter Claim \| Rebuttal \|` satisfies counter-claim + qualifying FID + disposition |
| C-08 | Recommended | **FAIL** | No Phase 5 hypothesis resolution sub-table; Phase 0 `Status` column is Phase 0-only |
| C-09 | Aspirational | FAIL | Recommendation/Confidence rendered as prose, not a 4-column table; no column header |
| C-10 | Aspirational | FAIL | Only Phase 1a register inline; no full pre-seeded register before Phase 0 |
| C-11 | Aspirational | PASS | BECAUSE block has `Citation (Phase N, F[N]-seq)` in header |
| C-12 | Aspirational | PASS | Phase 3 has `Fit Score (1-10)` column |
| C-13 | Aspirational | FAIL | Phase 0 lifecycle schema has no `Prior Confidence` column |
| C-14 | Aspirational | FAIL | Phase 0 header has no gate annotation |
| C-15 | Aspirational | PASS | Phase 2 has `Severity (R/Y/G)` |
| C-16 | Aspirational | FAIL | No full pre-seeded FINDING REGISTER before Phase 0 |
| C-17 | Aspirational | PASS | BECAUSE block explicitly lists all 6 slots |
| C-18 | Aspirational | FAIL | Recommendation output is labeled prose, not a 4-column table |
| C-19 | Aspirational | FAIL | Counter Block has 3 columns; does not match C-19's 4-column Counter-evidence schema |
| C-20 | Aspirational | FAIL | Phase 0 and Phase 5 missing gate annotations |
| C-21 | Aspirational | FAIL | `[COMPLETE BEFORE Phase 1b]` on line below header, not inline in header text |
| C-22 | Aspirational | PASS | Citation column header encodes `(Phase N, F[N]-seq)` format |
| C-23 | Aspirational | PASS | All column headers domain-specific throughout |
| C-24 | Aspirational | PASS | BECAUSE has distinct `Phase 1a / INERTIA` and `Phase 1b / RIVALS` rows |
| C-25 | Aspirational | PASS | BECAUSE block: `Phase \| Label \| Citation (...) \| Claim` — 4 columns |
| C-26 | Aspirational | FAIL | Phase 1b table has Response Strategy column, but no "with response strategy" register label |
| C-27 | Aspirational | FAIL | Recommendation/Confidence in prose — C-18 fails due to prose-load |
| C-28 | Aspirational | PASS | `Expected Result (Phase 0)` and `Actual Outcome (Phase 5)` encode temporal slots |
| C-29 | Aspirational | PASS | `[INERTIA IS THE PRIMARY COMPETITOR]` in header + `primary competitor: YES` in register |
| C-30 | Aspirational | FAIL | Phase 5 has Alignment/Gap/Counter Block/Synthesis Row — not the C-30 canonical 4 |
| C-31 | Aspirational | PASS | Phase 1a register: `FID \| Finding Summary \| Primary Competitor \| Switching Cost` |
| C-32 | Aspirational | PASS | **Counter Block:** with `FID \| Counter Claim \| Rebuttal` |
| C-33 | Aspirational | PASS | Entry schema column header: `Confidence (H=80%+ / M=50-79% / L<50%)` |
| C-34 | Aspirational | PASS | Entry schema defined before Phase 0, threshold encoded in Confidence column header |

**V-01 score**: 60.0 (Essential) + 20.0 (Recommended: C-06+C-07 pass, C-08 fail) + 7.0 (14 Aspirational × 0.5) = **87.0 / 103.0**

---

### V-02 — Single axis: C-34 anchor via recommendation schema preamble

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01 | Essential | PASS | Recommendation record schema pre-seeded; closure at Phase 5 |
| C-02 | Essential | PASS | Confidence (H/M/L) with calibration in recommendation schema |
| C-03 | Essential | PASS | All phases present |
| C-04 | Essential | PASS | Phase 1a before 1b with gate |
| C-05 | Essential | PASS | `Confidence Rationale (cite FIDs — not label alone)` column in pre-seeded record |
| C-06 | Recommended | PASS | Structured format with named phase sections and Phase 5 sub-tables |
| C-07 | Recommended | PASS | Counter Block present with FID + Counter Claim + Rebuttal |
| C-08 | Recommended | **FAIL** | No Phase 5 hypothesis resolution sub-table |
| C-09 | Aspirational | PASS | Pre-seeded recommendation record has `Confidence Rationale (cite FIDs — not label alone)` as column |
| C-10 | Aspirational | FAIL | FINDING REGISTER only for Phase 1a inline; no full pre-seeded register |
| C-11 | Aspirational | PASS | BECAUSE block `Citation (Phase N, F[N]-seq)` |
| C-12 | Aspirational | FAIL | Phase 3: "List at least one market signal with magnitude or direction" — no Fit Score column schema |
| C-13 | Aspirational | FAIL | Phase 0 schema lacks `Prior Confidence` column |
| C-14 | Aspirational | FAIL | Phase 5 header has no gate annotation |
| C-15 | Aspirational | FAIL | Phase 2 schema: `Severity` — no `(R/Y/G)` traffic-light encoded in header |
| C-16 | Aspirational | FAIL | No full pre-seeded FINDING REGISTER |
| C-17 | Aspirational | PASS | 6-row BECAUSE block enumerated |
| C-18 | Aspirational | PASS | `\| FID \| Recommendation \| Confidence (H=80%+...) \| Confidence Rationale (...) \|` pre-seeded as table |
| C-19 | Aspirational | FAIL | Counter Block is 3-column; no separate 4-column Counter-evidence table |
| C-20 | Aspirational | FAIL | Phase 5 missing gate |
| C-21 | Aspirational | FAIL | Gate on line below header, not inline |
| C-22 | Aspirational | PASS | BECAUSE block Citation column encodes hybrid format |
| C-23 | Aspirational | PASS | Domain-specific headers throughout (Phase 2 `Severity` is domain-specific) |
| C-24 | Aspirational | PASS | BECAUSE has 1a/INERTIA and 1b/RIVALS distinct rows |
| C-25 | Aspirational | PASS | BECAUSE block 4-column schema |
| C-26 | Aspirational | FAIL | Phase 1b has Response Strategy column; no "with response strategy" register label |
| C-27 | Aspirational | FAIL | C-15 traffic-light not in header; C-12 missing; prose load-bearing for Phase 3 |
| C-28 | Aspirational | PASS | `Expected Result (Phase 0)` and `Actual Outcome (Phase 5)` temporal slots |
| C-29 | Aspirational | PASS | Header `[INERTIA IS THE PRIMARY COMPETITOR]` + register `primary competitor: YES` |
| C-30 | Aspirational | FAIL | Phase 5 has Alignment/Gap/Counter Block/Synthesis Row — not C-30 canonical 4 |
| C-31 | Aspirational | PASS | Phase 1a register 4-column with Switching Cost |
| C-32 | Aspirational | PASS | **Counter Block:** with `FID \| Counter Claim \| Rebuttal` |
| C-33 | Aspirational | PASS | Recommendation schema has `Confidence (H=80%+...)` |
| C-34 | Aspirational | PASS | Recommendation record schema defined before Phase 0; threshold in column header |

**V-02 score**: 60.0 + 20.0 + 7.0 (14 Aspirational × 0.5) = **87.0 / 103.0**

*Note: V-02 swaps C-12 (FAIL — no Fit Score) for C-09 (PASS — recommendation record table) relative to V-01. Same total.*

---

### V-03 — Single axis: Lifecycle emphasis (unified schema preamble block)

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01 | Essential | PASS | Recommendation present |
| C-02 | Essential | PASS | Confidence present with calibration |
| C-03 | Essential | PASS | All phases present |
| C-04 | Essential | PASS | Phase 1a → Phase 1b gated |
| C-05 | Essential | PASS | `Confidence Rationale (cite FIDs — not label alone)` in prose close |
| C-06 | Recommended | PASS | SCHEMA PREAMBLE + all phases + Phase 5 sub-tables |
| C-07 | Recommended | PASS | Counter Block with FID/Counter Claim/Rebuttal |
| C-08 | Recommended | **FAIL** | No Phase 5 hypothesis resolution sub-table |
| C-09 | Aspirational | FAIL | Recommendation rendered as labeled prose, not a table |
| C-10 | Aspirational | FAIL | No full pre-seeded FINDING REGISTER |
| C-11 | Aspirational | PASS | BECAUSE schema `Citation (Phase N, F[N]-seq)` in preamble |
| C-12 | Aspirational | PASS | Phase 3 has `Fit Score (1-10)` column |
| C-13 | Aspirational | FAIL | Phase 0 lifecycle schema: no `Prior Confidence` column |
| C-14 | Aspirational | PASS | All phases gated; Phase 5 has `[COMPLETE PHASE 5 LAST]` — gate intent satisfied |
| C-15 | Aspirational | PASS | Phase 2 has `Severity (R/Y/G)` |
| C-16 | Aspirational | FAIL | No pre-seeded FINDING REGISTER block before Phase 0 |
| C-17 | Aspirational | PASS | 6-row BECAUSE block with all slots enumerated |
| C-18 | Aspirational | FAIL | No Phase 5 recommendation record table |
| C-19 | Aspirational | FAIL | Counter Block is 3-column only |
| C-20 | Aspirational | PASS | All phases annotated (Phase 5 annotation present) |
| C-21 | Aspirational | FAIL | `[COMPLETE BEFORE Phase 1b]` on line below Phase 1a header |
| C-22 | Aspirational | PASS | BECAUSE schema encodes hybrid key in Citation column header |
| C-23 | Aspirational | PASS | All column headers domain-specific |
| C-24 | Aspirational | PASS | BECAUSE has distinct 1a/INERTIA and 1b/RIVALS rows |
| C-25 | Aspirational | PASS | BECAUSE block: 4 named columns |
| C-26 | Aspirational | FAIL | Phase 1b table has Response Strategy; register label "with response strategy" not stated |
| C-27 | Aspirational | FAIL | Recommendation in prose; C-18/C-09/C-16 failures indicate prose-load |
| C-28 | Aspirational | PASS | `Expected Result (Phase 0)` and `Actual Outcome (Phase 5)` in preamble lifecycle schema |
| C-29 | Aspirational | PASS | Header `[INERTIA IS THE PRIMARY COMPETITOR]` + register `primary competitor: YES` |
| C-30 | Aspirational | FAIL | Phase 5: Alignment/Gap/Counter Block/Synthesis Row — not C-30 canonical 4 |
| C-31 | Aspirational | PASS | Phase 1a register 4-column with Switching Cost |
| C-32 | Aspirational | PASS | **Counter Block:** `FID \| Counter Claim \| Rebuttal` |
| C-33 | Aspirational | PASS | Entry schema in preamble has `Confidence (H=80%+...)` |
| C-34 | Aspirational | PASS | SCHEMA PREAMBLE entry schema (before Phase 0) encodes threshold in Confidence header |

**V-03 score**: 60.0 + 20.0 + 8.0 (16 Aspirational × 0.5) = **88.0 / 103.0**

*V-03 gains over V-01/V-02: C-14 and C-20 (gate annotations on all phases via preamble structure). Loses C-09/C-18 (no recommendation record table) and C-26 (no register label).*

---

### V-04 — Combined: Inertia framing + C-34 dual anchor

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01 | Essential | PASS | Recommendation record schema present; `Fill the pre-seeded recommendation record schema now` |
| C-02 | Essential | PASS | Confidence (H=80%+...) in both pre-Phase-0 schema definitions |
| C-03 | Essential | PASS | All phases |
| C-04 | Essential | PASS | Phase 1a before 1b with gate |
| C-05 | Essential | PASS | `Confidence Rationale (cite FIDs — not label alone)` as column in pre-seeded record |
| C-06 | Recommended | PASS | Two pre-Phase-0 schema definitions + all phases + Phase 5 sub-tables |
| C-07 | Recommended | PASS | Counter Block with FID/Counter Claim/Rebuttal |
| C-08 | Recommended | **FAIL** | No Phase 5 hypothesis resolution sub-table |
| C-09 | Aspirational | PASS | Recommendation record has `Confidence Rationale (cite FIDs — not label alone)` column |
| C-10 | Aspirational | FAIL | No full pre-seeded FINDING REGISTER before Phase 0 |
| C-11 | Aspirational | PASS | BECAUSE block Citation column encodes hybrid key |
| C-12 | Aspirational | PASS | Phase 3 has `Fit Score (1-10)` |
| C-13 | Aspirational | FAIL | Phase 0 lifecycle schema: no `Prior Confidence` column |
| C-14 | Aspirational | PASS | Phase 0 `[COMPLETE BEFORE PHASE 1]` present; Phase 5 `[COMPLETE PHASE 5 LAST]` |
| C-15 | Aspirational | PASS | Phase 2 `Severity (R/Y/G)` |
| C-16 | Aspirational | FAIL | No pre-seeded FINDING REGISTER block |
| C-17 | Aspirational | PASS | 6-row BECAUSE block |
| C-18 | Aspirational | PASS | 4-column recommendation record pre-seeded with correct headers |
| C-19 | Aspirational | FAIL | Counter Block (3-col); no separate 4-column Counter-evidence table |
| C-20 | Aspirational | PASS | All phases have gate annotations |
| C-21 | Aspirational | PASS | Phase 1a header inline: `**Phase 1a — ...** \`[COMPLETE BEFORE Phase 1b]\` \`[INERTIA...]\`` |
| C-22 | Aspirational | PASS | BECAUSE Citation column header encodes hybrid key format |
| C-23 | Aspirational | PASS | All domain-specific headers; Phase 5 Alignment/Gap blocks carry `Confidence (H=80%+...)` |
| C-24 | Aspirational | PASS | BECAUSE 1a/INERTIA and 1b/RIVALS distinct |
| C-25 | Aspirational | PASS | BECAUSE block 4-column |
| C-26 | Aspirational | PASS | Phase 1b table has Response Strategy; "FINDING REGISTER labels for Phase 1b FIDs note 'with response strategy'" stated explicitly |
| C-27 | Aspirational | FAIL | C-08/C-13/C-16/C-19 fail — missing sub-tables indicate structural gaps; C-19 absence means counter-evidence treatment relies on prose |
| C-28 | Aspirational | PASS | `Expected Result (Phase 0)` and `Actual Outcome (Phase 5)` in lifecycle schema |
| C-29 | Aspirational | PASS | Inline `[INERTIA IS THE PRIMARY COMPETITOR]` + register `primary competitor: YES` + Switching Cost = H |
| C-30 | Aspirational | FAIL | Phase 5: Alignment/Gap/Counter Block/Synthesis Row — not the C-30 canonical 4 sub-tables |
| C-31 | Aspirational | PASS | Phase 1a register 4-column with Switching Cost |
| C-32 | Aspirational | PASS | **Counter Block:** bold label + `FID \| Counter Claim \| Rebuttal` |
| C-33 | Aspirational | PASS | Both pre-Phase-0 schemas carry `Confidence (H=80%+...)` |
| C-34 | Aspirational | PASS | Evidence entry schema AND recommendation record schema both carry threshold before Phase 0 — dual anchor |

**V-04 score**: 60.0 + 20.0 + 10.0 (20 Aspirational × 0.5) = **90.0 / 103.0**

*V-04 gains over V-03: C-09 (+0.5), C-18 (+0.5), C-21 (+0.5), C-26 (+0.5) = +2.0 pts. C-34 dual anchor is the architectural highlight but doesn't score above V-03 on C-34 alone — the gains come from the recommendation record table and inline gate annotation.*

---

### V-05 — Full Integration (targeting 103.0/103.0)

| ID | Tier | Result | Evidence note |
|----|------|--------|---------------|
| C-01 | Essential | PASS | Recommendation record schema pre-seeded; `Fill the pre-seeded recommendation record (from Recommendation record sub-table above)` |
| C-02 | Essential | PASS | Confidence (H=80%+...) in Schema Preamble recommendation schema |
| C-03 | Essential | PASS | All phases 0–5 present |
| C-04 | Essential | PASS | Phase 1a `[COMPLETE BEFORE Phase 1b]` inline; Phase 1a precedes 1b |
| C-05 | Essential | PASS | `Confidence Rationale (cite FIDs — not label alone)` as column in recommendation record |
| C-06 | Recommended | PASS | SCHEMA PREAMBLE + pre-seeded FINDING REGISTER + all phases + Phase 5 with 4 bold-labeled sub-tables |
| C-07 | Recommended | PASS | **Counter-evidence:** sub-table: `\| Counter-Evidence \| Qualifying FID \| Recommended Next Step \| Condition \|` |
| C-08 | Recommended | PASS | **Hypothesis resolution:** sub-table in Phase 5: `\| FID \| Hypothesis \| Prior Confidence \| Actual Outcome \| Status (...) \|` |
| C-09 | Aspirational | PASS | `Confidence Rationale (cite FIDs — not label alone)` as column header in recommendation record table |
| C-10 | Aspirational | PASS | Full FINDING REGISTER with all phase placeholders committed under `[PRE-SEED BEFORE PHASE 0]` before Phase 0 section |
| C-11 | Aspirational | PASS | Because block schema: `Phase \| Label \| Citation (Phase N, F[N]-seq) \| Claim` |
| C-12 | Aspirational | PASS | Phase 3: `Fit Score (1-10)` column |
| C-13 | Aspirational | PASS | Phase 0 lifecycle schema in preamble: `\| Hypothesis \| Prior Confidence \| Method \| Expected Result (fill now) \| Actual Outcome (fill at Phase 5) \| Status \|` |
| C-14 | Aspirational | PASS | All phases have gate annotations; Phase 5 `[COMPLETE PHASE 5 LAST]` satisfies gate intent |
| C-15 | Aspirational | PASS | Phase 2: `Severity (R/Y/G)` |
| C-16 | Aspirational | PASS | Full FINDING REGISTER (all phases pre-seeded) committed before Phase 0 section under explicit gate |
| C-17 | Aspirational | PASS | Because block schema lists all 6 slots: Phase 0/PRIOR, Phase 1a/INERTIA, Phase 1b/RIVALS, Phase 2/FEASIBILITY, Phase 3/MARKET, Phase 4/WEB EVIDENCE |
| C-18 | Aspirational | PASS | `\| FID \| Recommendation \| Confidence (H=80%+...) \| Confidence Rationale (...) \|` in Schema Preamble + Phase 5 closure |
| C-19 | Aspirational | PASS | **Counter-evidence:** sub-table: `\| Counter-Evidence \| Qualifying FID \| Recommended Next Step \| Condition \|` — 4 named columns |
| C-20 | Aspirational | PASS | All phases annotated; Schema Preamble has `[COMPLETE BEFORE PHASE 0]`; Phase 5 `[COMPLETE PHASE 5 LAST]` |
| C-21 | Aspirational | PASS | Phase 1a header inline: `**Phase 1a — scout-competitors** \`[COMPLETE BEFORE Phase 1b]\` \`[INERTIA IS THE PRIMARY COMPETITOR]\`` |
| C-22 | Aspirational | PASS | Because block schema encodes `Citation (Phase N, F[N]-seq)` in column header |
| C-23 | Aspirational | PASS | All column headers domain-specific; no generic placeholders anywhere |
| C-24 | Aspirational | PASS | Because schema defines Phase 1a/INERTIA and Phase 1b/RIVALS as distinct row labels |
| C-25 | Aspirational | PASS | Because block schema: `Phase \| Label \| Citation (Phase N, F[N]-seq) \| Claim` — exactly 4 columns |
| C-26 | Aspirational | PASS | Phase 1b has `Response Strategy` column; `Close FINDING REGISTER Phase 1b rows (labels include "with response strategy")` |
| C-27 | Aspirational | PASS | All C-01..C-26 verifiable from column headers, table structure, gate annotations, register labels — no prose load-bearing |
| C-28 | Aspirational | PASS | Phase 0 lifecycle schema in preamble has `Expected Result (fill now)` and `Actual Outcome (fill at Phase 5)` — temporal slots named in preamble |
| C-29 | Aspirational | PASS | `[INERTIA IS THE PRIMARY COMPETITOR]` in Phase 1a header + F1a-01 `primary competitor: YES` / Switching Cost = H in register |
| C-30 | Aspirational | PASS | Phase 5: **Hypothesis resolution:** + **Recommendation record:** + **Counter-evidence:** + **Counter Block:** — all bold-labeled; per C-32 interaction note, Counter Block satisfies the fourth C-30 slot |
| C-31 | Aspirational | PASS | Phase 1a register (extended): `FID \| Finding Summary \| Primary Competitor \| Switching Cost` |
| C-32 | Aspirational | PASS | **Counter Block:** bold label + `\| FID \| Counter Claim \| Rebuttal \|` — structurally distinct from Counter-evidence table |
| C-33 | Aspirational | PASS | Entry schema and recommendation schema both carry `Confidence (H=80%+...)` in preamble |
| C-34 | Aspirational | PASS | SCHEMA PREAMBLE (before Phase 0) defines both entry schema and recommendation record schema with `Confidence (H=80%+ / M=50-79% / L<50%)` in Confidence column headers — one definition / unlimited propagation |

**V-05 score**: 60.0 (Essential) + 30.0 (Recommended: all 3 pass) + 13.0 (26 Aspirational × 0.5) = **103.0 / 103.0**

---

## Score Summary

| Var | Essential | Recommended | Aspirational | Total | All Essential Pass |
|-----|-----------|-------------|--------------|-------|--------------------|
| V-01 | 60.0 | 20.0 | 7.0 (14/26) | **87.0** | YES |
| V-02 | 60.0 | 20.0 | 7.0 (14/26) | **87.0** | YES |
| V-03 | 60.0 | 20.0 | 8.0 (16/26) | **88.0** | YES |
| V-04 | 60.0 | 20.0 | 10.0 (20/26) | **90.0** | YES |
| V-05 | 60.0 | 30.0 | 13.0 (26/26) | **103.0** | YES |

**Ranking**: V-05 > V-04 > V-03 > V-01 = V-02

---

## Excellence Signals from V-05

**What drove V-05 above V-04 (+13.0 pts):**

1. **Phase 5 Hypothesis resolution sub-table** (+10.0, C-08 Recommended): `| FID | Hypothesis | Prior Confidence | Actual Outcome | Status (CONFIRMED / REFUTED / PARTIAL) |` — closes the experiment lifecycle with a dedicated Phase 5 sub-table, satisfying the single largest gap across all previous variations.

2. **`Prior Confidence` column in Phase 0 preamble schema** (+0.5, C-13): The Schema Preamble defines `| Hypothesis | Prior Confidence | Method | Expected Result (fill now) | Actual Outcome (fill at Phase 5) | Status |` — prior belief committed before evidence runs, enabling confidence-delta traceability.

3. **Full pre-seeded FINDING REGISTER with all phase placeholders** (+0.5, C-16): All phase registers committed as a block under `[PRE-SEED BEFORE PHASE 0]` — FID consistency enforced structurally.

4. **Separate Counter-evidence sub-table alongside Counter Block** (+0.5, C-19): Two distinct Phase 5 risk-handling mechanisms: `Counter-evidence` (C-07/C-19 format: 4-column risk list) AND `Counter Block` (C-32 format: 3-column best-case rebuttal). Dual schema, dual purpose.

5. **Prose-free structural sufficiency** (+0.5, C-27): All 26 preceding criteria verifiable from column headers and table structure alone — the Schema Preamble's "one definition / unlimited propagation" architecture eliminates all prose-load.

6. **C-30 canonical four Phase 5 sub-tables** (+0.5, C-30): Hypothesis resolution + Recommendation record + Counter-evidence + Counter Block as distinct bold-labeled sub-tables satisfies the full C-30 requirement via the C-32 interaction.

**New structural patterns not yet captured as criteria:**

- **Prior Confidence propagated into Phase 5 hypothesis resolution**: The `Prior Confidence` column appears in the Phase 0 preamble schema AND again in the Phase 5 hypothesis resolution sub-table — enabling an explicit before/after confidence comparison per hypothesis (not just pass/fail on the hypothesis outcome). This is belief-calibration traceability at the hypothesis level, distinct from C-13 (which only requires the column in Phase 0) and C-08 (which only requires Phase 5 disposition).

- **Incremental FINDING REGISTER closure directives**: After each phase, V-05 adds `Close FINDING REGISTER Phase N rows` — a per-phase commit pattern that enforces the pre-seeded register is updated as evidence runs, not just pre-seeded and left open. Creates a two-stage commit architecture: placeholders at top, values filled progressively. This is not currently captured by C-10 (which only tests pre-seeding) or C-16 (which only tests pre-commitment).

---

```json
{"top_score": 103.0, "all_essential_pass": true, "new_patterns": ["Prior Confidence propagated from Phase 0 preamble schema into Phase 5 hypothesis resolution sub-table, enabling explicit before/after confidence comparison per hypothesis beyond status alone — belief-calibration traceability at hypothesis granularity", "Per-phase FINDING REGISTER closure directives after each phase enforce incremental register commit, creating a two-stage commit architecture: placeholders pre-seeded at document top, values filled progressively as each phase completes"]}
```
