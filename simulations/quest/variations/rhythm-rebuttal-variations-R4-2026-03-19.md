## R4 Variations — rhythm-rebuttal

Written to `simulations/quest/variations/rhythm-rebuttal-variations-R4-2026-03-19.md`.

---

**The R4 problem**: R3 V-05 already achieves 11/11 aspirational criteria. R4 is not about hitting C-17/C-18/C-19 — they are proven. R4 is about **robustness under stress**: silent failures that only appear with large, adversarial, or emotionally charged reviewer sets.

**Three R4 variation axes:**

| Variation | Axis | Key bet |
|-----------|------|---------|
| **V-01** | Rule consequence declarations | Each RULE states its violation consequence — non-compliance visible before generation, not after review; RULE-8's "incomplete, must rewrite" is categorically different from "use this format" |
| **V-02** | Phase 3.5 type audit | Explicit scope/framing/methodological verification before forecast — misclassification caught at earliest possible point, before it propagates to Phase 5 templates |
| **V-03** | Forecast-to-exchange traceability | Phase 4 forecast rows carry into Phase 5 exchange headers as FLAGGED annotations — author sees the predicted failure mode at the moment of writing, not in a pre-draft memo; Phase 6b validates FLAGGED exchanges first |
| **V-04** | A+B: consequences + type audit | |
| **V-05** | A+B+C: all three | Maximum: consequence-declared rules, upstream audit, forecast survives into exchange output |

**What changed from R3**: All five variations maintain C-09 through C-19 (11/11). The structural changes target the gap between "skill correctly specified" and "skill correctly executed under adversarial load." V-03 is the novel structural risk — FLAGGED exchange headers are a new pattern not present in any prior round.
B combined | Consequence declarations + type audit |
| **V-05** | A+B+C combined | All axes at maximum — 11/11 aspirational target with structural robustness for adversarial inputs |

**What changed from R3**: Every R4 variation maintains C-14 through C-19. The structural
changes target the gap between "skill correctly specified" and "skill correctly executed
under pressure." The R3 V-05 architecture is the proven floor; R4 tests hardening above it.

---

## Variation Axes (R4)

**Axis A — Rule consequence declarations**: R3 RULE-N blocks describe behavior. V-01 adds
a consequence clause to each rule: what fails, specifically, if the rule is violated.
RULE-8 reads "Violation: any Phase 5 block missing REVIEWER SAID / AUTHOR RESPONDS /
MANUSCRIPT OUTCOME is incomplete — rewrite before submission." Consequences stated before
generation begins are structurally different from consequences discovered during review.

**Axis B — Pre-classification type audit (Phase 3.5)**: R3 provides a misclassification
guide in Phase 3, but the author assigns types and moves on. V-02 adds a Phase 3.5
step: for every concern assigned scope, framing, or methodological (the three most often
confused), state explicitly "R-NN typed [type] not [most likely alternative] because
[one-sentence distinguishing reason]." This step runs between classification and forecasting,
catching errors at the earliest possible point.

**Axis C — Forecast-to-exchange traceability**: R3 Phase 4 forecast rows are written before
Phase 5 but not carried into Phase 5. V-03 annotates each exchange header with any forecast
flag targeting it: "Exchange R-03 | P1 | [F-01: too defensive]". Phase 6b validates
FLAGGED exchanges first, then checks for unflagged failures. The forecast is no longer a
pre-generation memo — it becomes an active label on the exchange itself.

---

## V-01 — Rule Consequence Declarations

**Axis**: RULE-N block with violation consequences (single axis A)
**Hypothesis**: A rule that states "Violation: [specific failure]" is structurally different
from a rule that states "You must [behavior]." Consequence declarations make non-compliance
visible before generation begins rather than detectable only in post-hoc review. RULE-8's
consequence ("any Phase 5 block missing the three-part structure is incomplete") makes the
format non-optional in a way that prescription alone cannot achieve. C-17 is satisfied at
maximum signal strength: the format is a binding rule with a named failure mode.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding constraints — including the
required exchange format — are declared before any work begins. Each rule states its violation
consequence. A rule whose consequence is named before generation is structurally harder to
violate than a rule whose consequence is discovered after review.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.
Violation: a P1 exchange with no-change and no compelling scientific counter-evidence
fails the artifact — the response will be rejected or escalated by the editor.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue.
Violation: a no-change response longer than 1 paragraph reads as defensive regardless of
content quality; editors and reviewers discount long justifications for inaction.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Close.
Violation: a multi-paragraph scope response is a category error — it concedes that the
scope challenge has merit and invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only. No
response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.
Violation: any response using combative or dismissive language is a professional failure
that may cause rejection regardless of the scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same reviewer paragraph.
Violation: a merged exchange will appear in the output as a single REVIEWER SAID block
quoting multiple distinct concerns — the editorial office will return it for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

