`trace-request-rubric-v6-2026-03-14.md` written. Here is the extraction summary:

---

**Two new criteria from R5 excellence signals:**

| New criterion | R5 excellence signal | What is testable on the response |
|---|---|---|
| **C-20** Exhaustiveness gate includes computable summary | V-04/V-05 excellence over V-02: gate names exact row count and Seq# addition count, not a bare assertion | Does the exhaustiveness section include a structured summary with integer row count and integer additions count? |
| **C-21** Candidate marking committed at exhaustiveness gate | V-05 excellence over V-03/V-04: per-row checklist carries Adv? field, dual-locking the forward pointer at re-examination time | Does each row of the per-row exhaustiveness checklist carry a candidate-marking field, present and filled before the adversarial section? |

**Scale:** 150 -> **160** (aspirational tier: 12 -> 14 criteria, 60 -> 70 pts). Golden threshold stays at >= 80.

---

**Signal not promoted:** V-05 labeled DISQUALIFIER `(C-14, C-17)` block naming five specific failing Parameters patterns. This is rubric enforcement vocabulary -- it improves scoring consistency but the testable criterion is already C-14 (parameters present) and C-17 (dedicated register). No new response artifact.

---

**Why these don't overlap:**

- **C-20 vs C-18:** C-18 requires demonstrating re-examination (name rows, reference inventory). C-20 requires the demonstration to include *integer counts* in a computable format. A checklist that names every row (C-18 PASS) without a summary count (C-20 FAIL) is the exact split seen between V-02 and V-04.
- **C-21 vs C-18 and C-19:** C-19 requires the candidate column in the catalog table. C-21 requires that same commitment to appear *in the per-row exhaustiveness checklist rows* -- so the forward pointer is locked during re-examination, not just during initial enumeration. V-05 vs V-04 is the exact split.

**Dependency additions:**
- C-20 depends on C-18 (C-18 -> C-15 -> C-13)
- C-21 depends on **both** C-18 (checklist structure must exist) and C-19 (candidate column must exist); both parents required
reviewed and the number of Seq# additions
made. A response can produce a per-row checklist naming every row (C-18 PASS) without stating
the row count or additions count (C-20 FAIL). A response can state "3 rows reviewed, 2
additions" alongside individual row entries (C-20 PASS, C-18 PASS). These are independent
tests: the gate summary requirement goes beyond demonstrating re-examination to producing a
computable audit artifact. If C-18 is not met, C-20 fails automatically.

**C-21 vs C-18 and C-19:** C-18 requires a per-row exhaustiveness checklist. C-19 requires a
candidate-marking column in the threat class catalog table with exactly one Y. C-21 requires
the per-row exhaustiveness checklist to also carry a candidate-marking field (e.g., Adv? =
[Y/N]) for each row -- committing the adversarial selection during exhaustiveness re-examination,
not only during catalog construction. A response can have the catalog candidate column (C-19
PASS) and the per-row checklist (C-18 PASS) without the candidate field in the checklist (C-21
FAIL). The V-05 pattern dual-locks the commitment: the catalog establishes the forward pointer
at enumeration time (C-19); the checklist confirms it during re-examination (C-21). If C-18 is
not met or C-19 is not met, C-21 fails automatically.

---

### Why these two, not others

| Signal considered | Disposition |
|---|---|
| V-04/V-05 computable gate summary (row count + additions count) vs V-02 unstructured gate statement | C-20 -- structured count artifact is independently testable; bare gate statement already satisfies C-18 |
| V-05 per-row checklist candidate field (Adv?) coupling C-18 and C-19 in one structure | C-21 -- field presence in checklist rows is independently testable from catalog column (C-19) |
| V-05 labeled DISQUALIFIER (C-14, C-17) block naming five specific Parameters failure patterns | Not promoted -- rubric enforcement vocabulary, not a new response artifact signal |

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

