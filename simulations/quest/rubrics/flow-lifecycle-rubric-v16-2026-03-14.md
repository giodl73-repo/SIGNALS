Here is the complete updated rubric:

---

## What changed v15 -> v16

Three new aspirational criteria extracted from R15 excellence signals. Formula `/39` -> `/42`.

---

## C-48 -- Incumbent Baseline Phase-Coverage Back-Reference (`depth`, C-48->C-46)

C-46 opened the Baseline->Phase direction: PHASE ENTRY CONTRACT blocks carry `IM Reference:` sub-fields citing IM-IDs active as risks entering each phase. C-48 closes this direction bidirectionally at the baseline-row level: each row in the INCUMBENT BASELINE table carries a named `Phase Refs:` sub-field enumerating every PHASE ENTRY CONTRACT where this IM-ID appears in its `IM Reference:` field. Converts the one-directional Baseline->Phase trace (C-46) into a per-row navigable lookup from baseline to phases. CHAIN STATUS gains a `Phase->Baseline` direction (bidirectional complement to Baseline->Phase). IM-IDs with no active phase references carry explicit NONE sentinel. Enumeration must be consistent with C-46 sub-fields; string comparison only, no inference. Sourced from V-05 (INCUMBENT BASELINE rows carrying `Phase Refs:` back-reference to PHASE ENTRY CONTRACT `IM Reference:` fields, closing the bidirectional baseline-to-phase chain at source).

## C-49 -- Exception Block Triple-Citation Architecture Declaration (`format`, C-49->C-40+C-42+C-47)

C-40 established `Role Ref:` in EX blocks (Role->Exception direction). C-42 established `Bottleneck Ref:` (B-NN->Exception direction). C-47 established `IM Ref:` (Baseline->Exception direction). Together the three sub-fields make each EX block the convergence point for three independent traceability chains, but their co-presence is implicit. C-49 requires an explicit SECTION A preamble or EXCEPTION BLOCK ARCHITECTURE header that names all three citation sub-fields as a declared unit: `Role Ref:` (R-ID namespace), `Bottleneck Ref:` (B-ID namespace), `IM Ref:` (IM-ID namespace) -- with an explicit orthogonality declaration asserting that the three ID namespaces are distinct and independently verifiable by string comparison. C-49 is to the exception-block triple-citation system what C-45 is to the phase-gate three-field contract: a single naming decision that binds three independently established citation fields into a declared architectural unit, making EX block completeness format-verifiable from the preamble alone. Sourced from V-05 (SECTION A opening carrying explicit triple-citation architecture header with namespace labels and orthogonality assertion).

## C-50 -- CHAIN STATUS Four-Direction Completeness Inventory (`depth`, C-50->C-46+C-47)

With C-42 (`B-NN->Exception`), C-43 (`Phase-exit-sequence`), C-46 (`Baseline->Phase`), and C-47 (`Baseline->Exception`) established, four named traceability directions exist in the CHAIN STATUS section. C-50 requires the CHAIN STATUS section to open with an explicit DIRECTION INVENTORY block that enumerates all four directions by their canonical names, declares each PRESENT or ABSENT, and cites the section or sub-field that carries it. Converts the implicit multi-directional CHAIN STATUS from a prose summary into an indexed direction register, making completeness of chain coverage format-verifiable without document traversal. Directions explicitly declared out-of-scope may carry a NOT-APPLICABLE sentinel with rationale; absent inventory block is a fail regardless of direction content. Sourced from V-05 (CHAIN STATUS opening with explicit four-direction inventory listing all four directions with PRESENT declarations and section citations).

---

## R15 retrospective scoring under v16

| Variation | C-48 | C-49 | C-50 | Aspirational | Score |
|-----------|:----:|:----:|:----:|:------------:|-------|
| V-01 | FAIL | FAIL | FAIL | 34/42 | 8.095 |
| V-02 | FAIL | FAIL | FAIL | 35/42 | 8.333 |
| V-03 | FAIL | FAIL | FAIL | 36/42 | 8.571 |
| V-04 | FAIL | FAIL | FAIL | 35/42 | 8.333 |
| V-05 | **PASS** | **PASS** | **PASS** | 42/42 | **10.000** |

