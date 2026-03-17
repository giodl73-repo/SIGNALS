## scout-compliance R3 Variations

Written to `simulations/quest/variations/scout-compliance-variations-R3-2026-03-14.md`.

---

### Summary

| # | Axis | Core Mechanism | Predicted Score |
|---|------|----------------|----------------|
| **V-01** | Inertia framing — C-14-safe | DEFAULT RISK as prose preamble (no `##`); VERDICT is first `##` | 112 |
| **V-02** | Lifecycle — forward declaration | One-sentence pre-commit before output: "## VERDICT is my first ## heading" | 112 |
| **V-03** | Output format — verdict annotation | Inline annotation at `## VERDICT`: "WRITE THIS FIRST. NO ## HEADING PRECEDES IT." | 112 |
| **V-04** | Combo: forward declaration + C-14-safe inertia | Pre-commit + prose risk preamble — double-encoding under adversarial register | 112 |
| **V-05** | Combo: terse R2-style + verdict annotation | R2 V-03 minimum-density body + V-03 annotation | 112 |

---

### R3 design logic

**The V-01 inertia test is the highest-stakes bet.** R2 V-05's only failure was that DEFAULT RISK was a `##` section. V-01 demotes it to prose. If the model adds a `## DEFAULT RISK` heading autonomously despite the instruction, the inertia frame is structurally incompatible with C-14 even with explicit instructions.

**V-02 tests whether the synthesis gate was over-engineered.** R2 V-02 used a full Phase 1 scratchpad to guarantee verdict primacy. A single declaration ("## VERDICT is the first ## heading I will produce") may be sufficient — lighter mechanism, same guarantee.

**V-03 and V-05 are the golden prompt candidates.** Local annotation at the `## VERDICT` entry is more maintainable than global ordering rules — future edits can't accidentally drop VERDICT from first position without touching the annotation. If V-05 (terse + annotation) reaches 112, the minimum viable prompt is ~25-30 lines.
**V-03 is the annotation test** — Named section contracts (R2 V-01 style) guaranteed C-11/C-12 via ordering alone. An inline annotation makes C-14 compliance a locally-readable property rather than a global ordering rule. Tests whether redundancy at the section level reduces displacement variance.

4. **V-04 is the high-stress combo test** — Inertia framing creates strong prose-expansion pressure that could tempt displacement. Double-encoding (pre-commitment + structural demotion) tests robustness under that pressure.

5. **V-05 finds the floor** — R2 V-03 terse reached 109 (likely 112 for V-01–V-04; V-03 is the fragility point). Adding one annotation to R2 V-03's body tests whether minimum viable instruction density can reach 112.

---

## V-01: C-14-safe inertia framing

**Axis**: Inertia framing — DEFAULT RISK motivation expressed as prose preamble (no `##` heading); `## VERDICT` is the first `##`-level heading unconditionally.

**Hypothesis**: R2 V-05 failed C-14 because DEFAULT RISK was a named `##` section that preceded VERDICT. The structural fix is a single demotion: risk motivation becomes introductory prose (no heading) immediately before `## VERDICT`. This preserves the motivational register — compliance officers reading about what goes wrong without a review — while satisfying C-14. If this works, the inertia frame is salvageable without any mechanism beyond structural demotion.

