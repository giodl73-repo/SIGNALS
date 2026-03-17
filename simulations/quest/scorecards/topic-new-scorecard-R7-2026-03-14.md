## Scorecard — topic-new Round 7 (v6 rubric)

### V-01 — Compact Gate Injection

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 2 appends row to `simulations/TOPICS.md` with topic, status, strategy path, registered |
| C-02 | PASS | Phase 3 creates `simulations/{topic}/strategy.md` |
| C-03 | PASS | Signal plan table has all six columns: namespace, skill, item name, owner role, stakeholder ref, priority |
| C-04 | PASS | FIELD SCHEMA + Phase 7 gate specify `essential` / `recommended` / `optional` only |
| C-05 | PASS | Phase 7 gate requires >= 1 essential; Commit Gate section enforces naming |
| C-06 | PASS | Phase 7 gate: >= 2 distinct namespaces |
| C-07 | PASS | Phase 3 exit gate: >= 2 sentences, design decision named |
| C-08 | PASS | Phase 7 gate: >= 2 distinct S-N refs in Stakeholder Ref column |
| C-09 | PASS | Dedicated Commit Gate section in Phase 7; each essential named by item name |
| C-10 | PASS | Phase 5 — Artifact Naming Convention is a dedicated section with pattern + example |
| C-11 | PASS | Phase 7 pre-write gate checklist before signal rows |
| C-12 | PASS | FIELD SCHEMA priority row: "Strategy unparseable as commit gate" / "Team commits without a defined stopping condition" |
| C-13 | PASS | Phase 5 = dedicated Artifact Naming section; Commit Gate = dedicated section in Phase 7 |
| C-14 | PASS | All FIELD SCHEMA rows (5) + all COVERAGE SCHEMA rows (3) carry Immediate Failure + Downstream Effect |
| C-15 | PASS | Phase 1 is stakeholders fill-in table as first output with risk columns |
| C-16 | PASS | Every criterion enforced by section header, schema table, checkbox, or template field |
| C-17 | PASS | Phase 1 fill-in table is required first output; Stakeholder Ref column cites S-N back to it |
| C-18 | PASS | FIELD SCHEMA and COVERAGE SCHEMA are separate named schemas, each with Immediate Failure + Downstream Effect columns |
| C-19 | PASS | FIELD SCHEMA has Stakeholder Ref column labeled "Required: cite S-N" |
| C-20 | PASS | Both schemas have two temporally distinct consequence columns: Immediate Failure / Downstream Effect |
| C-21 | PASS | Every phase 1–7 has an exit gate checklist; Phase 7 also has a pre-write gate — all boundaries covered |
| C-22 | PASS | Phase 1 exit gate: `- [ ] >= 3 rows, all four columns filled` — structural checkbox, not prose |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 14/14  
**Composite**: (5/5 × 60) + (3/3 × 30) + (14/14 × 10) = **100.0** ✓ Golden

---

