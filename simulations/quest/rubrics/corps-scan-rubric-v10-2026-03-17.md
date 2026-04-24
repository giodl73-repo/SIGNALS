# corps-scan Rubric v10 -- 2026-03-17

## What is new in v10

**Four new criteria from R9 (V-01/V-02/V-03/V-05 excellence signals):**

**C-39 -- Cross-manifest verification block: explicit arithmetic runner check before Phase 1 executes**
(requires C-38)
Beyond C-38 (cross-manifest count invariant structurally satisfied). The prompt includes a dedicated pre-execution verification block that explicitly computes the cross-manifest arithmetic — stating the CONSTRAINT MANIFEST TOTAL value, the per-phase test-item-count column values, their sum, and asserting equality — before Phase 1 begins. This block runs as the first model action, making count discrepancies detectable at the earliest possible point: before any phase body is read or any phase output is produced. A prompt where the cross-manifest invariant is satisfied structurally (C-38) but is only verifiable by post-hoc arithmetic does not pass. A prompt where the verification block appears after Phase 1 has started does not pass. The verification block must name the TOTAL value, name each per-phase item count, perform the explicit sum, and assert equality as a visible output directive. Evidence: V-01 "cross-manifest verification block — explicit arithmetic runner check before Phase 1 — discrepancy detectable at earliest possible point." Requires C-38.

**C-40 -- Gate token protocol: typed PASS/FAIL tokens at gate boundaries making gate state a first-class scannable artifact**
(requires C-19 + C-21)
Beyond C-19 (dual gate architecture) and C-21 (gates labeled with category name). Each gate boundary in the prompt directs the model to emit a typed gate-state token — specifically PASS or FAIL — as an explicit output artifact at the gate crossing point. The typed token makes gate state independently scannable: a reviewer locating all gate crossings by searching for the token pair can determine gate outcomes without reading phase body prose, test item lists, or conditional advance logic. A prompt where gates direct conditional advance logic but do not direct explicit typed token emission does not pass. A prompt where typed tokens appear in phase body prose rather than at gate boundary output points does not pass. The token must be emitted as a discrete artifact line at each gate, not embedded in a prose sentence. Evidence: V-02 "gate token protocol — typed PASS/FAIL tokens at gate boundaries — gate state scannable as first-class artifact." Requires C-19 and C-21.

**C-41 -- Numbered scan protocol: deterministic numbered traversal steps for Phase 2 inventory making signal omissions detectable by step-completeness**
(requires C-09 + C-11)
Beyond C-09 (pre-YAML scan inventory listed) and C-11 (inventory formatted as typed table). The Phase 2 scan procedure is expressed as a numbered step sequence anchored to specific scan targets (e.g., Step 1: scan `/src/`, Step 2: scan `/services/`, Step 3: scan `/config/`, Step 4: synthesize into inventory table) that directs the model to traverse a deterministic set of locations in order. Signal omissions become detectable by step-completeness: if the model has executed all N named steps, absence of a signal is structurally distinguished from a skipped step. A scan procedure expressed as prose directives, bullet points, or a single IVR triple without numbered step ordering does not pass. A numbered list that is not anchored to specific named scan targets (e.g., generic "scan the codebase systematically") does not pass. The numbered steps must be countable and each must name a distinct scan target or synthesis action. Evidence: V-03 "numbered scan protocol — deterministic 4-step traversal — signal omissions detectable by step-completeness, not post-hoc gap analysis." Requires C-09 and C-11.

