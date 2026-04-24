---
skill: quest-variate
skill_target: draft-brainstorm
round: 1
date: 2026-03-15
rubric_version: 1
---

# Variate R1 — draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format (table vs grouped list vs prose sections) | V-01, V-05 |
| Inertia framing (where + how prominently status quo is featured) | V-02, V-05 |
| Phrasing register (imperative/technical vs conversational/question-driven) | V-03 |
| Role sequence (single pass vs diverge→converge roles) | V-04 |
| Lifecycle emphasis (implicit phases vs named phase boundaries) | V-04 |

---

## V-01 — Output Format: Markdown Table

**Axis**: Output format
**Hypothesis**: Enforcing a rigid table with named columns makes C-02 anatomy mechanically auditable
and C-01 volume countable at a glance. The table constraint may reduce rationale depth (C-07) but
will prevent the most common anatomy failure — ideas missing one of the four fields.

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

Your job: generate a pool of 20-40 idea candidates — more than the team needs, wide enough to
make ranking meaningful.

**Step 1 — Build the table**

Output a markdown table with exactly these columns:

| # | Name | Pitch | Category | Rationale | Top-5? |
|---|------|-------|----------|-----------|--------|

Column rules:
- **#**: Sequential number (1, 2, 3...)
- **Name**: Short label, 2-5 words
- **Pitch**: One sentence — what the idea is
- **Category**: The dimension this idea occupies (e.g., Integration, UX, Architecture, Scope)
- **Rationale**: Why this idea serves {{topic}} specifically. Must cite a real constraint, user need,
  or opportunity in this topic. "This provides value" is not a rationale.
- **Top-5?**: Write `**YES**` in exactly 5 rows. Leave all others blank. These are the ideas with
  highest immediate viability — the ones a team could act on today.

Required row: include a row named **"Do Nothing"** with Category = "Status Quo". Its Rationale
must describe what the current trajectory produces for {{topic}} — not just say "do nothing is
an option."

Volume: 20-40 rows total (not counting the header row).

**Step 2 — Group by category**

After the table, repeat the ideas as grouped sections under category headers so they can be
scanned by dimension:

```
## [Category Name]

- **[Idea Name]** — [Pitch]
```

No new content here — just reorganize the same ideas under headers.

**Step 3 — AMEND**

Write an AMEND section with exactly 3 adjustments that would shift the pool in a different
direction. Each must name the shift and state what changes in the pool:

```
## AMEND

1. [Direction label]: [Which ideas enter, exit, or re-rank — and why]
2. [Direction label]: [Which ideas enter, exit, or re-rank — and why]
3. [Direction label]: [Which ideas enter, exit, or re-rank — and why]
```

**Step 4 — Write artifact**

Write the complete output (table + grouped view + AMEND) to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

Frontmatter:
```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

---

## V-02 — Inertia Framing: Status Quo Anchored First

**Axis**: Inertia framing
**Hypothesis**: Grounding the brainstorm in the status quo *before* generating alternatives
primes every subsequent rationale to implicitly contrast against inertia, which raises C-04
pass rate and increases C-07 specificity throughout the pool. The cost is that the status
quo section may crowd out idea volume at the top.

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

Before generating any alternative ideas, anchor the brainstorm in the status quo.

---

**Phase 0 — Inertia Anchor (required, runs first)**

Write 3-5 sentences describing what happens if the team makes no deliberate decision about
{{topic}}. Answer: What is the current path? What does it produce? What risks or missed
opportunities accumulate by default?

Then create the formal Do Nothing entry:

```
### Do Nothing (Status Quo)

**Pitch**: [One sentence: what the current trajectory produces for {{topic}}]
**Category**: Status Quo
**Rationale**: [What the team gets — and permanently gives up — by staying the course.
               Be specific to {{topic}}, not generic.]
```

This is your anchor point. Every idea generated after this is an alternative to this default.

---

**Phase 1 — Idea Pool**

Generate 20-40 idea candidates as alternatives to the status quo. For each idea, the rationale
should implicitly or explicitly contrast with the Do Nothing path — what does this idea unlock
that inertia does not?

Organize ideas under category headers (at least 4 distinct categories). For each idea:

```
## [Category Name]

### [Idea Name]

**Pitch**: [One sentence]
**Rationale**: [Why this serves {{topic}} better than the status quo — specific to this topic's
               constraints, users, or opportunities]
```

Mark exactly 5 ideas with `**` on their heading (e.g., `### ** Idea Name`). These are your
highest-viability picks — candidates a team could act on today.

---

**Phase 2 — AMEND**

Provide exactly 3 adjustments that would shift the pool:

```
## AMEND

1. [Shift direction]: [What ideas would enter, exit, or re-rank if this shift were applied]
2. [Shift direction]: [What ideas would enter, exit, or re-rank if this shift were applied]
3. [Shift direction]: [What ideas would enter, exit, or re-rank if this shift were applied]
```

Each adjustment must be specific enough that a reader could immediately re-run the brainstorm
in that direction and get a meaningfully different pool.

