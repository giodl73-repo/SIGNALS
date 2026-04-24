Now I have enough context. Three new patterns from R14: INERTIA ANCHOR GATE (C-48), STEP 0B STABILITY ANCHOR (C-49), PHASE GATE AUDIT SOURCE BINDING (C-50). Denominator 39 → 42. V-05 is the first ceiling at 42/42.

```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v15
date: 2026-03-17
source_rounds: R1–R14
denominator: 42
---

# draft-spec Skill Rubric — v15

## What changed from v14 — 3 new criteria

| Change | Pattern Source | What it addresses |
|--------|----------------|-------------------|
| **C-48** (new) | R14 V-01 (first appearance) — C-46 analysis: "INERTIA ANCHOR GATE body: 'Do not begin writing any proposal option until all three inertia costs are present in the STEP 0A INERTIA ANCHOR block above. A proposal option written before the anchor block is complete does not satisfy this gate.'" Stable in V-04 and V-05. R13 V-05 baseline carries STEP 0A INERTIA ANCHOR but no gate after it; C-48 is absent from all R13 variations. | *INERTIA ANCHOR GATE — a named gate block, labeled "INERTIA ANCHOR GATE" or equivalent, positioned immediately after the STEP 0A INERTIA ANCHOR block, explicitly blocking proposal option writing until all three inertia costs are present in the anchor block.* The gate body must use imperative register and name the blocking condition: no proposal option may be written before the anchor block is complete. Completes the inertia cost chain's missing gate position: define (Step 0a) → anchor (STEP 0A INERTIA ANCHOR) → **GATE** → options. Structural parallel to ANCHOR GATE (C-45), which blocks pitch writing until STEP 0C CONTRACT ANCHOR is complete. Structural dependency: requires STEP 0A INERTIA ANCHOR; if that block is absent, C-48 fails. The INERTIA ANCHOR block alone (without the gate) does not pass C-48. |
| **C-49** (new) | R14 V-02 (first appearance) — C-46 analysis: "STEP 0B STABILITY ANCHOR body: 'Before writing the Defeating Do Nothing block, copy the Step 0b STABILITY CITATION RECORD here... This is the anchor text. The Defeating Do Nothing block must contain this record verbatim. Do not begin writing the Defeating Do Nothing block until this anchor is complete.'" Stable in V-04 and V-05. R13 V-05 baseline carries STEP 0B CITATION BINDING; C-49 is absent from all R13 variations. | *STEP 0B STABILITY ANCHOR — a named anchor block, labeled "STEP 0B STABILITY ANCHOR" or equivalent, positioned in Phase 0 before the Defeating Do Nothing block, containing the Step 0b STABILITY CITATION RECORD verbatim, with an explicit instruction requiring that the Defeating Do Nothing block reproduce this record verbatim and not be written until this anchor is complete.* The anchor must both (a) hold the pasted record and (b) carry the blocking instruction forward. The instruction "Do not begin writing the Defeating Do Nothing block until this anchor is complete" (or equivalent) must be present. Structural dependency: requires STEP 0B CITATION BINDING; if that block is absent, C-49 fails. STEP 0B CITATION BINDING alone (without the stability anchor and blocking instruction) does not pass C-49. |
| **C-50** (new) | R14 V-03 (first appearance) — C-46 analysis: "PHASE GATE AUDIT SOURCE BINDING body: 'This audit does not redefine the gate requirements — it verifies...' ... Imperative present: 'Do not redefine the gate chain in this audit — verify conformance to the Phase 0 source.'" Stable in V-05. R13 V-05 baseline carries a Phase Gate Audit section but no named source binding block within it; C-50 is absent from all R13 variations. | *PHASE GATE AUDIT SOURCE BINDING — a named source binding block, labeled "PHASE GATE AUDIT SOURCE BINDING" or equivalent, within the Phase Gate Audit section, explicitly naming Phase 0 as the authoritative source for gate definitions and carrying the instruction not to redefine the gate chain in the audit — only to verify conformance.* The block must contain both (a) a statement that the audit does not redefine gate requirements and (b) an imperative instruction to verify conformance to the Phase 0 source rather than redefine it. Structural parallel to STEP 0C SOURCE BINDING in the Voice Compliance Audit. Structural dependency: requires the Phase Gate Audit section; if that section is absent, C-50 fails. A Phase Gate Audit without the named source binding block does not pass C-50. |

**Scoring formula**: `aspirational_pass / 42 * 10` (denom 39 → 42)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 42 * 10)
```