**C-42 -- Full-window compliance coverage: pre-execution, mid-phase, and post-phase controls all simultaneously present**
(requires C-39 + C-40 + C-41)
Beyond C-39 (pre-execution verification block), C-40 (gate token protocol), and C-41 (numbered scan protocol). All three compliance control layers are simultaneously present in the same prompt: (1) pre-execution count verification (C-39) covering the window before Phase 1 begins, (2) numbered scan protocol (C-41) covering the deterministic traversal window during Phase 2, and (3) gate token protocol (C-40) covering the window at each gate boundary between phases. The three controls bracket the full execution window: count integrity is enforced before any phase begins, traversal discipline is enforced during the inventory phase, and gate state is enforced as a typed artifact at each phase transition. A prompt satisfying any two of C-39/C-40/C-41 but not all three does not pass. A prompt where one of the three controls is present but delegated to a subsection of a phase rather than the designated structural position (pre-execution for C-39, Phase 2 body for C-41, gate boundary for C-40) does not pass. Evidence: V-05 "maximum compliance coverage: count integrity before P1, traversal discipline during P2, gate artifacts at boundaries." Requires C-39, C-40, and C-41 to all pass simultaneously.

**Score: 380 → 420 pts max. 38 → 42 criteria. Golden threshold unchanged.**

---

## What carried forward from v9

**C-35 -- Incompleteness predicate expressed as blockquote enabling rendered-markdown scan surface**
(requires C-33)
Beyond C-33 (predicate as first structural element of each phase body). The "Phase N is not complete until X" predicate uses rendered-markdown blockquote syntax (`>` prefix), making it visually and syntactically distinct from surrounding prose, ENTRY blocks, and IVR triple text. The blockquote format creates a fourth independent audit surface beyond the three required by C-31: a reviewer scanning rendered markdown locates all incompleteness predicates by visual inspection of blockquote elements alone, without reading ENTRY blocks, IVR triples, or the phase-contract table. C-33 can pass with bold-caps or plain prose; C-35 requires blockquote syntax. A prompt where predicates satisfy C-33 ordering but use bold-caps or plain prose does not pass. Requires C-33.

**C-36 -- Constraint manifest carries VIOLATION column making it a mini-IVR anti-pattern reference**
(requires C-28 + C-34)
Beyond C-28 (manifest enumerates labels with count) and C-34 (manifest has terminal TOTAL row). The constraint manifest includes a dedicated VIOLATION column alongside each IVR triple label, naming the concrete anti-pattern for that constraint. This converts the manifest from a bare label-and-count list into a mini-IVR reference table: a reviewer can confirm both what is required and what the specific failure looks like from the manifest alone, without navigating to the phase body containing that triple. Anti-patterns for all labeled constraints become scannable from the manifest, creating an independent failure-detection surface that requires no phase-body traversal. A manifest that lists labels, counts, and a TOTAL row but omits the VIOLATION column does not pass. A VIOLATION column present in any other table does not satisfy this criterion. Evidence: V-02 "VIOLATION column makes manifest a mini-IVR anti-pattern reference; anti-patterns scannable from manifest without reading phase bodies." Requires C-28 and C-34 to both pass.

**C-37 -- Phase-contract table carries test-item-count column enabling mechanical cross-check**
(requires C-32)
Beyond C-32 (phase-contract table as front-matter covering all phases). The phase-contract summary table includes a dedicated column stating the number of YES/NO checklist items that each phase's completion test block contains. The count declared in each row must equal the actual number of items present in the corresponding directed completion test block in the phase body. This creates a mechanical cross-check: a reviewer can verify that no test block has been truncated or extended by comparing the table count to the actual item count, without reading full phase body prose. A phase-contract table that includes ENTRY preconditions, incompleteness predicate, test directive, and conditional advance columns but omits the test-item-count column does not pass even if all other phase contract elements are present. A count column in any table other than the phase-contract front-matter table does not satisfy this criterion. Evidence: V-03 "count column in contract table creates cross-check: table count must equal YES/NO items in test block; mechanical discrepancy detection." Requires C-32 to pass.

