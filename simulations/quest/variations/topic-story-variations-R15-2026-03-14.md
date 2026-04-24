# topic-story Rubric v15 — 5 Variations (R15)

---

## V-01

**Axis**: Phrasing register — formal/technical, imperative voice, criterion-dense directives
**Hypothesis**: Dense specification language with explicit structural markers reduces ambiguity in per-section behavior, producing tighter adherence to S4b/S5 inertia framing and hedge class labeling.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

Your task: produce an editorial synthesis of all signals gathered for this topic. This is not a signal inventory. This is not a section-by-section summary. This is a coherent narrative in the author's voice interpreting what the signals say together — their collective meaning, the pattern they form, and what a decision-maker should do.

---

### Inputs

Load all signal artifacts for `{{topic}}` from the following namespaces:

- `simulations/scout/` — market, feasibility, compliance, positioning, naming, requirements, stakeholders
- `simulations/draft/` — pitch, proposal, spec
- `simulations/review/` — code, design, users, customers
- `simulations/flow/` — dataflow, lifecycle, integration, throttle, trigger, resilience, conversation
- `simulations/prove/` — hypothesis, websearch, prototype, interview, analysis, publish, intelligence, synthesize
- `simulations/listen/` — feedback, support, adoption
- `simulations/program/` — plan

Load only artifacts whose `topic` field matches `{{topic}}`. Ignore artifacts from other topics.

---

### Output Structure

Produce five sections: S1, S2, S3, S4, S5. Each section has a defined function and structural requirements. Execute each as specified.

---

**S1 — What We Set Out to Understand**

Write one paragraph. Past tense. State the investigative question that motivated signal gathering — the decision, capability, or uncertainty that caused this topic to be opened. Do not begin S1 with a phrase that inventories the signals or summarizes the investigation process.

**Prohibited opening class: aggregate-first hedging constructions.** This class includes any opening that leads with an inventory of the evidence base rather than the investigative question. Enumerated surface forms include: "The signals gathered for...", "This synthesis covers...", "Based on the evidence collected...", "Across the namespaces surveyed...", "The investigation examined...". The class label names the failure mode — opening by cataloging evidence rather than stating the question — so novel phrasings that belong to this class are prohibited even if their surface form does not appear above. A construction is an aggregate-first hedging construction when it satisfies the class criterion: it opens by gesturing at the evidence base rather than stating the investigative question. Class membership is determined by structural function, not surface similarity to enumerated examples.

Open with the question itself, or with the decision pressure that generated it, or with the capability's relationship to what it is meant to change.

---

**S2 — What Each Signal Revealed**

Write one paragraph per signal namespace that contributed a material finding. Each paragraph: (a) names the namespace, (b) states the key finding from that namespace — not all findings, the one that most directly informs the question in S1 — and (c) explains why that finding matters to the decision at hand. Omit namespaces that produced no artifacts for this topic. Do not enumerate findings; interpret them. The paragraph is the act of interpretation, not the transcript of a signal.

---

**S3 — What the Signals Say Together**

Write one paragraph. This is the editorial center of the artifact. Do not summarize S2. Identify the pattern or conclusion that emerges only when all findings are held simultaneously — the thing that is not visible from any single namespace but becomes visible across them. If the signals converge, state the convergence clearly and name what they converge on. If the signals fracture into competing interpretations, name the fracture explicitly and locate its source.

---

**S4 — What Remains Uncertain**

Write two sub-paragraphs, labeled S4a and S4b.

**S4a — Residual Uncertainties.** Name the signal gaps — namespaces not yet activated, questions the investigation opened without resolving, findings contradicted by other findings. Be specific. A residual uncertainty is only named if it is material to the recommendation in S5.

**S4b — Inertia Comparator.** State explicitly what happens if this feature is not built, or if the decision is deferred indefinitely. Name the status quo cost. Identify what the team or user continues to experience in the absence of this capability. This is the inertia baseline against which S5's recommendation will be measured. S4b must be present and must name a specific outcome, not a generic claim that inaction has costs.

---

**S5 — Recommendation**

Write three paragraphs: Para 1, Para 2, Para 3.

**Para 1 — Recommendation.** State the recommendation explicitly: proceed, pause, pivot, or abandon. Name the option. Give the primary reason drawn from S3. Cross-reference S4b: state whether the recommended action is preferable to the inertia scenario identified in S4b, and why. The recommendation must engage the inertia comparator — a recommendation that does not explain why acting is preferable to the S4b baseline is incomplete.

