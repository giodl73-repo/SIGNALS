Here are the 5 R9 variations targeting the open frontier:

---

## Round 9 Variation Map

| V | Axis | Targets | Hypothesis |
|---|------|---------|------------|
| **V-01** | Inertia framing | C-37 + C-38 | Add ANCHOR-CARD to Phase 3, `anchor: true` + `orthogonality` to YAML schema, and explicit Phase 1/Phase 2 labels to the cross-set scan — over R8 V-03 gap-first base |
| **V-02** | Role sequence | C-40 + C-41 (strengthened) | Assign formal `GAP-{slug}` identifiers in INERTIA-GAP ANALYSIS; require POSITIVE SOURCING statement per expert; Diagnosis Card cites gap by `GAP-{slug}` name, not positional number |
| **V-03** | Output format | C-37 (YAML) + C-41 (YAML) | Add `[FC-11] orthogonality` and `[FC-12] inertia_gap_inherited` to YAML schema; both fields must appear in output files, not only Diagnosis Cards |
| **V-04** | Combined | C-37–C-41 | Full synthesis of V-01 + V-02 + V-03: ANCHOR-CARD first + phase-decomposed scan + `GAP-{slug}` identifiers + POSITIVE SOURCING + YAML persistence of both fields |
| **V-05** | Combined, imperative register | C-37–C-41 (100.00 target) | V-04 content recast as numbered checklist with direct imperative phrasing and a Final Checklist that names each new criterion explicitly — tests whether register precision reduces edge-case failures |

---

Key design decisions for R9:

**V-01 vs R8 V-02** — V-02 had the ANCHOR-CARD in Diagnosis Cards but didn't extend `orthogonality` into the YAML output files, and its scan used numbered steps rather than explicitly named phases. V-01 fixes both.

**V-02 vs R8 V-03** — V-03 cited gaps positionally ("Gap N inertia resistance from Phase 2") rather than by named identifier. V-02 introduces the `GAP-{slug}` naming convention as the sourcing anchor and adds a mandatory POSITIVE SOURCING statement per expert, satisfying C-40's gate-vs-fence distinction.

**V-03** is a pure output-format axis — same pipeline, two new YAML fields — which isolates whether YAML persistence (vs. Diagnosis Card only) is what C-37 and C-41 specifically require.

**V-05's Final Checklist** is the novel structural element: it names C-37 through C-41 by criterion ID and states the observable evidence required for each, making the scoring model's own rubric visible to the generating model at completion time.
