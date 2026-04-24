Now I have everything needed. Let me write the R9 scorecard.

---

## Scorecard: corps-scan Round 9 (v9 rubric -- 380 pts max)

### Evaluation Method

R9 baked all four new v9 criteria (C-35, C-36, C-37, C-38) as structural invariants into every variation. The three variation axes (cross-manifest arithmetic verification block, gate token protocol, numbered scan protocol) each add compliance controls or audit surfaces but do not map to distinct rubric criteria at v9. Scoring therefore assesses all 38 criteria uniformly across all five variations, then differentiates by control density as a tiebreaker.

---

### Per-Criterion Analysis -- Common to All Variations

All five variations share the following structural scaffold:

- **META-RULE** declares manifest as binding constraint set (C-26)
- **CONSTRAINT MANIFEST** table: 4-column (Label / Phase / Constraint Summary / Violation Pattern), 14 labeled triples + TOTAL row (C-28, C-34, C-36)
- **PHASE CONTRACT TABLE** placed before all phase bodies, with Test items column P1=2, P2=5, P3=6, P4=1 (C-32, C-37)
- Cross-manifest count invariant: TOTAL(14) == 2+5+6+1 = 14 structurally satisfied in all 5 (C-38)
- Four phase bodies each opening with blockquote incompleteness predicate (`> **Phase N is not complete until**: ...`) before ENTRY block before IVR triples (C-33, C-35)

**ESSENTIAL (C-01 through C-05 -- 5 criteria, 50 pts)**

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-01 Valid org.yaml code fence | PASS | YAML template: `org:`, `groups:`, `teams:`, `exec-office:` keys |
| C-02 Team areas derived from repo signals | PASS | IVR-P3-A: every team traces to Phase 2 inventory row; walk/SCAN PROTOCOL targets `/src/`, `/services/`, etc. |
| C-03 Group structure organizes teams | PASS | IVR-P3-C: `groups:` wrapper with nested teams; VIOLATION names flat `teams:` under `org:` |
| C-04 Standard roles present per team | PASS | IVR-P3-D: 2+ substantive named roles per team; Inertia Advocate excluded from draft |
| C-05 Does not write .roles/ | PASS | IVR-P1-B: exclusion unconditional; REPAIR: "corps-scan produces draft org.yaml only" |

**RECOMMENDED (C-06 through C-08 -- 3 criteria, 30 pts)**

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-06 Pivot mode declared with rationale | PASS | IVR-P2-B: specific Signal column value citation required in pivot rationale |
| C-07 Exec office placeholder present | PASS | IVR-P3-E: `exec-office:` with `name:`; YAML template shows field |
| C-08 Amend options listed | PASS | IVR-P4-A + AMEND A/B/C with specific commands; anti-pattern explicitly named |

**ASPIRATIONAL (C-09 through C-38 -- 30 criteria, 300 pts)**

