Written to `simulations/quest/variations/campaign-validate-variations-R5-2026-03-16.md`.

---

## campaign-validate R5 Variations

**Context and axis choices:**

R4 root cause: both variations used `review-customers` (not `review-code`) — unconditional C-01 fail. The scorecard said the winning move is "V-01's synthesis pipeline + V-02's table skeleton." V5 adds three new criteria to target: C-20 (synthesis table with per-row anti-concatenation), C-21 (one-table-per-concern), C-22 (remediation as column not verdict prose).

---

### V-01 — C-01 Fix on R4 V-01 Pipeline
**Axis:** Single — sub-skill list correction (`review-code` replaces `review-customers` everywhere).  
**Hypothesis:** R4 V-01 was 122/145 with one essential failure. This is the minimum-change path: preserve adoption-first sequencing, merge-prohibition, column completeness, synthesis pipeline exactly, correct the sub-skill list. Expected ceiling: 134+.

### V-02 — Synthesis Table Axis (C-20)
**Axis:** Single — cross-signal synthesis encoded as a dedicated table with a named per-row anti-concatenation constraint. The constraint operates at row granularity, not document level.  
**Hypothesis:** R4 V-01 passed C-06 (synthesis present) but would fail C-20 (prose synthesis ≠ table with per-row constraint). Encoding the table + the per-row test makes each synthesis relationship independently assessable. Unlocks C-20 at zero cost to other criteria.

### V-03 — Remediation Column Axis (C-22)
**Axis:** Single — remediation paths are a required column in the P1 blockers table. The verdict section references T3 row numbers and explicitly does not restate remediations.  
**Hypothesis:** R4 V-01 scored C-10 PARTIAL (remediation implied in CONDITIONAL GO framing only). C-22 requires a column position. Moving remediations to a column also upgrades C-10 from PARTIAL to PASS. The verdict becomes a reference pointer, not a remediation container.

### V-04 — One-Table-Per-Concern Schema Declaration (C-21)
**Axis:** Single — the 5-table schema is declared upfront as an explicit constraint before execution instructions. Each table has a stated "one concern" label. Combining concerns is a named schema violation.  
**Hypothesis:** C-21 is not just about what the output looks like — it's about whether the schema constraint is stated. Declaring it forces the author to see missing tables as schema violations rather than absent prose. Also creates the C-17 cascade automatically: T5 (Rogers rows + columns) satisfies C-09/C-15/C-16/C-18 as a single schema decision.

### V-05 — Full Integration (C-01 fix + adoption-first + 5-table schema + C-20 + C-21 + C-22)
**Axis:** Combined — R4 V-01 excellence (adoption-first sequencing, complete pipeline) + R4 V-02 excellence (5-table skeleton, pre-declared Rogers rows) + all three v5 criteria (synthesis table with per-row constraint, one-concern-per-table declaration, remediation as column). The schema cascade note in T5 explicitly encodes the C-17 pattern.  
**Hypothesis:** This is the composite the R4 scorecard called "near-maximum on both tiers," extended with v5 additions. Maximum theoretical score: 160. Every essential, recommended, and aspirational criterion has a structural mechanism targeting it.
CAL SEPARATION DECLARATION: listen-feedback and listen-adoption are categorically
different questions. listen-feedback is retrospective prediction -- how will customers react
on first encounter? listen-adoption is predictive modeling -- which segments will adopt and
when? Do NOT merge these sections. Do not use Phase 1 findings as evidence in Phase 2.

For each of the 12 customer personas:
- State their initial reaction (positive / neutral / negative)
- Predict their NPS score (-10 to +10)
- Identify the primary objection or friction point

Aggregate: compute the weighted NPS prediction. Flag any segment with NPS < 0.

GATE: 12 persona reactions documented; categorical separation from Phase 1 maintained.

---

### Phase 3 -- review-users

Run the 5-persona usability walkthrough for {{topic}}.

