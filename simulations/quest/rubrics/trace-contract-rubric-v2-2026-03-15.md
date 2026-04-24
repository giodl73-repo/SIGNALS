Done. Here's the v2 rubric summary:

---

**Rubric: trace-contract v2**

**5 essential** (C-01 through C-05): unchanged

**3 recommended** (C-06 through C-08): unchanged

**4 aspirational** (C-09 through C-12) — 2.5 pts each:
- **C-09** Amendment suggestion *(carried from v1)*
- **C-10** Pattern recognition *(carried from v1)*
- **C-11 Structural field enforcement** *(new)* — tabular/templated format makes missing fields visually self-announcing at write time; empty cells announce themselves before any review step
- **C-12 Phase-gate confirmation** *(new)* — explicit "do not proceed" checkpoint between expected-writing and execution; sequencing alone without a gate statement does not pass

**What changed in scoring:** The aspirational pool stays at 10 pts but now distributes across 4 criteria (2.5 each vs. 5 each). R1's top variants (V-01, V-02, V-03) still score 90 — they hit 0/4 aspirational. But the new criteria now give golden prompts a clear path toward 95 or 100 in Round 2.
put section preceding actual output section; expected is annotated "from spec" or equivalent; no evidence that expected was written after-the-fact |
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

Four criteria share the 10-point pool (2.5 pts each).

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | **Amendment suggestion for breaking findings** -- for any finding classified breaking, the output proposes either a spec amendment (update the contract) or an implementation fix (update the code), with a rationale for which path is recommended | aspirational | depth | Every breaking finding includes a concrete "Recommended action" line that distinguishes spec-side vs. implementation-side resolution |
| C-10 | **Pattern recognition across findings** -- when two or more findings share a root cause, this is called out explicitly as a pattern, reducing the perceived finding count and pointing to a single fix | aspirational | coverage | Output contains a "Patterns" section or inline notes grouping related findings; applies only when N findings >= 2 |
| C-11 | **Structural field enforcement** -- findings are presented in a tabular or templated form format so that any missing required field (severity, root cause, spec ref) is visually self-announcing at write time, before any review step | aspirational | format | Output uses a table or per-finding block with labeled fields; absence of a field value produces a visible gap rather than silent omission |
| C-12 | **Phase-gate confirmation** -- the workflow enforces an explicit "do not proceed" checkpoint between expected-writing and execution, with a gate question or lock statement that prevents contaminating the expected record with observed output | aspirational | behavior | Output contains an explicit acknowledgment that expected was sealed before execution began (e.g., gate check question answered, "document locked" statement, or equivalent); sequencing alone without an explicit gate does not pass |

---

## Scoring Examples

| Scenario | Essential | Recommended | Aspirational | Composite | Golden? |
|----------|-----------|-------------|--------------|-----------|---------|
| All pass | 5/5 | 3/3 | 4/4 | 100 | yes |
| Missing spec refs | 4/5 | 3/3 | 2/4 | 83 | no (C-05 fails) |
| No root causes | 4/5 | 2/3 | 0/4 | 68 | no |
| Essential only | 5/5 | 0/3 | 0/4 | 60 | no (< 80) |
| Essential + all recommended | 5/5 | 3/3 | 0/4 | 90 | yes |
| R1 top score (V-01, V-02, V-03) | 5/5 | 3/3 | 0/4 | 90 | yes |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational (C-09, C-10) |
| v2 | 2026-03-15 | Added C-11 (structural field enforcement) and C-12 (phase-gate confirmation) from R1 excellence signals; aspirational pool now 4 criteria, 2.5 pts each |