**R14 scores under v15:**

| Variation | Unique addition(s) | Asp earned | Asp (of 42) | Composite | Note |
|-----------|--------------------|------------|-------------|-----------|------|
| V-01 | INERTIA ANCHOR GATE | C-09–C-47 + C-48 | 40/42 | 99.52 | Introduces INERTIA ANCHOR GATE (C-48); fails C-49 (no STEP 0B STABILITY ANCHOR) and C-50 (no PHASE GATE AUDIT SOURCE BINDING) |
| V-02 | STEP 0B STABILITY ANCHOR | C-09–C-47 + C-49 | 40/42 | 99.52 | Introduces STEP 0B STABILITY ANCHOR (C-49); fails C-48 (no INERTIA ANCHOR GATE) and C-50 (no PHASE GATE AUDIT SOURCE BINDING) |
| V-03 | PHASE GATE AUDIT SOURCE BINDING | C-09–C-47 + C-50 | 40/42 | 99.52 | Introduces PHASE GATE AUDIT SOURCE BINDING (C-50); fails C-48 (no INERTIA ANCHOR GATE) and C-49 (no STEP 0B STABILITY ANCHOR) |
| V-04 | V-01 + V-02 combined | C-09–C-47 + C-48 + C-49 | 41/42 | 99.76 | Carries INERTIA ANCHOR GATE (C-48) + STEP 0B STABILITY ANCHOR (C-49); fails C-50 (no PHASE GATE AUDIT SOURCE BINDING) |
| V-05 | V-01 + V-02 + V-03 combined | C-09–C-50 (all 42) | 42/42 | 100.00 | First ceiling under v15 — all three new gates present simultaneously |

C-48 is stable in V-01, V-04, V-05. C-49 is stable in V-02, V-04, V-05. C-50 is stable in V-03, V-05. V-05 is the only variation to carry all three simultaneously and the only first-ceiling under v15.

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

