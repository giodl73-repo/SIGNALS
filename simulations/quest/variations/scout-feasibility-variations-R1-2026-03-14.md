5 variations written to `simulations/quest/variations/scout-feasibility-variations-R1-2026-03-14.md`.

---

## Summary

| Variation | Axis | Core Hypothesis |
|-----------|------|-----------------|
| **V-01** Baseline | spec as written | establishes floor; silent inference failures (SF-01/SF-03) likely |
| **V-02** PM leads | role sequence | PM-first makes C-03 and C-09 structurally unavoidable — budget is visible before Architect scores |
| **V-03** Prose | output format | narrated paragraphs force substantive rationale for C-05/C-08; risk: C-01 traffic lights scatter |
| **V-04** Interrogative | phrasing register | Q&A frame makes silent inference impossible — every inferred value is an explicit answer |
| **V-05** Phased + inertia | lifecycle emphasis + inertia framing | hard phase gates block SF-01/SF-03; status-quo baseline pulls C-07 (scoped score) and C-10 (amendment list) into the verdict naturally |

**Expected rubric performance:**

- V-01 passes C-01/C-02 reliably; C-03/C-04 are the likely failure points (SF-03, SF-01)
- V-02 is the strongest candidate for C-09 (hour budget comparison) — it is the only variation that calculates hours before scoring
- V-03 is the strongest candidate for C-05/C-08 rationale quality — prose forces narration over enumeration
- V-04 is the SF-01/SF-03 fix candidate — question framing makes every inference a required answer
- V-05 is the best all-criteria candidate; phase gates cover C-03/C-04, inertia framing covers C-07/C-10

Run all 5 against the rubric to identify which criterion each variation reliably passes, then combine the winning patterns into V-golden.
red from it.

STACK SUMMARY: List the inferred stack. State the source of each inference.

TEAM AND TIMELINE: Infer team size and timeline from repo signals (contributor count,
complexity, project age). DISCLOSE these inferences explicitly before using them in any
calculation. Do not silently use "one sprint" or any other estimate.

ROLES: Run three lenses in order:
- Architect: Decompose the idea into components. Score each component complexity (1-10).
  Rate each GREEN / YELLOW / RED based on fit with the current stack.
- PM: Overlay the timeline. Given the inferred team size and timeline, is the complexity
  achievable? Flag over-budget explicitly.
- Strategy: For each component, recommend Build / Buy / Use existing. State the reason.

FINDINGS:
1. Component table: Name | Traffic light | Complexity score | Build-vs-buy
2. RED blockers: For each RED component, explain WHY it is a blocker and what would
   need to change to lift the rating.
3. Feasibility score: 0-100. Label: NOT FEASIBLE (<50) / FEASIBLE WITH CAVEATS (50-79)
   / FEASIBLE (80+).
4. If score < 50: provide a scoped alternative score. State the constraint that enables it
   (e.g., "Scoped to flat binding only: 62/100").
5. If FEASIBLE WITH CAVEATS: list numbered prerequisites. Every RED item must appear.

Write artifact to simulations/scout/feasibility/{topic}-feasibility-{date}.md with
frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred.
```

---

## V-02: PM leads (timeline-first role sequence)

Axis: Role sequence -- PM runs first, establishes budget before Architect scores complexity
Hypothesis: When PM surfaces team/timeline explicitly in Phase 1 before any scoring,
C-03 (inference disclosure) and C-09 (hour budget comparison) become structurally unavoidable.
The Architect then scores against a visible budget rather than an implicit one, reducing
SF-03 failures.

```
You are running /scout-feasibility. The PM role runs first. Timeline and team size must
be established before complexity scoring begins.

SETUP: Scan the repo for stack signals: package.json, tsconfig.json, Cargo.toml.
If canonical files are absent, fall back to CLAUDE.md, program.yaml, or README.
Disclose the fallback: name the file used, state what you inferred from it.

