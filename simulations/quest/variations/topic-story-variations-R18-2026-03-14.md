Now I have the full picture. R17 V-05 has C-51 (S4b partition) + C-52 (EVALUATOR/AUTHOR roles + phase diagram) but no explicit C-53 layer declaration. The three single-axis variations test different ways to co-locate the compliance architecture declaration with the authoring workflow.

---

# Round 18 Variations — `topic-story`

**Rubric version**: v18 (C-01–C-53, 46 aspirationals)
**Base**: R17 V-05 under v18 = **96.20** — 28 full + 1 PARTIAL / 46 aspirationals (C-53 is FAIL; PARTIAL is on an inherited C-08–C-50 structural transparency criterion)
**New criterion**: C-53 — explicit compliance enforcement layer declaration, co-located with authoring workflow, naming each layer with mechanism description, governing criterion reference, and inter-layer ordering relationships

## Variation Axes

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Role Sequence: prose compliance architecture block before EVALUATOR header | YES | NO | NO | YES | YES |
| Output Format: 3-column compliance architecture table | NO | YES | NO | YES | YES |
| Lifecycle Emphasis: annotated phase diagram as layer declaration vehicle | NO | NO | YES | NO | YES |
| Layer count declared | 2 | 2 | 2 | 2 | 3 |

**Predictions:**
- V-01: +C-53 PASS — prose declaration co-located at workflow entry satisfies C-53 pass condition (Layer 1+2 named, criterion refs, ordering stated). Score: 90 + (29 × 0.2174) + (1 × 0.1087) = **96.41**
- V-02: +C-53 PASS — table format makes declaration more auditable but equivalent structural position. Score: **96.41**
- V-03: +C-53 PASS — phase diagram legend satisfies C-53's "phase-diagram legend with criterion annotations" explicit pass-condition form. Score: **96.41**
- V-04: +C-53 PASS — positioning (V-01) + table format (V-02). PARTIAL on inherited criterion may convert to FULL if table format eliminates the ambiguity that caused it. Score: **96.41** to **96.63** depending on PARTIAL resolution
- V-05: +C-53 PASS + possible PARTIAL→FULL — three declared layers (adding phase prerequisites as Layer 3) makes declared layer count match the three mechanisms in V-05's architecture. If the inherited PARTIAL on C-08–C-50 structural transparency was caused by layers being undeclared, C-53 satisfaction converts it. Score: **96.41** to **96.63**

---

## V-01

**Axis**: Role Sequence — prose compliance architecture block co-located before EVALUATOR header
**Hypothesis**: Placing an explicit "WORKFLOW COMPLIANCE ARCHITECTURE" prose block immediately before the EVALUATOR role header — not in a rationale section, not at the end — satisfies C-53 because the block is encountered at the workflow entry point, names both enforcement layers with mechanism descriptions, and states inter-layer ordering before either role begins. Proximity to the EVALUATOR header makes the declaration maximally co-located with the production-order constraint it governs.

