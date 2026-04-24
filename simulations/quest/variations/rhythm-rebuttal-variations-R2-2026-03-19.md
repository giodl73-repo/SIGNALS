Written to `simulations/quest/variations/rhythm-rebuttal-variations-R2-2026-03-19.md`.

---

## R2 Variations — Summary

Five complete variations, all locking in C-11 + C-12 + C-13 + tightened C-09:

| Variation | Axis | New terrain vs R1 |
|-----------|------|-------------------|
| **V-01** | Inertia framing prominence | Inertia named in preamble + tier headers + per-tier rules — not just a single rules block |
| **V-02** | Output format: dialogue exchange | REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME — makes concern boundaries structurally uncollapsible |
| **V-03** | Role sequence: amendment-predictive | Weakness forecast (Phase 4) runs before response drafting (Phase 5) — self-monitoring frame |
| **V-04** | Lifecycle emphasis: constraint-first | All binding rules (RULE-1 through RULE-7) appear before Phase 1 — none can be missed mid-workflow |
| **V-05** | Combined (V-01 + V-02 + V-04) | Pre-workflow constraints + dialogue format + inertia in tier headers and exchange rules |

**Key bets for the scorecard:**
- V-04 and V-05 are the strongest C-11 candidates — RULE-1 names inertia explicitly before any generation begins
- V-03's amendment-predictive phase is the novel structural risk — C-08 may score higher (forecast accuracy check) or lower (six-phase skill adds complexity) depending on scorer interpretation
- V-02's dialogue format is the sharpest test of C-01/C-02 compliance — the exchange structure makes merged concerns immediately visible
fore any workflow phase so constraints are in active context throughout generation — eliminates mid-workflow rule blindness |
| **V-05** | Combined (V-01 + V-02 + V-04) | Inertia prominence + dialogue format + constraint-first together: each axis reinforces the others and all three new aspirational criteria are hit with maximum explicit coverage |

---

## V-01 — Inertia Framing Prominence

**Axis**: Inertia framing
**Hypothesis**: Naming "no change to manuscript" as the status-quo competitor from the opening preamble through every severity tier header — not just a rules section — embeds the inertia-resistance frame into the author's mental model before any writing begins, producing better P1 responses and more honest no-change rationales.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. This skill is built around a single
organizing principle: every response to a reviewer comment has exactly two outcomes —
the manuscript changes, or it does not. "No change" is the path of least resistance.
The skill is designed to resist that inertia for concerns that warrant it.

The goal is not to make every change. The goal is to EARN every non-change with evidence,
and to OVERCOME the inertia of non-change when the evidence requires it.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or the reviewer comments provided as input.
Read: the original paper or draft if available.
If no reviewer comments exist: stop and report an error. Do not invent fictional reviews.

---

## PHASE 2 -- STRATEGIC COMMITMENT (COVER LETTER FIRST)

Before decomposing individual concerns, commit to the revision strategy. This commitment
anchors all responses that follow and prevents capitulation drift — the tendency for early
responses to weaken your position on later ones.

**Paragraph 1**: Based on a first scan of the reviewer comments, name the 3-4 changes
this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Identify where you will respectfully disagree BEFORE writing any response.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If no anticipated disagreements: "All reviewer concerns have been addressed with manuscript
changes."

This cover letter will be reconciled against actual responses in Phase 5.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. One concern = one R-ID. Do not merge concerns from the
same reviewer, even if they appear in the same paragraph.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|
| R-01 | Referee 1 | factual / methodological / scope / framing / statistical / presentation | [1-sentence summary] | P1/P2/P3 |

Sort: P1 first, then P2, then P3. Within each tier, preserve reviewer order.

Types:
- **factual**: error in paper — correct directly with evidence
- **methodological**: design or execution flaw — fix or justify with evidence
- **scope**: request for work beyond this paper's claim space — brief non-defensive decline
- **framing**: misread of what the paper claims — clarify the framing
- **statistical**: missing analysis — add it or explain the constraint
- **presentation**: clarity or structure issue — fix in revision

Severity (inertia stakes per tier):
- **P1**: blocks acceptance — the inertia of "no change" must be actively overcome
- **P2**: strengthens the paper — address or provide rationale
- **P3**: editorial — fix or note briefly

---

## PHASE 4 -- RESPONSE LETTER (SEVERITY ORDER)

