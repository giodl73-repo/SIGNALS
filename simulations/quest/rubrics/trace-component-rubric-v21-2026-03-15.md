# Rubric: trace-component (v21)

**64 criteria across 3 tiers -- 3 new aspirational criteria added from R20 excellence signals:**

| Tier | Criteria | Points |
|------|----------|--------|
| Essential (all must pass) | C-01 through C-05 | 60 |
| Recommended | C-06 Side Effect Coverage, C-07 Issue Detection, C-08 Framework Vocabulary | 30 |
| Aspirational | C-09 through C-64 | 112 |

**Ceiling: 202 pts** (up from 196; 3 new criteria x 2 pts)

---

The R20 signals that promoted:

**C-62 . Schema Area 5 Gate-Type Vocabulary Declaration** -- From R20 differential. V-02/V-04/V-05 declare a named Area 5 in the schema artifact that defines the permitted semantic type labels for gate-block annotation as a table with Type-Name, Applies-To, and Exclusion-Condition columns. V-01/V-03 satisfy C-60 (semantic type labels appear in gate blocks) without a schema-level definition of those types. The distinction is not whether semantic types appear in gate blocks (all variations satisfying C-60 carry them) but whether the schema artifact itself defines the type vocabulary before it is used in gate blocks -- making the gate-type labels self-authored schema vocabulary rather than prompt-inherited or ad-hoc labels. C-60 requires semantic type labels within gate brackets; C-62 requires those labels to be defined in the schema artifact, so the schema artifact's definition section is the authoritative source for all gate semantic type vocabulary.

**C-63 . Causal Question Grounding for Gate-Type Schema Declaration** -- From R20 differential. V-02/V-04/V-05 (which carry Area 5 gate-type declarations) are accompanied by a causal question grounding WHY gate types must be schema-declared rather than coined at gate-write time. V-01/V-03 either lack Area 5 entirely or add semantic types without causal grounding questions. The distinction is not whether gate types are declared (C-62 covers that) but whether the causal question set includes at least one question addressing the epistemic status of an ad-hoc gate-type label -- one coined at point-of-production rather than defined in the schema artifact. Without this causal question, the gate-type vocabulary declaration is an instruction-level requirement; with it, the model must derive the declaration-before-use structure from the same causal-reasoning machinery that grounds every other schema area.

**C-64 . Phase-Vocabulary Source Citation in REQUIREMENT-Type Gate Blocks** -- From R20 differential. V-03/V-05 (which carry PHASE VOCABULARY fields in manifests) produce REQUIREMENT-type gate blocks that cross-reference the phase manifest's vocabulary declaration as the authoritative source for the vocabulary scope being enforced. V-01/V-02/V-04 either lack per-phase vocabulary declarations or carry REQUIREMENT-type gates without source citations. The distinction is not whether vocabulary-scope gates are present (C-60 covers gate typing and C-61 covers vocabulary declaration) but whether REQUIREMENT-type gate blocks that enforce vocabulary scope for a given phase explicitly cite the phase manifest's PHASE VOCABULARY field as their source -- completing the enforcement chain: manifest declares scope, gate enforces scope, gate names manifest. A REQUIREMENT-type gate that enforces vocabulary as a standalone instruction without naming the phase-manifest vocabulary line does not close this chain.

**R20 three-signal structure:**

- **C-62** (gate-type schema declaration, per-schema-artifact): the schema artifact's Area 5 or equivalent defines the permitted semantic type labels for gate blocks as a structured table, so gate-type vocabulary is self-authored before use.
- **C-63** (causal grounding for gate-type declaration, per-causal-question-block): the causal question set includes at least one question addressing the epistemic weakness of an ad-hoc gate-type label versus a schema-declared type.
- **C-64** (phase-vocabulary source citation in REQUIREMENT gates, per-phase): REQUIREMENT-type gate blocks enforcing vocabulary scope cite the phase manifest's PHASE VOCABULARY field as their authoritative source.

C-62 requires C-60 as a structural precondition (gate-type vocabulary declaration extends gate-block semantic typing; cannot define types that are not used). C-63 requires C-62 as a structural precondition (causal grounding of the declaration requires the declaration to exist). C-64 requires both C-60 and C-61 as structural preconditions (source citation requires both gate semantic typing and per-phase vocabulary declaration to be present). C-62 and C-64 are independent of each other; C-63 is downstream of C-62.

