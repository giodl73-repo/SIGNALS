# draft-brainstorm Skill Prompt Variations — Round 7

**Skill:** draft-brainstorm
**Round:** 7
**Date:** 2026-03-15
**Rubric:** v6 (C-01 through C-24)
**Target:** All 24 criteria pass in every variation. R7 axes explore structural approaches
that satisfy the two new C-23 and C-24 criteria introduced in v6, building on the R6
combinatorial baseline (V-05 of R6 satisfies C-01–C-22; R7 must additionally achieve C-23
and C-24 across all five variations).

---

## R7 Axis Selection

R6 explored: adversarial declaration before diverge (V-01), extended inertia anchor (V-02),
4-phase compressed pipeline (V-03), conversational dense inline conditionals (V-04),
adversarial-first + inertia-centered combination (V-05).

R7 all variations satisfy C-01 through C-22 as baseline, then vary on primary axes for C-23/C-24:

| Variation | Primary Axis | C-23 Mechanism | C-24 Mechanism |
|-----------|--------------|----------------|----------------|
| V-01 | Role sequence — challenge as Phase 0, before all else | Earliest possible pre-commitment | Anchor references challenge criteria by field |
| V-02 | Inertia-as-comparator — pool entries evaluated against anchor | Challenge table columns anchor evaluation | 6-field anchor as structural scaffold |
| V-03 | Ordered planning stack: Challenge→AMEND→Architecture→Anchor→Diverge | Dedicated structural phase before Phase 1 | Architecture-grounded 5-field anchor |
| V-04 | Conversational register with C-23/C-24 inline triggers | Inline "if criteria not pre-committed" trigger | Inline "if anchor missing threshold/topology" trigger |
| V-05 | Universal table stack — all phases as column-schema tables | Challenge criteria table with Test/Threshold/Surviving columns | Anchor table with all 5 fields as explicit columns |

---

## Criteria Coverage Map (v6 — all 24)

| Criterion | Satisfied by |
|-----------|-------------|
| C-01 volume 20–40 | Diverge phase + exit gate |
| C-02 anatomy 4 fields | Cluster phase (table columns) |
| C-03 exactly 5 ** | Selection phase (exactly 5, post-challenge) |
| C-04 inertia present | Anchor phase (dedicated, named) |
| C-05 AMEND 3 adjustments | AMEND phase (before diverge) |
| C-06 grouped by category | Architecture declares sections; Cluster phase fills them |
| C-07 topic-specific rationale | Cluster phase instruction |
| C-08 4+ categories ≤40% | Architecture phase (% of Pool + cap check inline) |
| C-09 top 5 differentiated | Selection phase (3+ categories required) |
| C-10 AMEND non-overlapping | AMEND phase (Direction column) |
| C-11 two-pass diverge/cluster | Diverge = name+pitch only; Cluster = assign category+rationale |
| C-12 AMEND downstream effects | AMEND phase (Downstream Effect column) |
| C-13 inertia costs AND benefits | Anchor phase (both fields required) |
| C-14 self-verification pass | Verify phase (row-by-row checklist, 24 rows) |
| C-15 AMEND-first | AMEND phase precedes architecture and diverge |
| C-16 Do Nothing as anchor phase | Dedicated anchor phase before diverge |
| C-17 architecture pre-commitment | Architecture phase (slots + % + cap) before diverge |
| C-18 adversarial before ** marks | Challenge phase defers ** marks |
| C-19 per-phase exit gates | Enumerated exit conditions at end of every phase |
| C-20 table format structural enforcement | Tables throughout; % of Pool column computed inline |
| C-21 architecture-grounded anchor | Sequence: AMEND → Architecture → Anchor → Diverge |
| C-22 inline conditional correction triggers | Mid-step "if X → adjust before continuing" triggers |
| C-23 pre-committed adversarial challenge criteria | Challenge criteria declared as dedicated structural phase *before* any candidate generated |
| C-24 extended inertia anatomy | 5-field anchor: costs, benefits, competitive threshold, bypasses, preserves |

---

## V-01 — Role Sequence: Challenge as Phase 0

**Variation axis:** Role sequence — adversarial challenge framework declared as the absolute first phase, before AMEND, architecture, and anchor
**Hypothesis:** Positioning challenge criteria as Phase 0 — the very first commitment in the session — ensures the evaluation framework predates all other structural decisions, preventing any possibility that AMEND choices, category architecture, or the anchor definition could retroactively influence what "surviving" means. Pre-commitment at Phase 0 is stronger than pre-commitment at Phase 1 or 2 because no prior structural context exists to bias the criteria.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate a pool of 20–40 idea candidates. Work through these phases in strict order. Do not begin a phase until the previous phase's exit gate is satisfied.

---

#### Phase 0 — Challenge Criteria Declaration

Before writing any adjustments, architecture, anchor, or candidates, declare the adversarial challenge framework that will govern `**` selection.

Output a table with these columns: `Test | Threshold | What Constitutes Surviving`

Required tests (add topic-specific tests as appropriate):

| Test | Threshold | What Constitutes Surviving |
|------|-----------|---------------------------|
| Differentiation | Zero overlap with any other candidate's core mechanism | Removing the candidate would eliminate a distinct approach unavailable elsewhere in the pool |
| Feasibility | No unsatisfied hard constraints given the topic's known context | Candidate can be implemented without acquiring capabilities or resources the topic doesn't have |
| Inertia displacement | Clears at least 2 of the 5 anchor fields defined in Phase 3 | Demonstrates a clear advantage on Costs or Competitive Threshold over the Do Nothing baseline |
| Coverage contribution | At least 1 of the 5 `**` candidates must come from each of 3 distinct categories | Removing this candidate from the top 5 would collapse coverage to fewer than 3 categories |

These criteria are pre-committed. They may not be modified in any later phase.

**EXIT GATE:**
- [ ] Challenge table has 4+ rows (at minimum the 4 required tests)
- [ ] Every row has Test, Threshold, and What Constitutes Surviving
- [ ] Inertia displacement test references the 5-field anchor structure (to be built in Phase 3)
- [ ] Any FAIL → correct in-place before Phase 1

---

#### Phase 1 — AMEND Planning

Before architecture or candidates, write 3 pool-shaping adjustments.

| # | Dimension | Shift Description | Downstream Effect on Pool | Direction |
|---|-----------|-------------------|--------------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

Rules:
- Each Dimension must name a specific axis (not "be more creative")
- Each Downstream Effect must name what types of candidates surface or drop out
- All three Directions must differ (one expands, one narrows, one redirects)
- If two adjustments point the same direction → rewrite one before continuing

