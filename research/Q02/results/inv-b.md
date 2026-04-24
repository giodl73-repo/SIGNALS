# Q02 Experiment (b) -- Per-Namespace Lifecycle Test

**Date**: 2026-03-14
**Method**: Design analysis -- 3 personas per namespace evaluate namespace-specific lifecycle
**Question**: Does each namespace's lifecycle feel natural, or is the 4-phase pattern forced?

---

## Summary

The 4-phase lifecycle (setup, execute, findings, amend) fits naturally for namespaces where the work is inherently multi-step and the output requires synthesis -- `/review:`, `/trace:`, `/flow:`, and `/prove:` all scored 4.0+ on natural fit. These namespaces map cleanly because their real-world workflows already have distinct phases: gather context, do analysis, synthesize results, iterate on feedback. The lifecycle is not imposing structure -- it is naming structure that already exists.

The lifecycle fits less naturally for namespaces where the user wants speed to a single artifact -- `/scout:` and `/draft:` both had personas who felt the 4-phase model adds ceremony to what should be a fast, single-output operation. PM personas in particular want to go from question to answer without stopping to confirm scope or review intermediate findings. The lightweight versions rescued these namespaces, but the fact that lightweight is the default expectation suggests the full lifecycle is overhead for these use cases.

`/listen:` and `/program:` sit in the middle. `/listen:` maps well because feedback simulation is naturally multi-step (select personas, simulate, synthesize, triage), but customer-facing roles want the merged lightweight version by default. `/program:` is the orchestrator and inherently needs all four phases, but its user base (leads, architects) is small and already thinks in staged plans -- the lifecycle is natural but the audience is narrow.

## Aggregate Scores by Namespace

| Namespace | Avg Natural Fit (1-5) | Avg Would-Use (1-5) | Lightweight Preferred? |
|-----------|----------------------|---------------------|----------------------|
| /scout: | 3.3 | 3.7 | Yes (3/3) |
| /draft: | 3.0 | 3.3 | Yes (3/3) |
| /review: | 4.7 | 4.7 | Split (1 yes, 2 no) |
| /flow: | 4.3 | 4.3 | Split (1 yes, 2 no) |
| /trace: | 4.7 | 4.7 | No (0/3) |
| /prove: | 4.3 | 4.3 | No (0/3) |
| /listen: | 3.7 | 4.0 | Yes (2/3) |
| /program: | 4.3 | 4.0 | No (0/3) |

## Per-Namespace Results

---

### /scout: -- PM proves the idea

**Scenario tested**: Using `/scout:competitors` to analyze the CRM market's AI copilot landscape. Setup identifies the CRM space with dimensions (AI features, pricing, extensibility). Execute researches Salesforce Einstein, HubSpot AI, Zoho Zia across those dimensions. Findings synthesizes into P1/P2/P3 positioning recommendations. Amend lets the PM challenge assumptions and add internal context.

#### PM Sales
- Natural fit: 3/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "Partially. When I need competitive intelligence, I already have a hypothesis -- 'we are behind on AI copilot for sellers.' I do not want to confirm scope and select dimensions first. I want to say 'show me where we stand on AI copilot vs Salesforce Einstein and HubSpot AI' and get the answer. The setup phase feels like it is asking me to do the tool's job. That said, the findings with P1/P2/P3 priorities maps perfectly to how I present to leadership -- that part is exactly right."
- "What would you change?": "Merge setup into the prompt. If I say '/scout:competitors AI copilot for sellers vs Salesforce, HubSpot', the tool should infer the space (CRM), the dimensions (AI features, seller adoption, pricing), and the scope. Do not ask me to confirm what I just told you. The amend phase is useful but should be optional -- sometimes the first pass is good enough and I just need to add a note, not re-run the analysis."
- Lightweight vs full: "Lightweight, every time. I am a PM -- I need speed to insight. If the full version takes 4 distinct steps with confirmation prompts, I will use a spreadsheet instead."

#### PM Commerce
- Natural fit: 3/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "The output format is right -- I need to walk into a review with a clear competitive position on conversion optimization, omnichannel, and POS reliability. But the 4-phase model assumes I am starting from scratch. Usually I am updating an existing competitive brief because a competitor just launched something. I want to say 'update my competitive brief -- Shopify just launched AI-powered checkout optimization' and get a delta, not a full re-analysis."
- "What would you change?": "Add an 'update' mode. Setup should detect if a prior scout artifact exists and offer to update it rather than starting over. The execute+findings merge in lightweight mode is correct -- separate findings from execution is artificial when the output is a single competitive brief."
- Lightweight vs full: "Lightweight. The full version is for annual strategic planning. Day-to-day competitive intelligence needs to be fast."

