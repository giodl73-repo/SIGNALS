# trace-skill Scorecard — Round 14 (v13 Rubric)

## Per-Variation Analysis

### V-01 — Single axis: SCORER HEURISTIC bold-labeled sub-element

**Architecture**: R13 V-05 baseline + `**SCORER HEURISTIC (C-43):**` bold label after the conformance-collapse claim body + numbered inline list for COUNT GATE scope (TCR at item 1).

| Band | ID | Result | Evidence |
|------|-----|--------|----------|
| Essential | C-01 | PASS | Gather/Bind/Execute/Verdict in sequence |
| Essential | C-02 | PASS | Spec inputs + invocation inputs enumerated by name/source |
| Essential | C-03 | PASS | Bind table maps every input to resolved value |
| Essential | C-04 | PASS | Execute produces artifact with `[ARTIFACT BEGINS HERE]`/`[ARTIFACT ENDS HERE]` delimiters |
| Essential | C-05 | PASS | Verdict compliance ledger declares PASS/FAIL |
| Recommended | C-06 | PASS | Phase Label Schema table emitted pre-trace with exact labels |
| Recommended | C-07 | PASS | Compliance ledger rows cite criterion IDs |
| Recommended | C-08 | PASS | "No elision. No placeholder sections." |
| Aspirational | C-09 | PASS | Coverage Matrix with closed-world preamble |
| Aspirational | C-10 | PASS | Relay carries role/signal/binding/status |
| Aspirational | C-11 | PASS | Section 1 spec inputs, Section 2 invocation inputs |
| Aspirational | C-12 | PASS | BLOCKED rule halts trace on Gap=YES |
| Aspirational | C-13 | PASS | `[ARTIFACT BEGINS/ENDS HERE]` delimiters |
| Aspirational | C-14 | PASS | Phase Label Schema table before trace content |
| Aspirational | C-15 | PASS | Compliance Ledger table (ID | Result | Evidence | Defect code) |
| Aspirational | C-16 | PASS | `StatusVocab` (CLOSED TYPE) on Bind Status column |
| Aspirational | C-17 | PASS | Conflict Precedence Rule declared; spec anchors |
| Aspirational | C-18 | PASS | Relay Binding cells carry `` `InputName = "ResolvedValue"` `` |
| Aspirational | C-19 | PASS | "Precedence applied (PrecedenceVocabulary)" column present |
| Aspirational | C-20 | PASS | CLOSED ASSERTION names Required=YES inputs explicitly |
| Aspirational | C-21 | PASS | ANTI-PATTERN row in Relay: "Do NOT write input name only" |
| Aspirational | C-22 | PASS | `PrecedenceVocabulary` closed three-value (override/default/BLOCKED) |
| Aspirational | C-23 | PASS | "Coverage Matrix is CLOSED for this invocation." terminus line |
| Aspirational | C-24 | PASS | ANTI-PATTERN row has VIOLATION in Required column — structurally independent |
| Aspirational | C-25 | PASS | `PrecedenceVocabulary` named type; "Precedence applied (PrecedenceVocabulary)" cites it |
| Aspirational | C-26 | PASS | STRUCTURAL MANDATE (C-26) block with header + closing heuristic |
| Aspirational | C-27 | PASS | `RequiredVocabulary` (CLOSED TYPE): YES \| VIOLATION |
| Aspirational | C-28 | PASS | All typed columns follow `ColumnName (TypeName)` uniformly across all tables |
| Aspirational | C-29 | PASS | STRUCTURAL MANDATE (C-36/C-37/C-38) blocks carry DefectCodeVocab-coded defect classifications |
| Aspirational | C-30 | PASS | `DefectCodeVocab` (CLOSED TYPE) enumerated: `{OPEN-WORLD-ASSERTION, COUNT-MISMATCH, EMPTY-CELL}` |
| Aspirational | C-31 | PASS | `Defect Code (DefectCodeVocab)` in DCR and `Defect code (DefectCodeVocab)` in Verdict — both annotated |
| Aspirational | C-32 | PASS | C-29 Audit Block + Compliance Ledger with Defect code column; PASS=`--`, FAIL=DefectCodeVocab value |
| Aspirational | C-33 | PASS | `**Independence Statement**:` present within DefectCodeVocab block |
| Aspirational | C-34 | PASS | IF actual == 7 THEN `confirmed` ELSE `mismatch` — binary gate |
| Aspirational | C-35 | PASS | PRE-READ GATE phases (a)/(b)/(c) before Compliance Ledger |
| Aspirational | C-36 | PASS | STRUCTURAL MANDATE (C-36) block for Independence Statement |
| Aspirational | C-37 | PASS | STRUCTURAL MANDATE (C-37): DEFECT: COUNT-MISMATCH emitted on gate failure |
| Aspirational | C-38 | PASS | STRUCTURAL MANDATE (C-38): DEFECT: EMPTY-CELL emitted on empty cell |
| Aspirational | C-39 | PASS | All STRUCTURAL MANDATE blocks start with `STRUCTURAL MANDATE (C-XX):` header |
| Aspirational | C-40 | PASS | All blocks close with `A scorer confirms C-XX compliance by ... alone without ...` |
| Aspirational | C-41 | PASS | Canonical form declared with MALFORMEDNESS RULE; both components named |
| Aspirational | C-42 | PASS | CONFORMANCE-COLLAPSE CLAIM states C-39+C-40 collapse via template check; Closing component required |
| Aspirational | C-43 | PASS | `**SCORER HEURISTIC (C-43):**` bold-labeled element present after claim body; carries "A scorer confirms C-42 compliance by locating this label alone without inspecting individual STRUCTURAL MANDATE block bodies" |
| Aspirational | C-44 | PASS | Numbered inline scope list item 1: `Template Component Registry: \`Required (RequiredVocabulary)\` -- 1 site`; TCR explicitly enumerated with full `ColumnName (TypeName)` notation |

