Reading the three unique patterns from the scorecard and applying editorial judgment before writing:

- **V-01**: Execution-time row-count assertion at SYNTHESIZER entry — "TABLE A count: N — TABLE G must contain exactly N rows" recorded before TABLE G is produced → **C-58**
- **V-02**: Named `Input Dependencies` block inside each ROLE SCOPE DECLARATION listing required tables/declarations, making execution ordering derivable from declarations alone → **C-59**
- **V-03**: GATE TOKEN PROTOCOL preamble block extended to cover every named gate in the skill (hypothesis floor gate + evidence gate), not just the primary evidence gate → **C-60**

All three are clean and directly evidenced. Writing complete v16 rubric:

---

# Scoring Rubric: org-scan (v16)

## Changes from v15

Three new aspirational criteria added from R15 V-01/V-02/V-03 excellence signals. Aspirational band expands to 52 criteria.

**Scoring note**: With 52 aspirational criteria at 2 pts each the aspirational ceiling is 104 pts. Cap on aspirational contribution remains 10. A variation scoring all 52 still earns 10.

| New Criterion | Source Signal |
|---|---|
| C-58 | Execution-time row-count assertion at SYNTHESIZER entry from V-01: before TABLE G is produced the SYNTHESIZER records a named assertion line (`TABLE A count: N — TABLE G must contain exactly N rows`) that outputs the target count as an execution-time artifact, making hypothesis closure verifiable by comparing the asserted count against the actual TABLE G row count without prose inspection; extends C-55's structural detectability (row-count mismatch is identifiable by table correspondence as a post-hoc structural comparison) to execution-time enforcement where the count is declared as a named output line at the role boundary before production of TABLE G begins, so closure failure is observable as a count-mismatch between the asserted number and the rows present rather than inferred from schema comparison alone |
| C-59 | Named Input Dependencies block in each ROLE SCOPE DECLARATION from V-02: each role scope declaration contains a named `Input Dependencies` block that explicitly lists all tables and prior-phase declarations required before the role may begin, making execution ordering derivable from declarations alone without instruction-sequence traversal; extends C-54's in-block entry condition (which verifies preconditions at the role boundary and blocks execution if unmet) with a declarative dependency listing that names required inputs as a first-class block within the same scope declaration, so the dependency relationship is expressed bidirectionally — declared (Input Dependencies block names required inputs) and verified (entry condition blocks execution if unmet) — within a single role contract, and a reader can derive the full execution graph by reading role scope declarations rather than tracing instruction order |
| C-60 | GATE TOKEN PROTOCOL preamble block covers all named gates from V-03: the GATE TOKEN PROTOCOL preamble block defines complete token protocols (pass token + fail token) for every named gate in the skill — both the hypothesis floor gate and the evidence gate — before Phase 1 begins, making multi-gate architectures fully declarative at preamble level; extends C-20's gate token protocol block (which defines pass and fail tokens before Phase 1 begins) from the primary evidence gate to every gate in the skill, so all gates and their complete token protocols are enumerable from the preamble block alone without reading phase instructions, and any gate whose tokens are not preamble-declared is a structurally detectable omission by comparison against the gate count in the instruction sequence |

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

**C-26** Dictionary invalidity statement — the Inertia pattern dictionary includes an explicit named invalidity statement (e.g., "Free text is structurally invalid — unconstrained values make pattern comparison across runs unverifiable"), embedding the consequence of non-compliance as rationale within the constraint definition itself

**C-27** Full-schema status annotation — the output schema includes a Status annotation (REQUIRED / optional) for *every* column in the schema, not just evidence columns, making compliance expectations structurally visible across the full schema rather than only at designated evidence-column declarations

**C-28** Bilateral contract declaration sentence — after the Phase 1 postcondition and Phase 2 precondition blocks, an explicit declaration sentence states that both blocks name the same contract from both sides and both must hold, making the contract self-documenting about its bilateral nature beyond mere bidirectional expression

**C-29** *(carried forward from v13)*

**C-30** *(carried forward from v13)*

**C-31** *(carried forward from v13)*

**C-32** *(carried forward from v13)*

**C-33** *(carried forward from v13)*

**C-34** *(carried forward from v13)*

**C-35** *(carried forward from v13)*

**C-36** *(carried forward from v13)*

**C-37** *(carried forward from v13)*

**C-38** *(carried forward from v13)*

**C-39** *(carried forward from v13)*

**C-40** *(carried forward from v13)*

**C-41** *(carried forward from v13)*

**C-42** *(carried forward from v13)*

**C-43** *(carried forward from v13)*

