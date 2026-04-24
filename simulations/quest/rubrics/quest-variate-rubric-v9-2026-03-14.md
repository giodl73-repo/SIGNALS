Written to `simulations/quest/rubrics/quest-variate-rubric-v9-2026-03-15.md`.

---

### Changes from v8 -> v9

**Three new criteria extracted:**

**C-28 — *Prevents:* label content density** (R8/V-01 vs V-03)
The R8 density ladder (V-02=0 modes, V-04=generic, V-03=1 mode, V-01=3 modes) isolates named-mode count as a distinct design dimension from label presence. C-16 required presence; C-28 requires ≥2 distinct named failure modes per phase. V-04's generic "generation errors" fails both C-16 and C-28 for independent reasons; V-03's single-mode label passes C-16, fails C-28.

**C-29 — Phase 3 structural enforcement parity** (R8/V-05)
V-05 added an explicit Phase 3 STOP CONDITION, closing the structural asymmetry between Phase 3 (label-only since R3) and Phases 1-2 (label + gate). C-27 covers Phase 1/Phase 2/checkpoint uniformly imperative (3 boundaries); C-29 extends to Phase 3 emission as a fourth boundary. Every variation V-01 through V-04 fails C-29 — Phase 3 gate was entirely absent before V-05.

**C-30 — Primary-effect field as cross-variation falsification anchor** (R8/V-01)
V-01's primary-effect embeds V-03's expected exact text ("where V-03 will contain only 'critique or scoring interleaving'") inside the primary-effect field, making the sibling's actual output the empirical test. Distinct from C-24 (structural property of own body) and C-19 (V-IDs anywhere in hypothesis): C-30 requires a sibling's positive expected text content in the primary-effect field itself as the falsification mechanism. Absence framing ("this block will be absent in V-01-V-04") does not satisfy — only positive expected text in the sibling.

**Scoring: denominator 20 → 23.**

Under v9, V-01 and V-05 remain co-leaders but each fails exactly one new criterion (C-29 for V-01, C-30 for V-05 — 89.57 each). The gaps are complementary: the **R9 baseline candidate** integrates both patterns (Phase 3 STOP CONDITION + primary-effect sibling text anchor) to become the first variation passing all 23 aspirational criteria.
