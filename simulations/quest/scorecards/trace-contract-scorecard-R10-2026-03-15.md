## Scorecard: trace-contract v10 — Round 10

**Date:** 2026-03-15
**Rubric:** v10 (C-01–C-30; essential C-01–C-05; max composite 110; golden threshold: all essential pass + composite ≥ 80)
**New criteria this round:** C-29 (`mechanism-type-shared:` unconditionally required with fix-strategy semantics), C-30 (`mechanism-distribution:` compact computed aggregate in Summary)

---

### Scoring Approach

C-01–C-28 (R9 ceiling = 100 pts): Essential (C-01–C-05, 12 pts each = 60), Recommended (C-06–C-13, 2.5 pts each = 20), Aspirational (C-14–C-28, ~1.33 pts each = 20). C-29: 5 pts. C-30: 5 pts. Max = 110.

---

### V-01 — Role Sequence: Connectors Expert Owns Patterns Synthesis (C-29 isolation)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Three contract surfaces | PASS | "Cover all three contract surfaces: Success path, Error path, At least one edge case" — required in S2 |
| C-02 | Every element in Diff | PASS | "Every element must appear. Elements present in Expected Output but absent from the Diff are silent omissions — the trace fails C-02 regardless of finding quality." |
| C-03 | Spec citation per element | PASS | "An expected element without a spec citation is not a valid contract entry." |
| C-04 | Gate token format | PASS | `[EXPECTED-SEALED \| clauses:{N} \| date:{YYYY-MM-DD} \| author:contract-expert \| phase:1-complete]` |
| C-05 | Mechanism hypothesis | PASS | Self-test in all three finding tiers: "If YES — symptom restatement; rewrite naming the internal mechanism." |
| C-06–C-22 | Earlier criteria (inherited) | PASS | Role-sequence axis does not touch severity tiers, rate-limit or auth edge cases, or earlier structural requirements. No regression evidence. |
| C-23 | Gate metadata manifest | PASS | Gate carries `clauses:N`, `date:`, `author:`, `phase:1-complete` — all four required identity fields. |
| C-24 | Multi-branch Patterns | PASS | Three explicit branch templates: Zero (`no-pattern-confirmation:`), Singleton (`single-finding-ref:` + `root-cause:`), Multi-pattern (`pattern-N:` blocks). "This section may not be silently omitted." |
| C-25 | Hypothesis self-test rule | PASS | "Could you have written this from the deviation line alone, without knowing the system? YES — symptom restatement; rewrite naming the internal mechanism. NO — mechanism; proceed." |
| C-26 | Post-findings closure token | PASS | `[FINDINGS-RESOLVED \| gate-clauses:{N} \| clauses-resolved:{M} \| phase:5-complete]` with CLAUSE-GAP guard. |
| C-27 | Branch template slots | PASS | Singleton: `single-finding-ref:`, `root-cause:`, `mechanism-type-shared: [... -- REQUIRED]`, `fix-strategy:`, `attribution:`, `single-fix:`. Multi: `pattern-N:` with `root-cause:`, `mechanism-type-shared: [... -- REQUIRED]`, `fix-strategy:`, `findings:`, `single-fix:`. Zero: `no-pattern-confirmation:`. |
| C-28 | Per-finding mechanism-type token | PASS | All three tiers carry `mechanism-type: [field-mapping \| serialization-path \| conditional-branch \| lifecycle-event \| schema-contract \| TAXONOMY-GAP + explanation]`. |
| C-29 | `mechanism-type-shared:` required + fix-strategy semantics | **PASS** | Singleton: `mechanism-type-shared: [... -- REQUIRED]` with dedicated `fix-strategy: [same-class: one spec or implementation change resolves all findings in this group \| mixed: findings require independent fixes — enumerate per finding]`. Multi-pattern: same. Role framing provides the structural reason: "Because the same expert who authored the contract specification groups findings by mechanism class, `mechanism-type-shared:` is not an optional annotation — it is the expert's required statement of mechanism alignment." |
| C-30 | `mechanism-distribution:` computed aggregate | **FAIL** | Summary still carries pipe-delimited placeholder: `Mechanism taxonomy distribution: field-mapping:{N} \| serialization-path:{N} \| conditional-branch:{N} \| lifecycle-event:{N} \| schema-contract:{N} \| TAXONOMY-GAP:{N}`. No enumeration instruction. C-30 is not targeted by this axis. |

**Essential**: 5/5 | **Recommended**: all pass | **Aspirational**: all pass | **C-29**: PASS (+5) | **C-30**: FAIL (+0)

