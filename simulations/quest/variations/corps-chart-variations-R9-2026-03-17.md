Here are the five R9 variations, targeting C-23, C-24, C-25:

---

## Variation Summary

| ID | Axis | New Criteria | Hypothesis |
|----|------|--------------|------------|
| **V-01** | FORMAT CONTRACT DISQUALIFY-IF (single) | C-23 | Pre-generation disqualification at schema-declaration time — DISQUALIFY-IF annotations inside the FORMAT CONTRACT fire before any PRODUCE command runs, placing the disqualifying output variants in immediate context at every writing moment. Tests whether schema-time signal alone reduces merged-column, denominator-free Quorum, and untyped cat-N failures without VERIFY blocks. |
| **V-02** | Four-field Rebuttal activation triad (single) | C-24 | The critical distinction from R8 V-05: the ROLE-NAME LOCK CHECK is embedded **inside** the REBUTTAL FORM block header, co-located with the ROLE UNDER PRESSURE field label, rather than placed as a sentence before the form. The model cannot fill ROLE UNDER PRESSURE without passing through the CHECK. Tests whether this structural co-location closes C-24 where R8's proximity-but-not-embedding did not. |
| **V-03** | Strict DRI/Owner ROLE-LOCK (single) | C-25 | Replaces all hedged DRI/Owner language ("where possible", "reference a role...") with mandatory present-tense enforcement ("every value must appear in the ROLE-NAME LOCK list — no new role names are introduced in this column") in the same instruction block as DRI/Owner formatting. Tests whether strict language at DRI/Owner closes the C-12 partial pattern without FORMAT CONTRACT or activation triad. |
| **V-04** | C-23 + C-24 combination | C-23, C-24 | Two-phase disqualification (DISQUALIFY-IF before generation + VERIFY at PRODUCE) combined with the C-24 activation triad (embedded CHECK form + VERIFY). Built on R8 V-04 base (vocabulary-lock/VERIFY already present). DRI/Owner remains the open variable. |
| **V-05** | Full integration: C-23 + C-24 + C-25 on R8 V-05 | C-23, C-24, C-25, all prior | Maximum constraint density: DISQUALIFY-IF in FORMAT CONTRACT, embedded-CHECK REBUTTAL FORM triad, strict mandatory DRI/Owner enforcement — all three layered on the R8 V-05 baseline. |

---

**Key R9 design decisions:**

**C-23** — The DISQUALIFY-IF annotations appear *inside* the FORMAT CONTRACT block (not at PRODUCE commands, which is what C-18 already does). This creates a two-phase disqualification: FORMAT CONTRACT fires pre-generation, VERIFY fires at production. The annotations target the three schemas with documented failure modes: headcount table (merged columns), charter Quorum (denominator-free), and Anti-Pattern Watch (untyped cat-N citations).

**C-24** — The activation triad's structural refinement over R8: the CHECK is the first line inside the REBUTTAL FORM code block, immediately above the `ROLE UNDER PRESSURE:` field label. The model reads the CHECK as part of reading the form template — it cannot fill the field without encountering the governance constraint.

**C-25** — The instruction block consolidates all DRI/Owner requirements in one place: the column definition, the mandatory role-lock language, and the row count minimum appear together. "Where possible" is replaced with "must appear" + "no new role names are introduced" — present-tense mandatory, not hedged advisory.

Written to: `simulations/quest/golden/corps-chart-variate-R9-2026-03-17.md`
