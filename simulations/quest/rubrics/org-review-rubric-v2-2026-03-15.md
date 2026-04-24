Rubric updated to v2. Here's what changed:

**New aspirational criteria (from Round 1 signals):**

- **C-11 — Disposition Code Output** (V-02, V-04): The summary must emit READY / CONDITIONAL / BLOCKED as an explicit code. V-04's READY/CONDITIONAL/BLOCKED pattern appeared in two high-scoring variations and transforms the review from opinion into a commit gate. Distinct from C-08 (which only requires a summary exists).

- **C-12 — Null Hypothesis Anchoring per Role** (V-03): Each reviewer's findings must include an explicit act/don't-act stance from their own frame, not just domain observations. V-03 showed this as the strongest C-03 discriminator — PM anchors on decision sufficiency, architect on technical justification, inertia-advocate on workaround viability. Distinct from C-03 (different framing) — C-12 checks that every frame is anchored to the build question.

**C-04 tightened:** Added the semantic anchoring insight from V-04 — strongest implementations define HIGH = blocks commitment, MEDIUM = conditions commitment, LOW = advisory. Not a pass/fail change, but strengthens the guidance.

**Scoring rebalanced:** Aspirational shifts from 2×10 pts to 4×5 pts each — total stays at 100. Golden threshold (80) unchanged.
