## Round 5 Scoring Complete

**Scorecard**: `simulations/quest/scorecards/simulate-derivation-scorecard-R5-2026-03-20.md`

---

### Results Summary

| Rank | Variation | Score | Band | Basis |
|------|-----------|-------|------|-------|
| 1 | **V-05** | 160/160 | Exemplary | All three principles in pre-Phase-1 preamble; cross-principle governance; Phase 4 cites preamble |
| 2 | **V-04** | 160/160 | Exemplary | Gate + ordering principles phase-local; safe fallback |
| 3 | **V-02** | 160/160 | Exemplary | Label principle + extended axis labels; strongest C-21 encoding |
| 4 | **V-01** | 160/160 | Exemplary | Gate principle only; C-20 robustness |
| 5 | **V-03** | 160/160 | Exemplary | Ordering principle with WHY; C-22 robustness |

**The R5 finding**: All five variations score 160/160 -- the v5 rubric ceiling. This is expected and correct. V-05-R4 already satisfied C-20/21/22 by having the correct text in the right template locations; all R5 variations inherit that structure and add principle declarations without removing anything scored. The v5 rubric's binary PASS/FAIL criteria cannot distinguish "pattern enforced by template text" from "pattern declared as a first-principles principle."

**Meta-finding**: The R5 improvements live above the rubric's measurement plane. They change how an LLM reasons about gate construction and label quality in novel contexts -- but no v5 criterion captures this. The improvements are real; the rubric just can't see them at this resolution.

