All changes are in place. Written to `simulations/quest/golden/quest-rubric-variate-v20-R19-2026-03-16.md`.

---

**What changed in v20:**

**C-51 — Phase 8.5 FORMAT TEMPLATE slot gate-enforced by co-located STOP condition** (extends C-49)

C-49 requires a FORMAT TEMPLATE with a mandatory `[C-NN]` slot. C-51 requires that slot to be co-located with a STOP condition blocking Phase 8.5 note completion until the slot is filled. This converts C-49's structural slot from an *SV-detectable unfilled placeholder* to a *gate failure at note-completion time* — a builder cannot seal the note without triggering an explicit block.

Independence: R18 baseline FORMAT TEMPLATE variation demonstrates PASS C-49 / FAIL C-51 (slot present, no co-located STOP). V-01 of R19 demonstrates PASS C-51.

**C-52 — STATUS QUO foil items preceded by SPAN DEFINITION pre-step** (extends C-50)

C-50 requires full-span enumeration in the foil item text. C-52 requires each foil item to be preceded by a declared SPAN DEFINITION block: previous failure criterion (or START), current failure criterion, and full pass-side enumeration — from which the foil item is transcribed. This converts C-50's *observed completeness property* into a *structurally pre-declared computation*.

Independence: V-02 of R19 demonstrates PASS C-50 / FAIL C-52 (full span in foil item, no pre-step). V-03 of R19 demonstrates PASS C-52.

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/44 × 10)` — denominator /42 → /44 (C-09 through C-52)

**Baseline for R20:** Variations satisfying C-49 + C-50 but lacking the co-located STOP gate (C-51 FAIL) or SPAN DEFINITION pre-steps (C-52 FAIL) score 42/44 × 10 = 9.55, composite ≤ 99.55.
