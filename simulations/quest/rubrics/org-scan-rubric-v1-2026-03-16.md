---
skill: quest-rubric
skill_target: org-scan
date: 2026-03-16
version: 1
---

# Scoring Rubric: org-scan

## Purpose

`org-scan` walks a repo and produces raw structural analysis — areas of work, team
boundaries, cross-cutting concerns, headcount signals, and a recommended org shape.
It is NOT an org chart. Its output feeds `org-chart`, which turns the analysis into
a structured artifact. This rubric tests whether the raw analysis is grounded,
complete enough to hand off, and correctly scoped.

---

## Essential Criteria (must all pass — 60% weight)

### C-01 Areas of Work Identified
**Category**: correctness
**Weight**: essential
**Text**: Output names at least 3 distinct areas of work, each derived from evidence
found in the repo (CLAUDE.md, namespaces, design directories, specs, or package.json),
not invented.
**Pass condition**: At least 3 named areas appear AND each is traceable to at least
one cited source artifact or repo pattern.

---

### C-02 Multi-Source Scan Performed
**Category**: coverage
**Weight**: essential
**Text**: Output demonstrates evidence from at least 3 of the 7 listed scan sources:
CLAUDE.md, package.json, design/ directories, namespaces, test coverage areas,
SPECS.md files, existing .craft/roles/.
**Pass condition**: At least 3 distinct scan source types are cited or referenced
in the analysis (by name or by path pattern), not just one type repeated.

---

### C-03 Headcount Signals Estimated
**Category**: correctness
**Weight**: essential
**Text**: Output estimates how many distinct expertise domains exist in the repo,
with rationale tied to the scan findings (not a round number stated without support).
**Pass condition**: A headcount signal (e.g., "3-4 distinct expertise domains") is
stated AND supported by at least one observation from the scan (e.g., namespace count,
role file count, discipline separation in specs).

---

### C-04 Cross-Cutting Concerns Surfaced
**Category**: depth
**Weight**: essential
**Text**: Output names at least one cross-cutting concern — a concern that spans
multiple areas and cannot be owned by a single team without coordination risk.
**Pass condition**: At least one cross-cutting concern is named (e.g., authentication,
data contracts, deployment pipeline) with a brief note on why it spans boundaries.

---

### C-05 Output Is Raw Analysis, Not an Org Chart
**Category**: behavior
**Weight**: essential
**Text**: Output does not produce a finalized org chart with named roles, reporting
lines, or box-and-line hierarchy. It is analytical prose and lists — input to
org-chart, not a replacement for it.
**Pass condition**: No finalized reporting structure, no "X reports to Y" statements,
no org-chart boxes appear. If a recommended shape is mentioned, it is a shape label
(flat, functional, matrix) not a drawn hierarchy.

---

## Recommended Criteria (better with these — 30% weight)

### C-06 Team Boundary Candidates Proposed
**Category**: depth
**Weight**: recommended
**Text**: Output proposes candidate team boundaries with supporting evidence — not just
areas of work, but where the seams might be between teams.
**Pass condition**: At least 2 candidate boundaries are proposed, each with a rationale
referencing a scan observation (e.g., "namespaces X and Y share no dependencies and
could separate cleanly").

---

### C-07 Recommended Org Shape With Rationale
**Category**: correctness
**Weight**: recommended
**Text**: Output names a recommended org shape (flat, functional, matrix, pods, etc.)
and explains why that shape fits the evidence found.
**Pass condition**: A shape label appears AND at least one sentence justifies it using
scan findings (e.g., "functional because expertise domains are deep and narrow").

---

### C-08 Evidence Gaps and Ambiguities Flagged
**Category**: depth
**Weight**: recommended
**Text**: Output explicitly notes areas where evidence was thin, absent, or ambiguous —
where the scan could not reach a confident conclusion.
**Pass condition**: At least one gap or ambiguity is named (e.g., "no test coverage
files found, so test ownership is unclear") so the consumer knows where to invest
before running org-chart.

---

## Aspirational Criteria (raise the bar — 10% weight)

### C-09 Specific File Paths Cited as Evidence
**Category**: correctness
**Weight**: aspirational
**Text**: Output cites at least 5 specific file paths (or path patterns) as direct
evidence for structural claims, making the analysis fully auditable.
**Pass condition**: 5 or more distinct file or directory paths appear in the analysis,
each linked to a structural observation.

---

### C-10 Current State Distinguished From Recommended State
**Category**: format
**Weight**: aspirational
**Text**: Output clearly separates what the scan found (current state) from what is
recommended (recommended state), so the consumer can see the gap between the two.
**Pass condition**: The document has visible separation — either labeled sections,
explicit "currently / recommended" phrasing, or a before/after table — for at least
two observations where current and recommended diverge.

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

### Score Bands

| Score | Interpretation |
|-------|---------------|
| 100   | Perfect — golden candidate |
| 80-99 | Golden (all essential pass, strong recommended) |
| 60-79 | Needs work — at least one essential failed or recommended weak |
| <60   | Not useful — multiple essential failures |

---

## Failure Pattern Guidance

| Pattern | Likely Cause |
|---------|-------------|
| C-01 fails: areas invented, not grounded | Skill skipped scan; used prior knowledge only |
| C-02 fails: only one source type cited | Scan loop stopped after CLAUDE.md |
| C-03 fails: headcount stated without support | Skill output a number with no derivation |
| C-04 fails: no cross-cutting concerns | Skill focused on areas only, missed seams |
| C-05 fails: org chart appeared in output | Skill confused org-scan with org-chart scope |
| C-06 fails: areas listed but no seam reasoning | Skill stopped at labeling, not analyzing |
| C-07 fails: shape label absent or unjustified | Skill produced observation soup with no synthesis |
| C-08 fails: no gaps mentioned | Skill over-confident; did not distinguish evidence from assumption |
