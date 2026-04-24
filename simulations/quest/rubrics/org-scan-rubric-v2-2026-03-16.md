Written. Here's the complete updated rubric:

---

# Scoring Rubric: org-scan (v2)

## Changes from v1

Three new aspirational criteria added from R1/V-01 excellence signals. Aspirational band stays 10% — now 5 criteria at 2 pts each instead of 2 criteria at 5 pts each.

| New Criterion | Source Signal |
|---|---|
| C-11 | Anti-fabrication language: "Do not invent areas that have no evidence basis" |
| C-12 | Hard phase-completion gate: "complete all before drawing conclusions" |
| C-13 | Double-stated constraint: C-05 in preamble AND repeated in output format |

---

## Essential (60%)

**C-01** Areas named and traceable to scan evidence, not invented  
**C-02** Multi-source scan — 3+ of 7 source types cited  
**C-03** Headcount estimated as a range with supporting rationale  
**C-04** Cross-cutting concerns named with boundary note  
**C-05** Raw analysis only — no org chart, no reporting lines

## Recommended (30%)

**C-06** Team boundary candidates with seam rationale  
**C-07** Org shape named and justified from findings  
**C-08** Evidence gaps and ambiguities flagged explicitly

## Aspirational (10%, 2 pts each)

**C-09** 5+ specific file paths cited as auditable evidence  
**C-10** Current state vs recommended state clearly separated  
**C-11** Anti-fabrication language embedded per evidence-dependent section  
**C-12** Hard sequencing gate: scan must complete before synthesis begins  
**C-13** Critical constraint (C-05) stated twice — preamble + output format

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.

---

**Design note on C-11/C-12/C-13**: These three patterns explain the 15-point gap between V-01 (95) and V-02 (80 at floor). They're aspirational because you can pass the essentials without them — but a skill with all three is structurally harder to violate than one without them.
me or by path pattern), not just one type repeated.

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
**Text**: Output names at least one cross-cutting concern -- a concern that spans
multiple areas and cannot be owned by a single team without coordination risk.
**Pass condition**: At least one cross-cutting concern is named (e.g., authentication,
data contracts, deployment pipeline) with a brief note on why it spans boundaries.

---

### C-05 Output Is Raw Analysis, Not an Org Chart
**Category**: behavior
**Weight**: essential
**Text**: Output does not produce a finalized org chart with named roles, reporting
lines, or box-and-line hierarchy. It is analytical prose and lists -- input to
org-chart, not a replacement for it.
**Pass condition**: No finalized reporting structure, no "X reports to Y" statements,
no org-chart boxes appear. If a recommended shape is mentioned, it is a shape label
(flat, functional, matrix) not a drawn hierarchy.

---

## Recommended Criteria (better with these -- 30% weight)

### C-06 Team Boundary Candidates Proposed
**Category**: depth
**Weight**: recommended
**Text**: Output proposes candidate team boundaries with supporting evidence -- not just
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
**Text**: Output explicitly notes areas where evidence was thin, absent, or ambiguous --
where the scan could not reach a confident conclusion.
**Pass condition**: At least one gap or ambiguity is named (e.g., "no test coverage
files found, so test ownership is unclear") so the consumer knows where to invest
before running org-chart.

---

## Aspirational Criteria (raise the bar -- 10% weight, 2 pts each)

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
**Pass condition**: The document has visible separation -- either labeled sections,
explicit "currently / recommended" phrasing, or a before/after table -- for at least
two observations where current and recommended diverge.

---

### C-11 Anti-Fabrication Language Explicit
**Category**: behavior
**Weight**: aspirational
**Text**: The skill prompt (or the output itself) names the failure mode it prohibits:
"Do not invent areas that have no evidence basis" or equivalent language appears
adjacent to each evidence-dependent output section, not only in a preamble.
**Pass condition**: At least one explicit "do not invent / fabricate / assume"
prohibition appears within or immediately before an evidence-dependent section --
not only in a top-level disclaimer.
**Why this matters**: A preamble warning is skimmable and forgotten. Embedding the
prohibition next to the task it governs is the structural pattern that prevents
hallucinated areas even in long outputs.

---

### C-12 Hard Phase-Completion Gate Before Synthesis
**Category**: behavior
**Weight**: aspirational
**Text**: The skill enforces a sequencing rule: all scan sources must be visited before
any synthesis step (areas, boundaries, shape) may begin. The gate is stated as a rule,
not just implied by phase order.
**Pass condition**: An explicit gate statement appears -- e.g., "complete all scan
phases before drawing conclusions", "do not proceed to Step 2 until all 7 sources have
been checked" -- and synthesis phases follow scan phases in the prompt structure.
**Why this matters**: Without a hard gate, a model can skip to synthesis after visiting
one source. Naming the gate makes premature synthesis a detectable violation, not just
a quality failure.

---

### C-13 Critical Constraints Stated Twice
**Category**: format
**Weight**: aspirational
**Text**: The most critical behavioral constraint (C-05: not an org chart) is stated
in at least two structurally separate locations: once in the preamble or skill context,
and again in the output format or closing instructions.
**Pass condition**: The "not an org chart" prohibition (or equivalent scoping
constraint) appears verbatim or in close paraphrase in both the setup section and the
output format section of the skill prompt.
**Why this matters**: A constraint stated once survives initial reading; a constraint
stated twice survives skimming and mid-output drift. V-01 passed C-05 cleanly; V-02
passed it but with lower structural confidence. Double-stating is the differentiator.

---

## Composite Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

PASS = full points per criterion | PARTIAL = half points | FAIL = 0

Points per band:
- Essential (C-01--05): 12 pts each, 60 pts total
- Recommended (C-06--08): 10 pts each, 30 pts total
- Aspirational (C-09--13): 2 pts each, 10 pts total

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

### Score Bands

| Score | Interpretation |
|-------|---------------|
| 100   | Perfect -- golden candidate |
| 80-99 | Golden (all essential pass, strong recommended) |
| 60-79 | Needs work -- at least one essential failed or recommended weak |
| <60   | Not useful -- multiple essential failures |

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
| C-11 fails: no anti-fabrication language | Prohibition only in preamble; mid-output sections unguarded |
| C-12 fails: no sequencing gate | Synthesis may run before scan is complete |
| C-13 fails: constraint stated only once | Critical scoping rule dropped on long outputs |
