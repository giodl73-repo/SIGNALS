Rubric v13 written to `simulations/quest/rubrics/discover-competitors-alt-rubric-v13-2026-03-17.md`.

---

**Three new criteria from R13 excellence signals:**

| ID | Criterion | Category | Source |
|----|-----------|----------|--------|
| C-47 | WRITE-TOKEN REGISTRY "Consumed by" column | behavior | V-01/V-04/V-05 — registry extended with consumption side; C-46 -> C-47 mirrors C-27 -> C-34 for OUTPUT CONTRACTS |
| C-48 | GATE 3 PATH-PRESENT row 0 before SOURCE-position check | format | V-02/V-04/V-05 — PATH absence independently named; applies declaration-before-execution to the gate validator itself |
| C-49 | Phase 5 COMPLETENESS row as structural tail validation | format | V-03/V-05 — Phase 5 ends with a named tail checkpoint; extends the GAP-CONFIRMED/THEREFORE final-row pattern to the findings phase |

**Scoring update (v12 -> v13):**

| | v12 | v13 |
|--|-----|-----|
| Aspirational count | 38 | 41 |
| Aspirational max | 190 | 205 |
| Max composite | 280 | 295 |
| Exceptional | >= 265 | >= 280 |
| Strong | >= 238 | >= 253 |

**Key dependency additions:**
- C-47 strictly stronger than C-46 (implies C-46; converse not true)
- C-48 independent of C-45 — requirement vs. enforcement surface; neither implies the other; both together align Phase 4 structure with its gate validator
- C-49 independent of C-37, C-36, C-45, C-38 — each targets a distinct phase or boundary
OUTPUT CONTRACTS: "Consumed by" is the token-lifecycle analogue of "Required by"; both make the consumption side machine-readable within PREFLIGHT
- C-48 is independent of C-45: C-45 targets Phase 4 structure (PATH row at row 0); C-48 targets GATE 3 validator structure (PATH-PRESENT check at row 0 before SOURCE-position check); neither implies the other; both together align the structural requirement and its gate enforcement
- C-49 is independent of C-37, C-36, and C-45: each applies to a distinct phase boundary; C-49 does not imply C-38 (AMEND table); C-38 does not imply C-49

---

## Essential Criteria (weight = 60 points total, 12 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Named competitors with threat levels | coverage | Output lists at least 3 named competitive alternatives (not categories, not generic "incumbent") including at least one status-quo option. Each named competitor must receive an explicit HIGH / MEDIUM / LOW threat rating. No competitor appears without a threat level. |
| C-02 | Inertia status quo (C0) identified | coverage | Output identifies the current status quo the user would abandon -- named and labeled as C0 or equivalent inertia anchor. This is the "do nothing" or "keep what I have" position, not a general market leader. C0 is distinct from other competitors and appears first or in a marked position. |
| C-03 | Threat level per competitor | coverage | Every competitor in the output -- including C0 and all external entries -- must receive an explicit HIGH / MEDIUM / LOW threat rating. No competitor appears without a threat level. |
| C-04 | Whitespace identified | coverage | Output names an uncontested space or gap that no listed competitor owns -- stated in its own finding or clearly labeled. |
| C-05 | Auto-detect without prompting | behavior | Topic domain is inferred from repo context (README, CLAUDE.md, package.json, etc.). Output does not ask the user to supply the domain or competitor names. |

---

## Recommended Criteria (weight = 30 points total, 10 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia stickiness reasoning | depth | Inertia section names at least one concrete mechanism -- switching cost, habit lock-in, or workaround satisfaction -- not just "inertia is high." The mechanism is specific to the status quo competitor's behavior or product feature, not a category label applied generically. |
| C-07 | Web-verified competitive claim | correctness | At least one named competitor characterization is supported by an inline citation (URL or publication) from a WebSearch result. The citation appears within the competitor entry, not in a trailing footnote block. |
| C-08 | AMEND section with 3 actionable adjustments | format | AMEND lists exactly 3 adjustments. Each names both what the user changes and what changes in the output as a result. |

---

