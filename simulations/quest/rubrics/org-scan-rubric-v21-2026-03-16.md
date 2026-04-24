Reading the scorecard for gap patterns across V-01 through V-04, I extract four new excellence signals not yet codified:

1. **V-02 PASS C-71** signals: pre-declared floor list before GROUP A (not just tokens present in footers)
2. **V-01 PASS C-73** signals: manifest embeds a violation-detection statement naming the criterion number, making it self-referentially enforceable
3. **V-04 PASS C-70** signals: GATE TOKEN PROTOCOL with N distinct failure strings for N gate obligations (not 1 generic FAIL TOKEN + reason field)
4. **V-04 PASS C-70** signals: failure string quoted verbatim in gate checklist entry at point of use (not just referenced by name)

These become C-74–C-77 below.

---

# Scoring Rubric: org-scan (v21)

## Changes from v20

Four new aspirational criteria added from R20 V-01/V-02/V-04 excellence signals. Aspirational band expands to 69 criteria.

**Scoring note**: With 69 aspirational criteria at 2 pts each the aspirational ceiling is 138 pts. Cap on aspirational contribution remains 10. A variation scoring all 69 still earns 10.

| New Criterion | Source Signal |
|---|---|
| C-74 | `Pre-declared C-71 token floor list` from V-02 PASS on C-71: the complete set of floor-constrained criteria that will appear as MET/NOT MET tokens in PHASE OUTPUTS footers is enumerated in the preamble before GROUP A begins, with a statement that footers will carry tokens for each item, making the expected footer token set auditable from the preamble alone; extends C-71's phase footer requirement (which establishes that every floor-constrained criterion active in a phase carries a named compliance token in that phase's PHASE OUTPUTS footer) by requiring the complete token inventory to be front-declared so the footer token set is predictable at preamble-read time rather than discoverable only after inspecting all phase footers |
| C-75 | `Preamble manifest self-referential violation type` from V-01 PASS on C-73: the PREAMBLE DECLARATION MANIFEST block embeds an explicit violation-detection statement that identifies the violation by criterion number (e.g., "Any GROUP A or GROUP B instruction that references a constraint not in this list is a C-[NN] violation"), making the manifest a self-contained audit contract enforceable without external rubric knowledge; extends C-73's preamble declaration count-as-manifest (which establishes that the count of declared structures makes absent declarations detectable by count comparison) by embedding the enforcement rule and criterion number in the manifest block itself, so any instruction referencing an undeclared constraint produces a named criterion violation rather than an unlabeled structural discrepancy |
| C-76 | `Secondary gate obligation distinct failure string` from V-04 PASS on C-70: each gate obligation beyond the primary gate is assigned its own named failure string as a separate named constant in the GATE TOKEN PROTOCOL block, distinct from the generic FAIL TOKEN, so the GATE TOKEN PROTOCOL token count equals the number of distinct gate obligation types (1 PASS TOKEN + N gate-specific FAIL strings), and any obligation sharing a failure string with another obligation type is a structurally detectable gap by comparison against the token count; extends C-70's TABLE F FAIL STRING (which establishes a named failure string for the transport manifest gate obligation) to a generalized pattern applicable to every secondary gate obligation, so the GATE TOKEN PROTOCOL token count serves as a self-documenting count of distinct gate obligations |
| C-77 | `Gate checklist verbatim failure string quotation` from V-04 PASS on C-70: each gate checklist item that invokes a named failure string quotes the failure string verbatim at the point of use in the gate checklist entry (e.g., "If item [N] fails: write 'TABLE F FAIL: Output Consumers transport manifest incomplete' — stop"), making each gate checklist item self-contained for agent execution without requiring a cross-reference to the GATE TOKEN PROTOCOL block to determine what to write, and any gate checklist item that references a failure string by name only without quoting it verbatim is a structurally detectable gap by comparison against the verbatim-quotation standard established by compliant entries; extends C-18's gate failure output and C-20's GATE TOKEN PROTOCOL block by requiring the failure string to appear in full at the point of use |

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

