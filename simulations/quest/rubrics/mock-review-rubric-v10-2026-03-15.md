Reading the R9 scorecard for new excellence signals before writing the rubric.

**Signal 3 — C-23 PARTIAL (consistent across all variants)**: Both V-01 and V-02 score PARTIAL on C-23 with the same evidence: "Structural position concept present; SQ-1 not named as slot requirement." The partial arises because the template carries the concept but the slot label does not reference SQ-1 as its sourcing field. A template that names SQ-1 as the slot's source citation — `Feeds tier decision: [Strategy SQ-1 answer]` — makes the connection between Strategy evaluation and MOCK-ACCEPTED rationale mechanically explicit rather than conceptually implied.

**Signal 4 — C-25 PARTIAL (consistent across all variants)**: Both variants score PARTIAL on C-25 with evidence "Framing present, mechanical slot not confirmed." The two-slot structure exists in framing instructions but is never declared as a named template pair. A template that names the pair explicitly — "RATIONALE TEMPLATE (2 required slots): (1) Structural position... (2) Contrast..." — makes slot completeness verifiable at the definition site, not just inferred from framing guidance.

New criteria: **C-30** (SQ-1 sourcing label in Structural position slot) and **C-31** (TRIAD header declares cardinality). Denominator: 21 → 23.

---

