# trace-request Rubric — v9 (2026-03-15)

**Scale:** 190 (Essential 60 + Recommended 30 + Aspirational 100)
**Golden threshold:** all 4 essential PASS AND composite >= 80

---

## Essential Criteria (weight: 60 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Boundary inventory complete** | coverage | Every service boundary the request will cross is enumerated in a sequential numbered table (Seq#) in traversal order, including: API gateway, authentication service, routing layer, each microservice or platform service, each storage system, any async queue or event bus, cache layers, and response assembly path. GATE: the traversal table must contain a row for every boundary in the inventory, in order. DISQUALIFIER: prose-only enumeration without a structured table; omitting token validation, plugin pipeline stages, async queues, or cache layers. |
| C-02 | **Step-0 binding declared** | coverage | The response opens with a Step-0 role and vocabulary declaration naming: the platform role adopted, the auth mechanism with specific scope string (not "valid token"), the primary service boundary names as the platform names them, the failure mode vocabulary (specific HTTP codes and behaviors, not "throttled"), and the permission model terms (specific privilege names, not "read permission"). The vocabulary commitment is forward-binding: all subsequent steps must use these terms, not generic substitutes. DISQUALIFIER: role declared without vocabulary commitment; generic vocabulary used in any step after Step 0. |
| C-03 | **Failure points per boundary** | correctness | Every boundary row in the traversal table carries a named failure mode with specific mechanism and behavioral consequence: HTTP status code, timeout threshold plus behavior, throttle rate plus breach behavior, auth rejection type. DISQUALIFIER: "may fail," "could error," or "an exception might be thrown" without a named mechanism; blank Failure Point cells. |
| C-04 | **Auth check per boundary** | correctness | Every boundary row carries an explicit authorization annotation naming the specific scope string, role identity, or mechanism evaluated. Boundaries with no auth requirement are explicitly marked. Auth gaps are flagged "AUTH GAP -- [reason]." DISQUALIFIER: "standard auth," "valid token," or "handled upstream" without naming the mechanism or upstream boundary; blank auth cells. |

---

## Recommended Criteria (weight: 30 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Latency sources identified** | depth | Each boundary or processing step contributing non-trivial latency is annotated with p50/p99 estimate. At least three distinct latency sources named. DISQUALIFIER: "fast," "low," or blank. Sub-5ms entries annotated as "< 5ms -- [reason]." |
| C-06 | **Error path traced end-to-end** | coverage | At least one full error path traced from origination point to caller response, showing how errors propagate, transform, or get swallowed across boundaries. DISQUALIFIER: "error returned to caller" without the propagation chain. |
| C-07 | **Batch and edge-case handling** | depth | Batch operations, pagination, or concurrent-request edge cases are called out and analyzed -- not just mentioned. Each entry names the specific limit, the boundary where it applies, and the behavioral consequence of hitting it. |

---

