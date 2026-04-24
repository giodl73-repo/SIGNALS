`topic-story-rubric-v4-2026-03-14.md` written. Three new criteria:

---

**C-16 -- Section Failure Modes Named in Template**
From V-01/V-03 PARTIAL C-14 vs V-02 PASS C-14. C-14 requires architecturally distinct stances; C-16 captures why V-02 could achieve it when the others couldn't — each section named the wrong operation, making the pass condition self-auditable. A section with an operation label but no failure mode leaves "architecturally distinct" as a judgment call at write-time.

**C-17 -- Collapse-Risk Sections Carry Own Anti-Neutral Instruction**
From V-01 PARTIAL C-11 / V-03 PARTIAL C-05+C-11 vs V-02 PASS C-11. Uncertainty and recommendation are the documented failure points — voice anchored only in synthesis leaves two sections undefended. C-11 tests whether register held; C-17 tests whether each collapse-risk section has its own enforcement mechanism. A skeptic check inherited from synthesis doesn't satisfy it; the instruction must live in the section.

**C-18 -- Signal Findings Section Includes Per-Finding Decision Check**
From V-02/V-03 PARTIAL C-10 vs V-01 PASS C-10. Both failing variations provided decision-relevance framing at the section level; V-01 passed because the inertia label at the signal findings header gave a per-item filter the author applies once per finding. Framing states the goal; a named per-item question is an operation with a yes/no result. C-10 tests the output; C-18 tests the mechanism.

**Scoring**: 11 aspirational criteria (C-08--C-18) sharing 10 pts, ~0.5-1.5 pts each. Formula unchanged.
failure-mode labels in every section structurally prevented collapse. C-11 tests whether the register held; C-17 requires each collapse-risk section to carry its own enforcement mechanism, not to inherit voice from synthesis.

**C-18 -- Signal Findings Section Includes Per-Finding Decision Check**
From the V-02 PARTIAL C-10 / V-03 PARTIAL C-10 vs V-01 PASS C-10 pattern. C-10 requires the document to be decision-oriented rather than completeness-oriented; C-18 requires the signal findings section to include a named, per-finding decision filter expressed as an answerable question. V-02 and V-03 provided framing ("find the most decision-relevant finding"; "one sentence, decision-relevant only") but no repeatable per-item check. V-01 passed because the inertia test was labeled at the signal findings header, providing a filter the author could apply to each finding individually. Framing instructs orientation at the section level; a named per-item check is operationally different -- the author applies it once per finding and arrives at a yes/no result. C-10 passes on a document that demonstrates decision-salience in the output; C-18 passes only if the mechanism for achieving it is present in the template.

The aspirational scoring note was updated: 11 criteria (C-08--C-18) now share the 10-point band (~0.5-1.5 pts each with partial credit). Composite formula unchanged.

### Inherited design rationale (v3)

Three aspirational criteria added in v3 (C-13, C-14, C-15), one per Round 2 scorecard pattern:

**C-13** -- From the C-10/C-12 synergy pattern. Round 2 found that decision-orientation and falsifiability are the same epistemic habit ("what makes this assertion defensible?"). C-13 captures the document-wide form: the inertia test must be visible in at least two non-synthesis sections, not just in signal selection (C-10) or the pattern statement (C-12). C-10 and C-12 each passing in their own sections does not satisfy C-13.

**C-14** -- From the C-11 orthogonality pattern. C-11 requires interpretive language in every section; C-14 requires each section's stance to be analytically distinct -- a different function, not just a different tone. Finding section curates for salience. Synthesis names the shape. Uncertainty accounts honestly. Recommendation advocates with accountability. Uniform register throughout, however interpretive, does not pass. This is the mechanism that makes C-11 and C-10/C-12 coexist.

**C-15** -- From the minimum viable C-12 pattern. C-12 requires a falsifiable claim to exist; C-15 requires the author to run the test in the open -- a rhetorical question ("what would they have to show is false?") or a conditional negation ("this claim fails if X"). A well-formed falsifiable claim that never names its own disproof condition does not pass C-15.

### Inherited design rationale (v2)

Three aspirational criteria added in v2 (C-10, C-11, C-12), one per Round 1 scorecard pattern:

**C-10** -- From the audience pressure pattern. Deliberate omission of detail that doesn't change the verdict. Pass condition catches documents that attempt comprehensive coverage rather than decision salience.

**C-11** -- From the trailing tone instruction pattern. C-05 fires on the synthesis section, but the uncertainty and recommendation sections frequently revert to neutral register. C-11 requires all four sections to exhibit interpretive language.

**C-12** -- From the causal contrast framing pattern. One level above C-09: C-09 requires a causal account to exist; C-12 requires it to be precise enough to disprove. "Conditions are favorable" passes C-09 and fails C-12.

### Inherited design rationale (v1)

The 4 essential criteria map directly to the skill's two defining properties -- structure and synthesis:

- **C-01** (structure) and **C-02/C-03** (synthesis) are deliberately separate: C-02 tests whether the author *resists* summarizing; C-03 tests whether they *succeeded* at synthesizing. You can fail one without failing the other.
- **C-04** (recommendation) is essential because without it the story has no point of view -- it's a think-piece, not a decision artifact.

The recommended criteria address the three most common failure modes after structure/synthesis are satisfied: voice collapse, vague uncertainty, and per-signal bloat.

The aspirational criteria are intentionally demanding. C-09 requires explaining *why* signals converge, not just observing that they do. C-10--C-12 require the output to behave like a senior analyst's product -- calibrated for a decision-maker, editorially consistent throughout, and causally precise. C-13--C-15 require the senior analyst habit to be architecturally embedded and visible, not incidentally present. C-16--C-18 require the template itself to enforce those habits structurally -- failure modes named per section, collapse-risk sections defended at the source, and the decision filter expressed as a per-item operation rather than a framing instruction.

---

## Essential Criteria

*All four must pass. Failure on any essential criterion caps composite at 59.*

### C-01 -- Four-Section Structure Present
- **Weight**: essential
- **Category**: format
- **Text**: The output must contain all four required sections: (1) per-signal findings, (2) what the signals say together, (3) what remains uncertain, (4) recommendation. Any missing section is an automatic essential fail.
- **Pass condition**: All four sections are present and labeled. A document that folds two sections together or omits one fails regardless of prose quality.

### C-02 -- Cross-Signal Synthesis (Not Summary)
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

*Output is better with these. Each contributes to the recommended score band (30 pts total, 10 pts each).*

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

*Raise the bar once essential and recommended are stable. 10 pts total across C-08--C-18, ~0.5-1.5 pts each, partial credit allowed.*

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

### C-10 -- Narrative Is Decision-Oriented, Not Completeness-Oriented
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The document is written for someone who must act, not someone who wants a full account. The author has made deliberate editorial choices about what to include based on what changes the decision -- and what to omit because it does not. A story calibrated for a decision-maker is shorter and sharper than one calibrated for comprehensiveness. Detail that fills the picture but does not change the verdict is left out.
- **Pass condition**: The document shows at least one deliberate omission -- detail a comprehensive report would include but this story excludes -- and every section stays focused on what drives or informs the decision. A document that attempts completeness across all signals rather than salience for a decision fails this criterion.

### C-11 -- Editorial Register Sustained Across All Sections
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The interpretive stance present in the synthesis section persists into the recommendation and uncertainty sections. Editorial voice is not a property of the opening -- it is the register of the entire document. The most common failure mode is a strong editorial synthesis followed by neutral reporting in the uncertainty section ("There are some areas where more data would be helpful") and a verdict-only recommendation. Every section must maintain the stance.
- **Pass condition**: All four sections contain at least one instance of interpretive language. A document that establishes strong voice in synthesis but reverts to neutral factual reporting in uncertainty or recommendation fails.

### C-12 -- Causal Claim Is Falsifiable
- **Weight**: aspirational
- **Category**: depth
- **Text**: The causal account in the pattern section is specific enough that a reader could identify what evidence would disprove it. "Signals converge because the API rate limits are not a blocker for our use case" is falsifiable -- show rate limit violations at scale and the claim falls. "Signals converge because conditions are favorable" is not falsifiable. This is a higher bar than C-09, which requires a causal account to exist; C-12 requires that account to be precise.
- **Pass condition**: The explanatory clause in the pattern section names a specific mechanism, assumption, or structural condition that, if shown false, would invalidate the pattern claim. A causal account that cannot be disproved is not a causal account -- it is a restatement of convergence in causal language.

### C-13 -- Inertia Test Applied Document-Wide
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The author applies a unified defensibility test to every substantive assertion in the document -- not just to signal selection (C-10) or the pattern statement (C-12). The test has two forms at different scales: "does this sentence change the verdict?" and "what would disprove this claim?" Both are expressions of the same epistemic habit. When this test runs throughout, decision-orientation and causal precision emerge together rather than appearing independently in isolated sections. A document where C-10 and C-12 each pass in their own sections but not elsewhere has not achieved C-13.
- **Pass condition**: The inertia habit is visible in at least two non-synthesis sections -- either as explicit omission with stated rationale ("this finding does not alter the verdict"), or as a named disproof condition applied outside the pattern section. Evidence in only one section does not pass.

### C-14 -- Per-Section Stance Is Architecturally Distinct
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The analyst occupies a different named role in each section, not the same editorial voice applied uniformly throughout. C-05 requires interpretive language; C-11 requires it in every section; C-14 requires each section's stance to be analytically distinct -- a different function, not just a different tone. The finding section curates for salience; the synthesis section names the shape; the uncertainty section accounts for limits honestly; the recommendation section advocates with accountability. These are not interchangeable. A document where every section sounds like the same author saying the same kind of thing at the same level of abstraction has not achieved C-14 even if it passes C-11.
- **Pass condition**: Each of the four sections occupies a distinct analytical stance that could not be confused with any other section's stance. The stances may be explicit (named roles or framing) or strongly implied by section-specific vocabulary and abstraction level. Uniform register throughout, however interpretive, does not pass.