#### PM Operations
- Natural fit: 4/5
- Would-use: 3/5
- "Does this match how you'd actually use this?": "Supply chain competitive analysis is more structured than sales or commerce scouting. When I evaluate competitors like Oracle SCM Cloud or SAP IBP, the dimensions matter -- demand planning accuracy, warehouse management depth, production scheduling flexibility. So the setup phase where I select dimensions actually adds value here because the wrong dimensions give useless results. The 4-phase model works better for operations scouting because the domain is more technical."
- "What would you change?": "The amend phase should support adding quantitative data. When I review competitive findings, I want to annotate with our own benchmark numbers -- 'our OTIF is 94.2%, competitor claims 97% but their measurement methodology is different.' The amend phase as described is too generic -- it needs to support structured annotations, not just 'add context.'"
- Lightweight vs full: "Lightweight for quick checks, but I would use the full version for quarterly planning. So the answer is: give me both, but make lightweight the default."

**Namespace verdict**: The lifecycle fits at a structural level but the setup phase feels redundant to PMs who already know what they want. Lightweight should be the default, with setup auto-inferred from the prompt. The amend phase needs to support structured annotations, not just free-text additions.

---

### /draft: -- Author writes the design

**Scenario tested**: Using `/draft:spec` to author an authentication specification for the simulate plugin. Setup gathers intent ("plugin auth for multi-tenant scenarios"), identifies audience (dev team), selects template (ADR format). Execute produces the spec section by section. Findings self-reviews for open questions and gaps. Amend lets the author fill gaps.

#### Backend Dataverse (architect hat)
- Natural fit: 3/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "As an architect, I appreciate the template selection in setup -- ADR vs RFC vs design doc matters. But the execute phase producing a full draft section by section assumes I am delegating the writing entirely. In practice, I write the architecture section myself and want the tool to fill in the operational details, security model, and migration plan. The lifecycle treats authoring as a monolithic action, but real spec writing is collaborative -- some sections I own, some I want help with."
- "What would you change?": "Execute should be section-by-section with the option to skip or self-author individual sections. The findings phase (self-review) is genuinely useful -- when I write specs, I always miss gaps that a fresh read would catch. But call it 'gap analysis' not 'findings' -- 'findings' sounds like a review output, and this is a drafting tool. Amend merging with findings makes sense -- after you show me the gaps, I want to fill them immediately, not in a separate phase."
- Lightweight vs full: "Lightweight for proposals, full for specifications. A proposal is one question and one document. A spec has structure that benefits from template selection and section-by-section authoring."

#### PM Sales
- Natural fit: 3/5
- Would-use: 3/5
- "Does this match how you'd actually use this?": "When I draft a spec, it is usually a feature proposal for the next release -- 'add AI-powered next-best-action to the seller workspace.' I do not need to select a template or identify the audience -- I know my audience is the dev team and the format is always a one-pager with problem, proposal, success metrics, and timeline. The setup phase is asking me questions I already know the answers to."
- "What would you change?": "Remember my preferences. After I use `/draft:spec` once and pick my template, do not ask again. The execute phase should produce a draft I can edit, not a final document. The findings/amend merge is correct -- show me the gaps inline in the draft with [TODO] markers, not as a separate document. I want one artifact, not a draft plus a gap analysis document."
- Lightweight vs full: "Lightweight. Always. I am writing a one-pager, not a design specification. If I need the full version, I will ask for it."

#### PM Finance
- Natural fit: 3/5
- Would-use: 3/5
- "Does this match how you'd actually use this?": "Finance specs are heavily regulated -- when I draft a spec for revenue recognition changes, the structure is dictated by the regulatory requirement (ASC 606 compliance), not by a template I select. The setup phase should detect the regulatory context and auto-select the appropriate structure. The execute phase is useful because regulatory specs have mandatory sections (impact analysis, audit trail requirements, compliance testing plan) that I might miss."
- "What would you change?": "Add domain-specific templates that auto-populate mandatory sections for regulated domains. For finance, every spec needs: regulatory reference, impact analysis, audit trail requirements, rollback plan, compliance testing criteria. The tool should know this when I say 'spec for ASC 606 revenue recognition changes' -- I should not have to configure it."
- Lightweight vs full: "Lightweight for internal proposals. Full for regulatory specs. But even the full version should auto-detect the domain and pre-populate structure -- do not ask me to select a template when the domain implies the template."

