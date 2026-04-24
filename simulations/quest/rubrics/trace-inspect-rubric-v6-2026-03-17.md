Reading the R9 scorecard evidence carefully before constructing the new criteria.

The scorecard shows V-01 achieving C-19 PASS with a specific structural implementation. Two properties appear in that evidence that C-01–C-21 do not capture:

1. **C-22 — Enforcement class annotation**: V-01's C-19 PASS evidence states *"Violation is architecturally impossible, not instructionally discouraged."* No existing criterion requires the skill to declare, per-invariant, whether its enforcement is architectural (structurally impossible to violate) or instructional (rule-based compliance required). C-19 governs whether the EG-first execution order is architectural; C-22 governs whether every invariant in the Coverage Matrix is annotated with its enforcement class.

2. **C-23 — Phase 2a/2b role membership enumerated**: The EG-FIRST EXECUTION CONSTRAINT block declares Phase 2a (EG roles only) → Phase 2b, but C-19's pass condition does not require naming which specific roles belong to each phase. C-23 requires the constraint block to include an explicit membership list — which roles are EG-class (Phase 2a) and which are SA/SG-class (Phase 2b) — making role assignment auditable independently of execution order.

Scoring adjustment: C-22 and C-23 at 0.5 pts each. Aspirational block: C-09 (2 pts) + C-10 (2 pts) + C-11–C-23 (13 × 0.5 = 6.5 pts) = 10.5 pts. Grand total: **100.5 pts**.

---

