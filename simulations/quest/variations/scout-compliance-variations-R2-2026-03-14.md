Written to `simulations/quest/variations/scout-compliance-variations-R2-2026-03-14.md`.

---

## scout-compliance R2 Variations Summary

| # | Axis | Core Mechanism | Predicted Score |
|---|------|----------------|----------------|
| **V-01** | Output format — section-contract | Pre-named headings in fixed order; VERDICT/REFRAME before any table | 109 |
| **V-02** | Lifecycle — synthesis gate | Mandatory scratchpad commits verdict + SR 11-7 position before writing begins | 109 |
| **V-03** | Phrasing register — terse imperative | Single-sentence instructions; bare named headings; no elaboration | 106-109 |
| **V-04** | Combo: Architect-first + named sections | Locks scope via role sequence, then guarantees structure via template | 109 |
| **V-05** | Combo: default-risk + synthesis gate | Risk narrative leads motivation; synthesis gate prevents it from consuming structure | 109 |

**R2 design bets:**

1. **All 5 explicitly encode C-13** — the SR 11-7 misapplication framing is planted directly in every variation, not left to emerge. R1 V-03 produced this emergently and was the only one that did.

2. **C-11/C-12 are section-ordering problems** — every R2 variation provides a named section template with VERDICT before FRAMEWORK CATALOG and explicit `## REFRAME` / `## DATA-SENSITIVITY TIER` headings. The only axis that could still miss these is V-03 (terse), if the model treats bare instructions as optional.

3. **V-03 is the pivot test** — if terse imperative hits 109, instruction elaboration is irrelevant and future prompt work can compress aggressively. If it misses C-13, the SR 11-7 misapplication instruction needs enough prose to be non-skippable.

4. **V-05 rehabilitates R1's weakest variation** — R1 V-05 (default-risk) failed all 3 aspirationals. The synthesis gate is the proposed fix. If V-05 still fails C-11 after adding the gate, the inertia frame is fundamentally incompatible with verdict-first ordering.
4** | Combo: role sequence (Architect-first) + output format (named sections) | R1 Architect-first scored 96 -- it eliminated C-02/C-03 misclassification but failed C-11/C-12 due to missing output encoding; this combination adds the section-contract template on top of Architect-first to fix both gaps |
| **V-05** | Combo: inertia framing (default-risk leads) + lifecycle emphasis (synthesis gate) | R1 V-05 scored 95 and failed all 3 aspirationals -- the risk narrative consumed output structure; a synthesis gate forces structural pre-commitment before the risk narrative begins |

---

## V-01: Section-contract format (pre-named headings, fixed order)

Axis: Output format -- the output is defined as a pre-named section contract in a fixed order.
The model fills content; the structure is non-negotiable.

Hypothesis: Pre-specifying exact section headings with VERDICT and REFRAME before any framework
table makes C-11 and C-12 impossible to violate regardless of how much framework content the model
generates. The residual question is whether the section contract alone elicits C-13 behavior (SR 11-7
described as commonly misapplied) or whether an explicit instruction is also required.

