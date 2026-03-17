Done. Here's what v15 adds:

**Four new aspirational criteria promoted from R18 V-02 (sequential-stage role architecture block):**

| ID | Pattern | Condition |
|----|---------|-----------|
| C-37 | `sequential-stage-role-execution` | Two labeled role stages (STAGE 1 = primary trace, STAGE 2 = review-and-extend), each with its own vocabulary list; Stage 2 references Stage 1 output explicitly |
| C-38 | `domain-annotated-gap-skeleton` | Domain column in the gap table (Phase \| Gap \| Domain \| Severity \| Why); fill instruction mandates cross-domain comparison; requires C-37 |
| C-39 | `per-domain-automation-hook` | FINDINGS requires ≥1 automation hook per domain, not one total; extends C-10; requires C-37 |
| C-40 | `cross-domain-extension-enumeration` | Stage 2 uses explicit sub-question enumeration naming domain-specific artifacts across all four phases; generic instruction fails; requires C-37 |

**Ceiling changes:**

| Path | v14 | v15 |
|------|-----|-----|
| Prose structural-adoption (single-stage) | 180/230 | 180/250 |
| Template (single-stage) | 170/230 | 170/250 |
| **Prose structural-adoption + two-stage role** | — | **200/250** |
| Template + two-stage role | — | 190/250 |

The two-stage architecture is path-orthogonal — it stacks on either prose or template base and adds a flat +20. The new ceiling of 200/250 is the R19 target.
