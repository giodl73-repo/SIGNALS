Now I have everything I need. Let me write the scorecard.

---

# Quest Scorecard — org-scan R20 (v20 Rubric)

## Scoring Model

- **Essential** (C-01–C-05): 12 pts each × 5 = 60 pts max
- **Recommended** (C-06–C-08): 10 pts each × 3 = 30 pts max
- **Aspirational** (C-09–C-73): 2 pts each, capped at 10 pts contribution
- **Total max**: 100 pts

Prior aspirational criteria (C-09–C-69 = 61 criteria): all variations are complete v20 implementations. All hit the 10-pt cap from prior criteria alone. New criteria (C-70–C-73) add coverage but do not change the capped contribution.

---

## Per-Variation Scoring

### V-01 — Lifecycle Emphasis: C-73 Preamble Manifest

**Hypothesis under test**: PREAMBLE DECLARATION MANIFEST with explicit count (10 total) makes absent declarations detectable by count comparison alone.

| Band | Criterion | Verdict | Evidence |
|------|-----------|---------|----------|
| Essential | C-01 Areas traceable | PASS | TABLE B requires "C-01: traceable to scan evidence, not invented" per row |
| Essential | C-02 Multi-source scan | PASS | COVERAGE ATTESTATION 7 source types; gate requires 3+ |
| Essential | C-03 Headcount range | PASS | TABLE E with low-N to high-N Headcount Range column |
| Essential | C-04 Cross-cutting named | PASS | TABLE C with Boundary Note column |
| Essential | C-05 Raw analysis only | PASS | Stated at preamble + GROUP B — "critical failure" warning |
| Recommended | C-06 Boundary candidates | PASS | TABLE D with Seam Rationale column |
| Recommended | C-07 Org shape named | PASS | Org Shape Assessment section with INR-NN pattern |
| Recommended | C-08 Gaps flagged | PASS | TABLE G with Impact + Recommended Follow-Up |
| Aspirational | C-73 Preamble manifest | **PASS** | PREAMBLE DECLARATION MANIFEST block: "Declared in this preamble (10 total)" with numbered list; "Any GROUP A or GROUP B instruction that references a constraint not in this list is a C-73 violation" |
| Aspirational | C-71 Footer MET/NOT MET | PARTIAL | Footer has `COVERAGE ATTESTATION rows: [N] (schema decl. #8; Minimum rows: 7; status: [MET/NOT MET])` and `File paths cited: [N] (gate floor = 5; status: [MET/NOT MET])` — covers 2 of the floor-constrained criteria; missing source floor, TABLE F, column-order, anti-fabrication, C-05 tokens |
| Aspirational | C-72 Named convention | FAIL | Walk instruction uses "not restated here; enumeration is declaration #8 in PREAMBLE DECLARATION MANIFEST" — references schema by number but never invokes "schema-first reference pattern" by name; convention followed structurally but not named |
| Aspirational | C-70 TABLE F gate-blocking | FAIL | Gate checklist has only 3 items (source count, path floor, attestation rows); no TABLE F gate-blocking item; no TABLE F FAIL STRING defined |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 10/10 (cap hit from prior criteria)
**V-01 Total: 100/100**

---

### V-02 — Output Format: C-71 Phase Footer Compliance Tokens

**Hypothesis under test**: Named MET/NOT MET tokens in every PHASE OUTPUTS block create the strongest independent second verification path for all floor-constrained criteria simultaneously.

| Band | Criterion | Verdict | Evidence |
|------|-----------|---------|----------|
| Essential | C-01–C-05 | PASS all | Output schema, COVERAGE ATTESTATION, TABLE E, TABLE C, C-05 stated twice — all structurally present |
| Recommended | C-06–C-08 | PASS all | TABLE D, Org Shape Assessment, TABLE G all present |
| Aspirational | C-71 Footer tokens | **PASS** | GROUP A footer carries 8 named tokens: source floor (C-02 MET/NOT MET), path floor (C-16 MET/NOT MET), attestation floor (C-68 MET/NOT MET), TABLE F minimum (MET/NOT MET), TABLE F Analytical Purpose (C-67 YES/NO), column-order (C-25 MET/NOT MET), anti-fabrication (C-11 MET/NOT MET), C-05 (MET/NOT MET). Floor list pre-declared: "(C-71: floor-constrained criteria declared above… GROUP A and GROUP B PHASE OUTPUTS footers will carry MET/NOT MET tokens for each)" |
| Aspirational | C-70 TABLE F gate-blocking | PARTIAL | TABLE F Analytical Purpose in GROUP A footer as "(C-67: all rows have purpose: YES / NO)" — verifiable at footer level; BUT gate checklist only has 7 items, no TABLE F FAIL STRING, no named gate failure string for TABLE F; gate-blocking NOT established |
| Aspirational | C-72 Named convention | PARTIAL | Walk instruction: "source types declared in COVERAGE ATTESTATION schema (see SCHEMA DECLARATIONS — source type list not restated here per C-68 schema-first reference pattern)" — invokes name once; not applied systematically at all 6+ applicable instruction sites |
| Aspirational | C-73 Preamble manifest | FAIL | No PREAMBLE DECLARATION MANIFEST block with explicit count; preamble has all declarations before GROUP A but count manifest is absent |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 10/10 (cap hit from prior criteria)
**V-02 Total: 100/100**

