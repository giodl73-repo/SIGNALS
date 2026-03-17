Written to `simulations/quest/golden/campaign-decide-variate-R1-2026-03-16.md`.

---

## campaign-decide — Variate R1 / 5 Variations

**Axes selected**: Inertia framing (single), Output format (single), Phrasing register (single), Lifecycle emphasis + inertia (combined), Inertia + evidence traceability (combined).

---

### V-01 — Inertia Framing
**Hypothesis**: Naming inertia as "Competitor Zero" with the explicit phrase "before naming any product or company" makes C-04 a structural constraint instead of a convention. A model that reads this rule literally cannot lead with named rivals.

**Core addition over baseline**: The COMPETITOR ZERO RULE block + two named sub-sections inside scout-competitors (Inertia Analysis / Named Rivals with an explicit ordering constraint).

---

### V-02 — Output Format (Table-Driven Brief)
**Hypothesis**: Pre-defining table schemas per phase turns domain coverage into fill-in work. C-03 passes by construction (six tables = six domains). The inertia row appearing *before* named rival rows hard-wires C-04 without requiring the model to remember a rule.

**Core addition**: Six explicit table schemas, each with required columns. Phase 6 template includes `Confidence rationale`, `Because (cite by Phase)`, and `Next step` rows — which targets C-09 and C-10 structurally.

---

### V-03 — Phrasing Register (Conversational)
**Hypothesis**: Question-driven framing encourages reasoning-aloud output that naturally produces "because" chains, potentially satisfying C-05 more organically. Useful as a contrast case — the *lowest-structure* variation.

**Core addition**: Six questions instead of six instructions. The recommendation question explicitly says "show your work: link the recommendation to the evidence above."

**Expected weakness**: No explicit section headers — C-06 likely fails unless the model adds its own.

---

### V-04 — Lifecycle Emphasis + Inertia Framing (Combined)
**Hypothesis**: Phase gates ("Gate check: ... --> proceed") prevent shallow passes. Each gate names exactly what must exist before advancing. The INERTIA GATE label on Phase 1 gives the constraint a visible identity.

**Core addition**: Six named phases with gate checks. Phase 6 separates `Confidence rationale` and conditioned next steps as required fields.

---

### V-05 — Inertia Framing + Evidence Traceability (Combined)
**Hypothesis**: Directly naming and prohibiting the two failure modes this skill was designed to prevent — no inertia-first ordering, floating recommendations — is more effective than implicit instruction. "Floating recommendations are not acceptable" names the exact failure pattern from C-05's rubric note.

**Core addition**: Named INERTIA-FIRST RULE + CITATION RULE blocks at the top. The Phase 6 template mandates at least three `because Phase [N]` citations with an explicit minimum count.

---

### Predicted Leaderboard

| Rank | Variation | Reasoning |
|------|-----------|-----------|
| 1 | V-05 | Directly targets C-04 and C-05 by name; C-08/C-09/C-10 in template |
| 2 | V-04 | Gate mechanics enforce coverage; combines C-04 framing with phase discipline |
| 3 | V-02 | Structure guarantees most criteria pass; risk is shallow table filling |
| 4 | V-01 | Targets C-04/C-05 well but no explicit structure for C-06 |
| 5 | V-03 | Most natural output; most likely to miss C-06 and C-03 |

Ready for `/quest-score` against the v1 rubric.
