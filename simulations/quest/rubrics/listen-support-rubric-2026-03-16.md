# listen-support Rubric v2

**13 criteria total.** Golden = all essential pass + composite >= 80.

---

## Summary

### Essential (60 pts, 12 pts each — all must pass)

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-01 | Ticket field completeness | Every ticket has all 6 fields: title, category, persona, volume, severity, body |
| C-02 | Vocabulary validity | Category in {how-to, bug, feature-request, config, integration}; volume in {high, medium, low}; severity in {P0-P3} |
| C-03 | First-person persona voice | All ticket bodies written as "I" — no third-person role references, no appositive patterns ("I, as the SRE") |
| C-04 | Gap analysis three-axis coverage | Doc gaps + design gaps + operational gaps each present with >=1 entry |
| C-05 | Minimum ticket count | At least 5 distinct tickets predicted |

### Recommended (30 pts, 10 pts each)

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-06 | Phase distribution | Tickets span Day 0-30, 31-60, 61-90; Phase 1 >= 2 tickets, Phase 3 >= 1 ticket |
| C-07 | Phase-severity alignment | Phase 1 → P2/P3; Phase 3 blocking → P0/P1 (adoption-curve rule) |
| C-08 | Role diversity | >= 3 distinct roles from: Support, SRE, PM, UX, C-01..C-12 |

### Aspirational (25 pts, 5 pts each)

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-09 | Inertia competitor grounding | >= 1 body names prior tool concretely, frames friction as transition tension |
| C-10 | Vocabulary pre-commitment table | Metadata table before bodies; bodies can't diverge from table |
| C-11 | Phase as first-class ticket field | Each ticket metadata block includes an explicit Phase field (Phase 1/2/3); phase is declared, not inferred |
| C-12 | Fallback-grounded severity rationale | >= 1 ticket body explicitly connects severity to prior-tool fallback availability (Phase 1: "can still fall back" → P2/P3; Phase 3: "no longer available" → P0/P1) |
| C-13 | Mid-output verification block | Output contains a structured PASS/FAIL verification block — separate from ticket list and gap analysis — that tabulates phase distribution counts and role/persona diversity counts |

**Minimum path to Golden:** all 5 essential (60 pts) + all 3 recommended (30 pts) = 90 pts. Aspirational not required.

---

## Essential Criteria (60 points total)

5 criteria. Each criterion: 12 points (pass = 12, fail = 0). **All 5 must pass for Golden.**

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Ticket field completeness** | format | essential | Every ticket in the output has all 6 required fields present and non-empty: title, category, persona, volume, severity, body. A single ticket missing any field fails the criterion for the entire output. |
| C-02 | **Vocabulary validity** | format | essential | All field values use only valid tokens: category in {how-to, bug, feature-request, config, integration}; volume in {high, medium, low}; severity in {P0, P1, P2, P3}. Composite or non-standard values ("P2/P3", "medium-high") fail the criterion. |
| C-03 | **First-person persona voice** | correctness | essential | All ticket bodies are written in first person ("I"). Third-person role references ("the SRE", "they", "their") and appositive constructions ("I, as the SRE", "I (the PM)") both fail the criterion. The persona is inhabited, not described. |
| C-04 | **Gap analysis three-axis coverage** | coverage | essential | The gap analysis explicitly addresses all three axes: doc gaps, design gaps, and operational gaps -- each with at least one substantive entry. An output that omits any axis entirely fails the criterion. |
| C-05 | **Minimum ticket count** | coverage | essential | At least 5 distinct tickets are predicted. Outputs with fewer than 5 tickets fail the criterion regardless of individual ticket quality. |

---

## Recommended Criteria (30 points total)

3 criteria. Each criterion: 10 points (pass = 10, fail = 0).

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Phase distribution across 90-day window** | coverage | recommended | Tickets are distributed across all three adoption phases (Day 0-30, Day 31-60, Day 61-90) with at least 2 tickets in Phase 1 (initial onboarding) and at least 1 in Phase 3 (committed user). An output where all tickets cluster in a single phase fails the criterion. |
| C-07 | **Phase-severity alignment** | correctness | recommended | Severity assignments directionally follow the adoption-curve inference rule: Phase 1 tickets are generally P2/P3 (user has a fallback, still learning); Phase 3 tickets involving blocking scenarios are P0/P1 (user is committed, no fallback). A Phase 1 P0/P1 non-outage ticket or a Phase 3 P3 blocking ticket is a violation. At least 3 tickets must be inspectable against this rule. |
| C-08 | **Role diversity** | coverage | recommended | Tickets represent at least 3 distinct roles or personas drawn from the stock set (Support, SRE, PM, UX, or any of C-01 through C-12). An output where all tickets are attributed to the same role or persona fails the criterion. |

