Here is the updated rubric:

---

# Rubric — scout-requirements (v6)

**24 criteria across 3 tiers. Total: 122 pts.**

---

## Essential (60 pts — 12 pts each) — unchanged

C-01 through C-05 carry forward without modification.

---

## Recommended (30 pts — 10 pts each) — unchanged

C-06 through C-08 carry forward without modification.

---

## Aspirational (32 pts — 2 pts each)

C-09 through C-21 carry forward from v5. Three new criteria:

| ID | Text | Source | Pass Condition |
|----|------|--------|----------------|
| **C-22** | Loop 2 → Loop 3 artifact dependency stated as a verbatim design contract | V-05 R1 | Charter contains a sentence that explicitly names the Loop 2 → Loop 3 dependency as a structural contract (e.g., "Loop 2 creates the execution artifacts Loop 3 requires as evidence"); the relationship is chartered, not inferred — C-20 requires the complementary design to *exist*; C-22 requires the charter to *own* it as a named obligation before execution begins |
| **C-23** | Per-law independent enforcement triplets: no cross-law single-point failure | V-05 R1 | For each law enforced (Law A = two-path ambiguity, Law B = closure gates), the charter assigns independent declare/apply/verify triplets — Law A's Loop 1 names Law A's Loop 2 specifically; Law B's Loop 1 names Law B's Loop 2 specifically; a shared preamble covering both laws as a single unit fails; independent chains mean one law's loop failure cannot cascade to the other |
| **C-24** | Structural closure of the meta-loop: declaring C-17 implies C-18 and C-19 as structural consequences | V-05 R1 | The charter's meta-requirement statement is self-closing: asserting Loop 1 (C-17) simultaneously instantiates Loops 2 and 3 as necessary consequences of the declaration, not as separately mandated additions — C-21 requires loops named by rubric ID; C-24 requires Loop 1's declaration to be structurally incomplete without Loop 2, making skipping impossible through logical closure rather than external enforcement |

---

## Scoring Bands

| Band | Score | Meaning |
|------|-------|---------|
| Golden | 110–122 | All essential + recommended pass; strong aspirational |
| Strong | 95–109 | All essential pass; most recommended; partial aspirational |
| Acceptable | 76–94 | All essential pass; partial recommended; minimal aspirational |
| Weak | 60–75 | All essential pass; recommended largely missing |
| Fail | < 60 | One or more essential criteria fail |

**Golden threshold**: all 5 essential pass AND composite >= 98/122 (~80%).

---

**What the three new criteria capture:**

- **C-22** distinguishes *having* the prevention-detection complementarity (C-20) from *committing to it in the charter* as a named design contract. A charter can achieve C-20 by design and still fail C-22 if it never names the obligation.

- **C-23** distinguishes C-17's "all three loops for each constraint" from per-law *independent* chains. Two laws with a shared enforcement preamble satisfy C-17 but fail C-23 — independence means neither chain's failure cascades.

- **C-24** distinguishes C-21's labeling requirement (loops named by rubric ID) from structural closure — Loop 1's declaration must make Loop 2 a logical necessity, not just a parallel item. Self-enforcing through closure, not through external mandate.

V-05 at 115/116 would score **117/122** under v6 (adding C-22 and C-23, still PARTIAL on C-21 and C-24). The next variation needs to close those two gaps to reach 122.
