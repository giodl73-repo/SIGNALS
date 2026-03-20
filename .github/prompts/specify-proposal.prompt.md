---
mode: agent
description: "Write a formal feature proposal — problem statement, proposed solution, why now, success criteria, stakeholders, risks, alternatives. Strategic alignm"
---
Topic: {topic}
Prior signals: [list any signals already gathered for this topic, or "none"]

---

## PHASE 1 — SIGNAL SCAN

Glob signals/**/{topic}-* to find any prior discovery for this topic.

| Signal file | Skill | Date | Key finding |
|-------------|-------|------|-------------|
| [path] | [skill] | [date] | [one-sentence finding] |
| ... | | | |

If no prior signals found: note "No prior signals — proposal will be grounded in stated
context only. Recommend running discover-competitors and discover-feasibility before finalizing."

Prior signal coverage: [STRONG (3+ signals) / PARTIAL (1-2 signals) / NONE]

---

## PHASE 2 — PROPOSAL

---

### Problem Statement

What are users doing today instead of this? Describe the current workaround in one paragraph.
Be specific: name the tool, the workflow step, the friction point. Avoid abstract framing.

[PROBLEM_STATEMENT]

---

### Proposed Solution

What we are building, in three sentences. Sentence 1: the capability. Sentence 2: the user
action that invokes it. Sentence 3: the outcome the user gets.

[PROPOSED_SOLUTION]

---

### Why Now

The trigger that makes this the right moment. Choose one primary trigger type and justify it:

| Trigger type | Active? | Evidence |
|-------------|---------|----------|
| Market shift | [YES / NO] | [cite signal or state observation] |
| User data | [YES / NO] | [cite signal or state observation] |
| Competitive move | [YES / NO] | [cite signal or state observation] |
| Platform change | [YES / NO] | [cite signal or state observation] |
| Internal driver | [YES / NO] | [state driver] |

Primary trigger: [trigger type — one sentence justifying why now vs. 6 months ago or later]

---

### Success Criteria

Three measurable outcomes. Each must be falsifiable: a number and a timeframe.

| Horizon | Outcome | Measurement |
|---------|---------|-------------|
| 30 days | [outcome] | [metric + target] |
| 60 days | [outcome] | [metric + target] |
| 90 days | [outcome] | [metric + target] |

North star metric: [the single metric that, if achieved, proves this proposal succeeded]

---

### Stakeholders

Who needs to be aligned before this proceeds?

| Role | Stake | Alignment needed | Veto? |
|------|-------|-----------------|-------|
| [role] | [what they care about] | [what they need to agree on] | [YES / NO] |
| [role] | [stake] | [alignment needed] | [YES / NO] |
| ... | | | |

Veto holders: [list roles with YES in Veto column. If none: "None identified."]

Critical alignment path: [which stakeholder must be aligned first, and why]

---

### Risks

Top three risks. Each risk must have a named mitigation — not "monitor closely."

| Rank | Risk | Likelihood | Impact | Mitigation |
|------|------|-----------|--------|------------|
| 1 | [risk] | [HIGH / MED / LOW] | [HIGH / MED / LOW] | [concrete mitigation] |
| 2 | [risk] | [HIGH / MED / LOW] | [HIGH / MED / LOW] | [concrete mitigation] |
| 3 | [risk] | [HIGH / MED / LOW] | [HIGH / MED / LOW] | [concrete mitigation] |

Highest-risk scenario: [the combination of risk + likelihood + impact that most threatens
the proposal. One sentence.]

---

### Alternatives Considered

At least two alternatives, including do-nothing. For each: what it is, why it was considered,
and why it was rejected.

| Alternative | Description | Why considered | Why rejected |
|-------------|-------------|----------------|--------------|
| Do nothing | [current state description] | [always baseline] | [cost of inaction — what gets worse] |
| [alt 2] | [description] | [reason considered] | [reason rejected] |
| [alt 3 — optional] | [description] | [reason considered] | [reason rejected] |

---

## PHASE 3 — ALIGNMENT CHECKLIST

Before this proposal moves to spec, the following teams need to sign off.

| Team | Question they need answered | Status |
|------|----------------------------|--------|
| Engineering | Is this feasible in the proposed scope? What is the rough effort? | [ ] Not started |
| Design | Is there a UX path that fits the existing product surface? | [ ] Not started |
| Legal | Does this touch data handling, compliance, or IP concerns? | [ ] Not started |
| Security | Are there auth or data exposure concerns in the proposed solution? | [ ] Not started |
| Support | Does this change existing behavior in ways that break user expectations? | [ ] Not started |

Minimum viable alignment: Engineering + one of (Design / Legal / Security) before spec writing.

---

## PHASE 4 — AMEND

AMEND mode: revisit a specific section with new information.

Section to amend: [problem-statement | proposed-solution | why-now | success-criteria |
                   stakeholders | risks | alternatives | alignment-checklist]
New information: [what changed]
Updated section: [rewrite only the named section]

---

Write artifact to: signals/specify/proposal/{topic}-proposal-{date}.md

Frontmatter:
```
skill: specify-proposal
topic: {topic}
date: {date}
```
