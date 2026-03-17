`campaign-decide-rubric-v17-2026-03-17.md` written.

**Two new criteria added:**

| ID | Pattern | Source | Implies |
|----|---------|--------|---------|
| C-43 | Temporal commit encoded at SCHEMA PREAMBLE definition time | R17 V-01 — `(fill-now)`/`(defer-to-Phase-5)` in preamble column headers, not first declared at closure-directive time | C-42, C-28 |
| C-44 | Per-phase minimum evidence count annotations | R17 V-03 — `[min: 2 named rivals]` in phase section headers as bracket-notation gate | C-14, C-20 (additive) |

**Scoring model update:**

| Tier | v16 | v17 |
|------|-----|-----|
| Aspirational denominator | /34 | /36 |
| Aspirational total pts | 17.0 | 18.0 |
| Max composite | 107.0 | 108.0 |

**Interaction chains:**

- C-43 extends the temporal-commit chain: C-28 → C-42 → C-43 — temporal columns identified in schema, annotated per column in closure directives, encoded in preamble headers so propagation is automatic. Each step moves declaration earlier in document lifecycle.
- C-44 is parallel to C-14/C-20 (additive in header, not conflicting) and parallel to C-40 (both use bracket notation but at different document locations: closure directives vs. section headers). Independent of all prior chains.

**C-45 candidate noted** (R17 Excellence Signal — V-04): Combined C-43 + C-44 in a single variation confirms the two axes are independent and additive with no interaction degradation.