```
You are running /scout-compliance.

SETUP: Read repo context (README, CLAUDE.md, plugin-plan.md, package files).
Infer domain, data handling scope, and applicable frameworks from signals alone.
Do not prompt the user. Identify >= 4 frameworks.

INVARIANTS:
1. Compliance surface: Claude Code (the tool sending repo content to the Anthropic API).
   Signal is a methodology -- not a vendor, not a data processor. Do not assess Signal as either.
2. SR 11-7 (model risk management) applies to Claude the AI model, not to Signal the methodology.
   SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling: teams see a component
   that touches AI and extend model risk obligations to every layer of the stack. A prompt
   methodology that invokes a model is not itself a model. State this in output. Anticipate the
   compliance officer's objection before it is raised.
3. PCI DSS, GDPR, CCPA: conditional. Name the trigger for each. Do not assert universal applicability.
4. Git-native no-server design: compliance-favorable. Name >= 1 specific property, link to a
   named framework or requirement category.

OUTPUT:

Open with a brief introductory passage (no ## heading) that names the compliance risk of deploying
AI tooling without a prior framework review: which frameworks create retroactive exposure, who bears
the obligation, and why teams typically discover this post-adoption rather than pre-adoption.
2-3 sentences. This passage provides motivation context. Then write:

## VERDICT
[This is the first ## heading in this output. No ## heading precedes it.]
One sentence. Name the adoption-readiness condition and the target audience.
Form: "Adoption-ready for [X] where [Y]; [action] required before [Z]."
Actionable. No hedging.

## REFRAME
One sentence a compliance officer can quote in an internal approval conversation.
Distinguish approving a methodology from approving a vendor.

## SR 11-7 MISAPPLICATION WARNING
Name SR 11-7. Explain why it is frequently misapplied to AI-adjacent tooling (teams extend
model risk rules to non-model components). Apply the correction to Signal specifically.
Pre-empt the compliance officer's objection before it is raised.

## SCOPE BOUNDARY
Claude Code / Anthropic: data processor under review.
Signal: methodology, not a vendor, not a data processor.

## FRAMEWORK CATALOG
| Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger |
>= 4 frameworks. Conditional entries require a named trigger condition.

## GIT-NATIVE ADVANTAGE
List. Each item: compliance property + named framework or requirement linkage. >= 1 item.

## REQUIREMENTS MATRIX
| Requirement | Framework | Status | Notes |
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
>= 5 rows. >= 1 SATISFIED (by design). >= 1 ACTION.

## FINDINGS REGISTER
| ID | Finding | Severity | Owner |
IDs: SF-01, SF-02, ... | Severity: HIGH / MEDIUM / LOW | >= 4 entries.

## DATA-SENSITIVITY TIER
Does artifact content include non-public information (specs, roadmap, architecture decisions)?
Recommend a tiering model (e.g., GREEN / YELLOW / RED) or name the policy gap.
Name a specific control or remediation -- do not only flag the risk.

## AMEND
3 specific adjustments. Each: what the user changes + what changes in the output.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## V-02: Forward verdict declaration

**Axis**: Lifecycle emphasis -- a single-sentence pre-commitment step declares `## VERDICT` as the first section before the output template runs. No full scratchpad, no phase separation.

**Hypothesis**: R2 V-02's synthesis gate used a full two-phase scratchpad to guarantee verdict primacy. The load-bearing mechanism may be simpler: a one-sentence declaration ("## VERDICT is the first ## heading I will produce") made before writing starts. If this lighter pre-commitment achieves C-14 parity with the synthesis gate, the two-phase structure was over-engineered for this specific guarantee. The declaration also forces scope commitment -- SR 11-7 and vendor boundary -- before any section is drafted.

```
You are running /scout-compliance.

SETUP: Scan repo context (README, CLAUDE.md, plugin-plan.md, package files). Infer domain,
data handling, and applicable frameworks from signals alone. Do not prompt. Identify >= 4 frameworks.

BEFORE WRITING ANY OUTPUT -- make the following declarations:
"## VERDICT is the first ## heading I will produce. No ## heading precedes it."
"The data processor is [component sending data to external API]. Signal is a methodology."
"SR 11-7 applies to Claude the AI model, not to Signal the methodology."

These declarations are your scope commitment. They are not part of the output.
Verify them now, then write the output below.

ANCHORS (non-negotiable):
- Claude Code / Anthropic is the data processor. Signal is a methodology, not a vendor.
- SR 11-7 (model risk management): applies to Claude, not to Signal. SR 11-7 is the most
  commonly misapplied framework in AI-adjacent tooling: teams extend model risk obligations
  to every AI-adjacent component. A prompt methodology that invokes a model is not itself a
  model. State this in output. Pre-empt the compliance officer's objection.
- PCI DSS, GDPR, CCPA: conditional. Named trigger required for each. No universal assertion.
- Git-native no-server: compliance-favorable. Name >= 1 property with framework linkage.

OUTPUT -- sections in this order:

## VERDICT
One sentence. Audience named. Condition named.
Form: "Adoption-ready for [X] where [Y]; [action] required before [Z]."
No hedging. This is the first ## heading you produce.

## REFRAME
One quotable sentence. Methodology approval vs. vendor approval.
Suitable for a compliance officer's internal approval conversation.

## SR 11-7 MISAPPLICATION WARNING
From your pre-write declaration: name SR 11-7, describe the misapplication mechanism
(model risk extended to non-model components), apply the correction to Signal, pre-empt
the objection.

## SCOPE BOUNDARY
Data processor: Claude Code / Anthropic.
Not under review: Signal (methodology, not vendor, not data processor).

## FRAMEWORK CATALOG
| Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger |
>= 4 frameworks. Conditional trigger required for all conditional entries.

## GIT-NATIVE ADVANTAGE
Compliance properties of the no-server design. Each linked to a named framework. >= 1 item.

## REQUIREMENTS MATRIX
| Requirement | Framework | Status | Notes |
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
>= 5 rows. >= 1 SATISFIED. >= 1 ACTION.

## FINDINGS REGISTER
| ID | Finding | Severity | Owner |
SF-01, SF-02, ... | HIGH / MEDIUM / LOW | >= 4 entries.

## DATA-SENSITIVITY TIER
Artifact NPI risk. Tiering model (GREEN / YELLOW / RED) or policy gap.
Specific control or remediation -- not just the flag.

## AMEND
3 adjustments. Each: user change + output impact.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## V-03: Verdict-annotated template

**Axis**: Output format -- the `## VERDICT` entry in the output template carries an inline annotation making C-14 compliance a locally-visible, named property at the point of use.

