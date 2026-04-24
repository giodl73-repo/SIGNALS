Written to `simulations/quest/variations/topic-story-variations-R4-2026-03-14.md`.

---

## Five Variations — Round 4 Summary

| # | Axis | Target | Hypothesis |
|---|------|--------|------------|
| **V-01** | Lifecycle — failure mode label per section | C-16 | R3 V-04 had named operations but no failure modes. Adding an explicit named failure mode per section makes C-16's pass condition self-auditable at write-time without requiring C-17/C-18 mechanisms. Clean isolate. |
| **V-02** | Phrasing register — dedicated anti-neutral directive inside collapse-risk sections | C-17 | The documented collapse pattern: strong editorial synthesis → uncertainty hedges → recommendation retreats to passive framing. A required scan directive embedded *within* sections 4 and 5 ("if you find yourself writing X, you have hedged, not accounted — revise") fires at the point of collapse, not in headers or preamble. Tests C-17 independently of failure mode labels. |
| **V-03** | Inertia framing — per-finding binary check replacing framing | C-18 | R3 V-01 passed C-10 via a decision filter at the section header — a framing instruction. C-18 requires a per-item operation: the author applies yes/no to each finding before writing it. V-03 replaces the framing with an explicit yes/no check with different instructions for each case, applied before writing, not after. |
| **V-04** | Lifecycle + phrasing register — failure modes (including neutral-drift labels) + per-finding binary check | C-16 + C-17 test + C-18 | C-17 accepts "a failure-mode label for neutral-register drift" as a qualifying enforcement element. V-04 provides failure modes per section where sections 4 and 5 explicitly name hedging/neutral-reporting as the wrong operation — testing whether a well-targeted failure mode satisfies C-17 without a separate directive. Also adds per-finding check (C-18). |
| **V-05** | Full compound — R3 V-05 base + all three new mechanisms | C-16 + C-17 + C-18 | R3 V-05 scored 100 on C-08–C-15. V-05 R4 adds: failure mode per section (C-16), dedicated anti-neutral in both collapse-risk sections separate from failure modes (C-17), per-finding binary check (C-18). If the three mechanisms are structurally additive, this is the golden candidate. |

**Key design decisions:**

- **V-04 is the C-17 discriminator.** If V-04's failure modes (naming neutral-drift specifically) satisfy C-17, then V-02's separate directive is redundant. If V-04 gets PARTIAL on C-17, C-17 requires a standalone instruction — not just a named failure mode. The R3 scorecard (V-02 R3 passed C-14 via failure modes; V-01 R3 got PARTIAL C-11 with only header labels) predicts V-04 will likely score PARTIAL, since a failure mode label is not the same as an enforcement mechanism the author is required to run as a scan step.

- **V-05's Section 5 closing sentence** explicitly echoes the Section 3 "This claim fails if" condition ("This call stands unless [condition] is shown to hold"), propagating the falsifiability thread into the verdict. This is the R3 V-05 defensibility-thread mechanism, preserved unchanged.

- **V-01 through V-03 are single-axis isolates.** If any criterion other than the targeted one scores higher in a single-axis variation than in R3 V-04, that reveals the mechanism was already partially present in the R3 base.
 clean.
- **V-02** uses R3 V-04's structure with anti-neutral directives embedded as required elements inside sections 4 and 5 — not at headers, not as closing reminders, but within the section text where the collapse risk occurs. The directive must appear before the author completes the section.
- **V-03** is surgical: the only change from R3 V-04 is in Section 2, where the per-signal decision filter is replaced with a yes/no binary check applied per finding. If C-18 passes in V-03 but not in R3 V-01, the distinction is the per-item operationalization vs. section-level framing.
- **V-04** targets the question: can a failure mode label for neutral-drift satisfy C-17, or does C-17 require a separate directive? The failure modes for sections 4 and 5 are written to name hedging/neutral-reporting specifically as the wrong operation.
- **V-05** is the full compound. If it scores below R3 V-05 on existing criteria, the regression isolates which new mechanism creates interference. If it scores 100 on C-16–C-18 with no regressions, R4 has its golden variation.

