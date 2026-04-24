Reading the scorecard carefully to extract the V-05 excellence signals that go beyond V-04 (the simple combination of C-22 + C-23).

**V-04** passes both C-22 and C-23 by combining V-01's column and V-02's membership blocks — that is the base. **V-05** adds two structural linkage moves not required by any current criterion:

1. The EG-FIRST EXECUTION CONSTRAINT block explicitly **cites** the Coverage Matrix Enforcement Class column — connecting the constraint declaration to the annotation source.
2. The VC-4 G-1 compliance ledger entry includes a **count-check that validates** the PHASE 2a/2b MEMBERSHIP declarations — the compliance pass for G-1 is anchored to the named membership list, not derived independently.

These are C-24 and C-25. Each 0.5 pts. Grand total: **101.5 pts**.

---

```markdown
# Trace-Inspect Rubric — v7

**Skill**: `trace-inspect`
**Version**: v7 (updated from v6 — added C-24 and C-25 from R10 excellence signals;
aspirational block: C-09 and C-10 at 2 pts each; C-11 through C-25 at 0.5 pts each;
grand total 101.5)
**Applies to**: Trace outputs produced by any variation of the trace-inspect skill
**Scoring**: 101.5-point composite. Golden threshold: all 5 essential criteria pass AND
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
> in v5 from R7 signals. C-22 and C-23 were added in v6 from R9 excellence signals. C-24 and
> C-25 are new in v7, extracted from R10 excellence signals (V-05 structural linkage moves that
> exceed the base combination of C-22 + C-23).

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Compliance ledger populated** | 2 pts | correctness | Phase 5 includes the full VC compliance ledger (VC-1 through VC-5) with one row per usage site declared in the Coverage Matrix. The "Observed behavior" cell names specific values, label lists, or invariant results — it does not say "as expected." All VC overall results are stated. A trace with a verdict but no compliance ledger, or a ledger with generic "as expected" observations, fails this criterion. |
| C-10 | **Schema 5 sub-step transition confirmations** | 2 pts | behavior | Each Phase 3 sub-step boundary (3a→3b, 3b→3c, 3c→3d) includes an explicit Schema 5 transition sentence confirming the completed sub-step and declaring the next valid to begin (e.g., "Schema 5 transition: Step 3a complete. Step 3b is valid to begin."). A trace with sub-step transitions that lack this confirmation sentence, or where sub-steps are separated by prose rather than named transition statements, fails this criterion. |
| C-11 | **Gate clearance summary blocks** | 0.5 pts | behavior | A GATE CLEARANCE SUMMARY block appears between Step 3c and Step 3d, summarizing the PASS/FAIL result for each of G-1, G-2, and G-3. A PHASE 4 GATE CLEARANCE SUMMARY block appears at Phase 4 (Amend) entry. A trace missing either block, or one that folds gate summaries into prose rather than discrete named blocks, fails this criterion. |
| C-12 | **Remediation log with exemption clause** | 0.5 pts | behavior | If any enforcement gate (G-1, G-2, or G-3) fails at Step 3c, a REMEDIATION LOG block records each failing gate's ID, failure cause, and remediation action taken before Step 3d proceeds. If all gates pass on first evaluation, a C-12 EXEMPTION clause is present confirming no remediation log is required. A trace with a gate failure and no REMEDIATION LOG, or a trace with no failures that omits the C-12 EXEMPTION clause, fails this criterion. |
| C-13 | **Schema 5 prerequisite verification lines** | 0.5 pts | behavior | Each Phase 3 sub-step includes a Schema 5 prerequisite verification line at its entry point confirming the prior sub-step is complete before the current sub-step begins (e.g., "Schema 5 prerequisite: Step 3a complete."). A trace where any sub-step begins without a prerequisite verification line fails this criterion. |
| C-14 | **Step 3b floor check before Step 3c** | 0.5 pts | behavior | A STEP 3b FLOOR CHECK block appears at the close of Step 3b output, before Step 3c begins. The block verifies that the findings table meets the minimum floor: >= 3 findings, >= 2 distinct Source types, no duplicate Action text. Step 3c may not begin until the FLOOR CHECK is present. A trace where Step 3c begins without a preceding FLOOR CHECK fails this criterion. |
| C-15 | **EG-FIRST EXECUTION CONSTRAINT block declared** | 0.5 pts | behavior | A named EG-FIRST EXECUTION CONSTRAINT block appears in Phase 2 before any role relay begins. The block states the two-phase execution rule: Phase 2a runs EG-class roles only; Phase 2b runs SA/SG-class roles only after all EG relays complete. A trace where Phase 2 begins without this named block, or where the block appears after the first relay, fails this criterion. |
| C-16 | **EG-RELAY COMPLETE barrier declared** | 0.5 pts | behavior | An EG-RELAY COMPLETE block appears in Phase 2 after the final EG-class relay and before the first SA/SG-class relay. The block confirms all EG roles have relayed and declares Phase 2b open. A trace where SA/SG-class relays begin without a preceding EG-RELAY COMPLETE barrier fails this criterion. |
| C-17 | **Role-Schema Binding Summary present** | 0.5 pts | correctness | Phase 1 (Setup) closes with a ROLE-SCHEMA BINDING SUMMARY block that lists every role, its declared phase (2a or 2b), and its Schema 2 Source label. The summary is distinct from per-role binding blocks and provides a single-location audit view of all role assignments. A trace where Phase 1 ends without this summary block fails this criterion. |
| C-18 | **Phase 2a/2b sequence verified at EG-RELAY COMPLETE** | 0.5 pts | behavior | The EG-RELAY COMPLETE block includes an explicit verification line confirming that no SA/SG-class relay ran before it (e.g., "Phase 2a sequence verified: no SA/SG relay preceded this barrier."). A trace where the EG-RELAY COMPLETE block appears but contains no sequence verification line fails this criterion. |
| C-19 | **EG-FIRST execution order is architectural** | 0.5 pts | behavior | The EG-FIRST EXECUTION CONSTRAINT block declares that the Phase 2a-before-2b execution order is structurally enforced, not instructionally requested. The block states that SA/SG-class relay execution is architecturally gated on EG-RELAY COMPLETE — violation is impossible, not merely discouraged. A trace where the constraint block exists but frames the execution order as a guideline or best practice fails this criterion. |
| C-20 | **Per-relay EG-FIRST conformance acknowledged** | 0.5 pts | behavior | Each SA/SG-class relay in Phase 2b opens with a conformance line acknowledging that EG-RELAY COMPLETE was declared before this relay began (e.g., "EG-FIRST conformance: EG-RELAY COMPLETE confirmed. Phase 2b relay authorized."). A trace where any SA/SG-class relay begins without this acknowledgment line fails this criterion. |
| C-21 | **Enforcement class declared for EG-FIRST invariant** | 0.5 pts | behavior | The EG-FIRST EXECUTION CONSTRAINT block includes an explicit enforcement class declaration for the Phase 2a/2b sequencing invariant, stating whether it is `architectural` (structurally impossible to violate) or `instructional` (rule-based compliance required). A trace where the constraint block asserts architectural enforcement without a named enforcement class declaration fails this criterion. |
| C-22 | **Enforcement class annotation per invariant** | 0.5 pts | correctness | Every invariant in the Coverage Matrix is annotated with its enforcement class (`architectural` or `instructional`), either via a dedicated Enforcement Class column in the matrix or via an `[enforcement: X]` suffix on each invariant declaration — making per-invariant enforcement status auditable without consulting the constraint blocks. A Coverage Matrix with no enforcement class annotation on any invariant, or one where only some invariants are annotated, fails this criterion. |
| C-23 | **Phase 2a/2b role membership enumerated** | 0.5 pts | behavior | The EG-FIRST EXECUTION CONSTRAINT block contains explicit named membership lists — PHASE 2a MEMBERSHIP (EG-class roles) and PHASE 2b MEMBERSHIP (SA/SG-class roles) — with per-phase role counts and a total-roles check. Role assignment is auditable from the constraint block alone without consulting the Role-Schema Binding Summary. A constraint block that declares phase sequencing without naming which roles belong to each phase fails this criterion. |
| C-24 | **Enforcement-constraint cross-reference** | 0.5 pts | correctness | The EG-FIRST EXECUTION CONSTRAINT block contains an explicit citation of the Coverage Matrix Enforcement Class column (or annotation site), creating navigable structural linkage from the execution constraint to the invariant annotation source. The linkage makes it possible to trace enforcement class provenance in both directions: from the constraint block to the matrix, and from the matrix to the constraint. A trace where the enforcement annotation (C-22) and the execution constraint (C-21) exist as independent structures without any declared cross-reference fails this criterion. |
| C-25 | **Membership count validation at compliance ledger** | 0.5 pts | behavior | The VC-4 G-1 entry in the compliance ledger includes a count-check that validates the PHASE 2a/2b MEMBERSHIP declarations from the EG-FIRST EXECUTION CONSTRAINT block — confirming that the distinct Source type count used to satisfy G-1 is consistent with the named membership lists rather than derived independently. The count-check cites the MEMBERSHIP block by name and confirms the count matches. A trace where G-1 is cleared at VC-4 without any reference to the MEMBERSHIP declarations fails this criterion. |
```