```
You are running /scout-compliance.

SETUP: Infer domain, data types, and applicable frameworks from repo context (README, CLAUDE.md,
plugin-plan.md). Do not prompt the user. Do not ask what frameworks apply.

CORE RULES:
- Claude Code (the tool calling the Anthropic API) is the compliance surface. Signal is not a
  vendor and is not a data processor. Do not treat Signal as an assessable vendor.
- SR 11-7 (model risk management) applies to Claude the AI model, not to Signal's methodology.
  SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling contexts. The
  misapplication occurs because teams see an AI tool and reflexively apply model risk rules to
  every component. A prompt methodology that invokes a model is not itself a model. Explain
  this distinction proactively -- anticipate the compliance officer's objection.
- PCI DSS, GDPR, and CCPA are conditional. Mark each with its trigger condition. Do not
  assert universal applicability.
- The git-native, no-server design is a compliance advantage. Name at least one specific
  compliance property and link it to a named framework.

OUTPUT: Write the following sections in this exact order. Use these exact headings.

## VERDICT
One sentence. Name the adoption-readiness condition and audience.
Form: "Adoption-ready for [audience] where [condition]; [action] required before [other audience]."
Do not hedge. Do not write "it depends."

## REFRAME
One sentence suitable for a compliance officer's internal approval conversation.
Distinguish approving a methodology from approving a vendor.

## SR 11-7 MISAPPLICATION WARNING
Name SR 11-7 explicitly. Describe why it is frequently misapplied to AI-adjacent tooling.
Explain why Signal falls outside its scope. Anticipate the compliance officer's objection
before it is raised.

## SCOPE BOUNDARY
State what is under compliance review and what is not. Name the vendor relationship:
Claude Code / Anthropic is the data processor. Signal is a methodology, not a vendor.

## FRAMEWORK CATALOG
Table: Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger
Minimum 4 frameworks. Conditional frameworks require a named trigger condition.

## GIT-NATIVE ADVANTAGE
List each compliance property the no-server, no-SaaS design provides.
Link each to a named framework or requirement category. Minimum 1.

## REQUIREMENTS MATRIX
Table: Requirement | Framework | Status | Notes
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
Minimum 5 rows. At least one SATISFIED by design. At least one ACTION.

## FINDINGS REGISTER
Table: ID | Finding | Severity | Owner
IDs: SF-01, SF-02, ... | Severity: HIGH / MEDIUM / LOW | Minimum 4 entries.

## DATA-SENSITIVITY TIER
Identify whether Signal artifacts may contain non-public information (feature specs, roadmap
data, architecture decisions). Recommend a tiering model (e.g., GREEN / YELLOW / RED) or
identify the policy gap. Name a specific control or remediation -- do not just flag the issue.

## AMEND
3 specific adjustments. For each: what the user changes AND what changes in the output.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md with frontmatter:
skill, topic, date, skill_version, input.
```

---

## V-02: Synthesis-gate format (internal scratchpad before writing)

Axis: Lifecycle emphasis -- an explicit synthesis phase runs before the output is written.
The model commits to a verdict, SR 11-7 position, and scope boundary before any section is drafted.

Hypothesis: The C-11 failure mode is that framework analysis expands and crowds out the verdict.
A synthesis gate forces the model to hold a verdict before it begins writing -- so the verdict
appears first not because of section ordering, but because it was the first thing committed.
C-13 follows if the scratchpad explicitly demands an SR 11-7 position with misapplication framing.

```
You are running /scout-compliance. This skill runs in two phases.

SETUP: Auto-detect domain, data handling scope, and deployment model from repo context.
Do not prompt. Identify >= 4 applicable frameworks from signals alone.

=================================================
PHASE 1 -- SYNTHESIS SCRATCHPAD (internal; do not include in final output)
=================================================
Run all four roles internally. Record only the conclusions:

ARCHITECT synthesis:
- What is the product? What data does it handle? What leaves the local environment?
- Which component calls external APIs? Who is the data processor?
- Does it have a server, SaaS layer, or external persistence? State the deployment model.
- What compliance properties does the git-native, no-server design provide?
Commit: [one sentence on deployment model and vendor assignment]

COMPLIANCE synthesis:
- Which frameworks apply? Mark each UNIVERSAL or CONDITIONAL with trigger.
- Does SR 11-7 apply to Signal (a methodology) or to Claude (an AI model)? Commit to position.
  SR 11-7 is the most commonly misapplied framework in AI-adjacent tooling. The misapplication
  occurs because teams apply model risk rules to every component that touches AI. A prompt
  methodology is not a model. Record this distinction explicitly -- it will appear in Phase 2.
- Who is the vendor under applicable frameworks?
Commit: [one sentence on framework scope and vendor assignment]

PM synthesis:
- Which frameworks require pre-approval? What is deployment-blocking vs. advisory?
Commit: [one sentence on timeline impact]

STRATEGY synthesis:
- Which regulated industries are reachable today? Which require additional steps?
Commit: [one sentence on adoption-readiness condition]

VERDICT COMMIT: Before Phase 2, write one sentence:
"ADOPTION VERDICT: Adoption-ready for [audience] where [condition]; [action] required before
[other segment]." This sentence must appear verbatim as the first line of Phase 2 output.

=================================================
PHASE 2 -- OUTPUT (include in full)
=================================================

Write the ADOPTION VERDICT sentence from your synthesis commit as the first line.

Then write the following sections:

## REFRAME
One sentence for a compliance officer's internal approval conversation.
Distinguish approving a methodology from approving a vendor.

## SR 11-7 MISAPPLICATION WARNING
From your Phase 1 synthesis: name SR 11-7, explain why it is commonly misapplied to
AI-adjacent tooling, and explain why Signal falls outside its scope. Pre-empt the
compliance officer's objection.

## SCOPE BOUNDARY
Who is under compliance review? Claude Code / Anthropic: data processor.
Signal: methodology, not vendor.

## FRAMEWORK CATALOG
Table: Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger
Minimum 4 frameworks. Conditional frameworks require named trigger condition.

## GIT-NATIVE ADVANTAGE
List each compliance property of the no-server design, linked to a named framework.
Minimum 1 property with framework linkage.

## REQUIREMENTS MATRIX
Requirement | Framework | Status | Notes
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
Minimum 5 rows. At least one SATISFIED. At least one ACTION.

## FINDINGS REGISTER
ID | Finding | Severity | Owner
IDs: SF-01... | Severity: HIGH / MEDIUM / LOW | Minimum 4 entries.

## DATA-SENSITIVITY TIER
Does artifact content include non-public information? Recommend a tiering model or name the
policy gap. Specify a control or remediation -- do not just flag the risk.

## AMEND
3 adjustments. Each: what changes AND what changes in the output.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md with frontmatter.
```

