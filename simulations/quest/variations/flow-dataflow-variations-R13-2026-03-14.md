Saved to `simulations/quest/rubrics/flow-dataflow-rubric-v13-2026-03-15.md`.

---

# flow-dataflow — Round 13 Variations

## R12 gap summary

**C-42 not satisfied in R12** — Parts A/B (C-37) and Phase Gate 2 SC cites (C-41) were each present but their joint property was never declared. No section stated: "every structural failure mode has a pre-declared navigation path to its governing SC." C-42 requires that closed-chain declaration to be explicit in the REGISTER DECLARATION header.

**C-43 not satisfied in R12** — SC-12 had governed role (C-39) and position distance (C-40) in its body, but the third attribute — "Phase Gate 2 item for this requirement must cite [SC-12] by number" — appeared only in the Phase Gate 2 checklist item. C-43 requires all three co-present in a single SC block. Without the self-declaration in SC-12's body, a reader of SC-12 alone cannot determine what Phase Gate 2 is required to cite.

## Variation axes

| Variation | Axis | Role sequence | Skip-level | Register |
|-----------|------|--------------|------------|----------|
| V-01 | Role sequence | Commerce → Finance → Operations | Operations cites [A-04] (Commerce, pos 1) | Tabular |
| V-02 | Output format | Finance → Commerce → Operations | Operations cites [A-04] (Finance, pos 1) | Conversational prose + C-33 |
| V-03 | Lifecycle emphasis | Operations → Finance → Commerce | Commerce cites [A-04] (Operations, pos 1) | Tabular; 4 stages/3 boundaries per role |
| V-04 | Role seq + inertia | Finance → Operations → Commerce | Commerce cites [A-04] (Finance, pos 1) | Tabular; Finance owns baseline |
| V-05 | Conversational imperative + role seq | Operations → Commerce → Finance | Finance cites [A-04] (Operations, pos 1) | Tabular; imperative instruction voice |

## C-42 and C-43 implementation pattern (all variations)

**C-43 — SC-12 body now contains all three attributes in a single block:**
```
SC-12 — Skip-level citation in [Role3]: [Role3]'s Citing: line must include [A-04]
— [Role1]'s boundary checks, produced two positions prior in the [R1 → R2 → R3]
sequence. [Role2] is [Role3]'s immediate predecessor; a Citing: line that names only
[Role2]'s tokens without [A-04] fails SC-12. The position distance is two: [Role3]
occupies position 3, [Role1] occupies position 1. A Phase Gate 2 verification item
for this requirement must cite [SC-12] by its numbered identifier in the item text
itself, so that an evaluator navigating from a failed checklist item reaches this
constraint declaration directly.
```

**C-42 — REGISTER DECLARATION header explicitly declares the closed chain:**
```
Closed verification chain: Every failed Phase Gate item in this output cites its
governing structural constraint by number in the item text. Part A governs all C-34
failures. Part B governs all C-35 failures. SC-12 governs all skip-level citation
failures, and its Phase Gate 2 item cites [SC-12] by number (see SC-12 body).
Together, Parts A/B and the SC-12 Phase Gate 2 item form a complete closed chain:
every structural failure mode has a pre-declared navigation path to its governing SC.
```

**C-41 — Phase Gate 2 item format (identical across all variations):**
```
- [ ] [SC-12]: [Role3]'s Citing: line must include [A-04] ([Role1]'s boundary checks,
  two positions prior in [R1 → R2 → R3]). A Citing: line with only [Role2]'s tokens
  without [A-04] fails SC-12. Mark ✗ if [A-04] absent.
```

## Scenario summary

| Variation | Domain | Pipeline |
|-----------|--------|----------|
| V-01 | Pharmaceutical supply-chain | Vendor catalog → hospital dispensary inventory |
| V-02 | E-commerce returns | Customer return authorization → GL ledger adjustment |
| V-03 | Manufacturing cost allocation | Production run → cost ledger → Commerce pricing |
| V-04 | Insurance claims | Claim submission → adjudication → payment disbursement |
| V-05 | Retail DTC revenue | Order placement → carrier → financial close |
