# trace-state Scoring Report — Round 2
## Rubric: v18 | Variations: V-01, V-02, V-03 (V-04 and V-05 not provided)

---

### V-01 — Output Format (Mandatory columnar schema)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | State Transition Completeness | PASS | Columns `[C-01a]` Starting State, `[C-01b]` Operation, `[C-01c]` Ending State in every row |
| C-02 | Pre + Postconditions | PASS | Columns `[C-02a]` Preconditions, `[C-02b]` Postconditions mechanically required by schema |
| C-03 | Two+ invariants checked | PASS | "Invariants Checked `[C-03]`" column with `INV-1 ✓, INV-2 ✓` example pattern in every row |
| C-04 | Labeled defect | PASS | DEFECT REGISTER section with Type, Triggering Operation, Reason columns |
| C-05 | Domain plausibility | PASS | "Finance state domain expert" explicit; "financial workflow contexts: approval stages, ledger entries, authorization levels, audit checkpoints" |
| C-06 | Consistent format | PASS | Uniform table enforced throughout; "no prose substitutions" explicitly banned |
| C-07 | Non-trivial invariants | PASS | "encode a real business rule, not a structural tautology" stated verbatim |
| C-08 | Race condition analysis | PASS | RACE CONDITION ANALYSIS section with `Ordering A→B:` / `Ordering B→A:` template slots |
| C-09 | Negative path trace | PASS | NEGATIVE PATH TRACE section: "invalid starting state → blocked operation → unchanged ending state → named error condition" — all four elements |
| C-10 | Reachability annotation | PASS | REACHABILITY ANNOTATION section; "Silent omissions do not qualify" enforcement |
| C-11 | Inline criterion anchoring | PASS | `[C-01a]`, `[C-01b]`, `[C-01c]`, `[C-02a]`, `[C-02b]`, `[C-03]`, `[C-07]`, `[C-13]` appear inside column headers |
| C-12 | Symmetric interleaving | PASS | Template slots `Ordering A→B: …` and `Ordering B→A: …` force both directions; asymmetry ruling required |
| C-13 | Invariant derivation pipeline | PASS | INVARIANT REGISTER has "Derived From Step `[C-13]`" column requiring explicit trace-row linkage at write time |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 5/5**
**Score: 60 + 30 + 10 = 100**

---

### V-02 — Role Sequence (Finance → CS → Sales)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | State Transition Completeness | PASS | "Starting state → Operation → Ending state" per-role; consolidated table in final output |
| C-02 | Pre + Postconditions | PASS | "Operation (with preconditions)" as prompt element; "ending state (with postconditions)" as element 3 |
| C-03 | Two+ invariants checked | PASS | "invariant check result" as fourth element per op; "at minimum two invariants" required from Finance |
| C-04 | Labeled defect | PASS | Finance role: "type, triggering operation, reason" — all three fields named |
| C-05 | Domain plausibility | PASS | Three domains covered by three expert roles |
| C-06 | Consistent format | PASS | "consistent numbered-step format" + single consolidated table at close |
| C-07 | Non-trivial invariants | PASS | "real financial rules (authorization thresholds, balance constraints, audit trail completeness)" named as targets |
| C-08 | Race condition analysis | PASS | CS role: "one concurrent operation pair… with BOTH orderings" |
| C-09 | Negative path trace | PASS | CS role: "invalid starting state, blocked operation, unchanged state, named error" — all four elements explicit |
| C-10 | Reachability annotation | PASS | Sales role: "List every transition NOT traced by any role. For each omission, give the rationale. Silent gaps do not qualify." |
| C-11 | Inline criterion anchoring | FAIL | No criterion IDs appear in field labels, column headers, or schema slots — prose-level only |
| C-12 | Symmetric interleaving | PASS | CS role: "BOTH orderings. State whether outcomes are symmetric." |
| C-13 | Invariant derivation pipeline | PASS | "Derive each invariant explicitly from an observed trace row — state which step made you recognize the rule" |

**Essential: 5/5 | Recommended: 3/3 | Aspirational: 4/5 (C-11 fails)**
**Score: 60 + 30 + 8 = 98**

---

### V-03 — Lifecycle Emphasis (Five-phase protocol, TRUNCATED after Phase 3)

Phases 4–5 missing. C-04, C-08, C-09, C-10, C-12 cannot be confirmed from visible content.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | State Transition Completeness | PASS | Phase 2: "Starting state → Operation → Ending state" per numbered step |
| C-02 | Pre + Postconditions | PASS | Phase 2: "preconditions · postconditions" required per operation |
| C-03 | Two+ invariants checked | PASS | Phase 2 gate: "INVARIANT CANDIDATES list has at least two entries" before Phase 3 begins |
| C-04 | Labeled defect | FAIL (truncated) | Not in Phases 1–3; presumably in Phase 4/5 |
| C-05 | Domain plausibility | PASS | "Sales / Customer Service / Finance — pick the lens" |
| C-06 | Consistent format | PASS | "consistent numbered-step format throughout" mandated in Phase 2 |
| C-07 | Non-trivial invariants | PARTIAL | Derivation from observed transitions implies non-trivial, but no anti-tautology guard stated |
| C-08 | Race condition | FAIL (truncated) | Not in visible phases |
| C-09 | Negative path trace | FAIL (truncated) | Not in visible phases |
| C-10 | Reachability annotation | FAIL (truncated) | Not in visible phases |
| C-11 | Inline criterion anchoring | FAIL | No criterion IDs in schema slots or column headers |
| C-12 | Symmetric interleaving | FAIL (truncated) | Not in visible phases |
| C-13 | Invariant derivation pipeline | PASS | Phase 2 "INVARIANT CANDIDATES" → Phase 3 promotion is an explicit step-grounded derivation pipeline |

**Essential: 4/5 (C-04 truncated) | Recommended: 1.5/3 | Aspirational: 1/5**
**Score: 48 + 15 + 2 = 65 (truncation-penalized; full prompt estimate: ~94)**

The phase-gate structure (gate: cannot proceed until X) is V-03's strongest design feature and would likely carry most remaining criteria in Phases 4–5.

---

## Ranking

| Rank | Variation | Score | All Essential Pass | Notes |
|------|-----------|-------|--------------------|-------|
| 1 | V-01 | 100 | Yes | Perfect coverage; schema-level enforcement |
| 2 | V-02 | 98 | Yes | Loses C-11 only |
| 3 | V-03 | 65* | No | Truncated; full prompt likely ~94 |
| — | V-04 | N/A | — | Not provided |
| — | V-05 | N/A | — | Not provided |

---

## Excellence Signals from V-01

1. **Schema-level criterion embedding** — criterion IDs in column headers ([C-01a], [C-03], [C-13]) make rubric satisfaction unavoidable at write time; the analyst cannot fill in a cell without satisfying the criterion. Distinct from prose instructions which can be ignored.

2. **Example row with placeholder syntax** — the filled `Step 1 / Step 2` rows with `…` anchors show exactly what belongs in each cell, eliminating schema ambiguity before the model starts generating.

3. **Explicit no-prose-substitution ban** — "no prose substitutions" as a hard constraint prevents fallback to narrative format that can satisfy tone but evade structural criteria.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["example row with placeholder syntax anchors schema before generation begins", "explicit no-prose-substitution ban prevents structural criterion evasion"]}
```
