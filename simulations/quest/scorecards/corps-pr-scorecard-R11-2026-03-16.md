## R11 Score — corps-pr (Rubric v10)

---

## Per-Variation Criterion Walkthrough

### Essential Criteria (C-01–C-05) — all variations

All five variations include Phase A routing table (C-01), binary domain-lens gate with rewrite consequence and drop rule in Phase C (C-05), Phase D consensus with structural mechanism explanation (C-03), and Phase E single unhedged decision (C-04). C-02 is covered by Phase C minimum-findings structure.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| **Essential total** | **5/5** | **5/5** | **5/5** | **5/5** | **5/5** |

---

### Recommended Criteria (C-06–C-08) — all variations

All five variations include: `COVERAGE GAP: [file]` notice (C-06), per-role `Summary: [N] findings -- [x] P1, [y] P2, [z] P3` (C-07), and AMEND SCOPE named-field block before Phase A (C-08).

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **3/3** | **3/3** | **3/3** | **3/3** | **3/3** |

---

### Aspirational Criteria (C-09–C-35)

Key discriminators are C-23, C-32, C-33, C-34, C-35.

**C-23 (READ RECEIPT has fields a–e):**
- V-01/V-04/V-05: receipts use labeled `(a)–(e)` fields including `(d) Ledger row` and `(e) Initial position` — **PASS**
- V-02/V-03: receipts use Section read / WORSE rows / BETTER rows / Conclusion / Budget strength only — **missing (d) and (e)** — **FAIL**

**C-32 (READ RECEIPT cross-references PRE-COMMITMENT for d and e):**
- V-01/V-04: (d) and (e) stated inline in receipt — per rubric, inline restatement passes — **PASS**
- V-05: field (e) accepts inline OR forward cross-reference to PRE-COMMITMENT — **PASS**
- V-02/V-03: (d) and (e) absent from receipt entirely — no inline, no cross-reference — **FAIL**

**C-33 (C2 RESULT scoped to READ RECEIPT completeness, not Phase B re-check):**
- V-01/V-04/V-05: C2 block is a per-field checklist `(a) Section read named: present / absent` ... through `(e)`. Explicit note: "C2 does NOT re-check Phase B content — that is C1's scope." — **PASS**
- V-02/V-03: C2 block checks `WORSE rows cited: [copy verbatim from Phase B]`, `BETTER rows cited:`, `Ledger row cited:`, `Net direction:` — explicitly Phase B content re-verification — **FAIL**

**C-34 (F-01 typed IA-RESPONSE in findings table — Type column required):**
- V-02: findings table is `| ID | Type | Severity | Description | Domain-Lens | Owner | Resolution |`; F-01 must have `Type = IA-RESPONSE`; explicit template rules for that Type cell — **PASS**
- V-05: same table structure with Type column; F-01 IA-RESPONSE typing with dual-content Description (IA verdict + role mechanism in same cell) — **PASS**
- V-01/V-03/V-04: findings table is `| ID | Severity | Finding | Domain-Lens | Owner | Resolution |` — no Type column — **FAIL**

**C-35 (READ RECEIPT block precedes C2 RESULT in per-role output):**
- V-01: per-role structure is 3A (READ RECEIPT) → 3B (C2 receipt field check) → 3C (PRE-COMMITMENT) → 3D (findings). Template ordering enforces receipt before C2 RESULT. — **PASS**
- V-02: per-role structure 3A (receipt) → 3B (C2 compliance) → 3C (PRE-COMMITMENT). Receipt before C2 RESULT structurally. — **PASS**
- V-03: per-role labeled STEP 1 (READ RECEIPT) → STEP 2 (C2 RESULT). Explicit compliance check: "Locate READ RECEIPT header. Locate C2 RESULT line. If C2 RESULT precedes receipt header, C-35 fails for this role." — **PASS**
- V-04/V-05: STEP 1 → STEP 2 with explicit "C2 RESULT must appear after READ RECEIPT block in output [C-35]" in pipeline entry condition. — **PASS**

**All other aspirational criteria (C-09 through C-31 except C-23; C-25 through C-30):**
All five variations pass. Key evidence:
- C-09/C-12: Mechanism lines require structural/architectural cause — ban-to-fix table present in all
- C-11: Phase B (IA) precedes Phase C (technical roles) in all
- C-13: 5-entry perspective-label ban table in all (≥3 required)
- C-14/C-31: F-01 description is `[IA found X; [role] rates P-N because [mechanism]]` in all — IA counterpoint inside finding body
- C-16: AMEND SCOPE named-field block (not prose) in all
- C-17/C-19/C-21: 4-row × 2-column ledger with Net column; WORSE/BETTER/Conclusion lines in all
- C-22: Exactly C1 (phase-level) + C2 (per-role), independently producing result tokens, in all
- C-24: Domain-Lens column in findings table in all
- C-25/C-28: Three labeled budget verdict clauses, each on own line, in all
- C-26: C1 RESULT and C2 RESULT per-role terminal lines in all
- C-27/C-29: PRE-COMMITMENT block with `[PRE-COMMITMENT SEALED]` token in all
- C-30: Phase C exit condition names PRE-COMMITMENT blocks presence in all

