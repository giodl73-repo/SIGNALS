# scout-inertia — V-01 through V-05

**Variation axes selected for single-axis (V-01, V-02, V-03):**
- Output format (table-dominant vs prose vs hybrid)
- Inertia framing (fail-first vs linear vs question-primed)
- Role sequence (roles-first anchor vs workaround-first vs lifecycle-ordered)

**Combined (V-04, V-05):** fail-first + table | question-primed + bridges + role sequence

---

## V-01 — Output Format: Table-Dominant

**Axis**: Output format (structured tables throughout)
**Hypothesis**: Tables force explicit quantification and make FM-to-trigger chains scannable, improving A-09 chain citation compliance vs prose narration.
**Structure**: `structure declaration | workaround table | cost table | FM table | defeat table`

---

```
Structure: table-dominant | linear-checklist

You are analyzing inertia as a competitor for the feature described below.
Inertia is the primary competitor for every feature. Teams already have a
workaround. Adopting your feature costs time, training, and disruption. Your
job is to map that workaround precisely and answer one question: why does
inertia lose?

If you cannot answer that question with specific, falsifiable defeat conditions,
stop and say so.

---

**Feature**: {{feature_name}}
**Context**: {{feature_context}}

---

## Step 1 — Workaround Map

Describe the current workaround in a table. Be concrete. Name the tool,
file format, or manual process teams use today.

| Dimension | Detail |
|-----------|--------|
| Primary workaround | (name and describe) |
| Who performs it | (role and frequency) |
| How long it takes | (time per instance) |
| Error rate or re-work rate | (quantify if possible) |
| Scale ceiling | (at what volume does it start to break) |

If multiple workarounds exist for different team types, add a row per variant.

---

## Step 2 — Switching Cost Table

Enumerate every cost a team would incur to abandon the workaround and adopt
the feature. Cite each cost to a specific role.

| Cost Type | Who Bears It | Estimated Magnitude | Evidence or Basis |
|-----------|--------------|---------------------|-------------------|
| Migration time | | | |
| Training | | | |
| Process disruption (in-flight work) | | | |
| Integration or tooling changes | | | |
| Approval or compliance overhead | | | |

Add rows as needed. Magnitude must be quantified (hours, days, dollars, or
percentage of a sprint). "High" without a unit fails.

---

## Step 3 — Failure Mode Table

Identify at least two failure modes: specific scenarios where the workaround
breaks, produces errors, causes re-work, or cannot scale. Generic pain points
do not count. Each failure mode must be observable and falsifiable.

| FM-ID | Failure Mode | Observable Symptom | Affected Role | Frequency or Trigger Condition |
|-------|-------------|-------------------|---------------|-------------------------------|
| FM-1 | | | | |
| FM-2 | | | | |
| FM-3 | | (optional) | | |

---

## Step 4 — Defeat Conditions

For each defeat condition, name the failure mode that makes switching possible
and the team type most likely to hit it. This is the FM-to-trigger chain.
"Teams switch when FM-2 causes delivery failures for teams shipping weekly"
passes. "Teams switch when costs become unsustainable" fails.

| Trigger ID | Condition | FM That Drives It | Team Type | Role Most Affected |
|------------|-----------|-------------------|-----------|--------------------|
| T-1 | | | | |
| T-2 | | | | |
| T-3 | (optional) | | | |

Inertia threat score: HIGH (default). State any conditions that would lower it
to MEDIUM, with justification.

---

## Step 5 — Inertia Verdict

Answer in one paragraph: **Why does inertia lose?**

The paragraph must reference at least one failure mode by ID and connect it to
a defeat condition. If you cannot write this paragraph with specific references,
state that the analysis is inconclusive and explain what evidence is missing.
```

---

## V-02 — Inertia Framing: Fail-First

**Axis**: Inertia framing (lead with the strongest case FOR inertia before pivoting to defeat conditions)
**Hypothesis**: Starting with maximum advocacy for the status quo forces the analyst to engage seriously with switching resistance, producing more honest and specific trigger analysis.
**Structure**: `structure declaration | fail-first | pivot | FM table | defeat conditions`

---

