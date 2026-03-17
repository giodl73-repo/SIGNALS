# draft-proposal — Round 7 Scorecard

## Variation Profiles (Design Summary)

| Var | Axis | C-25 | C-26 | C-27 | Predicted |
|-----|------|------|------|------|-----------|
| V-01 | Lifecycle emphasis — T-GUARD defined last | FAIL | PASS | PASS | 99.5 |
| V-02 | No COMPLETION STATUS slot in Phase 0 | PASS | FAIL | PASS | 99.5 |
| V-03 | No INERTIA COST/OFFSET | PASS | PASS | FAIL | 99.5 |
| V-04 | PM-first + table-dominant — all three new pass | PASS | PASS | PASS | 100.0 |
| V-05 | Formal register + lifecycle-heavy + inertia-forward — all three new pass | PASS | PASS | PASS | 100.0 |

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01 – C-04)

All five variations are designed with full option anatomy, decision framing, and dual-role participation. Essential criteria are structurally enforced by the Phase 0 amendment tracking table in all variations.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Options coverage (3+, do-nothing included) | PASS | PASS | PASS | PASS | PASS |
| C-02 | Option anatomy complete (desc, pros/cons, risk P+I, effort) | PASS | PASS | PASS | PASS | PASS |
| C-03 | Recommendation with rationale + confidence conditions | PASS | PASS | PASS | PASS | PASS |
| C-04 | Decision framing (question + stakes before options) | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal:** 4/4 all variations → **60 pts each**

---

### Recommended Criteria (C-05 – C-07)

Scout inventory step (Phase 1) is a discrete mandatory phase in all variations. Dual-role PM/Architect attribution is enforced by phase templates. Structured comparison table is required in Phase 6.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-05 | Scout artifact surfacing | PASS | PASS | PASS | PASS | PASS |
| C-06 | Dual-role participation | PASS | PASS | PASS | PASS | PASS |
| C-07 | Structured comparison table | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal:** 3/3 all variations → **30 pts each**

---

### Aspirational Criteria (C-08 – C-27)

Detailed below with discriminator notes on the three new axes.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-08 | Assumption + risk registers, 2+ entries each | PASS | PASS | PASS | PASS | PASS |
| C-09 | Amend phase self-critique, 1+ actionable item | PASS | PASS | PASS | PASS | PASS |
| C-10 | Scout artifact inventory as discrete step | PASS | PASS | PASS | PASS | PASS |
| C-11 | Per-category amend taxonomy (3 categories) | PASS | PASS | PASS | PASS | PASS |
| C-12 | Structural OWNER slot in all three amend entry types | PASS | PASS | PASS | PASS | PASS |
| C-13 | Split temporal anchor (TEMPORAL ANCHOR + INACTION CONSEQUENCE typed fields) | PASS | PASS | PASS | PASS | PASS |
| C-14 | DEADLINE slot in all three amend entry types | PASS | PASS | PASS | PASS | PASS |
| C-15 | F-row register with sign-off linkage (CONDITIONS → F-NN ID) | PASS | PASS | PASS | PASS | PASS |
| C-16 | Numeric P\*I risk scoring with project-specific anchors | PASS | PASS | PASS | PASS | PASS |
| C-17 | Registers-before-recommendation lifecycle ordering | PASS | PASS | PASS | PASS | PASS |
| C-18 | Front-loaded amendment table (prospective init, trigger rules) | PASS | PASS | PASS | PASS | PASS |
| C-19 | Canonical F-row field labels (FAILURE MODE / TRIGGER CONDITION / MITIGATION) | PASS | PASS | PASS | PASS | PASS |
| C-20 | PREREQUISITE GATE block before recommendation | PASS | PASS | PASS | PASS | PASS |
| C-21 | Dual-signatory F-ROW ANCHOR typed slots (PM + Architect each) | PASS | PASS | PASS | PASS | PASS |
| C-22 | Named trigger IDs (T-NN) with TRIGGER back-reference in amendment rows | PASS | PASS | PASS | PASS | PASS |
| C-23 | T-GUARD sentinel defined with catch-all scope vocabulary | PASS | PASS | PASS | PASS | PASS |
| C-24 | Empty-table completion semantics (explicit T-GUARD enforcement statement) | PASS | PASS | PASS | PASS | PASS |
| **C-25** | **Sentinel-first trigger ordering (T-GUARD at position 1)** | **FAIL** | PASS | PASS | PASS | PASS |
| **C-26** | **COMPLETION STATUS as Phase 0 typed initialization slot (PENDING → terminal)** | PASS | **FAIL** | PASS | PASS | PASS |
| **C-27** | **INERTIA COST on do-nothing + INERTIA OFFSET on each alternative + GATE item** | PASS | PASS | **FAIL** | PASS | PASS |

---

### C-25 Discriminator Detail

**V-01 FAIL evidence:** The V-01 trigger table defines T-01 through T-08 first, then appends T-GUARD as the final row. T-GUARD's scope vocabulary is correct ("any required typed slot, phase block, or gate item absent from the document") and C-23 passes on scope. But position 1 in the trigger table is occupied by T-01 (Scout inventory absent). A reviewer reads position 1 and finds a named specific trigger, not the sentinel. C-25 is independently falsifiable without scanning the remainder of the table.

