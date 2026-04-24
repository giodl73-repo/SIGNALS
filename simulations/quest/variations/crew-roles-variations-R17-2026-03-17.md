Written to `simulations/quest/golden/crew-roles-variate-R17-2026-03-17.md`.

---

# crew-roles -- Variate R17

**Baseline**: R16 V-04 (VERBOSE + INERTIA-AS-BENCHMARK), which satisfies all 28 v11 criteria including C-36. Formula: `aspirational_pass / 28 * 10`.

**Gaps probed**: C-36 is now structural. R17 stress-tests whether the current INERTIA BASELINE + INERTIA ANCHOR CHECK implementation has drift risks:

| Risk | Description |
|------|-------------|
| Risk-1 | Accidental verbatim -- prose strength terms are heuristically matchable; generic phrases pass INERTIA ANCHOR CHECK without real anchoring |
| Risk-2 | Late detection -- INERTIA ANCHOR CHECK fires only in Phase 7; errors in Phase 6.1 require cascade revision of all subsequent roles |
| Risk-3 | Single-file anchoring -- only the inertia-advocate references the baseline; the baseline has not actually shaped the registry |

**Axes**:

| Axis | Mechanism |
|------|-----------|
| D -- Labeled strength terms | Phase 2 INERTIA BASELINE numbers strengths `S1/S2/S3` and gaps `G1/G2/G3`; INERTIA ANCHOR CHECK requires `S1: {phrase}` verbatim (label + exact phrase, neither alone passes) |
| E -- Early INERTIA ANCHOR CHECK | Fires in Phase 6 Step 6.1 immediately after inertia-advocate is written; blocks STEP 6.2 if FAIL; Phase 7 INERTIA ANCHOR CHECK becomes a confirmation pass |
| F -- Cross-role baseline spread | Phase 6 LENS AUDIT gains item 6 checking each remaining role's `lens.verify` for any INERTIA BASELINE term; Phase 7 adds CROSS-ROLE SPREAD CHECK requiring at least one non-inertia-advocate role to reference the baseline |

**Variations**:

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| V-01 | D only | S-labels make anchoring structural, not heuristic |
| V-02 | E only | Early detection eliminates cascade revision from Phase 6.1 failures |
| V-03 | F only | Cross-role spread validates baseline has influenced the full registry |
| V-04 | D + E | Labels make anchoring precise; early check catches it before it propagates wrongly |
| V-05 | D + E + F | Full hardening: non-accidental anchors + early detection + distributed baseline influence |

**Predicted scorer**: V-04 and V-05 should both reach 28/28 = 10.0. V-01 through V-03 should also reach 28/28 since all preserve C-36. The differentiator will be whether the new axes expose a gap that becomes C-37 -- watch for whether V-03's CROSS-ROLE SPREAD CHECK (Axis-F) and V-01's S-label specificity requirement surface structural weaknesses not yet in the rubric.
