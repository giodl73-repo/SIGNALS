## trace-state — Round 9 Scoring (rubric v23)

---

### V-01 — Role Sequence: Finance → CS → Sales

#### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PASS** | Table columns: Starting State / Operation / Ending State present |
| C-02 | Preconditions + Postconditions | **PASS** | Columns present; nil-value instruction co-located at column header level |
| C-03 | Two+ domain-meaningful invariants | **PASS** | "declare at least two domain-meaningful invariants" before Pass 1 |
| C-04 | Labeled defect | **PASS** | Defect Section: Type / Triggering Operation / Reason |
| C-05 | Domain plausibility | **PASS** | Explicit business vocabulary list; generic states without business context disqualified |

**All essential: PASS → 60 pts**

#### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Consistent trace format | **PASS** | Uniform table throughout all three passes |
| C-07 | Non-trivial invariants | **PASS** | "real business rules, not structural data checks" + exclusion list |
| C-08 | Race condition analysis | **PASS** | "Name both operations and describe the conflict or resolution" |

**Recommended: 30 pts**

#### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **PASS** | Negative path section with all four elements; "confirm no mutation occurred" explicit |
| C-10 | FAIL | No reachability register |
| C-11 | FAIL | No criterion IDs in field labels |
| C-12 | FAIL | Single-ordering race analysis only |
| C-13 | FAIL | No trace row → invariant cross-reference |
| C-14 | FAIL | No schema-level criterion ID enforcement |
| C-15 | FAIL | No example row |
| C-16 | FAIL | No named prose ban |
| C-17 | **PASS** | "Minimum 5 rows per pass" |
| C-18 | **PASS** | Three named disqualifying patterns |
| C-19 | **PASS** | "invalidates the artifact" on floor violation |
| C-20 | FAIL | No positive qualifying example in invariant section |
| C-21 | FAIL | No anti-lazy-copy constraint in race section |
| C-22 | **PASS** | "write `none` if genuinely absent" in column header |
| C-23 | FAIL | No section-level invalidation clause |
| C-24 | FAIL | No example row present to guard |
| C-25 | FAIL | No cross-domain invariant register |
| C-26 | **PASS** | "Minimum 15 rows total across all three passes" |
| C-27 | **PASS** | Three disqualifying patterns in visible list structure |

Passing aspirational: C-09, C-17, C-18, C-19, C-22, C-26, C-27 = **7 → capped at 5 → 10 pts**

**V-01 Total: 60 + 30 + 10 = 100**

---

### V-02 — Output Format: Numbered Step Blocks with Schema-Level Criterion Embedding

#### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PASS** | `[C-01: Starting State]`, `[C-01: Ending State]`, `[C-01: Operation]` in step template |
| C-02 | Preconditions + Postconditions | **PASS** | `[C-02] Preconditions` and `[C-02] Postconditions` fields in every step |
| C-03 | Two+ domain-meaningful invariants | **PASS** | "declare at least two domain-meaningful invariants before Pass 1" |
| C-04 | Labeled defect | **PASS** | `[C-04] Defect` section with Type / Step Reference / Reason |
| C-05 | Domain plausibility | **PASS** | "Step content not anchored in one of these domains fails the domain plausibility check" |

**All essential: PASS → 60 pts**

#### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Consistent trace format | **PASS** | Numbered step blocks used consistently throughout all passes |
| C-07 | Non-trivial invariants | **PASS** | "must be real business rules" + three-pattern disqualified list |
| C-08 | Race condition analysis | **PASS** | `[C-08] Race Condition / Operations: ___ / Conflict or Resolution: ___` |

**Recommended: 30 pts**

#### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | FAIL | No negative path section |
| C-10 | FAIL | No reachability register |
| C-11 | **PASS** | Criterion IDs embedded as field labels (`[C-01]`, `[C-02]`, `[C-03]`, `[C-04]`, `[C-08]`) inside output format |
| C-12 | FAIL | Single-ordering race analysis only |
| C-13 | FAIL | No trace row → invariant cross-reference |
| C-14 | **PASS** | "The field labels carry criterion IDs. Filling any field satisfies the corresponding criterion for that step." — satisfaction unavoidable at write time |
| C-15 | **PASS** | EXAMPLE STEP with `___` anchors and `…` placeholders; all columns filled |
| C-16 | **PASS** | "No prose substitutions… is a format violation and invalidates the artifact" — named declared rule |
| C-17 | **PASS** | "Minimum 4 steps per pass" |
| C-18 | **PASS** | Three named disqualifying patterns |
| C-19 | **PASS** | "invalidates the artifact" on prose substitution |
| C-20 | **PASS** | Example step shows `Quote total must remain positive throughout lifecycle` — concrete positive qualifying example |
| C-21 | FAIL | No anti-lazy-copy constraint in race section |
| C-22 | FAIL | No nil-value instruction co-located at field level |
| C-23 | FAIL | No section-level invalidation clause |
| C-24 | **PASS** | "do not reproduce this block verbatim in your output; it is a reference anchor only" — co-located with example step |
| C-25 | FAIL | No cross-domain invariant aggregation register |
| C-26 | **PASS** | "Minimum 15 steps total across all three passes" |
| C-27 | **PASS** | Three disqualifying patterns in visible list structure |

Passing aspirational: C-11, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-24, C-26, C-27 = **11 → capped at 5 → 10 pts**

**V-02 Total: 60 + 30 + 10 = 100**

---

### V-03 — Lifecycle Emphasis: Phase Gates, Reachability, Cross-Pass Invariant Register

