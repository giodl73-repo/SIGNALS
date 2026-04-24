# org:committee Round 17 — Scorecard

## Summary

| Variation | Essential | Recommended | Aspirational | Composite | All Essential |
|-----------|-----------|-------------|--------------|-----------|---------------|
| V-01 | 60/60 | 30/30 | 70/70 | **160/160** | YES |
| V-02 | 60/60 | 30/30 | 65/70 | **155/160** | YES |
| V-03 | 60/60 | 30/30 | 69/70 | **159/160** | YES |
| V-04 | 60/60 | 30/30 | 70/70 | **160/160** | YES |
| V-05 | 60/60 | 30/30 | 70/70 | **160/160** | YES |

## Key Gaps

**V-02 (155/160):** C-28 FAIL (no skeleton pre-declaration step — architecturally incompatible with C-43) + C-43 FAIL (no `[BIDIRECTIONALITY: ___]` placeholder) + C-37 PARTIAL (named manifest sections are fill-time, not pre-declared). The variation's own hypothesis correctly predicted the ~158 ceiling — actual is 155 due to C-37 partial.

**V-03 (159/160):** C-30 PARTIAL — conversational register slides into descriptive prose in fill rules ("Look up .roles/...", "The point of Phase 1 is to find..."). PRINT/ENFORCE/VALIDATE anchors retain imperative register but surrounding guidance doesn't.

## Excellence Signals (V-04 / V-05 over V-01)

All three hit 160/160, but V-04 and V-05 demonstrate stronger patterns:

1. **Three-mode FAILS on INVARIANT VALIDATE** — tests each required seal element independently: (a) phase-commit present but prohibition absent, (b) both elements absent in a present seal line, (c) line absent entirely. V-01/V-02/V-03 only cover modes (b) and (c).

2. **VALIDATE on the BIDIRECTIONALITY clause fill itself** — `ACCEPTABLE: both directions stated / FAILS: only one direction named — half-coupling`. Converts the slot from structural presence to content-completeness test.

3. **Inertia-Advocate structurally guaranteed via SYNTHESIZE** — ensures Phase 1 findings always have an owner-voice in Phase 3 regardless of charter coverage.

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["Three-mode FAILS coverage on INVARIANT VALIDATE rules: enumerate (a) phase-commit present but prohibition absent, (b) both elements absent in a present seal, and (c) line absent entirely — testing each required element as an independent failure axis rather than testing joint absence", "VALIDATE rule on the BIDIRECTIONALITY clause fill itself — ACCEPTABLE: both directions stated / FAILS: only one direction named — converts the clause from a structural presence requirement to a content-completeness test", "Inertia-Advocate as a guaranteed structural participant via SYNTHESIZE instruction when absent from charter — ensuring Phase 1 findings always have an owner-voice in Phase 3 without depending on charter coverage"]}
```
