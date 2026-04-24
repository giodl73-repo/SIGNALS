## file-issue — Round 7 Scoring (Rubric v6)

---

### V-01 — C-19 Accumulation Only (C-18 intentionally absent)

**Essential criteria:**

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | All four required fields collected (skill, expected, actual, severity) across all four schemas |
| C-02 | PASS | Exactly four-value enum enforced; invalid input rejected with re-prompt in A1 |
| C-03 | PASS | GitHub issue format with `[{severity}] {skill}: {description}` title pattern; structured sections in each output template |
| C-04 | PASS | `simulations/feedback/{skill}-issue-{YYYY-MM-DD}.md` in B2 |

**Recommended criteria:**

| ID | Result | Evidence |
|----|--------|---------|
| C-05 | PASS | Per-severity title patterns name specific skill and symptom |
| C-06 | PASS | All schemas capture invocation, topic, chain; B1 reproducibility row enforces |
| C-07 | PASS | B3 presents `gh issue create` command |

**Aspirational criteria:**

| ID | Result | Evidence |
|----|--------|---------|
| C-08 | PASS | crash template: "Priority: HIGH -- skill non-functional" + Impact field; improvement template: Acceptance condition required |
| C-09 | PASS | B1 "Context enriched" row requires at least one item beyond the four required fields |
| C-10 | PASS | B1 validate gate is a separate phase before B2 write; blocking instruction "do not begin B2 until all rows pass" |
| C-11 | PASS | Each B1 row has explicit "Correction on fail" column with prescribed remediation |
| C-12 | PASS | Four architecturally distinct per-severity schemas and templates; crash has Impact; improvement has Acceptance condition |
| C-13 | PASS | `--label "{severity}"` in B3 gh command |
| C-14 | PASS | "Do not collect any other field until severity is confirmed." + "Severity determines both the collection schema used in A2 and the output template used in A3." — severity is sequenced first, nothing else proceeds until confirmed |
| C-15 | PASS | "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE." — explicit cross-phase blocking directive at the boundary |
| C-16 | PASS | Completion condition defines three verifiable states: (1) severity confirmed as valid enum, (2) required fields non-empty, (3) draft shown — specific and checkable |
| C-17 | **FAIL** | "Determines both" + C-19 alone (no C-18) is insufficient. Per R6 finding #3, the accumulation path requires "determines both" + C-18 + C-19. C-19 heading provenance establishes traceability but the gate (completion condition) does not verify the dispatch linkage — symmetric failure with R6 V-02 where C-18 alone failed C-17 |
| C-18 | **FAIL** | Intentionally absent. Completion condition: "Severity is confirmed as exactly one of the four valid enum values" — verifies confirmation but not dispatch linkage; no "dispatched by" language |
| C-19 | PASS | A2 heading: "(collection schema dispatched by severity in A1)"; A3 heading: "(output template dispatched by severity in A1)" — dispatch origin traceable through document structure |

**Aspirational: 10/12**
**Composite: (4/4 × 60) + (3/3 × 30) + (10/12 × 10) = 60 + 30 + 8.33 = 98.33**

---

### V-02 — Alternative Blocking Imperative

**Essential/Recommended:** All pass (identical coverage to R6 V-04 on these dimensions).

**Aspirational criteria:**

| ID | Result | Evidence |
|----|--------|---------|
| C-08–C-14 | PASS | Per R6 V-04 baseline; same severity-first sequencing, per-severity templates, tone matching |
| C-15 | **PASS** | "PHASE B IS LOCKED. Begin Phase B only after all Phase A conditions below are verified:" — "LOCKED" is an explicit declarative blocking state; "only after...verified" is the unblocking condition. The criterion specifies "explicit" and "blocking" semantics, not the exact imperative form. This alternative phrasing satisfies both. |
| C-16 | PASS | Conditions (1)–(3) beneath the blocking instruction define verifiable states: severity confirmed + dispatch occurred, fields non-empty, draft shown |
| C-17 | PASS | A1: "Severity confirmation is the single event that simultaneously dispatches both: (a) the collection schema... (b) the output template..." — explicit C-17 declaration. Reinforced by C-18 and C-19. |
| C-18 | PASS | Condition (1): "both the collection schema (A2) and output template (A3) have been dispatched by that confirmation (A1 done)" — explicitly verifies dispatch linkage in the completion condition |
| C-19 | PASS | A2: "(collection schema dispatched by severity in A1)"; A3: "(output template dispatched by severity in A1)" |