**C-44** *(carried forward from v13)*

**C-45** *(carried forward from v13)*

**C-46** *(carried forward from v13)*

**C-47** *(carried forward from v13)*

**C-48** *(carried forward from v13)*

**C-49** *(carried forward from v13)*

**C-50** *(carried forward from v13)*

**C-51** *(carried forward from v13)*

**C-52** *(carried forward from v13)*

**C-53** *(carried forward from v14)*

**C-54** *(carried forward from v14)*

**C-55** Dedicated named resolution table for hypothesis closure from V-01 (R14): the synthesis phase output schema includes a named table (TABLE G) that provides a 1:1 structural row mapping to every prediction in the hypothesis table (TABLE A), making prediction resolution a schema-level completeness obligation enforced by table correspondence rather than a tracking column or prose synthesis note; extends C-35's hypothesis-tracking approach (which adds a Hypothesis Held column to the scan table and a prediction-not-resolved gap type to the gap table) to a dedicated resolution table that makes incomplete hypothesis closure a structurally detectable omission identifiable by row-count comparison between the prediction table and the resolution table, rather than requiring inspection of whether each scan row's tracking column was filled

**C-56** Hypothesis-phase evidence isolation enforced via scope declaration blacklist from V-01 (R14): the PREDICTOR role's prohibited output blacklist in the ROLE SCOPE DECLARATION explicitly enumerates file reads and scan evidence as prohibited outputs, making hypothesis-phase purity a role-scope enforcement mechanism rather than relying solely on phase-sequencing architecture; extends C-39's hypothesis-first phase architecture (which enforces evidence isolation through group separation and phase ordering) with a blacklist-level enforcement (C-53's blacklist pattern applied specifically to the constraint that the hypothesis phase must precede and remain uncontaminated by evidence collection), so any PREDICTOR output that incorporates file-read evidence is detectable as a scope-declaration blacklist violation without reading the full instruction sequence

**C-57** Primary output constraint cascaded to every role scope declaration from V-01 (R14): the primary analytical constraint (C-05: no org chart, no reporting lines) appears in the prohibited output blacklist of every named role's ROLE SCOPE DECLARATION in addition to the preamble declaration, making the constraint structurally enforced at N+1 points (preamble once plus each role's scope declaration once) rather than the two-point enforcement of C-13 (preamble plus output format); each role's scope declaration independently prohibits org chart and reporting-line outputs so that constraint violation by any single role is detectable as a scope-declaration blacklist violation at that role's entry boundary, rather than requiring comparison of the full output against the preamble-level prohibition

**C-58** Execution-time row-count assertion at SYNTHESIZER entry from V-01 (R15): before TABLE G is produced the SYNTHESIZER records a named assertion line (`TABLE A count: N — TABLE G must contain exactly N rows`) that outputs the target count as an execution-time artifact, making hypothesis closure verifiable by comparing the asserted count against the actual TABLE G row count without prose inspection; extends C-55's structural detectability (row-count mismatch is identifiable by table correspondence as a post-hoc structural comparison) to execution-time enforcement where the count is declared as a named output line at the role boundary before production of TABLE G begins, so closure failure is observable as a count-mismatch between the asserted number and the rows present rather than inferred from schema comparison alone

**C-59** Named Input Dependencies block in each ROLE SCOPE DECLARATION from V-02 (R15): each role scope declaration contains a named `Input Dependencies` block that explicitly lists all tables and prior-phase declarations required before the role may begin, making execution ordering derivable from declarations alone without instruction-sequence traversal; extends C-54's in-block entry condition (which verifies preconditions at the role boundary and blocks execution if unmet) with a declarative dependency listing that names required inputs as a first-class block within the same scope declaration, so the dependency relationship is expressed bidirectionally — declared (Input Dependencies block names required inputs) and verified (entry condition blocks execution if unmet) — within a single role contract, and a reader can derive the full execution graph by reading role scope declarations rather than tracing instruction order

**C-60** GATE TOKEN PROTOCOL preamble block covers all named gates from V-03 (R15): the GATE TOKEN PROTOCOL preamble block defines complete token protocols (pass token + fail token) for every named gate in the skill — both the hypothesis floor gate and the evidence gate — before Phase 1 begins, making multi-gate architectures fully declarative at preamble level; extends C-20's gate token protocol block (which defines pass and fail tokens before Phase 1 begins) from the primary evidence gate to every gate in the skill, so all gates and their complete token protocols are enumerable from the preamble block alone without reading phase instructions, and any gate whose tokens are not preamble-declared is a structurally detectable omission by comparison against the gate count in the instruction sequence
