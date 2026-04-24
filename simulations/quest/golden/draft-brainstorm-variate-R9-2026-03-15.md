# draft-brainstorm Skill Prompt Variations — Round 9

**Skill:** draft-brainstorm
**Round:** 9
**Date:** 2026-03-15
**Rubric:** v8 (C-01 through C-29)
**Target:** All 29 criteria pass across all 5 variations. R9 builds on R8's establishment of
C-28 (challenge-first lifecycle) and C-29 (entry condition chaining) as baseline. R9 axes
explore structural refinements: schema propagation, condensed contracts, interrogative register,
and pre-scoring integration.

---

## R9 Axis Selection

R8 established C-28 and C-29 in V-01. R9 treats both as non-negotiable baseline across all
5 variations. Canonical ordering: `Challenge → AMEND → Architecture → Anchor → Diverge`.
Every phase boundary doubly sealed: exit gates (departure) + entry conditions (arrival).

| Variation | Primary Axis | Novel Structural Feature |
|-----------|--------------|--------------------------|
| V-01 | Canonical reference — all 29 criteria addressed maximally explicitly | Gold-standard implementation, no compression |
| V-02 | Schema propagation — challenge T-1/T-2/T-3 field names used as columns in architecture, anchor, cluster | Challenge framework is a running column thread, not a terminal gate |
| V-03 | Condensed contracts — phases as PRE / DO / ASSERT blocks | Shorter phase bodies, same coverage; tests if concision preserves all criteria |
| V-04 | Interrogative register — all instructions written as questions | "What challenge tests will you pre-commit?" vs. imperative "Declare the challenge framework" |
| V-05 | Full combination — canonical lifecycle + schema propagation + pre-scoring column in cluster | T-1/T-2/T-3 preliminary score on every candidate before formal challenge phase |

---

## Criteria Coverage Map (v8 — all 29)

| Criterion | Satisfied by |
|-----------|-------------|
| C-01 volume 20–40 | Diverge exit gate (count check) |
| C-02 anatomy 4 fields | Cluster table column schema (visible by structure) |
| C-03 exactly 5 ** | Selection phase (exactly 5, post-challenge) |
| C-04 inertia present | Dedicated anchor phase before diverge |
| C-05 AMEND 3 adjustments | AMEND phase (before architecture and diverge) |
| C-06 grouped by category | Architecture declares sections; cluster fills them |
| C-07 topic-specific rationale | Cluster phase instruction + exit gate sample |
| C-08 4+ categories ≤40% | Architecture: % of Pool column + cap check inline |
| C-09 top 5 differentiated | Selection: 3+ categories required across 5 picks |
| C-10 AMEND non-overlapping | AMEND: Direction column, all three must differ |
| C-11 two-pass diverge/cluster | Diverge = name+pitch only; Cluster = category+rationale |
| C-12 AMEND downstream effects | AMEND: Downstream Effect column |
| C-13 inertia costs AND benefits | Anchor: both Costs and Benefits fields required |
| C-14 self-verification pass | Verify phase (row-by-row checklist before write) |
| C-15 AMEND-first | AMEND Phase 2 precedes architecture (Phase 3) and diverge (Phase 5) |
| C-16 Do Nothing as anchor phase | Dedicated Phase 4 anchor before Phase 5 diverge |
| C-17 architecture pre-commitment | Architecture Phase 3: categories + slots + % + cap before diverge |
| C-18 adversarial before ** marks | Challenge phase defers ** marks until after tests |
| C-19 per-phase exit gates | Enumerated exit conditions at end of every phase |
| C-20 table format structural enforcement | Tables throughout; % of Pool column computed inline |
| C-21 architecture-grounded anchor | Sequence: AMEND → Architecture → Anchor → Diverge |
| C-22 inline conditional correction triggers | "If [violation] → adjust before continuing" inside steps |
| C-23 pre-committed adversarial challenge criteria | Phase 1 = Challenge before any pool activity |
| C-24 extended inertia anatomy | 5-field anchor: Costs, Benefits, Threshold, Bypasses, Preserves |
| C-25 architecture-AMEND alignment column | Architecture table has "AMEND Source" column |
| C-26 anchor net position synthesis field | Anchor has "Net Position" synthesis field (6th field) |
| C-27 adversarial challenge binds anchor fields | Phase 1 challenge table has "Anchor Dimension" column naming Phase 4 field labels |
| C-28 challenge-first lifecycle | Phase 1 = Challenge before AMEND, architecture, anchor, diverge |
| C-29 entry condition chaining | Every phase opens with "Entry: Phase N exit gates passed" |

---

## V-01 — Canonical Reference: Maximally Explicit

**Variation axis:** Lifecycle emphasis — all 29 criteria addressed at maximum verbosity; no
compression or novel structure.
**Hypothesis:** Writing out every criterion explicitly in the phase that satisfies it creates the
most legible, verifiable prompt. When a criterion's satisfaction mechanism is named by label
(e.g., "this satisfies C-17"), the model cannot accidentally omit it. The reference implementation
establishes the floor that subsequent variations compress or restructure.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate a pool of 20–40 idea candidates and identify the 5 most immediately viable. Work through
the 10 phases below in strict order. A phase may not begin until its entry condition is named and
its predecessor's exit gates are confirmed satisfied.

---

#### Phase 1 — Challenge Framework Declaration

**Entry:** Start of session. No prior phase.

Before any adjustments, categories, anchor, or candidates are written, declare the full adversarial
challenge framework. This phase is the absolute first structural artifact. Its criteria may not be
modified by any later phase.

Output the following table:

| ID | Test | Threshold | Surviving Means | Anchor Dimension |
|----|------|-----------|-----------------|------------------|
| T-1 | Differentiation | Zero overlap with any other candidate's core mechanism | Removing this candidate would eliminate a distinct approach unavailable elsewhere in the pool | N/A |
| T-2 | Feasibility | No unsatisfied hard constraints given `{{topic}}`'s known context | Can be implemented without acquiring capabilities the topic does not currently have | N/A |
| T-3 | Inertia Displacement | Clears at least 2 of the 5 anchor dimensions defined in Phase 4 | Demonstrates a clear advantage on at least 2 of: **Costs · Benefits · Competitive Threshold · Bypasses · Preserves** (Phase 4 fields) | Costs · Benefits · Competitive Threshold · Bypasses · Preserves |
| T-4 | Coverage Contribution | At least 1 of the 5 `**` picks must come from each of 3 distinct architecture categories | Removing this candidate from the top 5 would collapse coverage to fewer than 3 categories | N/A |

The `Anchor Dimension` column names the Do Nothing anchor field labels (to be grounded in Phase 4).
These names are pre-committed here so the anchor must implement them and the challenge is bound
to them by schema.

**EXIT GATE:**
- [ ] Challenge table has 4 rows (T-1 through T-4)
- [ ] Every row has all 5 columns filled
- [ ] T-3 Anchor Dimension column names at minimum: Costs, Competitive Threshold, Bypasses, Preserves
- [ ] Challenge criteria pre-committed; any revision attempt must be flagged as a protocol violation
- [ ] Any FAIL → correct in-place before Phase 2

