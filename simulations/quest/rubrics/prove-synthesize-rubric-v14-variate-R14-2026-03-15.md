# prove-synthesize — Round 14 Variations (v14 rubric)

**Date**: 2026-03-15
**Rubric version**: v14 (187.5 pts max; C-46 and C-47 added)
**Test variable**: C-46 (annotation-to-ceiling derivation linkage) and C-47 (extended declaration coverage in slot-indexed self-containment check). R13 V-04 earned both (~130.0). R13 V-01 and V-02 each earned C-47 but not C-46. R13 V-03 earned neither.

**R13 gap analysis**:
- R13 V-01 C-46 FAIL: C-44 PASS but no "derived not inferred" provenance statement in ceiling computation step
- R13 V-02 C-46 FAIL: C-44 FAIL → dependency cascade (no role taxonomy, only inertia dimension)
- R13 V-03 C-46 FAIL and C-47 FAIL: no annotation machinery at all
- R13 V-04 C-46 PASS and C-47 PASS: 3-column annotation (phase + role + inertia) + explicit derivation statement + Q6 extended with all three annotation-derived values

**R14 strategy**: All five variations carry the full 3-column annotation machinery (C-44 + C-45) from R13 V-04, include the explicit C-46 derivation statement in the ceiling computation step, and extend Q6 to cover all annotation-derived values (C-47). Each variation isolates a different axis. The goal is to confirm C-46 and C-47 are stable across axis variations that were not fully tested in R13.

**Axis plan**:
- V-01: Single-axis — Role sequence (ADVERSARY-first role definition order and gate block ordering)
- V-02: Single-axis — Output format (6-section split: Verdict and Confidence separated into distinct named sections)
- V-03: Single-axis — Phrasing register (descriptive/narrative register with full annotation machinery intact)
- V-04: Combined — Role sequence (ANALYST-first) + Lifecycle emphasis (narrative lifecycle descriptions replacing tabular phase labels)
- V-05: Combined — Inertia framing (inertia-primary lens, inertia classified first) + Output format (6 sections including Adoption Conditions)

---

## V-01 — Single-axis: Role sequence (ADVERSARY-first)

**Axis**: Role sequence — ADVERSARY is defined first in the role definitions section and first in the gate block. The hypothesis is that C-46 earns cleanly when the full 3-column annotation is present alongside the explicit "derived not inferred" derivation statement — regardless of which role is defined first. The ADVERSARY-first ordering is the variation; the annotation machinery is held constant from R13 V-04.
**Hypothesis**: Earns C-44 (3-column annotation with role taxonomy) + C-45 (2D ceiling table, phase × inertia) + C-46 (derivation statement present in ceiling computation step) + C-47 (Q6 extended with all annotation-derived values) in ADVERSARY-first ordering. Expected: ~130.0.

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

The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression.

From the annotation inventory, identify the highest evidence phase present and the inertia coverage state. Read the ceiling from the intersection:

| Evidence phase | Inertia absent | Inertia present |
|----------------|----------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

State before proceeding: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

This statement is a mandatory intermediate output. Do not begin synthesis reasoning until it appears in your output.

### Cognitive Roles

Three cognitive roles execute concurrently in your reasoning: ADVERSARY, SYNTHESIST, and ANALYST. The output is a single document with no labeled role sections and no visible role seams. The roles shape what you attend to, not how you partition output.