### V-02 — Conversational Register Fix

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Step 2 appends TOPICS.md row |
| C-02 | PASS | Step 3 creates `simulations/{topic}/strategy.md` |
| C-03 | PASS | Signal plan table has all required fields including Stakeholder Ref |
| C-04 | PASS | FIELD SCHEMA + Step 6 gate: `essential` or `recommended` or `optional` — nothing else |
| C-05 | PASS | COVERAGE SCHEMA + Step 6 gate: >= 1 essential |
| C-06 | PASS | COVERAGE SCHEMA + Step 6 gate: >= 2 different namespaces |
| C-07 | PASS | Step 3 exit gate: rationale section, >= 2 sentences, design decision named |
| C-08 | PASS | COVERAGE SCHEMA + Step 6 gate: >= 2 distinct S-N refs |
| C-09 | PASS | Step 7 — dedicated "Name the commit gate" step with done-when checklist |
| C-10 | PASS | Step 5 — dedicated "Know the naming pattern" step with example |
| C-11 | PASS | Step 6 is a pre-write gate checklist before writing any rows |
| C-12 | PASS | FIELD SCHEMA: "Strategy can't be parsed as a gate" / "Team doesn't know which signals must exist before commit" |
| C-13 | PASS | Step 5 = Artifact Naming section; Step 7 = Commit Gate step — both named |
| C-14 | PASS | Both FIELD SCHEMA and COVERAGE SCHEMA have two consequence columns throughout |
| C-15 | PASS | Step 1 is stakeholders fill-in table as first output |
| C-16 | PASS | All enforced constraints have structural homes (tables, checkboxes, steps) |
| C-17 | PASS | Step 1 fill-in table required as first output; S-N keys cited in signal plan |
| C-18 | PASS | FIELD SCHEMA and COVERAGE SCHEMA are separate named tables (Step 4), each with consequence columns — fixes R6 C-18 failure |
| C-19 | PASS | FIELD SCHEMA has Stakeholder Ref column: "Required — cite S-N" |
| C-20 | PASS | "If wrong immediately" / "What that causes downstream" — two temporal tiers in both schemas |
| C-21 | **FAIL** | Steps 1→2, 2→3, 3→4, 4→5, 5→6 all have "Before moving on" gates. But after Step 6 writes the signal plan, there is no exit gate before advancing to Step 7 — the boundary from completed signal rows to Commit Gate step is ungated. The Step 6 pre-write gate (C-11) is entry-only; C-21 requires an exit gate after output is produced |
| C-22 | PASS | Step 1 exit gate: `- [ ] Table has >= 3 rows with all four columns filled` — structural checkbox |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 13/14  
**Composite**: (5/5 × 60) + (3/3 × 30) + (13/14 × 10) = 60 + 30 + 9.29 = **99.29** ✓ Golden

---

### V-03 — Pipeline Overview Table

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 2 appends one row to TOPICS.md |
| C-02 | PASS | Phase 3 creates strategy file at `simulations/{topic}/strategy.md` |
| C-03 | PASS | Signal Plan table: Namespace, Skill, Item Name, Owner Role, Stakeholder Ref, Priority |
| C-04 | PASS | FIELD SCHEMA: `essential` / `recommended` / `optional` only |
| C-05 | PASS | Pre-write gate in Phase 6: >= 1 essential |
| C-06 | PASS | Pre-write gate: >= 2 distinct namespaces |
| C-07 | PASS | Phase 3 exit gate: >= 2 sentences, design decision named |
| C-08 | PASS | Pre-write gate: >= 2 distinct S-N refs |
| C-09 | PASS | "Commit Gate section" bold heading in Phase 6 with explicit item-name requirement |
| C-10 | PASS | Phase 5 — Artifact Naming Convention — dedicated phase |
| C-11 | PASS | Pre-write gate in Phase 6 before signal rows |
| C-12 | PASS | FIELD SCHEMA priority row: "Strategy unparseable as commit gate" / "Team proceeds without a defined stopping condition" |
| C-13 | PASS | Phase 5 = Artifact Naming section; "Commit Gate section" bold heading in Phase 6 |
| C-14 | PASS | Both schemas carry pervasive Immediate Failure + Downstream Effect |
| C-15 | PASS | Phase 1 is stakeholders fill-in table as first output |
| C-16 | PASS | Pipeline overview table, phase checkboxes, schema tables — all structural |
| C-17 | PASS | Phase 1 fill-in table as required first output; Stakeholder Ref traces back to it |
| C-18 | PASS | FIELD SCHEMA and COVERAGE SCHEMA are separate named schemas in Phase 4, each with two consequence columns |
| C-19 | PASS | FIELD SCHEMA has Stakeholder Ref column: "Required — cite S-N" |
| C-20 | PASS | Immediate Failure / Downstream Effect in both schemas — two temporal tiers |
| C-21 | PASS | Pipeline Overview table declares Exit Gate for every phase row before any phase runs; each phase also has an inline exit gate checklist — C-21 satisfied architecturally and inline |
| C-22 | PASS | Pipeline Overview Phase 1 row: ">= 3 rows; all 4 cols filled; specific roles"; Phase 1 exit gate checkbox: `>= 3 rows, all four columns filled` — structural enforcement at two levels |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 14/14  
**Composite**: **100.0** ✓ Golden

---

