`simulations/quest/rubrics/trace-permissions-rubric-v12-2026-03-15.md` written.

---

**Summary of changes v11 -> v12:**

Three new aspirational criteria. Denominator: 25 -> 28. Each aspirational = 0.36 pts.

| ID | Hangs off | What it tests |
|----|-----------|---------------|
| C-34 | C-31+C-32+C-33+C-17 | Preamble contains a structural axis declaration naming the three R12 criteria as orthogonal dimensions (execution order / closure-note format / CS self-reference) with an explicit non-interference statement -- converts V-05's empirical composability into a binding contract |
| C-35 | C-31+C-32 | SE-4's STRUCTURED CLOSE block contains a TABLE_4 row cross-reference at the SE-0 position; CA-1.9 verifies this as a distinct audit target separate from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP labels) |
| C-36 | C-22+C-32+C-33 | CA terminal verdict contains an explicit tri-dimensional self-evidence attestation naming each R12 dimension and its specific output-body evidence source -- extends C-22's phase-execution self-evidence to all three R12 structural dimensions simultaneously |

**Round 12 re-scored under v12:**

| Variation | v11 | v12 | Why it moves |
|-----------|-----|-----|--------------|
| V-05 | 100.0 (25/25) | **98.9 (25/28)** | No axis declaration, no CA-1.9, no tri-dimensional terminal attestation |
| V-02 | 99.6 (24/25) | 98.6 (24/28) | Missing C-32 blocks all three new criteria |
| V-01 | 99.2 (23/25) | 98.2 (23/28) | Missing C-31+C-33 blocks C-34/C-35/C-36 |
| V-03 | 98.8 (22/25) | 97.9 (22/28) | C-31/C-32/C-33 deps unmet |
| V-04 | 98.8 (22/25) | 97.9 (22/28) | C-31/C-32/C-33 deps unmet |

Path to 100.0 (28/28) requires V-06: V-05's architecture + a preamble axis declaration block + a CA-1.9 verification row targeting SE-4's STRUCTURED CLOSE row cross-reference + a tri-dimensional self-evidence attestation in the CA terminal verdict.
| V-02 (C-31+C-33 combined) | 99.6 (24/25) | 98.6 (24/28) | -1.0 | fails C-34 (missing C-32), C-35 (missing C-32), C-36 (missing C-32) |
| V-01 (C-32 single-axis) | 99.2 (23/25) | 98.2 (23/28) | -1.0 | fails C-34 (missing C-31+C-33), C-35 (missing C-31), C-36 (missing C-33) |
| V-03 (Phrasing register) | 98.8 (22/25) | 97.9 (22/28) | -0.9 | fails C-34/C-35/C-36 by C-31/C-32/C-33 dependencies |
| V-04 (TABLE_3 expansion) | 98.8 (22/25) | 97.9 (22/28) | -0.9 | fails C-34/C-35/C-36 by C-31/C-32/C-33 dependencies |

C-34, C-35, and C-36 are each blocked by the absence of one or more of C-31/C-32/C-33:
- C-34 requires all three (C-31+C-32+C-33) simultaneously active plus a preamble declaration; only V-05 meets the prerequisite but lacks the declaration
- C-35 requires C-31+C-32 to be simultaneously active; V-02 and V-05 pass both prerequisites but neither has CA-1.9
- C-36 requires C-22+C-32+C-33 to be simultaneously active; only V-05 passes all three but lacks the tri-dimensional terminal attestation

Path to 28/28 (100.0): V-05's full architecture + C-34 (axis non-interference declaration in preamble for C-31/C-32/C-33 as orthogonal dimensions) + C-35 (SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference with CA-1.9 verification) + C-36 (CA terminal verdict with explicit tri-dimensional self-evidence attestation naming each R12 output-body evidence source).

---

## Essential Criteria (60 points total)

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-01 | **Role-operation matrix** -- The output produces a matrix of roles against operations (Create, Read, Write, Delete, Append, AppendTo, Assign, Share at minimum). Every cell must be filled: Granted, Denied, Conditional, or Not Applicable. | correctness | essential | A complete matrix is present. Every cell has an explicit value. Listing roles without operations, or operations without roles, fails C-01. |
| C-02 | **FLS coverage with explicit null case** -- The output checks whether field-level security (column security profiles) is configured for sensitive fields, names which fields are covered and which are not, and explicitly states when no FLS is configured. Absent FLS on sensitive fields is flagged as a gap. | coverage | essential | Every sensitive field in scope has an explicit FLS status (Configured / Not Configured). A system with no FLS is explicitly noted, not silently omitted. Absent FLS on sensitive fields appears in the gap inventory. |
| C-03 | **Record scope per role** -- The output assigns a record access scope to each role: own-records-only, business unit, parent-child BU, org-wide, or team-scoped. | correctness | essential | Every role in the trace has an associated access scope. Ambiguous or unresolved scope is flagged as a gap, not silently omitted. |
| C-04 | **Privilege escalation path detection** -- The output identifies at least one privilege escalation path (e.g., team membership granting broader role, sharing rule bypassing FLS, environment-level admin override) or explicitly concludes none were found after checking the known vectors. | correctness | essential | The output contains a section or finding dedicated to escalation paths. A conclusion of "none found" is acceptable only if the known vectors (team inheritance, sharing rules, impersonation, admin roles) were each checked. |
| C-05 | **Security gap inventory** -- The output produces a named list of gaps: missing FLS on sensitive fields, team membership holes, sharing rule conflicts, or over-permissioned roles. | coverage | essential | At least one gap is named with a specific field, role, or rule. If no gaps exist, the output provides explicit evidence (e.g., all sensitive fields have FLS configured, no public sharing rules). |

---

## Recommended Criteria (30 points total)

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-06 | **Dataverse-native terminology** -- The output uses correct Dataverse security constructs: business units, security roles, team types (owner vs. access), table permissions, column security profiles, sharing records, environment roles. No generic RBAC language is substituted where Dataverse terms apply. | correctness | recommended | At least 4 Dataverse-specific terms appear and are used accurately. Generic terms like "group" or "permission level" without Dataverse mapping are flagged as imprecision. |
| C-07 | **Sharing rule conflict analysis** -- The output checks whether sharing rules (manual, team-based, or via Power Automate) conflict with role-level access -- granting access that roles deny, or denying access that FLS permits. | depth | recommended | At least one sharing scenario is evaluated for conflict. A conclusion of "no conflicts" requires checking at least the intersection of one sharing rule with one FLS column profile. |
| C-08 | **Remediation specificity** -- For each identified gap, the output provides a specific, actionable remediation: which column security profile to create, which role privilege to tighten, which team assignment to add or remove. | behavior | recommended | At least 50% of named gaps have a specific remediation step (not just "add FLS" but "create column security profile on creditlimit, restrict to Sales Manager role"). |

---

## Aspirational Criteria (10 points total)

