Written to `simulations/quest/rubrics/trace-permissions-rubric-v8-2026-03-16.md`.

---

## Summary of v8 changes

**Two new aspirational criteria** extracted from Round 7 pass/fail contrasts. Aspirational tier grows from N=21 to N=23 (weight per criterion ~0.435).

| ID | Name | Source |
|----|------|--------|
| C-29 | Verdict-level mechanism cross-audit | v7 suggested criterion, substantiated by R7 V-04 (C-25+C-26+C-27 combined creates structural precondition but no cross-check assertion) |
| C-30 | Equivalence clause in prohibition instructions | R7 V-01 C-27 FAIL (single parenthetical, no equivalence) vs. V-03 C-27 PASS ("or any equivalent back-reference"); V-03 C-25 FAIL (missing "no declaration tracing" from enumeration) |

**Discriminating logic:**
- C-29 separates outputs where declaration and verdict happen to name the same structural fact from outputs where the output itself asserts the match — reader-inferred alignment vs. output-verified alignment. Requires both C-20 and C-21 to be present; becomes the third checkpoint in the declaration→verdict→cross-audit chain.
- C-30 separates prohibition instructions that enumerate known disallowed forms from instructions that also close the enumeration gap with a semantic equivalence clause. Without the clause, an unlisted synonym satisfies all named prohibitions while violating intent; the clause converts the examples from an exhaustive list to a representative sample.

**Suggested v9 criterion:** inertia anchor falsification condition — when C-22 (inertia framing) is satisfied, each design assumption statement includes an explicit falsification condition naming the evidence that would flip the verdict to POSSIBLE. Separates assumptions that state the expected posture from assumptions that define the failure boundary.
