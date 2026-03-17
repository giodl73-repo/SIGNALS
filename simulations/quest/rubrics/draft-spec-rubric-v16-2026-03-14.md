**v16 written** to `simulations/quest/rubrics/draft-spec-rubric-v16-2026-03-15.md`.

---

**What changed v15 → v16:**

| | v15 | v16 |
|-|----|-----|
| Aspirational count | 38 | 39 |
| Total criteria | 46 | 47 |
| Formula denominator | 38 | 39 |
| Fractional sub-phase N/A group | C-38, C-39, C-40 | C-38, C-39, C-40, C-47 |

**One new criterion — C-47:**

**Chained ENTER/EXIT notation for fractional sub-phase absorption (structure).** C-44 requires the five numbered phases to form an unbroken named chain. C-38 requires Phase 2's gate dependency to name both pre-Phase-2 tokens. The gap: a template could satisfy both while leaving the fractional sub-phase's EXIT token absent from the Phase 2 ENTER block's named precondition list — present in the gate header but not in the chain notation. C-47 closes it: the ENTER block of a numbered phase following a fractional sub-phase must name EXIT tokens from ALL immediate predecessors (numbered + fractional). Requires C-44 and C-39.

**Why the other R16 JSON `new_patterns` entries didn't yield new criteria:** patterns 1–3 in the JSON (`cross-block structural rule dependency`, `dual-form structural fail rule`, `scope-qualified presence checks`) map exactly to C-40, C-45, and C-46 already formalized in v15. The scorecard is confirming those criteria hold, not discovering new ones. Excellence signal #4 (fractional sub-phase chain absorption) was the only pattern without an existing criterion.
