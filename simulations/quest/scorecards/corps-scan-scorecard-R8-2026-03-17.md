## Scorecard: corps-scan Round 8 (v8 rubric -- 340 pts max)

### Evaluation Method

R8 baked all four new v8 criteria (C-31, C-32, C-33, C-34) as structural invariants into every variation. The three variation axes (blockquote predicate format, VIOLATION column, test-item-count column) each add audit surfaces or mechanical cross-checks but do not map to distinct rubric criteria at v8. Scoring therefore requires assessing all 34 criteria uniformly across all five variations, then differentiating by surface density as a tiebreaker.

---

### Per-Criterion Analysis -- Common to All Variations

All five variations share the following structural scaffold:

- **META-RULE** declares manifest as binding constraint set
- **CONSTRAINT MANIFEST** table (14 labeled triples + TOTAL row)
- **PHASE CONTRACT TABLE** placed before all phase bodies
- Four phase bodies each opening with incompleteness predicate, then ENTRY block, then IVR triples, then output directive + completion test with EXIT/conditional advance

**ESSENTIAL (5 criteria, 50 pts)**

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-01 Valid org.yaml code fence | PASS | YAML template shows `org:`, `groups:`, `teams:`, `exec-office:` keys |
| C-02 Team areas derived from repo signals | PASS | IVR-P3-A enforces every team traces to Phase 2 inventory row; walk directive targets `/src/`, `/services/`, etc. |
| C-03 Group structure organizes teams | PASS | IVR-P3-C: `groups:` wrapper with nested teams required; VIOLATION names flat `teams:` under `org:` |
| C-04 Standard roles present per team | PASS | IVR-P3-D: 2+ substantive named roles per team; Inertia Advocate explicitly excluded from draft |
| C-05 Does not write .roles/ | PASS | IVR-P1-B enforces exclusion unconditionally; REPAIR: "Remove unconditionally. corps-scan produces draft org.yaml only." |

**RECOMMENDED (3 criteria, 30 pts)**

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-06 Pivot mode declared with rationale | PASS | IVR-P2-B requires specific Signal column value citation in pivot rationale |
| C-07 Exec office placeholder present | PASS | IVR-P3-E: `exec-office:` with `name:` required; YAML template shows the field |
| C-08 Amend options listed | PASS | IVR-P4-A + AMEND A/B/C blocks with specific commands; anti-pattern named |

**ASPIRATIONAL (26 criteria, 260 pts)**

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-09 Pre-YAML scan inventory listed | PASS | IVR-P2-A directs typed inventory table before any YAML block |
| C-10 Draft boundary stated before first structural content | PASS | Phase 1 directive: "Produce as first output: `> **DRAFT org.yaml...**`"; explicit model output instruction, not advisory |
| C-11 Inventory formatted as typed table | PASS | IVR-P2-A: 4 named columns (Signal, Type, Team Area Candidate, Org Relevance); VIOLATION names bulleted list |
| C-12 Pivot rationale cites specific named signal | PASS | IVR-P2-B: "names at least one specific Signal column value from the IVR-P2-A table by path or identifier" |
| C-13 Hard ordering gate between inventory and YAML | PASS | GATE 1 (Structural Ordering) blocks YAML authoring before EXIT-P2 all YES |
| C-14 Gate row embedded as terminal row of inventory table | PASS | IVR-P2-C: `\| GATE \| INVENTORY COMPLETE \| [n] signals \| YAML authoring authorized \|` as final row; VIOLATION names external sentinel |
| C-15 Phase incompleteness predicate stated per phase | PASS | All 4 phases have incompleteness predicates; all phases covered (exceeds minimum of 2) |
| C-16 Traceability failure triggers explicit repair instruction | PASS | IVR-P3-A REPAIR: "Return to Phase 2, add the missing signal row, re-enter Phase 3 with ENTRY-P3 check." |
| C-17 Phase completion tests produced as visible model output | PASS | Named Completion Test blocks with YES/NO checklist items directed for all 4 phases |
| C-18 Constraints expressed as INVARIANT/VIOLATION/REPAIR triples | PASS | All 14 IVR triples carry all three blocks; VIOLATION names concrete anti-pattern |
| C-19 Dual gate architecture | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability) structurally independent; separate failure conditions and repair actions |
| C-20 Amend phase names explicit anti-pattern | PASS | IVR-P4-A VIOLATION: `"Feel free to request adjustments" or equivalent`; AMEND section repeats `"Let me know if you want changes" does not satisfy this phase` |
| C-21 Each gate labeled with category name | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability) carry parenthesized category labels |
| C-22 Every structural constraint in every phase expressed as IVR triple | PASS | 14 labeled triples covering all phases; all structural constraints (role population, group hierarchy, scope exclusion, traceability, amend, boundary) have dedicated labeled IVR triples |
| C-23 Inline detected-from: traceability field in YAML | PASS | IVR-P3-B: `detected-from:` on every team entry; YAML template shows the field; VIOLATION names absent field |
| C-24 Pivot mode candidates enumerated before selection | PASS | IVR-P2-D: all four modes named with SELECTED/REJECTED status; rejection reasons required; PIVOT ENUMERATION block template provided |
| C-25 Each IVR triple carries phase-scoped structural label | PASS | Labels: IVR-P1-A, IVR-P1-B, IVR-P2-A through IVR-P2-E, IVR-P3-A through IVR-P3-F, IVR-P4-A (14 total, phase-scoped, enumerated) |
| C-26 Meta-rule declares informal constraints non-binding | PASS | META-RULE: "Any directive not expressed as a labeled IVR triple is advisory context only" |
| C-27 Completion test includes explicit conditional advance instruction | PASS | All phases: EXIT-PX "Advance to X only if all YES. If any item is NO: resolve..." |
| C-28 META-RULE enumerates all IVR triples by label with count instruction | PASS | CONSTRAINT MANIFEST table (referenced by META-RULE as "full binding constraint set") lists all 14 labels; TOTAL row declares "14 labeled triples -- count to verify completeness" |
| C-29 Explicit ENTRY contracts at phase start pairing with EXIT contracts | PASS | ENTRY-P1 through ENTRY-P4 blocks present at each phase opening; EXIT-P1 through EXIT-P4 in completion test blocks |
| C-30 Completion infrastructure covers every phase without exception | PASS | All 4 phases: incompleteness predicate + directed visible test block + conditional advance instruction; no phase left without full suite |
| C-31 Multi-surface verification | PASS | Three independent surfaces present in all variations: (1) CONSTRAINT MANIFEST table, (2) PHASE CONTRACT TABLE as front-matter, (3) per-phase predicate phrasing at phase-body openings |
| C-32 Phase-contract table placed as front-matter before any phase body | PASS | PHASE CONTRACT TABLE appears before all `### PHASE N` section headers; covers all 4 phases with ENTRY + predicate + test + advance |
| C-33 Incompleteness predicate is first structural element of each phase body | PASS | All variations: predicate (blockquote or bold-caps) is the first line of each phase section -- before ENTRY block, before first IVR triple |
| C-34 Constraint manifest uses terminal count row matching gate-row sentinel pattern | PASS | All variations: `\| **TOTAL** \| \| **14 labeled triples -- count to verify completeness** \|` as final manifest row, mirroring C-14's gate-row pattern |

