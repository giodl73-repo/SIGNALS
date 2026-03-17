Good. R14 V-05 was 100/100 (structured format, 39/39 aspirationals). R15 deliberately broke from structured format to editorial prose — dropping to 20/43 but keeping 94.77 (golden). V-05 (R15) passes C-47, C-48, C-18 (inertia verdict), C-12 (disproof condition), and related editorial criteria, but C-49 (S2→S4b chain) and C-50 (slot-label criterion citation) both fail.

The gain from fixing both: +0.4652 → 95.24. But the bigger picture is the same 23 other aspirationals (the structured-format criteria C-19 to C-44) still fail. R16 variations should: (1) fix C-49 and C-50, and (2) explore whether any structural recovery is possible without destroying the editorial format's coherence.

---

# topic-story Variations — R16

**Round**: 16  
**Skill**: `topic-story`  
**Base rubric**: `topic-story-rubric-v16-2026-03-15.md`  
**New criteria this round**: C-49, C-50  

## R15 State Summary

R15: V-05 scored 94.77 under v16 (20 of 43 aspirationals, 1 PARTIAL). The R15 editorial format (S1–S5 prose directives, slot-fill template) retained criteria associated with per-signal inertia verdict (`**Inertia verdict**:`, C-18), disproof condition (`**Disproof condition**:`, C-12), class-labeled hedge prohibition (C-47), three-element Para 3 (C-48), and inertia-anchored S5 (C-46), while dropping the structured-format criteria C-19 to C-44 (pre-artifact checklist, field inventory table, colon-label fields, prior-position fields). Two new v16 criteria both fail:

- **C-49**: V-05 S4b is an "Inertia Comparator" — a general description of what happens without the feature. It does not name signals from S2, does not reference the S2 verdict distribution, and cannot be audited against S2 YES/PARTIAL outputs. The S2→S4b chain is implicit, not legible from the artifact.
- **C-50**: V-05 slot headers embed `**Inertia verdict**: [YES/NO/PARTIAL]` field markers and the `(fails C-12)` criterion citation in S3. However, the rubric scoring treats these as prompt instructions rather than self-documenting criterion requirements co-located at the authoring slot — the PARTIAL suggests proximity but the auditable criterion-at-point-of-action test is not cleanly satisfied.

**R15 baseline under v16**: 94.77. Target for R16: 94.77 + 0.4652 (both C-49 and C-50 clean passes) = **95.24**. Stretch: recover structural criteria without losing editorial voice.

**R16 design requirement**: All five variations must satisfy C-49 (legible S2→S4b chain) and C-50 (criterion requirement embedded as slot-label at point of authoring action). Variation axes explore mechanism and depth.

**Variation axes for R16**:
- Single-axis: S4b restructure (direct C-49 fix — S4b slot explicitly draws named signals from S2 YES/PARTIAL verdicts) — V-01
- Single-axis: Slot-header criterion citations (direct C-50 fix — criterion numbers embedded in section headers as compliance requirements at point of authoring action) — V-02
- Single-axis: Role sequence (evaluator-first role produces S2 verdicts as discrete outputs that V-03 requires S4b to reference — C-49 as consequence of role sequence rather than structural instruction) — V-03
- Compound: S4b restructure + slot-header criterion citations (V-01 + V-02) — V-04
- Compound: Full integration (V-01 + V-02 + V-03 + pre-artifact checklist recovery for C-19) — V-05

---

## V-01 — Single-Axis: S4b Restructure (Direct C-49 Fix)

**Variation axis**: S4b slot restructured from general "Inertia Comparator" to two-part "Signal Baseline" that explicitly draws named signals from S2 YES/PARTIAL inertia verdicts — minimum change from R15 V-05.  
**Hypothesis**: The minimum change needed to satisfy C-49 is restructuring only S4b: require Part 1 to inventory the S2 YES/PARTIAL signals by name, and Part 2 to draw its characterization from Part 1 only. This makes the S2→S4b chain legible from the artifact without altering any other section of the R15 V-05 design.

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
PROHIBITED OPENING CLASS — aggregate-first hedging constructions: any construction that
opens by cataloging evidence rather than stating the question. Class label identifies the
failure mode by type: the question is displaced by an inventory of the evidence base.
Surface forms include: "The signals gathered for...", "This synthesis covers...", "Based
on the evidence collected...", "Across the namespaces surveyed...", "The investigation
examined...". Novel forms sharing this failure mode are prohibited — class membership
determined by structural function, not surface resemblance.
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
CONSTRAINT: Omit namespaces with no artifacts. If a namespace's inertia verdict is NO
and the finding has no secondary signal value, omit that namespace from S2. Close S2
with a count: "X namespaces omitted; all returned NO inertia verdict with no secondary
value."
Do not enumerate findings — interpret them.]

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
REQUIRED: Name signal gaps — namespaces not activated, questions opened without
resolution, contradicted findings.
CONSTRAINT: Only name uncertainties material to S5. Prohibited forms: "More research
may be needed", "There is uncertainty around", "Future work could explore". Required
form: "We do not know [X]; if X is shown to be false, the recommendation changes from
[current] to [Y]. Resolution method: [specific investigation]."]

