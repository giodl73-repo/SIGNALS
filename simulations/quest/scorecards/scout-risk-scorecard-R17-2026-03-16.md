---

# Scout-Risk — Round 17 Score — v16 Rubric

## Summary

| Variation | C-01..C-47 | C-48 | C-49 | C-50 | Score | Band |
|-----------|-----------|------|------|------|-------|------|
| Baseline (R16 V-05) | 168/168 | PASS | PASS | FAIL | 172/174 | Strong |
| V-01 | 168/168 | PASS | PASS | **PARTIAL** | 173/174 | Strong |
| V-02 | 168/168 | PASS | PASS | **PARTIAL** | 173/174 | Strong |
| V-03 | 168/168 | PASS | PASS | **PASS** | **174/174** | **GOLDEN** |
| V-04 | 168/168 | PASS | PASS | **PASS** | **174/174** | **GOLDEN** |
| V-05 | 168/168 | PASS | PASS | **PASS** | **174/174** | **GOLDEN** |

---

## Key Findings

**C-48 (structural independence)**: PASS in all variations — Phase 0c is a standalone `###` sibling of Phase 0 throughout. V-04 and V-05 additionally make this verifiable by local inspection ("equal structural weight to Phase 0" stated in the block itself).

**C-49 (per-site citation)**: PASS in all variations — baseline citations `(Phase 0c taxonomy)` already satisfy the criterion. V-05 upgrades to the exact block heading string `(Phase 0c Violation Taxonomy)` — verifiable by character-level match, no abbreviation resolution needed. No score change (already at max).

**C-50 (explicit closure declaration — compound AND)**: The isolation tests confirm the compound is enforced:
- V-01 ("This taxonomy is closed." only) → **PARTIAL** — half 1 alone insufficient
- V-02 ("No violation category outside this list..." only) → **PARTIAL** — half 2 alone insufficient
- V-03 through V-05 (both sentences) → **PASS**

**Recommended canonical**: V-03 for minimal stable form; V-05 for maximum audit precision.

---

## Excellence Signals

1. **Compound criterion isolation testing** — Designing V-01 and V-02 as deliberate half-tests proves the AND is enforced, not optional.
2. **Explicit structural parity declaration** — Stating "equal structural weight to Phase 0" within Phase 0c converts inferred structural equivalence to a stated constraint, verifiable by local inspection.
3. **Fully-qualified block name at citation sites** — Using the exact block heading as citation text (`Phase 0c Violation Taxonomy`) makes C-49 verifiable by character-level matching.

---

```json
{"top_score": 174, "all_essential_pass": true, "new_patterns": ["compound criterion isolation testing: V-01 and V-02 prove C-50 AND compound is enforced — closure declaration alone (V-01) and prohibition clause alone (V-02) both land at PARTIAL, confirming both halves are required", "explicit structural parity declaration: stating equal structural weight to peer block within the block opening converts inferred structural equivalence to a locally verifiable stated constraint", "fully-qualified block name at citation sites: using exact block heading string as citation text makes drawn-from verifiable by character-level match, eliminating abbreviation resolution"]}
```
