`topic-story-variations-R5-2026-03-14.md` written.

---

## Round 5 — Five Variations

| # | Axis | Target | Mechanism |
|---|------|--------|-----------|
| **V-01** | Lifecycle — numbered checklist before sections | C-19 | R4 V-04 base + 12-item numbered pre-artifact checklist moved *before* section instructions, aggregating requirements from C-10 through C-18 |
| **V-02** | Output format — required labeled field | C-20 | R4 V-01 base + `**Disproof condition**: [The claim fails if X.]` as a required labeled field in Section 3, structurally parallel to `**Pattern**:` |
| **V-03** | Phrasing register — verbatim strings in failure modes | C-21 | R4 V-04 base + verbatim forbidden pattern lists embedded in the failure mode descriptions for Sections 4 and 5 (no standalone anti-neutral directive) |
| **V-04** | Lifecycle + phrasing register | C-19 + C-21 | R4 V-04 base + numbered checklist (C-19) + verbatim strings in failure modes (C-21) combined |
| **V-05** | Full compound | C-19 + C-20 + C-21 | R4 V-05 base (100/18) + 14-item numbered checklist pre-sections + `**Disproof condition**:` as fourth Section 3 labeled field + verbatim strings in existing anti-neutral directives |

**Key discriminators for scoring:**

**C-19** fires on *position + numbering + comprehensiveness*. R4 V-04's five checks were numbered but appeared after the section instructions — review gate, not pre-writing gate. V-01 moves the checklist before all sections and expands it to 12 items covering every structural requirement. The question: does the checklist's position (pre vs. post) satisfy C-19, or does completeness alone matter?

**C-20** fires on *labeled field structure*. R4 V-01 had a prose falsifiability instruction; C-20 requires `**Disproof condition**: [...]` as a locatable labeled element. V-02 is the clean isolate — the only change from R4 V-01 is adding that one labeled field. If C-20 passes in V-02 and scored lower in R4 V-01, the label is the mechanism.

**C-21** fires on *verbatim scannable strings*. V-03 embeds them in failure mode descriptions rather than standalone directives — testing whether C-17 + verbatim strings = C-21 satisfaction. V-02 in R4 already had verbatim strings in its *standalone directive*; V-03 tests whether the same strings in a *failure mode description* produce the same result.

**V-05's `**Disproof condition**:`** is added as a *fourth* labeled field alongside the existing three (Pattern, This claim depends on, This claim fails if) — conservative extension, no existing mechanism replaced. The Section 5 defensibility thread echoes `**Disproof condition**` rather than `**This claim fails if**` to ensure the C-20 field is load-bearing in the artifact, not just present in the template.
cklist moved before all sections (C-19); (b) `**Disproof condition**:` labeled field added as a fourth required field in Section 3 (C-20); (c) verbatim forbidden pattern lists added inside the existing anti-neutral directives in Sections 4 and 5 (C-21). If the three additions are non-competing, this scores 100 on all 21 criteria. |

**Key design decisions:**

- **V-01 is the C-19 isolate.** The distinguishing factor from R4 V-04 is position (pre vs. post) and completeness (12 items covering C-10 through C-18 vs. 5 targeted checks). C-19 specifically fires on whether structural requirements are aggregated into an active pre-writing gate. R4 V-04's post-template numbered checks are visible only after reading the sections — making them a review step, not a verification prerequisite.

- **V-02 is the C-20 isolate.** The base (R4 V-01) has prose falsifiability enforcement but no labeled field. V-02 adds exactly one labeled field: `**Disproof condition**: [...]`. C-20 fires on template structure — whether the field is required. The rubric's C-15/C-20 distinction is: C-15 = run the check in the open (any form); C-20 = required labeled field (locatable by label scan, not by reading body text).

- **V-03 is the C-21 isolate.** C-21 requires "at least two verbatim hedge patterns the author can recognize and reject." R4 V-04's failure modes describe the wrong operation but don't list the actual strings. V-03 embeds the strings in the failure mode description, testing whether failure modes with verbatim examples satisfy C-21 without a standalone anti-neutral directive. This answers whether C-17 + verbatim strings = C-21 satisfaction.

- **V-05's `**Disproof condition**:` field** is added as a fourth labeled field in Section 3 alongside the R4 V-05 fields (Pattern, This claim depends on, This claim fails if). The conservative extension: it adds rather than replaces, preserving all R4 V-05 mechanisms. The Section 5 defensibility thread echoes `**Disproof condition**` instead of `**This claim fails if**` — the field that is C-20's canonical artifact element.

---

## V-01 — Numbered Pre-Artifact Checklist

