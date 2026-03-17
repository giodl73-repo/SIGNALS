Reading the scorecard architectural notes carefully to identify Round 3 patterns not yet captured in v3.

**New patterns to encode:**

1. **V-02 architectural note**: "Only variation where the template is simultaneously an input schema and output schema — severity-first means template selection gates collection, not just formatting." The specific signal: `"Do not collect any other field until severity is confirmed."` — severity is the *first* field collected, and its confirmation gates the rest of the form. This is stronger than C-02 (which requires enforcement) — it adds an ordering constraint.

2. **V-04 architectural note**: "Phase boundary produces the clearest gate signal. 'DO NOT BEGIN PHASE B' is structurally harder to skip than a pre-write checklist." The specific signal: two named macro-phases each encompassing multiple operations, with a cross-phase blocking instruction at the boundary. Distinct from C-10 (inline pre-write checklist) — the gate is a phase transition, not a step within a phase.

V-03's seventh validation check row is noted as "excess relative to rubric minimum" — not a new pattern, a deeper implementation of C-11.

New criteria: **C-14** (severity-first sequencing) and **C-15** (macro-phase hard boundary). Aspirational pool grows from 6 → 8; formula denominator updates accordingly.

**Round 3 scores under v4:**
- V-01: C-14 FAIL (no severity-first ordering), C-15 FAIL → 6/8 aspirational → **97.5**
- V-02: C-14 PASS, C-15 FAIL (step sequence, not macro-phase) → 7/8 → **98.75**
- V-03: C-14 FAIL (no severity-first ordering), C-15 FAIL (four-phase, not two-phase compression) → 6/8 → **97.5**
- V-04: C-14 FAIL (form table, no explicit severity-first), C-15 PASS → 7/8 → **98.75**

---

```markdown
# file-issue -- Scoring Rubric v4

**Skill**: `file-issue`
**Rubric version**: v4
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

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

### Round 3 scores under v4

| Variation | C-14 | C-15 | Aspirational hits | Composite | Verdict |
|-----------|------|------|-------------------|-----------|---------|
| V-01 | FAIL | FAIL | C-08 to C-13 (6/8) | **97.5** | Golden |
| V-02 | PASS | FAIL | C-08 to C-14 (7/8) | **98.75** | Golden |
| V-03 | FAIL | FAIL | C-08 to C-13 (6/8) | **97.5** | Golden |
| V-04 | FAIL | PASS | C-08 to C-13 + C-15 (7/8) | **98.75** | Golden |

All four variations remain Golden. The rubric now differentiates them where v3 could not.

---

**What changed v3 → v4:**

**C-14 -- Severity-first field sequencing** (from V-02)
V-02's architecture made severity the first sequenced event: severity collected and confirmed first, then -- and only then -- the collection form is presented. This means template selection gates collection rather than just formatting. The practical effect: a user who enters `outage` gets rejected and re-prompted before any other field is touched, and once a valid severity is confirmed, the correct collection form and output template are determined in a single step. V-01, V-03, and V-04 all enforce severity vocabulary (C-02 pass) but none impose an explicit sequencing constraint on when severity is collected relative to other fields.

**C-15 -- Macro-phase hard boundary** (from V-04)
V-04 compressed the four-operation sequence (collect, draft, validate, write) into two named macro-phases with a hard stop at the phase boundary. The V-04 architectural note identifies the key distinction: "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE" is structurally harder to skip than a pre-write checklist embedded in a step sequence -- the gate is a phase transition, not a step within a phase. V-03's named VALIDATE phase achieves a blocking gate (C-10 pass) but does not compress to a two-phase macro structure; V-02's named STEP 4 -- PRE-WRITE GATE achieves an explicit gate (C-10 pass) but remains a step within a linear sequence. Neither qualifies. The criterion specifically rewards the architectural insight that two-phase compression makes the gate location unambiguous.

**Key finding from Round 3:** All four variations scored 100/100 under v3, masking real architectural differences. Under v4, V-02 and V-04 score 98.75 by passing one new aspirational criterion each (C-14 and C-15 respectively), while V-01 and V-03 score 97.5 passing neither. The rubric now surfaces the severity-first sequencing pattern (V-02) and the macro-phase compression pattern (V-04) as distinct achievable targets for future variations.

**C-14/C-15 independence:** The two new criteria are independent. A skill could implement severity-first sequencing without macro-phase structure (V-02), macro-phase structure without severity-first sequencing (V-04), both simultaneously, or neither. A variation passing both would score 100 under v4 -- attainable but not yet demonstrated.
```
