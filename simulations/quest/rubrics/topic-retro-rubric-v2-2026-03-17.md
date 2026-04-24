Written to `simulations/quest/rubrics/topic-retro-rubric-v2-2026-03-17.md`.

---

Here is the complete updated rubric:

---

```
---
skill: quest-rubric
skill_target: topic-retro
date: 2026-03-17
version: 2
prior_version: topic-retro-rubric-v1-2026-03-17.md
changes: |
  Round 1 excellence signals promoted to aspirational criteria.
  C-11: systemic-pattern-echo-field
  C-12: three-way-wrong-gap-echo-isolation
  C-13: inertia-framing-for-gaps
  Scoring formula denominator updated (4 applicable when no AMEND, 5 when AMEND).
---
```

# Scoring Rubric: topic-retro (v2)

Post-commitment retrospective on a topic's signals. Evaluates whether the output delivers
structured retrospective value: what signals were gathered, which predictions held, which
failed, what gaps mattered, and the one unexpected finding (the Echo).

---

## Essential Criteria (60 points total)

### C-01 -- Signal Accuracy Section Present
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Named section lists at least one signal by name with both prediction and actual outcome. List without the comparison fails.

### C-02 -- Correct/Wrong Verdict Per Signal
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Every signal carries a verdict label. Vague language without a clear verdict fails.

### C-03 -- Gaps Section Present and Actionable
- **Weight**: essential  **Category**: coverage
- **Pass condition**: At least one gap named with decision-impact statement. Gap without impact fails.

### C-04 -- Echo Present (One Unexpected Finding)
- **Weight**: essential  **Category**: depth
- **Pass condition**: Exactly one Echo, framed as unpredicted (not a restatement of a wrong prediction). Multiple echoes or restatements fail.

### C-05 -- Topic and Commitment Context Established
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Topic name and commitment nature stated in first two sections.

---

## Recommended Criteria (30 points total)

### C-06 -- Signal Coverage Summary
- **Weight**: recommended  **Category**: coverage
- **Pass condition**: Summary distinguishes "signals gathered" from "signals absent" across all 9 namespaces.

### C-07 -- Improvement Recommendation Tied to Gaps or Echo
- **Weight**: recommended  **Category**: depth
- **Pass condition**: Recommendation names the specific gap or Echo it addresses and specifies a practice change.

### C-08 -- Accuracy Rate or Ratio Stated
- **Weight**: recommended  **Category**: format
- **Pass condition**: Numerical accuracy summary (ratio or percentage) present in or immediately following the Signal Accuracy section.

---

## Aspirational Criteria (10 points total)

### C-09 -- Echo Linked to Systemic Pattern *(baseline)*
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Echo section names a pattern or prior instance. One-off without pattern linkage fails.

### C-10 -- AMEND Variants Handled Correctly *(AMEND only)*
- **Weight**: aspirational  **Category**: behavior
- **Pass condition**: If AMEND present, amended scope named and honored. N/A when no AMEND.

### C-11 -- Echo Classification Field Present *(systemic-pattern-echo-field, Round 1)*
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Echo section carries a discrete classification label in scannable form (e.g., `Class: assumption-held-past-expiry`). Prose that describes but does not label fails. Independent of C-09.
- **Why**: Turns the Echo into a taxonomy entry — compounding value across future topics, not episodic.

### C-12 -- Three-Way Isolation: Wrong / Gap / Echo *(three-way-wrong-gap-echo-isolation, Round 1)*
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Explicit statement that the Echo is neither a wrong prediction nor a gap. Structurally separate sections without explicit distinction fail.
- **Why**: Prevents classification drift into the Echo section; enforces definitional integrity across the skeleton.

