---

# listen-feedback Variate — Round 20

**Rubric:** v17 | **Target criteria:** A-16, A-17, A-21, A-24, A-28

---

## Round 20 Variation Map

| Variation | Axis | A-16 | A-17 | A-21 | A-24 | A-28 | A-29/30/31 |
|-----------|------|------|------|------|------|------|------------|
| V-01 | Output Format (card sub-fields) | PASS | FAIL | FAIL | FAIL | FAIL | A-29 only |
| V-02 | Output Format (conjunctive bilateral fields) | FAIL | PASS | PASS | FAIL | FAIL | A-29 only |
| V-03 | Lifecycle Emphasis (directional sensitivity phase) | FAIL | FAIL | FAIL | FAIL | PASS | A-29 only |
| V-04 | Combination: Full inertia chain | PASS | PASS | PASS | PASS | FAIL | A-29 only |
| V-05 | Combination: Full stack (R19 V-05 base + inertia chain + directional sensitivity) | PASS | PASS | PASS | PASS | PASS | A-29+30+31 |

---

## V-01 — Output Format (Structured Inertia Sub-Fields)

**Axis:** Output format — persona card field structure
**Hypothesis:** Replacing the prose `Current approach:` field with a 4-sub-field structured baseline (What it delivers / Where it falls short / Floor-level switching cost / Persona-specific workflow disruption) grounds the NPS justification in a structured delta computation. A-16 passes (4 labeled sub-fields). A-09 passes (field is labeled `**Current approach:**`). A-17/A-21/A-24 do not pass — the NPS justification is still a single prose sentence and the gains/losses split is not structurally enforced.

---

*[See file: `simulations/quest/golden/listen-feedback-variate-R20-2026-03-15.md`]*

---

## V-02 — Output Format (Conjunctive Bilateral Gains/Losses)

**Axis:** Output format — bifurcated NPS field with conjunctive bilateral enforcement
**Hypothesis:** Splitting the NPS justification into `Gains from this spec` (Field 2) and `Losses and switching costs` (Field 3), each instruction naming the other field by label and explicitly prohibiting completion without the other, passes A-17 (bilateral coverage) and A-21 (conjunctive framing) simultaneously. A-16 does not pass — Field 1 is still prose, so A-24 cannot be satisfied either (no named sub-fields to cross-reference).

---

## V-03 — Lifecycle Emphasis (Directional Sensitivity Phase)

**Axis:** Lifecycle emphasis — explicit sensitivity phase with directional separation
**Hypothesis:** Adding a dedicated sensitivity phase that reports `Upward delta (+1)` and `Downward delta (−1)` as distinct lines per high-influence persona — with explicit band-crossing detection per direction — satisfies A-28. The differentiator from A-20 (symmetric ±1): when a persona score sits at a band boundary (6/7 or 8/9), a +1 move may cross a threshold while −1 stays in band, producing asymmetric narrative implications that a ±1 figure conceals. Card structure and CI enforcement held constant (A-29 only).

---

## V-04 — Combination: Full Inertia Chain

**Axis:** Combination (A-16 + A-17 + A-21 + A-24)
**Hypothesis:** The full inertia chain — structured 4-sub-field `Current approach:` → `Gains` instruction names `Losses` and cross-references `"Where it falls short"` sub-field → `Losses` instruction names `Gains` and cross-references `"Floor-level switching cost"` sub-field — makes bilateral coverage structurally enforced. A-24 adds the third enforcement layer: the evaluator cannot complete Fields 2 or 3 without invoking a named Field 1 sub-field, making omission of either side structurally detectable rather than just instructionally required. A-28 not targeted; A-30/A-31 not targeted.

---

## V-05 — Combination: Full Stack

**Axis:** Combination (R19 V-05 base + V-04 inertia chain + V-03 directional sensitivity)
**Hypothesis:** Every major structural constraint in the protocol gains the same property: (1) process-level enforcement, (2) bilateral grounding where applicable, and (3) co-located failure mode annotation. The derivation-phase CI (A-30) + co-located failure mode (A-31) handle the aggregate computation. The inertia chain (A-16/17/21/24) handles per-persona delta grounding. The directional sensitivity phase (A-28) makes asymmetric band-crossing effects visible as distinct narrative signals. Together these eliminate three classes of silent compliance failure: adding the CI parenthetical retroactively, completing gains without losses, and reporting ±delta without directional separation.

---

**Written to:** `simulations/quest/golden/listen-feedback-variate-R20-2026-03-15.md`

**Round 20 differentiators to watch in scoring:**

- **A-16 vs A-09:** Does the scorer distinguish structured sub-fields (A-16) from merely having a `Current approach:` label (A-09)? V-01 and V-04/V-05 should split here.
- **A-17 vs A-21:** Bilateral prohibition ("completing X without Y is a failure") vs. conjunctive naming ("Field 2 names Field 3"). Both are present in V-02/V-04/V-05; absence in V-01/V-03 should yield clean FAIL.
- **A-24 gating on A-16:** V-02 has A-17+A-21 but no named sub-fields to cross-reference — A-24 should FAIL there even though the bilateral structure exists, confirming A-16 is a prerequisite for A-24.
- **A-28 asymmetry:** The differentiator between V-03/V-05 and all others is whether upward and downward band-crossing effects are reported as distinct findings. A symmetric ±1 figure anywhere should yield FAIL on A-28.
