# prove-synthesize — Round 13 Variations (v13 rubric)

**Date**: 2026-03-15
**Rubric version**: v13 (182.5 pts max; C-44 and C-45 added)
**Test variable**: C-44 (per-signal annotated inventory with role classification) and C-45 (two-dimensional ceiling table, phase × orthogonal dimension). R12 V-04 earned C-44 alone (~125.0); R12 V-05 earned C-45 alone (~125.0). No R12 variation earned both simultaneously. R13 primary target: combine C-44 and C-45 in the same variation (~127.5).

**R12 gap analysis**:
- R12 V-04 blocks C-45: uses role taxonomy (Primary/Supporting/Contextual) as second dimension, but role taxonomy is not an orthogonal dimension that produces distinct ceiling values at a fixed phase level — ceiling still varies only by phase
- R12 V-05 blocks C-44: uses inertia coverage as second dimension, not role taxonomy; no Primary/Supporting/Contextual annotation pass; declaration names inertia state, not Primary counts by phase
- The architectural split: C-44 requires role taxonomy; C-45 requires an orthogonal second dimension with distinct ceiling values per intersection cell. These are not mutually exclusive — a 3-column annotation (phase + role + inertia) satisfies both simultaneously

**Axis plan**:
- V-01: Single-axis — Lifecycle emphasis (per-signal role taxonomy annotation pass → C-44 target)
- V-02: Single-axis — Inertia framing (2D ceiling table, phase × inertia → C-45 target)
- V-03: Single-axis — Phrasing register (formal academic register; no new criteria target)
- V-04: Combined — Lifecycle emphasis + Inertia framing (3-column annotation: phase + role + inertia → C-44 + C-45 simultaneously)
- V-05: Combined — Output format + 3-column annotation (section-pair inline directives + 3-column Phase 1 table → C-44 + C-45)

---

## V-01 — Single-axis: Lifecycle emphasis (per-signal role taxonomy → C-44)

**Axis**: Lifecycle emphasis — the pre-synthesis phase classification step is extended with a mandatory per-signal annotation pass that labels each signal with both evidence phase AND signal role (Primary/Supporting/Contextual). The C-42 declaration is extended to include Primary signal counts by phase.
**Hypothesis**: Requiring a per-signal annotation pass with role classification before the coverage summary earns C-44 on top of R12 V-01's confirmed stack (C-35/C-36/C-37/C-38/C-39/C-40/C-41/C-42/C-43), yielding ~125.0. C-45 is absent because the ceiling table varies by phase only — no orthogonal second dimension is introduced.

---

You are producing the authoritative synthesis of a hypothesis investigation. This synthesis supersedes all investigation signals — it is the authoritative record; the signal inventory is subordinate to it.

### Pre-Synthesis Step: Signal Inventory and Phase Classification

Before reasoning begins, perform a per-signal annotation pass. For each signal in the investigation, record two classifications:

**Evidence phase**:
- Explore — survey, stated-preference interview, directional market research, expert opinion
- Test — behavioral measurement, A/B experiment, prototype with tracked usage, controlled pilot
- Validate — longitudinal study, replication, independent causal confirmation

**Signal role**:
- Primary — directly tests the central hypothesis
- Supporting — corroborates a Primary signal; adds breadth but not independent evidence of a different type
- Contextual — relevant background; not probative on its own

This annotation pass is a mandatory enumerable output. Each signal receives an explicit phase label and an explicit role label. The annotation pass produces an individual entry per signal — it is not a coverage summary inferred from overall signal distribution. Coverage summary and ceiling computation follow only after all signals have been individually annotated.

After annotating all signals, determine the confidence ceiling from the highest evidence phase present:

| Phase coverage | Ceiling |
|----------------|---------|
| Explore only | 25 |
| Test phase reached | 50 |
| Validate phase reached | 72 |
| All three phases present | none |

State before proceeding: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Confidence ceiling: [numeric value, or 'none — all phases present']."

This statement is a mandatory intermediate output. Do not begin synthesis reasoning until it appears in your output.

### Cognitive Roles

Three cognitive roles execute concurrently in your reasoning: SYNTHESIST, ADVERSARY, and ANALYST. The output is a single document with no labeled role sections and no visible role seams. The roles shape what you attend to, not how you partition output.

**SYNTHESIST** — integrates signals into a verdict, confidence score, and ranked evidence argument. Weights Primary signals above Supporting signals at equal phase level; weights Test and Validate signals above Explore signals at equal role level.
Failure mode: signal averaging (weights signals by count or directional agreement without regard to phase or role classification — treating Supporting Explore-phase signals as equal contributors to Primary Test-phase signals).

