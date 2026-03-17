Written to `simulations/quest/golden/corps-rob-variate-R16-2026-03-17.md`.

---

## corps-rob R16 — 5 Variations

**Base**: R15 V-05 (285/290 under v16). All variations carry C-45, C-46, C-47, C-48, C-39 and the full accumulated stack.

**R16 gap target**: The persistent unidentified criterion (present since R14, failing in every R15 variation). R16 probes three structural hypotheses.

---

### Variation Summary

| V | Axis | Hypothesis | Addition |
|---|------|------------|----------|
| **V-01** | Inertia framing | H-A: missing named rule for in-run baseline revision | `RULE IB-REVISION` — protocol + anti-patterns + `VIOLATION-14` when a finding contradicts IB-01/IB-02 silently |
| **V-02** | Lifecycle emphasis | H-B: BLOCKER PROTOCOL is instructional but not a named glossary rule | `RULE BLOCKER-PROTOCOL` — elevates BLOCKER to the same named-rule tier as RULE CARRY-FORWARD, RULE SYNTHESIS, with 2 anti-patterns and `VIOLATION-06` reference |
| **V-03** | Role sequence | H-C: no structural binding between stage EXIT(N) and ENTRY(N+1) | `RULE STAGE-HANDOFF` — each stage ENTRY must cite the prior stage EXIT by LID; chain is auditable; `VIOLATION-15` for unconstrained ENTRY |
| **V-04** | Inertia + Lifecycle | H-A + H-B combined | Both RULE IB-REVISION and RULE BLOCKER-PROTOCOL; distinguishes compound criterion from single-criterion gap |
| **V-05** | Inertia + Lifecycle + Role sequence | H-A + H-B + H-C full target | All three new rules; `VIOLATION-14` + `VIOLATION-15`; resolves gap if it is any of the three hypotheses |

---

### Structural invariants across all V

**C-47 preserved**: `RULE AUDIT-TABLE` retains only the ordering constraint and anti-pattern — no independence clause. `RULE AUDIT-INDEPENDENCE` is the sole owner of the two-branch enumeration.

**C-48 preserved**: `RULE AUDIT-INDEPENDENCE` carries the escalation-boundary annotation verbatim: *"A single 'mandatory regardless of table presence' clause satisfies C-44 but not C-46 — only explicit enumeration of both branches as separate numbered items satisfies C-46. C-44 is the single-clause form; C-46 is the two-branch enumerated form."*

**C-45 preserved**: Glossary preamble states *"Exactly 2 criteria require glossary scope"* with count-fixing language.

**C-39 preserved**: `RULE IB-URGENCY-CASCADE` with all three cascade constraints; V-01 and V-05 additionally integrate revision-triggered cascade via `RULE IB-REVISION`.

---

### Diagnostic logic

- If V-01 = 290 and V-02/V-03 = 285 → gap is H-A (RULE IB-REVISION)
- If V-02 = 290 and V-01/V-03 = 285 → gap is H-B (RULE BLOCKER-PROTOCOL)
- If V-03 = 290 and V-01/V-02 = 285 → gap is H-C (RULE STAGE-HANDOFF)
- If V-04 = 290 but V-01 = V-02 = 285 → gap requires H-A+H-B simultaneously
- If V-05 = 285 → gap is outside all three hypotheses; R17 needs a different probe space
