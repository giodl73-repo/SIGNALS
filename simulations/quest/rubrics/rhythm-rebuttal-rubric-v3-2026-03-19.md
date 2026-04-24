Here is the complete updated rubric:

---

# Rubric: rhythm-rebuttal (v3)

## Change Log

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
| Aspirational (C-09–C-16) | 10 | (passed / **8**) * 10 |

Golden threshold: >= 90 AND all essential pass.

---

## Aspirational Criteria (updated section)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | No-change brevity explicitly stated | behavior | 1 paragraph max, scientific rationale, no over-arguing — **stated**, not implied |
| C-10 | Scope concerns handled distinctively | depth | 2–3 sentences, no argument, state claim space and move on |
| C-11 | P1 no-change framed as inertia to overcome | depth | Skill names "no change" as default inertia; author must OVERCOME with evidence |
| C-12 | Cover letter before individual responses | behavior | Cover letter phase structurally precedes decomposition and response phases |
| C-13 | Severity tier headers in response section | format | `--- P1 CONCERNS ---` etc. appear in the response letter, not only in the table |
| **C-14** | **Critical constraints in pre-workflow RULE-N block** | **format** | **A numbered RULE-N block before all phases covers at minimum the no-change and P1 constraints** |
| **C-15** | **Weakness forecast precedes response drafting** | **depth** | **Forecast step (predict likely failures) appears before drafting; amendment pass validates the prediction** |
| **C-16** | **Dialogue exchange format (REVIEWER SAID / AUTHOR RESPONDS / MANUSCRIPT OUTCOME)** | **format** | **Three-part atomic exchange template present and applied consistently in the response section** |

---

**Design notes on the three new criteria:**

- **C-14** captures the architectural insight from V-04: front-loading all rules into RULE-1 through RULE-N means a practitioner reads them before entering the workflow, not mid-stream when cognitive load is high. It is a placement criterion, not a content criterion — the rules themselves are already required by C-03, C-04, C-09, C-10.

- **C-15** upgrades C-08 from retrospective to predictive. A skill that forecasts "these three response types will be the weak spots" before drafting, then validates the forecast in the amendment pass, turns C-08 from housekeeping into a calibration loop. PARTIAL on C-08 does not imply PARTIAL on C-15 — they measure different things.

- **C-16** captures the structural anti-merging property of V-02's dialogue format. Because each exchange is a discrete atomic unit, concern merging requires active effort to break the template. This is distinct from C-01, which requires correct decomposition — C-16 is about the format that *enforces* it mechanically. A skill can pass C-01 without C-16 (by following rules) but C-16 makes C-01 structurally guaranteed.
at | essential | File is written to `signals/rhythm/rebuttal/{topic}-rebuttal-{date}.md`. Frontmatter contains all required fields: skill, topic, date, reviewer_count, concerns_addressed, manuscript_changes, no_change_responses. Values are integers, not placeholders. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | Concern types are correctly classified | correctness | recommended | Each concern is assigned one of the six defined types: factual, methodological, scope, framing, statistical, presentation. Classification matches the nature of the concern (e.g., a data error is "factual" not "framing"). Pass if >= 80% of type assignments are defensible. |
| C-07 | Cover letter present and structurally correct | coverage | recommended | Output includes a two-paragraph cover letter. Paragraph 1 thanks reviewers and names 3-4 key changes. Paragraph 2 flags any areas of respectful disagreement (or explicitly notes there are none). |
| C-08 | Amendment pass identifies real weaknesses | depth | recommended | Phase 5 names three specific responses that need strengthening, correctly labeled as: too defensive, concedes too much, or too brief. Each flag targets a genuine weakness in the draft response, not a trivially correct observation. |

---

## Aspirational Criteria (10 pts total)