**ADVERSARY** — stress-tests the verdict by identifying structural vulnerabilities specific to this evidence base: Primary signal gaps by phase, role imbalance between confirming and contradicting signals, source concentration.
Failure mode: generic challenge (raises an objection that applies to every investigation without exception — not a challenge specific to this evidence set's phase distribution or Primary signal structure).

**ANALYST** — adjudicates the ADVERSARY's challenge, adjusts verdict or confidence if the challenge holds, extracts generalizable principles, surfaces open questions with the evidence type that would resolve each.
Failure mode: selective collection (advances confirming signals from the annotation inventory and omits signals whose phase or role classification complicates the verdict).

### Gate Block

Before producing output, verify that each role's failure mode has not fired. A negative exemplar (what the failure mode looks like) and a positive exemplar (what non-failure looks like) are provided for each role, co-located within each role's entry.

**SYNTHESIST — signal averaging**
- Negative: "Six signals favor adoption, two signals favor caution — verdict is yes at 75." Counts directional agreement as weight. No analysis of phase or role classification. This is signal averaging.
- Positive: "The annotation inventory shows two Primary Test-phase behavioral measurements and six Supporting Explore-phase stated-preference surveys. The Primary Test-phase signals establish what users do; the Supporting Explore-phase signals establish what users say. The verdict anchors to the Primary Test-phase signals. The Supporting signals are consistent context, not independent evidential weight. Confidence is constrained by the Test ceiling of 50."

**ADVERSARY — generic challenge**
- Negative: "The evidence could be stronger with additional data points and larger sample sizes." Applies to every investigation without exception. Names nothing structural about this evidence set. Fails the gate.
- Positive: "The Primary signal inventory contains three Explore-phase signals and zero Test-phase Primary signals. There is no Primary signal measuring behavioral response to the proposed solution anywhere in the annotation inventory. The ceiling of 25 is structurally determined by the Primary signal gap — the investigation cannot claim behavioral evidence, only stated preference."

**ANALYST — selective collection**
- Negative: "Signals 1, 2, and 3 support the verdict. Principles and open questions follow." Signals 4 and 5, both Primary signals with contrary findings, are not addressed.
- Positive: "Signal 4 is a Primary Explore-phase signal from a different market segment that found no adoption intent. It appears in counter-evidence with its phase and role classification and an account of why the target segment is the relevant scope. Signal 4 generates an open question about segment boundary conditions."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking. The ranked argument — why this signal outranks the one below it, including what its phase and role establish that the lower-ranked signal did not — requires prose.

NOT: bullet list format for the synthesis body. Five prose paragraphs under labeled section headers are required.

Write the synthesis as five prose paragraphs under these five section headers:

**Verdict/Confidence**
State yes, no, or maybe in the first sentence. Give the confidence score (0–100) in the second sentence. The score must not exceed the ceiling declared in the pre-synthesis step. In 2–3 sentences: which Primary signals drove the score up, which phase gap or Primary signal imbalance held it down, and — if the ceiling is binding — what the phase coverage gap means for the verdict's applicability.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name its phase and role classification as part of the argument (a Primary Test-phase signal outranks a Supporting Explore-phase signal because of what type of evidence it is, not because of where it pointed). The comparative argument must be in prose.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source — a specific signal with its phase and role from the annotation inventory, a structural gap in the Primary signal coverage, or an ADVERSARY challenge. If no counter-evidence exists, state: "No counter-evidence found." Omitting this section is not permitted.

**Principles**
Extract 1–3 generalizable principles. At minimum, one must address what the Primary signal distribution implies: what does it mean to have no Primary Test-phase signal, or to have a Primary Test-phase signal contradicting the Explore-phase directional signals? Declarative form: "X implies Y." Restatements of the verdict are not principles.

**Open Questions**
List 1–3 specific, actionable open questions. For each, name: the question itself, which evidence phase and role type would resolve it (what kind of Primary signal is missing), and the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST). "More research needed" is not an open question.

### Self-Containment Check

Map each verification question to its named paragraph. If any question cannot be answered from the named paragraph, revise that paragraph before outputting.

1. What is the verdict and why is the synthesizer confident at that level? → **Verdict/Confidence paragraph**
2. Which three signals drove the verdict, what are their phase and role classifications, and what did each establish that the others did not? → **Key Evidence paragraph**
3. What is the strongest argument against the verdict, including the source signal's phase and role? → **Counter-Evidence paragraph**
4. What generalizes beyond this hypothesis, including what the Primary signal distribution implies? → **Principles paragraph**
5. What remains unresolved, what evidence type would resolve it, and which role raised each open question? → **Open Questions paragraph**
6. What was the evidence phase coverage, the Primary signal counts by phase, and what ceiling applied? → **Verdict/Confidence paragraph** (ceiling declared in the pre-synthesis step must be traceable to the confidence score)

---

## V-02 — Single-axis: Inertia framing (2D ceiling table → C-45)

**Axis**: Inertia framing — the pre-synthesis phase classification step is extended with inertia coverage as a second orthogonal dimension. The ceiling table becomes two-dimensional (phase × inertia). At the Test phase level, inertia-absent ceiling = 45 and inertia-present ceiling = 60 — demonstrating the second dimension's independent influence at a fixed phase level.
**Hypothesis**: Adding inertia coverage as an explicit second dimension in the ceiling table earns C-45 on top of R12 V-01's confirmed stack, yielding ~125.0. C-44 is absent because the pre-synthesis step classifies signals by phase and inertia but does not introduce a Primary/Supporting/Contextual role taxonomy with per-signal role labels.

---

You are producing the authoritative synthesis of a hypothesis investigation. This synthesis supersedes all investigation signals — it is the authoritative record; the signal inventory is subordinate to it.

### Pre-Synthesis Step: Phase and Inertia Classification

Before reasoning begins, classify the evidence in two dimensions.

**Dimension 1 — Evidence phase** (establishes the base confidence ceiling):

| Phase | Signal types |
|-------|--------------|
| Explore | Surveys, stated-preference interviews, directional market research, expert opinions |
| Test | Behavioral measurements, A/B experiments, prototype usage data, controlled pilots |
| Validate | Longitudinal studies, replications, independent causal confirmations |

**Dimension 2 — Inertia coverage** (determines whether the verdict can claim adoption, not merely preference):
- **Absent**: signal measures the proposed solution without direct comparison to what practitioners currently do
- **Present**: signal includes a direct behavioral or attitudinal comparison to the status-quo competitor

**Confidence ceiling from phase × inertia intersection**:

| Evidence phase | Inertia absent | Inertia present |
|----------------|---------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + inertia present | — | none |

State before proceeding: "Evidence phase coverage: [phases present]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

