# trace-state — Round 11 Scoring (Rubric v9 / v25)

## Scoring Basis

V-01 and V-02 have full (or near-full) prompt text — scored rigorously against all 31 criteria.
V-03, V-04, V-05 have variation map descriptions only — estimated from axis, hypothesis, and targeted aspirationals. Marked `[EST]`.

---

## V-01 — Role Sequence: Finance → CS → Sales

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | 7-column table includes Starting State, Operation, Ending State — all columns required |
| C-02 | PASS | Preconditions + Postconditions columns; rule: "Write `none` if genuinely absent — never leave these blank" |
| C-03 | PASS | "List at least 2 invariants" per domain; Invariants Checked is a required table column |
| C-04 | PASS | Defect Register section: Defect type, Triggering operation, Reason all required |
| C-05 | PASS | Explicit Finance → CS → Sales with named lifecycle states per domain |

**Essential: 60/60**

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "Uniform table format throughout all three domain passes" declared |
| C-07 | PASS | Disqualifying patterns listed; positive example "Invoice amount must remain positive after creation" |
| C-08 | PASS | Race Condition Analysis section present; conflict or resolution explicitly required |

**Recommended: 30/30**

### Aspirational (2 pts each, cap 5 → max 10 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Negative Path Trace: invalid state, blocked op, unchanged state, named error all required |
| C-10 | FAIL | No reachability annotation instruction |
| C-11 | FAIL | Column headers are plain — no criterion ID annotations in field labels |
| C-12 | PASS | Both orderings explicitly required: Ordering 1 (A→B) and Ordering 2 (B→A) |
| C-13 | PASS | "Record which Step row(s) caused you to identify it — e.g., 'Derived From: Step 3'. Required; invariants without derivation references are not linked." |
| C-14 | FAIL | Column headers don't embed criterion IDs — write-time enforcement absent |
| C-15 | FAIL | No example row with placeholder anchors |
| C-16 | PASS | "No prose substitutions. A row replaced with a narrative paragraph invalidates the artifact." — named rule |
| C-17 | PASS | "Minimum 5 rows per domain pass. Minimum 15 rows total." — explicit numeric floor |
| C-18 | PASS | Disqualifying patterns: `"ID is not null"`, `"record exists"`, `"amount field is populated"`, `"status field is set"` — named anti-examples |
| C-19 | PASS | "A row replaced with a narrative paragraph **invalidates the artifact**" — explicit consequence |
| C-20 | PASS | "Invoice amount must remain positive after creation qualifies" — explicit positive model |
| C-21 | PASS | "describe independently; do not write 'same as above' or reference Ordering 1" — in race section |
| C-22 | PARTIAL | "Write `none` if Preconditions or Postconditions are genuinely absent" in rules preamble, not co-located at column level — misses strict field-label placement requirement |
| C-23 | PASS | "Silent omissions from this section invalidate the section." — Defect Register section-level clause |
| C-24 | FAIL | No example row → guard not applicable |
| C-25 | PASS | "Invariant Register" aggregates all domains; Derived From column required for every entry |
| C-26 | PASS | "Minimum 15 rows total across all three passes" — explicit cross-pass floor |
| C-27 | PASS | Four disqualifying patterns listed in explicit enumeration: `"ID is not null"`, `"record exists"`, `"amount field is populated"`, `"status field is set"` |
| C-28 | PASS | "Name the two concurrent operations: Op A: ___ / Op B: ___" — both slots required |
| C-29 | PASS | "actively confirm no state mutation occurred — this is not satisfied by recording the unchanged state; it requires an explicit verification statement" |
| C-30 | FAIL | No criterion-instruction fusion in field labels |
| C-31 | FAIL | No sub-criterion element decomposition in column headers |

Passing aspirationals: C-09, C-12, C-13, C-16, C-17, C-18, C-19, C-20, C-21, C-23, C-25, C-26, C-27, C-28, C-29 → **15 of 23 pass → cap 10/10**

### V-01 Composite: **60 + 30 + 10 = 100/100** ✦ GOLDEN

---

## V-02 — Numbered Steps with Sub-Element Labels

> **Note:** Text is incomplete — V-02 CS domain instructions cut off; Defect Register, Invariant Register, Negative Path Trace, and Race Condition Analysis sections are absent. Scoring reflects visible text; missing sections score FAIL.

