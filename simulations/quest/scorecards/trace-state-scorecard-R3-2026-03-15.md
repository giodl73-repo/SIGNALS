## trace-state — Round 3 Scoring (v19 rubric)

---

### V-01 — Output Format Axis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PASS** | Column headers `From [C-01b]`, `Operation [C-01c]`, `To [C-01d]` mandate all three elements per row |
| C-02 | Precondition + Postcondition | **PASS** | `Pre [C-02a]` and `Post [C-02b]` as required columns; empty is not permitted |
| C-03 | Two+ domain invariants checked per op | **PASS** | `[C-03: ≥2 per row]` embedded in header; quantified enforcement inside the label |
| C-04 | At least one labeled defect | **PASS** | Defect Log section with minimum-one-row rule and permitted type vocabulary |
| C-05 | Domain plausibility | **PASS** | Three-expert review (Sales / CS / Finance) sequentially validates domain vocabulary and invariants |
| C-06 | Consistent trace format | **PASS** | Hard rule: "every element must appear in a table cell"; format violation named explicitly |
| C-07 | Non-trivial invariants | **PASS** | "Must encode real domain rules — not generic structural facts" stated in Invariant Declaration |
| C-08 | Race condition analysis | **PASS** | Race Condition Analysis table; both orderings required |
| C-09 | Negative path trace (4 elements) | **PASS** | Negative Path section: `Invalid State`, `Blocked Operation`, `Unchanged State`, `Named Error` — all four columns explicit |
| C-10 | Reachability annotation | **PASS** | "Omitted Transitions" section; "Silent omissions do not qualify" stated |
| C-11 | Inline criterion anchoring | **PASS** | `[C-01a]`, `[C-01b]`, `[C-02a]`, `[C-03: ≥2 per row]` inside column headers — IDs are field labels |
| C-12 | Symmetric interleaving (both orderings) | **PASS** | "Writing 'symmetric' without describing both does not qualify" — explicit disqualifier |
| C-13 | Invariant derivation pipeline | **PASS** | Invariant Derivation Pass section with `← derived from rows N, N, N` cross-reference format |
| C-14 | Schema-level write-time enforcement | **PASS** | Criterion IDs in headers make it structurally impossible to fill a cell without satisfying the criterion; compliance is unavoidable at write time |
| C-15 | Example row with placeholder syntax | **PASS** | `Draft | SubmitQuote | UnderReview | …` filled row with `…` anchors in every column, explicit instruction to replace |
| C-16 | Hard no-prose-substitution constraint | **PASS** | "Hard rule: No prose substitutions… If you find yourself writing a paragraph where a row belongs, that is a format violation" — named, declared |

**Essential**: 5/5 PASS → 60 pts  
**Recommended**: 3/3 PASS → 30 pts  
**Aspirational**: 8/8 PASS → capped at 10 pts  
**V-01 Total: 100/100**

---

### V-02 — Lifecycle Emphasis Axis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | **PASS** | `(FromState, Operation) → ToState` tuple format + table columns `From`, `Op`, `To` |
| C-02 | Precondition + Postcondition | **PASS** | Phase 1 (preconditions) and Phase 3 (postconditions) mandatory per operation; "write `none`" if empty |
| C-03 | Two+ domain invariants checked per op | **PASS** | Phase 3 invariant check required per row; "declare at least two" stated |
| C-04 | At least one labeled defect | **PASS** | Phase 4 defect table with "minimum: manufacture one defect" instruction |
| C-05 | Domain plausibility | **PASS** | Three domain choices; non-trivial invariant examples are domain-specific |
| C-06 | Consistent trace format | **PASS** | Numbered step table for Phases 1–3, separate defect table for Phase 4 |
| C-07 | Non-trivial invariants | **PASS** | "Must encode real business rules — not generic structural facts" + three concrete domain examples |
| C-08 | Race condition analysis | **PASS** | "Ordering 1 / Ordering 2" explicitly required with both direction descriptions |
| C-09 | Negative path trace (4 elements) | **FAIL** | Rejected Transition routes to Phase 4, but defect table columns (`Type`, `Triggering Op`, `State at Anomaly`, `Reason`) do not map cleanly to the required four: "Unchanged State" is absent as a distinct column |
| C-10 | Reachability annotation | **FAIL** | No omitted transitions section; silent omissions remain silent |
| C-11 | Inline criterion anchoring | **FAIL** | Headers use Phase labels (`Phase 1: Pre`, `Phase 3: Post`) — not criterion IDs (C-01, C-02, etc.); scoring note disqualifies phase references |
| C-12 | Symmetric interleaving | **PASS** | "Ordering 1 / Ordering 2" structure with both explicitly required |
| C-13 | Invariant derivation pipeline | **FAIL** | No post-trace derivation pass; invariants are declared but never cross-referenced to originating rows |
| C-14 | Schema-level write-time enforcement | **FAIL** | Column headers name phases, not criteria; filling a cell does not mechanically satisfy a named criterion |
| C-15 | Example row with placeholder syntax | **FAIL** | Header row only; no filled example row with `…` anchors provided |
| C-16 | Hard no-prose-substitution constraint | **FAIL** | "Do not skip phases or merge them" is a sequence rule, not a named ban on narrative fallback; no explicit hard constraint declared |

**Essential**: 5/5 PASS → 60 pts  
**Recommended**: 3/3 PASS → 30 pts  
**Aspirational**: C-12 only = 2 pts  
**V-02 Total: 92/100**

---

### Rankings

| Rank | Variation | Score | All Essential | Aspirational Earned |
|------|-----------|-------|---------------|---------------------|
| 1 | V-01 | 100 | Yes | 8/8 (capped 10) |
| 2 | V-02 | 92 | Yes | 1/8 (2 pts) |

---

### Excellence Signals from V-01

**Signal 1 — Quantified enforcement inside the column label**
`[C-03: ≥2 per row]` is not just an ID anchor — it embeds a numeric minimum inside the header. The column cannot be filled without satisfying both the criterion and the count constraint. This is a stronger form of C-14 than bare ID presence.

**Signal 2 — Three sequential domain experts as a structural plausibility gate**
The Sales / CS / Finance expert review panel is distinct from any single criterion. Each expert (a) confirms domain vocabulary, (b) flags or approves one non-trivial invariant, (c) signs off or escalates. This pattern converts C-05 from a passive check into an active sign-off chain, and it surfaces domain invariant quality at the review stage rather than leaving it implicit.

**Signal 3 — Business Rule column in Invariant Declaration**
The Invariant Declaration table has `Invariant` and `Business Rule` as separate columns. This forces explicit articulation of the business justification at declaration time, before any trace row is written — not just at check time. The rubric (C-07) requires non-trivial invariants but doesn't currently require a declaration-time justification column.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["quantified enforcement embedded in column label (count constraint inside header ID anchor strengthens C-14 beyond bare ID presence)", "sequential multi-domain expert sign-off panel converts domain plausibility from passive check to active validation chain", "invariant declaration with separate Business Rule column forces domain justification at declaration time rather than check time"]}
```
