---
skill: rhythm-decide
topic: ai-code-review
date: 2026-03-19
campaign: [discover-inertia, discover-competitors, discover-feasibility, discover-risk, discover-hypothesis, discover-websearch]
recommendation: COMMIT
confidence: standard
for: team
iterations: 1
---

# Decision Brief: ai-code-review

---

## CAMPAIGN SIGNAL SOURCES

| Step | Skill | Artifact | Status |
|------|-------|----------|--------|
| 1a | discover-inertia | signals/discover/inertia/ai-code-review-inertia-2026-03-18.md | PRIOR (confirmed) |
| 1b | discover-competitors | signals/discover/competitors/ai-code-review-competitors-2026-03-19.md | NEW |
| 2a | discover-feasibility | signals/discover/feasibility/ai-code-review-feasibility-2026-03-19.md | NEW |
| 2b | discover-risk | signals/discover/risk/ai-code-review-risk-2026-03-19.md | NEW |
| 3a | discover-hypothesis | signals/discover/hypothesis/ai-code-review-hypothesis-2026-03-18.md | PRIOR (confirmed) |
| 3b | discover-websearch | signals/discover/websearch/ai-code-review-websearch-2026-03-19.md | NEW |

All 6 campaign skills produced dedicated signal artifacts. 2 prior signals (inertia, hypothesis) from 2026-03-18 were reviewed and confirmed; 4 new signals generated on 2026-03-19.

---

## STEP 1: INERTIA AND COMPETITION

### 1a. Inertia Finding

Source: `signals/discover/inertia/ai-code-review-inertia-2026-03-18.md` (Phase 3)

**Inertia threat: MEDIUM**

Current workaround: ad-hoc paste-to-LLM (Claude/ChatGPT browser tab) + GitHub PR human review. Cost: ~$70,000/year in human reviewer labor for a 5-developer team (28 hrs/sprint at $120/hr fully loaded). Switching cost: ~2-3 days direct + 3-4 weeks habit formation.

The workaround is not visibly broken, which dampens urgency. Three override conditions justify downgrade from HIGH:
1. Cost is quantifiable at team scale ($70K/year)
2. GitHub Copilot Code Review (GA 2025) creates active competitive pressure -- teams are being asked "why aren't we using Copilot review?"
3. Known failure mode: ad-hoc paste produces no artifact, no coverage record, no cross-PR pattern detection -- increasingly visible in post-mortems

