---
skill: discover-inertia
topic: ai-code-review
date: 2026-03-18
inertia_score: MEDIUM
switching_cost: MEDIUM
---

# Inertia Analysis: ai-code-review

## PHASE 1 -- WORKAROUND MAP

| Field | Answer |
|-------|--------|
| Workaround name | Ad-hoc LLM paste + GitHub PR human review |
| How it works | (1) Developer opens PR, assigns 1-2 human reviewers. (2) Optionally, developer manually copies diff or key functions into a browser tab running Claude/ChatGPT with a freeform "review this" prompt. (3) Developer reads AI response inline, applies suggestions mentally, closes the tab. (4) Human reviewers add comments over 1-3 days. (5) Developer resolves comments. No artifact produced from either AI or human pass. |
| Who does it | Developer (initiates), senior engineers and tech leads (human reviewers), occasionally QA lead |
| Frequency | Every PR; 2-4 PRs/developer/week; each PR: 30-60 min human review time, 5-15 min ad-hoc LLM session if used at all |
| Implicit cost | 5 devs x 3 PRs/week x 45 min human review = 675 min/week = ~585 hours/year in reviewer time alone. At $120/hr fully loaded = ~$70,000/year in review-cycle labor for a 5-dev team. |
| Hidden cost | No record of what AI reviewers found or missed. Coverage varies by reviewer availability. Review quality degrades under deadline pressure. Bugs that slip through have no audit trail showing what was checked. Inconsistency compounds: the same anti-pattern ships repeatedly because no one connects the dots across PRs. |

---

## PHASE 2 -- SWITCHING COST TABLE

| Cost type | Estimate | Who bears it |
|-----------|----------|--------------|
| Learning / training | 2-4 hours | Developer (Signal skill invocation, artifact format, namespace model) |
| Integration / setup | 4-8 hours | Developer or tech lead (Signal install, reviewer persona config, output path wiring) |
| Process change | 3-4 weeks to re-establish habits | Full dev team (adding /review to pre-PR checklist, reviewing artifacts before requesting human reviewers) |
| Risk during transition | Human reviewers still required during ramp; parallel reviews create comment duplication, confusion about which feedback is authoritative | Team |
| **Total switching cost** | **~2-3 days of direct work + 3-4 weeks of habit formation** | |

Switching cost verdict: MEDIUM (1-5 days of direct cost; weeks of behavioral reorientation)

---

## PHASE 3 -- INERTIA THREAT SCORE

```
Inertia threat: MEDIUM

Override conditions met:
  - Workaround cost is quantifiable: ~$70,000/year in human review labor for 5-dev team
  - GitHub Copilot Code Review (native GitHub product, GA 2025) creates active market
    comparison -- teams already being asked "why aren't we using Copilot review?"
  - Known failure mode: ad-hoc LLM paste produces no artifact, no coverage record,
    no cross-PR pattern detection -- this gap is documentable and increasingly visible
    in post-mortems

Not LOW because:
  - Human PR review is deeply embedded team culture, not broken
  - No regulatory event forcing structured AI review
  - Paste-to-LLM workaround still functions adequately for individuals

Not HIGH because:
  - The cost is real and quantifiable at team scale
  - The competitive landscape (Copilot) is actively disrupting the status quo
  - Teams ARE being asked to evaluate AI review tooling -- the question is which one
```

---

## PHASE 4 -- CONDITIONS FOR INERTIA TO LOSE

1. **Post-mortem trigger: "we reviewed this, how did it ship?"** When a team faces a production incident and needs to show what review coverage existed, the ad-hoc paste-to-LLM workaround produces nothing. Signal's artifact trail (reviewer findings, coverage flags, date-stamped outputs) becomes the only defensible answer. This condition is closest to being true today: teams shipping AI-adjacent features face increasing scrutiny on review process.

2. **Review bottleneck becomes sprint blocker.** When waiting for human reviewer availability consistently delays shipping by 2+ days per sprint (measurable in cycle time metrics), teams start looking for anything that reduces that wait. Signal's ai-code-review lets developers pre-triage with structured AI review before requesting human review -- compressing human review time from 45 min to 10-15 min for already-triaged PRs. The threshold is when the team can demonstrate 30%+ reduction in time-to-merge.

3. **Copilot comparison forces a structured evaluation.** GitHub Copilot Code Review is native, zero-setup, already in the tool teams use. If Signal's ai-code-review cannot articulate a clear advantage over Copilot that a tech lead can explain in one sentence to their manager, inertia wins by default. The adoption barrier Signal must remove: "why not just use Copilot?" The answer must be specific (artifact permanence, cross-PR pattern detection, topic-scoped reviewer personas) -- not generic ("more customizable").

**Most important condition today:** #3. The Copilot comparison is already happening. Teams that evaluate AI code review are comparing Signal against a zero-friction native alternative. Unless Signal's artifact model and topic-scoped review are clearly differentiated, teams will default to the path of least resistance.

---

## PHASE 5 -- AMEND

1. **Switching cost quantification:** Direct cost is ~10-12 hours (setup + training). Habit formation is 3-4 weeks. Opportunity cost during transition (slower PRs while teams learn): ~1 sprint. Total first-month cost: approximately 1 developer-week equivalent.

2. **Workaround failure mode Signal must address:** The absence of a cross-PR pattern record. The paste-to-LLM workaround fails silently -- the same class of bug (e.g., missing null checks, non-validated inputs) ships across multiple PRs because no one has a record of what AI reviewers flagged before. Signal's artifact model fixes this, but the skill must produce artifacts that are searchable by pattern, not just by PR. If artifacts are siloed per PR with no aggregation layer, Signal has the same failure mode as paste-to-LLM.

3. **Single condition most likely to tip teams:** The post-mortem trigger (#1). When a team faces its first "how did this ship?" moment and the only honest answer is "we pasted it into ChatGPT and the reviewer didn't catch it," the demand for an artifact-producing, auditable AI review process becomes concrete. Signal should target teams that have recently had this conversation -- they are the early adopters.
