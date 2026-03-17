# draft-brainstorm Skill Prompt Variations — Round 5

**Skill:** draft-brainstorm
**Round:** 5
**Date:** 2026-03-15
**Rubric:** v4 (C-01 through C-18)
**Target:** All 18 criteria pass in every variation; axes explore structural alternatives, not criteria coverage.

---

## Criteria Coverage Map

All 5 variations are designed to hit all 18 criteria. The table below maps criteria to the phases that satisfy them — used to verify no criterion is dropped when an axis is varied.

| Criteria | Satisfied by |
|---|---|
| C-01 (volume 20-40) | Phase: Diverge/Cluster |
| C-02 (anatomy 4 fields) | Phase: Cluster |
| C-03 (exactly 5 **) | Phase: Finalize (after adversarial) |
| C-04 (inertia present) | Phase: Do Nothing Anchor |
| C-05 (AMEND 3 adjustments) | Phase: AMEND |
| C-06 (grouped by category) | Phase: Cluster / Write |
| C-07 (rationale topic-specific) | Phase: Cluster instruction |
| C-08 (4+ categories, <=40%) | Phase: Category Architecture |
| C-09 (top 5 span 3+ categories) | Phase: Adversarial / Finalize |
| C-10 (AMEND non-overlapping) | Phase: AMEND instruction |
| C-11 (two-pass diverge/cluster) | Phase: Diverge then Cluster |
| C-12 (AMEND names downstream effects) | Phase: AMEND instruction |
| C-13 (inertia costs + benefits) | Phase: Do Nothing Anchor |
| C-14 (structured verification) | Phase: Verify |
| C-15 (AMEND before pool) | Ordering: AMEND is Phase 1 |
| C-16 (Do Nothing as anchor phase) | Ordering: Anchor precedes Diverge |
| C-17 (architecture pre-commitment) | Phase: Category Architecture (before Diverge) |
| C-18 (adversarial before ** marks) | Phase: Adversarial (** deferred) |

---

## V-01 — Lifecycle Emphasis: Entry/Exit Gate Language Per Phase

**Variation axis:** Lifecycle emphasis
**Hypothesis:** Making phase boundaries maximally explicit — each phase carries an ENTRY CONDITION ("You may not start this phase until X is written above"), a named DELIVERABLE, and an EXIT CONDITION ("Do not continue until this deliverable appears") — eliminates phase-skipping and backfilling more reliably than imperative commands alone. The gate mechanism enforces temporal ordering structurally rather than by instruction.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Produce a pool of 20-40 idea candidates. Work through the phases below in strict order. Each phase has an ENTRY CONDITION you must satisfy before starting, a DELIVERABLE you must produce, and an EXIT CONDITION you must reach before proceeding.

---

#### PHASE 1 — AMEND ADJUSTMENTS

**ENTRY:** This is the first phase. Nothing precedes it.

**DELIVERABLE:** Write exactly 3 pool-shaping adjustments. For each:
- Name the dimension being shifted (e.g., scope, audience, timeline, risk profile, implementation depth)
- Describe its downstream effect on the candidate pool — what kinds of ideas would surface or disappear if this shift were applied
- Pull in a different direction from the other two (no two adjustments may point the same way)

Format each as: `[Dimension]: [shift description] → [downstream effect on pool]`

**EXIT:** All 3 adjustments are written, each with a named dimension and downstream effect, pulling in distinct directions.

---

#### PHASE 2 — STATUS QUO ANCHOR

**ENTRY:** Phase 1 is complete (3 AMEND adjustments written above).

**DELIVERABLE:** Write the Do Nothing candidate as a standalone entry. It must include:
- **Name:** "Do Nothing" or a specific name for the status quo
- **Pitch:** One sentence describing what continuing without change looks like for `{{topic}}`
- **Benefits of inertia:** What the current state provides that teams or users value (why people stay with it)
- **Costs of inertia:** What problems persist, compound, or foreclose by not acting

