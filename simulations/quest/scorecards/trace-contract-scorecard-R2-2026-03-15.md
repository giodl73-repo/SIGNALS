## trace-contract v2 — Round 2 Scoring

### Rubric Reference

| ID | Weight | Category |
|----|--------|----------|
| C-01 | 12 | Essential — expected before actual |
| C-02 | 12 | Essential — explicit diff |
| C-03 | 12 | Essential — severity classification |
| C-04 | 12 | Essential — root cause hypothesis |
| C-05 | 12 | Essential — spec reference |
| C-06 | 10 | Recommended — Automate/Connectors lens |
| C-07 | 10 | Recommended — summary verdict |
| C-08 | 10 | Recommended — clean confirmation |
| C-09 | 2.5 | Aspirational — amendment suggestion |
| C-10 | 2.5 | Aspirational — pattern recognition |
| C-11 | 2.5 | Aspirational — structural field enforcement |
| C-12 | 2.5 | Aspirational — phase-gate confirmation |

R1 baseline (top variants): 90 — all essential + all recommended, 0/4 aspirational. Each variation builds on that floor.

---

### V-01 — Phase-Gate Confirmation (C-12 target)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Expected sealed before execution; `[EXPECTED SEALED]` token makes the sequencing claim explicit and traceable |
| C-02 | PASS | R1 baseline maintained — before/after pairs stated per deviation |
| C-03 | PASS | R1 baseline — severity labels on all findings |
| C-04 | PASS | R1 baseline — root cause sentence per finding |
| C-05 | PASS | R1 baseline — spec reference per finding |
| C-06 | PASS | R1 baseline — integration-level impact called out |
| C-07 | PASS | R1 baseline — summary verdict with counts + PASS/FAIL |
| C-08 | PASS | R1 baseline — affirmative on zero-finding runs |
| C-09 | FAIL | Not targeted; no amendment line present |
| C-10 | FAIL | Not targeted; no patterns section |
| C-11 | FAIL | Not targeted; prose format preserved from R1 |
| C-12 | PASS | Explicit gate question answered in document + `[EXPECTED SEALED]` written before Step 3; meets "explicit acknowledgment" requirement — sequencing alone would not |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 1/4 = 2.5

**Composite: 92.5** — Golden

---

### V-02 — Structural Field Enforcement (C-11 target)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Expected annotated "from spec" within each per-finding block |
| C-02 | PASS | `deviation :` slot forces concrete before/after at write time |
| C-03 | PASS | `severity :` slot — empty cell is visually self-announcing |
| C-04 | PASS | `root-cause :` slot — same enforcement |
| C-05 | PASS | `spec-ref :` slot — same enforcement |
| C-06 | PASS | Mandatory `connector-impact :` slot at block level; missing value is immediately visible — strengthens R1 baseline |
| C-07 | PASS | R1 baseline — summary section present |
| C-08 | PASS | R1 baseline |
| C-09 | FAIL | Not targeted; no `recommended-action` slot |
| C-10 | FAIL | Not targeted |
| C-11 | PASS | Column-aligned labeled slots (`deviation / severity / spec-ref / root-cause / connector-impact`); absent field leaves a visible empty line vs. silent prose omission |
| C-12 | FAIL | Not targeted; no gate statement present |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 1/4 = 2.5

**Composite: 92.5** — Golden

---

### V-03 — Amendment Embedded in Finding (C-09 target)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Expected section annotated before execution |
| C-02 | PASS | R1 baseline |
| C-03 | PASS | Finding template splits by severity: `breaking` / `degraded` / `cosmetic` use distinct formats |
| C-04 | PASS | R1 baseline |
| C-05 | PASS | R1 baseline |
| C-06 | PASS | R1 baseline |
| C-07 | PASS | R1 baseline |
| C-08 | PASS | R1 baseline |
| C-09 | PASS | `recommended-action` slot is fifth field of the `breaking` template, filled inline before the block closes; distinguishes spec-side vs. implementation-side resolution — block cannot be "done" with an empty slot |
| C-10 | FAIL | Not targeted |
| C-11 | FAIL | Not targeted; breaking findings gain a fifth slot but the format is not the full labeled-column structure C-11 requires across all findings |
| C-12 | FAIL | Not targeted |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 1/4 = 2.5

**Composite: 92.5** — Golden

---

