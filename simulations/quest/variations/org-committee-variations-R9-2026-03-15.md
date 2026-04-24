Written to `simulations/quest/golden/org-committee-variate-R9-2026-03-16.md`.

---

## Round 9 Variations — Summary

All five variations target the three new R9 criteria (C-27, C-28, C-29) in addition to the full R8 baseline (129/130).

| Variation | Primary Axis | C-28 | C-27 | C-29 | Key Mechanism |
|-----------|-------------|------|------|------|---------------|
| **V-01** | Output format — skeleton-first | Pre-declared skeleton with every slot labeled upfront; Phase 2 present on page before any gate runs | INERTIA-FINDING-A/B/C/D labels in skeleton | Phase 2 slot is in the skeleton unconditionally; loop only delays filling it | Skeleton = enforcement; omission is a visible gap |
| **V-02** | Inertia framing — named labels | Inline (as generated) | `INERTIA-FINDING-*` as primary identifier everywhere; letter `(a)/(b)` retired | Explicit `LOOP UNTIL: GATE-N YES → Phase 2 fills unconditionally` prose | Label identity maintained end-to-end through CITE:/RESPONDS-TO: |
| **V-03** | Phrasing register — imperative | Inline | `INERTIA-FINDING-*` labels in FILL commands | `LOOP UNTIL:` / `IF ... → EXIT LOOP → CONTINUE TO PHASE 2` constructs | Machine-instruction register removes interpretive latitude on loops |
| **V-04** | Lifecycle + C-29 — loop diagrams | Inline | `INERTIA-FINDING-*` in Phase 1 | ASCII loop diagrams showing Phase 2 as unconditional exit target at bottom of Phase 1 box | Visual loop makes intra-phase scope unambiguous |
| **V-05** | Full synthesis | Full pre-declared skeleton (targets 132/132) | `INERTIA-FINDING-*` in skeleton slots + fill rules | Loop described within each phase's fill rules; Phase 2 slot pre-printed unconditionally | All criteria as skeleton slots; loop/gate inside each slot's instructions |

**The C-29 fix across all variations**: The critical lesson from R8 V-02 is that phrasing the gate as "do not proceed to Phase 2 until..." removes Phase 2 from the prompt, making it structurally absent. Every V-01 through V-05 here phrases the gate as a retry loop that exits to Phase 2 — Phase 2 is always present, the loop only controls *when* Phase 1 releases.
