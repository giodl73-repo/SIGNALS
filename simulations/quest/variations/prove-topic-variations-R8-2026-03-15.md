Written to `simulations/quest/golden/prove-topic-variate-R8-2026-03-15.md`.

---

## prove-topic — Round 8 Variations

**Anchor**: R7 V-05 (144/144 under v7). Round 8 targets three patterns in R7 V-05 that go beyond any current criterion.

---

### New axes identified from R7 V-05 excellence signals

| Axis | What it addresses | Why it's not covered by v7 |
|------|-------------------|---------------------------|
| **Handoff derivation annotations** | Every handoff field carries a `[derived from: X]` label — not just `incumbent_defense_closed` | C-23 requires one independent boolean; it doesn't require uniform derivation labeling on all fields |
| **Pre-committed handoff schema** | Full field contract (names + derivation sources) locked at CAMPAIGN OPEN as a session invariant | C-19 pre-commits the null-CE protocol; it doesn't require the handoff field list to be locked before Stage 0 |
| **Independence path chain** | `incumbent_defense_closed` carries a structured negative assertion: `NOT from dual_lock_fired; NOT from co_activation_confirmed` | C-23 requires structural independence; it doesn't require an explicit negative derivation chain as a distinct field |

---

### Variations

| ID | Axis | Type | R8 target |
|----|------|------|-----------|
| **V-01** | Handoff derivation annotations | Single-axis | All handoff fields labeled with derivation source; unlabeled field = format error |
| **V-02** | Pre-committed handoff schema | Single-axis | 8-field schema declared at CAMPAIGN OPEN; synthesis constrained to exact contract |
| **V-03** | Independence path chain | Single-axis | `positive_derivation:` + `independence_chain: NOT from...` on `incumbent_defense_closed` |
| **V-04** | V-01 + V-02 | Combination | Pre-committed schema with derivation sources; synthesis compliance check verifies labels against pre-declared contract |
| **V-05** | Full R7 V-05 stack + all R8 axes | Compound | Role sequence + table format + inertia framing + all three R8 axes; 9-field schema; independence path chain in both Stage 4 and Handoff |

**Preliminary anchor: V-05.** All v7 criteria satisfied; all three R8 targets present. The three axes are composable — pre-committing the schema with derivation sources (V-02) does not conflict with per-field labeling at synthesis (V-01); the independence path chain (V-03) is consistent with the pre-committed derivation source for `incumbent_defense_closed`.
