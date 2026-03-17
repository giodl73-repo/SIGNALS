## crew-roles — Quest Score R8 (Rubric v6)

**Baseline**: R7 V-01 = 100/100 (all 25 criteria). R8 probes two ES gaps beyond v6: ES-1 (verify-question source binding is soft) and ES-2 (audit iterations are discarded, leaving replacement provenance unverifiable).

**Scoring formula**: Essential 5×12=60 | Recommended 3×10=30 | Aspirational `aspirational_pass/17×10`=10 | Max 100.

---

### V-01 — Verify-question source citation

Adds `[Q: Q1/Q2/Q3]` annotations to each inertia-advocate `orientation.verify` question. Adds CHECK 5 in the Phase 6 verification gate validating annotation presence and dimension match. 6-phase structure identical to R7 baseline otherwise.

| ID | Criterion | V-01 | Evidence |
|----|-----------|------|----------|
| C-01 | All 5 fields | PASS | All required fields listed in role writing instructions |
| C-02 | Inertia-advocate present | PASS | Dedicated inertia-advocate with frame, verify, simplify |
| C-03 | Correct output path | PASS | `.craft/roles/{area}/` |
| C-04 | Domain specificity | PASS | `expertise.relevance` must reference Phase 1 vocabulary term |
| C-05 | Minimum 3 roles | PASS | "Minimum 3 roles total including inertia-advocate" |
| C-06 | Lens actionability | PASS | verify ends in `?`; simplify items are imperatives |
| C-07 | Collaborates_with resolves | PASS | CHECK 2 — orphan reference resolution at gate |
| C-08 | Perspective diversity | PASS | "Roles span at least 3 distinct perspective categories" |
| C-09 | Scope gradient | PASS | Phase 4 pre-write scope audit; CHECK 3 enforcement |
| C-10 | Inertia domain-grounded | PASS | Q1 current system named in frame verbatim |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 produces named vocabulary list; every `expertise.relevance` must reference Phase 1 term |
| C-12 | Inertia pre-characterization | PASS | Q1/Q2/Q3 explicit; verify questions reference Q-dimensions |
| C-13 | Registry summary table | PASS | CHECK 1 |
| C-14 | Scope-gradient-enforcement | PASS | CHECK 3; Phase 4 scope audit blocks writing |
| C-15 | Verification-gate-phase | PASS | Phase 6 bundles all 5 checks |
| C-16 | Vocabulary-linked Q&A | PASS | Each Q-answer `[vocab: {term-from-X-bucket}]` |
| C-17 | Pre-write scope audit | PASS | Phase 4 blocks until ≥2 distinct scope values |
| C-18 | Vocabulary check in gate | PASS | CHECK 4 in Phase 6 |
| C-19 | Inertia frame Q-slot template | PASS | Explicit slot template with named placeholders |
| C-20 | Q-domain-aligned vocab distribution | PASS | Cross-bucket selection fails Phase 2 exit |
| C-21 | Bucketed vocabulary extraction | PASS | Phase 1 produces three named Q-domain buckets |
| C-22 | Domain-alignment audit table | PASS | "restart from Q1 — do not re-score only the replaced row; evaluate all three rows as a unit" |
| C-23 | Frame Fill phase | PASS | Phase 3 — named dedicated phase before scope audit |
| C-24 | Full re-evaluation after replacement | PASS | Restart protocol "from row 1"; exit condition "evaluated as a unit" |
| C-25 | Frame-slot source citation | PASS | `Q1 slot ← Phase 2 Q1: [verbatim]` etc. |

**V-01 Score: Essential 60 + Recommended 30 + Aspirational 17/17×10 = 100/100**

---

### V-02 — Audit iteration log

Adds numbered `AUDIT ATTEMPT N` blocks to Phase 2; all prior blocks preserved in output; convergence declared with attempt count. 6-phase structure. Verification gate has 4 checks — no CHECK 5 (verify annotations not present in V-02; verify says "at least 2 reference Q1/Q2/Q3 dimensions by name" without structural citation).

