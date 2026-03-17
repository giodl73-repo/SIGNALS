Here is the complete v10 rubric with the two new criteria extracted from R9:

---

## What changed (v9 → v10)

**Two new criteria, 3 pts each. Max score: 160 → 166.**

### C-31 — Container Mechanism-Type Declaration
*Source: "ASSERTIONS" in the R9 container header across all five variations*

The header `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` has three structural dimensions:
1. **Position** — "PRE-EVALUATION" (C-21)
2. **Mechanism type** — "ASSERTIONS" **(C-31, new)**
3. **Trigger + cross-reference** — "(before any Round 2 construct evaluation begins)" (C-25 + C-27)

C-21 captured dimension 1. C-25/C-27 captured dimension 3. "ASSERTIONS" was always there but never formalized. It is independent of position and trigger — a header can say "PRE-EVALUATION NOTES" and satisfy C-21 and C-25 while failing C-31. The term constrains the container's authority: assertions are structural commitments, not suggestions.

**Pass condition:** The named portion of the container header (outside the boundary-event parenthetical) contains a mechanism-type term identifying content as assertive/declarative ("ASSERTIONS," "DECLARATIONS," "PRECONDITIONS," "PREREQUISITES"). Positional-only ("BLOCK"), advisory ("NOTES," "GUIDANCE"), or descriptive ("CONTEXT," "OVERVIEW") terms do not pass. Requires C-21.

### C-32 — Barrier Heading Evaluation-Type Subtitle
*Source: `## ROUND 2 — Structural Precision Pass` in all five R9 variations*

The barrier heading is not just `## ROUND 2` — it carries `— Structural Precision Pass`. This subtitle names the *analysis class* performed in that round, making the heading a sequence marker **and** an analysis-class declaration. No prior criterion touches the barrier heading's content: C-26 tests adjacency (relationship between heading and container), C-27 tests that the phrase matches the heading's ordinal — neither requires the heading to have a subtitle.

C-32 is strictly about the barrier heading, fully independent of all container-layer criteria (C-21–C-31).

**Pass condition:** Barrier heading contains both (a) a round/barrier ordinal AND (b) a dash-separated evaluation-type subtitle naming the analysis class. `## ROUND 2 — Structural Precision Pass` passes; `## ROUND 2 — Pass` and bare `## ROUND 2` do not. No preconditions.

---

**R9 retroactive scores under v10: all five 166/166.** C-31 and C-32 both confirm structural inertness across the five R9 content axes, matching the R6 inertness pattern for C-25/C-26 and the R9 inertness pattern for C-29/C-30.

Written to `simulations/quest/rubrics/flow-throttle-rubric-v10-2026-03-15.md`.