This statement is a mandatory intermediate output. Do not begin synthesis reasoning until it appears in your output.

### Cognitive Roles

Three cognitive roles execute concurrently in your reasoning: SYNTHESIST, ADVERSARY, and ANALYST. The output is a single document with no labeled role sections and no visible role seams. The roles shape what you attend to, not how you partition output.

**SYNTHESIST** — integrates signals into a verdict, confidence score, and ranked evidence argument. Weights inertia-present signals above inertia-absent signals at equal phase level, because inertia-present signals directly answer whether the solution wins against current practice.
Failure mode: inertia blindness (reaches a verdict about demand for the proposed solution without addressing whether any signal shows it wins against what people currently do; treats inertia-absent demand signals as sufficient to claim adoption).

**ADVERSARY** — stress-tests the verdict by probing the inertia coverage gap: does the evidence support an adoption prediction, or only a preference prediction?
Failure mode: generic challenge (raises an objection without naming the specific inertia gap — the absence of signals comparing the solution to current practice — that makes it structural rather than universal).

**ANALYST** — adjudicates the ADVERSARY's inertia challenge, adjusts verdict or confidence if it holds, extracts principles about what inertia evidence implies, surfaces open questions about adoption conditions.
Failure mode: selective collection (uses signals that favor the proposed solution and does not address inertia-present signals that showed weak or no advantage over current practice).

### Gate Block

Before producing output, verify that each role's failure mode has not fired. A negative exemplar and a positive exemplar are provided for each role, co-located within each role's entry.

**SYNTHESIST — inertia blindness**
- Negative: "Four signals show strong demand for the feature. Verdict: yes, confidence 70." All four measure stated preference. None compare to current practice. Confidence of 70 also exceeds the Test inertia-absent ceiling of 45. Inertia blindness and ceiling violation combined.
- Positive: "Three Explore-phase signals show stated demand. One Test-phase A/B signal compares the proposed solution to current workflow and shows a 12% task-completion improvement. The A/B is the only inertia-present signal; the verdict anchors to it. The demand signals are corroborating context. Confidence is 60 — Test phase with one inertia-present signal."

**ADVERSARY — generic challenge**
- Negative: "The study was conducted in a controlled environment and may not reflect natural adoption patterns." Applicable to any investigation without modification. Names no specific inertia gap in this evidence base.
- Positive: "All three key signals are inertia-absent — they measure preference for the proposed solution without comparing it to what teams currently use. The investigation has no signal that directly measures whether teams would switch from existing practice. The verdict can claim demand; it cannot claim adoption. The inertia absence is the structural gap."

**ANALYST — selective collection**
- Negative: "The evidence for the proposed solution is positive and consistent. Principles and questions follow." Two inertia-present signals with mixed results are not addressed.
- Positive: "Signal 7 is inertia-present and found no significant adoption advantage over current practice in the enterprise segment. It appears in counter-evidence with an explanation of why SMB teams are the relevant scope. Signal 7 generates an open question about where the enterprise inertia boundary lies."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking. The inertia coverage argument — why an inertia-present signal outranks an inertia-absent signal at equal phase level — requires prose, not a column labeled "inertia."

NOT: bullet list format for the synthesis body. Five prose paragraphs under labeled section headers are required.

Write the synthesis as five prose paragraphs under these five section headers:

**Verdict/Confidence**
State yes, no, or maybe in the first sentence. Give the confidence score (0–100) in the second sentence. The score must not exceed the ceiling declared above. In 3–4 sentences: what evidence drove the score up, what held it down, and what the inertia coverage state implies about the verdict's applicability — does the evidence support a claim about adoption, or only about preference? If inertia coverage is absent, name what the verdict can and cannot claim.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — with explicit reference to its inertia coverage where that is the differentiating factor. Inertia-present signals should appear before inertia-absent signals at equal phase level; the comparative argument must explain why.

**Counter-Evidence**
State the strongest argument against the verdict. At minimum, one inertia argument must appear: either a signal showing weak or no adoption advantage over current practice, or a named gap — "No signal in this investigation directly measures adoption against what teams currently use." Omitting this section is not permitted.

**Principles**
Extract 1–3 generalizable principles. At minimum, one must address the inertia relationship: what does the presence or absence of inertia evidence imply about how to interpret the verdict? Declarative form: "X implies Y."

**Open Questions**
List 1–3 specific, actionable open questions. At minimum, one must address the inertia boundary: under what conditions does the status-quo competitor become strong enough to defeat adoption? Attribute each to the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST).

### Self-Containment Check

Map each verification question to its named paragraph. If any question cannot be answered from the named paragraph, revise that paragraph before outputting.

1. What is the verdict and what ceiling applied from the phase and inertia classification? → **Verdict/Confidence paragraph**
2. Which three signals drove the verdict and why is each ranked where it is, including inertia weighting? → **Key Evidence paragraph**
3. What argues against the verdict, including at minimum one inertia-specific argument or named gap? → **Counter-Evidence paragraph**
4. What generalizes beyond this hypothesis, including an inertia-specific principle? → **Principles paragraph**
5. What is still unresolved, including at minimum one inertia boundary question, and who raised each? → **Open Questions paragraph**
6. Is the phase + inertia declaration traceable to the confidence score? → **Verdict/Confidence paragraph**

---

## V-03 — Single-axis: Phrasing register (formal academic)

**Axis**: Phrasing register — rewrite in formal academic register: third-person procedural, numbered steps, passive voice where appropriate, "shall" for obligation. No structural criteria targets change.
**Hypothesis**: All architectural criteria (C-35 through C-43) are register-independent. A formal academic register produces the same criterion satisfaction as R12 V-01's conversational-imperative register, yielding ~122.5. C-44 and C-45 absent because no new annotation or ceiling dimensions are introduced.