---

## Aspirational Criteria (25 points total)

5 criteria. Each criterion: 5 points (pass = 5, fail = 0).

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Inertia competitor grounding** | depth | aspirational | At least one ticket body names a specific prior tool or workflow the persona was using before adoption and frames the support trigger as a workflow-transition friction point -- not just a generic error or missing feature. The competing tool or prior workflow must be named concretely, not described generically as "previous tool" or "old solution". |
| C-10 | **Vocabulary pre-commitment table** | format | aspirational | A summary table declaring all ticket metadata (ID, title, category, persona, volume, severity) appears before any full ticket body is written. Bodies may not introduce field values that differ from the pre-committed table. This separates taxonomy decisions from prose execution. |
| C-11 | **Phase as first-class ticket field** | format | aspirational | Each ticket's structured metadata block includes an explicit Phase field (Phase 1, Phase 2, or Phase 3) alongside the standard 6 fields. Phase is a declared field value, not inferred from timing language in the body. This makes phase tracking happen at generation time and makes C-06/C-07 auditable per-ticket rather than by inference. |
| C-12 | **Fallback-grounded severity rationale** | depth | aspirational | At least one ticket body explicitly connects its severity choice to prior-tool fallback availability. A Phase 1 ticket references having a fallback ("I can still switch back to [prior tool]" → P2/P3) and/or a Phase 3 ticket references having no fallback ("I can no longer use [prior tool]" → P0/P1). Severity is derived from adoption position, not asserted. |
| C-13 | **Mid-output verification block** | format | aspirational | The output contains a structured verification block, separate from the ticket list and from the gap analysis, that explicitly tabulates: phase distribution counts by phase with PASS/FAIL judgment, and role/persona diversity count with PASS/FAIL judgment. The block appears after all tickets and before the gap analysis. |

---

## Scoring Reference

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 25)

Max composite: 115
Golden threshold: all C-01..C-05 pass AND composite >= 80
```

| Result | Meaning |
|--------|---------|
| All C-01..C-05 pass + composite >= 80 | Golden -- meets threshold |
| All C-01..C-05 pass + composite < 80 | Essential solid, weak on recommended/aspirational |
| Any C-01..C-05 fail | Below threshold regardless of composite score |

**Minimum path to Golden:** all 5 essential (60 pts) + all 3 recommended (30 pts) = 90 pts.
Aspirational not required for Golden.

**Round 1 reference scores (v2 formula):**

| Variant | Essential | Recommended | Aspirational | Composite | Golden |
|---------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/5 (48) | 1/3 (10) | 0/5 (0) | 58 | NO |
| V-02 | 5/5 (60) | 1/3 (10) | 0/5 (0) | 70 | NO |
| V-03 | 5/5 (60) | 3/3 (30) | C-09+C-11+C-12+C-13 (20) | 110 | YES |
| V-04 | 5/5 (60) | 3/3 (30) | C-09+C-11+C-12+C-13 (20) | 110 | YES |

*V-03/V-04 aspirational: C-09 (prior tool named), C-11 (Phase field in metadata), C-12 (fallback language in body), C-13 (STEP 4 verification block). C-10 failed in both — no pre-commitment table.*

---

## Criteria Ladder

Criteria are ordered by dependency where applicable:

- C-01 is the floor: no field present means nothing else is evaluable.
- C-02 depends on C-01: vocabulary can only be assessed if fields exist.
- C-03 extends C-01: body present (C-01) must also be in-persona (C-03).
- C-06 extends C-05: distribution only meaningful when count is sufficient.
- C-07 extends C-06: phase-severity alignment requires phase labels from C-06.
- C-10 extends C-01 + C-02: pre-commitment table only meaningful when field completeness and vocabulary validity are ensured.
- C-11 extends C-06: phase as a field only adds value when phase distribution is already being tracked (C-06).
- C-12 extends C-07 + C-09: fallback-grounded rationale requires both phase-severity alignment (C-07) and a named prior tool (C-09) to be meaningful.
- C-13 extends C-06 + C-08: a verification block only earns credit if the criteria it checks (phase distribution, role diversity) are themselves in scope.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-16 | Initial rubric — 10 criteria, max 100 pts |
| v2 | 2026-03-16 | Added C-11/C-12/C-13 from Round 1 excellence signals; aspirational bucket grows to 5 criteria × 5 pts = 25 pts; max composite 115 |