The Do Nothing candidate is a real competitor, not a placeholder. Both halves are required.

**EXIT:** Do Nothing entry is written with pitch, benefits, and costs all present.

---

#### PHASE 3 — CATEGORY ARCHITECTURE

**ENTRY:** Phase 2 is complete (Do Nothing anchor written above).

**DELIVERABLE:** Declare the category architecture before generating any idea. Produce this table:

| Category Name | Target Slot Count | Notes |
|---|---|---|
| Status Quo | 1 | Do Nothing only |
| [name] | [N] | |
| [name] | [N] | |
| [name] | [N] | |
| ... | | |

Requirements:
- At least 4 distinct named categories (including Status Quo)
- Slot counts sum to at least 20 and no more than 40
- No single category may hold more than 40% of total slots — enforce this now, not after generation
- Slot counts are binding commitments, not suggestions

**EXIT:** Architecture table is complete, >=4 categories, sum is 20-40, largest category is <=40% of total.

---

#### PHASE 4 — DIVERGE (names + pitches only)

**ENTRY:** Phase 3 is complete (category architecture table written above).

**DELIVERABLE:** Generate idea names and one-line pitches freely, targeting the slot counts from Phase 3. Do not assign categories or rationales yet — this pass is divergence only.

Produce: `Name — Pitch` for every idea, aiming for the Phase 3 slot counts.

**EXIT:** Every slot from Phase 3 has a corresponding name+pitch entry. No rationales or categories assigned yet.

---

#### PHASE 5 — CLUSTER (assign category + rationale)

**ENTRY:** Phase 4 is complete (all names and pitches written above, no categories or rationales yet).

**DELIVERABLE:** For each idea from Phase 4, assign:
- **Category:** must match a category declared in Phase 3
- **Rationale:** why this idea specifically serves `{{topic}}` — must reference the topic, not be generic boilerplate applicable to any feature

Include the Do Nothing candidate from Phase 2 in the Status Quo category.

Organize output under labeled category headings. Every idea must have all four fields: name, pitch, category, rationale.

**EXIT:** All candidates are organized under category headings. Every entry has 4 fields. Count is 20-40.

---

#### PHASE 6 — ADVERSARIAL CHALLENGE

**ENTRY:** Phase 5 is complete (full candidate pool with 4 fields per entry written above).

**DELIVERABLE:** Identify 5 tentative top picks. Do NOT mark them `**` yet — marks are withheld until after the challenge.

List them:
```
Tentative T1: [name] — [why it looks strong]
Tentative T2: [name] — [why it looks strong]
Tentative T3: [name] — [why it looks strong]
Tentative T4: [name] — [why it looks strong]
Tentative T5: [name] — [why it looks strong]
```

Now challenge each one: write one serious objection — a reason the idea might fail, be infeasible, or not genuinely serve `{{topic}}`. Then rule:

- **SURVIVE:** State what makes it robust despite the challenge.
- **ELIMINATE:** Replace it with the next strongest candidate not in the tentative 5. State why the replacement is more defensible.

The 5 survivors or replacements are your confirmed Top 5.

**EXIT:** Each tentative pick has been challenged, ruled SURVIVE or ELIMINATE, and 5 confirmed picks are named.

---

#### PHASE 7 — VERIFY

**ENTRY:** Phase 6 is complete (confirmed Top 5 named above).

**DELIVERABLE:** Fill this checklist before writing the artifact. Any FAIL must be corrected before proceeding.

| Check | Pass / Fail |
|---|---|
| Candidate count is between 20 and 40 | |
| Every candidate has name, pitch, category, rationale | |
| Exactly 5 candidates will be marked `**` | |
| Do Nothing has pitch + benefits + costs | |
| AMEND has exactly 3 adjustments | |
| Each AMEND adjustment has dimension + downstream effect | |
| All 3 AMEND adjustments pull in distinct directions | |
| Ideas are organized under labeled category headings | |
| At least 4 distinct categories | |
| No single category exceeds 40% of candidates | |
| Top 5 span at least 3 distinct categories | |
| All Top 5 survived or replaced through adversarial challenge | |
| Rationales reference `{{topic}}` specifically | |

