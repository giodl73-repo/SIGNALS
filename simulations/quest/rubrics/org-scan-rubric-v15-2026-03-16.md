The subagent flagged four candidate patterns. I'll now apply strict editorial judgment: discard the "restart instruction" for PREDICTOR (not directly evidenced in the scorecard — that's fabrication), and discard the completeness-rule-as-named-schema-element (the note in the scorecard is a *defect* flag, not an excellence signal). That leaves three clean new criteria. Writing the complete v15 rubric:

---

# Scoring Rubric: org-scan (v15)

## Changes from v14

Three new aspirational criteria added from R14 V-01 excellence signals. Aspirational band expands to 49 criteria.

**Scoring note**: With 49 aspirational criteria at 2 pts each the aspirational ceiling is 98 pts. Cap on aspirational contribution remains 10. A variation scoring all 49 still earns 10.

| New Criterion | Source Signal |
|---|---|
| C-55 | Dedicated named resolution table for hypothesis closure from V-01: the synthesis phase output schema includes a named table (TABLE G) that provides a 1:1 structural row mapping to every prediction in the hypothesis table (TABLE A), making prediction resolution a schema-level completeness obligation enforced by table correspondence rather than a tracking column or prose synthesis note; extends C-35's hypothesis-tracking approach (which adds a Hypothesis Held column to the scan table and a prediction-not-resolved gap type to the gap table) to a dedicated resolution table that makes incomplete hypothesis closure a structurally detectable omission identifiable by row-count comparison between the prediction table and the resolution table, rather than requiring inspection of whether each scan row's tracking column was filled |
| C-56 | Hypothesis-phase evidence isolation enforced via scope declaration blacklist from V-01: the PREDICTOR role's prohibited output blacklist in the ROLE SCOPE DECLARATION explicitly enumerates file reads and scan evidence as prohibited outputs, making hypothesis-phase purity a role-scope enforcement mechanism rather than relying solely on phase-sequencing architecture; extends C-39's hypothesis-first phase architecture (which enforces evidence isolation through group separation and phase ordering) with a blacklist-level enforcement (C-53's blacklist pattern applied specifically to the constraint that the hypothesis phase must precede and remain uncontaminated by evidence collection), so any PREDICTOR output that incorporates file-read evidence is detectable as a scope-declaration blacklist violation without reading the full instruction sequence |
| C-57 | Primary output constraint cascaded to every role scope declaration from V-01: the primary analytical constraint (C-05: no org chart, no reporting lines) appears in the prohibited output blacklist of every named role's ROLE SCOPE DECLARATION in addition to the preamble declaration, making the constraint structurally enforced at N+1 points (preamble once plus each role's scope declaration once) rather than the two-point enforcement of C-13 (preamble plus output format); each role's scope declaration independently prohibits org chart and reporting-line outputs so that constraint violation by any single role is detectable as a scope-declaration blacklist violation at that role's entry boundary, rather than requiring comparison of the full output against the preamble-level prohibition |

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

**C-29** Schema violation label — the column-order constraint includes an explicit named violation label (e.g., "Inverting the order is a schema violation"), making constraint violations identifiable by output inspection rather than requiring prose interpretation of whether the constraint was breached

**C-30** Universal schema governing statement — the output schema opens with a single governing statement asserting that Status applies to every column across all tables (e.g., "This schema governs every table in this skill. Status applies to every column."), establishing universal applicability structurally rather than relying on per-table annotations alone

**C-31** Named phase boundary header — the gate is introduced with a named phase boundary label (e.g., "PHASE 1 / PHASE 2 BOUNDARY: GATE EVALUATION:") that makes the boundary a structurally identifiable named element, not just a hard sequencing transition, enabling the gate location to be found by structural scanning rather than prose reading

**C-32** Sequential evaluation enforcement — the gate checklist includes an explicit instruction to evaluate items in order without skipping (e.g., "evaluate each item in order; do not skip"), making checklist execution sequential and verifiable as a stated constraint beyond merely being a numbered list

