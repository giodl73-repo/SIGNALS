Written to `simulations/quest/golden/corps-scan-variate-R2-2026-03-17.md`.

---

## corps-scan Variate R2 — 5 Variations

All five variations target the three new v2 criteria simultaneously. Here's what each does:

---

### V-01 — Output Format: Typed Inventory Table
**Single axis.** Requires the inventory as a typed 3-column table (`Signal | Path or Identifier | Pivot Relevance`) before any YAML. A sentinel line `--- [SIGNAL INVENTORY COMPLETE] ---` gates YAML. The table columns force each signal to be a citable row identifier, enabling C-12 naturally. Cleaner than R1's V-01 (YAML-first) — inventory now leads.

### V-02 — Lifecycle Emphasis: Two-Gate Protocol
**Single axis.** Collapses R1's four phases to exactly two hard gates. GATE-1 requires the typed table with a Signal ID column scheme (S-01, S-02...) and ends with `YAML authoring is now AUTHORIZED`. GATE-2 requires a Signal ID citation before drafting begins. Tighter than V-03 R1's four-phase system, which allowed conversational softening.

### V-03 — Phrasing Register: Precondition/Postcondition Spec
**Single axis.** Frames every phase as `PRECONDITION → OPERATION → POSTCONDITION`. The typed table is the postcondition of Phase 1 and the precondition of Phase 2 — making C-13 a contract invariant rather than advice. The Phase 2 postcondition has a mandatory `Identifier` field, making C-12 a postcondition violation if missing.

### V-04 — Table IS the Gate (Output Format + Lifecycle)
**Combination.** The Signal Inventory Table has a mandatory terminal row: `| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`. C-11 and C-13 are structurally inseparable — you cannot write the gate without first writing a typed table. Any YAML appearing before the GATE row is explicitly an ordering error.

### V-05 — Role Sequence + Typed Table (Role Sequence + Output Format)
**Combination.** Three roles with completion declarations as hard gates: SCANNER produces the typed table and writes `SCANNER COMPLETE: ...`. PIVOT ANALYST cites a Signal ID and writes `PIVOT ANALYST COMPLETE: ...`. DRAFTER requires both completion declarations before beginning. C-11/C-12/C-13 become role-boundary entry conditions — each declaration names the specific Signal ID, making the chain auditable end-to-end.

---

**Key R2 design decision**: Every variation uses a `Signal ID` column scheme (S-01, S-02...) in the typed table. This gives the pivot rationale a specific citable token — satisfying C-12 becomes trivial once the table exists with IDs.