| Criterion | All Variations | Evidence |
|-----------|---------------|----------|
| C-09 Pre-YAML scan inventory listed | PASS | IVR-P2-A: typed inventory table before any YAML block directed |
| C-10 Draft boundary stated before first structural content | PASS | Phase 1 output directive: blockquote boundary declaration as first output |
| C-11 Inventory formatted as typed table | PASS | IVR-P2-A: 4 named columns; VIOLATION names bulleted list |
| C-12 Pivot rationale cites specific named signal | PASS | IVR-P2-B: "names at least one specific Signal column value from the IVR-P2-A table" |
| C-13 Hard ordering gate between inventory and YAML | PASS | GATE 1 (Structural Ordering) blocks YAML before EXIT-P2 all YES |
| C-14 Gate row embedded as terminal row of inventory table | PASS | IVR-P2-C: `\| GATE \| INVENTORY COMPLETE \| [n] signals \| YAML authoring authorized \|` as final row |
| C-15 Phase incompleteness predicate stated per phase | PASS | All 4 phases carry incompleteness predicates |
| C-16 Traceability failure triggers explicit repair instruction | PASS | IVR-P3-A REPAIR: "Return to Phase 2, add the missing signal row, re-enter Phase 3" |
| C-17 Phase completion tests produced as visible model output | PASS | Named Completion Test blocks with YES/NO checklist items for all 4 phases |
| C-18 Constraints expressed as INVARIANT/VIOLATION/REPAIR triples | PASS | All 14 IVR triples carry all three blocks; VIOLATION names concrete anti-pattern |
| C-19 Dual gate architecture | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability): structurally independent, separate failure conditions |
| C-20 Amend phase names explicit anti-pattern | PASS | IVR-P4-A VIOLATION: `"Feel free to request adjustments"`; AMEND header repeats anti-pattern |
| C-21 Each gate labeled with category name | PASS | GATE 1 (Structural Ordering) and GATE 2 (Semantic Traceability) carry parenthesized labels |
| C-22 Every structural constraint in every phase expressed as IVR triple | PASS | 14 labeled triples covering all phases |
| C-23 Inline detected-from: traceability field in YAML | PASS | IVR-P3-B: `detected-from:` on every team entry; YAML template shows field |
| C-24 Pivot mode candidates enumerated before selection | PASS | IVR-P2-D: all four modes named with SELECTED/REJECTED; PIVOT ENUMERATION template |
| C-25 Each IVR triple carries phase-scoped structural label | PASS | Labels IVR-P1-A through IVR-P4-A, 14 total |
| C-26 Meta-rule declares informal constraints non-binding | PASS | META-RULE: "Any directive not expressed as a labeled IVR triple is advisory context only" |
| C-27 Completion test includes explicit conditional advance instruction | PASS | All phases: EXIT-PX "Advance to X only if all YES. If any item is NO: resolve..." |
| C-28 META-RULE enumerates all IVR triples by label with count instruction | PASS | CONSTRAINT MANIFEST: 14 labels; TOTAL row: "14 labeled triples -- count to verify completeness" |
| C-29 Explicit ENTRY contracts at phase start pairing with EXIT contracts | PASS | ENTRY-P1 through ENTRY-P4 at each phase opening; EXIT blocks in completion tests |
| C-30 Completion infrastructure covers every phase without exception | PASS | All 4 phases: predicate + test block + conditional advance; no phase omitted |
| C-31 Multi-surface verification: three independent audit surfaces | PASS | All 5 variations: (1) CONSTRAINT MANIFEST table, (2) PHASE CONTRACT TABLE front-matter, (3) blockquote predicate phrasing at phase-body openings |
| C-32 Phase-contract table as front-matter before any phase body | PASS | PHASE CONTRACT TABLE precedes all `### PHASE N` headers; covers all 4 phases |
| C-33 Incompleteness predicate is first structural element of each phase body | PASS | All variations: blockquote predicate is the first line of each phase section -- before ENTRY block, before first IVR triple |
| C-34 Constraint manifest terminal count row | PASS | `\| **TOTAL** \| \| **14 labeled triples -- count to verify completeness** \|` as final manifest row |
| C-35 Incompleteness predicate expressed as blockquote | PASS | All 4 phases use `> **Phase N is not complete until**: ...` blockquote syntax in all 5 variations |
| C-36 Constraint manifest carries VIOLATION column | PASS | 4-column manifest (Label / Phase / Constraint Summary / Violation Pattern) in all 5 variations |
| C-37 Phase-contract table carries test-item-count column | PASS | "Test items" column present: P1=2, P2=5, P3=6, P4=1 in all 5 variations |
| C-38 Cross-manifest count invariant: TOTAL equals sum of phase test-item counts | PASS | TOTAL(14) == 2+5+6+1=14: structurally satisfied in all 5; actively enforced via verification block in V-01, V-04, V-05 |

---

### Per-Variation Scorecard

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-38 (all) | PASS | PASS | PASS | PASS | PASS |
| **Score** | **380** | **380** | **380** | **380** | **380** |
| **% of max** | **100%** | **100%** | **100%** | **100%** | **100%** |
| **All essentials pass** | YES | YES | YES | YES | YES |
| **Golden** | YES | YES | YES | YES | YES |

---

### Differential Analysis (Tiebreaker by Control Density)

All five variations achieve the maximum rubric score. Differentiation is by controls exceeding current criteria -- these are the v10 signal candidates.