```
You are executing the /topic:story skill for Signal plugin.

Topic: {{topic}}
Date: {{date}}

Produce artifact: simulations/topic/story/{{topic}}-story-{{date}}.md

---

=== PRE-ARTIFACT CHECKLIST ===

Complete before writing any section:

[ ] Signal artifacts loaded from simulations/{{topic}}/ — all namespaces scanned
[ ] EVALUATOR phase designated to complete S2 before AUTHOR phase begins S4b
[ ] S4b Part 1 will list only YES/PARTIAL signals from S2 (labeled with S2 verdict)
[ ] S4b Part 2 will draw only from Part 1 — not from independent signal review
[ ] S1 opening does not use a PROHIBITED OPENING CLASS
[ ] S5 NEXT STEP names TRIGGER, ACTION, and INERTIA-AT-TRIGGER as explicit fields

---

=== LIFECYCLE ===

PHASE 1 (Load): Scan simulations/{{topic}}/ — collect all signal artifacts across namespaces.
PHASE 2 (Evaluate): EVALUATOR role produces S2 verdicts. Named outputs required before PHASE 4.
PHASE 3 (Frame): AUTHOR produces S1 (question framing) and S3 (editorial rationale).
PHASE 4 (Author): AUTHOR produces S4b — draws from PHASE 2 verdict inventory. Successor to PHASE 2.
PHASE 5 (Close): AUTHOR produces S5 (recommendation). Write artifact to disk.

---

=== WORKFLOW COMPLIANCE ARCHITECTURE ===

This workflow contains two enforcement layers. Both apply on every execution.

Layer 1 — S4b Input-Constraint Partition (S4b structural architecture):
  S4b is divided into two stages. Part 1 enumerates only YES and PARTIAL signals
  from S2, labeled with their S2 verdict. Part 2 draws characterization exclusively
  from Part 1 — it may not independently reference the full signal set or add signals
  not present in Part 1's verdict inventory.
  Governing mechanism: structural partition with explicit input-scope constraint in Part 2.

Layer 2 — Evaluator-First Production Order (role sequence architecture):
  The EVALUATOR role produces S2 verdicts as named outputs before the AUTHOR role
  begins S4b. S4b authoring is a successor activity to evaluator verdict production.
  The constraint is temporal: S4b authoring cannot begin until S2 verdicts exist as
  discrete named artifacts.
  Governing mechanism: role boundary with named production-order sequence constraint.

Inter-Layer Ordering:
  Layer 2 governs WHEN S4b authoring begins — the EVALUATOR phase must complete
  before the AUTHOR enters S4b. Layer 1 governs WHAT S4b may contain once begun —
  Part 2 is constrained to Part 1's named signal inventory.
  Satisfying Layer 2 without Layer 1 produces a role-separated workflow with
  unconstrained S4b composition. Satisfying Layer 1 without Layer 2 produces a
  constrained S4b without temporal enforcement on when verdicts are produced.
  Both layers are required; neither substitutes for the other.

---

=== EVALUATOR ROLE ===

Produce S2 verdicts for all signals before handing off to AUTHOR.

**S2 — Signal Verdicts**

For each signal artifact in simulations/{{topic}}/:

  Signal: {signal-name} ({namespace})
  Verdict: YES | PARTIAL | MISS
  **Inertia verdict**: YES | NO | PARTIAL — does this signal address the inertia
    position (the status-quo path that competes with building this feature)?
  Key finding: {one sentence — the specific evidence this signal produced}

Verdict definitions:
  YES — signal speaks directly to the decision with usable evidence
  PARTIAL — signal touches the decision but with limited scope or mixed results
  MISS — signal does not contribute to the decision question

EVALUATOR phase is complete when all loaded signals have verdict entries. The
S2 verdict list is the exclusive input inventory for S4b Part 1. Transfer it to
AUTHOR before beginning any AUTHOR-phase sections.

---

=== AUTHOR ROLE ===

Receives the EVALUATOR's S2 verdict inventory. S4b Part 2 draws only from that inventory.

**S1 — What We Set Out to Understand**

PROHIBITED OPENING CLASS: Do not begin with "This synthesis," "This story,"
"This analysis," "This document," or any variant of "This [noun]." Do not begin
with a meta-description of the artifact. Begin with the question or the situation.

In 2–3 sentences in the author's voice: what was the decision question this topic
was opened to answer? What needed to be understood before committing? Frame it
as a question the team was carrying, not as a description of the artifact.

---

**S3 — Editorial Rationale**

In 1–2 sentences: what interpretive lens does this synthesis apply? What framing
shapes how the signals are read together?

**Disproof condition**: What evidence, if found in the signals, would falsify this
editorial reading? Name the specific finding that would reverse the interpretation.

---

**S4b — Synthesis**

**Part 1 — Verdict Inventory** *(EVALUATOR output — transferred verbatim)*

Copy the EVALUATOR's S2 verdict list here. Include only YES and PARTIAL signals.
Label each with its S2 verdict. Format:

  - {signal-name} ({namespace}) (S2 verdict: YES): {key finding, one sentence}
  - {signal-name} ({namespace}) (S2 verdict: PARTIAL): {key finding, one sentence}

MISS signals are excluded from Part 1. Do not add signals not present in S2
YES/PARTIAL verdicts. This list is the exclusive input set for Part 2. An evaluator
must be able to verify Part 2's characterization against this list without narrative
inference — every signal named in Part 2 must appear in Part 1.

**Part 2 — Characterization** *(This section draws only from Part 1 — not from an
independent review of all signals. Signals not named in Part 1 may not appear here.)*

Synthesize what the Part 1 signals say together. This is an editorial interpretation
in the author's voice — not a per-signal summary. What pattern emerges across the
Part 1 signals? What does the constellation reveal that no single signal reveals alone?

Inertia comparison: Do the Part 1 signals collectively challenge or reinforce the
status-quo path? State the synthesis-level inertia verdict and cross-reference the
Part 1 signals that most directly support or undercut it.

---

**S5 — Recommendation**

Para 1: What remains uncertain? Name the specific signal gap. Which Part 1 finding
is most challenged by this missing signal? Cross-reference it by signal name.

Para 2: State the recommendation — one of:
**Proceed** | **Pause** | **Pivot** | **Abandon**
One-sentence editorial rationale grounded in the Part 2 characterization.

Para 3 — NEXT STEP:
  TRIGGER: {the condition or event that initiates the next action}
  ACTION: {what the team does when the trigger fires}
  INERTIA-AT-TRIGGER: {what the status-quo path looks like at that same trigger point}

---

=== OUTPUT CONTRACT ===

G-1: Artifact written to simulations/topic/story/{{topic}}-story-{{date}}.md. Path echoed.
G-2: S2 entries use format: Signal / Verdict / Inertia verdict / Key finding.
G-3: S4b Part 1 contains only YES/PARTIAL signals from S2, each labeled with S2 verdict.
G-4: S4b Part 2 names no signal not listed in Part 1.
G-5: S5 Para 3 contains TRIGGER, ACTION, and INERTIA-AT-TRIGGER as named fields.
```

---

## V-02

**Axis**: Output Format — three-column compliance architecture table; S4b Part 1 as table
**Hypothesis**: A structured three-column table (Layer | Enforcement Mechanism | Inter-Layer Ordering) satisfies C-53 more auditably than prose because the column structure mechanically enforces completeness — each row must carry all three fields — the row count makes the declared layer count explicit and verifiable in one scan, and the "Inter-Layer Ordering" column forces an ordering statement per layer rather than allowing it to be absorbed into a concluding prose sentence that could be omitted. The table format also applies to S4b Part 1 (verdict inventory), making the signal-to-verdict mapping auditable in tabular form.

