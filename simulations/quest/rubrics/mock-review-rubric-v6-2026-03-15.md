Scanning the R5 scorecard for patterns not yet captured in C-01 through C-21.

**New excellence signals extracted:**

- **V-04/V-05 inertia framing**: DEFAULT DECISION POSITION = REAL-REQUIRED; MOCK-ACCEPTED = earned escape. The scorecard notes V-04 introduces this ("makes MOCK-ACCEPTED an earned escape") and V-05 inherits it, with the observation that "inertia framing motivates why the escape argument is inherently contrastive — MOCK-ACCEPTED must argue against the REAL-REQUIRED default." A skill that treats both outcomes symmetrically cannot force the author to produce a contrastive argument. → **C-22**

- **V-05 C-20 enhancement**: The `Structural position` slot now explicitly anchors to Strategy SQ-1 ("The tier decision this namespace supports (from Strategy SQ-1) should appear here"). This creates a named cross-role link: the contrastive rationale is grounded in a specific sub-question answer, not a generic structural claim. V-02 has the two-slot structure but no SQ-1 anchor; V-05 adds the anchor. → **C-23**

- **V-05 C-21 enhancement**: The Artifact state field propagates into the next-steps entry format ("/{skill-id} {topic} — {artifact state from Artifact state field if eval-driven}"), producing end-to-end traceability from diagnostic SQ answer through verdict to next-steps. V-03 has the Artifact state field in the decision block; V-05 carries it forward into next-steps. A skill that defines the field but does not propagate it breaks the traceability chain. → **C-24**

Aspirational denominator updated from 13 to 16.

---

```markdown
# Quest Rubric — /quest:mock-review
**Version**: v6 | **Date**: 2026-03-15

---

## Scoring Formula

`(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/16 × 10)`

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
| C-22 | Decision inversion framing | The skill explicitly establishes REAL-REQUIRED as the default decision position and MOCK-ACCEPTED as an earned escape that requires an argument against the default. A named block (e.g., DEFAULT DECISION POSITION) states this inversion at the skill level — not only in rationale guidance. A skill that treats MOCK-ACCEPTED and REAL-REQUIRED as symmetric outcomes, or that introduces contrastive rationale guidance without establishing the inversion, does not satisfy this criterion. The inertia structure is what forces the author to produce a genuine contrastive argument rather than a confirmatory one. |
| C-23 | Strategy SQ-1 anchor in structural position | The `Structural position` slot of the MOCK-ACCEPTED rationale template explicitly names Strategy SQ-1 as its source — the tier decision the namespace supports. The slot grammar requires the author to state which specific tier decision this namespace feeds, distinguishing a namespace that supports a structural-form decision (no tier-boundary validation needed) from one that supports a tier-gating decision (real evidence required). A generic structural position statement ("this namespace has limited scope") without the SQ-1 anchor does not satisfy this criterion; the anchor must be a named slot requirement, not an example. |
| C-24 | Artifact state field propagation into next-steps | The `Artifact state` field defined in evaluation-driven REAL-REQUIRED decision blocks propagates forward into the next-steps entry format, producing entries of the form `/{skill-id} {topic} — {artifact state}`. This creates end-to-end traceability: diagnostic SQ answer → Artifact state field → verdict → next-steps entry. A skill that defines the Artifact state field in the decision block but does not require it in the next-steps entry format breaks the traceability chain. A next-steps entry that names only the skill and topic without the propagated artifact state does not satisfy this criterion. |

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
| C-14 SQ citation in verdict traceability | | |
| C-15 Entity-naming SQ grammar | | |
| C-16 Canary confirmation (prohibited under failure) | | |
| C-17 Auto-flagged contamination guard | | |
| C-18 Inter-step gate with forward reference | | |
| C-19 Structured trigger notation | | |
| C-20 Contrastive MOCK-ACCEPTED rationale | | |
| C-21 SQ answer structural signal | | |
| C-22 Decision inversion framing | | |
| C-23 Strategy SQ-1 anchor in structural position | | |
| C-24 Artifact state field propagation into next-steps | | |
```
