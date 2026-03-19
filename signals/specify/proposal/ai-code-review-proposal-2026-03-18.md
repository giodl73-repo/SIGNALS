---
skill: specify-proposal
topic: ai-code-review
date: 2026-03-18
---

# Proposal: ai-code-review

---

## PHASE 1 -- SIGNAL SCAN

| Signal file | Skill | Date | Key finding |
|-------------|-------|------|-------------|
| signals/discover/inertia/ai-code-review-inertia-2026-03-18.md | discover-inertia | 2026-03-18 | Ad-hoc paste-to-LLM + human PR review costs ~$70K/year for 5-dev team; inertia is MEDIUM because GitHub Copilot Code Review (GA 2025) is actively forcing structured AI review comparisons |
| signals/discover/hypothesis/ai-code-review-hypothesis-2026-03-18.md | discover-hypothesis | 2026-03-18 | Hypothesis OPEN at 72% confidence: structured review beats unstructured on defect detection, but key tension is whether the primary value is coverage quality or artifact permanence/audit trail |

Prior signal coverage: PARTIAL (2 signals -- inertia + hypothesis; no competitors signal)

Note: No discover-competitors signal exists. The inertia signal names GitHub Copilot Code Review as the primary competitive reference. Recommend running /discover-competitors before spec finalization to confirm competitive positioning.

---

## PHASE 2 -- PROPOSAL

---

### Problem Statement

Today, developers perform AI-assisted code review by manually copying diff content into a browser tab running Claude or ChatGPT, typing a freeform "review this" prompt, reading the response inline, and closing the tab. No artifact is produced. No coverage is recorded. No pattern is traceable across PRs. In parallel, one or two human reviewers are assigned in GitHub and provide comments over one to three days. The human review is the only record that anything was checked. When a bug ships -- and the post-mortem question becomes "how did this get through review?" -- the honest answer is: "we pasted it into an LLM and a senior engineer skimmed it on a deadline." The friction is not in running the review; it is in the absence of any structured output: no coverage map, no cross-PR finding history, no differentiation between what the AI checked and what it skipped. For a five-developer team running three PRs per developer per week, this represents roughly $70,000 per year in human reviewer time, with zero accumulated institutional knowledge from the AI passes.

---

### Proposed Solution

Signal's `/review:code` skill runs structured AI code review against a named topic, producing a permanent artifact that captures reviewer findings, coverage surface, and severity classifications linked to the topic's signal history. The developer invokes `/review:code topic:ai-code-review` before requesting human reviewers, passing the diff context. The developer receives a dated artifact in `signals/review/code/` with actionable findings organized by severity, explicit coverage flags for unchecked areas, and cross-reference to prior findings on the same topic -- compressing human review time by pre-triaging the obvious issues and creating an auditable record that survives the PR.

---

### Why Now

| Trigger type | Active? | Evidence |
|-------------|---------|----------|
| Market shift | YES | GitHub Copilot Code Review reached GA in 2025; teams are now actively evaluating AI code review tooling rather than treating it as experimental -- the question has shifted from "should we use AI review" to "which AI review tool do we use" |
| User data | NO | No usage data collected yet; inertia signal provides cost estimates but no behavioral telemetry |
| Competitive move | YES | GitHub Copilot Code Review is native to GitHub, zero-setup, already in the tool teams use daily -- inertia signal identifies "why not just use Copilot?" as the primary adoption barrier Signal must answer |
| Platform change | NO | No infrastructure change driving urgency |
| Internal driver | YES | Signal's artifact model (permanent, topic-scoped, cross-PR) is architecturally differentiated from Copilot's review model; building now establishes the differentiation story before Copilot captures the default position |

Primary trigger: Competitive move -- GitHub Copilot Code Review (GA 2025) has made structured AI code review a mainstream expectation, and teams evaluating options will default to the zero-friction native tool unless Signal articulates a specific, one-sentence advantage before the comparison moment arrives.

---

### Success Criteria

| Horizon | Outcome | Measurement |
|---------|---------|-------------|
| 30 days | Developers complete end-to-end AI code review for a real PR using the skill and produce a valid artifact | 3 artifacts produced by 2+ developers on distinct PRs, each with at least 5 finding entries and explicit coverage flags |
| 60 days | Human reviewer time per PR decreases measurably on PRs that were pre-triaged with `/review:code` | Average human reviewer comment count drops by 30%+ on signal-reviewed PRs vs. control PRs (same developers, same sprint) |
| 90 days | Cross-PR pattern detection surfaces at least one recurring finding class that was not caught by human review alone | At least one finding class (e.g., missing null checks, unvalidated inputs) identified as recurring across 3+ PRs via artifact search, with no corresponding human review comment trail |

North star metric: Number of production defects attributed to PRs with a Signal artifact vs. PRs without -- if artifact-reviewed PRs show lower post-merge defect rates over a 90-day window, the proposal succeeded.

---

### Stakeholders

