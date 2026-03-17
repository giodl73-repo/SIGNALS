Three new criteria to add, sourced from:
- **V-02** new signal: Output Consumers transport manifests (purpose per edge, not just adjacency)
- **V-03** new signal: COVERAGE ATTESTATION elevated to SCHEMA DECLARATION + gate checklist enforcement
- **V-04** title: "TABLE H Dynamic Floor + Bridge Rule" → execution-time row-count assertion + named BRIDGE RULE

Here is the complete updated rubric:

---

# Scoring Rubric: org-scan (v19)

## Changes from v18

Three new aspirational criteria added from R18 V-02/V-03/V-04 excellence signals. Aspirational band expands to 61 criteria.

**Scoring note**: With 61 aspirational criteria at 2 pts each the aspirational ceiling is 122 pts. Cap on aspirational contribution remains 10. A variation scoring all 61 still earns 10.

| New Criterion | Source Signal |
|---|---|
| C-67 | `Transport manifest Output Consumers` from V-02: each Output Consumers entry carries the consuming role, the specific tables consumed, AND the analytical purpose each table serves in that consuming phase — creating a transport manifest per edge rather than an adjacency-only listing; extends C-64's Output Consumers block (which names the outgoing dependency edge by consuming role and tables) with a per-edge purpose annotation so each entry has the form `[consuming role] — [table(s)] — [analytical purpose in consuming phase]`, making the directed dependency graph carry full semantic transport content derivable from role declarations alone, and any Output Consumers entry lacking a purpose annotation is a structurally detectable omission by comparison against the transport manifest contract |
| C-68 | `COVERAGE ATTESTATION schema-declared with gate-blocking enforcement` from V-03: the COVERAGE ATTESTATION is defined as a first-class SCHEMA DECLARATION entry with full column definitions and a `Minimum rows: 7` annotation, and its row floor is enforced as a named gate checklist item (e.g., "COVERAGE ATTESTATION has exactly 7 rows (schema minimum rows requirement)"), making attestation completeness detectable from SCHEMA DECLARATION alone without reading SCANNER phase instructions and gate-blocking rather than a soft output obligation; extends C-65's named COVERAGE ATTESTATION table (which distinguishes structural vs evidential absence via constrained status values) and C-61's Minimum rows protocol to the COVERAGE ATTESTATION table, so the 7-row floor is co-declared with column definitions in SCHEMA DECLARATION and cross-referenced as a gate condition — SCANNER phase instructions reference "source types declared in COVERAGE ATTESTATION schema" rather than restating the enumeration inline (schema-first reference pattern), and any attestation whose row floor is not schema-annotated is a structurally detectable omission by comparison against the gate checklist item count |
| C-69 | `TABLE H dynamic floor assertion + BRIDGE RULE` from V-04: before TABLE H is produced the SYNTHESIZER records a named assertion line (`Org Shape Dimension count: N — TABLE H must contain exactly N rows`) that outputs the target row count as an execution-time artifact, making dimension coverage verifiable by comparing the asserted count against the actual TABLE H row count without prose inspection; a named `BRIDGE RULE` constraint is declared (e.g., "Every TABLE H row must carry at least one `(cite TABLE B row)` annotation in its Driving Evidence cell") enforcing the evidence linkage from C-66 as a named structural rule rather than an output instruction, so the bridge between synthesis recommendations and scan evidence is verifiable by table correspondence alone and any TABLE H row lacking a TABLE B citation is a structurally detectable BRIDGE RULE violation; extends C-66's TABLE H -- Org Shape Delta (which requires TABLE B citations in Driving Evidence cells as an output instruction) to an execution-time counted assertion plus a named constraint, making both the dimension floor and the evidence linkage enumerable from declared artifacts rather than inferable from instruction compliance |

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

**C-62** *[retained from prior version]*

**C-63** *[retained from prior version]*

**C-64** `Output Consumers` block in each ROLE SCOPE DECLARATION — each role scope declaration carries an `Output Consumers` block that explicitly lists every downstream role that depends on the tables this role produces, naming the outgoing dependency edge symmetrically with C-59's `Input Dependencies` block (which names the incoming edge); together they make the full directed dependency graph derivable from role declarations in either direction without instruction-text traversal — a reader can determine for any role both what it requires and what requires it by reading scope declarations alone, so any role whose scope declaration lacks an `Output Consumers` block is a structurally detectable omission by comparison against the consumer references in other roles' `Input Dependencies` blocks

