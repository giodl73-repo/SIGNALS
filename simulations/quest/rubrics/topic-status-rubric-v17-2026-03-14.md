`topic-status-rubric-v17-2026-03-15.md` written. Here's the summary of what was extracted and formalized:

---

## v17 changes — Structural Tier 16 (+5 pts, max 295 → 300)

| ID | Name | Isolated by | Prerequisite | Points |
|----|------|-------------|--------------|--------|
| C-49 | PHASE 1 adversary defeat STOP predicate | V-01 vs V-04 | C-48 (conditional) | 5 |

**C-49** operationalizes the C-48 DEFEAT CONDITION at the execution gate. When C-48 is present (three-phase adversary chain), the STOP CONDITION must carry a predicate checking the PHASE 1 defeat condition — that DISK_SIGNALS was populated from a live glob result with zero-result case handled. When C-48 is absent, C-49 is **vacuously satisfied**: no PHASE 1 adversary is declared, so no STOP predicate is required at that position.

**Structural novelty:** C-49 is the first criterion in this rubric with vacuous-PASS behavior. All prior criteria (tiers 2–15) have hard implications — failing the prerequisite cascades to failing the dependent criterion. C-49 does not: failing C-48 does not cascade to failing C-49. Consequently, no hard implication `C-49 => C-48` is added to the implication map.

**Projected R18 scores under v17:** V-01 → 300; V-02 → 295 (C-47 FAIL); V-03 → 295 (C-48 FAIL, C-49 vacuous PASS, clean redesign confirmed); V-04 → 295 (C-49 FAIL); V-05 → 290 (C-47+C-48 FAIL, C-49 vacuous PASS). Three variants tie at 295 — each isolating a different criterion from a different ablation axis. No R18 variant fails all three simultaneously: the gap that defines Round 19.
