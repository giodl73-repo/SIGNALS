Written to `simulations/quest/golden/trace-contract-variate-v10-R10-2026-03-15.md`.

---

## trace-contract Variate — Round 10 (rubric v10)

### Round context

R9 V-05 was full platinum at C-01–C-28. The two new criteria for R10 are escalations from C-28 (per-finding `mechanism-type:` taxonomy):

- **C-29** — `mechanism-type-shared:` in Singleton and Multi-pattern branch templates. The field already exists in R9 V-05 but is marked **"if applicable"** (optional). C-29 escalates: unconditionally required, with fix-strategy semantics explicit — same-class → systemic root cause, one fix; `mixed` → coincident symptoms, independent fixes.

- **C-30** — `mechanism-distribution:` aggregate in Summary. R9 V-05 already has `Mechanism taxonomy distribution: field-mapping:? | ...` but it's a pipe-delimited placeholder. C-30 escalates: compact computed key `mechanism-distribution: field-mapping:2 serialization-path:1`, enumerated from S5 finding blocks (not estimated).

### Variation map

| # | Axis | Targets | Mechanism |
|---|------|---------|-----------|
| **V-01** | role-sequence | C-29 only | Connectors expert owns Phase 1 + Phase 4. Because the contract author runs Patterns synthesis, `mechanism-type-shared:` becomes a required expert judgment, not an optional annotation. |
| **V-02** | output-format | C-30 only | Summary `mechanism-distribution:` upgraded to compact space-separated aggregate with explicit enumeration instruction — "walk through every finding block, tally type tokens, write counts." |
| **V-03** | lifecycle-emphasis | C-29 + C-30 | Named **Taxonomy Synthesis step (Step 5.5)** inserted between findings and the closure gate. Sub-task A enumerates type tokens → `mechanism-distribution:` (C-30). Sub-task B identifies group type alignment → `mechanism-type-shared:` per group (C-29). Both computations forced before the gate closes. |
| **V-04** | role-sequence × output-format | C-29 + C-30 | Combines V-01 + V-02. Additive: role framing doesn't help Summary aggregate; format change doesn't promote `mechanism-type-shared:` from optional. |
| **V-05** | all three + R9 platinum base | C-29 + C-30 + C-01–C-28 | Skeleton pre-declaration of all upgraded positions. Two new behavioral protocol invariants (C-29: field unconditional; C-30: enumerated not estimated). New ceiling at 30/30 criteria. |

### Key structural changes from R9 V-05

1. **Patterns branches** — `mechanism-type-shared:` + `fix-strategy:` slots added, marked `REQUIRED`, "if applicable" removed
2. **Summary** — `mechanism-distribution: type:count type:count` replaces pipe-delimited placeholder; explicit enumeration instruction added
3. **Step 5.5** — Taxonomy Synthesis step (V-03/V-05) pre-computes both fields before the `[FINDINGS-RESOLVED ...]` gate closes
4. **Behavioral protocol** — Two new invariants (#11 and #12) in V-05
