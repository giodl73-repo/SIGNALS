Now I have all five variations. Let me score them.

---

# draft-pitch — Scorecard R5 (2026-03-14)

## Baseline Context

R4 V-05 scored 100/Platinum on v4 rubric. Against v5 it retroscores 98.57: passes C-19 (embedded negative example in Failure Mode definition), passes C-20 (`[active Exec inertia from SIGNAL DEFAULTS]` names source within placeholder), fails C-21 (both CTA placeholders source from SIGNAL DEFAULTS, a static block; no placeholder naming a dynamic gate output). All five R5 variations target C-21 by adding a placeholder that names AUDIENCE BELIEF MAP — produced by Phase 2 gate — while preserving all prior criteria.

---

## Criteria Evaluation

### Shared Structure (C-01 through C-17)

All five variations inherit the identical Phase 1–4 backbone plus Phase 6–7. Criteria C-01 through C-17 are evaluated once and apply to all.

| ID | Criterion | All 5 | Evidence |
|----|-----------|-------|----------|
| C-01 | Three versions present | PASS | Exec, Dev, Maker sections in Phase 5 |
| C-02 | All four elements per version | PASS | Hook, What, Why, CTA in all three |
| C-03 | Exec version outcome-first | PASS | Phase 4 gate forces outcome sentence before any product mention |
| C-04 | Anti-positioning section | PASS | Phase 6 produces "What Signal Is NOT" |
| C-05 | Dev version shows concrete interaction | PASS | `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md` |
| C-06 | Maker version jargon-free | PASS | "Zero unexplained acronyms. Zero namespace references. Zero CLI terminology." |
| C-07 | Prior signals consulted | PASS | Phase 1 checks three signal paths before any drafting |
| C-08 | Proof points specific and traceable | PASS | Phase 7 proof audit; Proof fallback: "730+ scenarios (simulations/techniques/)" |
| C-09 | Inertia named as primary competitor | PASS | POSITIONING LOCK: "The real competition... is not a named tool. It is ___." |
| C-10 | Exec self-check embedded at generation time | PASS | Phase 4 binary gate: write → test → rewrite until YES, locked before Phase 5 |
| C-11 | Positioning answers locked before prose | PASS | Phase 3 POSITIONING LOCK fully written before Phase 5 |
| C-12 | Default fallback values for missing signals | PASS | SIGNAL DEFAULTS table: 11 fields with explicit values per signal type |
| C-13 | DEFAULTS TABLE loaded unconditionally before intake | PASS | SIGNAL DEFAULTS block appears before Phase 1; no conditional loading |
| C-14 | Gate output named and cited by downstream | PASS | AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE all named in *Produces* and cited by Phase 5 *Consumes* by exact name |
| C-15 | Audience belief mapping precedes argument construction | PASS | Phase 2 (BELIEF MAP) produces written anchors before Phase 5 drafts |
| C-16 | Multi-node named dependency chain | PASS | Three-node chain: AUDIENCE BELIEF MAP (Phase 2) → POSITIONING LOCK (Phase 3) → EXEC OPENING SENTENCE (Phase 4), all consumed by Phase 5 by exact name |
| C-17 | Belief mapping includes per-audience failure modes | PASS | Failure Mode column definition: "A restatement of Core Belief in negative form does not pass (e.g., 'Exec won't believe the ROI argument' -- this restates the belief and is not a Failure Mode)" — present in all five |

---

### Differentiating Criteria (C-18 through C-21)

#### C-18 — Per-audience inertia fields in DEFAULTS with structural CTA template

Pass condition: distinct per-audience inertia field in SIGNAL DEFAULTS + CTA construction via explicit structural template. "(e.g., 'Instead of [inertia argument], [action]')" is an example form, not a required syntax.

| Var | C-18 | Evidence |
|-----|------|----------|
| V-01 | PASS | Per-audience DEFAULTS rows (Exec/Dev/Maker inertia). CTA: "Instead of [active Exec inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, exec row]." Explicit structural template. |
| V-02 | PASS | Per-audience DEFAULTS rows. CTA: "Instead of [inertia argument from AUDIENCE BELIEF MAP, exec row], [one specific decision...]." Structural template; inertia argument bound per-audience from DEFAULTS via BELIEF MAP Inertia Excuse column. |
| V-03 | PASS | Per-audience DEFAULTS rows. CTA: "Status quo: [active X inertia from SIGNAL DEFAULTS]. Action: [Inertia Counter from AUDIENCE BELIEF MAP, X row]." Two-part structural template. C-18 pass condition says "e.g." for the "Instead of" form; structural template is present and addresses per-audience inertia. |
| V-04 | PASS | Per-audience DEFAULTS rows. DEFAULTS binding declaration explicit in Phase 2. CTA: "Instead of [inertia argument from AUDIENCE BELIEF MAP, exec row], [Inertia Counter from AUDIENCE BELIEF MAP, exec row]." Per-audience inertia sourced through BELIEF MAP (bound from DEFAULTS). |
| V-05 | PASS | Per-audience DEFAULTS rows. CTA: "Instead of [active Exec inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, exec row]." Classic "Instead of" form with per-audience DEFAULTS source. |