**Axis**: Lifecycle emphasis (numbered checklist before section instructions, aggregating all structural requirements)
**Target**: C-19
**Hypothesis**: C-19 fires on two properties: (1) the checklist is numbered and (2) it aggregates all structural requirements into an active pre-writing gate — not a post-template review. R4 V-04 had five numbered post-template checks visible only after the author read the sections. C-19 requires the checklist to appear before section instructions, converting it from a review step into a prerequisite. V-01 takes R4 V-04 as base (passes C-16, C-17, C-18) and adds only the pre-artifact checklist. Single-axis isolate.

---

The question is not whether to learn more about `{topic}`. The question is whether to build it. The signals you gathered either justify that commitment, or they counsel against it. This story makes the case — or closes it.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

**NUMBERED PRE-ARTIFACT CHECKLIST**

Complete every item before reading the section instructions below. An unchecked item is a structural gap — plan how you will satisfy it. If an item cannot be satisfied from the signals you read, note what is missing before proceeding.

1. [ ] I can state the single decision gate this investigation was designed to resolve — not the topic name, the specific condition needed before committing to build
2. [ ] For each signal, I have identified one finding (not a summary) that changes the build/don't-build question
3. [ ] The build/don't-build filter will be applied per finding in Section 2: only findings that answer Yes to "does this change the verdict?" will appear; others will be stated as decision-neutral
4. [ ] The build/don't-build filter will appear explicitly in at least two non-synthesis sections — both Section 2 and Section 4 carry it
5. [ ] I can state the pattern in one sentence — the cross-signal finding no single signal contains
6. [ ] The pattern is falsifiable: I can name the specific empirically checkable condition that would break it
7. [ ] Each of the five sections will perform a distinct analytical operation: stake the question / curate evidence / name the pattern / account for limits / advocate for a verdict — not variations of the same operation
8. [ ] Section 2 will apply a per-finding yes/no check before writing each entry, not after
9. [ ] Section 4 will carry an anti-neutral enforcement mechanism inside the section — not inherited from Section 3, not at the section header only
10. [ ] Section 5 will carry an anti-neutral enforcement mechanism inside the section — not inherited from Section 3, not at the section header only
11. [ ] Every section will have a named failure mode that names the specific wrong cognitive operation, not a generic quality complaint
12. [ ] Section 3 will contain labeled artifact fields including a named disproof condition

Only proceed to the section instructions below when all 12 items are checked.

---

Each section below has a named operation and a named failure mode. Read both before writing. A section that performs its failure mode has failed regardless of prose quality.

---

### Section 1 — Stake the Question

**Operation**: establish the build/don't-build question this investigation was designed to answer.
**Failure mode**: restating the topic name or investigation area rather than the specific decision gate — "We investigated whether `{topic}` was feasible" (topic restatement) vs. "We needed to know whether X before we could responsibly commit to building `{topic}`" (decision gate).

One to two sentences. Write it as a decision gate. A reader who skips this section should miss something about the decision stakes.

*Decision filter: does stating this question anchor the reader in what the verdict depends on?*

### Section 2 — Curate the Evidence

**Operation**: select one decision-relevant finding per signal by applying a per-finding binary check.
**Failure mode**: transcribing signal outputs — including what the signals produced rather than what the build decision needs. The wrong operation documents; the right operation decides.

For each signal, apply this check before writing: **Does this finding change whether to build `{topic}`? Yes or No.**

- **Yes**: one sentence — the finding that shifts the build decision, in your interpretive language. "The feasibility signal settled the technical risk question — X is not a blocker" not "The feasibility signal found X within acceptable range."
- **No**: one sentence — "The [signal] signal's key finding does not change the build/don't-build question." Stop.

Every entry exists because it passed the check. No entry appears because it was interesting.

*Decision filter applied: any finding that does not change the verdict is stated as decision-neutral.*

### Section 3 — Name the Pattern

**Operation**: identify the cross-signal finding and explain the convergence causally.
**Failure mode**: describing that signals agree rather than explaining why — treating convergence as evidence of correctness rather than as a phenomenon requiring a causal account with a named mechanism.

What pattern emerges that no single signal contains? Name it. Apply the falsifiability test: the causal account must name the specific mechanism or structural condition that, if shown false, would break the pattern. "The signals align because the approach is sound" cannot be disproved.

After writing the synthesis, write the following labeled fields:

**Pattern**: [one extractable sentence with falsifiable causal logic]

**This claim depends on**: [the specific assumption or structural condition the pattern rests on]

**This claim fails if**: [a specific, empirically checkable condition that would invalidate the pattern]

Interpretive voice throughout: "What's striking is..." / "The convergence is not coincidental — it reflects..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

### Section 4 — Account for What's Open

**Operation**: inventory what the investigation left open and connect each gap to the decision stakes.
**Failure mode**: hedging without verdict consequence — expressing that more could be done, or naming topics of uncertainty, without identifying what specifically changes in the verdict if the uncertainty resolves. Writing "there is uncertainty around adoption" names a topic; naming an account requires specifying what changes in the verdict if it resolves adversely.