## Aspirational Criteria (weight = 205 points total, 5 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional whitespace finding | depth | The whitespace finding names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus input -- it requires the competitive map and the focus dimension together. A finding that merely cites both dimensions without demonstrating that either alone is insufficient does not pass. |
| C-10 | Table-stakes grounding per finding | depth | Each item in the findings section references at least one named competitor row or map entry by label. No finding is free-floating prose that does not require the competitive analysis to support it. Positive instruction alone does not ensure this passes -- the output must demonstrate that ungrounded findings are absent. |
| C-11 | Fully-cited competitor table | correctness | Every external competitor row (not just one) includes an inline citation from a WebSearch result. The citation appears within the row or immediately adjacent entry -- not in a footnote or trailing references section. This extends C-07 from minimum-one to all-external. |
| C-12 | Self-negating cross-dimensional finding | depth | The CROSS-DIMENSIONAL or equivalent whitespace finding explicitly argues why the finding cannot be derived from the competitive map alone and why it cannot be derived from the focus dimension alone. The output provides or implies the single-dimension reduction for each -- showing what is lost when either dimension is removed -- rather than just asserting cross-dimensionality. |
| C-13 | Claim-level finding anchors | depth | Each finding references a specific cell value, column value, or row-level attribute from a named competitor entry -- not just the competitor name. Findings grounded only by competitor name ("Competitor X reveals...") do not satisfy; findings grounded by a specific claim within that row do. |
| C-14 | AMEND as proof validator | behavior | The AMEND section requires that any adjustment shifting the focus dimension must rerun both single-dimension reductions (C-12 proofs) for the updated CROSS-DIMENSIONAL finding. A standalone instruction to "update the finding" does not satisfy -- the explicit rerun of both reduction arguments must be prescribed. |
| C-15 | Inline anchor tag before proof block | format | The proof block or cross-dimensional finding structure declares a named evidentiary source slot (e.g., SOURCE:, ANCHOR:, or equivalent label) before the reduction arguments are written. The evidentiary source is identified first; the proof follows. Constructing the argument before naming the evidence does not satisfy. |
| C-16 | Gate failure naming | format | The skill instruction names the error condition explicitly (e.g., "gate failure," "citation gate violation," or equivalent) rather than only describing the rule in positive terms. Naming the failure state makes the gate concrete and checkable; a rule stated only as a positive requirement does not satisfy. |
| C-17 | WHITESPACE grounded by attribute absence | depth | The WHITESPACE finding grounds the identified gap by naming specific attributes from competitor rows that are absent or uncontested across the table -- not by assertion alone. The gap is evidenced by what is missing at the attribute level across named rows, not by a claim that no competitor owns the space. |
| C-18 | NOT ACCEPTABLE examples for anchoring | format | The skill instruction includes at least one explicit NOT ACCEPTABLE example that names the most common inadequate-but-compliant form -- such as name-only anchoring ("Competitor X reveals..."). The example must name the failure pattern specifically; an abstract prohibition without a concrete negative exemplar does not satisfy. |
| C-19 | Synthesis-first output contracts | behavior | At least one output slot requirement -- named by label (e.g., "WHITESPACE absence evidence," "ANCHOR column value") -- is stated within the data-collection phase instruction, not only at the synthesis phase. The collection phase must explicitly name what the downstream output slot requires from the data gathered, making the synthesis requirement visible before data is collected. Stating the output requirement only at the synthesis phase does not satisfy. |
| C-20 | Structural column coercion for anchoring | format | The skill instruction specifies a column format or structural template (e.g., `Row C{N}, {attribute}: "{value}"`) that makes name-only entries syntactically non-conforming without requiring rule evaluation. The constraint must be defined as a format shape for the column or slot. A prohibition-only instruction -- even accompanied by NOT ACCEPTABLE examples -- does not satisfy; the shape constraint must be structural. |
| C-21 | Gate-as-section with PASS/FAIL table | format | At least one gate is formatted as a named section containing a structured table with three distinct columns: Check, Pass condition, and Failure state (or equivalent labels). The table must enumerate at least two rows corresponding to distinct checkable conditions. A gate stated only in prose -- even with bolded failure names -- does not satisfy. Both the section heading and the columnar table structure must be present. |
| C-22 | INERTIA-REF per-finding citation | depth | The skill instruction defines a named inertia reference token (e.g., INERTIA-REF, C0-REF, or equivalent) in the inertia section and requires each finding in the findings section to cite or compare against that token by name. The token must function as a mandatory per-finding reference baseline; a definition without required per-finding citation does not satisfy. An inertia entry present only as a table row -- without a named token required across findings -- does not satisfy. |
| C-23 | Output contract slot format specification | behavior | At least one output contract slot specifies both a label and a required structural format or template for the value that fills it (e.g., label: "Anchor column", format: `Row C{N}, {attribute}: "{value}"`). A slot named by label only -- without a format shape for its value -- does not satisfy this criterion. Labeling is necessary; prescribing the format of what fills the slot is what satisfies. |
| C-24 | Phase-to-contract back-references | behavior | At least one phase that produces data for a named output contract slot explicitly names the slot it fills at the point of production (e.g., "(fills WHITESPACE absence evidence slot -- see OUTPUT CONTRACTS)"). The output contract must forward-declare the slot; the producing phase must back-reference it by the same label. A one-directional reference -- contract declaration only, or phase mention without a prior contract declaration -- does not satisfy. |
| C-25 | Cross-table structural coercion | format | Structural column coercion (as defined by C-20) is applied independently in at least two tables: one in the data-collection phase (e.g., competitor table Anchor column) and one in the synthesis or findings phase (e.g., findings table Anchor column or INERTIA-REF-DELTA column). Each table must define its own format template for its relevant column or slot. A single-table coercion -- even with multiple coerced columns within that table -- does not satisfy. The coercion must span the collection-to-synthesis boundary. |
| C-26 | Consolidated PREFLIGHT gate block | format | All mandatory gates are consolidated into a single named PREFLIGHT (or equivalent) section that appears before Phase 1 or before any execution phase. Each gate within the block must satisfy C-21 (named subsection with a PASS/FAIL table). Distributing gates across individual phases -- even if each gate individually satisfies C-21 -- does not satisfy this criterion. The PREFLIGHT block must be a single section containing all gate subsections. |
| C-27 | Machine-readable phase assignment in output contract | behavior | The output contract table includes a dedicated column (e.g., "Filled by phase" or equivalent) that names the producing phase for each slot by name or number. A 3-column contract table -- even one with format templates per slot (C-23) -- does not satisfy; the phase assignment must appear as a queryable column in the contract table itself. This makes the forward link from contract to phase machine-readable without reading any phase heading. |
| C-28 | OUTPUT CONTRACTS co-located within PREFLIGHT | format | The OUTPUT CONTRACTS declaration is a named subsection within the PREFLIGHT block -- not a separate section before or after it. All mandatory gates and all output contract slots must be readable from within the same PREFLIGHT section. A separate OUTPUT CONTRACTS section placed outside PREFLIGHT does not satisfy even if it immediately precedes Phase 1. This extends C-26 from gate consolidation to full execution-specification consolidation. |
| C-29 | Full-path back-reference labels in producing phases | behavior | Back-reference labels in producing phase headings name the complete navigable path to the contract declaration (e.g., "PREFLIGHT > OUTPUT CONTRACTS" rather than just "OUTPUT CONTRACT"). This criterion applies only when OUTPUT CONTRACTS is embedded within a containing section (i.e., C-28 is satisfied); a top-level OUTPUT CONTRACT section needs no path prefix. A back-reference naming the contract section without its containing section does not satisfy when the contract is nested. |
| C-30 | Write-token instruction within INERTIA-REF gate | behavior | The INERTIA-REF gate includes an explicit write instruction that directs the model to record the resolved token value at gate evaluation time (e.g., "Write INERTIA-REF = [specific mechanism phrase from C0 row]"). A gate that only checks for the presence or correctness of INERTIA-REF without a write directive does not satisfy. This criterion requires the gate itself to perform the token write -- binding token resolution to gate execution. |
| C-31 | Write-token encoded as structural gate row | format | The INERTIA-REF write instruction is a dedicated row within a PASS/FAIL gate table -- not prose placed before or after the table. The row has distinct Check, Pass condition, and Failure state values; the Pass condition contains the write directive and token format; the Failure state names the write failure explicitly (e.g., "Inertia write failure"). Prose write instructions adjacent to a gate table do not satisfy; the write action must be a structural table row independently reviewable at score time. C-31 is a strictly stronger form of C-30: C-31 satisfaction implies C-30; the converse is not true. |
| C-32 | OUTPUT CONTRACTS declared first within PREFLIGHT | behavior | OUTPUT CONTRACTS is the first named subsection within the PREFLIGHT block -- appearing before any gate subsection. The production target is fully declared before any constraint logic is read. A PREFLIGHT block where OUTPUT CONTRACTS follows one or more gates does not satisfy even if it remains within PREFLIGHT (C-28). C-32 is a strictly stronger form of C-28: C-32 satisfaction implies C-28; the converse is not true. |
| C-33 | Forward-declared cross-dimensional proof slot in output contract | behavior | The output contract table includes a dedicated slot that explicitly names the cross-dimensional proof requirement (e.g., "Focus-scope evidence," "Cross-dimensional justification," or equivalent). The slot must appear in the contract table by name before the producing phase runs; a requirement stated only within Phase 4's instruction does not satisfy. The slot makes the synthesis obligation visible at contract read time -- before data collection begins -- so Phase 4 knows at execution time that scope evidence is a required output, not an optional elaboration. This extends C-19 (synthesis-first contracts) and C-23 (slot format specification) to the cross-dimensional proof requirement specifically. |
| C-34 | Inter-slot dependency column in output contract | behavior | The output contract table includes a dedicated "Required by" column (or equivalent) that names, for each slot, the upstream slots or tokens on which it depends -- making the inter-slot dependency chain machine-readable at contract time without reading any phase instruction. A contract table with a phase-assignment column (C-27) but no inter-slot dependency column does not satisfy. A contract where downstream slot dependency is described only in prose or within phase headings does not satisfy. This criterion is independent of C-27: both columns may coexist; neither implies the other. |
| C-35 | Syntactic format template for cross-dimensional proof slot | behavior | The output contract slot for the cross-dimensional proof (e.g., "Focus-scope evidence") includes a full parse-ready format template -- such as a pipe-delimited or equivalent syntax specifying each required component with placeholder text (e.g., `REDUCTION-1 NO: [...] | REDUCTION-2 NO: [...] | THEREFORE: [...]`) -- rather than a structural description of components. A slot that names the required components without providing a syntactically checkable template does not satisfy. C-35 is a strictly stronger form of C-33: C-35 satisfaction implies C-33; the converse is not true. |
| C-36 | Cross-dimensional proof encoded as structural PASS/FAIL table | format | The cross-dimensional proof phase (Phase 4 or equivalent) is structured as a named PASS/FAIL table with at least four rows -- SOURCE, REDUCTION-1, REDUCTION-2, and THEREFORE (or equivalent labels) -- each with a required value format and a named failure state. A prose-instructed proof phase with code-block output format does not satisfy; the proof structure must itself be a gate table where each row is an independently reviewable checkpoint. C-36 is a strictly stronger form of C-15: SOURCE row position is enforced by table structure (first row), not by prose instruction; C-36 satisfaction implies C-15; the converse is not true. |
| C-37 | WHITESPACE validation phase as CANDIDATE-first PASS/FAIL table | format | The WHITESPACE validation phase (Phase 3 or equivalent) is structured as a named PASS/FAIL table with at least four rows -- CANDIDATE (gap declaration), SOURCE/EVIDENCE, ABSENCE-EVIDENCE (or equivalent per-row attribute evidence), and GAP-CONFIRMED (or equivalent conclusion row) -- each with a required value format and a named failure state. CANDIDATE is the first row by table position, declaring the gap before any supporting evidence is presented. This applies to Phase 3 the same declaration-before-evidence structural ordering that C-36 enforces in Phase 4 via SOURCE row position: CANDIDATE-first by table row order prevents selective evidence assembly (choosing evidence to fit a pre-concluded gap) in the same way SOURCE-first prevents circular proof construction. A prose-instructed whitespace phase or a code-block output format does not satisfy; the validation structure must itself be a gate table where each row is an independently reviewable checkpoint. C-37 is the Phase 3 analogue of C-36 applied to whitespace validation. |
| C-38 | AMEND as structured table with Slots re-filled and Gates re-run columns | format | The AMEND section is formatted as a structured table that includes at minimum the following columns: what the user changes, what changes in the output, Slots re-filled (naming the specific output contract slot(s) affected by the adjustment by their contract label), and Gates re-run (naming the specific gate(s) that must re-execute after the adjustment, including the proof rerun gate when focus shifts). A prose-structured AMEND section -- even one that explicitly lists 3 adjustments (C-08) and prescribes proof reruns on focus shifts (C-14) -- does not satisfy; both obligations must be verifiable by column inspection without prose parsing. C-38 satisfaction implies C-08 (adjustments are table rows naming cause and effect) and C-14 (proof rerun obligation is the Gates re-run column entry for focus-shift rows): the table structure enforces both constraints at the amendment boundary. |
| C-39 | EXECUTION DEPENDENCY table in PREFLIGHT | behavior | The PREFLIGHT block includes a named EXECUTION DEPENDENCY table (or equivalent) that specifies step-level execution ordering -- listing each execution step, its prerequisite steps, and the gate or phase it corresponds to. The table makes the step-level DAG of the skill machine-readable within PREFLIGHT, complementing C-34's slot-level "Required by" column: C-34 makes inter-slot dependency readable at the contract level; C-39 makes inter-step execution order readable at the PREFLIGHT level. GATE 4 (inertia assessment) must appear as the root step in the DAG -- a step with no prerequisites -- making inertia-first a structural property of the execution graph rather than a prose ordering convention. A PREFLIGHT block containing only output contracts and gate tables without an execution ordering table does not satisfy even if C-34 is satisfied. A prose-described execution order does not satisfy; the step ordering must appear as a queryable table. |
| C-40 | FOCUS GATE as named PASS/FAIL gate in PREFLIGHT | format | The FOCUS validation step is structured as a named PASS/FAIL gate subsection within the PREFLIGHT block -- not as a prose check placed before or outside PREFLIGHT. The gate must satisfy the same structural requirements as other PREFLIGHT gates: a named subsection heading plus a PASS/FAIL table with at least two independently reviewable rows (Check, Pass condition, Failure state). A "FOCUS CHECK" or equivalent prose block that precedes PREFLIGHT or appears outside the PREFLIGHT section does not satisfy even if it performs the same logical validation. The FOCUS gate must evaluate whether the focus dimension is user-supplied or requires inference, with each branch as a checkable gate row. C-40 satisfaction implies C-26 (all mandatory gates in PREFLIGHT) as applied to the FOCUS gate specifically: placing FOCUS outside PREFLIGHT distributes gates across sections and violates C-26. |
| C-41 | Phase 3 vs-INERTIA-REF row uses slot 6 ternary-token format | format | The vs-INERTIA-REF row within the Phase 3 WHITESPACE validation table requires its value to conform to the slot 6 ternary-token syntax -- specifying the relational verb as one of {reinforces, challenges, contextualizes} followed by a quoted mechanism phrase drawn from the INERTIA-REF token (e.g., `vs. INERTIA-REF -- challenges: "{mechanism phrase}"`). A prose comparison ("the whitespace finding challenges inertia because...") or an unformatted free-text description in the vs-INERTIA-REF row does not satisfy. This makes the Phase 3 inertia comparison syntactically checkable using the same format as the slot 6 output artifact, eliminating interpretation at the validation step boundary and closing the format gap between Phase 3 validation and slot 6 production. C-41 does not imply C-37; C-37 does not imply C-41. |
| C-42 | EXECUTION DEPENDENCY table includes explicit Prerequisite steps column | behavior | The EXECUTION DEPENDENCY table in PREFLIGHT includes a dedicated "Prerequisite steps" column (or equivalent) that names, for each execution step, the specific upstream steps it depends on -- making the DAG edges machine-readable by column inspection without reading step descriptions or inferring order from row position. A table where execution order is communicated by row sequence alone -- without a column explicitly naming prerequisites for each step -- does not satisfy. The root step (GATE 4) must carry an explicit "-- (root)" or equivalent marker in the Prerequisite steps column, confirming zero prerequisites by declaration rather than absence. C-42 is a strictly stronger form of C-39: C-39 requires the EXECUTION DEPENDENCY table to exist; C-42 requires that table to expose DAG edges as a dedicated queryable column. C-42 satisfaction implies C-39; the converse is not true. |
| C-43 | FOCUS-STATE declared as named output contract slot | behavior | The OUTPUT CONTRACTS table includes a dedicated slot for the focus-dimension resolution output (e.g., FOCUS-STATE as slot 0 or equivalent) -- making focus resolution a named, machine-readable output artifact with a declared format template, not a gate-only control flow decision. When GATE 0 (focus validation) produces control flow without a corresponding named output slot in the contract table, downstream slots that depend on the focus-path decision cannot name their dependency by slot number in the "Required by" column (C-34); the dependency can only be expressed as a gate reference rather than as a slot reference, yielding partial C-34 satisfaction for focus-dependent slots. When FOCUS-STATE is declared as a named slot in the output contract with a format template (e.g., `{user-supplied | inferred: [topic-domain]}`), the inter-slot dependency chain is complete: downstream slots (e.g., slot 5 Focus-scope evidence) can name "Requires slot 0 (FOCUS-STATE)" making the focus-path conditional dependency machine-readable at contract time without reading any gate description. A skill where GATE 0 writes a FOCUS-STATE token but no corresponding slot 0 appears in the OUTPUT CONTRACTS table does not satisfy; the slot must be declared in the contract table with a format template. C-43 is independent of C-40: C-40 requires the FOCUS validation to be structured as a named PASS/FAIL gate in PREFLIGHT; C-43 requires the FOCUS resolution to produce a named output slot in the OUTPUT CONTRACTS table. A skill can satisfy C-40 without C-43 (gate present, no slot declared) or C-43 without C-40 (slot declared, gate not structured as a named PREFLIGHT subsection). C-43 is a prerequisite for slot-level C-34 satisfaction on focus-dependent downstream slots; C-43 does not imply C-34 in general. |
| C-44 | Exhaustive "Reads slot" declaration including conditional reads | behavior | Every execution step that reads a slot value to branch, gate, or format its output -- including steps that conditionally include or exclude a column or field based on a slot value -- declares that slot in a "Reads slot" column or equivalent cell within the EXECUTION DEPENDENCY table. A step that conditionally branches on slot 0 (FOCUS-STATE) for column inclusion or output format selection must list slot 0 in its "Reads slot" declaration alongside any other slots it consumes; omitting a conditional read because the branch produces the same output on most paths does not satisfy. The full set of slot reads for each step -- unconditional and conditional -- must be reconstructable by column inspection of the EXECUTION DEPENDENCY table without reading any phase body or prose. A step where the "Reads slot" cell lists only the slots consumed on the non-conditional path, omitting slots that gate which output path is taken, yields an incomplete data-flow graph: the omitted read is a real dependency edge absent from the machine-readable representation. C-44 does not imply C-42: the Prerequisite steps column (C-42) captures step-level control dependencies; the Reads slot column captures slot-level data dependencies. Both columns may coexist; neither implies the other. C-44 is independent of C-43: C-43 requires FOCUS-STATE to be declared as a named contract slot; C-44 requires every step that reads FOCUS-STATE (or any other slot) to declare that read in the EXECUTION DEPENDENCY table. C-43 satisfaction is a prerequisite for C-44 to be satisfiable for focus-dependent steps: a step cannot declare a slot read if the slot has no contract entry to name. |
| C-45 | Phase 4 PATH row as structural branch router at row 0 | format | The cross-dimensional proof phase (Phase 4 or equivalent) begins with a PATH row as row 0 of the PASS/FAIL table -- before the SOURCE row -- that reads slot 0 (FOCUS-STATE) and declares both execution branches as independently reviewable table checkpoints: active path (proceed to SOURCE row) and inactive path (write `VACUOUS-5: focus-inactive` and exit the table). A Phase 4 table that begins directly at SOURCE -- even when the focus check is mentioned in a phase header or prose preamble -- does not satisfy; the branch decision must be a named table row with a required value, pass condition, and failure state that is independently reviewable before any evidentiary content is evaluated. This extends the declaration-before-execution principle established by C-37 (CANDIDATE-first in Phase 3) to Phase 4: the path declaration precedes the proof construction, making both the active and inactive execution branches independently checkable without reading phase header prose. A Phase 4 table with SOURCE as its first row satisfies C-36 (at least four rows including SOURCE, REDUCTION-1, REDUCTION-2, THEREFORE) but not C-45; the PATH row must appear before SOURCE as row 0. C-45 satisfaction implies C-36; C-36 satisfaction does not imply C-45. C-45 is the Phase 4 structural analogue of C-37's CANDIDATE-first row order; neither implies the other -- each applies to a distinct phase boundary. |
| C-46 | WRITE-TOKEN REGISTRY as first-class PREFLIGHT table | format | The PREFLIGHT block includes a dedicated WRITE-TOKEN REGISTRY table (or equivalent) that indexes all write-token events -- listing for each event the gate or step that writes the token, the token name, the output contract slot it corresponds to, and whether the write occurs pre-DAG (before Phase 1) or within the DAG execution sequence. The table appears after OUTPUT CONTRACTS and before the first gate subsection within PREFLIGHT, making the write-token schedule O(1)-discoverable without scanning EXECUTION DEPENDENCY rows or individual gate tables. A skill where write-token events are discoverable only by reading the EXECUTION DEPENDENCY table or individual gate tables does not satisfy; the write-token schedule must be independently indexed as a dedicated PREFLIGHT table. The WRITE-TOKEN REGISTRY completes a three-table PREFLIGHT specification: OUTPUT CONTRACTS (slot inventory and format), EXECUTION DEPENDENCY (step ordering and prerequisites), and WRITE-TOKEN REGISTRY (write-event schedule). C-46 satisfaction implies C-28 (OUTPUT CONTRACTS within PREFLIGHT); C-46 is independent of C-32: a WRITE-TOKEN REGISTRY placed after OUTPUT CONTRACTS but before GATE 0 preserves C-32 satisfaction (OUTPUT CONTRACTS remains first) provided WRITE-TOKEN REGISTRY is not itself classified as a gate subsection. C-46 is independent of C-31: C-31 requires the INERTIA-REF write instruction to be a structural gate row in the gate table; C-46 requires the full write-token schedule to be indexed as a separate PREFLIGHT registry table. C-31 satisfaction does not imply C-46; C-46 satisfaction does not imply C-31. |
| C-47 | WRITE-TOKEN REGISTRY "Consumed by" column for bidirectional lifecycle | behavior | The WRITE-TOKEN REGISTRY table (C-46) includes a dedicated "Consumed by" column (or equivalent) that names, for each write-token event, the phase(s) or step(s) that read the written token after it is produced. A registry table that lists only the writing gate, token name, slot, and pre-DAG/in-DAG classification -- but omits the consumption side -- does not satisfy; the full bidirectional lifecycle (written by X at time T, consumed by phases Y and Z) must be machine-readable by column inspection without reading any phase body. This extends C-46 from a write-schedule registry to a full token lifecycle registry. C-47 applies to the WRITE-TOKEN REGISTRY the same bidirectionality principle that C-34 applies to the OUTPUT CONTRACTS table: C-34 adds a "Required by" column to name downstream slot consumers; C-47 adds a "Consumed by" column to name downstream token consumers. The two columns address different tables but serve the same purpose: making the consumption side of each produced artifact machine-readable within PREFLIGHT. C-47 is a strictly stronger form of C-46: C-47 satisfaction implies C-46; C-46 satisfaction does not imply C-47. |
| C-48 | GATE 3 PATH-PRESENT row 0 before SOURCE-position check | format | The GATE 3 PASS/FAIL table -- which validates the structural integrity of Phase 4 -- includes a dedicated PATH-PRESENT check as its first independently reviewable row (row 0 or equivalent leading position) before any SOURCE-position or row-ordering checks. The PATH-PRESENT row must have a Check value confirming the PATH row exists as row 0 of the Phase 4 table, a Pass condition stating the PATH row is present at position 0, and a Failure state naming the PATH absence explicitly (e.g., "PATH absent failure" or equivalent). A GATE 3 table that begins with SOURCE-position as its first check -- detecting PATH absence only as a SOURCE-mislocation (SOURCE found at row 0 when PATH is absent) -- does not satisfy; the absence of the PATH row must be independently detectable as a named failure before any positional check on SOURCE or subsequent rows proceeds. This applies to GATE 3 the same declaration-before-execution principle that C-45 applies to Phase 4 (PATH row before SOURCE) and C-37 applies to Phase 3 (CANDIDATE row before ABSENCE-EVIDENCE): the first checkpoint confirms the required structural element exists before any row evaluates its position or content. C-48 is independent of C-45: C-45 requires Phase 4 to have a PATH row at row 0; C-48 requires GATE 3 to independently confirm PATH presence as its first check, making PATH absence a named, independently reviewable failure before SOURCE-position analysis runs. A skill can satisfy C-45 (Phase 4 has a PATH row) without C-48 (GATE 3 detects PATH absence via SOURCE mislocation rather than a dedicated PATH-PRESENT check), and a skill can satisfy C-48 without satisfying C-45 if GATE 3 performs the PATH-PRESENT check but the Phase 4 table itself places PATH after SOURCE. Both together ensure the structural requirement (Phase 4 PATH at row 0, C-45) and its gate enforcement (GATE 3 PATH-PRESENT at row 0, C-48) are aligned. |
| C-49 | Phase 5 COMPLETENESS row as structural tail validation | format | Phase 5 (or the findings synthesis phase) includes a COMPLETENESS row (or equivalent named tail checkpoint) as the final row of its structured output table, with a Check confirming that all required per-finding elements are present across the complete findings set, a Pass condition naming the specific completeness requirements (e.g., every finding has an Anchor column value in the structural format; every finding carries an INERTIA-REF citation in ternary-token format), and a Failure state naming the aggregate validation failure explicitly (e.g., "Findings completeness failure" or equivalent). A findings phase that ends with the last finding row without a structural tail checkpoint does not satisfy; the completeness validation must be a named, independently reviewable table row -- not a prose post-hoc review instruction, a gate that precedes the findings phase, or a gate that follows Phase 5 as a separate section. The COMPLETENESS row makes Phase 5 self-validating: the phase both produces findings and confirms their collective completeness within the same table, eliminating a separate aggregate review gate. C-49 is independent of C-37 (Phase 3 structure), C-36 (Phase 4 structure), and C-45 (Phase 4 PATH row): each applies to a distinct phase; none implies the other. C-49 is independent of C-38 (AMEND structured table): C-38 makes the amendment boundary checkable; C-49 makes the initial findings production checkable at its tail. A skill can satisfy C-38 without C-49 (amendments are structured but findings have no tail validation) and vice versa. |

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-49 | 5 | 205 |
| **Max composite** | | | **295** |

