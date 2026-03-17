## R15 Scoring — listen-support v14 (265 pt ceiling)

### Scoring Foundation

**Base**: V-04 R14 = 265/265. All C-01 through C-43 at ceiling.

R15 variations are built from V-04 R14 with **additive** changes only. No existing mechanisms are removed or overwritten. The scoring question for each variation: do any additions break a passing criterion?

---

### V-01 — No-Exception Path Triple-Clause

**Change**: Both no-exception confirmation statements (Phase 1 and Phase 3 in Pass 2C) upgraded from single-clause `"do not paraphrase"` to triple-clause `"do not paraphrase, do not summarize, copy it verbatim word-for-word"`.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-37 | PASS | Inherited from base; no structural change to Steps 1–7, patterns, or coverage |
| C-38 (Dual-Field Step-4 Gate) | PASS | Step 4 retains "both items" language and two labeled fields (Confirmed + Verbatim from 2C) |
| C-39 (Every-Assignment Scope Confirmation) | PASS | "Confirmation: this rule applies to every severity assignment in the table below." preserved |
| C-40 (Exception Block Verbatim-Clause Instruction) | PASS | Exception block Paraphrase clause retains verbatim instruction |
| C-41 (Imperative Dual-Field Gate Language) | PASS | "Do not fill any cell in the table until both items are written" — imperative form preserved |
| C-42 (Cell-Level Table-Fill Prohibition) | PASS | "Do not fill any cell in the table until both items are written:" — unit is "any cell" |
| C-43 (Triple Verbatim-Prohibition Clause in Exception Block) | PASS | Exception block carries all three clauses (inherited) |
| C-44 candidate (No-Exception Triple-Clause) | PASS | Both no-exception paths now carry triple-clause — "do not paraphrase, do not summarize, copy it verbatim word-for-word" |

**Score: 265/265**

---

### V-02 — Phase Distribution Pre-Commitment Gate

**Change**: Step 4 acquires a third required item (PHASE DISTRIBUTION committed block) before any cell fills. Gate changes from "both items" to "all three items." Step 4B gains constraint 0 (count match).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-37 | PASS | Inherited from base; Steps 1–7, patterns, coverage unchanged |
| C-38 (Dual-Field Step-4 Gate) | PASS | Three labeled fields, including both required: "Required item 2 -- INFERENCE RULE (confirmed)" and "Required item 3 -- Verbatim from 2C." Failure mode is "single field"; three fields exceeds minimum. Gate instruction prohibits cell-fill until all items written. |
| C-39 (Every-Assignment Scope Confirmation) | PASS | "Confirmation: the inference rule applies to every severity assignment in the table below." preserved |
| C-40 (Exception Block Verbatim-Clause Instruction) | PASS | Exception block Paraphrase clause unchanged from base |
| C-41 (Imperative Dual-Field Gate Language) | PASS | "Do not fill any cell in the table until all three items are written:" — imperative prohibition form preserved |
| C-42 (Cell-Level Table-Fill Prohibition) | PASS | "Do not fill any cell in the table until all three items are written:" — unit is still "any cell" |
| C-43 (Triple Verbatim-Prohibition Clause in Exception Block) | PASS | Exception block triple-clause inherited from base |
| C-45 candidate (Phase Distribution Pre-Commitment) | PASS | Pre-fill PHASE DISTRIBUTION block with Phase 1/2/3 counts + total; verified at Step 4B constraint 0 |

**Score: 265/265**

---

### V-03 — Switching-Friction Minimum Count Gate

**Change**: Switching-Friction Gaps minimum upgraded from "at least one required, at least two recommended" to "minimum two required." Pre-count declaration gate (`SWITCHING-FRICTION COUNT: [N]`) required before any entry. Pass 2B gains count-match check.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-37 | PASS | Inherited from base; Step 4, Steps 1–6, 8 unchanged |
| C-38 (Dual-Field Step-4 Gate) | PASS | Step 4 unchanged from base; two labeled fields with "both items" gate |
| C-39 (Every-Assignment Scope Confirmation) | PASS | Preserved verbatim from base |
| C-40 (Exception Block Verbatim-Clause Instruction) | PASS | Exception block unchanged |
| C-41 (Imperative Dual-Field Gate Language) | PASS | Step 4 unchanged |
| C-42 (Cell-Level Table-Fill Prohibition) | PASS | Step 4 unchanged |
| C-43 (Triple Verbatim-Prohibition Clause in Exception Block) | PASS | Exception block inherited |
| C-04 (Gap Analysis Present and Structured) | PASS | Four sub-sections still present; count gate adds structure, does not remove sub-sections |
| C-29 (Dedicated Switching-Friction Gap Sub-Section with Competitor Field) | PASS | Sub-section still dedicated and separate; count gate is header-level addition |
| C-46 candidate (Switching-Friction Count Gate) | PASS | Pre-count declaration before entries; count-match verified at Pass 2B item 4 |

**Score: 265/265**

---

### V-04 — Combined (V-01 + V-02)

