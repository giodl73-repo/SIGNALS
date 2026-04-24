Reading the v8 rubric and scorecard to identify the new excellence patterns before writing v9.

Two new patterns emerge from the R12 scorecard:

1. **C-21 PARTIAL in V-01** — "'IA files already exist — do not overwrite' is implicit FORBIDDEN rather than declared." This reveals a class of prohibitions expressed as imperative negation ("do not X") rather than explicit `FORBIDDEN:` declarations. C-21 governs typed variable bindings; no criterion yet governs this broader prohibition-form requirement.

2. **C-19 PARTIAL in V-01** — "task instructions use plain imperative not MUST; constraint statements mostly MUST/FORBIDDEN but not universally." This reveals that phases mix task-step prose and constraint declarations without structural demarcation, making it impossible to identify constraint statements as a distinct class. C-19 requires MUST/FORBIDDEN register in constraint statements; no criterion yet requires those statements to be structurally separated from task steps.

Denominator: 20 → 22. Formula denominator updated accordingly.

---

```markdown
---
skill: quest-rubric
skill_target: org-build
date: 2026-03-16
version: 9
---

# Scoring Rubric — org-build

## Essential Criteria (5)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-01** | org-chart.md present with ASCII hierarchy | correctness | File exists and contains an ASCII box/line diagram with min 2 org levels. Flat name list fails. |
| **C-02** | All five role fields present in every .roles/ file | correctness | Every role file contains `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. Any missing field fails. |
| **C-03** | inertia-advocate role always present | correctness | A role file with `inertia` or `advocate` in name/title exists under `.roles/`. Absence fails unconditionally. |
| **C-04** | Role count within depth range | coverage | Standard: 20-30 files. Deep: 50+. Below lower bound fails. Exceeding upper bound by >20% without deep flag also fails. |
| **C-05** | Headcount by area table present | format | org-chart.md has table with `Area`, `Headcount`, `Key Roles`, `Decides`, `Escalates` columns. Table without Decides/Escalates fails. |

## Recommended Criteria (3)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-06** | Role files grouped by area subdirectories | format | `.roles/` has min 2 area subdirs. All roles flat with no grouping fails. |
| **C-07** | Operating rhythm table and committee charters complete | depth | Rhythm table with 3+ distinct rows (ROB + shiproom + governance) AND a charter per governance meeting with all 5 fields including Quorum as `N of M` fraction. |
| **C-08** | Inertia assessment reaches VERDICT with FLAT-CASE-PRESSURE rating | depth | org-chart.md contains `FLAT-CASE-PRESSURE:` with a closed-set rating and a `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED` verdict. Generic prose without rated verdict fails. |