**Namespace verdict**: The lifecycle is structurally sound but feels over-specified for PM use cases and under-specified for architect use cases. PMs want a single-artifact flow with inline gaps; architects want section-by-section collaboration. The setup phase should auto-detect intent and remember preferences. Findings/amend merging is the consensus expectation.

---

### /review: -- Team validates the design

**Scenario tested**: Using `/review:design` to review the simulate plugin's authentication spec. Setup identifies the spec, auto-selects Security Architect, API Designer, and Data Modeler roles. Execute runs three independent reviews with scores. Findings synthesizes consensus, splits, and severity. Amend lets the author address findings and re-run specific reviewers.

#### Backend Commerce
- Natural fit: 5/5
- Would-use: 5/5
- "Does this match how you'd actually use this?": "This is exactly how design reviews should work. In Commerce, when we review a CRT extension design, we need the security person to check payment connector implications, the API person to verify CSU contract compliance, and the data person to validate CDX sync patterns. Running them independently and then synthesizing is precisely right -- I have been in too many review meetings where one loud voice drowns out the others. Independent reviews followed by synthesis removes that bias."
- "What would you change?": "The amend phase should track which findings I addressed and which I deferred with a reason. Right now it says 'author addresses findings, re-runs specific reviewers on changes.' I want a resolution log: Finding F-01 resolved (code change), Finding F-02 deferred (out of scope, tracked in backlog), Finding F-03 disputed (my reasoning here). Then re-run only the reviewers whose findings I addressed."
- Lightweight vs full: "Full version. Commerce designs have cross-cutting concerns (offline mode, CDX sync, pricing engine) that need independent expert reviews. A single merged review would miss the interactions between these concerns."

#### Frontend PowerApps
- Natural fit: 5/5
- Would-use: 5/5
- "Does this match how you'd actually use this?": "When I build canvas apps, the review dimensions are completely different from backend -- delegation safety, responsive layout, component reuse, accessibility. Auto-selecting expert roles from the content is critical because a canvas app review needs a delegation expert, a UX expert, and a performance expert. The lifecycle captures this perfectly. Execute giving me independent scores per role means I can see that my delegation is perfect (5/5) but my responsive layout needs work (2/5) -- that specificity is what I need."
- "What would you change?": "The findings phase should include a severity-to-effort matrix. Not just P1/P2/P3 severity, but estimated effort to fix. A P1 delegation issue might be a one-line formula change. A P2 responsive layout issue might require restructuring three screens. Severity without effort leads to wrong prioritization."
- Lightweight vs full: "Full version for app reviews. But for quick code changes (formula updates), the lightweight single-document review is fine."

#### Developer Automate
- Natural fit: 4/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "For flow reviews, the auto-selection is important -- I need a trigger efficiency reviewer, an error handling reviewer, and a DLP compliance reviewer. The independent execution is correct because these are orthogonal concerns. But the setup phase auto-selecting roles 'from content' worries me -- Power Automate flows are JSON definitions. Can the tool really infer that this flow needs a DLP reviewer because it uses a non-business connector? The role selection needs to be accurate or I am better off selecting manually."
- "What would you change?": "Show me the auto-selected roles before execution and let me adjust. Do not just auto-select and run -- that is a black box. Also, for flow reviews specifically, the execute phase should include a 'run history analysis' option where the reviewer looks at actual flow run data (success rate, failure patterns, throttling incidents) in addition to the definition review."
- Lightweight vs full: "Full for production flows. Lightweight for personal/test flows. The distinction is deployment scope, not complexity."

**Namespace verdict**: The review lifecycle is the strongest fit of all namespaces. Independent execution with synthesis maps directly to how multi-discipline review actually works. All three personas would use the full version for production work. The amend phase needs a resolution tracking mechanism (finding-level accept/defer/dispute), and setup should show auto-selected roles for confirmation.

---

### /flow: -- Domain dev simulates the process

**Scenario tested**: Using `/flow:lifecycle` to simulate the Lead-to-Opportunity (L2O) process in Dynamics 365 Sales. Setup identifies the process (L2O), defines start state (new lead with BANT fields), end state (won opportunity with revenue), and selects Sales Dev + CRM Admin roles. Execute walks through each step with decision points and data changes. Findings identifies bottlenecks and missing exception paths. Amend lets the domain expert add business rules.

