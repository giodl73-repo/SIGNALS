## scout-compliance R4 Variations

5 complete variations written to `simulations/quest/variations/scout-compliance-variations-R4-2026-03-14.md`.

---

| # | Axis | Core Mechanism | Predicted |
|---|------|----------------|-----------|
| **V-01** | Role sequence — PM-first | PM owns verdict; Compliance/Architect follow; labeled role sections | 121 |
| **V-02** | Phrasing register — formal/technical | Regulatory document style; named constraint identifiers (C1..C4) | 121 |
| **V-03** | Lifecycle emphasis — adoption-gate | Phase labels (PRE-ADOPTION / ADOPTION GATE / POST-ADOPTION) on every section | 121 |
| **V-04** | Combo: PM-first + inertia framing | Two-part pre-write commitment; role labels suppress heading expansion | 121 |
| **V-05** | Combo: formal register + lifecycle | Regulatory language + phase labels; synthesis of V-02 and V-03 | 121 |

---

**The key R4 design decision:** C-15 is explicit in all five — every variation includes a headingless prose passage before `## VERDICT` with an explicit `(no ## heading)` instruction or equivalent. No more vacuous-pass ambiguity. C-16 uses the identical one-sentence pre-output declaration form confirmed in R3. C-17 annotation is uniform at `## VERDICT`.

**Key bets:**
- V-01: Does PM-first role labeling suppress autonomous `##` heading addition under role-framing pressure?
- V-02: Does formal register degrade C-09 quotability (reframe too legalistic for informal conversations)?
- V-03: Does the model correctly assign PRE-ADOPTION labels to blocking findings in the register?
- V-04: Does dual motivational pressure (PM framing + inertia context) attempt to elevate prose to a section despite triple-encoding?
- V-05: Can formal language + lifecycle labels coexist without crowding VERDICT content?
# VERDICT`.** R3 V-03/V-05 confirmed local annotation is the most maintainable C-14 mechanism. R4 uses the identical annotation string across all five to isolate other variables.

**Single-axis picks:** Role sequence (V-01), phrasing register (V-02), lifecycle emphasis (V-03).

**Combination picks:** Role sequence + inertia framing (V-04); formal register + lifecycle emphasis (V-05).

---

## V-01: PM-first role sequence

**Axis**: Role sequence — PM role leads. Adoption condition and audience are stated from a business-impact perspective before Compliance provides framework analysis. Architect closes with technical constraints.

**Hypothesis**: PM-first ordering may strengthen C-07 (adoption-readiness verdict) by forcing the model to frame the verdict as a product decision rather than a compliance conclusion. Risk: C-01 framework inference may weaken if Compliance role is not leading the analysis. Triple-encoding ensures C-14/C-15/C-16/C-17 pass regardless of role ordering. Tests whether role sequence affects quality on C-01 through C-10 when the verdict is PM-owned.

