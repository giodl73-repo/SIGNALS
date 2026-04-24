`trace-request-rubric-v5-2026-03-14.md` written. Here's the extraction summary:

---

**Three new criteria from R4 excellence signals:**

| New criterion | R4 excellence signal | What's testable on the response |
|---|---|---|
| **C-17** Remediation register as dedicated structure | Signal 1: three-layer enforcement (vocabulary source + **structural container** + text constraint) | Does a dedicated Remediation Register table exist, separate from the traversal table, with discrete Mechanism Type and Parameters columns? |
| **C-18** Exhaustiveness confirmation precedes adversarial section | Signal 2: lifecycle gate as **blocking condition**, not advisory paragraph | Does the response include an explicit on-record confirmation naming rows checked before the adversarial section begins? "Confirmed" alone fails; must demonstrate re-examination. |
| **C-19** Adversarial candidate pre-marked in threat catalog | Signal 3: C-16 Candidate as **forward pointer** (commit during enumeration), not backward lookup (rationalize post-hoc) | Does the catalog table contain a candidate-marking column with exactly one Y, present before the adversarial section? |

**Scale:** 135 → **150** (aspirational tier: 9 → 12 criteria, 45 → 60 pts). Golden threshold stays at ≥ 80.

**Dependency additions:**
- C-18 inherits from C-15 (which inherits from C-13)
- C-19 inherits from C-16 (which inherits from C-13 + C-09)
- C-17 is independent (inherits from C-14 by subject matter, but not by chain — a response can fail C-17 while passing C-14)

**Signal not promoted:** The C-07/C-13 cross-linking pattern from V-05 Step 10 evidence ("does this limit interact with the concurrent mutation class from Step 6?") was considered but is not named as a standalone excellence signal in the R4 scorecard, so it goes in the disposition table rather than becoming C-20.
04/V-05 blocking condition) vs 'for each row, re-examine your Step 3 boundary
inventory' (V-01 advisory paragraph)." C-15 requires each catalog entry to enumerate ALL
applicable boundaries. C-18 requires that the response include an explicit exhaustiveness
confirmation statement before the adversarial section begins -- demonstrating the check was
performed, not merely that the Seq# values happen to be complete. The confirmation may take the
form of a per-row verification checklist, an explicit "exhaustiveness check complete" summary
naming any added Seq# values discovered, or a gate statement certifying all rows were evaluated
against the full boundary inventory. A response that lists all Seq# (C-15 satisfied) without
any on-record confirmation that the check was performed before proceeding fails C-18. A
confirmation that consists only of "confirmed" without naming the rows or referencing the
boundary inventory fails -- the confirmation must demonstrate re-examination, not assert it.
If C-15 is not met, C-18 fails automatically.

**C-19 -- Adversarial candidate pre-marked in threat catalog** (coverage, 5 pts)

Extracted from R4 excellence signal 3: "C-16 Candidate as forward pointer, not backward lookup
-- marking the adversarial selection source with a C-16 Candidate = Y column during Step 6
(catalog construction) converts Step 7's cross-reference block from a backward lookup into a
forward pointer. The commitment is made during catalog construction when the model is in
systematic enumeration mode, not during adversarial scenario selection when the model may
rationalize a choice post-hoc." C-16 requires the adversarial scenario to be grounded in the
threat class catalog. C-19 requires that grounding to have been established prospectively: the
threat class catalog must include a candidate-marking column (e.g., "C-16 Candidate" or "Adv?")
with exactly one row marked Y and all other rows marked N, this marking appearing in the catalog
table before the adversarial section begins. The adversarial scenario then references the Y-
marked row. A catalog that contains no candidate column fails. A candidate column with zero or
multiple Y values fails. An adversarial scenario that references a catalog row not pre-marked Y
fails -- even if the cross-reference block is otherwise C-16-compliant. If C-16 is not met,
C-19 fails automatically.

---

### Why these three, not others

| Signal considered | Disposition |
|---|---|
| Three-layer enforcement: vocabulary source + structural container + text constraint (V-05 C-14) | C-17 -- structural container (dedicated register) is the independently testable response artifact signal; vocabulary source and text constraint are already enforced by C-14 |
| Lifecycle gate as blocking condition vs advisory paragraph (V-04/V-05 C-15) | C-18 -- explicit exhaustiveness confirmation on record is the response artifact signal |
| C-16 Candidate as forward pointer vs backward lookup (V-02/V-04 C-16) | C-19 -- candidate marker column in catalog table is the response artifact signal |
| V-05 Step 10 cross-catalog edge case interaction (C-07 evidence) | Not promoted -- structural linking of C-07 and C-13 noted in C-07 evidence but not named as a standalone excellence signal in R4 |
| V-03 structural-vs-text-constraint diagnostic | Not promoted -- diagnostic about constraint type effectiveness, not a new response signal |

---

### Why C-17, C-18, C-19 don't overlap with existing criteria

