Reading the R11 scorecard evidence carefully before writing. Two new patterns:

1. **C-40**: Pre-table explicit instruction reinforcing audience-discriminating cell values — first seen in V-02 (`"explicit pre-table instruction reinforces. Two mechanisms."`), carried through V-03/V-04/V-05. V-01 carries C-38 via template cells alone; this is the second mechanism.

2. **C-41**: Explicit `COLUMN-HEADER REQUIREMENT` statement reinforcing the Step 0c column header — first seen in V-05 (`"named explicitly in pre-table COLUMN-HEADER REQUIREMENT statement. Two mechanisms."`). V-01–V-04 carry C-39 via template header alone.

Denominator: 31 → 33. Scores under v12: V-01 31/33 (fails C-40, C-41), V-02–V-04 32/33 (fail C-41), V-05 33/33 (first ceiling).

---

```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v12
date: 2026-03-17
source_rounds: R1–R11
denominator: 33
---

# draft-spec Skill Rubric — v12

## What changed from v11 — 2 new criteria

| Change | Pattern Source | What it addresses |
|--------|----------------|-------------------|
| **C-40** (new) | R11 V-02 (first appearance) — C-38 evidence: "template cell values identical + explicit pre-table instruction reinforces. Two mechanisms." Confirmed stable in V-03 ("VCA unchanged from R10 V-02"), V-04 ("explicit pre-table instruction (from V-02) + template cell values"), and V-05 ("cell values unchanged from R10 V-02"). V-01 carries C-38 via template cell values alone and does not pass C-40. The dual-mechanism pattern — template cells plus a named instructional statement — is the stable structural form across V-02 through V-05. | *Pre-table explicit instruction reinforcing audience-discriminating cell values.* When C-38 passes, the skill prompt includes a standalone instructional statement before the VCA table — separate from the template's cell values — that explicitly names the audience-discriminating cell value format (e.g., "Each cell in the contract column must read 'Step 0c [audience] voice contract satisfied'", or equivalent). Template cell values alone (C-38) do not pass C-40; a distinct named instruction must be present. Structural dependency: requires C-38; if C-38 fails, C-40 fails. |
| **C-41** (new) | R11 V-05 (first appearance) — C-39 evidence: "column header present in template AND named explicitly in pre-table COLUMN-HEADER REQUIREMENT statement. Two mechanisms." V-01 through V-04 carry C-39 via the column header in the template alone; V-05 adds a second mechanism by including an explicit named requirement statement (labeled "COLUMN-HEADER REQUIREMENT" or equivalent) that separately states the exact column header format. No prior variation held both mechanisms for C-39. | *Explicit COLUMN-HEADER REQUIREMENT statement reinforcing the Step 0c column header.* When C-39 passes, the skill prompt includes an explicit named requirement statement — labeled "COLUMN-HEADER REQUIREMENT" or equivalent — that separately states the exact column header that must appear in the VCA table (e.g., "The third column header must read 'Step 0c Contract Verified'"). The column header in the template alone (C-39) does not pass C-41; a distinct named requirement statement must be present. Structural dependency: requires C-39; if C-39 fails, C-41 fails. |

**Scoring formula**: `aspirational_pass / 33 * 10` (denom 31 → 33)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 33 * 10)
```

**R11 scores under v12:**

| Variation | Asp earned | Asp (of 33) | Composite | Note |
|-----------|------------|-------------|-----------|------|
| V-01 | C-09–C-39 (all) | 31/33 | 99.39 | Fails C-40 (template cell values only, no pre-table instruction) and C-41 (template column header only, no COLUMN-HEADER REQUIREMENT statement) |
| V-02 | C-09–C-39, C-40 | 32/33 | 99.70 | Passes C-40 (explicit pre-table instruction present); fails C-41 (no COLUMN-HEADER REQUIREMENT statement) |
| V-03 | C-09–C-39, C-40 | 32/33 | 99.70 | VCA unchanged from R11 V-02; inherits C-40 pass; fails C-41 |
| V-04 | C-09–C-39, C-40 | 32/33 | 99.70 | Explicit pre-table instruction from V-02 retained under compression; fails C-41 |
| V-05 | C-09–C-41 (all 33) | 33/33 | 100.00 | First ceiling under v12 — template header (C-39) plus explicit COLUMN-HEADER REQUIREMENT statement (C-41); template cells (C-38) plus explicit pre-table instruction (C-40). Both dual-mechanism patterns present. |

