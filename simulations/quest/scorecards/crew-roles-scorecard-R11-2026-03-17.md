Now I have all the material needed. Let me score all 5 variations against rubric v6.

**Scoring setup:**
- V-01 = prompt variation ("Lifecycle emphasis") — confirmed as R7 V-01 baseline (R8 header states "R7 V-01 scored 100/100 against rubric v6")
- V-02 = R8 V-01 (Verify-question source citation, single axis)
- V-03 = R8 V-02 (Audit iteration log, single axis)
- V-04 = R8 V-03 (Inertia-first sequence, single axis)
- V-05 = R8 V-04 (ES-1 + ES-2 combined, two-axis)

**Composite score formula:**
- Essential: all 5 PASS → 60 pts; any FAIL → 0
- Recommended: PASS=10, PARTIAL=5, FAIL=0 per criterion → max 30
- Aspirational: (pass + 0.5×partial) / 17 × 10 → max 10
- Maximum: 100

---

# crew-roles — Quest Score Round 11 — Rubric v6

---

## V-01 — Lifecycle Emphasis (R7 baseline)

**Design:** 6-phase skill: Bucketed Vocabulary → Inertia Pre-char + Audit → Frame Fill → Pre-write Scope Audit → Role Writing → Verification Gate. Each phase has explicit entry/exit conditions with blocking language.

### Essential

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | Phase 5 template mandates name, orientation (frame/verify/simplify), expertise (depth/relevance), collaborates_with, scope |
| C-02 | Inertia-advocate present | PASS | Phase 5 writes inertia-advocate using Phase 3 completed frame; orientation.frame is non-generic (Phase 3 Q-slot template filled with verbatim answers) |
| C-03 | Correct output path | PASS | Intro explicitly states `.craft/roles/{area}/` |
| C-04 | Domain specificity | PASS | Phase 5: expertise.relevance must reference at least one Phase 1 vocabulary term |
| C-05 | Minimum 3 roles | PASS | Phase 5: minimum 3 roles spanning 3 distinct perspective categories |

All 5 essential PASS → **60 pts**

### Recommended

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Lens actionability | PASS | Phase 5 template: verify items end in `?`; simplify items are imperatives (Remove/Defer/Collapse/Merge) |
| C-07 | collaborates_with resolves | PASS | Phase 6 CHECK 2: orphan reference resolution gate; unresolved names are flagged and must be resolved before PASS |
| C-08 | Perspective diversity | PASS | Phase 5: minimum 3 distinct perspective categories (product, technical, inertia, domain-specialist) |

All 3 recommended PASS → **30 pts**

