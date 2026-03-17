Written to `simulations/quest/variations/topic-story-variations-R3-2026-03-14.md`.

---

## Five Variations — Round 3 Summary

| # | Axis | Target Criteria | Hypothesis |
|---|------|-----------------|------------|
| **V-01** | Inertia framing — extended to non-synthesis sections | C-13 | Two labeled forms of the inertia test (decision form / defensibility form), each assigned to specific section headers, force the habit to appear throughout rather than only at signal selection and the pattern field. |
| **V-02** | Lifecycle emphasis — distinct cognitive operations | C-14 | Labeling each section's analytical operation *plus its failure mode* prevents uniform-register collapse. R2 named stances (personas); R3 names operations (what the section produces, not how it sounds). |
| **V-03** | Phrasing register — falsifiability as labeled output field | C-15 | Three required artifact fields ("This pattern depends on" / "A reader who wanted to disprove this would need to show" / "This claim fails if") appear in the written document, not the model's reasoning. Satisfies C-15 pass condition by construction. |
| **V-04** | Inertia framing + lifecycle emphasis | C-10 + C-11 + C-12 + C-13 + C-14 | R2 E-4 blueprint: V-04 R2's inertia+falsifiability frame combined with per-section stances upgraded to architecturally distinct operations. Tests whether the two independent R2 mechanisms are genuinely complementary. |
| **V-05** | Role + lifecycle + inertia + phrasing (compound) | C-10 + C-11 + C-12 + C-13 + C-14 + C-15 | Full R2 best-mechanism stack (investigator role, audience pressure, inertia frame, falsifiability inline, register check) plus all three new criteria mechanisms. Golden candidate for R3. |

**Key design decisions:**

- **V-01** is the pure C-13 isolate. The two-form labeling at the document opening and per-section application is the mechanism. Nothing else in V-01 targets R3 criteria — so if C-13 passes and C-14/C-15 don't, the mechanism works in isolation.
- **V-02** adds operation-plus-failure-mode pairs, which R2's persona labels lacked. The failure mode framing is the C-14 mechanism — it specifies what each section must *not* do, making stances architecturally distinct rather than tonally distinct.
- **V-03** is surgical: identical to a clean baseline except for the three-sentence self-check block as a labeled artifact field. Strong signal for C-15 if it passes; reveals that the instruction alone (R2 V-04) was insufficient if V-03 scores higher.
- **V-04** combines V-01 and V-02 mechanisms. Tests whether inertia framing suppresses or reinforces operational distinctness (the R3 analog of the R2 C-10/C-11 tension).
- **V-05** is the full compound. If it scores below V-04, the three-sentence self-check field creates friction — isolate and remove. If it scores below V-03, the investigator framing is suppressing the falsifiability ceremony.
es the inertia/defensibility habit visible in ≥2 non-synthesis sections. V-04 R2 applied the decision filter to signal selection and the falsifiability test to the pattern — neither appeared explicitly in the uncertainty or recommendation sections. If the prompt names the inertia test's two forms upfront and then labels which form governs each section header, the habit becomes structural document-wide rather than incidental to synthesis.

---

The default decision on `{topic}` is to not build it. Every signal you gathered either changed that calculus or confirmed it. This story is the argument.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal established.

**The inertia test has two forms. Both apply throughout this document:**

- **Decision form** — "Does this sentence change whether `{topic}` should be built?" If not, cut it.
- **Defensibility form** — "What specific evidence would disprove this claim?" If nothing specific, revise until you can name the condition.

Every substantive assertion in the artifact should survive one or both tests. The form applied varies by section — each section header identifies which.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

### What We Set Out to Understand

*Inertia test: decision form.*

The investigation question from `strategy.md`, stated as the decision it was meant to inform. One to two sentences: what did we need to know before we could responsibly decide whether to build `{topic}`? Write it as a decision gate — what was the default before this investigation, and what had to change to revisit it?

*Check: does stating this question tell the reader what the verdict depends on? If it reads like any investigation question about any topic, sharpen it.*

### What the Signals Revealed

*Inertia test: decision form.*

For each signal: one sentence. Decision-relevant only. Ask for each finding: does this change whether to build `{topic}`? If yes, include it. If the most important finding from a signal is neutral to the build decision, say so in one sentence and stop.

