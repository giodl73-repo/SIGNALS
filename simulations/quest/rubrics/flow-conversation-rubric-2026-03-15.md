Rubric written to `simulations/quest/rubrics/flow-conversation-rubric-v1-2026-03-15.md`.

**9 criteria across 3 tiers:**

| Tier | Criteria |
|------|----------|
| Essential (60 pts) | C-01 Dialog path traced, C-02 Defect report present (all 4 types), C-03 Intent–response pairing, C-04 Fallback handling shown |
| Recommended (30 pts) | C-05 Session state tracked, C-06 Multi-path coverage, C-07 Topic graph completeness |
| Aspirational (10 pts) | C-08 Copilot Studio vocabulary, C-09 Actionable remediation per defect |

**Design rationale:** The essential tier enforces the minimum contract — a complete dialog trace with both sides of every turn, a defect report that covers all four named defect types, and at least one fallback branch. Without these, the output isn't a conversation flow simulation, it's just notes. The recommended tier pushes toward a full simulation (session state, multiple paths, node inventory). The aspirational tier rewards domain precision and operational value (specific fixes, not generic advice).
