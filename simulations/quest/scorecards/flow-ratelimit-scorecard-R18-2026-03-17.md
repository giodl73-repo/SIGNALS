---

## flow-ratelimit R18 — Score Results

**All five variations: 120/120** (34/34 aspirational criteria, all essential and recommended pass)

R18 was a clean sweep — every variation was designed to pass C-41 and C-42, and all five do. No variation shows regression on any of the 32 prior criteria.

### Rankings (all 120, differentiated by implementation depth)

| Rank | Variation | Key axis |
|------|-----------|----------|
| **1** | **V-05** | Three-plane enforcement + three-plane CHECK (e) + SCHEMA-V C-41 extension + UNRESOLVED REFERENCE violation class |
| **2** | **V-04** | Cell-level + Schema Registry simultaneously; orthogonal planes with combined CHECK (e) |
| **3** | **V-03** | BURST PATH TABLE as authoritative anchor; SCHEMA-V extension; bidirectional traceability |
| **4** | **V-01** | Cell-level SCHEMA-A CELL ANCHOR; scan-time detectable; seeds C-43 cleanly |
| **5** | **V-02** | Schema Production Registry with gate-linkage; seeds C-44 cleanly |

### New patterns from V-05
1. **Three-plane enforcement chain** — declaration / governance / cell planes independently auditable
2. **UNRESOLVED REFERENCE violation class** — format-compliant `BP-05:` prefix that has no BP-05 in Role 3 is a distinct violation from a missing prefix
3. **BURST PATH TABLE as single-source anchor** — traceability becomes a table lookup, not reader inference
4. **C-41 universality** — SCHEMA-V BASELINE BEHAVIOR referencing Role 3 tests whether artifact-falsifiability is a universal property of all BASELINE-type columns

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["three-plane enforcement chain (declaration+governance+cell) makes each artifact-traceability plane independently auditable without reading the other two", "UNRESOLVED REFERENCE violation class distinguishes format-compliant cell prefixes from semantically valid ones — a cell carrying BP-05 where no BP-05 exists in Role 3 is a different violation from a cell missing the prefix entirely", "BURST PATH TABLE as authoritative single-source anchor eliminates endpoint identity ambiguity across all downstream schema definitions — traceability becomes a table lookup rather than a reader inference", "C-41 universality extension: SCHEMA-V BASELINE BEHAVIOR referencing Role 3 Finding IDs tests whether artifact-falsifiability is a universal property of all BASELINE-type column definitions document-wide"]}
```

Scorecard written to `simulations/quest/scorecards/flow-ratelimit-scorecard-R18-2026-03-17.md`.
 STRUCTURAL/INCIDENTAL classification structurally enforced rather than prose-dependent. PASS all, stronger in V-03/V-05.
- **C-15** (Document-head Global Verdict): Role 1 before Role 2 in all variations. Gate 1→2 enforces no analysis until four claims written. PASS all.
- **C-17** (Cascading Section Gate Enforcement): All variations have explicit `Gate N→N+1:` language naming specific deliverables for every transition. V-02/V-04/V-05 also name gate conditions in the Schema Production Registry, strengthening C-17 evidence. PASS all.
- **C-36** (FNMI as Standalone Labeled Section): All have `### FORMAL NON-MODIFICATION INVARIANT — FNMI-R18` as its own section header between Role 8 and Role 9. PASS all.
- **C-37** (FNMI Four-Field Single-Block Completeness): All have (a)–(d) as individually labeled items in one contiguous block. PASS all.
- **C-38** (Reconciler Compliance-Verification Framing): All have `FNMI-R18: COMPLIANT / VIOLATION at [reference] — [description]` in Role 9 summary. PASS all.
- **C-39** (Format Contract Scenario-Anchored Column Definitions): All define BASELINE as "connector API call volume directed at the burst-path source endpoint... measured at burst onset... before mitigation" — scenario-named, self-contained. V-03/V-05 additionally reference the BURST PATH TABLE by name (additional anchoring, not a deferred-reference violation). PASS all.
- **C-40** (Format Contract Per-Table-Type Schema Decomposition): All declare SCHEMA-A, SCHEMA-V, SCHEMA-M, SCHEMA-B as separate named entries with their own column structures. PASS all.

**C-09 through C-40: PASS all five variations.**

---

### C-41 — Format Contract Cross-Role ID Anchoring in Column Definitions

Pass condition: BASELINE and PROTECTED definitions each reference at least one specific Finding ID produced by a named prior role, making the definition artifact-falsifiable.

