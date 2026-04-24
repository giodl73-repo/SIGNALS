Written to `simulations/quest/golden/trace-permissions-variate-R4-2026-03-16.md`.

---

## Round 4 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Output format — gap-state-neutral entity closure block (C-16 single-axis) | The `Gaps logged` field in the ENTITY CLOSURE template takes `G-## list` or `NONE` — never blank — so the format cannot branch on gap state. The conditional-closure failure mode (closure on clean entities only) is architecturally impossible when the template is identical for both states. |
| **V-02** | Role sequence — Write-capable role escalation vector spine (C-17 single-axis) | A mandatory five-row vector table per Write-capable role, where every row requires a verdict cell, makes NOT POSSIBLE omissions visible as blank cells. The table format is the enforcement: exhaustiveness is auditable from the output structure. |
| **V-03** | Phrasing register — formal security audit certification mode | Audit convention requires explicit "No finding — confirmed by reviewing..." statements as a matter of format, independently of what the model finds. Hypothesis: the register itself produces C-16 (section verdicts on all entities) and C-17 (No finding verdicts per vector) without additional structural enforcement. |
| **V-04** | Combined: gap-state-neutral closure (C-16) + Write-capable role vector spine (C-17) | Direct stack of V-01 and V-02 mechanics. The two structures are non-overlapping: the closure block fires at entity-section boundaries; the vector table fires in the escalation phase organized by role. |
| **V-05** | Combined: lifecycle emphasis (entity-gated phases with clearance gates) + inertia framing (named design assumptions drive gap detection) | Gating each entity as a clearable phase enforces C-16 via lifecycle rather than format: a phase that has not been cleared cannot be left behind. Inertia framing enforces C-17 indirectly: each escalation vector must be linked to an assumption, making unvoted vectors produce an irreconcilable assumption in the final verdict table. |

---

**Key structural innovations per variation:**

- **V-01:** The ENTITY CLOSURE block's `Gaps logged` field is gap-state-neutral — `G-01, G-03` or `NONE`, never absent or blank. Closure on a gap-containing entity names the gaps by ID without re-describing them.

- **V-02:** Escalation phase is role-first. Each Write-capable role owns a five-row vector table. NOT POSSIBLE cells require naming the specific closing mechanism (e.g., "sharing rule creation requires System Customizer privilege — this role does not hold it"). POSSIBLE cells require a Gap Log entry.

- **V-03:** Formal audit register replaces gap log with Findings Register (F-## numbering). Section Verdict blocks on every entity have a `Findings` field that takes a list or the word NONE — silence is non-conforming. Escalation "No finding" verdicts require a basis statement.

- **V-04:** Combines V-01's ENTITY CLOSURE template (identical on all entities, gap-state-neutral `Gaps logged` field) with V-02's five-vector escalation table (per Write-capable role, verdict required per row, NOT POSSIBLE must name the closing mechanism).

- **V-05:** Entity clearance gates introduce `CLEARED` vs `CLEARED: PENDING [G-##]` status — an entity with open gaps cannot silently advance. Assumption-violation framing means every escalation vector must be linked to an A-##, making an unvoted vector produce an irreconcilable assumption in the Phase 3 verdict table.
