# Round 17 Variations — `topic-story`

**Round**: 17
**Skill**: `topic-story`
**Base rubric**: `topic-story-rubric-v17-2026-03-14.md`
**New criteria this round**: C-51, C-52

---

## R16 State Summary

R16 produced two excellence signals that became C-51 and C-52 in v17:

- **C-51 (from R16 V-01)**: S4b partitioned into a verdict-inventory stage (Part 1, listing only YES/PARTIAL signals with S2 verdict labels) and a characterization stage (Part 2, explicitly constrained to draw only from Part 1). C-49 fires on content coherence (result legible); C-51 fires on architectural partition (process constrained).

- **C-52 (from R16 V-03)**: Distinct evaluator role or phase must complete S2 as named outputs before the author role or phase begins S4b. C-19 fires on gate mechanism; C-50 fires on slot-embedding; C-52 fires on temporal production order (workflow constraint type).

**R16 baseline under v17**: V-05 passes 25 of 45 aspirational criteria (0 PARTIAL) — 90 + (25 × 0.2222) = **95.56**

**R17 design requirement**: All five variations target C-51 and/or C-52. R16 V-05 base machinery (C-01–C-50) is preserved in all variations — the pre-artifact checklist, per-signal inertia verdict, slot-label constraint embedding, disproof condition, S5 Para 3 three-element action directive.

**Variation axes for R17**:
- Single-axis: S4b structural partition (C-51) — V-01
- Single-axis: Evaluator-first named role boundary (C-52) — V-02
- Single-axis: Lifecycle phase diagram (C-52 via phase sequencing rather than named roles) — V-03
- Compound: S4b partition + evaluator-first named role (V-01 + V-02) — V-04
- Compound: All three axes — V-05

**Score predictions under v17**:
- V-01: 26/45 — cracks C-51, misses C-52 (no role boundary). 90 + 5.778 = **95.78**
- V-02: 26/45 — cracks C-52, misses C-51 (S4b unified, no partition). 90 + 5.778 = **95.78**
- V-03: 26/45 — cracks C-52 via phase gating, misses C-51. 90 + 5.778 = **95.78**
- V-04: 27/45 — cracks both C-51 and C-52. 90 + 6.0 = **96.00**
- V-05: 27+/45 — cracks C-51, C-52; phase lifecycle structure may crack one additional criterion from the lifecycle/phase domain. 90 + 6.0+ = **96.00+**

**Discrimination at R17**: V-01/V-02/V-03 tie at 95.78; V-04 at 96.00; V-05 is the R17 ceiling candidate.

---

## V-01 — Single-Axis: S4b Structural Partition (C-51)

**Variation axis**: S4b structural partition — C-51 target
**Hypothesis**: Replacing the unified S4b inertia slot with a two-stage structure — Part 1 (verdict inventory: only YES/PARTIAL signals from S2 with explicit verdict labels) followed by Part 2 (characterization: a co-located constraint phrase prohibiting direct reference to signals outside Part 1) — cracks C-51 while preserving all C-01–C-50 compliance from R16 V-05. S3 is preserved as a lightweight pattern connector. Part 2 absorbs the inertia framing previously carried by the old unified S4b. No evaluator role boundary is introduced; workflow remains single-role, single-pass. Prediction: 26/45 — C-51 passes, C-52 fails (no role or phase boundary in the workflow structure).

---

You are executing the `topic-story` skill for topic `{{topic}}`.

Your task: produce an editorial synthesis of all signals gathered for this topic. Execute every slot in the template below. Slot instructions are binding specifications. Do not skip slots. Do not merge slots. Do not interpret slot constraints as stylistic preferences — they are structural requirements.

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

### Pre-Artifact Checklist

Before writing, verify:
- [ ] Namespaces scanned; artifacts for `{{topic}}` identified
- [ ] Every S2 paragraph will include an explicit `**Inertia verdict**:` field
- [ ] S3 will include a `**Disproof condition**:` labeled field
- [ ] S4a will name only uncertainties material to the S5 recommendation
- [ ] S4b Part 1 will list only YES/PARTIAL signals from S2 with S2 verdict labels
- [ ] S4b Part 2 will draw only from Part 1 — no direct reference to signals outside Part 1
- [ ] S5 Para 1 will name the verdict, the S3 pattern, the S4b Part 2 inertia comparison, and the disproof condition cross-reference
- [ ] S5 Para 3 will contain all three elements: TRIGGER, ACTION, INERTIA-AT-TRIGGER

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
forms: "The signals gathered for...", "This synthesis covers...", "Based on the evidence
collected...", "Across the namespaces surveyed...", "The investigation examined...". Novel
forms that share the failure mode are prohibited — class membership is determined by
structural function, not surface resemblance.
OPEN WITH: the question, the decision pressure, or the capability's relationship to what it
is meant to change.]

---

## S2 — What Each Signal Revealed

[SLOT: One paragraph per namespace with artifacts for this topic.
Per-paragraph required structure:
  (a) Namespace name.
  (b) Key finding: the single finding most directly informing S1's question.
  (c) Interpretation: why this finding is material to the decision.
  (d) Inertia verdict — write immediately after the finding:
      **Inertia verdict**: [YES — this finding displaces the status quo; the case for not
                               building gets weaker /
                           NO — this finding confirms the status quo holds; no reason to build
                               emerges /
                           PARTIAL — [one clause naming what aspect of the status quo shifts]]
CONSTRAINT: Interpret findings; do not enumerate them. Omit namespaces with no artifacts.
A namespace paragraph that omits **Inertia verdict**: fails C-18.
Namespaces with NO inertia verdict and no secondary signal value should be noted at the
end of S2 with a count ("X namespaces omitted; all NO with no secondary signal value").]

