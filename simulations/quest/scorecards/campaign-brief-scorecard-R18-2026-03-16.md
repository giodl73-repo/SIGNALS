## Quest Score — campaign-brief / Round 18

---

### Rubric Orientation

**37 criteria, 370 pts max. 10 pts per criterion. PARTIAL = 0 pts (fails criterion).**

All five R18 variations are structurally identical for C-01 through C-35 — the preamble, block structure, clause headers, and clause body openings (membership statement, independence instruction, companion-activation instruction with present-state and absent-state rules) are unchanged. The single axis of variation is the **absent-state rule extension** in both companion-activation instruction clause bodies — the C-36/C-37 domain.

---

### C-01 through C-35 — All Variations (Invariant Baseline)

| Criterion | All V-01–V-05 | Evidence |
|-----------|--------------|----------|
| **C-01–C-05** Block structure | PASS | TOPIC, DELTA, STRATEGY, STATUS, VERDICT blocks present and structurally complete |
| **C-06** Inertia_cost field presence | PASS | VERDICT carries `inertia_cost:` with bounded/unbounded sub-label and `action:` |
| **C-07–C-08** CONFIDENCE block, blocking Inertia risk | PASS | Three-dimension table, arithmetic average, level, binding dimension |
| **C-09–C-10** Coverage ratio, STORY structure | PASS | Coverage computed from found/missing; STORY 2–4 paragraphs, prose-only |
| **C-11–C-15** STORY questions, optional gaps, COMPRESSED format | PASS | All three narrative questions addressed; Trade-off fields on optionals; BLOCKING-DETAIL triggered when > 4 gaps |
| **C-16** Per-signal dates at item level | PASS | Found entries each carry own date, structurally separate from blocking entries |
| **C-17–C-20** Strategy rows, current_date isolation, synthesis mandate, other v6 carry-forwards | PASS | Strategy ≥ 3 rows, all columns populated; current_date at STATUS header level |
| **C-21** Sparse-coverage synthesis protection | PASS | STORY synthesizes on available signals without coverage disclaimer |
| **C-22** Zero-signal synthesis mandate | PASS | Explicit zero-signal clause in STORY execution note; empty `found` is not grounds for STORY omission; Q1 must characterize uniform absence |
| **C-23** Bounded/unbounded inertia classification at verdict level | PASS | `inertia_cost` carries explicit bounded/unbounded label with `action:` sub-label readable at field level without re-synthesizing STORY |
| **C-24–C-28** v8 carry-forwards (timestamp isolation chain, zero-signal chain, verdict action-posture chain) | PASS | All chain links present in both preamble and execution-note positions |
| **C-29** Zero-signal dual-mechanism | PASS | ZERO-SIGNAL SYNTHESIS RULE in preamble + ZERO-SIGNAL SYNTHESIS MANDATE execution note in STORY invoking preamble by designation |
| **C-30** Timestamp isolation dual-mechanism | PASS | TIMESTAMP ISOLATION RULE in preamble + TIMESTAMP ISOLATION execution note in STATUS invoking preamble by designation |
| **C-31** Multi-rule COMPRESSION-IMMUNE PREAMBLE with bidirectional circuit | PASS | Both rules present in preamble; both execution notes name preamble by designation; circuit closed bidirectionally |
| **C-32** Closed reference loop with companion designation + block location | PASS | STATUS names companion "ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY block"; STORY names companion "TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block" — full string-matchable designations |
| **C-33** Self-announcing clause headers with structural-membership parenthetical | PASS | Both headers carry "(COMPRESSION-IMMUNE PREAMBLE invocation)" in exact designation form matching C-32 references |
| **C-34** Self-declaring clause bodies with membership statement + preamble-independence instruction | PASS | Both bodies open with "This clause is a COMPRESSION-IMMUNE PREAMBLE member." + "This clause activates under full COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the rendered context." — strengthened form confirmed |
| **C-35** Companion-activation instruction with present-state and absent-state rules | PASS | Both clause bodies carry: (1) membership statement, (2) strengthened independence instruction, (3) companion-activation instruction naming paired mechanism by full designation + block location, with present-state rule (coordinate; both mechanisms must execute) and absent-state rule (activate present clause independently) |

