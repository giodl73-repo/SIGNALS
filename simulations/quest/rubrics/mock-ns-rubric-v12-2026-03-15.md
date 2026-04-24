v11 untouched (0 references), v12 clean (18 references across changelog, criteria, escalation chains, failure modes).

---

**v12 written** to `simulations/quest/rubrics/quest-rubric-mock-ns-v12-2026-03-15.md`.

**Two new criteria extracted from Round 12:**

**C-34 — Explicit lookup obligation** (depends on C-33)
V-03's advancement: the preamble includes an explicit directive obligating the executor to look up any bracket token in the resolution table before processing the containing row, and prohibits decoding from memory. Converts O(1) lookup *availability* (C-33) into a mandatory *protocol*. Gap closed: an executor who has seen `[A-1:FC]` before may bypass the table via context memory, forfeiting the orientation guarantee.

**C-35 — Use-site row navigation labels** (depends on C-34)
V-03's advancement: bracket-token rows at S-3 and A-1 carry inline parentheticals like `(P-0 table, row 1)` / `(P-0 table, row 2)` pointing to the exact preamble table row that resolves each token. Gap closed: a lookup obligation (C-34 pass) still requires a table scan to find the governing row; a row-specific label at the use site reduces that to a direct jump. Both sites must carry labels.

**Scoring**: aspirational denominator 25 → 27 (`pass/27 * 10`).
