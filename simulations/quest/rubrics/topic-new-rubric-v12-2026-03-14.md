`topic-new-rubric-v12-2026-03-15.md` written.

---

## v12 — three new criteria from R12 excellence signals

| ID | Name | Sharpens | Source |
|----|------|----------|--------|
| C-39 | FIELD SCHEMA carries a Decision-State Anchor column anchoring all three priority levels | C-35 | V-01/V-04/V-05 ES-1 |
| C-40 | F-05 Consumer must appear verbatim as a Decision-Maker Role in Phase 1 decision table | C-36 | V-02/V-04/V-05 ES-2 |
| C-41 | Pipeline overview carries a third consequence column naming the concrete recovery rework chain | C-38 | V-03/V-04/V-05 ES-3 |

**Aspirational denominator**: 30 → 33

**Scoring formula**: `aspirational_pass / 33 * 10`

---

**Gap logic:**

- **C-39** — C-35 closes vocabulary substitution at the essential tier only. C-39 adds a dedicated Decision-State Anchor column in FIELD SCHEMA anchoring all three tiers simultaneously: essential=decision blocked, recommended=quality risk accepted, optional=consumer decides unaffected. The recommended/optional collapse vector is now structurally closed alongside essential.

- **C-40** — C-36 makes Producer→Consumer a schema-level field, auditable by inspection. C-40 requires the Consumer value at fill time to appear verbatim as a Decision-Maker Role in the Phase 1 decision table, verified by an explicit Phase 2 exit gate checkpoint. Closes the orphaned-consumer failure mode: F-05 correctly formatted but pointing to a role with no grounded decision authority.

- **C-41** — C-38 names the team's inertia default (what the system drifts to without intervention). C-41 adds a third column naming the concrete recovery rework chain when the skip is caught late — "Re-run Phase 2, re-run Phase 3, re-write both output files." Closes the skip-cost underestimation axis where inertia is named correctly but the repair effort stays abstract.
