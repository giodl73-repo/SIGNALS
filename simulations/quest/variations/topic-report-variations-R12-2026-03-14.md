Written to `simulations/quest/rubrics/topic-report-rubric-v12-variations-R12-2026-03-15.md`.

---

## R12 Variations Summary

**Neutral base (V-05)**: R11 V-04 (D+E+F) — 37/37 under v12.

Three axes selected from the R12 discriminator candidates:

| Axis | Candidate | What it adds | Where it fires |
|------|-----------|-------------|----------------|
| G | C-46 | `[C-40]` tag on contamination consequence label | Recovery phase — consequence line in Branch A header |
| H | C-47 | Format-type qualifiers on G-2/G-3/G-4/G-5 Branch A register entries | Planning phase — CONTRACT REGISTER at read time |
| I | C-48 | Named `Contamination format-vector [C-48]:` line citing Branch B format types as the structural contamination mechanism | Recovery phase — joins C-34 prohibition to C-41 declarations |

**Variations:**

- **V-01 (G only)**: `SLOT 3 contamination consequence [C-40]:` — one character change to the label, makes the consequence criterion-recoverable at the label itself.
- **V-02 (H only)**: G-2 gains `(markdown table, four columns)`, G-3 gains `(markdown list, one item per signal)`, G-4/G-5 gain `(markdown sentence, prose)` — symmetric format pre-delivery to Branch A.
- **V-03 (G+H)**: Both axes; candidate composite C-49 = planning-phase format map + recovery-phase criterion-tagged consequence = closed format-contamination arc.
- **V-04 (G+H+I)**: Triple; Axis I adds `Contamination format-vector [C-48]:` before the consequence line, naming the Branch B format-type constraints from C-41 as the specific structural mechanism of contamination — converts C-34+C-41 from co-presence to a named joint property.
- **V-05 (neutral)**: R11 V-04 verbatim.

**Predicted tie**: V-01=V-02 at 38/40 under v13 if C-46 and C-47 are independent (no composite). The same structural question as R10's V-01=V-02 and R11's V-05=V-02, now rotated to consequence-label-tagging vs. Branch A format pre-delivery.
