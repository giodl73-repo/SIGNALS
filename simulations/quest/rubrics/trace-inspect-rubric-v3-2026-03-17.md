Scanning the R2 scorecard for patterns not yet captured in C-01 through C-13.

**New pattern extracted:**

- **V-04 C-11 × C-12 interaction**: When a remediation loop runs (C-12), the subsequent phase-entry gate-clearance summary (C-11) must reflect the post-remediation gate states, not the initial FAIL states. V-04 calls this out explicitly: "C-11's Phase 4 summary correctly reflects any remediation outcomes from C-12's loops." This is a cross-axis coherence property — each axis can pass in isolation yet the combined trace can still fail if the two blocks contradict each other. Not captured by C-11 (which only requires the summary to exist) or C-12 (which only requires the remediation record to exist).

This becomes **C-14**. No other pattern in R2 is distinct from existing criteria.

---

# Trace-Inspect Rubric — v3

**Skill**: `trace-inspect`
**Version**: v3 (updated from v2 — added C-14 from R2 excellence signals)
**Applies to**: Trace outputs produced by any variation of the trace-inspect skill
**Scoring**: 100-point composite. Golden threshold: all 5 essential criteria pass AND composite >= 80.

---

## Coverage Matrix

| Schema | Declared Elements | Invariant |
|--------|------------------|-----------|
| Schema 1 | Severity labels: {P1, P2, P3} | No other severity value anywhere in the trace |
| Schema 2 | Source labels: {SA, SG, EG, QO} | No other source value anywhere in the trace |
| Schema 3 | Lifecycle events: Stage 1 relay, SA-TO-SG PROMOTION, Stage 2 relay | Events occur in declared order |
| Schema 4 | Enforcement gates: G-1, G-2, G-3 | All three checked at Step 3c; no gate skipped |
| Schema 5 | Phase 3 sub-steps: 3a → 3b → 3c → 3d | Sub-steps run in declared order with transition confirmation |

---

## Essential Criteria

> All five must pass for the trace to be useful. A single essential failure makes the trace non-golden regardless of score.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Phase completeness** | essential | correctness | All four phases are present and structurally closed. Phase 1 (Setup) produces per-role schema binding blocks with explicit Schema 1 and Schema 2 binding fields and per-role gap attribution. Phase 2 (Execute) runs at least one role relay. Phase 3 (Findings) runs all four sub-steps in order (3a → 3b → 3c → 3d). Phase 4 (Amend) produces at least one change or dismissal entry. A trace missing any phase, or a phase present but producing no required output, fails. |
| C-02 | **Artifact produced** | essential | correctness | Phase 2 (Execute) writes a hand-compiled artifact file at `simulations/trace/skill/{topic}-skill-trace-{date}.md` (or equivalent declared path). The artifact contains every section the skill's artifact contract requires. An Execute phase that produces role relays without a written artifact fails. |
| C-03 | **Schema 1 + Schema 2 compliance** | essential | correctness | Every severity label used anywhere in the trace is from {P1, P2, P3}. Every Source label used anywhere in the trace is from {SA, SG, EG, QO}. A promoted SA gap uses the SG label in all phases after SA-TO-SG PROMOTION. Any label outside these sets, or a promoted gap retaining SA, is a structural violation and fails this criterion. |
| C-04 | **Enforcement gates checked** | essential | behavior | Step 3c records an explicit PASS or FAIL result for each of G-1, G-2, and G-3. G-1: >= 2 distinct Source types in Step 3b table. G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use only {P1, P2, P3}. A trace where any gate is omitted, implicitly assumed to pass, or advanced past despite a FAIL result fails this criterion. |
| C-05 | **Verdict present and classified** | essential | correctness | Phase 5 (or Verdict section) delivers one of three classifications: USEFUL, NEEDS-REDESIGN, or NEEDS-SPEC-REVISION, with the decision rationale. The classification follows the defined rules: NEEDS-SPEC-REVISION if any P1 SA gap remains SA after promotion; NEEDS-REDESIGN if EG gaps exceed 3 and indicate a structural role gap; USEFUL otherwise. A trace ending without a verdict, or with a verdict that contradicts the gap inventory, fails. |

---

## Recommended Criteria

> Output is better with these. Failing one degrades quality but does not make the trace useless.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **SA-TO-SG promotion evaluated** | recommended | depth | Every SA gap from the Stage 1 relay is evaluated at the SA-TO-SG PROMOTION lifecycle event. Each gap records PROMOTES TO SG or REMAINS SA with a one-sentence reason. The post-promotion inventory states SA remaining count and SG from promotion count. A trace with SA gaps that skip this evaluation, or where all SA gaps silently disappear without a promotion record, fails this criterion. |
| C-07 | **Per-role relays complete** | recommended | coverage | Each role in the execution sequence has a relay in Phase 2 with all required fields: Received from, Received values, Schema 2 compliance (Source labels used and YES/NO conformance), SA/SG gaps affecting this role, Produced (artifact content added), EG gaps encountered. A relay missing the "Schema 2 compliance" field, or a relay summarized as "role ran normally" without field-level detail, fails this criterion. |
| C-08 | **Findings table depth** | recommended | depth | The Step 3b findings table contains >= 3 distinct findings covering at least 2 different Source types. Each finding has a distinct Action (not a restatement of the finding). A table with only spec-layer (SA) findings or only execution-layer (EG) findings, or with Action cells that repeat the Finding text verbatim, fails this criterion. |