#### C-19 — Definitional instruction includes embedded named negative example

| Var | C-19 | Evidence |
|-----|------|----------|
| V-01 | PASS | Failure Mode definition: named prohibited form ("Exec won't believe the ROI argument") + explicit "this restates the belief and is not a Failure Mode" |
| V-02 | PASS | Identical Failure Mode definition |
| V-03 | PASS | Identical Failure Mode definition |
| V-04 | PASS | Identical Failure Mode definition |
| V-05 | PASS | Identical Failure Mode definition |

#### C-20 — Structural template placeholder names its source artifact within placeholder syntax

| Var | C-20 | Evidence |
|-----|------|----------|
| V-01 | PASS | CTA first placeholder: `[active audience inertia from SIGNAL DEFAULTS]` — names SIGNAL DEFAULTS within the placeholder. |
| V-02 | PASS | BELIEF MAP cell instruction: `[active Exec inertia from SIGNAL DEFAULTS]` / `[active Dev inertia from SIGNAL DEFAULTS]` / `[active Maker inertia from SIGNAL DEFAULTS]` — names SIGNAL DEFAULTS within each per-audience placeholder. |
| V-03 | PASS | CTA Part 1: `[active X inertia from SIGNAL DEFAULTS]` — names SIGNAL DEFAULTS within the placeholder. |
| V-04 | PASS | DEFAULTS binding declaration templates: `[active Exec inertia from SIGNAL DEFAULTS]`, `[active Dev inertia from SIGNAL DEFAULTS]`, `[active Maker inertia from SIGNAL DEFAULTS]` — names SIGNAL DEFAULTS within each placeholder. |
| V-05 | PASS | BELIEF MAP column definition: `[active Exec inertia from SIGNAL DEFAULTS]` per audience. CTA first placeholder also names SIGNAL DEFAULTS. Redundant coverage at two structural locations. |

#### C-21 — Structural template placeholder cites a dynamic gate output, creating visible execution dependency

Pass condition: placeholder names AUDIENCE BELIEF MAP (produced by Phase 2 gate step) by exact name assigned in *Produces* declaration; a SIGNAL DEFAULTS-only template does not pass.

| Var | C-21 | Evidence |
|-----|------|----------|
| V-01 | PASS | CTA second placeholder: `[Inertia Counter from AUDIENCE BELIEF MAP, audience row]` — names AUDIENCE BELIEF MAP by exact name from Phase 2 *Produces*. Execution dependency: Phase 5 CTA cannot be completed without Phase 2 gate having run and locked AUDIENCE BELIEF MAP. |
| V-02 | PASS | CTA: `[inertia argument from AUDIENCE BELIEF MAP, exec row]` — names AUDIENCE BELIEF MAP by exact Phase 2 *Produces* name. AUDIENCE BELIEF MAP is a Phase 2 gate output, not a static block. Execution dependency visible. |
| V-03 | PASS | CTA Part 2: `[Inertia Counter from AUDIENCE BELIEF MAP, X row]` — names AUDIENCE BELIEF MAP by exact Phase 2 *Produces* name. Execution dependency: "Action" part cannot be filled without Phase 2 complete. |
| V-04 | PASS | CTA: `[inertia argument from AUDIENCE BELIEF MAP, audience row]` — names AUDIENCE BELIEF MAP by exact Phase 2 *Produces* name. Both CTA placeholders reference AUDIENCE BELIEF MAP; the inertia values were bound from DEFAULTS into AUDIENCE BELIEF MAP at Phase 2, making AUDIENCE BELIEF MAP the authoritative dynamic source for Phase 5. |
| V-05 | PASS | CTA second placeholder: `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]`. Traceability declaration explicitly calls out: "AUDIENCE BELIEF MAP (gate output from Phase 2, produced and locked before Phase 5 begins; exact name used in *Produces* declaration above)." Strongest structural enforcement of visible execution dependency. |

