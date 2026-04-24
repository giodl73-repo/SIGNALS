Done. `simulations/quest/rubrics/quest-rubric-mock-ns-v15-2026-03-15.md` written.

---

**Three new criteria extracted from Round 15:**

**C-41 — Use-site pre-filled confirmation record template** (depends on C-40)
The aspirational maximum seeded in v14's C-40. Both V-03 and V-05 pass. Each bracket-token row at S-3 and A-1 carries a pre-filled template with token name, step, and row type already populated for that specific row — the executor fills in only the match result. Reduces compliance cost from open-form record construction to fill-in-the-blank.

**C-42 — Emit obligation woven into the hard-stop gate condition** (depends on C-40, C-38)
Only V-05 passes. V-03 lists "Emit confirmation record" inside Phase 2's definition but its gate text ends at "until both phases pass." V-05 names the record as an explicit gate precondition: "until both phases pass **and the record is emitted**." The gate now blocks on record existence, not merely on nominal phase completion. Required at all three locations.

**C-43 — Dual-naming + protocol-failure severity framing** (depends on C-39)
Only V-05 passes. V-02 names the bypass once (protocol-based); V-04 names it once (action-based). V-05 uses both — "without reading the Step and Row type cells" AND "without performing Phase 2" — closing the recognition gap where an executor might not identify their action under one framing. Concludes with "Locate-only is a protocol failure" (categorical-failure framing) rather than "has not satisfied this protocol" (gap-to-close framing). Both conditions required for PASS; single-condition scores PARTIAL.

**Scoring denominator: 32 → 35.** Formula: `aspirational_pass / 35 * 10`.
