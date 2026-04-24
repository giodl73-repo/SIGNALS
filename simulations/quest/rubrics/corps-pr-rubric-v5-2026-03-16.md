Written to `simulations/quest/rubrics/corps-pr-rubric-v5-2026-03-16.md`.

---

**Two new criteria extracted from V-04 excellence signals:**

**C-17 — Inertia Advocate section frames the status quo as a budget authority position with explicit cost terms** *(closes C-11 authority gap)*
V-04's "status-quo budget authority" framing went beyond C-11's sequencing + reference-object requirement. C-11 ensures the IA section is structurally first and provides a baseline. C-17 requires the baseline to be expressed in cost terms — what the current state costs to maintain vs. what the change costs to adopt — so technical roles must engage the arithmetic, not dismiss the position as preference.

**C-18 — Review process is structured as named phase gates with explicit entry and exit conditions, with domain-lens validity as the finding-generation exit gate** *(closes reproducibility gap)*
V-04's five-phase-gate structure made each transition (Routing → Role Activation → Finding Generation → Synthesis → Decision) independently auditable. C-18 requires this structure and specifically anchors C-15's binary test + rewrite consequence as the Phase-C exit gate — a finding cannot advance to synthesis without passing it. A skill that produces correct output without phase-gate structure passes all prior criteria and fails C-18.

**Scoring formula updated**: aspirational denominator 8 → 10; each criterion worth 1.0 pt; perfect run still 100.
hest-risk finding across all roles. A run that lists per-role findings without a synthesis section fails. |
| C-04 | Output contains exactly one explicit GO/NO-GO decision | essential | correctness | The output contains exactly one decision node with a value of GO, NO-GO, or GO WITH CONDITIONS. Delegated decisions ("the team should weigh"), hedged decisions ("consider merging"), and absent decisions all fail. |
| C-05 | Findings are specific to the role's domain lens | essential | correctness | Each finding must pass the domain-lens test: would only this role raise this finding given their domain? A finding that any generic reviewer could write, regardless of role, fails the criterion. The skill must include an explicit validity check — not just a specificity contract — that tests role-domain fidelity. |

---

## Recommended Criteria (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Coverage gaps are surfaced when no scope pattern matches a changed file | recommended | completeness | When a changed file matches no org.yaml scope pattern, the output contains an explicit coverage gap notice naming the unmatched file. A run that silently omits unmatched files fails. |
| C-07 | Per-role finding counts are summarized with severity breakdown | recommended | format | Each role findings section ends with a summary line stating: total findings for that role and the count by severity (e.g., "3 findings: 1 P1, 2 P3"). The summary must appear as a distinct element — not require the reader to count manually. A run with no per-role summaries fails. A run where summaries appear only in the consensus section and not per-role fails. |
| C-08 | AMEND mode scope is disclosed when run with added reviewer or changed scope | recommended | behavior | When run with an AMEND directive (e.g., "add security-architect", "change scope to compiler only"), output contains a scope disclosure block naming: (a) what was amended, (b) which roles were added or removed, (c) which prior findings are superseded. A run in default mode passes by default. An AMEND run with no scope disclosure fails. |

---

