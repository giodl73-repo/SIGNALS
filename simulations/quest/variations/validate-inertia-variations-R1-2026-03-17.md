Written to `simulations/quest/variations/validate-inertia-variations-R1-2026-03-17.md`.

---

## Summary

5 variations across 4 axes:

| # | Label | Axis | Hypothesis |
|---|-------|------|------------|
| V-01 | Baseline | Role sequence (persona-first) | Front-loading persona enumeration forces C-01 groundedness, prevents generic risk lists |
| V-02 | Scorecard table | Output format | Table columns make C-02/C-05/C-07 structurally impossible to omit |
| V-03 | Status-quo competitor | Inertia framing | Framing incumbent as competitor forces C-04 specificity -- Claude must explain why the persona "bought" the workaround |
| V-04 | Imperative register | Phrasing register | Short imperative steps with explicit output specs eliminate narrative-only outputs that fail C-05 |
| V-05 | Kill-barrier-first + phases | Combined | Kill barrier stated in Phase 1 before persona analysis -- C-03 can never be buried, and must justify the table that follows |

**Design tensions being tested:**
- **V-02 vs V-01**: Does the table over-constrain persona nuance, or does it cut omission errors on C-02/C-05?
- **V-03 vs V-01**: Does competitor framing deepen C-04, or does it crowd out habit/social proof depth?
- **V-04 vs V-01**: Does imperative register eliminate narrative-only outputs, or does it produce mechanical lists that miss C-01 groundedness?
- **V-05**: Does kill-barrier-first eliminate the most common failure mode (C-03 generic or buried), and does the 3-phase gate pay for its verbosity?

**Structural choices driving the key rubric risks:**
- C-03 (hardest to pass): V-04 enforces the label format literally; V-05 forces the hypothesis before any analysis can distract from it
- C-05 (score as artifact): V-02 and V-05 make the score a table column -- omitting it breaks the table
- C-10 (aspirational, structural vs. behavioral asymmetry): V-05 surfaces it explicitly in Phase 3 as an optional but prompted output
on forces groundedness (C-01) and prevents
generic risk lists by anchoring every claim to a named individual.

```
You are running /validate-inertia for topic: {topic}.

PURPOSE: Stress-test the adoption case. Even if this feature works perfectly, why would
users NOT adopt it? This is not a risk list -- it is an inertia analysis per persona.

STEP 1 -- PERSONA INVENTORY
Read the topic context: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.
Identify 3-5 distinct user personas from the signals. List each by name and role
(e.g., "Maya -- senior backend engineer who owns the deployment pipeline").
If no signals exist, construct personas from first principles for this topic.

STEP 2 -- WORKAROUND AUDIT
For each persona: what does this person do TODAY to solve the problem this feature addresses?
Name the specific workaround (a script, a convention, a tool, a manual step).
Assess how well it solves the problem on a 1-5 satisfaction scale with a one-line rationale.
A score of 4+ means the workaround is "good enough" -- flag these personas.

STEP 3 -- PERSONA INERTIA ANALYSIS
For each persona, analyze adoption resistance across four dimensions:
  - Switching cost: what would this persona have to change, abandon, or re-learn?
    Express at least one cost in concrete units (hours, steps, files, dollars, risk level).
  - Habit lock-in: what behavioral pattern or workflow ritual makes this persona
    likely to revert even after initial adoption?
  - Social proof: what does this persona need to see before they trust the feature enough
    to adopt? Be specific (e.g., "3 teammates using it daily", "a public case study").
  - Learning curve: how long does ramp-up take? Compare to something the persona already
    knows if possible (e.g., "similar to learning X, which took 2 days").

STEP 4 -- INERTIA SCORE
Assign each persona an inertia score: Low / Medium / High / Critical.
Use this scale consistently:
  Low = will likely adopt with no intervention
  Medium = needs onboarding support or social proof
  High = will resist without product changes or strong peer pressure
  Critical = will not adopt under current conditions

STEP 5 -- KILL BARRIER
Identify the single barrier most likely to block adoption entirely across all personas.
Label it explicitly as "Kill Barrier:" followed by one sentence naming the specific
mechanism (not a generic risk). This must be feature-specific.

STEP 6 -- SYNTHESIS
Write 2-3 sentences summarizing overall adoption inertia risk level (Low/Medium/High/Critical)
and the single most actionable mitigation for the kill barrier.

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-02: Scorecard table (output format axis)

Axis: Output format -- replace per-persona prose sections with a structured scorecard
table; synthesis and kill barrier remain as prose below the table

Hypothesis: A table with one column per inertia dimension makes it structurally impossible
to omit switching cost (C-02) or inertia score (C-05), and makes social proof (C-07)
visible at a glance across all personas simultaneously.

```
You are running /validate-inertia for topic: {topic}.

