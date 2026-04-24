Written to `simulations/quest/rubrics/campaign-track-rubric-v2-2026-03-16.md`. Here is the complete updated rubric:

---

```
---
skill: quest-rubric
skill_target: campaign-track
date: 2026-03-16
version: 2
---
```

# Scoring Rubric: campaign-track

**Skill description**: Run the full topic narrative campaign. Orchestrates: topic-new (register), topic-roadmap (plan signals), topic-status (current coverage), topic-story (narrative synthesis). Output: complete topic dashboard showing what signals exist, what is missing, and the narrative arc. Use at the start and end of a signal-gathering session.

---

## Essential Criteria

**C-01 -- Orchestration sequence** | essential | correctness
All four sub-skills invoked in order. Pass: explicit phase trace with distinct artifact per phase.

**C-02 -- Topic registration artifact** | essential | correctness
strategy.md with >= 3 planned signals, namespace, and priority. Pass: strategy artifact present with namespace/priority fields.

**C-03 -- Coverage delta display** | essential | coverage
9-namespace coverage table: planned / collected / missing, named gaps. Pass: table present with named namespace/skill gap entries.

**C-04 -- Narrative synthesis present** | essential | depth
Verdict verb from controlled vocabulary + hypothesis mutation block. Pass: verdict verb + at least one S0 mutation entry.

**C-05 -- Session-bookend utility** | essential | behavior
Handles both empty (0 signals) and populated state. Pass: zero-signal case runs topic-story with NOT YET REACHED verdict; populated case reflects signals.

---

## Recommended Criteria

**C-06 -- Actionable next-signal recommendations** | recommended | depth
Top-3 next signals, each with namespace/skill + gap reason.

**C-07 -- Coverage ratio and readiness statement** | recommended | format
Numeric ratio (X/N) + labeled readiness verdict (READY / NOT READY / CONDITIONALLY READY).

**C-08 -- Cross-namespace signal balance** | recommended | coverage
Per-namespace breakdown; zero-signal namespaces flagged explicitly.

---

## Aspirational Criteria

**C-09 -- Echo integration** | aspirational | depth
Unexpected findings called out distinctly from planned coverage.

**C-10 -- Dual-session delta** | aspirational | behavior
Session delta section: signals added, verdict change summary.

**C-11 -- Role-gated phases** *(new, from V-01 excellence)* | aspirational | correctness
Each phase assigns a distinct named AI persona (Registrar / Planner / Analyst / Narrator). Pass: four distinct role labels, consistent assignment — Registrar does not synthesize, Narrator does not plan. Generic "Assistant" labels fail.

**C-12 -- Explicit progression gates** *(new, from V-01 excellence)* | aspirational | behavior
Phase ordering enforced as a hard constraint via "do not proceed until [artifact X] is written" gates. Pass: at least one explicit gate statement between adjacent phases. A bare numbered list with no gating language fails.

**C-13 -- Empty-state as named section** *(new, from V-01 excellence)* | aspirational | behavior
Zero-signal first-invocation documented as a dedicated labeled section (e.g., "Empty State Handling") addressing each phase individually. Pass: distinct section present with per-phase behavior. A single buried sentence fails.

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

| Tier | Weight | Criteria |
|------|--------|----------|
| Essential | 60 pts | C-01 through C-05 |
| Recommended | 30 pts | C-06, C-07, C-08 |
| Aspirational | 10 pts | C-09, C-10, C-11, C-12, C-13 |

**Golden threshold**: All 5 essential pass AND composite >= 80.

**Minimum viable output**: C-01 + C-03 + C-04 must all pass.

---

The key change from v1: aspirational tier grows from 2 to 5 criteria, denominator in the formula updates from `/2` to `/5`. The three additions directly encode the structural techniques that made V-01 a perfect-score response.
gory: format
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

**C-11 -- Role-gated phases**
- Weight: aspirational
- Category: correctness
- Text: Each orchestration phase assigns a distinct named AI persona (e.g., Registrar,
  Planner, Analyst, Narrator), creating a structural contract that prevents role bleed.
  A phase cannot editorialize during registration or summarize during narration because
  the named role makes crossing that boundary a declared violation.
- Pass condition: Output names a distinct role or persona per phase (four distinct labels
  minimum) and the persona assignments are consistent -- the Registrar does not synthesize,
  the Narrator does not plan. Generic role labels ("Assistant") do not satisfy this
  criterion.

**C-12 -- Explicit progression gates**
- Weight: aspirational
- Category: behavior
- Text: The skill enforces phase ordering as a hard constraint, not merely a suggestion.
  Each phase includes an explicit "do not proceed until [artifact X] is written" gate
  that prevents phases from running in parallel or silently skipping when an artifact
  is absent.
- Pass condition: Output contains at least one explicit gate statement (or equivalent
  structured checkpoint) between adjacent phases. A numbered list of steps with no
  gating language does not satisfy this criterion; the gate must be expressed as a
  conditional or a named prerequisite artifact check.

**C-13 -- Empty-state as named section**
- Weight: aspirational
- Category: behavior
- Text: Zero-signal first-invocation behavior is documented as a named, first-class
  section -- not an inline caveat or a parenthetical note. The section specifies exactly
  how each phase behaves when no signals have been collected yet (e.g., Phase 3 shows
  all rows at 0, Phase 4 produces a skeleton with verdict = NOT YET REACHED).
- Pass condition: Output contains a distinct labeled section (e.g., "Empty State
  Handling" or "First-Invocation Behavior") that addresses each phase individually.
  A single sentence such as "works with no signals" buried in the description does not
  satisfy this criterion.

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

| Tier | Weight | Criteria |
|------|--------|----------|
| Essential | 60 pts | C-01, C-02, C-03, C-04, C-05 |
| Recommended | 30 pts | C-06, C-07, C-08 |
| Aspirational | 10 pts | C-09, C-10, C-11, C-12, C-13 |

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

**Minimum viable output**: C-01 + C-03 + C-04 must all pass for the output to be
considered usable at all. A dashboard with no coverage delta or no narrative verdict
is not a campaign output -- it is an incomplete run.
