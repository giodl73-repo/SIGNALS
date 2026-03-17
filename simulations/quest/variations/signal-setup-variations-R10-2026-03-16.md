Written to `simulations/quest/golden/signal-setup-variate-R10-2026-03-16.md`.

---

## Round 10 Variations — Summary

**Context**: R9 scored 100/100 (v8 rubric) for V-01, V-04, V-05. Three new criteria in v9 (C-25/C-26/C-27) formalize structural patterns observed but not yet enforced.

**Key gap from R9**: R9 V-05 (best carry-forward) probably passes C-25 and C-26 but has a **C-27 risk** — the Copilot already-configured case may live under a `**bold**` inline pseudo-gate rather than a `###` heading.

**Variation axes**:

| Var | Axes | C-25 | C-26 | C-27 | Predicted |
|-----|------|------|------|------|-----------|
| V-01 | A: Single detection parent (GATE 1A/1B) | PASS | FAIL | PARTIAL | 98.95 |
| V-02 | B: Copilot dual sub-gates (GATE 6A + GATE 6B) | PASS | PASS | PARTIAL | 99.47 |
| V-03 | C: No bold routing anywhere | PASS | PASS | PASS | 100.0 |
| V-04 | A+B: Consolidated + dual sub-gates | PASS | PASS | PROBABLE | 99.47–100.0 |
| V-05 | A+B+C: Full precision | PASS | PASS | PASS | 100.0 |

**Key structural decisions in V-05** (the full-coverage variant):
- Detection branches under a single parent: `GATE 1A` (missing) and `GATE 1B` (already configured) both encode `parent=1`
- Copilot extension: `GATE 5A` (already configured) + `GATE 5B` (confirm append) — full first-class sub-gate promotion for both
- Zero `**bold**` routing in parent gate bodies — all routing is plain prose pointing to heading-delimited sub-gates
- Heading outline enumerates all 10 gates/sub-gates without reading prose

**V-03 is the dark horse**: achieves 100.0 with the minimum sub-gate interpretation — only the confirmation needs to be a named sub-gate (GATE 6A), not the already-configured detection case. Simpler structure than V-05; if C-26 requires both branches to be promoted, V-03 drops.