**C-65** Named `COVERAGE ATTESTATION` table at SCANNER exit — the SCANNER produces a named `COVERAGE ATTESTATION` table at phase exit with one row per source type (all 7 enumerated) and a status column constrained to `scanned / not-found / not-applicable`, distinguishing structural absence (source type not applicable to this org) from evidential absence (source type applicable but no evidence found); extends C-02's multi-source citation requirement (3+ of 7 source types cited in TABLE B) and C-24's self-documenting pass token (which embeds `[N] sources scanned` as a count-level summary) to a per-type audit trail where coverage gaps are structurally visible as `not-found` rows rather than inferable from the absence of TABLE B citations, so any source type that was checked but yielded nothing is represented as a named row rather than a silent omission

**C-66** `TABLE H -- Org Shape Delta` in SYNTHESIZER output — the SYNTHESIZER produces a named `TABLE H -- Org Shape Delta` with four required columns — Dimension / Current State / Recommended State / Driving Evidence — where each Driving Evidence cell requires a `(cite TABLE B row)` annotation, extracting the per-dimension current-vs-recommended comparison from prose into a queryable structured table; extends C-10's current/recommended separation requirement (expressed as a prose instruction that current state and recommended state be clearly separated) and C-07's org shape requirement (named and justified from findings) to a schema-level obligation where the comparison surface is enumerable as table rows and any dimension lacking a TABLE B evidence citation is a structurally detectable omission, so the delta between current and recommended org shape is verifiable from table content alone without prose inspection

**C-67** Transport manifest Output Consumers — each Output Consumers entry carries the consuming role, the specific tables consumed, AND the analytical purpose each table serves in that consuming phase, making the directed dependency graph a transport manifest derivable from role declarations alone rather than an adjacency-only listing; extends C-64's Output Consumers block (which names the outgoing dependency edge by consuming role and tables) with a per-edge purpose annotation so each entry has the form `[consuming role] — [table(s)] — [analytical purpose in consuming phase]`, so the dependency graph carries full semantic transport content and any Output Consumers entry lacking a purpose annotation is a structurally detectable omission by comparison against the transport manifest contract — a reader can determine not only which roles depend on each table but why, without tracing instruction sequences or reading phase bodies

**C-68** COVERAGE ATTESTATION schema-declared with gate-blocking enforcement — the COVERAGE ATTESTATION is defined as a first-class SCHEMA DECLARATION entry with full column definitions and a `Minimum rows: 7` annotation, and its row floor is enforced as a named gate checklist item, making attestation completeness detectable from SCHEMA DECLARATION alone without reading SCANNER phase instructions and gate-blocking (violation halts phase progression) rather than a soft output obligation; extends C-65's named COVERAGE ATTESTATION table (which distinguishes structural vs evidential absence via constrained status values) and C-61's Minimum rows protocol to the COVERAGE ATTESTATION table, so the 7-row floor is co-declared with column definitions in SCHEMA DECLARATION and cross-referenced as a named gate condition — SCANNER phase instructions reference "source types declared in COVERAGE ATTESTATION schema" rather than restating the enumeration inline (schema-first reference pattern), and any attestation whose row floor is not schema-annotated is a structurally detectable omission by comparison against the gate checklist item count

**C-69** TABLE H dynamic floor assertion + BRIDGE RULE — before TABLE H is produced the SYNTHESIZER records a named assertion line (`Org Shape Dimension count: N — TABLE H must contain exactly N rows`) that outputs the target row count as an execution-time artifact, making dimension coverage verifiable by comparing the asserted count against the actual TABLE H row count without prose inspection; a named `BRIDGE RULE` constraint is declared requiring that every TABLE H row carry at least one `(cite TABLE B row)` annotation in its Driving Evidence cell, enforcing the evidence linkage from C-66 as a named structural rule rather than an output instruction, so the bridge between synthesis recommendations and scan evidence is verifiable by table correspondence alone and any TABLE H row lacking a TABLE B citation is a structurally detectable BRIDGE RULE violation; extends C-66's TABLE H -- Org Shape Delta (which requires TABLE B citations in Driving Evidence cells as an output instruction) to an execution-time counted assertion plus a named constraint, making both the dimension floor and the evidence linkage enumerable from declared artifacts rather than inferable from instruction compliance — mirrors the C-58 + C-61 pattern (execution-time assertion + schema annotation) applied to TABLE H