**EXIT GATE:**
- [ ] Exactly 3 rows
- [ ] Every row has Dimension, Downstream Effect, Direction
- [ ] All three Directions differ
- [ ] Any FAIL → correct in-place before Phase 2

---

#### Phase 2 — Architecture Declaration

Declare the category structure before any candidates.

| Category | Description | Target Count | % of Pool |
|----------|-------------|--------------|-----------|
| | | | |

Rules:
- At least 4 distinct categories
- % of Pool must be computed for each category
- No category may exceed 40% of total pool — if one does, redistribute before continuing
- Target counts must sum to a number between 20 and 40
- Compute total here: ______

**EXIT GATE:**
- [ ] 4+ categories
- [ ] % of Pool column is present and computed
- [ ] No category's % of Pool exceeds 40%
- [ ] Target counts sum to 20–40
- [ ] Any FAIL → correct in-place before Phase 3

---

#### Phase 3 — Do Nothing Anchor

Write the status quo entry as a structured 5-field anchor. This phase follows architecture so the anchor can reference the declared category landscape.

| Field | Content |
|-------|---------|
| Costs | What continuing the status quo actively costs (time, quality, competitive position, opportunities foregone) |
| Benefits | Why inertia is genuinely attractive — what the status quo does well that an alternative would need to match |
| Competitive Threshold | The specific level of advantage an alternative must demonstrate to justify displacing the status quo — reference categories from Phase 2 by name (e.g., "A candidate in the [Category X] bucket must demonstrate 2× improvement on [metric] to justify the transition cost") |
| Bypasses | Which of the declared Phase 2 categories the status quo renders unnecessary — name categories explicitly |
| Preserves | What the status quo protects that any transition would put at risk |

Rules:
- Competitive Threshold must name at least one Phase 2 category
- Bypasses must name at least one Phase 2 category
- This entry does NOT count toward the 20–40 pool; it is an anchor, not a candidate

**EXIT GATE:**
- [ ] All 5 fields present and non-empty
- [ ] Competitive Threshold names a specific metric or category from Phase 2
- [ ] Bypasses names at least one Phase 2 category
- [ ] Preserves names at least one thing at risk in a transition
- [ ] Any FAIL → correct in-place before Phase 4

---

#### Phase 4 — Diverge (Name + Pitch Only)

Generate 20–40 idea names and one-line pitches. Do not assign categories or rationales yet.

| # | Name | Pitch |
|---|------|-------|
| | | |

Rules:
- Do Nothing does not appear in this table (it is the Phase 3 anchor)
- If a candidate has no meaningful pitch that distinguishes it from another candidate → drop it
- Target 20–40 entries; stop at 40

**EXIT GATE:**
- [ ] Count is 20–40
- [ ] Every row has Name and Pitch
- [ ] No two rows have substantively identical pitches
- [ ] Any FAIL → correct in-place before Phase 5

---

#### Phase 5 — Cluster (Assign Category + Rationale)

For every diverge entry, assign a category from Phase 2 and write a topic-specific rationale.

| # | Name | Pitch | Category | Rationale |
|---|------|-------|----------|-----------|
| | | | | |

Rules:
- Category must be one of the Phase 2 declared categories (no new categories)
- Rationale must reference `{{topic}}` specifically — generic rationales that apply to any topic fail
- If a category fills beyond its Phase 2 target → flag inline: "Category [X] now at [N]% — redistributing [entry name] to [alternative category]"
- If a category exceeds 40% of total entries at any point → redistribute before continuing

**EXIT GATE:**
- [ ] All 4 fields present for every row
- [ ] No category exceeds 40% of entries
- [ ] At least 4 of 5 sampled rationales are topic-specific
- [ ] Any FAIL → correct in-place before Phase 6

---

#### Phase 6 — Adversarial Challenge

Apply the Phase 0 challenge criteria to identify `**` candidates. Do NOT assign `**` marks yet.

Step 6a: List 8–10 candidates from Phase 5 that appear most viable.

Step 6b: For each candidate, apply every test from Phase 0. Output:

| Candidate | Differentiation | Feasibility | Inertia Displacement | Coverage Contribution | Overall |
|-----------|----------------|-------------|---------------------|----------------------|---------|
| | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL |

Step 6c: Identify candidates where Overall = PASS. Do not mark `**` here.

Step 6d: If fewer than 5 candidates pass all tests → document the tradeoff for the closest failures and identify 5 finalists anyway.

**EXIT GATE:**
- [ ] 8–10 candidates evaluated
- [ ] All 4 Phase 0 tests applied to every candidate
- [ ] `**` marks not assigned in this phase
- [ ] At least 5 finalists identified (or documented exception)
- [ ] Any FAIL → correct in-place before Phase 7

---

#### Phase 7 — Selection

Assign `**` to exactly 5 Phase 6 finalists. Update the Phase 5 cluster table.

Rules:
- Exactly 5 `**` marks (no more, no fewer)
- The 5 picks must span at least 3 distinct Phase 2 categories
- Each `**` candidate survived Phase 6 challenge (or has a documented exception)

**EXIT GATE:**
- [ ] Exactly 5 `**` marks in the Phase 5 table
- [ ] 5 picks span 3+ categories
- [ ] Each pick passed Phase 6 (or has a documented exception)
- [ ] Any FAIL → correct in-place before Phase 8

---

#### Phase 8 — Verify

Run this 24-row checklist before writing the artifact.

| # | Check | PASS? |
|---|-------|-------|
| 1 | Challenge criteria table present (Phase 0) | |
| 2 | Challenge criteria table has 4+ rows | |
| 3 | Challenge criteria pre-committed (before Phase 1) | |
| 4 | AMEND has exactly 3 rows | |
| 5 | All 3 AMEND adjustments have Downstream Effect | |
| 6 | All 3 AMEND directions differ | |
| 7 | Architecture has 4+ categories | |
| 8 | No architecture category exceeds 40% | |
| 9 | Do Nothing anchor present (Phase 3) | |
| 10 | Anchor has Costs field | |
| 11 | Anchor has Benefits field | |
| 12 | Anchor has Competitive Threshold field | |
| 13 | Anchor has Bypasses field (names Phase 2 category) | |
| 14 | Anchor has Preserves field | |
| 15 | Pool count is 20–40 | |
| 16 | Every candidate has all 4 anatomy fields | |
| 17 | No pool category exceeds 40% | |
| 18 | 8–10 candidates challenged in Phase 6 | |
| 19 | Phase 6 applied all 4 Phase 0 tests | |
| 20 | Exactly 5 `**` marks | |
| 21 | 5 `**` picks span 3+ categories | |
| 22 | At least 4 of 5 sampled rationales are topic-specific | |
| 23 | AMEND section precedes architecture in the artifact | |
| 24 | Do Nothing anchor section precedes pool in the artifact | |

