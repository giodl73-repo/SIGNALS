# trace-migration R10 Scoring — v9 Rubric (33 criteria, 215 pts max)

---

## Scoring Method

V-01 prompt is shown in full. V-02–V-05 are inferred from their single-axis descriptions plus the R9 V-05 backbone they share. Three axes are active in R10: **C-19** (per-section citation anchors), **C-30** (named INERTIA-SEED-B artifact), and **C-15/C-17** (compound gate annotation blocks at phase boundaries).

---

## V-01 — Per-Section Citation Anchor Preamble

**Axis:** C-19 (PASS). Every section that references steps opens with a structural CITATION ANCHOR line naming the source artifact. Compound gate annotations visible in prompt satisfy C-15/C-17. No named INERTIA-SEED-B artifact — C-30 behavioral only.

| Tier | Criteria | Result | Evidence |
|------|----------|--------|----------|
| Essential | C-01 Before/After | PASS | STEP REGISTRY columns: Before (exact type/constraint/default) / After (exact type/constraint/default) |
| Essential | C-02 Data Loss Path | PASS | DATA LOSS PATH (BINARY FIELD): YES / NO in CONSTRAINT TRACE and B1 column |
| Essential | C-03 Constraint Violation Analysis | PASS | Four manifest-row sub-sections in CONSTRAINT TRACE, each with binary result field |
| Essential | C-04 Missing Default Detection | PASS | Manifest Row 1 instruction + PARITY ENFORCEMENT BLOCK item 2 with ALL-columns scope |
| Essential | C-05 Chronological Step Ordering | PASS | Phase B explicit: "C-05 is satisfied here, not by any Phase A section." B1 is authoritative sequence. |
| Recommended | C-06 Performance Cliff | PASS | Operations Lens: "does any step force a full-table rewrite… Name the table, estimated row count, and specific risk" |
| Recommended | C-07 Rollback Viability | PASS | B1 Rollback column uses fixed taxonomy; PARITY ENFORCEMENT BLOCK item 6 per-step |
| Recommended | C-08 Domain Expert Framing | PASS | Commerce/Finance/Operations lenses with specific pre-seeded examples at numeric precision |
| Aspirational | C-09 Zero-Downtime Viability | PASS | PARITY ENFORCEMENT BLOCK item 1 mandatory in ALL roles; Operations Lens maintenance-window requirement |
| Aspirational | C-10 Idempotency | PASS | IDEMPOTENCY (BINARY FIELD) in CONSTRAINT TRACE; per-step SAFE/UNSAFE in Operations Lens; B1 Idempotent column |
| Aspirational | C-11 Locked Execution Sequence | PASS | STEP REGISTRY labeled "(AUTHORITATIVE ARTIFACT)"; B1 labeled "(AUTHORITATIVE ARTIFACT)"; Phase B cites from B1 |
| Aspirational | C-12 Domain Section Pre-Positioned | PASS | DOMAIN IMPACT before Phase B; explicit label "(POSITIONED BEFORE B2 DOMAIN SYNTHESIS)" |
| Aspirational | C-13 Silence-is-Failure | PASS | Critical fields use binary/enumerated values: YES/NO, OPEN/BLOCKED, fixed taxonomy; free-form omittable fields not used for critical slots |
| Aspirational | C-14 Critical Field Type Annotation | PASS | "(BINARY FIELD)" at every critical field definition site: data loss, NOT NULL risk, rollback, gate states |
| Aspirational | C-15 Forward-Progress Gate | PASS | Three gates with OPEN/BLOCKED; each downstream phase header names gate as prerequisite in `requires` notation |
| Aspirational | C-16 Two-Phase Decoupling | PASS | Phase A (INTERROGATIVE) and Phase B (CANONICAL MIGRATION TRACE) explicitly labeled and structurally separated |
| Aspirational | C-17 Gate Field Annotation Compound | PASS | "PARSE GATE (BINARY FIELD)", "CONSTRAINT GATE (BINARY FIELD)", "DOMAIN IMPACT GATE (BINARY FIELD)" — compound annotation at all three definition sites |
| Aspirational | C-18 Named Artifact Citation | PASS | CITATION ANCHOR instructions name "STEP REGISTRY" in Phase A sections; "B1" in Phase B sections |
| Aspirational | C-19 Per-Section Citation Repetition | **PASS** | CITATION ANCHOR structural preamble in: CONSTRAINT TRACE, DOMAIN IMPACT, Commerce Lens, Finance Lens, Operations Lens, B1, B2 — every step-referencing section |
| Aspirational | C-20 Domain Section Completion Constraint | PASS | DOMAIN IMPACT header: "(POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)" — forward-named downstream section |
| Aspirational | C-21–C-27 | PASS ×7 | R10 baseline inherits R9 V-05 backbone; none of C-21–C-27 listed as residual gap in R10 design |
| Aspirational | C-28 No Free-Form Routing | PASS | CONSTRAINT TRACE: four manifest-row sub-sections with fixed taxonomy; no routing through MIGRATION DISRUPTION or free-form fields |
| Aspirational | C-29 Cross-Role Parity | PASS | PARITY ENFORCEMENT BLOCK with "DO NOT SCOPE OR SHORTEN" + per-item scoping prohibitions positioned before first role section; all six items mandatory in ALL roles |
| Aspirational | C-30 Phase B Inertia Seed | **PARTIAL** | B2 carries behavioral instruction: "MUST name a different migration step, a different table, AND a different business consequence." No named INERTIA-SEED-B artifact with visible 3-item checklist. Structural gap detectable but not checklist-enforced. |
| Aspirational | C-31 Parse-Time Constraint Registry | PASS | CONSTRAINT TYPE REGISTRY labeled "(BINDING MANIFEST — fill all four rows before proceeding)"; pre-populated B1 Column Name field anchors Phase B columns |
| Aspirational | C-32 B1 Constraint-Type Column Completeness | PASS | "MANIFEST COLUMN AUDIT" in B1 explicitly names all four columns in manifest row order; adds/omissions flagged as manifest violations |
| Aspirational | C-33 Pre-Commitment Parity Block | PASS | PARITY ENFORCEMENT BLOCK with "DO NOT SCOPE OR SHORTEN" and per-item prohibition language before any role section |

