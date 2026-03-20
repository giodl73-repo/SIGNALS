Written to `simulations/quest/variations/rhythm-rebuttal-variations-R1-2026-03-19.md`.

---

## Summary

5 complete variations generated:

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| **V-01** | Role sequence | Cover letter first — commits to change strategy before writing individual responses, preventing capitulation drift |
| **V-02** | Output format | Severity-sorted concern cards (P1→P2→P3) — P1s cannot be buried beneath minor editorial notes |
| **V-03** | Lifecycle emphasis | Expanded decomposition with per-type strategy guides and misclassification warnings — reduces scope/methodological confusion |
| **V-04** | Phrasing register | Short-sentence imperative register — commands only, no explanatory prose, pushes toward tighter output |
| **V-05** | Combined (3 axes) | Cover-first + severity cards + explicit inertia framing ("no change" named as the competitor for P1s) |

**Key design decisions:**
- V-03 has the most novel structural change — a full decision tree for type classification with a "misclassification risk" callout per type. The scope/methodological confusion is likely the most common failure mode in practice.
- V-05's inertia framing is the most conceptually interesting: explicitly naming "no change to manuscript" as the *default competitor* to overcome for P1s reframes the whole task from "justify changes" to "overcome inertia."
- All 5 variants cover all 10 rubric criteria (C-01 through C-10). Nothing was dropped.
at declared strategy rather than drifting.

---

```
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure

You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. The skill reads reviewer comments
(from validate-referee or pasted actual reviews) and produces a structured, professional
response. Cover letter is authored first to anchor the revision strategy before
individual responses are written.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or the reviewer comments provided as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- STRATEGIC FRAMING (COVER LETTER FIRST)

Before decomposing individual concerns, write the two-paragraph cover letter as a
commitment anchor. This forces you to identify the 3-4 key changes that matter most,
which disciplines every response that follows.

**Paragraph 1**: Identify the 3-4 most important changes this revision will make.
"We thank the referees for their careful reading of [paper title]. In response to
their comments, we have [list 3-4 main changes]. Full point-by-point responses follow."

**Paragraph 2**: Flag areas of respectful disagreement before you have written the
responses. Committing to disagreements upfront prevents capitulation drift.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale].
We have added text to clarify this." (If no disagreements, state so explicitly.)

This cover letter will be revised in Phase 5 if the individual responses reveal
additional changes not anticipated here.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern as a numbered item. One concern = one response.
Do not merge concerns from the same reviewer.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|
| R-01 | Referee 1 | factual / methodological / scope / framing / statistical / presentation | [1-sentence summary] | P1/P2/P3 |

Types:
- **factual**: correct the error directly, cite the evidence
- **methodological**: fix the method or explain why it is adequate
- **scope**: brief, non-defensive — "beyond scope of this paper"
- **framing**: clarify what the paper does and does not claim
- **statistical**: add the analysis or explain the constraint
- **presentation**: acknowledge and fix in revision

Severity:
- **P1**: Major concern — blocks acceptance without direct manuscript change
- **P2**: Moderate concern — addressable with clarification or minor revision
- **P3**: Minor / editorial — fix or acknowledge with brief note

---

## PHASE 4 -- RESPONSE LETTER

For each R-ID in decomposition order, produce a response block:

**R-[NN]: [Reviewer N] -- [concern summary]**

*Reviewer comment*: "[exact quote or paraphrase]"

*Response*:
[1-3 paragraphs. Professional, non-defensive, grateful register.
Strategies:
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise action]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N to make this clear."]

*Manuscript changes*: [Specific change: section, line, what was added/removed.
Or: "No change to manuscript — rationale above." No-change responses must be
concise (1 paragraph max) and state a clear scientific rationale.]

Rule: Every P1 concern must have a manuscript change. "No change" for a P1 requires
explicit, strong scientific justification — not just restating the original claim.

Scope concerns: keep responses to 2-3 sentences. Do not over-argue.

---

## PHASE 5 -- AMEND

Review the full response letter against the cover letter written in Phase 2.

**5a. Cover letter check**: Do the individual responses reveal changes not in the
cover letter? If so, update Paragraph 1 to reflect actual revision scope.

**5b. Weakness identification**: Name three responses that need strengthening:
1. [Response that is too defensive — reads as insecure, over-argues the obvious]
2. [Response that concedes too much — gives away something that should be held]
3. [Response that is too brief — the concern is more serious than the response acknowledges]

For each flagged response: state the failure mode and rewrite the response opening.

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
All frontmatter values must be integers.
```