---

## V-01 — Section Failure Modes Named in Template

**Axis**: Lifecycle emphasis (failure mode label per section, no other changes from R3 V-04 base)
**Hypothesis**: C-16 requires each section to name the specific wrong cognitive operation the author performs when they misuse that section. R3 V-04 named operations per section but not failure modes — making architectural distinctness a judgment call the author cannot self-audit. Adding an explicit failure mode per section converts "what this section should do" into a checkable binary: did I do the operation or the failure mode? If failure mode labeling alone fires C-16, the mechanism is isolated and does not depend on C-17/C-18 mechanisms.

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
**Failure mode**: restating the topic name or investigation area rather than the specific decision gate — describing what we studied instead of what we needed to know before we could commit.

One to two sentences. "We needed to know whether [X] before we could responsibly decide whether to build `{topic}`." A reader who skips this section should miss something about the decision stakes, not just the topic name.

*Decision filter: does stating this question tell the reader what the verdict depends on?*

### Section 2 — Curate the Evidence

**Operation**: select one decision-relevant finding per signal, omitting the rest.
**Failure mode**: transcribing signal outputs — including detail the artifacts produced, rather than the finding that most advances or complicates the build/don't-build question. The wrong operation fills the section; the right operation empties it to what matters.

For each signal: one sentence. Decision-relevant only. Ask for each finding: does this change the build/don't-build calculus for `{topic}`? If yes, include it. If no — if the finding fills out the picture without affecting the verdict — say so in one sentence ("The [signal] signal's key finding does not bear on the build/don't-build question") and stop.

Detail that doesn't shift the verdict is not in this section. Brevity here is correctness, not compression.

### Section 3 — Name the Pattern

**Operation**: identify the cross-signal finding — the insight that requires all signals together to see — and explain the convergence causally.
**Failure mode**: describing that signals agree rather than explaining why they agree; treating convergence as confirmation rather than as a phenomenon requiring a causal account.

Step back from the curated evidence. What pattern emerges that no single signal contains? Name it. Then apply the falsifiability test before completing this section: a pattern statement that says "the signals align because the approach is sound" cannot be disproved — it is a confidence statement, not a causal claim. A genuine causal account names the specific mechanism, assumption, or structural condition that accounts for the convergence — specific enough that a reader can name what evidence would break it.

Interpretive voice throughout: "What's striking is..." / "The convergence is not coincidental — it reflects a structural fact about..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

**Pattern**: [one extractable sentence with falsifiable causal logic]

*Falsifiability check*: if someone wanted to argue against your conclusion, they would need to show that [specific condition] does not hold. Name that condition explicitly.

### Section 4 — Account for What's Open

**Operation**: inventory what the investigation did not resolve and connect each gap to the decision stakes.
**Failure mode**: expressing that more could be done, or naming areas of general uncertainty, without identifying what is specifically unresolved and why it matters to the verdict — the difference between "there is uncertainty around X" (a topic) and "we do not know whether X exceeds threshold Y, and if it does not, the verdict changes to Z" (an account).

Name the specific gaps the investigation did not close. For each, state why it matters to the verdict and what a follow-on investigation would do to close it.

Required form: "We do not know [X]. If X is false, the recommendation changes to [Y]. It could be resolved by [specific method]."

*Decision filter: does each named uncertainty connect to the verdict? An uncertainty that wouldn't change the recommendation — even if resolved — is decision-neutral. Apply the filter: omit it or explicitly state its stakes.*

At least one named gap with decision stakes attached.

### Section 5 — Advocate for the Verdict