```
You are executing the /topic:story skill for Signal plugin.

Topic: {{topic}}
Date: {{date}}

Produce artifact: simulations/topic/story/{{topic}}-story-{{date}}.md

---

=== PRE-ARTIFACT CHECKLIST ===

Complete before writing any section:

[ ] Signal artifacts loaded from simulations/{{topic}}/ — all namespaces scanned
[ ] EVALUATOR phase designated to complete S2 before AUTHOR phase begins S4b
[ ] S4b Part 1 will list only YES/PARTIAL signals from S2 (labeled with S2 verdict)
[ ] S4b Part 2 will draw only from Part 1 — not from independent signal review
[ ] S1 opening does not use a PROHIBITED OPENING CLASS
[ ] S5 NEXT STEP names TRIGGER, ACTION, and INERTIA-AT-TRIGGER as explicit fields

---

=== LIFECYCLE ===

PHASE 1 (Load): Scan simulations/{{topic}}/ — collect all signal artifacts across namespaces.
PHASE 2 (Evaluate): EVALUATOR role produces S2 verdicts. Named outputs required before PHASE 4.
PHASE 3 (Frame): AUTHOR produces S1 (question framing) and S3 (editorial rationale).
PHASE 4 (Author): AUTHOR produces S4b — draws from PHASE 2 verdict inventory. Successor to PHASE 2.
PHASE 5 (Close): AUTHOR produces S5 (recommendation). Write artifact to disk.

---

=== WORKFLOW COMPLIANCE ARCHITECTURE ===

| Layer | Enforcement Mechanism | Inter-Layer Ordering |
|-------|----------------------|----------------------|
| Layer 1 — S4b input-constraint partition | S4b is structurally divided into Part 1 (verdict inventory: YES/PARTIAL signals from S2, labeled with verdict) and Part 2 (characterization constrained to Part 1 inputs only — may not reference signals outside Part 1). | Downstream of Layer 2: Part 1 draws from S2 verdicts that Layer 2 ensures exist before S4b begins. Layer 1 governs WHAT S4b may contain once the Layer 2 entry gate is passed. |
| Layer 2 — Evaluator-first production order | EVALUATOR role produces S2 verdicts as named outputs before AUTHOR role begins S4b. S4b authoring is a designated successor activity to evaluator verdict production. | Upstream of Layer 1: Layer 2 governs WHEN S4b authoring begins — the EVALUATOR phase must complete before the AUTHOR enters S4b. Satisfying Layer 1 without Layer 2 produces a constrained S4b without temporal enforcement on when verdicts exist. |

Declared layer count: 2. Implemented enforcement mechanisms: 2. Count matches.

---

=== EVALUATOR ROLE ===

Produce S2 verdicts for all signals before handing off to AUTHOR.

**S2 — Signal Verdicts**

For each signal artifact in simulations/{{topic}}/:

  Signal: {signal-name} ({namespace})
  Verdict: YES | PARTIAL | MISS
  **Inertia verdict**: YES | NO | PARTIAL — does this signal address the inertia
    position (the status-quo path that competes with building this feature)?
  Key finding: {one sentence — the specific evidence this signal produced}

Verdict definitions:
  YES — signal speaks directly to the decision with usable evidence
  PARTIAL — signal touches the decision but with limited scope or mixed results
  MISS — signal does not contribute to the decision question

EVALUATOR phase is complete when all loaded signals have verdict entries.
Transfer the S2 verdict list to AUTHOR as the exclusive input for S4b Part 1.

---

=== AUTHOR ROLE ===

Receives the EVALUATOR's S2 verdict inventory. S4b Part 2 draws only from that inventory.

**S1 — What We Set Out to Understand**

PROHIBITED OPENING CLASS: Do not begin with "This synthesis," "This story,"
"This analysis," "This document," or any variant of "This [noun]." Begin with
the question or the situation.

In 2–3 sentences in the author's voice: what was the decision question? What
needed to be understood before committing?

---

**S3 — Editorial Rationale**

In 1–2 sentences: what interpretive lens does this synthesis apply?

**Disproof condition**: What evidence would falsify this editorial reading?

---

**S4b — Synthesis**

**Part 1 — Verdict Inventory** *(EVALUATOR output — transferred verbatim from S2)*

Transfer YES and PARTIAL signals only. Format as table:

| Signal | Namespace | S2 Verdict | Inertia Verdict | Key Finding |
|--------|-----------|------------|-----------------|-------------|
| {name} | {ns} | YES | YES/NO/PARTIAL | {one sentence} |
| {name} | {ns} | PARTIAL | YES/NO/PARTIAL | {one sentence} |

MISS signals are excluded. Do not add rows not present in S2 YES/PARTIAL verdicts.
This table is the exclusive input set for Part 2. Row count in Part 2 references
must not exceed row count in Part 1.

**Part 2 — Characterization** *(This section draws only from Part 1 — not from an
independent review of all signals. Signals not named in Part 1 may not appear here.)*

Synthesize what the Part 1 signals say together — an editorial interpretation in
the author's voice, not a per-row summary. What pattern emerges? What does the
constellation reveal that no single signal reveals alone?

Inertia comparison: Do the Part 1 signals collectively challenge or reinforce the
status-quo path? State the synthesis-level inertia verdict.

---

**S5 — Recommendation**

Para 1: What remains uncertain? Name the specific signal gap and cross-reference
the Part 1 finding most challenged by this gap.

Para 2: **Proceed** | **Pause** | **Pivot** | **Abandon** — one-sentence rationale
grounded in Part 2 characterization.

Para 3 — NEXT STEP:
  TRIGGER: {condition that initiates the next action}
  ACTION: {what the team does when trigger fires}
  INERTIA-AT-TRIGGER: {what the status-quo path looks like at that same trigger}

---

=== OUTPUT CONTRACT ===

G-1: Artifact written to simulations/topic/story/{{topic}}-story-{{date}}.md. Path echoed.
G-2: S2 entries use format: Signal / Verdict / Inertia verdict / Key finding.
G-3: S4b Part 1 is a table with columns: Signal / Namespace / S2 Verdict / Inertia Verdict / Key Finding. Contains only YES/PARTIAL signals.
G-4: S4b Part 2 names no signal not present in Part 1 table.
G-5: S5 Para 3 contains TRIGGER, ACTION, and INERTIA-AT-TRIGGER as named fields.
```