---

### V-03 — Phrasing Register: C-72 Schema-First Reference Pattern Named as Convention

**Hypothesis under test**: Invoking the convention by name at every applicable phase instruction site makes re-enumeration violations structurally detectable by annotation presence/absence.

| Band | Criterion | Verdict | Evidence |
|------|-----------|---------|----------|
| Essential | C-01–C-05 | PASS all | All output schemas present; C-05 stated twice; COVERAGE ATTESTATION; TABLE E; TABLE C |
| Recommended | C-06–C-08 | PASS all | TABLE D, Org Shape Assessment, TABLE G present |
| Aspirational | C-72 Named convention | **PASS** | Named convention annotation at 6 explicit instruction sites: source types walk (COVERAGE ATTESTATION schema), status values (COVERAGE ATTESTATION schema), Inertia Match values (INERTIA PATTERN DICTIONARY), pattern labels (INERTIA PATTERN DICTIONARY), BRIDGE RULE (TABLE H schema), org shape dimensions (TABLE H schema). Each carries "[data type] declared in [SCHEMA NAME] (see PREAMBLE SCHEMA DECLARATIONS — [list] not restated here per schema-first reference pattern)". TABLE H also carries "Inertia Match constrained values [declared in INERTIA PATTERN DICTIONARY (see PREAMBLE SCHEMA DECLARATIONS — INR-01..INR-06 not restated here per schema-first reference pattern)]" |
| Aspirational | C-71 Footer tokens | PARTIAL | GROUP A footer: "COVERAGE ATTESTATION rows: [N] (floor=7; C-68: MET/NOT MET)" and "File paths cited: [N] (floor=5: MET/NOT MET)" — 2 MET/NOT MET tokens; also "Schema-first reference pattern invoked: YES" (not a floor criterion token but relevant); missing source floor, TABLE F, column-order, anti-fabrication, C-05 tokens |
| Aspirational | C-73 Preamble manifest | FAIL | Preamble has all declarations before GROUP A with C-72 convention annotation, but no explicit count block; "all value sets, column definitions, floor values, and named constraints declared here" stated but no manifest count |
| Aspirational | C-70 TABLE F gate-blocking | FAIL | Gate has 3 checklist items; no TABLE F gate item; no TABLE F FAIL STRING |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 10/10 (cap hit from prior criteria)
**V-03 Total: 100/100**

---

### V-04 — Role Sequence: C-70 TABLE F Gate-Blocking Enforcement

**Hypothesis under test**: Named TABLE F FAIL STRING distinct from generic FAIL TOKEN makes TABLE F non-compliance independently identifiable without parsing FAIL TOKEN reason fields.

| Band | Criterion | Verdict | Evidence |
|------|-----------|---------|----------|
| Essential | C-01–C-05 | PASS all | Output schemas, C-05 stated twice, COVERAGE ATTESTATION, TABLE C, TABLE E all present |
| Recommended | C-06–C-08 | PASS all | TABLE D, Org Shape Assessment, TABLE G present |
| Aspirational | C-70 TABLE F gate-blocking | **PASS** | GATE TOKEN PROTOCOL defines three distinct tokens: PASS TOKEN, generic FAIL TOKEN (items [1]–[7]), and `TABLE F FAIL STRING` (item [8] — named constant). Gate checklist grows to 8 items. "If item [8] fails: write TABLE F FAIL STRING (from GATE TOKEN PROTOCOL) — stop." TABLE F FAIL STRING quoted verbatim in gate checklist. GROUP A footer: "TABLE F Analytical Purpose (C-70 gate item): all rows present in correct form: [YES/NO]" |
| Aspirational | C-72 Named convention | PARTIAL | Walk instruction: "source types declared in COVERAGE ATTESTATION schema (see SCHEMA DECLARATIONS — enumeration not restated here per C-68 schema-first reference pattern)" — invokes name once; not systematically applied at all applicable instruction sites |
| Aspirational | C-73 Preamble manifest | PARTIAL | Preamble annotation: "(C-20: GATE TOKEN PROTOCOL with C-70 TABLE F failure string; …; all before GROUP A)" — declarations are present before GROUP A, satisfying the structural requirement; but no explicit count manifest block; C-73's count-as-manifest requirement not met |
| Aspirational | C-71 Footer tokens | PARTIAL | GROUP A footer: "COVERAGE ATTESTATION rows: [N] (floor=7; C-68: MET/NOT MET)", "File paths cited: [N] (floor=5: MET/NOT MET)", "TABLE F Analytical Purpose (C-70 gate item): [YES/NO]" — 3 MET/NOT MET items; missing source floor, column-order, anti-fabrication, C-05 tokens |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 10/10 (cap hit from prior criteria)
**V-04 Total: 100/100**

