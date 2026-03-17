Written to `simulations/quest/rubrics/trace-migration-rubric-v17-2026-03-15.md`.

---

**v16 -> v17 changes:**

| New | Axis | Core distinction |
|-----|------|-----------------|
| **C-48** | D | C-46 tests annotation presence at ENTRY REFERENCE positions. C-48 tests whether a rationale note is embedded at the point of use, stating that the annotation is self-documenting there without consulting the EXIT BLOCK. Passes C-46, fails C-48 = annotation symmetric, design intent must be inferred rather than read. |
| **C-49** | D | C-47 tests whether the manifest states a self-referential completeness rule. C-49 tests whether the rule includes an imperative action directive (positive: "Apply this rule"; negative: "do not rely on cross-document search"; or both). Passes C-47, fails C-49 = rule exists but application is unspecified. |
| **C-50** | D | C-47 tests whether the completeness rule exists. C-50 tests whether the rule's coverage domain is self-defining by enumerating the three block types (BOUNDARY PROTOCOL, EXIT BLOCK, ENTRY REFERENCE) rather than "any block." Passes C-47, fails C-50 = rule is correct but scope requires inference from prompt architecture. |

**Scoring:** 285 -> 300 pts · 47 -> 50 criteria · 39 -> 42 aspirational · Golden 206 -> 206 (69%).

**The ENTRY REFERENCE annotation chain is fully specified at two levels:** C-46 (annotation present) → C-48 (rationale embedded at point of use). The manifest completeness contract chain is now three levels deep: C-47 (rule stated) → C-49 (rule operationalized with action directive) → C-50 (rule scope self-defined by block-type enumeration).
