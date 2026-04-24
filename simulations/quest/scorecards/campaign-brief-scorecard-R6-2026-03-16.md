---

## campaign-brief / Round 6 — Score Summary

**Rubric:** v6 (21 criteria, 210 pts max)
**Base:** R5 V-05 (200/200 on v5)

| Var | Axes | Essential /50 | Recommended /30 | Aspirational /130 | Total /210 | Rank |
|-----|------|:---:|:---:|:---:|:---:|:---:|
| V-01 | Baseline (R5 V-05 verbatim) | **50** | **30** | **130** | **210** | 1 |
| V-02 | C-16 timestamp isolation | **50** | **30** | **130** | **210** | 1 |
| V-03 | Zero-signal lifecycle | **50** | **30** | **130** | **210** | 1 |
| V-04 | V-02 + V-03 | **50** | **30** | **130** | **210** | 1 |
| V-05 | V-02 + V-03 + inertia framing | **50** | **30** | **130** | **210** | 1 |

All five tie at 210/210. R6 has no open rubric gaps.

---

### Critical experiment results

**V-01 = 210/210 confirmed.** C-21 is fully satisfied by R5 V-05's pre-existing sparse-breadth clause — two instances: STORY question 1 body ("do not write 'insufficient signals'") and execution note ("sparse evidence makes question 1 brief, not absent; question 1 must state a direction"). C-21 was designed to score exactly what V-05 introduced; the design held.

**V-02/V-03 = 210/210.** Both axes are structurally inert on v6. C-16 isolation clause and zero-signal mandate strengthen robustness at live-output boundary conditions but open no new rubric dimension.

**V-05 vs V-04: identical.** Bounded/unbounded `inertia_cost` at VERDICT level does not interact with C-07 (item-level gap fields) or C-06 (verdict presence) — the scope levels are structurally independent.

---

### Excellence signals (from V-05, most complete)

1. **Zero-signal synthesis mandate** — closing the edge case where LLM vacates STORY on "insufficient data." Zero signals becomes "the gap pattern IS the evidence set"; question 1 must answer what uniform absence implies.

2. **Bounded/unbounded inertia classification** — forces the writer to declare not just *what* the risk is but *what the team does about it*: bounded = commit with known risk; unbounded = do not commit until resolved. Surfaced at VERDICT level, orthogonal to item-level gap fields.

---

### R7 design guidance

| Candidate | Source | Status |
|-----------|--------|--------|
| C-16 timestamp survival in COMPRESSED output | R5 design guidance + V-02 | Unconfirmed — V-02 shows the risk; needs live output at high gap count to falsify |
| Zero-signal STORY mandate (C-22 candidate) | V-03/V-04/V-05 | Inert on v6; distinct from C-21 (sparse vs zero) |
| Bounded/unbounded inertia scope (C-23 candidate) | V-05 | Inert on v6; distinct from C-07 (item level) and C-06 (verdict presence) |

**Preferred R7 base:** V-05 — all three robustness axes, 210/210, zero rubric cost.

```json
{"top_score": 210, "all_essential_pass": true, "new_patterns": ["zero-signal synthesis mandate: when found is empty, the gap pattern is the evidence set; STORY question 1 must characterize what uniform absence implies rather than vacating synthesis", "bounded/unbounded inertia classification at verdict level: inertia_cost must declare whether commit risk is recoverable post-commit or propagates to an irreversible state, enabling distinct action postures per verdict status"]}
```
 structure | P | P | P | P | P | Three questions defined in order; prose execution note requires all three at all coverage levels |
| C-19 | Gap reclassification rule from dual-field format | P | P | P | P | P | Reclassification annotated in output via `[RECLASSIFIED from BLOCKING:]` sub-section; `RECLASSIFIED: none` for clean cases |
| C-20 | Density ceiling operates on entry count | P | P | P | P | P | "threshold counts blocking gap *entries*" + "Per-entry field count is orthogonal to the threshold" — both stated explicitly |
| C-21 | Sparse-coverage synthesis protection | P | P | P | P | P | Sparse-breadth rule: "question 1 must state a direction"; "sparse evidence makes question 1 brief, not absent" — explicit clause in STORY execution note; direction requirement stated |

**Criterion totals (all variations):**
- Essential C-01–C-05: 50/50
- Recommended C-06–C-08: 30/30
- Aspirational C-09–C-21: 130/130

---

### Score Summary

| Var | Essential /50 | Recommended /30 | Aspirational /130 | Total /210 | Rank |
|-----|:---:|:---:|:---:|:---:|:---:|
| V-01 | **50** | **30** | **130** | **210** | 1 |
| V-02 | **50** | **30** | **130** | **210** | 1 |
| V-03 | **50** | **30** | **130** | **210** | 1 |
| V-04 | **50** | **30** | **130** | **210** | 1 |
| V-05 | **50** | **30** | **130** | **210** | 1 |