---

## V-03

**Axis**: Lifecycle Emphasis — annotated phase diagram serves as the compliance architecture declaration
**Hypothesis**: The C-53 pass condition explicitly names "a phase-diagram legend with criterion annotations" as an acceptable form for the compliance architecture declaration. V-03 tests this path directly: the lifecycle phase diagram is expanded with per-phase enforcement annotations and a "Layer Legend" subsection immediately following it. This positions the declaration inside the most prominent structural element of the workflow — the phase diagram every evaluator reads first — rather than in a separate block that could be read as commentary. The diagram IS the compliance architecture declaration; no separate block exists.

```
You are executing the /topic:story skill for Signal plugin.

Topic: {{topic}}
Date: {{date}}

Produce artifact: simulations/topic/story/{{topic}}-story-{{date}}.md

---

=== PRE-ARTIFACT CHECKLIST ===

Complete before writing any section:

[ ] Signal artifacts loaded from simulations/{{topic}}/ — all namespaces scanned
[ ] EVALUATOR phase designated to complete S2 before AUTHOR phase begins S4b
[ ] S4b Part 1 will list only YES/PARTIAL signals from S2 (labeled with S2 verdict)
[ ] S4b Part 2 will draw only from Part 1 — not from independent signal review
[ ] S1 opening does not use a PROHIBITED OPENING CLASS
[ ] S5 NEXT STEP names TRIGGER, ACTION, and INERTIA-AT-TRIGGER as explicit fields

---

=== LIFECYCLE AND COMPLIANCE ARCHITECTURE ===

```
PHASE 1 (Load)
    ↓
PHASE 2 (Evaluate) [LAYER 2: evaluator-first production order]
    ↓  ← ENTRY GATE: S2 verdicts must exist as named outputs before PHASE 4 begins
PHASE 3 (Frame)
    ↓
PHASE 4 (Author) [LAYER 1: S4b input-constraint partition]
    ↓  ← COMPOSITION GATE: Part 2 may only draw from Part 1 verdict inventory
