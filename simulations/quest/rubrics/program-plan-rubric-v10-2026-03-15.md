Written to `simulations/quest/rubrics/program-plan-rubric-v10-2026-03-16.md`.

---

## Two new criteria extracted from R9 excellence signals

**C-34 — Compound gate_fail: Annotation**

Source: V-02's diagnostic gap. V-02 passes the full gate infrastructure stack (C-24+C-28+C-32 all PASS) while failing both C-25 (no `Why:` rationale) and C-26 (no criterion tag at `gate_fail:`). This is the first variate to build production-side gate machinery while leaving both teaching-side annotations absent from the `gate_fail:` field. The pattern: C-25 and C-26 are independently satisfiable and independently missing — they must be explicitly co-required as a compound annotation at the field position itself.

**Pass condition**: Every non-echo zone's `gate_fail:` field carries both an inline criterion tag (`# WRONG C-04`) AND an inline `Why:` explanation at the same field line. Prerequisites: C-24, C-25, C-26.

---

**C-35 — Dual Error-Format Recommended Coverage**

Source: V-01's diagnostic gap. V-01 passes C-31 (BAD PLAN carries all 7 criterion tags including C-05/C-06/C-07) but fails C-29 (correction table has essential-tier pairs only). The BAD PLAN example-format and the correction table lookup-format build their recommended-tier coverage independently — C-31 closes the BAD PLAN gap; C-29 closes the correction table gap; C-35 requires both to hold simultaneously so a model consulting either artifact finds wrong shapes for every recommended violation.

**Pass condition**: C-29 AND C-31 both pass — no partial credit. Prerequisites: C-29, C-31.

---

**Scoring:** 26 → 28 aspirational criteria, 130 → 140 pts, total **230 pts**. Golden threshold (>= 80) unchanged.
