Now I have everything I need. Let me score all 5 variations.

---

# Quest Score — topic-achievements — Round 2

**Rubric**: v2 (2026-03-17) — 13 criteria: 5 essential (60 pts), 3 recommended (30 pts), 5 aspirational (10 pts)

**Scoring formula**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)`

---

## Criterion Reference

| ID | Tier | What it tests |
|----|------|---------------|
| C-01 | Essential | One state per achievement |
| C-02 | Essential | Falsified named as honesty signal |
| C-03 | Essential | Artifact-grounded classification |
| C-04 | Essential | In-progress shows numeric progress |
| C-05 | Essential | Next recommended action present and specific |
| C-06 | Recommended | All 7 categories represented |
| C-07 | Recommended | Earned achievements carry dates |
| C-08 | Recommended | Locked achievements state unlock conditions |
| C-09 | Aspirational | Maturity synthesis before classification |
| C-10 | Aspirational | Falsified framed as positive signal |
| C-11 | Aspirational | State-column isolation |
| C-12 | Aspirational | Synthesis placement boundary |
| C-13 | Aspirational | Hallucination-safe evidence fallback |

---

## V-01 — Output Format (C-11 target)

**Design**: Table with `Category | Achievement | State | Evidence / Progress | Date`, directive step ordering (Step 2 synthesis before Step 3 table), no escape hatch.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Table format enforces one State column value per row; every row carries exactly one of EARNED / IN-PROGRESS / LOCKED |
| C-02 | PASS | "Falsified is the achievement that proves intellectual honesty — it means the investigation was rigorous enough to follow evidence over assumptions" — named entry with honesty framing |
| C-03 | PASS | "cite the artifact from Step 1 by namespace/skill" for EARNED; numeric count for IN-PROGRESS |
| C-04 | PASS | "numeric progress in `n of m` form (e.g., '3 of 5 namespaces covered')" explicitly required |
| C-05 | PASS | Step 4 names skill, artifact, and achievement(s) advanced |
| C-06 | PASS | "Every category must appear. If a category has no achievements, include a row with `—` in Achievement, `LOCKED` in State..." |
| C-07 | PASS | Table has Date column; EARNED rule: "Date: earned date" |
| C-08 | PASS | LOCKED rule: "Evidence: the specific unlock condition (artifact type, count, or action required)" |
| C-09 | PASS | "Before classifying any achievement, write 1-3 sentences..." — step order requires synthesis before table |
| C-10 | PASS | "frame this as an open invitation" for not-yet-earned; positive Falsified note required |
| C-11 | PASS | Dedicated State column — verification by column scan, not prose parsing |
| C-12 | FAIL | Directive step ordering only; no explicit consequence clause ("placement after fails this requirement"). Rubric requires placement boundary stronger than a presence directive. Borderline classification per variate design. |
| C-13 | FAIL | No escape hatch instruction; no guidance for uncertain evidence |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 3/5 → 6 pts

**Composite: 96** — Gold

---

## V-02 — Lifecycle Emphasis (C-12 target)

**Design**: Prose output (no table), explicit placement rule with stated failure mode ("Placement after per-category classification — including as a closing reflection — fails this requirement"), no escape hatch.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "assign exactly one state: EARNED / IN-PROGRESS / LOCKED" per achievement |
| C-02 | PASS | "The **Falsified** achievement is a named entry in the chain category... Falsified is the achievement that proves the investigation was honest" |
| C-03 | PASS | "cite the artifact from Step 1 by namespace and skill" for EARNED |
| C-04 | PASS | "state numeric progress as `n of m`" for IN-PROGRESS |
| C-05 | PASS | Step 4: skill, artifact, achievement(s) named |
| C-06 | PASS | "Write 'No achievements yet in this category' if empty" |
| C-07 | PASS | EARNED rule: "include the date earned" |
| C-08 | PASS | LOCKED rule: "state the specific unlock condition" |
| C-09 | PASS | Synthesis explicitly required in Step 2 before Step 3 categories; placement rule bolded above classification |
| C-10 | PASS | "Falsified is the achievement that proves the investigation was honest — earning it means the team followed the evidence, not their assumptions" |
| C-11 | FAIL | Prose classification format; EARNED/IN-PROGRESS/LOCKED embedded in text list, not isolated to a dedicated column |
| C-12 | PASS | Explicit boundary rule with stated failure mode: "Placement after per-category classification — including as a closing reflection — **fails this requirement**." Consequence clause is present and unambiguous. |
| C-13 | FAIL | No escape hatch; evidence citation rules provide no namespace-level fallback for uncertainty |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 3/5 → 6 pts

**Composite: 96** — Gold

---

## V-03 — Phrasing Register (C-13 target)

**Design**: Prose output (no table), directive step ordering (no explicit boundary), explicit escape hatch ("When evidence is uncertain, cite the namespace or skill only... Namespace-level evidence is always acceptable and is the safe floor").

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "assign exactly one state" per achievement |
| C-02 | PASS | Falsified named entry with "proves intellectual honesty — the investigation followed evidence, not assumptions" |
| C-03 | PASS | Evidence drawn from Step 1 artifacts; escape hatch guides toward namespace citation rather than fabrication |
| C-04 | PASS | "state numeric progress as `n of m`" |
| C-05 | PASS | Step 4 specific |
| C-06 | PASS | All 7 categories required |
| C-07 | PASS | Dates on EARNED entries |
| C-08 | PASS | Unlock conditions on LOCKED entries |
| C-09 | PASS | "Before classifying any achievement, write 1-3 sentences" — directive placement |
| C-10 | PASS | Positive Falsified framing |
| C-11 | FAIL | Prose output; no dedicated state column |
| C-12 | FAIL | Directive ordering ("Before classifying any achievement, write...") without explicit consequence clause. Borderline per variate design — same structural gap as V-01. |
| C-13 | PASS | Explicit escape hatch: "When evidence is uncertain — when you are not sure which specific artifact supports a claim — cite the namespace or skill only... Do not invent an artifact name... Namespace-level evidence is always acceptable and is the safe floor." Framed as positive permission, not just prohibition. |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 3/5 → 6 pts

**Composite: 96** — Gold

---

## V-04 — Combination: C-11 + C-12

**Design**: Table (C-11) + explicit placement boundary with consequence ("Placement after the table — or as a closing paragraph — fails this requirement"), no escape hatch.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Table enforces one State per row |
| C-02 | PASS | "Falsified is proof of intellectual honesty — the investigation was rigorous enough to follow evidence over assumptions" |
| C-03 | PASS | Evidence from Step 1 artifacts |
| C-04 | PASS | Numeric `n of m` required |
| C-05 | PASS | Step 4 specific |
| C-06 | PASS | All 7 categories with LOCKED row for empty |
| C-07 | PASS | Date column in table |
| C-08 | PASS | LOCKED evidence: specific unlock condition |
| C-09 | PASS | Placement rule explicitly requires synthesis before Step 3 table |
| C-10 | PASS | "Falsified is proof of intellectual honesty... frame it as an open invitation, not a deficit" |
| C-11 | PASS | State column in table |
| C-12 | PASS | "**Placement rule**: This paragraph must appear before the first row of the achievement table in Step 3. Placement after the table — or as a closing paragraph — **fails this requirement**." Explicit consequence clause present. |
| C-13 | FAIL | No escape hatch; no namespace-fallback guidance |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 4/5 → 8 pts

**Composite: 98** — Gold

---

## V-05 — All Three Axes: C-11 + C-12 + C-13

**Design**: Table (C-11) + explicit placement boundary ("Position determines compliance" — C-12) + escape hatch ("Namespace-level evidence is always acceptable and is the preferred safe floor" — C-13).

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Table with dedicated State column; one value per row enforced |
| C-02 | PASS | "Falsified is the achievement that proves intellectual honesty. Earning it means the investigation was rigorous enough to follow evidence over assumptions. If not yet earned, frame it as an open invitation, not a deficit." |
| C-03 | PASS | "draw only from the Step 1 artifact inventory"; escape hatch channels uncertainty toward namespace citation |
| C-04 | PASS | "numeric progress in `n of m` form" required |
| C-05 | PASS | Step 4 specific |
| C-06 | PASS | All 7 categories; LOCKED row for empty categories |
| C-07 | PASS | Date column; EARNED rule: "Date: earned date" |
| C-08 | PASS | LOCKED rule: "specific unlock condition (artifact type, count, or action required)" |
| C-09 | PASS | Placement rule requires synthesis before table: "Placement after the table fails this requirement... Position determines compliance." |
| C-10 | PASS | Mandatory framing note: "Add a mandatory framing note below the Falsified row — include this regardless of classification state." Unconditional positive framing. |
| C-11 | PASS | Dedicated State column in table |
| C-12 | PASS | "Placement after the table fails this requirement — synthesis written as a closing reflection is not acceptable regardless of its quality. **Position determines compliance.**" Strongest consequence clause of all five variations. |
| C-13 | PASS | "When evidence is uncertain, cite the namespace or skill only (e.g., 'namespace: trace'). Do not invent artifact names. Namespace-level evidence is always acceptable and is the preferred safe floor." |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 5/5 → 10 pts

**Composite: 100** — Gold

---

## Scorecard Summary

| Var | Axis | C-11 | C-12 | C-13 | Aspirational | Composite | Band |
|-----|------|------|------|------|-------------|-----------|------|
| V-05 | All three | PASS | PASS | PASS | 5/5 | **100** | Gold |
| V-04 | C-11 + C-12 | PASS | PASS | FAIL | 4/5 | **98** | Gold |
| V-01 | C-11 only | PASS | FAIL | FAIL | 3/5 | **96** | Gold |
| V-02 | C-12 only | FAIL | PASS | FAIL | 3/5 | **96** | Gold |
| V-03 | C-13 only | FAIL | FAIL | PASS | 3/5 | **96** | Gold |

**All variations pass all 5 essential criteria** and all 3 recommended criteria. The spread is entirely in the aspirational tier.

---

## Isolation Confirmation

The single-axis variations (V-01, V-02, V-03) each score identically at 96 — confirming that each new mechanism is worth exactly 2 aspirational points independently. The additive model holds: V-04 (two mechanisms) scores 98, V-05 (three mechanisms) scores 100. No synergy effects or degradation observed across the tier boundary.

---

## Excellence Signals from V-05

**Signal 1 — Principle-level consequence rule.** V-05 collapses the C-12 placement boundary to a named principle: "Position determines compliance." Prior variations stated the consequence as a case ("placement after the table fails") — V-05 names the underlying rule. This pattern is more portable: it can transfer to any step-ordering requirement without requiring a per-case failure clause. Candidate for v3 rigor criterion: *named compliance principles over per-case consequence statements*.

**Signal 2 — Unconditional Falsified framing.** V-05 marks the Falsified note as mandatory regardless of state: "Add a mandatory framing note below the Falsified row — include this regardless of classification state." All prior variations say "add a framing note" only when not earned, or as a conditional. V-05's unconditional mandate prevents silent omission in edge cases where LOCKED Falsified entries might get abbreviated in list-completion mode. Candidate for v3 architecture criterion: *Falsified framing is non-negotiable regardless of EARNED/LOCKED state*.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Principle-level consequence rule: collapsing placement boundary to a named principle ('Position determines compliance') is more portable than per-case consequence statements and transfers to any step-ordering requirement", "Unconditional Falsified framing: marking the framing note as mandatory regardless of classification state prevents silent omission when LOCKED entries are abbreviated in list-completion mode"]}
```
