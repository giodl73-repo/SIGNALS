Rubric written to `simulations/quest/rubrics/campaign-simulate-rubric-v1-2026-03-17.md`.

---

**10 criteria across 3 tiers:**

**Essential (C-01–C-05, 60 pts) — all must pass:**
| ID | Criterion |
|----|-----------|
| C-01 | All five sub-skills execute (flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions) |
| C-02 | Findings ranked by blast radius with explicit severity tiers |
| C-03 | System boundary + severity labeled on every finding |
| C-04 | At least one concrete spec gap or contract violation surfaced |
| C-05 | Single synthesized report — not five sub-outputs concatenated |

**Recommended (C-06–C-08, 30 pts):**
| ID | Criterion |
|----|-----------|
| C-06 | Exception paths and edge cases identified (>= 2 across report) |
| C-07 | Each finding cites the sub-skill that surfaced it (>= 80%) |
| C-08 | State machine anomalies explicitly called out from trace-state |

**Aspirational (C-09–C-10, 10 pts):**
| ID | Criterion |
|----|-----------|
| C-09 | Test scenario baseline section with >= 3 scenarios linked to findings |
| C-10 | Finding IDs using F-NN pattern for lifecycle traceability |

**Golden threshold**: all of C-01–C-05 pass AND composite >= 80.

The most common failure modes to watch for: silent sub-skill skipping (fails C-01), five separate outputs with no synthesis (fails C-05), findings without severity labels (fails C-03).
