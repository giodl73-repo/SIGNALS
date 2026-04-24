# /quest:score — trace-state Round 4 (v19 rubric)

**Note**: Only V-01 and V-02 were supplied. V-03–V-05 scored as absent.

---

## V-01 Scorecard — Output Format axis

### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PASS** | Section 1 schema locks all three columns: `C-01a: Starting State`, `C-01b: Operation`, `C-01c: Ending State`; 5-row minimum enforced |
| C-02 | Precondition + Postcondition | **PASS** | `C-02a: Preconditions` and `C-02b: Postconditions` are explicit schema columns; "even if none" implicit via N/A rule |
| C-03 | Two+ invariants checked after every op | **PASS** | Section 2 requires ≥2 invariants; `Checked After Operation(s)` column is mandatory; no silent omission possible |
| C-04 | At least one labeled defect | **PASS** | Section 3 locks all four fields: type, triggering operation, reason, defect ID |
| C-05 | Domain plausibility | **PASS** | Finance Controller persona; example row uses `Invoice.DRAFT → PENDING_APPROVAL`; ledger vocabulary throughout |

**Essential: 60 / 60 — all pass**

### Recommended (30 pts)

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-06 | Consistent trace format | **PASS** | 10 | Locked table schema declared for every section; no free-form alternatives offered |
| C-07 | Non-trivial invariants | **PASS** | 10 | Section 2 explicitly bans generic structural rules: "not a generic structural rule like 'ID is not null'" — Finance-specific rule required |
| C-08 | Race condition analysis | **PASS** | 10 | Section 5 present with both orderings required; "symmetric" shortcut explicitly rejected |

**Recommended: 30 / 30**

### Aspirational (cap 10 pts, 2 pts each)

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-09 | Negative path trace | **PASS** | 2 | Section 4 mandates all four elements: invalid state, blocked op, unchanged state, named error |
| C-10 | Reachability annotation | **PASS** | 2 | Section 6 requires every omitted transition listed with rationale; "silent omissions do not qualify" named explicitly |
| C-11 | Inline criterion anchoring | **PASS** | 2 | Column headers carry IDs: `C-01a`, `C-01b`, `C-01c`, `C-02a`, `C-02b`, `C-03`, `C-07`, `C-13` — element-level, not section-level |
| C-12 | Symmetric interleaving | **PASS** | 2 | Section 5 schema has explicit A-before-B and B-before-A rows; "symmetric" shortcut rejection quoted verbatim |
| C-13 | Invariant derivation pipeline | **PASS** | 2 | `Derivation Source Row [C-13]` is a mandatory column in Section 2; C-13 requirement block explicitly states "declaring with no trace linkage does not satisfy C-13" |
| C-14 | Schema-level write-time enforcement | **PASS** | 2 | Column headers embed criterion IDs — filling any cell mechanically satisfies the criterion; compliance is structurally unavoidable, not instruction-dependent |
| C-15 | Example row with placeholder syntax | **PASS** | 2 | Section 1 includes a filled example row (`Invoice.DRAFT → PENDING_APPROVAL` with real postcondition) plus a `…` placeholder row; schema ambiguity eliminated before generation |
| C-16 | Hard no-prose-substitution constraint | **PASS** | 2 | `HARD RULE — NO PROSE SUBSTITUTIONS` block declared at prompt level; "violation invalidates the artifact" stated; closing reminder reinforces |

Earned: 8 × 2 = 16 → capped at **10 / 10**

### V-01 Composite: **100 / 100** ✓ Golden

---

## V-02 Scorecard — Role Sequence axis

### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PASS** | `Step N: State=[…] | Op=[…] | EndState=[…]` format present in all three expert passes |
| C-02 | Precondition + Postcondition | **PASS** | Each step template includes `Preconditions: …` and `Postconditions: …` lines |
| C-03 | Two+ invariants checked after every op | **PASS** | Each pass requires ≥2 invariants with `checked after steps:` annotation |
| C-04 | At least one labeled defect | **PASS** | Each pass has a `Defects Found` section; Synthesis has a consolidated defect register with type column |
| C-05 | Domain plausibility | **PASS** | Three named domains (Finance, Sales, CS) with role-specific vocabulary in each pass |