For each of 5 personas:
- Walk through the primary user flow step by step
- Score each friction point: P1 (blocks usage), P2 (degrades usage), P3 (polish item)
- Attribute each finding to a specific design decision

Cross-persona synthesis: which finding appears across 3+ personas? These are systemic.

GATE: 5 personas complete; P1/P2/P3 scoring applied to every finding.

---

### Phase 4 -- review-design

Run the 6-discipline design review for {{topic}}.

Disciplines: UX, Architecture, Security, Performance, Accessibility, Operational.
For each discipline: state the expert's lens, top finding, and severity (P1/P2/P3).

GATE: All 6 disciplines documented; no discipline silently skipped.

---

### Phase 5 -- review-code

Run the multi-discipline code review for {{topic}}.

For each discipline relevant to this feature (minimum 3):
- State the file or component reviewed
- Note the finding with severity (P1/P2/P3)
- Attribute to a specific code pattern or implementation decision

GATE: Code review complete; at least 3 disciplines represented.

---

### Ranked Findings Table

Rank ALL findings from all five sub-skills by adoption impact -- not by severity.
Adoption impact = how much does this finding reduce the adoption probability of the Early Majority?

| Rank | Finding | Source Sub-Skill | Severity | Adoption Impact | Segment Affected (~N%) | Status-Quo Workaround | Switching Cost |
|------|---------|-----------------|----------|-----------------|------------------------|----------------------|----------------|
| 1 | ... | ... | P1/P2/P3 | High/Med/Low | Early Majority (~35%) | ... | ... |

Rules:
- Severity is informational -- it does not govern rank order
- All columns are required for every row -- not just P1s
- "Status-Quo Workaround" and "Switching Cost" apply to every finding row

---

### Cross-Signal Synthesis

Identify cross-signal relationships: findings that are only visible when two or more sub-skills
are considered together. Each observation must:
- Name the two sub-skills whose outputs interact
- State the relationship (not a summary of either output)
- Explain why this relationship is not visible in either signal alone

Anti-concatenation rule: a synthesis observation that could have been written from a single
sub-skill's output alone is not synthesis -- rewrite or remove it.

---

### Go / No-Go Verdict

Declare one of:
- **GO**: No P1 finding blocks the Early Majority segment. Feature may ship.
- **NO-GO**: One or more P1 findings block the Early Majority. Do not ship.
- **CONDITIONAL GO**: P1 findings exist but each has a defined remediation path.
  Ship is blocked until all conditions are confirmed complete.
  Name each condition explicitly.

Top-3 blockers (or all if fewer than 3): attribute each to its source sub-skill.

---

### Artifact Write

Write the complete validation brief to: `simulations/{{topic}}/validate-{{date}}.md`

