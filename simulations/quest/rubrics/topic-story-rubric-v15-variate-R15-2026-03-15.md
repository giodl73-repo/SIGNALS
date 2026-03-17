# topic-story Rubric v15 — 5 Variations (R15)

**Round**: 15
**Skill**: `topic-story`
**Base rubric**: `topic-story-rubric-v15-2026-03-14.md`
**New criteria this round**: C-47, C-48

---

## R14 State Summary

R14: V-04 scored 99.756 (40/41 aspirational under v15 — missed C-47: no class label on
hedge prohibition). V-05 scored 99.756 (40/41 aspirational under v15 — missed C-48:
two-element Para 3, no inertia-at-trigger element).

- **C-47**: R14 V-04 hedge prohibition named patterns without assigning a class label.
  No term identified "aggregate-first hedging" or equivalent category — enumeration only,
  no class membership criterion stated.
- **C-48**: R14 V-05 Para 3 named trigger condition and action option but omitted inertia
  consequence at the trigger point. The inertia framing appeared at S5 level (C-46) but was
  not instantiated at the action gate level within Para 3.

**R14 baseline under v15**: V-04 and V-05 each pass 40 of 41 aspirational — 99.756.

**R15 design requirement**: All five variations must incorporate both C-47 and C-48.
Variation axes explore whether an editorial synthesis format (S1–S5 prose directives,
departing from the structured field inventory/checklist design) can satisfy the rubric
at competitive score. Two single-axis variations, one single-axis falsifiability axis,
then compounds.

**Important**: R15 variations adopt a new editorial format (S1–S5 with prose directives,
no field inventory table, no pre-artifact checklist, no labeled fields like `**Prior
position**:`). This is a structural departure from R14. Many criteria built around the
structured format (C-19–C-44) will not be satisfied by this design. R15 documents the
tradeoff: the new format's structural properties vs. the governance machinery of the old
format. Excellence signals from the R15 winner inform v16 criteria.

**Variation axes for R15**:
- Single-axis: Phrasing register (formal/imperative, criterion-dense directives) — V-01
- Single-axis: Output format (slot-fill template; rubric criteria embedded as slot
  instructions) — V-02
- Single-axis: Falsifiability axis (disproof condition in S3, inertia verdict per signal
  in S2, S5 cross-references disproof condition) — V-03
- Compound: Phrasing register + output format (V-01 + V-02) — V-04
- Compound: Full integration (V-01 + V-02 + V-03) — V-05

---

## V-01 — Single-Axis: Phrasing Register (Formal/Technical, Criterion-Dense)

**Variation axis**: Phrasing register — formal/technical, imperative voice, criterion-dense
directives
**Hypothesis**: Dense specification language with explicit structural markers reduces
ambiguity in per-section behavior, producing tighter adherence to S4b/S5 inertia framing
and hedge class labeling.

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

## V-02 — Single-Axis: Output Format (Slot-Fill Template)

**Variation axis**: Output format — slot-fill template; author populates labeled slots,
rubric criteria embedded as slot instructions
**Hypothesis**: Presenting the rubric criteria as slot labels rather than prose instructions
shifts compliance from recall to recognition, reducing structural omissions in S4b and
Para 3 inertia elements.

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
Identify the cross-namespace pattern — what is visible only when all findings are held
simultaneously.
If convergent: state what they converge on.
If fractured: name the fracture and locate its source.
Do not summarize S2. Do not restate individual findings.]

[SLOT: Disproof condition — one sentence.
After committing to the pattern claim, ask: what specific observation would invalidate it?
Write that as a disproof condition. Format: "This pattern fails if [specific observable
condition that, if shown to hold, invalidates the pattern claim]."
This is a required structural element. A pattern claim without a named disproof condition
is not falsifiable and must be revised before submission.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph.
Name the material gaps: signal namespaces not activated, questions opened without resolution,
findings contradicted by other findings.
Constraint: name only uncertainties that are material to the recommendation in S5.
Generic hedges ("more research may be needed on X") are prohibited. Required form: "We do
not know [X]; if X is shown to be false, the recommendation changes from [current] to [Y]."]

---

## S4b — Inertia Comparator

