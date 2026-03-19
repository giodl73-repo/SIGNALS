## R9 Scorecard: discover-causal

**Rubric:** v9 (22 criteria, 200 pts max) | **Base:** R8 V-05 (200/200)

### Results

| Variation | C-30 | Score | Tier |
|-----------|------|-------|------|
| V-01 (ARTIFACT field stripped) | FAIL | **195** | Golden |
| V-02 (integration rule stripped) | FAIL | **195** | Golden |
| V-03 (positive-only rule) | FAIL | **195** | Golden |
| V-04 (rule at Phase 3 only) | FAIL | **195** | Golden |
| V-05 (full ceiling + Phase 3 co-location) | PASS | **200** | Golden (ceiling) |

All 4 C-30 hypotheses confirmed:

1. **V-01:** ARTIFACT field is independently required -- Phase 6 integration rule alone does not satisfy C-30
2. **V-02:** Phase 6 integration rule is independently required -- ARTIFACT field alone does not satisfy C-30
3. **V-03:** Positive-only rule does not satisfy C-30 -- "does not pass" failure mode naming is load-bearing (parallel to C-22/C-20 pattern)
4. **V-04:** Rule must be at Phase 6 (synthesis point) -- Phase 3 placement does not satisfy C-30 (parallel to C-29 requiring the C-26 integrity rule at synthesis)

**v10 signal from V-05 (C-31 candidate):** ANCHOR-UPDATE PROHIBITED FORM co-located at Phase 3 CONDITIONAL BRANCH -- explicitly naming that recording the update at Phase 3 does not close the Phase 6 propagation requirement. Dual-site enforcement: Phase 3 production point + Phase 6 synthesis point. Mirrors the C-26/C-27 co-location pattern.

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["C-30 requires both Phase 6 integration rule AND anchor_updated_from_phase1 ARTIFACT field: each is independently required, neither substitutes for the other", "C-30 integration rule must name the failure mode with 'does not pass' language: positive-only rule ('must carry Phase 3 step') does not satisfy C-30 -- parallel to C-22/C-20 pattern", "C-30 requires the integration rule at Phase 6 (synthesis point): Phase 3 placement does not satisfy C-30 -- parallel to C-29 requiring the C-26 integrity check at synthesis", "V10 candidate C-31: stale-anchor prohibited form co-located at Phase 3 CONDITIONAL BRANCH -- naming at the update point that recording the update there does not close the Phase 6 propagation requirement; dual-site enforcement (Phase 3 production + Phase 6 synthesis)"]}
```
nt names what must happen; naming the failure mode requires naming what fails -- i.e., that "carrying the Phase 1 anchor unchanged when Phase 3 updated does not pass." Parallel to C-22 (which requires naming "conditioning on Competing or Unclear does not pass" rather than only stating the positive unconditional rule), C-30 requires the prohibited form named, not only the positive requirement stated.

**V-04 confirmed (195):** The stale-anchor rule at Phase 3 CONDITIONAL BRANCH does NOT satisfy C-30. C-30 is an integration criterion: its enforcement site is Phase 6 (where the stale anchor would appear), not Phase 3 (where the update is produced). Parallel to C-29 (which requires the C-26 integrity rule at synthesis/Phase 6, not only at Phase 3 where the anchor is produced), C-30 requires the stale-anchor check at the synthesis point. A rule at Phase 3 tells the model what to do when updating; it does not enforce what Phase 6 must carry. The positional requirement is Phase 6.

### V10 Candidate Signal (from V-05)

**C-31 (proposed): Stale-anchor prohibited form co-located at Phase 3 CONDITIONAL BRANCH.** When Phase 3 updates the preliminary anchor to a higher-confidence step, the moment of update must also carry a PROHIBITED FORM explicitly naming that correctly recording the update at Phase 3 does not close the Phase 6 propagation requirement. V-05 adds this co-location with ANCHOR-UPDATE PROHIBITED FORM: "recording the updated BEST-TRACEABLE ANCHOR here does not complete the propagation requirement. Phase 6 Falsification must also carry the updated step -- correctly recording the update here does not close the Phase 6 propagation requirement." Mirrors the C-26/C-27 co-location pattern: C-26 requires the anchor at Phase 1; C-27 requires the prohibition co-located at Phase 1. C-30 requires the integration rule at Phase 6 (synthesis point); C-31 would require the prohibited form co-located at Phase 3 (update point). V-01 through V-04 do not address this co-location.

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["C-30 requires both Phase 6 integration rule AND anchor_updated_from_phase1 ARTIFACT field: each is independently required, neither substitutes for the other", "C-30 integration rule must name the failure mode with 'does not pass' language: positive-only rule ('must carry Phase 3 step') does not satisfy C-30 -- parallel to C-22/C-20 pattern", "C-30 requires the integration rule at Phase 6 (synthesis point): Phase 3 placement does not satisfy C-30 -- parallel to C-29 requiring the C-26 integrity check at synthesis", "V10 candidate C-31: stale-anchor prohibited form co-located at Phase 3 CONDITIONAL BRANCH -- naming at the update point that recording the update there does not close the Phase 6 propagation requirement; dual-site enforcement (Phase 3 production + Phase 6 synthesis)"]}
```

---

### Criteria Detail

C-01 through C-29 are identical across all five variations (all inherited from R8 V-05 base with no changes). C-30 is the sole differentiating criterion in R9.