**EXIT:** All checks pass. Any FAIL is corrected in the pool above before writing.

---

#### PHASE 8 — WRITE ARTIFACT

**ENTRY:** Phase 7 is complete (all verification checks pass).

Write the final artifact to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`.

Structure:
1. **AMEND** — 3 adjustments from Phase 1
2. **[Category Name]** sections — candidates organized under labeled headings, `**` marks applied to confirmed Top 5

---

---

## V-02 — Output Format: Table-Centric Column Schema

**Variation axis:** Output format
**Hypothesis:** Using Markdown tables with explicit column schemas throughout (architecture plan, diverge pass, cluster pass, adversarial pass, verification checklist) makes the four-field anatomy requirement self-enforcing, makes counting trivial, and surfaces missing fields immediately at generation time. The table schema acts as a built-in anatomy checker — a field missing from a column is immediately visible.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate a pool of 20-40 idea candidates. Work through the phases below in order. All candidates and planning outputs use table format.

---

#### PHASE 1 — AMEND ADJUSTMENTS

Before generating any candidates, write the 3 pool-shaping adjustments. Adjustments must be written first — they shape the categories and ideas that follow.

| # | Dimension Shifted | Downstream Effect on Pool | Direction |
|---|---|---|---|
| A1 | | | |
| A2 | | | |
| A3 | | | |

Rules:
- Each row must have a named dimension and a downstream effect (what kinds of candidates appear or disappear)
- Direction column: each must be distinct — no two adjustments may pull the same way

---

#### PHASE 2 — STATUS QUO ANCHOR

Before generating alternatives, write the Do Nothing candidate as a standalone structural anchor.

**Do Nothing — `{{topic}}`**

| Field | Content |
|---|---|
| Pitch | [one sentence: what continuing without change looks like] |
| Why inertia is appealing | [what the status quo provides that has real value] |
| What inertia costs | [what problems persist or compound without action] |

This entry will appear in the candidate pool below under "Status Quo." Both benefit and cost halves are required.

---

#### PHASE 3 — CATEGORY ARCHITECTURE

Before generating any idea, declare the pool's shape.

| Category Name | Target Slot Count | % of Pool | Notes |
|---|---|---|---|
| Status Quo | 1 | [compute] | Do Nothing only |
| | | | |
| | | | |
| | | | |

Rules to enforce now:
- At least 4 named categories (including Status Quo)
- Total slot count: 20-40
- No single category may exceed 40% of total slots — verify the % column before proceeding
- These counts are binding commitments

---

#### PHASE 4 — DIVERGE (names + pitches only)

Target the slot counts from Phase 3. Generate name + pitch for every slot. Do not assign categories or rationales in this pass.

| # | Name | Pitch |
|---|---|---|
| 1 | | |
| 2 | | |
| ... | | |

Fill enough rows to meet Phase 3 slot totals. No rationales or category assignments yet.

---

#### PHASE 5 — CLUSTER (complete all 4 fields)

For each row from Phase 4, assign category and rationale. Rationale must reference `{{topic}}` specifically — not generic boilerplate applicable to any topic.

| # | Name | Pitch | Category | Rationale |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Include the Do Nothing candidate (from Phase 2) in the Status Quo row. Verify: every row has all 4 fields filled.

---

#### PHASE 6 — ADVERSARIAL CHALLENGE

Identify 5 tentative top picks. Do NOT mark them `**` yet.

| Pick | Name | Strength | Adversarial Objection | Verdict |
|---|---|---|---|---|
| T1 | | | | SURVIVE / ELIMINATE |
| T2 | | | | SURVIVE / ELIMINATE |
| T3 | | | | SURVIVE / ELIMINATE |
| T4 | | | | SURVIVE / ELIMINATE |
| T5 | | | | SURVIVE / ELIMINATE |

For any ELIMINATE verdict: name the replacement candidate and explain why it is more defensible.

Confirmed Top 5 after adversarial challenge: [list names — these are the only candidates that will receive `**` marks]

Check: confirmed Top 5 spans at least 3 distinct categories. If not, reconsider.

---

#### PHASE 7 — VERIFY

Fill this checklist before writing. Fix any FAIL in the pool above before proceeding.

| Criterion | Status |
|---|---|
| Candidate count is 20-40 | |
| Every row has name, pitch, category, rationale | |
| Exactly 5 candidates marked `**` (confirmed Top 5 only) | |
| Do Nothing has pitch + benefits + costs | |
| AMEND: 3 rows, each with dimension + downstream effect | |
| All 3 AMEND directions are distinct | |
| At least 4 category headings in the pool | |
| No category exceeds 40% of total candidates | |
| Top 5 span at least 3 distinct categories | |
| All rationales reference `{{topic}}` specifically | |

---

#### PHASE 8 — WRITE ARTIFACT

Write the final artifact to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`.