---

### Full Aspirational Scorecard

| Crit | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| **C-23** | PASS | **FAIL** | **FAIL** | PASS | PASS |
| C-24 | PASS | PASS | PASS | PASS | PASS |
| C-25 | PASS | PASS | PASS | PASS | PASS |
| C-26 | PASS | PASS | PASS | PASS | PASS |
| C-27 | PASS | PASS | PASS | PASS | PASS |
| C-28 | PASS | PASS | PASS | PASS | PASS |
| C-29 | PASS | PASS | PASS | PASS | PASS |
| C-30 | PASS | PASS | PASS | PASS | PASS |
| C-31 | PASS | PASS | PASS | PASS | PASS |
| **C-32** | PASS | **FAIL** | **FAIL** | PASS | PASS |
| **C-33** | PASS | **FAIL** | **FAIL** | PASS | PASS |
| **C-34** | **FAIL** | PASS | **FAIL** | **FAIL** | PASS |
| C-35 | PASS | PASS | PASS | PASS | PASS |
| **Asp. pass** | **26/27** | **24/27** | **23/27** | **26/27** | **27/27** |

---

## Composite Scores

```
composite = (5/5 * 60) + (3/3 * 30) + (aspirational_pass/27 * 10)
```

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-05 | 60.00 | 30.00 | 10.00 (27/27) | **100.00** |
| V-01 | 60.00 | 30.00 | 9.63 (26/27) | **99.63** |
| V-04 | 60.00 | 30.00 | 9.63 (26/27) | **99.63** |
| V-02 | 60.00 | 30.00 | 8.89 (24/27) | **98.89** |
| V-03 | 60.00 | 30.00 | 8.52 (23/27) | **98.52** |

---

## Ranking

1. **V-05 — 100.00** (all 27 aspirational, all 3 R11 targets passed simultaneously)
2. **V-01 — 99.63** (passes C-33 and C-35; fails C-34 — no Type column)
2. **V-04 — 99.63** (passes C-33 and C-35; fails C-34 — no Type column; tie with V-01)
4. **V-02 — 98.89** (passes C-34; fails C-23/C-32/C-33 — receipt missing d/e, C2 re-checks Phase B)
5. **V-03 — 98.52** (passes C-35 explicitly; fails C-23/C-32/C-33/C-34)

---

## Excellence Signals from V-05

**1. Seven-item enumerated Phase C exit list — one item per structural mechanism**
V-05's Phase C exit conditions are seven independently checkable numbered items, each citing the criterion it enforces. V-01/V-04 list them in a single prose sentence. Enumeration makes the exit gate auditable at item granularity: each condition can fail independently without collapsing the others.

**2. C-33 and C-35 declared as causally linked in the pipeline — not parallel exit conditions**
V-04 names both C-33 and C-35 in Phase C exit but treats them as two independent items. V-05 wires the causal direction into the declaration: "C2 RESULT must appear after READ RECEIPT block in output [C-35]" and then "C2 scope: receipt fields (a)-(e) complete... C2 does NOT re-verify Phase B — that is C1's scope [C-33]." The causal chain — C-35 ordering is the structural precondition for C-33's completeness check — is declared explicitly, making the integration argument auditable without consulting the rubric.

**3. Inline anti-pattern example at the C2 template use site (C-33)**
V-05's C2 block instructions include: "Replacing a receipt field check with 'WORSE rows verbatim cited: yes' would be a C-33 violation even if C2 RESULT: SATISFIED is output." This is an inline negative example naming the specific surface form of the anti-pattern — positioned where the violation would occur, not in a separate compliance note.

**4. Forward cross-reference option in receipt field (e) enables PRE-COMMITMENT timing separation**
V-05 allows field (e) to read "see PRE-COMMITMENT block below: (d) [row name], (e) committed below" instead of stating the position inline. This means the initial position is committed in the PRE-COMMITMENT block (where it can be SEALED as a timing claim) while the receipt remains auditably complete via the cross-reference. C-32 passes because the receipt points to the block by label; C-27/C-29 pass because the commitment is in the sealed block. The split enables both criteria simultaneously without duplicating content.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Seven-item enumerated Phase C exit list — one item per structural mechanism, each independently auditable by number", "C-33 and C-35 declared as causally linked in pipeline declaration (C-35 ordering is the structural precondition for C-33 completeness check), not as parallel independent exit conditions", "Inline anti-pattern example at the C2 template use site names the exact surface form of the C-33 violation without requiring rubric consultation"]}
```