Omit detail that fills out the picture without affecting the verdict — regardless of how interesting it is. Completeness is not the goal. The goal is: what did each signal add or remove from the build/don't-build case?

### What the Signals Say Together

*Inertia test: defensibility form.*

Step back from individual signals. What pattern emerged? Name it. Then, before completing the synthesis, apply the defensibility test explicitly to the pattern claim:

> Write the pattern. Then complete this sentence: **"This claim does not hold if [specific empirical condition]."** If you cannot complete it with something specific and checkable, the pattern is not yet a causal claim — it is a description of convergence. Revise until you can name the disproof condition.

Write the synthesis from the position of someone who has committed to an interpretation. Interpretive voice throughout: "What's striking is..." / "The convergence is not accidental — it reflects..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

**Pattern**: [one extractable sentence with a falsifiable causal basis]

### What Remains Uncertain

*Inertia test: defensibility form.*

Name what the investigation did not resolve. Apply the defensibility form to each named uncertainty: what would confirm or disconfirm it, and if it turns out to be false, does the recommendation change?

Required form: "We do not know [X]. This matters because if X is false, the verdict changes to [Y]. A follow-on investigation could resolve it by [specific approach]."

"More data may help" does not name an uncertainty. Generic hedges fail the defensibility test — they cannot be disproved because they make no claim. At least one named gap with decision stakes attached.

### Recommendation

*Inertia test: decision form.*

**Verdict**: proceed / pause / pivot / abandon

Connect the verdict to the named pattern. Then apply the decision form: why does the pattern force this verdict rather than the adjacent alternative? What would have to be different for the verdict to be pause instead of proceed, or abandon instead of pivot?

Specify the immediate next action — not what could happen someday, but the concrete step that happens this week as a result of this verdict.

*Check: would a skeptic who read this section alone know both what the verdict is and exactly why the pattern forces it rather than an alternative?*

---

*Before writing the artifact: verify the inertia test appears explicitly in at least two non-synthesis sections. The uncertainty section and the recommendation section both have labeled forms above — did both apply the test, not just acknowledge it? A section that acknowledges the test in its header but then writes neutral prose has not passed C-13.*

---

## V-02 — Architecturally Distinct Section Operations

**Axis**: Lifecycle emphasis (per-section analytical function as distinct cognitive operation)
**Hypothesis**: C-14 requires stances that are analytically distinct — not just different tones but different cognitive operations. V-03 and V-05 R2 named persona labels ("honest accountant," "decision advocate") but the underlying cognitive mode was the same throughout: interpretive narrator. C-14's pass condition requires that stances "could not be confused with any other section's stance." Labeling the cognitive operation — what the section produces, not how it sounds — and naming the failure mode for each operation, makes section-level distinctness structural.

---

Synthesize all gathered signals for `{topic}` into a narrative artifact at `simulations/{topic}/{topic}-story-{date}.md`.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

Each section performs a distinct analytical operation. Read the operation label and its failure mode before writing the section. If the section sounds like it is doing what a different section does, it has not completed its operation.

---

### Section 1 — Contextualize the Stakes

**Operation: establish the decision that this investigation was designed to inform.**
**Failure mode: restating the topic rather than the decision gate.**

You are not summarizing `strategy.md`. You are establishing why this investigation was worth doing — what was uncertain before it ran, and what decision was waiting on it. One to two sentences. A reader who skips this section should miss something about the stakes, not just the topic name. The word "whether" should appear: "We needed to know whether [X] before we could decide whether to [Y]."

### Section 2 — Curate the Signals

**Operation: select one decision-relevant finding per signal.**
**Failure mode: transcribing signal outputs rather than exercising editorial judgment.**

You read all the artifacts. Most of what you read is not here — because most of it does not change what a decision-maker needs to know. For each signal: one sentence, the finding that most advances or complicates the investigation question. Curation means choosing, not reducing. If a signal's key finding is irrelevant to the decision, say so in one sentence ("The X signal's most important finding — [Y] — does not bear on the build/don't-build question") and stop.

The operation is explicit: you are deciding what a decision-maker needs to see, not documenting what the investigation produced.

### Section 3 — Name the Shape

