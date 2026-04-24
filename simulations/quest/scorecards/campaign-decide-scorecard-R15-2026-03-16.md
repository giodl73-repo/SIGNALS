## R15 — campaign-decide Scoring Report

**Rubric**: v14 (38 criteria, max 105.0)
**Variations**: V-01 through V-05

---

## Scoring Legend

| Symbol | Meaning |
|--------|---------|
| PASS | Criterion fully satisfied |
| PARTIAL | Criterion partially satisfied (0.25 pts for aspirational) |
| FAIL | Criterion not satisfied |

---

## V-01 — C-37 fill-forward in Phase 5 header annotation

### Essential (C-01–C-05)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Recommendation column present in pre-seeded recommendation record schema |
| C-02 | PASS | `Confidence (H=80%+ / M=50-79% / L<50%)` column in recommendation schema |
| C-03 | PASS | All phases present: 0, 1a, 1b, 2, 3, 4, 5 |
| C-04 | PASS | Phase 1a `[COMPLETE BEFORE Phase 1b]` gate present, ordering enforced |
| C-05 | PASS | Because block schema `Citation (Phase N, F[N]-seq)` + Confidence Rationale requires FID citations |

**Essential subtotal: 60.0 / 60.0**

### Recommended (C-06–C-08)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | FINDING REGISTER header, titled phase sections, Phase 5 split into four sub-tables |
| C-07 | PASS | `Counter-evidence:` sub-table with `Counter-Evidence \| Qualifying FID \| Recommended Next Step \| Condition` |
| C-08 | PASS | `Hypothesis resolution:` sub-table with `Status (CONFIRMED / REFUTED / INCONCLUSIVE)` |

**Recommended subtotal: 30.0 / 30.0**

### Aspirational (C-09–C-38)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | `Confidence Rationale (cite FIDs — not label alone)` column header in recommendation schema |
| C-10 | PASS | FINDING REGISTER pre-seeded; all FIDs committed before evidence phases |
| C-11 | PASS | `Citation (Phase N, F[N]-seq)` column header encodes hybrid-key format |
| C-12 | PASS | Phase 3 has `Fit Score (1-10)` column |
| C-13 | PASS | Phase 0 schema has `Prior Confidence` and `Expected Result (Phase 0)` before Phase 1 gate |
| C-14 | PASS | All phase headers carry `[COMPLETE BEFORE PHASE N]` gate annotations |
| C-15 | PASS | Phase 2 has `Severity (R/Y/G)` traffic-light column |
| C-16 | PASS | FINDING REGISTER at document top under `[PRE-SEED BEFORE PHASE 0]` gate |
| C-17 | PASS | Because block schema names exactly 6 rows: Phase 0/PRIOR through Phase 4/WEB EVIDENCE |
| C-18 | PASS | Recommendation record: `FID \| Recommendation \| Confidence (H=80%+...) \| Confidence Rationale (cite FIDs...)` |
| C-19 | PASS | Counter-evidence: `Counter-Evidence \| Qualifying FID \| Recommended Next Step \| Condition` |
| C-20 | PASS | All phase headers carry gate annotations |
| C-21 | PASS | Phase 1a header: `[COMPLETE BEFORE Phase 1b]` distinct from `[COMPLETE BEFORE PHASE 2]` |
| C-22 | PASS | `Citation (Phase N, F[N]-seq)` encoded in Because block column header |
| C-23 | PASS | All tables use domain-specific column names throughout |
| C-24 | PASS | Because block schema rows separately enumerate `Phase 1a / INERTIA` and `Phase 1b / RIVALS` |
| C-25 | PASS | Because block schema: `Phase \| Label \| Citation (Phase N, F[N]-seq) \| Claim` — exactly 4 columns |
| C-26 | PASS | Phase 1b table has `Response Strategy` column; Phase 1b FID labels include "with response strategy" |
| C-27 | PASS | C-01–C-26 all verifiable from column headers, gate annotations, table structure, register labels |
| C-28 | PASS | Phase 0 schema: `Expected Result (Phase 0)` and `Actual Outcome (Phase 5)` with temporal slots in column names |
| C-29 | PASS | Phase 1a header: `[INERTIA IS THE PRIMARY COMPETITOR]`; FINDING REGISTER F1a-01: `primary competitor: YES` |
| C-30 | PASS | Four bold-labeled Phase 5 sub-tables: **Hypothesis resolution:** **Recommendation record:** **Counter-evidence:** **Counter Block:** |
| C-31 | PASS | Phase 1a register: `FID \| Finding Summary \| Primary Competitor \| Switching Cost` — 4-column extended schema |
| C-32 | PASS | **Counter Block:** sub-table: `FID \| Counter Claim \| Rebuttal` — distinct from Counter-evidence |
| C-33 | PASS | `Confidence (H=80%+ / M=50-79% / L<50%)` in column headers |
| C-34 | PASS | Confidence calibration encoded in evidence entry schema in SCHEMA PREAMBLE before Phase 0 |
| C-35 | PASS | Phase 5 hypothesis resolution table has `Prior Confidence` column with copy-from-Phase-0 directive |
| C-36 | PASS | All phases carry closure directives: "Close FINDING REGISTER Phase N rows — fill [column names]" |
| C-37 | PASS | Phase 5 hypothesis resolution schema defined in SCHEMA PREAMBLE; Phase 5 header carries `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]` — fill-forward at phase boundary level (strongest location) |
| C-38 | PASS | Prose column naming present in all phase closures: Phase 0 names "Finding Summary"; Phase 1a names "Finding Summary, Primary Competitor flag, and Switching Cost"; Phase 1b names "Finding Summary with 'with response strategy'"; etc. Columns named throughout — prose form rather than bracket notation |

