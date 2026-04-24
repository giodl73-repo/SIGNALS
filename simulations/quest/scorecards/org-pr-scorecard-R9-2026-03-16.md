## Scorecard — org-pr Round 9

**Rubric**: v8 | **N_aspirational**: 19

---

### Investigation Rulings

All three investigation targets resolve to **PASS**:

**C-09 (V-03/V-04) — PASS**: Inline gate in the opening topic line satisfies the phase/lifecycle gating criterion. All three gate elements are present (lifecycle condition + halt instruction + alternative path). C-09 is a content criterion, not a section-structure criterion. First round to confirm inline placement.

**C-12/C-24 (V-01/V-04/V-05) — PASS**: 2 named correction-paired forms (Untagged + Revision) satisfy both criteria. Aggregate is a formatting constraint, not a decision-path governance failure. C-12 and C-24 co-resolve as predicted. First round to confirm 2-form minimum.

**C-16 (V-02/V-04/V-05) — PASS**: 3-item focused self-check satisfies the post-generation coverage criterion. The 3 removed items are enforced by structural elements elsewhere in the prompt (template, authority chain declaration, locator gate). First round to confirm 3-item minimum.

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60 | 30 | 10.00 | **100.00** |
| V-02 | 60 | 30 | 10.00 | **100.00** |
| V-03 | 60 | 30 | 10.00 | **100.00** |
| V-04 | 60 | 30 | 10.00 | **100.00** |
| V-05 | 60 | 30 | 10.00 | **100.00** |

All five variations score **100.00** with zero PARTIAL entries — first full-clean round in the series. PASS_equiv = 19.0/19 for every variation.

---

### Excellence Signals (3 new patterns)

**1. C-09 gate structure agnosticism** (V-03, V-04): Phase/lifecycle gating fires on gate content alone. Inline opening sentence placement satisfies C-09 when the three gate elements are present. Labeled section is not load-bearing. → Potential **C-30**.

**2. C-12/C-24 2-form floor** (V-01, V-04, V-05): 2 governance-critical forms satisfy both named-invalid-form criteria. Minimum catalog = 2 forms when each addresses a distinct decision-path failure mode. → Potential **C-31**.

**3. C-16 3-item floor** (V-02, V-04, V-05): 3 focused post-generation items satisfy the self-correction gate criterion when removed items are enforced by structural redundancy elsewhere. Minimum check depth = 3. → Potential **C-32**.

