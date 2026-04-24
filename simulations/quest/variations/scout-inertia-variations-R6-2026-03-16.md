# scout-inertia — V-01 through V-05 (R6)

---

## V-01 — Variation Axis: Role Sequence
**Hypothesis**: Declaring all actors before any analysis forces role-level precision throughout; every cost, failure mode, and defeat condition automatically inherits a named owner rather than drifting to department labels.

```
You are running /scout:inertia for the topic: {{topic}}.

Inertia is the strongest competitor any feature faces. Your job is to analyze the
"do nothing" option in full — the specific workaround currently in use, what it
costs to keep it, where it breaks, and the exact conditions under which it loses.

────────────────────────────────────────────
STEP 1 — ROLE REGISTRY
────────────────────────────────────────────

Before any analysis, identify and declare the actors. Use role-level labels only
("the data analyst", "the PM", "the DevOps engineer" — never "the team" or
"users" or a department name).

Declare three roles:

  PERFORMER — the role that executes the workaround today
  DECISION-MAKER — the role that owns the build-vs-continue decision
  AFFECTED PARTY — the role that bears the downstream cost of the workaround

Every subsequent section must reference actors from this registry by their declared
role label. If an actor appears that was not declared here, add them to the registry
before using them.

────────────────────────────────────────────
STEP 2 — WORKAROUND MAP
────────────────────────────────────────────

Name the specific workaround in use today. "A manual process" does not pass. Provide
the exact mechanism: what is exported, where it goes, what tool is used, how often it
runs, and who (from your Role Registry) performs each step.

Then state the ongoing cost with a unit:
  "[PERFORMER] spends [N] [time unit] per [frequency] doing [specific action]."

────────────────────────────────────────────
STEP 3 — SWITCHING COST ANALYSIS
────────────────────────────────────────────

Quantify at least two categories of switching cost. Every cost must carry a unit.
At least one cost must be tied to a specific role from your registry.

Required categories:
  • Migration effort — hours or dollars, tied to PERFORMER or DECISION-MAKER
  • At least one of: training overhead, process disruption, or in-flight work at risk

Format each cost as:
  "[Cost category]: [role] spends/risks [N] [unit] because [specific reason]."

"Significant" without a number or unit fails this section.

────────────────────────────────────────────
STEP 4 — WORKAROUND FAILURE MODES
────────────────────────────────────────────

Identify at least two specific scenarios where the workaround breaks, produces
errors, causes rework, or cannot scale. Name the role from your registry who
experiences each failure.

Generic pain ("manual is slow") does not pass. Concrete observable failure
("CSV export silently truncates rows over 65,536 — no error, PERFORMER discovers
on downstream audit two days later") passes.

Format each failure mode as:
  FM-[N]: [Specific scenario]. Experienced by: [role from registry].
          Observable signal: [what the role sees when it happens].

────────────────────────────────────────────
STEP 5 — DEFEAT CONDITIONS
────────────────────────────────────────────

Identify at least two specific, falsifiable conditions under which teams abandon
the workaround. Each condition must:
  • Name a specific team type (not "users")
  • Be testable — an observer can confirm whether the condition has been met
  • Reference or connect to a failure mode from Step 4

"Teams switch when they see the value" fails. "Engineering teams switch when
FM-1 occurs more than once in a sprint and the re-work cost exceeds [N] hours"
passes.

Format each defeat condition as:
  DC-[N]: [Team type] switches when [falsifiable condition].
          Connected failure mode: FM-[N].

────────────────────────────────────────────
STEP 6 — INERTIA THREAT SCORE
────────────────────────────────────────────

Declare the inertia threat score: HIGH, MEDIUM, or LOW.

The default is HIGH. Any deviation from HIGH must be justified with a specific,
quantified condition drawn from the analysis above. An output that lists switching
costs and failure modes without aggregating them into a threat level is incomplete.

Format:
  Inertia Threat Score: [HIGH / MEDIUM / LOW]
  Justification: [one sentence drawn from the analysis, or "default HIGH applies"]
```

---

## V-02 — Variation Axis: Output Format (Tables + Numbered Inventory)
**Hypothesis**: Enforcing tabular output with required column schemas makes missing cells structurally visible — an unanswered unit or a missing role label creates a blank cell the author cannot hide in prose.