### C-15 -- Falsifiability Self-Check Is Explicit
- **Weight**: aspirational
- **Category**: depth
- **Text**: The document contains a visible moment where the author names what would disprove the causal claim -- not just a claim that is falsifiable in form, but an explicit analytical operation the reader can verify. This is one level above C-12: C-12 requires a falsifiable claim to exist; C-15 requires the author to have run the falsifiability test in the open. The minimum viable form is a rhetorical question ("what would they have to show is false?") or a conditional negation ("this claim does not hold if [specific condition]"). A well-formed falsifiable claim that never names its own disproof condition does not pass C-15.
- **Pass condition**: The document contains at least one explicit statement of the form "this claim fails if X," "what would disprove this is Y," or equivalent rhetorical form. The named condition must be specific and empirically checkable. "If the data is wrong" or "if our assumptions are off" does not qualify.

### C-16 -- Section Failure Modes Named in Template
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every section in the template names the specific wrong operation the author performs when they misuse that section -- not just what the section should do, but what it looks like when it fails. C-14 requires stances to be architecturally distinct; C-16 requires the failure mode for each stance to be explicitly labeled so the author can self-audit. Without named failure modes, C-14's pass condition is a judgment call the author cannot verify at write-time. With named failure modes, wrong-operation detection becomes a checkable step. The failure modes must be section-specific: the wrong operation for the finding section (transcribing outputs rather than curating for salience) is not the wrong operation for the recommendation section (stating a verdict without defending the adjacent alternative).
- **Pass condition**: Each of the four required sections has a named failure mode in the template -- the specific behavior that indicates the wrong operation is being performed. A section with a named operation but no named failure mode does not satisfy C-16. Generic failure modes ("not being specific enough," "being too long") do not qualify; the failure mode must name the wrong cognitive operation for that section.

### C-17 -- Collapse-Risk Sections Carry Own Anti-Neutral Instruction
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The uncertainty and recommendation sections each contain an explicit instruction preventing register collapse -- a stated directive, a failure-mode label, or a voice anchor specific to that section. These two sections are the documented failure points for C-11: editorial voice established in synthesis frequently does not persist into them. A template that provides anti-neutral instruction only in synthesis leaves the two collapse-risk sections structurally undefended. C-11 tests whether the register held in the final document; C-17 tests whether the mechanism for holding it is present in each section's template. A skeptic check in the recommendation section satisfies C-17 for that section if it is a required element, not an optional closing note.
- **Pass condition**: Both the uncertainty section and the recommendation section contain at least one explicit anti-neutral enforcement element -- a voice instruction, a failure-mode label for neutral-register drift, or a required stance phrase. An anti-neutral instruction present only in synthesis, a framing note present only in document-level preamble, or a closing reminder that post-dates the sections all fail this criterion.

### C-18 -- Signal Findings Section Includes Per-Finding Decision Check
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The signal findings section template includes a named, repeatable decision filter that the author applies to each individual finding -- not a framing instruction at the section level, but a per-item check expressed as an answerable question. C-10 requires the document to be decision-oriented; C-18 requires the mechanism for achieving this to be operationalized in the findings section as a named operation. Framing instructions ("include only decision-relevant findings") describe the goal. A per-item check ("for each finding, ask: does this change whether to build {topic}?") is an operation the author applies once per finding and can answer yes or no. A template that instructs the author to be selective without specifying the decision criterion does not pass C-18. The criterion named in the filter must be the build decision, not a generic salience criterion.
- **Pass condition**: The signal findings section template includes an explicit per-finding filter expressed as a question or binary test, where the criterion is the build-or-not decision for the topic under investigation. "The single most decision-relevant finding" is framing. "For each finding: does this change whether to build {topic}? If no, it does not appear here" is a named per-item operation. Only the latter passes.

---

## Scoring Reference

| Band | Score | Meaning |
|------|-------|---------|
| Essential fail | 0-59 | One or more essential criteria failed |
| Passing | 60-79 | All essential pass; recommended weak |
| Good | 80-89 | All essential pass; recommended mostly pass |
| Golden | 90-100 | All essential pass; recommended strong; aspirational present |

**Composite formula**: `essential_score + recommended_score + aspirational_score`

- Essential: 15 pts per criterion x 4 = 60 pts. All-or-nothing per criterion (no partial).
- Recommended: 10 pts per criterion x 3 = 30 pts. Partial credit allowed (5 pts for PARTIAL).
- Aspirational: 10 pts total across C-08--C-18, ~0.5-1.5 pts per criterion. Partial credit allowed.