PURPOSE: Produce an adoption inertia scorecard. Even if this feature works perfectly,
why would users NOT adopt it? The scorecard maps each persona's resistance across four
dimensions and assigns a score.

SETUP
Read topic signals: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.
Identify 3-5 personas from the signals. If signals are absent, construct personas
from first principles. List personas before the table.

WORKAROUND BASELINE
Before the scorecard, write one line per persona:
  Persona | Current workaround | Satisfaction (1-5) | Why it's "good enough"

INERTIA SCORECARD
Build this table (one row per persona):

| Persona | Switching Cost (concrete) | Habit / Ritual at Risk | Social Proof Needed | Learning Curve | Inertia Score |
|---------|--------------------------|------------------------|---------------------|----------------|---------------|

Column rules:
- Switching Cost: must include at least one concrete unit -- time (hours/days), effort
  (steps/files), money (dollars), or risk (rollback complexity). "High" alone fails.
- Habit / Ritual at Risk: name the specific behavioral pattern or workflow ritual,
  not a category. "Uses Makefile daily" not "relies on existing tooling".
- Social Proof Needed: specific threshold -- "needs 3 teammates to adopt first" or
  "requires a public case study from a similar-sized team". "Peer validation" alone fails.
- Learning Curve: ramp estimate in time or concept count, or comparison anchor
  ("similar to learning X, which took Y days").
- Inertia Score: exactly one of -- Low / Medium / High / Critical. All rows must use
  the same scale.

KILL BARRIER
After the table, write:
  Kill Barrier: {one sentence -- the single mechanism most likely to block adoption
  entirely. Must be specific to this feature, not a generic observation.}

OVERALL RISK
Synthesize the scorecard into one overall risk rating (Low/Medium/High/Critical)
with a one-sentence rationale. Propose one specific mitigation that directly addresses
the kill barrier -- actionable enough to include in a launch plan.

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-03: Status-quo competitor (inertia framing axis)

Axis: Inertia framing -- the current workaround is treated as a named competitor;
the entire analysis is framed as a competitive displacement problem

Hypothesis: Framing the status quo as a product the feature must displace forces
C-04 (workaround satisfaction) to be specific and grounded, and makes C-01 persona
reasons more concrete because Claude must explain why this persona "bought" the
incumbent solution.

```
You are running /validate-inertia for topic: {topic}.

FRAME: The status quo is a competitor. Before users can adopt this feature, it must
displace something they already use and trust. Your job is to model that displacement
problem persona by persona.

STEP 1 -- IDENTIFY THE INCUMBENT
Read topic signals: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.
Name the primary incumbent solution -- the thing users do today to solve this problem.
This could be a tool, a script, a convention, a manual process, or "nothing formal".
In one paragraph, describe why users chose the incumbent: what job does it do well,
and what does "good enough" look like from their perspective?

STEP 2 -- PERSONA PROFILES
Identify 3-5 personas from the signals (or construct from first principles).
For each persona, answer: why does this person use the incumbent? What made them
"buy" it -- even if it was just habit or default behavior? Name the specific reason
grounded in their role (not generic).

STEP 3 -- DISPLACEMENT COST PER PERSONA
For each persona, map the cost of switching away from the incumbent:
  - What must they give up? (features, familiarity, integrations, control)
  - What must they invest? Express in concrete units: hours to migrate, number of
    steps to change, files to update, risk of rollback.
  - What behavioral pattern would need to break? (the habit or ritual that is
    so automatic they would revert without noticing)

STEP 4 -- ADOPTION THRESHOLD
For each persona: what would it take to get them to switch?
  - Social proof: what specific evidence or peer behavior must they observe first?
  - Learning investment: how long does ramp-up take? Use a comparison if possible.
  - Minimum product bar: is there anything the feature must do differently for this
    persona to even consider switching? (structural vs. behavioral inertia)

STEP 5 -- INERTIA SCORE
Assign each persona an inertia score: Low / Medium / High / Critical.
All scores must use the same scale.

STEP 6 -- DISPLACEMENT VERDICT
Name the kill barrier: the single reason the feature will fail to displace the
incumbent for the largest or most critical segment.
Label it explicitly: "Kill Barrier:"
Then: overall adoption inertia risk (Low/Medium/High/Critical) and one mitigation.

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-04: Imperative register (phrasing register axis)

Axis: Phrasing register -- short imperative commands replace descriptive prose
instructions; no explanation of why steps exist, just what to produce

Hypothesis: Direct imperative commands with explicit output format specs reduce
the chance Claude produces a narrative-only output that fails C-05 (no discrete score),
and make the C-03 kill barrier label requirement impossible to misread.

```
You are running /validate-inertia for topic: {topic}.

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.

