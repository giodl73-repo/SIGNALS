---

## crew-check — Variate R4

Five complete prompt bodies targeting the two v4 additions (C-17 and C-18) over the R3 floor (C-11 through C-16 present in all).

| Variation | Axis | Primary targets |
|-----------|------|----------------|
| **V-01** | Named halt IDs as four-position bindings | C-17 |
| **V-02** | Structured gate-audit output | C-18 |
| **V-03** | Self-routing halt messages | C-17 variant |
| **V-04** | Named halt IDs + structured gate-audit | C-17 + C-18 |
| **V-05** | Full v4 integration + priority summary + audit-as-AMEND-menu | C-17 + C-18 + all R3 |

**Key design decisions:**

- **V-01** makes halt IDs first-class handles in four independent positions: registry definition, gate headers (`GATE 1 [G1]`), error messages (verbatim), and AMEND routing keys (`--amend rerun:G4-{role}`, `--amend reload:G1`). Sub-gate names go hierarchical: G4a, G4b, G4c, G4d encode position, not just role.

- **V-02** defines the exact `--amend halts` output format — a table with Gate ID, gate name, message triggered, and resolution step — and adds `--amend halts:{id}` for focused lookup. Defining the format forces tracking throughout execution, not just on demand.

- **V-03** embeds the re-entry command inside every halt message: `HALT [G4a-pm]: Lens anchor absent. → To continue: /crew-check [artifact] --amend rerun:pm`. The halt IS the fix instruction. Halt IDs are still stable (C-17 floor), but the primary innovation is the recovery flow.

- **V-04** explicitly couples the two criteria: four-position named IDs (C-17) cross-referenced by the structured audit output (C-18). Audit resolution steps reference the same gate IDs the model already saw in headers and error messages — three independent evidence trails per failure.

- **V-05** adds self-routing halt messages (V-03 pattern), priority summary tier between matrix and synthesis (R3 V-05 pattern), and audit-as-AMEND-menu (each audit entry includes a ready-to-paste re-entry command). The full claim: any halt leaves the user holding a structured action list, not a diagnostic puzzle.
ties active. Audit block includes ready-to-paste re-entry commands per fired gate, making it executable, not just informational. Priority summary between matrix and synthesis (R3 V-05 pattern). The full claim: any halt leaves the user with a structured action list, not a diagnostic puzzle. |

**Axes not explored in R4** (covered in R1–R3): role sequence, output format variation
(prose/list), lifecycle emphasis, phrasing register (coaching/interrogative/SHALL/formal),
inertia framing, phase-gated lifecycle, severity-sorted as primary axis, interrogative
diagnostic, readiness-gate as primary axis, hard-halt as primary axis.
