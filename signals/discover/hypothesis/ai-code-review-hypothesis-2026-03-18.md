---
skill: discover-hypothesis
topic: ai-code-review
date: 2026-03-18
confidence: 72
verdict: OPEN
---

# Hypothesis: ai-code-review

---

## PHASE 1: THE HYPOTHESIS

**Claim**: Structured AI code review that produces a permanent, topic-scoped artifact catches a materially higher rate of actionable defects than generic paste-to-LLM review, because the structure forces coverage discipline that unstructured prompts skip.

**Falsification condition**: If a controlled comparison shows that generic (unstructured) LLM review and structured artifact-producing review surface defects at a rate within 15% of each other on the same codebase, the claim is wrong -- the artifact model adds process overhead without a corresponding quality gain.

**Confidence**: 72

**Hypothesis class**:
- [ ] Behavioral -- predicts how users will act
- [x] Technical -- predicts what the system can or cannot do
- [ ] Market -- predicts competitive or adoption dynamics
- [ ] Causal -- predicts that X causes Y

*Secondary class*: Causal -- structure causes coverage discipline which causes higher defect detection rate.

---

## PHASE 2: THE PRIOR

**Team belief before**: "AI review is AI review -- the quality of the finding depends on the model, not how you wrap the prompt."

**Origin of the prior**: Analogy to spell-checkers and linters -- the tool catches what it catches regardless of how you invoke it. Reinforced by developers reporting that their ad-hoc paste sessions "work fine" for obvious issues. The paste-to-LLM workaround is not visibly broken, so the assumption is that more structure would not materially change outcomes.

**What would change their mind**:

| Evidence Type | Threshold to shift belief |
|---------------|--------------------------|
| Side-by-side review comparison | Structured review finds 2x or more high-severity issues per 200-line diff compared to unstructured review of the same diff |
| Developer self-report on coverage | 7 of 10 developers report that structured prompt scaffolding caused them to check areas they would have skipped in a free-form session |
| Defect-to-production correlation | In a retrospective over 20+ PRs, structured review artifact records show significantly fewer post-merge defect escapes than PRs with no artifact |
| Coverage completeness audit | Structured review covers >80% of diff surface area (measurable via line/function attribution); unstructured review covers <50% on the same diff |

**Confirmation bias check**: The team will instinctively dismiss findings that structured review is "slower" or "feels heavier" -- framing overhead as a process cost rather than a quality signal. They will also dismiss false positives as noise rather than as evidence of over-coverage. Name it now: any finding that "structure adds friction" will be rationalized as a UX problem, not as evidence that the hypothesis is wrong. The falsification condition must be defect detection rate, not developer comfort.

---

## PHASE 3: FALSIFICATION TESTS

**Test 1**:
- Method: Benchmark on real diffs (literature search / controlled prototype)
- What to measure: Number of unique, actionable findings (not duplicates, not style noise) per 200-line diff across structured vs. unstructured review of the same five diffs
- Falsification threshold: If structured review finds fewer than 1.5x the actionable issues found by unstructured review across 5 test diffs, the coverage-discipline advantage is not real
- Timeframe: Can be run in a single session -- 5 diffs x 2 review modes x 1 hour = ~1 day

**Test 2**:
- Method: Coverage attribution audit (log analysis / prototype)
- What to measure: What percentage of changed lines/functions in a PR diff are explicitly addressed in the review output -- for structured vs. unstructured
- Falsification threshold: If structured review's coverage rate is within 20 percentage points of unstructured review's coverage rate across 5 diffs, coverage discipline is not a meaningful differentiator
- Timeframe: Runnable immediately if 5 sample diffs are available (can use open-source PRs)

**Test 3** (HIGH confidence justifies a third test):
- Method: Retrospective literature search on structured vs. unstructured AI review studies
- What to measure: Whether published evidence (academic or industry) shows a quality difference between prompted/structured and unprompted/freeform LLM code review
- Falsification threshold: If 3 or more independent published findings show no statistically significant quality difference, the hypothesis has no external support base
- Timeframe: 1-2 hours of web search + literature scan

**If all three tests fail to falsify**: The hypothesis survives this round. Remaining uncertainty: the benefit may be real but context-dependent -- structured review may outperform only on complex, multi-concern diffs (security + performance + correctness simultaneously) and not on simple bug fixes. The scope of the claim should be narrowed in the next hypothesis revision to "complex multi-concern diffs."

---

## PHASE 4: INVESTIGATION SEQUENCE

Recommended next skills to test this hypothesis (in order):

1. `/discover-websearch` -- search for published comparisons of structured vs. unstructured LLM code review; look for GitHub Copilot Code Review vs. custom-prompted review benchmarks; search for "AI code review defect detection rate" studies (2024-2026)
2. `/discover-causal` -- trace the cause-chain: does structure actually force coverage, or does the model produce equivalent coverage regardless of prompt scaffolding?
3. `/discover-coherence` -- check whether this hypothesis is consistent with the inertia signal (which identified the paste-to-LLM failure mode as "no artifact, no coverage record, no cross-PR pattern detection") -- are we claiming coverage discipline or artifact permanence as the primary value?
4. `/discover-synthesize` -- run after at least 2 other signals exist; combine with inertia signal to determine whether coverage quality or audit trail is the stronger differentiation story

Stop if Test 1 or Test 2 falsifies before the full sequence -- do not continue investing in the differentiation story if the quality gap does not exist.

---

## AMEND

Three ways to sharpen this hypothesis:

1. **Narrow the claim**: "Structured AI review beats unstructured on all diffs" is too broad. Narrow to: "Structured AI review beats unstructured on diffs with 3+ concerns simultaneously (e.g., security + concurrency + error handling)." This is testable in one session by selecting diffs with known multi-concern failure modes and running both review modes. Narrower claim = faster falsification.

2. **Raise the falsification bar**: The current threshold (15% difference) is vague because it doesn't specify whether that's 15% of findings count or 15% of severity-weighted findings. Replace with: "If the structured review does not find at least one high-severity finding that the unstructured review missed, in 4 of 5 test diffs, the hypothesis is wrong." This is a binary observable per diff, not a percentage calculation.

3. **Add a null hypothesis**: Null: "There is no meaningful difference in defect detection rate between structured and unstructured LLM review on the same diff." Design Test 1 to reject the null -- if unstructured review catches the same high-severity issues as structured review, the null holds. The hypothesis only survives if structured review consistently surfaces findings the unstructured pass missed.

---

## HYPOTHESIS STATUS

```
Verdict: OPEN
Confidence: 72
Next action: /discover-websearch -- search for structured vs. unstructured LLM code review benchmarks
Blocking question: Does the coverage discipline from structured prompting produce a
                   measurably different finding set, or does the model converge on the
                   same issues regardless of prompt scaffolding?
Key tension with inertia signal: Inertia identified the primary failure mode as
                   "no artifact, no audit trail" -- not "low defect detection rate."
                   This hypothesis bets on quality improvement as the lead claim.
                   If websearch shows no quality gap, pivot the differentiation
                   story entirely to artifact permanence (audit trail) and drop
                   the coverage-discipline claim.
```