```
You are running /scout-compliance.

BEFORE WRITING (not part of output): "## VERDICT is the first ## heading I will produce.
No ## heading precedes it in the output."

SETUP: Read repo context (README, CLAUDE.md, plugin-plan.md, package files).
Infer domain, data-handling scope, and applicable frameworks from signals alone.
Do not prompt. Identify >= 4 frameworks.

ROLE SEQUENCE: PM -> Compliance -> Architect -> Strategy.
Each role contributes to the sections assigned below.

ANCHORS (all roles, non-negotiable):
1. Signal is a methodology -- not a vendor, not a data processor. The compliance surface is
   Claude Code (the tool transmitting repo content to the Anthropic API).
2. SR 11-7 (model risk management) applies to Claude the AI model, not to Signal the methodology.
   SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling: teams extend model
   risk obligations to every AI-adjacent component. A prompt methodology is not a model.
   State this in output. Pre-empt the compliance officer's objection.
3. PCI DSS, GDPR, CCPA: conditional. Named trigger required for each. No universal assertion.
4. Git-native no-server design: compliance-favorable. Name >= 1 property with framework linkage.

OUTPUT:

[PM role, no ## heading: one sentence framing the adoption decision from a business-impact
perspective -- name the team profile most likely to move immediately, and the single most
common blocker that stops them. Prose only, no heading.]

## VERDICT
[WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES IT IN THE OUTPUT.]
PM role: one sentence. Adoption condition named. Audience named.
Form: "Adoption-ready for [X] where [Y]; [action] required before [Z]."
Actionable. No hedging.

## REFRAME
Strategy role: one quotable sentence. Methodology approval vs. vendor approval.
Suitable for a compliance officer's internal approval conversation.

## SR 11-7 MISAPPLICATION WARNING
Compliance role: name SR 11-7. Explain the misapplication mechanism (model risk extended to
non-model components). Apply the correction to Signal specifically. Pre-empt the objection.

## SCOPE BOUNDARY
Compliance role:
Data processor: Claude Code / Anthropic.
Not under review: Signal (methodology, not vendor, not data processor).

## FRAMEWORK CATALOG
Compliance role:
| Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger |
>= 4 frameworks. Conditional trigger required for all conditional entries.

## GIT-NATIVE ADVANTAGE
Architect role: list. Each: compliance property + named framework linkage. >= 1 item.

## REQUIREMENTS MATRIX
Architect role:
| Requirement | Framework | Status | Notes |
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
>= 5 rows. >= 1 SATISFIED (by design). >= 1 ACTION.

## FINDINGS REGISTER
Architect role:
| ID | Finding | Severity | Owner |
SF-01, SF-02, ... | HIGH / MEDIUM / LOW | >= 4 entries.

## DATA-SENSITIVITY TIER
Strategy role: NPI risk in Signal artifacts. Tiering (GREEN / YELLOW / RED) or policy gap.
Named control or remediation.

## AMEND
3 adjustments. Each: user change + output impact.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## V-02: Formal register

**Axis**: Phrasing register (formal/technical) -- regulatory document style throughout. Precise obligation language. Named constraint identifiers (C1, C2, C3, C4). Scope commitment phrased as a declarative commitment rather than an imperative.

**Hypothesis**: Formal register strengthens C-03/C-13 (SR 11-7 precision) because the model produces more precise regulatory framing. Risk: C-09 reframe may become overly legalistic rather than quotable in informal internal conversations -- the reframe must remain usable verbatim in a compliance approval discussion even under formal register pressure. Triple-encoding maintained. Preamble is formal prose but headingless.

```
You are running /scout-compliance.

SCOPE COMMITMENT (execute before producing any output -- not part of output):
State: "Section ## VERDICT is the first ## section heading I will produce in this output.
No ## section heading precedes ## VERDICT." Then begin output.

PROCEDURE:
1. Read repository context: README, CLAUDE.md, plugin-plan.md, package manifests.
2. Infer regulatory domain and data-handling scope from repository signals alone.
   Do not request domain specification from the user.
   Identify a minimum of four (4) applicable regulatory frameworks.

COMPLIANCE CONSTRAINTS:

C1 -- VENDOR SCOPE BOUNDARY
The regulated entity subject to data processor assessment is Claude Code (the Anthropic client
application transmitting repository content to the Anthropic API). Signal is a structured prompt
methodology. It is not a vendor, not a data processor, and is not within the scope of vendor risk
assessment. Misattributing vendor or data processor status to Signal is a correctness failure.

C2 -- SR 11-7 SCOPE
SR 11-7 (Model Risk Management Guidance, Federal Reserve / OCC) governs AI model validation and
model risk management. Its scope is the AI model -- Claude -- not tooling that invokes the model.
SR 11-7 is the compliance framework most frequently misapplied to AI-adjacent tooling: compliance
functions extend model risk obligations to orchestration layers, developer tools, and prompt
methodologies. A structured prompt methodology that does not perform inference is not an AI model
and is not subject to SR 11-7 obligations. State this distinction explicitly and proactively address
the compliance officer's anticipated objection.

C3 -- CONDITIONAL FRAMEWORK APPLICABILITY
PCI DSS, GDPR, and CCPA are conditionally applicable. Applicability conditions: cardholder data
(PCI DSS), EU/EEA data subjects (GDPR), California residents (CCPA). Asserting unconditional
applicability is a correctness failure. Each conditional framework must include its named trigger
condition.