Confirm with: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`

---

## V-02 -- Synthesis Table Axis (C-20)

**Variation axis:** Output format -- the cross-signal synthesis section becomes a dedicated
table with an explicit per-row anti-concatenation constraint. All other elements from V-01
preserved. The table form makes each synthesis relationship discrete and independently testable.

**Hypothesis:** R4 V-01 included cross-signal synthesis as a prose section with a document-level
anti-concatenation rule (C-06 pass, C-20 fail). C-20 requires the constraint to operate at row
granularity, not document level. Encoding synthesis as a table where each row must satisfy a
named per-row constraint will pass C-20 while adding no structural cost to the existing pipeline.
This is the minimum change to unlock C-20 without disrupting C-06 through C-19.

---

Validate the design for: {{topic}} against real users and customers.

Run all five sub-skills in this order. Write findings into the sections below.

Sub-skills (required, all five, no substitutions):
1. listen-adoption   -- adoption curve, Rogers segments, % anchors
2. listen-feedback   -- 12-persona NPS prediction
3. review-users      -- 5-persona P1/P2/P3 walkthrough
4. review-design     -- 6-discipline expert review
5. review-code       -- file-level multi-discipline review (NOT review-customers)

---

### Phase execution

**listen-adoption**: Run the Rogers adoption curve for {{topic}}.

For each segment (Innovators ~5%, Early Adopters ~15%, Early Majority ~35%,
Late Majority ~30%, Laggards ~15%):
- Adoption condition, status-quo workaround, switching cost, chasm risk

All five segments required. % anchors are baselines -- adjust to feature context.

**listen-feedback**: Run the pre-ship NPS simulation.

CATEGORICAL SEPARATION: listen-feedback predicts first-encounter reaction (retrospective).
listen-adoption models long-term segment adoption (predictive). Keep these separate.

Per persona: initial reaction, NPS prediction (-10 to +10), primary objection.
Aggregate weighted NPS. Flag NPS < 0 segments.

**review-users**: 5-persona usability walkthrough.

Per persona: primary flow trace, friction scoring (P1 blocks / P2 degrades / P3 polish),
cross-persona synthesis for systemic findings (3+ personas).

**review-design**: 6-discipline review (UX, Architecture, Security, Performance,
Accessibility, Operational). Per discipline: expert lens, top finding, P1/P2/P3.

**review-code**: Multi-discipline code review. Minimum 3 disciplines. Per discipline:
file/component, finding, P1/P2/P3, code pattern attribution.

---

### Ranked Findings Table

| Rank | Finding | Source Sub-Skill | Severity | Adoption Impact | Segment (~N%) | Workaround | Switching Cost |
|------|---------|-----------------|----------|-----------------|---------------|------------|----------------|

Rank 1 = highest adoption impact. Severity is informational. All columns required per row.

---

### P1 Blockers with Remediation Paths

| # | Blocker | Source Sub-Skill | Workaround | Remediation Path | Effort |
|---|---------|-----------------|------------|-----------------|--------|

Remediation Path is required for every row. If this table is empty, no P1 blockers exist.

---

### Cross-Signal Synthesis Table

| # | Sub-Skills Spanned | Relationship | Why Not Visible in Either Sub-Skill Alone |
|---|--------------------|-------------|-------------------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

PER-ROW ANTI-CONCATENATION CONSTRAINT: Each row must satisfy the following test --
"Could this row have been written from reading either sub-skill's output in isolation?"
If yes: rewrite the row to name the emergent relationship, or remove it.

A row that summarizes a single sub-skill fails.
A row that notes the same finding appears in two sub-skills, without naming what the
co-occurrence reveals, fails.
A row that names an implication visible only when both signals are combined passes.

Minimum 3 rows. Each row is independently testable against the per-row constraint.

---

### Rogers Adoption Curve

| Segment | ~% of Base | Adoption Condition | Workaround Today | Switching Cost | Chasm Risk |
|---------|-----------|-------------------|-----------------|----------------|------------|
| Innovators | ~5% | | | | |
| Early Adopters | ~15% | | | | |
| Early Majority | ~35% | | | | |
| Late Majority | ~30% | | | | |
| Laggards | ~15% | | | | |

All five rows mandatory. A blank row is a visible gap.

---

### Go / No-Go Verdict

After all phases complete, inspect the P1 blockers table:
- **GO**: P1 blockers table is empty. No finding blocks the Early Majority.
- **NO-GO**: P1 blockers table has rows with missing remediation paths.
- **CONDITIONAL GO**: P1 blockers table has rows; all remediation paths specified.
  "Ship blocked until [blocker] is resolved via [remediation path]."

Top-3 blockers: name source sub-skill and reference the P1 blockers table row.

---

### Artifact Write

Write the complete validation brief to: `simulations/{{topic}}/validate-{{date}}.md`

Confirm with: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`

---

## V-03 -- Remediation Column Axis (C-22)

**Variation axis:** Lifecycle emphasis -- remediation paths move from the verdict section
(CONDITIONAL GO prose) to a required column in a dedicated P1 blockers table. The verdict
section references the table by row number instead of restating remediation paths.

**Hypothesis:** R4 V-01 scored C-10 PARTIAL because remediation was "implied only in
CONDITIONAL GO verdict framing" rather than as a column. C-22 requires remediation to appear
as a required column in a dedicated blockers table, not as verdict prose. This axis targets
the gap between C-10 PARTIAL and C-10 PASS, and simultaneously unlocks C-22 (new in v5).
The verdict section becomes a reference mechanism, not a remediation container.