### Essential (60 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | `Starting State [C-01a]`, `Operation Applied [C-01b]`, `State Changes [C-01c]`, `Ending State [C-01d]` — all labeled in step schema |
| C-02 | PASS | `Preconditions [C-02a — write "none" if genuinely absent]`, `Postconditions [C-02b — write "none" if genuinely absent]` |
| C-03 | PASS | `Invariants Checked [C-03 — minimum 2 per pass; never omit]` |
| C-04 | FAIL | Defect Register not present in visible text |
| C-05 | PASS | Sales, CS, Finance domains named with lifecycle states |

**Essential: 48/60 — C-04 FAIL → not golden regardless of composite**

### Recommended (30 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | "Uniform step format throughout all three passes" |
| C-07 | PASS | "Deal value must remain positive at Closed-Won qualifies"; disqualifying patterns listed |
| C-08 | FAIL | Race Condition Analysis not present in visible text |

**Recommended: 20/30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | FAIL | Negative Path Trace not in visible text |
| C-10 | FAIL | No reachability annotation |
| C-11 | PASS | `[C-01a]`, `[C-01b]`, `[C-02a]`, `[C-02b]`, `[C-03]` embedded as field labels inside step schema |
| C-12 | FAIL | Race section absent |
| C-13 | PASS | "cite the step number(s) that revealed it" — derivation pipeline required in Sales invariants |
| C-14 | PASS | Field labels embed criterion IDs: filling `Starting State [C-01a]` mechanically satisfies C-01a; satisfaction is structurally unavoidable |
| C-15 | PARTIAL | Example step has fully populated cells but uses real values rather than `…` placeholder anchors — does not meet strict `…`-anchor requirement |
| C-16 | PASS | "No prose substitutions. A step block replaced with narrative invalidates the artifact." |
| C-17 | PASS | "Minimum 5 steps per domain pass. Minimum 15 steps total." |
| C-18 | PASS | Disqualifying patterns listed: `"ID is not null"`, `"record exists"`, `"amount field is populated"` |
| C-19 | PASS | "invalidates the artifact" — explicit consequence |
| C-20 | PASS | "Opportunity close date cannot be earlier than creation date" + "Deal value must remain positive at Closed-Won" — two positive qualifying examples |
| C-21 | FAIL | Race section absent |
| C-22 | PASS | `[C-02a — write "none" if genuinely absent]` — nil-value instruction co-located at field label level ✦ (exceeds V-01 on this criterion) |
| C-23 | FAIL | Section-level invalidation clause not in visible text |
| C-24 | PASS | "do not reproduce in output" — explicit anti-literal-copy guard on example step |
| C-25 | FAIL | Invariant Register not in visible text |
| C-26 | PASS | "Minimum 15 steps total" |
| C-27 | PASS | Three-item exclusion list: `"ID is not null"`, `"record exists"`, `"amount field is populated"` |
| C-28 | FAIL | Race section absent |
| C-29 | FAIL | Negative Path section absent |
| C-30 | PASS | `[C-03 — minimum 2 per pass; never omit]` fuses criterion ID + behavioral directive in same annotation; `[C-02a — write "none" if genuinely absent]` same pattern ✦ **First live C-30** |
| C-31 | PASS | `[C-01a]`–`[C-01d]` decomposes C-01 into 4 sub-elements; `[C-02a]`/`[C-02b]` decomposes C-02 into 2 — each independently auditable ✦ **First live C-31** |

Passing aspirationals: C-11, C-13, C-14, C-16, C-17, C-18, C-19, C-20, C-22, C-24, C-26, C-27, C-30, C-31 → **14 of 23 pass → cap 10/10**

### V-02 Composite: **48 + 20 + 10 = 78/100** ✗ NOT GOLDEN (C-04 + C-08 block essential gate)

**V-02 Unique Contributions to v9 rubric:** First confirmed firing of C-30 and C-31. Also first proper C-22 (field-level nil-value co-location) and C-24 (example anti-copy guard).

---

## V-03 — Race Section 2× Structural Weight `[EST]`

Targeted aspirationals: C-12, C-21, C-28, C-23, C-29

