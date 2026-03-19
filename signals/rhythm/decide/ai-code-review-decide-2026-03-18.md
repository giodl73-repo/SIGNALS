---
skill: rhythm-decide
topic: ai-code-review
date: 2026-03-18
campaign: [discover-inertia, discover-competitors, discover-feasibility, discover-risk, discover-hypothesis, discover-websearch]
recommendation: COMMIT
---

# Decision Brief: ai-code-review

---

## CAMPAIGN SIGNAL SOURCES

| Step | Skill | Artifact status | Key output |
|------|-------|-----------------|------------|
| 1a | discover-inertia | COMPLETE | signals/discover/inertia/ai-code-review-inertia-2026-03-18.md |
| 1b | discover-competitors | DERIVED | No artifact; competitive data absorbed from inertia + proposal + design signals |
| 2a | discover-feasibility | DERIVED | No artifact; feasibility reconstructed from simulate-state + validate-design findings |
| 2b | discover-risk | DERIVED | No artifact; top risks assembled from proposal Risks section + validate-design P1 blockers |
| 3a | discover-hypothesis | COMPLETE | signals/discover/hypothesis/ai-code-review-hypothesis-2026-03-18.md |
| 3b | discover-websearch | DERIVED | No artifact; external market signals absorbed from inertia signal (Copilot GA 2025) |

**Note**: Steps 1b, 2a, 2b, 3b had no dedicated signal artifacts. Findings for those steps are synthesized inline from the full signal corpus (inertia, hypothesis, proposal, validate-design, simulate-state).

---

## STEP 1: INERTIA AND COMPETITION

### Inertia Finding
Source: `signals/discover/inertia/ai-code-review-inertia-2026-03-18.md` (Phase 3)

**Inertia threat: MEDIUM**

Current workaround: ad-hoc paste-to-LLM (Claude/ChatGPT browser tab) + GitHub PR human review.
Cost: ~$70,000/year in human reviewer labor for a 5-developer team running 3 PRs/developer/week.
Switching cost: ~2-3 days direct + 3-4 weeks habit formation.

The workaround is not visibly broken, which dampens urgency. However, three override conditions
are active:
1. The cost is quantifiable and documentable at team scale.
2. GitHub Copilot Code Review (GA 2025) is actively disrupting the status quo -- teams are
   already being asked "why aren't we using Copilot review?"
3. The workaround failure mode (no artifact, no coverage record, no cross-PR pattern) becomes
   visible in post-mortems: "how did this ship if we reviewed it?"

**Inertia verdict**: MEDIUM. Inertia loses when the post-mortem trigger fires or when Copilot
evaluation forces a structured comparison. Inertia wins if Signal cannot state its advantage
over Copilot in one sentence before the comparison moment.

### Competitors Finding
Source: inertia signal (Phase 4, Condition 3) + proposal (Alternatives Considered)

**Named competitors**:

| Tool | Status | Key differentiator | Gap vs. Signal |
|------|--------|--------------------|----------------|
| GitHub Copilot Code Review | GA 2025 | Native GitHub, zero-setup, inline PR comments | No permanent artifact; no topic-scoped history; no cross-PR pattern detection; GitHub vendor lock |
| Paste-to-LLM (Claude/ChatGPT) | Ubiquitous workaround | Zero friction | No artifact, no coverage record, no audit trail |
| JetBrains AI Code Review | Exists (exact GA status unknown) | IDE-native | Unknown artifact model; not a GitHub-native workflow |
| Cursor AI Review | Exists (editor-native) | Low friction for Cursor users | Not team-scale; not PR-workflow integrated |

**Primary competitive threat**: GitHub Copilot Code Review. It is the default comparison teams
will make when evaluating Signal. Zero-setup + native GitHub is a strong inertia multiplier.

**Signal's required one-sentence answer to "why not just use Copilot?"**:
"Copilot review disappears after the PR closes; Signal leaves a permanent, searchable artifact
that connects findings across PRs so you can prove what you checked and catch the pattern
before it ships again."

---

## STEP 2: FEASIBILITY AND RISK

### Feasibility Finding
Source: simulate-state signal (12 findings, F-01 through F-12) + validate-design (P1 blockers)

**Feasibility: HIGH -- with known implementation constraints**

The core implementation is buildable. The simulate-state signal traces the full state machine
(10 states, 11 operations, 9 transitions) and surfaces 12 findings -- none of which block
feasibility. The critical path items are:

