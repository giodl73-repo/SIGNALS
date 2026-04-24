# draft-brainstorm Skill Prompt Variations — Round 6

**Skill:** draft-brainstorm
**Round:** 6
**Date:** 2026-03-15
**Rubric:** v5 (C-01 through C-22)
**Target:** All 22 criteria pass in every variation. R5 established C-19 through C-22 as new aspirational criteria. R6 axes explore structural approaches that weren't available in R5 because those criteria didn't yet exist.

---

## R6 Axis Selection

R5 explored: per-phase exit gates (V-01), table format (V-02), architecture-before-anchor ordering (V-03), conversational register + inline conditionals (V-04), named adversarial persona + table format (V-05).

R6 explores new axes — all variations satisfy C-01 through C-22 as baseline, then vary on:

| Variation | Primary Axis | Novel Structural Choice |
|-----------|--------------|------------------------|
| V-01 | Role sequence | Challenge criteria declared **before** diverge — candidates generate knowing what they face |
| V-02 | Inertia framing | Do Nothing written as the **primary anchor** — all alternatives explicitly framed against it |
| V-03 | Lifecycle emphasis | **4-phase compressed** pipeline — planning / generation / selection / output |
| V-04 | Phrasing register | **Conversational dense** — parenthetical inline conditionals as natural coaching language |
| V-05 | Combination | Adversarial-first + inertia-centered + table format + per-phase gates + inline conditionals |

---

## Criteria Coverage Map

All 22 criteria must be satisfied in every variation.

| Criterion | Satisfied by |
|-----------|-------------|
| C-01 volume 20–40 | Diverge phase + exit gate |
| C-02 anatomy 4 fields | Cluster phase (table columns) |
| C-03 exactly 5 ** | Write phase (confirmed Top 5 only) |
| C-04 inertia present | Anchor phase (dedicated) |
| C-05 AMEND 3 adjustments | AMEND phase (Phase 1) |
| C-06 grouped by category | Cluster / Write phases |
| C-07 topic-specific rationale | Cluster phase instruction |
| C-08 4+ categories ≤40% | Architecture phase (% of Pool + cap check) |
| C-09 top 5 differentiated | Adversarial / Verify phases |
| C-10 AMEND non-overlapping | AMEND phase instruction |
| C-11 two-pass diverge/cluster | Phases: Diverge → Cluster |
| C-12 AMEND downstream effects | AMEND phase instruction |
| C-13 inertia costs + benefits | Anchor phase (both halves required) |
| C-14 structured verification | Verify phase (row-by-row checklist) |
| C-15 AMEND-first | Phase ordering (AMEND = Phase 1) |
| C-16 Do Nothing as anchor phase | Anchor = dedicated structural phase before Diverge |
| C-17 architecture pre-commitment | Architecture phase (slots + % + cap) before Diverge |
| C-18 adversarial before ** marks | Adversarial phase (** deferred until after challenge) |
| C-19 per-phase exit gates | Enumerated exit conditions at end of every phase |
| C-20 table format structural enforcement | Tables throughout; % of Pool column computed inline |
| C-21 architecture-before-anchor ordering | Sequence: AMEND → Architecture → Anchor → Diverge |
| C-22 inline conditional correction triggers | Mid-step "if X → adjust before continuing" triggers |

---

## V-01 — Role Sequence: Adversarial-First Declaration

**Variation axis:** Role sequence
**Hypothesis:** Declaring the adversarial challenge criteria *before* diverge — as an explicit Phase 4 that generates challenge tests the pool must survive — causes the model to self-censor weak candidates during generation rather than post-hoc. Candidates that wouldn't survive the declared tests are less likely to be generated in the first place. This makes the adversarial phase a selection event rather than a pruning event.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate a pool of 20–40 idea candidates. Work through these phases in strict order. Do not begin a phase until the previous phase's exit gate is satisfied.

---

#### Phase 1 — AMEND Adjustments

Before any candidates or architecture, write 3 pool-shaping adjustments.

| # | Dimension | Shift Description | Downstream Effect on Pool | Direction |
|---|-----------|-------------------|--------------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

Column rules:
- **Dimension**: the specific lever being moved (scope, audience, timeline, risk, implementation depth, etc.) — not a generic label
- **Downstream effect**: what types of candidates surface or disappear in `{{topic}}`'s pool — must name the topic
- **Direction**: one of: *expands / narrows / reframes / pivots / de-risks* — all 3 must differ

**Phase 1 exit gate:**
- [ ] Exactly 3 rows, all cells filled
- [ ] Every downstream effect references `{{topic}}` specifically
- [ ] All 3 Direction values are distinct

Any FAIL → correct in place before proceeding.

---

#### Phase 2 — Category Architecture

Declare the pool's shape before generating any ideas.

| Category | Target Slots | % of Pool | Cap Check (≤40%?) |
|----------|--------------|-----------|-------------------|
| Status Quo | 1 | [compute] | |
| | | | |
| | | | |
| **TOTAL** | | 100% | |

- At least 4 named categories including Status Quo
- Target slots sum: 20–40
- Compute % of Pool for every row before filling Cap Check

If any row's % of Pool exceeds 40%, redistribute slot counts now before continuing.

**Phase 2 exit gate:**
- [ ] ≥4 named categories
- [ ] Total slots: 20–40
- [ ] % of Pool computed for every row
- [ ] All Cap Check cells show PASS

Any FAIL → correct in place before proceeding.

---

#### Phase 3 — Status Quo Anchor

