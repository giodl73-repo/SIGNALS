Looking at the scorecard, I'll extract three excellence patterns:

1. **Forbidden-output enumeration** — V-04 scored the strongest on C-02 specifically because it named the forbidden outputs explicitly ("DO NOT mark EVIDENCE-HEAVY MOCK-ACCEPTED regardless of mock quality") rather than just stating what fires. That's a qualitatively different enforcement style.

2. **Zero-remaining confirmation gate** — V-03 was called out as "strongest C-04 enforcement among all variations" because of the explicit "zero Status fields may remain as MOCK after Phase 5 completes" confirmation requirement. That's a distinct verifiability pattern beyond just labeling the phase mandatory.

3. **Verifiable role-step separation** — V-04 had PM/Architect/Strategy as three separately completable STEPS with per-role diagnostic sub-questions. V-02 was called "strongest C-07 forcing function" because of "Name specific sections or mechanisms." Both point to the same pattern: role evaluations as individually verifiable units, not an inline template.

Here is the complete updated rubric:

---

```markdown
# Quest Rubric — /quest:mock-review
**Version**: v2 | **Date**: 2026-03-15

---

## Scoring Formula

`(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/5 × 10)`

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

**Essential**: __/5 = __ | **Recommended**: __/3 = __ | **Aspirational**: __/5 = __
**Composite**: (__ × 60) + (__ × 30) + (__ × 10) = __
**All essential pass**: YES / NO

---

## Threshold Guidance

| Score | Interpretation |
|-------|---------------|
| 90–100 | All essential + recommended pass; aspirational differentiate |
| 80–89 | Strong but has essential or recommended partials |
| 70–79 | Essential gaps; needs structural revision |
| < 70 | Fundamental behavior missing |

---

## Changelog

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | Added C-11 (forbidden-output enumeration), C-12 (zero-remaining confirmation gate), C-13 (verifiable role-step separation) from Round 1 excellence signals; aspirational weight unchanged at 10 pts, denominator updated to 5 |
```

---

The three new criteria target different failure modes:

- **C-11** catches rubrics that state rules but don't prevent the model from working around them
- **C-12** catches rubrics where write-back is named mandatory but has no verifiable completion signal
- **C-13** catches rubrics where role evaluation looks present in the template but can be satisfied with one-word verdicts

The aspirational denominator moves from `/2` to `/5` in the formula, so the weight per criterion drops from 5 pts to 2 pts — the 10-pt ceiling is unchanged.