**Hypothesis**: R2's section-contracts guaranteed C-11/C-12 via global ordering rules ("write in this exact order"). C-14 compliance in those variations was implied by position. An inline annotation ("WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES IT.") at the `## VERDICT` entry makes the requirement local and unambiguous at the exact point where it could fail. This removes reliance on the model scanning back to global ordering instructions. If this reduces variance below the R2 section-contract baseline, annotation at the point of use is the stronger mechanism.

```
You are running /scout-compliance.

SETUP: Infer domain, data scope, and applicable frameworks from repo context (README, CLAUDE.md,
plugin-plan.md, package files). Do not prompt. Identify >= 4 frameworks.

INVARIANTS:
1. Signal is a methodology -- not a vendor, not a data processor. The compliance surface is
   Claude Code (the tool sending repo content to the Anthropic API).
2. SR 11-7 applies to Claude the AI model, not to Signal the prompt methodology. SR 11-7 is
   the most commonly misapplied framework in AI-adjacent tooling: teams extend model risk
   obligations to every component that touches AI, including non-model layers. A structured
   prompt methodology is not a model. State this and pre-empt the compliance officer's objection.
3. PCI DSS, GDPR, CCPA are conditional frameworks. Each requires an explicit named trigger.
   Do not assert universal applicability.
4. Git-native no-server design is compliance-favorable. Name >= 1 specific property with
   framework linkage.

OUTPUT TEMPLATE -- write each section; requirements annotated inline:

## VERDICT
[WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES IT IN THE OUTPUT.]
One sentence. Audience named. Condition named.
Form: "Adoption-ready for [X] where [Y]; [action] required before [Z]."
Do not hedge.

## REFRAME
[quotable statement for compliance officer internal conversations]
One sentence. Methodology approval vs. vendor approval.

## SR 11-7 MISAPPLICATION WARNING
[C-13: named framework, misapplication mechanism, Signal-specific correction, objection pre-empted]
Name SR 11-7. Explain the misapplication mechanism (model risk rules extended to non-model layers).
Apply to Signal specifically. Pre-empt the objection.

## SCOPE BOUNDARY
[identifies data processor; excludes Signal from vendor scope]
Data processor: Claude Code / Anthropic.
Not under review: Signal (methodology, not vendor).

## FRAMEWORK CATALOG
[C-01: >= 4 frameworks inferred from repo signals; C-08: conditional triggers named]
| Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger |
Conditional trigger required for all conditional entries.

## GIT-NATIVE ADVANTAGE
[C-04: >= 1 compliance property of no-server design; named framework linkage]
List. Each: compliance property + framework.

## REQUIREMENTS MATRIX
[C-06: >= 5 rows; >= 1 SATISFIED by design; >= 1 ACTION]
| Requirement | Framework | Status | Notes |
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A

## FINDINGS REGISTER
[C-05: >= 4 entries with IDs and severity labels]
| ID | Finding | Severity | Owner |
SF-01, SF-02, ... | HIGH / MEDIUM / LOW

## DATA-SENSITIVITY TIER
[C-10: NPI risk identified; tiering model or policy gap; specific control or remediation]
Artifact content may include non-public information (specs, roadmap, architecture decisions).
Tiering model (GREEN / YELLOW / RED) or named policy gap. Named control or remediation.

## AMEND
[3 specific adjustments with output impact]
Each: user change + what changes in the output.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## V-04: Combo -- forward declaration + C-14-safe inertia framing

**Axes**: Lifecycle (forward declaration from V-02) combined with inertia framing (prose risk preamble from V-01). Double-encoding under adversarial conditions.

**Hypothesis**: V-01 tests whether structural demotion alone rescues the inertia frame. V-02 tests whether forward declaration alone guarantees C-14. V-04 tests whether the combination is more robust under adversarial pressure: the risk preamble creates expansion pressure that could tempt the model to add a `## DEFAULT RISK` heading despite instructions; the forward declaration is a second independent guard. If V-04 reaches 112 where V-01 or V-02 show variance, double-encoding is load-bearing under the inertia frame. If all three reach 112, single-mechanism is sufficient.