**Composite formula:**
```
composite = (essential_pass / 5 x 60)
          + (recommended_pass / 3 x 30)
          + (aspirational_pass / 41 x 205)
```

PARTIAL scores count as 0.5 for numerator purposes.

**Golden threshold:** All 5 essential pass AND composite >= 90

**Grade bands:**

| Score | Grade |
|-------|-------|
| 280 -- 295 | Exceptional |
| 253 -- 279 | Strong |
| 90 -- 252 | Passing |
| < 90 | Below bar |

Grade bands rescaled proportionally from v12 (v12 max = 280; v13 max = 295).
Exceptional threshold preserved at ~95% of max; Strong threshold at ~86% of max; Passing at golden threshold (90).

---

## Dependency Notes

- C-28 automatically satisfies C-26 (superset); C-29 requires C-28 (N/A otherwise)
- C-30 automatically satisfies C-22
- C-31 automatically satisfies C-30 (and therefore C-22)
- C-32 automatically satisfies C-28 (and therefore C-26)
- C-32 + C-28 together do not require C-29; full-path back-references remain a distinct criterion
- C-33 extends C-19 and C-23 to the cross-dimensional slot specifically; C-33 does not imply C-19 or C-23 in general
- C-35 automatically satisfies C-33; C-35 does not imply C-23 in general (C-23 may be satisfied by other slots)
- C-36 automatically satisfies C-15; C-36 does not imply C-21 in general (C-21 may be satisfied by other gate tables)
- C-34 independent of C-27: both are dedicated contract columns; neither implies the other
- C-37 is the Phase 3 structural analogue of C-36 (Phase 4); neither implies the other -- each applies to a distinct phase
- C-38 automatically satisfies C-08 and C-14; C-38 does not imply C-35 (slot format constraint is a contract-level obligation, not an AMEND-level one)
- C-39 complements C-34: C-34 is slot-level (output contract table), C-39 is step-level (execution DAG table); neither implies the other
- C-40 satisfaction implies C-26 applied to the FOCUS gate; C-40 is independent of C-37, C-38, C-39
- C-41 independent of C-37: C-37 targets Phase 3 table structure; C-41 targets the vs-INERTIA-REF row value format; neither implies the other
- C-42 automatically satisfies C-39; C-39 does not imply C-42
- C-43 independent of C-40: C-40 is about FOCUS gate structure in PREFLIGHT; C-43 is about FOCUS-STATE output slot in OUTPUT CONTRACTS; neither implies the other
- C-43 is a prerequisite for complete slot-level C-34 satisfaction on focus-dependent slots; C-43 does not imply C-34 in general
- C-44 independent of C-42: C-42 captures step-level control dependencies (Prerequisite steps column); C-44 captures slot-level data reads per step (Reads slot column); both may coexist in the EXECUTION DEPENDENCY table; neither implies the other
- C-44 is independent of C-43; C-43 satisfaction is a practical prerequisite for C-44 satisfiability on focus-dependent steps (a step cannot declare a slot read for a slot with no contract entry)
- C-45 automatically satisfies C-36; C-36 does not imply C-45 (PATH row as row 0 before SOURCE is a strictly stronger constraint than SOURCE present among at least four rows)
- C-45 is the Phase 4 structural analogue of C-37; neither implies the other -- each targets a distinct phase boundary
- C-46 automatically satisfies C-28; C-46 is independent of C-32 (WRITE-TOKEN REGISTRY between OUTPUT CONTRACTS and GATE 0 preserves OUTPUT CONTRACTS-first ordering); C-46 is independent of C-31 (gate-row write vs. PREFLIGHT registry table are distinct structural surfaces)
- C-47 automatically satisfies C-46; C-46 does not imply C-47 (write schedule without consumption side does not satisfy C-47)
- C-47 applies to WRITE-TOKEN REGISTRY the same bidirectionality that C-34 applies to OUTPUT CONTRACTS: "Consumed by" is the token-lifecycle analogue of "Required by"; both make the consumption side machine-readable within PREFLIGHT
- C-48 independent of C-45: C-45 targets Phase 4 structure (PATH row at row 0); C-48 targets GATE 3 structure (PATH-PRESENT check at row 0 before SOURCE-position check); neither implies the other; both together align the structural requirement and its gate enforcement
- C-49 independent of C-37, C-36, C-45: each applies to a distinct phase; C-49 independent of C-38: C-38 governs the amendment boundary; C-49 governs the tail of the initial findings production

