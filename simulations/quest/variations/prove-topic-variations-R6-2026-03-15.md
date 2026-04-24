**Round 6 variations written** to `simulations/quest/golden/prove-topic-variate-R6-2026-03-15.md`.

---

## Summary

### Axes and hypotheses

| Var | Axis | Hypothesis |
|-----|------|-----------|
| V-01 | **Role Sequence** | Two blocking roles (ROLE A = invariant registry, ROLE B = scout load) produce `invariant_registry_confirmed` as a first-class output of an independent role, not an annotation on scout-load. C-22 falls out structurally. |
| V-02 | **Output Format** (table) | A cumulative null-tally table with one row per evidence stage makes C-20's running count structural — the tally column is filled per-stage, not assembled at synthesis. |
| V-03 | **Lifecycle Emphasis** | STAGE ENTER / STAGE EXIT blocks with a required `null_tally` field in each exit gate forces tally language to appear at the moment the null occurs, not retroactively. |
| V-04 | **Phrasing Register + Inertia Framing** | Conversational register + incumbent-as-character. Running tally is "what the incumbent is still owed in review" — obligation framing rather than compliance framing. Tests whether debt language is a cleaner path to C-20 than protocol language. |
| V-05 | **Role Sequence + Output Format + Inertia** (combined) | All three axes active simultaneously: ROLE A produces C-22's second field, the incumbent-defense table produces C-20's tally, the dual-lock table row echoes into Handoff for C-21. Each criterion has a distinct structural source — no single axis can be dropped without losing one criterion. |

### C-20 / C-21 / C-22 coverage per variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-20 (per-stage tally) | Role exit blocks with "X stages remain" | Table row per stage with null count column | STAGE EXIT gate field | "Incumbent still owed N reviews" | Table row per stage |
| C-21 (co-activation in handoff) | `co_activation_confirmed: [must equal dual_lock_fired]` | Same field in Handoff table | Same field in STAGE 5 EXIT block | Same field in Handoff | Same field + `incumbent_defense_closed` |
| C-22 (registry as distinct field) | Two roles → two fields naturally | Two lines in hypothesis frontmatter | Two fields in GATE S exit | Two fields in hypothesis frontmatter | ROLE A + ROLE B → two fields |
