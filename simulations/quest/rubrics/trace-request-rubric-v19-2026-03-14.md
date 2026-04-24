**v19 written** to `simulations/quest/rubrics/trace-request-rubric-v19-2026-03-15.md`.

## What changed from v18 → v19

**One new criterion promoted from R20 excellence signals:**

**C-45 — GATE-8B VALIDATION-DERIVATION inline derivation token** (Tier B+ promoted)
- **Source:** R19 V-03 (first axis, structured field blocks, no CONSISTENCY-RULE confound) + R20 V-01 (second independent axis, phrasing register, no CONSISTENCY-RULE confound) + R20 V-03 (third confirming axis)
- **Signal:** `VALIDATION-DERIVATION: [derive outcome from matches value at point of emission: "yes" → "Contract prediction confirmed"; "no" → "falsified -- actual halt boundary was [BC-N label]"]` as a named structural token in the EVENT: CONTRADICTION / Step 8b block, co-located with DECLARE CONTRADICTION before Step 8c
- **R20 V-02 confirmation:** When C-44 (CONSISTENCY-RULE) is present, C-45 is intentionally suppressed — clean axis separation confirms the two are complementary design choices, not redundant
- **Depends on:** C-42 (source boolean) AND C-40 (Step 8b DECLARE CONTRADICTION location)

**Key design notes added:**
- C-45 vs C-44: competing surfaces — C-44 encodes derivation pre-trace in algorithm block; C-45 surfaces it inline at contradiction-fire point; V-02 pattern = C-44 PASS + C-45 FAIL; V-01/V-03 pattern = C-45 PASS + C-44 FAIL; combined = both PASS
- C-45 vs C-40 and C-45 vs C-42: disambiguation entries added

**Scale:** 275 → **280** (aspirational: 37 → 38 criteria, 185 → 190 pts). Golden threshold: **224/280** (80%).