| Variation | Evidence | Result |
|-----------|----------|--------|
| **V-01** | BASELINE: "identified by Finding ID in Role 3 (BP-xx)... This definition refers to the specific connector endpoint and Finding ID produced in Role 3 — not a generic 'before' state." PROTECTED: "for that Finding ID (BP-xx)" from Role 8c. Both definitions artifact-falsifiable via Role 3 BP-xx. Additionally adds cell-level `"BP-xx: [value]"` requirement on every SCHEMA-A cell — predicted C-43 candidate beyond C-41 scope. | **PASS** |
| **V-02** | BASELINE and PROTECTED use R17 V-01 column-definition baseline: "identified by Finding ID in Role 3 (BP-xx)" with explicit "This definition refers to the specific connector endpoint and Finding ID produced in Role 3 — not a generic 'before' state." Column-definition anchor only; no cell-level enforcement. Both definitions reference named prior roles. | **PASS** |
| **V-03** | BASELINE: "identified by Finding ID in Role 3 (BP-xx)... The 'BP-xx' refers to the primary burst-path Finding ID recorded in the BURST PATH TABLE produced in Role 3, column SCHEMA-A BASELINE SOURCE." Names specific artifact AND specific column — bidirectional traceability. PROTECTED references same BP-xx in context of Role 3's BURST PATH TABLE. SCHEMA-V BASELINE BEHAVIOR additionally references "primary Finding ID in Role 3's BURST PATH TABLE (BP-xx, column ENDPOINT NAME)" — extends C-41 pattern to a second schema. | **PASS** |
| **V-04** | V-01 column-level anchor + V-02 Schema Production Registry. BASELINE and PROTECTED carry "(BP-xx)" with Role 3 citation. Cell-level anchor requirement from V-01: each SCHEMA-A cell must open with resolved prefix. Two enforcement planes for C-41 simultaneously. CHECK (e) in Role 9 verifies cell anchors (e.4–e.6) including unresolved-reference check. | **PASS** |
| **V-05** | Full integration: column-level anchor references Role 3's BURST PATH TABLE by name and column (V-03 approach) + cell-level enforcement on every SCHEMA-A cell (V-01 approach) + SCHEMA-V BASELINE BEHAVIOR extension. Three-plane coverage: declaration plane (column definitions), governance plane (Schema Production Registry), cell plane (resolved BP-xx prefix per cell). Role 9 CHECK (e) audits all three planes with per-plane findings. | **PASS** |

---

### C-42 — Format Contract Role Governance Annotation

Pass condition: each named schema entry includes a role governance annotation identifying the specific role(s) that must produce schema-conformant tables of that type.

| Variation | Evidence | Result |
|-----------|----------|--------|
| **V-01** | Inline "Applies to:" on all four schemas: SCHEMA-A: "Role 7 quantified impact at load spike; Role 8a cascade failure analysis." SCHEMA-V: "Role 6 volume-to-behavior mapping." SCHEMA-M: "Role 8c per-finding mitigation prescriptions." SCHEMA-B: "Role 5 UX descriptions per throttle tier." All four schema entries name specific producing roles. | **PASS** |
| **V-02** | Schema Production Registry table at top of Format Contract: 4 rows mapping schema → producing role(s) → table type → gate condition. Plus inline "Applies to:" retained on each schema body with "(See Schema Production Registry for gate conditions.)" Registry completeness rule stated. Registry enables O(1) role governance lookup independently of reading schema body. Both annotation forms present. | **PASS** |
| **V-03** | Inline "Applies to:" on all four schemas (same as V-01). SCHEMA-A BASELINE definition additionally references "the BURST PATH TABLE produced in Role 3, column SCHEMA-A BASELINE SOURCE" — creates bidirectional link from Format Contract back to Role 3's named table, making the role assignment verifiable against Role 3's specific output artifact. | **PASS** |
| **V-04** | Schema Production Registry (V-02 structure) + inline "Applies to:" per schema with "(See Schema Production Registry for gate conditions and role assignments.)" Dual evidence: registry row count confirms coverage; inline annotation confirms per-schema role assignment. CHECK (e) in Role 9 audits registry completeness (e.1–e.3). | **PASS** |
| **V-05** | Schema Production Registry (V-02 structure) + inline "Applies to:" per schema + Role 9 three-plane CHECK (e) Plane 1 audits registry completeness: (e.1) registry has exactly four rows, (e.2) each producing role exists and produces a table, (e.3) each table's column headers match declared schema. Registry completeness rule: "every table-producing role must have a registry entry; missing row is a REGISTRY GAP violation, detectable by comparing registry row count against producing role count." Strongest C-42 enforcement: Role 9 verifies the registry is complete and accurate at evaluation time. | **PASS** |

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational 34/34 (30.000) | **Total** |
|-----------|---------------|-----------------|----------------------------|-----------|
| **V-01** | 60 | 30 | 30.000 | **120.000** |
| **V-02** | 60 | 30 | 30.000 | **120.000** |
| **V-03** | 60 | 30 | 30.000 | **120.000** |
| **V-04** | 60 | 30 | 30.000 | **120.000** |
| **V-05** | 60 | 30 | 30.000 | **120.000** |

---

## Ranking

