# prove-synthesize — Round 13 Scoring (v13 rubric)

## Scoring Approach

R13 tests whether V-04 and V-05 can earn C-44 and C-45 simultaneously via a 3-column per-signal annotation (phase + role + inertia). The other three variations are single-axis controls. All five build on the R12 V-01 confirmed stack (~122.5 under v13 baseline).

---

## Per-Variation Criterion Evaluation

### V-01 — Single-axis: Lifecycle emphasis (per-signal role taxonomy → C-44)

**Architecture base**: R12 V-01 stack (C-35/C-36/C-37/C-38/C-39/C-40/C-41/C-42/C-43 all PASS, confirmed carried forward).

| Criterion | Result | Evidence note |
|-----------|--------|--------------|
| Essential C-01…C-30 cluster | **PASS** | Same architecture as R12 V-01; register and annotation axis change does not touch essential criteria |
| C-35 Concurrent execution / seamless output | **PASS** | "Three cognitive roles execute concurrently in your reasoning" + no labeled role sections in output |
| C-36 Dual-exemplar adversarial gate | **PASS** | ADVERSARY gate entry contains "Negative:" and "Positive:" exemplars co-located; same pattern as R12 V-01 |
| C-37 Slot-indexed self-containment check | **PASS** | Six questions each mapped to named paragraph: "→ Verdict/Confidence paragraph", etc. Question 6 maps Primary counts by phase to Verdict/Confidence paragraph |
| C-38 Role-to-output closure attribution | **PASS** | Open Questions: "the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST)" — attribution required |
| C-39 Phase-gated confidence ceiling | **PASS** | Phase table (Explore/Test/Validate → 25/50/72/none) as pre-synthesis constraint; positioned before reasoning |
| C-40 Concurrent synthesis gate block | **PASS** | Named "Gate Block" section with all three roles indexed; positioned after role definitions, before output instructions |
| C-41 Slot-indexed revision mandate | **PASS** | "If any question cannot be answered from the named paragraph, revise that paragraph before outputting" |
| C-42 Ceiling declaration as mandatory intermediate output | **PASS** | "State before proceeding: 'Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Confidence ceiling: …'" — mandatory before reasoning begins; names phase, Primary counts, and ceiling |
| C-43 Gate block per-role dual exemplars | **PASS** | SYNTHESIST, ADVERSARY, ANALYST gate entries each contain both negative and positive exemplars co-located within the entry |
| C-44 Per-signal annotated inventory with role classification | **PASS** | Phase 1 annotates each signal individually with evidence phase AND role (Primary/Supporting/Contextual). Annotation pass is positioned as "mandatory enumerable output" — not a coverage summary. C-42 declaration extended to include "Primary signals by phase: [count per phase]". C-39/C-42 prerequisites satisfied |
| C-45 Two-dimensional ceiling table (phase × orthogonal) | **FAIL** | Ceiling table is 1D: Explore/Test/Validate → 25/50/72/none. No orthogonal inertia dimension. Role taxonomy (Primary/Supporting/Contextual) is the annotation's second column but produces no distinct ceiling values at fixed phase level — ceiling still varies by phase only |

**Essential PASS**: Yes. **Composite: ~122.5 (base) + 2.5 (C-44) = ~125.0**. Golden ✓

---

### V-02 — Single-axis: Inertia framing (2D ceiling table → C-45)

**Architecture base**: R12 V-01 stack preserved.

| Criterion | Result | Evidence note |
|-----------|--------|--------------|
| Essential C-01…C-30 cluster | **PASS** | Same architecture; inertia framing axis does not touch essential criteria |
| C-35 | **PASS** | Concurrent execution + seamless output stated |
| C-36 | **PASS** | SYNTHESIST, ADVERSARY, ANALYST gate entries each have negative + positive exemplars co-located |
| C-37 | **PASS** | Six slot-indexed questions including Q6: "Is the phase + inertia declaration traceable to the confidence score? → Verdict/Confidence paragraph" |
| C-38 | **PASS** | Open Questions: "Attribute each to the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST)" |
| C-39 | **PASS** | 2D phase × inertia table with ceilings defined; pre-synthesis constraint present |
| C-40 | **PASS** | Named Gate Block with all three roles indexed and exemplars present |
| C-41 | **PASS** | Slot-indexed revision mandate: "If any question cannot be answered from the named paragraph, revise that paragraph before outputting" |
| C-42 | **PASS** | "State before proceeding: 'Evidence phase coverage: [phases present]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']'" — mandatory intermediate output naming phase, inertia state, and ceiling |
| C-43 | **PASS** | All three role entries in gate block carry both failure and passing exemplars co-located |
| C-44 Per-signal annotated inventory with role classification | **FAIL** | Pre-synthesis step classifies signals by phase and inertia coverage but does NOT introduce Primary/Supporting/Contextual role taxonomy. No per-signal role annotation pass. Declaration names inertia state, not Primary counts by phase. Role classification dimension is absent |
| C-45 Two-dimensional ceiling table (phase × orthogonal) | **PASS** | Ceiling table uses two orthogonal dimensions: evidence phase (rows) and inertia coverage (columns: absent/present). Test phase: inertia-absent = 45, inertia-present = 60 — distinct ceilings at fixed phase level confirm independent influence. C-42 declaration extended to name inertia coverage state. C-39 prerequisite satisfied |

