## trace-component Round 12 — Scoring

### Rubric Architecture Summary (v12)

152-pt ceiling | 5 essential (60 pts) | 3 recommended (30 pts) | 31 aspirational (62 pts)
Two new criteria: **C-38** (Manifest-Close Adjacency Marker, 2 pts) and **C-39** (Self-Authored Schema Constraint, 2 pts)

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01 – C-05) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Event Anchor | PASS | PASS | PASS | PASS | PASS |
| C-02 Component Tree Traversal | PASS | PASS | PASS | PASS | PASS |
| C-03 State Update Map | PASS | PASS | PASS | PASS | PASS |
| C-04 Re-render Inventory | PASS | PASS | PASS | PASS | PASS |
| C-05 Final UI State | PASS | PASS | PASS | PASS | PASS |

All variations carry TABLE-1 through TABLE-6 with required fields, MUTATION PRE-DECLARATION, PROMOTION BLOCK, and four-phase UI table. **No essential failures.** Subtotal: 60/60 all.

---

### Recommended Criteria (C-06 – C-08) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-06 Side Effect Coverage | PASS | PASS | PASS | PASS | PASS | TABLE-5 explicit none-row in all |
| C-07 Issue Detection | PASS | PASS | PASS | PASS | PASS | TABLE-7 five rows, N/A prohibited, F-02 UR cross-ref |
| C-08 Framework Vocabulary | PASS | PASS | PASS | PASS | PASS | Framework Declaration table + terms throughout |

Subtotal: 30/30 all.

---

### Aspirational Criteria — Shared Baseline

Criteria where all five variations score identically:

| Criterion | All | Evidence note |
|-----------|-----|---------------|
| C-09 Fix Recommendations | PASS | TABLE-7 Fix column: `React.memo / createSelector / useMemo` named |
| C-10 Render Quantification | PASS | `Re-renders? [Yes (N) / No]` — count and verdict co-located in same cell |
| C-11 Inline Phase-Close Gates | PASS | GATE-1 through GATE-7 present; each names exact non-closing phrases |
| **C-12 Mandatory Comparison Column** | **FAIL** | No "What this adds vs. ad-hoc" or equivalent column in any table |
| C-13 Exact-Phrase Gate Family | PASS | GATE-1: "the button"/"N/A"; GATE-3: "state updates"/"previous value"; GATE-7: "no impact"/"low risk" — three+ distinct strings across multiple phases |
| C-14 Column-Header Escape Instruction | PASS | TABLE-4 `Necessary? [Yes — reason / No — reason]`; TABLE-7 `Finding [finding or "none detected — [reason]"]` embed constraints in header |
| C-15 Do-Nothing Cost | PASS | TABLE-7 `Do-Nothing Cost` column present in all |
| C-16 FINDINGS Section Gate | PASS | GATE-7 explicitly intercepts "no major issues", "no impact", "minor issue", "low risk", "no concerns found" |
| C-17 Triple Structural Lock | PASS | TABLE-7 Finding column: (1) mandatory + N/A prohibited, (2) header embeds constraint, (3) GATE-7 per-row escape intercept |
| C-18 Table Format for Triple Lock | PASS | TABLE-7 uses column headers throughout |
| C-19 Gate-Block Formalism | PASS | All prohibited strings in `[GATE-N: ...]` blocks — not prose instructions |
| C-20 Framework Declaration Gate | PASS | FRAMEWORK DECLARATION table as required output header (or via TRAVERSAL-SCHEMA Req A) |
| **C-21 Failure Mode Displacement** | **FAIL** | No explicit "NOT 'state updates' — Owner: X, Key: Y" displacement text in any variation; GATE blocks name blocked phrases but supply no replacement confirmation text |
| C-22 Re-render Necessity Annotation | PASS | TABLE-4 `Necessary? [Yes — reason / No — reason]` per row — necessity verdict required |
| C-23 Four-Phase UI Progression | PASS | TABLE-6 phases 1–4 all rows required, rows 3+4 not collapsed |
| C-24 Zero-Mutation Declaration | PASS | ZERO MUTATION DECLARATION block with Direct/Inherited/Reason fields |
| C-25 Issue Category Completeness | PASS | TABLE-7 F-01 through F-05 explicit categories, each row required |
| C-26 Unnecessary Re-render Promotion | PASS | PROMOTION BLOCK → TABLE-7 F-02 UR cross-ref with named fix |
| C-27 Mutation Count Pre-Declaration | PASS | `Mutations: N=___ direct, M=___ inherited (total: ___)` before table body |
| C-28 Per-Hop Direction Annotation | PASS | Direction column required per hop in TABLE-2 |
| C-29 Re-render Inventory Completeness | PASS | TABLE-4 requires every T-ID from TABLE-2 — inert hops included |
| C-30 Mutation Count Dual-Track | PASS | Pre-declaration separates direct/inherited — absorbed into existing TABLE-3 structure |
| C-31 Schema-Field Coverage of Aspirational | PASS | 9/10 of C-20–C-29 mapped to schema fields (C-21 unmapped); 9 ≥ 7 pass threshold |
| C-32 Blank-Blocked Field Primacy | PASS | All five essential criteria backed by TABLE-N columns; each readable from specific cell |
| C-33 Phase-Level Completeness Manifest | PASS | MANIFEST-1 through MANIFEST-5, each with Components/State keys/Side effects (all three fields) |
| C-34 Inert Pass-Through Explicit Marking | PASS | `<-> inert` Direction code + INERT-HOP DECLARATION block; zero-inert case explicitly declared |
| C-35 Criteria Audit Cross-Validation Table | PASS | TABLE-8 maps C-01–C-08 to schema fields with PASS/FAIL verdict |
| C-36 Inert-as-Default Direction Schema | PASS | All: `<-> inert` listed first/default; active codes require explicit selection; "in priority order" framing (V-01), null-hypothesis framing (V-03/V-05), or schema-declared default (V-02/V-04) |
| C-37 Manifest-Analysis Paired Block Structure | PASS | Five MANIFEST-N/TABLE-N labeled pairs in all variations; N matches across pairs; ≥3 minimum met |