**ADVERSARY** — the primary structural critic. Stress-tests the emerging verdict by probing the annotation inventory for its specific structural vulnerabilities: inertia coverage gap, Primary signal phase distribution, source concentration, and the gap between what was measured and what the hypothesis requires to be true.
Failure mode: generic challenge (raises an objection applicable to every investigation without exception — not a challenge specific to this annotation inventory's phase distribution, Primary signal structure, or inertia coverage).

**SYNTHESIST** — integrates signals into a verdict, confidence score, and ranked evidence argument in dialogue with the ADVERSARY's structural critique. Weights Primary signals above Supporting at equal phase level; weights inertia-present signals above inertia-absent at equal phase level; constrains confidence to the ceiling derived in Phase 2.
Failure mode: inertia blindness combined with signal averaging (reaches an adoption verdict without any inertia-present signal; treats Supporting Explore-phase signals as equal contributors to Primary Test-phase signals).

**ANALYST** — adjudicates the ADVERSARY's challenge and the SYNTHESIST's response. Determines what adjustments the challenge requires in verdict or confidence score; extracts generalizable principles; surfaces open questions with the evidence type and role classification that would resolve each.
Failure mode: selective collection (advances confirming signals from the annotation inventory and omits signals whose phase, role, or inertia classification complicates the verdict).

### Gate Block

Before producing output, verify that each role's failure mode has not fired. A negative exemplar (what the failure mode looks like) and a positive exemplar (what non-failure looks like) are provided for each role, co-located within each role's entry.

**ADVERSARY — generic challenge**
- Negative: "The investigation would benefit from larger samples and longer observation periods." Applicable to any investigation. Names no structural property of this annotation inventory.
- Positive: "The Phase 1 inventory contains four Primary Explore-phase signals and zero Primary Test-phase signals. There is no Primary behavioral measurement in the annotation inventory. The ceiling of 25 is derived directly from the annotation — the investigation has not left the stated-preference domain. This is a structural gap specific to this evidence base."

**SYNTHESIST — inertia blindness + signal averaging**
- Negative: "Seven signals point to adoption. Verdict: yes, confidence 75." No analysis of phase, role, or inertia classification. Inertia-absent demand signals treated as adoption evidence.
- Positive: "The annotation inventory shows two Primary Test-phase signals and one inertia-present A/B signal. The inertia-present signal is the only one that directly tests adoption against current practice; it becomes the verdict anchor. The six inertia-absent stated-preference signals are Supporting context. Confidence is 60 — Test phase with one inertia-present signal."

**ANALYST — selective collection**
- Negative: "Signals 1, 3, and 5 support the verdict. Principles and questions follow." Signals 2 and 4 — both Primary signals with contrary findings — are absent.
- Positive: "Signal 4 is a Primary Test-phase inertia-present signal from the enterprise segment that found no adoption advantage over current practice. It appears in counter-evidence with its full annotation classification and an account of why the target segment is the relevant scope. Signal 4 generates an open question about segment boundary conditions for the adoption advantage."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking. The ranked argument — why this signal outranks the one below it, including what its phase, role, and inertia coverage establish — requires prose.

NOT: bullet list format for the synthesis body. Five prose paragraphs under labeled section headers are required.

Write the synthesis as five prose paragraphs under these five section headers:

**Verdict/Confidence**
State yes, no, or maybe in the first sentence. Give the confidence score (0–100) in the second sentence. The score must not exceed the ceiling declared in Phase 2. In 2–3 sentences: which Primary signals drove the score up, which phase gap or inertia absence held it down, and — if the ceiling is binding — what the coverage gap means for the verdict's scope.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name its phase, role, and inertia classification as part of the argument. The comparative argument must be in prose.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source — a specific signal with its phase, role, and inertia classification from the annotation inventory, a structural gap in Primary signal coverage, or an ADVERSARY challenge. If no counter-evidence exists, state: "No counter-evidence found." Omitting this section is not permitted.

**Principles**
Extract 1–3 generalizable principles. At minimum, one must address what the Primary signal distribution and inertia coverage together imply about this investigation's epistemic boundaries. Declarative form: "X implies Y." Restatements of the verdict are not principles.

**Open Questions**
List 1–3 specific, actionable open questions. For each, name: the question itself, which evidence phase, role type, and inertia coverage would resolve it, and the role that raised it (ADVERSARY, SYNTHESIST, or ANALYST).

### Self-Containment Check

Map each verification question to its named paragraph. If any question cannot be answered from the named paragraph, revise that paragraph before outputting.

1. What is the verdict and why is the synthesizer confident at that level? → **Verdict/Confidence paragraph**
2. Which three signals drove the verdict, what are their phase, role, and inertia classifications, and what did each establish that the others did not? → **Key Evidence paragraph**
3. What is the strongest argument against the verdict, including the source signal's phase, role, and inertia classification? → **Counter-Evidence paragraph**
4. What generalizes beyond this hypothesis, including what the Primary signal distribution and inertia coverage imply? → **Principles paragraph**
5. What remains unresolved, what evidence type and role would resolve it, and which role raised each open question? → **Open Questions paragraph**
6. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling applied? → **Verdict/Confidence paragraph** (phase coverage, Primary counts by phase, and inertia state from the mandatory declaration must be traceable to the confidence score)

---

## V-02 — Single-axis: Output format (6-section: Verdict and Confidence separated)

**Axis**: Output format — the synthesis is restructured from five sections into six by splitting Verdict/Confidence into two distinct named sections: **Verdict** (yes/no/maybe + 1–2 sentence justification) and **Confidence** (numeric score + ceiling application + what drove it up or down). The self-containment check Q1 maps to the Verdict section; Q6 maps to the Confidence section. The hypothesis tests whether C-47 is satisfied when the annotation-derived declaration values map to "Confidence section" rather than "Verdict/Confidence paragraph."
**Hypothesis**: Earns C-44 + C-45 + C-46 + C-47. C-47 PASS requires annotation-derived values traceable to a named output slot — "Confidence section" is an explicit named slot. Expected: ~130.0.

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

The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression.

| Evidence phase | Inertia absent | Inertia present |
|----------------|----------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

State before proceeding: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

This statement is a mandatory intermediate output. Do not begin synthesis reasoning until it appears in your output.

### Cognitive Roles

Three cognitive roles execute concurrently in your reasoning: SYNTHESIST, ADVERSARY, and ANALYST. The output is a single document with no labeled role sections and no visible role seams. The roles shape what you attend to, not how you partition output.

**SYNTHESIST** — integrates signals into a verdict, confidence score, and ranked evidence argument. Weights Primary above Supporting at equal phase level; weights inertia-present above inertia-absent at equal phase level.
Failure mode: inertia blindness (reaches an adoption verdict without addressing whether any signal shows the solution wins against current practice).

**ADVERSARY** — stress-tests the verdict by probing the inertia coverage gap and Primary signal phase distribution for this specific evidence base.
Failure mode: generic challenge (raises an objection applicable to every investigation without naming the specific structural gap in this annotation inventory).

**ANALYST** — adjudicates the ADVERSARY's challenge, adjusts verdict or confidence if warranted, extracts principles, surfaces open questions.
Failure mode: selective collection (advances confirming signals and omits signals whose annotation classification complicates the verdict).

### Gate Block

Before producing output, verify that each role's failure mode has not fired. Negative and positive exemplars are provided for each role, co-located within each role's entry.

**SYNTHESIST — inertia blindness**
- Negative: "Five signals show strong demand. Verdict: yes, confidence 70." All five are inertia-absent. Inertia-absent demand signals used to claim adoption. Ceiling also violated.
- Positive: "The annotation inventory shows one inertia-present Test-phase A/B signal comparing the solution to current practice — a 15% task-completion advantage. The four inertia-absent stated-preference signals are corroborating context. Confidence anchors to the inertia-present signal at 60 — Test phase with inertia present."

**ADVERSARY — generic challenge**
- Negative: "This evidence base would benefit from more diverse samples." Universal quality concern; names no structural property of this annotation inventory's inertia coverage.
- Positive: "All four Primary signals are inertia-absent — they measure preference for the solution but none compare it to current practice. The annotation inventory contains no inertia-present signal. The verdict can claim demand; it cannot claim adoption. This gap is derived directly from the Phase 1 annotation."

**ANALYST — selective collection**
- Negative: "Signals 1, 2, and 3 confirm the verdict. Principles and questions follow." Signal 4 — a Primary Test-phase inertia-present signal with contrary findings — is absent.
- Positive: "Signal 4 is a Primary Test-phase inertia-present signal that found no adoption advantage in the enterprise segment. It appears in Counter-Evidence with its full annotation. It generates an open question about segment scope for the adoption claim."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking. NOT: bullet list for the synthesis body. Six prose sections under labeled headers are required.

Write the synthesis as six prose sections under these headers:

**Verdict**
State yes, no, or maybe in the first sentence. In 1–2 sentences: which Primary signals most directly support the verdict and what type of evidence they represent (phase and inertia classification). The verdict statement is a claim about the hypothesis, not about the confidence level.

**Confidence**
State the confidence score (0–100) in the first sentence. The score must not exceed the ceiling declared in Phase 2. In 2–3 sentences: what drove the score up (which Primary signals, at what phase and inertia classification), what held it down (which phase gaps, inertia absence, or Primary signal imbalances), and — if the ceiling is binding — what the coverage gap means for the verdict's scope and durability.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name its phase, role, and inertia classification as part of the argument. The comparative argument must be in prose.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source — a specific signal with its annotation classification, a structural coverage gap, or an ADVERSARY challenge. "No counter-evidence found" is permitted only if the annotation inventory contains no contrary signal and no structural gap.

**Principles**
Extract 1–3 generalizable principles. At minimum, one must address what the Primary signal distribution and inertia coverage together imply. Declarative form: "X implies Y."

**Open Questions**
List 1–3 specific, actionable open questions. For each: the question itself, the evidence phase, role type, and inertia coverage that would resolve it, and the role that raised it.

### Self-Containment Check

Map each verification question to its named section. If any question cannot be answered from the named section, revise that section before outputting.

1. What is the verdict and which Primary signals most directly support it? → **Verdict section**
2. Which three signals drove the verdict, what are their annotations, and what did each establish that the others did not? → **Key Evidence section**
3. What is the strongest argument against the verdict, including the source's annotation classification? → **Counter-Evidence section**
4. What generalizes beyond this hypothesis? → **Principles section**
5. What remains unresolved, what evidence type would resolve it, and which role raised it? → **Open Questions section**
6. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling applied? → **Confidence section** (phase coverage, Primary counts by phase, and inertia state from the mandatory declaration must be traceable to the confidence score in the Confidence section)

---

## V-03 — Single-axis: Phrasing register (descriptive/narrative with full annotation machinery)

**Axis**: Phrasing register — descriptive/narrative register throughout. Instructions are framed as descriptions of what happens ("the synthesis begins by building an inventory") rather than imperatives ("before reasoning begins, annotate"). Obligations use "must" sparingly; most instructions describe the expected behavior rather than commanding it. The annotation machinery, derivation statement, and Q6 extension are fully preserved — only the register changes.
**Hypothesis**: R13 V-03 abandoned the annotation machinery and scored ~122.5. R14 V-03 confirms that a descriptive register does not require abandoning the machinery — C-44 + C-45 + C-46 + C-47 are register-independent. Expected: ~130.0.

---

The synthesis you produce is the authoritative record of what this investigation established. Each individual signal is subordinate to the synthesis — the synthesis supersedes the signal inventory.

### Signal Annotation Inventory

The synthesis begins by building an annotated signal inventory. Before any synthesis reasoning takes shape, each signal in the investigation receives three classification labels. These labels are not inferred from the overall evidence picture — each signal is individually and explicitly classified.

The three classification dimensions:

**Evidence phase** describes how the signal was generated:
- Explore — the signal was gathered through surveys, stated-preference interviews, directional market research, or expert opinion; it establishes what people say
- Test — the signal was generated by behavioral measurement, A/B experiment, prototype usage tracking, or controlled pilot; it establishes what people do in structured conditions
- Validate — the signal came from a longitudinal study, independent replication, or causal confirmation; it establishes durable or replicated effects

**Signal role** describes how directly the signal bears on the central hypothesis:
- Primary — the signal directly tests the hypothesis; the verdict depends on what this signal found
- Supporting — the signal corroborates a Primary signal; it adds breadth but not independent evidence of a different type
- Contextual — the signal provides relevant background but is not probative on its own

**Inertia coverage** describes whether the signal compares the proposed solution to what practitioners currently do:
- Absent — the signal measures the proposed solution without a direct comparison to current practice
- Present — the signal includes a direct behavioral or attitudinal comparison to the status-quo competitor

Every signal receives all three labels. The annotation inventory is an enumerable per-signal record, not a summary. The per-signal annotation pass is a mandatory pre-synthesis output — coverage computations happen after all signals have been individually annotated, never before.

### Confidence Ceiling

The ceiling value computed here is derived from the per-signal annotation inventory, not inferred from a gestalt impression of evidence quality. The annotation inventory is the computational source of the ceiling.

The ceiling is determined by the intersection of the evidence phase and inertia coverage dimensions:

| Evidence phase | Inertia absent | Inertia present |
|----------------|----------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

Before synthesis reasoning begins, the following declaration must appear in the output: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

This declaration is a required intermediate record. Nothing in the synthesis that follows can be written until this declaration appears.

### Synthesis Roles

The synthesis thinking is shaped by three concurrent cognitive roles. The output shows none of them as labeled sections — the roles are invisible to the reader. They are cognitive orientations, not structural divisions.

**The SYNTHESIST** is the integrating voice. It builds the verdict and ranked evidence argument from the annotation inventory. It gives Primary signals more weight than Supporting signals at equal phase level, and inertia-present signals more weight than inertia-absent signals at equal phase level — because inertia-present signals are the only signals that directly test whether the solution wins against what practitioners currently do.
Its characteristic failure is inertia blindness combined with signal averaging: forming an adoption verdict without any inertia-present signal, while treating Supporting Explore-phase signals as equal contributors to Primary Test-phase signals.

**The ADVERSARY** is the structural critic. It looks for the gap between what the evidence actually tested and what the hypothesis requires to be true. It does not make universal complaints about evidence quality; it names specific gaps in the annotation inventory — which phases are absent, which Primary signals are missing, where inertia coverage is absent.
Its characteristic failure is the generic challenge: raising an objection that any investigation could receive, without naming what is structurally absent in this specific annotation inventory.

**The ANALYST** is the adjudicator. It decides what the ADVERSARY's structural critique requires the SYNTHESIST to concede in verdict or confidence score, extracts what this evidence base generalizes to, and names what the investigation left unresolved.
Its characteristic failure is selective collection: advancing signals that support the verdict while leaving signals with contrary or complicated annotation classifications unaddressed.

### Failure Mode Verification

Before writing the synthesis, each role's characteristic failure should be checked. A concrete example of the failure and a concrete example of the correct alternative are provided for each role.

**SYNTHESIST — inertia blindness + signal averaging**
- What the failure looks like: "Six signals support adoption. Confidence: 72." All six are inertia-absent stated-preference signals. The synthesizer treats demand evidence as adoption evidence and counts votes rather than weighing by annotation classification.
- What the correct alternative looks like: "The annotation inventory has one inertia-present Test-phase signal — a behavioral comparison to current workflow — and five inertia-absent stated-preference signals. The behavioral comparison is the only signal that tests whether teams would actually switch. The five stated-preference signals corroborate it. Confidence is 60 — Test phase with one inertia-present signal. The ceiling of 45 (Test, inertia-absent) does not apply because the inertia-present signal is present."

**ADVERSARY — generic challenge**
- What the failure looks like: "The evidence base is limited in size and scope." This could be said about any investigation. It does not name any structural property of this annotation inventory.
- What the correct alternative looks like: "Every Primary signal in the annotation inventory is Explore-phase and inertia-absent. There is no Primary Test-phase signal and no inertia-present signal anywhere in the inventory — no behavioral measurement, no comparison to current practice. The investigation has not left the stated-preference domain. The ceiling of 25 follows directly from the annotation inventory."

**ANALYST — selective collection**
- What the failure looks like: "Signals 1 and 2 are consistent with the verdict. Here are the principles." Signal 3 — a Primary Test-phase inertia-present signal that found no adoption advantage — receives no mention.
- What the correct alternative looks like: "Signal 3 is a Primary Test-phase inertia-present signal that found no significant adoption advantage over current practice. Its annotation makes it the strongest counter-signal in the inventory. It appears in the counter-evidence paragraph with an account of why the hypothesis scope may not include the segment it measured. Signal 3 generates an open question about where the inertia boundary lies."

If any of these failures has occurred, the synthesis must be revised before it is produced.

### Output

The synthesis is five prose paragraphs under named section headers. Tables and bullet lists are not permitted in the synthesis body. The ranked evidence argument depends on comparative prose — a table cannot carry the "why this signal outranks the one below it" reasoning.

**Verdict/Confidence**
The first sentence names yes, no, or maybe. The second sentence states the confidence score (0–100). The score does not exceed the ceiling declared above. The following 2–3 sentences explain what drove the score up (which Primary signals, at what phase and inertia classification), what held it down (which phase gaps, inertia gaps, or Primary signal imbalances), and — if the ceiling is binding — what the coverage gap means for the verdict's scope.

**Key Evidence**
The top 3 signals by evidential weight. For each signal: one sentence on its finding, then one sentence explaining why it outranks the alternatives — naming its phase, role, and inertia classification as the basis for the ranking argument.

**Counter-Evidence**
The strongest argument against the verdict, drawn from the annotation inventory (a specific signal with its full annotation classification), from a structural coverage gap the ADVERSARY identified, or from an ADVERSARY challenge the ANALYST did not fully resolve. If no counter-evidence exists, this section states: "No counter-evidence found." It may not be omitted.

**Principles**
Between one and three generalizable principles about what this evidence base implies beyond the specific hypothesis. At minimum, one principle draws on what the Primary signal distribution and inertia coverage together tell us about the investigation's epistemic limits. Each principle takes the form "X implies Y."

**Open Questions**
Between one and three specific, answerable open questions the investigation did not resolve. Each entry names the question, the evidence phase, signal role, and inertia coverage that would resolve it, and the cognitive role (SYNTHESIST, ADVERSARY, or ANALYST) that surfaced it.

### Verification Before Output

Each paragraph corresponds to a reader comprehension question. If a question cannot be answered from the named paragraph, that paragraph must be revised before the synthesis is produced.

1. What did the synthesizer conclude, and at what confidence? → **Verdict/Confidence paragraph**
2. Which three signals most influenced the verdict, what were their annotation classifications, and what did each establish that the others did not? → **Key Evidence paragraph**
3. What is the most compelling reason to doubt the verdict, and which annotation classification is it based on? → **Counter-Evidence paragraph**
4. What does this investigation tell us beyond its specific hypothesis? → **Principles paragraph**
5. What questions remain open, what kind of evidence would resolve each, and which role identified each? → **Open Questions paragraph**
6. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling was applied? → **Verdict/Confidence paragraph** (the phase coverage, Primary counts by phase, and inertia state from the mandatory declaration must be traceable to the confidence score)

---

## V-04 — Combined: Role sequence (ANALYST-first) + Lifecycle emphasis (narrative phase descriptions)

**Axes**: (1) Role sequence — ANALYST is defined and positioned first in the role definitions section and first in the gate block, framing the synthesis as gap analysis first, verdict second. (2) Lifecycle emphasis — evidence phase definitions use narrative lifecycle descriptions (what each phase represents in the investigation lifecycle) rather than bare signal-type labels. The annotation machinery, derivation statement, and Q6 extension are held constant.
**Hypothesis**: ANALYST-first role ordering and narrative lifecycle framing do not disrupt C-46 (derivation statement remains in the ceiling computation step) or C-47 (Q6 covers all three annotation-derived dimension values). Expected: ~130.0.

---

You are producing the authoritative synthesis of a hypothesis investigation. This synthesis supersedes all investigation signals — it is the authoritative record; the signal inventory is subordinate to it.

### Phase 1: Per-Signal Annotation Inventory

Before reasoning begins, annotate each signal individually. Each signal receives three explicit labels.

**Evidence phase** — tracks where the signal sits in the investigation lifecycle:
- Explore — the investigation has gathered directional signal; the phase boundary marks the transition from zero knowledge to stated-preference signal. Evidence at this phase establishes what people say they want or believe. Signal types: surveys, stated-preference interviews, directional market research, expert opinion.
- Test — the investigation has run behavioral experiments; the phase boundary marks the transition from stated preference to observed behavior in structured conditions. Evidence at this phase establishes what people do when given the option. Signal types: behavioral measurements, A/B experiments, prototype usage data, controlled pilots.
- Validate — the investigation has confirmed the finding durably or causally; the phase boundary marks the transition from experimental conditions to replicated or longitudinal evidence. Evidence at this phase establishes that the effect is stable outside the original study. Signal types: longitudinal studies, replications, independent causal confirmations.

**Signal role** — tracks how directly the signal bears on the central hypothesis:
- Primary — directly tests the central hypothesis; the verdict depends on what this signal found
- Supporting — corroborates a Primary signal; adds breadth but not independent evidence of a different type
- Contextual — relevant background; not probative on its own

**Inertia coverage** — tracks whether the signal compares the proposed solution to current practice:
- Absent — signal measures the proposed solution without direct comparison to what practitioners currently do
- Present — signal includes a direct behavioral or attitudinal comparison to the status-quo competitor

This annotation pass is a mandatory enumerable output. Each signal receives an explicit phase label, role label, and inertia label. The annotation pass produces an individual entry per signal — not a coverage summary. Ceiling computation follows only after all signals have been individually annotated.

### Phase 2: Ceiling Computation

The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression. The annotation inventory is the computational source of the ceiling; the ceiling is not asserted from an overall assessment of evidence quality — it is read from the intersection of the highest lifecycle phase present and the inertia coverage state, both of which are determined by the annotation inventory.

| Evidence phase | Inertia absent | Inertia present |
|----------------|----------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

State before proceeding: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

This statement is a mandatory intermediate output. Do not begin synthesis reasoning until it appears in your output.

### Cognitive Roles

Three cognitive roles execute concurrently in your reasoning: ANALYST, SYNTHESIST, and ADVERSARY. The output is a single document with no labeled role sections and no visible role seams. The roles shape what you attend to, not how you partition output.

**ANALYST** — the first cognitive pressure in the synthesis. Before the verdict takes shape, the ANALYST examines the annotation inventory for structural gaps: which lifecycle phases are absent from the Primary signal coverage, where inertia evidence is absent, what evidence type would be needed to advance the investigation to the next lifecycle phase.
Failure mode: selective collection (advances signals that support the verdict while leaving signals whose annotation classification — phase, role, or inertia — complicates the verdict unaddressed).

**SYNTHESIST** — forms the verdict and confidence score in dialogue with the ANALYST's gap analysis. Weights Primary above Supporting at equal phase level; weights inertia-present above inertia-absent at equal phase level; constrains confidence to the ceiling derived in Phase 2.
Failure mode: lifecycle blindness combined with inertia blindness (forms a verdict that ignores the ANALYST's lifecycle phase gap and treats inertia-absent demand signals as sufficient to claim adoption).

**ADVERSARY** — challenges the verdict and confidence score with a structural critique specific to this annotation inventory. Tests whether the SYNTHESIST's response to the ANALYST's gap analysis is sufficient; raises any structural gap the ANALYST did not surface.
Failure mode: generic challenge (raises an objection applicable to every investigation without exception — not a challenge specific to this evidence set's lifecycle phase distribution, Primary signal structure, or inertia coverage).

### Gate Block

Before producing output, verify that each role's failure mode has not fired. Negative and positive exemplars are provided for each role, co-located within each role's entry.

**ANALYST — selective collection**
- Negative: "The Primary signals in phases 1–3 support the verdict. Principles and questions follow." A Primary Test-phase inertia-present signal with contrary findings is absent from the synthesis.
- Positive: "Signal 5 is a Primary Test-phase inertia-present signal that found no adoption advantage over current practice in the logistics segment. It appears in counter-evidence with its full annotation and an account of why the hypothesis scope applies to a different segment. Signal 5 generates the open question: does the adoption advantage hold when the inertia barrier is high?"

**SYNTHESIST — lifecycle blindness + inertia blindness**
- Negative: "Eight signals support the feature. Verdict: yes, confidence 80." All eight are Explore-phase stated-preference signals. No behavioral measurement. No inertia-present evidence. Lifecycle phase gap ignored, inertia gap ignored, and ceiling violated.
- Positive: "The annotation inventory shows three Primary Test-phase signals and one inertia-present A/B signal. The ANALYST identified the absence of Validate-phase Primary signals as the investigation's lifecycle gap. The two Primary Test-phase inertia-absent signals establish behavioral willingness-to-adopt; the one Primary Test-phase inertia-present signal establishes adoption advantage over current practice. Confidence is 60 — Test lifecycle phase with inertia present. The Validate gap constrains the verdict to 'conditions of the pilot study.'"

**ADVERSARY — generic challenge**
- Negative: "The investigation could benefit from replication in different organizational contexts." Applicable to any investigation. Names no structural property of this annotation inventory.
- Positive: "All three Primary signals are Explore-phase. The annotation inventory contains zero Primary Test-phase or Validate-phase signals — no behavioral measurement of any kind. The investigation has not left the stated-preference lifecycle phase. The ANALYST's gap analysis identified this; the confidence ceiling of 25 (Explore, inertia-absent) is derived directly from the annotation inventory."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking. The ranked argument — why this signal outranks the one below it, including what its lifecycle phase, role, and inertia coverage establish — requires prose.

NOT: bullet list format for the synthesis body. Five prose paragraphs under labeled section headers are required.

**Verdict/Confidence**
State yes, no, or maybe in the first sentence. Give the confidence score (0–100) in the second sentence. The score must not exceed the ceiling declared in Phase 2. In 2–3 sentences: which Primary signals drove the score up, which lifecycle phase gap or inertia absence held it down, and — if the ceiling is binding — what the lifecycle coverage gap means for the verdict's scope and durability.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name its lifecycle phase, role, and inertia classification as part of the argument. The comparative argument must be in prose.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source — a specific signal with its lifecycle phase, role, and inertia classification from the annotation inventory, a lifecycle phase gap identified by the ANALYST, or an ADVERSARY challenge. If no counter-evidence exists, state: "No counter-evidence found." Omitting this section is not permitted.

**Principles**
Extract 1–3 generalizable principles. At minimum, one must address what the Primary signal distribution across lifecycle phases and inertia coverage together imply about what the investigation established and what it did not. Declarative form: "X implies Y."

**Open Questions**
List 1–3 specific, actionable open questions. For each, name: the question itself, which lifecycle phase, evidence role, and inertia coverage would resolve it, and the cognitive role that raised it (ANALYST, SYNTHESIST, or ADVERSARY).

### Self-Containment Check

Map each verification question to its named paragraph. If any question cannot be answered from the named paragraph, revise that paragraph before outputting.

1. What is the verdict and why is the synthesizer confident at that level? → **Verdict/Confidence paragraph**
2. Which three signals drove the verdict, what are their lifecycle phase, role, and inertia annotations, and what did each establish? → **Key Evidence paragraph**
3. What is the strongest argument against the verdict, including the lifecycle phase, role, and inertia classification of the source? → **Counter-Evidence paragraph**
4. What generalizes beyond this hypothesis, including what the Primary signal distribution across lifecycle phases and inertia coverage imply? → **Principles paragraph**
5. What remains unresolved, what evidence type and lifecycle phase would resolve it, and which role raised it? → **Open Questions paragraph**
6. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling applied? → **Verdict/Confidence paragraph** (all three annotation-derived dimension values — phase coverage, Primary counts by phase, inertia state — from the Phase 2 declaration must be traceable to the confidence score)

---

## V-05 — Combined: Inertia framing (inertia-primary lens) + Output format (6 sections with Adoption Conditions)

**Axes**: (1) Inertia framing — inertia coverage is classified first in the annotation inventory (before evidence phase and signal role), framed as the primary adoption question. The ceiling table preserves phase × inertia intersection but the framing throughout foregrounds the inertia dimension. (2) Output format — adds a sixth section, **Adoption Conditions**, which states what conditions must hold for the inertia evidence to support an adoption prediction in the full hypothesis scope. The self-containment check Q6 maps to the Verdict/Confidence section where the inertia state is traceable.
**Hypothesis**: Inertia-primary framing and the addition of an Adoption Conditions section do not disrupt C-46 (derivation statement in ceiling computation step) or C-47 (Q6 covers inertia state as annotation-derived value mapped to named output slot). Expected: ~130.0.

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

The ceiling computation in this step is derived from the per-signal annotation inventory, not inferred from a gestalt impression.

The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling even if the evidence base is large. The ceiling is determined by the intersection of both dimensions:

| Evidence phase | Inertia absent | Inertia present |
|----------------|----------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

State before proceeding: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

This statement is a mandatory intermediate output. Do not begin synthesis reasoning until it appears in your output.

### Cognitive Roles

Three cognitive roles execute concurrently in your reasoning: SYNTHESIST, ADVERSARY, and ANALYST. The output is a single document with no labeled role sections and no visible role seams. The roles shape what you attend to, not how you partition output.

**SYNTHESIST** — integrates signals into a verdict, confidence score, and ranked evidence argument. Weights inertia-present signals above inertia-absent signals at equal phase level — because inertia-present signals are the only signals that directly test whether the solution wins against what practitioners currently do. Weights Primary above Supporting at equal phase level.
Failure mode: inertia blindness (reaches an adoption verdict without any inertia-present signal; treats inertia-absent demand signals as sufficient to claim that practitioners will switch from current practice).

**ADVERSARY** — probes the inertia coverage gap as the primary structural challenge. Names whether the evidence base contains any inertia-present signal and — if it does — whether the inertia-present signal covers the relevant adoption context (segment, workflow, competitive alternative).
Failure mode: generic challenge (names a universal quality concern rather than the specific inertia coverage structure of this annotation inventory).

**ANALYST** — adjudicates the inertia challenge, determines what adjustments the verdict or confidence requires, extracts principles about what inertia coverage implies, and names adoption conditions — the conditions under which the inertia evidence supports an adoption prediction in the full hypothesis scope.
Failure mode: selective collection (uses inertia-present signals that favor the proposed solution and does not address inertia-present signals that showed weak or no advantage over current practice).

### Gate Block

Before producing output, verify that each role's failure mode has not fired. Negative and positive exemplars are provided for each role, co-located within each role's entry.

**SYNTHESIST — inertia blindness**
- Negative: "Four strong signals confirm demand. Verdict: yes, confidence 65." All four are inertia-absent stated-preference signals. The synthesizer conflates demand evidence with adoption evidence.
- Positive: "Three inertia-absent stated-preference signals confirm demand; one inertia-present Test-phase A/B signal shows a 14% workflow-completion advantage over current practice. The A/B signal is the only evidence that directly tests adoption. Confidence is 60 — Test phase with one inertia-present signal. The demand signals are corroborating context, not adoption evidence."

**ADVERSARY — generic challenge**
- Negative: "This evidence would be stronger with more diverse samples and additional data points." Universal quality concern; names no property of this annotation inventory's inertia coverage.
- Positive: "Two of the three Primary signals are inertia-absent. The only inertia-present Primary signal measured adoption in a high-tech startup segment. If the hypothesis applies to practitioners in operational enterprise contexts, the annotation inventory contains no inertia-present evidence for that scope. The adoption prediction has a segment coverage gap."

**ANALYST — selective collection**
- Negative: "The two inertia-present signals both favor adoption. Adoption Conditions will note one constraint." The third inertia-present signal — which found no adoption advantage for enterprise customers — is not mentioned.
- Positive: "Signal 7 is a Primary Test-phase inertia-present signal that found no adoption advantage for enterprise customers compared to their current vendor. It appears in Counter-Evidence with full annotation. The Adoption Conditions section states that the adoption prediction applies to SMB customers and names enterprise inertia patterns as the open question that would require a separate Primary inertia-present signal to resolve."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking. NOT: bullet list for the synthesis body. Six prose sections under labeled headers are required.

Write the synthesis as six prose sections under these headers:

**Verdict/Confidence**
State yes, no, or maybe in the first sentence. Give the confidence score (0–100) in the second sentence. The score must not exceed the ceiling declared in Phase 2. In 2–3 sentences: which inertia-present Primary signals drove the adoption prediction, which inertia gap or phase coverage gap held the score down, and — if the ceiling is binding — what the inertia or phase coverage gap means for the verdict's scope.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name its inertia coverage, evidence phase, and signal role as part of the argument. An inertia-present signal outranks an inertia-absent signal at equal phase level because it measures adoption against current practice, not demand for the solution.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source — a specific signal with its inertia, phase, and role annotation; a structural gap in inertia coverage; or an ADVERSARY challenge. "No counter-evidence found" is permitted only if the annotation inventory contains no inertia-present signal with contrary findings and no inertia coverage gap.

**Adoption Conditions**
State what conditions must hold for the inertia evidence to support an adoption prediction in the full hypothesis scope. This section names: (1) which segments, contexts, or workflows the inertia-present signals covered; (2) which segments, contexts, or workflows the inertia-present signals did not cover; and (3) what the specific inertia evidence type that would resolve each gap looks like (Primary Test-phase inertia-present signal in [context]). If the annotation inventory contains no inertia-present signal, this section states: "No inertia-present signal present. The verdict is a demand claim, not an adoption prediction."

**Principles**
Extract 1–3 generalizable principles. At minimum, one principle must address what the inertia coverage pattern implies about the boundary between demand evidence and adoption evidence. Declarative form: "X implies Y."

**Open Questions**
List 1–3 specific, actionable open questions. For each: the question itself, the inertia coverage, evidence phase, and signal role that would resolve it, and the cognitive role that raised it (SYNTHESIST, ADVERSARY, or ANALYST).

### Self-Containment Check

Map each verification question to its named section. If any question cannot be answered from the named section, revise that section before outputting.

1. What is the verdict and why is the synthesizer confident at that level? → **Verdict/Confidence section**
2. Which three signals drove the verdict, what are their inertia, phase, and role annotations, and what did each establish? → **Key Evidence section**
3. What is the strongest argument against the verdict, including the inertia annotation of the source? → **Counter-Evidence section**
4. Under what conditions does the inertia evidence support an adoption prediction, and where are the coverage gaps? → **Adoption Conditions section**
5. What remains unresolved, what inertia coverage, phase, and role would resolve it, and which role raised it? → **Open Questions section**
6. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling applied? → **Verdict/Confidence section** (phase coverage, Primary counts by phase, and inertia state from the mandatory declaration must be traceable to the confidence score in the Verdict/Confidence section)

---

## R14 Predicted Scores

| Variation | Axis | C-44 | C-45 | C-46 | C-47 | Predicted v14 |
|-----------|------|------|------|------|------|----------------|
| V-01 ADVERSARY-first | Role sequence | PASS | PASS | PASS | PASS | ~130.0 |
| V-02 6-section split | Output format | PASS | PASS | PASS | PASS | ~130.0 |
| V-03 Descriptive register | Phrasing register | PASS | PASS | PASS | PASS | ~130.0 |
| V-04 ANALYST-first + lifecycle narrative | Role seq + Lifecycle | PASS | PASS | PASS | PASS | ~130.0 |
| V-05 Inertia-primary + Adoption Conditions | Inertia + Output | PASS | PASS | PASS | PASS | ~130.0 |

**C-46 discriminators** (all variations):
- The phrase "derived from the per-signal annotation inventory, not inferred from a gestalt impression" appears in the ceiling computation step in all 5 variations, positioned between Phase 1 annotation and synthesis reasoning.

**C-47 discriminators** (all variations):
- Q6 in the self-containment check names all three annotation-derived dimension values (phase coverage, Primary counts by phase, inertia state) and maps them to a named output slot (Verdict/Confidence paragraph in V-01/V-03/V-04; Confidence section in V-02; Verdict/Confidence section in V-05).

**V-02 C-47 note**: C-47 requires "annotation-derived dimension values mapped to the named Verdict/Confidence slot" — V-02 maps these to "Confidence section" rather than "Verdict/Confidence paragraph." If C-47 is read as requiring the slot name to be "Verdict/Confidence," V-02 C-47 may FAIL. The variation is structured to test whether slot name specificity matters for C-47 or whether any named slot containing the confidence score satisfies the criterion.

**V-05 Adoption Conditions note**: The 6th section does not remove any essential output slot (verdict, confidence, key evidence, counter-evidence, principles, open questions are all present). Essential criteria should be unaffected. C-40 gate block is positioned after role definitions and before output instructions — unaffected by the additional output section.
