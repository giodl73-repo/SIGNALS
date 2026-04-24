Good — the v8 file is complete. C-08 through C-23 gives 16 aspirational criteria. The three JSON patterns become C-24, C-25, C-26 → denominator /16 → /19.

```markdown
# Flow-Trigger Skill — Evaluation Rubric (v9)

*Signal source: quest simulation runs, Rounds 1–12.*
*Last updated: 2026-03-15*

---

## Essential Criteria (60%)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Trigger Table Present** | format | A table enumerating discovered triggers with YES/NO firing status is present |
| C-02 | **Side-Effect Detection** | behavior | Side effects of firing triggers are identified and enumerated |
| C-03 | **Pathology Detection** | behavior | At least one pathology section (storm, missing trigger, circular dependency) is evaluated |
| C-04 | **Condition Clarity** | depth | Each trigger's firing condition is stated without ambiguity; environment/solution layer named |

*All four essentials must pass for Gold.*

---

## Recommended Criteria (30%)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Boundary / Scope Identification** | behavior | Scope of analysis is declared — which solution, environment, or automation boundary applies |
| C-06 | **Multi-Trigger Interaction** | depth | Interactions between triggers (cascade, race, mutual exclusion) are surfaced |
| C-07 | **Environment / Solution Layer Named** | depth | The environment and solution layer are explicitly named; response-scoped claims without layer attribution do not pass |

---

## Aspirational Criteria (10%)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Remediation Recommendations** | behavior | Every flagged pathology has an actionable remediation referencing specific PA/Copilot Studio constructs |
| C-09 | **Trigger Storm Quantification** | depth | Storm depth as a number or range; budget impact in PP request limits or run duration; hedged estimates fail |
| C-10 | **Proactive Budget Gate** *(new — R1 V-05)* | behavior | Budget section (storm depth, API requests, platform limit, budget consumed, run duration) present whenever M >= 3 AND any side effect exists — structured as a numbered section before pathology detection; does not wait for a confirmed storm verdict |
| C-11 | **Dual-Population Table** *(new — R1 V-05)* | format | Single unified table with `Fires? YES/NO` per row, including explicit per-row enforcement rule ("YES or NO only — no row may omit this column"); separate registered/firing lists do not satisfy this criterion |
| C-12 | **Registry Summary Code Block** *(new — R2 V-04/V-05)* | format | A structured code-fence or fixed-format block immediately following the trigger table declares M (firing triggers with side effects), N (all firing triggers), and Non-firing counts as explicit downstream-referenceable variables; implicit counts derived by row-counting the table do not satisfy this criterion |
| C-13 | **Per-Automation Calculation Basis** *(new — R2 V-04/V-05)* | depth | Budget section includes per-automation arithmetic showing additive action count components (e.g., "Flow A calls N Dataverse actions + M connector actions = X requests per invocation"); aggregate totals without per-automation intermediate arithmetic do not satisfy this criterion |
| C-14 | **Specialist Role Accountability Chain** *(new — R3 V-03)* | behavior | Distinct named roles (e.g., Registry Analyst, Pathology Analyst, Budget Analyst) assigned explicit accountability for at least three distinct output sections or columns; a single undifferentiated analyst role or generic expertise framing does not satisfy this criterion |
| C-15 | **Threat-First Phase Pre-Cataloging** *(new — R3 V-05)* | depth | A distinct pre-phase catalogs the threat surface — triggering automations, potential cascade paths, side-effect scope — before the trigger table is written; trigger table rows and pathology section reference named threats from the catalog; inline discovery during table construction does not satisfy this criterion even if coverage is complete |
| C-16 | **Verdict-First Pathology Structure** *(new — R4 V-05)* | format | Each pathology subsection opens with its verdict keyword (`DETECTED`, `NOT DETECTED`, or `INDETERMINATE`) as the first content element on its own line before any supporting evidence; subsections that build toward a verdict or embed it in prose do not satisfy this criterion even if the verdict word appears |
| C-17 | **Typed Threat Catalog Cross-Reference** *(new — R4 V-04)* | depth | The pre-phase produces at least two distinctly typed catalog sections (e.g., TC-1 candidate conditions, TC-2 cascade paths, TC-3 side effects), and at least two downstream sections (Condition column, Side Effects column, or pathology section) cite catalog entries by their type-number designation; prose references to a generic named catalog without typed numbering do not satisfy this criterion |
| C-18 | **Pre-Analysis Role for Failure Mode Ownership** *(new — R9 V-04)* | behavior | A named pre-analysis role (e.g., Inertia Analyst) distinct from all technical analyst roles produces a first-class failure mode artifact (e.g., IF-Storm, IF-Missing, IF-Circular labeled entries) before the threat-cataloging phase; pathology DETECTED and INDETERMINATE verdicts cross-reference the applicable failure mode label by name; C-14 requires named roles for output sections — this criterion extends accountability to the pre-analysis phase with its own artifact; output-section roles without a dedicated pre-analysis artifact do not satisfy this criterion |
| C-19 | **Three-Layer Remediation Cross-Reference** *(new — R9 V-04)* | depth | Each DETECTED or INDETERMINATE remediation entry cites all three layers: a specific PA/Copilot Studio construct (satisfying C-08), a TC-type-numbered catalog entry (satisfying C-17), and the IF-* failure mode label from the pre-analysis artifact that the remediation resolves; remediation entries satisfying C-08 and C-17 without IF-* loop closure do not satisfy this criterion; this criterion requires a C-18-compliant pre-analysis artifact to exist upstream |
| C-20 | **Threat Catalog IF-\* Back-Reference** *(new — R10, all variations)* | depth | TC-2 (cascade paths) and TC-3 (side-effect scope) entries annotate the applicable IF-* failure mode label from the pre-analysis artifact during threat cataloging — creating a bidirectional reference mesh between the failure mode catalog and the threat catalog; annotations must appear within the TC-2 and TC-3 entries themselves; downstream IF-* citations in the pathology section (C-18) or remediation (C-19) without TC-entry-level annotations do not satisfy this criterion; requires a C-18-compliant pre-analysis artifact upstream |
| C-21 | **IF-\* Forward Mesh Pre-Declaration** *(new — R11 V-01)* | depth | The pre-analysis role (C-18) pre-declares the expected IF-* label assignments for TC-2 and TC-3 entries before threat cataloging executes — publishing a declared expectation set that the threat cataloger must subsequently confirm or ⚠-flag per entry; a threat cataloger that independently discovers and assigns IF-* labels without a pre-declared expectation set to confirm or challenge does not satisfy this criterion; requires a C-18-compliant pre-analysis artifact upstream |
| C-22 | **Full-Catalog IF-\* Annotation** *(new — R11 V-02)* | depth | All three typed catalog sections — TC-1 (candidate conditions), TC-2 (cascade paths), and TC-3 (side-effect scope) — carry IF-* annotation columns or inline fields, extending the C-20 requirement to candidate condition entries; TC-1 entries that omit IF-* annotations while TC-2 and TC-3 carry them do not satisfy this criterion; requires a C-18-compliant pre-analysis artifact upstream |
| C-23 | **Orphaned IF-\* Detection Gate** *(new — R11 V-03)* | behavior | A dedicated completeness gate (e.g., Mesh Completeness Check) verifies that every IF-* label declared in the pre-analysis artifact appears in at least one TC entry annotation (satisfying C-20 or C-22) and at least one downstream pathology verdict citation (satisfying C-18); any IF-* label that exists in the pre-analysis artifact but is absent from TC annotations or absent from pathology citations is flagged as orphaned with an explicit ⚠ marker; a completeness check that verifies only downstream citations without TC-annotation coverage, or only TC-annotation coverage without downstream citations, does not satisfy this criterion; requires a C-18-compliant pre-analysis artifact upstream |
| C-24 | **Verbatim-Emit Caption Instruction** *(new — R12 V-02/V-05)* | format | At least one enforcement instruction is written as a caption directive requiring verbatim emission immediately after a structural artifact (e.g., "Caption (emit this text verbatim immediately after the table): [text]"), converting the rule from a prompt-side directive the model applies silently into a required output artifact that can be independently verified; enforcement instructions that appear only as narrative mandates without a verbatim-emit directive do not satisfy this criterion even if the model emits compliant output |
| C-25 | **Schema Field Inline Annotation** *(new — R12 V-02/V-05)* | format | Schema definitions for structured output artifacts (tables, code blocks, registry summaries) include inline field-level annotations binding each requirement to the exact output position the model must populate (e.g., `environment: string  <- specific named environment only`); requirement bindings that appear only in narrative enforcement sections outside the schema definition do not satisfy this criterion |
| C-26 | **Mesh Closure Certificate** *(new — R12, all variations)* | behavior | A required final certificate block unifies all four coverage dimensions — TC-2/TC-3 IF-* annotation (C-20), TC-1 IF-* annotation (C-22), forward mesh fulfillment (C-21 declared expectations confirmed or ⚠-flagged), and pathology verdict citation (C-18) — into a single PASS/FAIL/N/A audit row per IF-* label; scattered per-section coverage checks that are not consolidated into a single certificate artifact do not satisfy this criterion; requires a C-18-compliant pre-analysis artifact upstream |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 19 * 10)
```

