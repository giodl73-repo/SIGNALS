## Quest Score — corps-scan Round 7

### Scoring Setup

**Rubric**: v7 (30 criteria, 300 pts max)
**Invariants in all 5 variations**: C-28 (manifest enumeration), C-29 (ENTRY contracts), C-30 (full suite every phase)
**Variation axes**: V-01 (phase-contract table), V-02 (manifest as markdown table), V-03 (explicit predicate phrasing), V-04 (V-01+V-02), V-05 (V-01+V-02+V-03)

---

### Per-Criterion Evaluation

#### ESSENTIAL — 50 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|---------|
| C-01 Valid org.yaml | PASS | PASS | PASS | PASS | PASS | All: yaml code fence with `org:`, `groups:`, `exec-office:`, `teams:` keys present in template |
| C-02 Team areas from repo signals | PASS | PASS | PASS | PASS | PASS | All: IVR-P3-A requires every team to trace to Phase 2 inventory; `detected-from:` makes grounding explicit |
| C-03 Group structure | PASS | PASS | PASS | PASS | PASS | All: IVR-P3-C requires `groups:` wrapper with nested teams; template enforces hierarchy |
| C-04 Standard roles | PASS | PASS | PASS | PASS | PASS | All: IVR-P3-D requires 2+ substantive named roles per team; Inertia Advocate excluded |
| C-05 Does not write .craft/roles/ | PASS | PASS | PASS | PASS | PASS | All: IVR-P1-B + IVR-P3-F "C-05 active: no .craft/roles/ content" — dual enforcement |

**Essential subtotal: 50/50 all variations. All 5 essentials pass for all.**

---

#### RECOMMENDED — 30 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|---------|
| C-06 Pivot mode declared | PASS | PASS | PASS | PASS | PASS | All: IVR-P2-B mandates pivot with rationale; PIVOT ENUMERATION template declares selected mode |
| C-07 Exec office placeholder | PASS | PASS | PASS | PASS | PASS | All: IVR-P3-E requires `exec-office:` with `name:`; YAML template includes it |
| C-08 Amend options listed | PASS | PASS | PASS | PASS | PASS | All: IVR-P4-A + explicit AMEND A/B/C blocks with named commands |

**Recommended subtotal: 30/30 all variations.**

---

#### ASPIRATIONAL — 220 pts

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|---------|
| C-09 Pre-YAML inventory | PASS | PASS | PASS | PASS | PASS | All: IVR-P2-A requires typed table before YAML; hard gate enforces ordering |
| C-10 Draft boundary before content | PASS | PASS | PASS | PASS | PASS | All: IVR-P1-A makes boundary statement line 1; "Produce as first output" directive |
| C-11 Typed inventory table | PASS | PASS | PASS | PASS | PASS | All: IVR-P2-A requires 4-column table (Signal, Type, Team Area Candidate, Org Relevance) |
| C-12 Pivot cites named signal | PASS | PASS | PASS | PASS | PASS | All: IVR-P2-B VIOLATION "generic justification with no named table entry" explicitly excluded |
| C-13 Hard ordering gate | PASS | PASS | PASS | PASS | PASS | All: GATE 1 (Structural Ordering) prevents YAML before Phase 2 EXIT |
| C-14 Gate row as terminal table row | PASS | PASS | PASS | PASS | PASS | All: IVR-P2-C with VIOLATION "sentinel line appearing below the table" explicitly excluded |
| C-15 Phase incompleteness predicate | PASS | **PARTIAL** | PASS | PASS | PASS | V-01/V-04: PHASE CONTRACT TABLE "P1 not complete until..." column covers all 4 phases. V-03/V-05: explicit "PHASE N IS NOT COMPLETE UNTIL" at phase start. V-02: no predicate statement in phase bodies or contract table — completion test items operationalize the predicate but lack canonical "not complete until" form at phase start |
| C-16 Traceability failure repair | PASS | PASS | PASS | PASS | PASS | All: IVR-P3-A REPAIR "Return to Phase 2, add missing signal row, re-enter Phase 3" |
| C-17 Completion tests as visible output | PASS | PASS | PASS | PASS | PASS | All: YES/NO completion test blocks directed for all 4 phases (P1 through P4) |
| C-18 IVR triples with all three blocks | PASS | PASS | PASS | PASS | PASS | All: every triple has named INVARIANT, VIOLATION (with concrete example), REPAIR |
| C-19 Dual gate architecture | PASS | PASS | PASS | PASS | PASS | All: GATE 1 (Structural Ordering) + GATE 2 (Semantic Traceability) as independent enforcement points |
| C-20 Amend anti-pattern named | PASS | PASS | PASS | PASS | PASS | All: IVR-P4-A VIOLATION names "Feel free to request adjustments"; amend section header repeats anti-pattern |
| C-21 Gates labeled with category | PASS | PASS | PASS | PASS | PASS | All: "GATE 1 (Structural Ordering)" and "GATE 2 (Semantic Traceability)" with parenthesized labels |
| C-22 All constraints as IVR triples | PASS | PASS | PASS | PASS | PASS | All: 14 labeled triples cover all structural constraints across all phases — no prose-only constraint |
| C-23 Inline detected-from: in YAML | PASS | PASS | PASS | PASS | PASS | All: IVR-P3-B requires `detected-from:` on every team entry; YAML template shows annotation format |
| C-24 Pivot candidates enumerated | PASS | PASS | PASS | PASS | PASS | All: IVR-P2-D VIOLATION "only selected mode declared, rejected modes unnamed" + PIVOT ENUMERATION template |
| C-25 Phase-scoped labels on IVR | PASS | PASS | PASS | PASS | PASS | All: IVR-P1-A through IVR-P4-A labeling convention on all 14 triples |
| C-26 Meta-rule declares non-binding | PASS | PASS | PASS | PASS | PASS | All: explicit META-RULE block "Any directive not expressed as a labeled IVR triple is advisory context only" |
| C-27 Conditional advance instruction | PASS | PASS | PASS | PASS | PASS | All: EXIT-Pn blocks in every completion test name exactly what to do (advance or resolve failing item) |
| C-28 META-RULE enumerates all labels | PASS | PASS | PASS | PASS | PASS | V-01/V-03: inline list of all 14 labels + "Count: 14". V-02/V-04/V-05: manifest table with TOTAL row "14 labeled triples — count to verify completeness" |
| C-29 ENTRY contracts at phase start | PASS | PASS | PASS | PASS | PASS | All: ENTRY-P1/P2/P3/P4 blocks at each phase start; P1 "no prerequisites," P2/P3/P4 gate on prior phase completion |
| C-30 Full suite every phase | PASS | **PARTIAL** | PASS | PASS | PASS | V-02: C-15 PARTIAL (no canonical predicate form) → C-30 PARTIAL. All others: incompleteness predicate + directed test + conditional advance on all 4 phases |

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|
| V-01 | 50 | 30 | 220 | **300** | YES |
| V-02 | 50 | 30 | 210 | **290** | YES |
| V-03 | 50 | 30 | 220 | **300** | YES |
| V-04 | 50 | 30 | 220 | **300** | YES |
| V-05 | 50 | 30 | 220 | **300** | YES |

