Written to `simulations/quest/golden/campaign-behavior-variate-R10-2026-03-17.md`.

---

## campaign-behavior — R10 Variations

**Base:** R8 V-05 (DEPTH asymmetry anchors + Q6 + propagation chains)
**Rubric:** v8 (C-01–C-29, denominator 21 aspirational)
**New axes targeting v8 criteria C-27, C-28, C-29**

---

### Single-axis variations

**V-01 — Chain Terminus Registry (C-27)**
Adds a `**Terminus registry:**` table to Phase 0 assigning T-NN codes to every unique blast-surface endpoint. Field 3 becomes `propagation chain: [A] → [B] → [terminal: T-NN]`. Chains that cannot resolve = "unresolved chain — registry miss." Q1 in the calibration block is updated to trace chains to their T-NN terminus. All other structure is R8 V-05 unchanged.

**V-02 — EXECUTIVE SUMMARY section (C-28)**
Inserts `## EXECUTIVE SUMMARY` between the CALIBRATION BLOCK and CONSOLIDATE. Exactly 3 bullets required; each is `F-[N]: [name] | blast-radius: [tier] | chain: [A] -> [B] -> [terminal] | [CONFIRMED | RUNTIME ANOMALY]`. Top-3 identification is positional (bullet order), not inferred from the ranked findings list. No prose permitted in the section — three structured bullets, then stop.

**V-03 — Inline CONFIRMED evidence citation (C-29)**
Changes field 6 template to `CONFIRMED -- evidence: [source-phase]: [matching-finding-name]`. Propagates into VERDICT (`State CONFIRMED -- evidence: ...`) and into Q2 (audit gate: any CONFIRMED missing the inline citation must be revised before consolidation). Phase 4/5 tables also use the inline format for in-table CONFIRMED notations.

---

### Combinations

**V-04 — Terminus Registry + EXECUTIVE SUMMARY (C-27 + C-28; C-29 absent)**
Tests whether the two structural additions compose without interference. T-NN codes in field 3 feed directly into the EXECUTIVE SUMMARY bullet chain notation, creating a cross-section consistency check. C-29 is deliberately absent to isolate the C-27/C-28 interaction.

**V-05 — Full integration (C-27 + C-28 + C-29 + DEPTH asymmetry + Q6 + propagation chain)**
All six axes together. The EXECUTIVE SUMMARY bullet for a CONFIRMED finding now carries both the T-NN terminus chain and the inline evidence citation — the tightest possible top-3 summary. The VERDICT carries the T-NN chain and the `CONFIRMED -- evidence:` inline. Q2 audits for inline citations. This is the R10 golden candidate if all six axes compose cleanly.

---

### Differential from R8 V-05

| What R8 V-05 had | What R10 V-05 adds |
|---|---|
| DEPTH asymmetry `[ANCHOR: ...]` headers | Terminus registry T-NN table in Phase 0 |
| Q6 sequence integrity gate | `## EXECUTIVE SUMMARY` section (3 bullets, positional top-3) |
| Explicit propagation chain in field 3 | Inline `CONFIRMED -- evidence: phase: finding` in field 6, VERDICT, EXECUTIVE SUMMARY, and Q2 audit |