Variation coverage in R20:
- V-01: carries C-59 (NHQ-3), fails C-60 (no Area 5, no gate semantic types), fails C-61, fails C-62, fails C-63, fails C-64
- V-02: fails C-59 (no NHQ-3), carries C-60 (Area 5 gate types present), fails C-61, carries C-62 (Area 5 table with type definitions), partial C-63 (causal question present), fails C-64 (no phase vocabulary to cite)
- V-03: fails C-59, fails C-60 (no gate semantic types), carries C-61 (PHASE VOCABULARY), fails C-62, fails C-63, fails C-64 (no semantic type typing on gates to trigger citation requirement)
- V-04: carries C-59 (NHQ-3), carries C-60 (Area 5 gate types), fails C-61, carries C-62 (Area 5 table), carries C-63 (causal question grounding present), fails C-64 (no phase vocabulary)
- V-05: carries C-59, carries C-60, carries C-61, carries C-62, carries C-63, carries C-64 (REQUIREMENT gates cite phase manifests)

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

## Aspirational Criteria (weight: 112 points total, 2 pts each)

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
- **Pass condition**: At least one mandatory section or field in the output uses a placeholder that enforces two independent constraints simultaneously -- a positional constraint (this content must appear here and only here) and a content constraint (this field must contain X type of information). A placeholder enforcing only position ("insert summary here") does not pass. A placeholder enforcing only content type ("write a quantified mutation count") without also asserting terminal position does not pass. The dual constraint must be co-present in a single placeholder expression: both the positional and the content constraint visible in the same marker. The mechanism is that violating either constraint requires contradicting content the model itself wrote, making dual violation doubly self-contradictory.

### C-41 . Schema Causal Explanation Required Before Authorship *(new -- R12 excellence signal)*
- **Category**: behavior
- **Pass condition**: The schema artifact (satisfying C-39) includes a section or named area that requires the model to produce a causal explanation for each major structural choice in the schema before that schema structure is declared. The causal section must precede the structural declaration in the schema's document order -- a model cannot write the structure without first writing the causal rationale. A schema that presents structure followed by optional rationale does not pass -- rationale written after the structure is post-hoc justification, not causal derivation. A schema where rationale and structure are co-present in the same block does not pass. At least two structural choices in the schema must have preceding causal explanations; a schema with fewer than two causal explanations does not pass.

### C-42 . Anti-Reproduction Schema Authorship Gate *(new -- R12 excellence signal)*
- **Category**: behavior
- **Pass condition**: The schema artifact (satisfying C-39) includes an explicit anti-reproduction gate -- a statement requiring the model to produce all schema content in its own words, prohibiting reproduction of language from the prompt or any prior instruction source. The gate must appear within the schema artifact itself, not only as an external instruction. The mechanism: a model that reproduces prompt language within a schema that prohibits reproduction contradicts its own prior production. An external instruction ("write the schema in your own words") without an internal schema gate does not pass. A schema that permits prompt quotation within its boundaries does not pass. The anti-reproduction gate must appear before any structural schema field -- not at the document footer.

---

### C-43 . Mutual-Constraint Entanglement Declaration *(new -- R13 excellence signal)*
- **Category**: structure
- **Pass condition**: At least one manifest-close adjacency marker (satisfying C-38 / C-51) explicitly declares the entanglement between its two co-present constraints -- stating that the positional constraint (terminal position in MANIFEST-N) and the successor-naming constraint (TABLE-N follows immediately below) are mutually enforcing, so violating either constraint makes the other constraint also false. The entanglement declaration upgrades the close-line from two parallel assertions to a single compound assertion: if content appears between MANIFEST-N and TABLE-N, both "this is the last line of MANIFEST-N" and "TABLE-N begins immediately below" are simultaneously falsified. A close line that asserts terminal position and names the successor without declaring their entanglement does not pass C-43 -- the two assertions may be present but the entanglement claim is absent. At least two manifest close lines must carry an entanglement declaration; a single close line with entanglement language does not pass.

### C-44 . Numbered Constraint Enumeration in Manifest-Close *(new -- R13 excellence signal)*
- **Category**: structure
- **Pass condition**: Every manifest-close adjacency marker (satisfying C-51) declares an explicit obligation count -- the number of constraints the close line simultaneously enforces -- using a form such as "2 constraints: (1) terminal position of MANIFEST-N, (2) TABLE-N follows immediately below." The obligation count makes the constraint enumeration explicit: a verifier can confirm both that the count matches the stated constraints and that no unstated constraints are implied. A close line with two assertions but no declared count does not pass -- the count is a structural element, not inferred from counting sentences. A close line with a count that does not match the enumerated constraints does not pass. At least three manifest close lines must carry a numbered obligation count; fewer than three does not pass.