C-40 is stable across V-02–V-05 (four variations); C-41 is introduced by V-05 alone. The v12 ceiling requires both dual-mechanism patterns to be simultaneously present — one for cell values, one for the column header.

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

### Aspirational (denominator: 33)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Phase 0 four-step gate chain present** | structure | Steps 0a, 0b, 0c, and 0d are each present as named, sequential gates in Phase 0. All four steps must be explicitly labeled and ordered. Missing or merged steps = fail. |
| C-10 | **Step 0a: topic extraction gate** | structure | Step 0a extracts the feature topic from the input and gates on topic clarity before proceeding. The extracted topic must be named as an output of Step 0a. |
| C-11 | **Step 0b: context loading gate** | structure | Step 0b loads relevant context (prior signals, related specs, domain constraints) and gates on context sufficiency before proceeding. |
| C-12 | **Step 0c: voice contract derivation gate** | structure | Step 0c derives the three audience-specific voice contracts (exec, developer, maker) and gates on all three being present before proceeding. The three contracts must be named as outputs of Step 0c. |
| C-13 | **Step 0d: readiness gate** | structure | Step 0d performs a final readiness check across Steps 0a–0c outputs and gates on overall readiness before proceeding to Phase 1. |
| C-14 | **STABILITY CITATION RECORD Form A present** | traceability | A STABILITY CITATION RECORD Form A is present in the skill. It names the source artifact(s) that anchor the stable elements carried into this version. |
| C-15 | **STABILITY CITATION RECORD Form B present** | traceability | A STABILITY CITATION RECORD Form B is present. It names the specific structural elements confirmed stable and the variation(s) that confirmed them. |
| C-16 | **Verbatim paste instruction in Defeating Do Nothing** | depth | The Defeating Do Nothing section includes an explicit verbatim-paste instruction directing the model to paste specific evidence directly into the output (not paraphrase). The instruction must be structurally present as a named directive. |
| C-17 | **Separate `#### Defeating Do Nothing` labeled header** | structure | The Defeating Do Nothing content appears under a standalone `#### Defeating Do Nothing` header — not merged with or subordinated to the Options section header. |
| C-18 | **Spec write gate before Phase 2** | sequencing | A write gate for the spec artifact is present between Phase 1 and Phase 2. Phase 2 cannot begin until the spec artifact has been written. The gate must be explicit and labeled. |
| C-19 | **Proposal write gate before Phase 3** | sequencing | A write gate for the proposal artifact is present between Phase 2 and Phase 3. Phase 3 cannot begin until the proposal artifact has been written. The gate must be explicit and labeled. |
| C-20 | **Pitch write gate gated on voice differentiation** | sequencing | The pitch write gate conditions pitch production on confirmed voice differentiation across the three audience versions. The gate does not pass if the three versions are not demonstrably distinct. |
| C-21 | **COMPLETION INDEX present** | completeness | A COMPLETION INDEX is present as a named section in the skill output or skill structure. It is labeled and distinct from the artifact content. |
| C-22 | **Artifact Existence Record in COMPLETION INDEX** | completeness | The COMPLETION INDEX contains an Artifact Existence Record section that confirms each of the three artifacts (spec, proposal, pitch) exists on disk. |
| C-23 | **Phase Gate Audit in COMPLETION INDEX** | traceability | The COMPLETION INDEX contains a Phase Gate Audit section that confirms each phase gate (spec, proposal, pitch) was passed in sequence. |
| C-24 | **Citation Audit in COMPLETION INDEX** | traceability | The COMPLETION INDEX contains a Citation Audit section that confirms stability citations (Form A and Form B) are present and populated. |
| C-25 | **Voice Compliance Audit in COMPLETION INDEX** | correctness | The COMPLETION INDEX contains a Voice Compliance Audit (VCA) section that audits the three audience voice contracts against the pitch output. |
| C-26 | **Phase 1 produces spec draft before gate** | sequencing | Phase 1 produces a spec draft as its primary output before the spec write gate is evaluated. The draft is the input to the gate, not produced after it. |
| C-27 | **Phase 2 produces proposal draft before gate** | sequencing | Phase 2 produces a proposal draft as its primary output before the proposal write gate is evaluated. |
| C-28 | **Phase 3 produces pitch draft before gate** | sequencing | Phase 3 produces a pitch draft as its primary output before the pitch write gate is evaluated. |
| C-29 | **Options in proposal are structurally parallel** | structure | All proposal options follow the same structural template: description, pros, cons, risk, effort. Options that omit one or more fields relative to other options do not pass. |
| C-30 | **Pitch hook is audience-specific per version** | differentiation | Each of the three pitch versions (exec, developer, maker) opens with a hook that is specific to that audience's concerns — not a generic hook reused across versions. |
| C-31 | **Call to action is audience-specific per version** | differentiation | Each of the three pitch versions closes with a call to action specific to that audience's role and decision-making context. A generic CTA applied across all three versions does not pass. |
| C-32 | **Self-review in spec names at least one constraint gap** | depth | The spec self-review section identifies at least one gap or ambiguity in the Constraints section specifically — not only in other sections. |
| C-33 | **Proposal recommendation names the rejected option(s)** | depth | The proposal recommendation explicitly names the option(s) rejected and states why each was not chosen. A recommendation that only argues for the chosen option without naming rejections does not pass. |
| C-34 | **Gate anchor: audience contract name + "satisfied" in gate parenthetical** | structure | The Voice Differentiation Gate parenthetical opens with the audience-specific contract name followed by "satisfied" as the pass condition prefix — e.g., `(Step 0c exec voice contract satisfied: ...)`. The parenthetical must name the contract and use "satisfied" as the pass verb. A gate parenthetical without the contract name, without the audience identifier, or without "satisfied" does not pass. |
| C-35 | **Voice Differentiation Gate evaluates all three audience contracts** | coverage | The Voice Differentiation Gate evaluates all three audience contracts (exec, developer, maker) in sequence before the pitch write gate is authorized. Evaluation of fewer than three contracts does not pass. |
| C-36 | **Verb consistency: "satisfied" in gate parentheticals and VCA table cells** | consistency | The verb "satisfied" is used in both the gate parenthetical pass condition prefix and in the VCA table cell values for the contract column. A variation that uses "satisfied" in one location but a different verb (e.g., "confirmed", "verified", "met") in the other does not pass. Both locations must use the same verb. |
| C-37 | **VCA uses three-column table format with Audience / Verdict / Step 0c Contract Verified** | structure | The Voice Compliance Audit is rendered as a three-column table. The column headers are: `Audience`, `Verdict`, and `Step 0c Contract Verified` (or a structurally equivalent header carrying the Step 0c step reference). A VCA rendered as prose, a two-column table, or a table with a contract column header that does not include the Step 0c step reference does not pass. |
| C-38 | **Audience identifier in contract attribution phrase** | differentiation | When C-34, C-36, and C-37 all pass, the contract attribution phrase used in the gate parenthetical and in each VCA table row's contract cell explicitly names the audience for that row — e.g., "Step 0c **exec** voice contract satisfied" for the exec row, "Step 0c **dev** voice contract satisfied" for the dev row, "Step 0c **maker** voice contract satisfied" for the maker row. A phrase without an embedded audience specifier — e.g., "Step 0c voice contract satisfied" applied generically — does not pass regardless of row or location. Structural dependency: requires C-34, C-36, and C-37; if any dependency fails, C-38 fails. |
| C-39 | **Step 0c step reference in VCA contract column header** | traceability | When C-37 passes, the contract column header includes "Step 0c" as an explicit workflow step reference — e.g., "Step 0c Contract Verified". A column header that names the verification action without the Step 0c step identifier — e.g., "Contract Check", "Voice Contract", "Verified" — does not pass. Structural dependency: requires C-37; if C-37 fails, C-39 fails. |
| C-40 | **Pre-table explicit instruction reinforcing audience-discriminating cell values** | reinforcement | When C-38 passes, the skill prompt includes a standalone instructional statement before the VCA table — separate from the template's cell values — that explicitly names the audience-discriminating cell value format required for the contract column (e.g., "Each row's contract cell must read 'Step 0c [audience] voice contract satisfied'" or equivalent named directive). The audience-discriminating template cell values alone (C-38) do not pass C-40; a distinct pre-table named instruction must be present as a second mechanism. Structural dependency: requires C-38; if C-38 fails, C-40 fails. |
| C-41 | **Explicit COLUMN-HEADER REQUIREMENT statement reinforcing the Step 0c column header** | reinforcement | When C-39 passes, the skill prompt includes an explicit named requirement statement — labeled "COLUMN-HEADER REQUIREMENT" or structural equivalent — that separately states the exact column header that must appear in the VCA table (e.g., "The third column header must read 'Step 0c Contract Verified'"). The column header present in the template alone (C-39) does not pass C-41; a distinct named requirement statement must be present as a second mechanism. Structural dependency: requires C-39; if C-39 fails, C-41 fails. |
```
