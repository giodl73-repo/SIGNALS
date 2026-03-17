Written to `simulations/quest/golden/mock-accept-variate-R7-2026-03-17.md`.

---

## R7 Variate Summary

**Baseline:** R6 V-03/V-05 (co-goldens, 22/22 against v7)

| Variation | Axis | What changes | Predicted |
|-----------|------|--------------|-----------|
| **V-01** | inertia-framing (position) | DDP block moved from preamble to immediately before STEP 3; STEP 1/STEP 2 run without default frame | 22/22 — tests minimum positional requirement for C-30 |
| **V-02** | lifecycle-emphasis (C-29 relocation) | Cost-of-MOCK removed from STEP 3/STEP 4; added as Slot 3 in STEP 6 | **21/22, 99.09** — predicted C-29 FAIL, confirms evaluation-record binding |
| **V-03** | inertia-framing (phase echo) | INERTIA LEDGER added to GATE C and GATE D: running tally of namespaces at default vs. earned escape | 22/22 + C-31 signal |
| **V-04** | inertia-framing (position) + (phase echo) | V-01 mid-spec DDP + V-03 INERTIA LEDGER; C-29 inline kept | 22/22 + C-31 signal; tests DDP reposition + ledger interaction |
| **V-05** | lifecycle + output-format + inertia (full) | R6 V-05 base + INERTIA LEDGER at gates + new STEP 5 (MOCK COST REGISTER) aggregating all costs post-evaluation; original STEP 5–9 renumber to STEP 6–10 | 22/22 + C-31 + C-32 signals; length-pressure risk — monitor HALT dropout |

**Key hypotheses:**
- **V-02** is the diagnostic: if C-29 fails when moved to STEP 6, the evaluation-record location requirement is confirmed tight. If it passes, C-29 needs a stronger binding constraint.
- **V-01** probes whether C-30 needs the entire spec governed or just STEP 3/4. A pass here suggests the DDP block can be positioned later without losing C-30.
- **V-03 / V-04 / V-05** all carry C-31 signal detection: the INERTIA LEDGER is structurally distinct from C-29 (per-namespace cost) and C-30 (initial state declaration) — it is a per-phase running tally.
- **V-05**'s MOCK COST REGISTER (STEP 5) is a C-32 candidate: aggregated post-evaluation registry vs. inline evaluation fields.
