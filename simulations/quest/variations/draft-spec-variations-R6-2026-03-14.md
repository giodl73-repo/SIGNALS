Written to `simulations/quest/rubrics/draft-spec-rubric-v6-variate-R6-2026-03-15.md`.

---

## Round 6 — Axis Map

| V | Primary Axis | Hypothesis |
|---|-------------|------------|
| **V-01** | **C-22: Proper IG-ID register** — split into `[IG-REGISTER]` (guards, IG-XX) and `[ID-REGISTER]` (defeats, ID-XX) as parallel tables with distinct IDs | Structural separation of guards from defeats satisfies C-22's "parallel namespace, verifiable by counting pairs" definition; AMPLIFIED threshold and [INERTIA-ANALYZED] gate survive unchanged |
| **V-02** | **C-18: Scripted verbatim fallback copy** — two `VERBATIM RESPONSE:` blockquote variants (all-missing branch A / requirements-missing branch B) | Demarcating the fallback with `VERBATIM RESPONSE:` and adding the partial-context variant satisfies C-18 without touching any phase structure; C-09 passes by inclusion |
| **V-03** | **C-24: Cascade directive on every unified declaration** — `CASCADE TO: [location A of N] → [location B of N]` annotation on each unified element | Each declaration specifies its own propagation; ordinal denominators make C-19 load-bearing rather than incidental; C-15 upgrades from design aspiration to structurally declared contract |
| **V-04** | **C-22 + C-23: Proper IG-ID register + IG-role binding** — adds `Responsible Role` column to `[IG-REGISTER]` and `Confirming Role` to `[ID-REGISTER]`, cross-matched | Risk namespace achieves structural parity with requirements namespace at both tracking and accountability dimensions; role binding is inline on the IG entry, not deferred to a behavioral phase |
| **V-05** | **All three new axes + C-18** — V-01 (IG/ID split) + V-04 (role binding) + V-03 (cascade directives) + V-02 (verbatim fallback) | Expected 170/170; the only remaining PARTIAL from R5 (C-18) closes; every criterion is structurally instantiated rather than behaviorally implied |

---

## What R6 Targets

**New criteria in v6 rubric:**
- **C-22** (properly defined): IG register with distinct IG-XX guard entries + ID-XX defeat entries as parallel namespaces. V-05 R5 conflated these into a single row per inertia hypothesis. V-01 and V-04/V-05 split them.
- **C-23** (new): Each IG-XX carries a `Responsible Role` column inline on the guard entry itself — not in a separate phase. V-04 and V-05 implement this.
- **C-24** (new): Each unified role-and-source declaration carries a `CASCADE TO:` annotation naming all structural locations it instantiates, with ordinal denominators. V-03 and V-05 implement this.

**Carried from R5:**
- **C-18** (still PARTIAL baseline): V-02 and V-05 attack this directly with `VERBATIM RESPONSE:` blockquotes and a second partial-context variant.

V-05 is the first variation where all four remaining gap sources (C-22 definition, C-23, C-24, C-18) are addressed simultaneously in a single body.