**Closest active condition**: The Copilot comparison (#3 in inertia signal). Teams evaluating AI code review are comparing any tool against a zero-friction native alternative. The differentiation must be specific and one-sentence explainable.

### 1b. Competitive Finding

Source: `signals/discover/competitors/ai-code-review-competitors-2026-03-19.md`

**7 named competitors assessed. 2 HIGH threat (Copilot, CodeRabbit), 2 MEDIUM (Greptile, Qodo), 3 LOW (Sourcegraph Cody, SonarQube, Codacy).**

| Competitor | Threat | Why |
|------------|--------|-----|
| GitHub Copilot Code Review | HIGH | Zero setup, native GitHub, bundled pricing ($10-19/mo), already default for teams on Copilot |
| CodeRabbit | HIGH | Structured PR summaries, security-focused, multi-platform, $15-30/mo |
| Greptile | MEDIUM | Full codebase context (not just diff), but no cross-PR memory |
| Qodo | MEDIUM | Multi-repo context, enterprise governance, but no topic-scoped aggregation |

**Whitespace confirmed**: No current tool produces topic-scoped, persistent review artifacts with cross-PR pattern detection. This whitespace is verified by absence in two independent 2026 tool surveys (Manus 2026, AIWire 2026). Source: discover-websearch Claim 4.

**Table stakes for entry**: PR-native integration, <5 min review time, <15% false positive rate, security coverage, multi-language support.

---

## STEP 2: FEASIBILITY AND RISK

### 2a. Feasibility Finding

Source: `signals/discover/feasibility/ai-code-review-feasibility-2026-03-19.md`

**Score: 72/100 -- FEASIBLE WITH CAVEATS**

| Metric | Value |
|--------|-------|
| Team | 2 engineers |
| Timeline | 3-4 sprints (6-8 weeks) |
| Hours available | 480 |
| Hours estimated | 340 |
| Budget status | UNDER-BUDGET (+140 hrs buffer) |

5 of 7 components rated GREEN. 2 rated YELLOW:
- **Cross-PR pattern memory** (YELLOW): Tension with P-03 (Self-Contained Skills). Resolution: ship Phase 1 without cross-PR memory; design Phase 2 as a separate `review-patterns` synthesis skill that reads prior review artifacts.
- **Git diff extraction** (YELLOW): Platform-specific complexity (Windows MSYS2, macOS, Linux). Resolution: build standalone `signal-diff` utility, test on 3 platforms before integration (~2 days).

No RED blockers. Both YELLOW items have clear resolution paths that do not block Phase 1 shipping.

### 2b. Risk Finding

Source: `signals/discover/risk/ai-code-review-risk-2026-03-19.md`

**Overall pre-commitment risk level: MEDIUM**

Top 3 risks ranked by Severity x Likelihood:

| Rank | Risk | Severity | Likelihood | Mitigation |
|------|------|----------|------------|------------|
| 1 | Competitive displacement by Copilot | HIGH | MEDIUM | Ship topic-scoped aggregation + custom personas before Copilot closes the gap; monitor monthly |
| 2 | False positive alert fatigue | HIGH | MEDIUM | Quest loop must include FP-rate measurement; hard gate at <12% FP rate; tune for precision over recall |
| 3 | Inertia wins by default | HIGH | MEDIUM | Target teams in post-mortem moment when absence of audit trail is freshly painful |

Compliance risk: MEDIUM. Artifacts stored locally in repo (git-controlled). Signal's provenance model (P-09) is a compliance advantage over paste-to-LLM and Copilot.

---

## STEP 3: EVIDENCE

### 3a. Hypothesis Finding

Source: `signals/discover/hypothesis/ai-code-review-hypothesis-2026-03-18.md`

**Claim**: Structured AI code review that produces a permanent, topic-scoped artifact catches a materially higher rate of actionable defects than generic paste-to-LLM review, because the structure forces coverage discipline that unstructured prompts skip.

**Falsification condition**: If a controlled comparison shows that generic and structured LLM review surface defects at a rate within 15% of each other on the same codebase, the claim is wrong.

**Confidence**: 72/100

**Status**: OPEN. Two falsification tests designed but not yet executed. The hypothesis is plausible but unproven.

**Key tension**: The inertia signal identifies the primary failure mode as "no artifact, no audit trail" -- not "low defect detection rate." The hypothesis bets on quality improvement. If websearch shows no quality gap, the differentiation story should pivot entirely to artifact permanence.

### 3b. Web Evidence Finding

Source: `signals/discover/websearch/ai-code-review-websearch-2026-03-19.md`

**5 claims checked. 4 confirmed. 0 contradicted. 1 unconfirmed.**

| # | Claim | Verdict | Source |
|---|-------|---------|--------|
| 1 | Structured review catches more defects | UNCONFIRMED | No direct comparison study found (IJCRT 2025, Qodo 2025) |
| 2 | 5-15% FP rate; excess causes abandonment | CONFIRMED | Digital Applied 2025, Cubic 2025 |
| 3 | 84-90% AI adoption; 46% distrust accuracy | CONFIRMED | Stack Overflow Survey 2025, Infolia 2025 |
| 4 | No tool has cross-PR pattern memory | CONFIRMED | Manus 2026, AIWire 2026 (confirmed by absence) |
| 5 | Copilot is diff-only, ephemeral comments | CONFIRMED | Pull Panda 2025, Greptile 2026 |

**Critical finding**: The core hypothesis (Claim 1) is unconfirmed by external evidence. No published study compares structured vs. unstructured LLM code review on the same codebase. The quality-improvement story cannot be cited externally. However, the differentiation story (Claim 4: cross-PR pattern memory is uncontested whitespace) is confirmed.

**Implication**: Lead the value proposition with the confirmed differentiators (artifact permanence, audit trail, cross-PR memory, compliance-ready provenance) rather than the unconfirmed one (higher defect detection rate). The quality story can be added later if Signal runs its own internal benchmark.

---

## STEP 4: SYNTHESIS

### Decision Table

| Dimension | Signal | Confidence |
|-----------|--------|------------|
| Inertia threat | **MEDIUM** -- Workaround costs $70K/year but is invisible; Copilot comparison is the forcing function; post-mortem trigger is the tipping point | HIGH |
| Feasibility | **72/100 FEASIBLE WITH CAVEATS** -- 340 hrs estimated, 480 available; 2 YELLOW items have clear Phase 1/Phase 2 resolution | HIGH |
| Top risk | **Competitive displacement by Copilot** -- if GitHub ships persistent review history before Signal, the window closes. Mitigation: ship differentiated features first; monitor monthly | MED |
| Hypothesis | **Structured review improves defect detection** -- confidence 72, OPEN, unconfirmed by external evidence. Pivot lead story to artifact permanence | MED |
| Evidence | **4 of 5 claims confirmed**; whitespace (cross-PR pattern memory) is real and uncontested; Copilot is confirmed diff-only/ephemeral; core quality claim ungrounded | HIGH |

### Recommendation: **COMMIT**

### Rationale

The competitive whitespace is real and externally confirmed: no current tool produces topic-scoped, persistent review artifacts with cross-PR pattern detection. The market is large (84-90% of developers use AI tools; $70K/year workaround cost per 5-dev team), the build is feasible within budget (340/480 hrs, no RED blockers), and the inertia threat is only MEDIUM -- meaning teams ARE actively evaluating alternatives to their paste-to-LLM workaround. The primary risk is competitive timing: Copilot could close the artifact gap. Ship Phase 1 (base structured review with artifact output) fast, then Phase 2 (cross-PR pattern memory) to claim the whitespace before the window closes.

### Inertia Verdict

**Inertia loses -- conditionally.** The paste-to-LLM workaround fails silently (no artifact, no audit trail, no cross-PR memory), and this failure becomes visible in two forcing scenarios: (1) a post-mortem asking "how did this ship?" and (2) a team evaluation asking "why not just use Copilot?" For scenario 1, Signal's artifact model is the only tool that produces an auditable answer. For scenario 2, Signal must articulate a one-sentence advantage over the free default: "Copilot reviews your diff and forgets; Signal reviews your diff, records the finding, and tells you when the same pattern ships again." If Signal cannot deliver that sentence as a working feature, inertia wins.

---

## CAMPAIGN FINDINGS: NEW VS. CONFIRMED

| Finding | Status | Source |
|---------|--------|--------|
| Inertia threat MEDIUM (not HIGH, not LOW) | CONFIRMED (from 2026-03-18 inertia signal) | discover-inertia |
| Cross-PR pattern memory is uncontested whitespace | NEW (confirmed by 2 independent 2026 surveys) | discover-competitors + discover-websearch |
| Copilot is the primary named competitor (HIGH threat) | NEW (first dedicated competitive assessment) | discover-competitors |
| Feasibility 72/100 with 2 YELLOW items (no RED) | NEW (first dedicated feasibility assessment) | discover-feasibility |
| Competitive timing is the #1 risk | NEW (first risk register for this topic) | discover-risk |
| Core quality-improvement hypothesis is unconfirmed externally | NEW (websearch found no direct comparison study) | discover-websearch |
| Lead value prop should be artifact permanence, not quality improvement | NEW (derived from websearch evidence gap) | synthesis |
| Hypothesis confidence 72, OPEN | CONFIRMED (from 2026-03-18 hypothesis signal) | discover-hypothesis |

---

## ACTION ITEMS

| # | Action | Owner | Timeline |
|---|--------|-------|----------|
| 1 | Ship Phase 1: base review skill with per-PR artifact output (no cross-PR memory) | Engineering | Sprints 1-3 |
| 2 | Hard-gate quest loop at <12% false positive rate before shipping | Engineering | Sprint 2 |
| 3 | Build `signal-diff` cross-platform utility | Engineering | Sprint 1 |
| 4 | Resolve P-03 tension: design `review-patterns` as separate Phase 2 skill | Architecture | Sprint 2 |
| 5 | Run internal benchmark: structured vs. unstructured review on 5 real diffs | PM/Research | Sprint 1 |
| 6 | Monitor GitHub Copilot changelog monthly for persistent review features | PM | Ongoing |
| 7 | Draft one-sentence differentiator for team leads evaluating Copilot vs. Signal | PM | Sprint 1 |

---

QUALITY: 4
COPILOT_COMPATIBLE: Y
NOTES: All 6 campaign skills executed with dedicated artifacts. Web search worked well for competitive and market claims. The core hypothesis (structured > unstructured) remains ungrounded by external evidence -- this is the most important finding for product strategy. Copilot ran the full campaign sequence without issues; the only difference from Claude Code would be slightly less aggressive prompt-following on the structured template sections (Copilot tends to be more concise, which is actually fine for decision briefs).