**Operation: identify the pattern that emerges across signals — the finding that none of them states individually.**
**Failure mode: describing that signals agree rather than explaining why.**

You have the curated findings. Step back from them. What shape does this evidence take? What appears when you read the signals together that no single signal contains? Name the pattern. Then account for the convergence causally: what specific mechanism, assumption, or structural condition explains why the signals point this direction? A description of convergence ("three signals agree") is not a pattern. A causal account ("three signals agree because [specific condition X holds across all of them]") is.

Interpretive language throughout: "What's striking is..." / "The convergence reflects a structural fact about..." / "The evidence, taken together, forces a conclusion..."

**Pattern**: [one extractable sentence — the emergent finding and its causal basis]

### Section 4 — Account for Limits

**Operation: inventory what the investigation did not resolve and connect each gap to the decision stakes.**
**Failure mode: expressing that more could be done rather than naming what is specifically open.**

You are not hedging — you are accounting. The honest accountant names specific items the investigation left open, explains why each matters to the verdict, and identifies what would close each gap. "There is uncertainty around adoption rates" is hedging. "We do not know whether adoption exceeds 20% in the SMB segment — the signals only tested enterprise — and if it does not, the market case for `{topic}` does not hold at current resource levels" is accounting.

Required form: "We do not know [X]. This matters because if X is false, the verdict changes to [Y]. It could be resolved by [method]."

At least one named gap with decision stakes attached. The operation is explicit accounting, not probability assessment.

### Section 5 — Advocate for a Decision

**Operation: issue a verdict and defend the specific choice against the adjacent alternative.**
**Failure mode: stating a verdict without explaining why it rather than the neighboring option.**

You are not filing a report. You are making a call and you will stand behind it. Verdict: **proceed**, **pause**, **pivot**, or **abandon**. Connect the verdict to the named pattern — the rationale cites the pattern, not individual signals. Then defend the specific choice: why this verdict rather than the adjacent one (why proceed rather than pause, why pivot rather than abandon)? Specify the immediate next action: the person, team, or gate that moves as a result of this verdict.

---

*Before writing the artifact: can each section be identified by its operation alone, without reading the header? Section 2 curates; Section 3 names the shape; Section 4 accounts; Section 5 advocates. If any section sounds like it is performing the same operation as another section, it has not completed its operation — revise before writing.*

---

## V-03 — Falsifiability Self-Check as Labeled Artifact Field

**Axis**: Phrasing register (falsifiability ceremony — labeled output field, not embedded instruction)
**Hypothesis**: C-15 requires the author to run the falsifiability test visibly — as a labeled moment a reader can verify, not an instruction embedded in the section guidance. V-04 R2 embedded the falsifiability test as a negative example in the section instruction. V-02 R2 used a callout block before the section. Neither produced an explicit named self-check that appears in the output artifact. C-15's minimum viable form is "this claim fails if X." If the prompt requires this as a labeled output field — a written field in the document, not a thinking step — it will appear explicitly in every output and satisfy C-15's pass condition by construction.

---

Synthesize all gathered signals for `{topic}` into a narrative artifact at `simulations/{topic}/{topic}-story-{date}.md`.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

Write the four sections below. The synthesis section contains a **mandatory falsifiability self-check** that must appear in the artifact as a labeled output — not a thinking step, but a written field in the document.

---

### What We Set Out to Understand

The investigation question from `strategy.md`. One to two sentences: what did we need to learn, and what decision was it meant to inform? Write it as the question the signals were designed to answer.

### What the Signals Revealed

For each signal: one sentence, the single most decision-relevant finding. Selective, not exhaustive. The finding that most advances or complicates the investigation question — not a recap of the signal's output.

### What the Signals Say Together

Draw the cross-signal conclusion — the insight that requires all signals together to see. Name the pattern. Explain the convergence causally: what specific mechanism, assumption, or structural condition accounts for why the signals point this direction?

Take a position. Use interpretive language: "What's striking is..." / "The convergence points to a structural reason..." / "The signals together force a conclusion that no individual signal stated..."

**Pattern**: [one extractable sentence naming the emergent finding and its causal basis]

---

**Falsifiability self-check** — required artifact field. Write all three sentences before continuing:

