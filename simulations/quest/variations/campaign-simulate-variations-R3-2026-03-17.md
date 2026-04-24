Written to `simulations/quest/golden/campaign-simulate-variate-R3-2026-03-17.md`.

---

## Round 3 Variations Summary

**Single-axis variations target the three new v3 mechanisms (C-14, C-16, C-17/C-15/C-18):**

| Variation | Axis | Hypothesis | Primary Criteria Targeted |
|-----------|------|-----------|--------------------------|
| **V-01** | Schema-declaration first | Opening the prompt with the schema + boundary vocabulary map makes C-14 a transcription from line 1, not a recall from buried instructions | C-14, C-18 |
| **V-02** | Sentinel manifest pre-generation | Pre-authoring clean-run sentinel rows before any sub-skill executes makes C-16 a copy operation, not on-demand authoring after the fact | C-16, C-14 (manifest carries vocabulary) |
| **V-03** | Verification-gate-as-section | Elevating C-17 to a named section with a per-column audit table (PASS/FAIL + blank count) makes the gate inspectable in the artifact, not implied by clean output | C-17, C-15 |

**Combined variations:**

| Variation | Axes | What closes by construction |
|-----------|------|----------------------------|
| **V-04** | Schema-declaration + Sentinel manifest | C-14 (vocab from schema header), C-16 (manifest rows), C-18 (single table declared first), C-15 follows from schema contract |
| **V-05** | Schema-declaration + Sentinel manifest + Verification-gate-as-section | All five: C-14 + C-15 + C-16 + C-17 + C-18 each enforced by a distinct setup/gate artifact |

**Key difference from R2:** R2 embedded all structural requirements inside sub-skill instructions. R3 extracts them into *pre-execution setup artifacts* (schema contract, sentinel manifest) and *post-execution verification artifacts* (gate section). The hypothesis is that structure defined before the author touches a finding is more reliably followed than structure embedded in per-skill instructions.