**V-01 score**: 5/5 essential (60) + 3/3 recommended (30) + 36/36 aspirational (10) = **100**

---

### V-02 — Single axis: ANNOTATION SCOPE REGISTRY table

**Architecture**: R13 V-05 baseline + inline final-sentence C-43 heuristic in conformance-collapse claim + formal 7-row ANNOTATION SCOPE REGISTRY table for COUNT GATE scope (TCR at row 1).

C-43 through C-42: all PASS by same analysis as V-01.

| ID | Result | Evidence |
|----|--------|----------|
| C-43 | PASS | CONFORMANCE-COLLAPSE CLAIM final sentence: "A scorer confirms C-42 compliance by verifying this REQUIRED COMPONENTS declaration names both Header and Closing components with their governing criteria alone without inspecting individual STRUCTURAL MANDATE block bodies." Closes the claim paragraph directly. |
| C-44 | PASS | ANNOTATION SCOPE REGISTRY table, Site 1: `Template Component Registry \| \`Required (RequiredVocabulary)\` \| 1`. Full typed-column notation; independently row-verifiable by table lookup. |

**V-02 score**: 5/5 essential (60) + 3/3 recommended (30) + 36/36 aspirational (10) = **100**

---

### V-03 — Single axis: imperative register

**Architecture**: R13 V-05 baseline + imperative register throughout + CONFORMANCE-COLLAPSE RULE with mandatory closing directive + PRESENT/ABSENT checklist for COUNT GATE scope.

| ID | Result | Evidence |
|----|--------|----------|
| C-43 | PASS | `**You MUST close this rule with the following scorer confirmation line**:` directive followed immediately by "A scorer confirms C-42 compliance by verifying both Component 1 and Component 2 are declared as required above alone without inspecting individual STRUCTURAL MANDATE block bodies." Heuristic sentence present and closes the rule block. |
| C-44 | PASS | Numbered PRESENT/ABSENT checklist item 1: `Template Component Registry -- \`Required (RequiredVocabulary)\`: PRESENT / ABSENT`. TCR named with full `ColumnName (TypeName)` notation. |

All C-01–C-42 pass as baseline.

**V-03 score**: 5/5 essential (60) + 3/3 recommended (30) + 36/36 aspirational (10) = **100**

---

### V-04 — Combined: V-01 + V-02

**Architecture**: R13 V-05 baseline + `**SCORER HEURISTIC (C-43):**` bold label + ANNOTATION SCOPE REGISTRY table.

| ID | Result | Evidence |
|----|--------|----------|
| C-43 | PASS | Same bold-labeled `**SCORER HEURISTIC (C-43):**` element as V-01; structurally isolated, label-scannable |
| C-44 | PASS | Same ANNOTATION SCOPE REGISTRY table as V-02; Site 1 = TCR `Required (RequiredVocabulary)` |

All C-01–C-42 pass as baseline. Both C-43 and C-44 at structural peak: label-scan AND row-lookup independently.

**V-04 score**: 5/5 essential (60) + 3/3 recommended (30) + 36/36 aspirational (10) = **100**

---

### V-05 — Combined: V-01 + V-02 + V-03 + SCHEMA ROLE

**Architecture**: Full combination. SCHEMA ROLE runs pre-trace, producing TCR, canonical template, Phase Label Schema, and type declarations as named structural artifacts. `**SCORER HEURISTIC (C-43):**` appears inside SCHEMA ROLE Output 1. ANNOTATION SCOPE REGISTRY table for COUNT GATE.

