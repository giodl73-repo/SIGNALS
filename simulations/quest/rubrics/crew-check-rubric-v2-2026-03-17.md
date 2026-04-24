v2 written. Here's what changed and why:

**Three new aspirational criteria added from R1 excellence signals:**

| ID | Name | Source signal |
|----|------|---------------|
| C-11 | Lens-anchoring step | V-02 failed C-03 precisely because it lacked the explicit `orientation.frame` quote step that V-01/V-03/V-04 all enforce. The mechanism explains the outcome. |
| C-12 | Severity calibration contract | V-02 got PARTIAL on C-08 due to absent operational definitions. V-01/V-03/V-04 all define HIGH/MEDIUM/LOW with commit-gate semantics, not just labels. |
| C-13 | Challenger-first sequencing | Structural forcing function present in all three golden variations; drives severity anchoring and voice differentiation across subsequent reviewer rows. |

**Scoring mechanics:**
- Aspirational tier stays at 10 pts total — redistributed from 5 pts × 2 to 2 pts × 5
- Golden threshold unchanged: all 5 essential + composite >= 80
- A perfect R1 golden variation (V-01/V-03/V-04) now scores ~97 rather than ~97.5 — the new criteria were already exhibited, so scores are stable; future variations that miss C-11/C-12/C-13 will correctly score lower on the aspirational tier
