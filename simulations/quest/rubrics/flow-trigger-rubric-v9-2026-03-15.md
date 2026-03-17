**flow-trigger-rubric-v9** written to `simulations/quest/rubrics/flow-trigger-rubric-v9-2026-03-16.md`.

---

**Two new aspirational criteria (C-30–C-31), N_aspirational: 21 → 23, max (raw): 117.5 → 122.5:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-30 | V-04 advance — PROHIBITION 03a ("MAY NOT add candidates *after* denominator declaration") | Named prohibitions carry a lifecycle activation anchor (a named Phase 0 event after which the prohibition takes effect), making the prohibition's effective period self-verifiable from the Phase 0 registry. A globally-stated prohibition is ambiguous about when it activates; a temporally-anchored one creates a lifecycle-bound invariant. | C-21 (the prohibition contracts it makes lifecycle-aware), C-25 (the Phase 0 gate whose events serve as activation anchors) |
| C-31 | V-04 advance — "Role 1 (Auditor) explicitly produces a 7-layer EXCLUSION LOG" | Each artifact in the manifest names its producing role and production phase, making a missing artifact a named role deliverable failure rather than an anonymous structural gap. The CLOSURE CHECK gains attribution: "ART-02 — Role 1 (Auditor): ABSENT" vs. "ART-02: not found." | C-23 (the artifact lock it makes role-accountable), C-21 (the affirmative-obligation inverse: C-21 names what roles may not do; C-31 names what roles must produce) |

**Structural relationship:** C-30 couples prohibition contracts to the Phase 0 temporal structure — prohibitions activate at named lifecycle events, so their effective period is self-evident without reading role descriptions. C-31 couples artifact existence to role accountability — each manifest artifact has an owner, so production gaps are attributable rather than anonymous. Together with C-27–C-29 they complete the Phase 0 self-enforcement model: exit is computable (C-27), violation is detectable (C-28), rationale is non-separable (C-29), prohibitions are temporally-bound (C-30), and artifact production is role-traced (C-31).