**C-38 -- Cross-manifest count invariant: CONSTRAINT MANIFEST TOTAL equals sum of phase test-item counts**
(requires C-34 + C-37)
Beyond C-34 (manifest TOTAL row) and C-37 (phase-contract test-item-count column). The CONSTRAINT MANIFEST TOTAL row (declaring the count of labeled IVR triples) and the sum of the per-phase test-item-count column values in the PHASE CONTRACT TABLE declare the same count from two structurally independent front-matter perspectives. In a well-formed prompt the two values must be equal: N labeled IVR triples equals N total completion test items across all phases. A discrepancy between the manifest TOTAL and the sum of phase test-item counts is mechanically detectable by arithmetic on the two front-matter tables without reading any phase body. Having two independent front-matter tables anchoring the same count creates the strongest available cross-manifest invariant: a single table corruption cannot satisfy both tables simultaneously. A prompt where the manifest TOTAL and the phase-contract item-count sum agree but only because the count column is absent in the phase-contract table does not pass — both C-34 and C-37 must be independently satisfied. A prompt where the two counts disagree does not pass even if each table is internally consistent. Evidence: V-05 "Cross-manifest count invariant — CONSTRAINT MANIFEST TOTAL (14) equals sum of all phase test-item counts in PHASE CONTRACT TABLE (P1=2, P2=5, P3=6, P4=1, total=14); discrepancy between the two front-matter values mechanically detectable without reading any phase body." Requires C-34 and C-37 to both pass.

---

## What carried forward from v8

**C-31 -- Multi-surface verification: completion infrastructure anchored on three independent surfaces**
(requires C-28 + C-32 + C-33)
Three structurally independent audit surfaces simultaneously present: (1) constraint manifest (C-28) — all IVR triples enumerable by label scan alone; (2) phase-contract front-matter table (C-32) — all phases, entry preconditions, predicates, test directives, and conditional advances readable without entering phase bodies; (3) canonical predicate phrasing at phase-body openings (C-33) — incompleteness predicates locatable as the first structural element of each phase. Each surface independently sufficient to identify what is required; all three required simultaneously. A prompt with two of three surfaces does not pass. Evidence: V-05 (R7). Requires C-28, C-32, and C-33.

**C-32 -- Phase-contract table as front-matter before any phase body**
A single summary table placed before the first `### PHASE N` header covers all phases, with one row per phase. Minimum columns: phase identifier, ENTRY preconditions, incompleteness predicate summary, test directive, conditional advance instruction. A table placed inside any phase body does not satisfy this criterion. A table placed after Phase 1 has begun does not satisfy this criterion. A phase-contract table present but covering fewer than all phases does not pass.

**C-33 -- Incompleteness predicate is first structural element of each phase body**
(requires C-15)
Beyond C-15 (incompleteness predicate stated per phase). The "Phase N is not complete until X" predicate appears as the first content element inside the phase body section — before the ENTRY block, before the first IVR triple, before any prose preamble. The ordering constraint is strict: ENTRY block before first IVR triple is already required by C-29; C-33 requires the predicate to precede even the ENTRY block. A phase whose first element is an ENTRY block, then a predicate, does not pass. Requires C-15.

**C-34 -- Constraint manifest terminal count row**
(requires C-28)
Beyond C-28 (manifest enumerates labels). The constraint manifest table includes a terminal `TOTAL` row as its final row, stating the total number of labeled IVR triples with an explicit count-verification instruction (e.g., "14 labeled triples — count to verify completeness"). This row allows a reviewer to verify manifest completeness by counting manifest rows and comparing to the stated total without reading phase bodies. A manifest that lists all labels but omits the TOTAL row does not pass. A count appearing in prose above or below the table does not satisfy this criterion. Requires C-28.

---

## What carried forward from v7 and earlier

**C-29 -- Explicit ENTRY contracts at phase start pairing with EXIT contracts**
Each phase body opens with an ENTRY block naming the preconditions that must be satisfied before the phase begins, and each completion test block includes a corresponding EXIT block directing conditional advance. ENTRY and EXIT blocks are structurally paired: every phase has both. A phase with an EXIT block but no ENTRY block does not pass. A phase with an ENTRY block but no EXIT block does not pass.

