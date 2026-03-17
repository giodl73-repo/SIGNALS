Written to `simulations/quest/golden/org-review-variate-R16-2026-03-16.md`.

---

# org-review -- Variate Round 4 (v11 rubric, 2026-03-16)

5 complete prompt body variations targeting C-33/C-34/C-35 on top of the V-05 R11 §1-§16 base.

**R4 design target**: Combine V-05 R11's C-30+C-31+C-32 base (210/225) with C-33+C-34+C-35 additions (225/225). Prior rounds explored these mechanisms; R4 tries structurally different placements.

**Variation axes explored**:

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence / Output format -- §17 ROLE MANIFEST APPLICABILITY PROTOCOL | Applicability ratings pre-committed in the ROLE MANIFEST table (before any reviewer), not per-row in the LENS COVERAGE TABLE during review. Each manifest row gains an `Applicability` column. §15 inherits the rating. |
| V-02 | Role sequence / Lifecycle emphasis -- §17 PRE-REVIEW DOMAIN COVERAGE GAP-CHECK | §1 IN-SCOPE rows carry `[DOMAIN: label]` annotations. A dedicated DOMAIN COVERAGE GAP-CHECK section runs between ROLE MANIFEST and BRACKET OPENING, checking each domain for HIGH-applicability coverage before the first reviewer fires. GAP domains become ADVISORY-LENS-GAP items before any review runs. |
| V-03 | Inertia framing -- §17 NH DIMENSION TABLE CONTRACT with tiered dimensions | Challenger's BRACKET OPENING adds a NULL HYPOTHESIS DIMENSION TABLE with Tier column (MUST-CLEAR / ADVISORY) and NH Verdict column. A pre-committed two-step formula (MUST-CLEAR block check + tier-weighted tally) derives g_null(initial) from the NH Verdict column alone. The table is also emitted at BRACKET CLOSING with aggregate scores. |
| V-04 | V-01 + V-02 combination | §17 ROLE MANIFEST APPLICABILITY + §18 PRE-REVIEW DOMAIN GAP-CHECK. §18 uses §17's manifest ratings as its evidence basis -- a domain is HIGH-COVERED only if a role's manifest Applicability=HIGH AND its expertise.relevance covers the domain. C-33 and C-34 become causally linked. |
| V-05 | V-01 + V-02 + V-03 full integration | §17 (manifest applicability) → §15 (lens coverage inherits ratings) → §18 (domain gap-check uses §17 as evidence) + §19 (NH Dimension Table makes g_null(initial) table-derivable). §9 Stage 1 explicitly constrained to equal §19 formula result. All 27 aspirational criteria simultaneously satisfiable. 225/225 candidate. |

**Key structural distinctions from R12/R13**:
- R12/R13 added applicability as a separate §17/§18 contract clause with per-lens-entry ratings inside the reviewer phase. R4 V-01/V-04/V-05 commit applicability at the ROLE MANIFEST level (pre-review), making it the single upstream source for both §15 (LENS COVERAGE TABLE) and §18 (domain gap-check).
- R12/R13 placed the domain gap-check after lens tables. R4 V-02/V-04/V-05 move it before BRACKET OPENING, so domain gaps are visible before any reviewer fires.
- R4 V-03's NH Dimension Table adds Tier labels and a two-step formula (MUST-CLEAR block + weighted tally), giving g_null more structural depth than R13's two-column approach.