**Artifact format:**

```
### AMEND
[3 rows from Phase 1: Dimension → Downstream effect]

### [Category Name]
| # | Name | Pitch | Rationale |
|---|---|---|---|
[rows; ** applied to confirmed Top 5]

[repeat for each category]
```

---

---

## V-03 — Role Sequence: Architecture Before Anchor

**Variation axis:** Role sequence
**Hypothesis:** Placing the Category Architecture phase (Phase 2) before the Status Quo Anchor (Phase 3) — so that the pool's shape is declared before the baseline competitor is written — produces category structures that are more grounded in the topic's decision space rather than reactive to the Do Nothing framing. The alternative sequence tests whether the anchor biases the architect.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate a pool of 20-40 idea candidates. Work through the phases below in strict order. Complete each phase fully before proceeding to the next.

---

#### PHASE 1 — AMEND ADJUSTMENTS

Write 3 pool-shaping adjustments before anything else. These will influence what categories and candidates you generate.

For each adjustment, write:

```
AMEND-[N]: [specific dimension being shifted]
Shift: [what changes]
Downstream effect: [how this changes which candidates surface or disappear]
Direction: [expanding / narrowing / reframing / redirecting — must differ across all 3]
```

All 3 adjustments must pull in distinct directions. Each downstream effect must be specific to `{{topic}}`.

---

#### PHASE 2 — CATEGORY ARCHITECTURE

With the AMEND adjustments visible above, declare the category structure for the pool. This phase must complete before any idea is generated.

Declare each category:

```
Category: [name]
Target slots: [N ideas]
Rationale: [why this category is relevant to {{topic}}]
```

Requirements:
- At least 4 categories
- Slot totals sum to 20-40
- No category exceeds 40% of total — compute and verify before continuing
- Include "Status Quo" (1 slot) for the Do Nothing candidate

The AMEND adjustments above may suggest categories you would not have otherwise included. Update your architecture accordingly.

---

#### PHASE 3 — STATUS QUO ANCHOR

With the category architecture set, write the Do Nothing candidate as a dedicated structural entry before any alternatives.

**Do Nothing — Status Quo for `{{topic}}`**

- **Pitch:** [one sentence: what continuing without change looks like]
- **Why appealing:** [what is genuinely valuable about the current state — why teams or users stay with it]
- **What it costs:** [what problems remain unsolved, compound, or foreclose]

Both halves are required. This entry appears in the Status Quo category in the candidate pool.

---

#### PHASE 4 — DIVERGE (names + pitches only)

Generate idea names and one-line pitches freely, aiming for the slot counts from Phase 2. In this pass: names and pitches only. Do not assign categories or rationales.

List: `[#]. [Name] — [Pitch]`

Cover all Phase 2 categories and slot targets. Do not skip categories with low slot counts.

---

#### PHASE 5 — CLUSTER (assign category + rationale)

