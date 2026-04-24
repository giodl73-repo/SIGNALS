## `/quest:score` — `trace-request` Round 3

**Rubric version:** v3 (13 criteria, 120 pts max, golden ≥ 80 + all essential PASS)

---

## Criterion-by-Criterion Scoring

### Essential (15 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Entry point fully specified | PASS (15) | PASS (15) | PASS (15) | PASS (15) | PASS (15) |
| **C-02** Boundary inventory complete | PASS (15) | PASS (15) | PASS (15) | PASS (15) | PASS (15) |
| **C-03** Failure modes named with mechanism | PASS (15) | PASS (15) | PASS (15) | PASS (15) | PASS (15) |
| **C-04** Authorization gaps surfaced | PASS (15) | PASS (15) | PASS (15) | PASS (15) | PASS (15) |

**Evidence notes — Essential:**

- **C-01 (all):** V-01's DISQUALIFIER explicitly bans "a POST request" (no path), "a JSON body" (no field names), "an authenticated user" (no credential type). V-03's DISQUALIFIER register preserves this. V-04's interrogative questions force full specification. V-05 synthesizes all.
- **C-02 (all):** V-01's Step 3 GATE: "Step 4 rows must correspond to the boundaries listed here, in order. No boundary listed here may be absent from Step 4." All variations preserve this gate.
- **C-03 (all):** V-01's Step 4 Failure Mode DISQUALIFIER: "may fail," "could error," "an exception might be thrown" are explicitly banned. V-03's DISQUALIFIER register strengthens enforcement further.
- **C-04 (all):** V-01's Step 4 Auth? column with required "AUTH GAP — [reason]" for N rows; "standard auth," "valid token," "handled upstream" banned without naming upstream boundary.

---

### Recommended (10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-05** Latency sources identified | PASS (10) | PASS (10) | PASS (10) | PASS (10) | PASS (10) |
| **C-06** Error path traced end-to-end | PASS (10) | PASS (10) | PASS (10) | PASS (10) | PASS (10) |
| **C-07** Batch and edge-case handling | PASS (10) | PASS (10) | PASS (10) | PASS (10) | PASS (10) |

**Evidence notes — Recommended:**

- **C-05 (all):** V-01's Step 4 p50/p99 draw columns required per boundary; "fast," "low," blank explicitly banned. V-02 bakes budget columns into table schema. Preserved across all.
- **C-06 (all):** V-01's Step 7 adversarial scenario requires: selected threat class → divergence boundary → specific adversarial condition → "Trace artifact (ground truth)" full trace. The trace artifact section requires following the error path from divergence boundary through to caller response. All variations preserve the Step 7 adversarial trace structure.
- **C-07 (all):** R3 summary explicitly states "All R3 variations preserve the batch section from R2 V-05 to ensure C-07 is not regressed."

---

### Aspirational (5 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-08** Actionable remediation per failure point | PASS (5) | PASS (5) | PASS (5) | PARTIAL (2) | PASS (5) |
| **C-09** Adversarial path comparison | PASS (5) | PASS (5) | PASS (5) | PASS (5) | PASS (5) |
| **C-10** Critical path named | PASS (5) | PASS (5) | PASS (5) | PASS (5) | PASS (5) |
| **C-11** Authorization re-walk audit | PASS (5) | PASS (5) | PARTIAL (2) | PARTIAL (2) | PASS (5) |
| **C-12** Per-boundary latency budget table | PASS (5) | PASS (5) | PARTIAL (2) | PARTIAL (2) | PASS (5) |
| **C-13** Threat class catalog | PASS (5) | PASS (5) | PARTIAL (2) | PARTIAL (2) | PASS (5) |

**Evidence notes — Aspirational:**

**C-08:**
- V-01–V-03: Step 4 Remediation column DISQUALIFIER bans "add error handling," "improve resilience"; requires algorithm+values, threshold+interval, exact scope+identity. Structurally enforced.
- V-04 PARTIAL: Interrogative format asks about remediation but without the DISQUALIFIER text blocking generic answers, a model responding to questions is more likely to produce "add retry logic" without specifying algorithm or values.
- V-05: Full synthesis retains the DISQUALIFIER.

**C-09 (all):** V-01's Step 7 requires selection FROM Step 6 catalog (not independent choice), specific adversarial condition (not generic category), divergence boundary by Seq#. The catalog-before-scenario ordering is structurally enforced in V-01/V-02/V-05. V-03's DISQUALIFIER register and V-04's interrogative form preserve enough to ensure a specific adversarial path.

**C-10 (all):** V-01's Step 5 Part C requires: "Critical-path p50 = [= Part A p50 sum] ms; Critical-path p99 = [= Part A p99 sum] ms; Dominant boundary: [name — p99 draw — % of chain p99]." All variations preserve this structure.