### Aspirational

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Scope gradient | PASS | Phase 4 scope audit + Phase 6 CHECK 3 both enforce 2+ distinct scope values |
| C-10 | Inertia domain-grounded | PASS | Phase 2 Q1 names specific system from Bucket A; Phase 3 frame uses verbatim Phase 2 answers |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 extracts three named buckets; Phase 5 mandates expertise.relevance references a Phase 1 term |
| C-12 | Inertia pre-characterization | PASS | Phase 2 answers Q1/Q2/Q3 explicitly before writing inertia-advocate |
| C-13 | Registry summary table | PASS | Phase 6 CHECK 1 produces Role/Frame/Scope/Collaborates-With table |
| C-14 | Scope-gradient-enforcement | PASS | Phase 4 is a dedicated blocking gate: "Do not begin writing role files until at least 2 distinct scope values appear in the plan" |
| C-15 | Verification-gate-phase | PASS | Phase 6 "VERIFICATION GATE" bundles all 4 checks; each must declare PASS sequentially; "VERIFICATION GATE: PASS" only when all 4 pass |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Phase 2 bucket structure structurally wires Q1→Bucket A, Q2→Bucket B, Q3→Bucket C; audit table enforces domain alignment |
| C-17 | Pre-write scope audit | PASS | Phase 4 is a dedicated pre-write gate; writing is explicitly blocked until SCOPE AUDIT passes |
| C-18 | Vocabulary check in gate | PASS | Phase 6 CHECK 4: vocabulary coverage check; gate cannot PASS without this check |
| C-19 | Inertia frame Q-slot template | PASS | Phase 3 template: "[Q1 current system]", "[Q2 migration cost]", "[Q3 user habit]" — named placeholders that must be filled |
| C-20 | Q-domain-aligned vocab distribution | PASS | Phase 1 three distinct buckets; Phase 2 Q1 draws from Bucket A only, Q2 from B only, Q3 from C only; cross-bucket selection caught by audit table |
| C-21 | Bucketed vocabulary extraction | PASS | Phase 1 produces three named Q-domain buckets: Bucket A (Current-System), B (Migration-Cost), C (User-Habit) |
| C-22 | Domain-alignment audit table | PASS | Phase 2 produces structured audit table gating Phase 2 exit; any NO triggers replacement |
| C-23 | Frame Fill as phase-boundary artifact | PASS | Phase 3 "FRAME FILL" is a dedicated named phase that produces the frame string before Phase 5 (role writing) |
| C-24 | Audit-table full re-evaluation | PASS | Phase 2: "re-evaluation restarts from row 1 rather than re-scoring only the replaced row... evaluated as a unit, not per-row" |
| C-25 | Frame-slot source citation | PASS | Phase 3: Q1 slot ← Phase 2 Q1: [verbatim], Q2 slot ← Phase 2 Q2: [verbatim], Q3 slot ← Phase 2 Q3: [verbatim]; slot-binding verification: CHECK [PASS/FAIL] per slot |

All 17 aspirational PASS → 17/17 × 10 = **10 pts**

**V-01 Total: 100/100**

---

## V-02 — Verify-Question Source Citation (R8 V-01, single axis: ES-1)

**Design:** Extends V-01 by requiring each inertia-advocate `orientation.verify` question to carry a `[Q: Q1|Q2|Q3]` annotation binding it to its Phase 2 source. Phase 6 adds CHECK 5 (Verify-Question Citation Coverage) validating annotation-dimension matching.

### Essential

All 5 PASS — same structural basis as V-01. Phase 5 template, output path, inertia-advocate, and role count requirements unchanged. → **60 pts**

### Recommended

All 3 PASS — Phase 6 orphan check (C-07), perspective diversity enforced (C-08), lens actionability in template (C-06). → **30 pts**

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 4 scope audit + Phase 6 CHECK 3 |
| C-10 | PASS | Phase 2 Q1 names specific system; frame verbatim from Phase 3 |
| C-11 | PASS | Phase 1 bucketed vocab; Phase 5 expertise.relevance references Phase 1 term |
| C-12 | PASS | Phase 2 Q1/Q2/Q3 answered before writing |
| C-13 | PASS | Phase 6 CHECK 1 registry summary table |
| C-14 | PASS | Phase 4 pre-write scope gate blocks writing |
| C-15 | PASS | Phase 6 "VERIFICATION GATE" — 5 checks bundled; all must PASS |
| C-16 | PASS | Three buckets + per-answer `[vocab: {term}]` annotation enforces Q-vocab wiring |
| C-17 | PASS | Phase 4 dedicated pre-write scope audit |
| C-18 | PASS | Phase 6 CHECK 4 vocabulary coverage in gate |
| C-19 | PASS | Phase 3 frame template with named Q-slot placeholders |
| C-20 | PASS | Three buckets enforce per-Q domain isolation; same-term reuse across Q1/Q2/Q3 blocked by bucket assignment |
| C-21 | PASS | Phase 1 three named buckets: Current-System, Migration-Cost, User-Habit |
| C-22 | PASS | Phase 2 audit table gates Phase 2 exit |
| C-23 | PASS | Phase 3 FRAME FILL is dedicated phase before Phase 5 role writing |
| C-24 | PASS | Phase 2 restart protocol: "restart the audit table from Q1 — do not re-score only the replaced row. Evaluate all three rows simultaneously as a unit" |
| C-25 | PASS | Phase 3 Frame Fill: Q1/Q2/Q3 slot citations with slot-binding verification per slot |