| Role | Stake | Alignment needed | Veto? |
|------|-------|-----------------|-------|
| Tech Lead / Engineering Manager | Review process ownership, team velocity, tool adoption decisions | Agreement that pre-triage AI review reduces human reviewer burden without adding process overhead that slows PRs | YES |
| Senior Engineers (human reviewers) | Their review time is being substituted or compressed; they need confidence that AI pre-triage does not degrade review quality or shift accountability to the tool | Agreement on what the artifact covers and what it does not -- human reviewers must not feel the AI review replaces their judgment, only pre-filters noise | NO |
| Developer (primary user) | Wants a faster path to PR approval; will not adopt if invocation adds more than 2-3 minutes to PR prep | Clear, low-friction invocation model; artifact must appear in PR context without requiring a separate workflow | NO |
| Security / Compliance (if applicable) | AI-generated review artifacts may create records with legal or compliance implications; a dated artifact stating "no security issues found" could be cited in audit | Review the artifact format and disclaimer language before shipping; artifact must not imply exhaustive security certification | YES |

Veto holders: Tech Lead / Engineering Manager; Security / Compliance (if applicable)

Critical alignment path: Tech Lead first -- they control whether the skill enters the team's pre-PR checklist. Without tech lead buy-in, developer adoption is individually optional and will not produce the cross-PR pattern data that validates the north star metric. Security alignment is a conditional veto: required before artifacts are used in regulated contexts, not before internal dogfood.

---

### Risks

| Rank | Risk | Likelihood | Impact | Mitigation |
|------|------|-----------|--------|------------|
| 1 | Copilot default captures the market before Signal ships | HIGH | HIGH | Ship a working dogfood version within 30 days on Signal's own codebase; publish a one-page comparison of Signal artifact permanence vs. Copilot inline comments with a real before/after example from a Signal PR -- the comparison must exist before the team evaluation moment, not after |
| 2 | Artifact produces too many low-severity findings, developers treat output as noise and stop invoking the skill | MED | HIGH | Cap artifact output at 10 findings per review; require each finding to classify as HIGH / MED / LOW and filter to HIGH+MED by default; add a coverage summary section that shows what was checked even when findings are minimal -- value is in the coverage record, not finding volume |
| 3 | Hypothesis falsifies: structured review does not produce materially better findings than unstructured paste-to-LLM | MED | MED | If falsified, pivot the differentiation story entirely to artifact permanence and audit trail (already identified as primary failure mode in inertia signal); the coverage discipline claim is secondary and can be dropped without invalidating the product |

Highest-risk scenario: Copilot (HIGH likelihood, HIGH impact) -- GitHub ships incremental Copilot Code Review improvements in the next 60 days that close the artifact permanence gap (e.g., persistent review history per PR in GitHub's own UI), making Signal's primary differentiator moot before launch.

---

### Alternatives Considered

| Alternative | Description | Why considered | Why rejected |
|-------------|-------------|----------------|--------------|
| Do nothing | Teams continue ad-hoc paste-to-LLM + human PR review with no artifact | Always baseline; current state is functional | ~$70K/year in human review labor with zero accumulated institutional knowledge; inertia signal shows this cost is quantifiable and visible to teams under post-mortem scrutiny; Copilot comparison is already forcing structured evaluation regardless of Signal's decision |
| Adopt GitHub Copilot Code Review | Zero-setup, native GitHub integration, already in developers' workflow | Lowest friction path; Copilot is the competitive reference named in inertia signal | Copilot produces inline PR comments with no permanent artifact, no topic-scoped history, no cross-PR pattern detection; teams get AI review but lose the audit trail and institutional memory Signal's artifact model provides; also creates vendor dependency on GitHub for a core review process |
| Build a generic review wrapper (not topic-scoped) | Invoke an LLM with a structured prompt per PR but without Signal's topic registry or artifact naming convention | Lower build cost; faster to ship; removes the Signal-specific onboarding requirement | Reproduces the paste-to-LLM failure mode at the tool level -- findings are per-PR, not cross-PR; no topic registry means no pattern detection; without the artifact naming convention, review outputs are unsearchable; this is Copilot without the GitHub integration, which is strictly worse |

---

## PHASE 3 -- ALIGNMENT CHECKLIST

Before this proposal moves to spec, the following teams need to sign off.

| Team | Question they need answered | Status |
|------|----------------------------|--------|
| Engineering | Is structured AI review + artifact write implementable within the existing Signal skill invocation model? What is the rough effort for a working dogfood version? | [ ] Not started |
| Design | Is there a developer-facing UX for invoking the skill and viewing the artifact that fits inside the PR workflow (e.g., CLI output that maps to GitHub PR comment format)? | [ ] Not started |
| Legal | Do dated AI review artifacts that state findings (or absence of findings) create any liability or compliance exposure in regulated development contexts? | [ ] Not started |
| Security | Does the skill send diff content to an external LLM API? If so, what data handling controls apply? Are there cases where the diff contains secrets that would be transmitted? | [ ] Not started |
| Support | Does shipping `/review:code` change expectations about what Signal guarantees to catch -- and does that change the support burden when bugs ship despite a review artifact existing? | [ ] Not started |

Minimum viable alignment: Engineering (feasibility + effort) + Security (diff content data handling) before spec writing. Security is elevated to minimum viable because the skill transmits code to an external API and that data handling question must be answered before any real PRs are reviewed.

---

## PHASE 4 -- AMEND

AMEND mode: not active. No amendments at initial proposal.

Section to amend: [problem-statement | proposed-solution | why-now | success-criteria |
                   stakeholders | risks | alternatives | alignment-checklist]
New information: [what changed]
Updated section: [rewrite only the named section]