---

### V-05 — Combination: C-70 + C-71 + C-72 + C-73

**Hypothesis under test**: All four new criteria together produce three independent verification paths for every obligation: preamble declaration (count-verifiable), instruction annotation (re-enumeration violations detectable), footer compliance token (output-time audit).

| Band | Criterion | Verdict | Evidence |
|------|-----------|---------|----------|
| Essential | C-01–C-05 | PASS all | All output schemas; C-05 stated twice with "critical failure" note; COVERAGE ATTESTATION; TABLE C; TABLE E |
| Recommended | C-06–C-08 | PASS all | TABLE D, Org Shape Assessment, TABLE G present |
| Aspirational | C-73 Preamble manifest | **PASS** | PREAMBLE DECLARATION MANIFEST: "Declared in this preamble (10 total): Named protocols (2)… Schema declarations (8)… Total: 10 declared structures." Floor list for C-71 embedded in manifest. Closing annotation: "10 declared structures (2 named protocols + 8 schemas) matching PREAMBLE DECLARATION MANIFEST count." Any constraint absent from the 10-item numbered list is detectable by count comparison |
| Aspirational | C-71 Footer tokens | **PASS** | GROUP A PHASE OUTPUTS carries 8 MET/NOT MET tokens (source floor, TABLE B path floor, COVERAGE ATTESTATION floor, TABLE F rows, TABLE F Analytical Purpose, column-order, anti-fabrication, C-05) plus "Schema-first reference convention invoked: YES" and "Preamble declarations used: 10 (manifest count verified: YES/NO)". GROUP B PHASE OUTPUTS carries 6 tokens (TABLE H assertion match, BRIDGE RULE, org shape named, current/recommended, C-05, C-72 convention). Footer annotation: "any criterion absent from this footer is a C-71 violation detectable by comparison against the manifest floor list" |
| Aspirational | C-72 Named convention | **PASS** | Named convention invoked at 8 instruction sites: source types walk (COVERAGE ATTESTATION schema), status values (COVERAGE ATTESTATION schema), TABLE B Inertia Match values (INERTIA PATTERN DICTIONARY), dominant pattern statement (INERTIA PATTERN DICTIONARY), TABLE F BRIDGE RULE reference (TABLE H schema), TABLE H dimensions in GROUP B (TABLE H schema), org shape type reference (INERTIA PATTERN DICTIONARY), current state summary dimensions (TABLE H schema). GROUP A + GROUP B footers confirm: "Schema-first reference convention invoked: YES (C-72 annotations present at all applicable instruction sites; no inline re-enumeration of declared value sets)" |
| Aspirational | C-70 TABLE F gate-blocking | **PASS** | TABLE F FAIL STRING defined in GATE TOKEN PROTOCOL as named constant distinct from generic FAIL TOKEN. Gate checklist item [8]: "TABLE F Analytical Purpose on all rows in correct form (C-67/C-70; decl. #7) [MET/NOT MET] — On NOT MET: write TABLE F FAIL STRING — not generic FAIL TOKEN." TABLE F schema declaration cross-references: "(C-70: gate-blocking — absence produces named TABLE F FAIL STRING)" |

