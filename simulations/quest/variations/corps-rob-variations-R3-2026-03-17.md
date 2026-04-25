`sim/simulations/quest/golden/corps-rob-variate-R3-2026-03-17.md`

---

## R3 Variate Summary

**Target score:** 99+ (V-05 R2 ceiling was 97; two gaps cost 3 pts)

### What R3 fixes

| Gap | R2 cost | R3 mechanism |
|-----|---------|--------------|
| C-10 FAIL (all 5 variations) | −2 pts | `## Cross-Cutting Themes` section: named themes, ≥2 F-IDs from different stages, elevation sentence explaining *why* multi-stage recurrence is worse than single-stage |
| C-11 PARTIAL (all passing) | −1 pt | `CROSS-STAGE SYNTHESIS` block inside the closing handoff packet: backward F-ID entries with relationship type, ≥5 total across a 6-stage run |

### Variation grid

| Variation | C-10 fix | C-11 fix | V-05 base | Purpose |
|-----------|---------|---------|-----------|---------|
| **V-01** | YES | NO | minimal | Isolate C-10 |
| **V-02** | NO | YES | minimal (no briefing envelope) | Isolate C-11 via packet consolidation |
| **V-03** | NO | YES | V-05 full | C-11 on V-05 base; preserves briefing envelope |
| **V-04** | YES | YES | V-05 full | Both gaps fixed; first design targeting 99+ |
| **V-05** | YES | YES | 3-section minimal | No briefing envelope; single mechanism per gap; constraint-minimized |

### Key hypotheses to test

- **V-04 vs V-05**: Does the briefing envelope's C-02 enrichment justify its overhead, or does the minimal V-05 3-section design achieve the same score with less prompt surface?
- **V-02 risk**: Without the briefing envelope, does `CROSS-STAGE SYNTHESIS` in the packet alone hold C-08 at PASS, or does it degrade to C-08 PARTIAL?
- **V-04 redundancy risk**: Four backward-synthesis surfaces (briefing envelope + cross-stage references + handoff packet synthesis + themes section) — does the model produce genuine escalation analysis or shallow structural compliance at each?
