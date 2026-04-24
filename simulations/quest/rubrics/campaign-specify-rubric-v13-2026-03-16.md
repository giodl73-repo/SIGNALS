```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v13
date: 2026-03-17
source_rounds: R1–R12
denominator: 37
---

# draft-spec Skill Rubric — v13

## What changed from v12 — 4 new criteria

| Change | Pattern Source | What it addresses |
|--------|----------------|-------------------|
| **C-42** (new) | R12 V-02 (first appearance) — C-38 evidence: "STEP 0C SOURCE BINDING is a distinct block before the column header requirement; it reinforces the source-authority of the cell content." C-39 evidence: "STEP 0C SOURCE BINDING added before COLUMN-HEADER REQUIREMENT as a separate named block — does not replace or alter C-41 mechanism." Stable in V-03 ("VCA entirely unchanged from R11 V-05; STEP 0C CONTRACT ANCHOR in Phase 3 is upstream"), V-04 ("unchanged across both axes"), V-05 ("unchanged across all three axes"). V-01 carries C-38 and C-40 via the pre-table instruction and template cells; it does not include the SOURCE BINDING block and does not pass C-42. | *STEP 0C SOURCE BINDING block present — a named pre-table block, labeled "STEP 0C SOURCE BINDING" or equivalent, appearing before the COLUMN-HEADER REQUIREMENT in the Completion Index VCA section, that explicitly identifies the source authority for the Step 0c contract cell values.* The block asserts that the cell content in the Step 0c Contract Verified column must derive from and match the contract locked in Step 0c. The pre-table instruction (C-40) and template cell values (C-38) alone do not pass C-42; a distinct named source-binding block must be present. Structural dependency: requires C-38 and C-40; if either fails, C-42 fails. |
| **C-43** (new) | R12 V-03 (first appearance) — C-34 evidence: "STEP 0C CONTRACT ANCHOR operates at Phase 3 entry before pitch writing; gate parenthetical in Voice Differentiation Gate unchanged." C-37 evidence: "STEP 0C CONTRACT ANCHOR operates at Phase 3 entry, not in the Completion Index." C-38 evidence: "STEP 0C CONTRACT ANCHOR in Phase 3 is upstream of the VCA and does not alter VCA structure." Stable in V-04 ("referenced in both-axes confirmation"), V-05 ("all three axes"). V-01 and V-02 do not include the Phase 3 anchor and do not pass C-43. | *STEP 0C CONTRACT ANCHOR at Phase 3 entry — a named structural element, labeled "STEP 0C CONTRACT ANCHOR" or equivalent, positioned at Phase 3 entry before pitch writing begins.* It re-anchors the Step 0c voice contract at the phase level, completing a bidirectional chain: Step 0c establishes the contract forward (via C-34, C-36, C-38, C-39) and the Phase 3 anchor re-states the binding contract before the pitch is written (return path). The Voice Differentiation Gate (C-34) alone does not pass C-43; a distinct named anchor element at Phase 3 entry must be present. Structural dependency: requires C-34; if C-34 fails, C-43 fails. |
| **C-44** (new) | R12 V-04 (first appearance) — "CITATION FORM REQUIREMENT" named explicitly as one of the four R12 axis changes: "bidirectional VCA binding, Phase 3 re-anchor, CITATION FORM REQUIREMENT, phrasing compression." V-04 introduces this as its additive structural layer. Stable in V-05 ("unchanged across all three axes"; the three axes prior to V-05's own addition are SOURCE BINDING, CONTRACT ANCHOR, and CITATION FORM REQUIREMENT). V-01 through V-03 carry the STABILITY CITATION RECORD (Form A/B) template; they do not include the CITATION FORM REQUIREMENT statement and do not pass C-44. | *Explicit CITATION FORM REQUIREMENT statement reinforcing the STABILITY CITATION RECORD form format.* When the STABILITY CITATION RECORD passes, the skill prompt includes an explicit named requirement statement — labeled "CITATION FORM REQUIREMENT" or equivalent — that separately states which form (Form A or Form B) applies to each citation entry type and what the exact format must be. The STABILITY CITATION RECORD template alone does not pass C-44; a distinct named requirement statement must be present. Structural dependency: requires the STABILITY CITATION RECORD criterion (within C-09–C-33 block) to pass; if that fails, C-44 fails. |
| **C-45** (new) | R12 V-05 (first appearance) — C-34 evidence: "gate parenthetical unchanged across all three new axes." The three prior axes are SOURCE BINDING (V-02), CONTRACT ANCHOR (V-03), and CITATION FORM REQUIREMENT (V-04). V-05 introduces ANCHOR GATE as its additive structural layer — a gate at Phase 3 entry that explicitly validates the STEP 0C CONTRACT ANCHOR before pitch writing proceeds. V-01 through V-04 carry the Voice Differentiation Gate (C-34) and, from V-03 onwards, the STEP 0C CONTRACT ANCHOR (C-43); none include the ANCHOR GATE and none pass C-45. | *ANCHOR GATE — a named structural gate, labeled "ANCHOR GATE" or equivalent, positioned at Phase 3 entry after the STEP 0C CONTRACT ANCHOR.* It explicitly validates that the Step 0c contract anchor is present and binding before pitch writing is permitted — structurally parallel to the Voice Differentiation Gate (C-34), which validates voice differentiation before allowing pitch writing to proceed. The STEP 0C CONTRACT ANCHOR (C-43) alone does not pass C-45; a distinct named gate element must be present. Structural dependency: requires C-43; if C-43 fails, C-45 fails. |

**Scoring formula**: `aspirational_pass / 37 * 10` (denom 33 → 37)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 37 * 10)
```

