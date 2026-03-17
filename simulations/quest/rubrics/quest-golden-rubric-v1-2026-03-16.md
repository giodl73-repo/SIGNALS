---
skill: quest-rubric
skill_target: quest-golden
date: 2026-03-16
version: 1
---

# quest-golden Scoring Rubric — v1

**Purpose:** Objective function for quest:golden runs targeting the quest-golden skill.
Criteria define what a correct, high-quality quest-golden execution looks like.
The rubric grows as quest:golden discovers excellence patterns (QU3 additions).

---

## Essential Criteria (weight 1.0 — all must pass)

**C-01 — Dual convergence termination**

Without dual convergence conditions at loop exit, the loop can terminate on a single signal
and miss the distinction between "all scenarios pass" and "no new excellence remains to
discover," because passing all rubric criteria is a necessary but not sufficient condition
for a stable golden prompt. Not "stopping when all variations score well," but "stopping only
when BOTH trial convergence (all essential criteria pass across variations) AND quest
convergence (two consecutive rounds with zero new excellence patterns) are simultaneously true."

- **Weight:** essential
- **Category:** correctness
- **Pass:**
  LOCATION: loop termination logic or convergence check section.
  OBSERVABLE: explicit check for (1) all scenarios pass all essential criteria AND (2) no new
  excellence patterns found in this round AND the immediately preceding round; both conditions
  stated as required simultaneously.
  STANDARD: both conditions present in the same termination gate; single-condition termination
  or absence of either = FAIL.

---

**C-02 — Golden prompt written as full skill body**

Without writing the converged prompt body verbatim as the golden prompt, the loop produces a
variation history but no deployable artifact, because the golden prompt is the skill body, not
a variation label or a summary. Not "identifying the best variation by name," but "emitting the
converged prompt body in full as a standalone, runnable artifact for the target skill."

- **Weight:** essential
- **Category:** correctness
- **Pass:**
  LOCATION: golden output section (only at dual convergence).
  OBSERVABLE: complete prompt body written out in full, not summarized; labeled as the golden
  prompt; written to a named file at simulations/quest/golden/{skill}-golden-{date}.md.
  STANDARD: full verbatim body present; reference-only ("see V-03") or summary-only = FAIL.

---

**C-03 — Final rubric written as standalone artifact**

Without writing the final rubric, the theory of excellence is lost after the session ends,
because only the example remains and the next maintainer cannot know what each criterion
discovered or why it was added. Not "listing criteria inline," but "emitting the accumulated
rubric as a separate versioned file with all converged criteria, composite formula, denominator,
and golden threshold."

- **Weight:** essential
- **Category:** correctness
- **Pass:**
  LOCATION: final artifacts section (only at dual convergence).
  OBSERVABLE: rubric document written to simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
  containing all criteria, composite formula, denominator, and golden threshold.
  STANDARD: standalone artifact present; embedding criteria only inside the golden file = FAIL.

---

**C-04 — Excellence signal extraction (QU2) precedes criterion proposal (QU3)**

Without QU2 preceding QU3, proposed criteria are not grounded in observed output differences,
because a criterion that does not trace back to a measured output gap is an editorial guess,
not a discovered signal. Not "proposing criteria based on domain knowledge," but "extracting
the pattern from the observed gap between top and next-highest variation before writing any
criterion text."

- **Weight:** essential
- **Category:** behavior
- **Pass:**
  LOCATION: each round where a criterion is proposed.
  OBSERVABLE: QU2 extraction section naming (a) which variation pair showed the gap and
  (b) the observable output difference, appearing before QU3 criterion text in that round.
  STANDARD: QU2 populated before QU3 in every round with a criterion proposal; QU3 without
  preceding QU2 = FAIL for that round.

---

**C-05 — Rubric present at loop start (loaded or created)**

Without a rubric as the scoring objective function before the first score step, variation
rankings have no grounded standard and excellence signals cannot be derived from criterion
gaps. Not "scoring by qualitative judgment," but "loading an existing rubric for the target
skill or creating one via quest:rubric before the first variation is scored."

- **Weight:** essential
- **Category:** correctness
- **Pass:**
  LOCATION: loop initialization.
  OBSERVABLE: rubric artifact reference (loaded filename or creation confirmation) present
  before first score step.
  STANDARD: rubric present at loop start; scoring without a rubric reference = FAIL.

---

## Recommended Criteria (weight 0.5 — output is better with these)

**C-06 — Per-round iteration record**

Without a per-round iteration record, convergence cannot be audited, because the reader
cannot verify that dual convergence conditions were actually met or trace which excellence
signals produced which rubric additions. Not "summarizing results at the end," but "recording
each round's variation IDs, scores, named excellence signal (or explicit 'no new signal'),
and rubric delta (criterion added or none) as a navigable history."