**C-30 -- Completion infrastructure covers every phase without exception**
Every phase in the prompt — without omission — carries all three completion infrastructure elements: (1) incompleteness predicate, (2) YES/NO checklist completion test block, (3) conditional advance instruction. A prompt where any single phase lacks any one of these three elements does not pass, even if all other phases are fully instrumented.

**C-28 -- META-RULE enumerates all IVR triples by label with count instruction**
(requires C-26)
Beyond C-26 (META-RULE declares informal constraints non-binding). The constraint manifest table following the META-RULE enumerates every labeled IVR triple by its phase-scoped label, and instructs the reviewer to count labels to verify completeness. A META-RULE that declares IVR triples binding but does not enumerate them by label does not pass. A manifest present elsewhere in the document (not immediately following or accompanying the META-RULE) does not satisfy this criterion. Requires C-26.

**C-27 -- Completion test includes explicit conditional advance instruction**
Every phase completion test block directs the model: advance to the next phase only if all items are YES; if any item is NO, resolve the failing item before advancing. The instruction must name the target phase for advance and the recovery action for failure. A completion test that lists YES/NO items but does not state the conditional advance logic does not pass.

**C-26 -- Meta-rule declares informal constraints non-binding**
The prompt includes a META-RULE statement declaring that any directive not expressed as a labeled IVR triple is advisory context only and does not constitute a binding constraint. This rule makes the IVR triple format the exclusive binding constraint vehicle. A prompt with IVR triples but no META-RULE declaration does not pass.

**C-25 -- Each IVR triple carries phase-scoped structural label**
Every IVR triple in the prompt carries a label of the form IVR-PN-X (e.g., IVR-P2-A, IVR-P3-C) where N identifies the phase and X is an alphabetic sequence identifier within that phase. Labels must be unique across the entire prompt. An IVR triple present but without a label, or with a label that does not encode the phase, does not pass.

**C-24 -- Pivot mode candidates enumerated before selection**
Before the selected pivot mode is declared, all available pivot mode options are enumerated with their conditions, and the selected mode is marked SELECTED while all others are marked REJECTED with reasons. A prompt that declares a pivot mode without enumerating alternatives does not pass. A pivot enumeration that lists options without explicit SELECTED/REJECTED marking does not pass.

**C-23 -- Inline detected-from: traceability field in YAML**
(requires C-16)
Every team entry in the generated org.yaml carries a `detected-from:` field naming the specific Phase 2 inventory signal row or repository signal that justified the team's inclusion. The field is inline in the YAML, not in a separate prose section. A team entry without `detected-from:` does not pass. A `detected-from:` value that references a generic category rather than a specific named signal does not pass. Requires C-16.

**C-22 -- Every structural constraint in every phase expressed as IVR triple**
Every constraint that produces a pass/fail outcome across all phases is expressed as a labeled IVR triple. No structural constraint is expressed solely as prose, bold text, or a bullet point. A prompt with a constraint in Phase 4 expressed as a prose requirement but not as an IVR triple does not pass even if all other phases are fully triplified.

**C-21 -- Each gate labeled with category name**
Every gate in the dual gate architecture carries a parenthesized category name immediately after the gate identifier (e.g., GATE 1 (Structural Ordering), GATE 2 (Semantic Traceability)). The category name characterizes the type of failure the gate guards against. A gate identified by number only, without a category label, does not pass.

**C-20 -- Amend phase names explicit anti-pattern**
The Phase 4 amend section includes an IVR triple (IVR-P4-A or equivalent) whose VIOLATION block names the specific soft anti-pattern — e.g., `"Feel free to request adjustments"` or equivalent hedged response — that the phase is designed to replace. The named anti-pattern must be quoted or concretely described; a generic "vague response" label does not pass. The AMEND header or phase body must also restate the anti-pattern as a negative example.