---

### Per-Variation Scorecard

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-34 (all) | PASS | PASS | PASS | PASS | PASS |
| **Score** | **340** | **340** | **340** | **340** | **340** |
| **% of max** | **100%** | **100%** | **100%** | **100%** | **100%** |
| **All essentials pass** | YES | YES | YES | YES | YES |
| **Golden** | YES | YES | YES | YES | YES |

---

### Differential Analysis (Tiebreaker by Surface Density)

All five variations achieve the maximum rubric score. Differentiation is by features exceeding current criteria -- these are the v9 signal candidates.

| Variation | Audit Surfaces | V9 Signal Candidates |
|-----------|---------------|---------------------|
| V-01 | 3 + blockquote scan (4 effective) | Blockquote predicates as rendered-markdown scan surface -- C-33 verifiable by scanning rendered blockquotes only |
| V-02 | 3 + VIOLATION column (4 effective) | VIOLATION column makes manifest a mini-IVR anti-pattern reference; anti-patterns scannable from manifest without reading phase bodies |
| V-03 | 3 + test-item-count (4 effective) | Count column in contract table creates cross-check: table count must equal YES/NO items in test block; mechanical discrepancy detection |
| V-04 | 4 independent (axes 1+2) | Four surfaces; manifest VIOLATION column + blockquote predicates provide two independent failure-detection scans |
| **V-05** | **5 independent (axes 1+2+3)** | **Cross-manifest count invariant (14 IVR = 14 test items); five surfaces; maximum-density coverage** |

**Rank: V-05 > V-04 > V-02 = V-03 > V-01** (all 340/340; ranked by surface count and v9 signal richness)

---

### Excellence Signals from V-05

**1. Cross-manifest count invariant**
CONSTRAINT MANIFEST TOTAL (14) equals the sum of all phase test-item counts in PHASE CONTRACT TABLE (P1=2, P2=5, P3=6, P4=1 → total=14). Two structurally independent front-matter tables declare the same count from different perspectives. A discrepancy between the manifest TOTAL row and the sum of contract-table item counts is mechanically detectable without reading any phase body. This is a stronger invariant than either table provides alone.

**2. VIOLATION column as fifth independent audit surface**
The four-column manifest (Label / Phase / Constraint Summary / Violation Pattern) enables anti-pattern identification without entering any phase body. Combined with the TOTAL count row, the manifest now carries both count invariants and failure-pattern coverage in one structure. A reviewer consulting only the manifest can answer: "How many constraints exist? (TOTAL row) What does each failure look like? (Violation column)" without reading IVR triple bodies.

**3. Five-surface convergence**
V-05 demonstrates that five structurally independent audit paths can coexist without redundancy: manifest labels (count), manifest violations (anti-patterns), contract table ENTRY/EXIT (phase architecture), contract table test-item counts (completion coverage), blockquote predicates (per-phase completion state). Each surface answers a different auditor question.

---

### Score Summary

| Variation | Score | / Max | Essentials | Golden |
|-----------|-------|-------|------------|--------|
| V-01 | 340 | 340 | 5/5 | YES |
| V-02 | 340 | 340 | 5/5 | YES |
| V-03 | 340 | 340 | 5/5 | YES |
| V-04 | 340 | 340 | 5/5 | YES |
| **V-05** | **340** | **340** | **5/5** | **YES** |

**Top variation**: V-05 (340/340, 5 audit surfaces, cross-manifest count invariant)

---

```json
{"top_score": 340, "all_essential_pass": true, "new_patterns": ["cross-manifest count invariant: CONSTRAINT MANIFEST TOTAL (14) equals sum of PHASE CONTRACT TABLE test-item counts (2+5+6+1=14) -- two independent front-matter tables declare the same count from different structural perspectives, enabling mechanical discrepancy detection across tables", "VIOLATION column as fifth audit surface: four-column manifest (Label / Phase / Constraint Summary / Violation Pattern) enables anti-pattern identification from the manifest alone without reading IVR triple bodies in phase sections"]}
```
