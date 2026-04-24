# Scoring Rubric: org-scan (v18)

## Changes from v17

Three new aspirational criteria added from R17 V-02/V-03/V-04 excellence signals. Aspirational band expands to 58 criteria.

**Scoring note**: With 58 aspirational criteria at 2 pts each the aspirational ceiling is 116 pts. Cap on aspirational contribution remains 10. A variation scoring all 58 still earns 10.

| New Criterion | Source Signal |
|---|---|
| C-64 | `Output Consumers` block in each ROLE SCOPE DECLARATION from V-02: each role scope declaration carries an `Output Consumers` block that explicitly lists every downstream role that depends on the tables this role produces, naming the outgoing dependency edge symmetrically with C-59's `Input Dependencies` block (which names the incoming edge); together they make the full directed dependency graph derivable from role declarations in either direction without instruction-text traversal — a reader can determine for any role both what it requires and what requires it by reading scope declarations alone, so any role whose scope declaration lacks an `Output Consumers` block is a structurally detectable omission by comparison against the consumer references in other roles' `Input Dependencies` blocks |
| C-65 | Named `COVERAGE ATTESTATION` table at SCANNER exit from V-03: the SCANNER produces a named `COVERAGE ATTESTATION` table at phase exit with one row per source type (all 7 enumerated) and a status column constrained to `scanned / not-found / not-applicable`, distinguishing structural absence (source type not applicable to this org) from evidential absence (source type applicable but no evidence found); extends C-02's multi-source citation requirement (3+ of 7 source types cited in TABLE B) and C-24's self-documenting pass token (which embeds `[N] sources scanned` as a count-level summary) to a per-type audit trail where coverage gaps are structurally visible as `not-found` rows rather than inferable from the absence of TABLE B citations, so any source type that was checked but yielded nothing is represented as a named row rather than a silent omission |
| C-66 | `TABLE H -- Org Shape Delta` in SYNTHESIZER output from V-04: the SYNTHESIZER produces a named `TABLE H -- Org Shape Delta` with four required columns — Dimension / Current State / Recommended State / Driving Evidence — where each Driving Evidence cell requires a `(cite TABLE B row)` annotation, extracting the per-dimension current-vs-recommended comparison from prose into a queryable structured table; extends C-10's current/recommended separation requirement (expressed as a prose instruction that current state and recommended state be clearly separated) and C-07's org shape requirement (named and justified from findings) to a schema-level obligation where the comparison surface is enumerable as table rows and any dimension lacking a TABLE B evidence citation is a structurally detectable omission, so the delta between current and recommended org shape is verifiable from table content alone without prose inspection |

---

## Essential (60%)

**C-01** Areas named and traceable to scan evidence, not invented
**C-02** Multi-source scan — 3+ of 7 source types cited
**C-03** Headcount estimated as a range with supporting rationale
**C-04** Cross-cutting concerns named with boundary note
**C-05** Raw analysis only — no org chart, no reporting lines

---

## Recommended (30%)

**C-06** Team boundary candidates with seam rationale
**C-07** Org shape named and justified from findings
**C-08** Evidence gaps and ambiguities flagged explicitly

---

## Aspirational (10% cap, 2 pts each, max 10)

**C-09** 5+ specific file paths cited as auditable evidence

**C-10** Current state vs recommended state clearly separated

**C-11** Anti-fabrication language embedded per evidence-dependent section

**C-12** Hard sequencing gate: scan must complete before synthesis begins

**C-13** Critical constraint (C-05) stated twice — preamble + output format

**C-14** Verification checklist at sequencing gate — numbered items + required confirmation sentence before synthesis proceeds

**C-15** Structural group labels for phase separation — phases labeled as discrete named groups (e.g., GROUP A / GROUP B), not just section headings within a single flow

**C-16** File path floor enforced as a gate condition — 5-path requirement stated as a precondition that blocks proceeding to the next phase, not just an output expectation

**C-17** Gate confirmation token — the confirmation sentence follows a named-token format (e.g., "Gate clear — [brief summary]"), making gate passage machine-parseable rather than requiring prose interpretation

**C-18** Gate failure output — the gate condition includes an explicit named failure-state string (e.g., "write 'Path floor not met'") that the agent outputs when the condition is unmet, making gate failures verifiable without prose inspection