---

## Criterion Rationale (v2 additions)

**Why C-11 (Fully-cited table) over C-07 alone:**
Round 1 showed that requiring one citation is insufficient -- models satisfy C-07 with a single
verified claim and coast on unverified characterizations for all other rows. C-11 closes this
gap: WebSearch must be run per external competitor, not just once.

**Why C-12 (Self-negating cross-dimensional finding):**
C-09 scored PARTIAL in every variation across Round 1. The common failure: variations required
the finding to cite both dimensions but not to prove single-dimension insufficiency. C-12 makes
the exclusion test explicit and output-level -- the finding must demonstrate what is lost when
either dimension is removed, not merely assert it draws on both.

**Why C-13 (Claim-level anchors) over C-10 alone:**
C-10 requires findings to name a competitor row. C-13 requires findings to name a specific
claim within that row -- a threat rating, mechanism sentence, or focus-column value. The upgrade
matters because "Competitor X reveals a gap" is technically grounded but epistemically empty:
the reader cannot verify the inference without re-reading the full row. Claim-level anchors make
inferences checkable in one glance.

---

## Criterion Rationale (v3 additions)

**Why C-14 (AMEND as proof validator):**
V-05 (Round 2) showed that encoding C-12 in the static CROSS-DIMENSIONAL block is insufficient
if AMEND allows the user to shift the focus dimension without re-running both reductions. The
proof degrades silently after adjustment. Requiring AMEND to prescribe the full reduction rerun
propagates C-12 compliance across every iteration, not just the initial invocation.

**Why C-15 (Inline anchor tag before proof block):**
Round 2 analysis showed that models construct reduction proofs first and name evidence
incidentally -- or not at all. Declaring a named SOURCE or ANCHOR slot before the argument
forces the evidentiary basis to be resolved before the proof is assembled. This prevents
circular proof construction where the conclusion implicitly selects its own evidence.

**Why C-16 (Gate failure naming):**
Positive-only rule framing leaves the error state implicit. When a gate is violated, the model
has no named failure mode to report against. Naming the failure state explicitly makes gates
self-enforcing: the model can produce a structured error rather than silently violating the rule.

**Why C-17 (WHITESPACE grounded by attribute absence):**
C-04 requires the whitespace finding to exist. C-13 requires findings to anchor to specific
attributes. C-17 applies claim-level anchoring specifically to the WHITESPACE finding: the gap
must be shown to be vacant by naming which attributes across which rows confirm no competitor
owns it. Asserting "no competitor covers this space" without attribute-level evidence is the
WHITESPACE analogue of the name-only anchoring failure.

**Why C-18 (NOT ACCEPTABLE examples):**
V-03 and V-05 (Round 2) showed that ACCEPTABLE/NOT ACCEPTABLE example pairs are the single most
reliable mechanism for eliminating the name-only anchoring escape hatch. Abstract prohibitions
are consistently interpreted as satisfied by naming the competitor. A NOT ACCEPTABLE example
naming the exact inadequate form closes the interpretation gap.

---

## Criterion Rationale (v4 additions)

**Why C-19 (Synthesis-first output contracts):**
R4 V-01 and V-04 showed that declaring output slot requirements at data-collection time changes
what gets collected. When the instruction names "WHITESPACE absence evidence" as a required
output slot during Phase 3 collection, the collection step is automatically cued to gather
per-attribute absence data. When the requirement is only stated at synthesis time, the model
must backfill or fabricate what it failed to collect.

**Why C-20 (Structural column coercion for anchoring):**
R4 V-02 demonstrated the most adversarially robust C-13 mechanism: an Anchor column defined
with format `Row C{N}, {attribute}: "{value}"`. This format makes name-only entries
syntactically incorrect before any rule evaluation occurs. Prohibition instructions and NOT
ACCEPTABLE examples can be satisfied with a single compliant example while allowing
non-compliant cases to pass. A structural format constraint eliminates the escape entirely.

**Why C-21 (Gate-as-section with PASS/FAIL table):**
R4 V-04 showed that gate-as-section with a three-column PASS/FAIL table produces the most
debuggable skill structure: each gate condition becomes a checklist row with an unambiguous pass
condition and a named failure state. Tabular gates are directly executable as a review checklist
without interpretation.

**Why C-22 (INERTIA-REF per-finding citation):**
R4 V-03 and V-05 showed that naming an INERTIA-REF token and requiring each finding to cite it
elevates inertia from a first-row table entry to a gravitational reference frame. Without the
per-finding requirement, inertia is assessed once and then ignored during synthesis. With a
mandatory INERTIA-REF comparison per finding, every competitive inference is measured against
the status quo cost rather than against other external competitors.

---

## Criterion Rationale (v5 additions)

**Why C-23 (Output contract slot format specification):**
R5 V-04 showed that an output contract table where each slot has both a label and a required
format shape is fundamentally stronger than a label-only contract. A label-only slot tells the
producing phase what to collect; a format-specified slot tells it what shape the collection
must take. This upgrades the contract from a reminder to a machine-checkable constraint: a slot
filled in the wrong format is detectable without prose parsing, in the same way C-20's
structural coercion makes name-only cells detectable without rule evaluation.

**Why C-24 (Phase-to-contract back-references):**
R5 V-01 and V-04 showed that when the producing phase explicitly names the output contract slot
it fills, the collection-to-synthesis dependency becomes traceable in both directions. A
forward-only contract can drift: the phase may collect something that does not actually satisfy
the declared slot. When the phase back-references the slot by name, the constraint is active at
the moment of production, not only at synthesis time.

**Why C-25 (Cross-table structural coercion):**
R5 V-02 and V-05 showed that structural column coercion applied to both the competitor table
and the findings table eliminates the most common compliance gap: collecting claim-level anchor
values correctly but then re-stating them as name-only anchors in the findings. C-20 prevents
name-only anchoring at collection time; C-25 ensures the same constraint is enforced at
synthesis time, closing the round-trip escape.

**Why C-26 (Consolidated PREFLIGHT gate block):**
R5 V-03 showed that consolidating all gates into a single PREFLIGHT section before Phase 1
produces a skill that can be audited without reading the full phase sequence. A consolidated
PREFLIGHT block exposes all gates simultaneously: the model or a human reviewer can run the
complete gate checklist before any execution phase begins.

---

## Criterion Rationale (v6 additions)

**Why C-27 (Machine-readable phase assignment in output contract):**
R6 V-02, V-04, and V-05 showed that adding a "Filled by phase" column to the output contract
table completes the bidirectionality introduced by C-24 at the contract level itself. A
4-column contract table makes the phase assignment queryable from the contract alone: given any
slot, you can determine which phase is responsible without reading any phase heading.
Contract -> phase (C-27) complements phase -> contract (C-24).

**Why C-28 (OUTPUT CONTRACTS co-located within PREFLIGHT):**
R6 V-03 and V-05 showed that embedding OUTPUT CONTRACTS as a subsection within PREFLIGHT
produces the tightest possible front-loading. When gates and output contract slots are in the
same section, a single read of PREFLIGHT exposes the complete execution specification: what is
checked (gates), what is produced (output slots), what format it must take (C-23), and which
phase produces it (C-27). This extends C-26 from gate consolidation to full specification
consolidation: PREFLIGHT becomes the single source of truth for the skill.

**Why C-29 (Full-path back-reference labels in producing phases):**
R6 V-03 and V-05 showed that when OUTPUT CONTRACTS is nested within PREFLIGHT (C-28), a
back-reference label of "OUTPUT CONTRACT" alone is ambiguous. The full-path label
"PREFLIGHT > OUTPUT CONTRACTS" provides a navigable pointer: the reader knows to enter
PREFLIGHT and then locate the OUTPUT CONTRACTS subsection. When contracts are nested, the
path prefix is the difference between a navigable pointer and an unanchored name.

**Why C-30 (Write-token instruction within INERTIA-REF gate):**
R6 V-04 and V-05 showed that including an explicit write instruction within GATE 4 binds
INERTIA-REF token resolution to gate execution rather than treating it as a precondition. C-22
requires the token to be defined and per-finding cited; without C-30, the definition can float
in the inertia section while the gate merely checks for it. When the gate itself contains a
write instruction, the token is actively produced at the gate evaluation step rather than
passively checked. A gate that passes must have written the token, making the subsequent
per-finding citations (C-22) have a guaranteed referent.

---

## Criterion Rationale (v7 additions)

**Why C-31 (Write-token encoded as structural gate row):**
R7 V-03 and V-05 showed that encoding the INERTIA-REF write instruction as a dedicated
PASS/FAIL table row is categorically stronger than prose adjacent to the table. A prose write
directive can be read as guidance and skipped; a table row with a named Check, Pass condition,
and Failure state ("Inertia write failure") is independently reviewable at score time without
reading surrounding prose. The write action cannot be separated from gate logic when it occupies
its own table row: a reviewer scanning the gate table sees the write row as a discrete
checkpoint, not a contextual note. This is the same insight that motivates C-21 over C-16 --
structure makes rules checkable without interpretation. C-31 is a strictly stronger form of
C-30; it satisfies C-30 but not vice versa.

