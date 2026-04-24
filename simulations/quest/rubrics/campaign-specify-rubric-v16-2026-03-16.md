Three new patterns from R15. Two are fully evidenced (V-01 and V-02 watches); the third (STEP 0B FORWARD AUDIT NOTICE) is named in the scorecard intro as the third axis but its V-03 section wasn't included. I'll derive C-53 from the structural parallel with C-45 and note the inference.

Denominator: 42 → 45. V-05 is the first ceiling at 45/45.

```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v16
date: 2026-03-17
source_rounds: R1–R15
denominator: 45
---

# draft-spec Skill Rubric — v16

## What changed from v15 — 3 new criteria

| Change | Pattern Source | What it addresses |
|--------|----------------|-------------------|
| **C-51** (new) | R15 V-01 (first appearance) — scorecard V-01 watch: "STABILITY ANCHOR GATE present — named gate immediately after STEP 0B STABILITY ANCHOR, prohibiting Defeating Do Nothing writing before anchor is complete. Structural parallel to INERTIA ANCHOR GATE (gate after STEP 0A INERTIA ANCHOR) and ANCHOR GATE (gate after STEP 0C CONTRACT ANCHOR). Completes citation chain gate position (define → anchor → **GATE** → requirement → backward-bind)." Stable in V-04 and V-05. R14 V-05 baseline carries STEP 0B STABILITY ANCHOR but no gate after it; C-51 is absent from all R14 variations. | *STABILITY ANCHOR GATE — a named gate block, labeled "STABILITY ANCHOR GATE" or equivalent, positioned immediately after the STEP 0B STABILITY ANCHOR block, explicitly blocking Defeating Do Nothing writing until the STEP 0B STABILITY ANCHOR is complete.* The gate body must use imperative register and name the blocking condition: no Defeating Do Nothing block may be written before the stability anchor is complete. Structural parallel to INERTIA ANCHOR GATE (C-48), which blocks proposal option writing until STEP 0A INERTIA ANCHOR is complete, and ANCHOR GATE (C-45), which blocks pitch writing until STEP 0C CONTRACT ANCHOR is complete. Completes the citation chain's gate position: define (Step 0b) → anchor (STEP 0B STABILITY ANCHOR) → **GATE** → requirement (CITATION FORM REQUIREMENT) → backward-bind (STEP 0B CITATION BINDING). Structural dependency: requires STEP 0B STABILITY ANCHOR (C-49); if that block is absent, C-51 fails. The STEP 0B STABILITY ANCHOR alone (without the gate) does not pass C-51. |
| **C-52** (new) | R15 V-02 (first appearance) — scorecard V-02 watch: "STEP 0A INERTIA BINDING present in Phase Gate Audit — 'The inertia costs confirmed below were authored in Step 0a above. This audit does not redefine the inertia costs... do not rephrase, condense, or substitute them.' Named source-binding block for inertia costs parallel to STEP 0B CITATION BINDING (cites Step 0b) and STEP 0C SOURCE BINDING (cites Step 0c). Completes inertia cost chain backward-bind position (define → anchor → gate → **BACKWARD-BIND**)." Stable in V-04 and V-05. R14 V-05 baseline carries Phase Gate Audit but no named inertia source-binding block within it; C-52 is absent from all R14 variations. | *STEP 0A INERTIA BINDING — a named source-binding block, labeled "STEP 0A INERTIA BINDING" or equivalent, present in the Phase Gate Audit section, explicitly naming Step 0a as the authoring source of the inertia costs being confirmed in the audit, with an instruction not to redefine, rephrase, condense, or substitute them.* The block must both (a) identify Step 0a as the source and (b) carry the non-redefinition instruction. Structural parallel to STEP 0B CITATION BINDING (cites Step 0b as source of the stability citation record in the Citation Audit) and STEP 0C SOURCE BINDING (cites Step 0c as source of gate definitions in the Voice Compliance Audit). Completes the inertia cost chain's backward-bind position: define (Step 0a) → anchor (STEP 0A INERTIA ANCHOR) → gate (INERTIA ANCHOR GATE) → **BACKWARD-BIND** (STEP 0A INERTIA BINDING). Structural dependency: requires Phase Gate Audit section; if absent, C-52 fails. A Phase Gate Audit without the named inertia source-binding block does not pass C-52. |
| **C-53** (new) | R15 V-03 (first appearance) — named as the third new axis in the R15 scorecard baseline: "The three new axes (STABILITY ANCHOR GATE, STEP 0A INERTIA BINDING, STEP 0B FORWARD AUDIT NOTICE) are above the v15 denominator." Structural parallel to FORWARD AUDIT NOTICE (C-45) in Step 0c, which names the Voice Compliance Audit as the downstream verifier. STEP 0B FORWARD AUDIT NOTICE completes the forward-pointing position in the Step 0b chain (define → **FORWARD AUDIT NOTICE** → anchor → gate → backward-bind). V-03 scorecard section not included in scoring input; criterion derived from structural analogy with C-45 and the named chain position. Stable in V-05. | *STEP 0B FORWARD AUDIT NOTICE — a named forward audit notice, labeled "STEP 0B FORWARD AUDIT NOTICE" or equivalent, present in Step 0b, naming the downstream audit(s) that will verify the Step 0b content.* The notice must identify at least one named downstream section (e.g., Citation Audit, Phase Gate Audit) as the verifier of Step 0b content. Structural parallel to FORWARD AUDIT NOTICE (C-45) in Step 0c, which names the Voice Compliance Audit as the downstream verifier of the Step 0c voice contracts. Completes the Step 0b chain's forward-pointing position: define (Step 0b) → **FORWARD AUDIT NOTICE** → anchor (STEP 0B STABILITY ANCHOR) → gate (STABILITY ANCHOR GATE) → backward-bind (STEP 0B CITATION BINDING). Structural dependency: requires Step 0b; if Step 0b is absent, C-53 fails. Step 0b without the named forward audit notice block does not pass C-53. |

**Scoring formula**: `aspirational_pass / 45 * 10` (denom 42 → 45)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 45 * 10)
```