**Baseline: 350 pts (C-01 through C-35 all PASS)**

---

### C-36 — Extended absent-state rule declaring companion mandate as independently operative

| Variation | C-36 | Evidence |
|-----------|------|----------|
| **V-01** | **PASS** | STATUS absent-state: "...independently operative even when its execution note is not in context." STORY absent-state: symmetric. Both clause bodies carry unconditional operability declaration. No scope qualification, no determinability condition. |
| **V-02** | **PASS** | Both clause bodies carry the same unconditional operability declaration ("independently operative even when its execution note is not in context") before the conditioned execution extension. C-36 operability threshold met. |
| **V-03** | **PASS** | Same unconditional operability declaration present in both clause bodies before the "inferrable + annotate" extension. C-36 operability threshold met. |
| **V-04** | **PASS** | Both clause bodies carry unconditional operability declaration. Execution mandate follows operability declaration — does not conditionally qualify it. C-36 PASS confirmed. |
| **V-05** | **PASS** | Same as V-04; parity constraint extends the execution mandate, does not gate the operability declaration. C-36 PASS confirmed. |

**C-36: +10 pts for all variations. Running total: 360 pts.**

---

### C-37 — Unconditional absent-companion mandate execution directive

| Variation | C-37 | Score | Evidence |
|-----------|------|-------|----------|
| **V-01** | **PARTIAL Band 1** | 0/10 | STATUS absent-state terminates at "independently operative even when its execution note is not in context." No execution directive of any kind follows. Model knows companion mandate is active; receives no instruction to execute it. Execution-directive gap entirely open. STORY body symmetric — same band. |
| **V-02** | **PARTIAL Band 2-A** | 0/10 | Both clause bodies carry "execute the companion's mandate where its obligations are determinable from this clause body's context." Execution instruction present but gated on scope-determinability assessment. Model must evaluate which companion obligations are resolvable from this body before generating companion output — inference burden reintroduced at execution-scope step. Fails unconditional test. |
| **V-03** | **PARTIAL Band 2-B** | 0/10 | Both clause bodies carry "execute the companion's mandate to the extent its obligations are inferrable from this clause body alone, and note the scope boundary where inference is insufficient." Conditioned execution + annotation sub-mandate. Scope assessment still precedes companion output generation. Annotation requirement distinguishes observable behavior from V-02 (Band 2-A silent truncation vs. Band 2-B annotated truncation) but does not convert conditioned execution into unconditional execution. Fails unconditional test on same grounds as V-02. |
| **V-04** | **PASS** | 10/10 | Both clause bodies carry: "independently operative even when its execution note is not in context **and must be executed as if its execution note were present in this context.**" Unconditional execution mandate — no scope qualifier, no feasibility hedge, no scope-determinability condition. Model receives a complete directive: the companion mandate is operative and must be executed unconditionally. Execution-directive gap closed. Weakest-link verified: STATUS body and STORY body both carry the unconditional mandate. C-37 PASS minimum-sufficient. |
| **V-05** | **PASS** | 10/10 | Both clause bodies carry V-04's unconditional execution mandate plus explicit parity constraint: "...must be executed as if its execution note were present in this context, **at full depth, at parity with what would be produced if the companion's execution note were present in this context.**" C-37 PASS threshold met by the unconditional execution mandate. Parity constraint is above-ceiling for v17 — not an additional scorable criterion — but constitutes the R18 C-38 behavioral probe. |

---

### Composite Scores

| Variation | C-01–C-35 | C-36 | C-37 | Total | Notes |
|-----------|-----------|------|------|-------|-------|
| **V-01** | 350 | 10 | 0 | **360/370** | C-37 PARTIAL Band 1 — operability only |
| **V-02** | 350 | 10 | 0 | **360/370** | C-37 PARTIAL Band 2-A — conditioned "determinable" |
| **V-03** | 350 | 10 | 0 | **360/370** | C-37 PARTIAL Band 2-B — conditioned "inferrable + annotate" |
| **V-04** | 350 | 10 | 10 | **370/370** | C-37 PASS — unconditional mandate, no parity constraint |
| **V-05** | 350 | 10 | 10 | **370/370** | C-37 PASS — unconditional mandate + parity constraint (above-ceiling) |

