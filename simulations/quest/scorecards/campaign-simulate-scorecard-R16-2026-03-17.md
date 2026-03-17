# campaign-simulate — Round 16 Scoring (Rubric v14)

## Scoring Summary

| Rank | Var | Score | C-50 | C-51 | C-52 | Aspirational |
|------|-----|-------|------|------|------|-------------|
| 1 | **V-05** | **100.0** | PASS | PASS | PASS | 44/44 |
| 2 | V-04 | 99.8 | PASS | FAIL | PASS | 43/44 |
| 3 | V-01 | 99.5 | PASS | FAIL | FAIL | 42/44 |
| 3 | V-02 | 99.5 | FAIL | PASS | FAIL | 42/44 |
| 3 | V-03 | 99.5 | FAIL | FAIL | PASS | 42/44 |

**All variations**: essential + recommended criteria PASS → base = 90. C-09 through C-49 (41 inherited criteria) all PASS.

**Why V-05 is the sole 100.0:** All three R16 ceiling mechanisms operate on disjoint surfaces — checklist sub-claim 2 of axis 18 (C-50 scan table), pre-ECM standalone SEVERITY AXIOM block (C-51), checklist sub-claim 2 of axis 20 (C-52 audit table). Each is independently falsifiable without touching the other two.

**Why V-04 beats the single-mechanism variations:** Two disjoint surfaces (C-50 + C-52) with no interference — the column-scan enumeration table and the self-match audit table operate on different checklist sub-claims of different axes.

## Excellence Signals

1. **Table-schema-as-proof**: Both C-50 and C-52 convert assertions ("no narrative field read") into structural artifacts — a K-column table with no narrative column schema cannot silently include narrative context. The schema IS the proof.
2. **Axiom-first derivation**: The SEVERITY AXIOM block pre-states the ordering claim as a standalone named block; downstream checklist cites axiom text + one Status cell label only. No cross-column lookup required.
3. **Column-equality as verification primitive**: The `Match?` column in C-52's audit table makes F-ID equality violations visible by scan without reading Verb Source cell content. Generalizes to any self-referential F-NN constraint.

