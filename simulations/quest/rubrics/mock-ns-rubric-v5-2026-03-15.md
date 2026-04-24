**v5 written** to `simulations/quest/rubrics/quest-rubric-mock-ns-v5-2026-03-15.md`.

---

**What changed in v5:**

Three new aspirational criteria from Round 4 excellence signals:

- **C-18 — Named path class enumeration** at the compute site. C-16 requires "anywhere in this run"; C-18 requires the prohibition to explicitly name execution path classes — at minimum conditional branches, fallback paths, and regeneration sequences. V-02's `"not in any step, any conditional branch, any fallback path, or any regeneration sequence"` is the threshold reference; V-01 exceeds it with a catch-all and bypass-order clarifier. The gap closed: a general scope statement can still be read as covering only the normal step sequence; named classes eliminate that interpretive ambiguity.

- **C-19 — Anti-displacement closure** at the consumption site. C-17 requires the prohibition to be first; C-19 requires it to also name the specific instruction types that cannot precede it (field-listing, category lookup, formatting) and conclude with a declarative closure asserting no other instruction in the step precedes the rule. V-01's `"This rule is first — it applies before any field is listed, before any category lookup, before any formatting instruction in this step. No instruction in A-1 precedes this rule."` is the reference. The gap closed: a first-positioned prohibition that names no competitors can still be displaced when adjacent instructions are processed before the rule is anchored.

- **C-20 — Failure-consequence framing** at the consumption site. C-17 requires first position; C-19 requires anti-displacement closure; C-20 requires an explicit inertia-consequence statement naming the failure mechanism and why it's dangerous. V-05's `"Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible to downstream tooling and silently corrupts the artifact's trust tier."` is the reference. The gap closed: unexplained prohibitions can be deprioritized under execution pressure; naming the cost makes violation visible at the moment the instruction is processed.

**Scoring update:** Aspirational denominator changes from 9 to 12 (`pass/12 * 10`). Variants carrying only C-16 + C-17 (e.g., V-04) score ≈ 97.5 (11/12 aspirational). V-01 carries C-18 + C-19 but not C-20 (no consequence statement) → 98.3 (11.5/12 if C-19 treated as partial for catch-all absence, or 11/12 if C-20 strictly scored). V-05 is the only variant targeting all three new criteria simultaneously → 100.