---

#### Phase 2 — AMEND Planning

**Entry:** Phase 1 exit gates passed.

Before architecture or candidates, write 3 pool-shaping adjustments. These adjustments will
drive the category architecture in Phase 3.

| # | Dimension | Shift Description | Downstream Effect on Pool | Direction |
|---|-----------|-------------------|--------------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

Rules:
- Dimension: name a specific axis (not generic like "be more creative")
- Downstream Effect: name which types of candidates would surface or drop out
- Direction: one of **Expands / Narrows / Redirects** — all three must differ
- If two Directions are the same → rewrite one before continuing

**EXIT GATE:**
- [ ] Exactly 3 rows
- [ ] Every row has all 5 columns filled
- [ ] All 3 Directions are distinct (no two the same)
- [ ] Each Downstream Effect names a candidate type, not just "more options"
- [ ] Any FAIL → correct in-place before Phase 3

---

#### Phase 3 — Architecture Declaration

**Entry:** Phase 2 exit gates passed.

Declare the category structure before any candidates are generated. Include an AMEND Source
column mapping each category to the specific A1/A2/A3 adjustment that motivates it.

| Category | Description | Target Count | % of Pool | AMEND Source |
|----------|-------------|--------------|-----------|--------------|
| | | | | |

Rules:
- At least 4 distinct categories
- % of Pool must be computed for each row (Target Count ÷ Total × 100)
- No category may exceed 40% of total — if one does, redistribute before continuing
- Target counts must sum to a number between 20 and 40
- Every category must declare which AMEND adjustment (A1, A2, or A3) motivated it; if a
  category is motivated by baseline topic needs rather than an AMEND adjustment, write "Baseline"
  but at least 3 categories must cite A1, A2, or A3
- Compute total here: ______

If your largest category is at or above 40% of the total, redistribute before continuing.

**EXIT GATE:**
- [ ] 4+ categories
- [ ] % of Pool column present and computed for every row
- [ ] No category's % of Pool exceeds 40%
- [ ] Target counts sum to 20–40
- [ ] Every row has an AMEND Source entry
- [ ] At least 3 rows cite A1, A2, or A3
- [ ] Any FAIL → correct in-place before Phase 4

---

#### Phase 4 — Do Nothing Anchor

**Entry:** Phase 3 exit gates passed.

Write the status quo entry as a structured 6-field anchor. This phase follows architecture so
the anchor can reference the declared category landscape. The anchor does not count toward
the 20–40 pool.

The field names used here (Costs, Benefits, Competitive Threshold, Bypasses, Preserves) are the
same names pre-committed in Phase 1's T-3 Anchor Dimension column. The anchor implements them.

| Field | Content |
|-------|---------|
| Costs | What continuing the status quo actively costs (time, quality, competitive position, opportunities foregone). Be specific to `{{topic}}`. |
| Benefits | Why inertia is genuinely attractive — what the status quo does well that any alternative must match or exceed. |
| Competitive Threshold | The specific level of advantage an alternative must demonstrate to justify displacing the status quo. Name at least one Phase 3 architecture category explicitly (e.g., "A candidate in the [Category X] bucket must demonstrate [metric] to justify transition cost"). |
| Bypasses | Which Phase 3 categories the status quo renders unnecessary — name at least one category by its Phase 3 label. |
| Preserves | What the status quo protects that any transition would put at risk. Be specific. |
| Net Position | Integrative judgment: does inertia currently dominate? Under what specific condition (which category of alternative at which threshold) would it stop dominating? Must synthesize all five fields above, not restate them. |

Rules:
- Competitive Threshold must name at least one Phase 3 category
- Bypasses must name at least one Phase 3 category
- Net Position must name a specific displacement condition, not just "inertia is strong"

**EXIT GATE:**
- [ ] All 6 fields present and non-empty
- [ ] Competitive Threshold names a specific Phase 3 category
- [ ] Bypasses names at least one Phase 3 category
- [ ] Net Position names a specific displacement condition
- [ ] Any FAIL → correct in-place before Phase 5

---

#### Phase 5 — Diverge (Name + Pitch Only)

**Entry:** Phase 4 exit gates passed.

Generate 20–40 idea names and one-line pitches. Do not assign categories or rationales in this
phase — that is Phase 6's job.

| # | Name | Pitch |
|---|------|-------|
| | | |

Rules:
- Do Nothing does not appear in this table (it is the Phase 4 anchor)
- Pitch must be a single sentence distinguishing this idea from all others
- Target 20–40 entries; stop at 40; if you reach 40 before divergence feels complete, continue
  adding names only and defer any pitch that isn't genuinely distinct
- If any two pitches are substantively identical → drop the weaker one before continuing

**EXIT GATE:**
- [ ] Count is 20–40
- [ ] Every row has Name and Pitch
- [ ] No two pitches are substantively identical
- [ ] Any FAIL → correct in-place before Phase 6

---

#### Phase 6 — Cluster (Assign Category + Rationale)

**Entry:** Phase 5 exit gates passed.

For every diverge entry, assign a Phase 3 category and write a topic-specific rationale.

| # | Name | Pitch | Category | Rationale |
|---|------|-------|----------|-----------|
| | | | | |

Rules:
- Category must be one declared in Phase 3 (no new categories)
- Rationale must reference `{{topic}}` specifically — a rationale that would apply equally
  to any topic does not pass
- If any category fills beyond its Phase 3 target count → flag inline: "Category [X] at [N]%
  — redistributing [Name] to [alternative category]" before continuing
- If any category exceeds 40% of total entries at any point → redistribute before continuing

**EXIT GATE:**
- [ ] All 4 anatomy fields present for every row (Name, Pitch, Category, Rationale)
- [ ] No category exceeds 40% of entries
- [ ] At least 4 of 5 sampled rationales are topic-specific
- [ ] Any FAIL → correct in-place before Phase 7

---

#### Phase 7 — Adversarial Challenge

**Entry:** Phase 6 exit gates passed.

Apply the Phase 1 challenge criteria (T-1 through T-4) to identify `**` finalists.
Do NOT assign `**` marks in this phase.

Step 7a: List 8–10 candidates from Phase 6 that appear most viable.

Step 7b: For each candidate, apply all 4 Phase 1 tests. Output:

| Candidate | T-1: Differentiation | T-2: Feasibility | T-3: Inertia Displacement (Costs · Competitive Threshold · Bypasses · Preserves) | T-4: Coverage Contribution | Overall |
|-----------|---------------------|-----------------|----------------------------------------------------------------------------------|---------------------------|---------|
| | PASS/FAIL | PASS/FAIL | PASS/FAIL — name which anchor dimensions cleared | PASS/FAIL | PASS/FAIL |

Note: T-3 column header names the Phase 4 anchor field labels, as pre-committed in Phase 1.