With the architecture committed, write the Do Nothing candidate. Ground it explicitly in the architectural landscape — name which categories it bypasses and which it implicitly preserves.

| Field | Content |
|-------|---------|
| Name | Do Nothing / [status quo label for `{{topic}}`] |
| Pitch | [one sentence: what continuing without change looks like] |
| Category | Status Quo |
| Benefits | [what the current state genuinely provides — why teams or users stay with it] |
| Costs | [what problems persist, compound, or foreclose without action] |
| Architectural note | [which Phase 2 categories this bypasses; which it implicitly preserves] |

Both Benefits and Costs are required. Architectural note must name at least one declared category.

**Phase 3 exit gate:**
- [ ] Pitch is specific to `{{topic}}`
- [ ] Benefits present — not just "zero effort"
- [ ] Costs present
- [ ] Architectural note names at least one Phase 2 category

Any FAIL → correct in place before proceeding.

---

#### Phase 4 — Challenge Criteria Declaration

Before generating any candidates, declare the adversarial challenge criteria the pool must survive. Generate candidates in Phase 5 knowing they will face these tests.

A strong candidate for `{{topic}}` must survive each of the following:

1. [Challenge criterion 1 — specific to `{{topic}}`: what assumption or feasibility test must it pass?]
2. [Challenge criterion 2 — specific to `{{topic}}`: what distinctiveness or redundancy test must it pass?]
3. [Challenge criterion 3 — specific to `{{topic}}`: what adoption or strategic alignment test must it pass?]

These criteria will be applied verbatim in Phase 6.

**Phase 4 exit gate:**
- [ ] Exactly 3 criteria
- [ ] All 3 are specific to `{{topic}}` — not generic "must be feasible"
- [ ] Each criterion names a distinct type of pressure (assumption / distinctiveness / adoption, or comparable non-overlapping dimensions)

Any FAIL → correct in place before proceeding.

---

#### Phase 5a — Diverge (names + pitches only)

Generate names and one-line pitches, targeting Phase 2 slot counts. No categories or rationales in this pass.

As you generate, keep the Phase 4 challenge criteria visible — ideas that cannot plausibly survive any of the three tests are weak candidates.

| # | Name | Pitch |
|---|------|-------|
| 1 | | |
| 2 | | |
| ... | | |

If your running total for any single category would exceed 40% of the ideas generated so far, add ideas from underrepresented categories before continuing.

**Phase 5a exit gate:**
- [ ] Row count matches Phase 2 total slot target (±2)
- [ ] No single category visually dominates the list

Any FAIL → add ideas to underrepresented categories before proceeding.

---

#### Phase 5b — Cluster (complete all 4 fields)

For every row above, add Category and Rationale.

| # | Name | Pitch | Category | Rationale |
|---|------|-------|----------|-----------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

- Category must match a Phase 2 declared category name exactly
- Rationale must reference `{{topic}}` — if it could apply to any feature, rewrite it
- Include the Do Nothing candidate (Phase 3) in the Status Quo row

**Phase 5b exit gate:**
- [ ] Every row has all 4 fields filled (no empty cells)
- [ ] Total candidates: ≥20 and ≤40
- [ ] No category holds >40% of total (recheck % of Pool from Phase 2)
- [ ] All rationales reference `{{topic}}`

Any FAIL → correct in place before proceeding.

---

#### Phase 6 — Adversarial Challenge

Apply the Phase 4 criteria. No `**` marks until after this phase.

**6a — Tentative nominations:**

| Pick | Name | Why It Looks Strong |
|------|------|---------------------|
| T1 | | |
| T2 | | |
| T3 | | |
| T4 | | |
| T5 | | |

**6b — Challenge each pick against Phase 4 criteria:**

| Pick | Phase 4 Criterion Applied | Specific Objection | Verdict | Outcome |
|------|--------------------------|-------------------|---------|---------|
| T1 | | | SURVIVE / ELIMINATE | |
| T2 | | | SURVIVE / ELIMINATE | |
| T3 | | | SURVIVE / ELIMINATE | |
| T4 | | | SURVIVE / ELIMINATE | |
| T5 | | | SURVIVE / ELIMINATE | |

For ELIMINATE: name the replacement from the pool and explain why it fares better against the applied criterion.

**6c — Confirmed Top 5:** [list names — only these receive `**` marks]

**Phase 6 exit gate:**
- [ ] Every pick challenged against a named Phase 4 criterion
- [ ] Each verdict is SURVIVE or ELIMINATE — no blanks
- [ ] Exactly 5 confirmed picks named
- [ ] Confirmed Top 5 spans ≥3 distinct categories

Any FAIL → correct before proceeding.

---

#### Phase 7 — Verify

| Check | Criterion | Status |
|-------|-----------|--------|
| Candidate count: 20–40 | C-01 | |
| Every candidate has name, pitch, category, rationale | C-02 | |
| Exactly 5 `**` marks (confirmed Top 5 only) | C-03 | |
| Do Nothing: pitch + benefits + costs | C-04, C-13 | |
| AMEND: 3 rows, dimension + downstream effect + direction | C-05, C-10, C-12 | |
| ≥4 categories, all cap checks PASS | C-08 | |
| Top 5 spans ≥3 categories | C-09 | |
| All Top 5 passed adversarial challenge or were replaced | C-18 | |
| Challenge criteria declared before diverge | C-18 | |
| All rationales reference `{{topic}}` | C-07 | |
| Tables used with % of Pool computed | C-20 | |
| Architecture precedes anchor in phase ordering | C-21 | |
| Inline cap check trigger present in Phase 5a | C-22 | |

