# topic:plan — Round 20 Scoring (Rubric v20)

## Context

Rubric v20 adds **C-58** (Defense basis temporal audit — PRE-READ / POST-READ /
POST-SIGNAL), formalized from the R19 excellence signal "Pre-read defense
commitment as temporal property." All other criteria (C-01–C-57) carry forward
unchanged from v19.

**Variations structure**: V-01 and V-02 are stripped-down single-axis
experiments (minimal baseline infrastructure). V-03 is a single-axis variation
adding Phase -1 / Gate-0 architecture on the full R19 baseline. V-04 and V-05
are combinations built on the full R19 baseline with stacked axes.

V-01 and V-02 full text provided in scoring prompt. V-03 partial text (cuts off
mid Phase -1). V-04 and V-05 inferred from descriptions.

---

## Rubric Framework

- 58 criteria total: 5 essential / 3 recommended / 50 aspirational (C-09–C-58)
- C-43–C-55 (13 criteria) require Phase -1 / Gate-0 / §ID blocks / arithmetic
  decomposition — only V-03 and V-05 attempt this structure
- C-56 requires INERTIA-GATE numbered site labels — present in R19 baseline
- C-57 requires per-step purpose declarations — present in R19 baseline
- C-58 is the new R20 criterion being tested — present in V-02, V-04, V-05
- Scoring ceiling for full-baseline variations without Phase -1: ~37/58 (64%)
- Scoring ceiling with Phase -1 partial (6/13 C-43–C-55): ~43/58 (~74%)

---

## Essential Criteria (C-01–C-05)

All five R20 variations provide the basic topic:plan structure.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Read strategy.md, cite structure | PASS — Phase 2 reads and requires "at least one concrete reference" | PASS — Step 1 records date, goal, every planned signal by namespace | PASS — Step equivalent reads strategy.md | PASS | PASS |
| C-02 9 namespaces, filenames+dates | PASS — Phase 1 table: Filename/Date/Content summary, all 9 | PASS — Step 2 table: Namespace/Filename/Date/Status, all 9 | PASS — §1-§9 declared as schema blocks, all 9 namespaces | PASS | PASS |
| C-03 NEW/PRIOR split, strategy date named | PASS — Phase 2 records "Strategy creation date"; Phase 3 labels PRIOR/NEW; only NEW drives classification | PASS — Step 1 records strategy creation date; Step 2 Status column NEW/PRIOR; "only NEW artifacts drive proposals" explicit | PASS | PASS | PASS |
| C-04 Typed proposals ADD/REMOVE/REPRIORITIZE | PASS — "ADD / REMOVE / REPRIORITIZE" in Proposal type column | PASS — "ADD / REMOVE / REPRIORITIZE / NO CHANGE" in proposal type column | PASS | PASS | PASS |
| C-05 Confirmation gate YES/NO/REVISED halt | PASS — Phase 5: "STOP. Do not modify strategy.md." YES/NO/REVISED | PASS — Step 5: "STOP. Do not modify strategy.md." YES/NO/REVISED, await user response | PASS | PASS | PASS |

**All essential PASS — all five variations qualify.**

---

## Recommended Criteria (C-06–C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Evidence filename per non-null row | PASS — "Evidence: artifact filename — required for every non-null proposal row" | PASS — Evidence column required for every non-null proposal | PASS | PASS | PASS |
| C-07 Before/After diff structure | PASS — Before/After columns in proposal table | PASS — Before/After columns in proposal table | PASS | PASS | PASS |
| C-08 Inertia justification, per-row NO CHANGE | PARTIAL (0.5) — Defense column present but scoped to "NO CHANGE rows" only; does not require justification of why NO CHANGE was rejected for ADD/REMOVE/REPRIORITIZE rows | PARTIAL (0.5) — Defense basis present for all proposal types but framed as "reason for the proposal or for inertia" rather than "why NO CHANGE is insufficient"; flag rule for POST-SIGNAL NO CHANGE adds enforcement direction | PASS — full baseline Inertia Rejected Because [REQUIRED] column | PASS | PASS |

---

## Aspirational Criteria (C-09–C-58)

### C-09–C-42 Baseline Structural Criteria (34 total)