For each idea from Phase 4, add:
- **Category:** must match a Phase 2 category name exactly
- **Rationale:** why this idea serves `{{topic}}` specifically — must name the topic, not offer boilerplate applicable to any feature

Organize all entries under their category headings. Include the Do Nothing candidate (Phase 3) in the Status Quo section.

Every entry must have all 4 fields: name, pitch, category, rationale.

---

#### PHASE 6 — ADVERSARIAL CHALLENGE

From the full pool above, identify 5 tentative top picks. Write them down but do NOT mark them `**` yet.

```
Tentative T1: [name] — [one sentence on why it looks strong]
Tentative T2: [name] — [one sentence on why it looks strong]
Tentative T3: [name] — [one sentence on why it looks strong]
Tentative T4: [name] — [one sentence on why it looks strong]
Tentative T5: [name] — [one sentence on why it looks strong]
```

Now, for each tentative pick, write a serious objection — a reason it might fail, be infeasible, or not genuinely solve `{{topic}}`'s core problem. Then rule: **SURVIVE** or **ELIMINATE**.

- SURVIVE: state what makes it robust despite the objection
- ELIMINATE: name the replacement (next-strongest candidate not in the tentative 5) and explain why it is more defensible

After all 5 are ruled on, write your confirmed Top 5 list. Only these will receive `**` marks.

Verify: confirmed Top 5 spans at least 3 distinct categories.

---

#### PHASE 7 — VERIFY

Run this checklist before writing the artifact. Fix any FAIL above before proceeding.

| Check | Result |
|---|---|
| 20-40 named candidates | |
| Every candidate has name + pitch + category + rationale | |
| Exactly 5 `**` marks | |
| Do Nothing has pitch + benefits + costs | |
| AMEND: 3 adjustments, dimension + downstream effect, distinct directions | |
| 4+ categories, no single category > 40% | |
| Top 5 span 3+ categories | |
| All rationales reference `{{topic}}` | |
| All Top 5 passed or replaced through adversarial challenge | |

---

#### PHASE 8 — WRITE ARTIFACT

