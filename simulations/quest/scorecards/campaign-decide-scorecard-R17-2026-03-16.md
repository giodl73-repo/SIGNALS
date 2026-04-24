## campaign-decide — Round 17 Scoring

**Rubric**: campaign-decide-rubric-v16 | **Max**: 107.0 | **Variations**: V-01 through V-05

---

### Baseline Verification

All R17 variations inherit the full R16 V-05 structural payload:
- **C-41** — `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]` in Phase 5 header: all variations ✓
- **C-42** — `(fill-now)` / `(defer-to-Phase-5)` per-column bracket notation in all closure directives: all variations ✓

R17 axes introduce three independent experiments over the 107.0 baseline.

---

### Per-Variation Scoring

#### V-01 — C-43 candidate: temporal commit at SCHEMA PREAMBLE definition time

| Tier | Criteria | Verdict | Notes |
|------|----------|---------|-------|
| Essential | C-01..C-05 | PASS ×5 | Recommendation schema, confidence, 6 domains, 1a before 1b, citation columns all structurally enforced |
| Recommended | C-06..C-08 | PASS ×3 | FINDING REGISTER scaffold, counter-evidence 4-column, hypothesis resolution table present |
| C-09 | Confidence Rationale column | PASS | `Confidence Rationale (cite FIDs — not label alone)` in header |
| C-10 | FID consistency | PASS | Pre-seeded register covers all phases |
| C-11 | Cross-phase citation | PASS | `Citation (Phase N, F[N]-seq)` column header |
| C-12 | Segment scoring | PASS | `Fit Score (1-10)` column in Phase 3 |
| C-13 | Prior Confidence in Phase 0 | PASS | `Prior Confidence (fill-now)` in preamble schema |
| C-14 | Gate annotations | PASS | All phase headers carry `[COMPLETE BEFORE PHASE N]` or equivalent |
| C-15 | Traffic-light | PASS | `Severity (R/Y/G)` in Phase 2 |
| C-16 | Pre-seeded register | PASS | `[PRE-SEED BEFORE PHASE 0]` gate annotation |
| C-17 | 6-slot Because block | PASS | Schema rows: 0/PRIOR, 1a/INERTIA, 1b/RIVALS, 2/FEASIBILITY, 3/MARKET, 4/WEB EVIDENCE |
| C-18 | Recommendation record 4 cols | PASS | FID, Recommendation, Confidence, Confidence Rationale |
| C-19 | Counter-evidence record | PASS | Counter-Evidence, Qualifying FID, Recommended Next Step, Condition |
| C-20 | Gate annotations all phases | PASS | Phases 0-5 all carry gate annotations |
| C-21 | Phase 1a/1b gate | PASS | `[COMPLETE BEFORE Phase 1b]` distinct from inter-phase gate |
| C-22 | Hybrid citation format in header | PASS | `Citation (Phase N, F[N]-seq)` column header |
| C-23 | Domain-specific headers | PASS | No generic "Field/Value/Item" headers anywhere |
| C-24 | 1a/1b synthesis split | PASS | Phase 1a/INERTIA and Phase 1b/RIVALS distinct rows in Because schema |
| C-25 | Because table 4 cols | PASS | Phase, Label, Citation, Claim |
| C-26 | Per-rival response strategy | PASS | Response Strategy column + FINDING REGISTER Note "with response strategy" |
| C-27 | Prose-free structural sufficiency | PASS | All C-01..C-26 verifiable from headers and structure; no prose load-bearing |
| C-28 | Phase 0 experiment lifecycle schema | PASS | 7 columns; `(fill-now)`/`(defer-to-Phase-5)` in preamble column headers (C-43 form) |
| C-29 | Inertia primacy dual-signal | PASS | `[INERTIA IS THE PRIMARY COMPETITOR]` in header + `primary competitor: YES` in register |
| C-30 | Phase 5 bold sub-table labels | PASS | **Hypothesis resolution:**, **Recommendation record:**, **Counter-evidence:**, **Counter Block:** |
| C-31 | Phase 1a Switching Cost col | PASS | `FID / Finding Summary / Primary Competitor / Switching Cost` schema |
| C-32 | Phase 5 Counter Block schema | PASS | `FID / Counter Claim / Rebuttal`, structurally distinct from Counter-evidence |
| C-33 | Confidence quantified thresholds | PASS | H=80%+ / M=50-79% / L<50% in evidence entry and recommendation schemas |
| C-34 | Threshold in pre-Phase-0 schema | PASS | Evidence entry schema in SCHEMA PREAMBLE carries threshold in Confidence column header |
| C-35 | Prior Confidence in Phase 5 resolution | PASS | `Prior Confidence` column in hypothesis resolution schema |
| C-36 | Per-phase closure directives | PASS | `Close FINDING REGISTER Phase N rows` after each phase |
| C-37 | Hypothesis resolution schema in preamble | PASS | Schema pre-defined in SCHEMA PREAMBLE + "Fill from Schema Preamble" directive |
| C-38 | Column-specific closure directives | PASS | All closure directives name specific columns |
| C-39 | Fill-forward in Phase 5 header | PASS | `[SCHEMAS: ... — from SCHEMA PREAMBLE]` in Phase 5 section header |
| C-40 | Bracket notation for column lists | PASS | `[columns: FID (key, fill-now), ...]` bracket notation throughout |
| C-41 | Named-schema enumeration | PASS | `hypothesis-resolution, recommendation-record, because-block` individually named |
| C-42 | Per-column temporal annotation | PASS | `(fill-now)`/`(defer-to-Phase-5)` per column in all closure directives |