Step 7c: Identify candidates where Overall = PASS. Do not assign `**` here.

Step 7d: If fewer than 5 candidates pass all tests → document the tradeoff for the closest
failures and identify 5 finalists with exception notes.

**EXIT GATE:**
- [ ] 8–10 candidates evaluated
- [ ] All 4 Phase 1 tests applied to every candidate
- [ ] T-3 column names at least Costs, Competitive Threshold, Bypasses from Phase 4
- [ ] `**` marks not assigned in this phase
- [ ] At least 5 finalists identified (or documented exception)
- [ ] Any FAIL → correct in-place before Phase 8

---

#### Phase 8 — Selection

**Entry:** Phase 7 exit gates passed.

Assign `**` to exactly 5 Phase 7 finalists. Update the Phase 6 cluster table with marks.

Rules:
- Exactly 5 `**` marks — no more, no fewer
- The 5 picks must collectively span at least 3 distinct Phase 3 categories
- If the current finalists do not span 3 categories → swap out the weakest same-category
  finalist for the strongest candidate from an underrepresented category before assigning marks

**EXIT GATE:**
- [ ] Exactly 5 `**` marks in the Phase 6 table
- [ ] 5 picks span 3+ distinct Phase 3 categories
- [ ] Each pick passed Phase 7 (or has a documented exception)
- [ ] Any FAIL → correct in-place before Phase 9

---

#### Phase 9 — Verify

**Entry:** Phase 8 exit gates passed.

Run the following 29-row checklist before writing the artifact. Any FAIL must be corrected
in-place before proceeding.

| # | Check | PASS? |
|---|-------|-------|
| 1 | Phase 1 challenge table present with T-1 through T-4 rows | |
| 2 | Phase 1 T-3 Anchor Dimension column names anchor field labels | |
| 3 | Challenge criteria not modified after Phase 1 | |
| 4 | AMEND has exactly 3 rows | |
| 5 | All 3 AMEND rows have Dimension, Downstream Effect, Direction | |
| 6 | All 3 AMEND Directions are distinct | |
| 7 | Architecture has 4+ categories | |
| 8 | Architecture % of Pool column present and computed | |
| 9 | No architecture category exceeds 40% | |
| 10 | Architecture target counts sum to 20–40 | |
| 11 | Architecture AMEND Source column present; at least 3 rows cite A1/A2/A3 | |
| 12 | Do Nothing anchor present as a dedicated phase before diverge | |
| 13 | Anchor has Costs field (specific to topic) | |
| 14 | Anchor has Benefits field | |
| 15 | Anchor has Competitive Threshold field naming a Phase 3 category | |
| 16 | Anchor has Bypasses field naming a Phase 3 category | |
| 17 | Anchor has Preserves field | |
| 18 | Anchor has Net Position synthesis field naming a displacement condition | |
| 19 | Diverge (Phase 5) produced only Name + Pitch (no categories or rationales) | |
| 20 | Pool count is 20–40 | |
| 21 | Every candidate has all 4 anatomy fields (Name, Pitch, Category, Rationale) | |
| 22 | No pool category exceeds 40% | |
| 23 | At least 4 of 5 sampled rationales are topic-specific | |
| 24 | 8–10 candidates challenged in Phase 7 | |
| 25 | Phase 7 applied all 4 Phase 1 tests; T-3 column names anchor fields | |
| 26 | Exactly 5 `**` marks in final pool | |
| 27 | 5 `**` picks span 3+ categories | |
| 28 | Each phase opened with "Entry: Phase N exit gates passed" (or equivalent) | |
| 29 | AMEND section precedes architecture, anchor precedes pool in artifact | |

**EXIT GATE:**
- [ ] All 29 checks PASS
- [ ] Any FAIL → correct in-place before Phase 10

---

#### Phase 10 — Write Artifact

**Entry:** Phase 9 exit gates passed.

Write the final artifact to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Artifact structure:
1. Header: topic, date, candidate count, rubric version
2. AMEND section (from Phase 2)
3. Do Nothing Anchor — full 6-field table (from Phase 4)
4. Challenge Criteria — pre-committed framework (from Phase 1)
5. Candidate pool by category (from Phase 6, with `**` from Phase 8)
6. Challenge Summary table (from Phase 7)

---

## V-02 — Schema Propagation: Challenge Fields as Running Thread

**Variation axis:** Output format — challenge test IDs (T-1/T-2/T-3/T-4) used as column names
in architecture, anchor, and cluster phases, making the challenge framework a structural thread
rather than a terminal gate.
**Hypothesis:** When every subsequent phase carries the challenge test IDs as explicit columns,
the model is continuously reminded of what each structural decision must eventually satisfy.
Architecture categories labeled with their primary challenge test contribution are easier to keep
distinct. Cluster rationales labeled with their T-1/T-2 evidence surface weak rationales before
the formal adversarial phase. The challenge framework stops being a surprise at Phase 7.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate 20–40 idea candidates and identify 5 with `**`. Work through the 10 phases in strict
order. The Phase 1 challenge framework will appear as column references in every subsequent phase —
do not skip or rename those columns.

---

#### Phase 1 — Challenge Framework Declaration

**Entry:** Start of session. No prior phase.

Declare the adversarial challenge framework first. These test IDs (T-1 through T-4) will be
used as column references in Phases 3, 4, 6, and 7. Do not modify them after this phase.

| ID | Test | Threshold | Surviving Means | Anchor Dimension |
|----|------|-----------|-----------------|------------------|
| T-1 | Differentiation | Zero overlap with any other candidate's core mechanism | Removing this candidate loses a distinct approach | N/A |
| T-2 | Feasibility | No unsatisfied hard constraints for `{{topic}}` | Implementable without capabilities the topic lacks | N/A |
| T-3 | Inertia Displacement | Clears ≥2 of: **Costs · Competitive Threshold · Bypasses · Preserves** (Phase 4 fields) | Demonstrates explicit advantage on 2+ anchor dimensions | Costs · Competitive Threshold · Bypasses · Preserves |
| T-4 | Coverage Contribution | Removing this pick would collapse `**` coverage to <3 categories | Contributes a category not otherwise represented in top 5 | N/A |

The `Anchor Dimension` column pre-commits the Phase 4 anchor field names. Phase 4 must implement
exactly these labels.

**EXIT GATE:**
- [ ] T-1 through T-4 all present
- [ ] T-3 Anchor Dimension names: Costs, Competitive Threshold, Bypasses, Preserves
- [ ] Test IDs locked; no modifications permitted in later phases
- [ ] Any FAIL → correct in-place before Phase 2

---

#### Phase 2 — AMEND Planning

**Entry:** Phase 1 exit gates passed.

| # | Dimension | Shift | Downstream Effect | Direction |
|---|-----------|-------|-------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

- Direction must be Expands / Narrows / Redirects; all three must differ
- Downstream Effect must name specific candidate types, not just "more variety"
- If two Directions match → rewrite the one with weaker specificity before continuing

