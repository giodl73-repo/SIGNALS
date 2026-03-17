## mock-all Variate Scoring — Round 1

### V-01 — Role Sequence: Coverage Analyst First

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | PASS | Step 2 mandates `<!-- MOCK ARTIFACT -->` with Skill/Topic/Category/Date/Status/Flag fields per section |
| C-02 | Essential | PASS | Step 1 pre-classification table gives exact ground-truth labels before any artifact is written |
| C-03 | Essential | PASS | Explicit: "EVIDENCE-HEAVY namespaces (prove, listen) are auto-flagged REAL-REQUIRED regardless of artifact quality" |
| C-04 | Essential | PASS | Step 3: "exactly these 4 columns and 9 data rows" |
| C-05 | Essential | PASS | Dedicated FINAL LINE section; `{this-file}` annotated as "the artifact filename produced in this run (not a placeholder)" |
| C-06 | Recommended | PASS | Step 3 flag rules enumerate TIER-2-CRITICAL (trace) and TIER-3-CRITICAL (scout-feasibility, listen) |
| C-07 | Recommended | PASS | "3 or more substantive lines… Not generic filler. Show what a real artifact would say" |
| C-08 | Recommended | PASS | Step 3: scout-compliance and trace-permissions flagged REAL-REQUIRED; "apply conservatively" when TOPICS.md absent |
| C-09 | Aspirational | PASS | Step 4 specifies tier scoping with 3 explicit cases |
| C-10 | Aspirational | PASS | "Name a specific Signal skill invocation… Never write 'gather more data'" |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 2/2

**Score:** (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **100**
**Golden threshold:** PASS (all essential + score ≥ 80)

---

### V-02 — Output Format: Per-Section Verdict Block

| Criterion | Band | Result | Evidence |
|-----------|------|--------|----------|
| C-01 | Essential | PASS | 3-part section structure mandates MOCK ARTIFACT header with all required fields |
| C-02 | Essential | PASS | CATEGORY assignment rules inline; prove/listen → EVIDENCE-HEAVY, others correctly assigned |
| C-03 | Essential | PASS | "REAL-REQUIRED (mandatory — cannot be omitted)" — stronger phrasing than V-01 |
| C-04 | Essential | PASS | "9 rows. Exactly 4 columns." |
| C-05 | Essential | **FAIL** | Prompt has no FINAL LINE section; Coverage Verdict's per-section `Next:` field does not substitute for the handoff line `Next: /mock:review {topic} {this-file}` |
| C-06 | Recommended | PASS | FLAG rules enumerate TIER-2-CRITICAL and TIER-3-CRITICAL correctly |
| C-07 | Recommended | PASS | Stronger guardrails: "Not headers. Not category labels. Not the topic name repeated" |
| C-08 | Recommended | PASS | Compliance topics listed in FLAG rules |
| C-09 | Aspirational | PASS | TIER FLAG section present and explicit |
| C-10 | Aspirational | PASS | Per-section Coverage Verdict enforces `/{namespace}:{primary-skill} {topic}` format |

**Essential:** 4/5 | **Recommended:** 3/3 | **Aspirational:** 2/2

**Score:** (4/5 × 60) + (3/3 × 30) + (2/2 × 10) = 48 + 30 + 10 = **88**
**Golden threshold:** FAIL (C-05 essential failure)

---

### Ranking

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| 1 | V-01 | 100 | YES | Perfect across all bands |
| 2 | V-02 | 88 | NO | Strong structure but missing handoff instruction |

---

### Excellence Signals from V-01

1. **Pre-classify-then-generate ordering** — the classification table in Step 1 puts category ground truth in active context before any artifact body is written; the model cannot misclassify while generating because the answer is already on the page.
2. **Dedicated FINAL LINE section** — isolating the handoff instruction as its own numbered section with explicit anti-placeholder language ("not a placeholder") eliminates C-05 failures that occur when the instruction is buried in a prose block.
3. **Rationale injection alongside rules** — "A synthetic artifact cannot substitute for real signal in these namespaces" gives the model a reason for the REAL-REQUIRED flag, which increases adherence over bare imperatives.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-classify-then-generate ordering puts category ground truth in context before artifact writing begins", "dedicated FINAL LINE section with anti-placeholder annotation prevents C-05 failures", "rationale injection alongside rules increases flag compliance over bare imperatives"]}
```
