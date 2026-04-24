Written to `simulations/quest/rubrics/org-review-rubric-2026-03-16.md`.

---

**Rubric summary — org-review v1**

| Tier | Criteria | Points | What they test |
|------|----------|--------|----------------|
| Essential | C-01 to C-05 | 60 | Role manifest filled, contract cited, CH-IDs traced, gate vector complete, §3 algebra evaluated mechanically |
| Recommended | C-06 to C-08 | 30 | Scope surfaces are artifact-specific, action register is CH-ID-sourced, cross-role signals are concrete |
| Aspirational | C-09 to C-10 | 10 | Null hypothesis names a real inertia alternative, domain findings are role-grounded |

**Golden threshold**: all 5 essential pass + composite >= 80.

The two sharpest failure modes to watch:
- **C-03** — CH-IDs silently dropped between BRACKET OPENING and downstream tables (most common early failure)
- **C-05** — disposition written editorially ("given the findings...") instead of mechanically evaluating the §3 formula
rectness | Each of BRACKET OPENING, DOMAIN, LIFECYCLE, and BRACKET CLOSING sections opens with the exact string "Contract: DISPOSITION_CONTRACT v1". Any missing cite = fail. |
| C-03 | CH-IDs assigned and fully traced | correctness | Every CH-ID (CH-001, CH-002, ...) assigned in BRACKET OPENING appears in: (a) the DOMAIN CH-ID Response Table, (b) the LIFECYCLE CH-ID Response Table, and (c) the BRACKET CLOSING CH-ID Final Assessment. Missing any row in any table = fail. |
| C-04 | Gate vector table complete | format | GATE VECTOR TABLE has all four gates present: GOpen, G_domain (or G_domain Aggregate), G_lifecycle, GClose. Each gate has a named reviewer, a verdict (PASS / CONDITIONAL / FAIL), and a contract cite. No gate row is missing or blank. |
| C-05 | Disposition algebra applied mechanically | correctness | DISPOSITION section states each of {GOpen, G_domain_agg, G_lifecycle, GClose}, then evaluates the §3 formula explicitly (not editorially), and derives READY / CONDITIONAL / BLOCKED. The stated Overall Disposition is consistent with the formula output. |

### Recommended (output is better with these — 30 pts total, 10 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Scope enumeration artifact-specific | depth | §1 IN-SCOPE surfaces are concrete and artifact-specific — not generic ("all sections") or placeholder text. At least two distinct, named surfaces are listed. |
| C-07 | Action item register CH-ID sourced | correctness | Every PARTIAL or HOLDS CH-ID from BRACKET CLOSING Final Assessment has a corresponding row in the ACTION ITEM REGISTER with Disposition Class and Resolution Criterion filled. A HOLDS/PARTIAL CH-ID with no register row = fail. |
| C-08 | Cross-role signals are specific | depth | CROSS-ROLE SIGNALS section: CONVERGENCE names at least one CH-ID or finding echoed by two or more reviewers (not "None detected" if any convergence exists). CONFLICTS identifies any incompatible responses or writes "None detected" with justification. Neither field contains a placeholder. |

### Aspirational (raise the bar — 10 pts total, 5 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Null hypothesis is specific and challenger-grounded | depth | The null hypothesis names the concrete alternative the team uses today (tool, process, or workaround) rather than a generic phrase like "do nothing" or "status quo". Null hypothesis strength (HIGH / MEDIUM / LOW) is justified in one sentence. |
| C-10 | Domain findings are role-grounded and in-scope | depth | Each Additional Finding in the DOMAIN section names an in-scope surface from §1 and is attributable to the role's lens or expertise (not a generic observation any reviewer could make). At least two of three findings meet this bar. |

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Ready to use as golden prompt |
| Passing | all essential + 60-79 | Structurally sound, depth gaps |
| Borderline | 4 essential + any score | One essential gap — not usable without fix |
| Failing | <= 3 essential | Contract or CH-ID trace broken — output not useful |

---

## Vacuous Conditions

- C-07: If BRACKET CLOSING shows all CH-IDs DEFEATED, the register may contain only ADVISORY-OBS
  rows. Pass if register is present and DEFEATED status is consistent with the rows (or lack thereof).
- C-08: If the artifact generates only one CH-ID, CONVERGENCE field may legitimately be
  "None detected" — do not penalize if single-claim review has no multi-role echo.
- C-10: If `--depth deep` adds DOMAIN-2 or DOMAIN-3 sections, evaluate C-10 against the
  primary DOMAIN section only.

---

## Notes for Scorers

- C-03 is the most commonly failed criterion in early runs. Look for CH-ID rows silently dropped
  between BRACKET OPENING and downstream tables.
- C-05 fails when the model writes "Given the findings above, the disposition is CONDITIONAL"
  without evaluating the gate vector formula. The formula must appear explicitly.
- C-09 is aspirational because it requires the model to interpret the artifact's domain and
  generate a plausible inertia alternative — this is genuine judgment, not template-filling.