All five variants score 210/210. R6 has no open rubric gaps.

---

### Critical experiments — results

**V-01 = 210/210 confirmed.** C-21 is fully satisfied by R5 V-05's pre-existing sparse-breadth clause. The clause appears in two locations in V-01: (1) inside the STORY question 1 body ("Sparse-breadth rule: do not write 'insufficient signals'") and (2) in the STORY execution note ("sparse evidence makes question 1 brief, not absent; question 1 must state a direction"). C-21 PASS requires an explicit sparse-coverage clause with a direction requirement — both conditions are met. C-21 was designed to score exactly what V-05 introduced in R5; the design held.

**V-02 = 210/210.** The C-16 timestamp isolation sentence ("timestamps on found signals are not part of the density contract and must never be dropped or abbreviated") operates orthogonally to C-16. C-16 was already PASS in V-01 — the isolation clause is structural robustness against a live-output failure mode, not a new rubric axis. No scoring interaction found.

**V-03 = 210/210.** The zero-signal rule ("when found is empty, the gap pattern is the evidence set") extends C-21's sparse-breadth logic to the 0-signal extreme. C-21 tests sparse coverage (1-2 namespaces); C-18 tests structural presence. The zero-signal clause strengthens both without conflicting with either. No scoring change — structurally inert on v6, consistent with R5 V-03/V-05 precedent.

**V-04 = 210/210.** V-02 and V-03 axes operate on different blocks (STATUS density contract note vs STORY execution note). No interaction effects. Both are additive robustness additions. Combined = 210/210.

**V-05 vs V-04: identical.** The bounded/unbounded `inertia_cost` framing does not interact with C-07 (item-level gap fields) or C-06 (verdict presence). C-07 measures per-blocking-gap field structure; V-05's bounded/unbounded scope distinction lives at the VERDICT level (`inertia_cost`), a structurally independent location. V-05 = 210/210.

---

### Excellence signals from V-05 (most structurally complete)

**Signal 1 — Zero-signal synthesis mandate (V-03/V-04/V-05)**
The zero-signal clause closes the failure mode where an LLM receiving a topic with no artifacts at all writes "insufficient data — synthesis not possible." By explicitly declaring that "the gap pattern is the evidence set," the clause re-routes question 1 to characterize what uniform absence implies rather than vacating STORY. This is a boundary-condition guard on C-21 at the 0-signal extreme: C-21 covers sparse (1-2 namespaces); the zero-signal clause extends the protection to the absolute edge. Structurally inert on v6 — potential C-22 candidate.

**Signal 2 — Bounded/unbounded inertia classification at VERDICT level (V-05)**
Adding `bounded: <residual risk and why recoverable> | unbounded: <failure class and why irreversible>` to `inertia_cost` surfaces the action posture of the verdict. A READY verdict with bounded inertia means "commit — you can course-correct." A NOT READY verdict with unbounded inertia means "do not commit — the failure cannot be undone." This distinction forces the writer to answer not just "what is the risk" but "what does the team do about it." Structurally inert on v6 (C-06 and C-07 both PASS without it) — potential C-23 candidate if a second independent instance emerges.

---

### R7 design guidance

Three investigation candidates named in this round:

| Candidate | Origin | Status |
|-----------|--------|--------|
| C-16 timestamp survival in COMPRESSED output | R5 design guidance, V-02 robustness clause | Unconfirmed — V-02 shows the risk is real but R6 investigation found no scoring difference; would require a live output at high gap count to falsify |
| Zero-signal STORY mandate | V-03/V-04/V-05 zero-signal clause | Structurally inert on v6; distinct from C-21 (sparse vs empty); C-22 candidate if a second failure mode instance at 0-signal is observed |
| Bounded/unbounded inertia scope | V-05 inertia framing | Structurally inert on v6; distinct from C-07 (item-level) and C-06 (verdict presence); C-23 candidate if a second independent instance of VERDICT-level scope ambiguity is observed |

**Preferred R7 base:** V-05 — all three robustness axes incorporated, 210/210, zero rubric cost.

---

```json
{"top_score": 210, "all_essential_pass": true, "new_patterns": ["zero-signal synthesis mandate: when found is empty, the gap pattern is the evidence set; STORY question 1 must characterize what uniform absence implies rather than vacating synthesis", "bounded/unbounded inertia classification at verdict level: inertia_cost must declare whether commit risk is recoverable post-commit or propagates to an irreversible state, enabling distinct action postures per verdict status"]}
```