**EXIT GATE:**
- [ ] Exactly 3 rows
- [ ] All 5 columns filled per row
- [ ] All 3 Directions differ
- [ ] Any FAIL → correct in-place before Phase 3

---

#### Phase 3 — Architecture Declaration

**Entry:** Phase 2 exit gates passed.

Declare categories with their primary challenge test contribution and AMEND source.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary Challenge Test |
|----------|-------------|--------------|-----------|--------------|------------------------|
| | | | | | |

- `Primary Challenge Test`: which Phase 1 test (T-1/T-2/T-3/T-4) does this category most
  directly support? At least one category must support T-3 (Inertia Displacement).
- `AMEND Source`: which A1/A2/A3 adjustment motivated this category?
- If your largest category reaches or exceeds 40% of total → redistribute before continuing
- Total: ______

**EXIT GATE:**
- [ ] 4+ categories
- [ ] % of Pool computed for every row
- [ ] No category > 40%
- [ ] Totals sum to 20–40
- [ ] Every row has AMEND Source and Primary Challenge Test
- [ ] At least 1 category lists T-3 as primary test
- [ ] Any FAIL → correct in-place before Phase 4

---

#### Phase 4 — Do Nothing Anchor

**Entry:** Phase 3 exit gates passed.

Write the 6-field anchor using the exact field names pre-committed in Phase 1's T-3 Anchor
Dimension column.

| Field | Content | Challenge Test |
|-------|---------|----------------|
| Costs | [specific to `{{topic}}`] | T-3 |
| Benefits | [why inertia is genuinely attractive] | T-3 |
| Competitive Threshold | [displacement bar; name a Phase 3 category] | T-3 |
| Bypasses | [Phase 3 categories rendered unnecessary; name at least one] | T-3 |
| Preserves | [what transition would put at risk] | T-3 |
| Net Position | [integrative judgment: does inertia dominate now? what would displace it?] | T-3 synthesis |

The `Challenge Test` column traces each anchor field back to T-3, making the bidirectional
binding between Phase 1 and Phase 4 explicit in the schema.

**EXIT GATE:**
- [ ] All 6 fields present and non-empty
- [ ] Field labels match Phase 1 T-3 Anchor Dimension exactly
- [ ] Competitive Threshold names a specific Phase 3 category
- [ ] Net Position names a displacement condition, not just a directional statement
- [ ] Any FAIL → correct in-place before Phase 5

---

#### Phase 5 — Diverge (Name + Pitch Only)

**Entry:** Phase 4 exit gates passed.

Generate 20–40 idea names and one-line pitches only. No categories, no rationales.

| # | Name | Pitch |
|---|------|-------|
| | | |

- Do Nothing not included here (Phase 4 anchor)
- If any two pitches are substantively identical → drop the weaker before continuing
- Stop at 40 entries

**EXIT GATE:**
- [ ] Count is 20–40
- [ ] Name and Pitch present for every row
- [ ] No duplicate pitches
- [ ] Any FAIL → correct in-place before Phase 6

---

#### Phase 6 — Cluster (Category + Rationale + T-Evidence)

**Entry:** Phase 5 exit gates passed.

Assign a Phase 3 category and topic-specific rationale to every entry. Add a `T-Evidence`
column noting which Phase 1 test(s) this candidate's rationale already supports.

| # | Name | Pitch | Category | Rationale | T-Evidence |
|---|------|-------|----------|-----------|------------|
| | | | | | |

- Category must be from Phase 3 (no new categories)
- Rationale must reference `{{topic}}` specifically
- `T-Evidence`: note T-1, T-2, T-3, or T-4 where the rationale demonstrates the relevant
  threshold (e.g., "T-1: unique mechanism not seen elsewhere in pool")
- If a category exceeds 40% of entries → redistribute before continuing

**EXIT GATE:**
- [ ] All 5 columns filled for every row
- [ ] No category exceeds 40%
- [ ] At least 4 of 5 sampled rationales are topic-specific
- [ ] T-Evidence column present (may note N/A if no clear pre-score)
- [ ] Any FAIL → correct in-place before Phase 7

---

#### Phase 7 — Adversarial Challenge

**Entry:** Phase 6 exit gates passed.

Apply Phase 1 tests to 8–10 top candidates. Use Phase 1 test IDs as column headers.
Do NOT assign `**` marks here.

| Candidate | T-1: Differentiation | T-2: Feasibility | T-3: Inertia Displacement (Costs · Competitive Threshold · Bypasses · Preserves) | T-4: Coverage Contribution | Overall |
|-----------|---------------------|-----------------|----------------------------------------------------------------------------------|---------------------------|---------|
| | | | | | |

- T-3 column header names the Phase 4 anchor field labels (as pre-committed in Phase 1)
- For T-3: name which 2+ anchor dimensions the candidate clears
- If fewer than 5 pass Overall → document exceptions; identify 5 finalists anyway

**EXIT GATE:**
- [ ] 8–10 candidates evaluated
- [ ] All 4 tests applied; T-3 column names anchor field labels
- [ ] No `**` marks assigned in this phase
- [ ] At least 5 finalists identified
- [ ] Any FAIL → correct in-place before Phase 8

---

#### Phase 8 — Selection

**Entry:** Phase 7 exit gates passed.

Assign `**` to exactly 5 finalists. The 5 picks must span 3+ Phase 3 categories.
If they don't → swap out lowest-priority same-category finalist before assigning marks.

**EXIT GATE:**
- [ ] Exactly 5 `**` marks in the Phase 6 table
- [ ] 5 picks span 3+ categories
- [ ] Any FAIL → correct in-place before Phase 9

---

#### Phase 9 — Verify

**Entry:** Phase 8 exit gates passed.

Row-by-row checklist (29 rows). Any FAIL → correct in-place before Phase 10.

| # | Check | PASS? |
|---|-------|-------|
| 1 | Phase 1 challenge table present (T-1 through T-4) | |
| 2 | T-3 Anchor Dimension column names: Costs, Competitive Threshold, Bypasses, Preserves | |
| 3 | Phase 3 architecture has "Primary Challenge Test" column | |
| 4 | Phase 4 anchor field labels match Phase 1 T-3 Anchor Dimension | |
| 5 | Phase 6 cluster has "T-Evidence" column | |
| 6 | Phase 7 challenge T-3 column header names anchor field labels | |
| 7 | AMEND exactly 3 rows, all Directions differ | |
| 8 | Architecture 4+ categories, no category > 40%, AMEND Source column present | |
| 9 | At least 1 architecture category lists T-3 as primary test | |
| 10 | Anchor has all 6 fields (Costs, Benefits, Competitive Threshold, Bypasses, Preserves, Net Position) | |
| 11 | Net Position names a specific displacement condition | |
| 12 | Diverge produced only Name + Pitch | |
| 13 | Pool count is 20–40 | |
| 14 | Every candidate has Name, Pitch, Category, Rationale, T-Evidence | |
| 15 | No pool category exceeds 40% | |
| 16 | At least 4 of 5 sampled rationales are topic-specific | |
| 17 | 8–10 candidates challenged in Phase 7 | |
| 18 | Phase 7 applied all 4 tests; T-3 column names anchor fields | |
| 19 | Exactly 5 `**` marks | |
| 20 | 5 `**` picks span 3+ categories | |
| 21–29 | [Entry condition chaining verified: each phase opened with "Entry: Phase N exit gates passed"] | |

