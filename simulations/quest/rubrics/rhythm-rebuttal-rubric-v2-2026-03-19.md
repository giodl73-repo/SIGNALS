Done. Here's what changed from v1 to v2:

**Formula update**: aspirational denominator changes from `/2` to `/5` (2 criteria → 5 criteria). A skill hitting only C-09 + C-10 now scores 4/10 aspirational instead of 10/10.

**Three new aspirational criteria**:

| ID | Source | What it captures |
|----|--------|-----------------|
| C-11 | V-05 C-03 "Strongest implementation" | P1 "no change" framed as inertia to OVERCOME, not just justify |
| C-12 | V-01 variant name + V-05 Phase 2 | Cover letter written before response blocks — commitment anchor |
| C-13 | V-02 variant name + V-05 | Severity tier headers (`--- P1 CONCERNS ---`) in the response section |

**C-09 tightened**: Pass condition now explicitly requires the no-change brevity constraint to be *stated*, not implied — closing the gap that caused V-03's PARTIAL.

All three signals came directly from the scorecard's "Excellence Signals" section. V-03's decision-tree C-06 pattern was not added since it's already captured as "best implementation" evidence within existing recommended C-06; it distinguishes quality within the criterion rather than adding a new dimension.
 its own row. No concern is merged with another. |
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
| C-09 | No-change responses are brief and non-defensive | behavior | aspirational | Any response ending in "No change to manuscript" is concise (1 paragraph max), states a clear scientific rationale, and does not over-argue. Pass if all no-change responses meet this standard AND the constraint is stated explicitly in the skill (not just implied by format). |
| C-10 | Scope concerns handled distinctively | depth | aspirational | Concerns typed as "scope" use the brief, non-defensive pattern ("beyond scope of this paper") without dismissing the reviewer. Scope responses are noticeably shorter and less argumentative than methodological or factual responses. Pass if all scope-typed responses follow this pattern. |
| C-11 | P1 no-change responses framed as inertia to overcome | depth | aspirational | The skill explicitly names "no change to manuscript" as the default inertia competitor for P1 concerns — author must OVERCOME inertia with evidence, not merely justify position. A framing statement to this effect appears in the P1 rules section. Pass if the inertia/burden framing is present, not just a generic "justification required" rule. Source: V-05 C-03 strongest implementation. |
| C-12 | Cover letter drafted before individual responses | behavior | aspirational | The skill instructs the author to write (or draft) the cover letter before completing individual response blocks, committing to a revision narrative before individual responses can erode it. Pass if the cover letter phase appears structurally earlier than the response-drafting phase. An amendment pass that reconciles the committed cover letter against delivered responses is sufficient evidence. Source: V-01, V-05 cover-first commitment anchor. |
| C-13 | Severity tier headers partition the response section | format | aspirational | The skill inserts `--- P1 CONCERNS ---`, `--- P2 CONCERNS ---`, `--- P3 CONCERNS ---` (or equivalent labeled dividers) within the response section so that high-severity concerns cannot be visually buried by lower-severity editorial notes. Pass if severity-tier headers appear in the response letter structure, not only in the decomposition table. Source: V-02, V-05 severity-tier header pattern. |

---

## Scoring Notes

- If no reviewer comments are provided and no review artifact exists, the skill must surface a clear error. An output that invents fictional reviewer comments is an automatic C-02 fail.
- The amendment pass (Phase 5) is graded on correct identification of weaknesses, not rewrite quality. A correct identification with a weak rewrite still passes C-08.
- Frontmatter field values must be integers. A field containing a string placeholder (e.g., `"n"`) fails C-05.
- C-09 now requires the no-change constraint to be **explicitly stated**, not only implied by format structure. V-03 partial (R1) established that implicit enforcement is insufficient.
- C-11, C-12, C-13 are aspirational, not essential. A skill can reach Golden without them. They distinguish excellent implementations from merely passing ones.
