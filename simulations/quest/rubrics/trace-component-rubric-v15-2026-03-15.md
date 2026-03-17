# Rubric: trace-component (v15)

**48 criteria across 3 tiers -- 3 new aspirational criteria added from R14 excellence signals:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (all must pass) | C-01 through C-05 | 60 |
| Recommended | C-06 Side Effect Coverage, C-07 Issue Detection, C-08 Framework Vocabulary | 30 |
| Aspirational | C-09 through C-48 | 80 |

**Ceiling: 170 pts** (up from 164; 3 new criteria x 2 pts each)

---

The three R14 signals that promoted:

**C-46 . Epistemic-Register Question Framing** -- From V-05 HIGH-WATER MARK on C-42. V-05 frames its causal questions at the epistemic level -- "what is the epistemic status of a traversal hop before any evidence is applied?" -- rather than at the structural level used by V-04 -- "why must the block open with an explicit count label before the obligations are listed?" V-04's structural-level questions name the schema artifact implicitly (the question assumes the answer is a count label, making the response a structural copy rather than a derivation). V-05's epistemic questions require the model to reason about cognitive status and logical necessity before deriving the structural form. C-41 requires causal questions; C-46 requires those questions to be framed at the epistemic register so the structural answer is not implied by the question's vocabulary.

**C-47 . Causal-Completion Gate Before Schema Authorship** -- From V-05 "answers required before placeholder design" sequencing requirement on C-41. V-05 presents causal questions in a block that must be answered completely before the schema authorship slot appears -- the two phases are structurally sequential, not interleaved. V-01 and V-04 present causal questions and schema production in the same structural context, allowing a model to interleave explanation and design. Interleaving allows post-hoc rationalization: a model that chooses a structural form first can write the causal explanation after, presenting it as if it preceded the design. Sequenced completion enforces that the causal case exists in the output as a prior production before the schema artifact is written -- the model cannot rationalize a schema form it has not yet designed. C-41 requires causal explanation to be present; C-47 requires the prompt to enforce causal-phase completion as a structural precondition of schema-phase entry.

**C-48 . Null-Hypothesis Register in Causal Question Set** -- From V-05 "null-hypothesis question set + three-property question set in sequence" on C-41. V-05 decomposes the causal question set into two sequentially ordered registers: (1) a null-hypothesis register addressing the epistemic status of the default/unmarked case -- "what is the status of a hop before any evidence is applied?" -- and (2) a departure-property register addressing the structural properties required for the active/marked cases. V-01 and V-04 use single-register question sets that address only why structural properties are required, without separately interrogating the epistemic status of the null case. A single-register set allows the model to derive the departure conditions without establishing why the unmarked case is the correct default. The null-hypothesis register is structurally prior: the epistemic justification for the default must be established before the departure conditions can be evaluated as departures from it. A question set that asks only "why must active hops declare X" without first asking "what is the status of a hop before X is declared" conflates the null baseline with the departure condition.

**R14 triple structure:**

- **C-46** (epistemic-register, per-question): questions phrased at the structural level name the answer implicitly, enabling the model to copy rather than derive; epistemic-level questions require derivation from first principles.
- **C-47** (sequencing-enforcement, per-phase-boundary): causal completion before schema authorship prevents post-hoc rationalization; interleaved structure allows design to precede the explanation that is supposed to ground it.
- **C-48** (null-register, per-question-set): the null-hypothesis register establishes the epistemic baseline for the unmarked case before departure properties are evaluated; without it, departure conditions are asserted without a grounded baseline.

C-46 can be satisfied without C-47 (questions phrased epistemically but presented in an interleaved block). C-47 can be satisfied without C-46 (causal questions sequenced before schema authorship but questions are structurally framed). C-48 can be satisfied without C-46 or C-47 (null-hypothesis register present, questions structurally framed, block not sequenced). Full expression of the R14 causal-question cluster requires all three: C-48 establishes the null baseline, C-46 ensures the questions are derived not copied, C-47 enforces that derivation precedes design. V-05 carries all three; V-01 and V-04 carry C-41/C-42 precursors but none of C-46/C-47/C-48 as distinct structural properties.

---

## Essential Criteria (weight: 60 points total, 12 pts each)

All five must pass. Failing any one essential criterion fails the entire output regardless of composite score.