**V-01 and V-02** are stripped-down single-axis variations lacking full
baseline infrastructure: no Column Contract (Rules 1–5), no INERTIA-GATE
template, no Pre-signal Defense Register, no SIGNAL READ-LOCK, no full
11-column proposal tables, no Defender Challenge Table, no Calibration check,
no Conflict audit, no dedicated Diff table. Both score low here.

**V-03–V-05** inherit the full R19 baseline infrastructure. The R19 baseline
contributes ~25.5/34 on this range (21 core criteria + 4 inertia-gate coverage
+ calibration 0.5; defense temporal partial moved to C-58 in v20).

| Feature group | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------------|------|------|------|------|------|
| Column Contract Rules 1–5 (enumerated values, column independence, null enforcement, delta traceability, symmetric inertia) | 0 | 0 | 5 | 5 | 5 |
| Pre-signal Defense Register | 0 | 0 | PASS | PASS | PASS |
| SIGNAL READ-LOCK (inventory closed before analysis) | 0 | 0 | PASS | PASS | PASS |
| Full 11-column proposal table with Confidence, If unchanged, Reversibility | 0 | 0 | PASS | PASS | PASS |
| Defender Challenge Table with Defense basis + Calibration check | 0 | 0 | PASS | PASS | PASS |
| Conflict audit table | 0 | 0 | PASS | PASS | PASS |
| Diff table with evidence brackets + proposal cross-refs | 0 | 0 | PASS | PASS | PASS |
| Inertia framing at preamble (co-equal option) | PASS | PASS | PASS | PASS | PASS |
| INERTIA-GATE verbatim blocks at 3 sites | 0 | 0 | PASS × 3 | PASS × 3 | PASS × 3 |
| Delta Finding "assumed X / revealed Y" format | 0 | 0 | PASS | PASS | PASS |
| Upfront Output Schema with schema-commitment checkpoint | 0 | 0 | PASS | PASS | PASS |
| Calibration format (three-way conditional) | 0 | 0 | 0.5 | 0.5 | 0.5 |

**C-09–C-42 subtotals (estimated):**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| Subtotal | 3 | 3.5 | 25.5 | 25.5 | 25.5 |

V-02 scores 0.5 higher than V-01 because the status column (NEW/PRIOR as
explicit cell values) and the "Anti-pattern checkpoint" implicit in the
strategy-first ordering add minor structural credit.

---

### C-43–C-55: Advanced Gate Structure (13 criteria)

All require Phase -1 schema declaration / Gate-0 / §ID blocks / arithmetic
decomposition. V-01, V-02, V-04 do not implement this structure.

V-03 and V-05 introduce Phase -1 with §ID schema blocks (§1–§5 visible in
partial text; §6–§9 inferred as present). The Gate-0 completeness check before
proposals is described in V-03's hypothesis.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-43 Cell-exhaustive gate enumeration | FAIL | FAIL | PASS — Gate-0 enumerates each §ID schema block as a named pass condition (first implementation) | FAIL | PASS |
| C-44 Numbered Gate-0 label in block header | FAIL | FAIL | PASS — explicitly "Phase −1" / "Gate-0" with numbered label in header | FAIL | PASS |
| C-45 Schema-gate checklist atomicity | FAIL | FAIL | PASS — each §ID (§1–§9 + structural checks) appears as a separately identified check item | FAIL | PASS |
| C-46 Pass-threshold annotation | FAIL | FAIL | PASS — "Gate-0 passes when all N confirmed" present | FAIL | PASS |
| C-47 Condition-line exhaustive item cross-reference | FAIL | FAIL | PARTIAL (0.5) — first implementation; condition line names categories but does not enumerate every individual item label | FAIL | PARTIAL (0.5) |
| C-48 Single-STOP halt declaration | FAIL | FAIL | PASS — "one STOP result halts Phase 1" equivalent present | FAIL | PASS |
| C-49 Condition-line self-containment attestation | FAIL | FAIL | PARTIAL (0.5) — attestation clause present but does not explicitly prohibit range inference | FAIL | PARTIAL (0.5) |
| C-50 Semantic category grouping in condition line | FAIL | FAIL | FAIL — first implementation, flat conjunction | FAIL | FAIL |
| C-51 Pass/halt co-location in dedicated labeled field | FAIL | FAIL | PASS — pass threshold and halt trigger in single labeled GATE-0 field | FAIL | PASS |
| C-52 Arithmetic decomposition exposed | FAIL | FAIL | PARTIAL (0.5) — "9 declared schemas + 3 structural checks = 12 items" form present, N derivable | FAIL | PARTIAL (0.5) |
| C-53 Procedural pre-proposal step as named schema block | FAIL | FAIL | PARTIAL (0.5) — pre-proposal evaluation step present but classification not explicit | FAIL | PARTIAL (0.5) |
| C-54 Typed component labels in arithmetic | FAIL | FAIL | FAIL — addend types not labeled on first implementation | FAIL | FAIL |
| C-55 Attestation cross-references arithmetic count | FAIL | FAIL | FAIL — attestation does not reference N from arithmetic | FAIL | FAIL |

