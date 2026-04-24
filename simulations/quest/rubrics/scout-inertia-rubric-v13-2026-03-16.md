`scout-inertia-rubric-v13-2026-03-17.md` written. Ceiling 195 → 210.

---

**v12 → v13: three new criteria**

| # | Criterion | Source signal |
|---|-----------|---------------|
| A-29 | **Criterion ID in per-criterion authoring prompt label** | R12 V-03: `[C-01 COMMAND]: NAME...` through `[C-05 COMMAND]: NAME...`. Extends the criterion-ID-in-label traceability chain (A-23 = integrity rules, A-28 = checklist items) to the authoring-prompt layer. A-29 implies A-17. |
| A-30 | **COMMAND-register keyword in per-criterion prompt label** | R12 V-03 same evidence. The `COMMAND` keyword in the bracket label makes the directive nature of the prompt structurally explicit — parallel to how A-25 upgraded the bridge gate from a status check to an active command directive. A-30 implies A-29. |
| A-31 | **Named structural rule in FAIL-FIRST declaration body** | R12 V-03: `[FAIL-FIRST RULE]` structural label in FAIL-FIRST section body. A-10 requires the FAIL-FIRST section to exist; A-31 requires a named rule label within its body — structurally parallel to how A-16 added a named constraint rule inside the FM Inventory that A-14 required to exist. A-31 implies A-10. |

**Updated implication chain**: A-30 implies A-29 implies A-17 implies A-11. A-31 implies A-10. All prior chains unchanged.

**New category added**: `register` (A-30 — the only criterion in this category, capturing the COMMAND-register upgrade pattern at the prompt level).
