## flow-lifecycle — Round 17 Scorecard

### Scoring Basis

All five R17 variations are derived from the R16 V-05 baseline, which passed C-09 through C-50 (42 aspirational criteria). The three new v17 criteria — C-51, C-52, C-53 — are the discriminators. Score = aspirational_pass / 45 × 10 (all essential and recommended pass for all variations).

---

### Essential (C-01 – C-05) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 State Transition Coverage | PASS | PASS | PASS | PASS | PASS |
| C-02 Exception Flow Identification | PASS | PASS | PASS | PASS | PASS |
| C-03 Role Assignment Accuracy | PASS | PASS | PASS | PASS | PASS |
| C-04 Bottleneck and Gap Identification | PASS | PASS | PASS | PASS | PASS |
| C-05 Terminal State Completeness | PASS | PASS | PASS | PASS | PASS |
| **Essential sub-score** | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |

All variations inherit the complete R16 V-05 essential structure. No regression observed.

---

### Recommended (C-06 – C-08) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-06 Parallel Path Modeling | PASS | PASS | PASS | PASS | PASS |
| C-07 Edge Case Enumeration | PASS | PASS | PASS | PASS | PASS |
| C-08 Decision Point Explicitness | PASS | PASS | PASS | PASS | PASS |
| **Recommended sub-score** | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |

---

### Aspirational: C-09 – C-50 (Shared Baseline)

All five variations inherit the full R16 V-05 aspirational scaffold. C-09 through C-50 **PASS** for all variations. Notable confirmations:

- **C-48** (Incumbent Baseline Phase-Coverage Back-Reference): All PASS — `Phase Refs:` sub-fields present in INCUMBENT BASELINE rows.
- **C-49** (Exception Block Triple-Citation Architecture Declaration): All PASS — EXCEPTION BLOCK ARCHITECTURE header with three-namespace table and orthogonality assertion present in SECTION A preamble.
- **C-50** (CHAIN STATUS Four-Direction Completeness Inventory): All PASS — DIRECTION INVENTORY block present in all variations (3-col in V-01/V-02/V-04; 4-col in V-03/V-05), enumerating all four canonical directions with PRESENT/ABSENT status and section cites.

---

### Aspirational: C-51 – C-53 (R17 Discriminators)

#### C-51 — CHAIN STATUS Per-Direction Violation Check

Requires each PRESENT direction in DIRECTION INVENTORY to carry an explicit named violation check: source field, target field, and inconsistency pattern.

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | 3-col DIRECTION INVENTORY (Direction / Status / Section Cite). No Violation Check column. PRESENT declarations carry no falsifiability condition. | **FAIL** |
| V-02 | Identical 3-col structure to V-01. C-52 addition does not alter DIRECTION INVENTORY. | **FAIL** |
| V-03 | 4-col DIRECTION INVENTORY adds explicit `Violation Check` column. Each PRESENT direction carries a declarative string-comparison condition naming source field, target field, and exact inconsistency pattern. | **PASS** |
| V-04 | 3-col structure. C-53 addition (IM Ref hint phrasing) does not affect DIRECTION INVENTORY. | **FAIL** |
| V-05 | 4-col DIRECTION INVENTORY with per-direction violation checks (same as V-03), combined with C-52 and C-53 additions. | **PASS** |

#### C-52 — Phase Gate Contract Summary Return-and-Annotate Instruction

Requires a named `Return instruction:` labeled sub-field in PHASE GATE CONTRACT SUMMARY naming the target table (INCUMBENT BASELINE), target sub-field (`Phase Refs:`), and trigger condition.

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | Prose mention of `Phase Refs:` in PHASE GATE CONTRACT SUMMARY. No named `Return instruction:` field. Criterion targets trigger-site labeled instruction, not prose mention. | **FAIL** |
| V-02 | Explicit `**Return instruction:**` labeled sub-field added to PHASE GATE CONTRACT SUMMARY, naming INCUMBENT BASELINE, `Phase Refs:` sub-field, and "upon completing all PHASE ENTRY CONTRACT blocks" as trigger condition. | **PASS** |
| V-03 | Prose structure, same as V-01. C-51 addition does not affect PHASE GATE CONTRACT SUMMARY. | **FAIL** |
| V-04 | Prose structure, same as V-01. C-53 addition does not affect PHASE GATE CONTRACT SUMMARY. | **FAIL** |
| V-05 | Named `Return instruction:` field present (same as V-02), combined with C-51 and C-53 additions. | **PASS** |

