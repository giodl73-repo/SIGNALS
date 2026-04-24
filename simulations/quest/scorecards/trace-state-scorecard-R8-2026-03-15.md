## trace-state — Round 8 Scorecard (rubric v22)

---

### V-01 — Finance → CS → Sales (reversed domain sequence)

#### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PASS** | `Starting State [C-01a]` / `Operation [C-01b]` / `Ending State [C-01c]` columns in every pass table |
| C-02 | Precondition + Postcondition | **PASS** | `Preconditions [C-02a]` and `Postconditions [C-02b]` present in all three pass schemas |
| C-03 | Two+ domain-meaningful invariants | **PASS** | Invariants section in all three passes; "at least two invariants" required per pass |
| C-04 | At least one labeled defect | **PASS** | Defect Log with `Defect ID / Type / Triggering Operation / Reason`; one defect required |
| C-05 | Domain plausibility | **PASS** | Finance (`Invoice:Draft`), CS (`Case:Open`), Sales (`Opportunity:Qualified`) with recognizable ops |

**Essential: 5/5 — 60 pts**

#### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Consistent trace format | **PASS** | Tables used uniformly across all three passes |
| C-07 | Non-trivial invariants | **PASS** | Disqualifying pattern (`"ID is not null"`) named; qualifying pattern (`"Invoice total must remain positive…"`) named |
| C-08 | Race condition analysis | **PASS** | Ordering A→B and B→A tables present; conflict outcome required |

**Recommended: 3/3 — 30 pts**

#### Aspirational (cap 5 × 2 = 10 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Negative path trace | **PASS** | All four elements (Invalid Starting State, Blocked Operation, Unchanged Ending State, Named Error) |
| C-10 | Reachability annotation | **PASS** | Table present in all three passes; "Silent omissions invalidate this section" |
| C-11 | Inline criterion anchoring | **PASS** | Column headers carry IDs at element level: `[C-01a]`, `[C-02a]`, `[C-03]`, `[C-13]` |
| C-12 | Symmetric interleaving | **PASS** | "Ordering A → B" and "Ordering B → A" as independent tables; "Do not write 'same as above'" |
| C-13 | Invariant derivation pipeline | **PASS** | `Derived From (row refs) [C-13]` column; example `Pass 1 R2, Pass 1 R4` |
| C-14 | Schema-level write-time enforcement | **PASS** | Column IDs embedded in headers — filling `Starting State [C-01a]` mechanically satisfies C-01a; same for `[C-02a]`, `[C-22]`, `[C-03]`, `[C-13]` |
| C-15 | Example row with placeholder syntax | **PASS** | Filled example row in every pass with `…` anchors; start and end markers |
| C-16 | Hard no-prose-substitution constraint | **PASS** | "Hard constraint — violation invalidates this artifact: no prose substitutions" |
| C-17 | Quantified trace floor | **PASS** | "Minimum 5 rows per pass; at least 15 transition rows total" |
| C-18 | Named anti-example for invariant triviality | **PASS** | `"ID is not null"`, `"record exists"`, `"amount field is populated"` explicitly disqualified |
| C-19 | Artifact invalidation clause | **PASS** | "violation invalidates this artifact" at top-level constraint block |
| C-20 | Named qualifying example for invariant scope | **PASS** | `"Invoice total must remain positive from creation through payment…"` |
| C-21 | Anti-lazy-copy constraint in race section | **PASS** | Declared inside race section: "Do not write 'same as above' — each ordering must be self-contained and complete" |
| C-22 | Nil-value acknowledgment syntax | **PASS** | Co-located at column header: `Preconditions [C-02a] — write \`none\` if genuinely absent [C-22]` |
| C-23 | Section-level invalidation clause | **PASS** | "Silent omissions invalidate this section" in all three Reachability sections — scoped to section, independent of C-19 |
| C-24 | Anti-literal-copy guard on example rows | **PASS** | `"— Example row. Do not include this row in output. —"` co-located with each example row |
| C-25 | Cross-domain invariant aggregation register | **PASS** | "Consolidated Invariant Register [C-25]" spans all passes; `Derived From: Pass 1 R2, Pass 2 R1` cross-pass linkage |

**Aspirational: 17/17 eligible — cap 5 — 10 pts**

**V-01 Total: 100/100 — all_essential_pass: true**

---

### V-02 — Numbered-step list with named registers (no tables in transition body)