1. LIST PERSONAS
   Name 3-5 personas from the signals. Each entry: "Name -- role -- one sentence on
   their relationship to this problem." Construct from first principles if no signals.

2. WORKAROUND CHECK
   For each persona: name their current workaround and rate satisfaction 1-5.
   One line each. Flag any score of 4 or 5.

3. SWITCHING COST
   For each persona: state what they must change to adopt this feature.
   Include at least one concrete unit: hours, steps, files, dollars, or rollback risk.
   Do not use vague language ("significant effort", "some rework").

4. HABIT LOCK-IN
   For each persona: name the specific behavioral pattern that would cause them to
   revert after initial adoption. Must be persona-specific (not "existing tooling").

5. SOCIAL PROOF THRESHOLD
   For each persona: state the specific evidence they need before adopting.
   Example: "needs to see 2 teammates use it without issues for 2 sprints."

6. LEARNING CURVE
   For at least one persona: estimate ramp time or concept count.
   Use a comparison anchor if possible: "similar to learning X, which took Y."

7. INERTIA SCORE
   Assign each persona: Low / Medium / High / Critical.
   Same scale for all. No narrative substitutes -- score required.

8. KILL BARRIER
   Write exactly:
   "Kill Barrier: {one sentence naming the specific mechanism that would prevent
   adoption entirely for the most critical segment -- feature-specific, not generic.}"

9. OVERALL RISK
   One line: overall risk level (Low/Medium/High/Critical).
   One line: mitigation for the kill barrier named in step 8.

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```

---

## V-05: Kill-barrier-first + lifecycle phases + table (combined axis)

Axes combined: Kill barrier identification as Phase 1 (role sequence) + scorecard table
(output format) + explicit phase gates (lifecycle emphasis)

Hypothesis: Forcing kill barrier identification as the first output -- before any per-persona
analysis -- ensures C-03 is never buried in a summary and cannot be generic because
the analysis that follows must justify it. The phase gate structure prevents omissions
by making each output a prerequisite for the next.

```
You are running /validate-inertia for topic: {topic}.

PURPOSE: Map adoption inertia -- why users will NOT adopt this feature even if it works.
Three phases. Each phase produces a required output before the next begins.

--- PHASE 1: KILL BARRIER HYPOTHESIS ---

Read: simulations/scout/**/{topic}-*.md and simulations/discover/**/{topic}-*.md.
Based on what you know about this feature and its likely users, state your kill
barrier hypothesis NOW -- before persona analysis:

  Kill Barrier Hypothesis: {one sentence -- the single mechanism most likely to
  prevent adoption entirely. Must name a specific behavior, role, or structural
  constraint. Not a generic risk.}

You will validate or revise this hypothesis in Phase 2.

--- PHASE 2: PERSONA INERTIA SCORECARD ---

Identify 3-5 personas (from signals or first principles). Build this table:

| Persona | Workaround (satisfaction 1-5) | Switching Cost (concrete) | Habit at Risk | Social Proof Needed | Learning Curve | Inertia Score |
|---------|-------------------------------|--------------------------|---------------|---------------------|----------------|---------------|

Column rules:
- Workaround: name it + satisfaction rating. "None" is valid but must be justified.
- Switching Cost: at least one concrete unit (hours, steps, files, dollars, rollback risk).
  Vague language fails this column.
- Habit at Risk: specific behavioral pattern, not a category.
- Social Proof Needed: specific threshold -- names, numbers, or evidence type.
- Learning Curve: time estimate or concept count; comparison anchor if possible.
- Inertia Score: Low / Medium / High / Critical. Same scale for all rows.

After the table, answer: does the scorecard support or revise your Phase 1 hypothesis?
  "Kill Barrier (confirmed):" or "Kill Barrier (revised):" -- one sentence.

--- PHASE 3: SYNTHESIS ---

Overall adoption inertia risk: Low / Medium / High / Critical
Rationale: one sentence linking the kill barrier to the persona scores.

Mitigation: one specific action that directly addresses the kill barrier -- actionable
enough to include in a launch plan. Do not restate the barrier as a recommendation.

Inertia asymmetry (optional, include if the evidence supports it):
  Structural inertia personas (will not adopt without product changes): {list}
  Behavioral inertia personas (can be overcome with onboarding/framing): {list}
  This distinction identifies permanent lost TAM vs. delayed adoption.

Write artifact to simulations/validate/inertia/{topic}-validate-inertia-{date}.md
with frontmatter: topic, date, persona_count, kill_barrier (one line), overall_risk.
```
