All 40 criteria present (5 essential + 3 recommended + 32 aspirational). Header values correct.

---

**flow-trigger-rubric-v13** written to `simulations/quest/rubrics/flow-trigger-rubric-v13-2026-03-16.md`.

---

**One new aspirational criterion (C-40), N_aspirational: 31 → 32, max (raw): 142.5 → 145.0:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-40 | V-05 inseparability signal — attribution chain rationale embedded as a named note block *inside* the CLOSURE CHECK counter block, making rationale physically inseparable from the detection mechanism | Detection-mechanism-bound attribution rationale: the C-39 rationale appears inside the CLOSURE CHECK block (not in a separable section before or after it), converting silent content removal into a detectable structural change. Removing the rationale requires modifying the CLOSURE CHECK structure itself. | C-39 (section-level rationale requirement — C-40 is the mechanism-level binding requirement), C-29 (same C-26→C-29 progression: standalone section → inline embedding, applied here to the attribution chain context) |

**Structural relationship:** C-39 is the "C-26 level" — rationale must be co-located with the ARTIFACT MANIFEST, CLOSURE CHECK, or a named DESIGN RATIONALE section, but it can be a separable standalone section. C-40 is the "C-29 level" — rationale must be embedded *inside* the CLOSURE CHECK block, inseparable from the counter values. The V-04/V-05 scorecard split established this: V-04's separate ATTRIBUTION CHAIN DESIGN RATIONALE section earned a C-39 PASS; V-05's in-counter note block earned C-39 PASS and additionally demonstrated the inseparability property that C-40 now formalizes.
