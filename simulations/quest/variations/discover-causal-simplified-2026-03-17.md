---

## QU5 Result

**File written:** `simulations/quest/golden/discover-causal-golden-2026-03-17.md`

**Word count:** 3,226 → 2,203 | **Reduction: 32%**

### What was removed (20 excision sites, zero criteria lost)

| Phase | What removed | Why safe |
|-------|-------------|----------|
| Phase 0 PROHIBITED FORM | Sentences 3–4 (restatement + "not a neutral finding" characterization) | Sentence 1 already satisfies C-22 pass condition; sentence 5 (named conditional form) retained |
| Phase 0 | "A mechanism that merely also produces Y alongside the status quo is not a causal claim for X." | Explanatory gloss; Phase 2 Competing instruction carries the enforcement |
| Phase 1 PROHIBITED FORM | 4 trailing sentences (deferral example, confidence annotation note, "even one traceable step") | C-27 requires only "does not pass" at Phase 1; first sentence satisfies it |
| Phase 1 end | "Producing three thin or vague steps..." warning (2 sentences) | C-11 tests model behavior, not whether this sentence appears in the prompt |
| Phase 2 labeling block | 5-sentence explanation of why labels are required | C-16 is satisfied by the format requirement + "same label must appear identically" sentence |
| Phase 3 ANCHOR-UPDATE | "stale-anchor propagation failure occurs at Phase 6, not here. Both sites must reflect..." (summary sentences) | Explanatory summary after the operative C-31 prohibition sentence |
| Phase 3 PROHIBITED FORM (C-24) | 3-sentence elaboration after first sentence | C-24 requires the deferral form named as failure mode; first sentence does it |
| Phase 3 | "This branch confirms... It does not introduce fresh deferral." | Redundant with the block above |
| Phase 3 end | "A metric shortfall is an outcome check. Name where the mechanism stops working." | Operative prohibition is "Do not state falsification as a metric threshold" |
| Phase 4 | "These fields are orthogonal..." (2 sentences) | Restates FIELD INDEPENDENCE NOTE above |
| Phase 4 NULL-GAP | 6-sentence explanation block after 2-line example | C-21 requires showing the example; not the explanation of it |
| Phase 4 PROPAGATION | 2 trailing sentences | First sentence carries the C-25 enforcement; rest is restatement |
| Phase 4 end | External evidence tier note | No criterion tests for it |
| Phase 5 | "It does not count as a confounder..." | EXCLUDED sentence already covers it |
| Phase 5 | 4-bullet list of confounding types | No criterion requires these categories; C-07 instruction stands without them |
| Phase 6 Mechanism completeness | Parenthetical example | Illustrative only |
| Phase 6 stale-anchor rule | Explanatory trailing sentences | Operative "does not pass" sentence satisfies C-30 rule |
| Phase 6 C-31 rule | Design-rationale paragraph (escape hatch, model reading) | C-32 is satisfied by "does not pass C-31"; the rationale is not criterion-tested |
| Phase 6 C-34/C-35 + C-33/C-36 rules | Audit-state explanation sentences ("satisfies C-34 (behavioral failure, correct audit)...") | Both C-35 and C-36 two-element requirements preserved verbatim |
| Phase 6 end | Evidence gap analogy sentence + "Partial synthesis..." | Both redundant with adjacent specific rules |

### Criteria verification

- **C-01 through C-05 (essential):** PASS — all phase instructions intact
- **C-06 through C-08 (recommended):** PASS — labeling, confounder, AMEND structure preserved  
- **C-22, C-24, C-26–C-36 (key aspirationals):** PASS — every enforcement site (prohibited forms, integration rules, ARTIFACT fields) preserved at required locations
- **C-35 two-element requirement:** PASS — both "`false` -- not absent" and "fails C-34 separately from C-27 fail" present in Phase 6 rule
- **C-36 two-element requirement:** PASS — both "`false` -- not absent" and "fails C-33 separately from C-31 fail" present in Phase 6 rule

```json
{"simplified_word_count": 2203, "original_word_count": 3226, "all_essential_still_pass": true}
```
