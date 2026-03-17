`C:/src/sim/simulations/quest/rubrics/flow-lifecycle-rubric-v10-variate-R10-2026-03-15.md` written.

---

## flow-lifecycle — Round 10 Variations (Rubric v10)

**Ceiling entering R10**: 28/28 (R9 V-04/V-05 cracked C-34, C-35, C-36)
**Open criteria**: None. All 5 variations carry the full R9 ceiling as baseline.
**Formula**: `/28` · Golden threshold: all 5 essential + composite >= 80

---

### Variation Table

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| **V-01** | A: Role Sequence Schedule | Pre-declaring role-to-phase ownership as a named table creates a Role→Phase→B-NN traceability direction; B-NN Cause fields cite both IM-ID and blocking R-ID |
| **V-02** | B: Phase-exit gate `Blocked bottleneck:` | Adding a named sub-field citing B-NN in every PHASE EXIT GATE creates Phase→B-NN forward linkage verifiable by string comparison — the C-37 probe |
| **V-03** | C: BOTTLENECK IMPACT MATRIX | Consolidated cross-reference table [B-ID \| Phase \| IM-ID \| SLA node \| Time cost \| Mitigation owner] makes traceability density scannable in one artifact — may surface a C-37+ density criterion |
| **V-04** | A + B | Role sequence + exit gate bottleneck linkage — compound Role→Phase→B-NN→IM-ID chain verifiable at every link by string comparison |
| **V-05** | A + B + C | Maximum configuration: role schedule + exit gate B-ID + impact matrix compose into a full five-link chain (Role→Phase→B-NN→IM-ID→SLA node) |

---

### New structural elements per variation

**V-01 adds** (after Role Registry Gate, before Phase 1):
```
ROLE SEQUENCE SCHEDULE
| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role | Parallel Window |
```
B-NN Cause fields must cite both IM-ID and blocking R-ID.

**V-02 adds** (to every PHASE EXIT GATE):
```
- Blocked bottleneck: B-NN or NONE
  [B-ID must string-match Bottleneck Analysis block identifier]
```
CHAIN STATUS gains an "Exit gate consistency" check.

**V-03 adds** (after Gap Identification):
```
BOTTLENECK IMPACT MATRIX
| B-ID | Phase Affected | IM-ID Source | SLA Node (S-ID) | Time Cost | Mitigation Owner (R-ID) |
```
CHAIN STATUS gains a "Matrix consistency" check. Every cell is a string-comparison contract.

**V-04** = V-01 + V-02. PHASE EXIT GATE `Exit verification` role must match Role Sequence Schedule primary owner. CHAIN STATUS has both exit-gate-consistency and role-schedule checks.

**V-05** = V-01 + V-02 + V-03. Role Registry anti-generic validation expands to require each R-ID appear in the BOTTLENECK IMPACT MATRIX Mitigation Owner column. CHAIN STATUS verifies all four consistency dimensions.

---

### C-37 probe design

The rubric v10 notes that `Blocked bottleneck: B-NN or NONE` in the PHASE EXIT GATE was anticipated as a V-04/V-05 signal in R9. V-02 isolates it as a single-axis test; V-04 and V-05 carry it combined. If C-37 is: *"PHASE EXIT GATE `Blocked bottleneck:` sub-field names a B-ID that string-matches a declared B-NN block"*, then V-02 is the minimal probe and V-04/V-05 are the combined confirmations.
