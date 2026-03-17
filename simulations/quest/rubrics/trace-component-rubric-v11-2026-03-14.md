**trace-component-rubric-v11** written to `simulations/quest/rubrics/trace-component-rubric-v11-2026-03-14.md`.

---

## Two new criteria from R10 excellence signals

**C-36 . Inert-as-Default Direction Schema** *(R10 V-03 strong pass on C-34)*

V-03 listed `<-> inert` first in the Direction column's permitted values. This inverts the enforcement polarity from C-34: instead of requiring a model to remember to mark inert hops, the schema makes inertia the syntactic default and forces every active hop to declare departure. The distinction — annotation requirement vs. schema-structure requirement — is why V-03 scored 143/144 (highest in R10).

Pass condition: Direction column lists `<-> inert` first; active codes (prop-pass, event-propagate, dispatch, effect-trigger, context-provide) are named departures. Active-codes-first or inert-as-trailing-exception fails.

**C-37 . Manifest-Analysis Paired Block Structure** *(R10 V-04 "most machine-checkable" designation)*

V-04's MANIFEST-N/TABLE-N adjacent pairing makes the manifest-to-analysis gating relationship verifiable by inspection, not positional inference. C-33 only requires manifests to precede phases; a document-header manifest satisfies C-33 but can silently decouple from specific phases. Adjacent labeled pairs close that gap.

Pass condition: Each phase appears as consecutive MANIFEST-N / TABLE-N blocks with matching N; no intervening content; at least 3 pairs required. Header-manifest pattern fails.

---

**Updated ceiling: 148 pts** (29 aspirational criteria × 2 pts + 90 essential/recommended)
ss condition**: At least two named components in the traversal path are shown with a clear parent->child or handler->provider direction. A flat list of components with no structural relationship does not pass.

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

## Aspirational Criteria (weight: 58 points total, 2 pts each)

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

**Two new criteria -- rationale:**

| Criterion | Source pattern | What v10 covered | What v11 adds |
|-----------|---------------|-----------------|---------------|
| C-36 | R10: V-03 STRONG PASS on C-34 -- listing `<-> inert` first in the Direction column's permitted values inverts the enforcement polarity. C-34 requires marking inert hops; C-36 requires the schema to treat inertia as the syntactic default so active hops must declare departure. V-03 scored 143/144 (highest R10 score) on this design. | C-34 requires every inert hop to carry an explicit marker; C-28 requires per-hop direction annotation | Requires the direction schema itself to position inert as the default -- so the column structure enforces departure-declaration rather than relying on a model to remember to mark inert hops. Closes the gap between compliant annotation and structurally enforced annotation. |
| C-37 | R10: V-04 MANIFEST-N/TABLE-N paired blocks received the designation "most machine-checkable structure." C-33 requires manifests to precede phases; C-37 requires the pairing to be positionally adjacent with matching labels. V-04 scored 142/144; its MANIFEST-1/TABLE-1 structure was the R10 structural high-water mark. | C-33 requires per-phase manifests gating each analysis section | Requires the manifest and its analysis table to form an adjacent labeled pair (MANIFEST-N / TABLE-N) so the gating relationship is verifiable by structural inspection, not positional inference. A document-header manifest satisfies C-33 but fails C-37 because its coupling to specific phases is implicit. |

---

**R10 pair structure:**

- **C-36** (direction schema inversion): inertia is the syntactic default; active hops must declare departure. Enforces the inert/active distinction at the schema level, not the annotation level.
- **C-37** (manifest-analysis adjacency): each manifest is structurally coupled to its analysis table by position and label. Enforces the gating relationship at the block level, not the document level.

The two work together: C-36 ensures the traversal's Direction column cannot silently omit inert hops (they are the default, not the exception), and C-37 ensures each phase's manifest is provably coupled to its analysis rather than functioning as a general document header. Both extend the R9 triad's completeness-forward enforcement (C-33) and inert-hop explicitness (C-34) from annotation requirements to schema-structure requirements.

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
| **v11** | **C-36--C-37 (2 new)** | **148** | **R10** |
