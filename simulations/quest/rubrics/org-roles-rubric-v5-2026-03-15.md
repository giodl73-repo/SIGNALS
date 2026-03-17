**v5 written** to `simulations/quest/rubrics/org-roles-rubric-v5-2026-03-16.md`.

**Five new criteria added:**

| ID | Source variate | Pattern | What it's above |
|----|---------------|---------|-----------------|
| **C-21** | V-01 C-09 PASS | Instruction explicitly mandates per-role verify-question uniqueness with "no other role would prioritize this question first" language, applied while authoring | C-09 tests post-hoc output uniqueness; C-21 requires the instruction to prevent duplication by construction |
| **C-22** | V-01 C-10 PASS | Registry `total_roles` is gated against the actual count from the role-writing step via an explicit cross-reference instruction | C-10 tests content completeness; C-22 tests whether the count is independently grounded, not self-reported |
| **C-23** | V-03 C-13 PASS | Extension field introduced in the skill's first step in a named commitment block with three required sub-fields: field name + population source + purpose | C-20 requires naming before role writing; C-23 requires a formal three-element contract in the earliest step |
| **C-24** | V-04 C-01 PASS | Role-writing completion gate names exact field identifiers (`verify_questions`, `simplify_rules`) as string literals in gate conditions | C-01 tests field presence in output; C-24 tests that the gate enforces identifier precision before accepting output |
| **C-25** | V-01 C-05 PASS | Context analysis gate enumerates four named per-expert attributes (name, concern link, domain-vocabulary frame, verify focus), checked per expert not as a count | C-05 tests output specificity; C-25 tests that the derivation gate holds each expert to a minimum attribute record |

**Formula impact:** aspirational denominator `/12` → `/17`. Retroactive R4 scores: V-01 ≈ 98.82, V-02 ≈ 96.47, V-03 ≈ 98.24, V-04 ≥ 97.65 (partial scorecard). All four remain GOLDEN. V-01 and V-03 exchange ranks; V-02 drops relative to the field on three new FAILs. The ceiling rises; the threshold does not move.