All 17 aspirational PASS → **10 pts**

**V-02 Total: 100/100**

**Beyond-v6 addition:** Phase 5 inertia-advocate verify format: `{question ending in ?} [Q: Q1|Q2|Q3]`; Phase 6 CHECK 5 validates annotation-dimension binding; citation mismatch or absent annotation is a blocking gate failure.

---

## V-03 — Audit Iteration Log (R8 V-02, single axis: ES-2)

**Design:** Extends V-01 by numbering and preserving ALL Phase 2 audit attempt blocks in output. Each failed ATTEMPT block records replacement decision with old term, new term, and bucket-confirmed provenance. Convergence is declared after the final all-YES attempt; prior blocks are not deleted.

### Essential

All 5 PASS — same structural basis. → **60 pts**

### Recommended

All 3 PASS → **30 pts**

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 4 scope audit + Phase 6 CHECK 3 |
| C-10 | PASS | Q1 names specific system; frame verbatim |
| C-11 | PASS | Phase 1 bucketed vocab; expertise references Phase 1 term |
| C-12 | PASS | Phase 2 Q1/Q2/Q3 answered explicitly |
| C-13 | PASS | Phase 6 CHECK 1 registry table |
| C-14 | PASS | Phase 4 pre-write scope gate |
| C-15 | PASS | Phase 6 VERIFICATION GATE bundles all 4 checks |
| C-16 | PASS | Three buckets + `[vocab: {term}]` format on Q answers |
| C-17 | PASS | Phase 4 dedicated pre-write scope audit |
| C-18 | PASS | Phase 6 CHECK 4 vocabulary coverage |
| C-19 | PASS | Phase 3 frame template with named Q-slot placeholders |
| C-20 | PASS | Three buckets enforce Q-domain isolation |
| C-21 | PASS | Phase 1 three named buckets |
| C-22 | PASS | Phase 2 audit table with all-YES exit gate |
| C-23 | PASS | Phase 3 FRAME FILL dedicated phase |
| C-24 | PASS | Phase 2 iteration log: "Re-evaluate all three Q-answers starting from Q1"; numbered attempt blocks each evaluate all three rows from row 1 |
| C-25 | PASS | Phase 3 Frame Fill: Q1/Q2/Q3 slot citations; convergence Q answers cited verbatim |

All 17 aspirational PASS → **10 pts**

**V-03 Total: 100/100**

**Beyond-v6 addition:** Numbered ATTEMPT blocks preserve replacement history; each replacement records `"{old-term}" → "{new-term}" from [bucket name]. Basis: [one-line confirmation]` — replacement term's bucket origin verifiable after convergence, not just that a restart occurred.

---

## V-04 — Inertia-First Sequence (R8 V-03, single axis)

**Design:** 7-phase. Inverts standard sequence: Phase 1 = Current-System Identification (Q1 anchor established first), Phase 2 = Anchored Vocabulary Extraction (buckets populated using Q1 as the lens), Phase 3 = Q2/Q3 Completion + Audit, Phase 4 = Frame Fill, Phase 5 = Pre-write Scope Audit, Phase 6 = Write Role Files, Phase 7 = Verification Gate.

### Essential

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 6 template mandates all 5 fields |
| C-02 | PASS | Phase 6 inertia-advocate with Phase 4 frame verbatim |
| C-03 | PASS | `.craft/roles/{area}/` in intro |
| C-04 | PASS | Phase 6: expertise.relevance references Phase 2 vocabulary term anchored to Q1 system |
| C-05 | PASS | Phase 6: minimum 3 roles, 3 perspective categories |

→ **60 pts**

### Recommended

