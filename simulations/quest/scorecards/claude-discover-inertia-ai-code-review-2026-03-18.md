Artifact written to `signals/discover/inertia/ai-code-review-inertia-2026-03-18.md`.

---

**Summary:**

**Inertia score: MEDIUM | Switching cost: MEDIUM**

The primary workaround is **ad-hoc LLM paste + GitHub PR human review** — a combination that costs ~$70K/year in reviewer labor for a 5-dev team and produces no artifact trail. Inertia is MEDIUM rather than HIGH because GitHub Copilot Code Review (native, zero-setup) is actively disrupting the status quo and teams are already being asked to evaluate AI review tooling.

**The critical finding:** The single most dangerous inertia condition is the Copilot comparison (#3). Teams evaluating AI code review don't choose between Signal and doing nothing — they choose between Signal and Copilot. Signal must answer "why not just use Copilot?" in one sentence: artifact permanence + topic-scoped reviewer personas + cross-PR pattern detection. If that answer isn't in the pitch, inertia wins by default.

**The workaround failure mode Signal must address:** Paste-to-LLM fails silently across PRs — same bug class ships repeatedly because there's no record of what was flagged. Signal's artifact model fixes this only if artifacts are aggregatable by pattern. Per-PR siloed artifacts have the same failure mode.

---

QUALITY: 4
CLAUDE_COMPATIBLE: Y
NOTES: No existing topic context in signals/discover/inertia/ -- wrote fresh analysis from first principles. Copilot Code Review is a real product (GA 2025) that materially changes the inertia calculation; included as the primary competitive pressure. Phase 5 amendment on artifact aggregation is the highest-value design implication surfaced.