**Aspirational: 12/12**
**Composite: 60 + 30 + 10.00 = 100.00**

---

### V-03 — Dispatch Manifest Table in A1

**Essential/Recommended:** All pass.

**Aspirational criteria:**

| ID | Result | Evidence |
|----|--------|---------|
| C-08–C-13 | PASS | Per-severity templates and schemas maintained in full; B1 with corrections; --label in B3 |
| C-14 | PASS | "Do not proceed to A2 until one valid value is confirmed." — severity-first sequencing preserved; manifest row cannot be selected until a valid value is confirmed |
| C-15 | PASS | "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE." |
| C-16 | PASS | Completion condition: three verifiable states with explicit manifest dispatch verification |
| C-17 | **PASS** | A1: "Confirming severity is the single event that selects a row in the dispatch manifest below, simultaneously dispatching both the collection schema for A2 and the output template for A3." + "Both columns of the selected row are dispatched by this single confirmation event." Table structure makes both-column dispatch architecturally visible; table-based dispatch notation is structurally equivalent to prose for C-17. |
| C-18 | **PASS** | Completion condition: "both the collection schema and the output template from the A1 dispatch manifest row have been dispatched by that manifest selection event" — dispatch linkage explicitly verified in the gate; table form of C-16/C-18 is valid |
| C-19 | **PASS** | A2: "(collection schema from manifest row selected in A1)"; A3: "(output template from manifest row selected in A1)" — dispatch origin identified as manifest row selection in A1; "manifest row selected in A1" is dispatch provenance in the heading. Form differs from prose-provenance variations but satisfies the criterion. |

**Aspirational: 12/12**
**Composite: 60 + 30 + 10.00 = 100.00**

---

### V-04 — Completion Condition as Verification Table

**Essential/Recommended:** All pass.

**Aspirational criteria:**

| ID | Result | Evidence |
|----|--------|---------|
| C-08–C-14 | PASS | Identical to R6 V-04 on all these dimensions |
| C-15 | PASS | "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE." |
| C-16 | **PASS** | Four-row verification table with "Required State" column constitutes an explicit, verifiable completion condition. Each row names a checkable state: "Exactly one of: crash/wrong-output/missing-feature/improvement," "Both dispatched by severity confirmation event," "All required fields non-empty," "Draft shown to user." Table form satisfies the criterion — prose form is not load-bearing for C-16. |
| C-17 | PASS | A1: "simultaneously dispatches both: (a) the collection schema... (b) the output template..." + C-18 + C-19 |
| C-18 | **PASS** | Dispatch row in the verification table: "Both the collection schema (A2) and the output template (A3) have been dispatched by the severity confirmation event" — this row IS the completion condition; it explicitly requires dispatch verification. Table form is valid for C-18. |
| C-19 | PASS | A2: "(collection schema dispatched by severity in A1)"; A3: "(output template dispatched by severity in A1)" |

**Aspirational: 12/12**
**Composite: 60 + 30 + 10.00 = 100.00**

---

### V-05 — Maximum Compression

**Essential/Recommended:** All pass. Note: C-03 is preserved through condensed but structurally complete per-severity output templates in A3.

**Aspirational criteria:**

