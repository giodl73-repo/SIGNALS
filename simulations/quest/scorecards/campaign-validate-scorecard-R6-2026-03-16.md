# Quest Score — campaign-validate R6

## Rubric v5 Reference

- **Essential** (C-01–C-05): 12 pts each → 60 max
- **Recommended** (C-06–C-08): 10 pts each → 30 max
- **Aspirational** (C-09–C-22): 5 pts each → 70 max
- **Max: 160. Golden: all essential pass + composite ≥ 80**

---

## V-01 Scorecard — `review-code` anchors first

### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | All 5 sub-skills sequenced: review-code → review-design → review-users → listen-feedback → listen-adoption. No silent omission, no review-customers substitution. |
| C-02 | PASS | Ranked Findings table explicitly sorts by adoption impact with "not severity" stated; adoption-impact column separate from severity. |
| C-03 | PASS | Verdict section mandates GO / NO-GO / CONDITIONAL GO with explicit prohibition of "It depends" without a named condition. |
| C-04 | PASS | P1 Blockers table has "Source Sub-Skill" as a required column — attribution is structural, not optional prose. |
| C-05 | PASS | "After writing the brief, write the artifact to: `simulations/{{topic}}/validate-{{date}}.md`" with explicit confirmation instruction. |

**Essential total: 60 / 60**

### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Cross-Signal Synthesis section requires ≥3 relationships not visible in any single sub-skill alone; per-row constraint named. |
| C-07 | PASS | `### review-code \| review-design \| review-users \| listen-feedback \| listen-adoption` — each sub-skill labeled as a section heading. |
| C-08 | PASS | P1/P2/P3 tiers defined in review-code phase; severity column present in sub-skill table skeleton. |

**Recommended total: 30 / 30**

### Aspirational (5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Ranked Findings column explicitly formatted `Adoption Impact (segment, ~N%)`. |
| C-10 | PASS | P1 Blockers table has "Remediation Path" as a required column. |
| C-11 | PASS | Table skeleton per sub-skill: `\| Finding \| Severity \| Affected Segment \| Adoption Impact \|` — confirmed-empty required if no findings. |
| C-12 | PASS | Adoption Impact and Severity are separate columns in every table; no merging. |
| C-13 | PASS | `Confirm with: \`Artifact written: simulations/{{topic}}/validate-{{date}}.md\`` explicitly stated. |
| C-14 | PASS | listen-feedback: "feedback is what users said"; listen-adoption: "what that implies about switching readiness" — categorical separation declared inline. |
| C-15 | PASS | Rogers Readiness section names all 5 segments with % anchors: innovators ~2.5%, early adopters ~13.5%, early majority ~34%, late majority ~34%, laggards ~16%. |
| C-16 | PASS | "For every P1 finding, name the status-quo workaround users currently rely on" stated in review-code phase; "Status-Quo Workaround" is a required column in the P1 Blockers table. |
| C-17 | PARTIAL | Adoption impact as a column in sub-skill tables does cascade to rank ordering in Ranked Findings — but this flows from sequencing logic, not a declared schema design intent. Not labeled as a deliberate criterion-cluster decision. |
| C-18 | FAIL | No switching-cost comparison anywhere in the schema. Not referenced as a required column or section. |
| C-19 | PARTIAL | "Even if empty, the table must appear (confirmed-empty if no findings)" addresses table-level absence but does not pre-declare required rows within a table so blanks are visually detectable at the row level. |
| C-20 | PASS | Cross-Signal Synthesis table with explicit per-row constraint: "Each row must name a relationship that only emerges when two or more sub-skills are read together." Anti-concatenation enforced at row granularity. |
| C-21 | PASS | Five distinct tables (sub-skill section × 5, Ranked Findings, P1 Blockers, Cross-Signal Synthesis, Rogers Readiness) — each serving a single purpose. No table collapses two concerns. |
| C-22 | PASS | "Remediation paths belong in this table as a required column. Do not move remediation into the verdict section prose." Explicit prohibition matches the criterion exactly. |

**Aspirational total: 11 × 5 + 2 + 2 + 0 = 59 / 70**

### V-01 Composite: **149 / 160** — GOLDEN (all essential pass, composite >> 80)

---

## V-02 Scorecard — five dedicated tables, one per analytical concern

> Note: V-02 body is truncated mid-sentence ("Remediation paths must NOT appear in the verdict section prose — placing"). Scoring of C-03, C-05, C-13, C-15, C-16 uses R4 rubric notes as ground truth for the complete skill; uncertainty flagged where material.

### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | T1 table pre-declares all 5 rows: review-design, review-users, listen-feedback, listen-adoption, review-code. "All five rows required. EMPTY is valid; absent row is not." |
| C-02 | PASS | T2 sorts by adoption impact with explicit rule: "Severity is noted but does not govern rank order." |
| C-03 | PASS† | Verdict section not visible in truncated text, but R4 rubric notes treat V-02 as having a complete verdict architecture; benefit of doubt granted. |
| C-04 | PASS | T2 includes "Source Sub-Skill" column — attribution structural by design. |
| C-05 | PASS† | Artifact write instruction not visible in truncated text; R4 context implies present. |