```
composite = 100 (C-01–C-28 all pass) + 5 (C-29) + 0 (C-30) = 105/110
```

**Score: 105/110 — GOLDEN** (all essential pass, composite ≥ 80)

---

### V-02 — Output Format: Computed Mechanism-Distribution Aggregate in Summary (C-30 isolation)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Three contract surfaces | PASS | "Cover all three contract surfaces: Success path, Error path, At least one edge case" |
| C-02 | Every element in Diff | PASS | "Every element must appear. Missing elements are silent omissions — the trace fails C-02 regardless of finding quality." |
| C-03 | Spec citation per element | PASS | "An expected element without a spec citation is not a valid contract entry." |
| C-04 | Gate token format | PASS | `[EXPECTED-SEALED \| clauses:{N} \| date:{YYYY-MM-DD} \| author:contract-expert \| phase:1-complete]` |
| C-05 | Mechanism hypothesis | PASS | Self-test present in all three finding tiers. |
| C-06–C-22 | Earlier criteria (inherited) | PASS | Output-format axis targets only Summary. No regression in S2–S5. |
| C-23 | Gate metadata manifest | PASS | Gate carries all four identity fields including `clauses:N`. |
| C-24 | Multi-branch Patterns | **PARTIAL** | "This section may not be silently omitted" is present. Zero/singleton are conflated: "If no findings share a root cause (or if there are zero or one findings), write: No cross-finding patterns detected." Singleton is not a named distinct branch. The three-case named branch instruction structure from C-24 is absent. |
| C-25 | Hypothesis self-test rule | PASS | "Could you have written this from the deviation line alone without system knowledge? YES — rewrite." |
| C-26 | Post-findings closure token | PASS | `[FINDINGS-RESOLVED \| gate-clauses:{N} \| clauses-resolved:{M} \| phase:5-complete]` with CLAUSE-GAP guard. |
| C-27 | Branch template slots | **FAIL** | Patterns step is instruction-based only: "group them, name the shared mechanism, list the finding IDs, and state the single fix." No pre-printed `no-pattern-confirmation:`, `single-finding-ref:`, `root-cause:`, or `pattern-N:` structural slots. The branch-template structure required by C-27 is absent. |
| C-28 | Per-finding mechanism-type token | PASS | All three tiers carry `mechanism-type:` with taxonomy enumeration. |
| C-29 | `mechanism-type-shared:` required + fix-strategy semantics | **FAIL** | Patterns branch templates are absent (C-27 regression), so there are no structural slots to carry `mechanism-type-shared:`. Step 7 says "note whether grouped findings share a mechanism-type token — same-type groupings *often indicate* a single systemic fix" — advisory framing only, not a required structural field. C-29 is not targeted by this axis. |
| C-30 | `mechanism-distribution:` computed aggregate | **PASS** | Summary carries `mechanism-distribution: [type]:[count] [type]:[count] ...` with explicit enumeration instruction: "Walk through every finding block in S5. For each finding, read its `mechanism-type:` field. Tally the count per type token. Write the result as space-separated type:count pairs, omitting types with zero occurrences. Example: `mechanism-distribution: field-mapping:2 serialization-path:1`... This aggregate is not a template to fill with estimates — it is enumerated directly from the S5 finding blocks." |

**Essential**: 5/5 | **Recommended**: all pass | **Aspirational**: C-24 PARTIAL (−0.67), C-27 FAIL (−1.33) | **C-29**: FAIL (+0) | **C-30**: PASS (+5)

```
composite ≈ 100 − 0.67 (C-24 partial) − 1.33 (C-27 fail) + 0 (C-29) + 5 (C-30) = 103/110
```

**Score: ~103/110 — GOLDEN** (all essential pass, composite ≥ 80)

**Note**: V-02's regression on C-24/C-27 is an artifact of focusing the axis change on Summary while simplifying the Patterns step from the R9 V-05 base. The design intent was only to change the Summary aggregate; the Patterns simplification is an incidental defect.

---

