```markdown
# Rubric: rhythm-rebuttal (v5)

## Change Log

### v5 (2026-03-19) — R4 excellence patterns

**Formula update**: aspirational denominator changes from `/11` to `/14` (11 criteria → 14 criteria).

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-20 | Pattern 1 `rule violation consequence as pre-generation enforcement` | Each RULE-N carries an explicit "Violation: [specific failure mode]" clause — transforms behavioral instructions into structurally binding constraints with named stakes visible before the first exchange is written, shifting non-compliance detection from post-hoc review to pre-generation reading |
| C-21 | Pattern 2 `pre-classification type audit as upstream error gate` | Phase 3.5 requires one explicit distinguishing justification sentence per scope, framing, or methodological assignment before forecasting — the three most confusion-prone types are caught at the earliest possible gate before any misclassification propagates to the forecast table, exchange, or cover letter |
| C-22 | Pattern 3 `forecast flag carry-forward as live exchange annotation` | Phase 4 forecast rows targeting specific R-IDs are carried into Phase 5 exchange headers as FLAGGED annotations ("FLAGGED: [F-0N] [predicted failure mode — resist it]"), making the predicted failure visible at the moment of writing; Phase 6b validates FLAGGED exchanges first (did the predicted failure occur?) then checks unflagged exchanges (did any unpredicted failure occur?), creating two structurally distinct accuracy checks |

### v4 (2026-03-19) — R3 excellence patterns

**Formula update**: aspirational denominator changes from `/8` to `/11` (8 criteria → 11 criteria).

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-17 | Pattern 1 `format-as-rule architectural convergence` | Exchange template declared as a numbered RULE in the pre-workflow constraints block — one surface satisfies both C-14 (rules front-loaded) and C-16 (format enforced) rather than requiring two separate declarations |
| C-18 | Pattern 2 `forecast table specificity as falsifiability` | Forecast step uses a structured table (R-ID / predicted failure mode / trigger sentence) that enables row-by-row ACCURATE / MISSED / OVERSTATED validation in the amendment pass, turning C-15 from retrospective observation into a calibration loop |
| C-19 | Pattern 3 `type-response coupling by construction` | Per-type AUTHOR RESPONDS starter templates mean a wrong type assignment at Phase 3 produces a visibly wrong response at Phase 5, moving C-06 enforcement from the decomposition table to the exchange output itself |

### v3 (2026-03-19) — R2 excellence patterns

**Formula update**: aspirational denominator changes from `/5` to `/8` (5 criteria → 8 criteria).

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-14 | V-04 `constraint-first-register` | Critical behavioral rules hoisted into a pre-workflow RULE-N block, eliminating mid-workflow rule blindness |
| C-15 | V-03 `amendment-predictive-forecast` | Weakness forecast written before drafting — amendment pass validates prediction, not just observes post-hoc |
| C-16 | V-02 `dialogue-exchange-format` | Three-part REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME format makes concern merging structurally impossible |

---

## Scoring Formula

| Tier | Points | Formula |
|------|--------|---------|
| Essential (C-01–C-05) | 60 | 12 pts each |
| Recommended (C-06–C-08) | 30 | 10 pts each; PARTIAL = 5 |
| Aspirational (C-09–C-22) | 10 | (passed / **14**) * 10 |

Golden threshold: >= 90 AND all essential pass.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | Concerns decomposed individually | correctness | essential | Every reviewer concern is given its own R-ID entry. No merging of distinct concerns into a single response block. Pass if zero merged responses. |
| C-02 | Every concern receives a full response | coverage | essential | Each R-ID entry has a substantive response that addresses the specific concern raised. No R-ID entry is skipped, deferred, or answered with a placeholder. Pass if 100% of concerns have responses. |
| C-03 | P1 no-change requires overcoming inertia | depth | essential | The skill explicitly names "no change to manuscript" as the default inertia for P1 concerns. Author must produce scientific evidence that overcomes inertia — not merely justify position. The framing appears as a binding rule, not a suggestion. |
| C-04 | Professional register maintained throughout | behavior | essential | All responses use professional academic language. No defensive, dismissive, or adversarial phrasing. At least three register-preservation strategies are named (e.g., "thank the reviewer," "acknowledge the concern before responding," "hedge disagreement"). |
| C-05 | Correct output path; integer frontmatter | format | essential | File is written to `signals/rhythm/rebuttal/{topic}-rebuttal-{date}.md`. Frontmatter contains all required fields: skill, topic, date, reviewer_count, concerns_addressed, manuscript_changes, no_change_responses. Values are integers, not placeholders. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | Concern types are correctly classified | correctness | recommended | Each concern is assigned one of the six defined types: factual, methodological, scope, framing, statistical, presentation. Classification matches the nature of the concern (e.g., a data error is "factual" not "framing"). Pass if >= 80% of type assignments are defensible. |
| C-07 | Cover letter present and structurally correct | coverage | recommended | Output includes a two-paragraph cover letter. Paragraph 1 thanks reviewers and names 3-4 key changes. Paragraph 2 flags any areas of respectful disagreement (or explicitly notes there are none). |
| C-08 | Amendment pass identifies real weaknesses | depth | recommended | Phase 5 names three specific responses that need strengthening, correctly labeled as: too defensive, concedes too much, or too brief. Each flag targets a genuine weakness in the draft response, not a trivially correct observation. |

---

## Aspirational Criteria (10 pts total)

Denominator: 14. Score = (criteria passed / 14) * 10.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | No-change responses are brief and non-defensive | behavior | Any response ending in "No change to manuscript" is concise (1 paragraph max), states a clear scientific rationale, and does not over-argue. Pass if all no-change responses meet this standard AND the constraint is stated explicitly in the skill (not just implied by format). |
| C-10 | Scope concerns handled distinctively | depth | Concerns typed as "scope" use the brief, non-defensive pattern ("beyond scope of this paper") without dismissing the reviewer. Scope responses are noticeably shorter and less argumentative than methodological or factual responses. Pass if all scope-typed responses follow this pattern. |
| C-11 | P1 no-change responses framed as inertia to overcome | depth | The skill explicitly names "no change to manuscript" as the default inertia competitor for P1 concerns — author must OVERCOME inertia with evidence, not merely justify position. A framing statement to this effect appears in the P1 rules section. Pass if the inertia/burden framing is present, not just a generic "justification required" rule. Source: V-05 C-03 strongest implementation. |
| C-12 | Cover letter drafted before individual responses | behavior | The skill instructs the author to write (or draft) the cover letter before completing individual response blocks, committing to a revision narrative before individual responses can erode it. Pass if the cover letter phase appears structurally earlier than the response-drafting phase. An amendment pass that reconciles the committed cover letter against delivered responses is sufficient evidence. Source: V-01, V-05 cover-first commitment anchor. |
| C-13 | Severity tier headers in response section | format | `--- P1 CONCERNS ---`, `--- P2 CONCERNS ---`, `--- P3 CONCERNS ---` tier headers appear in the response letter section (Phase 5), not only in the classification table. |
| C-14 | Critical constraints in pre-workflow RULE-N block | format | A numbered RULE-N block before all phases covers at minimum the no-change constraint (RULE-2 equivalent) and the P1 inertia constraint (RULE-1 equivalent). Rules are encountered before the workflow starts, not mid-stream. |
| C-15 | Weakness forecast precedes response drafting | depth | A forecast step (predicting likely response failures) appears before the drafting phase. The amendment pass validates the forecast, not merely observes post-hoc. PARTIAL on C-08 does not imply PARTIAL on C-15 — they measure different things (housekeeping vs. calibration). |
| C-16 | Dialogue exchange format (REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME) | format | Three-part atomic exchange template is present and applied consistently in the response section. Because each exchange is a discrete atomic unit, concern merging requires active effort to break the template. Distinct from C-01 (which requires correct decomposition) — C-16 is the format that enforces C-01 mechanically. |
| C-17 | Exchange format declared as numbered RULE in pre-workflow constraints block | format | The three-part dialogue exchange format (C-16) is declared as a numbered RULE (e.g., RULE-8) in the pre-workflow constraints block rather than as mid-workflow guidance. A single architectural surface satisfies both C-14 (rules front-loaded) and C-16 (format enforced as binding rule). Pass if the exchange template rule appears in the RULE-N block, not only in the phase instructions. |
| C-18 | Weakness forecast uses structured table with trigger column | depth | The forecast step (C-15) uses a structured table with columns R-ID / predicted failure mode / trigger sentence rather than prose predictions. The trigger column forces a specific causal claim that the amendment pass can validate row-by-row as ACCURATE / MISSED / OVERSTATED. Pass if both the structured table and the row-by-row validation are present. |
| C-19 | Per-type AUTHOR RESPONDS templates (type-response coupling by construction) | format | Six per-type AUTHOR RESPONDS starter templates (factual, methodological, scope, framing, statistical, presentation) are present in the Phase 5 exchange block. A wrong type assignment at Phase 3 produces a visibly wrong response template at Phase 5, moving C-06 enforcement from the decomposition table to the exchange output itself. Pass if all six type templates are present and applied. |
| **C-20** | **Rule violation consequences declared per RULE-N (pre-generation enforcement)** | **format** | **Each RULE-N entry in the pre-workflow constraints block carries an explicit "Violation: [specific failure mode]" clause describing the named consequence of non-compliance. The consequence makes non-compliance visible before the first exchange is written — shifting detection from post-hoc review to pre-generation reading. Pass if at minimum RULE-1 (P1 inertia), RULE-2 (no-change), and RULE-8 (exchange format) carry explicit violation consequence clauses. Distinct from C-14 (which requires rules to be front-loaded) — C-20 requires each rule to declare its cost.** |
| **C-21** | **Phase 3.5 upstream type audit for ambiguous concern types** | **depth** | **A Phase 3.5 step requires one explicit distinguishing justification sentence per scope, framing, or methodological type assignment before the forecast is written. The sentence must state the specific distinguishing reason for this concern (not a restatement of the type definition), catching the three most confusion-prone types at the earliest possible gate before misclassification propagates to the forecast table, the exchange, or the cover letter. Pass if Phase 3.5 appears before Phase 4 and targets scope, framing, and methodological assignments specifically. Distinct from C-06 (which requires defensible assignments) — C-21 is the structural gate that forces committed justification output before propagation.** |
| **C-22** | **Forecast flags carried forward as live Phase 5 exchange annotations** | **depth** | **Phase 4 forecast rows targeting specific R-IDs are carried into Phase 5 exchange headers as FLAGGED annotations (e.g., "FLAGGED: [F-0N] [predicted failure mode — resist it]"), making the predicted failure mode visible at the moment of writing the exchange. Phase 6b validates FLAGGED exchanges first (did the predicted failure occur?) before checking unflagged exchanges (did any unpredicted failure occur?), creating two structurally distinct accuracy checks. Pass if both the FLAGGED carry-forward in Phase 5 headers and the two-check Phase 6b validation structure are present. Distinct from C-15 (which requires the forecast to precede drafting) and C-18 (which requires the forecast table format) — C-22 is the mechanism that eliminates isolation between the forecast step and the drafting step.** |
```
