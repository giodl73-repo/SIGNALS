**flow-dataflow — Round 6 Variations written** to `simulations/quest/golden/flow-dataflow-variate-R6-2026-03-15.md`

---

**R6 Design Summary**

The three new v5 criteria (C-17, C-18, C-19) each get a dedicated single-axis variation, plus a combination:

| Variation | Axis | Targets | Key Innovation |
|-----------|------|---------|----------------|
| **V-01** | Trigger ID pre-numbering | C-18 | NH-NN/LP-NN assigned at declaration; recovery table cites by ID — missing rows are structurally detectable without reading prose |
| **V-02** | Stage-exit entity declaration | C-17 | Each stage closes with "Entities exiting Stage N: [list]"; boundary's Entity at Risk must be drawn from that list — prevents ad-hoc entity invention at boundary time |
| **V-03** | Boundary latency decomposition | C-19 | Splits boundary latency into Transport Latency + Processing Overhead sub-columns; stale analysis addend sequence shows both components |
| **V-04** | Cross-reference verification index | C-17/C-18/C-19 | Post-trace index (one row per boundary) makes all three criteria co-visible; blank cell = explicit gap; includes a self-correction mandate |
| **V-05** | Combined | C-17+C-18+C-19 | Trigger IDs + stage-exit entity constraints + 6-col recovery audit table with Triggering Condition column + verification index with self-correction |

**Key structural bet**: V-01's Trigger IDs solve the C-18 "triggering condition" linkage problem that R5's "Entry Source + Location" columns left ambiguous. V-02's stage-exit declaration prevents the entity quality degradation that boundary-level free-form naming introduces. V-04/V-05's self-correction mandate — "if any status reports a gap, correct it in the upstream step before finalizing the index" — is a new enforcement pattern not present in R5.
