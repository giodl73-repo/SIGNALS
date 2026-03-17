# Quest Variate — scout-inertia R1

**Skill**: `scout-inertia` | **Round**: 1 | **Axes explored**: Role sequence, Output format, Lifecycle emphasis, Phrasing register, Inertia framing

---

## V-01 — Role Sequence: Workaround-first pipeline

**Variation axis**: Role sequence — Workaround Mapper runs before Cost Accountant, who runs before Strategist. Inertia judgment deferred to last.

**Hypothesis**: Anchoring on the workaround in detail before touching costs or conditions forces richer workaround description and reduces hand-waving on switching costs.

---

You are analyzing inertia — the option a team takes when they do nothing and keep using what they already have. This is the most important competitive analysis for any feature decision.

You will run three roles in sequence. Do not skip ahead. Each role reads the output of the prior role.

---

### Role 1 — Workaround Mapper

Your job: describe the current workaround in enough detail that a new team member could replicate it tomorrow.

Answer these questions with specifics:
- What tool, file type, manual step, or process does the team currently use?
- What data or action does the workaround handle?
- Who performs it (role, not name)?
- How often does it happen (daily, weekly, per-release)?
- What does the output look like (a file, a Slack message, a dashboard, a manual check)?

Do not move on until you have a named workaround with actor, frequency, and output artifact.

**Failure check**: If your answer contains only a category ("they use spreadsheets", "manual process"), stop and add specifics before continuing.

---

### Role 2 — Switching Cost Accountant

Read the workaround from Role 1. Your job: quantify what it costs to abandon it.

For each of the three dimensions below, provide a number or a range. Qualitative labels ("high", "moderate") are not acceptable — if you cannot estimate, say so explicitly and explain why.

**Time cost** — How many hours or days per user to learn and migrate? Include both one-time migration and ongoing ramp.

**Training cost** — What new concepts, tools, or workflows must the user learn? Estimate in hours of training or sessions required.

**Disruption cost** — What breaks during the transition period? Estimate in sprint-days of workflow disruption, or state the number of people affected by a handoff change.

Produce a cost table:

| Dimension | Estimate | Basis |
|-----------|----------|-------|
| Time | | |
| Training | | |
| Disruption | | |

---

### Role 3 — Inertia Strategist

Read the workaround (Role 1) and costs (Role 2). Your job: deliver the inertia verdict.

**Step A — Threat score**

State the inertia threat score. The default is HIGH. You may not downgrade it without naming a specific mitigating factor with documented evidence. "The feature is compelling" is not a mitigating factor.

```
Inertia threat score: HIGH
Rationale: [one sentence]
```

**Step B — Workaround failure modes**

Identify at least two specific scenarios where the current workaround breaks, produces errors, causes re-work, or cannot scale. These must be concrete and observable.

Format:
- **Failure mode 1**: [exact scenario — what triggers it, what goes wrong, what the user sees]
- **Failure mode 2**: [exact scenario]

Generic pain points ("manual is slow") do not qualify.

**Step C — Why inertia loses**

State at least two specific, falsifiable conditions under which a team abandons the workaround and adopts the feature. Each condition must be testable by a third party.

Format:
- **Condition 1**: Teams switch when [observable trigger] because [the workaround then does X, which causes Y].
- **Condition 2**: Teams switch when [observable trigger] because [the workaround then does X, which causes Y].

"Teams switch when they see the value" fails. "Teams switch when workaround failure mode 1 recurs three times in a sprint" passes.

---

**Final output**: Combine Role 1, Role 2, and Role 3 outputs into a single artifact. Do not omit any section.

---

## V-02 — Output Format: Table-structured with inline scoring

**Variation axis**: Output format — all major outputs are tables with explicit pass/fail scoring on each dimension. Prose is minimized to essential explanations.

**Hypothesis**: Forcing table output with pass/fail columns makes it harder to skip dimensions with vague language, and the self-scoring surfaces gaps before the human reviewer needs to.

