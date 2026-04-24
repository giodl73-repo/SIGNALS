Written to `simulations/quest/golden/corps-build-variate-R10-2026-03-17.md`.

---

## R10 -- corps-build: 5 Variations

**Baseline**: V-05 R9 (full C-01 through C-29 architecture, 100/100 on v9 rubric).

**Three candidate criteria surfaced:**

| Candidate | Axis | Source |
|-----------|------|--------|
| C-30 | **AMEND-CLEAR** -- named exit-gate re-audit after AMEND-RECEIPT rewrite | V-01, V-04, V-05 |
| C-31 | **BUILD-VERIFY-CLEAR** -- named re-audit gate after DRIFT correction | V-02, V-04, V-05 |
| C-32 | **PROFILE-ENTRY-VALID** -- per-entry specificity receipt before PROFILE-GATE | V-03, V-05 |

**Variation table:**

| Variation | Single axis | C-30 | C-31 | C-32 |
|-----------|-------------|------|------|------|
| V-01 | AMEND-CLEAR | YES | -- | -- |
| V-02 | BUILD-VERIFY-CLEAR | -- | YES | -- |
| V-03 | PROFILE-ENTRY-VALID | -- | -- | YES |
| V-04 | V-01 + V-02 | YES | YES | -- |
| V-05 | Full integration | YES | YES | YES |

**Design rationale (all three are TRANSCRIPTION-CLEAR analogs):**

- **AMEND-CLEAR** (C-30): AMEND-RECEIPT already closes the C-27 type-tag verification loop. AMEND-CLEAR adds the same re-audit exit guarantee that TRANSCRIPTION-CLEAR adds to PATH-B -- all three slots confirmed after any rewrite, not just the rewritten one. AMEND-PATH-A/AMEND-PATH-B are named siblings per C-22.

- **BUILD-VERIFY-CLEAR** (C-31): BUILD-VERIFY already corrects per-team DRIFT and re-emits per-team VERBATIM-BOTH. BUILD-VERIFY-CLEAR adds the post-correction global re-audit -- all N teams confirmed in one named pass before BUILD-VERIFY-COMPLETE. BV-PATH-A/BV-PATH-B are named siblings.

- **PROFILE-ENTRY-VALID** (C-32): The PROFILE block already declares a specificity rule. PROFILE-ENTRY-VALID closes specificity as a per-entry structural token with four named checks (defended-artifact, change-pressure, lens-phrase, expertise-seed), VALID/INVALID verdict per team, and rewrite before next entry on INVALID. PROFILE-GATE is gated on all-VALID.

All three are orthogonal: different phases, different receipts, independent of each other.
