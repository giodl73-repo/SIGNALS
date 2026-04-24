Written to `simulations/quest/golden/campaign-decide-variate-R4-2026-03-16.md`.

---

## R4 Summary

**R3 diagnosis driving R4**: R3 V-05 (the 100-target) is ambiguous on C-16 — it pre-assigns FIDs inline within phase sections, but the rubric evaluation note requires "a preamble section before any evidence heading." This ambiguity is what R4 resolves.

**Three single-axis variations:**

| ID | Axis | Key mechanism | C-16 | C-17 | Predicted v4 |
|----|------|--------------|------|------|--------------|
| V-01 | C-16 full preamble | Standalone FINDING REGISTER table with "—" skeletons before Phase 0 | **PASS (unambiguous)** | PASS (5 labeled slots) | 98.9–100 |
| V-02 | C-17 formula | "SLOT COUNT (5) = PHASE COUNT (5)" declared in synthesis preamble | FAIL (no FID system) | **PASS (arithmetic declared)** | 96.7 |
| V-03 | C-16 compact range | Register table lists FID *ranges* per phase (F0-01..F0-06), not individual rows | **CONDITIONAL** | PASS | 97.8–100 |

**Two combined variations:**

- **V-04** (100-target): full preamble register + formula slot count + Phase 0 + pre-assigned FIDs. All 9 aspirational criteria by construction. Only residual risk: C-12 FID-vs-Phase-syntax debate (low-to-moderate).
- **V-05** (phrasing axis): identical structure to V-04 with plain prose instructions instead of all-caps imperatives. Tests whether structure alone enforces compliance regardless of phrasing register.

**The R4 structural thesis**: C-16 and C-17 are best addressed by two distinct template mechanisms — a pre-phase register section (not inline FID tags) and an arithmetic slot-count declaration (not just counting labeled slots). V-04 applies both. V-03 tests the minimum viable register design.
