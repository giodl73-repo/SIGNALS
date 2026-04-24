Written to `simulations/quest/golden/trace-contract-variate-R5-2026-03-15.md`.

---

## Round 5 Variation Map

| Variation | Axis | Primary Target |
|-----------|------|----------------|
| V-01 | lifecycle-emphasis | C-19, C-18, C-13 |
| V-02 | output-format | C-16, C-15, C-11 |
| V-03 | phrasing-register | C-06, C-14 |
| V-04 | lifecycle + output-format | C-19, C-16, C-17 |
| V-05 | all five axes | C-01 through C-19 |

---

### Design decisions

**V-01 — The C-19 fix is structural, not content.** R4 V-05 already had a complete token contract (satisfying C-18), but it appeared *inside* a phase block. The single change in V-01: a named `## Behavioral Contract` section written before any `### ROLE:` heading. The model reads placement, non-substitutability, and verification mechanism before Phase 1 instructions begin.

**V-02 — Tier-stratified templates eliminate conditional field logic.** R4 V-02 used a unified template with `recommended-action` marked "required if breaking." That conditional language is exactly what C-16 rejects. Three separate templates — breaking (6 slots), degraded (5 slots), cosmetic (4 slots) — each have only unconditionally required fields. A missing slot is always a visible gap, never an optional one.

**V-03 — Frame before instruction.** Rather than adding a `connector-impact` slot requirement (structural), V-03 sets the integration lens in a preamble framing section. The hypothesis is that a reader who already has the "I'm writing for Automate flow builders" frame will naturally include integration-impact in every finding without needing a labeled slot to force it.

**V-04 — Three mechanisms at three lifecycle points.** Preamble governs pre-execution (C-19), stratified templates govern write-time (C-16), rationale sentence in the breaking template governs resolution depth (C-17). No overlap, no interference.

**V-05 — Additive full synthesis.** All five axes combined, with inertia framing added at each phase boundary naming the status-quo alternative. Pattern detection and per-finding connector-impact complete the aspirational tier.