**R15 scores under v16:**

| Variation | Unique addition(s) | Asp earned | Asp (of 45) | Composite | Note |
|-----------|--------------------|------------|-------------|-----------|------|
| V-01 | STABILITY ANCHOR GATE | C-09–C-50 + C-51 | 43/45 | 99.56 | Introduces STABILITY ANCHOR GATE (C-51); fails C-52 (no STEP 0A INERTIA BINDING) and C-53 (no STEP 0B FORWARD AUDIT NOTICE) |
| V-02 | STEP 0A INERTIA BINDING | C-09–C-50 + C-52 | 43/45 | 99.56 | Introduces STEP 0A INERTIA BINDING (C-52); fails C-51 (no STABILITY ANCHOR GATE) and C-53 (no STEP 0B FORWARD AUDIT NOTICE) |
| V-03 | STEP 0B FORWARD AUDIT NOTICE | C-09–C-50 + C-53 | 43/45 | 99.56 | Introduces STEP 0B FORWARD AUDIT NOTICE (C-53); fails C-51 (no STABILITY ANCHOR GATE) and C-52 (no STEP 0A INERTIA BINDING) |
| V-04 | V-01 + V-02 combined | C-09–C-50 + C-51 + C-52 | 44/45 | 99.78 | Carries STABILITY ANCHOR GATE (C-51) + STEP 0A INERTIA BINDING (C-52); fails C-53 (no STEP 0B FORWARD AUDIT NOTICE) |
| V-05 | V-01 + V-02 + V-03 combined | C-09–C-53 (all 45) | 45/45 | 100.00 | First ceiling under v16 — all three new patterns present simultaneously |

C-51 is stable in V-01, V-04, V-05. C-52 is stable in V-02, V-04, V-05. C-53 is stable in V-03, V-05. V-05 is the only variation to carry all three simultaneously and the only first-ceiling under v16.

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