---

You are producing a `scout-inertia` analysis artifact. This artifact answers one central question: **why does inertia lose?** If you cannot answer that question with specifics, the artifact is not complete.

Output every section as a table. After each table, score yourself on the required criteria.

---

### Section 1 — Workaround Profile

| Field | Value |
|-------|-------|
| Workaround name | |
| Tool / file type / process | |
| Data or action handled | |
| Who performs it (role) | |
| Frequency | |
| Output artifact | |

**Self-score C-01** (Workaround mapped in detail):
- [ ] PASS — Named workaround with actor, frequency, and output artifact present
- [ ] FAIL — Generic category only; return and add specifics

---

### Section 2 — Switching Cost Breakdown

| Dimension | Estimate | Unit | Basis / assumption |
|-----------|----------|------|--------------------|
| Time cost | | hours or days/user | |
| Training cost | | hours of training | |
| Disruption cost | | sprint-days or people affected | |

**Self-score C-02** (Switching cost quantified):
- [ ] PASS — At least 2 of 3 rows carry a number or range
- [ ] FAIL — Qualitative labels present; return and quantify

---

### Section 3 — Inertia Threat Score

| Field | Value |
|-------|-------|
| Score | HIGH / MEDIUM / LOW |
| Rationale | |
| Mitigating factor (if not HIGH) | |
| Evidence for mitigation | |

**Self-score C-03** (Score is HIGH):
- [ ] PASS — Score is HIGH, or mitigation is documented with named evidence
- [ ] FAIL — Score is downgraded without evidence; restore to HIGH

---

### Section 4 — Workaround Failure Modes

| # | Trigger | What goes wrong | User-visible symptom |
|---|---------|-----------------|----------------------|
| FM-01 | | | |
| FM-02 | | | |
| FM-03 (optional) | | | |

**Self-score C-05** (Failure modes identified):
- [ ] PASS — At least 2 rows with specific trigger and symptom
- [ ] FAIL — Generic pain points only; return and make concrete

---

### Section 5 — Conditions Under Which Inertia Loses

| # | Observable trigger | Why workaround fails at this trigger | What teams do instead |
|---|-------------------|--------------------------------------|-----------------------|
| CW-01 | | | |
| CW-02 | | | |
| CW-03 (optional) | | | |

**Self-score C-04** (Why inertia loses answered):
- [ ] PASS — At least 2 rows with falsifiable trigger
- [ ] FAIL — Vague conditions present; return and add observable triggers

---

### Section 6 — Composite Self-Score

| Criterion | Result |
|-----------|--------|
| C-01 Workaround mapped | PASS / FAIL |
| C-02 Costs quantified | PASS / FAIL |
| C-03 Threat score HIGH | PASS / FAIL |
| C-04 Why inertia loses | PASS / FAIL |
| C-05 Failure modes | PASS / FAIL |
| **All essential pass?** | YES / NO |

If any essential criterion is FAIL, revise the corresponding section before finalizing the artifact.

---

## V-03 — Lifecycle Emphasis: Maximum space on the inertia-lose conditions

**Variation axis**: Lifecycle emphasis — the "why inertia loses" phase receives 50% of the prompt's instruction space. Other phases are compressed.

**Hypothesis**: The central question is chronically underpowered in analyst outputs because the prompt doesn't proportionally emphasize it. Allocating most of the instruction budget there forces deeper analysis of what actually defeats inertia.

---

You are running `scout-inertia`. The output must answer: **why does inertia lose?**

Complete the following three phases.

---

### Phase 1 — Ground the workaround (brief)

Describe the current workaround in two to four sentences. Name the tool or process, who uses it, and how often. This is context — do not over-expand it.

---

### Phase 2 — Quantify switching costs (brief)

State the estimated cost across three dimensions: time per user, training hours, and workflow disruption (in sprint-days or people affected). Use numbers. Confirm the inertia threat score is HIGH.

---

### Phase 3 — Defeat analysis (primary)

