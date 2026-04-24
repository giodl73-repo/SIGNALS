## org-roles Round 11 Scoring — v11 Rubric (C-01 through C-49, /41)

**Baseline**: All five variations inherit R10 V-05 (100.00 under v11) as base. Primary task: verify no regressions, identify C-50 candidates.

---

### Evaluation Method

Since R10 V-05 achieved 41/41 (100.00), each R11 variation is evaluated for **regression risk** — does the new mechanism remove or degrade any element that contributed to R10 V-05's perfect score? Then evaluated for **new structural patterns** that weren't testable under v11.

---

## V-01 — SCAN ORDERING GATE (single-axis: lifecycle emphasis)

**Change from R10 V-05**: Adds a 6-item SCAN ORDERING GATE checklist after the Step 7 scan block, asserting each phase transition as a verified condition. Final checklist extended with SCAN ORDERING GATE confirmation. All other elements identical to R10 V-05.

**Regression analysis**:

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-48 | PASS | Four phases in canonical sequence under named headers (structural position — R10 V-05 basis). SCAN ORDERING GATE additionally declares the ordering as a formal gate condition; this is additive, cannot degrade C-48. |
| C-49 | PASS | Final checklist carries "Contract violations (C-29/C-33)" group header with explicit acknowledgment — same mechanism as R10 V-05. Per-file checklist retains "(CONTRACT VIOLATION type 1)" / "(CONTRACT VIOLATION type 2)" labels. No items removed. |
| C-29/C-33 | PASS | YAML template retains `# CONTRACT VIOLATION (type 1) — PHANTOM` / `(type 2) — UNIVERSALIST` annotations. Per-file checklist retains both contract violation items. |
| All other C-01 through C-47 | PASS (inherited) | No elements removed; SCAN ORDERING GATE is purely additive. |

**New mechanism**: The SCAN ORDERING GATE creates a **declared constraint** distinct from C-48's structural test. C-48 is satisfied when phases appear under independently named top-level headers in canonical sequence. The SCAN ORDERING GATE adds six per-transition assertions: "Phase 1 executed first; no checking occurred in Phase 1," "Phase 2 executed after Phase 1 was complete and before Phase 3 began," etc. A skill where phases happen to appear in order satisfies C-48; a skill that additionally asserts "Phase N executed AFTER Phase N-1 was complete" satisfies a stronger declared-ordering constraint. This is a new testable property.

**Score: 41/41 = 100.00**

---

## V-02 — Criterion-ID Propagation to All Gate Items (single-axis: output format)

**Change from R10 V-05**: Adds "Criterion check: [C-NN] ..." lines at the end of every step's rule block. Per-file checklist items carry explicit criterion-ID annotations ([C-07/FC-4], [C-46], [C-47], [C-29/C-33]). YAML template CONTRACT VIOLATION annotations carry [C-29].

**Regression analysis**:

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-49 | PASS (strengthened) | Per-file checklist items NOW carry explicit [C-NN] annotations per item — every checklist item in isolation reveals its criterion. This is the strongest possible C-49 satisfaction: individual items annotated, not just group headers. The base R10 V-05 mechanism (final checklist group headers) is retained AND strengthened. |
| C-29/C-33 | PASS (strengthened) | YAML template has `[C-29]` annotations on CONTRACT VIOLATION comments. Checklist items have [C-29/C-33] annotations. Two independent reinforcement sites. |
| C-48 | PASS | Four phases in canonical sequence. Criterion check line in Step 7 confirms: "[C-42] Phase 1 enumerate-only; [C-43] Phase 4 named revision; [C-48] canonical sequence verified." This is additive over the structural position. |
| All other C-01 through C-47 | PASS (inherited + annotated) | No elements removed; every step gains a trailing criterion check but step content is identical to R10 V-05. |

**New mechanism**: Criterion-ID annotations propagated to ALL gate items creates a **fully cross-referenced pipeline** where every checkpoint names its governing criterion. C-49 covers the per-file checklist; V-02's pattern extends self-auditing to derivation gates, scan gates, and registry gates. A skill where only the per-file checklist has criterion annotations satisfies C-49 but not this stronger property. A skill where every step-end gate includes "Criterion check: [C-NN]" lines is fully navigable without external rubric reference.

**Score: 41/41 = 100.00**

---

## V-03 — PROVENANCE-CHAIN DECLARATION (single-axis: inertia framing)