**Operation**: issue the verdict and defend the specific choice against the adjacent alternative — connecting the causal account in Section 3 to the action implied by it.
**Failure mode**: stating a verdict with reasons that could apply to any verdict of the same type — "the evidence supports proceeding" rather than "the evidence forces this verdict rather than the adjacent alternative because the pattern identified [specific causal mechanism] implies [specific implication that only proceed satisfies]."

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern — the rationale cites the pattern, not individual signals. Defend the specific verdict: why this one rather than the adjacent alternative? Specify the immediate next action. Recommend as someone who will be held accountable for the call.

Do not retreat to neutral language. "Given the evidence, I recommend [verdict] — specifically [action], because [the pattern named in Section 3 implies it]."

---

*Before writing the artifact — four checks:*

*— Does the failure mode label in each section name a specific wrong cognitive operation — not "being too vague" but the actual wrong thing the section can do? A generic failure mode does not satisfy C-16.*

*— Does the decision filter appear explicitly in at least two non-synthesis sections? (Sections 2 and 4 have labeled forms. Did both apply the filter — or only acknowledge it?)*

*— Does the pattern section name a specific, empirically checkable disproof condition?*

*— Can each section be identified by its operation alone? If a section sounds like it is performing a different section's operation, it has performed its failure mode — revise before writing.*

---

## V-02 — Anti-Neutral Instructions Inside Collapse-Risk Sections

**Axis**: Phrasing register (dedicated anti-neutral enforcement directive inside uncertainty and recommendation sections, no failure mode labels)
**Hypothesis**: C-17 requires each collapse-risk section to carry its own enforcement mechanism for register collapse, not to inherit voice anchoring from the synthesis section or from document-level preamble. The documented failure pattern is: strong editorial synthesis followed by the uncertainty section hedging into "more data may help" and the recommendation retreating to passive framing. An inline directive inside each collapse-risk section — placed where the collapse risk occurs, before the section's closing sentences — breaks this pattern by making neutral-register drift explicitly named and checkoutable at write-time. If V-02 scores higher on C-17 than R3 V-04 (which had operation labels but no collapse-risk-specific directives), the per-section directive is the mechanism.

---

The question is not whether to learn more about `{topic}`. The question is whether to build it. The signals you gathered either justify that commitment, or they counsel against it. This story makes the case — or closes it.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

For each signal, ask: does this finding change whether `{topic}` should be built? If yes, it belongs. If it adds texture without affecting the verdict, omit it.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

Each section below has a named operation. Read the operation before writing the section. A section that sounds like it is performing a different section's operation has not completed its job.

---

### Section 1 — Stake the Question

**Operation**: establish the build/don't-build question this investigation was designed to answer.

One to two sentences. "We needed to know whether [X] before we could responsibly decide whether to build `{topic}`." A reader who skips this section should miss something about the decision stakes.

*Decision filter: does stating this question tell the reader what the verdict depends on?*

### Section 2 — Curate the Evidence

**Operation**: select one decision-relevant finding per signal, omitting the rest.

For each signal: one sentence. Decision-relevant only. Ask for each finding: does this change the build/don't-build calculus for `{topic}`? If yes, include it. If no, say so in one sentence and stop.

Detail that doesn't shift the verdict is not in this section. Brevity here is correctness, not compression.

### Section 3 — Name the Pattern

**Operation**: identify the cross-signal finding and explain it causally.

Step back from the curated evidence. What pattern emerges that no single signal contains? Name it. Apply the falsifiability test: name the specific mechanism, assumption, or structural condition that accounts for the convergence, and name what would break it. A pattern statement that says "the signals align because the approach is sound" cannot be disproved — revise until the causal account is specific enough to name its own disproof condition.

Interpretive voice throughout: "What's striking is..." / "The convergence is not coincidental — it reflects..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

**Pattern**: [one extractable sentence with falsifiable causal logic]

*Falsifiability check*: if someone wanted to argue against your conclusion, they would need to show that [specific condition] does not hold. Name that condition explicitly.

### Section 4 — Account for What's Open

**Operation**: inventory what the investigation left unresolved, connected to the decision stakes.

Name the specific gaps the investigation did not close. For each, state why it matters to the verdict and what a follow-on investigation would need to close it.

