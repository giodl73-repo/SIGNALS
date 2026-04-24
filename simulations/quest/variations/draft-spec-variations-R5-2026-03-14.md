Saved to `simulations/quest/rubrics/draft-spec-rubric-v5-variate-R5-2026-03-15.md`.

---

## Axis Map

| Variation | Primary Axis | Hypothesis |
|-----------|-------------|------------|
| V-01 | **Unified Role-and-Source Declaration** | `ROLE INSPECTS artifact TO ACTION before gate` — one element satisfies C-12 + C-14 + C-20 simultaneously; inspection block becomes the gate's natural proof-of-work evidence |
| V-02 | **Output Format (REQUIRES/PRODUCES + INVALID IF)** | A REQUIRES/PRODUCES chain with explicit `INVALID IF` clauses satisfies C-21 as a structural template rule without role-sequence ordering; expected gap: C-12 (roles at phase headers, not inline) |
| V-03 | **Inertia Framing (IG-ID Parallel Namespace)** | Full first-class IG-ID treatment — numbered IDs, per-ID elimination paths, AMPLIFIED threshold, dedicated gate token — satisfies C-22 from a single axis alone |
| V-04 | Unified Declaration + REQUIRES/PRODUCES + Lifecycle | Combined intersection produces `"Role X INSPECTS Source Y REQUIRES [artifact] TO ACTION PRODUCES [token]"` — satisfies C-12, C-14, C-20, C-21 from one compound element; lifecycle BEGIN/END gates make ordering binding |
| V-05 | All four axes | C-22 receives unified-declaration treatment: `PM INSPECTS scout-feasibility AND scout-compliance REQUIRES [both] TO ASSESS each IG-ID PRODUCES [INERTIA-TABLE]` — extends the C-20 pattern to the risk class for full structural parity |

---

## Design Decisions Worth Noting

**Why C-21 appears in V-01 without a formal `INVALID IF` clause**: the V-01 pattern makes the inspection block the gate's named prerequisite by construction — `[PM-CONTRACT-SEAL]` lists the three artifacts it requires. The invalidity condition is embedded in the gate's prerequisite list rather than an explicit "INVALID IF" line. V-02 makes the invalidity declaration explicit as a separate structural rule. The scoring question for C-21 is whether a named-prerequisite list in a gate token satisfies "explicit structural invalidity rule" — that's the primary comparison point between V-01 and V-02.

**V-03 gap prediction**: likely fails C-12 (inline role annotations) and C-20 (unified declaration) — the IG-ID axis alone doesn't generate the combined role+source structural element. The interesting score will be whether C-22 alone materially increases composite over a V-01/V-02 baseline.

**V-04/V-05 combination prediction**: the intersection of `ROLE INSPECTS source` (V-01) and `REQUIRES [artifact]` (V-02) produces `ROLE INSPECTS source REQUIRES [artifact] TO ACTION PRODUCES [token]` — a compound element that is both the inline role annotation and the named REQUIRES declaration in one line. That's the canonical C-20 implementation the rubric describes: a single parseable instruction of the form "Role X inspects Source Y before confirming Z."