---

**Output**

Write the artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Total ideas in artifact (including Do Nothing): 20-40.

---

## V-03 — Phrasing Register: Conversational / Question-Driven

**Axis**: Phrasing register
**Hypothesis**: A question-driven, conversational prompt lowers generation friction and
surfaces more varied categories (C-08), because the model follows the questions naturally
rather than optimizing for template compliance. Risk: AMEND items may be less directive
(C-09), since the tone discourages prescriptive language.

---

You are helping the team think through: **{{topic}}**

The goal is to open the option space wide — more ideas than the team needs, so the best
ones don't get filtered out before they're even seen. You'll generate candidates, surface
the strongest, and flag a few ways the whole pool could shift.

---

**What are all the ways the team could approach {{topic}}?**

Think across at least 4 different angles. These might be: technical approaches, scope
choices, timing strategies, audience bets, build-vs-integrate decisions, risk profiles,
or whatever dimensions matter most for this topic. Aim for 20-40 candidates total.

For each idea, answer four questions:

1. **What's it called?** Short name, 2-5 words.
2. **What is it in one sentence?** The pitch.
3. **What kind of idea is this?** The category — use this as the grouping header.
4. **Why does this fit {{topic}} specifically?** The rationale — tie it to a real constraint,
   user need, or opportunity in *this* topic. Generic reasoning ("this is valuable") doesn't
   count.

Group ideas under their category headers.

---

**What happens if the team does nothing?**

Include one idea called **"Do Nothing"** (or **"Status Quo"**). What actually happens to
{{topic}} if no decision is made? What does the team inherit? Write a real rationale —
this is a legitimate option and often the one that wins by default.

---

**Which 5 ideas are most immediately viable?**

Mark exactly 5 ideas with `**` prefix on their heading. These are your top picks — the
ideas with the best chance of working given current constraints. The selection should be
defensible: if someone asked "why these five?", you could give a real answer.

---

**What would change the pool?**

End with an AMEND section. Give exactly 3 ways you could tilt this brainstorm in a
different direction. For each, name the direction and describe how the pool looks different:

```
## AMEND

1. If we [direction]: [which ideas enter or exit, and why the pool looks different]
2. If we [direction]: [which ideas enter or exit, and why the pool looks different]
3. If we [direction]: [which ideas enter or exit, and why the pool looks different]
```

---

**Write the output**

Save the complete brainstorm to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

---

## V-04 — Combination: Role Sequence + Lifecycle Emphasis

**Axes**: Role sequence (diverger then evaluator) + lifecycle emphasis (explicit named phases)
**Hypothesis**: Separating generation from evaluation into named roles with hard phase
boundaries forces the model to produce a larger raw pool before filtering, which improves
C-10 defensibility (top-5 selection is more honest when made from a completed pool rather
than incrementally). Explicit lifecycle labels also make C-05 AMEND more actionable (C-09)
by running AMEND as a structured evaluation step, not a postscript.

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in two distinct phases. Do not mix them. Complete Phase A fully before
starting Phase B.

---

## PHASE A — DIVERGE

**Your role in this phase: idea generator. Generate without evaluating. Quantity over
quality. Cover as much of the option space as possible.**

Generate at least 25 raw candidates for {{topic}}. Write each in this compact format:

```
- **[Name]** | [Category] | [Pitch]
```

Requirements for Phase A:
- No filtering or ranking at this stage
- Cover at least these dimensions: scope, timing, integration, audience, build-vs-buy, status quo
- The status quo entry is mandatory: name it **"Do Nothing"** or **"Status Quo"** with a
  pitch that describes what the current trajectory produces for {{topic}}
- Spread ideas across at least 4 categories
- Aim for 25-40 entries before stopping

---

## PHASE B — CONVERGE

**Your role in this phase: evaluator. Organize, deepen, and select.**

### B-1: Group and deepen

Reorganize the Phase A list under category headers. For each idea, add a Rationale field:

```
## [Category Name]

### [Idea Name]

**Pitch**: [from Phase A]
**Rationale**: [Why this specifically serves {{topic}} — cite a real constraint, user need,
               or opportunity. No generic reasoning.]
```

### B-2: Select top 5

Review the complete pool. Mark exactly 5 ideas with `**` on their heading. These are
your immediate-viability picks — ideas the team could act on today. Be deliberate: the
5 marked ideas should be meaningfully stronger than the ideas you do not mark. Do not
default to marking the first 5 you wrote.

### B-3: AMEND

Write an AMEND section with exactly 3 specific pool-shift adjustments. Each must be
re-runnable — a reader should be able to re-invoke the brainstorm with that directive
and get a noticeably different pool:

```
## AMEND

1. **[Direction label]** — [Which ideas enter, exit, or change rank. Why the pool looks
   different under this lens. What kind of ideas would dominate.]
2. **[Direction label]** — [...]
3. **[Direction label]** — [...]
```

---

## OUTPUT

