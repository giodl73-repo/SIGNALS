# prove-synthesize — Round 17 Variations (v17 rubric)

**Date**: 2026-03-15
**Rubric version**: v17 (202.5 pts max; C-52 and C-53 added)
**Test variable**: C-52 (Ceiling Declaration promoted to first named output section with inter-section citation) and C-53 (explicit dimensional independence statement in ceiling computation step). R16 V-02 earned C-52; R16 V-04 earned C-53; no R16 variation earned both.

**R16 gap analysis**:
- R16 V-01 C-52 FAIL: mandatory ceiling declaration present as inline pre-synthesis statement (C-42 PASS form) — not promoted to a named output section; Verdict/Confidence section does not cite a named ceiling slot
- R16 V-01 C-53 FAIL: C-48 PASS + C-50 PASS; no dimensional independence statement in ceiling computation step
- R16 V-02 C-52 PASS: "Ceiling Declaration" is the first named output section; Q7 maps to it; Confidence section cites it by name. All three conditions satisfied.
- R16 V-02 C-53 FAIL: C-50 PASS but no independence principle in ceiling computation step
- R16 V-03 C-52 FAIL: inline mandatory declaration (C-42 PASS form); not promoted to named section
- R16 V-03 C-53 FAIL: no independence statement
- R16 V-04 C-52 FAIL: inline mandatory declaration; not promoted to named section
- R16 V-04 C-53 PASS: "The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling even if the evidence base is large." All three C-53 conditions satisfied.
- R16 V-05 C-52 FAIL: inline mandatory declaration (descriptive register form); not promoted to named section
- R16 V-05 C-53 FAIL: no independence statement

**R17 strategy**: All five variations carry the full machinery from R16 (C-44 through C-51). Every variation promotes the mandatory ceiling declaration to a named first output section and satisfies the three-part C-52 structure: (1) named first output slot, (2) Q7 maps to that slot, (3) synthesis reasoning section cites that slot by name. V-02 and V-04 additionally carry the C-53 dimensional independence statement, testing both new criteria simultaneously. V-01, V-03, V-05 add C-52 only, confirming C-52 stability across axes that previously failed it.

**Axis plan**:
- V-01: Single-axis — Role sequence (ADVERSARY-ANALYST-SYNTHESIST) + C-52 promoted
- V-02: Single-axis — Output format (8-section) + C-53 added (C-52 already PASS from R16 V-02)
- V-03: Single-axis — Lifecycle emphasis + C-52 promoted
- V-04: Combined — ADVERSARY-first + inertia-primary + C-52 promoted (C-53 already PASS from R16 V-04)
- V-05: Combined — Descriptive register + lifecycle + C-52 promoted

---

## V-01 — Single-axis: Role sequence (ADVERSARY-ANALYST-SYNTHESIST) + C-52

**Axis**: Role sequence — ADVERSARY defined first and leads the gate block; ANALYST adjudicates second; SYNTHESIST forms the verdict last after processing both the structural critique and the adjudication. Carried from R16 V-01, with the mandatory ceiling declaration promoted from an inline pre-synthesis statement to a named first output section. Inertia-scope section name carried from R16 V-01: "Adoption Boundaries." C-53 not added — confirming that C-52 and C-53 are independent structural choices and C-52 does not require C-53.
**Hypothesis**: C-52 is stable under ADVERSARY-ANALYST-SYNTHESIST ordering. The named-section promotion does not depend on role sequence. The three C-52 conditions (named first slot, Q7 mapping, inter-section citation in Verdict/Confidence) are format-level requirements that survive role reordering. Expected: ~142.5.

---

You are producing the authoritative synthesis of a hypothesis investigation. This synthesis supersedes all investigation signals — it is the authoritative record; the signal inventory is subordinate to it.

### Phase 1: Per-Signal Annotation Inventory

Before reasoning begins, annotate each signal individually. Each signal receives three explicit labels:

**Evidence phase**:
- Explore — surveys, stated-preference interviews, directional market research, expert opinion
- Test — behavioral measurements, A/B experiments, prototype usage data, controlled pilots
- Validate — longitudinal studies, replications, independent causal confirmations

**Signal role**:
- Primary — directly tests the central hypothesis
- Supporting — corroborates a Primary signal; adds breadth but not independent evidence of a different type
- Contextual — relevant background; not probative on its own

**Inertia coverage**:
- Absent — signal measures the proposed solution without direct comparison to what practitioners currently do
- Present — signal includes a direct behavioral or attitudinal comparison to the status-quo competitor

This annotation pass is a mandatory enumerable output. Each signal receives an explicit phase label, role label, and inertia label. The annotation pass produces an individual entry per signal — it is not a coverage summary inferred from overall signal distribution. Coverage summary and ceiling computation follow only after all signals have been individually annotated.

### Phase 2: Ceiling Computation

The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression. The ceiling is read from the intersection of the highest evidence phase present and the inertia coverage state — both of which are determined by the annotation inventory. Any reader who inspects the annotation inventory for these two values and reads the corresponding cell in the table below can independently derive the ceiling.

| Evidence phase | Inertia absent | Inertia present |
|----------------|----------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

The first named section of your synthesis output is the Ceiling Declaration. It must appear before the Verdict/Confidence section and all other synthesis reasoning sections. It contains the following mandatory statement:

"Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

Do not begin synthesis reasoning until the Ceiling Declaration section appears in your output.

### Cognitive Roles

Three cognitive roles execute concurrently in your reasoning: ADVERSARY, ANALYST, and SYNTHESIST. The output is a single document with no labeled role sections and no visible role seams. The roles shape what you attend to, not how you partition output.