**C-33** Named gate entry condition — the gate requires a named phase-completion statement to be written before checklist evaluation begins (e.g., a SCANNER COMPLETE declaration or equivalent), enforcing sequential constraint on gate entry itself rather than only within the checklist items, adding a pre-gate checkpoint that is structurally distinct from in-checklist sequential enforcement

**C-34** Dual-register inertia dictionary — the Inertia pattern dictionary includes a Behavioral Signals column alongside structural code-pattern entries (e.g., team language, leadership framing, incident response patterns), adding human-observable behavioral tells so each pattern is verifiable by both code inspection and team observation rather than code evidence alone

**C-35** Hypothesis confirmation tracking column — the scan output schema includes a `Hypothesis Held` column (constrained vocabulary: yes / no / partial) that links each scan row to a prior Phase 1 prediction, and the gap table includes a "prediction not resolved" gap type, forming a complete machine-verifiable hypothesis-test-result loop across prediction, evidence, and outcome

**C-36** Gate entry as role control-transfer declaration — the named gate entry condition is expressed as a role handoff declaration (e.g., "SCANNER COMPLETE — control transfers to GATEKEEPER"), making gate entry failure equivalent to a control-transfer failure between named roles rather than an unmet precondition, the strongest possible enforcement framing for sequential phase separation

**C-37** Schema-first table definition — all output tables are defined with named letter identifiers (TABLE A, TABLE B, etc.) before any phase instructions begin, making every instruction reference a pre-declared named table by letter so that the full output schema is structurally inspectable before reading the instruction sequence

**C-38** Phase lifecycle ceremony — every phase boundary carries both an explicit exit condition (phase-completion statement written at phase end) and an explicit entry condition (gate precondition verified before the next phase begins), extending named lifecycle enforcement to every phase boundary rather than only to the primary sequencing gate

**C-39** Hypothesis-first phase architecture — a dedicated Phase 1 produces named pattern predictions before evidence collection begins, and the synthesis phase explicitly resolves each prediction against evidence, making hypothesis testing the structural driver of the phase sequence rather than a tracking column added to a table produced by a single combined scan-and-categorize phase

**C-40** Dictionary declared as primary analytical framework — the inertia pattern dictionary is explicitly framed as the PRIMARY ANALYTICAL FRAMEWORK (or equivalent declaration), establishing it as the analytical lens through which evidence is interpreted from the start rather than a post-hoc classification constraint, reorienting agent posture from classify-after-scan to hypothesize-before-scan

**C-41** Named boundary section at every phase transition — each phase boundary carries a named structural section header (e.g., "GROUP A / GROUP B BOUNDARY:") above the exit and entry condition blocks, making every phase transition machine-scannable as a named section element; extends the named phase boundary header (C-31) from the primary gate only to every phase boundary in the skill

**C-42** Schema declaration as named structural block — the schema-first table definitions are wrapped in a named block header (e.g., "SCHEMA DECLARATION") making the output schema a structurally addressable named element, analogous to the GATE TOKEN PROTOCOL block (C-20) for gate tokens, so the schema block is machine-scannable as a named section rather than an unnamed leading region preceding phase instructions

**C-43** *[criterion text not present in v14 source]*

**C-44** *[criterion text not present in v14 source]*

**C-45** *[criterion text not present in v14 source]*

**C-46** *[criterion text not present in v14 source]*

**C-47** *[criterion text not present in v14 source]*

**C-48** *[criterion text not present in v14 source]*

**C-49** *[criterion text not present in v14 source]*

**C-50** Named ROLE SCOPE DECLARATION block at phase start — each phase opens with a formally named `ROLE SCOPE DECLARATION` structural block that precedes all phase instructions, making each role's operating scope a structurally inspectable named element at the phase boundary rather than distributed through instruction prose; extends the named boundary section (C-41) and schema declaration block (C-42) patterns from phase-transition elements and schema preamble to per-role operating scope at phase entry, so every named role has its own addressable scope block parallel to the way every phase boundary has a named transition header

**C-51** PAF authority citation in scope declaration — the ROLE SCOPE DECLARATION cites the specific PAF phase binding as the role's authority source (e.g., "Authority: PAF Phase 1 binding"), grounding each role's operating domain in the framework declaration so scope claims are traceable to a named framework element rather than asserted by fiat; creates a bidirectional reference structure — the PAF assigns roles to phases (C-46: framework → role) and each role's scope declaration cites the PAF as its authority (C-51: role → framework), making the role-framework binding structurally navigable in both directions

