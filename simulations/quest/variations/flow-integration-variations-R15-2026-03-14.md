Written to `simulations/quest/rubrics/flow-integration-rubric-v15-variations-R15-2026-03-15.md`.

---

## flow-integration R15 — 5 Variations (v15 rubric, 247 pt ceiling)

### Summary

| Var | Axis | WHY Block Form | Concern Enum | Anchor Type | Predicted Score |
|-----|------|----------------|--------------|-------------|-----------------|
| V-01 | Single: C-37 stakes-only / consequence-form | Purpose + consequence anchor only | NO | Consequence-form | 212 (Q1 permissive) / 207 (-5 C-37 if enum required) |
| V-02 | Single: C-37 stakes-only / temporal form | Purpose + temporal anchor only | NO | Temporal | 212 (Q1 permissive) / 207 (-5 C-37 if enum required) |
| V-03 | Single: Phrasing register (conversational/imperative) | Consequence-form + concern enum, imperative voice | YES | Consequence-form | 212 — C-39 register neutrality |
| V-04 | Combined: Inertia framing + stakes-only / consequence-form | Discovery-failure inertia lead + consequence anchor | NO (discovery categories, not verification concerns) | Consequence-form | 207 most likely / 212 if any stakes anchor satisfies |
| V-05 | Combined: C-35 + C-37 + C-38 + C-39 ceiling | Consequence-form + concern enum (confirmed C-39 form) | YES | Consequence-form | 247/247 — full non-standard ceiling |

---

### Variation design rationale

**Q1 probe strategy (V-01 + V-02 as paired companions):** V-01 and V-02 probe the same question on different anchor surfaces. If both PASS → stakes anchor alone suffices; if both FAIL → concern enumeration is a C-37 requirement regardless of anchor form; if they diverge → form surface is a variable (unexpected under the current rubric where both forms are structurally equivalent by C-39).

**V-03** confirms C-39 is register-neutral. R14 V-03 tested declarative register with temporal anchor; R15 V-03 tests conversational/imperative register with consequence-form anchor — closing both axes simultaneously.

**V-04** is the richest stakes-only form: the inertia framing names discovery-failure categories (forgotten calls, untraced SDK calls, unmapped delegation chains) without naming verification concerns (auth, rate limits, retry, error propagation). It tests whether inertia context compensates for absent concern enumeration in the most favorable possible framing.

**V-05** is the ceiling confirmation run with C-39 as the fifth ceiling-contributing criterion. The non-standard five-row obligation table activates C-35/C-38; the consequence-form + concern-enumerated WHY block activates C-37/C-39; the YOU MUST NOT block activates C-27/C-30/C-31/C-34. If this scores 247/247, the v15 ceiling is confirmed reachable.