---

## S4b — Signal Baseline

[SLOT: Two-part structure. This section draws directly from S2 inertia verdicts — it is
not an independently composed inertia description.

PART 1 — Verdict inventory (drawn from S2):
List each namespace signal that received YES or PARTIAL inertia verdict in S2. For each,
write one line in this form:
  - {namespace} (S2 verdict: YES/PARTIAL): [one sentence — what this signal says about
    the status quo cost of not having this capability]

At least one signal must appear here. The signals named in Part 1 must match the YES or
PARTIAL verdicts produced in S2 — an evaluator must be able to verify each entry against
S2 by namespace name. If no signals received YES or PARTIAL in S2, write: "No signals
received YES or PARTIAL inertia verdict in S2; S4b baseline is unestablished." Do not
proceed to Part 2 in that case.

PART 2 — Baseline characterization:
In one paragraph, characterize what the Part 1 signals say collectively about what users
or teams continue to experience in the absence of this feature. Draw from Part 1 only —
do not introduce new evidence or name signals not present in Part 1. This paragraph is
the inertia baseline for S5 Para 1 cross-reference.

CHAIN REQUIREMENT: S4b is the downstream end of the S2→S4b traceability chain. Part 1
names the signals; Part 2 characterizes their collective meaning. S5 Para 1 cross-
references this section by name ("S4b"). An evaluator must be able to verify S4b's
baseline against S2 YES/PARTIAL verdicts without narrative inference.]

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
      move, competitive action, technical proof point, team capacity signal, date
      threshold.
  (b) ACTION: Specific step when trigger fires. Sprint commitment, prototype
      authorization, go/no-go decision gate, stakeholder review.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if the trigger fires without action.
      NOT the general delay cost from Para 1 or S4b. The specific thing lost at the
      moment the named trigger fires unmet: the window that closes, the position taken by
      a competitor, the technical debt that locks in, the team capacity that disperses.
      Must be tied directly to trigger (a) — not a background observation.
STRUCTURAL COMPLETENESS RULE: A Para 3 missing any of (a), (b), or (c) is structurally
incomplete and must be revised before submission.]
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

---

## V-02 — Single-Axis: Slot-Header Criterion Citations (Direct C-50 Fix)

**Variation axis**: Output format — criterion numbers embedded directly in section headers as explicit compliance requirements at the point of authoring action, not in separate instructions. Headers become self-documenting compliance anchors.  
**Hypothesis**: Embedding criterion citations (C-12, C-18, C-47, C-48, C-49) directly in section headers — adjacent to the section label rather than inside the slot body — makes each criterion's compliance requirement visible at the exact moment the author begins filling the slot, satisfying C-50 for multiple slots simultaneously. This also creates an audit anchor per section that can be verified without reference to a separate checklist.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

Your task: produce an editorial synthesis of all signals gathered for this topic. Execute every slot in the template below. Section headers include the criterion requirements governing that slot — these are compliance requirements, not orientation. Do not skip slots. Do not merge slots.

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

## S1 — What We Set Out to Understand [C-47: PROHIBITED CLASS — aggregate-first hedging constructions]

[SLOT: One paragraph. Past tense. Open with the investigative question, decision pressure,
or capability purpose — not with an inventory of the evidence base.
PROHIBITED OPENING CLASS — aggregate-first hedging constructions: any construction that
opens by cataloging evidence rather than the question. Class label names the failure mode
by type: question displaced by evidence inventory. Surface forms include: "The signals
gathered for...", "This synthesis covers...", "Based on the evidence collected...",
"Across the namespaces surveyed...", "The investigation examined...". Novel forms sharing
the failure mode are prohibited — class membership determined by structural function,
not surface resemblance. The class label names the type, not the list; novel paraphrases
that satisfy the failure-mode definition belong to the class.]

---

## S2 — What Each Signal Revealed [C-18: **Inertia verdict**: YES/NO/PARTIAL REQUIRED per namespace]