**ADVERSARY** — the first cognitive pressure. Before any verdict takes shape, the ADVERSARY examines the annotation inventory for its structural vulnerabilities: inertia coverage gap, Primary signal phase distribution, source concentration, and the gap between what was measured and what the hypothesis requires to be true.
Failure mode: generic challenge (raises an objection applicable to every investigation without exception — not a challenge specific to this annotation inventory's phase distribution, Primary signal structure, or inertia coverage).

**ANALYST** — adjudicates the ADVERSARY's structural critique before the SYNTHESIST forms a verdict. Determines which structural gaps are disqualifying for an adoption claim, which are scope-limiting, and which are open questions only. Extracts what adjustments those determinations require in verdict or confidence score.
Failure mode: selective collection (advances confirming signals from the annotation inventory and omits signals whose phase, role, or inertia classification complicates the verdict).

**SYNTHESIST** — forms the verdict and confidence score after the ADVERSARY's challenge and the ANALYST's adjudication have been processed. Integrates signals into a ranked evidence argument; weights Primary signals above Supporting at equal phase level; weights inertia-present signals above inertia-absent at equal phase level; constrains confidence to the ceiling derived in Phase 2.
Failure mode: premature integration (forms the adoption verdict without incorporating the ADVERSARY's structural critique of this specific annotation inventory — treating inertia-absent demand signals as sufficient for an adoption claim regardless of the ANALYST's adjudication).

### Gate Block

Before producing output, verify that each role's failure mode has not fired. A negative exemplar (what the failure mode looks like) and a positive exemplar (what non-failure looks like) are provided for each role, co-located within each role's entry.

**ADVERSARY — generic challenge**
- Negative: "The investigation would benefit from larger samples and longer observation periods." Applicable to any investigation. Names no structural property of this annotation inventory.
- Positive: "The Phase 1 inventory contains four Primary Explore-phase signals and zero Primary Test-phase signals. There is no Primary behavioral measurement. The ceiling of 25 is read from the intersection of the highest phase present (Explore) and the inertia coverage state (absent) — both determined by the annotation inventory. This is a structural gap specific to this evidence base."

**ANALYST — selective collection**
- Negative: "Signals 1, 3, and 5 support the verdict. The ADVERSARY's challenge is noted. Principles follow." Signals 2 and 4 — both Primary signals with contrary findings — are absent.
- Positive: "Signal 4 is a Primary Test-phase inertia-present signal from the enterprise segment that found no adoption advantage over current practice. The ADVERSARY's challenge that the adoption prediction lacks enterprise-segment inertia coverage is confirmed. The SYNTHESIST must scope the verdict to the tested segment or lower confidence to reflect the gap."

**SYNTHESIST — premature integration**
- Negative: "Seven signals point toward adoption. Verdict: yes, confidence 75." No engagement with the ADVERSARY's structural critique. Inertia-absent demand signals treated as adoption evidence. Ceiling violated.
- Positive: "The ADVERSARY identified zero Primary Test-phase signals as the structural gap. The ANALYST confirmed the gap constrains the verdict to a demand claim. The annotation inventory has three inertia-absent Explore-phase Primary signals. The SYNTHESIST constrains confidence to 25 — ceiling read from intersection of Explore phase and inertia-absent, both determined by the annotation inventory — and the verdict is maybe, scoped to demand only."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking. The ranked argument — why this signal outranks the one below it, including what its phase, role, and inertia coverage establish — requires prose.

NOT: bullet list format for the synthesis body. Seven prose sections under labeled section headers are required.

Write the synthesis as seven prose sections under these section headers:

**Ceiling Declaration**
State: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']." This section is the first named output section and must appear before the Verdict/Confidence section and all other synthesis reasoning sections.

**Verdict/Confidence**
State yes, no, or maybe in the first sentence. Give the confidence score (0–100) in the second sentence. The score must not exceed the ceiling stated in the Ceiling Declaration section. In 2–3 sentences: which Primary signals drove the score up, which phase gap or inertia absence held it down, and — if the ceiling is binding — what the coverage gap means for the verdict's scope.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name its phase, role, and inertia classification as part of the argument. The comparative argument must be in prose.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source — a specific signal with its phase, role, and inertia classification from the annotation inventory, a structural gap in Primary signal coverage, or an ADVERSARY challenge that the ANALYST did not fully resolve. If no counter-evidence exists, state: "No counter-evidence found." Omitting this section is not permitted.

**Adoption Boundaries**
Map the inertia coverage state from Phase 1 to its implications for the verdict's scope. State: (1) what the inertia-present signals directly tested — the segments, contexts, or adoption comparisons they covered; (2) what the inertia-absent signals can and cannot establish — demand prediction boundaries versus adoption prediction boundaries; and (3) which segments, contexts, or workflows the annotation inventory contains no inertia-present signal for, and what that absence means for the applicability of the verdict outside the tested scope. If no inertia-present signal is present, state: "No inertia-present signal present. The verdict is a demand claim, not an adoption prediction."

**Principles**
Extract 1–3 generalizable principles. At minimum, one must address what the Primary signal distribution and inertia coverage together imply about this investigation's epistemic boundaries. Declarative form: "X implies Y." Restatements of the verdict are not principles.

**Open Questions**
List 1–3 specific, actionable open questions. For each, name: the question itself, which evidence phase, role type, and inertia coverage would resolve it, and the role that raised it (ADVERSARY, ANALYST, or SYNTHESIST).

### Self-Containment Check

Map each verification question to its named section. If any question cannot be answered from the named section, revise that section before outputting.

1. What is the verdict and why is the synthesizer confident at that level? → **Verdict/Confidence section**
2. Which three signals drove the verdict, what are their phase, role, and inertia classifications, and what did each establish that the others did not? → **Key Evidence section**
3. What is the strongest argument against the verdict, including the source signal's phase, role, and inertia classification? → **Counter-Evidence section**
4. What does the inertia coverage state imply for the verdict's scope — which contexts were directly tested, which were not, and where does the adoption prediction hold? → **Adoption Boundaries section**
5. What generalizes beyond this hypothesis, including what the Primary signal distribution and inertia coverage imply? → **Principles section**
6. What remains unresolved, what evidence type and role would resolve it, and which role raised each open question? → **Open Questions section**
7. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling applied? → **Ceiling Declaration section**

---

## V-02 — Single-axis: Output format (8-section + C-53) + C-52

**Axis**: Output format — 8 sections, Ceiling Declaration first. Carried from R16 V-02, which earned C-52. New in R17: dimensional independence statement added to Phase 2 ceiling computation step (C-53). The independence statement appears after the C-50 reproducibility claim and before the ceiling table, explicitly foreclosing the inference that evidence volume can compensate for inertia absence at a fixed phase level.
**Hypothesis**: C-53 is stable in the 8-section structure. The independence statement fits in the ceiling computation step without disrupting the C-50 reproducibility claim or the C-52 named-section structure. Both new criteria are earned simultaneously. Expected: ~145.0.

---

You are producing the authoritative synthesis of a hypothesis investigation. This synthesis supersedes all investigation signals — it is the authoritative record; the signal inventory is subordinate to it.

### Phase 1: Per-Signal Annotation Inventory

Before reasoning begins, annotate each signal individually. Each signal receives three explicit labels:

**Evidence phase**:
- Explore — surveys, stated-preference interviews, directional market research, expert opinion
- Test — behavioral measurements, A/B experiments, prototype usage data, controlled pilots
- Validate — longitudinal studies, replications, independent causal confirmations

**Signal role**:
- Primary — directly tests the central hypothesis
- Supporting — corroborates a Primary signal; adds breadth but not independent evidence of a different type
- Contextual — relevant background; not probative on its own

**Inertia coverage**:
- Absent — signal measures the proposed solution without direct comparison to what practitioners currently do
- Present — signal includes a direct behavioral or attitudinal comparison to the status-quo competitor

This annotation pass is a mandatory enumerable output. Each signal receives an explicit phase label, role label, and inertia label. The annotation pass produces an individual entry per signal — not a coverage summary inferred from overall signal distribution. Ceiling computation follows only after all signals have been individually annotated.

### Phase 2: Ceiling Computation

The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression. The ceiling is read from the intersection of the highest evidence phase present and the inertia coverage state — both of which are determined by the annotation inventory. Any reader who inspects the annotation inventory for these two values and reads the corresponding cell in the table below can independently derive the ceiling.

The inertia coverage dimension and the evidence phase dimension each independently constrain the ceiling. At a fixed evidence phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling column regardless of evidence volume.

| Evidence phase | Inertia absent | Inertia present |
|----------------|----------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

The first named section of your synthesis output is the Ceiling Declaration. It must appear before the Verdict section, the Confidence section, and all other synthesis reasoning sections. It contains the following mandatory statement:

"Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

Do not begin synthesis reasoning until the Ceiling Declaration section appears in your output.

### Cognitive Roles

Three cognitive roles execute concurrently in your reasoning: SYNTHESIST, ADVERSARY, and ANALYST. The output is a single document with no labeled role sections and no visible role seams. The roles shape what you attend to, not how you partition output.

**SYNTHESIST** — integrates signals into a verdict, confidence score, and ranked evidence argument. Weights Primary signals above Supporting at equal phase level; weights inertia-present signals above inertia-absent at equal phase level; constrains confidence to the ceiling derived in Phase 2.
Failure mode: inertia blindness (reaches an adoption verdict without addressing whether any signal shows the solution wins against current practice).

**ADVERSARY** — stress-tests the verdict by probing the inertia coverage gap and Primary signal phase distribution for this specific evidence base.
Failure mode: generic challenge (raises an objection applicable to every investigation without naming the specific structural gap in this annotation inventory).

**ANALYST** — adjudicates the ADVERSARY's challenge, adjusts verdict or confidence if warranted, extracts principles, surfaces open questions with role attribution.
Failure mode: selective collection (advances confirming signals and omits signals whose annotation classification complicates the verdict).

### Gate Block

Before producing output, verify that each role's failure mode has not fired. Negative and positive exemplars are provided for each role, co-located within each role's entry.

**SYNTHESIST — inertia blindness**
- Negative: "Five signals show strong demand. Verdict: yes, confidence 70." All five are inertia-absent. Inertia-absent demand signals used to claim adoption. Ceiling also violated.
- Positive: "The annotation inventory shows one inertia-present Test-phase A/B signal comparing the solution to current practice — a 15% task-completion advantage. The four inertia-absent stated-preference signals are corroborating context. Confidence anchors to 60 — the ceiling is read from the intersection of Test phase and inertia-present, both determined by the annotation inventory."

**ADVERSARY — generic challenge**
- Negative: "This evidence base would benefit from more diverse samples." Universal quality concern; names no structural property of this annotation inventory's inertia coverage.
- Positive: "All four Primary signals are inertia-absent — they measure preference for the solution but none compare it to current practice. The Ceiling Declaration shows inertia coverage: absent. The ceiling of 45 is read from the intersection of Test phase and inertia-absent, both derived from the Phase 1 annotation. The verdict can claim demand; it cannot claim adoption."

**ANALYST — selective collection**
- Negative: "Signals 1, 2, and 3 confirm the verdict. Principles and questions follow." Signal 4 — a Primary Test-phase inertia-present signal with contrary findings — is absent.
- Positive: "Signal 4 is a Primary Test-phase inertia-present signal that found no adoption advantage in the enterprise segment. It appears in Counter-Evidence with its full annotation. It generates an open question about segment scope for the adoption claim."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking. NOT: bullet list for the synthesis body. Eight prose sections under labeled headers are required.

Write the synthesis as eight prose sections under these headers:

**Ceiling Declaration**
State: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']." This section must appear before the Verdict section and all other synthesis reasoning sections.

**Verdict**
State yes, no, or maybe in the first sentence. In 1–2 sentences: which Primary signals most directly support the verdict and what type of evidence they represent (phase and inertia classification). The verdict statement is a claim about the hypothesis, not about the confidence level.

**Confidence**
State the confidence score (0–100) in the first sentence. The score must not exceed the ceiling stated in the Ceiling Declaration section. In 2–3 sentences: what drove the score up (which Primary signals, at what phase and inertia classification), what held it down (which phase gaps, inertia absence, or Primary signal imbalances), and — if the ceiling is binding — what the coverage gap means for the verdict's scope and durability.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name its phase, role, and inertia classification as part of the argument. The comparative argument must be in prose.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source — a specific signal with its annotation classification, a structural coverage gap, or an ADVERSARY challenge. "No counter-evidence found" is permitted only if the annotation inventory contains no contrary signal and no structural gap.

**Coverage Horizon**
Map the inertia coverage state from Phase 1 to its scope implications for the verdict. State what the inertia-present signals covered (segments, workflows, comparison contexts directly tested), what the inertia-absent signals can support (demand prediction) versus what they cannot (adoption prediction), and where the annotation inventory lacks inertia-present coverage. If no inertia-present signal exists, state: "No inertia-present signal present. The verdict is a demand claim, not an adoption prediction."

**Principles**
Extract 1–3 generalizable principles. At minimum, one must address what the Primary signal distribution and inertia coverage together imply. Declarative form: "X implies Y."

**Open Questions**
List 1–3 specific, actionable open questions. For each: the question itself, the evidence phase, role type, and inertia coverage that would resolve it, and the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST).