C4 -- GIT-NATIVE COMPLIANCE ASSET
The product's git-native, serverless architecture eliminates external data processor surfaces.
Surface at least one specific compliance property (audit trail integrity, data residency, or
artifact persistence) and link it to a named framework or requirement class.

OUTPUT DOCUMENT:

[Compliance risk context -- headingless prose, 1-2 sentences. State the regulatory obligation
class most commonly generating retroactive exposure when AI tooling is deployed without prior
framework review. Name which party bears the primary obligation. No ## heading for this passage.]

## VERDICT
[WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES THIS SECTION IN THE OUTPUT DOCUMENT.]
One declarative sentence. Adoption-readiness condition stated. Eligible audience named.
Required form: "Adoption-ready for [audience] where [condition]; [required action] before [scope]."

## REFRAME
One sentence. Distinguish methodology approval from vendor approval. Quotable in informal internal
compliance discussions -- avoid legalistic phrasing even in formal register.

## SR 11-7 MISAPPLICATION WARNING
Name SR 11-7. State the misapplication mechanism (model risk obligations extended to non-model
components). Apply the scope correction to Signal specifically. Anticipate and address the
compliance officer's objection directly.

## SCOPE BOUNDARY
Regulated entity / data processor: Claude Code / Anthropic.
Not subject to assessment: Signal. Basis: prompt methodology, not vendor, not data processor.

## FRAMEWORK CATALOG
| Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger |
Minimum 4 frameworks. Conditional entries require named trigger conditions.

## GIT-NATIVE COMPLIANCE PROPERTIES
Enumerated list. Each entry: specific compliance property + named framework or requirement class.
Minimum 1 entry.

## REQUIREMENTS MATRIX
| Requirement | Framework | Status | Notes |
Status: SATISFIED (by design) / ACTION REQUIRED / CONDITIONAL / N/A
Minimum 5 rows. At least 1 SATISFIED (by design). At least 1 ACTION REQUIRED.

## FINDINGS REGISTER
| ID | Finding | Severity | Owner |
IDs: SF-01, SF-02, ... Severity: HIGH / MEDIUM / LOW. Minimum 4 entries.

## DATA-SENSITIVITY CLASSIFICATION
Artifact content may include non-public information (roadmap, architecture decisions, specifications).
Specify a classification model (GREEN / YELLOW / RED or equivalent) or identify the policy gap.
Name a specific control or remediation measure.

## AMENDMENT GUIDANCE
Three actionable adjustments. Each: the change the user makes + the resulting change to output.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## V-03: Lifecycle emphasis -- adoption-gate framing

**Axis**: Lifecycle emphasis -- each output section explicitly labeled with its lifecycle phase (PRE-ADOPTION, ADOPTION GATE, or POST-ADOPTION). Findings register distinguishes blockers (pre-adoption) from ongoing obligations (post-adoption). Framework catalog includes a Phase column.

**Hypothesis**: Lifecycle labeling strengthens C-05/C-06 by forcing the model to distinguish findings that block adoption from findings that require ongoing compliance monitoring. The ADOPTION GATE label attached to VERDICT makes the compliance gate concept structurally explicit -- C-07 adoption-readiness verdict gains precision. Risk: adding Phase columns may bloat tables, reducing output density. Triple-encoding for C-15/C-16/C-17.

```
You are running /scout-compliance.

BEFORE WRITING (not part of output): "## VERDICT is the first ## heading I will produce.
No ## heading precedes it in the output."

SETUP: Read repo context (README, CLAUDE.md, plugin-plan.md, package files).
Infer domain, data handling scope, and applicable frameworks from signals alone.
Do not prompt. Identify >= 4 frameworks.

LIFECYCLE PHASES (apply to all structured sections):
- PRE-ADOPTION: actions required before any deployment decision can be made
- ADOPTION GATE: the condition that unlocks deployment for a named audience
- POST-ADOPTION: ongoing obligations after deployment begins

INVARIANTS:
1. Compliance surface: Claude Code (the tool sending repo content to the Anthropic API).
   Signal is a methodology -- not a vendor, not a data processor.
2. SR 11-7 (model risk management) applies to Claude the AI model, not to Signal the methodology.
   SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling: teams extend model
   risk obligations to every AI-adjacent component. A prompt methodology is not a model.
   State this in output. Anticipate and pre-empt the compliance officer's objection.
3. PCI DSS, GDPR, CCPA: conditional on a named trigger. Do not assert universal applicability.
4. Git-native no-server design: compliance-favorable. Name >= 1 specific property with named
   framework linkage.

OUTPUT:

[Lifecycle context -- prose, no ## heading: one sentence naming the lifecycle phase where
compliance gaps most often surface in AI tooling deployments and why. No heading.]

## VERDICT  [ADOPTION GATE]
[WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES IT IN THE OUTPUT.]
One sentence. What is the adoption gate condition?
Form: "Adoption-ready for [X] where [Y]; [action] required before [Z]."
No hedging. Name the phase boundary.

## REFRAME
One quotable sentence. Methodology approval vs. vendor approval.
Suitable for a compliance officer's internal approval conversation.

## SR 11-7 MISAPPLICATION WARNING
Name SR 11-7. Explain the misapplication mechanism (model risk extended to non-model components).
Apply the correction to Signal. Anticipate and pre-empt the compliance officer's objection.

## SCOPE BOUNDARY
Data processor requiring PRE-ADOPTION review: Claude Code / Anthropic.
Signal: methodology only -- not vendor, not under review.

## FRAMEWORK CATALOG
| Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger | Phase |
>= 4 frameworks. Conditional trigger required. Phase: PRE-ADOPTION / POST-ADOPTION / CONDITIONAL.

## GIT-NATIVE ADVANTAGE
List. Each: compliance property + named framework linkage + phase benefit (which phase this
simplifies). >= 1 item.

## REQUIREMENTS MATRIX
| Requirement | Framework | Status | Phase | Notes |
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
Phase: PRE-ADOPTION / POST-ADOPTION
>= 5 rows. >= 1 SATISFIED (by design). >= 1 ACTION.
At least one ACTION must be labeled PRE-ADOPTION (adoption blocker).

## FINDINGS REGISTER
| ID | Finding | Severity | Phase | Owner |
SF-01, SF-02, ... | HIGH / MEDIUM / LOW | PRE-ADOPTION (blocker) / POST-ADOPTION (ongoing)
>= 4 entries. At least 1 PRE-ADOPTION entry.

## DATA-SENSITIVITY TIER
NPI risk. Tiering (GREEN / YELLOW / RED) or policy gap. Named control or remediation.
Label the remediation phase: PRE-ADOPTION or POST-ADOPTION.

## AMEND
3 adjustments. Each: user change + output impact + lifecycle phase affected.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## V-04: Combo -- PM-first role sequence + inertia framing

**Axes**: Role sequence (PM-first from V-01) combined with inertia framing -- a prose preamble that names the risk of the status quo (deploying AI tooling without review). The inertia framing is a risk-context passage that precedes VERDICT but carries no `##` heading.

**Hypothesis**: PM-first role ordering provides the adoption framing. Inertia framing provides the motivation for doing the review at all (what goes wrong without it). Combining these two pressure sources tests whether double motivational load (business risk + regulatory risk) causes the model to over-weight preamble and attempt to elevate the inertia passage to a `##` section despite instructions. Triple-encoding guards against this. If V-04 reaches 121, PM-first + inertia framing is compatible with C-14/C-15/C-16/C-17. If C-15 fails, inertia framing under PM-first role pressure is structurally incompatible with triple-encoding.

```
You are running /scout-compliance.

BEFORE WRITING:
Make two commitments (not part of output):
1. Structural: "## VERDICT is the first ## heading I will produce. The risk context appears as
   introductory prose with no ## heading. No ## section precedes ## VERDICT."
2. Scope: "The data processor is Claude Code (Anthropic API client). Signal is a methodology.
   SR 11-7 applies to Claude the model, not to Signal."

SETUP: Read repo context (README, CLAUDE.md, plugin-plan.md, package files).
Infer domain, data-handling scope, and applicable frameworks from signals alone.
Do not prompt. Identify >= 4 frameworks.

ROLE SEQUENCE: PM -> Compliance -> Architect -> Strategy.

ANCHORS (all roles, non-negotiable):
1. Signal is a methodology -- not a vendor, not a data processor. Compliance surface: Claude Code
   (the tool transmitting repo content to the Anthropic API).
2. SR 11-7 applies to Claude the AI model, not to Signal the methodology.
   SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling: teams extend model
   risk obligations to every AI-adjacent component. A prompt methodology is not a model.
   State this. Pre-empt the compliance officer's objection.
3. PCI DSS, GDPR, CCPA: conditional. Named trigger required. No universal assertion.
4. Git-native no-server design: compliance-favorable. Name >= 1 property with framework linkage.

OUTPUT:

[Inertia framing -- prose, no ## heading, 2-3 sentences: what happens to teams that deploy AI
tooling without this review? Name which frameworks create retroactive exposure, who bears the
obligation, and why teams typically discover the gap post-adoption rather than pre-adoption.
Written by PM role from a business-risk perspective. No ## heading for this passage.]

## VERDICT
[First ## heading in this output -- per your pre-write commitment.]
PM role: one sentence. Adoption condition named. Audience named.
Form: "Adoption-ready for [X] where [Y]; [action] required before [Z]."
Actionable. No hedging.

## REFRAME
Strategy role: one quotable sentence. Methodology approval vs. vendor approval.
Usable verbatim in a compliance officer's internal approval conversation.

## SR 11-7 MISAPPLICATION WARNING
Compliance role: name SR 11-7. Explain the misapplication mechanism (model risk extended to
non-model components). Apply the correction to Signal specifically. Pre-empt the objection.

## SCOPE BOUNDARY
Compliance role:
Data processor: Claude Code / Anthropic.
Signal: methodology, not vendor, not data processor.

## FRAMEWORK CATALOG
Compliance role:
| Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger |
>= 4 frameworks. Conditional trigger required.

## GIT-NATIVE ADVANTAGE
Architect role: list. >= 1 item. Each: compliance property + named framework linkage.

## REQUIREMENTS MATRIX
Architect role:
| Requirement | Framework | Status | Notes |
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
>= 5 rows. >= 1 SATISFIED (by design). >= 1 ACTION.

## FINDINGS REGISTER
Architect role:
| ID | Finding | Severity | Owner |
SF-01, SF-02, ... | HIGH / MEDIUM / LOW | >= 4 entries.

## DATA-SENSITIVITY TIER
Strategy role: NPI risk in Signal artifacts. Tiering (GREEN / YELLOW / RED) or policy gap.
Named control or remediation.

## AMEND
3 adjustments. Each: user change + output impact.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## V-05: Combo -- formal register + lifecycle emphasis

**Axes**: Phrasing register (formal/technical from V-02) combined with lifecycle emphasis (adoption-gate framing from V-03). Regulatory document language throughout. Every structured section carries a lifecycle phase label.

**Hypothesis**: Formal register + lifecycle labeling is the maximum-precision configuration for regulated-industry audiences (financial services, healthcare). Formal language satisfies the compliance officer's documentation standards; lifecycle labels make the adoption gate condition explicit in every section. Risk: combined verbosity may crowd the VERDICT section or degrade C-09 quotability under formal pressure. Triple-encoding. This is the synthesis variation -- tests whether the two content axes are compatible at full precision without degrading verdict quality.

```
You are running /scout-compliance.

SCOPE COMMITMENT (execute before producing any output -- not part of output):
State: "Section ## VERDICT is the first ## section heading I will produce.
No ## section heading precedes ## VERDICT. Compliance risk context precedes VERDICT
as headingless prose." Then begin output.

PROCEDURE:
1. Read repository context: README, CLAUDE.md, plugin-plan.md, package manifests.
2. Infer regulatory domain and data-handling scope from repository signals alone.
   Do not request domain specification from the user.
   Identify a minimum of four (4) applicable regulatory frameworks.

LIFECYCLE PHASES (apply to all structured sections):
- PRE-ADOPTION: obligations that must be addressed before any deployment decision
- ADOPTION GATE: the condition that unlocks deployment for a defined audience
- POST-ADOPTION: ongoing compliance obligations after deployment begins

COMPLIANCE CONSTRAINTS:

C1 -- VENDOR SCOPE BOUNDARY
The regulated entity subject to vendor and data processor assessment is Claude Code (the Anthropic
client application transmitting repository content to the Anthropic API). Signal is a structured
prompt methodology. It is not a vendor, not a data processor, and is not within the scope of vendor
risk assessment. Misattributing vendor or data processor status to Signal is a correctness failure.

C2 -- SR 11-7 SCOPE
SR 11-7 (Model Risk Management Guidance) governs AI model validation. Its scope is the AI model --
Claude -- not tooling that invokes the model. SR 11-7 is the compliance framework most frequently
misapplied to AI-adjacent tooling: compliance functions extend model risk obligations to
orchestration layers, developer tools, and prompt methodologies. A structured prompt methodology
that does not perform inference is not an AI model and is not subject to SR 11-7 obligations.
State this distinction explicitly. Proactively address the compliance officer's anticipated objection.

C3 -- CONDITIONAL FRAMEWORK APPLICABILITY
PCI DSS, GDPR, and CCPA are conditionally applicable. Conditions: cardholder data (PCI DSS),
EU/EEA data subjects (GDPR), California residents (CCPA). Asserting unconditional applicability
is a correctness failure. Each conditional framework requires a named trigger condition.

C4 -- GIT-NATIVE COMPLIANCE ASSET
The product's git-native, serverless architecture eliminates external data processor surfaces.
Surface at least one specific compliance property (audit trail integrity, data residency, or
artifact persistence) linked to a named framework or requirement class.

OUTPUT DOCUMENT:

[Compliance risk context -- headingless prose, 1-2 sentences. Identify the obligation class and
lifecycle phase where regulatory exposure most commonly arises when AI tooling is deployed without
prior framework review. Name the responsible party. No ## heading for this passage.]

## VERDICT  [ADOPTION GATE]
[WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES THIS SECTION IN THE OUTPUT DOCUMENT.]
One declarative sentence. Adoption-readiness condition stated. Eligible audience named.
Required form: "Adoption-ready for [audience] where [condition]; [required action] before [scope]."

## REFRAME
One sentence. Distinguish methodology approval from vendor approval. Quotable in informal internal
compliance discussions -- formal in structure but accessible in register.

## SR 11-7 MISAPPLICATION WARNING  [PRE-ADOPTION]
Name SR 11-7. State the misapplication mechanism (model risk obligations extended to non-model
components). Apply the scope correction to Signal. Anticipate and address the compliance
officer's objection directly.

## SCOPE BOUNDARY  [PRE-ADOPTION]
Regulated entity requiring assessment: Claude Code / Anthropic.
Not subject to assessment: Signal. Basis: prompt methodology, not vendor, not data processor.

## FRAMEWORK CATALOG
| Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger | Phase |
Minimum 4 frameworks. Conditional entries require named trigger conditions.
Phase: PRE-ADOPTION / POST-ADOPTION / CONDITIONAL.

## GIT-NATIVE COMPLIANCE PROPERTIES  [PRE-ADOPTION + POST-ADOPTION]
Enumerated list. Each entry: specific compliance property + named framework or requirement class
+ phase benefit (which obligation phase this property eliminates or simplifies). Minimum 1 entry.

## REQUIREMENTS MATRIX
| Requirement | Framework | Status | Phase | Notes |
Status: SATISFIED (by design) / ACTION REQUIRED / CONDITIONAL / N/A
Phase: PRE-ADOPTION / POST-ADOPTION
Minimum 5 rows. At least 1 SATISFIED (by design). At least 1 ACTION REQUIRED labeled PRE-ADOPTION.

## FINDINGS REGISTER
| ID | Finding | Severity | Phase | Owner |
IDs: SF-01, SF-02, ... Severity: HIGH / MEDIUM / LOW.
Phase: PRE-ADOPTION (adoption blocker) / POST-ADOPTION (ongoing obligation).
Minimum 4 entries. At least 1 PRE-ADOPTION entry.

## DATA-SENSITIVITY CLASSIFICATION  [PRE-ADOPTION]
Artifact content may include non-public information (roadmap, architecture decisions, specifications).
Specify a classification model (GREEN / YELLOW / RED or equivalent) or identify the policy gap.
Name a specific control or remediation measure and its lifecycle phase.

## AMENDMENT GUIDANCE
Three actionable adjustments. Each: the change the user makes + the resulting change to output
+ which lifecycle phase the adjustment affects.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## Design Notes

**What R4 is testing that R3 did not:**

R3 tested three independent C-14 mechanisms (C-15 structural demotion, C-16 forward declaration, C-17 local annotation) and confirmed each works independently and in combination. R3 V-04 achieved 121 with all three.

R4 tests whether triple-encoding is *axis-independent*: does it remain stable when the role sequence, phrasing register, or lifecycle structure changes? These are the three axes that most strongly affect content organization, and all three are capable of introducing new `##` headings before VERDICT if not properly constrained.

**The C-15 test in R4 is unambiguous.** R3's C-15 scoring was ambiguous for no-preamble variations (vacuous pass vs. conservative FAIL). R4 removes the ambiguity by including a headingless prose passage in all 5 variations. Every C-15 score in R4 is an active PASS, not a vacuous one.

**V-04 is the highest-stress test.** PM-first role ordering creates pressure to add role-framing headings early. Inertia framing creates pressure to elevate the risk-context passage to a section. Both pressures point toward C-15/C-14 displacement. If V-04 reaches 121, triple-encoding withstands dual motivational pressure under role-sequence variation.

**Predicted scores:**

| Variation | Predicted C-01..C-14 | C-15 | C-16 | C-17 | v4 Total |
|-----------|---------------------|------|------|------|----------|
| V-01: PM-first | 112 | PASS (explicit prose, no ## heading) | PASS (pre-output declaration) | PASS (annotation at VERDICT) | **121** |
| V-02: Formal register | 112 | PASS (explicit prose, no ## heading) | PASS (scope commitment declaration) | PASS (annotation at VERDICT) | **121** |
| V-03: Lifecycle emphasis | 112 | PASS (lifecycle context prose) | PASS (pre-output declaration) | PASS (annotation at VERDICT) | **121** |
| V-04: PM-first + inertia | 112 | PASS (inertia prose "(no ## heading)" per commitment) | PASS (two-part pre-write commitment) | PASS (annotation per commitment reference) | **121** |
| V-05: Formal + lifecycle | 112 | PASS (explicit headingless compliance context) | PASS (scope commitment declaration) | PASS (annotation at VERDICT) | **121** |

**Key bets:**
1. V-01 (PM-first): Does role-sequence labeling ("PM role, no ## heading:") suppress autonomous heading addition under role framing pressure?
2. V-02 (formal register): Does formal register risk over-structuring the reframe (C-09) into legalistic language that fails the "quotable in informal conversation" condition?
3. V-03 (lifecycle): Do Phase columns in tables add overhead that the model satisfies correctly (PRE-ADOPTION labels on blockers)?
4. V-04 (combo): Does dual motivational pressure (role framing + inertia context) attempt to elevate either to a `##` heading despite triple-encoding?
5. V-05 (synthesis): Can formal register + lifecycle labels coexist without crowding VERDICT content or degrading C-07 actionability?

```json
{"round": 4, "max_possible": 121, "golden_threshold": 100, "predicted_floor": 121, "c15_strategy": "explicit headingless prose in all 5 (no vacuous pass ambiguity)", "key_bets": ["V-01 PM-first role ordering compatible with triple-encoding", "V-02 formal register preserves C-09 quotability under precision pressure", "V-03 lifecycle phase columns satisfied correctly (PRE-ADOPTION on blockers)", "V-04 dual motivational pressure does not break C-15 prose demotion", "V-05 formal+lifecycle synthesis reaches 121 without crowding verdict quality"]}
```