All five variations pass C-41 and C-42 plus carry all 32 prior criteria intact. All score 120/120. Ranking reflects implementation depth, audit strength, and future-seeding value:

| Rank | Variation | Distinguishing factor |
|------|-----------|----------------------|
| 1 | **V-05** | Three-plane enforcement (declaration+governance+cell) simultaneously; three-plane CHECK (e) with per-plane findings; SCHEMA-V extension tests C-41 universality; UNRESOLVED REFERENCE violation class closes format-vs-semantic gap; seeds C-43, C-44, C-45 simultaneously |
| 2 | **V-04** | Two orthogonal enforcement planes (cell-level + Schema Production Registry); CHECK (e) audits both planes including unresolved-reference check (e.6); strongest single-document evidence for C-41+C-42 without lifecycle overhead; seeds C-43 and C-44 |
| 3 | **V-03** | BURST PATH TABLE makes Role 3 the authoritative anchor for all downstream BASELINE definitions (bidirectional traceability); SCHEMA-V extension tests C-41 universality independently of cell enforcement; SCHEMA-A SOURCE REFERENCE rejection clause closes deferred-reference gap; seeds C-45 in isolation |
| 4 | **V-01** | Cell-level enforcement makes every SCHEMA-A row independently verifiable without reading Format Contract; SCHEMA-A CELL ANCHOR rejection clause is scan-time detectable; simplest single-axis for C-43 isolation; seeds C-43 |
| 5 | **V-02** | Schema Production Registry is scan-time verifiable (count rows = producing role count); gate-linkage column makes production responsibility bidirectional; CHECK (e) registry audit adds runtime verification; cleanest single-axis for C-44 isolation; seeds C-44 |

---

## Excellence Signals from V-05

**1. Three-plane enforcement chain as a structural discipline**
Declaration plane (column definitions referencing Role 3's BURST PATH TABLE by name and column) + governance plane (Schema Production Registry mapping schema → role → gate) + cell plane (resolved BP-xx prefix on each SCHEMA-A cell). Each plane is independently auditable; a gap at any plane is detectable without reading the other two. Generalizable pattern: any artifact-traceability requirement should declare all three planes to close the format-compliance vs. semantic-compliance gap.

**2. UNRESOLVED REFERENCE as a new violation class**
CHECK (e) Plane 2 distinguishes between a cell that carries a Finding ID prefix in the correct format ("BP-01: ...") vs. a cell that carries a prefix that can't be resolved against Role 3's BURST PATH TABLE ("BP-05: ..." where BP-05 was never assigned in Role 3). UNRESOLVED REFERENCE is stronger than SCHEMA-A CELL ANCHOR: the former flags format-compliant cells whose referenced artifact doesn't exist; the latter only flags cells missing the prefix. This closes the gap between declaring a cell format (C-41) and enforcing that the declared format contains a valid reference (predicted C-43 candidate).

**3. BURST PATH TABLE as authoritative single-source anchor**
When Role 3 produces a formal table with ENDPOINT NAME and SCHEMA-A BASELINE SOURCE columns, both the Format Contract column definitions and downstream SCHEMA-A cells reference a single named table. Removes endpoint identity ambiguity: "is this the right endpoint" becomes a table lookup against a named column, not a reader inference from prose. Makes the traceability chain falsifiable end-to-end: Format Contract → BURST PATH TABLE → SCHEMA-A cell.

**4. C-41 universality extension to SCHEMA-V**
SCHEMA-V BASELINE BEHAVIOR definition referencing Role 3's BURST PATH TABLE tests whether Finding ID anchoring should be a universal property of all BASELINE-type column definitions (not just SCHEMA-A's BASELINE column). If the pattern holds under scoring, C-41 can be extended as a document-wide requirement: any column definition named BASELINE (or BASELINE-type) in any schema must reference a specific upstream Finding ID.

**5. Per-plane findings format in Role 9**
"Three-Plane Audit: Plane 1 (registry): N/N rows pass...; Plane 2 (cell anchors): N cells pass...; Plane 3 (SCHEMA-V source): N rows pass..." makes gap localization O(1): reader sees which plane has a violation without re-reading the full analysis. Parallels C-38's FNMI compliance-verdict framing applied to the multi-plane audit structure.

---

## JSON

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["three-plane enforcement chain (declaration+governance+cell) makes each artifact-traceability plane independently auditable without reading the other two", "UNRESOLVED REFERENCE violation class distinguishes format-compliant cell prefixes from semantically valid ones — a cell carrying BP-05 where no BP-05 exists in Role 3 is a different violation from a cell missing the prefix entirely", "BURST PATH TABLE as authoritative single-source anchor eliminates endpoint identity ambiguity across all downstream schema definitions — traceability becomes a table lookup rather than a reader inference", "C-41 universality extension: SCHEMA-V BASELINE BEHAVIOR referencing Role 3 Finding IDs tests whether artifact-falsifiability is a universal property of all BASELINE-type column definitions document-wide"]}
```