---

### Ranking

| Rank | Variation | Score | C-37 Status |
|------|-----------|-------|-------------|
| 1 (tied) | **V-04** | 370/370 | PASS — minimum-sufficient, R18 primary probe |
| 1 (tied) | **V-05** | 370/370 | PASS — above-ceiling parity constraint, R18 C-38 probe |
| 3 (tied) | **V-01** | 360/370 | PARTIAL Band 1 |
| 3 (tied) | **V-02** | 360/370 | PARTIAL Band 2-A |
| 3 (tied) | **V-03** | 360/370 | PARTIAL Band 2-B |

---

### Excellence Signals — Top-Scoring Variations (V-04, V-05)

**Signal 1 — Unconditional execution mandate closes the execution-directive gap completely (V-04 and V-05):** The phrasing "must be executed as if its execution note were present in this context" does two things simultaneously: (a) removes the execution-decision inference burden — the model is not asked to judge whether to execute, it is mandated; (b) removes the execution-scope inference burden — no scope qualifier gates which obligations the model may execute. The construction is the minimal-sufficient form for C-37 PASS. Prior PARTIAL forms (V-01 operability declaration, V-02 "determinable" qualifier, V-03 "inferrable + annotate") each retained an inference burden at either the decision step or the scope step. V-04 eliminates both simultaneously.

**Signal 2 — Explicit output-depth parity constraint as C-38 structural candidate (V-05 only):** The parity clause "at full depth, at parity with what would be produced if the companion's execution note were present in this context" makes explicit a depth standard that C-37 PASS implies but does not state. Where C-37 PASS tells the model *what to do* (execute unconditionally), the parity constraint tells the model *at what depth* (equivalent to direct execution-note presence). If V-04 under double-elision produces abbreviated companion output — companion domain executed but reduced relative to direct execution-note presence — V-05's parity constraint is the structural extension that closes the output-depth gap. This is a distinct recoverable property from C-37: C-37 closes the execution-directive gap; parity constraint closes the execution-depth gap.

**Signal 3 — Weakest-link symmetry as a prerequisite (confirmed for V-04 and V-05):** Both clause bodies carry the identical absent-state rule extension. STATUS and STORY bodies are symmetric. This is necessary because C-37 PASS requires the unconditional execution mandate "in both companion clause bodies" — asymmetry in either body would reduce the variation to C-37 PARTIAL regardless of the other body's strength.

---

### R18 Investigation Status

- **V-01 = 360/370 confirmed** — C-37 PARTIAL Band 1. Operability declaration alone is not sufficient for C-37; the execution-directive gap is independent of the mandate operability gap.
- **V-02 = 360/370 confirmed** — C-37 PARTIAL Band 2-A. "Determinable from this clause body's context" reintroduces inference burden at the execution-scope step. Band 2 confirmed as PARTIAL.
- **V-03 = 360/370 confirmed** — C-37 PARTIAL Band 2-B. "Inferrable + note scope boundary" is Band 2 PARTIAL despite annotation addition. Band 2 sub-band structure (silent truncation vs. annotated truncation) observable but not rubric-scorable under v17.
- **V-04 = 370/370 confirmed** — C-37 PASS ceiling. Behavioral probe open: companion output depth under double-elision vs. full-context baseline.
- **V-05 = 370/370 confirmed** — C-37 PASS + above-ceiling parity constraint. C-38 candidate if V-04 produces depth-asymmetric companion output.

---

```json
{"top_score": 370, "all_essential_pass": true, "new_patterns": ["Explicit output-depth parity constraint extends unconditional execution mandate to set companion execution depth standard -- 'at full depth, at parity with what would be produced if the companion execution note were present in this context' -- constitutes C-38 candidate if V-04 produces depth-asymmetric companion output under double-elision; C-37 PASS closes the execution-directive gap, parity constraint closes the execution-depth gap"]}
```