```markdown
# Quest Rubric — /quest:mock-review
**Version**: v10 | **Date**: 2026-03-15

---

## Scoring Formula

`(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/23 × 10)`

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
| C-25 | Dedicated contrast sub-slot in MOCK-ACCEPTED template | The MOCK-ACCEPTED rationale template contains a dedicated, labeled sub-slot (e.g., `Contrast:`) that is structurally separate from the `Structural position` slot. This mechanical separation closes the "confirmatory escape" identified in C-20: a single-slot template allows a confirmatory sentence to satisfy the rationale slot without producing a genuine contrastive argument. The two-slot structure requires the author to explicitly address the contrast in a dedicated field, making it impossible to satisfy the template without producing both components. A template with only a single `Rationale:` slot — even one with contrastive framing instructions — does not satisfy this criterion, because instructions are advisory and a slot is mechanical. |
| C-26 | Role-sequence gate as contamination control | The skill places Architect evaluation before PM evaluation so that architectural contradictions short-circuit structural analysis before it begins. A cross-step contamination guard at the Architect step boundary names both the specific verdict value that triggers the block and the downstream step being suppressed: "DO NOT apply PM evaluation to namespaces with `architect-verdict = CONTRADICTS-ARCHITECTURE`." This guard is distinct from the phase-separation requirement in C-17 (which blocks evaluation of auto-flagged namespaces) — C-26 requires a named inter-role guard that fires on a specific verdict value and prevents a later role step from running. A skill that separates Architect and PM into distinct steps without this named cross-step guard does not satisfy this criterion; the trigger condition must name the verdict value, not just the role boundary. |
| C-27 | Triad DO NOT coverage (complete forbidden-output set) | All three automatic rules carry individually labeled forbidden-output statements that together form an enumerable, mechanically verifiable set. The required triad is: (1) EVIDENCE-HEAVY — DO NOT statement naming that rule, (2) TIER-CRITICAL — DO NOT statement naming that rule, (3) COMPLIANCE — DO NOT statement naming that rule. A skill that covers two of the three rules does not satisfy this criterion; completeness across the full triad is the test. A single blanket prohibition ("DO NOT mark any auto-classified namespace MOCK-ACCEPTED") does not satisfy this criterion because it is not enumerable by rule label and cannot be mechanically verified for per-rule coverage. Each rule must have its own named DO NOT statement. |
| C-28 | Step-name anchor in forward reference | The inter-step gate forward reference names both the step number and the step's descriptive label — for example, "DO NOT proceed to Step 3 (PM Evaluation) until..." — not the step number alone. The label makes the gate self-resolving: a reader can verify the target step without counting from the beginning of the skill. A gate that names only a position ("Step N+1") does not satisfy this criterion because it requires counting context; a gate that names both position and label resolves in place. This criterion deepens C-18: C-18 requires a forward reference, C-28 requires that reference to carry the step's identity independently of its position. |
| C-29 | Phase-gate co-location of forbidden-output block | The FORBIDDEN OUTPUTS TRIAD block is positioned immediately adjacent to the phase gate that separates automatic rules from role evaluation — not distributed across role steps. This co-location design decouples C-26 (Architect-first role ordering) from C-27 (enumerable per-rule DO NOT statements): the triad block sits at the phase boundary, independent of which role runs first, so any role sequence satisfies C-27 without triggering ordering constraints. A skill that distributes forbidden-output statements across role steps ties C-27 satisfaction to step position: the DO NOT statements can only be verified by checking each step in sequence, creating an implicit dependency between the triad and the ordering. A skill with a single co-located TRIAD block satisfies C-27 in one scan at the phase gate and leaves role ordering free to satisfy C-26. |
| C-30 | SQ-1 sourcing label in Structural position slot | The `Structural position` slot in the MOCK-ACCEPTED rationale template carries an explicit SQ-1 source citation as a required slot field — for example, `Feeds tier decision: [Strategy SQ-1 answer]` — not as a framing example or instruction. The slot grammar requires the author to name the specific Strategy SQ-1 tier decision this namespace feeds; a generic structural position statement without the SQ-1 source label does not satisfy this criterion. This deepens C-23: C-23 requires SQ-1 to be named as the slot's conceptual source, C-30 requires the slot to encode the SQ-1 connection as a citation field — mechanically distinguishing a template that mentions SQ-1 from one that structurally captures the SQ-1 answer as a required slot output. A PARTIAL on C-23 (concept present, not a named slot) does not satisfy C-30, because the citation field must appear in the template definition itself, not only in surrounding guidance. |
| C-31 | TRIAD header declares cardinality | The FORBIDDEN OUTPUTS TRIAD block carries a header that explicitly declares the required cardinality — for example, "FORBIDDEN OUTPUTS TRIAD (3 rules, all required)" — making completeness verifiable at the block header without counting individual DO NOT statements. A TRIAD block that co-locates three DO NOT statements without a cardinality declaration satisfies C-27 (all three rules present) and C-29 (co-location) but not C-31, because verifying completeness still requires reading all entries rather than checking a declared count. The cardinality declaration converts a content-completeness check into a header-level assertion: a reviewer can confirm the triad is complete by reading the header alone, then confirm each entry matches. A block header that names the structure ("FORBIDDEN OUTPUTS") without declaring its cardinality does not satisfy this criterion; the count must be stated and marked as required. |

---

## Scoring Table Template

| Criterion | Rating (P / Pt / F) | Evidence |
|-----------|---------------------|---------|
| C-01 Decision completeness | | |
| C-02 Automatic rule correctness | | |
| C-03 MOCK-ACCEPTED reason codes | | |
| C-04 Status write-back | | |
| C-05 Next-steps priority ordering | | |
| C-06 Rule trigger named | | |
| C-07 PM/Arch/Strategy shown | | |
| C-08 Tier flag respected | | |
| C-09 Coverage gap synthesis | | |
| C-10 Namespace-specific rationale | | |
| C-11 Forbidden-output enumeration | | |
| C-12 Zero-remaining confirmation gate | | |
| C-13 Role-step separation | | |
| C-14 SQ answer citation | | |
| C-15 Entity-naming SQ grammar | | |
| C-16 Canary confirmation | | |
| C-17 Contamination guard | | |
| C-18 Inter-step gate forward reference | | |
| C-19 Structured trigger notation | | |
| C-20 Contrastive MOCK-ACCEPTED rationale | | |
| C-21 SQ answer structural signal | | |
| C-22 Decision inversion framing | | |
| C-23 Strategy SQ-1 anchor | | |
| C-24 Artifact state propagation | | |
| C-25 Dedicated contrast sub-slot | | |
| C-26 Role-sequence gate (Arch-first guard) | | |
| C-27 Triad DO NOT coverage | | |
| C-28 Step-name anchor in forward reference | | |
| C-29 Phase-gate co-location of TRIAD | | |
| C-30 SQ-1 sourcing label in Structural position slot | | |
| C-31 TRIAD header declares cardinality | | |
```