Required form: "We do not know [X]. If X is false, the recommendation changes to [Y]. It could be resolved by [specific method]."

**Anti-neutral directive — required for this section**: Before completing Section 4, scan every sentence. If a sentence names uncertainty without naming a verdict consequence, it is a hedge, not an account — revise before continuing.

*Decision filter applied: does each named uncertainty connect to the verdict?*

At least one named gap with verdict-consequence attached.

### Section 5 — Advocate for the Verdict

**Operation**: issue the verdict and defend the specific choice against the adjacent alternative.
**Failure mode**: filing a report rather than making a call — listing reasons and a verdict without defending the specific verdict against the adjacent alternative, or retreating to passive framing ("it seems reasonable to," "the evidence supports," "based on the available data") that gives the reader room to not act.

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern. Defend the specific choice: why this verdict rather than the adjacent alternative? Specify the immediate next action. Recommend as someone who will be held accountable.

**Anti-neutral directive — required for this section**: Before completing Section 5, scan every sentence. If a sentence gives the team lead room to not act, it has not made a call — revise before continuing.

"Given the evidence, I recommend [verdict] — specifically [action], because [the pattern named in Section 3] forces this verdict rather than [adjacent alternative]."

---

## V-02 — `**Disproof condition**:` as Required Labeled Artifact Field