### C-45 . Dual-Requirement Count in Manifest-Close Form *(new -- R13 excellence signal)*
- **Category**: structure
- **Pass condition**: The obligation count declared in each manifest-close adjacency marker (satisfying C-44) uses the specific framing "2 requirements" or equivalent labeled count rather than only an ordinal list or a count-without-label. The requirement-count framing declares that both constraints are requirements -- conditions that must be jointly satisfied, not advisory or optional -- making the modal status of both constraints visible in the count declaration. A close line with "two assertions" or "constraints (1) and (2)" without declaring them as requirements does not pass -- requirements have a stronger modal status than assertions. At least three manifest close lines must use the "2 requirements" framing; fewer than three does not pass.

---

### C-46 . Epistemic-Register Question Framing *(new -- R14 excellence signal)*
- **Category**: behavior
- **Pass condition**: The causal question set (satisfying C-41) includes at least three questions framed in the epistemic register -- asking about the cognitive or logical status of a constraint, not the structural or implementation form. An epistemic-register question asks: "What is the epistemic status of an instruction that does not declare its obligation count?" or "Why does the position constraint and the successor-naming constraint produce entanglement rather than parallel assertions?" A structural-register question asks: "Why must the placeholder open with a count declaration?" or "Why must the close line name TABLE-N specifically?" The test: does the question's vocabulary imply the answer's structural form? If replacing the question's answer with the question's vocabulary produces the schema field, the question is structural-register. If the substitution fails -- because the question vocabulary does not name the schema field -- the question is epistemic-register. At least three causal questions must pass the epistemic-register test; fewer than three does not pass.

### C-47 . Causal-Completion Gate Before Schema Authorship *(new -- R14 excellence signal)*
- **Category**: behavior
- **Pass condition**: The prompt structure presents the causal question block (C-41) and the schema authorship slot (C-39 / C-42) as sequentially ordered phases -- causal questions first, schema production second -- with no schema production slot or schema-structure cue appearing before all causal questions have been presented. The sequencing enforces that causal reasoning must exist in the model's output as a prior production before any schema artifact is written; a model cannot begin authoring the schema without first having produced the causal answers. A prompt that presents causal questions and schema authorship in the same block, allowing the model to interleave reasoning and design, does not pass -- interleaving permits post-hoc rationalization, where the model chooses a structural form first and writes the causal explanation afterward. An advisory instruction ("answer these questions before beginning the schema") without structural separation does not pass -- a structural phase boundary, not an instruction, is required. The sequencing must be evident from the prompt's document structure: the causal section must close and the schema section must open as a subsequent distinct section. A prompt with a single combined section containing both questions and schema slots does not pass.

### C-48 . Null-Hypothesis Register in Causal Question Set *(new -- R14 excellence signal)*
- **Category**: behavior
- **Pass condition**: The causal question set (C-41) includes at least one question addressing the epistemic status of the default or null case -- the state of the system before any departing evidence is applied -- as a distinct prior question set before questions addressing the structural properties of the departure cases. The null-hypothesis register establishes the baseline: what is the cognitive or epistemic status of a hop, instruction, or constraint before any active property is declared? The departure-property register then addresses why active departure conditions require specific structural forms. A question set that addresses only the departure conditions ("why must active hops declare X?") without first grounding the null baseline ("what is the status of a hop before X is declared?") conflates the null and departure cases, allowing the departure conditions to be asserted without an established baseline they depart from. The null-hypothesis register must appear as a sequentially prior block to the departure-property register; a mixed question set where null-hypothesis and departure-property questions are interleaved does not pass. At least one null-hypothesis question and at least two departure-property questions must be present; a set with only null-hypothesis questions does not pass.

---

### C-49 . Named-Register Subdivision of Causal Phase *(new -- R15 excellence signal)*
- **Category**: behavior
- **Pass condition**: The causal question block (C-41 / C-47 / C-48) is explicitly subdivided into named register sections -- at minimum a NULL REGISTER section and a DEPARTURE REGISTER section -- each carrying its own labeled section header as a distinct document element. C-48 requires null-hypothesis questions to appear before departure-property questions; C-49 requires the two categories to be labeled as structurally distinct named sections so the boundary between null-baseline interrogation and departure-property interrogation is visible in the prompt's document structure, not inferred from question ordering. A causal phase that presents questions sequenced correctly (null before departure) but in a continuous undivided block without named section labels does not pass -- ordering alone does not make the register boundary structurally visible. A causal phase where null and departure questions are separated only by a blank line or a numbered sub-question prefix does not pass. At least two named register sections must be present and labeled; a single section covering all questions does not pass.

