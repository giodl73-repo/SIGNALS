Written to `simulations/quest/variations/validate-inertia-variations-R1-2026-03-17.md`.

---

## validate-inertia Variations R1

| # | Label | Axis | Primary target |
|---|-------|------|----------------|
| V-01 | Per-persona scoring table | Output format | C-02, C-03 |
| V-02 | Hard phase gating | Lifecycle emphasis | C-01, C-04, C-05 |
| V-03 | Status-quo as named competitor | Inertia framing | C-02, C-06 |
| V-04 | Conversational walkthrough | Phrasing register | C-04, C-07 |
| V-05 | Full rubric stack | Combination | C-01–C-05 + C-06–C-08 |

**Axis choices and rationale:**

Three single-axis variations — output format, lifecycle emphasis, and inertia framing — then a conversational register variation as the fourth single-axis, then a combination.

**Single-axis failure modes targeted:**

- **V-01 (table format)** closes C-02/C-03 together. Prose allows qualitative hedging ("moderate resistance") that passes a surface reading. A table column labeled "Switching cost (quantified)" makes a vague fill visually incomplete; a per-row score table makes a shared blanket score structurally inapplicable.

- **V-02 (phase gating)** closes C-04 deferral. The kill barrier most often fails not because it's omitted but because it's buried in a list and the model fills it with the most available answer. Placing it as a mandatory phase that must commit before the aggregate verdict forces explicit argument.

- **V-03 (status-quo competitor)** closes C-06 by framing the workaround as a named product competing for the same adoption slot — which naturally prompts product-comparison thinking, grounded switching cost numbers, and specific satisfaction assessment. "The current solution does X well" produces more useful C-06 content than "assess workaround satisfaction."

- **V-04 (conversational)** closes C-07 by making habit lock-in and social proof emerge as part of a user story rather than as abstract dimensions to rate. The tradeoff is reduced structural rigidity; the gain is more candid behavioral characterization.

- **V-05** integrates all three without conflict: the competitor framing populates the table (V-03 + V-01), the phase gates enforce kill-barrier commitment (V-02), and C-08 mitigation is added as a required AMEND field.
tput format — inertia factor mapping and per-persona scoring are expressed as
structured tables, making quantification gaps and missing per-persona scores visually
incomplete rather than hidden in prose

**Hypothesis:** C-02 and C-03 fail most often because prose descriptions allow qualitative
hedging ("moderate switching cost", "various resistance levels") that satisfies a surface
reading without providing measurable values or distinct per-persona scores. A table column
labeled "Switching cost (quantified)" makes a qualitative fill like "it's inconvenient"
visually incomplete — the same way an empty cell does — and a per-row score table makes a
single blanket score structurally inapplicable.

