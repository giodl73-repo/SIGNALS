Rubric written to `simulations/quest/rubrics/topic-story-rubric-2026-03-14.md`.

**Design notes:**

The 4 essential criteria map directly to the skill's two defining properties — structure and synthesis:

- **C-01** (structure) and **C-02/C-03** (synthesis) capture the two things that make this skill distinct from a plain summary. C-02 and C-03 are deliberately separate: C-02 tests whether the author *resists* summarizing; C-03 tests whether they *succeeded* at synthesizing. You can fail one without failing the other.
- **C-04** (recommendation) is essential because without it the story has no point of view — it's a think-piece, not a decision artifact.

The recommended criteria address the three most common failure modes after structure/synthesis are satisfied: voice collapse (reads like a bot recap), vague uncertainty ("more work is needed"), and per-signal bloat (key finding inflates into a full recap).

The aspirational criteria are intentionally demanding — C-09 (causal logic in the pattern) requires the author to explain *why* signals converge, not just observe that they do. That's the difference between a senior analyst's synthesis and a junior analyst's.
y
- **Weight**: essential
- **Category**: behavior
- **Text**: The narrative interprets what signals mean together rather than describing each signal in isolation. The document must read as an editorial argument, not a list of per-signal summaries.
- **Pass condition**: The "what the signals say together" section draws a cross-signal conclusion not directly stated in any single signal artifact. If the section merely restates signal-level findings with connective tissue ("Signal A found X. Signal B found Y. In summary..."), it fails.

### C-03 -- Pattern Explicitly Named
- **Weight**: essential
- **Category**: depth
- **Text**: The output must articulate a named or describable pattern -- the emergent insight that comes from the signals converging. This is the central analytical product.
- **Pass condition**: A reader can extract a one-sentence pattern statement ("The signals converge on...") that is genuinely cross-signal. Vague gestures ("the signals are mostly positive") do not pass.

### C-04 -- Valid Recommendation with Rationale
- **Weight**: essential
- **Category**: correctness
- **Text**: The recommendation section must issue one of the four valid verdicts -- proceed, pause, pivot, or abandon -- and connect that verdict to the pattern identified.
- **Pass condition**: The verdict is one of {proceed, pause, pivot, abandon} (or a clear synonym). The rationale cites the pattern, not just individual signals. A verdict without reasoning fails.

---

## Recommended Criteria

*Output is better with these. Each contributes to the recommended score band.*

### C-05 -- Author's Editorial Voice
- **Weight**: recommended
- **Category**: behavior
- **Text**: The narrative is written from an interpretive stance -- not neutral reporting. The author takes a position on what the signals mean. Language such as "the evidence suggests," "what's striking is," "this pattern points toward," or first-person editorial framing signals this quality.
- **Pass condition**: At least two instances of interpretive language that go beyond neutral description. Purely passive or hedge-free factual recitation fails.

### C-06 -- Uncertainty Is Specific
- **Weight**: recommended
- **Category**: depth
- **Text**: The "what remains uncertain" section names concrete open questions, not generic hedges. "We don't know X because signals Y and Z gave conflicting results" passes. "More research may be needed" alone fails.
- **Pass condition**: At least one specific named unknown that a follow-on investigation could address. Generic uncertainty language without a concrete referent fails.

### C-07 -- Signal Findings Are Selective, Not Exhaustive
- **Weight**: recommended
- **Category**: format
- **Text**: The per-signal findings section surfaces the key finding from each signal -- not a comprehensive recap. The skill description explicitly calls for "key finding, not exhaustive." Brevity here is correctness.
- **Pass condition**: Each signal's entry is one to three sentences maximum. Any signal entry that reads as a full summary of the signal artifact fails this criterion.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable.*

### C-08 -- Recommendation Is Action-Forcing
- **Weight**: aspirational
- **Category**: depth
- **Text**: The recommendation goes beyond a verdict to specify a concrete next action -- who should do what, or what the immediate decision gate is. "Proceed" alone is a verdict; "Proceed to prototype; prioritize the auth flow given the risk signal from scout-compliance" is action-forcing.
- **Pass condition**: The recommendation includes at least one concrete follow-on action or decision gate beyond the verdict label.

### C-09 -- Pattern Has Causal Logic
- **Weight**: aspirational
- **Category**: depth
- **Text**: The pattern statement explains WHY the signals converge, not just THAT they converge. A causal account ("signals align because the core assumption held across all three market segments tested") is stronger than a correlation account ("three signals point in the same direction").
- **Pass condition**: The pattern section includes at least one explanatory clause that accounts for the convergence -- not just describes it.
