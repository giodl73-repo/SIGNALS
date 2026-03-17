Written to `simulations/quest/golden/prove-synthesize-golden-2026-03-14.md`.

**prove-synthesize quest complete.**

- **Winning variation**: V-01 — Role sequence ADVERSARY-ANALYST-SYNTHESIST + Adoption Boundaries
- **Simplified prompt**: ~1,340 words (21 cuts, 20% reduction, all 60 criteria preserved)
- **Score**: 157.5 / 215.0 (v20) · 162.5 / 220.0 (v21 retroactive)

The five patterns that made it golden:

1. **Per-signal annotation inventory as mandatory enumerable intermediate output.** Phase 1 locks one labeled entry per signal before any reasoning — "not a coverage summary" is the disqualifying constraint that creates the audit trail all downstream checks point back to.

2. **Dual-dimension independence constraint in Phase 2.** "A larger or higher-quality inertia-absent evidence base cannot exceed the ceiling" forecloses both volume and quality as compensatory routes in a single sentence. This one clause satisfies C-57, C-59, and seeds C-60.

3. **Ceiling Declaration as first structurally locked output section.** "Do not begin synthesis reasoning until the Ceiling Declaration appears" converts the ceiling from a rule into a sequencing constraint — the verdict cannot precede the ceiling on record.

4. **Per-role dual exemplars in the gate block.** Negative + positive exemplar co-located within each role's entry converts the gate from a checklist into a discrimination task. The model must match its draft against both forms, not just acknowledge the rule.

5. **Slot-indexed self-containment check as unconditional revision gate.** Seven numbered questions each mapped by arrow to a named section, with "revise if unable" as a hard instruction. Combined with "omitting this section is not permitted" (Counter-Evidence) and the gate block revision mandate, three independent revision triggers fire at different stages.
s in the annotation inventory and reads the corresponding cell in the table below can independently derive the ceiling.

The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, a larger or higher-quality inertia-absent evidence base cannot exceed the inertia-absent ceiling — evidence volume does not compensate for inertia absence.

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

Three cognitive roles execute concurrently in your reasoning: ADVERSARY, ANALYST, and SYNTHESIST. The output is a single document with no labeled role sections and no visible role seams.

**ADVERSARY** — Before any verdict takes shape, the ADVERSARY examines the annotation inventory for its structural vulnerabilities: inertia coverage gap, Primary signal phase distribution, source concentration, and the gap between what was measured and what the hypothesis requires to be true.
Failure mode: generic challenge (raises an objection not specific to this annotation inventory).

**ANALYST** — adjudicates the ADVERSARY's structural critique before the SYNTHESIST forms a verdict. Determines which structural gaps are disqualifying for an adoption claim, which are scope-limiting, and which are open questions only. Extracts what adjustments those determinations require in verdict or confidence score.
Failure mode: selective collection (advances confirming signals while omitting disconfirming ones).

**SYNTHESIST** — forms the verdict and confidence score after the ADVERSARY's challenge and the ANALYST's adjudication have been processed. Integrates signals into a ranked evidence argument; weights Primary signals above Supporting at equal phase level; weights inertia-present signals above inertia-absent at equal phase level; constrains confidence to the ceiling derived in Phase 2.
Failure mode: premature integration (forms the verdict without the ADVERSARY's structural critique or ANALYST's adjudication).

### Gate Block

Before producing output, verify that each role's failure mode has not fired.

**ADVERSARY — generic challenge**
- Negative: "The investigation would benefit from larger samples and longer observation periods." Applicable to any investigation. Names no structural property of this annotation inventory.
- Positive: "The Phase 1 inventory contains four Primary Explore-phase signals and zero Primary Test-phase signals. The ceiling of 25 is read from the intersection of the highest phase present (Explore) and the inertia coverage state (absent) — both determined by the annotation inventory."

**ANALYST — selective collection**
- Negative: "Signals 1, 3, and 5 support the verdict. The ADVERSARY's challenge is noted. Principles follow." Signals 2 and 4 — both Primary signals with contrary findings — are absent.
- Positive: "Signal 4 is a Primary Test-phase inertia-present signal that found no adoption advantage over current practice — confirming the ADVERSARY's inertia coverage challenge. The SYNTHESIST must scope the verdict to the tested segment or lower confidence."