**Axis**: Output format (required labeled field in Section 3's structured block)
**Target**: C-20
**Hypothesis**: C-20 fires on template structure: does the template require a labeled `**Disproof condition**:` field in the output, or only instruct the author to name a disproof condition somewhere in prose? R4 V-01 has a falsifiability check as an embedded instruction ("Name that condition explicitly") — this produces the condition in prose, variable in placement, not locatable by label. V-02 takes R4 V-01 as base and adds exactly one element: `**Disproof condition**: [The claim fails if X.]` as a required labeled field parallel to `**Pattern**: [...]`. Single-axis isolate: if C-20 passes in V-02 and scored lower in R4 V-01, the labeled field is the mechanism, not the prose content.

---

The question is not whether to learn more about `{topic}`. The question is whether to build it. The signals you gathered either justify that commitment, or they counsel against it. This story makes the case — or closes it.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

For each signal, ask: does this finding change whether `{topic}` should be built? If yes, it belongs. If it adds texture without affecting the verdict, omit it.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

Each section below has a named operation and a named failure mode. Read both before writing. A section that performs its failure mode rather than its operation has failed regardless of how well it is written.

---

### Section 1 — Stake the Question

**Operation**: establish the build/don't-build question this investigation was designed to answer.
**Failure mode**: restating the topic name or investigation area rather than the specific decision gate — describing what was studied instead of what was needed before committing.

One to two sentences. "We needed to know whether [X] before we could responsibly decide whether to build `{topic}`." A reader who skips this section should miss something about the decision stakes, not just the topic name.

*Decision filter: does stating this question tell the reader what the verdict depends on?*

### Section 2 — Curate the Evidence

**Operation**: select one decision-relevant finding per signal, omitting the rest.
**Failure mode**: transcribing signal outputs — including the detail the artifacts produced rather than the finding that most advances the build/don't-build question. The wrong operation fills the section; the right operation empties it to what matters.

For each signal: one sentence. Decision-relevant only. Ask for each finding: does this change the build/don't-build calculus for `{topic}`? If yes, include it. If no — say so in one sentence ("The [signal] signal's key finding does not bear on the build/don't-build question") and stop.

*Decision filter: does each finding change the build/don't-build question?*

### Section 3 — Name the Pattern

**Operation**: identify the cross-signal finding — the insight that requires all signals together to see — and explain the convergence causally.
**Failure mode**: describing that signals agree rather than explaining why they agree; treating convergence as confirmation rather than as a phenomenon requiring a causal account.

What pattern emerges that no single signal contains? Name it. Apply the falsifiability test: a pattern statement that says "the signals align because the approach is sound" cannot be disproved. A genuine causal account names the specific mechanism, assumption, or structural condition that accounts for the convergence — specific enough that a reader can name what evidence would break it.

After writing the synthesis, write the following labeled fields. All three are required and must appear exactly as labeled in the artifact:

**Pattern**: [one extractable sentence with falsifiable causal logic]

**This claim depends on**: [the specific assumption or structural condition the pattern rests on]

**Disproof condition**: [The claim fails if X. Name the specific observable condition that would show this pattern is wrong.]

The `**Disproof condition**:` field is a required artifact element — not optional prose, not a sentence embedded in the body text. A Section 3 that discusses falsifiability without a labeled `**Disproof condition**:` field is structurally incomplete, regardless of whether a disproof condition appears in the prose.

Interpretive voice throughout: "What's striking is..." / "The convergence is not coincidental — it reflects..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

*Falsifiability check: if someone wanted to argue against your conclusion, they would need to show that [specific condition] does not hold. Name that condition in the `**Disproof condition**:` field explicitly — not in the body text.*

### Section 4 — Account for What's Open

**Operation**: inventory what the investigation left unresolved and connect each gap to the decision stakes.
**Failure mode**: expressing that more could be done, or naming areas of general uncertainty, without identifying what is specifically unresolved and why it matters to the verdict — the difference between "there is uncertainty around X" (a topic) and "we do not know whether X, and if it does not hold, the verdict changes to Y" (an account).

Name the specific gaps the investigation did not close. For each, state why it matters to the verdict.

Required form: "We do not know [X]. If X is false, the recommendation changes to [Y]. It could be resolved by [specific method]."

*Decision filter: does each named uncertainty connect to the verdict? An uncertainty that wouldn't change the recommendation is decision-neutral.*

At least one named gap with decision stakes attached.

### Section 5 — Advocate for the Verdict

**Operation**: issue the verdict and defend the specific choice against the adjacent alternative.
**Failure mode**: filing a report rather than making a call — stating a verdict with reasons that could apply to any verdict of the same type, without defending why this specific verdict rather than the adjacent one; or retreating to passive framing that reports rather than commits.

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern — the rationale cites the pattern, not individual signals. Defend the specific verdict: why this one rather than the adjacent alternative? Specify the immediate next action. Recommend as someone who will be held accountable for the call.

Do not retreat to neutral language. "Given the evidence, I recommend [verdict] — specifically [action], because [the pattern named in Section 3 implies it]."

---

*Before writing the artifact — four checks:*

*1. Does the `**Disproof condition**:` field appear in Section 3 as a labeled field — not embedded in prose, not as a rhetorical question, but as a field a reader can locate by scanning for the label?*

*2. Is the condition in `**Disproof condition**:` a specific observable condition — not "if the data is wrong" but a named empirically checkable state?*

*3. Does the decision filter appear explicitly in at least two non-synthesis sections?*

*4. Does every section have a named failure mode that names the specific wrong cognitive operation?*

---

## V-03 — Verbatim Forbidden Patterns in Failure Mode Descriptions

**Axis**: Phrasing register (verbatim forbidden pattern strings embedded in failure mode descriptions for collapse-risk sections)
**Target**: C-21
**Hypothesis**: C-21 requires anti-neutral directives to name at least two verbatim hedge patterns the author can recognize and reject. R4 V-04's failure modes for Sections 4 and 5 name neutral-drift as the wrong operation but describe it in general terms without listing the actual strings. V-03 tests whether verbatim pattern lists embedded in failure mode descriptions satisfy C-21, independently of whether a standalone anti-neutral directive is present. If V-03 passes C-21 and R4 V-04 did not, the verbatim strings are the mechanism, not the directive format. This also probes the C-17/C-21 independence question: C-17 requires a per-section enforcement mechanism; C-21 requires verbatim strings within that mechanism. Does a failure mode label with verbatim strings satisfy both simultaneously?

---

The question is not whether to learn more about `{topic}`. The question is whether to build it. The signals you gathered either justify that commitment, or they counsel against it. This story makes the case — or closes it.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

For each signal, ask: does this finding change whether `{topic}` should be built? If yes, it belongs. If it adds texture without affecting the verdict, omit it.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

Each section below has a named operation and a named failure mode. Read both before writing.

---

### Section 1 — Stake the Question

**Operation**: establish the build/don't-build question this investigation was designed to answer.
**Failure mode**: restating the topic or area of investigation rather than the specific decision gate — "We investigated whether `{topic}` was feasible" (topic restatement) vs. "We needed to know whether X before we could responsibly commit to building `{topic}`" (decision gate).

One to two sentences. Write it as the question the verdict depends on.

*Decision filter: does stating this question anchor the reader in what would change the verdict?*

### Section 2 — Curate the Evidence

**Operation**: select one decision-relevant finding per signal by applying a per-finding binary check.
**Failure mode**: transcribing signal outputs — including what the signals produced rather than what the build decision needs. The wrong operation documents; the right operation decides.

For each signal, apply this check before writing: **Does this finding change whether to build `{topic}`? Yes or No.**

- **Yes**: one sentence — the finding that shifts the build decision, in interpretive language.
- **No**: one sentence — "The [signal] signal's key finding does not change the build/don't-build question." Stop.

Every entry in this section exists because it passed the yes/no check.

### Section 3 — Name the Pattern

**Operation**: identify the cross-signal finding and explain the convergence causally.
**Failure mode**: describing that signals agree rather than explaining why — treating convergence as evidence of correctness rather than as a phenomenon requiring a causal account with a named mechanism.

What pattern emerges that no single signal contains? Name it. Apply the falsifiability test: name the specific mechanism that, if shown false, would break the pattern.

**Pattern**: [one extractable sentence with falsifiable causal logic]

*Falsifiability check*: if someone wanted to disprove this, they would need to show that [specific condition] does not hold. Name that condition explicitly.

### Section 4 — Account for What's Open

**Operation**: inventory what the investigation left open and connect each gap to the decision stakes.
**Failure mode**: hedging without verdict consequence — producing uncertainty output that would be equally true whether the evidence were strong or weak, because the author has named topics without naming decision consequences. The author recognizes this failure by finding any of the following strings in their draft before completing this section:
- "More data may be needed on X" — names a topic, omits what changes in the verdict
- "This area warrants further investigation" — defers without staking a consequence
- "There is some uncertainty around X" — acknowledges without specifying the verdict impact
- "Future research could explore X" — moves to a next investigation rather than accounting for this one

Any sentence matching these patterns is a hedge. Replace with the required form: "We do not know [X]. If X is false, the recommendation changes to [Y]. It could be resolved by [specific method]."

*Decision filter: does each named uncertainty connect to the verdict?*

### Section 5 — Advocate for the Verdict

**Operation**: issue the verdict and defend the specific choice against the adjacent alternative.
**Failure mode**: filing a report rather than making a call — retreating from the verdict into language that reports findings without defending a specific decision. The author recognizes this failure by finding any of the following strings in their draft before completing this section:
- "Based on the available evidence, it would be reasonable to..." — reports without committing to a verdict
- "The team should consider..." — delegates the decision to the reader
- "It may be worth exploring..." — hedges the verdict into one option among many
- "Given the above, a reasonable next step would be..." — frames the verdict as a suggestion rather than a call

Any sentence matching these patterns has not made a call. Replace with: "I recommend [verdict] — specifically [action], because [the pattern named in Section 3] forces this verdict rather than [adjacent alternative]."

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

---

*Before writing the artifact — four checks:*

*1. Failure modes: does every section have a named failure mode that names the specific wrong cognitive operation?*

*2. Verbatim patterns in collapse-risk sections: do the failure modes for Sections 4 and 5 name specific scannable strings the author can match against their draft?*

*3. Per-finding binary check: did the yes/no check appear before each entry in Section 2 was written?*

*4. Pattern disproof condition: is it specific and empirically checkable?*

---

## V-04 — Numbered Checklist + Verbatim Forbidden Patterns

**Axis**: Lifecycle emphasis + phrasing register (numbered pre-artifact checklist + verbatim forbidden pattern strings in collapse-risk failure modes)
**Target**: C-19 + C-21
**Hypothesis**: C-19 (checklist structure and position) and C-21 (verbatim strings in enforcement instructions) are orthogonal: C-19 fires on the pre-writing gate, C-21 fires on whether named strings are present in the anti-neutral directives for collapse-risk sections. They should be additive without structural competition. V-04 tests this combination on R4 V-04 as base (passes C-16, C-17, C-18). If both C-19 and C-21 pass without regression, the mechanisms are independent. If one scores PARTIAL, the combination creates overhead — isolating which mechanism is the source.

---

The question is not whether to learn more about `{topic}`. The question is whether to build it. The signals you gathered either justify that commitment, or they counsel against it. This story makes the case — or closes it.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

**NUMBERED PRE-ARTIFACT CHECKLIST**

Complete every item before reading the section instructions. If an item is not satisfiable, note the gap explicitly before proceeding.

1. [ ] I can state the specific decision gate this investigation was designed to resolve — not the topic, the condition
2. [ ] For each signal, I have one finding that changes the build/don't-build question — not a summary, not a list
3. [ ] The build/don't-build filter will be applied per finding in Section 2 (yes/no before writing each entry)
4. [ ] The build/don't-build filter appears in at least two non-synthesis sections — both Sections 2 and 4 carry it explicitly
5. [ ] I can state the pattern in one sentence — the cross-signal finding no single signal contains
6. [ ] The pattern is falsifiable: I can name the specific empirically checkable condition that would break it
7. [ ] Each of the five sections will perform a distinct operation: stake / curate / name / account / advocate — no two sections will perform the same operation
8. [ ] Every section will have a named failure mode that names the specific wrong cognitive operation
9. [ ] The failure mode for Section 4 will name verbatim hedge patterns the author can scan for — not just describe hedging
10. [ ] The failure mode for Section 5 will name verbatim neutral-reporting patterns the author can scan for
11. [ ] Section 3 will contain labeled artifact fields (Pattern + supporting conditions)
12. [ ] Section 5's reversal condition will connect to Section 3's disproof condition

Only proceed when all 12 items are checked.

---

Each section has a named operation and a named failure mode. Read both before writing.

---

### Section 1 — Stake the Question

**Operation**: establish the decision gate this investigation was designed to resolve.
**Failure mode**: restating what was studied rather than what was at stake — "We investigated feasibility" (topic) vs. "We needed to know whether X before we could responsibly commit to building `{topic}`" (decision gate).

One to two sentences. Write the decision gate. A reader who skips this section should miss something about the stakes.

*Decision filter: does this question anchor the reader in what the verdict depends on?*

### Section 2 — Curate the Evidence

**Operation**: select one decision-relevant finding per signal by applying a per-finding binary check.
**Failure mode**: transcribing signal outputs — documenting what the signals produced rather than deciding what the build question needs.

For each signal: **Does this finding change whether to build `{topic}`? Yes or No.**

- **Yes**: one sentence — the finding that shifts the build decision, in interpretive language.
- **No**: "The [signal] signal's key finding does not change the build/don't-build question." Stop.

*Decision filter applied: any finding that does not change the verdict is stated as decision-neutral.*

### Section 3 — Name the Pattern

**Operation**: identify the cross-signal finding and explain the convergence causally.
**Failure mode**: describing that signals agree rather than explaining why — convergence as confirmation rather than as a phenomenon requiring a causal account.

Name the pattern. Explain the causal mechanism — not "the signals agree" but the structural reason. Apply the falsifiability test before completing this section.

**Pattern**: [one extractable sentence with falsifiable causal logic]

**This claim depends on**: [the specific assumption or structural condition the pattern rests on]

**This claim fails if**: [a specific, empirically checkable condition that would invalidate the pattern]

Interpretive voice: "What's striking is..." / "The convergence reflects..." / "The evidence forces a conclusion I did not expect..."

### Section 4 — Account for What's Open

**Operation**: inventory what the investigation left open and connect each gap to the decision stakes.
**Failure mode**: hedging without verdict consequence — producing uncertainty statements that would be equally true whether the evidence were strong or weak. The author names topics instead of accounting for consequences. Before completing this section, scan your draft for these strings — any match is a hedge, not an account:
- "More data may be needed on X" — names a topic, omits the verdict consequence
- "This area warrants further investigation" — defers without naming a stake
- "There is some uncertainty around X" — acknowledges without specifying what changes
- "Future research could explore X" — defers to a next investigation rather than this one's account

Replace any flagged sentence with: "We do not know [X]. If X is false, the recommendation changes to [Y]. It could be resolved by [specific method]."

Required form: "We do not know [X]. If X is false, the recommendation changes to [Y]. It could be resolved by [specific method]."

*Decision filter applied: does each named uncertainty connect to the verdict?*

### Section 5 — Advocate for the Verdict

**Operation**: issue the verdict and defend the specific choice against the adjacent alternative.
**Failure mode**: filing a report rather than making a call — retreating from the verdict into language that reports findings without defending a specific decision. Before completing this section, scan your draft for these strings — any match has not made a call:
- "Based on the available evidence, it would be reasonable to..." — reports without committing
- "The team should consider..." — delegates the decision to the reader
- "It may be worth exploring..." — hedges the verdict into an option among options
- "Given the above, a reasonable next step would be..." — frames the verdict as a suggestion

Replace any flagged sentence with: "I recommend [verdict] — specifically [action], because [the pattern named in Section 3] forces this verdict rather than [adjacent alternative]. This call stands unless [This claim fails if condition from Section 3] is shown to hold."

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

---

## V-05 — Full Compound: R4 V-05 Base + C-19 + C-20 + C-21

**Axis**: Role sequence + lifecycle emphasis + output format + phrasing register (all)
**Target**: C-19 + C-20 + C-21 (extending R4 V-05's 100/18 score to 21/21)
**Hypothesis**: R4 V-05 scored 100 on C-08–C-18 via: named investigator role + audience pressure; per-section operation + stance + failure mode; per-finding binary check (C-18); anti-neutral directives with named hedge patterns inside Sections 4 and 5 (C-17); labeled artifact fields (C-15); defensibility thread into Section 5. V-05 R5 adds three non-interfering mechanisms: (a) 14-item numbered pre-artifact checklist moved before all sections (C-19); (b) `**Disproof condition**:` added as a fourth required labeled field in Section 3 (C-20); (c) verbatim forbidden pattern lists extended with an explicit scan directive inside the existing anti-neutral directives in Sections 4 and 5 (C-21). If the three additions are non-competing with the R4 V-05 architecture, this is the 21-criterion golden candidate.

---

You are the lead investigator for `{topic}`. You gathered the signals. Now you are writing the story — a single document that tells your team lead what to do.

Your team lead will read this once. They will make a decision. The default — before your investigation — was to not build `{topic}`. The signals either change that default or confirm it. Make the document worthy of the decision.

**Read in this order:**

1. **Strategy first.** Read `simulations/{topic}/strategy.md`. Note the investigation question. Hold it in mind while reading everything else.
2. **Signals second.** Glob and read all `simulations/**/{topic}-*` artifacts. For each, ask: what is the single finding that most changes or confirms my answer to the investigation question?
3. **Complete the pre-artifact checklist.** All 14 items must be checked before writing any section.
4. **Write the story.** Each section has a named operation, a named investigator stance, and a named failure mode. Read all three before writing the section.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

**NUMBERED PRE-ARTIFACT CHECKLIST**

Complete every item before writing any section. Mark each as checked, or note explicitly what is missing.

**Structure and operations:**
1. [ ] All five sections are plannable: stake the question / curate evidence / name the pattern / account for limits / advocate for the verdict
2. [ ] Each section will perform a distinct analytical operation — no two sections perform the same operation
3. [ ] Every section has a named failure mode that names the specific wrong cognitive operation, not a generic quality complaint

**Decision-orientation:**
4. [ ] For each signal, I have identified one finding that changes the build/don't-build question — not a summary
5. [ ] The per-finding binary check (Yes/No) will be applied before writing each entry in Section 2 — not after
6. [ ] The build/don't-build filter appears in at least two non-synthesis sections (Sections 2 and 4 both carry it explicitly)

**Falsifiability:**
7. [ ] The pattern is falsifiable: I can state the specific empirically checkable condition that would break it
8. [ ] The `**Disproof condition**:` labeled field is ready to appear in Section 3 as a required artifact element — not embedded in prose
9. [ ] Section 5's reversal condition will echo Section 3's `**Disproof condition**` — the defensibility thread is planned

**Register:**
10. [ ] Section 4's anti-neutral directive will name at least two verbatim hedge strings the author can scan for and remove
11. [ ] Section 5's anti-neutral directive will name at least two verbatim neutral-reporting strings the author can scan for and remove
12. [ ] Section 4 carries a dedicated anti-neutral directive as a required element inside the section text
13. [ ] Section 5 carries a dedicated anti-neutral directive as a required element inside the section text

**Final readiness:**
14. [ ] A skeptic who reads only this completed artifact will know: (a) what the signals say together, (b) what specifically would change the verdict, (c) what happens next, and (d) what evidence would show the call was wrong

Only proceed to the section instructions below when all 14 items are checked.

---

Each section performs a distinct analytical operation. These operations are not interchangeable — a section doing the wrong operation has failed regardless of how well it is written. The failure mode names the wrong operation precisely so you can self-audit before writing.

---

### Section 1 — Stake the Question

**Operation**: establish the decision this investigation was designed to resolve.
**Your stance**: the investigator who chose to run it and knows why it mattered.
**Failure mode**: restating what was studied rather than what was at stake — "We investigated feasibility" (topic) vs. "We needed to know whether X before we could responsibly commit to building `{topic}`" (decision gate).

Restate the investigation question from `strategy.md` in your own words — as someone who knew why it mattered. One to two sentences. Write it as a decision gate: "We needed to know whether [X] before we could responsibly commit to building `{topic}`." The weight of the question should be present in the language.

*Decision filter applied: does this question anchor the reader in what the verdict depends on?*

### Section 2 — Curate the Evidence

**Operation**: select one decision-relevant finding per signal by applying a per-finding binary check before each entry is written.
**Your stance**: the investigator distilling each signal to its sharpest decision-relevant point — not the reporter transcribing what each signal found.
**Failure mode**: transcribing outputs rather than exercising editorial judgment — including what the signal produced rather than what the build decision needs. The wrong operation documents; the right operation decides.

For each signal, apply this check before writing: **Does this finding change whether to build `{topic}`? Yes or No.**

- **Yes**: write the finding in one sentence — the specific finding that shifts the build decision, written with the investigator's interpretive voice, not the signal artifact's language. "The feasibility signal settled the technical risk question — X is not a blocker at current load" not "The feasibility signal found X within acceptable range."
- **No**: write exactly: "The [signal-name] signal's key finding does not change the build/don't-build question for `{topic}`." Stop. The entry is complete.

The check must be applied before writing, not after. A finding that appears without a yes answer has been transcribed, not curated. Omission is explicit — a no-case entry names the signal and states the negative result.

*Decision filter applied: any finding that does not change the verdict is stated as decision-neutral. Omission is explicit, not silent.*

### Section 3 — Name the Pattern

**Operation**: identify the cross-signal finding — the insight that requires all signals together to see — and account for the convergence causally, with the disproof condition named as a required labeled artifact field.
**Your stance**: the analyst who sees what the evidence, taken together, forces — not the narrator summarizing what was found.
**Failure mode**: describing that signals agree rather than explaining why — convergence stated as confidence ("the signals all point in a positive direction") rather than as a causal claim with a named mechanism and a required labeled disproof condition.

Step back from the curated findings. What shape does this evidence take? What appears when you read the signals together that no single signal contains? Name the pattern. Then explain the convergence — not "the signals agree" but "the signals agree because [specific structural reason]."

Apply the falsifiability test before completing this section. A causal claim that cannot be disproved is not a causal claim — it is a confidence statement. A genuine causal account names the specific mechanism, assumption, or structural condition that, if shown false, would break the pattern.

After writing the synthesis, write the following labeled fields as required elements of the artifact. All four must appear exactly as labeled:

**Pattern**: [one extractable sentence — the emergent finding and its causal basis]

**This claim depends on**: [the specific assumption or structural condition the pattern rests on]

**This claim fails if**: [a specific, empirically checkable condition — not "if the data is wrong" but the named condition that would invalidate the pattern]

**Disproof condition**: [The pattern breaks if X is shown to hold. This is a required labeled field — locatable by label scan, not embedded in the body text above.]

Interpretive voice throughout: "What's striking is..." / "The convergence is not coincidental — it reflects a specific constraint that all signals assumed..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

### Section 4 — Account for Limits

**Operation**: inventory what the investigation left open and connect each gap to the decision stakes.
**Your stance**: the honest investigator who is still responsible for the question and has an opinion about which uncertainty is most consequential.
**Failure mode**: hedging without verdict consequence — expressing that more could be done, or naming areas of general uncertainty, without identifying what specifically changes in the verdict if the uncertainty resolves. The author has named topics rather than accounted for consequences.

Name what the investigation did not resolve. You know these gaps — you ran the investigation. Account for each one explicitly.

Required form: "We do not know [X]. This matters because if X is false, the verdict changes to [Y]. A follow-on investigation could resolve it by [specific method]."

**Anti-neutral directive — required for this section**: Before completing Section 4, scan every sentence for the following strings. Any sentence containing these patterns is a hedge, not an account — revise before continuing:
- "More data may be needed on..." — names a topic without naming the verdict consequence
- "This area warrants further investigation" — defers without staking a consequence
- "There is uncertainty around..." (without a stated verdict consequence) — acknowledges without accounting
- "Future work could explore..." — moves to a next investigation rather than accounting for this one

A hedge names a topic. An account names a gap, its decision stakes, and a method to close it. Do not hedge into vagueness — you have an opinion about which uncertainty is most consequential. Name it.

*Decision filter applied: does each named uncertainty connect to the verdict? An uncertainty that wouldn't change the recommendation is decision-neutral — state it as such or omit it.*

### Section 5 — Advocate for the Verdict

**Operation**: issue the verdict and defend the specific choice, connecting the causal account to the action it implies — and naming what would reverse it.
**Your stance**: the investigator who will be held accountable for the call.
**Failure mode**: filing a report rather than making a call — listing reasons and a verdict without defending the specific verdict against the adjacent alternative, or retreating to passive epistemic framing that gives the team lead room to not act.

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern — the rationale cites the pattern's causal account, not individual signals. Defend the specific choice: why this verdict rather than the adjacent alternative? The mechanism named in Section 3 grounds this. Specify the immediate next action: the person, team, or gate that moves as a result of this verdict.

**Anti-neutral directive — required for this section**: Before completing Section 5, scan every sentence for the following strings. Any sentence containing these patterns has filed a report rather than made a call — revise before continuing:
- "Based on the available evidence, it would be reasonable to..." — reports without committing to a verdict
- "The team should consider..." — delegates the decision to the reader
- "It may be worth exploring..." — hedges the verdict into one option among many
- "Given the above, a reasonable next step would be..." — frames the call as a suggestion rather than a verdict
- "The evidence supports moving forward, though caution is advised" — qualifies the verdict out of accountability

The recommendation section issues a verdict, defends it against the adjacent alternative, specifies an immediate action, and names what would reverse it. First person. Named accountability.

"Given the evidence, I recommend [verdict] — specifically [action], because the pattern identified in Section 3 [causal account] forces this verdict rather than [adjacent alternative]. This call stands unless [**Disproof condition** from Section 3] is shown to hold."

---

*Before finalizing the artifact — six checks:*

*1. Failure modes: does every section have a named failure mode specifying the wrong cognitive operation — not a generic quality complaint but the actual wrong thing the section can do?*

*2. Anti-neutral directives: does the anti-neutral directive appear inside Section 4 and inside Section 5, as a required scan step before the section is completed — with named verbatim strings the author can match against their draft?*

*3. Per-finding binary check: did the yes/no check appear before each entry in Section 2 was written? Are all no-case entries explicit one-sentence negations?*

*4. Labeled artifact fields: do "This claim depends on," "This claim fails if," and "Disproof condition" appear in the written artifact as labeled fields in Section 3?*

*5. Decision filter document-wide: does the build/don't-build filter appear explicitly in at least two non-synthesis sections? (Sections 2 and 4 both have labeled forms. Did both apply — not just acknowledge?)*

*6. Defensibility thread: does the recommendation section's closing sentence explicitly echo the `**Disproof condition**` field from Section 3 — making the falsifiability self-check load-bearing in the verdict, not confined to synthesis?*

*Final test: would a skeptic who reads only this document know what the signals say, what specifically would change the verdict, what happens next, and exactly what evidence would reverse the call? If yes, write the artifact.*
