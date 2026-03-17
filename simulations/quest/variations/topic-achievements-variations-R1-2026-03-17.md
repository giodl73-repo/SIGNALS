## Quest Variate — topic-achievements R1 (V-01 through V-05)

---

## V-01 — Role Sequence: Scanner → Classifier → Synthesizer

**Axis**: Role sequence — explicit three-role pipeline materializes the artifact list before any classification  
**Hypothesis**: Naming the scan role first and forcing an inventory output before classification prevents hallucinated artifact citations (C-03) and produces more accurate IN-PROGRESS ratios (C-04) because the classifier is constrained to a closed list.

---

```
You are running a three-role achievement scan for topic: $TOPIC

---

**ROLE 1 — Artifact Scanner**

Glob all signal artifacts in `simulations/` that belong to this topic. For each
artifact found, record:
- File path
- Namespace (subdirectory under `simulations/`)
- Skill name (subdirectory under the namespace)
- Date (from filename or frontmatter)

Output the full artifact inventory as a numbered list before proceeding. If no
artifacts exist, say so explicitly and skip to Role 3.

---

**ROLE 2 — Achievement Classifier**

Using ONLY the artifacts listed in Role 1 (cite by name or namespace — no
invented references), classify achievements across all 7 categories:

  exploration — breadth of namespaces touched
  depth       — signal count within any single namespace
  coverage    — fraction of the 9 Signal namespaces represented
  quality     — presence of review/prove/quest artifacts
  chain       — artifacts that reference prior artifacts (iteration evidence)
  discovery   — unexpected findings or hypothesis pivots
  corps/crew  — multi-contributor artifacts or org signals

For each category, list every achievement in it. Assign exactly one state:

- EARNED      — achieved; cite the artifact(s) from Role 1 and the ISO date earned
- IN-PROGRESS — partially achieved; show a numeric ratio (e.g., "3 of 5 namespaces")
                 and cite at least one Role 1 artifact
- LOCKED      — not yet achievable; state the unlock condition (what artifact type,
                 what count, what action)

Constraints:
- No achievement may carry two states.
- No EARNED or IN-PROGRESS entry may cite an artifact not in the Role 1 inventory.
- All 7 categories must appear. If a category has no applicable achievements,
  write: "No achievements yet — [unlock condition]."

---

**ROLE 3 — Synthesis Advisor**

**Falsified** (separate from the 7 categories — the intellectual honesty signal):

  Assign one state using the Role 1 inventory:
  - EARNED if any artifact records a retracted hypothesis, falsified assumption,
    or belief update. Cite the artifact and date. Frame this as a mark of
    rigorous inquiry — following the evidence is the achievement.
  - IN-PROGRESS if a hypothesis artifact exists but has not been tested or
    resolved. State the count of open hypotheses.
  - LOCKED if no hypothesis artifacts exist yet. Write: "This achievement is
    waiting for you — run /prove-hypothesis, follow the evidence wherever it
    leads, and if it surprises you, record it. Retracting a belief is the
    reward, not the penalty."

  Falsified must appear as its own block. It must not be embedded in the
  category loop above.

**Maturity synthesis** (1-3 sentences): Interpret the overall achievement
picture. What does it say about where this topic stands? E.g., "Strong on
exploration, no chain signal yet, Falsified not earned — investigation is
broad but shallow."

**Next recommended action**: Name one specific skill to invoke, the artifact
type it produces, and the achievement it advances. State the current-to-target
transition. Generic instructions ("add more artifacts") are not acceptable.
```

---

## V-02 — Output Format: Table-Primary Grid

**Axis**: Output format — achievement table as the primary artifact, prose as secondary  
**Hypothesis**: A structured table grid makes C-01 (one state per row) and C-06 (all 7 categories present) mechanically verifiable at a glance, and forces numeric ratios into a column rather than prose where they can be omitted.

---