### C-13 -- Inertia Framing for Gaps *(inertia-framing-for-gaps, Round 1)*
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: At least one gap entry names the prior assumption the missing signal would have confronted. "We lacked X data" without a belief anchor fails.
- **Why**: "Missing data" framing generates generic recommendations. Inertia framing generates targeted ones.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / applicable * 10)
```

- **No AMEND**: applicable = 4 (C-09, C-11, C-12, C-13)
- **AMEND present**: applicable = 5

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Trustworthy and actionable |
| Silver | >= 65, all essential pass | Useful but missing depth or coverage |
| Bronze | >= 50, all essential pass | Structurally valid, thin on insight |
| Fail | any essential fails | Not a valid retrospective |

---

**Key design notes for v2:**

- C-11 and C-09 are intentionally independent — linking the Echo to a class (C-11) and linking it to a prior instance (C-09) are different operations. Both can pass or fail separately.
- C-12 is labeled correctness despite being aspirational. It catches definitional drift that the essential criteria don't surface.
- C-13 does not add a gap-count requirement — one gap with inertia framing passes; five gaps with "we lacked X" framing fail.
icitly names the
  pattern or prior instance, not just the current observation. An Echo treated as a one-off
  without pattern linkage fails this criterion.

### C-10 -- AMEND Variants Handled Correctly
- **Weight**: aspirational
- **Category**: behavior
- **Pattern**: (conditional -- AMEND only)
- **Text**: When the skill is invoked with an AMEND modifier (focus on specific signal type,
  or adjusted time window), the output correctly scopes its analysis to the amendment without
  losing the structural skeleton (all three sections still present, even if narrowed).
- **Pass condition**: If an AMEND argument is provided, the amended scope is named in the
  preamble and the analysis stays within that scope. If no AMEND is provided, this criterion
  is N/A. An AMEND invocation that ignores the scope or drops required sections fails.

### C-11 -- Echo Classification Field Present
- **Weight**: aspirational
- **Category**: depth
- **Pattern**: systemic-pattern-echo-field (Round 1, V-03/V-04/V-05)
- **Text**: The Echo section contains a named classification field that assigns the Echo to a
  category of retrospective blind spot (e.g., "Class: assumption-held-past-expiry",
  "Class: signal-type-absent", "Class: late-stage-dependency"). A single sentence is
  sufficient; the requirement is that the label exists as a discrete, reusable field --
  not embedded in narrative prose.
- **Pass condition**: The Echo section (or immediately following it) carries an explicit
  classification label in a scannable form. Prose that describes the category without
  labelling it as a named field fails. The label must be distinct from the pattern linkage
  required by C-09 -- both can pass independently.
- **Why this matters**: A classification field turns the Echo from a one-topic observation
  into a taxonomy entry. Future topics can match against it, making the retrospective system
  compounding rather than episodic.

### C-12 -- Three-Way Isolation: Wrong / Gap / Echo
- **Weight**: aspirational
- **Category**: correctness
- **Pattern**: three-way-wrong-gap-echo-isolation (Round 1, V-05)
- **Text**: The output contains explicit language -- in the Echo section or in a structural
  preamble -- that distinguishes the Echo from both wrong predictions and from gaps. It is not
  sufficient to have three separate sections; the output must state why the Echo is neither
  a wrong prediction nor an unresolved gap.
- **Pass condition**: A direct statement of the form "this is not a wrong prediction (wrong
  predictions appear in Section X) and not a gap (gaps appear in Section Y)" or equivalent
  framing is present. Sections that are structurally separate but make no explicit
  distinction fail this criterion.
- **Why this matters**: Without the three-way distinction, models tend to migrate hard-to-
  classify items into the Echo section. The explicit isolation enforces definitional
  integrity across the retrospective skeleton.

### C-13 -- Inertia Framing for Gaps
- **Weight**: aspirational
- **Category**: depth
- **Pattern**: inertia-framing-for-gaps (Round 1, V-05)
- **Text**: Gaps are framed not merely as "signals that were absent" but as "signals that
  would have overcome the team's prior assumption or inertia" -- anchoring each gap to the
  specific belief state that existed before the commitment. A gap entry passes this criterion
  when it identifies what assumption the gap would have challenged, not just what information
  it would have added.
- **Pass condition**: At least one gap entry includes a prior-state anchor: the belief,
  assumption, or framing the team held before the commitment, and how the missing signal would
  have confronted it. A gap stated only as "we lacked X data" without naming the assumption
  it would have updated fails this criterion.
- **Why this matters**: "Missing data" framing produces generic recommendations ("gather more
  signals"). Inertia framing produces targeted ones ("run scout-feasibility before timeline
  commits when stakeholders have an existing vendor preference").

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / applicable * 10)
```

where `applicable` = number of aspirational criteria not marked N/A for this invocation:
- **No AMEND present**: applicable = 4 (C-09, C-11, C-12, C-13; C-10 is N/A)
- **AMEND present**: applicable = 5 (all criteria scored)

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Retrospective is trustworthy and actionable |
| Silver | >= 65, all essential pass | Useful but missing depth or coverage |
| Bronze | >= 50, all essential pass | Structurally valid, thin on insight |
| Fail | any essential fails | Output is not a valid retrospective |

---

## Notes for Evaluators

- C-01 through C-04 form the structural skeleton. A response missing any of the three named
  sections (Signal Accuracy, Gaps, Echo) automatically fails the corresponding essential.
- C-04 (Echo) is intentionally strict: the unexpected finding must be genuinely unpredicted.
  If a signal predicted X and X did not happen, that is a wrong prediction (C-02), not an
  Echo. The Echo is something no signal was even pointing at.
- C-10 is only scored when an AMEND modifier is present. Record it as N/A otherwise and use
  applicable = 4 in the scoring formula.
- C-11 and C-09 are independent: C-09 requires pattern linkage (connecting to a prior
  instance or broader class), C-11 requires a labelled classification field. A response can
  pass C-09 by naming a recurring pattern in prose while failing C-11 for lacking a discrete
  label, and vice versa.
- C-12 is a correctness criterion despite being aspirational. It penalises structural
  ambiguity that is not caught at the essential level.
- C-13 evaluates the quality of gap framing, not gap count. One gap with strong inertia
  framing passes; five gaps with "we lacked X" framing fail.