**Essential PASS**: Yes. **Composite: ~122.5 (base) + 2.5 (C-45) = ~125.0**. Golden ✓

---

### V-03 — Single-axis: Phrasing register (formal academic)

**Architecture base**: R12 V-01 structure, formal academic register throughout. No new annotation or ceiling dimensions introduced.

| Criterion | Result | Evidence note |
|-----------|--------|--------------|
| Essential C-01…C-30 cluster | **PASS** | Structural criteria are register-independent; formal register ("shall", numbered steps, passive voice) does not change architectural compliance |
| C-35 | **PASS** | "three cognitive roles execute concurrently in your reasoning … output document shall contain no role section headers and no visible demarcations" |
| C-36 | **PASS** | Each role's gate block entry contains "Negative exemplar" and "Positive exemplar" co-located |
| C-37 | **PASS** | Six verification questions each mapped to named section: "→ Verdict/Confidence", "→ Key Evidence", etc. |
| C-38 | **PASS** | Open Questions section: "the cognitive role that raised it (SYNTHESIST, ADVERSARY, or ANALYST) shall be attributed" |
| C-39 | **PASS** | Phase classification table + ceiling determination in Step 2 as pre-synthesis constraint; all three phases with ceiling values defined |
| C-40 | **PASS** | "Gate Procedure: Pre-Output Verification" — unified block, all three roles indexed, positioned after role definitions and before output specification |
| C-41 | **PASS** | "If any question cannot be answered from its named section, that section shall be revised before the output is submitted" |
| C-42 | **PASS** | "The following statement shall be produced before synthesis reasoning commences: 'Evidence phase coverage: [phases present]. Confidence ceiling: [numeric value, or 'none — all phases present']'" — mandatory intermediate output |
| C-43 | **PASS** | Each role gate entry contains "Negative exemplar" and "Positive exemplar" co-located within the role's entry; all three roles present |
| C-44 Per-signal annotated inventory with role classification | **FAIL** | Step 1 assigns phase labels per signal (per-signal annotation pass present) but no role classification (Primary/Supporting/Contextual) introduced. C-42 declaration names phase and ceiling only — no "Primary signals by phase" extension. Phase-only annotation without role taxonomy does not satisfy C-44 |
| C-45 Two-dimensional ceiling table (phase × orthogonal) | **FAIL** | Ceiling table is 1D: Explore/Test/Validate → 25/50/72/none. No orthogonal second dimension. Register change does not introduce any new ceiling axis |

**Essential PASS**: Yes. **Composite: ~122.5**. Golden ✓ (confirms register-independence of the criteria battery)

---

### V-04 — Combined: 3-column annotation (phase + role + inertia → C-44 + C-45)

**Architecture base**: R12 V-01 stack fully preserved with 3-column Phase 1 added.

