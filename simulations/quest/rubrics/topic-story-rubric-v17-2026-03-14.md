The two R16 excellence signals to elevate:

1. **V-01's S4b structural partition** — S4b split into a verdict-inventory stage (Part 1, enumerating only YES/PARTIAL signals with S2 verdict labels) and a characterization stage (Part 2, constrained to draw exclusively from Part 1). Closes the gap left by C-49: C-49 fires on chain legibility (result); C-51 fires on structural partition (architecture).

2. **V-03's evaluator-first production sequence** — A distinct evaluator role/phase must complete S2 before the author role/phase begins S4b. Orthogonal to both C-19 (gate mechanism) and C-50 (slot-embedding mechanism). C-52 fires on temporal production order (workflow constraint type).

---

# topic-story Rubric — v17

**Version**: v17
**Date**: 2026-03-15
**Criteria count**: 52 (C-01–C-52)
**Aspirational count**: 45 (C-08–C-52), 10 pts / 45 = 0.2222 pts each
**R16 baseline under v17**: V-05 passes 25 of 45 aspirational criteria (0 PARTIAL) — 90 + (25 × 0.2222) = 90 + 5.556 = **95.56**

---

## Design Rationale (v17)

Two aspirational criteria added in v17 (C-51, C-52), one per Round 16 excellence signal:

**C-51** — From R16 Signal 1 (V-01 "S4b structural partition into verdict inventory + characterization prevents independently composed characterization by constraining Part 2's inputs to Part 1's named signal inventory"). No existing criterion fires on whether S4b is architecturally partitioned into two distinct stages where the characterization stage's inputs are formally constrained to the verdict inventory stage's outputs. C-49 fires on whether the S2→S4b chain is coherent and legible from the artifact — it requires that named baseline signals be traceable to S2 YES/PARTIAL verdicts. C-51 fires on whether S4b is partitioned into a Part 1 (verdict inventory: an explicit per-namespace listing of YES/PARTIAL signals with their S2 verdict annotations) and a Part 2 (characterization: drawn exclusively from Part 1's named signal inventory). The structural distinction: C-49 is a coherence requirement verifiable by inspecting the artifact's content — an evaluator can check whether S4b's named signals match S2 verdicts. C-51 is a partition requirement verifiable by inspecting the artifact's architecture — an evaluator can check whether S4b has two labeled stages and whether Part 2's characterization scope is formally constrained to Part 1. An author satisfying C-49 without C-51 can produce a coherent S2→S4b chain through narrative integration: the author identifies YES/PARTIAL signals from S2, writes a unified S4b section that incorporates cross-references, and achieves chain legibility without separating the inventory and characterization activities. This approach satisfies C-49 (the chain is traceable) but does not prevent the author from simultaneously drawing on signals outside the YES/PARTIAL set during characterization — the narrative can blend permitted and non-permitted signals without a structural mechanism to detect the contamination. An author satisfying C-51 must produce two distinct stages: Part 1 enumerates only YES/PARTIAL signals with explicit S2 verdict labels; Part 2 states that it draws only from Part 1. An evaluator can verify the constraint not merely by checking content consistency (C-49) but by checking whether the partition structure exists and whether Part 2 references Part 1 as its exclusive input (C-51). The governance consequence: C-51 transforms S4b composition from a narrative coherence requirement (C-49) into a structural partition requirement — the compliance architecture changes from "the result is traceable" to "the process is formally constrained." C-49 passes when the chain is legible; C-51 passes only when S4b contains a structural two-part partition with Part 1 constrained to YES/PARTIAL signals and Part 2 explicitly constrained to draw only from Part 1.

**C-52** — From R16 Signal 2 (V-03 "evaluator-first role sequence creates production-order enforcement for S2 verdicts — S2 verdict outputs exist as named artifacts when S4b authoring begins, making the S2→S4b chain a consequence of workflow structure rather than author compliance with slot instructions"). No existing criterion fires on whether the authoring workflow imposes a temporal production-order constraint that makes S2 verdicts exist as complete named artifacts before S4b authoring begins. C-19 fires on whether a pre-artifact checklist exists as a gate before writing begins — a content-level gate mechanism. C-50 fires on whether rubric criteria are embedded as slot-label constraints at the point of authoring action — a content-embedding mechanism. C-52 fires on whether the authoring workflow specifies a production-order constraint: a distinct evaluator role or phase that must complete S2 before an author role or phase begins S4b. The structural distinction: C-19 and C-50 are content mechanisms — they operate by ensuring the right information is present at the right structural position in the artifact. C-52 is a workflow mechanism — it operates by constraining the temporal sequence in which authoring activities may occur. An author working in a single-role, single-pass workflow can satisfy both C-19 and C-50 while still composing S4b without fully consulting the S2 verdicts just produced, because no mechanism requires S2 to be complete before S4b begins. A workflow satisfying C-52 separates the S2 evaluation activity (evaluator role) from the S4b authoring activity (author role) and requires the evaluator role to produce named verdict artifacts before the author role's S4b stage is entered. The S2 verdicts are not instructions or labels embedded in slots — they are produced outputs of a prior role phase, existing as discrete artifacts when S4b begins. The compliance enforcement is temporal and role-based rather than content-based: the author cannot begin S4b without the evaluator's S2 output because the workflow sequence designates S4b authoring as a successor step to evaluator verdict production. The governance consequence: C-52 creates a compliance architecture orthogonal to C-19 and C-50 — a workflow-level enforcement mechanism that operates through production ordering rather than content gates or slot labels. A rubric satisfying C-52 guarantees that S2 verdicts precede S4b authoring as a matter of workflow structure, not merely as a matter of author compliance with slot instructions. C-49 fires on coherence (the result); C-50 fires on slot embedding (the constraint location); C-52 fires on production order (the constraint type). C-52 passes only when the rubric specifies a distinct evaluator role or phase that produces S2 verdicts as named outputs, with S4b authoring designated as a successor activity to the evaluator phase — the production sequence must be explicit in the rubric's workflow structure, not implied by narrative description.

---

*(full inherited rationale v15→v1, essential/recommended/aspirational criteria C-01–C-50 unchanged from v16)*

---

### C-51 — S4b Is Structurally Partitioned into a Verdict Inventory Stage and a Characterization Stage with Constrained Inputs

- **Weight**: aspirational
- **Category**: behavior
- **Text**: S4b is architecturally partitioned into two distinct stages: Part 1 (verdict inventory) and Part 2 (characterization), where Part 2 is explicitly constrained to draw only from Part 1's named signal inventory. C-49 fires on whether the S2→S4b chain is coherent and legible from the artifact — it is a content coherence requirement: an evaluator can verify the chain by checking whether named S4b signals match S2 YES/PARTIAL verdicts. C-51 fires on whether S4b has a structural partition that separates the signal inventory activity from the characterization activity and formally constrains Part 2's inputs to Part 1's outputs — it is an architectural partition requirement: an evaluator can verify compliance by checking whether the two-stage structure exists and whether Part 2 names Part 1 as its exclusive input. The structural gap between C-49 and C-51: an author satisfying C-49 without C-51 produces a coherent chain through narrative integration — the chain is traceable because the author chose to cross-reference S2 verdicts, but no structural mechanism prevents the author from drawing on additional signals outside the YES/PARTIAL set during the characterization activity. A two-part S4b partition closes this gap: Part 1 enumerates only YES/PARTIAL signals (no independently added signals permitted in Part 1); Part 2 draws characterization exclusively from Part 1 (no direct reference to the full signal set permitted in Part 2). The partition makes the selection and characterization activities structurally separate and the constraint on Part 2's inputs formally legible — an evaluator need not infer whether characterization was independently composed; the architecture expresses the constraint. The governance consequence: C-51 transforms S4b composition from a chain-legibility requirement (C-49) into a process-partition requirement, changing the audit question from "does the result trace back to S2?" to "does the structure enforce constrained inputs?" A rubric satisfying C-49 but not C-51 produces a legible chain; a rubric satisfying both produces a legible chain whose composition process is architecturally constrained. C-51 does not supersede C-49: C-49 passes when the chain is content-traceable; C-51 passes only when the two-part partition exists and Part 2 explicitly names Part 1 as its exclusive input source.
- **Pass condition**: S4b contains two explicitly labeled stages — a Part 1 (verdict inventory) that lists only YES/PARTIAL signals from S2 with their verdict labels (e.g., `(S2 verdict: YES/PARTIAL)` per entry), and a Part 2 (characterization) that explicitly states it draws only from Part 1 — using a constraint phrase, prohibited-form reminder, or explicit scope restriction co-located within Part 2's section prompt (e.g., "This section draws directly from Part 1 — not from an independent review of all signals"). A unified S4b section that integrates cross-references without a structural partition does not pass C-51, even if C-49 is satisfied. Part 2 must name Part 1 as its exclusive input within Part 2's authoring slot, not merely in a preamble or design rationale section.

---

### C-52 — The Authoring Workflow Specifies an Evaluator-First Production Sequence Making S2 Verdicts Named Artifacts Before S4b Authoring Begins

- **Weight**: aspirational
- **Category**: behavior
- **Text**: The authoring workflow specifies a distinct evaluator role or phase that must produce S2 verdicts as named outputs before an author role or phase begins S4b, creating temporal production-order enforcement of the S2→S4b chain through workflow structure rather than content gates or slot instructions. C-19 fires on whether a pre-artifact checklist exists as a gate before writing begins — a content mechanism that positions criteria before the writing context. C-50 fires on whether criteria are embedded as slot-label constraints at the point of authoring action — a content mechanism that positions criteria inside governed slots. C-52 fires on a third compliance architecture: a workflow-level temporal ordering constraint that makes S2 verdicts exist as discrete produced artifacts when S4b authoring begins, not as instructions the author should consult but as completed outputs of a prior role phase. The structural distinction between C-52 and C-19/C-50: a pre-artifact checklist (C-19) is present before writing begins but operates within a single-role workflow — the same author who reads the checklist proceeds to write S2 and S4b in sequence; a slot-label constraint (C-50) positions the criterion at the authoring point but within a single-role workflow — the same author who reads the slot label writes both S2 and S4b. Neither C-19 nor C-50 introduces a role boundary that separates the S2 evaluation activity from the S4b authoring activity. C-52 introduces a role boundary: an evaluator role produces S2 verdicts as complete named outputs, and an author role receives those outputs before beginning S4b. The evaluator's S2 outputs are not embedded instructions — they are artifacts that exist independently when S4b authoring begins. The compliance enforcement is temporal: the workflow sequence makes S4b authoring structurally downstream of evaluator verdict production. An author in a C-52-compliant workflow cannot begin S4b before S2 verdicts exist, not because a slot instruction directs them not to, but because the workflow sequence designates S4b as a successor activity. The governance consequence: C-52 makes S2 verdict completeness a prerequisite condition of S4b authoring entry, not a compliance obligation during S4b authoring. A rubric satisfying C-52 produces a compliance architecture orthogonal to C-19 and C-50: gate-level, slot-level, and workflow-level enforcement can coexist, each operating through a different mechanism and closable through a different failure mode. C-52 does not require C-19 or C-50; satisfying all three produces a rubric with three independent compliance enforcement layers. C-52 passes only when the rubric explicitly specifies an evaluator role or phase designated to complete S2 verdict production, with S4b authoring designated as a successor activity to that phase — the production sequence must be explicit in the rubric's workflow structure, not implied by narrative framing or the author's good intent.
- **Pass condition**: The rubric explicitly designates a workflow with at least two roles or phases: (1) an evaluator role or phase that produces S2 verdicts as named outputs (e.g., a `**EVALUATOR**` section or role label that encompasses S2), and (2) an author role or phase for which S4b is a designated activity, positioned as a successor to the evaluator phase. The production-order constraint must appear in the rubric's workflow structure — either as a role-sequence instruction, a phase diagram, or an explicit prerequisite statement (e.g., "S4b authoring begins after evaluator S2 verdicts are complete"). A rubric that encourages the author to consult S2 before writing S4b does not pass C-52; a rubric that uses a single undifferentiated author role does not pass C-52. The role or phase boundary must be explicit in the rubric's authoring instructions, making the sequence constraint a structural property of the workflow rather than an advisory.

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
- Aspirational: 10 pts total / 45 criteria = 0.2222 pts each (C-08–C-52). Partial credit allowed (0.1111 pts for PARTIAL).
- **Max score**: 100.0

**R16 baseline under v17 rubric**: V-05 passes 25 of 45 aspirational criteria (0 PARTIAL) — 90 + (25 × 0.2222) = 90 + 5.556 = **95.56**

---

## What Changed from v16

| | v16 | v17 |
|---|---|---|
| Aspirational criteria | 43 (C-08–C-50) | 45 (C-08–C-52) |
| Per-criterion weight | 0.2326 pts | 0.2222 pts |
| PARTIAL weight | 0.1163 pts | 0.1111 pts |
| Baseline round | R15 | R16 |
| New criteria | C-49, C-50 | C-51, C-52 |