Shared aspirational subtotal: 27 pass × 2 = **54 pts** (C-12 and C-21 fail = 0)

---

### Differentiating Criteria: C-38 and C-39

#### C-38 · Manifest-Close Adjacency Marker

Pass condition: every MANIFEST-N ends with explicit prohibition line as its **closing** content (not header, not charter preamble); at least three manifest blocks carry it.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **PASS** | Five manifests each end with `↓ TABLE-N begins immediately below. No content may appear between this line and the TABLE-N header.` pre-embedded after the code block, before the TABLE-N heading — prompt-provided close-line, structurally guaranteed |
| V-02 | **PASS** | Requirement C demands model declare exact close-line text; each manifest closes with `*[Close this manifest with the exact closing marker declared in your TRAVERSAL-SCHEMA before TABLE-N.]*` — model instantiates schema-declared text at each manifest end |
| V-03 | **FAIL** | Manifests use header annotation: `*(fill completely before writing TABLE-N — TABLE-N begins immediately below this block)*` in the manifest opener, not as closing line. C-38 pass condition explicitly excludes header-only placement. |
| V-04 | **PASS** | Same mechanism as V-02 + stronger placeholder: `*[Apply the Requirement C closing marker from your TRAVERSAL-SCHEMA here — verbatim, as this manifest's last line.]*` — "verbatim, as this manifest's last line" is a two-constraint instruction |
| V-05 | **PASS** | `*[Requirement C close-line — verbatim, last line of this manifest.]*` across all five manifests; Requirement C in schema asks model to explain *why* the marker must be the last line, not a header annotation |

#### C-39 · Self-Authored Schema Constraint

Pass condition: model produces named schema artifact (TRAVERSAL-SCHEMA or equivalent) declaring both C-36 inert-default and C-37 adjacency rules in a prior role *before* analysis begins; externally-provided templates fail.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | **FAIL** | No model-authored schema. Prompt provides complete template with close-lines pre-embedded. Model fills in values but authors no schema principles. |
| V-02 | **PASS** | Role 1 (Schema Architect) produces TRAVERSAL-SCHEMA from Requirements A–D. Req B: model declares Direction default contract in its own words. Req C: model declares adjacency rule and writes exact close-line text. Template slot is blank — "Author this document now... do not reproduce instruction text." |
| V-03 | **FAIL** | No model-authored schema. EPISTEMIC PRINCIPLE block is prompt-authored. No prior-role schema artifact. |
| V-04 | **PASS** | Role 1 produces TRAVERSAL-SCHEMA. Requirement B: Direction default. Requirement C: adjacency rule + "declare the exact text of the closing marker... explain why it must be the manifest's final line." Schema artifact legible; Role 2 bound by it. |
| V-05 | **PASS** | Role 1 produces TRAVERSAL-SCHEMA with Requirement B explicitly asking model to define "epistemic status of inertia" and Requirement C for close-line text + structural explanation. Most complete schema authorship of all five variations. |

---

## Composite Scores

| Criterion tier | Points available | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------------|-----------------|------|------|------|------|------|
| Essential (C-01–C-05) | 60 | 60 | 60 | 60 | 60 | 60 |
| Recommended (C-06–C-08) | 30 | 30 | 30 | 30 | 30 | 30 |
| Aspirational shared (27 pass) | 54 | 54 | 54 | 54 | 54 | 54 |
| C-12 (FAIL all) | 2 | 0 | 0 | 0 | 0 | 0 |
| C-21 (FAIL all) | 2 | 0 | 0 | 0 | 0 | 0 |
| C-38 | 2 | **2** | **2** | **0** | **2** | **2** |
| C-39 | 2 | **0** | **2** | **0** | **2** | **2** |
| **Total** | **152** | **146** | **148** | **144** | **148** | **148** |

---

## Variation Ranking