PHASE 1 -- PM (Timeline First):
Before scoring anything, surface these values explicitly:
- Team size: [N] (inferred from [source])
- Timeline: [N weeks] (inferred from [source])
- Available engineering hours: team_size x timeline_weeks x hours_per_week_estimate

Write these three lines before proceeding. Do not proceed until they are visible.

PHASE 2 -- Architect (Complexity Against Budget):
Decompose the idea into 4-8 components. For each:
- Complexity score (1-10)
- Estimated hours
- Traffic light: GREEN (fits stack and budget) / YELLOW (fits stack, tight budget)
  / RED (stack gap or over budget)

Sum the estimated hours. Compare to available hours from Phase 1. Flag over-budget
or under-budget explicitly.

PHASE 3 -- Strategy (Build-vs-Buy):
For each component: Build / Buy / Use existing. State the reason in one sentence.

FINDINGS:
1. Component table: Name | Est hours | Traffic light | Build-vs-buy
2. Hour budget: [estimated total] vs [available total]. Over/under flag.
3. RED blockers: each RED item -- why it is blocked, what would lift it
4. Feasibility score 0-100. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE
5. If score < 50: scoped alternative score with enabling constraint
6. If FEASIBLE WITH CAVEATS: numbered prerequisites, all RED items represented
7. Amendment list: 3 numbered actions, each traceable to a specific RED or YELLOW component

Write artifact to simulations/scout/feasibility/{topic}-feasibility-{date}.md with
frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated.
```

---

## V-03: Table-free prose (output format axis)

Axis: Output format -- replace component table with narrated paragraphs, no tables anywhere
Hypothesis: Prose sections force the model to narrate rationale rather than fill cells.
C-05 (RED blocker rationale) and C-08 (prerequisites) are more likely to contain substantive
reasoning when they cannot hide behind terse table entries. Risk: C-01 traffic lights may
scatter and become harder to scan.

```
You are running /scout-feasibility. Write in prose, not tables. Each finding is a
named section with a narrative, not a matrix row.

SETUP: Scan for stack signals (package.json, tsconfig.json, Cargo.toml).
If none found: write one sentence naming the fallback file and stating what you inferred.
This sentence is required before analysis begins.

INFERENCE DISCLOSURE:
Write these two sentences verbatim (with values filled in) before any scoring:
"Team size inferred as [N] from [source]."
"Timeline inferred as [N weeks] from [source]."

COMPONENT ANALYSIS:
For each major component (4-8 total), write a short paragraph:
- What the component does and what stack support it needs
- Whether the current stack provides it: state GREEN / YELLOW / RED
- Estimated complexity
- Build / Buy / Use existing recommendation with one-sentence reason

RED BLOCKERS:
For each RED component, write a dedicated paragraph:
- The specific gap (what is missing from the stack or timeline)
- What would change the rating (specific action, dependency, or scope reduction)
Do not group multiple RED items into a single paragraph.

FEASIBILITY VERDICT:
Score: [0-100]
Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE

If NOT FEASIBLE: follow immediately with a scoped alternative.
  "Scoped to [specific constraint]: [N]/100."
If FEASIBLE WITH CAVEATS: follow with a numbered prerequisite list.
  Every RED-rated component must be represented.

AMENDMENTS:
End with a numbered list of 3 actions. Each action must name the specific component
it addresses and state what changes in the feasibility assessment if it is completed.

Write artifact to simulations/scout/feasibility/{topic}-feasibility-{date}.md with
frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred.
```

---

## V-04: Interrogative register (phrasing axis)

Axis: Phrasing register -- diagnostic question sequence replaces imperative role instructions
Hypothesis: Framing each phase as a question the skill must answer forces every inferred
value to be stated as an answer. C-03 and C-04 silent inference failures (SF-01, SF-03)
become structurally impossible when the question "Who is building this?" must be answered
explicitly before proceeding. Risk: question framing may produce chattier output.

```
You are running /scout-feasibility. Proceed as a diagnostic -- answer each question in
sequence. Each answer is a finding.

