The scorecard cuts off partway through V-02, but the evidence from both variations is enough to extract two new criteria. Let me identify them precisely before writing.

**From V-01's complete scoring:**
- C-37 passes via: "Three-column table: Audience / Verdict / **Step 0c Contract Verified**" — the column header carries "Step 0c" as an explicit workflow step reference, not just a generic label
- C-39 emerges: the "Step 0c" prefix in the column header is a distinct structural element beyond C-37's general table-format requirement

**From V-02's synthesis (first 29/29):**
- The single-axis change — adding "satisfied" to table cells — means the full phrase "Step 0c **exec** voice contract satisfied" appears in *both* the gate parenthetical and the table cell, with the audience identifier embedded in the phrase itself
- C-38 emerges: when the synthesis is complete (C-34 + C-36 + C-37 all pass), the attribution phrase must carry the audience discriminator — "exec"/"dev"/"maker" — not just a generic contract name

Under v11 (denominator 31):
- V-01: 28/31 — gains C-39 (column header present), loses C-38 (structural dependency on C-34)
- V-02: 31/31 — first 100.00

---

```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v11
date: 2026-03-17
source_rounds: R1–R10
denominator: 31
---

# draft-spec Skill Rubric — v11

## What changed from v10 — 2 new criteria

| Change | Pattern Source | What it addresses |
|--------|----------------|-------------------|
| **C-38** (new) | R10 V-02 synthesis — first variation to pass C-34 + C-35 + C-36 + C-37 simultaneously. When all four structural layers align, the gate parenthetical phrase and the table row attribution phrase each contain an audience identifier embedded in the phrase itself (e.g., "Step 0c **exec** voice contract satisfied"). V-01's table cells carry "Step 0c exec voice contract satisfied" but V-01 has no gate (C-34 fails → C-38 fails by dependency). V-02 is the first to demonstrate audience-discriminating phrases in both locations. | *Audience identifier in contract attribution phrase.* When gate anchor (C-34), verb consistency (C-36), and table format (C-37) all pass, the contract attribution phrase used in the gate parenthetical and in each table row's contract cell explicitly names the audience for that row (e.g., "Step 0c exec voice contract satisfied" for exec, "Step 0c dev voice contract satisfied" for dev, "Step 0c maker voice contract satisfied" for maker). A phrase without an audience specifier — e.g., "Step 0c voice contract satisfied" applied generically to all rows — does not pass regardless of which row or gate it appears in. Structural dependency: requires C-34, C-36, and C-37 to be evaluable; if any dependency fails, C-38 fails by structural dependency. |
| **C-39** (new) | R10 V-01 structural axis — C-37 evidence explicitly names column header "Step 0c Contract Verified". The "Step 0c" step reference in the header ties the audit column to the specific workflow step that produced the contracts, not just to a generic verification action. Both V-01 and V-02 carry this header; the pattern is stable across the table-format structural axis. | *Step 0c step reference in VCA contract column header.* When the VCA uses table format with a dedicated contract column (C-37), the contract column header includes "Step 0c" as an explicit workflow step reference (e.g., "Step 0c Contract Verified"). A column header lacking the "Step 0c" step identifier — e.g., "Contract Check", "Voice Contract", "Verified" — does not pass. Structural dependency: requires C-37; if C-37 fails, C-39 fails. |

**Scoring formula**: `aspirational_pass / 31 * 10` (denom 29 → 31)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 31 * 10)
```

**R10 scores under v11:**

| Variation | Asp earned | Asp (of 31) | Composite | Note |
|-----------|------------|-------------|-----------|------|
| V-01 | C-09–C-33, C-35, C-37, C-39 | 28/31 | 99.03 | Gains C-39 (column header); C-38 fails by structural dependency on C-34 (no gate anchor) |
| V-02 | C-09–C-39 (all) | 31/31 | 100.00 | First ceiling — table + verb consistency + gate anchor + audience phrase + step-reference header all present |

V-01 recovers one point via C-39 (column header with "Step 0c" is present regardless of gate). V-02 achieves the first 100.00 composite: C-38 requires the complete synthesis (C-34 + C-36 + C-37), which V-02 uniquely holds. C-39 applies independently of the gate-anchor cluster and is passable without C-34.

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

### Aspirational (denominator: 31)

