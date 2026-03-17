---
skill: quest-rubric
skill_target: campaign-track
date: 2026-03-16
version: 1
---

# Scoring Rubric: campaign-track

**Skill description**: Run the full topic narrative campaign. Orchestrates: topic-new
(register), topic-roadmap (plan signals), topic-status (current coverage), topic-story
(narrative synthesis). Output: complete topic dashboard showing what signals exist, what
is missing, and the narrative arc. Use at the start and end of a signal-gathering session.

---

## Essential Criteria

**C-01 -- Orchestration sequence**
- Weight: essential
- Category: correctness
- Text: All four sub-skills are invoked in the correct order: topic-new (register) ->
  topic-roadmap (plan signals) -> topic-status (current coverage) -> topic-story
  (narrative synthesis). No sub-skill is skipped or reordered.
- Pass condition: Output explicitly names or traces all four sub-skill phases, in order,
  with each phase producing a distinct artifact or section. Any sub-skill omitted or
  invoked out of sequence fails this criterion.

**C-02 -- Topic registration artifact**
- Weight: essential
- Category: correctness
- Text: topic-new produces a registered topic entry and a strategy.md that lists planned
  signals with namespace, skill, item name, and priority (essential/recommended/optional).
  The strategy is the ground truth the rest of the campaign measures against.
- Pass condition: Output includes a strategy artifact (or a clear summary of it) listing
  at minimum 3 planned signals with namespace and priority. Absence of strategy fails
  this criterion.

**C-03 -- Coverage delta display**
- Weight: essential
- Category: coverage
- Text: topic-status shows a clear coverage picture: which planned signals have been
  collected, which are missing, and the ratio of collected to planned (e.g., 4/9 signals).
  The gap list must be specific -- named skills, not vague categories.
- Pass condition: Output contains a coverage table or list distinguishing collected vs
  missing signals, with named namespace/skill entries for each gap. A bare percentage
  without gap enumeration fails.

**C-04 -- Narrative synthesis present**
- Weight: essential
- Category: depth
- Text: topic-story synthesizes collected signals into a coherent editorial narrative --
  not a list of summaries. The narrative must express a working hypothesis (S0), how
  signals evolved it, and a verdict (PROCEED / PAUSE / PIVOT / ABANDON).
- Pass condition: Output contains a verdict section with one of the four verdict verbs
  plus a one-sentence directive, and at least one hypothesis mutation entry showing how
  a signal changed S0. Absence of verdict or absence of hypothesis evolution fails.

**C-05 -- Session-bookend utility**
- Weight: essential
- Category: behavior
- Text: The output is useful at both the start of a session (empty coverage, strategy
  defined) and the end of a session (coverage updated, narrative synthesized). The skill
  must handle the empty-signal case without crashing the narrative phase.
- Pass condition: If invoked with zero signals collected, topic-story still runs with
  S0 stated and gaps listed as all-open. If invoked with signals present, narrative
  reflects them. Refusing to run topic-story when no signals exist fails this criterion.

---

## Recommended Criteria

**C-06 -- Actionable next-signal recommendations**
- Weight: recommended
- Category: depth
- Text: The dashboard identifies which missing signals are highest priority to collect
  next, with namespace/skill names and rationale tied to open gaps in the narrative.
  "What to do next" is explicit, not left for the user to infer.
- Pass condition: Output contains a ranked or labeled list (at minimum top-3) of next
  signals to gather, each with namespace/skill and a one-sentence reason tied to a
  specific gap or verdict weakness.

**C-07 -- Coverage ratio and readiness statement**
- Weight: recommended
- Category: format
- Text: The dashboard includes a machine-readable or clearly scannable coverage ratio
  (e.g., "5 of 9 planned signals collected -- 56%") and an explicit readiness statement
  ("Ready for design commit" or "Not yet ready -- N blocking gaps remain").
- Pass condition: Output contains a numeric coverage ratio and a readiness verdict in
  a distinct labeled section. A narrative mention buried in prose without a label fails.

**C-08 -- Cross-namespace signal balance**
- Weight: recommended
- Category: coverage
- Text: topic-status calls out namespace-level distribution, flagging if coverage is
  heavily skewed toward one namespace (e.g., all signals from scout, none from prove or
  listen). Imbalance is surfaced, not silently accepted.
- Pass condition: Output includes a per-namespace coverage breakdown (even if brief) and
  flags any namespace with zero collected signals that has essential planned entries.

---

## Aspirational Criteria

**C-09 -- Echo integration**
- Weight: aspirational
- Category: depth
- Text: The narrative synthesis notes unexpected findings -- things learned that were not
  in the original strategy. These echoes (surprises, contradictions to S0) are called out
  distinctly from planned signal coverage, raising the story's epistemic value.
- Pass condition: Output contains at least one explicit echo entry: "We did not plan to
  learn X, but [artifact] revealed it." Absence of any unexpected finding synthesis
  does not fail essential/recommended but fails this criterion.

**C-10 -- Dual-session delta**
- Weight: aspirational
- Category: behavior
- Text: When invoked at the end of a session after having been invoked at the start, the
  output computes and surfaces the delta: which signals were added this session, how the
  verdict changed (if at all), and whether any gaps closed. The session is a traceable
  unit of progress.
- Pass condition: Output contains a session-delta section showing signals added this
  session (named) and a one-sentence verdict-change summary ("Verdict unchanged: PROCEED"
  or "Verdict updated from PAUSE to PROCEED because [gap closed]"). Only evaluable when
  two invocations exist for the same topic.

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

| Tier | Weight | Criteria |
|------|--------|----------|
| Essential | 60 pts | C-01, C-02, C-03, C-04, C-05 |
| Recommended | 30 pts | C-06, C-07, C-08 |
| Aspirational | 10 pts | C-09, C-10 |

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

**Minimum viable output**: C-01 + C-03 + C-04 must all pass for the output to be
considered usable at all. A dashboard with no coverage delta or no narrative verdict
is not a campaign output -- it is an incomplete run.