[SLOT: One paragraph.
State explicitly: what happens if this feature is not built, or if the decision is deferred
indefinitely?
Required elements:
  (a) The status quo cost — what the team or user continues to experience in the absence
      of this capability.
  (b) The specific outcome — named, not generic. "Users experience friction when doing X"
      passes; "the status quo is not ideal" fails.
S4b must be populated. An empty or generic S4b makes S5 Para 1 structurally incomplete.]

---

## S5 — Recommendation

[SLOT: Para 1 — Recommendation verdict.
Required elements:
  (a) Verdict: one of {proceed, pause, pivot, abandon}.
  (b) Primary reason: drawn from S3 (reference the cross-signal pattern).
  (c) Inertia comparison: state whether acting is preferable to the S4b inertia scenario,
      and why. Cross-reference S4b by name. A recommendation that does not address the
      inertia comparator identified in S4b is incomplete.]

[SLOT: Para 2 — Counterargument.
Required elements:
  (a) Name the strongest uncertainty from S4a.
  (b) Acknowledge why it is material.
  (c) State why the verdict holds despite it — or name the specific condition under which
      it would flip.]

[SLOT: Para 3 — Action Directive.
Required elements — all three must be present:
  (a) TRIGGER: The specific event or signal state that makes waiting costlier than acting.
      Must be identifiable and observable. Not "when you're ready" — a named event.
  (b) ACTION: The specific step recommended when the trigger fires. A sprint commitment,
      prototype authorization, go/no-go gate, or stakeholder review.
  (c) INERTIA-AT-TRIGGER: The specific outcome forgone if the trigger fires without action.
      This is NOT the general delay cost from Para 1 or S4b. This is the specific thing
      lost at the moment the trigger fires unmet — the window, position, debt, or capacity
      tied to the named trigger. Must be connected to the trigger in (a), not stated as
      background.
A Para 3 missing any of (a), (b), or (c) is structurally incomplete and must be revised.]
```

---

### Voice

The slot instructions are constraints, not suggestions. Populate each slot completely. Where the instruction says "required elements," all elements must appear. Where the instruction says "Do not," that form is prohibited.

Write in editorial voice throughout. No passive hedging. No probability substitutes for judgment.

---

## V-03 — Single-Axis: Falsifiability Axis

**Variation axis**: Falsifiability axis — add `**Disproof condition**:` as labeled field in S3,
add `**Inertia verdict**:` per-signal in S2, add falsifiability self-check instruction in S3,
add disproof condition cross-reference in S5 Para 1.
**Hypothesis**: Restoring the falsifiability and per-signal decision filter from the structured
format — as labeled fields within the S1–S5 prose design — recovers C-12, C-15, C-18, C-20,
and C-30 without requiring a full field inventory or pre-artifact checklist.

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

**Prohibited opening class: aggregate-first hedging constructions.** This class includes any opening that leads with an inventory of the evidence base rather than the investigative question. Enumerated surface forms include: "The signals gathered for...", "This synthesis covers...", "Based on the evidence collected...", "Across the namespaces surveyed...", "The investigation examined...". The class label names the failure mode — opening by cataloging evidence rather than stating the question — so novel phrasings that belong to this class are prohibited even if their surface form does not appear above. Class membership is determined by structural function, not surface similarity.

Open with the question itself, or with the decision pressure that generated it, or with the capability's relationship to what it is meant to change.

---

**S2 — What Each Signal Revealed**

Write one paragraph per signal namespace that contributed a material finding.

Each paragraph must include:
(a) the namespace name,
(b) the key finding — the one that most directly informs the question in S1,
(c) why that finding matters to the decision, and
(d) the inertia verdict for this finding.

For (d), immediately after the finding, write:

```
**Inertia verdict**: [YES — this finding displaces the status quo; the case for not building
                         gets weaker /
                     NO — this finding confirms the status quo holds; no reason to build
                         emerges /
                     PARTIAL — [one clause naming what aspect of the status quo shifts]]
