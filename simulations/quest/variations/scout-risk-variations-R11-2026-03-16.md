**Scout-Risk R11 variations written** to `simulations/quest/golden/scout-risk-variate-R11-2026-03-17.md`.

---

## Summary

**R11 baseline state**: R10 V-03 scored 136/136 against v10 rubric. Against v11, C-32 and C-33 are already satisfied by the existing prompt structure — only **C-34 fails** (AMEND section lacks a structured header naming active and suppressed dimensions). Target: 142/142.

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | AMEND framing (prose format) | C-34 can score independently of table format — structured AMEND Scope Declaration in prose satisfies the criterion |
| **V-02** | Output format (typed-column tables + AMEND header) | R10 V-03 baseline + structured AMEND declaration block = 142/142; C-32/C-33 confirmed by "Trigger Condition" column + vocabulary-constrained Dimension column |
| **V-03** | Lifecycle emphasis (AMEND as Phase 0a) | Positioning AMEND processing as a first-class phase before the taxonomy block makes the scope declaration the literal first output — stronger structural signal than a trailing section |
| **V-04** | Combination: output format + vocabulary-constrained AMEND fields | Mirrors the C-33 Dimension column rule onto the AMEND header itself — Active/Suppressed Dimensions field values constrained to the exact closed {Technical, Market, Compliance, Dependency, Timeline} set |
| **V-05** | Combination: all axes + phrasing register | Phase 0a + vocabulary-constrained AMEND header + tight imperative construction throughout — highest-confidence prompt for C-34 under both normal and AMEND operation |

### Key structural additions for C-34

All table-format variants (V-02 through V-05) add an **AMEND Scope Declaration** block that:
1. Is a named structural element (not trailing prose)
2. Has two explicitly labeled fields: `Active Dimensions` and `Suppressed Dimensions`
3. Requires every member of `{Technical, Market, Compliance, Dependency, Timeline}` to appear in exactly one field — no omissions, no duplicates
4. Makes AMEND compliance column-verifiable: a reviewer checks the header, not the full register

V-03/V-05 escalate further by making this Phase 0a — the literal first output of the register, before any table content.