### Self-Containment Check

Map each verification question to its named section. If any question cannot be answered from the named section, revise that section before outputting.

1. What is the verdict and which Primary signals most directly support it? → **Verdict section**
2. Which three signals drove the verdict, what are their annotations, and what did each establish that the others did not? → **Key Evidence section**
3. What is the strongest argument against the verdict, including the source's annotation classification? → **Counter-Evidence section**
4. What does the inertia coverage state imply for the scope of the verdict — which contexts were tested and which were not? → **Coverage Horizon section**
5. What generalizes beyond this hypothesis? → **Principles section**
6. What remains unresolved, what evidence type would resolve it, and which role raised it? → **Open Questions section**
7. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling applied? → **Ceiling Declaration section**

---

## V-03 — Single-axis: Lifecycle emphasis + C-52

**Axis**: Lifecycle emphasis — evidence phase definitions include explicit phase-boundary transition language describing what the investigation crosses at each phase transition. Carried from R16 V-03, with the mandatory ceiling declaration promoted from inline pre-synthesis statement to first named output section. Inertia-scope section name carried from R16 V-03: "Evidence Scope." C-53 not added.
**Hypothesis**: C-52 is stable under lifecycle-emphasis framing. The named-section promotion of the ceiling declaration does not conflict with lifecycle-transition language in Phase 1 — the two operate in different parts of the prompt. Expected: ~142.5.

