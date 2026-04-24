# Rubric: trace-component (v14)

**45 criteria across 3 tiers -- 3 new aspirational criteria added from R13 excellence signals:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (all must pass) | C-01 through C-05 | 60 |
| Recommended | C-06 Side Effect Coverage, C-07 Issue Detection, C-08 Framework Vocabulary | 30 |
| Aspirational | C-09 through C-45 | 74 |

**Ceiling: 164 pts** (up from 158; 3 new criteria x 2 pts each)

---

The three R13 signals that promoted:

**C-43 . Mutual-Constraint Entanglement Declaration** -- From V-03 and V-05 HIGH-WATER MARK on C-40. Each dual-constraint placeholder includes an explicit statement that neither the content constraint nor the positional constraint can be satisfied without the other -- "Neither satisfied without the other" (V-03) and "Neither satisfied without the other" (V-05). C-40 requires both constraints to be co-located in one instruction; C-43 requires the placeholder to additionally declare that the two constraints are mutually entangled -- that is, not merely co-present but logically inseparable. A placeholder that lists both constraints without the entanglement declaration leaves open the interpretation that satisfying one constraint partially satisfies the dual requirement. The entanglement declaration forecloses partial-satisfaction claims at point-of-production.

**C-44 . Numbered Constraint Enumeration in Placeholder** -- From V-03 and V-05 NUMBERED-LIST pattern on C-40. The dual-constraint placeholder enumerates its two constraints as a numbered list -- "(1) content -- ...; (2) position -- ..." -- rather than as a compound or conjunctive sentence. V-03's "`(1) content -- reproduce TRACE CHARTER's close-line exactly; (2) position -- absolute last line`" and V-05's "`(1) content -- TRAVERSAL-SCHEMA Area 3 close-line exactly; (2) position -- final content of MANIFEST-N, TABLE-N follows directly`" give each constraint a discrete item address. A compound phrasing such as "verbatim content as the last line" conflates two constraints into one surface, allowing a model to claim it satisfied both by addressing the compound phrase. Numbered items make each constraint independently checkable and independently satisfiable -- a model cannot satisfy item (2) by satisfying item (1).

**C-45 . Dual-Requirement Count Declaration in Placeholder** -- From V-03 "Two requirements, one instruction" and V-05 "Two simultaneous constraints -- one instruction" opener pattern on C-40. The dual-constraint placeholder opens with an explicit count declaration stating that exactly two requirements are imposed by this single instruction, before the constraints are enumerated. The opener establishes a structural contract: this instruction imposes N=2 requirements; satisfying fewer than two leaves the placeholder unsatisfied. V-03's "Two requirements, one instruction: (1) ... (2) ..." and V-05's "Two simultaneous constraints -- one instruction: (1) ... (2) ..." name the count and the unity before the content. A placeholder that enumerates both constraints without a leading count declaration does not establish the N=2 contract -- a model reading the placeholder could interpret the two constraints as one compound requirement with two aspects rather than two discrete requirements that must each be independently satisfied.

**R13 triple structure:**

- **C-43** (logical-binding, per-placeholder): the entanglement declaration forecloses partial-satisfaction claims; satisfying one constraint cannot be claimed as partial satisfaction of the dual requirement. C-40 requires co-location; C-43 requires declared inseparability.
- **C-44** (structural-granularity, per-placeholder): numbered enumeration makes each constraint a discrete, independently checkable item at point-of-production. A compound form allows conflation; numbered items prohibit it.
- **C-45** (contract-establishment, per-placeholder): the count declaration establishes the N=2 obligation before the constraints are listed. Without the count header, a model can interpret two constraints as aspects of one compound requirement; the count header makes the two-requirement obligation explicit at the placeholder's opening token.

C-43 can be satisfied without C-44 (entanglement declared, constraints not numbered). C-44 can be satisfied without C-43 (constraints numbered, no entanglement declaration). C-45 can be satisfied without C-43 or C-44 (count declared, constraints not numbered and not entangled). Full expression of the dual-constraint placeholder cluster requires all three: count declaration (C-45) establishes the obligation, numbered enumeration (C-44) makes each item independently addressable, and entanglement declaration (C-43) forecloses partial satisfaction. V-03 and V-05 are the only variations that carry all three; V-01, V-02, V-04 satisfy C-40 but carry none of C-43, C-44, C-45.

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

## Aspirational Criteria (weight: 74 points total, 2 pts each)

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

**Three new criteria -- rationale:**

| Criterion | Source pattern | What v13 covered | What v14 adds |
|-----------|---------------|-----------------|---------------|
| C-43 | R13: V-03 "Neither satisfied without the other" and V-05 "Neither satisfied without the other" -- both high-water variations independently arrived at the entanglement declaration as the structural advance over bare dual-constraint placeholders (V-01, V-02, V-04). C-40 requires co-location of both constraints in one instruction; V-03 and V-05 add the logical-binding statement that the two constraints are inseparable -- satisfying one does not partially discharge the dual requirement. | C-40 requires content-source and position-declaration to co-occur in one placeholder instruction | Requires the placeholder to additionally declare the entanglement: neither constraint satisfies the dual requirement independently. Forecloses partial-satisfaction claims at point-of-production. |
| C-44 | R13: V-03 "(1) content -- reproduce TRACE CHARTER's close-line exactly; (2) position -- absolute last line" and V-05 "(1) content -- TRAVERSAL-SCHEMA Area 3 close-line exactly; (2) position -- final content of MANIFEST-N, TABLE-N follows directly" -- numbered list format within the placeholder body. V-01, V-02, V-04 all express both constraints in compound sentence form. Numbered items give each constraint a discrete address that a model must satisfy independently; a compound sentence allows satisfying the surface form without satisfying both components. | C-40 requires both constraints in one instruction; does not specify the enumeration format | Requires the enumeration format to be numbered, making each constraint a discrete independently checkable item. Compound phrasing allows conflation; numbered items structurally prohibit it. |
| C-45 | R13: V-03 "Two requirements, one instruction: (1) ... (2) ..." and V-05 "Two simultaneous constraints -- one instruction: (1) ... (2) ..." -- leading count declaration before constraint enumeration. The opener names the N=2 obligation before the constraints are listed, establishing the contract count at the placeholder's first token. V-01, V-02, V-04 begin with the content reference or positional declaration directly, without a count opener. Without the count opener, a model reading the placeholder may interpret the two constraints as aspects of one compound requirement. | C-40 requires dual constraints; C-44 requires numbered enumeration | Requires the placeholder to open with an explicit N=2 count declaration before enumerating constraints. The count opener establishes the obligation count as the first signal; numbered enumeration (C-44) makes each item independently checkable; entanglement (C-43) declares neither alone suffices. All three together form the complete R13 placeholder cluster. |

---

**R13 triple structure:**

- **C-43** (logical-binding, per-placeholder): entanglement declaration closes the partial-satisfaction loophole; co-location (C-40) is necessary but not sufficient to foreclose the claim that satisfying the content constraint partially satisfies the dual requirement.
- **C-44** (structural-granularity, per-placeholder): numbered enumeration gives each constraint a discrete independently-checkable address; compound phrasing allows conflation at point-of-production.
- **C-45** (contract-establishment, per-placeholder): leading count declaration establishes the N=2 obligation at the placeholder's opening token, before the constraints are enumerated; without it a model can read two constraints as one compound requirement with two aspects.

The three criteria are orthogonal: C-43 can be satisfied without C-44 or C-45 (entanglement declared, no numbering, no count header). C-44 can be satisfied without C-43 or C-45 (constraints numbered, no entanglement, no count header). C-45 can be satisfied without C-43 or C-44 (count opener present, no numbering, no entanglement). Full expression of the dual-constraint placeholder cluster -- the R13 form -- requires all three: C-45 establishes the contract count, C-44 makes each constraint independently addressable, C-43 binds them as mutually inseparable. V-03 and V-05 carry all three; V-01, V-02, V-04 carry none of C-43/C-44/C-45 while still satisfying C-40.

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
| **v14** | **C-43--C-45 (3 new)** | **164** | **R13** |