```
Scan all signal artifacts for topic: $TOPIC and compute the achievement picture.

---

**Step 1 — Inventory**

Glob `simulations/` for all files belonging to this topic. Note each file's
namespace, skill name, and date. This inventory is your ground truth — every
EARNED and IN-PROGRESS classification must cite evidence from it.

---

**Step 2 — Achievement table**

Produce a markdown table:

| Category | Achievement | State | Evidence | Date |
|----------|-------------|-------|----------|------|

Rules for each column:
- **Category**: one of the 7 categories (exploration, depth, coverage, quality,
  chain, discovery, corps/crew). All 7 must appear. If a category has no
  achievements at all, include a row with `—` in Achievement and `LOCKED` in
  State.
- **Achievement**: the achievement name.
- **State**: exactly one of `EARNED`, `IN-PROGRESS`, `LOCKED`. One value per row.
- **Evidence**:
  - EARNED: artifact name or namespace from the Step 1 inventory.
  - IN-PROGRESS: numeric ratio (e.g., "4/9 namespaces") + artifact name or
    namespace. Vague qualifiers ("almost there") are not acceptable.
  - LOCKED: the unlock condition — artifact type, count, or action required.
- **Date**: ISO date for EARNED entries. Blank for IN-PROGRESS and LOCKED.

Anti-hallucination rule: no EARNED or IN-PROGRESS Evidence cell may name an
artifact not found in Step 1. If unsure, write the namespace only.

---

**Step 3 — Falsified (dedicated block below the table)**

Falsified is not a category — it is the intellectual honesty signal and the
most important achievement in the plugin. Render it as a standalone block:

```
### Falsified

State: [EARNED / IN-PROGRESS / LOCKED]
Evidence: [cite artifact, or state the condition]
Date: [ISO date if EARNED; blank otherwise]

[1-2 sentences. If EARNED: frame as a mark of rigorous inquiry — following
the evidence is what earned this. If LOCKED: frame as an open invitation —
the achievement is waiting for the first hypothesis that gets tested and
followed wherever it leads, even if it surprises you.]
```

---

**Step 4 — Maturity synthesis**

Write 1-3 sentences interpreting the table as a whole. What does the
achievement picture say about topic maturity? This paragraph must appear
before or immediately after the table — not buried at the end.

Example register: "Strong on exploration (5/9 namespaces), shallow on quality
signals, Falsified not yet engaged — this topic has breadth but lacks
verification depth."

---

**Step 5 — Next recommended action**

One action only. Format:

> **Next action**: Invoke `/[skill-name]` to produce a `[artifact-type]`
> artifact. This advances **[category]** from `[current state]` to
> `[target state]` by supplying `[what is currently missing]`.

Generic advice ("run more skills") is not acceptable.
```

---

## V-03 — Lifecycle Emphasis: Phase-Gated with Hard Boundaries

**Axis**: Lifecycle emphasis — numbered phases with mandatory gate outputs before proceeding  
**Hypothesis**: Hard phase gates prevent the model from compressing or skipping the Falsified structural check (C-02) when in list-completion mode, and force the maturity paragraph (C-09) to exist as a discrete artifact rather than an afterthought.

---

```
Achievement scan for topic: $TOPIC

Execute the following phases in order. Each phase has a mandatory output gate.
Do not compress or skip phases.

---

## PHASE 1 — SCAN

Glob all signal artifacts in `simulations/` for this topic.

Gate output (write this before Phase 2):
- Total artifact count
- Namespace coverage: which of the 9 namespaces have artifacts and how many
  (namespaces: scout, draft, review, flow, trace, prove, listen, program, topic)
- List of artifact file paths

Do not proceed to Phase 2 until this inventory is written.

---

## PHASE 2 — CLASSIFY

For each of the 7 achievement categories, enumerate all defined achievements
and assign a state. Categories:

  exploration · depth · coverage · quality · chain · discovery · corps/crew

State rules:
- **EARNED**: achieved based on Phase 1 inventory. Cite the artifact(s) by
  name or namespace. Include ISO date.
- **IN-PROGRESS**: partially achieved. Show a numeric ratio (e.g., "6 of 10
  artifacts needed"). Cite at least one Phase 1 artifact.
- **LOCKED**: not yet achievable. State the exact unlock condition: which
  artifact type, what count, what action.

Constraints:
- Each achievement carries exactly one state.
- EARNED and IN-PROGRESS citations must reference Phase 1 artifacts only.
  Invented artifact names fail Phase 2 and invalidate dependent phases.
- If a category has no applicable achievements, write: "No achievements
  available yet in this category — [unlock condition]."
- All 7 categories must appear.

---

## PHASE 3 — FALSIFIED

Falsified is structurally separate from the 7 categories. It is the
intellectual honesty signal — the achievement that rewards following the
evidence even when it contradicts your hypothesis. It must appear as its own
section, not embedded in Phase 2's category loop.

Assign one state:
- **EARNED**: a retraction, belief update, or falsified assumption is
  documented in the Phase 1 inventory. Cite the artifact and date. Frame this
  explicitly as a mark of rigorous inquiry — the most prestigious achievement
  on the board because most investigations never earn it.
- **IN-PROGRESS**: a hypothesis artifact exists but has not yet been tested or
  resolved. State count of open hypotheses (e.g., "2 open hypotheses, 0
  resolved").
- **LOCKED**: no hypothesis artifacts exist. Write: "This achievement is
  waiting for you — run /prove-hypothesis, follow the evidence wherever it
  leads, and if it surprises you, write it down. Retracting a belief is the
  reward."

---

## PHASE 4 — SYNTHESIZE

Write a 1-3 sentence maturity synthesis. What does the Phase 2 + Phase 3
output say, taken together, about where this topic stands?

Required: name the strongest signal category, the weakest, and whether
Falsified has been engaged.

Example: "Strong on exploration (4/9 namespaces), shallow on quality signals,
Falsified not yet earned — this topic has width but lacks verification depth."

This paragraph must be present before per-category detail in the final output.

---

## PHASE 5 — RECOMMEND

State the single highest-leverage next action.

Required format:

> **Next action**: Invoke `/[skill-name]` to produce a `[artifact-type]`
> artifact. This advances **[category]** from `[current state]` toward
> `[target state]` by providing `[what is currently missing]`.

The recommended skill must be a real Signal skill. The artifact type must be a
real Signal artifact type. Generic advice ("add more artifacts", "run more
skills") fails Phase 5.
```

