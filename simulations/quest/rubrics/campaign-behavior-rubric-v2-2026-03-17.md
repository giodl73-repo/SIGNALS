v2 written. Here's what was added and why:

---

**C-11 — Blast radius operationalized in output** (correctness)
V-02 and V-04 both anchored blast radius to concrete system terms ("how many components or users break," "corrupts shared state"). Without this, C-02 passes on the word "blast radius" but the ranking is unverifiable by a cold reviewer. C-11 rewards the extra step of making the criterion legible in-context.

**C-12 — Per-sub-skill schema typed to sub-skill purpose** (format)
V-04 used different column schemas per sub-skill (trace-contract: Expected/Actual/Violation; flow-lifecycle: Phase/Trigger/Outcome). A uniform Source/Finding/Remediation template applied to all five forces heterogeneous findings into mismatched columns and obscures sub-skill-specific signal. Pass condition requires at least 3 of 5 sub-skills use vocabulary-appropriate schemas.

**C-13 — Severity x blast radius co-located as distinct fields** (depth)
The root cause of C-08 failures in V-01 and V-03: both used blast radius rationale as a proxy for severity, leaving no epicenter intensity signal. V-02 and V-04 placed Severity as an explicit column *alongside* blast radius rationale. This criterion is intentionally stricter than C-08 — C-08 only requires severity to exist somewhere; C-13 requires it to coexist with blast radius on the same finding row so two-dimensional triage is possible in one scan.

**Scoring formula:** unchanged. N_aspirational goes from 2 to 5, so max aspirational contribution remains 10 pts — the denominator auto-adjusts per the formula.
nts findings ordered by blast radius
  (highest impact / widest system effect first). Blast radius is not interchangeable with
  severity or priority — it specifically captures how broadly a failure propagates across
  the system.
- **Pass condition:** Output includes a ranked findings list where ranking criterion is
  explicitly stated as blast radius (or equivalent: propagation scope, system-wide impact).
  Random order or severity-only ranking = FAIL.

---

### C-03 — Spec gaps identified or explicitly cleared
- **Weight:** essential
- **Category:** coverage
- **Text:** The report either names at least one spec gap found during the campaign, or
  explicitly states that no spec gaps were detected. A spec gap is a condition, state
  transition, or contract term that the spec does not address but the simulation exposes.
- **Pass condition:** Output contains a labeled "spec gaps" section (or equivalent heading)
  with findings or a clear "none found" statement. Omitting the section entirely = FAIL.

---

### C-04 — Contract violations surfaced or explicitly cleared
- **Weight:** essential
- **Category:** coverage
- **Text:** The report either names at least one contract violation (expected vs actual
  mismatch between components) or explicitly states that no violations were found. Contract
  violations come primarily from trace-contract but may surface in any sub-skill.
- **Pass condition:** Output contains a labeled "contract violations" section (or
  equivalent) with findings or a clear "none found" statement. Omitting the section = FAIL.

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
- **Text:** Each finding in the consolidated report names the sub-skill that produced it
  (e.g., "trace-state: missing rollback precondition"). Attribution allows the reader to
  know which simulation surface the finding came from.
- **Pass condition:** At least 80% of findings carry a sub-skill attribution tag or label.

---

### C-07 — Actionable remediation hint per finding
- **Weight:** recommended
- **Category:** depth
- **Text:** Each finding includes a short actionable hint describing what must change in
  the spec, contract, or implementation to resolve it. Hints need not be exhaustive — one
  clear direction per finding suffices.
- **Pass condition:** At least 70% of findings include a remediation hint or "fix direction"
  beyond restating the problem.

---

### C-08 — Severity or confidence annotation per finding
- **Weight:** recommended
- **Category:** depth
- **Text:** Each finding carries a severity tier (high/medium/low) or confidence level
  distinct from blast radius rank. Blast radius answers "how wide"; severity answers
  "how bad at the epicenter".
- **Pass condition:** Findings table or list includes a severity or confidence column/tag.
  Absent on 50%+ of findings = FAIL for this criterion.

---

## Aspirational Criteria (10 pts total)

### C-09 — Cross-skill pattern detection
- **Weight:** aspirational
- **Category:** depth
- **Text:** The report identifies findings that recur across two or more sub-skills as
  systemic issues (e.g., a missing state guard that trace-state flags AND trace-contract
  flags independently). Systemic findings are called out as higher-priority than isolated
  findings.
- **Pass condition:** At least one finding is explicitly labeled as cross-skill / systemic,
  with the contributing sub-skills named.

---

### C-10 — Implementation readiness verdict
- **Weight:** aspirational
- **Category:** behavior
- **Text:** The report closes with an explicit go / conditional-go / no-go verdict for
  implementation, with a one-sentence rationale citing the highest-blast-radius finding
  (or its absence). This turns the campaign from an informational artifact into a
  decision gate.