**C-11:**
- V-01/V-02 PASS: Step 6 threat catalog includes "Credential expiry" and "Missing permission scope" as pre-filled rows mapped to ALL applicable boundary Seq numbers. This is a post-traversal structured re-examination of every boundary for auth-related threats — surfaces which boundaries are missing scope validation or assume valid credentials without checking. Functionally equivalent to a dedicated auth re-walk for the purposes of the criterion.
- V-03/V-04 PARTIAL: DISQUALIFIER text (V-03) or interrogative questions (V-04) do not structurally scaffold a post-traversal auth re-walk. The threat catalog template is absent or unenforced; auth re-examination depends on model initiative, not variation structure.
- V-05 PASS: Full R2 V-05 mechanisms include explicit auth re-walk step, plus V-03 inherits the structured threat catalog.

**C-12:**
- V-01 PASS: Step 5 CLOSURE GATE: "The sequential p50 sum in Part A and the critical-path p50 in Part C must be the same number. If they differ, return to Step 4 and correct." The per-boundary rows are the source of truth; the total is derived. This directly enforces arithmetic consistency as a lifecycle gate.
- V-02 PASS: Budget columns baked into table schema with inline arithmetic rules — sequential vs. parallel distinction is column-level, forcing non-double-counting structurally.
- V-03 PARTIAL: DISQUALIFIER names the three failure modes (p50 mismatch, p99 mismatch, parallel double-counting) but provides no gate that forces the model to verify the sum. A model may produce non-summing rows that don't trigger the DISQUALIFIER if each row looks individually plausible.
- V-04 PARTIAL: "Does your sequential chain sum equal your critical-path total?" is a question, not a gate. The model answers in one pass without being forced to return and correct Step 4.
- V-05 PASS: Retains closure gate from V-01 plus DISQUALIFIER from V-03.

**C-13:**
- V-01 PASS: Step 6 pre-populates five threat class rows with an "All Applicable Boundary Seq Numbers" column. Rule: "A threat class that applies to three boundaries must list all three." Minimum 4 rows required. Structured catalog with column-level multi-boundary enforcement.
- V-02 PASS: Pre-filled catalog template with "All Applicable Boundaries (Seq#)" column — same structural enforcement, different output format.
- V-03 PARTIAL: DISQUALIFIER bans single-boundary rows, but without a pre-filled template forcing the model to enumerate all threat classes, the model may produce a 2–3 row ad-hoc catalog that technically avoids single-boundary entries while missing systematic class coverage.
- V-04 PARTIAL: Questions ask "What boundaries does each threat class apply to?" but without template scaffolding, multi-boundary enumeration is inconsistent — the model may answer with the highest-risk boundary for most classes.
- V-05 PASS: Full synthesis inherits V-01's boundary-Seq catalog plus V-03's DISQUALIFIER.

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | All Essential? | Golden? |
|-----------|-----------|-------------|--------------|-----------|----------------|---------|
| V-01 | 60/60 | 30/30 | 30/30 | **120/120** | YES | YES |
| V-02 | 60/60 | 30/30 | 30/30 | **120/120** | YES | YES |
| V-03 | 60/60 | 30/30 | 21/30 | **111/120** | YES | YES |
| V-04 | 60/60 | 30/30 | 18/30 | **108/120** | YES | YES |
| V-05 | 60/60 | 30/30 | 30/30 | **120/120** | YES | YES |

**V-03 aspirational breakdown:** C-08(5) + C-09(5) + C-10(5) + C-11(2) + C-12(2) + C-13(2) = 21  
**V-04 aspirational breakdown:** C-08(2) + C-09(5) + C-10(5) + C-11(2) + C-12(2) + C-13(2) = 18

**Rank:** V-01 = V-02 = V-05 (120) > V-03 (111) > V-04 (108)

---

## Excellence Signals

Top variations (V-01, V-02, V-05) share three structural patterns not previously captured:

**1. Source-of-truth inversion for latency arithmetic**
Per-boundary budget rows are the *source of truth*; the critical-path total is *derived from them*. V-01's closure gate makes this explicit: "If they differ, return to Step 4 and correct." The inverse (top-down allocation from a total budget to boundary rows) produces internally consistent-looking tables that can fail C-12 on arithmetic. Naming the direction of derivation is what forces genuine additive consistency.

**2. Catalog-before-scenario sequencing**
V-01's Step 6 (threat catalog) precedes Step 7 (adversarial selection), and Step 7 explicitly requires selecting FROM the catalog. This sequencing prevents the common failure mode where the adversarial scenario is chosen for memorability (expired token, 404) rather than risk-ranked systematic coverage. The dependency arrow from catalog to scenario is a structural forcing function.

**3. Pre-filled threat class rows as enumeration scaffolding**
V-02/V-01's pre-populated catalog rows (malformed input, credential expiry, concurrent mutation, missing permission scope, network partition) shift the model's task from *generating a threat list* to *filling in applicable boundaries per class*. This is distinct from asking "what threats apply" — it removes the generation burden and directs attention to boundary coverage, which is what C-13 actually tests.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["source-of-truth inversion: per-boundary rows are authoritative inputs, critical-path total is derived output — prevents top-down allocation that appears consistent but violates per-boundary arithmetic", "catalog-before-scenario sequencing: building the full threat catalog before selecting the adversarial scenario creates a traceable dependency that forces comprehensive enumeration over memorable cherry-picking"]}
```