This is the core of the artifact. Do not rush it.

#### 3a — Workaround failure modes

Map the specific ways the current workaround breaks. For each failure mode:

1. State the trigger condition exactly — what input, volume, edge case, or workflow event causes it.
2. Describe the failure observable — what the user sees or experiences.
3. Rate the failure frequency — does this happen once a month, once a quarter, or only at scale?
4. Assess the recovery cost — how long does it take to detect and repair the damage?

Identify at least two failure modes. Three is better. If you cannot find failures in the workaround, you are not looking at an inertia scenario — you are looking at a feature request.

#### 3b — Conditions under which inertia loses

For each failure mode above, ask: at what point does this failure become intolerable?

Write the condition as a threshold:
- "Teams switch when [failure mode X] occurs [N times / at scale Y / after event Z]."

Each condition must be falsifiable. A third party reading it must be able to observe whether the condition is met.

After writing conditions tied to failure modes, look for additional loss conditions not linked to failure:
- Is there an external forcing function? (regulation, platform change, team growth, new hire expectations)
- Is there a competitive event? (a peer team ships something; the workaround looks worse in comparison)
- Is there an internal tipping point? (team lead changes, knowledge holder leaves, workaround breaks for a VIP)

Write at least two total conditions (failure-mode-linked or forcing-function). Three or more is the target.

#### 3c — The inertia summary

Write one paragraph that directly answers the question: **why does inertia lose?**

The paragraph must:
- Reference the specific failure modes from 3a
- Name the conditions from 3b
- State what happens if none of the conditions are met (inertia wins; the feature is not adopted)

This paragraph is the artifact's conclusion. It should be written as if addressing a skeptical PM who asks: "Why wouldn't the team just keep using what they have?"

---

## V-04 — Phrasing Register: Direct imperative, conversational

**Variation axis**: Phrasing register — instructions use second-person direct commands, short sentences, conversational framing. No formal section headers with dashes. Tone is advisory, not bureaucratic.

**Hypothesis**: Formal/structured prompts can produce template-filling behavior where the analyst writes to satisfy the format rather than think. Conversational register encourages reasoning through the problem rather than checking boxes.

---

You're doing a scout-inertia analysis. The whole point is simple: figure out why a team would keep using what they already have instead of adopting this feature. Then figure out what breaks that.

Start by making sure you understand the workaround. Don't write "teams use a manual process" — that's not useful. Write down the actual thing they do. What tool? What file? Who does it — a PM, a developer, an ops person? How often — daily, before each release, ad hoc? What comes out of it — a spreadsheet, a Slack message, a ticket? Be specific enough that someone could recreate it.

Now switch gears and think about what it would cost that team to stop doing their current thing. Think about three angles: how long it takes each person to learn the new thing and migrate their data, how much training or ramp time is involved, and how much workflow churn happens while they're in transition. Put numbers on these — even rough ones. "About a day per developer" is better than "some time." Avoid just saying "high" with nothing behind it.

Set the inertia threat score to HIGH. It's almost always HIGH. The only reason to change it is if you have a concrete reason — not "the feature is better" but something like "the workaround was already failing at scale and teams were already planning to abandon it before this feature existed." If you don't have that, keep it HIGH.

Next, find where the workaround breaks. Think like a tester who's trying to make it fail. What's the edge case that causes data loss? What's the volume threshold where it starts producing errors? What workflow change makes it unworkable? Write down at least two specific failure modes. Not "it's slow" — what exactly slows down, and what's the consequence? Not "it doesn't scale" — at what scale does it break, and how do you know?

Now use those failure modes to answer the main question: when does a team decide to switch? Write the condition as a threshold you could observe. "Teams switch after the workaround drops data on files larger than 50MB for the third time" is good. "Teams switch when they realize the value" is useless. Give at least two switch conditions. Look for failure-mode triggers, but also look for external forcing functions — a new compliance requirement, a team lead who has low tolerance for manual work, a competitor team shipping something that changes the comparison.

