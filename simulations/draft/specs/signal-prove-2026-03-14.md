# Prove Specification

**Topic**: sim
**Namespace**: /prove:
**Skills**: 8
**Default mode**: Full
**Audience**: PMs, researchers, architects, and tech leads who need to validate assumptions with evidence before committing resources to a direction

## Purpose

Can we prove what we believe? /prove: answers this by structuring investigation as a formal lifecycle: state a hypothesis with falsification criteria, run experiments (web research, internal intelligence, prototypes, data analysis, stakeholder interviews), synthesize evidence into an answer-first format, and optionally publish findings as a reusable research artifact.

## Skills

### /prove:hypothesis

**What**: State a testable hypothesis with explicit falsification criteria — the starting point for every investigation.
**Stock roles**: None (the user is the researcher)
**Input**: A belief statement ("We think X"), context for why it matters, and optionally what would change your mind.
**Output**: A structured hypothesis document with: claim, reasoning, falsification criteria, proposed experiments, and confidence level (pre-evidence).
**Lifecycle**:
- Setup: User states what they believe and why. Skill extracts the core claim, identifies implicit assumptions, and proposes falsification criteria ("We'd change our mind if..."). User confirms or adjusts.
- Execute: Skill structures the hypothesis into a formal document. Identifies which experiment types (websearch, intelligence, prototype, analysis, interview) could test each aspect of the claim. Proposes an experiment plan with ordering (cheapest/fastest first).
- Findings: Self-review of the hypothesis — is the claim falsifiable? Are the criteria measurable? Is the experiment plan feasible? Flags unfalsifiable claims ("customers will love this" has no measurable threshold) and suggests rewording.
- Amend: User refines the hypothesis based on feedback. Adjusts falsification criteria to be measurable. Confirms experiment plan.
**Lightweight**: `--quick` takes the belief statement, produces a one-page hypothesis with 2-3 experiments, skips self-review.
**Artifact**: `prove/hypothesis/sim-{slug}-{date}.md`
**Example**:
User runs `/prove:hypothesis "We believe real-time sync is essential for our CRM users"`. Setup: Skill extracts claim ("real-time sync is essential"), asks "Essential means what — they won't buy without it? They'll churn? They'll complain?" User clarifies: "They won't adopt the product without it." Skill proposes falsification: "We'd change our mind if: fewer than 30% of target users rank real-time sync in their top 3 needs, OR if batch sync with <5 minute delay satisfies 80%+ of use cases." Execute: Proposes experiments — (1) websearch: competitor real-time sync adoption rates, (2) intelligence: internal telemetry on sync usage patterns, (3) interview: 5 simulated CRM user conversations about sync expectations. Findings: Self-review flags that "essential" needs a threshold — adds "adoption rate drops below 40% without it" as measurable criterion. Amend: User accepts refined hypothesis. Artifact written.

### /prove:websearch

**What**: Search the public web for evidence that supports or contradicts the hypothesis — competitor analysis, industry reports, blog posts, documentation, forum discussions.
**Stock roles**: None (automated research)
**Input**: The hypothesis document (from /prove:hypothesis) and specific research questions to answer.
**Output**: An evidence brief with: sources found, key findings per source, relevance to hypothesis (supports/contradicts/neutral), confidence in source quality, and a summary verdict.
**Lifecycle**:
- Setup: Read the hypothesis. Extract 3-5 specific research questions from the falsification criteria. Determine search strategy (competitor names, industry terms, technical keywords).
- Execute: Run web searches for each research question. For each result: extract key claims, assess source credibility (vendor blog vs. peer-reviewed study vs. forum post), determine relevance to hypothesis. Track which falsification criteria each finding addresses.
- Findings: Synthesize across all sources. For each falsification criterion: what does the web evidence say? How strong is it? Where are the gaps (no evidence found)? Overall verdict: does web evidence support, contradict, or leave the hypothesis unresolved?
- Amend: Researcher reviews findings, flags unreliable sources, adds context the web search missed ("this blog post is from 2019, the product has changed since then"), requests deeper searches on specific sub-questions.
**Lightweight**: `--quick` runs 3 searches, produces a bullet-point evidence summary, skips source credibility analysis.
**Artifact**: `prove/websearch/sim-{slug}-{date}.md`
**Example**:
Hypothesis: "Real-time sync is essential for CRM adoption." Research questions: (1) What % of CRM products offer real-time sync? (2) Do users complain about batch sync delays? (3) Has any CRM lost market share due to sync latency? Execute: Finds that Salesforce, HubSpot, and Dynamics all offer near-real-time sync but default to batch. G2 reviews show 12% of negative reviews mention sync delays. No evidence of market share loss from sync latency specifically. Findings: Web evidence is mixed — real-time sync is table stakes for enterprise CRM (all major players offer it), but batch sync is the default and most users don't change it. Verdict: partially supports hypothesis (it's expected) but contradicts "essential" (batch works for most). Amend: Researcher notes that enterprise tier is different from SMB — adds sub-question about enterprise-specific sync requirements.

