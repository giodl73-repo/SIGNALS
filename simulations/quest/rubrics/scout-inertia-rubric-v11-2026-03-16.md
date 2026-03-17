`scout-inertia-rubric-v11-2026-03-17.md` written.

---

**v10 -> v11: three new criteria, ceiling 165 -> 180**

| # | Criterion | Source signal |
|---|-----------|---------------|
| A-23 | **Criterion ID embedded in rule label text** | R10 V-02/V-03 signal: `[A-16 PRIMARY KEY RULE]`, `PRIMARY KEY CONSTRAINT [A-16]`, `REFERENTIAL INTEGRITY RULE (citation point) [A-19]`. A-16 and A-19 require the rules be present; A-23 requires each rule's criterion ID appear inside its label, enabling template auditing without external reference. A-23 implies A-19. |
| A-24 | **Dual-type inline threshold example in DC threshold column label** | R10 V-01/V-02/V-03 consistent signal: all three 165/165 variations use `(e.g., >10MB, >3 failures/week)` — two examples of distinct threshold types. A-21 requires one example; A-24 requires two examples of different unit families or comparison contexts, demonstrating that the operator+value+unit pattern generalizes. A-24 implies A-21. |
| A-25 | **Active command directive on bridge completion gate** | R10 V-02 signal: `[BRIDGE COMPLETION COMMAND]` as a named element alongside the Y/N table. A-22 requires a named verification block in position; A-25 requires that block to also carry an explicit active instruction telling the author to complete Q3/Q4 before proceeding. Passive status check vs. active directive. A-25 implies A-22. |

**Updated implication chain**: A-25 implies A-22 implies A-12. A-24 implies A-21 requires A-20 and A-13. A-23 implies A-19 implies A-16 implies A-14 implies A-08. A-18 implies A-15. A-17 implies A-11.

**R11 note**: A-24 may already be passing in R10 V-01/V-02/V-03 — all three use the dual-type example `>10MB, >3 failures/week`. V-04/V-05 unscored. R11 scoring will determine whether A-24 was a retroactive pass or requires explicit generation. A-23 and A-25 split V-02 from V-01/V-03 (V-02 has both; V-03 has A-23 only; V-01 has neither).