**Excellence signal (C-43 candidate)**: `| FID (key, fill-now) | Hypothesis (fill-now) | ... | Actual Outcome (Phase 5, defer-to-Phase-5) | Status (defer-to-Phase-5) |` — temporal commit encoded at SCHEMA PREAMBLE definition time. Downstream closure directives become confirmations, not declarations.

**V-01 composite: 107.0 / 107.0** | Essential PASS | New pattern: C-43

---

#### V-02 — Single axis: Decision Stakes inertia narrative block

All structural criteria identical to V-01 baseline except C-43 preamble temporal encoding is absent (Phase 0 schema uses parenthetical form: `Expected Result (Phase 0)` / `Actual Outcome (Phase 5)` rather than explicit `(fill-now)`/`(defer-to-Phase-5)` annotations).

| Changed criteria | Verdict | Notes |
|-----------------|---------|-------|
| C-28 | PASS | Parenthetical in column name satisfies alternative condition |
| C-42 | PASS | Closure directives carry per-column temporal annotations (gate-time, not preamble-time) |
| All others | PASS | Identical to V-01 except Decision Stakes prose block added before SCHEMA PREAMBLE |
| C-27 | PASS | Decision Stakes block is framing prose; no C-01..C-26 criterion requires reading it |

**Excellence signal (none new)**: Decision Stakes is a semantic priming innovation (prose framing for C-04/C-29 compliance) — valuable behavioral signal but not a new structural criterion.

**V-02 composite: 107.0 / 107.0** | Essential PASS | No new structural pattern

---

#### V-03 — Single axis: Per-phase minimum evidence count annotations

Adds `[min: 3 experiments]`, `[min: 1 inertia entry]`, `[min: 2 named rivals]`, `[min: 1 named barrier]`, `[min: 1 segment with fit score]`, `[min: 1 web-sourced entry with source and date]` to phase section headers. Uses same Phase 0 schema form as V-02 (no C-43).

| Changed criteria | Verdict | Notes |
|-----------------|---------|-------|
| C-14 / C-20 | PASS | Phase gate annotations still present; `[min: N]` annotations are additive, not replacing |
| C-23 | PASS | All domain-specific headers maintained |
| All others | PASS | Identical structural payload to V-02 |
| C-27 | PASS | Min-count annotations are header-level structural gates; no prose is load-bearing |

**Excellence signal (C-44 candidate)**: `[min: 2 named rivals]` in Phase 1b header — per-phase minimum evidence count as bracket-notation gate annotation, detectable by header scan without reading table body. Table under-population becomes a header-level failure class distinct from C-01..C-42.

**V-03 composite: 107.0 / 107.0** | Essential PASS | New pattern: C-44

---

#### V-04 — Combined: C-43 + phase budgets (V-01 + V-03)

Carries both C-43 preamble temporal encoding AND per-phase `[min: N]` budget annotations.

| Criteria | Verdict | Notes |
|----------|---------|-------|
| C-28 | PASS | C-43 form in preamble (fill-now/defer-to-Phase-5 in column headers) |
| C-42 | PASS | Closure directives confirm preamble annotation; temporal per-column in bracket notation |
| All others | PASS | Full V-01 + V-03 payload combined |
| C-27 | PASS | Both axes are structural; no prose load-bearing |