### /prove:intelligence

**What**: Query internal organizational knowledge (SharePoint, Teams, emails, eng.ms docs) via Work IQ for evidence that's not on the public web.
**Stock roles**: None (automated research via Work IQ relay)
**Input**: The hypothesis document and specific internal research questions (e.g., "What did the sales team hear from customers about sync?", "Are there internal telemetry dashboards for sync usage?").
**Output**: An internal evidence brief with: sources found, key findings, relevance to hypothesis, classification (confidential/internal/public), and a summary verdict.
**Lifecycle**:
- Setup: Read the hypothesis. Extract internal-specific research questions — things only knowable from inside the organization (customer feedback, telemetry, internal discussions, design decisions, post-mortems). Formulate Work IQ queries.
- Execute: Dispatch queries to Work IQ relay. For each result: extract key claims, identify the source type (email thread, Teams chat, SharePoint doc, ADO work item), assess recency and authority (PM spec vs. hallway conversation). Track which falsification criteria each finding addresses.
- Findings: Synthesize internal evidence. Compare with external evidence (from websearch if available). Identify insider knowledge that changes the picture — internal telemetry that contradicts public claims, customer feedback that's not reflected in reviews, design decisions that explain observed behavior.
- Amend: Researcher reviews, verifies source accuracy ("that email is from the old team, policy changed in Q3"), requests follow-up queries on promising leads.
**Lightweight**: `--quick` runs 2 Work IQ queries, produces a bullet-point summary, skips cross-referencing with external evidence.
**Artifact**: `prove/intelligence/sim-{slug}-{date}.md`
**Example**:
Hypothesis: "Real-time sync is essential for CRM adoption." Internal questions: (1) "What sync-related escalations did support handle in Q4?" (2) "What does the sync telemetry dashboard show for batch vs real-time usage?" Execute: Work IQ finds a Teams thread where a PM shared Q4 escalation data — 8 of 42 escalations were sync-related, but 6 of those 8 were about sync *failures*, not sync *latency*. Telemetry dashboard (SharePoint) shows 94% of tenants use batch sync, 6% enabled real-time, and of those 6%, average record count is <500. Findings: Internal evidence strongly contradicts "essential" — customers care about sync reliability, not sync speed. The 6% who use real-time are small tenants with low record counts. Verdict: hypothesis should pivot from "real-time sync" to "reliable sync." Amend: Researcher accepts the pivot, reformulates hypothesis.

### /prove:prototype