```
You are running /scout-compliance.

SETUP: Scan repo context (README, CLAUDE.md, plugin-plan.md, package files). Infer domain,
data handling scope, and frameworks from signals alone. Do not prompt. Identify >= 4 frameworks.

BEFORE WRITING:
Make two commitments:
1. Structural: "## VERDICT is the first ## heading I will produce. The risk context appears
   as introductory prose with no ## heading. No ## section precedes ## VERDICT."
2. Scope: Identify the component that sends repo content to an external API. That is the data
   processor. Signal is a methodology -- not that component, not a vendor.

Also commit your SR 11-7 position: SR 11-7 is model risk management. It applies to Claude the
AI model, not to Signal the prompt methodology. SR 11-7 is the most commonly misapplied framework
in AI-adjacent tooling -- teams extend model risk obligations to every AI-touching component.
A prompt methodology is not a model. This distinction appears as a named section in output.
Anticipate the compliance officer's objection.

ANCHORS:
- Claude Code / Anthropic: data processor. Signal: methodology, not vendor.
- PCI DSS, GDPR, CCPA: conditional. Named trigger for each. No universal assertion.
- Git-native no-server: compliance-favorable. Name >= 1 property with framework linkage.

OUTPUT:

[Introductory prose -- no ## heading -- 2-3 sentences: compliance risk of skipping this review,
which frameworks create retroactive exposure, who bears the obligation, why teams discover this
post-adoption. Written from your pre-write commitment. Then immediately:]

## VERDICT
[First ## heading in this document -- per your pre-write commitment.]
One sentence. Adoption condition. Audience named.
Form: "Adoption-ready for [X] where [Y]; [action] required before [Z]."
Actionable. No hedging.

## REFRAME
One quotable sentence. Methodology approval vs. vendor approval.
Usable verbatim in a compliance officer's internal approval conversation.

## SR 11-7 MISAPPLICATION WARNING
SR 11-7 named. Misapplication mechanism described (model risk extended to non-model components).
Signal's case applied. Objection pre-empted.

## SCOPE BOUNDARY
Data processor: Claude Code / Anthropic.
Signal: methodology, not vendor, not data processor.

## FRAMEWORK CATALOG
| Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger |
>= 4 frameworks. Conditional trigger required.

## GIT-NATIVE ADVANTAGE
List. >= 1 item. Each: compliance property + named framework linkage.

## REQUIREMENTS MATRIX
| Requirement | Framework | Status | Notes |
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
>= 5 rows. >= 1 SATISFIED (by design). >= 1 ACTION.

## FINDINGS REGISTER
| ID | Finding | Severity | Owner |
SF-01, SF-02, ... | HIGH / MEDIUM / LOW | >= 4 entries.

## DATA-SENSITIVITY TIER
NPI risk in Signal artifacts. Tiering model (GREEN / YELLOW / RED) or policy gap.
Named control or remediation.

## AMEND
3 adjustments. Each: user change + output impact.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## V-05: Combo -- terse R2-style + verdict annotation

**Axes**: Phrasing register (minimum instruction density, R2 V-03 baseline) combined with output format (inline verdict annotation from V-03 R3).

**Hypothesis**: R2 V-03 (terse imperative) reached 109/109 -- and by the v3 rubric likely reaches 112 since `## VERDICT` was already its first heading. But R2 V-03's C-13 encoding was flagged as the most fragile (terse instruction + section directive, less redundancy than V-01/V-02). V-05 takes R2 V-03's body and adds one annotation: `[WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES IT.]` at `## VERDICT`. If V-05 and R2 V-03 both score 112, annotation adds no value at terse density -- section ordering is sufficient. If V-05 scores higher under adversarial scoring, the annotation is load-bearing even at minimum density.

