I have everything I need. Three new signals in the scorecard evidence notes, all testable on the response artifact:

1. **Parameterized remediation** — C-08 evidence explicitly flags V-04 PARTIAL for producing "add retry logic" without "algorithm+values, threshold+interval, exact scope+identity." C-08 already requires "specific mechanism"; this is one level deeper — quantified operational parameters.

2. **Multi-boundary threat exhaustiveness** — C-13 evidence: V-01/V-02 PASS via explicit rule "a threat class that applies to three boundaries must list all three"; V-04 PARTIAL because "model may answer with the highest-risk boundary for most classes." C-13 requires mapping to boundaries where the class manifests but doesn't enforce ALL of them.

3. **Adversarial scenario catalog-grounded** — C-09 evidence: V-01/V-02/V-05 PASS because "adversarial scenario requires selection FROM Step 6 catalog (not independent choice)." C-09 requires an adversarial path; C-16 requires it be cross-referenced to the threat catalog.

---

```markdown
## `trace-request-rubric-v4-2026-03-14.md`

**Changes from v3:**

Three new aspirational criteria, expanding the tier from 6 → 9 criteria (30 → 45 pts). Total
scale 120 → 135. Golden threshold unchanged at >= 80.

---

### New Criteria

**C-14 — Remediation parameters quantified** (depth, 5 pts)

Extracted from V-01–V-03's remediation DISQUALIFIER pattern, which bans remediation items that
name a mechanism type without operational parameters ("add retry logic" fails; "exponential
backoff: initial=100ms, multiplier=2x, jitter=±20%, max-attempts=5" passes). C-08 requires a
specific mechanism — retry policy, circuit breaker, permission scope addition, payload validation
guard. C-14 requires that mechanism to be parameterized: retry policies include algorithm type and
values (initial delay, multiplier, max-attempts); circuit breakers include threshold and reset
interval; permission fixes include the exact scope string or role identity; payload guards include
the specific field name and validation predicate. V-04 earns C-08 PARTIAL precisely because
interrogative format without DISQUALIFIER enforcement allows "add retry logic" to pass — a
mechanism named but not parameterized. A remediation item that names the mechanism type without
quantified operational parameters fails.

**C-15 — Multi-boundary threat exhaustiveness** (coverage, 5 pts)

Extracted from V-01/V-02's Step 6 catalog enforcement rule: "a threat class that applies to three
boundaries must list all three." C-13 requires a structured threat catalog mapping at least four
distinct threat classes to the specific boundaries where each manifests. C-15 adds the
exhaustiveness requirement: each catalog entry must enumerate ALL applicable boundaries, not
merely the primary or highest-risk one. V-03 earns C-13 PARTIAL because without the pre-filled
template, models may produce catalogs that technically name multiple classes but list only one
boundary per class. V-04 earns C-13 PARTIAL because interrogative questions cause models to
answer with the highest-risk boundary rather than all applicable ones. A catalog entry that lists
one boundary for a threat class known to manifest at multiple boundaries fails.

**C-16 — Adversarial scenario catalog-grounded** (coverage, 5 pts)

Extracted from V-01/V-02/V-05's catalog-before-scenario ordering, explicitly called out in the
C-09 evidence: "catalog-before-scenario ordering is structurally enforced in V-01/V-02/V-05 —
Step 7 adversarial scenario requires selection FROM Step 6 catalog (not independent choice),
specific adversarial condition, divergence boundary by Seq#." C-09 requires an adversarial
scenario that shows divergence from the nominal path. C-16 requires that scenario to be
explicitly grounded in the threat class catalog (C-13): the trace must name the threat class from
the catalog and cite the boundary Seq# from the catalog entry where divergence occurs. An
adversarial scenario introduced ad-hoc — not cross-referenced to a catalog entry — fails. If no
catalog exists (C-13 fails), C-16 fails automatically.

---

### Why these three, not others

| Signal considered | Disposition |
|---|---|
| Algorithm+values in remediation DISQUALIFIER (V-01–V-03) | C-14 |
| All-applicable-boundaries rule per threat class (V-01/V-02 Step 6) | C-15 |
| Catalog-before-scenario selection ordering (V-01/V-02/V-05 Step 6→7) | C-16 |
| V-03 DISQUALIFIER register pattern | Variation design mechanism — constrains prompt, not response |
| V-04 interrogative format | Variation design mechanism — constrains prompt, not response |
| V-05 R1 boundary gate precondition | Already rejected in v3 — variation design |
| V-01/V-02 Step 5 closure gate (sum verification) | Already embedded in C-12: "collectively consistent with the critical-path total from C-10" |

---

### Why C-14, C-15, C-16 don't overlap with existing criteria

**C-14 vs C-08:** C-08 requires a named mechanism type ("retry policy"). C-14 requires that
mechanism to carry quantified operational parameters (algorithm, values, thresholds). "Exponential
backoff" satisfies C-08 but fails C-14; "exponential backoff: initial=100ms, multiplier=2x,
max-attempts=5" satisfies both.

**C-15 vs C-13:** C-13 requires a catalog mapping threat classes to "the specific boundaries
where each manifests." This is satisfied by listing one boundary per class. C-15 requires
exhaustive multi-boundary coverage — every applicable boundary listed, not just the
primary one. A catalog with four rows each citing one boundary passes C-13, fails C-15 if any
of those threats apply to additional boundaries.

**C-16 vs C-09 and C-13:** C-09 requires an adversarial scenario with a named divergence
boundary — the scenario may be freely chosen. C-13 requires a threat catalog — it says nothing
about the catalog being used as the source for the adversarial trace. C-16 closes the gap
between them: the adversarial scenario must be drawn from the catalog and cross-referenced by
threat class name and boundary Seq#.

---

### Scoring recap

| Tier | Criteria | Pts Each | Available |
|---|---|---|---|
| Essential | C-01–C-04 | 15 | 60 |
| Recommended | C-05–C-07 | 10 | 30 |
| Aspirational | C-08–C-16 | 5 | 45 |
| **Total** | | | **135** |

Golden: all 4 essential + composite >= 80.

---

## Essential Criteria (weight: 60 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Entry point declared** | coverage | The trace names the exact entry point: HTTP method, path, payload shape, and caller identity. Missing or vague entry point fails. |
| C-02 | **All service boundaries crossed** | coverage | Every distinct service boundary in the request path is enumerated in traversal order (e.g., gateway -> auth service -> domain API -> storage). Any boundary skipped -- including a well-known step like token validation -- fails. |
| C-03 | **Failure point at each boundary** | correctness | For every boundary listed in C-02, at least one concrete failure mode is identified (timeout, 4xx/5xx, auth rejection, payload mismatch, throttle, network partition). Generic "may fail" without a named mechanism fails. |
| C-04 | **Authorization gaps surfaced** | correctness | The trace explicitly identifies where authorization is checked (or not), names the permission/scope/role evaluated, and flags any boundary where authorization is absent or assumed. A trace that never mentions auth fails. |

---

## Recommended Criteria (weight: 30 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Latency sources identified** | depth | Each boundary or processing step contributing non-trivial latency is annotated (e.g., "synchronous Dataverse read -- p99 ~200ms", "token cache miss -- +40ms"). At least three distinct latency sources named. |
| C-06 | **Error path traced end-to-end** | coverage | At least one full error path is traced from origination point to caller response, showing how errors propagate, transform, or get swallowed across boundaries. A trace that covers only the happy path fails this criterion. |
| C-07 | **Batch and edge-case handling** | depth | Batch operations, pagination, or concurrent-request edge cases relevant to the request type are called out explicitly -- not just mentioned but analyzed (e.g., "batch of 1000 items: Dataverse 5000-record limit not hit, but per-request overhead multiplies"). |

---

## Aspirational Criteria (weight: 45 points)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Actionable remediation per failure point** | behavior | Every failure point from C-03 is paired with a concrete mitigation or design change (retry policy, circuit breaker, permission scope addition, payload validation guard). Generic "add error handling" fails; a specific mechanism passes. |
| C-09 | **Adversarial path comparison** | depth | Trace includes at least one adversarial scenario (malformed payload, expired token, concurrent mutation, missing required field) and shows how it diverges from the nominal path -- naming the specific boundary where divergence occurs and its outcome. |
| C-10 | **Critical path named** | depth | Beyond listing individual latency sources (C-05), the trace identifies the critical path: the specific sequence of boundaries whose cumulative latency determines worst-case response time. Parallel or cached paths are distinguished from the critical path. Total critical-path latency is estimated (p50 and p99). A trace that lists sources but does not name which sequence drives worst-case fails. |
| C-11 | **Authorization re-walk audit** | correctness | After the primary boundary traversal, the trace performs a dedicated second-pass authorization audit: walks the full boundary list from C-02 again, focused exclusively on privilege escalation paths, missing scope validations, and auth that is assumed but never verified. The audit must name at least one gap or escalation path not surfaced in the primary C-04 pass, or explicitly confirm that the re-walk found none. A trace that relies solely on per-boundary auth fields in the primary pass fails. |
| C-12 | **Per-boundary latency budget table** | depth | The traversal carries a dedicated p50/p99 budget column for every boundary -- not prose annotation but a structured column whose rows are individually sourced and collectively consistent with the critical-path total from C-10. Non-parallel segments sum to the total; parallel segments are not double-counted. A trace that annotates latency in prose or provides only a total estimate without per-boundary budget rows fails. |
| C-13 | **Threat class catalog** | depth | The trace includes a structured threat catalog: a table mapping at least four distinct threat classes (e.g., malformed input, credential expiry, concurrent mutation, missing permission scope, network partition) to the specific boundaries where each manifests. Threat classes must be enumerated systematically, not surfaced incidentally through one adversarial scenario. A trace that explores threats ad-hoc without a class-level catalog fails. |
| C-14 | **Remediation parameters quantified** | depth | Every remediation item from C-08 includes quantified operational parameters -- not just the mechanism type but its values: retry policies name algorithm, initial delay, multiplier, and max-attempts; circuit breakers name threshold and reset interval; permission fixes name the exact scope string or role identity; payload guards name the specific field and validation predicate. A remediation item that names the mechanism without operational parameters fails. |
| C-15 | **Multi-boundary threat exhaustiveness** | coverage | Every entry in the threat class catalog (C-13) lists ALL applicable boundary Seq numbers, not only the primary or highest-risk one. A threat class that manifests at boundaries 2, 5, and 7 must cite all three. A catalog entry that lists one boundary for a threat known to manifest at multiple boundaries fails. If C-13 is not met, C-15 fails automatically. |
| C-16 | **Adversarial scenario catalog-grounded** | coverage | The adversarial path comparison (C-09) is explicitly grounded in the threat class catalog (C-13): the trace names the threat class from the catalog and cites the boundary Seq# from the catalog entry where divergence occurs. An adversarial scenario introduced ad-hoc without cross-reference to a catalog entry fails. If C-13 is not met, C-16 fails automatically. |

---

## Scoring Worksheet

| Tier | Criteria | Pts Each | Points Available | Points Earned |
|------|----------|----------|-----------------|---------------|
| Essential | C-01, C-02, C-03, C-04 | 15 | 60 | -- |
| Recommended | C-05, C-06, C-07 | 10 | 30 | -- |
| Aspirational | C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16 | 5 | 45 | -- |
| **Total** | | | **135** | -- |

All criteria are binary: pass = full points, fail = 0.

**Golden**: all 4 essential pass AND composite >= 80.
```

---

**Extraction summary:**

| New criterion | Source signal in R3 scorecard |
|---|---|
| C-14 Remediation parameters quantified | C-08 evidence: V-04 PARTIAL — interrogative format produces "add retry logic" without "algorithm+values, threshold+interval" |
| C-15 Multi-boundary threat exhaustiveness | C-13 evidence: V-04 PARTIAL — "model may answer with the highest-risk boundary for most classes" rather than all applicable |
| C-16 Adversarial scenario catalog-grounded | C-09 evidence: V-01/V-02/V-05 PASS because "Step 7 requires selection FROM Step 6 catalog (not independent choice)" |

**One signal not promoted:** The Step 5 arithmetic closure gate (V-01/V-02 — if sums differ, return and correct) was considered for C-14, but it's already embedded in C-12's pass condition ("collectively consistent with the critical-path total from C-10"). No gap exists.

**Dependency chain introduced:** C-15 and C-16 both declare explicit failure if C-13 is not met, creating a two-node dependency on the catalog. This is intentional — both criteria measure precision properties of the catalog's content and use, not independent behaviors.