```
You are running /scout:inertia for the topic: {{topic}}.

Produce the analysis in the structured format below. Every table must be complete.
A blank cell is a failed criterion, not an acceptable gap. Do not add prose sections
outside the specified structure.

────────────────────────────────────────────
TABLE 1 — WORKAROUND PROFILE
────────────────────────────────────────────

| Field               | Value |
|---------------------|-------|
| Workaround name     | [exact mechanism, not "manual process"] |
| Performer role      | [role label, not department] |
| Frequency           | [how often it runs] |
| Ongoing cost        | [N] [unit] per [frequency] |
| Cost bearer (role)  | [role from performer or downstream] |

If any cell in this table is "N/A" or blank, the workaround has not been
sufficiently specified. Stop and research before proceeding.

────────────────────────────────────────────
TABLE 2 — FAILURE MODE INVENTORY
────────────────────────────────────────────

Number each failure mode. These numbers are referenced in Tables 3 and 4.
"Manual is slow" does not qualify — failure modes must be observable, specific,
and produce an error, silent corruption, rework, or a scale ceiling.

| FM# | Scenario | Trigger condition | Consequence | Role who experiences it |
|-----|----------|-------------------|-------------|-------------------------|
| FM-01 | | | | |
| FM-02 | | | | |
| FM-03 (optional) | | | | |

────────────────────────────────────────────
TABLE 3 — SWITCHING COST BREAKDOWN
────────────────────────────────────────────

At least two rows required. Every row must have a unit. At least one row must
name a specific role.

| Cost category | Description | Unit | Magnitude | Role |
|---------------|-------------|------|-----------|------|
| Migration effort | | hours or $ | | [role] |
| [training / disruption / in-flight risk] | | | | |

────────────────────────────────────────────
TABLE 4 — DEFEAT CONDITIONS
────────────────────────────────────────────

At least two rows required. Each condition must be falsifiable and reference at
least one FM from Table 2. "Teams switch when they see value" fails the
falsifiable test.

| DC# | Team type | Defeat condition (falsifiable) | Connected FM# |
|-----|-----------|-------------------------------|---------------|
| DC-01 | [specific team type] | | |
| DC-02 | [specific team type] | | |

────────────────────────────────────────────
THREAT SCORE DECLARATION
────────────────────────────────────────────

State one line:

  Inertia Threat Score: [HIGH / MEDIUM / LOW]

Then one sentence of justification. Default is HIGH. If you declare MEDIUM or LOW,
you must cite a specific quantified condition from the tables above that justifies
the downgrade. Listing costs without aggregating into a score is an incomplete
analysis.

────────────────────────────────────────────
COMPLETENESS CHECK (self-verify before submitting)
────────────────────────────────────────────

Before finalizing, confirm:
  [ ] Table 1: all cells filled, cost has a unit, performer is a role label
  [ ] Table 2: ≥2 FMs, each with a specific observable scenario and a named role
  [ ] Table 3: ≥2 costs with units, ≥1 tied to a role
  [ ] Table 4: ≥2 conditions, each falsifiable, each referencing an FM number
  [ ] Threat score declared with justification

Any unchecked box = incomplete output.
```

---

## V-03 — Variation Axis: Inertia Framing (Personified Competitor)
**Hypothesis**: Treating "Inertia" as a named competitor with a full competitor profile — strengths, vulnerabilities, defeat conditions — recruits the author's competitive analysis instincts and produces sharper falsifiable triggers than neutral cost-listing prompts.