Fix any FAIL before writing.

---

#### Phase 8 — Write Artifact

Write to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`.

Structure:
1. **AMEND** — 3-row table (Dimension | Shift | Downstream Effect | Direction)
2. **Category Architecture** — table with Target Slots and % of Pool
3. Candidate pool under category headings — tables with Name | Pitch | Rationale columns; `**` on confirmed Top 5
4. Do Nothing appears first in the Status Quo section

---

---

## V-02 — Inertia Framing: Do Nothing as Primary Anchor

**Variation axis:** Inertia framing
**Hypothesis:** Positioning the Do Nothing candidate as the explicit, highest-prominence entry in the pipeline — written in the most structural detail, placed first in the artifact, and framing every alternative as a response to it — produces a more honest, well-grounded pool. Teams evaluating the pool naturally compare against the baseline rather than against each other. The status quo earns the most scrutiny because it is the default choice, not an afterthought.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate a pool of 20–40 idea candidates. The organizing center of this brainstorm is the status quo — every alternative is evaluated as an answer to: "why is this better than doing nothing?" Work through these phases in strict order.

---

#### Phase 1 — AMEND Adjustments

Write 3 adjustments before any candidates. These shape what categories and alternatives get generated.

| # | Dimension | Shift Description | Downstream Effect on `{{topic}}` Pool | Direction |
|---|-----------|-------------------|---------------------------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

Direction values must be distinct across all 3 rows. Downstream effects must name `{{topic}}`.

**Phase 1 exit gate:**
- [ ] Exactly 3 rows, all cells filled
- [ ] All downstream effects reference `{{topic}}`
- [ ] All 3 directions are distinct

Any FAIL → correct before proceeding.

---

#### Phase 2 — Category Architecture

Declare the pool's shape before any idea is generated.

| Category | Target Slots | % of Pool | Cap Check (≤40%?) |
|----------|--------------|-----------|-------------------|
| Status Quo | 1 | [compute] | PASS |
| | | | |
| | | | |
| **TOTAL** | | 100% | |

At least 4 named categories, total 20–40. Compute % of Pool for every row. If any row would exceed 40%, redistribute now.

**Phase 2 exit gate:**
- [ ] ≥4 categories
- [ ] Total: 20–40
- [ ] % computed for all rows
- [ ] All cap checks PASS

Any FAIL → correct before proceeding.

---

#### Phase 3 — Do Nothing: The Primary Anchor

Write the Do Nothing candidate as the authoritative baseline. This is the most detailed entry in the artifact — every alternative will be measured against it.

**Entry format:**

| Field | Content |
|-------|---------|
| Name | **Do Nothing — `{{topic}}`** |
| Pitch | [one sentence: what life looks like if nothing changes] |
| Category | Status Quo |
| Who benefits from inertia | [which team roles or users are served well by the current state] |
| What inertia protects | [what the status quo preserves — existing workflows, sunk costs, cognitive familiarity] |
| What inertia costs | [what problems compound without action — specific to `{{topic}}`] |
| Competitive threshold | [what would an alternative need to offer to justify displacing this — name the bar] |

The *Competitive threshold* field makes Do Nothing an active competitor: alternatives that clear the bar are viable; those that don't are pool noise.

**Phase 3 exit gate:**
- [ ] All 7 fields present
- [ ] "Who benefits" names specific roles or user types
- [ ] "Competitive threshold" sets a concrete bar — not just "must be better"

Any FAIL → correct before proceeding.

---

#### Phase 4 — Diverge (names + pitches only)

Generate names and pitches targeting Phase 2 slot counts. No categories or rationales in this pass.

Keep the Phase 3 competitive threshold visible — generate ideas with the implicit question: does this clear the bar?

| # | Name | Pitch |
|---|------|-------|
| 1 | | |
| 2 | | |
| ... | | |

If any category grows to represent 40%+ of your running total, add ideas from underrepresented categories before continuing.

**Phase 4 exit gate:**
- [ ] Row count matches Phase 2 total target (±2)
- [ ] Do Nothing already exists (from Phase 3) — it does not need a row here

Any FAIL → add rows from underrepresented categories before proceeding.

---

#### Phase 5 — Cluster (complete all 4 fields)

Assign Category and Rationale to every Phase 4 row. For rationale: frame each idea's value relative to the Do Nothing baseline — why does this beat the status quo for `{{topic}}`?

| # | Name | Pitch | Category | Rationale (why this beats Do Nothing for `{{topic}}`) |
|---|------|-------|----------|----------------------------------------------------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

- Category must match a Phase 2 category name exactly
- Rationale that doesn't reference the Do Nothing baseline or `{{topic}}` is not sufficient

Include Do Nothing (Phase 3) in the Status Quo section.

**Phase 5 exit gate:**
- [ ] All 4 fields on every row
- [ ] Total: ≥20 and ≤40
- [ ] No category >40%
- [ ] All rationales reference `{{topic}}`

Any FAIL → correct before proceeding.

---

#### Phase 6 — Adversarial Challenge

Identify 5 tentative top picks. Do not mark `**` yet.

**6a — Nominations:**

| Pick | Name | Why It Looks Strong |
|------|------|---------------------|
| T1 | | |
| T2 | | |
| T3 | | |
| T4 | | |
| T5 | | |

**6b — Test against the Phase 3 competitive threshold:**

For each pick: does it clear the Do Nothing competitive threshold? Write the specific argument for why it does or does not. Verdict: SURVIVE or ELIMINATE.

| Pick | Threshold Test | Verdict | Outcome |
|------|----------------|---------|---------|
| T1 | [does it clear the bar? how?] | SURVIVE / ELIMINATE | |
| T2 | | | |
| T3 | | | |
| T4 | | | |
| T5 | | | |

For ELIMINATE: name the replacement from the pool. It must also survive the threshold test.

**6c — Confirmed Top 5:** [names — only these receive `**` marks]

Check: spans ≥3 distinct categories.

**Phase 6 exit gate:**
- [ ] All 5 picks tested against the Phase 3 threshold
- [ ] Exactly 5 confirmed picks
- [ ] Spans ≥3 categories

Any FAIL → correct before proceeding.

---

#### Phase 7 — Verify

| Check | Criterion | Status |
|-------|-----------|--------|
| Candidate count: 20–40 | C-01 | |
| Every candidate: name, pitch, category, rationale | C-02 | |
| Exactly 5 `**` marks | C-03 | |
| Do Nothing: pitch + benefits + costs (+ threshold) | C-04, C-13 | |
| AMEND: 3 rows, dimension + downstream effect, distinct directions | C-05, C-10, C-12 | |
| ≥4 categories, all cap checks PASS | C-08 | |
| Top 5 spans ≥3 categories | C-09 | |
| All Top 5 survived threshold test or replaced | C-18 | |
| Tables with % of Pool column | C-20 | |
| Architecture before anchor in phase ordering | C-21 | |
| Inline cap check trigger present in Phase 4 | C-22 | |

Fix any FAIL before writing.

---

#### Phase 8 — Write Artifact

Write to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`.