All essentials assumed PASS (no structural reason to drop any). Recommended all PASS — race emphasis amplifies C-08. Four-sub-section race schema fires: C-12 (both orderings), C-21 (anti-lazy-copy in race), C-28 (named op pair), C-23 (section-level invalidation in race), C-29 (active mutation verification). Baseline aspirationals (C-09, C-13, C-16–C-20, C-25–C-27) likely PASS. C-30, C-31, C-11, C-14 not targeted — FAIL.

**Estimated: ~90–100/100** — GOLDEN

---

## V-04 — Conversational Register + Inertia Framing `[EST]`

Targeted aspirationals: C-18, C-20, C-27, C-16, C-19

Accessible framing strengthens invariant quality anchors and consequence declarations. Risk: conversational register undercuts structural formalism — C-11, C-14, C-30, C-31 unlikely; C-06 may weaken; C-22 field-level co-location less likely; C-21 anti-lazy-copy may be soft-stated rather than declared. All essentials expected PASS if skeleton is sound. Recommended C-06 at PARTIAL risk.

**Estimated: ~75–82/100** — borderline; may not reach golden if C-06 weakens

---

## V-05 — Schema-First + Criterion-Instruction Fusion `[EST]`

Targeted aspirationals: C-30, C-31, C-14, C-11, C-19

This is the intended systematic successor to V-02's partial attempt. Full schema-first design with criterion IDs + behavioral directives fused into every field label fires C-30, C-31, C-11, C-14 simultaneously. Expected to replicate V-01 baseline (C-09, C-12, C-13, C-16–C-20, C-21, C-22, C-23, C-25–C-29) while adding the four new structural criteria V-01 misses. All essentials PASS. First variation designed to potentially score C-30 + C-31 + C-11 + C-14 together.

**Estimated: ~95–100/100** — GOLDEN; may exceed V-01 on criterion-coverage breadth

---

## Ranking

| Rank | Var | Score | Essential Gate | Notable |
|------|-----|-------|---------------|---------|
| 1 | V-01 | **100** (confirmed) | PASS — GOLDEN | Perfect composite; misses only C-10/C-11/C-14/C-15/C-24/C-30/C-31 |
| 2 | V-05 | ~95–100 (est.) | PASS — GOLDEN | First systematic C-30+C-31+C-11+C-14 coexistence |
| 3 | V-03 | ~90–100 (est.) | PASS — GOLDEN | Strongest race section; C-12/C-21/C-28/C-23/C-29 all fired |
| 4 | V-02 | **78** (confirmed, incomplete) | **FAIL** (C-04, C-08 absent) | First live C-30 + C-31; C-22 field-level; C-24 example guard |
| 5 | V-04 | ~75–82 (est.) | PASS (est.) | Conversational framing sacrifices structural criteria |

---

## Excellence Signals from V-01 (top confirmed)

1. **Dual-level invalidation** — artifact-level clause (`"invalidates the artifact"`) in prose rules (C-19) **and** section-level clause (`"Silent omissions from this section invalidate the section"`) in the Defect Register (C-23). Two enforcement granularities, structurally independent.

2. **Cross-domain Invariant Register as synthesis surface** — the `Invariant Register` table with Domain and `Derived From` columns forces C-13 (trace-row linkage) and C-25 (aggregation) to be satisfied by the same structural move. One table satisfies both criteria simultaneously.

3. **Enumerated exclusion list + positive qualifying example as a paired invariant quality gate** — listing four disqualifying patterns (C-27) alongside a named qualifying example (C-20) in the same invariant section creates a complete two-sided quality model: what fails the bar and what clears it. Neither alone is sufficient; the pairing eliminates ambiguity.

4. **Op-pair naming template + anti-lazy-copy constraint in the race section** — `Op A: ___ / Op B: ___` fills C-28 while "do not write 'same as above'" fills C-21; both are co-located in the race section header, so they are structurally inseparable from the section they govern.

5. **Active mutation-verification directive** — "actively confirm no state mutation occurred — this is not satisfied by recording the unchanged state" goes beyond passive state representation and fires C-29; the negative-contrast instruction ("not satisfied by recording") makes the distinction testable.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["dual-level invalidation: artifact-level clause (C-19) and section-level clause (C-23) declared in separate structural locations", "cross-domain Invariant Register with Derived From column satisfies C-13 and C-25 simultaneously from one table structure", "enumerated four-item exclusion list (C-27) paired with explicit positive qualifying example (C-20) in same invariant section — complete two-sided quality gate"]}
```
