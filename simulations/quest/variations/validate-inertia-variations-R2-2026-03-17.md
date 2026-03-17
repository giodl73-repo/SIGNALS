Written to `simulations/quest/variations/validate-inertia-variations-R2-2026-03-17.md`.

---

## Summary

5 variations across 4 axes:

| # | Label | Axis | Hypothesis |
|---|-------|------|------------|
| V-01 | Best-of-R1 baseline | Role sequence + inertia framing | V-05 kill-barrier-first + V-03 competitor framing combined -- new R2 floor |
| V-02 | Asymmetry triage first | Role sequence (structural vs behavioral before personas) | C-10 becomes a deliberate classification, not a post-hoc label |
| V-03 | Mitigation workshop | Lifecycle emphasis (mitigation phase with explicit anti-patterns) | C-09 passes with a specific action when failure modes are named |
| V-04 | Narrative register | Phrasing register (adoption strategist voice, "bet" + "story") | Richer C-06/C-12 via narrative; "bet" structure preserves C-11 |
| V-05 | Compressed scaffold | Output format (every line is a required output spec) | Zero padding forces all criteria without scaffolding noise |

**Key design decisions:**

**C-11 and C-12 are now structural requirements in all 5 variants** -- they were R1 excellence signals, now rubric criteria, so every R2 prompt bakes them in as baseline.

**Main new axis: asymmetry triage (V-02).** C-10 was untested in R1. V-02 makes structural vs behavioral classification its own phase before persona analysis, with the hypothesis that this produces a deliberate C-10 pass rather than an accidental one.

**Design tensions:**
- V-02 vs V-01: Does early asymmetry classification improve C-10 at the cost of persona depth?
- V-03 vs V-01: Does a dedicated mitigation workshop improve C-09, or does the verbosity tax kill-barrier focus?
- V-04: First narrative register test. C-05 (discrete score) is the risk -- does it survive the prose format?
- V-05: Extreme compression. C-06/C-07 depth is the risk -- does absence of explanatory context cause shallow habit/social-proof analysis?
cated mitigation workshop reliably improve C-09, or does the added verbosity dilute kill barrier focus?
- **V-04 vs imperative register (R1 V-04)**: Does narrative register produce richer C-06/C-12 at the cost of C-05 (discrete score feels unnatural in prose)?
- **V-05 vs R1 V-02 (scorecard)**: Does extreme compression with C-11/C-12 baked in outperform R1's table variant, or does missing context cause shallower persona analysis?

**Structural choices driving the key rubric risks:**
- C-11 (kill barrier first): All 5 variants enforce it as the first required output. R2 baseline assumption.
- C-12 (competitor framing): V-01, V-02, V-03, V-05 all require "why they chose the incumbent." V-04 requires the "incumbent's story" in narrative form.
- C-10 (asymmetry): V-02 makes it Phase 2 before personas. V-01, V-03, V-05 include it as a synthesis output. V-04 includes it at the verdict.
- C-09 (mitigation quality): V-03 adds explicit anti-patterns. All variants specify mitigation must not restate the barrier.

---

## V-01: Best-of-R1 combined baseline

Axes: Kill barrier sequenced first (C-11, from R1 V-05) + status-quo as competitor (C-12, from R1 V-03)

Hypothesis: Combining the two winning structural patterns from R1 into a single baseline
should reliably achieve both C-11 and C-12. This becomes the new R2 floor -- the minimum
a well-designed variant should score.