### V-04 — Pattern Recognition + Amendment (C-09 + C-10 target)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | R1 baseline |
| C-02 | PASS | R1 baseline |
| C-03 | PASS | R1 baseline |
| C-04 | PASS | R1 baseline |
| C-05 | PASS | R1 baseline |
| C-06 | PASS | R1 baseline |
| C-07 | PASS | R1 baseline |
| C-08 | PASS | R1 baseline |
| C-09 | PASS | V-03 inline `recommended-action` slot carried forward; every breaking finding has a concrete resolution path |
| C-10 | PASS | Required `## Patterns` section groups findings by shared root cause with a `single-fix :` line per group; N≥2 findings → pattern declared |
| C-11 | FAIL | Not targeted; no full tabular/labeled-slot format |
| C-12 | FAIL | Not targeted |

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 2/4 = 5

**Composite: 95** — Golden

---

### V-05 — All Aspirational Combined (C-09 + C-10 + C-11 + C-12)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Expected sealed under gate lock; annotated "from spec" within each labeled block |
| C-02 | PASS | `deviation :` slot forces explicit before/after — same mechanism as V-02 |
| C-03 | PASS | `severity :` slot; empty cell self-announces |
| C-04 | PASS | `root-cause :` slot |
| C-05 | PASS | `spec-ref :` slot |
| C-06 | PASS | Mandatory `connector-impact :` slot at block level (V-02 mechanism) |
| C-07 | PASS | Summary section with severity counts + PASS/FAIL verdict |
| C-08 | PASS | Affirmative on zero-finding runs |
| C-09 | PASS | `recommended-action` slot in every `breaking` block (V-03 mechanism); distinguishes spec-side vs. implementation-side |
| C-10 | PASS | `## Patterns` section after findings with `single-fix :` line (V-04 mechanism); verified no interference — patterns section is additive, not a replacement for per-finding blocks |
| C-11 | PASS | Full labeled-slot format across all findings — `breaking` blocks carry 5 fields, `degraded`/`cosmetic` carry 4; no silent omission possible (V-02 mechanism) |
| C-12 | PASS | Gate question answered in document + `[EXPECTED SEALED]` written before Step 3 (V-01 mechanism); no mechanism interference — gate precedes finding blocks entirely |

No interference between mechanisms confirmed: gate runs before findings (C-12), slots structure findings (C-11), amendment extends breaking slots (C-09), patterns section follows findings (C-10). Execution order is clean.

**Essential:** 5/5 = 60 | **Recommended:** 3/3 = 30 | **Aspirational:** 4/4 = 10

**Composite: 100** — Golden

---

### Rankings

| Rank | Variation | Score | Aspirationals Hit |
|------|-----------|-------|-------------------|
| 1 | V-05 | 100 | C-09 + C-10 + C-11 + C-12 |
| 2 | V-04 | 95 | C-09 + C-10 |
| 3 | V-01 | 92.5 | C-12 |
| 3 | V-02 | 92.5 | C-11 |
| 3 | V-03 | 92.5 | C-09 |

---

### Excellence Signals from V-05

**1. Gate-first sequencing creates a contamination firewall**
The gate question answered + `[EXPECTED SEALED]` written as a structural token before any finding blocks appear means expected-writing and actual-inspection are physically separated in the document. Reviewers can verify the order by inspection, not trust.

**2. Labeled slots eliminate silent omissions at write time**
The C-11 format moves quality enforcement from review time to write time. An unfilled `recommended-action :` or `spec-ref :` line is visible in the draft — no post-hoc audit required. This changes the error model from "reviewer catches missing field" to "author cannot submit a blank slot."

**3. Breaking finding blocks stay open until the amendment slot is filled**
C-09's inline `recommended-action` slot, embedded in the template rather than deferred to the summary, means a breaking finding is structurally incomplete until a resolution path is named. The format enforces the analysis, not the rubric.

**4. Patterns section compresses the finding count without hiding findings**
The `## Patterns` section after per-finding blocks gives reviewers two views: granular (all findings) and compressed (root-cause groups with single-fix lines). This satisfies C-10 without replacing the detailed record — both views coexist.

**5. No mechanism interference across all four aspirationals**
The four additions operate in strictly separated phases: gate (pre-findings) → labeled blocks (per-finding) → amendment slot (per-breaking-finding) → patterns section (post-findings). A well-designed V-05 prompt can specify all four independently, and they compose without collision.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Gate-first sequencing with explicit sealed token creates contamination firewall between expected-writing and execution phases", "Labeled slot format moves missing-field detection from review time to write time — blank line is self-announcing before any reviewer sees the document", "Breaking finding block stays structurally incomplete until amendment slot is filled — format enforces the analysis", "Four aspirational mechanisms (gate, slots, amendment, patterns) operate in non-overlapping phases and compose without interference"]}
```
