Written to `simulations/quest/golden/campaign-simulate-variate-R11-2026-03-17.md`.

---

## campaign-simulate -- Round 11 Variations

**Context**: R10 V-05 satisfies C-38/C-39/C-40. R11 pushes each ceiling one step further.

### Variation axes chosen

3 single-axis explorations → 1 combination → 1 full integration:

| | Variation | Axis | Innovation | Targets |
|---|-----------|------|------------|---------|
| V-01 | DR-NN Contributed Column | Output format | Layer Completion Record gains DR-NN Contributed column — fourth C-38 verification path; per-sub-skill dependency attribution without reading the dependency map | C-36, C-38 extension |
| V-02 | P1/P2 Gate Signal Decomposition | Phrasing register | Gate signal split into named P1 (execution order) + P2 (dependency map) with per-sub-skill DR attribution and addition confirmation (N1+N2+N3=N_total) — closes scope-attribution gap | C-32, C-36, C-38, C-39 extension |
| V-03 | Self-Reference as Opening Sentence | Phrasing register | Row Count Assertion opens: "This Row Count Assertion is itself C-37's completeness proof and appears as the final axis listed below" — self-reference verifiable from first sentence, not list scan | C-37, C-40 extension |
| V-04 | Mutual Cross-Reference | Output format + phrasing register | Combines V-01 DR-NN column + V-02 P1/P2; gate signal P2 explicitly cites "Layer Completion Record column DR-NN Contributed" — two mechanisms triangulate each other | C-32, C-36, C-38+C-39 extension |
| V-05 | Full Integration | All three | R10 V-05 eleven-axis base + V-01 column + V-04 P1/P2 + V-03 opening sentence; SAD preserved at 11 rows, three axis descriptions enriched | All through C-40 |

### New mechanisms introduced

**C-38 extension** (V-01, V-04, V-05): `DR-NN Contributed` column in the Layer Completion Record — a reviewer sums the column to get the full dependency map size without reading the map section. Empty-state template added for Platform sub-skills that contribute zero rules.

**C-39 extension** (V-02, V-04, V-05): Gate signal restructured as P1/P2 named properties. P2 lists per-sub-skill DR attribution with `N1 + N2 + N3 = N_total` addition confirmation. A scope-attribution mismatch (e.g., trace-state declaring permission rules) would be visible in P2's per-sub-skill listing even if the range total looks correct.

**C-40 extension** (V-03, V-05): Row Count Assertion opens with an explicit self-reference sentence. The C-40 property is verifiable by reading only the first sentence, rather than scanning the list to locate the C-37 axis entry.
