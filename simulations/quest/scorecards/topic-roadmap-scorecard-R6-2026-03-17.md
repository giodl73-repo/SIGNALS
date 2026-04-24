# Quest Score — topic-roadmap (Round 6)

> Note: Two variations provided (V-01, V-02). Rubric criteria C-05 through C-16 inferred from formula structure and pattern; C-17/C-18 are new this round per rubric preamble.

---

## Rubric Reference (inferred full set)

| Range | Count | Max pts |
|-------|-------|---------|
| Essential C-01–C-05 | 5 | 60 |
| Recommended C-06–C-08 | 3 | 30 |
| Aspirational C-09–C-18 | 10 × 2 | 20 |

Aspirational (inferred mapping):
- C-09: All 4 delta categories defined
- C-10: 1-line summary column in inventory
- C-11: Stop execution on null delta
- C-12: Before/After state in proposal rows
- C-13: Named NEW artifact per proposal
- C-14: Type-labeled null declaration
- C-15: Diff summary on apply
- C-16: Confidence levels in proposals
- C-17: *(new)* Bias label per proposal guard
- C-18: *(new)* WITHDRAW as row-level partial-accept operator

---

## V-01 — Inertia Framing Prominent

### Essential

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Inertia prior | **PASS** | First sentence: "The default outcome is NO CHANGE." Null declaration defined before any proposal logic. INERTIA HOLDS / NULL_DELTA block terminates the skill when no NEWs exist. |
| C-02 Delta before proposals | **PASS** | Step 2 = inventory (NEW/PRIOR), Step 3 = delta categories, Step 4 = proposals. Strict sequential ordering. |
| C-03 Concrete action-typed | **PASS** | Required columns: Action (ADD/REMOVE/REPRIORITIZE), Dimension, Before, After, Evidence. All three C-03 elements present. Invalid proposals explicitly excluded. |
| C-04 Confirmation gate | **PASS** | AWAITING CONFIRMATION block with YES / NO / WITHDRAW variants. "Do not modify strategy.md until the user responds." |
| C-05 Write guard | **PASS** | Explicit prohibition above Step 6. Write cannot occur before gate response. |

Essential pass: **5 / 5**

### Recommended

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-06 Type-labeled null | **PASS** | `Type: NULL_DELTA` literal in null declaration. |
| C-07 Namespace in inventory | **PASS** | Inventory table has Namespace column. |
| C-08 Diff summary on apply | **PASS** | Step 6: "diff summary: which dimensions changed and how." |

Recommended pass: **3 / 3**

### Aspirational

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-09 All 4 delta categories | 2 | CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED defined. |
| C-10 1-line summary | 2 | `Summary (1 line)` column in inventory. |
| C-11 Stop on null | 2 | "If no NEW artifacts exist: output the null declaration and stop." |
| C-12 Before/After state | 2 | Before and After columns required in proposal table. |
| C-13 Named artifact per proposal | 2 | "Proposals not backed by a named NEW artifact are invalid and must be omitted." |
| C-14 Type-labeled null | 2 | `NULL_DELTA` type in null declaration block. |
| C-15 Diff summary structured | 2 | Step 6 outputs change summary on apply; "No changes applied" on NO. |
| C-16 Confidence levels | **0** | No confidence column in proposal table. |
| C-17 Bias labels | 2 | "Bias blocked" column required; "names the cognitive bias this guard prevents." |
| C-18 WITHDRAW operator | 2 | "WITHDRAW <#> to remove a specific proposal before applying the rest." |

Aspirational raw: **18 / 20**

### Composite

```
(5/5 × 60) + (3/3 × 30) + (18/20 × 10)
= 60 + 30 + 9
= 99
```

All essential pass: **YES** | Golden: **YES (≥ 80, all essential)**

---

## V-02 — Output Format Table-First