**SYNTHESIST — premature integration**
- Negative: "Seven signals point toward adoption. Verdict: yes, confidence 75." No engagement with the ADVERSARY's structural critique. Ceiling violated.
- Positive: "The ADVERSARY identified zero Primary Test-phase signals as the structural gap. The ANALYST confirmed the gap constrains the verdict to a demand claim. The SYNTHESIST constrains confidence to 25 — the ceiling — and the verdict is maybe, scoped to demand only."

If any failure mode has fired, revise before producing output.

### Output Instructions

NOT: table format for key evidence ranking — the comparative argument requires prose.

NOT: bullet list format for the synthesis body. Seven prose sections under labeled section headers are required.

Write the synthesis as seven prose sections under these section headers:

**Ceiling Declaration**
State: "Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']."

**Verdict/Confidence**
State yes, no, or maybe in the first sentence. Give the confidence score (0–100), which must not exceed the ceiling in the Ceiling Declaration section. In 2–3 sentences: which Primary signals drove the score up, which phase gap or inertia absence held it down, and — if the ceiling is binding — what the coverage gap means for the verdict's scope.

**Key Evidence**
Name the top 3 signals. For each: one sentence on its finding. One sentence on why it outranks the alternatives — name its phase, role, and inertia classification as part of the argument.

**Counter-Evidence**
State the strongest argument against the verdict. Name the source — a specific signal with its phase, role, and inertia classification from the annotation inventory, a structural gap in Primary signal coverage, or an ADVERSARY challenge that the ANALYST did not fully resolve. If no counter-evidence exists, state: "No counter-evidence found." Omitting this section is not permitted.

**Adoption Boundaries**
State the implications of the inertia coverage state for verdict scope: (1) what the inertia-present signals directly tested — the segments, contexts, or adoption comparisons they covered; (2) what the inertia-absent signals can and cannot establish — demand prediction boundaries versus adoption prediction boundaries; and (3) which contexts the annotation inventory contains no inertia-present signal for, and what that absence means for verdict applicability. If no inertia-present signal is present, state: "No inertia-present signal present. The verdict is a demand claim, not an adoption prediction."

**Principles**
Extract 1–3 generalizable principles. At minimum, one must address what the Primary signal distribution and inertia coverage together imply about this investigation's epistemic boundaries. Declarative form: "X implies Y." Restatements of the verdict are not principles.

**Open Questions**
List 1–3 actionable open questions. For each: the question, which evidence phase/role/inertia would resolve it, and which role raised it.

### Self-Containment Check

Answer each question from its named section; revise if unable.

1. What is the verdict and why is the synthesizer confident at that level? → **Verdict/Confidence section**
2. Which three signals drove the verdict, what are their phase, role, and inertia classifications, and what did each establish that the others did not? → **Key Evidence section**
3. What is the strongest argument against the verdict, including the source signal's phase, role, and inertia classification? → **Counter-Evidence section**
4. What does the inertia coverage state imply for the verdict's scope — which contexts were directly tested, which were not, and where does the adoption prediction hold? → **Adoption Boundaries section**
5. What generalizes beyond this hypothesis, including what the Primary signal distribution and inertia coverage imply? → **Principles section**
6. What remains unresolved, what evidence type and role would resolve it, and which role raised each open question? → **Open Questions section**
7. What was the evidence phase coverage, the Primary signal counts by phase, the inertia coverage state, and what ceiling applied? → **Ceiling Declaration section**

---

## What Made It Golden

**1. Per-signal annotation inventory as a mandatory enumerable intermediate output.**
Phase 1 requires one labeled entry per signal — phase, role, inertia — before any reasoning begins. "Not a coverage summary" is the key constraint: a gestalt impression of the evidence base is disallowed. This creates a structured audit trail that every downstream criterion (ceiling derivation, gate block verification, self-containment check Q7) can point back to by reference, closing the traceability chain through the full output.

**2. Two-dimensional ceiling table with explicit dual-dimension independence constraint.**
Phase 2 derives a hard numerical ceiling from (evidence phase) x (inertia state) intersection. The independence statement — "a larger or higher-quality inertia-absent evidence base cannot exceed the inertia-absent ceiling" — names both volume and quality as separately foreclosed compensatory routes. This forecloses the class of inferences where evidence strength substitutes for inertia coverage, making the ceiling non-negotiable regardless of how many signals exist or how well-designed they are. This single sentence satisfies C-57, C-59, and seeds C-60.

**3. Ceiling Declaration as a structurally mandatory first output section.**
"Do not begin synthesis reasoning until the Ceiling Declaration section appears in your output" converts the ceiling from a rule to a structural anchor. The verdict cannot appear before the ceiling is on record. This sequencing constraint — reinforced by the self-containment check (Q7 → Ceiling Declaration) — means the ceiling is not a post-hoc adjustment but a locked upstream commitment.