### Aspirational (denominator: 45)

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
| C-45 | **FORWARD AUDIT NOTICE present in Step 0c** | structure | A named forward audit notice, labeled "FORWARD AUDIT NOTICE" or equivalent, is present in Step 0c, naming the Voice Compliance Audit as the downstream verifier of the Step 0c voice contracts. |
| C-46 | **All gates use imperative blocking register** | style | Every gate block in Phase 0 and at phase transitions uses imperative register: "Do not begin...", "Do not advance...", "Do not save...", or equivalent. Descriptive register ("this section is completed before...") does not pass. |
| C-47 | **GATE CHAIN REQUIREMENT names all four steps and all three gates** | structure | A named block, labeled "GATE CHAIN REQUIREMENT" or equivalent, is present in Phase 0, explicitly naming all four steps (0a, 0b, 0c, 0d) and all three gates, and stating that all must complete before Phase 1 begins. |
| C-48 | **INERTIA ANCHOR GATE present** | structure | A named gate block, labeled "INERTIA ANCHOR GATE" or equivalent, positioned immediately after the STEP 0A INERTIA ANCHOR block, explicitly blocking proposal option writing until all three inertia costs are present in the anchor block. The gate body must use imperative register and name the blocking condition. Structural dependency: requires STEP 0A INERTIA ANCHOR (C-42); if that block is absent, C-48 fails. |
| C-49 | **STEP 0B STABILITY ANCHOR present** | structure | A named anchor block, labeled "STEP 0B STABILITY ANCHOR" or equivalent, positioned in Phase 0 before the Defeating Do Nothing block, containing the Step 0b STABILITY CITATION RECORD verbatim, with an explicit instruction requiring that the Defeating Do Nothing block reproduce this record verbatim and not be written until this anchor is complete. The anchor must both (a) hold the pasted record and (b) carry the blocking instruction forward. Structural dependency: requires STEP 0B CITATION BINDING; if that block is absent, C-49 fails. |
| C-50 | **PHASE GATE AUDIT SOURCE BINDING present** | structure | A named source binding block, labeled "PHASE GATE AUDIT SOURCE BINDING" or equivalent, within the Phase Gate Audit section, explicitly naming Phase 0 as the authoritative source for gate definitions and carrying the instruction not to redefine the gate chain in the audit — only to verify conformance. The block must contain both (a) a statement that the audit does not redefine gate requirements and (b) an imperative instruction to verify conformance to the Phase 0 source rather than redefine it. Structural dependency: requires the Phase Gate Audit section; if absent, C-50 fails. |
| C-51 | **STABILITY ANCHOR GATE present** | structure | A named gate block, labeled "STABILITY ANCHOR GATE" or equivalent, positioned immediately after the STEP 0B STABILITY ANCHOR block, explicitly blocking Defeating Do Nothing writing until the STEP 0B STABILITY ANCHOR is complete. The gate body must use imperative register and name the blocking condition: no Defeating Do Nothing block may be written before the stability anchor is complete. Structural parallel to INERTIA ANCHOR GATE (C-48) and ANCHOR GATE (C-45). Completes the citation chain's gate position: define → anchor (STEP 0B STABILITY ANCHOR) → **GATE** → requirement → backward-bind. Structural dependency: requires STEP 0B STABILITY ANCHOR (C-49); if that block is absent, C-51 fails. The STEP 0B STABILITY ANCHOR alone (without the gate) does not pass C-51. |
| C-52 | **STEP 0A INERTIA BINDING present in Phase Gate Audit** | structure | A named source-binding block, labeled "STEP 0A INERTIA BINDING" or equivalent, present in the Phase Gate Audit section, explicitly naming Step 0a as the authoring source of the inertia costs being confirmed in the audit, with an instruction not to redefine, rephrase, condense, or substitute them. The block must both (a) identify Step 0a as the source and (b) carry the non-redefinition instruction. Structural parallel to STEP 0B CITATION BINDING (cites Step 0b) and STEP 0C SOURCE BINDING (cites Step 0c). Completes the inertia cost chain's backward-bind position: define → anchor → gate → **BACKWARD-BIND**. Structural dependency: requires Phase Gate Audit section; if absent, C-52 fails. |
| C-53 | **STEP 0B FORWARD AUDIT NOTICE present** | structure | A named forward audit notice, labeled "STEP 0B FORWARD AUDIT NOTICE" or equivalent, present in Step 0b, naming the downstream audit(s) that will verify the Step 0b content. The notice must identify at least one named downstream section (e.g., Citation Audit, Phase Gate Audit) as the verifier of Step 0b content. Structural parallel to FORWARD AUDIT NOTICE (C-45) in Step 0c, which names the Voice Compliance Audit as the downstream verifier. Completes the Step 0b chain's forward-pointing position: define (Step 0b) → **FORWARD AUDIT NOTICE** → anchor → gate → backward-bind. Structural dependency: requires Step 0b; if absent, C-53 fails. Step 0b without the named forward audit notice does not pass C-53. |
```

---

**Three new criteria: C-51, C-52, C-53. Denominator 42 → 45.**

The structural chains are now complete for both Step 0a and Step 0b:

| Step | Define | Forward Notice | Anchor | Gate | Backward-Bind |
|------|--------|----------------|--------|------|---------------|
| 0a | Step 0a (inertia costs) | — | C-42 STEP 0A INERTIA ANCHOR | C-48 INERTIA ANCHOR GATE | C-52 STEP 0A INERTIA BINDING |
| 0b | Step 0b (citation record) | C-53 STEP 0B FORWARD AUDIT NOTICE | C-49 STEP 0B STABILITY ANCHOR | C-51 STABILITY ANCHOR GATE | existing STEP 0B CITATION BINDING |
| 0c | Step 0c (voice contracts) | C-45 FORWARD AUDIT NOTICE | C-43 STEP 0C CONTRACT ANCHOR | C-45-adjacent ANCHOR GATE | C-50-adjacent STEP 0C SOURCE BINDING |
