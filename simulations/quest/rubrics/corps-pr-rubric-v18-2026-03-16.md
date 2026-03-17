Written to `simulations/quest/rubrics/corps-pr-rubric-v18-2026-03-17.md`.

---

## v17 -> v18: Two new criteria

**C-55 -- Phase D ban-to-fix reference table co-located with Mechanism column declaration**

Closes the gap left by C-12/C-13 (ban-to-fix check present; ban list enumerated). R20's V-02/V-04/V-05 Phase D ranked table format showed the banned-phrase reference table embedded directly adjacent to the Mechanism column declaration -- making compliance O(1) per Mechanism cell by cell scan, parallel to CLOSED PATHS declaration-point enforcement. C-55 requires the ban-to-fix table to be co-located with the Mechanism column declaration when Phase D uses a table format. Passes by default for prose Phase D (no Mechanism column).

**C-56 -- Phase D IA ledger summary rendered as named fields**

Closes the gap left by C-03 (Phase D synthesis covers all Phase C findings). R20's V-02/V-04/V-05 showed the Phase D preamble rendered as `IA ledger: ...` / `IA position: ...` named fields, extending the pipeline-wide named-block convention (READ RECEIPT, C2 RESULT, PRE-COMMITMENT) to the synthesis section. C-56 requires named field labels on the IA summary in Phase D when C-11 is active. Passes by default when no Inertia Advocate.

**Scoring update:**

| Band | Count | Per-criterion | Total |
|------|-------|--------------|-------|
| Essential (C-01--C-05) | 5 | 12.000 | 60 |
| Recommended (C-06--C-08) | 3 | 10.000 | 30 |
| Aspirational (C-09--C-56) | **48** | **~0.208** | 10 |
| **Max** | | | **100** |

R20 scores against v18: V-01/V-03 (prose Phase D) pass C-55 and C-56 by default; V-02/V-04/V-05 satisfy both actively. All five score 48/48 aspirational, composite 100. R21 target: propagate both patterns to all five variations including prose Phase D variants.
