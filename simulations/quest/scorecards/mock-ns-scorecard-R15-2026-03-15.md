I now have all the data needed. Let me evaluate each variation.

---

## Round 15 Scorecard — mock-ns (Rubric v14, denominator 32)

### Foundation Criteria C-01 through C-37

All five variations share the same structural base carried forward from R14's golden form. Spot-checking confirms:

| Criteria block | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-01 through C-05 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-06 through C-08 (recommended) | PASS | PASS | PASS | PASS | PASS |
| C-09 through C-13 (aspirational, format) | PASS | PASS | PASS | PASS | PASS |
| C-14 through C-17 (FLAG immutability chain) | PASS | PASS | PASS | PASS | PASS |
| C-18 through C-24 (path enumeration + instruction governance) | PASS | PASS | PASS | PASS | PASS |
| C-25 through C-27 (guarantee-break + structural isolation) | PASS | PASS | PASS | PASS | PASS |
| C-28 through C-33 (nav anchors + bracket tokens + structured preamble table) | PASS | PASS | PASS | PASS | PASS |
| C-34 (explicit lookup obligation) | PASS | PASS | PASS | PASS | PASS |
| C-35 (row-specific navigation labels at S-3 and A-1) | PASS | PASS | PASS | PASS | PASS |
| C-36 (two-phase confirmation gate in preamble) | PASS | PASS | PASS | PASS | PASS |
| C-37 (confirmation echo at both use sites) | PASS | PASS | PASS | PASS | PASS |

All 37 prior criteria: PASS across all five variations. Basis: shared structural foundation; R15 axes exclusively target C-38/C-39/C-40.

---

### New Criteria C-38 / C-39 / C-40

#### C-38 — Hard-stop gate language at all three locations (P-0, S-3, A-1)

Pass condition: "DO NOT WRITE THE ROW until both phases pass" (or equivalent execution block) at the preamble gate definition AND S-3 echo AND A-1 echo. All three must carry the hard-stop form.

| Variation | P-0 gate | S-3 echo | A-1 echo | Verdict |
|---|---|---|---|---|
| V-01 | "DO NOT WRITE THE ROW until both phases pass." | "DO NOT WRITE THE ROW until both phases pass." | "DO NOT WRITE THE ROW until both phases pass." | **PASS** |
| V-02 | "STOP. DO NOT WRITE THE ROW until both phases pass." | "STOP. DO NOT WRITE THE ROW until both phases pass." | "STOP. DO NOT WRITE THE ROW until both phases pass." | **PASS** |
| V-03 | "DO NOT WRITE THE ROW until both phases pass and the record is emitted." | "DO NOT WRITE THE ROW until both phases pass." | "DO NOT WRITE THE ROW until both phases pass." | **PASS** |
| V-04 | "DO NOT WRITE THE ROW until both phases pass." | "DO NOT WRITE THE ROW until both phases pass." | "DO NOT WRITE THE ROW until both phases pass." | **PASS** |
| V-05 | "STOP. DO NOT WRITE THE ROW until both phases pass and the record is emitted." | "DO NOT WRITE THE ROW until both phases pass and record is emitted." | "DO NOT WRITE THE ROW until both phases pass and record is emitted." | **PASS** |

All five pass C-38. Confirms that verbatim hard-stop is stable across all five axes when derived from R14's best form.

---

#### C-39 — Anti-bypass closing statement (C-36 dependency satisfied for all)

Pass condition: (a) names the bypass action explicitly (visual recognition / locate-only), (b) asserts it does not satisfy the protocol, (c) distinguishes it from Phase 2 completion.

**V-01**: No anti-bypass statement anywhere. → **FAIL**

**V-02**: After the STOP line in P-0 Phase 2:
> "An executor who recognizes a token without performing Phase 2 has not satisfied this protocol. Locate-only is a Phase 1 result; it does not satisfy the gate."
- (a) PASS: "recognizes a token without performing Phase 2" names visual recognition as the bypass.
- (b) PASS: "has not satisfied this protocol."
- (c) PASS: "Locate-only is a Phase 1 result" explicitly distinguishes Phase 1 from Phase 2 completion.
→ **PASS**

**V-03**: No anti-bypass statement. → **FAIL**

**V-04**: Opens P-0 before the abbreviation key:
> "Recognizing a token in the table below without reading the Step and Row type cells is a locate-only operation (Phase 1 only). An executor who performs only Phase 1 has not satisfied this protocol. Locate-only does not satisfy the confirmation gate."
- (a) PASS: "without reading the Step and Row type cells" is the specific bypass action named.
- (b) PASS: "has not satisfied this protocol."
- (c) PASS: "(Phase 1 only)" explicitly frames it as not completing Phase 2.
→ **PASS**