**What**: Build a minimal prototype to test a specific aspect of the hypothesis — measure behavior, performance, feasibility, or user reaction to a concrete artifact.
**Stock roles**: None (the prototype is the experiment)
**Input**: The hypothesis document and a specific question that can only be answered by building something (e.g., "Can we parse 10K records in <2 seconds?", "Does the proposed CLI flow feel natural?").
**Output**: A prototype report with: what was built, what was measured, raw measurements, interpretation against falsification criteria, and replication instructions.
**Lifecycle**:
- Setup: Define the prototype scope — what exactly to build, what to measure, what constitutes success/failure against the falsification criteria. Scope must be achievable in hours, not days. If it takes more than a day, decompose into smaller prototypes.
- Execute: Build the prototype. Run measurements. Record raw data (timing, error rates, output sizes, user reactions). Compare measurements against falsification thresholds.
- Findings: Interpret results. Did the prototype confirm or refute the hypothesis? Were there surprises? What limitations does the prototype have (scope, fidelity, sample size)? How confident are we in the results?
- Amend: Researcher reviews, challenges prototype design ("you tested with 100 records but our threshold is 10K"), requests follow-up prototypes for edge cases.
**Lightweight**: `--quick` builds a single-measurement prototype, produces a pass/fail result with raw data, skips interpretation.
**Artifact**: `prove/prototype/sim-{slug}-{date}.md`
**Example**:
Hypothesis: "Our compiler can handle 1000-spec workspaces without degrading below 5 seconds." Prototype scope: Generate synthetic workspaces at 100, 500, 1000, 2000 specs. Measure compile time for each. Success threshold: 1000 specs < 5 seconds. Execute: Built workspace generator. Results — 100 specs: 0.3s, 500 specs: 1.8s, 1000 specs: 4.7s, 2000 specs: 14.2s. Findings: Hypothesis confirmed at 1000 specs (4.7s < 5s threshold) but growth is super-linear — 2000 specs is 3x slower than expected from linear projection. The bottleneck is cross-reference resolution (O(n^2) in current implementation). Amend: Researcher notes the O(n^2) bottleneck — files a follow-up hypothesis: "Cross-reference resolution can be optimized to O(n log n) with an index."

### /prove:analysis

**What**: Analyze existing data, telemetry, logs, or metrics to find patterns that support or contradict the hypothesis — no new data collection, just interrogation of what exists.
**Stock roles**: None (data analysis)
**Input**: The hypothesis document and pointers to data sources (telemetry dashboards, log files, CSV exports, database queries, existing reports).
**Output**: An analysis report with: data sources examined, methodology, key findings (with charts/tables where appropriate), statistical confidence, and interpretation against falsification criteria.
**Lifecycle**:
- Setup: Identify available data sources relevant to the hypothesis. Determine what questions to ask of each data source. Define the analysis methodology (descriptive statistics, trend analysis, cohort comparison, etc.). Confirm data access and quality.
- Execute: Run the analysis. For each data source: extract relevant metrics, compute aggregates, identify trends and outliers, test against falsification thresholds. Produce tables and summaries of raw findings.
- Findings: Interpret the data. Do the numbers support or contradict the hypothesis? How strong is the signal vs. noise? Are there confounding variables? What's the confidence level? Where are data gaps that prevent a definitive answer?
- Amend: Researcher reviews, challenges methodology ("you compared monthly averages but the hypothesis is about peak load — use P95 instead"), requests deeper cuts on specific segments.
**Lightweight**: `--quick` runs a single-metric analysis against the primary falsification criterion, produces a one-paragraph verdict, skips methodology documentation.
**Artifact**: `prove/analysis/sim-{slug}-{date}.md`
**Example**:
Hypothesis: "Plugin execution failures are caused by timeout, not by logic errors." Data sources: Production error logs (last 90 days), plugin execution telemetry. Execute: Analyzed 12,847 plugin failures. Categorized by error type: timeout (58%), null reference (22%), permission denied (14%), other (6%). Timeout failures correlate with payload size > 4MB (r=0.87). Findings: Hypothesis partially confirmed — timeout is the leading cause (58%) but not the dominant cause. Null reference errors (22%) suggest a significant logic error population. The 4MB payload correlation suggests a specific mitigation (payload size validation). Amend: Researcher refines — "timeout is the *plurality* cause, not the *majority* cause. We should address both timeout and null reference."

### /prove:interview