#### Developer Sales
- Natural fit: 5/5
- Would-use: 5/5
- "Does this match how you'd actually use this?": "This is my daily work described as a tool. The L2O process has QualifyLead creating three records atomically, BPF stages with required fields, opportunity scoring, and WinOpportunity/LoseOpportunity at the end. Walking through each step with decision points is exactly how I debug issues -- 'the seller qualified a lead but the opportunity did not appear, what happened?' The lifecycle captures this perfectly: setup defines the process boundaries, execute traces each step, findings identifies where things break, amend adds the business rules I know but the tool does not."
- "What would you change?": "The execute phase should support branching paths. L2O is not linear -- a lead can be disqualified (branch to close), the opportunity can be reassigned (branch to different BPF), or the quote can be revised (loop back). The current description implies a linear walkthrough. I need a trace that shows all paths, not just the happy path. Also, the findings should distinguish between 'missing configuration' (fixable) and 'platform limitation' (not fixable)."
- Lightweight vs full: "Full version for multi-step processes like L2O, period close, and P2P. Lightweight for trigger chains where I just need to know what fires."

#### Developer Finance
- Natural fit: 4/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "The period close process in Finance is exactly the kind of thing this simulates -- 8+ steps in a specific order (revaluation, bank reconciliation, inventory close, depreciation, accruals, consolidation, reporting, period lock). Each step has preconditions and post-conditions. The lifecycle maps well because I need to define the start state (open period with unposted transactions), walk through each step checking dependencies, and identify where the close will break."
- "What would you change?": "The execute phase needs dependency enforcement -- not just walking through steps sequentially, but validating preconditions. 'Inventory close must complete before financial reporting' is a hard dependency. If I skip it, the findings should flag it as P1 blocking, not just a suggestion. Also, the amend phase should support adding timing estimates -- 'inventory close takes 4 hours for 50K transactions' -- so I can build a close calendar."
- Lightweight vs full: "Full version for period close and P2P lifecycle. The lightweight trigger version is useful for checking what posts when an invoice is approved."

#### Developer Operations
- Natural fit: 4/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "Procure-to-pay (P2P) is the classic operations lifecycle -- purchase requisition, approval, PO creation, product receipt, invoice matching, payment. Each step involves different forms, different approval workflows, and different data entities. The lifecycle maps well. But operations processes have a unique challenge: they interact with physical reality. A production order is not just data -- it requires machine availability, material availability, and labor scheduling. The 'execute' phase needs to account for physical constraints, not just data flow."
- "What would you change?": "Add a 'constraints' section to the execute phase. For each step, I want to specify not just what data changes but what physical/resource constraints must be satisfied. 'Production order step 3: Report as finished -- requires: machine M-01 available, material BOM-4523 on hand, quality check QC-01 passed.' This makes the simulation match reality. Without constraints, the simulation is an idealized happy path that never matches the shop floor."
- Lightweight vs full: "Full version for document lifecycles. Lightweight for simple trigger chains. But I suspect I will use the full version 80% of the time because operations processes are inherently multi-step."

**Namespace verdict**: The lifecycle is a natural fit for domain process simulation. All three personas recognized their daily work in the 4-phase model. Key improvements needed: branching path support in execute (not just linear walks), dependency enforcement (not just documentation), and physical/resource constraint modeling. The lightweight version works for trigger chains but the full version is the expected default for business process lifecycles.

---

### /trace: -- System dev simulates the platform

**Scenario tested**: Using `/trace:request` to trace a POST /api/data/v9.2/accounts request through the Dataverse platform. Setup identifies the request, entry point (API gateway), expected endpoint (record created in Azure SQL), and context (standard table, Sales solution). Execute traces layer by layer: API gateway, authentication, OData routing, plug-in pipeline (pre-validation, pre-operation, main operation, post-operation), Azure SQL write, service endpoint triggers, response assembly. Findings identifies failure points, latency risks, and contract mismatches. Amend lets the system dev correct architectural assumptions.

#### Backend Dataverse
- Natural fit: 5/5
- Would-use: 5/5
- "Does this match how you'd actually use this?": "This is hand-compilation of the Dataverse request pipeline. I do this mentally every time I debug a 500 error or a timeout. The lifecycle is perfect: I define what I am tracing (setup), I trace it layer by layer (execute), I identify where it fails (findings), and I correct wrong assumptions (amend). The execute phase description -- 'gateway to auth to routing to business logic to data layer to response' -- is exactly the Dataverse pipeline. I would add: the plug-in pipeline stages (10, 20, 30, 40) should be explicit in the trace, not lumped into 'business logic.'"
- "What would you change?": "The execute phase should produce a structured trace artifact, not just narrative text. I want a table: Layer | Input | Output | Latency | Failure Modes. This maps to how I actually diagnose issues -- I look at each layer boundary and check what went in vs what came out. Also, add a 'batch mode' trace for $batch requests, because batch requests have different pipeline behavior (changeset transactions, Content-ID resolution, partial failure handling)."
- Lightweight vs full: "Full version. Always. System traces are inherently multi-layer. A lightweight version that skips layers is worse than no trace at all -- it gives false confidence."