### Aspirational (denominator: 42)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Phase 0 four-step gate chain present** | structure | Steps 0a, 0b, 0c, and 0d are each present as named, sequential gates in Phase 0. All four steps must be explicitly labeled and ordered. Missing or merged steps = fail. |
| C-10–C-33 | *(carried forward unchanged from v12)* | — | *(see v12 for full text of each criterion)* |
| C-34 | **Gate anchor with audience-specific contract name + "satisfied" prefix** | structure | The Voice Differentiation Gate parenthetical names each audience contract in the form `Step 0c [audience] voice contract satisfied: [condition]`. All three audience variants (exec, dev, maker) must be present and correctly formed. |
| C-35 | *(carried forward unchanged from v12)* | — | *(see v12)* |
| C-36–C-41 | *(carried forward unchanged from v13)* | — | *(see v13 for full text of each criterion)* |
| C-42 | **STEP 0A INERTIA ANCHOR present** | structure | A named anchor block, labeled "STEP 0A INERTIA ANCHOR" or equivalent, is present at Phase 2 entry before any proposal option, requiring verbatim copy of all three Step 0a inertia costs. Structural parallel to STEP 0C CONTRACT ANCHOR at Phase 3 entry. |
| C-43 | **STEP 0C CONTRACT ANCHOR present** | structure | A named anchor block, labeled "STEP 0C CONTRACT ANCHOR" or equivalent, is present at Phase 3 entry before pitch writing, containing the voice contract sentences for all three audiences verbatim, with explicit instruction to copy them from Step 0c. |
| C-44 | **CITATION FORM REQUIREMENT present** | structure | A named requirement block, labeled "CITATION FORM REQUIREMENT" or equivalent, is present in the Citation Audit, specifying the required form (Form A or Form B) for the verbatim citation that must appear in the Defeating Do Nothing block. |
| C-45 | **ANCHOR GATE present** | structure | A named gate block, labeled "ANCHOR GATE" or equivalent, is positioned immediately after STEP 0C CONTRACT ANCHOR, explicitly blocking pitch writing until the STEP 0C CONTRACT ANCHOR block is complete and all three audience contract sentences are present. |
| C-46 | **IMPERATIVE REGISTER throughout** | register | All structural instructions in the skill prompt use imperative mode throughout. The skill addresses the executor directly with imperative constructions ("Write", "Fill in", "Halt and state", "Verify") rather than descriptive constructions ("The skill writes", "The column should be filled", "The skill halts when"). Named block labels (e.g., "STEP 0C SOURCE BINDING", "COLUMN-HEADER REQUIREMENT") are excluded from register evaluation — only the instructional body text must be imperative. A single structural section using descriptive phrasing for instructions fails C-46. |
| C-47 | **GATE CHAIN REQUIREMENT statement present** | structure | A named requirement statement, labeled "GATE CHAIN REQUIREMENT" or equivalent, explicitly declares that all four Phase 0 steps must be present as named sequential gates. The statement separately and explicitly requires that Steps 0a, 0b, 0c, and 0d each appear as labeled, ordered gate elements in Phase 0. The Phase 0 gate chain (C-09) alone does not pass C-47; a distinct named requirement statement referencing all four steps must be present. Structural dependency: requires C-09; if C-09 fails, C-47 fails. |
| C-48 | **INERTIA ANCHOR GATE present** | structure | A named gate block, labeled "INERTIA ANCHOR GATE" or equivalent, is positioned immediately after the STEP 0A INERTIA ANCHOR block, explicitly blocking proposal option writing until all three inertia costs are present in the anchor block. The gate body must use imperative register and name the blocking condition. Completes the inertia cost chain: define (Step 0a) → anchor (STEP 0A INERTIA ANCHOR) → **GATE** → options. Structural parallel to ANCHOR GATE (C-45). Structural dependency: requires STEP 0A INERTIA ANCHOR (C-42); if that block is absent, C-48 fails. The STEP 0A INERTIA ANCHOR block alone does not pass C-48. |
| C-49 | **STEP 0B STABILITY ANCHOR present** | structure | A named anchor block, labeled "STEP 0B STABILITY ANCHOR" or equivalent, is positioned in Phase 0 before the Defeating Do Nothing block, containing the Step 0b STABILITY CITATION RECORD verbatim, with an explicit instruction that (a) the Defeating Do Nothing block must reproduce this record verbatim and (b) the Defeating Do Nothing block must not be written until this anchor is complete. Both the pasted record and the blocking instruction must be present. Structural dependency: requires STEP 0B CITATION BINDING; if that block is absent, C-49 fails. STEP 0B CITATION BINDING alone does not pass C-49. |
| C-50 | **PHASE GATE AUDIT SOURCE BINDING present** | structure | A named source binding block, labeled "PHASE GATE AUDIT SOURCE BINDING" or equivalent, is present within the Phase Gate Audit section, explicitly naming Phase 0 as the authoritative source for gate definitions, and carrying both (a) a statement that the audit does not redefine gate requirements and (b) an imperative instruction to verify conformance to the Phase 0 source rather than redefine it. Structural parallel to STEP 0C SOURCE BINDING in the Voice Compliance Audit. Structural dependency: requires the Phase Gate Audit section; if that section is absent, C-50 fails. A Phase Gate Audit without the named source binding block does not pass C-50. |
```

---

Three new criteria added: C-48 (INERTIA ANCHOR GATE), C-49 (STEP 0B STABILITY ANCHOR), C-50 (PHASE GATE AUDIT SOURCE BINDING). Denominator 39 → 42. V-05 is the sole first-ceiling at 42/42. V-01/V-02/V-03 score 40/42 (99.52), V-04 scores 41/42 (99.76).
