The rubric itself is in the prompt content you provided. I have all I need to write v10.

Two new criteria emerge from the R9 scorecard:

1. **C-36** — from V-03's diagnostic: lexical verb consistency between gate parenthetical and audit row attribution
2. **C-37** — from V-02's structural axis: table format with dedicated contract column in Voice Compliance Audit

R9 scores under v10 (denom 29):
- V-01: 26/29 (misses C-34, C-36, C-37)
- V-02: 28/29 (gains C-37; misses C-36 — table column value `Step 0c exec voice contract` carries no verb, gate uses "satisfied")
- V-03: 28/29 (gains C-36; misses C-37 — bullet rows)
- V-04: 26/29 (misses C-34, C-36, C-37)

The v10 ceiling is 29/29 — requires table format + verb consistency + gate anchor.

---

# draft-spec Skill Rubric — v10

## What changed from v9 — 2 new criteria

| Change | Pattern Source | What it addresses |
|--------|----------------|-------------------|
| **C-36** (new) | V-03 diagnostic finding — "Lexical consistency between gate parenthetical ('satisfied') and audit rows ('satisfied') is a structural bonus — not required but creates cleaner traceability" | *Lexical verb consistency between gate parenthetical and audit row attribution.* When both a gate parenthetical with contract attribution (C-34) and per-audience audit rows with contract attribution (C-35) exist, the verb used in the gate parenthetical and the verb used in each corresponding audit row are the same (e.g., gate says `Step 0c exec voice contract satisfied` → row says `Step 0c exec voice contract satisfied`). Verb mismatch between gate and row does not pass. |
| **C-37** (new) | V-02 structural axis — table replaces bullet rows, with dedicated `Step 0c Contract Verified` column; rubric note explicitly flags the format distinction as a future revision candidate | *Table format with dedicated contract column in Voice Compliance Audit.* When per-audience audit rows exist (C-33), the Voice Compliance Audit section presents audit rows as a structured table with at minimum an Audience column, a Verdict column, and a dedicated Step 0c contract verification column (e.g., `Step 0c Contract Verified`). A flat bullet-list format does not pass. |

**Scoring formula**: `aspirational_pass / 29 * 10` (denom 27 → 29)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 29 * 10)
```

**R9 scores under v10:**

| Variation | Asp earned | Asp (of 29) | Composite | Note |
|-----------|------------|-------------|-----------|------|
| V-01 | C-09–C-33, C-35 | 26/29 | 98.97 | Misses C-34 (no gate anchor), C-36 (no gate to match), C-37 (bullet rows) |
| V-02 | C-09–C-35, C-37 | 28/29 | 99.66 | Table format gains C-37; table column carries no verb — C-36 fails |
| V-03 | C-09–C-35, C-36 | 28/29 | 99.66 | Verb consistency gains C-36; bullet rows — C-37 fails |
| V-04 | C-09–C-33, C-35 | 26/29 | 98.97 | Instruction + satisfied rows; no gate anchor — C-34, C-36, C-37 all fail |

V-02 and V-03 are tied at 28/29 via different paths: V-02 has the table structure without verb consistency; V-03 has verb consistency without the table. The v10 ceiling is 29/29 — requires table format, verb consistency, and gate anchor together.

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

### Aspirational (denominator: 29)

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
| C-36 | **Lexical verb consistency between gate parenthetical and audit row attribution** | traceability | When both a gate parenthetical with contract attribution (C-34) and per-audience audit rows with contract attribution (C-35) exist, the verb used in the gate parenthetical and the verb used in each corresponding audit row are identical (e.g., gate: `Step 0c exec voice contract satisfied` → row: `Step 0c exec voice contract satisfied`). Verb mismatch between gate and row does not pass. |
| C-37 | **Table format with dedicated contract column in Voice Compliance Audit** | structure | When per-audience audit rows exist (C-33), the Voice Compliance Audit section presents audit rows as a structured table with at minimum an Audience column, a Verdict column, and a dedicated Step 0c contract verification column (e.g., `Step 0c Contract Verified`). A flat bullet-list format does not pass. |

---

## Version History

| Version | Denominator | Key additions |
|---------|-------------|---------------|
| v7 | 23 | C-27 introduced (formal audit section) |
| v8 | 26 | C-28, C-29, C-32 (per-audience gates, contract naming, categorization declaration) |
| v9 | 27 | C-33, C-34, C-35 (per-audience audit rows, gate contract anchor, row contract attribution) |
| v10 | 29 | C-36 (gate/row verb consistency), C-37 (table format with contract column) |
