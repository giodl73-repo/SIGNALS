Written to `simulations/quest/rubrics/corps-pr-rubric-v4-2026-03-16.md`.

---

**Two new criteria extracted from Round 3 PARTIAL signals:**

**C-15 — Domain-lens validity check is stated as an explicit rewrite gate, not a naming contract** *(closes V-02 C-05 gap)*
V-02's column contract required `auth/middleware.ts:88`-style specificity but had no "would only this role raise this?" test. Specificity ensures location precision, not role-domain fidelity. C-15 requires both the binary test and the rewrite consequence to be present. A variation that passes C-05 via naming precision alone fails C-15.

**C-16 — AMEND scope disclosure is a structured block with named output fields, not prose instructions** *(closes V-03 C-08 gap)*
V-03's AMEND section said "state what role was added, which files triggered the addition, which earlier findings are superseded" — but prose instructions leave format undefined. A model can satisfy the words while producing a different layout each run. C-16 requires template slots with named fields, making the block a first-class auditable artifact.

**Scoring formula updated**: aspirational denominator 6 → 8; each aspirational criterion worth 1.25 pts; perfect run still 100.
only; V-02 named one prohibited phrase; V-04 named one prohibited phrase with a "do not" framing; none were exhaustive. The first new criterion (C-13) closes this gap: the prohibition must enumerate >=3 banned phrases as a self-auditable checklist, not a general principle. The second new criterion (C-14) makes C-11's reference-object sequencing bidirectional: technical role sections must explicitly anchor at least one finding against the Inertia Advocate's verdict by name, completing the structural loop that C-11 opens.

**v4 additions**: Round 3 scoring revealed two distinct PARTIAL patterns. First (C-05 in V-02): a column contract that enforced code-surface specificity (file+line) but omitted the domain-lens validity test — specificity ensures location precision but not role-domain fidelity; a finding naming a specific location that any generic reviewer could write passes the naming contract and fails C-05. C-15 closes this gap by requiring the validity check to be stated as an explicit binary test plus a rewrite consequence, not derivable from a specificity rule alone. Second (C-08 in V-03): an AMEND disclosure that listed required elements as prose instruction but provided no structured output block template — a model following prose instructions can format the disclosure inconsistently run to run. C-16 closes this gap by requiring the AMEND block to be a templated output structure with named fields, not a description of what to say.

---