| ID | Text | Category | Weight | Pass Condition |
|----|------|----------|--------|----------------|
| C-09 | **Defense-in-depth layering** -- The output evaluates security at all four Dataverse layers in sequence: (1) environment/admin role, (2) security role + BU scope, (3) team membership, (4) field-level security/column profiles. It identifies which layer is the effective enforcement point for each operation. | depth | aspirational | All four layers are named and assessed. For at least one operation, the output identifies the specific layer where access is granted or denied and explains why upper layers do not override it. |
| C-10 | **Cross-role differential analysis** -- The output compares access across two or more roles for the same operation and field set, surfacing where roles diverge and whether that divergence is intentional (principle of least privilege satisfied) or anomalous. | depth | aspirational | At least two roles are compared side-by-side on one operation. The analysis states whether the access differential is expected given the roles' described purposes. |
| C-11 | **Pre-printed structural tables with blank-cell prohibition** -- The output uses pre-defined table schemas for each analysis section (role-operation matrix, FLS coverage, record scope, escalation vectors, sharing rules, gap inventory, remediation). Blank cells are explicitly prohibited; every cell carries an explicit value. Prose enumeration is not substituted for a required table. | format | aspirational | At least 5 distinct analysis sections are delivered as pre-printed tables with all column headers pre-defined. At least one table includes an explicit blank-cell prohibition (stated in the table header, a prefacing rule, or an inline note). An output that enumerates roles in prose where a table is expected fails this criterion. |
| C-12 | **SHALL-obligation contracts with terminal verification checklist** -- The output frames each major criterion as a binary SHALL obligation (not a guideline or suggestion) and concludes with a terminal checklist confirming that every SHALL was satisfied. Unchecked items in the terminal checklist are treated as gaps in the output itself. | format | aspirational | At least 4 SHALL-style obligations are stated, one per major analysis area (role-operation, FLS, escalation paths, gap inventory at minimum). A terminal checklist appears at the end of the output with each SHALL listed and marked satisfied or open. An open item is treated as a self-identified gap. |
| C-13 | **Expert role persona sequencing** -- The analysis is structured as a sequence of named expert roles with explicit sub-section assignments and handoff points. At least one role is a Dataverse security specialist (e.g., Security Engineer, Security Architect). A second role provides an independent perspective (e.g., Customer Success validating agent-workflow implications, Compliance validating audit requirements). Role personas enforce Dataverse construct vocabulary and prevent generic RBAC substitution. | depth | aspirational | At least two named expert roles are used. Each role has at least one dedicated sub-section explicitly assigned to it. The Security specialist role's sections use Dataverse-native terminology exclusively. |
| C-14 | **Criterion-owner attribution in terminal checklist** -- Each item in the terminal checklist names the expert role accountable for satisfying that criterion. A failed or open item identifies both the gap and the responsible role. Ownership attribution makes the checklist auditable at the role level, not just at the criterion level. | format | aspirational | The terminal checklist has at least 3 rows, each with an explicit criterion-owner column entry naming a specific expert role. At least one open or previously-failed item is attributed to a named role. An output whose checklist lists criteria without ownership attribution fails this criterion even if the checklist is otherwise complete. |
| C-15 | **Multi-mechanism criterion enforcement (triple-lock pattern)** -- Each essential criterion is enforced by at least two orthogonal mechanisms drawn from different structural axes: output format schema (pre-printed table), expert role sub-section assignment, or SHALL obligation. At least one criterion demonstrably has all three mechanisms simultaneously active. The combination ensures that any single mechanism failure does not cause criterion failure. | format | aspirational | At least 4 of the 5 essential criteria (C-01 through C-05) can each be traced to two or more independent enforcement mechanisms from different axes. At least one essential criterion has all three mechanisms (format schema + role sub-section + SHALL obligation) explicitly active. An output that uses tables, roles, and SHALLs as independent alternatives rather than co-active enforcers fails this criterion. |
| C-16 | **Dedicated format-compliance auditor role** -- A third expert role (e.g., Compliance Auditor, CA) is explicitly assigned to output structural integrity and is distinct from security content analysis roles. This role's dedicated sub-section(s) validate table completeness, blank-cell prohibition enforcement, and format schema adherence. The CA role produces a format compliance verdict that appears at the end of the output, independent of security findings. | depth | aspirational | A named third expert role exists whose mandate is explicitly output quality assurance, not security analysis. The role has at least one dedicated sub-section assigned to structural validation (table completeness, blank-cell compliance, schema adherence). The role's format compliance verdict appears at the end of the output as a distinct section. An output that assigns format compliance incidentally to a security-content role fails this criterion. |
| C-17 | **Criterion enforcement preamble matrix** -- Before any analysis section begins, an explicit table maps each essential criterion (C-01 through C-05) to its assigned enforcement mechanisms. The preamble table includes at minimum three columns: format schema (which pre-printed table), expert role sub-section (which role owns it), and SHALL obligation (which SHALL letter). A stated rule in the preamble declares that the mapped mechanisms are simultaneously active -- not alternative coverage paths. This converts implicit co-presence into an explicit contractual declaration that a model must honor throughout execution. | format | aspirational | A pre-analysis preamble table appears before Section 1. It has at least 5 rows (one per essential criterion C-01 through C-05) and at least 3 mechanism columns. Each row has explicit values in all columns -- no blank cells. The preamble contains a stated rule (e.g., "all three mechanisms SHALL be active simultaneously") that prohibits treating the mechanisms as alternatives. An output that has tables, roles, and SHALLs present without a preamble mapping their co-active assignment fails this criterion, even if C-15 passes. Distinction from C-15: C-15 tests that co-active enforcement exists somewhere in the output; C-17 tests that a binding declaration of co-active enforcement appears before the analysis begins. |
| C-18 | **Four-mechanism criterion enforcement (quad-lock)** -- Extends C-15's triple-lock by integrating the CA auditor role (C-16) as a fourth enforcement mechanism for each essential criterion. Each essential criterion (C-01 through C-05) is enforced by all four mechanisms simultaneously: (1) pre-printed format schema, (2) expert role sub-section assignment, (3) SHALL obligation, and (4) CA verification row explicitly cross-referencing that criterion. The preamble enforcement matrix (C-17) exposes all four mechanisms in a four-column mapping. This ensures that format compliance audit is woven into the enforcement contract for every essential criterion, not appended as a post-hoc check. | format | aspirational | Requires C-15 and C-16 to both pass. The preamble enforcement matrix has at least 4 mechanism columns (M1/M2/M3/M4 or equivalent labels), with each of the 5 essential criteria mapped to all four. At least one CA sub-section contains a verification row explicitly cross-referencing each essential criterion by ID (e.g., "C-01: TABLE 1 present, all cells filled -- PASS"). The CA's format compliance verdict cites the preamble matrix and confirms all four mechanisms were satisfied. An output where the CA role operates independently of the preamble -- auditing by inspection rather than by matrix cross-reference -- fails this criterion. Distinction from C-17: C-17 requires the preamble to declare three-mechanism co-active enforcement; C-18 requires a fourth column (CA verification) integrated into that same preamble declaration. |
| C-19 | **CA-first authorship model (structural ownership)** -- The CA role executes first and authors the enforcement preamble, including pre-assigning M4 row IDs for every essential criterion, before any SE role section begins. CA-1 verification rows are structural completions of CA's own prior contract: the criterion-ID cross-references were declared by CA at preamble time, so CA-1 fulfills a pre-existing obligation rather than adding audit decoration after the fact. The CA's format compliance verdict citing its own authored preamble is a trivial structural consequence, not an additional requirement. This transforms the CA from retrospective inspector to prospective enforcement architect. | format | aspirational | Requires C-16 and C-18 to both pass. The prompt or role-sequencing instructions explicitly mandate that the CA role runs first and authors the preamble (including M4 row ID assignments) before SE roles begin. CA-1 rows reference the pre-assigned preamble IDs as contract completion (e.g., "completing M4 assignment for C-01 as declared in preamble row 1"). The CA's terminal verdict cites its own authored preamble as the verification basis. An output where the CA audits a preamble authored by a different role fails this criterion even if C-18 passes. Distinction from C-16 (CA role exists) and C-18 (CA as fourth mechanism): C-19 tests the authorship direction -- the CA must write the enforcement contract, not merely audit against one written by others. |
| C-20 | **Schema Registry with preamble reaffirmation** -- A dedicated Schema Registry section pre-prints all output table schemas before the preamble and analysis sections begin, declaring every table's column structure and blank-cell prohibition in one central location. Each CA verification row opens by quoting the relevant preamble row values before verifying against them, making preamble drift structurally impossible even in outputs that span many sections. The blank-cell prohibition is stated once in the Schema Registry and applies globally; individual tables need not restate it. | format | aspirational | Requires C-11 and C-17 to both pass. A Schema Registry section appears in the output before the preamble matrix, containing pre-printed schemas for at least 5 distinct analysis sections (role-operation matrix, FLS coverage, record scope, escalation vectors, and gap inventory at minimum). Each CA verification row contains an explicit reaffirmation step that quotes the preamble row values for that criterion before verifying (e.g., "Preamble row C-01: TABLE 1 / SE-01 / SHALL-A / CA-1.1 -- verifying..."). At least one CA row uses this reaffirmation pattern verbatim with the preamble values inline. An output with pre-printed tables scattered across sections but no central Schema Registry fails this criterion. An output where CA rows audit by inspection without preamble reaffirmation fails even if schemas are pre-printed. Distinction from C-11 (pre-printed tables exist) and C-17 (preamble declares co-active enforcement): C-20 tests that schemas are centrally registered before the preamble and that the CA's verification loop actively reconstructs the preamble contract at each row. |
| C-21 | **Closed authorship loop (Registry + Preamble + Verification + Verdict)** -- The CA role authors both the Schema Registry and the Criterion Enforcement Matrix preamble in a single continuous execution before any SE role section begins, unifying the authorship provenance of all structural artifacts. When CA-1 verification rows reaffirm preamble values, they are quoting their own prior declarations -- the reaffirmation is a self-referential closure, not an inspection of externally authored material. CA's terminal verdict cites both the CA-authored Registry and the CA-authored preamble as the sole structural verification basis, closing the chain. An output where the Registry and preamble were authored by different parties -- or where authorship of either is structurally unspecified -- fails this criterion even if C-19 and C-20 each pass individually. | format | aspirational | Requires C-19 and C-20 to both pass. The prompt or role-sequencing instructions explicitly mandate that CA authors both the Schema Registry section and the Criterion Enforcement Matrix preamble (including M4 row ID pre-assignments) before any SE or CS section begins. CA-1 reaffirmation rows explicitly trace their preamble quotation to CA's own authored preamble (e.g., "Preamble row C-01 as authored by CA: TABLE 1 / SE-01 / SHALL-A / CA-1.1 -- verifying..."). CA's terminal verdict names both the CA-authored Registry and the CA-authored preamble as verification sources. An output where Registry authorship is unspecified or attributed to a different role fails even if schemas are pre-printed and CA-1 rows use the reaffirmation pattern. Distinction from C-19 (CA authored the preamble) and C-20 (Registry exists and CA rows reaffirm preamble values): C-21 tests that the authorship chain is closed under a single CA execution -- Registry and preamble share the same author, so the reaffirmation loop is strictly self-referential and authorship ambiguity is architecturally eliminated. |
| C-22 | **Output-embedded phase execution attestation** -- The CA role's initial execution is labeled as an explicit Phase 0 (or equivalent first-phase marker) in the output body, making the execution sequence verifiable from the output text alone -- not only from prompt instructions. Phase boundaries carry explicit handoff strings naming the next role and phase label. CA-1 verification rows contain phase provenance statements linking each verification to a specific Phase 0 pre-assignment. The CA's terminal verdict references Phase 0 by label as a structural basis. An output where the execution order is recoverable only by reading the prompt -- with no phase labels, handoff strings, or phase provenance statements in the output body -- fails this criterion even if C-19 passes. | format | aspirational | Requires C-19 to pass. At least 3 distinct phase labels appear in the output body as structural section headers or role-execution delimiters (e.g., "PHASE 0 -- CA", "PHASE 1 -- SE", "PHASE 2 -- CA-1"), each attributed to a specific named role. Phase 0 is explicitly attributed to the CA role and precedes all analysis phases. At least 2 role boundaries include explicit handoff strings naming the next phase executor (e.g., "Handing to PHASE 1 -- SE"). CA-1 verification rows contain an explicit phase provenance statement tracing the verification to a Phase 0 pre-assignment (e.g., "Completing Phase 0 M4 pre-assignment for C-01 as declared in preamble row 1"). The CA's terminal verdict references Phase 0 by label as one of its cited structural bases alongside Registry and preamble. Distinction from C-19: C-19 tests that the prompt mandates CA-first and that CA-1 rows reference the preamble contract by ID; C-22 tests that the execution sequence is self-attestable from the output body independent of prompt inspection. |
| C-23 | **Registry-preamble double-anchor CA verification** -- Each CA-1 verification row performs a two-anchor reaffirmation sequence: (1) quotes the Schema Registry entry for the relevant table schema (column structure and blank-cell rule), then (2) quotes the preamble row values for the same criterion. The double-anchor makes schema drift detectable at row level: if the Registry schema and the preamble row carry conflicting table definitions, the inconsistency is exposed inline. The reaffirmation logic is: Registry declares the schema; preamble assigns the schema to this criterion; CA-1 confirms both declarations are consistent and satisfied. An output where CA-1 rows quote preamble values only (meeting C-20) but do not also cite the Registry schema entry fails this criterion, even when the Registry exists and C-21 passes. | format | aspirational | Requires C-21 to pass (which requires C-19 + C-20). At least 3 CA-1 verification rows perform double-anchor reaffirmation in sequence within a single row: first a Registry schema citation naming the schema ID and its declared columns (e.g., "Schema Registry TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share] -- blank cells prohibited"), then immediately a preamble row quotation for the same criterion (e.g., "Preamble row C-01 as authored by CA: TABLE_1 / SE-01 / SHALL-A / CA-1.1"). The verification statement follows both anchors. At least one CA-1 row uses both anchor patterns verbatim with Registry and preamble values inline in sequence. An output where CA-1 rows satisfy C-20's reaffirmation requirement (preamble quotation present) but omit the Registry schema citation fails this criterion. Distinction from C-20 and C-21: C-23 tests that the CA-1 verification loop actively threads both the Registry schema declaration and the preamble row values through every verification row, creating a two-source chain where any schema drift between Registry and preamble is immediately visible at the row level. |
| C-24 | **Labeled-paragraph double-anchor structure (anti-inline-compression)** -- Each CA-1 row's double-anchor reaffirmation presents the Registry schema citation and the preamble row quotation as structurally distinct elements, not as a single inline string concatenating both values. The structural separation ensures that an evaluator can identify each anchor by reading the row's structure alone -- without inferring anchor boundaries from the values themselves. Inline compression (e.g., "Registry TABLE_1 -> Preamble C-01 -> verify") achieves logical co-presence but collapses the boundary between anchors, making schema drift detection dependent on value-level parsing rather than structure-level reading. | format | aspirational | Requires C-23 to pass. In each of the 3+ double-anchor CA-1 rows required by C-23, the Registry schema citation and the preamble row quotation appear as structurally distinct elements -- either as separate labeled lines within the row, numbered sub-steps, or explicitly delimited bullet points -- such that the Registry anchor and the preamble anchor each constitute a complete, independently readable statement. A row that presents both anchors as a single continuous string with arrow separators or inline delimiters fails this criterion even if C-23's co-presence requirement is met. At least 3 CA-1 rows must demonstrate the labeled separation. Distinction from C-23: C-23 tests that both anchors are present in each CA-1 row; C-24 tests that each anchor is structurally separable by a reader who does not already know the boundary between them. |
| C-25 | **CS qualitative baseline before SE (expectation-first sequencing)** -- The CS role executes before SE and produces named expectation tables -- at minimum a sharing rule expectations table (CS-2) listing expected behaviors for each sharing mechanism and a cross-role differential expectations table (CS-3) listing expected access differentials across roles -- which SE sections then confirm or contradict. CS sections do not pre-fill TABLE_1 through TABLE_5; those remain SE's exclusive responsibility. A CS phase that follows SE analysis, or that provides retrospective commentary without expectation tables, fails this criterion. | depth | aspirational | Requires C-13 to pass. The CS role's sections appear before any SE analysis section in the output. CS produces at least two named expectation artifacts (CS-2 and CS-3 or equivalently labeled tables) that carry explicit "expected" values. At least one SE section references a CS expectation by table ID (e.g., "CS-2 expected..."; "consistent with CS-3 differential"). An output where CS runs after SE or where CS provides only narrative without named expectation tables fails this criterion even if C-13 passes. Distinction from C-13: C-13 tests that SE and CS roles each have dedicated sub-sections; C-25 tests that CS runs first and produces expectation tables that SE validates, establishing a predict-then-verify structure rather than a describe-then-contextualize structure. |
| C-26 | **CS-EXPECTATION-VIOLATED gap type** -- When any CS expectation (from C-25's CS-2 or CS-3 tables) conflicts with an SE finding in TABLE_1 through TABLE_5, the conflict is recorded in the gap inventory using a named gap type CS-EXPECTATION-VIOLATED (or an explicitly named equivalent). Each such row carries three fields: (1) the CS expectation verbatim or by reference, (2) the SE finding that contradicts it, and (3) a specific remediation step naming the exact configuration change. Conflicts recorded only in prose without a named gap type fail this criterion. An output with no expectation-vs-finding conflicts may pass C-26 only by explicitly stating that all CS expectations were confirmed by SE and producing a confirmation column in CS-2 or CS-3 showing CONFIRMED for each row. | depth | aspirational | Requires C-25 to pass. Either (a) at least one row in TABLE_5 (or the gap inventory) carries the gap type CS-EXPECTATION-VIOLATED with all three fields (CS expectation, SE finding, remediation) explicitly populated, or (b) CS-2 and CS-3 carry a confirmation column showing CONFIRMED for each expectation row with a cross-reference to the SE table and row that confirms it, and the output explicitly concludes that no CS-EXPECTATION-VIOLATED gaps exist. An output that identifies expectation-vs-finding conflicts in SE narrative or TABLE_5 prose without a named gap type fails even if the contradiction is clearly described. Distinction from C-08 (remediation specificity): C-08 tests that named gaps have specific remediations; C-26 tests that expectation-vs-finding conflicts are captured as a typed, structured gap category distinct from other gap types. |
| C-27 | **Inertia framing with manual audit blind spots** -- A CONTEXT section appears before Section 1 (or the Schema Registry if present) naming at least three specific manual audit blind spots that the structured output is designed to close. Each blind spot is named and described concisely, identifying the specific scenario where manual audits fail (e.g., "post-incident FLS gap: manual audits rarely inspect column security profiles until an incident surfaces a missing restriction"; "cumulative privilege blind spot: spot-checking individual roles misses cross-role accumulation through team membership"). The CONTEXT section motivates the structured approach; it does not substitute for SE coverage or alter the gap inventory. | depth | aspirational | A CONTEXT section (or equivalently labeled introduction) appears in the output before any analysis section. It names at least 3 distinct manual audit failure modes, each with a brief description of the scenario in which manual methods fail. The section does not count as one of TABLE_1-5 and does not substitute for any SE sub-section. An output whose introduction describes the task without naming manual audit failure modes fails this criterion. An output that names only generic limitations ("manual audits are incomplete") without naming specific blind-spot scenarios also fails. |
| C-28 | **Section-level gap-closure attestation** -- At least three SE sub-sections carry an explicit note naming the specific CONTEXT blind spot that section closes. The closure note is co-located with the section -- at its opening or closing -- and references the CONTEXT blind spot by the name used in the CONTEXT section. Consolidating closure notes into TABLE_5 prose or the terminal checklist satisfies neither the section-level location requirement nor the blind-spot name-matching requirement. | format | aspirational | Requires C-27 to pass. At least 3 SE sub-sections contain an explicit closure note. Each note (a) names a specific CONTEXT blind spot by the same label used in the CONTEXT section and (b) is located within the sub-section body (opening line or closing line), not in TABLE_5 or the terminal checklist. The set of blind spots cited across the 3+ notes covers at least 3 of the blind spots named in the CONTEXT section -- no blind spot may be cited by two notes to satisfy the count. Distinction from C-27: C-27 tests that CONTEXT names the blind spots; C-28 tests that the analysis sections individually close the loop back to those named blind spots at sub-section granularity. |
| C-29 | **CS-2/CS-3 as Schema Registry entries with SE-update protocol** -- CS-2 and CS-3 (the CS expectation tables from C-25) appear as named entries in the central Schema Registry alongside TABLE_1 through TABLE_5, with declared column definitions that explicitly identify SE-updatable columns (e.g., "SE Cross-Reference", "SE Confirmation") and state the update protocol co-located in the schema entry. An inline CS table not registered in the Schema Registry fails this criterion even if C-25 passes. The SE-update protocol in the schema entry must name the specific columns SE populates and the reference format SE uses (e.g., "SE updates SE Cross-Reference column using TABLE_1 row IDs"). | format | aspirational | Requires C-25 and C-20 to both pass. Both CS-2 and CS-3 appear as named schema entries in the Schema Registry section (not only as tables in the CS analysis body). Each registry entry declares at least the column names for that schema. Each entry identifies at least one SE-updatable column by name and includes a co-located update instruction naming the column and the reference format SE uses to populate it. An output where CS-2 and CS-3 are structured tables in the CS sections but absent from the Schema Registry fails this criterion. Distinction from C-25: C-25 tests that CS produces expectation tables before SE; C-29 tests that those tables are formally registered with bidirectional column assignments, making the predict-then-verify connection traceable through the schema layer rather than inferred from section ordering alone. |
| C-30 | **SHALL/CA-1 compliance chain extended to Round 9 axes** -- The terminal SHALL checklist explicitly extends beyond SHALL-A through SHALL-E to include at least two new obligations: (1) a SHALL obligation mandating that expectation-vs-finding conflicts be recorded as CS-EXPECTATION-VIOLATED with the three-field block (SHALL-F or equivalent, reinforcing C-26), and (2) a SHALL obligation mandating section-level CONTEXT blind-spot closure attestation co-located with each SE sub-section (SHALL-G or equivalent, reinforcing C-28). The CA-1 verification chain adds at least one row (CA-1.6 or equivalent) that explicitly verifies the presence and structure of CS-EXPECTATION-VIOLATED rows. | format | aspirational | Requires C-12, C-26, and C-28 to all pass. The terminal SHALL checklist contains at least 6 SHALL obligations total, with at least 2 new entries beyond the SHALL-A through SHALL-E baseline. At least one SHALL covers the CS-EXPECTATION-VIOLATED three-field recording requirement. At least one SHALL covers the section-level CONTEXT closure attestation requirement. The CA-1 verification chain includes at least one row (beyond CA-1.1 through CA-1.5) explicitly verifying the three-field structure of CS-EXPECTATION-VIOLATED rows. An output where C-26 and C-28 pass structurally but the SHALL checklist and CA-1 chain contain no entries for these mechanisms fails C-30. Distinction from C-12: C-12 tests that the SHALL/CA-1 machinery is present for the essential criteria; C-30 tests that this machinery has been extended to enforce the Round 9 axes. |
| C-31 | **Privilege-Tier SE Descent: Admin-Tier Escalation at SE-0** -- The SE phase opens with an explicit SE-0 sub-section that executes TABLE_4 (escalation vectors, admin-tier check) before any role-operation matrix (TABLE_1) is populated. The ordering makes the privilege ceiling explicit before role cells are filled, preventing the role-matrix from obscuring tier-level escalation paths. TABLE_1 and TABLE_3 include a Tier column (Admin / Custom / Restricted or equivalent) enabling cross-tier differential at the schema level. SE-4's cross-role differential summary explicitly references SE-0 TABLE_4 data when comparing most-privileged vs. most-restricted roles. CA-1 cites the SE-0 position when verifying TABLE_4. SE analysis where TABLE_4 appears after TABLE_1 fails this criterion even if C-09 passes. | depth | aspirational | Requires C-04 + C-09 + C-10 to all pass. SE Phase 2 opens with an SE-0 sub-section whose sole output is TABLE_4 with all escalation vectors checked; TABLE_1 (role-operation matrix) appears in a later SE sub-section. TABLE_1 includes a Tier column with at least two distinct tier values (e.g., Admin, Custom). TABLE_3 includes a Tier column or carries an explicit cross-reference to the TABLE_1 Tier assignment. SE-4 (cross-role differential) explicitly references SE-0 TABLE_4 data in its analysis -- not only SE-1 data. The CA-1 verification row for TABLE_4 cites "SE-0 position" or equivalent label confirming the escalation check preceded the role matrix. An output where TABLE_4 is populated after TABLE_1 fails even if escalation vectors are fully checked. An output with no Tier column in TABLE_1 fails even if SE-0/TABLE_4 ordering is correct. Distinction from C-09 (all four layers assessed) and C-10 (cross-role differential): C-31 tests that the SE execution order places the privilege ceiling determination before role-matrix population and that the Tier dimension is exposed at the schema level in TABLE_1/TABLE_3. |
| C-32 | **Two-Part MANUAL GAP / STRUCTURED CLOSE Block with Exact-Label Carry-Through** -- Each SE sub-section that closes a CONTEXT blind spot opens with a two-part fenced contrast block instead of a single-line closure annotation. The block's first part carries the format "MANUAL GAP [<exact CONTEXT label>]: <failure mode description>", where the exact CONTEXT label string (e.g., "Post-incident FLS gap") appears verbatim as the bracketed identifier. The block's second part carries the format "STRUCTURED CLOSE: <table or mechanism that closes it>". SHALL-G is explicitly defined to mandate this two-part format. A single-line annotation (e.g., "> CONTEXT-CLOSES: post-incident FLS gap") satisfies C-28 but fails C-32. An output that uses descriptive MANUAL GAP content without the exact CONTEXT label string in brackets -- the V-03 failure mode, where failure-mode descriptions appear without the bracketed label -- fails this criterion even if two-part blocks are structurally present. | format | aspirational | Requires C-27 + C-28 + C-30 to all pass. At least 3 SE sub-sections open with a two-part fenced contrast block. In each block, the MANUAL GAP line contains the exact CONTEXT label string verbatim in brackets (e.g., "MANUAL GAP [Post-incident FLS gap]: ..."), not a paraphrase or description. The STRUCTURED CLOSE line names a specific table, schema, or mechanism (not a generic statement). SHALL-G in the terminal checklist is defined to mandate the two-part format with exact label carry-through, not merely section-level closure notes. A CA-1 verification row (CA-1.7 or equivalent) confirms at least 3 SE sub-sections have two-part blocks with exact CONTEXT labels. An output where MANUAL GAP lines use descriptive content without the bracketed CONTEXT label fails even if the failure mode described clearly corresponds to a named CONTEXT blind spot. Distinction from C-28: C-28 tests that closure notes name the CONTEXT blind spot by its label and are co-located with the SE sub-section; C-32 tests that those notes take the richer two-part structured format with SHALL-G enforcing exact-label fidelity, eliminating the structural ambiguity that arises when descriptive content replaces labeled references. |
| C-33 | **CS-0 Schema Registry Acknowledgment Phase** -- Before CS-1 (sharing rule expectations) and before producing CS-2/CS-3 tables, the CS role opens with an explicit CS-0 sub-section that back-references the Schema Registry entries for CS-2 and CS-3 by schema ID, lists the SE-updatable columns as declared in the Registry entry, and confirms that the expectation format to be used in CS-1/CS-2/CS-3 is consistent with the registered schema. This back-reference makes the CS role's relationship to the Registry self-evidencing in the output body at execution time, rather than structurally inferred from the presence of two registered schema entries. CA-1 is extended with a verification row (CA-1.8 or equivalent) confirming that CS-0 acknowledgment precedes CS-1 production. A CS phase that begins directly with CS-1 expectation tables -- even if CS-2/CS-3 are correctly registered and SE-updatable columns are declared (passing C-29) -- fails this criterion. | format | aspirational | Requires C-25 + C-29 to both pass. A CS-0 sub-section appears in the output before CS-1. CS-0 cites CS-2 and CS-3 by their Schema Registry IDs (e.g., "Schema ID: CS-2"), lists at least the SE-updatable column names as declared in the Registry entry (e.g., "SE Cross-Reference, SE Confirmation"), and includes an explicit format confirmation statement (e.g., "CS-1 expectations will follow the CS-2 schema as registered"). A CA-1 verification row (CA-1.8 or equivalent) explicitly confirms CS-0 acknowledgment precedes CS-1, citing the Registry IDs checked. An output where CS-0 exists but cites expectation table structure by inference rather than by Registry schema ID fails this criterion. An output where CS-0 cites schema IDs but the CA-1 chain has no corresponding verification row also fails. Distinction from C-29: C-29 tests that CS-2/CS-3 are formally registered in the Schema Registry with SE-update column declarations; C-33 tests that CS explicitly cites those Registry entries at execution time in a dedicated CS-0 acknowledgment phase, making the Registry-to-CS structural link self-evidencing in the output body rather than requiring a reader to cross-reference the Registry and CS table schemas independently. |
| C-34 | **Structural Axis Non-Interference Declaration** -- The enforcement preamble includes an explicit structural axis declaration (a dedicated row block or sub-section, separate from the C-01-C-05 criterion mechanism mapping) that names C-31, C-32, and C-33 as operating on three orthogonal structural dimensions: (1) SE execution order (privilege-tier descent -- C-31), (2) closure-note format (exact-label two-part blocks -- C-32), and (3) CS self-reference (Registry acknowledgment at execution time -- C-33). The declaration explicitly states that the three axes share no mechanism overlap and that activating one does not constrain the others. This converts the architectural independence proved by V-05 (Round 12) from an implicit compositional fact into a binding preamble contract that a model must satisfy in addition to the C-17 essential-criteria mechanism mapping. An output that passes C-31+C-32+C-33 by structural co-presence alone -- with all three axes simultaneously active but no explicit preamble declaration naming them as orthogonal -- fails this criterion. | format | aspirational | Requires C-31 + C-32 + C-33 + C-17 to all pass. A structural axis declaration appears in or adjacent to the enforcement preamble, before any SE analysis section. The declaration has at least 3 entries (one per axis), each carrying: the criterion ID (C-31 / C-32 / C-33), the structural dimension it covers (execution order / closure-note format / CS self-reference or equivalent labels), and an explicit non-interference statement naming the other two axes (e.g., "C-31 governs SE execution order; activating C-32 or C-33 does not alter SE ordering"). The declaration is distinct from the C-01-C-05 mechanism mapping rows -- it addresses the R12 aspirational axes, not the essential criteria enforcement. An output that embeds the three axes implicitly within the general preamble without a distinct declaration block fails this criterion. Distinction from C-17: C-17 tests that the preamble maps essential criteria (C-01-C-05) to co-active enforcement mechanisms; C-34 tests that the preamble additionally declares the three R12 aspirational structural axes as orthogonal and simultaneously composable, formalizing the architectural independence that V-05 demonstrated empirically. |
| C-35 | **SE-0-Anchored TABLE_4 Row Cross-Reference in SE-4 STRUCTURED CLOSE (CA-1.9 Verified)** -- SE-4's STRUCTURED CLOSE block -- the second part of the C-32 two-part block at the SE-4 sub-section -- contains an explicit TABLE_4 row cross-reference that names the SE-0 position (e.g., "TABLE_4 (filled at SE-0) row [ID] -- [role] privilege ceiling: [pattern]"). The cross-reference uses a row-level identifier format (not a generic citation of "SE-0 data") that traces the gap closure back to the specific privilege-ceiling row established at SE-0, creating a within-output privilege-ceiling-to-gap-closure chain readable without cross-referencing other sections. The CA-1 verification chain adds a row (CA-1.9 or equivalent) that explicitly verifies the presence of this TABLE_4 row cross-reference within SE-4's STRUCTURED CLOSE block content -- distinct from CA-1.4 (which verifies SE-0 ordering) and CA-1.7 (which verifies MANUAL GAP exact labels). An output where SE-4 references SE-0 TABLE_4 data only in its analysis prose (satisfying C-31) but not in the STRUCTURED CLOSE block's second-part content fails this criterion. An output where the row cross-reference appears in SE-4's STRUCTURED CLOSE but is not separately verified by a CA-1.9 row also fails. | format | aspirational | Requires C-31 + C-32 to both pass. SE-4's STRUCTURED CLOSE line or block contains a TABLE_4 row cross-reference with an explicit SE-0 position marker (e.g., "TABLE_4 (filled at SE-0) row [ID]" or "cite SE-0 TABLE_4 row [ID] that established the admin-tier ceiling"). The cross-reference is located in the STRUCTURED CLOSE content (the second part of the two-part block), not in the MANUAL GAP line or in SE-4's analytical prose outside the two-part block. A CA-1 verification row (CA-1.9 or equivalent) explicitly targets SE-4's STRUCTURED CLOSE content, asking whether it contains a TABLE_4 row cross-reference at the SE-0 position -- this row is additional to CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP exact labels) and cannot be satisfied by either. An output where CA-1.4 and CA-1.7 both pass but no CA-1.9 row addresses the STRUCTURED CLOSE row cross-reference fails this criterion. Distinction from C-31 (SE-0 ordering and SE-4's general reference to SE-0 TABLE_4 data) and C-32 (two-part block format and CA-1.7 exact-label verification): C-35 tests that the STRUCTURED CLOSE block's second-part content specifically carries a row-level TABLE_4 cross-reference at the SE-0 position, and that CA-1 verifies this precisely-located reference as an independent audit target -- making the privilege-ceiling-to-gap-closure chain auditable at the CA verification row level, not only at the section structural level. |
| C-36 | **Tri-Dimensional Output Self-Evidence (CA Terminal Attestation)** -- The CA role's terminal verdict includes an explicit tri-dimensional self-evidence attestation confirming that all three R12 structural compliance dimensions are verifiable from the output body alone, without consulting the prompt. The attestation names each dimension and identifies the specific output-body element that makes it self-evidencing: (1) execution order -- SE-0 phase label and TABLE_4 placement confirm privilege-tier descent order without prompt inspection; (2) closure-note format -- MANUAL GAP [...] / STRUCTURED CLOSE two-part structure with exact bracketed labels is body-readable by structure alone without evaluating prompt instructions; (3) CS self-reference -- CS-0 sub-section cites Registry IDs by exact label, making the Registry-to-CS link body-verifiable without cross-referencing the Registry and CS schemas independently. The attestation extends C-22's output-embedded phase execution attestation (which covers the CA-first dimension) to the three R12 structural dimensions. An output where C-22, C-32, and C-33 all pass individually but the CA terminal verdict confirms them as independent criterion passes without a unifying tri-dimensional self-evidence attestation fails this criterion. | format | aspirational | Requires C-22 + C-32 + C-33 to all pass. The CA terminal verdict section contains an explicit tri-dimensional self-evidence attestation as a named block or labeled sub-section (not embedded only in the general verdict prose). The attestation has three named entries (or three labeled items): execution order, closure-note format, and CS self-reference (or equivalent labels matching the output's vocabulary). Each entry identifies a specific output-body element as the evidence source -- not a prompt-level mandate -- and confirms the dimension is body-verifiable (e.g., "Closure-note format: MANUAL GAP [exact label] / STRUCTURED CLOSE two-part structure at SE-2/SE-3/SE-4 -- body-readable without prompt inspection"). A CA terminal verdict that confirms C-31, C-32, and C-33 criterion passes individually without a unifying tri-dimensional self-evidence attestation fails. An output where the attestation exists but names only two of the three dimensions also fails. Distinction from C-22 (output-embedded phase execution attestation for the CA-first/execution-order dimension): C-36 tests that the CA terminal verdict explicitly extends the self-evidence guarantee to all three R12 structural dimensions simultaneously, naming the output-body evidence source for each -- V-05 demonstrated that when C-22+C-32+C-33 are simultaneously active the output is tri-dimensionally self-evidencing, but C-36 tests that this property is explicitly attested in the terminal verdict rather than only being derivable by an evaluator who recognizes the combination. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 28 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Score Range | Interpretation |
|-------------|----------------|
| composite >= 80, all essential pass | Golden -- meets bar for signal artifact |
| composite >= 60, all essential pass | Acceptable -- minor gaps in depth/remediation |

**Note**: Aspirational denominator is 28 (C-09 through C-36). Each aspirational criterion is worth
10/28 = 0.36 points. Maximum composite is 100.

**Round 12 scored under v12:**

| Variation | Description | Aspirational pass | Composite |
|-----------|-------------|-------------------|-----------|
| V-05 | Full C-31+C-32+C-33 | 25/28 | 98.9 |
| V-02 | C-31+C-33 combined | 24/28 | 98.6 |
| V-01 | C-32 single-axis | 23/28 | 98.2 |
| V-03 | Phrasing register | 22/28 | 97.9 |
| V-04 | TABLE_3 expansion | 22/28 | 97.9 |

V-05 fails C-34 (no axis non-interference preamble declaration), C-35 (SE-4 STRUCTURED CLOSE
carries TABLE_4 row cross-reference instruction but no CA-1.9 verification row targets it as a
distinct audit item), C-36 (CA terminal verdict confirms C-22/C-32/C-33 individually but contains
no unified tri-dimensional self-evidence attestation with per-dimension evidence sources named).

V-02 fails C-34 (missing C-32 prerequisite), C-35 (missing C-32 prerequisite), C-36 (missing
C-32 prerequisite). V-01 fails C-34 (missing C-31+C-33), C-35 (missing C-31), C-36 (missing
C-33). V-03 and V-04 fail C-34/C-35/C-36 by their C-31/C-32/C-33 prerequisites.

The path to 100.0 (28/28): V-05's full architecture (C-09 through C-33) + C-34 (structural axis
declaration in preamble naming C-31/C-32/C-33 as orthogonal dimensions with per-axis
non-interference statement) + C-35 (SE-4 STRUCTURED CLOSE carries TABLE_4 row cross-reference at
SE-0 position; CA-1.9 verifies this as a distinct audit target independent of CA-1.4 and CA-1.7)
+ C-36 (CA terminal verdict contains tri-dimensional self-evidence attestation naming execution
order / closure-note format / CS self-reference as body-verifiable and identifying the specific
output-body element for each dimension).