Denominator: 8. Score = (criteria passed / 8) * 10.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | No-change responses are brief and non-defensive | behavior | aspirational | Any response ending in "No change to manuscript" is concise (1 paragraph max), states a clear scientific rationale, and does not over-argue. Pass if all no-change responses meet this standard AND the constraint is stated explicitly in the skill (not just implied by format). |
| C-10 | Scope concerns handled distinctively | depth | aspirational | Concerns typed as "scope" use the brief, non-defensive pattern ("beyond scope of this paper") without dismissing the reviewer. Scope responses are noticeably shorter and less argumentative than methodological or factual responses. Pass if all scope-typed responses follow this pattern. |
| C-11 | P1 no-change responses framed as inertia to overcome | depth | aspirational | The skill explicitly names "no change to manuscript" as the default inertia competitor for P1 concerns — author must OVERCOME inertia with evidence, not merely justify position. A framing statement to this effect appears in the P1 rules section. Pass if the inertia/burden framing is present, not just a generic "justification required" rule. Source: V-05 C-03 strongest implementation. |
| C-12 | Cover letter drafted before individual responses | behavior | aspirational | The skill instructs the author to write (or draft) the cover letter before completing individual response blocks, committing to a revision narrative before individual responses can erode it. Pass if the cover letter phase appears structurally earlier than the response-drafting phase. An amendment pass that reconciles the committed cover letter against delivered responses is sufficient evidence. Source: V-01, V-05 cover-first commitment anchor. |
| C-13 | Severity tier headers partition the response section | format | aspirational | The skill inserts `--- P1 CONCERNS ---`, `--- P2 CONCERNS ---`, `--- P3 CONCERNS ---` (or equivalent labeled dividers) within the response section so that high-severity concerns cannot be visually buried by lower-severity editorial notes. Pass if severity-tier headers appear in the response letter structure, not only in the decomposition table. Source: V-02, V-05 severity-tier header pattern. |
| C-14 | Critical constraints hoisted into pre-workflow RULE-N block | format | aspirational | The skill places all critical behavioral constraints (no-change brevity, scope handling, P1 inertia framing, register rules) in a numbered RULE-N block before the workflow phases begin. Rules are not scattered across phase descriptions where mid-workflow rule blindness can occur. Pass if a pre-workflow rules block exists and covers at minimum the no-change and P1 constraints. Source: V-04 constraint-first-register pattern. |
| C-15 | Weakness forecast precedes response drafting | depth | aspirational | The skill includes a dedicated forecasting step that predicts which response types are most likely to fail (too defensive, concedes too much, too brief) before individual responses are drafted. The amendment pass then validates the forecast against delivered responses, making C-08 a confirmed prediction rather than a post-hoc observation. Pass if the forecast step appears before the response-drafting phase and the amendment pass references it. Source: V-03 amendment-predictive-forecast pattern. |
| C-16 | Dialogue exchange format structures response blocks | format | aspirational | Response blocks use a three-part dialogue exchange structure: REVIEWER SAID (exact quote or paraphrase) / AUTHOR RESPONDS (strategy labeled: AGREE / PARTIALLY AGREE / RESPECTFULLY DISAGREE) / MANUSCRIPT OUTCOME. This discrete unit format makes concern merging structurally impossible, since each exchange is atomic. Pass if the three-part template is present in the response section and applied consistently. Source: V-02 dialogue-exchange-format pattern. |

---

## Scoring Notes

- If no reviewer comments are provided and no review artifact exists, the skill must surface a clear error. An output that invents fictional reviewer comments is an automatic C-02 fail.
- The amendment pass (Phase 5) is graded on correct identification of weaknesses, not rewrite quality. A correct identification with a weak rewrite still passes C-08.
- Frontmatter field values must be integers. A field containing a string placeholder (e.g., `"n"`) fails C-05.
- C-09 requires the no-change constraint to be **explicitly stated**, not only implied by format structure. V-03 partial (R1) established that implicit enforcement is insufficient.
- C-11, C-12, C-13 are aspirational, not essential. A skill can reach Golden without them. They distinguish excellent implementations from merely passing ones.
- C-14, C-15, C-16 are also aspirational. C-14 (pre-workflow RULE-N block) and C-16 (dialogue exchange format) are architectural choices that affect all criteria simultaneously; C-15 (weakness forecast) upgrades C-08 from observation to validated prediction.
- A skill implementing C-16 (dialogue exchange) implicitly satisfies C-01's no-merging requirement by structural enforcement; both are still graded independently since C-01 is essential.
