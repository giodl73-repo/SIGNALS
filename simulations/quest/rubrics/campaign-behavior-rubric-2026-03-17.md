```markdown
---
skill: quest-rubric
skill_target: campaign-behavior
date: 2026-03-17
version: 1
---

# Scoring Rubric: campaign-behavior

**Skill purpose:** Orchestrates five technical simulation sub-skills (flow-lifecycle,
flow-conversation, trace-state, trace-contract, trace-permissions) in sequence and
produces a consolidated findings report ranked by blast radius — used before
implementation to surface spec gaps and contract violations.

---

## Scoring Formula

```
composite = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
```

**Golden threshold:** all essential criteria pass AND composite >= 80.

---

## Essential Criteria (60 pts total, must all pass)

### C-01 — All five sub-skills executed
- **Weight:** essential
- **Category:** correctness
- **Text:** The output demonstrates that all five sub-skills ran: flow-lifecycle,
  flow-conversation, trace-state, trace-contract, trace-permissions. Each must contribute
  at least one finding, observation, or explicit "no findings" declaration.
- **Pass condition:** Output contains a clearly attributed section or result block for
  each of the five sub-skills. A sub-skill may be marked clean/no-findings, but it must
  be present. Missing any sub-skill = FAIL.

---

### C-02 — Findings ranked by blast radius
- **Weight:** essential
- **Category:** correctness
- **Text:** The consolidated findings report presents findings ordered by blast radius
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
  separate skill outputs. Findings from different sub-skills should be synthesized — cross-
  referenced where they reinforce or contradict each other.
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

## Criterion Summary Table

| ID   | Text (short)                          | Weight        | Category    |
|------|---------------------------------------|---------------|-------------|
| C-01 | All five sub-skills executed          | essential     | correctness |
| C-02 | Findings ranked by blast radius       | essential     | correctness |
| C-03 | Spec gaps identified or cleared       | essential     | coverage    |
| C-04 | Contract violations surfaced/cleared  | essential     | coverage    |
| C-05 | Consolidated report, not five dumps   | essential     | format      |
| C-06 | Per-finding source attribution        | recommended   | depth       |
| C-07 | Actionable remediation hint per find  | recommended   | depth       |
| C-08 | Severity/confidence annotation        | recommended   | depth       |
| C-09 | Cross-skill systemic pattern called out | aspirational | depth       |
| C-10 | Implementation readiness verdict      | aspirational  | behavior    |

---

## Scoring Example

All essential pass, 2/3 recommended pass, 0/2 aspirational pass:

```
composite = (5/5 * 60) + (2/3 * 30) + (0/2 * 10)
          = 60 + 20 + 0
          = 80  → golden threshold met (>=80, all essential pass)
```
```
