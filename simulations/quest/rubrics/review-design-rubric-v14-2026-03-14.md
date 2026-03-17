Written to `simulations/quest/rubrics/review-design-rubric-v14-2026-03-15.md`.

---

**Two new criteria extracted from R14:**

**C-43 | BLOCK 2.7 P1 Section Registry for Upstream Amendment Target Lock**
- Pattern class: behavior (proactive anchoring — parallel to C-15 BLOCK 1.5, C-21 BLOCK 0)
- V-02/V-04/V-05 introduced a dedicated intermediate block positioned after BLOCK 2 and before BLOCK 3 that commits the complete set of valid BLOCK 5 amendment targets; F-28 resolves against this locked registry rather than performing a live P1 row scan at BLOCK 5 generation time
- Pass condition: dedicated named block (BLOCK 2.7 or equivalent) present after BLOCK 2 before BLOCK 3, enumerating all BLOCK 2 P1 Section values; F-28 references it as its anchor; inline pre-check inside BLOCK 5 fails (wrong lifecycle position)

**C-44 | Cross-Block Mismatch Halts Specify Both Upstream and Downstream Resolution Paths**
- Pattern class: behavior / repair completeness (extends C-37 for the class of cross-block reference mismatch halts)
- V-01 F-28: `"Correct the Section value to match a BLOCK 2 P1 Section, or add the P1 finding to BLOCK 2 before continuing."` — names both directions because the mismatch is directionally ambiguous: either the BLOCK 5 row targets the wrong section (fix downstream) or a P1 was missed in that section (add upstream)
- Pass condition: every cross-block reference mismatch halt (F-28 and equivalents) specifies both the downstream correction path and the upstream addition path; single-direction corrective action passes C-37, fails C-44; structural absence halts (F-01, F-04) and count-parity halts (F-09, F-12) are exempt (unambiguous repair direction)

**Formula:** denominator 35 → 37. Each aspirational criterion ~0.270 pts. Ceiling 100 preserved.

**C-37 update:** R14 signal note added — the anaphoric resolution boundary is now precisely documented: `"Populate it before continuing. Halt."` passes (unambiguous referent in trigger clause); `"Populate. Halt."` fails (bare verb, no referent named or recoverable). The pass/fail boundary is referential completeness, not lexical length.

**C-42 update:** Pass condition note added — F-28 may resolve against a dedicated BLOCK 2.7 registry (C-43) rather than a live BLOCK 2 lookup; both placement strategies satisfy C-42. R14 three-strategy experiment (inline/registry/pre-check) documented.