```
You are running /validate:inertia for topic: {topic}.

Feature under adoption stress-test: {feature}

This skill stress-tests the adoption case. The goal is not to evaluate the feature's quality
-- assume it works perfectly. The question is: why would the right users still not switch?

PERSONA IDENTIFICATION

Name 2-4 user personas most likely to evaluate this feature for adoption. For each persona:
  - Name and brief role description (one sentence)
  - What outcome they currently achieve using their existing workflow
  - What workaround or tool they already use to get that outcome today

These must be named, specific personas -- not "users" or "developers". A persona without a
named current workaround does not qualify.

INERTIA FACTOR TABLE

Map each persona to the five inertia dimensions in the table below. Fill every cell. If a
dimension genuinely does not apply to a persona, write "N/A -- [one-word reason]".

| Persona | Workaround satisfaction | Switching cost (quantified) | Habit lock-in | Social proof req. | Learning curve |
|---------|------------------------|----------------------------|---------------|-------------------|----------------|

Column definitions:

Workaround satisfaction: How well does their current approach meet the need?
  H = fully or near-fully meets it / M = partially meets it / L = unreliable or painful

Switching cost (quantified): The cost to move from current workaround to the new feature.
  Must be expressed as a measurable value: time (e.g., "~3 hours migration"), money,
  steps required (e.g., "4-step reconfiguration"), or a relative ratio (e.g., "3x more
  setup than current"). Qualitative-only entries ("high effort", "it's annoying") do not
  pass this column.

Habit lock-in: The behavioral pattern that resists change -- muscle memory, workflow
  integration, or mental model. One phrase. Example: "daily keyboard shortcut habit".

Social proof req.: Does adoption require seeing peers adopt first?
  Y = requires peer proof before committing / N = solo adopter viable / ? = unclear

Learning curve: Low / Medium / High, plus one qualifying detail.
  Example: "High -- requires learning new query syntax after years of GUI workflow"

INERTIA SCORES

Assign each persona an overall inertia score and name its primary driver.

| Persona | Inertia score | Primary driver |
|---------|---------------|----------------|

Score scale:
  Low = minimal resistance; switching cost and lock-in are low; workaround is poor
  Medium = meaningful resistance; at least one high-friction dimension present
  High = significant resistance; multiple high-friction dimensions OR high workaround satisfaction
  Critical = adoption-blocking; persona is unlikely to switch regardless of quality

Primary driver: the single dimension from the inertia factor table that dominates for this
persona. One of: workaround satisfaction / switching cost / habit lock-in / social proof /
learning curve.

KILL-BARRIER IDENTIFICATION

Review the inertia factor table and scores. Identify the single barrier most likely to block
adoption across all personas, even after all other friction is resolved.

ADOPTION KILLER: [barrier name -- one of the five inertia dimensions, or a named compound]
Persona most affected: [name]
Why it survives: [why this barrier persists even when switching cost, learning curve, and
  other dimensions are reduced -- what structural property makes it last]

Only one adoption killer. If two seem equivalent, argue for the one that is harder to
address through a product or onboarding change.

OVERALL ADOPTION INERTIA RISK

OVERALL RISK: [Low / Medium / High / Critical]
Rationale: [1-2 sentences -- ties the verdict to the per-persona score distribution and the
  adoption killer; does not re-list every score]

AMEND

Narrow the analysis to the highest-inertia persona.

Persona: [name -- the one with the highest inertia score from the table]
Switching cost (quantified): [the specific measurable cost for this persona, from the table
  -- must be a concrete value, not a re-statement of the dimension name]
Kill barrier: [from KILL-BARRIER IDENTIFICATION -- the one adoption-blocking factor]
Scenario: [one sentence -- the specific moment where this persona encounters the kill barrier
  and decides not to adopt, even though the feature works correctly]
Adoption condition: [what single change -- to the feature, onboarding, migration tooling,
  pricing, or social proof mechanism -- would most reduce the kill barrier for this persona]

Write artifact to simulations/validate/inertia/{topic}-inertia-{date}.md.
Frontmatter: topic, date, feature, personas (list), persona_count, kill_barrier,
overall_risk, inertia_scores (map of persona name to Low/Medium/High/Critical).
```

---

## V-02: Hard phase gating (lifecycle emphasis axis)

**Axis:** Lifecycle emphasis — each phase has an explicit prerequisite check and a named
output that must be committed before proceeding; the kill-barrier phase sits between per-
persona scoring and the aggregate verdict, making it structurally impossible to produce an
overall risk without first nominating a single killer

**Hypothesis:** C-04 fails most often not because the prompt omits the kill-barrier
requirement but because it is embedded inside a list of outputs that can be produced in
any order or omitted when time pressure is felt. Placing kill-barrier identification as a
mandatory phase output — with an explicit "do not produce the aggregate verdict until this
is named" instruction — forces the model to commit to a single adoption killer before
synthesizing. The same gating logic applied to persona identification (C-01) prevents
generic persona lists that pass surface inspection.

