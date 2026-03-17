Written to `simulations/quest/golden/mock-review-variate-R4-2026-03-15.md`.

---

## Round 4 — Summary

**What R3 left open** (three new v4 criteria extracted from R3 signals):

| Criterion | R3 V-05 state | R4 fix |
|-----------|--------------|--------|
| C-17 Auto-flagged contamination guard | Prohibition present, error unnamed | V-01: "named error: **auto-rule contamination**" appended; violation diagnosable by label |
| C-18 Inter-step gate with next-step reference | Role-step gates (STEP 3→4, 4→5) already name next step; READ and AUTO-FLAG gates do not | V-02: all eight gate positions updated to "DO NOT proceed to STEP N until..." |
| C-19 Structured trigger notation | Two notations co-exist: `trigger = ` in listing, `Trigger:` in template; not mechanically parseable from single rule | V-03: unified `trigger = {label}` everywhere; structural field note with enumeration and fixed position |

**Variation axes:**

- **V-01** (single): lifecycle — named contamination error (C-17)
- **V-02** (single): lifecycle — all-gate forward naming (C-18)
- **V-03** (single): output-format — unified trigger field notation (C-19)
- **V-04** (combined): C-17 + C-18
- **V-05** (ceiling): C-17 + C-18 + C-19 + pre-printed next-steps skeleton with mandatory cross-namespace risk statement (C-09)

The most interesting discriminator is whether V-05's C-09 slot is satisfied genuinely — a cross-namespace synthesis that names a specific Tier-N decision at risk — or syntactically, as a restatement of the top-ranked REAL-REQUIRED namespace. That's the test to watch in scoring.
