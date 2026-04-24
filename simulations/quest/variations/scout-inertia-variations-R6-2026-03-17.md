Written to `simulations/quest/golden/scout-inertia-variate-R6-2026-03-17.md`.

---

## R6 Variations — Summary

**Variation Map**

| ID | Axis | Key Change from R5 |
|----|------|--------------------|
| V-01 | C-19 minimum viable | Adds "Replication Fidelity Standard" named label + 2 inline pairs to R5 V-01 (Competitor Zero base) |
| V-02 | C-20 maximum density | Converts every fail condition to a full pass/fail pair throughout R5 V-02 (Schema block base) |
| V-03 | C-19 comprehensive via roles | Names all 5 multi-component requirements as sub-protocols (Replication Fidelity Standard, Switching Cost Protocol, Failure Mode Standard, Loss Condition Standard, Anchored Rebuttal Protocol) in role instructions |
| V-04 | C-19+C-20 as phase-protocol headers | Phase headers declare sub-protocol names; each phase opens with inline pass/fail pairs |
| V-05 | All axes | R5 V-05 extended: all 5 sub-protocols named in template positions + counter-example pairs at every requirement in Sections A, C, D, F |

**Key design insights:**

- **C-19/C-20 independence confirmed**: V-01 = C-19 minimal + C-20 minimal; V-02 = C-19 minimal + C-20 maximal. They are satisfiable separately at minimum cost.
- **C-12 gap in V-01/V-02**: Single-axis variations don't carry the NAMED CLAIM anchor (not their axis). V-03–V-05 close it via the Anchored Rebuttal Protocol label.
- **Natural co-occurrence**: Comprehensive C-19 (V-03–V-05) creates more sites for C-20 pairs — each named sub-protocol's numbered items are natural pair-anchors.
- **Reliability gradient**: V-01 (1 named protocol, 2 pairs) → V-05 (5 named protocols, 10+ pairs). V-05 requires five independent omissions to fail.

**Predicted scores**: V-01/V-02 at ~99.6 (C-12 PARTIAL); V-03/V-04/V-05 at 100.