**C-19 -- Dual gate architecture**
(requires C-13)
Two structurally independent gates are present with separate names, separate positions in the prompt, and separate failure conditions. Gate 1 (Structural Ordering): blocks YAML authoring until Phase 2 inventory is complete. Gate 2 (Semantic Traceability): blocks Phase 3 completion until every YAML team entry traces to a Phase 2 inventory row. The two gates guard against distinct failure modes; satisfying one does not satisfy the other. A single gate with two conditions does not pass. Requires C-13.

**C-18 -- Constraints expressed as INVARIANT/VIOLATION/REPAIR triples**
Every labeled constraint carries all three IVR blocks: INVARIANT (what must hold), VIOLATION (the concrete anti-pattern that fails it), and REPAIR (the directed recovery action when violation is detected). An IVR triple missing any one of the three blocks does not pass. A VIOLATION block naming a generic failure category rather than a concrete anti-pattern does not pass. A REPAIR block directing "try again" or equivalent without specific recovery steps does not pass.

**C-17 -- Phase completion tests produced as visible model output**
Each phase includes a named completion test block — e.g., "Phase N Completion Test" — directing the model to produce the YES/NO checklist items as visible output, not as internal reasoning. The block must be named and must direct explicit output. A phase where completion logic is embedded in prose without a named output block does not pass.

**C-16 -- Traceability failure triggers explicit repair instruction**
(requires C-23)
The IVR triple governing YAML team traceability (IVR-P3-A or equivalent) includes a REPAIR block that directs a specific recovery action when a team entry lacks traceability: return to Phase 2, add the missing signal row, re-enter Phase 3. A REPAIR block that says "ensure traceability" without naming the specific recovery sequence does not pass. Requires C-23 (since the repair targets the `detected-from:` field).

**C-15 -- Phase incompleteness predicate stated per phase**
Every phase in the prompt states an incompleteness predicate of the form "Phase N is not complete until X" where X names the specific completion condition. The predicate must name a concrete, verifiable condition, not a general instruction. A phase without an incompleteness predicate does not pass. A predicate stating "Phase N is not complete until you are satisfied" or equivalent non-verifiable condition does not pass.

**C-14 -- Gate row embedded as terminal row of inventory table**
(requires C-11)
The inventory table produced in Phase 2 includes a terminal gate row — e.g., `| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |` — as its final row. This embeds the gate signal directly in the table artifact, making the gate condition inseparable from the inventory it governs. A gate directive appearing below the table in prose does not satisfy this criterion. Requires C-11.

**C-13 -- Hard ordering gate between inventory and YAML**
(requires C-09)
An explicit gate directive blocks YAML block authoring until Phase 2 inventory is complete and the EXIT-P2 checklist is all YES. The gate must name both the blocking condition (inventory incomplete) and the unblock condition (all EXIT-P2 items YES). A prompt where inventory and YAML authoring are in the same phase without an ordering gate does not pass. A prompt where the gate is mentioned but not enforced via a blocking directive does not pass. Requires C-09.

**C-12 -- Pivot rationale cites specific named signal**
(requires C-06)
Beyond C-06 (pivot mode declared with rationale). The pivot rationale names at least one specific Signal column value from the Phase 2 inventory table row that triggered the mode selection. A rationale citing "the signals indicate" or "based on the scan" without quoting a named signal value does not pass. Requires C-06.

**C-11 -- Inventory formatted as typed table**
(requires C-09)
Beyond C-09 (inventory listed). The Phase 2 scan inventory is produced as a markdown table with named columns (minimum: signal name, type/category, location, pivot signal indicator). A bulleted list, a numbered list, or a prose enumeration does not pass even if it contains the correct information. Requires C-09.

**C-10 -- Draft boundary stated before first structural content**
The model's first output in Phase 1 is a blockquote or clearly delimited boundary declaration stating that the output is a draft subject to Phase 4 amendment. This boundary declaration precedes all structural content (inventory, YAML, completion tests). A boundary note appended after structural content does not pass.