Required form: "We do not know [X]. If X is false, the recommendation changes to [Y]. It could be resolved by [specific method]."

**Anti-neutral directive — required**: Before completing this section, scan every sentence. If you find any of the following, you have written a hedge rather than an account and must revise:
- "More data may be needed on [X]"
- "This area warrants further investigation"
- "There is uncertainty around [X]" (without stating what changes if it resolves)
- Any sentence that names a topic of uncertainty without naming a verdict consequence

A hedge names a topic. An account names a gap, its decision stakes, and a method to close it. No sentence that names uncertainty without a stated verdict consequence survives this section.

*Decision filter: does each named uncertainty connect to the verdict?*

At least one named gap with decision stakes attached.

### Section 5 — Advocate for the Verdict

**Operation**: issue the verdict and defend the specific choice against the adjacent alternative.

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern — the rationale cites the pattern, not individual signals. Defend the specific verdict: why this one rather than the adjacent alternative? Specify the immediate next action. Recommend as someone who will be held accountable for the call.

**Anti-neutral directive — required**: Before completing this section, scan every sentence. If you find any of the following, you have filed a report rather than made a call and must revise:
- "Based on the available evidence, it would be reasonable to..."
- "The team should consider..."
- "It may be worth..."
- Any passive or hedge-qualified framing of the verdict

The recommendation section issues a verdict, a rationale that names the pattern, a defense of the specific choice against the adjacent alternative, and an immediate next action. First person. Named accountability. "I recommend [verdict] — specifically [action], because [the pattern named in Section 3 forces it, not the adjacent alternative]."

---

*Before writing the artifact — four checks:*

*— Does the anti-neutral directive appear inside Section 4 and inside Section 5 — not just in headers, not just in closing reminders, but as a required element within the section text where collapse risk is highest?*

*— Does the decision filter appear explicitly in at least two non-synthesis sections?*

*— Does the pattern section name a specific, empirically checkable disproof condition?*

*— Does the anti-neutral directive in each collapse-risk section name specific hedge language to scan for — not "avoid being vague" but named patterns the author can detect and remove?*

---

## V-03 — Per-Finding Binary Check in Signal Findings

**Axis**: Inertia framing (per-finding binary check replacing section-level framing in signal findings section)
**Hypothesis**: C-18 requires a per-item decision filter expressed as an answerable question, where the criterion is the build-or-not decision. R3 V-01 passed C-10 via a decision filter applied at the section header ("does this change whether to build {topic}?") — but this is a framing instruction, not a per-item check. The difference is operational: a section-level framing instruction tells the author what orientation to hold while writing; a per-finding binary check requires the author to apply a yes/no test to each finding individually before writing it, with explicit instruction for both the yes and no case. V-03 isolates this mechanism: the only change from the R3 V-04 base is in Section 2, where the framing-level filter is replaced with a named yes/no check applied once per finding.

---

The question is not whether to learn more about `{topic}`. The question is whether to build it. The signals you gathered either justify that commitment, or they counsel against it. This story makes the case — or closes it.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

Each section below has a named operation. Read the operation before writing the section.

---

### Section 1 — Stake the Question

**Operation**: establish the build/don't-build question this investigation was designed to answer.

One to two sentences. "We needed to know whether [X] before we could responsibly decide whether to build `{topic}`." A reader who skips this section should miss something about the decision stakes.

*Decision filter: does stating this question tell the reader what the verdict depends on?*

### Section 2 — Curate the Evidence

**Operation**: select one decision-relevant finding per signal, applying a per-finding binary check before writing each entry.

For each signal, apply this check before writing: **Does this finding change whether to build `{topic}`? Yes or No.**

- **Yes**: Write the finding in one sentence — the specific finding that shifts or confirms the build decision, written with editorial judgment ("The feasibility signal established that X — which removes the primary technical risk" not "The feasibility signal found X").
- **No**: Write exactly: "The [signal-name] signal's key finding does not change the build/don't-build question." Stop. Do not add detail, context, or qualification.