**4. Concurrent cognitive roles with per-role dual exemplars in the gate block.**
ADVERSARY, ANALYST, and SYNTHESIST execute with structural dependencies: the ADVERSARY examines the annotation inventory for inventory-specific gaps (not generic challenges), the ANALYST adjudicates before the SYNTHESIST forms a verdict. The gate block provides a negative exemplar (what the failure mode looks like) and a positive exemplar (what non-failure looks like) for each role, co-located. This converts the gate block from a checklist into a discrimination task: the model must actively match its draft against the negative and positive exemplars, not merely acknowledge the rule.

**5. Slot-indexed self-containment check as a mandatory revision gate.**
Seven numbered questions each mapped by arrow notation to a named section. "Revise if unable" is an unconditional instruction, not advisory. The check operates as a closed feedback loop: the output is complete only when every section can answer its verification question. Combined with the "Omitting this section is not permitted" enforcement in Counter-Evidence and the per-role revision mandate in the gate block, the prompt creates three independent revision triggers that activate at different stages of output production.

---

## Final Rubric Criteria Summary (v21 — 220.0 pts max, 60 criteria)

### Essential — C-01 to C-19 (90.0 pts, 4.74 pts each)

| ID | Name | Pass condition |
|----|------|----------------|
| C-01 | Role-annotated signal table | Phase 1 assigns phase/role/inertia labels per signal |
| C-02 | Per-signal verdict assignment | Annotation entries are per-signal, not inferred from overall distribution |
| C-03 | Evidence summary per signal | Phase 1 annotation is a mandatory enumerable per-signal output |
| C-04 | Synthesis verdict present | Verdict/Confidence section states yes/no/maybe |
| C-05 | Confidence level stated | Confidence score (0-100) given in Verdict/Confidence section |
| C-06 | Risk or gap identification | Counter-Evidence and Open Questions sections structurally required |
| C-07 | Recommendation present | Open Questions provides actionable paths; Verdict anchors adoption scope |
| C-08 | Structured output format | 7 named prose sections mandated; bullet lists and tables prohibited |
| C-09 | Signal count stated | Ceiling Declaration states "Primary signals by phase: [count per phase]" |
| C-10 | Conflicting signal acknowledgment | Counter-Evidence cannot be omitted; gate block failure modes cover selective collection |
| C-11 | Lifecycle phase coverage stated | Ceiling Declaration states phases present; Phase 1 labels each signal's phase |
| C-12 | Inertia state addressed | Inertia coverage is a required per-signal label and explicit in Ceiling Declaration |
| C-13 | Scope boundary stated | Dedicated Adoption Boundaries section maps inertia coverage to verdict scope |
| C-14 | No hallucinated signals | Synthesis works from annotation inventory, not invention |
| C-15 | No fabricated evidence | Ceiling derivation read from annotation inventory intersection |
| C-16 | Role separation maintained | Three concurrent cognitive roles; no labeled role sections in output |
| C-17 | Output slots complete | All 7 sections mandated with explicit content requirements |
| C-18 | Annotation inventory present | Phase 1 annotation is a "mandatory enumerable output" — cannot be skipped |
| C-19 | Phase-gated ceiling applied | Phase 2 ceiling derives from annotation inventory intersection; ceiling table present |

### Aspirational — C-20 to C-34 (37.5 pts, 2.5 pts each)

| ID | Name |
|----|------|
| C-20 | Multi-role annotation present — ADVERSARY, ANALYST, SYNTHESIST |
| C-21 | Per-signal role attribution — role label is one of three mandatory annotation dimensions |
| C-22 | Adversarial challenge present — ADVERSARY cognitive role structurally required; gate block confirms non-generic fire |
| C-23 | Synthesist integration present — SYNTHESIST integrates after ADVERSARY + ANALYST; premature integration is named failure mode |
| C-24 | Advocate qualification present — ANALYST adjudicates which gaps are disqualifying, scope-limiting, or open questions only |
| C-25 | Ceiling value stated numerically — "Confidence ceiling: [numeric value, or 'none']" in Ceiling Declaration |
| C-26 | Ceiling rationale stated — Phase 2 derivation from annotation inventory intersection |
| C-27 | Inertia coverage scope mapped — Adoption Boundaries maps inertia coverage to verdict scope |
| C-28 | Lifecycle phase distribution shown — Ceiling Declaration: "Primary signals by phase: [count per phase]" |
| C-29 | Conflicting roles reconciled — ANALYST adjudicates ADVERSARY challenge before SYNTHESIST forms verdict |
| C-30 | Gap prioritization present — Open Questions assigns evidence type, phase, role, attribution per gap |
| C-31 | Revision path stated — Open Questions provides actionable resolution path |
| C-32 | Self-containment check present — 7 verification questions mapped to named sections |
| C-33 | Output closure stated — self-containment check Q7 closes Ceiling Declaration |
| C-34 | Role-to-output traceability present — Open Questions requires "which role raised it" per item |