V-02 supplies constraint prose and names two mandatory structures (Invariant Register, Defect Log) but the format spec body is replaced with `placeholder`. The model receives rules but no schema, leaving generation without structural anchors.

#### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PARTIAL** | Numbered-step format prescribed but no schema defines the three required columns; derivable from convention, not from structure |
| C-02 | Precondition + Postcondition | **FAIL** | No precondition/postcondition fields specified anywhere in the visible prompt |
| C-03 | Two+ domain-meaningful invariants | **PARTIAL** | "Invariant Register" named as mandatory but no field spec, no count floor, no domain-rule constraint |
| C-04 | At least one labeled defect | **PARTIAL** | "Defect Log" named as mandatory but no field spec for type, triggering operation, reason |
| C-05 | Domain plausibility | **PASS** | Sales → CS → Finance domain sequence named |

**Essential: 1 pass / 3 partial / 1 fail — ~30 pts; all_essential_pass: false**

#### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Consistent trace format | **PARTIAL** | Numbered steps prescribed but no schema enforces uniformity across passes |
| C-07 | Non-trivial invariants | **FAIL** | No disqualifying or qualifying patterns stated |
| C-08 | Race condition analysis | **FAIL** | Not mentioned |

**Recommended: ~5 pts**

#### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **FAIL** | Not mentioned |
| C-10 | **FAIL** | Not mentioned |
| C-11 | **FAIL** | No criterion IDs in format |
| C-12 | **FAIL** | No race section |
| C-13 | **FAIL** | No derivation linkage |
| C-14 | **FAIL** | No schema slots exist |
| C-15 | **FAIL** | No example rows |
| C-16 | **PASS** | "No summary prose may substitute for any required field" |
| C-17 | **PASS** | "Minimum 5 operations per domain pass (15 operations total)" |
| C-18 | **FAIL** | No disqualifying pattern named |
| C-19 | **PASS** | "Omitting either invalidates the artifact" |
| C-20 | **FAIL** | No qualifying example |
| C-21 | **FAIL** | No race section |
| C-22 | **FAIL** | No nil-value instruction at field level |
| C-23 | **FAIL** | Only artifact-level clause; no section-scoped clause |
| C-24 | **FAIL** | No example rows to guard |
| C-25 | **PARTIAL** | "Aggregate findings into named registers" — structure implied but unnamed, no cross-pass derivation spec visible |

**Aspirational: C-16, C-17, C-19 pass = 6 pts**

**V-02 Total: ~41/100 — all_essential_pass: false**

---

### Ranking

| Rank | Variation | Score | All Essential |
|------|-----------|-------|---------------|
| 1 | V-01 (Finance → CS → Sales) | **100** | Yes |
| 2 | V-02 (Numbered-step + registers) | **~41** | No |

---

### Excellence Signals — V-01

1. **Domain sequence carries embedded rationale** — "Finance leads because its states are enumerable and its invariants are measurable, establishing the rigor baseline the other passes must match." The ordering is not merely prescribed; it is justified within the prompt, making the sequence instruction load-bearing rather than arbitrary. A model told *why* Finance leads is less likely to treat the three passes as interchangeable.

2. **Dual-anchor column headers** — A single column header satisfies two criteria simultaneously: `Preconditions [C-02a] — write \`none\` if genuinely absent [C-22]`. C-02a is anchored for structural completeness; C-22 is anchored for nil-value syntax. This compression removes the need for a separate nil-value instruction section.

3. **Per-pass proximate floor restatement** — "Fill minimum 5 rows for this pass" appears immediately after each pass's example row, making the floor constraint *local* to the generation point in addition to the global declaration at the top. Constraint proximity reduces the chance the model discards the rule when generating later passes.

4. **Example row sandwich** — Each example is bracketed by `— Example row. Do not include in output. —` and `— End example row. —`, creating an unambiguous span. The closing marker eliminates ambiguity about where the example ends and live generation begins.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Domain sequence rationale as load-bearing instruction — stating WHY a domain leads (e.g., Finance first because 'states are enumerable and invariants are measurable, establishing the rigor baseline') makes the ordering structural rather than arbitrary, reducing pass-transposition risk", "Per-pass proximate floor restatement — minimum row count declared again immediately after each example row ('Fill minimum 5 rows for this pass'), making the floor constraint local to each generation point in addition to the global declaration"]}
```
