Written to `simulations/quest/rubrics/topic-report-rubric-v10-variations-R10-2026-03-15.md`.

---

## Round 10 Variations -- `topic-report`

**Base**: R9 V-04 triple (25/25 under v10). All 5 variations score 100.0 under v10; discrimination only activates under v11 when C-34, C-35, C-36 are added.

### Variation axes

| Axis | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|-------------|------|------|------|------|------|
| A: C-34 main-branch recovery directive | Branch A THREE-LAYER header renamed BRANCH A; recovery names action + prohibited alternative + register labels | YES | NO | YES | YES | NO |
| B: C-35 branch-qualified slot indexing | CONTRACT REGISTER carries `[SLOT n / BRANCH A]` and dual-branch mapping for G-7/G-9 | NO | YES | YES | YES | NO |
| C: C-36 explicit temporal coordination | Branch A header adds Coordination line naming planning-phase (C-35 map) then recovery-phase (C-34 directive) temporal sequence | NO | NO | NO | YES | NO |

### Key design decisions

**C-34** is the Branch A analogue of C-29 (which gave Branch B its named recovery directive). It adds three things to the Branch A header: (1) names it `(BRANCH A)`, (2) names the prohibited alternative (`do not cross-reference Branch B`), (3) cross-references the CONTRACT REGISTER by label for recovery without a spec search.

**C-35** extends C-30 (slot-indexed register) to be branch-aware. `G-7a COMPLETENESS [SLOT 3]` becomes `G-7a COMPLETENESS [SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]`. This closes the forward-map ambiguity that C-30 leaves open: unqualified `[SLOT 3]` is implicitly Branch A but not named as such, so a model on the Branch B path cannot map it without guessing.

**C-36** (V-04 only) adds a `Coordination:` line to the Branch A header that names the temporal property: C-35 established the branch-qualified slot map at execution start (planning phase); C-34 fires the recovery directive at the write point against that map (recovery phase). The V-03/V-04 scoring split will determine whether C-36 requires explicit naming or is scored structurally from C-34 + C-35 co-presence.

**Asymmetry note**: C-35 requires C-30 as precondition (can't branch-qualify what isn't slot-indexed). This means R9 V-01 (which lacks C-30) cannot satisfy C-35 even if retested -- the R10 variations break R9's pairwise tie by making C-35 a dependency-asymmetric criterion over the R9 base axes.

### Predicted ordering under v11 (formula `asp/28 * 10`)

V-04 (100.0) >= V-03 (99.6) > V-01 = V-02 (99.3) > V-05 (98.2)
