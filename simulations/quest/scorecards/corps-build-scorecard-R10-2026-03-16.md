Now I have everything needed to score all five variations. Let me produce the scorecard.

---

# Quest Scorecard: corps-build — Round 10 (Rubric v9)

## Scoring Context

All five R10 variations use **V-05 R9 as their baseline**, which achieved 100/100 on all 29 v9 criteria. Each variation adds one or more new structural axes (C-30/C-31/C-32 candidates) without removing any existing structural guarantees. Scoring question: does any variation lose a v9 criterion in the process of adding a new axis?

---

## Criterion-by-Criterion Analysis

### Essential (C-01 through C-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Role file completeness | PASS | PASS | PASS | PASS | PASS |
| C-02 org-chart.md with ASCII diagram | PASS | PASS | PASS | PASS | PASS |
| C-03 Inertia Advocate in every team | PASS | PASS | PASS | PASS | PASS |
| C-04 org.yaml structural fidelity | PASS | PASS | PASS | PASS | PASS |
| C-05 Role file typed fields present | PASS | PASS | PASS | PASS | PASS |

**Evidence**: All variations retain PARSE (Phase 1), WRITE-IA (Phase 6) with IA-COMPLETE gate, WRITE-ROLES (Phase 8) with per-role five-field output, and directory structure derived from org.yaml. No variation introduces structural changes that could affect file output completeness.

---

### Recommended (C-06 through C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Headcount table + levels | PASS | PASS | PASS | PASS | PASS |
| C-07 Standard vs specialized distinction | PASS | PASS | PASS | PASS | PASS |
| C-08 AMEND section with three options | PASS | PASS | PASS | PASS | PASS |

**Evidence (C-06)**: ARTIFACT-A and ARTIFACT-C produced in CONTRACT (Phase 4) before any file writes; transcribed verbatim into org-chart.md sections 2 and 4. All five variations preserve this. **Evidence (C-07)**: Scope field in each role file explicitly set to `standard -- present in all teams` or `specialized -- [team name]` or `exec office`; unchanged across all variations. **Evidence (C-08)**: All variations emit AMEND section with `[REGENERATE-AREA]`, `[ADJUST-LEVEL]`, `[CHANGE-STRUCTURE]` options referencing specific org.yaml values. V-01/V-04/V-05 add AMEND-PATH-A/B on top of this; V-02/V-03 preserve the base AMEND-RECEIPT without the path naming but still satisfy C-08.

---

### Aspirational (C-09 through C-29)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 IA team-contextualized | PASS | PASS | PASS | PASS | PASS |
| C-10 Cross-reference integrity | PASS | PASS | PASS | PASS | PASS |
| C-11 Pre-write validation gate | PASS | PASS | PASS | PASS | PASS |
| C-12 IA-first write ordering | PASS | PASS | PASS | PASS | PASS |
| C-13 Headcount table as build contract | PASS | PASS | PASS | PASS | PASS |
| C-14 Analytic narrative prose | PASS | PASS | PASS | PASS | PASS |
| C-15 IA file as person-portrait | PASS | PASS | PASS | PASS | PASS |
| C-16 Resistance profile pre-IA | PASS | PASS | PASS | PASS | PASS |
| C-17 CROSS-REF IA lens at build-complete | PASS | PASS | PASS | PASS | PASS |
| C-18 Contract verbatim transcription | PASS | PASS | PASS | PASS | PASS |
| C-19 TRANSCRIPTION-RECEIPT auto-correct | PASS | PASS | PASS | PASS | PASS |
| C-20 BUILD-VERIFY single-purpose phase | PASS | PASS | PASS | PASS | PASS |
| C-21 TRANSCRIPTION-CLEAR re-audit gate | PASS | PASS | PASS | PASS | PASS |
| C-22 Named binary path structure | PASS | PASS | PASS | PASS | PASS |
| C-23 Declarative block-shape rules | PASS | PASS | PASS | PASS | PASS |
| C-24 Phase lifecycle boundary markers | PASS | PASS | PASS | PASS | PASS |
| C-25 Resistance landscape as contract artifact | PASS | PASS | PASS | PASS | PASS |
| C-26 Named write passes with per-pass receipts | PASS | PASS | PASS | PASS | PASS |
| C-27 AMEND-RECEIPT type-tagged options | PASS | PASS | PASS | PASS | PASS |
| C-28 BUILD-VERIFY two-field IA verification | PASS | PASS | PASS | PASS | PASS |
| C-29 SECTIONS-COMPLETE declarative rule | PASS | PASS | PASS | PASS | PASS |

