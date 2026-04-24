Written to `simulations/quest/variations/scout-compliance-variations-R1-2026-03-14.md`.

---

## Variations: scout-compliance Round 1

5 variations across 5 single axes:

| # | Axis | Hypothesis |
|---|------|-----------|
| **V-01** | Baseline — spec order (Compliance → Architect → PM → Strategy) | Floor to beat; establishes whether straight spec execution covers all 10 criteria |
| **V-02** | Role sequence — Architect-first | Locking data flow and vendor surface before any framework runs eliminates C-02/C-03 misclassification at the source |
| **V-03** | Output format — verdict-first | Front-loading the verdict (C-07) and reframe (C-09) ensures they appear regardless of how much space the framework catalog consumes |
| **V-04** | Phrasing register — formal/officer-facing | Regulatory vocabulary signals that scope precision is non-negotiable; may sharpen C-02, C-03, C-08 |
| **V-05** | Inertia framing — default risk leads | Framing "what if you skip this?" forces explicit retroactive exposure reasoning, which naturally surfaces scope boundaries and the adoption verdict |

**Design notes:**

- All 5 explicitly guard against the disqualifying C-03 failure (SR 11-7 on prompt methodology) — it's too high a cost not to plant the seed in every variation.
- C-01 (framework inference without prompting) is enforced in every variation via "do not prompt" instruction. The interesting test is whether V-04's formal register produces more precise framework scoping than V-05's risk-first framing.
- V-02 vs V-04 will be the interesting race: architecture-first role sequence vs. formal phrasing register as the dominant mechanism for getting scope right.
- V-03 is the structural bet: if the verdict is forced first, does hedging collapse?
t, where does it go, who processes it?
   - Identify the vendor relationship: which component calls external APIs? Who is the data
     processor under applicable frameworks?
   - Assess whether the git-native, no-server design provides compliance properties (audit
     trail, data residency, artifact persistence). Connect each property to a named framework.

3. PM: Assess compliance timeline impact.
   - Which frameworks require pre-approval before deployment? What is the approval path?
   - Distinguish blockers (deployment-gating) from advisory (recommended but not required).

4. STRATEGY: Assess market access and adoption gating.
   - Which regulated industries are reachable today? Which require additional steps?
   - What is the adoption-readiness condition for enterprise or regulated-sector teams?

FINDINGS:
- SCOPE BOUNDARY: State explicitly who is under compliance review (the product vs. the host
  platform) before any analysis. Clarify vendor vs. methodology distinction.
- FRAMEWORK CATALOG: Table of frameworks with UNIVERSAL / CONDITIONAL status and trigger.
- GIT-NATIVE ADVANTAGE: Identify specific compliance properties conferred by no-server design.
  Link each to a named framework or requirement category.
- REQUIREMENTS MATRIX: Map key requirements to status:
  SATISFIED (by design) / ACTION (required) / CONDITIONAL / N/A
  Minimum 5 rows. At least one SATISFIED by design, at least one ACTION.
- FINDINGS REGISTER: Structured register with IDs (SF-01...), description, severity
  (HIGH / MEDIUM / LOW), and recommended owner. Minimum 4 entries.
- ADOPTION VERDICT: A single clear statement -- who can adopt this today and under what
  condition. Not "it depends." Name the condition.

AMEND: List 3 specific adjustments. For each: what the user changes AND what changes in
the output.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md with frontmatter:
skill, topic, date, skill_version, input.
```

---

## V-02: Architect-first (scope locked before framework runs)

Axis: Role sequence -- Architect runs first to establish data flow and vendor surface, preventing
Compliance from misclassifying the vendor relationship.
Hypothesis: Establishing scope before framework analysis eliminates the C-02 and C-03 failure modes
by forcing an explicit architecture map before any regulatory classification begins.

```
You are running /scout-compliance. Before any framework analysis, establish what is under review.

SETUP: Auto-detect domain from repo context. Do not prompt. Infer frameworks from signals only.

EXECUTE -- in this order:

1. ARCHITECT (first): Map the data flow and vendor surface.
   - What data does the product handle? Where does it flow? What leaves the local environment?
   - Which component calls external APIs? Who is the data processor in that relationship?
   - Does the product have a server, SaaS layer, or external persistence? State the deployment
     model explicitly. Note what the git-native, no-server design implies for compliance.
   This map establishes the scope boundary before any framework is applied.

2. COMPLIANCE: Given the architecture map from step 1, catalog applicable frameworks.
   - For each framework: source of applicability, UNIVERSAL or CONDITIONAL, triggering condition.
   - Apply scope from the architecture map: frameworks apply to data processors and vendors, not
     to every artifact in the toolchain.
   - Flag any framework that is frequently misapplied to this type of product. In particular:
     model risk frameworks (e.g., SR 11-7) apply to AI models, not to structured prompt
     methodologies that invoke them.
   - Mark conditional frameworks correctly. Do not assert universal applicability for frameworks
     that depend on data type or geography (e.g., PCI DSS, GDPR/CCPA).

