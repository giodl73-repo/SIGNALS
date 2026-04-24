Written to `simulations/quest/golden/corps-achievements-variate-R11-2026-03-16.md`.

---

## Variate R11 — corps-achievements

**Basis**: R9 V-05 scored 100 on v8; R11 is the first round targeting v10 (C-29, C-30, C-28 redefined). No R10 variate was produced.

---

### Variation Axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | C-29 as labeled `RETRY:` blocks | Making retries observable (not just instructed) creates an auditable correction artifact — a labeled block can't be silently dropped |
| **V-02** | C-30 as standalone `ATTRIBUTION INTEGRITY GATE [C-28/C-30]` | Isolation forces backward-inference prohibition to be its own pass/fail step, not absorbed into a larger cluster gate pass |
| **V-03** | C-28 pervasive first-person ownership | Applying `"Before I write this section, I confirm [C-28]:"` at every output section (not just leaderboard) shifts the model from checklist auditor to committed agent throughout |
| **V-04** | C-29 retry blocks + C-30 standalone gate + stagnation-first lifecycle | Phase 0 pattern diagnosis makes retries contextually richer ("correction predicted by [PATTERN_LABEL]"), and C-30 is reinforced by Phase 0 having enumerated contributors without scoring before the attribution gate runs |
| **V-05** | C-29/C-30 absorbed into super-gate labels; C-27 updated | LEADERBOARD CLUSTER GATE becomes `[C-16/C-19/C-21/C-30]`; STRUCTURAL AUDIT expands to `[C-20/C-25/C-26/C-27/C-28/C-29/C-30]`; C-27 verifies the new label — a model that writes the old label without C-30 produces a C-27-detectable wrong-enumeration failure |

### Key structural changes across all five

1. **C-29 fail paths**: All existing "Fail:" lines updated to `GATE FAILED [C-XX]: [specific instance] — CORRECTION: [action]. Re-running this section.` — V-01 and V-04 additionally wrap the re-run in labeled `> RETRY: … > END RETRY` blocks.

2. **C-30 placement**: V-01/V-03 embed it in the leaderboard pre-write confirmation; V-02/V-04 isolate it as a standalone `ATTRIBUTION INTEGRITY GATE [C-28/C-30]`; V-05 absorbs it into the cluster label `[C-16/C-19/C-21/C-30]`.

3. **C-28 redefinition**: All variations use `"Before I write this section, I confirm [C-28]:"` ownership syntax — V-03 applies it at every output section header.

4. **V-05 C-27 update**: The structural audit's named super-gate verification now covers `LEADERBOARD CLUSTER GATE [C-16/C-19/C-21/C-30]` with all four IDs enumerated, closing the wrong-enumeration failure mode for the new criterion.
