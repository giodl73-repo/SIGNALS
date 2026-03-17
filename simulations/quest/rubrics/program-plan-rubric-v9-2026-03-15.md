Written to `simulations/quest/rubrics/program-plan-rubric-v9-2026-03-16.md`.

---

## Three new criteria from R8 excellence signals

**C-31 — Complete BAD-YAML Cross-Criterion Coverage**
The plan-level BAD YAML block (C-15) contains at least one `# WRONG C-XX` tag for each of the 7 criteria (C-01 through C-07). C-16 requires ≥1 tagged error anywhere; C-31 requires the BAD PLAN block itself to be a complete single-artifact index — all 7 criteria (essential + recommended) each represented by a tagged wrong field in the block. R8 source: V-03's BAD PLAN block carried 7 criterion-tagged violations spanning C-01 through C-07 — the first variate to make the block a complete criterion index rather than an essential-tier-only sample.

**C-32 — Production Gate Field Correction Bridge**
When the three-field gate structure (C-28) is present, the production `gate:` sibling at every non-echo zone carries an explicit `# check correction table: gate values` bridge at the field position itself. C-21 requires bridges at all gate-type fields; C-28 introduces the `gate:` production field as a structurally distinct sibling; C-32 requires the bridge to appear at the production slot specifically — the model encounters the lookup pointer at the exact moment it fills the gate, not at the contrast-only fields. C-18 and C-28 are prerequisites. R8 source: V-04 (first variate combining the three-field structure with a correction bridge at the production `gate:` field across all non-echo zones).

**C-33 — Maximal Zone Teaching Density**
Every dependency-bearing non-echo zone simultaneously carries all four annotation mechanisms: (a) three-field gate structure with criterion-tagged `gate_fail:` (C-28 + C-26), (b) production `gate:` with correction bridge (C-32), (c) dual-position dep reminder in uniform syntax at both zone-header and skills line (C-27), and (d) independent dep reminder + correction bridge at the `skills:` line (C-30). C-33 checks that all four coexist in every dependent zone — each zone a fully equipped authoring unit requiring no cross-document navigation. R8 source: V-05 (first variate achieving full four-mechanism coexistence at every dependency-bearing zone).

**Scoring change:** Aspirational 23 → 26 criteria, 115 → 130 pts. Total max: **220 pts.** Golden threshold (>= 80) unchanged.
