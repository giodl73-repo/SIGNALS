Here is the complete updated rubric as Markdown:

---

# Rubric: trace-contract v7

Reading the scorecard, one synthesis pattern emerges from R6:

- **V-R6-A**: Full artifact skeleton as master structural guarantor — V-03 tests presenting the complete artifact skeleton (all section headers and template slots in final position) before Phase 1 begins. C-19 requires behavioral rules to precede Phase 1; it does not require the artifact's structural layout to be pre-committed. C-20 requires the `## Patterns` block in the summary template embedded within Phase 5; it does not require all other sections to be pre-declared. The skeleton-first approach is the next escalation in the structural-enforcement ladder (C-11 → C-16 → C-19 → C-20 → **C-22**): every section header is unconditionally present before any content is written, making the skeleton the simultaneous commitment device, structural completeness enforcer, and phase-separation guarantor → **C-22**

---

Evaluates the quality of a `trace:contract` skill execution.
A **golden** output scores ≥ 80 and passes all essential criteria.

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 – C-05 | 12 pts each = 60 pts |
| Recommended | C-06 – C-08 | 10 pts each = 30 pts |
| Aspirational | C-09 – C-22 | 14 pts total (1.0 pt each) |
| **Max composite** | | **104** |

---

## Essential Criteria (60 pts total)

*(C-01 through C-05 unchanged from v6)*

---

## Aspirational Criteria (14 pts total)

Fourteen criteria share the 14-point pool (1.0 pt each).

*(C-09 through C-21 unchanged from v6)*

**C-22** is the only new criterion:

| C-22 | **Full artifact skeleton before Phase 1** *(R6)* — the complete artifact skeleton (all section headers and template slots in final position) is presented as a named structural declaration before Phase 1 begins, making every section unconditionally visible from the start; the skeleton functions simultaneously as a document-shape commitment device, a structural completeness enforcer for all sections (including Patterns), and a phase-separation guarantor | format | A complete artifact skeleton section appears before Phase 1, containing all section headers and template slots in their final positions; a named preamble behavioral protocol (C-19) placed before Phase 1 without a structural skeleton does not satisfy C-22; a pre-printed Patterns slot embedded within a Phase 5 summary template (C-20) without a top-level skeleton declaration does not satisfy C-22; instructional text directing the model to produce specific sections (C-11) without a pre-printed skeleton does not satisfy C-22 |

---

**Key changes from v6 → v7:**
- Aspirational pool: 13 → 14 pts (C-22 added)
- Max composite: 103 → 104
- R6 top scores land at **101** (tied: V-02 with C-21 PASS, and V-03 with C-20 + C-22 PASS, each failing two other criteria)
- V-01 (pre-printed Patterns, unified template) scores **100** — adds C-22 FAIL to its existing C-15/C-16 fails
r clause number); findings without a reference do not pass |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **Automate / Connectors lens** — the Automate or Connectors contract expert stock role perspective is applied: findings distinguish schema-level contract violations (breaking for integrations) from runtime behavior deviations | recommended | depth | At least one finding explicitly calls out integration-level impact (e.g., "this field rename breaks Automate connector mappings") or the absence of findings is confirmed from that lens |
| C-07 | **Summary verdict** — the output ends with an aggregate verdict: total finding count broken down by severity (breaking / degraded / cosmetic) and an overall pass/fail against the contract | recommended | format | A summary section exists with counts per severity and a clear PASS or FAIL conclusion; partial counts without a verdict do not pass |
| C-08 | **Clean confirmation when no findings** — if expected matches actual, the output explicitly states contract honored rather than returning empty content | recommended | behavior | Zero-finding runs produce an affirmative statement ("Contract honored — no deviations found") rather than silence or a blank section |

---

## Aspirational Criteria (14 pts total)

Fourteen criteria share the 14-point pool (1.0 pt each).

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
| C-20 | **Pre-printed pattern block in summary template** *(R5)* — the summary section pre-prints a named `## Patterns` (or equivalent) block as a structural slot, requiring the model to either populate it with grouped findings or write an explicit "No patterns identified" statement; the block is unconditionally present in the template regardless of finding count, making pattern analysis structurally mandatory at write time rather than conditionally added | coverage | The summary template contains a pre-printed named Patterns block; instructional notes directing the model to add a pattern note when applicable (which satisfies C-10) do not satisfy C-20 without the pre-printed structural slot |
| C-21 | **Integration-impact universality in stratified architecture** *(R5)* — in a stratified template architecture (C-16), the `connector-impact` (or equivalent) slot appears in all three tier templates including cosmetic, on the basis that cosmetic deviations may still affect downstream display, documentation, or monitoring integrations; omitting the slot from the cosmetic tier because schema breakage is considered unlikely is not a valid structural exemption | depth | All three tier templates (breaking, degraded, cosmetic) carry a labeled integration-impact field; a stratified architecture where connector-impact appears only in breaking and degraded tiers (which may satisfy C-16 and C-06 individually) does not satisfy C-21; does not apply when using a unified template (C-14 governs instead); applies only when N findings ≥ 1 and a stratified template architecture is used |
| C-22 | **Full artifact skeleton before Phase 1** *(R6)* — the complete artifact skeleton (all section headers and template slots in final position) is presented as a named structural declaration before Phase 1 begins, making every section unconditionally visible from the start; the skeleton functions simultaneously as a document-shape commitment device, a structural completeness enforcer for all sections (including Patterns), and a phase-separation guarantor | format | A complete artifact skeleton section appears before Phase 1, containing all section headers and template slots in their final positions; a named preamble behavioral protocol (which satisfies C-19) placed before Phase 1 without a structural skeleton does not satisfy C-22; a pre-printed Patterns slot embedded within a Phase 5 summary template (which satisfies C-20) without a top-level skeleton declaration does not satisfy C-22; instructional text directing the model to produce specific sections (which satisfies C-11) without a pre-printed skeleton does not satisfy C-22 |

---

## Scoring Examples

| Scenario | Essential | Recommended | Aspirational | Composite | Golden? |
|----------|-----------|-------------|--------------|-----------|---------|
| All pass | 5/5 | 3/3 | 14/14 | 104 | yes |
| Essential + all recommended + 12 aspirational | 5/5 | 3/3 | 12/14 | 102 | yes |
| R6 runner-up (V-02: C-21 PASS, C-20 FAIL, C-22 FAIL) | 5/5 | 3/3 | 11/14 | 101 | yes |
| R6 (V-03 skeleton-first: C-20 PASS, C-22 PASS, C-15 FAIL, C-16 FAIL, C-21 N/A) | 5/5 | 3/3 | 11/14 | 101 | yes |
| R6 (V-01: C-20 PASS, C-15 FAIL, C-16 FAIL, C-21 N/A, C-22 FAIL) | 5/5 | 3/3 | 10/14 | 100 | yes |
| R5 top score (V-01: C-19 + C-20 gap + C-15/C-16 gap) | 5/5 | 3/3 | 9/14 | 99 | yes |
| R5 runner-up (V-02: C-15 + C-16, no C-10/C-14/C-18/C-19/C-20/C-21) | 5/5 | 3/3 | 7/14 | 97 | yes |
| R4 top score (V-02: C-18 + C-19, avoids C-04 gap) | 5/5 | 3/3 | 8/14 | 98 | yes |
| R3 top score (C-16 + C-17 + C-18, no C-10 or C-19) | 5/5 | 3/3 | 6/14 | 96 | yes |
| R2 single aspirational (C-13, C-14, or C-15) | 5/5 | 3/3 | 1/14 | 91 | yes |