**Change from R10 V-05**: Adds PROVENANCE-CHAIN DECLARATION block in Step 6 PREPARE — three named chains (A: GAP-ANALYSIS → Diagnosis Card → YAML inertia_gap_inherited; B: Scan+Anchor → Diagnosis Card → YAML orthogonality; C: INERTIA-SURFACE → REGISTRY.md inertia_surface) each with Source, Transit, Destination, and Integrity rule. Diagnosis Card fields gain "Chain A transit" and "Chain B transit" labels. YAML template fields gain "Chain B/A destination" comment prefixes. Final checklist gains "Provenance chains declared and verified" section. Per-file checklist gains [Chain A] and [Chain B] annotations on orthogonality and inertia_gap_inherited items.

**Regression analysis**:

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-49 | PASS | V-03 does NOT add C-NN annotations to per-file checklist items (uses [Chain A]/[Chain B] instead). However, the final checklist retains the "Contract violations (C-29/C-33):" group header with explicit acknowledgment — the same mechanism that earned R10 V-05 its C-49 PASS. No C-49 regression. |
| C-29/C-33 | PASS | YAML template retains both CONTRACT VIOLATION annotations (type 1/type 2). Per-file checklist retains both items. Final checklist explicitly names C-29/C-33. |
| C-47 (YAML inertia_gap_inherited persistence) | PASS (strengthened) | PROVENANCE-CHAIN DECLARATION Chain A explicitly defines the three-artifact chain and the integrity rule ("positional reference breaks Chain A"). The YAML field comment now reads "Chain A destination — GAP-{slug}: [verbatim]" — stronger provenance tracing than R10 V-05. |
| C-46 (YAML orthogonality persistence) | PASS (strengthened) | Chain B provides explicit source→transit→destination for orthogonality. YAML field comment reads "Chain B destination — copy verbatim from Diagnosis Card." |
| C-41 (Diagnosis Card inertia-gap provenance field) | PASS (strengthened) | "Chain A transit" annotation on Diagnosis Card field makes provenance explicit. |
| All other C-01 through C-48 | PASS (inherited) | No elements removed; all additions are additive. |

**New mechanism**: The PROVENANCE-CHAIN DECLARATION creates a **named artifact contract for multi-step field inheritance** before any Diagnosis Card is written. Currently C-41/C-47 require the three-artifact chain to exist structurally, but no criterion requires declaring the chains as a formal pre-writing artifact. A skill where the chain is enforced by field format rules (R10 V-05 basis) satisfies C-41/C-47; a skill that additionally writes a named declaration block before producing any artifacts adds a new self-auditing layer — "what are the three chains, where does each field come from, what breaks them?"

**Score: 41/41 = 100.00**

---

## V-04 — Combined: SCAN ORDERING GATE + Criterion-ID Propagation (V-01 + V-02)

**Change from R10 V-05**: SCAN ORDERING GATE from V-01 plus [C-NN] annotations on SCAN ORDERING GATE items AND every step-end criterion check block plus per-file checklist item annotations from V-02.

**Regression analysis**:

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-48 | PASS (doubly reinforced) | Structural phase ordering (R10 V-05) + SCAN ORDERING GATE (V-01) + criterion-annotated SCAN ORDERING GATE items like "[C-48]" on ordering assertions (V-02). |
| C-49 | PASS (strongest in series) | Per-file checklist items each carry C-NN annotations. Step-end criterion check blocks annotate all gate items. Two independent sites for per-item criterion annotation. |
| C-29/C-33 | PASS (doubly reinforced) | YAML template has [C-29] annotations. Checklist items have [C-29/C-33] annotations. SCAN ORDERING GATE's gate items carry [C-48] etc. — demonstrating that the V-02 mechanism extends across all gate types. |
| All other C-01 through C-47 | PASS (inherited from both V-01 and V-02) | V-01 and V-02 are orthogonal mechanisms; combining them introduces no conflicts. |

**Independence test**: V-01 and V-02 address different structural properties (V-01: ordering-as-declared-constraint; V-02: criterion-ID-at-every-checkpoint). Combining them confirms they are independent: SCAN ORDERING GATE items can carry [C-NN] annotations, demonstrating that the ordering gate itself can be criterion-referenced.

**Score: 41/41 = 100.00**

---

## V-05 — All Three Axes + Formal Phase Register (V-01 + V-02 + V-03 + register change)

**Change from R10 V-05**: All three new mechanisms (SCAN ORDERING GATE, criterion-ID propagation, PROVENANCE-CHAIN DECLARATION) plus switch from imperative Step register to formal Phase 0–6 register with named GATE blocks.

