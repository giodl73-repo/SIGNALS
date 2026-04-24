The background search found two files mentioning `rhythm-rebuttal`:

- `release/.claude/skills/rhythm-rebuttal/SKILL.md` — the skill definition (already read)
- `signals/rhythm-rebuttal.md` — the signal artifact copy

Both were already covered in the rubric generation. Nothing missed.
on, response letter, cover letter, and amendment pass.

## Composite Score Formula

```
score = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | Concern decomposition table is present and complete | correctness | essential | Output includes a Markdown table with columns R-ID, Reviewer, Type, Summary, Severity. Every distinct concern from the reviewer comments appears as its own row. No concern is merged with another. |
| C-02 | Every concern has a response block | correctness | essential | For each R-ID in the decomposition table, a response block exists with all three elements: reviewer comment (exact quote or paraphrase), response text, and manuscript changes. No R-ID is skipped. |
| C-03 | P1 concerns have manuscript changes | correctness | essential | Every concern marked Severity P1 has a non-empty "Manuscript changes" field. "No change" is not acceptable for P1 without explicit strong justification. Pass if all P1 concerns have stated changes. |
| C-04 | Response register is professional and non-defensive | behavior | essential | Responses use one of the three stated strategies (AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE). No response reads as combative, dismissive, or sycophantic. Pass if all responses maintain appropriate academic register. |
| C-05 | Artifact written to correct path with valid frontmatter | format | essential | File is written to `signals/rhythm/rebuttal/{topic}-rebuttal-{date}.md`. Frontmatter contains all required fields: skill, topic, date, reviewer_count, concerns_addressed, manuscript_changes, no_change_responses. Values are integers, not placeholders. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | Concern types are correctly classified | correctness | recommended | Each concern is assigned one of the six defined types: factual, methodological, scope, framing, statistical, presentation. Classification matches the nature of the concern (e.g., a data error is "factual" not "framing"). Pass if >= 80% of type assignments are defensible. |
| C-07 | Cover letter present and structurally correct | coverage | recommended | Output includes a two-paragraph cover letter. Paragraph 1 thanks reviewers and names 3-4 key changes. Paragraph 2 flags any areas of respectful disagreement (or explicitly notes there are none). |
| C-08 | Amendment pass identifies real weaknesses | depth | recommended | Phase 5 names three specific responses that need strengthening, correctly labeled as: too defensive, concedes too much, or too brief. Each flag targets a genuine weakness in the draft response, not a trivially correct observation. |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | No-change responses are brief and non-defensive | behavior | aspirational | Any response ending in "No change to manuscript" is concise (1 paragraph max), states a clear scientific rationale, and does not over-argue. Pass if all no-change responses meet this standard. |
| C-10 | Scope concerns handled distinctively | depth | aspirational | Concerns typed as "scope" use the brief, non-defensive pattern ("beyond scope of this paper") without dismissing the reviewer. Scope responses are noticeably shorter and less argumentative than methodological or factual responses. Pass if all scope-typed responses follow this pattern. |

---

## Scoring Notes

- If no reviewer comments are provided and no review artifact exists, the skill must surface a clear error. An output that invents fictional reviewer comments is an automatic C-02 fail.
- The amendment pass (Phase 5) is graded on correct identification of weaknesses, not rewrite quality. A correct identification with a weak rewrite still passes C-08.
- Frontmatter field values must be integers. A field containing a string placeholder (e.g., `"n"`) fails C-05.