**Para 2 — Counterargument.** Address the strongest material uncertainty from S4a. Acknowledge what makes it material. Explain why the recommendation in Para 1 holds despite it, or name the specific condition under which it would flip to a different recommendation.

**Para 3 — Action Directive.** State the action directive as three elements:

1. **Trigger condition** — identify the specific event or signal state that would make waiting costlier than acting. Name it precisely: a market event, a competitive move, a technical proof point, a team capacity signal, or a date threshold. The trigger is not "when you're ready" or "when confidence increases" — it must be an identifiable, observable event.

2. **Action option** — state the specific step recommended when the trigger fires. This is the concrete action: a sprint commitment, a prototype authorization, a go/no-go decision gate, a stakeholder review.

3. **Inertia consequence at trigger** — name the specific outcome forgone if the trigger fires without action. This is not the general claim from Para 1 or S4b that delay is costly. This is the specific thing lost at the moment the trigger fires unmet: the window that closes, the position that is taken by a competitor, the technical debt that locks in, the team capacity that disperses. The inertia-at-trigger element must be tied to the trigger condition named in element 1, not stated as a background observation.

A Para 3 that contains trigger + action but omits the inertia consequence at trigger is structurally incomplete and must be revised before submission.

---

### Voice

Editorial. The author has read the signals, formed a view, and is now writing in their own voice to explain what they found and what they recommend. Confidence where the signals are clear; explicit uncertainty where they are not. No passive-voice hedging ("it would appear that..."). No probability vocabulary as a substitute for judgment ("there may be some evidence suggesting...").

The author is not a summarizer. The author is a decision advisor.

---

### Output

Filename: `{{topic}}-story-{{date}}.md`

Frontmatter:

```yaml
---
topic: {{topic}}
signal: story
date: {{date}}
---
```

Save to: `simulations/topic/{{topic}}-story-{{date}}.md`

---

## V-02

**Axis**: Output format — slot-fill template; author populates labeled slots, rubric criteria embedded as slot instructions
**Hypothesis**: Presenting the rubric criteria as slot labels rather than prose instructions shifts compliance from recall to recognition, reducing structural omissions in S4b and Para 3 inertia elements.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

Read all signal artifacts for `{{topic}}` across all namespaces. Then produce the story artifact by populating every slot in the template below. Each slot has a label, an instruction, and a required element count. Do not skip slots. Do not merge slots.

---

### Signal Input

Load from:
- `simulations/scout/` — market, feasibility, compliance, positioning, naming, requirements, stakeholders
- `simulations/draft/` — pitch, proposal, spec
- `simulations/review/` — code, design, users, customers
- `simulations/flow/` — dataflow, lifecycle, integration, throttle, trigger, resilience, conversation
- `simulations/prove/` — hypothesis, websearch, prototype, interview, analysis, publish, intelligence, synthesize
- `simulations/listen/` — feedback, support, adoption
- `simulations/program/` — plan

Match only artifacts where `topic: {{topic}}`.

---

### Story Template

Produce one file. Populate every slot. Do not alter slot labels. Do not omit slots.

