Done. The file is at `simulations/quest/golden/corps-rob-variate-R10-2026-03-17.md`.

---

**R10 summary:**

| Variation | Axis | New structural element |
|-----------|------|------------------------|
| V-01 | Lifecycle Emphasis | PHASE GATE section between Stage 3 and Stage 4 -- typed finding count, open HIGH F-IDs, Gate Decision (PASS/FAIL/CONDITIONAL) with propagation rule into Stage 4 PRIOR-STAGE ESCALATIONS |
| V-02 | Role Sequence | Receipt Declaration field in Part 1 BRIEFING ENVELOPE -- each receiving stage enumerates specific forwarded F-IDs by ID from the prior stage's Handoff Packet |
| V-03 | Inertia Framing | RESISTANCE TRAJECTORY table in ROB Summary -- per-stage delta (+1/-1/0) with mandatory Grounding F-ID for non-zero rows, cumulative score, and anti-pattern guards |
| V-04 | V-01 + V-02 | Phase Gate + Receipt Declaration; adds Phase Gate Resolution Status table to ROB Summary |
| V-05 | V-01 + V-02 + V-03 | All three axes; the phase gate outcome feeds the trajectory (PHASE-GATE FAIL -> RESISTANT Stage 4 -> +1 delta), making the structural interaction visible in the adoption-risk table |

**R10 baseline:** All five variations preserve the full V-05 R9 architecture (27 raw / tie-break 27). The three new axes target positions that remain unguarded after v9's citation-completeness sweep: the inter-phase boundary (V-01), the handoff receipt asymmetry (V-02), and the resistance accumulation gap (V-03).