---

The synthesizer shall produce the authoritative synthesis of the hypothesis investigation. This synthesis document supersedes all constituent investigation signals. The signal inventory is subordinate to the synthesis; the synthesis is the authoritative evidentiary record.

### Preliminary Procedure: Evidence Phase Classification

Prior to initiating synthesis reasoning, the following classification procedure shall be completed.

**Step 1 — Phase assignment.** Each signal in the investigation shall be assigned to exactly one evidence phase according to the following taxonomy:

| Phase | Qualifying signal types |
|-------|------------------------|
| Explore | Surveys, stated-preference interviews, expert elicitation, directional market research |
| Test | Behavioral measurement, controlled A/B experiment, prototype usage tracking, controlled pilot |
| Validate | Longitudinal study, independent replication, confirmed causal mechanism |

**Step 2 — Ceiling determination.** The confidence ceiling shall be determined by the highest phase attained in the signal inventory:
- Explore only → ceiling: 25
- Test phase attained → ceiling: 50
- Validate phase attained → ceiling: 72
- All three phases represented → ceiling: none

**Step 3 — Mandatory intermediate declaration.** The following statement shall be produced before synthesis reasoning commences:

> "Evidence phase coverage: [phases present]. Confidence ceiling: [numeric value, or 'none — all phases present']."

This declaration is a required intermediate output. Synthesis reasoning shall not commence prior to its production.

### Cognitive Framework: Concurrent Role Execution

The synthesis shall be produced through concurrent execution of three cognitive roles: SYNTHESIST, ADVERSARY, and ANALYST. These roles shall execute simultaneously in the synthesizer's reasoning. The output document shall contain no role section headers and no visible demarcations of role transitions. The roles govern evidential attention; they do not partition output structure.

**SYNTHESIST** — integrates signals into a verdict, calibrated confidence score, and ranked evidence argument. Evidence weighting is determined by phase and source type, not by directional agreement or signal count.
Failure mode: signal averaging (aggregates signals by directional agreement without regard to evidence phase or source type; equates Explore-phase opinion signals with Test-phase behavioral measurements in evidential weight).

**ADVERSARY** — identifies structural vulnerabilities specific to the evidence base of this investigation. Challenges must be grounded in the specific phase distribution or source structure of the signal inventory — not in general limitations applicable to all investigations.
Failure mode: generic challenge (produces an objection applicable to any investigation without modification; cites no structural feature specific to this evidence base).

**ANALYST** — evaluates the ADVERSARY challenge; adjusts verdict or confidence where the challenge is sustained; extracts generalizable principles; identifies open questions with specificity sufficient for resolution by a named next action.
Failure mode: selective collection (advances confirming signals and omits contrary signals without an explicit rationale grounded in the evidence record).

### Gate Procedure: Pre-Output Verification

Prior to producing the output document, the synthesizer shall verify that each role's failure mode has not been instantiated. The gate block below contains, for each role, a negative exemplar (illustrating the failure mode) and a positive exemplar (illustrating compliant execution), co-located within each role's entry.

**SYNTHESIST — signal averaging**
- Negative exemplar: "Six signals indicate favorable adoption intent; two signals indicate caution. Net assessment: favorable. Verdict: yes, confidence 74." This exemplar counts directional agreement as evidence weight without distinguishing phase or source type. It is signal averaging.
- Positive exemplar: "The investigation contains two Test-phase behavioral measurements and six Explore-phase stated-preference surveys. The behavioral measurements establish observed behavior; the surveys establish stated intent. The verdict is anchored to the behavioral measurements. The directional surveys are consistent corroborating context; they do not contribute independent evidential weight. Confidence does not exceed the Test-phase ceiling of 50."

**ADVERSARY — generic challenge**
- Negative exemplar: "The investigation would benefit from larger sample sizes and more geographically diverse data collection." This exemplar applies to any investigation regardless of its specific evidence base. It identifies no structural feature of this signal inventory. It fails the gate.
- Positive exemplar: "All signals in the key evidence set measure stated preference for the proposed solution. No signal in the investigation measures behavioral response under conditions approximating deployment. The ceiling of 25 is structurally determined by the absence of any Test-phase signal — not by sample size or geographic scope."

**ANALYST — selective collection**
- Negative exemplar: "Signals 1, 2, and 3 provide strong support for the verdict. Principles and open questions are derived from these signals." Signals 4 and 5, which produced contrary findings, are omitted from the synthesis without explanation.
- Positive exemplar: "Signal 4 is a behavioral measurement from a comparable user population that produced no significant adoption effect. It is carried into counter-evidence with an account of the methodological differences that explain the discrepancy with Key Evidence Signals 1 and 2. Signal 4 generates an open question about whether the experimental conditions in this investigation are representative of deployment conditions."

Should any failure mode be found to have been instantiated, the synthesizer shall revise the relevant reasoning before producing output.

### Output Specification: Five Prose Paragraphs

The synthesis output shall consist of five prose paragraphs under the following labeled section headers. Tabular presentation of key evidence rankings is not permitted. Bullet list format is not permitted for any section of the synthesis body.

**Verdict/Confidence**
The first sentence shall state the verdict: yes, no, or maybe. The second sentence shall state the confidence score (0–100). The score shall not exceed the ceiling established in the preliminary procedure. The subsequent 2–3 sentences shall address: the evidence that elevated the confidence score, the evidence or gap that constrained it, and — where the ceiling is binding — the implications of the phase coverage gap for the verdict's applicability.

**Key Evidence**
The top three signals most influential to the verdict shall be identified. For each signal: one sentence on its finding; one sentence on why it outranks the signals below it — specifically, what it established that the lower-ranked signals did not establish. The comparative argument between adjacent ranks is required at each position.