### C-01 . Event Anchor
- **Category**: correctness
- **Weight**: essential
- **Text**: The output names the exact event that triggered the trace: the event type (click, submit, input, etc.), the specific UI component that fired it (not a generic description like "the button"), the event payload or input value if relevant, and the handler function or lifecycle hook that received it.
- **Pass condition**: The event type, the exact component name, and the handler function are all named. "The button fires a click event" without naming the handler does not pass. "The input" without naming the component does not pass.

### C-02 . Component Tree Traversal
- **Category**: correctness
- **Weight**: essential
- **Text**: The output traces the path of the action through the component hierarchy -- from the event-receiving leaf up through handlers, context providers, or HOCs to the root of the affected subtree. Each hop names the component.
- **Pass condition**: At least two named components in the traversal path are shown with a clear parent->child or handler->provider direction. A flat list of components with no structural relationship does not pass.

### C-03 . State Update Map
- **Category**: correctness
- **Weight**: essential
- **Text**: The output identifies every state mutation triggered by the action: local component state (useState, this.setState), context state, and store state (Redux, Zustand, Pinia, etc.). For each mutation: the state key, old value shape, new value shape, and the component or store that owns it.
- **Pass condition**: At least one concrete state mutation is named with its owner. "State updates" as a section header with no specifics does not pass. "State changes in response to the action" does not pass. "The store is modified" without naming the key or slice does not pass.

### C-04 . Re-render Inventory
- **Category**: correctness
- **Weight**: essential
- **Text**: The output lists which components re-render as a result of the state changes, explaining why each one re-renders (owns the state, subscribes to context, receives new props, etc.).
- **Pass condition**: At least one component is listed with its re-render cause. "Several components re-render" without naming them does not pass. "Components re-render as expected" without naming them does not pass.

### C-05 . Final UI State
- **Category**: correctness
- **Weight**: essential
- **Text**: The output describes the observable UI state after all synchronous effects and at least one async settle point (e.g., after a loading state resolves). This is the "what the user sees" close to the trace.
- **Pass condition**: A concrete final state is described -- visible elements, disabled states, error messages, or confirmed no-change. "UI updates accordingly" does not pass. "The UI reflects the state changes" does not pass. "Success and error states are handled" without describing what the user sees does not pass.

---

## Recommended Criteria (weight: 30 points total)

Output is meaningfully better with these. Missing one is acceptable; missing all three is a gap.

### C-06 . Side Effect Coverage
- **Category**: coverage
- **Weight**: recommended (10 pts)
- **Pass condition**: At least one side effect identified with its mechanism. If none, explicitly state "No side effects -- confirmed synchronous: no API calls, timers, subscriptions, or navigation triggered by this action." Silence does not pass.

### C-07 . Issue Detection
- **Category**: depth
- **Weight**: recommended (10 pts)
- **Pass condition**: At least one issue named with its component or state path, presented in a structured FINDINGS table with N/A-prohibited columns. An advisory narrative section with a single-block escape path does not pass. "May have performance issues" does not pass.

### C-08 . Framework Vocabulary
- **Category**: behavior
- **Weight**: recommended (10 pts)
- **Pass condition**: At least two framework-specific terms correctly applied in context.

---

## Aspirational Criteria (weight: 80 points total, 2 pts each)

### C-09 . Fix Recommendations
- **Category**: depth
- **Pass condition**: At least one issue has a fix naming a specific API or pattern.

### C-10 . Render Quantification
- **Category**: depth
- **Pass condition**: At least one component has a numeric render annotation AND verdict co-located in the same table row or sentence. Separation into two columns or two sections does not satisfy.

### C-11 . Inline Phase-Close Gates
- **Category**: structure
- **Pass condition**: At least three trace phases each end with an explicit gate statement naming exact phrases that do not close the phase.

### C-12 . Mandatory Comparison Column
- **Category**: structure
- **Pass condition**: At least one table includes a "What this adds vs. ad-hoc" or equivalent comparison column that is populated for every row.

### C-13 . Exact-Phrase Gate Family
- **Category**: structure
- **Pass condition**: The phase gate set intercepts at least three distinct escape strings across multiple phases (not just one phase). Generic intercepts like "no impact", "minor issue", and "low risk" each appear as named non-closers in at least one gate.

### C-14 . Column-Header Escape Instruction
- **Category**: structure
- **Pass condition**: At least one mandatory column embeds its fill constraint in the column header itself (e.g., "Verdict [justified/unnecessary/0x]"), providing enforcement at cell-write time independent of surrounding prose instructions.

### C-15 . Do-Nothing Cost
- **Category**: depth
- **Pass condition**: At least one finding quantifies the cost or risk of leaving the issue unaddressed, not merely describing the issue itself.