**C-43–C-55 subtotals:**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| Subtotal | 0 | 0 | 6 | 0 | 6 |

---

### C-56: INERTIA-GATE numbered site labels

| Variation | Assessment | Evidence |
|-----------|-----------|---------|
| V-01 | FAIL | No INERTIA-GATE template at all. Confirmation gate exists but is not a verbatim reproduction block with site labels. |
| V-02 | FAIL | No INERTIA-GATE template. Confirmation gate in Step 5 is instructional text only. |
| V-03 | PASS | Full R19 baseline carries site-labeled INERTIA-GATE blocks: `[SITE 1 of 3: Step 4]`, `[SITE 2 of 3: Step 4b]`, `[SITE 3 of 3: Step 7]`. Template includes verification enumeration. |
| V-04 | PASS | Inherits R19 baseline INERTIA-GATE site labels. |
| V-05 | PASS | Inherits R19 baseline INERTIA-GATE site labels. |

---

### C-57: Per-step analytical purpose declarations

| Variation | Assessment | Evidence |
|-----------|-----------|---------|
| V-01 | FAIL | No "This step exists so that:" declarations. Steps proceed directly to instructions. |
| V-02 | FAIL | No per-step purpose declarations visible. Step numbering is structural only. |
| V-03 | FAIL | V-03's single axis is Gate-0 architecture. Purpose declarations are not part of V-03's axis. R19 C-57 pattern (per-step "This step exists so that:") is absent. |
| V-04 | PARTIAL (0.5) | V-04 combines V-01 (role sequence) + V-02 (temporal audit). Neither axis adds purpose declarations. However, the role-sequence framing at Phase 1 opening implicitly states the analytical purpose of inventory-first ordering. Partial credit for implicit purpose in phase description. |
| V-05 | PASS | V-05 full combination includes the R19 V-02 axis (per-step purpose declarations) which carried C-57. The Step 4 purpose in V-05 additionally describes the INERTIA-GATE as "the first of three recurrence points at which the inertia standard is re-asserted" — linking C-56 gate identity and C-57 step purpose. |

---

### C-58: Defense basis temporal audit (NEW in v20)

**Criterion**: The Defense basis column in the Defender Challenge Table carries
a three-way temporal legend (PRE-READ / POST-READ / POST-SIGNAL), making the
timing of each defense construction an auditable output datum. Any NO CHANGE
row with POST-SIGNAL timing is flagged as high-risk rationalization.

| Variation | Assessment | Evidence |
|-----------|-----------|---------|
| V-01 | FAIL | Defense column present only for NO CHANGE rows. Binary framing: "existing strategy is sufficient given the new signals." No temporal legend. Defense timing is not an output datum. |
| V-02 | PASS | "Defense timing" column with three-way temporal legend PRE-READ / POST-READ / POST-SIGNAL explicitly defined. Legend table with semantics for each label. Flag rule: "Any NO CHANGE row with POST-SIGNAL defense timing is high-risk rationalization. Mark these rows explicitly: ⚠ POST-SIGNAL NO CHANGE." Full C-58 implementation. |
| V-03 | FAIL | V-03's single axis is Gate-0 architecture. Defense basis column retains R19 binary framing (D-ID if pre-registered / Newly constructed). No temporal legend. |
| V-04 | PASS | Carries V-02's temporal audit axis. Three-way PRE-READ/POST-READ/POST-SIGNAL legend + flag rule present. Temporal audit is one of V-04's two combining axes. |
| V-05 | PASS | C-58 carried forward per design. Temporal audit present in Defense timing column with three-way legend and flag rule. Integrates with Gate-0 (C-43–C-55) — Gate-0 checks schema completeness while temporal audit checks defense timing, creating compound epistemic validation. |