```
You are running /scout:inertia for the topic: {{topic}}.

In this analysis, Inertia is your primary competitor. Not a legacy tool. Not
a market incumbent. Inertia is the option to keep doing what the team already
does. It has an existing user base (everyone currently using the workaround),
a proven track record (it works well enough), low switching cost to maintain,
and a powerful sales pitch: "we don't have to change anything."

Your job is to profile Inertia as you would any serious competitor — and then
find its vulnerabilities.

────────────────────────────────────────────
SECTION 1 — INERTIA'S PRODUCT
────────────────────────────────────────────

Describe Inertia's current offering: the specific workaround in use. Name it
precisely — the tool, the export mechanism, the shared location, the manual step.
"A manual process" is not a product description.

Then identify the role that "buys" Inertia every week by performing the workaround,
and state what they pay for it:
  "[Role] pays [N] [unit] per [frequency] to keep using Inertia."

────────────────────────────────────────────
SECTION 2 — INERTIA'S COMPETITIVE STRENGTHS
────────────────────────────────────────────

Inertia's strengths are your feature's switching costs. List at least two.
Every strength must carry a unit — "Inertia is sticky" without a number is
not a competitive analysis.

Required:
  • Migration moat — the time or money cost to migrate from the workaround
  • At least one of: training inertia, process disruption cost, in-flight work at risk

For each strength, tie the cost to a specific role. A strength that cannot be
assigned to a role is underspecified.

────────────────────────────────────────────
SECTION 3 — INERTIA'S VULNERABILITIES (FAILURE MODES)
────────────────────────────────────────────

Every competitor has weaknesses. Inertia's weaknesses are the specific scenarios
where the workaround breaks, corrupts data, causes rework, or hits a scale ceiling.

Find at least two vulnerabilities. Generic weaknesses ("it's slow") are not
vulnerabilities — they are positioning claims. A real vulnerability is specific,
observable, and produces a concrete consequence the role can see:

  FM-[N]: [Scenario where Inertia fails]. Role who experiences it: [role].
          Observable consequence: [what they see — error, corruption, rework, delay].

────────────────────────────────────────────
SECTION 4 — DEFEAT CONDITIONS (INERTIA'S LOSS SCENARIOS)
────────────────────────────────────────────

Under what specific, observable conditions does a team decide Inertia has lost?

These are not aspiration statements ("when teams realize the value"). They are
observable events tied to Inertia's vulnerabilities from Section 3. A defeat
condition names a team type, states a testable trigger, and connects to a
failure mode.

Identify at least two defeat conditions:

  DC-[N]: [Team type] abandons Inertia when [falsifiable event, connected to FM-N].

A defeat condition that any team could trigger, regardless of type, is not
specific enough. Name the segment.

────────────────────────────────────────────
SECTION 5 — INERTIA THREAT SCORE (COMPETITIVE VERDICT)
────────────────────────────────────────────

Issue your competitive verdict on Inertia as a competitor to this feature.

  Inertia Threat Score: HIGH / MEDIUM / LOW

Inertia starts at HIGH. It only drops if your analysis has uncovered a specific,
quantified condition under which its switching cost becomes negligible or its
failure modes become immediately visible to decision-makers. State the condition
if you downgrade.

If you cannot name the two defeat conditions in Section 4 with falsifiable
triggers, the score is HIGH and the feature decision should pause.
```

---

## V-04 — Combination Axis: Role Sequence + A-08 Fail-First + A-12 BRIDGE Dual-Closure
**Hypothesis**: Numbering failure modes before defeat conditions are written (A-08), then closing both the FM→actor chain and FM→trigger chain through named bridge artifacts (A-12 Q3 and Q4), structurally guarantees the high-value A-08+A-12 combination that R5 left untested.

