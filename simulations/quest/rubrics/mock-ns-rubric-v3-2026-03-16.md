Written to `simulations/quest/rubrics/mock-ns-rubric-v3-2026-03-16.md`.

---

**What changed from v2:**

**Three new aspirational criteria** (C-14, C-15, C-16) extracted from R2 V-05 excellence signals:

| ID | Text | Source signal |
|----|------|---------------|
| C-14 | Assembly expressed as discrete named steps A-1 through A-5 | "separated assembly steps make each output responsibility a discrete verifiable unit" |
| C-15 | CONSTRAINT block names prohibited S-0 operations by type (no category lookup, no skill selection, no mock generation) | "CONSTRAINT keyword names prohibited operations by type, not just by ordering" |
| C-16 | Wildcard patterns `trace-*`, `listen-*` appear in the FLAG table condition column cell, not only in footnotes | "wildcard notation in FLAG table condition column -- directly in the case match cell" |

**C-12 clarified** — R2 canary result encoded: step-labeled separation satisfies C-12; CONSTRAINT block (C-15) is defense-in-depth only and does not move the C-12 score.

**C-13 clarified** — meta-instruction format satisfies C-13; R2 Pattern 2 result encoded in the pass condition.

**Two new failure traps** added to the table: "C-13 via meta-instruction only" (passes C-13, misses C-14) and "Wildcard in footnote only" (passes C-11, fails C-16).

**Scoring note**: With 16 criteria total — 5 essential (50) + 3 recommended (30) + 8 aspirational (32) — the max is now 112 pts. To stay at 100-max, aspirational weight drops to 2.5 pts each, or you re-tier the point model before R3.
clarified:** R2 canary confirmed that the CONSTRAINT block is not required for C-12. Step-labeled separation with an explicit tier-carry handoff sentence satisfies the pass condition. CONSTRAINT block (C-15) adds adversarial robustness but does not move the C-12 score.

---

### v2 (2026-03-16) — R1 patterns promoted to aspirational criteria

**C-05 strengthened** — pass condition now explicitly says "without reading the header."

**C-06 tightened** — ordering requirement called out (TOPICS.md line first); half-credit not granted.

**C-10 clarified** — bold statement that no compliance tags = default pass.

**Three new aspirational criteria from R1:**

| ID | Text | Source |
|----|------|--------|
| C-11 | FLAG rule names critical namespaces explicitly (`trace-*`, `scout-feasibility`, `listen-*`) and covers all 5 cases | R1 Pattern 2 — tier-conditional completeness |
| C-12 | S-0 TOPICS.md step resolves tier before S-1 skill selection begins | R1 Pattern 1 — S-0 as structural anchor |
| C-13 | Category lookup halts with error on unrecognized skill-id | R1 V-05 only — error-stop on unknown skill |

---

### v1 (2026-03-16) — initial rubric

Baseline from first golden construction.

---

## Essential Criteria

*All must pass for golden.*

### C-01
- **Text**: Artifact header contains all 6 required fields.
- **Weight**: essential
- **Category**: format
- **Pass condition**: Header block contains exactly: `skill`, `topic`, `tier`, `category`, `flag`, `date`. All fields are present, non-empty, and in the standard header format. Any missing or misnamed field is a fail.

### C-02
- **Text**: CATEGORY is correctly assigned for the selected skill-id.
- **Weight**: essential
- **Category**: correctness
- **Pass condition**: HIGH-STRUCTURE skills (mock-ns, mock-all, mock-review, flow-lifecycle, flow-throttle, flow-trigger, flow-resilience, flow-dataflow, flow-conversation, flow-integration, trace-component, trace-contract, trace-deployment, trace-migration, trace-request, trace-permissions, trace-state, trace-skill, org-chart, org-committee, org-review, org-roles, scout-compliance, scout-requirements, scout-stakeholders, scout-naming, scout-positioning, scout-market, draft-brainstorm, draft-pitch, draft-spec, draft-proposal, program-plan, etc.) produce `HIGH-STRUCTURE`. EVIDENCE-HEAVY skills (prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption) produce `EVIDENCE-HEAVY`. MIXED skills (scout-competitors, prove-hypothesis, review-customers, review-users) produce `MIXED`. Any mismatch is a fail.

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
- **Pass condition**: The FLAG computation is expressed as a complete table or enumerated case list covering all 5 category/tier/skill-condition combinations: (1) HIGH-STRUCTURE non-critical any tier, (2) HIGH-STRUCTURE critical tier 1, (3) HIGH-STRUCTURE critical tier >= 2, (4) EVIDENCE-HEAVY, (5) MIXED. Critical namespaces are named explicitly as `trace-*`, `scout-feasibility`, and `listen-*` -- a generic description like "critical skills" without enumeration is not sufficient. This goes beyond C-03 (which only checks the output flag value) to the completeness of the rule that produces it. Source: R1 Pattern 2 -- tier-conditional completeness in V-03/V-04/V-05 required explicit name enumeration to fire correctly.