Violation: any Phase 5 block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten before submission. RULE-5 and RULE-8
together enforce atomicity: a merged concern cannot produce a valid REVIEWER SAID block.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter before decomposing or responding to any concern. Commitment anchor:
commit to the revision narrative before drafting can erode it.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

Updated in Phase 6a to reflect actual outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — the type assigned here directly gates the AUTHOR RESPONDS
strategy in Phase 5. Assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" — factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" — methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" — scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" — framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" — statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance — RULE-1 applies (violation: no-change without compelling evidence fails artifact)
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only — generic statements ("P1 concerns are hard") do not count.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [what makes this concern invite over-explanation or emotional register?] |
| F-02 | [R-NN] | concedes too much | [why would the draft over-concede? reviewer overreaching, emotional pressure?] |
| F-03 | [R-NN] | too brief | [why might this concern be under-addressed? buried, overlapping, deferred?] |

Hold this forecast while drafting Phase 5. Phase 6b validates each row.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange (Violation: see RULE-8 consequence above). Write in severity
order:

--- P1 CONCERNS (RULE-1 applies — inertia must be overcome with evidence) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. Use the type-specific AUTHOR RESPONDS template:

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification or fix description.]
                  We have [specific change or explanation] in §N."

  scope:          [2-3 sentences. RULE-3. "This question lies beyond the scope of the present
                  paper, which [state claim space]. We note it as a direction for future work."]

  framing:        "The paper claims [exact manuscript claim]. The reviewer may be reading this
                  as [misread]. We have added [clarifying language] to §N."

  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"

  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale. RULE-1 if P1, RULE-2 always,
RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation**: Compare Phase 2 cover letter against Phase 5 outcomes.
Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 for any shift
in disagreement framing.

**6b. Forecast validation**: Row-by-row check against Phase 4 forecast table:

| Forecast | R-ID | Predicted failure | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|-------------------------------|
| F-01 | | too defensive | |
| F-02 | | concedes too much | |
| F-03 | | too brief | |

Name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (may match forecast rows or name new targets):
1. [R-NN] — too defensive: [rewrite AUTHOR RESPONDS opening to remove defensive register]
2. [R-NN] — concedes too much: [what to hold; why the concession went too far]
3. [R-NN] — too brief: [what is understated; what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-02 — Pre-Classification Type Audit

**Axis**: Phase 3.5 type audit between decomposition and forecast (single axis B)
**Hypothesis**: R3 provides a misclassification guide during Phase 3 but the author assigns
types and moves on with no verification. Adding Phase 3.5 — an explicit audit for every
scope, framing, or methodological assignment (the three most misclassified types) — catches
errors at the earliest possible point, before they propagate to the forecast table, the
exchange, or the cover letter. C-19's type-response coupling is strongest when the coupling
begins at classification, not at drafting. A verified Phase 3 type is structurally less
likely to produce a wrong Phase 5 response than an unverified one.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules — including the required
exchange format — are declared before any work begins. A type audit step between decomposition
and forecast catches classification errors before they reach the exchange phase. Per-type
AUTHOR RESPONDS templates mean a wrong type produces a visibly wrong response — the audit
minimizes the chance of reaching that diagnostic.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue. A long no-change reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Close.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only. No
response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same reviewer paragraph.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

  RULE-5 and RULE-8 together: one exchange per concern. A merged concern cannot produce a
  valid REVIEWER SAID block. The type assigned in Phase 3 (and verified in Phase 3.5)
  determines the AUTHOR RESPONDS strategy in Phase 5.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter before decomposing or responding to any concern. Commitment anchor:
commit to the revision narrative before drafting can erode it.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

Updated in Phase 6a to reflect actual outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" — factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" — methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" — scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" — framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" — statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance — RULE-1 applies; "no change" is the inertia to overcome
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 3.5 -- TYPE AUDIT

For every concern assigned scope, framing, or methodological, verify the assignment against
the most likely alternative before proceeding. Do this now — after the Phase 3 table is
complete and before writing the forecast.

For each scope, framing, or methodological assignment in the table:

  R-[NN] typed [assigned type] not [most likely alternative type] because:
  [one sentence stating the specific distinguishing reason for this concern]

Example:
  R-03 typed scope not methodological because: the reviewer asks for a new experiment
  testing a different population, not a correction to the existing experimental design.

  R-07 typed framing not factual because: the paper's claim is correctly stated in §2.3;
  the reviewer is reading the abstract's shorthand as a broader claim the paper does not make.

If any assignment looks wrong on audit, correct the Phase 3 table before proceeding.
Only concerns typed scope, framing, and methodological require audit entries; factual,
statistical, and presentation assignments are self-verifying.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only — generic statements ("P1 concerns are hard") do not count.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [what makes this concern invite over-explanation or emotional register?] |
| F-02 | [R-NN] | concedes too much | [why would the draft over-concede? reviewer overreaching, emotional pressure?] |
| F-03 | [R-NN] | too brief | [why might this concern be under-addressed? buried, overlapping, deferred?] |

Hold this forecast while drafting Phase 5. Phase 6b validates each row.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies — inertia must be overcome with evidence) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. Use the type-specific AUTHOR RESPONDS template
(type verified in Phase 3.5 for scope/framing/methodological concerns):

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification or fix description.]
                  We have [specific change or explanation] in §N."

  scope:          [2-3 sentences. RULE-3. "This question lies beyond the scope of the present
                  paper, which [state claim space]. We note it as a direction for future work."]

  framing:        "The paper claims [exact manuscript claim]. The reviewer may be reading this
                  as [misread]. We have added [clarifying language] to §N."

  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"

  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale. RULE-1 if P1, RULE-2 always,
RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation**: Compare Phase 2 cover letter against Phase 5 outcomes.
Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 for any shift
in disagreement framing.

**6b. Forecast validation**: Row-by-row check against Phase 4 forecast table:

| Forecast | R-ID | Predicted failure | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|-------------------------------|
| F-01 | | too defensive | |
| F-02 | | concedes too much | |
| F-03 | | too brief | |

Name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (may match forecast rows or name new targets):
1. [R-NN] — too defensive: [rewrite AUTHOR RESPONDS opening to remove defensive register]
2. [R-NN] — concedes too much: [what to hold; why the concession went too far]
3. [R-NN] — too brief: [what is understated; what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-03 — Forecast-to-Exchange Traceability

**Axis**: Forecast flag carried into exchange header (single axis C)
**Hypothesis**: The R3 forecast (Phase 4) and the exchange log (Phase 5) are structurally
isolated — the author writes the forecast, then writes exchanges without seeing the forecast
in the same surface. V-03 annotates each Phase 5 exchange header with any forecast row
targeting it. The author sees the flag at the moment of writing, not in a separate pre-draft
step. Phase 6b validates FLAGGED exchanges first, producing two distinct accuracy checks:
forecast accuracy (did the predicted failure occur?) and coverage (did any unflagged exchange
fail?). C-18 is strengthened: the trigger column now names the mechanism the author is
watching for in real time, not just predicting before generation.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules — including the required
exchange format — are declared before any work begins. The weakness forecast is a structured
table with trigger-level specificity. Forecast rows carry forward into exchange headers:
a flagged exchange displays the predicted failure mode at the moment of writing. The author
cannot write the exchange without seeing the warning.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue. A long no-change reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Close.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only. No
response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same reviewer paragraph.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

  RULE-5 and RULE-8 together: one exchange per concern. A merged concern cannot produce a
  valid REVIEWER SAID block. Forecast flags (from Phase 4) appear in the exchange header
  when present — do not suppress or ignore them.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter before decomposing or responding to any concern. Commitment anchor:
commit to the revision narrative before drafting can erode it.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

Updated in Phase 6a to reflect actual outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — the type assigned here directly gates the AUTHOR RESPONDS
strategy in Phase 5. Assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" — factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" — methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" — scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" — framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" — statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance — RULE-1 applies; "no change" is the inertia to overcome
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only — generic statements do not count. The trigger column must commit to a causal mechanism,
not just a concern property. These rows carry forward as flags into Phase 5 exchange headers.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [what makes this concern invite over-explanation? name the mechanism, not just "it's hard"] |
| F-02 | [R-NN] | concedes too much | [why would the draft over-concede? name the reviewer move or pressure, not just "partly right"] |
| F-03 | [R-NN] | too brief | [why might this concern be under-addressed? name the structural reason it gets skipped] |

These rows carry forward: when writing Phase 5, flag each exchange that matches a forecast
row. The flag appears in the exchange header, keeping the prediction active during drafting.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies — inertia must be overcome with evidence) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. If the R-ID appears in the Phase 4 forecast table,
include the forecast flag in the exchange header. The flag makes the prediction visible
at the moment of writing.

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = F-01/F-02/F-03 target: add "| FLAGGED: [F-0N] [predicted failure mode]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification or fix description.]
                  We have [specific change or explanation] in §N."

  scope:          [2-3 sentences. RULE-3. "This question lies beyond the scope of the present
                  paper, which [state claim space]. We note it as a direction for future work."]

  framing:        "The paper claims [exact manuscript claim]. The reviewer may be reading this
                  as [misread]. We have added [clarifying language] to §N."

  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"

  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale. RULE-1 if P1, RULE-2 always,
RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation**: Compare Phase 2 cover letter against Phase 5 outcomes.
Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 for any shift
in disagreement framing.

**6b. Forecast validation**: Validate FLAGGED exchanges first (did the predicted failure
occur?), then check all remaining exchanges for unflagged failures.

FLAGGED exchanges:
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (FLAGGED exchanges take priority; add unflagged
failures as needed to reach three):
1. [R-NN] — too defensive: [rewrite AUTHOR RESPONDS opening to remove defensive register]
2. [R-NN] — concedes too much: [what to hold; why the concession went too far]
3. [R-NN] — too brief: [what is understated; what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-04 — Consequence Declarations + Type Audit (A+B)

**Axes**: RULE-N consequence declarations (A) + Phase 3.5 type audit (B) combined
**Hypothesis**: A+B together close the two most common silent-failure paths in R3: rules
stated without consequences (author reads them, applies them inconsistently, and cannot
self-diagnose the failure) and type misclassification propagating unchecked to Phase 5.
Consequence declarations make each rule's violation visible before generation; the type
audit catches the most common classification errors before the forecast table is populated.
C-17 is satisfied at maximum signal strength (RULE-8 has a named violation consequence);
C-19 is pre-validated at Phase 3.5 so a wrong type almost never reaches Phase 5.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules — including the required
exchange format — are declared before any work begins, each with a violation consequence.
A type audit step between decomposition and forecast catches misclassifications before they
propagate. Per-type AUTHOR RESPONDS templates mean a wrong type produces a visibly wrong
response; the audit minimizes the chance of reaching that diagnostic.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.
Violation: a P1 exchange with no-change and no compelling scientific counter-evidence
fails the artifact — editors treat it as a non-response.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue.
Violation: a no-change response longer than 1 paragraph reads as defensive regardless
of content quality; editors and reviewers discount long justifications for inaction.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Close.
Violation: a multi-paragraph scope response concedes that the scope challenge has merit
and invites escalation to a revision demand.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only. No
response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.
Violation: any combative or dismissive phrasing is a professional failure that may cause
rejection independent of the scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same reviewer paragraph.
Violation: a merged exchange will appear as a single REVIEWER SAID block quoting multiple
distinct concerns — the editorial office will return it for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

Violation: any Phase 5 block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten before submission. RULE-5 and RULE-8
together enforce atomicity: a merged concern cannot produce a valid REVIEWER SAID block.
The type assigned in Phase 3 (and verified in Phase 3.5) determines the AUTHOR RESPONDS
strategy in Phase 5.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter before decomposing or responding to any concern. Commitment anchor:
commit to the revision narrative before drafting can erode it.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

Updated in Phase 6a to reflect actual outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — the type assigned here is verified in Phase 3.5 before proceeding.
Assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" — factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" — methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" — scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" — framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" — statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance — RULE-1 applies (Violation: see RULE-1 consequence above)
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 3.5 -- TYPE AUDIT

For every concern assigned scope, framing, or methodological, verify the assignment now —
before writing the forecast. State one sentence per assignment:

  R-[NN] typed [assigned type] not [most likely alternative] because:
  [specific distinguishing reason for this concern, not a restatement of the type definition]

Example:
  R-03 typed scope not methodological because: the reviewer requests a new population-level
  study; the existing cohort study design is not questioned.

  R-07 typed framing not factual because: §2.3 states the claim correctly; the reviewer is
  reading the abstract shorthand as a stronger universality claim the paper does not make.

If any assignment looks wrong on audit, correct the Phase 3 table before proceeding.
Only scope, framing, and methodological assignments require audit entries.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only — generic statements do not count.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [what makes this concern invite over-explanation or emotional register?] |
| F-02 | [R-NN] | concedes too much | [why would the draft over-concede? reviewer overreaching, emotional pressure?] |
| F-03 | [R-NN] | too brief | [why might this concern be under-addressed? buried, overlapping, deferred?] |

Hold this forecast while drafting Phase 5. Phase 6b validates each row.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange (Violation: see RULE-8 consequence above). Write in severity
order:

--- P1 CONCERNS (RULE-1 applies — inertia must be overcome with evidence) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. Use the type-specific AUTHOR RESPONDS template
(type verified in Phase 3.5 for scope/framing/methodological):

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification or fix description.]
                  We have [specific change or explanation] in §N."

  scope:          [2-3 sentences. RULE-3. "This question lies beyond the scope of the present
                  paper, which [state claim space]. We note it as a direction for future work."]

  framing:        "The paper claims [exact manuscript claim]. The reviewer may be reading this
                  as [misread]. We have added [clarifying language] to §N."

  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"

  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale. RULE-1 if P1, RULE-2 always,
RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation**: Compare Phase 2 cover letter against Phase 5 outcomes.
Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 for any shift
in disagreement framing.

**6b. Forecast validation**: Row-by-row check against Phase 4 forecast table:

| Forecast | R-ID | Predicted failure | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|-------------------------------|
| F-01 | | too defensive | |
| F-02 | | concedes too much | |
| F-03 | | too brief | |

Name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (may match forecast rows or name new targets):
1. [R-NN] — too defensive: [rewrite AUTHOR RESPONDS opening to remove defensive register]
2. [R-NN] — concedes too much: [what to hold; why the concession went too far]
3. [R-NN] — too brief: [what is understated; what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-05 — Full Integration (A+B+C)

**Axes**: Consequence declarations (A) + Type audit (B) + Forecast-to-exchange traceability (C)
**Hypothesis**: All three R4 axes at maximum explicit coverage. Each RULE names its violation
consequence (A), so non-compliance is visible before generation and cannot be discovered only
in post-hoc review. Phase 3.5 type audit catches classification errors for the three most
misclassified types (B) before they reach the forecast or exchange phases. Phase 4 forecast
rows carry forward as flags into Phase 5 exchange headers (C), so the author sees the
predicted failure mode at the moment of writing — the forecast is no longer a pre-draft memo
but an active annotation. C-17, C-18, and C-19 are each hit at maximum signal strength:
RULE-8 consequence declaration (C-17), structured tabular forecast with mechanism-level
triggers and row-by-row validation on FLAGGED exchanges (C-18), type-verified per-type
templates with upstream audit (C-19).

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules — including the required
exchange format — are declared before any work begins, each with a violation consequence.
A type audit between decomposition and forecast eliminates misclassification before it
propagates. Forecast rows carry forward as flags into exchange headers: the predicted failure
mode is visible at the moment of writing, not only in a pre-draft step. The amendment pass
validates FLAGGED exchanges first, then checks for unflagged failures.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.
Violation: a P1 exchange with no-change and no compelling scientific counter-evidence
fails the artifact — editors treat it as a non-response.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue.
Violation: a no-change response longer than 1 paragraph reads as defensive regardless
of content quality.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Close.
Violation: a multi-paragraph scope response concedes that the scope challenge has merit
and invites escalation.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only. No
response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.
Violation: combative or dismissive phrasing is a professional failure that may cause
rejection independent of scientific merits.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same reviewer paragraph.
Violation: a merged exchange produces a single REVIEWER SAID block quoting multiple
distinct concerns — the editorial office will return it for revision.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.
Violation: non-integer frontmatter values fail artifact validation at write time.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.
Violation: fabricated reviewer comments constitute academic misconduct; halt immediately.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

Violation: any Phase 5 block missing REVIEWER SAID, AUTHOR RESPONDS, or MANUSCRIPT OUTCOME
is structurally incomplete and must be rewritten. RULE-5 and RULE-8 together enforce
atomicity: a merged concern cannot produce a valid REVIEWER SAID block. The type assigned
in Phase 3 (and verified in Phase 3.5) determines the AUTHOR RESPONDS strategy in Phase 5.
Forecast flags from Phase 4 appear in the exchange header — do not suppress or ignore them.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter before decomposing or responding to any concern. Commitment anchor:
commit to the revision narrative before drafting can erode it.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

Updated in Phase 6a to reflect actual outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — type is verified in Phase 3.5 before proceeding. Assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" — factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" — methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" — scope = paper doesn't claim this; methodological = it tried and failed |
| framing | Reviewer misread what the paper claims | "Factual" — framing = reviewer error; factual = paper error |
| statistical | Missing or incorrect analysis the paper should include | "Methodological" — statistical = analysis layer; methodological = experimental design |
| presentation | Clarity, structure, notation, language | Safe fallback for concerns with no scientific content impact |

Severity:
- **P1**: blocks acceptance — RULE-1 applies (Violation: see RULE-1 consequence above)
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 3.5 -- TYPE AUDIT

For every concern assigned scope, framing, or methodological, verify the assignment before
writing the forecast. State one sentence per assignment:

  R-[NN] typed [assigned type] not [most likely alternative] because:
  [specific distinguishing reason for this concern, not a restatement of the type definition]

Example:
  R-03 typed scope not methodological because: reviewer requests new population-level
  replication; the existing study design is not questioned.

  R-07 typed framing not factual because: §2.3 states the claim correctly; the reviewer
  reads the abstract shorthand as a stronger universality claim the paper does not make.

If any assignment looks wrong on audit, correct the Phase 3 table before proceeding.
Only scope, framing, and methodological assignments require audit entries.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Specific predictions
only — generic statements do not count. The trigger column must name a causal mechanism
(not just a concern property). These rows carry forward as flags into Phase 5 headers.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [name the specific author action that will cause this — not just "the concern is hard"] |
| F-02 | [R-NN] | concedes too much | [name the reviewer move or pressure that will cause over-concession] |
| F-03 | [R-NN] | too brief | [name the structural reason this concern gets under-addressed — buried, overlap, deferred] |

When writing Phase 5: flag each exchange whose R-ID matches a forecast row. The flag
appears in the exchange header and keeps the prediction visible during drafting.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange (Violation: see RULE-8 consequence above). Write in severity
order:

--- P1 CONCERNS (RULE-1 applies — inertia must be overcome with evidence) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. If the R-ID appears in the Phase 4 forecast, add the
forecast flag to the exchange header. Use the type-specific AUTHOR RESPONDS template
(type verified in Phase 3.5 for scope/framing/methodological):

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**
[If R-NN = forecast target: append "| FLAGGED: [F-0N] [predicted failure mode — resist it]"]

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification or fix description.]
                  We have [specific change or explanation] in §N."

  scope:          [2-3 sentences. RULE-3. "This question lies beyond the scope of the present
                  paper, which [state claim space]. We note it as a direction for future work."]

  framing:        "The paper claims [exact manuscript claim]. The reviewer may be reading this
                  as [misread]. We have added [clarifying language] to §N."

  statistical:    "[Added the analysis / explained the constraint.] [Result or rationale.]"

  presentation:   "We have [specific change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale. RULE-1 if P1, RULE-2 always,
RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation**: Compare Phase 2 cover letter against Phase 5 outcomes.
Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 for any shift
in disagreement framing.

**6b. Forecast validation**: Validate FLAGGED exchanges first, then check unflagged exchanges.

FLAGGED exchanges (from Phase 4 forecast rows):
| Forecast | R-ID | Predicted failure | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|------------------|--------|-------------------------------|
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

Unflagged failures: name any quality failure in Phase 5 not predicted in Phase 4.

**6c. Three exchanges to strengthen** (FLAGGED exchanges take priority; add unflagged
failures as needed to reach three):
1. [R-NN] — too defensive: [rewrite AUTHOR RESPONDS opening to remove defensive register]
2. [R-NN] — concedes too much: [what to hold; why the concession went too far]
3. [R-NN] — too brief: [what is understated; what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## Variation Comparison

| Dimension | V-01 (Axis A) | V-02 (Axis B) | V-03 (Axis C) | V-04 (A+B) | V-05 (A+B+C) |
|-----------|--------------|--------------|--------------|-----------|-------------|
| RULE-N block style | RULE-1..8 + violation consequences | RULE-1..8 (standard) | RULE-1..8 (standard) | RULE-1..8 + consequences | RULE-1..8 + consequences |
| Type audit step | None | Phase 3.5 (scope/framing/methodological) | None | Phase 3.5 | Phase 3.5 |
| Forecast row carry-forward | None — forecast stays in Phase 4 | None | Phase 5 header FLAGGED annotation | None | Phase 5 FLAGGED + Phase 6b FLAGGED-first |
| Phase 6b validation | Row-by-row table | Row-by-row table | FLAGGED-first then unflagged | Row-by-row table | FLAGGED-first then unflagged |
| Phases | 6 (standard) | 6 + 3.5 audit | 6 (standard) | 6 + 3.5 audit | 6 + 3.5 audit |
| C-17 (RULE-8 in pre-workflow) | PASS — with consequence | PASS — standard | PASS — standard | PASS — with consequence | PASS — with consequence |
| C-18 (tabular forecast + row-by-row) | PASS — standard table | PASS — standard table | PASS — FLAGGED-first validation is stronger | PASS — standard table | PASS — FLAGGED-first validation is stronger |
| C-19 (per-type AUTHOR RESPONDS) | PASS — standard templates | PASS — audit upstream | PASS — standard templates | PASS — audit upstream | PASS — audit upstream + templates |
| C-06 risk | Low | Very low (audit step) | Low | Very low (audit step) | Minimal (audit upstream + templates downstream) |
| Novel risk | Rules become verbose with 8 consequence clauses | Phase 3.5 adds length; very long review sets may produce verbose audit | FLAGGED header annotation requires tracking forecast R-IDs through Phase 5 | Combined length increase from consequences + audit | Maximum prompt length of all R4 variations |

## Rubric Coverage Check (v4 — 19 criteria)

All five R4 variations cover:

**Essential (C-01–C-05)**: 5/5
- C-01: Phase 3 decomposition table with RULE-5; RULE-8 atomicity enforcement makes merged concerns visibly malformed at Phase 5
- C-02: REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME per R-ID; every concern has a complete three-part exchange
- C-03: RULE-1 (pre-workflow in all five) — names "inertia default," requires OVERCOMES with evidence; P1 tier header reinforces in Phase 5
- C-04: RULE-4 — three strategies named (AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE); type-specific templates model correct register; consequence in V-01/V-04/V-05 adds "professional failure" framing
- C-05: Correct path stated; RULE-6 integer enforcement; consequence in V-01/V-04/V-05

**Recommended (C-06–C-08)**: 3/3
- C-06: Six types with misclassification guide (all five); Phase 3.5 audit in V-02/V-04/V-05 makes >= 80% defensible a near-certainty; type-specific templates in Phase 5 make misclassification visible at exchange
- C-07: Phase 2 cover letter before Phase 3; two paragraphs; Phase 6a reconciliation
- C-08: Phase 6c: three labeled weaknesses (too defensive, concedes too much, too brief) with specific rewrite targets

**Aspirational (C-09–C-19)**: 11/11 target
- C-09: RULE-2 "1 paragraph max, do not over-argue" — explicit in all five (with consequence in V-01/V-04/V-05)
- C-10: RULE-3 "2-3 sentences max, state claim space, close" — explicit in all five
- C-11: RULE-1 names "inertia default" and requires OVERCOMES — explicit in all five before Phase 1
- C-12: Phase 2 cover letter structurally before Phase 3 decomposition and Phase 5 exchange log in all five
- C-13: `--- P1 CONCERNS ---`, `--- P2 CONCERNS ---`, `--- P3 CONCERNS ---` tier headers in Phase 5 of all five
- C-14: Numbered RULE-N block before Phase 1 (RULE-1 through RULE-8) in all five
- C-15: Phase 4 forecast before Phase 5 responses in all five; Phase 6b validates predictions
- C-16: Three-part REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME in Phase 5 of all five
- C-17: RULE-8 declares exchange format in pre-workflow constraints block in all five
- C-18: Tabular forecast (R-ID / failure mode / trigger) + row-by-row validation in Phase 6b in all five; V-03/V-05 strengthen with FLAGGED-first ordering
- C-19: Per-type AUTHOR RESPONDS templates in Phase 5 of all five; V-02/V-04/V-05 upstream audit at Phase 3.5 makes misclassification detectable before templates are reached
