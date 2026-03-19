If --compact flag: output the hypothesis statement, top 2 falsification conditions, and 1 recommended experiment only. Skip prior analysis and confidence calibration.

You are running /discover-hypothesis for: {{topic}}

State what you believe and what would change your mind before any investigation begins.
This is a commitment artifact -- you cannot move the goalposts after seeing results.

---

## PHASE 1: THE HYPOTHESIS

State the hypothesis in three parts:

**Claim**: [One sentence. What you believe to be true about {{topic}}.]

**Falsification condition**: [One sentence. What specific, observable evidence would prove this claim wrong?]

**Confidence**: [0-100. Where are you starting? 50 = coin flip. 80 = strong prior. 30 = weak hunch.]

**Hypothesis class**:
- [ ] Behavioral -- predicts how users will act
- [ ] Technical -- predicts what the system can or cannot do
- [ ] Market -- predicts competitive or adoption dynamics
- [ ] Causal -- predicts that X causes Y

---

## PHASE 2: THE PRIOR

What did the team believe before this investigation?

**Team belief before**: [One sentence describing the pre-existing assumption or the "everyone knows..." belief this hypothesis is testing.]

**Origin of the prior**: [Where did this belief come from? Customer feedback / gut feel / analogy to another product / prior data / other]

**What would change their mind**:
| Evidence Type | Threshold to shift belief |
|---------------|--------------------------|
| [e.g., user interviews] | [e.g., 5 of 7 users describe the same friction] |
| [e.g., benchmark data]  | [e.g., latency under 200ms in 95th percentile]  |
| [e.g., market research] | [e.g., 2+ competitors ship this by Q3]          |

**Confirmation bias check**: What would the team instinctively dismiss even if it showed up as evidence? Name it now.

---

## PHASE 3: FALSIFICATION TESTS

Design at least 2 specific, observable tests that would prove the hypothesis wrong.
A good falsification test names the measurement, the threshold, and the timeframe.

**Test 1**:
- Method: [Interview / prototype / log analysis / benchmark / literature search / other]
- What to measure: [Specific observable thing]
- Falsification threshold: [If [METRIC] is [VALUE], the hypothesis is wrong]
- Timeframe: [When can this test be run?]

**Test 2**:
- Method: [Interview / prototype / log analysis / benchmark / literature search / other]
- What to measure: [Specific observable thing]
- Falsification threshold: [If [METRIC] is [VALUE], the hypothesis is wrong]
- Timeframe: [When can this test be run?]

[Add Test 3 if the hypothesis is HIGH confidence -- a high-confidence hypothesis needs more falsification surface.]

**If both tests fail to falsify**: The hypothesis survives this round. State what remaining uncertainty exists.

---

## PHASE 4: INVESTIGATION SEQUENCE

Recommended next skills to test this hypothesis (in order):
1. /discover-websearch -- ground the claim in public evidence before running deeper investigation
2. /discover-causal -- trace the cause-chain behind the claim
3. /discover-coherence -- check whether the hypothesis is consistent with other signals on {{topic}}
4. /discover-synthesize -- run after at least 2 other signals exist

Stop if falsification threshold is hit before the full sequence completes.

---

## AMEND

3 ways to sharpen this hypothesis:

1. **Narrow the claim**: The current claim may be too broad. Scope it to a specific user segment, time window, or usage context. Narrower = faster to falsify.

2. **Raise the falsification bar**: If the falsification condition is vague ("poor adoption"), replace it with a number. "Fewer than 3 of 10 users complete the flow in session 1" is falsifiable. "Poor adoption" is not.

3. **Add a null hypothesis**: State the null explicitly -- "There is no meaningful difference between X and Y" -- and design Test 1 to reject the null, not just confirm the claim.

---

Write artifact to: signals/discover/hypothesis/{{topic}}-hypothesis-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-[this-skill]-{date}.md). No namespace subdirectory.
Include frontmatter: skill: discover-hypothesis, topic: {{topic}}, date: {{date}}, confidence: [0-100], verdict: OPEN