**C-09 -- Pre-YAML scan inventory listed**
(requires C-02)
Before any `org.yaml` block is authored, a scan inventory of detected repository signals is produced as a discrete artifact, listing the signals that will justify team entries in the YAML. The inventory must precede the YAML block; a YAML block followed by a traceability section does not pass. Requires C-02.

---

## Criteria Table (All 42)

### ESSENTIAL — C-01 through C-05 (5 criteria, 50 pts)
*All five must pass for a Golden score.*

| # | Criterion | Short Name | Pts |
|---|-----------|------------|-----|
| C-01 | Valid org.yaml code fence with required top-level keys (`org:`, `groups:`, `teams:`, `exec-office:`) | Valid YAML scaffold | 10 |
| C-02 | Team areas derived from repository signals, not from generic org patterns | Signal-derived teams | 10 |
| C-03 | Group structure organizes teams under `groups:` wrapper with nested team entries | Group-wrapped structure | 10 |
| C-04 | Standard roles present per team: 2+ substantive named roles; Inertia Advocate excluded from draft | Roles present | 10 |
| C-05 | Does not write `.roles/` directory or any role files; corps-scan produces draft org.yaml only | No role file writes | 10 |

### RECOMMENDED — C-06 through C-08 (3 criteria, 30 pts)

| # | Criterion | Short Name | Pts |
|---|-----------|------------|-----|
| C-06 | Pivot mode declared with rationale citing scan evidence | Pivot mode declared | 10 |
| C-07 | `exec-office:` placeholder present with `name:` field in YAML | Exec office present | 10 |
| C-08 | Amend options listed with specific amendment commands; anti-pattern named | Amend options listed | 10 |

### ASPIRATIONAL — C-09 through C-42 (34 criteria, 340 pts)

