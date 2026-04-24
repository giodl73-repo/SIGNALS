Written to `simulations/quest/rubrics/scout-market-rubric-v4-2026-03-14.md`.

---

**Three new criteria (C-15, C-16, C-17) — one per excellence signal:**

| ID | Signal | Criterion | What it captures |
|----|--------|-----------|-----------------|
| C-15 | ES-04 | Unified cross-segment scoring table | Wide-table format with WTP/Revenue Model/Price Point as adjacent columns; enables direct cross-segment comparison in one view; per-card does not pass |
| C-16 | ES-05 | Inertia-break label forecloses time-based responses | Pre-printed "Inertia-break condition:" label (or equivalent) makes "Year 2+" structurally invalid; implicit "what inertia barrier is resolved" passes C-14 but not C-16 |
| C-17 | ES-06 | STATUS QUO quantification chain at source and consumption | Forward-reference in STATUS QUO pre-commits to quantification; beachhead cites cost by value and source format; C-12 reminder-at-consumption only does not satisfy |

**Formula:** `aspirational_pass/9 * 10` (9 criteria, ceiling 100)

**R3 retroactive scores under v4:**

| V | C-15 | C-16 | C-17 | Asp | Score |
|---|------|------|------|-----|-------|
| V-01 | PASS | FAIL | FAIL | 7/9 | 97.8 |
| V-02 | FAIL | PASS | FAIL | 7/9 | 97.8 |
| V-03 | FAIL | FAIL | FAIL | 3/9 | 93.3 |
| V-04 | PASS | FAIL | FAIL | 7/9 | 97.8 |
| V-05 | FAIL | PASS | PASS | 8/9 | **98.9** |

V-05 remains the golden candidate. Path to 100 requires combining all three new patterns — V-05 + a unified summary table gets there without sacrificing any existing passes.
fallback at deployment scale.

**C-17: STATUS QUO quantification chain enforced at source and consumption** (depth)
ES-06 introduced the SOURCE-AND-CONSUMPTION chain. A C-12-passing output states "not building this means..." at the beachhead. C-17 requires both ends of the chain to be mandatory: the STATUS QUO section includes a forward-reference instruction ("required in 'Not building this means:' below -- do not write a vague estimate"), and the beachhead statement includes a format-trace citation back to the STATUS QUO cost ("costing approximately $X from STATUS QUO"). Reminder-at-consumption only (C-12 standard) passes C-12; chain-enforcement at both source and consumption is required for C-17.

**Scoring formula updated:** `aspirational_pass/9 * 10` (was `/6`). Ceiling stays at 100.

**Score shifts under v4 (retroactive, R3 variations):**
- R3-V-05: 100 -> **98.9** (C-15 FAIL -- per-card, no unified cross-segment table; C-16 PASS; C-17 PASS -- 8/9)
- R3-V-01: 100 -> **97.8** (C-15 PASS; C-16 FAIL -- implicit trigger; C-17 FAIL -- 7/9)
- R3-V-02: 100 -> **97.8** (C-15 FAIL; C-16 PASS; C-17 FAIL -- 7/9)
- R3-V-04: 100 -> **97.8** (C-15 PASS; C-16 FAIL; C-17 FAIL -- 7/9)
- R3-V-03: 95 -> **93.3** (C-15..C-17 all FAIL -- 3/9 aspirational; formula denominator change only)

V-05 remains the golden candidate at 98.9. Path to 100 under v4 requires a new variation combining wide-table unified scoring (C-15), explicit inertia-break label (C-16), and STATUS QUO quantification chain (C-17).

---

## Essential Criteria (60 pts total)