**EXIT GATE:**
- [ ] All 29 checks PASS
- [ ] Any FAIL → correct in-place before Phase 10

---

#### Phase 10 — Write Artifact

**Entry:** Phase 9 exit gates passed.

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure: Header → AMEND → Anchor (6 fields) → Challenge Criteria → Pool by category (with `**`) → Challenge Summary

---

## V-03 — Condensed Contracts: PRE / DO / ASSERT Notation

**Variation axis:** Phrasing register — phases structured as formal three-part contracts
(PRE: what must be true before starting / DO: what to execute / ASSERT: what must be true
when done). Tests if concise contract notation preserves all criterion coverage with fewer words.
**Hypothesis:** Verbose phase bodies inflate prompt length without adding coverage. A PRE/DO/ASSERT
structure separates precondition (entry condition), execution instruction, and postcondition
(exit gate) into three labeled slots per phase, giving evaluators three clear surfaces to check.
The discipline of naming preconditions separately from postconditions may surface omitted entry
conditions more reliably than embedded prose.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate 20–40 idea candidates; mark 5 with `**`. Execute the 10 phases below as formal contracts.
Each phase has three parts: **PRE** (what must be true before starting), **DO** (what to execute),
**ASSERT** (what must be true when done). Any ASSERT failure must be corrected in-place before the
next phase's PRE is invoked.

---

**Phase 1 — Challenge Framework**

PRE: Start of session. No prior phase exit gates to satisfy.

DO: Produce the challenge table. These criteria govern `**` selection throughout.

| ID | Test | Threshold | Surviving Means | Anchor Dimension |
|----|------|-----------|-----------------|------------------|
| T-1 | Differentiation | Zero overlap in core mechanism | Removing this loses a distinct approach | N/A |
| T-2 | Feasibility | No unmet hard constraints for `{{topic}}` | Implementable given topic's current capabilities | N/A |
| T-3 | Inertia Displacement | Clears ≥2 of: **Costs · Competitive Threshold · Bypasses · Preserves** | Explicit advantage on 2+ Phase 4 anchor dimensions | Costs · Competitive Threshold · Bypasses · Preserves |
| T-4 | Coverage Contribution | Removing this pick collapses `**` to <3 categories | Contributes a category not otherwise in top 5 | N/A |

ASSERT:
- [ ] T-1 through T-4 present
- [ ] T-3 Anchor Dimension column names: Costs, Competitive Threshold, Bypasses, Preserves
- [ ] Criteria locked; no modification permitted after Phase 1

---

**Phase 2 — AMEND Planning**

PRE: Phase 1 exit gates (ASSERT) passed.

DO: Write 3 pool-shaping adjustments.

| # | Dimension | Shift | Downstream Effect | Direction |
|---|-----------|-------|-------------------|-----------|
| A1 | | | | Expands |
| A2 | | | | Narrows |
| A3 | | | | Redirects |

Direction must be Expands / Narrows / Redirects; all three must differ. If two match →
rewrite one before continuing.

ASSERT:
- [ ] Exactly 3 rows; all 5 columns filled
- [ ] All 3 Directions distinct

---

**Phase 3 — Architecture Declaration**

PRE: Phase 2 ASSERT passed.

DO: Declare category structure. Include AMEND Source and compute % of Pool.

| Category | Description | Target Count | % of Pool | AMEND Source |
|----------|-------------|--------------|-----------|--------------|
| | | | | |

4+ categories. No category > 40% (redistribute if needed). Counts sum to 20–40.
At least 3 categories must cite A1, A2, or A3 in AMEND Source.

ASSERT:
- [ ] 4+ categories; % of Pool computed; no category > 40%; totals sum to 20–40
- [ ] AMEND Source column present; at least 3 rows cite A1/A2/A3

---

**Phase 4 — Do Nothing Anchor**

PRE: Phase 3 ASSERT passed.

DO: Write the 6-field anchor using Phase 1 T-3 field names. This is a baseline comparator, not
a pool candidate.

| Field | Content |
|-------|---------|
| Costs | [specific to `{{topic}}`] |
| Benefits | [genuine appeal of the status quo] |
| Competitive Threshold | [displacement bar; name a Phase 3 category] |
| Bypasses | [Phase 3 categories the status quo renders unnecessary; name at least one] |
| Preserves | [what a transition would put at risk] |
| Net Position | [integrative judgment: does inertia currently dominate? what would displace it?] |

Field labels must match Phase 1 T-3 Anchor Dimension exactly.

ASSERT:
- [ ] All 6 fields present and non-empty
- [ ] Competitive Threshold names a specific Phase 3 category
- [ ] Net Position names a specific displacement condition

---

**Phase 5 — Diverge**

PRE: Phase 4 ASSERT passed.

DO: Generate 20–40 name + pitch pairs. No categories or rationales here.

| # | Name | Pitch |
|---|------|-------|
| | | |

Stop at 40. Drop any pitch that duplicates another.

ASSERT:
- [ ] Count is 20–40; every row has Name and Pitch; no duplicate pitches

---

**Phase 6 — Cluster**

PRE: Phase 5 ASSERT passed.

DO: Assign Phase 3 category and topic-specific rationale to every entry.

| # | Name | Pitch | Category | Rationale |
|---|------|-------|----------|-----------|
| | | | | |

Category must be from Phase 3. Rationale must reference `{{topic}}` specifically.
If any category exceeds 40% → redistribute before continuing.

ASSERT:
- [ ] All 4 anatomy fields present for every row
- [ ] No category > 40%; at least 4 of 5 sampled rationales are topic-specific

---

**Phase 7 — Adversarial Challenge**

PRE: Phase 6 ASSERT passed.

DO: Apply Phase 1 tests to 8–10 top candidates. Do not assign `**` marks here.

| Candidate | T-1: Differentiation | T-2: Feasibility | T-3: Inertia Displacement (Costs · Competitive Threshold · Bypasses · Preserves) | T-4: Coverage Contribution | Overall |
|-----------|---------------------|-----------------|----------------------------------------------------------------------------------|---------------------------|---------|

Name which anchor dimensions each candidate clears in the T-3 column.
If <5 overall pass → document exceptions; identify 5 finalists.

ASSERT:
- [ ] 8–10 candidates evaluated; all 4 tests applied; T-3 column names anchor field labels; no `**` assigned; 5+ finalists

---

**Phase 8 — Selection**

PRE: Phase 7 ASSERT passed.