```
You are running /validate-inertia for topic: {topic}.

FRAME: The status quo is a competitor. Before users can adopt this feature, it must
displace something they already use and trust. Your analysis runs in three phases.

--- PHASE 1: KILL BARRIER HYPOTHESIS ---

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

First, name the incumbent -- the tool, script, convention, or manual process users rely
on today to solve the problem this feature addresses.

In one sentence, state why users chose the incumbent: what job does it do well for them?

Now state your kill barrier hypothesis before any persona analysis:

  Kill Barrier Hypothesis: {one sentence -- the single mechanism most likely to prevent
  adoption entirely. Must name a specific behavior, role, or structural constraint. Not
  derived from persona aggregation -- this is a prediction you will validate below.}

--- PHASE 2: PERSONA DISPLACEMENT SCORECARD ---

Identify 3-5 personas from the signals (or construct from first principles). For each
persona, answer: why does this person use the incumbent? What made them "buy" it -- even
if it was just habit or default behavior? Name the role-grounded reason.

Build this table:

| Persona | Why They Use the Incumbent | Switching Cost (concrete) | Habit at Risk | Social Proof Needed | Learning Curve | Inertia Score |
|---------|---------------------------|--------------------------|---------------|---------------------|----------------|---------------|

Column rules:
- Why They Use the Incumbent: the adoption decision -- "X won this persona because their
  role requires..." Not "it works" but WHY it works for this specific person.
- Switching Cost: at least one concrete unit (hours, steps, files, dollars, rollback risk).
  "High" or "significant effort" fails this column.
- Habit at Risk: specific behavioral pattern, not a category. "Runs make check before every
  commit" not "relies on existing tooling."
- Social Proof Needed: specific threshold -- numbers, names, or evidence type. "Peer
  validation" fails.
- Learning Curve: time estimate or concept count; comparison anchor if possible ("similar
  to learning X, which took Y days").
- Inertia Score: Low / Medium / High / Critical. Same scale for all rows. Required for
  every persona.

After the table: does the scorecard confirm or revise your Phase 1 hypothesis?
  "Kill Barrier (confirmed):" or "Kill Barrier (revised):" -- one sentence.

--- PHASE 3: SYNTHESIS ---

Overall adoption inertia risk: Low / Medium / High / Critical
Rationale: one sentence linking the kill barrier to the persona distribution.

Mitigation: one specific action that directly addresses the kill barrier -- actionable
enough to include in a launch plan. Do not restate the barrier as a recommendation.
Do not propose generic onboarding.

Inertia asymmetry (include if the evidence supports it):
  Structural inertia personas (will not adopt without product changes): {list or "none"}
  Behavioral inertia personas (can be overcome with onboarding/framing): {list}

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-02: Asymmetry triage first

Axis: Role sequence -- structural vs behavioral inertia classification at the feature level
runs before persona analysis; kill barrier hypothesis runs before that

Hypothesis: When Claude classifies the feature's inertia landscape as structural vs
behavioral before analyzing any persona, C-10 becomes a deliberate analytical choice
rather than a post-hoc label. The classification also constrains mitigation type:
structural demands a product answer, behavioral demands a launch answer -- and this
constraint propagates into C-09.

```
You are running /validate-inertia for topic: {topic}.

PURPOSE: Map adoption inertia and classify its type. The type of inertia determines the
type of solution. Four phases -- each output gates the next.

--- PHASE 1: KILL BARRIER HYPOTHESIS ---

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

Before any analysis, state your kill barrier hypothesis:
  Kill Barrier Hypothesis: {specific mechanism, role, or structural constraint that would
  prevent adoption entirely. Not generic. Not derived from personas -- this is your
  prediction before looking at the data.}

--- PHASE 2: INERTIA LANDSCAPE CLASSIFICATION ---

Before analyzing individual personas, classify the resistance this feature faces:

  Primary inertia type: Structural | Behavioral | Mixed

  Structural inertia = the feature does not yet satisfy a requirement users consider
  non-negotiable. No amount of onboarding or framing overcomes this -- the product
  must change.

  Behavioral inertia = the feature is capable enough, but habits, workflows, and social
  dynamics prevent adoption. The right launch strategy can reach these users.

  Classification rationale: one sentence explaining which type dominates and why.

  If Mixed: estimate the split (e.g., "60% behavioral, 40% structural") and name the
  structural blocker explicitly.

Name the incumbent -- the tool, script, convention, or process users rely on today.
In one sentence: why did users choose it? What job does it do well for them?

--- PHASE 3: PERSONA DISPLACEMENT SCORECARD ---

Identify 3-5 personas from the signals (or construct from first principles). For each
persona, state why they chose the incumbent -- role-grounded, not generic.

Build this table:

| Persona | Why They Use the Incumbent | Workaround Satisfaction (1-5) | Switching Cost (concrete) | Habit at Risk | Social Proof Needed | Learning Curve | Inertia Score | Inertia Type |
|---------|---------------------------|-------------------------------|--------------------------|---------------|---------------------|----------------|---------------|--------------|

Column rules:
- Why They Use the Incumbent: the adoption decision -- "X won this persona because..."
- Workaround Satisfaction: 1-5 scale. Flag 4+ as "good enough." State the specific reason.
- Switching Cost: concrete units only (hours, steps, files, dollars, rollback risk). Vague fails.
- Habit at Risk: specific behavioral pattern, not a category.
- Social Proof Needed: specific threshold -- names, numbers, evidence type.
- Learning Curve: time or concept count; comparison anchor preferred.
- Inertia Score: Low / Medium / High / Critical. Consistent scale.
- Inertia Type: Structural | Behavioral -- classify each persona individually.

