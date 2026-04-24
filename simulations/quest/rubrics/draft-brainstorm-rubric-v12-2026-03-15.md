Written to `simulations/quest/rubrics/draft-brainstorm-rubric-v12-2026-03-16.md` (1,121 lines, +74 from v11's 1,047).

---

## What changed from v11

**Two new criteria extracted from R11 excellence signals:**

### C-35 — Phase-0 Inertia Prefacing *(r12 aspirational, 2.5 pts)*

Sharpens C-14. Signal: V-03/V-05 R11 place Do Nothing in a dedicated **Phase 0** block *before* Phase 1 begins. C-14 requires a framing paragraph before the pool; C-35 additionally requires the inertia baseline to occupy its own numbered phase (Phase 0) that **closes before Phase 1 opens** — a hard architectural boundary, not just paragraph ordering within a shared phase.

- V-03/V-05 R11 PASS: "Phase 0 Do Nothing entry with Pitch + Rationale" precedes "Phase 1a" generation paragraph
- V-01 R11 FAIL: inertia framing integrated into Stage 1a (C-14 PASS, C-35 FAIL)
- V-02/V-04 R11 FAIL: "Phase 1a" / "Step 1" — inertia embedded in Phase 1, no Phase 0

### C-36 — Net-Count Volume Specification *(r12 aspirational, 2.5 pts)*

Sharpens C-01. Signal: V-03/V-05 R11 state volume as **"19-39 additional…total 20-40"** — naming both the net-new count and the total. C-01 requires the total (20-40); C-36 additionally requires the net-new count, making Do Nothing's role in the total explicit and preventing the model from generating 20+ new ideas plus Do Nothing and overshooting the range.

- V-03/V-05 R11 PASS: "19-39 additional…total 20-40"
- V-01/V-02/V-04 R11 FAIL: "Generate 20-40 candidates" — total only

**Lineage additions:**
```
C-01  volume: 20-40 total?
  C-36  net-new count alongside total? ("19-39 additional...total 20-40")

C-14  inertia-first framing paragraph before pool?
  C-35  Do Nothing in Phase 0 before Phase 1 (hard phase boundary)?
```

**Max raised: 160 → 165.**

**R11 projected scores under v12:**
- V-03 R11: **165** — first to achieve 165 (C-35 PASS + C-36 PASS, all others pass)
- V-05 R11: **160** — C-15 FAIL (−5) cancels C-35+C-36 gain (+5); net 165−5=160
- V-01 R11: **160** — C-35 FAIL, C-36 FAIL; full pass on all other 34 criteria
- V-04 R11: **160** — same as V-01
- V-02 R11: **155** — C-15 FAIL (−5), C-35 FAIL, C-36 FAIL; 165−10=155