Any FAIL → correct in-place before Phase 9.

**EXIT GATE:**
- [ ] All 24 checks PASS
- [ ] Any FAIL → correct in-place before Phase 9

---

#### Phase 9 — Write

Write the final artifact to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure:
1. Header: topic, date, candidate count, rubric version
2. AMEND section (from Phase 1)
3. Do Nothing Anchor (full 5-field table from Phase 3)
4. Challenge Criteria (from Phase 0 — pre-committed framework)
5. Candidate pool by category section (from Phase 5, with `**` from Phase 7)
6. Challenge Summary table (from Phase 6)

---

## V-02 — Inertia-as-Comparator: Pool Entries Evaluated Against Anchor

**Variation axis:** Inertia framing — Do Nothing is the primary structural comparator; every `**` candidate must explicitly beat it on at least 2 anchor dimensions
**Hypothesis:** When the Do Nothing anchor's 5 fields define the evaluation dimensions explicitly (Costs, Benefits, Competitive Threshold, Bypasses, Preserves), and candidates are required to reference those dimensions in their challenge phase, the anchor does real structural work rather than being a checkbox entry. The competitive threshold field forces a named displacement bar, preventing `**` marks from being assigned to candidates that don't clearly beat the status quo.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Your job is to generate 20–40 idea candidates and identify the 5 most viable. The Do Nothing option (status quo) is your primary comparator — every strong candidate must demonstrate why it beats continuing as-is.

Work through these phases in strict order. Do not advance until the phase's exit gate is satisfied.

---

#### Phase 1 — AMEND Planning

Write 3 pool-shaping adjustments before any candidates.

Output:

| # | Dimension | Shift | Downstream Effect | Direction |
|---|-----------|-------|-------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

- Dimension: specific axis (not "be more creative")
- Shift: what changes (e.g., "reduce implementation scope to single-team")
- Downstream Effect: what kinds of candidates surface or drop out
- Direction: one of Expands / Narrows / Redirects — all three must differ
- If two Directions are the same → rewrite one before continuing

**EXIT GATE:**
- [ ] Exactly 3 rows
- [ ] All 4 columns filled per row
- [ ] All 3 Directions differ
- [ ] Any FAIL → correct in-place before Phase 2

---

#### Phase 2 — Architecture Declaration

Commit to the category structure.

| Category | Description | Target Count | % of Pool |
|----------|-------------|--------------|-----------|
| | | | |

Rules:
- 4+ categories
- % of Pool must be computed for each row
- No category may exceed 40%; if one does, redistribute before continuing
- Targets must sum to 20–40
- Totals row: [sum here]

**EXIT GATE:**
- [ ] 4+ categories
- [ ] % of Pool present and computed
- [ ] No category > 40%
- [ ] Totals sum to 20–40
- [ ] Any FAIL → correct in-place before Phase 3

---

#### Phase 3 — Do Nothing Anchor (Primary Comparator)

The status quo is the first "candidate" and the baseline against which all alternatives must compete. Write it as a full 6-field structured entry — this is not a one-line placeholder.

| Field | Content |
|-------|---------|
| **Costs** | What continuing the status quo actively costs — time, quality loss, competitive erosion, missed opportunities |
| **Benefits** | Why inertia is genuinely attractive — familiarity, zero migration risk, known failure modes, sunk cost preservation |
| **Competitive Threshold** | The minimum advantage an alternative must demonstrate to justify displacing the status quo. Be specific: name the Phase 2 categories where displacement is feasible, the metric or quality bar required, and how large the advantage must be (e.g., "a candidate in the [X] category must demonstrate at least [Y] improvement on [Z] — otherwise the transition costs are not justified") |
| **Bypasses** | Which Phase 2 categories the status quo renders unnecessary — name them by their Phase 2 label |
| **Preserves** | What the status quo protects that a transition would put at risk — name specific things (team knowledge, existing integrations, sunk investment, operating stability) |
| **Net Position** | One-sentence summary of the status quo's structural position: where it is strong, where it is vulnerable |

The Competitive Threshold must name at least one Phase 2 category and one specific metric or bar. "Good enough to justify change" is not specific — name the dimension and the magnitude.

**EXIT GATE:**
- [ ] All 6 fields present and non-empty
- [ ] Competitive Threshold names a Phase 2 category and a specific bar
- [ ] Bypasses names at least one Phase 2 category
- [ ] Preserves names at least one specific thing at risk
- [ ] Any FAIL → correct in-place before Phase 4

---

#### Phase 4 — Challenge Criteria Declaration

Now that the anchor defines the evaluation dimensions, pre-commit the adversarial challenge criteria that govern `**` selection.

Output a challenge table with columns: `Test | Threshold | What Constitutes Surviving`

Required tests:

| Test | Threshold | What Constitutes Surviving |
|------|-----------|---------------------------|
| Inertia displacement | Candidate explicitly beats Do Nothing on at least 2 of the 5 anchor fields (Costs, Benefits, Competitive Threshold, Bypasses, Preserves) | Challenge response names 2+ anchor fields and explains the advantage |
| Differentiation | Core mechanism does not overlap with any other candidate | Removing this candidate removes an approach not available elsewhere in the pool |
| Feasibility | No unsatisfied hard constraints for `{{topic}}` | Candidate operates within the topic's known capabilities and resources |
| Top-5 coverage | The 5 `**` picks collectively cover 3+ distinct Phase 2 categories | This candidate, if removed from the top 5, causes coverage to collapse below 3 categories |

These criteria are pre-committed. They may not be modified in Phases 5–7.

**EXIT GATE:**
- [ ] 4+ tests present
- [ ] Every test has Threshold and What Constitutes Surviving
- [ ] Inertia displacement test explicitly references anchor fields
- [ ] Table is declared before diverge (this phase precedes Phase 5)
- [ ] Any FAIL → correct in-place before Phase 5

---

#### Phase 5 — Diverge (Name + Pitch Only)

Generate names and one-line pitches for 20–40 candidates. Do not assign categories or rationales yet.

| # | Name | Pitch |
|---|------|-------|
| | | |

- Do Nothing does not appear here (it lives in Phase 3)
- If two entries have the same core pitch → drop the weaker one
- Stop at 40