```
---
topic: {{topic}}
signal: story
date: {{date}}
---

## S1 — What We Set Out to Understand

[SLOT: Opening sentence — state the investigative question, decision pressure, or core uncertainty.
CONSTRAINT: Must NOT be an aggregate-first hedging construction. This class of prohibited openings 
leads with an inventory of the evidence base rather than the investigative question. Prohibited 
surface forms: "The signals gathered for...", "This synthesis covers...", "Based on the evidence 
collected...", "Across the namespaces surveyed...". The class boundary: any opening that gestures 
at the evidence base before stating the question belongs to this class, regardless of surface form.
Open with the question, the decision pressure, or the capability's purpose — not with what was 
gathered.]

[SLOT: Investigative question — one paragraph. What were we trying to learn? What decision was 
this investigation meant to inform? Why was this question worth investigating?]

---

## S2 — What Each Signal Revealed

[SLOT: For each namespace with artifacts, one paragraph.
Format per namespace paragraph:
  - Namespace name (e.g., scout, prove, listen)
  - Key finding: the single finding that most directly informs S1's question
  - Interpretation: why this finding is material to the decision
Do not include namespaces with no artifacts for this topic.
Do not list findings — interpret them.]

---

## S3 — What the Signals Say Together

[SLOT: One paragraph. Editorial synthesis only.
Identify the cross-namespace pattern — what is visible only when all findings are 
held simultaneously. 
If convergent: state what they converge on.
If fractured: name the fracture and locate its source.
Do not summarize S2. Do not restate individual findings.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph.
Name the material gaps: signal namespaces not activated, questions opened without resolution, 
findings contradicted by other findings.
Include only uncertainties material to S5's recommendation.]

---

## S4b — Inertia Comparator

[SLOT: One paragraph.
REQUIRED ELEMENT: Name what happens if this feature is not built or the decision is deferred.
State the status-quo cost explicitly. Name what the team or user continues to experience in 
the absence of this capability.
This is the inertia baseline S5's recommendation must be measured against.
A slot that says "inaction has costs" without naming them does not satisfy this requirement.]

---

## S5 — Recommendation

### Para 1 — Recommendation Statement

[SLOT: One paragraph.
REQUIRED: Name the recommendation — proceed, pause, pivot, or abandon.
REQUIRED: Give the primary reason drawn from S3.
REQUIRED: Engage the inertia comparator from S4b — explain why the recommended action is 
preferable to the S4b inertia scenario.]

### Para 2 — Counterargument and Resilience

[SLOT: One paragraph.
REQUIRED: Name the strongest material uncertainty from S4a.
REQUIRED: Explain why the recommendation holds despite it, OR name the condition under which 
the recommendation would change.]

### Para 3 — Action Directive

[SLOT: Three-element directive. All three elements are required.

ELEMENT 1 — Trigger Condition:
State the specific, observable event or signal state that makes waiting costlier than acting.
Must be identifiable and verifiable — not "when confidence increases" or "when ready".
Examples: a competitor launch, a technical proof point, a capacity window, a date threshold.

ELEMENT 2 — Action Option:
State the specific step recommended when the trigger fires.
Must be a concrete action — not a general direction. 
Examples: sprint authorization, prototype funding, go/no-go gate, stakeholder decision.

ELEMENT 3 — Inertia Consequence at Trigger:
Name the specific outcome forgone if the trigger fires without action.
This is NOT the general delay cost from Para 1 or S4b.
This is the specific thing lost at the moment the trigger fires unmet:
the window that closes, the position taken, the technical lock-in that occurs, 
the team capacity that disperses.
Must be tied to the specific trigger in Element 1, not stated as a background observation.

A Para 3 missing any of these three elements must be revised before submission.]
```

---

### Voice

Write in the author's voice throughout. The author is a decision advisor who has read the signals and formed a view. The tone is editorial: direct where the signals are clear, explicitly uncertain where they are not. Avoid passive-voice hedging constructions.

---

### Submission

Save the completed template to: `simulations/topic/{{topic}}-story-{{date}}.md`

Verify before saving: every slot is populated; Para 3 contains all three required elements (trigger, action, inertia-at-trigger); S4b names a specific inertia outcome; S1 does not open with an aggregate-first hedging construction.

---

## V-03

**Axis**: Inertia framing — status-quo competitor named and foregrounded throughout; every section makes the inertia scenario legible, not just S4b/S5
**Hypothesis**: Distributing inertia framing across all five sections produces stronger S4b/S5 inertia elements by establishing the status-quo competitor as a named entity early and returning to it explicitly at each section boundary.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

Before you write a single section, establish the inertia scenario: what is the current state of affairs if this feature does not exist? What does the user or team do instead? What is the cost of that alternative? Give this scenario a name — "the inertia scenario" or a more specific label drawn from the signals — and carry it as an explicit reference throughout the artifact.

The topic-story artifact is an editorial synthesis of all signals gathered for `{{topic}}`. It is not a signal inventory. It is a decision argument: evidence gathered, pattern found, recommendation made. The inertia scenario is the decision's implicit comparator — the answer to "compared to what?" The story must make that comparator legible in every section where it is relevant, not only in the recommendation.

---

### Step 1 — Establish the Inertia Scenario

Before writing S1–S5, name the inertia scenario. Load signal artifacts from:

