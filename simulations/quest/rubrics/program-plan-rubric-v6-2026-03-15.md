Written to `simulations/quest/rubrics/program-plan-rubric-v6-2026-03-16.md`.

---

## Three new criteria added from R5 excellence signals

**C-22 — Complete Recommended-Tier Error Annotation**
All three recommended criteria (C-05, C-06, C-07) must appear in error artifacts, not just "at least one" as C-19 requires. C-19 opens the cross-tier coverage gap; C-22 closes it. R5 source: V-01's BAD PLAN tagged all three — `# WRONG C-05`, `# WRONG C-06`, `# WRONG C-07` — the first full recommended-tier annotation. Pass: all three covered; no partial.

**C-23 — Dual-Position Zone Dependency Reminder**
Dependency reminders appear at BOTH the zone-header AND the `skills:` placeholder within each dependency-bearing zone. C-20 requires only the skills position; C-23 adds the zone boundary, closing both attention gaps within a zone. R5 source: V-01 failed C-20 (header only, not skills position); V-02 passed with both positions — `# requires: ...` at zone header AND at `skills:` line. Pass: all dependency-bearing zones dual-position; partial: >= half.

**C-24 — Template-Field Gate Contrast**
Per-zone FAIL/PASS gate contrast appears as actual YAML template fields (`FAIL gate: "..."` / `PASS gate: "..."` as skeleton keys), not just comment annotations. C-17 requires inline per-zone contrast; C-24 requires the contrast to be structural — YAML keys the model must resolve, not comments it can scan past. R5 source: V-02 embedded labeled contrast pairs as YAML fields at all 5 non-echo zones. Pass: all non-echo zones have template-field contrast; partial: >= half.

**Scoring change:** Aspirational tier 14 → 17 criteria, 70 → 85 pts. Total max is now **175**. Golden threshold (>= 80) unchanged.
