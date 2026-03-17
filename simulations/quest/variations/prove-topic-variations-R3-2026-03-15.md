Written to `simulations/quest/golden/prove-topic-variate-R3-2026-03-15.md`.

---

## prove-topic — Variation Round R3 Summary

Five complete variations targeting the new C-14/C-15 criteria from rubric v3, plus a new single-axis axis not explored in R1 or R2.

| Variation | Axis | New Signal Targeted |
|-----------|------|---------------------|
| **V-01** | Evidence weighting | Weighted ledger (30/30/40) with Thin-prototype cap at synthesis |
| **V-02** | Confidence calibration | Numeric 0–10 score per stage; < 4 any stage → LOW cap; composite in frontmatter |
| **V-03** | Artifact chaining | `prior_artifact:` field in every frontmatter creates traversable audit chain |
| **V-04** | Counter-evidence posture + gate trace | Mandatory Part B counter-evidence search at S2/S3/S4; gate_s_path in artifact (C-15 amplified); null-result fallback in register (C-14) |
| **V-05** | Full compound | R1 GATE S + per-path naming + R2 comparator + C-14 counter-evidence register + C-15 gate trace + R3 evidence weights |

**Where C-14 appears in each variation:**
- V-01/V-02: `Counter-Evidence` section with explicit null fallback in synthesis
- V-03: Same, with chain-break framing ("recommend adversarial pass")
- V-04: Counter-evidence as mandatory Part B at each evidence stage + aggregate register at synthesis
- V-05: Same as V-04, with strongest null-fallback language ("cannot be treated as confirmation")

**Where C-15 appears in each variation:**
- All five: `gate_s_cleared: true` in hypothesis frontmatter
- V-04/V-05: Also `gate_s_path:` so gate clearance is auditable from artifact alone without session replay