- **Weight:** recommended
- **Category:** coverage
- **Pass:**
  LOCATION: iteration history section or per-round log.
  OBSERVABLE: entry per round with (a) variation IDs scored, (b) top composite score,
  (c) excellence signal name or "none," (d) criterion added or "none."
  STANDARD: >= 1 entry per round executed; missing any of the four fields = suboptimal.

---

**C-07 — Excellence signal isolation (not just top-variation properties)**

Without excellence signal isolation, the extracted pattern names what the best variation
contains rather than what made it better than its nearest competitor, because shared
properties of all high-scoring variations are not signals of excellence. Not "listing
properties of the top variation," but "differentiating the top variation's winning property
from properties shared by all variations at the same score level."

- **Weight:** recommended
- **Category:** depth
- **Pass:**
  LOCATION: QU2 extraction for each round with a proposed criterion.
  OBSERVABLE: contrast statement naming what the top variation had that the next-highest
  variation lacked (e.g., "V-03 had X; V-01 and V-02 did not").
  STANDARD: isolation contrast present; listing top-variation properties without a contrast
  against the next-highest = FAIL.

---

**C-08 — Criterion proposal includes tier and pass condition**

Without tier assignment and a pass condition in criterion proposals, the proposed criterion
is incomplete and cannot be integrated into the rubric without editorial judgment, because
tier determines score weight and the pass condition determines whether the criterion is
evaluable. Not "proposing criterion text alone," but "proposing criterion text with tier
(essential/recommended/aspirational) and a slot-filled pass condition."

- **Weight:** recommended
- **Category:** format
- **Pass:**
  LOCATION: QU3 criterion proposal.
  OBSERVABLE: three fields present — text, tier, pass condition — in each criterion proposal.
  STANDARD: all three present; missing any one = suboptimal.

---

## Aspirational Criteria (weight 0.25 — raise the bar once essential/recommended are stable)

**C-09 — "What made it golden" mechanism narrative**

Without a mechanism narrative accompanying the golden prompt, the golden prompt is an example
without a theory, because the structural discoveries made during the loop are not explained
and the next maintainer cannot know which decisions were load-bearing. Not "emitting the
converged prompt body alone," but "accompanying it with a named section explaining each
structural mechanism discovered, which round found it, and what output gap it closed."

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: golden prompt output, adjacent to the prompt body.
  OBSERVABLE: named section (e.g., "What Made It Golden") with >= 2 mechanism descriptions;
  each citing (a) the round it was discovered and (b) the output gap it closed.
  STANDARD: mechanism descriptions with round citations present; generic praise without
  round citation = FAIL.

---

**C-10 — Persistent gap identification (ablated criteria)**

Without persistent gap identification, the rubric presents a false ceiling, because criteria
that were proposed but never activated across all rounds represent open hypotheses — not
settled knowledge — and the next round's designer needs to know they exist. Not "emitting
only active criteria," but "naming criteria with zero activations across all rounds as ablated,
with a suggested targeted probe approach."

- **Weight:** aspirational
- **Category:** coverage
- **Pass:**
  LOCATION: final rubric or convergence output.
  OBSERVABLE: named section or annotation for criteria with zero activations across all rounds;
  each ablated criterion named with a suggested probe; OR explicit "no ablated criteria"
  statement if none exist.
  STANDARD: present if any criteria were ablated; omission without a "none" declaration = FAIL.

---

## Scoring

**Composite formula:**

```
Score = (essential_pass / 5)   * 60
      + (recommended_pass / 3) * 30
      + (aspirational_pass / 2) * 10
```

**Tier table:**

| Tier         | Weight | Count | Max contribution |
|--------------|--------|-------|-----------------|
| Essential    | 1.0    | 5     | 60              |
| Recommended  | 0.5    | 3     | 30              |
| Aspirational | 0.25   | 2     | 10              |
| **Total**    |        | **10**| **100**         |

**Golden threshold:** All 5 essential criteria pass AND composite >= 80

**PARTIAL:** Score = 70–79.
Earn conditions: all 5 essential pass + exactly 1 of 3 recommended pass (composite = 70).
A partial output has the loop structure correct but missing iteration record, signal
isolation, or criterion completeness. Partial is not golden.

**FAIL:** Any essential criterion fails (composite irrelevant).

---

## Version History

| Version | Date       | Criteria   | Change                          |
|---------|------------|------------|---------------------------------|
| v1      | 2026-03-16 | C-01..C-10 | Initial rubric from /quest:rubric |