The check must be applied to every finding before it is written. An entry that appears in this section without passing the check has been transcribed, not curated. Do not apply the check after writing — apply it before.

### Section 3 — Name the Pattern

**Operation**: identify the cross-signal finding and explain it causally.

Step back from the curated evidence. What pattern emerges that no single signal contains? Name it. Apply the falsifiability test: name the specific mechanism, assumption, or structural condition that accounts for the convergence. A pattern statement that says "the signals align because the approach is sound" cannot be disproved — revise until you can name what would break it.

Interpretive voice throughout: "What's striking is..." / "The convergence is not coincidental — it reflects..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

**Pattern**: [one extractable sentence with falsifiable causal logic]

*Falsifiability check*: if someone wanted to argue against your conclusion, they would need to show that [specific condition] does not hold. Name that condition explicitly.

### Section 4 — Account for What's Open

**Operation**: inventory what the investigation left unresolved, connected to the decision stakes.

Name the specific gaps the investigation did not close. For each, state why it matters to the verdict and what a follow-on investigation would need to close it.

Required form: "We do not know [X]. If X is false, the recommendation changes to [Y]. It could be resolved by [specific method]."

*Decision filter: does each named uncertainty connect to the verdict? An uncertainty that wouldn't change the recommendation is decision-neutral.*

At least one named gap with decision stakes attached.

### Section 5 — Advocate for the Verdict

**Operation**: issue the verdict and defend the specific choice against the adjacent alternative.

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern. Defend the specific verdict: why this one rather than the adjacent alternative? Specify the immediate next action.

Do not retreat to neutral language. "Given the evidence, I recommend [verdict] — specifically [action], because [the pattern named in Section 3 implies it]."

---

*Before writing the artifact — four checks:*

*— Did the yes/no binary check appear in the author's process for each finding in Section 2 — before writing, not after? Any entry that was written without a yes answer to "does this change whether to build `{topic}`?" has not been curated.*

*— Is the no-case handled explicitly — a single sentence that names the signal and states the finding does not change the build question? Not "this signal was inconclusive" but "the [signal] finding does not change the build/don't-build question."*

*— Does the decision filter appear explicitly in at least two non-synthesis sections?*

*— Does the pattern section name a specific, empirically checkable disproof condition?*

---

## V-04 — Failure Modes Including Neutral-Drift Labels + Decision Filters

**Axis**: Lifecycle emphasis + phrasing register (failure modes per section, where collapse-risk sections explicitly name neutral-drift as their failure mode — no separate anti-neutral directive)
**Hypothesis**: C-17's pass condition explicitly accepts "a failure-mode label for neutral-register drift" as a qualifying enforcement element. If the failure mode for the uncertainty section specifically names hedging as the wrong operation ("expressing uncertainty without verdict consequence — writing 'more may be needed' rather than naming what changes and how"), and the failure mode for the recommendation section specifically names neutral reporting as the wrong operation ("filing a report rather than making a call — listing reasons rather than defending the specific verdict against the adjacent alternative"), then the failure mode label satisfies C-17 without a separate anti-neutral directive. V-04 tests this: failure modes per section (C-16), collapse-risk failure modes targeting neutral-drift specifically (testing C-17 via the failure-mode-label route), and per-finding binary check (C-18). If C-17 scores PASS, failure mode labeling is sufficient and V-02's separate directive is redundant. If C-17 scores PARTIAL, C-17 requires a standalone enforcement instruction beyond naming the failure mode.

---

The question is not whether to learn more about `{topic}`. The question is whether to build it. The signals you gathered either justify that commitment, or they counsel against it. This story makes the case — or closes it.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

For each signal, ask: does this finding change whether `{topic}` should be built? If yes, it belongs. If it adds texture without affecting the verdict, omit it.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

Each section has a named operation and a named failure mode — the specific wrong cognitive operation the author performs when they misuse that section. Read both before writing.

---

