**trace-component R8 — 5 variations written.**

---

## Variation Summary

| V# | Axis | Primary C-27/C-28/C-29 Mechanism | Hypothesis |
|----|------|-----------------------------------|------------|
| **V-01** | Output format (schema tables) | Mutation count field + direction column per-row + T-ID completeness rule | Schema shape prevents elision better than instruction memory |
| **V-02** | Lifecycle emphasis (phase gates) | Blocking exit conditions — each phase cannot close until C-27/C-28/C-29 requirements met | Exit gates are softer than schema fields but clearer than prose instructions |
| **V-03** | Phrasing register (formal/technical) | Instruction-driven, no structural enforcement | Technical precision helps straightforward cases; zero-mutation and per-hop gaps expected |
| **V-04** | Role sequence (developer + auditor) | Auditor TABLE 2.0 compliance check explicitly verifies all three new criteria | Second-pass verification catches what developer role misses; gaps flagged not prevented |
| **V-05** | Inertia framing + output format | `↔ inert pass-through` direction makes per-hop annotation natural; N+M count makes zero-mutation explicit; T-ID completeness enforced by change/inertia symmetry | Symmetric framing adds a structural dimension V-01 lacks — "what held inert" is a required output, not an omission |

---

**Key R8 design decisions:**

- **V-01** is the direct evolution of R7's winning V-01 — C-27/C-28/C-29 were already in its schema, but now they're named requirements.
- **V-02** turns them into phase exit conditions — blocking gates vs. column shape.
- **V-03** is the control — no structural enforcement, tests whether register alone holds.
- **V-04** introduces a second role whose explicit job is to audit C-27/C-28/C-29 compliance.
- **V-05** is the novel axis — inertia framing makes "what didn't change" a first-class output, which structurally prevents the silence patterns that C-27/C-28/C-29 target through a different mechanism than tables alone.

Predicted ranking: V-01 ≥ V-05 > V-04 ≥ V-02 >> V-03. V-05's inertia framing is the hypothesis to test — it addresses the same structural gaps through a different frame that may score better on the C-09–C-23 aspirational criteria where V-01 had ~4-point gaps.