Structure:
1. **AMEND** — table (Dimension | Shift | Downstream Effect | Direction)
2. **Status Quo** section first — Do Nothing entry prominent, includes competitive threshold
3. Remaining candidate pool under category headings — tables with Name | Pitch | Rationale; `**` on confirmed Top 5

---

---

## V-03 — Lifecycle Emphasis: Compressed 4-Phase Pipeline

**Variation axis:** Lifecycle emphasis
**Hypothesis:** Reducing 7–8 named phases to 4 dense phases — Planning / Generation / Selection / Output — lowers phase-switching overhead while retaining all structural mechanisms. Each compressed phase contains multiple sub-steps with their own inline conditionals and exit gates. The hypothesis is that fewer named boundaries reduce friction without sacrificing structural discipline.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate a pool of 20–40 idea candidates. Work through 4 phases in strict order. Each phase contains multiple sub-steps. Complete every sub-step before advancing.

---

#### Phase 1 — Plan (AMEND + Architecture + Anchor)

**Step 1.1 — AMEND Adjustments**

Write 3 pool-shaping adjustments. Table format required.

| # | Dimension | Shift | Downstream Effect on Pool | Direction |
|---|-----------|-------|--------------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

Downstream effects must name `{{topic}}`. All 3 directions must differ.

**Step 1.2 — Category Architecture**

With AMEND adjustments visible, declare the pool's shape.

| Category | Target Slots | % of Pool | Cap Check (≤40%?) |
|----------|--------------|-----------|-------------------|
| Status Quo | 1 | [compute] | |
| | | | |
| **TOTAL** | | 100% | |

At least 4 categories. Total: 20–40. Compute % of Pool for every row. If any row exceeds 40%, redistribute now before continuing to Step 1.3.

**Step 1.3 — Status Quo Anchor**

With architecture committed, write Do Nothing. Ground it in the architectural landscape — which declared categories does the status quo bypass? Which does it implicitly preserve?

| Field | Content |
|-------|---------|
| Name | Do Nothing / `{{topic}}` |
| Pitch | |
| Category | Status Quo |
| Benefits | [why inertia is appealing — what teams or users keep] |
| Costs | [what compounds or forecloses without action] |
| Bypasses | [named Phase 1.2 categories this bypasses] |
| Preserves | [named Phase 1.2 categories this implicitly serves] |

Both Benefits and Costs required. Bypasses/Preserves must name at least one declared category each.

**Phase 1 exit gate:**
- [ ] AMEND: 3 rows, all cells filled, distinct directions
- [ ] Architecture: ≥4 categories, total 20–40, % computed, all cap checks PASS
- [ ] Anchor: benefits, costs, and architectural notes all present

Any FAIL → correct the specific sub-step before proceeding to Phase 2.

---

#### Phase 2 — Generate (Diverge + Cluster)

**Step 2.1 — Diverge**

Generate names and pitches targeting Phase 1.2 slot counts. Names and pitches only — no categories or rationales.

| # | Name | Pitch |
|---|------|-------|
| 1 | | |
| 2 | | |
| ... | | |

If any single category of ideas reaches 40%+ of your running count, add ideas from underrepresented categories before continuing.

**Step 2.2 — Cluster**

Extend every row above with Category and Rationale.

| # | Name | Pitch | Category | Rationale |
|---|------|-------|----------|-----------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Category must match a Phase 1.2 name. Rationale must reference `{{topic}}` — if the same sentence could describe any feature, rewrite it.

Include Do Nothing (Phase 1.3) in the Status Quo row.

**Phase 2 exit gate:**
- [ ] Total candidates: ≥20 and ≤40
- [ ] Every row has all 4 fields (no empty cells)
- [ ] No category holds >40% of total
- [ ] All rationales reference `{{topic}}`
- [ ] Two-pass structure preserved (diverge table before cluster table)

Any FAIL → correct before proceeding to Phase 3.