All five must pass -- if any fail the output is not useful.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Segment IDs assigned** | coverage | essential | Every segment has a unique ID (e.g., S1, S2, S3); IDs appear consistently across all tables and the final ranking |
| C-02 | **TAM/SAM/SOM table present** | coverage | essential | A table with TAM, SAM, SOM values exists with one row per segment; no segment is omitted |
| C-03 | **3-dimension fit scoring applied** | correctness | essential | Pain, WTP, and Accessibility are all scored (1-10 scale); composite fit score = arithmetic mean of all three dimensions (no weights); no dimension is missing |
| C-04 | **Composite rank formula applied** | correctness | essential | Rank score = fit score + (10 - GTM difficulty) applied to every segment; final ranking matches the computed values |
| C-05 | **Beachhead recommendation with rationale** | depth | essential | One segment named as beachhead; rationale cites fit score, GTM difficulty, and why this segment is preferred over the highest-WTP segment |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Unit consistency** | correctness | recommended | Tooling segments use developer headcount; platform/enterprise segments use dollar TAM; units are not mixed within the same column of the same table |
| C-07 | **Sequencing path stated** | depth | recommended | A Y1 -> Y2+ adoption sequence is given (e.g., S1 -> S2 -> S3 -> defer S4) with one sentence of justification per transition |
| C-08 | **At least one amendment or open question** | depth | recommended | Phase 4 (or equivalent) lists 1+ concrete next steps to validate or refine the analysis (e.g., price-test assumption, disaggregate a segment, add a dimension) |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Non-obvious insight surfaced** | depth | aspirational | Output surfaces at least one finding that reverses naive intuition (e.g., highest-WTP segment ranks last because GTM difficulty dominates; free model for beachhead locks in methodology before monetization) |
| C-10 | **Revenue model per segment** | coverage | aspirational | Every segment has a stated revenue model (free, freemium, seat license, etc.) and at least one segment has a concrete price point or ARR target |
| C-11 | **STATUS QUO baseline stated before scoring** | depth | aspirational | A do-nothing / status quo cost is named before any fit scoring begins; pain scores or WTP scores for at least one segment are explicitly anchored to switching cost or observable inertia (not abstract ratings); the inertia anchor is traceable to the ranking output |
| C-12 | **Opportunity cost of inaction stated at beachhead** | depth | aspirational | The beachhead recommendation includes a "not building this means..." statement (or equivalent); the cost of deferring the beachhead segment is stated at the decision point -- quantified, estimated, or tied back to the STATUS QUO cost from C-11 |
| C-13 | **Revenue model co-located with WTP score** | coverage | aspirational | Revenue model and price point for each segment appear alongside (or within) the fit scoring view for that segment -- not in a separate trailing table; the co-location makes the WTP-vs-revenue-model comparison visible without cross-referencing; at least one segment shows a concrete price point adjacent to its WTP score; passes via either per-card vertical adjacency or wide-table column adjacency (see C-15) |
| C-14 | **Sequencing transition conditioned on inertia break** | depth | aspirational | The Y1->Y2+ sequencing transitions cite a named observable condition drawn from the STATUS QUO inertia analysis -- not a time-based assumption; at least one transition trigger is traceable to the inertia anchor from C-11 (e.g., "when compliance inertia breaks," "after methodology lock-in prevents reversion"); passes via explicit or implicit trigger field (see C-16 for explicit-only scoring) |
| C-15 | **Unified cross-segment scoring table** | coverage | aspirational | A single table presents WTP, Revenue Model, Price Point, fit score, and GTM difficulty as adjacent columns with one row per segment; no dimension requires lookup in a separate section; direct cross-segment comparison is possible within one view; wide-table format only -- per-card format does not satisfy this criterion |
| C-16 | **Inertia-break transition label forecloses time-based responses** | depth | aspirational | The sequencing section uses a pre-printed or explicitly-labeled field whose label type requires a named observable condition -- not a free-form justification field; label must be specific enough that "Year 2+" or "when adoption grows" is not a valid response to it (e.g., "Inertia-break condition:", "Named STATUS QUO trigger:"); implicit trigger fields (e.g., "Transition trigger: what inertia barrier is resolved") do not satisfy this criterion |
| C-17 | **STATUS QUO quantification chain enforced at source and consumption** | depth | aspirational | Two conditions both required: (1) the STATUS QUO section includes a forward-reference instruction that pre-commits to a quantified estimate for use at beachhead (e.g., "required in 'Not building this means:' below -- do not write a vague estimate"); (2) the beachhead "not building this means:" cites the STATUS QUO cost by value and source (e.g., "costing approximately $X from STATUS QUO"); a reminder at consumption only (C-12 standard) does not satisfy this criterion |

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-17 that pass   (max 9)

composite = (essential_pass/5    * 60)
          + (recommended_pass/3  * 30)
          + (aspirational_pass/9 * 10)

