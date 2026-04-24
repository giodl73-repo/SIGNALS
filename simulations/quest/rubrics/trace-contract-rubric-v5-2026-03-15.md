Reading the scorecard, one synthesis pattern emerges from R4 — resolving a structural tension that C-18 addressed only partially:

- **V-R4-A**: Preamble-first behavioral protocol — not just specifying the full token contract (placement, anti-paraphrase, verification — C-18), but isolating that contract as a named section *before Phase 1 begins*, so the model encounters all behavioral rules before any phase instruction; inline or mid-prompt embedding does not satisfy this → **C-19**

```markdown
# Rubric: trace-contract v5

Evaluates the quality of a `trace:contract` skill execution.
A **golden** output scores ≥ 80 and passes all essential criteria.

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 – C-05 | 12 pts each = 60 pts |
| Recommended | C-06 – C-08 | 10 pts each = 30 pts |
| Aspirational | C-09 – C-19 | 11 pts total (1.0 pt each) |
| **Max composite** | | **101** |

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

## Aspirational Criteria (11 pts total)

Eleven criteria share the 11-point pool (1.0 pt each).

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Amendment suggestion for breaking findings** — for any finding classified breaking, the output proposes either a spec amendment (update the contract) or an implementation fix (update the code), with a rationale for which path is recommended | depth | Every breaking finding includes a concrete "Recommended action" line that distinguishes spec-side vs. implementation-side resolution |
| C-10 | **Pattern recognition across findings** — when two or more findings share a root cause, this is called out explicitly as a pattern, reducing the perceived finding count and pointing to a single fix | coverage | Output contains a "Patterns" section or inline notes grouping related findings; applies only when N findings ≥ 2 |
| C-11 | **Structural field enforcement** — findings are presented in a tabular or templated block format so that any missing required field (severity, root cause, spec ref) is visually self-announcing at write time, before any review step | format | Output uses a table or per-finding block with labeled fields; absence of a field value produces a visible gap rather than silent omission |
| C-12 | **Phase-gate confirmation** — the workflow enforces an explicit "do not proceed" checkpoint between expected-writing and execution, with a gate question or lock statement that prevents contaminating the expected record with observed output | behavior | Output contains an explicit acknowledgment that expected was sealed before execution began (e.g., gate check question answered, "document locked" statement, or equivalent); sequencing alone without an explicit gate does not pass |
| C-13 | **Machine-readable gate token** — the phase-gate uses a structured, parseable marker (e.g., `[EXPECTED SEALED]`) embedded at the exact gate point in the document, enabling automated or mechanical verification of the sequencing invariant | behavior | A distinct structured token appears in the document immediately after expected is written and before execution output begins; prose statements that expected was sealed before execution (which satisfy C-12) do not satisfy C-13 without the token |
| C-14 | **Per-finding integration coverage** — every finding block includes an explicitly labeled `connector-impact` (or equivalent) slot, making integration-lens coverage structurally mandatory across all findings rather than relying on an at-least-one callout | depth | All finding blocks carry a labeled integration-impact field; at-least-one callout (which satisfies C-06) without per-finding structural enforcement does not pass; applies only when N findings ≥ 1 |
| C-15 | **Amendment enforcement by template structure** — the breaking-finding template includes `recommended-action` as a required labeled slot (fifth field or equivalent), so a breaking finding block cannot be recorded as complete without addressing resolution path at write time | depth | Breaking findings use a template with an explicit `recommended-action` (or equivalent) slot; inclusion of amendment text in prose outside a structured slot (which satisfies C-09) does not satisfy C-15; applies only when N breaking findings ≥ 1 |
| C-16 | **Severity-stratified template architecture** *(R3)* — the finding templates are differentiated by severity tier: one template per level (breaking / degraded / cosmetic), each encoding only the fields structurally appropriate to that tier, eliminating conditional field requirements within a unified template | format | Three distinct template blocks exist, one per severity tier; required fields within each template are unconditionally mandatory for that tier with no conditional ("required if breaking") language; a single unified template with conditional fields (which may satisfy C-11 and C-15) does not satisfy C-16; applies only when N findings ≥ 1 |
| C-17 | **Rationale-anchored resolution path** *(R3)* — the `recommended-action` slot includes not only a vocabulary-constrained choice (amend-spec / fix-impl / needs-discussion) but a one-sentence rationale identifying which side of the contract is wrong and why, grounding the resolution direction in the root cause analysis | depth | Every breaking finding's resolution slot carries both a vocabulary choice and a distinct rationale sentence; a vocabulary choice alone (which satisfies C-09 and C-15) does not satisfy C-17; applies only when N breaking findings ≥ 1 |
| C-18 | **Token contract specification** *(R3)* — beyond embedding a machine-parseable gate token (C-13), the output specifies the full behavioral contract of that token: its exact placement rule (e.g., own line, immediately after last expected-output entry), an explicit anti-paraphrase constraint (no equivalent phrasing substitutable for the token), and a description of how the token enables automated verification | behavior | The gate token section or preamble states all three properties — placement, non-substitutability, and verification mechanism; presence of the token alone (which satisfies C-13) does not satisfy C-18 |
| C-19 | **Preamble-first behavioral protocol** *(R4)* — the behavioral contract for the gate token (and any other cross-phase rules) is isolated as a named section at the top of the prompt, before Phase 1 begins, so the model encounters all behavioral rules in sequence before any phase instruction; mid-prompt, inline, or appended placement does not satisfy this criterion | behavior | A named preamble section exists before Phase 1 containing the token contract and cross-phase behavioral rules; content that satisfies C-18 for completeness but appears inside a phase block or after Phase 1 begins does not satisfy C-19 |

---

## Scoring Examples

| Scenario | Essential | Recommended | Aspirational | Composite | Golden? |
|----------|-----------|-------------|--------------|-----------|---------|
| All pass | 5/5 | 3/3 | 11/11 | 101 | yes |
| Essential + all recommended + 9 aspirational | 5/5 | 3/3 | 9/11 | 99 | yes |
| R4 top score (V-02: C-18 + C-19, avoids C-04 gap) | 5/5 | 3/3 | 8/11 | 98 | yes |
| R3 top score (C-16 + C-17 + C-18, no C-10 or C-19) | 5/5 | 3/3 | 6/11 | 96 | yes |
| R2 single aspirational (C-13, C-14, or C-15) | 5/5 | 3/3 | 1/11 | 91 | yes |
| R1 top score (0/11 aspirational) | 5/5 | 3/3 | 0/11 | 90 | yes |
| Missing spec refs (C-05 fails) | 4/5 | 3/3 | 2/11 | 80 | no (C-05 fails) |
```

---

**What changed v4 → v5:**

- **C-19 added** — preamble-first behavioral protocol: the distinction from C-18 is *position*, not *content*. C-18 requires the three token contract properties to be stated somewhere; C-19 requires them to appear *before Phase 1*, so behavioral rules precede phase instructions entirely. V-01 had placement (own line) but failed C-18; V-02 passed C-18 and C-19 by leading with a named protocol block.
- **Aspirational pool** updated from 10 pts (C-09–C-18) to 11 pts (C-09–C-19), max composite 101.
- **Scoring examples** updated: R4 top score row added (98), prior rows revised to reflect 11-pt aspirational denominator.