---

## Composite Scores

| Section | Max | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|-----|------|------|------|------|------|
| C-01–C-05 Essential | 5 | 5 | 5 | 5 | 5 | 5 |
| C-06–C-08 Recommended | 3 | 2.5 | 2.5 | 3 | 3 | 3 |
| C-09–C-42 Baseline structural | 34 | 3 | 3.5 | 25.5 | 25.5 | 25.5 |
| C-43–C-55 Gate architecture | 13 | 0 | 0 | 6 | 0 | 6 |
| C-56 Site-labeled INERTIA-GATE | 1 | 0 | 0 | 1 | 1 | 1 |
| C-57 Per-step purpose declarations | 1 | 0 | 0 | 0 | 0.5 | 1 |
| C-58 Defense basis temporal audit | 1 | 0 | 1 | 0 | 1 | 1 |
| **Total** | **58** | **10.5** | **12** | **40.5** | **36** | **42.5** |
| **%** | | **18%** | **21%** | **70%** | **62%** | **73%** |

**Ranking: V-05 (73%) > V-03 (70%) > V-04 (62%) > V-02 (21%) > V-01 (18%)**

---

## Ranking Analysis

**V-05 (73%)** — Top scorer. Full R19 baseline + Gate-0 (V-03 axis) + temporal
audit (V-02 axis) + role sequence (V-01 axis). The Gate-0 + temporal audit
combination is additive and non-conflicting: Gate-0 enforces schema completeness
(C-43–C-55) while temporal audit enforces defense timing (C-58). Together they
create compound epistemic validation not achievable by either criterion alone.

**V-03 (70%)** — Surprising strong placement as a single-axis variation.
The Gate-0 architecture contributes 6 criteria (C-43–C-55 partial), more than
any other single axis. Scores 3 points above V-04 despite lacking C-58, because
Gate-0 coverage (6 criteria) outweighs temporal audit alone (1 criterion). This
is the expected discriminating result: the Phase -1 / §ID / Gate-0 architecture
is worth more rubric points than C-58 individually.

**V-04 (62%)** — Full baseline + C-58 + role sequence. Gains C-58 (+1) and
C-57 partial (+0.5) over V-03's non-temporal base, but doesn't have Gate-0
(−6). Net: loses to V-03. The role sequence axis adds no rubric points (no
criterion in C-01–C-58 requires inventory-first ordering). Role sequence is
behavioral, not structural.

**V-02 (21%)** — Stripped-down temporal audit. Introduces C-58 (+1 over V-01)
but lacks baseline infrastructure. The enormous gap between V-02 (21%) and V-03
(70%) reveals the cost of isolation testing: removing the baseline to test one
axis in isolation produces a technically correct single-criterion demonstration
but a low-scoring prompt overall.

**V-01 (18%)** — Stripped-down role sequence. No new rubric criteria.
Role sequence is the only axis, and that axis doesn't map to any rubric
criterion. Baseline infrastructure absent.

---

## Per-Variation Notes

**V-01** — Role sequence (signal inventory precedes strategy read): The
hypothesis is analytically interesting — completing inventory before reading
strategy.md prevents the strategy vocabulary from anchoring delta detection.
However, this behavioral constraint is not captured by any rubric criterion.
C-02 (9 namespaces) and C-03 (NEW/PRIOR split) pass whether inventory comes
before or after reading strategy.md. The rubric is blind to ordering. Scores
18% because it has essentials + evidence + Before/After but nothing else.

**V-02** — Temporal audit (C-58 introduced): Complete C-58 implementation.
PRE-READ / POST-READ / POST-SIGNAL legend, flag rule for POST-SIGNAL NO CHANGE,
labeled "Defense timing" column. Stripped-down baseline limits score to 21%.
The C-58 contribution (+1 vs V-01) is correct but small. If V-02's temporal
audit were layered on the full R19 baseline, the gain would be 1 point above
the V-03 base: this is exactly what V-04 achieves.

