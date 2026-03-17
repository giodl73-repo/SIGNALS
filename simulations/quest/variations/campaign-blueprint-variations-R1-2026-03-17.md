Written to `simulations/quest/golden/campaign-blueprint-variate-R1-2026-03-17.md`.

---

## campaign-blueprint Variations — Round 1

Five complete, runnable skill body prompts for `campaign-blueprint` against rubric v1.

---

### Variation Axes

| Axis | Label | Hypothesis |
|------|-------|-----------|
| A | Inertia-first framing | Forces C-06 (inertia baseline in all 3 artifacts) near-automatic; sharpens do-nothing option (C-03) |
| B | Contract matrix first | Forces C-09 (contract declared before execution) and prevents C-05 failures (cross-artifact contradiction) |
| C | PM-first role sequence | Improves audience resonance (C-04) and inertia framing (C-06); risk is spec technical depth (C-02) |
| D | Conversational register | Surfaces gaps naturally (C-08); risk is missing required structural sections |
| E | Full combination A+B+C+scout gate | Maximizes composite score across all rubric bands |

---

### V-01 — Axis A: Inertia-First Framing

Opens with a mandatory `INERTIA BASELINE` block (`Today / Cost / Do-nothing trajectory`) before any artifact. The baseline is named and carried forward by reference into all three artifacts. Option A in the proposal must explicitly quantify what inertia costs continue. Each pitch version must state what changes for that audience specifically.

**Key structural move**: C-06 cannot fail because the baseline is pre-declared and the instructions explicitly require all three artifacts to reference it. C-03 is strengthened because the do-nothing option has a specific template to fill.

---

### V-02 — Axis B: Contract Matrix First

Opens with the READ/WRITE/PRESERVE/CARRIES FORWARD table printed before Artifact 1. Each artifact begins with a dependency check: "Reading [prior artifact]. Feature name: [X]. Constraints carried forward: [list]." Artifacts end with structured tags `[SPEC WRITTEN]`, `[PROPOSAL WRITTEN — Option X recommended]`, `[PITCH WRITTEN]`.

**Key structural move**: C-09 cannot fail because the table is printed in output before execution. C-05 is mechanically enforced by the dependency check at the top of each artifact.

---

### V-03 — Axis C: PM-First Role Sequence

PM leads all three artifacts. Architect advises on spec (DESIGN and CONSTRAINTS only). Strategy advises on pitch (per-audience framing). PM makes the recommendation in the proposal with Architect sign-off on feasibility. Each role handoff is explicit and printed.

**Key structural move**: Inertia framing is stronger because PM is inherently user-outcome focused. Risk: C-02 (spec technical depth) depends on the PM explicitly routing DESIGN and CONSTRAINTS to the Architect before finalizing.

---

### V-04 — Axis D: Conversational Register

Questions replace imperatives: "What problem are we solving?" becomes PURPOSE; "What must the feature do?" becomes REQUIREMENTS; "What don't we know yet?" becomes OPEN QUESTIONS. Scout scan is framed as "check whether there are existing signals" rather than a gate.

**Key structural move**: C-08 is likely to score higher because the question framing ("what don't we know yet?") is more likely to surface authentic gaps than a command to "list open questions." Risk: the five spec sections may be weaker because they emerge from prose questions rather than labeled section requirements.

---

### V-05 — Combined: Inertia + Contract Matrix + Scout Gate + Role Handoffs

Phase 0 runs three steps in sequence: (0a) scout gate with per-signal routing table, (0b) inertia baseline, (0c) contract matrix. Each artifact begins with an explicit dependency check and ends with a role handoff statement. PM consistency check at Artifact 3 before writing ends.

**Key structural move**: This is the maximal-coverage variation. C-06 (inertia), C-07 (scout integration), C-09 (contract matrix), and C-05 (sequence integrity) are all near-automatic. The tradeoff is prompt length — a longer prompt has higher setup overhead but lower per-criterion failure risk.

---

**Scoring prediction** (against rubric v1):

| Variant | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Predicted composite |
|---------|------|------|------|------|------|------|------|------|------|------|---------------------|
| V-01 | FULL | FULL | FULL | FULL | FULL | FULL | PARTIAL | PARTIAL | NO | FULL | ~83 |
| V-02 | FULL | FULL | FULL | FULL | FULL | PARTIAL | PARTIAL | PARTIAL | FULL | PARTIAL | ~82 |
| V-03 | FULL | PARTIAL | FULL | FULL | FULL | FULL | FULL | FULL | NO | PARTIAL | ~80 |
| V-04 | FULL | PARTIAL | FULL | FULL | FULL | FULL | PARTIAL | FULL | NO | FULL | ~79 |
| V-05 | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL | ~100 |

V-05 is predicted golden if the model follows all phases. The main failure mode to watch: does Phase 0 output actually appear before Artifact 1, or does the model collapse it silently?