### V-03 — Lifecycle Emphasis: Taxonomy Synthesis Step (C-29 + C-30 via census)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Three contract surfaces | PASS | Three surfaces required in S2. |
| C-02 | Every element in Diff | PASS | Silent omission rule present. |
| C-03 | Spec citation per element | PASS | "An expected element without a spec citation is not a valid contract entry." |
| C-04 | Gate token format | PASS | Full metadata gate token required. |
| C-05 | Mechanism hypothesis | PASS | Self-test present in all finding tiers. |
| C-06–C-22 | Earlier criteria | PASS | Lifecycle axis inserts S5.5 between S5 and closure. No regression in earlier structure. |
| C-23 | Gate metadata manifest | PASS | `[EXPECTED-SEALED \| clauses:{N} \| date:{YYYY-MM-DD} \| author:contract-expert \| phase:1-complete]` |
| C-24 | Multi-branch Patterns | PASS | Three named branches with distinct cardinality conditions and non-omission clause. |
| C-25 | Hypothesis self-test rule | PASS | Self-test decision procedure in all finding tiers. |
| C-26 | Post-findings closure token | PASS | Closure token placed after S5.5 (both sub-tasks complete before gate closes). |
| C-27 | Branch template slots | PASS | Singleton: `single-finding-ref:`, `root-cause:`, `mechanism-type-shared: [copy from Step 5.5 Sub-task B]`, `single-fix: [... enumerate per finding if 'mixed']`. Multi: `pattern-N:` with `root-cause:`, `mechanism-type-shared:`, `findings:`, `single-fix:`. Zero: `no-pattern-confirmation:`. |
| C-28 | Per-finding mechanism-type token | PASS | All tiers carry `mechanism-type:` from taxonomy. |
| C-29 | `mechanism-type-shared:` required + fix-strategy semantics | **PASS** | S5.5 Sub-task B creates a required lifecycle position: "For each candidate Patterns group (two or more findings sharing a root cause), read the `mechanism-type:` token of each finding in the group. Determine: do all findings in this group share a single mechanism type, or do they span multiple types?" Output: `group-candidate-N: findings=[F-NN, F-MM] mechanism-type-shared=[type token or 'mixed']` — this is then copied into the branch template. The field is unconditionally required (lifecycle step is mandatory, not optional). Fix-strategy semantics conveyed via `single-fix: [what change resolves all findings if mechanism-type-shared is a single class; enumerate per finding if 'mixed']`. **Note**: No dedicated `fix-strategy:` slot; semantics embedded in `single-fix:` instructions. Less structurally explicit than V-01/V-04/V-05 but pass-level because the semantics are present and the field is unconditional. |
| C-30 | `mechanism-distribution:` computed aggregate | **PASS** | S5.5 Sub-task A: "Walk through every finding block written in Step 5 in order. For each finding, read the `mechanism-type:` field value. Tally the count per type token across all findings. Write the result as the `mechanism-distribution:` line." Summary copies verbatim from S5.5: `mechanism-distribution: [copy the line from Step 5.5 Sub-task A verbatim]`. |

**Essential**: 5/5 | **Recommended**: all pass | **Aspirational**: all pass | **C-29**: PASS (+5) | **C-30**: PASS (+5)

```
composite = 100 (C-01–C-28 all pass) + 5 (C-29) + 5 (C-30) = 110/110
```

**Score: 110/110 — GOLDEN**

---

### V-04 — Combination: Role Sequence × Output Format (C-29 × C-30)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-22 | Earlier criteria | PASS | Both axes preserve prior structure. |
| C-23 | Gate metadata manifest | PASS | Full metadata gate token. |
| C-24 | Multi-branch Patterns | PASS | Three named branches with handling instructions. |
| C-25 | Hypothesis self-test rule | PASS | Self-test present. |
| C-26 | Post-findings closure token | PASS | Closure token with CLAUSE-GAP guard. |
| C-27 | Branch template slots | PASS | Singleton: `mechanism-type-shared: [... -- REQUIRED]`, `fix-strategy: [same-class: one fix resolves all \| mixed: enumerate per-finding fixes]`, `attribution:`, `single-fix:`. Multi: `pattern-N:` with four unconditional slots plus `fix-strategy:`. Zero: `no-pattern-confirmation:`. |
| C-28 | Per-finding mechanism-type token | PASS | All tiers carry taxonomy token. |
| C-29 | `mechanism-type-shared:` required + fix-strategy semantics | **PASS** | Strongest two-axis C-29 evidence: role framing makes it "a required expert judgment, not an optional annotation" + dedicated `fix-strategy:` slot with explicit semantics: "same-class: one fix resolves all findings in this group \| mixed: enumerate per-finding fixes." Both Singleton and Multi-pattern branches mark `mechanism-type-shared:` REQUIRED. |
| C-30 | `mechanism-distribution:` computed aggregate | **PASS** | Summary `mechanism-distribution: [type]:[count] [type]:[count] ...` with enumeration instruction: "Enumerate every `mechanism-type:` field value across all finding blocks in S5. Count occurrences per type token. Write as space-separated type:count pairs, omitting zero-occurrence types." |

**Essential**: 5/5 | **Recommended**: all pass | **Aspirational**: all pass | **C-29**: PASS (+5) | **C-30**: PASS (+5)

