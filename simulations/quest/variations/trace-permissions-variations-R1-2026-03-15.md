Written to `simulations/quest/golden/trace-permissions-variate-R1-2026-03-15.md`.

---

## Round 1 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence -- entity-centric, risk-surface-first | Anchoring on entities before roles forces C-01 completeness; riskiest entity first pulls C-03/C-04 forward before attention degrades |
| V-02 | Output format -- prose investigation log with explicit tokens (FINDING / GAP / VERDICT / FIX) | Tests whether C-03/C-04 depth survives without table scaffolding; reveals whether structure or reasoning does the work |
| V-03 | Phrasing register -- conversational walking-investigator, first-person | Mandatory surprise and judgment language ("this concerned me because...") prompts C-04/C-07 coverage that formal enumeration voice suppresses |
| V-04 | Combined: extended inventory gate + phase-end checkpoint summaries | Hard gates with self-audit checkpoints prevent the skip pattern of completing the operation matrix then skipping FLS; model must confirm coverage before advancing |
| V-05 | Combined: inertia framing (stated assumptions before analysis) + CS-last as validator | Writing design assumptions first makes assumption-violation the primary output type; CS role traced last becomes a test of expert-level claims rather than a parallel description |

---

**Design notes on the axes chosen vs. R1:**

R1 (already in the file from a prior session) used: LP scoring matrix, ceiling/floor role sequence, formal specification assertions, checkpoint gates, and adversarial/inertia framing.

These five new variations go different directions:
- V-01 reorders the analysis around *data* rather than *roles* -- entity-centric is a structurally different starting point
- V-02 strips tables entirely to isolate whether reasoning or scaffolding drives coverage
- V-03 tests whether permission-granting language ("I found... this surprised me") produces better gap identification than declarative enumeration
- V-04 combines lifecycle gates (like R1-V04) but adds explicit self-audit checkpoints the model must sign off on
- V-05 uses inertia framing differently than R1-V05 -- instead of "default config as adversary," it's "stated team assumptions as hypotheses to falsify," which is a softer but broader framing that applies even when the team has customized the config
