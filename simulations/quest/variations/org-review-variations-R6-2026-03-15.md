---

# org-review R6 — 5 Variations

Written to `simulations/quest/golden/org-review-variate-R6-2026-03-16.md`.

---

## Strategy Summary

R6 targets the two new v6 criteria exclusively. Three single-axis, two combinations.

| # | Axis | Primary Criteria Targeted | Novelty vs Prior Rounds |
|---|------|--------------------------|-------------------------|
| **V-01** | Lifecycle emphasis | C-22 | Step 1 scope declaration with explicit gate rule: "role selection (Step 2) may not begin until this step is complete." First mechanism to structurally satisfy C-22 — R5 PARTIAL because scope was declared inside the body without a gate condition. |
| **V-02** | Output format | C-23, C-20, C-17 | CH-IDs assigned to every challenge claim. Mandatory CH-ID response table in every downstream section. Closes with ACTION ITEM REGISTER: one row per open CH-ID, disposition class + owner role + resolution criterion. |
| **V-03** | Phrasing register | C-19 + C-22 | `DISPOSITION_CONTRACT v1` immutable preamble block containing §1 scope enumeration, §2 severity semantics, §3 disposition algebra, §4 contract cite requirement. Scope and severity are contract-bound before reviewers run — deviations are auditable at section level, not just synthesis. |
| **V-04** | Scope gate + bracket + CH-ID | C-22, C-15, C-18, C-20, C-17, partial C-23 | Combines Step 1 gate (V-01 mechanism) + adversarial bracket with stated override authority (GClose = FAIL overrides all) + CH-ID response tables per reviewer + action register. Pre-stated disposition formula before Gate 1. Projected ~103–108/115. |
| **V-05** | Full combination | All 23 criteria | Pre-printed fill-the-brackets template + DISPOSITION_CONTRACT (§1 scope, §2 severity, §3 algebra, §4 cite, §5 CH-ID tracing) + bracket architecture + full CH-ID action register with resolution-criterion column. Maximum structural coverage. Projected ~109–114/115. |

---

## Key Mechanisms Introduced in R6

**Scope pre-reviewer gate** (V-01, V-03, V-04, V-05):
The gate rule lives on the `STEP 1` heading itself — `[GATE — role selection may not begin until this step is complete]`. Role selection is Step 2. This makes the temporal ordering explicit and audit-visible, not just instructional.

**CH-ID action register** (V-02, V-04, V-05):
Challenge claims get `CH-001`, `CH-002`, etc. at the challenger gate. Every downstream reviewer has a pre-printed response table keyed to those IDs. Post-synthesis register has one row per open CH-ID with `Disposition Class | Owner Role | Resolution Criterion` — the full traceability chain from challenge claim through to action disposition.

**DISPOSITION_CONTRACT as scope anchor** (V-03, V-05):
Prior variations placed severity semantics in free-form preamble prose. V-03/V-05 put scope, severity, and algebra inside a named `DISPOSITION_CONTRACT v1` immutable block. The contract cite (`Contract: DISPOSITION_CONTRACT v1`) on every reviewer section makes omission structurally visible — it's a missing field, not a paraphrase failure.

**GClose override authority — explicit statement** (V-04, V-05):
`GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict from the challenger is not overturned by G_domain or G_lifecycle PASses. This override authority is explicit and structural — it is not subject to editorial revision at the Disposition step.` The override is stated twice: once in the bracket closing section, once in the disposition section's formula block.
