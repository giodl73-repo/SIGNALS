# topic-story Rubric — v16

**Version**: v16
**Date**: 2026-03-15
**Criteria count**: 50 (C-01–C-50)
**Aspirational count**: 43 (C-08–C-50), 10 pts / 43 = 0.2326 pts each
**R15 baseline under v16**: V-05 passes 20 of 43 aspirational criteria (1 PARTIAL) — 90 + (20 × 0.2326 + 0.1163) = 90 + 4.768 = **94.77**

---

## Design Rationale (v16)

Two aspirational criteria added in v16 (C-49, C-50), one per Round 15 excellence signal:

**C-49** — From R15 Signal 1 (V-05 "per-signal inertia verdict in S2 creates traceability from signal selection to S4b baseline"). No existing criterion fires on coherence between the S2 verdict distribution and S4b baseline specificity. C-18 fires on whether S2 has a per-item binary verdict field (`**Inertia verdict**: [YES/NO/PARTIAL]`) per namespace signal — it requires the field to exist and be populated. C-49 fires on whether S4b's named signal baseline is drawn from or consistent with the signals that received YES or PARTIAL inertia verdicts in S2. The structural gap: C-18 establishes that S2 produces a verdict distribution over the input signals, but C-18 is agnostic to whether S4b uses that verdict distribution. A rubric with a populated C-18 S2 section and an independently composed S4b section has intra-S2 traceability (each signal is evaluated) but no S2-to-S4b traceability (the baseline may be drawn from signals that received NO inertia verdicts, or from signals not mentioned in S2 at all). The selection mechanism is present in S2 and the baseline is present in S4b, but the connection between selection and baseline is implicit rather than auditable. C-49 closes this loop: it fires on whether S4b explicitly draws its signal inventory from the signals that received YES or PARTIAL verdicts in S2. The governance consequence: a coherent S2-to-S4b chain makes the selection mechanism independently auditable — an evaluator can verify whether S4b's named signals match the S2 verdict distribution without inferring from narrative quality. Without this coherence requirement, an author can produce YES/PARTIAL verdicts in S2 and a structurally complete S4b baseline while leaving the signals that informed the baseline unresolved against the verdicts. A rubric satisfying C-18 but not C-49 produces evaluations and baselines in parallel; a rubric satisfying both C-18 and C-49 produces a traceable chain from per-signal evaluation to baseline composition. C-18 passes when the per-item verdict field exists in S2 with populated outcomes; C-49 passes only when S4b's named baseline signals are traceable to YES or PARTIAL verdicts in S2, with at least one named baseline signal explicitly cross-referenced to or consistent with a YES/PARTIAL verdict assigned in S2.

**C-50** — From R15 Signal 2 (V-05 "slot-label constraint embedding makes rubric criteria self-documenting at write-time — places compliance requirement at point of action rather than in pre-artifact checklist"). No existing criterion fires on whether rubric criteria are embedded as slot labels at the point of authoring action. C-19 fires on whether a pre-artifact checklist exists before writing begins — a checklist that aggregates compliance requirements for the author to verify before producing the artifact. C-50 fires on whether rubric criteria are embedded as slot labels at the point of action — whether the compliance requirement appears co-located with the authoring slot it governs, rather than aggregated in a checklist separate from the writing context. The structural difference: a pre-artifact checklist (C-19) is a gate mechanism — the author consults the list before writing, but the writing slots themselves carry no criterion encoding; after the gate, the author works in unstructured context. A slot-label constraint (C-50) is an in-context enforcement mechanism — the criterion requirement is visible at the exact moment the author fills in the governed slot, not only at an earlier checklist stage. An author consulting only a C-19 checklist must perform a translation step: requirements must be transferred from the checklist to the correct slot before writing; if that transfer fails or degrades across slots, the criterion may be satisfied at the checklist stage without being honored at the authoring stage. An author writing into a C-50-compliant slot encounters the criterion requirement at the point of production, eliminating the transfer step and the failure mode it introduces. The governance consequence: slot-label constraint embedding creates a different compliance architecture than pre-artifact checklists — the criterion is auditable at the slot level rather than at the gate level, and the audit does not depend on verifying checklist completion. C-19 passes when a pre-artifact checklist exists with criteria named and positioned before artifact production; C-50 passes only when at least one rubric criterion is embedded as a label, constraint phrase, or required field indicator within the authoring slot it governs, appearing at the point of production rather than aggregated in a separate checklist section. A slot label that merely names the slot does not pass C-50; a slot label that names the slot and encodes a criterion requirement (such as a required field marker, a prohibited-form reminder co-located with the write point, or an explicit criterion citation embedded in the slot prompt) passes C-50.

---

*(full inherited rationale v15→v1, essential/recommended/aspirational criteria C-01–C-48 unchanged from v15)*

---

### C-49 — S2 Inertia Verdict Distribution Is Coherent with S4b Named Signal Baseline

