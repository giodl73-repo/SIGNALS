Written to `simulations/quest/golden/trace-skill-variate-R9-v9-2026-03-15.md`.

---

**R9 variations summary**:

| Variation | Axis | New criterion targeted | Key change from R8 V-05 |
|-----------|------|----------------------|-------------------------|
| V-01 | Single: C-30 | DefectCodeVocab closed type | Registry section gains full closed-type declaration block with 5 codes defined inline -- same structural formalism as RequiredVocabulary. C-30 audit in Verdict confirms. |
| V-02 | Single: C-31 | C-28 site count audit | C-28 audit block adds Verdict ledger's Defect code column as separate composed site #12; terminates with explicit count assertion: "12 (10 pre-C-29 + 2 C-29-composed)." |
| V-03 | Single: C-32 | Fully populated ledger + C-29 audit at top | C-29 audit moves to Verdict TOP, gains three-part check: (a) registry present, (b) FAIL rows cite vocab code, (c) no empty cells. PASS rows carry `--` sentinel explicitly. |
| V-04 | Combined: C-30 + C-31 | Both | Closed-type declaration + 12-site count in C-28 audit. Independent -- operate at registry vs. audit-block level. |
| V-05 | Combined: C-30 + C-31 + C-32 | All three -- complete R9 target | All upgrades. Ledger column is simultaneously typed (C-31), fully populated (C-32), and self-certified by top-of-Verdict audit (C-32). |

The key structural insight for R9: R8 closed one vocabulary (`RequiredVocabulary`). R9 closes the second (`DefectCodeVocab`), counts the composed annotation sites explicitly, and makes the ledger self-certifying by moving the integrity audit to precede the table it governs.