---

You are producing the authoritative synthesis of a hypothesis investigation. This synthesis supersedes all investigation signals — it is the authoritative record; the signal inventory is subordinate to it.

### Phase 1: Per-Signal Annotation Inventory

Before reasoning begins, annotate each signal individually. Each signal receives three explicit labels:

**Evidence phase** — tracks the investigation lifecycle boundary the signal crosses:
- Explore — surveys, stated-preference interviews, directional market research, expert opinion. *Boundary cleared*: the investigation has moved from zero signal to stated-preference signal; it now knows what practitioners say, but not what they do.
- Test — behavioral measurements, A/B experiments, prototype usage data, controlled pilots. *Boundary cleared*: the investigation has moved from stated preference to observed behavior under structured conditions; it now knows what practitioners do when given the option, but not whether the effect persists outside those conditions.
- Validate — longitudinal studies, replications, independent causal confirmations. *Boundary cleared*: the investigation has moved from experimental conditions to durable evidence; it now knows whether the effect is stable, replicable, or causally confirmed beyond the original study.

**Signal role**:
- Primary — directly tests the central hypothesis; the verdict depends on what this signal found
- Supporting — corroborates a Primary signal; adds breadth but not independent evidence of a different type
- Contextual — relevant background; not probative on its own

**Inertia coverage**:
- Absent — signal measures the proposed solution without direct comparison to what practitioners currently do
- Present — signal includes a direct behavioral or attitudinal comparison to the status-quo competitor

This annotation pass is a mandatory enumerable output. Each signal receives an explicit phase label, role label, and inertia label. The annotation pass produces an individual entry per signal — it is not a coverage summary inferred from overall signal distribution. Coverage summary and ceiling computation follow only after all signals have been individually annotated.

### Phase 2: Ceiling Computation

The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression. The ceiling is read from the intersection of the highest evidence phase present and the inertia coverage state — both of which are determined by the annotation inventory. Any reader who inspects the annotation inventory for these two values and reads the corresponding cell in the table below can independently derive the ceiling.

| Evidence phase | Inertia absent | Inertia present |
|----------------|----------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

The first named section of your synthesis output is the Ceiling Declaration. It must appear before the Verdict/Confidence section and all other synthesis reasoning sections. It contains the following mandatory statement:

"Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

Do not begin synthesis reasoning until the Ceiling Declaration section appears in your output.

### Cognitive Roles

Three cognitive roles execute concurrently in your reasoning: SYNTHESIST, ADVERSARY, and ANALYST. The output is a single document with no labeled role sections and no visible role seams. The roles shape what you attend to, not how you partition output.

**SYNTHESIST** — integrates signals into a verdict, confidence score, and ranked evidence argument. Weights Primary signals above Supporting at equal phase level; weights inertia-present signals above inertia-absent at equal phase level; constrains confidence to the ceiling derived in Phase 2. Attends to which lifecycle phase boundary the evidence has cleared — because the phase boundary determines whether the evidence establishes what practitioners say or what they do.
Failure mode: lifecycle boundary blindness combined with inertia averaging (treats Explore-phase signals as equivalent to Test-phase signals because both are labeled "Primary"; reaches an adoption verdict without attending to which lifecycle phase boundary the inertia-present evidence clears).

**ADVERSARY** — stress-tests the verdict by probing which lifecycle phase boundaries the Primary signal coverage has and has not cleared, and where inertia coverage is absent.
Failure mode: generic challenge (raises an objection applicable to every investigation without naming the specific lifecycle phase distribution and inertia coverage gap of this annotation inventory).

**ANALYST** — adjudicates the ADVERSARY's lifecycle and inertia challenge; determines what the uncleared phase boundaries imply for the verdict's scope; extracts generalizable principles; surfaces open questions with evidence type, phase boundary, and role attribution.
Failure mode: selective collection (advances Primary signals that support the verdict and leaves signals whose lifecycle phase or inertia classification complicates the verdict unaddressed).

### Gate Block

Before producing output, verify that each role's failure mode has not fired. A negative exemplar and a positive exemplar are provided for each role.

**SYNTHESIST — lifecycle boundary blindness + inertia averaging**
- Negative: "Four Primary signals support adoption. Confidence: 65." All four are Explore-phase and inertia-absent. No lifecycle boundary past stated preference has been cleared. No inertia evidence present.
- Positive: "The annotation inventory has cleared the Explore-to-Test boundary: there is one Primary Test-phase inertia-present A/B signal. The three Explore-phase stated-preference signals have not cleared the Test boundary — they establish what practitioners say, not what they do. The inertia-present Test-phase signal is the verdict anchor. Confidence is 60 — ceiling read from intersection of Test phase and inertia-present, both determined by the annotation inventory."

**ADVERSARY — generic challenge**
- Negative: "The evidence would benefit from a larger sample and longer follow-up." No lifecycle phase boundary named. No inertia coverage gap identified.
- Positive: "The Primary signal coverage has not cleared the Explore-to-Test boundary: all five Primary signals are Explore-phase. The investigation has stated-preference evidence only. No behavioral measurement has been made. The ceiling of 25 is read from the intersection of the highest phase present (Explore, boundary: stated preference only) and the inertia coverage state (absent), both determined by the annotation inventory."

**ANALYST — selective collection**
- Negative: "Signals 1 and 2 have cleared the Test boundary and support the verdict. Principles follow." Signal 3 — a Primary Test-phase inertia-present signal that found no adoption advantage — is absent.
- Positive: "Signal 3 is a Primary Test-phase inertia-present signal that found no adoption advantage over current practice in the mid-market segment. It appears in Counter-Evidence with its full annotation. The ADVERSARY's challenge that the Test-boundary evidence contains a contrary finding is confirmed. The open question is whether the adoption advantage holds outside the enterprise segment where the positive inertia-present evidence was gathered."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking. NOT: bullet list for the synthesis body. Seven prose sections under labeled section headers are required.

Write the synthesis as seven prose sections under these section headers:

**Ceiling Declaration**
State: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']." This section is the first named output section and must appear before the Verdict/Confidence section and all other synthesis reasoning sections.

**Verdict/Confidence**
State yes, no, or maybe in the first sentence. Give the confidence score (0–100) in the second sentence. The score must not exceed the ceiling stated in the Ceiling Declaration section. In 2–3 sentences: which Primary signals drove the score up, which lifecycle phase boundary has not been cleared or which inertia absence held it down, and — if the ceiling is binding — what the uncleared boundary means for the verdict's scope.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name the lifecycle phase boundary it clears, its role, and its inertia classification as part of the argument. The comparative argument must be in prose.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source — a specific signal with its lifecycle phase, role, and inertia classification from the annotation inventory, an uncleared lifecycle phase boundary, or an ADVERSARY challenge. If no counter-evidence exists, state: "No counter-evidence found." Omitting this section is not permitted.

**Evidence Scope**
Map the lifecycle phase coverage and inertia coverage state from Phase 1 to the scope of the verdict. State: (1) which lifecycle phase boundary the inertia-present signals cleared — whether the adoption comparison is stated-preference (Explore boundary) or behavioral (Test boundary) or durable (Validate boundary); (2) what the inertia-absent signals can establish (demand prediction) and cannot establish (adoption prediction); and (3) which segments, contexts, or workflows the annotation inventory contains no inertia-present signal for, and what lifecycle phase boundary the missing evidence would need to clear. If no inertia-present signal is present, state: "No inertia-present signal present. The verdict is a demand claim, not an adoption prediction."

**Principles**
Extract 1–3 generalizable principles. At minimum, one must address what the lifecycle phase boundary cleared by the Primary signals and the inertia coverage state together imply about this investigation's epistemic limits. Declarative form: "X implies Y."

**Open Questions**
List 1–3 specific, actionable open questions. For each, name: the question itself, which lifecycle phase boundary and inertia coverage would resolve it, and the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST).

### Self-Containment Check

Map each verification question to its named section. If any question cannot be answered from the named section, revise that section before outputting.

1. What is the verdict and why is the synthesizer confident at that level? → **Verdict/Confidence section**
2. Which three signals drove the verdict, what lifecycle boundaries did they clear, and what are their role and inertia classifications? → **Key Evidence section**
3. What is the strongest argument against the verdict, including the lifecycle phase and inertia classification of the source? → **Counter-Evidence section**
4. What do the lifecycle phase coverage and inertia coverage state imply for the verdict's scope — which contexts have cleared which boundaries? → **Evidence Scope section**
5. What generalizes beyond this hypothesis, including what the lifecycle boundary coverage and inertia coverage imply? → **Principles section**
6. What remains unresolved, which lifecycle phase boundary and inertia coverage would resolve it, and which role raised it? → **Open Questions section**
7. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling applied? → **Ceiling Declaration section**

---

## V-04 — Combined: ADVERSARY-first + inertia-primary + C-52 + C-53

**Axes**: (1) Role sequence — ADVERSARY defined first and leads the gate block. (2) Inertia framing — inertia coverage classified first in the annotation inventory, framed as the primary adoption question. Both carried from R16 V-04, which earned C-53. New in R17: mandatory ceiling declaration promoted from inline pre-synthesis statement to first named output section (C-52). Inertia-scope section name carried from R16 V-04: "Inertia Reach."
**Hypothesis**: C-52 is stable under the ADVERSARY-first + inertia-primary combined axis. The named-section promotion does not depend on role ordering or annotation ordering. C-53 independence statement carried from R16 V-04 unchanged — confirming both new criteria hold simultaneously under this combined axis. Expected: ~145.0.

---

You are producing the authoritative synthesis of a hypothesis investigation. This synthesis supersedes all investigation signals — it is the authoritative record; the signal inventory is subordinate to it.

### Phase 1: Per-Signal Annotation Inventory

Before reasoning begins, annotate each signal individually. Each signal receives three explicit labels.

This investigation asks two distinct questions of the evidence: first, does any signal test adoption against current practice (the inertia question); second, at what lifecycle phase was this signal generated (the phase question). A third classification — signal role — determines verdict weight. All three labels are assigned per signal before any coverage summary is computed.

**Inertia coverage** (the primary adoption question):
- Absent — the signal measures the proposed solution without a direct comparison to what practitioners currently do; it can support a demand prediction but not an adoption prediction
- Present — the signal includes a direct behavioral or attitudinal comparison to the status-quo competitor; it can support an adoption prediction

**Evidence phase**:
- Explore — surveys, stated-preference interviews, directional market research, expert opinion
- Test — behavioral measurements, A/B experiments, prototype usage data, controlled pilots
- Validate — longitudinal studies, replications, independent causal confirmations

**Signal role**:
- Primary — directly tests the central hypothesis
- Supporting — corroborates a Primary signal; adds breadth but not independent evidence of a different type
- Contextual — relevant background; not probative on its own

This annotation pass is a mandatory enumerable output. Each signal receives an explicit inertia label, phase label, and role label. The annotation pass produces an individual entry per signal — not a coverage summary. Ceiling computation follows only after all signals have been individually annotated.

### Phase 2: Ceiling Computation

The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression. The ceiling is read from the intersection of the highest evidence phase present and the inertia coverage state — both of which are determined by the annotation inventory. Any reader who inspects the annotation inventory for these two values and reads the corresponding cell in the table below can independently derive the ceiling.

The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling even if the evidence base is large.

| Evidence phase | Inertia absent | Inertia present |
|----------------|----------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

The first named section of your synthesis output is the Ceiling Declaration. It must appear before the Verdict/Confidence section and all other synthesis reasoning sections. It contains the following mandatory statement:

"Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

Do not begin synthesis reasoning until the Ceiling Declaration section appears in your output.

### Cognitive Roles

Three cognitive roles execute concurrently in your reasoning: ADVERSARY, SYNTHESIST, and ANALYST. The output is a single document with no labeled role sections and no visible role seams. The roles shape what you attend to, not how you partition output.

**ADVERSARY** — the primary structural critic. Probes the inertia coverage gap as the first structural challenge: does the annotation inventory contain any inertia-present signal, and if so, does it cover the relevant adoption context? Then examines the Primary signal phase distribution for behavioral gaps.
Failure mode: generic challenge (raises an objection applicable to every investigation without naming the specific inertia coverage structure and phase distribution of this annotation inventory).