#### Developer Commerce
- Natural fit: 5/5
- Would-use: 5/5
- "Does this match how you'd actually use this?": "Commerce has the most complex request paths in the platform. A POS transaction goes: Store Commerce app, local CRT, offline database, sync to CSU, CSU processes through CRT handlers, calls HQ real-time operations for inventory check, receives response, processes payment through Adyen connector, completes transaction, queues for CDX upload to HQ. That is 8+ service boundaries. The 4-phase lifecycle maps perfectly because I need to define which path I am tracing (setup), trace each boundary (execute), identify where POS goes offline gracefully vs crashes (findings), and correct assumptions about offline behavior (amend)."
- "What would you change?": "Add a 'offline mode' trace variant. I need to trace two paths: the online path (normal) and the offline path (degraded). The comparison between them is where the bugs live -- 'this works online but fails offline because the offline CRT does not support this handler.' Also, the findings should include latency budgets -- each layer gets a time allocation, and if any layer exceeds its budget, that is a P1 finding."
- Lightweight vs full: "Full version for request traces. The lightweight permission trace works for RBAC checks but request traces need every layer."

#### Developer Automate
- Natural fit: 4/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "Tracing a cloud flow execution maps well to this lifecycle. A flow trigger fires, the runtime evaluates conditions, calls connectors (each with its own auth, throttling, retry), processes responses, and completes or fails. The 4-phase model works because I need to define the trigger event (setup), trace through each action in the flow with connector calls (execute), identify where throttling or auth failures happen (findings), and correct assumptions about connector behavior (amend)."
- "What would you change?": "The execute phase should support tracing concurrent branches. Cloud flows support parallel branches -- actions running simultaneously. A linear trace does not capture this. I need a trace that shows: Branch A calls Dataverse at T+100ms, Branch B calls SharePoint at T+100ms, both return by T+500ms, then the flow continues sequentially. Also, the findings should highlight 429 throttling risks by calculating aggregate API call volume across all branches."
- Lightweight vs full: "Full version for production flow traces. The lightweight permission trace is useful for checking DLP violations, but flow execution traces need the full pipeline."

**Namespace verdict**: The trace lifecycle is the most natural fit alongside review. System developers already think in layers, boundaries, and contracts -- the 4-phase model names what they already do. All three personas scored 4-5 and prefer the full version. Key improvements: structured trace artifacts (table format, not narrative), concurrent/parallel path support, offline/degraded mode comparison, and latency budget annotations.

---

### /prove: -- Investigation

**Scenario tested**: Using `/prove:hypothesis` through `/prove:synthesize` to investigate whether Dynamics 365 customers want real-time sync between Dataverse and external CRMs. Hypothesis: "Customers want real-time bidirectional sync. We would change our mind if fewer than 5% enable it or if latency above 2 seconds makes it unusable." Execute runs `/prove:websearch` (industry reports), `/prove:analysis` (existing telemetry), and `/prove:interview` (simulated customer interviews). Findings merges evidence into answer-first format with confidence levels. Amend reviews synthesis and challenges weak evidence.

#### PM Sales
- Natural fit: 4/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "Investigation is how I make decisions. 'Should we invest in real-time sync for the sales pipeline?' -- I need evidence, not opinions. The hypothesis-first approach is right because it forces me to define what would change my mind before I look for evidence. That prevents confirmation bias. The multi-experiment approach (websearch + analysis + interview) is exactly how I triangulate -- public data, our own telemetry, and customer voice."
- "What would you change?": "The synthesize step should produce a one-page executive brief, not a research paper. I need: 'Answer: Yes, for accounts with fewer than 100 records. Evidence: moderate confidence. Recommendation: build for small datasets, defer large-scale sync.' Leadership does not read findings documents -- they read briefs. Also, the publish step should be optional by default, not a named phase. Most investigations do not need to become papers."
- Lightweight vs full: "Full version. Investigation requires rigor. Skipping the hypothesis or the synthesis produces unreliable conclusions. But synthesize should produce an executive brief, not an academic paper."

