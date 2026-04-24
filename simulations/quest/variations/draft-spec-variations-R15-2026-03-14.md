Written to `simulations/quest/rubrics/draft-spec-rubric-v14-variate-R15-2026-03-15.md`.

---

## Quest Variate — `draft-spec` — Round 15 (Rubric v14)

### Axis Map

| Variation | Primary Axis | Hypothesis | Expected Score |
|-----------|-------------|------------|----------------|
| V-01 | **Output format** — [DD-REGISTER] in Phase 3 Design (DD-ID, Decision, R-ID Coverage, Trade-off, Architect Note; blank R-ID Coverage = structural fail) | DD-register criterion-neutral; C-41/C-42/C-43 baseline satisfied; no extension patterns | 30/35 aspirational |
| V-02 | **Inertia framing** — [STATUS-QUO-SNAPSHOT] as Phase 2 opening block before [IG-REGISTER]; Condition 1 extended to snapshot presence (C-36); structural fail rule co-located (C-37) | STATUS-QUO-SNAPSHOT activates C-36/C-37; C-41/C-42/C-43 satisfied | 32/35 aspirational |
| V-03 | **Role sequence** — Architect co-leads Phase 1 alongside PM; → ROLE: PM + ARCHITECT at Phase 1 entry | C-43 condition (1) requires single-actor Phase 1 marker; V-03 intentionally violates it to surface the embedded ordering assumption | 29/35 aspirational (C-43 = FAIL) |
| V-04 | **Compound: V-01 + V-02 + Phase 1.5** — [DD-REGISTER] + [STATUS-QUO-SNAPSHOT] + Phase 1.5 STRATEGY INERTIA SCOPING + [STRATEGY-SCOPE-SEAL] + dual-token Phase 2 gate + C-40 cross-reference | All eight extension criteria active; DD-register neutral across all | 35/35 aspirational, 175/175 |
| V-05 | **Full synthesis: V-01 + V-02 + V-03 + Phase 1.5** — all of V-04 plus Architect co-leads Phase 1 | C-43 TBD: if → ROLE: PM (lead) + ARCHITECT (consult) satisfies condition (1), 35/35; if not, 34/35. Sets up C-43 boundary clarification for R16. | 34–35/35 aspirational |

---

### Key R15 Discovery Questions

1. **DD-register (V-01, V-04, V-05)**: Does the structured Design section trigger any unexpected interaction with C-05 (five guided sections in prescribed order) or C-27 (actor-directive form)? Expected: no — but the completeness rule (blank R-ID Coverage = structural fail) is a new structural rule category not yet in the rubric.

2. **STATUS-QUO-SNAPSHOT before [IG-REGISTER] (V-02, V-04, V-05)**: Does placing the snapshot block as Phase 2's opening element affect [INERTIA-ANALYZED] Condition 1 evaluation order? The condition names all three blocks — does ordering matter?

3. **C-43 boundary (V-03, V-05)**: Does → ROLE: PM (lead) + ARCHITECT (consult) satisfy C-43 condition (1), which specifies a "single-actor marker" at Phase 1? This is the primary rubric boundary test for R15. If it satisfies, V-05 is 35/35 and C-43's wording needs tightening for R16.