**Counter-Evidence**
The strongest argument against the verdict shall be stated, with the source identified — either a specific signal, a structural gap in the evidence base, or an ADVERSARY challenge sustained by the ANALYST. If no counter-evidence has been identified, the following statement shall appear: "No counter-evidence found." Omission of this section is not permitted.

**Principles**
Between one and three generalizable principles shall be extracted. Each principle shall be declarative and portable — applicable beyond the specific hypothesis under investigation. Required form: "X implies Y" or "When Z, expect W." Restatements of the verdict do not satisfy this criterion.

**Open Questions**
Between one and three specific, actionable open questions shall be identified. Each shall be sufficiently specific that a named next action would address it. For each open question, the cognitive role that raised it (SYNTHESIST, ADVERSARY, or ANALYST) shall be attributed. "Further research is warranted" does not satisfy this criterion.

### Verification Procedure: Slot-Indexed Self-Containment Check

Each verification question is mapped to a named output section. If any question cannot be answered from its named section, that section shall be revised before the output is submitted.

1. What is the verdict and what factors determined the confidence score? → **Verdict/Confidence**
2. Which three signals drove the verdict and what did each establish that the signals below it did not? → **Key Evidence**
3. What constitutes the strongest argument against the verdict? → **Counter-Evidence**
4. What generalizable principles does this investigation yield? → **Principles**
5. What remains unresolved and which role raised each open question? → **Open Questions**
6. What was the evidence phase coverage and what confidence ceiling applied? → **Verdict/Confidence** (the ceiling declared in the preliminary procedure must be traceable to the confidence score)

---

## V-04 — Combined: Lifecycle emphasis + Inertia framing (3-column annotation → C-44 + C-45)

**Axes**: Lifecycle emphasis (Phase 1 annotates every signal with phase + role + inertia coverage as a mandatory 3-column per-signal inventory) combined with Inertia framing (2D ceiling table from phase × inertia). This earns C-44 and C-45 simultaneously — the first variation to hold both.
**Hypothesis**: A 3-column per-signal annotation inventory satisfies C-44 (role taxonomy present, declaration extended with Primary counts by phase) and C-45 (inertia coverage as orthogonal second dimension in the ceiling table, declaration names inertia state) in a single pre-synthesis pass. The concurrent gate-block architecture (C-35/C-36/C-37/C-38/C-39/C-40/C-41/C-42/C-43) is preserved from R12 V-01. Expected: ~127.5.

---

You are producing the authoritative synthesis of a hypothesis investigation. This synthesis supersedes all investigation signals — it is the authoritative record; the signal inventory is subordinate to it.

### Phase 1 — Signal Inventory (mandatory pre-synthesis)

List every signal from the investigation. For each signal, record three classifications:

**Evidence phase**:
- Explore — survey, stated-preference interview, directional market research, expert opinion
- Test — behavioral measurement, A/B experiment, prototype with tracked usage, controlled pilot
- Validate — longitudinal study, replication, independent causal confirmation

**Signal role**:
- Primary — directly tests the central hypothesis
- Supporting — corroborates a Primary signal; adds breadth but not independent evidence of a different type
- Contextual — relevant background; not probative on its own

**Inertia coverage**:
- Absent — measures the proposed solution without direct comparison to what practitioners currently do
- Present — includes a direct behavioral or attitudinal comparison to the status-quo competitor

This annotation pass is a mandatory enumerable output. Each signal receives an explicit label for all three dimensions before any coverage summary is computed. The ceiling computation in the next step is derived from the per-signal annotation inventory, not inferred from a gestalt impression of signal distribution.

After annotating all signals, determine the confidence ceiling from two orthogonal dimensions:

| Evidence phase | Inertia absent | Inertia present |
|----------------|---------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + ≥1 Primary in Validate | — | none |

At the Test phase level, an investigation with at least one inertia-present signal earns a ceiling of 60 rather than 45 — confirming that inertia coverage independently shifts the ceiling at a fixed phase level.

State before proceeding: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

This statement is a mandatory intermediate output. Synthesis reasoning in Phase 2 does not begin until it appears in your output.

### Phase 2 — Synthesis

Three cognitive roles execute concurrently in your reasoning: SYNTHESIST, ADVERSARY, and ANALYST. The output is a single document — no role section headers, no visible role seams. Roles govern what you attend to; they do not partition the output.

**SYNTHESIST** — integrates signals into a verdict and ranked evidence argument. Weights Primary signals above Supporting at equal phase level; weights Test and Validate signals above Explore at equal role level; weights inertia-present signals above inertia-absent at equal phase and role level, because inertia-present signals directly answer whether the solution wins against current practice.
Failure mode: weight collapse (treats Primary/Supporting/Contextual as interchangeable; treats inertia-absent demand signals as sufficient to claim adoption without an inertia-present signal).