> **This pattern depends on**: [the specific assumption or structural condition the claim rests on]
>
> **A reader who wanted to disprove this pattern would need to show**: [the specific evidence or finding that would break the claim]
>
> **This claim fails if**: [a specific, empirically checkable condition — not "if the data is wrong" but the named condition]

*Example (do not copy — write from your own pattern):*
> *This pattern depends on: the webhook infrastructure remaining the integration path for all three customer segments tested.*
> *A reader who wanted to disprove it would need to show: that any of the three segments requires a non-webhook integration path under standard load.*
> *This claim fails if: the webhook layer is replaced or bypassed in any segment before the feature ships.*

*If you cannot complete all three sentences with specific, checkable conditions, the pattern statement is not yet a causal claim — revise the pattern until the self-check can be completed.*

---

Continue the synthesis after the self-check. The synthesis and the self-check should cohere: the synthesis states the pattern; the self-check names exactly what would break it.

### What Remains Uncertain

Name what the investigation did not resolve. At least one specific open question a follow-on investigation could address. Connect each gap to the stakes: "We do not know X. If X turns out to be false, the verdict changes to [Y]."

### Recommendation

**Verdict**: proceed / pause / pivot / abandon

Connect the verdict to the named pattern. Specify the immediate next action — the concrete step that follows from this verdict. "Proceed" is a verdict; "Proceed to prototype, scoped to the auth flow flagged by the compliance signal as the one untested constraint" is a recommendation.

---

*The falsifiability self-check field is a required output in the artifact — all three labeled sentences must appear in the written document. A pattern statement with no named disproof condition is not a causal claim. If the self-check cannot be completed, revise the pattern.*

---

## V-04 — Inertia Frame + Architecturally Distinct Stances

**Axis**: Inertia framing + lifecycle emphasis (combined)
**Hypothesis**: The R2 E-4 blueprint. Combine V-04 R2's inertia+falsifiability frame (C-10 + C-12) with per-section stances upgraded to architecturally distinct operations (C-14) and explicitly extended into non-synthesis sections (C-13). If both independent R2 mechanisms are complementary, this variation should recover the full aspirational score no single R2 variation achieved — passing C-10, C-11, C-12 simultaneously while also passing C-13 and C-14.

---

The question is not whether to learn more about `{topic}`. The question is whether to build it. The signals you gathered either justify that commitment, or they counsel against it. This story makes the case — or closes it.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

For each signal, ask: does this finding change whether `{topic}` should be built? If yes, it belongs. If it adds texture without affecting the verdict, omit it — regardless of how detailed or interesting it is.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

Each section below has a named operation — the specific analytical work that section must do. Read the operation before writing the section. A section that sounds like it is doing what a different section does has not completed its operation.

---

### Section 1 — Stake the Question

**Operation: establish the build/don't-build question this investigation was designed to answer.**

One to two sentences. State the investigation question as the decision it was meant to inform: "We needed to know [X] before we could responsibly decide whether to build `{topic}`." A reader who skips this section should miss something about the decision stakes, not just the topic name.

*Decision filter: does stating this question tell the reader what the verdict depends on?*

### Section 2 — Curate the Evidence

**Operation: select one decision-relevant finding per signal. Omit the rest.**

For each signal: one sentence. Decision-relevant only. Ask for each finding: does this change the build/don't-build calculus for `{topic}`? If yes, include it. If no — if the finding fills out the picture without affecting the verdict — say so in one sentence and stop. Detail that doesn't shift the verdict is not in this section.

Brevity here is correctness, not compression. You are choosing what a decision-maker needs to see.

### Section 3 — Name the Pattern

**Operation: identify the cross-signal finding and explain it causally.**

Step back from the curated evidence. What pattern emerges that no single signal contains? Name it. Then apply the falsifiability test before proceeding:

A pattern statement that says "the signals align because the approach is sound" cannot be disproved — it is a confidence statement, not a causal claim. A genuine causal account names the specific mechanism, assumption, or structural condition that accounts for the convergence — specific enough that a reader can name what evidence would break it.

Write the pattern with this test applied. If someone wanted to argue against your conclusion, they would need to show that [specific condition] does not hold. Name that condition explicitly.

Interpretive voice throughout: "What's striking is..." / "The convergence is not coincidental — it reflects a specific structural constraint..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

