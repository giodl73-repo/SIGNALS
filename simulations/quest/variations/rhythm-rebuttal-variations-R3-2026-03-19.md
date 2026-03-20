## R3 Variations — rhythm-rebuttal

Five complete variations written to `simulations/quest/variations/rhythm-rebuttal-variations-R3-2026-03-19.md`.

**The R3 problem**: Under the new v3 rubric (denominator 8), all R2 variations score below 100. The best R2 combination (V-05) scored 98.75 — missing C-15 (forecast before draft). To hit 100, all three new aspirational criteria must be satisfied simultaneously: C-14 (pre-workflow RULE-N), C-15 (forecast before draft), C-16 (dialogue exchange format).

**Three R3 variation axes:**

| Variation | Axis | Key bet |
|-----------|------|---------|
| **V-01** | Forecast structure: tabular | Forecast table (R-ID / failure mode / trigger) + row-by-row Phase 6 validation makes C-15 specific and falsifiable |
| **V-02** | RULE-N block depth: RULE-8 declares exchange format | C-14 and C-16 share one architectural surface — format is a binding rule, not Phase 5 guidance |
| **V-03** | Exchange enrichment: type-specific templates | Per-type AUTHOR RESPONDS starters + misclassification table closes V-04 R2's persistent C-06 PARTIAL |
| **V-04** | A+B combined | Tabular forecast + RULE-8 |
| **V-05** | A+B+C combined | All axes at maximum — 8/8 aspirational target |

**What changed from R2**: Every R3 variation hits C-14 + C-15 + C-16 together. The R2 best variations each had at most two of the three (V-05 R2 had C-14+C-16 but not C-15). The R3 six-phase structure (`RULE-N → cover letter → decomposition → forecast → exchange log → amend`) is the canonical combination.
fic and row-by-row — stronger evidence of amendment-predictive behavior than V-03 R2's prose forecast
- V-02's RULE-8 is the cleanest C-16 implementation: the format is a binding rule, not formatting guidance

---

## Variation Axes (R3)

Three single axes selected for R3 exploration:

**Axis A — Forecast structure**: The R2 V-03 weakness forecast is three prose predictions. A structured forecast table (R-ID | predicted failure mode | trigger) makes each prediction specific, falsifiable, and cross-referenceable to Phase 6 validation. Tests whether tabular precision strengthens C-15 beyond the R2 baseline.

**Axis B — RULE-N block depth**: R2 V-04 and V-05 front-load RULE-1 through RULE-7. Adding RULE-8 (the exchange format template itself, as a binding rule) means C-14 and C-16 are both satisfied by the same architectural structure — rules block defines the format before any phase starts.

**Axis C — Exchange template enrichment**: V-04 R2 had a persistent C-06 PARTIAL because type descriptions were minimal one-liners. Moving the concern type into the exchange header and providing per-type AUTHOR RESPONDS templates (not just generic AGREE/DISAGREE) ties type classification to response quality, making C-06 defensible by construction.

---

## V-01 — Tabular Forecast

**Axis**: Forecast structure (single axis)
**Hypothesis**: A structured forecast table — R-ID, predicted failure mode, one-sentence trigger — makes each Phase 4 prediction specific and falsifiable. The Phase 6 validation pass becomes row-by-row (ACCURATE / MISSED / OVERSTATED per forecast row), producing a closed calibration loop rather than an impressionistic after-the-fact check. C-15 is strongest when the forecast is precise enough to be wrong.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. This skill is organized around three
architectural properties: binding constraints stated before workflow begins, a structured
weakness forecast before any response is drafted, and a dialogue exchange format that makes
concern merging structurally impossible.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

These rules apply throughout. Violating any one fails the artifact.

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path that requires no additional work from the author. To maintain no-change
on a P1, produce strong scientific evidence that OVERCOMES that inertia. Restating the
original position does not overcome inertia. If the evidence is not compelling, make the
change.

**RULE-2 (No-change brevity rule)**: Any response ending in "No change to manuscript" must
be 1 paragraph max. State the scientific rationale. Do not over-argue. A long no-change
response reads as defensive regardless of content quality.