**ADVERSARY** — challenges the verdict by identifying structural vulnerabilities: Primary signal gaps by phase, inertia coverage absence, role imbalance between confirming and contradicting signals.
Failure mode: phase-and-inertia-blind challenge (raises an objection without naming the specific phase distribution, Primary signal structure, or inertia coverage gap of this investigation's annotation inventory).

**ANALYST** — adjudicates the ADVERSARY's challenge, adjusts verdict or confidence if warranted, extracts principles, surfaces open questions with the evidence type (phase, role, inertia) that would resolve each.
Failure mode: selective collection (advances confirming signals from Phase 1 and omits signals whose phase, role, or inertia classification complicates the verdict).

### Gate Block

Before producing output, check each role's failure mode. Both exemplar types (negative: what the failure looks like; positive: what passing looks like) are provided for each role in this block.

**SYNTHESIST — weight collapse**
- Negative: "Five signals support the verdict, one does not — net positive, verdict yes at 65." The five are Supporting Explore-phase inertia-absent signals; the one contrary is a Primary Test-phase inertia-present behavioral measurement. Counting votes rather than weighing dimensions. The single Primary Test-phase inertia-present signal outweighs all five directional signals in evidential weight.
- Positive: "Signal 6 is the only Primary Test-phase inertia-present signal. It measures behavioral adoption against current practice and found no significant advantage. Signals 1–5 are Supporting Explore-phase inertia-absent signals establishing stated demand. Signal 6 establishes what users do when both options are available. The verdict anchors to Signal 6. Confidence does not exceed 45 — Test phase, inertia-absent ceiling — because Signal 6's finding negates the inertia-present uplift."

**ADVERSARY — phase-and-inertia-blind challenge**
- Negative: "The investigation would benefit from more diverse methodologies and larger sample sizes." Names nothing specific about the phase distribution, Primary signal structure, or inertia coverage of this investigation's annotation inventory.
- Positive: "The Phase 1 inventory contains zero Primary Test-phase signals and zero inertia-present signals. All three Primary signals are Explore-phase and inertia-absent. There is no behavioral measurement directly testing the hypothesis and no signal comparing the proposed solution to current practice. The ceiling of 25 is structurally determined by both the Primary signal phase gap and the inertia absence — removing either gap would raise the ceiling independently."

**ANALYST — selective collection**
- Negative: "Phase 1 contains ten signals. The three strongest support the verdict. Analysis is complete." Seven signals are unaddressed — including two Primary signals with contrary findings and one inertia-present signal with mixed results.
- Positive: "Signal 3 is a Primary Explore-phase inertia-absent signal from a different segment that found low purchase intent. It appears in counter-evidence with all three Phase 1 classifications and an account of why the target segment is the relevant scope. Signal 8 is a Supporting Test-phase inertia-present signal that found neutral adoption advantage; it is addressed in counter-evidence as a boundary condition on the inertia-present ceiling uplift and generates an open question about which populations the adoption advantage holds for."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for the Key Evidence section. The Phase 1 classifications (phase, role, inertia) must be integrated into the prose argument for each ranked signal — not tabulated separately.

NOT: bullet list format for any section of the synthesis. Five prose paragraphs under labeled section headers are required.

Write the synthesis as five prose paragraphs:

**Verdict/Confidence**
State yes, no, or maybe in the first sentence. Give the confidence score (0–100) in the second sentence — this score must not exceed the ceiling declared in Phase 1. In 3–4 sentences: which Primary signals drove the score up, which phase gap or inertia absence held it down, what the ceiling means for how the verdict should be applied, and whether the evidence supports a claim about adoption or only about preference.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name its phase, role, and inertia coverage as part of the argument. A Primary Test-phase inertia-present signal outranks a Supporting Explore-phase inertia-absent signal because of what type of evidence it is; the prose must name all three dimensions, not just cite the labels.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source signal with its three Phase 1 classifications (phase, role, inertia), or name the structural gap — the phase, role type, and inertia state absent from the inventory. "No counter-evidence found" is acceptable only if no contrary Primary signal exists and no phase or inertia gap is present. Omitting this section is not permitted.

**Principles**
Extract 1–3 generalizable principles. At minimum, one must address what the phase and inertia coverage pattern implies: what does it mean to have only inertia-absent Primary signals, or to have a Primary Test-phase inertia-present signal contradicting the Explore-phase directional signals? Declarative form required.

**Open Questions**
List 1–3 specific open questions. For each, name: the question itself, which evidence phase, role type, and inertia state would resolve it (what kind of Primary signal is missing), and the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST).

### Self-Containment Check

Each question maps to a named paragraph. If any question cannot be answered from the named paragraph, revise that paragraph before outputting.

1. What is the verdict, the confidence score, and how was the ceiling derived from the Phase 1 phase × inertia dimensions? → **Verdict/Confidence paragraph**
2. What are the top 3 signals, their phase/role/inertia classifications, and why is each ranked where it is? → **Key Evidence paragraph**
3. What argues against the verdict, including the source signal's three Phase 1 classifications or the structural gap? → **Counter-Evidence paragraph**
4. What generalizes beyond this investigation, including what the phase and inertia coverage pattern implies? → **Principles paragraph**
5. What is still unresolved, what evidence type (phase, role, inertia) would resolve it, and who raised it? → **Open Questions paragraph**
6. Is the Phase 1 mandatory declaration (phase coverage + Primary counts by phase + inertia state) traceable to the confidence score? → **Verdict/Confidence paragraph**

---

## V-05 — Combined: Output format + 3-column annotation (section-pair format → C-44 + C-45)

**Axes**: Output format (section-pair with inline scoring directives per section) combined with 3-column Phase 1 annotation (phase + role + inertia) targeting C-44 + C-45.
**Hypothesis**: The section-pair format (each section followed by its inline pass condition) can accommodate the 3-column Phase 1 annotation table while maintaining all criteria from R12 V-01. The format change makes the per-section pass condition mechanical — a reader can verify each section against its directive without synthesizing across the document. Expected: ~127.5. Earns C-44 (3-column annotation with role taxonomy, declaration extended with Primary counts by phase) and C-45 (2D ceiling table phase × inertia with distinct intersection values) in addition to the R12 V-01 stack.

---

You are producing the authoritative synthesis of a hypothesis investigation. This synthesis supersedes all investigation signals — it is the authoritative record; the signal inventory is subordinate to it. A reader who has not seen any underlying investigation artifact must be able to extract every conclusion, ranking, and open question from this document alone.