```
Structure: fail-first | pivot | FM-grounded defeat

You are analyzing inertia as a competitor for a feature. Inertia is the
primary competitor. Start by making the strongest possible case FOR it.

Then find where it breaks.

---

**Feature**: {{feature_name}}
**Context**: {{feature_context}}

---

## Part 1 — The Case for Doing Nothing

Argue that the team should keep the current workaround. Be specific. Name the
workaround. Describe it in enough detail that someone unfamiliar with the team
could replicate it. Quantify switching cost (time, training, disruption). Name
the roles who would be most disrupted.

Your argument should be uncomfortable. If it reads like a strawman, it is not
strong enough.

Required elements in Part 1:
- Name of the current workaround
- Who owns it (role, not just "the team")
- How long it has been in use (if estimable)
- Three quantified reasons to keep it:
  1. Migration cost (hours or days, cited to a role)
  2. Training cost (hours, who attends)
  3. Process disruption (what is in-flight that would be interrupted)
- Inertia threat score: HIGH (default; justify any deviation)

---

## Part 2 — The Pivot: Where Inertia Shows Cracks

Now identify specific, observable failure modes in the workaround. These are
the only valid paths to switching. Each failure mode must be:
- Observable: a person can see or measure when it occurs
- Falsifiable: there is a condition under which it does NOT occur
- Scoped: it affects a specific role or team type

**Failure Mode 1 (FM-1)**
- Description:
- Observable symptom:
- Role most affected:
- Frequency or volume trigger:

**Failure Mode 2 (FM-2)**
- Description:
- Observable symptom:
- Role most affected:
- Frequency or volume trigger:

*(Add FM-3 if a third failure mode is materially distinct from FM-1 and FM-2.)*

---

## Part 3 — Defeat Conditions

For each defeat condition, state:
1. The trigger: the specific circumstance that causes the team to act
2. The failure mode that makes the trigger possible (cite by ID)
3. The team type most exposed to this trigger
4. The role who feels it most acutely

Format:

**Defeat Condition 1**
- Trigger: [specific, falsifiable condition]
- Driven by: FM-[N] — [brief description of the failure mode]
- Team type: [who hits this]
- Role: [who feels it]

**Defeat Condition 2**
- Trigger:
- Driven by:
- Team type:
- Role:

Conditions such as "teams switch when they see the value" or "adoption grows
over time" are not defeat conditions. Reject them. Replace with mechanism.

---

## Part 4 — Verdict

One paragraph. Begin with: "Inertia loses when..."

Cite at least one failure mode by ID. Connect it to a defeat condition. State
what type of team is most likely to cross the threshold first. State what
evidence would change this verdict.
```

---

## V-03 — Role Sequence: Roles-First Anchor

**Axis**: Role sequence (enumerate and anchor to specific roles before analyzing workarounds)
**Hypothesis**: Anchoring every analysis step to specific roles before describing workarounds forces role-level precision throughout, improving R-01 and R-02 compliance and making cost citations more specific.
**Structure**: `structure declaration | role inventory | per-role workaround | per-role FM | defeat by role`

---

```
Structure: role-anchored | per-role workaround | FM-by-role | defeat by team type

You are analyzing inertia as a competitor for the feature described below.
Inertia is the primary competitor. Before analyzing anything else, identify who
is affected. Then trace the workaround, failure modes, and defeat conditions
through those specific roles.

---

**Feature**: {{feature_name}}
**Context**: {{feature_context}}

---

## Section 1 — Role Inventory

List every role that uses or is affected by the current workaround. For each
role, state:
- What they do with the workaround
- How often
- What they would have to change to adopt the feature

| Role | Current Behavior | Frequency | Change Required |
|------|-----------------|-----------|-----------------|
| | | | |
| | | | |

Minimum two roles. If only one role exists, note that and explain why.
If different team types use different workarounds, note the variant per row.

---

## Section 2 — Per-Role Workaround Map

For each role identified in Section 1, describe the workaround in enough
detail that someone new could replicate it. Include:
- The specific tool, file format, or manual step
- The error or quality risk in their current process
- One quantified cost (time per instance, error rate, or re-work rate)

**[Role 1]**
- Workaround: 
- Error or quality risk: 
- Quantified cost: 

**[Role 2]**
- Workaround: 
- Error or quality risk: 
- Quantified cost: 

---

## Section 3 — Switching Cost, by Role

For each role, enumerate what they would lose by switching to the feature.
This is the inertia force from their perspective.

**[Role 1]**
- Migration time: (hours/days)
- Training: (hours, what they need to learn)
- In-flight disruption: (what they would have to pause or migrate)

**[Role 2]**
- Migration time: 
- Training: 
- In-flight disruption: 

Inertia threat score for this feature: HIGH (default). Note any role where
the switching cost is lower than average and explain why.

---

## Section 4 — Failure Modes, by Role

Identify at least two failure modes: observable scenarios where the current
workaround breaks or causes re-work. Assign each failure mode to the role most
affected. Generic pain points ("slow") do not pass.

**FM-1**
- Scenario: 
- Observable symptom: 
- Primary role affected: 
- Volume or frequency trigger: 

**FM-2**
- Scenario: 
- Observable symptom: 
- Primary role affected: 
- Volume or frequency trigger: 

---

## Section 5 — Defeat Conditions, Scoped to Team Type

State the specific conditions under which each role or team type abandons the
workaround. Each condition must be:
- Falsifiable (names a threshold, not a sentiment)
- Connected to a failure mode by ID
- Scoped to the role or team type most affected

**Defeat Condition 1**
- Condition: 
- Role that triggers it: 
- FM that makes it possible: FM-[N]
- Team type most exposed: 

**Defeat Condition 2**
- Condition: 
- Role that triggers it: 
- FM that makes it possible: FM-[N]
- Team type most exposed: 

---

## Section 6 — Verdict

Why does inertia lose? Write one paragraph that:
1. Names the failure mode most likely to break the workaround
2. States the team type that hits it first
3. Identifies the role who owns the decision to switch
4. Gives the condition under which that role acts

If you cannot write this paragraph with specific references, state what is
missing and what investigation would fill the gap.
```