After the table: confirm or revise your Phase 1 hypothesis.
  "Kill Barrier (confirmed):" or "Kill Barrier (revised):" -- one sentence.

--- PHASE 4: SYNTHESIS ---

Overall adoption inertia risk: Low / Medium / High / Critical

Inertia asymmetry:
  Structural (will not adopt without product changes): {personas}
    -- permanent lost TAM until product changes
  Behavioral (can be overcome with onboarding/framing): {personas}
    -- delayed adoption, reachable with launch strategy
  Implication: one sentence on what this means for launch timing or scope.

Mitigation: one specific action targeting the kill barrier.
  If the kill barrier is structural: name the product change required.
  If the kill barrier is behavioral: name the launch sequence or social proof intervention.
  Do not restate the barrier. Do not propose generic onboarding.

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-03: Mitigation workshop

Axis: Lifecycle emphasis -- mitigation gets a dedicated phase with explicit anti-patterns
and a success signal requirement; C-11 and C-12 run as standard baseline

Hypothesis: When mitigation has its own structured phase with named failure modes to
avoid, C-09 passes with a specific, non-trivial action rather than a restated barrier or
a "improve onboarding" placeholder. The success signal requirement further forces
specificity by asking Claude to operationalize the mitigation.

```
You are running /validate-inertia for topic: {topic}.

PURPOSE: Map adoption inertia and produce a launch-ready mitigation plan. This is an
evidence brief a product manager can act on -- not a risk list.

--- PHASE 1: KILL BARRIER HYPOTHESIS ---

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

Before any persona work, state the kill barrier hypothesis:
  Kill Barrier Hypothesis: {the single mechanism most likely to prevent adoption entirely.
  Feature-specific. Stated before persona analysis -- you will confirm or revise below.}

--- PHASE 2: COMPETITOR ANALYSIS ---

Name the incumbent: the tool, convention, or process users rely on today.

For each persona (3-5, from signals or first principles):
  - Why did this persona choose the incumbent? Role-grounded reason -- "X won this persona
    because their role requires..." Not just what they use, but why they use it.
  - Workaround satisfaction (1-5). Flag 4+ as "good enough" and state why.
  - What would switching cost them? At least one concrete unit: hours to migrate, number
    of files to change, dollars, rollback risk. Vague language ("significant effort") fails.
  - What behavioral pattern or ritual keeps them on the incumbent even when it frustrates
    them? Name the specific habit, not the category.
  - What social proof would it take for them to try the feature? Specific threshold.

Assign each persona an inertia score: Low / Medium / High / Critical.

After persona analysis: confirm or revise your Phase 1 hypothesis.

--- PHASE 3: MITIGATION WORKSHOP ---

This phase produces the actionable deliverable. Common failure modes -- avoid these:
  x "Improve onboarding" -- too generic, no owner, unmeasurable
  x "Address the switching cost" -- restates the barrier, not a solution
  x "Provide documentation" -- not targeted at the kill barrier mechanism
  x Any mitigation that does not directly remove or reduce the kill barrier

For the kill barrier, write:

  Kill Barrier: {confirmed or revised -- one sentence}
  Why this kills adoption: {the mechanism, not the symptom -- one sentence}
  Mitigation: {one specific action -- name the product change, launch sequence, social
    proof seeding strategy, or integration that directly removes this barrier. Specific
    enough to assign to an owner.}
  Success signal: {how you would know the mitigation worked -- an observable behavior,
    a metric, or a milestone that signals the barrier is removed}

Overall adoption inertia risk: Low / Medium / High / Critical

Inertia asymmetry (if the evidence supports it):
  Structural inertia personas (product must change): {list}
  Behavioral inertia personas (launch strategy can reach): {list}

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-04: Narrative register

Axis: Phrasing register -- adoption strategist voice, narrative persona portraits, story
framing for the incumbent; kill barrier stated as a "bet" before analysis (C-11 in
narrative form); competitor framing as "incumbent's story" (C-12 in narrative form)

Hypothesis: Narrative register produces richer C-06 (habit lock-in -- behavioral patterns
feel more natural in story form) and C-12 (incumbent adoption story -- "Maya adopted the
bash script because..." is a natural sentence in this register) while the "bet" structure
preserves C-11 structural sequencing. Risk: C-05 (discrete score) may feel unnatural in
prose and get omitted or softened.

```
You are running /validate-inertia for topic: {topic}.

You are acting as an adoption strategist who has watched many well-built features fail
because nobody switched. Your job is to understand why this feature will sit unused
despite working correctly.

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