**Pattern**: [one extractable sentence with falsifiable causal logic]

### Section 4 — Account for What's Open

**Operation: inventory what the investigation left unresolved, connected to the decision stakes.**

You are not hedging — you are accounting. Name the specific gaps the investigation did not close. For each, state why it matters to the verdict and what a follow-on investigation would need to do to close it.

Required form: "We do not know [X]. If X is false, the recommendation changes to [Y]. It could be resolved by [specific method]."

*Decision filter: does each named uncertainty connect to the verdict? An uncertainty that wouldn't change the recommendation — even if resolved — is decision-neutral. Apply the filter: omit it or explain its stakes.*

At least one named gap with decision stakes attached.

### Section 5 — Advocate for the Verdict

**Operation: issue the verdict and defend the specific choice against the adjacent alternative.**

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern — the rationale cites the pattern, not individual signals. Defend the specific verdict: why this one rather than the adjacent alternative? The causal account from Section 3 grounds this: the verdict follows from the pattern because [reason that invokes the specific mechanism named].

Specify the immediate next action. Recommend as someone who will be held accountable for the call.

Do not retreat to neutral language here. "Given the evidence, I recommend [verdict] — specifically [action], because [the pattern named in Section 3 implies it]."

---

*Before writing the artifact — four checks:*

*— Does the decision filter appear explicitly in at least two non-synthesis sections? (Sections 2 and 4 have labeled forms above. Did both apply the filter — or just acknowledge it in the header?)*

*— Does the pattern section name a specific disproof condition? (Not "the data could be wrong" — a specific, empirically checkable condition.)*

*— Can each section be identified by its operation alone? (Curate ≠ name the shape ≠ account ≠ advocate. If two sections sound like the same thing, one has not completed its operation.)*

*— Does the editorial register persist through Section 5? (If Section 4 or 5 reverts to neutral factual reporting, it has not completed its operation.)*

*Final test: would a skeptic who reads only this document know both what the signals say and exactly what evidence would change the verdict?*

---

## V-05 — Compound: All Three New Criteria

**Axis**: Role sequence + lifecycle emphasis + inertia framing + phrasing register
**Hypothesis**: The compound golden candidate. Full R2 best-mechanism stack (V-04 R2: inertia frame + falsifiability inline + negative example; V-05 R2: named investigator role + audience pressure + per-section stances + register self-check) plus three new targeting mechanisms: inertia test explicitly in ≥2 non-synthesis sections (C-13), per-section stances as architecturally distinct operations (C-14), and falsifiability self-check as a labeled artifact field (C-15). If these mechanisms are complementary rather than competing, this is the 100-point variation for R3. If it scores below V-04, the regression isolates which new mechanism creates tension with the R2 base.

---

You are the lead investigator for `{topic}`. You gathered the signals. Now you are writing the story — a single document that tells your team lead what to do.

Your team lead will read this once. They will make a decision. The default — before your investigation — was to not build `{topic}`. The signals either change that default or confirm it. Make the document worthy of the decision.

**Read in this order:**

1. **Strategy first.** Read `simulations/{topic}/strategy.md`. Note the investigation question. Hold it in mind while reading everything else.
2. **Signals second.** Glob and read all `simulations/**/{topic}-*` artifacts. For each, ask: what is the single finding that most changes or confirms my answer to the investigation question?
3. **Write the story.** Each section below has a named operation. Read the operation label before writing the section.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

Each section performs a distinct analytical operation. These operations are not interchangeable — a section doing the wrong operation has failed its job regardless of how well it is written.

---

### Section 1 — Stake the Question

**Operation: establish the decision this investigation was designed to resolve.**
**Your stance: the investigator who chose to run it.**

Restate the investigation question from `strategy.md` in your own words — as someone who knew why it mattered. One to two sentences. Write it as a decision gate: "We needed to know whether [X] before we could responsibly commit to building `{topic}`." The weight of the question should be present in the language.

*Decision filter applied: does this question anchor the reader in what the verdict depends on?*

### Section 2 — Curate the Evidence

**Operation: select one decision-relevant finding per signal, omitting the rest.**
**Your stance: the investigator distilling each signal to its sharpest decision-relevant point.**