**Three R6 candidates** emerge from V-05's architecture:
- C-23: Structural principles declared in a pre-phase preamble (not only at first-use sites)
- C-24: Application sites explicitly name their governing preamble principle (cross-reference present)
- C-25: When multiple principles are co-located, at least one is evaluable against another

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["pre-phase preamble compliance model: all structural principles declared before Phase 1 so the LLM builds its compliance model from named invariants before generating any output -- an LLM encountering a novel gate mid-execution has the principle already active, not recalled from a phase-local template", "cross-principle governance: co-located principles can be applied to each other -- the label principle prompts checking whether 'SOUND BLOCKED' satisfies the label quality test; the gate principle prompts checking whether the ordering rule would name a blocked verdict if formulated as a gate", "application-site principle anchoring: each gate or ordering rule at its application site explicitly names its governing preamble principle ('per the ordering principle in Structural Commitments'), making the declaration-to-application chain auditable in a single pass"]}
```
 fault present in the register." Inherited from V-05-R4 by all five variations.

**C-08 evidence** (all): V-05-R4 added explicit naming requirements inside the type definitions: "the Justification cell must name the algebraic rule, identity, or substitution... A step with an unexplained jump may not be labeled EXACT" (EXACT) and "the Justification cell must state the physical assumption being encoded" (PHYSICAL). All R5 variations inherit these expanded type definitions unchanged.

| Recommended subtotal | V-01: 30/30 | V-02: 30/30 | V-03: 30/30 | V-04: 30/30 | V-05: 30/30 |

---

### Aspirational Criteria (70 pts)

#### C-09 through C-19 (inherited from V-05-R4)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Catches fault not in paper | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-10 | Expands compressed steps | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-11 | APPROX verified independently (prose) | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-12 | Severity labels inline in Amend fixes | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-13 | Verification blocks contain prose reasoning | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-14 | APPROX reasoning independent of source | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-15 | All axes stack without phase-dropping | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-16 | Prose density uniform across block types | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-17 | APPROX gate has mandatory recovery | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-18 | Axis-commitment gateway gates Phase 2 entry | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-19 | Amend fixes ordered by severity (P1 first) | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |

**C-09**: Phase 2 source acknowledgment block + Phase 3 "NEW: not acknowledged by paper" tagging -- pipeline complete in all variations (inherited).

**C-10**: Phase 1b expansion pass with S-NNa/S-NNb and "(interpolated)" label; auto-pass note if no compressed steps. Inherited.

**C-11**: APPROX check requires (a) "in the tracer's own words -- do not merely quote the paper" and (b) domain-regime grounding. Inherited.

**C-12**: Amend template states "[F-ID] [P1/P2/P3]: [specific fix]" -- severity label is inline at the point of recommended action. Inherited.

**C-13**: Reasoning rule in Phase 2 -- "Every verdict token must be followed by a dash and at least one sentence of reasoning." Inherited.

**C-14**: Source-removal test present with domain-principle grounding requirement. Inherited.

**C-15**: Gateway table commits all three axes before Phase 2; interpolated sub-steps must have verification blocks; prose rule applies throughout. Inherited.

**C-16**: Density uniformity rule in Phase 2 -- "prose density must be uniform across the APPROX sub-block and the three primary checks... Mixed density within a single step block fails this rule." Inherited.

**C-17**: "SOUND BLOCKED for this step. You must replace (b)... A SOUND verdict may not be recorded for this APPROX block while (b) remains a paraphrase of the source." Consequence named; prohibition unconditional. Inherited.

**C-18**: Three-row gateway table (ACTIVE/ABSENT per axis A/B/C) with gate "Do NOT proceed to Phase 2 until all present axes show ACTIVE." Axis C labeled "NEW-tagged fault detection" (V-01/V-03/V-04) or "NEW-tagged fault detection for unacknowledged errors" (V-02/V-05). Both forms satisfy C-18's pass condition. All pass.

**C-19**: Unconditional severity ordering rule "P1 fixes first, then P2 fixes, then P3 fixes. The first fix is always the highest-severity fault present in the register. When the register contains faults at multiple severity levels, no lower-severity fix may precede a higher-severity fix in the list." Inherited.

#### C-20 through C-22 (new R5 aspirational criteria)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-20 | Mandatory gates name the prohibited action explicitly | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-21 | Gateway axis labels name exact mechanistic behaviors | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| C-22 | Ordering rules stated as unconditional enumeration | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |

**C-20 evidence** (all):
- APPROX gate: "SOUND BLOCKED for this step... A SOUND verdict may not be recorded for this APPROX block while (b) remains a paraphrase of the source." Both accepted forms present ("SOUND BLOCKED" and "may not be recorded while [condition] remains"). PASS.
- Phase 1b gate: "Do NOT proceed to Phase 2 until all present axes show ACTIVE." Names the downstream action (Phase 2 entry) explicitly. PASS.
- **Principle quality difference**: V-01/V-04/V-05 add a named gate principle ("Every mandatory gate in this skill names the verdict token that is blocked until compliance -- not merely the corrective action required") which makes the invariant self-verifiable in novel contexts. V-02/V-03 satisfy C-20 by template text alone. C-20 passes in all five but robustness differs.

**C-21 evidence** (all):
- V-01/V-03/V-04: Axis C labeled "NEW-tagged fault detection" -- specific enough that only the exact tagging operation satisfies it. PASS.
- V-02/V-05: Axis C labeled "NEW-tagged fault detection for unacknowledged errors" -- adds the exact condition ("unacknowledged") making compliance test even more precise. Both also add axis A extended to "Interpolated sub-step expansion with S-NNa/S-NNb labeling" (names the exact format) and axis B to "Prose-per-check reasoning in all verification blocks" (names the exact application scope). Stronger but criterion PASS in all cases.
- **Principle quality difference**: V-02/V-05 add the axis-label distinguishing test as a named principle ("Could a different, non-compliant behavior satisfy this label by reasonable reading?") -- the LLM can apply this to any label it writes, not just copy the examples. V-01/V-03/V-04 satisfy C-21 by label text alone.

**C-22 evidence** (all):
- All variations have "P1 fixes first, then P2 fixes, then P3 fixes. The first fix is always the highest-severity fault present in the register. When the register contains faults at multiple severity levels, no lower-severity fix may precede a higher-severity fix in the list." This is a single unconditional enumeration naming all three tiers. PASS.
- **Principle quality difference**: V-03/V-04/V-05 add the WHY: "A conditional chain ('if P1 faults exist, fix P1 first; if no P1 but P2 exist, fix P2 first') states the top tier leads but leaves all subordinate-tier ordering implicit -- an Amend with P2 and P3 faults can satisfy the conditional form while placing a P3 fix before a P2 fix." The LLM can now self-verify whether its own ordering rule has hidden conditional reasoning. V-01/V-02 satisfy C-22 by sentence form alone.

| Aspirational subtotal | V-01: 70/70 | V-02: 70/70 | V-03: 70/70 | V-04: 70/70 | V-05: 70/70 |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 | 60/60 | 30/30 | 70/70 | **160/160** | Exemplary |
| V-02 | 60/60 | 30/30 | 70/70 | **160/160** | Exemplary |
| V-03 | 60/60 | 30/30 | 70/70 | **160/160** | Exemplary |
| V-04 | 60/60 | 30/30 | 70/70 | **160/160** | Exemplary |
| V-05 | 60/60 | 30/30 | 70/70 | **160/160** | Exemplary |

**The R5 result**: All five variations score 160/160. This is the expected outcome. V-05-R4 already satisfied C-20/21/22 by having the correct text in the correct template locations. All R5 variations inherit that structure and add principle declarations without removing any scored element. The v5 rubric's binary PASS/FAIL criteria cannot distinguish between a pattern enforced by template text alone vs. a pattern declared as a first-principles principle -- both pass the same criterion. The rubric ceiling is reached and held.

**What this means**: The R5 improvements are structural robustness improvements that live above the rubric's measurement plane. They change how an LLM in a novel context would reason about gate construction, label quality, and ordering rules -- but no v5 criterion captures this. The new patterns from R5/V-05 are candidates for R6 rubric criteria.

---

## Rankings

Since all five variations score 160/160, ranking is by first-principles robustness quality of C-20/21/22 encoding:

| Rank | Variation | Score | Band | Principle coverage |
|------|-----------|-------|------|-------------------|
| 1 | **V-05** | 160/160 | Exemplary | All three principles in pre-Phase-1 preamble; cross-principle governance; Phase 4 cites preamble by name |
| 2 | **V-04** | 160/160 | Exemplary | Gate principle (Phase 2) + ordering principle (Phase 4); two of three; phase-local positions; safe fallback |
| 3 | **V-02** | 160/160 | Exemplary | Label principle + extended axis labels; strongest C-21 encoding; no gate or ordering principle |
| 4 | **V-01** | 160/160 | Exemplary | Gate principle (Phase 2 preamble) only; minimal change; C-20 robustness |
| 5 | **V-03** | 160/160 | Exemplary | Ordering principle with WHY (Phase 4 only); minimal change; C-22 robustness |

**Ranking basis**: V-05 is ranked first because it encodes all three principles where the LLM reads them before generating any phase output -- the compliance model is built from principles, not from template examples encountered during output generation. V-04 is second because it covers two of three principles without the preamble's cognitive-load risk. V-02 ranks third because extended axis labels add lasting clarity to C-21 even in a single-axis change. V-01 and V-03 are near-equal minimal changes.

---

## Excellence Signals from V-05

**1. Pre-phase preamble builds the compliance model before output begins**
The `## STRUCTURAL COMMITMENTS` block appears before Phase 1, so the LLM reads all three principles before generating any table, any verification block, or any fix. This is architecturally different from embedding each principle at the phase where it first applies (V-01/V-02/V-03 approach): the LLM's compliance model is holistic from the start, not assembled incrementally as it reads each phase. An LLM encountering a novel gate context mid-execution has no principle to recall if the principle was never declared upfront; one that read the preamble has the invariant already active.