**Aspirational subtotal: 15.0 / 15.0**

### V-01 Total: **105.0 / 105.0**

---

## V-02 — C-38 bracket notation column enumeration

### Essential (C-01–C-05)

All essential criteria: PASS (same structural basis as V-01)

**Essential subtotal: 60.0 / 60.0**

### Recommended (C-06–C-08)

All recommended criteria: PASS

**Recommended subtotal: 30.0 / 30.0**

### Aspirational (C-09–C-38)

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-36 | PASS | Same structural basis as V-01; all preamble schemas, register, gate annotations present |
| C-37 | PASS | Phase 5 hypothesis resolution schema defined in SCHEMA PREAMBLE with description "pre-committed here so the schema is architecturally visible before any evidence runs"; Phase 5 body directive: "Fill the Phase 5 hypothesis resolution schema from the Schema Preamble" — body-level fill-forward satisfies criterion |
| C-38 | PASS | Bracket notation `[columns: FID, Finding Summary, Phase]` / `[columns: FID, Finding Summary, Primary Competitor, Switching Cost]` / `[columns: FID, Finding Summary, Phase, Note (include "with response strategy" per FID)]` across all phase closures — machine-verifiable column enumeration, strongest C-38 encoding |

**Aspirational subtotal: 15.0 / 15.0**

### V-02 Total: **105.0 / 105.0**

---

## V-03 — Documentation voice (C-37/C-38 as specification)

### Essential (C-01–C-05)

All essential criteria: PASS

**Essential subtotal: 60.0 / 60.0**

### Recommended (C-06–C-08)

All recommended criteria: PASS

**Recommended subtotal: 30.0 / 30.0**

### Aspirational (C-09–C-38)

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-36 | PASS | Preamble schemas, register, gate annotations all structurally present; documentation voice does not affect column-header verifiability |
| C-27 | PASS | C-01–C-26 all verifiable from structural elements; documentation-voice closure notes relate to C-36 (aspirational, outside C-27 scope) — C-27 scope unaffected |
| C-37 | PASS | Phase 5 hypothesis resolution schema defined in SCHEMA PREAMBLE ("pre-committed in this preamble"); Phase 5 body: "The Phase 5 hypothesis resolution sub-table uses the schema defined in the Schema Preamble" — documentation voice fill-forward satisfies explicit reference requirement |
| C-38 | PASS | Phase 1a closure names "Finding Summary, Primary Competitor flag, and Switching Cost"; other closures name "Finding Summary" and relevant fields in prose — columns named throughout, consistent with prose baseline |

**Aspirational subtotal: 15.0 / 15.0**

### V-03 Total: **105.0 / 105.0**

---

## V-04 — Schema architecture overview + bracket notation

### Essential (C-01–C-05)

All essential criteria: PASS

**Essential subtotal: 60.0 / 60.0**

### Recommended (C-06–C-08)

All recommended criteria: PASS

**Recommended subtotal: 30.0 / 30.0**

### Aspirational (C-09–C-38)

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-36 | PASS | All prior structural elements present; schema architecture table adds an index layer |
| C-37 | PASS | Schema Architecture table at SCHEMA PREAMBLE top explicitly lists "Phase 5 hypothesis resolution schema — Used in: Phase 5 hypothesis resolution sub-table"; preamble carries full schema definition; Phase 5 body: "Fill the Phase 5 hypothesis resolution schema from the Schema Preamble (see Schema Architecture table above)" — dual-path C-37 encoding: architecture index + body fill-forward |
| C-38 | PASS | Bracket notation `[columns: ...]` across all six phase closure points — same quality as V-02 |