PHASE 5 (Close)
```

**Layer Legend**

Layer 1 — S4b Input-Constraint Partition [governs PHASE 4 internal composition]:
  S4b is structurally divided into Part 1 (verdict inventory — YES/PARTIAL signals
  from S2, labeled with S2 verdict) and Part 2 (characterization constrained to
  Part 1 inputs only). Part 2 may not reference signals outside Part 1. This is
  an architectural partition enforced by explicit scope-restriction in Part 2's slot.

Layer 2 — Evaluator-First Production Order [governs PHASE 2 → PHASE 4 transition]:
  EVALUATOR role produces S2 verdicts as named outputs in PHASE 2. PHASE 4 (S4b
  authoring) is a designated successor to PHASE 2. S4b authoring cannot begin
  before PHASE 2 outputs exist. This is a temporal constraint enforced by
  role-boundary and phase-sequence prerequisite.

Inter-Layer Ordering:
  Layer 2 governs the phase transition gate (WHEN PHASE 4 begins).
  Layer 1 governs PHASE 4's internal composition constraint (WHAT Part 2 may contain
  once PHASE 4 is entered).
  Layer 2 is the entry condition; Layer 1 is the composition constraint.
  The two layers are orthogonal — each operates at a different point in the execution
  sequence and each has a distinct failure mode if violated independently.

Declared layer count: 2. Implemented enforcement mechanisms: 2. Count matches.

---

=== EVALUATOR ROLE ===

Produce S2 verdicts for all signals (PHASE 2). This phase must complete before
the AUTHOR begins S4b (PHASE 4).

**S2 — Signal Verdicts**

For each signal artifact in simulations/{{topic}}/:

  Signal: {signal-name} ({namespace})
  Verdict: YES | PARTIAL | MISS
  **Inertia verdict**: YES | NO | PARTIAL — does this signal address the inertia
    position (the status-quo path that competes with building this feature)?
  Key finding: {one sentence — the specific evidence this signal produced}

Verdict definitions:
  YES — signal speaks directly to the decision with usable evidence
  PARTIAL — signal touches the decision but with limited scope or mixed results
  MISS — signal does not contribute to the decision question

PHASE 2 is complete when all loaded signals have verdict entries. Transfer the
verdict list to AUTHOR as the PHASE 4 input inventory (S4b Part 1 source).

---

=== AUTHOR ROLE ===

Receives the EVALUATOR's S2 verdict inventory (PHASE 2 output). Begin PHASE 3.

**S1 — What We Set Out to Understand** *(PHASE 3)*

PROHIBITED OPENING CLASS: Do not begin with "This synthesis," "This story,"
"This analysis," "This document," or any variant of "This [noun]." Begin with
the question or the situation.

In 2–3 sentences in the author's voice: what was the decision question? What
needed to be understood before committing?

---

**S3 — Editorial Rationale** *(PHASE 3)*

In 1–2 sentences: what interpretive lens does this synthesis apply?

**Disproof condition**: What evidence would falsify this editorial reading?

---

**S4b — Synthesis** *(PHASE 4 — requires PHASE 2 outputs as input)*

**Part 1 — Verdict Inventory** *(EVALUATOR output — transferred verbatim)*

List only YES and PARTIAL signals from S2, labeled with S2 verdict:

  - {signal-name} ({namespace}) (S2 verdict: YES): {key finding, one sentence}
  - {signal-name} ({namespace}) (S2 verdict: PARTIAL): {key finding, one sentence}

MISS signals are excluded. Do not add signals not present in S2 YES/PARTIAL verdicts.
This list is the exclusive input for Part 2. An evaluator verifying Layer 1 compliance
checks that every signal in Part 2 appears in Part 1.

**Part 2 — Characterization** *(This section draws only from Part 1 — not from an
independent review of all signals. Signals not named in Part 1 may not appear here.)*

Synthesize what the Part 1 signals say together — an editorial interpretation in
the author's voice, not a per-signal summary. What pattern emerges? What does the
constellation reveal that no single signal reveals alone?

Inertia comparison: Do the Part 1 signals collectively challenge or reinforce the
status-quo path? State the synthesis-level inertia verdict.

---

**S5 — Recommendation** *(PHASE 5)*

Para 1: What remains uncertain? Name the specific signal gap and cross-reference
the Part 1 finding most challenged by this gap.

Para 2: **Proceed** | **Pause** | **Pivot** | **Abandon** — one-sentence rationale
grounded in Part 2 characterization.

Para 3 — NEXT STEP:
  TRIGGER: {condition that initiates the next action}
  ACTION: {what the team does when trigger fires}
  INERTIA-AT-TRIGGER: {what the status-quo path looks like at that same trigger}

---

=== OUTPUT CONTRACT ===

G-1: Artifact written to simulations/topic/story/{{topic}}-story-{{date}}.md. Path echoed.
G-2: S2 entries use format: Signal / Verdict / Inertia verdict / Key finding.
G-3: S4b Part 1 contains only YES/PARTIAL signals from S2, each labeled with S2 verdict.
G-4: S4b Part 2 names no signal not listed in Part 1.
G-5: S5 Para 3 contains TRIGGER, ACTION, and INERTIA-AT-TRIGGER as named fields.
```

---

## V-04

**Axis**: Combined — Role Sequence (V-01 positioning) + Output Format (V-02 table)
**Hypothesis**: The V-01 prose block correctly positions the declaration at the workflow entry point (co-located with the role sequence header) but prose form may allow ordering statements to compress into sentences that blur the per-layer structure. The V-02 table correctly enforces per-layer completeness but is structurally orphaned if not co-located with the role sequence. V-04 combines both: a three-column table placed immediately before the EVALUATOR header. The table format makes the declaration auditable in one scan; the positioning ensures the evaluator encounters it at the production-sequence entry point. Prediction: cleaner C-53 satisfaction than either single-axis variation, and the table format may also resolve the inherited PARTIAL on a structural transparency criterion in C-08–C-50 that prose declarations leave ambiguous.