**EXIT GATE:**
- [ ] Count is 20–40
- [ ] Every row has Name and Pitch
- [ ] No duplicate pitches
- [ ] Any FAIL → correct in-place before Phase 6

---

#### Phase 6 — Cluster (Category + Rationale)

Assign each Phase 5 candidate a Phase 2 category and a topic-specific rationale.

| # | Name | Pitch | Category | Rationale |
|---|------|-------|----------|-----------|
| | | | | |

Rules:
- Category must be a Phase 2 label (no new categories)
- Rationale must reference `{{topic}}` — a rationale that applies to any topic fails
- If a category exceeds 40% of total entries → redistribute inline before continuing
- After filling each category section: check count against Phase 2 target; if over by 2+ → redistribute before adding more

**EXIT GATE:**
- [ ] All 4 fields present for every row
- [ ] No category exceeds 40%
- [ ] At least 4 of 5 sampled rationales are topic-specific
- [ ] Any FAIL → correct in-place before Phase 7

---

#### Phase 7 — Adversarial Challenge

Apply Phase 4 criteria to 8–10 top candidates. Do NOT assign `**` yet.

Step 7a — shortlist 8–10 by apparent viability.

Step 7b — for each, apply all 4 Phase 4 tests AND explicitly check whether the candidate beats Do Nothing on 2+ anchor fields:

| Candidate | Inertia Displacement (2+ fields) | Differentiation | Feasibility | Coverage | Overall |
|-----------|----------------------------------|----------------|-------------|----------|---------|
| | PASS/FAIL (name fields) | PASS/FAIL | PASS/FAIL | PASS/FAIL | PASS/FAIL |

Step 7c — no `**` marks in this phase.

Step 7d — identify 5 finalists (or document exception if fewer than 5 pass all tests).

**EXIT GATE:**
- [ ] 8–10 candidates in the challenge table
- [ ] Inertia Displacement column names the specific anchor fields where the candidate wins
- [ ] `**` marks not assigned
- [ ] 5 finalists identified
- [ ] Any FAIL → correct in-place before Phase 8

---

#### Phase 8 — Selection

Mark exactly 5 Phase 7 finalists with `**` in the Phase 6 cluster table.

- Exactly 5 marks
- Spans 3+ Phase 2 categories
- Each survives Phase 7 challenge or has a documented exception

**EXIT GATE:**
- [ ] Exactly 5 `**` marks
- [ ] 3+ categories covered
- [ ] All 5 survived Phase 7 (or documented)
- [ ] Any FAIL → correct in-place before Phase 9

---

#### Phase 9 — Verify

Run this 24-row checklist.

| # | Check | PASS? |
|---|-------|-------|
| 1 | AMEND has exactly 3 adjustments | |
| 2 | All 3 AMEND directions differ | |
| 3 | All 3 AMEND adjustments name downstream effects | |
| 4 | Architecture has 4+ categories | |
| 5 | No architecture category exceeds 40% | |
| 6 | Do Nothing anchor present | |
| 7 | Anchor has Costs field | |
| 8 | Anchor has Benefits field | |
| 9 | Anchor has Competitive Threshold (names category + metric) | |
| 10 | Anchor has Bypasses (names Phase 2 category) | |
| 11 | Anchor has Preserves | |
| 12 | Challenge criteria table present (Phase 4) | |
| 13 | Challenge criteria pre-committed before diverge | |
| 14 | Inertia Displacement test in challenge table | |
| 15 | Pool count is 20–40 | |
| 16 | Every candidate has all 4 anatomy fields | |
| 17 | No pool category exceeds 40% | |
| 18 | Adversarial challenge applied before `**` marks | |
| 19 | Challenge table shows anchor fields beaten per candidate | |
| 20 | Exactly 5 `**` marks | |
| 21 | 5 `**` picks span 3+ categories | |
| 22 | At least 4 of 5 sampled rationales are topic-specific | |
| 23 | AMEND section in artifact precedes pool | |
| 24 | Do Nothing anchor section in artifact precedes pool | |

Any FAIL → correct in-place before Phase 10.

---

#### Phase 10 — Write

Write the artifact to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure:
1. Header (topic, date, count)
2. AMEND section
3. Do Nothing Anchor (full 6-field table)
4. Pre-Committed Challenge Criteria (Phase 4 table)
5. Candidate pool by category section (with `**`)
6. Challenge Summary (Phase 7 table)

---

## V-03 — Ordered Planning Stack: Challenge → AMEND → Architecture → Anchor → Diverge

**Variation axis:** Role sequence + lifecycle emphasis — all five planning phases complete before any candidate is generated
**Hypothesis:** The optimal pre-diverge sequence is: challenge criteria first (so the evaluation framework exists before all planning choices are made) → AMEND (so pool-shaping choices are influenced by the evaluation framework) → architecture (so the structural scaffold respects AMEND directions) → anchor (so the inertia comparator references the full architecture and can name which categories it bypasses and preserves). This ordering makes every subsequent phase structurally grounded in the previous one — the challenge criteria inform AMEND, AMEND informs architecture, architecture informs the anchor. Diverge begins only when all five planning phases are complete.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate a pool of 20–40 idea candidates. Complete all five planning phases before generating any candidates. The planning phases must execute in the order shown — each phase builds on the previous.

---

#### Phase 1 — Challenge Criteria

Pre-commit the adversarial framework that will govern `**` selection. Nothing else has been written yet — these criteria are genuinely prior to all other decisions.

| Test | Threshold | What Constitutes Surviving |
|------|-----------|---------------------------|
| Differentiation | No core mechanism overlap with any other candidate | Removing this candidate removes an approach unavailable elsewhere |
| Feasibility | No unsatisfied hard constraints for `{{topic}}` | Operates within the topic's known capabilities |
| Inertia displacement | Beats Do Nothing on 2+ of 5 anchor dimensions | Challenge response names the dimensions and the advantage |
| Collective coverage | Top 5 spans 3+ distinct categories | Removing this pick reduces category coverage below 3 |

Add up to 2 additional topic-specific tests if warranted. These criteria are locked — no modifications in later phases.

**EXIT GATE:**
- [ ] 4+ test rows
- [ ] Every row has Test, Threshold, What Constitutes Surviving
- [ ] Inertia displacement test references anchor dimensions (even though anchor is not yet written)
- [ ] Any FAIL → correct in-place before Phase 2

---

#### Phase 2 — AMEND Planning