All 3 PASS → **30 pts**

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 5 scope audit + Phase 7 CHECK 3 |
| C-10 | PASS | Phase 1 names specific Q1 system as proper noun; Phase 4 frame uses Phase 3 verbatim answers |
| C-11 | PASS | Phase 2 anchored vocabulary; Phase 6 expertise.relevance references Phase 2 term |
| C-12 | PASS | Phase 3 answers Q1 (from Phase 1), Q2, Q3 explicitly before writing |
| C-13 | PASS | Phase 7 CHECK 1 registry table |
| C-14 | PASS | Phase 5 pre-write scope gate blocks writing |
| C-15 | PASS | Phase 7 VERIFICATION GATE bundles all 4 checks |
| C-16 | PASS | Phase 2 anchored vocabulary buckets + `[vocab: {term}]` on Q2/Q3 answers; Q1 carries Current-System term from Phase 1 |
| C-17 | PASS | Phase 5 dedicated pre-write scope audit |
| C-18 | PASS | Phase 7 CHECK 4 vocabulary coverage in gate |
| C-19 | PASS | Phase 4 frame template: "Teams using [Q1 current system] have [Q2 migration cost] invested. Ask whether this change is worth [Q3 user habit] disruption..." |
| C-20 | PASS | Anchored buckets: Q1-anchored Current-System, Q1-anchored Migration-Cost, Q1-anchored User-Habit; cross-bucket selection blocked by Phase 3 audit |
| C-21 | PASS | Phase 2 three named buckets: Current-System Terms, Migration-Cost Terms, User-Habit Terms |
| C-22 | PASS | Phase 3 audit table; restart from Q1; all three rows must be YES |
| C-23 | PASS | Phase 4 FRAME FILL is dedicated named phase before Phase 6 role writing |
| C-24 | PASS | Phase 3: "restart the audit table from Q1... Evaluate all three rows as a unit. Repeat until all YES" |
| C-25 | PASS | Phase 4: "Q1 slot ← Phase 1 / Phase 3 Q1: [verbatim Q1 answer]", "Q2 slot ← Phase 3 Q2...", "Q3 slot ← Phase 3 Q3..." with slot-binding verification |

All 17 aspirational PASS → **10 pts**

**V-04 Total: 100/100**

**Beyond-v6 addition:** Q1 anchor established in Phase 1 before vocabulary extraction; Phase 2 buckets populated using Q1 as the lens ("not generic domain vocabulary — terms that specifically describe what Q1 is"). Prevents abstract vocabulary drift where domain-relevant terms appear in buckets without being anchored to the specific status-quo system.

---

## V-05 — ES-1 + ES-2 Combined (R8 V-04, two-axis)

**Design:** 6-phase synthesis of V-02 (verify citations) and V-03 (iteration log). Phase 2 has audit iteration log with numbered blocks preserved. Phase 5 inertia-advocate verify questions carry `[Q:]` annotations. Phase 6 has 5 checks including CHECK 5 (Verify-Question Citation Coverage).

### Essential

All 5 PASS → **60 pts**

### Recommended

All 3 PASS → **30 pts**

### Aspirational

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 4 scope audit + Phase 6 CHECK 3 |
| C-10 | PASS | Q1 names specific system; frame verbatim from Phase 3 |
| C-11 | PASS | Phase 1 bucketed vocab; expertise references Phase 1 term |
| C-12 | PASS | Phase 2 Q1/Q2/Q3 answered before writing |
| C-13 | PASS | Phase 6 CHECK 1 registry table |
| C-14 | PASS | Phase 4 pre-write scope gate |
| C-15 | PASS | Phase 6 VERIFICATION GATE: 5 checks bundled; all must PASS |
| C-16 | PASS | Three buckets + `[vocab: {term}]` per Q answer |
| C-17 | PASS | Phase 4 dedicated pre-write scope audit |
| C-18 | PASS | Phase 6 CHECK 4 vocabulary coverage |
| C-19 | PASS | Phase 3 frame template with named Q-slot placeholders |
| C-20 | PASS | Three buckets enforce per-Q domain isolation |
| C-21 | PASS | Phase 1 three named buckets |
| C-22 | PASS | Phase 2 iteration log: all-YES audit table; exit declared only after convergence |
| C-23 | PASS | Phase 3 FRAME FILL dedicated phase before Phase 5 role writing |
| C-24 | PASS | Iteration log restart: "Re-evaluate all three Q-answers from Q1 as a unit. Each restart writes a new numbered block." |
| C-25 | PASS | Phase 3 Frame Fill: verbatim slot citations per Q; slot-binding verification |