**C-19** Inertia Match column — scan output includes a per-row Inertia Match column that anchors each finding to an organizational inertia pattern, making scan evidence structured and pattern-linked rather than descriptive prose

**C-20** Bidirectional gate token protocol block — a named `GATE TOKEN PROTOCOL` block in the preamble defines both the pass token and fail token as named constants before Phase 1 begins, making the gate protocol self-contained and referenceable throughout the skill rather than defined only at the point of use

**C-21** Required table column enforcement — evidence columns (Inertia Match, file paths) are declared as *required* table columns in the output schema, making omissions structurally visible as empty cells rather than silently absent from prose narrative

**C-22** Formal phase contract — the gate is expressed bidirectionally as the postcondition of Phase 1 *and* the precondition of Phase 2, naming both sides of the contract explicitly so the phase boundary is verifiable in either direction, not just a unidirectional sequencing rule

**C-23** Inertia pattern dictionary — the Inertia Match column is constrained by a named pattern dictionary (enumerated valid values with labels) embedded in the skill before Phase 1 begins, preventing free-text entry that would make pattern-linkage structurally unverifiable

**C-24** Self-documenting pass token — the pass token includes explicit acknowledgment of the key conditions verified (e.g., source count, path floor status, dominant pattern name), making the token self-reporting about what it asserts rather than a bare named signal of passage

**C-25** Inertia Match column-order enforcement — the Inertia Match column is positioned *before* File Path Evidence in the scan output schema, enforcing that pattern identification precedes evidence citation as a structural column-order constraint rather than a layout preference

*[C-26 through C-57 — retained from prior versions]*

**C-58** Execution-time row-count assertion at SYNTHESIZER entry — before TABLE G is produced the SYNTHESIZER records a named assertion line (`TABLE A count: N — TABLE G must contain exactly N rows`) that outputs the target count as an execution-time artifact, making hypothesis closure verifiable by comparing the asserted count against the actual TABLE G row count without prose inspection; extends C-55's structural detectability (row-count mismatch is identifiable by table correspondence as a post-hoc structural comparison) to execution-time enforcement where the count is declared as a named output line at the role boundary before production of TABLE G begins, so closure failure is observable as a count-mismatch between the asserted number and the rows present rather than inferred from schema comparison alone

**C-59** Named `Input Dependencies` block in each ROLE SCOPE DECLARATION — each role scope declaration contains a named `Input Dependencies` block that explicitly lists all tables and prior-phase declarations required before the role may begin, making execution ordering derivable from declarations alone without instruction-sequence traversal; extends C-54's in-block entry condition (which verifies preconditions at the role boundary and blocks execution if unmet) with a declarative dependency listing that names required inputs as a first-class block within the same scope declaration, so the dependency relationship is expressed bidirectionally — declared (Input Dependencies block names required inputs) and verified (entry condition blocks execution if unmet) — within a single role contract, and a reader can derive the full execution graph by reading role scope declarations rather than tracing instruction order

**C-60** GATE TOKEN PROTOCOL preamble block covers all named gates — the GATE TOKEN PROTOCOL preamble block defines complete token protocols (pass token + fail token) for every named gate in the skill — both the hypothesis floor gate and the evidence gate — before Phase 1 begins, making multi-gate architectures fully declarative at preamble level; extends C-20's gate token protocol block (which defines pass and fail tokens before Phase 1 begins) from the primary evidence gate to every gate in the skill, so all gates and their complete token protocols are enumerable from the preamble block alone without reading phase instructions, and any gate whose tokens are not preamble-declared is a structurally detectable omission by comparison against the gate count in the instruction sequence

**C-61** `Minimum rows:` annotation in SCHEMA — each SCHEMA DECLARATION table with a quantifiable row floor carries a named `Minimum rows:` line (TABLE A: 3 minimum for hypothesis gate passage; TABLE B: 5 for file path floor; TABLE G: N matching TABLE A count), making the schema function as both a type contract and a quantitative contract; extends C-58's execution-time row-count assertion at the SYNTHESIZER entry boundary (which declares the count as a named output line at role execution time) to a schema-level declarative annotation co-located with the column definitions, so row-floor obligations are enumerable from schema declarations alone without reading gate conditions, SYNTHESIZER preamble assertions, or instruction sequences — the schema becomes the single authoritative source for both structural shape and quantitative minimums, and any table whose row floor is not schema-annotated is a structurally detectable omission by comparison against the table count in the gate conditions

