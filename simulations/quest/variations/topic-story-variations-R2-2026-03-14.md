Written to `simulations/quest/variations/topic-story-variations-R2-2026-03-14.md`.

---

## Five Variations — Round 2 Summary

| # | Axis | Target Criteria | Hypothesis |
|---|------|-----------------|------------|
| **V-01** | Inertia framing | C-10 | "Does this change the build/don't-build decision?" as the filter for every sentence. Primary mechanism for decision-orientation. |
| **V-02** | Causal falsifiability via contrast examples | C-12 | Two-example block (weak/strong) immediately before synthesis instruction. Isolates whether naming the failure mode alone is sufficient to move C-12. |
| **V-03** | Per-section voice anchors | C-11 | Each section gets a named stance ("honest accountant," "decision advocate") before the model writes it. Prevents trailing-tone collapse structurally. |
| **V-04** | Inertia + falsifiability (combined) | C-10 + C-12 | Tests whether decision-argument framing naturally produces falsifiable causal claims, or whether explicit falsifiability instruction is still required within the frame. |
| **V-05** | Investigator stance + register checkpoints | C-11 + C-05 (extending V-04/R1) | V-04 (R1) had strong voice but trailing-tone collapse. Adds per-section checkpoints to the investigator frame without disturbing the editorial momentum. |

**Key tensions for scoring:**