### C-16 . FINDINGS Section Gate
- **Category**: structure
- **Pass condition**: The closing FINDINGS or consolidation section has its own explicit gate intercepting at least two phrases that summarize-away rather than enumerate issues -- specifically strings such as "no impact", "minor issue", "low risk", or "no concerns found". Phase-only gates do not satisfy this criterion; the FINDINGS section itself must carry the gate so that escape strings that survive trace phases are intercepted at consolidation.

### C-17 . Triple Structural Lock
- **Category**: structure
- **Pass condition**: At least one mandatory column is enforced by all three independent mechanisms simultaneously: (1) the column is present in the template and marked mandatory, (2) the column header embeds the constraint instruction (satisfying C-14), and (3) a per-row exact-phrase gate names the specific strings a model produces when it clears the first two mechanisms without substantive content. Having only one or two of the three mechanisms does not pass -- the lock is only complete when all three are co-present.

### C-18 . Table Format Required for Triple Lock
- **Category**: structure
- **Pass condition**: The FINDINGS section uses table format with column headers. Field-block or per-finding prose format does not pass this criterion even if mandatory fields and gate blocks are present -- field labels are not column headers, and without column headers the C-17 mechanism (2) is structurally absent, making the triple lock architecturally impossible.

### C-19 . Gate-Block Formalism Not Substitutable by Imperative Prohibition
- **Category**: structure
- **Pass condition**: All prohibited escape strings are intercepted in bracketed [GATE: ...] blocks -- not in narrative "does not pass" or "is not acceptable" prose. Naming the same forbidden strings in prose instructions has zero structural equivalence to a gate block: a model that clears a prose prohibition still has no structural signal that the output is malformed, whereas a gate block names the failure at point-of-production. An output passes this criterion only if the enforcement format is gate-block formalism; same strings in wrong format does not pass.

### C-20 . Framework Declaration Gate
- **Category**: behavior
- **Pass condition**: The output includes an explicit framework and state management declaration before any phase analysis begins -- naming the framework (React, Vue, Angular, etc.) and the state management layer (Redux, Pinia, Zustand, NgRx, etc.) as a required output header. A pickup instruction without a required output declaration does not pass. Framework inferred silently from context does not pass.

### C-21 . Failure Mode Displacement
- **Category**: behavior
- **Pass condition**: The output produces explicit displacement text that names the blocked phrase and the required replacement -- e.g., "NOT 'state updates' -- Owner: CartStore, Key: items, Old: [], New: [{id: 1}]". Instruction-level blocking without displacement confirmation text in the output does not pass.

### C-22 . Re-render Necessity Annotation
- **Category**: depth
- **Pass condition**: Every component in the re-render inventory carries an explicit necessity annotation: necessary (reason: owns state / receives new props / subscribes to changed context) or unnecessary (reason: memoization missing / selector too broad / etc.). A re-render list with causes but no necessity verdict per component does not pass.

### C-23 . Four-Phase UI Progression
- **Category**: correctness
- **Pass condition**: The final UI state section covers all four phases in order: (1) before the action -- the baseline state the user started from, (2) immediately after the action fires -- optimistic or synchronous update, (3) after async resolution -- success state, (4) after async rejection -- error state. A three-phase section that collapses success and error or omits the pre-action baseline does not pass.

### C-24 . Zero-Mutation Declaration *(new -- R6 excellence signal)*
- **Category**: correctness
- **Pass condition**: When the traced action produces no state mutations, the output includes an explicit zero-mutation declaration -- naming the reason (read-only operation, display-only component, event consumed without store dispatch, etc.) and confirming that no local, context, or store state was modified. A missing state section does not pass. Silence does not pass. This criterion applies only to traces where no mutations occur; it is N/A otherwise.

### C-25 . Issue Category Completeness *(new -- R6 excellence signal)*
- **Category**: coverage
- **Pass condition**: The findings section explicitly addresses at least three of the following issue categories: render performance / unnecessary re-renders / accessibility / async error handling / memory leaks. Each category must appear either with a concrete finding or with an explicit "none detected -- [brief reason]" confirmation. A findings section that lists only discovered issues without clearing unchecked categories does not pass.

### C-26 . Unnecessary Re-render Promotion *(new -- R6 excellence signal)*
- **Category**: depth
- **Pass condition**: Every re-render annotated as unnecessary in the re-render inventory (C-22) appears in the findings section, referenced by component name, with a named fix -- a specific API or pattern (e.g., React.memo, createSelector, computed with stable deps). If the re-render inventory contains no unnecessary re-renders, the findings section includes an explicit statement to that effect. A findings section that omits the cross-link from inventory to fix does not pass.