| ID | Criterion | V-02 | Evidence |
|----|-----------|------|----------|
| C-01–C-08 | All essential + recommended | PASS | Same as R7 baseline; all present |
| C-09–C-10 | Scope gradient, domain-grounded | PASS | Scope audit + Q1 named in frame |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 bucketed vocab; `expertise.relevance` references Phase 1 term |
| C-12 | Inertia pre-characterization | PASS | Q1/Q2/Q3 explicit; verify "at least 2 reference Q-dimensions" |
| C-13–C-18 | Structural gates | PASS | CHECK 1–4 in Phase 6; scope audit in Phase 4 |
| C-19–C-21 | Slot template, Q-domain, bucketed vocab | PASS | Phase 3 slot template; Phase 1 buckets; cross-bucket fails exit |
| C-22 | Audit table at Phase 2 exit | PASS | Iteration log; each ATTEMPT N re-evaluates from Q1 as unit |
| C-23 | Frame Fill phase | PASS | Phase 3 named |
| C-24 | Full re-evaluation after replacement | PASS | "Re-evaluate all three Q-answers starting from Q1. Write a new numbered block." |
| C-25 | Frame-slot source citation | PASS | `Q1 slot ← Phase 2 Q1: [verbatim — from convergence Q1]` |

**V-02 Score: Essential 60 + Recommended 30 + Aspirational 17/17×10 = 100/100**

---

### V-03 — Inertia-first sequence

7-phase structure: Phase 1 = current-system identification (Q1 only), Phase 2 = anchored vocabulary extraction, Phase 3 = Q2/Q3 + audit, Phase 4 = Frame Fill, Phase 5 = scope audit, Phase 6 = role writing, Phase 7 = gate (4 checks). No CHECK 5 (verify: "at least 2 reference Q1/Q2/Q3 by name," no `[Q:]` annotations).

**Critical gap**: C-11 and C-21 require "Phase 1 produces" the vocabulary list and three named buckets. V-03 Phase 1 produces only the current-system identification; vocabulary extraction is Phase 2. The Phase 1 exit condition is "current system named; Q1 = [named entity]" — no vocabulary produced. This is a structural phase-label mismatch against both criteria, not a spirit violation (vocabulary does exist before Q&A, but in Phase 2).

| ID | Criterion | V-03 | Evidence |
|----|-----------|------|----------|
| C-01–C-08 | All essential + recommended | PASS | Present in all phases |
| C-09, C-10 | Scope gradient, domain-grounded | PASS | Phase 5 scope audit; Q1 proper noun in frame |
| **C-11** | **Vocabulary-forced-field** | **PARTIAL** | Vocabulary list produced in Phase 2, not Phase 1; criteria require "Phase 1 produces"; `expertise.relevance` does reference Phase 2 terms (functional requirement met but phase-attribution wrong) |
| C-12 | Inertia pre-characterization | PASS | Q1 in Phase 1; Q2/Q3 in Phase 3; verify references dimensions |
| C-13–C-18 | Structural gates | PASS | CHECK 1–4 in Phase 7; Phase 5 scope audit |
| C-19–C-20 | Slot template, Q-domain aligned | PASS | Phase 4 slot template; Q2/Q3 draw from respective buckets |
| **C-21** | **Bucketed vocabulary extraction** | **PARTIAL** | Three named Q-domain buckets produced in Phase 2 (not Phase 1 as required by criteria); Phase 1 exit condition explicitly "current system named; Q1 = [named entity]" only |
| C-22 | Audit table at Phase 3 exit | PASS | Restart from Q1; "evaluate all three rows as a unit" (at Phase 3 exit, not Phase 2 — phase label differs but function equivalent) |
| C-23–C-25 | Frame Fill, re-evaluation, citations | PASS | Phase 4 named Frame Fill; restart protocol in Phase 3; slot citations in Phase 4 |