**C-52** Permitted output whitelist in scope declaration — the ROLE SCOPE DECLARATION enumerates the complete set of output tables the role is permitted to produce (e.g., "Permitted outputs: TABLE A only" for PREDICTOR, "Permitted outputs: TABLE B / C / D" for SCANNER), making role output compliance machine-verifiable against a declared whitelist rather than requiring inference from phase instructions; complements C-45's schema-level table role attribution (which names the producing role per table) with a role-level inverse statement (which tables the role owns), so the attribution is structurally navigable from both the table side and the role side

**C-53** Prohibited output blacklist in scope declaration — the ROLE SCOPE DECLARATION enumerates the output types the role is explicitly prohibited from producing (e.g., "Prohibited outputs: file reads / scan tables / gate token / org chart" for PREDICTOR, "Prohibited outputs: PREDICTOR domain / GATEKEEPER domain / synthesis" for SCANNER), making cross-role output violations structurally detectable as named blacklist violations rather than requiring inference about role boundaries from the instruction sequence; prohibited lists cover both other-role output domains and globally prohibited output types (e.g., org chart), enforcing C-05's raw-analysis constraint at the individual role-scope level in addition to the preamble and phase-entry levels

**C-54** In-block constraint check as role-entry condition — the ROLE SCOPE DECLARATION includes a constraint verification step within the block itself, making constraint compliance a role-entry condition structurally embedded in the scope declaration rather than an external gate condition or a prose instruction within the phase body; extends C-33's named gate entry condition from the primary SCANNER/GATEKEEPER boundary only to every role's scope declaration, making constraint verification universal across all role entries rather than enforced only at the primary sequencing gate

**C-55** Dedicated named resolution table for hypothesis closure — the synthesis phase output schema includes a named table (TABLE G or equivalent) that provides a 1:1 structural row mapping to every prediction in the hypothesis table (TABLE A), making prediction resolution a schema-level completeness obligation enforced by table correspondence rather than a tracking column or prose synthesis note; extends C-35's hypothesis-tracking approach (which adds a Hypothesis Held column to the scan table and a prediction-not-resolved gap type to the gap table) to a dedicated resolution table that makes incomplete hypothesis closure a structurally detectable omission identifiable by row-count comparison between the prediction table and the resolution table, rather than requiring inspection of whether each scan row's tracking column was filled

**C-56** Hypothesis-phase evidence isolation enforced via scope declaration blacklist — the PREDICTOR role's prohibited output blacklist in the ROLE SCOPE DECLARATION explicitly enumerates file reads and scan evidence as prohibited outputs, making hypothesis-phase purity a role-scope enforcement mechanism rather than relying solely on phase-sequencing architecture; extends C-39's hypothesis-first phase architecture (which enforces evidence isolation through group separation and phase ordering) with a blacklist-level enforcement (C-53's blacklist pattern applied specifically to the constraint that the hypothesis phase must precede and remain uncontaminated by evidence collection), so any PREDICTOR output that incorporates file-read evidence is detectable as a scope-declaration blacklist violation without reading the full instruction sequence

**C-57** Primary output constraint cascaded to every role scope declaration — the primary analytical constraint (C-05: no org chart, no reporting lines) appears in the prohibited output blacklist of every named role's ROLE SCOPE DECLARATION in addition to the preamble declaration, making the constraint structurally enforced at N+1 points (preamble once plus each role's scope declaration once) rather than the two-point enforcement of C-13 (preamble plus output format); each role's scope declaration independently prohibits org chart and reporting-line outputs so that constraint violation by any single role is detectable as a scope-declaration blacklist violation at that role's entry boundary, rather than requiring comparison of the full output against the preamble-level prohibition

---

**Three new criteria from R14 V-01: C-55 (dedicated resolution table), C-56 (evidence isolation via blacklist), C-57 (constraint cascaded to every role scope). Aspirational total: 49 criteria. Ceiling: 98 pts. Cap: 10.**
