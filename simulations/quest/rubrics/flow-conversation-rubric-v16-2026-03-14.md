Written to `simulations/quest/rubrics/flow-conversation-rubric-v16-2026-03-15.md`.

---

**Three new criteria extracted from Round 16:**

| ID | Criterion | Axis | Requires | Exclusive to |
|----|-----------|------|----------|--------------|
| C-69 | WRONG_SCHEMA sweep result embedded in CONTRACT_AUDIT_GATE_HONORED (not a parallel block the gate ignores) | Gate-precondition axis — C-67's sweep becomes a gate field | C-67 PASS | V-05 |
| C-70 | Role instructions reference LIFECYCLE_PROTOCOL section by name; no inline re-declaration of any HANDOFF_TO/Received pair outside the dedicated section | Single-source-of-truth axis — C-66's dedicated section becomes the sole authoritative location | C-66 PASS | V-01, V-04, V-05 |
| C-71 | Parenthetical verification status embedded in CONTRACT_AUDIT_GATE_HONORED (parallel to C-69 on the parenthetical axis) | Gate-precondition axis — C-68's standalone check propagates into the gate assertion | C-68 PASS | V-05 |

**Chain structure:**
- C-69 → C-67 → C-64: manifest detection → Phase 6-A finding → gate precondition
- C-70 → C-66 → C-63: token presence → dedicated section → single source of truth
- C-71 → C-68 → C-65: row-count contract → Phase 6-A finding → gate precondition

**Scoring:** Aspirational tier 141 → 147 pts. Max 234 → **240**.