Write the artifact to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`.

Structure:
1. **AMEND** section — 3 adjustments, each showing dimension and downstream effect
2. Candidate pool organized under category headings, `**` marks on confirmed Top 5

---

---

## V-04 — Phrasing Register: Conversational Descriptive

**Variation axis:** Phrasing register
**Hypothesis:** Framing each phase in a descriptive, conversational register ("Here's what to do in this step...") rather than imperative commands ("You MUST complete Phase X before...") produces more naturally-worded rationale prose and reduces the mechanical, template-feel in the output — while identical structural phases ensure all 18 criteria are still structurally satisfied.

---

### Prompt Body

You're running draft-brainstorm for the topic: `{{topic}}`

The goal is a rich pool of 20-40 idea candidates that gives you more than you need — so you can rank and filter. Here's how to work through it. Take each step fully before moving to the next.

---

#### Step 1: Write your three pool-shaping adjustments first

Before any ideas, take a moment to write down three ways you could tilt the pool in a different direction. These adjustments are worth doing upfront because they'll shape what you think to generate later.

For each one, say: what dimension is shifting, and what effect would that have on the kinds of ideas that show up? For example: "If we made this more conservative on scope, we'd see more low-effort operational plays and fewer speculative integrations."

Make sure the three adjustments pull in different directions — not three versions of "more ambitious" or three versions of "narrower scope." You're trying to triangulate the space, not push it one way.

---

#### Step 2: Map out the category shape before generating ideas

Knowing the AMEND adjustments you just wrote, think about what categories this topic's idea space naturally breaks into. Declare them here, with a sense of how many ideas each should hold.

For each category, note:
- Category name
- How many ideas you're aiming for (a specific number or range)
- Why this category matters for `{{topic}}`

A few things to keep in mind: you want at least four distinct categories, the total should land between 20 and 40 candidates, and no single category should hold more than 40% of the pool (otherwise the pool gets lopsided). Include "Status Quo" as one of your categories — it'll hold the Do Nothing candidate.

Work through the math now: if your biggest category is 40% or more of the total, adjust before continuing.

---

#### Step 3: Write the Do Nothing candidate as its own entry

Before writing alternatives, take a moment to describe the status quo honestly. This is a real competitor to every other idea — the choice teams make when they choose not to act.

Write it as a standalone entry with:
- A pitch: what does life look like if nothing changes for `{{topic}}`?
- What's genuinely appealing about it: what does the current state give teams or users that they'd lose by changing? (This is why people stay with the status quo — don't skip this.)
- What it actually costs: what problems don't get solved, what opportunities close off, what compounds over time?

Both sides matter. The Do Nothing entry appears in the Status Quo category in the pool below.

---

#### Step 4: Diverge — generate names and pitches freely

Now generate ideas. Using the category map from Step 2 as your guide, produce a name and one-line pitch for each slot. In this pass, just names and pitches — don't worry about assigning categories or writing rationales yet. Let the ideas come first.

Aim for the slot targets you set. Cover every category.

---

#### Step 5: Cluster — add category and rationale to everything

Go through every idea from Step 4 and add:
- Which category it belongs to (must be one you named in Step 2)
- A rationale that's specific to `{{topic}}` — not a generic sentence that could describe any feature's value. Reference the topic itself.

Organize everything under category headings. Include the Do Nothing entry in the Status Quo section. Every idea needs all four fields: name, pitch, category, rationale.

---

#### Step 6: Challenge your tentative top five

From the pool above, pick five ideas that feel strongest — but don't mark them `**` yet. Write them down first:

```
Tentative top pick 1: [name] — [why you like it]
Tentative top pick 2: [name] — [why you like it]
Tentative top pick 3: [name] — [why you like it]
Tentative top pick 4: [name] — [why you like it]
Tentative top pick 5: [name] — [why you like it]
```

Now push back on each one. What's the strongest reason each of these might not work? What assumption might be wrong, or what might make it harder to execute than it looks? Rule each one: does it survive the challenge, or should it be replaced?

If you eliminate one, bring in the next-strongest from the rest of the pool and explain why it's a better choice.

Once all five have been ruled on, you have your confirmed top five. These are the only candidates that will get `**` marks. Check that they span at least 3 different categories — five variations on the same idea doesn't make a diverse top five.

---

#### Step 7: Check your work before writing

Before writing the artifact, run through this list:

| What to check | OK? |
|---|---|
| 20-40 named candidates (count them) | |
| Every candidate has name, pitch, category, rationale | |
| Exactly 5 `**` marks, all from the confirmed top five | |
| Do Nothing has pitch + why it's appealing + what it costs | |
| 3 AMEND adjustments, each with a dimension and downstream effect | |
| AMEND adjustments pull in 3 different directions | |
| At least 4 categories, none holding more than 40% | |
| Top 5 spans 3+ categories | |
| Rationales reference `{{topic}}` specifically | |

Fix anything that's off before writing the final artifact.

---

#### Step 8: Write the artifact

Write to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`.

Include:
1. **AMEND** — your 3 adjustments, each showing the dimension and downstream effect
2. The candidate pool under category headings, with `**` on the confirmed top five

---

---

## V-05 — Combination: Named Adversarial Persona + Table Format

**Variation axes:** Named adversarial identity (makes challenge pressure concrete and harder to rubber-stamp) + Table-centric output format (from V-02, self-enforcing anatomy)
**Hypothesis:** Assigning a specific named adversarial voice ("the Skeptic") to the challenge phase — with a defined mandate, a characteristic tone, and explicit elimination authority — produces harder adversarial pressure than a generic "challenge each pick" instruction. Combined with table format (V-02) for structural discipline throughout, this variation maximizes both C-18 depth and C-02/C-14 reliability.

---

### Prompt Body

