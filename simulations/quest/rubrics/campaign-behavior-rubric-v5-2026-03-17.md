Looking at the scorecard evidence, I can identify three new patterns from Round 5 not captured by C-01 through C-18:

1. **V-02**: 7-field ranked finding as an atomic structured block (beyond C-06/C-07/C-08 which each cover one field in isolation)
2. **V-01**: Explicit ranking tiebreaker protocol — CONFIRMED > unconfirmed, SYSTEMIC > isolated — as secondary/tertiary sort keys beyond blast radius
3. **V-02**: SYSTEMIC flag includes the enumerated corroborating phase list, not just a binary yes/no

These become C-19, C-20, C-21. Aspirational denominator bumps from 10 to 13.

---

```markdown
# Quest Rubric — campaign-behavior (org-review)
**Version:** v5
**Updated:** 2026-03-17
**Author:** Quest Engine

---

## Scoring Formula

| Tier         | Criteria                         | Max pts |
|--------------|----------------------------------|---------|
| Essential    | C-01–C-05 (10 pts each)          | 50      |
| Recommended  | C-06–C-08 (10 pts each)          | 30      |
| Aspirational | C-09–C-21 — (passed/13) × 10    | 10      |
| **Total**    |                                  | **90**  |

PASS = full credit. PARTIAL = half credit. FAIL = 0.
Aspirational tier is binary PASS/FAIL per criterion; score = (count passed / 13) × 10,
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

### C-05 — Single consolidated report
- **Weight:** essential
- **Category:** form
- **Text:** The campaign produces one unified report — not five phase outputs
  concatenated. The consolidated report synthesizes across phases; raw phase output
  appended in sequence is not synthesis.
- **Pass condition:** Output is a single document with a consolidation section that
  integrates findings across phases. Five separate phase blocks with no synthesis = FAIL.

---

## Recommended Criteria (30 pts total)

### C-06 — Source attribution per finding
- **Weight:** recommended
- **Category:** traceability
- **Text:** Each ranked finding names the sub-skill phase that produced it. Attribution
  makes findings auditable and lets reviewers verify the evidence chain.
- **Pass condition:** Every ranked finding includes a source field naming the originating
  phase (e.g., "Source: trace-permissions"). Findings without source = FAIL.

---

### C-07 — Remediation hint per finding
- **Weight:** recommended
- **Category:** actionability
- **Text:** Each ranked finding includes a concrete fix direction — one specific change
  to the spec, contract, or implementation. Generic advice ("fix the bug") does not
  qualify.
- **Pass condition:** Every ranked finding includes a "What must change:" field with
  a concrete, targeted action. Vague or absent remediation = FAIL.

---

### C-08 — Severity explicit per finding
- **Weight:** recommended
- **Category:** correctness
- **Text:** Each ranked finding carries an explicit severity rating at the epicenter
  (high / med / low). Severity measures local damage intensity; it is not blast radius.
- **Pass condition:** Every ranked finding includes a severity field with one of three
  named values. Missing or implied severity = FAIL.

---

## Aspirational Criteria (C-09–C-21)

Score = (count passed / 13) × 10, rounded to nearest integer.

---

### C-09 — SYSTEMIC findings elevated
- **Category:** synthesis
- **Text:** Findings that recur across three or more phases are marked SYSTEMIC and
  ranked above isolated findings of equivalent blast radius. SYSTEMIC status signals
  architectural root cause rather than local defect.
- **Pass condition:** Output distinguishes SYSTEMIC from isolated findings and uses
  that distinction as a ranking input. No SYSTEMIC distinction = FAIL.

---

### C-10 — Verdict names component
- **Category:** precision
- **Text:** The campaign verdict (final summary statement) names the specific component
  carrying the widest blast radius by its census component name. Vague verdicts ("the
  system has risk") do not qualify.
- **Pass condition:** Verdict contains at least one named component from the topology
  census and states why it carries the widest blast radius. Generic verdict = FAIL.

---

### C-11 — Blast radius expressed via component names
- **Category:** precision
- **Text:** Every blast radius claim references named census components. A finding that
  cannot name a specific component from the topology inventory is ungrounded and must
  be returned to the spec. "Affects many components" without names = FAIL.
- **Pass condition:** Every blast radius field (or equivalent) enumerates at least one
  named census component. Unnamed/implied blast radius = FAIL.

---

### C-12 — Sub-skill typed schemas
- **Category:** structure
- **Text:** Each of the five sub-skills uses a distinct column vocabulary appropriate
  to that skill's domain (e.g., Role/Resource/Action for permissions; State/Invariant
  for state; Producer/Consumer for contracts; Phase/Entry/Exit for lifecycle;
  Trigger/Race for flow-trigger). A single generic schema applied to all five = FAIL.
- **Pass condition:** Five distinguishable column vocabularies present, one per
  sub-skill. Generic or shared schemas = FAIL.

---

### C-13 — Severity and blast radius kept distinct
- **Category:** correctness
- **Text:** Severity (local damage intensity at the epicenter) and blast radius
  (propagation width across the system) appear as separate, explicitly labeled fields.
  Merging them into a single "impact" score destroys the analytical value of both.
- **Pass condition:** Both fields present and labeled distinctly in every ranked
  finding. Merged or conflated = FAIL.

---

### C-14 — Calibration block
- **Category:** rigor
- **Text:** A named calibration block appears after all five phase outputs and before
  the consolidated report. It re-grounds blast radius claims by revisiting the access
  surface inventory and shared state identified in Phase 0, and re-assesses any
  findings that changed meaning across phases.
- **Pass condition:** Named calibration section present, positioned between phases and
  consolidation, containing at least re-grounding against Phase 0 census. Absent or
  mispositioned = FAIL.

---

### C-15 — Phase 0 topology census
- **Category:** rigor
- **Text:** A pre-execution topology census (Phase 0) catalogs all components,
  roles, and shared state before any sub-skill runs. This census is the reference
  inventory for blast radius amplifier identification throughout all phases.
- **Pass condition:** Named Phase 0 (or equivalent) present before any phase output,
  containing a component/role inventory. Absent = FAIL.

---

### C-16 — Per-phase exit criteria
- **Category:** completeness
- **Text:** Each of the five phases carries explicit EXIT CRITERIA with affirmative
  clean-state declarations (e.g., "trace-permissions: clean — no escalation paths
  detected"). Exit criteria gate phase completion and prevent silent partial execution.
- **Pass condition:** All five phases include named exit criteria with affirmative or
  finding-anchored closure statements. Any phase without exit criteria = FAIL.

---

### C-17 — CONFIRMED distinction
- **Category:** evidence quality
- **Text:** Runtime findings are classified CONFIRMED when cross-referenced against
  contract topology findings from a prior phase. CONFIRMED findings carry stronger
  evidence weight than single-phase findings and are ranked above unconfirmed findings
  of equal blast radius.
- **Pass condition:** CONFIRMED classification present in calibration or consolidation;
  used as a ranking input. No CONFIRMED distinction = FAIL.

---

### C-18 — Q1–Qn interrogative calibration
- **Category:** rigor
- **Text:** Calibration is structured as a numbered interrogative sequence (Q1, Q2,
  Q3 … Qn) rather than a prose block or phase re-statement. Each question targets a
  specific re-grounding concern (e.g., "Q1: Does any finding's blast radius change
  when we account for shared state identified in Phase 0?"). This form makes
  calibration gaps visible and auditable.
- **Pass condition:** Calibration section contains at least three numbered Q-form
  questions with explicit answers. Prose-only or phase-block calibration = FAIL.

---

### C-19 — Ranked finding atomic schema
- **Category:** structure
- **Text:** Each ranked finding is presented as a complete, numbered multi-field block
  containing all required fields together (minimum: name, source phase, blast radius,
  severity, SYSTEMIC flag, remediation). Findings presented as prose paragraphs or
  as partial inline annotations with some fields missing break the atomic contract and
  make cross-finding comparison unreliable.
- **Pass condition:** Every ranked finding uses a consistent numbered-field block
  structure with all six minimum fields present for each finding. Prose findings or
  partial field sets = FAIL.

---

### C-20 — Blast radius ranking tiebreaker protocol
- **Category:** correctness
- **Text:** The ranking protocol specifies explicit secondary and tertiary sort keys
  for findings with equal blast radius. Required tiebreaker order: (1) blast radius
  descending, (2) CONFIRMED > unconfirmed, (3) SYSTEMIC > isolated. Without explicit
  tiebreaker rules, ranking is arbitrary for tied findings and cannot be reproduced
  or audited.
- **Pass condition:** Ranking section explicitly states secondary and tertiary sort
  keys matching (or superseding) CONFIRMED > unconfirmed and SYSTEMIC > isolated.
  Blast-radius-only ranking with no tiebreaker = FAIL.

---

### C-21 — SYSTEMIC phase enumeration
- **Category:** evidence quality
- **Text:** SYSTEMIC findings enumerate the specific corroborating phases by name
  (e.g., "SYSTEMIC: yes — phases: trace-contract, flow-lifecycle") rather than a
  binary yes/no flag. Phase enumeration makes the cross-phase evidence chain auditable
  and distinguishes a finding corroborated by two phases from one corroborated by all
  five.
- **Pass condition:** Every SYSTEMIC-flagged finding includes the list of corroborating
  phase names. Binary SYSTEMIC flag without phase list = FAIL.

---

## Changelog

| Version | Date       | Changes |
|---------|------------|---------|
| v1      | 2026-03-14 | Initial rubric — C-01–C-08 |
| v2      | 2026-03-14 | Added aspirational tier C-09–C-11 |
| v3      | 2026-03-15 | Added C-12–C-14 from R3 patterns |
| v4      | 2026-03-17 | Added C-15–C-18 from R4/R5 patterns; aspirational denominator 10 |
| v5      | 2026-03-17 | Added C-19–C-21 from R5 patterns; aspirational denominator 13 |
```

---

Three new criteria added:

- **C-19** captures the V-02 pattern of treating each ranked finding as an atomic 6+ field block, not individual annotations scattered across prose
- **C-20** captures the V-01 tiebreaker chain — the ranking rule is incomplete without secondary/tertiary keys for equal blast-radius findings
- **C-21** captures the V-02 SYSTEMIC field that names corroborating phases — distinguishes "3 of 5 phases agree" from "2 of 5 agree," which the binary flag can't express