### C-27 . Mutation Count Pre-Declaration *(new -- R7 excellence signal)*
- **Category**: correctness
- **Pass condition**: Before the state mutation table or section, the output declares the total count of state mutations produced by the action -- e.g., "Mutation count: N=3" or "State mutations: 0." For N=0 this declaration serves as the structural gate leading into C-24. For N>0 the declared count must match the number of mutations enumerated; a count that does not match the table row count does not pass. Omitting the pre-declaration and proceeding directly to the table does not pass.

### C-28 . Per-Hop Direction Annotation *(new -- R7 excellence signal)*
- **Category**: correctness
- **Pass condition**: Each hop in the component tree traversal carries an explicit direction annotation indicating the flow of the event or data at that hop -- upward propagation, downward prop-passing, event delegation, or context injection. C-02 requires that traversal direction be shown; this criterion requires the annotation to appear per hop, not once as a summary statement. A traversal that names components and shows overall direction but does not annotate each hop individually does not pass.

### C-29 . Re-render Inventory Completeness by Traversal *(new -- R7 excellence signal)*
- **Category**: correctness
- **Pass condition**: Every component named in the component tree traversal (C-02) must appear in the re-render inventory (C-04) with a verdict -- either a re-render verdict (re-renders -- reason: owns state / receives new props / etc.) or a non-render verdict (does not re-render -- reason: no state owned, no props changed, not subscribed to changed context, etc.). C-04 requires "at least one component with its re-render cause"; this criterion requires traversal-complete accounting so no traversal component is silently dropped. A re-render inventory that names fewer components than the traversal without explicit non-render verdicts for the missing ones does not pass.

---

### C-30 . Mutation Count Dual-Track (Direct + Inherited) *(new -- R8 excellence signal)*
- **Category**: correctness
- **Pass condition**: The mutation pre-declaration (C-27) distinguishes direct mutations -- state writes the action produces immediately -- from inherited mutations -- state writes triggered transitively through subscriptions, effects, computed properties, or watchers. Format: "Mutations: N=X direct, M=Y inherited" (or equivalent labeling) embedded in the existing mutation table header or pre-declaration line. A single-value count that conflates direct and inherited mutations does not pass. A separate sub-table introduced solely to separate the two counts does not pass -- the dual count must be absorbed into the existing mutation table structure without structural proliferation.

### C-31 . Schema-Field Coverage of Aspirational Criteria *(new -- R8 excellence signal)*
- **Category**: behavior
- **Pass condition**: Every structural element required by C-20 through C-29 is surfaced in the output as a schema-enforced field -- a named table column, a required row with fixed column headers, or a required cell that cannot be left blank -- rather than as a prose statement or advisory instruction alone. For each criterion in C-20 through C-29, there must be a corresponding field in the output's table structure that makes omission structurally visible. An output where all of C-20 through C-29 is satisfied through prose sections without table-column enforcement does not pass. An output where at least 7 of the 10 criteria map to specific schema fields passes; fewer than 5 does not pass.

### C-32 . Blank-Blocked Field Primacy *(new -- R8 excellence signal)*
- **Category**: behavior
- **Pass condition**: The output's primary enforcement mechanism for the five essential criteria (C-01 through C-05) is schema-field prevention -- table columns or required rows that cannot be left blank -- rather than prose narration, advisory instructions, or post-hoc auditor verification. Each of C-01 through C-05 must be satisfiable by reading a specific table cell or required row in the output, not only by reading the prose. An output that satisfies C-01 through C-05 entirely through narrative paragraphs without any corresponding schema field does not pass. An output where at least three of the five essential criteria are backed by blank-blocked schema fields passes; fewer than three does not pass.

---

### C-33 . Phase-Level Completeness Manifest *(new -- R9 excellence signal)*
- **Category**: behavior
- **Pass condition**: Each phase of the trace -- event reception, component traversal, state mutation, re-render, and UI settle -- is preceded by an explicit phase manifest declaring: (1) which components are in scope for that phase, (2) which state keys may be touched, and (3) which side effects may fire. The manifest gates the phase analysis: the analysis for a phase cannot begin until its manifest is declared. A global schema that declares fields once at the top without per-phase manifest repetition does not pass. A phase manifest that omits any of the three required fields does not pass. At least two phases must carry a complete manifest; a single manifested phase does not pass.