**Why C-32 (OUTPUT CONTRACTS declared first within PREFLIGHT):**
R7 V-02 and V-05 showed that placing OUTPUT CONTRACTS as the first subsection in PREFLIGHT --
before any gate logic -- changes the cognitive model under which gates are evaluated. When the
contract is declared first, every subsequent gate is framed as a precondition for fulfilling a
known production obligation: the gate's write action (C-30, C-31) resolves a forward-declared
slot rather than producing a token ad hoc. When OUTPUT CONTRACTS follows one or more gates, the
production target is discovered only after some constraints have already been applied, reversing
the specification-before-constraint order that motivates C-19, C-23, C-24, C-26, C-27, and
C-28. Spec-first PREFLIGHT is the final closure of this design principle at the section level:
the contract is not just inside PREFLIGHT (C-28) but is the first thing read within it. C-32 is
a strictly stronger form of C-28; it satisfies C-28 but not vice versa.

**Why C-33 (Forward-declared cross-dimensional proof slot in output contract):**
R7 V-05 showed that including a dedicated "Focus-scope evidence" slot in the output contract
makes the cross-dimensional proof requirement visible at contract read time, before Phase 4
runs. Without an explicit slot, the scope evidence requirement is discoverable only by reading
Phase 4's instruction -- making it a synthesis-phase surprise rather than a collection-time
obligation. When the contract names the slot, Phase 4 knows before it runs that scope evidence
is a required output with a defined format, not an optional elaboration. This extends C-19
(synthesis-first contracts) to the cross-dimensional proof specifically, and extends C-23 (slot
format specification) to close the last unspecified output slot. The 6th-slot pattern also
interacts with C-27: when the contract includes a "Filled by phase" column, the Phase 4
assignment for the Focus-scope evidence slot makes the cross-dimensional proof obligation fully
machine-readable at the contract level.

---

## Criterion Rationale (v8 additions)

**Why C-34 (Inter-slot dependency column in output contract):**
R8 V-01 and V-04 showed that adding a "Required by" column to the output contract table
exposes the token dependency chain (INERTIA-REF as root slot -> Focus-scope evidence slot 5 ->
INERTIA-REF-DELTA slot 6) without reading any phase instruction. A contract with only a
"Filled by phase" column (C-27) tells you who produces each slot but not which downstream slots
depend on it. When the "Required by" column is present, a reviewer can identify the blast radius
of a gate failure at contract read time: if INERTIA-REF is not written, slots 5 and 6 are
immediately known to be at risk. This makes inter-slot dependency a first-class property of the
contract specification rather than an inference from reading the full phase sequence.
C-34 is orthogonal to C-27: "Filled by phase" names the producer; "Required by" names the
dependents. Both columns may coexist in the same contract table; neither implies the other.

**Why C-35 (Syntactic format template for cross-dimensional proof slot):**
R8 V-02 showed that the pipe-delimited format template for slot 5 (`REDUCTION-1 NO: [...] |
REDUCTION-2 NO: [...] | THEREFORE: [...]`) is syntactically checkable in a way that a
structural description ("SOURCE row + REDUCTION-1 row + REDUCTION-2 row + THEREFORE row") is
not. A structural description names the required components and their order; a syntactic
template provides a parse-ready skeleton where a non-conforming fill is detectable by pattern
match rather than by semantic interpretation. The distinction matters at score time: checking
whether a slot value matches `REDUCTION-1 NO: [...] | ...` requires no judgment; checking
whether it contains "all four required components" does. C-35 is a strictly stronger form of
C-33: C-33 requires the slot to exist by name; C-35 requires the slot to also have a
syntactically checkable format. C-35 does not imply C-23 in general -- other slots may satisfy
C-23 independently of whether C-35 is satisfied for slot 5.

**Why C-36 (Cross-dimensional proof encoded as structural PASS/FAIL table):**
R8 V-03 and V-04 showed that restructuring Phase 4 as a 4-row PASS/FAIL table -- SOURCE row,
REDUCTION-1 row, REDUCTION-2 row, THEREFORE row -- transforms the proof from a prose-guided
construction into an independently reviewable checklist. When Phase 4 is a code-block proof,
SOURCE position is enforced by instruction ("declare SOURCE before arguments"); when Phase 4 is
a PASS/FAIL table, SOURCE position is enforced by table row order -- the first row is the
SOURCE row, and any other ordering is structurally malformed. This is the same insight that
motivates C-21 over C-16 (tabular gate rows over prose gates) and C-31 over C-30 (write
directive as table row over prose directive): structural position enforces ordering without
requiring rule evaluation. C-36 is a strictly stronger form of C-15: C-15 requires SOURCE to be
declared before the proof arguments; C-36 requires SOURCE to be the first row of a table whose
subsequent rows are the proof arguments, each with a required value format and a named failure
state. C-36 satisfaction implies C-15; a skill satisfying C-15 via a code-block proof does not
satisfy C-36.

---

## Criterion Rationale (v9 additions)

**Why C-37 (WHITESPACE validation phase as CANDIDATE-first PASS/FAIL table):**
R9 V-01, V-04, and V-05 showed that structuring Phase 3 as a CANDIDATE-first PASS/FAIL table
applies to whitespace validation the same structural insight that C-36 applies to the
cross-dimensional proof in Phase 4. The core vulnerability in prose-instructed whitespace phases
is selective evidence assembly: the model concludes a gap exists and then finds attributes that
support it, discarding attributes that complicate the finding. When CANDIDATE is the first row
of a table -- forced to be declared before any ABSENCE-EVIDENCE or GAP-CONFIRMED rows can be
filled -- the gap candidate is fixed before evidence is presented. A prose instruction to
"declare your candidate first" can be satisfied by re-ordering two sentences; a table where
CANDIDATE is row 1 makes any other ordering structurally malformed. C-37 is the Phase 3
analogue of C-36: the same declaration-before-evidence principle applied to whitespace
validation instead of cross-dimensional proof. Neither implies the other; each targets a
distinct phase boundary.

**Why C-38 (AMEND as structured table with Slots re-filled and Gates re-run columns):**
R9 V-02, V-04, and V-05 showed that encoding the AMEND section as a structured table with
"Slots re-filled" and "Gates re-run" as queryable columns elevates the amendment boundary to
the same structural level as the output contract. C-08 requires 3 adjustments, each naming
cause and effect; C-14 requires proof reruns on focus shifts. Both can be satisfied in prose
with careful wording -- but at score time, verifying C-08 and C-14 compliance requires reading
and interpreting the prose for each adjustment. When AMEND is a table with a "Gates re-run"
column, C-14 compliance is checkable by scanning the column for focus-shift rows: if the entry
is blank or names only output updates, the violation is immediately visible. Similarly, the
"Slots re-filled" column makes the output contract implication of each adjustment queryable
without prose parsing. This closes the amendment escape hatch: a user cannot shift the focus
dimension and satisfy C-08 without the "Gates re-run" column exposing the required proof rerun.
C-38 satisfaction implies C-08 and C-14 because the columnar structure enforces both at the
table level. C-38 is the amendment-lifecycle analogue of C-27 (output contract phase column)
and C-21 (gate tables): structured columns replace prose enforcement at a new boundary.

**Why C-39 (EXECUTION DEPENDENCY table in PREFLIGHT):**
R9 V-03 and V-05 showed that adding an EXECUTION DEPENDENCY table to PREFLIGHT completes
PREFLIGHT as a full execution specification. C-34 makes inter-slot dependencies machine-readable
at the contract level: given a slot, you know which downstream slots depend on it. C-39 makes
inter-step execution order machine-readable at the DAG level: given a step, you know which
steps must complete before it and which steps it unblocks. The two tables are complementary and
non-redundant -- C-34 is a data dependency graph (output slots), C-39 is a control dependency
graph (execution steps). The critical structural property C-39 introduces is GATE 4 as root
step (no prerequisites): this makes inertia-first not merely a prose ordering convention but a
DAG property enforced by the table. Any execution plan that runs a phase before GATE 4 is
structurally non-conforming relative to the DAG, not merely in violation of a prose rule.
With C-39 satisfied, PREFLIGHT contains: output slot declarations (C-32, OUTPUT CONTRACTS
first), slot dependency chain (C-34, "Required by" column), slot producers (C-27, "Filled by
phase" column), gate constraints (C-26, gate subsections), and step ordering (C-39, EXECUTION
DEPENDENCY table) -- making PREFLIGHT a complete and machine-readable execution specification
without reading any phase body.

---

## Criterion Rationale (v10 additions)

**Why C-40 (FOCUS GATE as named PASS/FAIL gate in PREFLIGHT):**
R10 V-01, V-04, and V-05 showed that structuring the FOCUS validation step as a named PASS/FAIL
gate within PREFLIGHT closes the last gate that remained as prose in prior variations. V-02 and
V-03 placed FOCUS CHECK as a prose block before the PREFLIGHT section, which means PREFLIGHT
does not contain a complete gate inventory: a reviewer reading only PREFLIGHT cannot audit all
constraints without also reading any pre-PREFLIGHT prose. When FOCUS is a named gate subsection
inside PREFLIGHT, the constraint set is fully visible within the section boundary. This is the
same insight that motivates C-26 (all gates in PREFLIGHT) applied specifically to the FOCUS
validation step: FOCUS outside PREFLIGHT distributes the gate surface across sections, requiring
full-document reads to audit correctness. C-40 is the structural analogue of C-26 applied to
the one gate that C-26 alone does not force inside PREFLIGHT when prose alternatives exist.

**Why C-41 (Phase 3 vs-INERTIA-REF row uses slot 6 ternary-token format):**
R10 V-02, V-04, and V-05 showed that applying the slot 6 ternary-token format (`vs. INERTIA-REF
-- {reinforces|challenges|contextualizes}: {phrase}`) to the vs-INERTIA-REF row in Phase 3
eliminates a format discontinuity between the validation step and its output artifact. When the
Phase 3 table row uses prose ("the finding challenges inertia because..."), the relationship is
interpretable but not checkable by pattern match. When the same row uses the ternary-token
format, the comparison is syntactically aligned with slot 6 output: a reviewer can verify the
inertia comparison in Phase 3 using the same format rule applied to the final output, making
the Phase 3 gate and the slot 6 production contract mutually reinforcing. V-01 and V-03 used
prose comparison in the vs-INERTIA-REF row -- satisfying C-37 (Phase 3 is a PASS/FAIL table)
but leaving the inertia comparison value unstructured. C-41 closes this remaining format gap at
the row-value level within an already-structured table. The ternary-token constraint at Phase 3
is the same principle that motivates C-35 at the contract level: syntactic checkability
eliminates interpretation at review time.

**Why C-42 (EXECUTION DEPENDENCY table includes explicit Prerequisite steps column):**
R10 V-03 and V-05 showed that adding a dedicated "Prerequisite steps" column to the EXECUTION
DEPENDENCY table makes DAG edges machine-readable without inferring them from row position or
step descriptions. C-39 requires the table to exist and GATE 4 to appear as a root step; it
does not require the prerequisite relationship to be a queryable column. Variations V-01, V-02,
and V-04 had EXECUTION DEPENDENCY tables (satisfying C-39) but communicated step ordering
through row sequence alone -- meaning the DAG structure was readable but not queryable by
column. When a "Prerequisite steps" column is present, the dependency relationship for each
step is a cell value: GATE 4 shows "-- (root)" confirming zero prerequisites by declaration;
downstream steps show the specific steps they wait on. This makes the DAG edges first-class
data within the table rather than implicit in its structure. C-42 is to C-39 what C-34 is to
C-27: both add a dependency column to an existing structural table, upgrading the table from a
producer/sequence declaration to a full dependency graph. C-42 is a strictly stronger form of
C-39; it satisfies C-39 but not vice versa.