Write responses in sorted order. Open each severity tier with a named inertia header:

--- P1 CONCERNS — inertia must be overcome with evidence ---
--- P2 CONCERNS — address or explain ---
--- P3 CONCERNS ---

For each R-ID, produce a response block:

**R-[NN]: [Reviewer N] -- [concern summary]**

*Reviewer comment*: "[exact quote or paraphrase]"

*Response* [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
[1-3 paragraphs. Register: professional, non-defensive, grateful.
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N to make this clear."]

*Manuscript changes*: [Section + what was added/removed.]
Or: *No change to manuscript* — [rationale, 1 paragraph max, clear scientific basis]

Inertia rules — applied per tier:

P1 no-change: "No change to manuscript" is the default inertia for P1 concerns — the path
that requires no additional work. To maintain no-change on a P1, you must OVERCOME that
inertia with positive evidence, not merely restate the original position. If the evidence
is not compelling, make the change.

Scope no-change: Scope concerns already have the correct answer — no change. Keep the
response 2-3 sentences. Do not explain, defend, or justify the scope boundary. State the
paper's claim space and move on. Over-arguing a scope decision is itself inertia resistance
in the wrong direction.

All no-change responses: 1 paragraph max. State the scientific rationale clearly. Do not
over-argue — a long no-change response reads as defensive regardless of content quality.

---

## PHASE 5 -- AMEND

**5a. Cover letter reconciliation**: Compare the Phase 2 cover letter against actual Phase 4
responses. Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 if the
disagreement framing shifted during drafting.

**5b. Weakness flags** — name three responses that need strengthening:
1. [R-ID] — too defensive: [rewrite opening sentence to remove defensive register]
2. [R-ID] — concedes too much: [identify what was given up unnecessarily; what to hold]
3. [R-ID] — too brief: [name what is understated; what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
All frontmatter values must be integers. No string placeholders.
```

---

## V-02 — Dialogue Exchange Format

**Axis**: Output format
**Hypothesis**: Formatting each response as a numbered dialogue exchange (REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME) makes the letter's structure more legible to editors, prevents merged concerns by treating each exchange as a discrete conversational unit, and makes the severity-tier partitioning feel natural rather than imposed.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter as a structured exchange log.
Each concern is handled as one numbered exchange: the reviewer's position, the author's
response, and the manuscript outcome. Exchanges are grouped by severity so P1 concerns
cannot be buried beneath editorial notes.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or the reviewer comments provided as input.
Read: the original paper or draft if available.
If no reviewer comments exist: stop and report an error. Do not invent fictional reviews.

---

## PHASE 2 -- COVER LETTER (COMMITMENT ANCHOR)

Write the cover letter before decomposing individual concerns. This is the commitment anchor:
naming the revision strategy before individual responses are written prevents capitulation
drift where one difficult response weakens all subsequent positions.

**Paragraph 1**: Name the 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement upfront — before they can be eroded
by the drafting process.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If no anticipated disagreements: state so explicitly.

This cover letter will be updated in Phase 5 to reflect actual responses.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern as an exchange entry. One exchange = one concern. Do not merge
two concerns from the same reviewer even if they appear in the same paragraph.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Types (assign exactly one):
- **factual**: error in paper — correct directly with evidence
- **methodological**: design or execution flaw — fix or justify
- **scope**: request for work outside this paper's claim space — brief, non-defensive decline
- **framing**: misread of the paper's claims — clarify
- **statistical**: missing analysis — add or explain the constraint
- **presentation**: clarity or structure issue — fix in revision

Severity:
- **P1**: acceptance-blocking — manuscript change required; "no change" must overcome inertia
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note

Sort table: P1 first, then P2, then P3. Within each tier, preserve reviewer order.

---

## PHASE 4 -- EXCHANGE LOG (SEVERITY ORDER)

Write exchanges in sorted order, grouped by severity tier:

--- P1 CONCERNS (manuscript changes required) ---
--- P2 CONCERNS (clarification or minor revision) ---
--- P3 CONCERNS ---

For each R-ID, write one exchange:

---
**Exchange [R-NN] | [P1/P2/P3] | [Reviewer N] | [Type] | [concern summary]**

**REVIEWER SAID:**
> "[exact quote or paraphrase of the concern]"

**AUTHOR RESPONDS** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
[1-3 paragraphs. Register: professional, non-defensive, grateful.
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N to make this clear."]

**MANUSCRIPT OUTCOME:**
[Section and specific change. Or: "No change — [1 paragraph scientific rationale]."]
---

Exchange rules:
- P1 exchanges: "no change" requires overcoming inertia with positive evidence — not
  restating the original position. If you cannot produce compelling scientific justification,
  make the change.
- Scope exchanges: AUTHOR RESPONDS must be 2-3 sentences max. Do not argue the scope
  boundary. State the paper's claim space and close.
- No-change outcomes at any severity: 1 paragraph max. State the scientific basis. Do not
  over-argue — a long no-change outcome reads as defensive.

---

## PHASE 5 -- AMEND

**5a. Cover letter check**: Compare the Phase 2 cover letter against the Phase 4 exchange
log. Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 if the
anticipated disagreements changed during drafting.

**5b. Three weak exchanges** to strengthen:
1. [R-NN] — too defensive: [rewrite the AUTHOR RESPONDS opening]
2. [R-NN] — concedes too much: [identify what should be held; rewrite the concession]
3. [R-NN] — too brief: [name what is understated in AUTHOR RESPONDS; what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
All frontmatter values must be integers. No string placeholders.
```

---

## V-03 — Amendment-Predictive Sequence

**Axis**: Role sequence
**Hypothesis**: Predicting which concerns are most likely to produce defensive, over-conceding, or under-addressed responses BEFORE writing any response blocks creates a self-monitoring frame that reduces the most common quality failures — authors who know in advance where they tend to capitulate hold firmer when they reach those concerns.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. This version front-loads a weakness
forecast: before any response is drafted, the author identifies which concerns are most
likely to produce defensive, over-conceding, or insufficient responses. The forecast
disciplines the draft. The amendment pass closes the loop.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or the reviewer comments provided as input.
Read: the original paper or draft if available.
If no reviewer comments exist: stop and report an error. Do not invent fictional reviews.

---

## PHASE 2 -- COVER LETTER (STRATEGIC COMMITMENT)

Write the cover letter first — before decomposing or responding to individual concerns.
This is the commitment anchor that prevents capitulation drift.

**Paragraph 1**: Identify the 3-4 most important changes this revision will make based
on a first scan of the reviewer comments.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name where you will respectfully disagree.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If no disagreements: state explicitly.

This cover letter is a commitment anchor. It will be reconciled against actual responses
in Phase 6.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. One concern = one R-ID. Do not merge.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|
| R-01 | Referee 1 | factual / methodological / scope / framing / statistical / presentation | [1-sentence summary] | P1/P2/P3 |

Sort: P1 first, then P2, then P3. Within each tier, preserve reviewer order.

Types:
- **factual**: error in paper — correct directly with evidence
- **methodological**: design or execution flaw — fix or justify
- **scope**: more-work request — brief non-defensive decline
- **framing**: misread of claim — clarify
- **statistical**: missing analysis — add or explain the constraint
- **presentation**: clarity issue — fix in revision

Severity:
- **P1**: blocks acceptance — manuscript change required; "no change" is the inertia default
  that must be overcome, not merely justified
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note

---

## PHASE 4 -- WEAKNESS FORECAST

Before writing any response, scan the decomposition table and predict where quality will
break down. Name exactly three:

1. **Most likely to produce a defensive response**: [R-ID] — because [reason: disagreement
   with P1 concern, emotionally charged framing, challenges to core methodology]
2. **Most likely to produce over-concession**: [R-ID] — because [reason: reviewer is partly
   right but asking for more than warranted, P2 framed as P1]
3. **Most likely to be under-addressed**: [R-ID] — because [reason: P1 concern buried in a
   list with P3s, scope concern that masks a real methodological gap]

Hold this forecast while drafting Phase 5. The amendment pass in Phase 6 will check whether
the forecast was accurate.

---

## PHASE 5 -- RESPONSE LETTER (SEVERITY ORDER)

Write responses in sorted order. Open each severity tier with a header:

--- P1 CONCERNS (manuscript changes required) ---
--- P2 CONCERNS (clarification or minor revision) ---
--- P3 CONCERNS ---

For each R-ID, produce a response block:

**R-[NN]: [Reviewer N] -- [concern summary]**

*Reviewer comment*: "[exact quote or paraphrase]"

*Response* [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
[1-3 paragraphs. Register: professional, non-defensive, grateful.
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N."]

*Manuscript changes*: [Section + specific change. Or: "No change — [rationale]."]

Rules:
- **P1 no-change**: "No change" is the inertia default for P1 concerns. To maintain it,
  you must OVERCOME that inertia with positive evidence — not merely restate your original
  position. If the evidence is not compelling, make the change.
- **Scope no-change**: Scope concerns already have the correct answer. Keep the response
  2-3 sentences. Do not argue.
- **All no-change responses**: 1 paragraph max. State the scientific rationale. Do not
  over-argue — a long no-change response reads as defensive.

---

## PHASE 6 -- AMEND

**6a. Forecast check**: Did the concerns flagged in Phase 4 produce the predicted failure
modes in Phase 5? Note where the forecast was accurate and where it was not.

**6b. Cover letter reconciliation**: Compare the Phase 2 cover letter against Phase 5
responses. Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 if
the disagreement framing changed during drafting.

**6c. Three responses to strengthen** (may overlap with Phase 4 predictions):
1. [R-ID] — too defensive: [rewrite opening sentence to remove defensive register]
2. [R-ID] — concedes too much: [what to hold; why the concession went too far]
3. [R-ID] — too brief: [what is understated; what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
All frontmatter values must be integers. No string placeholders.
```

---

## V-04 — Constraint-First Register

**Axis**: Lifecycle emphasis
**Hypothesis**: Stating every binding rule before any workflow phase — not embedded mid-skill in rules sections — keeps constraints in active context throughout generation. A model that encounters a P1 no-change rule mid-response may apply it inconsistently; a model that read it before Phase 1 cannot claim it was out of scope.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

These rules apply throughout. Violating any one fails the artifact.

**RULE-1 (P1 inertia rule)**: Every P1 concern must have a non-empty manuscript changes
field. "No change to manuscript" on a P1 concern is the inertia default — the path that
requires no additional work. To maintain it, produce strong scientific evidence that
OVERCOMES that inertia. Restating the original position does not overcome inertia. If the
evidence is not compelling, make the change.

**RULE-2 (No-change brevity rule)**: Any response ending in "No change to manuscript" must
be 1 paragraph max. State the scientific rationale. Do not over-argue. A long no-change
response reads as defensive regardless of content quality.

**RULE-3 (Scope rule)**: Concerns typed as "scope" receive 2-3 sentences max. Do not argue,
explain, or defend the scope boundary. State the paper's claim space and move on.

**RULE-4 (Register rule)**: Every response uses one of three strategies:
AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE. No response is combative, dismissive,
or sycophantic. Professional, non-defensive, grateful throughout.

**RULE-5 (Decomposition rule)**: One concern = one R-ID. Do not merge two concerns from the
same reviewer, even if they appear in the same paragraph of the review.

**RULE-6 (Frontmatter rule)**: All frontmatter values must be integers. No string placeholders.

**RULE-7 (Error rule)**: If no reviewer comments exist, stop and report an error. Do not
invent fictional reviews.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or the reviewer comments provided as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- COVER LETTER (BEFORE DECOMPOSITION)

Write the cover letter now — before decomposing individual concerns. Writing it first is the
commitment anchor that prevents capitulation drift: you commit to a revision strategy before
individual responses can erode it.

**Paragraph 1**: Name the 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If none anticipated: state explicitly.

This cover letter will be updated in Phase 5 if actual responses reveal additional changes.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Build the table. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|
| R-01 | Referee 1 | factual / methodological / scope / framing / statistical / presentation | [1-sentence summary] | P1/P2/P3 |

Sort: P1 first, then P2, then P3. Within each tier, preserve reviewer order.

Types:
- **factual**: error in paper — correct directly (RULE-4 applies)
- **methodological**: design flaw — fix or justify
- **scope**: more-work request — brief decline (RULE-3 applies)
- **framing**: misread of claim — clarify
- **statistical**: missing analysis — add or explain
- **presentation**: clarity issue — fix in revision

Severity:
- **P1**: blocks acceptance (RULE-1 applies)
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note

---

## PHASE 4 -- RESPONSE LETTER (SEVERITY ORDER)

Write responses in sorted order. Open each tier with a header:

--- P1 CONCERNS (manuscript changes required) ---
--- P2 CONCERNS ---
--- P3 CONCERNS ---

For each R-ID, produce a response block:

**R-[NN]: [Reviewer N] -- [concern summary]**

*Reviewer comment*: "[exact quote or paraphrase]"

*Response* [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
[1-3 paragraphs. Apply RULE-4.
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N."]

*Manuscript changes*: [Section + specific change.]
Or: *No change* — [rationale. Apply RULE-1 for P1, RULE-2 for all, RULE-3 for scope.]

---

## PHASE 5 -- AMEND

**5a. Cover letter check**: Compare Phase 2 cover letter against Phase 4 responses. Update
Paragraph 1 to reflect changes actually made. Update Paragraph 2 if anticipated disagreements
changed.

**5b. Three responses to strengthen**:
1. [R-ID] — too defensive: [rewrite opening sentence to remove defensive register]
2. [R-ID] — concedes too much: [what should be held; why the concession went too far]
3. [R-ID] — too brief: [what is understated; what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## V-05 — Combined (Inertia Prominence + Dialogue Format + Constraint-First)

**Axes**: Inertia framing prominence (V-01) + Output format: dialogue exchange (V-02) + Constraint-first register (V-04)
**Hypothesis**: Frontloading constraints ensures no rule is missed; dialogue exchange format makes concern boundaries structurally impossible to merge; inertia framing embedded in constraints, tier headers, and exchange rules produces maximal resistance to capitulation. All three new aspirational criteria (C-11, C-12, C-13) are hit at maximum explicit coverage.

```
You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter as a structured exchange log. Each concern
is one exchange. Exchanges are severity-sorted. Constraints are stated before any work begins.

The organizing principle: "No change to manuscript" is the default position for every concern.
The skill is designed to make sure that default is EARNED on P2/P3 concerns and OVERCOME on
P1 concerns when the evidence requires it.

---

## BINDING CONSTRAINTS (READ BEFORE STARTING)

**RULE-1 (P1 inertia rule)**: "No change to manuscript" is the inertia default for P1
concerns — the path that requires no additional work from the author. To maintain no-change
on a P1, produce positive evidence that OVERCOMES that inertia. Restating the original
position does not count. If the evidence is not compelling, make the change.

**RULE-2 (No-change brevity rule)**: Any exchange ending in "No change" must state the
scientific rationale in 1 paragraph max. Do not over-argue. Over-arguing a no-change
response makes it read as defensive regardless of its content.

**RULE-3 (Scope rule)**: Scope exchanges receive 2-3 sentences max in AUTHOR RESPONDS.
Scope concerns already have the correct answer: no change. Do not argue, explain, or
defend the scope boundary. State the paper's claim space and close.

**RULE-4 (Register rule)**: Every AUTHOR RESPONDS uses one of: AGREE / PARTIALLY AGREE /
RESPECTFULLY DISAGREE. No exchange is combative, dismissive, or sycophantic.

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

## PHASE 2 -- COVER LETTER (COMMITMENT ANCHOR — BEFORE DECOMPOSITION)

Write the cover letter now — before decomposing or responding to individual concerns. This
is the commitment anchor: it commits the author to a revision strategy before the drafting
process can erode it. Authors who write the cover letter last tend to let individual responses
drift toward capitulation; authors who write it first hold firmer.

**Paragraph 1**: Name the 3-4 changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Name areas of respectful disagreement now, before writing individual responses.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
If no anticipated disagreements: "All reviewer concerns have been addressed with manuscript
changes."

This cover letter will be reconciled against actual exchange outcomes in Phase 5.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern as an exchange entry. Apply RULE-5.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|

Types (assign exactly one):
- **factual**: error in paper — correct directly with evidence
- **methodological**: design or execution flaw — fix or justify
- **scope**: request for work outside this paper's claim space — brief decline (RULE-3)
- **framing**: misread of what the paper claims — clarify
- **statistical**: missing analysis — add or explain the constraint
- **presentation**: clarity or structure issue — fix in revision

Severity:
- **P1**: acceptance-blocking — RULE-1 applies; inertia must be overcome
- **P2**: moderate — address or explain
- **P3**: editorial — fix or note

Sort table: P1 first, then P2, then P3. Within each tier, preserve reviewer order.

---

## PHASE 4 -- EXCHANGE LOG (SEVERITY ORDER)

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

## PHASE 5 -- AMEND

**5a. Cover letter reconciliation**: Compare the Phase 2 cover letter against the Phase 4
exchange log. Update Paragraph 1 to reflect changes actually made. Update Paragraph 2 if
the anticipated disagreements changed during drafting. The cover letter must accurately
reflect the revision as delivered, not as planned.

**5b. Three weak exchanges** to strengthen:
1. [R-NN] — too defensive: [rewrite the AUTHOR RESPONDS opening to remove defensive register]
2. [R-NN] — concedes too much: [identify what was given up unnecessarily; what to hold]
3. [R-NN] — too brief: [name what is understated in AUTHOR RESPONDS; what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
Apply RULE-6: all values must be integers.
```

---

## Variation Comparison

| Dimension | R1 Baseline (V-05) | V-01 R2 | V-02 R2 | V-03 R2 | V-04 R2 | V-05 R2 |
|-----------|-------------------|---------|---------|---------|---------|---------|
| C-11 (inertia framing for P1 no-change) | YES — rules section | YES — preamble + tier headers + rules | YES — exchange rules | YES — Phase 3 severity def + Phase 5 rules | YES — RULE-1 before Phase 1 | YES — RULE-1 + tier headers + exchange rules |
| C-12 (cover letter before responses) | YES — Phase 2 | YES — Phase 2 | YES — Phase 2 | YES — Phase 2 | YES — Phase 2 | YES — Phase 2 |
| C-13 (severity tier headers) | YES — Phase 4 | YES — Phase 4 (inertia-labeled) | YES — Phase 4 | YES — Phase 5 | YES — Phase 4 | YES — Phase 4 (RULE-1 annotated) |
| C-09 (no-change brevity, explicit) | YES | YES — named per tier | YES — exchange rule | YES — "1 paragraph max" stated | YES — RULE-2 | YES — RULE-2 |
| C-10 (scope distinctively short) | YES | YES — "2-3 sentences, move on" | YES — "2-3 sentences max" | YES | YES — RULE-3 | YES — RULE-3 |
| Response format | Severity-sorted cards | Block format, severity order | Dialogue exchange (REVIEWER / AUTHOR / OUTCOME) | Block format, severity order | Block format, severity order | Dialogue exchange, RULE-annotated |
| Inertia placement | Single rules block | Preamble + tier headers + rules | Exchange-level rules | Phase 3 severity defs + response rules | RULE-1 (pre-workflow) | RULE-1 + Phase 4 headers + exchange rules |
| Constraint placement | Embedded in phases | Embedded in phases | Embedded in phases | Embedded in phases | **Pre-workflow block** | **Pre-workflow block** |
| Amendment sequencing | Standard | Standard | Standard | **Forecast before draft** (Phase 4 → 5 → 6) | Standard | Standard |
| New axis | — | Inertia prominence | Dialogue format | Amendment-predictive | Constraint-first | Combined (V-01+V-02+V-04) |

## Rubric Coverage Check (v2 — 13 criteria)

All five R2 variations cover:

Essential (C-01 through C-05):
- C-01: Full decomposition table with R-ID / Reviewer / Type / Summary / Severity; no merged concerns
- C-02: Response block per R-ID with reviewer comment, response text, manuscript changes
- C-03: P1 requires manuscript change; "no change" requires explicit strong justification
- C-04: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE with professional register guidance
- C-05: Correct artifact path + integer frontmatter (explicitly enforced)

Recommended (C-06 through C-08):
- C-06: Six types named and differentiated (factual / methodological / scope / framing / statistical / presentation)
- C-07: Two-paragraph cover letter with specified structure
- C-08: Amendment pass naming three weakness types (defensive / concedes-too-much / too-brief)

Aspirational (C-09 through C-13):
- C-09: No-change brevity constraint explicitly stated ("1 paragraph max") — not implied
- C-10: Scope responses distinctively short (2-3 sentences) in all variations
- C-11: P1 "no change" named as inertia to OVERCOME, not merely justify — present in all five
- C-12: Cover letter appears as Phase 2 (before decomposition and responses) in all five
- C-13: Severity tier headers (--- P1 CONCERNS ---, etc.) present in response section of all five
