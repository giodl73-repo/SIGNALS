Written to `simulations/quest/golden/org-rob-variate-R1-2026-03-16.md`.

---

## org-rob — Prompt Variations R1

Five complete, runnable skill body prompts:

---

### V-01 — Role Sequence: Bottom-Up Escalation
**Axis:** Role sequence
**Hypothesis:** Running teams → pm → tpm → arch-board → leadership → spire forces downstream stages to inherit and compress upstream findings rather than produce independent reviews. Cross-stage coherence (C-06) emerges structurally from the escalation chain.

**Key mechanics:**
- Fixed bottom-up order regardless of `--stage` flags
- Each stage's findings table references parent-stage finding IDs (`TM-NN`, `PM-NN`, `R-NN`)
- Cross-stage synthesis block traces the full escalation chain explicitly
- `tpm` go/no-go block is a labeled top-level element (satisfies C-05)

---

### V-02 — Output Format: Table-First per Stage
**Axis:** Output format
**Hypothesis:** A table-first format — findings as rows with ID/severity/owner/resolution — automatically satisfies C-03, C-04, C-07 without requiring the model to infer what "structured" means. Prose is reserved for verdict rationale only.

**Key mechanics:**
- Every stage uses the same findings table schema; stage-specific columns added per stage (TPM adds `Likelihood`; spire uses a Mission Alignment table)
- Stage verdicts are themselves a one-row table
- Cross-stage summary uses three tables: Escalation Chain, Open Blockers, Cross-Cutting Themes
- Stage prefix system (`LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`) enforces finding traceability

---

### V-03 — Inertia Framing: Status-Quo Challenger Leads
**Axis:** Inertia framing
**Hypothesis:** Making the `inertia-advocate` (from `.craft/roles/signal/inertia-advocate.md`) the first voice in every stage forces each role to answer "why is change better than doing nothing?" before writing findings. Produces role-specific findings grounded in Signal's unique philosophy (C-02) rather than generic governance output.

**Key mechanics:**
- `inertia-advocate.md` loaded first; runs an inertia challenge block at the top of every stage
- Inertia threat level (HIGH/MED/LOW) required at stage open
- Each stage's role must respond to the inertia challenge in at least one finding
- TPM stage adds an "inertia risk" register entry — risk of NOT shipping
- Cross-stage synthesis includes an Inertia Resolution table across all stages

---

### V-04 — Role Sequence + Lifecycle Emphasis (Combination)
**Axes:** Role sequence (top-down governance-first) + Lifecycle emphasis (explicit phase contracts + gate conditions)
**Hypothesis:** Combining top-down order with explicit phase contracts (entry condition / role / findings / exit condition / escalation) forces C-06 (cross-stage coherence) and C-09 (inter-stage blocker detection) to emerge structurally — each stage's exit condition is the next stage's entry condition.

**Key mechanics:**
- Six formal phase contracts with explicit entry/exit conditions
- Each stage escalates named finding IDs to the next stage; receiving stage must respond
- `arch-board` can retroactively invalidate `tpm` go/no-go via inter-stage blocker mechanism
- Cross-stage synthesis shows the full escalation chain as a table: `LDR-NN → TM-NN → PM-NN → R-NN → AB-NN`

---

### V-05 — Phrasing Register + Output Format (Combination)
**Axes:** Phrasing register (conversational imperative, first-person role voice) + Output format (hybrid: numbered prose findings with labeled verdict headers)
**Hypothesis:** Voicing each role in first person using their documented lens items forces role identity into the grammar of every finding (C-02). Hybrid prose+header format keeps output readable while ensuring all four ROB structural elements are present (C-03).

**Key mechanics:**
- Each stage opens with the role's `orientation.frame` as a first-person statement
- `pm.md` and `architect.md` `lens.verify` items are worked through explicitly, one-by-one
- `inertia-advocate` lens surfaced through the PM's required inertia finding
- TPM go/no-go is a `##`-level header — the loudest structural element in the stage
- Cross-stage summary written in "neutral observer" voice, explicitly noting when two roles flagged the same concern

---

**Rubric coverage map:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Stage identity | + | + | + | + | + |
| C-02 Role-loaded perspective | o | o | ++ | o | ++ |
| C-03 ROB format compliance | + | ++ | + | + | + |
| C-04 Actionable findings | + | ++ | + | ++ | + |
| C-05 Explicit go/no-go | + | ++ | ++ | ++ | ++ |
| C-06 Cross-stage coherence | ++ | + | o | ++ | o |
| C-07 Risk register structure | + | ++ | + | ++ | + |
| C-08 Spire cascade | + | ++ | ++ | ++ | + |
| C-09 Inter-stage blockers | + | o | o | ++ | o |
| C-10 Cross-cutting themes | + | + | + | ++ | ++ |

`++` = structural enforcement &nbsp;`+` = natural outcome &nbsp;`o` = possible but not enforced

**Predicted leaderboard:** V-04 > V-02 > V-05 > V-01 > V-03 — V-04's phase contracts structurally enforce the most criteria; V-03's inertia framing is differentiating for C-02 but may sacrifice format compliance.
