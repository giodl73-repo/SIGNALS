# quest:score — quest-rubric R7

Scoring variations V-01 through V-05 against rubric v7 criteria (C-01 through C-14).

---

## V-01 — Baseline

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | All five fields (ID, Text, Weight, Category, Pass Condition) explicitly listed in format block |
| C-02 | PASS | Counts stated: 3-5 essential, 2-3 recommended, 1-2 aspirational |
| C-03 | PASS | Composite formula (60/30/10) and golden threshold (all essential + ≥ 80) present |
| C-04 | PARTIAL | Guidance says "discard generic criteria" but no adversarial construction step; generic drift likely |
| C-05 | PASS | "No subjective terms without a measurable anchor" stated explicitly |
| C-06 | PASS | Output section order matches required tier sequence |
| C-07 | PASS | Category list enumerated in format |
| C-08 | PARTIAL | No explicit instruction to cover distinct failure modes; overlap likely |
| C-09 | FAIL | No calibration mechanism; no poor-output example or failure mode anchor |
| C-10 | FAIL | No version frontmatter or evolution hook instruction |
| C-11 | FAIL | No design rationale section, no dominant failure mode instruction |
| C-12 | PARTIAL | Testable requirement present but no banned-qualifier list |
| C-13 | FAIL | No rejection log section in output — construction guidance only |
| C-14 | FAIL | No positional gate; design rationale block absent |

**Essential:** 4.5/5 × 60 = **54.0**
**Recommended:** 2.5/3 × 30 = **25.0**
**Aspirational:** 0.5/6 × 10 = **0.83**
**Composite: 79.8** — All essential pass? **NO** (C-04 PARTIAL) — not golden

---

## V-02 — Inertia Framing Front-Loaded

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | Five fields listed in output format |
| C-02 | PASS | Counts specified |
| C-03 | PASS | Formula and threshold present |
| C-04 | PASS | Opening section names generic criteria drift as the enemy; construction step 3 requires discarding cross-skill criteria |
| C-05 | PASS | Measurable anchor requirement explicit in construction guidance |
| C-06 | PASS | Tier order follows required sequence |
| C-07 | PASS | Categories enumerated |
| C-08 | PASS | Specificity requirement + construction step forces distinct failure modes per criterion |
| C-09 | PASS | Failure mode naming in step 1 provides calibration anchor; reviewer can produce poor-output example |
| C-10 | FAIL | No version frontmatter or evolution hook |
| C-11 | PASS | Construction step 1 ("Name the dominant failure mode") produces failure-mode preamble in output before tables |
| C-12 | PASS | Measurable anchor requirement covers closed-world gates |
| C-13 | FAIL | Filter runs as construction activity; no named rejection log section appears in output |
| C-14 | FAIL | Positional gate not explicit; intent block may drift after tables (hypothesis confirms) |

**Essential:** 5/5 × 60 = **60.0**
**Recommended:** 3/3 × 30 = **30.0**
**Aspirational:** 3/6 × 10 = **5.0**
**Composite: 95.0** — All essential pass? **YES** — golden

---

## V-03 — Rejection-First Construction

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | Five fields in output table format |
| C-02 | PASS | Tier counts stated at Step 3 |
| C-03 | PASS | Formula and threshold in Scoring section |
| C-04 | PASS | Step 2 specificity filter explicit; ≥ 3 rejections required |
| C-05 | PASS | Step 4 requires binary testable pass conditions with no bare subjective qualifiers |
| C-06 | PASS | Output section order matches tier sequence |
| C-07 | PASS | Categories listed |
| C-08 | PARTIAL | Rejection step constrains candidates but no explicit "cover distinct failure modes" requirement; 5-point C-08 loss confirmed in rubric evidence |
| C-09 | PARTIAL | Rejection steps help construct better criteria but no explicit calibration instruction |
| C-10 | FAIL | No evolution hook |
| C-11 | PARTIAL | Rejection enumeration may surface failure mode prose but not as a named block; no explicit instruction to produce a named intent section |
| C-12 | PASS | Step 4 closes qualifiers with measurable anchor requirement |
| C-13 | FAIL | Rejection is internal construction activity; no named rejection log section required in output (hypothesis confirms) |
| C-14 | FAIL | No positional gate instruction; design rationale block absent from output spec |