**What**: Conduct simulated stakeholder interviews to gather qualitative evidence — the AI plays the interviewee (customer, user, executive, partner) and the researcher asks questions.
**Stock roles**: Interviewee roles are drawn from customer personas (C-01 through C-12) or custom stakeholder profiles
**Input**: The hypothesis document, which stakeholder perspectives to interview, and an interview guide (3-5 key questions).
**Output**: Per-interview transcript with key quotes, an interviewer's summary of themes, and relevance to hypothesis falsification criteria.
**Lifecycle**:
- Setup: Select 3-5 stakeholder perspectives relevant to the hypothesis. For each, establish their context (role, experience, concerns). Draft an interview guide with open-ended questions. Define what you're listening for (confirmation signals, contradiction signals, surprise signals).
- Execute: Conduct each interview. The AI plays the stakeholder in character — with their blind spots, biases, and domain knowledge. Researcher asks questions. Stakeholder responds authentically (including "I don't know" and "that's not how I think about it"). Record key quotes verbatim.
- Findings: Cross-interview synthesis. Identify themes that emerged across multiple stakeholders. Flag contradictions between stakeholders. Extract the strongest quotes for and against the hypothesis. Assess whether qualitative evidence shifts confidence up or down.
- Amend: Researcher reviews transcripts, identifies follow-up questions, requests additional interviews with different stakeholder types if initial coverage is too narrow.
**Lightweight**: `--quick` runs 2 interviews with the most relevant personas, produces a theme summary without full transcripts, skips follow-up.
**Artifact**: `prove/interview/sim-{slug}-{date}.md`
**Example**:
Hypothesis: "Developers will prefer YAML configuration over a visual editor for agent setup." Interview 3 stakeholders: C-02 James (developer), C-01 Maria (maker), C-11 Tomoko (team lead). Interview with James: "YAML, obviously. I can version it, diff it, template it. Visual editors are where config goes to die." Interview with Maria: "I don't know what YAML is. If you showed me a form with dropdowns, I'd fill it in. If you showed me a text file with colons and dashes, I'd close it." Interview with Tomoko: "My team is mixed — 3 devs who want YAML and 2 ops people who want a UI. Can we have both? The devs would set it up in YAML and the ops people would view it in a dashboard." Findings: Hypothesis confirmed for developer audience but contradicted for maker audience. Team lead reveals the real need: both interfaces backed by the same config. Key quote from Tomoko: "The format is an implementation detail. The question is who needs to touch it."

### /prove:synthesize