**C-67** Transport manifest Output Consumers — each Output Consumers entry carries the consuming role, the specific tables consumed, AND the analytical purpose each table serves in that consuming phase, creating a transport manifest per edge rather than an adjacency-only listing; extends C-64's Output Consumers block (which names the outgoing dependency edge by consuming role and tables) with a per-edge purpose annotation so each entry has the form `[consuming role] — [table(s)] — [analytical purpose in consuming phase]`, making the directed dependency graph carry full semantic transport content derivable from role declarations alone, and any Output Consumers entry lacking a purpose annotation is a structurally detectable omission by comparison against the transport manifest contract

**C-68** COVERAGE ATTESTATION schema-declared with gate-blocking enforcement — the COVERAGE ATTESTATION is defined as a first-class SCHEMA DECLARATION entry with full column definitions and a `Minimum rows: 7` annotation, and its row floor is enforced as a named gate checklist item (e.g., "COVERAGE ATTESTATION has exactly 7 rows (schema minimum rows requirement)"), making attestation completeness detectable from SCHEMA DECLARATION alone without reading SCANNER phase instructions and gate-blocking rather than a soft output obligation; extends C-65's named COVERAGE ATTESTATION table (which distinguishes structural vs evidential absence via constrained status values) and C-61's Minimum rows protocol to the COVERAGE ATTESTATION table, so the 7-row floor is co-declared with column definitions in SCHEMA DECLARATION and cross-referenced as a gate condition — SCANNER phase instructions reference "source types declared in COVERAGE ATTESTATION schema" rather than restating the enumeration inline (schema-first reference pattern), and any attestation whose row floor is not schema-annotated is a structurally detectable omission by comparison against the gate checklist item count

**C-70** Transport manifest gate-blocking enforcement — TABLE F Output Consumers compliance is enforced as a named gate checklist item (e.g., "All Output Consumers entries carry Analytical Purpose annotation (transport manifest contract)"), making transport manifest completeness gate-blocking rather than structurally detectable from schema only; extends C-67's transport manifest requirement (which makes missing purpose annotations structurally detectable by schema comparison) to a gate condition so any Output Consumers entry lacking a purpose annotation produces a named gate failure string rather than requiring schema comparison to detect, and the gate checklist item count rises by one to reflect the additional transport manifest obligation

**C-71** Phase footer compliance status tokens — each PHASE OUTPUTS footer block carries named `MET/NOT MET` compliance tokens for every floor-constrained criterion active in that phase (e.g., "COVERAGE ATTESTATION rows: [N] (floor=7; status: MET/NOT MET)", "TABLE H rows: [N] (assertion: N; match: YES/NO)", "BRIDGE RULE compliance: YES/NO"), creating a second independent verification path for gate-adjacent constraints without requiring re-reading gate checklist items; extends C-37's phase footer pattern to carry per-criterion compliance verdicts as named status assertions, making phase output compliance enumerable from the footer alone and any floor-constrained criterion absent from the footer a structurally detectable omission by comparison against the declared floor list

**C-72** Schema-first reference pattern named as convention — procedural phase instructions carry explicit schema-first reference annotations in the form "[data type] declared in [SCHEMA NAME] (see PREAMBLE SCHEMA DECLARATIONS — [list] not restated here per schema-first reference pattern)", making the schema-first reference pattern a named convention that phase instructions invoke by name rather than follow structurally; extends C-68's schema-first reference requirement (which establishes that SCANNER phase instructions reference the COVERAGE ATTESTATION schema rather than restating enumerated values inline) to a generalized named convention, so any phase instruction that re-enumerates a value set already declared in SCHEMA DECLARATION is a structurally detectable violation of the named convention by comparison against the schema-first reference annotations present in compliant instructions