Q1. What is the stack?
Scan: package.json, tsconfig.json, Cargo.toml. List what you find.
If canonical files are absent: write one sentence naming the fallback file and stating
what you inferred from it. Required before Q2.

Q2. Who is building this, and when?
State explicitly:
- Inferred team size: [N] (source: ___)
- Inferred timeline: [N weeks] (source: ___)
- Available hours: [N]
Do not proceed to Q3 without writing these three values.

Q3. What are the components?
Decompose the idea into 4-8 components. For each, state:
- What stack support it requires
- Whether the stack has it: GREEN / YELLOW / RED
- Estimated complexity (1-10)

Q4. What is blocked?
For every RED component:
- Why is it blocked? (specific gap)
- What would unblock it? (specific action or dependency)
Do not skip this question if any component is RED.

Q5. Should each component be built, bought, or reused?
For each component: Build / Buy / Use existing. One sentence of reasoning.

Q6. What is the verdict?
Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE.

If score < 50: state a scoped alternative. "Scoped to [constraint]: [N]/100." Required.
If FEASIBLE WITH CAVEATS: numbered prerequisite list, all RED items included.

Q7. What should the team do next?
List 3 numbered actions. Each must name the specific RED or YELLOW component it addresses.

Write artifact to simulations/scout/feasibility/{topic}-feasibility-{date}.md with
frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred.
```

---

## V-05: Combined -- lifecycle explicit + inertia framing

Axis: Lifecycle emphasis (6 named phases with hard gates) + inertia framing (status-quo
baseline comparison in the verdict)
Hypothesis: Hard phase gates prevent SF-01/SF-03 silent inference by making Phase 2
(inference surface) a visible checkpoint that must complete before Phase 3. The inertia
framing forces a scoped fallback narrative (C-07) and amendment list (C-10) to emerge
naturally because the skill must articulate what "not building" costs vs. what "building
scoped" costs.

```
You are running /scout-feasibility. Treat "do nothing" as the reference option.
The feasibility verdict must be measured against the cost of not building.

PHASE 1 -- STACK SCAN:
Scan: package.json, tsconfig.json, Cargo.toml.
Output: list each detected signal and what it tells you about the stack.
If canonical files absent: name the fallback file. State what you inferred.
This disclosure is required before Phase 2 begins.

PHASE 2 -- INFERENCE SURFACE:
Write these three lines explicitly. Do not proceed to Phase 3 without them:
- "Team size inferred as [N] from [source]."
- "Timeline inferred as [N weeks] from [source]."
- "Available hours: [N]."

PHASE 3 -- COMPONENT RATING:
Decompose into 4-8 components. For each:
- Traffic light: GREEN / YELLOW / RED
- Complexity score (1-10)
- Estimated hours
- Build / Buy / Use existing (Strategy role, one-sentence reason)
- Architect note: what the current stack provides and what is missing

PHASE 4 -- BLOCKERS:
For every RED component, two required items:
- Blocker statement: the specific gap and why it cannot be deferred
- Lift condition: the specific change that would move this component to YELLOW

PHASE 5 -- VERDICT:
Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE.

Status-quo comparison: "Teams that skip feasibility assessment risk [specific failure
mode given the RED findings]. This assessment changes [what specifically] about that risk."

If score < 50: scoped alternative required.
  "Scoped to [specific constraint]: [N]/100. This scope removes [RED items] from scope."
If FEASIBLE WITH CAVEATS: numbered prerequisites, all RED items represented.

PHASE 6 -- AMENDMENTS:
Numbered list of 3 actions. Each must:
- Name the specific RED or YELLOW component it addresses
- State what changes in the feasibility score if the action is completed
  (e.g., "Completing this moves component X from RED to YELLOW, raising score by ~10 pts")

Write artifact to simulations/scout/feasibility/{topic}-feasibility-{date}.md with
frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred.
```
