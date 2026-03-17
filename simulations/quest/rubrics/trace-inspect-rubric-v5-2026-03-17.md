Scanning the R7 scorecard for patterns not yet captured in C-01 through C-21.

**New patterns extracted:**

Three distinct excellence properties appear in the R7 evidence notes that no existing criterion covers:

- **C-19 — EG-first structural role ordering**: V-04 achieves C-16 compliance architecturally by declaring that all EG-producing roles run before the SA-TO-SG PROMOTION lifecycle event. The note is explicit: "structural: EG roles always run before promotion evaluation → EVIDENCE-GROUNDED state is architectural default, not just a rule." V-01/V-03 satisfy C-16 through MUST/VIOLATION rule pairs — the author must comply; violation is possible. V-04 constrains the execution sequence so violation is structurally impossible. C-16 governs whether execution evidence is cited; C-19 governs whether the execution model guarantees evidence is always available before citation is needed.

- **C-20 — Inertia registry with explicit inheritance declaration**: V-05 C-10–C-14 evidence reads "Inherited and named in inertia registry"; C-06–C-08 reads "Inherited and reinforced by inertia framing." No other variant includes this mechanism. An explicit registry block names all prior-version criteria by ID and declares each as inherited — silence does not imply continuity. Without such a registry, a future version could silently drop a criterion and no structural element would surface the omission. Not captured by any existing criterion, which evaluate trace content; C-20 evaluates whether the skill version itself declares its inheritance chain.

- **C-21 — Attribution table co-located in compliance ledger**: V-05 C-09 evidence reads "C-17 attribution table wired directly into VC-4 G-1 row." V-02 achieves C-17 PASS and C-09 PASS through two structurally independent elements (standalone attribution table + separate ledger). V-05 embeds the attribution table as a pre-printed sub-structure of the VC-4 row. Both variants satisfy C-09 and C-17; only V-05 satisfies C-21. The co-location property makes filling the ledger and completing the attribution a single operation — the two cannot drift apart across executions.

These become C-19, C-20, C-21.

Scoring adjustment: with 13 aspirational criteria (C-09 through C-21): C-09 and C-10 remain at 2 pts each (4 pts); C-11 through C-21 at 0.5 pts each (5.5 pts). Total aspirational = 9.5 pts. Grand total = 99.5 pts; golden threshold unchanged at composite >= 80 with all essential passing.

---