**R12 scores under v13:**

| Variation | Asp earned | Asp (of 37) | Composite | Note |
|-----------|------------|-------------|-----------|------|
| V-01 | C-09–C-41 (all) | 33/37 | 98.92 | Inherits full R11 V-05 baseline (passes C-40, C-41); fails C-42 (no SOURCE BINDING block), C-43 (no Phase 3 CONTRACT ANCHOR), C-44 (no CITATION FORM REQUIREMENT statement), C-45 (no ANCHOR GATE) |
| V-02 | C-09–C-41, C-42 | 34/37 | 99.19 | Passes C-42 (STEP 0C SOURCE BINDING block present before COLUMN-HEADER REQUIREMENT); fails C-43, C-44, C-45 |
| V-03 | C-09–C-42, C-43 | 35/37 | 99.46 | Passes C-43 (STEP 0C CONTRACT ANCHOR at Phase 3 entry); fails C-44, C-45 |
| V-04 | C-09–C-43, C-44 | 36/37 | 99.73 | Passes C-44 (explicit CITATION FORM REQUIREMENT statement); fails C-45 (no ANCHOR GATE) |
| V-05 | C-09–C-45 (all 37) | 37/37 | 100.00 | First ceiling under v13 — all four new axes present: SOURCE BINDING (C-42), Phase 3 CONTRACT ANCHOR (C-43), CITATION FORM REQUIREMENT (C-44), ANCHOR GATE (C-45) |

C-42 is stable across V-02–V-05 (four variations); C-43 across V-03–V-05 (three); C-44 across V-04–V-05 (two); C-45 is introduced by V-05 alone. The v13 ceiling requires all four new axes simultaneously.

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

### Aspirational (denominator: 37)

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
| C-41 | **Explicit COLUMN-HEADER REQUIREMENT statement reinforcing the Step 0c column header** | reinforcement | The skill prompt includes an explicit named requirement statement — labeled "COLUMN-HEADER REQUIREMENT" or equivalent — that separately states the exact column header that must appear in the VCA table (e.g., "The third column header must read 'Step 0c Contract Verified'"). The column header in the template alone (C-39) does not pass C-41; a distinct named requirement statement must be present. Structural dependency: requires C-39. |
| C-42 | **STEP 0C SOURCE BINDING block present** | reinforcement | The skill prompt includes a named pre-table block — labeled "STEP 0C SOURCE BINDING" or equivalent — appearing before the COLUMN-HEADER REQUIREMENT in the Completion Index VCA section, that explicitly identifies the source authority for the Step 0c contract cell values (i.e., asserts that cell content must derive from and match the contract locked in Step 0c). The pre-table instruction (C-40) and template cell values (C-38) alone do not pass C-42; a distinct named source-binding block must be present. Structural dependency: requires C-38 and C-40. |
| C-43 | **STEP 0C CONTRACT ANCHOR at Phase 3 entry** | structure | The skill prompt includes a named structural element — labeled "STEP 0C CONTRACT ANCHOR" or equivalent — positioned at Phase 3 entry before pitch writing begins, that re-states the binding Step 0c voice contract at the phase level. This completes the bidirectional chain: Step 0c establishes the contract forward (C-34, C-36, C-38, C-39); the Phase 3 anchor re-asserts it on the return path before pitch writing. The Voice Differentiation Gate (C-34) alone does not pass C-43; a distinct named anchor element at Phase 3 entry must be present. Structural dependency: requires C-34. |
| C-44 | **Explicit CITATION FORM REQUIREMENT statement reinforcing the STABILITY CITATION RECORD format** | reinforcement | The skill prompt includes an explicit named requirement statement — labeled "CITATION FORM REQUIREMENT" or equivalent — that separately states which form (Form A or Form B) applies to each citation entry type and what the exact format must be. The STABILITY CITATION RECORD template alone does not pass C-44; a distinct named requirement statement must be present. Structural dependency: requires the STABILITY CITATION RECORD criterion (within C-09–C-33 block) to pass. |
| C-45 | **ANCHOR GATE validating the Phase 3 contract anchor** | structure | The skill prompt includes a named structural gate — labeled "ANCHOR GATE" or equivalent — positioned at Phase 3 entry after the STEP 0C CONTRACT ANCHOR, that explicitly validates the anchor is present and binding before pitch writing is permitted. Structurally parallel to the Voice Differentiation Gate (C-34): as C-34 gates on voice differentiation, C-45 gates on anchor presence. The STEP 0C CONTRACT ANCHOR (C-43) alone does not pass C-45; a distinct named gate element must be present. Structural dependency: requires C-43. |
```
