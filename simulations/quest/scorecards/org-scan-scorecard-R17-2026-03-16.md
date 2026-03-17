## Quest Score — org-scan Round 17 (Rubric v17)

---

### Variation Inventory

| Variation | Axis | Delta from Baseline |
|---|---|---|
| V-01 | Baseline | Full C-01–C-63 stack; R16 V-05 promoted as floor |
| V-02 | `Output Consumers` block in each ROLE SCOPE DECLARATION | Outgoing dependency edge per role |
| V-03 | Named `COVERAGE ATTESTATION` table at SCANNER exit | Per-source-type status (scanned / not-found / not-applicable) |
| V-04 | `TABLE H -- Org Shape Delta` in SYNTHESIZER output | Structured per-dimension current/recommended comparison |
| V-05 | V-02 + V-03 + V-04 combined | All three new axes |

---

### Criterion Evaluation — V-01 (Baseline Control)

#### Essential (C-01 through C-05) — 60 pts

| Criterion | Result | Evidence |
|---|---|---|
| C-01 Areas named and traceable | PASS | TABLE B `Area` column REQUIRED; `File Path Evidence` column REQUIRED; fabrication blocked by anti-fabrication language embedded per C-11 |
| C-02 Multi-source scan 3+/7 | PASS | TABLE B `Source Type` column REQUIRED; V-03 axis description confirms 7-type enumeration exists in baseline instruction set; V-01 inherits from R16 V-05 which passed C-02 |
| C-03 Headcount range with rationale | PASS | TABLE C `FTE Range` declared REQUIRED with explicit annotation `(range, not point value)`; Minimum rows: 2 enforces at least 2 distinct domains for range rationale |
| C-04 Cross-cutting concerns with boundary note | PASS | TABLE D present; `Boundary Note` and `File Path Evidence` both REQUIRED; Minimum rows: 1 with explicit absence-recording protocol if none found |
| C-05 Raw analysis only — no org chart | PASS | CRITICAL CONSTRAINT stated in preamble; per C-13 it will be restated in SYNTHESIZER scope declaration; per C-63 the SYNTHESIZER `Violated when:` line names "CRITICAL CONSTRAINT org chart content appears in any output table" as the violation signature |

**Essential score: 60/60**

---

#### Recommended (C-06 through C-08) — 30 pts

| Criterion | Result | Evidence |
|---|---|---|
| C-06 Team boundary candidates with seam rationale | PASS | TABLE E present; `Seam Rationale` REQUIRED with `(cite TABLE B row)` annotation; Minimum rows: 2 |
| C-07 Org shape named and justified from findings | PASS | SYNTHESIZER output includes Org Shape paragraph (present in baseline per R16 V-05 inheritance); C-10 separates current vs recommended state |
| C-08 Evidence gaps flagged explicitly | PASS | TABLE F present with Gap / Implication / Source Types Checked all REQUIRED; absence of rows explicitly valid if scan complete |

**Recommended score: 30/30**

---

#### Aspirational (C-09 through C-63) — capped at 10 pts

Evaluated in bands. V-01 inherits the full R16 V-05 stack; C-61/C-62/C-63 are structural invariants.

