Reading the scorecard carefully, three new patterns appear — each a synthesis of two existing criteria that neither one alone captures:

- **V-01**: `[EXPECTED SEALED]` machine-parseable token — not just an acknowledgment (C-12) but a structured marker that enables mechanical verification → **C-13**
- **V-02**: mandatory `connector-impact` slot on every finding — not just at-least-one callout (C-06) and not just structural enforcement in general (C-11), but their intersection → **C-14**
- **V-03**: `recommended-action` as a required slot in the breaking-finding template — not just amendment content (C-09) but structural enforcement of that content → **C-15**

Seven aspirational criteria share the 10-point pool (~1.4 pts each).

---

```markdown
# Rubric: trace-contract v3

Evaluates the quality of a `trace:contract` skill execution.
A **golden** output scores ≥ 80 and passes all essential criteria.

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 – C-05 | 12 pts each = 60 pts |
| Recommended | C-06 – C-08 | 10 pts each = 30 pts |
| Aspirational | C-09 – C-15 | 10 pts total (~1.4 pts each) |
| **Max composite** | | **100** |

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Expected before actual** — the expected output section is written and finalized before the operation is executed, establishing a pre-run record | essential | integrity | Expected section appears in the document before the actual output section; annotated "from spec" or equivalent; no evidence that expected was written after-the-fact |
| C-02 | **Explicit diff** — the difference between expected and actual is shown with enough precision that a reader can reproduce the comparison without re-running the operation | essential | correctness | Each deviation is stated as a concrete before/after or missing/extra field pair; vague statements like "output differs" do not pass |
| C-03 | **Severity classification per finding** — every mismatch is labeled breaking, degraded, or cosmetic using the skill's defined taxonomy | essential | correctness | All findings carry exactly one severity label; unlabeled or free-form severity descriptions do not pass |
| C-04 | **Root cause hypothesis per finding** — each mismatch includes a stated hypothesis for *why* the deviation occurred (not merely that it occurred) | essential | depth | Every finding has a distinct root cause sentence; "unknown" alone does not pass — at minimum a plausible hypothesis must be offered |
| C-05 | **Spec reference per finding** — each mismatch cites the specific spec section, field, or contract clause that the deviation violates | essential | coverage | Every finding includes a spec reference (section name, field name, or clause number); findings without a reference do not pass |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **Automate / Connectors lens** — the Automate or Connectors contract expert stock role perspective is applied: findings distinguish schema-level contract violations (breaking for integrations) from runtime behavior deviations | recommended | depth | At least one finding explicitly calls out integration-level impact (e.g., "this field rename breaks Automate connector mappings") or the absence of findings is confirmed from that lens |
| C-07 | **Summary verdict** — the output ends with an aggregate verdict: total finding count broken down by severity (breaking / degraded / cosmetic) and an overall pass/fail against the contract | recommended | format | A summary section exists with counts per severity and a clear PASS or FAIL conclusion; partial counts without a verdict do not pass |
| C-08 | **Clean confirmation when no findings** — if expected matches actual, the output explicitly states contract honored rather than returning empty content | recommended | behavior | Zero-finding runs produce an affirmative statement ("Contract honored — no deviations found") rather than silence or a blank section |

---

## Aspirational Criteria (10 pts total)

Seven criteria share the 10-point pool (~1.4 pts each).

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Amendment suggestion for breaking findings** — for any finding classified breaking, the output proposes either a spec amendment (update the contract) or an implementation fix (update the code), with a rationale for which path is recommended | depth | Every breaking finding includes a concrete "Recommended action" line that distinguishes spec-side vs. implementation-side resolution |
| C-10 | **Pattern recognition across findings** — when two or more findings share a root cause, this is called out explicitly as a pattern, reducing the perceived finding count and pointing to a single fix | coverage | Output contains a "Patterns" section or inline notes grouping related findings; applies only when N findings ≥ 2 |
| C-11 | **Structural field enforcement** — findings are presented in a tabular or templated block format so that any missing required field (severity, root cause, spec ref) is visually self-announcing at write time, before any review step | format | Output uses a table or per-finding block with labeled fields; absence of a field value produces a visible gap rather than silent omission |
| C-12 | **Phase-gate confirmation** — the workflow enforces an explicit "do not proceed" checkpoint between expected-writing and execution, with a gate question or lock statement that prevents contaminating the expected record with observed output | behavior | Output contains an explicit acknowledgment that expected was sealed before execution began (e.g., gate check question answered, "document locked" statement, or equivalent); sequencing alone without an explicit gate does not pass |
| C-13 | **Machine-readable gate token** *(new)* — the phase-gate uses a structured, parseable marker (e.g., `[EXPECTED SEALED]`) embedded at the exact gate point in the document, enabling automated or mechanical verification of the sequencing invariant | behavior | A distinct structured token appears in the document immediately after expected is written and before execution output begins; prose statements that expected was sealed before execution (which satisfy C-12) do not satisfy C-13 without the token |
| C-14 | **Per-finding integration coverage** *(new)* — every finding block includes an explicitly labeled `connector-impact` (or equivalent) slot, making integration-lens coverage structurally mandatory across all findings rather than relying on an at-least-one callout | depth | All finding blocks carry a labeled integration-impact field; at-least-one callout (which satisfies C-06) without per-finding structural enforcement does not pass; applies only when N findings ≥ 1 |
| C-15 | **Amendment enforcement by template structure** *(new)* — the breaking-finding template includes `recommended-action` as a required labeled slot (fifth field or equivalent), so a breaking finding block cannot be recorded as complete without addressing resolution path at write time | depth | Breaking findings use a template with an explicit `recommended-action` (or equivalent) slot; inclusion of amendment text in prose outside a structured slot (which satisfies C-09) does not satisfy C-15; applies only when N breaking findings ≥ 1 |

---

## Scoring Examples

| Scenario | Essential | Recommended | Aspirational | Composite | Golden? |
|----------|-----------|-------------|--------------|-----------|---------|
| All pass | 5/5 | 3/3 | 7/7 | 100 | yes |
| Essential + all recommended + 4 aspirational | 5/5 | 3/3 | 4/7 | 95.7 | yes |
| R2 single aspirational (V-01, V-02, or V-03 under v3) | 5/5 | 3/3 | 1/7 | 91.4 | yes |
| R1 top score (0/7 aspirational) | 5/5 | 3/3 | 0/7 | 90 | yes |
| Missing spec refs | 4/5 | 3/3 | 2/7 | 82.9 | no (C-05 fails) |
| No root causes | 4/5 | 2/3 | 0/7 | 68 | no |
| Essential only | 5/5 | 0/3 | 0/7 | 60 | no (< 80) |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial rubric — 5 essential, 3 recommended, 2 aspirational (C-09, C-10) |
| v2 | 2026-03-15 | Added C-11 (structural field enforcement) and C-12 (phase-gate confirmation) from R1 excellence signals; aspirational pool 4 criteria × 2.5 pts |
| v3 | 2026-03-15 | Added C-13 (machine-readable gate token), C-14 (per-finding integration coverage), C-15 (amendment enforcement by template structure) from R2 excellence signals; aspirational pool 7 criteria × ~1.4 pts |
```

---

**What changed and why:**

| New criterion | Source variant | Synthesis it captures |
|--------------|----------------|-----------------------|
| C-13 | V-01 | C-12 × traceability — token makes the gate claim mechanical, not just stated |
| C-14 | V-02 | C-06 × C-11 — per-finding integration slot enforces coverage structurally, not statistically |
| C-15 | V-03 | C-09 × C-11 — amendment slot in the breaking template makes omission visually self-announcing at write time |

R1 top variants still score 90 (0/7 aspirational). V-01/V-02/V-03 score 91.4 under v3 (vs. 92.5 under v2, because the pool now distributes across 7 criteria). A variant hitting C-11 + C-14 + C-15 simultaneously — all three structural-enforcement criteria — would reach ~94.3.