---

## V-02 — Output Format (Severity-Sorted Concern Cards)

**Axis**: Output format
**Hypothesis**: Sorting concern cards by severity (P1 first, P2 second, P3 last) rather than by reviewer order ensures the highest-stakes concerns receive the most careful treatment and cannot be buried under minor editorial notes.

---

```
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure

You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. Concerns are surfaced and
responded to in severity order (P1 → P2 → P3) rather than reviewer order, ensuring
critical concerns receive maximum attention first. The response letter maps back to
reviewer numbers so editors can navigate it normally.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or the reviewer comments provided as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- CONCERN DECOMPOSITION

Extract every distinct concern. Assign R-ID, reviewer, type, summary, and severity.
One concern = one card. Do not merge concerns.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|
| R-01 | Referee 1 | factual / methodological / scope / framing / statistical / presentation | [1-sentence summary] | P1/P2/P3 |

Sort the table P1 first, then P2, then P3. Within each tier, preserve reviewer order.

Types:
- **factual**: error in the paper — correct directly with evidence
- **methodological**: design or execution issue — fix or justify
- **scope**: request outside paper's claim space — brief, non-defensive dismissal
- **framing**: misread of what the paper claims — clarify the framing
- **statistical**: power, corrections, effect sizes — add analysis or explain constraint
- **presentation**: clarity, structure, labeling — fix in revision

---

## PHASE 3 -- RESPONSE LETTER (SEVERITY ORDER)

Respond in sorted order: all P1 cards first, then P2, then P3.
At the top of each severity tier, write a one-line header:

```
--- P1 CONCERNS (manuscript changes required) ---
--- P2 CONCERNS (clarification or minor revision) ---
--- P3 CONCERNS (editorial or optional) ---
```

For each R-ID, produce a concern card:

---
**[P1 / P2 / P3] R-[NN] | [Reviewer N] | [Type] | [concern summary]**

> *Reviewer comment*: "[exact quote or paraphrase]"

**Response** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
[1-3 paragraphs. Professional, non-defensive, grateful.

  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise action]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N to make this clear."]

**Manuscript changes**: [Specific change: section, paragraph, what was added/removed.]
Or: **No change** — [1 paragraph scientific rationale. No-change responses must not over-argue.]

---

Rules:
- Every P1 card must have a non-empty manuscript changes field.
- "No change" on a P1 requires explicit strong justification in the card.
- Scope cards: 2-3 sentences max. Do not argue the scope decision.

---

## PHASE 4 -- COVER LETTER

Two-paragraph cover letter. Written after responses so it accurately reflects what
was actually changed (not what was planned).

**Paragraph 1**: Thank reviewers. List 3-4 key changes made in this revision.
"We thank the referees for their careful reading of [paper title]. In response to
their comments, we have [list 3-4 main changes]."

**Paragraph 2**: Flag areas of respectful disagreement, or explicitly state there are none.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale].
We have added text to §N to clarify this."

---

## PHASE 5 -- AMEND

Name three specific response cards that need strengthening:
1. [R-ID] — too defensive: [1-sentence rewrite of opening]
2. [R-ID] — concedes too much: [what should be held and why]
3. [R-ID] — too brief: [what the response understates and what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
All frontmatter values must be integers.
```

---

## V-03 — Lifecycle Emphasis (Expanded Decomposition)

**Axis**: Lifecycle emphasis
**Hypothesis**: Expanding Phase 2 with full per-type strategy guides and worked examples reduces type misclassification. Authors who misclassify "scope" as "methodological" write over-long defensive responses; an expanded decomposition phase catches this before the response letter is drafted.

---

