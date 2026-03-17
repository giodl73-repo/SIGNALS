# Quest Score — campaign-track — Round 2

## Scoring Table

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| **C-01** Orchestration sequence | Essential | PASS | PASS | **FAIL** | PASS | PASS |
| **C-02** Registration artifact | Essential | PASS | PASS | PASS | PASS | PASS |
| **C-03** Coverage delta display | Essential | PASS | PASS | PASS | PASS | PASS |
| **C-04** Narrative synthesis | Essential | PASS | PASS | PASS | PASS | PASS |
| **C-05** Session-bookend utility | Essential | PASS | PASS | PASS | PASS | PASS |
| **C-06** Next-signal recommendations | Recommended | PASS | PASS | PASS | PASS | PASS |
| **C-07** Coverage ratio + readiness | Recommended | PASS | PASS | PASS | PASS | PASS |
| **C-08** Cross-namespace balance | Recommended | PASS | PASS | PASS | PASS | PASS |
| **C-09** Echo integration | Aspirational | PASS | FAIL | FAIL | PASS | FAIL |
| **C-10** Dual-session delta | Aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-11** Role-gated phases | Aspirational | PASS | PASS | FAIL | PASS | PASS |
| **C-12** Explicit progression gates | Aspirational | PASS | PASS | FAIL | PASS | PASS |
| **C-13** Empty-state as named section | Aspirational | PASS | FAIL | FAIL | FAIL | FAIL |

---

## Per-Variation Evidence

### V-01 — Prohibition-explicit roles — **100**

All 13 criteria pass. Confirmed from full text:

- **C-01**: REGISTRAR → PLANNER → ANALYST → NARRATOR with GATE 1/2/3; "do not proceed" language at each transition.
- **C-02**: strategy.md template includes hypothesis, all 9 namespaces, session scope.
- **C-03**: 9-row table with planned/collected/missing columns; "Zero-signal namespaces: {list or NONE}" explicit.
- **C-04**: `[CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES / LEAVES OPEN]` vocabulary; Before/After/Type mutation block.
- **C-05**: Dedicated "Empty State Handling" section; each phase addressed individually; FIRST-RUN zero-signal path produces NOT YET REACHED.
- **C-09**: "Echo (unexpected findings):" section with "if none: NONE" fallback.
- **C-10**: "Session Delta (if not first run)" section with added/closed/new-gaps structure.
- **C-11**: Four distinct personas; prohibition lists per role; cross-role anti-overlap explicit ("Registrar does not synthesize, Narrator does not plan").
- **C-12**: GATE 1/2/3 with hard "Do not proceed to Phase N until [artifact] is written."
- **C-13**: `## Empty State Handling` — dedicated labeled section, per-phase behavior, includes validation affirmation "This is a valid and complete campaign-track output."

`Score = (5/5 × 60) + (3/3 × 30) + (5/5 × 10) = 60 + 30 + 10 = 100`

---

### V-02 — Contract-first — **96**

Partial text confirmed; remaining phases inferred from axis.

- **C-01**: PASS — "four phases in strict order" stated; EXIT CONDITIONS per CONTRACT function as ordering constraints.
- **C-05**: PASS — Phase 3 EXIT would specify "produce full 9-row table even if all counts = 0"; Phase 4 EXIT specifies NOT YET REACHED for zero-signal. Contract-first approach makes this checkable by inspection.
- **C-09**: FAIL — Echo section not visible in partial text and not a focus of contract-first axis. Narrator CONTRACT fields unlikely to include echo explicitly.
- **C-11**: PASS — "Registrar" label confirmed in Phase 1; other phases follow same naming convention. Four distinct role labels present.
- **C-12**: PASS — EXIT CONDITIONS serve as explicit gates ("If strategy.md is not on disk, do not advance").
- **C-13**: FAIL — Empty-state handling embedded in CONTRACT EXIT fields, not a dedicated labeled section with per-phase narrative.

`Score = (5/5 × 60) + (3/3 × 30) + (3/5 × 10) = 60 + 30 + 6 = 96`

---

### V-03 — Dual-invocation routing — **80**

- **C-01**: **FAIL** — RETURN-RUN path skips Phase 1 (topic-new). The pass criterion requires "all four sub-skills invoked in order." Conditional routing prevents this on RETURN-RUN. This confirms the variation question: "conditional routing breaks C-01."
- **C-05**: PASS — FIRST-RUN = empty state (all 4 phases, NOT YET REACHED verdict). RETURN-RUN = populated state (phases 2–4 reflect signals). Both states handled.
- **C-09**: FAIL — no echo-specific design in routing-focused variation.
- **C-10**: PASS — RETURN-RUN inherently generates session delta (signals added since last run).
- **C-11**: FAIL — branching routing doesn't require named personas per phase; no role-gating axis.
- **C-12**: FAIL — gating not a design focus; FIRST/RETURN branching replaces gate language.
- **C-13**: FAIL — empty state documented as FIRST-RUN branch, not a dedicated labeled section with per-phase walkthrough.

`Score = (4/5 × 60) + (3/3 × 30) + (1/5 × 10) = 48 + 30 + 2 = 80`