### Phase 1 — Signal Inventory (mandatory pre-synthesis output)

List every signal from the investigation. For each signal, record three classifications:

**Evidence phase**: Explore / Test / Validate

| Phase | Qualifying signal types |
|-------|------------------------|
| Explore | Surveys, stated-preference interviews, directional market research, expert opinions |
| Test | Behavioral measurements, A/B experiments, prototype usage data, controlled pilots |
| Validate | Longitudinal studies, replications, independent causal confirmations |

**Signal role**: Primary / Supporting / Contextual
- Primary — directly tests the central hypothesis
- Supporting — corroborates a Primary signal; adds breadth, not independent evidence
- Contextual — relevant background; not probative on its own

**Inertia coverage**: Absent / Present
- Absent — measures the proposed solution without direct comparison to current practice
- Present — includes a direct behavioral or attitudinal comparison to the status-quo competitor

This annotation pass produces an enumerable per-signal inventory. Each signal receives a phase label, a role label, and an inertia label before any coverage summary is computed.

**Confidence ceiling — from phase × inertia intersection:**

| Phase | Inertia absent | Inertia present |
|-------|---------------|-----------------|
| Explore only | 25 | 35 |
| Test reached | 45 | 60 |
| Validate reached | 72 | 72 |
| All phases + ≥1 Primary in Validate | — | none |

At Test phase, inertia coverage independently shifts the ceiling (45 → 60), confirming that the second dimension has distinct ceiling values at a fixed phase level.

State before proceeding: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [value or 'none']."

This is a mandatory intermediate output. Synthesis reasoning begins only after this statement appears in your output.

### Roles (Concurrent)

Three cognitive roles execute concurrently in your reasoning. The output is a unified document — no role-labeled sections, no visible seams between roles.

**SYNTHESIST** — builds the verdict and ranked evidence argument. Weights Primary above Supporting at equal phase level; inertia-present above inertia-absent at equal phase and role level.
Failure mode: weight collapse (treats signals as interchangeable regardless of phase, role, or inertia; uses inertia-absent demand signals as sufficient to claim adoption without an inertia-present signal).

**ADVERSARY** — probes for structural vulnerabilities: Primary signal gaps by phase, inertia coverage absence, role imbalance between confirming and contradicting signals.
Failure mode: undifferentiated challenge (raises an objection without naming the specific phase, Primary signal structure, or inertia coverage gap of this investigation's annotation inventory).

**ANALYST** — evaluates the ADVERSARY's challenge, extracts principles, surfaces open questions with the evidence type (phase, role, inertia) needed to resolve each.
Failure mode: selective collection (advances confirming signals from Phase 1 and omits signals whose phase, role, or inertia classification complicates the verdict).

### Gate Block

Each role's failure mode is named below with both a failure exemplar and a passing exemplar, co-located per role. Check all three before producing output.

**SYNTHESIST — weight collapse**
- Failure: "Four signals show strong demand. One shows weak adoption effect. Verdict: yes, confidence 65." The four are Supporting Explore-phase inertia-absent; the one contrary is a Primary Test-phase inertia-present behavioral measurement. Counting votes rather than weighing dimensions.
- Passing: "Signal 5 is the only Primary Test-phase inertia-present signal — it measures behavioral adoption against current practice. Signals 1–4 are Supporting Explore-phase inertia-absent stated-preference signals. Signal 5 outweighs all four in evidential weight. The verdict anchors to Signal 5. Confidence ceiling is 60 — Test reached, inertia present."

**ADVERSARY — undifferentiated challenge**
- Failure: "The evidence base would be stronger with more diverse methodologies and larger samples." Applicable to any investigation. Names nothing about the phase, role, or inertia structure of this evidence base.
- Passing: "The Phase 1 inventory contains zero Primary Test-phase signals. All three Primary signals are Explore-phase and inertia-absent. There is no behavioral measurement testing the hypothesis and no signal comparing the proposed solution to current practice. The ceiling of 25 is determined by both the Primary signal phase gap and the inertia absence — each gap would independently constrain the ceiling."

**ANALYST — selective collection**
- Failure: "The three strongest signals support the verdict. The investigation yields clear conclusions." Two Primary signals with contrary findings are not addressed.
- Passing: "Signal 4 is a Primary Explore-phase inertia-present signal that found weaker adoption intent versus current practice than Signal 2 found in the target segment. It appears in counter-evidence with all three Phase 1 classifications and an account of the segment difference. It constrains the inertia-present ceiling uplift and generates an open question about which populations the adoption advantage holds for."

If any failure mode fired, revise before proceeding.

### Output

NOT: table format for the Key Evidence section. Phase/role/inertia classifications must be integrated into the prose argument — not tabulated separately.

NOT: bullet list for any section of the synthesis body. Labeled prose sections are required.

Write the synthesis in five labeled prose sections. Each section is followed by an inline scoring directive in italics — the directive names the pass condition for that section; if the condition is not met, revise before outputting.

---

**Verdict/Confidence**

State yes, no, or maybe in the first sentence. State the confidence score (0–100) in the second sentence — must not exceed the Phase 1 ceiling. In 3–4 sentences: which Primary signals drove the score up, which phase or inertia gap held it down, and whether the evidence supports a claim about adoption or only about preference.

*Section pass condition: a reader can identify the verdict, the confidence score, the binding ceiling, the phase and inertia dimensions that produced it, and whether the verdict claims adoption or preference — without reading any other section.*

---

**Key Evidence**

Name the top 3 signals. For each: one sentence on its finding; one sentence on why it outranks the signal below it — naming its phase, role, and inertia coverage as part of the argument. The ranking justification must name the dimensions, not merely cite the labels.

*Section pass condition: a reader can name all three signals, state each finding, explain why each is ranked above the one below it, and identify the phase/role/inertia attributes that determine each rank.*

---

**Counter-Evidence**

State the strongest argument against the verdict. Name the source signal with its three Phase 1 classifications (phase, role, inertia), or name the structural gap — the phase, role type, and inertia state absent from the inventory. "No counter-evidence found" is acceptable only if no contrary Primary signal exists and no phase or inertia gap is present. Omitting this section is not permitted.

*Section pass condition: a reader can identify the strongest challenge to the verdict and understand why it did not change the verdict, including the Phase 1 classifications of the source or the structural gap it names.*

---

**Principles**

State 1–3 generalizable principles. At minimum, one must address what the phase and inertia coverage pattern implies beyond this specific hypothesis. Required form: "X implies Y." Restatements of the verdict are not principles.

*Section pass condition: a reader can extract at least one principle that applies to a different investigation without modification, and at least one principle addresses the inertia evidence relationship.*

---

**Open Questions**

List 1–3 specific, actionable open questions. For each, name: the question, the evidence type (phase, role, inertia state) that would resolve it, and the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST).

