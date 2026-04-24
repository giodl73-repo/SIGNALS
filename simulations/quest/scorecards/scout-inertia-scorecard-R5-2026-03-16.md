**scout-inertia R5 — Complete**

Scores against v5 rubric (ceiling 110):

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|-------------------|
| 1 | V-05 (Q-primed + bridges + roles) | **95** | A-06 + A-09 + A-10 |
| 2 | V-01 (table-dominant) | **90** | A-09 + A-10 |
| 2 | V-03 (roles-first) | **90** | A-09 + A-10 |
| 4 | V-02 (advocacy-first) | **85** | A-09 only |
| 4 | V-04 (fail-first + table) | **85** | A-09 only |

All variations pass the golden threshold (all 5 essential pass, score >= 80).

**Three findings worth noting for R6:**

1. **A-09 is now baseline** — all five variations pass it. It should be reclassified alongside A-01–A-04 in the next rubric revision.

2. **A-08 fails uniformly** — R5 variations optimized for A-09/A-10 and didn't carry forward the fail-first structural ordering (C-05 before C-01) from R4 V-05. R6 combinations should pair A-08 with the new criteria.

3. **"fail-first" vocabulary collision** — V-02 and V-04 declare `fail-first` meaning advocacy-first, not FM-section-first. A-10 catches the mismatch at a glance. R6 should enforce: declaring "fail-first" requires the C-05 section to come first structurally.

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["BRIDGE marker as structural artifact closes A-06 and A-09 simultaneously — Q3 bridge establishes FM-to-actor chain; Q4 bridge establishes FM-to-trigger chain; together they enforce the full causal sequence without requiring reviewer reconstruction", "Question-per-criterion mapping makes rubric coverage gaps structurally visible — each question corresponds to an essential criterion; an unanswered question is a visible missing criterion rather than a content deficit caught only at review", "fail-first vocabulary collision detected by A-10 — V-02 and V-04 declare fail-first in the advocacy sense while violating the structural definition; A-10 makes this discrepancy a first-class quality signal detectable before reading section content"]}
```
r cross-segment synthesis |
| A-08 | **FAIL** | Linear order: Step 1 = workaround (C-01), Step 3 = failure modes (C-05) — C-01 precedes C-05 |
| A-09 | **PASS** | Step 4 defeat table: "FM That Drives It" column explicitly required; worked example cites FM-2 by ID in the condition cell |
| A-10 | **PASS** | "Structure: table-dominant \| linear-checklist" declared at top; matches actual structure (tables throughout, linear C-01→C-02→C-05→C-04 order) |

**Score: 90** (E=50, R=30, A-09+A-10=10)

---

### V-02 — Inertia Framing: Advocacy-First with FM-Grounded Defeat

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Part 1 requires: workaround name, who owns it (role, not "the team"), duration estimate, three quantified reasons |
| C-02 | **PASS** | Part 1: migration cost (hours or days, cited to a role), training (hours + who attends), process disruption — three cost dimensions with units required |
| C-03 | **PASS** | Part 1: "Inertia threat score: HIGH (default; justify any deviation)" |
| C-04 | **PASS** | Part 3: structured defeat condition format with "Driven by: FM-[N] — [brief description]" required; falsifiability enforced by instruction and negative example |
| C-05 | **PASS** | Part 2: FM-1, FM-2 each require description, observable symptom, role most affected, frequency/volume trigger; observable + falsifiable + scoped criteria all stated |
| R-01 | **PASS** | Part 3: "Team type: [who hits this]" required per defeat condition |
| R-02 | **PASS** | Part 1: "who owns it (role, not just 'the team')"; Part 2: "Role most affected" per FM; Part 3: "Role: [who feels it]" |
| R-03 | **PASS** | Part 1: migration cost explicitly "cited to a role"; training "who attends" enforces role anchor |
| A-05 | **FAIL** | No sentence-first prompts; prose sections use structured fields but no "formulate as a sentence before entering" mechanism |
| A-06 | **FAIL** | "Part 2 — The Pivot" label implies transition but does not name what Part 1 produced or how it constrains Part 2 entries |
| A-07 | **FAIL** | Single-pass analysis; no segmentation |
| A-08 | **FAIL** | Part 1 = workaround identity + costs (C-01/C-02), Part 2 = failure modes (C-05) — C-01 precedes C-05; not fail-first by rubric definition |
| A-09 | **PASS** | Part 3: "The failure mode that makes the trigger possible (cite by ID)" explicitly required; template "Driven by: FM-[N] — [brief description]" |
| A-10 | **FAIL** | Declares "fail-first" but Section 1 is inertia advocacy (C-01/C-02 content), not a failure-mode section (C-05). A-10 pass condition: "if 'fail-first' is declared, Section 1 must be a failure-mode section." V-02 uses "fail-first" in the advocacy sense (start by advocating for status quo) but violates the structural definition (failure-mode section first). The declaration makes a structural claim it does not fulfill under rubric vocabulary. |

**Score: 85** (E=50, R=30, A-09=5)

---

### V-03 — Role Sequence: Roles-First Anchor

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Sections 1+2: role inventory then per-role workaround map with specific tool, error/quality risk, and quantified cost per role |
| C-02 | **PASS** | Section 3: per-role cost blocks with migration time (hours/days), training (hours + content), in-flight disruption per role |
| C-03 | **PASS** | Section 3: "Inertia threat score for this feature: HIGH (default). Note any role where the switching cost is lower than average." |
| C-04 | **PASS** | Section 5: defeat conditions each require "FM that makes it possible: FM-[N]" and falsifiable threshold; sentiment triggers explicitly rejected |
| C-05 | **PASS** | Section 4: FM-1, FM-2 with scenario, observable symptom, primary role affected, volume/frequency trigger; "Generic pain points ('slow') do not pass" |
| R-01 | **PASS** | Section 5: "Team type most exposed" required per defeat condition |
| R-02 | **PASS** | Section 1 role inventory forces specific role names first; all subsequent sections reference those roles explicitly |
| R-03 | **PASS** | Section 3 is fully per-role; each cost block headed by the role name declared in Section 1 |
| A-05 | **FAIL** | No sentence-first prompts before tables; Section 1 table entered cold |
| A-06 | **FAIL** | No explicit bridge instructions; sections flow logically by lifecycle but without named transition constraints |
| A-07 | **FAIL** | Sequential per-role analysis, not multi-segment A/B synthesis with ID-citation columns |
| A-08 | **FAIL** | Section 2 = per-role workaround (C-01), Section 4 = failure modes (C-05) — C-01 precedes C-05 |
| A-09 | **PASS** | Section 5: "FM that makes it possible: FM-[N]" is a required field in the defeat condition block format |
| A-10 | **PASS** | "Structure: role-anchored \| per-role workaround \| FM-by-role \| defeat by team type" declared at top; matches actual section order exactly |

**Score: 90** (E=50, R=30, A-09+A-10=10)

---

### V-04 — Combined: Fail-First + Table-Dominant

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Phase 2: workaround summary table (name, roles, frequency, time cost, error rate, scale ceiling, time in use) — all dimensions present |
| C-02 | **PASS** | Phase 3: cost table with Role column; "Magnitude column must contain a unit (hours, days, %, sprint fraction). 'Significant' without a unit fails." |
| C-03 | **PASS** | Phase 1: "Inertia threat score: HIGH (default). State any conditions that would lower this score, with quantified justification." |
| C-04 | **PASS** | Phase 5: defeat table with FM column pre-labeled "FM-[N]:" in each row; "Condition column: must be falsifiable. 'Teams switch when they see value' fails." |
| C-05 | **PASS** | Phase 4: FM-1, FM-2 with observable symptom and volume/frequency trigger columns; worked example "CSV export silently truncates rows over 65,536 — no error message" |
| R-01 | **PASS** | Phase 5: "Team Type" column in defeat table |
| R-02 | **PASS** | Phase 2: "Primary roles" row; Phase 4: "Affected Role" column; Phase 5: "Role Most Affected" column |
| R-03 | **PASS** | Phase 3: "Role" column present; basis field required per row |
| A-05 | **FAIL** | Phase 1 is prose advocacy; subsequent phases go directly to tables with no sentence-first prompts |
| A-06 | **FAIL** | No explicit bridge instructions between phases |
| A-07 | **FAIL** | Single-pass analysis; no segmentation |
| A-08 | **FAIL** | Phase 1+2+3 = inertia advocacy + workaround + costs (C-01/C-02), Phase 4 = failure modes (C-05) — C-01 precedes C-05; not fail-first by rubric definition |
| A-09 | **PASS** | Phase 5: "FM That Drives It" column with "FM-[N]:" pre-filled in each row — strongest FM-citation enforcement of all R5 variations; pre-filled cell makes omission structurally visible before submission |
| A-10 | **FAIL** | Declares "fail-first" but Phase 1 = inertia case prose (C-01/C-02 content), not failure modes (C-05). Same vocabulary collision as V-02: "fail-first" used in advocacy sense, not structural FM-first sense. A-10 detects the mismatch at a glance. |

**Score: 85** (E=50, R=30, A-09=5)

---

### V-05 — Combined: Question-Primed + Bridges + Role Sequence

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS** | Q1: "two roles, each with a named workaround and a specific quality risk" — minimum answer contract with worked example showing role + tool + specific failure |
| C-02 | **PASS** | Q2: "two roles with quantified migration time and one in-flight risk per role"; units required (hours, days, sprint); inertia threat score embedded in Q2 |
| C-03 | **PASS** | Q2: "Inertia threat score: HIGH (state any exception with justification)" |
| C-04 | **PASS** | Q4: each defeat condition requires trigger (falsifiable threshold), FM-[N] citation, team type, role who owns the decision; minimum answer contract with worked example |
| C-05 | **PASS** | Q3: 2+ failure modes each with observable symptom, role who sees it first, volume/frequency trigger condition; BRIDGE statement required per FM |
| R-01 | **PASS** | Q4: "Which team type is most exposed to this trigger?" required per defeat condition |
| R-02 | **PASS** | Q1: role names required; Q2: costs by role; Q3: "who sees it first (the role)"; Q4: "which role owns the decision to switch" |
| R-03 | **PASS** | Q2: per-role quantified migration time explicitly in minimum answer contract; "two roles with quantified migration time" |
| A-05 | **FAIL** | No tables; Q sections use prose with minimum answer contracts. A-05 targets "each table... preceded by a prose-first prompt" — the mechanism is absent. Question-answer format serves the same cognitive function but does not satisfy the criterion's table-specific scope. |
| A-06 | **PASS** | Q3: explicit BRIDGE format "FM-[N] exposes [Role] because [mechanism], costing [quantified impact]" — names upstream FM and downstream role+cost constraint. Q4: explicit BRIDGE format "T-[N] is possible because FM-[N] [describe mechanism]" — names upstream FM and downstream enabling mechanism. Both bridges name prior output and what it constrains. |
| A-07 | **FAIL** | Sequential single-pass questions; Q5 synthesis cites IDs from one pass — not multi-segment A/B synthesis with cross-segment ID-citation columns |
| A-08 | **FAIL** | Q1 = who uses the workaround (C-01), Q3 = where it breaks (C-05) — C-01 precedes C-05; not fail-first |
| A-09 | **PASS** | Q4: "Which failure mode makes this trigger possible? (cite FM-[N])" required per defeat condition; BRIDGE format "T-[N] is possible because FM-[N]..." enforces FM citation at two layers — field requirement AND required prose artifact |
| A-10 | **PASS** | "Structure: question-primed \| role-anchored \| bridge-marked" declared at top; matches actual structure: Q-framed sections, roles established in Q1, BRIDGE markers present in Q3 and Q4 as required artifacts |

**Score: 95** (E=50, R=30, A-06+A-09+A-10=15)

---

### Summary

| Variation | Axes | Essential | Recommended | Aspirational-new | **Score** | Golden |
|-----------|------|-----------|-------------|------------------|-----------|--------|
| V-05 | Q-primed + bridges + roles | 5/5 | 3/3 | A-06+A-09+A-10 = 3/6 | **95** | YES |
| V-01 | Table-dominant | 5/5 | 3/3 | A-09+A-10 = 2/6 | **90** | YES |
| V-03 | Roles-first | 5/5 | 3/3 | A-09+A-10 = 2/6 | **90** | YES |
| V-02 | Fail-first (advocacy) | 5/5 | 3/3 | A-09 = 1/6 | **85** | YES |
| V-04 | Fail-first + table | 5/5 | 3/3 | A-09 = 1/6 | **85** | YES |

**Ranking**: V-05 > V-01 = V-03 > V-02 = V-04

---

### Systematic Findings

**A-09 is now structural baseline.** All five variations pass A-09. Every R5 variation was designed with an FM-citation requirement in the defeat conditions section (column, field, or BRIDGE statement). A-09 has graduated from differentiator to expected baseline — consistent with how A-01 through A-04 became baseline before R5. If R6 introduces a new criterion, A-09 should be reclassified to baseline.

**A-08 fails in all five variations.** None implement fail-first ordering structurally (C-05 before C-01). R5 variations focused on A-09 and A-10 and did not carry forward the A-08 structural pattern established by R4 V-05 (two-pass segmented with fail-first within each pass). R6 should test combinations that include A-08 with the R5 criteria.

**"fail-first" vocabulary collision (V-02, V-04).** Both declare "fail-first" in their structure declarations but use the term in the advocacy sense (start by making the case FOR the status quo) rather than the structural sense (failure-mode section before workaround-identity section). A-10 detects this discrepancy at a glance: the declared technique does not match the rubric-defined structural behavior. This is the quality signal A-10 was designed to surface.

---

### Excellence Signals from V-05

**1. BRIDGE marker closes both A-06 and A-09 simultaneously**
V-05 requires two BRIDGE statements: Q3 bridges FM to role+cost ("FM-[N] exposes [Role] because [mechanism], costing [impact]"); Q4 bridges defeat condition to FM mechanism ("T-[N] is possible because FM-[N] [describe mechanism]"). Together they enforce the full causal chain — FM symptom → named actor → quantified cost → FM-grounded trigger — as required prose artifacts, not implicit connections a reviewer must reconstruct. A-06 and A-09 reinforce each other: without A-06 bridges (V-01, V-03), A-09 FM citations exist in a column but the mechanism linking FM to actor to trigger is left implicit.

**2. Question-per-criterion mapping makes gaps visible as unanswered questions**
Q1=C-01, Q2=C-02+C-03, Q3=C-05, Q4=C-04. Each question maps directly to an essential criterion. A missing criterion is an unanswered question — structurally visible without reviewing section content. Other variations require the reviewer to verify criterion coverage by cross-referencing table columns; V-05 makes criterion presence or absence observable at question level.

**3. "fail-first" vocabulary collision is a first-class quality signal at R5**
V-02 and V-04 both declare "fail-first" while implementing advocacy-first ordering. The declarations create structural claims that A-10 flags without reading the full output. This finding establishes a vocabulary standard for R6: any variation that declares "fail-first" must implement the A-08 structural criterion (C-05 section before C-01 section), not merely advocate for the status quo before pivoting to failures.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["BRIDGE marker as structural artifact closes A-06 and A-09 simultaneously — Q3 bridge establishes FM-to-actor chain; Q4 bridge establishes FM-to-trigger chain; together they enforce the full causal sequence without requiring reviewer reconstruction", "Question-per-criterion mapping makes rubric coverage gaps structurally visible — each question corresponds to an essential criterion; an unanswered question is a visible missing criterion rather than a content deficit caught only at review", "fail-first vocabulary collision detected by A-10 — V-02 and V-04 declare fail-first in the advocacy sense while violating the structural definition; A-10 makes this discrepancy a first-class quality signal detectable before reading section content"]}
```