| ID | Result | Evidence |
|----|--------|---------|
| C-08 | PASS | crash template retains "Priority: HIGH -- skill non-functional" and Impact field inline; improvement retains "Acceptance condition: {testable definition of done}" inline |
| C-09 | PASS | B1 "Context enriched" row retained: "Add topic, invocation, chain, version, date, or rubric reference" |
| C-10 | PASS | B1 header: "do not begin B2 until all rows pass" — validation gate structurally separates collect/draft from write |
| C-11 | PASS | All 7 B1 rows retain explicit correction column; compression merged title-format and title-specificity rows but each surviving row has a prescribed remedy |
| C-12 | PASS | Four distinct per-severity schemas (inline field chains) and four distinct output templates; crash retains Priority+Impact; improvement retains Acceptance condition — structural distinctness survives compression |
| C-13 | PASS | `--label "{severity}"` in B3 |
| C-14 | PASS | "Do not collect any other field until severity is confirmed." |
| C-15 | PASS | "DO NOT BEGIN PHASE B UNTIL PHASE A IS COMPLETE." |
| C-16 | PASS | Completion condition: "(1) Severity confirmed + both dispatched (A1 done). (2) Required fields non-empty (A2 done). (3) Draft shown (A3 done)." — verifiable states intact after compression |
| C-17 | PASS | "Severity confirmation is the single event that simultaneously dispatches both (a) the collection schema (A2) and (b) the output template (A3). Both are determined by this single event." — C-17 explicit declaration fully preserved in compressed A1 |
| C-18 | PASS | Completion condition (1): "both the collection schema (A2) and output template (A3) have been dispatched by that confirmation" — dispatch verification clause survives maximum compression |
| C-19 | PASS | A2: "(collection schema dispatched by severity in A1)"; A3: "(output template dispatched by severity in A1)" — provenance headings preserved verbatim |

**Aspirational: 12/12**
**Composite: 60 + 30 + 10.00 = 100.00**

---

## Round 7 Scorecard

| Variation | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Aspirational | Composite | Verdict |
|-----------|------|------|------|------|------|------|--------------|-----------|---------|
| V-01 | PASS | PASS | PASS | **FAIL** | **FAIL** | PASS | 10/12 | **98.33** | Golden |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | 12/12 | **100.00** | Golden |
| V-03 | PASS | PASS | PASS | PASS | PASS | PASS | 12/12 | **100.00** | Golden |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | 12/12 | **100.00** | Golden |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | 12/12 | **100.00** | Golden |

---

## Open Questions — Closed

| Question | Predicted | Actual | Finding |
|----------|-----------|--------|---------|
| C-19 alone (no C-18) sufficient for C-17? | FAIL | **FAIL** | Symmetry confirmed: neither C-18 alone (R6 V-02) nor C-19 alone (R7 V-01) satisfies C-17; both are jointly required for the accumulation path |
| "PHASE B IS LOCKED" satisfies C-15? | PASS | **PASS** | Imperative form is not load-bearing; blocking semantics are sufficient |
| Table-based dispatch manifest satisfies C-17/C-18/C-19? | 99.17–100.00 | **100.00** | Table notation fully equivalent to prose for all three dispatch criteria |
| Table-form completion condition satisfies C-16/C-18? | PASS | **PASS** | Form is not load-bearing; Required State column in table is valid for both criteria |
| Maximum compression preserves 12/12? | PASS | **PASS** | Only structural anchors are load-bearing; surrounding elaboration is expendable |

---

## Excellence Signals

**V-02**: "PHASE B IS LOCKED" is the strongest blocking imperative tested — it names the blocked state as a property of Phase B (LOCKED) rather than issuing an instruction to the model (DO NOT BEGIN). The unblocking condition "Begin Phase B only after all Phase A conditions below are verified" makes the lifting condition explicit. This form may be more parse-reliable than the imperative form across model variations.

**V-03**: The dispatch manifest table is the most compact and visually authoritative C-17 implementation. By making the dispatch architecture a literal table (severity → schema + template), row selection *is* dispatch — the structural form embodies the criterion rather than describing it. This is the only variation where a reader can verify the dispatch topology at a glance without reading prose.

**V-04**: Gate column ("A1 done", "A2 done", "A3 done") in the verification table creates a bidirectional reference: completion condition rows trace back to the sub-operation that must complete to enable them. This makes the completion gate self-documenting about its source dependencies.

**V-05**: Minimum viable 12/12 implementation identified. Structural anchors that cannot be compressed without criterion loss: (1) "simultaneously dispatches both (a)... (b)..." in A1, (2) "both dispatched by that confirmation" in completion condition, (3) provenance headings on A2 and A3, (4) "DO NOT BEGIN PHASE B" blocking instruction. All surrounding prose is expendable.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": []}
```
