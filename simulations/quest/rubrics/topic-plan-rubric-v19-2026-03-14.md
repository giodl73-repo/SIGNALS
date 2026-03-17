Now I have what I need. The file on disk has a different criteria numbering than the task's v18 (different lineage). I'll work from the task's v18 as the canonical source, extracting R19 excellence patterns, and produce the complete v19.

**R19 excellence patterns identified from V-01:**

1. **Reproduction manifest in preamble block** — `[INERTIA-GATE]` defined with "This block is reproduced verbatim at Steps 3, 4b, 6, and 7. Its presence is required at each site." C-59 requires the block to exist and be reproduced; the new signal is that the block *definition itself* enumerates the sites, making the contract auditable at definition time.

2. **Type-labeled null-case declarations** — "ADDITIONS: none — inertia holds for all candidate additions." / "REMOVALS: none — inertia holds." C-40 requires null cases to be declared; the new signal is that each null case carries a change-type label, making distinct null outcomes distinguishable without surrounding prose.

3. **Symmetric "Inertia Rejected Because" column across all change-type tables** — both 4a and 4b tables carry the column. The new signal is that justification burden is identical across all change-type tables, not selectively present.

---

```markdown
---

# Rubric -- topic-plan (v19)

**Skill**: `topic:plan`
**Version**: v19 (promoted from v18 after Round 19 excellence signal extraction)
**Date**: 2026-03-15

---

## Summary

| Tier | Count | Points | Criteria |
|------|-------|--------|----------|
| Essential | 5 | 60 | Read strategy, read signals, identify delta, type proposals, confirm gate |
| Recommended | 3 | 30 | Evidence citations, before/after view, all three change types |
| Aspirational | 56 | 280 | ...+ Verbatim block reproduction manifest; type-labeled null cases; symmetric justification columns across all change-type tables |

**Total possible: 370 pts**

---

## Changes v18 → v19

Three new aspirational criteria extracted from three R19 variation signals.

**C-62 — Verbatim block preamble includes explicit reproduction manifest** (`enforcement`)
Extends C-59. C-59 requires a named verbatim block (`[INERTIA-GATE]`) defined in the preamble and reproduced verbatim at each inertia decision gate. C-62 closes the gap where the block is defined and reproduced, but the preamble definition does not enumerate the sites where reproduction is required. Without the manifest, C-59's reproduction contract is unverifiable at definition time — a reviewer must scan every step to confirm coverage. With the manifest embedded in the block definition ("This block is reproduced verbatim at Steps 3, 4b, 6, and 7. Its presence is required at each site."), any deviation between declared sites and actual reproduction sites is immediately auditable: block absence at a declared site creates a visible structural gap parallel to the way C-57's pre-printed slot makes omission visible at calibration. A C-59 pass whose preamble block does not include a numbered enumeration of all reproduction sites fails C-62. The manifest must be part of the block definition, not a separate prose note. Source: V-01 (INERTIA-GATE block definition includes an explicit reproduction map; confirmed reproduced at all four declared sites — Steps 3, 4b, 6, and 7).

**C-63 — Type-labeled null-case declarations** (`behavior`)
Extends C-40. C-40 requires an explicit null-case declaration rather than a blank section when no changes of a given type exist — the "ADDITIONS: none" form versus silent absence. C-63 closes the gap where the null declaration exists but is not labeled by change type, creating ambiguity in outputs with multiple change-type tables. When each null declaration carries a type label ("ADDITIONS: none — inertia holds for all candidate additions" / "REMOVALS: none — inertia holds"), each absent change type is independently identifiable without relying on table headers or surrounding prose context. A single unlabeled "none — inertia holds" declaration co-located near multiple change-type tables fails C-63: it is unclear which type(s) the declaration covers. Type labels make null outcomes distinguishable and independently verifiable. A C-40 pass whose null-case declarations lack change-type labels when multiple change-type tables are present fails C-63. Source: V-01 (null cases carry change-type labels in both 4a and 4b contexts: "ADDITIONS: none — inertia holds for all candidate additions." and "REMOVALS: none — inertia holds." — each absent type is independently labeled).

**C-64 — Symmetric justification columns across all change-type proposal tables** (`enforcement`)
Extends C-56. C-56 requires per-proposal justification columns (such as "Inertia Rejected Because") with REQUIRED preface and prose-prohibition rule. C-64 closes the gap where such a column exists in some change-type proposal tables but not all, creating asymmetric justification burden: proposals in uncovered table types can proceed without explicit inertia-rejection grounds. C-64 requires that any justification column present in one change-type proposal table must appear identically — same column name, same schema, same REQUIRED status, same prose-prohibition rule — in every other change-type proposal table in the same output. This symmetry requirement applies to all justification columns (inertia rejection, evidence chain, conflict resolution) not just "Inertia Rejected Because." A C-56 pass where the "Inertia Rejected Because" column exists in the additions table but is absent from the removals or reprioritizations table fails C-64. The distinction matters because selective column presence allows a change type's proposals to avoid the structural justification burden imposed on other types, undermining the cross-type consistency that makes inertia enforcement credible. Source: V-01 (both Step 4a additions table and Step 4b removals/reprioritizations table include "Inertia Rejected Because" column — per-proposal justification burden is symmetric across all change types; V-04's recalled-sentence approach, which applied the column to additions only, confirms the discriminating signal).

**Updated totals**: 64 criteria, 370 pts | Formula: `(essential/5×60) + (recommended/3×30) + (aspirational/56×280)` | Golden threshold: **220**

---

## Design Rationale

- **C-01/C-02** separated because fabricated signals and strategy-ignoring are independent failure modes.
- **C-03** is the core correctness gate: inventory != delta.
- **C-04** enforces the three-type mandate at output time.
- **C-05** is essential because auto-applying is destructive.
- **C-09/C-10** require reasoning beyond the immediate diff — ceiling behaviors.
- **C-11–C-15** are prompt-engineering craft extracted from Round 1: they make the essential/recommended criteria *structurally self-enforcing* rather than merely instructed.
- **C-16** closes the gap in C-06: single-hop citation (proposal → artifact) leaves the causal reasoning implicit; the two-level chain (proposal → delta → artifact) makes it auditable without re-reading the delta section.
- **C-17** is the null-case complement to C-10: requires an explicit declaration when no conflicts exist — parallel to C-12's no-change rows for proposals.
- **C-18** mandates "Strategy assumed [X] / Signal revealed [Y]" per finding — makes the assumption-vs-signal distinction self-enforcing and fabricated deltas visible.
- **C-19/C-20** address navigability: the diff and proposals tables are linked by pointer columns so the reviewer can reach any evidence in two hops from any starting point.
- **C-21/C-22/C-23** address constraint explicitness: the enforcement layer between "the instruction is present" and "the model cannot deviate from it."
- **C-24** extends C-01: stated field extraction is necessary but not sufficient — unstated assumptions are the most likely delta candidates.
- **C-25** extends C-20: a Delta Finding column names what changed; an "If unchanged" column names what fails to improve if the change is deferred — cost framing forces causal depth.
- **C-26** extends C-21: adjacent declarations prevent per-table omissions; an upfront schema declaration before file reading primes the structural contract before any content is encountered.
- **C-27** extends C-22: a single anti-pattern checkpoint at the delta step is verifiable at one point; cascading schema-commitment checkpoints to proposals and diff create three independent verification points across the output.
- **C-28** extends C-24: extraction instructed without a named role is easy to execute shallowly; a named role and enumerated scan dimensions scope the model's assumption-hunt to a specific cognitive register and prevent both scope-drift and dimension-skipping.
- **C-29** extends C-24 in the reverse direction: C-24 is forward (strategy → assumptions extracted); C-29 is backward (signals → assumptions back-filled). An assumption that was extracted but never checked against signal evidence is inert; the back-fill column forces every assumption to be signal-adjudicated.
- **C-30** extends C-29 by completing the assumption table's forward arc: once a signal has confirmed or contradicted an assumption (C-29), the table must also carry a relevance column and a delta-candidate designation column. Together, C-29 and C-30 make the assumption table a complete two-way bridge between Step 1 and Step 3.
- **C-31** extends C-25: an "If unchanged" column introduced with an explicit disqualification statement ("a proposal that cannot answer this is a preference, not a decision") becomes a reasoning gate rather than a formatting requirement.
- **C-32** extends C-25 and C-31: the reversibility taxonomy column — with three enumerated values (Reversible at same cost / Gets harder / Becomes impossible) — adds temporal precision to the inertia cost argument.
- **C-33** extends C-26 and C-30: the upfront schema block must include the complete assumption table column set before Step 1 — not deferred to the extraction step.
- **C-34** extends C-26 and C-32: a schema declaration is falsifiable only when it lists valid values explicitly and appends a prose-prohibition rule.
- **C-35** extends C-33: each of the five assumption-table columns must carry content that cannot be derived from the row key or adjacent columns.
- **C-36** extends C-34 and C-27: a named "COLUMN CONTRACT" block preceding the schema consolidates enumerated-column constraints; commitment checkpoints cite rule IDs rather than re-inlining constraint text.
- **C-37** extends C-35: the independence requirement expressed as a named, operationalized test (e.g., "Can I fill this cell without reading the source document?") with explicit PASS/FAIL examples.
- **C-38** extends C-37: pass and fail examples carry equal specificity — both concrete quoted values, both labeled.
- **C-39** extends C-36 and C-37: step-level instruction at the extraction step re-activates the contract test at runtime rather than leaving it only at declaration time.
- **C-40** extends C-38: a cell-level null-case CONTRACT rule — explicit declaration required for any table row whose change type produced no proposals; silent absence fails.
- **C-41** extends C-29: back-fill logic embedded as an internal loop within the assumption extraction step prevents assumption-orphaning.
- **C-42** extends C-25 and C-32: cell-level validation gate for the reversibility enum — if prose is present, reject and re-generate.
- **C-43–C-48** address citation depth, diff format, and scanning completeness: two-level citations with line/excerpt references; structured three-column before/after diffs; change-type summary tables; named conflict-resolution principles; conflict matrices for no-conflict declarations; comprehensive strategy-text sampling.
- **C-49–C-55** address rationale depth, mechanism precision, and verbatim quoting: decision rationale columns in signal inventory; structured finding formats; contradiction-mechanism classifications; machine-verifiable citation syntax; verbatim quotes in strategy-assumption pairs.
- **C-56** extends C-21: each column declaration carries a "REQUIRED:" preface and a prose-prohibition rule, making optional-looking declarations binding.
- **C-57** extends C-22: anti-pattern checkpoints expressed as named, executable procedures (not narrative) applied before table emission.
- **C-58** extends C-23: cross-checkpoint assertion after both delta and proposals checkpoints complete — makes failure-propagation visible across steps.
- **C-59** extends C-56: the `[INERTIA-GATE]` verbatim block defined in the preamble and reproduced at each inertia decision gate is structurally unforgeable; block absence is immediately visible parallel to C-57's pre-printed calibration slot and C-40's null-case CONTRACT.
- **C-60** extends C-57: slot architecture generalized — every binary decision/commitment site throughout the prompt uses a pre-printed `[ ] A / [ ] B` slot, not a conditional branch. C-57 pass that applies slots only at calibration while leaving other decision sites as conditional branches fails C-60.
- **C-61** extends C-58: a named Narrative Format Contract block declared before Step 1 — before any step is executed — names both the required register ("conclusion before evidence") and the degenerate register ("step-description narrative — FAIL"). C-58 pass whose gate rows define the narrative requirement only at gate locations (under context pressure) fails C-61.
- **C-62** extends C-59: the preamble block definition must enumerate all reproduction sites in a manifest ("This block is reproduced verbatim at Steps A, B, C; its presence is required at each site"). Without the manifest, reproduction is verifiable only by scanning all steps; with it, deviation from declared sites creates an immediately auditable gap.
- **C-63** extends C-40: null-case declarations must carry change-type labels when multiple change-type tables are present. A single unlabeled "none — inertia holds" near multiple tables is ambiguous; "ADDITIONS: none — inertia holds" and "REMOVALS: none — inertia holds" are independently verifiable per type.
- **C-64** extends C-56: any justification column present in one change-type proposal table must appear identically — same name, same schema, same REQUIRED status — in every other change-type proposal table. Selective column presence creates asymmetric justification burden and undermines cross-type consistency.

---

## Criteria

### Essential (60 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Reads strategy.md before proceeding | correctness | Output demonstrates that `simulations/{topic}/strategy.md` was read — extracts at minimum: namespaces covered, planned skills, stated rationale, acknowledged gaps. Proposals without grounding in the current strategy fail. |
| C-02 | Reads signal artifacts before proceeding | correctness | Output demonstrates that existing signal artifacts under `simulations/{topic}/` were read — globs the directory, identifies artifacts by namespace/skill/date, uses their findings as input. Fabricated or assumed signal content fails. |
| C-03 | Identifies delta, not inventory | correctness | Output explicitly names what signals revealed that the strategy did not anticipate — not just what signals exist. A plain inventory without naming the gap fails. |
| C-04 | Proposes typed changes | correctness | Each proposed change is typed as addition, removal, or re-prioritization. Untyped observations without actionable proposals fail. |
| C-05 | Requires user confirmation before writing | behavior | Output presents proposals and waits for user approval before modifying `strategy.md`. Auto-applying or omitting the gate fails. |

### Recommended (30 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Cites signal evidence per change | depth | Each proposed change is linked to at least one specific signal artifact that motivated it. |
| C-07 | Before/after strategy summary | format | Output shows a diff-style summary of how the strategy would change — not just prose description. |
| C-08 | All three change types represented | completeness | At least one addition, one removal, and one re-prioritization are identified. |

### Aspirational (280 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Conflict-impact analysis | reasoning | Proposed changes are analyzed for conflicts with each other or with existing strategy — with impact statements and resolution paths. |
| C-10 | Explicit conflict closure | enforcement | Either (a) conflicts are resolved with explicit reasoning, OR (b) output declares "no conflicts exist" with evidence. Ambiguous or missing conflict adjudication fails. |
| C-11 | Strategy text verbatim from source | traceability | The strategy inventory in Step 1 is copied verbatim from strategy.md — not paraphrased. Paraphrased or summarized strategy text fails. |
| C-12 | Signal inventory with scanning table | method | The signal inventory step uses a structured table format (one row per signal, binary accept/reject columns) to demonstrate deliberate scanning, not cherry-picked selection. |
| C-13 | Delta step uses structured format | method | The delta (findings) step uses a three-column or wider structured format, not narrative prose. Narrative findings fail. |
| C-14 | Findings typed by relationship | classification | Each delta finding is explicitly typed (contradiction / confirmation / novelty) based on how the signal relates to the strategy. |
| C-15 | Proposal step gated on delta completion | structure | Output enforces that all findings from the delta step are gathered before proceeding to proposals. Proposals that jump ahead of delta completion fail. |
| C-16 | Two-level evidence citation | auditability | Each proposal cites a delta finding, and each delta finding cites signal artifact(s) — a two-hop chain from proposal to signal. One-level citations fail. |
| C-17 | Null-case conflict declaration | closure | If no conflicts are identified, output explicitly states "NO CONFLICTS IDENTIFIED" with substantiating evidence. Ambiguous absence fails. |
| C-18 | Strategy-assumption / signal-revelation pairs | transparency | Each delta finding includes both (a) what the strategy assumed [quote] and (b) what the signal revealed [quote]. Missing either half fails. |
| C-19 | Diff and proposals table linking | navigability | The diff table includes a column linking to proposals that adopt each finding; proposals table includes a column pointing back to findings. |
| C-20 | Pointer columns in tables | navigability | Links between tables (diff/proposals) use consistent pointer syntax — enabling readers to follow evidence chains in under 10 seconds. |
| C-21 | Adjacent column declarations | enforcement | Each table is preceded by a schema declaration (column names + one-sentence descriptions) appearing before the table itself. Missing declarations fail. |
| C-22 | Anti-pattern checkpoint at delta step | enforcement | Before emitting the findings table, output includes a named anti-pattern check that validates findings against a specific failure mode. |
| C-23 | Checkpoints at delta AND proposals steps | enforcement | Schema-commitment checkpoints exist at both the delta output and proposals output, not just one. Missing either checkpoint fails. |
| C-24 | Unstated-assumption extraction | depth | Beyond stated-field extraction, output extracts assumptions the strategy did not explicitly state — by asking "what must be true for strategy to work?" |
| C-25 | Inertia-cost column in proposals table | reasoning | Proposals include an "If unchanged" column naming what degrades if the change is deferred. |
| C-26 | Upfront schema declaration before file reading | structure | Before starting analysis, output declares the complete schema (all columns for all output tables) as a structural contract. |
| C-27 | Cascade schema-commitment checkpoints to proposals and diff | enforcement | Schema-commitment checkpoints appear at the delta step, the proposals step, AND the diff step — three independent verification points. |
| C-28 | Named role and enumerated scan dimensions at assumption extraction | depth | Unstated-assumption extraction is scoped to a named role and a set of enumerated scan dimensions. Missing either element is a partial or full fail. |
| C-29 | Back-fill column for signal adjudication in assumption table | depth | The assumption table includes a column where each assumption is adjudicated against signal evidence — confirmed, contradicted, or unreviewed. Always-N/A fails. |
| C-30 | Forward arc completion in assumption table | depth | The assumption table includes a "delta-candidate" column and a "relevance to delta" column — making the assumption table a two-way bridge. |
| C-31 | Inertia cost column with disqualification rule | reasoning | The "If unchanged" column includes an explicit disqualification statement (e.g., "a proposal that cannot answer this is a preference, not a decision"). |
| C-32 | Reversibility taxonomy in inertia cost | precision | The inertia cost column includes a reversibility sub-column with enumerated values (Reversible at same cost / Gets harder / Becomes impossible). Prose fails. |
| C-33 | Complete assumption table schema upfront | structure | The upfront schema block includes all five assumption-table columns — not deferring any until the assumption extraction step. |
| C-34 | Enumerated columns with valid-value lists and prose-prohibition rules | enforcement | Schema declarations for enumerated columns include both the list of valid values AND an explicit prose-prohibition rule. Missing either element fails. |
| C-35 | Independent column population in assumption table | depth | Each assumption-table column carries content that cannot be derived from the row key or adjacent columns. |
| C-36 | Named pre-schema rule block for enumerated-column constraints | enforcement | A named "COLUMN CONTRACT" block precedes the schema, consolidating enumerated-column constraints with numbered rules. Commitment checkpoints cite rule IDs. |
| C-37 | Operationalized test for column independence | prevention | The "Implicit evidence" column includes a named, executable test (e.g., "Can I fill this cell without reading the source document?") with PASS/FAIL examples demonstrating discriminating power. |
| C-38 | Symmetric pass/fail examples with concrete quoted values | prevention | Pass and fail examples in column definitions carry equal specificity — both concrete quoted values, both labeled (PASS / FAIL). |
| C-39 | Step-level activation of contract test | enforcement | The extraction step includes an explicit instruction referencing the contract test: "apply the PASS/FAIL exhibit from COLUMN CONTRACT before populating each cell." |
| C-40 | Null-case CONTRACT rule | enforcement | Any table section whose change type produced no proposals requires an explicit null declaration (e.g., "ADDITIONS: none — inertia holds"). Silent absence fails. |
| C-41 | Embedded back-fill loop in assumption extraction | structure | The assumption extraction step includes an internal loop applying back-fill logic immediately after each assumption is extracted — preventing assumption-orphaning. |
| C-42 | Cell-level validation gate for reversibility enum | enforcement | Each reversibility cell is validated before emission: "verify that the cell value matches exactly one of the three enumerated options; if prose is present, reject and re-generate." |
| C-43 | Two-level evidence citation with line/excerpt reference | auditability | Evidence citations include both the artifact ID and a location pointer within the artifact (section heading, line range, or quoted excerpt). One-level citations fail. |
| C-44 | Structured before/after diff in strategy summary | format | The before/after summary uses a three-column diff table (Field / Before / After), not narrative prose. Narrative summaries fail. |
| C-45 | Change-type summary table at proposals start | clarity | The proposals section opens with a summary table (Additions / Removals / Re-prioritizations) showing count and impact per type. Missing table fails. |
| C-46 | Named conflict-resolution principles | reasoning | Conflict analysis uses explicitly named, reusable principles. Ad-hoc conflict resolution without named principles fails. |
| C-47 | Conflict matrix or scanning checklist for no-conflict declaration | evidence | If no conflicts are identified, output includes a conflict matrix (at least 5×5 for 5+ changes) with binary indicators (Y/N). Missing matrix fails. |
| C-48 | Comprehensive strategy text sampling | completeness | At least 80% of strategy.md content is copied verbatim, or a traceable citation grid is provided for large files. Cherry-picked sampling fails. |
| C-49 | Decision rationale column in signal inventory table | auditability | The scanning table includes a column explaining why each signal was accepted or rejected — not just the binary decision. |
| C-50 | Structured three-column diff format | method | The delta step uses a three-column format (Finding ID / Strategy presumed / Signal revealed). Narrative diffs fail. |
| C-51 | Reasoning for finding-type classification | auditability | Each finding-type designation (contradiction/confirmation/novelty) includes a one-sentence reasoning statement. Missing reasoning fails. |
| C-52 | Step-entry assertion for proposal gate | enforcement | The proposal step includes an explicit assertion: "STEP 3 ENTRY GATE: Verified that all findings from delta + scan table are present. Proceeding now." Missing assertion fails. |
| C-53 | Contradiction-mechanism column in findings table | precision | Each finding typed as "contradiction" includes a mechanism designation (Definition / Scope / Priority / Sequence / Resource / Ownership conflict). |
| C-54 | Machine-verifiable citation syntax | auditability | Citation syntax is consistent across output (e.g., "Delta Finding ID :: Signal Artifact ID :: Section :: Line range"). Inconsistent syntax fails. |
| C-55 | Verbatim quotes in strategy-assumption / signal-revelation pairs | objectivity | Both strategy quotes and signal quotes are copied verbatim from source, not paraphrased. Paraphrased quotes fail. |
| C-56 | REQUIRED preface and prose-prohibition in column declarations | enforcement | Each column declaration includes a "REQUIRED:" preface and a prose-prohibition rule. Missing either element fails. |
| C-57 | Named, executable anti-pattern procedure | prevention | Anti-pattern checkpoints are expressed as executable procedures (e.g., "For each proposal, ask: Does X contain prose? If yes, reject."), not narrative. Narrative checkpoints fail. |
| C-58 | Cross-checkpoint assertion | integrity | After both delta and proposals checkpoints complete, output includes an assertion: "Zero proposal rows failed either checkpoint and were not emitted." Missing assertion fails. |
| C-59 | Inertia recurrence as unforgeable verbatim block template | behavior | A named verbatim block (`[INERTIA-GATE]`) is defined in the preamble and reproduced verbatim at each inertia decision gate. Inline recalled sentences fail; a block whose absence is structurally visible passes. A C-56 pass whose recurrence markers are inline prose rather than reproduced verbatim blocks fails C-59. |
| C-60 | Pre-printed slot architecture generalized to all binary decision sites | enforcement | Every binary decision/commitment site throughout the prompt uses a pre-printed `[ ] A / [ ] B` slot, not a conditional branch. A C-57 pass that applies slots only at the calibration check while leaving other decision sites as conditional branches fails C-60. |
| C-61 | Narrative Format Contract declared upfront as a named block before Step 1 | enforcement | A named Narrative Format Contract block appears before Step 1 — before any step is executed — naming both the required register ("conclusion before evidence") and the degenerate register ("step-description narrative — FAIL"). A C-58 pass whose gate rows name the degenerate form but define the requirement only at gate locations fails C-61. |
| C-62 | Verbatim block preamble includes explicit reproduction manifest | enforcement | The `[INERTIA-GATE]` block definition in the preamble enumerates all steps where the block will be reproduced ("This block is reproduced verbatim at Steps A, B, C; its presence is required at each site"). Without the manifest, reproduction is verifiable only by scanning all steps; with it, block absence at any declared site creates an immediately auditable gap. A C-59 pass whose preamble block does not enumerate its reproduction sites fails C-62. |
| C-63 | Type-labeled null-case declarations | behavior | When multiple change-type tables are present, each null-case declaration explicitly names the change type it covers ("ADDITIONS: none — inertia holds" / "REMOVALS: none — inertia holds"). A C-40 pass with unlabeled null declarations ("none — inertia holds") that are ambiguous across multiple change-type tables fails C-63. |
| C-64 | Symmetric justification columns across all change-type proposal tables | enforcement | Any justification column (e.g., "Inertia Rejected Because") present in one change-type proposal table must appear identically — same name, same schema, same REQUIRED status — in every other change-type proposal table. A C-56 pass where the justification column exists in the additions table but is absent from the removals or reprioritizations table fails C-64. |

---

## Score Formula

```
score = (essential_passed/5 × 60)
      + (recommended_passed/3 × 30)
      + (aspirational_passed/56 × 280)
```

**Golden threshold: 220 / 370**

Tier weights: Essential 16.2% · Recommended 8.1% · Aspirational 75.7%

---

## Version History

| Version | Criteria | Total pts | Golden | Key additions |
|---------|----------|-----------|--------|---------------|
| v18 | 61 | 355 | 210 | C-59 inertia verbatim block; C-60 slot architecture; C-61 Narrative Format Contract |
| **v19** | **64** | **370** | **220** | C-62 reproduction manifest; C-63 type-labeled null cases; C-64 symmetric justification columns |
```