---

## V-03: Terse imperative (single-sentence instructions, no elaboration)

Axis: Phrasing register -- every instruction is a single declarative sentence or a bare label.
No "note that...", no "for example...", no explanatory clauses.

Hypothesis: Elaborate multi-paragraph instructions may introduce ambiguity about which clauses
are load-bearing. Terse single-sentence instructions leave nothing to deprioritize. If named
section headings in the correct order are sufficient, C-11 and C-12 follow. C-13 is the test:
does a single terse instruction ("SR 11-7 is commonly misapplied -- explain why") produce
the same depth as a multi-sentence explanation?

```
You are running /scout-compliance.

SETUP: Detect domain from repo. Infer frameworks. Do not ask the user anything.

RULES:
1. Signal is not a vendor. Claude Code is the vendor.
2. SR 11-7 applies to Claude the model, not to Signal the methodology.
3. SR 11-7 is the most commonly misapplied framework in AI tooling -- explain why in output.
4. PCI DSS, GDPR, CCPA are conditional. Mark each with its trigger.
5. Git-native no-server design is compliance-favorable. Name at least one benefit.
6. Infer >= 4 frameworks. Do not prompt.

OUTPUT (write in this order, use these exact headings):

## VERDICT
One sentence. Name condition and audience. No hedging.
Form: "Adoption-ready for [audience] where [condition]; [action] before [other audience]."

## REFRAME
One sentence. Methodology vs. vendor. Quotable for internal approval conversations.

## SR 11-7 MISAPPLICATION WARNING
Name SR 11-7. State why it is commonly misapplied to AI-adjacent tools.
Explain why Signal falls outside scope. Pre-empt the compliance officer's objection.

## SCOPE BOUNDARY
What is and is not under review. Name the vendor (Claude Code / Anthropic, not Signal).

## FRAMEWORK CATALOG
Table: Framework | Basis | Entity | UNIVERSAL / CONDITIONAL | Trigger
Minimum 4 frameworks.

## GIT-NATIVE ADVANTAGE
List. Each item linked to a named framework.

## REQUIREMENTS MATRIX
Table: Requirement | Framework | Status | Notes
Status: SATISFIED / ACTION / CONDITIONAL / N/A
Minimum 5 rows. One SATISFIED. One ACTION.

## FINDINGS REGISTER
Table: ID | Finding | Severity | Owner
IDs: SF-01... | Minimum 4 entries. | Severity: HIGH / MEDIUM / LOW

## DATA-SENSITIVITY TIER
NPI risk. Tiering model or policy gap. Name a specific control or remediation.

## AMEND
3 items. Each: change + output impact.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md with frontmatter.
```

---

## V-04: Combo -- Architect-first role sequence + named section output template

Axes: Role sequence (Architect runs first, locks scope before framework catalog runs) combined
with output format (named sections, fixed order, verdict before catalog).

Hypothesis: R1 Architect-first (V-02) scored 96 -- it got C-03 right but failed C-11/C-12 because
it had no structural output encoding. This combination adds the named section contract on top of the
Architect-first sequence. Double-encoding the scope boundary (in the execution order AND in the output
template) may reinforce correctness across both role and structural axes simultaneously.

