**flow-ratelimit Variate R10** — written to `simulations/quest/golden/flow-ratelimit-variate-R10-2026-03-17.md`.

---

## Variation Map

| # | Axis | Hypothesis | C-27 | C-28 | C-29 | Predicted |
|---|------|-----------|------|------|------|-----------|
| **V-01** | Role sequence: Verdict gains Claim (d) | Elevating UX commitment to Verdict level makes tier-count changes trigger REVISED markers at gate boundaries, not only at terminal reconciliation | — | PASS | — | 118/120 |
| **V-02** | Output format: Schema B in Format Contract | Declaring Schema B as a named structural schema with its own STRUCTURAL REJECTION CLAUSE gives scan-time UX field detectability parallel to Schema A column enforcement | PASS | — | — | 118/120 |
| **V-03** | Lifecycle emphasis: six-item gate (a)–(f) | Naming (e) tier-count-against-burst-path-audit and (f) structure-compliance as separately enumerated blocking conditions closes two residual bypass paths R9's gate left open | — | — | PASS | 118/120 |
| **V-04** | Combined: role seq + output format | Claim (d) (reader-facing) + Schema B (scanner-facing) + Terminal Reconciler check (d) form a two-layer closed loop; neither alone closes both gaps | PASS | PASS | — | 120/120 |
| **V-05** | Combined: all three axes | Three mechanisms, three closed loops: Verdict commits tier count (C-28), Format Contract enforces structure (C-27), gate verifies burst-path tier count and structure compliance as separate named conditions (C-29), Reconciler audits both independently at close | PASS | PASS | PASS | 120/120 |

---

## Key design decisions for R10

**C-27 placement:** Schema B lives in the Format Contract (Role 1 / Format Contract section), not in Role 6's template instructions. This is the structural authority difference — a Format Contract declaration makes the schema enforceable by the Reconciler's independent check (d), separate from the gate audit in check (b).

**C-28 trigger rule:** Claim (d) specifies the REVISED marker must be inserted "at the gate boundary of the role where the discovery occurred — not deferred to terminal reconciliation." This is the specific C-28 mechanism: mid-analysis tier discovery triggers a Verdict-level marker at the gate, not only at document close.

**C-29 separation:** V-03 and V-05 use the phrase "Each condition is a separately named blocking gate condition. Combining any two into a compound condition does not satisfy both." Items (e) and (f) each get their own checkbox and prose definition. Item (e) explicitly names "Role 4 burst path audit count" as the verification target rather than the two-tier minimum.
