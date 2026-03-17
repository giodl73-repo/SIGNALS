Written to `simulations/quest/golden/quest-rubric-variate-v6-R06-2026-03-16.md`.

---

## Round 6 — Variation Summary

**Axes chosen for single-axis:** lifecycle-emphasis, role-sequence, phrasing-register

| Variation | Axis | What Changed | Criteria Targeted |
|-----------|------|--------------|-------------------|
| **V-01** | lifecycle-emphasis | Author Entry Gate names SA-1 and SA-2 by identifier with AUTHOR ACCESS: GRANTED/DENIED block | C-20 |
| **V-02** | role-sequence | Citation rule: CM-NN must survive from INERTIA-RECORD into canonical CRITERION row Pass Condition; Structural Verification checks citation presence | C-19 |
| **V-03** | phrasing-register | Hard-stop PHASE STATUS declarations (OPEN/CLOSED/BLOCKED) replace checklist-advisory format at all phase boundaries | C-20 (register test) |
| **V-04** | lifecycle × role-sequence | V-01 × V-02: named-artifact inventory gate + citation retention in canonical row + explicit Final Rubric "retain CM-NN verbatim" rule | C-19, C-20 |
| **V-05** | lifecycle × role-sequence × phrasing-register + inertia-framing | Full stack: V-04 + PHASE STATUS declarations + named Status-Quo Rubric competitor front-loaded in opening framing | C-07, C-19, C-20 |

**Key design choices:**

1. **V-01 vs. R5 V-05 gate:** R5 V-05 said "DO NOT begin until Spec Analyst Completion Gate cleared" — names the gate, not the artifacts. V-01's ARTIFACT INVENTORY block lists SA-1 and SA-2 by identifier with inline status. The C-20 distinguishing test is whether the blocking language names the specific artifacts, not just the phase.

2. **V-02 citation rule:** The gap C-19 targets is canonicalization stripping — identifiers present in INERTIA-RECORD but absent from CRITERION table rows. V-02 adds an explicit citation rule in the CRITERION recording step, a citation check in Structural Verification, and a "retain CM-NN verbatim" note in FINAL RUBRIC. Three checkpoints to prevent stripping.

3. **V-03 register:** Uses `CRITERION GATE: [OPEN/BLOCKED]` inline in the INERTIA-RECORD block itself — the model must commit to a gate status before recording each criterion. This is a per-criterion analog of V-01's phase-level gate.

4. **V-05 "Status-Quo Rubric" framing:** Replaces "Inertia Test" language with "Status-Quo Test" throughout — reframes the same mechanism as a competitive comparison rather than a quality check. Tests whether competitive framing front-loads specificity pressure.

**Anchor:** V-04. Mechanisms operate at non-competing lifecycle positions (phase entry vs. row content). If V-04 fails one criterion that its single-axis variation passed, the interaction is detectable and documented in the roadmap.