```
You are executing the /topic:story skill for Signal plugin.

Topic: {{topic}}
Date: {{date}}

Produce artifact: simulations/topic/story/{{topic}}-story-{{date}}.md

---

=== PRE-ARTIFACT CHECKLIST ===

Complete before writing any section:

[ ] Signal artifacts loaded from simulations/{{topic}}/ — all namespaces scanned
[ ] EVALUATOR phase designated to complete S2 before AUTHOR phase begins S4b
[ ] S4b Part 1 will list only YES/PARTIAL signals from S2 (labeled with S2 verdict)
[ ] S4b Part 2 will draw only from Part 1 — not from independent signal review
[ ] S1 opening does not use a PROHIBITED OPENING CLASS
[ ] S5 NEXT STEP names TRIGGER, ACTION, and INERTIA-AT-TRIGGER as explicit fields

---

=== LIFECYCLE ===

PHASE 1 (Load): Scan simulations/{{topic}}/ — collect all signal artifacts across namespaces.
PHASE 2 (Evaluate): EVALUATOR role produces S2 verdicts. Named outputs required before PHASE 4.
PHASE 3 (Frame): AUTHOR produces S1 (question framing) and S3 (editorial rationale).
PHASE 4 (Author): AUTHOR produces S4b — draws from PHASE 2 verdict inventory. Successor to PHASE 2.
PHASE 5 (Close): AUTHOR produces S5 (recommendation). Write artifact to disk.

---

=== WORKFLOW COMPLIANCE ARCHITECTURE ===

Declared layers: 2. Implemented enforcement mechanisms: 2. Counts match.

| Layer | Enforcement Mechanism | Inter-Layer Ordering |
|-------|----------------------|----------------------|
| **Layer 1** S4b input-constraint partition | S4b divides into Part 1 (verdict inventory — YES/PARTIAL signals from S2 with S2 verdict label) and Part 2 (characterization constrained to Part 1 inputs only; signals not in Part 1 may not appear in Part 2). Partition enforced by explicit scope-restriction in Part 2 slot. | **Downstream of Layer 2.** Governs WHAT Part 2 may contain once S4b authoring begins. Failure mode if violated alone: unconstrained S4b composition despite verdicts existing. |
| **Layer 2** Evaluator-first production order | EVALUATOR role produces S2 verdicts as named outputs before AUTHOR role begins S4b. S4b authoring is a designated successor activity — the workflow sequence designates PHASE 4 as downstream of PHASE 2. Constraint is temporal: S4b cannot begin until S2 verdicts exist as discrete artifacts. | **Upstream of Layer 1.** Governs WHEN S4b authoring begins — EVALUATOR phase must complete first. Failure mode if violated alone: constrained S4b architecture with no production-order guarantee on when verdicts are produced. |

---

=== EVALUATOR ROLE ===

Produce S2 verdicts for all signals (PHASE 2) before the AUTHOR begins S4b (PHASE 4).

**S2 — Signal Verdicts**

For each signal artifact in simulations/{{topic}}/:

  Signal: {signal-name} ({namespace})
  Verdict: YES | PARTIAL | MISS
  **Inertia verdict**: YES | NO | PARTIAL — does this signal address the inertia
    position (the status-quo path that competes with building this feature)?
  Key finding: {one sentence — the specific evidence this signal produced}

Verdict definitions:
  YES — signal speaks directly to the decision with usable evidence
  PARTIAL — signal touches the decision but with limited scope or mixed results
  MISS — signal does not contribute to the decision question

EVALUATOR phase is complete when all loaded signals have verdict entries. Transfer
the verdict list to AUTHOR. This list is the Layer 1 input inventory for S4b Part 1.

---

=== AUTHOR ROLE ===

Receives EVALUATOR's S2 verdict inventory. S4b Part 2 draws only from that inventory.

**S1 — What We Set Out to Understand**

PROHIBITED OPENING CLASS: Do not begin with "This synthesis," "This story,"
"This analysis," "This document," or any variant of "This [noun]." Begin with
the question or the situation.

In 2–3 sentences in the author's voice: what was the decision question? What
needed to be understood before committing?

---

**S3 — Editorial Rationale**

In 1–2 sentences: what interpretive lens does this synthesis apply?

**Disproof condition**: What evidence would falsify this editorial reading?

---

**S4b — Synthesis**

**Part 1 — Verdict Inventory** *(EVALUATOR output — transferred verbatim)*

Transfer YES and PARTIAL signals only. Format as table:

| Signal | Namespace | S2 Verdict | Inertia Verdict | Key Finding |
|--------|-----------|------------|-----------------|-------------|
| {name} | {ns} | YES | YES/NO/PARTIAL | {one sentence} |
| {name} | {ns} | PARTIAL | YES/NO/PARTIAL | {one sentence} |

MISS signals are excluded. Do not add rows for signals not present in S2
YES/PARTIAL verdicts. This table is the exclusive input set for Part 2. An
evaluator verifying Layer 1 compliance checks that (a) all Part 2 signal
references appear in this table, and (b) no row present here is from S2 MISS.

**Part 2 — Characterization** *(This section draws only from Part 1 — not from
an independent review of all signals. Signals not in Part 1 table may not appear here.)*

Synthesize what the Part 1 signals say together — an editorial interpretation in
the author's voice, not a per-row summary. What pattern emerges? What does the
constellation reveal that no single signal reveals alone?

Inertia comparison: Do the Part 1 signals collectively challenge or reinforce the
status-quo path? State the synthesis-level inertia verdict and identify which Part 1
signals carry the most weight in the inertia determination.

---

**S5 — Recommendation**

Para 1: What remains uncertain? Name the specific signal gap and cross-reference
the Part 1 finding most challenged by this gap.

Para 2: **Proceed** | **Pause** | **Pivot** | **Abandon** — one-sentence rationale
grounded in Part 2 characterization.

Para 3 — NEXT STEP:
  TRIGGER: {condition that initiates the next action}
  ACTION: {what the team does when trigger fires}
  INERTIA-AT-TRIGGER: {what the status-quo path looks like at that same trigger}

---

=== OUTPUT CONTRACT ===

G-1: Artifact written to simulations/topic/story/{{topic}}-story-{{date}}.md. Path echoed.
G-2: S2 entries use format: Signal / Verdict / Inertia verdict / Key finding.
G-3: S4b Part 1 is a table with columns: Signal / Namespace / S2 Verdict / Inertia Verdict / Key Finding. Contains only YES/PARTIAL signals.
G-4: S4b Part 2 names no signal not present in Part 1 table.
G-5: S5 Para 3 contains TRIGGER, ACTION, and INERTIA-AT-TRIGGER as named fields.
```

---

## V-05