Scorecard written to `simulations/quest/scorecards/campaign-simulate-scorecard-R16-2026-03-17.md`.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["table-schema-as-proof: K-column table with no narrative column IS the scan-sufficiency proof; schema design excludes narrative read by construction", "axiom-first derivation: standalone named axiom block before governed artifact enables downstream compliance proof from axiom-text + cell-value alone with no cross-column lookup", "column-equality as verification primitive: audit table where column A == column B is the correctness check; Match? column makes violations visible by scan without reading cell content"]}
```
lumn scan table; verbatim declaration references table by name | **PASS** | SAD axis 21 present; sub-claim 2 table schema F-ID\|FT Verb\|RQG Verb; sub-claim 3 declares "3-column scan table at sub-claim 2 is the enumeration proof; column-scan declared sufficient" |
| V-02 | Column-scan verification axis (axis 18) uses R15 V-05 prose-pair enumeration format; no 3-column scan table in checklist sub-claim 2; no dedicated Column-scan enumeration table axis | **FAIL** | SAD axis 18 sub-claim 2: "all FT (F-ID, Verb) pairs listed; all RQG (F-ID, Verb) pairs listed; set equality declared" — prose format, not table structure |
| V-03 | Column-scan verification axis (axis 18) uses R15 V-05 prose-pair enumeration format; no 3-column scan table in checklist sub-claim 2; no dedicated Column-scan enumeration table axis | **FAIL** | Same as V-02 — prose enumeration only |
| V-04 | Inherits V-01's Column-scan enumeration table axis as axis 21 (of 23) | **PASS** | SAD axis 21 present; same mechanism as V-01 |
| V-05 | Inherits V-01's Column-scan enumeration table axis as axis 21 (of 24) | **PASS** | SAD axis 21 present; same mechanism as V-01 |

---

### C-51 — Tier Ordering Derivable from SEVERITY AXIOM + Status Cell Alone

**Requirement**: A formal SEVERITY AXIOM block (standalone named block, not embedded in prose) must appear immediately before the ECM table. The axiom text "T1 severity > T2 severity. T1 = promise-breach. T2 = planning gap." must be the derivation source. Compliance checklist sub-claim 3 of the SKIPPED-tier axis must derive severity ordering from axiom text + ECM Status cell tier label alone — no Examining Sub-Skill column consulted, no finding content accessed. Declaration required: "gap ordering derived from SEVERITY AXIOM; no sub-skill column or finding content consulted." Absence = C-51 ceiling fail.

| Variation | Mechanism for C-51 | Status | Evidence |
|-----------|--------------------|--------|---------|
| V-01 | SKIPPED-tier axis (axis 19) uses R15 V-05 format: tier derivation rule above ECM, SKIPPED-T1/T2 in Status cells. No SEVERITY AXIOM block. No Tier severity axiom SAD axis. | **FAIL** | SKIPPED-tier axis sub-claim 3 declares severity ordering from tier labels, but no standalone SEVERITY AXIOM block; required declaration "gap ordering derived from SEVERITY AXIOM" cannot fire |
| V-02 | SEVERITY AXIOM block added immediately before ECM table; Tier severity axiom axis (axis 21) added to SAD; SKIPPED-tier axis sub-claim 3 cites axiom text + Status cell label only; checklist declares "gap ordering derived from SEVERITY AXIOM; no sub-skill column or finding content consulted" | **PASS** | SAD axis 21 (Tier severity axiom axis) present; SEVERITY AXIOM block written as standalone named block; sub-claim 3 of SKIPPED-tier axis explicitly references axiom; required declaration present |
| V-03 | Same as V-01 — R15 V-05 SKIPPED-tier format; no SEVERITY AXIOM block | **FAIL** | No SEVERITY AXIOM block; no Tier severity axiom axis in SAD |
| V-04 | V-01 + V-03 combined; V-02 mechanism not included. No SEVERITY AXIOM block | **FAIL** | SAD has Column-scan enumeration table axis (21) and Self-match audit table axis (22); no Tier severity axiom axis; no SEVERITY AXIOM block before ECM |
| V-05 | Inherits V-02's SEVERITY AXIOM block and Tier severity axiom axis as axis 22 (of 24); full integration | **PASS** | SAD axis 22 (Tier severity axiom axis) present; SEVERITY AXIOM block before ECM; all three sub-claims of Tier severity axiom axis fire; required declaration present |

---

### C-52 — Verb Source Self-Match Verified by 3-Column Audit Table

**Requirement**: Compliance checklist sub-claim 2 of the Verb-source chain axis must BE a 3-column audit table (RQG Row F-ID | Verb Source F-NN | Match?). Column-equality scan of columns 1 and 2 IS the self-match verification — a mismatch row is visible by scan without reading Verb Source cell content. Checklist must declare: "self-match verified by column-equality scan; Verb Source cell content not read for any row." Absence = C-52 ceiling fail.

| Variation | Mechanism for C-52 | Status | Evidence |
|-----------|--------------------|--------|---------|
| V-01 | Verb-source chain axis (axis 20) uses R15 V-05 format: sub-claim 2 traces one complete three-point chain; sub-claim 3 audits CORRECTED entries. No 3-column audit table in checklist sub-claim 2 | **FAIL** | Verb-source chain axis sub-claim 2: "compliance checklist sub-claim 2 traces one complete three-point chain — chain traversable forward and backward"; prose chain trace, not structural table |
| V-02 | Verb-source chain axis (axis 20) uses R15 V-05 format; same as V-01 | **FAIL** | Same evidence |
| V-03 | Verb-source chain axis (axis 20) restructured: checklist sub-claim 2 IS a 3-column self-match audit table (RQG Row F-ID \| Verb Source F-NN \| Match?); Self-match audit table axis (axis 21) added; declaration present | **PASS** | SAD axis 21 (Self-match audit table axis) present; Verb-source chain axis sub-claim 2 schema: "3-column self-match audit table (RQG Row F-ID \| Verb Source F-NN \| Match?) written here; table verifiable by column-equality scan"; required declaration present |
| V-04 | Inherits V-03's Self-match audit table mechanism as axis 22 (of 23) | **PASS** | SAD axis 22 (Self-match audit table axis) present; same mechanism as V-03 |
| V-05 | Inherits V-03's Self-match audit table mechanism as axis 23 (of 24); full integration | **PASS** | SAD axis 23 (Self-match audit table axis) present; same mechanism as V-03 |

---

## Composite Scoring

### Per-Variation Aspirational Pass Count

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 – C-49 (41 criteria) | 41 | 41 | 41 | 41 | 41 |
| C-50 (column-scan enumeration table) | PASS | FAIL | FAIL | PASS | PASS |
| C-51 (severity axiom tier derivation) | FAIL | PASS | FAIL | FAIL | PASS |
| C-52 (self-match audit table) | FAIL | FAIL | PASS | PASS | PASS |
| **Total aspirational pass** | **42/44** | **42/44** | **42/44** | **43/44** | **44/44** |

### Score Computation

| Variation | Base | Aspirational Bonus | **Score** |
|-----------|------|-------------------|-----------|
| V-01 | 90 | (42/44) × 10 = 9.55 | **99.5** |
| V-02 | 90 | (42/44) × 10 = 9.55 | **99.5** |
| V-03 | 90 | (42/44) × 10 = 9.55 | **99.5** |
| V-04 | 90 | (43/44) × 10 = 9.77 | **99.8** |
| V-05 | 90 | (44/44) × 10 = 10.0 | **100.0** |

### Ranking

| Rank | Variation | Score | Key advantage |
|------|-----------|-------|---------------|
| 1 | V-05 | 100.0 | All three ceiling mechanisms: C-50 + C-51 + C-52 |
| 2 | V-04 | 99.8 | Two ceiling mechanisms: C-50 + C-52 |
| 3 (tie) | V-01 | 99.5 | C-50 only |
| 3 (tie) | V-02 | 99.5 | C-51 only |
| 3 (tie) | V-03 | 99.5 | C-52 only |

---

## Excellence Signals — V-05

**What made V-05 the sole 100.0 scorer:**

### Signal 1 — Three Disjoint Proof Surfaces
V-05 operates three ceiling mechanisms on structurally non-overlapping surfaces:
- C-50: checklist sub-claim 2 of axis 18 (column-scan verification axis)
- C-51: pre-ECM standalone SEVERITY AXIOM block
- C-52: checklist sub-claim 2 of axis 20 (Verb-source chain axis)

Each surface can be falsified independently without touching the other two. A REASSESSED blast status doesn't affect the FT Verb scan table (C-50). A CORRECTED Verb Source entry (C-52) doesn't affect the SEVERITY AXIOM block (C-51). The surface independence is declared in the RQG, making independence itself a verifiable claim.

### Signal 2 — Structural Table as Proof Artifact (C-50 and C-52)
Both C-50 and C-52 use the same pattern: replace a prose assertion or chain trace with a structured N-column table whose **schema** excludes narrative columns, making the format itself the falsifiable artifact.
- C-50: `| F-ID | FT Verb | RQG Verb |` — no narrative column → no narrative field read possible by construction
- C-52: `| RQG Row F-ID | Verb Source F-NN | Match? |` — column equality check IS the self-match verification; mismatch row visible by scan

This pattern converts assertions ("I did not read narrative fields", "F-NN matches row F-ID") into structural proofs: an examiner can verify the claim by table-column inspection alone.

### Signal 3 — Formal Axiom as Standalone Derivation Source (C-51)
The SEVERITY AXIOM block converts the T1 > T2 ordering from a convention embedded in prose into a falsifiable named block that precedes the ECM table. The compliance checklist sub-claim 3 of SKIPPED-tier axis cites only the axiom text and the ECM Status cell tier label — no Examining Sub-Skill column consulted, no SKIPPED reason field read. The ordering derivation becomes a two-step column scan: (1) read axiom text, (2) read Status cell tier label. This generalizes: any severity/ordering claim can be structured as "axiom block → cell label → derivation" without requiring cross-column lookup.

### Signal 4 — Count Invariant Self-Reference at 24
The Row Count Assertion's "Nth and final of N" property scales cleanly to 24 axes. The opening sentence simultaneously encodes self-reference (C-42) and count invariant (C-44) at zero-scan scope, and the enumerated list includes all three new axes by name at positions 21, 22, 23. No brittle count-specific encoding; the pattern works at any N.

---

## New Patterns from R16

**Pattern 1 — Table-schema-as-proof**
Replacing a prose enumeration or chain trace with a structured K-column table (where K is small and no column is a narrative field) converts a compliance assertion into a structural artifact. The schema's column set IS the proof: a table with no narrative column cannot silently include narrative context. Applicable to any "I verified X without reading Y" claim: structure X as the table's column set; exclude Y by schema design.

**Pattern 2 — Axiom-first derivation**
Pre-state an ordering or severity claim as a named standalone block before the artifact it governs. The downstream compliance proof cites axiom text + a single cell value, requiring no cross-column lookup. Eliminates ambiguity about what constitutes the severity source. The axiom block is independently falsifiable: any outcome that contradicts it can be flagged at the axiom's own terms.

**Pattern 3 — Column-equality as verification primitive**
Design audit tables where correctness reduces to a column-equality check (column A value == column B value). The Match? column makes failures visible by table scan without reading cell content. Applicable to any self-referential constraint (e.g., "the ID cited in field X must equal the row's own ID"). The structural form converts an assertion into an enumerated proof.

---

*Scorecard written: 2026-03-17. Rubric: v14. Variations file: campaign-simulate-variations-R16-2026-03-17.md.*
