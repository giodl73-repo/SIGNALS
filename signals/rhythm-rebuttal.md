You are running /rhythm-rebuttal for: {{topic}}

Generates the formal response-to-reviewers letter. This is the highest-frequency use case once papers are under submission. The skill reads reviewer comments (from validate-referee or pasted actual reviews) and produces a structured, professional response.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: the review artifact (from validate-referee) or the reviewer comments provided as input.
Read: the original paper or draft if available.

---

## PHASE 2 -- CONCERN DECOMPOSITION

Extract every distinct concern as a numbered item. One concern = one response.

| R-ID | Reviewer | Type | Summary | Severity |
|------|----------|------|---------|---------|
| R-01 | Referee 1 | factual / methodological / scope / framing / statistical / presentation | [1-sentence summary] | P1/P2/P3 |

Types matter for the response strategy:
- **factual**: correct the error directly, cite the evidence
- **methodological**: either fix the method or explain why it's adequate
- **scope**: "beyond scope of this paper" response — must be brief and non-defensive
- **framing**: clarify what the paper does and doesn't claim
- **statistical**: power, effect sizes, corrections — either add the analysis or explain the constraint
- **presentation**: fix in revision, acknowledge in response

---

## PHASE 3 -- RESPONSE LETTER

For each R-ID, produce a response block:

```
**R-[NN]: [Reviewer N] — [concern summary]**

*Reviewer comment*: "[exact quote or paraphrase of the concern]"

*Response*:
[1-3 paragraphs. Register: professional, non-defensive, grateful.
Strategies:
  AGREE: "The reviewer is correct. We have [done X] in the revised manuscript."
  PARTIALLY AGREE: "We agree that [X]. However, [qualification]. We have [compromise action]."
  RESPECTFULLY DISAGREE: "We appreciate this concern. However, [evidence/reasoning]. We have added [clarifying text] to §N to make this clear."]

*Manuscript changes*: [Specific change made — section, line, what was added/removed. Or: "No change to manuscript — rationale above."]
```

Every P1 concern must have a manuscript change. "No change" requires strong justification.

---

## PHASE 4 -- COVER LETTER

Two-paragraph cover letter:

**Paragraph 1**: Thank the reviewers, name the key changes made in this revision.
"We thank the three referees for their careful reading of [paper title]. In response to their comments, we have [list 3-4 main changes]."

**Paragraph 2**: Flag any areas of respectful disagreement.
"We respectfully maintain our position on [X] for the following reasons: [brief rationale]. We have added text to §N to clarify this."

---

## PHASE 5 -- AMEND

Three responses that need strengthening:
1. [Response that is too defensive — rewrite to be more confident]
2. [Response that concedes too much — identify what can be held]
3. [Response that is too brief — the concern is more serious than the response acknowledges]

Write artifact to: signals/rhythm/rebuttal/{{topic}}-rebuttal-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-rebuttal, topic: {{topic}}, date: {{date}}, reviewer_count: [n], concerns_addressed: [n], manuscript_changes: [n], no_change_responses: [n]