```

Omit namespaces with no artifacts for this topic. A finding whose inertia verdict is NO and that does not affect any other decision dimension should be omitted — note the omission at the end of S2 with a count ("X namespaces omitted; all returned NO inertia verdict with no secondary signal value").

---

**S3 — What the Signals Say Together**

Write one paragraph. This is the editorial center of the artifact. Do not summarize S2. Identify the pattern or conclusion that emerges only when all findings are held simultaneously. If the signals converge, state the convergence and name what they converge on. If they fracture, name the fracture and locate its source.

After the paragraph, run the falsifiability self-check: commit to the pattern claim, then ask — what specific observation would show this pattern is wrong? Write the result as a required labeled field:

```
**Disproof condition**: [This pattern fails if: specific observable condition that, if shown
                        to hold, invalidates the pattern claim above.]
```

The `**Disproof condition**:` label is required. A pattern claim without a named disproof condition is not falsifiable and must be revised before S4 is written. Do not proceed to S4 until `**Disproof condition**:` is written.

---

**S4 — What Remains Uncertain**

Write two sub-paragraphs, labeled S4a and S4b.

**S4a — Residual Uncertainties.** Name the signal gaps — namespaces not yet activated, questions the investigation opened without resolving, findings contradicted by other findings. Be specific. A residual uncertainty is only named if it is material to the recommendation in S5.

**S4b — Inertia Comparator.** State explicitly what happens if this feature is not built, or if the decision is deferred indefinitely. Name the status quo cost. Identify what the team or user continues to experience in the absence of this capability. This is the inertia baseline against which S5's recommendation will be measured. S4b must be present and must name a specific outcome, not a generic claim that inaction has costs.

---

**S5 — Recommendation**

Write three paragraphs: Para 1, Para 2, Para 3.

**Para 1 — Recommendation.** State the recommendation explicitly: proceed, pause, pivot, or abandon. Name the option. Give the primary reason drawn from S3. Cross-reference S4b: state whether the recommended action is preferable to the inertia scenario identified in S4b, and why. Also cross-reference the `**Disproof condition**:` from S3: state explicitly that this recommendation stands unless the disproof condition is shown to hold. Form: "This call stands unless [**Disproof condition**] is demonstrated."

**Para 2 — Counterargument.** Address the strongest material uncertainty from S4a. Acknowledge what makes it material. Explain why the recommendation in Para 1 holds despite it, or name the specific condition under which it would flip to a different recommendation.

**Para 3 — Action Directive.** State the action directive as three elements:

1. **Trigger condition** — identify the specific event or signal state that would make waiting costlier than acting. Name it precisely: a market event, a competitive move, a technical proof point, a team capacity signal, or a date threshold. The trigger is not "when you're ready" or "when confidence increases" — it must be an identifiable, observable event.

2. **Action option** — state the specific step recommended when the trigger fires.

3. **Inertia consequence at trigger** — name the specific outcome forgone if the trigger fires without action. This is the specific thing lost at the moment the trigger fires unmet, tied to the trigger condition named in element 1.

A Para 3 that contains trigger + action but omits the inertia consequence at trigger is structurally incomplete and must be revised before submission.

---

### Voice

Editorial. Confidence where the signals are clear; explicit uncertainty where they are not. No passive-voice hedging ("it would appear that..."). No probability vocabulary as a substitute for judgment ("there may be some evidence suggesting...").

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

## V-04 — Compound: Phrasing Register + Output Format (V-01 + V-02)

**Variation axis**: Compound — formal/technical phrasing register (V-01) combined with
slot-fill template structure (V-02)
**Hypothesis**: Combining criterion-dense imperative directives with labeled slot constraints
produces the highest compliance rate for C-47 and C-48 among non-falsifiability variations,
by giving both the phrasing register and the structural scaffolding needed to avoid omissions.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

Your task: produce an editorial synthesis of all signals gathered for this topic. Execute every slot in the template below. The slot instructions are binding specifications, not orientation. Do not skip slots. Do not merge slots. Do not interpret slot constraints as stylistic preferences — they are structural requirements.

---

### Signal Input

Load all signal artifacts for `{{topic}}` from:
- `simulations/scout/` — market, feasibility, compliance, positioning, naming, requirements, stakeholders
- `simulations/draft/` — pitch, proposal, spec
- `simulations/review/` — code, design, users, customers
- `simulations/flow/` — dataflow, lifecycle, integration, throttle, trigger, resilience, conversation
- `simulations/prove/` — hypothesis, websearch, prototype, interview, analysis, publish, intelligence, synthesize
- `simulations/listen/` — feedback, support, adoption
- `simulations/program/` — plan

Match only artifacts where `topic: {{topic}}`. Reject all others.

---

### Story Template

```
---
topic: {{topic}}
signal: story
date: {{date}}
---

