## Quest Scorecard — crew-roles | Round 7 | Rubric v6

---

### Note on Input

Only **V-01** was provided in the variations block. V-02 through V-05 are referenced in the header but not present. Scoring proceeds for V-01 only; ranking is trivially V-01.

---

## V-01 — Baseline: Explicit Phase Boundaries

**Axis**: Lifecycle emphasis — numbered named phases with entry conditions, named work products, and explicit exit gates.

---

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | **PASS** | Phase 5 enumerates all five fields explicitly: `name`, `orientation`, `expertise`, `collaborates_with`, `scope`. |
| C-02 | Inertia-advocate present | **PASS** | Phase 2 pre-characterizes the inertia frame; Phase 5 constrains `orientation.verify` to reference at least 2 of the 3 Q-dimensions; the advocate is a first-class structural role. |
| C-03 | Correct output path | **PASS** | Phase 5: "Write each role file to `.craft/roles/{area}/{role-slug}.md`". |
| C-04 | Domain specificity | **PASS** | Phase 1 extracts domain vocabulary from input; Phase 5 requires every `expertise.relevance` to reference at least one Phase 1 term; generic language cannot pass vocabulary check. |
| C-05 | Minimum 3 roles | **PASS** | Phase 5: "Minimum 3 roles, including the inertia-advocate". |

**Essential result: 5/5 PASS**

---

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Lens actionability | **PASS** | Phase 5: "`orientation.verify` entries are questions ending with `?`; `orientation.simplify` entries are imperatives". |
| C-07 | Collaborates_with resolves | **PASS** | Phase 6 CHECK 2 is a named Orphan Reference Check: "For every `collaborates_with` value: does a file with that name exist in the registry?" — explicit blocking gate. |
| C-08 | Perspective diversity | **PASS** | Phase 5: "Roles span at least 3 distinct perspective categories; no category monopoly". |

**Recommended result: 3/3 PASS**

---

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Scope gradient | **PASS** | Phase 5: "Roles span at least 2 distinct scope values (e.g., `team`, `cross-team`, `org`); no homogeneous scope set". |
| C-10 | Inertia domain-grounded | **PASS** | Phase 2 Q1 requires current system name from Current-System bucket; Q2 requires migration cost term; Phase 3 fills both into named frame slots. Frame cannot contain generic language. |
| C-11 | Vocabulary-forced-field | **PASS** | Phase 1 produces bucketed vocabulary; Phase 5 gates `expertise.relevance` on Phase 1 term reference; CHECK 4 in Phase 6 enforces this structurally. |
| C-12 | Inertia pre-characterization | **PASS** | Phase 2 answers Q1/Q2/Q3 as named questions; Phase 5 requires verify questions to reference at least 2 of the 3 dimensions. |
| C-13 | Registry summary table | **PASS** | Phase 6 CHECK 1 requires full role registry summary table as named structural output. |
| C-14 | Scope-gradient-enforcement | **PASS** | Phase 4 is a dedicated Pre-Write Scope Audit that blocks writing until ≥2 distinct scope values are in the plan; structural gate, not soft instruction. Phase 6 CHECK 3 also verifies post-write. |
| C-15 | Verification-gate-phase | **PASS** | Phase 6 bundles all four checks into one named gate with explicit `GATE RESULT: PASS / BLOCKED (list failing checks)`. No check is scattered; all are co-located. |
| C-16 | Vocabulary-linked inertia Q&A | **PASS** | Phase 2 requires Q1 answer from Current-System bucket, Q2 from Migration-Cost bucket, Q3 from User-Habit bucket — each Q is structurally wired to its Phase 1 bucket, not just instructed to be. |
| C-17 | Pre-write scope audit | **PASS** | Phase 4 is a named phase whose exit condition is "≥2 distinct scope values" before any role file is written — prevention gate, not post-write correction. |
| C-18 | Vocabulary check in verification gate | **PASS** | Phase 6 CHECK 4: "For every role: does `expertise.relevance` reference a Phase 1 vocabulary term? List any roles failing this check." Gate PASS requires all four checks including this one. |
| C-19 | Inertia frame Q-slot template | **PASS** | Phase 3 shows the template verbatim with named placeholders `[Q1 current system]` and `[Q2 migration cost]`; slots must be filled, not described. |
| C-20 | Q-domain-aligned vocabulary distribution | **PASS** | Phase 2 explicitly assigns each Q to its domain bucket; same-term reuse across buckets fails the bucket constraint structurally (term can only appear in one bucket from Phase 1 exit condition). |
| C-21 | Bucketed vocabulary extraction | **PASS** | Phase 1 output format shows three named buckets (Current-System Terms, Migration-Cost Terms, User-Habit Terms) with explicit assignment; flat list cannot satisfy the exit condition. |
| C-22 | Domain-alignment audit table at Phase 2 exit | **PASS** | Phase 2 includes the structured audit table `Q-Number \| Term Used \| Expected Domain \| Match YES/NO`; any NO triggers replacement; all-YES is a hard exit condition. |
| C-23 | Frame Fill as phase-boundary artifact | **PASS** | Phase 3 is a standalone named phase (PHASE 3 — Frame Fill) that produces the completed frame string before Phase 5 (role writing); unfilled slots block Phase 3 exit; role writing cannot begin with an incomplete frame. |
| C-24 | Audit-table full re-evaluation after replacement | **PASS** | Phase 2 explicitly: "Restart the audit table from Q1 — do not re-score only the replaced row. Re-evaluate all three rows as a unit. Repeat until all three rows show YES." Incremental re-scoring is structurally prohibited. |
| C-25 | Frame-slot source citation in Frame Fill output | **PASS** | Phase 3 output format: "Q1 slot ← Phase 2 Q1: [verbatim Phase 2 Q1 answer]" and "Q2 slot ← Phase 2 Q2: [verbatim Phase 2 Q2 answer]". Binding verification is a named exit condition: "A slot populated from the wrong Q answer is a blocking error." |

