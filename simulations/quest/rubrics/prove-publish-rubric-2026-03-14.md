Rubric written to `simulations/quest/rubrics/prove-publish-rubric-2026-03-14.md`.

**10 criteria across 3 tiers:**

**Essential (5) — 60 pts:**
- C-01: All 8 sections present (format)
- C-02: Hypothesis resolved in Findings — confirmed/refuted/qualified (correctness)
- C-03: Evidence traceable to named artifacts (correctness)
- C-04: Findings are synthesized conclusions, not data restatements (depth)
- C-05: Principles are numbered, action-oriented rules (depth)

**Recommended (3) — 30 pts:**
- C-06: Panel review with 2+ named expert roles (coverage)
- C-07: Abstract standalone-useful in <200 words (format)
- C-08: Future Work has 2+ concrete investigable questions (coverage)

**Aspirational (2) — 10 pts:**
- C-09: Principles cross-referenced to findings by ID (depth)
- C-10: Cold-start readable — no undefined jargon, self-contained (behavior)

The key design choice: C-02 (hypothesis resolved) and C-03 (traceable evidence) guard against the most common failure mode for prove-publish — outputs that look like papers but are actually just narrative summaries disconnected from the actual investigation work.
"The hypothesis was confirmed: ...", "The hypothesis was refuted because ...",
  or "Partially confirmed under condition X but not Y"). Findings that never reference the
  hypothesis fail.

### C-03 - Evidence is traceable
- **Category**: correctness
- **Weight**: essential
- **Text**: Every claim in the Evidence section can be traced to a named artifact, source, or
  investigation output (file path, scorecard, interview ID, experiment result, etc.).
- **Pass condition**: Each evidentiary claim has at least one citation or reference anchor.
  General assertions with no backing ("we observed that...") fail this criterion.

### C-04 - Findings are synthesized conclusions, not raw data
- **Category**: depth
- **Weight**: essential
- **Text**: The Findings section contains interpreted conclusions drawn from evidence -- not a
  restatement or summary of the Evidence section. Findings answer "what does this mean?" not
  "what happened?".
- **Pass condition**: At least three distinct findings are present, each expressing a conclusion
  (a judgment, pattern, or causal claim) rather than an observation or data point.

### C-05 - Principles are extractable and reusable
- **Category**: depth
- **Weight**: essential
- **Text**: The Principles section contains numbered, action-oriented rules or heuristics that a
  future team can apply independently -- without reading the full paper.
- **Pass condition**: At least two principles are present. Each is phrased as a rule (imperative
  or conditional: "Always X", "When Y, do Z", "Prefer A over B because..."). Vague summaries
  ("this area is complex") fail.

---

## Recommended Criteria (weight: 30 -- improve quality)

### C-06 - Panel review with named expert roles
- **Category**: coverage
- **Weight**: recommended
- **Text**: The paper includes a simplified panel review section where at least two named expert
  roles (e.g. domain expert, skeptic, practitioner) provide critique, identify gaps, or assign
  a score.
- **Pass condition**: A review block is present with at least two distinct named reviewer
  perspectives. Each reviewer provides at least one substantive critique or endorsement, not just
  a score.

### C-07 - Abstract is standalone-useful
- **Category**: format
- **Weight**: recommended
- **Text**: The Abstract alone is sufficient for a reader to decide whether the paper is relevant
  to their question. It names the topic, the hypothesis, the method, and the key finding in
  under 200 words.
- **Pass condition**: A reader who reads only the Abstract can state: (a) what question was
  investigated, (b) how it was investigated, and (c) what was found. An abstract that merely
  describes structure ("this paper covers...") fails.

### C-08 - Future Work identifies concrete next questions
- **Category**: coverage
- **Weight**: recommended
- **Text**: The Future Work section lists specific, actionable next investigations -- not generic
  statements like "more research is needed."
- **Pass condition**: At least two future work items are phrased as investigable questions or
  proposed experiments, with enough specificity that a team could start them without further
  clarification.

---

## Aspirational Criteria (weight: 10 -- raise the bar)

### C-09 - Principles cross-referenced to findings
- **Category**: depth
- **Weight**: aspirational
- **Text**: Each principle in the Principles section is explicitly linked to the finding(s) that
  produced it (e.g. "Principle 1 [from F-02, F-05]: ..."). This creates a traceable chain from
  evidence to findings to principles.
- **Pass condition**: Every principle has at least one finding reference. Papers with unnumbered
  findings or unlinked principles fail.

### C-10 - New-team cold-start readability
- **Category**: behavior
- **Weight**: aspirational
- **Text**: The paper is self-contained enough that a team member with no prior context on this
  topic could read it and act on the principles without consulting the underlying investigation
  artifacts.
- **Pass condition**: The paper defines all domain-specific terms it uses, provides enough method
  context to understand why evidence was collected the way it was, and the Limitations section is
  honest about what the paper does not cover. Evaluated by attempting a cold read and checking
  for undefined jargon or unexplained jumps.

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band       | Score              | Meaning                          |
|------------|--------------------|----------------------------------|
| Golden     | >= 80, all E pass  | Publishable -- institutional memory |
| Passing    | >= 60, all E pass  | Usable with gaps                 |
| Needs work | Any essential fail | Not yet a paper                  |
| Failing    | < 40               | Restart recommended              |