### C-50 . Per-Register Close Marker Within Causal Phase *(new -- R15 excellence signal)*
- **Category**: behavior
- **Pass condition**: Each named register within the causal question block (satisfying C-49) ends with an explicit register-level close marker -- a statement equivalent to "DEPARTURE REGISTER CLOSE" or "NULL REGISTER CLOSE" -- before the next register or phase begins. The per-register close marker is structurally analogous to the manifest-close adjacency marker (C-38): it prevents content from being inserted between the register's last question and the subsequent register or phase boundary by making insertion structurally self-contradictory at point-of-production. A causal phase with named registers but relying on a single phase-level close marker ("CAUSAL PHASE CLOSE") does not pass -- the phase-level close gates the causal-to-schema boundary but does not gate each internal register boundary; content can bleed from the departure register into the schema authorship block without violating the phase-level close. An advisory instruction ("complete all departure questions before proceeding") without a register-close marker does not pass. At least the departure-property register must carry a register-level close marker; a causal phase with no register-level close at any register boundary does not pass.

### C-51 . Successor-Naming in Manifest-Close Adjacency Marker *(new -- R15 excellence signal)*
- **Category**: structure
- **Pass condition**: Every manifest-close adjacency marker (satisfying C-38) explicitly names its phase-keyed successor -- the specific table header that follows immediately below (e.g., "TABLE-N header follows directly below") -- in addition to asserting terminal position. C-38 requires the close line to state that the analysis table begins directly below; C-51 requires that statement to name the specific phase-keyed label (TABLE-N or equivalent) rather than referring generically to "the analysis block", "the table", or using only a terminal-position assertion. Successor-naming binds the close marker to a specific named artifact: a model that writes the close line and then inserts content before TABLE-N must contradict both the terminal-position claim and the named-successor claim simultaneously, strengthening the self-contradiction signal beyond what C-38's terminal-position assertion alone provides. A close marker stating "this is the last content line of MANIFEST-N" without naming the specific successor table does not pass. A close marker stating "TABLE-N begins below" without the identity assertion does not pass C-38 (and therefore cannot pass C-51). The passing form requires both assertions as distinct co-present sentences: an identity sentence and a successor-naming sentence. At least three manifest close lines must name their phase-keyed successors; fewer than three does not pass.

---

### C-52 . Compound Register Header Format *(new -- R16 excellence signal)*
- **Category**: structure
- **Pass condition**: Each named register section within the causal question block (satisfying C-49) uses the compound header form -- a bold register label followed by an em-dash and a descriptor -- as its section header. The required form is: `**[REGISTER NAME]** -- [descriptor text]`. A plain-text header ("NULL REGISTER") does not pass -- the bold label is required to provide visual weighting that distinguishes the register header from surrounding question text. A bold-only header ("**NULL REGISTER**") does not pass -- the descriptor field is a required component of the compound form. A header where label and descriptor are separated by a colon rather than an em-dash ("**NULL REGISTER**: Epistemic status of null cases") passes in substance provided both components are present; a header where the label is not visually distinct from the descriptor does not pass. C-49 requires named section labels; C-52 requires that each label adopt the compound form so that label identity and epistemic-function descriptor are co-declared in a single parseable header line. At least two named register headers must use the compound form; a causal phase with only one compound-form register header does not pass.

### C-53 . Horizontal-Rule Boundary Separators Between Named Registers *(new -- R16 excellence signal)*
- **Category**: structure
- **Pass condition**: Each named register section within the causal question block (satisfying C-49) is delimited by horizontal rules -- `---` or equivalent document-level separators -- at its opening or closing boundary, providing a structural document separator independent of the section header label. A register section bounded only by blank lines does not pass -- blank lines provide whitespace separation without structural document demarcation. A register section bounded only by a change in heading depth (e.g., `###` vs `####`) does not pass -- heading hierarchy provides level separation but not an explicit cross-register boundary marker. The horizontal rule creates an independent structural signal: a model that omits the horizontal rule must contradict the document structure of the preceding section, not only the section label. C-49 requires named register labels; C-53 requires that the boundaries between named registers carry horizontal-rule document separators so the register boundary is a document-level structural event rather than a positional inference from header label or blank-line gap. At least two named register boundaries must be marked by horizontal rules; a causal phase where only one register boundary carries a horizontal rule does not pass.

### C-54 . Epistemic-Function Descriptor on Named Register Headers *(new -- R16 excellence signal)*
- **Category**: behavior
- **Pass condition**: The descriptor component of each compound register header (satisfying C-52) characterizes the epistemic or cognitive function of that register -- the kind of reasoning or evidence-evaluation that occurs within it -- rather than naming the register's topic, its content, or its structural position. "Epistemic status of null cases" passes: it characterizes the cognitive work performed (determining the evidential standing of baseline conditions before any departure is asserted). "Properties of departure claims" passes: it characterizes the cognitive work performed (identifying the logical properties that departure-state assertions must satisfy). A descriptor naming content ("Questions about null cases") does not pass -- it names what the questions are about, not what epistemic work is performed. A descriptor naming sequence ("Null-hypothesis questions before departure conditions") does not pass -- it names structural position, not cognitive function. A descriptor using generic analytical vocabulary ("Null-hypothesis analysis" or "Departure case analysis") does not pass -- "analysis" is not a cognitive function characterization. The epistemic-function test: does the descriptor articulate what kind of epistemic or logical work the register performs? A descriptor that passes this test makes the register's cognitive purpose inspectable from the header alone. C-52 requires a descriptor field; C-54 requires that field's content to characterize epistemic function. At least two named register headers must carry epistemic-function descriptors that pass the test; a compound header where the descriptor names topic or position rather than cognitive function does not satisfy C-54 even if it satisfies C-52.