```
You are running /scout:inertia for the topic: {{topic}}.

This analysis has six sections. Complete them in order. Sections 3 and 4 use
reference numbers from Section 2. Sections Q3 and Q4 are named BRIDGE artifacts
that must close two explicit chains — do not omit them.

────────────────────────────────────────────
SECTION 1 — ROLE REGISTRY
────────────────────────────────────────────

Declare every actor before any analysis begins. Use role-level labels only.
Never use "the team", "users", or a department name.

  PERFORMER: [role that executes the workaround]
  DECISION-MAKER: [role that owns the adopt/continue decision]
  AFFECTED PARTY: [role that bears downstream cost]

Add any additional roles discovered during the analysis here before using them.

────────────────────────────────────────────
SECTION 2 — WORKAROUND MAP
────────────────────────────────────────────

Name the specific workaround. Identify the tool, the export format, the
destination, the frequency, and which REGISTRY role performs it.

State the ongoing cost with a unit:
  "[PERFORMER] spends [N] [unit] per [frequency] doing [specific action]."

────────────────────────────────────────────
SECTION 3 — FAILURE MODE INVENTORY  ← COMPLETE BEFORE SECTION 5
────────────────────────────────────────────

IMPORTANT: Number failure modes here before writing defeat conditions in Section 5.
Defeat conditions reference FM numbers. You cannot write a grounded defeat condition
without a numbered failure mode to reference.

Identify at least two failure modes where the workaround breaks, produces errors,
causes rework, or cannot scale. Generic pain ("manual is slow") fails — you need a
specific observable scenario.

  FM-01: [Specific scenario]. Trigger: [what causes it]. Consequence: [what
         PERFORMER or AFFECTED PARTY sees]. Role: [from registry].

  FM-02: [Specific scenario]. Trigger: [what causes it]. Consequence: [what
         PERFORMER or AFFECTED PARTY sees]. Role: [from registry].

────────────────────────────────────────────
SECTION 4 — SWITCHING COST ANALYSIS
────────────────────────────────────────────

Quantify at least two switching cost categories with units. At least one must
be tied to a specific REGISTRY role.

  • Migration effort: [ROLE] spends [N] [unit] to migrate because [reason].
  • [Training / disruption / in-flight risk]: [ROLE] incurs [N] [unit] because [reason].

"Significant" without a number fails.

────────────────────────────────────────────
SECTION 5 — DEFEAT CONDITIONS  ← REFERENCE FM NUMBERS FROM SECTION 3
────────────────────────────────────────────

Write at least two defeat conditions. Each must:
  • Reference a numbered FM from Section 3
  • Name a specific team type (not "users")
  • Be falsifiable — an observer can confirm whether it has been met

  DC-01: [Team type] abandons the workaround when [falsifiable condition].
         Connected to: FM-[N].

  DC-02: [Team type] abandons the workaround when [falsifiable condition].
         Connected to: FM-[N].

────────────────────────────────────────────
Q3 BRIDGE — FM → ACTOR CLOSURE
────────────────────────────────────────────

This is a named bridge artifact. It closes the chain from failure mode to
the actor who experiences it. It must be structurally present — it cannot
be satisfied by prose that happens to mention both.

For each FM in Section 3, state:
  FM-[N] → experienced by [REGISTRY role] → therefore the primary target
  of DC-[N] defeat condition.

If a failure mode has no named role in your registry, return to Section 1
and add the role before completing this section.

────────────────────────────────────────────
Q4 BRIDGE — FM → TRIGGER CLOSURE
────────────────────────────────────────────

This is the second named bridge artifact. It closes the chain from failure
mode to the observable trigger that activates a defeat condition.

For each DC in Section 5, state:
  DC-[N] is triggered when FM-[N] occurs under [specific observable condition].
  Observable signal: [what DECISION-MAKER sees that confirms the trigger fired].

This is the moment inertia loses. If you cannot state an observable signal,
the defeat condition is not falsifiable and Section 5 must be revised.

────────────────────────────────────────────
SECTION 6 — INERTIA THREAT SCORE
────────────────────────────────────────────

  Inertia Threat Score: [HIGH / MEDIUM / LOW]
  Justification: [one sentence citing switching cost magnitude or FM frequency
                  from the analysis above; default is HIGH]

If Q3 or Q4 BRIDGE artifacts are incomplete, do not soften the threat score
downward — an analysis with broken chains has not earned a MEDIUM or LOW.
```

---

## V-05 — Combination Axis: A-11 Question-per-Criterion + A-12 BRIDGE Dual-Closure
**Hypothesis**: Embedding one explicit answerable question per essential criterion (A-11) makes unanswered criteria structurally visible as blank answers — the author cannot skip C-05 failure modes by writing good C-04 defeat conditions. BRIDGE markers then guarantee the FM→actor and FM→trigger chains close regardless of prose quality.