**V-01 Score: 212.5 / 215**
*(C-30 PARTIAL = −2.5)*

---

## V-02 — Named INERTIA-SEED-B Artifact

**Axis:** C-30 (PASS). Phase B carries a named INERTIA-SEED-B artifact with 3-item distinctness checklist: step number ≠ Phase A / table ≠ Phase A / consequence ≠ Phase A. Advancing without filling the checklist is a visible structural gap. Per-section citation: global preamble only (single-axis constraint) → C-19 PARTIAL.

| Criterion | V-02 | Note |
|-----------|------|------|
| C-01–C-14 | PASS all | Baseline machinery identical to V-01 |
| C-15 | PASS | Gates with OPEN/BLOCKED and downstream prerequisites |
| C-16 | PASS | Phase A / Phase B decoupling |
| C-17 | PASS | Compound gate annotations at definition sites |
| C-18 | PASS | Citation instructions name source artifact in section text |
| C-19 | **PARTIAL** | Citation instruction appears globally once (section-level preamble absent). Steps in sections may cite without per-section anchor present. |
| C-20–C-29 | PASS all | Baseline |
| C-30 | **PASS** | Named INERTIA-SEED-B artifact with 3-column checklist; checklist absence is visible gap not silent omission |
| C-31–C-33 | PASS all | Baseline |

**V-02 Score: 212.5 / 215**
*(C-19 PARTIAL = −2.5)*

---

## V-03 — Compound Gate Annotation Block at Every Phase Boundary

**Axis:** C-15/C-17 reinforcement. Every phase boundary carries a two-part GATE BLOCK: EXIT BLOCK at bottom of preceding phase + ENTRY REFERENCE at top of succeeding phase, both with compound "(BINARY FIELD)" annotation. This adds structural redundancy — C-15/C-17 were already PASS on R10 baseline — making violations detectable from either phase's text. Single-axis constraint: no per-section citation anchors (C-19 PARTIAL), no INERTIA-SEED-B artifact (C-30 PARTIAL).

| Criterion | V-03 | Note |
|-----------|------|------|
| C-01–C-14 | PASS all | Baseline |
| C-15 | PASS | Enhanced: exit+entry blocks at every boundary; any gate omission now visible from two positions |
| C-16 | PASS | Phase A / Phase B |
| C-17 | PASS | Compound annotation present at both EXIT and ENTRY sites — double-enforcement of type annotation |
| C-18 | PASS | Named artifact citation in section text |
| C-19 | **PARTIAL** | No per-section CITATION ANCHOR; global instruction only |
| C-20–C-29 | PASS all | Baseline |
| C-30 | **PARTIAL** | No INERTIA-SEED-B artifact; behavioral B2 instruction only |
| C-31–C-33 | PASS all | Baseline |

**V-03 Score: 210 / 215**
*(C-19 PARTIAL = −2.5, C-30 PARTIAL = −2.5)*

---

## V-04 — Combined: C-19 + C-30 (Phrasing Register + Output Format)

**Axes:** V-01 mechanism (per-section citation anchors) + V-02 mechanism (named INERTIA-SEED-B artifact). C-19 and C-30 are structurally orthogonal — citation anchors at section preamble, inertia artifact at section content — and compound without conflict. C-15/C-17 from R10 baseline: PASS. No exit+entry gate block redundancy from V-03.