```
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure

You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. This version front-loads the
decomposition phase with full type strategy guides. Spend time here — getting the
type right determines the response length, tone, and strategy for every concern that
follows.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or the reviewer comments provided as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- CONCERN DECOMPOSITION (EXPANDED)

This is the critical phase. Extract every distinct concern. Do not merge two concerns
into one row even if they come from the same paragraph of a review. One concern = one R-ID.

Build the decomposition table:

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|
| R-01 | Referee 1 | [see types below] | [1-sentence summary] | P1/P2/P3 |

### Type Classification Guide

Assign exactly one type per concern. Use the decision tree below.

**factual**
- What it looks like: "The paper states X, but X is incorrect." "Your citation says Y but the
  source actually says Z." "Fig. 3 label is wrong."
- Response strategy: Correct the error directly. Cite the evidence. Do not argue.
- Manuscript change: Always required. Fix the error.
- Length: 1 paragraph.
- Misclassification risk: Do not call this "framing" — factual errors need correction, not reframing.

**methodological**
- What it looks like: "The experimental design does not control for X." "The sample size is
  insufficient." "You should have used method Y instead of Z."
- Response strategy: Either fix the method in the revision (AGREE) or explain why the
  existing method is adequate with evidence (RESPECTFULLY DISAGREE).
- Manuscript change: Required for AGREE. For DISAGREE: add clarifying text explaining why.
- Length: 2-3 paragraphs.
- Misclassification risk: Do not call this "scope" — methodological concerns are in-scope
  by definition and require substantive responses.

**scope**
- What it looks like: "The paper should also study X." "Why didn't you include Y population?"
  "Future work should address Z."
- Response strategy: "We agree this is an interesting direction. It is beyond the scope of
  this paper. We have added a note to the limitations section."
- Manuscript change: Optional — add a future work sentence if helpful.
- Length: 2-3 sentences MAX. Do not argue, defend, or over-explain.
- Misclassification risk: The most common error is treating scope concerns as methodological
  and writing 3-paragraph defenses. If the reviewer is asking for MORE work rather than
  questioning existing work, it is scope.

**framing**
- What it looks like: "The paper overclaims." "This finding does not support the conclusion."
  "The abstract says X but the paper shows Y."
- Response strategy: Clarify what the paper does and does not claim. Adjust the framing
  language in the manuscript.
- Manuscript change: Usually required — adjust abstract, introduction, or discussion language.
- Length: 1-2 paragraphs.

**statistical**
- What it looks like: "No power analysis." "Effect sizes not reported." "You need to correct
  for multiple comparisons." "Confidence intervals missing."
- Response strategy: Either add the requested analysis (AGREE) or explain the constraint
  (PARTIALLY AGREE: "We agree in principle; our dataset does not support this test because...").
- Manuscript change: Required if adding analysis. If not: explain and add clarifying text.
- Length: 1-2 paragraphs.

**presentation**
- What it looks like: "Figure 2 is hard to read." "The introduction is too long." "Define
  acronym X on first use." "Numbering is inconsistent."
- Response strategy: Acknowledge and fix. No defense needed.
- Manuscript change: Always fix. "No change" is rarely justified for presentation concerns.
- Length: 1 sentence.

### Severity Assignment

- **P1**: The paper cannot be accepted without directly addressing this concern.
  Includes: factual errors, major methodological flaws, overclaiming conclusions.
- **P2**: The paper would be strengthened by addressing this, but it does not block acceptance.
  Includes: missing analyses, framing improvements, scope additions.
- **P3**: Minor, editorial, or optional.
  Includes: presentation, typos, style, suggested citations.

After building the table, verify: no two rows have identical summaries. If they do, you
have merged two concerns — split them.

---

## PHASE 3 -- RESPONSE LETTER

For each R-ID in table order, produce:

**R-[NN]: [Reviewer N] -- [concern summary]**

*Reviewer comment*: "[exact quote or paraphrase]"

*Response*:
[Follow the strategy for this concern's type. Use one of:
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise action]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N to make this clear."]

*Manuscript changes*: [Section, line or paragraph, what changed. Or: "No change — [rationale]."]

P1 rule: Every P1 concern must state a specific manuscript change. "No change" on a P1
requires an explicit scientific justification, not a restatement of the original claim.

Scope rule: Responses to scope concerns must be 2-3 sentences. If yours exceeds this,
reclassify the concern — it is probably methodological.

---

## PHASE 4 -- COVER LETTER

Two-paragraph cover letter.

**Paragraph 1**: Thank reviewers. Name 3-4 key changes.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Flag respectful disagreements, or state explicitly that there are none.

---

## PHASE 5 -- AMEND

Three responses to strengthen:
1. [R-ID] too defensive — [rewrite opening sentence]
2. [R-ID] concedes too much — [what to hold and why]
3. [R-ID] too brief — [what the response understates]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
All frontmatter values must be integers.
```

---

## V-04 — Phrasing Register (Conversational / Imperative)

**Axis**: Phrasing register
**Hypothesis**: A short-sentence imperative register (commands only, no explanatory prose blocks) reduces model verbosity in the output, pushing it toward tight professional responses rather than over-explained academic hedging.

---

