**Decision Brief: ai-code-review**

| Dimension | Signal | Confidence |
|-----------|--------|------------|
| Inertia threat | MEDIUM -- $70K/year workaround cost; Copilot comparison already forcing structured evaluation | HIGH |
| Competition | Copilot is the primary threat (GA 2025, zero-setup, native GitHub); Signal must answer "why not Copilot?" before the evaluation moment | HIGH |
| Feasibility | HIGH -- dogfood-ready in 30 days; production in 6-8 dev-weeks; 6 P1 blockers + 2 critical race conditions, all known and solvable | HIGH |
| Top risk | Data transmission P1s (secret scanning, data classification) block real PR review until resolved; Copilot default-capture is time-critical | HIGH |
| Hypothesis | OPEN at 72% -- quality claim untested; audit trail value independently strong regardless of outcome | MED |
| Evidence | Copilot GA confirms market validation; industry data supports LLM review value but doesn't differentiate structured vs. unstructured | MED |

---

**Recommendation: COMMIT**

The market has validated AI code review as production-grade (Copilot GA 2025). The workaround failure mode is documentable (no artifact, no audit trail). Signal's one-sentence Copilot answer is: *"Copilot review disappears when the PR closes; Signal leaves a permanent, searchable artifact that connects findings across PRs."* Feasibility is clean -- 12 implementation findings from simulate-state, none blocking. The hypothesis being open doesn't block commitment: the audit trail story is independently strong enough to justify building now.

**5 pre-dogfood conditions** (all internal, achievable in 30 days):
1. Diff input mechanism defined
2. Pre-transmission secret scanning gate implemented
3. Data classification gate documented
4. Mandatory disclaimer added to artifact schema
5. 2-week baseline measurement protocol executed

**Inertia verdict**: Inertia loses. Copilot GA is already forcing structured AI review evaluations regardless of Signal. The question for every team is now "which tool?" not "should we?" Signal's window is: get to a real artifact from a real PR before the comparison happens.

Artifact written to: `signals/rhythm/decide/ai-code-review-decide-2026-03-18.md`

---

QUALITY: 5
CLAUDE_COMPATIBLE: Y
NOTES: Full campaign synthesized from 6 sources. Steps 1b/2a/2b/3b had no dedicated artifacts -- findings derived from existing corpus (inertia, hypothesis, proposal, validate-design, simulate-state). All source signals were complete and high-quality (4-5). Strongest single input: Copilot GA 2025 sets the time window and reframes the decision from "is this worth building?" to "how fast can we ship before the default forms?"