| ID | Criterion | All Variations | Evidence Note |
|----|-----------|---------------|---------------|
| C-01 | Mechanism traced as pathway | **PASS** | Phase 2 traces observable intermediate steps; each step names agent and indicator |
| C-02 | Falsification is mechanism break | **PASS** | Phase 3 requires "mechanism fails if Step N -- Name -- does not occur"; metric threshold excluded |
| C-03 | Inertia check performed | **PASS** | Phase 0 INERTIA GATE required before mechanism work; all three verdict values must shape Phase 6 |
| C-04 | Causal claim narrowed in AMEND | **PASS** | Phase 6 AMEND requires narrowed claim; restating or broadening explicitly does not pass |
| C-05 | Context evidence assessed | **PASS** | Phase 4 assesses per-step evidence; external research distinguished from team-specific |
| C-06 | Mechanism pathway is testable | **PASS** | Phase 2 requires observable indicators per step; vague pathways do not produce gradeable labels |
| C-07 | At least one confounder identified | **PASS** | Phase 5 requires at least one alternative explanation excluding the inertia case |
| C-08 | AMEND output is actionable | **PASS** | Phase 6 Amended requires mechanism qualifier, scope condition, inertia incorporation, confounder note |
| C-09 | Evidence quality rated | **PASS** | Phase 4 defines T1/T2/T3/none tiers; Aggregate evidence tier is required output regardless of gaps |
| C-10 | Multiple causal pathways considered | **PASS** | Phase 2 requires secondary pathway check; complementary/competing/nested/singular noted |
| C-11 | Incompleteness acknowledged | **PASS** | Phase 1 readiness gate requires honest self-assessment; fabricating thin steps named as failure |
| C-12 | Break anchored to named step | **PASS** | Phase 3 requires "Step [N] -- [Name]" format; UNCERTAIN steps still anchor with noted uncertainty |
| C-13 | Evidence gap localized to steps | **PASS** | Phase 4 per-step accounting; gap field required even when value is "none" |
| C-14 | AMEND conditioned on inertia | **PASS** | Phase 6 inertia incorporation required; all three verdict forms prescribed |
| C-15 | AMEND synthesizes all phases | **PASS** | Phase 6 requires named fields from every prior phase; omitting any does not pass |
| C-16 | Pathway steps formally labeled | **PASS** | Phase 2 STEP LABELING REQUIREMENT is structural prerequisite; positional references do not pass |
| C-17 | Confounder distinguished from inertia | **PASS** | Phase 5 explicitly excludes inertia case; required acknowledgment of exclusion |
| C-18 | Incomplete pathway still anchors | **PASS** | Phase 3 CONDITIONAL BRANCH requires BEST-TRACEABLE ANCHOR format; metric deferral named as failure |
| C-19 | Evidence gap and tier are separate fields | **PASS** | Phase 4 FIELD INDEPENDENCE NOTE; two named entries explicitly required |
| C-20 | AMEND inertia is unconditional | **PASS** | Phase 6 names all three verdict forms; no verdict makes incorporation optional |
| C-21 | Null-gap counterexample proven | **PASS** | Phase 4 NULL-GAP COUNTEREXAMPLE instantiates "gap: none, tier: T1" state explicitly |
| C-22 | Inertia conditional form excluded | **PASS** | Phase 0 PROHIBITED FORM names "conditioning on Competing or Unclear does not pass" |
| C-23 | Mechanism completeness is named AMEND field | **PASS** | Phase 6 Mechanism completeness is standalone named field; embedding in clause text does not pass |
| C-24 | Falsification deferral form excluded | **PASS** | Phase 3 PROHIBITED FORM (C-24) names "deferring or omitting step-level falsification does not pass" |
| C-25 | Evidence gap is standalone AMEND field | **PASS** | Phase 6 Evidence gap is distinct named field; PROPAGATION REQUIREMENT names this explicitly |
| C-26 | Anchor co-located with declaration | **PASS** | Phase 1 SUB-STEP 2 requires preliminary anchor before Phase 2; Phase 3 confirms/extends |
| C-27 | C-26 prohibition co-located at Phase 1 | **PASS** | Phase 1 SUB-STEP 2 PROHIBITED FORM names "does not pass" at declaration point |
| C-28 | Phase 3 frames anchor as confirmation | **PASS** | Phase 3 CONDITIONAL BRANCH uses "already on record from Phase 1 SUB-STEP 2" |
| C-29 | C-26 integrity rule at synthesis | **PASS** | Phase 6 integration rules include: "A response where Phase 1 contains no PRELIMINARY ANCHOR and Phase 6 Falsification carries the first anchor does not pass C-26" |

---

### C-30 Detail by Variation

| Variation | Integration rule present | Rule has "does not pass" | Rule at Phase 6 | ARTIFACT field present | C-30 verdict |
|-----------|------------------------|--------------------------|-----------------|----------------------|--------------|
| V-01 | YES | YES | YES | NO | FAIL |
| V-02 | NO | -- | -- | YES | FAIL |
| V-03 | YES | NO (positive-only) | YES | YES | FAIL |
| V-04 | YES (Phase 3 only) | YES | NO | YES | FAIL |
| V-05 | YES + Phase 3 co-location | YES | YES | YES | PASS |

**C-30 gradeability in all variations:** C-26 PASS (Phase 1 preliminary anchor present) + C-28 PASS (Phase 3 uses "already on record from Phase 1 SUB-STEP 2"). C-30 is gradeable in all five variations. Since Phase 3 CONDITIONAL BRANCH in the base updates the anchor from Phase 1 when higher-confidence steps are traced, C-30 is not N/A -- the update path is active.
