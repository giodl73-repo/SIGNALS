Written to `simulations/quest/rubrics/scout-market-rubric-v3-2026-03-14.md`.

---

**Two new aspirational criteria added:**

**C-13: Revenue model co-located with WTP score** (coverage)
The key R2 insight: V-01 and V-02 both pass C-10 (revenue model exists), but only V-02 passes C-13 (revenue model *adjacent to WTP*). Co-location is what makes C-09 structural — the model is forced to confront whether a free entry model is consistent with a high WTP score, rather than noting it in a trailing section.

**C-14: Sequencing transition conditioned on inertia break** (depth)
V-02's sequencing has a "transition trigger field" that must cite a named condition from the STATUS QUO analysis, not a time period. C-07 passes with "Year 2+"; C-14 requires "when compliance inertia breaks." Independent of C-14, C-07 still passes.

**Scoring formula:** `aspirational_pass/6 * 10` — ceiling stays 100.

**Score shifts under v3:**
- R2-V-02: still 100 (passes C-13 + C-14)
- R2-V-01: 97.5 → **95** (C-13 fails — standalone trailing table)
- R1-V-05: 97.5 → **95** (C-13 + C-14 both absent)
- R1-V-03: 95 → **93.3** (same reason)
the comparison is unavoidable
- C-07 requires a sequencing path with justification; C-14 requires the justification to be an *inertia-break condition*, not an arbitrary time period
- C-13 is what makes C-09 structural in V-02: juxtaposing WTP and revenue model in the same view forces the model to surface whether a free entry model is inconsistent with a high WTP score

**Scoring formula updated:** `aspirational_pass/6 * 10` (was `/4`). Ceiling stays at 100.

**Retroactive consequence:**
- R2-V-02 passes C-13 and C-14 -> still 100
- R2-V-01 fails C-12 and C-13 (standalone revenue table, no co-location) -> 95 (was 97.5)
- R1-V-05 passes C-11, C-12 but lacks C-13/C-14 -> 95 (was 97.5)

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
| C-13 | **Revenue model co-located with WTP score** | coverage | aspirational | Revenue model and price point for each segment appear alongside (or within) the fit scoring view for that segment -- not in a separate trailing table; the co-location makes the WTP-vs-revenue-model comparison visible without cross-referencing; at least one segment shows a concrete price point adjacent to its WTP score |
| C-14 | **Sequencing transition conditioned on inertia break** | depth | aspirational | The Y1->Y2+ sequencing transitions cite a named observable condition drawn from the STATUS QUO inertia analysis -- not a time-based assumption; at least one transition trigger is traceable to the inertia anchor from C-11 (e.g., "when compliance inertia breaks," "after methodology lock-in prevents reversion") |

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-14 that pass   (max 6)

composite = (essential_pass/5    * 60)
          + (recommended_pass/3  * 30)
          + (aspirational_pass/6 * 10)

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
| R1-P1: No STATUS QUO section | C-11 | Aspirational fail; C-09 may still pass by model discretion but is fragile |
| R1-P2: No "not building this means..." at beachhead | C-12 | Aspirational fail; insight is surfaced in analysis but does not resurface at the decision point |
| R2-P1: Revenue model in trailing table, not co-located | C-13 | Aspirational fail; C-09 may pass narratively but WTP-vs-model comparison is not forced |
| R2-P2: Sequencing uses time-based transitions, not inertia signals | C-14 | Aspirational fail; C-07 passes but sequencing is not grounded in STATUS QUO analysis |

---

## Calibration Notes

### R1 Calibration

**Top score (R1):** 95 -- V-03 (Inertia framing) and V-05 (Full synthesis) tied.

**What separated the 95s from the 90s:** STATUS QUO section + mandatory inertia anchor column. Without structural scaffolding, C-09 depends on model discretion; all three 90-point variations prompted the WTP/GTM comparison but did not force it.

**C-11 independence from C-09:** A variation can pass C-09 (the insight occurs) without passing C-11 (grounding is present before scoring). V-01, V-02, V-04 all show this -- C-09 PARTIAL despite prompting the comparison, because inertia was never anchored.

**C-12 independence from C-09 and C-11:** V-05 uniquely surfaces the do-nothing cost a third time at the beachhead via the "Not building this means:" pre-printed line. The insight is restated *where the decision is made*, not just in the analysis.

**C-10 gap:** Failed in all five R1 variations. No template included a revenue model field.

### R2 Calibration

**Top score (R2):** 100 -- V-02 (Revenue Model Per Segment Card). First perfect score.

**What separated R2-V-02 from R2-V-01 (C-13 delta):** V-01 places revenue model in a standalone section after COMPOSITE RANK. V-02 embeds revenue model + price point in each per-segment scoring card alongside WTP. The co-location in V-02 is what makes C-09 structural rather than narrative -- the juxtaposition forces the model to confront whether a free entry model is consistent with a high WTP score. V-01 still passes C-09 (the insight emerges from a trailing note), but C-13 fails because the comparison is not forced by the structure.

**C-14 evidence:** V-02's sequencing uses an explicit "transition trigger field" in each Y1/Y2+ row. The trigger must reference a named condition, not "Year 2." This is the first variation to tie sequencing to STATUS QUO inertia analysis rather than arbitrary time periods.

**C-13 + C-14 independence:** C-13 is about where revenue model data appears; C-14 is about what sequencing justifications cite. A variation could pass C-13 (co-located revenue model) and fail C-14 (time-based sequencing), or vice versa.

### R1 scores under v3 rubric (retroactive)

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Asp | Composite |
|-----------|------|------|------|------|------|------|-----|-----------|
| R1-V-01 | PARTIAL | FAIL | FAIL | FAIL | FAIL | FAIL | 0/6 | 90 |
| R1-V-02 | PARTIAL | FAIL | FAIL | FAIL | FAIL | FAIL | 0/6 | 90 |
| R1-V-03 | PASS | FAIL | PASS | FAIL | FAIL | FAIL | 2/6 | 93.3 |
| R1-V-04 | PARTIAL | FAIL | FAIL | FAIL | FAIL | FAIL | 0/6 | 90 |
| R1-V-05 | PASS | FAIL | PASS | PASS | FAIL | FAIL | 3/6 | 95 |

### R2 scores under v3 rubric

| Variation | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Asp | Composite |
|-----------|------|------|------|------|------|------|-----|-----------|
| R2-V-01 | PASS | PASS | PASS | FAIL | FAIL | -- | 3/6 | 95 |
| R2-V-02 | PASS | PASS | PASS | PASS | PASS | PASS | 6/6 | 100 |

Note: R2-V-01 drops from 97.5 (v2) to 95 (v3) -- C-13 now fails because the revenue model is in a trailing standalone table, not co-located with WTP. R2-V-03 through R2-V-05 not yet scored under v3.

### Path to 100 (R3 and beyond)

Must pass all six aspirational criteria. C-13 and C-14 together require:
1. Per-segment card structure (or equivalent co-location mechanism)
2. STATUS QUO section with named inertia anchor (C-11 prerequisite for C-14)
3. Sequencing transitions that reference the inertia anchor by name

V-02 (R2) is the first template to achieve this. The key architectural insight: per-segment cards create no-omission paths for C-10 and C-13, force juxtaposition for C-09 and C-13, and provide a natural home for the C-14 transition trigger field alongside the sequencing output.