### V-04 — Schema-Row-Cited Gates

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 2 appends TOPICS.md row |
| C-02 | PASS | Phase 3 creates strategy file |
| C-03 | PASS | Signal plan table has all required fields |
| C-04 | PASS | F-05 row + pre-write gate (F-05 checkbox): `essential` / `recommended` / `optional` only |
| C-05 | PASS | COV-01 threshold + pre-write gate: >= 1 essential |
| C-06 | PASS | COV-02 threshold + pre-write gate: >= 2 distinct namespaces |
| C-07 | PASS | Phase 3 exit gate: "RATIONALE: >= 2 sentences; design decision named" |
| C-08 | PASS | COV-03 threshold + pre-write gate: >= 2 distinct S-N refs |
| C-09 | PASS | Commit Gate section in Phase 6 with item-name naming requirement |
| C-10 | PASS | Phase 5 — Artifact Naming Convention — dedicated phase |
| C-11 | PASS | Pre-write gate in Phase 6 cites F-01 through F-05 + COV-01 through COV-03 |
| C-12 | PASS | F-05: "Strategy unparseable as commit gate" / "Team commits without a defined stopping condition" |
| C-13 | PASS | Phase 5 = Artifact Naming section; Commit Gate = named bold section in Phase 6 |
| C-14 | PASS | Every F-01–F-05 and COV-01–COV-03 row has Immediate Failure + Downstream Effect |
| C-15 | PASS | Phase 1 is stakeholders fill-in table as first output |
| C-16 | PASS | Schema row IDs (F-N, COV-N) create mechanical coupling; gate items cite rows rather than prose |
| C-17 | PASS | Phase 1 fill-in table required as first output; S-N refs enforced through F-04 |
| C-18 | PASS | FIELD SCHEMA (rows F-01–F-05) and COVERAGE SCHEMA (rows COV-01–COV-03) are separate named schemas with consequence columns; pre-write gate cites rows by ID — full C-18 satisfaction |
| C-19 | PASS | F-04 row has Stakeholder Ref column: "Required — cite S-N" |
| C-20 | PASS | Immediate Failure / Downstream Effect — two separate temporal columns in both schemas |
| C-21 | PASS | Phase 1 exit gate (S-TABLE), Phase 2 (TOPICS-ROW), Phase 3 (RATIONALE), Phase 4 (F-01–F-05 + COV-01–COV-03), Phase 5 (ART-NAMING), Phase 6 (pre-write + post-write exit gate) — all boundaries gated; schema-ID notation satisfies "named condition" requirement |
| C-22 | PASS | Phase 1 exit gate: `- [ ] S-TABLE: >= 3 rows, all four columns filled, roles specific` — structural checkbox with explicit count threshold |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 14/14  
**Composite**: **100.0** ✓ Golden

---

### V-05 — Inertia Framing + Per-Phase Gates

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 2 appends TOPICS.md row |
| C-02 | PASS | Phase 3 creates `simulations/{topic}/strategy.md` |
| C-03 | PASS | Phase 7 signal plan table has all required fields + Stakeholder Ref |
| C-04 | PASS | FIELD SCHEMA + Phase 7 pre-write gate: `essential` / `recommended` / `optional` only |
| C-05 | PASS | Phase 7 pre-write gate: >= 1 essential |
| C-06 | PASS | Phase 7 pre-write gate: >= 2 distinct namespaces |
| C-07 | PASS | Phase 3 exit gate: rationale exists, >= 2 sentences, design decision named |
| C-08 | PASS | Phase 7 pre-write gate: >= 2 distinct S-N refs |
| C-09 | PASS | Phase 8 — Commit Gate — dedicated phase with item-name requirement |
| C-10 | PASS | Phase 5 — Artifact Naming Convention — dedicated phase |
| C-11 | PASS | Phase 7 pre-write gate before signal rows |
| C-12 | PASS | FIELD SCHEMA priority: "Strategy unparseable as commit gate" / "Team commits without a stopping condition" |
| C-13 | PASS | Phase 5 = Artifact Naming phase; Phase 8 = Commit Gate phase — each its own heading |
| C-14 | PASS | FIELD SCHEMA (Phase 4) and COVERAGE SCHEMA (Phase 6) both carry two consequence columns pervasively |
| C-15 | PASS | Phase 1 opens with inertia statement about default louder-voice behavior + required stakeholder fill-in table |
| C-16 | PASS | Every constraint enforced by schema table, checkbox, or section header; no criteria enforced by prose alone |
| C-17 | PASS | Phase 1 fill-in table required as first output; S-N keys cited in Phase 7 Stakeholder Ref column |
| C-18 | PASS | FIELD SCHEMA (Phase 4) and COVERAGE SCHEMA (Phase 6) are separate named phases/schemas, each with two consequence columns |
| C-19 | PASS | FIELD SCHEMA has Stakeholder Ref column: "Required — cite S-N" |
| C-20 | PASS | Immediate Failure / Downstream Effect — two temporally distinct columns in both schemas |
| C-21 | PASS | Phase 1 exit gate, Phase 2 exit gate, Phase 3 exit gate, Phase 4 exit gate, Phase 5 exit gate, Phase 6 exit gate, Phase 7 (pre-write gate + post-write exit gate), Phase 8 exit gate — all 8 phases gated; inertia opener per phase adds semantic weight without replacing structural gate |
| C-22 | PASS | Phase 1 exit gate: `- [ ] >= 3 rows, all four columns filled` — structural checkbox with quantified threshold |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 14/14  
**Composite**: **100.0** ✓ Golden

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 Compact Gate Injection | 5/5 | 3/3 | 14/14 | **100.0** | ✓ |
| V-02 Conversational Register Fix | 5/5 | 3/3 | 13/14 | **99.29** | ✓ |
| V-03 Pipeline Overview Table | 5/5 | 3/3 | 14/14 | **100.0** | ✓ |
| V-04 Schema-Row-Cited Gates | 5/5 | 3/3 | 14/14 | **100.0** | ✓ |
| V-05 Inertia Framing + Per-Phase Gates | 5/5 | 3/3 | 14/14 | **100.0** | ✓ |

