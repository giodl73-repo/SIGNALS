## org-scan Round 18 — Scorecard

---

### Scoring Architecture

| Band | Points | Max |
|---|---|---|
| Essential (C-01 – C-05) | 12 pts × 5 | 60 |
| Recommended (C-06 – C-08) | 10 pts × 3 | 30 |
| Aspirational (2 pts each, 58 criteria) | capped | 10 |
| **Total** | | **100** |

Aspirational cap threshold: 5 criteria met = 10 pts. All variations carry 40+ qualifying aspirational criteria — cap is trivially cleared.

---

### V-01 — Baseline R18 (Control)

**Essential** — 60/60

| Criterion | Result | Evidence |
|---|---|---|
| C-01 | PASS | TABLE B Area column + anti-fabrication rule blocks invented areas |
| C-02 | PASS | "Scan at least 3 of 7 source types" in Phase 2 |
| C-03 | PASS | TABLE C FTE Range REQUIRED as range, not point value |
| C-04 | PASS | TABLE D Concern + Boundary Note REQUIRED |
| C-05 | PASS | Critical constraint preamble + SYNTHESIZER CONSTRAINT RESTATEMENT |

**Recommended** — 30/30

| Criterion | Result | Evidence |
|---|---|---|
| C-06 | PASS | TABLE E Seam Rationale citing TABLE B row numbers |
| C-07 | PASS | Org Shape section separates CURRENT STATE / RECOMMENDED STATE |
| C-08 | PASS | TABLE F gaps tracked; not-found attestation rows propagate |

**Aspirational** — 10/10 (cap cleared)

Key passes: C-09 through C-66 all fire. Notable highlights:
- C-13 PASS: Critical constraint stated in preamble + SYNTHESIZER restatement
- C-14 PASS: Gate checklist 5 numbered items + named token sentence
- C-15 PASS: GROUP A / GROUP B / GROUP C structural labels
- C-20 PASS: GATE TOKEN PROTOCOL preamble block with all three gates
- C-22 **PASS**: Explicit bilateral contract language — "This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name the same contract."
- C-60 PASS: Protocol block covers all three gates
- C-64 PASS: Output Consumers blocks in PREDICTOR, SCANNER, SYNTHESIZER
- C-65 PASS: COVERAGE ATTESTATION at SCANNER exit, 7 rows, constrained status
- C-66 PASS: TABLE H -- Org Shape Delta with TABLE B citations

**V-01 Score: 100/100**

---

### V-02 — Table-payload Output Consumers

**Essential** — 60/60 (identical to V-01)
**Recommended** — 30/30 (identical to V-01)

**Aspirational** — 10/10 (cap cleared)

Key changes from V-01:

| Criterion | Result | Evidence |
|---|---|---|
| C-22 | PARTIAL | SCANNER/GATEKEEPER boundary omits explicit "postcondition of Phase 2 AND precondition of Phase 3" bilateral naming; both sides implied by checklist item 1 + SYNTHESIZER entry condition but not co-declared |
| C-64 | **PASS+** | Output Consumers entries exceed C-64 minimum: PREDICTOR entry names "purpose: cross-references each TABLE B finding row against the TABLE A row for its matching pattern ID to populate the Hypothesis Held column; without TABLE A, SCANNER cannot anchor..."; SCANNER entries enumerate TABLE B→TABLE E/G/H citation purposes, TABLE C→Headcount Range derivation, TABLE D→cross-cutting evidence, COVERAGE ATTESTATION→TABLE F gap propagation; SYNTHESIZER entries name org-build consumption purpose per table — this is a transport manifest per edge, not just adjacency |

C-22 PARTIAL does not reduce total: cap is cleared by 30+ other passing aspirational criteria.

**New structural signal beyond C-64**: Each Output Consumers entry carries the consuming role, the specific tables consumed, AND the analytical purpose each table serves in that consuming phase — creating a directed dependency graph with full transport manifests derivable from role declarations alone.

**V-02 Score: 100/100**

---

### V-03 — COVERAGE ATTESTATION Schema-Declared

**Essential** — 60/60
**Recommended** — 30/30

**Aspirational** — 10/10 (cap cleared)

Key changes from V-01:

| Criterion | Result | Evidence |
|---|---|---|
| C-22 | PARTIAL | Same as V-02 — bilateral language absent from SCANNER/GATEKEEPER boundary |
| C-65 | **PASS+** | COVERAGE ATTESTATION elevated from a SCANNER-phase output instruction to a first-class SCHEMA DECLARATION entry: full column definitions (Source Type REQUIRED enumerated, Status REQUIRED constrained, Notes REQUIRED one-sentence minimum), Minimum rows: 7 annotation, "A COVERAGE ATTESTATION with fewer than 7 rows is a schema violation detectable by comparison against this Minimum rows annotation without reading the SCANNER phase body" — extends C-61's Minimum rows protocol |
| Gate checklist | PASS+ | Item 6 added: "COVERAGE ATTESTATION has exactly 7 rows (schema minimum rows requirement)" — attestation row floor is now a gateable condition, not only an output instruction; gate checklist grows from 5 to 6 items |