**V-03 Score: Essential 60 + Recommended 30 + Aspirational (15 + 2×0.5)/17×10 = 60 + 30 + 9.41 = 99.4/100**

---

### V-04 — ES-1 + ES-2 combined

6-phase structure combining V-01 (verify `[Q:]` citations + CHECK 5) and V-02 (audit iteration log). Both additions applied simultaneously; no phase-label reorganization.

| ID | Criterion | V-04 | Evidence |
|----|-----------|------|----------|
| C-01–C-08 | All essential + recommended | PASS | Same as baseline |
| C-09–C-10 | Scope, domain-grounded | PASS | Phase 4 scope audit; Q1 in frame |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 bucketed vocab; Phase 5 requires Phase 1 term in `expertise.relevance` |
| C-12–C-18 | Inertia Q&A, structural gates | PASS | Q1/Q2/Q3; CHECK 1–5 in Phase 6 |
| C-19–C-21 | Slot template, Q-domain, bucketed | PASS | Phase 3 slot template; Phase 1 buckets; Q-domain aligned |
| C-22 | Audit table at Phase 2 exit | PASS | Iteration log; each attempt re-evaluates from Q1 as unit |
| C-23 | Frame Fill phase | PASS | Phase 3 named |
| C-24 | Full re-evaluation | PASS | "Re-evaluate all three Q-answers from Q1 as a unit" |
| C-25 | Frame-slot source citation | PASS | `Q1 slot ← Phase 2 Q1: [verbatim from convergence]` |

**V-04 Score: Essential 60 + Recommended 30 + Aspirational 17/17×10 = 100/100**

---

### V-05 — ES-1 + ES-2 + Inertia-first

7-phase structure combining all three axes: V-03 phase order (inertia-first) + V-02 iteration log in Phase 3 + V-01 verify `[Q:]` citations in Phase 6 + CHECK 5 in Phase 7. Most comprehensive variation.

Same C-11 and C-21 phase-label issue as V-03: Phase 1 produces only the current-system identification; vocabulary extracted in Phase 2. V-05 Phase 6 (role writing) references "Phase 2 vocabulary term" and Phase 7 CHECK 4 validates "Phase 2 vocabulary term" — criteria require Phase 1.

| ID | Criterion | V-05 | Evidence |
|----|-----------|------|----------|
| C-01–C-08 | All essential + recommended | PASS | Present throughout |
| C-09, C-10 | Scope, domain-grounded | PASS | Phase 5 scope audit; Q1 proper noun in frame |
| **C-11** | **Vocabulary-forced-field** | **PARTIAL** | Vocabulary list in Phase 2; Phase 6/7 reference "Phase 2 vocabulary term"; criteria require Phase 1 production |
| C-12 | Inertia pre-characterization | PASS | Q1 Phase 1; Q2/Q3 Phase 3; verify references dims with `[Q:]` |
| C-13–C-18 | Structural gates | PASS | CHECK 1–5 in Phase 7; Phase 5 scope audit |
| C-19–C-20 | Slot template, Q-domain | PASS | Phase 4 slot template; Q2/Q3 from buckets |
| **C-21** | **Bucketed vocabulary extraction** | **PARTIAL** | Buckets in Phase 2; Phase 1 exit condition is current-system identification only |
| C-22 | Audit table at Phase 3 exit | PASS | Phase 3 iteration log; "re-evaluate starting from Q1" |
| C-23 | Frame Fill phase | PASS | Phase 4 named Frame Fill |
| C-24 | Full re-evaluation | PASS | "Re-evaluate all three Q-answers starting from Q1" in Phase 3 |
| C-25 | Frame-slot source citation | PASS | Phase 4: `Q1 slot ← Phase 1 / Phase 3 Q1: [verbatim]` etc. |

