Written to `simulations/quest/golden/prove-program-variate-R7-2026-03-15.md`.

---

# prove-program -- Variations R7 (V-01 through V-05)

**R7 context**: R6 confirmed 160/160 across 4-role model, numbered-step format, conversational register, lifecycle+inertia combined, and triple combined. v6 rubric unchanged.

**R7 axes — new territory:**

| # | Label | Axis | Description |
|---|-------|------|-------------|
| V-01 | 2-role model | Role sequence | Consolidate FRAMER/PLANNER/RUNNER/EVALUATOR into ARCHITECT + EXECUTOR. GATE-1 becomes the only inter-role boundary, making it the sole architectural checkpoint. |
| V-02 | Pure prose | Output format | Zero tables. All structure (plan, findings, principles, gates, audit) expressed as labeled prose paragraphs. No markdown tables anywhere. |
| V-03 | Formal spec register | Phrasing register | RFC 2119 normative language throughout: MUST, SHALL, MUST NOT, PROHIBITED. Executor is "the executor" (third person). Gates are specification constraints, not procedural instructions. |
| V-04 | Prose + gate density | Combined (format + lifecycle) | No tables + every phase transition has a named gate with a prose FAIL block. Pulls prose format and gate density against each other. |
| V-05 | 3-role + formal + inertia | Combined (role + register + inertia) | STRATEGIST / INVESTIGATOR / JUDGE in RFC language. prove-topic appears as a named benchmark with a capability map at every role boundary, not only Phase 0. |

**Structural invariants preserved in all 5 variations:**
- C-20: Atomic conjunction gate (Condition A AND Condition B, two-row boolean, single PASS line) before experiment plan
- C-21: GATE-CAL before synthesis with named FAIL condition ("all findings rated HIGH")
- C-22: Per-block citation contract in each consumer experiment's INPUT section, not a global preamble
- C-18: >=2 named gates at phase transitions
- C-19: >=3 inline FAIL conditions
- C-08: prove-topic named and its specific limitation identified

**Prediction**: All five score 160/160. C-20/C-21/C-22 are format-agnostic and register-agnostic structural properties.