**Golden threshold**: all 4 essential pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Output is trustworthy and production-useful |
| Silver | 60–79 or 1 essential miss | Useful but requires human verification |
| Bronze | 40–59 | Partial signal; major gaps present |
| Fail | < 40 or 2+ essential miss | Not usable; regenerate |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-14 | Initial — C-01 through C-07 |
| v2 | 2026-03-14 | Added C-08 through C-11 from R1 excellence signals |
| v3 | 2026-03-14 | Added C-12, C-13 from R2 V-04/V-05 signals; denominator /6 → /8 |
| v4 | 2026-03-14 | Added C-14, C-15 from R3 V-03/V-05 signals; denominator /8 → /10 |
| v5 | 2026-03-14 | Added C-16 (verdict-first pathology, R4 V-05), C-17 (typed threat catalog cross-reference, R4 V-04); denominator /10 → /10 |
| v6 | 2026-03-15 | Added C-18 (pre-analysis role for failure mode ownership, R9 V-04), C-19 (three-layer remediation cross-reference, R9 V-04); denominator /10 → /12 |
| v7 | 2026-03-15 | Added C-20 (threat catalog IF-* back-reference, R10 universal signal); denominator /12 → /13 |
| v8 | 2026-03-15 | Added C-21 (IF-* forward mesh pre-declaration, R11 V-01), C-22 (full-catalog IF-* annotation, R11 V-02), C-23 (orphaned IF-* detection gate, R11 V-03); denominator /13 → /16 |
| v9 | 2026-03-15 | Added C-24 (verbatim-emit caption instruction, R12 V-02/V-05), C-25 (schema field inline annotation, R12 V-02/V-05), C-26 (mesh closure certificate, R12 all variations); denominator /16 → /19 |
```

---

Three criteria, one per JSON pattern:

| New ID | Source Signal | Core Mechanism |
|--------|--------------|----------------|
| C-24 | R12 V-02/V-05 verbatim-emit | Caption directive forces enforcement text into model output — makes the rule a verifiable artifact, not a silent directive |
| C-25 | R12 V-02/V-05 inline annotation | Field-level comments inside schema definitions bind requirements to exact output positions; narrative enforcement outside the schema does not satisfy |
| C-26 | R12 all variations mesh certificate | Single PASS/FAIL/N/A audit block per IF-* label unifying all four coverage dimensions — replaces four scattered checks with one verifiable compliance signal |

**C-24 and C-25 are prompt-engineering structure criteria** — they describe how the rubric prompt itself must be constructed to reliably elicit coverage. That is a first for this rubric: prior criteria describe output shape; these two describe instruction shape. Worth tracking whether they hold up as stable signals or drift as model behavior changes.