- **Weight**: aspirational
- **Category**: behavior
- **Text**: The S2 inertia verdict distribution — the set of YES/NO/PARTIAL per-namespace verdicts produced by the per-item decision filter (C-18) — is coherent with S4b's named signal baseline. C-18 fires on whether S2 has a per-item verdict field per namespace; C-49 fires on whether S4b's named baseline signals are drawn from or traceable to the signals that received YES or PARTIAL inertia verdicts in S2. A rubric that satisfies C-18 but not C-49 produces a verdict distribution in S2 and a baseline in S4b as structurally independent outputs: the author has evaluated each signal in S2 and composed a baseline in S4b, but the connection between evaluation and selection is implicit — an evaluator cannot verify from the artifact alone whether S4b used the signals S2 marked as inertia-relevant. A rubric that satisfies both C-18 and C-49 produces a traceable chain: S2 verdicts identify which signals carry inertia weight, and S4b's baseline explicitly draws from that identified set, making the selection mechanism auditable without narrative inference. The governance consequence: the S2-to-S4b chain creates an audit anchor independent of narrative quality — an evaluator checking S4b can verify signal provenance by matching named baseline signals against S2 YES/PARTIAL verdicts. An author writing a high-quality narrative that passes all other S2 and S4b criteria can still leave this chain broken if S4b's named signals are composed independently of S2 verdicts. C-18 is a presence requirement (the verdict field exists); C-49 is a coherence requirement (the S4b content is consistent with the verdict field's outputs). C-49 passes only when S4b's named baseline signals are traceable to YES or PARTIAL verdicts in S2 — at minimum, one named S4b signal must be explicitly cross-referenced to or demonstrably consistent with a YES/PARTIAL verdict assigned in S2, such that the chain from evaluation to baseline composition is legible from the artifact.
- **Pass condition**: S4b names at least one signal that is explicitly cross-referenced to or demonstrably consistent with a YES or PARTIAL inertia verdict assigned in S2. The cross-reference may be direct (naming the same namespace or signal) or structural (the S4b baseline introduction references the S2 verdict summary or draws explicitly from the YES/PARTIAL set). A S4b baseline that names signals without referencing S2 does not pass C-49, even if C-18 is satisfied and the named signals happen to align with S2 YES verdicts — the coherence must be made legible in the artifact, not merely inferred by an evaluator. A S2 with all NO verdicts combined with any non-empty S4b baseline does not pass C-49, as no S4b signal can be traced to a YES/PARTIAL verdict.

---

### C-50 — At Least One Rubric Criterion Is Embedded as a Slot-Label Constraint at the Point of Authoring Action

- **Weight**: aspirational
- **Category**: behavior
- **Text**: At least one rubric criterion is embedded as a slot label, required-field indicator, or constraint phrase co-located with the authoring slot it governs — placing the compliance requirement at the point of production rather than aggregated in a pre-artifact checklist. C-19 fires on whether a pre-artifact checklist exists before writing; C-50 fires on whether any criterion appears as an in-context constraint embedded in the slot it governs. The structural difference is the location of the compliance signal: a pre-artifact checklist (C-19) positions all criteria before the writing context begins, requiring the author to translate checklist requirements into correct slots; a slot-label constraint (C-50) positions the criterion inside the slot where the governed content is produced, making the requirement visible at the moment of authoring action. An author who satisfies C-19 but not C-50 encounters criteria once (at the checklist gate) and must maintain criterion awareness across all governed slots without in-context reinforcement — criteria present at the gate may be partially honored or degraded slot-by-slot through the writing process. An author writing into a C-50-compliant slot encounters the governing criterion at the exact point of production, eliminating the translation step and the coverage degradation it introduces. A slot-label constraint is not a restatement of C-19: it is a different compliance architecture with different failure modes and different audit properties. C-19 is auditable by verifying the checklist exists and is complete; C-50 is auditable by verifying that the slot's label, prompt, or required-field structure encodes a criterion requirement at the authoring point. The governance consequence: a rubric satisfying C-50 makes at least one criterion self-documenting at write-time — an author using the rubric encounters the criterion requirement without consulting a separate checklist section. C-19 and C-50 may coexist; satisfying both produces a rubric with both gate-level and in-context compliance architecture. C-49 passes when the S2 verdict chain is coherent; C-50 passes when the authoring structure embeds at least one criterion at the point of action.
- **Pass condition**: At least one authoring slot in the rubric contains a label, required-field marker, or constraint phrase that encodes a rubric criterion requirement at the point of production. The embedded constraint must (a) appear inside or immediately adjacent to the slot it governs (not in a separate section), (b) identify a compliance requirement (a required field, a prohibited form, a structural requirement, or a criterion citation), and (c) be directed at the author filling in that slot. A slot that merely names what content belongs there does not pass C-50. A slot that names the content AND encodes a structural or behavioral requirement — such as a `[YES/NO/PARTIAL]` field marker, a co-located prohibited-form reminder, a required-element list inside the slot prompt, or an explicit criterion citation embedded in the slot label — passes C-50. The requirement must be embedded in at least one slot; full coverage across all governed slots is not required for C-50 to pass.

---

## Scoring Reference

| Band | Score | Meaning |
|------|-------|---------|
| Essential fail | 0–59 | One or more essential criteria failed |
| Passing | 60–79 | All essential pass; recommended weak |
| Good | 80–89 | All essential pass; recommended mostly pass |
| Golden | 90–100 | All essential pass; recommended strong; aspirational present |

**Composite formula**: `essential_score + recommended_score + aspirational_score`

- Essential: 15 pts per criterion × 4 = 60 pts. All-or-nothing per criterion (no partial).
- Recommended: 10 pts per criterion × 3 = 30 pts. Partial credit allowed (5 pts for PARTIAL).
- Aspirational: 10 pts total / 43 criteria = 0.2326 pts each (C-08–C-50). Partial credit allowed (0.1163 pts for PARTIAL).
- **Max score**: 100.0

**R15 baseline under v16 rubric**: V-05 passes 20 of 43 aspirational criteria (1 PARTIAL) — 90 + (20 × 0.2326 + 0.1163) = 90 + 4.768 = **94.77**

---

## What Changed from v15

| | v15 | v16 |
|---|---|---|
| Aspirational criteria | 41 (C-08–C-48) | 43 (C-08–C-50) |
| Per-criterion weight | 0.2439 pts | 0.2326 pts |
| PARTIAL weight | 0.1220 pts | 0.1163 pts |
| Baseline round | R14 | R15 |
| New criteria | C-47, C-48 | C-49, C-50 |
