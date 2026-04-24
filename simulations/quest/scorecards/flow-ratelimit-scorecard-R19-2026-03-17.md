## flow-ratelimit — Round 19 Scoring

---

### Essential Criteria (60 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Rate Limit Tier Distinction | PASS | PASS | PASS | PASS | PASS |
| C-02 | No Single-Category Collapsing | PASS | PASS | PASS | PASS | PASS |
| C-03 | Observable UX Per Throttle Tier | PASS | PASS | PASS | PASS | PASS |
| C-04 | Unprotected Burst Path Identification | PASS | PASS | PASS | PASS | PASS |
| C-05 | Retry-After Handling Gap Check | PASS | PASS | PASS | PASS | PASS |

**Evidence (shared):** Role 3 gate requires at least one STRUCTURAL burst path with Finding IDs. Role 4 scope-distinction check prevents tier-variant collapsing. Role 5 SCHEMA-B template enforces four-field UX per tier. Role 8c SCHEMA-M one-row-per-Finding-ID (BP-xx + RH-xx) captures retry gaps.

All essential: **5/5 → 60 pts** across all variations.

---

### Recommended Criteria (30 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Cascading Throttle Failure Scenario | PASS | PASS | PASS | PASS | PASS |
| C-07 | Numeric Rate Limit Specificity | PASS | PASS | PASS | PASS | PASS |
| C-08 | Volume-to-Behavior Mapping | PASS | PASS | PASS | PASS | PASS |

**Evidence (shared):** Role 8a requires causal chain statement with explicit trigger mechanism. Role 4 requires concrete numeric threshold with source. Role 6 SCHEMA-V declares VOLUME RANGE / BASELINE BEHAVIOR / PROTECTED BEHAVIOR / Delta.

All recommended: **3/3 → 30 pts** across all variations.

---

### Aspirational Criteria (30 pts — 37 criteria, 0.8108 pts each)

#### Inherited Base (C-09 through C-42 — 34 criteria)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Per-bottleneck Mitigation Prescriptions | PASS | PASS | PASS | PASS | PASS |
| C-10 | Quantified Impact at Load Spike | PASS | PASS | PASS | PASS | PASS |
| C-11 | Burst Gap Classification (Structural vs. Incidental) | PASS | PASS | PASS | PASS | PASS |
| C-12 | Dual-state Volume Mapping | PASS | PASS | PASS | PASS | PASS |
| C-13 | Verdict-before-Evidence Structure | PASS | PASS | PASS | PASS | PASS |
| C-14 | Baseline-delta Mitigation | PASS | PASS | PASS | PASS | PASS |
| C-15 | Document-head Global Verdict | PASS | PASS | PASS | PASS | PASS |
| C-16 | Format Contract Preamble | PASS | PASS | PASS | PASS | PASS |
| C-17 | Cascading Section Gate Enforcement | PASS | PASS | PASS | PASS | PASS |
| C-18–C-35 | *(18 criteria from R4–R14)* | PASS×18 | PASS×18 | PASS×18 | PASS×18 | PASS×18 |
| C-36 | FNMI as Standalone Labeled Section | PASS | PASS | PASS | PASS | PASS |
| C-37 | FNMI Four-Field Single-Block Completeness | PASS | PASS | PASS | PASS | PASS |
| C-38 | Reconciler Compliance-Verification Framing | PASS | PASS | PASS | PASS | PASS |
| C-39 | Format Contract Scenario-Anchored Column Definitions | PASS | PASS | PASS | PASS | PASS |
| C-40 | Format Contract Per-Table-Type Schema Decomposition | PASS | PASS | PASS | PASS | PASS |
| C-41 | Format Contract Cross-Role ID Anchoring in Column Definitions | PASS | PASS | PASS | PASS | PASS |
| C-42 | Format Contract Role Governance Annotation | PASS | PASS | PASS | PASS | PASS |

**Evidence notes:**
- **C-15:** Role 1 Gate 1→2 "No analysis, inventory, or table has appeared yet." V-01's Role 1 adds explicit self-containment language: "a reader of only this block knows the core finding, the primary unprotected path, the system status, and the UX coverage scope." All variations enforce revision-currency via inline REVISED markers at gate boundaries, not deferred to the reconciler.
- **C-39:** V-01 BASELINE definition: "the connector API call volume directed at the burst-path source endpoint identified by Finding ID in Role 3 (BP-xx), measured at the point of burst onset...This definition refers to the specific connector endpoint and Finding ID produced in Role 3 — not a generic 'before' state." V-03/V-05 route through BURST PATH TABLE with SCHEMA-A BASELINE SOURCE column — the column name is scenario-specific. All self-contained within the Format Contract section.
- **C-41:** V-03 and V-05 route through the BURST PATH TABLE (a named prior-role artifact) rather than citing BP-xx directly. The BURST PATH TABLE contains the Finding IDs and is produced by Role 3; the Format Contract definition names the table and column by name. This satisfies artifact-falsifiability at definition level; the specific BP-xx is resolved via the table rather than hardcoded. PASS.