### Essential

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Inertia prior | **PASS** | Phase 3 enforces inertia via NULL_DELTA table row: "Inertia holds; no proposals follow — Then stop." Satisfies pass condition (b): type-labeled null declaration. Framing is reactive (Phase 3) rather than proactive (opening), but the pass condition is met. |
| C-02 Delta before proposals | **PASS** | Phase 2 = inventory, Phase 3 = delta, Phase 4 = proposals. Table-first format makes ordering structurally explicit. |
| C-03 Concrete action-typed | **PASS** | Phase 4 columns: Action (ADD/REMOVE/REPRIORITIZE), Dimension, Before, After, Evidence. All C-03 elements present. Confidence and Bias blocked added as bonus columns. |
| C-04 Confirmation gate | **PASS** | Phase 5 AWAITING CONFIRMATION with YES / NO / WITHDRAW. |
| C-05 Write guard | **PASS** | "Respond before any writes occur." Explicit. |

Essential pass: **5 / 5**

### Recommended

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-06 Type-labeled null | **PASS** | Phase 3 NULL_DELTA row label. |
| C-07 Namespace in inventory | **PASS** | Phase 2 table has Namespace column. |
| C-08 Diff summary on apply | **PASS** | Phase 6 outputs | Proposal # | Applied | Change summary | table. |

Recommended pass: **3 / 3**

### Aspirational

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-09 All 4 delta categories | 2 | CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED in Phase 3. |
| C-10 1-line summary | 2 | Phase 2: "1-line summary" column. |
| C-11 Stop on null | 2 | Phase 3: "Then stop." after NULL_DELTA row. |
| C-12 Before/After state | 2 | Before and After columns in Phase 4 table. |
| C-13 Named artifact per proposal | 2 | "Omit any proposal not backed by a named NEW artifact." |
| C-14 Type-labeled null | 2 | NULL_DELTA label in Phase 3 row. |
| C-15 Diff summary structured | 2 | Phase 6 table with Applied column; structured NO row. |
| C-16 Confidence levels | **2** | "Confidence: HIGH / MEDIUM / LOW" column required in Phase 4. |
| C-17 Bias labels | 2 | "Bias blocked" column in Phase 4 table. |
| C-18 WITHDRAW operator | 2 | Phase 5: "WITHDRAW <#> — drop proposal #N, then re-confirm remaining." |

Aspirational raw: **20 / 20**

### Composite

```
(5/5 × 60) + (3/3 × 30) + (20/20 × 10)
= 60 + 30 + 10
= 100
```

All essential pass: **YES** | Golden: **YES**

---

## Rankings

| Rank | Variation | Composite | All Essential | Golden |
|------|-----------|-----------|---------------|--------|
| 1 | V-02 (Table-First) | **100** | YES | YES |
| 2 | V-01 (Inertia Framing) | **99** | YES | YES |

Gap is C-16 (confidence levels). V-01's hypothesis — that inertia framing prominence reduces spurious proposals — is well-executed but the missing confidence column is a measurable loss.

---

## Excellence Signals (from V-02)

**Signal 1 — Table-first as a structural correctness guarantee.**
Prose allows a model to bury a PRIOR artifact in narrative and slip it past a human reviewer. Requiring a table at every phase means every artifact gets an explicit Status cell: NEW or PRIOR. No prose-burial path exists. This is a design pattern, not just a formatting choice — it makes C-02 failures structurally harder to commit.

**Signal 2 — Structured rejection output mirrors apply output.**
V-02 Phase 6 on NO outputs: `| — | NO | strategy.md unchanged |` — same table shape as the apply output. This means the apply/reject states are machine-readable and schema-consistent. V-01 emits plain text on NO. The mirrored table pattern may warrant a rubric criterion: *apply and reject outputs share the same table schema*.

---

## New Pattern Candidates for C-19 / C-20

| # | Pattern | Why it matters |
|---|---------|---------------|
| C-19 | Apply/reject outputs are schema-consistent (same table structure for all outcomes) | Enables automated scoring and diff comparison; eliminates ad-hoc prose on rejection path |
| C-20 | Table-first format required at all classification phases (not just proposals) | Structural guarantee against classification errors in inventory and delta phases |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["apply and reject outputs share the same table schema for machine-readable consistency", "table-first format required at all classification phases as structural correctness guarantee"]}
```