SCANNER Phase 2 instruction references "all 7 source types declared in COVERAGE ATTESTATION schema" — instructions defer to schema for the source-type enumeration (schema-first reference pattern).

**New structural signal beyond C-65**: COVERAGE ATTESTATION schema-declared with Minimum rows: 7 makes row-floor violations detectable from SCHEMA DECLARATION alone without reading SCANNER phase instructions; gate checklist enforcement makes this a gate-blocking condition rather than a soft output obligation.

**V-03 Score: 100/100**

---

### V-04 — TABLE H Dynamic Floor + Bridge Rule

**Essential** — 60/60
**Recommended** — 30/30

**Aspirational** — 10/10 (cap cleared)

Key changes from V-01:

| Criterion | Result | Evidence |
|---|---|---|
| C-22 | PARTIAL | Bilateral language absent; both phases implied but not co-named |
| C-66 | **PASS+** | TABLE H Minimum rows tightened from "1" to "N (must equal TABLE E count — every team boundary candidate maps to at least one org shape dimension; a TABLE H with fewer rows than TABLE E is a schema violation detectable by comparing the two tables' row counts without reading the SYNTHESIZER instructions)" |
| Bridge rule | NEW | TABLE F receives named bridge rule in SCHEMA DECLARATION: "any TABLE H row where Recommended State != Current State must produce a TABLE F entry" with prescribed Gap, Implication, Source Types Checked templates — recommendations are not orphaned in TABLE H but propagate to tracked gaps automatically |
| SYNTHESIS gate | PASS+ | Gate extended to 6 items: adds "TABLE H row count >= TABLE E row count" (item 4) and "Each TABLE H row with Recommended State != Current State has a TABLE F bridge entry" (item 5); PASS token extended to include "[N] TABLE E rows, [N] TABLE H rows, TABLE H bridge rule applied" |
| Execution-time assertion | PASS+ | Second execution-time assertion added before TABLE H production: "TABLE E count: [N] -- TABLE H must contain at least [N] rows" — extends C-58's execution-time assertion pattern to the TABLE E→TABLE H cross-table floor |

**New structural signals beyond C-66**:
1. Cross-table dynamic floor — TABLE H Minimum rows = TABLE E count: floor is not a static constant but an execution-time cross-table relationship, making the constraint structurally verifiable by comparing two table row counts.
2. Recommendation-to-gap bridge rule — TABLE H delta rows automatically produce TABLE F entries at schema level: org shape recommendations are tracked as pending gaps rather than orphaned in TABLE H until acted upon.

**V-04 Score: 100/100**

---

### V-05 — Full Combination + Schema-First Register

**Essential** — 60/60
**Recommended** — 30/30

**Aspirational** — 10/10 (cap cleared)

This variation combines V-02 + V-03 + V-04 axes and adds a fourth axis: the schema-first register.

| Criterion | Result | Evidence |
|---|---|---|
| C-22 | PARTIAL | Bilateral language absent from SCANNER/GATEKEEPER boundary section (same pattern as V-02 through V-04) |
| C-64 | PASS+ | Table-payload Output Consumers (V-02 axis): PREDICTOR names TABLE A purpose per consumer; SCANNER names TABLE B, C, D, COVERAGE ATTESTATION purposes in separate consumer entries; SYNTHESIZER names TABLE G (confidence levels for org-build) and TABLE H (dimensional design targets for org-build) purpose per table |
| C-65 | PASS+ | COVERAGE ATTESTATION schema-declared (V-03 axis): in SCHEMA DECLARATION with column definitions, REQUIRED annotations, Minimum rows: 7, violation detectability note; gate checklist item 6 enforces row floor |
| C-66 | PASS+ | TABLE H Minimum rows = TABLE E count + bridge rule in SCHEMA DECLARATION (V-04 axis) |
| Schema-first register | NEW | SCHEMA DECLARATION header explicitly declares: "All structural obligations -- table shapes, minimum rows, column requirements, cross-table bridge rules, and coverage audit requirements -- are declared here before Phase 1 begins. No structural property of this skill requires reading phase instructions to discover; the schema is the single authoritative source." This elevates schema from a type contract to a type + quantitative + bridge contract — a reader can determine ALL structural obligations from one location |
| SYNTHESIS gate | PASS+ | Extended 6-item checklist + PASS token includes TABLE E/TABLE H counts and bridge rule status |
| Coverage attestation + gate | PASS+ | Gate checklist item 6 (from V-03) present in V-05 |
| Bridge rule | PASS+ | TABLE F bridge rule declared in SCHEMA DECLARATION (from V-04), not only in phase instructions — making it a schema-level obligation |

