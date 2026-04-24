Written to `simulations/quest/golden/topic-achievements-variate-R5-2026-03-17.md`.

---

## Variate R5 — topic-achievements

**Variation axes selected:**

| Axis | Targets | Used In |
|------|---------|---------|
| Phrasing register (preservation directive as numbered session invariant) | C-18 | V-01, V-04, V-05 |
| Output format (preservation directive as block-local header annotation) | C-18 | V-02, V-04 |
| Lifecycle emphasis (gate architecture: each gate defines required output, not just a count) | C-19 | V-03, V-04, V-05 |

---

### Summary of what each variation tests

**V-01 — Phrasing register: preservation as session invariant (C-18)**
Invariant 4 appears in the prompt preamble before any steps: "The Falsified Achievement Contract block below is pre-printed compliance text. Do not rewrite, rephrase, or restructure that block." The block carries only the PRE-PRINTED label — no local directive. This isolates instruction-body placement as the single structural anchor for C-18. No gate architecture (C-19 not targeted).

**V-02 — Output format: preservation directive in block header (C-18)**
The first line inside the pre-printed block reads: "THIS BLOCK IS PRE-PRINTED. Do not rewrite, rephrase, or restructure any text in this block." No session invariant pointing to it — isolating block-local placement. The floor lives as Rule 3 inside the same block (C-17 via structural independence from conditional labels). No gate architecture.

**V-03 — Lifecycle emphasis: gate architecture with defined output per gate (C-19)**
Every gate specifies a required output template. The key new behavior: CLASSIFY GATE requires all category lines to appear explicitly — `Exploration: [list]`, `Depth: [n] artifacts`, etc. — before Phase 3 may begin. A count alone does not clear the gate. This is the C-19 distinction: the gate defines what completion looks like, and that definition forces visible intermediate output. No pre-printed block (C-16/C-18 not targeted).

**V-04 — Combination: dual preservation directive + CLASSIFY GATE with full output (C-16 + C-18 + C-19)**
Two independent C-18 anchors: session invariant 4 (governing from above, before any phase) and the block-local first line ("THIS BLOCK IS PRE-PRINTED. Do not rewrite..."). Neither can be missed without the other still firing. CLASSIFY GATE requires the full per-category record.

**V-05 — Golden synthesis: session invariant + pre-printed skeleton + full gate architecture (C-16 + C-17 + C-18 + C-19)**
Extends R4 V-05 with both new criteria cleanly. C-18: Invariant D in the preamble names the pre-printed template explicitly and states the preservation rule. C-19: CLASSIFY GATE now requires the full per-category record — the R4 summary count (`[n] of 7 categories`) remains as the closing summary line but is preceded by all seven explicit category lines. SCAN GATE, STATE GATE, and WRITE GATE each define their required output format. The Falsified LOCKED cell pre-prints the compliance text verbatim (C-16 + C-17 via the floor sentence in that cell).

---

**Key C-18 diagnostic**: V-01 and V-02 test whether placement matters — invariant body vs block-local. If one passes and the other fails, it tells you whether "stated in the instruction body" means the governing section or just anywhere in the prompt.

**Key C-19 diagnostic**: V-03 tests whether specifying the full required output format (vs just a count) changes gate compliance. If R4 V-03 passed C-19 with its count-only gate and R5 V-03 also passes, the distinction collapses. If only R5 V-03 passes, the per-category record is what C-19 actually requires.
