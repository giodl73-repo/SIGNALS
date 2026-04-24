Written to `simulations/quest/golden/topic-achievements-variate-R7-2026-03-17.md`.

---

## Variate R7 — topic-achievements

**Basis**: R6 V-05 (Golden Synthesis, Platinum 100/100 under v6). v7 adds C-22 and C-23, both of which R6 V-05 satisfies structurally. R7 asks whether they're satisfied *fully* — i.e., whether the registry is truly self-sufficient and the FAIL contracts are truly bi-directional at the semantic level.

---

### Variation Axes

| Axis | Targets | Used In |
|------|---------|---------|
| Lifecycle emphasis — registry full-schema expansion | C-22 | V-01, V-04, V-05 |
| Output format — registry primacy declaration | C-22 | V-02, V-04, V-05 |
| Phrasing register — severity-stratified FAIL blocks (Tier 1/2/3) | C-23 | V-03, V-04, V-05 |

---

### Summary of Five Variations

**V-01 — Registry Full-Schema Expansion**
R6 registry compresses schemas into abbreviated inline table cells — the CLASSIFY row is a single cell listing 7 lines in shorthand. V-01 expands each gate into a complete multi-line block in the registry. Per-phase prefaces reference back ("schema declared in registry above") instead of independently restating. The registry alone is now sufficient for C-22 inspection with no cross-referencing required.

**V-02 — Registry Primacy Declaration**
R6 V-05 has no explicit statement of which source is authoritative — registry and per-phase prefaces are parallel. V-02 adds `REGISTRY PRIMACY`: "Phase instructions implement these contracts; they do not redefine them." Per-phase prefaces are labeled as restatements, not independent authorities. This makes C-22's co-location binding, not merely structural.

**V-03 — Severity-Stratified FAIL Blocks**
R6 V-05's FAIL blocks are flat lists. V-03 restructures each FAIL block into three tiers: Tier 1 (structural — gate label missing), Tier 2 (completeness — required fields missing), Tier 3 (semantic bypass — fields present but intent bypassed). Tier 3 is the hardest failure mode to detect and is explicitly named as the most consequential. This targets C-23 at the semantic level, not just the format level.

**V-04 — Combination: Full-Schema Registry + Primacy**
V-01 + V-02. The registry is complete (no abbreviation) and authoritative (primacy declared). FAIL blocks preserved from R6 V-05.

**V-05 — Golden Synthesis: All Three Axes + R6 V-05 Three-Layer Architecture**
Full-schema registry + primacy + severity-stratified FAIL + per-phase schema preface labeled as "restatement of registry authority." C-22 is covered at three levels: complete (full schemas), co-located (single registry), authoritative (primacy). C-23 is covered with Tier 3 semantic-bypass named explicitly per gate.
