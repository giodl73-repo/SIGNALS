# listen-feedback Skill — Round 12 Variations (V-01 through V-05)

---

## V-01 — Single Axis: Role Sequence

**Axis:** Role sequence — UX Read runs first, then C-01..C-12 in ascending NPS order, then PM Read closes.
**Hypothesis:** Surfacing UX friction before persona scoring seeds the output with interaction concerns that downstream persona cards are more likely to pick up and label specifically, reducing generic feedback and improving severity calibration across cards.

---

```
You are simulating customer reactions to a spec before it ships.

You will produce output in this exact role sequence:
1. UX Read — runs first, before any persona cards
2. Persona cards C-01 through C-12 — ordered by ascending predicted NPS (lowest first)
3. PM Read — runs last, after all persona evidence is in

---

## Spec Under Review

{{spec}}

---

## Step 1 — UX Read

Produce a UX Read from the lens of a UX practitioner who has read the spec end to end.

Coverage (2+ sentences):
- Clarity of the user interaction model
- Onboarding friction and first-run experience
- Task completion paths and edge states
- Visual/interaction consistency with existing conventions

List at most 3 UX concerns, each with an explicit severity label:
blocking | major | minor | cosmetic

---

## Step 2 — Persona Cards

The 12 customer personas are C-01 through C-12. Each persona has a name, role, and 
behavioral profile that shapes how they evaluate software decisions.

Produce one card per persona. After completing all 12 cards, sort them in ascending NPS 
order (lowest NPS score first, highest last). Break ties by persona ID.

Each card must use this exact field sequence — no reordering:

---
### [C-XX] [Name] — [Role]

**Current approach:** What this persona does today, without this spec. Required field.
If no equivalent workflow exists, state that explicitly.

**Gains from this spec:** What this persona specifically gains by adopting the spec.
Ground gains in the persona's role and current context, not generic spec features.

**Losses and switching costs:** What this persona loses or must absorb: migration burden,
learning curve, workflow disruption, re-training cost, opportunity cost.
For Promoter-tier personas (NPS 9–10) where friction is genuinely negligible, write:
"No significant losses identified — [one sentence explaining why friction is minimal]."

**NPS:** [1–10]

**Band:** Detractor (1–6) | Passive (7–8) | Promoter (9–10)

**NPS justification:** One or more sentences connecting this persona's context to the
score. Must reference what this persona gains or loses relative to their current approach.
Feature description alone does not satisfy this field.

**Feedback:**
(Order: blocking first, then major, then minor, then cosmetic)
- [BLOCKING] Item text
- [major] Item text
- [minor] Item text
- [cosmetic] Item text

If this persona has no objections, state: "No objections identified."

**Revision recommendation:** Name the specific spec element that, if changed, would
improve this persona's NPS. Generic advice ("improve documentation") does not satisfy
this field — the recommendation must reference a named section, feature, or behavior
in the spec.
---

---

## Step 3 — PM Read

After all 12 persona cards, write a PM Read (2+ sentences) that synthesizes:
- The dominant cross-persona risk pattern
- Which personas represent the highest business priority to satisfy
- One prioritized revision action the PM would queue first

---

## Step 4 — Aggregate NPS Section

Compute the aggregate NPS: sum of all 12 persona scores divided by 12. Round to one
decimal place.

Output these labeled fields:

**Aggregate NPS:** [X.X]
**Threshold (7.0):** MET | NOT MET
(If NOT MET, flag: "Spec requires revision before ship.")

**Band distribution:**
- Promoters (9–10): [count]
- Passives (7–8): [count]
- Detractors (1–6): [count]

**Dominant Detractor objection:** The single feedback theme most frequently cited by
Detractor-tier (score 1–6) personas. Format: "[Theme name] — cited by X of Y Detractors."

**Sensitivity analysis:** Identify the 2–3 personas whose scores contribute most to
moving the aggregate mean. For each persona, state: "If [C-XX]'s score shifted from
[current] to [±2 adjusted], aggregate mean moves from [X.X] to [Y.Y]."
Use contribution-delta framing. Do not frame as proximity to the 7.0 threshold.

**Blocker escalation:**
List every blocking-severity item from all 12 cards. Include the persona ID next to each.
If no blocking items exist, state: "No blocking issues identified."

---

## Step 5 — Cross-Persona Theme Matrix

Produce a table with these columns:

| Theme | Personas | Highest Severity | Severity Distribution | Blocking Count |
|-------|----------|------------------|-----------------------|----------------|

- Theme: name of the recurring feedback pattern
- Personas: IDs of all personas who raised this theme
- Highest Severity: the worst severity level assigned to this theme across all cards
- Severity Distribution: per-level counts, e.g. "1 blocking, 3 major, 2 minor"
- Blocking Count: integer; 0 if no blocking items under this theme

The cross-persona theme matrix is the final substantive section of the output.
No new analytical content appears after the theme matrix.
```

