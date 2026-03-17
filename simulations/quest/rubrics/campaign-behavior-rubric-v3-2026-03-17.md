Looking at the scorecard, V-03 introduces a structural pattern not yet captured by any criterion: the **CALIBRATION BLOCK** — a named synthesis phase inserted between sub-skill execution and consolidation, which re-grounds blast radius in actual findings rather than pre-declared topology. This is distinct from C-11 (which is an *output* criterion — did blast radius end up concrete?) because it specifies a *process architecture* mechanism that produces that outcome reliably.

No other genuinely novel patterns appear in the available scoring data. V-04's combo of C-11 + C-12 is a combination, not a new criterion.

---

```markdown
# Quest Rubric — campaign-behavior (org-review)
**Version:** v3
**Updated:** 2026-03-17
**Author:** Quest Engine

---

## Scoring Formula

| Tier        | Criteria          | Max pts |
|-------------|-------------------|---------|
| Essential   | C-01–C-05 (10 pts each) | 50 |
| Recommended | C-06–C-08 (10 pts each) | 30 |
| Aspirational | C-09–C-14 — (passed/6) × 10 | 10 |
| **Total**   |                   | **90** |

PASS = full credit. PARTIAL = half credit. FAIL = 0.
Aspirational tier is binary PASS/FAIL per criterion; score = (count passed / 6) × 10,
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
- **Category:** coverage
- **Text:** The report either names at least one contract violation (expected vs actual
  mismatch between components) or explicitly states that no violations were found.
  Contract violations come primarily from trace-contract but may surface in any
  sub-skill.
- **Pass condition:** Output contains a labeled "contract violations" section (or
  equivalent) with findings or a clear "none found" statement. Omitting the section
  = FAIL.

---

### C-05 — Consolidated report (not five independent outputs)
- **Weight:** essential
- **Category:** format
- **Text:** The output is a single unified findings report, not a concatenation of five
  separate skill outputs. Findings from different sub-skills should be synthesized —
  cross-referenced where they reinforce or contradict each other.
- **Pass condition:** Output reads as one coherent document with a summary section and
  integrated findings. A raw dump of five separate outputs with no synthesis = FAIL.

---

## Recommended Criteria (30 pts total)

### C-06 — Per-finding source attribution
- **Weight:** recommended
- **Category:** depth
- **Text:** Each finding in the consolidated report names the sub-skill that produced
  it (e.g., "trace-state: missing rollback precondition"). Attribution allows the
  reader to know which simulation surface the finding came from.
- **Pass condition:** At least 80% of findings carry a sub-skill attribution tag or
  label.

---

### C-07 — Actionable remediation hint per finding
- **Weight:** recommended
- **Category:** depth
- **Text:** Each finding includes a short actionable hint describing what must change
  in the spec, contract, or implementation to resolve it. Hints need not be exhaustive
  — one clear direction per finding suffices.
- **Pass condition:** At least 70% of findings include a remediation hint or "fix
  direction" beyond restating the problem.

---

### C-08 — Severity explicit per finding
- **Weight:** recommended
- **Category:** depth
- **Text:** Each finding carries an explicit severity rating (HIGH / MED / LOW or
  equivalent scale) representing intensity at the epicenter — independent of how
  broadly the failure propagates (that is blast radius). The two dimensions are
  complementary, not substitutes.
- **Pass condition:** At least 70% of findings carry an explicit severity label.
  Using blast radius rationale as a proxy for severity without a discrete severity
  field = FAIL.

---

## Aspirational Criteria (10 pts total — binary per criterion)

Score = (criteria passed / 6) × 10, rounded to nearest integer.

---

### C-09 — Systemic findings cross-referenced
- **Category:** depth
- **Text:** Findings corroborated by two or more sub-skills are explicitly flagged as
  SYSTEMIC (or equivalent). Cross-sub-skill corroboration signals design-level rather
  than implementation-level defects and should be surfaced prominently.
- **Pass condition:** Output contains at least one SYSTEMIC flag, or explicitly states
  that no cross-sub-skill corroboration was found.

---

### C-10 — Verdict names top finding by component
- **Category:** correctness
- **Text:** The closing verdict or summary section names the single highest-blast-radius
  finding and identifies the specific component (or shared state surface) at the
  epicenter. A verdict that only names an abstract risk category without anchoring to a
  concrete system artifact is insufficient.
- **Pass condition:** Verdict section names both (a) the finding and (b) the component
  or shared state surface it originates from.

---

### C-11 — Blast radius operationalized in output
- **Category:** correctness
- **Text:** Blast radius is expressed in concrete system terms within the output — naming
  specific components, shared state surfaces, or user populations affected — rather than
  generic language ("widespread," "significant"). Concrete grounding makes the ranking
  independently verifiable by a cold reviewer who was not present for the campaign.
- **Pass condition:** At least one finding explicitly names which component or shared
  state surface defines the blast radius boundary. Generic-only language = FAIL.

---

### C-12 — Per-sub-skill schema typed to sub-skill purpose
- **Category:** format
- **Text:** Each sub-skill section uses a column schema whose vocabulary matches the
  sub-skill's analytical purpose rather than a uniform generic template. Examples:
  trace-contract → Expected/Actual/Violation; flow-lifecycle → Phase/Trigger/Outcome;
  trace-permissions → Principal/Required/Actual. Forcing heterogeneous findings into a
  single Source/Finding/Remediation schema obscures sub-skill-specific signal.
- **Pass condition:** At least 3 of 5 sub-skills use a column schema whose headers are
  drawn from that sub-skill's vocabulary. Uniform schema across all five = FAIL.

---

### C-13 — Severity × blast radius co-located as distinct fields
- **Category:** depth
- **Text:** On each finding row, severity (epicenter intensity) and blast radius
  (propagation scope) appear as distinct labeled fields so two-dimensional triage is
  possible in a single scan. This criterion is intentionally stricter than C-08: C-08
  only requires severity to exist somewhere in the output; C-13 requires it to coexist
  with blast radius on the same finding row.
- **Pass condition:** At least 70% of findings carry both a severity label and a blast
  radius statement as distinct fields on the same row. Severity buried in prose or
  blast radius relegated to a separate section = FAIL.

---

### C-14 — Calibration block as named synthesis phase
- **Category:** process
- **Text:** Between sub-skill execution and final consolidation, a named CALIBRATION
  (or equivalent synthesis) phase explicitly re-evaluates and grounds blast radius
  assignments against the actual findings collected — not against pre-declared topology
  or generic definitions. The calibration block prevents the ranking step from operating
  on impact language that was declared before evidence was gathered. This criterion
  captures process architecture; C-11 captures the output outcome. A campaign can pass
  C-11 via pre-execution census (V-01 pattern) or via post-execution calibration
  (V-03 pattern) — C-14 specifically rewards the post-execution calibration variant.
- **Pass condition:** Output or prompt structure contains a named calibration or
  re-grounding phase after sub-skill execution that produces or revises blast radius
  assignments from collected findings before the ranking step runs.

---

## Version History

| Version | Changes |
|---------|---------|
| v1 | C-01–C-05 essential, C-06–C-08 recommended |
| v2 | Added C-09–C-13 aspirational; N_aspirational = 5 |
| v3 | Added C-14 (calibration block as named synthesis phase) from V-03 excellence signal; N_aspirational = 6 |
```

---

**What's new in v3 and why:**

**C-14 — Calibration block as named synthesis phase** (process)
V-03 introduced a structural phase between execution and consolidation that re-grounds blast radius in actual findings. This is the mechanism that makes C-11 reliable under conditions where no pre-execution topology census is available. Without C-14, two routes to passing C-11 exist (pre-execution census and post-execution calibration) but only V-01's route is structurally rewarded. C-14 creates a distinct reward signal for the evidence-driven grounding pattern. The `**Why different from C-11:**` distinction is explicit in the criterion text: C-11 is the output criterion; C-14 is the process criterion.

**Scoring formula:** N_aspirational increases from 5 to 6, so the denominator auto-adjusts. The maximum aspirational contribution remains 10 pts.