```
You are running /validate:inertia for topic: {topic}.

Feature under adoption stress-test: {feature}

=== PHASE 1: PERSONA ROSTER ===

Before any inertia analysis: name the user personas.

List 2-4 personas who are plausible adopters of this feature. Each persona must have:
  (a) a name and brief role description
  (b) the specific outcome they currently achieve without this feature
  (c) the named workaround they use today to achieve that outcome

Prerequisite check: does every persona have a named current workaround?

If yes: proceed to Phase 2.
If no: complete the workaround field for every persona before proceeding. A persona entry
  without a current workaround is incomplete -- "they don't have one" is valid only if
  explained (e.g., "outcome is not achievable today").

=== PHASE 2: INERTIA FACTOR MAPPING ===

For each persona in Phase 1, assess the five inertia factors.

For each persona, address each dimension:
  1. Workaround satisfaction: How well does the current workaround meet the need? Rate:
     High (fully satisfies), Medium (partial), or Low (poor/unreliable). One sentence basis.
  2. Switching cost: The cost to migrate from the current workaround to this feature.
     Express as a concrete measurable value: time estimate, step count, effort rating (1-10),
     or relative cost ("3x the setup of current workflow"). Qualitative descriptions alone
     ("it's hard") do not qualify -- attach a number or relative measure.
  3. Habit lock-in: The behavioral pattern that creates resistance. Name the specific habit
     or integrated workflow behavior (e.g., "relies on existing file naming convention
     that 40+ scripts depend on").
  4. Social proof requirement: Does this persona need to see peer adoption before committing?
     Characterize as: needs peer proof / solo adopter / unclear. One sentence basis.
  5. Learning curve: Low / Medium / High. Name the specific knowledge delta required.

=== PHASE 3: PER-PERSONA INERTIA SCORES ===

For each persona, assign an inertia score and identify the primary driver.

Scale:
  Low: minimal resistance across dimensions; workaround is poor or low-satisfaction
  Medium: meaningful resistance; at least one high-friction dimension
  High: significant resistance; multiple high-friction dimensions or high workaround satisfaction
  Critical: adoption-blocking; this persona will not switch absent a structural change

Primary driver: the single factor from Phase 2 that most explains this persona's score.

List format:
  [Persona name]: [Score] -- primary driver: [dimension]

Every Phase 1 persona must have a score. A single shared score for all personas does not pass.

=== PHASE 4: KILL-BARRIER IDENTIFICATION ===

Do not produce the aggregate verdict until this phase is complete.

Review the Phase 2 mappings and Phase 3 scores. Identify exactly one adoption killer:
the single barrier that would block adoption even if all other inertia factors were reduced
to zero through product improvements or onboarding changes.

ADOPTION KILLER: [barrier name]
Affected persona(s): [name(s) from Phase 1]
Why it survives: [the structural property that makes this barrier persist after other
  friction is removed -- not "it's the highest-rated" but why specifically it cannot be
  addressed by the same moves that address other barriers]
Confidence: [High / Medium / Low -- how confident are you this is the single worst barrier
  vs. a candidate among equals]

If two barriers seem tied, argue for the one that is less addressable through a product
change and label it the killer. Do not name two.

=== PHASE 5: AGGREGATE VERDICT ===

Using the Phase 3 scores and Phase 4 kill barrier, produce the overall adoption inertia risk.

OVERALL RISK: [Low / Medium / High / Critical]
Score distribution: [brief characterization of how Phase 3 scores are distributed, e.g.,
  "2 High, 1 Medium, 1 Low"]
Rationale: [1 sentence -- explain why the overall risk is at the level you named, grounded
  in the score distribution and the kill barrier; do not re-list all scores]

=== PHASE 6: AMEND ===

Narrow the analysis to the persona with the highest Phase 3 inertia score.

Required fields:
  Persona: [name]
  Switching cost (quantified): [the measurable cost from Phase 2 for this persona -- must
    include a concrete unit; "high" alone does not pass]
  Kill barrier: [from Phase 4 -- must match the named adoption killer]
  Worst-case scenario: [one sentence -- the specific adoption decision moment where the kill
    barrier causes this persona to stay with their current workaround]
  Mitigation: [the one structural change -- feature, migration tool, pricing lever, or
    onboarding modification -- most likely to neutralize the kill barrier for this persona]

Write artifact to simulations/validate/inertia/{topic}-inertia-{date}.md.
Frontmatter: topic, date, feature, personas (list), persona_count, kill_barrier,
kill_barrier_confidence, overall_risk, inertia_scores (map of persona to score),
mitigation_proposed (true/false).
```

---

## V-03: Status-quo as named competitor (inertia framing axis)

