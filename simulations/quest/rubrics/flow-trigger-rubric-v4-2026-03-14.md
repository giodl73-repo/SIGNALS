Reading the R3 scorecard for excellence signals not yet captured in v3 criteria.

Two patterns emerge:

1. **PASS+ on C-04 for V-03** — specialist role handoff (Registry Analyst → Pathology Analyst → Budget Analyst) with named per-section accountability. This appears across C-04, C-05, and C-06 as a differentiator for V-03.

2. **PASS+ on C-04 for V-05** — threat-first Phase 1 pre-cataloging before the trigger table is written. Appears across C-04, C-05 as the V-05 structural differentiator.

Neither is captured by any existing C-08 through C-13 criterion.

---

# flow-trigger Rubric — v4

**Two new aspirational criteria** extracted from R3 scorecard PASS+ signals on C-04 (V-03 and V-05):

**C-14 — Specialist Role Accountability Chain** *(behavior)*
V-03 achieves PASS+ on C-04 (and above-baseline on C-05, C-06) by assigning distinct named roles — Registry Analyst, Pathology Analyst, Budget Analyst — each with explicit accountability for specific output sections and columns. A variation satisfies C-14 if named roles map 1:1 to at least three distinct output sections; generic "you are an expert" framing or a single undifferentiated analyst role does not satisfy this criterion. Role handoff creates fresh-eyes review of each section, which is why C-04 reaches PASS+: the Pathology Analyst cannot see the Registry Analyst's prior work and must derive pathology findings independently.

**C-15 — Threat-First Phase Pre-Cataloging** *(depth)*
V-05 achieves PASS+ on C-04 and above-baseline on C-05 by running a dedicated threat-surface phase (Phase 1) before the trigger table is written. This phase identifies triggering automations, potential cascade paths, and side-effect scope so that trigger table rows are pre-populated from a named threat catalog rather than discovered inline during table construction. A variation satisfies C-15 if a distinct pre-phase produces a named threat catalog that the trigger table and pathology sections reference by name; discovering threats inline during table construction does not satisfy this criterion even if coverage is complete.

**Scoring formula update**: aspirational denominator changes from `/6` to `/8`; max aspirational contribution stays at 10 points; composite ceiling unchanged at 100. Step size per criterion: ~1.67 → ~1.25.

---

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

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
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
| v1 | 2026-03-14 | Initial rubric — 4 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-14 | Added C-10 (Proactive Budget Gate) and C-11 (Dual-Population Table) from R1 V-05 excellence signals; aspirational pool expanded from 2 to 4; scoring denominator updated |
| v3 | 2026-03-14 | Added C-12 (Registry Summary Code Block) and C-13 (Per-Automation Calculation Basis) from R2 V-04/V-05 excellence signals; aspirational pool expanded from 4 to 6; scoring denominator updated |
| v4 | 2026-03-14 | Added C-14 (Specialist Role Accountability Chain) and C-15 (Threat-First Phase Pre-Cataloging) from R3 V-03/V-05 PASS+ signals on C-04; aspirational pool expanded from 6 to 8; scoring denominator updated |

---

**Key changes from v3:**

- **C-14** captures the specialist role structure from V-03. PASS+ on C-04 and above-baseline performance on C-05 and C-06 trace directly to the Registry Analyst / Pathology Analyst / Budget Analyst handoff chain. The mechanism is fresh-eyes review: each named role cannot assume the prior role's findings are complete, so each section gets independent verification. A prompt with a single analyst role — even a detailed one — does not produce the same structural independence. C-14 is satisfied only when named roles map 1:1 to at least three distinct output sections with explicit per-section accountability.

- **C-15** captures the threat-first pre-cataloging structure from V-05. PASS+ on C-04 and above-baseline on C-05 both cite Phase 1's threat surface as the cause. The difference from inline discovery is directional: inline discovery finds threats while building the table and may miss interactions between triggers not yet encountered; pre-cataloging names the full threat surface first so that every table row and every pathology finding is a lookup against a known set. A variation that discovers threats inline can still satisfy C-04 (coverage complete) and C-08 (remediation specific) while failing C-15 — the two criteria measure different properties of the same detection process.

- **Scoring denominator** for aspirational updated from `/6` to `/8`; aspirational max contribution stays at 10 points, so the composite ceiling is unchanged at 100. Step size per aspirational criterion changes from ~1.67 to ~1.25.