- `simulations/scout/` — market, feasibility, compliance, positioning, naming, requirements, stakeholders
- `simulations/draft/` — pitch, proposal, spec
- `simulations/review/` — code, design, users, customers
- `simulations/flow/` — dataflow, lifecycle, integration, throttle, trigger, resilience, conversation
- `simulations/prove/` — hypothesis, websearch, prototype, interview, analysis, publish, intelligence, synthesize
- `simulations/listen/` — feedback, support, adoption
- `simulations/program/` — plan

From the signals, identify: what does the user or team currently do in the absence of this capability? What is the current workaround, gap, or absent support? Name it. This name will appear in S4b and S5 as the inertia comparator. Establish it now; do not let it remain implicit.

---

### Step 2 — Write the Story

Produce five sections: S1, S2, S3, S4, S5.

---

**S1 — What We Set Out to Understand**

State the investigative question. One paragraph, past tense. Name what was being evaluated and why the question was worth investigating. Where relevant, place the question in relief against the inertia scenario — the investigation was opened because the current state (inertia scenario name) was insufficient in some way. If that framing is accurate for this topic, use it; if the investigation was motivated differently, state the actual motivation.

Do not begin S1 with a phrase that inventories the signals or catalogs what was gathered. **Prohibited class: aggregate-first hedging constructions** — openings that lead with an evidence base summary rather than the investigative question. This class includes but is not limited to: "The signals gathered for...", "This synthesis covers...", "Based on the evidence collected...", "Across the namespaces surveyed...". The class criterion is structural: the opening places the evidence base first and the question second, reversing the appropriate order. Any opening that satisfies this criterion belongs to this class, regardless of surface form.

---

**S2 — What Each Signal Revealed**

One paragraph per contributing namespace. Each paragraph names the namespace, states the key finding, and interprets its significance to the decision. Where a signal finding directly characterizes or quantifies the inertia scenario — what users currently endure, what teams currently work around — name that characterization explicitly. The inertia scenario is a real cost; signal findings that document it are material and should be identified as such.

---

**S3 — What the Signals Say Together**

One paragraph. The editorial synthesis. Identify the cross-namespace pattern. If the signals converge, name what they converge on. If the signals fracture, name the fracture. Where the convergence or fracture bears directly on the inertia scenario — where the signals collectively confirm, complicate, or reframe the cost of not building — name that bearing explicitly. The story is not just "what the signals say about the feature" but "what the signals say about the decision," and the decision includes the alternative.

---

**S4 — What Remains Uncertain**

Two sub-paragraphs.

**S4a — Residual Uncertainties.** Name material gaps and unresolved findings. Be specific. Include only uncertainties that could change the recommendation in S5.

**S4b — Inertia Comparator.** State the inertia scenario named in Step 1 explicitly. Describe what the user or team continues to experience in the absence of this capability. Name the status-quo cost. This is not a hedged claim ("there may be some cost to delay") — it is a named description of the current state that the recommendation in S5 will compete against. S4b must be specific enough that a decision-maker could explain the inertia scenario to a third party from this paragraph alone.

---

**S5 — Recommendation**

Three paragraphs.

**Para 1.** State the recommendation: proceed, pause, pivot, or abandon. Name it. Give the primary reason from S3. Explicitly compare the recommended action to the inertia scenario from S4b: why is acting preferable to remaining in the inertia scenario? The recommendation must be made relative to the inertia comparator, not in isolation.

**Para 2.** Address the strongest material uncertainty from S4a. Explain why the recommendation holds despite it, or name the condition that would flip it.

**Para 3.** State the action directive. This paragraph must contain three structural elements — no fewer:

First, name the **trigger condition**: the specific observable event or signal state at which waiting becomes costlier than acting. The trigger must be verifiable — a market event, a technical threshold, a competitive move, a capacity window, a date — not a general readiness condition.

Second, state the **action option**: the specific step recommended when the trigger fires. This is a concrete commitment, not a general direction.

Third, name the **inertia consequence at the trigger**: what is specifically forgone if the trigger fires without action. This is not the general inertia scenario from S4b. This is the particular cost at the trigger point — the thing that is irreversibly lost or locked in at the moment the trigger fires unmet. The inertia-at-trigger element must be tied to the specific trigger condition named in this paragraph. A Para 3 that includes trigger and action but omits the inertia consequence at the trigger is incomplete.

---

### Voice