```markdown
# Trace-Inspect Rubric — v6

**Skill**: `trace-inspect`
**Version**: v6 (updated from v5 — added C-22 and C-23 from R9 excellence signals;
aspirational block: C-09 and C-10 at 2 pts each; C-11 through C-23 at 0.5 pts each;
grand total 100.5)
**Applies to**: Trace outputs produced by any variation of the trace-inspect skill
**Scoring**: 100.5-point composite. Golden threshold: all 5 essential criteria pass AND
composite >= 80.

---

## Coverage Matrix

| Schema | Declared Elements                                              | Invariant                                              |
|--------|----------------------------------------------------------------|--------------------------------------------------------|
| Schema 1 | Severity labels: {P1, P2, P3}                              | No other severity value anywhere in the trace          |
| Schema 2 | Source labels: {SA, SG, EG, QO}                            | No other source value anywhere in the trace            |
| Schema 3 | Lifecycle events: Stage 1 relay, SA-TO-SG PROMOTION, Stage 2 relay | Events occur in declared order                  |
| Schema 4 | Enforcement gates: G-1, G-2, G-3                           | All three checked at Step 3c; no gate skipped          |
| Schema 5 | Phase 3 sub-steps: 3a → 3b → 3c → 3d                      | Sub-steps run in declared order with transition confirmation |

---

## Essential Criteria

> All five must pass for the trace to be useful. A single essential failure makes the trace
> non-golden regardless of score.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Phase completeness** | essential | correctness | All four phases are present and structurally closed. Phase 1 (Setup) produces per-role schema binding blocks with explicit Schema 1 and Schema 2 binding fields and per-role gap attribution. Phase 2 (Execute) runs at least one role relay. Phase 3 (Findings) runs all four sub-steps in order (3a → 3b → 3c → 3d). Phase 4 (Amend) produces at least one change or dismissal entry. A trace missing any phase, or a phase present but producing no required output, fails. |
| C-02 | **Artifact produced** | essential | correctness | Phase 2 (Execute) writes a hand-compiled artifact file at `simulations/trace/skill/{topic}-skill-trace-{date}.md` (or equivalent declared path). The artifact contains every section the skill's artifact contract requires. An Execute phase that produces role relays without a written artifact fails. |
| C-03 | **Schema 1 + Schema 2 compliance** | essential | correctness | Every severity label used anywhere in the trace is from {P1, P2, P3}. Every Source label used anywhere in the trace is from {SA, SG, EG, QO}. A promoted SA gap uses the SG label in all phases after SA-TO-SG PROMOTION. Any label outside these sets, or a promoted gap retaining SA, is a structural violation and fails this criterion. |
| C-04 | **Enforcement gates checked** | essential | behavior | Step 3c records an explicit PASS or FAIL result for each of G-1, G-2, and G-3. G-1: >= 2 distinct Source types in Step 3b table. G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use only {P1, P2, P3}. A trace where any gate is omitted, implicitly assumed to pass, or advanced past despite a FAIL result fails this criterion. |
| C-05 | **Verdict present and classified** | essential | correctness | Phase 5 (or Verdict section) delivers one of three classifications: USEFUL, NEEDS-REDESIGN, or NEEDS-SPEC-REVISION, with the decision rationale. The classification follows the defined rules: NEEDS-SPEC-REVISION if any P1 SA gap remains SA after promotion; NEEDS-REDESIGN if EG gaps exceed 3 and indicate a structural role gap; USEFUL otherwise. A trace ending without a verdict, or with a verdict that contradicts the gap inventory, fails. |

---

## Recommended Criteria

> Output is better with these. Failing one degrades quality but does not make the trace
> useless.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **SA-TO-SG promotion evaluated** | recommended | depth | Every SA gap from the Stage 1 relay is evaluated at the SA-TO-SG PROMOTION lifecycle event. Each gap records PROMOTES TO SG or REMAINS SA with a one-sentence reason. The post-promotion inventory states SA remaining count and SG from promotion count. A trace with SA gaps that skip this evaluation, or where all SA gaps silently disappear without a promotion record, fails this criterion. |
| C-07 | **Per-role relays complete** | recommended | coverage | Each role in the execution sequence has a relay in Phase 2 with all required fields: Received from, Received values, Schema 2 compliance (Source labels used and YES/NO conformance), SA/SG gaps affecting this role, Produced (artifact content added), EG gaps encountered. A relay missing the "Schema 2 compliance" field, or a relay summarized as "role ran normally" without field-level detail, fails this criterion. |
| C-08 | **Findings table depth** | recommended | depth | The Step 3b findings table contains >= 3 distinct findings covering at least 2 different Source types. Each finding has a distinct Action (not a restatement of the finding). A table with only spec-layer (SA) findings or only execution-layer (EG) findings, or with Action cells that repeat the Finding text verbatim, fails this criterion. |

---

## Aspirational Criteria

> Raise the bar once essential and recommended are stable. C-09 and C-10 were present in v1.
> C-11, C-12, and C-13 were added in v2 from R1 excellence signals. C-14 was added in v3 from
> R2 signals. C-15 through C-18 were added in v4 from R6 signals. C-19 through C-21 were added
> in v5 from R7 signals. C-22 and C-23 are new in v6, extracted from R9 excellence signals.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Compliance ledger populated** | 2 pts | correctness | Phase 5 includes the full VC compliance ledger (VC-1 through VC-5) with one row per usage site declared in the Coverage Matrix. The "Observed behavior" cell names specific values, label lists, or invariant results — it does not say "as expected." All VC overall results are stated. A trace with a verdict but no compliance ledger, or a ledger with generic "as expected" observations, fails this criterion. |
| C-10 | **Schema 5 sub-step transition confirmations** | 2 pts | behavior | Each Phase 3 sub-step boundary (3a→3b, 3b→3c, 3c→3d) includes an explicit Schema 5 transition sentence confirming the completed sub-step and declaring the next valid to begin (e.g., "Schema 5 transition: Step 3a complete. Step 3b is valid to begin."). A trace with sub-step transitions that lack this confirmation sentence, or where sub-steps are separated by prose rather than named transition statements, fails this criterion. |
| C-11 | **Gate clearance summary blocks** | 0.5 pts | behavior | A GATE CLEARANCE SUMMARY block appears between Step 3c and Step 3d, summarizing the PASS/FAIL result for each of G-1, G-2, and G-3. A PHASE 4 GATE CLEARANCE SUMMARY block appears at Phase 4 (Amend) entry. A trace missing either block, or one that folds gate summaries into prose rather than discrete named blocks, fails this criterion. |
| C-12 | **Remediation log with exemption clause** | 0.5 pts | behavior | If any enforcement gate (G-1, G-2, or G-3) fails at Step 3c, a REMEDIATION LOG block records each failing gate's ID, failure cause, and remediation action taken before Step 3d proceeds. If all gates pass on first evaluation, a C-12 EXEMPTION clause is present confirming no remediation log is required. A trace with a gate failure and no REMEDIATION LOG, or a trace with no failures that omits the C-12 EXEMPTION clause, fails this criterion. |
| C-13 | **Schema 5 prerequisite verification lines** | 0.5 pts | behavior | Each Phase 3 sub-step includes a Schema 5 prerequisite verification line at its entry point confirming the prior sub-step is complete before the current sub-step begins (e.g., "Schema 5 prerequisite: Step 3a complete."). A trace where any sub-step begins without a prerequisite verification line fails this criterion. |
| C-14 | **Step 3b floor check before Step 3c** | 0.5 pts | behavior | A STEP 3b FLOOR CHECK block appears at the close of Step 3b output, before Step 3c begins. The block verifies that the findings table meets the minimum floor: >= 3 findings, >= 2 distinct Source types, no duplicate Action text. Step 3c may not begin until the FLOOR CHECK is present. A trace where Step 3c begins without a preceding FLOOR CHECK fails this criterion. |
| C-15 | **Layer diversity declaration at Stage 1 close** | 0.5 pts | coverage | Stage 1 (the Setup phase, after all per-role schema binding blocks) concludes with an explicit Layer Diversity declaration: PASS if role-level gaps span at least 2 Source types, FAIL otherwise. A trace where Stage 1 ends without this declaration, or where the declaration is embedded in prose rather than a named block, fails this criterion. |
| C-16 | **EG-evidence grounding declared in promotion section** | 0.5 pts | depth | The SA-TO-SG PROMOTION lifecycle event section includes an explicit statement that promotion decisions may cite observed execution evidence from Phase 2 relays. A promotion section that evaluates SA gaps without this EG-evidence grounding declaration fails this criterion. |
| C-17 | **VC-4 G-1 cross-role attribution in compliance ledger** | 0.5 pts | correctness | The VC-4 G-1 row in the compliance ledger includes an Observed behavior cell that names each Source type observed and identifies which roles contributed evidence of that type. A VC-4 G-1 row with generic "gate passed" observations, or a row that confirms the gate result without cross-role source attribution, fails this criterion. |
| C-18 | **Verdict classification rules pre-stated** | 0.5 pts | correctness | The Verdict section states all three classification rules (NEEDS-SPEC-REVISION, NEEDS-REDESIGN, USEFUL) with their trigger conditions before the verdict assignment field appears. A trace where only the final verdict classification is stated without the preceding rule set, or where the verdict appears before the trigger conditions, fails this criterion. |
| C-19 | **EG-first structural role ordering** | 0.5 pts | behavior | An EG-FIRST EXECUTION CONSTRAINT block appears after the Role-Schema Binding Summary, declaring Phase 2a (EG roles only) → EG-RELAY COMPLETE checkpoint → SA-TO-SG PROMOTION → Phase 2b execution order. The block states the structural invariant that SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE checkpoint passes. A trace without this block, or one that states EG-first ordering as an instruction to the author rather than a structural constraint on the execution model, fails this criterion. |
| C-20 | **Criterion inheritance registry** | 0.5 pts | correctness | A CRITERION INHERITANCE REGISTRY block names all criteria from the prior rubric version by ID and declares each as inherited, revised, or removed. Silence does not imply continuity — any criterion absent from the registry is treated as silently dropped. A skill version that lacks an inheritance registry entirely fails this criterion. |
| C-21 | **Attribution table co-located in compliance ledger** | 0.5 pts | correctness | The VC-4 G-1 row in the compliance ledger includes a pre-printed attribution sub-table embedded directly in the row cell, making filling the ledger and completing source attribution a single atomic operation. A trace where the attribution table is a standalone element separate from the VC-4 row, or where attribution is deferred to a section outside the ledger, fails this criterion. |
| C-22 | **Enforcement class annotation on Coverage Matrix invariants** | 0.5 pts | correctness | Each invariant in the Coverage Matrix is annotated with its enforcement class — ARCHITECTURAL (the execution model makes violation structurally impossible) or INSTRUCTIONAL (violation is possible; the author must comply by rule). A Coverage Matrix with invariants that lack enforcement class annotations, or a trace that describes constraint enforcement without distinguishing architectural impossibility from rule-based compliance, fails this criterion. |
| C-23 | **Phase 2a and Phase 2b role membership enumerated** | 0.5 pts | behavior | The EG-FIRST EXECUTION CONSTRAINT block includes an explicit membership declaration: a named list of which roles execute in Phase 2a (EG-class roles) and which roles execute in Phase 2b (SA/SG-class roles). A constraint block that states the execution order without enumerating role assignments by phase, leaving role classification implicit or derivable only from the role schema, fails this criterion. |
```

---

**Scoring summary for v6**

| Block | Criteria | Weight |
|---|---|---|
| Essential | C-01–C-05 | Pass/fail prerequisite; single FAIL = non-golden |
| Recommended | C-06–C-08 | Degrade quality if failed |
| Aspirational | C-09, C-10 | 2 pts each |
| Aspirational | C-11–C-23 | 0.5 pts each (13 × 0.5 = 6.5 pts) |
| **Total aspirational** | C-09–C-23 | **10.5 pts** |
| **Grand total** | | **100.5 pts** |

R9 champion entry state achieves C-19, C-20, C-21 → **99.5 / 100.5** (C-22 and C-23 each FAIL, 0.5 pts each gap).