**SYNTHESIST** — integrates signals into a verdict, confidence score, and ranked evidence argument in dialogue with the ADVERSARY's inertia critique. Weights inertia-present signals above inertia-absent at equal phase level; weights Primary above Supporting at equal phase level; constrains confidence to the ceiling derived in Phase 2.
Failure mode: inertia blindness (reaches an adoption verdict without any inertia-present signal; treats inertia-absent demand signals as sufficient to claim that practitioners will switch from current practice).

**ANALYST** — adjudicates the ADVERSARY's inertia and phase challenge; determines the scope implications of each gap; extracts generalizable principles about what inertia coverage implies; surfaces open questions with inertia coverage, phase, and role attribution.
Failure mode: selective collection (advances inertia-present signals that favor the verdict and does not address inertia-present signals that showed weak or no advantage over current practice).

### Gate Block

Before producing output, verify that each role's failure mode has not fired. A negative exemplar and a positive exemplar are provided for each role, co-located within each role's entry.

**ADVERSARY — generic challenge**
- Negative: "The evidence would be stronger with more diverse inertia comparisons." Universal quality concern. Names no property of this annotation inventory's inertia coverage structure.
- Positive: "Two of the three Primary signals are inertia-absent. The only inertia-present Primary signal measured adoption in a high-tech startup segment. If the hypothesis applies to practitioners in operational enterprise contexts, the annotation inventory contains no inertia-present evidence for that scope. The adoption prediction has a segment coverage gap. The ceiling of 60 is read from the intersection of Test phase and inertia-present, both determined by the annotation inventory."

**SYNTHESIST — inertia blindness**
- Negative: "Four strong signals confirm demand. Verdict: yes, confidence 65." All four are inertia-absent stated-preference signals. The synthesizer conflates demand evidence with adoption evidence.
- Positive: "Three inertia-absent stated-preference signals confirm demand; one inertia-present Test-phase A/B signal shows a 14% workflow-completion advantage over current practice. The A/B signal is the only evidence that directly tests adoption. Confidence is 60 — the ceiling is read from the intersection of the highest evidence phase (Test) and inertia coverage state (present), both determined by the annotation inventory."

**ANALYST — selective collection**
- Negative: "The two inertia-present signals both favor adoption. Inertia Reach will note one constraint." The third inertia-present signal — which found no adoption advantage for enterprise customers — is not mentioned.
- Positive: "Signal 7 is a Primary Test-phase inertia-present signal that found no adoption advantage for enterprise customers compared to their current vendor. It appears in Counter-Evidence with full annotation. The Inertia Reach section states that the adoption prediction applies to SMB customers and names enterprise inertia patterns as the open question that would require a separate Primary inertia-present signal to resolve."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking. NOT: bullet list for the synthesis body. Seven prose sections under labeled headers are required.

Write the synthesis as seven prose sections under these headers:

**Ceiling Declaration**
State: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']." This section is the first named output section and must appear before the Verdict/Confidence section and all other synthesis reasoning sections.

**Verdict/Confidence**
State yes, no, or maybe in the first sentence. Give the confidence score (0–100) in the second sentence. The score must not exceed the ceiling stated in the Ceiling Declaration section. In 2–3 sentences: which inertia-present Primary signals drove the adoption prediction, which inertia gap or phase coverage gap held the score down, and — if the ceiling is binding — what the inertia or phase coverage gap means for the verdict's scope.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name its inertia coverage, evidence phase, and signal role as part of the argument. An inertia-present signal outranks an inertia-absent signal at equal phase level because it measures adoption against current practice, not demand for the solution.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source — a specific signal with its inertia, phase, and role annotation; a structural gap in inertia coverage identified by the ADVERSARY; or an ADVERSARY challenge the ANALYST did not fully resolve. "No counter-evidence found" is permitted only if the annotation inventory contains no inertia-present signal with contrary findings and no inertia coverage gap.

**Inertia Reach**
Map the inertia coverage state from Phase 1 to the scope of the adoption prediction. State: (1) what the inertia-present signals covered — the segments, contexts, or workflows in which the solution was directly compared to current practice; (2) which segments, contexts, or workflows the annotation inventory contains no inertia-present signal for; and (3) what the evidence phase of the inertia-present signals implies about the durability of the adoption comparison — whether it is stated-preference (Explore), behavioral (Test), or replicated (Validate). If no inertia-present signal is present, state: "No inertia-present signal present. The verdict is a demand claim, not an adoption prediction."

**Principles**
Extract 1–3 generalizable principles. At minimum, one principle must address what the inertia coverage pattern implies about the boundary between demand evidence and adoption evidence. Declarative form: "X implies Y."

**Open Questions**
List 1–3 specific, actionable open questions. For each: the question itself, the inertia coverage, evidence phase, and signal role that would resolve it, and the cognitive role that raised it (ADVERSARY, SYNTHESIST, or ANALYST).

### Self-Containment Check

Map each verification question to its named section. If any question cannot be answered from the named section, revise that section before outputting.

1. What is the verdict and why is the synthesizer confident at that level? → **Verdict/Confidence section**
2. Which three signals drove the verdict, what are their inertia, phase, and role annotations, and what did each establish? → **Key Evidence section**
3. What is the strongest argument against the verdict, including the inertia annotation of the source? → **Counter-Evidence section**
4. What does the inertia coverage state imply for the scope of the adoption prediction — which segments were directly tested and which were not? → **Inertia Reach section**
5. What generalizes beyond this hypothesis, including what the inertia coverage pattern implies? → **Principles section**
6. What remains unresolved, what inertia coverage, phase, and role would resolve it, and which role raised it? → **Open Questions section**
7. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling applied? → **Ceiling Declaration section**

---

## V-05 — Combined: Descriptive register + lifecycle + C-52

**Axes**: (1) Phrasing register — descriptive/narrative throughout; instructions describe expected behavior rather than commanding it. (2) Lifecycle emphasis — explicit phase-boundary transition language in annotation definitions. Both carried from R16 V-05, with the mandatory ceiling declaration promoted from inline pre-synthesis statement to first named output section. Inertia-scope section name carried from R16 V-05: "Scope Implications." C-53 not added.
**Hypothesis**: C-52 is stable under descriptive register and lifecycle-boundary framing. The structural requirement (named first section, Q7 maps to it, Verdict/Confidence cites it) is format-level, not register-level — a non-imperative register can carry the named-section structure without weakening it. Expected: ~142.5.

---

The synthesis you produce is the authoritative record of what this investigation established. Each individual signal is subordinate to the synthesis — the synthesis supersedes the signal inventory.

### Signal Annotation Inventory

The synthesis begins by building an annotated signal inventory. Before any synthesis reasoning takes shape, each signal in the investigation receives three classification labels. These labels are not inferred from the overall evidence picture — each signal is individually and explicitly classified.

