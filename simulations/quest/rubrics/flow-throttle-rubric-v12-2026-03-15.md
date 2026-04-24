Written to `simulations/quest/rubrics/flow-throttle-rubric-v12-2026-03-16.md`.

**Two new criteria extracted from V-04:**

| ID | Pattern | Source |
|----|---------|--------|
| C-33 | **Annotation field-count declaration** — when C-29+C-30 co-satisfy a three-field annotation, a header line must declare the field count and field names so completeness is verifiable by count-scan rather than criterion-matching |
| C-34 | **Closed observable set in audit test** — the C-31 observable list must declare its count per path (e.g., "Gate present — 5 observables:"), applying the C-27 closed-register pattern to the audit observable set |

**Score delta**: 120 pts (24 × 5) → 130 pts (26 × 5), max composite 210 → 220. Golden threshold unchanged.

**Structural logic:** C-33 is the canonical-form closure for multi-field annotations (analogous to how C-27 closes the exemption register). C-34 is the observable-list closure for audit tests (same pattern applied to the C-31 observable set). Both emerge from V-04's combination — neither is visible in V-02 or V-03 alone because the interaction between a formally-complete three-field annotation and a named-observable list only surfaces the "open enumeration" problem when both are present simultaneously.