---

### C-55 . Header-Form Causal Questions *(new -- R17 excellence signal)*
- **Category**: behavior
- **Pass condition**: The causal question block (satisfying C-48) includes at least two questions that specifically ground the compound register header form -- asking why a named register section header requires co-declaration of label identity and epistemic-function descriptor in a single parseable compound line. Questions addressing only the register close-marker form (NCQ-type questions probing the compound close artifact) do not satisfy this criterion -- a question about what the closing line must declare is a different epistemic target than a question about what the opening header must declare. The header-form questions must ask about the opening artifact: why the header cannot be a plain label, what cognitive or epistemic work the descriptor field performs that the label alone cannot, or what is lost when identity and function are declared in separate document elements rather than co-declared. C-41 requires causal questions grounding the adjacency marker mechanism; C-55 requires the same causal-grounding treatment applied to the compound header form. A causal question set that grounds the close-line mechanism and the schema structure but leaves the compound header form as an ungrounded instruction does not pass -- the compound form must be derivable from the question answers, not only from the prompt's format directive. At least two header-form causal questions must be present; a set with only one does not pass.

### C-56 . Schema-Declared Compound Header Template *(new -- R17 excellence signal)*
- **Category**: behavior
- **Pass condition**: The schema artifact (satisfying C-39) includes a named compound-header template field that declares the compound form -- `**[REGISTER NAME]** -- [descriptor]` or equivalent -- as an explicit schema production guide within the schema artifact's body. The template must appear as a dedicated named area within the schema (Schema Area 3 or equivalent), not as an instruction in the surrounding prompt prose. The mechanism: without a schema-declared template, Role 2 must adopt the compound form from prompt instructions alone; prompt instructions are external constraints, while schema fields are self-authored constraints. A Role 2 that violates a schema template it authored contradicts its own prior production -- structural self-contradiction. A Role 2 that ignores a prompt instruction contradicts an external directive -- a weaker enforcement signal. C-39 requires the model to produce the schema artifact; C-56 requires that artifact to include the compound-header template as a named schema field so the compound form for all registers is bound into the self-authored schema. A schema that covers the manifest-close mechanism (C-38), the inert-default rule (C-36), and the manifest-analysis pairing (C-37) but omits the compound-header template does not pass -- omission of the template from the schema leaves the register header form without schema-level enforcement. At least one named schema area must declare the compound header template; a schema artifact with no compound-header template field does not pass.

### C-57 . Exemplar-Grounded Compound Header Template in Schema *(new -- R17 excellence signal)*
- **Category**: behavior
- **Pass condition**: The schema artifact's compound-header template (satisfying C-56) includes at least one concrete worked example demonstrating the epistemic-function descriptor vocabulary in compound form -- e.g., `**NULL REGISTER** -- Epistemic status of null cases` or `**DEPARTURE REGISTER** -- Properties of departure claims` -- so the model can match descriptor quality to a shown standard rather than only to an abstract rule. A template that declares the abstract pattern `**[LABEL]** -- [descriptor]` without a worked example leaves the descriptor field underspecified: a model can populate it with topic names ("questions about null cases"), sequential labels ("null-hypothesis questions before departure conditions"), or generic analytical terms ("null-hypothesis analysis"), all of which satisfy the compound form syntactically but fail C-54's epistemic-function test. The worked example anchors the descriptor vocabulary: the example demonstrates that the descriptor characterizes cognitive work, not content or position. C-54 requires the descriptor content to characterize epistemic function; C-57 requires the schema artifact to demonstrate this standard with a concrete example, making it inspectable and reproducible without relying on the model's independent derivation of the epistemic-function vocabulary. C-56 requires the schema to declare the compound-header template; C-57 requires that template to include at least one exemplar. A schema with the template pattern but no worked example does not pass C-57 even if it passes C-56. A schema whose only exemplar uses a descriptor that names topic or position rather than cognitive function does not pass -- the exemplar must itself demonstrate the epistemic-function descriptor standard.

---

