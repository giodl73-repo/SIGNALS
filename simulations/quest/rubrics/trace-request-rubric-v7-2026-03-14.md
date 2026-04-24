`trace-request-rubric-v7-2026-03-14.md` written. Here is the extraction summary:

---

**Two new criteria from R7 excellence signals:**

| New criterion | R7 excellence signal | What is testable on the response |
|---|---|---|
| **C-22** Batch-catalog cross-check gate computable summary | ES-1 (V-04/V-05): three-integer gate `N edge cases x M catalog rows -> K interactions found` before the register | Are all three integers present, non-approximate, placed after the batch section and before the register, with per-case entries citing catalog row numbers? |
| **C-23** Adversarial and error traces cite Rem# entries at divergence boundary | ES-2 (V-05): Steps 7 and 9 each cite applicable Rem# from the Register inline at the failure boundary | Does each of the adversarial trace and the error path trace include an inline Rem# citation at the exact divergence or origination boundary? |

**Scale:** 160 -> **170** (aspirational tier: 14 -> 16 criteria, 70 -> 80 pts). Golden threshold stays at >= 80.

---

**Signal not promoted:** ES-3 vocabulary coherence -- Step 0 binding propagates platform-specific terminology through C-03/C-04/C-14 fields. Requires cross-step token comparison, not binary field presence. Not yet a computable criterion.

---

**Why these don't overlap:**

- **C-22 vs C-07 and C-13:** C-07 requires batch entries with limits and consequences. C-13 requires a threat catalog. C-22 requires a blocking three-integer gate cross-checking those two structures before the register begins. C-07 PASS + C-13 PASS with no gate = C-22 FAIL.
- **C-23 vs C-08/C-17/C-09/C-06:** C-08/C-14/C-17 verify the Register is structurally complete. C-09 and C-06 verify the adversarial and error traces exist. C-23 requires those traces to reference the Register inline at the point of failure -- not in a trailing summary. A complete Register + complete traces with no cross-link = C-23 FAIL.

**Dependency additions:**
- C-22 depends on both C-07 (batch section exists) and C-13 (catalog exists); both parents required
- C-23 depends on C-08 (Register exists), C-09 (adversarial trace exists), and C-06 (error trace exists); all three required
- [reason]." |

---

## Recommended Criteria (weight: 30 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Latency sources identified** | depth | Each boundary or processing step contributing non-trivial latency is annotated with p50/p99 estimate. At least three distinct latency sources named. DISQUALIFIER: "fast," "low," or blank. Sub-5ms entries annotated as "< 5ms -- [reason]." |
| C-06 | **Error path traced end-to-end** | coverage | At least one full error path traced from origination point to caller response, showing how errors propagate, transform, or get swallowed across boundaries. DISQUALIFIER: "error returned to caller" without the propagation chain. |
| C-07 | **Batch and edge-case handling** | depth | Batch operations, pagination, or concurrent-request edge cases are called out and analyzed -- not just mentioned. Each entry names the specific limit, the boundary where it applies, and the behavioral consequence of hitting it. |

---

## Aspirational Criteria (weight: 80 points)

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
| C-22 | **Batch-catalog cross-check gate computable summary** | depth | Before the remediation register section begins, the response includes a three-integer cross-check gate summarizing the batch/edge-case analysis against the threat catalog: "N edge cases x M catalog rows -> K interactions found." All three integers must be present and non-approximate. The gate must appear after the batch section (C-07) and before the register section, and per-case entries within the batch section must cite actual catalog row numbers from C-13. A prose assertion ("all edge cases checked") without the three-integer format fails. A gate present but missing any one integer fails. If C-07 is not met or C-13 is not met, C-22 fails automatically. |
| C-23 | **Adversarial and error traces cite Rem# entries at divergence boundary** | coverage | The adversarial path section (C-09) and the error path section (C-06) each include an explicit back-reference to the applicable Remediation Register entry (Rem# or row ID) at the exact boundary where divergence or error origination occurs. A Register that is structurally complete (C-08, C-14, C-17) but never referenced from within the adversarial or error path trace fails this criterion. The citation must name the specific Rem# and appear inline at the divergence or origination boundary -- not as a trailing summary appended after the trace. A response may have a complete Register and complete adversarial and error traces and still fail C-23 if the two structures are not cross-linked at the point of failure. If C-08 is not met, C-09 is not met, or C-06 is not met, C-23 fails automatically. |