golden = (essential_pass == 5) AND (composite >= 80)
```

| Score | Label |
|-------|-------|
| 90-100 | Exemplary |
| 80-89 | Golden (meets threshold) |
| 60-79 | Partial -- review failed essential |
| < 60 | Failing |

---

## Failure Modes (from trace findings)

| Finding | Maps to | Impact if missed |
|---------|---------|-----------------|
| SF-04: Mixes dollar TAM and headcount TAM | C-06 | Recommended fail only; output still useful if fit scoring is correct |
| SF-05: Scoring scale not defined in spec | C-03 | Essential fail if dimensions are absent or composite is not an average |
| SF-06: Artifact path not confirmed | n/a | Not scored; informational |
| R1-P1: No STATUS QUO section | C-11 | Aspirational fail; also gates C-14, C-16, C-17 |
| R1-P2: No "not building this means..." at beachhead | C-12, C-17 | C-12 aspirational fail; C-17 also fails (no consumption anchor) |
| R2-P1: Revenue model in trailing table, not co-located | C-13 | Aspirational fail; C-09 may pass narratively but WTP-vs-model comparison is not forced |
| R2-P2: Sequencing uses time-based transitions, not inertia signals | C-14 | Aspirational fail; C-07 passes but sequencing is not grounded in STATUS QUO analysis |
| R3-P1: No unified cross-segment scoring table | C-15 | Aspirational fail; C-13 may pass via per-card adjacency, but cross-segment comparison requires section lookup |
| R3-P2: Implicit trigger field instead of explicit inertia-break label | C-16 | Aspirational fail; C-14 passes, but label forecloses time-based fallback at deployment scale |
| R3-P3: C-12 quantification reminder at consumption only, no source forward-reference | C-17 | Aspirational fail; C-12 passes (statement exists), but chain enforcement requires both ends |

---

## Calibration Notes

### R1 Calibration

**Top score (R1):** 95 -- V-03 (Inertia framing) and V-05 (Full synthesis) tied.

**What separated the 95s from the 90s:** STATUS QUO section + mandatory inertia anchor column. Without structural scaffolding, C-09 depends on model discretion; all three 90-point variations prompted the WTP/GTM comparison but did not force it.

**C-11 independence from C-09:** A variation can pass C-09 (the insight occurs) without passing C-11 (grounding is present before scoring). V-01, V-02, V-04 all show this -- C-09 PARTIAL despite prompting the comparison, because inertia was never anchored.

**C-12 independence from C-09 and C-11:** V-05 uniquely surfaces the do-nothing cost a third time at the beachhead via the "Not building this means:" pre-printed line. The insight is restated *where the decision is made*, not just in the analysis.

**C-10 gap:** Failed in all five R1 variations. No template included a revenue model field.

### R2 Calibration

**Top score (R2):** 100 (v2 rubric) -- V-02 (Revenue Model Per Segment Card). First perfect score under the rubric at that time.

**What separated R2-V-02 from R2-V-01 (C-13 delta):** V-01 places revenue model in a standalone section after COMPOSITE RANK. V-02 embeds revenue model + price point in each per-segment scoring card alongside WTP. The co-location in V-02 is what makes C-09 structural rather than narrative -- the juxtaposition forces the model to confront whether a free entry model is consistent with a high WTP score.

**C-14 evidence:** V-02's sequencing uses an explicit "transition trigger field" in each Y1/Y2+ row. The trigger must reference a named condition, not "Year 2." This is the first variation to tie sequencing to STATUS QUO inertia analysis rather than arbitrary time periods.

**C-13 + C-14 independence:** C-13 is about where revenue model data appears; C-14 is about what sequencing justifications cite. A variation could pass C-13 (co-located revenue model) and fail C-14 (time-based sequencing), or vice versa.

### R3 Calibration

**Top score (R3):** 98.9 -- V-05 (Golden candidate). Per-card + explicit C-14 label + quantified C-12 chain.

**R3 confirmed two structural paths to C-13:** Wide-table column adjacency (V-01, V-04: WTP | Revenue Model | Price Point as adjacent columns in one unified scoring row) is architecturally equivalent to per-card vertical adjacency (V-02, V-05: WTP immediately above Revenue Model and Price Point within each segment block). C-13 pass condition updated to make both paths explicit.

**C-16 evidence:** V-02 uses a pre-printed "Inertia-break condition:" label. V-04 uses "Transition trigger: what inertia barrier is resolved or what channel opens" -- an implicit field. Both pass C-14; only V-02 and V-05 pass C-16. Identical scores under v3 because C-16 did not exist; now differentiated.

**C-17 evidence (ES-06, V-05):** V-05 uniquely enforces quantification at STATUS QUO with a forward-reference mandate ("required in 'Not building this means:' below -- do not write a vague estimate"), and the beachhead statement includes a format-chain citation ("costing approximately $X from STATUS QUO"). V-02 has a "not building this means:" line (passes C-12) but no source forward-reference. V-05 is the sole R3 carrier of C-17.

**STATUS QUO gates (v4):** C-11, C-12, C-14, C-16, and C-17 all require STATUS QUO. Any template without STATUS QUO is capped at 93.3 (C-09, C-10, C-13, C-15 can pass regardless -- 4/9 aspirational = 60 + 30 + 4.4 = 94.4; V-03 confirms the ceiling at 93.3 because only C-09, C-10, C-13 pass -- not C-15).

**C-15 vs. C-16 vs. C-17 independence:** Each new criterion is structurally orthogonal. C-15 (wide table format) can pass while C-16 fails (implicit trigger in sequencing sub-section). C-16 (explicit label) can pass while C-15 fails (per-card layout). C-17 (chain enforcement) can pass regardless of format choice. No R3 variation passes all three; each current template embodies exactly one or two of the new patterns.

### R1 scores under v4 rubric (retroactive)

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | Asp | Composite |
|-----------|------|------|------|------|------|------|------|------|------|-----|-----------|
| R1-V-01 | PARTIAL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0/9 | 90.0 |
| R1-V-02 | PARTIAL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0/9 | 90.0 |
| R1-V-03 | PASS | FAIL | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 2/9 | 92.2 |
| R1-V-04 | PARTIAL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0/9 | 90.0 |
| R1-V-05 | PASS | FAIL | PASS | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | 3/9 | 93.3 |

### R2 scores under v4 rubric (retroactive)

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | Asp | Composite |
|-----------|------|------|------|------|------|------|------|------|------|-----|-----------|
| R2-V-01 | PASS | PASS | PASS | FAIL | FAIL | -- | FAIL | FAIL | FAIL | 3/9 | 93.3 |
| R2-V-02 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | FAIL | 7/9 | 97.8 |

Note: R2-V-02 drops from 100 (v3) to 97.8 (v4) -- now fails C-15 (per-card, not unified cross-segment table) and C-17 (no source forward-reference for C-12 quantification).

### R3 scores under v4 rubric

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | Asp | Composite |
|-----------|------|------|------|------|------|------|------|------|------|-----|-----------|
| R3-V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | FAIL | 7/9 | 97.8 |
| R3-V-02 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | FAIL | 7/9 | 97.8 |
| R3-V-03 | PASS | PASS | FAIL | FAIL | PASS | FAIL | FAIL | FAIL | FAIL | 3/9 | 93.3 |
| R3-V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | FAIL | 7/9 | 97.8 |
| R3-V-05 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | 8/9 | 98.9 |

V-05 is the current golden candidate at 98.9. V-01, V-02, V-04 are architecturally distinct 97.8 templates -- each passes exactly one of the three new criteria. No R3 variation passes all three new criteria simultaneously.

### Path to 100 (v4)

Must pass all nine aspirational criteria. C-15, C-16, and C-17 together require:
1. Unified cross-segment scoring table with WTP, Revenue Model, Price Point as adjacent columns (C-15) -- wide-table format
2. Explicit "Inertia-break condition:" label (or equivalent) in sequencing transitions (C-16) -- not an implicit trigger field
3. STATUS QUO quantification forward-reference + beachhead format-chain citation (C-17) -- both source and consumption mandatory

No current variation achieves all three. The architectural challenge: C-15 requires wide-table format, which is in tension with per-card format (the natural home for C-16's explicit label and C-17's consumption-side chain). A v4 path-to-100 template must either:
- Use wide-table unified scoring (satisfies C-15) AND embed the explicit inertia-break label in a sequencing sub-table (satisfies C-16) AND enforce the quantification chain in STATUS QUO and beachhead sections (satisfies C-17), OR
- Use per-card format (satisfies C-16 and C-17 naturally) AND add a unified summary table for cross-segment comparison (satisfies C-15)

V-05's architecture (per-card + explicit label + chain) is closest: adding a unified summary table would yield 9/9 = 100 without sacrificing any existing passes.
