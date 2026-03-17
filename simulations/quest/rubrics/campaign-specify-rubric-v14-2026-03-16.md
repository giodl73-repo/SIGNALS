Good — the existing files are for a different `draft-spec` series. The rubric in the prompt is the `campaign-specify` series. Two new patterns are clearly evidenced:

1. **C-46** — IMPERATIVE REGISTER (V-01, first appearance): V-01 "changes register (descriptive vs. imperative)" while all named structural blocks retain exact labels. Stable across V-01–V-05.
2. **C-47** — GATE CHAIN REQUIREMENT (V-05, first appearance): "V-05 adds GATE CHAIN REQUIREMENT explicitly declaring C-09's requirement by name — this is a *reinforcement* of C-09, not a structural deviation from it." V-01–V-04 carry the gate chain (C-09 passes) but none include the named requirement statement.

Denominator: 37 → 39. V-01–V-04 score 38/39 (C-46 pass, C-47 fail); V-05 = 39/39 (first ceiling).

```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v14
date: 2026-03-17
source_rounds: R1–R13
denominator: 39
---

# draft-spec Skill Rubric — v14

## What changed from v13 — 2 new criteria

| Change | Pattern Source | What it addresses |
|--------|----------------|-------------------|
| **C-46** (new) | R13 V-01 (first appearance) — Scoring basis: "Each variation either changes register (V-01) or adds new structural blocks while explicitly preserving C-42 through C-45 unchanged." C-09 analysis: "V-01 changes register (descriptive vs. imperative) but all named structural blocks retain exact labels." Stable in V-02 ("same block preserved unchanged"), V-03, V-04, V-05 (register inherited through the sequential chain). R12 V-05 (the R13 baseline) uses descriptive register and does not pass C-46. | *IMPERATIVE REGISTER — all structural instructions in the skill prompt use imperative mode throughout.* The skill addresses the executor directly with imperative constructions ("Write", "Fill in", "Halt and state", "Verify") rather than descriptive constructions ("The skill writes", "The column should be filled", "The skill halts when"). This is a cross-cutting register property evaluated across all phases and structural blocks. Named block labels (e.g., "STEP 0C SOURCE BINDING", "COLUMN-HEADER REQUIREMENT") are excluded from register evaluation — only the instructional body text must be imperative. A single structural section using descriptive phrasing for instructions fails C-46. No structural dependency; applies independently of other aspirational criteria. |
| **C-47** (new) | R13 V-05 (first appearance) — C-09 analysis: "V-05 adds GATE CHAIN REQUIREMENT explicitly declaring C-09's requirement by name — this is a *reinforcement* of C-09, not a structural deviation from it." V-01 through V-04 carry the Phase 0 four-step gate chain (C-09 passes in all five variations) but none include the GATE CHAIN REQUIREMENT statement and none pass C-47. | *GATE CHAIN REQUIREMENT — a named requirement statement, labeled "GATE CHAIN REQUIREMENT" or equivalent, explicitly declaring that all four Phase 0 steps must be present as named sequential gates.* The statement separately and explicitly requires that Steps 0a, 0b, 0c, and 0d each appear as labeled, ordered gate elements in Phase 0 — reinforcing C-09 by name at the requirement level rather than merely instantiating the chain. The Phase 0 gate chain (C-09) alone does not pass C-47; a distinct named requirement statement referencing all four steps must be present. Structural dependency: requires C-09; if C-09 fails, C-47 fails. |

**Scoring formula**: `aspirational_pass / 39 * 10` (denom 37 → 39)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 39 * 10)
```

**R13 scores under v14:**

| Variation | Asp earned | Asp (of 39) | Composite | Note |
|-----------|------------|-------------|-----------|------|
| V-01 | C-09–C-45 + C-46 | 38/39 | 99.74 | Introduces IMPERATIVE REGISTER (C-46); all R12 V-05 baseline criteria pass; fails C-47 (no GATE CHAIN REQUIREMENT) |
| V-02 | C-09–C-46 | 38/39 | 99.74 | Preserves C-46 (register inherited); adds unnamed structural block not captured by v14 criteria; fails C-47 |
| V-03 | C-09–C-46 | 38/39 | 99.74 | Same — unnamed structural addition not captured by v14; fails C-47 |
| V-04 | C-09–C-46 | 38/39 | 99.74 | Same — unnamed structural addition not captured by v14; fails C-47 |
| V-05 | C-09–C-47 (all 39) | 39/39 | 100.00 | First ceiling under v14 — IMPERATIVE REGISTER (C-46, inherited from V-01 chain) + GATE CHAIN REQUIREMENT (C-47, introduced) |

C-46 is stable across V-01–V-05 (all five variations); C-47 first appears in V-05 alone. The v14 ceiling requires both simultaneously. Note: V-02–V-04 each introduce one unnamed structural block that is a candidate for v15 criteria; without stable names in the R13 scorecard those patterns are not codified here.

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