**Aspirational result: 17/17 PASS**

---

### Score Computation

| Category | Weight | Score |
|----------|--------|-------|
| Essential (5 criteria) | 50 pts (10 each) | 50 / 50 |
| Recommended (3 criteria) | 40 pts (~13.3 each) | 40 / 40 |
| Aspirational (17/17 × 10) | 10 pts | 10 / 10 |
| **Total** | **100** | **100** |

---

### Ranking

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-01 | **100** | YES |

---

## Excellence Signals

V-01 is the first variation to achieve all 25 criteria. Two patterns emerge as genuine second-order gaps that v6 does not fully close:

**ES-1 — Verify-question source binding is soft, not cited**

Phase 3 establishes citation format for the frame string: `Q1 slot ← Phase 2 Q1: [verbatim]`. But Phase 5 says the inertia-advocate `orientation.verify` "must reference at least 2 of: current system, migration cost, user habit" — this is a semantic mandate, not a citation requirement. A verify question can satisfy this check by mentioning the dimension implicitly without tracing to a specific Phase 2 answer. The structural gap: the same slot-binding discipline applied to the frame string in Phase 3 is not applied to the verify question fields. A verify question could reference the Q1 dimension using a term from a different bucket without triggering any structural detection.

**ES-2 — Discarded audit table iterations are not preserved**

Phase 2 requires restarting from Q1 on any NO row, but the instruction is to "repeat until all three rows show YES" — the final table overwrites the failed attempt in output. When a replacement occurs, the replacement decision and the discarded attempt disappear. The final all-YES table is structurally complete, but there is no mechanism to verify that the replacement term was actually sourced from the correct bucket rather than inferred from context. A replacement term that passes its row in isolation but originates from outside the bucket is undetectable after the prior table is gone.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["verify-question source binding is a soft mandate not a citation requirement — the slot-citation discipline of Phase 3 Frame Fill does not extend to orientation.verify fields, allowing a verify question to reference a Q-dimension implicitly without a traceable Phase 2 answer binding", "discarded audit table iterations are not preserved in output — when Phase 2 triggers a restart, the failed attempt is overwritten and the replacement term source cannot be verified against the bucket after the fact"]}
```