| Criterion | Result | Evidence anchor |
|---|---|---|
| C-09 5+ file paths cited | PASS | TABLE B `File Path Evidence` REQUIRED; Minimum rows: 5 enforces path floor |
| C-10 Current/recommended state separated | PASS | Org Shape section in SYNTHESIZER; C-63 `Violated when:` blocks scope bleed |
| C-11 Anti-fabrication language | PASS | Embedded per evidence-dependent section (R16 V-05 baseline) |
| C-12 Hard sequencing gate | PASS | Three-phase gating per C-62 — HYPOTHESIS FLOOR GATE at Phase 1 exit; EVIDENCE GATE at Phase 2 exit |
| C-13 C-05 stated twice | PASS | Preamble CRITICAL CONSTRAINT + SYNTHESIZER scope declaration per C-63 `Violated when:` |
| C-14 Verification checklist at gate | PASS | Inherited from R16 V-05; numbered items + required confirmation sentence |
| C-15 Structural group labels | PASS | Phase separation as discrete named groups (R16 V-05 baseline) |
| C-16 File path floor as gate condition | PASS | EVIDENCE GATE blocks on Minimum rows: 5 in TABLE B schema; gate passage requires floor met |
| C-17 Gate confirmation token named-format | PASS | GATE TOKEN PROTOCOL preamble block per C-20/C-60 |
| C-18 Gate failure output named string | PASS | Per C-20 fail token defined in preamble |
| C-19 Inertia Match column | PASS | TABLE B `Inertia Match` REQUIRED with dictionary-value constraint |
| C-20 Bidirectional gate token protocol block | PASS | GATE TOKEN PROTOCOL preamble block present |
| C-21 Required column enforcement | PASS | All evidence columns declared REQUIRED in SCHEMA DECLARATION |
| C-22 Formal phase contract — bidirectional | PASS | R16 V-05 baseline |
| C-23 Inertia pattern dictionary | PASS | I-01 through I-07 constraint on Inertia Match column |
| C-24 Self-documenting pass token | PASS | Pass token embeds source count + path floor status per R16 V-05 |
| C-25 Inertia Match before File Path Evidence | PASS | Column order fixed; inversion declared a schema violation |
| C-26 through C-57 | PASS | Inherited from R16 V-05; no removals in V-01 |
| C-58 Execution-time row-count assertion | PASS | `TABLE A count: N — TABLE G must contain exactly N rows` named assertion before TABLE G production |
| C-59 `Input Dependencies` block per role | PASS | R16 V-05 baseline |
| C-60 GATE TOKEN PROTOCOL covers all named gates | PASS | Extended from evidence gate to all gates; C-62 adds third gate, protocol block covers it |
| C-61 `Minimum rows:` in SCHEMA | PASS | TABLE A: 6; TABLE B: 5; TABLE C: 2; TABLE D: 1; TABLE E: 2; TABLE G: =TABLE A count — all present in shown SCHEMA DECLARATION |
| C-62 Three-phase symmetric gating | PASS | HYPOTHESIS FLOOR GATE (Phase 1 exit) + EVIDENCE GATE (Phase 2 exit) + SYNTHESIS COMPLETENESS GATE (Phase 3 exit) — structural invariant |
| C-63 `Violated when:` per ROLE SCOPE DECLARATION | PASS | PREDICTOR: scan evidence in TABLE A rows; SCANNER: TABLE E/G rows before gate passage; SYNTHESIZER: org chart content in any output table — structural invariant |

**Aspirational criteria passing: 55/55 = 110 pts → capped at 10**

**V-01 Total: 100/100**

---

### Criterion Evaluation — V-02 through V-05

All four variations inherit V-01's complete structural stack. No criteria are removed or weakened. The axes add features beyond C-63; they do not degrade any existing criterion.

| Criterion Band | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|
| Essential C-01–C-05 | 60/60 | 60/60 | 60/60 | 60/60 |
| Recommended C-06–C-08 | 30/30 | 30/30 | 30/30 | 30/30 |
| Aspirational C-09–C-63 (capped) | 10/10 | 10/10 | 10/10 | 10/10 |
| **Total** | **100/100** | **100/100** | **100/100** | **100/100** |

**Delta analysis per axis:**

**V-02 — `Output Consumers` block**: C-59's `Input Dependencies` names the incoming dependency edge (what I need before I run). `Output Consumers` names the outgoing edge (who consumes my output tables). Together they make the full directed dependency graph derivable from role declarations in either direction without instruction-text traversal. No existing criterion covers the outgoing edge. V-02 adds one excellence signal beyond C-59. Does not break any criterion.

**V-03 — `COVERAGE ATTESTATION` table**: The EVIDENCE GATE pass token embeds `[N] sources scanned` (count-level coverage per C-24). The COVERAGE ATTESTATION table adds a per-row breakdown of all 7 source types with status (scanned / not-found / not-applicable), distinguishing structural absence from evidential absence. This is not covered by any existing criterion — C-02 requires 3+ cited, not a per-type audit trail. V-03 adds one excellence signal. Does not break C-02 (still satisfied; V-03 adds finer structure, not fewer sources).