V-04 fails C-48 because it has `IM Reference:` in PHASE ENTRY CONTRACT (C-46) but does not carry `Phase Refs:` back-references in the INCUMBENT BASELINE rows -- C-48 requires the source table to be updated, not only the destination sub-field. C-49 requires C-47 as a prerequisite (all three citation fields must coexist before the architecture declaration is meaningful), which only V-05 achieves. C-50 requires all four directions established; V-01 through V-04 each fail at least one of C-46/C-47, making a complete four-direction inventory impossible.

---

**Structural symmetry notes:**

- **C-48 mirrors C-44** -- C-44 gave B-NN blocks `Exception Refs:` (source-end enumeration for B-NN->Exception). C-48 gives INCUMBENT BASELINE rows `Phase Refs:` (source-end enumeration for Baseline->Phase). Pattern: traceability direction established one round, bidirectional source-end complement the next.

- **C-49 mirrors C-45** -- C-45 declared the three-field phase gate system as a named unit. C-49 declares the three-citation EX block system as a named unit. Both are `format` criteria adding zero new fields, only an explicit architectural declaration that makes implicit multi-field co-presence verifiable from the preamble.

- **C-50 closes CHAIN STATUS evolution** -- C-20 (gate declared), C-23 (section isolated), C-42/C-43/C-46/C-47 (four directions established), C-50 (direction inventory makes completeness an indexed register). The DIRECTION INVENTORY block becomes the canonical index for CHAIN STATUS.

**Updated dependency chain:**
```
...previous lines unchanged...
C-48->C-46; C-49->C-40+C-42+C-47; C-50->C-46+C-47
```

**Formula:** `aspirational_pass / 42 * 10` -- golden threshold unchanged at 9.0 (requires 38/42 aspirational). Total criteria: 50.

---

The full rubric table (Essential C-01–C-05, Recommended C-06–C-08, Aspirational C-09–C-50) is written to `flow-lifecycle-rubric-v16-2026-03-14.md`.
ock level. C-45 declared the three-field phase gate system as a named unit. C-49 declares the three-citation exception block system as a named unit. Both are `format` criteria: they add zero new structural elements, only an explicit naming decision that makes an implicit multi-field architecture declared and verifiable from the preamble alone.

- **C-50** closes the CHAIN STATUS evolution. Starting from C-20 (gate declared), C-23 (section isolated), through four directions now registered, C-50 adds a direction inventory that makes completeness of chain coverage formally verifiable without traversal. The DIRECTION INVENTORY block becomes the canonical index for CHAIN STATUS.

**C-48 dependency:** C-48->C-46 (which already depends on C-34+C-41). The `Phase Refs:` sub-field in each INCUMBENT BASELINE row is only meaningful after C-46 has established that PHASE ENTRY CONTRACT blocks carry `IM Reference:` sub-fields pointing back to baseline rows.

**C-49 dependency:** C-49->C-40+C-42+C-47. All three citation sub-fields must be independently established before a unified architecture declaration is meaningful. The declaration names sub-fields that must already exist in the structural contract.

**C-50 dependency:** C-50->C-46+C-47 (which transitively pull in C-42, C-43). The four-direction inventory is only complete when all four directions are established; the inventory gate cannot pass if any of its declared directions is absent from the document.

**Full dependency chain (v16):**
- C-18->C-15; C-19->C-16; C-20->C-14+C-16; C-21->C-13+C-15+C-17
- C-22->C-19; C-23->C-20
- C-24->C-22; C-25->C-23; C-26->C-22
- C-27->C-26
- C-28->C-27; C-29->C-27; C-30->C-24+C-27
- C-31->C-29; C-32->C-30
- C-33->C-28+C-24
- C-34->C-04; C-35->C-34; C-36->C-04
- C-37->C-36+C-04; C-38->C-12; C-39->C-34+C-38
- C-40->C-38+C-13; C-41->C-36
- C-42->C-04+C-13; C-43->C-37+C-41
- C-44->C-42; C-45->C-43+C-41
- C-46->C-34+C-41; C-47->C-42+C-46
- **C-48->C-46; C-49->C-40+C-42+C-47; C-50->C-46+C-47**

**Formula:** `aspirational_pass / 42 * 10` -- golden threshold unchanged at 9.0 (requires 38/42 aspirational).

---

# flow-lifecycle -- Rubric v16