---

#### Phase 3 — Select (Adversarial Challenge)

**Step 3.1 — Tentative nominations** (no `**` marks yet):

| Pick | Name | Why It Looks Strong |
|------|------|---------------------|
| T1 | | |
| T2 | | |
| T3 | | |
| T4 | | |
| T5 | | |

**Step 3.2 — Challenge each pick:**

Write a serious objection for each — a reason it might fail, misread the problem, or be weaker than it appears for `{{topic}}`. Verdict: SURVIVE or ELIMINATE.

| Pick | Adversarial Objection | Verdict | Outcome |
|------|----------------------|---------|---------|
| T1 | | SURVIVE / ELIMINATE | [defense or replacement] |
| T2 | | | |
| T3 | | | |
| T4 | | | |
| T5 | | | |

For ELIMINATE: name the replacement from the pool; explain why it is more defensible.

**Step 3.3 — Confirmed Top 5:** [names — only these receive `**` marks]

Verify: confirmed Top 5 spans ≥3 distinct categories. If not, reconsider.

**Phase 3 exit gate:**
- [ ] All 5 tentative picks challenged with specific objections
- [ ] Exactly 5 confirmed picks named
- [ ] Confirmed Top 5 spans ≥3 categories

Any FAIL → correct before proceeding to Phase 4.

---

#### Phase 4 — Output (Verify + Write)

**Step 4.1 — Verify**

| Check | Criterion | Status |
|-------|-----------|--------|
| Candidates: 20–40 | C-01 | |
| All 4 fields on every entry | C-02 | |
| Exactly 5 `**` marks | C-03 | |
| Do Nothing: pitch + benefits + costs | C-04, C-13 | |
| AMEND: 3 rows, dimension + downstream effect, distinct directions | C-05, C-10, C-12 | |
| ≥4 categories, all cap checks PASS | C-08 | |
| Top 5 spans ≥3 categories | C-09 | |
| Two-pass structure (diverge then cluster) | C-11 | |
| All Top 5 challenged | C-18 | |
| Per-phase exit gates present in all phases | C-19 | |
| % of Pool column computed in architecture | C-20 | |
| Architecture before anchor (Step 1.2 before 1.3) | C-21 | |
| Inline conditional trigger in Phase 2.1 | C-22 | |

Fix any FAIL before writing.

**Step 4.2 — Write Artifact**