**What**: Merge evidence from all completed experiments into an answer-first synthesis — the definitive "what we learned" document for the investigation.
**Stock roles**: None (synthesis is a structural operation)
**Input**: The hypothesis document and all completed experiment artifacts (websearch, intelligence, prototype, analysis, interview — whichever were run).
**Output**: A synthesis document with: answer (1-2 sentences), confidence level (high/medium/low with rationale), evidence summary per experiment, principles extracted, what we got wrong, and recommended next steps.
**Lifecycle**:
- Setup: Gather all experiment artifacts. Verify each experiment's findings are finalized (no pending Amend cycles). Map each experiment's verdict to the falsification criteria. Identify which criteria are resolved vs. still open.
- Execute: Synthesize across experiments. For each falsification criterion: what does the combined evidence say? Where do experiments agree? Where do they conflict? Weight evidence by quality (prototype measurement > interview anecdote > blog post). Derive the answer — confirmed, refuted, or partially confirmed with caveats.
- Findings: Extract principles — reusable insights that apply beyond this specific hypothesis. Document "what we thought vs. what we actually learned." Identify residual uncertainties and recommended follow-up investigations.
- Amend: Researcher reviews synthesis, challenges evidence weighting, adds context that crosses experiments ("the prototype and the telemetry analysis actually measure the same thing differently — we should reconcile"), confirms the answer.
**Lightweight**: `--quick` produces a 1-page summary with answer, confidence, and top 3 findings. Skips principle extraction and what-we-got-wrong.
**Artifact**: `prove/synthesize/sim-{slug}-{date}.md`
**Example**:
Investigation: "Real-time sync is essential for CRM adoption." Experiments completed: websearch (mixed — table stakes but batch is default), intelligence (contradicts — customers care about reliability, not speed), interview (splits — developers want real-time, makers don't care), analysis (partially confirms — 58% of failures are timeout-related). Synthesis answer: "Real-time sync is expected but not essential. Customers care about sync reliability first, speed second. The 6% real-time adoption rate and maker indifference suggest investing in reliable batch sync with an optional real-time tier for power users." Confidence: medium (intelligence and interview evidence strong, but analysis was tangential — timeout != latency preference). Principles: (1) "Essential" claims usually decompose into "expected" + "important for a segment." (2) Internal telemetry often contradicts public narrative. (3) Makers and developers have opposite preferences — always test both. What we got wrong: assumed "essential" was binary. It's a spectrum, and the answer depends on segment.

### /prove:publish

**What**: Package a completed investigation into a formal research artifact suitable for sharing — with abstract, methodology, findings, and peer review.
**Stock roles**: 3 academic reviewers (generalist, methodology specialist, domain specialist) drawn from the Panel 3-tier system
**Input**: The synthesis document (from /prove:synthesize) and the target audience (internal team, leadership, external community).
**Output**: A published research paper with: abstract, introduction, methodology, findings, discussion, conclusion, and peer review scores.
**Lifecycle**:
- Setup: Read the synthesis. Determine the target format (internal brief, research paper, or technical report). Select 3 academic reviewers appropriate for the domain and methodology. Confirm scope — some investigations produce a 2-page brief, others a 20-page paper.
- Execute: Author the paper from the synthesis. Structure follows the target format. The author role writes; reviewers are not involved yet. Figures, tables, and evidence summaries are included from experiment artifacts.
- Findings: 3 reviewers evaluate the paper independently. Generalist checks clarity and significance. Methodology specialist checks experimental design and evidence weighting. Domain specialist checks domain accuracy and practical applicability. Each scores on a 10-point scale (from Panel scoring rubric) and provides specific findings.
- Amend: Author addresses reviewer findings. Revise paper. Re-submit to reviewers who had P1 findings. Iterate until all reviewers score >= 7/10.
**Lightweight**: `--quick` produces a 1-page brief with abstract and key findings, skips peer review.
**Artifact**: `prove/publish/sim-{slug}-{date}.md`
**Example**:
Investigation: "Real-time sync is essential for CRM adoption." Synthesis complete with medium confidence. User requests internal research paper for the platform team. Setup: Selects reviewers — Generalist (research quality), Distributed Systems Specialist (sync architecture methodology), CRM Domain Expert (Dynamics applicability). Execute: Authors 8-page paper — abstract summarizes the pivot from "essential" to "expected but not essential," methodology section describes the 5-experiment approach, findings present per-experiment evidence with confidence ratings, discussion section proposes the "reliable batch + optional real-time tier" recommendation. Findings: Generalist scores 8/10 — "clear and well-structured." Methodology Specialist scores 6/10, P1: "Prototype measured compiler performance, not sync performance — this experiment doesn't test the hypothesis. Either remove or reframe." Domain Expert scores 7/10, P2: "Missing discussion of offline-first mobile scenarios — relevant for field sales CRM." Amend: Author removes the tangential prototype, adds offline-first discussion. Re-submit to Methodology Specialist — scores 8/10. Published.

## Roles

### Stock roles

| Role | What It Does | Used By |
|------|-------------|---------|
| Academic Generalist | Reviews research clarity, significance, structure, and accessibility | publish |
| Methodology Specialist | Reviews experimental design, evidence weighting, statistical rigor, and reproducibility | publish |
| Domain Specialist | Reviews domain accuracy, practical applicability, and completeness of domain coverage | publish |

### Custom roles (optional)

`/prove:interview` benefits most from custom roles. If your investigation involves stakeholders not covered by the C-01 through C-12 personas (e.g., a specific vendor partner, a regulatory body representative, an open-source community maintainer), create stakeholder profiles in `.craft/roles/{name}/ROLE.md` with their background, concerns, blind spots, and communication style.

`/prove:publish` can use custom reviewer roles for domain-specific expertise. If your investigation is in a niche area (e.g., quantum computing, regulatory compliance for medical devices), create reviewer profiles with their publication history, evaluation criteria, and pet peeves.

## Artifacts

```
prove/
├── hypothesis/
│   ├── sim-realtime-sync-2026-03-14.md          # Initial hypothesis
│   └── sim-compiler-scale-2026-03-15.md         # Compiler scaling hypothesis
├── websearch/
│   ├── sim-realtime-sync-2026-03-14.md          # Web evidence for sync investigation
│   └── sim-compiler-benchmarks-2026-03-15.md    # Competitor compiler benchmarks
├── intelligence/
│   ├── sim-realtime-sync-2026-03-14.md          # Internal evidence for sync
│   └── sim-customer-escalations-2026-03-15.md   # Internal escalation data
├── prototype/
│   ├── sim-compiler-scale-2026-03-15.md         # Workspace size benchmark
│   └── sim-sync-latency-2026-03-16.md           # Sync latency measurement
├── analysis/
│   ├── sim-plugin-failures-2026-03-14.md        # Error log analysis
│   └── sim-sync-telemetry-2026-03-15.md         # Sync usage telemetry
├── interview/
│   ├── sim-realtime-sync-2026-03-14.md          # Stakeholder interviews on sync
│   └── sim-yaml-vs-ui-2026-03-16.md             # Config preference interviews
├── synthesize/
│   ├── sim-realtime-sync-2026-03-15.md          # Final synthesis for sync investigation
│   └── sim-compiler-scale-2026-03-16.md         # Final synthesis for compiler scaling
└── publish/
    ├── sim-realtime-sync-2026-03-16.md          # Published paper on sync findings
    └── sim-compiler-scale-2026-03-17.md         # Published paper on compiler scaling
```

All artifact filenames use the pattern `sim-{slug}-{date}.md`. The topic prefix `sim` ties all artifacts for the simulate plugin's self-dogfooding investigation together. A different initiative would use its own topic prefix (e.g., `crm-realtime-sync-2026-03-14.md`).

## Technique Heritage

| Skill | Technique | What It Contributes |
|-------|-----------|-------------------|
| hypothesis | 08 Hypothesis Investigation | Formal hypothesis structure with falsification criteria. "State what you believe, state what would change your mind." Directly from `/research` skill's 708-line orchestrator. |
| websearch | 08 Hypothesis Investigation | Web research as one experiment type within the investigation lifecycle. Source credibility assessment. |
| intelligence | 08 Hypothesis Investigation | Internal knowledge mining via Work IQ. The "insider evidence" experiment type. Evidence classification (confidential/internal/public). |
| prototype | 08 Hypothesis Investigation | Build-and-measure experiment type. Scope constraint (hours, not days). Raw measurement + interpretation pattern. |
| analysis | 08 Hypothesis Investigation | Data interrogation experiment type. Existing data, no new collection. Statistical confidence assessment. |
| interview | 08 Hypothesis Investigation + 04 Persona Walkthrough | Simulated stakeholder conversations. Draws personas from Customer Persona system (C-01 through C-12) or custom profiles. First-person in-character responses. |
| synthesize | 08 Hypothesis Investigation | Answer-first synthesis. "What we thought vs. what we actually learned." Principle extraction. Confidence levels. Directly from the investigation lifecycle's synthesis phase. |
| publish | 09 Academic Peer Review | 3-tier panel system (51 reviewers). 10-point scoring rubric. Multi-round review with resubmission. Paper/module/board progression. Directly from Panel's review lifecycle. |

## Cross-Namespace Integration

**Inputs from other namespaces**:
- `/scout:competitors` and `/scout:feasibility` findings often generate hypotheses — "competitors don't offer X, so there's a market gap" becomes a `/prove:hypothesis`
- `/draft:spec` produces design decisions that may need evidence — "we chose YAML over JSON because..." becomes a provable claim
- `/review:design` P1 findings that are disputed ("I disagree that this is a security risk") become hypotheses to prove or refute

**Outputs to other namespaces**:
- `/prove:synthesize` produces validated findings that feed into `/draft:spec` (evidence-based design decisions) and `/draft:proposal` (evidence-backed recommendations)
- `/prove:publish` produces research papers that feed into `/review:design` as reference material (reviewers can cite published investigations)
- `/prove:interview` stakeholder quotes feed into `/review:customers` as calibration data (do simulated customers match real interview data?)
- `/prove:analysis` data findings feed into `/listen:adoption` as baseline metrics (pre-ship vs. post-ship comparison)

**Internal sequencing**: The 8 skills form an explicit multi-step lifecycle:
1. `/prove:hypothesis` (always first)
2. Pick 1-5 experiments: `/prove:websearch`, `/prove:intelligence`, `/prove:prototype`, `/prove:analysis`, `/prove:interview` (any order, run in parallel or sequence)
3. `/prove:synthesize` (after experiments complete)
4. `/prove:publish` (optional, after synthesis)

This sequencing is enforced by artifact dependencies — synthesize requires experiment artifacts to exist, publish requires a synthesis artifact.

**Orchestration**: `/program:plan` uses this internal sequencing to plan investigation stages. A program that includes `/prove:` will generate stages for hypothesis, experiments, and synthesis automatically.