### Section 1 — Stake the Question

**Operation**: establish the build/don't-build question this investigation was designed to answer.
**Failure mode**: restating the topic or area of investigation rather than the specific decision gate — "We investigated whether `{topic}` was feasible" (topic restatement) vs. "We needed to know whether X before we could responsibly commit to building `{topic}`" (decision gate).

One to two sentences. Write it as the question the verdict depends on. A reader who skips this section should miss something about the stakes.

*Decision filter: does stating this question anchor the reader in what would change the verdict?*

### Section 2 — Curate the Evidence

**Operation**: select one decision-relevant finding per signal by applying a per-finding binary check.
**Failure mode**: transcribing signal outputs — including what the signals produced, rather than what the build decision needs. The wrong operation documents; the right operation decides.

For each signal, apply this check before writing: **Does this finding change whether to build `{topic}`? Yes or No.**

- **Yes**: one sentence — the finding that shifts the build decision, in your own interpretive language.
- **No**: one sentence — "The [signal] signal's key finding does not change the build/don't-build question." Stop.

Every entry in this section exists because it passed the yes/no check. No entry appears here because it was interesting or detailed.

### Section 3 — Name the Pattern

**Operation**: identify the cross-signal finding and explain the convergence causally — the insight that requires all signals together to see.
**Failure mode**: describing that signals agree rather than explaining why — treating convergence as evidence of correctness rather than as a phenomenon that requires a causal account with a named mechanism.

Step back from the curated evidence. What pattern emerges that no single signal contains? Name it. Apply the falsifiability test: name the specific mechanism, assumption, or structural condition that accounts for the convergence — specific enough that a reader can name what would break it.

Interpretive voice throughout: "What's striking is..." / "The convergence is not coincidental — it reflects..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

**Pattern**: [one extractable sentence with falsifiable causal logic]

*Falsifiability check*: if someone wanted to disprove this, they would need to show that [specific condition] does not hold. Name that condition explicitly before continuing.

### Section 4 — Account for What's Open

**Operation**: inventory what the investigation left unresolved and connect each gap to the decision stakes.
**Failure mode**: hedging without verdict consequence — expressing that more could be done, or naming topics of uncertainty, without identifying what specifically changes in the verdict if the uncertainty resolves. Writing "there is uncertainty around adoption rates" names a topic; writing "we do not know whether adoption exceeds 20% in the SMB segment, and if it does not, the market case for `{topic}` fails at current resource levels" names an account.

Required form: "We do not know [X]. If X is false, the recommendation changes to [Y]. It could be resolved by [specific method]."

*Decision filter: does each named uncertainty connect to the verdict? An uncertainty that wouldn't change the recommendation is decision-neutral — state it as such or omit it.*

At least one named gap with verdict-consequence attached.

### Section 5 — Advocate for the Verdict

**Operation**: issue the verdict and defend the specific choice against the adjacent alternative, grounding the defense in the causal account from Section 3.
**Failure mode**: filing a report rather than making a call — stating reasons and a verdict without defending the specific verdict against the adjacent alternative ("proceed rather than pause because X"), or retreating to passive epistemic framing ("it seems reasonable to," "the evidence supports," "based on the available data").

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern. Defend the specific verdict: why this one rather than the neighboring option? What would have to be different for the verdict to be pause rather than proceed, or abandon rather than pivot? Specify the immediate next action.

"Given the evidence, I recommend [verdict] — specifically [action], because [the pattern named in Section 3] forces this verdict rather than [adjacent alternative]."

---

*Before writing the artifact — five checks:*

*1. Failure modes: does every section have a named failure mode that specifies the wrong cognitive operation, not a generic quality complaint ("too vague," "too long")?*

*2. Collapse-risk failure modes: do the failure modes for Sections 4 and 5 explicitly name hedging / neutral reporting as the wrong operation — not just "being vague" but the specific failure pattern?*

*3. Per-finding binary check: did the yes/no check appear before each entry in Section 2 was written?*