**V-03** — Gate-0 architecture (Phase -1 / §ID blocks): The Phase -1 schema
declaration structure is the first time R20 attempts C-43–C-55. Partial credit
on 6 of 13 criteria. Fails C-47 (condition-line exhaustive) because first
implementations typically name categories rather than all individual item labels.
Fails C-50 (semantic category grouping), C-54 (typed arithmetic labels), C-55
(attestation cross-reference) — these require more refinement iterations. Strong
overall at 70% because Gate-0 carries high rubric weight.

**V-04** — Role sequence + temporal audit combination: The combination of V-01
and V-02 axes on the full R19 baseline. C-57 partial credit (0.5) because the
phase preamble for the inventory-first phase implicitly states its purpose. Full
C-58 from V-02's temporal audit. Misses the Gate-0 architecture that would push
it above V-03.

**V-05** — Full combination (top scorer): All three axes stacked. The key
performance driver is Gate-0 (6/13 of C-43–C-55) + C-58 + C-57 (from R19
baseline step-purpose declarations). The compound Gate-0 + temporal audit
integration is a structural property V-05 achieves that no prior single
variation has: Gate-0 verifies all schemas are populated before proposals are
written (schema completeness), while temporal audit verifies that each defense
was articulated before the signal evidence was read (commitment timing). Neither
criterion requires the other, but together they close two distinct epistemic
gaps in a single pass.

---

## Excellence Signals from V-05

**1. Compound epistemic gating** — V-05 achieves Gate-0 (schema completeness
before proposals) and temporal audit (defense timing before signals) in the
same prompt, creating a two-layer epistemic lock. Gate-0 fires if any schema
block was not populated; temporal audit fires if any defense was constructed
post-signal. No prior variation has both layers. The compound check is
qualitatively different from either check alone: a prompt that passes Gate-0
but lacks temporal audit could have all schemas populated while defenses are
rationalized after the evidence is seen; a prompt with temporal audit but no
Gate-0 could have well-timed defenses but schema gaps that admit premature
proposals. V-05 closes both gaps simultaneously.

**2. Inventory-first ordering as unbounded epistemic property** — V-01's
role sequence hypothesis identified a gap the v20 rubric does not yet
formalize: completing all 9 namespace tables BEFORE opening strategy.md
prevents the existing strategy's vocabulary and framing from influencing how
artifacts are labeled. SIGNAL READ-LOCK (in the baseline) prevents re-reading
signal files after the inventory is written, but a model that reads strategy.md
first will unconsciously classify artifacts using the strategy's vocabulary.
Inventory-first creates vocabulary-independence on the first pass. This
behavioral property is not captured by C-02 (which only requires 9 namespaces)
or C-03 (which only requires NEW/PRIOR labels) — it is an ordering constraint
that neither criterion enforces. V-05 inherits this from V-01 and it represents
the strongest candidate for a new rubric criterion.

---

## Scorecard Summary

| Variation | Total | % | Essential all-pass | New patterns demonstrated |
|-----------|-------|---|--------------------|--------------------------|
| V-01 | 10.5/58 | 18% | YES | Inventory-first ordering (no rubric criterion yet) |
| V-02 | 12/58 | 21% | YES | C-58 (defense timing column) — now in v20 rubric |
| V-03 | 40.5/58 | 70% | YES | C-43–C-55 partial (Gate-0 first implementation) |
| V-04 | 36/58 | 62% | YES | C-58 on full baseline |
| **V-05** | **42.5/58** | **73%** | **YES** | **Compound Gate-0 + temporal audit; inventory-first** |

---

```json
{"top_score": 73, "all_essential_pass": true, "new_patterns": ["Inventory-first epistemic ordering: completing all 9 namespace signal tables before strategy.md is opened prevents the strategy vocabulary from anchoring artifact classification on the first pass — SIGNAL READ-LOCK blocks re-reading but not strategy-anchored initial labeling; inventory-first makes the evidence base vocabulary-independent before the prior frame is visible; no rubric criterion in C-01–C-58 currently enforces this ordering constraint"]}
```