```markdown
# Trace-Inspect Rubric — v5

**Skill**: `trace-inspect`
**Version**: v5 (updated from v4 — added C-19 through C-21 from R7 excellence signals;
aspirational weights redistributed: C-11 through C-21 each 0.5 pts; grand total 99.5)
**Applies to**: Trace outputs produced by any variation of the trace-inspect skill
**Scoring**: 99.5-point composite. Golden threshold: all 5 essential criteria pass AND
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
> R2 signals. C-15 through C-18 were added in v4 from R6 signals. C-19 through C-21 are new
> in v5, extracted from R7 excellence signals.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Compliance ledger populated** | 2 pts | correctness | Phase 5 includes the full VC compliance ledger (VC-1 through VC-5) with one row per usage site declared in the Coverage Matrix. The "Observed behavior" cell names specific values, label lists, or invariant results — it does not say "as expected." All VC overall results are stated. A trace with a verdict but no compliance ledger, or a ledger with generic "as expected" observations, fails this criterion. |
| C-10 | **Schema 5 sub-step transitions explicit** | 2 pts | behavior | Each of the four Phase 3 sub-steps (3a, 3b, 3c, 3d) states its Schema 5 prerequisite and its Schema 5 transition sentence confirming the prerequisite was satisfied before the sub-step began. A trace that runs sub-steps without recording the transition (e.g., jumps from Step 3a directly to Step 3b content without stating "Step 3a complete, Step 3b is valid to begin") fails this criterion. |
| C-11 | **Phase-entry gate-clearance summary** | 0.5 pts | behavior | Before Step 3d begins and before Phase 4 begins, the trace records a consolidated gate-clearance summary that names all three gates and their results (e.g., "G-1 PASS, G-2 PASS, G-3 PASS — Phase 4 is valid to begin"). This is distinct from C-04, which requires individual gate results, and from C-10, which requires per-sub-step transition sentences. A trace where gates are individually recorded (satisfying C-04) but no consolidated entry-clearance summary appears at each phase boundary fails this criterion. |
| C-12 | **Gate-failure remediation loop documented** | 0.5 pts | behavior | If any gate records a FAIL during Step 3c, the trace documents: (1) the specific remediation action taken (what was added, changed, or removed in Step 3b to resolve the failure), (2) a re-check of the gate after remediation, and (3) the updated gate result (PASS or FAIL). A trace that records a FAIL and proceeds without remediation, records a FAIL and simply stops, or transitions from FAIL to PASS without an explicit remediation entry fails this criterion. Traces where all three gates pass on first evaluation are exempt; the trace must emit an explicit "C-12 exemption applies" notice to confirm the exemption rather than relying on silence. |
| C-13 | **Sub-step prerequisite verification checkboxes** | 0.5 pts | behavior | Each of the four Phase 3 sub-steps (3a, 3b, 3c, 3d) opens with an explicit prerequisite check in the form "Prerequisite: [stated condition]. Check: YES / NO" (or structurally equivalent). The YES resolution must name a specific artifact or row — a bare YES without a named referent is treated as a mechanical answer and fails. This is a stronger requirement than C-10: C-10 requires transition sentences after completion of the prior step; C-13 requires named-artifact verification before beginning the current step. A trace that satisfies C-10 but does not open each sub-step with an explicit named-artifact check fails this criterion. |
| C-14 | **Remediation-to-summary coherence** | 0.5 pts | behavior | When one or more gates record a FAIL during Step 3c and a remediation loop is documented per C-12, the Phase 4 entry gate-clearance summary (C-11) must reflect the post-remediation gate states, not the initial evaluation states. A trace that documents a remediation loop resolving a FAIL to PASS but then records the original FAIL result in the consolidated Phase 4 summary fails this criterion — the two structural blocks must agree on the final state of each gate. Traces where C-12 is exempt (all gates pass on first evaluation) are also exempt from C-14. This criterion is only evaluable when both C-11 and C-12 are present; a trace failing either C-11 or C-12 is not evaluated for C-14. |
| C-15 | **Post-table findings FLOOR CHECK** | 0.5 pts | behavior | After the Step 3b findings table is written, the trace includes a structural FLOOR CHECK block that: (1) names every finding ID in the table explicitly (not just a count), (2) states the row count and confirms count >= 3, (3) lists every distinct Source type present and confirms the count >= 2, and (4) asserts Action uniqueness (no two rows share identical Action text). The FLOOR CHECK must emit a PASS or FAIL result. A FAIL result from the FLOOR CHECK must block Step 3c from proceeding. A trace that satisfies C-08 (the table content meets minimums) but does not include this post-table verification block fails this criterion. This is distinct from C-08, which governs table content; C-15 governs whether the trace explicitly verifies its own table content before advancing to gate evaluation. |
| C-16 | **Execution-evidence mandatory citation at SA-TO-SG promotion** | 0.5 pts | depth | At the SA-TO-SG PROMOTION lifecycle event, the trace declares an EVIDENCE CLASSIFICATION state for each gap evaluated: EVIDENCE-GROUNDED (execution has run and the gap was observed during relay) or SPEC-INFERENCE (no execution run; gap inferred from spec only). When execution has run, citing SPEC-INFERENCE is a structural violation. The promotion reason must be grounded in the EVIDENCE-GROUNDED observation, not a restatement of the spec gap. A trace that satisfies C-06 (promotion evaluated with a reason) but uses permissive "may cite execution evidence" language — or that cites SPEC-INFERENCE when execution evidence is available — fails this criterion. |
| C-17 | **G-1 cross-role attribution in compliance ledger** | 0.5 pts | correctness | The VC-4 compliance ledger row for G-1 includes a two-column attribution table structured as: Source type | Roles producing findings of that type. Each Source type represented in the Step 3b findings table must have a named row listing the specific roles whose relays contributed findings of that type. A prose summary in the VC-4 observation cell that mentions roles without a structured per-Source-type breakdown fails this criterion. This is an above-threshold precision property relative to C-09, which requires specific observations; C-17 requires that G-1's observation include structured cross-role traceability, not just a conformance assertion. |
| C-18 | **Remediation entry precision** | 0.5 pts | behavior | When a gate-failure remediation loop is documented per C-12, each remediation action entry must name the specific finding artifact affected: the finding ID, its Source type, and the exact Action text added or changed (e.g., "added F-04 (Source: EG, Action: add schema binding step for Role C)"). An entry that says "added a finding" or "changed the action" without naming the finding ID fails this criterion regardless of whether the table content is correct. This is an above-threshold precision property relative to C-12, which requires a specific remediation action; C-18 requires that the action entry include named artifact references sufficient to reconstruct what changed without re-reading the table. Traces where C-12 is exempt are also exempt from C-18. |
| C-19 | **EG-first structural role ordering** | 0.5 pts | behavior | The Phase 2 execution sequence explicitly places all EG-producing roles before the SA-TO-SG PROMOTION lifecycle event. The execution protocol declares this ordering as a structural constraint — not a recommendation — so that EVIDENCE-GROUNDED state at the promotion gate is an architectural default rather than a compliance obligation. A skill variation that satisfies C-16 (mandatory citation rule) through a MUST/VIOLATION obligation pair but does not constrain the role execution sequence fails C-19: the rule requires compliance, but the sequence permits violation if the author deviates. A variation that declares EG roles must precede the promotion gate — making it structurally impossible to reach the promotion event without execution evidence available — passes. This criterion is distinct from C-16, which governs what the citation must say; C-19 governs whether the execution model guarantees evidence exists before citation is needed. |
| C-20 | **Inertia registry for prior-version criteria** | 0.5 pts | behavior | The skill version includes an explicit inertia registry block that names all prior-version aspirational criteria by ID and declares each as inherited unchanged into the current version. Silence does not imply continuity: the absence of a registry entry for a given criterion ID is treated as a silent drop, not an inheritance. A skill version that omits this block fails this criterion regardless of whether the prior criteria are in fact present in the skill's body. The registry functions as a regression barrier: any future version that removes or modifies a prior criterion must explicitly update the registry, making the change visible and intentional. A registry entry that says "all prior criteria inherited" without naming individual IDs is treated as insufficient — each criterion must be named. |
| C-21 | **Attribution table co-located in compliance ledger** | 0.5 pts | correctness | The G-1 cross-role attribution table required by C-17 is structurally embedded within the VC-4 compliance ledger row as a pre-printed sub-structure, not maintained as a standalone block separate from the ledger. A trace that satisfies both C-09 (compliance ledger populated) and C-17 (attribution table present) through two structurally independent elements passes both criteria but fails C-21. The co-location property ensures that filling in the VC-4 ledger row and completing the attribution table are a single operation — the two cannot be completed in isolation or drift apart across executions. A trace where the attribution table appears outside the ledger structure (e.g., in a separate section before or after Phase 5) satisfies C-17 but fails C-21. This criterion is only evaluable when both C-09 and C-17 are present; a trace failing either C-09 or C-17 is not evaluated for C-21. |
```