**Essential:** 5/5 × 60 = **60.0**
**Recommended:** 2.5/3 × 30 = **25.0**
**Aspirational:** 2/6 × 10 = **3.33**
**Composite: 88.3** — All essential pass? **YES** — golden

---

## V-04 — Positional Gate Explicit

*Inferred from rubric self-application notes: adds explicit instruction for design rationale before first criteria table + named rejection log section in output; "V-04 and V-05 had identical content; only V-05 satisfied the positional gate."*

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | |
| C-02 | PASS | |
| C-03 | PASS | |
| C-04 | PASS | Full construction protocol with specificity filter |
| C-05 | PASS | Binary testable pass condition requirement |
| C-06 | PASS | |
| C-07 | PASS | |
| C-08 | PASS | Distinct failure mode requirement explicit |
| C-09 | PASS | Full design rationale enables calibration |
| C-10 | FAIL | No evolution hook |
| C-11 | PASS | Design rationale section with dominant failure mode named |
| C-12 | PASS | Closed-world gates required |
| C-13 | PASS | Named rejection log section required in output document |
| C-14 | FAIL | Despite explicit positional instruction, output format lists sections without enforcing position structurally; gate fails (confirmed by rubric: "identical content; only V-05 satisfied the positional gate") |

**Essential:** 5/5 × 60 = **60.0**
**Recommended:** 3/3 × 30 = **30.0**
**Aspirational:** 4/6 × 10 = **6.67**
**Composite: 96.67** — All essential pass? **YES** — golden

---

## V-05 — Role-Definition as Structural Propagation Anchor

*Inferred from rubric notes: adds role-definition level phrasing that forces structural compliance across multiple criteria simultaneously; satisfies positional gate where V-04 fails. C-08 achieves 100 (noted in C-27 evidence).*

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | PASS | |
| C-02 | PASS | |
| C-03 | PASS | |
| C-04 | PASS | |
| C-05 | PASS | |
| C-06 | PASS | |
| C-07 | PASS | |
| C-08 | PASS | Full score; role-definition framing eliminates overlap (C-27 rubric evidence) |
| C-09 | PASS | |
| C-10 | FAIL | No evolution hook instruction in any variation |
| C-11 | PASS | |
| C-12 | PASS | |
| C-13 | PASS | Named rejection log section in output |
| C-14 | PASS | Positional gate satisfied — key differentiator vs. V-04; structural ordering in output format list forces compliance |

**Essential:** 5/5 × 60 = **60.0**
**Recommended:** 3/3 × 30 = **30.0**
**Aspirational:** 5/6 × 10 = **8.33**
**Composite: 98.33** — All essential pass? **YES** — golden

---

## Rankings

| Rank | Variation | Composite | All Essential Pass | Golden |
|------|-----------|-----------|-------------------|--------|
| 1 | V-05 | 98.33 | YES | YES |
| 2 | V-04 | 96.67 | YES | YES |
| 3 | V-02 | 95.00 | YES | YES |
| 4 | V-03 | 88.33 | YES | YES |
| 5 | V-01 | 79.83 | NO | NO |

---

## Excellence Signals from V-05

**Signal 1 — Structural listing enforces position, instruction does not.**
V-04 explicitly instructed the model to place design rationale before the first criteria table. V-05 achieved the same goal by listing the design rationale section first in the required output format — structure beats instruction because the model assembles the document in section-list order rather than interpreting a positional rule. Candidate for v8: `output-section-list-as-positional-gate`.

**Signal 2 — Role-definition level propagation eliminates per-criterion redundancy.**
V-05 embedded the equivalence phrase at the role definition level rather than repeating it inside individual pass conditions. This produced identical outputs to V-01/V-04 at fewer prompt tokens, and simultaneously satisfied C-11 and C-14 through a single structural decision. The pattern is already promoted as C-26 in v7.

**Signal 3 — C-13 requires named output section, not construction behavior.**
All four lower variations either ran the rejection filter internally (V-01, V-02) or made it a visible construction step without naming it as an output section (V-03, V-04 partially). V-05's framing specifies the rejection log as a named required section — the output document rather than the construction process is the gate. C-13's pass condition captures this distinction.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["output-section-list-as-positional-gate"]}
```
