# flow-dataflow — Round 12 Scoring

## Rubric Summary

- **34 aspirational criteria** — C-1 through C-41 (C-39/C-40/C-41 new in R12)
- **Weight per criterion**: 10 / 34 ≈ 0.294 pts
- **Max composite score**: 10.0

---

## Differentiating Criteria Matrix

All five variations are assumed to satisfy C-1 through C-35 (base criteria from prior rounds) and C-38 (skip-level citation present in SC-12) by construction. The table focuses on the six criteria where variations diverge.

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| **C-36** | Baseline-first ordering | FAIL | PASS | PASS | PASS | PASS |
| **C-37** | REGISTER DECLARATION Parts A/B as sole C-34/C-35 authority | FAIL | FAIL | FAIL | FAIL | PASS |
| **C-38** | Skip-level citation explicitly required in SC | PASS | PASS | PASS | PASS | PASS |
| **C-39** | SC body names governed role by boundary context label (e.g., "at Finance boundaries") | PASS | FAIL | FAIL | PASS | PASS |
| **C-40** | Position distance declared as standalone clause in SC body (e.g., "two roles prior" as a sentence-completing declaration, not parenthetical) | PASS | FAIL | FAIL | PASS | PASS |
| **C-41** | SC number appears in Phase Gate verification item's consequence text (pass/fail body), not only as a label prefix | PASS | PASS | PASS | PASS | PASS |

### Evidence notes

**V-01 — C-36 FAIL**: DOMAIN CONTEXT holds `[A-01]` only; no `[A-02]` baseline-first ordering declared. C-37 FAIL: no Parts A/B structure. C-39 PASS: SC-12 body contains "at Finance boundaries". C-40 PASS: "Position distance: two (2) roles prior" as standalone clause. C-41 PASS: Phase Gate 2 item ends "fails SC-12" in consequence text.

**V-02 — C-36 PASS**: baseline-first stated as targeted. C-37 FAIL: not targeted. C-39 FAIL: not mentioned; Commerce → Operations → Finance ordering shifts the skip-level to Finance-citing-Commerce but the SC body role-boundary label is not asserted. C-40 FAIL: same gap. C-41 PASS: "inline consequence clause with distinct phrasing" satisfies SC number in verification body.

**V-03 — C-36 PASS**: targeted. C-37 FAIL: not targeted. C-39 FAIL: dedicated SKIP-LEVEL CITATION GATE subsection gives three items but SC body label for the governed role is not asserted. C-40 FAIL: position distance not declared in SC body as standalone clause. C-41 PASS: three-item sub-block in Phase Gate 2 names the SC number in each item's body — expanded coverage satisfies criterion.

**V-04 — C-36 PASS**: targeted. C-37 FAIL: explicitly excluded ("No Parts A/B"). C-39 PASS: "explicit 'Commerce boundaries' (C-39)" asserted. C-40 PASS: "'two roles prior' standalone clause (C-40)" asserted. C-41 PASS: "'fails SC-12' consequence in Phase Gate 2 item (C-41)" asserted.

**V-05 — All six PASS**: "Full combination C-36 + C-37 + C-38 + C-39 + C-40 + C-41" explicitly declared. C-37 is uniquely satisfied here — REGISTER DECLARATION Parts A/B as sole authority for the tabular compliance markers (C-34/C-35).

---

## Per-Variation Composite Scores

| Variation | Criteria Satisfied | Score (× 0.294) | Rank |
|-----------|-------------------|-----------------|------|
| V-05 | 34 / 34 | **10.00** | 1st |
| V-04 | 33 / 34 | **9.71** | 2nd |
| V-01 | 32 / 34 | **9.41** | 3rd |
| V-02 | 31 / 34 | **9.12** | 4th= |
| V-03 | 31 / 34 | **9.12** | 4th= |

---

## Excellence Signals — V-05

**Signal 1 — C-37 + C-41 closed verification chain**: When REGISTER DECLARATION Parts A/B serves as the sole authority for tabular compliance (C-37) AND the Phase Gate item consequence text names the failing SC (C-41), an evaluator can verify both the field-level format and the skip-level gate without external context. The output becomes self-contained: each failure mode names its governing SC in the place where failure surfaces.

**Signal 2 — All three new criteria coexist without structural conflict**: V-05 demonstrates that C-39 (boundary context label), C-40 (position distance standalone clause), and C-41 (SC number in consequence body) can be satisfied simultaneously in a single SC-12 block. Prior rounds had these addressed across multiple variations; V-05 proves a single skip-level constraint can carry all three without crowding.

**Signal 3 — C-37 uniquely blocks C-34/C-35 re-declaration drift**: With REGISTER DECLARATION as the sole authority, no subsequent role section can silently restate the boundary block schema with variant column ordering or omitted fields. C-37 functions as an immutability constraint on the register specification — parallel to how SC-5 functions as immutability on the SLA threshold.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["C-37 + C-41 closed verification chain: REGISTER DECLARATION Parts A/B sole authority combined with SC number in Phase Gate consequence text makes every failure mode name its governing SC at the point of failure, eliminating evaluator search", "C-39 + C-40 + C-41 coexist in a single SC block: boundary context label, position distance standalone clause, and verification consequence can all be carried by one constraint without crowding or ambiguity"]}
```