**Essential: 60 / 60 — all pass**

### Recommended (30 pts)

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-06 | Consistent trace format | **PASS** | 10 | Numbered step format `Step N: State=[…]` declared consistently across all three passes |
| C-07 | Non-trivial invariants | **PARTIAL** | 5 | Role-specific framing ("Finance business rules", "Sales pipeline rules", "SLA rules") implies non-triviality but no explicit guard against generic structural invariants like the "ID is not null" ban in V-01 |
| C-08 | Race condition analysis | **PASS** | 10 | Synthesis section requires both orderings (A before B / B before A); no symmetric shortcut permitted |

**Recommended: 25 / 30**

### Aspirational (cap 10 pts, 2 pts each)

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-09 | Negative path trace | **FAIL** | 0 | No negative path section anywhere in the prompt |
| C-10 | Reachability annotation | **FAIL** | 0 | No omitted transitions section |
| C-11 | Inline criterion anchoring | **FAIL** | 0 | No criterion IDs appear in field labels or schema elements |
| C-12 | Symmetric interleaving | **PASS** | 2 | Synthesis explicitly lists both orderings; format enforces it with two bullet lines |
| C-13 | Invariant derivation pipeline | **FAIL** | 0 | Invariants name "which steps they are checked after" but no cross-reference to trace rows as derivation sources |
| C-14 | Schema-level write-time enforcement | **FAIL** | 0 | No criterion IDs in column headers; compliance is instruction-dependent, not structurally enforced |
| C-15 | Example row with placeholder syntax | **FAIL** | 0 | Template shows `Step 1: State=[…]` as a format sample but no filled example row with placeholder anchors |
| C-16 | Hard no-prose-substitution constraint | **FAIL** | 0 | No prose ban declared; narrative fallback is implicitly permitted |

Earned: 1 × 2 = 2 → **2 / 10**

### V-02 Composite: **87 / 100** ✓ Golden (threshold met)

---

## Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite |
|------|-----------|-----------|-------------|--------------|-----------|
| 1 | V-01 | 60 / 60 | 30 / 30 | 10 / 10 | **100** |
| 2 | V-02 | 60 / 60 | 25 / 30 | 2 / 10 | **87** |
| — | V-03 | — | — | — | absent |
| — | V-04 | — | — | — | absent |
| — | V-05 | — | — | — | absent |

---

## Excellence Signals from V-01

**Signal 1 — Criterion IDs as column headers, not prose labels**
Every column header in V-01 embeds its criterion ID (`C-01a: Starting State`, `C-02b: Postconditions`, `C-13: Derivation Source Row`). This isn't annotation; it is schema. The act of filling a cell simultaneously satisfies the criterion. No cross-referencing required, no instruction-dependent compliance.

**Signal 2 — Filled example row with `…` placeholder anchors**
V-01's Section 1 includes a complete worked example row (`Invoice.DRAFT → PENDING_APPROVAL` with real preconditions and postconditions) followed immediately by a `…` row. This eliminates schema ambiguity before generation: every column has a visible contract. Empty-skeleton templates leave producers guessing; the filled example does not.

**Signal 3 — Hard declared rule with invalidation consequence**
V-01 names the constraint (`HARD RULE — NO PROSE SUBSTITUTIONS`), specifies the mechanism for compliance (`write "N/A" or "none"`), and attaches a consequence (`violation of this rule invalidates the artifact`). The closing reminder repeats the ban. This is a rule with teeth, not an instruction that can be quietly ignored. V-02 has neither the declaration nor the consequence.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["criterion-id-as-column-header produces structural compliance without cross-reference", "filled-example-row-with-placeholder-anchors eliminates schema ambiguity before generation", "hard-rule-with-invalidation-consequence prevents prose fallback where instruction alone would not"]}
```