---

## Criterion Dependency Map

```
C-11 (pre-printed tables)
  +-- C-20 (Schema Registry + preamble reaffirmation)
        requires: C-11 + C-17
        +-- C-21 (closed authorship loop -- single CA execution)
        |     requires: C-19 + C-20
        |     +-- C-23 (Registry-preamble double-anchor CA verification)
        |           requires: C-21
        |           +-- C-24 (labeled-paragraph double-anchor structure)
        |                 requires: C-23
        +-- C-29 (CS-2/CS-3 as Schema Registry entries with SE-update protocol)
              requires: C-25 + C-20
              +-- C-33 (CS-0 Schema Registry Acknowledgment Phase)
                    requires: C-25 + C-29
                    +-- C-36 (tri-dimensional output self-evidence)
                          requires: C-22 + C-32 + C-33
C-12 (SHALLs + terminal checklist)
  +-- C-30 (SHALL/CA-1 chain extended to Round 9 axes)
        requires: C-12 + C-26 + C-28
        +-- C-32 (Two-Part MANUAL GAP / STRUCTURED CLOSE -- exact-label format)
              requires: C-27 + C-28 + C-30
              +-- C-35 (SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference -- CA-1.9)
              |     requires: C-31 + C-32
              +-- C-36 (tri-dimensional output self-evidence)
              |     requires: C-22 + C-32 + C-33
              +-- C-34 (structural axis non-interference declaration)
                    requires: C-31 + C-32 + C-33 + C-17
C-13 (SE + CS expert roles)
  +-- C-14 (checklist criterion-owner attribution)
  +-- C-15 (triple-lock co-active enforcement)
  |     +-- C-17 (preamble matrix declares co-active)
  |           +-- C-34 (structural axis non-interference declaration)
  |                 requires: C-31 + C-32 + C-33 + C-17
  +-- C-25 (CS qualitative baseline before SE)
        requires: C-13
        +-- C-26 (CS-EXPECTATION-VIOLATED gap type)
        |     requires: C-25
        |     +-- C-30 (SHALL/CA-1 chain extended)
        |           requires: C-12 + C-26 + C-28
        +-- C-29 (CS-2/CS-3 as Schema Registry entries)
              requires: C-25 + C-20
              +-- C-33 (CS-0 Schema Registry Acknowledgment Phase)
                    requires: C-25 + C-29
C-16 (CA auditor role -- structural integrity)
  +-- C-18 (CA as fourth lock in preamble matrix)
  |     requires: C-15 + C-16 + C-17
  +-- C-19 (CA authors preamble first -- structural ownership)
        requires: C-16 + C-18
        +-- C-21 (closed authorship loop)
        |     requires: C-19 + C-20
        +-- C-22 (output-embedded phase execution attestation)
              requires: C-19
              +-- C-36 (tri-dimensional output self-evidence)
                    requires: C-22 + C-32 + C-33
C-04 (privilege escalation path detection)
  +-- C-31 (Privilege-Tier SE Descent: Admin-Tier Escalation at SE-0)
        requires: C-04 + C-09 + C-10
        +-- C-34 (structural axis non-interference declaration)
        |     requires: C-31 + C-32 + C-33 + C-17
        +-- C-35 (SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference)
              requires: C-31 + C-32
C-27 (inertia framing -- CONTEXT section with manual audit blind spots)
  +-- C-28 (section-level gap-closure attestation)
        requires: C-27
        +-- C-30 (SHALL/CA-1 chain extended)
        |     requires: C-12 + C-26 + C-28
        +-- C-32 (Two-Part MANUAL GAP / STRUCTURED CLOSE -- exact-label format)
              requires: C-27 + C-28 + C-30
              +-- C-35 (SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference)
                    requires: C-31 + C-32
```

