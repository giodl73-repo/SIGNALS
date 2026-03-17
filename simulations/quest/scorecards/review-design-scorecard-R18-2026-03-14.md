## Round 18 Scorecard — `review-design` (Rubric v17)

**Baseline state entering R18:** R17 V-02 body + R17 V-05 BLOCK 5. Carrying criteria C-01–C-49 PASS, C-50 PASS (F-29 from R17 V-02), C-51 **FAIL** (R17 V-02 F-30 trigger fired on absence only; C-51 requires firing on wrong lifecycle position). Denominator: 44 aspirational.

---

### Shared Baseline Criteria (identical across all five variations)

All blocks except BLOCK 2.7 are identical. Criteria C-01–C-07 (essential + recommended) and C-08–C-49 (aspirational) carry forward unchanged.

| Criteria | Status | Note |
|---|---|---|
| **C-01** All 6 stock disciplines | PASS | Inherited; all 6 present |
| **C-02** Severity tag on every finding | PASS | F-02 in BLOCK 2 |
| **C-03** Domain expert auto-selection justified | PASS | BLOCK 0 → BLOCK 1 chain with F-13/F-18 |
| **C-04** Consensus block present | PASS | F-04 in BLOCK 3 |
| **C-05** Unique catches surfaced | PASS | BLOCK 4 with no-catch sentinel |
| **C-06** Amend pathway described | PASS | BLOCK 5, F-05 on full-re-review |
| **C-07** Finding traceability to section | PASS | F-27 on empty P1 Section cell |
| **C-08–C-12** | PASS | Pyramid gate, expert disagreement, structural columns, pyramid block, severity pyramid gate |
| **C-13** Expert trace table column form | PASS | BLOCK 1 table with Signal/Expert/Reason columns |
| **C-14–C-17** | PASS | F-ID coverage, BLOCK 1.5 roster lock, Source column, F-10 orphan detection |
| **C-18–C-22** | PASS | F-11 SPLIT synthesis, F-12 P1 count parity, BLOCK 5 4-col table, BLOCK 0 pre-scan, BLOCK 3 4-col table |
| **C-23** Register isolation | PASS | Block headers use formal modal vocabulary |
| **C-24–C-31** | PASS | F-16/F-17/F-18/F-19/F-20/F-21/F-22/F-23 all present |
| **C-32–C-35** | PASS | F-24/F-25/F-26/F-27 content completeness halts |
| **C-36** Section column leftmost in BLOCK 2 | PASS | Section is leftmost column in finding tables |
| **C-37** Inline corrective action in halts | PASS | All F-IDs name corrective action with target cell/referent |
| **C-38–C-41** | PASS | Amendment Cost column, Priority Rank column, inertia principle, BLOCK 5 Section-first |
| **C-42–C-46** | PASS | F-28 cross-block verify, BLOCK 2.7 dedicated registry, bidirectional resolution, BLOCK 3 Elevation Record, SEALED gates |
| **C-47** F-31 Elevation Record value halt | PASS | F-31 fires on non-ELEVATED/BASELINE Consensus Status |
| **C-48** SEALED F-code enumeration | PASS | All SEALED statements enumerate specific F-IDs with role descriptions |
| **C-49** CONSENSUS ELEVATION RULE fully enumerated | PASS | From R17 V-05 BLOCK 5: tier rank ranges, sort keys, non-conformance prohibition |

---

### BLOCK 2.7 Differential Analysis — C-50 and C-51

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-50** F-29 inbound integrity halt | PASS | PASS | PASS | PASS | PASS |
| **C-51** F-30 position integrity halt | PASS | PASS | PASS | PASS | PASS |

**C-50 evidence per variation:**

- **V-01** — Phase B: `CONSTRAINT VIOLATED when any registry row has no matching P1 row in BLOCK 2. Remove the spurious row from this registry before continuing. Halt. (F-29)` Trigger and corrective action both present. C-37 ✓.
- **V-02** — 3-column table + `BLOCK 2 P1 Backed?` column. F-29 fires when any row carries `No`. Structural column makes inbound violation detectable without executing halt logic. Corrective action: `Remove the spurious row from this registry before continuing.` C-37 ✓.
- **V-03** — Formal modal contract: `Every row in this registry SHALL correspond to at least one P1 finding row in BLOCK 2...A registry row without a backing BLOCK 2 P1 finding is spurious and SHALL NOT appear`. F-29 fires on `no corresponding BLOCK 2 P1 finding with the identical Section value`. Corrective action: `Remove the spurious row before continuing.` (anaphoric referent unambiguous from trigger). C-37 ✓.
- **V-04** — Phase B with 3-column table. F-29 fires on `No` in `BLOCK 2 P1 Backed?`. Corrective action: `Remove the spurious row from this registry before continuing.` C-37 ✓.
- **V-05** — Phase B with formal modal contract. F-29 fires on `no corresponding BLOCK 2 P1 finding with the identical Section value`. Corrective action: `Remove the spurious row from this registry before continuing.` C-37 ✓.

**C-51 evidence per variation:**