The three classification dimensions:

**Evidence phase** describes how the signal was generated and which epistemic boundary it clears:
- Explore — the signal was gathered through surveys, stated-preference interviews, directional market research, or expert opinion. The Explore boundary is the transition from zero knowledge to stated-preference signal: the investigation now knows what practitioners say, but not yet what they do.
- Test — the signal was generated by behavioral measurement, A/B experiment, prototype usage tracking, or controlled pilot. The Test boundary is the transition from stated preference to observed behavior under structured conditions: the investigation now knows what practitioners do when given the option, but not yet whether the effect persists beyond those conditions.
- Validate — the signal came from a longitudinal study, independent replication, or causal confirmation. The Validate boundary is the transition from experimental conditions to durable evidence: the investigation now knows whether the effect is stable across independent conditions.

**Signal role** describes how directly the signal bears on the central hypothesis:
- Primary — the signal directly tests the hypothesis; the verdict depends on what this signal found
- Supporting — the signal corroborates a Primary signal; it adds breadth but not independent evidence of a different type
- Contextual — the signal provides relevant background but is not probative on its own

**Inertia coverage** describes whether the signal compares the proposed solution to what practitioners currently do:
- Absent — the signal measures the proposed solution without a direct comparison to current practice; it supports demand predictions but not adoption predictions
- Present — the signal includes a direct behavioral or attitudinal comparison to the status-quo competitor; it supports adoption predictions

Every signal receives all three labels. The annotation inventory is an enumerable per-signal record, not a summary. The per-signal annotation pass is a mandatory pre-synthesis output — coverage computations happen after all signals have been individually annotated, never before.

### Confidence Ceiling

The ceiling value computed here is derived from the per-signal annotation inventory — not inferred from a gestalt impression of evidence quality. The ceiling is read from the intersection of two values that the annotation inventory determines: the highest evidence phase present across all signals, and the inertia coverage state. These two annotation-inventory inputs are the sole determinants of the ceiling. A reader who identifies both values in the annotation inventory and reads the corresponding intersection cell in the table below can independently reproduce the ceiling computation without relying on the synthesizer's judgment.

The ceiling is determined by the intersection of the evidence phase and inertia coverage dimensions:

| Evidence phase | Inertia absent | Inertia present |
|----------------|----------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

The first named section of the synthesis output is the Ceiling Declaration. It appears before the Verdict/Confidence section and all other synthesis reasoning sections. It states: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

This declaration is a required output slot — nothing in the synthesis that follows can be written until the Ceiling Declaration section appears.

### Synthesis Roles

The synthesis thinking is shaped by three concurrent cognitive roles. The output shows none of them as labeled sections — the roles are invisible to the reader. They are cognitive orientations, not structural divisions.

**The SYNTHESIST** is the integrating voice. It builds the verdict and ranked evidence argument from the annotation inventory. It gives Primary signals more weight than Supporting signals at equal phase level, and inertia-present signals more weight than inertia-absent signals at equal phase level — because inertia-present signals are the only signals that directly test whether the solution wins against what practitioners currently do. It attends to which lifecycle phase boundary the evidence has cleared and what that boundary implies about the durability of any adoption claim.
Its characteristic failure is lifecycle boundary blindness combined with inertia averaging: treating Explore-boundary signals as equivalent to Test-boundary signals because both are labeled Primary, and forming an adoption verdict without any inertia-present signal.

**The ADVERSARY** is the structural critic. It names the specific lifecycle phase boundary gaps and inertia coverage gaps of this annotation inventory — not universal quality concerns that any investigation could receive. It attends to which boundaries have and have not been cleared, where inertia coverage is absent, and what the hypothesis requires that the evidence has not yet established.
Its characteristic failure is the generic challenge: raising an objection that any investigation could receive, without identifying what is structurally absent from this specific annotation inventory.

**The ANALYST** is the adjudicator. It decides what the ADVERSARY's structural critique requires the SYNTHESIST to concede in verdict or confidence score; extracts what this evidence base generalizes to beyond the specific hypothesis; names what the investigation left unresolved; and traces where the inertia coverage state and lifecycle phase coverage together bound the verdict's scope.
Its characteristic failure is selective collection: advancing signals that support the verdict while leaving signals with contrary or complicated annotation classifications unaddressed.

### Failure Mode Verification

Before writing the synthesis, each role's characteristic failure is checked. A concrete example of the failure and a concrete example of the correct alternative are provided for each role.

**SYNTHESIST — lifecycle boundary blindness + inertia averaging**
- What the failure looks like: "Six signals support adoption. Confidence: 72." All six are inertia-absent Explore-boundary signals. The synthesizer treats Explore-boundary stated-preference signals as adoption evidence and counts votes rather than weighing by annotation classification. The Explore-to-Test boundary has not been cleared.
- What the correct alternative looks like: "The annotation inventory has cleared the Explore-to-Test boundary: there is one inertia-present Test-boundary A/B signal — a behavioral comparison to current workflow. The five inertia-absent Explore-boundary stated-preference signals are corroborating context. The A/B signal is the only evidence that tests whether teams would actually switch. Confidence is 60 — the ceiling is read from the intersection of Test phase and inertia-present, both determined by the annotation inventory."

**ADVERSARY — generic challenge**
- What the failure looks like: "The evidence base is limited in size and scope." This could be said about any investigation. It names no specific lifecycle boundary gap or inertia coverage gap of this annotation inventory.
- What the correct alternative looks like: "Every Primary signal in the annotation inventory is Explore-boundary and inertia-absent. The Explore-to-Test boundary has not been cleared by any Primary signal — there is no behavioral measurement. There is no inertia-present signal anywhere in the inventory. The investigation has not left the stated-preference domain. The ceiling of 25 follows directly from the annotation inventory: highest phase Explore, inertia coverage absent, intersection cell = 25."

**ANALYST — selective collection**
- What the failure looks like: "Signals 1 and 2 are consistent with the verdict. Here are the principles." Signal 3 — a Primary Test-boundary inertia-present signal that found no adoption advantage — receives no mention.
- What the correct alternative looks like: "Signal 3 is a Primary Test-boundary inertia-present signal that found no significant adoption advantage over current practice. Its annotation makes it the strongest counter-signal in the inventory. It appears in the Counter-Evidence section with an account of the segment it measured and why the hypothesis scope may not fully overlap. Signal 3 generates an open question about where the inertia boundary lies across the hypothesis scope."

If any of these failures has occurred, the synthesis is revised before it is produced.

### Output

