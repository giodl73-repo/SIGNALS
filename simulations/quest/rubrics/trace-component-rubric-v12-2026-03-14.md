**trace-component-rubric-v12** written to `simulations/quest/rubrics/trace-component-rubric-v12-2026-03-15.md`.

---

## Two new criteria from R11 excellence signals

**C-38 . Manifest-Close Adjacency Marker** *(V-02 HIGH-WATER MARK on C-37)*

The `↓ TABLE-N begins immediately below` line embedded at the manifest's **closing position** — not in the header, not in a charter preamble. This is the structural distinction that makes adjacency enforcement point-of-production: a model inserting content after that line must contradict the last thing it wrote.

- V-01 carried the instruction at the manifest header (non-zero risk: content can slip between manifest content and table)
- V-03/V-05 declared the rule in a charter preamble (role-drift risk across phases)
- V-04 had both header + close marker (PASS, two mechanisms)
- V-02 had five close-line markers, no header instruction needed (structural high-water mark)

Pass condition: every MANIFEST-N ends with the prohibition line as its last content; at least three manifest blocks carry it; charter-only or header-only fails.

**C-39 . Self-Authored Schema Constraint** *(V-03 SCHEMA CHARTER + V-05 TRAVERSAL-SCHEMA)*

When the model authors the schema artifact (declaring the inert-default and adjacency rules) in a prior role before the trace analysis, violation in the analysis role is self-contradiction of prior output — not disobedience of an external instruction. V-03's "Organizational Principle 2" and V-05's Role 1 TRAVERSAL-SCHEMA exemplify this; both closed the gap between instruction-compliance and self-constraint.

Pass condition: model produces a named schema artifact (SCHEMA CHARTER, TRAVERSAL-SCHEMA, or equivalent) declaring both the C-36 inert-default rule and the C-37 adjacency rule before the analysis role begins; externally-provided templates fail.

---

**Updated ceiling: 152 pts** (31 aspirational × 2 + 90 essential/recommended)

**Pair structure:** C-38 is micro-enforcement (per-manifest close line), C-39 is macro-enforcement (schema ownership across the full trace). They are orthogonal: C-38 can be satisfied without C-39 (close markers present, schema externally provided) and vice versa. Full enforcement requires both.
