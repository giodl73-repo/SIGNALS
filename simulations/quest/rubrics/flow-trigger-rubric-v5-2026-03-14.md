Scanning the R4 scorecard for PASS+ signals and above-baseline differentiators not covered by C-08 through C-15.

**Two new patterns extracted:**

1. **V-05 PASS+ on C-04** — verdict-first pathology structure: each subsection opens with `DETECTED / NOT DETECTED / INDETERMINATE` as its first element before any evidence. Distinct from C-14 (role accountability) and C-08 (remediation); this is a *format* discipline inside the pathology section itself.

2. **V-04 above-baseline on C-04, C-05, C-06** — typed threat catalog cross-reference system (TC-1 candidate conditions, TC-2 cascade paths, TC-3 side effects). C-15 requires a pre-phase catalog but does not require typed numbering or downstream citation by type-number. V-04 earns the uplift specifically because `Condition` column cites TC-1, `Side Effects` column cites TC-3, and pathology section cites TC-2 cascade pairs — typed precision, not just a generic named catalog.

---

```markdown
# flow-trigger Rubric — v5

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
| C-16 | **Verdict-First Pathology Structure** *(new — R4 V-05)* | format | Each pathology subsection opens with its verdict keyword (`DETECTED`, `NOT DETECTED`, or `INDETERMINATE`) as the first content element on its own line before any supporting evidence; subsections that build toward a verdict or embed it in prose do not satisfy this criterion even if the verdict is present |
| C-17 | **Typed Threat Catalog Cross-Reference** *(new — R4 V-04)* | depth | The pre-phase produces at least two distinctly typed catalog sections (e.g., TC-1 candidate conditions, TC-2 cascade paths, TC-3 side effects), and at least two downstream sections (Condition column, Side Effects column, or pathology section) cite catalog entries by their type-number designation; prose references to a generic named catalog without typed numbering do not satisfy this criterion |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
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
| v4 | 2026-03-14 | Added C-14, C-15 from R3 V-03/V-05 signals; denominator /8 |
| v5 | 2026-03-14 | Added C-16 (verdict-first pathology, R4 V-05 PASS+), C-17 (typed threat catalog cross-reference, R4 V-04 uplift); denominator /8 → /10 |
```

---

Two criteria added:

- **C-16** captures the *format discipline* that earned V-05 its PASS+ on C-04 — verdict keyword leads each subsection, evidence follows. This is separable from C-14 (who does the analysis) and C-08 (what the remediation says).
- **C-17** captures V-04's typed numbering scheme (TC-1/TC-2/TC-3) that C-15 under-specifies. C-15 requires a pre-phase catalog with named references; C-17 requires the catalog be *typed and numbered* so downstream sections can cite by type-number — the precision that gave V-04 above-baseline on three criteria simultaneously.

Denominator moves from `/8` to `/10`; step size per aspirational criterion drops from ~1.25 to ~1.0 points.