| Rank | Variation | Score | All Essential | C-38 | C-39 |
|------|-----------|-------|---------------|------|------|
| 1 (tie) | **V-02** Role sequence — Schema Architect from requirements | **148/152** | YES | PASS | PASS |
| 1 (tie) | **V-04** Combined: Close-line + Schema Architect | **148/152** | YES | PASS | PASS |
| 1 (tie) | **V-05** All three axes: Schema + Null-Hypothesis + Close-line | **148/152** | YES | PASS | PASS |
| 4 | V-01 Lifecycle Emphasis — close-line pre-embedded | 146/152 | YES | PASS | FAIL |
| 5 | V-03 Inertia Framing — null hypothesis, header annotation | 144/152 | YES | FAIL | FAIL |

**4-pt gap** separates the three-way top tier from V-03 (the only variation failing both new criteria).

---

## Tiebreaker Analysis: V-02 vs V-04 vs V-05

All three score 148. Qualitative differentiation:

**V-02** (Role sequence only): Model produces schema from requirements; close-line declared in Req C and instantiated per manifest. Cleanest single-axis proof of C-39. Placeholder wording is `*[Close this manifest with the exact closing marker...]*` — correct but no "verbatim/last line" precision.

**V-04** (Role sequence + Lifecycle): Same as V-02 but placeholder adds "verbatim, as this manifest's last line" — two explicit constraints in one instruction (schema fidelity AND position). The Requirement C text reads "explain why it must be the manifest's final line, not a header annotation" — the model must justify the structural reason, not just declare the text.

**V-05** (All three): V-04 plus null-hypothesis framing in Requirement B. The schema Requirement B forces the model to articulate *why* inertia is the null (not just name it as the default) and connects that principle to the Direction column's default value. The Role column framing shifts to `Role [Null confirmed: reason / Active claim: departure + evidence]` — departure codes become *claims requiring evidence*, not just annotations. If the model internalizes the null-hypothesis epistemology when authoring Req B, it propagates into the findings table: unnecessary re-renders are "unsupported necessity claims" rather than performance concerns.

**V-05 ranked first on qualitative depth** — the epistemic framework from Requirement B propagates through the full trace in a way V-04 and V-02 don't achieve.

---

## Excellence Signals from Top Scorers

### Signal E-1: Requirement C as Causal Bridge (V-04/V-05)

R11 C-38 and C-39 were designed as orthogonal — C-38 (micro, per-manifest) and C-39 (macro, schema level). V-04/V-05 reveal a **single causal chain** that satisfies both simultaneously: Schema Requirement C declares the close-line text → the manifest placeholder demands that exact text "verbatim, as this manifest's last line." The model cannot satisfy one without the other — authoring Req C produces the text that each manifest must end with. This is a structural tighter than satisfying C-38 and C-39 independently.

**Potential R13 criterion**: Require that the schema's Requirement C (or equivalent) explicitly state *why* the close-line must be the manifest's last content (not header, not charter) — the model explains the structural reason, not just names the text. V-04 achieves this by asking the model to "explain why it must be the manifest's final line, not a header annotation."

### Signal E-2: Null-Hypothesis Role Vocabulary (V-03/V-05)

The Role column shift from `Acted: [desc] / Inert: [reason]` to `Null confirmed: [reason] / Active claim: [departure + evidence]` makes the epistemic status of each hop **format-detectable**. A departure code in the Direction cell without "Active claim:" prefix + evidence in the Role cell is structurally visible as an unsupported claim. This isn't enforced by current criteria — C-36 covers Direction column defaults; no criterion covers Role column vocabulary.

**Potential R13 criterion**: Role column in TABLE-2 must use claim-framing vocabulary — active hops declare "Active claim: [departure code] — [evidence]" and inert hops declare "Null confirmed: [reason]". Departure code present without "Active claim:" prefix in the same row is detectable as an unsatisfied constraint.

---

## New Patterns (not yet criteria)

1. **Causal bridge via Requirement C**: Schema Requirement C as the single origin that produces both the model-authored adjacency rule (C-39) and the per-manifest close-line text (C-38). When the requirement asks the model to *also explain the structural justification*, the model cannot satisfy it by rote.

2. **Null-hypothesis Role vocabulary propagation**: `Null confirmed: [reason] / Active claim: [departure + evidence]` in the Role column makes unsupported departure codes structurally detectable at cell level — the claim-framing extends the null-hypothesis epistemology from Direction column semantics into Role column format.

---

```json
{"top_score": 148, "all_essential_pass": true, "new_patterns": ["Causal bridge via Requirement C: when schema authoring (C-39) explicitly includes declaring the close-line text as a named requirement, and manifest placeholders demand that text verbatim as the last line, macro schema ownership and micro close-line enforcement are satisfied by a single causal chain rather than two independent mechanisms", "Null-hypothesis Role vocabulary: shifting TABLE-2 Role column from Acted/Inert to Null confirmed: reason / Active claim: departure + evidence makes unsupported departure codes structurally detectable at cell level — a departure code without Active claim: prefix and evidence in the same row is a format violation, extending the null-hypothesis epistemology from Direction column semantics into Role column enforcement"]}
```