## Aspirational Criteria (weight: 70 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Actionable remediation per failure point** | behavior | Every failure point from C-03 is paired with a concrete mitigation naming the mechanism type: retry policy, circuit breaker, permission scope addition, payload validation guard. DISQUALIFIER: "add error handling," "add retry logic" without a mechanism type. |
| C-09 | **Adversarial path comparison** | depth | At least one adversarial scenario (malformed payload, expired token, concurrent mutation, missing required field) shows how the path diverges from nominal -- naming the specific boundary Seq# where divergence occurs, the adversarial condition, the post-divergence path, and the concrete outcome. |
| C-10 | **Critical path named** | depth | The trace identifies the critical path: the specific Seq# chain whose cumulative latency determines worst-case response time. Parallel or cached paths are distinguished. Critical-path p50 and p99 estimated. Per-boundary rows are the source; totals are derived. A trace that lists sources but does not identify the critical sequence fails. |
| C-11 | **Authorization re-walk audit** | correctness | A dedicated second-pass authorization audit walks the full boundary list focused on privilege escalation paths, missing scope validations, and assumed-but-unverified auth. Must name at least one new gap or explicitly confirm per-boundary that the three highest-risk boundaries are clean. DISQUALIFIER: re-walk section that mirrors Step 4 auth fields without raising new questions. |
| C-12 | **Per-boundary latency budget table** | depth | The traversal carries a dedicated p50/p99 budget column for every boundary. Non-parallel segments sum to the critical-path total from C-10; parallel segments are not double-counted. SUM CLOSURE GATE: if per-boundary sums differ from critical-path total, the response must reconcile before proceeding. Prose latency annotation without a structured column fails. |
| C-13 | **Threat class catalog** | depth | A structured threat catalog table maps at least four distinct threat classes to the specific boundary Seq numbers where each manifests. At least five rows, four required. DISQUALIFIER: fewer than four threat classes; single-boundary row for a threat known to manifest at multiple boundaries. |
| C-14 | **Remediation parameters quantified** | depth | Every remediation item from C-08 includes quantified operational parameters: retry policies name algorithm, initial delay, multiplier, and max-attempts; circuit breakers name threshold and reset interval; permission fixes name the exact scope string or role identity; payload guards name the specific field and validation predicate. DISQUALIFIER: mechanism type named without operational parameters. |
| C-15 | **Multi-boundary threat exhaustiveness** | coverage | Every entry in the threat class catalog lists ALL applicable boundary Seq numbers -- not only the primary or highest-risk one. A threat class that manifests at boundaries 2, 5, and 7 must cite all three. DISQUALIFIER: single Seq# for a threat known to manifest at multiple boundaries; enumeration shortcuts ("multiple," "various"). If C-13 is not met, C-15 fails automatically. |
| C-16 | **Adversarial scenario catalog-grounded** | coverage | The adversarial path comparison (C-09) is explicitly grounded in the threat class catalog (C-13). A mandatory cross-reference block appears before the adversarial trace with four required fields: catalog row #, exact threat class name, all catalog Seq# for that row, and selected divergence Seq#. An ad-hoc adversarial scenario without cross-reference fails. If C-13 is not met, C-16 fails automatically. |
| C-17 | **Remediation register as dedicated structure** | depth | The remediation output is organized as a dedicated separate table -- a Remediation Register -- distinct from the primary boundary traversal table. The register includes at minimum three discrete columns: failure reference (boundary Seq# or row ID), mechanism type, and parameters. Remediation items embedded as inline annotations within the traversal table fail this criterion even when individually C-08- and C-14-compliant. The dedicated structure makes incomplete Parameters cells structurally visible as omissions. |
| C-18 | **Exhaustiveness confirmation precedes adversarial section** | depth | Before the adversarial scenario section begins, the response includes an explicit on-record confirmation that the threat class catalog exhaustiveness check was completed. The confirmation must demonstrate re-examination: it names rows checked, references the boundary inventory, or lists any Seq# values added. DISQUALIFIER: bare "confirmed" assertion without naming rows or referencing inventory; confirmation that appears after the adversarial section begins. If C-15 is not met, C-18 fails automatically. |
| C-19 | **Adversarial candidate pre-marked in threat catalog** | coverage | The threat class catalog includes a candidate-marking column with exactly one row marked Y and all other rows marked N, this marking present in the catalog table before the adversarial section begins. The adversarial scenario references the Y-marked row. DISQUALIFIER: no candidate column; candidate column with zero or multiple Y values; adversarial scenario referencing a row not pre-marked Y. If C-16 is not met, C-19 fails automatically. |
| C-20 | **Exhaustiveness gate includes computable summary** | depth | The exhaustiveness confirmation section includes a structured gate summary stating the exact number of catalog rows reviewed and the exact number of Seq# additions made -- in a computable format (e.g., "N rows reviewed against Step 3 inventory, X Seq# additions made"). A per-row checklist without a summary count fails. A summary that omits either count fails. A summary using approximate or hedged language ("all rows," "a few additions") fails. The counts must be integers derivable from the catalog and boundary inventory. If C-18 is not met, C-20 fails automatically. |
| C-21 | **Candidate marking committed at exhaustiveness gate** | coverage | Each row in the per-row exhaustiveness checklist carries a candidate-marking field (e.g., "Adv? = Y" or "Adv? = N"), filled before the adversarial section begins. The Adv? = Y checklist entry must correspond to the same catalog row as the catalog Y-marked candidate. This dual-locks the forward pointer: the threat catalog establishes the candidate during enumeration (C-19); the exhaustiveness checklist confirms it during re-examination (C-21). A checklist without a candidate field per row fails. A checklist with the field blank or filled after the adversarial section begins fails. If C-18 is not met or C-19 is not met, C-21 fails automatically. |

---

## Scoring Worksheet

| Tier | Criteria | Pts Each | Points Available | Points Earned |
|------|----------|----------|-----------------|---------------|
| Essential | C-01, C-02, C-03, C-04 | 15 | 60 | -- |
| Recommended | C-05, C-06, C-07 | 10 | 30 | -- |
| Aspirational | C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-21 | 5 | 70 | -- |
| **Total** | | | **160** | -- |

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
        +-- C-16 (catalog-grounded)
              +-- C-19 (candidate pre-marked in catalog)
                    +-- C-21 (candidate marking in gate checklist)*

C-08 (actionable remediation)
  +-- C-14 (parameters quantified)
        +-- C-17 (dedicated register structure)  [independent of C-13 chain]

C-10 (critical path)
  +-- C-12 (per-boundary budget, sums to C-10)

* C-21 has dual parents: C-18 (checklist structure exists) and C-19 (candidate column exists).
  Both must pass for C-21 to be eligible.
```

---

## Round History

| Round | Rubric | Scale | Top Score | Key addition |
|-------|--------|-------|-----------|--------------|
| R3 | v3 | 120 | -- | C-10, C-11, C-12, C-13 |
| R4 | v4 | 135 | 135/135 (V-01,02,04,05) | C-14, C-15, C-16 |
| R5 | v5 | 150 | -- | C-17, C-18, C-19 |
| R6 | v6 | 160 | -- | C-20, C-21 |