**Axis**: Combined — Role Sequence + Lifecycle (annotated phase diagram) + Output Format (table) + three declared layers
**Hypothesis**: R17 V-05 had three enforcement mechanisms — EVALUATOR/AUTHOR role boundary, S4b structural partition, and phase-sequence prerequisites — but declared zero of them as an architecture. C-53 fires on this gap. V-05 closes it by declaring all three mechanisms as a named three-layer architecture in a table co-located with the lifecycle diagram. Layer 3 (phase-sequence prerequisites) is named explicitly as a distinct enforcement mechanism that reinforces Layer 2 through an independent path. The declared layer count (3) matches the implemented mechanism count (3). The inter-layer ordering states both that Layer 3 reinforces Layer 2 (redundant entry-gate enforcement) and that Layer 1 operates downstream of both — a compound entry gate and a composition gate, declared as a system. This transforms V-05's three-mechanism architecture from emergent coexistence into declared architecture. Prediction: C-53 PASS, and if the inherited PARTIAL on C-08–C-50 was caused by the undeclared phase-diagram enforcement not satisfying structural transparency, this round's explicit declaration may convert that PARTIAL to FULL.

```
You are executing the /topic:story skill for Signal plugin.

Topic: {{topic}}
Date: {{date}}

Produce artifact: simulations/topic/story/{{topic}}-story-{{date}}.md

---

=== PRE-ARTIFACT CHECKLIST ===

Complete before writing any section:

[ ] Signal artifacts loaded from simulations/{{topic}}/ — all namespaces scanned
[ ] EVALUATOR phase designated to complete S2 before AUTHOR phase begins S4b
[ ] S4b Part 1 will list only YES/PARTIAL signals from S2 (labeled with S2 verdict)
[ ] S4b Part 2 will draw only from Part 1 — not from independent signal review
[ ] S1 opening does not use a PROHIBITED OPENING CLASS
[ ] S5 NEXT STEP names TRIGGER, ACTION, and INERTIA-AT-TRIGGER as explicit fields

---

=== LIFECYCLE AND COMPLIANCE ARCHITECTURE ===

```
PHASE 1 (Load)
    ↓
PHASE 2 (Evaluate) [LAYER 2 + LAYER 3: evaluator-first production order]
    ↓  ← ENTRY GATE A: EVALUATOR role boundary (Layer 2)
    ↓  ← ENTRY GATE B: phase-sequence prerequisite (Layer 3)
PHASE 3 (Frame)
    ↓
PHASE 4 (Author) [LAYER 1: S4b input-constraint partition]
    ↓  ← COMPOSITION GATE: Part 2 draws only from Part 1 verdict inventory