```
composite = 100 + 5 + 5 = 110/110
```

**Score: 110/110 — GOLDEN**

---

### V-05 — Full R10 Ceiling: Role Sequence × Output Format × Lifecycle + R9 Platinum Base

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-22 | Earlier criteria | PASS | All preserved in skeleton pre-declaration and behavioral protocol. |
| C-23 | Gate metadata manifest | PASS | Skeleton pre-prints `[EXPECTED-SEALED \| clauses:{N} \| date:{YYYY-MM-DD} \| author:contract-expert \| phase:1-complete]`. |
| C-24 | Multi-branch Patterns | PASS | Three branch templates pre-printed in skeleton with named condition labels. Behavioral protocol rule 10: "S7 may not be silently omitted for any finding count." |
| C-25 | Hypothesis self-test rule | PASS | Behavioral protocol rule 7: "Every `hypothesis-draft:` must pass the necessary-information self-test." Pre-printed in all three finding tier templates. |
| C-26 | Post-findings closure token | PASS | Closure token pre-printed in skeleton, positioned after S5.5. Protocol rule 9: "The `[FINDINGS-RESOLVED ...]` token must appear immediately after the last finding block and after S5.5 is complete." |
| C-27 | Branch template slots | PASS | All three branch templates pre-printed in skeleton with full slot sets. Singleton: `single-finding-ref:`, `root-cause:`, `mechanism-type-shared: [copy from S5.5... -- REQUIRED; same-class signals systemic root cause one fix; mixed signals coincident symptoms independent fixes]`, `fix-strategy:`, `attribution:`, `single-fix:`. Multi: same per pattern block with `patterns-summary:`. Zero: `no-pattern-confirmation:`. |
| C-28 | Per-finding mechanism-type token | PASS | Protocol rule 8: "Every finding must carry a `mechanism-type:` token selected from the five-item enumeration before the `mechanism:` prose. Free-text without a preceding type token is a structural violation." Taxonomy table pre-declared. |
| C-29 | `mechanism-type-shared:` required + fix-strategy semantics | **PASS** | Three-layer enforcement: (1) Behavioral protocol invariant 11: "`mechanism-type-shared:` is unconditionally required in every non-zero Patterns branch (Singleton and Multi-pattern). Writing 'N/A', leaving the slot blank, or omitting it is a structural violation. 'If applicable' does not apply." (2) S5.5 Sub-task B pre-computes all group-type determinations before the gate closes. (3) Patterns branch templates pre-print the slot with "REQUIRED; same-class signals systemic root cause one fix; mixed signals coincident symptoms independent fixes" — fix-strategy semantics embedded directly in the slot instruction. |
| C-30 | `mechanism-distribution:` computed aggregate | **PASS** | Three-layer enforcement: (1) Behavioral protocol invariant 12: "`mechanism-distribution:` in S6 is enumerated from S5 finding blocks by the Taxonomy Synthesis step (S5.5). It is not a template to fill with estimates or placeholders. A distribution line with `?` values, pipe-delimited format, or a verbose label fails." (2) S5.5 Sub-task A mandates the census. (3) Skeleton Summary slot: `mechanism-distribution: [copy verbatim from S5.5 Sub-task A]`. |

**Essential**: 5/5 | **Recommended**: all pass | **Aspirational**: all pass | **C-29**: PASS (+5) | **C-30**: PASS (+5)

```
composite = 100 + 5 + 5 = 110/110
```

**Score: 110/110 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | C-24 | C-27 | C-28 | C-29 | C-30 | Composite | Golden? |
|------|-----------|-----------|------|------|------|------|------|-----------|---------|
| 1 | V-05 Full ceiling | 5/5 | PASS | PASS | PASS | PASS | PASS | **110/110** | YES |
| 1 | V-04 Role × Format | 5/5 | PASS | PASS | PASS | PASS | PASS | **110/110** | YES |
| 1 | V-03 Lifecycle | 5/5 | PASS | PASS | PASS | PASS | PASS | **110/110** | YES |
| 4 | V-01 Role (C-29 only) | 5/5 | PASS | PASS | PASS | PASS | FAIL | **105/110** | YES |
| 5 | V-02 Format (C-30 only) | 5/5 | PARTIAL | FAIL | PASS | FAIL | PASS | **~103/110** | YES |

### C-29 and C-30 isolation results