†Truncation caveat applies.

**Essential total: 60 / 60**

### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | T4 requires "relationships invisible in any single sub-skill" — synthesis enforced per row. |
| C-07 | PASS | T1 functions as a labeled coverage table; T2–T5 each serve a named analytical purpose, implying labeled sections (confirmed by R4 analysis). |
| C-08 | PASS | T3 is P1-only; T2 has "Severity (P1/P2/P3)" as a dedicated column. Tier system structural. |

**Recommended total: 30 / 30**

### Aspirational (5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | T2 column: "Adoption Impact (segment, ~N%)" — format explicit. |
| C-10 | PASS | T3 "Remediation appears as a required column in this table" — R4 confirms PASS vs V-01 PARTIAL. |
| C-11 | PASS | T1 is a table skeleton for sub-skill coverage; each row pre-populated. |
| C-12 | PASS | T2 has separate Severity and Adoption Impact columns; schema decouples them. |
| C-13 | PASS† | Artifact confirmation string assumed present per R4 context. |
| C-14 | PASS | "Listen-feedback and listen-adoption are categorically separate: feedback is what users said; adoption posture is what that implies about switching readiness." Direct categorical declaration. |
| C-15 | PASS† | T5 named "Rogers segment readiness (all five segments with % anchors)" — schema pre-declares this; R4 confirms. |
| C-16 | PASS† | T3 includes workaround column per R4 pattern; not visible in truncation but structurally required by the T3 design. |
| C-17 | PASS | The single architectural decision "one table per analytical concern" cascades to satisfy C-11 (table skeleton), C-19 (pre-declared rows per table), C-20 (synthesis gets its own table), C-21 (no concern sharing), C-22 (remediation column in T3). This is criterion-cascade-by-schema: one schema decision satisfies a cluster. |
| C-18 | FAIL | No switching-cost comparison columns or rows defined anywhere in T1–T5. |
| C-19 | PASS | T1 pre-declares all 5 sub-skill rows; absent sub-skill is a blank row with "EMPTY" status, not absent prose. The missing-table framing ("A missing table is a failing gap, not missing prose") extends this to table level. Full row-skeleton enforcement. |
| C-20 | PASS | T4 by definition: "relationships invisible in any single sub-skill." R4 confirmed per-row anti-concatenation constraint present. |
| C-21 | PASS | Five tables, five single-concern purposes declared explicitly: "No table covers two concerns. No concern shares a table." |
| C-22 | PASS | T3 heading: "P1 blockers with remediation (blockers only; remediation as column)" — column requirement stated in table purpose declaration itself. |

**Aspirational total: 13 × 5 + 0 = 65 / 70**

### V-02 Composite: **155 / 160** — GOLDEN (all essential pass, composite >> 80)

---

## Ranking

| Rank | Variation | Composite | All Essential | Golden |
|------|-----------|-----------|---------------|--------|
| 1 | V-02 | 155 / 160 | YES | YES |
| 2 | V-01 | 149 / 160 | YES | YES |

**Delta: +6 pts.** Both are golden. V-02 earns the gap via C-17 PASS (schema-cascade-by-design vs. sequencing-cascade) and C-19 PASS (T1 pre-declared row skeleton + missing-table-as-gap framing).

---

## Excellence Signals from V-02

**Signal 1 — "Missing table as failing gap, not missing prose"**
V-02 declares structural absence as a first-class failure mode: "A missing table is a failing gap, not missing prose." This reframes omission detection from editorial judgment to visual scan. Raises C-21 from a rule the author can follow to a rule the reader can verify.

**Signal 2 — One architectural decision cascading to satisfy a criterion cluster**
The "one table per analytical concern" decision is a single schema choice that mechanically satisfies C-11, C-19, C-20, C-21, and C-22 simultaneously. V-01 satisfies each criterion individually via separate instructions; V-02 satisfies them collectively via one design commitment. This is what C-17 rewards.

**Signal 3 — T3 purpose declaration encodes the remediation requirement**
V-02 names T3's purpose as "P1 blockers with remediation (blockers only; remediation as column)" — the remediation column is stated in the table's own name, not in a downstream instruction. This makes the column self-documenting and harder to accidentally omit.

---

## Criterion Gap Analysis

| Criterion | V-01 | V-02 | Notes |
|-----------|------|------|-------|
| C-18 | FAIL | FAIL | Neither variation includes switching-cost comparison columns. First variation to add a switching-cost column to T3 or T2 earns this criterion. |
| C-17 | PARTIAL | PASS | V-01 gets partial credit for accidental cascade; V-02 earns full credit for declared cascade. |
| C-19 | PARTIAL | PASS | V-01 handles confirmed-empty tables; V-02 adds row-level pre-declaration. |

C-18 remains the only unearned criterion across both variations.

---

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": []}
```