With challenge criteria in place, write 3 pool-shaping adjustments. The criteria tell you what must survive; the adjustments tell you what kinds of things should be generated.

| # | Dimension | Shift | Downstream Effect on Pool | Direction |
|---|-----------|-------|--------------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

- Each Downstream Effect must reference a type of candidate that would surface or drop out
- All three Directions must differ (Expands / Narrows / Redirects)
- If two adjustments point the same direction → rewrite one before continuing

**EXIT GATE:**
- [ ] Exactly 3 rows
- [ ] All columns filled
- [ ] All 3 Directions differ
- [ ] Any FAIL → correct in-place before Phase 3

---

#### Phase 3 — Architecture Declaration

With AMEND adjustments defining what the pool should emphasize, commit to the category structure. The adjustments' Downstream Effects should be visible in the category targets.

| Category | Description | Target Count | % of Pool | Aligned With AMEND |
|----------|-------------|--------------|-----------|-------------------|
| | | | | |

Rules:
- 4+ categories
- % of Pool must be computed
- No category may exceed 40% — if one does, redistribute before continuing
- Targets must sum to 20–40
- Aligned With AMEND: name which AMEND adjustment (A1/A2/A3/none) is reflected in this category's size or description
- If no AMEND adjustment is visible in the category allocation → annotate why

**EXIT GATE:**
- [ ] 4+ categories
- [ ] % of Pool present and computed
- [ ] No category > 40%
- [ ] Targets sum to 20–40
- [ ] Aligned With AMEND column filled
- [ ] Any FAIL → correct in-place before Phase 4

---

#### Phase 4 — Do Nothing Anchor

With the full category architecture declared, write the status quo anchor. The anchor must reference the architecture — it can only name Bypasses and Preserves by referring to declared Phase 3 category labels.

| Field | Content |
|-------|---------|
| **Costs** | What continuing the status quo actively costs for `{{topic}}` |
| **Benefits** | Why inertia is genuinely attractive — what staying in place does well |
| **Competitive Threshold** | What an alternative must demonstrate to justify displacing the status quo. Name the Phase 3 categories where a challenger could plausibly win, the specific metric or quality bar required, and the minimum magnitude of advantage (e.g., "A candidate in the [Category] bucket must show [2×/elimination/3-month faster] on [metric] before transition costs are justified") |
| **Bypasses** | Phase 3 categories the status quo renders unnecessary — name by Phase 3 label |
| **Preserves** | What the status quo protects that a transition would put at risk — be specific |

This entry does not count toward the 20–40 pool.

**EXIT GATE:**
- [ ] All 5 fields present and non-empty
- [ ] Competitive Threshold names a Phase 3 category label and a specific metric
- [ ] Bypasses names at least one Phase 3 category
- [ ] Preserves names at least one specific thing
- [ ] Any FAIL → correct in-place before Phase 5

---

#### Phase 5 — Diverge (Name + Pitch Only)

Planning is complete. Generate 20–40 idea names and one-line pitches. No categories or rationales yet.

| # | Name | Pitch |
|---|------|-------|
| | | |

- Do Nothing does not appear here (it is the Phase 4 anchor)
- Stop at 40; if over → cull weakest entries inline
- If a candidate is a minor variant of another → merge or drop before continuing

**EXIT GATE:**
- [ ] Count is 20–40
- [ ] Every row has Name and Pitch
- [ ] No two rows are substantially identical
- [ ] Any FAIL → correct in-place before Phase 6

---

#### Phase 6 — Cluster (Category + Rationale)

Assign each Phase 5 candidate a Phase 3 category and a `{{topic}}`-specific rationale.

| # | Name | Pitch | Category | Rationale |
|---|------|-------|----------|-----------|
| | | | | |

- Category must be a Phase 3 label
- Rationale must name `{{topic}}` specifically — generic rationales fail
- After filling each category: check running count against Phase 3 target — if over by 2+ → redistribute inline
- If any category hits 40% of total entries → redistribute before continuing

**EXIT GATE:**
- [ ] All 4 fields for every row
- [ ] No category exceeds 40%
- [ ] At least 4 of 5 sampled rationales reference `{{topic}}`
- [ ] Any FAIL → correct in-place before Phase 7

---

#### Phase 7 — Adversarial Challenge

Apply Phase 1 criteria to 8–10 top candidates. No `**` marks yet.

| Candidate | Differentiation | Feasibility | Inertia Displacement (name dimensions) | Coverage | Overall |
|-----------|----------------|-------------|----------------------------------------|----------|---------|
| | | | | | |

- Inertia Displacement: name which 2+ anchor dimensions from Phase 4 the candidate wins on
- No `**` assignment in this phase
- Identify 5 finalists

**EXIT GATE:**
- [ ] 8–10 candidates evaluated
- [ ] All Phase 1 tests applied
- [ ] Inertia Displacement column names the specific Phase 4 dimensions
- [ ] `**` not assigned
- [ ] 5 finalists named
- [ ] Any FAIL → correct in-place before Phase 8

---

#### Phase 8 — Selection

Mark exactly 5 Phase 7 finalists with `**` in the Phase 6 table.

- Exactly 5 marks
- Spans 3+ Phase 3 categories
- Each survived Phase 7

**EXIT GATE:**
- [ ] Exactly 5 `**` marks
- [ ] 3+ categories
- [ ] Each `**` survived Phase 7
- [ ] Any FAIL → correct in-place before Phase 9

---

#### Phase 9 — Verify

| # | Check | PASS? |
|---|-------|-------|
| 1 | Phase 1 challenge criteria present and pre-committed | |
| 2 | Phase 1 has 4+ tests with Threshold and What Constitutes Surviving | |
| 3 | AMEND has exactly 3 rows | |
| 4 | AMEND directions all differ | |
| 5 | AMEND downstream effects present | |
| 6 | Architecture has 4+ categories | |
| 7 | No architecture category > 40% | |
| 8 | Architecture Aligned With AMEND column filled | |
| 9 | Do Nothing anchor present | |
| 10 | Anchor has Costs | |
| 11 | Anchor has Benefits | |
| 12 | Anchor has Competitive Threshold (Phase 3 category + metric) | |
| 13 | Anchor has Bypasses (Phase 3 category named) | |
| 14 | Anchor has Preserves | |
| 15 | Pool count is 20–40 | |
| 16 | Every candidate has all 4 anatomy fields | |
| 17 | No pool category > 40% | |
| 18 | Challenge applied before `**` marks | |
| 19 | Inertia Displacement column names anchor dimensions | |
| 20 | Exactly 5 `**` marks | |
| 21 | 5 `**` picks span 3+ categories | |
| 22 | 4 of 5 sampled rationales topic-specific | |
| 23 | Sequence is Phase 1→2→3→4 before Phase 5 diverge | |
| 24 | AMEND and anchor in artifact before pool | |