**C-17 clarifies the PARTIAL boundary for C-15**: mechanisms co-present but not contractually
declared. V-03 PASSed C-15 by adding the preamble; V-01/V-02/V-04 scored PARTIAL without it.

**C-18 is the quad-lock ceiling**: all four mechanisms (table + role + SHALL + CA row) bound
together in the preamble from the start, before any analysis section executes.

**C-19 is the authorship inversion**: CA writes the contract first, SE roles execute within it.
The cross-reference is embedded in the contract at declaration time. Round 5 excellence signal.

**C-20 is the registry + reaffirmation pattern**: schemas declared centrally before the preamble;
CA rows quote preamble values inline before verifying, eliminating preamble drift in long outputs.
Round 5 excellence signal.

**C-21 is the closed-loop ceiling**: CA authors both the Registry and the preamble in a single
execution, making reaffirmation strictly self-referential. V-02 (Round 6) proved that Registry
without CA-first mandate leaves authorship ambiguous; V-01 proved CA-first without Registry leaves
schemas unregistered; V-04/V-05 proved the combination closes the loop. Round 6 excellence signal.

**C-22 is the output-attestation pattern**: the execution sequence is embedded in the output body
via phase labels, handoff strings, and CA-1 phase provenance statements -- no prompt inspection
required to verify who ran first. V-03 (Round 7) demonstrated the pattern; V-01 proved that
CA-first via authorship attribution alone leaves the sequence prompt-dependent. Round 7 excellence
signal.