```
You are running /scout:inertia for the topic: {{topic}}.

Each section below contains one required question. You must answer it directly
before moving to analysis. An unanswered question is a missing criterion —
it cannot be compensated by quality elsewhere in the output.

────────────────────────────────────────────
[C-01] WORKAROUND IDENTIFICATION
────────────────────────────────────────────

Required question — answer this before the section:
  "What is the exact name of the workaround, which specific role performs it,
   and what is the measured cost in time or money per unit of frequency?"

Answer: ___________

Analysis: Expand on the mechanism — what tool is used, what format is exported,
where it lands, what the recipient does with it. Every actor must be named at
role level ("the data analyst", not "the team").

────────────────────────────────────────────
[C-05] WORKAROUND FAILURE MODES  ← BEFORE DEFEAT CONDITIONS
────────────────────────────────────────────

Required question — answer this before the section:
  "In what specific scenario does the workaround produce an error, silent failure,
   data corruption, or hit a scale ceiling — and which role experiences it?"

Answer: ___________

Analysis: Identify at least two failure modes. Number them FM-01, FM-02 (continue
as needed). Each must name an observable consequence — not a general slowness
complaint, but a specific thing that breaks or corrupts.

  FM-01: [scenario]. Observable consequence: [what the role sees]. Role: [label].
  FM-02: [scenario]. Observable consequence: [what the role sees]. Role: [label].

────────────────────────────────────────────
[C-02] SWITCHING COST QUANTIFICATION
────────────────────────────────────────────

Required question — answer this before the section:
  "What are the migration hours for [PERFORMER role], and what training,
   disruption, or in-flight work costs add to that migration?"

Answer: ___________

Analysis: State at least two cost categories with units. "Significant" without
a number fails. At least one cost must be tied to a named role.

  Migration: [role] spends [N] [unit] to migrate because [specific reason].
  [Second category]: [role] incurs [N] [unit] because [specific reason].

────────────────────────────────────────────
[C-04] DEFEAT CONDITIONS
────────────────────────────────────────────

Required question — answer this before the section:
  "Under exactly what observable, testable condition does [specific team type]
   abandon the workaround — and which FM from the inventory triggers it?"

Answer: ___________

Analysis: Identify at least two defeat conditions. Each must name a team type,
be falsifiable, and reference a numbered FM from the C-05 section above.

  DC-01: [Team type] abandons the workaround when [falsifiable condition].
         References: FM-[N].
  DC-02: [Team type] abandons the workaround when [falsifiable condition].
         References: FM-[N].

────────────────────────────────────────────
[C-03] INERTIA THREAT SCORE
────────────────────────────────────────────

Required question — answer this before the section:
  "What is the inertia threat score — and if it is not HIGH, what specific
   quantified condition from the analysis above justifies the downgrade?"

Answer: ___________

  Inertia Threat Score: [HIGH / MEDIUM / LOW]
  Justification: [cite the specific condition, or state "default HIGH applies"]

────────────────────────────────────────────
Q3 BRIDGE — FM → ACTOR CLOSURE  [named artifact]
────────────────────────────────────────────

For each numbered FM above, close the chain to the actor who experiences it
and the defeat condition it feeds:

  FM-[N] → experienced by [role] → activates DC-[N] when [observable trigger].

This artifact is structurally required. If a failure mode has no named role,
return to C-05 and add the role before completing this bridge.

────────────────────────────────────────────
Q4 BRIDGE — FM → TRIGGER CLOSURE  [named artifact]
────────────────────────────────────────────

For each defeat condition above, close the chain to the specific FM trigger
and the observable signal the DECISION-MAKER sees:

  DC-[N] fires when FM-[N] occurs under [observable condition].
  Signal visible to [DECISION-MAKER role]: [what they see that confirms it].

This artifact is structurally required. A defeat condition with no observable
signal is not falsifiable. If Q4 cannot be completed, revise C-04 first.

────────────────────────────────────────────
COMPLETENESS GATE
────────────────────────────────────────────

Before submitting, verify:
  [ ] C-01 required question answered (named workaround, role, unit cost)
  [ ] C-05 required question answered (≥2 FM, numbered, role named)
  [ ] C-02 required question answered (≥2 costs with units, ≥1 to a role)
  [ ] C-04 required question answered (≥2 falsifiable conditions, FM referenced)
  [ ] C-03 required question answered (threat score declared)
  [ ] Q3 BRIDGE: every FM closed to an actor and a defeat condition
  [ ] Q4 BRIDGE: every defeat condition closed to an FM trigger and observable signal

Any unchecked box = structural gap, not a content gap.
```

---

## Variation Summary

| Variation | Primary Axis | A-08 | A-11 | A-12 | Key Bet |
|-----------|-------------|------|------|------|---------|
| V-01 | Role sequence (registry-first) | — | — | — | Role registry prevents department-drift throughout |
| V-02 | Output format (tables) | implicit numbering | — | — | Blank cells surface missing criteria structurally |
| V-03 | Inertia framing (personified competitor) | — | — | — | Competitor instincts sharpen falsifiability |
| V-04 | Role-first + A-08 + A-12 | explicit FM-before-DC | — | Q3+Q4 named | R6 target: A-08+A-12 combination, roles anchor the chains |
| V-05 | A-11 + A-12 | implicit (C-05 before C-04) | explicit question/criterion | Q3+Q4 named | Unanswered questions visible as blanks; bridge guarantees chain closure |
