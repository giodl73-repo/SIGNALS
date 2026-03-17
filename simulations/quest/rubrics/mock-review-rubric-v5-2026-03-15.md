Scanning the scorecard for patterns not yet captured in C-01 through C-19.

**New excellence signals extracted:**

- **V-05 C-10 PARTIAL**: "The rationale is confirmatory, not contrastive... does not require explaining why this namespace's structural pattern makes real evidence unnecessary vs. what would require real evidence." C-10 requires a rationale sentence explaining why the code applies. The new pattern requires the rationale to *contrast* the namespace's structural state against the threshold that would require real evidence — forcing the author to demonstrate they understand the decision boundary, not just confirm the code was selected. → **C-20**

- **V-05 C-14 PARTIAL**: "There is no named failure mode or positive structural signal (e.g., a field format that forces present-tense artifact naming vs. past-tense assessment). A reviewer reading the output cannot mechanically distinguish a genuine SQ answer from a verdict restatement without judgment." C-14 requires citing the SQ answer. The new pattern requires a *positive structural signal* — a field form (present-tense artifact naming) that mechanically distinguishes citation from restatement, plus a named failure mode for the restatement error. → **C-21**

Scoring table template also corrected: v4 template truncated at C-10. v5 includes all 21 rows. Aspirational denominator updated from 11 to 13.

---

```markdown
# Quest Rubric — /quest:mock-review
**Version**: v5 | **Date**: 2026-03-15

---

## Scoring Formula

`(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/13 × 10)`

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
| C-17 | Auto-flagged contamination guard | Beyond phase separation, the skill includes an explicit prohibition on applying role evaluation to namespaces that have already been decided by automatic rules. The guard names the contamination error ("DO NOT apply evaluation to auto-flagged namespace") — not merely the rule trigger condition. Separating phases without naming the contamination error does not satisfy this criterion. |
| C-18 | Inter-step gate with next-step reference | Role-step completion gates name the specific next step being blocked ("DO NOT proceed to Step N+1 until..."), making the gate actionable rather than merely declarative. A completion note without a forward reference to the named next step does not satisfy this criterion. |
| C-19 | Structured trigger notation | The rule trigger appears in a named, parseable template field (e.g., `trigger = {rule label}`) rather than embedded in prose. The field is in a fixed position within the decision output block and can be mechanically verified. Mentioning the rule name in free-form text does not satisfy this criterion. |
| C-20 | Contrastive MOCK-ACCEPTED rationale | Each MOCK-ACCEPTED rationale sentence not only confirms that the reason code applies but contrasts the namespace's structural state against the threshold that would require real evidence — explaining why this namespace does not cross that threshold. A confirmatory sentence ("structural coverage is sufficient here") does not satisfy this criterion; a contrastive sentence does ("this namespace has no tier-gating decisions and no architecture-pattern dependencies, so structural coverage is sufficient — unlike a trace or scout-feasibility namespace where those factors would require real evidence"). |
| C-21 | SQ answer structural signal | The sub-question answer citation template provides a positive structural signal — a field form that mechanically distinguishes a genuine SQ answer from a verdict restatement — rather than only a negative prohibition. Present-tense artifact naming ("Section 3.2 lists no fallback path") is distinguished from past-tense assessment restatement ("Architect found no fallback path"). The template names this distinction as a structural rule and names the restatement error ("verdict echo"). A template that only says "not a restatement of the verdict" without providing the distinguishing form does not satisfy this criterion. |

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
| C-17 Auto-flagged contamination guard | | |
| C-18 Inter-step gate with next-step reference | | |
| C-19 Structured trigger notation | | |
| C-20 Contrastive MOCK-ACCEPTED rationale | | |
| C-21 SQ answer structural signal | | |
```
