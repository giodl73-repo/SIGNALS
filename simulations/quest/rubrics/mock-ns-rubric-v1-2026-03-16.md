---
skill: quest-rubric
skill_target: mock-ns
date: 2026-03-16
version: 1
---

# Scoring Rubric: mock-ns

## Purpose

Defines what good output looks like for `/mock-ns`. Used as the objective function for
`/quest-golden` and by `/quest-score` to rank candidate outputs.

**Golden threshold**: all essential criteria pass + composite score >= 80.

**Composite formula**:
  (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)

---

## Essential Criteria

*All must pass. Without these the output is not useful.*

### C-01
- **Text**: MOCK ARTIFACT header block is present, correctly positioned, and contains all six required fields.
- **Weight**: essential
- **Category**: format
- **Pass condition**: The header appears immediately after any frontmatter and before all body content. All six fields are present with non-empty values: `Skill`, `Topic`, `Category`, `Date`, `Status`, `Flag`. No field is missing or blank. Status reads `MOCK (awaiting review)`.

### C-02
- **Text**: CATEGORY is correctly assigned from the canonical registry for the selected skill.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: The Category field in the header matches the lookup result from the S-2 registry exactly. HIGH-STRUCTURE skills (scout-feasibility, draft-spec, review-design, flow-resilience, trace-request, program-plan, etc.) produce `HIGH-STRUCTURE`. EVIDENCE-HEAVY skills (prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption) produce `EVIDENCE-HEAVY`. MIXED skills (scout-competitors, prove-hypothesis, review-customers, review-users) produce `MIXED`. Any mismatch is a fail.

### C-03
- **Text**: FLAG is correctly computed from CATEGORY and tier, and written verbatim into the header.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: Flag value matches the S-3 case that applies: HIGH-STRUCTURE non-critical = `none (structural coverage reliable)`; HIGH-STRUCTURE critical at tier >= 2 = `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)`; EVIDENCE-HEAVY = `REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)`; MIXED = `REVIEW-FOR-PLAUSIBILITY`. Compliance override applied when compliance tags are present for scout-compliance or trace-permissions. Any deviation from the case rules is a fail.

### C-04
- **Text**: Fidelity warning block is present and matches the assigned CATEGORY.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: A fidelity warning section appears between the header and the artifact body, delimited by `---`. The warning text matches the CATEGORY: EVIDENCE-HEAVY warning states the content is evidentially fabricated and a real run is required; MIXED warning distinguishes reliable structural elements from potentially fabricated specific claims; HIGH-STRUCTURE warning describes structural reliability and tier escalation. A generic or missing warning is a fail.

### C-05
- **Text**: Artifact body is skill-specific -- not generic prose.
- **Weight**: essential
- **Category**: depth
- **Pass condition**: A reader familiar with the target skill can identify which skill was mocked from the section headings, tables, and enforcement mechanisms alone. The body includes all required section headings for the selected skill, at least one skill-specific table or scored list in its expected position, and a gate or verdict line where the real skill produces one. A body that could belong to any skill is a fail.

---

## Recommended Criteria

*Output is better with these. Failing one lowers the score but does not block golden.*

### C-06
- **Text**: S-1 setup emit lines are present: TOPICS.md status line and skill selection line.
- **Weight**: recommended
- **Category**: behavior
- **Pass condition**: Output contains a dedicated line in the form `> TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}` and a second line `> Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...`. Both lines appear before the artifact header.

### C-07
- **Text**: Artifact is written to the correct path and the write confirmation is emitted.
- **Weight**: recommended
- **Category**: behavior
- **Pass condition**: Output contains `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md`. The filename uses the namespace (not the skill-id), the topic matches the input, and the date matches the run date. A path using skill-id in place of namespace is a fail.

### C-08
- **Text**: Next-step line is the final line of the artifact.
- **Weight**: recommended
- **Category**: format
- **Pass condition**: The artifact ends with `Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md`. Omission is acceptable only when the skill was called from within a mock-review session to regenerate a thin namespace (the skill spec permits this); otherwise absence is a fail.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

### C-09
- **Text**: Default skill selection follows the exclusion constraint for the `topic` namespace.
- **Weight**: aspirational
- **Category**: correctness
- **Pass condition**: When namespace=`topic` and no `--skill` flag is provided, the selected skill is `topic-plan`, not `topic-status`. `topic-status` is explicitly excluded as meta-structural. Selecting `topic-status` as default is a fail.

### C-10
- **Text**: Compliance override is applied when compliance tags are present.
- **Weight**: aspirational
- **Category**: correctness
- **Pass condition**: When TOPICS.md contains compliance tags and the selected skill is `scout-compliance` or `trace-permissions`, FLAG is overridden to `REAL-REQUIRED (compliance-sensitive)` regardless of CATEGORY or tier. If compliance tags are present and the override is not applied, the criterion fails. If no compliance tags are present, the criterion passes by default.

---

## Common Failure Modes

| Failure | Criterion | Description |
|---------|-----------|-------------|
| EVIDENCE-HEAVY flagged as `none` | C-03 | listen-support or prove-interview assigned FLAG = `none` instead of `REAL-REQUIRED` |
| Generic body | C-05 | Artifact body uses paragraph prose with no skill-specific tables or verdict line |
| Skill-id in filename | C-07 | Path uses `{topic}-{skill-id}-mock-{date}.md` instead of `{topic}-{namespace}-mock-{date}.md` |
| Category/Flag mismatch | C-02 + C-03 | CATEGORY assigned correctly but FLAG computed for a different category |
| Missing fidelity warning | C-04 | Header present but no warning block before body content |