Editorial. The author has formed a view from the signals and is arguing for it. Direct where the signals are clear; named and qualified where they are not. The inertia scenario is a real entity in the narrative — not a rhetorical gesture but a specific, nameable alternative that the recommendation competes against.

---

### Output

Filename: `{{topic}}-story-{{date}}.md`

Frontmatter:
```yaml
---
topic: {{topic}}
signal: story
date: {{date}}
---
```

Save to: `simulations/topic/{{topic}}-story-{{date}}.md`

---

## V-04

**Axes**: Role sequence (Evidence Reader → Pattern Finder → Decision Framer, sequential activation) + Lifecycle emphasis (explicit phase boundaries with completion criteria and handoff signals)
**Hypothesis**: Separating the reading, synthesis, and recommendation roles into sequential phases — each with an explicit completion gate before the next activates — prevents premature recommendation formation and strengthens S3 pattern quality and S5 inertia specificity.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

This skill runs in three sequential phases. Each phase has a defined role, a defined input, defined outputs, and a completion gate. Do not begin Phase 2 until Phase 1's completion gate is met. Do not begin Phase 3 until Phase 2's completion gate is met.

---

### Phase 1 — Evidence Reader

**Role**: You are the Evidence Reader. Your task is to gather and read all signal artifacts for `{{topic}}`. You do not interpret yet. You do not form recommendations yet. You read.

**Inputs**: All signal artifacts where `topic: {{topic}}` in:
- `simulations/scout/` — market, feasibility, compliance, positioning, naming, requirements, stakeholders
- `simulations/draft/` — pitch, proposal, spec
- `simulations/review/` — code, design, users, customers
- `simulations/flow/` — dataflow, lifecycle, integration, throttle, trigger, resilience, conversation
- `simulations/prove/` — hypothesis, websearch, prototype, interview, analysis, publish, intelligence, synthesize
- `simulations/listen/` — feedback, support, adoption
- `simulations/program/` — plan

**Output of Phase 1** (internal, not written to file):
For each namespace that has at least one artifact:
- Namespace name
- Number of artifacts
- The single most significant finding, stated in one sentence
- The inertia signal (if present): any finding that characterizes what users or teams currently do without this capability

**Completion gate**: All contributing namespaces have been read. An inertia signal has been identified if present in the artifacts. The Evidence Reader's outputs are complete. Proceed to Phase 2.

---

### Phase 2 — Pattern Finder

**Role**: You are the Pattern Finder. You have the Evidence Reader's findings. Your task is to identify the cross-namespace pattern — what the signals say together that is not visible from any single namespace.

**Inputs**: Evidence Reader outputs from Phase 1.

**Work** (internal, not written to file):
1. Array all namespace findings simultaneously.
2. Identify convergences: where two or more namespaces point to the same conclusion.
3. Identify fractures: where two or more namespaces contradict each other or point toward different conclusions.
4. Identify the dominant pattern: if convergences outweigh fractures, name the convergence; if fractures dominate, name the fracture and its source.
5. Identify residual uncertainties: namespace gaps, contradicted findings, questions opened without resolution — limit to those material to a recommendation.
6. Confirm the inertia scenario: using the inertia signal from Phase 1 (or its absence), state what continues to occur if this feature is not built. Name it.

**Output of Phase 2** (internal, not written to file):
- Dominant pattern statement (one sentence)
- Fracture description (if present, one sentence; if absent, note its absence)
- Residual uncertainties list (max 3, each material)
- Named inertia scenario: what happens without this capability

**Completion gate**: Dominant pattern is named. Inertia scenario is named. Residual uncertainties are identified. Proceed to Phase 3.

---

### Phase 3 — Decision Framer

**Role**: You are the Decision Framer. You have the Pattern Finder's synthesis. Your task is to write the topic-story artifact: five sections, S1 through S5, in the author's editorial voice.

**Inputs**: Evidence Reader outputs (Phase 1) + Pattern Finder outputs (Phase 2).

---

**S1 — What We Set Out to Understand**

One paragraph. Past tense. State the investigative question that opened this topic. Name what was being evaluated and the decision it was meant to inform.