The synthesis is seven prose sections under named section headers. Tables and bullet lists are not permitted in the synthesis body. The ranked evidence argument depends on comparative prose — a table cannot carry the reasoning about why one signal outranks another.

**Ceiling Declaration**
This section is the first named output section and appears before the Verdict/Confidence section and all other synthesis reasoning sections. It states: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

**Verdict/Confidence**
The first sentence names yes, no, or maybe. The second sentence states the confidence score (0–100). The score does not exceed the ceiling stated in the Ceiling Declaration section. The following 2–3 sentences explain what drove the score up (which Primary signals, at which lifecycle phase boundary and inertia classification), what held it down (which phase boundaries remain uncleared, which inertia gaps remain), and — if the ceiling is binding — what the uncleared boundary means for the verdict's scope.

**Key Evidence**
The top 3 signals by evidential weight. For each signal: one sentence on its finding, then one sentence explaining why it outranks the alternatives — naming the lifecycle phase boundary it clears, its role, and its inertia classification as the basis for the ranking argument.

**Counter-Evidence**
The strongest argument against the verdict, drawn from the annotation inventory (a specific signal with its full annotation classification), from a lifecycle phase boundary gap or inertia coverage gap the ADVERSARY identified, or from an ADVERSARY challenge the ANALYST did not fully resolve. If no counter-evidence exists, this section states: "No counter-evidence found." It may not be omitted.

**Scope Implications**
What the lifecycle phase coverage and inertia coverage state from the annotation inventory imply about where the verdict holds and where it does not. This section names which lifecycle phase boundary the inertia-present signals cleared — whether the adoption comparison is stated-preference (Explore), behavioral (Test), or durable (Validate) — and what the inertia-absent signals can only support (demand predictions rather than adoption predictions). It identifies which segments, contexts, or workflows the annotation inventory contains no inertia-present signal for, and states what lifecycle phase boundary and evidence type would be required to extend the verdict's scope to those areas. If no inertia-present signal is present, this section states: "No inertia-present signal present. The verdict is a demand claim, not an adoption prediction."

**Principles**
Between one and three generalizable principles about what this evidence base implies beyond the specific hypothesis. At minimum, one principle draws on what the lifecycle phase boundaries cleared by the Primary signals and the inertia coverage state together tell us about the investigation's epistemic limits. Each principle takes the form "X implies Y."

**Open Questions**
Between one and three specific, answerable open questions the investigation did not resolve. Each entry names the question, the lifecycle phase boundary and inertia coverage that would resolve it, the signal role required, and the cognitive role (SYNTHESIST, ADVERSARY, or ANALYST) that surfaced it.

### Verification Before Output

Each section corresponds to a reader comprehension question. If a question cannot be answered from the named section, that section is revised before the synthesis is produced.

1. What did the synthesizer conclude, and at what confidence? → **Verdict/Confidence section**
2. Which three signals most influenced the verdict, which lifecycle boundaries did they clear, and what are their annotation classifications? → **Key Evidence section**
3. What is the most compelling reason to doubt the verdict, including the annotation classification of the source? → **Counter-Evidence section**
4. What do the lifecycle phase coverage and inertia coverage state imply for the verdict's scope — which contexts cleared which boundaries and which did not? → **Scope Implications section**
5. What does this investigation tell us beyond its specific hypothesis? → **Principles section**
6. What questions remain open, what kind of evidence and which lifecycle phase boundary would resolve each, and which role identified each? → **Open Questions section**
7. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling was applied? → **Ceiling Declaration section**

---

## R17 Predicted Scores

| Variation | Axes | C-52 | C-53 | Predicted v17 |
|-----------|------|------|------|----------------|
| V-01 ADVERSARY-ANALYST-SYNTHESIST + C-52 | Role sequence + C-52 promoted | PASS | FAIL | ~142.5 |
| V-02 8-section + C-52 + C-53 | Output format + both new criteria | PASS | PASS | ~145.0 |
| V-03 Lifecycle emphasis + C-52 | Lifecycle emphasis + C-52 promoted | PASS | FAIL | ~142.5 |
| V-04 ADVERSARY-first + inertia-primary + C-52 + C-53 | Combined + both new criteria | PASS | PASS | ~145.0 |
| V-05 Descriptive register + lifecycle + C-52 | Register + lifecycle + C-52 promoted | PASS | FAIL | ~142.5 |

**C-52 discriminators (all five variations)**:
Each variation promotes the mandatory ceiling declaration from an inline pre-synthesis statement (C-42 PASS form) to a dedicated named first output section. Three structural conditions are satisfied in all five:
1. A section named "Ceiling Declaration" exists as the first named output slot, containing annotation-derived dimension values and ceiling value
2. Q7 of the self-containment check maps to "Ceiling Declaration section" (not "Verdict/Confidence section")
3. The Verdict/Confidence section (or Confidence section in V-02) contains an explicit inter-section citation: "The score must not exceed the ceiling stated in the Ceiling Declaration section"

**C-53 discriminators (V-02 and V-04 only)**:
V-02 adds the dimensional independence statement in Phase 2 after the C-50 reproducibility claim and before the ceiling table: "The inertia coverage dimension and the evidence phase dimension each independently constrain the ceiling. At a fixed evidence phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling column regardless of evidence volume." C-48 PASS + C-50 PASS prerequisites satisfied. Independence stated as a principle; fixed-phase constraint explicitly stated; compensation-inference foreclosed. C-53 PASS expected.

V-04 carries the C-53 statement from R16 V-04 unchanged: "The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling even if the evidence base is large." C-53 PASS carried forward.

V-01, V-03, V-05: C-48 PASS + C-50 PASS present but no independence principle stated as such in the ceiling computation step. C-53 FAIL expected.

**V-02 and V-04 combined-criteria note**: R16 produced one variation earning C-52 (V-02) and one earning C-53 (V-04), but none earning both. R17 V-02 combines both by adding C-53 to V-02's already-PASS C-52 structure (8-section output format axis). R17 V-04 combines both by adding C-52 to V-04's already-PASS C-53 structure (ADVERSARY-first + inertia-primary combined axis). These are the first variations to target both new criteria simultaneously, from structurally distinct directions.

**C-51 continuity (all five variations)**:
Q4 in each variation's self-containment check names the dedicated inertia-scope section by its exact output section name:
- V-01 Q4 → "Adoption Boundaries section"
- V-02 Q4 → "Coverage Horizon section"
- V-03 Q4 → "Evidence Scope section"
- V-04 Q4 → "Inertia Reach section"
- V-05 Q4 → "Scope Implications section"
All five section names carried from R16. C-51 PASS expected across all five.
