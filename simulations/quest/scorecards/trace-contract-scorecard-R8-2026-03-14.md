structurally weaker than the other.

**2. Role separation declared "not operationally optional."**
V-05 is the only variation to use this exact framing: `"Role separation is structurally enforced — it is not operationally optional."` This closes an ambiguity present in every prior round: a well-structured template with role assignments can still be run by a single agent who substitutes both roles. The "not operationally optional" declaration makes the role requirement a stated constraint, not a description of recommended practice.

**3. Inertia risk explanations precede each contamination gate.**
Each phase in V-05 opens with the specific inertia risk that phase closes — scope anchoring, value anchoring, residual contamination. This makes contamination barriers explanatorily coherent: an agent cannot skip the barrier without first encountering the reason it exists. Reduces bypass risk for C-23/C-30/C-31 compared to variations where gate items appear without framing.

**4. STOP markers bind lifecycle sequencing to role ownership at the same boundary.**
V-05 STOP after GATE 1: `"Phase 1B cannot begin until gate1_isolation_confirmed = true. Phase 1B owner is Automate — not Expert. Role separation is a structural requirement: the same role that built Phase 1A cannot certify GATE 1B."` One STOP marker carries three constraints simultaneously: gate dependency, role assignment, and explicit prohibition. The lifecycle axis and role axis reinforce each other at the same enforcement point.

**5. Delta grouping by inertia batch (new pattern, not yet a criterion).**
V-05 Phase 5: `"Amendments correcting inertia-spec-drift (typically breaking, P1) form a coherent remediation batch. Group them by amendment type within the P1 tier."` This is orthogonal to C-22 (priority) and C-28 (amendment type) — it adds a grouping/batching layer within the delta that makes inertia-driven amendments distinguishable from schema-only corrections. Not yet a rubric criterion; candidate for C-33.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["two-clause confirmable form applied symmetrically to both GATE 1 contamination paths — actual-output isolation and inertia exclusion use identical structural form, preventing one path from being treated as weaker than the other", "role separation declared structurally enforced and not operationally optional — closes the gap where a well-structured template with role assignments can still be run by a single agent substituting both roles", "inertia-batch grouping in CONTRACT DELTA — amendments correcting inertia-spec-drift grouped as a coherent remediation batch within the P1 priority tier, orthogonal to C-22 priority and C-28 amendment type"]}
```
