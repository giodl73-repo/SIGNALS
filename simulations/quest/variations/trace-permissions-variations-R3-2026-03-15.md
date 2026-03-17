Written to `simulations/quest/golden/trace-permissions-variate-R3-2026-03-16.md`.

---

## Round 3 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Output format — numbered gap IDs (C-15 single-axis) | Assigning `[G-##]` at discovery and requiring downstream sections to cite by ID makes the gap log a referenceable artifact; re-description instead of citation is a detectable format failure |
| **V-02** | Lifecycle emphasis — entity closure protocol (C-13 single-axis) | A mandatory ENTITY CLOSURE block at the end of every entity section — naming (a) operations reviewed, (b) fields confirmed by name, (c) gaps tallied — forces explicit coverage assertion before the trace can advance |
| **V-03** | Role sequence — per-role sharing verdict spine (C-14 single-axis) | Role-first organization with a mandatory SHARING RULE VERDICT block closing each role section — covering every entity the role touches, clean or conflicted — makes C-14 structurally unavoidable |
| **V-04** | Combined: numbered IDs (C-15) + entity closure (C-13) | The entity closure block is the ID-assignment point: provisional signals accumulate inline during traversal, get promoted to `[G-##]` at closure; the two mechanisms are structurally linked so neither can be satisfied without the other |
| **V-05** | Combined: phrasing register (verdict vocabulary) + inertia framing (OWD + stock baseline as null hypothesis) | Every sharing rule analysis is anchored to the stated Dataverse stock baseline — "BASELINE MATCH" or "DEVIATION `[G-##]`" — forcing a per-role verdict (C-14) and a deviation-based gap ID (C-15) without requiring the model to generate conflict from nothing |

**Key design decisions:**
- V-04 links C-13 and C-15 causally: provisional signal → entity closure → ID assignment → remediation citation. The coupling means you cannot satisfy one without the other.
- V-05's inertia framing is the most architecturally distinct. By declaring the baseline before checking actual configuration, sharing rule silence becomes structurally impossible — every role needs a "matches baseline" or "deviates" verdict.
- V-01 through V-03 are clean single-axis variations; if prior round patterns hold, V-01 (IDs) will be the hardest to satisfy on first run because the downstream citation requirement catches retroactive log-filling.