| Criterion | Result | Evidence note |
|-----------|--------|--------------|
| Essential C-01…C-30 cluster | **PASS** | Same architecture as R12 V-01; 3-column annotation is an additive pre-synthesis step, not a structural change |
| C-35 | **PASS** | "Three cognitive roles execute concurrently in your reasoning … output is a single document — no role section headers, no visible role seams" |
| C-36 | **PASS** | Gate block entries: SYNTHESIST, ADVERSARY, ANALYST each contain "Negative:" and "Positive:" exemplars co-located |
| C-37 | **PASS** | Self-containment check maps 6 questions to named paragraphs; Q6 explicitly maps Phase 1 declaration (phase + Primary counts + inertia state) to Verdict/Confidence paragraph |
| C-38 | **PASS** | Open Questions section: "the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST)" required for each question |
| C-39 | **PASS** | 2D ceiling table as pre-synthesis constraint; positioned in Phase 1 before synthesis reasoning in Phase 2 |
| C-40 | **PASS** | Named "Gate Block" section with SYNTHESIST/ADVERSARY/ANALYST indexed; positioned after role definitions (Phase 2 cognitive framework) and before Output Instructions |
| C-41 | **PASS** | "If any question cannot be answered from the named paragraph, revise that paragraph before outputting" |
| C-42 | **PASS** | "State before proceeding: 'Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [numeric value, or 'none']'" — mandatory intermediate output naming all three classification dimensions |
| C-43 | **PASS** | All three roles in gate block carry both negative and positive exemplars co-located within each role's entry |
| C-44 Per-signal annotated inventory with role classification | **PASS** | Phase 1 annotates every signal with three columns: phase + role (Primary/Supporting/Contextual) + inertia. Role annotation is the second column of an enumerable mandatory per-signal table. C-42 declaration extended to "Primary signals by phase: [count per phase]" — ceiling derivable by inspection. "The ceiling computation in the next step is derived from the per-signal annotation inventory, not inferred from a gestalt impression." C-39/C-42 prerequisites satisfied |
| C-45 Two-dimensional ceiling table (phase × orthogonal) | **PASS** | 2D ceiling table: rows = evidence phase (Explore/Test/Validate), columns = inertia coverage (absent/present). Test phase: absent = 45, present = 60. "At the Test phase level, an investigation with at least one inertia-present signal earns a ceiling of 60 rather than 45 — confirming that inertia coverage independently shifts the ceiling at a fixed phase level." C-42 declaration names inertia coverage state. C-39 prerequisite satisfied. The role taxonomy is a separate annotation column from inertia coverage — C-44 and C-45 satisfied by distinct dimensions in the same Phase 1 pass |

**Essential PASS**: Yes. **Composite: ~122.5 (base) + 2.5 (C-44) + 2.5 (C-45) = ~127.5**. Golden ✓

---

### V-05 — Combined: Section-pair format + 3-column annotation (→ C-44 + C-45)

**Architecture base**: R12 V-01 stack with 3-column Phase 1 (same as V-04) + section-pair output format (each section followed by inline italicized pass condition directive).

| Criterion | Result | Evidence note |
|-----------|--------|--------------|
| Essential C-01…C-30 cluster | **PASS** | Format change (inline directives) is additive; does not touch essential criteria |
| C-35 | **PASS** | "Three cognitive roles execute concurrently in your reasoning. The output is a unified document — no role-labeled sections, no visible seams between roles" |
| C-36 | **PASS** | Gate block: SYNTHESIST ("Failure:" / "Passing:"), ADVERSARY ("Failure:" / "Passing:"), ANALYST ("Failure:" / "Passing:") — dual exemplars co-located per role |
| C-37 | **PASS** | Self-containment check maps 6 questions to named sections; Q6 maps Phase 1 declaration traceability to Verdict/Confidence section |
| C-38 | **PASS** | Open Questions section directive: "the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST)" in both the section instruction and the section pass condition |
| C-39 | **PASS** | 2D ceiling table in Phase 1 as pre-synthesis constraint; ceiling computation explicitly tied to annotation inventory |
| C-40 | **PASS** | Named "Gate Block" section indexing all three roles with exemplars; positioned after Roles section, before Output section |
| C-41 | **PASS** | Self-containment check: "If any question cannot be answered from the named section, revise that section before outputting" — slot-specific remediation |
| C-42 | **PASS** | "State before proceeding: 'Evidence phase coverage: [phases present]. Primary signals by phase: [count per phase]. Inertia coverage: [absent / partial / present]. Confidence ceiling: [value or 'none']'" — mandatory intermediate output with all classification dimensions |
| C-43 | **PASS** | All three roles in gate block carry both failure and passing exemplars co-located within each role's entry |
| C-44 Per-signal annotated inventory with role classification | **PASS** | Phase 1 annotates every signal with phase + role (Primary/Supporting/Contextual) + inertia as "enumerable per-signal inventory." Role annotation (second column) is present. Declaration extended with "Primary signals by phase: [count per phase]." Same rationale as V-04; section-pair format axis does not affect C-44 compliance |
| C-45 Two-dimensional ceiling table (phase × orthogonal) | **PASS** | Same 2D ceiling table as V-04 (phase × inertia, Test: 45 vs 60). "At Test phase, inertia coverage independently shifts the ceiling (45 → 60), confirming that the second dimension has distinct ceiling values at a fixed phase level." Declaration names inertia state. C-39 prerequisite satisfied |