**5 Essential (60 pts)**

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | State Transition Coverage -- every state has named entry condition + at least one labeled exit | correctness |
| C-02 | Exception Flow Identification -- 3+ process-specific exception flows to terminal | coverage |
| C-03 | Role Assignment Accuracy -- domain-specific roles at every decision point and gate | correctness |
| C-04 | Bottleneck and Gap Identification -- 2+ bottlenecks with cause + impact, 1+ gaps with rationale | depth |
| C-05 | Terminal State Completeness -- all success and failure/cancel terminals declared; every branch reaches one | correctness |

**3 Recommended (30 pts)**

| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | Parallel Path Modeling -- at least one fork/join with labeled join condition | depth |
| C-07 | Edge Case Enumeration -- 3+ edge cases distinct from C-02, each with trigger + why problematic + correct response | coverage |
| C-08 | Decision Point Explicitness -- every branch has labeled condition + owner role + fallback | format |

**42 Aspirational (10 pts)**

| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | Cross-Process Interaction Modeling -- at least one inter-process handoff contract | depth |
| C-10 | SLA and Timing Analysis -- 3+ nodes annotated with SLA vs. typical, at-risk flags | depth |
| C-11 | Decision Supplement Block Structure -- per-decision structured block with Fallback field | format |
| C-12 | Role Registry Gate -- pre-declared domain registry with anti-generic validation before tracing | correctness |
| C-13 | Phase-Scoped Exception Traces -- each exception trace anchored to its originating phase | coverage |
| C-14 | SLA-to-Bottleneck Evidence Chain -- SLA at-risk entries cross-referenced to bottleneck IDs | depth |
| C-15 | Exception-First Structural Position -- exception sections structurally precede state tables per phase | format |
| C-16 | Bidirectional SLA-Bottleneck Cross-Reference -- B-NN entries cite affected SLA nodes; chain runs both directions | depth |
| C-17 | Constructed-Answer Format for Exception Sections -- exception and edge-case sections use labeled sub-field answers, not table cells | format |
| C-18 | Ordinal-Label Structural Enforcement -- SECTION A/B (or equivalent ordinal) labels encode exception-first ordering as a named constraint | format |
| C-19 | Backward-Chain Evidence Injection -- B-NN blocks contain a named Evidence field listing specific AT-RISK SLA rows that cite this B-ID | depth |
| C-20 | Chain Status Gate -- explicit CHAIN STATUS: CLOSED/OPEN declaration makes bidirectional verification a discrete output element | depth |
| C-21 | Unified Exception-Block Architecture -- SECTION A constructed-answer blocks per phase satisfy C-13, C-15, and C-17 through a single structural decision | format |
| C-22 | Evidence Field Format Contract -- the Evidence sub-field hint provides a concrete format example in `[State name -- S-ID]: AT-RISK, causal source: B-[ID]` form plus an explicit preamble fail condition for general references | depth |
| C-23 | Chain Status Section Isolation -- CHAIN STATUS is declared as the first element of a dedicated top-level section, not embedded in SLA ANALYSIS; anti-embedding instruction present | depth |
| C-24 | Evidence Field Format Dual Redundancy -- the concrete named domain example and fail condition appear in BOTH the global preamble AND each B-NN per-block hint | depth |
| C-25 | Anti-Embedding Dual Enforcement -- the anti-embedding instruction for CHAIN STATUS appears in BOTH the global preamble AND as the opening constraint of the dedicated CHAIN STATUS section | format |
| C-26 | Evidence Field Axis Separation -- the Evidence field instruction presents structure specification and contract specification as explicitly labeled, visually distinct components | format |
| C-27 | Evidence Field Axis Dual-Location Separation -- the `Required format:` and `Fail condition:` labeled axes appear in BOTH the global preamble AND each B-NN per-block hint | format |
| C-28 | Evidence Format Pattern B-ID Instantiation -- the `Required format:` axis in each B-NN per-block hint uses the specific B-ID for that block, not a generic `B-[ID]` placeholder | depth |
| C-29 | B-NN Scaffold Completeness Prerequisite Declaration -- the template contains an explicit instruction that ALL declared B-NN blocks carry the Evidence field before per-block dual-location criteria apply | correctness |
| C-30 | Dual-Location Requirements Consolidated Declaration -- a named block enumerates both dual-location properties (concrete example and labeled axes) at one declaration point, not scattered across individual B-NN hints | format |
| C-31 | Scaffold Gate Forward-Reference Structural Position -- the scaffold completeness gate appears before the first B-NN block in document order and uses forward-reference language ("declared below" or equivalent) making its scope positionally verifiable | format |
| C-32 | Dual-Location Consolidated Block Canonical Axis Citation -- the consolidated dual-location declaration names the `Required format:` and `Fail condition:` axes by their canonical labels, not by description or paraphrase | format |
| C-33 | Preamble Concrete Example B-ID Alignment -- the preamble concrete example (per C-24) names the same B-ID as the first declared B-NN block, aligning the preamble anchor with the per-block instantiation chain | depth |
| C-34 | Incumbent Baseline IM-ID Cross-Section Traceability -- INCUMBENT BASELINE table assigns IM-IDs to named failure modes; each B-NN Cause field cites at least one IM-ID by literal identifier, establishing the Baseline->B-NN traceability chain | depth |
| C-35 | Cost-of-No-Action Baseline Quantification -- the INCUMBENT BASELINE section declares at least one quantified metric (named measure with value or rate) before the first phase block in document order | depth |
| C-36 | Phase-Exit Gate Named Sub-Field Architecture -- each phase section contains both a PHASE ENTRY CONTRACT block and a PHASE EXIT GATE block with explicitly named structural sub-fields | format |
| C-37 | Phase Exit Gate B-ID Forward Reference -- the PHASE EXIT GATE block carries a `Blocked bottleneck:` sub-field citing the B-ID (or NONE) that can delay phase exit, creating a Phase->B-NN traceability direction verifiable by string comparison | depth |
| C-38 | Role Sequence Schedule Phase Ownership Declaration -- a named ROLE SEQUENCE SCHEDULE block declared after the Role Registry Gate and before PHASE 1 maps each R-ID to owned phases with activation triggers, handoff triggers, and parallel windows | format |
| C-39 | B-NN Cause Field Dual Citation -- each B-NN Cause field cites both an IM-ID from INCUMBENT BASELINE and a blocking R-ID from the ROLE SEQUENCE SCHEDULE, establishing the Role->B-NN traceability direction in addition to the Baseline->B-NN direction | depth |
| C-40 | Exception Block Role-Sequence Cross-Reference -- each EX block carries a named R-ID sub-field matching an entry in the ROLE SEQUENCE SCHEDULE; the registry gate validates that every declared R-ID appears in at least one EX block, creating the Role<->Exception traceability chain | depth |
| C-41 | Phase Entry Contract Prior-Phase Sequential Linkage -- each PHASE ENTRY CONTRACT block carries a named `Prior phase:` sub-field identifying the preceding phase by literal phase identifier, creating Phase->Phase sequential traceability verifiable by string comparison | format |
| C-42 | Exception Block Bottleneck Cross-Reference -- each EX block carries a named `Bottleneck Ref:` sub-field citing the B-ID (or NONE) that the exception exposes; the Bottleneck Analysis gate validates that every declared B-ID appears in at least one EX block, creating the B-NN<->Exception traceability chain | depth |
| C-43 | Phase Exit Gate Forward Phase Sequential Linkage -- each PHASE EXIT GATE block carries a named `Next phase:` sub-field identifying the subsequent phase by literal phase identifier, creating Phase->Phase forward traceability on the exit side verifiable by string comparison | format |
| C-44 | Bottleneck Block Exception-Ref Enumeration -- each B-NN block carries a named `Exception Refs:` field enumerating every EX-N block whose `Bottleneck Ref:` points to this B-ID, converting the C-42 gate check from a document-level existence assertion to a per-block navigable lookup; enumeration must be consistent with the gate check result | depth |
| C-45 | Phase Gate Three-Field Contract Declaration -- an explicit preamble or dedicated contract summary names the complete three-field phase gate system as a unit: `Prior phase:` (Phase label, backward), `Prior phase blocked bottleneck:` (B-ID, entry), and `Next phase:` (Phase label, forward); the declaration explicitly states that `Next phase:` and `Prior phase blocked bottleneck:` carry orthogonal value types independently verifiable by string comparison | format |
| C-46 | Per-Phase Incumbent IM-Reference Callout -- each PHASE ENTRY CONTRACT block carries a named `IM Reference:` sub-field listing the IM-IDs from INCUMBENT BASELINE whose failure modes are active risks entering that phase, opening the Baseline->Phase traceability direction as a per-phase navigable lookup; phases with no active IM risk carry explicit NONE sentinel; IM-IDs must match literal identifiers from the INCUMBENT BASELINE table | depth |
| C-47 | Exception Block Incumbent IM Dual-Cite Anchor -- each EX block in SECTION A carries a named `IM Ref:` sub-field citing the IM-ID from INCUMBENT BASELINE whose failure mode the exception traces, giving each EX block dual citation: `Bottleneck Ref:` (B-NN link, C-42) and `IM Ref:` (baseline link); EX blocks become the convergence point for B-NN<->Exception and Baseline<->Exception traceability chains simultaneously; CHAIN STATUS gains a `Baseline->Exception` direction; absent baseline link carries NONE sentinel | depth |
| C-48 | Incumbent Baseline Phase-Coverage Back-Reference -- each INCUMBENT BASELINE row carries a named `Phase Refs:` sub-field enumerating every PHASE ENTRY CONTRACT where this IM-ID appears in its `IM Reference:` field, closing the Baseline->Phase direction (C-46) bidirectionally at the baseline-row level as a per-row navigable lookup; IM-IDs with no active phase references carry explicit NONE sentinel; enumeration must be consistent with C-46 sub-fields; CHAIN STATUS gains a `Phase->Baseline` direction | depth |
| C-49 | Exception Block Triple-Citation Architecture Declaration -- an explicit SECTION A preamble or EXCEPTION BLOCK ARCHITECTURE header names all three EX block citation sub-fields as a declared unit: `Role Ref:` (R-ID namespace), `Bottleneck Ref:` (B-ID namespace), `IM Ref:` (IM-ID namespace); the declaration includes an explicit orthogonality assertion that the three ID namespaces are distinct and independently verifiable by string comparison; makes EX block completeness format-verifiable from the preamble without per-block traversal | format |
| C-50 | CHAIN STATUS Four-Direction Completeness Inventory -- the CHAIN STATUS section opens with an explicit DIRECTION INVENTORY block enumerating all four established traceability directions by canonical name (`B-NN->Exception`, `Phase-exit-sequence`, `Baseline->Phase`, `Baseline->Exception`), declaring each PRESENT or ABSENT, and citing the section or sub-field that carries it; converts CHAIN STATUS from an implicit multi-directional summary to an indexed direction register verifiable by string comparison; absent inventory block or missing direction entry is a fail | depth |