---

## V-02 — Single Axis: Inertia Framing

**Axis:** Inertia framing — the status-quo competitor is the dominant evaluation anchor. Every persona assesses the spec as a change-from rather than a feature-to.
**Hypothesis:** Foregrounding the current-behavior baseline before spec features forces bilateral gain/loss analysis by construction, producing higher-quality NPS justifications and more precise switching cost estimates.

---

```
You are simulating how 12 customer personas and 2 professional roles evaluate a proposed
spec — measured against what they do today.

The evaluation frame is behavioral economics, not feature comparison. Every persona begins
by describing their current behavior (the inertia baseline). The spec is then evaluated as
a departure from that baseline: what do they gain, what do they lose, and is the trade
worth making?

---

## Spec Under Review

{{spec}}

---

## Evaluation Protocol

For each persona, the analysis runs in this order:

**Phase 1 — Inertia Baseline**
Before evaluating the spec at all: what does this persona do today? What tools, workflows,
or manual steps constitute their current approach? This is the competitor the spec must
displace.

**Phase 2 — Bilateral Impact**
Given the inertia baseline:
- What does this persona gain by switching to the spec?
- What does this persona lose or sacrifice (switching cost, migration, retraining,
  disruption, opportunity cost)?

**Phase 3 — Verdict**
Given the bilateral evidence from Phase 2, what NPS does this persona give (1–10)?
The score must follow the evidence — gains/losses must be stated before the NPS.

**Phase 4 — Specific Feedback**
What specific changes to the spec would reduce the loss side or amplify the gain side?
Feedback items carry explicit severity: blocking | major | minor | cosmetic.

---

## Persona Cards — C-01 through C-12

Produce one card per persona. Present cards in ascending NPS order (lowest first).
Each card must follow this exact field sequence:

---
### [C-XX] [Name] — [Role]

**Current approach:** [Phase 1 — inertia baseline for this persona. Required. If no
prior workflow exists, state that and explain what behavioral inertia they carry instead
(e.g., "does not currently do this; inertia is toward not doing it at all").]

**Gains from this spec:** [Phase 2a — what this persona specifically gains by departing
from their current approach. Ground gains in the baseline named above, not in generic
spec benefits.]

**Losses and switching costs:** [Phase 2b — what this persona loses or absorbs.
Name the loss concretely: migration burden, learning curve, workflow disruption, tool
switching overhead, retraining cost, productivity dip during transition.
For Promoter-tier personas (NPS 9–10) where no meaningful friction exists, state:
"No significant losses identified — [one sentence of reasoning]."]

**NPS:** [1–10, derived from the bilateral evidence above]

**Band:** Detractor (1–6) | Passive (7–8) | Promoter (9–10)

**NPS justification:** [One or more sentences. Must connect the bilateral evidence
(gains vs. losses) to the score. A justification that only describes spec features,
without referencing the current approach as a comparison point, does not satisfy
this field.]

**Feedback:**
(Severity order: blocking first, major, minor, cosmetic)
- [BLOCKING] Item text
- [major] Item text
- [minor] Item text
- [cosmetic] Item text

Minimum one item, or state "No objections identified."

**Revision recommendation:** Name the specific spec element that, if changed, would
reduce losses or amplify gains for this persona. Reference a named section, feature,
or behavior in the spec — not a generic improvement directive.
---

---

## Professional Reads

### UX Read

(After all 12 persona cards)

Write a UX Read (2+ sentences) that assesses the spec from a practitioner lens.
Focus on interaction model clarity, onboarding friction relative to current tools,
task completion paths, and consistency with existing patterns.
List UX concerns with severity labels: blocking | major | minor | cosmetic.

### PM Read

(After UX Read)

Write a PM Read (2+ sentences) that assesses cross-persona adoption risk, names the
highest-priority inertia barrier, and identifies the one spec change most likely to
shift the aggregate NPS above threshold.

---

## Aggregate NPS Section

Compute aggregate NPS: sum of 12 persona scores divided by 12, rounded to one decimal.

**Aggregate NPS:** [X.X]
**Threshold (7.0):** MET | NOT MET
(NOT MET = flag spec for revision)

**Band distribution:**
- Promoters (9–10): [count]
- Passives (7–8): [count]
- Detractors (1–6): [count]

**Dominant Detractor objection:** Single most common blocking/major theme among
Detractor-tier personas. Format: "[Theme] — cited by X of Y Detractors."

**Sensitivity analysis:** Identify 2–3 personas whose scores most influence the mean.
For each: "Removing [C-XX] (NPS [N]) shifts aggregate from [X.X] to [Y.Y]."
Frame as contribution delta, not threshold proximity.

**Blocker escalation:** All [BLOCKING] items from all cards, with persona IDs.
If none: "No blocking issues identified."

---

## Cross-Persona Theme Matrix

| Theme | Personas | Highest Severity | Severity Distribution | Blocking Count |
|-------|----------|------------------|-----------------------|----------------|

Annotate each theme with per-severity counts, not just the highest severity.

The theme matrix is the last substantive section. No analytical content follows it.
```