Any FAIL → correct in-place before Phase 10.

---

#### Phase 10 — Write

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure:
1. Header
2. Pre-Committed Challenge Criteria (Phase 1)
3. AMEND section (Phase 2)
4. Do Nothing Anchor (Phase 4)
5. Candidate pool by category section (Phase 6, with `**` from Phase 8)
6. Challenge Summary (Phase 7)

---

## V-04 — Conversational Register with C-23/C-24 Inline Triggers

**Variation axis:** Phrasing register — conversational descriptive with inline conditionals embedding C-23 and C-24 enforcement directly inside generation steps
**Hypothesis:** When C-23 and C-24 violations are intercepted as inline conditionals woven into the instructions themselves — "if your challenge criteria don't include a threshold, add one before moving forward" and "if your anchor is missing a Competitive Threshold, fill it in before writing Bypasses" — the model catches violations at the moment of generation rather than at a terminal verification pass. Inline triggers are lower friction than phase gates because the correction instruction is adjacent to the operation that could produce the violation.

---

### Prompt Body

You are running draft-brainstorm for the topic: `{{topic}}`. Work through these steps in order. Each step builds on the last — do not skip ahead.

---

**Step 1 — Pre-commit the challenge framework first.**

Before you write a single adjustment, category, or idea, write down how `**` candidates will be evaluated. Make a small table: one row per test, with a Threshold column that says what a candidate must demonstrate and a Surviving column that says what passing looks like.

