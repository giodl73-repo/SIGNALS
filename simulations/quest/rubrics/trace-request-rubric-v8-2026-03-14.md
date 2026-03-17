`trace-request-rubric-v8-2026-03-15.md` written. Here is the extraction summary:

---

**Two new criteria from R8 excellence signals:**

| New criterion | R8 excellence signal | What is testable |
|---|---|---|
| **C-24** Batch-catalog cross-check gate table-verifiable | ES-1 (V-03/V-05): K integer derivable by counting "X" cells in a visible EC# × TRow# table | Is the backing table present? Does counting "X" cells yield exactly K? Does column count equal threat catalog row count, and row count equal edge-case section row count? |
| **C-25** Per-boundary scope enumeration at auth re-walk | ES-2 (V-04/V-05): Every boundary has a named Required Scope/Role; Gap? column marks invoked-vs-required mismatches | Is a scope enumeration table present before re-walk findings? Does it carry all four columns (Scope/Role Invoked, Required Scope/Role, Verified?, Gap?)? Are blank Required Scope/Role cells explained? |

**Scale:** 170 → **180** (aspirational tier: 16 → 18 criteria, 80 → 90 pts). Golden threshold stays at >= 80.

---

**Signal not promoted:** ES-3 scope-gap Rem# citation — gaps from Step 8a Gap? column propagate into the Remediation Register with exact scope string parameters. Speculative; requires a confirmed three-way cross-link (Step 8a → Step 11 → Step 7/9). Strong **C-26 candidate** once C-25 produces round evidence.

---

**Why these don't overlap their parents:**

- **C-24 vs C-22:** C-22 tests format (three non-approximate integers before the register). C-24 tests verifiability (integers cell-derivable from a visible table). C-22 PASS + no backing table = C-24 FAIL.
- **C-25 vs C-11:** C-11 tests discovery (new gap named or highest-risk boundaries certified). C-25 tests exhaustiveness surface (structured per-boundary table precedes findings). C-11 PASS + narrative audit without table = C-25 FAIL.

**New dependency edges:**
- C-24 depends on C-22
- C-25 depends on C-11 (re-walk exists) and C-04 (auth check per boundary, source for Invoked column); both parents required
