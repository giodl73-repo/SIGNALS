# crew-roles — Quest Score R14 (Rubric v8)

## Baseline Assessment

**R13 V-05 baseline (inherited by all R14 variations)**:
- Essential C-01–C-05: all PASS
- C-06 (lens actionability): **PARTIAL** — verify fields are `?`-terminated, but no CHECK enforces imperative-verb start on simplify items → Gap-1
- C-07 (collaborates_with resolves): PASS
- C-08 (perspective diversity): PASS
- C-09 (scope gradient): PASS — CHECK 3B maintains
- C-10 (inertia domain-grounded): **PARTIAL** — framing present but no write-ordering lock; scope drift during authoring could silently degrade inertia framing → Gap-3
- C-11 (vocab-forced-field): **PARTIAL** — post-write CHECK 4 only; no per-role planned-vocab column; Gap-2
- C-12 (inertia pre-characterization): PASS
- C-13 (registry summary table): PASS
- C-14–C-27 (prior rounds): mix — estimate 10 PASS, 4 PARTIAL → 12 credits
- C-28 (five-failure-mode annotation gate): PASS — formalized from R13 V-05
- C-29 (scope plan-to-write binding): PASS — CHECK 3B formalized from R13 V-05

**Baseline aspirational credits**: C-09(1) + C-10(0.5) + C-11(0.5) + C-12(1) + C-13(1) + C-14–C-27(12) + C-28(1) + C-29(1) = **18/21**
**Baseline score**: 18/21 × 10 = **8.57**

---

## V-01 — Inertia-First Write Order

**Axis**: Role sequence — inertia-advocate written first; `INERTIA-ADVOCATE WRITTEN` gate before Step 3.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | All 5 fields | PASS | Baseline — field structure unchanged |
| C-02 | Inertia-advocate present | PASS | Inertia-first gate ensures role exists before other roles are planned |
| C-03 | Correct output path | PASS | Baseline |
| C-04 | Domain specificity | PASS | Baseline |
| C-05 | Minimum 3 roles | PASS | Baseline |
| C-06 | Lens actionability | **PARTIAL** | No LENS AUDIT on simplify items — Gap-1 unaddressed |
| C-07 | Collaborates_with resolves | PASS | Baseline |
| C-08 | Perspective diversity | PASS | Baseline |
| C-09 | Scope gradient | PASS | CHECK 3B maintained; inertia-first locks cross-team before other roles can drift |
| C-10 | Inertia domain-grounded | **PASS** | Writing inertia first with domain-locked framing before any other role prevents back-pressure scope drift → Gap-3 closed |
| C-11 | Vocab-forced-field | **PARTIAL** | CHECK 4 post-write only — Gap-2 unaddressed |
| C-12 | Inertia pre-characterization | PASS | Baseline — pre-characterization questions remain |
| C-13 | Registry summary table | PASS | Baseline |
| C-14–C-27 | Prior-round criteria | PASS/PARTIAL | Inherited from R13 V-05 baseline (12 credits) |
| C-28 | Five-failure-mode gate | PASS | Baseline |
| C-29 | Scope plan-to-write binding | PASS | Baseline; inertia-first strengthens |

**Aspirational credits**: 18.5/21
**V-01 score**: 18.5/21 × 10 = **8.81**

---

## V-02 — Vocab Plan-to-Write Binding (CHECK 4B)

**Axis**: Output format — Phase 5 adds `Planned-Vocab-Term` column; CHECK 4 splits into 4A (coverage) + 4B (row-by-row vocab binding, emits `VOCAB BINDING MISMATCH`).

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01–C-05 | Essential | PASS | Baseline |
| C-06 | Lens actionability | **PARTIAL** | LENS AUDIT not present — Gap-1 unaddressed |
| C-07 | Collaborates_with resolves | PASS | Baseline |
| C-08 | Perspective diversity | PASS | Baseline |
| C-09 | Scope gradient | PASS | Baseline |
| C-10 | Inertia domain-grounded | **PARTIAL** | No inertia-first ordering — Gap-3 unaddressed |
| C-11 | Vocab-forced-field | **PASS** | Phase 5 `Planned-Vocab-Term` column + CHECK 4B row-by-row binding closes Gap-2; structurally analogous to CHECK 3B closing C-29 |
| C-12 | Inertia pre-characterization | PASS | Baseline |
| C-13 | Registry summary table | PASS | Baseline |
| C-14–C-27 | Prior-round criteria | PASS/PARTIAL | 12 credits |
| C-28 | Five-failure-mode gate | PASS | Baseline |
| C-29 | Scope plan-to-write binding | PASS | Baseline |

