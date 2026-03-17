Here are the R11 variations for `campaign-brief`, written to `simulations/quest/golden/campaign-brief-variate-R11-2026-03-17.md`.

---

## Round 11 — campaign-brief variations summary

**What R11 is testing:** Whether C-30 (timestamp isolation dual-mechanism independence) is independently necessary beyond C-24's existing dual-location restatement.

**Variation axes:**

| Variation | Axis | C-29 | C-30 | Expected |
|-----------|------|------|------|----------|
| V-01 | C-30 absent — pure R10 best form (control) | PASS | PARTIAL | 290/300 |
| V-02 | C-30 preamble-only — timestamp isolation rule in preamble, no declarative guard | PASS | PARTIAL | 290/300 |
| V-03 | C-30 declarative-only — COMPRESSED-COLLAPSE GUARD in STATUS execution note, no preamble | PASS | PARTIAL | 290/300 |
| V-04 | C-30 full dual-mechanism — preamble + COMPRESSED-COLLAPSE GUARD (two separate preamble blocks) | PASS | PASS | 300/300 |
| V-05 | Full sweep — both rules in shared COMPRESSION-IMMUNE PREAMBLE block | PASS | PASS | 300/300 |

**The key new mechanism (C-30):** The COMPRESSED-COLLAPSE GUARD is the declarative component — it names "COMPRESSED-collapse" as the specific failure mode it prevents (the model treating `found` timestamps as abbreviatable alongside blocking entries). This mirrors exactly how TOKEN-PRESSURE GUARD names "conditional-context suppression" for C-29. The two guards on each rule target orthogonal failure modes: preamble position counters location elision; the named declarative guard counters processing-without-absorption.

**V-05's structural innovation:** A single `COMPRESSION-IMMUNE PREAMBLE` block containing both rules, each independently guarded. The rubric's R10 excellence signal predicted this: "suppressing any single rule requires suppressing the entire preamble" — making it an atomic compression contract rather than two independent preamble sections.