**Deductions from V-02**: C-15 PARTIAL (−5), C-30 PARTIAL (−5) = −10 pts. All other variations: perfect.

---

### Ranking

1. **V-05** — 300/300 (three independent anchors for C-28/C-29/C-30: manifest table + phase-contract table + explicit predicate phrasing — highest audit density)
2. **V-04** — 300/300 (two structural tables: manifest + phase-contract, doubly-anchored without phase-body predicate text)
3. **V-01** — 300/300 (phase-contract table as top-level audit guide; C-28 satisfied by inline manifest in META-RULE)
4. **V-03** — 300/300 (canonical "Phase N is not complete until X" phrasing at phase start; simplest implementation of the three new criteria)
5. **V-02** — 290/300 (manifest as markdown table is visually superior for C-28 but misses C-15/C-30 canonical predicate form — single-axis focus leaves a gap)

---

### Excellence Signals — V-05 (Top Scorer)

**Pattern 1: Three-surface redundancy for new criteria.** V-05's three anchors (manifest table, phase-contract table, explicit predicate phrasing) mean a reviewer can verify C-28/C-29/C-30 from any one surface without needing the others. Each surface is independently sufficient; together they make discrepancy detectable on the first read.

**Pattern 2: Phase-contract table as front-matter contract.** Placing ENTRY + predicate + test + advance for all 4 phases in a single table before any phase body creates a top-level audit interface. A reviewer can confirm the full phase architecture in one scan, then validate that each phase body implements what the table declares.

**Pattern 3: Canonical "not complete until" phrasing as first structural element per phase.** In V-05, the incompleteness predicate appears as the FIRST line of each phase body, before ENTRY, before IVR triples. This makes C-15/C-30 compliance checkable by scanning phase-openings only — no need to read completion test blocks or cross-reference a summary table.

**Pattern 4: Manifest table count row mirrors gate-row pattern.** The "TOTAL | 14 labeled triples — count to verify completeness" row in the manifest table uses the same structural device as IVR-P2-C's gate row. Both create a terminal sentinel whose value must match a count — mechanical discrepancy detection without text parsing. The gate-row pattern is now applied in two locations.

---

```json
{"top_score": 300, "all_essential_pass": true, "new_patterns": ["Three-surface redundancy: manifest table + phase-contract table + canonical predicate phrasing creates three independently sufficient audit surfaces for C-28/C-29/C-30", "Phase-contract summary table as front-matter contract: ENTRY/EXIT/predicate/test for all phases in one scannable table before any phase body — full architecture audit in one view", "Canonical 'Phase N is not complete until X' predicate as first structural element of each phase body — C-30 compliance checkable by scanning phase-openings only"]}
```
