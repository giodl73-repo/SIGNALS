## trace-state R7 — Scoring Report (Rubric v21)

> **Note**: Both artifacts show `placeholder` as ground truth. Scoring evaluates prompt-design quality — whether the structural instructions reliably elicit criterion-satisfying outputs.

---

## V-01 — Hard Schema with Embedded Criterion IDs

### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | PASS | Table columns `Starting State [C-01a]`, `Operation [C-01b]`, `Ending State [C-01c]` structurally enforce all three elements in every row |
| C-02 | Precondition + Postcondition per operation | PASS | Dedicated columns with nil-value instruction at header level: `[C-02a — write \`none\` if genuinely absent]` |
| C-03 | Two+ domain-meaningful invariants | PASS | Section B requires ≥ 2 invariants with `Domain` and `Checked After Operations` columns; inline `Invariants Checked [C-03]` column in trace table seeds candidates |
| C-04 | At least one labeled defect | PASS | Section C hard schema: `Defect # | Type | Triggering Operation | Reason`; "no prose substitutions" enforced |
| C-05 | Domain plausibility | PASS | Opening role framing: "Finance / Customer Service / Sales state domain expert"; example row grounds in Finance lifecycle |

**Essential subtotal: 60 / 60**

---

### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Consistent trace format | PASS | Single schema with `Minimum 5 rows` enforces uniform table throughout; no mixed prose/table mode possible |
| C-07 | Non-trivial invariants | PASS | Section B names disqualifying pattern ("ID is not null") and qualifying example ("Invoice amount must remain positive after creation") |
| C-08 | Race condition analysis | PASS | Section D with full Ordering A→B and B→A table structures present |

**Recommended subtotal: 30 / 30**

---

### Aspirational (10 pts cap)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Negative path trace | PASS | Section E: `Invalid starting state | Blocked operation | State after rejection | Named error`; nil instruction on all fields |
| C-10 | Reachability annotation | PASS | Section F: "List every transition you omitted and why. Silent omissions **invalidate this section**." |
| C-11 | Inline criterion anchoring | PASS | Column headers carry IDs inside the output format itself: `[C-01]`, `[C-01a]`, `[C-02a]`, `[C-03]` — auditable at element level |
| C-12 | Symmetric interleaving | PASS | Both Ordering A→B and Ordering B→A have full table structures with identical fields; neither references the other |
| C-13 | Invariant derivation pipeline | PARTIAL | Trace table embeds invariant candidates per row (`Invariants Checked [C-03]`); Section B has `Checked After Operations` linking back to row numbers — cross-reference exists but framing is "validation direction" not "derivation direction"; pipeline is traceable, framing is weak |
| C-14 | Schema-level write-time enforcement | PASS | "Filling any cell mechanically satisfies the labeled criterion" declared in schema preamble; ID in column header makes compliance unavoidable at write time |
| C-15 | Example row with placeholder syntax | PASS | Filled example row with `…` anchors in every column; "do not include in output" guard prevents literal copy while preserving template |
| C-16 | Hard no-prose-substitution constraint | PASS | "Substituting prose for a structural column **invalidates the artifact**" declared as opening compliance rule |
| C-17 | Quantified trace floor | PASS | "Minimum 5 rows" declared inside Section A format spec |
| C-18 | Named anti-example for invariant triviality | PASS | Section B: "structural non-rules such as 'ID is not null', 'record exists', 'timestamp is set'" named as disqualifying |
| C-19 | Artifact invalidation clause | PASS | Opening rule: "invalidates the artifact — reviewers will reject it and request resubmission" — explicit consequence stated |
| C-20 | Named qualifying example for invariant scope | PASS | Section B: "Invoice amount must remain positive after creation — this is valid because it encodes a lifecycle constraint on a domain entity" — concrete positive model |
| C-21 | Anti-lazy-copy constraint in race section | PASS | Section D: "Do not write 'same as above' in the second ordering — each ordering must stand alone" declared inside race section |
| C-22 | Nil-value acknowledgment syntax | PASS | Preconditions column: `[C-02a — write \`none\` if genuinely absent]`; Section E: `[write \`none\` if genuinely absent]` at field level |

**Aspirational earned**: 13 clear PASS + 1 PARTIAL = 13 qualifying  
**Aspirational score**: min(13 × 2, 10) = **10 / 10**

**V-01 Composite: 60 + 30 + 10 = 100**  
**Golden threshold**: PASS (all essential + composite ≥ 80)

---

## V-02 — Role Sequence: Finance → CS → Sales

### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | PASS | Each pass table has `Starting State | Operation | Ending State`; three-pass structure covers all domains |
| C-02 | Precondition + Postcondition per operation | PASS | Table columns include `Preconditions [write \`none\` if genuinely absent]` and `Postconditions [write \`none\` if genuinely absent]` with nil instruction at header level |
| C-03 | Two+ domain-meaningful invariants | PASS | Consolidated Invariant Register requires minimum 2 with explicit derivation linkage column |
| C-04 | At least one labeled defect | PASS | Defect Log section with `Type | Triggering Operation | Reason` table; type options enumerated |
| C-05 | Domain plausibility | PASS | Three explicit domain passes with domain-appropriate context clues: monetary lifecycle (Finance), SLA/escalation (CS), opportunity stages/quota (Sales) |