## Aspirational Criteria (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Consensus analysis includes root cause synthesis for role-divergent findings | aspirational | depth | When two or more roles disagree on a finding, the consensus section contains a root cause synthesis stating WHY the roles diverge -- not just that they do. The synthesis must name the structural reason (e.g., "compiler-lead rates P1 because the change affects codegen path; tpm rates P3 because no user-facing behavior changes"). A consensus section that only lists the highest-severity verdict without explaining divergence fails. A run with no divergent findings passes by default. |
| C-10 | GO WITH CONDITIONS names the role responsible for each condition's sign-off | aspirational | correctness | When the recommendation is GO WITH CONDITIONS, each condition names: (a) what must be resolved, (b) which role must confirm resolution before merge. A GO WITH CONDITIONS recommendation that lists conditions without named owner roles fails. A GO or NO-GO recommendation passes by default. |
| C-11 | Inertia Advocate is sequenced first and output is structured as a reference object | aspirational | structure | When the Inertia Advocate is a selected reviewer, their section appears before all technical role sections. The section must be structured so subsequent technical roles have a baseline to argue against -- not merely a first-in-list position. A run that does not include the Inertia Advocate as a selected reviewer passes by default. |
| C-12 | Divergence explanations name the architectural mechanism, not the perspective difference | aspirational | depth | When the consensus section explains why two roles diverge, the explanation names a structural or architectural mechanism in the code as the cause -- not a difference in reviewer perspective, focus, or priorities. An explanation of the form "they see this differently because of their role" fails. An explanation of the form "compiler-lead sees risk because the change bypasses the existing guard at auth/middleware.ts:88" passes. A run with no divergent findings passes by default. |
| C-13 | Perspective-label prohibition is enumerated, not principled | aspirational | depth | The skill's consensus template contains an explicit, enumerated ban list of >=3 prohibited perspective-label phrases -- not a general instruction to "avoid perspective labels." The ban list must be checkable: a reviewer can scan the output against each listed phrase and make a binary pass/fail determination per phrase. A prohibition expressed only as a positive instruction ("name the mechanism") or a single example ("'they prioritize differently' fails") is insufficient -- the ban list must enumerate multiple distinct surface forms of the anti-pattern. A run with no divergent findings passes by default. |
| C-14 | Each technical role section explicitly anchors at least one finding against the Inertia Advocate's verdict | aspirational | depth | When the Inertia Advocate is a selected reviewer, each subsequent technical role section must contain at least one finding that names the Inertia Advocate's assessment as the counterpoint -- e.g., "IA found the current error-handling sufficient; compiler-lead rates P1 because the new codegen path bypasses the existing guard." The anchor may appear in any finding within the section; it does not need to be F-01. A technical role section with zero IA references fails. A run that does not include the Inertia Advocate as a selected reviewer passes by default. |
| C-15 | Domain-lens validity check is stated as an explicit rewrite gate, not a naming contract | aspirational | correctness | The skill must include a domain-lens validity check expressed as: (a) a binary test -- "would only this role raise this finding given their domain?" -- and (b) a rewrite consequence -- "if any generic reviewer could write the same sentence, revise it." A specificity contract (e.g., "name the file and line") that does not include the domain-lens test fails -- specificity ensures location precision, not role-domain fidelity. A skill that enforces naming precision without the explicit rewrite gate passes C-05 but fails C-15. |
| C-16 | AMEND scope disclosure is a structured block with named output fields, not prose instructions | aspirational | format | When the skill includes AMEND mode handling, the scope disclosure must be a structured output block with named fields enumerated as template slots -- not a prose instruction describing what to say. The block must name at minimum: (a) what was amended, (b) which roles were added or removed, (c) which prior findings are superseded. A disclosure format expressed as prose instruction ("state what role was added, which files triggered it...") without a templated output block fails. A run in default mode passes by default. |
| C-17 | Inertia Advocate section frames the status quo as a budget authority position with explicit cost terms | aspirational | depth | When the Inertia Advocate is a selected reviewer, their section must frame the status quo in cost terms -- not as opinion or risk-listing, but as a cost/risk tradeoff: what the current state costs to maintain and what the proposed change costs to adopt. The IA as budget authority means their verdict is expressed as a quantified position (e.g., "maintaining current error-handling costs Y in incident exposure; adopting this change costs Z in integration risk"), not as enumerated concerns without cost framing. A section that lists IA risks without cost framing fails. A run that does not include the Inertia Advocate as a selected reviewer passes by default. |
| C-18 | Review process is structured as named phase gates with explicit entry and exit conditions, with domain-lens validity as the finding-generation exit gate | aspirational | structure | The skill structures the review output as a sequence of named phases (e.g., Routing, Role Activation, Finding Generation, Synthesis, Decision), where each phase names: (a) its entry condition -- what must be true to begin, (b) its exit condition -- what must be satisfied to advance, and (c) which rubric criteria the phase gates. The domain-lens validity check (C-15's binary test + rewrite consequence) must be positioned as the exit condition for the finding-generation phase -- no finding advances to synthesis without passing it. A review that produces correct output without a phase-gate structure passes other criteria but fails C-18. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

*aspirational denominator increased from 8 to 10 in v5; each criterion is worth 1.0 pt; a perfect run still scores 100.*

---

## What changed from v4

**C-17 closes the C-11 authority gap.** C-11 requires the Inertia Advocate to be sequenced first and structured as a reference object. Round 4 (V-04) showed a variation that went further: the IA was designated as the "status-quo budget authority," with their section required to quantify maintenance cost and adoption cost as a tradeoff -- not merely list concerns or establish a baseline position. A section that passes C-11 via sequencing and structural reference but frames the IA verdict as opinion or risk enumeration fails C-17. The cost-framing requirement makes the IA verdict a quantified anchor that technical roles must engage arithmetically, not dismiss as preference.

**C-18 closes the reproducibility gap across the full review process.** Prior criteria (C-01 through C-16) define what each output element must contain, but none require the review to be structured as a phase-gated sequence with explicit entry and exit conditions. Round 4 (V-04) introduced a five-phase-gate structure that makes each transition from Routing through Decision auditable: a reviewer can inspect the exit condition for any phase and verify it was met before the next phase began. C-18 adds this requirement and explicitly anchors C-15's domain-lens validity check as the exit gate for the finding-generation phase -- connecting the binary test + rewrite consequence to a structural position in the review pipeline, not just a check that happens to appear somewhere in the output. A skill that produces correct results without this phase structure passes all prior criteria and fails C-18.

**Scoring formula updated**: aspirational denominator 8 -> 10; each aspirational criterion worth 1.0 pt; perfect run still 100.