---

## Scoring Worksheet

| Tier | Criteria | Pts Each | Points Available | Points Earned |
|------|----------|----------|-----------------|---------------|
| Essential | C-01, C-02, C-03, C-04 | 15 | 60 | -- |
| Recommended | C-05, C-06, C-07 | 10 | 30 | -- |
| Aspirational | C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-23 | 5 | 80 | -- |
| **Total** | | | **170** | -- |

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

C-07 (batch/edge-case handling)
  +-- C-22 (batch-catalog cross-check gate)**

C-08 (actionable remediation)
  +-- C-14 (parameters quantified)
  |     +-- C-17 (dedicated register structure)
  +-- C-23 (Rem# citation at divergence/origination boundary)***

C-09 (adversarial path)
  +-- C-23 (Rem# citation at divergence boundary)***

C-06 (error path)
  +-- C-23 (Rem# citation at error origination boundary)***

C-10 (critical path)
  +-- C-12 (per-boundary budget, sums to C-10)

* C-21 has dual parents: C-18 (checklist structure exists) and C-19 (candidate column
  exists). Both must pass for C-21 to be eligible.

** C-22 has dual parents: C-07 (batch section exists with per-case entries) and C-13
   (catalog exists with row numbers to cite). Both must pass for C-22 to be eligible.

*** C-23 has three parents: C-08 (Register exists), C-09 (adversarial trace exists),
    and C-06 (error trace exists). All three must pass for C-23 to be eligible.
```

---

## Why C-22 and C-23 are independent

**C-22 vs C-07 and C-13:** C-07 requires batch/edge-case entries naming limits and
behavioral consequences. C-13 requires a threat catalog with Seq# citations. C-22 requires
a blocking gate between those two structures and the remediation register, expressed as
three integers: edge-case count, catalog row count, interaction count. A response can have
a complete batch section (C-07 PASS) and a complete threat catalog (C-13 PASS) without
cross-referencing them in a computable gate before the register (C-22 FAIL). The
three-integer gate is independently testable: absence of any one integer is a binary fail.

**C-23 vs C-08, C-17, C-09, C-06:** C-08/C-14/C-17 verify the Remediation Register exists
and is structurally complete. C-09 verifies an adversarial scenario exists. C-06 verifies
an error path exists. C-23 verifies that the adversarial and error path traces close the
loop back to the Register at the exact point of failure -- an inline cross-link, not a
trailing summary. A response can have a complete Register and a complete adversarial trace
and pass C-08 through C-21 while failing C-23 if the two structures are never cross-linked
at the divergence or origination boundary.

---

## Signal not promoted from R7

| Signal considered | Disposition |
|---|---|
| ES-3: vocabulary coherence -- Step 0 binding propagates platform-specific terminology through C-03/C-04/C-14 fields | Not promoted -- requires cross-step token comparison, not binary field presence; not yet a computable criterion |

---

## Round History

| Round | Rubric | Scale | Top Score | Key addition |
|-------|--------|-------|-----------|--------------|
| R3 | v3 | 120 | -- | C-10, C-11, C-12, C-13 |
| R4 | v4 | 135 | 135/135 (V-01,02,04,05) | C-14, C-15, C-16 |
| R5 | v5 | 150 | -- | C-17, C-18, C-19 |
| R6 | v6 | 160 | -- | C-20, C-21 |
| R7 | v7 | 170 | 160/160 (V-02,03,04,05) | C-22, C-23 |
