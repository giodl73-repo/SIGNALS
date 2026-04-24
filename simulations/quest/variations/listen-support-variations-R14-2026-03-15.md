Written to `simulations/quest/golden/listen-support-variate-R14-2026-03-15.md`.

---

**R14 variation summary:**

| Variation | Axis | New criterion targeted |
|-----------|------|----------------------|
| V-01 | Two-layer labeling (LAYER 1 of 2 / LAYER 2 of 2) | C-38 |
| V-02 | Grep anchor token `[SYNERGY-ANCHOR: C33xC34]` in both sites | C-39 |
| V-03 | Explicit DEGRADATION CLAUSE with if/then conditional | C-40 |
| V-04 | V-01 + V-02 | C-38 + C-39 |
| V-05 | All three | C-38 + C-39 + C-40 |

**What each axis adds over R13 V-05:**

- **C-38 (V-01):** R13 had both sites but neither was labeled. LAYER 1/2 labels let a scorer confirm two-location presence by scanning for the label strings without reading content.
- **C-39 (V-02):** R13 had no navigation mechanism between the two sites. The `[SYNERGY-ANCHOR: C33xC34]` token embedded in both sites lets a scorer grep once and reach both — closes the declaration-to-trace loop.
- **C-40 (V-03):** R13 had a single-line "Degradation declared: YES/NO." The DEGRADATION CLAUSE restructures it as a testable if/then: trigger condition (token absent) → immediate consequence (prose required) → C-34 cascade (no-traversal degrades). Makes the claim auditable as a logical proposition, not just an assertion.
