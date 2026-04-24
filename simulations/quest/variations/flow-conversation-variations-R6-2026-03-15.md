Written to `simulations/quest/golden/flow-conversation-variate-R6-2026-03-15.md`.

---

## Round 6 — flow-conversation Variations

**Rubric:** v6 (C-01–C-16, max 135 pts)
**New criterion:** C-16 — Cross-Mechanism Prohibition Convergence

### Variation Map

| Var | Axis | C-13 | C-14 | C-15 | C-12 | C-16 | Predicted |
|-----|------|------|------|------|------|------|-----------|
| V-01 | C-15 only — no register, no foils | FAIL | FAIL | PASS | PASS | FAIL | 120/135 |
| V-02 | C-15 + C-13 — hypothesis + register, no foils | PASS | FAIL | PASS | PASS | FAIL | 125/135 |
| V-03 | C-15 + C-14 — hypothesis + foils, no register | FAIL | PASS | PASS | PASS | FAIL | 125/135 |
| V-04 | C-15 + C-13 + C-14, no phase gates | PASS | PASS | PASS | FAIL | FAIL | 125/135 |
| V-05 | All seven mechanisms | PASS | PASS | PASS | PASS | PASS | 135/135 |

### C-16 structure in V-05

C-16 requires all three prohibition-delivery structures present and non-redundant. V-05 achieves this with three independent prohibition axes:

- **Register zero-points** (concept-level omissions): `"session context is maintained appropriately"` (no variable names), `"Collisions might occur if topics have similar phrasing"` (no predicted node), `"The agent addresses the main scenarios comprehensively"` (no per-node inventory). None of these appear in the foils or exit conditions.

- **Section foils** (structural anti-patterns): `"User greets the agent. Agent identifies intent and fulfills request. Conversation ends normally."` (prose trace instead of table), `"When unrecognized input is received, the agent re-prompts; if retries fail, the session escalates."` (exception path as summary). Neither appears in the register or exit conditions.

- **Exit MAY NOT gates** (completion-state blockers): `"MAY NOT trace the same node sequence as Phase 3 with a different utterance"` (path non-uniqueness), `"MAY NOT use 'possible' or 'unclear' as verdicts"` (specific forbidden words), `"MAY NOT omit a Phase 2 node from the coverage table"` (missing coverage row). None appear in the register or foils.

V-01–V-04 each have at most two active structures. C-16 cannot fire. V-05 is the only variation where all three coexist with non-overlapping content.