**V-04** is the milestone design: minimum catalog (2 forms) + minimum self-check (3 items) + minimum gate structure (inline sentence) + single axis = **100.00**.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-09 gate structure agnosticism: phase/lifecycle gating fires on gate content (lifecycle condition + halt instruction + alternative path reference), not section structure; an inline opening sentence satisfies C-09 when all three gate elements are present; labeled Phase Gate section is not load-bearing for the criterion", "C-12/C-24 2-form floor: both named-invalid-form and correction-paired-catalog criteria are satisfied by 2 governance-critical forms (Untagged + Revision) with correction instructions; Aggregate is a formatting constraint (not a decision-path failure mode); minimum catalog size is 2 when retained forms each address a distinct governance failure mode (verdict formula corruption + authority chain corruption); C-12 and C-24 co-resolve", "C-16 3-item floor: self-correction gate pre-commit fires on post-generation coverage quality not item count; 3 focused items covering verdict formula, conflict resolution column, and invalid-form scan satisfy C-16 when the removed items (if-stays fill, upstream override prohibition, locator validity) are enforced by named structural elements elsewhere in the prompt; minimum check depth is 3 when structural redundancy is present"]}
```
xception.

---

## Recommended Criteria (30 pts / 6 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Projection-aware consensus | PASS | PASS | PASS | PASS | PASS |
| C-07 Conflict analysis (resolution present) | PASS | PASS | PASS | PASS | PASS |
| C-08 Locator self-correction gate | PASS | PASS | PASS | PASS | PASS |
| C-09 Phase/lifecycle gating | PASS | PASS | **PASS** | **PASS** | PASS |
| C-10 Downstream risk field | PASS | PASS | PASS | PASS | PASS |
| **Recommended total** | **30** | **30** | **30** | **30** | **30** |

Evidence notes:

**C-09 V-01/V-02/V-05**: Dedicated "### Phase Gate" section with explicit PRE-MERGE label,
halt instruction, and /org-review alternative. PASS — consistent with all prior rounds.

**C-09 V-03/V-04**: Inline gate in opening topic line. Gate content confirmed present:
lifecycle condition + halt + alternative path. PASS per investigation ruling above. First
round to confirm the inline placement path.

**C-06 all**: "Projection convergence call: ALIGNED or DIVERGENT" present with direction
declaration in all five variations. PASS.

**C-07 all**: Standalone Conflict Analysis section with 4-column table including Resolution
column present in all five variations. PASS.

**C-08 all**: "Locator self-correction gate: If valid → include. If invalid → rewrite to
the most specific anchor" present in all five. PASS.

**C-10 all**: "Downstream Risk" as a named column in the finding template present in all
five variations. PASS.

---

## Aspirational Criteria (10 pts, N=19)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Formula lock | PASS | PASS | PASS | PASS | PASS |
| C-12 Named invalid forms | **PASS** | PASS | PASS | **PASS** | **PASS** |
| C-13 Inertia / if-stays framing | PASS | PASS | PASS | PASS | PASS |
| C-14 Verdict escape closure | PASS | PASS | PASS | PASS | PASS |
| C-15 Projection convergence call | PASS | PASS | PASS | PASS | PASS |
| C-16 Self-correction gate pre-commit | PASS | **PASS** | PASS | **PASS** | **PASS** |
| C-17 Role authority sequence declaration | PASS | PASS | PASS | PASS | PASS |
| C-18 Axis conflict resolution rule | N/A | N/A | N/A | N/A | N/A |
| C-19 Verdict hardening pair | PASS | PASS | PASS | PASS | PASS |
| C-20 Priority table | N/A | N/A | N/A | N/A | N/A |
| C-21 Authority-inertia reconciliation rule | N/A | N/A | N/A | N/A | PASS |
| C-22 Conflict resolution column | PASS | PASS | PASS | PASS | PASS |
| C-23 Judgment-elimination declaration | PASS | PASS | PASS | PASS | PASS |
| C-24 Correction-paired invalid form catalog | **PASS** | PASS | PASS | **PASS** | **PASS** |
| C-25 Co-occurrence coupling label | PASS | PASS | PASS | PASS | PASS |
| C-26 Governance scope declaration | N/A | N/A | N/A | N/A | PASS |
| C-27 Priority axis non-redundancy | N/A | N/A | N/A | N/A | N/A |
| C-28 Distributed conflict table completeness | N/A | N/A | N/A | N/A | N/A |
| C-29 Governance declaration co-location | N/A | N/A | N/A | N/A | PASS |

**All N/A entries count as PASS_equiv = 1.0.**

---

### Evidence Notes — All Aspirational Criteria

**C-11 all**: "Any P1 finding from any role = No-Go. Not editable. No exceptions." Formula
lock present in all five. PASS.

**C-12 V-02/V-03**: 3 named forms (Untagged, Revision, Aggregate). PASS — unambiguous.

**C-12 V-01/V-04/V-05**: 2 named forms (Untagged, Revision). PASS per investigation
ruling above.

**C-13 all**: "If-Stays Projection" is a named column in the per-role finding template in
all five. PASS.

**C-14 all**: "No other escape path exists. A P1 + Go claim is invalid under this formula."
Explicit exclusion statement present in all five variations. PASS. Note: R9 V-01 is built on
the V-04(R8) architecture which includes the exclusion statement — this is not the R8 V-01
architecture (per-role sub-tables without the exclusion statement). C-14 PASS for all five.

**C-15 all**: Projection convergence call with ALIGNED/DIVERGENT declaration in all five.
PASS.

**C-16 V-01/V-03**: 6-item pre-commit self-check. PASS — unambiguous.

**C-16 V-02/V-04/V-05**: 3-item pre-commit self-check. PASS per investigation ruling above.

**C-17 all**: Numbered authority positions declared in Authority Chain section
(Security 1 → UX 6). PASS.

**C-18 all**: No priority table in any variation. N/A→PASS.

**C-19 all**: "Both must be satisfied simultaneously. A locked formula without escape closure
allows novel escape claims. An escape closure without a locked formula allows formula
modification before the check. The pair closes the decision space." Present in all five.
PASS.

**C-20 all**: No priority table in any variation. N/A→PASS.

**C-21 V-01/V-02/V-03/V-04**: Single-axis designs. No axis declaration. If-Stays Projection
column is a format feature, not a declared governance axis. No reconciliation rule needed.
N/A→PASS.

**C-21 V-05**: Opening block declares "two governance axes: authority chain [...] and inertia
framing [...]" plus reconciliation rule ("the conflict resolves mechanically from the
authority chain — no judgment required"). Inertia is a declared governance axis. PASS.

**C-22 all**: Standalone Conflict Analysis section with 4-column table including Resolution
column in all five variations. PASS.

**C-23 V-01/V-02/V-03/V-04**: "derived mechanically from the authority chain, no judgment
required" in the Conflict Analysis resolution column instruction. PASS.

**C-23 V-05**: Opening reconciliation rule: "the conflict resolves mechanically from the
authority chain — no judgment required." Resolution column instruction does not repeat the
phrase. C-23 is a content criterion (phrase in conflict-resolution governance context) not a
structural criterion. Opening placement confirmed sufficient per R8 V-05. PASS.

**C-24 V-02/V-03**: 3 forms with corrections (Untagged → tag instruction, Revision →
if-stays instruction, Aggregate → split instruction). PASS — unambiguous.

**C-24 V-01/V-04/V-05**: 2 forms with corrections (Untagged → tag instruction, Revision →
if-stays instruction). PASS per investigation ruling above.

**C-25 all**: "Both must be satisfied simultaneously" present in all five. PASS.

**C-26 V-01/V-02/V-03/V-04**: Single-axis designs. No axis count declaration present.
"N/A if only one axis is present — no declaration needed for single-axis prompts." N/A→PASS.

**C-26 V-05**: "This prompt operates under two governance axes" — explicit integer count
declared. PASS.

**C-27 all**: No priority table in any variation. N/A→PASS.

**C-28 all**: All five use a centralized standalone Conflict Analysis section. No per-role
conflict sub-tables. C-28 condition ("FAIL if any per-role table is missing one or more
fields") does not apply. N/A→PASS.

**C-29 V-01/V-02/V-03/V-04**: C-26 is N/A (single-axis). Only one governance declaration
present (judgment-elimination in the resolution column instruction). "N/A if only one of the
two declarations is present." N/A→PASS.

**C-29 V-05**: Opening preamble contains both "two governance axes" (axis count
declaration, satisfies C-26) and "no judgment required" (judgment-elimination declaration,
satisfies C-23). Both co-located in the same opening block before any operational content.
PASS — consistent with R8 V-05 confirmed pattern.

---

## PASS_equiv Calculation

| Variation | Full-weight (PASS/N/A) | PARTIAL | PASS_equiv | Aspirational pts |
|-----------|------------------------|---------|------------|-----------------|
| V-01 | 19 | 0 | **19.0** | **10.00** |
| V-02 | 19 | 0 | **19.0** | **10.00** |
| V-03 | 19 | 0 | **19.0** | **10.00** |
| V-04 | 19 | 0 | **19.0** | **10.00** |
| V-05 | 19 | 0 | **19.0** | **10.00** |

All five variations achieve PASS_equiv = 19.0/19 = 1.0. Zero PARTIAL entries in any
variation — a first for this skill.

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 | 60 | 30 | 10.00 | **100.00** |
| V-02 | 60 | 30 | 10.00 | **100.00** |
| V-03 | 60 | 30 | 10.00 | **100.00** |
| V-04 | 60 | 30 | 10.00 | **100.00** |
| V-05 | 60 | 30 | 10.00 | **100.00** |

All five variations score 100.00 with no PARTIAL entries. The three investigation targets
(C-09 implicit gate, C-12/C-24 2-form catalog, C-16 3-item check) all resolve to PASS. The
minimum-content hypotheses are confirmed.

---

## Ranking

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|--------------------|
| 1 (tied) | V-01 | 100.00 | 2-form catalog; minimum catalog floor confirmed |
| 1 (tied) | V-02 | 100.00 | 3-item self-check; minimum check depth confirmed |
| 1 (tied) | V-03 | 100.00 | Implicit phase gate; gate structure agnosticism confirmed |
| 1 (tied) | V-04 | 100.00 | All three reductions combined; minimum-content single-axis design |
| 1 (tied) | V-05 | 100.00 | 2-axis + co-location + minimized catalog and check; no 2-axis content premium |

V-04 is the notable result: the single minimum-content design (fewest named forms, fewest
self-check items, most implicit gate framing) that reaches 100.00. V-05 confirms that
2-axis designs absorb the same simplifications without penalty.

---

## Excellence Signals

**1. C-09 gate structure agnosticism: inline opening placement satisfies phase/lifecycle
gating.** V-03 and V-04 embed the full gate condition in the opening topic line rather than
in a dedicated labeled section. The criterion fires on gate content — lifecycle condition,
halt instruction, alternative path reference — not on section structure. A single inline
sentence ("This skill runs before merge only — if the PR has already merged, halt and use
/org-review instead") carries all three gate elements and satisfies C-09. Phase gates may
be structurally consolidated into the opening line without a section heading. First round
to confirm this placement path. Potential C-30: gate content may be structurally
consolidated (no labeled section required) when all three elements are present and
positioned at the prompt's execution entry point.

**2. C-12/C-24 2-form floor: governance-critical catalog satisfies both named-form
criteria.** V-01, V-04, and V-05 drop Aggregate from the invalid-form catalog, retaining
only Untagged and Revision. Both criteria pass with 2 forms because the pass condition is
presence of named correction-paired forms, not exhaustive enumeration. Aggregate is a
formatting constraint (prevents multi-surface row conflation) — its absence does not open a
verdict formula or authority chain failure mode. Untagged and Revision are the
governance-critical forms: one corrupts the verdict formula, the other corrupts the
authority chain. 2 forms with correction instructions satisfy C-12 and C-24
simultaneously. C-12 and C-24 co-resolve as predicted: same catalog evidence, same
outcome. First round to confirm 2-form minimum. Potential C-31: the minimum named-form
catalog is 2 governance-critical forms when each retained form addresses a distinct
decision-path failure mode.

**3. C-16 3-item floor: focused post-generation coverage satisfies the self-correction gate
criterion.** V-02, V-04, and V-05 reduce the pre-commit self-check to 3 items: verdict
formula verification, conflict resolution column completeness, invalid-form scan. The 3
removed items (if-stays projection fill, upstream override prohibition, locator validity)
are enforced by other structural elements — the per-role template, the authority chain
declaration, and the locator self-correction gate respectively. C-16 fires on the quality
of post-generation coverage, not on item count. 3 targeted items addressing the three
failure modes most likely to survive generation (wrong formula, blank resolution cell,
contaminated finding row) satisfy C-16 when redundant items are covered by structural
redundancy elsewhere. First round to confirm 3-item minimum. Potential C-32: the minimum
self-check depth is 3 items when removed items are demonstrably enforced by named
structural elements in the same prompt.

**4. Five concurrent 100.00 paths with zero PARTIAL entries — first full-clean round.**
All five variations score 100.00 with no PARTIAL entries. The rubric now has a fully
explored content floor for single-axis and 2-axis designs: minimum catalog (2 forms),
minimum self-check (3 items), minimum gate structure (inline sentence), minimum axis count
(1). V-04 represents the minimum-content 100.00 design: 2 named forms, 3 self-check items,
implicit gate, single axis. V-05 confirms that 2-axis designs incur no content premium when
co-location is applied.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-09 gate structure agnosticism: phase/lifecycle gating fires on gate content (lifecycle condition + halt instruction + alternative path reference), not section structure; an inline opening sentence satisfies C-09 when all three gate elements are present; labeled Phase Gate section is not load-bearing for the criterion", "C-12/C-24 2-form floor: both named-invalid-form and correction-paired-catalog criteria are satisfied by 2 governance-critical forms (Untagged + Revision) with correction instructions; Aggregate is a formatting constraint (not a decision-path failure mode); minimum catalog size is 2 when retained forms each address a distinct governance failure mode (verdict formula corruption + authority chain corruption); C-12 and C-24 co-resolve", "C-16 3-item floor: self-correction gate pre-commit fires on post-generation coverage quality not item count; 3 focused items covering verdict formula, conflict resolution column, and invalid-form scan satisfy C-16 when the removed items (if-stays fill, upstream override prohibition, locator validity) are enforced by named structural elements elsewhere in the prompt; minimum check depth is 3 when structural redundancy is present"]}
```
