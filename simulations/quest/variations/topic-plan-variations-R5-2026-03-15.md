Written to `simulations/quest/golden/topic-plan-variate-R5-new-2026-03-15.md`.

---

## Round 5 — topic-plan Variations (rubric v5 revised, C-01–C-23)

Three new criteria targeted: **C-21** (vocabulary contract violation enumeration), **C-22** (row-number anchor citation), **C-23** (verbatim-quoted banned forms).

---

### V-01 — Output format: Named-violation vocabulary contract (C-21)

**Axis**: A `VOCABULARY CONTRACT` block is prepended to the schemas section. Beyond defining `??` and `--`, it enumerates three named violations: blank cells (VIOLATION-1), `??` in confirmed-zero cells (VIOLATION-2), `--` in required cells (VIOLATION-3).

**Hypothesis**: C-17 defines the two tokens but leaves misuse conditions implicit. C-21 closes this by making violation modes as explicitly defined as the tokens themselves. Without named violations, a model can write `??` where a confirmed 0 belongs (VIOLATION-2) and satisfy the token-presence check while breaking the intent. The contract is self-enforcing only when violations are enumerated, not just implied.

---

### V-02 — Lifecycle emphasis: Defense register with row-number anchors (C-22)

**Axis**: A **Phase 0** is inserted before Phase 1. It builds `Schema DR` — a defense register with explicit `D-R-1, D-R-2, ...` row IDs. Every proposal row in Schemas E and F must include a `Defense defeated: Row D-R-N` column citing the exact row number.

**Hypothesis**: C-18/C-08 require that proposals name the defense they defeated, but "named defense" without a row number forces reviewers to match names across tables by prose — fragile under abbreviation or paraphrase. C-22 makes linkage independently verifiable by cross-reference: a Row D-R-3 citation resolves without re-reading the defense text. Missing row numbers are detectable without content review.

---

### V-03 — Phrasing register: Verbatim-quoted banned forms everywhere (C-23)

**Axis**: Every hedge-phrase disqualification rule in the prompt is stated as a verbatim-quoted list — exact strings as they would appear in model output (`"no change needed"`, `"change is clearly warranted"`, `"a few"`, etc.) — across vs. NO CHANGE, null declarations, and delta count sentences.

**Hypothesis**: C-16 bans "hedge phrases" but described paraphrases leave wiggle room — a model may produce "no significant change required" and not recognize it as matching "no change needed." Verbatim-quoted banned forms are pattern-matchable: the model can scan its own output for exact string matches. This removes the interpretive layer between instruction and compliance.

---

### V-04 — Combination: C-21 + C-22

Merges the `VOCABULARY CONTRACT` named-violation block (V-01) with the `Schema DR` defense register and row-number `Defense defeated` column (V-02). Orthogonal failure modes addressed simultaneously: sentinel misuse and unverifiable inertia linkage.

---

### V-05 — Full combination: C-21 + C-22 + C-23

All three mechanisms in a single prompt: `VOCABULARY CONTRACT` with three named violations, Phase 0 defense register with `D-R-N` anchors, and verbatim-quoted banned-forms list applied to vs. NO CHANGE, null declarations, and delta count sentences. Tests whether the three mechanisms compound each other or interfere under context load.