**Aspirational subtotal: 15.0 / 15.0**

### V-04 Total: **105.0 / 105.0**

---

## V-05 — Full integration (all axes combined)

### Essential (C-01–C-05)

All essential criteria: PASS

**Essential subtotal: 60.0 / 60.0**

### Recommended (C-06–C-08)

All recommended criteria: PASS

**Recommended subtotal: 30.0 / 30.0**

### Aspirational (C-09–C-38)

| ID | Result | Evidence |
|----|--------|----------|
| C-09–C-36 | PASS | All prior structural elements present |
| C-37 | PASS | **Triple-path encoding**: (1) Schema Architecture table lists "Phase 5 hypothesis resolution schema — Used in: Phase 5 hypothesis resolution sub-table" at document index level; (2) Phase 5 header carries `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]` at phase boundary; (3) Phase 5 body: "Fill the Phase 5 hypothesis resolution schema from the Schema Preamble (see Schema Architecture table above)" — three independent structural verification paths, no single path is load-bearing |
| C-38 | PASS | Bracket notation `[columns: ...]` across all six phase closure points — uniform, machine-verifiable, highest-quality C-38 encoding |

**Aspirational subtotal: 15.0 / 15.0**

### V-05 Total: **105.0 / 105.0**

---

## Composite Summary

| Variation | Essential | Recommended | Aspirational | **Total** | All-Essential |
|-----------|-----------|-------------|--------------|-----------|---------------|
| V-01 | 60.0 | 30.0 | 15.0 | **105.0** | YES |
| V-02 | 60.0 | 30.0 | 15.0 | **105.0** | YES |
| V-03 | 60.0 | 30.0 | 15.0 | **105.0** | YES |
| V-04 | 60.0 | 30.0 | 15.0 | **105.0** | YES |
| V-05 | 60.0 | 30.0 | 15.0 | **105.0** | YES |

---

## Ranking by Signal Quality (all tied at 105.0)

| Rank | Var | C-37 signal strength | C-38 signal strength | Net advantage |
|------|-----|---------------------|---------------------|---------------|
| 1 | **V-05** | Triple-path: architecture index + header annotation + body directive | Bracket notation across all phases | Maximum structural redundancy — C-37 verifiable from any one of three independent paths |
| 2 | **V-04** | Dual-path: architecture index + body directive | Bracket notation | Architecture table adds pre-preamble verifiability; no header annotation |
| 3 | **V-01** | Header annotation fires at phase boundary | Prose naming (baseline) | Strongest single-path C-37 location; C-38 weakest of passing variations |
| 4 | **V-02** | Body directive | Bracket notation | Strongest single-path C-38 encoding; C-37 standard body form |
| 5 | **V-03** | Documentation voice body directive | Documentation voice prose naming | Structurally equivalent; lowest signal clarity of passing set |

---

## Excellence Signals from V-05

**Signal 1 — Schema architecture index table as pre-preamble C-37 amplifier**

The schema architecture table placed at the top of the SCHEMA PREAMBLE creates a document-level registry of all five schemas with their propagation paths:

```
| Schema | Defined here | Used in |
| Phase 5 hypothesis resolution schema | Yes | Phase 5 hypothesis resolution sub-table |
```

This makes C-37 verifiable from the document index before any schema definition body is read. Unlike a preamble-body-only definition (C-37 baseline), the index table separates the fact of schema existence from the schema content itself — a reviewer can confirm the fill-forward relationship without reading Phase 5 at all.

**Signal 2 — Triple-path criterion encoding for C-37**

V-05 encodes C-37 via three independent structural paths: (1) architecture index table, (2) Phase 5 header annotation `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]`, (3) Phase 5 body fill-forward reference. No single path is load-bearing. If any one path is missed by an executing agent, two others remain. This is the first appearance of three-path redundancy for a single criterion.

**Signal 3 — No new extractable criterion**

All structural novelties (architecture index, header annotation, bracket notation) satisfy C-37 and C-38 at PASS level across all five variations, including in their weaker forms. No pattern in R15 fails to satisfy any rubric criterion — the variation space is maximally saturated at 105.0 for all five. R15 exhausts the variation axes for C-37/C-38 without revealing new structural gaps. The v15 rubric should look outward to schema interactions not yet captured (e.g., schema architecture table as its own extractable criterion C-39 if triple-path encoding is judged separately from C-37 fill-forward).

---

```json
{"top_score": 105.0, "all_essential_pass": true, "new_patterns": ["Schema architecture index table placed before schema definitions makes fill-forward relationship verifiable from document index alone — three-path C-37 encoding: index + header annotation + body directive"]}
```