**C-17 vs C-08 and C-14:** C-08 requires a specific mechanism type named per failure point.
C-14 requires that mechanism to carry quantified operational parameters. C-17 requires the
remediation output itself to be organized as a dedicated separate table. A response may satisfy
C-08 (mechanism named) and C-14 (parameters quantified) entirely through inline annotations in
the traversal table and fail C-17. A dedicated register satisfies C-17 regardless of whether
inline annotations also appear.

**C-18 vs C-15:** C-15 requires each catalog entry to list ALL applicable boundary Seq numbers.
C-18 requires an explicit on-record confirmation that the check producing those Seq# values was
performed before the adversarial section. These are independent: a response can list all Seq#
(C-15 PASS) without confirming the check was performed (C-18 FAIL), and a response can include
a confirmation statement but omit a boundary Seq# from a catalog row (C-18 PASS, C-15 FAIL).

**C-19 vs C-16:** C-16 requires the adversarial scenario to name the threat class from the
catalog and cite the divergence boundary Seq# from that catalog row. C-19 requires the selection
to have been pre-committed during catalog construction, evidenced by a candidate-marking column
in the catalog table. A response can produce a cross-reference block with all four required
fields (C-16 PASS) while selecting the row post-hoc without a candidate column (C-19 FAIL). The
distinction captures whether the adversarial selection was part of systematic enumeration or
retrospective justification.

---

### Dependency chain

C-18 depends on C-15 (which depends on C-13).
C-19 depends on C-16 (which depends on C-13 and C-09).
C-17 is independent.

---

### Scoring recap

| Tier | Criteria | Pts Each | Available |
|---|---|---|---|
| Essential | C-01--C-04 | 15 | 60 |
| Recommended | C-05--C-07 | 10 | 30 |
| Aspirational | C-08--C-19 | 5 | 60 |
| **Total** | | | **150** |

Golden: all 4 essential PASS + composite >= 80.

---

## Essential Criteria (weight: 60 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Entry point declared** | coverage | The trace names the exact entry point: HTTP method, path, payload shape, and caller identity. Missing or vague entry point fails. DISQUALIFIER: "a POST request" (no path), "a JSON body" (no field names), "an authenticated user" (no credential type). |
| C-02 | **All service boundaries crossed** | coverage | Every distinct service boundary in the request path is enumerated in traversal order. Any boundary skipped -- including well-known steps like token validation -- fails. GATE: traversal table rows must correspond to the boundary inventory in order; no boundary listed may be absent from the table. |
| C-03 | **Failure point at each boundary** | correctness | For every boundary, at least one concrete failure mode is identified with exact mechanism: HTTP status code, timeout threshold + behavior, throttle rate + breach behavior, auth rejection type. DISQUALIFIER: "may fail," "could error," "an exception might be thrown" without a named mechanism. |
| C-04 | **Authorization gaps surfaced** | correctness | The trace identifies where authorization is checked or not, names the permission/scope/role evaluated, and flags any boundary where authorization is absent or assumed. DISQUALIFIER: "standard auth," "valid token," "handled upstream" without naming the upstream boundary. Auth gaps marked "AUTH GAP -- [reason]." |

---

## Recommended Criteria (weight: 30 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Latency sources identified** | depth | Each boundary or processing step contributing non-trivial latency is annotated with p50/p99 estimate. At least three distinct latency sources named. DISQUALIFIER: "fast," "low," or blank. Sub-5ms entries annotated as "< 5ms -- [reason]." |
| C-06 | **Error path traced end-to-end** | coverage | At least one full error path traced from origination point to caller response, showing how errors propagate, transform, or get swallowed across boundaries. DISQUALIFIER: "error returned to caller" without the propagation chain. |
| C-07 | **Batch and edge-case handling** | depth | Batch operations, pagination, or concurrent-request edge cases are called out and analyzed -- not just mentioned. Each entry names the specific limit, the boundary where it applies, and the behavioral consequence of hitting it. |

---

