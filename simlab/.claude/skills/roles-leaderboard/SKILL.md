---
name: roles-leaderboard
description: Team achievement leaderboard across all topics and contributors. Scans all signals/ artifacts, ranks contributors by achievements, shows team milestones and coverage gaps. DISPLAY ONLY — writes no files.
allowed-tools: [Read, Glob]
param_set: lean
---

You are running /roles-leaderboard for this workspace.

Scan ALL signals/ directories for signal artifacts across all topics and contributors.
DISPLAY ONLY — write no files.

---

## STEP 1: Inventory

Find all signal artifact files: signals/**/*-*-*.md
Extract: contributor (from frontmatter author field if present), topic, skill, date.
Group by contributor. If no author metadata, treat as "team" contributions.

---

## STEP 2: Compute per-contributor achievement counts

For each contributor, count achievements earned across ALL their topics using the same
criteria as /achievements (dual-prefix namespace scanning for compatibility).

---

## STEP 3: Compute team-level metrics

COVERAGE GAPS — namespaces nobody has run:
- List any of the 9 namespaces (discover/specify/validate/simulate/trace/prove/listen/rhythm/roles)
  where ZERO artifacts exist across all contributors and topics.

TEAM MILESTONES:
- [ ] First Team Signal — 2+ contributors have artifacts
- [ ] Shared Coverage — any topic with 5+ namespaces covered by 2+ contributors
- [ ] Debate Starter — same topic, same skill, different contributors (shows evidence diversity)

---

## STEP 4: Display leaderboard

```
Signal Team Leaderboard
================================================================

CONTRIBUTORS (ranked by achievements):
  1. [name]     [N] achievements  [top achievement]
  2. [name]     [N] achievements  [top achievement]
  ...

TEAM MILESTONES:
  [x] First Team Signal
  [ ] Shared Coverage -- closest: [topic] needs [contributor] to run [namespace]

COVERAGE GAPS (namespaces nobody has touched):
  -> [namespace]: suggested first skill: /[skill] [topic]

TOP TOPICS BY COVERAGE:
  [topic]: N/9 namespaces | [contributor list]

RECOMMENDED NEXT:
  For [contributor]: /[skill] [topic] -- unlocks [achievement] + fills [gap]
================================================================
```

If no artifacts exist yet: show empty leaderboard with "Start your first session: /discover-competitors <your-feature>"
