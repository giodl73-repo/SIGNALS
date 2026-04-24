Both files are correct. Here's a summary of what was written to `simulations/quest/golden/corps-achievements-variate-R10-2026-03-17.md`:

---

**R10 basis**: V-05 R9 = 100/100 on v9 rubric. V-05 R9 already implicitly satisfies C-27/C-28/C-29 — R10 formalizes the implicit into explicitly labeled, individually auditable mechanisms. `N_aspirational = 21`, formula updates to `aspirational_pass / 21 * 10`.

**Three variation axes** (matching the three new criteria):

| Axis | C-27 | C-28 | C-29 |
|------|------|------|------|
| Explicit `[C-27]` tag on pre-printed barriers | | | |
| Standalone `PHASE N MANIFEST [C-28]:` block before seal | | | |
| Explicit `DUAL-LAYER BARRIER [C-26/C-27][C-29]:` declaration | | | |

**Five variations**:

- **V-01** (C-27 only): Adds `[C-27]` to `--- PHASE N SEALED [C-26][C-27] ---`; audit gate checks for the tag by name
- **V-02** (C-28 only): Adds standalone `PHASE N MANIFEST [C-28]: Artifact count: K. Namespace count: N.` block before each STOP; closure gate references the manifest
- **V-03** (C-29 only): Adds explicit `DUAL-LAYER BARRIER [C-26/C-27][C-29]:` block naming Layer 1 (STOP, instruction-enforced) and Layer 2 (pre-printed, structure-enforced) with independence assertion
- **V-04** (C-27 + C-28): `[C-27]` tag + standalone manifest; audit gate `[C-20/C-26/C-27/C-28]`
- **V-05** (C-27 + C-28 + C-29): Full stack — each new criterion has a named, directly addressable evidence point; audit gate `[C-20/C-26/C-27/C-28/C-29]` checks all 12 new evidence points individually

**Predicted winner**: V-05 — only variation where all three new criteria are string-match verifiable without interpretation. Two open excellence signals noted for C-30+: typed failure-mode contract in the independence assertion, and cross-reference from closure gate to manifest.