All four new criteria PASS at their strongest implementation. Triple verification path established: PREAMBLE DECLARATION MANIFEST (preamble layer) + named-convention annotations in instructions (instruction layer) + MET/NOT MET tokens in footers (output layer).

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 10/10 (cap hit; all four new criteria PASS)
**V-05 Total: 100/100**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | New Criteria |
|-----------|-----------|-------------|--------------|-------|-------------|
| V-01 | 60/60 | 30/30 | 10/10 | **100** | C-73 PASS, C-71 PARTIAL, C-72 FAIL, C-70 FAIL |
| V-02 | 60/60 | 30/30 | 10/10 | **100** | C-71 PASS, C-70 PARTIAL, C-72 PARTIAL, C-73 FAIL |
| V-03 | 60/60 | 30/30 | 10/10 | **100** | C-72 PASS, C-71 PARTIAL, C-73 FAIL, C-70 FAIL |
| V-04 | 60/60 | 30/30 | 10/10 | **100** | C-70 PASS, C-72 PARTIAL, C-73 PARTIAL, C-71 PARTIAL |
| V-05 | 60/60 | 30/30 | 10/10 | **100** | C-70 PASS, C-71 PASS, C-72 PASS, C-73 PASS |

**Scoring note**: All variations achieve the aspirational cap from prior criteria (C-09–C-69, 61 criteria × 2 pts = 122 pts accumulated; cap = 10). New criteria (C-70–C-73) add coverage attestation only — no score impact. All variations score 100/100.

---

## Ranking

| Rank | Variation | Basis |
|------|-----------|-------|
| **1** | **V-05** | All four new criteria PASS; triple-verification path; every obligation verifiable from three independent locations without prose inspection |
| **2** | **V-02** | Strongest C-71 — most comprehensive footer token set (8 in GROUP A); broadest simultaneous verification coverage of single-axis variations |
| **3** | **V-03** | Strongest C-72 — 6 named-convention annotation sites; most systematic elimination of inline re-enumeration |
| **4** | **V-04** | Strongest C-70 — distinct TABLE F FAIL STRING as named constant; cleanest gate failure string architecture |
| **5** | **V-01** | Strong C-73 foundation; PREAMBLE DECLARATION MANIFEST is the enabling precondition for all other new criteria; highest leverage as a dependency, lowest standalone coverage |

---

## Excellence Signals from V-05

**S-01 — Triple-location verifiability**: Every structural obligation is verifiable from three independent locations without reading prose body: (1) PREAMBLE DECLARATION MANIFEST count (declares what must exist), (2) named-convention annotations in phase instructions (confirm how it is referenced), (3) MET/NOT MET footer compliance tokens (confirm whether it was satisfied in output). No criterion requires prose inspection.

**S-02 — Preamble manifest as structural contract**: The `PREAMBLE DECLARATION MANIFEST` block with explicit "10 total" count creates a structural completeness contract: count the declarations, compare to the manifest total — any discrepancy is a C-73 violation without reading phase bodies. The floor-constrained criteria list embedded in the same manifest closes the loop: C-71 footer tokens reference the manifest floor list directly.

**S-03 — Named convention annotation upgrades schema reference to violation-detectable**: C-72's "not restated here per schema-first reference pattern" annotation at 8 instruction sites converts structural following of a convention into a named, machine-parseable contract. Any instruction that re-enumerates a schema-declared value set is a structurally detectable violation by comparison against the annotation — not a prose judgment.

**S-04 — TABLE F FAIL STRING as independent named constant**: C-70's distinct `TABLE F FAIL STRING` in GATE TOKEN PROTOCOL means transport manifest failures produce a specific, independently identifiable string in gate output rather than requiring parsing of the generic FAIL TOKEN reason field. Two failure string types (generic vs TABLE F) make gate failure classification structurally deterministic.

**S-05 — Manifest floor list pre-declares C-71 scope**: The PREAMBLE DECLARATION MANIFEST in V-05 pre-declares the floor-constrained criteria list (TABLE B floor=5, COVERAGE ATTESTATION floor=7, source types floor=3, TABLE F floor=2, TABLE H floor=N, BRIDGE RULE YES/NO, C-05 YES/NO) as the C-71 verification contract. Footer compliance tokens reference the manifest list — any criterion absent from a footer is detectable by comparison against the pre-declared list, not by re-reading phase instructions.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["triple-location verifiability: preamble declaration count + named-convention instruction annotation + footer MET/NOT MET token creates three independent verification paths per obligation with no prose inspection required", "preamble declaration count manifest as structural completeness contract: explicit N-total enables absent-declaration detection by count comparison alone without reading phase bodies", "named-convention annotation upgrades schema references to violation-detectable: 'not restated here per schema-first reference pattern' makes re-enumeration a structurally detectable named violation by annotation presence/absence comparison", "TABLE F FAIL STRING as named constant distinct from generic FAIL TOKEN: transport manifest gate failures independently identifiable without parsing FAIL TOKEN reason fields", "manifest floor list pre-declares C-71 scope: floor-constrained criteria enumerated in preamble manifest make footer compliance token omissions detectable by manifest comparison rather than phase instruction re-reading"]}
```