**Regression analysis** (focus: does formal register re-introduce C-29/C-33/C-49 failures seen in R10 V-03/V-04?):

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-29 | PASS | YAML template: `# CONTRACT VIOLATION (type 1) — PHANTOM ... [C-29]` and `# CONTRACT VIOLATION (type 2) — UNIVERSALIST ... [C-29]`. Phase 5 GATE item 10 explicitly checks "[C-28/C-29/C-33]". Two independent PASS signals. R10 V-03/V-04 failed this with formal register because the CONTRACT VIOLATION labels weren't in the YAML template comments — V-05 carries them with [C-29] annotation. |
| C-33 | PASS | YAML template CONTRACT VIOLATION labels are mirrored at the write site. Phase 5 GATE explicitly mentions "labels mirrored in template annotation per [C-33]." |
| C-49 | PASS | Per-file checklist in Phase 5 carries full [C-NN] annotations on all seven items: `[C-07/FC-4]`, `[C-07/FC-5]`, `[C-46]`, `[C-47]`, `[C-37]`, `[C-29/C-33]` (twice). Every checklist item in isolation reveals its criterion. |
| C-48 | PASS | Four phases in canonical sequence under named headers (Phase 1/2/3/4). SCAN ORDERING GATE present inside Phase 5 with six criterion-annotated items. Phase 5 GATE item 4 explicitly checks "SCAN ORDERING GATE confirmed with all six items checked; Phase 4 complete before YAML writing began [C-42/C-43/C-48]." Triple reinforcement. |
| C-30 | PASS | EXTENSION-COMMITMENT purpose says: "answers the Phase 0 diagnostic question — 'what is the strongest existing-system argument that makes {topic} premature?'" — explicitly names the diagnostic question. |
| C-26 | PASS (strongest) | Full FIELD-CONTRACT with [FC-1] through [FC-12] entries, each individually labeled. [FC-10] carries both CONTRACT VIOLATION labels. [FC-11]/[FC-12] carry REQUIRED/REQUIRED FORMAT with explicit YAML persistence statements. Phase 0 GATE checks all twelve FC entries. |
| C-23 | PASS | EXTENSION-COMMITMENT in Phase 0 (before any context reading) with all three elements: field_name, population_source, purpose. |
| C-47 | PASS (strongest in series) | PROVENANCE-CHAIN DECLARATION Chain A: "Destination: Phase 5 YAML role file — field: inertia_gap_inherited [FC-12]." [FC-12] in FIELD-CONTRACT requires the field. Phase 5 GATE item 8 checks "[FC-12] citing GAP-{slug} — not positional [C-47]." Three independent enforcement points. |
| C-46 | PASS (strongest in series) | PROVENANCE-CHAIN DECLARATION Chain B. [FC-11] in FIELD-CONTRACT requires the field with REQUIRED FORMAT. Phase 5 GATE item 7. Three independent enforcement points. |
| C-31 | PASS | BANNED names appear in: [FC-1] PROHIBITED NAMES clause (contract block — location 1), Phase 2 GATE item 5 "No placeholder names per [FC-1]" (gate condition — location 2), Phase 5 GATE item 10 "[C-28/C-29/C-33]" (write step gate — location 3). Three independent locations. |
| All other C-01 through C-47 | PASS (inherited + gate-checked) | Phase register gates explicitly enumerate C-NN identifiers at each checkpoint; no element from R10 V-05 is absent. |

**Structural test result**: The formal register + PROVENANCE-CHAIN DECLARATION in Phase 0 + SCAN ORDERING GATE with [C-NN] annotations + per-file checklist annotations collectively protect C-29/C-33/C-49 through three independent enforcement sites each — more robust than R10 V-05 (which relied on one final-checklist site). The formal register hypothesis is **confirmed**: formal Phase register CAN hold 100.00 when C-29/C-33 annotations are embedded in both the YAML template and the per-file checklist.

**Score: 41/41 = 100.00**

---

## Composite Scores and Ranking

Using formula: (essential_pass/essential_total) × 60 + (correctness_pass/correctness_total) × 30 + (differentiating_pass/41) × 10

All variations inherit all essential criteria from R10 V-05. No regressions found in any variation. All variations achieve 41/41 differentiating criteria.

| Rank | Variation | Score | v11 Status |
|------|-----------|-------|-----------|
| 1 (tied) | V-05 | **100.00** | GOLDEN — all three new mechanisms + formal register |
| 1 (tied) | V-04 | **100.00** | GOLDEN — V-01+V-02 independent mechanisms confirmed |
| 1 (tied) | V-01 | **100.00** | GOLDEN — SCAN ORDERING GATE as declared ordering constraint |
| 1 (tied) | V-02 | **100.00** | GOLDEN — criterion-ID propagation across full pipeline |
| 1 (tied) | V-03 | **100.00** | GOLDEN — PROVENANCE-CHAIN DECLARATION as pre-writing artifact |

