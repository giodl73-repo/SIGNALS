## trace-state — Round 5 Scoring (rubric v20)

---

## V-01 — Output Format: Schema-Level Enforcement

### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PASS** | Table columns `Starting State [C-01a]`, `Operation [C-01b]`, `Ending State [C-01c]` structurally enforce all three elements |
| C-02 | Pre + Postconditions per op | **PASS** | `Preconditions [C-02a]` and `Postconditions [C-02b]` as labeled columns; Hard rule #3 forbids empty cells |
| C-03 | Two+ domain invariants checked after every op | **PASS** | `I-1 ✓/✗ [C-03]` and `I-2 ✓/✗ [C-03]` columns + Section 2 declaration table |
| C-04 | At least one labeled defect | **PASS** | Section 3 — Defect Catalog with ID, Type, Triggering Operation, Reason |
| C-05 | Domain plausibility | **PASS** | Example row grounds in Sales ("Opportunity: Qualified → Proposal"); domain selector explicit |

**Essential: 60/60**

### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Consistent trace format | **PASS** | Uniform table throughout all six sections |
| C-07 | Non-trivial invariants | **PASS** | C-18 bans "ID is not null" by name; example row shows `amount > 0`, `stage ∈ valid set` |
| C-08 | Race condition analysis | **PASS** | Section 5 present with both orderings |

**Recommended: 30/30**

### Aspirational (cap 10 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Negative path trace | **PASS** | Section 4 with all 4 required elements |
| C-10 | Reachability annotation | **PASS** | Section 6 — Omitted Transitions; note "Silent omissions do not qualify" |
| C-11 | Inline criterion anchoring | **PASS** | Column headers carry `[C-01a]`, `[C-01b]`, `[C-02a]`, `[C-02b]`, `[C-01c]`, `[C-03]`, `[C-04]` — IDs at field label level |
| C-12 | Symmetric interleaving | **PASS** | Section 5 has explicit "A → B ordering" and "B → A ordering" blocks |
| C-13 | Invariant derivation pipeline | **PASS** | Section 2 table has `Source row(s) in trace [C-13]` column; cross-reference is structural |
| C-14 | Schema-level write-time enforcement | **PASS** | Filling `Starting State [C-01a]` satisfies C-01a mechanically; cannot complete cell without satisfying criterion |
| C-15 | Example row with placeholder syntax | **PASS** | Row EX fully filled with real values; rows 1–5 use `…` anchors in every cell |
| C-16 | Hard no-prose-substitution constraint | **PASS** | Hard rule #1: "No prose substitutions for table columns. Every cell must be filled with structured content." |
| C-17 | Quantified trace floor | **PASS** | Hard rule #2: "at least 5 data rows (not counting example row EX)" declared inside schema |
| C-18 | Named anti-example for invariant triviality | **PASS** | Hard rule #4: "`ID is not null` … Structural database constraints are not domain invariants." |
| C-19 | Artifact invalidation clause | **PASS** | Preamble: "violation of any rule below **invalidates this artifact**"; Hard rule #4 also: "your artifact is **invalid** if you submit this" |

Earned: 11/11 → raw 22 pts → **capped at 10**

**V-01 composite: 60 + 30 + 10 = 100/100**

---

## V-02 — Role Sequence: Finance First

### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PASS** | Step 2 format includes Starting state, Operation name, Ending state per operation |
| C-02 | Pre + Postconditions per op | **PASS** | Step 2 fields include Preconditions and Postconditions; "(write `none` only if genuinely absent)" |
| C-03 | Two+ domain invariants checked after every op | **PASS** | Step 1 declares I-1, I-2; Step 2 includes "Invariants checked: I-1 [holds / violated], I-2 [holds / violated]" |
| C-04 | At least one labeled defect | **PASS** | Step 3 — Defect catalog with D-N, Type, Triggering operation, Reason |
| C-05 | Domain plausibility | **PASS** | Finance-first framing; qualifying examples explicitly grounded in invoices, expense reports, period-close |

**Essential: 60/60**

### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Consistent trace format | **PASS** | Numbered operation format used uniformly across all 5+ operations |
| C-07 | Non-trivial invariants | **PASS** | Step 1 gives Finance qualifying examples ("Invoice amount must remain positive after creation") and explicitly names disqualifying patterns |
| C-08 | Race condition analysis | **PASS** | Step 5 with Order 1 and Order 2; explicit "Do not write 'same as above'" ban |

**Recommended: 30/30**

### Aspirational (cap 10 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Negative path trace | **PASS** | Step 4 with all 4 elements |
| C-10 | Reachability annotation | **FAIL** | No section for omitted transitions with rationale |
| C-11 | Inline criterion anchoring | **FAIL** | Field labels ("Starting state:", "Preconditions:") carry no criterion IDs; section headers don't qualify |
| C-12 | Symmetric interleaving | **PASS** | "Order 1 — A executes first" and "Order 2 — B executes first" both explicitly described |
| C-13 | Invariant derivation pipeline | **PASS** | Step 6 — "For each invariant, note which trace operation revealed or confirmed it" with explicit cross-reference format |
| C-14 | Schema-level write-time enforcement | **FAIL** | Prose format has no criterion-labeled columns; compliance is instruction-dependent, not structurally unavoidable |
| C-15 | Example row with placeholder syntax | **FAIL** | Step 2 provides template placeholders but no filled example row with real values |
| C-16 | Hard no-prose-substitution constraint | **FAIL** | V-02 is itself a prose format; no ban declared; earning this would contradict the format choice |
| C-17 | Quantified trace floor | **PASS** | Step 2 header says "Trace at least 5 operations"; "Minimum 5 operations" at step foot |
| C-18 | Named anti-example for invariant triviality | **PASS** | Step 1: "Disqualifying examples — do not submit these: 'ID is not null' — database constraint, not a domain invariant" |
| C-19 | Artifact invalidation clause | **FAIL** | "Disqualifying examples — do not submit these" is a prohibition; no explicit consequence ("invalidates the artifact") stated |

Earned: C-09, C-12, C-13, C-17, C-18 = 5/11 → 10 pts → **exactly at cap**

**V-02 composite: 60 + 30 + 10 = 100/100**

---

## Ranking

| Rank | Variation | Composite | Essential | Recommended | Aspirational earned |
|------|-----------|-----------|-----------|-------------|---------------------|
| **1** | **V-01** | **100** | 60/60 | 30/30 | **11/11** (capped 10) |
| **2** | **V-02** | **100** | 60/60 | 30/30 | **5/11** (capped 10) |

Both hit 100. V-01 is structurally dominant — it earns 11 aspirational criteria against V-02's 5, missing only the cap to show separation. V-01 is the top variation.

---

## Excellence Signals from V-01

**1. Hard-rule preamble with artifact invalidation consequence**
The opening "Hard rules — violation of any rule below **invalidates this artifact**" is a single sentence that activates C-16, C-19, and the credibility of every subsequent constraint. V-02's "do not submit these" is a prohibition without teeth.

**2. Five aspirational criteria earned structurally via column headers**
Embedding `[C-01a]`, `[C-02a]`, `[C-03]`, `[C-04]` directly in column labels means filling any cell mechanically satisfies the criterion (C-11, C-14). This collapses rubric-compliance from instruction-following to schema-filling.

**3. Numeric floor declared inside the schema body, not in prose instructions**
"Minimum 5 data rows required" appears beneath the table itself, not in a separate instruction block. The floor travels with the format.

**4. Fully-filled example row anchors every column with a real value**
Row EX shows a complete, domain-grounded Sales example in every cell. Rows 1–5 then have `…` placeholders. The model cannot mistake what goes where.

**5. Named anti-example embedded at the constraint's point of use**
C-18 is satisfied by placing the banned pattern ("'ID is not null'") inside Hard rule #4 alongside the prohibition — not in a separate invariant-quality section. The disqualification is co-located with the enforcement mechanism.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["artifact-invalidation-consequence-clause-activates-C19-structurally", "schema-column-headers-with-criterion-IDs-make-compliance-unavoidable-at-write-time", "quantified-floor-declared-inside-schema-body-not-prose-instructions", "fully-filled-example-row-with-per-cell-placeholder-anchors-eliminates-schema-ambiguity", "named-anti-example-co-located-with-constraint-at-point-of-use"]}
```