**RULE-3 (Scope rule)**: Concerns typed as "scope" receive 2-3 sentences in AUTHOR RESPONDS.
Do not argue, explain, or defend the scope boundary. State the paper's claim space and move on.

**RULE-4 (Register rule)**: Every response uses one of three strategies:
AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE. No response is combative, dismissive,
or sycophantic. Professional, non-defensive, grateful throughout.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns from
the same reviewer, even if they appear in the same paragraph.

**RULE-6 (Frontmatter rule)**: All frontmatter values must be integers. No string placeholders.

**RULE-7 (Error rule)**: If no reviewer comments exist, stop and report an error. Do not
invent fictional reviews.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or the reviewer comments provided as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter now — before decomposing individual concerns. This is the commitment
anchor that prevents capitulation drift: commit to the revision strategy before individual
responses can erode it.

**Paragraph 1**: Name the 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none anticipated: state so explicitly.

This cover letter will be updated in Phase 6 to reflect actual exchange outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|
| R-01 | Referee 1 | factual / methodological / scope / framing / statistical / presentation | [1-sentence summary] | P1/P2/P3 |

Types (assign exactly one):
- **factual**: error in the paper — data mistake, wrong citation, calculation error; correct
  directly with evidence
- **methodological**: existing experiment or analysis is flawed — fix or justify with scientific
  reasoning; distinguish from scope (reviewer wants new experiments) vs methodological (existing
  experiments are questioned)
- **scope**: request for work outside this paper's claim space — RULE-3 applies; use when
  reviewer wants a new experiment or domain extension, not when current methods are criticized
- **framing**: misread of what the paper claims — clarify the claim without adding evidence;
  both framing and scope are no-change candidates but for different reasons
- **statistical**: missing or incorrect analysis — add it or explain the constraint preventing it
- **presentation**: clarity, structure, notation, or language issue — fix in revision

Severity:
- **P1**: blocks acceptance — RULE-1 applies; inertia of no-change must be overcome
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note

Sort table: P1 first, then P2, then P3. Within tier, preserve reviewer order.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any response, produce a structured forecast. Be specific — a generic
prediction ("P1 concerns are hard") does not count as a valid forecast entry.

| Forecast | R-ID | Predicted failure mode | Why this concern, not another |
|----------|------|------------------------|-------------------------------|
| F-01 | [R-NN] | too defensive | [1 sentence: what about this concern invites over-explanation or combative register?] |
| F-02 | [R-NN] | concedes too much | [1 sentence: reviewer is partly right but overreaching, or concern is emotionally pressuring] |
| F-03 | [R-NN] | too brief | [1 sentence: buried in longer comment, overlaps stronger concern, requires analysis the author may skip] |

Hold this forecast table while drafting Phase 5. Phase 6b validates each row.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Write exchanges in sorted order, grouped by severity tier:

--- P1 CONCERNS (RULE-1 applies — inertia must be overcome with evidence) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange:

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**