---

Validate the design for: {{topic}} against real users and customers.

Sub-skills (five required, in this order):
1. review-design     -- 6-discipline expert review
2. review-users      -- 5-persona usability walkthrough
3. review-code       -- file-level code review (NOT review-customers)
4. listen-feedback   -- pre-ship NPS prediction, retrospective
5. listen-adoption   -- Rogers adoption curve, predictive

All five sub-skills are required. review-code is required; review-customers is not in this
campaign. Silent omission of any sub-skill fails unconditionally.

---

### Per-Sub-Skill Findings

Produce a labeled section per sub-skill. Use the sub-skill name as the section header.

**review-design**: 6 disciplines -- UX, Architecture, Security, Performance, Accessibility,
Operational. Per discipline: expert lens, top finding, P1/P2/P3 severity.
All 6 disciplines required. No discipline silently skipped.

**review-users**: 5-persona walkthrough. Per persona: primary flow trace, P1/P2/P3 scoring,
attribution to a specific design decision. Cross-persona synthesis: findings in 3+ personas
are systemic.

**review-code**: Multi-discipline code review. Minimum 3 disciplines. Per discipline:
file or component, finding, P1/P2/P3, code pattern attribution.

CATEGORICAL SEPARATION REQUIRED: The following two sub-skills are categorically different.
- listen-feedback = how customers react on first encounter (retrospective NPS prediction)
- listen-adoption = which Rogers segments adopt and when (predictive adoption modeling)
Do not merge findings. Do not reference Phase 5 data in Phase 4 or vice versa.

**listen-feedback**: 12 customer personas. Per persona: initial reaction, NPS prediction
(-10 to +10), primary objection. Aggregate weighted NPS. Flag NPS < 0 per segment.

**listen-adoption**: For each Rogers segment (Innovators ~5%, Early Adopters ~15%,
Early Majority ~35%, Late Majority ~30%, Laggards ~15%): adoption condition, today's
workaround, switching cost, chasm risk. All five segments required with % anchors.

---

### Ranked Findings Table

Collect all findings from all five sub-skills. Rank by adoption impact.
A finding that blocks the Early Majority outranks a P1 finding that affects only Innovators.

| Rank | Finding | Source Sub-Skill | Severity | Adoption Impact | Segment Affected (~N%) | Status-Quo Workaround | Switching Cost |
|------|---------|-----------------|----------|-----------------|------------------------|----------------------|----------------|

Severity is informational. Adoption impact governs rank. All columns required per row.

---

### P1 Blockers Table (with Remediation Column)

List every P1 finding here. Remediation paths are a required column in this table.
They are not prose in the verdict section. Every P1 row receives a remediation path.

| # | Blocker | Source Sub-Skill | Status-Quo Workaround | Remediation Path | Effort |
|---|---------|-----------------|----------------------|-----------------|--------|

Rules:
- Remediation Path column is required for every row, not optional for "easy" blockers.
- The verdict section references this table by row number. It does not restate remediations.
- A row with a blank Remediation Path cell blocks CONDITIONAL GO as a verdict option.
- If this table is empty, GO is the only available verdict.

---

### Rogers Adoption Curve

| Segment | ~% of Base | Adoption Condition | Workaround Today | Switching Cost | Chasm Risk |
|---------|-----------|-------------------|-----------------|----------------|------------|
| Innovators | ~5% | | | | |
| Early Adopters | ~15% | | | | |
| Early Majority | ~35% | | | | |
| Late Majority | ~30% | | | | |
| Laggards | ~15% | | | | |

All five rows mandatory.

---

### Cross-Signal Synthesis

Identify findings visible only when two or more sub-skills are considered together.
Each observation: name the sub-skills, name the relationship, explain why it was not
visible in either signal alone.