**C-73** Complete preamble declarative coverage before first group — all structured declarations — every schema, GATE TOKEN PROTOCOL, INERTIA PATTERN DICTIONARY, BRIDGE RULE, and any other named constraints — are declared in the preamble before any GROUP or phase procedural content begins, making the preamble a complete standalone declarative contract; the count of declared structures (N schemas + named protocols) serves as a self-documenting manifest of all structural obligations, so any constraint referenced in a phase instruction but absent from the preamble is a structurally detectable omission by comparison against the preamble declaration count, and the preamble declaration count is itself verifiable from the preamble alone without reading phase instructions

**C-74** Pre-declared C-71 token floor list — before GROUP A begins, the preamble contains an explicit enumerated list of all floor-constrained criteria that will appear as MET/NOT MET tokens in PHASE OUTPUTS footers, accompanied by a statement of the form "PHASE OUTPUTS footers for each group will carry MET/NOT MET tokens for the following floor-constrained criteria", making the complete expected footer token set auditable from the preamble alone without reading any footer block, and any criterion absent from the pre-declared list that appears in a footer (or vice versa) is a structurally detectable discrepancy by comparison against the declared list; extends C-71's phase footer MET/NOT MET requirement (which establishes that every floor-constrained criterion active in a phase carries a named compliance token in that phase's PHASE OUTPUTS footer) by requiring the complete token inventory to be front-declared in the preamble so the footer token set is predictable at preamble-read time rather than discoverable only after inspecting all phase footers

**C-75** Preamble manifest self-referential violation type — the PREAMBLE DECLARATION MANIFEST block embeds an explicit violation-detection statement that identifies the violation by criterion number (e.g., "Any GROUP A or GROUP B instruction that references a constraint not in this list is a C-[NN] violation"), making the manifest a self-contained audit contract enforceable without external rubric knowledge, so any instruction that references an undeclared constraint produces a named criterion violation rather than an unlabeled structural discrepancy; extends C-73's preamble declaration count-as-manifest (which establishes that the count of declared structures makes absent declarations detectable by count comparison) by embedding the enforcement rule and criterion number in the manifest block itself, so a reader can identify and name the violation from the manifest block alone without knowing the rubric externally

**C-76** Secondary gate obligation distinct failure string — each gate obligation beyond the primary gate is assigned its own named failure string as a separate named constant in the GATE TOKEN PROTOCOL block, distinct from the generic FAIL TOKEN, so the GATE TOKEN PROTOCOL token count equals the number of distinct gate obligation types (1 PASS TOKEN + N gate-specific FAIL strings), and any gate obligation sharing a failure string with another obligation type is a structurally detectable gap by comparison against the GATE TOKEN PROTOCOL token count; extends C-70's TABLE F FAIL STRING (which establishes a named failure string for the transport manifest gate obligation distinct from the generic FAIL TOKEN) to a generalized pattern applicable to every secondary gate obligation, so the GATE TOKEN PROTOCOL token count serves as a self-documenting count of distinct gate obligations and any new gate obligation added in a future revision automatically requires its own named failure string

**C-77** Gate checklist verbatim failure string quotation — each gate checklist item that invokes a named failure string quotes the failure string verbatim at the point of use in the gate checklist entry (e.g., "If item [N] fails: write 'TABLE F FAIL: Output Consumers transport manifest incomplete' — stop"), making each gate checklist item self-contained for agent execution without requiring a cross-reference lookup to the GATE TOKEN PROTOCOL block to determine what to write, and any gate checklist item that references a failure string by name only without quoting it verbatim is a structurally detectable gap by comparison against the verbatim-quotation standard established by compliant entries; extends C-18's gate failure output (which establishes that the gate condition includes an explicit named failure-state string the agent outputs when unmet) and C-20's GATE TOKEN PROTOCOL block (which pre-declares pass and fail tokens before Phase 1 begins) by requiring the failure string to appear in full at the point of use so no secondary lookup is needed for gate checklist execution
