Saved to `simulations/quest/golden/org-chart-variate-R1-2026-03-15.md`.

---

# org-chart Variate — Round 1

## Variation Map

| V | Axis | Key Change | Hypothesis |
|---|------|------------|------------|
| V-01 | inertia-framing | Inertia gate with a VERDICT field (CAN-OPERATE-FLAT / STRUCTURE-WARRANTED) that blocks org-box writing | Named VERDICT prevents C-01 from collapsing into a generic intro paragraph |
| V-02 | output-format | Four section scaffolds (INERTIA-ASSESSMENT, ASCII-ORG-BOX, HEADCOUNT-TABLE, RHYTHM-TABLE) as fill-in templates | Pre-specified slots make section omission structurally impossible; protects C-07, C-04, C-05 |
| V-03 | role-sequence | `.craft/roles/` read is Step 1; produces a ROLES-LOADED list that all subsequent sections must reference by name | Forces C-03 from the start rather than as a retrofit; if roles exist they anchor the design |
| V-04 | phrasing-register + inertia-framing | Fully imperative DO/DO NOT register combined with the VERDICT gate | Hard prohibitions block the three most common essential failures: skipping inertia, flat list instead of hierarchy, rhythm table with only ROB |
| V-05 | lifecycle-emphasis + output-format | Five-phase sequence (READ-ROLES → ASSESS-INERTIA → DESIGN-STRUCTURE → DOCUMENT-RHYTHMS → CHARTER-COMMITTEES) with per-phase output contracts and a charter-element checklist | Phase gating prevents later phases from executing before earlier ones complete; the charter checklist (purpose + membership + decides/escalates) directly targets C-06 and C-08 |

---

**Design notes:**

- **C-01 is the hardest to protect** — V-01 and V-04 both address it directly; V-05 addresses it via phase gating. All three approaches should be scored to see which formulation produces the most substantive inertia sections.
- **C-03 context-sensitivity** — V-03 makes the `.craft/roles/` read explicit and produces an artifact (ROLES-LOADED table) that is visible in the output, making it easy for the evaluator to check the run context. The `.craft/roles/signal/` directory has `pm.md`, `architect.md`, and `inertia-advocate.md` — these should appear by name in any run against the current repo.
- **C-05 floor** — V-04 includes an explicit prohibition against a single-ROB rhythm table. V-02 and V-05 each have minimum row requirements built into the template slot.
- **C-06 + C-08 coverage** — V-05 is the only variation with an explicit charter checklist and a Decides/Escalates column in the headcount table. If V-05 scores higher on recommended criteria, the checklist + split-column approach is the mechanism.