Write to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`.

Structure:
1. **AMEND** — 3-row table
2. **Category Architecture** — table with % of Pool
3. Candidate pool under category headings — tables; `**` on confirmed Top 5
4. Status Quo section contains Do Nothing with full anchor detail

---

---

## V-04 — Phrasing Register: Conversational Dense

**Variation axis:** Phrasing register
**Hypothesis:** Writing every instruction in a natural, coaching-voice register — with inline conditionals embedded as parenthetical advice inside generation steps rather than as structured gates — produces the most natural rationale prose and the least mechanical output. The conversational register makes inline error interception feel like guidance rather than enforcement, which may improve compliance in practice. Dense inline conditionals (one per generation step) provide the C-22 mechanism without disrupting the flow of the prompt.

---

### Prompt Body

You're running draft-brainstorm for the topic: `{{topic}}`

The goal: generate a pool of 20–40 idea candidates — more than you need, so you can rank and filter. Here's how to work through it. Take each step in full before moving on.

---

#### Step 1 — Write your three pool-shaping adjustments first

Before any ideas, write down three ways you could tilt this pool in a different direction. Do these first because they'll change what categories and ideas you reach for.

For each one, put it in a table row — you want to be precise here:

| # | Dimension | What shifts | Effect on the pool for `{{topic}}` | Direction |
|---|-----------|-------------|-----------------------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

A useful adjustment names a specific dimension (scope, audience, timeline, risk profile) and says what that shift would do to the kinds of ideas that show up. "Be more creative" isn't a dimension — name the actual lever.

The three adjustments should pull in different directions. If you find you've written three variations of "more ambitious," that's a single direction repeated — pick genuinely distinct dimensions before moving on.

Once you've got all three rows filled and each direction is distinct, move to Step 2.

---

#### Step 2 — Map out the category shape before generating ideas

With your AMEND adjustments visible, think about what categories this topic's idea space naturally breaks into. Put them in a table so the shape is committed before you generate:

| Category | Target Slots | % of Pool | Cap Check (≤40%?) |
|----------|--------------|-----------|-------------------|
| Status Quo | 1 | [compute] | |
| | | | |
| **TOTAL** | | 100% | |

Fill in the % of Pool column for every row — it's the only way to catch a category that's grown too large. You want at least four distinct categories, a total between 20 and 40, and no single category holding more than 40% of the pool.

If you add up the % column and your biggest category is at 40% or more, redistribute the target slots now before moving on — you'll be fighting the concentration problem in every phase that follows if you don't fix it here.

Once the architecture table is filled and every cap check says PASS, move to Step 3.

---

#### Step 3 — Write the Do Nothing candidate as its own dedicated entry

Before writing any alternatives, take a moment to describe the status quo honestly. It's a real competitor to every other idea on this list.

Write it in a table of its own:

| Field | Content |
|-------|---------|
| Name | Do Nothing / [status quo label for `{{topic}}`] |
| Pitch | [one sentence: what continuing without change looks like] |
| Category | Status Quo |
| Why appealing | [what the current state gives teams or users that they'd lose by changing] |
| What it costs | [what problems don't get solved, what compounds, what closes off] |
| Architecture note | [which categories from Step 2 does the status quo bypass? which does it implicitly serve?] |

You need both sides — the appeal and the cost. An entry that only lists the costs is advocacy for change, not an honest description of the baseline. The architecture note makes this entry useful later when you're comparing it to alternatives.

Once you've got all fields filled with both halves present, move to Step 4.

---

#### Step 4 — Generate names and pitches, freely

Now generate ideas. Use the category map from Step 2 as your guide — work through each category, aiming for the slot count you set.

In this pass, just names and pitches:

| # | Name | Pitch |
|---|------|-------|
| 1 | | |
| 2 | | |
| ... | | |

Don't add categories or rationales yet — this is the diverge pass. Generate freely.

One thing to watch as you fill rows: if you notice ideas for one category are stacking up and you're already at or above 40% of your running total, pull back from that category and add ideas from the ones with fewer entries before continuing. The architecture table you built in Step 2 is the target — work toward it.

Once you've hit the total target from Step 2, move to Step 4b.

---

#### Step 4b — Add category and rationale to everything

Go through every row from Step 4 and extend it with two more columns:

| # | Name | Pitch | Category | Rationale |
|---|------|-------|----------|-----------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Category must match one of the names from your Step 2 table exactly. Rationale is where you explain why this specific idea serves `{{topic}}` — not a generic sentence that would fit any feature. If you write "improves the developer experience" and that sentence would be equally true for any idea you generate, go one level deeper and say what it improves specifically for `{{topic}}`.

Include the Do Nothing entry from Step 3 in the Status Quo row.

Once every row has all four fields filled and the total is between 20 and 40, move to Step 5.

---

#### Step 5 — Challenge your tentative top five before marking them

From the pool above, pick five ideas that feel like the strongest candidates — but don't mark them `**` yet. Write them down first:

| Pick | Name | Why you like it |
|------|------|-----------------|
| T1 | | |
| T2 | | |
| T3 | | |
| T4 | | |
| T5 | | |

Now push back on each one. What's the strongest reason each of these might not work for `{{topic}}`? What assumption might be wrong, or what might make it harder to pull off than it looks? Write the objection, then decide: does it survive, or should you replace it?

| Pick | Adversarial objection | Verdict | What happens |
|------|----------------------|---------|-------------|
| T1 | | SURVIVE / ELIMINATE | [defense or replacement + why it's more defensible] |
| T2 | | | |
| T3 | | | |
| T4 | | | |
| T5 | | | |

If you eliminate one, bring in the next-strongest candidate from the rest of the pool and run the same pressure test on it before accepting it as a replacement.

Once all five have been ruled on, you have your confirmed Top 5. These are the only ones that get `**` marks. Check that they span at least three different categories — five variations on the same approach isn't a useful set of top picks.

---

#### Step 6 — Check your work before writing

Go through this list and mark each item before writing:

| What to check | Criterion | OK? |
|---------------|-----------|-----|
| Count: 20–40 candidates (count the rows) | C-01 | |
| Every candidate has name, pitch, category, rationale | C-02 | |
| Exactly 5 `**` marks — confirmed Top 5 only | C-03 | |
| Do Nothing has pitch + appeal + costs | C-04, C-13 | |
| AMEND: 3 rows, dimension + downstream effect | C-05, C-12 | |
| AMEND: all 3 directions distinct | C-10 | |
| ≥4 categories, all cap checks PASS | C-08 | |
| Top 5 spans ≥3 categories | C-09 | |
| Two-pass: diverge table then cluster table | C-11 | |
| All Top 5 challenged before `**` assignment | C-18 | |
| % of Pool computed in architecture table | C-20 | |
| Architecture before anchor in step ordering | C-21 | |
| Inline conditional in Step 4 ("if >40%, adjust before continuing") | C-22 | |

If anything is off, fix it in the pool above before writing. Don't move to writing until this list is clean.

---

#### Step 7 — Write the artifact

Write to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`.

Include:
1. **AMEND** — your 3-row table showing dimension, shift, downstream effect, direction
2. Candidate pool under category headings — tables with Name | Pitch | Rationale columns; `**` marks on the confirmed Top 5
3. Status Quo section has Do Nothing as its own full entry with both appeal and costs

---

---

## V-05 — Combination: Adversarial-First + Inertia-Centered + Table + Gates + Inline Conditionals

**Variation axes:** Role sequence (adversarial-first declaration) + Inertia framing (Do Nothing as primary anchor) + Output format (table throughout) + Lifecycle emphasis (per-phase exit gates) + Phrasing register (inline conditionals)
**Hypothesis:** The maximum-coverage pipeline — combining every mechanism from V-01 through V-04 into a single coherent structure — represents the ceiling for this rubric. The two novel axes from R6 (adversarial-first declaration and inertia-centered framing) compound: declaring challenge criteria before diverge and making Do Nothing the primary anchor creates a pool where every alternative knows both what it needs to beat (the baseline) and what pressure it will face (the challenge criteria). This should produce the most defensible top-5 selection of any variation.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate a pool of 20–40 idea candidates. The organizing principle: the status quo is the default winner until an idea earns its place. Work through these phases in strict order. All structured outputs use table format.

---

#### Phase 1 — AMEND Adjustments

Write 3 pool-shaping adjustments before any architecture, anchor, or candidates.

| # | Dimension | Shift | Downstream Effect on `{{topic}}` Pool | Direction |
|---|-----------|-------|---------------------------------------|-----------|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |

