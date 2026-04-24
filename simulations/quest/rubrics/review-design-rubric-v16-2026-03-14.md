Written to `simulations/quest/rubrics/review-design-rubric-v16-2026-03-15.md`.

---

**Summary of changes from v15 to v16:**

**New criteria (C-47, C-48, C-49):**

- **C-47 | Elevation Record Consensus Status Named Halt** — A named halt (F-31) fires when any BLOCK 3 Elevation Record row's Consensus Status value is not ELEVATED or BASELINE. Applies C-37's closed-enumeration value-naming requirement as an inline enforcement gate on the typed classification column C-45 introduced. Source: V-02, V-04, V-05 all carry F-31 in R16.

- **C-48 | SEALED Gate F-Code Enumeration** — Each SEALED statement (C-46) enumerates the specific F-codes verified within the block by name, making the attestation an auditable inspection record. C-46's floor is summary prose; C-48 requires per-F-code enumeration. V-04 form: "F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed. BLOCK 4 proceeds." V-05 enriched form (with inline invariant descriptions) also satisfies this. V-01 summary SEALED confirms C-48 is orthogonal to C-46.

- **C-49 | CONSENSUS ELEVATION RULE Three-Level Explicit Ordering with Non-Conformance Prohibition** — The BLOCK 5 rule explicitly enumerates all ordered tiers with sort keys (ELEVATED 1..n sorted by Amendment Cost then reviewer count; BASELINE n+1..P1_count same keys; no ties) and includes an explicit non-conformance prohibition: "Re-assessing consensus status at BLOCK 5 generation time is non-conformant." C-45 requires the rule exists; C-49 requires full algorithmic enumeration. Source: V-05 R16 only.

**R16 signals added to existing criteria:**

- **C-37** — Closed-enumeration boundary confirmed across three enumerations: AGREE/SPLIT (F-14), P1/P2/P3 (F-02), ELEVATED/BASELINE (F-31). V-03 FAIL confirmed.
- **C-45** — R16 signal noting C-47 and C-49 as next aspirational steps above C-45.
- **C-46** — R16 signal documenting three observed SEALED quality levels (summary / F-code enumeration / F-code + invariant description).

**Formula:** denominator 39 → 42. Each aspirational criterion ~0.238 pts. Ceiling 100 preserved.
