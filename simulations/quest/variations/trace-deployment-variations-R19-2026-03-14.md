Saved to `simulations/quest/golden/trace-deployment-variate-R19-2026-03-15.md`.

---

## Round 19 — trace-deployment Variate Summary

**5 variations generated. Axes used: Role Sequence (single), Output Format (single), Lifecycle Emphasis (single), + two combinations.**

### Variation Map

| Var | Axis | C-37 | C-38 | C-39 | C-40 | Notes |
|-----|------|:----:|:----:|:----:|:----:|-------|
| V-01 | Role Sequence | PASS | PASS | PASS | PASS | Commerce-first Stage 1 → Operations Stage 2; per-stage vocab lists; 4 domain sub-questions |
| V-02 | Output Format | PASS | PASS | PASS | PARTIAL | Both stages table-anchored with row floors; sub-questions name domains but don't cover all 4 phases |
| V-03 | Lifecycle Emphasis | PASS | PASS | PASS | PASS | Per-phase vocab + coverage floors; Stage 2 uses 4×4 (phase × domain) sub-question grid |
| V-04 | Role Seq + Register | PASS | PASS | PASS | PASS | DIRECTIVE/SUB-QUESTION framing; required fields per item; eliminates prose hedging |
| V-05 | Combined (all three) | PASS | PASS | PASS | PASS | Per-phase tables + coverage floors + 8 domain sub-questions; designed for 200/250 ceiling |

### Key design decisions

**V-01** is the clean baseline — single-axis, two vocabulary lists, four domain sub-questions in Stage 2. The stage boundary is unambiguous. C-40 passes because sub-questions 1–4 each name a domain explicitly.

**V-02** is the table-enforcement bet: mandatory row fills with `[S2]` prefixing make domain gaps structurally visible at inspection time. C-40 is only PARTIAL because Stage 2 sub-questions don't decompose by phase — they're domain-only. This is the variation most likely to score lower if the rubric checks phase coverage.

**V-03** is the anti-phase-collapse design. The 4×4 sub-question grid (1a/1b/1c/1d through 4a/4b/4c/4d) forces Stage 2 to cross every domain against every phase. This is the strongest C-40 implementation outside of V-05.

**V-04** tests whether DIRECTIVE + required-field lists produce more artifact density than open-ended prose instructions. The formal register also reduces the "Add monitoring" class of generic answers — the AUTOMATION HOOKS constraint line explicitly rejects that pattern.

**V-05** is the ceiling-target prompt: per-phase tables with floor constraints, eight named domain sub-questions (2 per domain × 4 domains), and an expanded AUTOMATION HOOKS table with a Pipeline Stage column. All four C-37–C-40 criteria fire simultaneously. The sub-questions reference Stage 1 by Phase + row number, which is the specific Stage 2 → Stage 1 cross-reference C-37 requires.
