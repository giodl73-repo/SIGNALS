Written to `simulations/quest/golden/draft-proposal-variate-R18-2026-03-15.md`.

---

## Round 18 Variate Summary

**New criteria in v18:** C-44 (T-40 CONDITION exemplar must explain *why* the quoted T-38 form is abstract) and C-45 (T-42 CONDITION must carry inline exemplar of a deficient T-40 form). Denominator /36 → /38.

### Five variations

| # | Axis | Key mechanism | Designed fails | Predicted score |
|---|------|---------------|----------------|-----------------|
| **V-01** | Lifecycle emphasis | T-40 and T-42 both abstract in spec — no exemplar content guidance | C-42→C-43→C-44 cascade + C-45 = 4 fails | 34/38 → **98.95** |
| **V-02** | Output format | T-40 gets exemplar-quoting directive only (no abstractness explanation, no prescription); T-42 abstract | C-44 (independent), C-43, C-45 = 3 fails | 35/38 → **99.21** |
| **V-03** | Phrasing register | T-40 fully spec'd with labeled Part 1 (exemplar+explanation) and Part 2 (prescription); T-42 abstract-only | C-45 only = 1 fail | 37/38 → **99.74** |
| **V-04** | Lifecycle + output format | Stale T-24 check (`!= 43`) → 43-row table; T-40 exemplar-guided but no explanation or prescription; T-42 exemplar-guided | C-24, C-44, C-43 = 3 fails | 35/38 → **99.21** |
| **V-05** | Phrasing register + cascade | Phase 2 RISK uses inline P×I (no `[R-NN pending]`); Phase 9b absent; T-40/T-42 abstract | C-23 cascade root → C-26+C-31..C-43+C-44+C-45 = 17 fails | 21/38 → **95.53** |

### What's new in R18 vs R17

- **T-24 count bump**: all v18 specs say `!= 45`; V-04 deliberately uses stale `!= 43` to fire C-24
- **T-40 CONDITION Part 1 extension**: the exemplar must now include the abstractness explanation inline (C-44). V-02 is the clean isolation of C-44 independent fail — exemplar present, explanation absent
- **T-42 CONDITION exemplar**: new in v18. V-03 is the C-45 isolation — T-40 fully documented, T-42 gets no exemplar direction
- **Cascade depth in V-05**: the C-23 cascade root now pulls 2 more criteria (C-44 via C-42 cascade, C-45 independent) compared to the same path under v17