- **Pass condition:** Output ends with a clearly labeled verdict (go / conditional-go /
  no-go) and a rationale sentence. Missing or ambiguous verdict = FAIL for this criterion.

---

### C-11 — Blast radius operationalized in output
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The output includes an operational definition of blast radius as applied to
  the system under review — naming what propagates (downstream components, shared state,
  user-visible surfaces, dependent consumers) and how scope was estimated for this
  specific system. Without an anchored definition, readers cannot interpret relative ranks
  or compare findings across campaigns. C-02 can pass without this; C-11 rewards the
  extra step of making the ranking legible to a cold reviewer.
- **Pass condition:** The ranked findings section or an adjacent definition block states
  what blast radius measures for this system in one or two concrete terms. A generic
  restatement of "how broadly a failure propagates" with no system-specific grounding
  does not satisfy this criterion.
- **Excellence signal source:** R1 — V-02 ("Blast radius = how broadly a failure
  propagates across the system") and V-04 ("how many components or users break...
  corrupts shared state") scored 100; V-01 deferred the definition to the end of the
  prompt; V-03 embedded it inline with no structural anchor.

---

### C-12 — Per-sub-skill schema typed to sub-skill purpose
- **Weight:** aspirational
- **Category:** format
- **Text:** The per-sub-skill output sections use column schemas appropriate to what each
  sub-skill surfaces rather than a single uniform template applied to all five. Examples:
  trace-contract findings carry Expected / Actual / Violation columns; trace-state
  findings carry State / Transition / Precondition columns; flow-lifecycle findings carry
  Phase / Trigger / Outcome columns. A typed schema makes each section easier to scan and
  prevents force-fitting heterogeneous findings into mismatched columns.
- **Pass condition:** At least three of the five sub-skill output sections use a schema
  with column names that reflect the vocabulary of that sub-skill. A uniform
  Source/Finding/Blast-Radius/Remediation template applied identically to all five
  sub-skills does not satisfy this criterion even if the content is good.
- **Excellence signal source:** R1 — V-04 (combo trace-first + table-dominant) used typed
  schemas per sub-skill and was the only variant to score 100 on both C-08 and C-09
  without relying on format scaffolding alone.

---

### C-13 — Severity x blast radius co-located as distinct fields per finding
- **Weight:** aspirational
- **Category:** depth
- **Text:** Each finding in the consolidated report carries both a severity tier
  (high/med/low at the failure epicenter) and a blast radius rationale (propagation scope)
  as adjacent, visually distinct fields in the same row or block. The two dimensions are
  orthogonal: a finding can be low-severity but wide-blast (a silent default that
  silently breaks many consumers) or high-severity but narrow-blast (a crash in one
  isolated path). Co-locating both on one row enables two-dimensional triage in a single
  scan. Merging them into one field, or carrying only one, does not satisfy this criterion
  even if C-08 passes.
- **Pass condition:** The consolidated findings table or list contains clearly labeled,
  non-merged severity and blast radius fields for each finding. Either field absent or
  both fields collapsed into a single "impact" label = FAIL for this criterion.
- **Excellence signal source:** R1 — C-08 failures in V-01 and V-03 both resulted from
  templates that used blast radius rationale as a proxy for severity. V-02 and V-04
  avoided the failure by placing Severity as an explicit column alongside blast radius
  rationale. This criterion rewards that structural choice.

---

## Criterion Summary Table

| ID   | Text (short)                             | Weight       | Category    |
|------|------------------------------------------|--------------|-------------|
| C-01 | All five sub-skills executed             | essential    | correctness |
| C-02 | Findings ranked by blast radius          | essential    | correctness |
| C-03 | Spec gaps identified or cleared          | essential    | coverage    |
| C-04 | Contract violations surfaced/cleared     | essential    | coverage    |
| C-05 | Consolidated report, not five dumps      | essential    | format      |
| C-06 | Per-finding source attribution           | recommended  | depth       |
| C-07 | Actionable remediation hint per finding  | recommended  | depth       |
| C-08 | Severity/confidence annotation           | recommended  | depth       |
| C-09 | Cross-skill systemic pattern called out  | aspirational | depth       |
| C-10 | Implementation readiness verdict         | aspirational | behavior    |
| C-11 | Blast radius operationalized in output   | aspirational | correctness |
| C-12 | Per-sub-skill schema typed to purpose    | aspirational | format      |
| C-13 | Severity x blast radius co-located       | aspirational | depth       |

---

## Scoring Example

All essential pass, 2/3 recommended pass, 3/5 aspirational pass:

```
composite = (5/5 * 60) + (2/3 * 30) + (3/5 * 10)
          = 60 + 20 + 6
          = 86  -> golden threshold met (>=80, all essential pass)
```

All essential pass, 3/3 recommended pass, 5/5 aspirational pass (perfect):

```
composite = (5/5 * 60) + (3/3 * 30) + (5/5 * 10)
          = 60 + 30 + 10
          = 100
```