```
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure

You are running /rhythm-rebuttal for: {{topic}}

Task: build the response-to-reviewers letter. Read the reviewer comments. Decompose.
Respond. Write the cover letter. Amend. Five steps — do them in order.

---

## STEP 1 — READ

Read the review artifact from validate-referee, or use the reviewer comments in the input.
Read the paper draft if available.
If no reviewer comments exist: stop and report an error. Do not invent fictional reviews.

---

## STEP 2 — DECOMPOSE

Build a table. One row per concern. Do not merge two concerns.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|
| R-01 | Referee 1 | factual / methodological / scope / framing / statistical / presentation | [1-sentence summary] | P1/P2/P3 |

Type rules:
- factual: error in the paper. Correct it.
- methodological: flaw in design or execution. Fix it or justify it.
- scope: request for more work. Decline briefly. Do not argue.
- framing: misread of the claim. Clarify it.
- statistical: missing analysis. Add it or explain the constraint.
- presentation: clarity issue. Fix it.

Severity rules:
- P1: blocks acceptance. Manuscript change required.
- P2: strengthens the paper. Address or explain.
- P3: minor. Fix or note.

---

## STEP 3 — RESPOND

One block per R-ID.

**R-[NN]: [Reviewer N] -- [concern summary]**
> "[exact quote or paraphrase of the concern]"

Response (pick one): AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE.
Write 1-3 paragraphs. Keep tone: professional, non-defensive, grateful.

- AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
- PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise]."
- RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence]. We have
  added [clarifying text] to §N."

Manuscript changes: [section + what changed]. Or: "No change — [1-paragraph rationale]."

Hard rules:
- P1 concern = manuscript change required. No exceptions without strong scientific justification.
- Scope concern = 2-3 sentences max. Nothing more.
- No-change response = 1 paragraph max. State the scientific reason. Do not over-argue.

---

## STEP 4 — COVER LETTER

Two paragraphs. Short.

Para 1: Thank reviewers. Name 3-4 changes.
Para 2: Flag disagreements. Or say there are none.

---

## STEP 5 — AMEND

Find three weak responses. Name them.

1. Too defensive: [R-ID] — [rewrite the opening sentence]
2. Concedes too much: [R-ID] — [what to hold]
3. Too brief: [R-ID] — [what is understated]

---

Write: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
Frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
All values: integers. No placeholders.
```

---

## V-05 — Combined (Cover-First + Severity Cards + Inertia Framing)

**Axes**: Role sequence (cover letter first) + Output format (severity-keyed concern cards) + Inertia framing (explicit "no change" competitor)
**Hypothesis**: The three axes reinforce each other. Cover-first commits the author to a change strategy before writing responses. Severity cards prevent burying P1s. Inertia framing names "no change to manuscript" as a default bias that must be actively resisted for P1 concerns, reducing capitulation.

---