#### Developer Connectors
- Natural fit: 5/5
- Would-use: 5/5
- "Does this match how you'd actually use this?": "When I investigate whether a custom connector can handle enterprise-scale throughput, I need exactly this workflow. Hypothesis: 'Our connector can handle 10K requests per hour without exceeding the 429 threshold.' Experiments: websearch for API provider documentation on rate limits, analysis of our connector telemetry, prototype of a load test. Synthesize: 'Answer: No. The provider throttles at 600 requests per 5 minutes. At 10K/hour, we will hit 429 responses 40% of the time.' This is exactly how I build the case for a throttle-handling enhancement."
- "What would you change?": "The prototype experiment type is the most valuable for me. I want the prototype step to produce runnable artifacts -- not just a description of what was built, but the actual test script or flow that I can re-run when the API changes. Also, the analysis step should support querying specific telemetry sources -- connector execution logs, 429 response rates, average latency by connector. Generic 'analyze data' is too vague."
- Lightweight vs full: "Full version. Connector decisions have long-term implications (certification, SLA commitments). Skipping the hypothesis or the synthesis leads to undocumented architectural decisions that haunt us later."

#### Developer Copilot Studio
- Natural fit: 4/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "When I investigate whether generative answers can replace authored topics for common customer questions, I need evidence. Hypothesis: 'Generative answers from knowledge sources will correctly answer 80% of tier-1 support questions.' Experiments: analysis of topic completion rates, interview (simulated customer interactions), prototype (test agent with generative answers only). Synthesize the results with confidence levels. This maps well to the prove lifecycle."
- "What would you change?": "The interview experiment type should support simulated multi-turn conversations, not just single-question interviews. Agent interactions are conversational -- I need to test follow-up handling, clarification requests, and topic transitions. Also, the synthesize step should include a 'recommended next step' -- investigation without action is just curiosity. 'Based on this evidence, we recommend: move 15 topics to generative answers, keep 8 authored topics for complex workflows.'"
- Lightweight vs full: "Full version. Agent decisions affect every customer interaction. Cutting corners on evidence produces agents that confidently give wrong answers."

**Namespace verdict**: The prove lifecycle has the strongest conceptual fit because `/prove:` was explicitly designed as a multi-step investigation process. All three personas recognized the value of hypothesis-first, multi-experiment, synthesis-based investigation. The existing lifecycle maps so naturally that the only adjustments are output format (executive brief for PMs, runnable artifacts for devs) and experiment type specificity (multi-turn interviews, queryable telemetry, re-runnable prototypes).

---

### /listen: -- Post-ship feedback simulation

**Scenario tested**: Using `/listen:feedback` to simulate customer reactions to a new AI copilot for the seller workspace in Dynamics 365 Sales. Setup identifies the shipped feature (AI copilot for sellers), selects 6 customer personas (field seller, sales manager, sales ops, revenue leadership, small business seller, enterprise seller), defines feedback dimensions (usability, value, friction). Execute has each persona evaluate from their perspective. Findings synthesizes adoption blockers, delight moments, and friction patterns. Amend triages findings into backlog.

#### Frontend Customer Service
- Natural fit: 4/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "After we ship a new feature in the agent workspace -- say, AI-suggested knowledge articles in the sidebar -- I want to know what agents will actually think. The persona-based evaluation is the right approach because different agents have different needs: a tier-1 agent handling high volume wants speed, a tier-2 specialist wants accuracy, a supervisor wants visibility. The lifecycle captures this. But the 'findings' phase should weight feedback by persona importance -- a tier-1 agent's friction matters more than a supervisor's feature request because tier-1 agents are 80% of the user base."
- "What would you change?": "Weight persona feedback by user volume. A finding that affects 80% of users (tier-1 agents) should automatically be P1. A finding from a low-volume persona (supervisor) should be P2 at most unless it is a blocking issue. Also, the execute+findings merge in lightweight mode is the right default -- I do not need a separate synthesis step when I have 6 persona reactions. I can see the patterns myself."
- Lightweight vs full: "Lightweight for feature launches. Full for major redesigns where I need the triage (amend) phase to produce a backlog."