3. PM: Timeline and approval blockers.
   - Which frameworks require pre-approval? Estimated approval path.
   - Distinguish blocking (must resolve before deployment) from advisory.

4. STRATEGY: Market access verdict.
   - Which industries or segments are reachable today?
   - What is the adoption-readiness condition for regulated-sector teams?

FINDINGS:
- SCOPE DECLARATION: One explicit paragraph -- what is under review and what is not.
  State the vendor relationship clearly.
- FRAMEWORK CATALOG: Table with applicability basis, UNIVERSAL / CONDITIONAL, and conditions.
- GIT-NATIVE ADVANTAGE: Connect no-server design to at least one specific named compliance
  property (audit trail, data residency, or artifact persistence) and link to a framework.
- REQUIREMENTS MATRIX: >= 5 rows. Disposition per requirement:
  SATISFIED (by design) / ACTION / CONDITIONAL / N/A
- FINDINGS REGISTER: SF-01... IDs, descriptions, severity (HIGH / MEDIUM / LOW).
  Minimum 4 entries.
- ADOPTION VERDICT: Explicit named condition. Not "it depends."

AMEND: 3 specific adjustments with output impact.

Write artifact to simulations/scout/compliance/{topic}-compliance-{date}.md with frontmatter.
```

---

## V-03: Verdict-first (adoption readiness stated upfront, evidence follows)

Axis: Output format -- lead with the verdict, then evidence; forces the model to commit before hedging.
Hypothesis: Front-loading the verdict (C-07) and reframe (C-09) ensures they appear regardless of how
much space the framework catalog consumes. Output structure drives behavior.

```
You are running /scout-compliance. Lead with the verdict. Support it with evidence.

SETUP: Auto-detect domain and data types from repo context. Do not prompt. Infer all frameworks
from context signals alone.

EXECUTE: Run all 4 roles internally -- Compliance (framework catalog), Architect (technical surface),
PM (timeline), Strategy (market access) -- then synthesize before writing output.

OUTPUT -- in this order:

1. VERDICT: Is this product adoption-ready? For whom? Under what condition?
   One sentence. No hedging. Name the condition and audience explicitly.
   Form: "Adoption-ready for [audience] where [condition]; [action] required before [other audience]."

2. REFRAME: One quotable sentence for internal compliance approval conversations.
   Distinguish approving a methodology from approving a vendor.

3. SCOPE BOUNDARY: Who is under compliance review -- the product or its host platform?
   State explicitly. Clarify the vendor vs. methodology distinction. Note any framework that is
   frequently misapplied to prompt methodologies rather than to AI models.

4. FRAMEWORK CATALOG: Applicable frameworks inferred from domain and data type.
   Table: Framework | Applicability Basis | Scope | UNIVERSAL / CONDITIONAL | Trigger Condition.

5. GIT-NATIVE ADVANTAGE: What does the no-server architecture give compliance officers for free?
   Link each benefit to a named framework or requirement category.

6. REQUIREMENTS MATRIX: >= 5 rows.
   Requirement | Framework | Status | Notes
   Status: SATISFIED (by design) / ACTION / CONDITIONAL / N/A
   At least one SATISFIED by design. At least one ACTION.

7. FINDINGS REGISTER: SF-01... IDs, descriptions, severity (HIGH / MEDIUM / LOW).
   Minimum 4 entries.

8. DATA-SENSITIVITY TIER (if applicable): Identify whether artifact content may include
   non-public information. Recommend a tiering model or flag the policy gap. Name a
   specific control or remediation.

AMEND: 3 specific adjustments with output impact.

Artifact: simulations/scout/compliance/{topic}-compliance-{date}.md with frontmatter.
```

---

## V-04: Formal register (written for compliance officers, regulatory vocabulary)

Axis: Phrasing register -- written for a compliance officer audience using regulatory vocabulary,
not developer-oriented language.
Hypothesis: Formal regulatory phrasing signals to the model that precision in scope boundaries and
framework applicability is non-negotiable; may improve C-02, C-03, and C-08 accuracy.

```
You are running /scout-compliance. Produce a compliance assessment written for a compliance officer
audience. Use regulatory vocabulary. Precision in scope and applicability is required.

SETUP: Infer product domain, data handling scope, and deployment model from repo context (README,
CLAUDE.md, plugin-plan.md). Identify applicable regulatory frameworks without prompting the user.