## Aspirational Criteria (weight: 60 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Actionable remediation per failure point** | behavior | Every failure point from C-03 is paired with a concrete mitigation naming the mechanism type: retry policy, circuit breaker, permission scope addition, payload validation guard. DISQUALIFIER: "add error handling," "add retry logic" without a mechanism type. |
| C-09 | **Adversarial path comparison** | depth | At least one adversarial scenario (malformed payload, expired token, concurrent mutation, missing required field) shows how the path diverges from nominal -- naming the specific boundary Seq# where divergence occurs, the adversarial condition, the post-divergence path, and the concrete outcome. |
| C-10 | **Critical path named** | depth | The trace identifies the critical path: the specific Seq# chain whose cumulative latency determines worst-case response time. Parallel or cached paths are distinguished. Critical-path p50 and p99 estimated. Per-boundary rows are the source; totals are derived. A trace that lists sources but does not identify the critical sequence fails. |
| C-11 | **Authorization re-walk audit** | correctness | A dedicated second-pass authorization audit walks the full boundary list focused on privilege escalation paths, missing scope validations, and assumed-but-unverified auth. Must name at least one new gap or explicitly confirm per-boundary that the three highest-risk boundaries are clean. DISQUALIFIER: re-walk section that mirrors Step 4's auth fields without raising new questions. |
| C-12 | **Per-boundary latency budget table** | depth | The traversal carries a dedicated p50/p99 budget column for every boundary. Non-parallel segments sum to the critical-path total from C-10; parallel segments are not double-counted. SUM CLOSURE GATE: if per-boundary sums differ from critical-path total, the response must reconcile before proceeding. Prose latency annotation without a structured column fails. |
| C-13 | **Threat class catalog** | depth | A structured threat catalog table maps at least four distinct threat classes to the specific boundary Seq numbers where each manifests. At least five rows, four required. DISQUALIFIER: fewer than four threat classes; single-boundary row for a threat known to manifest at multiple boundaries. |
| C-14 | **Remediation parameters quantified** | depth | Every remediation item from C-08 includes quantified operational parameters: retry policies name algorithm, initial delay, multiplier, and max-attempts; circuit breakers name threshold and reset interval; permission fixes name the exact scope string or role identity; payload guards name the specific field and validation predicate. DISQUALIFIER: mechanism type named without operational parameters. |
| C-15 | **Multi-boundary threat exhaustiveness** | coverage | Every entry in the threat class catalog lists ALL applicable boundary Seq numbers -- not only the primary or highest-risk one. A threat class that manifests at boundaries 2, 5, and 7 must cite all three. DISQUALIFIER: single Seq# for a threat known to manifest at multiple boundaries; enumeration shortcuts ("multiple," "various"). If C-13 is not met, C-15 fails automatically. |
| C-16 | **Adversarial scenario catalog-grounded** | coverage | The adversarial path comparison (C-09) is explicitly grounded in the threat class catalog (C-13). A mandatory cross-reference block appears before the adversarial trace with four required fields: catalog row #, exact threat class name, all catalog Seq# for that row, and selected divergence Seq#. An ad-hoc adversarial scenario without cross-reference fails. If C-13 is not met, C-16 fails automatically. |
| C-17 | **Remediation register as dedicated structure** | depth | The remediation output is organized as a dedicated separate table -- a Remediation Register -- distinct from the primary boundary traversal table. The register includes at minimum three discrete columns: failure reference (boundary Seq# or row ID), mechanism type, and parameters. Remediation items embedded as inline annotations within the traversal table fail this criterion even when individually C-08- and C-14-compliant. The dedicated structure makes incomplete Parameters cells structurally visible as omissions. |
| C-18 | **Exhaustiveness confirmation precedes adversarial section** | depth | Before the adversarial scenario section begins, the response includes an explicit on-record confirmation that the threat class catalog exhaustiveness check was completed. The confirmation must demonstrate re-examination: it names rows checked, references the boundary inventory, or lists any Seq# values added. DISQUALIFIER: bare "confirmed" assertion without naming rows or referencing inventory; confirmation that appears after the adversarial section begins. If C-15 is not met, C-18 fails automatically. |
| C-19 | **Adversarial candidate pre-marked in threat catalog** | coverage | The threat class catalog includes a candidate-marking column with exactly one row marked Y and all other rows marked N, this marking present in the catalog table before the adversarial section begins. The adversarial scenario references the Y-marked row. DISQUALIFIER: no candidate column; candidate column with zero or multiple Y values; adversarial scenario referencing a row not pre-marked Y. If C-16 is not met, C-19 fails automatically. |

---

## Scoring Worksheet

| Tier | Criteria | Pts Each | Points Available | Points Earned |
|------|----------|----------|-----------------|---------------|
| Essential | C-01, C-02, C-03, C-04 | 15 | 60 | -- |
| Recommended | C-05, C-06, C-07 | 10 | 30 | -- |
| Aspirational | C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19 | 5 | 60 | -- |
| **Total** | | | **150** | -- |

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
  +-- C-09 (adversarial path)
        +-- C-16 (catalog-grounded)
              +-- C-19 (candidate pre-marked in catalog)

C-08 (actionable remediation)
  +-- C-14 (parameters quantified)
        +-- C-17 (dedicated register structure)  [independent of C-13 chain]

C-10 (critical path)
  +-- C-12 (per-boundary budget, sums to C-10)
```

---

## Round History

| Round | Rubric | Scale | Top Score | V-03 Score | Key addition |
|-------|--------|-------|-----------|------------|--------------|
| R3 | v3 | 120 | -- | PARTIAL on C-11/C-12/C-13 | C-10, C-11, C-12, C-13 |
| R4 | v4 | 135 | 135/135 (V-01,02,04,05) | 120/135 | C-14, C-15, C-16 |
| R5 | v5 | 150 | -- | -- | C-17, C-18, C-19 |