### Aspirational (denominator: 39)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Phase 0 four-step gate chain present** | structure | Steps 0a, 0b, 0c, and 0d are each present as named, sequential gates in Phase 0. All four steps must be explicitly labeled and ordered. Missing or merged steps = fail. |
| C-10–C-33 | *(carried forward unchanged from v12)* | — | *(see v12 for full text of each criterion)* |
| C-34 | **Gate anchor with audience-specific contract name + "satisfied" prefix** | structure | The Voice Differentiation Gate parenthetical names each audience contract in the form `Step 0c [audience] voice contract satisfied: [condition]`. All three audience variants (exec, dev, maker) must be present and correctly formed. |
| C-35 | *(carried forward unchanged from v12)* | — | *(see v12)* |
| C-36 | **Verb consistency: "satisfied" in gate parentheticals AND in VCA cell values** | consistency | The verb "satisfied" appears in both the Voice Differentiation Gate parentheticals (C-34) and the VCA cell values. No mixing with alternative verbs (e.g., "met", "confirmed"). |
| C-37 | **VCA three-column table format (Audience / Verdict / Step 0c Contract Verified)** | structure | The Voice Compliance Audit table in the Completion Index uses exactly three columns with headers `Audience`, `Verdict`, and `Step 0c Contract Verified`. Column names must match exactly. |
| C-38 | **Audience identifier embedded in VCA cell values** | consistency | Cell values in the Step 0c Contract Verified column embed the audience identifier in the form `Step 0c [audience] voice contract satisfied` (e.g., `Step 0c exec voice contract satisfied`). All three rows must be correctly formed. Structural dependency: requires C-34, C-36, C-37. |
| C-39 | **"Step 0c" step reference in VCA column header** | consistency | The third column header reads exactly `Step 0c Contract Verified`. Structural dependency: requires C-37. |
| C-40 | **Pre-table explicit instruction reinforcing audience-discriminating cell values** | reinforcement | The skill prompt includes a standalone instructional statement before the VCA table — separate from the template's cell values — that explicitly names the audience-discriminating cell value format (e.g., "Fill in the Step 0c Contract Verified column with the exact Step 0c contract name followed by 'satisfied'", or equivalent). Template cell values alone (C-38) do not pass C-40; a distinct named instruction must be present. Structural dependency: requires C-38. |
| C-41 | *(carried forward unchanged from v12)* | — | *(see v12)* |
| C-42 | **STEP 0C SOURCE BINDING block present** | reinforcement | A named pre-table block, labeled "STEP 0C SOURCE BINDING" or equivalent, appears before the COLUMN-HEADER REQUIREMENT in the Completion Index VCA section, explicitly identifying the source authority for the Step 0c contract cell values. The block asserts that the cell content in the Step 0c Contract Verified column must derive from and match the contract locked in Step 0c. The pre-table instruction (C-40) and template cell values (C-38) alone do not pass C-42; a distinct named source-binding block must be present. Structural dependency: requires C-38 and C-40; if either fails, C-42 fails. |
| C-43 | **STEP 0C CONTRACT ANCHOR at Phase 3 entry** | structure | A named structural element, labeled "STEP 0C CONTRACT ANCHOR" or equivalent, positioned at Phase 3 entry before pitch writing begins. It re-anchors the Step 0c voice contract at the phase level, completing a bidirectional chain: Step 0c establishes the contract forward (via C-34, C-36, C-38, C-39) and the Phase 3 anchor re-states the binding contract before the pitch is written (return path). The Voice Differentiation Gate (C-34) alone does not pass C-43; a distinct named anchor element at Phase 3 entry must be present. Structural dependency: requires C-34; if C-34 fails, C-43 fails. |
| C-44 | **Explicit CITATION FORM REQUIREMENT statement** | reinforcement | When the STABILITY CITATION RECORD passes, the skill prompt includes an explicit named requirement statement — labeled "CITATION FORM REQUIREMENT" or equivalent — that separately states which form (Form A or Form B) applies to each citation entry type and what the exact format must be. The STABILITY CITATION RECORD template alone does not pass C-44; a distinct named requirement statement must be present. Structural dependency: requires the STABILITY CITATION RECORD criterion (within C-09–C-33 block) to pass; if that fails, C-44 fails. |
| C-45 | **ANCHOR GATE at Phase 3 entry** | structure | A named structural gate, labeled "ANCHOR GATE" or equivalent, positioned at Phase 3 entry after the STEP 0C CONTRACT ANCHOR. It explicitly validates that the Step 0c contract anchor is present and binding before pitch writing is permitted — structurally parallel to the Voice Differentiation Gate (C-34). The STEP 0C CONTRACT ANCHOR (C-43) alone does not pass C-45; a distinct named gate element must be present. Structural dependency: requires C-43; if C-43 fails, C-45 fails. |
| C-46 | **IMPERATIVE REGISTER throughout structural instructions** | style | All structural instructions in the skill prompt use imperative mode — commands addressed to the executor ("Write", "Fill in", "Halt and state", "Verify") rather than descriptive phrasing about what the skill does ("The skill writes", "The column should be filled"). This is a cross-cutting property evaluated across all phases and structural blocks. Named block labels (e.g., "STEP 0C SOURCE BINDING") are excluded from register evaluation; only instructional body text is evaluated. Any structural section whose instructional body uses non-imperative phrasing fails C-46. No structural dependency. |
| C-47 | **GATE CHAIN REQUIREMENT — named statement declaring Phase 0 four-step gate chain** | reinforcement | A named requirement statement, labeled "GATE CHAIN REQUIREMENT" or equivalent, is explicitly present in the skill prompt, separately and explicitly declaring that Steps 0a, 0b, 0c, and 0d must all be present as named, sequential gate elements in Phase 0. The Phase 0 gate chain itself (C-09) does not pass C-47; a distinct named requirement statement referencing all four steps by name must be present. Structural dependency: requires C-09; if C-09 fails, C-47 fails. |
```

**Summary of changes:**

| | v13 | v14 |
|-|-----|-----|
| New criteria | C-42–C-45 (from R12) | C-46–C-47 (from R13) |
| Aspirational denominator | 37 | 39 |
| Formula | `asp / 37 * 10` | `asp / 39 * 10` |
| First ceiling | R12 V-05 | R13 V-05 |
| Uncodified candidates | — | V-02/V-03/V-04 unnamed blocks → v15 |