```
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure

You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. Inertia note: "no change to manuscript"
is the default that does not need to be earned — it is the starting position. Every response
either earns a change (for AGREE/PARTIALLY AGREE) or defends the status quo with evidence
(for RESPECTFULLY DISAGREE). The inertia response is not a valid answer for P1 concerns
without explicit scientific justification.

The cover letter is written first as a strategic commitment anchor. Responses follow in
severity order. The amendment pass closes the loop.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or the reviewer comments provided as input.
Read: the original paper or draft if available.
If no reviewer comments exist: stop and report an error. Do not invent fictional reviews.

---

## PHASE 2 -- STRATEGIC COMMITMENT (COVER LETTER FIRST)

Before you know how any individual concern will be answered, commit to the revision strategy.

**Paragraph 1**: Identify the 3-4 key changes this revision will make based on a first scan
of the reviewer comments. Name them in specific terms.
"We thank the referees for their careful reading of [paper title]. In response to their
comments, we have [list 3-4 main changes]."

**Paragraph 2**: Identify areas where you will respectfully disagree — before writing the
individual responses. This prevents capitulation drift where early responses weaken your
position on later ones.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]."
(If no disagreements anticipated, state: "All reviewer concerns have been addressed with
manuscript changes.")

This cover letter will be checked against actual responses in Phase 5 and updated if needed.

---

## PHASE 3 -- CONCERN DECOMPOSITION

Extract every distinct concern. One concern = one card. Do not merge.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|
| R-01 | Referee 1 | factual / methodological / scope / framing / statistical / presentation | [1-sentence summary] | P1/P2/P3 |

Sort: P1 rows first, then P2, then P3. Preserve reviewer order within each tier.

Types:
- **factual**: error in paper — correct with evidence
- **methodological**: design/execution flaw — fix or justify
- **scope**: request for more work — brief non-defensive decline
- **framing**: misread of claim — clarify framing
- **statistical**: missing analysis — add or explain constraint
- **presentation**: clarity issue — fix in revision

Severity:
- **P1**: blocks acceptance — manuscript change required
- **P2**: moderate — address or explain
- **P3**: minor — fix or note

---

## PHASE 4 -- RESPONSE CARDS (SEVERITY ORDER)

Write responses in sorted order. Open each tier with a header:

```
--- P1 CONCERNS — manuscript changes required ---
--- P2 CONCERNS — clarification or minor revision ---
--- P3 CONCERNS ---
```

For each R-ID, produce a concern card:

---
**[P1/P2/P3] R-[NN] | [Reviewer N] | [Type]**
*[concern summary]*

> *Reviewer comment*: "[exact quote or paraphrase]"

**Response** [AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE]:
[1-3 paragraphs. Professional, non-defensive, grateful.
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning].
    We have added [clarifying text] to §N to make this clear."]

**Manuscript changes**: [Section, paragraph, what was added/removed.]
Or: **No change** — [1 paragraph scientific rationale.]

---

Inertia rules — explicitly:
- "No change" is the DEFAULT position. It does not need to be argued for.
- For P1 concerns, "no change" is the INERTIA competitor you must OVERCOME with evidence.
  If you cannot produce strong scientific justification for no-change on a P1, make the change.
- For scope concerns, "no change" IS the correct answer. Keep the response 2-3 sentences.
  Do not argue the scope decision; simply state the paper's claim space and move on.
- For no-change responses at any level: 1 paragraph max. Clear scientific rationale.
  Do not over-argue — over-arguing a no-change response makes it read as defensive.

---

## PHASE 5 -- AMEND

**5a. Cover letter reconciliation**: Compare the cover letter from Phase 2 to the actual
responses in Phase 4. Update Paragraph 1 to reflect the changes that were actually made.
If the disagreement framing in Paragraph 2 changed, update it.

**5b. Weakness flags**:
1. [R-ID] — too defensive: [rewrite opening sentence to remove defensive register]
2. [R-ID] — concedes too much: [identify what was conceded unnecessarily, what to hold]
3. [R-ID] — too brief: [name what the response understates, what to add]

---

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}},
reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
All frontmatter values must be integers. No string placeholders.
```

---

## Variation Comparison

| Dimension | Original | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| Phase order | Acquire→Decompose→Respond→Cover→Amend | Acquire→**Cover**→Decompose→Respond→Amend | Original + severity sort | Original | Same as original (renamed Steps) | Acquire→**Cover**→Decompose→**Severity cards**→Amend |
| Response format | Code block | Code block | **Severity-keyed concern cards** | Code block | **Bold header + blockquote** | **Severity-keyed concern cards** |
| Decomposition depth | Medium | Medium | Medium | **Expanded with per-type guides** | Minimal (rules only) | Medium |
| Phrasing register | Formal/instructional | Formal/instructional | Formal/instructional | Formal/instructional | **Conversational/imperative** | Formal/instructional |
| Inertia framing | None | None | None | None | None | **Explicit — "no change" as named competitor** |
| Cover letter placement | Phase 4 (after responses) | **Phase 2 (before responses)** | Phase 4 (after responses) | Phase 4 | Step 4 | **Phase 2 (before responses)** |
| Scope handling note | 1 line | 1 line | 1 line | **Full section with misclassification warning** | 1 line | **Explicit inertia rule for scope** |

## Rubric Coverage Check

All five variations cover:
- C-01: Decomposition table with R-ID / Reviewer / Type / Summary / Severity columns
- C-02: Response block with reviewer comment, response text, manuscript changes per R-ID
- C-03: P1 requires manuscript change (explicitly stated in all variants)
- C-04: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE strategies with register guidance
- C-05: Artifact path + integer frontmatter (explicitly enforced in all variants)
- C-06: Six type categories named (factual / methodological / scope / framing / statistical / presentation)
- C-07: Two-paragraph cover letter with specified structure
- C-08: Amendment pass naming three weakness types (defensive / concedes-too-much / too-brief)
- C-09: No-change responses: 1 paragraph max, scientific rationale (all variants)
- C-10: Scope responses distinctively short (2-3 sentences) in all variants

No rubric criteria are dropped across any variation.