### C-12
- **Text**: TOPICS.md step resolves tier before skill selection begins.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: The S-0 TOPICS.md step completes -- emitting the status line with tier -- before the S-1 skill selection step begins. This ordering is what allows the tier value to propagate into the tier-conditional FLAG rule in S-3. A prompt that reads TOPICS.md and emits the status line but within the same step as skill selection (rather than prior to it) does not satisfy this criterion. **Note (R2 canary):** Step-labeled separation with an explicit "carry tier into S-2 and S-3" handoff sentence satisfies this criterion -- a CONSTRAINT block is not required. The CONSTRAINT block (C-15) adds adversarial robustness but does not move the C-12 score. Source: R1 Pattern 1 -- S-0 as structural anchor that enables tier-conditional firing.

### C-13
- **Text**: Category lookup halts with a clear error on unrecognized skill-ids.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: When a skill-id is provided that does not exist in the canonical registry, the skill emits an error and stops -- it does not silently assign a fallback category or produce a mock with a guessed CATEGORY. The error message names the unrecognized skill-id and directs the user to the registry. A meta-instruction ("emit an error that names the skill-id and points to the registry") satisfies this criterion -- content requirements (name skill-id + registry pointer) are what matter, not template format. Source: R1 V-05; R2 Pattern 2 confirmed meta-instruction equivalence.

### C-14
- **Text**: Artifact assembly is expressed as discrete named steps, each a separate verifiable unit.
- **Weight**: aspirational
- **Category**: structure
- **Pass condition**: The prompt names at least 5 discrete assembly steps in sequence: A-1 HEADER (emit the 6-field header block), A-2 FIDELITY WARNING (emit the category-matched warning), A-3 BODY (emit the skill-specific sections and tables), A-4 WRITE (write the artifact to the correct path and emit the write confirmation), A-5 NEXT-STEP (emit the next-step line as the final output). Each step is labeled and addresses a single output responsibility. A prompt that produces the same outputs in prose sequence without discrete step labels does not satisfy this criterion. Source: R2 V-05 excellence signal -- "separated artifact assembly steps make each output responsibility a discrete verifiable unit."

### C-15
- **Text**: A CONSTRAINT block explicitly names the operations prohibited during S-0.
- **Weight**: aspirational
- **Category**: behavior
- **Pass condition**: A labeled CONSTRAINT section (or equivalent explicit prohibition block) appears at or within the S-0 step definition and names at minimum three prohibited operation types: no category lookup, no skill selection, no mock generation. The prohibition must name the operation types, not merely restate the ordering rule. A prompt that only says "complete S-0 before S-1" without naming what is prohibited does not satisfy this criterion. Note: C-12 (step ordering) passes without C-15 -- this criterion adds adversarial robustness for cases where a model might perform disallowed operations mid-step despite correct ordering signals. Source: R2 V-05 excellence signal -- "CONSTRAINT keyword as explicit step gate names prohibited operations by type, not just by ordering."

### C-16
- **Text**: Wildcard patterns for critical namespaces appear directly in the FLAG table condition column.
- **Weight**: aspirational
- **Category**: correctness
- **Pass condition**: In the FLAG computation table, the condition cell for the critical HIGH-STRUCTURE case contains the wildcard patterns `trace-*` and `listen-*` directly in the match expression (e.g., "HIGH-STRUCTURE AND skill-id matches trace-*, scout-feasibility, or listen-*"). Listing `trace-*` and `listen-*` only in a footnote or expansion block below the table -- while the condition cell reads "critical skill" or similar -- does not satisfy this criterion. C-11 requires enumeration somewhere in the rule; C-16 requires that enumeration to appear in the condition column cell itself. Source: R2 V-05 excellence signal -- "wildcard notation in FLAG table condition column -- `trace-*`, `listen-*` appear directly in the case match cell, not only in the expansion footnote."

---

## Common Failure Modes

| Failure | Criterion | Description |
|---------|-----------|-------------|
| EVIDENCE-HEAVY flagged as `none` | C-03 | listen-support or prove-interview assigned FLAG = `none` instead of `REAL-REQUIRED` |
| Generic body | C-05 | Artifact body uses paragraph prose with no skill-specific tables or verdict line |
| Skill-id in filename | C-07 | Path uses `{topic}-{skill-id}-mock-{date}.md` instead of `{topic}-{namespace}-mock-{date}.md` |
| Category/Flag mismatch | C-02 + C-03 | CATEGORY assigned correctly but FLAG computed for a different category |
| Missing fidelity warning | C-04 | Header present but no warning block before body content |
| Partial C-06 setup | C-06 | Generating emit present with tier field, but TOPICS.md status line absent. Half-credit is not granted -- C-06 requires both lines. V-02 (R1) hit this trap: scored 90 instead of 100. |
| C-10 default-pass not modeled | C-10 | Predictors mark C-10 as fail when no compliance tags are present. The rubric grants a default pass in this case. The criterion only fires when compliance tags exist. |
| C-13 via meta-instruction only | C-13 | Error guard stated as meta-instruction rather than a literal template with `{skill-id}` placeholder. Passes C-13 (content requirements met) but misses C-14's assembly-step standard. |
| Wildcard in footnote only | C-16 | `trace-*`, `listen-*` appear in an expansion note below the FLAG table but the condition cell reads "critical skill." Passes C-11 (enumeration present) but fails C-16 (must be in condition cell). |