Anti-concatenation rule: a synthesis observation derivable from one sub-skill alone is
not synthesis. Rewrite it to name the emergent insight, or remove it.

---

### Go / No-Go Verdict

Inspect the P1 blockers table:
- **GO**: P1 blockers table is empty.
- **NO-GO**: One or more P1 rows have an empty Remediation Path cell.
- **CONDITIONAL GO**: All P1 rows have remediation paths. Ship condition:
  "Blocked until rows [#] are resolved per remediation paths in the blockers table."

Top-3 blockers: reference the row number from the P1 blockers table and name the source
sub-skill. Do not restate remediation paths here -- they are in the table.

---

### Artifact Write

Write the complete validation brief to: `simulations/{{topic}}/validate-{{date}}.md`

Confirm with: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`

---

## V-04 -- One-Table-Per-Concern Schema Declaration (C-21)

**Variation axis:** Output format -- the full table schema is declared at the top of the
prompt as an explicit design constraint, before any execution instructions. Each table
covers exactly one analytical concern. The schema declaration is the structural gate:
combining concerns into one table is a named schema violation.

**Hypothesis:** C-21 requires that "each analytical concern has its own dedicated table
with a single focus." Making the schema explicit as a constraint (not just an emergent
property of the instructions) forces the author to see missing tables as schema violations
rather than absent prose. This also sets up C-17 cascade: T5 (Rogers rows + required
columns) simultaneously satisfies C-09, C-15, C-16, and C-18 as a single schema decision.
The schema declaration approach makes C-19 (pre-declared rows) automatic for T1 and T5.

---

Validate the design for: {{topic}} against real users and customers.

---

### Output Schema

This validation brief uses a one-table-per-analytical-concern architecture.
Each concern has exactly one table. No table combines two concerns.
Adding a concern to an existing table is a schema violation.

| Table | Name | Analytical Concern | Required Rows |
|-------|------|--------------------|---------------|
| T1 | Sub-skill execution status | Did each sub-skill complete? | 5 rows (one per sub-skill) |
| T2 | Ranked findings | What did we find, by adoption impact? | One per finding |
| T3 | P1 blockers + remediation | What blocks ship, and how to fix it? | One per P1 finding |
| T4 | Cross-signal synthesis | What relationships exist across sub-skills? | Min 3 |
| T5 | Rogers adoption curve | How does each segment adopt? | 5 rows (one per segment) |

The schema is the output contract. Declare it in the artifact. Populate it through execution.

---

### Sub-Skills (required, adoption-first order)

| Order | Sub-Skill | Role | Feeds |
|-------|-----------|------|-------|
| 1 | listen-adoption | Adoption modeling -- Rogers, chasm, % anchors | T1, T2, T5 |
| 2 | listen-feedback | Pre-ship NPS prediction -- 12 personas | T1, T2, T3 |
| 3 | review-users | 5-persona usability walkthrough -- P1/P2/P3 | T1, T2, T3 |
| 4 | review-design | 6-discipline expert review -- P1/P2/P3 | T1, T2, T3 |
| 5 | review-code | File-level code review -- min 3 disciplines | T1, T2, T3 |

REQUIRED: review-code is sub-skill 5. review-customers is NOT in this schema.
A T1 row for review-customers is a schema violation. Including review-customers or omitting
review-code fails the campaign unconditionally.

CATEGORICAL SEPARATION: listen-feedback and listen-adoption are separate sub-skills with
separate T1 rows and separate analytical concerns. listen-feedback = first-encounter reaction.
listen-adoption = long-term adoption modeling. Do not merge their findings.

---

### T1 -- Sub-Skill Execution Status

| Sub-Skill | Order | Status | Feeds |
|-----------|-------|--------|-------|
| listen-adoption | 1 | PENDING | T2, T5 |
| listen-feedback | 2 | PENDING | T2, T3 |
| review-users | 3 | PENDING | T2, T3 |
| review-design | 4 | PENDING | T2, T3 |
| review-code | 5 | PENDING | T2, T3 |

Execute each sub-skill. Update its T1 row to COMPLETE before proceeding to the next.
A PENDING row at verdict time is a schema violation.

Execution notes:
- **listen-adoption**: Populate T5 directly during execution.
- **listen-feedback**: 12 personas, NPS per persona, aggregate NPS.
- **review-users**: 5 personas, P1/P2/P3 per friction point, cross-persona synthesis.
- **review-design**: 6 disciplines (UX, Architecture, Security, Performance, Accessibility, Operational).
- **review-code**: Minimum 3 disciplines, file/component, P1/P2/P3.

---

### T2 -- Ranked Findings

One concern: what did we find, ordered by adoption impact?

| Rank | Finding | Source | Severity | Adoption Impact | Segment (~N%) | Workaround | Switching Cost |
|------|---------|--------|----------|-----------------|---------------|------------|----------------|

Rules:
- Rank 1 = highest adoption impact. Severity is informational.
- All columns required for every row -- "Workaround" and "Switching Cost" apply to P2/P3 as well.
- Do not add synthesis rows here (synthesis is T4's concern).

---

### T3 -- P1 Blockers with Remediation Paths

One concern: what blocks ship, and what fixes it?

| # | Blocker | Source | Workaround | Remediation Path | Effort | Owner |
|---|---------|--------|------------|-----------------|--------|-------|

Rules:
- Every P1 finding from T2 appears here.
- Remediation Path is a required column -- every row has one.
- The verdict references T3 row numbers. It does not restate remediation paths in prose.
- This table is the only location for remediation paths. Including them in the verdict
  section violates the one-concern-per-table schema.

---

### T4 -- Cross-Signal Synthesis

One concern: what relationships exist across sub-skills?

| # | Sub-Skills Spanned | Relationship | Why Not Visible in Either Sub-Skill Alone | Implication |
|---|--------------------|-------------|-------------------------------------------|-------------|

PER-ROW ANTI-CONCATENATION CONSTRAINT: Each row must name a relationship that could not
be written from reading either sub-skill in isolation. Test: "If I removed one sub-skill
from the evidence, could I still write this row?" If yes, rewrite or remove it.

No finding summaries, no restatements of T2 data, no single-sub-skill observations.
Minimum 3 rows. Each row is independently testable.

---

### T5 -- Rogers Adoption Curve

One concern: how does each segment adopt? This is the only location for Rogers data.

| Segment | ~% of Base | Adoption Condition | Workaround Today | Switching Cost | Chasm Risk |
|---------|-----------|-------------------|-----------------|----------------|------------|
| Innovators | ~5% | | | | |
| Early Adopters | ~15% | | | | |
| Early Majority | ~35% | | | | |
| Late Majority | ~30% | | | | |
| Laggards | ~15% | | | | |

All five rows mandatory. % anchors are baselines. Do not duplicate segment data in T2.
T5 encodes C-09, C-15, C-16, and C-18 simultaneously: the schema decision (five pre-declared
rows + required columns for workaround and switching cost) cascades all four criteria.

---

### Verdict

After T1 through T5 are complete:

- **GO**: T3 is empty; no P1 findings. Early Majority adoption condition in T5 is defined.
- **NO-GO**: T3 has rows where Remediation Path is blank or unspecified.
- **CONDITIONAL GO**: T3 has rows; all Remediation Path cells are specific and actionable.
  State: "Ship blocked until T3 row(s) [#] resolved per remediation paths in T3."

Top-3 blockers: reference T3 row numbers and source sub-skills.
Do not restate remediation paths -- they are in T3.

---

### Artifact Write

Write the complete validation brief to: `simulations/{{topic}}/validate-{{date}}.md`
Include T1 through T5 and the verdict.

Confirm with: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`