Write the complete artifact (Phase B output only — Phase A is working material, not final)
to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Total ideas in the final artifact: 20-40. Trim Phase A if you generated more than 40;
keep all entries in range.

---

## V-05 — Combination: Prose Sections + Integrated Inertia Framing

**Axes**: Output format (prose sections with embedded ideas) + inertia framing (status
quo woven through rationales, not siloed as a single entry)
**Hypothesis**: Writing ideas as prose sections rather than lists forces more developed
rationale prose (C-07), while threading inertia comparisons into every category's framing
distributes the "contrast with doing nothing" signal throughout, making C-04 robust
(dedicated entry is still present) and C-07 stronger (rationales are forced to be
comparative rather than standalone assertions). Risk: higher output length may cause
volume to drift above 40 (C-01 upper bound).

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

Generate a ranked idea pool organized as prose sections. The pool must be wide enough
(20-40 ideas) to make the top-5 selection meaningful and the AMEND adjustments honest.

---

**Structure**

Organize the artifact as prose sections — one section per category (minimum 4 categories,
plus the required Status Quo section described below).

Each category section opens with 1-2 sentences framing what this category represents
and why it is a relevant dimension for {{topic}}. Follow with the ideas in that category.

Format for each idea:

```
### ** Idea Name     <- top-5 pick (exactly 5 total across all sections)
                OR
### Idea Name        <- all others

**Pitch**: One sentence describing the idea.

**Rationale**: Why this idea serves {{topic}} — specific to this topic's constraints,
users, or opportunities. Where natural, note what this achieves that the status quo
would not. Avoid generic reasoning.
```

---

**Required section: Status Quo**

Every brainstorm must include a "Status Quo" category section. Place it first or last
(your choice), but it must be present. The section contains exactly one idea: **Do Nothing**.

The section framing should describe what the current trajectory looks like for {{topic}}.
The Do Nothing rationale must answer: what does the team inherit if no decision is made?
What accumulates, what stays stuck, what risks go unaddressed? Do not write "doing nothing
is always an option." Write what doing nothing actually looks like for this topic.

---

**Top-5 selection**

Mark exactly 5 ideas across all categories with `**` on their heading. Distribute the
marks thoughtfully — do not cluster all 5 in one category unless that is genuinely where
the strongest ideas sit. The 5 marked ideas represent your honest read of which candidates
could ship soonest given typical resource and risk constraints.

---

**AMEND**

Close the artifact with an AMEND section. Provide exactly 3 pool adjustments. Each must
name the direction and explain how the pool changes — which ideas gain relevance, which
lose it, and what new candidates might appear:

```
## AMEND

1. **[Direction label]** — [What shifts: entries that enter, exit, or re-rank, and why
   the pool looks different under this lens]
2. **[Direction label]** — [...]
3. **[Direction label]** — [...]
```

---

**Artifact**

Write to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Total ideas across all sections (including Do Nothing in Status Quo): 20-40.

---

## Rubric Coverage Analysis

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 volume (20-40) | Explicit in table | Explicit at end | Stated (20-40) | Phase A 25+, B trim to range | Stated at top + end |
| C-02 idea anatomy | Table columns force it | Per-idea block | 4 questions per idea | Phase A compact, Phase B full block | Per-idea block |
| C-03 top-5 marker | YES column in table | `**` heading prefix | `**` heading prefix | B-2 explicit step | `**` heading prefix |
| C-04 inertia check | Required row, rationale named | Phase 0 mandatory + framing para | Named inline, real rationale required | Mandatory in Phase A dimensions | Required section, rationale rules explicit |
| C-05 AMEND (3 items) | Step 3, 3 items | Phase 2, 3 items | End section, 3 items | B-3 explicit step | Close section, 3 items |
| C-06 category grouping | Step 2 regrouping | Category headers | Group under headers | Phase B headers | Prose sections per category |
| C-07 rationale specificity | "cite a real constraint" | "contrast with Do Nothing" | "tie to real constraint" | "cite a real constraint" | Woven comparison throughout |
| C-08 category diversity (4+) | "at least 4" stated | "at least 4 categories" | "at least 4 angles" | "at least these dimensions" (6 named) | "minimum 4 categories" |
| C-09 AMEND actionability | "state what changes in pool" | "specific enough to re-run" | Named direction + pool change | "re-runnable" explicit | "explain how pool changes" |
| C-10 top-5 defensibility | Not addressed | Not addressed | "defensible: could give real answer" | "meaningfully stronger, don't default to first 5" | "honest read", "thoughtfully distribute" |

**Observations**:
- V-04 is strongest on C-10 (explicit "do not default to marking the first 5 you wrote")
- V-05 is strongest on C-07 (inertia comparison threaded into every rationale)
- V-01 is weakest on C-10 and C-09 (table format leaves no room for defensibility framing)
- V-02 is strongest on C-04 (Phase 0 forces the model to think about inertia before any idea)
- V-03 may produce most diverse categories (C-08) due to question-driven exploration framing