## Aspirational Criteria (weight: 100 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Actionable remediation per failure point** | behavior | Every failure point from C-03 is paired with a concrete mitigation naming the mechanism type: retry policy, circuit breaker, permission scope addition, payload validation guard. DISQUALIFIER: "add error handling," "add retry logic" without a mechanism type. |
| C-09 | **Adversarial path comparison** | depth | At least one adversarial scenario (malformed payload, expired token, concurrent mutation, missing required field) shows how the path diverges from nominal -- naming the specific boundary Seq# where divergence occurs, the adversarial condition, the post-divergence path, and the concrete outcome. |
| C-10 | **Critical path named** | depth | The trace identifies the critical path: the specific Seq# chain whose cumulative latency determines worst-case response time. Parallel or cached paths are distinguished. Critical-path p50 and p99 estimated. Per-boundary rows are the source; totals are derived. A trace that lists sources but does not identify the critical sequence fails. |
| C-11 | **Authorization re-walk audit** | correctness | A dedicated second-pass authorization audit walks the full boundary list focused on privilege escalation paths, missing scope validations, and assumed-but-unverified auth. Must name at least one new gap or explicitly confirm per-boundary that the three highest-risk boundaries are clean. DISQUALIFIER: re-walk section that mirrors Step 3 auth fields without raising new questions. |
| C-12 | **Per-boundary latency budget table** | depth | The traversal carries a dedicated p50/p99 budget column for every boundary. Non-parallel segments sum to the critical-path total from C-10; parallel segments are not double-counted. SUM CLOSURE GATE: if per-boundary sums differ from critical-path total, the response must reconcile before proceeding. Prose latency annotation without a structured column fails. |
| C-13 | **Threat class catalog** | depth | A structured threat catalog table maps at least four distinct threat classes to the specific boundary Seq numbers where each manifests. At least five rows, four required. DISQUALIFIER: fewer than four threat classes; single-boundary row for a threat known to manifest at multiple boundaries. |
| C-14 | **Remediation parameters quantified** | depth | Every remediation item from C-08 includes quantified operational parameters: retry policies name algorithm, initial delay, multiplier, and max-attempts; circuit breakers name threshold and reset interval; permission fixes name the exact scope string or role identity; payload guards name the specific field and validation predicate. DISQUALIFIER: mechanism type named without operational parameters. |
| C-15 | **Multi-boundary threat exhaustiveness** | coverage | Every entry in the threat class catalog lists ALL applicable boundary Seq numbers -- not only the primary or highest-risk one. A threat class that manifests at boundaries 2, 5, and 7 must cite all three. DISQUALIFIER: single Seq# for a threat known to manifest at multiple boundaries; enumeration shortcuts ("multiple," "various"). If C-13 is not met, C-15 fails automatically. |
| C-16 | **Adversarial scenario catalog-grounded** | coverage | The adversarial path comparison (C-09) is explicitly grounded in the threat class catalog (C-13). A mandatory cross-reference block appears before the adversarial trace with four required fields: catalog row #, exact threat class name, all catalog Seq# for that row, and selected divergence Seq#. An ad-hoc adversarial scenario without cross-reference fails. If C-13 is not met, C-16 fails automatically. |
| C-17 | **Remediation register as dedicated structure** | depth | The remediation output is organized as a dedicated separate table -- a Remediation Register -- distinct from the primary boundary traversal table. The register includes at minimum three discrete columns: failure reference (boundary Seq# or row ID), mechanism type, and parameters. Remediation items embedded as inline annotations within the traversal table fail this criterion even when individually C-08- and C-14-compliant. The dedicated structure makes incomplete Parameters cells structurally visible as omissions. |
| C-18 | **Exhaustiveness confirmation precedes adversarial section** | depth | Before the adversarial scenario section begins, the response includes an explicit on-record confirmation that the threat class catalog exhaustiveness check was completed. The confirmation must demonstrate re-examination: it names rows checked, references the boundary inventory, or lists any Seq# values added. DISQUALIFIER: bare "confirmed" assertion without naming rows or referencing inventory; confirmation that appears after the adversarial section begins. If C-15 is not met, C-18 fails automatically. |
| C-19 | **Adversarial candidate pre-marked in threat catalog** | coverage | The threat class catalog includes a candidate-marking column with exactly one row marked Y and all other rows marked N, this marking present in the catalog table before the adversarial section begins. The adversarial scenario references the Y-marked row. DISQUALIFIER: no candidate column; candidate column with zero or multiple Y values; adversarial scenario referencing a row not pre-marked Y. If C-16 is not met, C-19 fails automatically. |
| C-20 | **Exhaustiveness gate includes computable summary** | depth | The exhaustiveness confirmation section includes a structured gate summary stating the exact number of catalog rows reviewed and the exact number of Seq# additions made -- in a computable format (e.g., "N rows reviewed against Step 2 inventory, X Seq# additions made"). A per-row checklist without a summary count fails. A summary that omits either count fails. A summary using approximate or hedged language ("all rows," "a few additions") fails. The counts must be integers derivable from the catalog and boundary inventory. If C-18 is not met, C-20 fails automatically. |
| C-21 | **Candidate marking committed at exhaustiveness gate** | coverage | Each row in the per-row exhaustiveness checklist carries a candidate-marking field (e.g., "Adv? = Y" or "Adv? = N"), filled before the adversarial section begins. The Adv? = Y checklist entry must correspond to the same catalog row as the catalog Y-marked candidate. This dual-locks the forward pointer: the threat catalog establishes the candidate during enumeration (C-19); the exhaustiveness checklist confirms it during re-examination (C-21). A checklist without a candidate field per row fails. A checklist with the field blank or filled after the adversarial section begins fails. If C-18 is not met or C-19 is not met, C-21 fails automatically. |
| C-22 | **Batch-catalog cross-check gate computable summary** | depth | Before the remediation register section begins, the response includes a three-integer cross-check gate summarizing the batch/edge-case analysis against the threat catalog: "N edge cases x M catalog rows -> K interactions found." All three integers must be present and non-approximate. The gate must appear after the batch section (C-07) and before the register section, and per-case entries within the batch section must cite actual catalog row numbers from C-13. A prose assertion ("all edge cases checked") without the three-integer format fails. A gate present but missing any one integer fails. If C-07 is not met or C-13 is not met, C-22 fails automatically. |
| C-23 | **Adversarial and error traces cite Rem# entries at divergence boundary** | coverage | The adversarial path section (C-09) and the error path section (C-06) each include an explicit back-reference to the applicable Remediation Register entry (Rem# or row ID) at the exact boundary where divergence or error origination occurs. A Register that is structurally complete (C-08, C-14, C-17) but never referenced from within the adversarial or error path trace fails this criterion. The citation must name the specific Rem# and appear inline at the divergence or origination boundary -- not as a trailing summary appended after the trace. A response may have a complete Register and complete adversarial and error traces and still fail C-23 if the two structures are not cross-linked at the point of failure. If C-08 is not met, C-09 is not met, or C-06 is not met, C-23 fails automatically. |
| C-24 | **Batch-catalog cross-check gate table-verifiable** | depth | The three-integer cross-check gate required by C-22 is backed by a visible named table mapping every edge case (EC# rows) against every threat catalog row (TRow columns), with each cell marked "X" (interaction present) or blank (no interaction). The three integers must be independently derivable from the table structure: N = count of EC# rows (must equal count of rows in the edge-case section), M = count of TRow columns (must equal count of rows in the threat class catalog), K = count of "X" cells in the table. A prose "N edge cases x M catalog rows -> K interactions found" statement without a backing table fails. A table present but where the stated K does not match the count of "X" cells fails. DISQUALIFIER: gate integers stated without a backing table; stated K not cell-verifiable from the table. If C-22 is not met, C-24 fails automatically. |
| C-25 | **Per-boundary scope enumeration at auth re-walk** | correctness | The authorization re-walk includes a dedicated per-boundary scope enumeration table that precedes re-walk findings and covers every boundary from the inventory. The table carries four required columns: Scope/Role Invoked (the exact string from Step 0 vocabulary and Step 3 auth check), Required Scope/Role (the minimum scope or role the platform requires for the operation at this boundary), Verified? (Y if the traversal confirms the check occurs at runtime; N if assumed from upstream validation), Gap? (Y if invoked scope does not cover required scope, or if Verified? = N at a boundary where downstream operations depend on this check; N otherwise). Every boundary must name a Required Scope/Role or provide an explicit explanation why none applies. A boundary where Required Scope/Role is blank and Gap? = N is a disallowed shortcut. A narrative re-walk without the scope enumeration table fails even if C-11 re-walk findings are substantive. DISQUALIFIER: scope enumeration table absent; Required Scope/Role cells left blank without explanation; Gap? column absent. If C-11 is not met or C-04 is not met, C-25 fails automatically. |
| C-26 | **Scope-gap Rem# three-way cross-link** | correctness | Every Gap?=Y row in the scope enumeration table (Step 8a / C-25) must cite a dedicated Remediation Register entry (Rem#) in Step 11 with the exact scope string as the Parameters value. When the gap boundary Seq# also appears as a divergence or error origination point in the adversarial or error path traces, the three-way link Step 8a -> Step 11 -> Step 7/9 must be explicitly traceable: the Rem# cited in the scope table, the Rem# entry in the register, and the Rem# inline citation in the trace must all reference the same boundary and the same scope string. A scope gap named in the enumeration table without a corresponding Rem# citation is a half-audit: the problem is identified without committing to the fix string. DISQUALIFIER: any Gap?=Y row in the scope enumeration table without a Rem# citation in Step 11; Rem# Parameters that omit or misstate the exact scope string from the Gap?=Y row; the three-way link absent when the boundary Seq# appears in adversarial or error traces. If C-25 is not met or C-23 is not met, C-26 fails automatically. |
| C-27 | **Vocabulary conformance gate** | correctness | Step 0 assigns a VT# identifier to each committed vocabulary term, making every term individually addressable. Step 3a (or an equivalent pre-Step-4 conformance pass) produces a per-term conformance table checking each VT# term against its actual usage in the Step 3 auth check cells. The table yields a D-integer (count of deviations: cells using a generic substitute instead of the committed term). A D=0 gate summary is required before Step 4 begins. D > 0 triggers a correction cycle back to Step 3; the correction must be completed and the D=0 gate re-confirmed before the trace proceeds. This converts C-02's narrative forward-binding declaration into a computable structural check: the vocabulary commitment is not asserted, it is verified. DISQUALIFIER: Step 0 vocabulary declared without VT# identifiers; per-term conformance table absent; D-integer gate summary absent before Step 4; D > 0 without a documented correction cycle; correction cycle not completed before Step 4 proceeds. If C-02 is not met, C-27 fails automatically. |

---

## Scoring Worksheet

| Tier | Criteria | Pts Each | Points Available | Points Earned |
|------|----------|----------|-----------------|---------------|
| Essential | C-01, C-02, C-03, C-04 | 15 | 60 | -- |
| Recommended | C-05, C-06, C-07 | 10 | 30 | -- |
| Aspirational | C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27 | 5 | 100 | -- |
| **Total** | | | **190** | -- |

All criteria are binary: pass = full points, fail = 0. PARTIAL is permitted during scoring
rounds when a criterion is substantively attempted but a named failure mode applies; PARTIAL
earns 2 points and is flagged as a gap signal for the next rubric version.

**Golden**: all 4 essential PASS AND composite >= 80.

---

## Dependency Map

```
C-13 (threat catalog)
  +-- C-15 (multi-boundary exhaustiveness)
  |     +-- C-18 (exhaustiveness confirmation precedes adversarial)
  |           +-- C-20 (computable gate summary)
  |           +-- C-21 (candidate marking in gate checklist)*
  +-- C-09 (adversarial path)
  |     +-- C-16 (catalog-grounded)
  |           +-- C-19 (candidate pre-marked in catalog)
  |                 +-- C-21 (candidate marking in gate checklist)*
  +-- C-22 (batch-catalog cross-check gate)**
        +-- C-24 (cross-check gate table-verifiable)

C-07 (batch/edge-case handling)
  +-- C-22 (batch-catalog cross-check gate)**
        +-- C-24 (cross-check gate table-verifiable)

C-08 (actionable remediation)
  +-- C-14 (parameters quantified)
  |     +-- C-17 (dedicated register structure)
  +-- C-23 (Rem# citation at divergence/origination boundary)***

C-09 (adversarial path)
  +-- C-23 (Rem# citation at divergence boundary)***
        +-- C-26 (scope-gap Rem# three-way cross-link)****

C-06 (error path)
  +-- C-23 (Rem# citation at error origination boundary)***
        +-- C-26 (scope-gap Rem# three-way cross-link)****

C-10 (critical path)
  +-- C-12 (per-boundary budget, sums to C-10)

C-04 (auth check per boundary)
  +-- C-25 (per-boundary scope enumeration)
        +-- C-26 (scope-gap Rem# three-way cross-link)****

C-11 (auth re-walk audit)
  +-- C-25 (per-boundary scope enumeration)
        +-- C-26 (scope-gap Rem# three-way cross-link)****

C-02 (Step-0 binding declared)
  +-- C-27 (vocabulary conformance gate)

* C-21 has dual parents: C-18 (checklist structure exists) and C-19 (candidate column
  exists). Both must pass for C-21 to be eligible.

** C-22 has dual parents: C-07 (batch section exists with per-case entries) and C-13
   (catalog exists with row numbers to cite). Both must pass for C-22 to be eligible.

*** C-23 has three parents: C-08 (Register exists), C-09 (adversarial trace exists),
    and C-06 (error trace exists). All three must pass for C-23 to be eligible.

**** C-26 has dual parents: C-25 (scope enumeration table with Gap? column exists) and
     C-23 (Rem# citations exist in the Register and are linked from traces). Both must
     pass for C-26 to be eligible.
```

---

## Why C-26 and C-27 are independent of their parents

**C-26 vs C-25:** C-25 tests that a structured scope enumeration table precedes re-walk
findings, with Gap? column populated. C-26 tests that every Gap?=Y row in that table
propagates to a named Rem# in Step 11 with the exact scope string as Parameters, and
that the link is traceable when the boundary also appears in adversarial/error traces.
A response can produce a complete scope enumeration table with all Gap?=Y rows correctly
identified and pass C-25, then fail C-26 if none of those gaps are wired to Remediation
Register entries. The table satisfies the exhaustiveness-surface contract; the cross-link
satisfies the audit-closure contract.

**C-27 vs C-02:** C-02 tests that Step 0 declares a role and forward-binding vocabulary
with specific scope strings and permission model terms. C-27 tests that the vocabulary
commitment is structurally verified rather than narratively asserted: VT# identifiers are
assigned, a per-term conformance table is produced, and a D=0 gate is confirmed before
Step 4. A response can open with a precise Step-0 vocabulary declaration and pass C-02,
then fail C-27 if no VT# identifiers appear and no per-term check follows. The declaration
satisfies the commitment contract; the conformance gate satisfies the verifiability contract.

---

## Signals not promoted from R9

| Signal considered | Disposition |
|---|---|
| ES-3 (V-05 only): VT# scope string propagates coherently across Step 3 Auth Check, Step 8a Scope/Role Invoked, and Step 11 Permission Fix Parameters for the same Gap?=Y boundary | Not promoted -- design surface only. Requires both C-26 (three-way cross-link exists) and C-27 (vocabulary terms are VT#-addressable) to produce consistent round evidence before a computable binary can be defined. Strong C-28 candidate when C-26 and C-27 both yield multi-round data. |

---

## Round History

| Round | Rubric | Scale | Top Score | Key addition |
|-------|--------|-------|-----------|--------------|
| R3 | v3 | 120 | -- | C-10, C-11, C-12, C-13 |
| R4 | v4 | 135 | 135/135 (V-01,02,04,05) | C-14, C-15, C-16 |
| R5 | v5 | 150 | -- | C-17, C-18, C-19 |
| R6 | v6 | 160 | -- | C-20, C-21 |
| R7 | v7 | 170 | 160/160 (V-02,03,04,05) | C-22, C-23 |
| R8 | v8 | 180 | 170/170 (V-03,04,05) | C-24, C-25 |
| R9 | v9 | 190 | 180/180 (V-03,04,05) | C-26, C-27 |
