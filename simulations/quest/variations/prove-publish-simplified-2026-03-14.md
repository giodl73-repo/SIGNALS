---

## Simplification Report — prove-publish QU5

**Original word count**: 1,686  
**Simplified word count**: 1,349  
**Reduction**: 337 words (20.0%)  
**All 5 essential criteria preserved**: YES

---

### What was removed (30 distinct cuts)

Every removal fell into one of four categories:

**1. Meta-commentary doing no instructional work** (73 words cut)
- "Each role has exactly one criterion-responsibility per R4 criterion..." — design philosophy, not direction; role list already shows it
- All `(C-NN)` criterion tags from role list and phase headers — tracking labels for humans; the model needs to know what to produce, not which rubric item it satisfies

**2. Redundancy between adjacent instructions and templates** (90 words cut)
- "Evidence writing is complete when all claims are entered. Mid-Skeptic audits next." — Phase 4 follows Phase 3; implied
- "Lead Author states verdict after Mid-Skeptic scaffold is complete." — Phase 5 follows Phase 4; implied
- "These classifications are provisional. Lead Author uses them in Phase 6." — "Provisional" is in the column header
- "Provisional classifications may not be silently changed." — the SCAFFOLD CONFLICT entry requirement implies it
- "Basis: evidence items above only. No finding prose exists." — duplicates "Classifications committed from evidence items only, before any finding prose"
- "For each finding in the Mid-Skeptic scaffold:" + "Finding prose using final classifications..." — templates are self-explanatory

**3. Aspirational machinery not needed for C-01–C-05** (36 words cut)
- "CONTRIBUTION or INERTIA FLAG as appropriate." — aspirational annotation, zero essential coverage
- Status Quo gap/default fields — minimum 2 beliefs satisfies C-12; extra fields serve C-16 only
- "NET-NEW rows must be explicitly marked." — implied by Status column definition

**4. Verbosity in templates and examples** (138 words cut)
- Output A aside inside the paper template block (22 words → 0)
- NON-NEGOTIABLES closing 3 sentences → 1 sentence
- F-03 row from scaffold table (F-01 + F-02 cover both classification types)
- E-02 intermediate citation audit row (E-01 + "..." covers the pattern)
- F-02 CONFIRMED row from SCAFFOLD AUDIT (CONFIRMED + CONFLICT both shown)
- Method Include text compressed from 42 → 22 words
- SCAFFOLD CONFLICT Reason label: long descriptive → concise

---

### Essential criteria verification

| | Criterion | Preserved |
|---|---|---|
| C-01 | All 8 sections present | YES — Phase 6 lists all 8 explicitly |
| C-02 | Hypothesis explicitly resolved | YES — Phase 5 forces committed verdict; "Not accepted" rejects hedging |
| C-03 | Evidence is traceable | YES — Phase 3 E-[N] format + Phase 4 audit + EVIDENCE COMPLETE gate |
| C-04 | Findings are synthesized | YES — "[conclusion — 'what does this mean?']" + PF-04 + Post-Skeptic Item 4 |
| C-05 | Principles are extractable | YES — "Minimum 2 numbered rules. Form: Always X..." with finding citations |

```json
{"simplified_word_count": 1349, "original_word_count": 1686, "all_essential_still_pass": true}
```