All inherited base: **34/34 PASS** across all variations.

---

#### New R19 Criteria (C-43 through C-45)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-43 | Schema Cell-Level ID Anchor | **PASS** | **PARTIAL** | **FAIL** | **PASS** | **PASS** |
| C-44 | Schema Production Registry | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| C-45 | BURST PATH TABLE as Authoritative Single-Source Anchor | **FAIL** | **FAIL** | **PASS** | **FAIL** | **PASS** |

**C-43 evidence per variation:**
- **V-01 PASS:** Format Contract declares SCHEMA-A CELL ANCHOR requirement ("every data cell...must open with 'BP-xx: [value]'"). Both violation classes explicitly defined and labeled: CELL ANCHOR (scan-time, missing prefix) vs. UNRESOLVED REFERENCE (cross-ref required, prefix present but no matching Finding ID in Role 3). Role 9 CHECK (e) e.1–e.3 audits both classes separately with distinct report labels. Gate 2→3 requires "SCHEMA-A CELL ANCHOR requirement and both violation class definitions present."
- **V-02 PARTIAL:** Role 7 instructions require "BP-xx prefix required" on BASELINE/PROTECTED/DERIVATION CHAIN cells. But: Format Contract SCHEMA-A entry declares no CELL ANCHOR requirement. Two violation classes are not defined anywhere. CHECK (e) is registry-only; no cell anchor audit exists. Enforces the prefix structurally but fails the violation-class distinction requirement.
- **V-03 FAIL:** Uses BURST PATH TABLE routing instead of BP-xx prefix pattern. Role 7 requires "BASELINE cell must state the BURST PATH TABLE row it draws from (e.g., 'BURST PATH TABLE / BP-01 / SCHEMA-A BASELINE SOURCE: [value]')." This satisfies C-45 cell routing but not C-43's explicit BP-xx: prefix requirement on every cell. No CELL ANCHOR or UNRESOLVED REFERENCE violation classes defined. No cell anchor audit in CHECK (e).
- **V-04 PASS:** Format Contract declares CELL ANCHOR requirement with both violation classes. CHECK (e) Plane 2 (e.4–e.6) audits CELL ANCHOR and UNRESOLVED REFERENCE separately.
- **V-05 PASS:** Full three-plane CHECK (e). Plane 3 (e.5–e.6) audits BP-xx prefix presence and cross-references against BURST PATH TABLE BP ID column. Violation class separation explicitly required in findings output ("A report that merges them as 'missing or invalid prefix' does not satisfy this requirement").

**C-44 evidence per variation:**
- **V-01 FAIL:** No Schema Production Registry. CHECK (e) audits only cell anchors.
- **V-02 PASS:** Schema Production Registry placed before all schema body entries. 4-row table (SCHEMA-A, SCHEMA-V, SCHEMA-M, SCHEMA-B) with PRODUCING ROLE(S) and GATE CONDITION columns. Registry completeness rule stated: "row count must equal producing role count; missing row = REGISTRY GAP violation." CHECK (e) e.1–e.3 audits row count, gate fill, and orphaned schemas. Per-entry annotations preserved and not replaced.
- **V-03 FAIL:** No Schema Production Registry.
- **V-04 PASS:** Schema Production Registry at Format Contract head with same 4-row structure as V-02. CHECK (e) Plane 1 (e.1–e.3) audits REGISTRY GAP, REGISTRY GATE GAP, and ORPHANED SCHEMA.
- **V-05 PASS:** Same registry as V-02/V-04 with explicit completeness rule in the registry block itself. CHECK (e) Plane 1 distinguishes REGISTRY GAP (producing role without registry entry) from ORPHANED SCHEMA (schema body entry without registry entry) — two distinct violation classes at the registry plane.