**V-02/V-03/V-04/V-05:** T-GUARD appears as position 1 in all; specific named triggers follow. C-25 passes.

---

### C-26 Discriminator Detail

**V-02 FAIL evidence:** V-02's Phase 0 amendment tracking table initializes trigger definitions and amendment rows but does not include a COMPLETION STATUS typed slot. The completion declaration may appear at Phase 13 as a prose instruction or appended statement (satisfying C-24) but does not exist as a structural field from document creation. A document that adds the completion declaration in the final phase without a Phase 0 COMPLETION STATUS slot passes C-24 and fails C-26. The structural slot must be live from initialization, not declared at close.

**V-01/V-03/V-04/V-05:** Phase 0 block includes `COMPLETION STATUS: PENDING` as a typed field. At Phase 13, the field is updated to the terminal T-GUARD enforcement statement. C-26 passes.

---

### C-27 Discriminator Detail

**V-03 FAIL evidence:** V-03 omits INERTIA COST from Option 0 (do-nothing) and omits INERTIA OFFSET from all alternatives. Risk register entries use numeric P\*I (C-16 passes — Phase 3 anchors defined, R-NN entries scored numerically). But the do-nothing option is treated as a qualitative baseline ("ongoing maintenance burden") rather than a computable per-sprint cost curve. C-27 is independently required from C-16: numeric risk scoring on R-NN entries does not imply inertia quantification on the option anatomy. PREREQUISITE GATE (C-20) also fails the inertia-axis binary item — neither condition is confirmed.

**V-01/V-02/V-04/V-05:** Option 0 carries `INERTIA COST: P: N x I: N = P*I: N per sprint` using Phase 3 anchors. Each alternative carries `INERTIA OFFSET: Sprint N — crossover point...`. PREREQUISITE GATE includes the inertia-axis binary confirming both fields present. C-27 passes.

---

## Score Computation

| Variation | Essential (×60) | Recommended (×30) | Aspirational (/20 × 10) | **Composite** |
|-----------|-----------------|-------------------|--------------------------|---------------|
| V-01 | 4/4 = 60.0 | 3/3 = 30.0 | 19/20 = 9.5 | **99.5** |
| V-02 | 4/4 = 60.0 | 3/3 = 30.0 | 19/20 = 9.5 | **99.5** |
| V-03 | 4/4 = 60.0 | 3/3 = 30.0 | 19/20 = 9.5 | **99.5** |
| V-04 | 4/4 = 60.0 | 3/3 = 30.0 | 20/20 = 10.0 | **100.0** |
| V-05 | 4/4 = 60.0 | 3/3 = 30.0 | 20/20 = 10.0 | **100.0** |

---

## Ranking

1. **V-04** — 100.0 (PM-first + table-dominant, all new criteria pass)
1. **V-05** — 100.0 (formal register + lifecycle-heavy + inertia-forward, all new criteria pass)
3. **V-01** — 99.5 (fails C-25: T-GUARD placed last despite correct scope)
3. **V-02** — 99.5 (fails C-26: COMPLETION STATUS not a Phase 0 typed slot)
3. **V-03** — 99.5 (fails C-27: no inertia quantification on options)

---

## Excellence Signals (from V-04/V-05)

Three structural patterns distinguish the 100.0 ceiling from the 99.5 variations. Each is independently verifiable without document-level scanning:

1. **Sentinel-first trigger ordering** — T-GUARD occupies position 1 in the Phase 0 trigger definition table, above all T-NN named triggers. Enforcement direction shifts from backstop to frontline: any unanticipated structural gap routes to the catch-all before any specific trigger is consulted. A reviewer confirms C-25 by reading exactly one cell.

2. **COMPLETION STATUS as a live mandatory Phase 0 field** — The amendment tracking table initializes with a `COMPLETION STATUS: PENDING` typed slot from document creation. The field is not a Phase 13 instruction or appended prose — it is structurally present, has a vocabulary-constrained initial value, and must be updated at completion. The field being mandatory from initialization removes the silent-skip path that C-24 alone cannot prevent.

3. **Do-nothing option carries a computable per-sprint cost curve** — INERTIA COST on Option 0 uses the same P\*I numeric scale defined in Phase 3 anchors, producing a named per-sprint accumulation metric. Each alternative's INERTIA OFFSET names the sprint crossover point as a computable threshold, not a qualitative description. The PREREQUISITE GATE binary items make both fields machine-checkable at sign-off. The decision converts from "do-nothing vs act" into "act before sprint N or pay P\*I per sprint thereafter."

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["sentinel-first trigger ordering places T-GUARD at position 1 in Phase 0 trigger table — enforcement direction shifts from backstop to frontline, one-cell verification", "COMPLETION STATUS initialized as a live typed slot in Phase 0 with PENDING value — completion semantic is mandatory from document creation not appended at Phase 13, closes the silent-skip path", "do-nothing option carries numeric per-sprint INERTIA COST using Phase 3 P*I anchors; each alternative names INERTIA OFFSET sprint crossover — converts qualitative baseline into computable cost curve with PREREQUISITE GATE binary enforcement"]}
```
