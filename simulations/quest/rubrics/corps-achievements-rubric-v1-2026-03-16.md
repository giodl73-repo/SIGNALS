---
skill: quest-rubric
skill_target: corps-achievements
date: 2026-03-16
version: 1
---

# Scoring Rubric: corps-achievements

Scores output from the `corps-achievements` skill, which scans signal artifacts across all
topics in a workspace and computes team-level achievements: earned achievements by topic and
contributor, team milestones, contributor leaderboard, and recommended next actions.

---

## Criteria

### ESSENTIAL

**C-01 | Artifact scan grounded in workspace state**
- Weight: essential
- Category: correctness
- Pass condition: Output references the actual signal artifacts found in the workspace (files
  cited match files that exist under `simulations/`), OR workspace is correctly reported as
  empty/sparse. Output must not invent topics or contributors not present in the repo.

**C-02 | All discovered topics represented**
- Weight: essential
- Category: coverage
- Pass condition: Every topic discovered during the scan appears in the achievements section
  (even if as "no achievements earned yet"). No topic found in `simulations/` is silently
  omitted.

**C-03 | Three named team milestones reported**
- Weight: essential
- Category: correctness
- Pass condition: Output contains a dedicated milestones section that addresses all three
  named milestones by name: "first team signal", "shared coverage", "debate starter".
  Each milestone is labeled earned or not-yet-earned. A section that only lists some of the
  three does not pass.

**C-04 | Contributor leaderboard present**
- Weight: essential
- Category: format
- Pass condition: A leaderboard section exists, ranks contributors by signal contribution
  (count or weighted), and includes at least one entry. If no contributors are detectable,
  output states this explicitly rather than omitting the section.

**C-05 | Next actions present and achievement-linked**
- Weight: essential
- Category: behavior
- Pass condition: Output contains at least two recommended next actions, and each action
  names the specific achievement it would unlock. Generic advice ("add more signals") does
  not pass; action must specify namespace, topic, or milestone target.

---

### RECOMMENDED

**C-06 | Earned vs. available achievements visually separated**
- Weight: recommended
- Category: format
- Pass condition: Output clearly distinguishes earned achievements (already unlocked) from
  available achievements (criteria met but not credited, or not yet met). A flat list with
  no distinction does not pass.

**C-07 | Achievement taxonomy with at least two categories**
- Weight: recommended
- Category: depth
- Pass condition: Achievements are grouped into at least two distinct categories (e.g.,
  by namespace, coverage depth, collaboration type, or milestone class). A flat, uncategorized
  list of achievements does not pass.

**C-08 | Sprint or cadence framing**
- Weight: recommended
- Category: format
- Pass condition: Output includes a date or sprint label, and uses cadence-appropriate
  framing ("this sprint", "week of ...", "since last run") somewhere in the summary or
  intro. Output that reads as a static, timeless report does not pass.

---

### ASPIRATIONAL

**C-09 | Close-to-unlock signals ("1 away" callouts)**
- Weight: aspirational
- Category: depth
- Pass condition: Output identifies at least one achievement or milestone that is close to
  being earned (e.g., "Team needs 1 more contributor signal in `scout` to unlock Shared
  Coverage") with the specific gap quantified. Output that only lists what is earned, not
  what is close, does not pass.

**C-10 | Cross-topic or cross-contributor insight**
- Weight: aspirational
- Category: depth
- Pass condition: Output surfaces at least one explicit cross-topic or cross-contributor
  pattern as a named insight (e.g., "Alice spans 4 topics -- highest breadth on the team",
  or "The `flow` namespace has 100% team participation -- only namespace with this"). A
  simple list of per-topic stats does not pass; the insight must be stated as a sentence
  drawing a conclusion.

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

| Threshold | Meaning |
|-----------|---------|
| All 5 essential pass AND composite >= 80 | Golden |
| All 5 essential pass AND composite < 80 | Passing (recommended/aspirational gaps) |
| 4 essential pass | Near-miss -- one essential gap |
| < 4 essential pass | Failing -- output not usable |

---

## Notes for Scorers

- C-01 correctness check: glob `simulations/**/*` and verify any topics named in the output
  exist as directories or files. A hallucinated topic name is a hard C-01 fail.
- C-03 milestone check: look for all three terms by name. A synonym (e.g., "first signal
  posted") without naming the milestone is insufficient.
- C-05 action quality: an action passes if it has both a verb ("add a scout signal for X")
  and names the achievement it targets ("to unlock Shared Coverage").
- C-09 quantification: "1 more signal" or "2 contributors short" are both passing forms.
  "Almost there" without a number is not.
