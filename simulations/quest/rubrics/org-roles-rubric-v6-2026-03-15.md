**v6 written** to `simulations/quest/rubrics/org-roles-rubric-v6-2026-03-16.md`.

**Five new criteria added:**

| ID | Source variate(s) | Pattern | What it's above |
|----|------------------|---------|-----------------|
| **C-26** | V-02 C-01 PASS, V-05 dual mechanism | Skill defines a numbered FC-N contract block as the single authoritative source for field identifiers, referenced by gates and templates | C-24 tests gate-level quoting; C-26 tests existence of a unified contract structure separate from templates |
| **C-27** | V-03 C-22 PASS (PHASE5_COUNT), V-05 C-22 PASS | Cross-step count declared as a named variable in a PREPARE sub-step before WRITE begins; WRITE phase binds to the variable | C-22 tests that a gate instruction requires cross-step verification; C-27 tests the mechanism — pre-write input vs. post-write check |
| **C-28** | V-02 C-05 PASS | Instruction explicitly names placeholder name anti-patterns (e.g., "domain-expert", "expert-1") that would pass visual review but violate C-05 specificity | C-05 tests output specificity; C-28 tests defensive prohibition of the specific failure class |
| **C-29** | V-02 C-08/C-14 PASS, V-05 C-08/C-14 PASS | Dual-failure prohibitions framed as CONTRACT VIOLATION (type 1)/(type 2) inside a named contract block, not as advisory failure modes | C-14 requires typed labels; C-29 requires contract violation framing — makes the prohibition binding rather than advisory |
| **C-30** | V-04 C-23 PASS, V-05 C-23 PASS | Extension commitment block's purpose sub-field explicitly names the Phase 0 diagnostic question it answers, not just describes the field's content | C-23 requires three elements; C-30 requires the purpose element to close back to the skill's own opening diagnostic |

**Formula impact:** aspirational denominator `/17` → `/22`. R5 retroactive scores: V-05 = 99.55 (new leader), V-02 = 99.09, V-04 = 98.18, V-01 = 97.73, V-03 ≈ 97.73. V-01 drops from first to fourth — missing all five new criteria. V-02 rises on three new PASSes from its FC-N contract architecture. All five remain GOLDEN.
