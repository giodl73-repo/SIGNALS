Written to `simulations/quest/golden/corps-rob-variate-R6-2026-03-16.md`.

---

## R6 -- corps-rob -- 5 Variations

**New criteria targeted:** C-22 (post-stage role-concern gap scan), C-23 (post-stage triage note gap scan), C-24 (multi-type post-stage audit suite)

**R5 V-01 got all three incidentally.** R6 makes each a formal named requirement.

---

### Variation axes selected

| Var | Axis | Target |
|-----|------|--------|
| V-01 | ROLE CONCERN GAPS as mandatory post-stage section -- absence is a format error; explicit NONE required; C-22 | C-22 |
| V-02 | TRIAGE NOTE GAPS with field-level compliance granularity -- not just section presence but per-field checking (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR populated) | C-23 (+C-18) |
| V-03 | RULE AUDIT-SUITE -- three independent post-stage sections with distinct pre-commitment scopes as an explicit named requirement; scope diversity stated; combined sections prohibited | C-24 |
| V-04 | Role-concern gap scan + triage note gap scan as companion required sections; Calibration Errors provides the third suite dimension for C-24 | C-22, C-23 |
| V-05 | Full R6 stack on R5 V-05 base -- RULES A-N (fourteen rules); RULE N states the audit suite emerges from RULE L + RULE M + Calibration Errors from RULE D | C-11 through C-24 |

---

### Key design decisions

**V-01 single-axis mechanism**: The claim is that "required; its absence is a format error" is the operative upgrade over R5 V-01's incidental section. R5 V-01 included Role Concern Gaps as a trailing section; no rule stated it was mandatory.

**V-02 field-level granularity**: The upgrade over R5 V-03 is the three failure conditions (a) section absent, (b) field label missing, (c) field content is placeholder. R5 V-03 only checked structural presence, not content quality of each field.

**V-03 explicit anti-pattern**: "A single merged section that covers all three dimensions does not satisfy RULE AUDIT-SUITE" and "Three sections that all cover the same dimension do not satisfy RULE AUDIT-SUITE -- scope diversity is required." These prohibitions are the mechanism; without them a model can satisfy the spirit while failing the letter.

**V-04 combination**: RULE BOOKEND-AUDIT names the pair together; Calibration Errors (from the Calibration Block enforcement) provides the third distinct dimension naturally, enabling C-24 without needing a separate RULE AUDIT-SUITE statement.

**V-05 expected score**: 60 (essential) + 20 (recommended C-07 + C-08) + 14×5 (all fourteen aspirational C-11 through C-24) = **130** minimum if all fourteen rules fire. If C-06 (cross-stage coherence) also fires: 135.
