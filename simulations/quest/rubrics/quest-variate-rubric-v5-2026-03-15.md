Written to `simulations/quest/rubrics/quest-rubric-variate-R5-2026-03-15.md`.

---

## What changed v4 -> v5

3 new aspirational criteria (C-25 through C-27), each traceable to a specific R4 excellence signal:

| ID | Criterion | Source signal | Distinction from prior criteria |
|----|-----------|---------------|---------------------------------|
| C-25 | **Dual failure condition sub-fields as separately labeled keys** | E-01: `failure-condition-outcome:` and `failure-condition-implementation:` as distinct keys | C-20 requires two mechanistically-distinct conditions by *content*. C-25 requires they appear as *two named keys* — making omission structurally detectable by field presence without prose parsing. |
| C-26 | **Per-body axis-freeze protocol inside the generation loop** | E-02: read committed axis → name and freeze every other axis → write | C-17 is a document-level lock at generation start. C-26 is per-body, inside the loop — surfacing contamination risk before each body rather than locking once at the top. |
| C-27 | **Pre-generation variation map as a standalone top-level artifact** | E-03: variation map placed as separate section with its own header + freeze instruction | C-24 requires the *content* (per-variation per-criterion predictions). C-27 requires the *structure*: a separate top-level section header and an explicit immutability declaration at the section level. |

**Scoring formula**: aspirational denominator bumped from `/16` to `/19`. All bands and weights unchanged.