*C-09 through C-26 are inherited from prior rubric versions and not reproduced here. All were passed by R7 V-05 and inherited unchanged.*

*C-30, C-31, C-32 were added in post-R7 rounds and are passed by all current baselines. They are treated as inherited and not reproduced here.*

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-27 | **Formal Voice Compliance Audit section with preamble enumeration** | structure | The output contains a structurally named `### Voice Compliance Audit` section. The section opens with a preamble that enumerates the four named compliance sections. Bullet entries in a flat Additional index do not pass. |
| C-28 | **Per-audience gate Pass/Fail verdicts** | gates | Step 3 records a Pass or Fail verdict individually for exec, dev, and maker audiences. A single combined gate verdict does not pass. |
| C-29 | **Step 0c contract naming in Step 3** | naming | Step 3 explicitly references the Step 0c contract name for each audience gate. Behavioral criteria without Step 0c contract attribution do not pass. |
| C-33 | **Per-audience audit rows in VCA** | structure | The Voice Compliance Audit section contains at least three rows corresponding to the exec, dev, and maker audiences individually. A single combined row or summary statement does not pass. |
| C-34 | **Gate parenthetical with contract attribution** | gates | Each per-audience gate in Step 3 includes a parenthetical that names the Step 0c contract used to evaluate that audience (e.g., `Step 0c exec voice contract satisfied`). A gate verdict with behavioral criteria but no contract name in the parenthetical does not pass. |
| C-35 | **Per-audience audit rows with contract attribution** | naming | Each per-audience audit row in the Voice Compliance Audit names the Step 0c contract that was verified for that audience inline in the row content (e.g., "Step 0c exec voice contract satisfied"). A row with a verdict but no contract attribution does not pass. |
| C-36 | **Lexical verb consistency gate↔audit** | consistency | When both a gate parenthetical with contract attribution (C-34) and per-audience audit rows with contract attribution (C-35) exist, the verb used in the gate parenthetical and the verb used in the corresponding audit row are the same (e.g., gate says `Step 0c exec voice contract satisfied` → row says `Step 0c exec voice contract satisfied`). Verb mismatch between gate and row does not pass. Structural dependency: if C-34 fails, C-36 fails by structural dependency. |
| C-37 | **Table format with dedicated contract column in Voice Compliance Audit** | structure | When per-audience audit rows exist (C-33), the Voice Compliance Audit section presents audit rows as a structured table with at minimum an Audience column, a Verdict column, and a dedicated Step 0c contract verification column (e.g., `Step 0c Contract Verified`). A flat bullet-list format does not pass. |
| C-38 | **Audience identifier in contract attribution phrase** | consistency | When gate anchor (C-34), verb consistency (C-36), and table format (C-37) all pass, the contract attribution phrase used in the gate parenthetical and in each table row's contract cell explicitly names the audience for that row (e.g., "Step 0c **exec** voice contract satisfied" for exec, "Step 0c **dev** voice contract satisfied" for dev, "Step 0c **maker** voice contract satisfied" for maker). A phrase without an audience specifier — e.g., "Step 0c voice contract satisfied" applied generically — does not pass regardless of which row or gate it appears in. Structural dependency: requires C-34, C-36, and C-37 to be evaluable; if any dependency fails, C-38 fails by structural dependency. |
| C-39 | **Step 0c step reference in VCA contract column header** | structure | When the VCA uses table format with a dedicated contract column (C-37), the contract column header includes "Step 0c" as an explicit workflow step reference (e.g., "Step 0c Contract Verified"). A column header lacking the "Step 0c" step identifier — e.g., "Contract Check", "Voice Contract", "Verified" — does not pass. Structural dependency: requires C-37; if C-37 fails, C-39 fails. |

---

## Dependency chain (C-34 cluster)

```
C-34 (gate anchor)
 └── C-36 (verb consistency gate↔row)  — depends on C-34
      └── C-38 (audience identifier in phrase) — depends on C-34 + C-36 + C-37

C-37 (table format)
 └── C-39 (Step 0c header prefix)  — depends on C-37 only
      ↑ independent of gate-anchor cluster; passes when C-34 fails
```

C-39 is the only new criterion passable without C-34. All other v10→v11 aspirational criteria in the gate-anchor cluster (C-36, C-38) require C-34 as a structural prerequisite.
```