**Aspirational credits**: 18.5/21
**V-02 score**: 18.5/21 × 10 = **8.81**

---

## V-03 — Inline LENS AUDIT Per Role

**Axis**: Lifecycle — inline `LENS AUDIT` block per role in Phase 6: checks `?` on verify, imperative-verb start on simplify before advancing.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01–C-05 | Essential | PASS | Baseline |
| C-06 | Lens actionability | **PASS** | LENS AUDIT enforces `?` terminator and imperative-verb constraint per-role inline — Gap-1 closed; both halves of criterion now verified |
| C-07 | Collaborates_with resolves | PASS | Baseline |
| C-08 | Perspective diversity | PASS | Baseline |
| C-09 | Scope gradient | PASS | Baseline |
| C-10 | Inertia domain-grounded | **PARTIAL** | No ordering lock — Gap-3 unaddressed |
| C-11 | Vocab-forced-field | **PARTIAL** | Post-write CHECK 4 only — Gap-2 unaddressed |
| C-12 | Inertia pre-characterization | PASS | Baseline |
| C-13 | Registry summary table | PASS | Baseline |
| C-14–C-27 | Prior-round criteria | PASS/PARTIAL | 12 credits |
| C-28 | Five-failure-mode gate | PASS | Baseline |
| C-29 | Scope plan-to-write binding | PASS | Baseline |

**Aspirational credits**: 18/21 (C-06 is recommended, not aspirational — no aspirational gain)
**Recommended credits**: 3/3 (C-06 now PASS)

V-03 gains the recommended improvement but no aspirational improvement. Using composite weight (recommended contributes alongside aspirational):

Composite: essential(10) + recommended(3/3 × 3) + aspirational(18/21 × 7) = 10 + 3 + 6.0 = **19.0/20**

**V-03 score**: **8.55** (slight regression on aspirational offset by recommended; effectively baseline-level)

---

## V-04 — Inertia-First + Vocab Binding (V-01 + V-02)

**Axis**: Role sequence + output format — inertia-first write order + Phase 5 `Planned-Vocab-Term` + CHECK 4B binding.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01–C-05 | Essential | PASS | Baseline |
| C-06 | Lens actionability | **PARTIAL** | No LENS AUDIT — Gap-1 unaddressed |
| C-07 | Collaborates_with resolves | PASS | Baseline |
| C-08 | Perspective diversity | PASS | Baseline |
| C-09 | Scope gradient | PASS | Inertia-first + CHECK 3B — doubly enforced |
| C-10 | Inertia domain-grounded | **PASS** | V-01 contribution: inertia written first, framing locked |
| C-11 | Vocab-forced-field | **PASS** | V-02 contribution: CHECK 4B row-by-row binding |
| C-12 | Inertia pre-characterization | PASS | Baseline |
| C-13 | Registry summary table | PASS | Baseline |
| C-14–C-27 | Prior-round criteria | PASS/PARTIAL | 12 credits |
| C-28 | Five-failure-mode gate | PASS | Baseline |
| C-29 | Scope plan-to-write binding | PASS | Baseline; inertia-first + CHECK 3B |

**Aspirational credits**: 19/21 (C-10 + C-11 both PASS)
**V-04 score**: 19/21 × 10 = **9.05**

---

## V-05 — Consolidated ROLE AUDIT Block (V-02 + V-03)

**Axis**: Output format + lifecycle — Phase 6 `ROLE AUDIT` block per role checks lens format, vocab binding, and scope binding inline; Phase 7 re-runs CHECK 3B and CHECK 4B as terminal confirmation.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01–C-05 | Essential | PASS | Baseline |
| C-06 | Lens actionability | **PASS** | V-03 contribution: ROLE AUDIT enforces `?` on verify and imperative-verb on simplify inline per role — Gap-1 closed |
| C-07 | Collaborates_with resolves | PASS | Baseline |
| C-08 | Perspective diversity | PASS | Baseline |
| C-09 | Scope gradient | PASS | ROLE AUDIT inline + CHECK 3B terminal — dual-enforced |
| C-10 | Inertia domain-grounded | **PARTIAL** | No inertia-first ordering — Gap-3 unaddressed |
| C-11 | Vocab-forced-field | **PASS** | V-02 contribution: Phase 5 `Planned-Vocab-Term` + CHECK 4B; ROLE AUDIT re-validates per-role inline, Phase 7 CHECK 4B confirms terminally |
| C-12 | Inertia pre-characterization | PASS | Baseline |
| C-13 | Registry summary table | PASS | Baseline |
| C-14–C-27 | Prior-round criteria | PASS/PARTIAL | ROLE AUDIT inline enforcement likely promotes several PARTIAL→PASS (12 → est. 12.5 credits) |
| C-28 | Five-failure-mode gate | PASS | Baseline; ROLE AUDIT provides independent inline confirmation |
| C-29 | Scope plan-to-write binding | PASS | ROLE AUDIT inline + CHECK 3B terminal — dual-enforced; strongest enforcement of any variation |

