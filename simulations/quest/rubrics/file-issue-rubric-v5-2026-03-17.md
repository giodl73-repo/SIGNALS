Reading the Round 4 scorecard for new patterns not yet encoded in v4.

**New patterns visible:**

1. **V-01 C-14 "Strongest single-step isolation"**: "Severity then loads the matching form (Step 2) and output template (Step 3)." C-14 already requires severity-first sequencing and calls the unified dispatch "the strongest implementation" — but doesn't make it a separate pass condition. A skill can pass C-14 by sequencing severity first without dispatching both the collection schema and output template from that single event. New criterion: **C-17 — severity-driven unified pipeline dispatch**.

2. **V-02 C-15 "Completion condition defined"**: The phase blocking instruction goes beyond "DO NOT BEGIN PHASE B" to name the verifiable state that constitutes Phase A completion. C-15 requires the blocking instruction but doesn't require the completion condition to be defined. New criterion: **C-16 — phase boundary completion condition**.

Aspirational pool grows 8 → 10; formula denominator updates.

---

```markdown
# file-issue -- Scoring Rubric v5

**Skill**: `file-issue`
**Rubric version**: v5
**Date**: 2026-03-17
**Applies to**: All `file-issue` golden and scored variations

---

## Essential Criteria (60% of score)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Required fields captured** | coverage | essential | Skill collects all four required fields from the user: skill name, expected behavior, actual behavior, and severity. A skill that proceeds without all four fields is a fail. |
| C-02 | **Severity vocabulary enforcement** | format | essential | Skill enforces exactly the four-value severity enum: `crash`, `wrong-output`, `missing-feature`, `improvement`. Accepts no synonyms, free-text, or alternative values. On invalid input, rejects and re-prompts rather than proceeding. |
| C-03 | **GitHub issue format** | format | essential | Output is formatted as a GitHub issue: a title line following a `[{severity}] {skill}: {description}` pattern, plus a structured body with at minimum Expected / Actual / Steps / Context sections. Prose description without title/sections is a fail. |
| C-04 | **Artifact path under simulations/feedback/** | behavior | essential | Skill writes or clearly specifies an artifact path under `simulations/feedback/`. Path must be non-ambiguous (includes skill name and date or slug). |

---

## Recommended Criteria (30% of score)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Actionable, specific issue title** | format | recommended | The GitHub issue title names the specific skill and the specific problem -- not generic phrases like "Bug report" or "Issue with skill". Pass: title contains skill name + symptom or behavior. |
| C-06 | **Sufficient reproducibility context** | depth | recommended | Body includes enough detail for a maintainer to reproduce or understand the issue: what input was given, what the environment was, or what sequence of events led to the problem. A one-sentence description alone is a fail. |
| C-07 | **Repo open offer presented** | behavior | recommended | Skill explicitly offers to open the issue at the Signal repo (e.g., asks the user if they want to open it, or provides a `gh issue create` command). |

---

## Aspirational Criteria (10% of score)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Severity-appropriate framing** | depth | aspirational | Tone and urgency match severity: `crash` uses urgent language and asks for immediate reproduction steps; `improvement` uses constructive, proposal-oriented framing. |
| C-09 | **Skill context enrichment** | coverage | aspirational | Issue body includes at least one enriching context item beyond the four required fields: skill version or date, related skills in the invocation chain, topic name, or a reference to an existing rubric or golden artifact. |
| C-10 | **Pre-write validation gate** | structure | aspirational | Skill includes a structured check phase -- separate from drafting -- that verifies reproducibility, tone match, and field completeness before writing the artifact. The gate must block the write step; a post-write summary check does not qualify. *(Excellence signal: V-03 PHASE 3 -- VALIDATE.)* |
| C-11 | **Corrective actions per validation check** | structure | aspirational | Each validation check item includes an explicit corrective action specifying what the skill does on failure. A checklist of pass/fail conditions without prescribed remedies does not qualify. *(Excellence signal: V-04 STEP 3 table.)* |
| C-12 | **Per-severity body templates** | structure | aspirational | Skill maintains four distinct body templates -- one per severity value -- that architecturally enforce severity-appropriate fields, tone, and required sections. The `crash` template includes priority and impact fields; the `improvement` template requires an acceptance condition. A single generic template with tone guidance does not qualify; template selection must determine structure, not just style. *(Excellence signal: V-04 full synthesis.)* |
| C-13 | **Severity-labeled issue creation** | behavior | aspirational | The `gh issue create` command includes `--label "{severity}"` so the opened issue is immediately classified in the repo's label taxonomy. A bare `gh issue create` without `--label` does not qualify. *(Excellence signal: V-04 STEP 4 offer.)* |
| C-14 | **Severity-first field sequencing** | structure | aspirational | Severity is the first required field collected and must be validated before any other required field is requested. The skill explicitly states that no other collection occurs until a valid severity value is confirmed. A skill that presents all four required fields simultaneously or in unordered fashion does not qualify. Template selection driven by severity confirmation -- so that the correct collection form and output template are both determined by a single sequenced event -- is the strongest implementation. *(Excellence signal: V-02 "Do not collect any other field until severity is confirmed.")* |
| C-15 | **Macro-phase hard boundary** | structure | aspirational | The skill organizes work into two named macro-phases -- each encompassing multiple sub-operations (e.g., PHASE A: COLLECT+DRAFT / PHASE B: VALIDATE+WRITE) -- with an explicit cross-phase blocking instruction at the boundary ("DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE"). A linear step sequence with a named gate step does not qualify; the gate must be a phase transition where the entire second phase is blocked until the first phase completes. A four-step sequence with a pre-write checklist at step 3 does not qualify. *(Excellence signal: V-04 dual blocking -- phase level and row level.)* |
| C-16 | **Phase boundary completion condition** | structure | aspirational | The cross-phase blocking instruction at the macro-phase boundary defines an explicit, verifiable completion condition: a named state that must be true for Phase A to be considered complete (e.g., "all required fields confirmed and severity-driven template loaded"), not merely a temporal "before beginning Phase B." The completion condition must be checkable -- a specific state, not a restatement of the blocking instruction. A skill that has a C-15 phase boundary but states only "DO NOT BEGIN PHASE B" without defining what constitutes Phase A completion does not qualify. *(Excellence signal: V-02 C-15 evidence -- "Completion condition defined.")* |
| C-17 | **Severity-driven unified pipeline dispatch** | structure | aspirational | Severity confirmation is the single event that dispatches both (a) the collection schema -- which fields to collect, in which form, with which prompts -- and (b) the output template -- which artifact structure to generate. The two selections must be linked to the same severity confirmation event, not handled separately. A skill that uses severity to select the output template but applies a fixed collection form to all severities does not qualify; severity must determine both pipelines. This extends C-14: where C-14 requires severity to be sequenced first, C-17 requires severity to be the full-pipeline dispatch key. A skill can pass C-14 without passing C-17. *(Excellence signal: V-01 C-14 -- "Severity then loads the matching form (Step 2) and output template (Step 3). Strongest single-step isolation implementation.")* |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
```