*4. Decision filter: does it appear explicitly in at least two non-synthesis sections?*

*5. Pattern disproof condition: is it specific and empirically checkable — not "if the data is wrong" but a named condition?*

---

## V-05 — Full Compound: R3 V-05 Base + All Three New Mechanisms

**Axis**: Role sequence + lifecycle emphasis + inertia framing + phrasing register (all)
**Hypothesis**: The R4 golden candidate. R3 V-05 scored 100 on C-08–C-15 via: named investigator role, audience pressure, per-section operations and stances, labeled decision filters at section headers, labeled artifact fields (Pattern + This claim depends on + This claim fails if), defensibility thread into recommendation. V-05 R4 adds three new mechanisms targeting the new criteria without modifying any existing mechanism: (a) failure mode per section in addition to operation + stance (C-16); (b) dedicated anti-neutral directive inside sections 4 and 5, separate from failure mode labels (C-17); (c) per-finding binary check in section 2 (C-18). If these mechanisms are structurally additive and non-competing, this variation extends the 100-point R3 score to C-16–C-18 without regression. If it scores below R3 V-05 on any criterion, the regression isolates which mechanism creates overhead.

---

You are the lead investigator for `{topic}`. You gathered the signals. Now you are writing the story — a single document that tells your team lead what to do.

Your team lead will read this once. They will make a decision. The default — before your investigation — was to not build `{topic}`. The signals either change that default or confirm it. Make the document worthy of the decision.

**Read in this order:**

1. **Strategy first.** Read `simulations/{topic}/strategy.md`. Note the investigation question. Hold it in mind while reading everything else.
2. **Signals second.** Glob and read all `simulations/**/{topic}-*` artifacts. For each, ask: what is the single finding that most changes or confirms my answer to the investigation question?
3. **Write the story.** Each section has a named operation, a named investigator stance, and a named failure mode. Read all three before writing the section.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

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

- **Yes**: write the finding in one sentence — the specific finding that shifts the build decision, written with the investigator's interpretive voice, not the signal artifact's language. "The feasibility signal settled the technical risk question — the API rate limits are not a blocker at current load" not "The feasibility signal found API rate limits within acceptable range."
- **No**: write exactly: "The [signal-name] signal's key finding does not change the build/don't-build question for `{topic}`." Stop. The entry is complete.

The check must be applied before writing, not after. A finding that appears in this section without a yes answer has been transcribed, not curated. Omission is explicit — a no-case entry names the signal and states the negative result.

*Decision filter applied: any finding that does not change the verdict is stated as decision-neutral. Omission is explicit, not silent.*

### Section 3 — Name the Pattern

**Operation**: identify the cross-signal finding — the insight that requires all signals together to see — and account for the convergence causally, with the disproof condition named as a labeled artifact field.
**Your stance**: the analyst who sees what the evidence, taken together, forces — not the narrator summarizing what was found.
**Failure mode**: describing that signals agree rather than explaining why — convergence stated as confidence ("the signals all point in a positive direction") rather than as a causal claim with a named mechanism and a named disproof condition.

Step back from the curated findings. What shape does this evidence take? What appears when you read the signals together that no single signal contains? Name the pattern. Then explain the convergence — not "the signals agree" but "the signals agree because [specific structural reason]."

Apply the falsifiability test before completing this section. A causal claim that cannot be disproved is not a causal claim — it is a confidence statement. A genuine causal account names the specific mechanism, assumption, or structural condition that, if shown false, would break the pattern.

After writing the synthesis, write the following labeled fields as part of the artifact:

**Pattern**: [one extractable sentence — the emergent finding and its causal basis]

**This claim depends on**: [the specific assumption or structural condition the pattern rests on]

**This claim fails if**: [a specific, empirically checkable condition — not "if the data is wrong" but the named condition that would invalidate the pattern]

Interpretive voice throughout: "What's striking is..." / "The convergence is not coincidental — it reflects a specific constraint that all signals assumed..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