---

## Criterion Rationale (v11 additions)

**Why C-43 (FOCUS-STATE declared as named output contract slot):**
R11 V-01, V-04, and V-05 showed that declaring FOCUS-STATE as a named output slot (slot 0) in
the OUTPUT CONTRACTS table completes the C-34 "Required by" dependency chain for
focus-dependent downstream slots. V-02 and V-03 structured GATE 0 as a focus validation gate
that produced control flow but no named output slot in the contract table. As a result, slot 5
(Focus-scope evidence) could only name its upstream dependency as a gate reference ("Requires
GATE 0") rather than a slot reference ("Requires slot 0 (FOCUS-STATE)"), yielding PARTIAL
satisfaction of C-34 for those variations. When FOCUS-STATE is declared as slot 0 with a format
template, the full dependency chain becomes slot-addressable: slot 5's "Required by" column can
name slot 0 by number, making the focus-path conditional dependency machine-readable at contract
time using the same mechanism as other inter-slot dependencies. The insight is analogous to the
one motivating C-34 itself: C-34 requires a "Required by" column so that slot dependencies are
queryable; C-43 requires that the FOCUS resolution output be a named slot so that
focus-dependent slots have a slot number to name in that column. Gate references in the
"Required by" column are a partial solution -- they identify the upstream condition but cross
a type boundary (gate vs. slot) that breaks the uniformity of the dependency graph. Declaring
FOCUS-STATE as slot 0 closes this type boundary: every entry in the "Required by" column is a
slot reference, making the dependency graph fully uniform and queryable by slot number alone.
C-43 is independent of C-40: a skill can have a FOCUS gate in PREFLIGHT (C-40) without a
FOCUS-STATE output slot in the contract (C-43 fails), or declare a FOCUS-STATE slot without
structuring the validation as a named PASS/FAIL gate (C-43 without C-40). Together, C-40 and
C-43 close both surfaces: C-40 ensures focus validation is a first-class gate; C-43 ensures
focus resolution is a first-class output slot.

---

## Criterion Rationale (v12 additions)

**Why C-44 (Exhaustive "Reads slot" declaration including conditional reads):**
R12 V-01, V-04, and V-05 showed that Phase 2 conditionally branches on slot 0 (FOCUS-STATE)
to determine whether a Focus column appears in the competitor table -- a real data-flow edge
that was omitted from the "Reads slot" declaration in R11 V-05. V-01, V-04, and V-05 add
`0 -- FOCUS-STATE (Focus column inclusion)` to Phase 2's "Reads slot" cell alongside slot 1,
making the conditional read explicit. The missing read is not a minor gap: when a phase
branches on a slot value to decide what output to produce, that slot is a genuine input to the
phase. Omitting it from the "Reads slot" column means the EXECUTION DEPENDENCY table's
data-flow graph is incomplete -- a reader cannot reconstruct the full set of slot dependencies
from column inspection alone. The rule is precise: every step that reads a slot to decide
anything (column inclusion, output format, branch path) must declare it. This is the slot-level
analogue of C-42's insistence that every control dependency be a queryable column entry: just
as C-42 requires prerequisite steps to be declared as data rather than implied by row order,
C-44 requires slot reads to be declared as data rather than implied by reading phase bodies.
C-44 is independent of C-42 (control vs. data dependencies) and of C-43 (whether FOCUS-STATE
is a named slot vs. whether its reads are declared): both must be satisfied together for the
EXECUTION DEPENDENCY table to be a complete, machine-readable data-flow specification.

**Why C-45 (Phase 4 PATH row as structural branch router at row 0):**
R12 V-02, V-04, and V-05 showed that adding a PATH row as row 0 of the Phase 4 PASS/FAIL table
-- before SOURCE -- applies to the proof phase the same declaration-before-execution principle
that C-37 established for Phase 3 (CANDIDATE-first). Without a PATH row, the active/inactive
branch decision for Phase 4 is made implicitly: the phase header indicates that focus-inactive
invocations skip Phase 4, but this branch logic is not a named, independently reviewable table
checkpoint. A reviewer reading the Phase 4 table alone cannot determine the skip condition
without reading the phase header. When PATH is row 0, both execution branches are declared
within the table itself: active path (proceed to SOURCE) and inactive path (write
`VACUOUS-5: focus-inactive` and exit) are independently checkable without prose. This closes
the last remaining declaration-before-execution gap in the two high-stakes phases: C-37
established CANDIDATE-first for whitespace validation (Phase 3); C-45 establishes PATH-first
for cross-dimensional proof (Phase 4). The insight is structural: SOURCE as row 1 is a valid
Phase 4 table satisfying C-36; PATH as row 0 before SOURCE is a strictly stronger constraint
that makes the branch decision a first-class table checkpoint rather than a phase-header
implication. V-01 and V-03 satisfied C-36 (SOURCE present among four rows) but not C-45 (no
PATH row before SOURCE). C-45 satisfaction implies C-36; the converse is not true.

**Why C-46 (WRITE-TOKEN REGISTRY as first-class PREFLIGHT table):**
R12 V-03 and V-05 showed that adding a dedicated WRITE-TOKEN REGISTRY table to PREFLIGHT --
after OUTPUT CONTRACTS and before GATE 0 -- completes PREFLIGHT as a three-table execution
specification. Prior variations exposed write-token events only via EXECUTION DEPENDENCY rows
or individual gate tables: discovering all write events required scanning both the step-ordering
table and each gate subsection. The registry table indexes all write events in one place: given
any gate name or token name, the write schedule is O(1)-discoverable. The registry also makes
the pre-DAG vs. in-DAG classification of each write event explicit: GATE 0 writes FOCUS-STATE
pre-DAG (before Phase 1 runs); GATE 4 writes INERTIA-REF pre-DAG (root step, no prerequisites);
any write that occurs within a phase step is classified as in-DAG. This classification matters
for understanding token availability: a token written pre-DAG is available to all phases; a
token written in-DAG is available only to downstream steps. Without a registry, this
classification is derivable only by cross-referencing the EXECUTION DEPENDENCY table and each
gate's write row. With a registry, it is a first-class table column. C-46 is the third table
that completes PREFLIGHT's machine-readable specification: OUTPUT CONTRACTS (what is produced
and in what format), EXECUTION DEPENDENCY (in what order and with what prerequisites), WRITE-
TOKEN REGISTRY (when each write-token event occurs and which slot it populates). Together, the
three tables make PREFLIGHT a complete and self-contained specification: no phase body need be
read to understand the full lifecycle of any output slot.

---

## Criterion Rationale (v13 additions)

