---

**trace-request R14 variations written** → `simulations/quest/rubrics/trace-request-rubric-v13-variate-R14-2026-03-15.md`

## Summary

5 complete variations targeting **C-37** (CHECKER ALGORITHM block with MATCH-RULE / HALT-RULE / OUTPUT-RULE immediately after TOKEN-COUNT in Step 8 Header):

| Variation | Axis | C-37 Mechanism | Key Risk |
|-----------|------|----------------|----------|
| **V-01** | Role sequence | Algorithm-Declarant pre-declares in Step A; Step 8 Header reproduces verbatim | Reproduction may paraphrase if Step A tokens are loosely formed |
| **V-02** | Output format | CHECKER ALGORITHM skeleton pre-printed as mandatory fill-in fields in Step 8 Header template | Model fills token labels with prose paragraphs instead of machine-greppable phrases |
| **V-03** | Lifecycle emphasis | ALGORITHM-CONTRACT named phase gates Step 8a entry; phase requires block before advancing | Block produced correctly in P-2 artifact but Step 8 Header placement (after TOKEN-COUNT) may be imprecise |
| **V-04** | Role sequence + Lifecycle | Scope-Verifier role entry contract IS the CHECKER ALGORITHM; role handoff + phase gate double-enforce | Role entry block correct but Step 8 Header carry may not reproduce at exact TOKEN-COUNT position |
| **V-05** | Output format + Register + Inertia | Pre-printed skeleton + declarative register + inertia framing anchors CHECKER ALGORITHM against ad-hoc scope-checking status quo | Inertia framing section may cause model to produce the block correctly there but compress it in Step 8 Header |

**C-37 failure pattern from R13 diagnosed**: four of five R13 variations produced TOKEN-COUNT but embedded algorithm logic in Step 8b prose or as a single combined sentence — missing structural independence of the three named tokens. Each R14 variation attacks a specific failure mode from a different direction.
