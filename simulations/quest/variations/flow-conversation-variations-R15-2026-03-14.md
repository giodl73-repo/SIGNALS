Written to `simulations/quest/rubrics/flow-conversation-rubric-v14-variations-R15-2026-03-15.md`.

---

## Round 15 Variations Summary

**Axes selected for R15:**

| Axis | Criterion target | Single-axis |
|------|-----------------|-------------|
| L — Full lifecycle protocol closure | C-63 | V-01 |
| M — Schema-typed manifest rows | C-64 | V-02 |
| N — Row-count CA verification | C-65 | V-03 |
| L+M | C-63 + C-64 | V-04 |
| L+M+N | C-63 + C-64 + C-65 | V-05 |

---

**What each variation does to close its target criterion:**

**V-01 (Axis L)** — Tightens the two gaps R14 V-05 left in C-63: the Auditor now closes Phase 6-A specifically (not Phase 6 as a whole) with `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER`, and the RP opens with the exact token string `"Received AUDITOR_CERTIFICATION: COMPLETE."`. All 5 boundaries are now bidirectionally locked with matching outgoing/incoming tokens.

**V-02 (Axis M)** — Adds a `SCHEMA_TYPE` column to PRE_FLIGHT_MANIFEST. Rows for 0-A-8/9/10/11 carry `SCHEMA_TYPE: FIELD|VALUE`. At Phase 0-CA-1, status resolves to `COMPLETE | MISSING | WRONG_SCHEMA`. `WRONG_SCHEMA` applies when the declaration is present but uses prose instead of FIELD|VALUE tables. The manifest becomes the enforcement origin for schema type, not the rubric text.

**V-03 (Axis N)** — Adds full parenthetical row counts to all four `DECLARATION_SCHEMA_COMPLETE` entries in Phase 0-CA-1: `DECLARATION_NAME: PASS|FAIL (count N rows: [named breakdown])`. FAIL entries name the specific missing fields. A binary PASS|FAIL without a count does not satisfy the verification contract. Also adds a Phase 6-A check that verifies counts were present.

**V-04 (L+M)** — Combines lifecycle protocol + schema-typed manifest. C-63 closes the token boundary layer; C-64 closes the manifest schema layer. Together they eliminate the "wrong-format declaration silently passing" case and the "implicit RP start" case simultaneously.

**V-05 (L+M+N)** — All three axes. The three criteria form interlocking layers: C-63 governs what crosses role boundaries, C-64 governs what the manifest knows about encoding contracts, C-65 governs how deeply the CA verifies those contracts. All three ambiguity zones from R14 PARTIAL scores are structurally closed.
