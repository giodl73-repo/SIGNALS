Written to `simulations/quest/golden/corps-rob-variate-R1-2026-03-17.md`.

---

## Variate R1 — corps-rob (rubric v1, 2026-03-17)

### Variation Axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence — bottom-up | Operational stages before leadership; leadership synthesizes rather than frames |
| V-02 | Output format — compact single-line | Minimum-footprint format tests whether C-02 role specificity survives compression |
| V-03 | Phrasing register — workshop facilitation | Second-person active, present-tense; model writes from inside the reviewer role |
| V-04 | Inertia framing + lifecycle emphasis | Inertia anchor + per-stage handoff packets; C-08 and C-09 generated structurally |
| V-05 | Per-stage scorecard + escalation ledger | Self-evaluation scorecard per stage + thread-level ledger at document end |

---

### V-01 — Role Sequence: Bottom-Up

**Axis**: Role sequence
**Hypothesis**: Running teams→pm→tpm→arch-board before leadership inverts the information flow. Leadership's exec briefing sees what the organization already surfaced, forcing at least one leadership finding to confirm or contradict an upstream finding by ID. Predicted gain: natural C-08 cross-stage coherence in the leadership stage. Predicted risk: leadership reads reactive rather than strategic.

**Stage order**: `teams → pm → tpm → arch-board → leadership → exec-office`

Key structural rules:
- Leadership stage must reference at least one upstream finding by ID
- Exec-office stage sees a fully stress-tested picture before tracing the mission cascade
- All six canonical stage labels required (C-01); no stage merged or skipped

---

### V-02 — Output Format: Compact Single-Line

**Axis**: Output format
**Hypothesis**: Maximum-density single-line findings (`F-01 HIGH [concern] | Owner: [role] | Resolution: [action]`) make every structural element machine-verifiable and eliminate format failures. Predicted failure mode: findings compress to category labels, losing role-loaded specificity (C-02). Predicted benefit: C-03, C-04, C-05 structurally guaranteed.

Key structural rules:
- Stage header = single line: `## Stage: [name] | ROLE: [name] — [lens]`
- Findings = single-line pipe-delimited entries
- TPM additions: `RISK REGISTER:` label followed by `R-01 [HIGH/HIGH] [risk] | Mitigation: [action]` per row; `GO/NO-GO:` as a standalone labeled line
- Exec-office additions: `MISSION CASCADE:` label followed by `[mission] → [program] → [topic] | ALIGNED/PARTIAL/GAP`
- Cross-stage inline references appended to the finding line that references them

---

### V-03 — Phrasing Register: Workshop Facilitation

**Axis**: Phrasing register
**Hypothesis**: Second-person active, present-tense framing ("you are the facilitator… let them notice what they notice") activates persona orientation more organically than procedural ENFORCE directives. Model writes the review from inside the moment. Predicted gain: richer C-02 role-loaded voice. Predicted risk: persona voice crowds out structural markers, creating C-03 format failures.

Key structural rules:
- No procedural numbered steps in the prompt — narrative description of what each stage does
- Persona orientation described in natural language, not a field to fill in
- TPM go/no-go rule stated as "the call is labeled and top-level — not hidden in a paragraph"
- Exec-office rule stated as "name the mission — not 'strategic priorities'"

---

### V-04 — Inertia Framing + Lifecycle Emphasis

**Axes**: Inertia framing + lifecycle emphasis
**Hypothesis**: A permanent Inertia Anchor (what this topic displaces, what the displacement costs) combined with per-stage INERTIA CHECK lines and explicit HANDOFF PACKET at stage close produces two structural benefits: (1) every stage finding is grounded in status-quo pressure from that role's perspective (C-02 enrichment), (2) the handoff packet forces a look-back generating C-08 cross-stage references without unprompted recall. BLOCKER field in handoff packet directly surfaces C-09.

Key structural rules:
- Inertia Anchor block before Stage 1 (INERTIA + DISPLACEMENT COST)
- Stage open includes INERTIA CHECK line
- Stage close includes HANDOFF PACKET (PASSING TO NEXT STAGE + BLOCKER: YES/NO)
- End-of-run ROB Summary: INERTIA STATUS, BLOCKERS RAISED, OPEN HANDOFFS

---

### V-05 — Per-Stage Scorecard + Escalation Ledger

**Axes**: Output format (scorecard) + cross-stage coherence (escalation ledger)
**Hypothesis**: A 4-dimension scorecard at stage close (role specificity / finding depth / severity spread / resolution quality, rated 1-3) forces the model to evaluate its own stage output before moving on, surfacing self-correction opportunities. An Escalation Ledger at document end collects all finding threads in one table, making C-08 (cross-stage coherence) and C-10 (cross-cutting theme elevation) structurally impossible to miss. Predicted risk: scorecard is self-referential, distracting from finding quality.

Key structural rules:
- Stage Scorecard table after every stage verdict (4 dimensions, 1-3 scale)
- Escalation Ledger after all stages: thread ID, concern, stages involved, pattern (escalating/stable/mixed), action
- Thread entries must cross-reference specific finding IDs across stages
- Arch-board specificity requirement: named interface/contract/schema, not "tight coupling"