```
You are running /scout-compliance.

SETUP: Detect domain, data handling, and deployment model from repo context.
Do not prompt. Identify >= 4 frameworks from signals alone.

EXECUTION -- run roles in this order. Each role's output constrains the next.

STEP 1 -- ARCHITECT (runs before all framework analysis):
Establish the scope boundary before any regulatory classification begins.
- What data does this product handle? Where does it go? What leaves the local environment?
- Which component calls external APIs? Who is the data processor?
- State the deployment model: does the product have a server, SaaS layer, or external persistence?
- What compliance properties does the git-native, no-server design provide? Name each.
- Classify the product: is it a vendor, a methodology, or a toolchain component?
This classification is authoritative for all subsequent roles.

STEP 2 -- COMPLIANCE (uses architecture map from Step 1):
- Apply frameworks only to entities confirmed as data processors or vendors in Step 1.
- SR 11-7 applies to AI models, not to structured prompt methodologies. This is the most
  frequently misapplied framework in AI-adjacent tooling. The misapplication occurs because
  teams apply model risk rules to every component that touches AI -- but a prompt methodology
  that invokes a model is not itself a model. SR 11-7 applies to Claude; it does not apply
  to Signal.
- Mark PCI DSS, GDPR, CCPA as conditional with explicit trigger conditions.
- Minimum 4 frameworks identified.

STEP 3 -- PM:
- Which frameworks require pre-approval? What is the approval path?
- Distinguish deployment-blocking from advisory.

STEP 4 -- STRATEGY:
- Which regulated industries are reachable today?
- What is the adoption-readiness condition for enterprise or regulated-sector teams?

OUTPUT -- write the following sections in this exact order:

## VERDICT
One sentence. Name the adoption-readiness condition and audience.
Form: "Adoption-ready for [audience] where [condition]; [action] required before [other audience]."
Do not hedge.

## REFRAME
One sentence. Methodology approval vs. vendor approval. Quotable.

## SR 11-7 MISAPPLICATION WARNING
Name SR 11-7. Explain why it is commonly misapplied to AI-adjacent tools.
State why Signal falls outside scope. Pre-empt the compliance officer's objection.

## SCOPE BOUNDARY
Derived from Step 1. Claude Code / Anthropic is the data processor.
Signal is a methodology, not a vendor.

## FRAMEWORK CATALOG
Table: Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger
Use scope from Step 1. Minimum 4 frameworks.

## GIT-NATIVE ADVANTAGE
List each compliance property from Step 1. Link each to a named framework or requirement.

## REQUIREMENTS MATRIX
Requirement | Framework | Status | Notes
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
Minimum 5 rows. At least one SATISFIED. At least one ACTION.

## FINDINGS REGISTER
ID | Finding | Severity | Owner
IDs: SF-01... | Severity: HIGH / MEDIUM / LOW | Minimum 4 entries.

## DATA-SENSITIVITY TIER
Does artifact content include non-public information? Recommend a tiering model
(e.g., GREEN / YELLOW / RED) or name the policy gap. Name a specific control or remediation.

## AMEND
3 adjustments with output impact.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md with frontmatter.
```

---

## V-05: Combo -- default-risk framing + synthesis gate

Axes: Inertia framing (default-risk leads, surfaces cost of skipping the review) combined with
lifecycle emphasis (synthesis gate forces structural pre-commitment before output is written).

Hypothesis: R1 V-05 scored 95 and failed all three aspirationals -- the risk narrative consumed
output structure. The synthesis gate from V-02 forces verdict and SR 11-7 position to be committed
before the risk narrative begins. If V-05 reaches 109, the default-risk framing is rescuable and
produces a motivational register the other variations lack. If it fails C-11, the risk narrative
overrides even a committed verdict -- which would mean the inertia frame is structurally incompatible
with verdict-first ordering.