### Aspirational — C-35 to C-50 (40.0 pts, 2.5 pts each)

| ID | Name |
|----|------|
| C-35 | Concurrent execution + seamless output — three roles execute concurrently; no labeled role sections or visible role seams |
| C-36 | Dual-exemplar adversarial gate — gate block provides negative + positive exemplar for ADVERSARY failure mode |
| C-37 | Slot-indexed self-containment check — each of 7 verification questions mapped to its named section by arrow notation |
| C-38 | Role-to-output closure attribution — Open Questions requires "role that raised it"; self-containment Q6 closes it |
| C-39 | Phase-gated confidence ceiling — ceiling table with phase rows; intersection with inertia state is the derivation mechanism |
| C-40 | Concurrent synthesis gate block — gate block required before output; revision mandated if any failure mode fired |
| C-41 | Slot-indexed revision mandate — Self-Containment Check: "revise if unable" as unconditional instruction |
| C-42 | Ceiling declaration mandatory intermediate output — "Do not begin synthesis reasoning until the Ceiling Declaration appears in your output" |
| C-43 | Gate block per-role dual exemplars — all three roles have co-located negative + positive exemplars |
| C-44 | Per-signal annotated inventory — "individual entry per signal — it is not a coverage summary" |
| C-45 | Two-dimensional ceiling table — 4x2 ceiling table (Evidence phase x Inertia absent/present) |
| C-46 | Annotation-to-ceiling derivation linkage — ceiling read from intersection of highest phase present and inertia coverage state, both from annotation inventory |
| C-47 | Extended declaration coverage in self-containment check — Q7 covers phase coverage, Primary signal counts by phase, inertia state, ceiling value — all mapped to Ceiling Declaration |
| C-48 | Ceiling derivation intersection mechanics — "Any reader who inspects those two values in the annotation inventory and reads the corresponding cell can independently derive the ceiling" |
| C-49 | Dedicated inertia-scope traceability section — Adoption Boundaries is a named dedicated section |
| C-50 | Inertia-absent demand boundary stated — Adoption Boundaries item (2) distinguishes demand prediction from adoption prediction |

### Aspirational — C-51 to C-60 (25.0 pts, 2.5 pts each)

| ID | Name |
|----|------|
| C-51 | Inertia-absent ceiling enforced at synthesis output level — Verdict/Confidence score must not exceed Ceiling Declaration value |
| C-52 | Ceiling Declaration as first named output section — positioned before Verdict/Confidence and all other synthesis sections |
| C-53 | Dimensional independence statement in ceiling computation step — "each independently constrain confidence" in Phase 2 before the table |
| C-54 | C-52 + C-53 simultaneous satisfaction — Ceiling Declaration first AND independence statement in ceiling computation step |
| C-55 | Merged Verdict/Confidence as single ceiling-bound output unit — verdict and score appear in one section with ceiling-binding citation |
| C-56 | C-54 + C-55 simultaneous satisfaction — C-52 + C-53 + C-55 all present |
| C-57 | Explicit compensation foreclosure label in independence statement — names the compensatory inference class being foreclosed ("evidence volume does not compensate for inertia absence") |
| C-58 | C-56 + C-57 simultaneous satisfaction — complete ceiling structural form with explicit compensation foreclosure |
| C-59 | Explicit quality-dimension compensation foreclosure in independence statement — names both "larger" (volume) and "higher-quality" (quality) as co-equal separately foreclosed compensatory routes in the conditional restriction |
| C-60 | C-58 + C-59 simultaneous satisfaction — complete ceiling structural form with dual-dimension explicit compensation foreclosure; closes the language precision chain for the independence statement |

**Max composite**: 220.0 pts (60 criteria) | **Golden threshold**: >= 90 | **V-01 score**: 162.5 (v21 retroactive)