## Essential Criteria (60 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Reviewer routing is traceable to org.yaml scope patterns | essential | correctness | The output shows, for each selected reviewer, which org.yaml scope pattern matched which changed file. A run that lists selected reviewers without routing evidence fails. A run that infers reviewers from filename or convention without citing org.yaml fails. |
| C-02 | All findings carry explicit severity labels | essential | format | Every finding — across all reviewer sections — carries a severity label from the defined set (P1/P2/P3 or equivalent). A finding without a severity label fails the criterion for the entire run. |
| C-03 | Output includes cross-role consensus synthesis | essential | correctness | The output contains a synthesis section that covers: (a) what all roles agreed on, (b) where roles diverged, and (c) the highest-risk finding across all roles. A run that lists per-role findings without a synthesis section fails. |
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
| C-09 | Consensus analysis includes root cause synthesis for role-divergent findings | aspirational | depth | When two or more roles disagree on a finding, the consensus section contains a root cause synthesis stating WHY the roles diverge — not just that they do. The synthesis must name the structural reason (e.g., "compiler-lead rates P1 because the change affects codegen path; tpm rates P3 because no user-facing behavior changes"). A consensus section that only lists the highest-severity verdict without explaining divergence fails. |
| C-10 | GO WITH CONDITIONS names the role responsible for each condition's sign-off | aspirational | correctness | When the recommendation is GO WITH CONDITIONS, each condition names: (a) what must be resolved, (b) which role must confirm resolution before merge. A GO WITH CONDITIONS recommendation that lists conditions without named owner roles fails. A GO or NO-GO recommendation passes by default. |
| C-11 | Inertia Advocate is sequenced first and output is structured as a reference object | aspirational | structure | When the Inertia Advocate is a selected reviewer, their section appears before all technical role sections. The section must be structured so subsequent technical roles have a baseline to argue against — not merely a first-in-list position. A run that does not include the Inertia Advocate as a selected reviewer passes by default. |
| C-12 | Divergence explanations name the architectural mechanism, not the perspective difference | aspirational | depth | When the consensus section explains why two roles diverge, the explanation names a structural or architectural mechanism in the code as the cause — not a difference in reviewer perspective, focus, or priorities. An explanation of the form "they see this differently because of their role" fails. An explanation of the form "compiler-lead sees risk because the change bypasses the existing guard at auth/middleware.ts:88" passes. A run with no divergent findings passes by default. |
| C-13 | Perspective-label prohibition is enumerated, not principled | aspirational | depth | The skill's consensus template contains an explicit, enumerated ban list of >=3 prohibited perspective-label phrases — not a general instruction to "avoid perspective labels." The ban list must be checkable: a reviewer can scan the output against each listed phrase and make a binary pass/fail determination per phrase. A prohibition expressed only as a positive instruction ("name the mechanism") or a single example ("'they prioritize differently' fails") is insufficient — the ban list must enumerate multiple distinct surface forms of the anti-pattern. A run with no divergent findings passes by default. |
| C-14 | Each technical role section explicitly anchors at least one finding against the Inertia Advocate's verdict | aspirational | depth | When the Inertia Advocate is a selected reviewer, each subsequent technical role section must contain at least one finding that names the Inertia Advocate's assessment as the counterpoint — e.g., "IA found the current error-handling sufficient; compiler-lead rates P1 because the new codegen path bypasses the existing guard." The anchor may appear in any finding within the section; it does not need to be F-01. A technical role section with zero IA references fails. A run that does not include the Inertia Advocate as a selected reviewer passes by default. |
| C-15 | Domain-lens validity check is stated as an explicit rewrite gate, not a naming contract | aspirational | correctness | The skill must include a domain-lens validity check expressed as: (a) a binary test — "would only this role raise this finding given their domain?" — and (b) a rewrite consequence — "if any generic reviewer could write the same sentence, revise it." A specificity contract (e.g., "name the file and line") that does not include the domain-lens test fails — specificity ensures location precision, not role-domain fidelity. A skill that enforces naming precision without the explicit rewrite gate passes C-05 but fails C-15. |
| C-16 | AMEND scope disclosure is a structured block with named output fields, not prose instructions | aspirational | format | When the skill includes AMEND mode handling, the scope disclosure must be a structured output block with named fields enumerated as template slots — not a prose instruction describing what to say. The block must name at minimum: (a) what was amended, (b) which roles were added or removed, (c) which prior findings are superseded. A disclosure format expressed as prose instruction ("state what role was added, which files triggered it...") without a templated output block fails. A run in default mode passes by default. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

*aspirational denominator increased from 6 to 8 in v4; each criterion is worth 1.25 pts; a perfect run still scores 100.*

---

## What changed from v3

**C-15 closes the C-05 precision gap.** C-05 requires findings to be domain-specific, but Round 3 showed that a well-formed column contract enforcing file+line specificity can satisfy the letter of C-05 while leaving the spirit unmet: a finding naming `auth/middleware.ts:88` passes a specificity check even if any reviewer could have written it. C-15 requires the validity check to be an explicit binary question plus a rewrite instruction — not derivable from a naming rule alone. A variation that passes C-05 via specificity contract but omits the "would only this role raise this?" gate fails C-15.

**C-16 closes the C-08 consistency gap.** C-08 requires AMEND scope disclosure with three named elements. Round 3 showed that listing those elements as prose instructions ("say what role was added, which files triggered it...") leaves output format undefined — a model following prose instructions can produce a different layout each run. C-16 requires the AMEND block to be a templated structure with named fields, making the disclosure format a first-class artifact. A variation that satisfies C-08 via prose description but omits a structured template fails C-16.
