Written to `simulations/quest/golden/quest-score-variate-R3-2026-03-16.md`.

---

## quest-score Variate — Round 3

### What changed from R2

R2's two excellence signals became the new criteria:
- **C-13** (derivation-complete gate marker) — sourced from V-01's `[DERIVE COMPLETE]` gate
- **C-14** (required fields in primary output block) — sourced from V-02's in-block `#### Golden` placement

Expected R2 verdicts on the new criteria: V-04 and V-05 likely pass both; V-01 passes C-13 but fails C-14 (Golden in synthesis); V-02 passes C-14 but fails C-13 (no gate token); V-03 fails both.

### Variation axes

| Axis | V | Single/Combined | Core mechanism |
|------|---|-----------------|----------------|
| D — DERIVE phase hardening | V-01 | Single | Pre-gate self-scan (2nd enforcement point for C-13) + explicit Phase 3 prohibition |
| E — Pre-printed in-block skeleton | V-02 | Single | All required per-output sections pre-printed as fill-in fixtures; post-block completeness scan |
| F — C-13/C-14 anti-patterns | V-03 | Single | Named negative examples for both failure modes: gate absent/premature (C-13), fields in synthesis/drift (C-14) |
| D+E | V-04 | Combined | Gate hardening + pre-printed skeleton |
| D+E+F | V-05 | Combined | All three axes; anti-patterns fire first, gate fires at Phase 1/3 boundary, skeleton fires per-block |

### Key structural prediction

V-04 and V-05 should pass C-13 and C-14. The discriminators within the passing cluster will be structural strength: does V-05's pre-scan + pre-printing + anti-pattern reinforcement reduce model-behavior risk on C-14 compared to V-04's pre-printing alone? V-03 is the risk probe: does a negative anchor without structural enforcement produce compliance, or does it merely shift which failure mode appears?