**V-05 Score: Essential 60 + Recommended 30 + Aspirational (15 + 2×0.5)/17×10 = 60 + 30 + 9.41 = 99.4/100**

---

### Composite Scores and Rankings

| Rank | Variation | Essential | Recommended | Aspirational | Total | Notes |
|------|-----------|-----------|-------------|--------------|-------|-------|
| 1 (tie) | V-01 | 60 | 30 | 10.00 | **100** | Verify `[Q:]` citations + CHECK 5 |
| 1 (tie) | V-02 | 60 | 30 | 10.00 | **100** | Iteration log; no `[Q:]` in verify |
| 1 (tie) | V-04 | 60 | 30 | 10.00 | **100** | V-01 + V-02 combined |
| 4 (tie) | V-03 | 60 | 30 | 9.41 | **99.4** | Inertia-first; C-11/C-21 phase-label PARTIAL |
| 4 (tie) | V-05 | 60 | 30 | 9.41 | **99.4** | V-03+V-01+V-02; C-11/C-21 PARTIAL carry through |

**All essential criteria pass across all variations.**

**V-04 is the strongest single variation for v7 purposes**: it scores 100/100 while demonstrating both new structural patterns (verify citations + iteration log) without the phase-label reorganization that creates C-11/C-21 friction. V-05's inertia-first sequence is a genuine improvement in vocabulary anchoring quality but introduces a structural tension with Phase 1 attribution criteria.

---

### Excellence Signals

**ES-1 (from V-01 / V-04 / V-05) — Verify-question `[Q:]` dimension annotation with gate validation**

The inertia-advocate `orientation.verify` questions carry `[Q: Q1]`, `[Q: Q2]`, `[Q: Q3]` annotations. CHECK 5 in the verification gate validates (a) that each question has an annotation and (b) that the annotation matches the Q-dimension the question actually draws from. A question naming the Q1 current system by its Phase 1 proper noun passes semantically in v6 — it satisfies C-12's "reference at least 2 dimensions" — but the question could draw from a Phase 2 answer that doesn't correspond to the Q1 answer (e.g., paraphrasing from context rather than tracing to a specific Phase 2 Q-answer). The `[Q:]` annotation makes the binding structural: the annotation claim can be verified against the question content, and the gate fails if they diverge. This closes the same implicit-population gap C-25 closes for the frame string, applied uniformly to verify fields.

**ES-2 (from V-02 / V-04 / V-05) — Numbered AUDIT ATTEMPT log with bucket-provenance replacement records**

Phase 2 (or Phase 3 in inertia-first variations) opens numbered `AUDIT ATTEMPT N` blocks. Each failed attempt records: the NO row, the old term, the replacement term, the bucket name the replacement came from, and a one-line confirmation that the replacement belongs to that bucket and is not inferred from context. Prior attempt blocks are never deleted. `AUDIT CONVERGENCE: ATTEMPT [N] ALL YES. [N] attempt(s) required.` After convergence, the full replacement history remains in the output. V-02's key insight is that the current "repeat until all-YES" instruction produces a structurally correct final table without leaving any evidence of what was replaced or whether the replacement was sourced from the correct bucket — a term inferred from domain context rather than drawn from the bucket can pass its row in re-evaluation and leave no trace. The numbered log closes this gap by making provenance verifiable after the fact.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["orientation.verify questions on the inertia-advocate carry [Q: Q1/Q2/Q3] dimension annotations validated in verification gate CHECK 5 — closes the implicit-binding gap where a verify question satisfies C-12 semantically by naming a Q-dimension but draws from the wrong Phase 2 answer without structural detection", "Phase 2 audit opens numbered AUDIT ATTEMPT N blocks with replacement records preserved in output — each NO row triggers a replacement entry stating old term, new term, bucket name, and one-line bucket-membership confirmation; AUDIT CONVERGENCE declares attempt count; full history remains visible after convergence, making replacement provenance verifiable beyond the final all-YES table"]}
```
