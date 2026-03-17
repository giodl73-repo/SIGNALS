`simulations/quest/golden/scout-size-variate-R3-2026-03-16.md` written.

---

## scout-size — Prompt Variations R3

Five complete variations targeting the v3 rubric (14 criteria). The two new criteria drive the design:

- **C-13** (explicit tier destination): V-01 R2 near-miss — template had `[LEVEL]` in the rule but not enforced in the slot. R3 makes `[LEVEL]` fill explicit and non-negotiable in every variation.
- **C-14** (falsifiable conditions): R2 had anti-pattern *language* but no structural *slot*. R3 adds a mandatory `Settle by:` / `Verify by:` field in every variation.

### Three single-axis bets

| ID | Axis | C-13 mechanism | C-14 mechanism |
|----|------|----------------|----------------|
| **V-01** | Lifecycle emphasis — sensitivity as two phases (name, then verify) | Phase 1 template requires `[LEVEL]` fill + "direction without destination fails" | Phase 2 "Settle by:" sub-field is mandatory; anti-pattern examples show failing/passing |
| **V-02** | Output format — tier-transition table with Destination Tier + Verify-by columns | Dedicated "Destination Tier" cell — can't be implied, can't be blank | Dedicated "Verify by" cell — "further investigation" explicitly fails |
| **V-03** | Phrasing register — conversational/Socratic, workaround-as-protagonist | `[LEVEL]` required inside the question; "naming the destination fails" embedded | "Colleague test": *could a teammate go investigate this? What would they do?* |

### Two combinations

| ID | Axes | Bet |
|----|------|-----|
| **V-04** | Format + lifecycle (table rows + Phase 2 sub-field) | Dual structural handles: Destination Tier column prevents C-13 omission; Phase 2 prose field prevents C-14 generic filler |
| **V-05** | Full integration | All axes + dedicated anti-pattern tables for C-13 (4 failing forms) and C-14 (4 failing forms + replacements) + 14-criterion self-check |