- Dimension: the specific lever (scope, audience, timeline, risk, implementation depth — not generic)
- Downstream effect: what candidate types appear or disappear; must name `{{topic}}`
- Direction: distinct across all 3 rows (expands / narrows / reframes / pivots / de-risks)

**Phase 1 exit gate:**
- [ ] Exactly 3 rows, all cells filled
- [ ] All downstream effects name `{{topic}}`
- [ ] All 3 directions are distinct

Any FAIL → correct before proceeding.

---

#### Phase 2 — Category Architecture

With AMEND adjustments visible, declare the pool's shape.

| Category | Target Slots | % of Pool | Cap Check (≤40%?) |
|----------|--------------|-----------|-------------------|
| Status Quo | 1 | [compute] | |
| | | | |
| | | | |
| **TOTAL** | | 100% | |

Fill % of Pool for every row. If any category would exceed 40%, redistribute target slots now — the cap is enforced here, not at the end.

**Phase 2 exit gate:**
- [ ] ≥4 named categories including Status Quo
- [ ] Total slots: 20–40
- [ ] % of Pool computed for every row
- [ ] All Cap Check cells show PASS

Any FAIL → correct before proceeding.

---

#### Phase 3 — Do Nothing: Primary Anchor

With architecture committed, write the Do Nothing candidate. This is the most structurally detailed entry in the artifact — every alternative will be measured against it.

| Field | Content |
|-------|---------|
| Name | Do Nothing — `{{topic}}` |
| Pitch | [one sentence: what continuing without change looks like] |
| Category | Status Quo |
| Who benefits from inertia | [which roles or users the current state serves well] |
| What inertia protects | [existing workflows, sunk costs, familiarity — be specific] |
| What inertia costs | [what compounds or forecloses without action — specific to `{{topic}}`] |
| Competitive threshold | [what an alternative must offer to justify displacing this] |
| Bypasses | [Phase 2 categories the status quo bypasses] |
| Preserves | [Phase 2 categories the status quo implicitly serves] |

All 9 fields required. Competitive threshold must be concrete. Bypasses/Preserves must name at least one declared category each.

**Phase 3 exit gate:**
- [ ] All 9 fields present
- [ ] Competitive threshold is concrete (not just "must be better")
- [ ] Bypasses and Preserves name at least one Phase 2 category each

Any FAIL → correct before proceeding.

---

#### Phase 4 — Challenge Criteria Declaration

Before generating any candidates, declare the adversarial tests the pool must survive. Generate in Phase 5 knowing these criteria exist.

For `{{topic}}`, a strong candidate must survive:

| # | Challenge Criterion | Type |
|---|---------------------|------|
| C1 | [feasibility/assumption test specific to `{{topic}}`] | feasibility |
| C2 | [distinctiveness/redundancy test specific to `{{topic}}`] | distinctiveness |
| C3 | [Phase 3 threshold alignment test] | threshold |

Criterion C3 must be grounded in the Phase 3 competitive threshold.

**Phase 4 exit gate:**
- [ ] Exactly 3 criteria
- [ ] C3 references the Phase 3 competitive threshold explicitly
- [ ] All 3 are specific to `{{topic}}`
- [ ] The 3 types are distinct (no two feasibility tests, etc.)

Any FAIL → correct before proceeding.

---

#### Phase 5a — Diverge (names + pitches only)

Generate names and pitches targeting Phase 2 slot counts. No categories or rationales. Keep Phase 3 anchor and Phase 4 criteria visible.

| # | Name | Pitch |
|---|------|-------|
| 1 | | |
| 2 | | |
| ... | | |

After every 5 rows: if any single category of ideas now represents ≥40% of your running count, add rows from underrepresented categories before continuing.

**Phase 5a exit gate:**
- [ ] Row count matches Phase 2 total target (±2)
- [ ] No category visually dominates the diverge table

Any FAIL → add rows to underrepresented categories before proceeding.

---

#### Phase 5b — Cluster (complete all 4 fields)

Extend every Phase 5a row with Category and Rationale.

| # | Name | Pitch | Category | Rationale |
|---|------|-------|----------|-----------|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

- Category: must match a Phase 2 declared name exactly
- Rationale: must reference `{{topic}}` and explain why this beats the Phase 3 baseline — generic boilerplate fails
- Include Do Nothing (Phase 3) in the Status Quo row

**Phase 5b exit gate:**
- [ ] Every row has all 4 fields filled
- [ ] Total: ≥20 and ≤40
- [ ] No category holds >40% of total
- [ ] All rationales reference `{{topic}}`

Any FAIL → correct before proceeding.

---

#### Phase 6 — Adversarial Challenge

Apply Phase 4 criteria. No `**` marks until confirmed.

**6a — Tentative nominations:**

| Pick | Name | Why It Looks Strong |
|------|------|---------------------|
| T1 | | |
| T2 | | |
| T3 | | |
| T4 | | |
| T5 | | |

**6b — Challenge against Phase 4 criteria:**

| Pick | Criterion Applied | Specific Objection | Verdict | Outcome |
|------|------------------|--------------------|---------|---------|
| T1 | C[1/2/3] | | SURVIVE / ELIMINATE | |
| T2 | | | | |
| T3 | | | | |
| T4 | | | | |
| T5 | | | | |

For ELIMINATE: name replacement from pool; it must survive the same criterion before acceptance.

**6c — Confirmed Top 5:** [list names — only these receive `**` marks]

Verify: confirmed Top 5 spans ≥3 distinct categories and each represents a meaningfully distinct approach (removing any one would lose a distinct angle).