**Essential subtotal: 60 / 60**

---

### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Consistent trace format | PASS | "Same format as Pass 1" instruction enforces uniform table structure across all three passes |
| C-07 | Non-trivial invariants | PASS | Pass 1 names disqualifying patterns ("ID is not null", "record exists") and qualifying example ("Invoice amount must remain positive after creation") |
| C-08 | Race condition analysis | PASS | Race section with both-orderings instruction present; "Describe both orderings in full and independently" |

**Recommended subtotal: 30 / 30**

---

### Aspirational (10 pts cap)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Negative path trace | FAIL | No negative path section; rejected operations not addressed |
| C-10 | Reachability annotation | FAIL | No reachability section; omitted transitions not required |
| C-11 | Inline criterion anchoring | FAIL | No criterion IDs embedded in column headers or output format elements |
| C-12 | Symmetric interleaving | PASS | "Describe both orderings in full and independently — written independently, not by reference to the above" with explicit A→B and B→A labels |
| C-13 | Invariant derivation pipeline | PASS | Consolidated Invariant Register has `Derived From (row refs)` column with example `Pass 1 R2, Pass 2 R1` — explicit bidirectional derivation linkage; strongest C-13 support across both variations |
| C-14 | Schema-level write-time enforcement | FAIL | No embedded criterion IDs in schema headers; compliance is instruction-dependent, not structurally unavoidable |
| C-15 | Example row with placeholder syntax | FAIL | No filled example row provided in any pass |
| C-16 | Hard no-prose-substitution constraint | FAIL | No general no-prose-substitution rule; tables presented without explicit invalidation consequence |
| C-17 | Quantified trace floor | PASS | "Minimum 3 Finance operations", "Minimum 3 CS operations", "Minimum 3 Sales operations" — numeric floors declared inside format spec |
| C-18 | Named anti-example for invariant triviality | PASS | Pass 1: "Do not write structural properties ('ID is not null', 'record exists')" named as disqualifying |
| C-19 | Artifact invalidation clause | FAIL | No constraint carries explicit "invalidates the artifact" consequence language |
| C-20 | Named qualifying example for invariant scope | PASS | Pass 1: "Invoice amount must remain positive after creation" named as valid qualifying example |
| C-21 | Anti-lazy-copy constraint in race section | PASS | Race section: "Do not write 'same as above' or refer the second ordering to the first" declared inside race condition instructions |
| C-22 | Nil-value acknowledgment syntax | PASS | Preconditions/Postconditions column headers carry `[write \`none\` if genuinely absent]`; cross-domain invariant field carries `write \`none\` — no cross-domain invariant applies (do not leave blank)` |

**Aspirational earned**: 7 PASS  
**Aspirational score**: min(7 × 2, 10) = **10 / 10**

**V-02 Composite: 60 + 30 + 10 = 100**  
**Golden threshold**: PASS (all essential + composite ≥ 80)

---

## Summary Table

| Variation | Essential | Recommended | Aspirational Criteria | Aspirational Pts | Composite | Golden |
|-----------|-----------|-------------|----------------------|------------------|-----------|--------|
| V-01 | 60 | 30 | 13 / 14 | 10 | **100** | PASS |
| V-02 | 60 | 30 | 7 / 14 | 10 | **100** | PASS |

**Ranking**: V-01 ≥ V-02 (tied at 100; V-01 superior in structural coverage and robustness)

---

## Excellence Signals from V-01

**1. Pre-schema invalidation framing**
The compliance rule appears *before* the schema, not inside a section. Declaring the consequence ("invalidates the artifact") before presenting the structure primes compliance as self-protection rather than instruction-following. Models treat the invalidation threat as ambient context while filling each cell.

**2. Example row with explicit exclusion guard**
The "do not include in output" instruction on the example row solves a structural tension: example rows help models understand cell content but also invite literal copying. The exclusion guard preserves template utility while preventing contamination of the output.

**3. Criterion ID at field label granularity (not section level)**
Column headers like `Preconditions [C-02a — write \`none\` if genuinely absent]` pack three things into one label: criterion ID, nil-value instruction, and the field name. This eliminates the need for cross-referencing — compliance evidence, format instruction, and semantic meaning coexist at the site where the model writes the value.

**4. Nil-value syntax co-located with optional fields (C-22)**
Rather than a preamble note about empty cells, V-01 embeds `write \`none\` if genuinely absent` directly in the column header of every field where absence is legitimate. This prevents the ambiguity between "blank because omitted" and "blank because none applies" at the exact point of entry.

**Notable from V-02 only — C-13 derivation direction**
V-02's Consolidated Invariant Register uses `Derived From (row refs)` rather than V-01's `Checked After Operations`. The derivation framing ("this invariant came from Pass 1 R2") is structurally stronger for C-13 than the validation framing ("this invariant is checked after Op 1, Op 3"). Worth backporting to the hard-schema format.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Pre-schema invalidation framing — placing the consequence clause before the schema body primes compliance-as-self-protection rather than instruction-following", "Example-row exclusion instruction — 'do not include in output' preserves template utility while blocking literal copy contamination of output", "Derivation-direction framing for C-13 — 'Derived From (row refs)' column in invariant register is structurally stronger than 'Checked After Operations' for satisfying the derivation pipeline criterion"]}
```
