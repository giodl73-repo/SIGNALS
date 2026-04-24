Scorecard R2 written. Results:

---

## validate-consistency — R2 Scores

| Rank | Variation | Score | Gap |
|------|-----------|-------|-----|
| 1 (tie) | **V-04** | **115/115** | C-04, C-11, C-12, C-13 all PASS |
| 1 (tie) | **V-05** | **115/115** | C-04, C-11, C-12, C-13 all PASS |
| 3 (tie) | V-02 | 110 | C-13 miss (no gate between Step 2 and Step 3) |
| 3 (tie) | V-03 | 110 | C-13 miss (no gate before Pass 2) |
| 5 | V-01 | 104 | C-04 partial + C-11 miss (rules, no mechanism) |

**Projections confirmed**: all five within 1-2 points of the variation map estimates.

---

**Three new patterns captured at 115:**

1. **Inline classification-time INERTIA CHECK** — fires at severity assignment, names 4 drift patterns, requires paper citation. Timing is what makes it different from a standing Skeptic rule.

2. **Named three-count gate** — Total/MULTI/SINGLE stated before Phase 3; "PASS 2 does not begin until these three numbers are stated." Re-sweep trigger if SINGLE=0.

3. **FINAL COUNT table with source-phase column** — three-row table, each row names its source phase. V-05 extends it to stay correct after DA-driven severity changes in Phase 4B.

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["inline-classification-time-inertia-check: INERTIA CHECK fires at severity assignment, not in a preamble; names 4 drift patterns; paper citation required before any P1 downgrade; pattern applied without paper support is explicitly disqualified", "named-three-count-gate: Total/MULTI/SINGLE statement required before Phase 3 begins; re-sweep triggered if SINGLE=0 with any numerical values in paper; gate closes Phase 2 structurally not just narratively", "final-count-table-with-source-phase-column: three-row table binding each frontmatter field to a named phase event; prevents stale carry-forward; V-05 extends it to account for post-DA severity changes"]}
```
table is still present, with row: 'none found'" |
| V-04 | PASS | Step 7 table: I-ID, Type, What conflicts, Inertia check result, Severity, Fix required; "If no inconsistencies: include the table with row 'none found'" |
| V-05 | PASS | Phase 4 table with same columns; "If no inconsistencies found: table is still present" |

All PASS — 12/12 each.

---

### C-04 — P1 issues correctly identified and not downgraded (12 pts essential)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PARTIAL | Severity definitions only: "P1: Different values for the same quantity, or two equations that provably disagree." No structural guard. A model run can silently relabel. |
| V-02 | PASS | INERTIA CHECK explicitly lists 4 drift patterns; "A pattern applied without paper support is not a valid basis for downgrading from P1." Paper citation required before any downgrade. |
| V-03 | PASS | Skeptic: "Severity rules — these are hard. The Skeptic does not negotiate them down: P1 — REJECT condition. No exceptions." Named role mandate embedded at severity rule. |
| V-04 | PASS | INERTIA CHECK identical to V-02; "Do not relabel P2 unless the INERTIA CHECK found explicit paper support for a lesser classification." |
| V-05 | PASS | Skeptic hard rule + Phase 4B DA block: "A finding that survives Devil's Advocate review stays at P1." Downgrade requires documented rebuttal. Inertia warning fires if all defenses are accepted. |

V-01: 6/12. Others: 12/12.

---

### C-05 — Artifact frontmatter contains all required fields (12 pts essential)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | Frontmatter instruction names all 6 fields; "p1_count and p2_count = count of P1 and P2 rows in the Phase 4 register. Count after Phase 4 is complete. Do not carry forward from earlier." |
| V-02 | PASS | Step 9 explicitly derives all three counts from named steps; frontmatter uses `[count from Step 9]` notation |
| V-03 | PASS | FINAL COUNT table drives frontmatter; "Frontmatter using the FINAL COUNT table" — each field traced to table row |
| V-04 | PASS | Step 9 "Derive each value from the named step output, not from memory or estimates"; frontmatter annotations: `[from Step 9 — Step 7 P1 rows]` |
| V-05 | PASS | FINAL COUNT table post Phase 4B; frontmatter: `[from FINAL COUNT — Phase 4 post-4B P1 rows]` |

All PASS — 12/12 each.

---

### C-06 — All four check types (3A-3D) executed (10 pts recommended)

All five have explicit 3A, 3B, 3C, and 3D sections; every variation includes a "none applicable" fallback for 3D. All PASS — 10/10 each.

---

### C-07 — Phase 5 amendments ordered and actionable (10 pts recommended)

All five: ordered P1->P2->P3, exact location + correct value, prohibition on "verify which is correct." All PASS — 10/10 each.

---

### C-08 — Equation consistency (3B) shows algebraic reasoning for FAIL (10 pts recommended)

All five explicitly prohibit "they differ" and require the symbolic step. V-03 and V-05 embed this as a named SKEPTIC RULE inside the section itself. All PASS — 10/10 each.

---

### C-09 — Boundary/limit checks (3C) include explicit evaluation steps (5 pts aspirational)

All five: "Show the substitution for every row, pass or fail." V-03 and V-05 embed as SKEPTIC RULE. All PASS — 5/5 each.

---

### C-10 — Single-location quantities registered as unverifiable (5 pts aspirational)

All five: explicit single-location annotation required; V-01 includes Phase 2 Gate re-sweep trigger if single count = 0. All PASS — 5/5 each.

---

### C-11 — P1 severity structurally enforced, not just stated (5 pts aspirational)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | MISS | Phase 4 has a rule ("P1...reject condition") but no named adversarial role, challenge block, or inertia warning. A rule is not a mechanism. |
| V-02 | PASS | INERTIA CHECK at Step 7 is a named adversarial mechanism — 4 patterns listed, paper citation required, "pattern applied without paper support is not a valid basis for downgrading" |
| V-03 | PASS | Skeptic is a named adversarial role with structural mandate "does not negotiate them down"; embedded inside the severity rule definition |
| V-04 | PASS | INERTIA CHECK identical to V-02 — fires at classification time with documented-citation requirement |
| V-05 | PASS | DA block in Phase 4B: named-defenses list, required rebuttal-or-acceptance, inertia re-examine warning if all defenses accepted |

V-01: 0/5. Others: 5/5.

---

### C-12 — Frontmatter counts bound to a named phase event (5 pts aspirational)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | "quantities_checked = the 'Total quantities registered' from the Phase 2 Gate"; "Count after Phase 4 is complete" — named source phases |
| V-02 | PASS | Step 9: each count names its source step ("total rows in Step 2 table", "P1 rows in Step 7 table") |
| V-03 | PASS (strongest) | FINAL COUNT table: 3-row table, each row names source phase explicitly; "Do not estimate. Do not fill in advance." |
| V-04 | PASS | Step 9: "quantities_checked = total rows in the Step 2 table (confirmed in Step 2G tally)"; frontmatter: `[from Step 9 — Step 2G tally]` |
| V-05 | PASS (strongest) | FINAL COUNT table post Phase 4B: source phases named per row; "If a finding was downgraded during Phase 4B, the counts below already reflect that change" — handles the DA-update case explicitly |

All PASS — 5/5 each. V-03 and V-05 are the strongest implementations.

---

### C-13 — Completeness gate present between Phase 2 and Phase 3 (5 pts aspirational)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | PASS | `PHASE 2 GATE — REGISTRY CLOSED` section: states total, MULTI, SINGLE counts; "Phase 2 is now closed. Do not add quantities during Phase 3." Re-sweep trigger if SINGLE=0. |
| V-02 | MISS | No gate between Step 2 and Step 3. Goes directly from SINGLE/MULTI marking to 3A cross-check. |
| V-03 | MISS | Pass 1 completes Steps A and B, then PASS 2 begins immediately. No count summary required before Phase 3. |
| V-04 | PASS | `Step 2G — Registry Gate`: total, MULTI, SINGLE counts required; "SINGLE quantities exist in almost every paper" re-sweep trigger; gate explicitly closes before Step 3. |
| V-05 | PASS | Pass 1 Step C: "PASS 2 does not begin until these three numbers are stated"; re-sweep trigger if SINGLE=0. |

V-02, V-03: 0/5. Others: 5/5.

---

## Composite Scores

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | **Total** |
|-----------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:---------:|
| V-01 | 12 | 12 | 12 | 6 | 12 | 10 | 10 | 10 | 5 | 5 | 0 | 5 | 5 | **104** |
| V-02 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 5 | 5 | 0 | **110** |
| V-03 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 5 | 5 | 0 | **110** |
| V-04 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 5 | 5 | 5 | **115** |
| V-05 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 5 | 5 | 5 | **115** |

---

## Ranking

| Rank | Variation | Score | All Essential Pass? | Notes |
|------|-----------|-------|---------------------|-------|
| 1 (tie) | V-04 | 115 | Yes | Step-list lineage; minimal structural overhead — 3 insertions (Step 2G, INERTIA CHECK at Step 7, Step 9 binding) each at the natural position |
| 1 (tie) | V-05 | 115 | Yes | Full synthesis — Skeptic + DA block + Step C gate + FINAL COUNT; strongest individual C-11 mechanism (DA + inertia re-examine warning) |
| 3 (tie) | V-02 | 110 | Yes | INERTIA CHECK is the best standalone C-11 pattern; only miss is C-13 (no gate between Step 2 and Step 3) |
| 3 (tie) | V-03 | 110 | Yes | Auditor/Skeptic + FINAL COUNT is the cleanest C-12 implementation; only miss is C-13 (no gate before Pass 2) |
| 5 | V-01 | 104 | No (C-04 partial) | Gate implementation is clean; C-11 gap is the structural weakness — rules without a named mechanism cannot hold P1 verdicts under pressure to smooth things over |

---

## Excellence Signals

**Pattern 1: Inline classification-time INERTIA CHECK (V-02, V-04)**
The four drift patterns are listed at the point where severity is assigned — not in a preamble. Paper citation is required before applying any pattern. "A pattern applied without paper support is not a valid basis for downgrading from P1." The difference from a standing Skeptic rule is timing: the instruction appears in the context window at the moment the decision is made.

**Pattern 2: Named three-count gate before Phase 3 (V-01, V-04, V-05)**
Total / MULTI / SINGLE must be stated before Phase 3 begins. V-05 strengthens it: "PASS 2 does not begin until these three numbers are stated." The re-sweep trigger catches the most common form of partial Phase 2 failure — a registry that omits quantities seen only once, because those are the ones most likely to be skipped.

**Pattern 3: FINAL COUNT table with source-phase column (V-03, V-05)**
Three-row table naming the source phase for each frontmatter field. Not prose. Not a buried instruction. A table with a `Derived from` column makes the binding visible and auditable. V-05 adds: accounts for post-DA downgrades in the count, so the table remains correct after Phase 4B changes severity assignments.

---

## Cross-Round Delta (R1 -> R2)

| Axis | R1 top score | R2 top score | Delta | What moved |
|------|:------------:|:------------:|:-----:|-----------|
| Essential coverage | 60/60 | 60/60 | 0 | All essential criteria already fully addressed in R1 |
| Recommended coverage | 30/30 | 30/30 | 0 | No change |
| Aspirational coverage | 10/10 | 25/25 | +15 | C-11, C-12, C-13 all added and fully addressed in V-04, V-05 |
| Total | 100 | 115 | +15 | Three new aspirational criteria, all captured by two variations |

R1 C-04 partial (V-02, V-04 in R1) is now fully fixed in R2 V-02, V-04 via INERTIA CHECK. The V-01(R1) Skeptic role pattern that scored 100 in R1 now scores 110 in R2 (C-13 miss) — structural completeness gate was the missing piece.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["inline-classification-time-inertia-check: INERTIA CHECK fires at severity assignment, not in a preamble; names 4 drift patterns; paper citation required before any P1 downgrade; pattern applied without paper support is explicitly disqualified", "named-three-count-gate: Total/MULTI/SINGLE statement required before Phase 3 begins; re-sweep triggered if SINGLE=0 with any numerical values in paper; gate closes Phase 2 structurally not just narratively", "final-count-table-with-source-phase-column: three-row table binding each frontmatter field to a named phase event; prevents stale carry-forward; V-05 extends it to account for post-DA severity changes"]}
```