**V-05**: Opens P-0 before the abbreviation key:
> "Recognizing a token in the table below without reading the Step and Row type cells is a locate-only operation (Phase 1 only). An executor who recognizes a token without performing Phase 2 has not satisfied this protocol. Locate-only is a protocol failure."
- (a) PASS: "without reading the Step and Row type cells" + "without performing Phase 2" — two distinct naming forms.
- (b) PASS: "has not satisfied this protocol."
- (c) PASS: "(Phase 1 only)" + "Locate-only is a protocol failure" — strongest severity framing in the set.
→ **PASS**

---

#### C-40 — Confirmation record output obligation (C-38 dependency satisfied for all)

Pass condition: Phase 2 is not a silent assertion — executor must emit a confirmation record. Requires the preamble gate definition to state the emit obligation, and use-site pre-filled templates at S-3 and A-1.

**V-01**: Phase 2 is "assert that the step name matches... and that the row type name matches." No emit instruction anywhere. → **FAIL**

**V-02**: Phase 2 ends with STOP but no emit record. Use-site echoes carry hard-stop but no template. → **FAIL**

**V-03**:
- P-0 gate: "Emit confirmation record: Phase 1 confirmed: {token} located at P-0 row {N}. Phase 2 confirmed: Step={step}, Row type={row-type}; match=PASS." — emit obligation stated in preamble gate. ✓
- S-3 use site: pre-filled template "Phase 1 confirmed: [S-3:CS] at P-0 row 1. Phase 2 confirmed: Step=S-3, Row type=Cross-site reference row; match=PASS." ✓
- A-1 use site: pre-filled template "Phase 1 confirmed: [A-1:FC] at P-0 row 2. Phase 2 confirmed: Step=A-1, Row type=Failure consequence row; match=PASS." ✓
→ **PASS**

**V-04**: No emit record. Use-site echoes carry hard-stop only. → **FAIL**

**V-05**:
- P-0 gate: "Emit confirmation record: Phase 1 confirmed: {token} located at P-0 row {N}. Phase 2 confirmed: Step={step}, Row type={row-type}; match=PASS." ✓
- S-3 use site: pre-filled template + "DO NOT WRITE THE ROW until both phases pass and record is emitted." ✓
- A-1 use site: pre-filled template + "DO NOT WRITE THE ROW until both phases pass and record is emitted." ✓

Note: V-05 additionally weaves the emit obligation directly into the hard-stop gate condition ("until both phases pass **and the record is emitted**"), making emission a gate precondition rather than a sub-task of Phase 2. This is stronger than V-03 which ends its gate with "until both phases pass" (the emit is listed within Phase 2 but not echoed in the gate).
→ **PASS**

---

### Per-Variation Composite Scores

Formula: `aspirational_pass / 32 * 10`

#### V-01 — Phrasing Register

| Criterion | Status | Evidence note |
|---|---|---|
| C-01 to C-37 | 37 PASS | Shared foundation |
| C-38 | PASS | Hard-stop at P-0, S-3, A-1 verbatim |
| C-39 | FAIL | No anti-bypass statement at any location |
| C-40 | FAIL | No emit record; Phase 2 remains silent assertion |

**Pass count: 30/32 — Score: 9.375**

Hypothesis confirmed for its scope: C-38 alone is achievable with verbatim repetition at all three sites. Clean isolation result — C-38 is now a stable baseline, not an aspirational differentiator.

---

#### V-02 — Lifecycle Emphasis

| Criterion | Status | Evidence note |
|---|---|---|
| C-01 to C-37 | 37 PASS | Shared foundation |
| C-38 | PASS | "STOP. DO NOT WRITE THE ROW" at P-0, S-3, A-1 |
| C-39 | PASS | Closing statement after STOP names locate-only bypass, asserts protocol failure, distinguishes Phase 1/2 |
| C-40 | FAIL | No emit record; Phase 2 remains silent assertion |

**Pass count: 31/32 — Score: 9.688**

The sub-section structure (Phase 1/Phase 2 named headers) adds visual non-collapsibility. STOP + anti-bypass closing is the strongest closing-position form in the set. Gap: Phase 2 is still unverifiable from the output.

---

#### V-03 — Output Format

| Criterion | Status | Evidence note |
|---|---|---|
| C-01 to C-37 | 37 PASS | Shared foundation |
| C-38 | PASS | Hard-stop at P-0, S-3, A-1 with "and the record is emitted" extension |
| C-39 | FAIL | No anti-bypass statement at any location |
| C-40 | PASS | Emit record in P-0 gate; pre-filled templates at S-3 and A-1 with named fields |