---

## V-05 -- Full Integration: Adoption-First + 5-Table Schema + C-20 + C-21 + C-22

**Variation axis:** Combined -- adoption-first sequencing (R4 V-01 excellence pattern),
5-table pre-declared schema (R4 V-02 excellence pattern), synthesis table with per-row
anti-concatenation (C-20), one-table-per-analytical-concern (C-21), remediation as
required column not verdict prose (C-22), C-01 fix (review-code not review-customers).

**Hypothesis:** The R4 scorecard stated explicitly: "A composite variation combining V-01's
synthesis pipeline with V-02's table skeleton would score near-maximum on both tiers." V-05
is that composite, extended with v5's three new criteria. The schema declares all five tables
upfront. T4 is a synthesis table with a per-row anti-concatenation constraint (C-20). Each
table covers exactly one concern and states it (C-21). T3 has a Remediation Path column and
the verdict references T3 by row number, not prose (C-22). All v4 cascade patterns preserved:
T5 Rogers rows + columns cascade C-09/C-15/C-16/C-18 simultaneously (C-17). The adoption-first
execution order frames all downstream findings as adoption barriers from the start (C-02).

---

Validate the design for: {{topic}} against real users and customers.

---

### Output Schema Declaration

Five tables. One analytical concern per table. No table combines two concerns.
Combining concerns violates the schema. A missing table is a visible gap.