| ID | Result | Evidence |
|----|--------|----------|
| C-28 | PASS | TCR in SCHEMA ROLE Output 1 has `Required (RequiredVocabulary)` column — the TCR is a produced trace artifact; uniform `ColumnName (TypeName)` convention applies across all 7 annotation sites |
| C-43 | PASS | `**SCORER HEURISTIC (C-43):**` bold-labeled element within SCHEMA ROLE Output 1: "A scorer confirms C-42 compliance by locating this label and reading its stated method alone without inspecting individual STRUCTURAL MANDATE block bodies." Label is part of the trace-produced SCHEMA ROLE output. |
| C-44 | PASS | ANNOTATION SCOPE REGISTRY table in COUNT GATE, Site 1 = `Template Component Registry \| \`Required (RequiredVocabulary)\` \| 1`. TCR is both enumerated in scope AND produced as trace artifact — doubly verifiable. |

Note: SCHEMA ROLE elevates TCR from a prompt annotation to a named trace output. The `Required (RequiredVocabulary)` column exists in the trace record before the COUNT GATE runs. This is beyond C-44 as written but represents a structural advancement.

**V-05 score**: 5/5 essential (60) + 3/3 recommended (30) + 36/36 aspirational (10) = **100**

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Score |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 5/5 | 3/3 | 36/36 | **100** |
| V-02 | 5/5 | 3/3 | 36/36 | **100** |
| V-03 | 5/5 | 3/3 | 36/36 | **100** |
| V-04 | 5/5 | 3/3 | 36/36 | **100** |
| V-05 | 5/5 | 3/3 | 36/36 | **100** |

**All five variations clear golden threshold (all essential PASS, composite ≥ 80).**

---

## Ranking and Excellence Analysis

All five score 100 — C-43 and C-44 introduced no scoring gap in R14, consistent with the design goal that all five carry both criteria as baseline. Discrimination shifts to *structural quality* of the C-43 and C-44 implementations, which would become C-45/C-46 in v14.

**Structural quality ranking** (within the 100-band):

**Tier 1 — V-04 and V-05**: Both C-43 bold-label AND C-44 registry-table. Two independent label-scannable confirmation paths. V-05 additionally elevates TCR to trace output artifact, making C-44's annotation site verifiable in the trace record before the COUNT GATE runs.

**Tier 2 — V-01 and V-02**: One axis each at structural peak. V-01: C-43 bold-label but C-44 as numbered inline list. V-02: C-44 registry-table but C-43 as inline final sentence.

**Tier 3 — V-03**: Both axes functional but neither structurally isolated. C-43 via imperative directive prefix; C-44 via PRESENT/ABSENT checklist. Passes both criteria but requires two-step access for each.

---

## Excellence Signals (C-45/C-46 Candidates)

**Signal 1 — SCORER HEURISTIC as structurally isolated bold-labeled sub-element (V-01/V-04/V-05)**

The conformance-collapse claim body states the mechanism; the `**SCORER HEURISTIC (C-43):**` label follows as an independently citable element, paralleling the `**Independence Statement**:` isolation pattern from C-36. A scorer finds the C-43 confirmation heuristic by label scan without reading the claim body — the same structural isolation discipline that C-36 applied to the independence statement now applied to the conformance-collapse confirmation path. This upgrades C-43 from *confirmation sentence present at claim close* to *confirmation heuristic label-scannable without claim body traversal*.

**Signal 2 — ANNOTATION SCOPE REGISTRY as formal table (V-02/V-04/V-05)**

The COUNT GATE annotation site scope becomes a registry table (Site | Location | Typed Column | Count) with one row per annotation site. Each site is independently row-verifiable by table lookup, applying the same structural discipline to annotation site enumeration that the Defect Classification Registry applies to defect codes. V-05 adds a further step: because the TCR is a SCHEMA ROLE output, the table's TCR row points to a trace-produced artifact rather than a prompt annotation — the annotation site exists in the output space before the gate runs.

---

## New Patterns JSON

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["SCORER HEURISTIC bold-label isolation: the C-43 confirmation heuristic is a structurally isolated **SCORER HEURISTIC (C-43):** labeled sub-element after the conformance-collapse claim body, paralleling **Independence Statement**: isolation from C-36 — a scorer locates the C-42 confirmation path by label scan alone without reading the claim body", "ANNOTATION SCOPE REGISTRY table: the COUNT GATE annotation site scope is a formal registry table (Site | Location | Typed Column | Count) with one row per typed annotation site including TCR row 1, applying DCR-style row discipline to annotation scope enumeration — C-44 compliance is row-verifiable by table lookup without prose parsing"]}
```