**Phase 6 exit gate:**
- [ ] All 5 picks challenged against a named Phase 4 criterion
- [ ] Exactly 5 confirmed picks
- [ ] Spans ≥3 categories
- [ ] Each pick represents a distinct approach (no two are variations of the same idea)

Any FAIL → correct before proceeding.

---

#### Phase 7 — Verify

| Check | Criterion | Status |
|-------|-----------|--------|
| Candidates: 20–40 | C-01 | |
| All 4 fields on every candidate | C-02 | |
| Exactly 5 `**` marks | C-03 | |
| Do Nothing: pitch + benefits + costs | C-04, C-13 | |
| AMEND: 3 rows, dimension + downstream effect, distinct directions | C-05, C-10, C-12 | |
| ≥4 categories, all cap checks PASS | C-08 | |
| Top 5 spans ≥3 categories, distinct approaches | C-09 | |
| Two-pass: diverge table before cluster table | C-11 | |
| All Top 5 survived adversarial challenge | C-18 | |
| Per-phase exit gates present in all phases | C-19 | |
| Tables used; % of Pool computed in architecture | C-20 | |
| Architecture (Phase 2) before anchor (Phase 3) | C-21 | |
| Inline conditional triggers in Phase 5a | C-22 | |
| Challenge criteria declared before diverge | C-18 / V-01 | |
| Do Nothing includes competitive threshold | C-13 / V-02 | |

Fix any FAIL before writing.

---

#### Phase 8 — Write Artifact

Write to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`.

Structure:
1. **AMEND** — 3-row table (Dimension | Shift | Downstream Effect | Direction)
2. **Category Architecture** — table with Target Slots and % of Pool
3. **Status Quo** — Do Nothing entry first, full 9-field table
4. Candidate pool under remaining category headings — tables with Name | Pitch | Rationale; `**` on confirmed Top 5

---

---

## Variation Summary

| Variation | Primary Axis | Novel Structural Choice | Key Criteria Targeted |
|-----------|--------------|------------------------|-----------------------|
| V-01 | Role sequence | Challenge criteria declared before diverge | C-18 (adversarial depth), C-04 (inertia as competitor) |
| V-02 | Inertia framing | Do Nothing as primary anchor with competitive threshold | C-13 (costs+benefits), C-04, C-18 (threshold-based challenge) |
| V-03 | Lifecycle emphasis | 4-phase compressed pipeline (Planning / Generate / Select / Output) | C-19 (gates), C-11 (two-pass), C-17 (architecture) |
| V-04 | Phrasing register | Conversational dense with parenthetical inline conditionals | C-22 (inline triggers), C-07 (topic-specific rationale) |
| V-05 | Combination | Adversarial-first + inertia-centered + table + gates + inline | All C-01 through C-22 |

## Criteria Coverage Verification — All 22 Criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 volume 20–40 | P5b exit | P5b exit | P2 exit | S4b | P5b exit |
| C-02 anatomy 4 fields | P5b cluster table | P5b cluster table | P2.2 table | S4b table | P5b table |
| C-03 exactly 5 ** | P8 write | P8 write | P4 write | S7 write | P8 write |
| C-04 inertia present | P3 anchor | P3 anchor | P1.3 anchor | S3 | P3 anchor |
| C-05 AMEND 3 adjustments | P1 | P1 | P1.1 | S1 | P1 |
| C-06 grouped by category | P8 structure | P8 structure | P4 structure | S7 | P8 structure |
| C-07 topic-specific rationale | P5b instruction | P5b instruction | P2.2 instruction | S4b instruction | P5b instruction |
| C-08 4+ cats ≤40% | P2 architecture | P2 architecture | P1.2 architecture | S2 | P2 architecture |
| C-09 top 5 differentiated | P6c check | P6c check | P3.3 check | S5 check | P6c check |
| C-10 AMEND non-overlapping | P1 direction col | P1 direction col | P1.1 direction | S1 direction | P1 direction col |
| C-11 two-pass | P5a + P5b | P4 + P5 | P2.1 + P2.2 | S4 + S4b | P5a + P5b |
| C-12 AMEND downstream | P1 effect col | P1 effect col | P1.1 effect col | S1 effect col | P1 effect col |
| C-13 inertia costs+benefits | P3 both fields | P3 both fields | P1.3 both fields | S3 both halves | P3 both fields |
| C-14 structured verify | P7 checklist | P7 checklist | P4.1 checklist | S6 | P7 checklist |
| C-15 AMEND-first | P1 is first | P1 is first | P1.1 is first | S1 is first | P1 is first |
| C-16 Do Nothing anchor | P3 dedicated | P3 dedicated | P1.3 dedicated | S3 dedicated | P3 dedicated |
| C-17 architecture pre-commit | P2 slots+cap | P2 slots+cap | P1.2 slots+cap | S2 slots+cap | P2 slots+cap |
| C-18 adversarial before ** | P6 challenge | P6 threshold test | P3.2 challenge | S5 challenge | P6 challenge |
| C-19 per-phase exit gates | P1–P6 gates | P1–P6 gates | P1–P3 gates | (S steps + check) | P1–P6 gates |
| C-20 table format + % col | P2 architecture + tables | P2 + all tables | P1.2 + tables | S2 table | P2 + all tables |
| C-21 architecture before anchor | P2 before P3 | P2 before P3 | P1.2 before P1.3 | S2 before S3 | P2 before P3 |
| C-22 inline conditionals | P5a mid-step | P4 mid-step | P2.1 mid-step | S4 parenthetical | P5a mid-step |