DO: Assign `**` to exactly 5 finalists. The 5 must span 3+ Phase 3 categories. If not →
swap lowest-priority same-category finalist for strongest underrepresented-category candidate.

ASSERT:
- [ ] Exactly 5 `**` marks; 5 picks span 3+ categories

---

**Phase 9 — Verify**

PRE: Phase 8 ASSERT passed.

DO: Run the 29-row checklist from V-01. Any FAIL → correct in-place.

ASSERT:
- [ ] All 29 checks PASS

---

**Phase 10 — Write Artifact**

PRE: Phase 9 ASSERT passed.

DO: Write to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure: Header → AMEND → Anchor (6 fields) → Challenge Criteria → Pool by category (with `**`) → Challenge Summary

---

## V-04 — Interrogative Register: Instructions as Questions

**Variation axis:** Phrasing register — all phase instructions written as questions the model
must answer, rather than imperatives.
**Hypothesis:** Interrogative framing requires the model to commit to an answer before
generating output, rather than filling in a template by rote. "What adversarial tests will
govern `**` selection?" produces a more deliberate challenge framework than "Write the
challenge table." Questions also make phase transitions feel like genuine decision points
rather than mechanical steps. The risk is ambiguity — a question might be answered too
briefly. Exit gates remain imperative to maintain structural enforcement.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Your goal: a pool of 20–40 idea candidates with 5 marked `**`. Answer the questions in each
phase before proceeding. Do not skip a phase. All exit gate conditions must be confirmed before
moving forward.

---

#### Phase 1 — What adversarial tests will govern `**` selection?

**Entry:** Start of session. No prior phase.

Before any adjustments, categories, anchor, or candidates: decide which tests a candidate must
pass to earn `**`. This is the most important decision in the session — it must be made first,
before you know what ideas you will generate.

Answer: produce the following challenge table with tests appropriate to `{{topic}}`.

| ID | Test | Threshold | What Does Surviving Mean? | Anchor Dimension |
|----|------|-----------|--------------------------|------------------|
| T-1 | Differentiation | Zero overlap in core mechanism | Removing this candidate loses a distinct approach | N/A |
| T-2 | Feasibility | No unmet hard constraints | Implementable given `{{topic}}`'s current resources and capabilities | N/A |
| T-3 | Inertia Displacement | Clears ≥2 of: **Costs · Competitive Threshold · Bypasses · Preserves** | Advantage on 2+ Phase 4 anchor dimensions over the status quo | Costs · Competitive Threshold · Bypasses · Preserves |
| T-4 | Coverage Contribution | Removing this pick would collapse `**` coverage to <3 categories | Contributes a category not otherwise in the top 5 | N/A |

Why T-3's Anchor Dimension column names field labels from Phase 4: by committing now to which
anchor dimensions you will test against, Phase 4 must implement those exact field names. The
challenge is bound to the anchor by schema, not by ad hoc evaluation.

These criteria are locked after this phase.

**EXIT GATE:**
- [ ] T-1 through T-4 all defined
- [ ] T-3 Anchor Dimension names: Costs, Competitive Threshold, Bypasses, Preserves
- [ ] Challenge criteria locked; any FAIL → correct in-place before Phase 2

---

#### Phase 2 — What 3 adjustments would reshape this pool most meaningfully?

**Entry:** Phase 1 exit gates passed.

Before you design the category structure: what three levers — each pulling in a different
direction — would most change what kinds of ideas surface for `{{topic}}`?

Answer with a table. Each lever must name what changes, how the pool would shift, and
which direction it pulls (Expands / Narrows / Redirects — all three must differ).

| # | What dimension shifts? | What changes specifically? | How does the pool shift? | Which direction? |
|---|----------------------|--------------------------|--------------------------|-----------------|
| A1 | | | | Expands |
| A2 | | | | Narrows |
| A3 | | | | Redirects |

If you find yourself writing two adjustments that both Expand (or both Narrow) →
rewrite the weaker one before continuing; they should pull in different directions.

**EXIT GATE:**
- [ ] Exactly 3 rows; all 4 columns filled per row
- [ ] All 3 directions differ
- [ ] Downstream effects name specific candidate types
- [ ] Any FAIL → correct in-place before Phase 3

---

#### Phase 3 — What category structure will organize this pool?

**Entry:** Phase 2 exit gates passed.

Before generating any ideas: what named sections will the pool be divided into? How many
ideas should each section hold? Which A1/A2/A3 adjustment motivated each section?

Answer with a table. Make sure no section holds more than 40% of the total pool.

| Category | What belongs here? | Target Count | % of Pool | Motivated by which AMEND adjustment? |
|----------|--------------------|--------------|-----------|--------------------------------------|
| | | | | |

Total: ______

If your largest category is 40% or more of the total → reduce its target count and
redistribute to underrepresented categories before continuing.

**EXIT GATE:**
- [ ] 4+ categories; % of Pool computed; no category > 40%; totals sum to 20–40
- [ ] Every row names an AMEND source; at least 3 cite A1/A2/A3
- [ ] Any FAIL → correct in-place before Phase 4

---

#### Phase 4 — What does the status quo look like — and why might someone prefer it?

**Entry:** Phase 3 exit gates passed.

Before generating alternatives: what is continuing as-is actually like for `{{topic}}`?
What does it cost? Why is it genuinely appealing? What would an alternative have to demonstrate
to justify the switch?

Answer with the anchor table. Use these exact field names (they were pre-committed in Phase 1):

| Field | Your answer for `{{topic}}` |
|-------|-----------------------------|
| Costs | |
| Benefits | |
| Competitive Threshold | (name a specific Phase 3 category in your answer) |
| Bypasses | (name at least one Phase 3 category) |
| Preserves | |
| Net Position | (does inertia dominate now? what specific condition would displace it?) |

**EXIT GATE:**
- [ ] All 6 fields answered, non-empty
- [ ] Competitive Threshold names a Phase 3 category
- [ ] Net Position names a specific displacement condition, not just "inertia is strong"
- [ ] Any FAIL → correct in-place before Phase 5

---

#### Phase 5 — What ideas exist for this topic?

**Entry:** Phase 4 exit gates passed.

Generate 20–40 idea names and pitches. Don't worry about categories or rationales yet —
that comes in Phase 6.

| # | Name | Pitch (one sentence) |
|---|------|---------------------|
| | | |

If you generate a pitch that doesn't distinguish the idea from another entry → either sharpen
it or drop the idea before continuing.

**EXIT GATE:**
- [ ] Count is 20–40; every row has Name and Pitch; no duplicate pitches
- [ ] Any FAIL → correct in-place before Phase 6

---

#### Phase 6 — How do these ideas fit the structure, and why does each one matter for this topic?

**Entry:** Phase 5 exit gates passed.

For every Phase 5 idea: which Phase 3 category does it belong to, and why does it specifically
serve `{{topic}}`?

| # | Name | Pitch | Category | Rationale (why specifically for `{{topic}}`) |
|---|------|-------|----------|--------------------------------------------|
| | | | | |

