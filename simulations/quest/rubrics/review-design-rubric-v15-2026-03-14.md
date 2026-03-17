Written to `simulations/quest/rubrics/review-design-rubric-v15-2026-03-15.md`.

---

**Changes from v14 to v15:**

**New criteria (C-45, C-46):**

- **C-45 | BLOCK 3 Elevation Record as Typed Intermediate Artifact** — BLOCK 3 produces a typed classification (ELEVATED/BASELINE) per P1 finding; BLOCK 5 consumes it via a named CONSENSUS ELEVATION RULE for deterministic priority ordering. Eliminates re-computation drift by anchoring the priority artifact at consensus time, not amend time. Source: V-05 R15 excellence signal.

- **C-46 | BLOCK N SEALED Lifecycle Gate Statements** — Every lifecycle block closes with an explicit SEALED attestation naming (a) what was verified and (b) what proceeds next. Structurally parallel to C-14 (halt coverage on failure path) but inverted: SEALED gates attest the success path. Together they close the lifecycle contract in both directions. Source: V-04 R15 excellence signal.

**Updates to existing criteria:**

- **C-37** — R15 signal added: naming a field without naming the required value class fails when that class is a closed enumeration (e.g., "Replace the Type value" without naming AGREE or SPLIT). The referent-completeness boundary extends to value specifications, not just field references.
- **C-43** — Pass condition note added: inline pre-check inside BLOCK 5 is non-conformant; POSITION CONSTRAINT negative naming (explicitly stating this) closes the enforcement gap. R15 signal documenting V-02/V-04/V-05 all using this pattern.
- **C-44** — Pass condition updated to enumerate all 6 mismatch halts (F-03, F-10, F-15, F-16, F-17, F-28). R15 signal added documenting V-05 as the first full-class PASS with labeled `Downstream fix:` / `Upstream fix:` applied uniformly.

**Formula:** denominator 37 → 39. Each aspirational criterion ~0.256 pts. Ceiling 100 preserved.