---

## S3 — What the Signals Say Together

[SLOT: One paragraph. Editorial synthesis.
REQUIRED: Identify the cross-namespace pattern visible only when all findings are held
simultaneously. Name what the signals converge on (if convergent) or name the fracture and
locate its source (if fractured).
PROHIBITED: Summarizing S2. Restating individual findings.]

[SLOT: Disproof condition — REQUIRED structural element.
After committing to the pattern claim, ask: what specific observation would invalidate it?
Write as a labeled field:
  **Disproof condition**: [This pattern fails if: specific observable condition that, if
                          shown to hold, invalidates the pattern claim above.]
A pattern without a named disproof condition is not falsifiable. Do not proceed to S4 until
this field is populated.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph.
REQUIRED: Name signal gaps — namespaces not activated, questions opened without resolution,
contradicted findings.
CONSTRAINT: Only name uncertainties material to the S5 recommendation.
REQUIRED FORM: "We do not know [X]; if X is shown to be false, the recommendation changes
from [current] to [Y]."
Generic hedges ("more research may be needed") are prohibited.]

---

## S4b — Signal Characterization

[SLOT: This section has two parts. Complete Part 1 before writing Part 2. Do not merge parts.
The two-part structure is a compliance architecture — an evaluator will check whether
the partition exists and whether Part 2's inputs are formally constrained to Part 1.]

### S4b Part 1 — Verdict Inventory

[SLOT: Enumerate only signals that received YES or PARTIAL inertia verdicts in S2.
REQUIRED FORMAT per entry:
  - {namespace}/{signal-skill} (S2 verdict: YES)
  - {namespace}/{signal-skill} (S2 verdict: PARTIAL — [one-clause qualifier from S2])
CONSTRAINT: NO-verdict signals are excluded. Do not introduce signals not evaluated in S2.
Do not add interpretive prose — enumeration only.
A Part 1 that includes NO-verdict signals or signals not present in S2 fails C-51.]

### S4b Part 2 — Characterization

[SLOT: Editorial synthesis.
THIS SECTION DRAWS ONLY FROM PART 1 — NOT FROM AN INDEPENDENT REVIEW OF ALL SIGNALS.
REQUIRED ELEMENTS:
  (a) What the Part 1 signals say together about this feature's readiness. State the pattern
      in the author's voice. Specific, not generic. Three to five sentences.
  (b) The status quo cost — what the team or user continues to experience in the absence of
      this capability, drawn from at least one named Part 1 signal.
PROHIBITED: Introducing signals or evidence not named in Part 1. Direct reference to S2 or
to signals that received NO verdicts. Part 2's scope is bounded by Part 1.
An evaluator verifying C-51 checks whether Part 2 references signals outside Part 1 — any
such reference is a compliance failure regardless of narrative quality.]

---

## S5 — Recommendation

[SLOT: Para 1 — Recommendation verdict.
REQUIRED ELEMENTS — all must appear:
  (a) Verdict: one of {proceed, pause, pivot, abandon}.
  (b) Reason: drawn from S3 pattern claim. Name the S3 pattern.
  (c) Inertia comparison: state whether acting is preferable to the S4b Part 2 inertia
      scenario, and why. Reference S4b Part 2 by name.
  (d) Disproof condition cross-reference: "This call stands unless [S3 **Disproof condition**]
      is demonstrated."
A Para 1 missing any of (b), (c), or (d) is structurally incomplete.]

[SLOT: Para 2 — Counterargument.
REQUIRED ELEMENTS:
  (a) The strongest uncertainty from S4a — named.
  (b) Why it is material.
  (c) Why the verdict holds despite it — or the specific condition under which it flips.]

[SLOT: Para 3 — Action Directive.
REQUIRED ELEMENTS — all three must be present:
  (a) TRIGGER: Specific observable event or signal state that makes waiting costlier than
      acting. Must be identifiable. Not "when ready" or "when confidence increases."
  (b) ACTION: Specific step when trigger fires — sprint commitment, prototype authorization,
      go/no-go gate, or stakeholder review.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if the trigger fires without action.
      NOT the general delay cost from Para 1 or S4b. The specific thing lost at the moment
      the trigger fires unmet, tied to the named trigger in (a).
A Para 3 missing any of (a), (b), or (c) must be revised before submission.]
```

---

### Voice

Editorial. The author has read the signals, formed a view, and is writing in their own voice. Confidence where signals are clear; explicit uncertainty where they are not. No passive-voice hedging ("it would appear that..."). No probability vocabulary as a substitute for judgment ("there may be some evidence suggesting...").

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

## V-02 — Single-Axis: Evaluator-First Named Role Boundary (C-52)

**Variation axis**: Role sequence — evaluator-first named role boundary targeting C-52
**Hypothesis**: Prefixing the prompt with a mandatory `EVALUATOR` role section that must produce S2 as a complete named handoff output before the `AUTHOR` role begins — enforced by an explicit role boundary marker and a prerequisite statement at the AUTHOR section header — cracks C-52 through workflow-level temporal ordering. S4b remains as a unified characterization slot (no structural partition); the inertia comparator content is preserved within S4b. The EVALUATOR label and successor-activity designation create the compliance architecture C-52 requires: two distinct roles, S2 as a named evaluator output, S4b as an author-phase successor activity. Prediction: 26/45 — C-52 passes, C-51 fails (S4b has no structural Part 1/Part 2 partition).

---

You are executing the `topic-story` skill for topic `{{topic}}`.

This task has two roles with a mandatory boundary between them. **EVALUATOR role must complete before AUTHOR role begins.** The production sequence is a structural requirement — not a suggestion about ordering.

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

## EVALUATOR ROLE

Your role is **EVALUATOR**. Read every signal artifact for `{{topic}}`. Produce S2 below as your complete named output for this role. S2 is the evaluator's verdict record — it exists as a discrete produced artifact, not as a checklist or orientation for the author. The AUTHOR role receives S2 as a complete output before S4b authoring begins.

**Do not proceed to AUTHOR ROLE until S2 is fully populated.**

### S2 — Signal Verdict Record (EVALUATOR OUTPUT)

```
[SLOT: One paragraph per namespace with artifacts for this topic. This is the EVALUATOR's
named output. The AUTHOR role receives this record as its S4b input.
Per-paragraph required structure:
  (a) Namespace name.
  (b) Key finding: the single finding most directly informing the investigative question.
  (c) Interpretation: why this finding is material to the decision.
  (d) Inertia verdict — write immediately after the finding:
      **Inertia verdict**: [YES — this finding displaces the status quo; the case for not
                               building gets weaker /
                           NO — this finding confirms the status quo holds /
                           PARTIAL — [one clause naming what aspect of the status quo shifts]]
CONSTRAINT: Interpret findings; do not enumerate them. Omit namespaces with no artifacts.
A paragraph missing **Inertia verdict**: fails C-18.
EVALUATOR NOTE: S2 is a named verdict record. It is complete when every namespace with
artifacts has an inertia verdict. The AUTHOR role's S4b draws from this record.]
```

---

**[EVALUATOR ROLE COMPLETE — S2 IS THE NAMED OUTPUT. PROCEED TO AUTHOR ROLE.]**

---

## AUTHOR ROLE

Your role is **AUTHOR**. S2 is complete above. You may now proceed to the Story Template below.

S2 verdicts exist as named evaluator outputs. S4b is a successor activity to the evaluator role — it draws from the S2 verdict record, not from an independent review of the signal set.

**Pre-Author Checklist** — verify before writing:
- [ ] S2 is complete and every active namespace has an inertia verdict
- [ ] S3 will include a `**Disproof condition**:` labeled field
- [ ] S4a will name only uncertainties material to the S5 recommendation
- [ ] S4b will name its signal inventory from S2 YES/PARTIAL signals (for C-49 chain legibility)
- [ ] S5 Para 1 will include verdict, S3 pattern, S4b inertia comparison, and disproof condition
- [ ] S5 Para 3 will contain all three elements: TRIGGER, ACTION, INERTIA-AT-TRIGGER

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
failure mode: leading with inventory of evidence rather than the question. Surface forms:
"The signals gathered for...", "This synthesis covers...", "Based on the evidence
collected...", "Across the namespaces surveyed...". Class membership is determined by
structural function, not surface resemblance.
OPEN WITH: the question, the decision pressure, or the capability's relationship to what it
is meant to change.]

---

## S3 — What the Signals Say Together

[SLOT: One paragraph. Editorial synthesis.
REQUIRED: Identify the cross-namespace pattern visible only when all S2 findings are held
simultaneously. Name what the signals converge on (if convergent) or name the fracture and
locate its source (if fractured).
PROHIBITED: Summarizing S2. Restating individual findings.]

[SLOT: Disproof condition — REQUIRED structural element.
  **Disproof condition**: [This pattern fails if: specific observable condition that, if
                          shown to hold, invalidates the pattern claim above.]
A pattern without a named disproof condition is not falsifiable. Do not proceed to S4 until
this field is populated.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph.
REQUIRED: Name signal gaps — namespaces not activated, questions opened without resolution,
contradicted findings.
CONSTRAINT: Only name uncertainties material to the S5 recommendation.
REQUIRED FORM: "We do not know [X]; if X is shown to be false, the recommendation changes
from [current] to [Y]."
Generic hedges are prohibited.]

---

## S4b — Signal Characterization

[SLOT: One paragraph. AUTHOR role — successor activity to EVALUATOR S2.
THIS SECTION DRAWS FROM S2 YES/PARTIAL SIGNALS — NOT FROM AN INDEPENDENT REVIEW OF ALL
SIGNALS.
REQUIRED ELEMENTS:
  (a) Name the signals from S2 that received YES or PARTIAL inertia verdicts. Reference the
      S2 verdict record. At least one named signal must be explicitly cross-referenced to its
      S2 YES/PARTIAL verdict.
  (b) What those YES/PARTIAL signals say together about this feature's readiness.
  (c) The status quo cost — what the team or user continues to experience in the absence of
      this capability. Specific outcome required; generic claims fail.
CONSTRAINT: S4b is the author's characterization of what the evaluator's YES/PARTIAL signals
say together. The evaluator's S2 verdicts are the named inputs. An S4b composed without
reference to the S2 verdict record is not a valid successor activity to the evaluator role.]

---

## S5 — Recommendation

[SLOT: Para 1 — Recommendation verdict.
REQUIRED ELEMENTS — all must appear:
  (a) Verdict: one of {proceed, pause, pivot, abandon}.
  (b) Reason: drawn from S3 pattern claim.
  (c) Inertia comparison: state whether acting is preferable to the S4b inertia scenario,
      and why. Reference S4b by name.
  (d) Disproof condition cross-reference: "This call stands unless [S3 **Disproof condition**]
      is demonstrated."
A Para 1 missing any of (b), (c), or (d) is structurally incomplete.]

[SLOT: Para 2 — Counterargument.
REQUIRED ELEMENTS:
  (a) The strongest uncertainty from S4a — named.
  (b) Why it is material.
  (c) Why the verdict holds despite it — or the condition under which it flips.]

[SLOT: Para 3 — Action Directive.
REQUIRED ELEMENTS — all three must be present:
  (a) TRIGGER: Specific observable event or signal state that makes waiting costlier than
      acting. Must be identifiable. Not "when ready."
  (b) ACTION: Specific step when trigger fires.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if trigger fires without action. NOT the
      general delay cost. The specific thing lost at the moment the trigger fires unmet.
A Para 3 missing any of (a), (b), or (c) must be revised before submission.]
```

---

### Voice

Editorial. No passive-voice hedging. No probability vocabulary as a substitute for judgment. The author has received the evaluator's S2 verdicts and is writing to explain what they reveal and what the decision-maker should do.

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

## V-03 — Single-Axis: Lifecycle Phase Diagram (C-52 via Phase Sequencing)

**Variation axis**: Lifecycle emphasis — C-52 via phase sequencing rather than named roles
**Hypothesis**: Restructuring the entire prompt as a five-phase lifecycle diagram (DISCOVER → EVALUATE → SYNTHESIZE → CHARACTERIZE → RECOMMEND) with explicit phase prerequisite gates cracks C-52 through phase-sequence enforcement rather than named role labels. Each phase has a named output and a "prerequisite: prior phase complete" header. Phase 2 (EVALUATE) produces S2 as its named output; Phase 4 (CHARACTERIZE) begins S4b as a designated successor to Phase 2's output. This mechanism is architecturally distinct from both the named-role approach (V-02) and the slot-embedding approach (C-50): it enforces temporal ordering through phase structure rather than role assignment or content constraints. Prediction: 26/45 — C-52 passes via phase gating, C-51 fails (no S4b two-part partition).

---

You are executing the `topic-story` skill for topic `{{topic}}`.

This task proceeds through five phases. Each phase has a named output and a prerequisite. **Do not begin a phase before its prerequisite is satisfied.** The phase sequence is a structural requirement — not a stylistic preference.

---

### Phase Overview

```
PHASE 1 — DISCOVER    → output: signal inventory
PHASE 2 — EVALUATE    → output: S2 verdict record (prerequisite for Phase 4)
PHASE 3 — SYNTHESIZE  → output: S3 pattern + disproof condition
PHASE 4 — CHARACTERIZE → output: S4a + S4b (prerequisite: Phase 2 complete)
PHASE 5 — RECOMMEND   → output: S5 (prerequisite: Phases 2, 3, 4 complete)
```

---

## PHASE 1 — DISCOVER

**Prerequisite**: None.
**Output**: Signal inventory — list of namespaces with artifacts for `{{topic}}`.

Load all signal artifacts for `{{topic}}` from:
- `simulations/scout/` — market, feasibility, compliance, positioning, naming, requirements, stakeholders
- `simulations/draft/` — pitch, proposal, spec
- `simulations/review/` — code, design, users, customers
- `simulations/flow/` — dataflow, lifecycle, integration, throttle, trigger, resilience, conversation
- `simulations/prove/` — hypothesis, websearch, prototype, interview, analysis, publish, intelligence, synthesize
- `simulations/listen/` — feedback, support, adoption
- `simulations/program/` — plan

Match only artifacts where `topic: {{topic}}`. Identify which namespaces have artifacts. Phase 1 output: list of active namespaces.

**Phase 1 complete when**: all namespaces scanned and active namespace list exists.

---

## PHASE 2 — EVALUATE

**Prerequisite**: Phase 1 complete (signal inventory exists).
**Output**: S2 — Signal Verdict Record. This is the named output of the evaluate phase. It exists as a discrete produced artifact before Phase 4 begins.

For each active namespace from Phase 1, produce one paragraph:

```
[SLOT — S2 per-namespace evaluation:
  (a) Namespace name.
  (b) Key finding: the single finding most directly informing the investigative question.
  (c) Interpretation: why this finding is material to the decision.
  (d) **Inertia verdict**: [YES — displaces status quo / NO — confirms status quo holds /
                            PARTIAL — [one clause naming what shifts]]
A paragraph missing **Inertia verdict**: fails C-18.
S2 is a verdict record — every active namespace must have an inertia verdict before Phase 4
begins. Phase 2 is not complete until all active namespaces have been evaluated.]
```

**Phase 2 complete when**: S2 verdict record exists with inertia verdicts for every active namespace. Do not begin Phase 4 before this condition is satisfied.

---

## PHASE 3 — SYNTHESIZE

**Prerequisite**: Phase 2 complete (S2 verdict record exists).
**Output**: S1 (investigative framing) + S3 (cross-namespace pattern + disproof condition).

```
[SLOT — S1: What We Set Out to Understand
One paragraph. Past tense.
REQUIRED: State the investigative question — the decision, capability, or uncertainty that
opened this topic.
PROHIBITED OPENING CLASS — aggregate-first hedging constructions: openings that gesture at
the evidence base before stating the question. Class label names the failure mode: leading
with inventory of evidence rather than the question. Surface forms: "The signals gathered
for...", "This synthesis covers...", "Based on the evidence collected...". Class membership
is determined by structural function, not surface resemblance.
OPEN WITH: the question, the decision pressure, or the capability's relationship to what it
is meant to change.]

[SLOT — S3: What the Signals Say Together
One paragraph. Editorial synthesis of Phase 2 findings.
REQUIRED: Identify the cross-namespace pattern visible only when all S2 findings are held
simultaneously. Name what the signals converge on (if convergent) or name the fracture and
locate its source (if fractured).
PROHIBITED: Summarizing S2. Restating individual namespace findings.]

[SLOT — S3 Disproof Condition: REQUIRED structural element.
  **Disproof condition**: [This pattern fails if: specific observable condition that, if
                          shown to hold, invalidates the pattern claim above.]
Phase 3 is not complete until **Disproof condition**: is populated.]
```

**Phase 3 complete when**: S1 paragraph and S3 paragraph with labeled `**Disproof condition**:` exist.

---

## PHASE 4 — CHARACTERIZE

**Prerequisite**: Phase 2 complete (S2 verdict record exists). S4b is a successor activity to the Phase 2 evaluate output — it draws from S2 YES/PARTIAL signals as named Phase 2 artifacts.
**Output**: S4a (residual uncertainties) + S4b (signal characterization).

```
[SLOT — S4a: Residual Uncertainties
One paragraph.
REQUIRED: Name signal gaps material to the Phase 5 recommendation.
REQUIRED FORM: "We do not know [X]; if X is shown to be false, the recommendation changes
from [current] to [Y]."
Generic hedges prohibited.]

[SLOT — S4b: Signal Characterization
One paragraph. Phase 4 output — draws from Phase 2 S2 YES/PARTIAL signals as named inputs.
REQUIRED ELEMENTS:
  (a) Name the signals from Phase 2 S2 that received YES or PARTIAL inertia verdicts.
      At least one named signal explicitly cross-referenced to its S2 YES/PARTIAL verdict.
  (b) What those signals say together about this feature's readiness.
  (c) The status quo cost — specific outcome the team or user experiences in the absence of
      this capability, drawn from at least one named S2 YES/PARTIAL signal.
CONSTRAINT: S4b is formally downstream of Phase 2. Its named signal inventory is the Phase 2
verdict record. An S4b composed without reference to Phase 2 S2 outputs is not a valid
Phase 4 artifact.]
```

**Phase 4 complete when**: S4a paragraph and S4b paragraph with named Phase 2 signals exist.

---

## PHASE 5 — RECOMMEND

**Prerequisite**: Phases 2, 3, and 4 complete (S2, S3, S4a, S4b all exist as named phase outputs).
**Output**: S5 (recommendation — three paragraphs).

```
[SLOT — Para 1: Recommendation verdict.
REQUIRED ELEMENTS — all must appear:
  (a) Verdict: one of {proceed, pause, pivot, abandon}.
  (b) Reason: drawn from Phase 3 S3 pattern claim.
  (c) Inertia comparison: state whether acting is preferable to the Phase 4 S4b inertia
      scenario, and why. Reference S4b by name.
  (d) Disproof condition cross-reference: "This call stands unless [S3 **Disproof condition**]
      is demonstrated."
A Para 1 missing any of (b), (c), or (d) is structurally incomplete.]

[SLOT — Para 2: Counterargument.
REQUIRED ELEMENTS:
  (a) The strongest uncertainty from Phase 4 S4a — named.
  (b) Why it is material.
  (c) Why the verdict holds — or the condition under which it flips.]

[SLOT — Para 3: Action Directive.
REQUIRED ELEMENTS — all three must be present:
  (a) TRIGGER: Specific observable event that makes waiting costlier than acting. Named,
      identifiable. Not "when ready."
  (b) ACTION: Specific step when trigger fires.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if trigger fires without action.
      NOT general delay cost. Specific thing lost at the moment the named trigger fires
      unmet.
A Para 3 missing any of (a), (b), or (c) must be revised before submission.]
```

**Phase 5 complete when**: S5 with all three paragraphs exists and Para 3 contains TRIGGER, ACTION, and INERTIA-AT-TRIGGER.

---

### Voice

Editorial throughout all phases. No passive-voice hedging. No probability vocabulary as a substitute for judgment. The Phase 3 synthesis and Phase 5 recommendation are written in the author's voice.

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

## V-04 — Compound: S4b Partition + Evaluator-First (V-01 + V-02)

**Variation axis**: Compound — S4b structural partition (C-51) + evaluator-first named role boundary (C-52)
**Hypothesis**: Combining the EVALUATOR/AUTHOR role boundary (V-02) with the two-part S4b partition (V-01) produces a two-layer enforcement chain for the S2→S4b chain: the EVALUATOR role creates temporal production ordering (C-52) and the S4b Part 1/Part 2 partition creates architectural input-constraint enforcement (C-51). Each mechanism closes a distinct failure mode: C-52 ensures S2 verdicts exist as named artifacts before S4b begins; C-51 ensures S4b's characterization draws only from the Part 1 inventory of YES/PARTIAL signals. Prediction: 27/45 — cracks both C-51 and C-52. 90 + 6.0 = **96.00**.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

This task has two roles with a mandatory boundary between them. **EVALUATOR role must complete before AUTHOR role begins.** The production sequence is a structural requirement.

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

## EVALUATOR ROLE

Your role is **EVALUATOR**. Read every signal artifact for `{{topic}}`. Produce S2 below as your complete named output. S2 is the evaluator's verdict record — a discrete produced artifact that the AUTHOR role receives before beginning S4b. **Do not proceed to AUTHOR ROLE until S2 is fully populated.**

### S2 — Signal Verdict Record (EVALUATOR OUTPUT)

```
[SLOT: One paragraph per namespace with artifacts. EVALUATOR's named output.
Per-paragraph required structure:
  (a) Namespace name.
  (b) Key finding: the single finding most directly informing the investigative question.
  (c) Interpretation: why this finding is material to the decision.
  (d) **Inertia verdict**: [YES — displaces status quo; case for not building weakens /
                            NO — confirms status quo holds; no reason to build /
                            PARTIAL — [one clause naming what shifts]]
CONSTRAINT: Interpret findings; do not enumerate. Omit namespaces with no artifacts.
A paragraph missing **Inertia verdict**: fails C-18.
EVALUATOR NOTE: S2 is complete when every active namespace has an inertia verdict.
The AUTHOR role's S4b Part 1 draws from this verdict record as its exclusive input.]
```

---

**[EVALUATOR ROLE COMPLETE — S2 IS THE NAMED OUTPUT. PROCEED TO AUTHOR ROLE.]**

---

## AUTHOR ROLE

Your role is **AUTHOR**. S2 is complete above. You may now proceed to the Story Template.

S2 verdicts exist as named evaluator outputs. S4b Part 1 draws from this record as its exclusive input. S4b Part 2 draws only from Part 1. The chain is: EVALUATOR S2 → S4b Part 1 → S4b Part 2.

**Pre-Author Checklist** — verify before writing:
- [ ] S2 is complete; every active namespace has an inertia verdict
- [ ] S3 will include a `**Disproof condition**:` labeled field
- [ ] S4a will name only uncertainties material to the S5 recommendation
- [ ] S4b Part 1 will list only YES/PARTIAL signals from EVALUATOR S2, with verdict labels
- [ ] S4b Part 2 will draw only from Part 1 — constraint phrase co-located within Part 2 slot
- [ ] S5 Para 1 will include verdict, S3 pattern, S4b Part 2 inertia comparison, and disproof condition
- [ ] S5 Para 3 will contain all three elements: TRIGGER, ACTION, INERTIA-AT-TRIGGER

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
failure mode: leading with inventory of evidence rather than the question. Surface forms:
"The signals gathered for...", "This synthesis covers...", "Based on the evidence
collected...", "Across the namespaces surveyed...". Class membership is structural function,
not surface resemblance.
OPEN WITH: the question, the decision pressure, or the capability's relationship to what it
is meant to change.]

---

## S3 — What the Signals Say Together

[SLOT: One paragraph. Editorial synthesis.
REQUIRED: Identify the cross-namespace pattern visible only when all S2 findings are held
simultaneously. Name what they converge on (if convergent) or name the fracture and locate
its source (if fractured).
PROHIBITED: Summarizing S2. Restating individual namespace findings.]

[SLOT: Disproof condition — REQUIRED structural element.
  **Disproof condition**: [This pattern fails if: specific observable condition that, if
                          shown to hold, invalidates the pattern claim above.]
Do not proceed to S4 until this field is populated.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph.
REQUIRED: Name signal gaps material to the S5 recommendation.
REQUIRED FORM: "We do not know [X]; if X is shown to be false, the recommendation changes
from [current] to [Y]."
Generic hedges prohibited.]

---

## S4b — Signal Characterization

[SLOT: This section has two parts. Complete Part 1 before writing Part 2. Do not merge parts.
The EVALUATOR's S2 verdict record is the input to Part 1. Part 2 draws only from Part 1.
This is a two-layer enforcement chain: EVALUATOR S2 → Part 1 (inventory) → Part 2 (synthesis).]

### S4b Part 1 — Verdict Inventory (draws from EVALUATOR S2)

[SLOT: Enumerate only signals that received YES or PARTIAL inertia verdicts in EVALUATOR S2.
REQUIRED FORMAT per entry:
  - {namespace}/{signal-skill} (S2 verdict: YES)
  - {namespace}/{signal-skill} (S2 verdict: PARTIAL — [qualifier from EVALUATOR S2])
CONSTRAINT: NO-verdict signals are excluded. Do not introduce signals not in EVALUATOR S2.
Enumeration only — no interpretive prose in Part 1.
A Part 1 that includes NO-verdict signals or signals outside the EVALUATOR S2 record fails C-51.]

### S4b Part 2 — Characterization (draws only from Part 1)

[SLOT: Editorial synthesis.
THIS SECTION DRAWS ONLY FROM PART 1 — NOT FROM AN INDEPENDENT REVIEW OF ALL SIGNALS.
REQUIRED ELEMENTS:
  (a) What the Part 1 signals say together about this feature's readiness. Author's voice.
      Specific, not generic. Three to five sentences.
  (b) The status quo cost — what the team or user continues to experience without this
      capability, drawn from at least one named Part 1 signal.
PROHIBITED: Introducing signals not in Part 1. Direct reference to EVALUATOR S2 or the full
signal set. Part 2's scope is bounded by Part 1.
COMPLIANCE NOTE: An evaluator verifying C-51 checks whether Part 2 references signals outside
Part 1. Any such reference is a compliance failure regardless of narrative quality.]

---

## S5 — Recommendation

[SLOT: Para 1 — Recommendation verdict.
REQUIRED ELEMENTS — all must appear:
  (a) Verdict: one of {proceed, pause, pivot, abandon}.
  (b) Reason: drawn from S3 pattern claim.
  (c) Inertia comparison: state whether acting is preferable to S4b Part 2 inertia scenario,
      and why. Reference S4b Part 2 by name.
  (d) Disproof condition cross-reference: "This call stands unless [S3 **Disproof condition**]
      is demonstrated."
A Para 1 missing any of (b), (c), or (d) is structurally incomplete.]

[SLOT: Para 2 — Counterargument.
REQUIRED ELEMENTS:
  (a) The strongest uncertainty from S4a — named.
  (b) Why it is material.
  (c) Why the verdict holds — or the condition under which it flips.]

[SLOT: Para 3 — Action Directive.
REQUIRED ELEMENTS — all three must be present:
  (a) TRIGGER: Specific observable event that makes waiting costlier than acting. Named,
      identifiable. Not "when ready."
  (b) ACTION: Specific step when trigger fires.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if trigger fires without action.
      NOT general delay cost. Specific thing lost at the moment the named trigger fires unmet.
A Para 3 missing any of (a), (b), or (c) must be revised before submission.]
```

---

### Voice

Editorial throughout. No passive-voice hedging. No probability vocabulary as a substitute for judgment. The AUTHOR has received the EVALUATOR's S2 verdict record and writes to explain what the YES/PARTIAL signals say together and what the decision-maker should do.

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

## V-05 — Compound: All Three Axes (V-01 + V-02 + V-03)

**Variation axis**: Full compound — S4b structural partition (C-51) + evaluator-first named role boundary (C-52) + lifecycle phase diagram (additional enforcement layer)
**Hypothesis**: Layering all three mechanisms produces the maximum enforcement architecture for the S2→S4b chain and the maximum compliance surface for R17: (1) the EVALUATOR role boundary creates workflow-level temporal ordering (C-52); (2) S4b Part 1/Part 2 creates architectural input-constraint enforcement (C-51); (3) the phase diagram creates an additional prerequisite-gate layer that expresses the production sequence at the lifecycle level rather than only at the role level. The third layer (phase diagram) is not redundant with C-52 — it operates at a different structural level and may fire additional aspirational criteria in the lifecycle/sequencing domain that are not cracked by either the role boundary or the S4b partition alone. Prediction: 27+/45 — cracks C-51 and C-52; phase lifecycle structure is the excellence signal candidate for R18. 90 + 6.0+ = **96.00+**.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

This task has two roles and five phases. The roles are sequenced: **EVALUATOR** precedes **AUTHOR**. The phases are sequenced: each phase has a named output and a prerequisite. **Do not begin a role or phase before its prerequisite is satisfied.**

---

### Lifecycle Overview

```
EVALUATOR ROLE
  PHASE 1 — DISCOVER    output: signal inventory
  PHASE 2 — EVALUATE    output: S2 verdict record  ← named handoff to AUTHOR

AUTHOR ROLE (begins after Phase 2 complete)
  PHASE 3 — SYNTHESIZE  output: S1 + S3 + disproof condition
  PHASE 4 — CHARACTERIZE output: S4a + S4b Part 1 + S4b Part 2
  PHASE 5 — RECOMMEND   output: S5 Para 1 + Para 2 + Para 3
```

S4b Part 1 is a successor activity to Phase 2. S4b Part 2 is a successor activity to S4b Part 1. The chain is: EVALUATOR Phase 2 S2 → S4b Part 1 (inventory) → S4b Part 2 (characterization). Each link in the chain is a structural dependency — not a stylistic sequencing preference.

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

## EVALUATOR ROLE

---

### PHASE 1 — DISCOVER

**Prerequisite**: None.
**Output**: Signal inventory — list of namespaces with artifacts for `{{topic}}`.

Scan all namespaces above. Identify active namespaces (namespaces that have at least one artifact with `topic: {{topic}}`). Phase 1 output is the active namespace list.

**Phase 1 complete when**: every namespace has been scanned and active namespaces identified.

---

### PHASE 2 — EVALUATE

**Prerequisite**: Phase 1 complete (signal inventory exists).
**Output**: S2 — Signal Verdict Record. Named output of the EVALUATOR role. Discrete produced artifact. The AUTHOR role receives S2 as a complete named input before Phase 4 begins. Do not begin Phase 3 before S2 is fully populated.

```
[SLOT — S2: Signal Verdict Record (EVALUATOR Phase 2 output)
One paragraph per active namespace from Phase 1.
Per-paragraph required structure:
  (a) Namespace name.
  (b) Key finding: the single finding most directly informing the investigative question.
  (c) Interpretation: why this finding is material to the decision.
  (d) **Inertia verdict**: [YES — displaces status quo; case for not building weakens /
                            NO — confirms status quo holds /
                            PARTIAL — [one clause naming what shifts]]
CONSTRAINT: Interpret findings; do not enumerate. Omit namespaces with no artifacts.
A paragraph missing **Inertia verdict**: fails C-18.
PHASE 2 GATE: S2 is complete when every active Phase 1 namespace has an inertia verdict.
S4b Part 1 draws from this record as its exclusive input. Do not proceed to Phase 3 until
this gate condition is satisfied.]
```

**Phase 2 complete when**: S2 verdict record exists with inertia verdicts for every active Phase 1 namespace.

---

**[EVALUATOR ROLE COMPLETE — S2 IS THE NAMED OUTPUT. PROCEED TO AUTHOR ROLE.]**

---

## AUTHOR ROLE

S2 is complete above. Phase 2 is the EVALUATOR's named output. S4b Part 1 is a Phase 4 successor activity to Phase 2 — it receives S2 as its exclusive input. S4b Part 2 is a successor activity to S4b Part 1 — it receives Part 1 as its exclusive input.

---

### PHASE 3 — SYNTHESIZE

**Prerequisite**: Phase 2 complete (S2 verdict record exists as EVALUATOR named output).
**Output**: S1 (investigative framing) + S3 (cross-namespace pattern + disproof condition).

```
[SLOT — S1: What We Set Out to Understand
One paragraph. Past tense.
REQUIRED: State the investigative question — the decision, capability, or uncertainty that
opened this topic.
PROHIBITED OPENING CLASS — aggregate-first hedging constructions: any opening that gestures
at the evidence base before stating the question. Class label names the failure mode: leading
with inventory of evidence rather than the question. Surface forms: "The signals gathered
for...", "This synthesis covers...", "Based on the evidence collected...", "Across the
namespaces surveyed...". Class membership is structural function, not surface resemblance.
OPEN WITH: the question, the decision pressure, or the capability's relationship to what it
is meant to change.]

[SLOT — S3: What the Signals Say Together
One paragraph. Editorial synthesis.
REQUIRED: Identify the cross-namespace pattern visible only when all Phase 2 findings are
held simultaneously. Name what they converge on (if convergent) or name the fracture and
locate its source (if fractured).
PROHIBITED: Summarizing S2. Restating individual namespace findings.]

[SLOT — S3 Disproof Condition: REQUIRED structural element.
  **Disproof condition**: [This pattern fails if: specific observable condition that, if
                          shown to hold, invalidates the pattern claim above.]
Phase 3 is not complete until **Disproof condition**: is populated. Do not proceed to
Phase 4 without it.]
```

**Phase 3 complete when**: S1 paragraph, S3 paragraph, and labeled `**Disproof condition**:` field exist.

---

### PHASE 4 — CHARACTERIZE

**Prerequisite**: Phase 2 complete (EVALUATOR S2 exists as named output). S4b Part 1 is a direct successor to Phase 2 — its input is the Phase 2 S2 verdict record.
**Output**: S4a (residual uncertainties) + S4b Part 1 (verdict inventory) + S4b Part 2 (characterization).

```
[SLOT — S4a: Residual Uncertainties
One paragraph.
REQUIRED: Name signal gaps material to the Phase 5 recommendation.
REQUIRED FORM: "We do not know [X]; if X is shown to be false, the recommendation changes
from [current] to [Y]."
Generic hedges prohibited.]

[SLOT — S4b: Signal Characterization
This section has two parts. Complete Part 1 before writing Part 2. Do not merge parts.
The compliance architecture: Phase 2 S2 → Part 1 (inventory, constrained to S2 YES/PARTIAL)
→ Part 2 (characterization, constrained to Part 1). Each arrow is a structural dependency.]

  [SLOT — S4b Part 1: Verdict Inventory (Phase 4 successor to Phase 2)
  Enumerate only signals that received YES or PARTIAL inertia verdicts in Phase 2 S2.
  REQUIRED FORMAT per entry:
    - {namespace}/{signal-skill} (S2 verdict: YES)
    - {namespace}/{signal-skill} (S2 verdict: PARTIAL — [qualifier from Phase 2 S2])
  CONSTRAINT: NO-verdict signals are excluded. Do not introduce signals not in Phase 2 S2.
  Enumeration only — no interpretive prose.
  A Part 1 that includes NO-verdict signals or signals outside Phase 2 S2 fails C-51.
  Phase 4 proceeds to Part 2 only after Part 1 is complete.]

  [SLOT — S4b Part 2: Characterization (successor to Part 1)
  THIS SECTION DRAWS ONLY FROM PART 1 — NOT FROM AN INDEPENDENT REVIEW OF ALL SIGNALS.
  REQUIRED ELEMENTS:
    (a) What the Part 1 signals say together about this feature's readiness. Author's voice.
        Specific, not generic. Three to five sentences.
    (b) The status quo cost — what the team or user experiences without this capability,
        drawn from at least one named Part 1 signal.
  PROHIBITED: Introducing signals not in Part 1. Direct reference to Phase 2 S2 or the full
  signal set. Part 2's input scope is formally bounded by Part 1.
  COMPLIANCE NOTE: An evaluator verifying C-51 checks whether Part 2 references signals
  outside Part 1. Any such reference is a compliance failure regardless of narrative quality.]
```

**Phase 4 complete when**: S4a, S4b Part 1 (YES/PARTIAL signals only), and S4b Part 2 (constrained to Part 1) all exist.

---

### PHASE 5 — RECOMMEND

**Prerequisite**: Phases 2, 3, and 4 complete. All named phase outputs exist: S2 (Phase 2), S1+S3+disproof (Phase 3), S4a+S4b Part 1+S4b Part 2 (Phase 4).
**Output**: S5 — three-paragraph recommendation.

```
[SLOT — Para 1: Recommendation verdict.
REQUIRED ELEMENTS — all must appear:
  (a) Verdict: one of {proceed, pause, pivot, abandon}.
  (b) Reason: drawn from Phase 3 S3 pattern claim.
  (c) Inertia comparison: state whether acting is preferable to the Phase 4 S4b Part 2
      inertia scenario, and why. Reference S4b Part 2 by name.
  (d) Disproof condition cross-reference: "This call stands unless [Phase 3 S3
      **Disproof condition**] is demonstrated."
A Para 1 missing any of (b), (c), or (d) is structurally incomplete.]

[SLOT — Para 2: Counterargument.
REQUIRED ELEMENTS:
  (a) The strongest uncertainty from Phase 4 S4a — named.
  (b) Why it is material.
  (c) Why the verdict holds — or the condition under which it flips.]

[SLOT — Para 3: Action Directive.
REQUIRED ELEMENTS — all three must be present:
  (a) TRIGGER: Specific observable event that makes waiting costlier than acting. Named,
      identifiable. Not "when ready."
  (b) ACTION: Specific step when trigger fires.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if trigger fires without action.
      NOT general delay cost. Specific thing lost at the moment the named trigger fires unmet.
A Para 3 missing any of (a), (b), or (c) must be revised before submission.]
```

**Phase 5 complete when**: S5 with all three paragraphs exists and Para 3 contains all three required elements.

---

### Voice

Editorial throughout all phases and roles. No passive-voice hedging. No probability vocabulary as a substitute for judgment. The AUTHOR role writes S1, S3, S4, and S5 after the EVALUATOR role has produced S2 as a named artifact.

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
