---

## R10 Variation Summary

| Variation | Axis | New Structural Element | Candidate Criterion |
|-----------|------|----------------------|---------------------|
| **V-01** | Role sequence | Intra-row column-group gate (C-phase before D-phase within slot); 5-level architecture (Table → Section → Slot → **Column-Group** → Column) | C-32: *Intra-row column-group sequencing gate* |
| **V-02** | Output format | Trigger Condition column (D-owned, 10th column): threshold expression + detection signal; closes scenario lifecycle at entry end | C-33: *Trigger condition specification — threshold + detection signal, bounding scenario at entry as Recovery/TTV bounds it at exit* |
| **V-03** | Lifecycle emphasis | Verification Signal as 3rd sub-field per Recovery Path stage (mechanism + SLA + **VS**); each stage now names its observable confirmation | C-34: *Verification signal per recovery stage — commitment-and-confirmation pair per stage* |
| **V-04** | V-01 + V-03 | Column-group gate + verification signals | C-32 + C-34 simultaneously |
| **V-05** | All three | All axes + full R9 inherited machinery (C-17 through C-31) | C-32 + C-33 + C-34 simultaneously; richest scenario lifecycle specification |

**Key preservation**: All 15 v9 criteria (C-17 through C-31) are explicitly carried in every variation. The Column Contract, Architecture table forward references, anti-split instructions, phase gate, row descriptors with slot-level imperatives, consequence enumeration, sub-field completeness gates, and three-component chronic framing are all present and intact.

**Expected R10 discrimination under v9 rubric**: All five variations tie at 15/23 = 96.52 (rubric saturated). Differentiation is by pattern richness. Tiebreaker: V-05 > V-04 > V-03 = V-02 > V-01 by candidate-criterion accumulation.