### C-34 . Inert Pass-Through Explicit Marking *(new -- R9 excellence signal)*
- **Category**: correctness
- **Pass condition**: Every component in the traversal path that receives an event or prop but produces no state mutation and triggers no side effect is explicitly marked as an inert pass-through -- using a notation such as `<-> inert`, `no-op hop`, or an equivalent label -- rather than being silently omitted or described only in prose. If all traversal hops produce mutations or side effects (no inert hops exist), the output includes an explicit statement: "No inert pass-through hops -- all traversal components contribute to state or effects." Inertia implied by absence from the re-render inventory (C-04) does not satisfy this criterion. A component described as "just forwarding props" without an explicit inert marker does not pass.

### C-35 . Criteria Audit Cross-Validation Table *(new -- R9 excellence signal)*
- **Category**: behavior
- **Pass condition**: A secondary audit table appears in the output that maps each essential and recommended criterion (C-01 through C-08) to its satisfying schema field -- naming the criterion label, the schema field or table column that satisfies it, and a PASS/FAIL verdict derived from reading that field. The audit table is a produced artifact in the output, not an internal validation step. An auditor role that validates criteria without emitting a table does not pass. A prose claim of completeness ("all essential criteria met") does not pass. The audit table must reference at least five of the eight criteria (C-01 through C-08) by label; a table covering fewer than five does not pass.

---

### C-36 . Inert-as-Default Direction Schema *(new -- R10 excellence signal)*
- **Category**: behavior
- **Pass condition**: The traversal schema's Direction column lists `<-> inert` (or equivalent no-op label) as the first and default permitted value, with active departure codes -- prop-pass, event-propagate, dispatch, effect-trigger, context-provide, or framework equivalents -- as named alternatives requiring explicit selection. Every hop in the traversal table carries a Direction cell populated from this schema. The structural implication is that inertia is the unmarked case and every active hop must declare its departure code; the schema enforces this by position, not by instruction. A schema where inert appears as a named special case positioned alongside active codes without priority does not pass. A direction column populated with active-code annotations that treats inertia as absence-of-annotation does not pass. A schema listing active codes first with inert as the trailing exception does not pass.

### C-37 . Manifest-Analysis Paired Block Structure *(new -- R10 excellence signal)*
- **Category**: behavior
- **Pass condition**: Each trace phase's manifest block and its corresponding analysis block appear as an explicitly labeled and positionally adjacent pair -- MANIFEST-N immediately followed by TABLE-N (or equivalent phase-keyed labels where N matches across the pair) -- with no intervening content between the manifest close and the analysis open. The pairing guarantee is structural: a manifest at the document header separated from analysis tables by other content does not pass, because positional separation decouples the manifest from the phase it gates. A manifest whose phase label does not correspond to its analysis table's phase label does not pass. At least three MANIFEST-N/TABLE-N pairs must be present; fewer than three does not pass.

---

### C-38 . Manifest-Close Adjacency Marker *(new -- R11 excellence signal)*
- **Category**: structure
- **Pass condition**: Every manifest block (MANIFEST-N) ends with an explicit prohibition marker as its closing line -- a statement that the corresponding analysis table begins directly below and no content may appear between the manifest close and the table header (e.g., "down-arrow TABLE-N begins immediately below. No content may appear between this line and the TABLE-N header."). This marker must appear as the final line of the manifest block -- not in the manifest's opening instruction, not in a document-level charter or preamble, and not as an annotation at the table's opening line. The mechanism: a model inserting content between manifest close and table header must contradict the last line it wrote, making violation structurally self-contradictory at point-of-production. A manifest that carries a fill instruction at its header without a closing prohibition line does not pass. A document charter that declares the adjacency rule once without embedding it in each manifest's close does not pass. At least three manifest blocks must carry the close-line prohibition marker; fewer than three does not pass.

### C-39 . Self-Authored Schema Constraint *(new -- R11 excellence signal)*
- **Category**: behavior
- **Pass condition**: The prompt structure requires the model to produce a named schema artifact -- a SCHEMA CHARTER, TRAVERSAL-SCHEMA, or equivalent named document -- in a prior role or step that explicitly declares at minimum: (1) the inert-default rule from C-36 (Direction column defaults to `<-> inert`; active hops must declare departure), and (2) the manifest-adjacency rule from C-37 (MANIFEST-N / TABLE-N adjacent pairs; no intervening content). The analysis role is then bound by its own prior production: violating the schema the model authored is structural self-contradiction of prior output, not disobedience of an external instruction. A schema handed to the model as a pre-filled template to follow does not pass -- the model must produce the schema artifact itself. A schema authored by the prompt writer and presented as a constraint does not pass. The produced schema artifact must be a named, legible document that a reader can reference to verify the analysis role's compliance. An output where the model begins the trace analysis without first having authored a schema artifact does not pass.

