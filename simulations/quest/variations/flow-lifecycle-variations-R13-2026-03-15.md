Written to `simulations/quest/golden/flow-lifecycle-variate-R13-2026-03-15.md`.

---

## flow-lifecycle R13 — Five Variations

**Target criteria:** C-42 (STEP 0A/0B sequential labels), C-43 (Initial Phase field), C-44 (SECONDARY/DERIVED typed escape codes), C-45 (certified Handler R-ID in downstream gate)

**Hypothesis matrix:**

| Variation | C-42 | C-43 | C-44 | C-45 | Axis |
|-----------|:----:|:----:|:----:|:----:|------|
| V-01 | TARGET | TARGET | HOLD | HOLD | Output Format |
| V-02 | HOLD | HOLD | TARGET | HOLD | Phrasing Register |
| V-03 | HOLD | HOLD | HOLD | TARGET | Lifecycle Emphasis |
| V-04 | TARGET | TARGET | TARGET | HOLD | Role Sequence + Output Format |
| V-05 | TARGET | TARGET | TARGET | TARGET | Lifecycle Emphasis + Phrasing Register + Inertia Framing |

---

### Key structural decisions across the five variations:

**V-01 (Output Format)** — C-43 and C-42 via inline column-header placement. The Initial Phase column appears as a defined header cell ("Mandatory; blank is a structural fail") rather than a preamble instruction. The argument: a blank column cell is more visible than a skipped paragraph.

**V-02 (Phrasing Register)** — C-44 via imperative production instructions. "Write SECONDARY:[rationale] for any role outside LT scope — not N/A, not blank. State the specific reason." The argument: the rule is active at the exact moment the author is filling the cell, not in a preamble read once and forgotten.

**V-03 (Lifecycle Emphasis)** — C-45 via phase-granular certification conditioning. The downstream gate is framed as a per-phase closure condition: exception flows in a phase must carry certified Handler R-IDs before that phase's terminals are authored, making certification a rolling obligation rather than a final bulk scan.

**V-04 (Role Sequence + Output Format)** — Combines C-42 + C-43 + C-44. Roles are the first schema section after STEP 0A/0B, pre-certifying exception authority before any phase or state is authored. Both typed escape codes (SECONDARY, DERIVED) appear as column-header definitions in their respective sections.

**V-05 (Lifecycle Emphasis + Phrasing Register + Inertia Framing)** — Full v13 floor. Status-quo process declared up front; incumbent comparison columns run through Phase Index (`Status-Quo Gap`), State Trace (`Incumbent Delta`), Exception Catalog (`As-Is Detection?`), and Bottleneck Register (`Incumbent Workaround`). The inertia framing creates dual-column pressure on the Entry Trigger field — an author filling a DERIVED:rationale row must simultaneously explain the LT combination logic AND the status-quo gap, making generic "N/A" implausible structurally.
