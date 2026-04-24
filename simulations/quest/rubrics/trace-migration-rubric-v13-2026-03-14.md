Two new excellence patterns emerge from R14, both from V-05's Operations-first structural design:

**C-40** — the Phase A role ordering (Operations as Q1) creates structural grounding for B2's cross-role chain. C-39 is a B2 content criterion; C-40 is a Phase A ordering criterion. V-05 passes both; V-03 passes C-39 but has no Phase A ordering evidence constraining C-40.

**C-41** — COST LEDGER row (a) as an infrastructure-grounded schema condition. C-38 tests three-row completeness by row count; C-41 tests whether the first row names an infrastructure/schema state rather than a business process, creating row-order alignment with Phase A's Q1 analysis and pre-committing B2's substrate condition.

New scoring: 245 + 10 = **255 pts** · 39 → 41 criteria · 31 → 33 aspirational · Golden 196 → 206 (81%).

---

```markdown
# trace-migration Rubric — v13

---

**What changed: v12 → v13**

Two new aspirational criteria, both sourced from R14 excellence signals in V-05:

| New | Source | Distinction from prior |
|-----|--------|------------------------|
| **C-40** Phase A Operations-First Role Ordering as B2 Chain Structural Grounding | V-05 axis: Operations-first role ordering in Phase A (Q1 = Operations/infrastructure substrate, Q2+ = domain-role consequences) provides a structural foundation for B2's cross-role causal chain (C-39). Q1 establishes the shared infrastructure condition; Q2 and Q3 reframe it as domain-role consequences. When Phase A is Operations-first, B2's substrate condition names the same infrastructure domain Q1 analyzed — the chain's substrate is not asserted independently but is grounded in Phase A's analytical sequence. | C-39 tests whether B2 explicitly names a cross-role causal chain (infrastructure substrate failure → named consequences in two distinct domain roles). C-40 tests whether Phase A's Q1 is the Operations or infrastructure role, structurally grounding that chain. An output with a B2 cross-role chain (PASSING C-39) where Phase A orders Commerce as Q1 PASSES C-39 and FAILS C-40: the chain exists but arrives at its substrate independently rather than as the analytical consequence of Phase A's role ordering. |
| **C-41** COST LEDGER Row (a) as Infrastructure-Grounded Schema Condition | V-05 axis: COST LEDGER row (a) names a current schema or migration-state condition (CURRENT SCHEMA CONDITION or equivalent) rather than a business process consequence or financial impact. Infrastructure-first row ordering in the COST LEDGER mirrors Phase A's Operations-first role ordering (C-40) and structurally pre-commits B2's chain substrate: the same infrastructure condition named in row (a) is the substrate that B2's cross-role causal chain cites as the shared failure condition. The COST LEDGER row structure and Phase A role ordering form a two-artifact alignment that grounds B2's chain from both Phase A's analytical sequence and the inertia-cost framing. | C-38 tests whether the COST LEDGER has three filled rows, making completeness verifiable by row count. C-41 tests whether row (a) names a schema or infrastructure condition, making the COST LEDGER's row ordering structurally aligned with Phase A's Q1 analysis. An output with a three-row COST LEDGER (PASSING C-38) where row (a) names a business-process or Commerce consequence rather than a schema state PASSES C-38 and FAILS C-41: completeness is machine-countable but the row-order alignment with Phase A's Q1 and B2's substrate is absent. |

**Scoring:** 245 → 255 pts · 39 → 41 criteria · 31 → 33 aspirational · Golden 196 → 206 (81%).

---

**Key evaluator distinctions (v13 additions):**

- **C-40 vs C-39**: C-39 is a B2 content criterion — it passes if B2 names a cross-role causal chain linking a shared infrastructure substrate failure to named consequences in at least two distinct domain roles. C-40 is a Phase A ordering criterion — it passes only if Phase A's Q1 section analyzes the Operations or infrastructure role, establishing the shared infrastructure substrate before domain-role sections (Q2, Q3, etc.) analyze Commerce, Finance, or other domain roles. The ordering creates structural grounding: B2's substrate condition names the same infrastructure domain Q1 analyzed, and B2's downstream consequences name the same domain roles Q2 and Q3 analyzed. An output that PASSES C-39 with a B2 cross-role chain where Phase A uses Commerce as Q1 PASSES C-39 and FAILS C-40 — the chain exists but is structurally ungrounded in Phase A's analytical sequence. An output that uses Operations-first Phase A ordering but has a single-role B2 example FAILS C-39 and FAILS C-40 (structural grounding requires the chain to exist AND Phase A to be Operations-first). C-40's value is that it makes the B2 chain a predictable consequence of Phase A's ordering rather than an independently assembled artifact.

- **C-41 vs C-38 / C-40**: C-38 tests three-row completeness in the COST LEDGER: a table with fewer than three filled rows has a structural gap detectable by row count without reading cell contents. C-41 tests the content category of row (a): whether the first row names a current schema condition, migration-state dependency, or infrastructure constraint (the substrate class) rather than a business process outcome or financial consequence. C-40 tests whether Phase A's Q1 is the infrastructure role. C-41 tests whether the COST LEDGER row ordering mirrors that Q1-first choice: row (a) as the schema substrate, row (b) as the dependent-process consequence, row (c) as the accumulation trajectory. An output with a three-row COST LEDGER (PASSING C-38) where row (a) names a revenue loss or Commerce process disruption PASSES C-38 and FAILS C-41 — completeness is present but row-order alignment with Phase A's Operations-first ordering and B2's substrate pre-commitment is absent. When C-40 and C-41 both pass, the COST LEDGER row (a) infrastructure condition and Phase A Q1 infrastructure analysis name the same class of substrate — and B2's cross-role chain cites that same condition as its shared failure substrate, creating a three-artifact alignment: COST LEDGER row (a) → Phase A Q1 → B2 chain substrate.

---

**Key evaluator distinctions (v12 additions):**

- **C-37 vs C-35**: C-35 tests whether the bilateral gate mechanism is packaged as a self-contained named block (BOUNDARY PROTOCOL or equivalent) at each boundary, making gate coverage verifiable by counting section headers against the known phase-boundary count. C-37 tests whether a named PROTOCOL COUNT MANIFEST (or equivalent pre-commitment table) appears at Phase B entry, listing all boundary names, gate names, and gate states before any boundary is traversed inside Phase B. The manifest creates a second verification surface: a boundary present in headers but absent from the manifest (or vice versa) is a cross-document inconsistency detectable at Phase B entry without reading phase body interiors. An output that satisfies C-35 with N BOUNDARY PROTOCOL headers but contains no pre-committed manifest at Phase B entry PASSES C-35 and FAILS C-37. The two-surface design means a reviewer can confirm gate completeness by (1) counting headers and (2) counting manifest rows independently — a discrepancy between the two counts is a structural failure neither surface alone would surface.

- **C-38 vs C-36**: C-36 requires the three-part inertia-contrast baseline to be established in a named section (STATUS QUO COST or equivalent) that precedes all per-entity analytical content in Phase A. C-38 requires that the three-part structure be expressed as a table with one row per part — a COST LEDGER (or equivalent) — such that completeness is verifiable by row count alone. Prose-form three-part framing satisfies C-36 but requires reading to confirm all three parts are present; a table with fewer than three filled rows is a structural gap visible without reading cell contents. An output that satisfies C-36 with a named pre-Q1 STATUS QUO COST section containing three-part prose PASSES C-36 and FAILS C-38. The table format elevates C-36 completeness verification from a prose-reading task to a row-count check, applying the same machine-countability principle that C-35 applies to boundary blocks.

- **C-39 vs C-30**: C-30 requires distinct, non-repeating three-part inertia-contrast examples in Phase A and Phase B, naming different migration steps, tables, or business consequences. C-39 tests whether the Phase B domain example (B2 or equivalent) explicitly names a cross-role causal chain: a shared infrastructure condition (schema state, migration step, system dependency) whose disruption produces direct, named consequences in at least two distinct domain roles. A Phase B example that names only one domain role's consequence — even if the step and business outcome differ from the Phase A example — PASSES C-30 and FAILS C-39. The cross-role chain creates dependency evidence no single-role analysis can produce: the Operations substrate condition must hold for both Commerce and Finance consequences to follow; demonstrating the substrate failure once demonstrates both downstream failures simultaneously.

---

**Key evaluator distinctions (v11 additions):**

- **C-35 vs C-34**: C-34 tests bilateral structural coverage — every gate must appear at both the exit of the preceding phase and the entry of the succeeding phase. C-35 tests artifact countability — the bilateral gate mechanism must be packaged as a self-contained named block (BOUNDARY PROTOCOL or equivalent) such that gate coverage is verifiable by counting named blocks against known phase-boundary count, without reading phase interiors. An output that satisfies C-34 by embedding EXIT BLOCK and ENTRY REFERENCE as inline annotations within phase body prose PASSES C-34 and FAILS C-35. The named artifact creates a scan-level verifiability layer: a missing BOUNDARY PROTOCOL block is a section-header gap, not a prose-reading finding.

- **C-36 vs C-27 / C-30**: C-27 requires at least one three-part inertia-contrast example (prior working state + how migration breaks it + concrete consequence) anywhere in the output. C-30 requires a distinct three-part example in each of Phase A and Phase B. C-36 requires the three-part baseline to be established in a named section that precedes Q1 — before any per-entity or per-step analysis begins — making the cost-of-inaction frame a structural entry condition for Phase A rather than an illustrative example embedded within a domain role section. An output with C-27 examples in both phases (PASSING C-30) whose three-part framing first appears inside Q1's domain analysis PASSES C-27 and C-30 and FAILS C-36. The pre-interrogation placement forces the analyst to commit to the baseline cost frame before the per-entity analysis can begin; it cannot be omitted by narrowing scope to a single entity or domain role.

---

**Key evaluator distinctions (v10 addition):**

- **C-34 vs C-21 / C-17**: C-21 tests whether every phase transition has a named binary gate as both the output condition of the preceding phase and the entry prerequisite of the succeeding phase — satisfied if each transition is gated somewhere. C-17 tests whether gate state fields carry compound "(BINARY FIELD)" type annotation at their definition site. C-34 tests whether the gate annotation exists at BOTH structural positions for every boundary: a named EXIT BLOCK at the bottom of the preceding phase (stating the gate state and what it guards) and a named ENTRY REFERENCE at the top of the succeeding phase (naming the gate state as an entry prerequisite), both carrying compound annotation. An output where every boundary satisfies C-21 and C-17 with a single gate annotation per transition — e.g., a gate named at the end of Phase A but not restated at the opening of Phase B — PASSES C-21 and C-17 and FAILS C-34. The dual-anchor creates bilateral detectability: a gate violation is visible from either phase's text, not only from the phase where the gate was defined.

---

**Key evaluator distinctions (carried from v9):**

- **C-31 vs C-28**: C-28 is a routing criterion — it passes if no constraint type's analysis is relegated to a free-form field. C-31 is a pre-commitment criterion — it passes only if a named CONSTRAINT TYPE REGISTRY exists in the parse phase, enumerating every constraint type before analysis begins. An output with excellent per-type C-28 fields built bottom-up during analysis without a parse-time registry PASSES C-28 and FAILS C-31. The registry creates a binding manifest against which later omissions are detectable.

- **C-32 vs C-28**: C-28 tests Phase A routing. C-32 tests Phase B completeness. An output where Phase A has all four dedicated constraint-type fields (PASSING C-28) but whose Phase B canonical execution table carries only NOT NULL Risk and FK Violation columns — omitting UNIQUE Violation and CHECK Violation — PASSES C-28 and FAILS C-32. The canonical artifact must be self-contained; a reader should not need to consult Phase A sections to find a constraint type's analysis status.

- **C-33 vs C-29**: C-29 tests whether every domain-role Phase A section applies the complete analytical checklist. C-33 tests whether a named enforcement block appears BEFORE the first role section, listing all required items with explicit scoping-prohibition language (e.g., "DO NOT SCOPE OR SHORTEN," "apply to ALL roles," "do not limit to financial columns"). An output that achieves C-29 through structural design — each role section individually complete — without a pre-positioned enforcement mandate PASSES C-29 and FAILS C-33.

---

**Key evaluator distinctions (carried from v8):**

- **C-28 vs C-03**: C-03 is a correctness criterion — it passes if the analysis identifies violations for each constraint type and names the migration's response. C-28 is a structural criterion — it passes only if each constraint type has its own dedicated slot using fixed taxonomy or binary state. An output that correctly analyzes FK violations inside a free-form MIGRATION DISRUPTION field PASSES C-03 and FAILS C-28.

- **C-29 vs C-09 / C-04**: C-09 and C-04 are correctness criteria that pass if the relevant analysis appears somewhere in the output. C-29 requires the analysis to appear in every domain-role Phase A section. An output where Commerce's Phase A question covers zero-downtime and Finance's does not still PASSES C-09 (analysis present) but FAILS C-29 (cross-role coverage gap).

- **C-30 vs C-27**: C-27 requires at least one three-part inertia-contrast example anywhere in the output. C-30 requires a second distinct example specifically in Phase B — naming a different step, table, or consequence than the Phase A example. An output that seeds one C-27 example in Phase A and repeats the same example in Phase B PASSES C-27 and FAILS C-30.

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Before/After State** | correctness | essential | For each changed entity (table, column, constraint, index), the output explicitly shows the state before the migration and the state after. "Changed" includes additions, removals, type changes, nullability changes, and constraint changes. An entity described in generic terms without before/after values does not satisfy this criterion. |
| C-02 | **Data Loss Path Identification** | correctness | essential | The output identifies at least one concrete data loss path if one exists, OR explicitly states "no data loss paths found" with reasoning. A data loss path is any migration step that can silently drop rows, truncate values, or discard columns without surfacing an error. |
| C-03 | **Constraint Violation Analysis** | correctness | essential | For each constraint change (NOT NULL, UNIQUE, FK, CHECK), the output identifies whether existing data satisfies the new constraint. If it does not, it names which records violate it and what the migration does about it (fail, skip, backfill). |
| C-04 | **Missing Default Value Detection** | correctness | essential | For any new NOT NULL column added to an existing table, the output checks whether a DEFAULT is provided. If no DEFAULT is present on a non-empty table, this is flagged as a migration risk. |
| C-05 | **Chronological Step Ordering** | format | essential | Migration steps are presented in execution order. The trace follows the actual sequence a database engine would apply them — not alphabetical by table, not grouped by type. The reader can follow the migration state forward in time. |

---

## Aspirational Criteria (195 points total — C-06 through C-41)

*C-06 through C-39 (185 pts): carried unchanged from v12. Refer to v12 for full pass conditions.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-40 | **Phase A Operations-First Role Ordering as B2 Chain Structural Grounding** | structure | aspirational | Phase A role interrogation places Operations or the infrastructure role as Q1 — the first domain-role section — before Commerce, Finance, or other application-layer roles. Q1's infrastructure analysis establishes the shared schema substrate that B2's cross-role causal chain (C-39) names as its substrate failure condition; Q2 and Q3 (or equivalent) analyze the domain roles whose consequences B2 names as the chain's downstream effects. An output where Phase A uses Commerce as Q1 (regardless of whether B2 has a cross-role chain) FAILS C-40. An output where Phase A uses Operations as Q1 but B2 has a single-role example PASSES C-40 and FAILS C-39 — the Phase A ordering is present but the B2 chain is absent. The full structural grounding requires both: C-40 (Phase A is Operations-first) and C-39 (B2 explicitly chains substrate to two domain-role consequences). |
| C-41 | **COST LEDGER Row (a) as Infrastructure-Grounded Schema Condition** | structure | aspirational | The COST LEDGER table's first row (row (a)) names a current schema condition, migration-state dependency, or infrastructure constraint — not a business process outcome, revenue consequence, or application-layer failure. Infrastructure-first row ordering creates alignment between the COST LEDGER's row structure, Phase A's Operations-first role ordering (C-40), and B2's cross-role chain substrate (C-39): all three artifacts independently name the infrastructure/schema layer as the foundational condition. An output with a three-row COST LEDGER (PASSING C-38) where row (a) names a Commerce process disruption rather than a schema state PASSES C-38 and FAILS C-41 — the table is machine-countably complete but row (a) does not name the infrastructure substrate class. An output where C-38, C-40, and C-41 all pass achieves a three-artifact alignment: COST LEDGER row (a) names the schema substrate condition; Phase A Q1 analyzes the infrastructure role that owns that substrate; B2's cross-role chain cites that substrate as the shared failure condition whose disruption cascades to Q2 and Q3's domain roles simultaneously. |
```