---

### C-40 . Dual-Constraint Position-and-Content Placeholder *(new -- R12 excellence signal)*
- **Category**: structure
- **Pass condition**: Each manifest's close-line placeholder enforces both the content constraint (verbatim reproduction of the exact text declared in the schema artifact) and the positional constraint (this placeholder occupies the manifest's last line) within a single instruction string. A placeholder that specifies the content source without naming the positional constraint does not pass. A placeholder that names the position without naming the content source does not pass. The dual form eliminates two independent failure modes simultaneously: text drift (wrong text or paraphrase inserted instead of the schema-declared text) and positional drift (marker placed before trailing manifest content rather than at manifest close). The content-source reference and the position declaration must co-occur in the same placeholder instruction; satisfying each constraint in a separate instruction does not pass. At least three manifest placeholders must carry the dual-constraint form; fewer than three does not pass.

### C-41 . Schema Causal Explanation Requirement *(new -- R12 excellence signal)*
- **Category**: behavior
- **Pass condition**: The schema artifact (satisfying C-39) requires the model to articulate the structural reason why the adjacency marker must occupy the manifest's closing position -- not merely declare that it must. The causal explanation requirement appears as an explicit authorship instruction within the schema prompt: the model must explain the enforcement mechanism (why a close-line at the last position makes violation structurally self-contradictory) before or as part of declaring the close-line text. A schema that states the rule ("adjacency marker required as last line") without requiring causal reasoning does not pass. A schema that asks "explain why the marker must be the last line" as part of the authorship task passes. The causal explanation elevates the constraint from a positional directive to a structural reasoning commitment: the model cannot violate the rule without contradicting its own stated understanding of the mechanism, not only its own prior structural output.

### C-42 . Anti-Reproduction Schema Authorship *(new -- R12 excellence signal)*
- **Category**: behavior
- **Pass condition**: The schema artifact prompt slot is blank -- no pre-filled template text for the model to modify, adjust, or reproduce -- and carries an explicit instruction prohibiting verbatim or near-verbatim reproduction of the requirement text. The model must author the schema constraints in its own words from a blank authorship context. A prompt that pre-fills the schema template and asks the model to complete or adjust it does not pass. A prompt that presents the requirements as prose and instructs the model to formalize them into a schema does not pass -- copying the prose into a table format is reproduction, not authorship. The blank-slot plus anti-copy structure ensures the schema is a genuine cognitive production: a model that transcribes requirement text has not authored a schema. C-39 requires the model to produce the schema itself; C-42 requires the prompt to structurally enforce the authorship condition rather than aspirationally request it. An output where the schema artifact's content is substantially identical to the prompt's requirement text does not pass.

---

### C-43 . Mutual-Constraint Entanglement Declaration *(new -- R13 excellence signal)*
- **Category**: structure
- **Pass condition**: Each dual-constraint placeholder (satisfying C-40) includes an explicit statement that neither the content constraint nor the positional constraint can be satisfied without the other -- "Neither satisfied without the other" or equivalent entanglement language appearing within the placeholder instruction itself. A placeholder that co-locates both constraints without declaring their mutual dependence does not pass -- co-location is C-40's requirement; C-43 requires the additional declaration that satisfying one constraint alone does not partially satisfy the dual requirement. The entanglement declaration must appear in the placeholder body, not in surrounding prose instructions or document-level preamble. A document charter that states "constraints are mutually dependent" without embedding the declaration in each placeholder does not pass. At least three manifest placeholders must carry the entanglement declaration; fewer than three does not pass.

### C-44 . Numbered Constraint Enumeration in Placeholder *(new -- R13 excellence signal)*
- **Category**: structure
- **Pass condition**: Each dual-constraint placeholder (satisfying C-40) enumerates its content and positional constraints as a numbered list -- "(1) content -- [source and verbatim instruction]; (2) position -- [positional declaration]" or equivalent numbered form -- rather than as a compound or conjunctive sentence. A placeholder phrasing such as "verbatim content as the last line" conflates both constraints into a single surface, allowing a model to claim compliance with the compound phrase while addressing only one constraint. Numbered items give each constraint a discrete address: item (1) can be independently verified; item (2) can be independently verified; partial satisfaction of one is not satisfaction of the placeholder. A placeholder with both constraints present but written as a single compound instruction does not pass. A placeholder with numbered items where the numbering does not correspond to distinct content and position constraints does not pass. At least three manifest placeholders must use the numbered enumeration form; fewer than three does not pass.