**C-45 evidence per variation:**
- **V-01 FAIL:** No BURST PATH TABLE. Format Contract BASELINE cites "Finding ID in Role 3 (BP-xx)" directly — satisfies C-41 but not C-45.
- **V-02 FAIL:** No BURST PATH TABLE.
- **V-03 PASS:** Role 3 produces BURST PATH TABLE with BP ID, ENDPOINT NAME, BURST TYPE, TRIGGER CONDITION, SCHEMA-A BASELINE SOURCE columns. Format Contract SCHEMA-A BASELINE routes through this table ("The BURST PATH TABLE is the authoritative source for this definition: BASELINE is not independently anchored to a Finding ID"). Bidirectionality enforced: forward (BASELINE definition names table and SCHEMA-A BASELINE SOURCE column), backward (column name "SCHEMA-A BASELINE SOURCE" identifies the schema it feeds). CHECK (e) e.1–e.4 audits table presence, backward traceability, forward traceability from Format Contract, and BASELINE cell routing at Roles 7/8a.
- **V-04 FAIL:** No BURST PATH TABLE. Role 3 is basic burst path audit without table.
- **V-05 PASS:** Role 3 produces BURST PATH TABLE identical structure to V-03. Format Contract BASELINE routes through it. Additional integration: cell-level BP-xx prefixes resolve to BURST PATH TABLE rows (each cell's BP-xx is verifiable against BURST PATH TABLE BP ID column). Format Contract adds SCHEMA-A BASELINE SOURCE VIOLATION as a named rejection clause ("BASELINE cell cites a Finding ID directly instead of routing through the BURST PATH TABLE"). CHECK (e) Plane 2 (e.4) audits full bidirectionality including cell routing.

---

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (30) | Composite | /120 |
|-----------|---------------|-----------------|------------------|-----------|------|
| V-01 | 60 | 30 | 35.0/37 × 30 = **28.38** | **118.38** | 98.7% |
| V-02 | 60 | 30 | 35.5/37 × 30 = **28.78** | **118.78** | 99.0% |
| V-03 | 60 | 30 | 35.0/37 × 30 = **28.38** | **118.38** | 98.7% |
| V-04 | 60 | 30 | 36.0/37 × 30 = **29.19** | **119.19** | 99.3% |
| V-05 | 60 | 30 | 37.0/37 × 30 = **30.00** | **120.00** | 100.0% |

*V-02 aspirational: 34 base PASS + 0.5 (C-43 PARTIAL) + 1 (C-44 PASS) + 0 (C-45 FAIL) = 35.5*

---

### Rankings

| Rank | Variation | Score | New R19 criteria passing |
|------|-----------|-------|--------------------------|
| 1 | **V-05** | 120.00 | C-43 + C-44 + C-45 (all three) |
| 2 | **V-04** | 119.19 | C-43 + C-44 |
| 3 | **V-02** | 118.78 | C-44 (+ C-43 PARTIAL) |
| 4 | **V-01** | 118.38 | C-43 only |
| 4 | **V-03** | 118.38 | C-45 only |

V-01 and V-03 tie. Within the tie: V-01 adds verification capability at cell level (each cell independently falsifiable); V-03 adds structural concentration of endpoint identity authority. Neither is stronger than the other at this tier.

---

### Excellence Signals from V-05

**Pattern 1 — Three-plane audit with named plane independence:**  
CHECK (e) splits into Plane 1 (registry), Plane 2 (BURST PATH TABLE bidirectionality), Plane 3 (cell anchor). Each plane auditable without the others. "Partial failure in one plane does not affect the others" is stated explicitly. When a document partially conforms, the audit names the specific traceability granularity that broke — schema-to-role (Plane 1), definition-to-table (Plane 2), or cell-to-artifact (Plane 3) — rather than emitting a single undifferentiated failure.

**Pattern 2 — Traceability stack closes all three granularities simultaneously:**  
Format Contract SCHEMA-A definition routes through BURST PATH TABLE (definition-level anchor). Each SCHEMA-A cell carries BP-xx prefix pointing to a BURST PATH TABLE row (cell-level anchor). The BURST PATH TABLE column is named for the schema it feeds (backward anchor). A reader can enter the traceability chain at any level — column definition, cell value, or table lookup — and traverse to the source artifact. Prior variations closed at most two of the three levels.

**Pattern 3 — SCHEMA-A BASELINE SOURCE VIOLATION as a named rejection clause:**  
V-05 adds a fifth rejection clause to SCHEMA-A in the Format Contract: "SCHEMA-A BASELINE SOURCE VIOLATION: BASELINE cell cites a Finding ID directly instead of routing through the BURST PATH TABLE." This makes the C-41/C-45 distinction structurally enforced in-document: a reader can identify at scan time whether a BASELINE cell is C-41-compliant but C-45-noncompliant (has a Finding ID but no table routing) vs. C-45-compliant (routes through BURST PATH TABLE). Without this clause, the distinction requires knowing which round introduced which requirement.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["three-plane CHECK (e) with named plane independence — partial failure names specific traceability granularity (schema-to-role, definition-to-table, cell-to-artifact) without conflating planes", "full traceability stack: BURST PATH TABLE anchors column definitions, BP-xx prefixes anchor cell values, SCHEMA-A BASELINE SOURCE column name anchors backward from table to schema — all three levels simultaneously verifiable", "SCHEMA-A BASELINE SOURCE VIOLATION as a named Format Contract rejection clause — structurally distinguishes C-41 compliance (direct Finding ID) from C-45 compliance (table routing) at scan time without requiring cross-round rubric knowledge"]}
```