All 17 aspirational PASS → **10 pts**

**V-05 Total: 100/100**

**Beyond-v6 additions (both axes):**
- Verify citation: `{question} [Q: Q1|Q2|Q3]` on all inertia-advocate verify questions; Phase 6 CHECK 5 validates annotation-dimension binding with `[CITATION MISMATCH]` flag
- Iteration log: numbered ATTEMPT blocks preserved; each replacement records `"{old-term}" → "{new-term}" from [bucket name]` with bucket-confirmed basis

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Total | Essential All-PASS |
|-----------|-----------|-------------|--------------|-------|--------------------|
| V-01 Lifecycle emphasis | 60/60 | 30/30 | 10/10 | **100** | YES |
| V-02 Verify-question citation | 60/60 | 30/30 | 10/10 | **100** | YES |
| V-03 Audit iteration log | 60/60 | 30/30 | 10/10 | **100** | YES |
| V-04 Inertia-first sequence | 60/60 | 30/30 | 10/10 | **100** | YES |
| V-05 ES-1+ES-2 combined | 60/60 | 30/30 | 10/10 | **100** | YES |

**Rank (composite score):** All tied at 100/100. V-05 is the highest-integration variation at this score tier; V-04 introduces a distinct structural innovation (inertia-first phase order) that is orthogonal to the citation/log mechanisms.

---

## Excellence Signals

All 5 variations satisfy all 25 rubric v6 criteria. V-01 was the R7 baseline that first achieved 100/100 on v6. V-02 through V-05 maintain that score while adding structural mechanisms that close two gaps V-01 leaves open at the output level.

**ES-1 (from V-02, amplified in V-05): Verify-question source annotation is a distinct traceability surface from frame-slot citation.**

V-01 applies citation discipline (`Q1 slot ← Phase 2 Q1: [verbatim]`) to the frame string (C-25) but not to inertia-advocate `orientation.verify` questions. A verify question satisfies C-12 by naming the Q1/Q2/Q3 dimension semantically — "What does the current system provide that the proposed approach cannot match?" references Q1 without binding to the specific Phase 2 Q1 answer. The same implicit-population error C-25 closes for the frame string remains open for verify questions: a question can pass C-12 while drawing from the wrong Phase 2 answer or from no Phase 2 answer at all. V-02 closes this by requiring each verify question to carry `[Q: Q1|Q2|Q3]`, making the binding machine-checkable, and CHECK 5 in the gate validates annotation-dimension matching as a blocking condition.

**ES-2 (from V-03, amplified in V-05): The audit restart protocol's provenance gap survives all-YES convergence.**

V-01's Phase 2 restart rule (C-24) requires re-evaluation from row Q1 after any NO, evaluating all three rows as a unit. This closes the incremental-replacement gap C-24 targets. But the instruction to "restart evaluation" overwrites each failed attempt: the final all-YES table is structurally complete, yet the replacement term's bucket origin is unverifiable after convergence. A term inferred from context rather than drawn from the correct bucket can produce an all-YES table indistinguishable from a correctly-sourced one. V-03 closes this by numbering each restart attempt and requiring all prior ATTEMPT blocks to remain in the output, each recording the replacement decision with its bucket-confirmed basis. The replacement term's provenance is visible alongside the convergence result.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Verify-question Q-source annotation: each inertia-advocate orientation.verify question carries a [Q: Q1|Q2|Q3] annotation binding it to its Phase 2 source dimension; a verification gate CHECK validates annotation-dimension matching and flags citation mismatches as blocking errors — the same traceability surface C-25 establishes for frame-slot population", "Audit iteration log with replacement provenance: Phase 2 restart attempts are numbered and preserved in output (AUDIT ATTEMPT 1, 2, ...N); each blocked attempt records old term, new term, bucket name, and one-line bucket-confirmed basis — the replacement term's provenance is verifiable after convergence, preventing a context-inferred term from producing an all-YES table indistinguishable from a correctly-sourced one"]}
```
