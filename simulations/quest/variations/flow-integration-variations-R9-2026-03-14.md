Written to `simulations/quest/rubrics/flow-integration-rubric-v9-variations-R9-2026-03-15.md`.

---

## R9 Variations — flow-integration

| V | Axis | Open Question | Non-Standard Terms | C-26 Form | C-27 Form | Frame |
|---|------|---------------|--------------------|-----------|-----------|-------|
| V-01 | C-26 instruction minimum | Q1 | No | Cross-reference mapping table (no ARE) | N/A | Stages |
| V-02 | C-27 prohibition scope | Q2 | Yes: shadow-call / taken-for-granted / fog-system / relay-chain | Explicit ARE | Per-term inline in obligation table | Stages |
| V-03 | Outer frame vocabulary | C-28 frame-agnosticism | No | Explicit ARE | N/A | **Phases** |
| V-04 | C-26 + C-27 joint | Q1 + Q2 | Yes: anchor-call / rubber-stamped / ghost-system / proxy-chain | Cross-reference table | Per-term inline | **Sections** |
| V-05 | Conversational register + role sequence split | Register/sequence agnosticism | No | Explicit ARE (conversational phrasing) | N/A | Stages |

---

### What each variation is testing

**V-01 (Q1 probe)** — C-26 minimum. The obligation terms → column header mapping is expressed as a two-column cross-reference table with an explicit mismatch-detection statement, not as "the headers ARE the Obligation Term values." If the ARE keyword is required for C-26, this scores 187/192 (−5). If any unambiguous schema-aligned instruction suffices, 192/192.

**V-02 (Q2 probe)** — C-27 scope. Non-standard terms with per-row prohibition: the obligation table gains a `YOU MUST NOT substitute` column, each row naming exactly one forbidden canonical token. R8 V-05 used a single comprehensive block covering all four. V-02 distributes one prohibition per row. If a single block is required, 187/192 (−5). If per-term distribution satisfies, 192/192.

**V-03 (frame-agnosticism)** — C-28 is outer-frame-agnostic. Phase vocabulary substitutes identically: `*(no phase number — appended after Phase 3, the last numbered phase)*` + "does not appear between any two numbered phases." No open question to settle; this is a confirming variation. Predicted 192/192.

**V-04 (Q1+Q2 joint)** — Both open questions in one variation, using a third non-standard vocabulary and section frame. Worst case 182/192 (−5/−5 if both open questions resolve negatively, −5 C-27). Best case 192/192.

**V-05 (register + sequence)** — Conversational second-person imperative throughout. Role sequence split: expert persona brief at top → Stage 1 opens → obligation table inside Stage 1 (before gate) → inventory table → gate statement. The C-16/C-24 requirements are "before the inventory gate" — obligation table is co-located inside Stage 1 but still precedes the gate, satisfying both. If conversational phrasing or the role-sequence split creates a structural miss, this catches it. Predicted 192/192.