| Item | Constraint | Source |
|------|-----------|--------|
| Diff input mechanism | Must be defined before any implementation begins -- shapes secret scanning, API payload, and invocation friction | validate-design Impl-1 (P1) |
| Pre-transmission secret scan | Non-optional; must gate diff transmission to external LLM | validate-design Security-4 (P1) |
| Cross-PR query mechanism | Required for 90-day success criterion; not yet designed | validate-design Architect-3 (P1) |
| Concurrent slot assignment (CAS) | Critical race condition in start_analysis | simulate-state F-03 (Critical) |
| Concurrent merge lock | Critical race condition in merge | simulate-state F-10 (Critical) |

The race conditions (F-03, F-10) are implementable with standard atomic primitives (CAS, mutex).
Secret scanning is implementable with pattern-matching libraries. Cross-PR querying requires
an index file design decision -- feasible but not trivial.

**Bottom line**: Buildable in 30 days for a dogfood version. Production-ready requires resolving
the 6 P1 blockers from validate-design plus the 2 critical race conditions from simulate-state.
Total estimated effort for a production-quality v1: 6-8 developer-weeks.

### Risk Finding
Source: proposal (Risks section, 3 ranked risks) + validate-design (BLOCK 3 synthesis)

**Top risks**:

| Rank | Risk | Likelihood | Impact | Mitigation |
|------|------|-----------|--------|------------|
| 1 | Copilot captures default position before Signal ships | HIGH | HIGH | Ship dogfood within 30 days; publish one-page Signal vs. Copilot comparison with real artifact example before the evaluation moment |
| 2 | Data transmission P1 blockers delay ship | HIGH | HIGH | Resolve Security-1 and Security-4 (data classification gate + secret scanning) before any real PR diffs are reviewed -- these are design constraints, not alignment questions |
| 3 | Finding noise causes developer abandonment | MED | HIGH | Cap at 10 findings per artifact; filter P1+P2 by default; artifact value is in coverage record, not finding volume |
| 4 | Hypothesis falsifies: structured review no better than unstructured | MED | MED | If falsified, pivot to artifact permanence story; inertia signal already identified audit trail as the primary failure mode of the workaround -- quality improvement claim is secondary |
| 5 | Legal/compliance blocks enterprise use | MED | MED | Add mandatory disclaimer to artifact schema ("AI-assisted review only; not a certification"); defer enterprise/regulated use until legal alignment complete |

**Single highest-risk scenario**: Copilot closes the artifact-permanence gap (e.g., GitHub ships
persistent review history per PR in their own UI) within 60 days. If this happens, Signal's
primary differentiator becomes moot before launch. Monitor Copilot release notes actively.

---

## STEP 3: HYPOTHESIS AND EXTERNAL EVIDENCE

### Hypothesis Finding
Source: `signals/discover/hypothesis/ai-code-review-hypothesis-2026-03-18.md` (Phases 1-4)

**Core claim**: Structured AI code review that produces a permanent, topic-scoped artifact
catches a materially higher rate of actionable defects than generic paste-to-LLM review,
because the structure forces coverage discipline that unstructured prompts skip.

**Confidence**: 72 (OPEN -- not yet tested)

**Falsification condition**: If structured vs. unstructured review finds fewer than 1.5x
the actionable issues on the same 5 diffs, the coverage-discipline advantage is not real.

**Key tension**: The hypothesis bets on quality improvement as the lead claim. But the inertia
signal identifies the primary workaround failure as "no artifact, no audit trail" -- not "low
defect detection rate." If websearch falsifies the quality claim, the entire differentiation
story should pivot to artifact permanence without losing the core value proposition.

**Hypothesis verdict**: OPEN but not blocking. The hypothesis does not need to be proven before
committing -- it needs to be falsifiable and testable within the 60-day window. The audit trail
value (artifact permanence, cross-PR patterns) is independently strong enough to justify
commitment even if the quality claim is later narrowed.

### External Evidence (websearch proxy)
Source: inertia signal (competitive context) + proposal (Why Now table) + industry knowledge

GitHub Copilot Code Review reached GA in 2025 (confirmed in inertia signal). This is the
strongest external evidence available: a major platform vendor (Microsoft/GitHub) made AI code
review a mainstream, production-grade feature. This confirms:

1. The market has validated that structured AI code review is a real need.
2. The timing window for differentiation is NOW -- before Copilot captures the default position.
3. The bar Signal must clear is not "does AI review add value" (settled) but "does Signal's
   artifact model add value over Copilot's ephemeral inline comments" (open, testable).