**V-02 failure analysis**: C-21 fails on a single boundary — after writing the signal plan in Step 6 there is no exit gate before advancing to Step 7 (Commit Gate). Steps 1–5 each have a "Before moving on" checklist; Step 6 has only a pre-write entry gate. The signal rows can be written, potentially failing FIELD SCHEMA or COVERAGE SCHEMA constraints, and the model advances silently to the commit gate. C-11 (pre-write gate) ≠ C-21 (gate-per-boundary); a step that produces structured output needs both an entry gate and an exit gate.

---

## Excellence Signals

**From V-01**: Minimum viable gate form — a one-item or two-item checkbox after every section is sufficient for C-21. Compact gates do not require prose elaboration; two checkboxes (`>= 3 rows, all four columns filled` / `roles are specific`) fully satisfy C-22 as a structural exit gate.

**From V-03**: Pipeline overview table as architectural gate declaration — putting all exit gates into a summary table before any phase content is read satisfies C-21 structurally before the model encounters any phase. The model cannot miss gate conditions because they appear in one place before execution begins, then again inline per phase. Dual-layer (overview table + inline gate) is redundant in the best sense.

**From V-04**: Schema-row-cited gates (F-01, COV-01) satisfy C-21's "named condition" requirement. Schema-ID notation makes gates compact and mechanically coupled to constraint definitions — the gate cites its source rather than restating prose. No other variation achieves this coupling; V-04 is the cleanest mechanical solution.

**From V-05**: Commit Gate as its own phase (Phase 8) rather than a section inside the signal plan phase creates the cleanest boundary: Phase 7 owns signal row production and its own exit gate; Phase 8 owns the named gate and its own exit gate. This separation eliminates V-02's failure mode structurally — the signal plan and the commit gate can never occupy the same ungated step.

**V-02 failure yields a precise rule**: A phase that produces output (signal rows) needs two gate checkpoints — an entry gate before writing (C-11) and an exit gate after writing (C-21). Providing only the entry gate leaves the step without a post-production verification boundary.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Schema-row-cited gates using F-N/COV-N identifiers satisfy C-21 named-condition requirement and create mechanical coupling between constraint definition and enforcement checkpoint without restating prose", "Pipeline overview table with Exit Gate column satisfies C-21 architecturally before any phase runs — all gate conditions visible in one place before execution begins, then reinforced inline per phase", "Pre-write gate alone does not satisfy C-21: a step that produces structured output needs an exit gate after production; V-02's Step 6 entry-only gate left the signal-plan-to-commit-gate boundary ungated"]}
```