### Round 4 scores under v5

| Variation | C-14 | C-15 | C-16 | C-17 | Aspirational hits | Composite | Verdict |
|-----------|------|------|------|------|-------------------|-----------|---------|
| V-01 | PASS | FAIL | FAIL | PASS | C-08 to C-14, C-17 (8/10) | **98.0** | Golden |
| V-02 | FAIL | PASS | PASS | FAIL | C-08 to C-13, C-15, C-16 (8/10) | **98.0** | Golden |
```

---

**Summary of changes v4 → v5:**

- **C-16** (phase boundary completion condition): extracted from V-02 Round 4 C-15 evidence — "Completion condition defined." C-15 already requires the blocking instruction; C-16 separately requires that the instruction names a verifiable state constituting Phase A completion. A skill with C-15 but no explicit completion condition fails C-16.

- **C-17** (severity-driven unified pipeline dispatch): extracted from V-01 Round 4 C-14 evidence — severity confirmation loads both the collection form (Step 2) and the output template (Step 3) in a single dispatch event. C-14 awards this as "the strongest implementation" but does not require it for PASS. C-17 isolates the pattern as its own criterion: severity must be the dispatch key for both collection schema and output template, not just sequenced first.

- **Formula denominator**: aspirational pool 8 → 10, reducing the per-criterion contribution from 1.25 to 1.0 points. A variation scoring 8/10 aspirational now composites at 98.0 vs. 98.75 under v4. Perfect aspirational (10/10) still contributes a full 10 points.