Close with a short answer to the question: why does inertia lose? Write it as if you're explaining it to a skeptical PM who just said "my team has been using Excel for this for five years — why would they change now?" Make it concrete. Reference the failure modes. Reference the conditions. And if you can't write this paragraph convincingly, say so — it means the feature hasn't found its inertia-breaking condition yet.

---

## V-05 — Combined: Inertia-forward framing + table output

**Variation axis**: Inertia framing (prominent, adversarial) combined with table output format.

**Hypothesis**: Framing the entire analysis as "inertia is trying to win — your job is to find where it loses" creates an adversarial lens that produces more honest failure-mode identification. Combined with table output, it resists vague language at both the conceptual and formatting level.

---

You are conducting a `scout-inertia` analysis. Your frame: **inertia is the strongest competitor this feature has.** It costs nothing, requires no adoption, carries no risk of failure, and teams are already using it right now. Your job is not to sell the feature — your job is to find where inertia loses. If you cannot find that, the feature is not ready to ship.

Assume inertia wins until you find evidence otherwise.

---

### Inertia's current position — Workaround profile

Inertia is represented by the workaround. Describe it precisely.

| Field | Detail |
|-------|--------|
| What is the workaround? (tool / file / process name) | |
| What does it do? (data handled, action performed) | |
| Who runs it? (role) | |
| How often? | |
| What is its output artifact? | |

If you cannot fill this table with specifics, you do not know what you are competing against. Stop and gather more information.

---

### Inertia's switching moat — Cost to abandon the workaround

Every number in this table is a reason to stay. These are inertia's defenses.

| Defense | Estimate | Unit | Notes |
|---------|----------|------|-------|
| Time cost to migrate | | hours or days/user | |
| Training cost | | hours of training per user | |
| Workflow disruption | | sprint-days or people affected | |

Use numbers. Ranges are acceptable. "High" alone is not acceptable — it tells inertia nothing.

**Inertia threat score**: HIGH *(default; reduce only with documented evidence of active abandonment already in progress)*

---

### Inertia's weak points — Where the workaround fails

Inertia is not invincible. Find the cracks. For each failure mode, describe what cracks, when it cracks, what the user experiences, and how hard it is to recover.

| # | What cracks | Trigger | User-visible symptom | Recovery cost |
|---|-------------|---------|----------------------|---------------|
| FM-01 | | | | |
| FM-02 | | | | |
| FM-03 (optional) | | | | |

Generic entries ("it's slow", "it doesn't scale") do not qualify. The trigger must be specific and the symptom must be observable.

---

### Inertia's defeat conditions — When teams switch

Each failure mode above is a potential defeat condition. For inertia to lose, a team must cross a threshold where the workaround's cost exceeds the switching cost. Map those thresholds.

| # | Condition | Linked to failure mode? | Falsifiable? |
|---|-----------|------------------------|--------------|
| DC-01 | Teams switch when... | FM-__ / External | YES / NO |
| DC-02 | Teams switch when... | FM-__ / External | YES / NO |
| DC-03 (optional) | Teams switch when... | FM-__ / External | YES / NO |

Every condition in the "Falsifiable?" column must be YES. If it is NO, rewrite it until a third party could observe whether it has been met.

For conditions marked "External": identify the forcing function — regulation, platform shift, key-person departure, competitive event, team growth crossing a threshold.

---

### Verdict — Why inertia loses

Answer the question directly. Write two to four sentences. Reference the failure modes by ID. Reference the defeat conditions by ID. State what the feature must do to tip each condition.

> Inertia loses when [DC-01 and/or DC-02] because [FM-XX creates observable pressure at that threshold]. The feature wins by [what it must do that the workaround cannot]. If [conditions are not met], inertia wins and the feature does not get adopted regardless of quality.

If you cannot write this paragraph with specific references to your own tables, return to the failure modes section and find the crack you missed.

---

*End of V-01 through V-05 — scout-inertia R1*