**Excellence signals**: C-43 (preamble temporal) + C-44 (phase budgets) — orthogonal axes, no interaction.

**V-04 composite: 107.0 / 107.0** | Essential PASS | Two new patterns confirmed

---

#### V-05 — Full integration: C-43 + Decision Stakes + phase budgets

Carries all three R17 axes over the R16 V-05 baseline. Decision Stakes block + C-43 preamble temporal + C-44 phase budget minimums.

| Criteria | Verdict | Notes |
|----------|---------|-------|
| C-28 | PASS | C-43 column headers in preamble |
| C-42 | PASS | Per-column temporal in bracket notation; preamble is single source of truth, gates confirm |
| C-39 / C-41 | PASS | `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]` inherited |
| All others | PASS | Full payload; Phase 5 closure note: "column temporal commits declared in SCHEMA PREAMBLE, confirmed here" |
| C-27 | PASS | Decision Stakes prose is framing; all criteria structurally verifiable |

**Excellence signals**: C-43 + C-44 + Decision Stakes semantic priming. Phase 5 closure language is strongest: "confirmed from preamble schema" emphasizes the confirmation-not-declaration semantic.

**V-05 composite: 107.0 / 107.0** | Essential PASS | All three R17 patterns

---

### Composite Score Table

| Var | Essential (60) | Recommended (30) | Aspirational C-09..C-42 (17) | Total | C-43 | C-44 |
|-----|---------------|-----------------|------------------------------|-------|------|------|
| V-01 | 60.0 | 30.0 | 17.0 | **107.0** | ✓ | — |
| V-02 | 60.0 | 30.0 | 17.0 | **107.0** | — | — |
| V-03 | 60.0 | 30.0 | 17.0 | **107.0** | — | ✓ |
| V-04 | 60.0 | 30.0 | 17.0 | **107.0** | ✓ | ✓ |
| V-05 | 60.0 | 30.0 | 17.0 | **107.0** | ✓ | ✓ |

**Ranking (by candidate pattern coverage)**:
1. **V-05** — C-43 + C-44 + Decision Stakes semantic priming (3 axes); "confirmed from preamble" language strongest
2. **V-04** — C-43 + C-44 (2 structural axes); no Decision Stakes
3. **V-01** — C-43 only; single-axis preamble temporal encoding
4. **V-03** — C-44 only; single-axis phase budgets
5. **V-02** — Decision Stakes only; semantic priming, no new structural criterion

---

### Excellence Signals from V-05 (top variation)

**Signal 1 — C-43 preamble temporal encoding**: Encoding `(fill-now)` / `(defer-to-Phase-5)` directly in SCHEMA PREAMBLE column headers at definition time converts temporal commit from a gate-instruction (declared 5× across closure directives) to a schema property (declared once, propagated everywhere). The Phase 5 closure note "column temporal commits declared in SCHEMA PREAMBLE, confirmed here" explicitly states the confirmation-not-declaration semantic — highest structural authority for fill discipline.

**Signal 2 — C-44 per-phase minimum annotations**: `[min: N]` bracket annotations in phase section headers elevate evidence-density requirements from body-level prose ("list at least two named rivals") to header-level structural gates. A reviewer scanning only section headers can detect gate-annotation violation without opening any table. This is the same structural authority level as completion gates (`[COMPLETE BEFORE PHASE N]`) — the minimum is structurally co-equal with the phase boundary.

**Signal 3 — "confirmed here" closure language**: V-05 Phase 5 closure note reads "column temporal commits declared in SCHEMA PREAMBLE, confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)]." The word "confirmed" is architecturally precise — it makes the declaration/confirmation distinction explicit at the point of Phase 5 closure, reinforcing that the preamble is the single source of truth.

---

```json
{"top_score": 107.0, "all_essential_pass": true, "new_patterns": ["C-43: temporal commit annotation encoded in SCHEMA PREAMBLE column headers at definition time — (fill-now)/(defer-to-Phase-5) per column in preamble schema, downstream closure directives confirm rather than declare", "C-44: per-phase minimum evidence count as bracket-notation gate annotation in section header — [min: N] at header level makes table under-population detectable by header scan without reading table body"]}
```