---

## V-04 — Synthesis-First + Conversational Register (combo)

**Axes**: Role sequence reversed (synthesizer opens) + conversational/imperative register  
**Hypothesis**: Asking "what does the overall picture look like?" before enumerating categories produces the maturity paragraph (C-09) naturally rather than as a forced afterthought, and the conversational register reduces list-completion pressure that causes state compression.

---

```
Before you list a single achievement, step back and read the topic as a whole.

Topic: $TOPIC

---

**First: read the room**

Scan `simulations/` for every signal artifact belonging to this topic. Don't
classify yet — just look at what's there and notice the shape of it. Then
answer, in 2-3 sentences: what does this topic's signal footprint look like
right now? Is it broad but thin? Deep in one namespace and missing others? Has
anyone followed a hypothesis to a conclusion, or is everything still open?

Write this paragraph before doing anything else. It's your maturity synthesis,
and it will shape how you read every achievement that follows.

---

**Then: work through the seven categories**

For each of the seven categories, tell me what's earned, what's moving, and
what's still locked. The categories are:

  exploration · depth · coverage · quality · chain · discovery · corps/crew

A few rules as you go:

- For EARNED: give a date and cite the real artifact name or namespace from the
  scan. Not something you inferred — something you actually found.
- For IN-PROGRESS: give a number. "3 of 5 namespaces" is good. "Almost there"
  or "partially done" alone is not — add the ratio.
- For LOCKED: give an unlock path. What artifact type unlocks it? What count?
  What action? "Not yet earned" with no path forward doesn't help anyone.
- If a category has nothing to show at all, say so explicitly rather than
  skipping it. All 7 categories must appear.
- Each achievement gets exactly one state. No hedging between two.

---

**Then: Falsified — the one that matters most**

Falsified is not one of the seven categories. It lives apart because what it
measures is different: not volume or breadth, but intellectual honesty. It
rewards following the evidence even when it contradicts what you started out
believing.

Check the artifact inventory: does anything record a retraction, a falsified
assumption, or a pivot away from an earlier belief? If yes — that's EARNED,
and it's the most meaningful achievement on the board. Give it a date and cite
the artifact.

If there's a hypothesis artifact but no resolution yet — that's IN-PROGRESS.
How many open hypotheses are in the inventory?

If there's nothing yet — that's LOCKED. But frame it right: this isn't a
missing box. It's an open invitation. Run /prove-hypothesis, follow wherever
the evidence goes, and if it surprises you, write that down. The moment you
record that surprise is the moment you earn this. Never frame the absence of
Falsified as a failure — it is simply a next step waiting to be taken.

---

**Finally: tell me the one thing to do next**

One action. Name the specific Signal skill to invoke, name the artifact type
it produces, name which achievement it moves and from what state to what state.
Make it specific enough that someone can act on it right now without asking a
follow-up question. If the maturity synthesis in your opening paragraph pointed
at an obvious gap, the next action should attack that gap.
```

