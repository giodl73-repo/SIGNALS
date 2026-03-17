**flow-trigger-rubric-v7** written to `simulations/quest/rubrics/flow-trigger-rubric-v7-2026-03-16.md`.

---

**Two new aspirational criteria (C-25–C-26), N_aspirational: 16 → 18, max (raw): 105 → 110:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-25 | Excellence Signal 1 + JSON pattern 1 — V-05 Phase 0 gate | Named pre-enumeration lifecycle phase with typed entry/exit conditions; the exit signal is the structural proof that all pre-enumeration obligations (scope gate, manifest lock, EOR table, cascade budget, breach token protocol) are satisfied before enumeration begins — making C-14 a lifecycle obligation rather than a best-practice | C-14 (scope gate it makes structurally mandatory), C-23 (manifest locking it enforces via exit signal) |
| C-26 | Excellence Signal 3 — V-05 INERTIA CONTRAST | Named contrast section that documents, for at least two structural mechanisms, both (a) the weaker inertia-driven alternative and (b) the specific failure mode that alternative produces — making each mechanism's rationale traceable within the artifact independent of the external rubric, resisting criterion-drift across rounds | C-23, C-24 (the contrast makes their rationale co-located with their mechanisms) |

**Structural relationship:** C-25 is the lifecycle enforcement complement to C-23 — where C-23 requires artifacts to be locked before enumeration, C-25 provides the mechanism that proves they were: the Phase 0 exit signal. An output with role-gating or format pre-population alone (V-01, V-02) satisfies C-23 because artifacts are declared before enumeration; only C-25 requires the declarative proof that all pre-enumeration obligations were simultaneously satisfied as a named lifecycle event. C-26 is the epistemic complement to both — it embeds the *why* alongside the *what*, so structural choices survive the rubric version that motivated them. Together C-25 and C-26 represent what separated V-05 from V-03 (which had Phase 0 but no INERTIA CONTRAST) and from V-04 (which had phrasing register but neither Phase 0 gate nor embedded rationale): the combination of lifecycle enforcement and co-located motivation makes the structure self-explaining and self-enforcing.