---

## Composite Scores

Formula: `(essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/14 * 10)`

| Variation | Essential (4/4) | Recommended (3/3) | Aspirational (14/14) | Composite | Tier |
|-----------|-----------------|-------------------|----------------------|-----------|------|
| V-01 | 60 | 30 | 10 | **100** | Platinum |
| V-02 | 60 | 30 | 10 | **100** | Platinum |
| V-03 | 60 | 30 | 10 | **100** | Platinum |
| V-04 | 60 | 30 | 10 | **100** | Platinum |
| V-05 | 60 | 30 | 10 | **100** | Platinum |

All five variations score 100/Platinum. The diagnostic question (V-03: does C-18 require "Instead of" syntax?) resolves as PASS: C-18's pass condition uses "(e.g.)" to introduce the template form example; V-03's "Status quo: [X]. Action: [Y]." satisfies the structural requirement with per-audience DEFAULTS fields and a two-part structural template.

---

## Ranking

All five tie at 100. Within the Platinum cluster, differentiation by structural depth:

| Rank | Variation | Structural distinction |
|------|-----------|----------------------|
| 1 | **V-05** | Traceability declaration names both source types by kind (static/dynamic) + per-audience cell templates at BELIEF MAP step + pre-commit instruction for Inertia Counter. Most inspectable from skill text alone. |
| 2 | **V-04** | Phase-split source citations: DEFAULTS binding as explicit pre-table instruction in Phase 2, CTA names AUDIENCE BELIEF MAP exclusively. Cleanest single-source CTA. |
| 2 | **V-02** | Same phase-split pattern as V-04 but per-row cell instructions in BELIEF MAP rather than a pre-table binding block. |
| 4 | **V-01** | Both sources in single CTA line — minimal change from R4 V-05, single axis. Effective but least architectural. |
| 4 | **V-03** | Diagnostic variation. Two-part "Status quo / Action" template resolves the C-18 form question (form-agnostic). Same structural coverage as V-01. |

**Golden candidate: V-05** — combines all three axes, introduces traceability declaration, pre-commit instruction, and redundant C-20 coverage at BELIEF MAP step and CTA.

---

## Excellence Signals

Three new patterns emerge from R5 that were not captured by C-19/C-20/C-21:

**V-05-E-01**: **Dual-source traceability declaration in Phase 5** — An explicit prose paragraph at the CTA construction step names both source types (static defaults block / dynamic gate output), their provenance, and asserts that both placeholders must be resolved before CTA construction is complete. This makes the static/dynamic dependency structure inspectable from skill text alone without needing to trace execution. Example: "The two placeholders have distinct source types: `[active [audience] inertia from SIGNAL DEFAULTS]` -- draws from SIGNAL DEFAULTS (static block, available before any phase runs)... `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]` -- draws from AUDIENCE BELIEF MAP (gate output from Phase 2, produced and locked before Phase 5 begins...)."

**V-05-E-02**: **Inertia Counter pre-commit instruction at population time** — The BELIEF MAP Inertia Counter column definition tells the model, at Phase 2 fill time, exactly how this cell will be consumed in Phase 5: "Pre-commit this value -- Phase 5 CTA uses `[Inertia Counter from AUDIENCE BELIEF MAP, audience row]` by exact reference. Do not leave ambiguous." This creates a forward declaration at data-entry time, preventing vague population that breaks downstream reference.

**V-02/V-04-E-01**: **Phase-split source citation** — C-20 (static source) and C-21 (dynamic gate output) satisfied at different structural locations: C-20 at the data-binding step (Phase 2, where the DEFAULTS values are written into BELIEF MAP), C-21 at the output-construction step (Phase 5 CTA). This makes each source citation visible at its natural point of origin rather than only at consumption.

---

## Saved to

`simulations/quest/scorecards/draft-pitch-scorecard-R5-2026-03-14.md`

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dual-source traceability declaration in CTA construction step names both source types (static defaults block vs. dynamic gate output) by kind with provenance statement and completion constraint", "Inertia Counter pre-commit instruction at BELIEF MAP fill time names the exact Phase 5 citation form, creating forward declaration at data-entry time", "Phase-split source citation: C-20 (static source) satisfied at BELIEF MAP binding step, C-21 (dynamic gate output) satisfied at CTA construction step -- each citation visible at its point of origin"]}
```