- **V-01** — Phase A gate: F-30 fires `when this block appears at any lifecycle position other than the conformant window (after BLOCK 2.5 SEALED, before BLOCK 3)`. Fires on wrong position, not just absence. SEALED: `F-30 (position integrity: Phase A gate cleared; block is in conformant lifecycle window after BLOCK 2.5 SEALED and before BLOCK 3)`. ✓
- **V-02** — POSITION CONSTRAINT header + F-30 fires `when this block appears at any lifecycle position other than the conformant window (after BLOCK 2.5 SEALED, before BLOCK 3)`. SEALED: `F-30 (position integrity: block in conformant window after BLOCK 2.5 SEALED and before BLOCK 3)`. ✓
- **V-03** — Formal position contract: `BLOCK 2.7 SHALL occupy the lifecycle window bounded below by BLOCK 2.5 SEALED and above by BLOCK 3.` F-30 fires `when this block is produced at any position outside the conformant lifecycle window`. SEALED: `F-30 (position integrity: BLOCK 2.7 in conformant lifecycle window after BLOCK 2.5 SEALED and before BLOCK 3)`. ✓
- **V-04** — Phase A (F-30) + Phase B (F-29). F-30 fires `when this block appears at any lifecycle position outside the conformant window (after BLOCK 2.5 SEALED, before BLOCK 3)`. SEALED: `F-30 (position integrity: Phase A cleared; block in conformant window after BLOCK 2.5 SEALED and before BLOCK 3)`. ✓
- **V-05** — Inertia note + Phase A. F-30 fires `when this block is produced at any lifecycle position outside the conformant window (after BLOCK 2.5 SEALED, before BLOCK 3). BLOCK 2.7 is non-conformant at any other position.` SEALED: `F-30 (position integrity: Phase A cleared; BLOCK 2.7 occupies conformant lifecycle window after BLOCK 2.5 SEALED and before BLOCK 3; absence and wrong-position both non-conformant)`. ✓ SEALED explicitly names both non-conformant trigger forms.

---

### Per-Variation Composite Scores

All variations: 4/4 essential PASS, 3/3 recommended PASS, 44/44 aspirational PASS.

```
composite = (4/4 × 60) + (3/3 × 30) + (44/44 × 10)
          = 60 + 30 + 10
          = 100.00
```

| Variation | Essential | Recommended | Aspirational | Composite | Rank |
|---|---|---|---|---|---|
| **V-05** | 4/4 | 3/3 | 44/44 | **100.00** | 1 |
| **V-04** | 4/4 | 3/3 | 44/44 | **100.00** | 2 |
| **V-01** | 4/4 | 3/3 | 44/44 | **100.00** | 3 |
| **V-03** | 4/4 | 3/3 | 44/44 | **100.00** | 4 |
| **V-02** | 4/4 | 3/3 | 44/44 | **100.00** | 5 |

**Tiebreak rationale (all score 100; ranked by design quality):**

1. **V-05** — Three axes combined. Inertia note explicitly documents the prior-round absence-vs-position gap at the block level. SEALED F-30 description names both non-conformant forms ("absence and wrong-position both non-conformant") — closes the inference gap at the attestation layer. Most future-proof: the position-integrity scope of F-30 is encoded as self-explaining text, not just a trigger condition.
2. **V-04** — Two structural mechanisms simultaneously: phase gate forces sequential position→inbound verification order; `BLOCK 2 P1 Backed?` column makes inbound violations cell-detectable without halt execution. Strongest concurrent structural enforcement.
3. **V-01** — Phase A / Phase B labels make the two orthogonal enforcement classes (position integrity, inbound integrity) explicit sequential checkpoints. Clean lifecycle architecture.
4. **V-03** — Formal modal contracts (SHALL / SHALL NOT) declare the enforcement class proactively. Works without phase labels; relies on register alone to drive C-51 pass.
5. **V-02** — POSITION CONSTRAINT header + structural column. Correct and functional; POSITION CONSTRAINT is declarative prose rather than a phase checkpoint, making it slightly weaker than phase labeling for C-51 clarity.

---

### Excellence Signals (from V-05)

**Signal 1 — Block-level inertia note documenting F-code scope evolution:**
V-05 inserts an inertia note at BLOCK 2.7 that explicitly names the prior form ("Prior skill forms through R17 stated F-30 as 'fires when this block is absent'"), names the new scope ("F-30 fires when BLOCK 2.7 is not in its conformant lifecycle position, whether absent or misplaced"), and explains why both conditions are non-conformant. The note serves future maintainers directly: without it, a future edit that reverts "wrong position" to "absent" would be a silent regression with no inline evidence of why the position-integrity form is required. The note converts a rubric criterion into self-defending text.

**Signal 2 — SEALED attestation names both non-conformant trigger forms explicitly:**
V-05 BLOCK 2.7 SEALED reads: `F-30 (position integrity: Phase A cleared; BLOCK 2.7 occupies conformant lifecycle window after BLOCK 2.5 SEALED and before BLOCK 3; absence and wrong-position both non-conformant)`. Prior SEALED forms attested position correctness in positive form only ("block is in conformant position"). Naming both failure modes in the SEALED record closes the inference gap at the attestation layer — an auditor of the SEALED record sees both prohibited conditions, not just confirmation that the current execution cleared the gate.

**Candidate for C-52:** Block-level inertia note documenting enforcement class scope broadening — fires (as a rubric miss) when an F-code's trigger condition was deliberately extended from a narrower class (absence) to a broader class (position integrity) but no inline note explains the extension to future maintainers.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["block-level inertia note documenting prior-round F-code scope gap — names both prohibited trigger forms (absence and wrong-position) to protect position-integrity enforcement class against future regression", "SEALED gate names both non-conformant trigger forms explicitly in F-30 attestation record, closing inference gap at attestation layer rather than at trigger-condition layer only"]}
```
