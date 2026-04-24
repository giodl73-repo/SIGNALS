Written to `simulations/quest/rubrics/quest-rubric-mock-ns-v13-2026-03-15.md`.

**What changed from v12:**

**C-36 — Two-phase confirmation gate** (depends on C-35)
The C-34 lookup obligation is a single *locate* step. V-01 splits it into two phases: (1) locate the preamble table row by token name, (2) read Step + Row type cells and assert the resolution matches the processing context before writing the row. A locate-only obligation is satisfied by visual token recognition; the confirm phase requires a semantic cell-read that is externally observable and assertable. Preamble must state both phases explicitly, with confirmation framed as a prerequisite to writing the row.

**C-37 — Confirmation echo at use site** (depends on C-36)
The C-36 preamble gate defines the protocol once. V-01 adds a use-site trigger — "CONFIRMATION REQUIRED before writing this row" — prefixed before the C-35 navigation label at both S-3 and A-1. Without the echo, the preamble protocol is active only at preamble-reading time; the trigger re-activates it at the exact point of use, eliminating the recall burden. Both sites must carry the trigger for a PASS; positioning must precede the navigation label and row content.

**Scoring**: aspirational denominator 27 → 29. Formula: `aspirational_pass / 29 * 10`.

**Escalation chain**: C-37 lands at both compute site and consumption site columns, mirroring C-35's bilateral placement — the echo is required at both bracket-token rows regardless of which site they inhabit.
