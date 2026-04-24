`topic-story-rubric-v7-2026-03-14.md` written.

**Three new criteria extracted from R6 excellence signals:**

**C-25 -- Checklist Extension Preserves Binary-Verifiability: Each New Item Is Independently Audited**
From Signal 1 (C-22 totality). C-22 fires on the assembled checklist; C-25 fires on the per-item design discipline at addition time. The gap: a structural checklist extended with one adequacy item (will the field's content be specific?) rather than a presence item (does the field appear?) fails C-22 in total. C-25 requires separating the structural gate from the quality aspiration before any item is added.

**C-26 -- Labeled Fields Introduced by Each Design Axis Are Registered in the Checklist at Incorporation Time**
From Signal 2 (multi-axis orphaning). C-24 fires on orphaned fields at rubric-application time; C-26 fires on the design-time practice that creates them. V-05's three orphaned fields came from a single unregistered axis. The design rule: incorporating a second axis obligates an immediate checklist sweep for every field that axis introduces -- not a retrospective audit.

**C-27 -- Binary-Verifiable Complete Coverage Is a Single Design Property, Not Two Independent Optimizations**
From Signal 3 (compositional antagonism). R6 produced no variation satisfying both C-22 and C-24 simultaneously -- each variation optimized one property while foreclosing the other. C-27 requires both to emerge from the same design procedure: for each required labeled field in the complete template inventory, write one presence-verification item. This procedure is not decomposable into sequential passes.

**Scoring updated:** 20 aspirational criteria (C-08--C-27), 0.5 pts each (10/20). Formula unchanged.
d to have a checklist item; C-26 requires the checklist to be updated at the moment each design axis is incorporated, not retrospectively. V-05 failed C-24 because it inherited `**Baseline distance**:`, `**Prior position**:`, and `**Signals establish**:` from the inertia-framing design axis but its checklist was built against a different axis (V-01's falsifiability-centered structure). The orphaning was systematic -- all three missing items came from a single unregistered axis. C-24 fires on the presence of orphaned fields; C-26 fires on the design practice that creates them: treating a checklist as complete when its scope matches one design axis while the template incorporates labeled fields from a second. The design rule is: every labeled field has an originating design axis, and the checklist must be updated as a required step whenever a new design axis is incorporated -- not as a retrospective audit after all fields are assembled. A template author who adds labeled fields from a second design axis without simultaneously updating the checklist has violated C-26, even if the orphaning is not yet visible in the current version's labeled field inventory.

**C-27 -- Binary-Verifiable Complete Coverage Is a Single Design Property, Not Two Independent Optimizations**
From R6 Signal 3 (C-22 and C-24 compositional antagonism). C-22 (every item is a locate-and-find operation) and C-24 (every labeled field has a checklist item, every checklist item maps to a labeled field) can each be satisfied independently by designs that achieve one while failing the other. V-01 achieves C-24 by maintaining a minimal labeled-field set, but fails C-22 because one item tests content quality rather than field presence. V-05 achieves C-22 by confining all items to locate-and-find operations, but fails C-24 because three inherited fields are not covered. No variation in R6 satisfies both simultaneously. C-27 fires on the compound design requirement: a checklist that satisfies C-22 and C-24 must achieve both properties from the same design pass over the template's full labeled-field inventory. The procedure that guarantees this: for each required labeled field in the complete template (including fields introduced by every design axis present), write exactly one checklist item that verifies the field's presence by locating its label string. Applied uniformly, this procedure simultaneously produces locate-and-find items (satisfying C-22) and complete field coverage (satisfying C-24). A checklist designed by any other method -- optimizing binary-verifiability first and then checking coverage, or achieving coverage first and then auditing item form -- risks the compositional failure R6 demonstrated, because each optimization pass can introduce violations of the property the other pass achieved.

**Scoring updated**: 20 aspirational criteria (C-08--C-27) sharing 10 pts, 0.5 pts each (10/20). Formula unchanged.

### Inherited design rationale (v6)

Three aspirational criteria added in v6 (C-22, C-23, C-24), one per Round 5 scorecard pattern:

**C-22** -- From V-01's checklist item design in R5. C-19 requires items to target named structural requirements; C-22 captures the quality gap between "targeting a named area" and "answerable by locating a specific element." V-01's items could be verified by reading one instruction in one section -- no quality judgment required. "Does Section 2 include a binary yes/no filter applied per signal?" is a locate-and-find operation. "Is the document decision-oriented?" is an editorial assessment. C-19 passes on item count and requirement-targeting; C-22 passes only when every item can be verified by finding or not finding a specific named element. The pass condition is total: one editorial item disqualifies the entire checklist.

**C-23** -- From V-01's S4 and S5 scan instructions in R5. V-01 passed C-17 and failed C-21. The intermediate form it deployed -- "scan every sentence -- if a sentence names uncertainty without naming a verdict consequence, revise" -- names the structural condition at sentence grain without providing a quotable string. C-17 fires on any anti-neutral directive; C-23 fires on naming the sentence-level structural condition; C-21 fires on providing a quoted string the author can match. V-01 satisfied C-23 but not C-21. C-23 is the precondition for C-21: you name the condition before you can provide an example of it.

**C-24** -- From the C-19/C-20 structural pairing visible across V-01 and V-02 in R5. The two criteria encode the same logic at different ends of the writing act: the checklist verifies before writing that a required element will be present; the labeled field confirms after writing where to find it. C-24 requires the pairing to be complete -- every required labeled output field in the template has a corresponding pre-artifact checklist item, and every checklist item verifying a required output element has a corresponding labeled field. A template can pass both C-19 and C-20 without C-24 if they don't correspond. Orphaned checklist items and orphaned labeled fields both fail.

### Inherited design rationale (v5)

Three aspirational criteria added in v5 (C-19, C-20, C-21), one per Round 4 scorecard pattern:

**C-19** -- From V-01's enforcement pattern in R4. Every enforcement mechanism cited for C-10, C-12, C-13, C-14, C-16, C-17, C-18 ran through a numbered pre-artifact check. The innovation is aggregation: structural requirements embedded in section headers and body text are passive constraints discoverable only by reading every section. A checklist converts them into an active pre-writing gate. None of C-16, C-17, or C-18 requires the author to actively verify compliance before writing; C-19 does. A template whose structural requirements are present but not aggregated into a pre-writing check does not satisfy C-19.

**C-20** -- From C-15's persistent PARTIAL across R3 and R4. C-15 requires the author to run the falsifiability check in the open; C-20 requires the disproof condition to appear as a required labeled field in the output, not as an embedded instruction to name it. The distinction is structural: embedded instructions produce conditions entangled in prose, variable in placement, not locatable without reading the body text. A required labeled field (`**Disproof condition**: [The claim fails if X.]`) produces a verifiable artifact element. Two rounds of PARTIAL show that embedded instructions do not reliably produce labeled fields. C-20 fires on the template structure, not the output quality.

**C-21** -- From V-02's C-17 being scored "strongest in R4." C-17 requires anti-neutral instruction inside collapse-risk sections; C-21 requires that instruction to name at least two verbatim hedge patterns the author can recognize and reject. "Do not retreat to neutral language" requires judgment at write-time. "Do not write 'Based on the available evidence, it would be reasonable to...' or 'The team should consider...'" enables detection -- the author scans for the named strings. C-17 passes on any anti-neutral instruction; C-21 passes only if the instruction names recognizable phrases the author can match against their draft.

### Inherited design rationale (v4)

Three aspirational criteria added in v4 (C-16, C-17, C-18), one per Round 3 scorecard pattern:

**C-16** -- From V-01/V-03 PARTIAL C-14 vs V-02 PASS C-14 in R3. C-14 requires architecturally distinct stances; C-16 captures why V-02 could achieve it when the others couldn't -- each section named the wrong operation, making the pass condition self-auditable. A section with an operation label but no failure mode leaves "architecturally distinct" as a judgment call at write-time. The failure mode must name the specific wrong cognitive operation for that section, not a generic complaint.

**C-17** -- From V-01 PARTIAL C-11 / V-03 PARTIAL C-05+C-11 vs V-02 PASS C-11 in R3. Uncertainty and recommendation are the documented failure points -- voice anchored only in synthesis leaves two sections undefended. C-11 tests whether register held; C-17 tests whether each collapse-risk section has its own enforcement mechanism. A skeptic check inherited from synthesis doesn't satisfy it; the instruction must live in the section.

**C-18** -- From V-02/V-03 PARTIAL C-10 vs V-01 PASS C-10 in R3. Both failing variations provided decision-relevance framing at the section level; V-01 passed because the inertia label at the signal findings header gave a per-item filter the author applies once per finding. Framing states the goal; a named per-item question is an operation with a yes/no result. C-10 tests the output; C-18 tests the mechanism.

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

The aspirational criteria are intentionally demanding. C-09 requires explaining *why* signals converge, not just observing that they do. C-10--C-12 require the output to behave like a senior analyst's product -- calibrated for a decision-maker, editorially consistent throughout, and causally precise. C-13--C-15 require the senior analyst habit to be architecturally embedded and visible, not incidentally present. C-16--C-18 require the template itself to enforce those habits structurally -- failure modes named per section, collapse-risk sections defended at the source, and the decision filter expressed as a per-item operation rather than a framing instruction. C-19--C-21 require the enforcement mechanisms to be active, not passive -- aggregated into a pre-writing checklist, bound to a labeled output field, and operationalized as verbatim pattern-matching rather than orientation instructions. C-22--C-24 require the enforcement mechanisms to be internally coherent -- checklist items designed for structural verification rather than quality judgment, anti-neutral directives that name the sentence-level failure condition rather than instruct orientation, and a complete correspondence between pre-writing checklist items and required labeled output fields. C-25--C-27 require the enforcement mechanisms to remain coherent under composition -- each new checklist item independently audited for binary-verifiability before inclusion, each new design axis registering its labeled fields into the checklist at incorporation time, and binary-verifiable complete coverage achieved as a single design property rather than the residue of two independent optimizations that happen to coexist.

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

*Raise the bar once essential and recommended are stable. 10 pts total across C-08--C-27, 0.5 pts each (10/20), partial credit allowed.*

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

### C-19 -- Template Contains Numbered Pre-Artifact Checklist
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The template includes a numbered pre-artifact checklist that the author runs before writing -- aggregating the structural requirements from C-16, C-17, and C-18 into an active verification step rather than leaving them embedded in section headers and body text. C-16 requires failure modes to exist; C-17 requires anti-neutral instructions inside collapse-risk sections; C-18 requires a per-finding decision filter in the signal findings section. None of these requires the author to actively verify compliance before writing. Without a pre-artifact check, structural requirements are discoverable only by reading every section in sequence; an author can satisfy them incidentally or miss them entirely. A numbered pre-artifact checklist makes compliance a required gate, not a passive property. The checklist must be positioned before the section scaffolding so the author encounters it before writing any section.
- **Pass condition**: The template contains a numbered pre-artifact checklist with at least three items, each targeting a named structural requirement (not generic writing quality). The checklist must appear before the section scaffolding. A post-artifact review checklist does not satisfy C-19. Checklist items that test generic quality ("Is the writing clear?") do not count toward the minimum; items must be checkable against a named structural requirement from the template.

### C-20 -- Disproof Condition Appears as Required Labeled Artifact Field
- **Weight**: aspirational
- **Category**: depth
- **Text**: The disproof condition for the causal claim appears as a required labeled field in the output -- a named slot the template enforces -- not as a condition embedded in body prose following an instruction to "name it explicitly." C-15 requires the author to have run the falsifiability check in the open; C-20 requires the template to provide a dedicated labeled location for the result. The distinction is structural: an embedded instruction produces disproof conditions that vary in placement, legibility, and separability from the surrounding paragraph. A required labeled field (e.g., `**Disproof condition**: [The claim fails if X.]` or `*Fails if*: [specific condition]`) produces a verifiable artifact element the rubric can locate without reading the body text. Two rounds of PARTIAL on C-15 show that embedded instructions do not reliably produce labeled fields: the instruction is followed in spirit but not in form, and the condition remains entangled in prose. C-20 fires on the template structure, not the output quality; a template that instructs well but provides no labeled slot fails C-20 even if the author produces a strong disproof condition.
- **Pass condition**: The template includes a required labeled field in the pattern/synthesis section that explicitly receives the disproof condition as a standalone element, separate from the causal claim it tests. The field must be a named slot in the template (not a property of the author's prose style). An instruction to "name the condition" embedded in section body text does not pass, even if it reliably produces a disproof condition in the output.

### C-21 -- Anti-Neutral Directives Include Verbatim Forbidden Patterns
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The anti-neutral enforcement instructions in collapse-risk sections name at least two verbatim or near-verbatim hedge patterns the author should recognize and reject -- not just instruct against neutral language. C-17 requires anti-neutral instruction to exist inside the uncertainty and recommendation sections; C-21 requires that instruction to be operationalized as pattern-matching, not orientation. The difference is write-time verifiability: "Do not retreat to neutral language" requires the author to judge whether their language is neutral. "Do not write 'Based on the available evidence, it would be reasonable to...' or 'The team should consider...'" enables detection -- the author can scan their draft for the named strings. V-02's C-17 was scored as "strongest in R4" specifically because its directives included specific verbatim examples of neutral-register phrases. C-17 passes on any anti-neutral instruction present inside the section; C-21 passes only if that instruction names recognizable phrases the author can match against their draft.
- **Pass condition**: At least one collapse-risk section (uncertainty or recommendation) contains an anti-neutral directive that names a minimum of two verbatim or near-verbatim hedge phrases with identifying strings. General instructions ("avoid hedging," "be direct," "take a position," "do not be neutral") do not satisfy C-21 regardless of their placement or force. The phrases must be specific enough that an author could search their own text for them.

### C-22 -- Checklist Items Are Binary-Verifiable Against Named Template Elements
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every item in the pre-artifact checklist can be answered yes or no by locating a specific named element in the template or output -- without quality assessment. C-19 requires the checklist to exist and its items to target named structural requirements; C-22 requires each item to be designed so that verification is a locate-and-find operation, not an editorial judgment. The distinction is the author's cognitive task at check-time: "Does Section 2 include a binary yes/no filter applied per signal?" can be answered by reading one instruction in Section 2. "Is the document decision-oriented?" requires the author to evaluate the section as a whole. Binary-verifiable items function as structural gates because the answer is unambiguous; quality-assessment items function as prompts whose answer depends on the author's self-assessment. A checklist that targets named requirements but frames each item as a quality question does not satisfy C-22 even if the same requirements are covered. The pass condition is total: one editorial item disqualifies the entire checklist regardless of how many binary-verifiable items accompany it.
- **Pass condition**: Every checklist item names a specific template element (a labeled field, a required instruction, a named structural property) that can be found or not found in the template. Items that require quality assessment ("Is X specific enough?" "Does Y hold throughout?") do not pass C-22 even if they target structural areas. Items must be answerable by structural inspection, not editorial review.

### C-23 -- Anti-Neutral Directives Name the Sentence-Level Failure Condition
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The anti-neutral enforcement instructions in collapse-risk sections name the specific structural condition at the sentence level that indicates neutral register -- not just what register to avoid (C-17) and not yet the verbatim string to match (C-21). The condition identifies what feature of a sentence signals the wrong operation: "if a sentence names uncertainty without naming a verdict consequence" names the structural failure at sentence grain. "Do not retreat to neutral language" requires the author to judge register holistically. A named sentence-level condition makes the scan more directed than orientation while remaining distinct from verbatim string detection. C-17 fires on any anti-neutral directive inside the section; C-23 fires on naming a sentence-level structural condition; C-21 fires on providing a quotable string. A template can pass C-23 without passing C-21 -- V-01's S4 and S5 demonstrated this in R5 -- and C-23 is a precondition for the full operationalization C-21 requires.
- **Pass condition**: At least one collapse-risk section contains an anti-neutral directive that names a specific sentence-level structural condition indicating the wrong operation ("if a sentence does X," "any sentence that lacks Y"). A directive that names only the outcome to avoid ("neutral language," "hedging," "passive voice") does not pass C-23 even if the named outcome is precise. The condition must identify a structural feature the author can scan for, prior to supplying any verbatim example.

### C-24 -- Checklist Items and Labeled Output Fields Form Complete Structural Pairs
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Every required labeled output field in the template has a corresponding pre-artifact checklist item, and every checklist item that verifies a required output element has a corresponding labeled field in the template. C-19 requires a pre-artifact checklist; C-20 requires a labeled field for the disproof condition. C-24 requires the two enforcement mechanisms to be complete as a pair. The logic: a checklist item verifies before writing that a required element will be present; a labeled field confirms after writing where to find it. When every required output element has both a checklist verifier and a labeled field, the structural closure is complete -- no required element can be missing from the artifact without the checklist having failed to catch it, and no checklist item verifies something the template does not also require as a named output slot. A template where some required elements appear in prose without labeled fields, or where checklist items cover areas that have no labeled output slot, has not achieved C-24.
- **Pass condition**: Every required labeled field in the output template (including at minimum the disproof condition field required by C-20) has a corresponding item in the pre-artifact checklist, and every checklist item targeting a required output element maps to a named labeled field in the template. Orphaned checklist items (items with no corresponding labeled field) and orphaned labeled fields (fields with no corresponding checklist item) each fail C-24. The pairing need not be one-to-one if a single checklist item covers multiple fields, provided each field is verifiably addressed.

### C-25 -- Checklist Extension Preserves Binary-Verifiability: Each New Item Is Independently Audited
- **Weight**: aspirational
- **Category**: behavior
- **Text**: When a pre-artifact checklist is extended to cover additional requirements -- new labeled fields, inherited design axes, added structural gates -- each new item must independently satisfy C-22's locate-and-find standard before being added. C-22 fires on the output property of the assembled checklist (is every item binary-verifiable?); C-25 fires on the per-item design discipline that produces or fails to produce a C-22-compliant checklist. V-01's 14-item checklist failed C-22 because item 10 tested adequacy ("Will `**Disproof condition**:` name a specific observable condition?") rather than presence ("Does `**Disproof condition**:` appear?"). The editorial item was introduced by extending a structural checklist with an item that mixed presence verification and quality aspiration. C-22's pass condition is total: one editorial item disqualifies the entire checklist regardless of how many binary-verifiable items accompany it. C-25 requires the author to separate the structural gate (is the field present?) from the quality aspiration (is the content specific?) and put only the structural gate in the checklist. An item that "almost" qualifies as binary-verifiable -- that tests a structural property but phrases it as a quality question -- still disqualifies the checklist for C-22 purposes, and still fails C-25 at item-addition time.
- **Pass condition**: Each item added to the checklist during any extension pass can be answered by locating a named element in the template -- a field label, a required instruction, a named structural property. Items that ask whether a field's content will meet a quality standard do not pass C-25, even if the underlying field is required and the quality aspiration is legitimate. The per-item audit must precede inclusion; a checklist assembled without independent item-level auditing does not satisfy C-25 even if the assembled checklist happens to pass C-22.

### C-26 -- Labeled Fields Introduced by Each Design Axis Are Registered in the Checklist at Incorporation Time
- **Weight**: aspirational
- **Category**: behavior
- **Text**: When a template incorporates a new design axis -- inheriting labeled fields from a different design pattern, a different variation, or a different structural source -- the checklist must be updated to cover those fields as a required step at the moment of incorporation. C-24 requires complete pairing between checklist items and labeled fields; C-26 requires the practice that produces complete pairing in multi-axis templates. V-05 combined labeled fields from two design axes (falsifiability-centered structure from V-01; inertia-framing fields `**Baseline distance**:`, `**Prior position**:`, `**Signals establish**:` from V-02) but its checklist was built against only the first. All three fields from the second axis were systematically orphaned -- not because individual fields were overlooked, but because the entire second axis was never registered. C-24 catches the resulting gap at rubric-application time; C-26 fires on the design-time practice: the failure to treat checklist updating as a required step when a new design axis is incorporated, rather than as a retrospective audit. The design rule: every labeled field has an originating design axis, and incorporating a new axis obligates an immediate checklist update covering every labeled field that axis introduces.
- **Pass condition**: Every design axis present in the template has a corresponding checklist registration sweep that added binary-verifiable items for each labeled field introduced by that axis. A checklist that covers the primary design axis completely but omits a secondary axis fails C-26 even if C-24 would identify the same gap. The criterion fires on process (was a registration sweep performed for each axis?) as much as on outcome (are all fields covered?). A template author who performs a full coverage audit retrospectively and adds all missing items satisfies C-24 but not C-26, unless the retrospective audit is structured as an axis-by-axis registration sweep.

### C-27 -- Binary-Verifiable Complete Coverage Is a Single Design Property, Not Two Independent Optimizations
- **Weight**: aspirational
- **Category**: behavior
- **Text**: C-22 (every checklist item is a locate-and-find operation) and C-24 (every labeled field has a checklist item, every checklist item maps to a labeled field) must be satisfied by the same checklist design, not by independent optimizations applied to different parts of the checklist. R6 produced no variation satisfying both simultaneously: V-01 achieved C-24 through a minimal labeled-field set but failed C-22 on one editorial item; V-05 achieved C-22 through fully binary-verifiable items but failed C-24 on three inherited orphaned fields. Each variation optimized one property while making a design choice that precluded the other. C-27 fires on the compound design requirement: a template cannot satisfy C-27 by satisfying C-22 and C-24 through separate design moves that happen to coexist -- it must achieve both through a single design procedure in which the two properties are not in tension. The procedure that guarantees this: for each required labeled field in the template's complete inventory (covering all design axes), write exactly one checklist item that verifies the field's presence by locating its label string. Applied uniformly, this procedure simultaneously produces locate-and-find items (satisfying C-22) and complete field coverage (satisfying C-24). A checklist designed by any other method -- auditing item form first then checking coverage, or achieving coverage first then auditing item form -- risks the compositional failure R6 demonstrated, because each optimization pass can introduce violations of the property the other pass achieved.
- **Pass condition**: The checklist satisfies both C-22 and C-24, and the design procedure used to produce the checklist treats labeled fields as the primary unit -- one presence-verification item per required labeled field, derived from a single pass over the complete template field inventory. A checklist that satisfies C-22 and C-24 as measured outcomes but was produced by separate optimization passes does not satisfy C-27 if the author cannot demonstrate that the two properties were achieved without tradeoff.

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
- Aspirational: 10 pts total across C-08--C-27, 0.5 pts per criterion (10/20). Partial credit allowed.
