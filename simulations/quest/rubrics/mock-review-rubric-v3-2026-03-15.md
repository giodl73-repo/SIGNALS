Looking at the scorecard evidence systematically for patterns not yet captured as criteria:

**V-04 C-06 evidence**: "Name the specific evaluation that failed and the **sub-question answer** that drove it" — verdict traceability extends beyond naming the verdict to citing the specific diagnostic answer.

**V-04 + V-03 C-07 evidence**: PM "Name at least one section that is present" / Architect "Name the element" / Strategy "What specific Tier {tier} decision" — sub-question grammar forces artifact-naming, not opinion verdicts.

**V-02 C-12 evidence**: "MUST NOT be written if any field missed" — the confirmation is not just required; it is *prohibited* under the failure condition. A canary output, not just a completion signal.

Three new aspirational criteria: **C-14** (sub-question answer citation), **C-15** (entity-naming sub-question grammar), **C-16** (canary confirmation — prohibited under failure).

---

```markdown
# Quest Rubric — /quest:mock-review
**Version**: v3 | **Date**: 2026-03-15

---

## Scoring Formula

`(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/8 × 10)`

**PARTIAL** = 0.5 credit. **PASS** = 1.0. **FAIL** = 0.

---

## Criteria

### Essential (60 pts) — hard correctness and behavior invariants

| ID | Name | What to look for |
|----|------|-----------------|
| C-01 | Decision completeness | Every namespace appears in exactly one decision list. No namespace is skipped or left undecided. Auto-flagged namespaces count as decided. |
| C-02 | Automatic rule correctness | EVIDENCE-HEAVY, TIER-CRITICAL, and COMPLIANCE rules all fire before any role evaluation begins. Rules are not role-overridable. A hard gate or STOP instruction separates auto-flagging from the evaluation phase. |
| C-03 | MOCK-ACCEPTED reason code present | At least one exact code from `STRUCTURAL-COVERAGE-SUFFICIENT` / `DOMAIN-KNOWLEDGE-CONSISTENT` appears per MOCK-ACCEPTED decision. No paraphrase. No invented codes. |
| C-04 | Status fields written back | Status lines in the source artifact are edited in-place. A named mandatory phase covers the write-back action. This is the defining behavior of the skill. |
| C-05 | Next-steps list in priority order | Critical namespaces (trace, scout-feasibility, listen) listed before non-critical, evidence-heavy last. Ordering rule is stated explicitly, not inferred. |

### Recommended (30 pts) — depth and traceability

| ID | Name | What to look for |
|----|------|-----------------|
| C-06 | Rule trigger named per REAL-REQUIRED | Each auto-flagged namespace records which rule fired (`EVIDENCE-HEAVY`, `TIER-CRITICAL`, or `COMPLIANCE`). Evaluation-driven REAL-REQUIRED decisions name the evaluation verdict that drove them. |
| C-07 | PM/Architect/Strategy evaluation shown | All three roles produce a verdict for each non-auto namespace. PM sub-questions reference sections, gates, or tables. Architect checks for contradiction with known architectural facts. Strategy assesses coverage adequacy for the stated tier. |
| C-08 | Tier flag respected | Tier is stated at the top of the output with its source. TIER-CRITICAL rule correctly gates on Tier >= 2. Tier is applied consistently throughout the review. |

### Aspirational (10 pts) — raise the bar once basics are solid

| ID | Name | What to look for |
|----|------|-----------------|
| C-09 | Coverage gap synthesis | Next-steps section includes a cross-namespace risk statement and urgency grouping commentary, not just a flat priority-ordered list. |
| C-10 | Namespace-specific MOCK-ACCEPTED rationale | Each MOCK-ACCEPTED decision includes an explanatory sentence stating why the reason code applies to that specific namespace — not a bare code. |
| C-11 | Forbidden-output enumeration for auto-rules | Auto-rule enforcement explicitly names the forbidden outputs ("DO NOT mark EVIDENCE-HEAVY MOCK-ACCEPTED regardless of mock quality") rather than only stating trigger conditions. Forbidden-output phrasing is present for all three rules. |
| C-12 | Zero-remaining confirmation gate | The write-back phase includes an explicit verification step confirming that zero Status fields remain as `MOCK (awaiting review)` after the phase completes. The confirmation is a required output, not implied. |
| C-13 | Verifiable role-step separation | PM, Architect, and Strategy evaluations are structured as separately completable, individually verifiable steps — each with its own heading, diagnostic sub-questions, and required verdict. An inline combined template does not satisfy this criterion. |
| C-14 | Sub-question answer citation in verdict traceability | For evaluation-driven REAL-REQUIRED decisions, the output names not only the failing verdict but the specific sub-question answer that drove it. The verdict is fully traceable to a diagnostic result, not just to a role evaluation. |
| C-15 | Entity-naming sub-question grammar | PM, Architect, and Strategy sub-questions are phrased to require naming a specific artifact — a section, element, table, or tier decision — rather than producing a yes/no or opinion answer. Sub-question grammar uses "Name X" or "What specific X" forms. A sub-question answered with "yes/no" or a general assessment does not satisfy this criterion. |
| C-16 | Canary confirmation (prohibited under failure) | The zero-remaining confirmation statement is not only required on success — it is explicitly prohibited if any Status field remains as `MOCK`. The confirmation is a canary output: its presence asserts the condition is met; writing it when the condition is not met is a named error. |

---

## Scoring Table Template

| Criterion | Rating (P / Pt / F) | Evidence |
|-----------|---------------------|---------|
| C-01 Decision completeness | | |
| C-02 Automatic rule correctness | | |
| C-03 MOCK-ACCEPTED reason codes | | |
| C-04 Status write-back | | |
| C-05 Next-steps priority order | | |
| C-06 Rule trigger named | | |
| C-07 PM/Arch/Strategy shown | | |
| C-08 Tier flag respected | | |
| C-09 Coverage gap synthesis | | |
| C-10 MOCK-ACCEPTED namespace-specific rationale | | |
| C-11 Forbidden-output enumeration | | |
| C-12 Zero-remaining confirmation gate | | |
| C-13 Verifiable role-step separation | | |
| C-14 Sub-question answer citation | | |
| C-15 Entity-naming sub-question grammar | | |
| C-16 Canary confirmation (prohibited under failure) | | |

**Essential**: __/5 = __ | **Recommended**: __/3 = __ | **Aspirational**: __/8 = __
**Composite**: (__ × 60) + (__ × 30) + (__ × 10) = __
**All essential pass**: YES / NO
```

---

**What changed from v2:**

| New criterion | Source signal | Distinguishes from |
|---|---|---|
| C-14 | V-04 C-06 evidence: "sub-question answer that drove it" | C-06 only requires naming the verdict |
| C-15 | V-04 + V-03 C-07 evidence: "Name at least one section", "Name the element" | C-13 requires structural separation; C-15 requires the sub-question *grammar* to force artifact-naming |
| C-16 | V-02 C-12 evidence: "MUST NOT be written if any field missed" | C-12 requires a confirmation; C-16 requires the confirmation to be *prohibited* under the failure condition — a canary, not a checkbox |

**Scoring formula updated**: denominator for aspirational moves from `/5` to `/8` to reflect the expanded set.