**Pass count: 31/32 — Score: 9.688**

C-40 is cleanly demonstrated in isolation. The pre-filled template forces a pause (filling named fields) that prevents Phase 1/Phase 2 collapse. Gap: no bypass is named; an executor may still not understand why Phase 2 matters before attempting the gate.

---

#### V-04 — Role Sequence + Inertia Framing

| Criterion | Status | Evidence note |
|---|---|---|
| C-01 to C-37 | 37 PASS | Shared foundation |
| C-38 | PASS | Hard-stop at P-0, S-3, A-1 |
| C-39 | PASS | Opening preamble names bypass before abbreviation key, before table, before protocol definition |
| C-40 | FAIL | No emit record; Phase 2 remains silent assertion |

**Pass count: 31/32 — Score: 9.688**

The opening-position anti-bypass creates a rejection frame: the executor knows locate-only is a named failure before encountering the protocol. This is the inertia-framing hypothesis confirmed — but produces same score as V-02, making it an axis test rather than a score differentiator. Gap: identical to V-02, no emit record.

---

#### V-05 — Full Convergence

| Criterion | Status | Evidence note |
|---|---|---|
| C-01 to C-37 | 37 PASS | Shared foundation |
| C-38 | PASS | "STOP. DO NOT WRITE THE ROW until both phases pass and the record is emitted." at P-0; same hard-stop woven into emit condition at S-3 and A-1 |
| C-39 | PASS | Opening preamble + "Locate-only is a protocol failure" (strongest severity framing) |
| C-40 | PASS | Emit obligation in P-0 gate + emit woven into C-38 gate condition + pre-filled templates at S-3 and A-1 |

**Pass count: 32/32 — Score: 10.0**

Full convergence achieved. Each bypass path (visual recognition, skipped Phase 2, silent assertion) fails at least two independent mechanisms simultaneously. The V-05 form seeds the v15 reference maximum.

---

### Ranking

| Rank | Variation | Score | New criteria |
|---|---|---|---|
| 1 | V-05 Full Convergence | **10.0** (32/32) | C-38 + C-39 + C-40 |
| 2 | V-02 Lifecycle Emphasis | 9.688 (31/32) | C-38 + C-39 |
| 2 | V-03 Output Format | 9.688 (31/32) | C-38 + C-40 |
| 2 | V-04 Inertia Framing | 9.688 (31/32) | C-38 + C-39 |
| 5 | V-01 Phrasing Register | 9.375 (30/32) | C-38 only |

---

### Excellence Signals from V-05

**Signal 1 — Emit obligation woven into the gate condition, not only into Phase 2 sub-task.**
V-03 places emit inside Phase 2 ("read cells; assert; emit record") and ends with "DO NOT WRITE THE ROW until both phases pass." V-05 places emit inside Phase 2 AND echoes it in the gate condition: "until both phases pass **and the record is emitted**." This makes emission a gate precondition, not a completable sub-task. An executor who performs Phase 2 silently and reaches the gate is still blocked — the gate explicitly requires the record to exist before proceeding.

**Signal 2 — "Locate-only is a protocol failure" as the strongest severity register.**
V-02 uses "Locate-only is a Phase 1 result; it does not satisfy the gate." V-04 uses "Locate-only does not satisfy the confirmation gate." V-05 uses "Locate-only is a protocol failure." The severity escalation — from "does not satisfy" (a sufficiency framing) to "is a protocol failure" (a violation framing) — labels the action as a categorically wrong outcome, not merely an incomplete one.

**Signal 3 — Three independent bypass-prevention mechanisms stacked on the same gate.**
No single bypass path survives V-05: (1) the opening rejection preamble blocks visual-recognition before the table is seen; (2) the Phase 2 sub-section with STOP boundary makes the gate physically non-collapsible into a single scan; (3) the emitted record makes Phase 2 non-silent — the record must exist in the output. Any one mechanism could theoretically be bypassed; three simultaneous mechanisms require an executor to actively override each independently.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Emit obligation woven into gate condition as a precondition (not only listed within Phase 2 sub-task): 'until both phases pass and the record is emitted' closes the gap where Phase 2 can be completed silently and the gate reached without a record", "Severity escalation to protocol-failure register: 'Locate-only is a protocol failure' frames the bypass as a categorical violation rather than an insufficiency, stronger than 'does not satisfy the gate'", "Three independent bypass-prevention mechanisms stacked on the same gate: opening rejection frame (C-39) + Phase 2 sub-section with STOP boundary (C-38 structural) + emitted observable record (C-40) -- any single bypass path fails at least two mechanisms simultaneously"]}
```
