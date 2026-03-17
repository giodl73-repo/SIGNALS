---
skill: quest-rubric
skill_target: trace-contract
date: 2026-03-15
version: 1
---

# Rubric: trace-contract

Compare expected vs. actual output using the three-directory pattern. The expected output
is the contract -- written from spec *before* execution. Any deviation is a finding.
Stock roles: Automate / Connectors contract expert.

---

## Scoring Formula

```
Composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential pass AND composite >= 80.

---

## Essential Criteria (60 pts total -- all must pass)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Contract-first order** -- the expected output is derived from the spec and written down *before* the actual operation is run, not reverse-engineered from actual output | essential | behavior | Output explicitly shows expected output section preceding actual output section; expected is annotated "from spec" or equivalent; no evidence that expected was written after-the-fact |
| C-02 | **Explicit diff** -- the difference between expected and actual is shown with enough precision that a reader can reproduce the comparison without re-running the operation | essential | correctness | Each deviation is stated as a concrete before/after or missing/extra field pair; vague statements like "output differs" do not pass |
| C-03 | **Severity classification per finding** -- every mismatch is labeled breaking, degraded, or cosmetic using the skill's defined taxonomy | essential | correctness | All findings carry exactly one severity label; unlabeled or free-form severity descriptions do not pass |
| C-04 | **Root cause hypothesis per finding** -- each mismatch includes a stated hypothesis for *why* the deviation occurred (not merely that it occurred) | essential | depth | Every finding has a distinct root cause sentence; "unknown" alone does not pass -- at minimum a plausible hypothesis must be offered |
| C-05 | **Spec reference per finding** -- each mismatch cites the specific spec section, field, or contract clause that the deviation violates | essential | coverage | Every finding includes a spec reference (section name, field name, or clause number); findings without a reference do not pass |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **Automate / Connectors lens** -- the Automate or Connectors contract expert stock role perspective is applied: findings distinguish schema-level contract violations (breaking for integrations) from runtime behavior deviations | recommended | depth | At least one finding explicitly calls out integration-level impact (e.g., "this field rename breaks Automate connector mappings") or the absence of findings is confirmed from that lens |
| C-07 | **Summary verdict** -- the output ends with an aggregate verdict: total finding count broken down by severity (breaking / degraded / cosmetic) and an overall pass/fail against the contract | recommended | format | A summary section exists with counts per severity and a clear PASS or FAIL conclusion; partial counts without a verdict do not pass |
| C-08 | **Clean confirmation when no findings** -- if expected matches actual, the output explicitly states contract honored rather than returning empty content | recommended | behavior | Zero-finding runs produce an affirmative statement ("Contract honored -- no deviations found") rather than silence or a blank section |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Amendment suggestion for breaking findings** -- for any finding classified breaking, the output proposes either a spec amendment (update the contract) or an implementation fix (update the code), with a rationale for which path is recommended | aspirational | depth | Every breaking finding includes a concrete "Recommended action" line that distinguishes spec-side vs. implementation-side resolution |
| C-10 | **Pattern recognition across findings** -- when two or more findings share a root cause, this is called out explicitly as a pattern, reducing the perceived finding count and pointing to a single fix | aspirational | coverage | Output contains a "Patterns" section or inline notes grouping related findings; applies only when N findings >= 2 |

---

## Scoring Examples

| Scenario | Essential | Recommended | Aspirational | Composite | Golden? |
|----------|-----------|-------------|--------------|-----------|---------|
| All pass | 5/5 | 3/3 | 2/2 | 100 | yes |
| Missing spec refs | 4/5 | 3/3 | 1/2 | 83 | no (C-05 fails) |
| No root causes | 4/5 | 2/3 | 0/2 | 68 | no |
| Essential only | 5/5 | 0/3 | 0/2 | 60 | no (< 80) |
| Essential + all recommended | 5/5 | 3/3 | 0/2 | 90 | yes |