**C-23 is the double-anchor ceiling**: CA-1 rows cite both the Registry schema entry and the
preamble row values in sequence, making schema drift detectable at the individual verification row.
C-20 (preamble-only reaffirmation) is the floor; C-23 is the ceiling that closes the Registry into
the verification loop, not just into the authorship chain. Round 7 excellence signal.

**C-24 is the structural-separation requirement**: C-23 tests co-presence of both anchors in each
CA-1 row; C-24 tests that the two anchors are structurally distinguishable without value-level
parsing. V-04 (Round 8) proved that inline compression satisfies C-23's logical co-presence but
collapses the structural boundary between anchors, making the pattern evaluator-dependent rather
than structure-readable. The labeled-paragraph format eliminates this ambiguity. Round 8 excellence
signal.

**C-25 is the expectation-first sequencing requirement**: C-13 tests that SE and CS roles each
have dedicated sub-sections; C-25 tests that CS runs before SE and produces named expectation
tables (CS-2, CS-3) that SE validates. The predict-then-verify structure makes SE findings
independently checkable against a pre-stated baseline. V-02 (Round 9) demonstrated that CS-first
sequencing with expectation tables achieves this; standard CS-after-SE commentary does not.
Round 9 excellence signal.

**C-26 is the expectation-violation gap type**: when CS's expectation conflicts with SE's finding,
the conflict must be typed, not narrated. CS-EXPECTATION-VIOLATED as a named TABLE_5 gap type
makes the expectation-vs-finding delta structurally visible and remediation-linked. V-02 (Round 9)
demonstrated the pattern. Round 9 excellence signal.