### Section 4 — Account for Limits

**Operation**: inventory what the investigation left open and connect each gap to the decision stakes.
**Your stance**: the honest investigator who is still responsible for the question and has an opinion about which uncertainty is most consequential.
**Failure mode**: hedging without verdict consequence — expressing that more could be done, or naming areas of general uncertainty, without identifying what specifically changes in the verdict if the uncertainty resolves.

Name what the investigation did not resolve. You know these gaps — you ran the investigation. Account for each one explicitly.

Required form: "We do not know [X]. This matters because if X is false, the verdict changes to [Y]. A follow-on investigation could resolve it by [specific method]."

**Anti-neutral directive — required for this section**: Before completing Section 4, scan every sentence. If you find any of the following, you have hedged rather than accounted — revise before continuing:
- "More data may be needed on [X]"
- "This area warrants further investigation"
- "There is uncertainty around [X]" without a stated verdict consequence
- Any sentence that names a topic of uncertainty without naming what changes in the verdict if it resolves

A hedge names a topic. An account names a gap, its decision stakes, and a method to close it. Do not hedge into vagueness — you have an opinion about which uncertainty is most consequential. Name it.

*Decision filter applied: does each named uncertainty connect to the verdict? An uncertainty that wouldn't change the recommendation is decision-neutral — state it as such or omit it.*

### Section 5 — Advocate for the Verdict

**Operation**: issue the verdict and defend the specific choice, connecting the causal account to the action it implies — and naming what would reverse it.
**Your stance**: the investigator who will be held accountable for the call.
**Failure mode**: filing a report rather than making a call — listing reasons and a verdict without defending the specific verdict against the adjacent alternative, or retreating to passive epistemic framing that gives the team lead room to not act.

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern — the rationale cites the pattern's causal account, not individual signals. Defend the specific choice: why this verdict rather than the adjacent alternative? The mechanism named in Section 3 grounds this: the verdict follows because [reason invoking the specific mechanism or condition].

Specify the immediate next action: the person, team, or gate that moves as a result of this verdict.

**Anti-neutral directive — required for this section**: Before completing Section 5, scan every sentence. If you find any of the following, you have filed a report rather than made a call — revise before continuing:
- "Based on the available evidence, it would be reasonable to..."
- "The team should consider..."
- "It may be worth..."
- Any passive or hedge-qualified framing that gives the reader the option to not act

The recommendation section issues a verdict, defends it against the adjacent alternative, specifies an immediate action, and names what would reverse it. First person. Named accountability.

"Given the evidence, I recommend [verdict] — specifically [action], because the pattern identified in Section 3 [causal account] forces this verdict rather than [adjacent alternative]. This call stands unless [**This claim fails if** condition from Section 3] is shown to hold."

---

*Before writing the artifact — six checks:*

*1. Failure modes: does every section have a named failure mode specifying the wrong cognitive operation — not a generic quality complaint but the actual wrong thing the section can do?*

*2. Collapse-risk anti-neutral: does the anti-neutral directive appear inside Section 4 and inside Section 5, as a required scan step before the section is completed — not in a header label, not in a closing reminder, but within the section text?*

*3. Per-finding binary check: did the yes/no check appear before each entry in Section 2 was written? Are all no-case entries explicit one-sentence negations?*

*4. Labeled artifact fields: do "This claim depends on" and "This claim fails if" appear in the written artifact as labeled fields in Section 3?*

*5. Decision filter document-wide: does the build/don't-build filter appear explicitly in at least two non-synthesis sections? (Sections 2 and 4 both have labeled forms. Did both apply — not just acknowledge?)*

*6. Defensibility thread: does the recommendation section's closing sentence explicitly echo the "This claim fails if" condition from Section 3 — making the falsifiability self-check load-bearing in the verdict, not confined to synthesis?*

*Final test: would a skeptic who reads only this document know what the signals say, what specifically would change the verdict, what happens next, and exactly what evidence would reverse the call? If yes, write the artifact.*