**Changes**: V-01's no-exception triple-clause + V-02's phase distribution pre-commitment gate. Distinct structural slots — no overlap. Cell-level gate ("any cell") retained; scope confirmation retained; exception block triple-clause retained.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-37 | PASS | Inherited from base; both axes are additive |
| C-38 (Dual-Field Step-4 Gate) | PASS | Three labeled fields (phase distribution + inference rule confirmed + verbatim anchor); both C-38-required fields present; gate prohibits filling until all three written |
| C-39 (Every-Assignment Scope Confirmation) | PASS | "Confirmation: the inference rule applies to every severity assignment in the table below." |
| C-40 (Exception Block Verbatim-Clause Instruction) | PASS | Inherited from base |
| C-41 (Imperative Dual-Field Gate Language) | PASS | "Do not fill any cell in the table until all three items are written:" — imperative form |
| C-42 (Cell-Level Table-Fill Prohibition) | PASS | "Do not fill any cell in the table until all three items are written:" — "any cell" unit |
| C-43 (Triple Verbatim-Prohibition Clause in Exception Block) | PASS | Inherited from base; V-01 axis does not touch exception block |
| C-44 candidate | PASS | No-exception paths carry triple-clause (V-01 axis) |
| C-45 candidate | PASS | Phase distribution pre-commitment block with count verification (V-02 axis) |

**Score: 265/265**

---

### V-05 — Full Synthesis (V-01 + V-02 + V-03)

**Changes**: All three R15 axes simultaneously. Three independent structural slots — no overlap between V-01 (no-exception path text), V-02 (Step 4 header + Step 4B), and V-03 (Step 7 Switching-Friction header + Pass 2B).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-37 | PASS | All three axes are additive; no removal of any base mechanism |
| C-38 (Dual-Field Step-4 Gate) | PASS | Three labeled fields including both required; gate prohibits cell-fill until all written |
| C-39 (Every-Assignment Scope Confirmation) | PASS | Scope confirmation statement preserved |
| C-40 (Exception Block Verbatim-Clause Instruction) | PASS | Exception block unchanged |
| C-41 (Imperative Dual-Field Gate Language) | PASS | Imperative prohibition preserved; "any cell" still governed |
| C-42 (Cell-Level Table-Fill Prohibition) | PASS | "Do not fill any cell in the table until all three items are written:" — "any cell" unit |
| C-43 (Triple Verbatim-Prohibition Clause in Exception Block) | PASS | Inherited from base; no axis touches exception block clauses |
| C-44 candidate | PASS | No-exception triple-clause (V-01 axis) |
| C-45 candidate | PASS | Phase distribution pre-commitment (V-02 axis) |
| C-46 candidate | PASS | Switching-friction count gate (V-03 axis) |

**Score: 265/265**

---

### Composite Scores — Ranked

| Variation | Score (v14) | C-44 cand. | C-45 cand. | C-46 cand. | Fails |
|-----------|-------------|-----------|-----------|-----------|-------|
| V-01 | 265/265 | PASS | -- | -- | none |
| V-02 | 265/265 | -- | PASS | -- | none |
| V-03 | 265/265 | -- | -- | PASS | none |
| V-04 | 265/265 | PASS | PASS | -- | none |
| V-05 | 265/265 | PASS | PASS | PASS | none |

All five variations inherit V-04 R14 without breaking any existing criterion. Under v14, all tie at ceiling.

---

### Excellence Signals

**Top-scoring variation**: V-05 (265/265 under v14; satisfies all three new candidate criteria simultaneously — only variation reaching above-ceiling on all three axes).

**Pattern 1 — Symmetric triple-clause propagation**: C-43 closed the condensation path in the exception block (rare path). V-01/V-04/V-05 close it in the no-exception path (common path — executes for Phase 1 on most runs). The pattern: every verbatim-retrieval instruction, at whatever frequency it executes, should carry all three prohibition clauses. The no-exception path is the *more important* target because it fires more often.

**Pattern 2 — Pre-commitment contract reuse**: The inference rule double-gate (C-34/C-38) demonstrates that a pre-fill declaration + post-fill verification creates a testable contract. V-02/V-04/V-05 apply the same structural pattern to phase distribution. V-03/V-05 apply it to switching-friction count. The excellence signal: any constraint that currently only has a post-hoc audit is a candidate for a pre-commitment gate using the same `DECLARE → FILL → VERIFY` structure.

**Pattern 3 — Additive instruction density without interference**: V-05 adds three independent requirement blocks across three structural slots (Step 4 header, Step 7 header, Pass 2B) without degrading any of the forty-three prior criteria. The pattern: slot-specific additions (each gate lives in exactly one named location) don't compound into interference — enabling criterion accumulation across rounds without regression.

---

```json
{"top_score": 265, "all_essential_pass": true, "new_patterns": ["Symmetric triple-clause propagation: close the condensation path at every verbatim-retrieval site, not just the exception path -- the no-exception path executes more often and warrants the same triple-clause gate", "Pre-commitment contract reuse: any constraint with only a post-hoc audit is a candidate for the DECLARE->FILL->VERIFY structure already proven by the inference rule double-gate", "Additive instruction density without interference: slot-specific additions across independent structural locations accumulate criterion coverage without causing regression on prior criteria"]}
```
