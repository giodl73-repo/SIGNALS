Written to `simulations/quest/golden/program-plan-variate-R15-2026-03-16.md`.

---

## R15 Variate Summary (V-01 through V-05)

All five satisfy C-47, C-48, and C-49 in addition to full C-01–C-46 coverage.

| Variation | Axis | C-47 form | C-48 form | C-49 protocol name |
|-----------|------|-----------|-----------|-------------------|
| **V-01** | Phrasing Register (Compact) | Full Why: as 4-column table cell | 4th column per row; C-42 "Entry (N) below" column | `SCAN PROTOCOL` — `C1`/`C3` labels |
| **V-02** | Role Sequence (Protocol First) | Full Why: in prose-indented entry | Per-entry `(rule declared in BOUNDED BLOCK PROTOCOL above)` suffix | `BOUNDED BLOCK PROTOCOL` — appears BEFORE the 3-class table |
| **V-03** | Output Format (Enumeration) | Full Why: as numbered list item | `(rule #N above)` / `instance #N below` per item | `BLOCK SCAN PROTOCOL` — `(P1)`/`(P3)` labels |
| **V-04** | C-47 + C-48 Co-designed | Full Why: text IS fused into the back-ref phrase | Fused Why:/nav phrase per entry; C-42 table column | `BLOCK SPECIFICATION PROTOCOL` |
| **V-05** | Extended Protocol | C-47 named as sub-req (b) of Component 1; C-46 footer explicitly verifies Why: presence | C-48 named as sub-req (c) of Component 1 | `BLOCK SPECIFICATION PROTOCOL` — most formal spec |

**Key design decisions across all five:**
- C-47: Every C-41 gate_fail: index entry carries the full `Why: execution-history check, not artifact-verifiable` text verbatim
- C-48: Each C-41 entry has its own back-ref (not a single shared header pointer); each C-42 row has a forward-ref column pointing to a specific entry number
- C-49: The C-42 named section IS the protocol declaration; the C-41 header and C-46 footer are labeled as components of the same named protocol entity