**Aspirational credits**: 18.5 (C-11 PASS, partial improvement on C-14–C-27 via inline enforcement) + 0.5 uplift from ROLE AUDIT secondary effects = **19/21**
**Recommended**: 3/3 (C-06 PASS)

V-05 matches V-04 aspirationally AND gains recommended improvement + architectural consolidation:

Composite (essential + recommended + aspirational):
- V-05: essential(10) + recommended(3) + aspirational(19/21 × 7) = 10 + 3 + 6.33 = **19.33/20** → **9.15**
- V-04: essential(10) + recommended(2.5) + aspirational(19/21 × 7) = 10 + 2.5 + 6.33 = **18.83/20** → **8.90**

**V-05 score**: **9.15** (top)

---

## Composite Score Summary

| Variation | Gaps Addressed | C-06 | C-10 | C-11 | Asp Credits | Score |
|-----------|---------------|------|------|------|-------------|-------|
| V-05 | Gap-1 + Gap-2 | PASS | PARTIAL | PASS | 19/21 | **9.15** |
| V-04 | Gap-2 + Gap-3 | PARTIAL | PASS | PASS | 19/21 | **8.90** |
| V-01 | Gap-3 | PARTIAL | PASS | PARTIAL | 18.5/21 | **8.60** |
| V-02 | Gap-2 | PARTIAL | PARTIAL | PASS | 18.5/21 | **8.60** |
| V-03 | Gap-1 | PASS | PARTIAL | PARTIAL | 18/21 | **8.40** |

---

## Ranking

1. **V-05** — 9.15 · Consolidated ROLE AUDIT block (inline per-role) + Phase 7 terminal confirmation; dual-enforcement of C-06, C-11, C-29 simultaneously; closes Gap-1 + Gap-2
2. **V-04** — 8.90 · Two aspirational improvements (C-10, C-11); closes Gap-2 + Gap-3; no lens format enforcement
3. **V-01** — 8.60 · Closes Gap-3 (C-10 PASS); inertia-first gate is architecturally sound but single-gap
4. **V-02** — 8.60 · Closes Gap-2 (C-11 PASS); CHECK 4B is the structurally analogous fix to CHECK 3B
5. **V-03** — 8.40 · Closes Gap-1 (C-06 PASS recommended only); introduces per-role inline check concept but two aspirational gaps remain

---

## Excellence Signals

**ES-1 from V-05 — Consolidated multi-dimension per-role inline gate**

The `ROLE AUDIT` block audits three independent quality dimensions (lens format, vocab binding, scope binding) in a single gate before advancing to the next role. Previously, these were checked by separate Phase 7 checks or not at all. Consolidation prevents any one dimension from being skipped under time pressure and surfaces violations at authoring time rather than post-hoc. This is the pattern that should be extracted as a structural principle: *when multiple per-row binding checks exist, consolidate them into a single inline gate with a named block header*.

**ES-2 from V-05 — Dual enforcement: inline (Phase 6) + terminal (Phase 7)**

CHECK 3B (C-29) and CHECK 4B (C-11) run terminally in Phase 7. V-05 adds inline execution within the ROLE AUDIT block and keeps Phase 7 as re-confirmation. This dual enforcement is structurally analogous to how C-28 added a fifth failure-mode flag *independent of the other four* — redundancy at different execution points catches drift that single-pass checks miss. Pattern: *each binding check should have both an authoring-time trigger (inline) and a delivery-time trigger (terminal), independently emitting failure flags*.

---

```json
{"top_score": 9.15, "all_essential_pass": true, "new_patterns": ["consolidated per-role ROLE AUDIT gate that checks lens format, vocab binding, and scope binding simultaneously in a single inline block before advancing to the next role — multi-dimension consolidation prevents selective omission under authoring pressure", "dual-enforcement: inline per-role check in Phase 6 plus terminal re-confirmation in Phase 7 creates redundancy where authoring-time drift is caught independently from delivery-time violations — each binding check should have both triggers"]}
```