#### C-53 — EX Block Hint Architecture Back-Reference

Requires each EX block `IM Ref:` hint to carry an explicit inline back-reference to the EXCEPTION BLOCK ARCHITECTURE declaration **by name**. A generic parenthetical not anchored to the named declaration block is a FAIL.

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | `IM Ref:` hint reads "(see architecture above)". Generic — not anchored to "EXCEPTION BLOCK ARCHITECTURE" by name. Per C-53: "a generic parenthetical not anchored to the EXCEPTION BLOCK ARCHITECTURE header by name is a FAIL." | **FAIL** |
| V-02 | Same "(see architecture above)" as V-01. C-52 addition does not touch EX block hints. | **FAIL** |
| V-03 | Same "(see architecture above)" as V-01. C-51 addition does not touch EX block hints. | **FAIL** |
| V-04 | `IM Ref:` hint reads "(see EXCEPTION BLOCK ARCHITECTURE above)". Names the declaration block explicitly. | **PASS** |
| V-05 | Same "(see EXCEPTION BLOCK ARCHITECTURE above)" as V-04, combined with C-51 and C-52 additions. | **PASS** |

---

### Composite Scores

| Variation | C-09..C-50 | C-51 | C-52 | C-53 | Aspirational | Score | Golden? |
|-----------|:----------:|:----:|:----:|:----:|:------------:|------:|:-------:|
| V-01 | 42 PASS | FAIL | FAIL | FAIL | 42/45 | **9.333** | YES |
| V-02 | 42 PASS | FAIL | PASS | FAIL | 43/45 | **9.556** | YES |
| V-03 | 42 PASS | PASS | FAIL | FAIL | 43/45 | **9.556** | YES |
| V-04 | 42 PASS | FAIL | FAIL | PASS | 43/45 | **9.556** | YES |
| V-05 | 42 PASS | PASS | PASS | PASS | 45/45 | **10.000** | YES |

All five variations exceed the golden threshold (9.0). V-05 is the definitive reference.

---

### Ranking

1. **V-05** — 10.000 — All three new criteria explicit; complete aspirational pass
2. **V-02** — 9.556 — C-52 isolated; trigger-site authoring instruction present
3. **V-03** — 9.556 — C-51 isolated; per-direction falsifiability register present
4. **V-04** — 9.556 — C-53 isolated; named architecture back-reference in hints
5. **V-01** — 9.333 — R16 baseline; all three new criteria implicit (fail)

V-02, V-03, V-04 tie at 9.556. Each isolates a single criterion correctly. Their equivalence confirms the three new criteria are independent — no criterion hides inside another's structure.

---

### Excellence Signals from V-05

**1. Static declaration → active falsifiability register (C-51)**
The DIRECTION INVENTORY evolves from a roster (PRESENT/ABSENT + cite) to a verification gate: each PRESENT direction carries a named string-comparison condition that would reopen the chain. This makes CHAIN STATUS CLOSED a claim that can be falsified without inspecting the full document.

**2. Trigger-site instruction closes the authoring loop (C-52)**
C-48 annotated the destination (INCUMBENT BASELINE `Phase Refs:`). C-52 annotates the source (PHASE GATE CONTRACT SUMMARY). Together they form a documented round-trip: the phase-gate section emits an explicit "return and back-annotate" instruction, preventing the back-annotation from being an implicit co-authoring assumption.

**3. Named back-reference at point of use (C-53)**
"(see architecture above)" is navigable only if the author remembers there is an architecture declaration. "(see EXCEPTION BLOCK ARCHITECTURE above)" names the exact anchor, making the orthogonality assertion discoverable at the exact moment of per-block authoring — no preamble traversal required.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["per-direction violation check in DIRECTION INVENTORY converts static PRESENT/ABSENT roster into active falsifiability register — CHAIN STATUS CLOSED becomes a falsifiable claim", "named return instruction at trigger site (PHASE GATE CONTRACT SUMMARY) closes authoring loop for destination annotation (C-48 Phase Refs), converting implicit co-authoring responsibility into a documented workflow step", "IM Ref hint naming EXCEPTION BLOCK ARCHITECTURE by exact declaration title anchors authors to architecture at point of EX-block authoring — eliminates preamble traversal requirement"]}
```