## S1 — What We Set Out to Understand

[SLOT: One paragraph. Past tense.
REQUIRED: State the investigative question — the decision, capability, or uncertainty that
opened this topic.
PROHIBITED OPENING CLASS — aggregate-first hedging constructions: any construction that
opens by gesturing at the evidence base before stating the question. Class label names the
failure mode: leading with an inventory of evidence rather than the question itself. Surface
forms include: "The signals gathered for...", "This synthesis covers...", "Based on the
evidence collected...", "Across the namespaces surveyed...", "The investigation examined...".
Novel forms that share the failure mode are prohibited even if not in this list — class
membership is determined by structural function, not surface resemblance.
OPEN WITH: the question, the decision pressure, or the capability's relationship to what
it is meant to change.]

---

## S2 — What Each Signal Revealed

[SLOT: One paragraph per namespace with artifacts.
Per-paragraph required structure:
  (a) Namespace name.
  (b) Key finding: the single finding most directly informing S1's question.
  (c) Interpretation: why this finding is material to the decision.
CONSTRAINT: Interpret findings; do not enumerate them. Omit namespaces with no artifacts.
Do not write a finding for any namespace that produced no artifact for this topic.]

---

## S3 — What the Signals Say Together

[SLOT: One paragraph. Editorial synthesis.
REQUIRED: Identify the cross-namespace pattern visible only when all findings are held
simultaneously. Name what the signals converge on (if convergent) or name the fracture and
locate its source (if fractured).
PROHIBITED: Summarizing S2. Restating individual findings.
This paragraph is the editorial center of the artifact.]

