Everything checks out. Here is the complete updated rubric (key new content):

---

# program-plan Rubric — v12

**33 aspirational criteria, 4 essential, 3 recommended. Total max: 255 pts.**

Three criteria added from R11 excellence signals:

---

### C-38 — BAD PLAN Header Affirmative Full-Criterion Coverage Claim

- **Weight**: aspirational
- **Category**: depth
- **Text**: The BAD PLAN block's header does not merely avoid false restriction (C-36) but affirmatively states full criterion spectrum coverage — "all 7 criteria," "C-01 through C-07," "essential and recommended violations," or equivalent positive claim. A neutral header ("BAD PLAN") passes C-36 but leaves coverage scope ambiguous: a model reading it cannot determine how many criteria to scan for. An affirmative claim primes the model to look for all 7 tags. C-36 closes the false-restriction failure (essential-only label over full-coverage block); C-38 closes the neutral-silence failure (header neither restricts nor affirms). Evidence from R11: V-04/V-05 have accurate headers (C-36 passes) but no variate yet uses affirmative language — the distinction between "not falsely restricted" and "positively claimed" is the gap C-38 targets.
- **Pass condition**: BAD PLAN header includes an affirmative claim of full-criterion coverage naming all 7 criteria collectively or individually. Prerequisites: C-36, C-31.
- **Partial credit**: Not applicable.

---

### C-39 — BAD PLAN Skills-Field Criterion-Tag Co-Location

- **Weight**: aspirational
- **Category**: depth
- **Text**: Every `skills:` entry in the BAD PLAN block that violates C-03 (invented skill name, unrecognized namespace) carries `# WRONG C-03` inline at the skills-field line itself — not at adjacent gate or name fields. C-26 establishes co-location at `gate_fail:` fields for C-04; C-37 establishes it at `name:` fields for C-06; C-39 extends the same discipline to `skills:` entries for C-03, completing field-level co-location across all three primary YAML field types. Without C-39, a BAD PLAN may satisfy C-31 while leaving invented skill names physically unannotated at the field — a model filling the skills slot encounters the wrong shape without a criterion tag naming why. Evidence from R11: V-04/V-05 carry C-26 (gate field) and C-37 (name field) co-location; skills-field co-location has not been assessed — the structural logic of C-26 and C-37 applies directly and C-39 makes it explicit.
- **Pass condition**: Every C-03-violating skills entry in the BAD PLAN carries `# WRONG C-03` inline on that line. Prerequisites: C-22, C-31.
- **Partial credit**: Field-level C-03 annotation on at least half the violating skills entries but not all.

---

### C-40 — Compound gate_fail: Annotation and Correction-Table Recommended Coverage Conjunction

- **Weight**: aspirational
- **Category**: depth
- **Text**: Both the YAML-template teaching zone (C-34 compound `gate_fail:` annotation with criterion tag + `Why:`) and the correction-table lookup format (C-29 recommended-tier wrong-to-correct pairs) are simultaneously present, ensuring recommended-tier error teaching is delivered at both teaching moments: template-filling time (model resolves gate fields) and pre-generation consultation time (model scans correction table before authoring). C-35 pairs BAD PLAN example block (C-31) with correction table (C-29); C-40 pairs YAML template compound annotation (C-34) with correction table (C-29) — closing the gap between the third teaching format and the lookup format. The two conjunction criteria are orthogonal. Evidence from R11: V-04 and V-05 achieve both C-34 and C-29 simultaneously — the first rounds to confirm these mechanisms are additive and non-conflicting, establishing the conjunction as a named target.
- **Pass condition**: C-34 and C-29 must both pass independently. Prerequisites: C-34, C-29.
- **Partial credit**: Not applicable.

---

**Scoring delta**: 30 → 33 aspirational criteria · 150 → 165 aspirational pts · **240 → 255 total pts**. Formula: `aspirational_pass/33 * 165`. Golden threshold (>= 80) unchanged.

**Version history**: v10 added C-34/C-35 from R9; v11 added C-36/C-37 from R10; v12 adds C-38/C-39/C-40 from R11.

**Pattern map**:

| Criterion | Source pattern | Gap closed |
|-----------|----------------|------------|
| **C-38** | C-36 is a free win — affirmative claim costs nothing more | Neutral-silence: header neither restricts nor affirms full coverage |
| **C-39** | Co-location rule generalizes to third field type | skills: entries unannotated at field position (C-26 = gate field, C-37 = name field, C-39 = skills field) |
| **C-40** | C-34 and C-29 are structurally orthogonal — their conjunction is a named target | YAML-template teaching zone + correction-table lookup zone not jointly required for recommended-tier coverage |

File written to `simulations/quest/rubrics/program-plan-rubric-v12-2026-03-16.md`.