#### Essential (60 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PASS** | Table columns: Starting State / Operation / Ending State |
| C-02 | Preconditions + Postconditions | **PASS** | Columns present (no nil-value instruction — C-22 gap, but column presence satisfies essential) |
| C-03 | Two+ domain-meaningful invariants | **PASS** | "Declare at least two invariants per pass before running that pass" |
| C-04 | Labeled defect | **PASS** | "label at least one defect: type, row reference, reason" |
| C-05 | Domain plausibility | **PASS** | Three domains named; Invariant Register attributes invariants to named passes |

**All essential: PASS → 60 pts**

#### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Consistent trace format | **PASS** | Uniform table throughout all three passes |
| C-07 | Non-trivial invariants | **PASS** | Four-pattern disqualified list enforces non-triviality by exclusion |
| C-08 | Race condition analysis | **PASS** | Full race section requiring conflict or resolution; bidirectional analysis present |

**Recommended: 30 pts**

#### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | FAIL | No negative path section |
| C-10 | **PASS** | Reachability Register per pass; "Silent omissions invalidate this section"; explicit completeness-declaration escape hatch |
| C-11 | FAIL | No criterion IDs in field labels |
| C-12 | **PASS** | Both orderings explicitly required; "Ordering A→B: [describe fully]" and "Ordering B→A: [describe fully]" |
| C-13 | **PASS** | "Cross-reference every declared invariant to at least one transition row (e.g., 'CS Pass, Row 3')" |
| C-14 | FAIL | No schema-level criterion ID enforcement |
| C-15 | FAIL | No example row |
| C-16 | FAIL | No named prose ban |
| C-17 | **PASS** | "Minimum 5 rows per pass" |
| C-18 | **PASS** | Four named disqualifying patterns (including `"field is not empty"` — one additional beyond V-01/V-02) |
| C-19 | FAIL | No artifact-level invalidation clause; completeness floors declare no consequence |
| C-20 | FAIL | No positive qualifying example in invariant section |
| C-21 | **PASS** | "do not write 'same as above' or reference Ordering A" — declared inside race condition section |
| C-22 | FAIL | No nil-value instruction co-located at field level |
| C-23 | **PASS** | "Silent omissions invalidate this section" in Reachability Register — section-scoped consequence |
| C-24 | FAIL | No example row present to guard |
| C-25 | **PASS** | Named "Invariant Register" spanning all three passes; `Derived From` column with row-level cross-reference |
| C-26 | **PASS** | "Minimum 15 rows total across all three passes" |
| C-27 | **PASS** | Four disqualifying patterns in visible list structure |

Passing aspirational: C-10, C-12, C-13, C-17, C-18, C-21, C-23, C-25, C-26, C-27 = **10 → capped at 5 → 10 pts**

**V-03 Total: 60 + 30 + 10 = 100**

---

## Rankings

| Rank | Variation | Score | Essential | Recommended | Aspirational Qualifying |
|------|-----------|-------|-----------|-------------|------------------------|
| 1 | V-02 | **100** | 5/5 | 3/3 | 11 (deepest breadth) |
| 2 | V-03 | **100** | 5/5 | 3/3 | 10 |
| 3 | V-01 | **100** | 5/5 | 3/3 | 7 |

Three-way tie at 100. Composite scores are identical; V-02 ranks first on aspirational breadth (11 qualifying vs. 10 vs. 7). V-03 ranks second on aspirational coverage in distinct quadrants (lifecycle analysis, cross-pass synthesis, symmetric race analysis).

---

## Excellence Signals (V-02)

1. **Schema-level criterion embedding (C-14 + C-11 simultaneously)**: Writing `[C-01: Starting State] ___` in the field label makes criterion satisfaction structurally unavoidable. A filled step is a compliant step by construction — the strongest enforcement mechanism observed so far.

2. **Example step as positive invariant model (C-20)**: Embedding a concrete valid invariant (`Quote total must remain positive throughout lifecycle`) inside the example step provides a positive qualifying example through demonstration rather than instruction.

3. **Co-located anti-copy guard (C-24)**: "do not reproduce this block verbatim in your output; it is a reference anchor only" immediately adjacent to the example row prevents template contamination without relying on general-purpose instructions elsewhere.

4. **Artifact invalidation on format violation (C-19 via C-16)**: Coupling the prose ban to an invalidation consequence ("format violation and **invalidates the artifact**") creates enforcement with consequence rather than instruction without stakes.

---

## New Patterns (uncaptured by existing criteria)

**Pattern A — Mutation-confirmation assertion (V-01)**: The negative path section requires "Post-rejection state — must be unchanged; **confirm no mutation occurred**." This goes beyond C-09's "unchanged state" requirement by demanding an explicit confirmation assertion, making immutability of rejected operations affirmatively stated rather than inferred from the ending-state value.

**Pattern B — Completeness-declaration escape hatch (V-03)**: The Reachability Register reads: "A pass with no Reachability Register entry is valid only if all reachable transitions were traced and that fact is explicitly stated." This acknowledges full tracing as a legitimate outcome with its own declaration requirement — distinct from C-10 which governs omissions. A complete trace without omissions currently has no structural form to declare its completeness.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["mutation-confirmation assertion: negative path must explicitly confirm no mutation occurred, distinct from stating ending state is unchanged", "completeness-declaration escape hatch: reachability section accepts explicit full-trace declaration as alternative to listing omissions, giving complete traces a structural form"]}
```
