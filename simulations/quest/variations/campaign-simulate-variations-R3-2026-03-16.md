Written to `simulations/quest/golden/campaign-simulate-variate-R3-2026-03-16.md`.

---

## Round 3 Variations Summary

**Context**: R2 achieved the essentials + C-11/C-12/C-13. R3 targets the three new aspirational criteria from v3: **C-14** (vacuous-filter acknowledgment), **C-15** (active negative comparison), **C-16** (structural coverage symmetry).

---

### V-01 -- Filter Log Resolution (Output Format axis)
**Axis**: Adds a mandatory **Filter Log Resolution** block after the filter table. Two templates:
- Template A (normal): at least one rejection logged
- Template B (vacuous): zero rejections logged → explicit RECALIBRATION REQUIRED notice

**Targets**: C-14 by construction. Zero rejections cannot be silently accepted.
**Hardest remaining**: C-11 (universal empty-state), C-15 (active negative comparison)

---

### V-02 -- Active Negative Comparison Phase (Lifecycle Emphasis axis)
**Axis**: Cross-skill analysis restructured as a **3-step comparison protocol**:
- Step 1: list all candidate pairings (F-IDs from different checks that share surface similarity)
- Step 2: compare each pair → verdict + reason (compounding / independent)
- Step 3: declare patterns — only after Steps 1+2 are complete

"No patterns" cannot be written without a completed comparison table.

**Targets**: C-15 by construction. Passive omission is structurally blocked.
**Hardest remaining**: C-14 (vacuous-filter trap), C-11 (empty-state all sections)

---

### V-03 -- Inertia Framing (New axis, not previously explored)
**Axis**: Each check opens with `> Without this check: teams typically miss [X]`. The findings report asks "what would a team that only read the spec have shipped wrong?" A finding that can't answer this question doesn't get elevated.

**Targets**: Motivational axis — drives C-05 (spec anchoring), C-04/C-10 (blast radius as the natural "what breaks" answer), C-08 (remediation follows from "what to fix"). Creates natural pressure toward specificity without adding schema overhead.
**Hardest remaining**: C-14, C-15 (R3 aspirationals not directly addressed)

---

### V-04 -- Combined (Filter Log Resolution + Active Negative Comparison)
**Axes**: V-01 + V-02

**Targets**: C-14 + C-15 both by construction. Filtering axis is structurally enforced (filter log + resolution block). Cross-skill section is structurally enforced (3-step comparison). This combination gives **partial C-16**: both named axes have structural enforcement, but no universal empty-state protocol covers all other section types.
**Hardest remaining**: C-11 (full empty-state coverage), C-12 (elevation narrative)

---

### V-05 -- Combined: Full Structural Symmetry
**Axes**: Filter Log Resolution + Active Negative Comparison + Universal Empty-State + **Structural symmetry declaration**

The preamble explicitly names both structural axes and their mechanisms. A **structural enforcement checklist** at the end lists verifiable signals for both axes — neither requires reading finding content to confirm.

**Targets**: C-14 + C-15 + C-11 + **C-16 (directly)** — the symmetry declaration makes both axes observable from structure alone, which is exactly what C-16 requires.

---

**Key axis innovation in R3**: The "inertia framing" axis (V-03) is new to R3 — it hasn't been tried in R1 or R2. It works differently from schema-enforcement axes: instead of adding structural guardrails, it repositions the author's goal from "fill in columns" to "prove what static review misses." Worth scoring independently to test whether motivational framing competes with structural enforcement on the same criteria.