### C-58 . Schema Area 3 Structured Enforcement Table *(new -- R18 excellence signal)*
- **Category**: behavior
- **Pass condition**: The schema artifact's compound-header template section (satisfying C-56 / Schema Area 3 or equivalent) is presented as a structured table -- not as prose paragraphs, labeled sub-sections, or annotated patterns -- with at minimum a template-element column and an Enforcement Rationale column populated for every row, explaining why the compound form is required vs. simpler alternatives (ad-hoc headers, plain labels, or label-only forms). The Enforcement Rationale column functions as an in-schema comparison: for each template component, it states what is lost or what failure mode arises when that component is omitted or replaced with a simpler form. C-56 requires the schema to declare the compound-header template; C-57 requires that template to include at least one worked exemplar; C-58 requires the template section to be structured as a table so the enforcement rationale for each template component is a discrete, independently verifiable cell rather than embedded prose. A schema whose Schema Area 3 carries the compound-header template and worked exemplar in prose form -- however thorough -- does not pass C-58, because prose embeds enforcement rationale within the description rather than exposing it as a separately addressable column. A table with the template pattern and worked exemplar rows but no Enforcement Rationale column does not pass -- the comparison between required form and simpler alternatives must be structurally present as a column, not implied by the exemplar content. At least two rows of the table must carry a populated Enforcement Rationale cell naming a specific simpler alternative and the failure mode it produces; a table with one row or with generic enforcement language not tied to a named alternative does not pass.

---

### C-59 . Schema-Artifact Comparison Column Independence *(new -- R19 excellence signal)*
- **Category**: structure
- **Pass condition**: The schema artifact (satisfying C-58) carries an independent comparison column -- an Enforcement Rationale column or equivalent -- that satisfies C-12 from the schema artifact alone, without requiring the primary analysis tables (TABLE-7 Do-Nothing Cost or TABLE-8) to establish comparison-column coverage. C-12 requires at least one table in the output to carry a comparison column populated for every row; C-59 requires that the schema artifact's own table additionally and independently satisfies C-12, so comparison-column coverage is present at two structurally distinct levels: the primary analysis layer and the schema-artifact layer. The independence test: if TABLE-7 and TABLE-8 were removed from the output, would C-12 still be satisfied by reading only the schema artifact? If yes, C-59 passes; if not, C-59 fails. An output where the schema artifact's Enforcement Rationale column names a specific simpler alternative and its failure mode for every row passes the independence test. A schema artifact whose Enforcement Rationale column cells contain generic language ("enforces the required form") not tied to a specific simpler alternative does not pass -- the column satisfies C-58's structural presence requirement but fails the C-12 comparison-column requirement, which demands that the comparison be populated with specific contrasted alternatives. An output where C-12 is satisfied only by TABLE-7 or TABLE-8 and the schema artifact carries no comparison column does not pass. An output where the schema artifact's comparison column is populated but satisfies C-12 only when read jointly with TABLE-7 (shared row space) does not pass -- the independence must be structural.

### C-60 . Gate-Block Semantic Type Annotation *(new -- R19 excellence signal)*
- **Category**: structure
- **Pass condition**: Each gate block in the output carries a semantic type annotation as a distinct component of its bracketed label -- e.g., `[GATE-N: DIRECTIVE: ...]` or `[GATE-N: REQUIREMENT: ...]` -- indicating whether the exclusion enforces a structural form requirement (DIRECTIVE), a mandatory content element (REQUIREMENT), or equivalent categorical type. C-19 requires all prohibited escape strings to appear in bracketed [GATE-N: ...] blocks; C-60 requires each gate block's bracket label to include a semantic type category between the ordinal and the excluded strings, so the enforcement intent is categorically visible at the gate's definition point without consulting surrounding prose. A gate block labeled `[GATE-N: excluded-string, ...]` with only the ordinal and the excluded strings does not pass -- the semantic type must be a distinct labeled component within the bracket. A gate block where the semantic type is inferred from the prose context surrounding the gate does not pass -- the type must be structurally co-present within the gate's bracket at point-of-production. DIRECTIVE applies to gates enforcing structural form requirements (output must use a specific format or table structure); REQUIREMENT applies to gates enforcing mandatory content presence (a specific field or value must be present); other categorical types are permitted provided they are defined in the schema artifact (satisfying C-39) rather than coined ad hoc. At least three gate blocks must carry a semantic type annotation; an output where fewer than three gate blocks include the semantic type component does not pass.