---

## V-04 — Combined: Fail-First + Table-Dominant

**Axes**: Inertia framing (fail-first) + Output format (tables)
**Hypothesis**: Fail-first framing combined with tables forces each failure mode to be row-itemized with explicit FM-to-trigger chain citations, directly enforcing A-09 chain compliance at the structural level rather than relying on prose discipline.
**Structure**: `structure declaration | fail-first prose section | FM table | defeat table with FM column | verdict`

---

```
Structure: fail-first | table-dominant | FM-to-trigger chain

You are analyzing inertia as a competitor for the feature described below.
Inertia is the primary competitor for every feature.

Start by making the strongest case for the status quo. Then find the failure
modes. Then show where the chain from failure mode to switching trigger is
specific enough to be actionable.

If you cannot complete the FM-to-trigger chain for at least two defeat
conditions, the analysis is incomplete. Say so.

---

**Feature**: {{feature_name}}
**Context**: {{feature_context}}

---

## Phase 1 — Inertia Case (Prose)

Write 2-3 paragraphs arguing that the team should keep the current workaround.
Name the workaround. Quantify the switching cost for the two most affected
roles. Describe what is at risk if the migration goes wrong.

This argument must be specific enough that a skeptic would find it credible.
If it reads as weak, revisit your switching cost estimates.

Inertia threat score: HIGH (default). State any conditions that would lower
this score, with quantified justification.

---

## Phase 2 — Workaround Summary Table

| Attribute | Value |
|-----------|-------|
| Workaround name | |
| Primary roles | |
| Frequency of use | |
| Time cost per instance | |
| Known error or re-work rate | |
| Scale ceiling | |
| Approximate time in use | |

---

## Phase 3 — Switching Cost Table

| Cost Type | Role | Magnitude | Basis |
|-----------|------|-----------|-------|
| Migration | | | |
| Training | | | |
| In-flight disruption | | | |
| Tool or integration changes | | | |
| Approval or compliance overhead | | | |

Magnitude column must contain a unit (hours, days, %, sprint fraction).
"Significant" without a unit fails.

---

## Phase 4 — Failure Mode Table

| FM-ID | Failure Mode | Observable Symptom | Affected Role | Volume or Frequency Trigger |
|-------|-------------|-------------------|---------------|----------------------------|
| FM-1 | | | | |
| FM-2 | | | | |
| FM-3 | (optional) | | | |

Each failure mode must be observable (measurable symptom) and falsifiable
(a condition under which it does NOT occur). "Manual processes are slow" fails.
"CSV export silently truncates rows over 65,536 — no error message" passes.

---

## Phase 5 — Defeat Condition Table

This is the FM-to-trigger chain. Each row must name the failure mode that makes
the defeat condition possible. Without the FM column, the chain is incomplete.

| Trigger ID | Condition | FM That Drives It | Team Type | Role Most Affected |
|------------|-----------|-------------------|-----------|--------------------|
| T-1 | | FM-[N]: | | |
| T-2 | | FM-[N]: | | |
| T-3 | (optional) | FM-[N]: | | |

Condition column: must be falsifiable. "Teams switch when they see value" fails.
"Teams switch when FM-2 causes two or more delivery failures per quarter" passes.

---

## Phase 6 — Verdict

One paragraph beginning: "Inertia loses when..."

Required:
- One failure mode cited by ID
- One defeat condition cited by trigger ID
- The team type that hits the threshold first
- What evidence would change this verdict
```

---

## V-05 — Combined: Question-Primed + Bridges + Role Sequence

