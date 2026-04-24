Written to `simulations/quest/golden/trace-permissions-variate-R13-2026-03-17.md`.

---

## Round 13 Variation Map

| Variation | Axis | v12 Hypothesis | Delta from R12-V-05 |
|-----------|------|----------------|---------------------|
| **V-01** | Single-axis C-35: SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-ref + CA-1.9 | **26/28** | Adds CA-1.9 pre-assignment + SE-0 slot in SE-4 STRUCTURED CLOSE; CA-1.9 distinguished from CA-1.4 and CA-1.7 |
| **V-02** | Single-axis C-34: preamble R12 Structural Axis Declaration | **26/28** | Adds R12 STRUCTURAL AXIS DECLARATION block after preamble table naming execution order / closure-note format / CS self-reference as orthogonal with non-interference statement |
| **V-03** | Single-axis C-36: tri-dimensional CA terminal self-evidence attestation | **26/28** | Adds TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block in terminal verdict naming each dimension with specific Phase output-body evidence source |
| **V-04** | Combined C-34+C-35 | **27/28** | V-02 + V-01; preamble axis declaration adds CA-1.9 to Dimension 1 verification row |
| **V-05** | Full combination C-34+C-35+C-36 | **28/28** | V-04 + tri-dimensional terminal attestation; non-interference declaration cites CA-1.4+CA-1.9 for Dimension 1 |

**Key architectural decisions:**

1. **CA-1.9 scope isolation** — Three non-overlapping audit targets on SE-4: CA-1.4 (TABLE_4 at SE-0 before TABLE_1), CA-1.7 (MANUAL GAP exact-label block at SE-4 opening), CA-1.9 (TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE block). The scope distinction is stated in the pre-assignment table, in SHALL-G, and in CA-1.9's verification row.

2. **SE-0 slot semantics** — SE-4's STRUCTURED CLOSE block opens with an explicit `SE-0 cross-reference:` line naming a specific TABLE_4 vector row by its exact label, along with the Checked? value and Finding. This makes the cross-reference structurally distinct from the broader STRUCTURED CLOSE prose that follows.

3. **Axis declaration placement** — The R12 STRUCTURAL AXIS DECLARATION sits inside Step 0.2 (preamble), after the five-row enforcement matrix and before the SHALL obligations. V-05's declaration includes CA-1.4+CA-1.9 as the dual verifiers of Dimension 1, connecting the axis declaration to the new CA-1.9 row.

4. **Tri-dimensional attestation form** — V-03/V-05's attestation is a named table (three rows, Dimension / Label / Evidence Source columns), not prose. Each evidence source names a specific section and a specific string that would be found there by inspection, satisfying the "specific output-body evidence source" requirement of C-36.