If any category fills beyond its Phase 3 target → note it inline and redistribute before
continuing. If a category hits 40% of total → redistribute immediately.

**EXIT GATE:**
- [ ] All 4 anatomy fields present for every row
- [ ] No category > 40%
- [ ] At least 4 of 5 sampled rationales are specific to `{{topic}}`
- [ ] Any FAIL → correct in-place before Phase 7

---

#### Phase 7 — Which candidates actually survive scrutiny?

**Entry:** Phase 6 exit gates passed.

Pick 8–10 candidates that look strongest. For each, ask: does it pass all 4 Phase 1 tests?
Do NOT assign `**` here — that's Phase 8.

| Candidate | T-1: Differentiation | T-2: Feasibility | T-3: Inertia Displacement (Costs · Competitive Threshold · Bypasses · Preserves) | T-4: Coverage | Overall |
|-----------|---------------------|-----------------|----------------------------------------------------------------------------------|---------------|---------|

For T-3: name which anchor dimensions the candidate clears.

If fewer than 5 pass Overall → document which tests the closest failures almost cleared.
Identify 5 finalists regardless.

**EXIT GATE:**
- [ ] 8–10 evaluated; all 4 tests applied; T-3 column names anchor field labels
- [ ] No `**` assigned; at least 5 finalists named
- [ ] Any FAIL → correct in-place before Phase 8

---

#### Phase 8 — Which 5 earn `**`?

**Entry:** Phase 7 exit gates passed.

Assign `**` to exactly 5 finalists from Phase 7. The 5 must represent at least 3 different
Phase 3 categories — if they don't, swap one same-category finalist for the strongest
underrepresented-category candidate.

**EXIT GATE:**
- [ ] Exactly 5 `**` marks
- [ ] 5 picks span 3+ distinct Phase 3 categories
- [ ] Any FAIL → correct in-place before Phase 9

---

#### Phase 9 — Does the output satisfy all criteria?

**Entry:** Phase 8 exit gates passed.

Row-by-row check (29 rows from V-01). Any FAIL → correct in-place before Phase 10.

**EXIT GATE:**
- [ ] All 29 checks PASS

---

#### Phase 10 — Write the artifact.

**Entry:** Phase 9 exit gates passed.

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure: Header → AMEND → Anchor (6 fields) → Challenge Criteria → Pool by category (with `**`) → Challenge Summary

---

## V-05 — Full Combination: Canonical + Schema Propagation + Pre-Scoring

**Variation axis:** Full combination — V-01 canonical lifecycle + V-02 schema propagation
(challenge IDs as column thread) + pre-scoring column in Phase 6 cluster (T-1/T-2/T-3
preliminary scores on every candidate before the formal adversarial phase).
**Hypothesis:** Pre-scoring every candidate in the cluster phase creates a running ledger of
challenge-test evidence that makes Phase 7 adversarial challenge more reliable. Rather than
asking the model to recall why a candidate is strong at Phase 7, the T-Evidence in Phase 6
has already recorded the evidence. The formal Phase 7 challenge becomes a threshold-application
step on pre-existing evidence, not a fresh judgment. This should reduce omission errors in
T-3 (Inertia Displacement) specifically, since the anchor fields are visible in every phase.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate 20–40 idea candidates; mark 5 with `**`. Execute all 10 phases in order. Every phase
opens with its entry condition and closes with its exit gate. The Phase 1 challenge test IDs
(T-1 through T-4) will be referenced as columns in Phases 3, 4, 6, and 7. A pre-scoring column
in Phase 6 builds the evidence base that Phase 7 will evaluate formally.

---

#### Phase 1 — Challenge Framework Declaration

**Entry:** Start of session. No prior phase.

Declare the challenge framework first. Test IDs T-1 through T-4 are the evaluation spine
of this entire session.

| ID | Test | Threshold | Surviving Means | Anchor Dimension |
|----|------|-----------|-----------------|------------------|
| T-1 | Differentiation | Zero overlap in core mechanism | Removing this candidate loses a distinct approach | N/A |
| T-2 | Feasibility | No unmet hard constraints for `{{topic}}` | Implementable without capabilities the topic lacks | N/A |
| T-3 | Inertia Displacement | Clears ≥2 of: **Costs · Competitive Threshold · Bypasses · Preserves** | Explicit advantage on 2+ Phase 4 anchor dimensions | Costs · Competitive Threshold · Bypasses · Preserves |
| T-4 | Coverage Contribution | Removal collapses `**` coverage to <3 categories | Contributes a category not otherwise in top 5 | N/A |

These criteria are pre-committed. Phase 6 will pre-score every candidate against them.
Phase 7 will apply them formally. No modifications permitted after this phase.

**EXIT GATE:**
- [ ] T-1 through T-4 all present; T-3 Anchor Dimension names: Costs, Competitive Threshold, Bypasses, Preserves
- [ ] Criteria locked; any FAIL → correct in-place before Phase 2

---

#### Phase 2 — AMEND Planning

**Entry:** Phase 1 exit gates passed.

Write 3 pool-shaping adjustments. These will drive category architecture in Phase 3.

| # | Dimension | Shift Description | Downstream Effect on Pool | Direction |
|---|-----------|-------------------|--------------------------|-----------|
| A1 | | | | Expands |
| A2 | | | | Narrows |
| A3 | | | | Redirects |

All 3 Directions must differ. Downstream Effect must name specific candidate types.
If two Directions match → rewrite the weaker one before continuing.

**EXIT GATE:**
- [ ] Exactly 3 rows; all 5 columns filled; all 3 Directions distinct
- [ ] Any FAIL → correct in-place before Phase 3

---

#### Phase 3 — Architecture Declaration

**Entry:** Phase 2 exit gates passed.

Declare category structure with AMEND Source, Primary Challenge Test, and % of Pool.

| Category | Description | Target Count | % of Pool | AMEND Source | Primary T-Test |
|----------|-------------|--------------|-----------|--------------|----------------|
| | | | | | |

Total: ______

- `AMEND Source`: which A1/A2/A3 adjustment motivated this category?
- `Primary T-Test`: which Phase 1 test does this category most directly support?
  At least one category must list T-3.
- No category may exceed 40%; redistribute if needed.
- Totals must sum to 20–40.

If your largest category is at or above 40% → redistribute before continuing.

**EXIT GATE:**
- [ ] 4+ categories; % of Pool computed; no category > 40%; totals sum to 20–40
- [ ] Every row has AMEND Source and Primary T-Test; at least 1 row lists T-3
- [ ] At least 3 rows cite A1/A2/A3
- [ ] Any FAIL → correct in-place before Phase 4

---

#### Phase 4 — Do Nothing Anchor

**Entry:** Phase 3 exit gates passed.

Write the 6-field anchor. Field names are pre-committed by Phase 1's T-3 Anchor Dimension column.
A `Challenge Binding` column traces each field back to the Phase 1 test it satisfies.