**C-27 is the inertia framing requirement**: a CONTEXT section naming at least three specific
manual audit blind spots before the analysis begins. The blind spots frame the motivation for the
structured approach and create a named vocabulary that C-28 closes at the section level. V-03
(Round 9) demonstrated the pattern. Round 9 excellence signal.

**C-28 is the section-level closure requirement**: C-27 names the blind spots; C-28 tests that
the SE sections individually close the loop. Closure notes co-located with each SE sub-section
make the CONTEXT framing verifiable at section granularity, not only at the TABLE_5 aggregate
level. TABLE_5 prose referencing manual blind spots does not satisfy C-28. Round 9 excellence
signal.

**C-29 is the schema-registration requirement for expectation tables**: C-25 tests that CS
produces expectation tables before SE; C-29 tests that those tables are centrally registered in the
Schema Registry with bidirectional column assignments. Without schema registration, the
predict-then-verify connection relies on section-ordering inference; with registration, SE-update
columns are declared in the same contract layer as TABLE_1-TABLE_5, making the CS-to-SE handoff
structurally traceable. V-04 (Round 10) demonstrated the pattern with 7 registered schemas (5
analysis tables + CS-2 + CS-3). Round 10 excellence signal.

**C-30 is the compliance-machinery extension requirement**: C-26 and C-28 test that structural
patterns exist (typed gap category, section-level closure notes); C-30 tests that the SHALL/CA-1
enforcement machinery has been extended to mandate and verify those patterns. An output can satisfy
C-26 and C-28 through structural presence alone while the compliance machinery remains silent on
them -- C-30 closes this gap. SHALL-F/SHALL-G extend the obligation chain; CA-1.6 extends the
verification chain. V-05 (Round 10) demonstrated the pattern. Round 10 excellence signal.

