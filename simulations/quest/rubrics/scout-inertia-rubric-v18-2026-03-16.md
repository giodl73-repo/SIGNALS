v18 written to `simulations/quest/rubrics/scout-inertia-rubric-v18-2026-03-17.md`.

---

## v17 → v18 summary

**Two new criteria extracted from R17 scorecard:**

| # | Criterion | Source signal | Key distinction |
|---|-----------|---------------|-----------------|
| A-42 | **Domain-prefix vocabulary coherence across all three structural rule labels** | V-03: `INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]`, `INERTIA THREAT FAIL-FIRST RULE [A-31]` — all three share "INERTIA THREAT" prefix | A-23 requires criterion IDs in rule labels; A-42 additionally requires all three labels to share a common domain-prefix drawn from the axis vocabulary — the rule-label analogue of A-37 (position-index schema consistency) |
| A-43 | **Verification-action register verb in gate heading interrogative** | V-03: `EACH BRIDGE ARTIFACT VERIFIED?` uses VERIFIED (epistemic action) vs V-01/V-02's COMPLETE (state assertion); A-39 scoring note records the form "encodes per-element verification requirement" — a semantic property beyond cardinality alone | A-39 requires a cardinality quantifier; A-43 additionally requires the gate verb to be from verification-action vocabulary (VERIFIED, CONFIRMED, VALIDATED, CHECKED), not completion-state vocabulary (COMPLETE, BUILT, DONE, READY) |

**Ceiling: 260 → 270**

**New implication chains:**
- `A-43 implies A-39 implies A-33 implies A-27 implies A-22 implies A-12`
- `A-42 implies A-23 implies A-19 implies A-16 implies A-14 implies A-08`

**R18 target**: A 270/270 variation requires V-03's scaffold (domain-prefix rule coherence + VERIFIED verb) combined with STRUCTURAL FAULTS (A-40 + A-41) on a schema-consistent position-indexed gate (A-37) with any valid cardinality quantifier (A-39). The EACH/VERIFIED combination from V-03 satisfies both A-43 and A-39 simultaneously.
