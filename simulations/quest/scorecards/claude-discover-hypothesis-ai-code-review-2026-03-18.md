Artifact written to `signals/discover/hypothesis/ai-code-review-hypothesis-2026-03-18.md`.

---

**Hypothesis summary**:

**Claim**: Structured AI code review (artifact-producing, topic-scoped) catches materially more actionable defects than paste-to-LLM review because structure enforces coverage discipline that freeform prompts skip.

**Confidence**: 72 -- strong prior, but the inertia signal creates a tension worth flagging immediately: the existing signal identified the failure mode as *no artifact/audit trail*, not *low defect detection rate*. These are different differentiation stories. If websearch finds no quality gap between structured and unstructured review, the hypothesis flips -- the lead claim becomes audit permanence, not coverage quality.

**Key falsification**: Structured review finds fewer than 1.5x actionable issues per diff vs. unstructured review on the same 5 test diffs.

**Critical tension to resolve next**: `/discover-websearch` -- does published evidence support a quality gap, or do models converge on the same findings regardless of prompt scaffolding?

---

QUALITY: 5
CLAUDE_COMPATIBLE: Y
NOTES: Inertia signal provided strong context -- used it to surface the hypothesis tension (quality improvement vs. audit trail) directly in Phase 4 and the status block. Third falsification test added per high-confidence requirement. Null hypothesis explicit in AMEND section.