**Essential PASS**: Yes. **Composite: ~122.5 (base) + 2.5 (C-44) + 2.5 (C-45) = ~127.5**. Golden ✓

---

## Score Summary

| Variation | Axis | C-44 | C-45 | Composite | Golden |
|-----------|------|------|------|-----------|--------|
| V-01 — Lifecycle emphasis | Single | PASS | FAIL | **~125.0** | ✓ |
| V-02 — Inertia framing | Single | FAIL | PASS | **~125.0** | ✓ |
| V-03 — Formal academic register | Single | FAIL | FAIL | **~122.5** | ✓ |
| V-04 — 3-column annotation | Combined | PASS | PASS | **~127.5** | ✓ |
| V-05 — Section-pair + 3-column | Combined | PASS | PASS | **~127.5** | ✓ |

---

## Excellence Signals from the R13 Top-Scoring Cluster

V-04 and V-05 tie at ~127.5. The advance over the single-axis variations is structural, not additive — a 3-column per-signal annotation satisfies C-44 and C-45 in a single Phase 1 pass because role taxonomy and inertia coverage are orthogonal annotation dimensions that do not conflict. Three patterns in V-04/V-05 exceed the current criteria battery and are candidates for R14:

**Pattern A — Single-pass multi-dimensional annotation as auditable computation chain**: The 3-column per-signal inventory makes every downstream value (phase coverage, Primary counts by phase, inertia state, ceiling) mechanically derivable by recomputing from the inventory table. A reader can audit the declared ceiling by summing columns and checking the intersection table — no inference from gestalt distribution required. C-44 and C-45 together require the *existence* of the inventory and that it *feeds* the declaration; they do not yet require that the declaration values be *provably consistent* with the inventory. A new criterion could require the per-signal table to appear in the output (not just as an instruction to produce it) so that the ceiling declaration is verifiable by inspection.

**Pattern B — Inline section pass condition (section-pair format, V-05 only)**: V-05's per-section italic directives co-locate the pass condition with the section it governs. This distributes verification to the point of production: a synthesizer can check each section's sufficiency without navigating to the self-containment check. The existing C-37/C-41 pair centralizes verification post-hoc; the inline directive makes it immediate and section-local. A new criterion could require that the pass condition for each output section appear inline within that section's instruction, not only in a separate self-containment block.

**Pattern C — Three-dimensional weight dominance specification**: Both V-04 and V-05 specify a fully ordered weight hierarchy across all three annotation dimensions simultaneously: Primary-Test-Inertia-present dominates Primary-Test-Inertia-absent, which dominates Primary-Explore-Inertia-absent, which dominates Supporting-Test, etc. The gate block exemplars instantiate this hierarchy with concrete comparison cases. No existing criterion requires that the weight dominance ordering be stated explicitly across all three axes — C-39 requires the phase dimension; C-44/C-45 add the role and inertia dimensions to the annotation. A new criterion could require a stated ordinal dominance rule for multi-dimensional weight ranking, making the SYNTHESIST's weighting function fully auditable.

---

## Ranking

1. **V-04** (~127.5) — 3-column annotation (phase + role + inertia); achieves first simultaneous C-44 + C-45
2. **V-05** (~127.5) — Same 3-column annotation plus section-pair format; tied with V-04; introduces Pattern B (inline section pass conditions) as candidate R14 signal
3. **V-01** (~125.0) — Role taxonomy single-axis; confirms C-44 earnable without 2D ceiling
4. **V-02** (~125.0) — Inertia framing single-axis; confirms C-45 earnable without role taxonomy
5. **V-03** (~122.5) — Register-independence control; confirms criteria battery is register-agnostic

---

```json
{"top_score": 127.5, "all_essential_pass": true, "new_patterns": ["3-column per-signal annotation (phase + role + inertia) makes ceiling declaration auditable by mechanical recomputation from the inventory table — derivation not inference", "Inline section pass conditions (section-pair format) co-locate the sufficiency test with the section it governs, distributing verification to the point of production rather than centralizing it in a post-hoc self-containment check", "Three-dimensional weight dominance hierarchy (phase × role × inertia) can be stated as an explicit ordinal rule, making the SYNTHESIST weighting function fully auditable across all annotation axes simultaneously"]}
```
