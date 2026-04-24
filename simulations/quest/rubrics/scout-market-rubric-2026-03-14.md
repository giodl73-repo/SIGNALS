`simulations/quest/rubrics/scout-market-rubric-2026-03-14.md` written.

**Structure:**

- **5 essential** (C-01..C-05): segment ID, TAM/SAM/SOM table, 3-dimension fit scoring, rank formula applied correctly, beachhead + rationale. All five must pass — if any of these fail the output isn't useful.
- **3 recommended** (C-06..C-08): unit consistency (the SF-04 finding), sequencing path, at least one amendment.
- **2 aspirational** (C-09..C-10): non-obvious insight surfaced (the high-WTP-killed-by-GTM-difficulty flip), revenue model per segment.

**Key design decisions:**
- Unit consistency (SF-04) is *recommended* not essential — an output can still be useful even if it mixes units, as long as the fit scoring and beachhead logic are correct.
- C-03 is the essential that catches SF-05 — if the 3-dimension scoring scale isn't applied, the whole composite rank collapses.
- C-05 requires the rationale to explicitly address the highest-WTP segment, which is what makes the beachhead recommendation non-trivial.
 weights); no missing dimension |
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

---

## Scoring Guide

```
essential_pass = count of C-01..C-05 that pass   (max 5)
recommended_pass = count of C-06..C-08 that pass  (max 3)
aspirational_pass = count of C-09..C-10 that pass (max 2)

composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/2 * 10)

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
