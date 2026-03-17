Written to `simulations/quest/golden/trace-skill-variate-R14-2026-03-15.md`.

---

## R14 Variations — Design Summary

**Entry state**: All R13 variations passed C-42. C-43 and C-44 are the new discriminating signals. All 5 R14 variations carry both as baseline.

---

### V-01 — Single axis: C-43 structural isolation
**`**SCORER HEURISTIC (C-43):**` as bold-labeled sub-element**

The conformance-collapse claim body states the mechanism; the `**SCORER HEURISTIC (C-43):**` label follows as a structurally isolated element, paralleling the `**Independence Statement**:` pattern from DefectCodeVocab (C-36). A scorer confirms C-43 by label scan without reading the claim body.

C-44: numbered inline list with `Required (RequiredVocabulary)` as item 1.

---

### V-02 — Single axis: C-44 scope format
**ANNOTATION SCOPE REGISTRY table with TCR as row 1**

The COUNT GATE replaces prose scope description with a formal 7-row table. Row 1 is `Template Component Registry | Required (RequiredVocabulary) | 1`. C-44 compliance is checkable by table row lookup alone.

C-43: standard inline final-sentence in the conformance-collapse claim.

---

### V-03 — Single axis: phrasing register
**Imperative throughout — "MUST", "NEVER", "ALWAYS"**

All structural requirements as commands. The conformance-collapse claim uses a `**You MUST close this rule with the following scorer confirmation line**:` directive to make C-43 feel like a hard rule rather than a structural description. COUNT GATE scope as PRESENT/ABSENT checklist.

---

### V-04 — Combined: V-01 + V-02
**SCORER HEURISTIC label + ANNOTATION SCOPE REGISTRY table**

Both structural isolation mechanisms together. Scorer can confirm C-43 by label scan AND C-44 by table row lookup independently.

---

### V-05 — Combined: V-01 + V-02 + V-03 + SCHEMA ROLE
**Maximum structural isolation via pre-trace SCHEMA ROLE**

The TCR (and its `Required (RequiredVocabulary)` column) is a **SCHEMA ROLE output artifact**, not just a prompt comment — making C-44's target independently verifiable before the COUNT GATE runs. All three axes apply throughout. The `**SCORER HEURISTIC (C-43):**` label appears inside the SCHEMA ROLE output section, making it part of the trace record.