---

## V-03 — Single Axis: Phrasing Register

**Axis:** Phrasing register — conversational and persona-voiced. The prompt addresses the model in second person for each persona and uses plain English throughout.
**Hypothesis:** Persona-voiced framing ("Step into C-07's shoes — what do you do today?") activates more authentic-sounding internal monologue in the output, reducing template-feel and producing more specific, role-grounded feedback.

---

```
You're going to read a spec and tell us how 12 different customers would react to it.

For each customer, you'll think through what they do today, what they'd gain or lose if
this spec shipped, and what NPS score (1–10) they'd give it. Then you'll write their
honest feedback — with every item tagged by how serious it is.

After the customers, two professional roles — UX and PM — add their perspective.

Then you'll tally the scores and surface the patterns.

---

Here's the spec:

{{spec}}

---

## The 12 Customer Personas

Work through each customer one at a time. For each one, step into their shoes and think
through the four phases before writing anything:

1. What does this person do today, before this spec exists?
2. What do they gain if they adopt it?
3. What do they lose or have to deal with (migration, learning curve, disruption)?
4. Given that picture — what NPS do they give it?

Write the gains and losses before you write the NPS. The score should come out of the
evidence, not the other way around.

**Use this field order for every card — no exceptions:**

---
### [C-XX] [Name] — [Job Title or Role]

**Current approach:** What does this person do today without this spec? Be specific
to their role. If they have no existing workflow, say so.

**Gains from this spec:** What would genuinely improve for this person if the spec
shipped? Ground this in their current approach — don't just list features.

**Losses and switching costs:** What would this person have to give up, unlearn, or
absorb? Think: time, disruption, retraining, migration burden, loss of familiar patterns.
If this person is clearly a Promoter (NPS 9–10) and the friction really is negligible,
say "No significant losses — [why]."

**NPS:** [1–10]

**Band:** Detractor (1–6) | Passive (7–8) | Promoter (9–10)

**NPS justification:** Why did they land on that number? Connect the gains and losses
above to the score. If the justification doesn't reference their current situation,
rewrite it.

**Feedback:** What specifically would they want changed? Tag every item:
(Put the most serious items first)
- [BLOCKING] Must-fix before they'd use it
- [major] Important but not a dealbreaker
- [minor] Nice to have
- [cosmetic] Small polish item

If they have no complaints: "No objections identified."

**Revision recommendation:** What one specific thing in the spec, if changed, would
move their NPS up? Name the actual spec element — not a general direction like
"make it simpler."
---

After all 12 cards, re-sort them from lowest NPS to highest. If two personas tie,
put the lower-numbered one first.

---

## UX Read

Now step back and read the spec through a UX practitioner's eyes.

What works? What doesn't? Where's the interaction model unclear? Where does onboarding
feel steep? How does it compare to what users probably already know?

Write 2+ sentences of synthesis, then list your top concerns — max 3 — each tagged
blocking | major | minor | cosmetic.

The UX Read goes before the PM Read.

---

## PM Read

Step into the PM chair. You've seen the UX read and all 12 customer reactions.

Write 2+ sentences: What's the adoption risk? Who's the hardest persona to win over and
why? What's the one thing you'd fix first?

---

## The Numbers

Add up the 12 NPS scores and divide by 12. Round to one decimal.

**Aggregate NPS:** [X.X]
**Threshold check:** 7.0 — did we hit it? MET | NOT MET
(If NOT MET: spec needs revision before ship.)

**Who's who:**
- Promoters (9–10): [count]
- Passives (7–8): [count]
- Detractors (1–6): [count]

**Dominant Detractor objection:** What's the one complaint that keeps coming up among
the Detractors? "[Theme] — X of Y Detractors raised this."

**Most influential scores:** Pick 2–3 personas who are really moving the mean.
For each: "If [C-XX]'s score went from [N] to [N±2], the aggregate would shift from
[X.X] to [Y.Y]." Don't say "they're near the threshold" — say how much they actually
pull the number.

**Blockers:** Every [BLOCKING] item from all the cards, with persona IDs.
If there are none: "No blocking issues identified."

---

## Theme Map

Make a table of the patterns that came up across multiple cards:

| Theme | Personas | Worst Severity | Per-Severity Counts | Blocking Count |
|-------|----------|----------------|---------------------|----------------|

This table is the last thing in the output. Nothing analytical after it.
```

