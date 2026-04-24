Reading the scorecard carefully to extract the two new criteria and produce the complete v20 rubric.

**Pattern extraction from Round 19:**
- **C-42** — Universal criterion-ID labeling: three-tier definition (PASS / PARTIAL / FAIL) grounded by V-01 PARTIAL boundary case and V-02 FAIL floor
- **C-43** — Dedicated leftmost `Row #` column: binary (PASS / FAIL) grounded by V-04 explicit fail case and V-05 belt-and-suspenders still-PASS confirmation

---

```markdown
# Quest Rubric — /quest:mock-review
**Version**: v20 | **Date**: 2026-03-16

---

## Scoring Formula

`(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/37 × 10)`

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
| C-31 | *(established in prior round)* | All variants PASS — baseline. |
| C-32 | *(established in prior round)* | All variants PASS — baseline. |
| C-33 | *(established in prior round)* | All variants PASS — baseline. |
| C-34 | *(established in prior round)* | All variants PASS — baseline. |
| C-35 | Strategy-first tier anchoring before Arch evaluation | Strategy evaluation runs before Architect evaluation so that tier anchoring is established before structural contradiction checking begins. A cross-step gate at the Strategy step boundary names the tier-decision output that Architect evaluation consumes. A skill with Architect evaluation preceding Strategy does not satisfy this criterion; the tier anchor must exist as a named prerequisite for the Architect step, not as a parallel or post-hoc input. |
| C-36 | Arch-first before Strategy for structural contradiction gating | Architect evaluation runs before Strategy evaluation so that architectural contradictions short-circuit tier-coverage analysis before it begins. The Architect step boundary includes a named gate that blocks Strategy evaluation for namespaces with `architect-verdict = CONTRADICTS-ARCHITECTURE`. A skill with Strategy evaluation preceding Architect does not satisfy this criterion; the structural contradiction check must precede tier-coverage analysis, not follow it. Note: C-35 and C-36 impose mutually exclusive role orderings — a skill satisfies exactly one of the two depending on its chosen role sequence. |
| C-37 | *(established in prior round)* | All variants PASS — baseline. |
| C-38 | *(established in prior round)* | All variants PASS — baseline. |
| C-39 | *(established in prior round)* | All variants PASS — baseline. |
| C-40 | *(established in prior round)* | All variants PASS — baseline. |
| C-41 | *(established in prior round)* | All variants PASS — baseline. |
| C-42 | Universal criterion-ID labeling | PASS when every criterion-bearing structural element carries a `[C-NN]` label: TRIAD header, AUTO-RULE guard header, inline SQ rows, step headings, slot headers, and canary block. PARTIAL when all such elements are labeled except the TRIAD header alone — the sole unlabeled case established by V-01 as the boundary condition. FAIL when labels appear only on core decision-block template slots (reason-code, Structural position, Contrast, Artifact state) while guard headers, step headings, and canary block carry no labels — the V-02 floor pattern. Adding per-row `[C-NN]` labels inside table cells on top of a labeled column header is belt-and-suspenders redundancy: it does not earn above PASS, but it does not fail the criterion. |
| C-43 | Dedicated leftmost `Row #` column | PASS when all evaluation steps present sub-questions in `\| Row # \| Sub-question \|` tabular form with the row number occupying its own dedicated leftmost column. FAIL when row numbers are embedded as `SQ-N:` prefixes inside cell content rather than occupying a dedicated column. The presence of per-row criterion-ID labels inside the Sub-question cell (V-05 belt-and-suspenders pattern) does not affect this criterion; C-43 tests column structure only. |
```

---

**What changed in v20:**

| # | Change |
|---|--------|
| Version | v19 → v20 |
| C-39, C-40, C-41 | Added as `*(established in prior round)*` baseline entries — referenced in R19 scorecard but absent from rubric text |
| C-42 | Full definition added: universal criterion-ID labeling, three-tier PASS/PARTIAL/FAIL with V-01 boundary and V-02 floor anchors, belt-and-suspenders non-bonus clause |
| C-43 | Full definition added: dedicated leftmost `Row #` column, binary PASS/FAIL with V-04 fail case and V-05 structural-only test clause |
| Denominator | Stays 37 — no new additions |
