Reading the scorecard carefully for new patterns not yet encoded in v5.

**New patterns visible:**

1. **V-04 "completion condition embeds dispatch verification"**: Current C-16 requires the completion condition to name a verifiable state — but does not require that state to verify C-17 compliance. V-04's Phase A completion condition explicitly requires that both the collection schema *and* the output template were dispatched by severity confirmation, making the gate verify unified dispatch, not merely field presence. A skill can pass C-16 with a state like "all fields confirmed and non-empty" without verifying dispatch linkage. New criterion: **C-18 — completion condition embeds dispatch verification**.

2. **V-04 "sub-operation headings encode dispatch provenance"**: Sub-operation headings include explicit provenance markers (e.g., "dispatched by severity in A1") making the C-17 dispatch chain traceable through the document structure without re-reading A1. A heading like "A2: Load Collection Form" names the operation but not its dispatch origin. New criterion: **C-19 — dispatch provenance encoded in sub-operation headings**.

Aspirational pool grows 10 → 12; formula denominator updates.

---

```markdown
# file-issue -- Scoring Rubric v6

**Skill**: `file-issue`
**Rubric version**: v6
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
| C-18 | **Completion condition embeds dispatch verification** | structure | aspirational | The Phase A completion condition explicitly requires that both the collection schema and the output template were dispatched by severity confirmation -- not merely that both are present or non-empty. The gate must verify the dispatch linkage, making C-16 compliance also verify C-17 compliance. A completion condition that checks "all required fields confirmed and non-empty" without verifying that they were collected via a severity-dispatched schema does not qualify. A skill can pass C-16 without passing C-18. *(Excellence signal: V-04 -- "Phase A completion state (1) explicitly requires that both collection schema and output template were dispatched by severity confirmation, making the gate verify C-17 compliance not just field presence.")* |
| C-19 | **Dispatch provenance encoded in sub-operation headings** | structure | aspirational | Sub-operation headings include explicit dispatch provenance markers identifying where the dispatch for that sub-operation originated (e.g., "A2: Load Collection Schema (dispatched by severity in A1)"). The C-17 dispatch chain must be traceable through the document structure without re-reading A1. A heading that names the operation without naming its dispatch origin does not qualify; the provenance must appear in the heading itself, not only in the body of the sub-operation. *(Excellence signal: V-04 -- "sub-operation headings encode dispatch provenance ('dispatched by severity in A1') making the C-17 chain traceable through the structure without re-reading A1.")* |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

### Round 4 scores under v6

| Variation | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Aspirational hits | Composite | Verdict |
|-----------|------|------|------|------|------|------|-------------------|-----------|---------|
| V-01 | PASS | FAIL | FAIL | PASS | FAIL | FAIL | C-08 to C-14, C-17 (8/12) | **96.67** | Golden |
| V-02 | FAIL | PASS | PASS | FAIL | FAIL | FAIL | C-08 to C-13, C-15, C-16 (8/12) | **96.67** | Golden |

### Round 5 scores under v6

| Variation | C-17 | C-18 | C-19 | Aspirational hits | Composite | Verdict |
|-----------|------|------|------|-------------------|-----------|---------|
| V-04 | PASS | PASS | PASS | 12/12 | **100.0** | Golden |
| V-05 | PASS | PASS | PASS | 12/12 | **100.0** | Golden |
| V-03 | FAIL | FAIL | FAIL | 9/12 | **97.5** | Golden |
| V-01 | PASS | FAIL | FAIL | 8/12 | **96.67** | Golden |
| V-02 | FAIL | FAIL | FAIL | 8/12 | **96.67** | Golden |

---

## Detailed Scorecards

### V-01 -- Unified Dispatch, No Macro-Phase

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | PASS | All four fields collected; severity rejection enforced |
| C-02 | Severity vocabulary enforcement | PASS | Four values only; reject and re-prompt |
| C-03 | GitHub issue format | PASS | Title + structured sections per severity |
| C-04 | Artifact path under simulations/feedback/ | PASS | Path specified with skill name and date |
| C-05 | Actionable, specific issue title | PASS | Per-severity title patterns name skill + symptom |
| C-06 | Sufficient reproducibility context | PASS | Invocation, topic, chain, steps in body |
| C-07 | Repo open offer presented | PASS | `gh issue create` command in OFFER step |
| C-08 | Severity-appropriate framing | PASS | Tone guidance per severity level |
| C-09 | Skill context enrichment | PASS | Chain, version, scope beyond four required fields |
| C-10 | Pre-write validation gate | PASS | Structured gate step before write |
| C-11 | Corrective actions per validation check | PASS | "Correction on fail" column present on all six rows |
| C-12 | Per-severity body templates | PASS | Four structurally distinct templates; crash has Priority+Impact; improvement has Acceptance condition |
| C-13 | Severity-labeled issue creation | PASS | `--label "{severity}"` in OFFER command |
| C-14 | Severity-first field sequencing | PASS | "Severity is the pipeline key. Do not collect any other field until severity is confirmed." First step. |
| C-15 | Macro-phase hard boundary | FAIL | Linear 5-step structure. STEP 4 is a gate but not a macro-phase; a five-step sequence with a gate at step 4 does not qualify. |
| C-16 | Phase boundary completion condition | FAIL | No macro-phase boundary; no verifiable completion condition defined. |
| C-17 | Severity-driven unified pipeline dispatch | PASS | "Severity confirmation is the single event that dispatches both: (a) the collection schema... and (b) the output template... Both selections are made by this one confirmation event." Explicit unified dispatch. |
| C-18 | Completion condition embeds dispatch verification | FAIL | No macro-phase boundary means no completion condition exists at all; C-18 cannot be satisfied without C-15 and C-16. |
| C-19 | Dispatch provenance encoded in sub-operation headings | FAIL | No sub-operation headings with provenance markers observed; linear step structure does not encode dispatch origin in headings. |

**Essential**: 4/4 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 8/12 = 6.67
**Composite: 96.67** | **Golden**

---

### V-02 -- Completion Condition in Macro-Phase (C-16, single axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | PASS | A1 collects all four fields; severity rejection enforced |
| C-02 | Severity vocabulary enforcement | PASS | Exactly four values; reject and re-prompt at A1 |
| C-03 | GitHub issue format | PASS | Four per-severity templates in A2 with title + structured sections |
| C-04 | Artifact path under simulations/feedback/ | PASS | B2 specifies `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` |
| C-05 | Actionable, specific issue title | PASS | Per-severity title patterns name skill + symptom |
| C-06 | Sufficient reproducibility context | PASS | Invocation, topic, chain, steps in all templates |
| C-07 | Repo open offer presented | PASS | B3 OFFER includes full `gh issue create` |
| C-08 | Severity-appropriate framing | PASS | Template tone guidance (crash=urgent+impact; improvement=proposal+acceptance) |
| C-09 | Skill context enrichment | PASS | Delta, scope, acceptance condition, chain, version beyond four required |
| C-10 | Pre-write validation gate | PASS | B1 is the gate; "Do not begin B2 until all rows pass" |
| C-11 | Corrective actions per validation check | PASS | "Correction on fail" column on every B1 row |
| C-12 | Per-severity body templates | PASS | Four distinct templates; crash has Priority+Impact; improvement has Acceptance condition |
| C-13 | Severity-labeled issue creation | PASS | `--label "{severity}"` in B3 command |
| C-14 | Severity-first field sequencing | FAIL | A1 presents all four fields simultaneously: "1. Skill, 2. Expected, 3. Actual, 4. Severity." Severity listed fourth; no instruction to collect severity before other fields. |
| C-15 | Macro-phase hard boundary | PASS | Phase A (A1+A2 -- field intake + authoring) and Phase B (B1+B2+B3) with "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE." |
| C-16 | Phase boundary completion condition | PASS | Three-condition verifiable state: (1) all four fields confirmed and non-empty, (2) severity validated as one of four enum values, (3) draft shown to user and not yet revised for Phase B. |
| C-17 | Severity-driven unified pipeline dispatch | FAIL | Collection in A1 is a fixed form for all severities -- all four fields presented simultaneously regardless of severity. Only A2 template selection is severity-driven. Collection schema not dispatched by severity; it is a generic intake form. |
| C-18 | Completion condition embeds dispatch verification | FAIL | C-16 completion condition verifies field presence and severity validity, but not that the collection schema was dispatched by severity. Because C-17 fails (collection schema is severity-independent), the completion condition cannot verify dispatch linkage that does not exist. |
| C-19 | Dispatch provenance encoded in sub-operation headings | FAIL | Sub-operation headings name operations (A1, A2, B1, B2, B3) without encoding dispatch provenance. No evidence of provenance markers in heading text. |

**Essential**: 4/4 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 8/12 = 6.67
**Composite: 96.67** | **Golden**

---

### V-03 -- Combined C-14 + C-15 + C-16, Without Unified Dispatch

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | PASS | A1 confirms severity; A2 loads per-severity form with all required fields marked |
| C-02 | Severity vocabulary enforcement | PASS | A1: four values only; reject with re-prompt |
| C-03 | GitHub issue format | PASS | Four per-severity templates in A3 with title + sections |
| C-04 | Artifact path under simulations/feedback/ | PASS | B2 specifies `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` |
| C-05 | Actionable, specific issue title | PASS | Per-severity title patterns name skill + symptom |
| C-06 | Sufficient reproducibility context | PASS | Invocation, topic, steps, scope in templates |
| C-07 | Repo open offer presented | PASS | B3 OFFER with `gh issue create` |
| C-08 | Severity-appropriate framing | PASS | Crash=urgent+priority+impact; improvement=proposal+acceptance in templates and B1 tone check |
| C-09 | Skill context enrichment | PASS | Scope, references, acceptance condition, chain, version per severity |
| C-10 | Pre-write validation gate | PASS | B1 is the gate before B2 with blocking instruction "Do not begin B2 until all rows pass" |
| C-11 | Corrective actions per validation check | PASS | "Correction on fail" column on every B1 row |
| C-12 | Per-severity body templates | PASS | Four distinct templates; crash has Priority+Impact; improvement has Acceptance condition |
| C-13 | Severity-labeled issue creation | PASS | `--label "{severity}"` in B3 command |
| C-14 | Severity-first field sequencing | PASS | A1: "first and only operation until confirmed." "Do not collect any other field until a valid severity value is confirmed." |
| C-15 | Macro-phase hard boundary | PASS | Phase A (A1+A2+A3 -- three sub-operations) and Phase B (B1+B2+B3) with "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE." |
| C-16 | Phase boundary completion condition | PASS | Three-condition verifiable state: (1) severity confirmed as valid enum (A1 done), (2) all required fields from severity-appropriate form non-empty (A2 done), (3) draft shown to user (A3 done). |
| C-17 | Severity-driven unified pipeline dispatch | FAIL | A1: "Severity determines the collection form used in A2 and the output template used in A3." This is sequential determination -- A2 and A3 named as separate downstream targets of severity. No "single event that simultaneously dispatches both" framing; no unified dispatch declaration. C-17 requires the dispatch relationship to be framed as a unified single-event dispatch, not inferrable from sequential enumeration. |
| C-18 | Completion condition embeds dispatch verification | FAIL | C-16 completion condition checks field presence per severity-appropriate form (A2 done) and draft generation (A3 done), but does not require verification that both pipelines were dispatched by a single unified severity event. Because C-17 fails -- the dispatch relationship is sequential, not unified -- the completion condition cannot embed verification of a unified dispatch that was not declared. |
| C-19 | Dispatch provenance encoded in sub-operation headings | FAIL | Sub-operation headings name operations ("A1: Severity Intake", "A2: Load Collection Form", "A3: Draft Output") without encoding dispatch provenance. No evidence that headings carry markers tracing operations back to the A1 dispatch event. |

**Essential**: 4/4 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 9/12 = 7.5
**Composite: 97.5** | **Golden**

**C-17 judgment (carried forward from v5)**: V-03's A1 links both pipelines to severity but via "determines X and Y" -- a sequential list of downstream effects. C-17's pass condition requires unified dispatch framing: severity as the explicit single-event dispatch key, not as the implicit cause of two downstream selections. "Determines X and Y" describes what severity affects; "simultaneously dispatches both (a)... and (b)" declares severity as the unified pipeline key. The gap between V-03 (97.5) and V-04 (100.0) under v6 is the unified dispatch framing (C-17) plus the two structural properties that require C-17 compliance to be present first (C-18, C-19).

---

### V-04 -- Full Combination: C-14 + C-15 + C-16 + C-17 + C-18 + C-19

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Required fields captured | PASS | Per-severity collection schemas; required markers explicit |
| C-02 | Severity vocabulary enforcement | PASS | Four values; reject with re-prompt at A1 |
| C-03 | GitHub issue format | PASS | Four per-severity output templates with title + sections |
| C-04 | Artifact path under simulations/feedback/ | PASS | B2 specifies `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` |
| C-05 | Actionable, specific issue title | PASS | Per-severity title patterns name skill + symptom |
| C-06 | Sufficient reproducibility context | PASS | Invocation, topic, chain, scope in templates |
| C-07 | Repo open offer presented | PASS | B3 OFFER with `gh issue create` |
| C-08 | Severity-appropriate framing | PASS | Per-template tone; B1 tone check row references template tone |
| C-09 | Skill context enrichment | PASS | Per-severity enrichment fields; scope, acceptance condition, chain, version |
| C-10 | Pre-write validation gate | PASS | B1 is the gate; "Do not begin B2 until all rows pass" |
| C-11 | Corrective actions per validation check | PASS | "Correction on fail" column present on all rows |
| C-12 | Per-severity body templates | PASS | Four structurally distinct templates; crash has Priority+Impact; improvement has Acceptance condition |
| C-13 | Severity-labeled issue creation | PASS | `--label "{severity}"` in B3 OFFER command |
| C-14 | Severity-first field sequencing | PASS | A1: severity is the first and only step until confirmed; explicit blocking before any other field |
| C-15 | Macro-phase hard boundary | PASS | Phase A (A1+A2+A3) and Phase B (B1+B2+B3) with "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE" |
| C-16 | Phase boundary completion condition | PASS | Three-condition verifiable state at boundary: (1) severity confirmed and both pipelines dispatched from A1, (2) all severity-dispatched collection fields non-empty, (3) severity-dispatched output template rendered and shown to user |
| C-17 | Severity-driven unified pipeline dispatch | PASS | A1: "severity confirmation simultaneously dispatches both (a) the collection schema (A2) and (b) the output template (A3)." Explicit unified single-event dispatch with (a)/(b) enumeration. |
| C-18 | Completion condition embeds dispatch verification | PASS | C-16 completion condition item (1) explicitly requires that "both collection schema and output template were dispatched by severity confirmation" -- making the gate verify C-17 compliance, not merely field presence. Field presence in item (2) is additionally conditioned on the severity-dispatched schema, not a generic form. |
| C-19 | Dispatch provenance encoded in sub-operation headings | PASS | Sub-operation headings carry explicit provenance markers: "A2: Load Collection Schema (dispatched by severity in A1)" and "A3: Load Output Template (dispatched by severity in A1)". C-17 dispatch chain is traceable from the heading text alone without re-reading A1. |

**Essential**: 4/4 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: 12/12 = 10.0
**Composite: 100.0** | **Golden**

---

## Summary of changes v5 → v6

Two new aspirational criteria added from Round 5 excellence signals. Both require C-17 compliance as a precondition -- a skill that fails C-17 cannot satisfy either.

**C-18** closes the gap between a completion condition that verifies state and one that verifies dispatch. C-16 required a verifiable state; C-18 requires that state to be dispatch-linked -- the gate must confirm that both pipelines were dispatched from severity, making Phase A completion a structural proxy for C-17 verification.

**C-19** makes the C-17 dispatch chain legible at the document structure level. A reader should be able to identify which sub-operations were severity-dispatched from the heading text alone. This is a documentation-of-intent pattern: the architecture is declared in the structure, not only in the operational prose of A1.

Formula denominator updated: aspirational pool 10 → 12.

Score impact on prior variations: R4 and R5 variations that did not achieve C-17 (V-02, V-03) or lacked a macro-phase entirely (V-01) also fail C-18 and C-19, reducing their composite scores under v6. V-04 and V-05, which were the first variations to achieve C-17, retain 100.0 as both new criteria are present in their design.
```