**Selected evidence notes:**

- **C-22** (Named binary path): V-01/V-04/V-05 add AMEND-PATH-A/AMEND-PATH-B on top of existing PATH-A/PATH-B; V-02/V-04/V-05 add BV-PATH-A/BV-PATH-B. V-03 retains only PATH-A/PATH-B in WRITE-CHART — sufficient to pass C-22's "at least one conditional phase with two labeled paths" condition. All PASS.

- **C-23** (Declarative correctness rules): All variations inherit VALIDATE, BUILD-VERIFY, TRANSCRIPTION-RECEIPT, SECTIONS-COMPLETE, AMEND-RECEIPT, and PROFILE block correctness rules from V-05 R9. V-01 additionally declares AMEND-CLEAR correctness rule ("fewer than three type tags is structurally incomplete"). V-02 declares BUILD-VERIFY-CLEAR correctness rule ("fewer than N teams is structurally incomplete"). V-03 declares PROFILE-ENTRY-VALID correctness rule ("fewer than four checks is structurally incomplete"). All exceed the two-block minimum.

- **C-24** (Phase lifecycle boundaries): Every variation uses `PHASE-ENTERED: [phase] -- precondition: [gate]` and `PHASE-EXITED: [phase] -- gate: [gate]` for all 10 phases. This is explicitly stated in each variation header. All PASS.

- **C-28** (BUILD-VERIFY two-field): All variations emit `lens verdict: VERBATIM / DRIFT` and `expertise verdict: VERBATIM / DRIFT` as distinct labeled fields per team, plus a team-level verdict of `VERBATIM-BOTH / DRIFT-LENS / DRIFT-EXPERTISE / DRIFT-BOTH`. V-02 adds BV-PATH-A/BV-PATH-B on top of this but does not alter the two-field verification structure. All PASS.

- **C-29** (SECTIONS-COMPLETE declarative rule): All variations state "A correct SECTIONS-COMPLETE block names all four pass receipt tokens; a SECTIONS-COMPLETE block naming fewer than four is structurally incomplete." This declarative correctness rule is present in all five. PASS.

---

## Composite Scores

| Variation | Essential (5/5×60) | Recommended (3/3×30) | Aspirational (21/21×10) | Composite |
|-----------|-------------------|---------------------|------------------------|-----------|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

All five variations achieve **100/100**. Golden threshold: met (all essential PASS, composite >= 80).

---

## Ranking

All five tie at 100/100 on the v9 rubric. Ordering by structural density added for R11 extraction:

| Rank | Variation | Score | New axes added |
|------|-----------|-------|----------------|
| 1 | **V-05** | 100 | AMEND-CLEAR + BUILD-VERIFY-CLEAR + PROFILE-ENTRY-VALID (3 axes) |
| 2 | **V-04** | 100 | AMEND-CLEAR + BUILD-VERIFY-CLEAR (2 axes) |
| 3 | **V-01** | 100 | AMEND-CLEAR (1 axis) |
| 3 | **V-02** | 100 | BUILD-VERIFY-CLEAR (1 axis) |
| 3 | **V-03** | 100 | PROFILE-ENTRY-VALID (1 axis) |

V-05 is the extractable baseline for R11.

---

## Excellence Signals from V-05

Three patterns in V-05 are the primary candidates for C-30/C-31/C-32 in R11:

**Signal 1 — AMEND-CLEAR as PASS-AMEND exit gate (C-30 candidate)**
V-05 introduces AMEND-PATH-A/AMEND-PATH-B as named sibling paths after AMEND-RECEIPT. AMEND-PATH-B triggers AMEND-CLEAR, which re-audits all three type-tagged option slots (not only the rewritten one) before AMEND-WRITTEN. The correctness rule is explicit: "An AMEND-CLEAR naming fewer than three type tags is structurally incomplete and does not serve as an AMEND-PATH-B exit gate. An AMEND-PATH-B exit that emits AMEND-WRITTEN before AMEND-CLEAR is structurally invalid." This extends the TRANSCRIPTION-CLEAR exit-gate guarantee to PASS-AMEND — the phase cannot exit with any unverified type-tagged slot.

**Signal 2 — BUILD-VERIFY-CLEAR as BUILD-VERIFY exit gate (C-31 candidate)**
V-05 introduces BV-PATH-A/BV-PATH-B. BV-PATH-B triggers BUILD-VERIFY-CLEAR, which lists all N teams with VERBATIM-BOTH in a single pass before BUILD-VERIFY-COMPLETE. "A BUILD-VERIFY-CLEAR naming fewer than N teams is structurally incomplete and does not serve as a BV-PATH-B exit gate. A BV-PATH-B exit that emits BUILD-VERIFY-COMPLETE before BUILD-VERIFY-CLEAR is structurally invalid." This extends the TRANSCRIPTION-CLEAR pattern to BUILD-VERIFY: per-team-sequential correction becomes post-correction-global confirmation.

**Signal 3 — PROFILE-ENTRY-VALID per-entry specificity receipt (C-32 candidate)**
V-05 introduces PROFILE-ENTRY-VALID fired immediately after each PROFILE entry. The receipt carries exactly four named specificity checks: `defended-artifact (SPECIFIC/CATEGORICAL)`, `change-pressure (SPECIFIC/CATEGORICAL)`, `lens-phrase (GROUNDED/UNGROUNDED)`, `expertise-seed (SPECIFIC/CATEGORICAL)`, plus a VALID/INVALID verdict. CATEGORICAL or UNGROUNDED triggers a rewrite before the next team. PROFILE-GATE is gated on all entries VALID. "A correct PROFILE-ENTRY-VALID carries exactly four checks; fewer than four is structurally incomplete." This closes the specificity gap that existed in all R9 variations: specificity was declared as a rule but was only verified implicitly at BUILD-VERIFY time — now it is verified as a named token at extraction time.

---

## Observations

**R10 achieves complete TRANSCRIPTION-CLEAR analog coverage**: The TRANSCRIPTION-CLEAR pattern (introduced in R5 as C-21, applying a named re-audit gate after any rewrite) now covers four phases:
- WRITE-CHART: TRANSCRIPTION-CLEAR (C-21, existing)
- PASS-AMEND: AMEND-CLEAR (C-30 candidate)
- BUILD-VERIFY: BUILD-VERIFY-CLEAR (C-31 candidate)
- PROFILE: PROFILE-ENTRY-VALID (C-32 candidate — analogous but applied at entry time rather than exit time)

All three R10 new patterns are orthogonal and coexist cleanly in V-05: PROFILE-ENTRY-VALID operates in Phase 3, AMEND-CLEAR in Phase 7, BUILD-VERIFY-CLEAR in Phase 9. V-04 confirms AMEND-CLEAR and BUILD-VERIFY-CLEAR coexist without interference; V-05 confirms all three coexist.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["AMEND-CLEAR named exit-gate re-audit block with AMEND-PATH-A/AMEND-PATH-B binary path structure closing all three type-tagged option slots before AMEND-WRITTEN", "BUILD-VERIFY-CLEAR named exit-gate re-audit block with BV-PATH-A/BV-PATH-B binary path structure confirming all N teams VERBATIM-BOTH before BUILD-VERIFY-COMPLETE", "PROFILE-ENTRY-VALID per-entry specificity receipt with four named checks (defended-artifact, change-pressure, lens-phrase, expertise-seed) closing specificity at extraction time as a named structural token before PROFILE-GATE"]}
```
