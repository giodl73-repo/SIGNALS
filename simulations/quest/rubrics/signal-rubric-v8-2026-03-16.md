**v8 written** to `simulations/quest/rubrics/signal-rubric-v8-2026-03-17.md`.

---

**Two new criteria extracted from R8:**

**C-24 — Meta-rule inventory by explicit RULE number** (aspirational / depth)

The RULE enforcing C-23 must name each governed meta-rule by explicit RULE number. Without it, a C-23 verifier must scan the full rule list to discover which rules are meta-rules — O(N). With it, the target set is O(1) at the point of enforcement.

- V-01 R8: FAIL — RULE 15 states the requirement, names no targets
- V-02/V-03 R8: PASS — RULE 15 names RULE 12, RULE 13, RULE 14 explicitly

**C-25 — Expected evidence strings stated inline in the C-23 rule** (aspirational / depth)

The RULE enforcing C-23 must state the expected evidence string for each governed meta-rule inline. Without it, the auditor knows *which* rules to check (C-24) but must still look each one up to know *what to look for* before checking. With it, the full C-23 audit is self-contained at RULE 15: read the expected strings, perform three targeted confirmations, done.

- V-01/V-02 R8: FAIL
- V-03 R8: PASS — RULE 15 states "RULE 12 contains 'Count = 15'; RULE 13 contains '15/15 checked = valid output'; RULE 14 names RULE 11"

---

**Formula update:**

```
aspirational_pass / 17 x 10  (~0.59 pts each, was ~0.67)
```

**R8 scores under v8** — the three previously indistinguishable variations now separate:

| Variation | C-24 | C-25 | Score |
|-----------|------|------|-------|
| V-01 | FAIL | FAIL | 98.82 |
| V-02 | PASS | FAIL | 99.41 |
| V-03 | PASS | PASS | 100.00 |