**REVIEWER SAID:**
> "[exact quote or paraphrase of the concern]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
[1-3 paragraphs. Apply RULE-4.
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N to make this clear."]

**MANUSCRIPT OUTCOME:**
[Section and specific change made.]
Or: No change — [rationale. Apply RULE-1 if P1, RULE-2 always, RULE-3 if scope.]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation**: Compare the Phase 2 cover letter against Phase 5
exchange outcomes. Update Paragraph 1 to reflect changes actually made. Update Paragraph 2
if anticipated disagreements changed during drafting.

**6b. Forecast validation**: For each Phase 4 forecast row, check whether the predicted
failure mode materialized in Phase 5:

| Forecast | R-ID | Predicted | Actual | ACCURATE / MISSED / OVERSTATED |
|----------|------|-----------|--------|-------------------------------|
| F-01 | | too defensive | | |
| F-02 | | concedes too much | | |
| F-03 | | too brief | | |

Name any quality failure in Phase 5 that was NOT predicted in Phase 4.

**6c. Three exchanges to strengthen** (may be F-01/F-02/F-03 targets or new):
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

## V-02 — Exchange Format in RULE-N Block

**Axis**: RULE-N block depth (single axis)
**Hypothesis**: Declaring the dialogue exchange template as RULE-8 — a binding constraint in the pre-workflow block, not formatting guidance in Phase 5 — means C-14 and C-16 are satisfied by the same architectural structure. A format rule embedded mid-skill is encountered after generation begins; a format rule in the constraints block is encountered before the first character is written. This makes the three-part template structurally non-optional from the start.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding constraints — including the
required exchange format — are declared before any work begins. A format that is a rule
cannot be forgotten mid-workflow.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path requiring no additional author work. To maintain no-change on a P1,
produce scientific evidence that OVERCOMES that inertia. Restating the original position
does not overcome inertia. If the evidence is not compelling, make the change.

**RULE-2 (No-change brevity rule)**: Any no-change outcome must state the rationale in
1 paragraph max. Do not over-argue. A long no-change reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns get 2-3 sentences in AUTHOR RESPONDS. Do not
argue or defend the scope boundary. State the paper's claim space and close.

**RULE-4 (Register rule)**: Every AUTHOR RESPONDS uses exactly one of:
AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE. No response is combative, dismissive,
or sycophantic. Professional, non-defensive, grateful throughout.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same paragraph of a reviewer's comments.

**RULE-6 (Frontmatter rule)**: All frontmatter values must be integers. No string placeholders.

**RULE-7 (Error rule)**: If no reviewer comments exist, stop and report a clear error.
Do not invent fictional reviews.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must follow this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

  This is not optional formatting. RULE-5 and RULE-8 together: one exchange per concern.
  A merged concern cannot produce a valid REVIEWER SAID block. Violating either rule
  fails the artifact.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments provided as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter before decomposing individual concerns. Commitment anchor: naming
the revision strategy before individual responses prevents capitulation drift.

**Paragraph 1**: Name the 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before writing any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If no anticipated disagreements: state so explicitly.

This cover letter will be reconciled against actual exchange outcomes in Phase 6.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Types (assign exactly one):
- **factual**: data error, wrong citation, calculation mistake in the paper — correct with evidence
- **methodological**: existing experiment or analysis is flawed — fix or justify the design;
  not "we need more experiments" (scope) but "the existing experiment is wrong"
- **scope**: work outside this paper's claim space — RULE-3 applies; use when reviewer wants
  new experiments or domain extensions
- **framing**: misread of what the paper claims — clarify without adding new evidence; the
  reviewer has the wrong mental model of the paper's claims
- **statistical**: missing or incorrect analysis — add it or explain the constraint preventing it
- **presentation**: clarity, structure, notation, or language — fix in revision

Severity:
- **P1**: blocks acceptance — RULE-1 applies; "no change" must overcome inertia
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

Sort table: P1 first, then P2, then P3. Within tier, preserve reviewer order.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, scan the decomposition table. Predict where the draft will
fail. Name exactly three concerns most likely to produce quality failures:

1. **Most likely to produce a defensive response**: [R-ID] — because [specific reason: what
   makes this concern trigger over-explanation or emotional register in the AUTHOR RESPONDS?]
2. **Most likely to produce over-concession**: [R-ID] — because [specific reason: reviewer
   is partly right but overreaching, or the concern is emotionally pressuring]
3. **Most likely to be under-addressed**: [R-ID] — because [specific reason: buried in a
   longer review, overlaps a stronger concern, or requires analysis the author may skip]

Hold this forecast while drafting Phase 5. Phase 6b validates the predictions.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies — inertia must be overcome) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
[1-3 paragraphs. Apply RULE-4.
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N."]

**MANUSCRIPT OUTCOME:**
[Section and specific change. Or: No change — [rationale. Apply RULE-1 if P1, RULE-2
always, RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation**: Compare Phase 2 cover letter against Phase 5 exchange
outcomes. Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 if
anticipated disagreements changed during drafting.

**6b. Forecast validation**: For each Phase 4 prediction: did the predicted failure mode
materialize in Phase 5? Note ACCURATE / MISSED / OVERSTATED for each. Name any failure
that occurred in Phase 5 that was not predicted in Phase 4.

**6c. Three exchanges to strengthen** (may overlap Phase 4 predictions or name new targets):
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

## V-03 — Type-Specific Exchange Guide

**Axis**: Exchange template enrichment (single axis)
**Hypothesis**: Including the concern type in the exchange header and providing per-type AUTHOR RESPONDS templates — not just generic AGREE/DISAGREE starters — ties type classification to response quality by construction. The type assigned in Phase 3 directly gates the response strategy used in Phase 5. This closes V-04 R2's persistent C-06 PARTIAL (minimal type descriptions, >20% misclassification risk) and makes C-06 defensible at every exchange rather than only in the decomposition table.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter as a structured exchange log. The concern
type assigned during decomposition directly determines the response strategy used in the
exchange. Classification and response quality are coupled: assigning the wrong type produces
a visibly wrong response.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default. To maintain it, produce evidence that OVERCOMES that inertia. Restating the original
position does not overcome inertia. If the evidence is not compelling, make the change.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue. A long no-change reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Close.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
No response is combative, dismissive, or sycophantic.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter before decomposing individual concerns. This commits the revision
narrative before individual exchanges can erode it.

**Paragraph 1**: Name the 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none anticipated: "All reviewer concerns have been addressed with manuscript changes."

This cover letter will be reconciled in Phase 6.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — the type assigned here determines the AUTHOR RESPONDS strategy
in Phase 5. Assign exactly one:

| Type | When to use | Common misclassification |
|------|-------------|--------------------------|
| factual | Data error, wrong citation, calculation mistake in the manuscript | Not "framing" — factual is an error in the paper, not a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | Not "scope" — methodological challenges the current work; scope asks for new work |
| scope | Reviewer requests new experiments or domain extensions beyond this paper's claims | Not "methodological" — scope means the paper doesn't claim to address this; methodological means it tried but did it wrong |
| framing | Reviewer misread what the paper claims — the claim is correct, the reviewer has the wrong model | Not "factual" — framing is the reviewer's misread; factual is an error in the paper |
| statistical | Missing or incorrect analysis that the paper should include | Not "methodological" — statistical is about the analysis layer; methodological is about the experimental design |
| presentation | Clarity, structure, notation, or language issue | Safe default for concerns that don't affect scientific content |

Severity:
- **P1**: blocks acceptance — RULE-1 applies; inertia of no-change must be overcome
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note briefly

Sort table: P1 first, then P2, then P3. Within tier, preserve reviewer order.

---

## PHASE 4 -- WEAKNESS FORECAST

Scan the decomposition table. Before writing any exchange, name exactly three concerns
most likely to produce quality failures:

1. **Most likely to produce a defensive response**: [R-ID] — [why: what about this concern
   invites over-explanation or emotional register in AUTHOR RESPONDS?]
2. **Most likely to produce over-concession**: [R-ID] — [why: reviewer is partly right but
   overreaching, or the concern emotionally pressures the author to give more than warranted]
3. **Most likely to be under-addressed**: [R-ID] — [why: buried in a longer comment, overlaps
   a stronger concern, involves analysis the author may be tempted to defer]

Hold while drafting Phase 5. Phase 6b validates these predictions.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Write exchanges in sorted order. Severity tier headers:

--- P1 CONCERNS (RULE-1 applies — inertia must be overcome with evidence) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange. AUTHOR RESPONDS uses the type-specific strategy
from Phase 3:

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  If type = factual:
    "The reviewer is correct. [State corrected data or source.] We have updated [specific
    location] in the revised manuscript."

  If type = methodological:
    "We agree that [aspect of the concern]. [Scientific justification for current design or
    description of the fix.] We have [specific change or added explanation] in §N."

  If type = scope:
    [2-3 sentences. RULE-3. "This question lies beyond the scope of the present paper,
    which [state the claim space]. We note it as a direction for future work."]

  If type = framing:
    "The paper claims [exact claim from manuscript]. The reviewer may be reading this as
    [the misread]. We have added [clarifying language] to §N to make the claim explicit."

  If type = statistical:
    "[Added the analysis / explained the constraint preventing it.] [State result or
    rationale in 1-2 sentences.]"

  If type = presentation:
    "We have [specific editorial change] in the revised manuscript."

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale. Apply RULE-1 if P1, RULE-2
always, RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation**: Compare Phase 2 cover letter against Phase 5 outcomes.
Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 for any shift
in disagreement framing.

**6b. Forecast validation**: For each Phase 4 prediction: did it materialize in Phase 5?
Note ACCURATE / MISSED / OVERSTATED for each. Name any unpredicted failures.

**6c. Three exchanges to strengthen**:
1. [R-NN] — too defensive: [rewrite AUTHOR RESPONDS opening]
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

## V-04 — Tabular Forecast + Exchange Format in RULE-N

**Axes**: Forecast structure (A) + RULE-N block depth (B) combined
**Hypothesis**: A structured forecast table makes Phase 4 predictions falsifiable; declaring the exchange format as RULE-8 makes Phase 5 format non-optional. Together, A+B means the forecast table rows map directly to exchange identifiers in Phase 5, and the Phase 6 validation pass has both a structured forecast to check (A) and a format rule to confirm was followed (B). C-15 and C-16 are each maximally explicit without requiring a six-type response guide (which arrives in V-05).

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. Constraints come first. The exchange
format is a binding rule. The weakness forecast is a structured table — specific, falsifiable,
row-by-row. The amendment pass validates predictions, not just observes.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" on a P1 concern is the inertia
default — the path that requires no additional work from the author. To maintain no-change
on a P1, produce scientific evidence that OVERCOMES that inertia. Restating the original
position does not overcome inertia. If the evidence is not compelling, make the change.

**RULE-2 (No-change brevity rule)**: Any no-change outcome: 1 paragraph max. State the
scientific rationale. Do not over-argue. A long no-change reads as defensive.

**RULE-3 (Scope rule)**: Scope concerns: AUTHOR RESPONDS in 2-3 sentences max. State the
paper's claim space. Do not argue or defend. Move on.

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
No response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same paragraph of a reviewer's comments.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this exact
three-part structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [1-3 paragraphs]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

  RULE-5 and RULE-8 together: one exchange per concern. A merged concern cannot produce
  a valid REVIEWER SAID block. Both rules must be satisfied per exchange.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter before decomposing individual concerns. Commitment anchor: naming
the revision strategy before individual responses prevents capitulation drift.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: state so explicitly.

Updated in Phase 6a.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Types (assign exactly one):
- **factual**: data error, wrong citation, calculation mistake — correct directly with evidence;
  distinguish from framing (reviewer's misread) vs factual (error in the paper itself)
- **methodological**: existing experiment or analysis design is flawed — fix or justify;
  distinguish from scope (wants new experiments) vs methodological (existing ones are wrong)
- **scope**: request for new work outside this paper's claims — RULE-3 applies; brief decline
- **framing**: misread of the paper's claims — clarify without adding evidence
- **statistical**: missing or incorrect analysis — add it or explain the constraint
- **presentation**: clarity, structure, notation, language — fix in revision

Severity:
- **P1**: blocks acceptance — RULE-1 applies; "no change" is the inertia to overcome
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note

Sort: P1 first, P2 second, P3 third. Within tier, preserve reviewer order.

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any exchange, produce a structured failure forecast. Be specific — generic
predictions ("P1 concerns are hard") do not count.

| Forecast | R-ID | Predicted failure mode | Trigger |
|----------|------|------------------------|---------|
| F-01 | [R-NN] | too defensive | [1 sentence: what makes this concern invite over-explanation?] |
| F-02 | [R-NN] | concedes too much | [1 sentence: why would the draft over-concede here?] |
| F-03 | [R-NN] | too brief | [1 sentence: why might this concern be under-addressed?] |

Hold this forecast table while drafting Phase 5. Phase 6b validates each row.

---

## PHASE 5 -- EXCHANGE LOG (SEVERITY ORDER)

Apply RULE-8 to every exchange. Write in severity order:

--- P1 CONCERNS (RULE-1 applies — inertia must be overcome) ---
--- P2 CONCERNS (address or explain) ---
--- P3 CONCERNS ---

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
[1-3 paragraphs. Apply RULE-4.
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N."]

**MANUSCRIPT OUTCOME:**
[Section + specific change. Or: No change — [rationale. RULE-1 if P1, RULE-2 always,
RULE-3 if scope.]]
---

---

## PHASE 6 -- AMEND

**6a. Cover letter reconciliation**: Compare Phase 2 cover letter against Phase 5 outcomes.
Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 if anticipated
disagreements changed during drafting.

**6b. Forecast validation**: For each Phase 4 forecast row, check whether the predicted
failure mode materialized in Phase 5:

| Forecast | Predicted failure | ACCURATE / MISSED / OVERSTATED |
|----------|------------------|-------------------------------|
| F-01 | too defensive | |
| F-02 | concedes too much | |
| F-03 | too brief | |

Name any quality failure in Phase 5 that was not predicted in Phase 4.

**6c. Three exchanges to strengthen** (may match forecast rows or name new targets):
1. [R-NN] — too defensive: [rewrite AUTHOR RESPONDS opening]
2. [R-NN] — concedes too much: [what to hold; why]
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

**Axes**: Tabular forecast (A) + exchange format in RULE-N block (B) + type-specific exchange guide (C) combined
**Hypothesis**: All three new R3 axes at maximum explicit coverage: RULE-8 declares the exchange format as a binding constraint; the forecast is a structured table with row-by-row Phase 6 validation; AUTHOR RESPONDS uses per-type templates so type assignment in Phase 3 directly produces the correct response structure in Phase 5. Every new aspirational criterion (C-14, C-15, C-16) is hit at maximum signal strength. All eight aspirational criteria (C-09 through C-16) should pass.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. All binding rules — including the required
exchange format — are declared before any work begins. The weakness forecast is a structured
table with row-by-row validation. Each exchange uses a type-specific response strategy so
classification quality is visible in the output, not just in the decomposition table.

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

**RULE-4 (Register rule)**: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE only.
No response is combative, dismissive, or sycophantic. Professional, non-defensive, grateful.

**RULE-5 (Decomposition rule)**: One concern = one exchange. Do not merge two concerns,
even if they appear in the same paragraph of a reviewer's comments.

**RULE-6 (Frontmatter rule)**: All frontmatter values are integers. No string placeholders.

**RULE-7 (Error rule)**: No reviewer comments = stop and report error. Do not invent reviews.

**RULE-8 (Exchange format rule)**: Every response block in Phase 5 must use this three-part
structure:

  REVIEWER SAID: [exact quote or paraphrase of the concern]
  AUTHOR RESPONDS [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]: [type-specific response]
  MANUSCRIPT OUTCOME: [specific section + change] or [No change — rationale]

  RULE-5 and RULE-8 together: one exchange per concern. A merged concern cannot produce a
  valid REVIEWER SAID block. The type assigned in Phase 3 determines the AUTHOR RESPONDS
  strategy — see Phase 5 for the type-specific templates.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or reviewer comments as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter before decomposing or responding to any concern. Commitment anchor:
commit to the revision narrative before the drafting process can erode it.

**Paragraph 1**: Name 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before drafting any exchange.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none: "All reviewer concerns have been addressed with manuscript changes."

Updated in Phase 6a to reflect actual outcomes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. Apply RULE-5. The type assigned here directly gates the
AUTHOR RESPONDS strategy in Phase 5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Type assignment guide — assign exactly one:

| Type | When to use | Common misclassification to avoid |
|------|-------------|-----------------------------------|
| factual | Data error, wrong citation, calculation mistake in the paper | "Framing" — factual is an error in the paper; framing is a misread by the reviewer |
| methodological | Existing experiment or analysis design is flawed | "Scope" — methodological = current work is wrong; scope = reviewer wants new work |
| scope | Reviewer requests new experiments or domain extensions | "Methodological" — scope = the paper doesn't claim this; methodological = it tried and failed |
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
only — generic statements do not count.

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

For each R-ID, write one exchange. Use the type-specific AUTHOR RESPONDS template:

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**

**REVIEWER SAID:**
> "[exact quote or paraphrase]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:

  factual:        "The reviewer is correct. [Corrected data or source.] We have updated
                  [specific location] in the revised manuscript."

  methodological: "We agree that [aspect]. [Scientific justification for current design or
                  description of fix.] We have [specific change or explanation] in §N."

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

## Variation Comparison

| Dimension | V-01 (Axis A) | V-02 (Axis B) | V-03 (Axis C) | V-04 (A+B) | V-05 (A+B+C) |
|-----------|--------------|--------------|--------------|-----------|-------------|
| Forecast format | Tabular (F-01/F-02/F-03 table) | Prose (3 labeled predictions) | Prose (3 labeled predictions) | Tabular | Tabular |
| Phase 6 forecast check | Row-by-row validation table | ACCURATE/MISSED/OVERSTATED prose | ACCURATE/MISSED/OVERSTATED prose | Row-by-row table | Row-by-row table |
| Exchange format declared | Phase 5 (mid-workflow) | RULE-8 (pre-workflow) | Phase 5 (mid-workflow) | RULE-8 | RULE-8 |
| AUTHOR RESPONDS templates | Generic (AGREE/DISAGREE starters) | Generic | Type-specific (6 templates) | Generic | Type-specific |
| Type disambiguation guidance | Brief (2-line per type + one distinguishing note) | Brief | Full table (when-to-use + common misclassification) | Brief + one distinguishing note | Full table |
| C-14 (pre-workflow RULE-N) | PASS (RULE-1 through RULE-7) | PASS (RULE-1 through RULE-8) | PASS (RULE-1 through RULE-7) | PASS | PASS |
| C-15 (forecast before draft) | PASS — tabular, row-by-row | PASS — prose, named predictions | PASS — prose, named predictions | PASS — tabular | PASS — tabular |
| C-16 (dialogue exchange format) | PASS — Phase 5 exchange log | PASS — RULE-8 + Phase 5 | PASS — Phase 5 exchange log | PASS — RULE-8 + Phase 5 | PASS — RULE-8 + Phase 5 |
| C-06 risk | Low (disambiguation note per type) | Low | Very low (misclassification table) | Low | Very low |

## Rubric Coverage Check (v3 — 16 criteria)

All five R3 variations cover:

**Essential (C-01–C-05)**: 5/5
- C-01: Full 5-column decomposition table; RULE-5 prohibits merging; dialogue format enforces atomicity in Phase 5
- C-02: Every concern has REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME per R-ID
- C-03: RULE-1 (pre-workflow in all five) — "no change" is inertia; must OVERCOME with evidence; P1 tier header reinforces
- C-04: RULE-4 — three strategies named; register explicitly specified; templates provided
- C-05: Correct path; RULE-6 — all frontmatter values are integers, no string placeholders

**Recommended (C-06–C-08)**: 3/3
- C-06: Six types with disambiguation notes (V-01, V-02, V-04: brief notes; V-03, V-05: full misclassification table)
- C-07: Phase 2 cover letter before Phase 3 decomposition; two paragraphs; Phase 6a reconciliation
- C-08: Phase 6c: three labeled weakness types (too defensive, concedes too much, too brief) with specific rewrite targets

**Aspirational (C-09–C-16)**: 8/8 target
- C-09: RULE-2 states "1 paragraph max, do not over-argue" — explicit in all five
- C-10: RULE-3 states "2-3 sentences max, state claim space, close" — explicit in all five
- C-11: RULE-1 names "inertia default" and requires OVERCOMES — explicit in all five before Phase 1
- C-12: Phase 2 cover letter structurally before Phase 3 and Phase 5 in all five
- C-13: Severity tier headers (--- P1 CONCERNS ---, etc.) in Phase 5 exchange log of all five
- C-14: Numbered RULE-N block before Phase 1 in all five (RULE-1 through RULE-7 minimum)
- C-15: Phase 4 weakness forecast before Phase 5 responses in all five; Phase 6b validates predictions
- C-16: Three-part REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME in Phase 5 of all five
