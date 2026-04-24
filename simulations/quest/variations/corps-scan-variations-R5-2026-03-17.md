Written to `simulations/quest/golden/corps-scan-variate-R5-2026-03-17.md`.

---

## R5 Variate Summary — corps-scan

**5 complete variations targeting v5 rubric (220 pts, 22 criteria)**

The three new invariants across all variations:

| Criterion | How each variation addresses it |
|-----------|--------------------------------|
| **C-20** (amend anti-pattern named) | Explicit `"'Let me know if you want changes' does not satisfy this phase"` inside every amend directive |
| **C-21** (gate category labels) | `GATE 1 (Structural Ordering)` and `GATE 2 (Semantic Traceability)` in every variation |
| **C-22** (IVR on ALL structural constraints) | Each variation takes a different structural approach to achieving full IVR coverage |

**Variation axes:**

| Variation | Single-axis | Structural approach to C-22 |
|-----------|-------------|------------------------------|
| **V-01** | Role sequence | IVR triples declared per-role: ROLE 1 owns Phase 1+4, ROLE 2 owns Phase 2, ROLE 3 owns Phase 3 |
| **V-02** | Output format | SPEC-object architecture — every constraint is a named SPEC; no prose-directive fallback possible |
| **V-03** | Phrasing register | Formal REQ-N.N numbered requirements — each requirement is an IVR triple by construction |
| **V-04** | Role sequence + output format | Dedicated SPEC Auditor role (ROLE 3) whose sole deliverable is the all-phases SPEC table |
| **V-05** | Lifecycle emphasis + phrasing register | Entry/exit IVR specs per phase — every boundary is a triple; intra-phase constraints are triples too |

**IVR triple counts by variation (C-22 evidence):**
- V-01: 14 labeled IVR triples (4+4+5+1 across roles)
- V-02: 12 SPEC objects (all phases covered)
- V-03: 11 REQUIREMENTs with IVR sub-clauses
- V-04: 9 IVR (ROLE 1/2 headers) + 7-row SPEC table (all phases)
- V-05: 15 IVR triples (entry+intra+exit across 4 phases)
