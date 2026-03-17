Written to `simulations/quest/golden/scout-size-variate-R6-2026-03-17.md`.

---

## Round 6 — scout-size Prompt Variations

**R6 axes** (targeting v6 rubric — C-22 and C-23):

| ID | Axis | C-21 | C-22 | C-20 | C-23 | Expected Score |
|----|------|------|------|------|------|----------------|
| **V-01** | Synthesis named chain | PASS | PASS | FAIL | FAIL | 98.67 |
| **V-02** | Navigational guards | FAIL | FAIL | PASS | PASS | 98.67 |
| **V-03** | Minimal combination | PASS | PASS | PASS | PASS | **100** |
| **V-04** | Full integration + 23-criterion self-check | PASS | PASS | PASS | PASS | **100** |
| **V-05** | Dual enforcement + structural definitions | PASS | PASS | PASS | PASS | **100** |

**Key mechanisms added in R6:**

**C-22 (verdict close template)**: The synthesis templates now mechanically enforce the gate label at both ends. The verdict close is no longer freeform — each template begins `"The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed/revised/partially revised..."`. This makes the gate label structurally required in what the model writes, not just in the instruction preamble. The disqualifying form `"my earlier estimate was confirmed"` is explicitly named in V-04/V-05.

**C-23 (navigational redirect)**: The distinction is dead-end vs. navigational. `"Do not include scope exclusions here"` is a dead end — it closes a door. `"Scope was resolved in PRE-FLIGHT GATE, not in analysis steps"` is a navigational redirect — it closes the door AND points to the room. Every adjacent section in V-03–V-05 uses the redirect form for both canonical field types (scope exclusions → PRE-FLIGHT GATE, unknowns → OPEN UNKNOWNS).

**V-03 is the new minimum prompt** for 100/100 on v6. **V-05 is the highest-reliability prompt** — the C-22 and C-23 self-check items name the exact disqualifying conditions, making compliance self-auditable before writing.