---

## Aspirational Criteria

> Raise the bar once essential and recommended are stable. C-09 and C-10 were present in v1. C-11, C-12, and C-13 were added in v2 from R1 excellence signals. C-14 is new in v3, extracted from the R2 V-04 cross-axis interaction.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Compliance ledger populated** | aspirational | correctness | Phase 5 includes the full VC compliance ledger (VC-1 through VC-5) with one row per usage site declared in the Coverage Matrix. The "Observed behavior" cell names specific values, label lists, or invariant results — it does not say "as expected." All VC overall results are stated. A trace with a verdict but no compliance ledger, or a ledger with generic "as expected" observations, fails this criterion. |
| C-10 | **Schema 5 sub-step transitions explicit** | aspirational | behavior | Each of the four Phase 3 sub-steps (3a, 3b, 3c, 3d) states its Schema 5 prerequisite and its Schema 5 transition sentence confirming the prerequisite was satisfied before the sub-step began. A trace that runs sub-steps without recording the transition (e.g., jumps from Step 3a directly to Step 3b content without stating "Step 3a complete, Step 3b is valid to begin") fails this criterion. |
| C-11 | **Phase-entry gate clearance summary** | aspirational | behavior | Before Step 3d begins and before Phase 4 begins, the trace records a consolidated gate-clearance summary that names all three gates and their results (e.g., "G-1 PASS, G-2 PASS, G-3 PASS — Phase 4 is valid to begin"). This is distinct from C-04, which requires individual gate results, and from C-10, which requires per-sub-step transition sentences. A trace where gates are individually recorded (satisfying C-04) but no consolidated entry-clearance summary appears at each phase boundary fails this criterion. |
| C-12 | **Gate-failure remediation loop documented** | aspirational | behavior | If any gate records a FAIL during Step 3c, the trace documents: (1) the specific remediation action taken (what was added, changed, or removed in Step 3b to resolve the failure), (2) a re-check of the gate after remediation, and (3) the updated gate result (PASS or FAIL). A trace that records a FAIL and proceeds without remediation, records a FAIL and simply stops, or transitions from FAIL to PASS without an explicit remediation entry fails this criterion. Traces where all three gates pass on first evaluation are exempt; the trace must emit an explicit "C-12 exemption applies" notice to confirm the exemption rather than relying on silence. |
| C-13 | **Sub-step prerequisite verification checkboxes** | aspirational | behavior | Each of the four Phase 3 sub-steps (3a, 3b, 3c, 3d) opens with an explicit prerequisite check in the form "Prerequisite: [stated condition]. Check: YES / NO" (or structurally equivalent). The YES resolution must name a specific artifact or row — a bare YES without a named referent is treated as a mechanical answer and fails. This is a stronger requirement than C-10: C-10 requires transition sentences after completion of the prior step; C-13 requires named-artifact verification before beginning the current step. A trace that satisfies C-10 but does not open each sub-step with an explicit named-artifact check fails this criterion. |
| C-14 | **Remediation-to-summary coherence** | aspirational | behavior | When one or more gates record a FAIL during Step 3c and a remediation loop is documented per C-12, the Phase 4 entry gate-clearance summary (C-11) must reflect the post-remediation gate states, not the initial evaluation states. A trace that documents a remediation loop resolving a FAIL to PASS but then records the original FAIL result in the consolidated Phase 4 summary fails this criterion — the two structural blocks must agree on the final state of each gate. Traces where C-12 is exempt (all gates pass on first evaluation) are also exempt from C-14. This criterion is only evaluable when both C-11 and C-12 are present; a trace failing either C-11 or C-12 is not evaluated for C-14. |

---

## Scoring Summary

| Tier | Criteria | Points available |
|------|----------|-----------------|
| Essential (all must pass) | C-01, C-02, C-03, C-04, C-05 | 60 |
| Recommended | C-06, C-07, C-08 | 30 |
| Aspirational | C-09, C-10, C-11, C-12, C-13, C-14 | 10 |

**Composite** = (essential_pass / 5 × 60) + (recommended_pass / 3 × 30) + (aspirational_pass / 6 × 10)

---

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial rubric — C-01 through C-10 |
| v2 | Added C-11, C-12, C-13 from R1 excellence signals (phase-entry summaries, remediation loops, prerequisite checkboxes) |
| v3 | Added C-14 from R2 V-04 cross-axis interaction (remediation-to-summary coherence) |