---

## V-04 — Combined Axes: Output Format + Role Sequence

**Axes:** Output format (schema-first, table-heavy, machine-parseable structure) + Role sequence (UX → ascending-NPS personas → PM).
**Hypothesis:** Providing an explicit field schema as a reference table at the top of the prompt, before any instructions, reduces format drift across 14 roles and produces output that can be parsed programmatically without cleanup. Role sequence (UX first) ensures UX-derived concerns are seeded early.

---

```
You are producing a structured customer-reaction report for a spec under review.

## Card Schema Reference

Before any instructions, the canonical card schema is defined here. Every persona card
in this output must conform exactly to this schema — fields in this order, no additions
or reorderings:

| # | Field Label | Required | Notes |
|---|-------------|----------|-------|
| 1 | `**Current approach:**` | Always | Inertia baseline; state "none" explicitly if applicable |
| 2 | `**Gains from this spec:**` | Always | Specific to this persona's context |
| 3 | `**Losses and switching costs:**` | Always | Promoter exception: state "No significant losses — [reason]" |
| 4 | `**NPS:**` | Always | Integer 1–10; derived from fields 2 and 3 |
| 5 | `**Band:**` | Always | Detractor (1–6) / Passive (7–8) / Promoter (9–10) |
| 6 | `**NPS justification:**` | Always | References current approach; not feature description |
| 7 | `**Feedback:**` | Always | Severity-ordered; min 1 item or "No objections identified" |
| 8 | `**Revision recommendation:**` | Always | Named spec element; no generic advice |

Fields 2 and 3 (Gains / Losses) must appear in document order before field 4 (NPS).
This is the pre-commitment constraint: evidence precedes verdict.

---

## Spec Under Review

{{spec}}

---

## Execution Sequence

Run the following sections in this order:

### Section 1 — UX Read

Role: UX practitioner reviewing the spec for interaction model quality.

Output format:

**UX Read**

[2+ sentence synthesis covering: interaction model clarity, onboarding friction, task
completion paths, consistency with existing conventions]

| # | Concern | Severity |
|---|---------|----------|
| 1 | [text]  | blocking / major / minor / cosmetic |
| 2 | [text]  | ... |
| 3 | [text]  | ... |

Maximum 3 concerns. If fewer concerns exist, reduce the table accordingly.

---

### Section 2 — Persona Cards C-01 through C-12

Produce one card per persona using the schema defined above.

Card header format:
### [C-XX] [Name] — [Role]

After producing all 12 cards, re-order them in ascending NPS sequence
(lowest NPS first, highest last; ties broken by persona ID ascending).

Severity ordering within the Feedback field:
blocking → major → minor → cosmetic (no lower-severity item precedes a higher-severity item)

Inline marker for blocking items: prefix the item with `[BLOCKING]`

---

### Section 3 — PM Read

Role: PM synthesizing all evidence produced in Sections 1 and 2.

Output format:

**PM Read**

[2+ sentence synthesis covering: dominant adoption risk, highest-priority persona to
satisfy, one prioritized revision action]

---

### Section 4 — Aggregate NPS

Compute: (sum of 12 NPS scores) / 12, rounded to one decimal place.

**Aggregate NPS:** [X.X]

**Threshold (7.0):** MET | NOT MET
_(NOT MET: append "Spec requires revision before ship.")_

**Band distribution table:**

| Band | Range | Count |
|------|-------|-------|
| Promoter | 9–10 | [N] |
| Passive | 7–8 | [N] |
| Detractor | 1–6 | [N] |

**Dominant Detractor objection:** [Theme name] — cited by [X] of [Y] Detectors.

**Sensitivity analysis table:**

| Persona | Current NPS | Adjusted NPS | Aggregate Before | Aggregate After | Delta |
|---------|-------------|--------------|-----------------|-----------------|-------|
| C-XX    | N           | N±2          | X.X             | Y.Y             | ±Z.Z  |

Include 2–3 rows. Select the personas whose adjustment produces the largest absolute
delta in aggregate mean. Do not frame proximity to 7.0 threshold as the selection
criterion.

**Blocker escalation table:**

| Persona | Blocking Item |
|---------|---------------|
| C-XX    | [text]        |

If no blocking items: single row: | — | No blocking issues identified. |

---

### Section 5 — Cross-Persona Theme Matrix

This is the final substantive section. No analytical content appears after it.

| Theme | Personas | Highest Severity | Severity Distribution | Blocking Count |
|-------|----------|------------------|-----------------------|----------------|
| [name] | C-XX, C-YY | blocking | 1 blocking, 2 major, 1 minor | 1 |

Column definitions:
- Theme: recurring feedback pattern name (2–5 words)
- Personas: comma-separated IDs of all personas who raised this theme
- Highest Severity: worst severity level across all instances
- Severity Distribution: per-level count string, e.g. "0 blocking, 3 major, 2 minor, 1 cosmetic"
- Blocking Count: integer count of blocking-severity instances under this theme
```

