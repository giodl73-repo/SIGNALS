Scanning the scorecard for patterns not yet captured, then writing v4.

**New excellence signals extracted:**

- **V-04 C-02**: "DO NOT apply ... evaluation to any auto-flagged namespace" — beyond phase separation, an explicit cross-contamination guard. C-02 requires rules to fire first; this requires naming the contamination error itself. → **C-17**

- **V-01/V-04 C-13**: "completion gate" / "DO NOT proceed to Step N+1 until..." — C-13 requires separate steps with headings and verdicts. The new pattern requires a *forward-blocking gate that names the specific next step*, making the gate actionable rather than merely declarative. → **C-18**

- **V-01/V-04 C-06**: `trigger = {rule label}` as a named template field rather than prose mention. C-06 requires "records which rule fired"; excellence requires a *structured, parseable field* in a fixed position. → **C-19**

Also fixing the scoring table in v3 which was missing C-16 and updating the formula denominator from 8 to 11 aspirational.

---

```markdown
# Quest Rubric — /quest:mock-review
**Version**: v4 | **Date**: 2026-03-15

---

## Scoring Formula

`(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/11 × 10)`

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
| C-16 Canary confirmation | | |
| C-17 Auto-flagged contamination guard | | |
| C-18 Inter-step gate with next-step reference | | |
| C-19 Structured trigger notation | | |
```

---

**Changes from v3:**

| # | What changed | Why |
|---|---|---|
| Formula | denominator 8 → 11 aspirational | three new criteria added |
| C-17 | Auto-flagged contamination guard | V-04 C-02: "DO NOT apply evaluation to auto-flagged namespace" is a distinct guard beyond phase ordering |
| C-18 | Inter-step gate with next-step reference | V-01/V-04 C-13: "DO NOT proceed to Step N+1 until..." names the blocked step; declarative completion notes don't |
| C-19 | Structured trigger notation | V-01/V-04 C-06: `trigger = {rule label}` as a parseable field is stronger than prose mention |
| Table | Added C-16 row | Was missing from v3 scoring table despite being in criteria |
