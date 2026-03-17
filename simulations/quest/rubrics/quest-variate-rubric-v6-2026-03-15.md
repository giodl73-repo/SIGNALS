Written to `simulations/quest/rubrics/quest-rubric-variate-R6-2026-03-15.md`.

---

## What changed v5 → v6

**4 new aspirational criteria** extracted from R5 excellence signals:

| ID | Criterion | Source | Key distinction |
|----|-----------|--------|-----------------|
| **C-28** | Count-verifiable axis-freeze completeness gate | R5 V-03, V-05 | C-26 requires *naming* each axis. C-28 requires declaring the expected *count* and refusing to proceed if the count isn't met — count audit vs name audit. |
| **C-29** | VARIATION MAP as authoritative read-source for in-loop freeze | R5 V-05 | C-26 (per-body freeze) and C-27 (standalone map) can pass independently. C-29 requires the map to explicitly declare it is the source and the freeze entries to confirm they read from it — wires the two artifacts into a chain. |
| **C-30** | Failure-condition predictions in pre-generation variation map | R5 V-04 | C-24 requires "which criteria improve." C-30 requires the map to also contain per-variation failure-mode predictions (`failure-condition-outcome prediction`, `failure-condition-implementation prediction`) — extends the map from "what improves" to "what breaks and how." |
| **C-31** | Cross-artifact axis consistency gate in the generation loop | R5 V-05 | C-15 requires a gate that names criteria. C-31 requires the gate to explicitly verify the VARIATION MAP axis matches the per-variation planning header axis — detects silent divergence between the two artifacts before the body is written. |

**Scoring formula**: aspirational denominator `/ 19` → `/ 23`. All bands and weights unchanged.
