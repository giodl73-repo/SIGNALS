Written to `simulations/quest/rubrics/prove-publish-rubric-v2-2026-03-14.md`.

---

**Three new aspirational criteria extracted from R1 excellence signals:**

| ID | Name | Source signal | Why it's new |
|----|------|--------------|--------------|
| C-11 | Findings classified by novelty | V-05 BASELINE MATCH / NEW SIGNAL tagging (C-04 PASS) | Forces authors to label what actually changed — beyond synthesis quality |
| C-12 | Status Quo section | V-05 "gives new readers context they'd otherwise infer" (C-10 PASS) | A structural section, not just readability — makes contribution legible by contrast |
| C-13 | Citation audit precedes Findings | V-03 "Citation-audited before Findings begins" (C-03 PASS) | Lifecycle gate, not content check — blocks rationalization drift at the source |

**Scoring formula updated:**
- Aspirational pool stays 10 pts total
- Now distributed across 5 criteria at 2 pts each (was 2 criteria at 5 pts each)
- Golden threshold unchanged: all 5 essential pass + composite >= 80
assified by novelty — BASELINE MATCH or NEW SIGNAL (depth) [NEW]
- C-12: Status Quo section documents prior belief baseline (coverage) [NEW]
- C-13: Citation audit completed before Findings are written (process) [NEW]

The key design choice: C-02 (hypothesis resolved) and C-03 (traceable evidence) guard
against the most common failure mode for prove-publish — outputs that look like papers but
are actually just narrative summaries disconnected from the actual investigation work.

---

## Essential Criteria (weight: 60 — must all pass)

### C-01 - All 8 sections present
- **Category**: format
- **Weight**: essential
- **Text**: The paper contains all 8 required sections: Abstract, Hypothesis, Method, Evidence,
  Findings, Principles, Future Work, Limitations. Missing or merged sections fail.
- **Pass condition**: All 8 section headers are present. Sections may be brief but must be
  explicitly present and separately headed.

### C-02 - Hypothesis is explicitly resolved
- **Category**: correctness
- **Weight**: essential
- **Text**: The paper states an explicit verdict on the hypothesis before listing findings.
  Acceptable forms: "The hypothesis was confirmed: ...", "The hypothesis was refuted
  because ...", or "Partially confirmed under condition X but not Y". Findings that never
  reference the hypothesis fail.
- **Pass condition**: A HYPOTHESIS VERDICT sentence appears before the first finding. The
  sentence commits to confirmed, refuted, or partially confirmed with a reason. Evasive
  framings ("the evidence suggests...") without a verdict fail.

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
- **Text**: The Findings section contains interpreted conclusions drawn from evidence — not a
  restatement or summary of the Evidence section. Findings answer "what does this mean?" not
  "what happened?".
- **Pass condition**: At least three distinct findings are present, each expressing a conclusion
  (a judgment, pattern, or causal claim) rather than an observation or data point.

### C-05 - Principles are extractable and reusable
- **Category**: depth
- **Weight**: essential
- **Text**: The Principles section contains numbered, action-oriented rules or heuristics that a
  future team can apply independently — without reading the full paper.
- **Pass condition**: At least two principles are present. Each is phrased as a rule (imperative
  or conditional: "Always X", "When Y, do Z", "Prefer A over B because..."). Vague summaries
  ("this area is complex") fail.

---

## Recommended Criteria (weight: 30 — improve quality)

### C-06 - Panel review with named expert roles
- **Category**: coverage
- **Weight**: recommended
- **Text**: The paper includes a simplified panel review section where at least two named expert
  roles (e.g. domain expert, skeptic, practitioner) provide critique, identify gaps, or assign
  a score.
- **Pass condition**: A review block is present with at least two distinct named reviewer
  perspectives. Each reviewer provides at least one substantive critique or endorsement, not
  just a score.

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
- **Text**: The Future Work section lists specific, actionable next investigations — not generic
  statements like "more research is needed."
- **Pass condition**: At least two future work items are phrased as investigable questions or
  proposed experiments, with enough specificity that a team could start them without further
  clarification.

---

