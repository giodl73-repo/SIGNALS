Reading the scorecard, the three variation titles are the signal source: each variation's **distinctive mechanism** is the candidate criterion. Let me extract them.

**V-01 "IF-\* Forward Mesh Pre-Declaration"** — Role 0 pre-declares expected TC-2/TC-3 IF-\* assignments before cataloging; Role 1 confirms or ⚠-flags each. Not just producing labels, but creating a declared expectation set that must be verified → **C-21**

**V-02 "TC-1 IF-\* Annotation Column"** — Extends IF-\* annotation to TC-1 (candidate conditions), so all three catalog types carry the column. C-20 only requires TC-2/TC-3 → **C-22**

**V-03 "Orphaned IF-\* Detection Gate"** — The "Mesh Completeness Check" in the C-20 evidence line is the tell: a dedicated gate that flags any IF-\* label that exists in the pre-analysis artifact but has no TC entry annotation AND no downstream pathology citation → **C-23**

Denominator: /13 → /16.

---

```markdown
# Flow-Trigger Skill — Evaluation Rubric (v8)

*Signal source: quest simulation runs, Rounds 1–11.*
*Last updated: 2026-03-15*

---

## Essential Criteria (60%)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Trigger Table Present** | format | A table enumerating discovered triggers with YES/NO firing status is present |
| C-02 | **Side-Effect Detection** | behavior | Side effects of firing triggers are identified and enumerated |
| C-03 | **Pathology Detection** | behavior | At least one pathology section (storm, missing trigger, circular dependency) is evaluated |
| C-04 | **Condition Clarity** | depth | Each trigger's firing condition is stated without ambiguity; environment/solution layer named |
| C-05 | **Boundary / Scope Identification** | behavior | Scope of analysis is declared — which solution, environment, or automation boundary applies |
| C-06 | **Multi-Trigger Interaction** | depth | Interactions between triggers (cascade, race, mutual exclusion) are surfaced |
| C-07 | **Environment / Solution Layer Named** | depth | The environment and solution layer are explicitly named; response-scoped claims without layer attribution do not pass |

*All four non-optional essentials (C-01 through C-04) must pass for Gold.*

---

## Recommended Criteria (30%)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Boundary / Scope Identification** | behavior | Scope of analysis declared |
| C-06 | **Multi-Trigger Interaction** | depth | Cascade, race, mutual-exclusion interactions surfaced |
| C-07 | **Environment / Solution Layer Named** | depth | Layer explicitly named; ambiguous; environment/solution layer named |

*Wait — let me reconstruct from the provided rubric correctly.*
```

---

Let me write this cleanly from the provided v7 content:

```markdown
# Flow-Trigger Skill — Evaluation Rubric (v8)

*Signal source: quest simulation runs, Rounds 1–11.*
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

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)
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
| v5 | 2026-03-14 | Added C-16 (verdict-first pathology, R4 V-05 PASS+), C-17 (typed threat catalog cross-reference, R4 V-04 uplift); denominator /10 → /10 |
| v6 | 2026-03-15 | Added C-18 (pre-analysis role for failure mode ownership, R9 V-04), C-19 (three-layer remediation cross-reference, R9 V-04); denominator /10 → /12 |
| v7 | 2026-03-15 | Added C-20 (threat catalog IF-* back-reference, R10 universal signal — all five variations); denominator /12 → /13 |
| v8 | 2026-03-15 | Added C-21 (IF-* forward mesh pre-declaration, R11 V-01), C-22 (full-catalog IF-* annotation — TC-1 extension, R11 V-02), C-23 (orphaned IF-* detection gate, R11 V-03); denominator /13 → /16 |
```

---

**Three criteria extracted, one per variation title:**

| New ID | Source Signal | Core Mechanism |
|--------|--------------|----------------|
| C-21 | R11 V-01 "Forward Mesh Pre-Declaration" | Pre-analysis role publishes expected TC-2/TC-3 assignments *before* cataloging; cataloger confirms or ⚠-flags each |
| C-22 | R11 V-02 "TC-1 IF-\* Annotation Column" | Extends IF-\* annotation from TC-2/TC-3 (C-20) to TC-1 — all three catalog types carry the field |
| C-23 | R11 V-03 "Orphaned IF-\* Detection Gate" | Dedicated completeness gate; any IF-\* label without both a TC annotation *and* a pathology citation is flagged orphaned |

The dependency chain now has a closure check: C-18 → C-21 (pre-declaration) → C-20/C-22 (TC annotation) → C-23 (completeness gate) → C-18/C-19 (downstream citation). C-23 is the only criterion that reads the entire mesh from outside and flags gaps.
