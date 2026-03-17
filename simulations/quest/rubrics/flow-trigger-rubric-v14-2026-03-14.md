Done. `flow-trigger-rubric-v14-2026-03-15.md` written.

**v14 summary:**

| Change | Detail |
|--------|--------|
| **New criteria** | C-39, C-40, C-41 extracted from R17 V-01/V-02/V-03 axes |
| **Denominator** | /31 → /34 |
| **Formula** | `aspirational_pass / 34 * 10` |

**Three new criteria:**

- **C-39** (V-01 axis): PASSAGE_KEY fields in all 7 GATE-STATE blocks — gate artifact declares which upstream CHAIN-LINK keys it consumed to confirm passage; Role 5 audits a 21-column manifest table (14 Presence slots + 7 passage-key slots); PASSAGE-KEY-GAP is distinct from MANIFEST-GAP. Distinguishes from C-37 (chain-layer key readback) by operating at the gate-artifact layer — bidirectional key chain from emissions → gate declarations.

- **C-40** (V-02 axis): 14-row Ownership Registry at simulation header; Role 5 gains an Owner verification column alongside Presence; OWNER-MISMATCH format `(declared: [role], expected: [role from registry])`. Distinguishes from C-35 (four owners declared) by adding a detection layer — ownership is registerable and auditable, not just named in prose.

- **C-41** (V-03 axis): `SIMULATION MANIFEST — DERIVATION PROOF` block with `ROLE_COUNT=7`, `GATE_COUNT=7`, `TOTAL=14`, `MANIFEST_DENOMINATOR=/14`; Role 5 performs a `DERIVATION VERIFICATION` phase before slot audit with named `DERIVATION-MISMATCH` failure. Distinguishes from C-38 (manifest exists with uniform gap protocol) by requiring the denominator to be derived, not asserted.

**R17 retroactive under v14:**

| Variation | Aspirational | Composite |
|-----------|-------------|-----------|
| V-01 | 32/34 | 99.41 |
| V-02 | 32/34 | 99.41 |
| V-03 | 32/34 | 99.41 |
| V-04 | 33/34 | 99.71 |
| V-05 | 34/34 | **100.00** |

**R16 V-05 retroactive**: drops from 100.00 (v13) to **99.12** (v14) — none of C-39/C-40/C-41 present.