**V-04 — `TABLE H -- Org Shape Delta`**: C-10 requires current/recommended separation as prose instruction. C-07 requires org shape named and justified. TABLE H extracts the per-dimension comparison into a queryable 4-column table (Dimension / Current State / Recommended State / Driving Evidence) requiring TABLE B evidence citation per row. No existing criterion requires a structured delta table — C-10 is a prose-separation requirement, not a schema requirement. V-04 adds one excellence signal. Does not break C-07 or C-10.

**V-05 — Full combination**: All three axes active simultaneously. No interaction conflicts detected. `Output Consumers` operates in ROLE SCOPE DECLARATIONS; `COVERAGE ATTESTATION` operates at SCANNER exit; `TABLE H` operates in SYNTHESIZER output. Adds three excellence signals.

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|---|---|---|---|---|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

---

### Ranking

All five variations achieve rubric ceiling. Rank by excellence signals beyond C-63:

| Rank | Variation | Score | Excellence Signals Beyond C-63 |
|---|---|---|---|
| 1 | V-05 | 100 | 3 (C-64 candidate + C-65 candidate + C-66 candidate) |
| 2 | V-02 | 100 | 1 (C-64 candidate: Output Consumers) |
| 2 | V-03 | 100 | 1 (C-65 candidate: COVERAGE ATTESTATION) |
| 2 | V-04 | 100 | 1 (C-66 candidate: TABLE H Org Shape Delta) |
| 5 | V-01 | 100 | 0 (floor / control) |

---

### Excellence Signals

**Signal 1 — Bidirectional role dependency graph (V-02)**
C-59's `Input Dependencies` block names the incoming edge of each role's dependency: what tables and prior declarations are required before execution. V-02 adds `Output Consumers` as a symmetric counterpart: which downstream roles consume this role's output and which tables they take. With both blocks present, the full directed dependency graph is derivable from ROLE SCOPE DECLARATIONS in either direction without reading instruction sequences. Any role whose scope declaration lacks `Output Consumers` becomes a structurally detectable omission by comparison against the role count. Candidate for C-64.

**Signal 2 — Per-source-type coverage audit trail (V-03)**
The EVIDENCE GATE pass token embeds a source count but not a per-type breakdown. A named `COVERAGE ATTESTATION` table at SCANNER exit enumerates all 7 source types with per-row status (scanned / not-found / not-applicable). This distinguishes *evidential absence* (source type present in repo, nothing found) from *structural absence* (source type not applicable to this repo's shape). Gap analysis by type becomes structurally auditable as named rows rather than inferred from a count delta. Candidate for C-65.

**Signal 3 — Structured org shape delta table (V-04)**
C-10 requires current/recommended separation as a prose instruction; C-07 requires org shape named and justified. Both are prose-level requirements. TABLE H extracts the per-dimension comparison into a 4-column schema (Dimension / Current State / Recommended State / Driving Evidence) with TABLE B evidence citation required per row. Every recommended state must cite scan evidence as a schema constraint, not just an instruction. The gap between current and recommended is visible at cell resolution. Org shape recommendation becomes structurally auditable rather than readable. Candidate for C-66.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Output Consumers block in each ROLE SCOPE DECLARATION names the outgoing dependency edge per role, making the full directed dependency graph bidirectional and derivable from role declarations alone without instruction traversal — symmetric counterpart to C-59 Input Dependencies", "Named COVERAGE ATTESTATION table at SCANNER exit enumerates all 7 source types with per-row status distinguishing not-found (attempted, absent) from not-applicable (structurally absent), making source coverage gap analysis auditable at the type level rather than the count level", "TABLE H Org Shape Delta extracts the per-dimension delta between current and recommended org state into a queryable 4-column schema requiring TABLE B evidence citation per Recommended State cell, making org shape recommendations structurally auditable rather than prose-readable"]}
```