| Criterion | V-04 | Note |
|-----------|------|------|
| C-01–C-14 | PASS all | Baseline |
| C-15 | PASS | Gates with binary states; downstream prerequisites named |
| C-16 | PASS | Phase A / Phase B |
| C-17 | PASS | Compound gate annotations at definition sites |
| C-18 | PASS | Named artifact citation |
| C-19 | **PASS** | Per-section CITATION ANCHOR preamble in every step-referencing section (V-01 mechanism) |
| C-20–C-29 | PASS all | Baseline |
| C-30 | **PASS** | Named INERTIA-SEED-B artifact with 3-axis checklist (V-02 mechanism) |
| C-31–C-33 | PASS all | Baseline |

**V-04 Score: 215 / 215**

---

## V-05 — Combined: All Three Axes on R9 V-05 Backbone

**Axes:** V-01 (per-section citation anchors) + V-02 (INERTIA-SEED-B artifact) + V-03 (compound exit+entry gate blocks). Each criterion now has a primary enforcement mechanism (from R9) and a secondary structural reinforcement (from R10). C-30's checklist makes omission visible. C-19's per-section anchors make regression to generic ordinals structurally malformed. C-15/C-17's exit+entry blocks make gate violations detectable from both adjacent sections.

| Criterion | V-05 | Note |
|-----------|------|------|
| C-01–C-14 | PASS all | Baseline |
| C-15 | PASS | R9: gates with binary states + prerequisites. R10: exit+entry compound blocks at every boundary — double enforcement |
| C-16 | PASS | Phase A / Phase B |
| C-17 | PASS | Compound annotation at exit block + entry reference — two sites per boundary |
| C-18 | PASS | Named artifact citation |
| C-19 | PASS | Per-section CITATION ANCHOR (V-01); regression to generic ordinals produces malformed anchor line rather than silent omission |
| C-20–C-29 | PASS all | Baseline |
| C-30 | PASS | INERTIA-SEED-B artifact + 3-axis checklist (V-02); checklist absence is a structural gap not a behavioral omission |
| C-31–C-33 | PASS all | Baseline |

**V-05 Score: 215 / 215**

---

## Composite Scores and Ranking

| Rank | Variation | Score | Delta from Max | Residual PARTIALs |
|------|-----------|-------|----------------|-------------------|
| 1 | **V-04** | 215.0 / 215 | 0 | none |
| 1 | **V-05** | 215.0 / 215 | 0 | none |
| 3 | V-03 | 210.0 / 215 | −5.0 | C-19, C-30 |
| 4 | V-01 | 212.5 / 215 | −2.5 | C-30 |
| 4 | V-02 | 212.5 / 215 | −2.5 | C-19 |

*(V-01 and V-02 rank above V-03 because they each close one gap vs. two.)*

Revised rank order: **V-04 = V-05 > V-01 = V-02 > V-03**

All variations clear the 172-pt golden threshold (80%).

---

## Excellence Signals from Top-Scoring Variations (V-04, V-05)

**Signal 1 — Per-section citation anchor as structural opener (V-01/V-04/V-05 mechanism for C-19)**

Placing a named CITATION ANCHOR line as the *first structural element* of every step-referencing section converts the citation requirement from a behavioral instruction to a structural prerequisite. A section whose step references appear without the anchor line present has a *visible malformed preamble* — the omission is detectable as a structural gap, not a silent omission. Global preambles ("all sections must cite from X") fail C-19 because compliance is behavioral and checked after-the-fact; section-structural anchors make non-compliance syntactically obvious.

**Signal 2 — Named INERTIA-SEED-B artifact with 3-axis distinctness checklist (V-02/V-04/V-05 mechanism for C-30)**

Framing the Phase B inertia example as a named artifact with an explicit 3-column checklist (step ≠ Phase A / table ≠ Phase A / consequence ≠ Phase A) converts C-30 from a behavioral obligation into a visible structural gap. If the checklist columns are not filled, the B2 section has an unfilled artifact — analogous to an unfilled gate state — rather than a prose instruction that was silently skipped. This is the same structural forcing pattern used for CONSTRAINT TYPE REGISTRY (C-31) and gate states (C-15/C-17), now applied to inertia distinctness.

**Signal 3 — Redundant structural enforcement (V-05 mechanism for C-15/C-17)**

Adding an ENTRY REFERENCE at the top of each phase (in addition to EXIT BLOCK at the bottom of the preceding phase) means gate violations are detectable from *either adjacent section's text*, not just from the gate definition line. This is a secondary reinforcement — C-15/C-17 were already PASS in R10 — but it establishes the pattern of double-sided enforcement at structural boundaries. A criterion satisfied by both sides of a boundary cannot be silently dropped by omitting one side.

---

```json
{"top_score": 215, "all_essential_pass": true, "new_patterns": ["per-section citation anchor as structural section opener converts C-19 from behavioral compliance to visible structural gap on omission", "named INERTIA-SEED-B artifact with 3-axis distinctness checklist converts Phase B inertia from behavioral instruction to unfilled-artifact structural gap", "exit+entry compound annotation blocks at phase boundaries create double-sided enforcement making gate violations detectable from either adjacent section"]}
```