For each signal: one sentence. Write it as the investigator who read it with the investigation question in mind. "The feasibility signal settled the technical risk question — the API rate limits are not a blocker at current load" not "The feasibility signal found API rate limits within acceptable range." The finding carries your interpretive judgment, not just the signal's output.

For each finding, ask: does this change the build/don't-build calculus? If no — if the finding is decision-neutral, however detailed or interesting — say so in one sentence and stop. Completeness is not the goal. Decision salience is.

*Decision filter applied: any finding that does not change the verdict is stated as decision-neutral and omitted from full treatment. Omission is explicit, not silent.*

### Section 3 — Name the Pattern

**Operation: identify the cross-signal finding and account for it causally, with the disproof condition named.**
**Your stance: the analyst who sees what the evidence, taken together, forces.**

Step back from the curated findings. What shape does this evidence take? What appears when you read the signals together that no single signal contains? Name the pattern. Then explain the convergence — not "the signals agree" but "the signals agree because [specific structural reason]."

Apply the falsifiability test before completing this section. A causal claim that cannot be disproved is not a causal claim — it is a confidence statement. A genuine causal account names the specific mechanism, assumption, or structural condition that, if shown false, would break the pattern.

After writing the synthesis, write the following labeled fields as part of the artifact:

**Pattern**: [one extractable sentence — the emergent finding and its causal basis]

**This claim depends on**: [the specific assumption or structural condition the pattern rests on]

**This claim fails if**: [a specific, empirically checkable condition — not "if the data is wrong" but the named condition]

Interpretive voice throughout: "What's striking is..." / "The convergence is not coincidental — it reflects a specific constraint that all three signals assumed..." / "The evidence forces a conclusion I did not enter this investigation expecting..."

### Section 4 — Account for Limits

**Operation: inventory what the investigation left open and connect each gap to the decision stakes.**
**Your stance: the honest investigator who is still responsible for the question.**

Name what the investigation did not resolve. You know these gaps — you ran the investigation. Account for each one: what is specifically open, why does it matter to the verdict, and what would close it? This operation is explicit accounting, not hedging.

Required form: "We do not know [X]. This matters because if X is false, the verdict changes to [Y]. A follow-on investigation could resolve it by [specific method]."

*Decision filter applied: does each named uncertainty connect to the verdict? An uncertainty that wouldn't change the recommendation — even if resolved — is decision-neutral. State it as such or omit it.*

Do not hedge into vagueness. You have an opinion about which uncertainty is most consequential. Name it.

### Section 5 — Advocate for the Verdict

**Operation: issue the verdict and defend the specific choice, connecting the causal account to the action.**
**Your stance: the investigator who will be held accountable for the call.**

Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern — the rationale cites the pattern's causal account, not individual signals. Defend the specific choice: why this verdict rather than the adjacent alternative? The mechanism named in Section 3 grounds this: the verdict follows because [reason invoking the specific mechanism or condition].

Specify the immediate next action: the person, team, or gate that moves as a result of this verdict.

Do not retreat to neutral language here. "Given the evidence, I recommend [verdict] — specifically [action], because the pattern identified [causal account] implies it. This call stands unless [disproof condition from Section 3] is shown to hold."

---

*Before writing the artifact — four checks:*

*1. Decision filter document-wide: does the build/don't-build filter appear explicitly in at least two non-synthesis sections? (Sections 2 and 4 both have labeled forms above. Did both actually apply the filter — or just acknowledge it in the header label?)*

*2. Distinct operations: can each section be identified by its operation alone, without the header? Curate (Section 2) ≠ Name the shape (Section 3) ≠ Account (Section 4) ≠ Advocate (Section 5). If two sections sound like they are doing the same thing, one has not completed its operation.*

*3. Falsifiability self-check: do the "This claim depends on" and "This claim fails if" fields appear in the artifact as written fields — not just in the author's reasoning? If the pattern statement cannot produce a specific, empirically checkable disproof condition, revise the pattern until it can.*

*4. Register: does the investigator's voice persist from Section 1 through Section 5? If Section 4 or 5 reverts to neutral reporting — describing findings rather than accounting for them or advocating from them — those sections have not completed their operations. Revise before writing.*

*Final test: would a skeptic who reads only this document know what the signals say, what specifically would change the verdict, and what happens next? If yes, write the artifact.*
