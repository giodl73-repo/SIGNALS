Written to `simulations/quest/golden/listen-support-variate-R2-2026-03-15.md`.

---

## listen-support — Round 2 Variations

**Baseline:** V-05 R1 (composite 75.5). Three universal fixes applied to all variations.

### Fixed in all R2 variations

| Fix | Criterion |
|-----|-----------|
| PERFORMANCE MODE DECLARATION with first-person mandate + third-person prohibition | C-03 → PASS |
| Gap section format requires `Tickets: T-NN, T-NN` | C-04 → PASS |
| Ticket count gate now `>= 6 and <= 12` | C-06 → PASS |

### New axes explored (R1 deferred phrasing register and inertia framing)

---

**V-01 — Phrasing register (character-embodiment)**
PERFORMANCE MODE rewritten as identity-embodiment rather than a prohibition list. Each persona gets a backstory and emotional state ("You are the on-call engineer. You knew the old system's failure modes by heart..."). The hypothesis: identity framing suppresses third-person drift more reliably than rule-avoidance because it changes the generation mode, not just adds a constraint.

---

**V-02 — Inertia framing (status-quo competitor)**
Adds STEP 1B STATUS QUO ANALYSIS before ticket generation: name what users are replacing, the habit they carry in, the primary migration friction. Phase 1 must include at least one migration-confusion ticket. Gap analysis gains a migration friction sub-section. The hypothesis: naming the prior approach generates a distinct failure class ("I expected it to work like the old way") that generic prompts never surface.

---

**V-03 — Theme-first generation**
Declares 2-3 named themes with their underlying product/doc failure before any ticket is generated. Tickets are organized by theme rather than phase. The hypothesis: theme-first makes C-09 (ticket clustering) satisfied by construction rather than retrospective grouping; clusters are coherent because they were declared as design.

---

**V-04 — Combined: character-embodiment + inertia framing**
V-01 × V-02. Migration history feeds persona backstory: each character knows what they migrated from, which grounds their confusion in a real prior habit. The hypothesis: the two axes reinforce each other — identity framing makes migration-rooted frustration vivid rather than generic.

---

**V-05 — Full synthesis (golden candidate)**
V-05-R1 structure (phase distribution target + ROLE-PHASE CROSS-MATRIX) + all R2 axes + STEP 7B resolution paths for high-volume/P0-P1 tickets (C-10). Five axes address five distinct generation-time failure modes without structural conflict. Dual-pass verification explicitly checks C-12 (role-phase compound coverage) and C-13 (phase-calibrated severity).

**Expected R2 composite: ~88** — all five essential pass, all three recommended pass, C-09/C-10/C-11/C-12/C-13 all targeted.