#### Developer Sales
- Natural fit: 3/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "As a developer, I care about technical friction more than adoption curves. When I ship a new forecast dashboard, I want to know: does it load fast enough? Do sellers understand the data? Does it break on mobile? The persona feedback approach is useful but the dimensions should include technical quality (performance, responsiveness, error handling), not just usability/value/friction. The lifecycle works but the dimension selection in setup needs to offer technical dimensions for developer users."
- "What would you change?": "Add a 'technical feedback' dimension that covers performance, reliability, and edge case behavior. When a seller persona says 'the dashboard is slow,' I need specifics: 'loading 500 opportunities takes 4 seconds on a typical laptop.' The current findings format (adoption blockers, delight moments, friction patterns) is PM language. Give me developer-specific findings: performance issues, error states, edge cases."
- Lightweight vs full: "Lightweight for incremental changes. I do not need a full persona evaluation for a bug fix. But for new features, the full version with triage is valuable."

#### Developer Commerce
- Natural fit: 4/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "Commerce has the most diverse user base -- online shoppers, store associates, store managers, merchandisers, omnichannel ops leads. Simulating their reactions to a new checkout flow or POS update is exactly what this does. The lifecycle works because I define the feature (setup), simulate reactions (execute), identify patterns (findings), and triage (amend). But Commerce has a unique constraint: POS feedback must account for queue pressure. A store associate's reaction to a feature is different when there are 5 people in line vs when the store is empty."
- "What would you change?": "Add contextual scenarios to persona evaluation. Do not just ask 'what does the store associate think of this feature?' -- ask 'what does the store associate think of this feature when processing 200 transactions per day with 3-minute average wait time?' Context changes everything in retail. Also, the findings should separate online channel feedback from in-store feedback -- they are different audiences with different success metrics."
- Lightweight vs full: "Lightweight for online features. Full for POS changes where I need both the persona evaluation and the triage into separate channel backlogs."

**Namespace verdict**: The lifecycle fits well for feedback simulation, but the execute+findings merge is the expected default for most use cases. The full 4-phase version adds value only for major launches requiring formal triage. Key improvements: weight persona feedback by user volume, add technical feedback dimensions, and support contextual scenarios (queue pressure, load conditions).

---

### /program: -- Lead orchestrates all

**Scenario tested**: Using `/program:plan` to plan the rollout of a new AI copilot feature for Dynamics 365 CRM. Setup defines the initiative ("AI copilot for CRM -- lead scoring, next-best-action, conversation intelligence"), selects namespaces (scout, draft, review, trace, listen), and sets gates. Execute generates a staged plan with skill sequence and dependencies. Findings validates the plan (right order, achievable gates, missing skills). Amend lets the lead adjust.

#### Backend Dataverse (architect hat)
- Natural fit: 5/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "As an architect, I think in staged plans with dependencies and gates. This is exactly how I plan large initiatives -- scout the competitive landscape, draft the design, review with experts, trace the system paths, build, and simulate customer feedback. The lifecycle maps perfectly to how I structure work. The 'findings' phase that validates the plan (right order? missing skills?) is valuable because I always miss something in the first pass -- usually the '/flow:' skills because I default to system thinking and forget about business process simulation."
- "What would you change?": "The execute phase should produce a visual dependency graph, not just a YAML file. I need to see that scout must complete before draft, that review can run in parallel with initial trace work, and that listen depends on build completing. A flat list of stages does not capture parallelism. Also, each gate should have a definition of done, not just a description. 'PM approves findings' is too vague -- what specific artifact must exist? What score threshold must be met?"
- Lightweight vs full: "Full version. Orchestration without validation is a list, not a plan. The findings phase that catches missing skills and wrong ordering is the whole point."

#### PM Commerce
- Natural fit: 4/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "I use staged plans for every major Commerce initiative -- new payment connector, omnichannel redesign, POS offline improvement. The program lifecycle works because I need to sequence the work and set gates. But I care more about the gates than the skill sequence. The value of `/program:plan` is not telling me which skills to run -- I know my process. It is validating that I have not skipped a critical step and that my gates are achievable."
- "What would you change?": "Focus the findings phase on gate validation, not skill selection. 'Your gate says No blocking findings remain but you have not included /review:customers -- customer persona testing would catch adoption blockers before you ship.' That is the insight I need. Also, the plan should include time estimates per stage. A plan without timelines is an aspiration, not a plan."
- Lightweight vs full: "Full version. If I am using an orchestrator, I need the validation (findings) and adjustment (amend) phases. Otherwise I would just write a Markdown checklist."