**Opening constraint**: Do not begin S1 with an **aggregate-first hedging construction** — the class of openings that leads with an inventory of the evidence base before stating the investigative question. Prohibited surface forms include: "The signals gathered for...", "This synthesis covers...", "Based on the evidence collected...", "Across the namespaces surveyed...", "The investigation examined...". This is a class prohibition, not merely an enumeration: any opening satisfying the structural criterion — evidence base first, question second — belongs to this class even if its surface form does not appear above. Open with the question, the decision pressure, or the capability's purpose.

---

**S2 — What Each Signal Revealed**

One paragraph per contributing namespace. Each paragraph: names the namespace, states the key finding from the Evidence Reader's reading of that namespace, and explains why it matters to the question in S1. Do not enumerate findings. Interpret them.

---

**S3 — What the Signals Say Together**

One paragraph. Write directly from the Pattern Finder's dominant pattern statement. Do not re-summarize S2. State the cross-namespace pattern — convergence or fracture — in the author's own interpretive voice.

---

**S4 — What Remains Uncertain**

**S4a.** One paragraph. Write from the Pattern Finder's residual uncertainties. Name only uncertainties material to the recommendation. Be specific.

**S4b.** One paragraph. Write from the Pattern Finder's named inertia scenario. Describe what continues to occur without this capability. Name the status-quo cost explicitly. S4b is the inertia comparator for S5.

---

**S5 — Recommendation**

**Para 1.** State the recommendation: proceed, pause, pivot, or abandon. Name it. Give the primary reason drawn from S3. Engage the inertia comparator from S4b: state that the recommended action is preferable to the S4b inertia scenario and explain why.

**Para 2.** Address the strongest residual uncertainty from S4a. Explain why the recommendation holds despite it, or name the condition that flips it.

**Para 3.** The action directive. Contains three required elements:

- **Trigger condition**: the specific observable event or signal state at which waiting becomes costlier than acting. Must be identifiable and verifiable.
- **Action option**: the specific step recommended when the trigger fires. Concrete, not general.
- **Inertia consequence at trigger**: the specific outcome forgone if the trigger fires without action. This is not the general inertia scenario from S4b — it is the particular cost at the trigger point, tied to the specific trigger condition named in this paragraph. The trigger is the decision event; the inertia-at-trigger element names what is irreversibly lost at that event if action is not taken.

All three elements are required. A Para 3 with trigger + action and no inertia-at-trigger element is structurally incomplete and must be revised.

---

**Voice**: Editorial throughout. The Decision Framer writes in the author's voice — confident where the Pattern Finder's synthesis is strong, explicitly uncertain where residual uncertainties are material. No passive hedging. No probability vocabulary as a substitute for interpretation.

---

**Output**

Filename: `{{topic}}-story-{{date}}.md`

```yaml
---
topic: {{topic}}
signal: story
date: {{date}}
---
```

Save to: `simulations/topic/{{topic}}-story-{{date}}.md`

---

## V-05

**Axes**: Phrasing register (conversational, second-person) + Inertia framing (distributed throughout, status-quo named early) + Output format (narrative guidance over structural template)
**Hypothesis**: Conversational second-person framing lowers the cognitive distance between instruction and execution, making inertia framing and three-element Para 3 requirements easier to internalize as authorial moves rather than checklist items, producing more naturally integrated compliance.

---

You're writing the topic-story for `{{topic}}`.

Here's what this artifact is: it's the editorial synthesis. You've spent time gathering signals across namespaces, and now you're going to say what you actually think. Not what each signal said — you're past that. What do they say together? What does that mean for the decision? What should happen next?

This is you, as an author, writing in your own voice.

---

### Before you start — name the alternative

Before you write the first word of the story, take a moment to name the inertia scenario: what happens if this feature doesn't get built? What do users do instead? What gap does the team live with? Give it a name you'll use throughout. The story you're about to write is ultimately a decision argument, and every decision argument has an implicit comparator — the thing that continues if no action is taken. Name yours now so you can reference it naturally as you write.

Load your signal artifacts from `simulations/` across these namespaces: scout, draft, review, flow, prove, listen, program. Only artifacts where `topic: {{topic}}`.

---

### S1 — What You Set Out to Understand

This is your opening paragraph. You're telling the reader what question you were trying to answer, what decision this investigation was meant to inform, or what capability you were evaluating and why it mattered enough to investigate.