**Axis:** Inertia framing — the existing workaround is introduced at the start as the
"current solution" competing for the same adoption slot; switching cost is framed as the
gap the user must cross to move away from a product they already use, not an abstract
friction metric

**Hypothesis:** C-02 (quantified switching cost) and C-06 (workaround satisfaction) fail
together when the prompt treats inertia as a diffuse psychological resistance rather than
as a specific competitive threat from a named tool or workflow. When the prompt names the
workaround as "the current solution that this feature must displace," it naturally prompts
product-comparison thinking: what would the user give up, what would they gain, and what
is the migration cost measured in concrete terms. This framing produces more specific
workaround satisfaction assessments (the current solution's strengths are the inertia) and
more grounded switching cost numbers (the gap between the two solutions, not abstract effort).

```
You are running /validate:inertia for topic: {topic}.

Feature under adoption stress-test: {feature}

Before this feature, users had a solution. That solution is the competition.

This skill treats inertia not as a psychological bias but as a concrete competitive threat:
the existing workaround that already solves the problem, has loyal users, and costs nothing
to keep using. Your job is to characterize that competition by persona and identify the one
reason users would choose to stay with it even if this feature works perfectly.

CURRENT SOLUTIONS INVENTORY

Name the workarounds or existing tools that each target persona already uses to achieve the
same outcome this feature addresses.

For each persona:
  Persona: [name and role]
  Current solution: [the specific tool, workflow, or workaround they use today]
  What the current solution does well: [1-2 sentences -- why users are satisfied with it,
    or if they aren't, what keeps them using it anyway]
  What it fails at: [the specific gap that this feature claims to close]

These must be concrete. "They use ad hoc methods" is not a current solution -- name what
they actually do.

SWITCHING COST ANALYSIS

For each persona, calculate the cost to cross from the current solution to this feature.

The switching cost is not effort in the abstract -- it is the sum of:
  (a) Migration cost: what they must do to move their existing work, data, or habits
  (b) Relearning cost: what they must unlearn and learn to use the new approach
  (c) Risk cost: what they risk losing if the transition fails or is incomplete

Express the switching cost for each persona as a quantified estimate:
  - Time: hours or days required to migrate + ramp
  - Steps: number of discrete actions needed to switch
  - Effort rating: 1-10 relative to other workflow changes this persona makes
  - Relative cost: "X times more setup than simply continuing to use [current solution]"

Qualitative descriptions alone do not count. Each persona needs at least one number,
range, or relative measure.

CURRENT SOLUTION STRENGTH SCORES

Rate how well each persona's current solution serves them today.

| Persona | Current solution | Satisfaction (H/M/L) | Reason satisfaction persists |
|---------|-----------------|---------------------|------------------------------|

Satisfaction scale:
  H = the current solution fully or near-fully meets the need; user has little motivation to switch
  M = partially meets the need; user is aware of gaps but has adapted to them
  L = the current solution is unreliable or painful; user actively wants an alternative

"Reason satisfaction persists": even for L-rated solutions, name why the user has not
already switched to something else (e.g., "switching requires re-training the team",
"no better alternative exists", "the pain is tolerable compared to migration risk").

HABIT AND SOCIAL DYNAMICS

For each persona, assess:
  Habit lock-in: What behavioral pattern or integrated workflow makes the current solution
    "sticky" beyond rational preference? Name the specific habit (e.g., "uses the tool's
    keyboard shortcuts 50+ times per day", "all team documentation references the current
    tool's output format").
  Social proof requirement: Is this persona's adoption decision individual or social?
    Does adoption require seeing peers or senior colleagues switch first? Name the social
    proof threshold if known (e.g., "needs 2+ teammates to adopt before committing",
    "will wait for team lead endorsement").

PER-PERSONA INERTIA SCORES

For each persona, assign an inertia score that reflects how competitive their current
solution is, given switching cost, satisfaction, habit, and social dynamics.

  Low = the current solution is weak; this persona would consider switching with minimal push
  Medium = the current solution has real strengths; switching requires meaningful incentive
  High = the current solution is strong; switching requires both incentive and reduced switching cost
  Critical = the current solution is entrenched; this persona will not switch absent a
    structural change (migration tool, mandated switch, pricing disruption)

For each: [Persona]: [Score] -- [one-sentence reason, referencing the current solution's
  specific strength]

KILL-BARRIER IDENTIFICATION

Across all personas and all inertia dimensions: what is the single reason users would
choose to keep their current solution even after this feature is polished and proven?

ADOPTION KILLER: [barrier name]
Which personas: [names]
Why the current solution wins on this dimension: [specific statement about what the current
  solution offers on this dimension that this feature cannot easily match or require users
  to give up]

OVERALL ADOPTION INERTIA RISK

OVERALL RISK: [Low / Medium / High / Critical]
Rationale: [1-2 sentences -- connects the competitive strength of current solutions, the
  per-persona score distribution, and the adoption killer]

AMEND

Focus on the persona most likely to keep their current solution.

Persona: [name -- highest inertia score]
Current solution: [the specific workaround this persona uses today]
Switching cost (quantified): [the measurable cost from SWITCHING COST ANALYSIS]
Kill barrier: [from KILL-BARRIER IDENTIFICATION]
Competitive framing: [one sentence -- the specific advantage the current solution holds
  over this feature that explains why the kill barrier survives product improvements]
Adoption unlock: [what would have to change -- in the feature, in pricing, in migration
  support, or in the current solution's viability -- for this persona to switch]

Write artifact to simulations/validate/inertia/{topic}-inertia-{date}.md.
Frontmatter: topic, date, feature, personas (list), persona_count,
workaround_satisfaction_assessed (true/false), kill_barrier, overall_risk,
inertia_scores (map of persona to score).
```

---

## V-04: Conversational walkthrough (phrasing register axis)

**Axis:** Phrasing register — descriptive and conversational; the prompt walks through each
persona as a narrative scenario ("walk through what this user's day looks like") rather than
issuing structured commands; the kill-barrier identification is framed as an argument the
model must make, not a field to fill

**Hypothesis:** C-04 (kill-barrier identification) and C-07 (habit lock-in + social proof)
fail structurally when prompts treat them as checklist items. The model fills the field with
the most salient answer rather than reasoning to the correct one. A conversational register
-- asking "what would this user's internal monologue be when they decide not to switch?" --
surfaces behavioral patterns (habit lock-in) and peer-adoption dynamics (social proof) as
part of the user story rather than as abstract dimensions to rate. The cost is reduced
structural rigidity; the gain is more candid, specific kill-barrier reasoning.

```
You are running /validate:inertia for topic: {topic}.

Feature under adoption stress-test: {feature}

Let's assume this feature ships in perfect working order. It does exactly what it claims.
Every bug is fixed. The UX is polished. Now walk through why the right users would still
not adopt it.

Start by deciding who you're thinking about. Name 2-4 users who would plausibly look at
this feature and consider adopting it. Don't use categories like "power users" or
"developers" -- give each one a name and a job, and tell me what they do today to accomplish
the same thing this feature would do for them.

For each persona, walk through their relationship with their current approach:

How happy are they with what they're already doing? Think about this concretely -- do they
complain about it? Is it good enough that switching would feel like unnecessary effort, or
is it painful enough that they'd welcome any improvement? Tell me what their current
solution does well from their perspective, even if it's objectively limited.

Now think through what it would actually take for them to switch. Not "effort" in the
abstract -- what would they literally have to do? Reconfigure something? Re-train their
hands to use different shortcuts? Convince their teammates to change their shared process?
Put a number on it where you can: how many hours, how many steps, how much risk of
disrupting their existing work. The goal is to make the switching cost feel real and
specific, not just "moderate" or "high."

For each persona, think about whether adoption is a solo decision or a social one. Some
people will try new tools independently the moment they seem good enough. Others will wait
until they see their colleagues using something before they'll risk the disruption. Which
is true here, and why? Does this persona need external validation or a team mandate before
committing? What would tip them over?

Think about what they'd lose if they switched -- not just switching cost, but habit. What
have they built up over time around their current approach that switching would require them
to abandon? Keyboard patterns, naming conventions, mental models, integrations with other
tools they rely on. The more specific you can be, the better.

After walking through each persona, step back and answer this: if you had to name the one
reason users would choose not to switch -- the factor that would survive even after the
switching cost is reduced, the learning curve is flattened, and early adopters demonstrate
it works -- what would it be?

Make this argument explicitly. Don't just list it; tell me why this factor is the one that
survives when everything else is addressed. Label it:

ADOPTION KILLER: [name the barrier]

Then give each persona an inertia score: Low, Medium, High, or Critical. Low means they'd
switch with minimal push. Critical means they're not switching absent a structural change
to their situation (migration tooling, pricing, team mandate, or the current solution
becoming unavailable). Tell me the score and the sentence that justifies it.

Finally, pull it together into an overall verdict for adoption risk:

OVERALL RISK: [Low / Medium / High / Critical]
Rationale: [one or two sentences -- what the per-persona picture adds up to, anchored in
  the adoption killer you named]

AMEND

Pick the one persona you're most worried about. The one who is most likely to look at this
feature, see that it works, and still stay with their current approach.

Tell me:
  - Who they are (persona name)
  - What switching to this feature would concretely cost them (a number or relative measure,
    not just "high effort")
  - What the single adoption killer is for them
  - The specific moment in their workday where they'd encounter that killer and decide not
    to switch
  - What one change -- to the feature, to the onboarding, to the migration path, or to
    the social or organizational context -- would most reduce that barrier

Write artifact to simulations/validate/inertia/{topic}-inertia-{date}.md.
Frontmatter: topic, date, feature, personas (list), persona_count, kill_barrier,
overall_risk, inertia_scores (map of persona to score), habit_lockup_assessed (true/false),
social_proof_assessed (true/false).
```

---

## V-05: Full rubric stack (combination)

**Axes:** Per-persona scoring table (V-01) + status-quo framing (V-03) + hard phase gating
(V-02) + mitigation path for the kill barrier (C-08)

**Hypothesis:** Each single-axis variation closes one failure mode: V-01 closes the
quantification gap (C-02, C-03), V-03 closes the workaround satisfaction gap (C-06),
V-02 closes the kill-barrier deferral gap (C-04, C-05), and adding C-08 explicitly makes
the mitigation a named output. The combination integrates all three axes without conflicts:
the status-quo competitor framing populates the table, the phase gates enforce commitment
to the kill barrier, and the mitigation appears in the AMEND section as a required field.
Expected output: all 5 essential criteria + all 3 recommended criteria.

```
You are running /validate:inertia for topic: {topic}.

Feature under adoption stress-test: {feature}

This feature has a competitor: whatever users do today. This skill maps that competition
by persona, scores each persona's resistance to switching, and identifies the single barrier
that would block adoption even after all other friction is reduced.

=== PHASE 1: CURRENT SOLUTIONS INVENTORY ===

Name 2-4 personas who are plausible adopters of this feature.

For each persona, answer the prerequisite before proceeding to analysis:
  (a) Persona name and brief role
  (b) The specific outcome they need (one sentence)
  (c) The named current solution they use to achieve that outcome -- the tool, workflow,
      script, or manual process that exists right now
  (d) What the current solution does well for this persona -- the genuine strengths that
      create satisfaction and resistance to change

Prerequisite gate: every persona must have a named current solution before proceeding. If
you cannot name one ("they have no workaround"), explain why the outcome is currently
unachievable and what that means for the inertia analysis.

=== PHASE 2: INERTIA FACTOR TABLE ===

Map every persona to the five inertia dimensions. Fill all cells. If a dimension does not
apply to a specific persona, write "N/A -- [reason]".

| Persona | Workaround satisfaction (H/M/L + basis) | Switching cost (quantified) | Habit lock-in | Social proof req. | Learning curve |
|---------|-----------------------------------------|----------------------------|---------------|-------------------|----------------|

Column definitions:

Workaround satisfaction: How well does the current solution serve this persona?
  H = fully or near-fully meets the need / M = partial / L = unreliable or painful
  Append a one-phrase basis: e.g., "H -- team's entire delivery pipeline depends on it"

Switching cost (quantified): Concrete migration cost to move from current solution to
  this feature. Required formats:
  - Time: "~4 hours to migrate existing configs + 1 day ramp"
  - Steps: "6-step reconfiguration process, 3 of which require manual verification"
  - Relative: "2x the setup time vs. renewing current tool license"
  - Effort rating: "8/10 -- comparable to last major toolchain migration"
  Qualitative descriptions alone ("significant effort") do not satisfy this column.

Habit lock-in: The specific behavioral pattern that makes the current solution sticky.
  Name the concrete habit, not the category. Example: "runs the same 3-command sequence
  from terminal memory 20+ times per day" rather than "uses keyboard shortcuts".

Social proof req.: Is adoption individual or social for this persona?
  Name the specific threshold: "needs 2+ teammates on the tool before committing",
  "will adopt solo if it reduces her reporting time by >30%", or "requires team lead
  mandate". Not just "Y" or "N".

Learning curve: Low / Medium / High + the specific knowledge gap.
  Example: "High -- must replace 5 years of familiarity with current query syntax".

=== PHASE 3: PER-PERSONA INERTIA SCORES ===

For each persona, assign an inertia score based on the Phase 2 table. All personas from
Phase 1 must be scored. A single shared score for multiple personas does not pass.

Score scale:
  Low: minimal resistance; current solution is weak; switching cost is low; workaround
    satisfaction is L
  Medium: meaningful resistance; at least one high-friction dimension from Phase 2
  High: significant resistance; multiple high-friction dimensions OR workaround satisfaction
    is H
  Critical: adoption-blocking; structural change required (migration tool, pricing, mandate,
    or current solution becoming unavailable)

For each persona:
  [Persona name]: [Score]
  Primary driver: [the single Phase 2 dimension most responsible for this score]
  Score rationale: [one sentence -- why this dimension dominates over the others]

=== PHASE 4: KILL-BARRIER IDENTIFICATION ===

Do not proceed to Phase 5 until this phase produces a single named adoption killer.

Review Phase 2 mappings and Phase 3 scores. Identify the one barrier that would survive
even if: switching cost were reduced by a migration tool, the learning curve were flattened
by better onboarding, and early adopters demonstrated success.

ADOPTION KILLER: [barrier name]
Affected persona(s): [names]
Why it survives: [the structural reason this barrier persists after the other friction is
  addressed -- what property makes it irreducible through typical product or onboarding
  improvements]
Severity: High / Critical [based on Phase 3 scores of affected personas]

Only one adoption killer. If two are plausible, argue for the one that is harder to
address without changing the feature's fundamental design.

=== PHASE 5: AGGREGATE VERDICT ===

OVERALL RISK: [Low / Medium / High / Critical]
Score distribution: [count of personas at each level, e.g., "1 Critical, 2 High, 1 Medium"]
Rationale: [1-2 sentences -- why the overall risk level is what it is, anchored in the
  Phase 3 distribution and the Phase 4 kill barrier; does not re-list every score]

=== PHASE 6: AMEND ===

Narrow the analysis to the highest-inertia persona and produce a focused adoption
challenge statement with a mitigation path.

Required fields:

  Persona: [name -- the one with the highest Phase 3 score]
  Current solution: [the specific tool or workflow this persona uses today]
  Switching cost (quantified): [the concrete value from Phase 2 for this persona -- must
    include a unit; "high" alone does not pass]
  Kill barrier: [must match the Phase 4 adoption killer exactly]
  Scenario: [one sentence -- the specific moment where this persona encounters the kill
    barrier and decides to stay with their current solution, even though the feature works]
  Mitigation: [one concrete intervention -- feature change, migration tool, pricing lever,
    onboarding redesign, or social proof mechanism -- that would most reduce the kill barrier
    for this persona; explain why this specific intervention addresses the structural reason
    named in Phase 4]

Write artifact to simulations/validate/inertia/{topic}-inertia-{date}.md.
Frontmatter: topic, date, feature, personas (list), persona_count,
workaround_satisfaction_assessed (true/false), habit_lockup_assessed (true/false),
social_proof_assessed (true/false), kill_barrier, kill_barrier_severity,
overall_risk, inertia_scores (map of persona to score), mitigation_proposed (true/false).
```
