Rubric written to `simulations/quest/rubrics/mock-ns-rubric-v2-2026-03-16.md`.

---

**What changed from v1:**

**C-05 strengthened** — pass condition now explicitly says "without reading the header," matching V-05's strongest wording.

**C-06 tightened** — pass condition now calls out the ordering requirement (TOPICS.md line first, generating line second) and explicitly states that half-credit is not granted. V-02's trap ("had tier but no TOPICS.md line") is now blocked by the wording.

**C-10 clarified** — added bold statement that no compliance tags = default pass. The R1 prediction error (predictors treated absence of tags as a fail) is now directly addressed.

**Three new aspirational criteria:**

| ID | Text | Source |
|----|------|--------|
| C-11 | FLAG rule names critical namespaces explicitly (`trace-*`, `scout-feasibility`, `listen-*`) and covers all 5 cases | R1 Pattern 2 — V-03/V-04/V-05 tier-conditional completeness |
| C-12 | S-0 TOPICS.md step resolves tier *before* S-1 skill selection begins | R1 Pattern 1 — S-0 as structural anchor enabling tier-conditional firing |
| C-13 | Category lookup halts with error on unrecognized skill-id | R1 V-05 only — "error-stop on unknown skill" |

**Two new failure traps added** to the table: partial C-06 setup (V-02's exact failure) and C-10 default-pass not modeled.
t, program-plan, etc.) produce `HIGH-STRUCTURE`. EVIDENCE-HEAVY skills (prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption) produce `EVIDENCE-HEAVY`. MIXED skills (scout-competitors, prove-hypothesis, review-customers, review-users) produce `MIXED`. Any mismatch is a fail.

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
- **Pass condition**: A reader familiar with the target skill can identify which skill was mocked from the section headings, tables, and enforcement mechanisms alone -- without reading the header. The body includes all required section headings for the selected skill, at least one skill-specific table or scored list in its expected position, and a gate or verdict line where the real skill produces one. A body that could belong to any skill is a fail.

---

## Recommended Criteria

*Output is better with these. Failing one lowers the score but does not block golden.*

### C-06
- **Text**: S-1 setup emit lines are present: TOPICS.md status line and skill selection line.
- **Weight**: recommended
- **Category**: behavior
- **Pass condition**: Output contains a dedicated line in the form `> TOPICS.md: {found/not found}, tier: {tier}, compliance tags: {tags or none}` and a second line `> Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...`. Both lines appear before the artifact header. The TOPICS.md line must appear first (S-0 before S-1). Having only the generating line -- even with tier present -- is a fail. Having only the TOPICS.md line is a fail. Both are required.

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
- **Pass condition**: When TOPICS.md contains compliance tags and the selected skill is `scout-compliance` or `trace-permissions`, FLAG is overridden to `REAL-REQUIRED (compliance-sensitive)` regardless of CATEGORY or tier. If compliance tags are present and the override is not applied, the criterion fails. **If no compliance tags are present, the criterion passes by default** -- the absence of compliance tags is not a failure state.

### C-11
- **Text**: FLAG computation rule names critical skill namespaces explicitly and covers all 5 cases.
- **Weight**: aspirational
- **Category**: correctness
- **Pass condition**: The FLAG computation is expressed as a complete table or enumerated case list covering all 5 category/tier/skill-condition combinations: (1) HIGH-STRUCTURE non-critical any tier, (2) HIGH-STRUCTURE critical tier 1, (3) HIGH-STRUCTURE critical tier >= 2, (4) EVIDENCE-HEAVY, (5) MIXED. Critical namespaces are named explicitly as `trace-*`, `scout-feasibility`, and `listen-*` -- a generic description like "critical skills" without enumeration is not sufficient. This goes beyond C-03 (which only checks the output flag value) to the completeness of the rule that produces it. Source: R1 scorecard Pattern 2 -- tier-conditional completeness in V-03/V-04/V-05 required explicit name enumeration to fire correctly.

### C-12
- **Text**: TOPICS.md step resolves tier before skill selection begins.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: The S-0 TOPICS.md step completes -- emitting the status line with tier -- before the S-1 skill selection step begins. This ordering is what allows the tier value to propagate into the tier-conditional FLAG rule in S-3. A prompt that reads TOPICS.md and emits the status line but within the same step as skill selection (rather than prior to it) does not satisfy this criterion. Source: R1 scorecard Pattern 1 -- S-0 as structural anchor that enables tier-conditional firing.

### C-13
- **Text**: Category lookup halts with a clear error on unrecognized skill-ids.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: When a skill-id is provided that does not exist in the canonical registry, the skill emits an error and stops -- it does not silently assign a fallback category or produce a mock with a guessed CATEGORY. The error message names the unrecognized skill-id and directs the user to the registry. Source: R1 scorecard V-05 evidence -- "error-stop on unknown skill" was the only variation to include this guard.

---

## Common Failure Modes

| Failure | Criterion | Description |
|---------|-----------|-------------|
| EVIDENCE-HEAVY flagged as `none` | C-03 | listen-support or prove-interview assigned FLAG = `none` instead of `REAL-REQUIRED` |
| Generic body | C-05 | Artifact body uses paragraph prose with no skill-specific tables or verdict line |
| Skill-id in filename | C-07 | Path uses `{topic}-{skill-id}-mock-{date}.md` instead of `{topic}-{namespace}-mock-{date}.md` |
| Category/Flag mismatch | C-02 + C-03 | CATEGORY assigned correctly but FLAG computed for a different category |
| Missing fidelity warning | C-04 | Header present but no warning block before body content |
| Partial C-06 setup | C-06 | Generating emit present with tier field, but TOPICS.md status line absent. Half-credit is not granted -- C-06 requires both lines. V-02 hit this trap: scored 90 instead of 100. |
| C-10 default-pass not modeled | C-10 | Predictors mark C-10 as fail when no compliance tags are present. The rubric grants a default pass in this case. The criterion only fires when compliance tags exist. |