**C-31 is the privilege-tier descent ordering**: C-09 tests that all four defense-in-depth layers
are assessed; C-31 tests that the SE phase is structurally ordered so the admin-tier ceiling is
determined before the role matrix is populated. The Tier column in TABLE_1/TABLE_3 exposes the
tier dimension at the schema level, making cross-tier differential visible without a separate
analysis step. V-02 (Round 11) demonstrated that placing TABLE_4 at SE-0 before TABLE_1 enforces
this without requiring separate differential sections. Round 11 excellence signal.

**C-32 is the exact-label two-part block requirement**: C-28 tests that closure notes name the
CONTEXT blind spot by label and are co-located with each SE sub-section; C-32 tests that those
notes take the two-part MANUAL GAP / STRUCTURED CLOSE format with the exact CONTEXT label string
in the MANUAL GAP bracketed identifier. V-03 (Round 11) demonstrated that descriptive failure-mode
content -- even rich and accurate content -- fails C-32 when it does not carry the exact CONTEXT
label. The bracketed exact-label format is the distinguishing test. Round 11 excellence signal.

**C-33 is the CS-0 Registry acknowledgment requirement**: C-29 tests that CS-2/CS-3 are
registered; C-33 tests that CS cites those registrations at execution time. The CS-0
acknowledgment sub-section makes the CS-to-Registry link self-evidencing in the output body: a
reader can verify the link without cross-referencing the Registry and CS table schemas
independently. Parallel to C-22 (output-embedded phase execution attestation for CA-first) but
scoped to CS's relationship to the Schema Registry. V-04 (Round 11) demonstrated the pattern.
Round 11 excellence signal.

