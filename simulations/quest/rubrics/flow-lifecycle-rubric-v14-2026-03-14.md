`flow-lifecycle-rubric-v14-2026-03-14.md` written. Here is the complete updated rubric:

---

## What changed v13 → v14

Two new aspirational criteria extracted from R13 excellence signals. Formula `/35` → `/37`.

---

## C-44 — Bottleneck Block Exception-Ref Enumeration (`depth`, C-44→C-42)

C-42 established a preamble gate check — document-level existence assertion that every B-ID appears in at least one EX block. C-44 escalates to block level: each B-NN block carries a named `Exception Refs: EX-N, EX-M, ...` field enumerating every EX block whose `Bottleneck Ref:` points to this bottleneck. Converts gate-level navigation into per-block navigable lookup. Enumeration must be consistent with the gate check result (string-comparable, no inference). Sourced from V-02 (per-block refs) and V-05 (refs + consistency check).

## C-45 — Phase Gate Three-Field Contract Declaration (`format`, C-45→C-43+C-41)

C-41 + C-37 + C-43 together define a three-field phase gate contract, but their relationship is implicit. C-45 requires an explicit preamble or CONTRACT SUMMARY block naming all three fields as a unit: `Prior phase:` (Phase label, backward), `Prior phase blocked bottleneck:` (B-ID, entry), `Next phase:` (Phase label, forward) — and explicitly declaring that the last two carry orthogonal value types independently verifiable by string comparison. C-45 is to the phase gate system what C-21 is to the exception-block architecture: a single naming decision that binds multiple criteria into a declared unit. Sourced from V-04 (explicit preamble) and V-05 (three-field named as unit).

---

## R13 retrospective scoring under v14

| Variation | C-44 | C-45 | Aspirational | Score |
|-----------|:----:|:----:|:------------:|-------|
| V-01 | FAIL | FAIL | 34/37 | 9.189 |
| V-02 | **PASS** | FAIL | 35/37 | 9.459 |
| V-03 | FAIL | FAIL | 34/37 | 9.189 |
| V-04 | FAIL | **PASS** | 36/37 | 9.730 |
| V-05 | **PASS** | **PASS** | 37/37 | **10.000** |

V-05 achieves perfect aspirational coverage. V-04 and V-03 cross golden threshold at ≥9.0. The four-step progression (gate only → per-block refs → orthogonality declared → three-field named) is now fully captured as four discrete criteria (C-42, C-44, C-43, C-45).
 and binds multiple criteria into a declared unit.

**Updated dependency chain:**
```
C-40->C-38+C-13; C-41->C-36
C-42->C-04+C-13; C-43->C-37+C-41
C-44->C-42; C-45->C-43+C-41
```

**Scoring formula:** `aspirational_pass / 37 * 10` -- golden threshold unchanged.

---

**C-42 design rationale (carried from v13).**
Symmetric to C-40. C-40 closed Role<->Exception; C-42 closes B-NN<->Exception. Each EX block carries a `Bottleneck Ref: B-ID` sub-field (or NONE). The Bottleneck Analysis section gains a gate check that every declared B-ID appears in at least one EX block, closing the chain bidirectionally. Dark bottlenecks -- declared but with no exception-phase trace -- become named gate violations. CHAIN STATUS gains a `B-NN->Exception` direction. String comparison only, no reader inference.

**C-43 design rationale (carried from v13).**
Symmetric to C-41 on the exit side. C-41 put `Prior phase:` in entry contracts (backward). C-43 puts `Next phase:` in exit gates (forward). Last phase carries NONE/END sentinel. Together C-41+C-43 complete bidirectional Phase->Phase gate-to-gate linkage -- out-of-order rendering detectable in both directions by identifier mismatch. The `Next phase:` sub-field is orthogonal to `Blocked bottleneck:` (C-37): one is a Phase label, one is a B-ID. CHAIN STATUS gains a `Phase-exit-sequence` direction.

**Full dependency chain (v14):**
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
- **C-44->C-42; C-45->C-43+C-41**

**Formula:** `aspirational_pass / 37 * 10` -- golden threshold unchanged.

---

# flow-lifecycle -- Rubric v14

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

**37 Aspirational (10 pts)**

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

---

## Scoring

```
score = (essential_pass/5 x 60)
      + (recommended_pass/3 x 30)
      + (aspirational_pass/37 x 10)
```

**Golden threshold:** `score >= 9.0` (unchanged).

Essential and recommended criteria are evaluated as full-credit pass/fail per criterion.
Aspirational score is a continuous ratio: `aspirational_pass / 37 x 10`.

---

## Criterion Category Summary

| Category | Criteria | Count |
|----------|----------|-------|
| correctness | C-01, C-03, C-05, C-12, C-29 | 5 |
| coverage | C-02, C-07, C-13 | 3 |
| depth | C-04, C-06, C-09, C-10, C-14, C-16, C-19, C-20, C-22, C-23, C-24, C-28, C-33, C-34, C-35, C-37, C-39, C-40, C-42, C-44 | 20 |
| format | C-08, C-11, C-15, C-17, C-18, C-21, C-25, C-26, C-27, C-30, C-31, C-32, C-36, C-38, C-41, C-43, C-45 | 17 |

Total criteria: 45 (5 essential + 3 recommended + 37 aspirational).

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
```
