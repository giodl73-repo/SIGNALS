Written to `simulations/quest/golden/crew-roles-variate-R18-2026-03-17.md`.

---

## crew-roles -- Variate R18

**Baseline**: R17 V-04 (Axis-D + Axis-E, all 30 criteria).

**Gaps probed**: C-37 and C-38 are now structural. R18 stress-tests the labeled-anchor mechanism under three new risks:

| Risk | Description | Axis |
|------|-------------|------|
| Risk-3 | Phase 4 FRAME FILL for inertia-advocate omits S-labels; EARLY ANCHOR CHECK forces Phase 4 revision mid-execution | **Axis-G** |
| Risk-4 | Phase 2 EXIT GATE has no operational definition of "non-generic"; S1: "easy to use" can pass the gate | **Axis-H** |
| Risk-5 | C-37/C-38 verify only the inertia-advocate's lens.verify; the baseline may not influence any other role | **Axis-F** (carried from R17) |

**Variations**:

- **V-01 (Axis-G — FRAME FILL PRE-ANCHOR)**: Fires a `FRAME FILL PRE-ANCHOR CHECK` immediately after the inertia-advocate's FRAME FILL block in Phase 4, before continuing to remaining roles. Makes Phase 6.1 a confirmation rather than error-detection.

- **V-02 (Axis-H — NON-GENERIC DEFINITION)**: Adds an operational definition at Phase 2 EXIT GATE: a phrase is non-generic if it contains a domain-specific noun/verb that cannot appear unchanged in a different domain's baseline. Includes a negative-example list.

- **V-03 (Axis-F — CROSS-ROLE BASELINE SPREAD)**: Adds a 6th LENS AUDIT item in STEP 6.2 (does this role reference an INERTIA BASELINE S or G term?) and a `CROSS-ROLE SPREAD CHECK` in Phase 7 requiring at least one non-inertia-advocate role to reference the baseline.

- **V-04 (Axis-G + Axis-H)**: Two-barrier pattern — Phase 2 gates phrase quality, Phase 4 gates label discipline, Phase 6.1 confirms.

- **V-05 (Axis-G + Axis-H + Axis-F)**: Full integration — complete audit chain from Phase 2 phrase quality through Phase 4 pre-anchor through Phase 6.1 early check through LENS AUDIT spread through Phase 7 CROSS-ROLE SPREAD CHECK.
