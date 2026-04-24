Written to `simulations/quest/rubrics/quest-rubric-mock-ns-v2-2026-03-15.md`.

**What changed in v2:**

Three new aspirational criteria extracted from Round 1 excellence signals:

- **C-11** — Flag computed as a named step *before* header assembly. V-01's "computes flag before header block; references it by name" and V-03's "Do not defer it" both signal that procedural sequencing is the key defense against the most common C-04 failure. C-04 only checks presence; C-11 checks that the value was resolved first.

- **C-12** — topic-status exclusion documented inline with the default skill table. C-06 passes when the right default is chosen. C-12 catches the residual risk: if the exclusion note is absent, a model under pressure can still substitute topic-status. V-01 and V-03 both carried explicit exclusion language ("topic-status is excluded as meta-structural", "Do NOT use topic-status") — that's the pattern to promote.

- **C-13** — Fidelity warning leads the body as a framing section with `---` delimiters. C-07 passes when the warning is present anywhere. C-13 captures V-04's strongest pattern: warning block positioned *before* mock content as the organizing concept, not appended after. Explicitly independent of C-07 so the distinction is scoreable.

**Scoring update:** aspirational denominator changes from 2 to 5 (`pass/5 * 10`), keeping the band ceiling at 10 and total composite at 100. C-07 pass condition tightened to score truncated HIGH-STRUCTURE warnings as PARTIAL (addresses V-02's gap). C-10 pass condition tightened to require a dedicated emit line (also addresses V-02's gap).
