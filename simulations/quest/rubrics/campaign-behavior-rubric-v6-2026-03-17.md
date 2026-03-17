Reading the scorecard carefully for new Round 6 patterns before writing the updated rubric.

From the scorecard, two new excellence patterns emerge:

1. **V-03** introduces **state-anchor execution order** — trace-state runs first to pre-classify blast radius from shared-state topology before downstream sub-skills execute
2. **V-04** introduces **permissions-anchor position** — trace-permissions is positioned before the flow sub-skills so privilege boundary classification anchors flow analysis

These become **C-22** and **C-23**. Denominator bumps from 13 → 15.

---

```markdown
# Quest Rubric — campaign-behavior (org-review)
**Version:** v6
**Updated:** 2026-03-17
**Author:** Quest Engine

---

## Scoring Formula

| Tier         | Criteria                         | Max pts |
|--------------|----------------------------------|---------|
| Essential    | C-01–C-05 (10 pts each)          | 50      |
| Recommended  | C-06–C-08 (10 pts each)          | 30      |
| Aspirational | C-09–C-23 — (passed/15) × 10    | 10      |
| **Total**    |                                  | **90**  |

PASS = full credit. PARTIAL = half credit. FAIL = 0.
Aspirational tier is binary PASS/FAIL per criterion; score = (count passed / 15) × 10,
rounded to nearest integer.

---

## Essential Criteria (50 pts total)

### C-01 — All 5 sub-skills executed
- **Weight:** essential
- **Category:** coverage
- **Text:** The campaign runs all five sub-skills: trace-contract, trace-state,
  trace-permissions, flow-lifecycle, and flow-trigger. Partial execution invalidates
  blast radius ranking because findings from skipped sub-skills are absent.
- **Pass condition:** All five sub-skills are named in the output with evidence of
  execution (findings, tables, or explicit "none found" statements). Fewer than five
  named = FAIL.

---

### C-02 — Findings ranked by blast radius
- **Weight:** essential
- **Category:** correctness
- **Text:** The consolidated report presents findings ordered by blast radius
  (highest impact / widest system effect first). Blast radius is not interchangeable
  with severity or priority — it specifically captures how broadly a failure propagates
  across the system.
- **Pass condition:** Output includes a ranked findings list where ranking criterion is
  explicitly stated as blast radius (or equivalent: propagation scope, system-wide
  impact). Random order or severity-only ranking = FAIL.

---

### C-03 — Spec gaps identified or explicitly cleared
- **Weight:** essential
- **Category:** coverage
- **Text:** The report either names at least one spec gap found during the campaign, or
  explicitly states that no spec gaps were detected. A spec gap is a condition, state
  transition, or contract term that the spec does not address but the simulation exposes.
- **Pass condition:** Output contains a labeled "spec gaps" section (or equivalent
  heading) with findings or a clear "none found" statement. Omitting the section
  entirely = FAIL.

---

### C-04 — Contract violations surfaced or explicitly cleared
- **Weight:** essential
- **Category:** correctness
- **Text:** The report either names at least one contract violation found during the
  campaign, or explicitly states that no violations were detected. A contract violation
  is a producer/consumer mismatch, broken invariant, or privilege boundary crossed.
- **Pass condition:** Output contains a labeled "contract violations" section (or
  equivalent) with findings or a clear "none found" statement. Omitting the section
  entirely = FAIL.

---

### C-05 — Lifecycle violations surfaced or explicitly cleared
- **Weight:** essential
- **Category:** correctness
- **Text:** The report either names at least one lifecycle violation found during the
  campaign, or explicitly states that no violations were detected. A lifecycle violation
  is a state transition that contradicts the defined lifecycle sequence, a trigger
  fired outside its permitted phase, or a flow that exits without reaching a terminal
  state.
- **Pass condition:** Output contains a labeled "lifecycle violations" section (or
  equivalent) with findings or a clear "none found" statement. Omitting the section
  entirely = FAIL.

---

## Recommended Criteria (30 pts total)

### C-06 — Blast radius classification label per finding
- **Weight:** recommended
- **Category:** structure
- **Text:** Each finding in the consolidated output carries an explicit blast radius
  classification label: SYSTEMIC, ISOLATED, or LOCAL. The label is not inferred from
  the description — it is stated as a named field. This enables downstream sorting,
  filtering, and tiebreaker application without re-reading prose.
- **Pass condition:** Every finding in the consolidated list has a blast radius label.
  Any finding without a label = PARTIAL. No findings with labels = FAIL.

---

### C-07 — Confirmation status per finding
- **Weight:** recommended
- **Category:** structure
- **Text:** Each finding carries an explicit confirmation status: CONFIRMED or
  unconfirmed. CONFIRMED means the finding was corroborated by evidence from at least
  two sources or phases. Unconfirmed means it was observed once and requires further
  investigation. The distinction matters for prioritization and for applying the
  tiebreaker protocol (C-20).
- **Pass condition:** Every finding in the consolidated list has a confirmation status
  field. Any finding without status = PARTIAL. No findings with status = FAIL.

---

### C-08 — Sub-skill attribution per finding
- **Weight:** recommended
- **Category:** traceability
- **Text:** Each finding names the sub-skill (or sub-skills, for compound findings) that
  produced it. Attribution enables the reader to re-run only the relevant sub-skill
  when re-examining a finding, and identifies which sub-skills are generating the most
  signal.
- **Pass condition:** Every finding in the consolidated list names at least one
  originating sub-skill. Any finding without attribution = PARTIAL. No findings with
  attribution = FAIL.

---

## Aspirational Criteria (10 pts total — binary PASS/FAIL per criterion)

Score = (count passed / 15) × 10, rounded to nearest integer.

---

### C-09 — Finding ID in F-NN format
- **Category:** structure
- **Text:** Each finding is assigned a stable numeric ID in the format F-01, F-02, …
  F-NN. IDs are assigned in blast-radius order (F-01 = highest blast radius). Stable
  IDs allow findings to be cited in spec updates, scorecards, and follow-on campaigns
  without ambiguity.
- **Pass condition:** All findings carry F-NN IDs in blast-radius order.

---

### C-10 — Lifecycle phase tag per flow finding
- **Category:** traceability
- **Text:** Findings produced by flow-lifecycle and flow-trigger are tagged with the
  lifecycle phase in which the violation occurs (e.g., INIT, ACTIVE, SUSPENDED,
  TERMINAL). Phase tagging allows cross-campaign comparison and feeds into SYSTEMIC
  phase enumeration (C-21).
- **Pass condition:** All flow-lifecycle and flow-trigger findings carry a phase tag.

---

### C-11 — Cross-sub-skill compound findings identified
- **Category:** synthesis
- **Text:** Where a single failure mechanism spans multiple sub-skills (e.g., a contract
  violation that also produces a lifecycle violation), the finding is explicitly marked
  as compound and lists all originating sub-skills. Compound findings typically carry
  elevated blast radius because the failure mode propagates across domain boundaries.
- **Pass condition:** At least one compound finding is identified and labeled, or the
  output explicitly states "no compound findings detected."

---

### C-12 — Spec gap citations include missing clause
- **Category:** precision
- **Text:** Each spec gap finding names the specific condition, transition, or invariant
  that is absent from the spec — not just a description of the gap's effect. A citation
  such as "spec does not define behavior when role is revoked mid-session" is acceptable;
  "spec is incomplete" is not.
- **Pass condition:** Every spec gap finding includes a missing-clause citation.

---

### C-13 — Contract violation citations name producer and consumer
- **Category:** precision
- **Text:** Each contract violation finding names the producing component (the component
  whose output violates the contract) and the consuming component (the component that
  depends on the violated term). Naming both sides identifies the blast radius boundary
  and the remediation ownership.
- **Pass condition:** Every contract violation finding names both a producer and a
  consumer.

---

### C-14 — Privilege escalation paths enumerated
- **Category:** security
- **Text:** The trace-permissions sub-skill output explicitly lists any privilege
  escalation paths discovered — sequences of operations or state transitions that allow
  a role to acquire permissions not granted in the role definition. If none are found,
  the output explicitly states "no escalation paths detected."
- **Pass condition:** Output contains a labeled privilege escalation section with paths
  or an explicit "none found" statement.

---

### C-15 — Severity assigned using defined scale
- **Category:** correctness
- **Text:** Each finding carries a severity level drawn from a defined scale (e.g.,
  CRITICAL / HIGH / MEDIUM / LOW). The scale is stated in a definitions section so
  severity labels are applied consistently. Severity is a separate field from blast
  radius — blast radius measures propagation scope; severity measures impact intensity
  at the point of failure.
- **Pass condition:** All findings carry severity labels from a named scale defined in
  the output.

---

### C-16 — Executive summary with top-3 findings by blast radius
- **Category:** communication
- **Text:** The consolidated output opens with an executive summary that names the top 3
  findings by blast radius, their blast radius labels, and their confirmation status.
  The summary is self-contained — a reader can assess campaign risk without reading
  the full findings list.
- **Pass condition:** Executive summary present and names top 3 findings with blast
  radius and confirmation status.

---

### C-17 — Evidence basis declared per CONFIRMED finding
- **Category:** rigor
- **Text:** Each CONFIRMED finding states the evidence basis for its confirmation: which
  phases or sources corroborate it, and what the corroborating signal is. "CONFIRMED"
  without evidence basis is not verifiable and degrades the value of the tiebreaker
  protocol (C-20).
- **Pass condition:** Every CONFIRMED finding includes an evidence basis statement.

---

### C-18 — Q1–Qn interrogative calibration
- **Category:** calibration
- **Text:** The campaign prompt includes a numbered interrogative block (Q1 through Qn,
  where n ≥ 3) placed before or within the CONSOLIDATE step. Each question names a
  specific re-grounding target (a blast radius assumption, a spec term, a role boundary)
  and requires an explicit answer before the consolidated ranking is finalized.
  Interrogative calibration prevents ranking drift that occurs when the model anchors
  to early assumptions without re-examining them against the full finding set.
- **Pass condition:** Output contains a numbered Q1–Qn block; each question has a named
  re-grounding target and an explicit answer. Fewer than 3 questions or unanswered
  questions = FAIL.

---

### C-19 — Atomic 7-field finding block
- **Category:** structure
- **Text:** Each finding in the consolidated output is presented as a structured block
  with all 7 fields present: (1) Finding ID, (2) Sub-skill source, (3) Blast radius
  label, (4) Severity, (5) Confirmation status, (6) Description, (7) Remediation. The
  7 fields must appear together as a unit — scattering fields across prose sections
  makes tiebreaker application and cross-finding comparison unreliable.
- **Pass condition:** Every finding in the consolidated list presents all 7 fields in a
  contiguous block. Any finding missing one or more fields = FAIL for this criterion.

---

### C-20 — Tiebreaker protocol stated and applied
- **Category:** correctness
- **Text:** When two or more findings share the same blast radius classification, the
  output applies an explicit tiebreaker in this order: (1) CONFIRMED > unconfirmed,
  (2) SYSTEMIC > isolated. The tiebreaker protocol must be stated in a definitions
  section before it is applied — implicit tie-breaking does not satisfy this criterion.
- **Pass condition:** Tiebreaker protocol is stated (CONFIRMED > unconfirmed, SYSTEMIC
  > isolated) and visibly applied to at least one tied pair in the findings list. If no
  ties exist, the protocol must still be stated with a note that no ties were
  encountered.

---

### C-21 — SYSTEMIC flag includes enumerated phase list
- **Category:** precision
- **Text:** Any finding classified SYSTEMIC must include an inline enumeration of the
  corroborating phases — not a binary yes/no flag. The form is:
  `SYSTEMIC: yes — phases: [phase-A], [phase-B], [phase-C]`. A bare `SYSTEMIC: yes`
  without phase enumeration is insufficient because it does not establish the scope of
  propagation across the lifecycle.
- **Pass condition:** Every SYSTEMIC-classified finding carries an enumerated phase list
  in the prescribed format. Any SYSTEMIC finding with a binary flag only = FAIL for
  this criterion.

---

### C-22 — State-anchor execution order
- **Category:** sequencing
- **Text:** trace-state is designated as the first sub-skill to execute in the campaign
  sequence. State topology — which states are shared, which transitions are
  multi-party, which invariants span components — pre-classifies blast radius candidates
  for all downstream sub-skills. Running trace-state first means that contract tracing,
  permission tracing, and flow analysis inherit a pre-built blast radius map rather
  than constructing one post-hoc from individual sub-skill findings.
- **Pass condition:** Campaign instructions or output explicitly designate trace-state
  as the first sub-skill, with rationale that state topology pre-classifies blast radius
  for downstream sub-skills. Any other sub-skill executing first without explicit
  justification = FAIL.

---

### C-23 — Permissions-anchor position before flow sub-skills
- **Category:** sequencing
- **Text:** trace-permissions is positioned to execute before flow-lifecycle and
  flow-trigger. Privilege boundary classification must precede flow analysis because
  flow violations that cross privilege boundaries carry elevated blast radius — a flow
  that triggers across a permission boundary is SYSTEMIC by definition. Without
  permissions-anchor ordering, flow sub-skills may classify blast radius without
  visibility into privilege scope, understating propagation.
- **Pass condition:** Campaign instructions or output explicitly position
  trace-permissions before flow-lifecycle and flow-trigger, with rationale that
  privilege boundary classification anchors flow blast radius assessment. Flow
  sub-skills executing before trace-permissions without justification = FAIL.

---

## Changelog

| Version | Date       | Changes                                                                 |
|---------|------------|-------------------------------------------------------------------------|
| v6      | 2026-03-17 | Add C-22 (state-anchor order), C-23 (permissions-anchor); denominator 13→15 |
| v5      | 2026-03-17 | Add C-19 (atomic 7-field block), C-20 (tiebreaker protocol), C-21 (SYSTEMIC phase enumeration); denominator 10→13 |
| v4      | prior      | Add C-18 (Q1–Qn interrogative calibration); denominator 9→10            |
| v1–v3   | prior      | C-01–C-17 established                                                   |
```