| Field | Content | Challenge Binding |
|-------|---------|-------------------|
| Costs | [specific to `{{topic}}`] | T-3 |
| Benefits | [genuine appeal of status quo] | T-3 |
| Competitive Threshold | [displacement bar; name a Phase 3 category explicitly] | T-3 |
| Bypasses | [Phase 3 categories rendered unnecessary; name at least one] | T-3 |
| Preserves | [what a transition would put at risk] | T-3 |
| Net Position | [integrative: does inertia dominate now? what specific condition displaces it?] | T-3 synthesis |

Field labels must match Phase 1 T-3 Anchor Dimension exactly. Net Position must name a
specific displacement condition, not merely directional language.

**EXIT GATE:**
- [ ] All 6 fields present and non-empty; field labels match Phase 1 T-3 exactly
- [ ] Competitive Threshold names a Phase 3 category; Net Position names a displacement condition
- [ ] Challenge Binding column present on every row
- [ ] Any FAIL → correct in-place before Phase 5

---

#### Phase 5 — Diverge (Name + Pitch Only)

**Entry:** Phase 4 exit gates passed.

Generate 20–40 idea names and one-line pitches. No categories or rationales here.

| # | Name | Pitch |
|---|------|-------|
| | | |

Do Nothing excluded (Phase 4 anchor). Stop at 40. Drop duplicate pitches.

**EXIT GATE:**
- [ ] Count is 20–40; every row has Name and Pitch; no duplicate pitches
- [ ] Any FAIL → correct in-place before Phase 6

---

#### Phase 6 — Cluster with Pre-Scoring

**Entry:** Phase 5 exit gates passed.

For every entry: assign Phase 3 category, write topic-specific rationale, and add a
`Pre-Score` column recording preliminary T-1/T-2/T-3/T-4 evidence.

| # | Name | Pitch | Category | Rationale | Pre-Score |
|---|------|-------|----------|-----------|-----------|
| | | | | | |

Pre-Score format: `T-1:PASS/PARTIAL/FAIL · T-2:PASS/PARTIAL/FAIL · T-3:[dims cleared] · T-4:PASS/PARTIAL/FAIL`

For T-3, name which of Costs / Competitive Threshold / Bypasses / Preserves the rationale
already demonstrates evidence for.

Rules:
- Category must be from Phase 3; rationale must reference `{{topic}}` specifically
- If a category exceeds 40% → redistribute before continuing
- Pre-Score is preliminary evidence; formal adjudication happens in Phase 7

**EXIT GATE:**
- [ ] All 5 columns present for every row (including Pre-Score)
- [ ] No category > 40%
- [ ] At least 4 of 5 sampled rationales are topic-specific
- [ ] Pre-Score column present with T-1/T-2/T-3/T-4 notation for every row
- [ ] Any FAIL → correct in-place before Phase 7

---

#### Phase 7 — Adversarial Challenge (Evidence-Informed)

**Entry:** Phase 6 exit gates passed.

Select 8–10 candidates with the strongest Phase 6 Pre-Scores as the challenge pool.
Apply Phase 1 tests formally using Phase 6 evidence as the starting point.
Do NOT assign `**` marks here.

| Candidate | T-1: Differentiation | T-2: Feasibility | T-3: Inertia Displacement (Costs · Competitive Threshold · Bypasses · Preserves) | T-4: Coverage Contribution | Ph6 Pre-Score | Overall |
|-----------|---------------------|-----------------|----------------------------------------------------------------------------------|---------------------------|---------------|---------|

- T-3 column header names the Phase 4 anchor field labels (as pre-committed in Phase 1)
- `Ph6 Pre-Score` carries forward the Phase 6 preliminary score for reference
- For T-3: confirm or revise Phase 6's preliminary evidence; name which dimensions cleared
- If <5 candidates pass all tests → document exceptions; identify 5 finalists

**EXIT GATE:**
- [ ] 8–10 candidates evaluated using Phase 6 Pre-Score as starting evidence
- [ ] All 4 Phase 1 tests applied; T-3 column names anchor field labels
- [ ] Ph6 Pre-Score column carried forward
- [ ] No `**` assigned; at least 5 finalists identified
- [ ] Any FAIL → correct in-place before Phase 8

---

#### Phase 8 — Selection

**Entry:** Phase 7 exit gates passed.

Assign `**` to exactly 5 Phase 7 finalists. The 5 must span at least 3 distinct Phase 3
categories. If they don't → swap the weakest same-category finalist for the strongest
underrepresented-category candidate, then assign marks.

**EXIT GATE:**
- [ ] Exactly 5 `**` marks in the Phase 6 cluster table
- [ ] 5 picks span 3+ distinct Phase 3 categories
- [ ] Any FAIL → correct in-place before Phase 9

---

#### Phase 9 — Verify

**Entry:** Phase 8 exit gates passed.

Run the 29-row checklist (from V-01). Additionally verify:
- [ ] Phase 6 cluster table has Pre-Score column with T-1/T-2/T-3/T-4 notation
- [ ] Phase 7 challenge table has Ph6 Pre-Score column
- [ ] T-3 column in Phase 7 names: Costs, Competitive Threshold, Bypasses, Preserves

Any FAIL → correct in-place before Phase 10.

**EXIT GATE:**
- [ ] All 29 V-01 checks PASS plus the 3 V-05 additional checks

---

#### Phase 10 — Write Artifact

**Entry:** Phase 9 exit gates passed.

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Structure:
1. Header: topic, date, candidate count, rubric version
2. AMEND section (from Phase 2)
3. Do Nothing Anchor — full 6-field table with Challenge Binding column (from Phase 4)
4. Challenge Criteria — pre-committed framework (from Phase 1)
5. Candidate pool by category with `**` marks (from Phase 6, updated from Phase 8)
   — include Pre-Score column in the pool table
6. Challenge Summary table (from Phase 7, including Ph6 Pre-Score column)

---

## R9 Variation Summary

| Variation | Key Structural Feature | C-28 | C-29 | Novel Above R8 |
|-----------|------------------------|------|------|----------------|
| V-01 | Canonical reference — maximally explicit, 29-row checklist | Phase 1 | Entry: on all phases | Gold standard baseline |
| V-02 | Schema propagation — T-1/T-2/T-3/T-4 as column thread through all phases | Phase 1 | Entry: on all phases | Challenge-to-Architecture binding column; T-Evidence in cluster |
| V-03 | Condensed PRE/DO/ASSERT contracts — same lifecycle, fewer words | Phase 1 PRE block | PRE: chains previous ASSERT | Concision without criterion loss |
| V-04 | Interrogative register — all instructions as questions | Phase 1 question | Entry: on all phases | Questions drive deliberate commitment before generation |
| V-05 | Full combination — canonical + schema propagation + Pre-Score in cluster | Phase 1 | Entry: on all phases | Pre-scoring every candidate in cluster creates running evidence ledger before Phase 7 |