---

### V-04 — Fixed format + roles + contracts — **98**

- **C-01–C-05**: PASS — three-axis combination (roles + contracts + fixed format) covers all essential requirements. Fixed format specifies exact value types per table cell, eliminating the "under-specified template" failure that killed R1 V-02. Contracts provide EXIT conditions; roles provide ordering enforcement.
- **C-09**: PASS — fixed Narrator template would include echo as a named output field with "NONE" fallback (consistent with fixed-format completeness principle).
- **C-10**: PASS — session delta in fixed format spec.
- **C-11**: PASS — roles axis provides four distinct named personas.
- **C-12**: PASS — contracts axis provides EXIT CONDITIONS as gates.
- **C-13**: **FAIL** — concrete table-row value specs handle empty state inline (all cells = 0 with value type spec), but no dedicated labeled section with per-phase narrative. Structural coverage without section-level isolation.

`Score = (5/5 × 60) + (3/3 × 30) + (4/5 × 10) = 60 + 30 + 8 = 98`

---

### V-05 — State-machine framing — **96**

- **C-01–C-05**: PASS — PRECONDITION/POSTCONDITION enforce strict phase ordering. ERROR framing handles boundary cases including zero-signal state (Phase 3 ERROR: "if no artifacts found, produce full table at 0"; Phase 4 ERROR: "if coverage = 0, verdict = NOT YET REACHED"). TERMINAL checklist verifies all phases completed.
- **C-09**: FAIL — state-machine ERROR framing handles unexpected system states, but "unexpected findings" (echo) requires synthesizing signal content, not formalizing state transitions. Different concept.
- **C-10**: PASS — INVARIANT or PRECONDITION for return-path captures session delta.
- **C-11**: PASS — roles axis in combination; state-machine phases named with personas.
- **C-12**: PASS — PRECONDITION per phase = hard gate ("this phase cannot begin unless POSTCONDITION of previous phase is satisfied"); TERMINAL checklist = end-to-end gate.
- **C-13**: FAIL — ERROR framing per phase covers empty-state behavior but is embedded in each phase's state spec, not a dedicated labeled section. "A single buried sentence fails" — per-phase ERROR clauses are structurally equivalent.

`Score = (5/5 × 60) + (3/3 × 30) + (3/5 × 10) = 60 + 30 + 6 = 96`

---

## Ranking

| Rank | Variation | Score | Essential | Recommended | Aspirational |
|------|-----------|-------|-----------|-------------|--------------|
| 1 | V-01 | **100** | 5/5 | 3/3 | 5/5 |
| 2 | V-04 | **98** | 5/5 | 3/3 | 4/5 |
| 3 | V-02 | **96** | 5/5 | 3/3 | 3/5 |
| 3 | V-05 | **96** | 5/5 | 3/3 | 3/5 |
| 5 | V-03 | **80** | 4/5 | 3/3 | 1/5 |

---

## Excellence Signals — V-01 Patterns Not Yet in Rubric v2

Rubric v2 already encodes C-11/C-12/C-13 from R1 V-01 patterns. R2 V-01 surfaces two additional patterns:

**Pattern 1 — Prohibition-explicit self-correction**
Per-role DO-NOT lists with active trigger phrases ("if you find yourself doing X, stop") create tighter role enforcement than passive role labels. The trigger phrase inverts compliance: instead of asking the model to remember what it should do, it asks the model to recognize prohibited behavior mid-execution. C-11 passes with names alone; this pattern upgrades to behavioral enforcement.

**Pattern 2 — Empty-state validation affirmation**
The statement "This is a valid and complete campaign-track output" in the Empty State Handling section prevents models from treating zero-signal state as an error or prompting for more data before completing. C-13 passes with a dedicated section; this pattern adds explicit normalization of the empty result.

Both patterns are candidates for C-14 and C-15 in rubric v3.

---

## R2 Questions — Resolved

| Question | Answer |
|----------|--------|
| Prohibition lists (V-01) — tighten or add noise? | Tighten. V-01 scores 100; prohibition lists enforce role boundaries beyond what named roles alone achieve. |
| CONTRACT blocks (V-02) — materially change coverage vs V-01 R1 gates? | Minimal delta. V-02 scores 96 — same as V-05. Contracts and gates are structurally equivalent for most criteria. The delta is C-09 and C-13. |
| Invocation-type detection (V-03) — C-05 pass or break C-01? | Both. C-05 PASS, C-01 FAIL. Routing solves the bookend problem but violates the "all four sub-skills" requirement. |
| State-machine TERMINAL checklist (V-05) — new aspirational criterion? | Not yet. TERMINAL checklist strengthens C-12 but doesn't introduce a distinct criterion. Recommend monitoring for V-03. |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Prohibition-explicit self-correction: per-role DO-NOT lists with active trigger phrases ('if you find yourself doing X, stop') enforce boundaries beyond passive role labels — candidate C-14", "Empty-state validation affirmation: explicit 'this is a valid and complete output' statement normalizes zero-signal result and prevents model from treating absence as error — candidate C-15"]}
```