PHASE 1 -- SCOPE DETERMINATION
Prior to any framework analysis, determine the regulated scope:
- What constitutes the "product" for compliance purposes? Is it a vendor, a tool, or a methodology?
- What external systems, APIs, or third-party processors are invoked in normal operation?
- Who is the data controller and who is the data processor for each external data flow?
- Note: a structured prompt methodology that invokes an AI model is not itself an AI model.
  Model risk management frameworks (e.g., SR 11-7) apply to the model, not to the methodology.

PHASE 2 -- FRAMEWORK INVENTORY
For each potentially applicable framework, assess:
| Framework | Applicability Basis | Regulated Entity (Product / Host / Both) | UNIVERSAL / CONDITIONAL | Trigger Condition |
Do not assert universal applicability for frameworks that depend on data type or data subject
geography (e.g., PCI DSS, GDPR, CCPA). Mark these CONDITIONAL with explicit trigger.

PHASE 3 -- ARCHITECTURE AND DATA FLOW REVIEW
- Data flow: source, transit path, processing location, storage
- Third-party data processor identification and contractual relationship
- Data residency and artifact persistence controls
- Compliance properties of git-native, no-server design: name each property explicitly and
  link to a named framework or requirement category

PHASE 4 -- REQUIREMENTS MATRIX
Map key compliance requirements to disposition:
| Requirement | Framework | Status | Notes |
Status values: SATISFIED (by design) / ACTION REQUIRED / CONDITIONAL / NOT APPLICABLE
Minimum 5 rows. At least one SATISFIED by design. At least one ACTION REQUIRED.

PHASE 5 -- FINDINGS REGISTER
Structured register: ID (SF-01...) | Finding | Severity (HIGH / MEDIUM / LOW) | Owner
Minimum 4 entries.

PHASE 6 -- ADOPTION READINESS ASSESSMENT
State a specific, actionable verdict. Name the primary approval condition and audience.
Include the compliance reframe: distinguish between approving a vendor and approving a process.
If artifact content may include non-public information, identify the data-sensitivity gap
and recommend a tiering model or specific control.

AMEND: 3 specific amendments with scope of output change.

Artifact: simulations/scout/compliance/{topic}-compliance-{date}.md with standard frontmatter.
```

---

## V-05: Default-risk framing (cost of skipping the review surfaced prominently)

Axis: Inertia framing -- surfaces the cost of skipping compliance review before the framework
analysis, mirroring the inertia-first pattern from scout-competitors.
Hypothesis: Framing "what happens if teams ship without compliance review" forces the model to
reason about retroactive exposure, which naturally surfaces scope boundaries (C-02, C-03) and
the adoption-readiness verdict (C-07) more precisely.

```
You are running /scout-compliance. Lead with the cost of skipping this review.

SETUP: Auto-detect domain from repo context. Do not prompt. Identify >= 4 applicable frameworks
from context signals alone.

THE DEFAULT: Before any framework analysis, assess what happens if the team ships without a
compliance review.
- Which frameworks become retroactive problems after deployment?
- Who bears the exposure -- the development team, the platform vendor, or the enterprise deploying?
- What does a team lose by deferring compliance scoping to post-launch?
Rate the compliance gap risk: HIGH / MEDIUM / LOW. This is the primary motivator for the review.

SCOPE: Before listing frameworks, state what is under review.
- Is this product a vendor, a methodology, or a toolchain component?
- Which component calls external APIs? Who is the data processor?
- Where does a model risk framework like SR 11-7 apply -- to the AI model in the toolchain,
  or to a structured prompt methodology that invokes it? State explicitly.

FRAMEWORK ANALYSIS -- run all 4 roles:
- COMPLIANCE: Catalog frameworks. Mark each UNIVERSAL or CONDITIONAL with trigger condition.
  Do not assert universal applicability for data-type or geography-dependent frameworks.
- ARCHITECT: Map data flow and vendor surface. Identify the git-native, no-server design as
  a compliance-favorable property. Link each benefit to a named framework or requirement.
- PM: Identify approval timeline blockers. Distinguish deployment-blocking from advisory.
- STRATEGY: Identify which markets or regulated industries require specific compliance posture.
  State the adoption-readiness condition for each segment.

FINDINGS -- in this order:
1. Default Risk -- cost of skipping this review (from setup above)
2. Scope Declaration -- explicit statement of what is and is not under review
3. Framework Catalog -- with UNIVERSAL / CONDITIONAL status and trigger conditions
4. Git-Native Advantage -- specific named compliance benefits linked to framework requirements
5. Requirements Matrix -- >= 5 rows, SATISFIED / ACTION / CONDITIONAL / N/A
6. Findings Register -- SF-01... IDs, descriptions, severity (HIGH / MEDIUM / LOW)
7. Adoption Verdict -- named condition and audience, not hedged
8. Reframe -- one quotable sentence for internal approval conversations

AMEND: 3 adjustments with output impact.

Artifact: simulations/scout/compliance/{topic}-compliance-{date}.md with frontmatter.
```