- **V-01 vs V-03** for C-10: V-01 uses framing pressure (who it's for), V-03 uses section-level discipline (what each section does). A document can pass one and fail the other — this tells you which mechanism is load-bearing.
- **V-02** is the most surgical prompt in the set — almost identical to a baseline except for the two-example contrast block. Strong signal if it moves C-12 alone.
- **V-04** will reveal whether C-10 and C-12 are compatible or compete: stripping to decision salience may also strip the causal precision needed for C-12.
- **V-05** is the evolutionary continuation of the best R1 result — if V-04 (R1) was already near-golden on C-05 and C-09, V-05 should push it to C-11 coverage without regression.
al precision needed for C-12. The combination reveals whether these two aspirational criteria coexist.
- **V-05** is the evolutionary path from the strongest R1 result. V-04 (R1) has good C-09 and C-05 behavior; its primary failure mode is C-11 trailing-tone collapse. Register checkpoints directly address that gap without disturbing the investigator frame that produces the voice.

---

## V-01 — Inertia Framing: Status-Quo Competitor

**Axis**: Inertia framing
**Hypothesis**: The default decision on any feature is to not build it. Framing the story as a document that must justify departing from inertia — or confirm that inertia is correct — forces the author to write for decision salience. Every sentence must answer: does this change the build/don't-build calculus? Detail that doesn't shift the verdict is not decision-oriented; it is padding. This framing is the primary mechanism for C-10.

---

The default decision for `{topic}` is to not build it. Before the investigation, that was the reasonable call: low cost, no commitment. The signals you gathered either change that calculus, or they confirm it. Either outcome is valid. The story is the argument.

**Read first:**
1. `simulations/{topic}/strategy.md` — what question did the investigation set out to answer?
2. All `simulations/**/{topic}-*` artifacts — what did each signal establish?

As you read each signal, ask: **Does this finding change the build/don't-build decision?** If yes, it belongs in the story. If not — if it fills out the picture without affecting the verdict — it does not belong, regardless of how interesting it is.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

### What We Set Out to Understand

The investigation question from `strategy.md`, stated plainly. What was the default before we gathered signals, and what did we need to learn to revisit it? One to two sentences.

### What the Signals Revealed

For each signal: one sentence. Not a recap — the specific finding relevant to the build/don't-build question. Omit anything that does not affect the decision. If a signal produced rich findings that are all decision-neutral, say so in one sentence and move on. Completeness is not the goal. Salience is.

### What the Signals Say Together

This is the argument. Step back from individual signals and ask: given everything gathered, has the default changed? What pattern emerged across signals that either justifies departing from inertia, or reinforces it?

Name the pattern. Explain why the signals point this way — not just that they do. Identify the specific assumption, constraint, or dynamic that accounts for the convergence. If someone wanted to argue against your conclusion, what would they have to show is false?

This section should be written by someone who has made a decision — not someone still weighing options.

**Pattern**: [one extractable sentence — the argument in its most compressed form]

### What Remains Uncertain

Name what the investigation did not resolve. Be specific: what would have to be true for the recommended verdict to be wrong? "More data may help" does not name an uncertainty. "We do not know whether X holds at scale because no signal tested beyond Y users — if it does not, the pattern breaks" does.

### Recommendation

State one of: **proceed**, **pause**, **pivot**, or **abandon**.

Connect the verdict to the named pattern. Then say what acting on it requires: the immediate next action, the decision gate, the thing that happens this week. A verdict without an action is a position paper, not a recommendation.

---

*Write to decide, not to document. If the story were a memo to the person who must say yes or no to building `{topic}`, would every sentence earn its place?*

---

## V-02 — Causal Falsifiability Instruction: Contrast Examples

**Axis**: Phrasing register (causal precision via contrast instruction)
**Hypothesis**: The C-12 failure mode is not imprecision — it is the appearance of precision. A causal claim that uses causal language ("because," "accounts for," "driven by") but cannot be disproved reads as analytical while passing no analytical test. Providing two-sentence contrast examples of falsifiable vs. non-falsifiable claims, immediately before the synthesis instruction, makes the failure mode recognizable before the model writes it.

---

Synthesize all gathered signals for `{topic}` into a narrative artifact at `simulations/{topic}/{topic}-story-{date}.md`.

**Read first:**
1. `simulations/{topic}/strategy.md` — the investigation question.
2. All `simulations/**/{topic}-*` artifacts — what each signal found.

**Write the four sections below.** Before you write "What the Signals Say Together," read the causal precision note.

---

### What We Set Out to Understand

The investigation question from `strategy.md`. One to two sentences. What did we need to know, and why?

### What the Signals Revealed

For each signal: one sentence, the single most important finding. Selective, not exhaustive — the key finding that most advances or complicates the investigation question.

---

**Causal precision note — read before writing the next section.**

A pattern statement has two jobs: name the convergence, and explain it. Most pattern statements only do the first. The difference:

> *Weak (non-falsifiable)*: "The signals converge because the feature is well-positioned for the market." What would make this false? Nothing specific. It is a restatement of convergence in causal language.

> *Strong (falsifiable)*: "The signals converge because the integration cost is bounded by the existing webhook infrastructure — all three technical signals assumed this constraint holds. If the webhook layer is replaced or removed, the convergence breaks." What would make this false? Show that the webhook assumption does not hold.

The test: after writing your pattern statement, ask — what specific evidence would disprove it? If the answer is "nothing specific," the claim is not causal. Revise until you can name what would falsify it.

---

### What the Signals Say Together

Draw the cross-signal conclusion — the insight that requires all signals together to see. Name the pattern. Apply the causal precision test: explain why the signals converge, in terms specific enough that a reader can identify what evidence would break the claim.

Interpretive voice. "What's striking is..." / "The convergence points to a specific structural reason..." / "The pattern holds because..." Take a position.

**Pattern**: [one extractable sentence with falsifiable causal logic]

### What Remains Uncertain

Name the open questions this investigation did not resolve. At least one specific unknown a follow-on investigation could address. Format: "We do not know [X] because [Y] — this matters because if X is false, the recommendation changes."

### Recommendation

**Verdict**: proceed / pause / pivot / abandon

Connect the verdict to the named pattern. Specify the immediate next action or decision gate — "proceed" alone is a verdict, not a recommendation.

---

## V-03 — Register Checkpoint: Per-Section Voice Anchors

**Axis**: Lifecycle emphasis (per-section editorial register)
**Hypothesis**: The most common C-11 failure mode is strong editorial voice in the synthesis section that collapses into neutral reporting in uncertainty and recommendation. This happens because synthesis is the section most associated with interpretation — the others feel like they are reporting facts. Assigning a named editorial stance to each section before writing it makes register a property of the whole document, not just the opening.

---

Synthesize all gathered signals for `{topic}` into a narrative artifact at `simulations/{topic}/{topic}-story-{date}.md`.

**Read first:**
1. `simulations/{topic}/strategy.md`
2. All `simulations/**/{topic}-*` artifacts

Each section of the story has a named stance. Read the stance before you write the section. The stance is not decoration — it is the register the section must maintain throughout.

---

### Section 1 — What We Set Out to Understand

**Stance: the investigator framing the question.**
You chose this investigation. You know why it mattered. Write it as someone who decided to spend time on this — not as a neutral documenter of what `strategy.md` says. One to two sentences that make the reader feel the weight of the question.

### Section 2 — What the Signals Revealed

**Stance: the informed editor choosing what to surface.**
You read all the signals. Most of what you read is not in this section, because most of it does not change what the reader needs to know. Write each signal's entry as an editor who selected the one finding that matters — not as a transcriptionist listing outputs. One sentence per signal; brevity is the stance.

### Section 3 — What the Signals Say Together

**Stance: the analyst who sees the shape of the evidence.**
You have held all the signals at once. Something emerged that no single signal said. Name it. Explain the convergence — not "three signals point this way" but "three signals point this way because [specific shared constraint or mechanism]." Write as someone who has an interpretation, not a system generating a report.

Interpretive language throughout: "What's striking is...," "The evidence forces a conclusion...," "This pattern holds because..."

**Pattern**: [one extractable sentence naming the emergent finding]

### Section 4 — What Remains Uncertain

**Stance: the honest accountant — not the hedger.**
You know what the investigation did not resolve. Name it without retreating into vagueness. "There is uncertainty around X" is hedging. "We do not know X, and here is why that matters: if X is false, the verdict changes" is honest accounting. At least one specific open question a follow-on investigation could answer. Maintain the editorial stance — you have an opinion about which uncertainty is most consequential.

### Section 5 — Recommendation

**Stance: the decision advocate who will be held accountable.**
You are not filing a report — you are making a call. State the verdict: **proceed**, **pause**, **pivot**, or **abandon**. Connect it to the pattern you named. Recommend as someone who will stand behind this decision. Specify the immediate next action: what happens now, not what could happen someday.

---

*After writing all five sections, read them in sequence: does the editorial register persist from Section 1 through Section 5? A document that establishes strong voice in Section 3 and reverts to neutral factual reporting in Sections 4 and 5 has failed to sustain the stance. Revise the trailing sections before writing the artifact.*

---

## V-04 — Inertia Framing + Causal Falsifiability

**Axis**: Inertia framing (C-10) + causal falsifiability instruction (C-12)
**Hypothesis**: Decision-orientation and causal precision are not in tension — they reinforce each other. A document written for a decision-maker needs a precise causal account because the decision-maker will ask both "why does the evidence point this way?" and "what would make this wrong?" The combination tests whether framing the document as a decision argument naturally produces more falsifiable causal claims, or whether explicit falsifiability instruction is still required even within the decision-argument frame.

---

The question is not whether to learn more about `{topic}`. The question is whether to build it. The signals you gathered either justify that commitment, or they counsel against it. Write the story that makes the case — or closes it.

**Read first:**
1. `simulations/{topic}/strategy.md`
2. All `simulations/**/{topic}-*` artifacts

For each signal, ask: does this finding change whether `{topic}` should be built? If yes, it belongs. If it adds texture without affecting the verdict, it does not — regardless of how detailed or interesting it is.

**Write the artifact** at `simulations/{topic}/{topic}-story-{date}.md`.

---

### What We Set Out to Understand

The investigation question, stated as the decision it was meant to inform: "We needed to know [X] before we could responsibly decide [Y]." One to two sentences.

### What the Signals Revealed

One sentence per signal. Decision-relevant only. If a signal's most important finding is neutral to the build/don't-build question, say so in one sentence. Omit the rest.

### What the Signals Say Together

The argument. Before you write this section, apply the falsifiability test:

> A pattern statement that explains convergence as "the signals align because the approach is sound" cannot be disproved. It is a confidence statement, not a causal claim. A genuine causal claim names the specific mechanism, assumption, or structural condition that accounts for the convergence — specific enough that a reader can name what evidence would break it.

Write the pattern with this test applied. Name the emergent cross-signal finding. Explain the convergence precisely enough that someone who wanted to argue against your conclusion would know exactly what to disprove. Take a position.

**Pattern**: [one extractable sentence with falsifiable causal logic]

### What Remains Uncertain

Name what the investigation did not resolve — and connect it to the decision. "We do not know X. If X is false, the recommendation changes to [Y]." At least one specific, named uncertainty with stakes attached. Generic hedges do not name an uncertainty.

### Recommendation

**Verdict**: proceed / pause / pivot / abandon

Ground the verdict in the named pattern. Connect the causal account to the decision: the verdict follows from the pattern because [reason]. Say what acting on the verdict requires — the immediate next action, the thing that must happen before the decision is final.

---

*The test for this story: would a skeptic who reads only this document know both what the signals say and exactly what evidence would change the verdict? If yes, the story is decision-oriented and causally precise.*

---

## V-05 — Role Sequence + Register Checkpoint

**Axis**: Role sequence (strategy-first read order, decision-advocate framing) + lifecycle emphasis (per-section register checkpoints)
**Hypothesis**: V-04 (R1) established strong C-05 and C-09 behavior through named-investigator framing and explicit "why do signals converge" instruction. Its primary failure mode is C-11 trailing-tone collapse: strong voice in synthesis, neutral reporting in uncertainty and recommendation. Adding per-section register checkpoints to the investigator frame should preserve what V-04/R1 does well while closing the trailing-tone gap — without disrupting the editorial momentum the investigator stance produces.

---

You are the lead investigator for `{topic}`. You have gathered the signals. Now you are writing the story — a single document that tells your team lead what to do.

Your team lead will read this once. They will make a decision. Make the document worthy of the decision.

**Read in this order:**

1. **Strategy first.** Read `simulations/{topic}/strategy.md`. Note the investigation question. Hold it in mind while reading everything else.

2. **Signals second.** Glob and read all `simulations/**/{topic}-*` artifacts. For each, ask: what is the single finding that most changes or confirms my answer to the investigation question?

3. **Write the story.** Each section has a named stance below. Read the stance before writing the section.

---

**Artifact**: `simulations/{topic}/{topic}-story-{date}.md`

---

### What We Set Out to Understand

**Stance: the investigator who chose the question.**
Restate the investigation question from `strategy.md` in your own words. Write it as someone who knew why it mattered — not as a neutral transcription. One to two sentences that anchor the reader in the problem, not the process.

### What the Signals Revealed

**Stance: the investigator distilling each signal to its sharpest point.**
For each signal: one sentence. Write it as the investigator who read it with the investigation question in mind — not as a cataloguer. "The feasibility signal settled the technical risk question — the API rate limits are not a blocker" not "The feasibility signal found that API rate limits are within acceptable range." The finding should carry the investigator's interpretive judgment, not just the signal's output.

### What the Signals Say Together

**Stance: the analyst who sees what the evidence, taken together, forces.**
Step back from individual signals. What shape does the evidence take? Name the pattern. Explain the convergence — not "three signals agree" but "three signals agree because [specific structural reason]." Write with the confidence of someone who has done the work and has an opinion.

"What's striking is..." / "The convergence is not coincidental — it reflects..." / "The evidence forces a conclusion I did not enter the investigation expecting..."

**Pattern**: [one extractable sentence stating the cross-signal finding and its causal basis]

### What Remains Uncertain

**Stance: the honest investigator accounting for the limits of the work.**
You know what the investigation did not resolve. Name it as someone who is still responsible for the question — not as someone passing uncertainty to the reader. At least one specific open question a follow-on investigation could address. Connect it to the stakes: "We do not know X; if X turns out to be false, the verdict changes to [Y]."

Do not hedge into vagueness. Maintain the investigator's voice: "This investigation did not reach [X]. That matters because..."

### Recommendation

**Stance: the investigator who will be accountable for the call.**
Verdict: **proceed**, **pause**, **pivot**, or **abandon**. State it plainly.

Connect the verdict to the named pattern — the rationale cites the pattern, not individual signals. Specify what acting on the verdict requires: the immediate next action, the person or team responsible, the decision gate. Recommend as someone who will stand behind it.

Do not retreat to neutral language here. "Given the evidence, I recommend proceeding to prototype — specifically targeting the auth flow, which the signals flagged as the one untested constraint."

---

*Register check before writing the artifact: does the investigator's voice persist from the opening question through the final recommendation? If the uncertainty or recommendation sections feel like neutral reporting, they are not in the investigator's stance. Revise them before writing.*