You need at least four tests — differentiation (the candidate adds something others don't), feasibility (it works within the topic's constraints), inertia displacement (it beats continuing as-is on at least two dimensions you'll name when you write the anchor), and coverage (the five picks together span three or more categories). Add topic-specific tests if the topic suggests them.

If any test is missing a Threshold — not just a name, but an actual pass bar — fill it in before you move on. A test without a threshold is a decoration, not a gate.

This table is locked. Do not revise it later to make candidates pass.

Before moving to Step 2: count your tests (need 4+), confirm every row has Threshold and Surviving, and confirm the inertia displacement test will reference your anchor dimensions once the anchor is written.

---

**Step 2 — Write the three AMEND adjustments.**

Write them now, before the architecture and before any ideas. You need three, they need to pull in three different directions, and each one needs to say what would change in the pool if you applied it.

Make a table: Adjustment, Dimension (what axis is being shifted), Downstream Effect (what kinds of ideas surface or drop out), Direction (Expands / Narrows / Redirects).

If two adjustments have the same Direction — rewrite one before continuing. If an adjustment says "be more creative" without naming a specific axis — replace it with something actionable.

Before Step 3: confirm exactly 3 rows, all Directions differ, all Downstream Effects name a candidate type.

---

**Step 3 — Declare the category architecture.**

Lay out the categories in a table: Category, Description, Target Count, % of Pool. Compute the % of Pool for each row — do not leave it blank.

Aim for 4–6 categories and a total of 22–35 entries. No single category should hold more than 40% of the total — if you see one approaching 40% while planning, redistribute the target counts before continuing.

If your biggest category's % of Pool hits 40% or more, adjust counts before moving on.

Before Step 4: confirm 4+ categories, confirm % of Pool is computed, confirm no category exceeds 40%, confirm targets sum to 20–40.

---

**Step 4 — Write the Do Nothing anchor.**

This is the status quo — what happens if the topic team does nothing. Write it as a structured table with these five fields: Costs, Benefits, Competitive Threshold, Bypasses, Preserves.

Costs: what the status quo actively costs — time, quality, position, missed opportunities. Benefits: why inertia is genuinely attractive — do not minimize this; name real reasons people stay put. Competitive Threshold: what level of advantage an alternative must show to justify displacing the status quo — name a specific category from Step 3 and a specific bar (e.g., "a candidate in [Category X] must demonstrate [2× improvement / elimination of Y risk / 3-month cycle reduction] before the transition is worth it"). Bypasses: which Step 3 categories the status quo renders unnecessary — name them by label. Preserves: what the status quo protects that any transition puts at risk.

If you find yourself writing a Competitive Threshold that says "good enough to justify change" without naming a category or a magnitude — stop and rewrite it. If Bypasses doesn't name at least one Step 3 category label — go back and name one. If Preserves is vague ("existing processes") — make it specific.

Before Step 5: confirm all 5 fields are present, Competitive Threshold names a Step 3 category and a specific bar, Bypasses names a Step 3 category.

---

**Step 5 — Diverge: names and pitches only.**

Generate 20–40 ideas. For now, just the name and a one-line pitch. No categories, no rationales yet.

| # | Name | Pitch |
|---|------|-------|
| | | |

Do Nothing doesn't go here — it's the Step 4 anchor. Keep going until you have 20–40 distinct entries. If two entries share the same core mechanism, drop the weaker one. Stop at 40.

If your count is under 20, keep generating. If it's over 40, cull the weakest before Step 6.

---

**Step 6 — Cluster: assign category and rationale.**

Take the Step 5 table and add two more columns: Category (a Step 3 label) and Rationale (why this candidate serves `{{topic}}` specifically).

| # | Name | Pitch | Category | Rationale |
|---|------|-------|----------|-----------|
| | | | | |

Category must be one of your Step 3 labels — no new categories. Rationale must reference `{{topic}}` — if a rationale could apply to any topic equally, rewrite it.

After each category section is complete, check its count against the Step 3 target. If a category is running more than 2 entries over its target, redistribute into a lighter category before continuing. If any category hits 40% of total entries — redistribute now, not at the end.

Before Step 7: confirm all 4 fields for every row, confirm no category exceeds 40%, spot-check 5 rationales for topic-specificity.

---

**Step 7 — Challenge: apply the Step 1 criteria.**

Pick 8–10 candidates that look strongest. For each, apply the four Step 1 tests. Make a table: Candidate, then one column per test, then Overall.

| Candidate | Differentiation | Feasibility | Inertia Displacement | Coverage | Overall |
|-----------|----------------|-------------|---------------------|----------|---------|
| | | | | | |

For Inertia Displacement: do not just write PASS — name which two anchor dimensions from Step 4 the candidate wins on (e.g., "Costs + Competitive Threshold: eliminates [specific cost], clears the [Category X] displacement bar").

Do not assign `**` here. Name your 5 finalists at the bottom of this step.

If fewer than 5 candidates pass all tests — document the tradeoff for the next-closest and include them in the finalist list with a note.

---

**Step 8 — Assign exactly 5 `**` marks.**

Go back to the Step 6 table and mark exactly 5 of the Phase 7 finalists with `**`.

Count them: if you have more than 5 or fewer than 5, fix it before continuing. Confirm the 5 picks span at least 3 distinct Step 3 categories — if they don't, swap one out.

---

**Step 9 — Verify before writing.**

Run through this checklist:

| # | Check | PASS? |
|---|-------|-------|
| 1 | Challenge criteria table from Step 1 is present | |
| 2 | Challenge criteria has 4+ tests with Threshold + Surviving | |
| 3 | Challenge criteria was written before AMEND and architecture | |
| 4 | AMEND has exactly 3 rows | |
| 5 | All 3 AMEND directions differ | |
| 6 | All 3 AMEND adjustments have downstream effects | |
| 7 | Architecture has 4+ categories | |
| 8 | No architecture category > 40% | |
| 9 | Do Nothing anchor present | |
| 10 | Anchor has Costs | |
| 11 | Anchor has Benefits | |
| 12 | Anchor has Competitive Threshold (category + metric named) | |
| 13 | Anchor has Bypasses (Step 3 category named) | |
| 14 | Anchor has Preserves | |
| 15 | Pool count is 20–40 | |
| 16 | All 4 anatomy fields present for every candidate | |
| 17 | No pool category > 40% | |
| 18 | Step 7 challenge applied before `**` | |
| 19 | Inertia Displacement column names specific anchor dimensions | |
| 20 | Exactly 5 `**` marks | |
| 21 | 5 `**` picks span 3+ categories | |
| 22 | 4 of 5 sampled rationales are `{{topic}}`-specific | |
| 23 | Step 1 (challenge) runs before Steps 2–6 | |
| 24 | Anchor section precedes pool section in the artifact | |

Any FAIL → fix it before Step 10.

---

**Step 10 — Write the artifact.**

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure:
1. Header
2. Pre-Committed Challenge Criteria (Step 1)
3. AMEND section (Step 2)
4. Do Nothing Anchor (Step 4)
5. Candidate pool by category section (Step 6, with `**`)
6. Challenge Summary (Step 7)

---

## V-05 — Universal Table Stack: All Phases as Column-Schema Tables

**Variation axis:** Output format — every structural phase outputs a table with named columns, so violations in any phase are visually absent by column structure rather than detectable only through a checklist
**Hypothesis:** When the challenge criteria, AMEND adjustments, architecture, anchor, and idea pool are all expressed as tables with required column schemas, a missing field is structurally impossible to conceal — the blank column cell is visible before a checklist runs. The architecture table's computed % of Pool column makes the concentration cap verifiable at a glance. The anchor's 5-column row makes a missing Competitive Threshold visible by column position. This format converts conceptual requirements into structural constraints: if the column exists, the field must exist.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Every phase outputs a table with required columns. A missing field is visible by blank column — correct inline before advancing.

Work through phases in strict order. Do not advance until each phase's exit gate is satisfied.

---

#### Phase 1 — Challenge Criteria Table

Output:

| # | Test | Threshold | What Constitutes Surviving | Phase Where Applied |
|---|------|-----------|---------------------------|---------------------|
| | | | | |

Required rows:
- Differentiation: threshold = core mechanism doesn't overlap; surviving = removing candidate removes a distinct approach
- Feasibility: threshold = no unsatisfied hard constraints; surviving = operates within topic's known capabilities
- Inertia Displacement: threshold = beats Do Nothing on 2+ of 5 anchor dimensions (Costs / Benefits / Competitive Threshold / Bypasses / Preserves); surviving = challenge response names the 2+ dimensions and the advantage
- Coverage Contribution: threshold = removing from top 5 reduces category coverage below 3; surviving = eliminating this pick collapses distinct approach coverage

Add topic-specific tests as warranted.

Phase Where Applied column: enter "Phase 7" for all rows.

These criteria are pre-committed. No revision after Phase 1 is complete.

**EXIT GATE:**
- [ ] 4+ rows
- [ ] All 5 columns filled per row
- [ ] Inertia Displacement threshold names the 5 anchor dimensions by label
- [ ] Any FAIL → correct in-place before Phase 2

---

#### Phase 2 — AMEND Table

| # | Dimension | Shift Description | Downstream Effect on Pool | Direction |
|---|-----------|-------------------|--------------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

- All 5 columns required per row
- Direction values: one Expands, one Narrows, one Redirects — all three must differ
- Downstream Effect must name a candidate type that surfaces or drops out
- If two Directions are the same → rewrite before advancing

**EXIT GATE:**
- [ ] Exactly 3 rows
- [ ] All 5 columns filled
- [ ] All 3 Directions differ
- [ ] Any FAIL → correct in-place before Phase 3

---

#### Phase 3 — Architecture Table

| Category | Description | Target Count | % of Pool | Aligned With AMEND |
|----------|-------------|--------------|-----------|-------------------|
| | | | | |
| **TOTAL** | | [sum] | 100% | |

Rules:
- 4+ category rows
- % of Pool = Target Count / Total × 100; compute and fill
- No % of Pool may exceed 40% — if one does, redistribute target counts before continuing
- Total must be 20–40
- Aligned With AMEND: A1 / A2 / A3 / none — explain if none

**EXIT GATE:**
- [ ] 4+ category rows
- [ ] % of Pool computed and filled
- [ ] No category > 40%
- [ ] TOTAL row present; sum is 20–40
- [ ] Aligned With AMEND filled
- [ ] Any FAIL → correct in-place before Phase 4

---

#### Phase 4 — Do Nothing Anchor Table

| Field | Content | Notes |
|-------|---------|-------|
| Costs | | (what the status quo actively costs) |
| Benefits | | (why inertia is genuinely attractive) |
| Competitive Threshold | | (what an alternative must demonstrate; name a Phase 3 category and a specific metric/bar) |
| Bypasses | | (which Phase 3 categories the status quo renders unnecessary — use Phase 3 labels) |
| Preserves | | (what the status quo protects that a transition puts at risk) |

All 3 columns required for every row. Content column may not be blank.

Rules:
- Competitive Threshold: if it doesn't name a Phase 3 category label and a specific advantage bar → rewrite before Phase 5
- Bypasses: if it doesn't name at least one Phase 3 category label → rewrite before Phase 5
- This entry does not count toward pool totals

**EXIT GATE:**
- [ ] All 5 rows present
- [ ] Every Content cell non-empty
- [ ] Competitive Threshold names a Phase 3 category and a bar
- [ ] Bypasses names a Phase 3 category by label
- [ ] Any FAIL → correct in-place before Phase 5

---

#### Phase 5 — Diverge Table (Name + Pitch Only)

| # | Name | Pitch |
|---|------|-------|
| | | |

- 3 columns required for every row
- Target: 20–40 rows (not counting Do Nothing — that is the Phase 4 anchor)
- If two entries have the same core pitch → drop weaker before continuing
- Stop at 40; if over 40 → cull inline

**EXIT GATE:**
- [ ] Count is 20–40
- [ ] All 3 columns filled per row
- [ ] No duplicate core pitches
- [ ] Any FAIL → correct in-place before Phase 6

---

#### Phase 6 — Cluster Table (Full Anatomy)

| # | Name | Pitch | Category | Rationale | ** |
|---|------|-------|----------|-----------|-----|
| | | | | | |

- 6 columns required (** column filled in Phase 8; leave blank here)
- Category: Phase 3 label only
- Rationale: must reference `{{topic}}` by name — generic rationales fail
- After each category group: check running count against Phase 3 target; if over by 2+ → redistribute inline
- If any category's row count hits 40% of total → redistribute before continuing

**EXIT GATE:**
- [ ] First 5 columns filled for every row
- [ ] No category exceeds 40%
- [ ] At least 4 of 5 sampled rationales reference `{{topic}}`
- [ ] Any FAIL → correct in-place before Phase 7

---

#### Phase 7 — Challenge Table

Step 7a: Select 8–10 candidates from Phase 6 by apparent viability. List their names.

Step 7b: Output challenge table:

| Candidate | Test 1: Differentiation | Test 2: Feasibility | Test 3: Inertia Displacement (name Phase 4 dims) | Test 4: Coverage | Overall |
|-----------|------------------------|---------------------|--------------------------------------------------|------------------|---------|
| | PASS/FAIL | PASS/FAIL | PASS/FAIL (Costs? Benefits? Threshold? Bypasses? Preserves?) | PASS/FAIL | PASS/FAIL |

- Test 3 column must name which Phase 4 anchor dimensions the candidate wins on
- No `**` in this phase

Step 7c: List 5 finalists.

**EXIT GATE:**
- [ ] 8–10 rows in challenge table
- [ ] All 5 test columns filled per row
- [ ] Test 3 names specific Phase 4 dimensions
- [ ] `**` not assigned here
- [ ] 5 finalists listed
- [ ] Any FAIL → correct in-place before Phase 8

---

#### Phase 8 — Selection

Fill the `**` column in the Phase 6 cluster table for exactly 5 Phase 7 finalists.

- `**` value for selected: `**`
- `**` value for all others: blank
- Count the `**` marks: must be exactly 5
- Check that the 5 picks span 3+ Phase 3 category labels
- Confirm each `**` candidate was a Phase 7 finalist

**EXIT GATE:**
- [ ] Exactly 5 `**` marks in Phase 6 table
- [ ] 5 picks span 3+ Phase 3 categories
- [ ] All 5 are Phase 7 finalists
- [ ] Any FAIL → correct in-place before Phase 9

---

#### Phase 9 — Verify Table

| # | Check | PASS? |
|---|-------|-------|
| 1 | Challenge criteria table present (Phase 1) | |
| 2 | Challenge criteria has 4+ rows | |
| 3 | All 5 columns filled in challenge table | |
| 4 | Inertia Displacement threshold names 5 anchor dimensions | |
| 5 | AMEND has exactly 3 rows | |
| 6 | All 3 AMEND directions differ | |
| 7 | AMEND downstream effects filled | |
| 8 | Architecture has 4+ categories | |
| 9 | % of Pool column computed and present | |
| 10 | No architecture category > 40% | |
| 11 | Architecture total is 20–40 | |
| 12 | Anchor table has all 5 field rows | |
| 13 | Anchor Costs non-empty | |
| 14 | Anchor Benefits non-empty | |
| 15 | Anchor Competitive Threshold names Phase 3 category + metric | |
| 16 | Anchor Bypasses names Phase 3 category label | |
| 17 | Anchor Preserves non-empty | |
| 18 | Pool count is 20–40 | |
| 19 | All 6 columns in Phase 6 cluster table (incl. blank ** column) | |
| 20 | No pool category > 40% | |
| 21 | Challenge table 8–10 rows with all 5 test columns | |
| 22 | Exactly 5 `**` marks in Phase 6 table | |
| 23 | 5 `**` picks span 3+ categories | |
| 24 | 4 of 5 sampled rationales reference `{{topic}}` | |

Any FAIL → correct in-place before Phase 10.

---

#### Phase 10 — Write

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure:
1. Header (topic, date, count, rubric v6)
2. Pre-Committed Challenge Criteria table (Phase 1)
3. AMEND table (Phase 2)
4. Do Nothing Anchor table (Phase 4)
5. Candidate pool grouped by Phase 3 category sections (Phase 6, with `**`)
6. Challenge Summary table (Phase 7)

---

## Criteria Differential: R6→R7

| C-23 | C-24 | R6 Coverage | R7 Coverage |
|------|------|-------------|-------------|
| Pre-committed adversarial challenge criteria | Extended inertia anatomy (5 fields) | V-05 earns PASS+ on C-23; V-02 earns PASS+ on C-24 | All 5 variations satisfy both by structural design |

**Key structural innovations in R7 not present in R6:**

1. **Phase 0 / Phase 1 as challenge-first** (V-01, V-03, V-05): challenge criteria table is the literal first output, before AMEND, before architecture, before anchor — making C-23 unambiguously satisfied by position.

2. **Anchor-references-challenge cross-link** (V-02, V-03): the anchor's Competitive Threshold field explicitly references anchor dimension names that also appear in the challenge table's Inertia Displacement test — creating a semantic loop that makes C-23 and C-24 mutually reinforcing.

3. **5-field anchor with Phase 2/3 category cross-references in Bypasses and Competitive Threshold** (all variations): the anchor cannot be written generically — it must name specific category labels from the architecture phase, grounding the inertia description in the declared category landscape.

4. **Challenge table with "Inertia Displacement (name Phase 4 dims)" column** (V-05 Phase 7): the challenge table column schema forces naming of anchor dimensions, making C-24's field structure do work in the adversarial phase, not just in the anchor phase.
