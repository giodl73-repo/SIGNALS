Looking at the R8 scorecard, the one excellence signal that transcends C-33 and C-34 is the **richer audit row form** introduced by V-03: each per-audience row in the Voice Compliance Audit section carries inline Step 0c contract attribution. V-01 and V-04 earn C-33 with bare rows; V-03 and V-05 go further by attributing the contract name within each row. That V-04 hits 100.0 on v8 without this pattern — while V-05 has it — is the gap that becomes C-35.

---

# draft-spec Skill Rubric — v9

## What changed from v8 — 1 new criterion

| Change | Pattern Source | What it addresses |
|--------|----------------|-------------------|
| **C-35** (new) | V-03 richer C-33 form vs V-01/V-04 bare rows — R8 scorecard distinguishes "separate rows present" from "contract attributed in each row" | *Step 0c contract attribution in per-audience Voice Compliance Audit rows.* When per-audience audit rows exist (C-33), each row names the applicable Step 0c contract inline (e.g., `Exec verdict: Pass — Step 0c exec voice contract verified`). Rows without inline contract attribution do not pass. |

**Scoring formula**: `aspirational_pass / 27 * 10` (denom 26 → 27)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 27 * 10)
```

**R8 scores under v9:**

| Variation | Asp earned | Asp (of 27) | Composite | Note |
|-----------|------------|-------------|-----------|------|
| V-01 | C-27, C-28, C-29, C-32, C-33 | 25/27 | 99.3 | Bare rows; no contract attribution per row; no gate anchor |
| V-02 | C-27, C-28, C-29, C-32, C-34 | 25/27 | 99.3 | Gate anchor present; no separate audit rows |
| V-03 | C-27, C-28, C-29, C-32, C-33, C-35 | 26/27 | 99.6 | Richer audit rows; gate anchor absent |
| V-04 | C-27, C-28, C-29, C-32, C-33, C-34 | 26/27 | 99.6 | Bare rows + gate anchor; no per-row attribution |
| V-05 | C-27, C-28, C-29, C-32, C-33, C-34, C-35 | 27/27 | 100.0 | Richer rows + gate anchor — full traceability |

V-05 is sole 100.0. V-03 and V-04 are tied at 99.6 via different 26/27 paths: V-03 has richer audit rows without the gate anchor; V-04 has the gate anchor without per-row attribution. C-35 is the remaining differentiator. The R9 ceiling is 27/27.

---

## Criteria

### Essential (output is not useful without these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Three artifacts produced** | completeness | essential | The skill produces all three artifacts: spec, proposal, and pitch. All three must exist as written files on disk. Missing any artifact = fail. |
| C-02 | **Spec has all six required sections** | completeness | essential | The spec artifact contains all six sections: Overview, User Problem, Proposed Solution, Constraints, Open Questions, and Self-Review. Missing or empty section = fail. |
| C-03 | **Proposal has 3+ options including do-nothing** | completeness | essential | The proposal artifact contains at least three options. One option must be explicitly named "Do Nothing" (or equivalent). Each option must include description, pros, cons, risk, effort, and a recommendation section with stated rationale. |
| C-04 | **Pitch covers three audience versions** | coverage | essential | The pitch artifact contains exec, developer, and maker versions. Each version has: hook, what it does, why it matters, and call to action. Missing any version = fail. |
| C-05 | **Cross-artifact consistency** | correctness | essential | The feature name, core behavior, and key constraints described in the spec are consistent with those referenced in the proposal and pitch. No contradictions between artifacts on fundamental scope. |

---

### Recommended (output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Spec self-review flags gaps** | depth | recommended | The spec artifact includes a self-review section identifying open questions, ambiguities, or sections needing more detail. At least one gap or open question named. "No gaps found" does not pass. |
| C-07 | **Pitch contains anti-positioning section** | depth | recommended | The pitch artifact includes an anti-positioning section explicitly stating what the feature is NOT, distinct from the three audience versions. |
| C-08 | **Proposal recommendation cites trade-off rationale** | depth | recommended | The proposal recommendation section explicitly references the key trade-off(s) that drove the choice — not just a preference statement. The rationale must be traceable to a specific constraint or risk identified in the options analysis. |

---

### Aspirational (denominator: 27)

*C-09 through C-26 are inherited from prior rubric versions and not reproduced here. All were passed by R7 V-05 and inherited unchanged.*

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-27 | **Formal Voice Compliance Audit section with preamble enumeration** | structure | The output contains a structurally named `### Voice Compliance Audit` section. The section opens with a preamble that enumerates the four named compliance sections. Bullet entries in a flat Additional index do not pass. |
| C-28 | **Per-audience gate Pass/Fail verdicts** | gates | Step 3 records a Pass or Fail verdict individually for exec, dev, and maker audiences. A single combined gate verdict does not pass. |
| C-29 | **Step 0c contract naming in Step 3** | naming | Step 3 explicitly references the Step 0c contract name for each audience gate. Behavioral criteria without Step 0c contract attribution do not pass. |
| C-30–C-31 | *(inherited — see prior rubric)* | — | — |
| C-32 | **Compliance categorization declaration in COMPLETION INDEX preamble** | structure | The COMPLETION INDEX preamble not only enumerates the four named sections but explicitly declares that each section classifies a distinct category of compliance state. Section naming without categorization purpose does not pass. |
| C-33 | **Per-audience verdicts in Voice Compliance Audit section** | traceability | When the formal Voice Compliance Audit section (C-27) and per-audience gate Pass/Fail (C-28) both exist, the audit section records individual verdicts for exec, dev, and maker separately. A combined single-line gate result does not pass. |
| C-34 | **Step 0c contract anchor embedded in gate parenthetical Pass condition** | traceability | When parenthetical per-audience gate criteria (C-28) and Step 0c naming in Step 3 (C-29) both exist, the parenthetical Pass condition for each audience explicitly names the applicable Step 0c contract (e.g., `Pass (Step 0c exec voice contract satisfied: ...)`). Parenthetical criteria without contract attribution do not pass. |
| C-35 | **Step 0c contract attribution in per-audience Voice Compliance Audit rows** | traceability | When per-audience audit rows exist (C-33), each row names the applicable Step 0c contract inline within the row (e.g., `Exec verdict: Pass — Step 0c exec voice contract verified`). Rows without inline contract attribution do not pass. |

---

## Version History

| Version | Denominator | Key additions |
|---------|-------------|---------------|
| v7 | 23 | C-27 introduced (formal audit section) |
| v8 | 26 | C-27 tightened; C-32, C-33, C-34 added |
| **v9** | **27** | **C-35 added** — per-row Step 0c attribution inside audit rows |
