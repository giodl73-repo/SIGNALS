```markdown
# flow-trigger Rubric — v6

## Essential Criteria (60%)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Unified Trigger Table** | format | Single table covering all registered triggers with YES/NO Fires? column; no row may omit the Fires? value |
| C-02 | **Trigger Inputs/Outputs** | depth | Each trigger has at least one concrete input and one concrete output |
| C-03 | **Firing Sequence** | format | Integer `#` for YES rows; `--` for NO rows; explicit enforcement rule stated |
| C-04 | **Pathology Detection** | coverage | All three pathology types addressed — flagged with evidence or confirmed absent |

## Recommended Criteria (30%)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Side Effects** | depth | At least one side effect per trigger that has one; clean triggers noted |
| C-06 | **Condition Evaluation** | correctness | Gate conditions stated per trigger; "always fires" claims justified |
| C-07 | **Scenario Boundary** | format | Triggering change unambiguous; environment/solution layer named |

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

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

**Golden threshold**: all 4 essential pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Output is trustworthy and production-useful |
| Silver | 60-79 or 1 essential miss | Useful but requires human verification |
| Bronze | 40-59 | Partial signal; major gaps present |
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
```

---

Two notes on the additions:

**C-18** extends C-14's role accountability model into the pre-analysis phase. C-14 assigns named roles to output sections; C-18 requires a role whose *sole* product is a failure mode catalog that precedes Phase 1A. The IF-* label requirement on pathology verdicts creates a traceable thread from pre-analysis through detection.

**C-19** is a closure criterion: it only fires if C-18 is also satisfied, because the IF-* label it requires can only exist if the pre-analysis artifact exists. A response earning C-08 + C-17 but not C-18 cannot earn C-19 — the third layer has no source to cite.
