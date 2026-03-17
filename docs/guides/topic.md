# topic — Coverage Tracking and Narrative Synthesis

## The short version

The topic namespace manages the investigation narrative. Six skills: open a topic, check
status, write a report, update the strategy, synthesize everything into a story, and surface
unexpected findings as an echo. topic is the namespace that answers "are we ready to commit?"

---

## When to use this namespace

Use topic at the start of an investigation to register it, during the investigation to check
coverage, and at the end to synthesize the signals into a decision.

- You are starting a new feature investigation and want to register it with a strategy.
- You want to know which namespaces have coverage and which are missing.
- You want a shareable status report for a standup or stakeholder update.
- The investigation has gathered enough signals and you want to synthesize them into a decision.
- You want to capture what the investigation found that you did not expect.

Every skill writes standalone. But without topic-new, there is no strategy to check coverage
against. Without topic-status, you do not know when you are done. Without topic-story, the
signals are a pile of artifacts without a narrative.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `topic-new` | Registers the topic in TOPICS.md, creates strategy.md with planned signals, namespace coverage plan, owner roles, and priorities. | First step in any planned investigation. |
| `topic-status` | Shows current signal coverage, gaps, and readiness in the terminal. Does NOT write a file. Globs all signals, cross-references strategy. | Anytime during an investigation. "Am I done?" |
| `topic-report` | Same as topic-status but writes a shareable file. --format teams produces compact ASCII for paste into Teams/standup. | When you need a written status artifact for stakeholders. |
| `topic-plan` | Revises the strategy as the investigation evolves. Reads current strategy.md and all gathered signals. Proposes additions, removals, re-prioritizations. | When new signals reveal unexpected dimensions that need coverage. |
| `topic-story` | Synthesizes all signals into a narrative: what we investigated, what each signal revealed (key finding), what the signals say together, what remains uncertain, and the recommendation. | When the investigation is complete enough for a decision. |
| `topic-echo` | Synthesizes unexpected findings only: "What did we learn that we did not expect?" Each surprise named, traced to source signal, assessed for design impact. | After all essential signals are in. Always the final step. |

---

## Example workflow

You are investigating "payment-reminders" from the start.

**Step 1: Open the topic.**

```
/topic-new payment-reminders
```

Creates `simulations/TOPICS.md` entry. Creates `simulations/payment-reminders/strategy.md`
with a planned signal list: scout-competitors (essential, PM), scout-feasibility (essential,
Architect), draft-spec (essential, PM+Arch), review-design (recommended, Team), flow-lifecycle
(recommended, Dev), listen-adoption (optional, PM).

**Step 2: Run some skills. Check status.**

After running scout-competitors, scout-feasibility, and draft-spec:

```
/topic-status payment-reminders
```

```
topic: payment-reminders
strategy: 6 signals planned
found:    3 signals

  ESSENTIAL (must have)
    [x] scout-competitors    payment-reminders-competitors-2026-03-16.md
    [x] scout-feasibility    payment-reminders-feasibility-2026-03-16.md
    [x] draft-spec           payment-reminders-spec-2026-03-16.md

  RECOMMENDED
    [ ] review-design        not found
    [ ] flow-lifecycle       not found
    [ ] listen-adoption      not found

  COVERAGE: 50% -- not ready for design commit
```

**Step 3: After reaching coverage, synthesize.**

```
/topic-story payment-reminders
```

Synthesizes: "We set out to determine whether automated payment reminders could reduce
days-to-pay by 25%. Scout found the primary threat is the existing spreadsheet workflow.
Feasibility found a throttle constraint requiring batching design. Prove found timing is
the critical variable. Listen found two adoption blockers: no org policy controls, no audit
log. Together the signals say: build it, but address the audit log and policy controls before
ship. Recommendation: PROCEED with two pre-ship spec updates."

**Step 4: Capture the unexpected.**

```
/topic-echo payment-reminders
```

Surprises: (1) Enterprise accounts show no benefit from automated reminders -- a finding
that contradicts the hypothesis for that segment. (2) The prove-interview simulation revealed
that Finance Admins want reminder preview before sending -- no signal anticipated this.

---

## What it produces

topic artifacts write to `simulations/{topic}/` and `simulations/TOPICS.md`:

```
simulations/
  TOPICS.md                               registry of all topics
  payment-reminders/
    strategy.md                           investigation plan
    status-2026-03-16.md                  topic-report output
    payment-reminders-story-2026-03-16.md topic-story output
    payment-reminders-echo-2026-03-16.md  topic-echo output
```

Example frontmatter for topic-story:

```yaml
---
skill: topic-story
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**topic-echo is always the last step.** topic-echo asks "what did we learn that we did not
expect?" It cannot produce useful output until the essential signals are gathered. Running
it early produces a shallow echo. Running it last produces institutional memory -- the record
of surprises that the next team inherits.

**topic-story is not a summary.** topic-story is an editorial synthesis. Do not use it to
summarize each signal -- that produces a list, not a narrative. Use it to interpret what
the signals say together. The synthesis is the decision artifact; the individual signals
are the evidence.

**topic-plan is the course-correction tool.** If a signal reveals an unexpected dimension,
run topic-plan to revise the strategy. The strategy.md is a living document, not a contract.
topic-plan keeps it aligned with what the investigation has actually found.

---

## What's next

- **[program](program.md)** -- plan the investigation stages before running skills.
- **[prove](prove.md)** -- topic-echo often surfaces hypotheses worth testing. Run prove after the echo.
- **[corp](corp.md)** -- for features with org-level decision requirements, topic-story feeds into corp-rob.
- **[ACHIEVEMENTS](../ACHIEVEMENTS.md)** -- Full Coverage and Pre-Commitment Ready are earned through topic-status milestones.