**Axes**: Phrasing register (question-primed) + Role sequence (roles-first) + Lifecycle emphasis (bridge markers)
**Hypothesis**: Framing each section as a question forces the analyst to produce an answer, not a description. Bridge markers between failure mode → actor → cost → trigger make A-09 chain citation a structural requirement rather than an optional connection.
**Structure**: `structure declaration | question-primed | role-anchored | bridge-marked FM-to-trigger chain`

---

```
Structure: question-primed | role-anchored | bridge-marked

Answer each question below in sequence. Each question has a minimum answer
contract. If you cannot meet the contract, state what is missing.

The central question — Why does inertia lose? — appears at the end. Every
earlier question builds the evidence required to answer it.

---

**Feature**: {{feature_name}}
**Context**: {{feature_context}}

---

### Q1 — Who uses the current workaround, and how?

Name every role that touches the workaround. For each role:
- What specific tool, file, or manual step do they use?
- How often?
- What is their primary quality or reliability risk in the current process?

Minimum answer contract: two roles, each with a named workaround and a
specific quality risk. "The team exports manually" fails. "Data analysts export
to CSV and re-import to Excel weekly; rows above 65,536 are silently dropped"
passes.

---

### Q2 — What does switching cost, by role?

For each role identified in Q1:
- What would they have to stop doing or migrate?
- How long would that take? (cite a unit: hours, days, sprint)
- What training is required?
- What is at risk if the migration fails mid-flight?

Minimum answer contract: two roles with quantified migration time and one
in-flight risk per role.

Inertia threat score: HIGH (state any exception with justification).

---

### Q3 — Where does the workaround break?

Name at least two failure modes: specific scenarios where the workaround
produces an error, causes re-work, or fails to scale.

For each failure mode, answer:
- What exactly happens? (the observable symptom)
- Who sees it first? (the role)
- Under what condition does it occur? (volume, frequency, or event)

**BRIDGE →** From each failure mode, draw an explicit bridge to the role it
exposes and the cost that role bears when it occurs. Format:

> FM-[N] exposes [Role] because [mechanism], costing [quantified impact].

Minimum answer contract: two failure modes, each with a BRIDGE statement.
"Manual processes create errors" fails. "FM-1: CSV row-truncation exposes the
Data Analyst because the export provides no warning, costing 4-8 hours of
re-work per incident when downstream reports fail reconciliation" passes.

---

### Q4 — Under what specific conditions does the workaround fail to hold?

Name at least two defeat conditions: the precise circumstances under which a
team stops tolerating the workaround and acts.

For each defeat condition:
- What is the trigger? (falsifiable threshold or event)
- Which failure mode makes this trigger possible? (cite FM-[N])
- Which team type is most exposed to this trigger?
- Which role owns the decision to switch?

**BRIDGE →** From each defeat condition, draw an explicit bridge back to its
failure mode. Format:

> T-[N] is possible because FM-[N] [describe the mechanism that enables switching].

Minimum answer contract: two defeat conditions, each with FM citation and
BRIDGE statement. "Teams switch when the pain is high enough" fails.
"T-1: Teams switch when FM-1 causes two or more reconciliation failures in a
single quarter, because at that frequency the cost of staying exceeds the
migration cost — T-1 is possible because FM-1 produces silent data loss
that only surfaces after downstream delivery, giving teams no early warning to
absorb the impact" passes.

---

### Q5 — Why does inertia lose?

Write one paragraph that synthesizes Q1 through Q4.

Required elements:
- The failure mode most likely to break the workaround (cite by ID)
- The team type that hits the threshold first
- The role who owns the switch decision
- The defeat condition that triggers the switch (cite by ID)
- One sentence on what evidence would change this verdict

If you cannot write this paragraph with specific references to prior answers,
identify which question produced insufficient evidence and what investigation
would fill the gap.
```

---

## Variation Summary

| Variation | Axes | Key Hypothesis | A-09 Strategy | A-10 |
|-----------|------|---------------|--------------|------|
| V-01 | Format: table-dominant | Tables force quantification + FM scanning | FM column in defeat table | Declared |
| V-02 | Framing: fail-first | Advocacy pressure → honest triggers | Explicit mechanism in Part 3 | Declared |
| V-03 | Sequence: roles-first | Role anchor forces R-01/R-02 throughout | FM assigned to role, defeat scoped to team type | Declared |
| V-04 | Framing + Format | Fail-first + tables → FM column structurally required | Phase 5 table: FM column mandatory | Declared |
| V-05 | Register + Bridges + Roles | Questions force answers; bridges make chain explicit | BRIDGE marker is a structural requirement per section | Declared |

**Recommendation for golden testing order**: V-02 first (highest fail-first pressure), V-05 second (bridge markers enforce chain most explicitly), V-04 third (combines both pressures in table form). V-01 and V-03 establish baselines for format and role-anchor independently.