| Variation | Controls Beyond C-38 | Control Point | v10 Signal Candidates |
|-----------|----------------------|---------------|----------------------|
| V-01 | Cross-manifest verification block | Pre-execution | Explicit arithmetic runner check before Phase 1 -- discrepancy detectable at earliest possible point |
| V-02 | Gate token protocol | Post-phase | Typed PASS/FAIL tokens at gate boundaries -- gate state scannable as first-class artifact |
| V-03 | Numbered scan protocol | Mid-Phase 2 | Deterministic 4-step traversal -- signal omissions detectable by step-completeness, not post-hoc gap analysis |
| V-04 | Axes 1 + 2 | Pre-exec + post-phase | Earliest detection (before P1) + latest enforcement (at gate) bracket the full execution window |
| **V-05** | **Axes 1 + 2 + 3** | **Pre + mid + post** | **Maximum compliance coverage: count integrity before P1, traversal discipline during P2, gate artifacts at boundaries** |

**Rank: V-05 > V-04 > V-01 > V-02 > V-03** (all 380/380; ranked by coverage window span and artifact independence)

Rationale for V-01 > V-02 ordering: The cross-manifest verification block fires before any phase output is produced -- a discrepancy halts execution before the runner commits to any phase work. Gate tokens (V-02) enforce phase ordering but can only fire after phase work is complete. Pre-execution detection is structurally earlier and therefore prevents more waste. V-03 ranks last because SCAN PROTOCOL improves execution quality within Phase 2 but does not add an independent audit surface or produce a scannable artifact.

---

### Excellence Signals from V-05

**1. Cross-manifest arithmetic self-verification as pre-execution compliance gate**
The explicit `CROSS-MANIFEST VERIFICATION` block placed after the two front-matter tables requires the runner to compute `TOTAL(14) == P1(2) + P2(5) + P3(6) + P4(1) = 14` before Phase 1 begins. This promotes C-38 from a passive structural property (the two values happen to agree) to an active runner obligation (the runner must perform the arithmetic and confirm agreement). Any prompt corruption that changes TOTAL or any test-item count without updating the other table becomes detectable before the first phase output is produced. This is the maximum-earliness detection point available in the execution lifecycle.

**2. Gate token protocol as typed compliance artifact at phase boundaries**
The `GATE TOKEN PROTOCOL` block declares canonical PASS and FAIL token strings for GATE 1 and GATE 2. Each gate produces its token as the final line of its embedding completion test block. A reviewer auditing an execution trace can confirm gate compliance by scanning for the token strings at completion test boundaries, without reading any phase body prose. The FAIL token carries a named IVR label and reason, making the failure actionable without re-reading the full phase. Gate state transitions from implicit (prose continuation) to explicit (typed artifact).

**3. Numbered scan protocol as deterministic traversal checklist**
Replacing the prose walk directive with a 4-step `SCAN PROTOCOL` (top-level dirs → source subtrees → workspace configs → CLAUDE.md/role files) creates an execution checklist parallel to the Phase 2 completion test. A signal source omitted from the numbered steps cannot silently fall through -- the runner must complete each step and record discoveries before proceeding. This is the earliest possible detection point for inventory incompleteness: within Phase 2, before the inventory table is finalized.

---

### Score Summary

| Variation | Score | / Max | Essentials | Golden |
|-----------|-------|-------|------------|--------|
| V-01 | 380 | 380 | 5/5 | YES |
| V-02 | 380 | 380 | 5/5 | YES |
| V-03 | 380 | 380 | 5/5 | YES |
| V-04 | 380 | 380 | 5/5 | YES |
| **V-05** | **380** | **380** | **5/5** | **YES** |

**Top variation**: V-05 (380/380, pre-exec + mid-phase + post-phase controls, three independent compliance artifacts)

---

```json
{"top_score": 380, "all_essential_pass": true, "new_patterns": ["cross-manifest arithmetic self-verification block placed after front-matter tables requires runner to confirm TOTAL equals sum of phase test-item counts before Phase 1 begins -- promotes C-38 from passive structural invariant to active pre-execution gate; discrepancy halts execution before any phase output is produced", "gate token protocol declares typed PASS/FAIL token strings for each gate; tokens appear as final line of embedding completion test block; gate state becomes mechanically scannable artifact without reading phase body prose; FAIL token carries named IVR label and reason", "numbered scan protocol replaces unordered walk directive with 4 explicit steps (top-level dirs, source subtrees, workspace configs, CLAUDE.md/role files); each step must be completed and discoveries recorded before proceeding; signal omissions detectable by step-completeness check within Phase 2 before inventory is finalized"]}
```
