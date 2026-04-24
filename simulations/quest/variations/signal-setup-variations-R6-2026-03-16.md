---

## signal-setup R6 Variations — V-01 through V-05

Written to `simulations/quest/golden/signal-setup-variate-R6-2026-03-16.md`.

---

### What this round targets

v6 added two criteria from the R5 V-05 pattern:

| New criterion | Gap in V-05 R4 |
|---|---|
| **C-19** — future-moment anchor at *every* decline exit | GATE 4 had it ("before the next build"), GATE 1 didn't |
| **C-20** — GATE 2 names the *mechanism* of permanence (auto-load) | GATE 2 affirmed consequence but not how it works |

All other criteria (C-01..C-18) were already passing in V-05 R4 — all five variations carry them forward unchanged.

---

### Variation map

| # | Axis | Change | C-19 | C-20 | Predicted |
|---|------|--------|------|------|-----------|
| V-01 | Axis A — GATE 1 anchor | GATE 1 decline: adds "before you write the first line" | PASS | FAIL | 99.2 |
| V-02 | Axis B — GATE 2 mechanism | GATE 2: adds "every session... loads CLAUDE.md automatically" | FAIL | PASS | 99.2 |
| V-03 | Axis C — GATE 6 anchor | GATE 6 decline: adds Copilot-specific future moment | PARTIAL* | FAIL | 98.3–99.2 |
| V-04 | A+B | GATE 1 + GATE 2 both fixed | PASS | PASS | **100.0** |
| V-05 | A+B+C | All three decline exits carry distinct future moments | PASS | PASS | **100.0** |

*V-03 is the C-19 boundary probe — it only passes if GATE 6 counts as an "equivalent exit" under the rubric's definition.

**Three future moments in V-05:**
- GATE 1: *"before you write the first line"* — workspace with no CLAUDE.md
- GATE 4: *"before the next build"* — workspace with CLAUDE.md, Signal absent
- GATE 6: *"before the next Copilot session reaches for a build suggestion"* — Copilot unconfigured

V-04 is the minimum path to 100. V-05 is the semantically complete form — holds in both narrow and broad readings of C-19.
