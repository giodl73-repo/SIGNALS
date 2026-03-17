Done. `campaign-decide-rubric-v15-2026-03-17.md` written.

**Two new criteria added:**

| ID | Pattern | Source | Implies |
|----|---------|--------|---------|
| C-39 | Fill-forward directive encoded as Phase 5 section-header gate annotation | R15 V-01 — "fill-forward at phase boundary level (strongest location)" excellence signal | C-37, C-35, C-13 |
| C-40 | Bracket notation for FINDING REGISTER column-closure directives | R15 V-02 — bracket vs prose column enumeration variation axis | C-38, C-36 |

**Scoring model update:**

| Tier | v14 | v15 |
|------|-----|-----|
| Aspirational denominator | /30 | /32 |
| Aspirational total pts | 15.0 | 16.0 |
| Max composite | 105.0 | 106.0 |

**Interaction chains extended:**

- C-39 closes the C-13 → C-35 → C-37 → C-39 chain: prior anchored at Phase 0, carried to Phase 5, schema pre-defined in preamble, fill-forward directive placed in Phase 5 section header as a gate annotation (strongest propagation location — precedes all sub-table content)
- C-40 closes the C-16 → C-36 → C-38 → C-40 chain: pre-seeded once, closed per-phase, columns named per closure, column list encoded in bracket notation (machine-parseable, syntax-distinct from prose)

**Design note on C-39 vs C-37:** C-37 requires the fill-forward directive to exist in Phase 5 pointing back to the preamble. C-39 hardens the location: the directive must be in the section header itself, not inline below it. The R15 V-01 evidence makes this explicit — `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]` in the header is called out as "fill-forward at phase boundary level (strongest location)", which is a new structural property above the C-37 threshold.
