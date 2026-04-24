---
skill: trace-skill
topic: plugin
item: prove-hypothesis
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-prove-2026-03-14.md
---

# /trace-skill -- prove-hypothesis

**Invocation**: `/prove-hypothesis "Signal's zero-config first-run works for a Dynamics developer with no prior context"`
**Scenario**: PM using prove-hypothesis as the entry point to a prove investigation

## Phase 1: Setup

No prior prove artifacts for this topic. Starting fresh.
The skill must produce: a stated hypothesis, falsification condition, confidence level,
and a list of experiments that will test it.

## Phase 2: Execute

```
# Hypothesis: Signal Zero-Config First-Run

**Claim**: A Dynamics 365 developer who has never heard of Signal can install it,
run /scout-competitors on their current feature, and get a useful competitive brief
within 15 minutes -- without reading any documentation.

**Falsification condition**: The hypothesis is false if ANY of:
- Developer cannot find where to copy the SKILL.md file without asking someone
- Developer cannot invoke the skill without reading the SKILL.md source
- The output is generic enough that the developer says "this isn't about my feature"
- The whole process takes more than 15 minutes

**Confidence**: 60/100
Why 60: The install step requires knowing what .claude/skills/ is. Our review:users
trace showed Maker needed developer help. Dynamics devs are more technical but this
is still a step that could break.

**Experiments to run**:
1. prove:interview -- simulate 3 Dynamics developers going through the install cold
2. prove:prototype -- write a signal-install.sh and test the install time
3. prove:analysis -- analyze the review:users trace findings for install friction data
```

## Phase 3: Findings

The hypothesis is well-formed: specific claim, clear falsification conditions,
honest confidence level, concrete experiments.

Key strength: the falsification conditions are testable (15-minute timer, "not about
my feature" subjective test). Most hypotheses fail to specify what would falsify them.

One gap: no prior signal data loaded (no prior prove runs on this topic). The skill
should explicitly note: "No prior investigation signals found. Starting from scratch."

## Phase 4: Amend

1. Add `--confidence [0-100]` flag so the PM can declare their prior belief explicitly
2. Add explicit "what would confirm this" alongside "what would falsify this"
3. The falsification conditions are good -- the spec should make them required, not optional

## Verdict

**Result**: USEFUL. prove-hypothesis works as an investigation entry point.
The scientific method framing (claim, falsification, experiments) is the right discipline.

### Findings Register
| ID | Finding | Severity |
|----|---------|----------|
| SF-01 | No "no prior signals" explicit note in spec | MINOR |
| SF-02 | --confidence flag missing (implicit confidence is vague) | MINOR |
| SF-03 | "What would confirm" is implicit -- should be explicit alongside falsification | MINOR |
| SF-04 | Hypothesis-first discipline immediately useful for PM audience -- delight | DELIGHT |
