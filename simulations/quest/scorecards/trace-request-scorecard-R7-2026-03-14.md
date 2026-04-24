---

## trace-request -- Round 7 Scorecard

**Rubric:** v6 (160 pts) | **Date:** 2026-03-14

---

### Per-Variation Scores

| Rank | Variation | Score | Gap | All Essential |
|------|-----------|-------|-----|---------------|
| 1 | V-02 (vocabulary commitment) | **160/160** | -- | PASS |
| 1 | V-03 (anti-pattern framing) | **160/160** | -- | PASS |
| 1 | V-04 (vocabulary + batch-catalog gate) | **160/160** | -- | PASS |
| 1 | V-05 (combined: all axes + Rem# citation) | **160/160** | -- | PASS |
| 5 | V-01 (advisory phrasing) | **150/160** | −5 C-20, −5 C-21 | PASS |

---

### Key findings

**V-01** confirms rubric stability: removing DISQUALIFIER enforcement from the exhaustiveness gate produces the same −10 pt gap (C-20, C-21) as R6 V-01 and R6 V-02. The criterion pressure is load-bearing and correctly placed.

**V-02, V-03, V-04, V-05** all score 160/160 because R7's axes (vocabulary binding, anti-pattern framing, batch-catalog gate, Rem# citation) operate *above* the current C-01--C-21 surface — they improve response quality and surface new artifact candidates without intersecting any existing testable boundary.

**R7 is the first round where the top-tier tie is total**: four variations at 160/160, each revealing a different qualitative or structural dimension not yet captured by the rubric.

---

### Excellence Signals — V-05

**ES-1: Batch-catalog cross-check gate (C-22 candidate)** — V-04/V-05 add a three-integer summary at Step 10 before Step 11 may begin: `N edge cases × M catalog rows → K interactions found`. Parallel structure to the exhaustiveness gate (C-20) one level up the stack. Pass condition: gate summary present with all three integers, gate placement before Step 11, per-case entries naming actual catalog row numbers. Dependency: C-07 + C-13.

**ES-2: Cross-step Rem# citation (C-23 candidate)** — V-05 requires Steps 7 and 9 to each cite applicable Rem# entries from the Register at the failure boundary. C-08/C-14/C-17 verify Register existence and completeness; C-23 verifies the adversarial and error path analyses close the loop *back* to those entries at the exact point of failure. A complete Register with no back-reference from Steps 7/9 would pass all current criteria and fail C-23. Dependency: C-08 + C-09 + C-06.

**ES-3: Vocabulary coherence (qualitative only)** — Step 0 binding propagates platform-specific terminology through C-03/C-04/C-14 fields. Not promoted: requires cross-step token comparison, not binary field presence. Not yet a computable criterion.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["C-22: batch-catalog cross-check gate computable summary (N cases, M catalog rows, K interactions) required before Step 11", "C-23: adversarial trace (Step 7) and error path (Step 9) must each cite applicable Rem# entries from Register at divergence/origination boundary"]}
```
visory phrasing does not prevent mechanism naming |
| C-09 | Adversarial path comparison | **PASS** | Step 7 mandatory cross-reference block preserved; four-field structure retained |
| C-10 | Critical path named | **PASS** | Step 5 preserved; "try to resolve" discrepancy language is advisory but structural ask remains |
| C-11 | Authorization re-walk audit | **PASS** | Step 8 asks for new gap or per-boundary certification; advisory phrasing, model likely raises at least one new finding |
| C-12 | Per-boundary latency budget table | **PASS** | Step 4 p50/p99 columns present; Step 5 reconciliation phrased as suggestion ("try to resolve") but still present |
| C-13 | Threat class catalog | **PASS** | Step 6 table described with Adv? column; "aim for at least 5 rows" advisory but model likely complies |
| C-14 | Remediation parameters quantified | **PASS** | Step 11 Parameters column guidance preserved with quantified type descriptions |
| C-15 | Multi-boundary threat exhaustiveness | **PASS** | Step 6 guidance says "list every boundary where this threat class can manifest"; advisory phrasing sufficient |
| C-16 | Adversarial scenario catalog-grounded | **PASS** | Step 7 mandatory cross-reference block retained with four required fields |
| C-17 | Remediation register as dedicated structure | **PASS** | Step 11 described as "dedicated section separate from Step 4" |
| C-18 | Exhaustiveness confirmation precedes adversarial | **PASS** | Advisory exhaustiveness section appears before Step 7; suggests per-row review format ("noting any additions found") and asks for short confirmation before proceeding; timing is structurally before Step 7 in the prompt layout; "names rows checked" condition met at suggestion level |
| C-19 | Adversarial candidate pre-marked in catalog | **PASS** | Step 6 Adv? column described; "Mark exactly one row Y" instruction retained in advisory form |
| C-20 | Exhaustiveness gate includes computable summary | **FAIL** | Gate summary asks for "a short confirmation that the check is done and note which catalog row is your adversarial candidate" -- no integer count for rows reviewed, no integer count for Seq# additions; hedged advisory language cannot produce a computable artifact |
| C-21 | Candidate marking committed at exhaustiveness gate | **FAIL** | Advisory paragraph describes no per-row Adv? field in the exhaustiveness checklist; model has no signal to add the field; C-18 PASS but prompt does not describe the dual-lock structure |

### Score computation

| Tier | Criteria | Pts Each | Available | Earned |
|------|----------|----------|-----------|--------|
| Essential | C-01--C-04 (4xPASS) | 15 | 60 | **60** |
| Recommended | C-05--C-07 (3xPASS) | 10 | 30 | **30** |
| Aspirational | C-08--C-19 (12xPASS) | 5 | 60 | **60** |
| Aspirational | C-20 FAIL | 5 | 5 | **0** |
| Aspirational | C-21 FAIL | 5 | 5 | **0** |
| **Total** | | | **160** | **150** |

**150/160** | All essential PASS | Golden: YES (>=80, all essential PASS)
**Gap:** -10 pts (C-20 -5, C-21 -5)

---

## V-02 -- Role sequence: vocabulary commitment

### Axis
Step 0 added with explicit per-role vocabulary commitment block. All R6 V-05 structural
requirements preserved: blocking gate, integer count summary, per-row Adv? field,
DISQUALIFIER enforcement throughout.

### Criterion-by-criterion

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Entry point declared | **PASS** | Step 1 DISQUALIFIER present; Step 0 vocabulary commitment means credential type will use platform-specific form |
| C-02 | All service boundaries crossed | **PASS** | GATE structure preserved: "Step 4 must contain a row for every boundary listed here, in order" |
| C-03 | Failure point at each boundary | **PASS** | Step 4 DISQUALIFIER present; Step 0 failure mode vocabulary forces platform-specific mechanisms (not "may fail") |
| C-04 | Authorization gaps surfaced | **PASS** | AUTH GAP markup enforced; Step 0 auth vocabulary tightens the upstream Seq# requirement |
| C-05 | Latency sources identified | **PASS** | p50/p99 guidance and sub-5ms annotation preserved; minimum 3 sources stated |
| C-06 | Error path traced end-to-end | **PASS** | Step 9 DISQUALIFIER preserved |
| C-07 | Batch and edge-case handling | **PASS** | Step 10 limit/Seq#/consequence format preserved |
| C-08 | Actionable remediation per failure point | **PASS** | Step 11 Mechanism Type column retained; DISQUALIFIER against "add retry logic" preserved |
| C-09 | Adversarial path comparison | **PASS** | Step 7 mandatory cross-reference block preserved with four required fields |
| C-10 | Critical path named | **PASS** | Step 5 SUM CLOSURE GATE preserved |
| C-11 | Authorization re-walk audit | **PASS** | Step 8 requirement preserved; Step 0 permission vocabulary produces richer per-boundary evidence |
| C-12 | Per-boundary latency budget table | **PASS** | Step 4 p50/p99 columns; SUM CLOSURE GATE in Step 5 |
| C-13 | Threat class catalog | **PASS** | Step 6 construction rules preserved; 5+ rows, 4+ threat classes; Step 0 vocabulary tightens threat class naming |
| C-14 | Remediation parameters quantified | **PASS** | Step 11 Parameters guidance preserved; Step 0 vocabulary supplies exact scope strings |
| C-15 | Multi-boundary threat exhaustiveness | **PASS** | DISQUALIFIER against single Seq# and enumeration shortcuts preserved |
| C-16 | Adversarial scenario catalog-grounded | **PASS** | Step 7 cross-reference block preserved |
| C-17 | Remediation register as dedicated structure | **PASS** | Step 11 dedicated separate table with three required columns |
| C-18 | Exhaustiveness confirmation precedes adversarial | **PASS** | EXHAUSTIVENESS GATE blocking structure preserved; per-row checklist required before Step 7 |
| C-19 | Adversarial candidate pre-marked in catalog | **PASS** | Adv? column enforced during Step 6 construction; DISQUALIFIER against post-hoc fill |
| C-20 | Exhaustiveness gate includes computable summary | **PASS** | Integer count gate summary preserved: "N rows reviewed against Step 3 inventory, X Seq# additions made"; DISQUALIFIER blocks both hedged forms |
| C-21 | Candidate marking committed at exhaustiveness gate | **PASS** | Per-row Adv? field in exhaustiveness checklist preserved; DISQUALIFIER blocks missing or post-hoc fill |

### Score computation

| Tier | Criteria | Pts Each | Available | Earned |
|------|----------|----------|-----------|--------|
| Essential | C-01--C-04 (4xPASS) | 15 | 60 | **60** |
| Recommended | C-05--C-07 (3xPASS) | 10 | 30 | **30** |
| Aspirational | C-08--C-21 (14xPASS) | 5 | 70 | **70** |
| **Total** | | | **160** | **160** |

**160/160** | All essential PASS | Golden: YES
**Gap:** none
**New signal:** Vocabulary coherence -- platform-specific terms propagate from Step 0 into
C-03 failure modes, C-04 auth gaps, C-11 re-walk, and C-14 parameters. C-22 candidate
(qualitative; not yet a computable criterion).

---

## V-03 -- Inertia framing: anti-pattern callout per major step

### Axis
Named anti-pattern block added before each major step. All R6 V-05 structural requirements
preserved identically: blocking gate, integer counts, per-row Adv? field, DISQUALIFIER
enforcement throughout.

### Criterion-by-criterion

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Entry point declared | **PASS** | DISQUALIFIER preserved; anti-pattern block ("A POST with a JSON body from an authenticated user") sets up the exact contrast the DISQUALIFIER enforces |
| C-02 | All service boundaries crossed | **PASS** | GATE preserved; anti-pattern block names what a surface inventory misses (token validation, plugin pipeline, async queues, cache layers) |
| C-03 | Failure point at each boundary | **PASS** | DISQUALIFIER preserved; anti-pattern block ("'may timeout' without a threshold") reinforces mechanism specificity |
| C-04 | Authorization gaps surfaced | **PASS** | AUTH GAP markup enforced; anti-pattern block ("'standard auth' or 'valid token'... hides an auth gap as a confirmation of security") sharpens the gap-detection signal |
| C-05 | Latency sources identified | **PASS** | p50/p99 guidance preserved |
| C-06 | Error path traced end-to-end | **PASS** | Step 9 DISQUALIFIER preserved |
| C-07 | Batch and edge-case handling | **PASS** | Step 10 format preserved |
| C-08 | Actionable remediation per failure point | **PASS** | Step 11 DISQUALIFIER preserved; anti-pattern block ("embedded inline annotations... hide omissions") reinforces dedicated structure |
| C-09 | Adversarial path comparison | **PASS** | Step 7 mandatory cross-reference block preserved; anti-pattern block reinforces catalog-grounded requirement |
| C-10 | Critical path named | **PASS** | Step 5 SUM CLOSURE GATE preserved |
| C-11 | Authorization re-walk audit | **PASS** | Step 8 requirement preserved; anti-pattern block ("A copy of Step 4 is not an audit") directly targets the C-11 failure mode |
| C-12 | Per-boundary latency budget table | **PASS** | Step 4 p50/p99 columns; SUM CLOSURE GATE |
| C-13 | Threat class catalog | **PASS** | Construction rules preserved; anti-pattern block ("single Seq# per threat row") reinforces C-15 |
| C-14 | Remediation parameters quantified | **PASS** | Step 11 quantified parameters guidance preserved |
| C-15 | Multi-boundary threat exhaustiveness | **PASS** | DISQUALIFIER preserved; anti-pattern block names the "single Seq# per threat" failure pattern |
| C-16 | Adversarial scenario catalog-grounded | **PASS** | Cross-reference block preserved; anti-pattern block ("Inventing an adversarial scenario not grounded in the threat catalog") reinforces catalog-grounded requirement |
| C-17 | Remediation register as dedicated structure | **PASS** | Step 11 dedicated table; anti-pattern block targets embedded-inline failure mode directly |
| C-18 | Exhaustiveness confirmation precedes adversarial | **PASS** | EXHAUSTIVENESS GATE blocking structure preserved; per-row checklist required |
| C-19 | Adversarial candidate pre-marked in catalog | **PASS** | Adv? column in Step 6; DISQUALIFIER against post-hoc fill preserved |
| C-20 | Exhaustiveness gate includes computable summary | **PASS** | Integer count gate summary preserved with both DISQUALIFIER blocks |
| C-21 | Candidate marking committed at exhaustiveness gate | **PASS** | Per-row Adv? field in checklist preserved; DISQUALIFIER blocks missing or post-hoc fill |

### Score computation

| Tier | Criteria | Pts Each | Available | Earned |
|------|----------|----------|-----------|--------|
| Essential | C-01--C-04 (4xPASS) | 15 | 60 | **60** |
| Recommended | C-05--C-07 (3xPASS) | 10 | 30 | **30** |
| Aspirational | C-08--C-21 (14xPASS) | 5 | 70 | **70** |
| **Total** | | | **160** | **160** |

**160/160** | All essential PASS | Golden: YES
**Gap:** none
**New signal:** Anti-pattern contrast depth -- each step names the naive failure mode that the
DISQUALIFIER blocks prevent, driving richer responses in C-03, C-04, C-11. Qualitative
dimension only; no new computable criterion.

---

## V-04 -- Role vocabulary + Step 10->6 gate (two-axis)

### Axis
V-02 vocabulary commitment (Step 0) PLUS Step 10 batch-edge-case cross-check elevated
to a blocking gate with a three-integer summary required before Step 11 may begin.
All C-01--C-21 requirements preserved.

### Criterion-by-criterion

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 through C-17 | **PASS** | Identical to V-02 on shared axes; Step 0 vocabulary and all DISQUALIFIER blocks preserved |
| C-18 | Exhaustiveness confirmation precedes adversarial | **PASS** | EXHAUSTIVENESS GATE blocking structure preserved; per-row checklist required before Step 7 |
| C-19 | Adversarial candidate pre-marked in catalog | **PASS** | Adv? column; DISQUALIFIER against post-hoc fill |
| C-20 | Exhaustiveness gate includes computable summary | **PASS** | Integer count gate summary preserved: "N rows reviewed, X Seq# additions made" |
| C-21 | Candidate marking committed at exhaustiveness gate | **PASS** | Per-row Adv? field in checklist preserved with DISQUALIFIER |

### Score computation

| Tier | Criteria | Pts Each | Available | Earned |
|------|----------|----------|-----------|--------|
| Essential | C-01--C-04 (4xPASS) | 15 | 60 | **60** |
| Recommended | C-05--C-07 (3xPASS) | 10 | 30 | **30** |
| Aspirational | C-08--C-21 (14xPASS) | 5 | 70 | **70** |
| **Total** | | | **160** | **160** |

**160/160** | All essential PASS | Golden: YES
**Gap:** none
**New signal:** BATCH-CATALOG CROSS-CHECK GATE produces a computable three-integer artifact:
"N edge cases cross-referenced against M catalog rows, K interactions found." This is
independently testable and does not overlap with C-20 (which gates Step 6 rows against
Step 3 inventory). C-22 candidate.

---

## V-05 -- Combined: role vocabulary + anti-patterns + batch-catalog gate + cross-step Rem#

### Axis
Three-axis combination: Step 0 vocabulary commitment + anti-pattern blocks per step +
BATCH-CATALOG CROSS-CHECK GATE at Step 10 + NEW: Steps 7 and 9 must each cite applicable
Rem# entries from the Step 11 Register at the divergence/origination boundary.

### Criterion-by-criterion

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 through C-17 | **PASS** | All R6 V-05 structural requirements preserved; Step 0 vocabulary + anti-pattern blocks add depth but do not break any criterion |
| C-18 | Exhaustiveness confirmation precedes adversarial | **PASS** | EXHAUSTIVENESS GATE blocking structure preserved |
| C-19 | Adversarial candidate pre-marked in catalog | **PASS** | Adv? column enforced; DISQUALIFIER against zero or multiple Y |
| C-20 | Exhaustiveness gate includes computable summary | **PASS** | Integer count gate summary with both DISQUALIFIER blocks |
| C-21 | Candidate marking committed at exhaustiveness gate | **PASS** | Per-row Adv? field in checklist with DISQUALIFIER blocks |

### Score computation

| Tier | Criteria | Pts Each | Available | Earned |
|------|----------|----------|-----------|--------|
| Essential | C-01--C-04 (4xPASS) | 15 | 60 | **60** |
| Recommended | C-05--C-07 (3xPASS) | 10 | 30 | **30** |
| Aspirational | C-08--C-21 (14xPASS) | 5 | 70 | **70** |
| **Total** | | | **160** | **160** |

**160/160** | All essential PASS | Golden: YES
**Gap:** none
**New signals:**
- C-22 candidate: BATCH-CATALOG CROSS-CHECK GATE three-integer summary (N cases, M rows, K interactions)
- C-23 candidate: adversarial trace (Step 7) and error path (Step 9) each cite applicable Rem#
  entries from Register at divergence/origination boundary; absence or non-traceable citation
  is independently testable

---

## Rankings

| Rank | Variation | Score | Gap | All Essential |
|------|-----------|-------|-----|---------------|
| 1 | V-02 (vocabulary commitment) | **160/160** | -- | PASS |
| 1 | V-03 (anti-pattern framing) | **160/160** | -- | PASS |
| 1 | V-04 (vocabulary + batch-catalog gate) | **160/160** | -- | PASS |
| 1 | V-05 (combined: all axes + Rem# citation) | **160/160** | -- | PASS |
| 5 | V-01 (advisory phrasing) | **150/160** | -5 C-20, -5 C-21 | PASS |

V-01 confirms the R6 finding: removing DISQUALIFIER enforcement pressure from the
exhaustiveness gate produces the same -10 pt gap (C-20 -5, C-21 -5) as R6 V-01 and
R6 V-02. The criterion is stable.

V-02, V-03, V-04, V-05 tie at 160/160 because R7 axes do not intersect the existing
C-01--C-21 testable surface -- they operate above it, revealing qualitative dimensions
and new computable candidates without degrading any current criterion.

---

## Excellence Signals -- V-05 (top-ranked: most new candidates)

**ES-1: Batch-catalog cross-check gate (C-22 candidate)**
V-04 and V-05 require a three-integer summary at Step 10 before Step 11 may begin:
N edge cases, M catalog rows examined, K interactions found. The exhaustiveness gate
(C-20) closes Step 6 against Step 3. The batch-catalog gate closes Step 10 against
Step 6. These are structurally parallel gates at different levels of the artifact stack,
and a response can pass C-20 while omitting the Step 10 gate entirely. Independently
testable: integer presence, gate placement before Step 11, per-case entries naming actual
catalog row numbers.

**ES-2: Cross-step Rem# citation (C-23 candidate)**
V-05 requires Steps 7 and 9 to each cite applicable Rem# entries from the Register at
the failure boundary. C-08 through C-17 verify that the Register exists and is populated.
C-23 verifies that the adversarial and error path analyses close the loop back to those
entries at the exact point of failure -- a feedback coupling not tested by any current
criterion. A response with a complete Register (C-08, C-14, C-17 PASS) and no back-
reference from Steps 7 or 9 would pass all current criteria but fail C-23. Independently
testable: Rem# field present in Step 7 cross-reference block, Rem# traceable to a
Register row, same in Step 9 remediation close-out.

**ES-3: Vocabulary propagation coherence (qualitative, not yet a criterion)**
V-02, V-04, V-05 bind platform-specific terminology at Step 0 and enforce it through
DISQUALIFIER pressure at Steps 4, 7, 11. This produces responses where failure modes,
auth gap labels, and remediation scope strings use the same vocabulary set -- a coherence
dimension that the current rubric tests indirectly (C-03, C-04, C-14) but does not
test as a cross-step property. No computable criterion yet identified; the test would
require comparing vocabulary tokens across steps, which is a scoring task beyond binary
PASS/FAIL.

---

## New Patterns Assessment

| Signal | Disposition |
|--------|-------------|
| BATCH-CATALOG CROSS-CHECK GATE three-integer summary (V-04, V-05) | C-22 candidate -- independently testable; does not overlap C-20; dependency on C-07 (batch cases must exist) and C-13 (threat catalog must exist) |
| Cross-step Rem# citation in Steps 7 and 9 (V-05) | C-23 candidate -- independently testable; does not overlap C-08/C-14/C-17 (Register content vs. back-reference); dependency on C-08 + C-09 + C-06 |
| Vocabulary coherence across steps (V-02, V-03, V-04, V-05) | Not promoted -- no single computable artifact; improves response quality but test requires cross-step token comparison, not binary field presence |
| V-01 advisory regression (-10 pts) | Confirms rubric stability -- DISQUALIFIER enforcement is load-bearing for C-20 and C-21; criterion design is correct |

Both C-22 and C-23 are independently testable and have no existing criterion overlap.
They represent the live scoring surface for R8.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["C-22: batch-catalog cross-check gate computable summary (N cases, M catalog rows, K interactions) required before Step 11", "C-23: adversarial trace (Step 7) and error path (Step 9) must each cite applicable Rem# entries from Register at divergence/origination boundary"]}
```