| Table | Name | Analytical Concern (single) |
|-------|------|------------------------------|
| T1 | Sub-skill status | Did each sub-skill complete? |
| T2 | Ranked findings | What did we find, ordered by adoption impact? |
| T3 | P1 blockers + remediation | What blocks ship and what fixes it? |
| T4 | Cross-signal synthesis | What relationships exist only across sub-skills? |
| T5 | Rogers adoption curve | How does each segment adopt? |

Declare this schema in the artifact. Populate through execution.

---

### Sub-Skills (execution order: adoption-first)

| Order | Sub-Skill | Why This Order |
|-------|-----------|----------------|
| 1 | listen-adoption | Frame all findings as adoption barriers from the start |
| 2 | listen-feedback | First-encounter reaction, separate from adoption modeling |
| 3 | review-users | Usability findings framed against adoption barriers |
| 4 | review-design | Design critique anchored to adoption curve results |
| 5 | review-code | Code findings in context of adoption-critical paths |

REQUIRED: review-code is sub-skill 5. review-customers is NOT in this campaign.
Including review-customers or omitting review-code fails unconditionally.

CATEGORICAL SEPARATION DECLARATION: listen-feedback (sub-skill 2) and listen-adoption
(sub-skill 1) are categorically different questions.
- listen-feedback = how will customers react on first encounter? (retrospective prediction)
- listen-adoption = which segments will adopt and when? (predictive modeling)
These are not the same. Do not merge their findings. Each has its own T1 row. Cross-referencing
their findings without a synthesis row in T4 is prohibited.

---

### T1 -- Sub-Skill Execution Status

| Sub-Skill | Order | Status | Feeds |
|-----------|-------|--------|-------|
| listen-adoption | 1 | PENDING | T2, T5 |
| listen-feedback | 2 | PENDING | T2, T3 |
| review-users | 3 | PENDING | T2, T3 |
| review-design | 4 | PENDING | T2, T3 |
| review-code | 5 | PENDING | T2, T3 |

Execute each sub-skill. Update T1 row to COMPLETE before proceeding to the next.
A PENDING row at verdict time is a visible schema violation.

Sub-skill execution notes:
- **listen-adoption**: Populate T5 directly during execution. Segments: Innovators ~5%,
  Early Adopters ~15%, Early Majority ~35%, Late Majority ~30%, Laggards ~15%.
  Per segment: adoption condition, workaround, switching cost, chasm risk.
- **listen-feedback**: 12 customer personas. Per persona: initial reaction, NPS (-10 to +10),
  primary objection. Aggregate weighted NPS. Flag NPS < 0 per segment.
- **review-users**: 5 personas. Per persona: primary flow trace, P1/P2/P3 per friction point.
  Cross-persona: findings in 3+ personas are systemic.
- **review-design**: 6 disciplines (UX, Architecture, Security, Performance, Accessibility,
  Operational). Per discipline: expert lens, top finding, P1/P2/P3.