**Cross-round ceiling under v11**: R10 V-05 and all five R11 variates at 100.00. Ceiling remains closed. Frontier has not advanced — it was closed by R10 V-05 and R11 confirms it holds under five independent perturbations.

---

## Excellence Signals

**Signal 1 — V-01/V-04/V-05: Ordering-as-declared-constraint**

The SCAN ORDERING GATE transforms C-48's structural test (phases appear in canonical order) into a declared and verified constraint (each phase transition individually asserted). The six gate items — "Phase 1 executed first; no checking occurred," "Phase 2 executed after Phase 1 was complete and before Phase 3 began," etc. — create a per-transition ordering proof that cannot be satisfied by arranging phases under correct headers without running the gate. C-48 PASS does not require this gate; C-48 PASS does not distinguish a skill that declares it from one that merely arranges it. The gate is a new testable structural property.

**Signal 2 — V-02/V-04/V-05: Criterion-ID gate propagation across full pipeline**

C-49 covers the per-file write checklist. V-02 extends criterion-ID annotation to every step-end gate block. "Criterion check: [C-42] Phase 1 enumerate-only; [C-43] Phase 4 named revision; [C-48] canonical sequence..." at Step 7's end; "[C-45] POSITIVE SOURCING field inline per expert record..." at Step 4's end; "[C-10] all five fields present..." at Step 9's end. A skill satisfying C-49 has a self-auditing per-file checklist; a skill with full criterion-ID gate propagation has a self-auditing entire pipeline. The property is distinct, observable, and independently falsifiable (Step 4 criterion check could exist without Step 9 criterion check).

**Signal 3 — V-03/V-05: PROVENANCE-CHAIN DECLARATION as pre-writing artifact**

The three artifact chains (inertia gap: GAP-ANALYSIS → Diagnosis Card → YAML field; orthogonality: scan+anchor → Diagnosis Card → YAML field; status-quo claim: INERTIA-SURFACE → REGISTRY.md) exist structurally in R10 V-05. V-03 adds a named declaration block written BEFORE any Diagnosis Card, specifying Source, Transit, Destination, and Integrity rule for each chain. C-41/C-47 test that the chains are populated correctly; they do not test whether the chains were declared as a formal pre-writing artifact. The declaration enables a new verification pattern: "Chain A integrity rule: copy verbatim at each transit; positional reference at destination breaks Chain A." This is a provenance contract, not a structural enforcement — a new property class.

**V-05 synthesis observation**: V-05 demonstrates that all three new mechanisms are compatible with the formal Phase register AND with each other. Specifically: (a) PROVENANCE-CHAIN DECLARATION in Phase 0 precedes all context reading; (b) SCAN ORDERING GATE is embedded inside the Phase 5 scan procedure with criterion annotations; (c) per-file checklist criterion annotations protect C-29/C-33/C-49 that the formal register historically broke. V-05 answers the falsifiability question from the round: the formal register does NOT re-introduce C-29/C-33 regression when CONTRACT VIOLATION labels are in the YAML template AND in the per-file checklist (two sites vs R10 V-03/V-04's zero YAML-template sites).

---

## v12 Criterion Candidates (C-50+)

| ID | Source | Pattern |
|----|--------|---------|
| **C-50** | V-01/V-04/V-05 | The four-phase scan includes a SCAN ORDERING GATE with per-phase-transition assertions ("Phase N executed after Phase N-1 was complete and before Phase N+1 began") — canonical ordering declared and verified, not inferred from structural position |
| **C-51** | V-02/V-04/V-05 | Every step-end gate block (not only the per-file write checklist) includes a criterion check line annotating the C-NN identifiers it enforces — full-pipeline criterion cross-referencing |
| **C-52** | V-03/V-05 | A PROVENANCE-CHAIN DECLARATION block written before any Diagnosis Card names all artifact inheritance chains with Source, Transit, Destination, and Integrity rule — making chain contracts explicit rather than structurally inferred |

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["canonical scan ordering declared as explicit per-phase-transition gate condition (not inferred from structural header position) — SCAN ORDERING GATE with six per-transition assertions", "criterion-ID annotations propagated to every step-end gate block across the full pipeline, not only the per-file write checklist — fully cross-referenced pipeline", "PROVENANCE-CHAIN DECLARATION block written before any Diagnosis Card, naming all three artifact inheritance chains with Source, Transit, Destination, and Integrity rule — provenance contract as pre-writing artifact"]}
```