## Aspirational Criteria (weight: 10 — raise the bar)

Each aspirational criterion is worth 2 pts. All 5 passing = 10/10.

### C-09 - Principles cross-referenced to findings
- **Category**: depth
- **Weight**: aspirational (2 pts)
- **Text**: Each principle in the Principles section is explicitly linked to the finding(s) that
  produced it (e.g. "Principle 1 [from F-02, F-05]: ..."). This creates a traceable chain from
  evidence to findings to principles.
- **Pass condition**: Every principle has at least one finding reference. Papers with unnumbered
  findings or unlinked principles fail.

### C-10 - New-team cold-start readability
- **Category**: behavior
- **Weight**: aspirational (2 pts)
- **Text**: The paper is self-contained enough that a team member with no prior context on this
  topic could read it and act on the principles without consulting the underlying investigation
  artifacts.
- **Pass condition**: The paper defines all domain-specific terms it uses, provides enough method
  context to understand why evidence was collected the way it was, and the Limitations section is
  honest about what the paper does not cover. Evaluated by attempting a cold read and checking
  for undefined jargon or unexplained jumps.

### C-11 - Findings classified by novelty
- **Category**: depth
- **Weight**: aspirational (2 pts)
- **Source**: V-05 excellence signal — BASELINE MATCH vs NEW SIGNAL tagging (R1 scorecard C-04)
- **Text**: Each finding is labeled to distinguish whether it confirms a prior belief
  (BASELINE MATCH) or challenges/extends it (NEW SIGNAL). This forces the author to
  explicitly identify what the investigation actually changed about the team's understanding.
- **Pass condition**: Every numbered finding carries a novelty tag. At least one finding is
  labeled NEW SIGNAL. Papers where all findings merely restate what was already believed fail
  this criterion even if synthesis quality is otherwise high.

### C-12 - Status Quo section documents prior belief baseline
- **Category**: coverage
- **Weight**: aspirational (2 pts)
- **Source**: V-05 excellence signal — Status Quo section gives new readers context they'd
  otherwise have to infer (R1 scorecard C-10)
- **Text**: The paper includes a Status Quo section (or equivalent subsection) that explicitly
  records what the team believed about this topic before the investigation began. This makes the
  paper's contribution legible by contrast — a reader can see exactly what changed.
- **Pass condition**: A Status Quo section or "Prior Belief" block is present that contains at
  least two concrete prior beliefs or assumptions held at investigation start. The section must
  precede the Hypothesis. Generic "background" text with no stated beliefs fails.

### C-13 - Citation audit precedes Findings
- **Category**: process
- **Weight**: aspirational (2 pts)
- **Source**: V-03 excellence signal — "Citation-audited before Findings begins" — strongest
  single enforcement of C-03 across all variations (R1 scorecard C-03)
- **Text**: The paper demonstrates (or its prompt enforces) that all Evidence citations were
  verified complete before any Findings were written. This prevents rationalization drift —
  the tendency to write conclusions first and then backfill evidence to fit them.
- **Pass condition**: The paper includes an explicit audit note, completion gate, or structural
  ordering that demonstrates evidence was locked before conclusions were drawn. Acceptable
  forms: a pre-Findings evidence checklist, an "Evidence complete as of [date/artifact]"
  marker, or a method description that names citation audit as a lifecycle step. Papers with
  no evidence of this ordering fail even if C-03 passes.

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band       | Score              | Meaning                             |
|------------|--------------------|-------------------------------------|
| Golden     | >= 80, all E pass  | Publishable — institutional memory  |
| Passing    | >= 60, all E pass  | Usable with gaps                    |
| Needs work | Any essential fail | Not yet a paper                     |
| Failing    | < 40               | Restart recommended                 |

---

## Version History

| Version | Date       | Changes                                                                                              |
|---------|------------|------------------------------------------------------------------------------------------------------|
| v1      | 2026-03-14 | Initial rubric — 10 criteria, 3 tiers                                                               |
| v2      | 2026-03-14 | Added C-11, C-12, C-13 from R1 excellence signals; aspirational pool redistributed to 2 pts each   |
