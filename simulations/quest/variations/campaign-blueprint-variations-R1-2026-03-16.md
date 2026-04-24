---

## campaign-blueprint — V-01 through V-05

Written to `simulations/quest/golden/campaign-blueprint-variate-R1-2026-03-16.md`.

---

### Variation summary

| ID | Axis | Core hypothesis |
|----|------|-----------------|
| **V-01** | Role sequence | Front-load a campaign-level Strategy brief — writes a 4-line shared contract before any sub-skill runs, preventing topic drift (C-03 risk) |
| **V-02** | Output format | Tabular field contract per option and a summary table at close — harder to accidentally drop a required field than in prose (C-05 risk) |
| **V-03** | Lifecycle emphasis | Explicit `SETUP / EXECUTE / FINDINGS / AMEND` phases with a hard `GATE:` between each artifact — prevents out-of-order contamination (C-04 risk) |
| **V-04** | Register + inertia | Conversational imperative register + "do-nothing is a real option with real cost" foregrounded at campaign open — anchors every "why it matters" to the inertia baseline instead of feature enthusiasm |
| **V-05** | Full integration | Combines all four axes: role assignment per artifact, tabular format for proposal, gated lifecycle phases, conversational register, and a persistent inertia thread through all three artifacts |

---

### Design notes for scoring

- **C-01/C-02 (all artifacts present, correct paths)** — V-02 and V-05 are the strongest here because the table at campaign close makes a missing artifact visually obvious.
- **C-03 (consistent topic identity)** — V-01 is the targeted fix; the 4-line brief is the shared contract.
- **C-04 (execution order)** — V-03 is the targeted fix; the `GATE:` keyword makes the ordering unambiguous.
- **C-05 (sub-artifact structure)** — V-02 is the targeted fix; required table fields can't be quietly omitted.
- **C-09 (narrative arc, no content duplication)** — V-04 and V-05 address this by grounding each artifact's conviction in inertia cost rather than restating the spec.