---

START WITH YOUR BET

Before you look at any persona, write your bet:

  "My bet is that this feature's adoption will be blocked by ___. The specific mechanism
  is ___. I'm stating this before looking at the data so I can test whether the persona
  work confirms or revises it."

This is your kill barrier hypothesis. You will return to it at the end.

---

THE INCUMBENT'S STORY

Name the thing users do today -- the incumbent. But don't just name it. Tell its story.

Why did users adopt it? What does it do for them that feels reliable and familiar? What
is the implicit promise it keeps -- even if it is slow, clunky, or fragile?

For at least one persona, tell the story of how they came to rely on it:
  "Maya adopted the bash script because..."
  "The team uses the manual process because it gives them..."
  "They chose it because at the time, it was the only thing that..."

This is the story your feature must displace.

---

PERSONA INERTIA PORTRAITS

Identify 3-5 personas from the signals (or construct from first principles). For each,
write a portrait addressing these elements:

  Who are they and what is their relationship to this problem?
  What is their current workaround and how satisfied are they? (Rate 1-5.)
  What would switching actually cost them? Use concrete terms: hours, number of files to
    touch, risk of something breaking, investment to migrate existing work.
  What is the habit or ritual that would pull them back -- the behavior that fires before
    they even think about it?
  What would they need to see from colleagues or the community before trusting this feature?
  How long would it take them to feel fluent? Compare to something they already know.

Close each portrait with one line:
  Inertia Score: Low / Medium / High / Critical

---

THE VERDICT

Revisit your bet. Confirmed or revised?

  Kill Barrier: {one sentence -- the specific mechanism that would prevent adoption
  entirely. Must be feature-specific and grounded in what the portrait work revealed.}

Overall adoption inertia risk: Low / Medium / High / Critical

What is the one thing that would change this outcome? Name a specific mitigation --
not "improve onboarding" but the actual intervention: a product decision, a launch
sequence, a social proof seeding strategy, a specific integration. Name the action
and the owner.

Inertia asymmetry (if the portrait work reveals it):
  Who won't adopt without product changes? (structural inertia)
  Who can be reached with the right launch approach? (behavioral inertia)

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-05: Compressed minimal scaffold

Axes: Output format (ultra-compact) + lifecycle emphasis (every line is a required output
spec, zero explanatory padding)

Hypothesis: A minimal prompt where every sentence is a required output specification --
no explanations of why steps exist, no descriptions of what good looks like -- reduces
noise-to-signal ratio. Claude produces all criteria without narrative buffer because there
is no ambiguity about what each section must contain. Risk: absence of context about WHY
each output matters may produce shallower C-06 and C-07.

```
You are running /validate-inertia for topic: {topic}.

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

Produce these sections in order. Do not reorder.

---

1. KILL BARRIER HYPOTHESIS

Kill Barrier Hypothesis: {specific mechanism -- not generic, not derived from personas,
stated before any persona work}

---

2. INCUMBENT

Name: {the tool, script, convention, or process users rely on today}
Why users chose it: "They adopted it because ___." (at least one persona -- the adoption
decision, not just current state)

---

3. PERSONA TABLE (3-5 personas)

| Persona + Role | Why Incumbent Won | Workaround Satisfaction (1-5) | Switching Cost | Habit at Risk | Social Proof Needed | Learning Curve | Inertia Score |
|---------------|-------------------|-------------------------------|----------------|---------------|---------------------|----------------|---------------|

Rules:
- Why Incumbent Won: role-grounded reason, not "it works."
- Switching Cost: concrete units (hours, steps, files, dollars, rollback risk). "High" fails.
- Habit at Risk: specific behavior, not a category.
- Social Proof Needed: specific threshold -- number, name, or evidence type.
- Learning Curve: time or concept count; comparison anchor preferred.
- Inertia Score: exactly Low / Medium / High / Critical. Same scale. Required for every row.

---

4. KILL BARRIER

Kill Barrier (confirmed or revised): {one sentence -- confirm or revise the Phase 1 hypothesis}

---

5. INERTIA ASYMMETRY

Structural (product must change to reach these personas): {list or "none"}
Behavioral (launch strategy can reach these personas): {list}
Lost TAM implication: {one sentence}

---

6. OVERALL RISK + MITIGATION

Overall risk: Low / Medium / High / Critical
Mitigation: {specific action targeting the kill barrier. Not a restatement. Not "improve
onboarding." Specific enough to assign to an owner and measure.}

---

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```