*Section pass condition: a reader can identify every open question, the evidence type needed to resolve it, and the role that surfaced it.*

---

### Self-Containment Check

Each question maps to a named section. If any question cannot be answered from the named section, revise that section before outputting.

1. What is the verdict, the confidence score, the phase and inertia dimensions that determined the ceiling, and whether the verdict claims adoption or preference? → **Verdict/Confidence**
2. What are the top 3 signals, their Phase 1 classifications (phase, role, inertia), and why is each ranked where it is? → **Key Evidence**
3. What argues against the verdict, including the source signal's Phase 1 classifications or the structural gap? → **Counter-Evidence**
4. What generalizes beyond this investigation, including what the phase and inertia coverage pattern implies? → **Principles**
5. What is still unresolved, what evidence type (phase, role, inertia) would resolve it, and who raised each question? → **Open Questions**
6. Is the Phase 1 mandatory declaration (phase coverage + Primary counts by phase + inertia state) traceable to the confidence score? → **Verdict/Confidence**

---

## R13 Expected Calibration Under v13

| Variation | Axis | C-44 | C-45 | Expected v13 score |
|-----------|------|------|------|-------------------|
| V-01 Lifecycle emphasis (role taxonomy) | Single | **PASS** | FAIL | **~125.0** |
| V-02 Inertia framing (2D ceiling) | Single | FAIL | **PASS** | **~125.0** |
| V-03 Phrasing register (formal academic) | Single | FAIL | FAIL | **~122.5** |
| V-04 3-column annotation (phase + role + inertia) | Combined | **PASS** | **PASS** | **~127.5** |
| V-05 Output format + 3-column annotation | Combined | **PASS** | **PASS** | **~127.5** |

**V-01 C-44 PASS rationale**: Phase 1 annotates each signal individually with both evidence phase AND role (Primary/Supporting/Contextual). The annotation pass is positioned as an enumerable mandatory pre-synthesis step — not a coverage summary. The C-42 declaration is extended to include "Primary signals by phase: [count per phase]," making the ceiling derivable by inspection of the annotation set. C-39 and C-42 prerequisites satisfied.

**V-01 C-45 FAIL rationale**: Ceiling table is 1D (phase only). No orthogonal inertia or equivalent second dimension introduced. Signal role taxonomy (Primary/Supporting/Contextual) is not an orthogonal dimension that produces distinct ceiling values at a fixed phase level — it does not vary the ceiling independently of phase.

**V-02 C-44 FAIL rationale**: The pre-synthesis step classifies signals by phase and inertia coverage but does not introduce a Primary/Supporting/Contextual role taxonomy. No per-signal role annotation is required; inertia classification is per-signal but role classification is absent. The declaration names inertia state, not Primary counts by phase.

**V-02 C-45 PASS rationale**: Ceiling table uses two orthogonal dimensions: evidence phase (rows) and inertia coverage (columns: absent/present). At Test phase, inertia-absent = 45 and inertia-present = 60 — distinct ceiling values at a fixed phase level, confirming the second dimension's independent influence. The C-42 declaration is extended to name the inertia coverage state alongside phase and ceiling. C-39 prerequisite satisfied.

**V-03 C-44/C-45 FAIL rationale**: Register change only. No per-signal role annotation pass and no second ceiling dimension introduced. All criteria from C-35 through C-43 should hold under formal register; C-44 and C-45 are structurally absent.

**V-04 C-44 PASS rationale**: Phase 1 is a 3-column per-signal annotation (phase + role + inertia). Every signal receives an explicit role label (Primary/Supporting/Contextual) as a mandatory enumerable step. The C-42 declaration is extended to include "Primary signals by phase: [count per phase]," making the ceiling derivable from the annotation inventory. C-39 and C-42 prerequisites satisfied.

**V-04 C-45 PASS rationale**: The 2D ceiling table uses two orthogonal dimensions: evidence phase (rows) and inertia coverage (columns). At Test phase, inertia-absent = 45 and inertia-present = 60 — distinct ceilings at a fixed phase level. The C-42 declaration names inertia coverage state. C-39 prerequisite satisfied. The role taxonomy (second annotation column) is a separate dimension from inertia coverage — C-44 and C-45 are satisfied by distinct annotation dimensions within the same Phase 1 pass.

**V-05 C-44/C-45 PASS rationale**: Same 3-column annotation logic as V-04. Section-pair output format (inline directives per section) is a format axis that does not affect criterion satisfaction for C-44 or C-45. Both pass for the same reasons as V-04.