You are running the draft-brainstorm skill for the topic: `{{topic}}`

Generate a pool of 20-40 idea candidates. Work through the phases below in order. Use table format for structured outputs.

---

#### PHASE 1 — AMEND ADJUSTMENTS

Before generating any candidates, write 3 pool-shaping adjustments.

| # | Dimension Shifted | How Shifting It Changes the Pool | Direction |
|---|---|---|---|
| A1 | | | |
| A2 | | | |
| A3 | | | |

- **Dimension:** the specific lever being moved (scope, audience, timeline, risk tolerance, implementation depth, etc.)
- **How it changes the pool:** what types of candidates surface or disappear — be specific to `{{topic}}`
- **Direction:** one of: expands / narrows / reframes / pivots / de-risks — must differ across all 3 rows

---

#### PHASE 2 — STATUS QUO ANCHOR

Write the Do Nothing candidate as a standalone structural entry before alternatives.

| Field | Content |
|---|---|
| Name | Do Nothing / [specific status quo name] |
| Pitch | [one sentence: what continuing without change means for `{{topic}}`] |
| Why appealing | [what the current state genuinely provides — why teams or users stay] |
| What it costs | [what problems persist, compound, or foreclose without action] |

Both halves (appeals and costs) are required. This entry appears in the Status Quo category below.

---

#### PHASE 3 — CATEGORY ARCHITECTURE

Declare the pool's shape before generating any idea.

| Category Name | Target Slots | % of Pool | Cap Check (<=40%?) |
|---|---|---|---|
| Status Quo | 1 | [compute] | [pass/fail] |
| | | | |
| | | | |
| | | | |
| **TOTAL** | | 100% | |

Requirements:
- At least 4 named categories
- Total slots: 20-40
- No category may exceed 40% — the Cap Check column must show PASS for all rows before proceeding

---

#### PHASE 4 — DIVERGE (names + pitches only)

Generate names and pitches targeting Phase 3 slot counts. No categories or rationales in this pass.

| # | Name | Pitch |
|---|---|---|
| 1 | | |
| 2 | | |
| ... | | |

---

#### PHASE 5 — CLUSTER (complete all 4 fields)

Assign category and rationale to every idea from Phase 4. Rationale must reference `{{topic}}` — not generic boilerplate.

| # | Name | Pitch | Category | Rationale |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

Include Do Nothing (Phase 2) in the Status Quo row.

---

#### PHASE 6 — THE SKEPTIC'S CHALLENGE

**Role:** You are now the Skeptic. The Skeptic's mandate: find the weaknesses in the apparent top candidates and eliminate any that do not hold up under scrutiny. The Skeptic is not hostile — they are rigorous. Their job is to ensure the `**` marks go only to candidates that can withstand realistic pushback.

**Step 6a — Tentative nominations (no `**` marks yet):**

| Pick | Name | Why It Looks Strong |
|---|---|---|
| T1 | | |
| T2 | | |
| T3 | | |
| T4 | | |
| T5 | | |

**Step 6b — The Skeptic cross-examines each pick:**

For each tentative pick, the Skeptic raises one serious challenge — a specific reason the idea might fail, be infeasible, misread user needs, or be weaker than it appears for `{{topic}}`.

| Pick | Skeptic's Challenge | Verdict | Outcome |
|---|---|---|---|
| T1 | | SURVIVE / ELIMINATE | [if survive: defense; if eliminate: replacement + why] |
| T2 | | SURVIVE / ELIMINATE | |
| T3 | | SURVIVE / ELIMINATE | |
| T4 | | SURVIVE / ELIMINATE | |
| T5 | | SURVIVE / ELIMINATE | |

The Skeptic does not allow rubber-stamp survivals. If the challenge reveals a genuine weakness, the pick is eliminated regardless of how promising it looked.

**Step 6c — Confirmed Top 5:**

The 5 survivors or replacements are: [list names]

The Skeptic verifies: confirmed Top 5 spans at least 3 distinct categories. If not, the Skeptic requires reconsideration.