## Aspirational Criteria (22)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-09** | Org Evolution Roadmap with typed triggers | depth | 2+ rows: Row 1 is headcount threshold, Row 2 is different category. Two headcount thresholds fails. |
| **C-10** | Anti-Pattern Watch uses cat-N typed citations | correctness | 2+ rows where every "Why It Applies Here" cell opens with `[element name] (cat-N) —` syntax. Plain prose fails. Descriptive format guidance without imperative MUST fails. |
| **C-11** | Phase-gate with cross-artifact coherence: IA scope references FLAT-CASE-PRESSURE rating | depth | inertia-advocate `scope` field is derived from the FLAT-CASE-PRESSURE rating via pre-written templates (one per rating level). Generic scope text not tied to rated verdict fails. |
| **C-12** | Anti-pattern categories derived from structural design choice | depth | Anti-pattern category selection is explicitly tied to the design decision: flat org produces cat-3/cat-2; deep hierarchy produces cat-1/cat-4. Category choices independent of structure fail. |
| **C-13** | Single-verdict guard uses explicit error framing | correctness | C-08 verdict block contains explicit error framing — e.g., "Only one verdict. Both is an error." Permissive phrasing ("choose one", "pick either") fails. |
| **C-14** | Phase gates produce named typed output variables consumed by downstream input contracts | depth | At least one phase gate records a named typed output variable (e.g., T1-VERDICT, T1-PRESSURE) and at least one downstream phase declares an explicit input contract referencing that variable by name. Gate output that is implicit or unnamed fails. Downstream phase with no input contract declaration fails. |
| **C-15** | Verdict guard is bidirectional — "neither" is also an explicit error | correctness | C-08 verdict block explicitly names both failure modes: "Both is an error" AND "Neither is an error." A guard that covers only the "both" direction fails. Symmetric FORBIDDEN framing ("FORBIDDEN: writing both. FORBIDDEN: omitting both.") satisfies this criterion. |
| **C-16** | Anti-pattern Mitigation cells contain remediation actions, not format guidance | correctness | Every Mitigation cell in the Anti-Pattern Watch table contains a specific remediation action. Cells containing descriptive format instructions or column-structure guidance instead of actions fail. |
| **C-17** | IA scope template applied verbatim — paraphrase fails | correctness | The inertia-advocate `scope` field contains the exact text of the applicable rating-keyed template. Paraphrase, adaptation, or any deviation from the template text fails. "Derived, not composed" is necessary but not sufficient; verbatim copy is required. |
| **C-18** | Category exclusion sets are explicitly FORBIDDEN per verdict path | depth | The anti-pattern derivation block states not only which categories are required per verdict but also which are forbidden: CAN-OPERATE-FLAT forbids cat-1/cat-4; STRUCTURE-WARRANTED forbids cat-2/cat-3. Stating the correct path without forbidding the wrong path fails. |
| **C-19** | Imperative register used uniformly across all phase instructions | correctness | Every constraint statement in every phase uses MUST or FORBIDDEN. Advisory language ("should", "prefer", "typically", "consider") in any constraint context fails. C-10 requires MUST in one section; this criterion requires that register across the entire output. |
| **C-20** | All phase gates declare typed outputs and all dependent phases declare input contracts | depth | Every phase gate in the output declares named typed output variables. Every phase that consumes a prior gate's output declares an explicit input contract naming that variable. C-14 requires at least one such pair; this criterion requires systematic coverage. Any gate with implicit or unnamed output fails. Any consuming phase with no input contract declaration fails. |
| **C-21** | Constraint-completeness seal: every typed gate variable is governed by MUST/FORBIDDEN in its consuming phase | depth | For every named typed output variable declared at a phase gate, the downstream input contract that consumes it is governed by MUST or FORBIDDEN — not advisory language. C-19 requires uniform register across all phases; C-20 requires systematic gate coverage; this criterion requires the two properties to intersect: each typed variable binding must be simultaneously named (C-20) and imperatively constrained (C-19). A typed binding consumed with "should reference" or "typically uses" fails. Advisory language anywhere in an input contract that governs a named gate variable fails. |
| **C-22** | Pre-print skeleton with named placeholder slots keyed to gate variables | format | The output contains a filled template skeleton for at least one artifact, showing its shape with explicit named placeholder slots (e.g., `{{T1-VERDICT}}`, `[FLAT-CASE-PRESSURE-RATING]`) that correspond directly to typed output variables declared at phase gates. A typed variable declaration with no corresponding template slot fails. A skeleton with unnamed or untyped slots (e.g., `[VALUE]`, `___`) fails. Template shape must be derivable from gate variable names alone — a reader who knows only the gate outputs must be able to fill in every slot without ambiguity. |
| **C-23** | Phase-execution ordering constraint: FORBIDDEN beginning a phase before recording all preceding gate outputs | correctness | Every phase transition includes an explicit prohibition on starting the next phase before all output variables of the current phase have been recorded. Stating output contracts without a temporal ordering guard fails. A blanket "record before proceeding" instruction at the top of the prompt is insufficient — each phase boundary must carry the constraint. This operates at the process level: it governs execution order, not schema content. A prompt that defines correct gate schemas (C-20) but omits the ordering FORBIDDEN at any phase boundary fails this criterion. |
| **C-24** | Record-block checkpoint: named record block materialized after each phase gate | format | After every phase gate, the output contains a named record block — a structured text block that materializes each typed output variable by name and value (e.g., `T2-PRESSURE: ELEVATED`, `T2-VERDICT: STRUCTURE-WARRANTED`) before the next phase begins. A gate variable appearing only in a contract table fails; it must appear as an emitted record block. Record blocks serve as auditable checkpoints: they make gate boundaries observable and expose dangling outputs (variables declared but never emitted). A prompt that defines gate contracts (C-20) and ordering guards (C-23) but never requires materialized record blocks fails this criterion. |
| **C-25** | Double-guard at every phase boundary: outbound FORBIDDEN at gate and inbound FORBIDDEN at consuming phase | depth | Every phase transition carries two orthogonal FORBIDDENs: one at the outbound gate ("FORBIDDEN: beginning Phase N+1 before emitting this record block") and one at the inbound contract of the consuming phase ("FORBIDDEN: executing Phase N+1 before Phase N record block is emitted"). A single FORBIDDEN in only one direction — outbound only or inbound only — fails. C-23 requires per-boundary ordering guards; this criterion requires those guards to be bidirectionally redundant so that a model that skips either the gate emission or the input contract check still hits the other. |
| **C-26** | Record block construct unifies gate declaration, ordering anchor, and materialization in one structure | depth | The record block (e.g., `=== RECORD: PHASE-N ===`) is designed so that a single construct simultaneously satisfies gate variable declaration (C-20), anchors the phase-ordering FORBIDDEN to a concrete emitted artifact (C-23), and is the materialized record block (C-24) — with the variable names it emits directly available for imperative binding in the downstream input contract (C-21). A prompt that implements gate contracts, ordering guards, and record blocks as three separate constructs without structural unification fails. The record block must be the artifact from which all four properties are observable from one location; a reader seeing only the record block definition must be able to derive the gate schema, the ordering constraint anchor, and the materialization checkpoint without cross-referencing other sections. |
| **C-27** | Depth-flag-conditional count floor in Phase 1 instruction | correctness | Phase 1 binds the role count floor explicitly to the T1-DEPTH-FLAG value: "T1-DEPTH-FLAG = standard → MUST enumerate 20–30 roles; T1-DEPTH-FLAG = deep → MUST enumerate 50+ roles." A flat count range stated without flag binding fails. A depth flag declared without a per-value count floor fails. Stating the count range in a rubric or preamble without encoding it as a phase-instruction conditional also fails — the binding must be inside the phase instruction itself. |
| **C-28** | Ordering anchor embedded as named first field inside record block | format | Every `=== RECORD: PHASE-N ===` block contains a `PHASE-ORDERING-GUARD:` field as its first entry, carrying a FORBIDDEN directive naming the next phase (e.g., `PHASE-ORDERING-GUARD: FORBIDDEN: Phase N+1 begins before this block is emitted.`). The anchor must be structurally inside the block — not in surrounding preamble, phase-end prose, or a separate instruction section. C-26 requires the block to be the artifact from which the ordering constraint is derivable; this criterion tests the specific mechanism that satisfies C-26. A block that relies on a preamble assertion of structural unification — even if that preamble explicitly claims the block IS the ordering anchor — fails. Claiming unification in prose is not structural unification. |
| **C-29** | All prohibitions use explicit `FORBIDDEN:` declaration — no imperative negation | correctness | Every prohibition in every phase takes the form `FORBIDDEN: [action]`. Imperative negation forms — "do not X", "never X", "avoid X", "X already exists — do not overwrite", or any phrasing that implies prohibition without the `FORBIDDEN:` keyword — fail in any constraint context. The prohibition form must be structurally distinguishable as a constraint, not interpretable as a task instruction. C-21 governs FORBIDDEN bindings on named typed gate variables; this criterion extends the same explicitness requirement to all prohibitions throughout the prompt regardless of whether they govern typed variables. A prompt that correctly uses `FORBIDDEN:` for gate variables (satisfying C-21) but uses "do not overwrite" elsewhere fails this criterion. |
| **C-30** | Phase instructions structurally segment task steps from constraint declarations | format | Each phase separates task-execution instructions (what to enumerate, evaluate, or produce) from constraint declarations (MUST/FORBIDDEN statements) using a structural boundary — e.g., a dedicated Constraints subsection, a labeled block, or explicit headers ("Task:" / "Constraints:"). A phase that interleaves task-step prose and MUST/FORBIDDEN constraints without structural demarcation fails. C-19 requires MUST/FORBIDDEN register in constraint statements; this criterion requires those statements to be structurally identifiable as a distinct class from task steps so that a reader can audit constraints independently of task prose. A phase whose MUST/FORBIDDEN constraints are scattered among task instructions without segmentation fails even if every constraint individually uses the correct register. |

## Formula

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/22 * 10)
```

---

## What changed in v9

| Change | Rationale |
|--------|-----------|
| Added C-29: explicit `FORBIDDEN:` declaration required for all prohibitions | R12 V-01 C-21 PARTIAL surfaced "do not overwrite" as implicit FORBIDDEN — imperative negation satisfies the intent but is not structurally machine-readable as a constraint. C-21 covered typed variable bindings; C-29 extends the prohibition-form requirement to every prohibition in the prompt. |
| Added C-30: task steps and constraint declarations structurally segmented per phase | R12 V-01 C-19 PARTIAL surfaced that phases mixing task prose with MUST/FORBIDDEN constraints cannot be audited for constraint completeness. C-19 requires the correct register in constraint statements; C-30 requires those statements to be structurally demarcated from task steps so they form an identifiable, auditable class. |
| Aspirational denominator 20 → 22; formula updated accordingly | Two new aspirational criteria added. |
```