PHASE 5 (Close)
```

**Compliance Architecture — Declared Layers**

Declared layers: 3. Implemented enforcement mechanisms: 3. Counts match.

| Layer | Enforcement Mechanism | Governing Element | Inter-Layer Ordering |
|-------|----------------------|------------------|----------------------|
| **Layer 1** S4b input-constraint partition | S4b divides into Part 1 (verdict inventory — YES/PARTIAL signals from S2 with S2 verdict label) and Part 2 (characterization constrained to Part 1 inputs only; signals not in Part 1 may not appear in Part 2). Enforced by explicit scope-restriction in Part 2 slot. | PHASE 4 internal composition | **Downstream of Layers 2 and 3.** Governs WHAT Part 2 may contain once the entry gate (Layers 2+3) is passed. Failure mode if violated alone: unconstrained S4b composition despite Layers 2+3 enforcing correct entry timing. |
| **Layer 2** Evaluator-first role sequence | EVALUATOR role produces S2 verdicts as named outputs before AUTHOR role begins S4b. Role boundary designates S4b authoring as a successor activity to evaluator verdict production. Enforced by explicit EVALUATOR/AUTHOR role labels and production-order sequence constraint. | PHASE 2 → PHASE 4 role transition | **Upstream of Layer 1; parallel with Layer 3.** Governs WHEN S4b authoring begins via role boundary. Layer 3 provides a second independent enforcement path for the same entry gate. Failure mode if violated alone: S4b authored before verdicts exist as discrete artifacts, despite Layer 1 partition being structurally present. |
| **Layer 3** Phase-sequence prerequisites | Phase diagram designates PHASE 2 as a formal prerequisite for PHASE 4. The phase sequence makes S4b authoring structurally downstream of evaluator verdict production independent of role labels — the phase gate enforces the same constraint as Layer 2 through a different mechanism (phase ordering rather than role boundary). | PHASE 2 → PHASE 4 phase gate | **Upstream of Layer 1; parallel with Layer 2.** Reinforces Layer 2 through a distinct audit surface — Layer 2 is verifiable by inspecting role labels; Layer 3 is verifiable by inspecting the phase sequence. Either layer's enforcement survives removal of the other. Both govern the same transition gate (PHASE 2 → PHASE 4) through independent paths. |

**Inter-Layer Ordering Summary**:
Layers 2 and 3 are co-equal entry-gate mechanisms — both govern when S4b authoring begins, through independent paths (role boundary and phase sequence). Layer 1 operates downstream: it governs what S4b may contain once the Layers 2+3 entry gate is passed. A rubric satisfying Layers 2+3 but not Layer 1 produces a temporally enforced workflow with unconstrained composition. A rubric satisfying Layer 1 but not Layers 2+3 produces a constrained composition architecture without temporal production-order enforcement.

---

=== EVALUATOR ROLE ===

Produce S2 verdicts for all signals (PHASE 2). PHASE 4 (S4b authoring) cannot begin
until this phase is complete.

**S2 — Signal Verdicts**

For each signal artifact in simulations/{{topic}}/:

  Signal: {signal-name} ({namespace})
  Verdict: YES | PARTIAL | MISS
  **Inertia verdict**: YES | NO | PARTIAL — does this signal address the inertia
    position (the status-quo path that competes with building this feature)?
  Key finding: {one sentence — the specific evidence this signal produced}

Verdict definitions:
  YES — signal speaks directly to the decision with usable evidence
  PARTIAL — signal touches the decision but with limited scope or mixed results
  MISS — signal does not contribute to the decision question

PHASE 2 is complete when all loaded signals have verdict entries. Transfer the
full verdict list to AUTHOR. This is the Layer 1 input inventory for S4b Part 1.
PHASE 4 (S4b authoring) may begin only after this transfer is complete.

---

=== AUTHOR ROLE ===

Receives EVALUATOR's S2 verdict inventory (PHASE 2 output). Begin PHASE 3, then PHASE 4.

**S1 — What We Set Out to Understand** *(PHASE 3)*

PROHIBITED OPENING CLASS: Do not begin with "This synthesis," "This story,"
"This analysis," "This document," or any variant of "This [noun]." Begin with
the question or the situation.

In 2–3 sentences in the author's voice: what was the decision question? What
needed to be understood before committing?

---

**S3 — Editorial Rationale** *(PHASE 3)*

In 1–2 sentences: what interpretive lens does this synthesis apply?

**Disproof condition**: What evidence would falsify this editorial reading?

---

**S4b — Synthesis** *(PHASE 4 — entry requires PHASE 2 outputs; composition governed by Layer 1)*

**Part 1 — Verdict Inventory** *(EVALUATOR output — transferred verbatim from S2)*

Transfer YES and PARTIAL signals only. Format as table:

| Signal | Namespace | S2 Verdict | Inertia Verdict | Key Finding |
|--------|-----------|------------|-----------------|-------------|
| {name} | {ns} | YES | YES/NO/PARTIAL | {one sentence} |
| {name} | {ns} | PARTIAL | YES/NO/PARTIAL | {one sentence} |

MISS signals are excluded. Do not add rows for signals not present in S2
YES/PARTIAL verdicts. This table is the Layer 1 input inventory — the exclusive
source for Part 2. An evaluator verifying Layer 1 compliance confirms: (a) every
signal named in Part 2 appears in this table, (b) no MISS signal appears as a row,
(c) S2 verdict labels are present on every row.

**Part 2 — Characterization** *(This section draws only from Part 1 — not from
an independent review of all signals. Signals not in the Part 1 table may not appear here.)*

Synthesize what the Part 1 signals say together — an editorial interpretation in
the author's voice, not a per-row summary. What pattern emerges? What does the
constellation reveal that no single signal reveals alone?

Inertia comparison: Do the Part 1 signals collectively challenge or reinforce the
status-quo path? State the synthesis-level inertia verdict and identify which
Part 1 signals carry the most weight in the inertia determination.

---

**S5 — Recommendation** *(PHASE 5)*

Para 1: What remains uncertain? Name the specific signal gap and cross-reference
the Part 1 finding most challenged by this gap (use the table row's Signal name).

Para 2: **Proceed** | **Pause** | **Pivot** | **Abandon** — one-sentence rationale
grounded in Part 2 characterization.

Para 3 — NEXT STEP:
  TRIGGER: {condition that initiates the next action}
  ACTION: {what the team does when trigger fires}
  INERTIA-AT-TRIGGER: {what the status-quo path looks like at that same trigger}

---

=== OUTPUT CONTRACT ===

G-1: Artifact written to simulations/topic/story/{{topic}}-story-{{date}}.md. Path echoed.
G-2: S2 entries use format: Signal / Verdict / Inertia verdict / Key finding.
G-3: S4b Part 1 is a table with columns: Signal / Namespace / S2 Verdict / Inertia Verdict / Key Finding. Contains only YES/PARTIAL signals.
G-4: S4b Part 2 names no signal not present in Part 1 table.
G-5: S5 Para 3 contains TRIGGER, ACTION, and INERTIA-AT-TRIGGER as named fields.
G-6: Compliance architecture table declares 3 layers; implemented mechanisms are 3; counts match.
```

---

## Variation Summary

| Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| C-53 declaration form | prose block | 3-col table | phase-diagram legend | 3-col table | 4-col table |
| C-53 declaration location | before EVALUATOR header | before EVALUATOR header | inside lifecycle section | before EVALUATOR header | inside lifecycle section |
| Declared layer count | 2 | 2 | 2 | 2 | **3** |
| Layer 3 (phase prerequisites) declared | NO | NO | NO | NO | YES |
| S4b Part 1 format | bullet list | table | bullet list | **table** | table |
| Lifecycle diagram annotated | NO | NO | **YES** | NO | YES |
| Explicit "counts match" assertion | NO | YES | YES | YES | YES |
| Predicted C-53 result | PASS | PASS | PASS | PASS | PASS |
| Predicted inherited PARTIAL resolution | stays PARTIAL | possible FULL | possible FULL | possible FULL | likely FULL |

**Score ceiling**: V-05 targets 90 + (29 × 0.2174) + (0 PARTIAL) = **96.30** if PARTIAL converts to FULL, or 90 + (29 × 0.2174) + (1 × 0.1087) = **96.41** if PARTIAL stays. The PARTIAL resolution is the R18 discriminator between variations — all five are expected to pass C-53, so the score spread will be determined by whether the table format + explicit layer-count assertion closes the structural transparency gap that produced the inherited PARTIAL.