#### Developer Finance
- Natural fit: 4/5
- Would-use: 4/5
- "Does this match how you'd actually use this?": "Finance initiatives like ASC 606 compliance or period close automation are inherently staged -- you cannot build until you have the spec, and you cannot ship until you have traced the posting paths. The program lifecycle captures this. But finance has a unique constraint: regulatory deadlines. A program plan for finance must include external dependencies (audit firm review, regulatory filing dates) that are not skills in the simulate plugin."
- "What would you change?": "Support external dependencies -- things outside the simulate plugin's control. 'External auditor review of the spec' is not a simulate skill, but it is a gate in my program. The plan should accommodate external milestones alongside skill-based stages. Also, the amend phase should support plan versioning -- when I adjust the plan, I want to see what changed from v1 to v2, not just the current state."
- Lightweight vs full: "Full version. Orchestration of a finance initiative without validation against regulatory deadlines is negligent."

**Namespace verdict**: The lifecycle fits naturally because `/program:` is inherently about staged planning with validation. All three personas would use the full version. Key improvements: visual dependency graphs (not flat YAML), gate definitions of done (not descriptions), time estimates per stage, external dependency support (non-skill milestones), and plan versioning in amend.

---

## Cross-Namespace Patterns

### Namespaces where lifecycle fits naturally (4.0+)
- **/review:** (4.7) -- Independent multi-expert review with synthesis is exactly how design reviews work. The lifecycle names what already exists.
- **/trace:** (4.7) -- System developers already think in layers and boundaries. The 4-phase model is just structured hand-compilation.
- **/prove:** (4.3) -- Investigation was designed as a multi-step process. The lifecycle is not imposed -- it is inherent.
- **/flow:** (4.3) -- Business process simulation is inherently multi-step with start states, decision points, and findings.
- **/program:** (4.3) -- Orchestration requires all four phases by definition. You cannot plan without validating the plan.

### Namespaces where lifecycle feels forced (<3.5)
- **/draft:** (3.0) -- Authoring is not a 4-phase process. Writers want to go from intent to artifact with inline feedback, not through distinct phases. The lightweight version (one question, produce draft, review inline) is the real workflow.
- **/scout:** (3.3) -- PMs want speed to insight. The setup phase feels like the tool asking the user to do its job. Auto-detect from prompt, merge execute+findings, make amend optional.

### Lightweight vs full preference by namespace
- **Lightweight always**: /scout: (3/3), /draft: (3/3)
- **Lightweight default, full available**: /listen: (2/3)
- **Full default, lightweight available**: /flow: (2/3 full), /review: (2/3 full)
- **Full always**: /trace: (3/3), /prove: (3/3), /program: (3/3)

### Common change requests
1. **Structured trace artifacts** (table format, not narrative) -- requested by /trace: personas (3/3), /flow: personas (2/3)
2. **Show auto-selected roles before execution** -- requested by /review: (1/3), implied by /scout: (2/3)
3. **Resolution tracking in amend** (accept/defer/dispute per finding) -- requested by /review: (2/3), /flow: (1/3)
4. **Remember user preferences** (template selection, dimension preferences) -- requested by /draft: (2/3), /scout: (1/3)
5. **Weight findings by user volume** -- requested by /listen: (2/3)
6. **External dependency support** -- requested by /program: (2/3)
7. **Branching/parallel path support** -- requested by /flow: (2/3), /trace: (2/3)
8. **Executive brief output option** (vs research paper) -- requested by /prove: (1/3), /scout: (2/3)
9. **Time estimates per stage** -- requested by /program: (2/3), /flow: (1/3)
10. **Domain-specific auto-detection** (regulatory context for finance, offline mode for Commerce) -- requested by /draft: (1/3), /trace: (1/3), /listen: (1/3)

### Recommended adjustments per namespace

| Namespace | Adjustment |
|-----------|------------|
| /scout: | Make lightweight the default. Auto-infer scope from prompt. Support 'update' mode for existing artifacts. |
| /draft: | Merge findings/amend into inline gap markers. Support section-by-section collaboration. Remember template preferences. |
| /review: | Add resolution tracking (accept/defer/dispute). Show auto-selected roles for confirmation before execution. Add effort estimates to findings. |
| /flow: | Support branching paths (not linear-only). Add dependency enforcement (hard vs soft). Add resource/physical constraints. |
| /trace: | Produce structured trace tables (Layer / Input / Output / Latency / Failure Modes). Support concurrent path tracing. Add latency budget annotations. |
| /prove: | Produce executive briefs (not just papers). Support re-runnable prototype artifacts. Add 'recommended next step' to synthesis. |
| /listen: | Weight feedback by persona volume. Add technical feedback dimensions. Support contextual scenarios (load, queue pressure). |
| /program: | Visual dependency graphs. Gate definitions of done. External dependency support. Plan versioning in amend. Time estimates. |