**C-62** Three-phase symmetric gating — HYPOTHESIS FLOOR GATE at Phase 1 exit, EVIDENCE GATE at Phase 2 exit, and SYNTHESIS COMPLETENESS GATE at Phase 3 exit make every phase boundary structurally auditable through the same named-token protocol; extends C-60's all-gates-declared requirement (GATE TOKEN PROTOCOL preamble block defines complete token protocols for every named gate before Phase 1 begins) from a two-gate to a three-gate architecture where the number of gates equals the number of phases and each phase exit carries its own named gate with a complete pass/fail token pair defined in the preamble, so the entire phase-transition surface is verifiable as named machine-parseable tokens without prose inspection and any phase boundary lacking a preamble-declared gate token pair is a structurally detectable omission by comparing the gate count in the preamble against the phase count in the instruction sequence

**C-63** Named `Violated when:` entry in each ROLE SCOPE DECLARATION — each role scope declaration carries a `Violated when:` line specifying the exact structural output signature that constitutes scope violation for that role — PREDICTOR violated when scan evidence appears in TABLE A rows; SCANNER violated when TABLE E or TABLE G rows appear before gate passage; SYNTHESIZER violated when CRITICAL CONSTRAINT org chart content appears in any output table — transforming prohibition lists into per-role auditable detectors where scope breach is identifiable as a named structural condition present in output rather than inferred from absent expected content; extends C-56's PREDICTOR-specific prohibited output list (a single role's restriction expressed as a prohibition) to a per-role machine-readable violation signature for every role in the skill, so the full scope-violation detection surface is enumerable from role scope declarations alone without reading instruction text, and any role whose scope declaration lacks a `Violated when:` entry is a structurally detectable omission by comparison against the role count in the skill

**C-64** Named `Output Consumers` block in each ROLE SCOPE DECLARATION — each role scope declaration carries an `Output Consumers` block that explicitly lists every downstream role that depends on the tables this role produces, naming the outgoing dependency edge symmetrically with C-59's `Input Dependencies` block (which names the incoming edge); together they make the full directed dependency graph derivable from role declarations in either direction without instruction-text traversal — a reader can determine for any role both what it requires and what requires it by reading scope declarations alone, so any role whose scope declaration lacks an `Output Consumers` block is a structurally detectable omission by comparison against the consumer references in other roles' `Input Dependencies` blocks

**C-65** Named `COVERAGE ATTESTATION` table at SCANNER exit — the SCANNER produces a named `COVERAGE ATTESTATION` table at phase exit with one row per source type (all 7 enumerated) and a status column constrained to `scanned / not-found / not-applicable`, distinguishing structural absence (source type not applicable to this org) from evidential absence (source type applicable but no evidence found); extends C-02's multi-source citation requirement (3+ of 7 source types cited in TABLE B) and C-24's self-documenting pass token (which embeds `[N] sources scanned` as a count-level summary) to a per-type audit trail where coverage gaps are structurally visible as `not-found` rows rather than inferable from the absence of TABLE B citations, so any source type that was checked but yielded nothing is represented as a named row rather than a silent omission

**C-66** `TABLE H -- Org Shape Delta` in SYNTHESIZER output — the SYNTHESIZER produces a named `TABLE H -- Org Shape Delta` with four required columns — Dimension / Current State / Recommended State / Driving Evidence — where each Driving Evidence cell requires a `(cite TABLE B row)` annotation, extracting the per-dimension current-vs-recommended comparison from prose into a queryable structured table; extends C-10's current/recommended separation requirement (expressed as a prose instruction that current state and recommended state be clearly separated) and C-07's org shape requirement (named and justified from findings) to a schema-level obligation where the comparison surface is enumerable as table rows and any dimension lacking a TABLE B evidence citation is a structurally detectable omission, so the delta between current and recommended org shape is verifiable from table content alone without prose inspection