**2. Cross-principle governance: principles can be applied to each other**
When all three principles are co-located, each can be checked against the others. The label principle ("could a non-compliant behavior satisfy this label?") prompts the LLM to check whether "SOUND BLOCKED" -- the gate's verdict label -- satisfies the label quality test. The gate principle ("names the verdict token that is blocked") prompts the LLM to verify that the ordering rule itself, if formulated as a gate, would name the blocked verdict. Single-phase embedding does not enable this cross-checking; only co-location does.

**3. Application-site principle anchoring: Phase 4 cross-references the preamble**
The Phase 4 severity ordering rule reads: "Severity ordering rule (unconditional enumeration per the ordering principle in Structural Commitments):" -- this names the governing principle at the point of application. An LLM reading the ordering rule also reads the pointer back to the declaration, making the connection auditable in a single pass. The pattern is: declare in the preamble, apply in the phase, cross-reference at application site.

**4. Single-pass auditability of all structural commitments**
An evaluator (or the LLM self-checking its output) can verify all three structural commitments by reading the preamble alone. No phase-scanning required to find the gate principle, label principle, and ordering principle. This is valuable both for human review and for LLM self-verification at the start of a new derivation.

---

## Meta-Finding: R5 Improvements Exceed Rubric Resolution

The R5 quest exposed a ceiling effect: when C-20/21/22 were designed as R4 patterns and their pass conditions capture the presence of correct text, any variation that preserves that text passes -- regardless of whether the pattern is declared as a named principle or merely embedded in a template. The rubric cannot distinguish "the LLM will follow this pattern because the template text demonstrates it" from "the LLM will follow this pattern because the principle is declared and the LLM can self-verify compliance."

**Implication for R6**: Three potential new rubric criteria emerge from V-05's innovations:

| Candidate | What it detects |
|-----------|----------------|
| C-23 | Structural principles declared in a pre-phase preamble, not only at first-use sites |
| C-24 | At least one application site explicitly names its governing preamble principle (cross-reference present) |
| C-25 | When multiple structural principles are present, at least one principle is evaluable against another (cross-principle testability) |

These three would raise the ceiling from 160 to 175 (3 × 5 pts) and force R6 variations to demonstrate principled architecture, not merely correct template text.

---

## Recommendation

**Ship V-05 as the R5 skill.** It is the only variation that delivers all three first-principles encoding improvements simultaneously and achieves single-pass auditability of all structural commitments.

**Fallback**: If the `## STRUCTURAL COMMITMENTS` preamble adds cognitive load that compresses Phase 1 or Phase 2 on long derivations, use **V-04** (gate + ordering principles in phase-local positions, no preamble, identical rubric score). V-04 encodes C-20 and C-22 robustly; C-21's label quality is maintained by the inherited extended axis labels from V-05-R4.

**Do not ship V-01, V-02, or V-03 alone.** Each addresses only one of three principles. V-01 and V-03 are solid minimal additions but leave two of three principles as template-only patterns. V-02 is the weakest standalone choice (label principle covers only C-21; gate and ordering remain template-only).

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["pre-phase preamble compliance model: all structural principles declared before Phase 1 so the LLM builds its compliance model from named invariants before generating any output -- an LLM encountering a novel gate mid-execution has the principle already active, not recalled from a phase-local template", "cross-principle governance: co-located principles can be applied to each other -- the label principle prompts checking whether 'SOUND BLOCKED' satisfies the label quality test; the gate principle prompts checking whether the ordering rule would name a blocked verdict if formulated as a gate", "application-site principle anchoring: each gate or ordering rule at its application site explicitly names its governing preamble principle ('per the ordering principle in Structural Commitments'), making the declaration-to-application chain auditable in a single pass"]}
```