**Structural coherence check** — do the three axes interact constructively or create tension?

- V-02 (table-payload consumers) × V-03 (schema-declared attestation): SCANNER's Output Consumers entry for COVERAGE ATTESTATION now reads "purpose: not-found rows are TABLE F bridge candidates per the TABLE F bridge rule in SCHEMA DECLARATION; the attestation makes source-type gap analysis auditable at row resolution, not only at count level" — the consumer entry cross-references the schema declaration. Constructive.
- V-03 × V-04 (bridge rule): SCANNER instruction defers to schema: "Output COVERAGE ATTESTATION per SCHEMA DECLARATION (exactly 7 rows)." Bridge rule is in schema. Constructive — schema is the reference point for both.
- V-02 × V-04: SYNTHESIZER Output Consumers entries describe what org-build does with TABLE G and TABLE H with purpose annotations that reference the Recommended State cells as design targets. Constructive.

No structural tension detected. The schema-first register emerges as a coherent consequence of combining all three axes.

**V-05 Score: 100/100**

---

### Rankings

| Rank | Variation | Score | Distinguishing Property |
|---|---|---|---|
| 1 | V-05 | 100/100 | All three axes + schema-first register; 4 new C-67+ signals |
| 2 | V-04 | 100/100 | Dynamic floor + bridge rule; SYNTHESIS gate extended |
| 3 | V-03 | 100/100 | Schema-declared attestation; attestation row floor gateable |
| 4 | V-02 | 100/100 | Table-payload dependency manifests per edge |
| 5 | V-01 | 100/100 | Baseline; only variation with explicit C-22 bilateral language |

**Note on V-01 C-22 advantage**: V-01 is the only variation retaining the explicit "postcondition of Phase 2 and the precondition of Phase 3" bilateral contract naming. V-02 through V-05 omit this in condensing the boundary section. This is a regression from V-01 in V-02-V-05 — a future variation should restore it.

---

### Excellence Signals from V-05 (C-67+ Candidates)

**Signal 1 — Table-payload dependency manifest** (extends C-64)
Each Output Consumers entry names the consuming role, the specific tables consumed, AND the analytical purpose each table serves in that consuming phase. Role-level edge (C-64) names adjacency; table-payload manifest names the transport contract per edge. A reader can determine not just that Role A feeds Role B, but what Role B does with each table it receives — the dependency graph is semantically annotated, not just topologically enumerated.

**Signal 2 — Schema-declared coverage audit with gateable floor** (extends C-65)
COVERAGE ATTESTATION elevated to SCHEMA DECLARATION with column definitions, REQUIRED annotations, and Minimum rows: 7. Row-floor violations are detectable from schema alone without reading SCANNER phase instructions. Gate checklist item 6 makes the row floor a gate-blocking condition rather than an output expectation.

**Signal 3 — Cross-table dynamic floor** (extends C-66)
TABLE H Minimum rows = TABLE E count: floor is not a static constant but an execution-time cross-table relationship. Every team boundary candidate (TABLE E) maps to at least one org shape dimension (TABLE H). A TABLE H with fewer rows than TABLE E is a structurally detectable schema violation by row-count comparison alone.

**Signal 4 — Recommendation-to-gap bridge rule** (extends C-66)
Any TABLE H row where Recommended State ≠ Current State must produce a TABLE F entry with prescribed templates. Org shape recommendations are not orphaned in TABLE H — they propagate to TABLE F as tracked pending gaps. The loop between recommendation and evidence-gap tracking closes at schema level, making unacted-upon recommendations structurally visible as TABLE F rows.

**Signal 5 — Schema-first register**
Explicit SCHEMA DECLARATION header declares the schema is the single authoritative source for all structural obligations: table shapes, minimum rows, column requirements, cross-table bridge rules, AND coverage audit requirements. No structural property requires reading phase instructions to discover. Schema graduates from type contract to type + quantitative + bridge contract.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["table-payload dependency manifest per Output Consumers edge names consuming role, tables consumed, and analytical purpose — dependency graph carries transport manifest not just adjacency", "COVERAGE ATTESTATION schema-declared with Minimum rows: 7 makes row-floor violations detectable from schema without reading SCANNER phase body; gate checklist item enforces as blocking condition", "cross-table dynamic floor TABLE H Minimum rows = TABLE E count creates execution-time inter-table constraint verifiable by row-count comparison alone", "TABLE H / TABLE F bridge rule propagates each delta row into a tracked TABLE F gap entry — recommendations are structurally visible as pending gaps not orphaned states", "schema-first register explicit declaration that schema is single authoritative source for shapes, floors, bridge rules, and coverage audit — schema becomes type + quantitative + bridge contract"]}
```