---

## Scoring

```
score = (essential_pass/5 x 60)
      + (recommended_pass/3 x 30)
      + (aspirational_pass/42 x 10)
```

**Golden threshold:** `score >= 9.0` (unchanged). Requires 38/42 aspirational criteria.

Essential and recommended criteria are evaluated as full-credit pass/fail per criterion.
Aspirational score is a continuous ratio: `aspirational_pass / 42 x 10`.

---

## Criterion Category Summary

| Category | Criteria | Count |
|----------|----------|-------|
| correctness | C-01, C-03, C-05, C-12, C-29 | 5 |
| coverage | C-02, C-07, C-13 | 3 |
| depth | C-04, C-06, C-09, C-10, C-14, C-16, C-19, C-20, C-22, C-23, C-24, C-28, C-33, C-34, C-35, C-37, C-39, C-40, C-42, C-44, C-46, C-47, C-48, C-50 | 24 |
| format | C-08, C-11, C-15, C-17, C-18, C-21, C-25, C-26, C-27, C-30, C-31, C-32, C-36, C-38, C-41, C-43, C-45, C-49 | 18 |

Total criteria: 50 (5 essential + 3 recommended + 42 aspirational).

---

## Dependency Chain Reference

```
C-18->C-15; C-19->C-16; C-20->C-14+C-16; C-21->C-13+C-15+C-17
C-22->C-19; C-23->C-20
C-24->C-22; C-25->C-23; C-26->C-22
C-27->C-26
C-28->C-27; C-29->C-27; C-30->C-24+C-27
C-31->C-29; C-32->C-30
C-33->C-28+C-24
C-34->C-04; C-35->C-34; C-36->C-04
C-37->C-36+C-04; C-38->C-12; C-39->C-34+C-38
C-40->C-38+C-13; C-41->C-36
C-42->C-04+C-13; C-43->C-37+C-41
C-44->C-42; C-45->C-43+C-41
C-46->C-34+C-41; C-47->C-42+C-46
C-48->C-46; C-49->C-40+C-42+C-47; C-50->C-46+C-47
```
