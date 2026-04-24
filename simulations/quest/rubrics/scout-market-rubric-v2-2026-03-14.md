Written to `simulations/quest/rubrics/scout-market-rubric-v2-2026-03-14.md` (123 lines).

---

**What changed from v1:**

Two new aspirational criteria, drawn directly from the V-03/V-05 excellence signals:

**C-11: STATUS QUO baseline stated before scoring** (depth / aspirational)
> A do-nothing cost is named before any fit scoring begins; pain/WTP scores for at least one segment are anchored to switching cost or observable inertia; the anchor is traceable to the ranking output.

**C-12: Opportunity cost of inaction stated at beachhead** (depth / aspirational)
> The beachhead recommendation includes a "not building this means..." statement; the cost of deferring is stated at the decision point — not just in the analysis.

**Why these are independent from C-09:**
- C-09 requires the rank-reversal insight to *occur* (can pass by model discretion)
- C-11 requires the *grounding* to be present before scoring (structural, not narrative)
- C-12 requires the insight to *resurface at the decision point* (V-05's unique move)

**Scoring formula updated:** `aspirational_pass/4 * 10` (was `/2`). Ceiling stays at 100.

**Retroactive consequence:** V-05 now scores **97.5**, not 95 — C-12 was always there, now it's scoreable. V-03 and V-05 are no longer tied. The path to 100 is V-05 + revenue model field (C-10).
1 or C-12 -- but those passes are fragile.

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

---

## Scoring Guide

```
essential_pass    = count of C-01..C-05 that pass   (max 5)
recommended_pass  = count of C-06..C-08 that pass   (max 3)
aspirational_pass = count of C-09..C-12 that pass   (max 4)

composite = (essential_pass/5    * 60)
          + (recommended_pass/3  * 30)
          + (aspirational_pass/4 * 10)

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

---

## R1 Calibration Notes

**Top score (R1):** 95 -- V-03 (Inertia framing) and V-05 (Full synthesis) tied.

**What separated the 95s from the 90s:** STATUS QUO section + mandatory inertia anchor column. Without structural scaffolding, C-09 depends on model discretion; all three 90-point variations prompted the WTP/GTM comparison but did not force it.

**C-11 independence from C-09:** A variation can pass C-09 (the insight occurs) without passing C-11 (grounding is present before scoring). V-01, V-02, V-04 all show this -- C-09 PARTIAL despite prompting the comparison, because inertia was never anchored. C-11 makes the gap explicit and scoreable.

**C-12 independence from C-09 and C-11:** V-05 uniquely surfaces the do-nothing cost a third time at the beachhead via the "Not building this means:" pre-printed line. This is a distinct structural move -- the insight is restated *where the decision is made*, not just in the analysis.

**C-10 gap:** Failed in all five R1 variations. No template included a revenue model field. Closing C-10 requires an explicit per-segment field; the ground truth trace produced revenue models naturally (PM surfaced them in Phase 2), but no skill prompt elicited them.

**Path to 100 (R2):** V-05 + revenue model field per segment card + inertia anchor column = candidate for perfect score if C-09, C-10, C-11, and C-12 all pass.

**R1 scores under v2 rubric (retroactive):**

| Variation | C-09 | C-10 | C-11 | C-12 | Aspirational | Composite |
|-----------|------|------|------|------|--------------|-----------|
| V-01 | PARTIAL | FAIL | FAIL | FAIL | 0/4 | 90 |
| V-02 | PARTIAL | FAIL | FAIL | FAIL | 0/4 | 90 |
| V-03 | PASS | FAIL | PASS | FAIL | 2/4 | 95 |
| V-04 | PARTIAL | FAIL | FAIL | FAIL | 0/4 | 90 |
| V-05 | PASS | FAIL | PASS | PASS | 3/4 | 97.5 |

Note: Under v2, V-05 scores 97.5 (not 95) because C-12 now passes -- the "Not building this means:" field is a scoreable criterion, not merely a structural note. V-03 and V-05 are no longer tied.
