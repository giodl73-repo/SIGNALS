Written to `simulations/quest/rubrics/quest-rubric-mock-ns-v14-2026-03-15.md`.

---

**Three new criteria extracted from Round 14:**

**C-38 — Hard-stop gate language** (depends on C-37)
V-02 and V-05 demonstrate that "DO NOT WRITE THE ROW until both phases pass" is categorically different from "Confirmation is a prerequisite." Prerequisite framing is an ordering constraint; hard-stop is an execution block. Required at all three locations: preamble gate definition, S-3 echo, A-1 echo.

**C-39 — Anti-bypass closing statement** (depends on C-36)
V-03's closing note — "An executor who recognizes a token without performing Phase 2 has not satisfied this protocol" — names the specific bypass being prevented (visual recognition without semantic read) and asserts it as a protocol failure. Structurally parallel to C-23 (failure-consequence at compute site) applied to the preamble gate.

**C-40 — Confirmation record output obligation** (depends on C-38)
V-05 upgrades Phase 2 from internal assertion to observable output: "Emit confirmation record." An assertion is unverifiable; a record in the output is auditable. The use-site pre-filled template (V-05's echo) is seeded as the v15 aspirational maximum.

**Scoring denominator: 29 → 32.** Formula: `aspirational_pass / 32 * 10`.
