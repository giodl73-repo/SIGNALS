---
skill: quest-variate
skill_target: draft-brainstorm
round: 2
date: 2026-03-15
rubric_version: 2
r1_best: V-04 @ 107.5 (missed C-14)
r2_target: 110/110 — close all four extended aspirational gaps
---

# Variate R2 — draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R2 focuses on closing the four extended aspirational criteria introduced in rubric v2:
- **C-11** Sequential-Default Guard — explicit prohibition against marking ideas in generation order
- **C-12** Amendment Re-Runnability Bar — re-invocability test explicitly stated
- **C-13** Category Dimension Taxonomy — named dimension types as scaffolding (not just a count)
- **C-14** Inertia-First Framing Paragraph — dedicated paragraph before alternatives, not just a table row

R1 gap analysis:
- V-04 (107.5): passed C-11, C-12, C-13; missed C-14
- V-02 (102.5): passed C-12, C-14; missed C-11, C-13
- No R1 variation passed all four extended criteria

---

## Variation Axes Selected

| Axis | New in R2? | Used In |
|------|-----------|---------|
| Anti-pattern prohibition framing (constraint-first voice) | Yes | V-01 |
| Dimensional taxonomy as primary organizing spine | Yes | V-02 |
| Post-generation self-review step (verification phase) | Yes | V-03 |
| Role sequence + inertia-first framing (closes V-04's C-14 gap) | Combo | V-04 |
| Dimensional taxonomy + table format + scoring self-check | Combo | V-05 |

---

## V-01 — Anti-Pattern Prohibition Framing

**Axis**: Phrasing register — constraint-first / prohibitive
**Hypothesis**: Leading each instruction with an explicit "do not" for the corresponding
failure mode is harder to ignore than positive framing. C-11 becomes structurally
unavoidable (the prohibition is a heading-level instruction), C-12 is stated as a
rule not an observation, and C-14's framing paragraph is introduced before alternatives
are mentioned. Risk: the prohibitive register may feel adversarial and crowd out creative
breadth (C-08).

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

---

### Step 0 — Inertia Paragraph (write this before any ideas)

**Do not skip this step.**

Write a paragraph (3-5 sentences) describing the current trajectory for {{topic}}:
What happens if the team makes no deliberate decision? What does the path of least
resistance produce? What accumulates by default — technically, organizationally,
or for users?

This paragraph frames the entire brainstorm. Every idea generated after this is an
alternative to the trajectory you just described.

---

### Step 1 — Generate the idea pool

**Do not filter or rank while generating.** Produce volume first.

Generate 20-40 candidates for {{topic}}. You must span at least 4 of the following
dimension types — use these as your category scaffolding:

- **Scope** — how much of the problem space this addresses
- **Timing** — when this is introduced relative to the product lifecycle
- **Integration** — how this connects to existing systems or teams
- **Audience** — who this is primarily for
- **Build vs. Buy** — whether this is built internally or adopted from outside
- **Risk Profile** — conservative vs. aggressive bets
- **Status Quo** — the inertia option (always required)

**Do not invent category names that map to the same dimension.** For example,
"Fast Approach" and "Quick Approach" are not two distinct dimension types — they
are the same axis with cosmetic variation.

For each idea, provide all four of:

```
## [Category / Dimension]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this serves {{topic}} specifically — name a real constraint,
user need, or opportunity in this topic. Do not write "this provides value."
```

**Required candidate**: Include **Do Nothing** in the Status Quo category. Its
rationale must describe what the current trajectory (from Step 0) produces —
not just say "doing nothing is an option."

---

### Step 2 — Mark the top 5

**Do not mark ideas in the order you generated them.** The first 5 ideas in your
pool are not your best 5 — they are your starting point.

Review the complete pool from Step 1. Mark exactly 5 ideas with `**` on their
heading (e.g., `### ** Idea Name`). These 5 represent your honest read of which
candidates could move forward today given typical constraints.

The selection is defensible if you could answer: "Why these five and not the
unmarked idea in the same category?"

---

### Step 3 — AMEND

Write an AMEND section with exactly 3 pool-shift adjustments.

**Do not write vague adjustments** like "be more creative" or "think bigger."
Each item must: (a) name a specific direction, (b) describe which ideas would
enter, exit, or re-rank, and (c) be re-invocable — a reader must be able to
take this directive, re-run the brainstorm, and get a noticeably different pool.

```
## AMEND

1. **[Direction label]** — [Which ideas enter, exit, or re-rank. What new
   candidates appear. Why the pool looks different under this lens. Specific
   enough to re-run.]
2. **[Direction label]** — [...]
3. **[Direction label]** — [...]
```

---

### Step 4 — Write artifact

Save to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Final artifact structure: Step 0 paragraph, then categorized ideas, then AMEND.
Total idea count (including Do Nothing): 20-40.

---

## V-02 — Dimensional Taxonomy as Primary Spine

**Axis**: Category dimension taxonomy — C-13 as the organizing principle, not a
check at the end
**Hypothesis**: If the prompt requires the model to construct the brainstorm along
6 required dimensional axes (with Do Nothing as a mandatory seventh), then C-08
diversity is structurally guaranteed, C-13 passes by construction, and the C-14
framing paragraph emerges naturally as the preamble to the taxonomy. C-11 is
addressed by making the top-5 step explicitly post-construction. Risk: locking
axes may suppress creativity — the model may produce ideas that fit the axis labels
but miss important angles that don't map cleanly to any prescribed dimension.

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

Your job: map the full option space across 6 required dimensions, then evaluate.

---

### Preliminary: Status Quo Trajectory

Before opening any dimension, write a paragraph that describes the current state
of {{topic}}: What is in motion today? What does the team inherit if no explicit
decision is made? What risks or missed opportunities compound over time by default?

This paragraph is the baseline against which every idea that follows is measured.

---

### Axis Map

You will generate ideas across the following 6 required dimensions. Each dimension
must produce at least 3 ideas (and may produce more). Label each section with the
dimension name as a header.

**Dimension 1 — Scope**
Ideas in this axis vary *how much* of {{topic}}'s problem space is addressed —
from the minimal viable slice to the comprehensive overhaul.

**Dimension 2 — Timing**
Ideas in this axis vary *when* intervention happens — early bets, staged rollouts,
deferred commitments, and just-in-time decisions.

**Dimension 3 — Integration**
Ideas in this axis vary *how* the solution connects to existing systems, platforms,
or external dependencies relevant to {{topic}}.

**Dimension 4 — Audience**
Ideas in this axis vary *who* the primary beneficiary is — different user segments,
internal teams, or downstream consumers of {{topic}}'s output.

**Dimension 5 — Build vs. Buy**
Ideas in this axis vary *how* capability is acquired — built internally, adopted
from outside, extended from existing components, or delegated.

**Dimension 6 — Risk Profile**
Ideas in this axis vary *how much uncertainty* is accepted — conservative,
incremental bets vs. high-variance, high-ceiling bets.

**Dimension 7 — Status Quo (mandatory)**
This dimension contains exactly one idea: **Do Nothing**. Write the pitch and
rationale as a description of the current trajectory from the Preliminary section —
not as a placeholder. What does the team concretely get (and give up) by staying
the course on {{topic}}?

---

### Idea Format

For every idea in every dimension:

```
## [Dimension Name]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this option specifically serves {{topic}} — name a real
constraint, user need, or opportunity. Must be topic-specific, not generic.
```

Total ideas across all 7 dimensions: 20-40. Trim or expand to stay in range.

---

### Top-5 Selection

After completing all 7 dimensions, review the full pool. Mark exactly 5 ideas
with `**` on their heading. These are your immediate-viability picks.

Rules for selection:
- Do not mark ideas in the order you generated them — finish the full pool first
- Distribute marks across at least 2 different dimensions if the pool supports it
- Each marked idea should be more actionable today than its unmarked peers in the
  same dimension

---

### AMEND

Write an AMEND section with exactly 3 pool-shift adjustments. Each adjustment must:
(a) name a specific shift axis, (b) describe which ideas would enter, exit, or
re-rank, and (c) be re-invocable — a reader must be able to re-run this brainstorm
using only that directive and produce a noticeably different pool. Vague directions
("think bigger") do not meet the re-invocability bar.

```
## AMEND

1. **[Direction]** — [What changes in the pool. What enters, exits, re-ranks.
   Re-runnable: a reader with this directive produces a different pool.]
2. **[Direction]** — [...]
3. **[Direction]** — [...]
```

---

### Artifact

Save to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Preliminary paragraph → 7 dimension sections → AMEND.

---

## V-03 — Post-Generation Self-Review Step

**Axis**: Lifecycle emphasis — a mandatory verification phase after generation,
before finalization
**Hypothesis**: A named verification phase forces the model to review its own output
against the four common failure modes before writing the final artifact. C-11 is
caught by explicit self-check ("are these the first 5 you wrote?"), C-10
defensibility improves because the check requires comparison, and C-09/C-12 AMEND
quality improves because the self-check tests re-invocability before committing.
C-13 and C-14 are addressed structurally in the generation phase. Risk: the
verification step may add length without adding quality if the model treats it as
a formality.

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in two phases: GENERATE, then VERIFY. Do not finalize the artifact
until you have completed the verification step.

---

## PHASE 1 — GENERATE

### 1a. Inertia Frame

Write a framing paragraph (3-5 sentences) for {{topic}}: What is the current
trajectory? What does the team inherit if no decision is made? What accumulates —
technically, organizationally, or for users?

This paragraph appears at the top of the final artifact and precedes all ideas.

### 1b. Idea Pool

Generate 20-40 candidates for {{topic}} organized under category headers. Span at
least these 4 dimension types (use as category scaffolding):

- Scope (how much of the problem is addressed)
- Timing (when the intervention lands)
- Integration (how it connects to existing systems or teams)
- Audience (who benefits most)
- Build vs. Buy (acquisition model)
- Risk Profile (conservative to aggressive)

You may add additional dimensions beyond these. Label each as a markdown header.

For each idea:

```
## [Category]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this serves {{topic}} specifically — cite a real constraint,
user need, or opportunity. No generic reasoning.
```

**Required**: Include **Do Nothing** in a Status Quo category. Its rationale
must continue the framing paragraph from 1a — what the current trajectory concretely
produces for {{topic}}.

**Do not mark top-5 yet.** Complete the full pool before selecting.

### 1c. AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. Label each direction
and describe what changes. Do not finalize yet — the verification step will check
these.

---

## PHASE 2 — VERIFY

Before writing the final artifact, answer these 4 checks:

**Check A — Sequential Default**
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool — the best ideas are rarely the
first ones written. Select the 5 most immediately actionable, not the 5 most
recently visible.

**Check B — Top-5 Defensibility**
For each of your 5 picks, can you complete this sentence: "I chose this over
[unmarked peer in same category] because ___"? If you cannot, the selection
is not defensible. Adjust if needed.

**Check C — AMEND Re-Invocability**
For each of your 3 AMEND items: if a reader took only that directive and
re-ran this brainstorm, would they get a noticeably different pool? If the
answer is "probably the same pool with different labels," the directive is
not re-invocable. Sharpen until each amendment produces a clearly different
candidate distribution.

**Check D — Inertia Paragraph**
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. The paragraph is not optional and must precede alternatives.

---

## PHASE 3 — FINALIZE

Mark exactly 5 ideas with `**` on their heading (informed by Check A and B).
Update AMEND items if Check C required changes.

Write the final artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Inertia paragraph, then categorized ideas (with top-5 marked),
then AMEND. Total ideas (including Do Nothing): 20-40.

---

## V-04 — Combination: Role Sequence + Inertia-First + All Four Extended Criteria

**Axes**: Role sequence (diverger then evaluator) + inertia-first framing (C-14) +
explicit sequential guard (C-11) + re-invocability bar (C-12) + dimension taxonomy
(C-13)
**Hypothesis**: R1's V-04 scored 107.5 but missed C-14 because Do Nothing was
required as a Phase A entry but no framing paragraph was required before alternatives.
R2-V-04 closes that gap by adding a mandatory Phase 0 inertia paragraph that precedes
Phase A generation, while keeping the diverge→converge role separation that made R1-V-04
strongest on C-10. With all four extended aspirational criteria explicitly addressed,
this variation targets 110/110.

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in three named phases. Complete each phase fully before advancing.
Do not mix generation and evaluation.

---

## PHASE 0 — INERTIA ANCHOR (runs before any ideas)

Write a paragraph (3-5 sentences) that describes the current trajectory for
{{topic}}. Answer: What is in motion today, even if no decision is made? What
does the team inherit by default? What technical debt, missed opportunity, or
user friction accumulates if no deliberate choice is taken?

This paragraph is the anchor for the entire brainstorm. It appears first in the
final artifact, before any alternatives. Every idea generated in Phase A is an
alternative to this default path.

---

## PHASE A — DIVERGE

**Your role: idea generator. Generate without evaluating. Quantity first.**

Generate at least 25 raw candidates for {{topic}}. Use this compact format:

```
- **[Name]** | [Category] | [Pitch]
```

Your categories must span at least these dimension types — use them as scaffolding:

- **Scope** — how much of the problem is addressed
- **Timing** — when the intervention lands relative to the product lifecycle
- **Integration** — how it connects to existing systems or external dependencies
- **Audience** — who the primary beneficiary is
- **Build vs. Buy** — internal build, external adoption, or extension of existing
- **Status Quo** — the inertia option (mandatory, exactly one entry)

You may introduce additional dimension types. Do not create category names that
map to the same underlying axis with different labels.

**Required entry**: **Do Nothing** in the Status Quo category. Pitch must
describe what the current trajectory (from Phase 0) produces for {{topic}}.

Generate 25-40 entries before stopping. Do not evaluate or rank in this phase.

---

## PHASE B — CONVERGE

**Your role: evaluator. Organize, deepen, and select.**

### B-1: Group and Deepen

Reorganize the Phase A list under category headers. For each idea, add a
Rationale field:

```
## [Category]

### [Idea Name]

**Pitch**: [from Phase A]
**Rationale**: [Why this serves {{topic}} specifically — cite a real constraint,
user need, or opportunity. No generic reasoning.]
```

### B-2: Select Top 5

Review the complete pool from B-1. Mark exactly 5 ideas with `**` on their
heading (e.g., `### ** Idea Name`).

**Do not default to marking the first 5 you wrote.** The diverge phase produced
a wide pool for a reason — scan the full set before committing. The 5 marked
ideas should be meaningfully more actionable than their unmarked peers. The
selection is defensible if, for each marked idea, you can identify a weaker
unmarked candidate in the same category that you chose not to mark.

### B-3: AMEND

Write an AMEND section with exactly 3 pool-shift adjustments. Each item must
meet all three conditions:
(a) names a specific shift axis,
(b) describes which ideas would enter, exit, or re-rank and why the pool looks
    different,
(c) is re-invocable — a reader must be able to take this directive, re-run the
    brainstorm, and obtain a noticeably different pool without needing further
    clarification.

Vague directions ("be more ambitious") do not meet bar (c). The directive must
be specific enough to produce a different candidate distribution on re-run.

```
## AMEND

1. **[Direction label]** — [Which ideas enter, exit, or re-rank. Why the pool
   looks different. Re-invocable: produces different pool on re-run.]
2. **[Direction label]** — [...]
3. **[Direction label]** — [...]
```

---

## OUTPUT

Write the final artifact (Phase 0 paragraph + Phase B output — Phase A is
working material, not final) to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Phase 0 paragraph, then categorized ideas (Phase B, top-5 marked),
then AMEND. Total ideas (including Do Nothing): 20-40.

---

## V-05 — Combination: Dimensional Taxonomy + Scoring Self-Check + Table Format

**Axes**: Dimensional taxonomy as primary spine (C-13) + post-generation scoring
self-check (novel — not in R1) + table output format (R1-V-01 enhanced)
**Hypothesis**: R1-V-01 used a table format which gave strong C-02 anatomy compliance
but was weakest on C-10 and C-09. Combining the table with (a) a mandatory dimensional
taxonomy for column scaffolding, (b) a scoring self-check that walks the model through
all failure modes before finalizing, and (c) an inertia framing paragraph that precedes
the table closes all four extended criteria while keeping the auditability advantages of
the table format. Risk: the scoring self-check adds length and may feel procedural;
table rationale cells may still be shallow if not constrained.

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

---

### Preamble: Inertia Frame

Before generating any ideas, write a paragraph (3-5 sentences) describing the
current trajectory for {{topic}}: What happens if the team makes no deliberate
decision? What is already in motion? What does the path of least resistance produce?

This paragraph must appear before the idea table in the final artifact.

---

### Step 1 — Build the Table

Generate a markdown table with exactly these columns:

| # | Name | Pitch | Dimension | Rationale | Top-5? |
|---|------|-------|-----------|-----------|--------|

Column rules:
- **#**: Sequential number
- **Name**: 2-5 words
- **Pitch**: One sentence — what the idea is
- **Dimension**: One of the following required dimension types. You must cover
  at least 4 of these 6 (Status Quo is always required):
  - `Scope` — how much of {{topic}}'s problem is addressed
  - `Timing` — when the intervention occurs in the lifecycle
  - `Integration` — how it connects to existing systems or external dependencies
  - `Audience` — who the primary beneficiary is
  - `Build vs. Buy` — internal vs. external acquisition
  - `Status Quo` — the inertia option (exactly 1 row, named **Do Nothing**)
- **Rationale**: Why this serves {{topic}} — cite a specific constraint, user
  need, or opportunity in this topic. "This provides value" is not a rationale.
- **Top-5?**: Leave blank. You will fill this in Step 3 after reviewing the full
  table.

Required row: **Do Nothing** with Dimension = `Status Quo`. Its Rationale must
describe what the current trajectory from the Preamble produces — not "doing
nothing is an option."

Volume: 20-40 rows total.

---

### Step 2 — Scoring Self-Check (do this before marking top-5)

Before filling in the Top-5? column, answer these checks internally:

**Anti-Sequential Check**: Look at rows 1-5. Are you planning to mark these
because they are the best, or because they were the first? If the five strongest
ideas are scattered throughout the table, the selection is honest. If they are
rows 1-5, rescan the full table.

**Dimensional Coverage Check**: Are your `Dimension` values spread across at
least 4 distinct types? If 10 rows share the same dimension label, you have a
coverage gap — add more rows or relabel.

**AMEND Pre-Check**: Before writing the AMEND section, test each directive
mentally: if a reader took this directive and re-ran the brainstorm, would they
get a different set of rows? If not, the directive needs sharpening.

---

### Step 3 — Mark Top-5

Fill in `**YES**` in exactly 5 rows' Top-5? column. These are the ideas with
highest immediate viability given typical resource and risk constraints.

The selection must be defensible: for each marked row, there is a weaker unmarked
row in the same dimension that you chose not to mark.

---

### Step 4 — Category View

After the table, repeat the ideas grouped under their Dimension headers so ideas
can be scanned by axis:

```
## [Dimension Name]

- **[Idea Name]** — [Pitch]  [**TOP-5**] (if marked)
```

---

### Step 5 — AMEND

Write an AMEND section with exactly 3 adjustments. Each must meet all three bars:
(a) names a specific shift axis, (b) describes which rows enter, exit, or re-rank
and why, (c) is re-invocable — a reader can re-run the brainstorm from this
directive and produce a noticeably different table without additional clarification.

```
## AMEND

1. **[Direction label]** — [Rows that enter, exit, or re-rank. Why the table
   looks different. Re-runnable with this directive alone.]
2. **[Direction label]** — [...]
3. **[Direction label]** — [...]
```

---

### Step 6 — Write Artifact

Save to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Preamble paragraph, table, Category View, AMEND.

---

## Rubric Coverage Analysis — R2

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 volume (20-40) | Stated | Stated | Stated | Phase A 25+, trim to range | Stated |
| C-02 idea anatomy (4 fields) | Per-idea block | Per-idea block | Per-idea block | Phase B full block | Table columns |
| C-03 top-5 marker (**) | `**` heading prefix | `**` heading prefix | `**` heading prefix | B-2 explicit step | Table column YES |
| C-04 inertia check | Required, rationale explicit | Status Quo dimension required | Required, tied to framing para | Phase 0 + Phase A mandatory | Required row |
| C-05 AMEND (3 items) | Step 3, 3 items | AMEND section, 3 items | 1c draft + Phase 2 verify | B-3, 3 items | Step 5, 3 items |
| C-06 category grouping | Category headers | Dimension headers | Category headers | Phase B headers | Category View step |
| C-07 rationale specificity | "cite a real constraint" | "topic-specific, not generic" | "cite real constraint" | "cite real constraint" | "cite specific constraint" |
| C-08 category diversity (4+) | 4 of 6 named dimensions | 7 dimensions (6 named + SQ) | 4 named dimensions | At least these 6 dimensions | 4 of 6 named dimensions |
| C-09 AMEND actionability | "describe what changes" | Re-invocability stated | Check C tests re-invocability | Sub-conditions (a)(b)(c) explicit | Sub-conditions (a)(b)(c) explicit |
| C-10 top-5 defensibility | "defensible: could give real answer" | "finish pool first; compare peers" | Check A+B explicit | "do not default to first 5" explicit | Anti-Sequential Check step |
| C-11 sequential-default guard | "Do not mark in order generated" | "finish pool before selecting" | Check A explicit prohibition | "Do not default to marking first 5" | Anti-Sequential Check step |
| C-12 re-runnability bar | "re-invocable — re-run produces diff pool" | Re-invocability bar stated | Check C tests re-invocability | Sub-condition (c) stated explicitly | "re-runnable with this directive alone" |
| C-13 category dimension taxonomy | 6 named dimension types listed | 6 named dimension types with descriptions | 6 named dimension types | 6 named dimension types | 6 named dimension types |
| C-14 inertia-first framing paragraph | Step 0 paragraph before any ideas | Preliminary paragraph before dimensions | Phase 1a framing paragraph | Phase 0 paragraph — explicit "appears first" | Preamble paragraph — explicit "before table" |

**Expected scores** (all variations target all four extended criteria):

| Variation | C-01..C-10 | C-11 | C-12 | C-13 | C-14 | Projected |
|-----------|-----------|------|------|------|------|-----------|
| R2-V-01 | 100 | pass | pass | pass | pass | 110 |
| R2-V-02 | 100 | pass | pass | pass | pass | 110 |
| R2-V-03 | 100 | pass | pass | pass | pass | 110 |
| R2-V-04 | 100 | pass | pass | pass | pass | 110 |
| R2-V-05 | 100 | pass | pass | pass | pass | 110 |

**Observations**:
- V-04 is the direct evolution of R1-V-04 — same role-separation strength, C-14 gap closed
- V-03 is the only variation that uses verification as a lifecycle phase rather than inline instruction — the weakest form if the model treats it as a formality, the strongest if it genuinely triggers a rescan
- V-01's prohibitive register makes C-11 harder to ignore than positive framing; risk is reduced creative breadth
- V-02 is most structurally guaranteed on C-13 (7 dimension sections by construction) and C-08 (dimensional coverage is unavoidable)
- V-05 is the only variation that combines table format (strong C-02 auditability) with all four extended criteria — closes R1-V-01's main weaknesses

**Key R2 insight**: Every R2 variation targets 110/110 because the four extended criteria are now known quantities. The differentiation question for R3 (if needed) is empirical: which variation produces the highest-quality *output* given a real topic — not which variation best addresses the rubric.