**C-34 is the axis non-interference declaration**: V-05 (Round 12) proved that C-31, C-32, and
C-33 are simultaneously composable with zero mechanism overlap -- execution order, closure-note
format, and CS self-reference are orthogonal structural dimensions. C-34 converts this empirically
proved independence into a binding preamble contract. An output can pass C-31+C-32+C-33 through
structural co-presence (as V-05 did) while no preamble declaration names their orthogonality;
C-34 closes that gap by requiring the declaration separately from the mechanism mapping rows of
C-17. Round 12 excellence signal.

**C-35 is the STRUCTURED CLOSE row cross-reference requirement**: C-31 tests that SE-4
references SE-0 TABLE_4 data; C-35 tests that this reference is specifically located within the
SE-4 STRUCTURED CLOSE block content and verified by a CA-1.9 row as a distinct audit target.
The precise location -- inside the STRUCTURED CLOSE, not in SE-4's analysis prose -- makes the
privilege-ceiling-to-gap-closure chain traceable at the CA audit row level. V-05's SE-4
STRUCTURED CLOSE carries the template instruction ("cite SE-0 TABLE_4 row ID") but no CA-1.9
row targets it independently, leaving the chain auditable only at the structural section level.
Round 12 excellence signal.

**C-36 is the tri-dimensional terminal attestation requirement**: C-22 tests that the execution
sequence is output-embedded for the CA-first dimension; C-36 tests that the CA terminal verdict
explicitly extends the self-evidence guarantee to all three R12 structural dimensions simultaneously
(execution order, closure-note format, CS self-reference), naming the specific output-body evidence
source for each. V-05 demonstrated that C-22+C-32+C-33 active simultaneously makes the output
tri-dimensionally self-evidencing -- a reader can verify all three dimensions from the output body
alone -- but C-36 tests that this property is explicitly declared in the CA terminal verdict rather
than only derivable by an evaluator who recognizes the combination. Round 12 excellence signal.
