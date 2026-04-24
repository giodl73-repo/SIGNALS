Written to `simulations/quest/golden/prove-topic-variate-R5-2026-03-15.md`.

---

## Round 5 — Five Variations

### Single-axis variations

**V-01 — Lifecycle emphasis (C-19 target)**
Rewrites CAMPAIGN OPEN as a `PROTOCOL DECLARATION` with named `NULL-CE INVARIANT A` and `NULL-CE INVARIANT B` fields. Language is explicitly pre-commitment: *"committed here — applies regardless of what is found"*, *"pre-registered appointment — not a synthesis decision"*. Each stage's null-result note references the invariant by letter and says "pre-committed protocol, not a new decision."

**V-02 — Output format (C-18 target)**
Synthesis uses an `ATOMIC DUAL-LOCK ACTIVATION` block with a bordered entry/exit. One trigger condition (`all three null`). Both LOCK A (CE-score) and LOCK B (escalation) are outputs of the same block entry. A `co_activation_confirmed` field in the handoff must equal `dual_lock_fired` — making partial activation visible as a format error, not just a semantic miss.

**V-03 — Phrasing register (C-19 propagation)**
Invariant language propagates through every stage null-result note: *"running tally: S2 null"*, *"pre-registered session obligations, not conditional judgments"*, *"one stage remaining — if Stage 4 null, both pre-committed invariants execute"*. The model carries the protocol forward actively at each stage rather than rediscovering it at synthesis.

### Combined variations

**V-04 — Protocol Manifest + Atomic Dual-Lock (C-19 + C-18 direct)**
CAMPAIGN OPEN has a three-invariant manifest (A: reviewer, B: cap formula, C: co-activation rule). STAGE 5 uses the ATOMIC DUAL-LOCK block. The GATE S checklist includes all six fields — including both invariants and the co-activation rule — before Stage 1 can open. This is the tightest direct target for the two new criteria.

**V-05 — Full excellence compound (R4 V-05 base + C-18 + C-19)**
Takes R4's highest-scoring variation and applies two targeted upgrades: (1) CAMPAIGN OPEN → PROTOCOL MANIFEST with invariant language, (2) the LOCK 1/LOCK 2 sequential structure → ATOMIC DUAL-LOCK ACTIVATION block. All R4 mechanisms preserved: evidence ledger, prototype cap, 4-checkbox GATE S, per-artifact full paths, gate_s_cleared in frontmatter. Should satisfy C-01 through C-19 simultaneously.

---

**Key design distinction R4 → R5:**

| Gap | R4 behavior | R5 fix |
|-----|-------------|--------|
| C-19 | Fields filled as registration slots | Declared as named session invariants with "pre-committed / cannot be modified" language |
| C-18 | LOCK 1 / LOCK 2 sequential blocks — each has its own `if all null:` condition | Single ATOMIC DUAL-LOCK block — one entry condition, both outputs required, `co_activation_confirmed` field enforces integrity |