**Why C-47 (WRITE-TOKEN REGISTRY "Consumed by" column for bidirectional lifecycle):**
R13 V-01, V-04, and V-05 showed that adding a "Consumed by" column to the WRITE-TOKEN REGISTRY
closes the same bidirectionality gap that C-34 closes for the OUTPUT CONTRACTS table. C-46
introduced the WRITE-TOKEN REGISTRY as the write-schedule index: given a gate, you can
determine which token it writes and when. C-34 added a "Required by" column to OUTPUT CONTRACTS
so that given a slot, you can determine which downstream slots depend on it. The remaining gap
is symmetric: given a written token, you cannot determine which downstream phases consume it
without reading each phase body. V-02 and V-03 (R13) had WRITE-TOKEN REGISTRY tables satisfying
C-46 but with no consumption column -- the registry indexed writes but not reads. V-01, V-04,
and V-05 extended the registry with "Consumed by" entries (e.g., INERTIA-REF consumed by Phase
3, Phase 5; FOCUS-STATE consumed by Phase 2 conditional, Phase 4 PATH row), making the full
token lifecycle bidirectional at the registry level. The analogy is precise: C-27 ("Filled by
phase") makes the producer side of OUTPUT CONTRACTS machine-readable; C-34 ("Required by")
makes the consumer side machine-readable. C-46 makes the producer side of WRITE-TOKEN REGISTRY
machine-readable; C-47 ("Consumed by") makes the consumer side machine-readable. Both tables
become fully bidirectional when both their producer and consumer columns are present. C-47 is a
strictly stronger form of C-46; it satisfies C-46 but not vice versa.

**Why C-48 (GATE 3 PATH-PRESENT row 0 before SOURCE-position check):**
R13 V-02, V-04, and V-05 showed that adding a PATH-PRESENT row as the first checkpoint in
GATE 3 applies to the gate validator the same declaration-before-execution principle that C-45
applies to Phase 4 itself and C-37 applies to Phase 3. GATE 3 validates Phase 4's structural
integrity; without a dedicated PATH-PRESENT row, GATE 3 may check SOURCE position as its first
row -- which implicitly detects PATH absence (SOURCE found at row 0 indicates PATH is missing)
but does not name it. When PATH absence is detected only as "SOURCE mislocation," the failure
is real but its root cause is unnamed at the gate level: a reviewer reading GATE 3 sees
"SOURCE not at row 1" rather than "PATH row absent." V-01 and V-03 (R13) had GATE 3 tables
where SOURCE-position was row 0 of the gate, leaving PATH absence as a derived inference rather
than a named failure state. V-02, V-04, and V-05 added PATH-PRESENT as gate row 0 with a
dedicated failure state ("PATH absent failure"), making the absence independently detectable
before any positional analysis runs. This is the validator analogue of the declaration-before-
execution principle: just as C-45 ensures Phase 4 declares both active and inactive execution
branches before evidentiary rows, C-48 ensures GATE 3 confirms the required structural element
exists before checking its position. The two criteria are complementary: C-45 is the structural
requirement; C-48 is the validator that enforces it with named, independent detectability.
C-48 does not imply C-45; C-45 does not imply C-48; both must be satisfied for the Phase 4
PATH pattern to be fully specified and fully enforced.

**Why C-49 (Phase 5 COMPLETENESS row as structural tail validation):**
R13 V-03 and V-05 showed that adding a COMPLETENESS row as the final row of Phase 5's
structured table closes the last phase boundary that lacks a named, independently checkable
completeness checkpoint. Prior phases have analogous structural closures: Phase 3 ends with a
GAP-CONFIRMED row (C-37); Phase 4 ends with a THEREFORE row (C-36, C-45). Phase 5 (findings
synthesis) produces findings rows and then ends -- leaving collective completeness (all findings
have Anchor values; all findings have INERTIA-REF citations in ternary-token format) verifiable
only by scanning all rows rather than by reading a single named row. V-03 and V-05 added a
COMPLETENESS row as Phase 5's tail that checks the aggregate: its Failure state ("Findings
completeness failure") names the collective validation failure as a first-class checkpoint
rather than a post-hoc audit. This is the Phase 5 analogue of the GAP-CONFIRMED row in Phase 3
and the THEREFORE row in Phase 4: each phase's final row confirms that the phase's output meets
its production contract before the next phase begins. The tail validation pattern also
reinforces C-38's amendment-boundary column "Gates re-run": if a COMPLETENESS failure occurs
after an amendment, the AMEND table's "Gates re-run" column for that row must name Phase 5
re-execution, making the completeness obligation explicit at the amendment boundary. C-49 does
not imply C-38 and C-38 does not imply C-49; both close different boundaries of the same
production lifecycle.

---

## Notes on Criterion Relationships

**C-21 vs C-16:**
C-16 requires naming failure states (satisfied by bolded prose); C-21 requires the gate to be
structured as a section with a PASS/FAIL table. R4 confirmed both can be PASS simultaneously;
they target different structural levels.

**C-26 vs C-21:**
C-21 requires at least one gate to be a named section with a PASS/FAIL table; C-26 requires all
gates to be consolidated into a single pre-phase PREFLIGHT block. A skill satisfying C-26
automatically satisfies C-21 via the gates within it.

**C-28 vs C-26:**
C-26 requires all gates in a single PREFLIGHT block. C-28 requires OUTPUT CONTRACTS to also be
a subsection within that block. C-28 satisfaction implies C-26; the converse is not true.

**C-32 vs C-28:**
C-28 requires OUTPUT CONTRACTS to be a subsection within PREFLIGHT. C-32 requires it to be the
first subsection. C-32 satisfaction implies C-28 (and C-26); the converse is not true.

**C-29 dependency on C-28:**
C-29 is only applicable when C-28 is satisfied. If OUTPUT CONTRACTS is a top-level section, no
path prefix is needed. In scoring, if C-28 is not satisfied, treat C-29 as N/A (score 0).

**C-30 vs C-22:**
C-30 satisfaction implies C-22. A skill can define INERTIA-REF in the inertia section (C-22)
without the gate performing the write (C-30).

**C-31 vs C-30:**
C-31 requires the write directive to be a structural table row with a named failure state.
C-31 satisfaction implies C-30 (and C-22). The converse is not true.

**C-33 vs C-19 and C-23:**
C-33 extends C-19 to the cross-dimensional proof slot specifically. C-33 does not imply C-19
or C-23 in general -- those may be satisfied by other slots independently of C-33.

**C-35 vs C-33:**
C-35 requires the cross-dimensional proof slot to have a syntactically checkable format
template. C-35 satisfaction implies C-33. C-33 satisfaction does not imply C-35 -- a slot
identified only by name, or described structurally, satisfies C-33 but not C-35.

**C-36 vs C-15:**
C-36 requires the entire proof phase to be a PASS/FAIL table. C-36 satisfaction implies C-15
(SOURCE is the first row, before the proof arguments by table position). C-15 satisfaction via
code-block format does not imply C-36.

**C-34 vs C-27:**
C-27 adds a "Filled by phase" column (producer assignment). C-34 adds a "Required by" column
(dependent slot declaration). Both are contract-level columns; neither implies the other. A
5-column contract may satisfy both; a 4-column contract may satisfy C-27 without C-34 or C-34
without C-27.

**C-37 vs C-36:**
C-37 applies the 4-row PASS/FAIL table pattern to Phase 3 (whitespace validation); C-36 applies
it to Phase 4 (cross-dimensional proof). Neither implies the other -- each targets a distinct
phase. A skill may satisfy C-36 without structuring Phase 3 as a table (C-37 fails) and vice
versa.

**C-38 vs C-08 and C-14:**
C-38 satisfaction implies C-08 (each adjustment is a table row naming cause and effect) and C-14
(proof rerun obligation is queryable via the Gates re-run column for focus-shift rows). C-08 and
C-14 do not imply C-38 -- prose AMEND sections that satisfy both criteria do not satisfy C-38.

**C-39 vs C-34:**
C-34 is a slot-level dependency graph within the output contract table. C-39 is a step-level
execution DAG within PREFLIGHT. Both are PREFLIGHT-level machine-readable tables; neither
implies the other. A skill may have slot dependencies (C-34) without an execution ordering table
(C-39) and vice versa.

**C-40 vs C-26:**
C-26 requires all mandatory gates in PREFLIGHT. C-40 requires the FOCUS gate specifically to
be a named PASS/FAIL gate subsection within PREFLIGHT -- not just any prose check. In practice,
a skill where all numbered gates are in PREFLIGHT but FOCUS is prose before PREFLIGHT satisfies
neither C-26 (FOCUS is a mandatory gate, distributed outside the block) nor C-40 (FOCUS is not
a named gate in PREFLIGHT). C-40 satisfaction implies C-26 for the FOCUS gate; C-26 does not
automatically generate C-40 if FOCUS was treated as prose rather than a gate.

**C-41 vs C-37:**
C-37 requires Phase 3 to be a CANDIDATE-first 4-row PASS/FAIL table; C-41 requires the
vs-INERTIA-REF row within that table to use the ternary-token format. C-41 does not imply C-37
(ternary format could appear in a prose phase); C-37 does not imply C-41 (the table can satisfy
the 4-row structural requirement without constraining the inertia comparison row value format).
Both may be satisfied independently; both may be satisfied together.

**C-42 vs C-39:**
C-42 is a strictly stronger form of C-39. C-42 requires the EXECUTION DEPENDENCY table to
include a "Prerequisite steps" column as a queryable column. C-39 requires the table to exist
with GATE 4 as root step; row position may imply ordering without a dedicated column. C-42
satisfaction implies C-39; C-39 satisfaction does not imply C-42.

**C-43 vs C-40:**
C-40 requires the FOCUS validation to be a named PASS/FAIL gate subsection in PREFLIGHT. C-43
requires the FOCUS resolution output to be a named slot in the OUTPUT CONTRACTS table. Each
addresses a different surface: C-40 is about gate structure; C-43 is about output slot
declaration. A skill with a FOCUS gate in PREFLIGHT (C-40) but no FOCUS-STATE slot in the
contract (C-43 fails) leaves focus-dependent slots unable to name their dependency by slot
number. A skill with a FOCUS-STATE slot declared but no gate structure (C-43 without C-40) has
the output artifact but lacks the structural gate that makes the validation checkable. Both
criteria together cover the full focus-dimension lifecycle: C-40 ensures focus validation is
first-class at the gate level; C-43 ensures focus resolution is first-class at the output slot
level.

**C-43 vs C-34:**
C-43 is a prerequisite for complete slot-level C-34 satisfaction when focus resolution is
upstream of one or more output slots. A skill satisfying C-34 without C-43 will show a gate
reference ("Requires GATE 0") rather than a slot reference ("Requires slot 0 (FOCUS-STATE)")
in the "Required by" column for focus-dependent slots, yielding PARTIAL satisfaction of C-34
for those rows. C-43 does not imply C-34 in general: a slot 0 declared without a "Required by"
column in the contract satisfies C-43 but not C-34.

**C-44 vs C-42:**
C-42 captures step-level control dependencies via a "Prerequisite steps" column in the
EXECUTION DEPENDENCY table -- which steps must complete before a given step runs. C-44 captures
slot-level data reads per step via a "Reads slot" column -- which output contract slots a step
reads as input. Both are columns within the same EXECUTION DEPENDENCY table; neither implies
the other. A table with only a "Prerequisite steps" column satisfies C-42 without C-44; a table
with only a "Reads slot" column satisfies C-44 without C-42. Both together make the EXECUTION
DEPENDENCY table a fully bidirectional data-flow and control-flow graph.

**C-44 vs C-43:**
C-43 is a practical prerequisite for C-44 satisfiability on focus-dependent steps. A step
cannot declare "Reads slot 0 (FOCUS-STATE)" in the EXECUTION DEPENDENCY table if FOCUS-STATE
has no slot entry in the OUTPUT CONTRACTS table to name. When C-43 is satisfied (slot 0
declared), C-44 can be satisfied for Phase 2 by adding slot 0 to the Reads slot cell. When
C-43 is not satisfied (no slot 0), C-44 cannot be fully satisfied for focus-dependent steps --
the read can only be expressed as "Reads GATE 0 output" (a gate reference), the same type-
boundary problem that C-43 was introduced to solve for the "Required by" column (C-34).

**C-45 vs C-36:**
C-36 requires Phase 4 to be a PASS/FAIL table with at least four rows including SOURCE,
REDUCTION-1, REDUCTION-2, and THEREFORE. A Phase 4 table with SOURCE as row 1 satisfies C-36.
C-45 additionally requires a PATH row as row 0 -- before SOURCE -- that declares both the
active and inactive execution branches as independently reviewable checkpoints. C-45 is a
strictly stronger form of C-36: C-45 satisfaction implies C-36; C-36 satisfaction does not
imply C-45.

**C-45 vs C-37:**
C-37 applies CANDIDATE-first row ordering to Phase 3 (whitespace validation). C-45 applies
PATH-first row ordering to Phase 4 (cross-dimensional proof). Both enforce declaration-before-
execution at the table level; neither implies the other -- each targets a distinct phase
boundary with a distinct row-0 declaration.

**C-46 vs C-31:**
C-31 requires the INERTIA-REF write instruction to be a dedicated row within the GATE 4
PASS/FAIL table. C-46 requires a separate WRITE-TOKEN REGISTRY table in PREFLIGHT indexing all
write-token events across all gates. C-46 satisfaction does not require C-31 (the registry
can index write events without requiring each to be a structural gate row); C-31 satisfaction
does not imply C-46 (a structural gate row for INERTIA-REF write does not produce a registry
table). Both may coexist; neither implies the other.

**C-46 vs C-32:**
C-32 requires OUTPUT CONTRACTS to be the first named subsection within PREFLIGHT. A
WRITE-TOKEN REGISTRY placed after OUTPUT CONTRACTS and before GATE 0 preserves C-32 compliance
provided the registry is not classified as a gate subsection. C-46 satisfaction implies C-28
(OUTPUT CONTRACTS within PREFLIGHT) but is compatible with C-32 in all standard placements.

**C-47 vs C-46:**
C-47 requires the WRITE-TOKEN REGISTRY to include a "Consumed by" column naming downstream
token consumers. C-46 requires only the write-schedule columns (gate, token, slot, pre-DAG/
in-DAG). C-47 is a strictly stronger form of C-46: C-47 satisfaction implies C-46; C-46
satisfaction does not imply C-47. The upgrade from C-46 to C-47 mirrors the upgrade from C-27
("Filled by phase") to C-34 ("Required by") in OUTPUT CONTRACTS: both add the consumption side
to an existing producer-oriented table.

**C-47 vs C-34:**
C-34 adds "Required by" to OUTPUT CONTRACTS (slot-level consumers). C-47 adds "Consumed by"
to WRITE-TOKEN REGISTRY (token-level consumers). Both make the consumption side of produced
artifacts machine-readable within PREFLIGHT; they address different tables. A skill can satisfy
C-34 without C-47 (slot consumers declared in contract but token consumers absent from
registry) and vice versa. Both together make PREFLIGHT fully bidirectional at both the slot
level (C-34) and the token level (C-47).

**C-48 vs C-45:**
C-45 is the structural requirement: Phase 4 must have a PATH row at row 0 before SOURCE. C-48
is the validator enforcement: GATE 3 must confirm PATH presence as its first independently
checkable row before SOURCE-position analysis. Neither implies the other -- each targets a
different structural surface (Phase 4 table vs. GATE 3 table). Both together align requirement
and enforcement: C-45 ensures Phase 4 is correct; C-48 ensures GATE 3 detects Phase 4
violations with named failure states rather than inferring PATH absence from SOURCE mislocation.

**C-48 vs C-36/C-37:**
C-36 and C-37 define PASS/FAIL table structure for Phase 4 and Phase 3 respectively. C-48
defines PASS/FAIL table structure for GATE 3 (the validator of Phase 4). The three criteria
address three distinct structural surfaces; none implies any other.

**C-49 vs C-37 and C-36/C-45:**
C-37 defines the CANDIDATE-first PASS/FAIL table structure for Phase 3, including GAP-CONFIRMED
as its final row. C-36/C-45 define the PASS/FAIL table structure for Phase 4, including
THEREFORE as its final row. C-49 defines the COMPLETENESS row as the final checkpoint of Phase
5. Each applies to a distinct phase; none implies any other. The pattern is consistent across
phases: each phase's structured table ends with a named confirmation row that makes the phase's
output acceptance checkable as a single independently reviewable checkpoint.

**C-49 vs C-38:**
C-38 makes the amendment boundary checkable (Slots re-filled and Gates re-run as queryable
columns). C-49 makes the initial findings production checkable (COMPLETENESS row as Phase 5
tail validation). C-38 closes the amendment lifecycle; C-49 closes the initial production
lifecycle. A skill can satisfy C-38 without C-49 (amendments are structured, initial findings
have no tail row) and vice versa. Both together close the full production-and-amendment
lifecycle of Phase 5.

---

## Summary of Changes

**v1 -> v2:**
- C-11 added -- all external rows must be cited (not just minimum one)
- C-12 added -- cross-dimensional finding must prove single-dimension insufficiency
- C-13 added -- findings must anchor to specific attribute values, not just competitor names
- Aspirational tier expands from 2 to 5 criteria
- Max composite moves from 100 to 115

**v2 -> v3:**
- C-14 added -- AMEND must prescribe C-12 proof rerun on focus shift (not just output update)
- C-15 added -- proof block must declare evidentiary source slot before reduction arguments
- C-16 added -- gate instructions must name the failure state, not only the positive rule
- C-17 added -- WHITESPACE finding must ground the gap in attribute-level absence across rows
- C-18 added -- skill instruction must include a NOT ACCEPTABLE exemplar for name-only anchoring
- Aspirational tier expands from 5 to 10 criteria; aspirational max moves from 25 to 50
- Max composite moves from 115 to 140
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 131, Strong >= 118, Passing >= 90

**v3 -> v4:**
- C-19 added -- collection phase must name output slot requirements by label (synthesis-first contracts)
- C-20 added -- anchoring must be enforced by column format shape, not prohibition alone
- C-21 added -- at least one gate must be a named section with a three-column PASS/FAIL table
- C-22 added -- INERTIA-REF token must be defined and required per finding as a reference baseline
- Aspirational tier expands from 10 to 14 criteria; aspirational max moves from 50 to 70
- Max composite moves from 140 to 160
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 150, Strong >= 135, Passing >= 90

**v4 -> v5:**
- C-23 added -- output contract slots must specify format shape per slot, not label only
- C-24 added -- producing phases must back-reference the output contract slot they fill
- C-25 added -- structural column coercion must span both collection and synthesis tables
- C-26 added -- all gates must be consolidated into a single pre-phase PREFLIGHT block
- Aspirational tier expands from 14 to 18 criteria; aspirational max moves from 70 to 90
- Max composite moves from 160 to 180
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 169, Strong >= 151, Passing >= 90

**v5 -> v6:**
- C-27 added -- output contract table must include a dedicated phase-assignment column
- C-28 added -- OUTPUT CONTRACTS must be a subsection within PREFLIGHT (full specification consolidation)
- C-29 added -- back-references must use full document path when OUTPUT CONTRACTS is nested
- C-30 added -- INERTIA-REF gate must include explicit write-token instruction, not just a check
- Aspirational tier expands from 18 to 22 criteria; aspirational max moves from 90 to 110
- Max composite moves from 180 to 200
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 188, Strong >= 168, Passing >= 90

**v6 -> v7:**
- C-31 added -- INERTIA-REF write instruction must be a structural PASS/FAIL table row with named failure state (strictly stronger than C-30; write-token-as-gate-row pattern from R7 V-03, V-05)
- C-32 added -- OUTPUT CONTRACTS must be the first subsection within PREFLIGHT, before all gates (strictly stronger than C-28; spec-first PREFLIGHT pattern from R7 V-02, V-05)
- C-33 added -- output contract must include a dedicated slot forward-declaring the cross-dimensional proof requirement (focus-scope evidence slot pattern from R7 V-05)
- Aspirational tier expands from 22 to 25 criteria; aspirational max moves from 110 to 125
- Max composite moves from 200 to 215
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 202, Strong >= 181, Passing >= 90

**v7 -> v8:**
- C-34 added -- output contract table must include a "Required by" column naming inter-slot dependencies (dependency chain readable at contract time; from R8 V-01, V-04)
- C-35 added -- cross-dimensional proof slot must have a parse-ready syntactic format template, not a structural description (strictly stronger than C-33; from R8 V-02)
- C-36 added -- cross-dimensional proof phase must be structured as a 4-row PASS/FAIL table with named failure states per row (strictly stronger than C-15; from R8 V-03, V-04)
- Aspirational tier expands from 25 to 28 criteria; aspirational max moves from 125 to 140
- Max composite moves from 215 to 230
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 216, Strong >= 194, Passing >= 90

**v8 -> v9:**
- C-37 added -- WHITESPACE validation phase must be a CANDIDATE-first 4-row PASS/FAIL table (Phase 3 structural analogue of C-36; CANDIDATE-first by row order prevents selective evidence assembly; from R9 V-01, V-04, V-05)
- C-38 added -- AMEND must be a structured table with Slots re-filled and Gates re-run as queryable columns (implies C-08 and C-14; amendment-lifecycle analogue of C-27 and C-21; from R9 V-02, V-04, V-05)
- C-39 added -- PREFLIGHT must include an EXECUTION DEPENDENCY table with GATE 4 as root step, making inertia-first a structural DAG property rather than a prose convention (complements C-34's slot-level dependency column; from R9 V-03, V-05)
- Aspirational tier expands from 28 to 31 criteria; aspirational max moves from 140 to 155
- Max composite moves from 230 to 245
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 231, Strong >= 206, Passing >= 90

**v9 -> v10:**
- C-40 added -- FOCUS validation must be structured as a named PASS/FAIL gate subsection within PREFLIGHT, not prose before or outside PREFLIGHT (closes the last gate surface that C-26 alone does not force inside PREFLIGHT when prose alternatives exist; implies C-26 for the FOCUS gate; from R10 V-01, V-04, V-05)
- C-41 added -- Phase 3 vs-INERTIA-REF row must use the slot 6 ternary-token format ({reinforces|challenges|contextualizes}: {phrase}), making the Phase 3 inertia comparison syntactically checkable using the same format as the slot 6 output artifact (independent of C-37; from R10 V-02, V-04, V-05)
- C-42 added -- EXECUTION DEPENDENCY table must include a dedicated "Prerequisite steps" column making DAG edges queryable by column inspection, not inferable from row sequence alone (strictly stronger than C-39; from R10 V-03, V-05)
- Aspirational tier expands from 31 to 34 criteria; aspirational max moves from 155 to 170
- Max composite moves from 245 to 260
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 245, Strong >= 219, Passing >= 90

**v10 -> v11:**
- C-43 added -- OUTPUT CONTRACTS must include a dedicated FOCUS-STATE slot (slot 0 or equivalent) with a format template, making focus resolution a named output artifact rather than gate-only control flow; closes the C-34 type-boundary gap where focus-dependent slots must reference a gate rather than a slot in the "Required by" column, yielding partial C-34 satisfaction (independent of C-40; from R11 V-01, V-04, V-05 vs. V-02, V-03 PARTIAL on C-34)
- Aspirational tier expands from 34 to 35 criteria; aspirational max moves from 170 to 175
- Max composite moves from 260 to 265
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 250, Strong >= 223, Passing >= 90

**v11 -> v12:**
- C-44 added -- EXECUTION DEPENDENCY table must declare all slot reads per step including conditional reads (e.g., Phase 2's conditional branch on slot 0 for Focus column inclusion); omitting a conditional read yields an incomplete data-flow graph; "Reads slot" column must be exhaustive for every step that branches on a slot value (independent of C-42; slot-level data reads vs. step-level control dependencies; from R12 V-01, V-04, V-05 vs. R11 V-05 omission)
- C-45 added -- Phase 4 cross-dimensional proof table must begin with a PATH row as row 0 before SOURCE, declaring both active and inactive execution branches as independently reviewable table checkpoints; extends C-37's CANDIDATE-first principle from Phase 3 to Phase 4; strictly stronger than C-36 (PATH row before SOURCE vs. SOURCE present among four rows; from R12 V-02, V-04, V-05)
- C-46 added -- PREFLIGHT must include a dedicated WRITE-TOKEN REGISTRY table (after OUTPUT CONTRACTS, before GATE 0) indexing all write-token events by gate, token, slot, and pre-DAG/in-DAG classification; completes the three-table PREFLIGHT specification: OUTPUT CONTRACTS + EXECUTION DEPENDENCY + WRITE-TOKEN REGISTRY; O(1)-discoverable write schedule without scanning individual gate tables (from R12 V-03, V-05)
- Aspirational tier expands from 35 to 38 criteria; aspirational max moves from 175 to 190
- Max composite moves from 265 to 280
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 265, Strong >= 238, Passing >= 90

**v12 -> v13:**
- C-47 added -- WRITE-TOKEN REGISTRY must include a "Consumed by" column naming downstream token consumers, making the full token lifecycle bidirectional within PREFLIGHT; extends C-46 from write-schedule registry to full lifecycle registry; strictly stronger than C-46; applies to WRITE-TOKEN REGISTRY the same bidirectionality that C-34 ("Required by") applies to OUTPUT CONTRACTS (from R13 V-01, V-04, V-05 vs. V-02, V-03 registry write-only)
- C-48 added -- GATE 3 must include a dedicated PATH-PRESENT check as its first independently reviewable row before any SOURCE-position check, making PATH absence a named failure state rather than a SOURCE-mislocation inference; applies to GATE 3 the same declaration-before-execution principle that C-45 applies to Phase 4 and C-37 applies to Phase 3; independent of C-45 (requirement vs. enforcement surface) (from R13 V-02, V-04, V-05 vs. V-01, V-03 GATE 3 SOURCE-first)
- C-49 added -- Phase 5 findings synthesis table must end with a COMPLETENESS row as a named tail checkpoint confirming all per-finding elements are present, with a named "Findings completeness failure" state; makes Phase 5 self-validating; extends the final-row confirmation pattern established by GAP-CONFIRMED (C-37) and THEREFORE (C-36/C-45) to the findings synthesis phase; independent of C-38 (amendment boundary) and C-37/C-36/C-45 (each targets a distinct phase) (from R13 V-03, V-05 vs. V-01, V-02, V-04 no Phase 5 tail row)
- Aspirational tier expands from 38 to 41 criteria; aspirational max moves from 190 to 205
- Max composite moves from 280 to 295
- Golden threshold unchanged: all 5 essential PASS AND composite >= 90
- Grade bands rescaled: Exceptional >= 280, Strong >= 253, Passing >= 90