---

## V-05 — Combined Axes: Phrasing Register + Inertia Framing

**Axes:** Phrasing register (formal/technical with precise contract language) + Inertia framing (status-quo-first: spec evaluated as disruption to a named behavioral baseline, not as a feature list).
**Hypothesis:** The combination of formal register (which enforces field discipline) with inertia-first framing (which anchors every score to a named before-state) produces the most rigorous bilateral analysis and the most defensible NPS justifications, at the cost of reading less conversationally.

---

```
You are executing a pre-ship customer-reaction simulation. The evaluation frame is
behavioral displacement: each persona holds an existing behavioral equilibrium, and the
spec is evaluated as a perturbation to that equilibrium. NPS scores measure whether the
displaced equilibrium is better or worse than the prior one, weighted by the magnitude
of displacement.

---

## Input

{{spec}}

---

## Evaluation Frame: Behavioral Displacement Model

For each persona, the simulation proceeds in four phases:

**Phase 1 — Equilibrium State (Current Approach)**
Identify the persona's current behavioral equilibrium: what tools, habits, processes,
or absence-of-processes constitute their status quo? This is the baseline against which
all gains and losses are measured. The equilibrium state is required for every persona;
if no equivalent workflow exists, the equilibrium state is "no behavior" — which carries
its own inertia (the inertia of not starting).

**Phase 2 — Displacement Analysis**
Given the equilibrium state, analyze the perturbation introduced by the spec:

*Gain vector:* What does this persona receive as a result of displacement?
Gains must be grounded in the equilibrium state — they represent improvements relative
to the current approach, not abstract feature benefits.

*Loss vector:* What does this persona sacrifice or absorb as a cost of displacement?
Losses include: migration burden, retraining time, workflow disruption, tooling
transition, productivity degradation during ramp, opportunity cost of switching effort.
For Promoter-tier outcomes (NPS 9–10) where displacement cost is genuinely negligible,
state: "No significant displacement cost identified — [one sentence of reasoning
grounded in the equilibrium state]."

**Phase 3 — NPS Derivation**
Derive the NPS (1–10) from the displacement analysis. The NPS field must appear after
the gain vector and loss vector in document order. A score that precedes its bilateral
evidence is structurally invalid.

**Phase 4 — Targeted Feedback**
Identify specific friction points in the spec that generate loss-vector components or
suppress gain-vector components. Each item carries an explicit severity classification:
blocking | major | minor | cosmetic. Items are ordered by descending severity within
the card.

---

## Card Structure

Each persona card must conform to this field sequence exactly:

---
### [C-XX] [Persona Name] — [Role Descriptor]

**Current approach:** [Phase 1 output — equilibrium state description]

**Gains from this spec:** [Phase 2, gain vector — grounded in equilibrium state]

**Losses and switching costs:** [Phase 2, loss vector — named displacement costs;
Promoter exception stated with reasoning if applicable]

**NPS:** [1–10]

**Band:** Detractor (1–6) | Passive (7–8) | Promoter (9–10)

**NPS justification:** [Phase 3 derivation — connects bilateral displacement analysis
to the score. Must reference the equilibrium state explicitly. Feature description
without equilibrium comparison does not satisfy this field.]

**Feedback:**
[Phase 4 — severity-descending order: blocking first, then major, minor, cosmetic]
- [BLOCKING] [item]
- [major] [item]
- [minor] [item]
- [cosmetic] [item]
[Minimum one item; or state "No objections identified."]

**Revision recommendation:** [Specific named spec element whose modification would
alter the loss vector or amplify the gain vector for this persona. Generic improvement
directives do not satisfy this field.]
---

---

## Execution Order

1. Produce all 12 persona cards (C-01 through C-12).
2. After producing all cards, sort them in ascending NPS order (lowest NPS first,
   highest last; ties resolved by ascending persona ID).
3. Append the UX Read.
4. Append the PM Read.
5. Append the Aggregate NPS section.
6. Append the Cross-Persona Theme Matrix (final section).

---

## UX Read

Following all 12 sorted persona cards, produce a UX Read.

Frame: The UX practitioner assesses whether the spec's interaction model produces
acceptable displacement cost for the median user, and whether onboarding scaffolding
is sufficient to bridge the equilibrium gap.

Content requirements (2+ sentences minimum):
- Interaction model legibility relative to likely prior-state mental models
- Onboarding friction: does the spec accommodate the transition from current approach?
- Task completion path coverage: are primary flows complete?
- Consistency with established interaction conventions

Feedback items (maximum 3): each severity-labeled blocking | major | minor | cosmetic.

The UX Read precedes the PM Read.

---

## PM Read

Following the UX Read, produce a PM Read (2+ sentences).

Frame: The PM synthesizes the displacement analysis across all 12 personas and two
professional reads. The PM is accountable for adoption risk and ship decision.

Required content:
- Dominant adoption barrier (the loss-vector component cited most frequently)
- Highest-priority persona cohort to address
- One revision action that would most improve aggregate NPS, with reasoning

---

## Aggregate NPS Section

Computation: arithmetic mean of all 12 persona NPS scores, rounded to one decimal place.

**Aggregate NPS:** [X.X]
**Threshold (7.0):** MET | NOT MET
(NOT MET: "Spec requires revision — aggregate NPS [X.X] is below the 7.0 ship threshold.")

**Band distribution:**
- Promoters (9–10): [N]
- Passives (7–8): [N]
- Detractors (1–6): [N]

**Dominant Detractor objection:** The single loss-vector component or friction theme
most frequently cited by Detractor-tier personas (NPS 1–6). Required format:
"[Theme] — cited by [X] of [Y] Detractors."

**Sensitivity analysis:** Identify the 2–3 personas whose NPS values produce the
greatest aggregate mean delta when varied. For each:
"If [C-XX]'s NPS shifted from [current] to [current ± 2], aggregate mean would move
from [X.X] to [Y.Y] (delta: [±Z.Z])."
Frame as contribution delta. Threshold-proximity framing (e.g., "this persona is just
below 7.0") does not satisfy this requirement.

**Blocker escalation:** All [BLOCKING]-classified items across all 12 persona cards,
attributed by persona ID. If none: "No blocking items identified."

---

## Cross-Persona Theme Matrix

This section is the final substantive section of the output. No analytical content
appears after the theme matrix.

| Theme | Personas | Highest Severity | Severity Distribution | Blocking Count |
|-------|----------|------------------|-----------------------|----------------|

Column specifications:
- **Theme:** Recurring pattern name derived from feedback items (3–6 words preferred)
- **Personas:** All persona IDs whose feedback contributed to this theme
- **Highest Severity:** Maximum severity level observed for this theme
- **Severity Distribution:** Per-tier count string, e.g. "1 blocking, 3 major, 2 minor, 0 cosmetic"
- **Blocking Count:** Integer count of [BLOCKING] items classified under this theme

A theme requires at least 2 persona citations to qualify for inclusion in the matrix.
Single-persona concerns appear only in the individual persona card, not in the matrix.
```

---

## Variation Summary

| Variation | Primary Axis | Secondary Axis | Key Structural Bet |
|-----------|-------------|----------------|-------------------|
| V-01 | Role sequence | — | UX seeds feedback vocabulary before persona scoring |
| V-02 | Inertia framing | — | Status-quo-first frame forces bilateral analysis |
| V-03 | Phrasing register | — | Persona-voice prompt produces more authentic reactions |
| V-04 | Output format | Role sequence | Schema-first + table-heavy reduces format drift |
| V-05 | Phrasing register | Inertia framing | Formal + displacement model produces most rigorous bilateral coverage |

All five variations enforce A-19 pre-commitment ordering: `Gains` → `Losses` → `NPS` → `Band` → `NPS justification` is the mandatory card field sequence in every variation.
