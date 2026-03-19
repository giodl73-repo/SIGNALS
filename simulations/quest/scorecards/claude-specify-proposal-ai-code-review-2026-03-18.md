## PHASE 1 -- SIGNAL SCAN

| Signal file | Skill | Date | Key finding |
|-------------|-------|------|-------------|
| signals/discover/inertia/ai-code-review-inertia-2026-03-18.md | discover-inertia | 2026-03-18 | Ad-hoc paste-to-LLM + human PR review costs ~$70K/year for 5-dev team; MEDIUM inertia because Copilot is forcing structured evaluation comparisons |
| signals/discover/hypothesis/ai-code-review-hypothesis-2026-03-18.md | discover-hypothesis | 2026-03-18 | Hypothesis OPEN (72% confidence): structured review catches more defects, but key tension is whether primary value is coverage quality vs. artifact permanence |

Prior signal coverage: **PARTIAL (2 signals -- no competitors signal)**

---

## PHASE 2 -- PROPOSAL (summary)

**Problem Statement**: Developers paste diffs into browser LLM tabs, get a response, close the tab. No artifact. No coverage record. No cross-PR pattern history. ~$70K/year in human review labor for a 5-dev team with zero accumulated institutional knowledge from the AI passes.

**Proposed Solution**: `/review:code topic:ai-code-review` runs structured AI review before requesting human reviewers, producing a permanent dated artifact with findings, coverage flags, and cross-reference to prior topic signals. Human review time compresses because noise is pre-triaged.

**Primary trigger**: Competitive move -- GitHub Copilot Code Review (GA 2025) has made AI review a mainstream expectation. Teams evaluating options default to Copilot unless Signal answers "why not just use Copilot?" with a specific, demonstrable answer before the comparison moment.

**North star metric**: Lower post-merge defect rate on Signal-artifact-reviewed PRs vs. control PRs over 90 days.

**Veto holders**: Tech Lead/EM (process ownership) + Security (diff content sent to external API -- elevated to minimum viable alignment).

**Highest risk**: Copilot ships persistent artifact history in GitHub UI within 60 days, closing Signal's primary differentiator before launch.

---

Artifact written to: `signals/specify/proposal/ai-code-review-proposal-2026-03-18.md`

---

QUALITY: 4
CLAUDE_COMPATIBLE: Y
NOTES: Two prior signals provided solid grounding -- inertia gave concrete cost data and competitive framing; hypothesis surfaced the artifact-permanence vs. coverage-quality tension that shaped the differentiation story. No competitors signal exists; proposal flags this gap and incorporates Copilot as the named competitive reference from inertia. Security was elevated to minimum viable alignment (from optional) because the skill transmits diff content to an external API -- this is a real data handling question that blocks dogfood use on real PRs.