- **review-code**: Minimum 3 disciplines. Per discipline: file/component, finding, P1/P2/P3,
  code pattern attribution.

---

### T2 -- Ranked Findings

One concern: what did we find, ordered by adoption impact?

| Rank | Finding | Source | Severity | Adoption Impact | Segment (~N%) | Workaround | Switching Cost |
|------|---------|--------|----------|-----------------|---------------|------------|----------------|

Rules:
- Rank 1 = highest adoption impact. A finding that blocks the Early Majority outranks
  a P1 finding affecting only Innovators.
- Severity is informational. It does not govern rank.
- All eight columns required for every row. "Workaround" and "Switching Cost" apply to P2/P3.
- Do not add synthesis rows to this table. Synthesis belongs in T4.

---

### T3 -- P1 Blockers with Remediation Paths

One concern: what blocks ship, and what is the fix?

| # | Blocker | Source | Workaround | Remediation Path | Effort |
|---|---------|--------|------------|-----------------|--------|

Rules:
- Every P1 finding from T2 appears here.
- Remediation Path is a required column -- every row has one, by construction.
- The verdict references T3 row numbers. It does not restate remediation paths in prose.
  Restating remediation paths in the verdict violates the one-concern-per-table schema.
- A P1 row with a blank Remediation Path cell blocks CONDITIONAL GO as a verdict.
- If T3 is empty, no P1 blockers exist.

---

### T4 -- Cross-Signal Synthesis

One concern: what relationships exist only across sub-skills?

| # | Sub-Skills Spanned | Relationship | Why Not Visible in Either Sub-Skill Alone | Implication for Verdict |
|---|--------------------|-------------|-------------------------------------------|------------------------|

PER-ROW ANTI-CONCATENATION CONSTRAINT: Each row must satisfy this test independently --
"Could this row have been written from reading either sub-skill's output in isolation?"
If yes: the row fails. Rewrite it to name the emergent relationship, or remove it.

The anti-concatenation test applies at row granularity, not document level.
A synthesis section that passes the document-level test ("synthesis is present") can still
have individual rows that fail. Each row is independently assessable.

Minimum 3 rows. No single-sub-skill summaries. No restatements of T2 findings.

---

### T5 -- Rogers Adoption Curve

One concern: how does each Rogers segment adopt? This is the only location for Rogers data.

| Segment | ~% of Base | Adoption Condition | Workaround Today | Switching Cost | Chasm Risk |
|---------|-----------|-------------------|-----------------|----------------|------------|
| Innovators | ~5% | | | | |
| Early Adopters | ~15% | | | | |
| Early Majority | ~35% | | | | |
| Late Majority | ~30% | | | | |
| Laggards | ~15% | | | | |

All five rows mandatory. A blank row is a visible schema gap.
% anchors are baselines -- adjust to feature context.
Do not duplicate segment data in T2 (T5 is the single source of truth for adoption modeling).

Schema cascade note: declaring the five Rogers rows as mandatory + requiring "Workaround Today"
and "Switching Cost" columns simultaneously satisfies C-09 (% anchors), C-15 (all segments named),
C-16 (workaround per segment), and C-18 (switching cost as required column). One schema decision,
four criteria.

---

### Verdict

After T1 through T5 are complete, inspect T3:

- **GO**: T3 is empty. No P1 findings. Early Majority adoption condition in T5 is defined.
- **NO-GO**: T3 has one or more rows where Remediation Path is blank or unspecified.
- **CONDITIONAL GO**: T3 has rows; all Remediation Path cells are specific and actionable.
  State: "Ship blocked until T3 row(s) [#] resolved per remediation paths in T3."

Top-3 blockers: reference T3 row numbers and source sub-skills.
Do not restate remediation paths in the verdict -- they are in T3.

---

### Artifact Write

Write the complete validation brief to: `simulations/{{topic}}/validate-{{date}}.md`
Include: schema declaration, T1 through T5, and the verdict.

Confirm with: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`