Only these 5 will receive `**` marks.

---

#### PHASE 7 — VERIFY

| Criterion | Status |
|---|---|
| Candidate count 20-40 | |
| Every row has name, pitch, category, rationale | |
| Exactly 5 `**` marks (confirmed Top 5 only) | |
| Do Nothing has pitch + appeals + costs | |
| AMEND: 3 rows, dimension + downstream effect, distinct directions | |
| 4+ categories, cap check passes (no category >40%) | |
| Top 5 spans 3+ categories | |
| All Top 5 passed The Skeptic or were replaced | |
| Rationales reference `{{topic}}` specifically | |

Fix any FAIL before writing.

---

#### PHASE 8 — WRITE ARTIFACT

Write the final artifact to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`.

**Format:**

```
### AMEND
| # | Dimension | Downstream Effect | Direction |
[3 rows from Phase 1]

### [Category Name]
| # | Name | Pitch | Rationale |
[rows; ** applied to confirmed Top 5]

[repeat for each category]
```

---

---

## Variation Summary

| Variation | Primary Axis | Key Structural Choice | Hypothesis to Test |
|---|---|---|---|
| V-01 | Lifecycle emphasis | Entry/exit gate language per phase | Gate language enforces ordering better than imperatives |
| V-02 | Output format | Table schema throughout | Column schema makes anatomy self-enforcing |
| V-03 | Role sequence | Architecture before Do Nothing anchor | Declaring categories before baseline reduces anchor bias |
| V-04 | Phrasing register | Conversational/descriptive | Descriptive register produces more natural rationale prose |
| V-05 | Combination | Named Skeptic + table format | Named adversarial identity produces harder challenge pressure |

## Criteria Coverage Verification

All 5 variations satisfy all 18 criteria:

| Criteria | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-01 volume | P4 diverge | P4 diverge | P4 diverge | S4 diverge | P4 diverge |
| C-02 anatomy | P5 cluster | P5 cluster | P5 cluster | S5 cluster | P5 cluster |
| C-03 exactly 5 ** | P8 write | P8 write | P8 write | S8 write | P8 write |
| C-04 inertia present | P2 anchor | P2 anchor | P3 anchor | S3 anchor | P2 anchor |
| C-05 AMEND 3 | P1 | P1 | P1 | S1 | P1 |
| C-06 grouped | P5/P8 | P5/P8 | P5/P8 | S5/S8 | P5/P8 |
| C-07 topic-specific | P5 instruction | P5 instruction | P5 instruction | S5 instruction | P5 instruction |
| C-08 4+ cats <=40% | P3 | P3 | P2 | S2 | P3 |
| C-09 top 5 differentiated | P6 verify | P6 verify | P6 verify | S6 verify | P6c |
| C-10 AMEND non-overlap | P1 instruction | P1 instruction | P1 instruction | S1 instruction | P1 instruction |
| C-11 two-pass | P4+P5 | P4+P5 | P4+P5 | S4+S5 | P4+P5 |
| C-12 AMEND downstream | P1 instruction | P1 instruction | P1 instruction | S1 instruction | P1 instruction |
| C-13 inertia costs+benefits | P2 anchor | P2 anchor | P3 anchor | S3 anchor | P2 anchor |
| C-14 structured verify | P7 checklist | P7 checklist | P7 checklist | S7 checklist | P7 checklist |
| C-15 AMEND-first | P1 first | P1 first | P1 first | S1 first | P1 first |
| C-16 Do Nothing anchor | P2 dedicated | P2 dedicated | P3 dedicated | S3 dedicated | P2 dedicated |
| C-17 architecture pre-commit | P3 (slots+cap) | P3 (slots+cap) | P2 (slots+cap) | S2 (slots+cap) | P3 (slots+cap) |
| C-18 adversarial challenge | P6 challenge | P6 challenge | P6 challenge | S6 challenge | P6 Skeptic |