One thing not to do: don't open by cataloging the evidence. You'll recognize this failure mode — it looks like "The signals gathered for X covered seven namespaces..." or "This synthesis examines the evidence from..." or "Based on the investigation conducted across...". These are **aggregate-first hedging constructions**: openings that lead with the evidence base rather than the question. The problem with them is that they tell the reader what was gathered rather than why it mattered. The class criterion is structural, not cosmetic — any opening that places evidence inventory before investigative question belongs to this class, even if it doesn't match any of the surface forms listed. Don't open that way. Open with the question, or the pressure that generated it, or the thing you needed to understand and didn't yet.

---

### S2 — What Each Signal Told You

For each namespace that contributed something material, write one paragraph. You're not transcribing the signal — you're saying what it meant. What was the key thing you learned from this namespace? Why does it matter to the question in S1?

If the scout signals showed something about who actually wants this and why, say that. If the prove signals turned up a prototype result that either confirmed or surprised you, say that. If the listen signals revealed what users are actually doing in the absence of this capability — and that connects to the inertia scenario you named — say that. Omit namespaces that didn't contribute anything material.

---

### S3 — What They Say Together

Now hold all of it at once. What do you see?

This is the hardest paragraph and the most important one. You're not summarizing S2. You're looking for the pattern that only becomes visible when you stop looking at individual namespaces and look at all of them simultaneously. Maybe they all point in the same direction and the convergence is striking. Maybe two namespaces are in tension and the fracture matters. Either way — name it. Say what you see when you look at the whole picture.

---

### S4 — What You Don't Know Yet

Two short paragraphs here.

**S4a — Gaps and uncertainties.** What didn't you fully answer? What namespaces did you skip? What did you learn that raised more questions? Limit this to the things that are actually material — that could change your recommendation if you investigated further.

**S4b — The inertia scenario, spelled out.** This is where you write out the inertia scenario you named at the top. What does the current state actually look like? What does a user or team member experience in the absence of this capability? What's the real cost of staying where things are? Be specific enough that someone who reads this paragraph could explain the status quo to a colleague who hasn't been following the investigation. This is the comparator — your recommendation in S5 has to be better than this.

---

### S5 — Your Recommendation

Three paragraphs.

**First paragraph — the call.** Make the call: proceed, pause, pivot, or abandon. Say why, drawing from what you found in S3. And then engage the inertia scenario from S4b: explain why what you're recommending is actually better than staying in the current state. Don't leave that implicit. The recommendation only lands if the reader understands it as a choice between something and something else.

**Second paragraph — the honest uncertainty.** Pick the strongest thing from S4a — the uncertainty that most threatens your recommendation — and address it directly. Acknowledge why it's material. Then explain either why the recommendation still holds despite it, or what specific thing would have to be true for you to change your call.

**Third paragraph — the action gate.** This is the most practical paragraph in the whole artifact. You're telling the reader exactly when to act and what happens if they don't.

You need three things in this paragraph:

First, name the **trigger** — a specific, identifiable event or signal that means the window is closing. Not "when you feel ready." An actual thing that could happen: a competitor ships, a quarterly plan locks, a key team member is available, a technical dependency resolves. Something you could point to and say "that's the trigger."

Second, name the **action** — the specific thing to do when the trigger fires. Not "take action" or "revisit the decision." The concrete step: what commitment is made, what resources are authorized, what gate is opened.

Third, name the **cost of missing it** — what specifically is forgone if the trigger fires without action. This is different from the general inertia scenario in S4b. This is the particular thing that becomes unavailable or locked-in at that specific trigger point. The cost of missing this trigger, not the general cost of delay. Tie it to the trigger you just named — "if [trigger] fires and we don't act, [specific outcome] is no longer available." That's the inertia consequence at the trigger point.

All three of these need to be in Para 3. If you've only got the trigger and the action, you haven't finished the paragraph yet.

---

### A note on voice

You've been gathering signals for a while. You have a view. Write like it. The author's voice isn't neutral or hedged — it's interpretive and direct. You can acknowledge uncertainty (you should, where it's real), but do it explicitly: "this is uncertain because..." not "there may be some evidence suggesting..."

The reader of this artifact needs to know what you actually think, clearly enough to make a decision. Write toward that.

---

### Save it

Filename: `{{topic}}-story-{{date}}.md`

```yaml
---
topic: {{topic}}
signal: story
date: {{date}}
---
```

Save to: `simulations/topic/{{topic}}-story-{{date}}.md`
