Written to `simulations/quest/rubrics/trace-permissions-rubric-v4-2026-03-16.md`.

---

**Two new criteria extracted from Round 3:**

**C-16 — Entity closure parity across gap states** (from V-01 C-13 PARTIAL)

V-01's `ENTITY CLEAR` format only fired on gap-free entities. Entities where gaps were found advanced without an equivalent closure block — the closure ritual was absent precisely where it carried the most information. C-13 requires closure to exist somewhere; C-16 tightens to: the closure must appear on a gap-containing entity. Pass condition: at least one entity section where gaps were found includes a named closure assertion before advancing.

**C-17 — Multi-vector escalation enumeration** (from V-03 Phase 2d)

V-03's four-vector escalation table (sharing rules, team membership, field inheritance, role hierarchy) gave each vector an explicit `POSSIBLE / NOT POSSIBLE + evidence` verdict per Write-capable role. C-05 requires tracing one found path; C-17 adds: enumerate the complete set of vectors checked, including those found absent. Without NOT POSSIBLE verdicts, the analysis is indistinguishable from one that simply stopped early. Pass condition: at least three distinct escalation mechanism types named, each with a verdict, for at least one Write-capable role.

---

**Tier update:** Aspirational grows from N=8 to N=10. Per-criterion weight drops from 1.25 to 1.0 points, preserving the 10-point total.