[SLOT: One paragraph per namespace with artifacts.
Per-paragraph required structure:
  (a) Namespace name.
  (b) Key finding: the single finding most directly informing S1's question.
  (c) Interpretation: why this finding is material to the decision.
  (d) **Inertia verdict**: [YES / NO / PARTIAL] — required field, immediately following
      the finding. YES: displaces status quo, case for not building weakens. NO: confirms
      status quo, no build reason emerges. PARTIAL: [one clause naming what aspect shifts].
      This field is required per namespace paragraph; omitting it fails C-18.
CONSTRAINT: Omit namespaces with no artifacts. Close S2 with a count if any namespaces
are omitted.]

---

## S3 — What the Signals Say Together [C-12: **Disproof condition** REQUIRED before proceeding to S4]

[SLOT: One paragraph. Editorial synthesis only. Identify the cross-namespace pattern
visible only when all findings are held simultaneously. Name convergence or fracture.
PROHIBITED: Summarizing S2. Restating findings. Signal-list construction.]

[SLOT: Falsifiability gate — run after paragraph above:
  **Disproof condition**: [This pattern fails if: specific observable condition that, if
  shown to hold, invalidates the pattern claim above.]
Required: populate this field before writing S4. A pattern without a named disproof
condition fails C-12 and must be revised before proceeding.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph.
Name only uncertainties material to S5. Required form: "We do not know [X]; if X is
shown to be false, the recommendation changes from [current] to [Y]. Resolution:
[specific investigation]." Generic hedges are prohibited.]

---

## S4b — Signal Baseline [C-49: S4b MUST draw from S2 YES/PARTIAL verdicts — chain must be legible]

[SLOT: Two parts. S4b is the downstream end of the S2→S4b chain. Part 1 names the
S2 YES/PARTIAL signals. Part 2 draws only from Part 1.

PART 1 — S2 verdict inventory:
  - {namespace} (S2 verdict: YES/PARTIAL): [one sentence — status quo cost of absence]
Repeat for every namespace that received YES or PARTIAL in S2. If none, state:
"No YES/PARTIAL verdicts in S2; S4b baseline is unestablished."

PART 2 — Baseline characterization:
One paragraph drawing from Part 1 only. What do the Part 1 signals say collectively
about what users or teams experience in the absence of this capability? Do not introduce
evidence not in Part 1. S5 Para 1 cross-references this section by name.]

---

## S5 — Recommendation [C-46: Para 1 MUST name inertia comparator and cross-reference S4b | C-48: Para 3 MUST have trigger + action + inertia-at-trigger]

[SLOT: Para 1 — Recommendation verdict.
  (a) Verdict: {proceed, pause, pivot, abandon}.
  (b) Reason: from S3 pattern claim.
  (c) Inertia comparison: state why acting is preferable to the S4b baseline. Name S4b.
      (Required by C-46 — fails if S4b not cross-referenced.)
  (d) Falsifiability closure: "This call stands unless [**Disproof condition** from S3]
      is shown to hold."]

[SLOT: Para 2 — Counterargument.
  (a) Strongest S4a uncertainty — named.
  (b) Why it is material.
  (c) Why the verdict holds, or the condition under which it flips.]

[SLOT: Para 3 — Action Directive. (Required by C-48: all three elements must appear.)
  (a) TRIGGER: Named observable event that makes waiting costlier than acting. Not "when
      ready" — a specific, identifiable event.
  (b) ACTION: Specific step when trigger fires.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if trigger fires without action.
      Tied to trigger (a). Not the general delay cost from Para 1 or S4b.
A Para 3 missing any element fails C-48 and must be revised.]
```

---

### Voice

Section headers cite the governing criteria — these are not reminders, they are the compliance architecture. Populate each slot with editorial conviction. No passive hedging. No probability vocabulary as a substitute for judgment.

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

## V-03 — Single-Axis: Role Sequence (Evaluator-First)

**Variation axis**: Role sequence — an explicit Signal Evaluator role runs first and produces the S2 inertia verdict distribution as a discrete, named output before the Narrative Synthesizer constructs the story. S4b is explicitly required to reference the Evaluator's verdict output, making C-49 a consequence of role handoff rather than a structural template requirement.  
**Hypothesis**: Framing the verdict distribution as the output of a named role (Signal Evaluator) and requiring the downstream role (Narrative Synthesizer) to explicitly reference that output in S4b creates a more robust C-49 chain than a template instruction alone — role handoff makes the chain architectural rather than instructional, and the named output ("verdict distribution from Role 1") provides a concrete reference anchor the author must use.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

Your task: produce an editorial synthesis of all signals gathered for this topic. Execute the three roles below in order. Each role produces a distinct output. Complete each role fully before beginning the next. The final artifact is produced in Role 3.

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

### Role Sequence

#### ROLE 1 — Signal Evaluator

Evaluate each namespace that has artifacts for this topic. For each, produce:

- **Namespace**: [name]
- **Key finding**: [one sentence — the claim the namespace makes that most directly bears on the feature decision]
- **Inertia verdict**: YES / NO / PARTIAL  
  - YES: this finding displaces the status quo; the case against building weakens  
  - NO: this finding confirms the status quo holds; no build reason emerges  
  - PARTIAL: [one clause naming what shifts and what does not]

Produce this evaluation for every namespace with artifacts. Namespaces with no artifacts are noted with "no artifacts — excluded." Do not write the narrative. Do not draw conclusions across namespaces. Complete the verdict per namespace before proceeding to Role 2.

**Role 1 output**: A verdict distribution — a list of namespaces with their key findings and inertia verdicts. This output is the input to Role 2.

---

#### ROLE 2 — Baseline Composer

Using the Role 1 verdict distribution:

1. Identify every namespace that received YES or PARTIAL verdict.
2. For each YES/PARTIAL namespace, write one sentence stating what its finding means for the status quo — what users or teams continue to experience if this feature is not built.
3. Compose a one-paragraph baseline characterization that draws from these sentences only. Do not introduce evidence not in the Role 1 verdict distribution.

**Role 2 output**: An inertia baseline — a verdict inventory (the YES/PARTIAL namespaces with their status quo sentences) and a baseline characterization paragraph. This output is the input to S4b in Role 3. S4b must reference this output by name ("the Role 1 verdict distribution") and draw its content from it.

---

#### ROLE 3 — Narrative Synthesizer

Using the Role 1 verdict distribution and Role 2 inertia baseline, produce the story artifact by populating every slot in the template below. S4b draws from Role 2's output — use it explicitly.

```
---
topic: {{topic}}
signal: story
date: {{date}}
---

## S1 — What We Set Out to Understand

[SLOT: One paragraph. Past tense. State the investigative question — the decision,
capability, or uncertainty that opened this topic.
PROHIBITED OPENING CLASS — aggregate-first hedging constructions: any construction that
opens by cataloging evidence rather than the investigative question. Class label names
the failure mode by type: question displaced by evidence inventory. Surface forms
include: "The signals gathered for...", "This synthesis covers...", "Based on the
evidence collected...", "Across the namespaces surveyed...", "The investigation
examined...". Novel forms sharing the failure mode are prohibited. Class membership
determined by structural function, not surface resemblance.
OPEN WITH: the question, the decision pressure, or the capability's relationship to
what it is meant to change.]

---

## S2 — What Each Signal Revealed

[SLOT: Populate from Role 1 verdict distribution. One paragraph per namespace with
artifacts. Per-paragraph structure:
  (a) Namespace name.
  (b) Key finding (from Role 1 — carry the exact claim, then interpret it).
  (c) Interpretation: why this finding is material to the decision.
  (d) **Inertia verdict**: [carry Role 1 verdict for this namespace]
Omit namespaces with no artifacts. Close S2 with a count of omitted namespaces if any.]

---

## S3 — What the Signals Say Together

[SLOT: One paragraph. Editorial synthesis. Identify the cross-namespace pattern visible
only when all Role 1 findings are held simultaneously — what do they say together that
no single namespace says alone? If convergent, name the convergence. If fractured, name
the fracture and locate its source.
PROHIBITED: Summarizing S2. Restating individual findings.]

[SLOT: Falsifiability gate:
  **Disproof condition**: [This pattern fails if: specific observable condition that,
  if shown to hold, invalidates the pattern claim above.]
REQUIRED before proceeding to S4. Fails C-12 if absent.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph. Name only uncertainties material to S5. Required form: "We do
not know [X]; if X is shown to be false, the recommendation changes from [current] to
[Y]. Resolution: [specific investigation]." Generic hedges prohibited.]

---

## S4b — Signal Baseline [drawn from Role 2 inertia baseline — reference by name]

[SLOT: Populate directly from Role 2 output. Do not compose independently.

PART 1 — Role 2 verdict inventory (carry from Role 2 without modification):
  - {namespace} (Role 1 verdict: YES/PARTIAL): [status quo cost sentence from Role 2]

PART 2 — Role 2 baseline characterization (carry from Role 2, revise for editorial
voice if needed, but do not introduce new evidence):
[One paragraph drawn from Part 1 signals only.]

CHAIN INTEGRITY: S4b's Part 1 must list the same namespaces that Role 1 assigned YES
or PARTIAL. An evaluator must be able to match Part 1 against Role 1 outputs. If the
lists diverge, correct S4b — not Role 1.]

---

## S5 — Recommendation

[SLOT: Para 1 — Recommendation verdict.
  (a) Verdict: {proceed, pause, pivot, abandon}.
  (b) Reason: from S3 pattern claim.
  (c) Inertia comparison: state why acting is preferable to the S4b baseline. Cross-
      reference S4b by name. A Para 1 without S4b cross-reference is incomplete.
  (d) Falsifiability closure: "This call stands unless [**Disproof condition** from S3]
      is shown to hold."]

[SLOT: Para 2 — Counterargument.
  (a) Strongest S4a uncertainty — named explicitly.
  (b) Why it is material.
  (c) Why the verdict holds, or the condition under which it flips.]

[SLOT: Para 3 — Action Directive. All three elements required:
  (a) TRIGGER: Named observable event that makes waiting costlier than acting.
  (b) ACTION: Specific step when trigger fires.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if trigger fires without action,
      tied to trigger (a). Not a general delay cost.
A Para 3 missing any element is structurally incomplete and must be revised.]
```

---

### Voice

Role outputs feed the template; editorial conviction fills the content. No passive hedging. No probability vocabulary substituting for judgment. The author is a decision advisor, not a summarizer.

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

## V-04 — Compound: S4b Restructure + Slot-Header Criterion Citations (V-01 + V-02)

**Variation axis**: Compound — direct C-49 fix (S4b two-part structure drawing from S2 YES/PARTIAL verdicts, V-01) combined with slot-header criterion citations at point of authoring action (V-02). Minimal role-sequence change; all structural work done in the template.  
**Hypothesis**: Combining the C-49-targeted S4b slot structure with explicit criterion citations in section headers produces the cleanest path to satisfying both new v16 criteria without role-sequence overhead. V-01 fixes C-49 as a template requirement; V-02 fixes C-50 as a header annotation. The compound produces an artifact where every major compliance requirement is visible at the section header, and S4b's chain is legible without narrative inference.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

Your task: produce an editorial synthesis of all signals gathered for this topic. Execute every slot in the template below. Section headers include criterion compliance requirements — these are binding specifications at the point of authoring action, not orientation. Do not skip slots. Do not merge slots.

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
## [C-47: PROHIBITED — aggregate-first hedging constructions; class membership by function]

[SLOT: One paragraph. Past tense. State the investigative question — the decision,
capability, or uncertainty that opened this topic.
PROHIBITED OPENING CLASS — aggregate-first hedging constructions: any construction that
opens by cataloging evidence rather than stating the investigative question. Class label
names the failure mode by type: question displaced by evidence inventory. Surface forms
include: "The signals gathered for...", "This synthesis covers...", "Based on the
evidence collected...", "Across the namespaces surveyed...", "The investigation
examined...". Class membership determined by structural function — novel forms sharing
the failure mode are prohibited even if not in the surface list.
OPEN WITH: the question, the decision pressure, or the capability's relationship to
what it is meant to change.]

---

## S2 — What Each Signal Revealed
## [C-18: **Inertia verdict**: YES/NO/PARTIAL — REQUIRED labeled field per namespace]

[SLOT: One paragraph per namespace with artifacts.
Per-paragraph required structure:
  (a) Namespace name.
  (b) Key finding: the single finding most directly informing S1's question.
  (c) Interpretation: why this finding is material to the decision.
  (d) **Inertia verdict**: [YES / NO / PARTIAL] — required field. Failure to include
      this field per namespace fails C-18.
      YES: displaces status quo; case for not building weakens.
      NO: confirms status quo holds; no build reason emerges.
      PARTIAL: [one clause naming what shifts].
CONSTRAINT: Omit namespaces with no artifacts. Close S2 with an omission count.]

---

## S3 — What the Signals Say Together
## [C-12: **Disproof condition** — REQUIRED labeled field before proceeding to S4]

[SLOT: One paragraph. Editorial synthesis. Identify the cross-namespace pattern visible
only when all findings are held simultaneously. Name convergence or fracture.
PROHIBITED: Summarizing S2. Restating findings. Signal-list construction.]

[SLOT: Falsifiability gate — populate immediately after paragraph above:
  **Disproof condition**: [This pattern fails if: specific observable condition that,
  if shown to hold, invalidates the pattern claim above.]
Failure to populate this field fails C-12. Do not proceed to S4a until populated.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph. Name only uncertainties material to S5.
Required form: "We do not know [X]; if X is shown to be false, the recommendation
changes from [current] to [Y]. Resolution: [specific investigation]."
Generic hedges ("more research may be needed") are prohibited.]

---

## S4b — Signal Baseline
## [C-49: DRAWS FROM S2 YES/PARTIAL VERDICTS — chain must be auditable without narrative inference]

[SLOT: Two-part structure. S4b is the downstream end of the S2→S4b traceability chain.

PART 1 — S2 YES/PARTIAL verdict inventory:
List every namespace that received YES or PARTIAL inertia verdict in S2. For each:
  - {namespace} (S2 verdict: YES/PARTIAL): [one sentence — what this signal says about
    the status quo cost of not having this capability]
At least one entry required. If S2 produced no YES or PARTIAL verdicts, write: "No
YES/PARTIAL verdicts in S2; S4b baseline is unestablished." Do not write Part 2.

PART 2 — Baseline characterization:
One paragraph drawn from Part 1 entries only. What do the Part 1 signals say
collectively about what users or teams experience in the absence of this capability?
Do not introduce signals or evidence not in Part 1. This paragraph is the inertia
baseline for S5 Para 1.

CHAIN AUDIT: An evaluator must be able to match every Part 1 entry against an S2
YES/PARTIAL verdict by namespace name. A Part 1 that names signals not present in S2
as YES/PARTIAL fails C-49.]

---

## S5 — Recommendation
## [C-46: Para 1 MUST cross-reference S4b | C-48: Para 3 MUST have trigger + action + inertia-at-trigger]

[SLOT: Para 1 — Recommendation verdict.
REQUIRED ELEMENTS:
  (a) Verdict: {proceed, pause, pivot, abandon}.
  (b) Reason: primary reason from S3 pattern claim.
  (c) Inertia comparison: state why acting is preferable to S4b baseline. Name "S4b"
      explicitly. Failure to cross-reference S4b fails C-46.
  (d) Falsifiability closure: "This call stands unless [**Disproof condition** from S3]
      is shown to hold."]

[SLOT: Para 2 — Counterargument.
  (a) Strongest S4a uncertainty — named explicitly.
  (b) Why it is material.
  (c) Why the verdict holds despite it — or the condition under which it flips.]

[SLOT: Para 3 — Action Directive. (C-48: all three elements required.)
  (a) TRIGGER: Named observable event making waiting costlier than acting. Not "when
      ready" — a specific event: market move, technical proof point, date threshold.
  (b) ACTION: Specific step when trigger fires.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if trigger fires without action.
      Tied directly to trigger (a). Not a general delay observation from Para 1/S4b.
STRUCTURAL COMPLETENESS RULE (C-48): A Para 3 missing (a), (b), or (c) must be
revised before submission.]
```

---

### Voice

Section headers embed the governing criteria — compliance architecture at the authoring point, not in a checklist. Populate with editorial conviction. No passive hedging. No probability substitutes for judgment.

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

## V-05 — Full Compound: S4b Restructure + Slot-Header Citations + Evaluator-First + Pre-Artifact Checklist

**Variation axis**: Full compound — direct C-49 fix (S4b two-part verdict-traced structure, V-01) + slot-header criterion citations (V-02) + evaluator-first role sequence (V-03) + pre-artifact checklist (C-19 recovery attempt).  
**Hypothesis**: Full integration adds a pre-artifact checklist to V-04 (recovering C-19) and layers the evaluator-first role sequence (V-03) as the mechanism that generates the S2 verdicts, making the S2→S4b chain a role-handoff artifact rather than purely a template instruction. Combining all four changes produces the maximum coverage variation: C-49 satisfied by role handoff + S4b template structure; C-50 satisfied by slot-header criterion citations; C-19 recovered by the pre-artifact checklist; and the evaluator-first sequence independently grounds the S2 verdicts before the synthesizer composes from them. The pre-artifact checklist also acts as an audit gate before the template is filled, creating a two-layer compliance architecture (gate-level + in-context) that satisfies both C-19 and C-50 simultaneously.

---

You are executing the `topic-story` skill for topic `{{topic}}`.

Your task: produce an editorial synthesis of all signals gathered for this topic. Complete the pre-artifact checklist first. Then execute the three roles in order. The final artifact is produced in Role 3.

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

Complete before writing any section. State each check as PASS, FAIL, or N/A with one sentence of evidence.

- [ ] **Namespace inventory**: All eight namespace directories checked; artifact list compiled.
- [ ] **S1 question identified**: The investigative question that opened this topic is stated in one sentence.
- [ ] **Aggregate-first hedging prohibition understood**: The class of prohibited S1 openings is known (any construction that opens by cataloging evidence rather than the question — failure mode by type, not surface match).
- [ ] **S2 verdicts ready**: Each namespace with artifacts has been assigned an inertia verdict (YES/NO/PARTIAL) before narrative is written. Verdict distribution recorded.
- [ ] **S2→S4b chain prepared**: YES and PARTIAL namespaces from the S2 verdict distribution are identified. S4b will draw from this set, not from independent composition.
- [ ] **S3 disproof condition formulated**: A falsifying condition for the expected pattern claim is stated. Pattern claim and disproof condition will be written together in S3.
- [ ] **S4a material uncertainties identified**: Uncertainties material to the S5 recommendation are named; generic hedges removed.
- [ ] **Para 3 three elements prepared**: Trigger condition, action option, and inertia consequence at trigger are each identified for S5 Para 3.

Do not proceed to Role 1 until all checklist items are either PASS or N/A with justification.

---

### Role Sequence

#### ROLE 1 — Signal Evaluator

Produce the S2 verdict distribution. For each namespace with artifacts:

- **Namespace**: [name]
- **Key finding**: [one sentence — the claim the namespace makes that most directly bears on the feature decision]
- **Inertia verdict**: YES / NO / PARTIAL  
  - YES: finding displaces the status quo; case against building weakens  
  - NO: finding confirms status quo holds; no build reason emerges  
  - PARTIAL: [one clause naming what shifts and what does not]

Evaluate every namespace with artifacts. Note "no artifacts — excluded" for namespaces with no artifacts. Do not write narrative. Do not draw cross-namespace conclusions. Complete the verdict distribution before proceeding.

**Role 1 output**: Verdict distribution — a named list of namespaces with key findings and inertia verdicts. This is the input to Role 2 and the authoritative source for S2 and S4b in Role 3.

---

#### ROLE 2 — Baseline Composer

Using the Role 1 verdict distribution, identify every YES or PARTIAL namespace. For each:

1. Write one sentence: what does this finding say about the status quo cost of not having this capability — what do users or teams continue to experience in its absence?
2. Compile these sentences into an inertia baseline.
3. Write a one-paragraph baseline characterization drawing from these sentences only. Do not introduce evidence not in the Role 1 verdict distribution.

**Role 2 output**: Inertia baseline — an inventory of YES/PARTIAL namespaces with status quo cost sentences, plus a baseline characterization paragraph. This is the direct input to S4b in Role 3.

---

#### ROLE 3 — Narrative Synthesizer

Using Role 1 verdict distribution and Role 2 inertia baseline, populate every slot in the template below.

```
---
topic: {{topic}}
signal: story
date: {{date}}
---

## S1 — What We Set Out to Understand
## [C-47: PROHIBITED CLASS — aggregate-first hedging constructions; class membership by failure mode, not surface form]

[SLOT: One paragraph. Past tense.
PROHIBITED OPENING CLASS — aggregate-first hedging constructions: any construction
that opens by cataloging evidence rather than the investigative question. Class label
names the failure mode by type. Surface forms: "The signals gathered for...", "This
synthesis covers...", "Based on the evidence collected...", "Across the namespaces
surveyed...", "The investigation examined...". Novel forms sharing the failure mode are
prohibited; class membership determined by function, not surface resemblance.
OPEN WITH: the question, the decision pressure, or the capability's relationship to
what it is meant to change. Not with what was gathered.]

---

## S2 — What Each Signal Revealed
## [C-18: **Inertia verdict**: YES/NO/PARTIAL — REQUIRED labeled field per namespace; carry from Role 1]

[SLOT: Populate from Role 1 verdict distribution. One paragraph per namespace.
Per-paragraph structure:
  (a) Namespace name.
  (b) Key finding (from Role 1 — carry the claim, then interpret it in editorial voice).
  (c) Interpretation: why this finding is material to the decision.
  (d) **Inertia verdict**: [carry Role 1 verdict] — required field per paragraph.
      Failure to carry the Role 1 verdict fails C-18.
Omit namespaces with no artifacts. Close S2 with an omission count.]

---

## S3 — What the Signals Say Together
## [C-12: **Disproof condition** — REQUIRED labeled field; populate before proceeding to S4]

[SLOT: One paragraph. Editorial synthesis of Role 1 findings held simultaneously.
Identify cross-namespace pattern. Name convergence or fracture. PROHIBITED: Summarizing
S2. Restating findings.]

[SLOT: Falsifiability gate:
  **Disproof condition**: [This pattern fails if: specific observable condition that,
  if shown to hold, invalidates the pattern claim above.]
Required. Absence fails C-12. Do not write S4a until this field is populated.]

---

## S4a — Residual Uncertainties

[SLOT: One paragraph. Name only uncertainties material to S5. Required form: "We do
not know [X]; if X is shown to be false, the recommendation changes from [current] to
[Y]. Resolution: [specific investigation]." Generic hedges prohibited.]

---

## S4b — Signal Baseline
## [C-49: DRAWS FROM ROLE 2 INERTIA BASELINE — match Part 1 against Role 1 YES/PARTIAL set; chain auditable without inference]

[SLOT: Populate directly from Role 2 output. Two parts.

PART 1 — Role 2 verdict inventory (carry from Role 2):
  - {namespace} (Role 1 verdict: YES/PARTIAL): [status quo cost sentence from Role 2]
Repeat for every YES/PARTIAL namespace from Role 1. At least one required. If Role 1
produced no YES/PARTIAL verdicts, state: "No YES/PARTIAL verdicts in Role 1; baseline
unestablished." Do not write Part 2.

PART 2 — Role 2 baseline characterization (carry and revise for editorial voice):
One paragraph from Part 1 entries only. Do not introduce evidence not in Part 1. This
is the inertia baseline for S5 Para 1 cross-reference.

CHAIN AUDIT: Part 1 entries must match Role 1 YES/PARTIAL namespaces. Divergence must
be corrected in Part 1, not in Role 1. S5 Para 1 names "S4b" to cross-reference here.]

---

## S5 — Recommendation
## [C-46: Para 1 cross-references S4b by name | C-48: Para 3 requires trigger + action + inertia-at-trigger]

[SLOT: Para 1 — Recommendation verdict.
  (a) Verdict: {proceed, pause, pivot, abandon}.
  (b) Reason: from S3 pattern claim.
  (c) Inertia comparison: state why acting is preferable to S4b baseline. Name "S4b"
      explicitly. Absent reference fails C-46.
  (d) Falsifiability closure: "This call stands unless [**Disproof condition** from S3]
      is shown to hold."]

[SLOT: Para 2 — Counterargument.
  (a) Strongest S4a uncertainty — named.
  (b) Why it is material.
  (c) Why verdict holds despite it, or the condition under which it flips.]

[SLOT: Para 3 — Action Directive. (C-48: all three elements must be present.)
  (a) TRIGGER: Named observable event making waiting costlier than acting. Not "when
      ready" — a specific event.
  (b) ACTION: Specific step when trigger fires.
  (c) INERTIA-AT-TRIGGER: Specific outcome forgone if trigger fires without action.
      Tied to trigger (a) — not a general delay cost from Para 1 or S4b.
Absence of any element fails C-48. Must be revised before submission.]
```

---

### Voice

Role outputs feed the template slots. Editorial conviction fills the content. No passive hedging. No probability substitutes for judgment. The pre-artifact checklist is the gate; the slot headers are the in-context enforcement; the role sequence is the evidence chain. All three layers serve the same author making the same call.

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

## Variation Summary

| | Axis | C-49 mechanism | C-50 mechanism | C-19 | Role sequence |
|---|---|---|---|---|---|
| V-01 | S4b restructure | Two-part slot: Part 1 names S2 YES/PARTIAL signals | Inherits V-05(R15) slot markers | No | None |
| V-02 | Slot-header citations | S4b header: `[C-49: DRAWS FROM S2 YES/PARTIAL VERDICTS]` | Criterion numbers in section headers | No | None |
| V-03 | Evaluator-first | Role handoff: S4b explicitly references Role 2 output | Inherits V-05(R15) slot markers | No | Evaluator → Baseline → Synthesizer |
| V-04 | V-01 + V-02 | Two-part slot + header citation | Criterion headers on all major sections | No | None |
| V-05 | Full compound | Role handoff + two-part slot + header citation | Criterion headers + pre-artifact checklist (dual architecture) | Pre-artifact checklist | Evaluator → Baseline → Synthesizer |

**Predicted winner**: V-05 — it satisfies C-49 through both a role-handoff mechanism and a structural S4b template requirement, satisfies C-50 through both slot-header criterion citations and in-slot field markers, and recovers C-19 through the pre-artifact checklist gate. The dual compliance architecture (gate-level checklist + in-context slot headers) is the strongest C-50 formulation across all five variations.