```
You are running /scout-compliance.

SETUP: Detect domain from repo. Infer frameworks. Do not ask anything. Identify >= 4 frameworks.

RULES:
1. Signal is not a vendor. Claude Code / Anthropic is the data processor.
2. SR 11-7 applies to Claude the model, not to Signal the methodology.
3. SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling -- explain the
   mechanism in output (teams extend model risk rules to non-model layers) and pre-empt the
   compliance officer's objection.
4. PCI DSS, GDPR, CCPA are conditional -- mark each with its trigger, do not assert universal.
5. Git-native no-server design is compliance-favorable -- name >= 1 benefit with framework link.

OUTPUT (write sections in this order):

## VERDICT
[WRITE THIS SECTION FIRST. NO ## HEADING PRECEDES IT IN THE OUTPUT.]
One sentence. Condition. Audience. Form: "Adoption-ready for [X] where [Y]; [Z] before [W]."
No hedging.

## REFRAME
One sentence. Methodology vs. vendor. Quotable.

## SR 11-7 MISAPPLICATION WARNING
Name SR 11-7. Mechanism of misapplication. Why Signal is outside scope. Objection pre-empted.

## SCOPE BOUNDARY
Claude Code / Anthropic: data processor. Signal: methodology, not vendor.

## FRAMEWORK CATALOG
| Framework | Basis | Entity | UNIVERSAL / CONDITIONAL | Trigger |
>= 4 frameworks.

## GIT-NATIVE ADVANTAGE
List. Each item: property + named framework. >= 1 item.

## REQUIREMENTS MATRIX
| Requirement | Framework | Status | Notes |
>= 5 rows. >= 1 SATISFIED. >= 1 ACTION.

## FINDINGS REGISTER
| ID | Finding | Severity | Owner |
SF-01... | HIGH / MEDIUM / LOW | >= 4 entries.

## DATA-SENSITIVITY TIER
NPI risk. Tiering (GREEN / YELLOW / RED) or policy gap. Specific control or remediation.

## AMEND
3 items. Each: change + output impact.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md
Frontmatter: skill, topic, date, skill_version, input.
```

---

## Design Notes

**What R3 is testing that R2 did not:**

R2 tested whether all aspirationals (C-11/C-12/C-13) could be structurally guaranteed across diverse axes. R2 confirmed: named sections in fixed order are both necessary and sufficient for C-11/C-12; explicit C-13 planting is necessary (general framing is insufficient); and DEFAULT RISK as a `##` section before VERDICT is a C-14 displacement fail.

R3 tests two questions:
1. Can the inertia frame be salvaged for C-14 with a structural demotion? (V-01, V-04)
2. Is the pre-commitment mechanism lighter than a full synthesis gate while still guaranteeing C-14? (V-02, V-04)
3. Does annotation at the point of use reduce variance below the global-ordering baseline? (V-03, V-05)

**Predicted scores:**

| Variation | Predicted C-14 | Expected v3 score |
|-----------|---------------|------------------|
| V-01: C-14-safe inertia | PASS | 112 |
| V-02: Forward declaration | PASS | 112 |
| V-03: Verdict annotation | PASS | 112 |
| V-04: Combo declaration + inertia | PASS | 112 |
| V-05: Terse + annotation | PASS | 112 |

All 5 are predicted to reach 112 because:
- C-01..C-10 (100 pts): all R2 invariants carried forward intact
- C-11 (3 pts): VERDICT before any framework table -- guaranteed by section ordering in all 5
- C-12 (3 pts): REFRAME and DATA-SENSITIVITY TIER as named `##` sections -- guaranteed in all 5
- C-13 (3 pts): Explicit SR 11-7 misapplication instruction present in all 5 (planted, not emergent)
- C-14 (3 pts): VERDICT is first `##` heading -- each variation has a distinct mechanism for this

**The V-01 inertia test is the highest-stakes bet.** If V-01 reaches 112, the inertia frame is fully rehabilitated by a single structural demotion. If it fails C-14 despite the annotation ("[This is the first ## heading in this output. No ## heading precedes it.]"), it means the model adds a `## DEFAULT RISK` heading autonomously under the risk-framing register -- which would be a signal that the inertia frame is structurally incompatible with C-14 even with explicit instructions.

**If V-02 (forward declaration) reaches 112 at lower complexity than R2 V-02 (synthesis gate):**
The synthesis gate was over-engineered. A one-sentence pre-commitment is the minimum viable mechanism for C-14 guarantee. This simplifies the golden prompt candidate substantially.

**If V-05 (terse + annotation) reaches 112:**
The minimum viable prompt for this skill is approximately 25-30 lines. Every additional instruction above that adds robustness but not correctness floor lift.

**R3 golden prompt candidate:** V-03 (verdict-annotated template) or V-05 (terse + annotation) -- whichever is more compact while maintaining 112. The annotation mechanism (local C-14 compliance at the point of use) is more maintainable than global ordering rules because future edits to the section order cannot accidentally drop `## VERDICT` from first position without touching the annotation.

```json
{"round": 3, "max_possible": 112, "golden_threshold": 100, "predicted_floor": 112, "key_bets": ["V-01 inertia frame rehabilitation via structural demotion", "V-02 lightweight pre-commitment vs synthesis gate", "V-03 annotation at point of use vs global ordering", "V-05 minimum viable prompt at terse density"]}
```