---

## V-05 — Gap-First Inertia Framing + Prose + Compressed Lifecycle (combo)

**Axes**: Inertia framing prominent (gaps named first) + prose-primary output + compressed single-pass lifecycle  
**Hypothesis**: Opening with what's missing rather than what's earned orients the reader toward action, improves next-action specificity (C-05) because the gap is already named, and makes LOCKED entries feel like a roadmap rather than a scorecard deficit. Prose format reduces table-filling mechanics and lets Falsified framing (C-10) breathe.

---

```
Topic: $TOPIC
Task: Achievement scan — gap-first orientation

Scan `simulations/` for all signal artifacts belonging to this topic. Then
narrate the achievement picture with the gaps first. The goal is an actionable
picture, not a celebration.

---

**Part 1 — What's missing (LOCKED)**

Start here. For each of the 7 categories — exploration, depth, coverage,
quality, chain, discovery, corps/crew — identify which achievements are locked
and what it would take to unlock them. For each locked achievement, name:
- The artifact type that would unlock it
- The count or threshold required
- The specific Signal skill that produces that artifact type

Vague unlock conditions ("needs more work", "add more signals") are not
acceptable. Every locked achievement gets a concrete path.

If a category has no locked achievements because everything is earned, say so
briefly and move on.

---

**Part 2 — What's moving (IN-PROGRESS and EARNED)**

Now name what's happening. For IN-PROGRESS achievements, show the ratio — how
far along, based on actual artifacts from the scan. Cite by artifact name or
namespace; do not cite artifacts you didn't find. "3 of 5 namespaces" is
acceptable; "partially done" alone is not.

For EARNED achievements, give the date and the artifact or namespace that
sealed it. One sentence per earned achievement is enough — this section is
intentionally proportionate to Part 1, not larger.

---

**Part 3 — Falsified**

Falsified is not part of the 7-category system. It measures something
different: whether this investigation has had the intellectual courage to
follow evidence away from its starting hypothesis. It is the most prestigious
achievement in the Signal system precisely because most investigations never
earn it.

State clearly — EARNED, IN-PROGRESS, or LOCKED — and back it up:
- EARNED: cite the artifact that records the retraction or belief update, and
  the date. Name what belief was held and what replaced it. Frame earning this
  as a marker of rigorous inquiry, not as a record of being wrong.
- IN-PROGRESS: state how many hypothesis artifacts exist and how many have been
  tested or resolved.
- LOCKED: write the invitation. What action produces a testable hypothesis?
  What does following the evidence look like in practice? Frame the locked
  state as "this achievement is waiting for the first honest test" — never as
  a deficit or an absence.

---

**Part 4 — What to do next**

This is the whole point of the scan. Name one specific next action that follows
directly from Part 1. Format:

> Invoke `/[skill-name]` to produce a `[artifact-type]` artifact. This
> unlocks **[achievement name]** in the **[category]** category, advancing
> it from `LOCKED` to `IN-PROGRESS` (or from `IN-PROGRESS` to `EARNED`)
> by supplying `[what is currently missing from the inventory]`.

The named skill must be a real Signal skill. If Part 1 identified multiple
locked achievements, pick the one with the highest leverage — the one whose
unlock would cascade progress into adjacent categories.

---

**Part 5 — Maturity synthesis**

Close with 1-3 sentences reading the full picture: what the gaps and progress
say together about where this topic stands in the signal lifecycle. Name the
strongest area, the weakest, and whether the topic is approaching readiness
for a decision artifact. This synthesis closes the scan — the opening was gaps,
the close is interpretation.
```

---

## Variation Summary

| Variation | Primary Axis | Secondary Axis | Key Hypothesis |
|-----------|-------------|----------------|----------------|
| V-01 | Role sequence (S→C→Synth) | — | Closed inventory list prevents hallucination (C-03) |
| V-02 | Output format (table-primary) | — | Grid format enforces C-01 and C-06 mechanically |
| V-03 | Lifecycle (phase-gated) | — | Hard gates prevent Falsified compression (C-02) |
| V-04 | Role sequence (synth-first) | Conversational register | Natural C-09 paragraph; reduces list-completion pressure |
| V-05 | Inertia framing (gap-first) | Prose + compressed lifecycle | Gap-first orientation improves C-05 next-action specificity |