| Variation | C-29 target | C-30 target | C-29 result | C-30 result |
|-----------|-------------|-------------|-------------|-------------|
| V-01 | YES | NO | PASS | FAIL |
| V-02 | NO | YES | FAIL | PASS |
| V-03 | YES (via S5.5) | YES (via S5.5) | PASS | PASS |
| V-04 | YES (role framing) | YES (format) | PASS | PASS |
| V-05 | YES (all three) | YES (all three) | PASS | PASS |

**Independence confirmed**: V-01 and V-02 each satisfy exactly the criterion targeted. Neither axis change accidentally satisfies the other.

---

## Within-110 Structural Guarantee Ranking

| Strength | Variation | Why |
|----------|-----------|-----|
| Strongest | V-05 | Behavioral protocol invariants 11 and 12 state violations explicitly at protocol layer. Skeleton pre-declares every obligation before Phase 1. S5.5 forces computation before gate closes. Fix-strategy semantics embedded in the slot instruction itself. |
| Strong | V-04 | Explicit `fix-strategy:` slots in both Singleton and Multi-pattern templates. Enumeration instruction in Summary. No lifecycle step — both axes act at different structural positions without a unifying step. |
| Moderate | V-03 | S5.5 is an elegant single step satisfying both criteria by forcing computation at a fixed lifecycle position. `fix-strategy:` semantics conveyed via `single-fix:` instructions (no dedicated slot). Works at execution time but lower write-time structural pressure than V-04/V-05. |

---

## Excellence Signals — Round 10

### E-1: Lifecycle census step satisfies two orthogonal criteria via a single mechanism (V-03)

S5.5 Taxonomy Synthesis inserts a mandatory computation step between S5 findings and the closure gate. Sub-task A produces `mechanism-distribution:` (feeding C-30). Sub-task B produces `group-candidate-N: mechanism-type-shared=[...]` (feeding C-29). A single structural addition — one named step at a fixed lifecycle position — satisfies two criteria that operate on different sections (Summary and Patterns). The computation-then-copy pattern eliminates write-time cognitive pressure for both fields: the author computes in S5.5, then copies verbatim in S6 and S7.

### E-2: C-29/C-30 axis independence is cleanly confirmed by the isolation tests

V-01 (role-sequence axis) passes C-29 and fails C-30. V-02 (output-format axis) passes C-30 and fails C-29. Neither axis change accidentally satisfies the other. This confirms the rubric's framing that the two criteria "operate on orthogonal structural layers" — C-29 on Patterns synthesis semantics, C-30 on Summary aggregate format. The combination axes (V-03/V-04/V-05) all require touching both structural positions.

### E-3: V-02 regression reveals that output-format isolation risks Patterns simplification

V-02's focus on the Summary aggregate led to a simplified Patterns step that lacks the pre-printed structural slots required by C-27 and the three-named-branch structure required by C-24. This is a confirmation of a general risk: when a variation targets one section for format upgrades, adjacent sections may be simplified by the author's attention. V-04 and V-05 avoid this by explicitly maintaining the full Patterns template structure alongside the Summary upgrade.

### E-4: Three-mechanism combination (V-05) eliminates all write-time obligation gaps

V-05 layers three distinct enforcement channels: behavioral protocol invariants (cognitive commitment before Phase 1), skeleton pre-declaration (structural visibility), and lifecycle step (computational enforcement). No new obligation is introduced under write-time pressure. The regression hypothesis holds: the two new invariants add slot-filling obligations without changing role boundaries, phase sequence, or essential coverage requirements.

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- Full 30/30 criteria with strongest structural guarantees
- Behavioral protocol invariants make C-29 and C-30 violations explicit at the protocol layer
- Skeleton pre-declaration means no obligation is introduced under write-time pressure
- Three-mechanism layering (protocol + skeleton + lifecycle step) provides belt-and-suspenders enforcement not present in any isolation variation

**V-04** is the closest competitor without the lifecycle step. If S5.5 is considered operationally heavyweight, V-04 achieves both C-29 and C-30 via two independent structural axes with explicit `fix-strategy:` slots.

**V-03** demonstrates that a single lifecycle census step can satisfy both new criteria elegantly. The `single-fix:` approach to fix-strategy semantics is structurally weaker than a dedicated `fix-strategy:` slot but may produce equivalent output quality in practice.

---

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["Lifecycle census step (S5.5) satisfies two orthogonal criteria via a single structural mechanism: computation forced at a fixed lifecycle position before the gate closes, with outputs copied verbatim into both Summary and Patterns sections, eliminating write-time pressure for both C-29 and C-30", "C-29 and C-30 axis independence confirmed by isolation tests: role-sequence satisfies C-29 only, output-format satisfies C-30 only, neither accidentally satisfies the other — combination axes required to reach both criteria simultaneously"]}
```