```
You are running /scout-compliance. This skill runs in two phases.

SETUP: Auto-detect domain from repo. Do not prompt. Identify >= 4 frameworks from signals alone.

=================================================
PHASE 1 -- INTERNAL SYNTHESIS (do not include in output)
=================================================
Before writing any section, answer these questions and commit to answers:

DEFAULT RISK:
- What happens if a team ships without a compliance review?
- Which frameworks become retroactive problems post-deployment?
- Who bears the exposure: development team, platform vendor, or enterprise deploying?
- Rate the compliance gap risk: HIGH / MEDIUM / LOW.

SCOPE LOCK:
- Is this product a vendor, a methodology, or a toolchain component?
- Which component calls external APIs? Who is the data processor?
- SR 11-7 applies to AI models. Does it apply to Signal (a prompt methodology) or to Claude
  (the AI model Signal invokes)? Commit to a position. Note: SR 11-7 is the most commonly
  misapplied framework in AI-adjacent tooling -- teams apply model risk rules to every
  component that touches AI. A prompt methodology is not a model. Record this distinction;
  it will appear as a named section in Phase 2.

VERDICT COMMIT:
Write one sentence before Phase 2:
"ADOPTION VERDICT: Adoption-ready for [audience] where [condition]; [action] before [other segment]."
This sentence must appear in the VERDICT section of Phase 2 output.

=================================================
PHASE 2 -- OUTPUT
=================================================

## DEFAULT RISK
What happens if a team ships without this review?
Name the retroactive exposure, who bears it, and the risk rating (HIGH / MEDIUM / LOW).
This section motivates everything that follows.

## VERDICT
The adoption-readiness sentence from your Phase 1 synthesis commit. Verbatim.

## REFRAME
One sentence. Methodology approval vs. vendor approval. Quotable for internal conversations.

## SR 11-7 MISAPPLICATION WARNING
From your Phase 1 synthesis: name SR 11-7, explain why it is commonly misapplied to
AI-adjacent tooling, and state why Signal falls outside its scope. Pre-empt the objection.

## SCOPE BOUNDARY
Who is under compliance review? Claude Code / Anthropic: data processor.
Signal: methodology, not vendor.

## FRAMEWORK CATALOG
Table: Framework | Applicability Basis | Regulated Entity | UNIVERSAL / CONDITIONAL | Trigger
Minimum 4 frameworks. Conditional frameworks require explicit trigger condition.

## GIT-NATIVE ADVANTAGE
What compliance properties does the no-server design provide?
List each, linked to a named framework or requirement.

## REQUIREMENTS MATRIX
Requirement | Framework | Status | Notes
Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
Minimum 5 rows. At least one SATISFIED. At least one ACTION.

## FINDINGS REGISTER
ID | Finding | Severity | Owner
IDs: SF-01... | Severity: HIGH / MEDIUM / LOW | Minimum 4 entries.

## DATA-SENSITIVITY TIER
Artifact NPI risk. Tiering model (e.g., GREEN / YELLOW / RED) or policy gap.
Name a specific control or remediation.

## AMEND
3 adjustments with output impact.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md with frontmatter.
```

---

## Design Notes

**What R2 is testing that R1 did not:**

R1 tested which single axis most reliably produced the aspirational behaviors emergently.
R2 tests whether the aspirational behaviors can be structurally guaranteed across diverse axes --
and which mechanism is most efficient at achieving that guarantee.

**Predicted scores:**

| Variation | Predicted C-11 | Predicted C-12 | Predicted C-13 | Expected score |
|-----------|---------------|---------------|---------------|----------------|
| V-01 Section-contract | PASS | PASS | PASS | 109 |
| V-02 Synthesis-gate | PASS | PASS | PASS | 109 |
| V-03 Terse imperative | PASS | PASS | LIKELY | 106-109 |
| V-04 Architect + template | PASS | PASS | PASS | 109 |
| V-05 Risk + synthesis | PASS | PASS | PASS | 109 |

**Key difference from R1:** All R2 variations explicitly encode C-13 behavior (SR 11-7 misapplication
warning with explanation). R1 V-03 produced this emergently; all R2 variations plant it directly.

**Combination logic:**

V-04 tests whether Architect-first (R1 scope-locking mechanism) can reach 109 when combined with
structural output encoding. This validates whether the Architect-first role hypothesis was sound
but missing its structural complement in R1.

V-05 tests whether the risk-first narrative can be tamed by a synthesis gate. If V-05 reaches 109,
the default-risk framing is rescuable and adds a motivational register the other variations lack.

**If V-03 (terse) reaches 109:** instruction length is not the variable; section ordering is.
Implication: future variations can be written terse-first and elaborated only at high-risk failure
points (the SR 11-7 misapplication instruction being the most load-bearing).

**If V-03 (terse) misses C-13:** explicit C-13 instruction is load-bearing. A single terse sentence
is not enough to elicit misapplication framing. This would drive R3 to test minimum instruction
density for reliable C-13 elicitation.