### C-45 . Dual-Requirement Count Declaration in Placeholder *(new -- R13 excellence signal)*
- **Category**: structure
- **Pass condition**: Each dual-constraint placeholder (satisfying C-40) opens with an explicit count declaration stating that exactly two requirements are imposed by this single instruction -- "Two requirements, one instruction" or "Two simultaneous constraints -- one instruction" or equivalent N=2 framing -- as the placeholder's leading phrase, before the constraints are enumerated. The count declaration establishes a structural contract at the placeholder's opening token: this instruction carries N=2 obligations; satisfying fewer than two leaves the placeholder unfulfilled. A placeholder that enumerates both constraints without a leading count declaration allows a model to interpret the two constraints as aspects of a single compound requirement; the count declaration forecloses this interpretation by naming the obligation count explicitly. The count declaration must appear at the start of the placeholder instruction, not mid-placeholder or at the close. A placeholder that says "N=2 constraints" after listing the constraints does not pass -- the contract must be established before the constraints are read. At least three manifest placeholders must carry the leading count declaration; fewer than three does not pass.

---

### C-46 . Epistemic-Register Question Framing *(new -- R14 excellence signal)*
- **Category**: behavior
- **Pass condition**: Every causal question in the C-41 question set is phrased at the epistemic or logical-necessity level -- asking about the cognitive status of evidence, the consequence of absence, or the logical structure of constraint -- rather than at the structural or implementation level. A question that names a specific schema artifact type in its text (count declaration, numbered enumeration, positional marker, adjacency marker) implies the structural answer, enabling the model to map the question label directly to a schema field rather than deriving the form from the underlying concept. An epistemic-register question addresses the concept ("what is the logical status of an instruction that does not declare its obligation count?") and requires the model to derive the structural response. A structural-register question names the answer implicitly ("why must the placeholder open with a count declaration?"). The test: replacing the question's answer with the question's vocabulary should produce the schema field. If that substitution works, the question is structural-register. If the substitution fails -- because the question's vocabulary does not name the schema field -- the question is epistemic-register. At least three causal questions in the set must pass the epistemic-register test; fewer than three does not pass.

### C-47 . Causal-Completion Gate Before Schema Authorship *(new -- R14 excellence signal)*
- **Category**: behavior
- **Pass condition**: The prompt structure presents the causal question block (C-41) and the schema authorship slot (C-39 / C-42) as sequentially ordered phases -- causal questions first, schema production second -- with no schema production slot or schema-structure cue appearing before all causal questions have been presented. The sequencing enforces that causal reasoning must exist in the model's output as a prior production before any schema artifact is written; a model cannot begin authoring the schema without first having produced the causal answers. A prompt that presents causal questions and schema authorship in the same block, allowing the model to interleave reasoning and design, does not pass -- interleaving permits post-hoc rationalization, where the model chooses a structural form first and writes the causal explanation afterward. An advisory instruction ("answer these questions before beginning the schema") without structural separation does not pass -- a structural phase boundary, not an instruction, is required. The sequencing must be evident from the prompt's document structure: the causal section must close and the schema section must open as a subsequent distinct section. A prompt with a single combined section containing both questions and schema slots does not pass.

### C-48 . Null-Hypothesis Register in Causal Question Set *(new -- R14 excellence signal)*
- **Category**: behavior
- **Pass condition**: The causal question set (C-41) includes at least one question addressing the epistemic status of the default or null case -- the state of the system before any departing evidence is applied -- as a distinct prior question set before questions addressing the structural properties of the departure cases. The null-hypothesis register establishes the baseline: what is the cognitive or epistemic status of a hop, instruction, or constraint before any active property is declared? The departure-property register then addresses why active departure conditions require specific structural forms. A question set that addresses only the departure conditions ("why must active hops declare X?") without first grounding the null baseline ("what is the status of a hop before X is declared?") conflates the null and departure cases, allowing the departure conditions to be asserted without an established baseline they depart from. The null-hypothesis register must appear as a sequentially prior block to the departure-property register; a mixed question set where null-hypothesis and departure-property questions are interleaved does not pass. At least one null-hypothesis question and at least two departure-property questions must be present; a set with only null-hypothesis questions does not pass.