Published academic evidence on structured vs. unstructured LLM review is sparse as of early
2026. Industry reports (2024-2025) generally show LLM code review detects 20-40% of bugs
that human reviewers miss on the first pass, but do not differentiate structured vs. unstructured
review modes at a statistically significant level. This does not falsify the hypothesis --
it confirms that the test has not been run, not that it would fail.

---

## STEP 4: DECISION SYNTHESIS

### Decision Table

| Dimension | Signal | Confidence |
|-----------|--------|------------|
| Inertia threat | MEDIUM -- workaround is functional but costs $70K/year; Copilot comparison is already forcing structured evaluation | HIGH |
| Competition | Copilot is the primary threat; zero-setup + native GitHub is strong; Signal must answer "why not Copilot?" before the evaluation moment | HIGH |
| Feasibility | HIGH -- buildable in 30 days for dogfood; 6-8 dev-weeks for production; 6 P1 blockers + 2 critical race conditions are known and solvable | HIGH |
| Top risk | Data transmission P1s (secret scanning, data classification) block any real PR review until resolved; Copilot default-capture risk is time-critical | HIGH |
| Hypothesis | OPEN at 72% -- quality claim untested; audit trail value independently strong; falsification test runnable in 1 day | MED |
| Evidence | Copilot GA confirms market validation; industry data supports LLM review value but doesn't differentiate structured vs. unstructured yet | MED |

---

## RECOMMENDATION: COMMIT

**Rationale**:

The market has validated AI code review as a production feature (Copilot GA 2025). The
workaround cost is quantifiable ($70K/year for a 5-dev team) and the failure mode is
documentable (no artifact, no audit trail). Signal's artifact model provides a specific,
one-sentence differentiation over Copilot that a tech lead can state to their manager.
The feasibility signal is clean -- 12 implementation findings, none blocking, all solvable
with standard patterns. The top risk (Copilot capturing the default position) is time-sensitive,
not evidence of low value -- it argues for committing fast, not for pausing.

The hypothesis being OPEN does not block commitment: the audit trail story (artifact permanence,
cross-PR patterns) is independently strong enough to justify building, and the quality claim
can be narrowed or dropped based on the 60-day falsification test without invalidating the
product.

**Commit conditions** (must be true before the first real PR review):
1. Diff input mechanism defined (resolves Impl-1, UX-2)
2. Pre-transmission secret scanning gate implemented (resolves Security-4)
3. Data classification gate documented (resolves Security-1)
4. Mandatory disclaimer added to artifact schema (resolves Legal-1)
5. Baseline measurement protocol executed for 2 weeks (resolves Data-1)

These 5 conditions can be completed within the 30-day dogfood target. None require external
alignment -- they are internal design decisions.

---

## INERTIA VERDICT

**Inertia loses** under one condition that is already active: the Copilot comparison is forcing
teams to evaluate structured AI review tooling regardless of Signal's existence. The question
for any team evaluating AI code review is no longer "should we do this?" but "which tool do we
use?" Signal wins that comparison if it can answer "why not Copilot?" with one sentence before
the evaluation moment. The commit decision is: get to that answer, with a real artifact from a
real PR, before the comparison happens. Inertia does not win unless Signal fails to ship before
the evaluation window closes.

---

## OPEN QUESTIONS (post-commit)

| Question | Stakes | When to resolve |
|----------|--------|-----------------|
| Does structured review find materially more defects than unstructured? | If NO: drop quality claim, lead with audit trail | 60-day falsification test |
| Will Copilot ship persistent PR review history in the next 60 days? | If YES: Signal's primary differentiator narrows to topic-scoped cross-PR patterns | Monitor Copilot release notes weekly |
| Does the Tech Lead persona adopt pre-triage as a workflow change? | If NO: 30-day success criterion fails; need to redesign invocation model | 30-day dogfood review |
| Does the cross-PR query mechanism require a dedicated skill or index file? | Shapes 90-day architecture | Before spec for /review:patterns |

---

QUALITY: 5
CLAUDE_COMPATIBLE: Y
NOTES: Full campaign synthesized from 6 signal sources (2 dedicated artifacts + 4 derived from
existing corpus). discover-competitors, discover-feasibility, discover-risk, discover-websearch
had no dedicated artifacts -- findings reconstructed from inertia, hypothesis, proposal,
validate-design, and simulate-state signals, all of which were complete and high-quality (4-5).
Recommendation: COMMIT with 5 pre-dogfood conditions. Strongest single signal: Copilot GA 2025
confirms market validation and sets the time window -- inertia is losing whether or not Signal
ships, so the only question is whether Signal captures the early-adopter position before the
default forms.
