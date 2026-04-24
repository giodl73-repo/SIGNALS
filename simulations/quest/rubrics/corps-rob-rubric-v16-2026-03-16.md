Written to `simulations/quest/rubrics/corps-rob-rubric-v16-2026-03-17.md`.

**Two new criteria extracted from R15 excellence signals:**

**C-47 — RULE AUDIT-INDEPENDENCE Named-Rule Decomposition** (C-46 dep)
V-03 and V-05 both factor the independence declaration out of RULE AUDIT-TABLE entirely. RULE AUDIT-TABLE retains only ordering + anti-pattern (C-41). A separate named RULE AUDIT-INDEPENDENCE owns the two-branch enumeration. Single-responsibility decomposition: each rule auditable in isolation. The V-02/V-04 embedded path satisfies C-46; only the factored path satisfies C-47.

**C-48 — RULE AUDIT-INDEPENDENCE Escalation-Boundary Annotation** (C-47 dep)
V-03's RULE AUDIT-INDEPENDENCE (and V-05's identical form) prints the escalation boundary inline: "a single 'mandatory regardless of table presence' clause satisfies C-44 but not C-46 -- only explicit enumeration of both branches satisfies C-46." Names the C-44-satisfying form, declares it insufficient for C-46, names the C-46-satisfying form. Rule is self-documenting without rubric consultation. Parallels C-41's anti-pattern discipline applied to the independence escalation.

**Scoring impact:**

| | v15 | v16 |
|--|-----|-----|
| Aspirational pool | 38 x 5 = 190 | 40 x 5 = 200 |
| Max composite | 280 | 290 |

**Retroactive R15 best under v16:** V-05 = 285/290 (C-45+C-46+C-47+C-48 all pass; persistent gap criterion still unresolved). Ideal R16 targets 290/290.