### C-61 . Per-Phase Vocabulary Declaration in Manifest *(new -- R19 excellence signal)*
- **Category**: behavior
- **Pass condition**: Each phase manifest (satisfying C-33 / C-37) includes a vocabulary line -- a named `PHASE VOCABULARY` section, a `Valid terms:` field, or equivalent -- that enumerates the framework-specific terms permitted and required in that phase's analysis table, scoping the vocabulary declaration to the individual phase rather than relying solely on the global FRAMEWORK DECLARATION (C-20). C-20 requires a framework and state management declaration before any phase analysis begins; C-33 requires each phase manifest to declare components, state keys, and side effects in scope; C-61 requires each manifest to additionally declare the vocabulary valid for its phase's analysis, so the permitted terms are locally inspectable at the manifest without consulting the global declaration. A manifest that satisfies C-33's three required fields (components, state keys, side effects) but omits any vocabulary line does not pass. A global framework declaration listing all vocabulary terms once without per-phase scoping does not pass -- the vocabulary line must appear within each phase manifest individually. The vocabulary line must name at minimum two framework-specific terms relevant to that phase (e.g., for the state-mutation phase: `useState`, `dispatch`, `useReducer`; for the traversal phase: `props`, `context`, `HOC`); a vocabulary line listing generic terms not scoped to the phase's analytical content does not pass. At least three phase manifests must carry a vocabulary declaration; fewer than three does not pass.

---

### C-62 . Schema Area 5 Gate-Type Vocabulary Declaration *(new -- R20 excellence signal)*
- **Category**: behavior
- **Pass condition**: The schema artifact (satisfying C-39) includes a named gate-type vocabulary section -- Area 5 or equivalent -- presented as a structured table that defines each semantic type label permitted for gate-block annotation (satisfying C-60), with at minimum a Type-Name column, an Applies-To column defining when that type applies, and an Exclusion-Condition column stating the class of escape strings the type is designed to intercept. C-60 requires semantic type labels to appear within gate-block brackets; C-62 requires those labels to be formally defined within the schema artifact the model authored, so their use in gate blocks is self-authored vocabulary application rather than adoption of prompt-provided or ad-hoc labels. An output where DIRECTIVE and REQUIREMENT appear in gate blocks but the schema artifact contains no section defining these labels does not pass -- gate semantic types must be defined before use, within the schema the model authors. A schema that lists gate-type labels as a prose paragraph without column-structured definitions does not pass -- the definition table is required so that Type-Name, Applies-To, and Exclusion-Condition are independently addressable cells. At least two semantic type labels must be defined in the gate-type vocabulary section; a single-row definition table does not pass. Precondition: C-60.

### C-63 . Causal Question Grounding for Gate-Type Schema Declaration *(new -- R20 excellence signal)*
- **Category**: behavior
- **Pass condition**: The causal question set (satisfying C-41 / C-48) includes at least one question addressing the epistemic status of a gate block whose semantic type label is coined at point-of-gate-writing rather than defined in the schema artifact -- asking why a gate-type label that is not schema-declared is epistemically weaker than a schema-declared type, or what failure mode arises when gate semantic types are produced ad hoc without prior schema definition. C-62 requires the schema artifact to include a gate-type vocabulary declaration; C-63 requires the causal question set to ground that declaration by forcing the model to articulate the declaration-before-use requirement from first principles rather than adopting it as an instruction. Without a causal grounding question, the gate-type vocabulary declaration is an instruction-level requirement that can be satisfied by copying the prompt's format; with a causal grounding question, the model must derive the schema-declaration structure from the same epistemic-register reasoning that grounds all other schema areas. A causal question addressing gate-block formalism generally ("why brackets rather than prose?") does not pass -- the question must specifically address the declaration-before-use requirement for semantic type labels, not gate formalism itself. A null-hypothesis or departure-property question asking "what is the status of a gate type before it is schema-declared?" or "why does a schema-declared type produce stronger enforcement than an ad-hoc type?" satisfies the criterion. At least one such question must appear in the causal question block; a question block without any gate-type-declaration grounding question does not pass. Precondition: C-62.