| # | Criterion | Short Name | Deps | Pts |
|---|-----------|------------|------|-----|
| C-09 | Pre-YAML scan inventory listed before any YAML block | Inventory before YAML | C-02 | 10 |
| C-10 | Draft boundary declared as first model output before structural content | Draft boundary first | — | 10 |
| C-11 | Inventory formatted as typed markdown table with named columns | Typed inventory table | C-09 | 10 |
| C-12 | Pivot rationale cites at least one specific named signal from inventory | Pivot cites signal | C-06 | 10 |
| C-13 | Hard ordering gate blocks YAML until Phase 2 inventory complete | Ordering gate | C-09 | 10 |
| C-14 | Gate row embedded as terminal row of inventory table | Gate row in table | C-11 | 10 |
| C-15 | Phase incompleteness predicate stated per phase with verifiable condition | Predicate per phase | — | 10 |
| C-16 | Traceability failure triggers explicit named recovery sequence | Traceability repair | C-23 | 10 |
| C-17 | Phase completion tests produced as named visible model output blocks | Named completion tests | — | 10 |
| C-18 | Constraints expressed as INVARIANT/VIOLATION/REPAIR triples with concrete anti-patterns | IVR triples | — | 10 |
| C-19 | Dual gate architecture: two independent gates with distinct failure conditions | Dual gate | C-13 | 10 |
| C-20 | Amend phase names explicit soft anti-pattern in IVR VIOLATION block | Amend anti-pattern named | — | 10 |
| C-21 | Each gate labeled with parenthesized category name | Gate category label | C-19 | 10 |
| C-22 | Every structural constraint in every phase expressed as IVR triple | Full IVR coverage | C-18 | 10 |
| C-23 | Inline `detected-from:` traceability field on every YAML team entry | detected-from field | C-16 | 10 |
| C-24 | All pivot mode candidates enumerated with SELECTED/REJECTED before mode declared | Pivot enumeration | C-06 | 10 |
| C-25 | Each IVR triple carries phase-scoped label of form IVR-PN-X | Phase-scoped labels | C-18 | 10 |
| C-26 | META-RULE declares informal constraints non-binding; IVR triple format is sole binding vehicle | META-RULE present | — | 10 |
| C-27 | Every completion test includes explicit conditional advance instruction with target phase | Conditional advance | C-17 | 10 |
| C-28 | Constraint manifest enumerates all IVR labels with count-verification instruction | Label manifest | C-26 | 10 |
| C-29 | ENTRY contracts at phase start paired with EXIT contracts in completion test | ENTRY/EXIT pairing | — | 10 |
| C-30 | Completion infrastructure (predicate + test + advance) covers every phase without exception | Full phase coverage | C-15, C-17, C-27 | 10 |
| C-31 | Three independent audit surfaces: manifest, phase-contract table, predicate phrasing | Multi-surface verification | C-28, C-32, C-33 | 10 |
| C-32 | Phase-contract table as front-matter before any phase body, covering all phases | Phase-contract front-matter | — | 10 |
| C-33 | Incompleteness predicate is first structural element of each phase body, before ENTRY block | Predicate-first ordering | C-15 | 10 |
| C-34 | Constraint manifest includes terminal TOTAL row with count and verification instruction | Manifest TOTAL row | C-28 | 10 |
| C-35 | Incompleteness predicate expressed as rendered-markdown blockquote (`>` prefix) | Blockquote predicate | C-33 | 10 |
| C-36 | Constraint manifest carries VIOLATION column making it a mini-IVR reference table | Manifest VIOLATION column | C-28, C-34 | 10 |
| C-37 | Phase-contract table carries test-item-count column enabling mechanical cross-check | Contract count column | C-32 | 10 |
| C-38 | Cross-manifest count invariant: MANIFEST TOTAL equals sum of phase test-item counts | Cross-manifest invariant | C-34, C-37 | 10 |
| C-39 | Pre-execution verification block explicitly computes cross-manifest arithmetic before Phase 1 | Pre-exec verification block | C-38 | 10 |
| C-40 | Gate token protocol: typed PASS/FAIL tokens emitted at gate boundaries as first-class artifacts | Gate token protocol | C-19, C-21 | 10 |
| C-41 | Numbered scan protocol: deterministic numbered steps with named targets for Phase 2 traversal | Numbered scan protocol | C-09, C-11 | 10 |
| C-42 | Full-window coverage: pre-execution (C-39), mid-phase (C-41), and post-phase (C-40) all present | Full-window compliance | C-39, C-40, C-41 | 10 |

---

## Scoring Summary

| Tier | Criteria | Max Pts |
|------|----------|---------|
| Essential | C-01 – C-05 | 50 |
| Recommended | C-06 – C-08 | 30 |
| Aspirational | C-09 – C-42 | 340 |
| **Total** | **42** | **420** |

**Golden threshold**: All 5 Essential criteria pass. (Unchanged from v9.)

**Score interpretation**:

| Range | Label |
|-------|-------|
| 420 / 420 | Perfect |
| 380 – 410 | Near-perfect (missing one or more v10 controls) |
| 340 – 370 | Strong (v9 complete, v10 partially satisfied) |
| 280 – 330 | Solid (core infrastructure complete) |
| < 280 | Developing |

---

## Dependency Graph (v10 additions only)

```
C-38 ──► C-39   (pre-exec verification block)
C-19
  └── C-21 ──► C-40   (gate token protocol)
C-09
  └── C-11 ──► C-41   (numbered scan protocol)

C-39
C-40 ──► C-42   (full-window coverage)
C-41
```

---

## Version History

| Version | Criteria | Max Pts | New Criteria |
|---------|----------|---------|--------------|
| v10 | 42 | 420 | C-39 (pre-exec verification), C-40 (gate tokens), C-41 (numbered scan), C-42 (full-window) |
| v9 | 38 | 380 | C-35 (blockquote predicate), C-36 (manifest VIOLATION col), C-37 (contract count col), C-38 (cross-manifest invariant) |
| v8 | 34 | 340 | C-31 (multi-surface), C-32 (phase-contract front-matter), C-33 (predicate-first), C-34 (manifest TOTAL row) |