---

**Three new criteria -- rationale:**

| Criterion | Source pattern | What v14 covered | What v15 adds |
|-----------|---------------|-----------------|---------------|
| C-46 | R14: V-05 null-hypothesis framing ("what is the epistemic status of a traversal hop before any evidence is applied?") vs. V-04 labeled structural questions ("why must the block open with an explicit count label before the obligations are listed?"). V-05 is the highest advance on C-42 in R14 -- PARTIAL because schema structure is still implied but via a more abstract mechanism. Structural-register questions name the schema field in the question vocabulary, enabling copy-by-substitution. Epistemic-register questions require the model to derive the structural form from the conceptual frame. | C-41 requires causal questions; C-42 requires blank-slot authorship. Neither specifies the epistemic register of the questions themselves. | Requires causal questions to be framed at the epistemic level so the structural answer is not implied by the question vocabulary. A model answering an epistemic question cannot satisfy it by copying question labels into schema fields. |
| C-47 | R14: V-05 "answers required before placeholder design" -- explicit sequencing requirement enforcing causal-phase completion before schema-authorship-phase entry. V-01 and V-04 present questions and schema slot in the same structural context, allowing interleaving. Interleaving allows post-hoc rationalization: a model that designs the schema first can write the causal answers afterward, presenting them as prior. Sequential completion enforces that the causal case is a genuine prior production. | C-41 requires causal explanation to appear in the output; C-42 requires blank authorship slot. Neither enforces the temporal ordering of the two phases. | Requires the prompt to enforce causal-phase completion as a structural precondition of schema-phase entry -- not advisory but structural, with a phase boundary between the causal question block and the schema authorship slot. |
| C-48 | R14: V-05 "null-hypothesis question set + three-property question set in sequence" -- two-register decomposition with the null/default epistemic case addressed as a distinct prior block before departure-property questions. V-01 and V-04 address only departure properties (why must X structural form be used?) without a null-hypothesis baseline. The null register is structurally prior: the epistemic justification for the default must be established before departure conditions can be evaluated as departures from it. Without the null register, the departure conditions are asserted without a grounded baseline. | C-41 requires causal questions; C-46 requires epistemic framing. Neither requires the null case to be addressed as a distinct prior register. | Requires at least one null-hypothesis register question addressing the epistemic status of the default/null case before departure-property questions are presented; the two registers must appear in order with null first. |

---

**R14 triple structure:**

- **C-46** (epistemic-register, per-question): structural-register questions enable copy-by-substitution; epistemic-register questions require derivation -- the model must map from concept to form rather than label to field.
- **C-47** (sequencing-enforcement, per-phase-boundary): sequential completion prevents post-hoc rationalization; interleaving allows a model to design-then-explain rather than explain-then-design.
- **C-48** (null-register, per-question-set): the null-hypothesis baseline must precede departure-property questions; without an established null, departure conditions are asserted without a grounded baseline they depart from.

C-46 can be satisfied without C-47 (questions phrased epistemically but in an interleaved block with schema production). C-47 can be satisfied without C-46 (causal questions sequenced before schema authorship but questions are structural-register). C-48 can be satisfied without C-46 or C-47 (null-hypothesis register present, questions structural-register, phases not sequenced). Full expression of the R14 causal-question cluster requires all three: C-48 establishes the null baseline as a prior register, C-46 ensures questions require derivation rather than copy, C-47 enforces that the complete causal case precedes schema authorship. V-05 carries evidence of all three; V-01 and V-04 carry C-41/C-42 precursors but none of C-46/C-47/C-48 as distinct structural properties.

---

**Version history (aspirational tier):**

| Version | New criteria | Ceiling | R-signal source |
|---------|-------------|---------|----------------|
| v5 | C-09--C-19 (11 criteria) | 112 | R4 |
| v6 | C-20--C-23 (4 new) | 120 | R5 |
| v7 | C-24--C-26 (3 new) | 126 | R6 |
| v8 | C-27--C-29 (3 new) | 132 | R7 |
| v9 | C-30--C-32 (3 new) | 138 | R8 |
| v10 | C-33--C-35 (3 new) | 144 | R9 |
| v11 | C-36--C-37 (2 new) | 148 | R10 |
| v12 | C-38--C-39 (2 new) | 152 | R11 |
| v13 | C-40--C-42 (3 new) | 158 | R12 |
| v14 | C-43--C-45 (3 new) | 164 | R13 |
| **v15** | **C-46--C-48 (3 new)** | **170** | **R14** |