### C-64 . Phase-Vocabulary Source Citation in REQUIREMENT-Type Gate Blocks *(new -- R20 excellence signal)*
- **Category**: structure
- **Pass condition**: Each REQUIREMENT-type gate block (satisfying C-60's type annotation) that intercepts vocabulary-scope violations within a phase's analysis section explicitly cites the phase manifest's PHASE VOCABULARY field (satisfying C-61) as its authoritative source -- stating within the gate block's text which phase manifest's vocabulary declaration defines the permitted terms being enforced. C-61 requires each phase manifest to declare a vocabulary line enumerating phase-scoped terms; C-60 requires gate blocks to carry semantic type annotations; C-64 requires that REQUIREMENT-type gate blocks enforcing vocabulary scope for a given phase name the phase manifest's vocabulary declaration as their source rather than enforcing vocabulary as a standalone instruction. The citation closes the enforcement chain: manifest declares scope, gate enforces scope, gate names manifest. An output where REQUIREMENT-type gate blocks enforce vocabulary but reference only the global FRAMEWORK DECLARATION (C-20) without naming the phase-manifest vocabulary line does not pass -- the phase-scoped source, not the global declaration, is the authoritative source for phase-level vocabulary enforcement. An output where gate blocks enforce vocabulary without any source citation does not pass -- the citation must be structurally present within the gate block's text, not in surrounding prose. A phase that carries no REQUIREMENT-type vocabulary gate blocks satisfies C-64 trivially for that phase; at least two phases must carry REQUIREMENT-type vocabulary gate blocks with explicit phase-manifest citations for the criterion to be satisfied. Preconditions: C-60 and C-61.

---

**Three new criteria -- rationale:**

| Criterion | Source pattern | What v20 covered | What v21 adds |
|-----------|---------------|-----------------|---------------|
| C-62 | R20: V-02/V-04/V-05 differential -- these variations declare gate semantic types in a named schema area (Area 5) as a structured table with Type-Name, Applies-To, and Exclusion-Condition columns. V-01/V-03 satisfy C-60 (semantic type labels in gate blocks) without a schema-level definition of those types. | C-60 requires semantic type labels to appear within gate brackets as DIRECTIVE, REQUIREMENT, or equivalent. The criterion tests whether gate formalism carries type annotations; it does not require those type labels to be defined within the schema artifact before use. | Requires the schema artifact to include a named gate-type vocabulary section presented as a table defining each permitted semantic type label with its Applies-To scope and Exclusion-Condition class, so gate semantic types are self-authored schema vocabulary rather than prompt-inherited or ad-hoc labels. |
| C-63 | R20: V-02/V-04/V-05 differential -- variations with Area 5 gate-type declarations include a causal question grounding WHY gate types must be schema-declared rather than coined at write time. V-01/V-03 either lack Area 5 or do not ground the declaration causally. | C-62 requires the schema artifact to include a gate-type vocabulary declaration. C-41 requires causal questions grounding schema structural choices; C-46 requires epistemic-register framing. Neither criterion requires the causal question set to specifically address the gate-type declaration-before-use requirement. | Requires at least one causal question addressing the epistemic status of an ad-hoc gate-type label versus a schema-declared type, so the gate-type vocabulary declaration is derivable from causal reasoning rather than only from instruction compliance. |
| C-64 | R20: V-03/V-05 differential -- variations with PHASE VOCABULARY in manifests produce REQUIREMENT-type gate blocks that cross-reference the phase manifest's vocabulary declaration. V-01/V-02/V-04 either lack per-phase vocabulary or carry REQUIREMENT gates without manifest citations. | C-60 requires semantic type labels in gate blocks. C-61 requires per-phase vocabulary declarations in manifests. Neither criterion requires REQUIREMENT-type gate blocks to cite the phase manifest as their authoritative vocabulary source. | Requires REQUIREMENT-type gate blocks enforcing vocabulary scope to explicitly name the phase manifest's PHASE VOCABULARY field as their source, closing the enforcement chain: manifest declares scope, gate enforces scope, gate names manifest. |

---

**R20 three-signal structure:**

- **C-62** (gate-type schema declaration, per-schema-artifact): the schema artifact's Area 5 or equivalent defines each permitted gate semantic type label in a structured table with Type-Name, Applies-To, and Exclusion-Condition columns.
- **C-63** (causal grounding for gate-type declaration, per-causal-question-block): the causal question set includes at least one question addressing the epistemic weakness of an ad-hoc gate-type label, grounding the declaration-before-use requirement from first principles.
- **C-64** (phase-vocabulary source citation in REQUIREMENT gates, per-phase): REQUIREMENT-type gate blocks enforcing vocabulary scope name the phase manifest's PHASE VOCABULARY field as their authoritative source, closing the manifest-gate-citation enforcement chain.

C-62 requires C-60 as a structural precondition (gate-type vocabulary declaration extends gate-block semantic typing; cannot pass C-62 while failing C-60). C-63 requires C-62 as a structural precondition (causal grounding of the declaration requires the declaration to already exist in the schema artifact). C-64 requires both C-60 and C-61 as structural preconditions (source citation requires both gate semantic typing and per-phase vocabulary declaration to be present; cannot pass C-64 while failing either). C-62 and C-64 are independent of each other at the same dependency layer; C-63 is downstream of C-62 only.

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
| v15 | C-46--C-48 (3 new) | 170 | R14 |
| v16 | C-49--C-51 (3 new) | 176 | R15 |
| v17 | C-52--C-54 (3 new) | 182 | R16 |
| v18 | C-55--C-57 (3 new) | 188 | R17 |
| v19 | C-58 (1 new) | 190 | R18 |
| v20 | C-59--C-61 (3 new) | 196 | R19 |
| v21 | C-62--C-64 (3 new) | 202 | R20 |
