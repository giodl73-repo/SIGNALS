Saved to `simulations/quest/rubrics/trace-migration-variations-R5-2026-03-14.md`.

---

## Round 5 Variations — trace-migration

Five complete prompts targeting the four new v5 criteria (C-19–C-22) while preserving all prior 140/140 structure.

---

### Variation Summary

| V | Axis | Key structural choices |
|---|------|----------------------|
| **V-01** | Role sequence (Ops→Finance→Commerce) | 7-gate Phase A chain; C-22 example in Q5 domain section |
| **V-02** | Output format (labeled prose blocks) | Replaces tables with prose paragraphs; C-22 example integrates as narrative |
| **V-03** | Lifecycle emphasis (5-gate two-phase) | PARSE→TRACE→DOMAIN→OPERATIONAL→VERIFY + Phase B; fixes R4 V-03's C-05 failure |
| **V-04** | Role sequence + phrasing register (Finance-first, terse imperative) | "FIND. CLASSIFY. GATE." format; dollar threshold mandatory before gate opens |
| **V-05** | Lifecycle + phrasing register + inertia framing (conversational) | Scenario questions + "status-quo cost" framing + 7-gate chain including B2 and B3 sub-gates |

---

### How Each Variation Closes the v5 Gaps

**C-19 (per-section citation repetition):** All five variations repeat `"Step N from Q1"` (or equivalent) inside every question or prose section body — not only in a global preamble. This is the key structural fix versus R4 variations where citation instructions were sometimes global-only.

**C-20 (domain header completion constraint):** Every variation's domain section header carries an explicit forward-reference naming the downstream section it must precede — e.g., `POSITIONED BEFORE Q7 VERIFY — complete before writing Q7`. The instruction is executable, not merely positional.

**C-21 (complete phase gate chain):** Every phase transition has a named `(BINARY FIELD): OPEN / BLOCKED` gate:
- V-01/V-04: 7 gates (one per Q-to-Q transition + VERDICT in Phase B)
- V-02: Same 7 gates in prose format
- V-03: 6 gates (PARSE→TRACE→DOMAIN→OPERATIONAL→VERIFY→VERDICT)
- V-05: 7+ gates, including B2→B3 (DOMAIN SYNTHESIS GATE) and B3→B4 (VERIFY COMPLETION GATE) — every Phase B sub-phase transition is also gated

**C-22 (pre-seeded inline domain example):** Every variation seeds the same worked example in the domain section as model output text — `Step 3 from Q1: transactions.payment_amount decimal(19,4)→decimal(10,2), charges over $99,999,999.99 silently capped` — not as an instruction to the reader.

---

### Predicted Differentiators at Scoring

**V-03** is the cleanest C-21 architecture (5 explicit lifecycle phase headers, each naming its prerequisite gate). No ambiguity about what counts as a "phase transition."

**V-05** has the deepest C-21 coverage (gates inside Phase B sub-phases), but the question is whether B-sections qualify as "phase transitions" under the rubric. The DOMAIN SYNTHESIS GATE and VERIFY COMPLETION GATE add structural value regardless.

**V-02** is the first prose-format two-phase variation in the series — it tests whether C-13/C-14 binary fields survive the format change, and whether C-19 per-section citation is as visible in prose as in question headers.

**V-04**'s terse imperative register is the most distinct register variation yet, and is the only variation where Finance precedes Commerce before Operations — likely maximizing C-08 precision-loss specificity.