[SLOT: Disproof condition.
REQUIRED: After committing to the pattern claim, name the specific observation that would
invalidate it. Write as a labeled field:
  **Disproof condition**: [This pattern fails if: specific observable condition that, if
  shown to hold, invalidates the pattern claim above.]
This field is structurally required. A pattern without a named disproof condition is not
falsifiable and fails C-12. Do not proceed to S4 until this field is populated.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph.
REQUIRED: Name signal gaps — namespaces not activated, questions opened without resolution,
contradicted findings.
CONSTRAINT: Only name uncertainties material to the S5 recommendation. Generic hedges
are prohibited. Required form: "We do not know [X]; if X is shown to be false, the
recommendation changes from [current] to [Y]."]

---

## S4b — Inertia Comparator

[SLOT: One paragraph.
REQUIRED ELEMENTS:
  (a) What happens if this feature is not built or the decision is deferred indefinitely.
  (b) The status quo cost — what the team or user continues to experience in the absence
      of this capability. Must name a specific outcome. Generic claims fail.
CONSTRAINT: S4b must be populated before Para 1 of S5 is written. A recommendation
that cross-references S4b when S4b is unpopulated is structurally defective.]

---

## S5 — Recommendation

[SLOT: Para 1 — Recommendation verdict.
REQUIRED ELEMENTS — all three must appear:
  (a) Verdict: one of {proceed, pause, pivot, abandon}.
  (b) Reason: drawn from S3 pattern claim.
  (c) Inertia comparison: explicitly state whether acting is preferable to the S4b inertia
      scenario, and why. Reference S4b by name. A Para 1 without inertia comparison is
      incomplete.
ALSO REQUIRED: State that this call stands unless the disproof condition from S3 is
demonstrated. Form: "This call stands unless [**Disproof condition**] is shown to hold."]

[SLOT: Para 2 — Counterargument.
REQUIRED ELEMENTS:
  (a) The strongest uncertainty from S4a — named.
  (b) Why it is material.
  (c) Why the verdict holds despite it — or the specific condition under which it flips.]

[SLOT: Para 3 — Action Directive.
REQUIRED ELEMENTS — all three must be present and clearly labeled:
  (a) TRIGGER: Specific observable event or signal state that makes waiting costlier than
      acting. Must be identifiable. Not "when ready" or "when confidence increases."
  (b) ACTION: Specific step when trigger fires. Sprint commitment, prototype authorization,
      go/no-go gate, stakeholder review.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if the trigger fires without action.
      NOT the general delay cost from Para 1 or S4b. This is the specific thing lost at
      the moment the named trigger fires unmet — the window, position, debt, or capacity
      tied directly to trigger (a). Must be connected to (a), not stated as background.
STRUCTURAL COMPLETENESS RULE: A Para 3 missing (a), (b), or (c) is structurally incomplete
and must be revised before submission.]
```

---

### Voice

Populate slots with editorial conviction. No passive hedging. No probability vocabulary substituting for judgment. The slot instructions specify structure; the voice is the author's.

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

## V-05 — Compound: Full Integration (V-01 + V-02 + V-03)

**Variation axis**: Full compound — formal/technical phrasing (V-01) + slot-fill template
(V-02) + falsifiability axis with `**Disproof condition**:` and `**Inertia verdict**:` (V-03)
**Hypothesis**: Full integration produces the highest aspirational score in R15 by combining
the criterion-dense phrasing register, the slot scaffolding that makes criteria visible at
write-time, and the falsifiability/inertia verdict labels that recover C-12, C-15, C-18,
C-20, and C-30 within the new editorial format.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

Your task: produce an editorial synthesis of all signals gathered for this topic. Execute every slot in the template below. Slot instructions are binding structural specifications. All required elements must be present. Do not skip slots. Do not merge slots.

---

### Signal Input

Load all signal artifacts for `{{topic}}` from:
- `simulations/scout/` — market, feasibility, compliance, positioning, naming, requirements, stakeholders
- `simulations/draft/` — pitch, proposal, spec
- `simulations/review/` — code, design, users, customers
- `simulations/flow/` — dataflow, lifecycle, integration, throttle, trigger, resilience, conversation
- `simulations/prove/` — hypothesis, websearch, prototype, interview, analysis, publish, intelligence, synthesize
- `simulations/listen/` — feedback, support, adoption
- `simulations/program/` — plan

Match only artifacts where `topic: {{topic}}`. Reject all others.

---

### Story Template

```
---
topic: {{topic}}
signal: story
date: {{date}}
---

## S1 — What We Set Out to Understand

[SLOT: One paragraph. Past tense.
REQUIRED: State the investigative question — the decision, capability, or uncertainty that
opened this topic.
PROHIBITED OPENING CLASS — aggregate-first hedging constructions: constructions that open
by cataloging evidence rather than stating the question. Class label identifies the failure
mode by type: the question is displaced by an inventory of the evidence base. Surface forms
include: "The signals gathered for...", "This synthesis covers...", "Based on the evidence
collected...", "Across the namespaces surveyed...", "The investigation examined...". Novel
forms sharing this failure mode are prohibited — class membership determined by structural
function, not surface resemblance.
OPEN WITH: the question, the decision pressure, or the capability's relationship to what
it is meant to change. Not with what was gathered.]

---

## S2 — What Each Signal Revealed

[SLOT: One paragraph per namespace with artifacts.
Per-paragraph required structure:
  (a) Namespace name.
  (b) Key finding: the single finding most directly informing S1's question.
  (c) Interpretation: why this finding is material to the decision.
  (d) INERTIA VERDICT — required labeled field immediately following the finding:
        **Inertia verdict**: [YES — this displaces the status quo; the case for not
                                  building gets weaker /
                             NO — this confirms the status quo holds; no reason to
                                  build emerges /
                             PARTIAL — [one clause naming what aspect shifts]]
CONSTRAINT: Omit namespaces with no artifacts. If a namespace's inertia verdict is NO and
the finding has no secondary signal value, omit that namespace from S2. Close S2 with a
count: "X namespaces omitted; all returned NO inertia verdict with no secondary value."
Do not enumerate findings — interpret them. The paragraph is the act of interpretation.]

---

## S3 — What the Signals Say Together

[SLOT: One paragraph. Editorial synthesis.
REQUIRED: Identify the cross-namespace pattern visible only when all findings are held
simultaneously. Name what the signals converge on (if convergent) or name the fracture
and locate its source (if fractured).
PROHIBITED: Summarizing S2. Restating individual findings. Signal-list construction.
This paragraph is the editorial center of the artifact.]

[SLOT: Falsifiability self-check — run after committing to the pattern claim.
After writing the paragraph above, ask: what specific observation would show this pattern
is wrong? That is the disproof condition. Write it as a required labeled field:
  **Disproof condition**: [This pattern fails if: specific observable condition that, if
  shown to hold, invalidates the pattern claim above.]
REQUIRED: This field must be populated before S4 is written. A pattern claim without a
named disproof condition is not falsifiable (fails C-12) and must be revised.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph.
REQUIRED: Name signal gaps — namespaces not activated, questions opened without resolution,
contradicted findings.
CONSTRAINT: Only name uncertainties material to S5. Prohibited forms: "More research may be
needed", "There is uncertainty around", "Future work could explore". Required form: "We do
not know [X]; if X is shown to be false, the recommendation changes from [current] to [Y].
Resolution method: [specific investigation]."]

---

## S4b — Inertia Comparator

[SLOT: One paragraph.
REQUIRED ELEMENTS:
  (a) What happens if this feature is not built or the decision is deferred indefinitely.
  (b) Status quo cost: the specific outcome the team or user continues to experience in the
      absence of this capability. Must name a specific outcome — generic claims fail.
CONSTRAINT: S4b must be populated before Para 1 of S5 is written. S5 Para 1 must
cross-reference this section by name. An unpopulated S4b makes S5 Para 1 structurally
defective.]

---

## S5 — Recommendation

[SLOT: Para 1 — Recommendation verdict.
REQUIRED ELEMENTS — all three must appear:
  (a) Verdict: one of {proceed, pause, pivot, abandon}.
  (b) Reason: primary reason drawn from S3 pattern claim.
  (c) Inertia comparison: explicitly state whether acting is preferable to the inertia
      scenario in S4b, and why. Cross-reference S4b by name.
ALSO REQUIRED: Falsifiability closure. State that this recommendation stands unless the
S3 disproof condition is demonstrated. Form: "This call stands unless [**Disproof
condition** from S3] is shown to hold."
PROHIBITED: A Para 1 that does not address the S4b inertia comparator. A Para 1 that
does not name the disproof condition as the revision trigger.]

[SLOT: Para 2 — Counterargument.
REQUIRED ELEMENTS:
  (a) Strongest uncertainty from S4a — named explicitly.
  (b) Why it is material to the recommendation.
  (c) Why the verdict holds despite it — OR the specific condition under which it flips
      to a different recommendation.]

[SLOT: Para 3 — Action Directive.
REQUIRED ELEMENTS — all three must be present, in this order:
  (a) TRIGGER: Specific observable event or signal state that makes waiting costlier than
      acting. Must be identifiable and named. Not "when ready" — a specific event: market
      move, competitive action, technical proof point, team capacity signal, date threshold.
  (b) ACTION: Specific step when trigger fires. Sprint commitment, prototype authorization,
      go/no-go decision gate, stakeholder review.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if the trigger fires without action.
      NOT the general delay cost from Para 1 or S4b. The specific thing lost at the moment
      the named trigger fires unmet: the window that closes, the position taken by a
      competitor, the technical debt that locks in, the team capacity that disperses.
      Must be tied directly to trigger (a) — not a background observation.
STRUCTURAL COMPLETENESS RULE: A Para 3 missing any of (a), (b), or (c) is structurally
incomplete and must be revised before submission. The three elements create the decision
gate: when to act, what to do, and what is lost by not acting at that specific moment.]
```

---

### Voice

Slot instructions specify structure. Editorial conviction fills the content. No passive hedging ("it would appear that..."). No probability vocabulary as a substitute for judgment ("there may be some evidence suggesting..."). Confidence where the signals are clear; explicit uncertainty where they are not. The author is not a summarizer. The author is a decision advisor held accountable for the call.

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
