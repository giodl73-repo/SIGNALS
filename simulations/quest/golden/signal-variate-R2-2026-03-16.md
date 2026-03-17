---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-16
round: 2
rubric: simulations/quest/rubrics/signal-rubric-v2-2026-03-16.md
---

# Quest Variate -- /signal (Round 2)

**Skill**: `signal` -- command index showing all skills by namespace.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v2-2026-03-16.md`
**Rubric changes from v1**: Added C-11 (purpose tagline in header), C-12 (blockquote routing hints),
C-13 (quantified output artifacts); aspirational denominator updated from 2 to 5.

**Context**: R1 champion was V-05 (100 pts on v1). All R1 variations passed C-09. C-12 and C-13 were
partially present in V-02 and V-03 but not enforced by rule. C-11 was implicit in V-03/V-05 but not
required by prompt. R2 isolates and enforces each new criterion by rule before combining.

**Axes explored**:
- V-01: C-13 single-axis -- quantified output artifact descriptions (strict enforcement rule)
- V-02: C-12 single-axis -- blockquote routing hints (explicit format rule)
- V-03: C-11 single-axis -- purpose taglines in namespace headers (explicit format rule)
- V-04: Combination -- C-11 + C-12 + C-13 all three new criteria together
- V-05: Full integration -- all 5 aspirational criteria (C-09 through C-13) + R1 V-05 excellence patterns

**Canonical sub-skill counts** (per rubric C-02):
scout:8, draft:4, review:4, flow:7, trace:7, prove:9, listen:3, program:2, topic:6, quest:4, mock:3, org:4

---

## V-01 -- C-13 Single-Axis: Quantified Artifact Descriptions

**Axis**: C-13 -- descriptions reference quantified output artifacts
**Hypothesis**: Adding an explicit DESCRIPTION RULE ("every description must name a specific count,
named format, or rated deliverable") forces the model to produce C-13-compliant descriptions
without changing any other structural aspect of V-01 R1. This isolates the effect of quantified
artifact language on the output.

```
Show the Signal command index.

MODE DETECTION:
- No args: print the full index, all 12 namespaces.
- One arg (e.g., /signal flow): print only that namespace section.
- --bare flag: print only command names as a flat list, no descriptions, no headers.

DESCRIPTION RULE: Every sub-skill description must name a specific output --
a count, named format, or rated deliverable. Vague phrases alone are not acceptable.
  PASS: "competitive landscape map with 5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"

FULL INDEX FORMAT -- repeat this pattern for each namespace:

- /<namespace> -- <Namespace> namespace -- <N> skills for <domain purpose>.

  /<sub-skill-1>  -> <quantified description naming specific output>
  /<sub-skill-2>  -> <quantified description naming specific output>
  ...

  Run any sub-skill directly, or describe your <domain noun> and the most relevant <namespace> skill will run.

NAMESPACES AND SKILLS (output exactly these, in this order):

scout -- 8 skills:
  /scout-competitors   -> competitive landscape map with inertia as primary competitor; 5-8 rivals rated HIGH/MEDIUM/LOW threat
  /scout-feasibility   -> traffic-light ratings (RED/YELLOW/GREEN) across technical, team, timeline, and budget dimensions
  /scout-naming        -> name shortlist with trademark clearance status, domain availability, and per-persona score per name
  /scout-compliance    -> regulatory framework map: applicable laws, enforcement risk rating, and design-blocking constraints
  /scout-market        -> market sizing with TAM/SAM/SOM table and segment ranking by fit score
  /scout-stakeholders  -> power/interest grid with named stakeholders, veto risk rating, and influence path per stakeholder
  /scout-positioning   -> per-audience positioning statement (3+ audiences) with differentiation axis per audience
  /scout-requirements  -> MoSCoW-prioritized requirements list with dependency graph and ambiguity flags

draft -- 4 skills:
  /draft-spec        -> specification with 8+ guided sections, completeness checklist, and self-review verdict
  /draft-proposal    -> proposal with 3-option minimum, option comparison table, and recommendation rationale
  /draft-pitch       -> pitch deck in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
  /draft-brainstorm  -> idea pool with inertia baseline entry and per-idea peer-comparison score

review -- 4 skills:
  /review-design     -> design review through 6 disciplines with named expert and pass/fail verdict per discipline
  /review-code       -> code review with file-level annotations, severity rating per finding, and pass/fail per discipline
  /review-users      -> 5 persona advocates each produce usability score and cross-persona synthesis
  /review-customers  -> 12 customer personas each produce would-adopt rating, NPS prediction, and top concern

flow -- 7 skills:
  /flow-lifecycle    -> phase-by-phase lifecycle with entry/exit contracts, exception flows, and rollback conditions per phase
  /flow-conversation -> multi-turn conversation trace through topic graph with dead-end count and loop detection
  /flow-trigger      -> fire-order list and side-effect table for every field/event change in the trigger set
  /flow-dataflow     -> pipeline stage-by-stage trace with data loss event count and schema mismatch list
  /flow-integration  -> cross-system integration trace with named connector gaps and failure mode per gap
  /flow-throttle     -> throughput table by burst tier with backpressure propagation path and degradation thresholds
  /flow-resilience   -> scenario table for offline, partial failure, and eventual consistency with recovery path per scenario

trace -- 7 skills:
  /trace-request     -> request path with every service boundary named, hop count, and latency estimate per hop
  /trace-state       -> state transition table with precondition, postcondition, and invariant check per transition
  /trace-contract    -> three-directory expected-vs-actual comparison with mismatch severity (CRITICAL/MAJOR/MINOR) per delta
  /trace-component   -> user action traced through component tree with re-render count and state update path
  /trace-deployment  -> deployment sequence with pre-flight checklist, canary validation step, and rollback trigger condition
  /trace-migration   -> schema change with before/after row counts, data loss detection, and rollback SQL
  /trace-permissions -> RBAC matrix showing who can do what with privilege escalation path and gap count

prove -- 9 skills:
  /prove-hypothesis  -> hypothesis card with claim, falsification condition, confidence level (0-100%), and experiment list
  /prove-websearch   -> evidence set with direct quotes, source URLs, and strength-of-evidence rating per source
  /prove-intelligence -> internal evidence with file-path citations, line references, and relevance rating per source
  /prove-prototype   -> prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
  /prove-analysis    -> correlation-vs-causation analysis table with source attribution per finding
  /prove-interview   -> simulated interview transcript per persona with quoted responses grounded in documented roles
  /prove-synthesize  -> answer-first synthesis with overall confidence rating and named counter-evidence list
  /prove-publish     -> paper with abstract, method, findings table, limitations, and implications
  /prove-topic       -> full prove campaign producing hypothesis card through synthesis in one automated command

listen -- 3 skills:
  /listen-feedback  -> pre-ship reaction across 12 customer personas with per-persona NPS prediction and threshold gate verdict
  /listen-support   -> ranked top-10 support tickets for first 90 days with ticket category and gap source
  /listen-adoption  -> adoption curve across 5 Rogers archetypes with chasm gap analysis and crossing strategy

program -- 2 skills:
  /program-plan   -> staged plan with named milestones, gate criteria, and signal tracking per topic
  /prove-program  -> multi-contributor research orchestrator producing contributor assignments and synthesis plan

topic -- 6 skills:
  /topic-new     -> topic registration with strategy document, planned signal list, and coverage roadmap
  /topic-status  -> terminal coverage dashboard: signal count by namespace, gap count, readiness percentage
  /topic-report  -> shareable status document with coverage table, gap list, and readiness statement
  /topic-plan    -> strategy revision with change table per signal and user confirmation before commit
  /topic-story   -> narrative synthesis across all signals with coherence score and design recommendation
  /topic-echo    -> unexpected findings list with source signal and implication per finding

quest -- 4 skills:
  /quest-rubric  -> rubric with C-01+ criteria each having weight, category, and pass condition
  /quest-variate -> N complete prompt variations (default 5) each labeled with axis and hypothesis
  /quest-score   -> per-variation scorecard with composite score, ranked leaderboard, and failure patterns
  /quest-golden  -> full optimization loop producing the converged golden prompt with convergence report

mock -- 3 skills:
  /mock-all     -> synthetic artifacts for all 9 namespaces with coverage percentage per namespace
  /mock-ns      -> single-namespace mock artifact with category annotation and coverage gap summary
  /mock-review  -> namespace-by-namespace verdict: MOCK-ACCEPTED or REAL-REQUIRED with rationale per namespace

org -- 4 skills:
  /org-roles      -> typed role registry with orientation statement, decision lens, and expertise profile per role
  /org-chart      -> org structure with named areas, committee charters, and operating rhythm cadences
  /org-review     -> artifact reviewed through all relevant roles from .craft/roles/ with verdict per role
  /org-committee  -> meeting simulation with agenda items, named participants, and decision per item

BARE MODE: When --bare flag is present, output only the slash-command names as a flat list.
One command per line. No descriptions. No namespace headers. No routing hints.

FILTERED MODE: When a namespace argument is present, output only that namespace's section.
Same format as full index but only one namespace block.
```

---

## V-02 -- C-12 Single-Axis: Blockquote Routing Hints

**Axis**: C-12 -- routing hints formatted as Markdown blockquote (`>`)
**Hypothesis**: Making the blockquote format an explicit FORMAT RULE (not just a convention in the
template data) ensures every routing hint renders as a `>` blockquote. Inline prose routing is
explicitly forbidden. This isolates the effect of enforced blockquote format on C-12 compliance.

```
Show the Signal command index.

INVOCATION:
  /signal             -> full index, all 12 namespaces
  /signal <ns>        -> single namespace only (e.g., /signal flow)
  /signal --bare      -> flat list of command names only, no descriptions

OUTPUT RULES:
1. Full index: emit all 12 namespace sections in order: scout, draft, review, flow, trace,
   prove, listen, program, topic, quest, mock, org.
2. Each namespace section:
   Header:  ## <Namespace> namespace -- <N> skills
   Entries: one per line, format: `/<command>`  <description>
   Routing: see ROUTING FORMAT RULE below.
3. Bare mode: one command name per line, no headers, no descriptions.
4. Filtered mode: emit only the matching namespace section. Same structure as full.
5. Do not invent skills. Do not omit skills. Counts are fixed.

ROUTING FORMAT RULE:
Every namespace section MUST end with a Markdown blockquote routing hint.
The `>` character must appear at the start of the line. Inline prose is not acceptable.
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Run any scout skill directly, or describe your need.

SKILL REGISTRY (authoritative -- do not alter):

## Scout namespace -- 8 skills
`/scout-competitors`   competitive landscape leading with inertia as primary competitor
`/scout-feasibility`   technical feasibility with traffic-light ratings and budget chain
`/scout-naming`        name generation with trademark, domain search, and persona scoring
`/scout-compliance`    regulatory and policy scan before design begins
`/scout-market`        market sizing and segment ranking by fit score
`/scout-stakeholders`  stakeholder map with power/interest grid and veto risk ranking
`/scout-positioning`   per-audience positioning with competitive differentiation
`/scout-requirements`  requirements extraction with MoSCoW prioritization and dependency graph
> Describe your discovery need and the most relevant scout skill will run.

## Draft namespace -- 4 skills
`/draft-spec`        specification authoring with guided section structure and self-review
`/draft-proposal`    proposal or ADR with three-option minimum and recommendation rationale
`/draft-pitch`       pitch deck narrative in exec, developer, and maker versions
`/draft-brainstorm`  idea pool with inertia baseline and peer-comparison scoring
> Describe your authoring need and the most relevant draft skill will run.

## Review namespace -- 4 skills
`/review-design`     multi-expert design review through 6 disciplines and domain-selected experts
`/review-code`       code review with file-level annotations and pass/fail per discipline
`/review-users`      five persona advocates walk through design with usability scores
`/review-customers`  twelve customer personas evaluate for usefulness and would-adopt
> Describe your review artifact and the most relevant review skill will run.

## Flow namespace -- 7 skills
`/flow-lifecycle`    document lifecycle with phase contracts and exception flows
`/flow-conversation` multi-turn agent conversation with dead-end and loop detection
`/flow-trigger`      automation trigger fire order and side effects per event change
`/flow-dataflow`     ETL pipeline tracing with data loss and schema mismatch detection
`/flow-integration`  cross-system integration tracing with gap analysis
`/flow-throttle`     rate-limit throughput with backpressure propagation
`/flow-resilience`   degraded-condition simulation: offline, partial failure, eventual consistency
> Describe your domain process and the most relevant flow skill will run.

## Trace namespace -- 7 skills
`/trace-request`     request hand-compilation through service boundaries, no boundary skipped
`/trace-state`       state transition with preconditions, postconditions, invariants
`/trace-contract`    expected vs actual output comparison with mismatch severity
`/trace-component`   user action through UI component tree and re-render chain
`/trace-deployment`  deployment sequence with pre-checks and rollback path
`/trace-migration`   schema change with before/after data state and data loss detection
`/trace-permissions` RBAC walk-through with privilege escalation detection
> Describe your system behavior and the most relevant trace skill will run.

## Prove namespace -- 9 skills
`/prove-hypothesis`   hypothesis framing with claim, falsification, confidence, and experiments
`/prove-websearch`    web evidence with direct quotes, URLs, and strength-of-evidence per source
`/prove-intelligence` internal source search with file-path citations and relevance assessment
`/prove-prototype`    smallest-possible prototype with predicted vs actual results
`/prove-analysis`     data pattern analysis distinguishing correlation from causation
`/prove-interview`    persona-driven stakeholder interview simulation
`/prove-synthesize`   answer-first synthesis with confidence rating and counter-evidence
`/prove-publish`      write-up as paper with abstract, method, findings, limitations
`/prove-topic`        full prove campaign orchestrating hypothesis through synthesis
> Describe your hypothesis and the most relevant prove skill will run.

## Listen namespace -- 3 skills
`/listen-feedback`  pre-ship customer reaction with per-persona NPS prediction
`/listen-support`   top support ticket prediction for first 90 days
`/listen-adoption`  adoption curve simulation across Rogers archetypes with chasm analysis
> Describe your feature and the most relevant listen skill will run.

## Program namespace -- 2 skills
`/program-plan`   staged program plan with gates and topic tracking
`/prove-program`  general-purpose research orchestrator for open-ended questions
> Describe your program need and the most relevant skill will run.

## Topic namespace -- 6 skills
`/topic-new`     topic registration with strategy planning and signal coverage plan
`/topic-status`  terminal coverage display computed from signal glob
`/topic-report`  shareable status document with progress table and readiness statement
`/topic-plan`    signal strategy revision as new information arrives
`/topic-story`   editorial synthesis of all signals into a coherent narrative
`/topic-echo`    unexpected findings synthesis: what did we learn that we did not expect?
> Describe your topic management need and the most relevant skill will run.

## Quest namespace -- 4 skills
`/quest-rubric`  define what good output looks like: criteria with pass conditions
`/quest-variate` generate N prompt variations of a skill body for comparison
`/quest-score`   score outputs against a rubric with leaderboard and failure patterns
`/quest-golden`  find the golden prompt through systematic variation and scoring
> Describe your optimization goal and the most relevant quest skill will run.

## Mock namespace -- 3 skills
`/mock-all`     synthetic signal artifacts for all 9 namespaces with coverage picture
`/mock-ns`      mock artifact for a single namespace with category annotation
`/mock-review`  coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace
> Describe your coverage need and the most relevant mock skill will run.

## Org namespace -- 4 skills
`/org-roles`      typed role registry with orientation, lens, and expertise
`/org-chart`      org structure with areas, committees, and operating rhythms
`/org-review`     full org review running artifact through all relevant roles
`/org-committee`  committee meeting simulation for ROB, shiproom, or architecture board
> Describe your organizational need and the most relevant org skill will run.
```

---

## V-03 -- C-11 Single-Axis: Purpose Taglines in Namespace Headers

**Axis**: C-11 -- namespace purpose tagline appended to count header
**Hypothesis**: An explicit TAGLINE FORMAT RULE in the prompt (tagline must start with a verb,
be distinct per namespace, answer "what is this namespace for?") ensures C-11 passes reliably.
The rule makes implicit convention explicit, preventing bare-count or generic-suffix outputs.

```
Show the Signal command index. Signal has 12 namespaces and 61 skills.

INVOCATION MODES:
  /signal              full index, all namespaces
  /signal <namespace>  filter to one namespace
  /signal --bare       command names only, one per line

NAMESPACE HEADER FORMAT RULE:
Every namespace header must follow this pattern exactly:
  ### <Namespace> -- <N> skills -- <purpose tagline>

The purpose tagline MUST:
- Start with a verb (discover, author, validate, simulate, trace, prove, hear, orchestrate,
  manage, optimize, generate, model)
- Be distinct from all other namespace taglines
- Answer the question "what is this namespace for?"

  PASS: ### Scout -- 8 skills -- discover what's true before you design
  FAIL: ### Scout -- 8 skills -- scouting and research
  FAIL: ### Scout -- 8 skills (tagline missing)

FULL INDEX: emit one section per namespace.
Each section: header line (per format above) + blank line + skill entries + blank line + routing hint.
Routing hint format: > Describe your <domain noun> and the most relevant <namespace> skill will run.

Descriptions must reference the concrete output artifact or method. No two descriptions may be identical.

---

### Scout -- 8 skills -- discover what's true before you design

/scout-competitors   competitive landscape map with inertia as primary competitor and named rivals with threat ratings
/scout-feasibility   technical feasibility with traffic-light ratings across team, timeline, and budget dimensions
/scout-naming        name shortlist with trademark clearance, domain availability, and per-persona scoring
/scout-compliance    regulatory framework map with applicable laws and enforcement risk before design begins
/scout-market        market sizing with TAM/SAM/SOM and segment table ranked by fit score
/scout-stakeholders  stakeholder map with power/interest grid, veto risk ranking, and influence paths
/scout-positioning   per-audience positioning statements with competitive differentiation and category definition
/scout-requirements  requirements extraction with MoSCoW prioritization, dependency graph, and ambiguity flags

> Describe your discovery need and the most relevant scout skill will run.

---

### Draft -- 4 skills -- author design artifacts from intent

/draft-spec        technical specification with guided section structure, completeness check, and self-review
/draft-proposal    proposal or ADR with problem statement, three-option minimum, and recommendation rationale
/draft-pitch       pitch deck narrative in exec (1-page), developer (technical), and maker (hands-on) versions
/draft-brainstorm  idea pool with inertia baseline, named competitors per idea, and peer-comparison scoring

> Describe your artifact type and the most relevant draft skill will run.

---

### Review -- 4 skills -- validate design and code before committing

/review-design     multi-expert review through 6 standard disciplines plus domain-selected experts
/review-code       code review with file-level annotations, severity rating, and pass/fail per discipline
/review-users      five persona advocates walk through design with usability score and cross-persona synthesis
/review-customers  twelve customer personas each evaluate for usefulness, clarity, and would-adopt

> Describe your review artifact and the most relevant review skill will run.

---

### Flow -- 7 skills -- simulate domain processes before building them

/flow-lifecycle    phase-by-phase document lifecycle with entry/exit contracts and exception flows
/flow-conversation multi-turn agent conversation through topic graph with dead-end and loop detection
/flow-trigger      automation trigger fire order and side-effect table for every field/event change
/flow-dataflow     ETL and sync pipeline tracing with data loss detection and schema mismatch identification
/flow-integration  cross-system integration trace through connectors and APIs with gap analysis and failure modes
/flow-throttle     rate-limit throughput simulation with backpressure propagation and burst path coverage
/flow-resilience   degraded-condition simulation: offline, partial failure, and eventual consistency scenarios

> Describe your domain process and the most relevant flow skill will run.

---

### Trace -- 7 skills -- hand-compile platform behavior step by step

/trace-request     request path hand-compiled through every service boundary with no hop skipped
/trace-state       state machine hand-compilation with preconditions, postconditions, and invariant checks
/trace-contract    three-directory expected-vs-actual comparison with mismatch severity rating per delta
/trace-component   user action traced through UI component tree, state management, and re-render chain
/trace-deployment  deployment sequence with pre-flight checks, canary validation, and rollback path
/trace-migration   schema change with before/after data state, row-count verification, and data loss detection
/trace-permissions RBAC walk-through showing who can do what with privilege escalation and gap detection

> Describe your platform behavior and the most relevant trace skill will run.

---

### Prove -- 9 skills -- gather evidence before claiming something is true

/prove-hypothesis  hypothesis card with claim, falsification condition, confidence level, and experiment list
/prove-websearch   web evidence with direct quotes, source URLs, and strength-of-evidence rating per source
/prove-intelligence internal source search with file-path citations and relevance assessment
/prove-prototype   smallest-possible prototype with defined measure and predicted vs actual results
/prove-analysis    data pattern analysis isolating correlation from causation with source attribution
/prove-interview   persona-driven stakeholder interview simulation grounded in documented role knowledge
/prove-synthesize  answer-first evidence synthesis with confidence rating and named counter-evidence
/prove-publish     investigation write-up as paper with abstract, method, findings, and limitations
/prove-topic       full prove campaign orchestrating hypothesis through synthesis in one command

> Describe your hypothesis and the most relevant prove skill will run.

---

### Listen -- 3 skills -- hear what customers will say before they say it

/listen-feedback  pre-ship customer reaction simulation with per-persona NPS prediction and threshold gate
/listen-support   top support ticket prediction for first 90 days post-ship with gap analysis
/listen-adoption  adoption curve simulation across Rogers archetypes with chasm identification and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

### Program -- 2 skills -- orchestrate multi-topic investigations

/program-plan   staged program plan with milestones, gates, and topic-level signal tracking
/prove-program  general-purpose research orchestrator for open-ended questions requiring multiple contributors

> Describe your program scope and the most relevant skill will run.

---

### Topic -- 6 skills -- manage the narrative across a topic's lifecycle

/topic-new     register a topic with strategy planning, signal inventory, and coverage roadmap
/topic-status  terminal coverage dashboard computed live from signal glob against strategy
/topic-report  shareable status document with coverage table, gap list, and readiness statement
/topic-plan    signal strategy revision as new information arrives with user confirmation before update
/topic-story   editorial synthesis of all signals into a coherent narrative with design recommendation
/topic-echo    unexpected findings synthesis: what did we learn that we did not expect?

> Describe your topic management need and the most relevant skill will run.

---

### Quest -- 4 skills -- improve skill prompts through systematic variation and scoring

/quest-rubric  define what good output looks like: ranked criteria with pass conditions and weights
/quest-variate generate N complete prompt variations of a skill body along specified axes
/quest-score   score N skill outputs against a rubric with leaderboard and failure-pattern detection
/quest-golden  run the full golden prompt loop: variate -> score -> extract -> evolve until convergence

> Describe your optimization goal and the most relevant quest skill will run.

---

### Mock -- 3 skills -- generate synthetic signals when real ones are not ready

/mock-all     full set of synthetic signal artifacts across all 9 namespaces with coverage picture
/mock-ns      single-namespace mock artifact with category annotation and coverage gap summary
/mock-review  coverage review per namespace writing MOCK-ACCEPTED or REAL-REQUIRED with rationale

> Describe your coverage need and the most relevant mock skill will run.

---

### Org -- 4 skills -- model organizational structure and decision processes

/org-roles      typed role registry for a domain with orientation statement, lens, and expertise profile
/org-chart      full org structure with named areas, committee charters, and operating rhythm cadences
/org-review     artifact review run through all relevant roles from the .craft/roles/ registry
/org-committee  committee meeting simulation for ROB, shiproom, or architecture board with agenda and outcomes

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE OUTPUT (when --bare):
Print all 61 command names as a flat list. One per line. No descriptions. No headers. No tips.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Same structure as full index. One section only.
```

---

## V-04 -- Combination: C-11 + C-12 + C-13 (All Three New Criteria)

**Axis**: C-11 + C-12 + C-13 combined
**Hypothesis**: Three explicit enforcement rules for the new aspirational criteria, combined in one
variation, produce a prompt that reliably satisfies all three simultaneously. Single-axis variants
(V-01/V-02/V-03) confirm each rule works in isolation; this combination confirms they do not interfere.

```
Show the Signal command index. Signal has 12 namespaces and 61 skills.

INVOCATION MODES:
  /signal              full index, all namespaces
  /signal <namespace>  filter to one namespace
  /signal --bare       command names only, one per line

THREE ENFORCEMENT RULES -- all must be satisfied simultaneously:

RULE 1 (TAGLINE): Every namespace header must follow this format:
  ### <Namespace> -- <N> skills -- <verb phrase>
  The verb phrase must answer "what is this namespace for?" and be distinct per namespace.
  PASS: ### Scout -- 8 skills -- discover what's true before you design
  FAIL: ### Scout -- 8 skills (no tagline)

RULE 2 (BLOCKQUOTE): Every namespace section must end with a Markdown blockquote:
  > Describe your <domain noun> and the most relevant <namespace> skill will run.
  The `>` must be at line start. Inline prose routing is not acceptable.

RULE 3 (QUANTIFIED): Every sub-skill description must name a specific output --
  a count (5-8 competitors), named format (TAM/SAM/SOM), or rated deliverable (HIGH/MEDIUM/LOW).
  Vague phrases alone ("analysis", "simulation") do not satisfy this rule.

---

### Scout -- 8 skills -- discover what's true before you design

/scout-competitors   competitive landscape map with inertia as primary competitor; 5-8 rivals rated HIGH/MEDIUM/LOW threat
/scout-feasibility   traffic-light ratings (RED/YELLOW/GREEN) across technical, team, timeline, and budget dimensions
/scout-naming        name shortlist with trademark clearance status, domain availability, and per-persona score per name
/scout-compliance    regulatory framework map: applicable laws, enforcement risk rating, and design-blocking constraints
/scout-market        market sizing with TAM/SAM/SOM table and segment ranking by fit score
/scout-stakeholders  power/interest grid with named stakeholders, veto risk rating, and influence path per stakeholder
/scout-positioning   per-audience positioning statement (3+ audiences) with differentiation axis per audience
/scout-requirements  MoSCoW-prioritized requirements list with dependency graph and ambiguity flags

> Describe your discovery need and the most relevant scout skill will run.

---

### Draft -- 4 skills -- author design artifacts from intent

/draft-spec        specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    proposal with 3-option minimum, option comparison table, and recommendation rationale
/draft-pitch       pitch deck in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  idea pool with inertia baseline entry and per-idea peer-comparison score

> Describe your artifact need and the most relevant draft skill will run.

---

### Review -- 4 skills -- validate design and code before committing

/review-design     design review through 6 disciplines with named expert and pass/fail verdict per discipline
/review-code       code review with file-level annotations, severity rating per finding, and pass/fail per discipline
/review-users      5 persona advocates each produce usability score and cross-persona synthesis
/review-customers  12 customer personas each produce would-adopt rating, NPS prediction, and top concern

> Describe your review artifact and the most relevant review skill will run.

---

### Flow -- 7 skills -- simulate domain processes before building them

/flow-lifecycle    phase-by-phase lifecycle with entry/exit contracts, exception flows, and rollback conditions per phase
/flow-conversation multi-turn conversation trace through topic graph with dead-end count and loop detection
/flow-trigger      fire-order list and side-effect table for every field/event change in the trigger set
/flow-dataflow     pipeline stage-by-stage trace with data loss event count and schema mismatch list
/flow-integration  cross-system integration trace with named connector gaps and failure mode per gap
/flow-throttle     throughput table by burst tier with backpressure propagation path and degradation thresholds
/flow-resilience   scenario table for offline, partial failure, and eventual consistency with recovery path per scenario

> Describe your domain process and the most relevant flow skill will run.

---

### Trace -- 7 skills -- hand-compile platform behavior step by step

/trace-request     request path with every service boundary named, hop count, and latency estimate per hop
/trace-state       state transition table with precondition, postcondition, and invariant check per transition
/trace-contract    three-directory expected-vs-actual comparison with mismatch severity (CRITICAL/MAJOR/MINOR) per delta
/trace-component   user action traced through component tree with re-render count and state update path
/trace-deployment  deployment sequence with pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   schema change with before/after row counts, data loss detection, and rollback SQL
/trace-permissions RBAC matrix showing who can do what with privilege escalation path and gap count

> Describe your platform behavior and the most relevant trace skill will run.

---

### Prove -- 9 skills -- gather evidence before claiming something is true

/prove-hypothesis  hypothesis card with claim, falsification condition, confidence (0-100%), and experiment list
/prove-websearch   evidence set with direct quotes, source URLs, and strength-of-evidence rating per source
/prove-intelligence internal evidence with file-path citations, line references, and relevance rating per source
/prove-prototype   prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    correlation-vs-causation analysis table with source attribution per finding
/prove-interview   simulated interview transcript per persona with quoted responses grounded in documented roles
/prove-synthesize  answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     paper with abstract, method, findings table, limitations, and implications
/prove-topic       full prove campaign producing hypothesis card through synthesis in one automated command

> Describe your hypothesis and the most relevant prove skill will run.

---

### Listen -- 3 skills -- hear what customers will say before they say it

/listen-feedback  pre-ship reaction across 12 customer personas with per-persona NPS prediction and threshold gate verdict
/listen-support   ranked top-10 support tickets for first 90 days with ticket category and gap source
/listen-adoption  adoption curve across 5 Rogers archetypes with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

### Program -- 2 skills -- orchestrate multi-topic investigations

/program-plan   staged plan with named milestones, gate criteria, and signal tracking per topic
/prove-program  multi-contributor research orchestrator producing contributor assignments and synthesis plan

> Describe your program scope and the most relevant skill will run.

---

### Topic -- 6 skills -- manage the narrative across a topic's lifecycle

/topic-new     topic registration with strategy document, planned signal list, and coverage roadmap
/topic-status  terminal coverage dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  shareable status document with coverage table, gap list, and readiness statement
/topic-plan    strategy revision with change table per signal and user confirmation before commit
/topic-story   narrative synthesis across all signals with coherence score and design recommendation
/topic-echo    unexpected findings list with source signal and implication per finding

> Describe your topic management need and the most relevant skill will run.

---

### Quest -- 4 skills -- optimize skill prompts through systematic variation and scoring

/quest-rubric  rubric with C-01+ criteria each having weight, category, and pass condition
/quest-variate N complete prompt variations (default 5) labeled with axis and hypothesis
/quest-score   per-variation scorecard with composite score, ranked leaderboard, and failure patterns
/quest-golden  full optimization loop producing the converged golden prompt with convergence report

> Describe your optimization goal and the most relevant quest skill will run.

---

### Mock -- 3 skills -- generate synthetic signals when real data is not yet available

/mock-all     synthetic artifacts for all 9 namespaces with coverage percentage per namespace
/mock-ns      single-namespace mock artifact with category annotation and coverage gap summary
/mock-review  namespace-by-namespace verdict: MOCK-ACCEPTED or REAL-REQUIRED with rationale per namespace

> Describe your coverage need and the most relevant mock skill will run.

---

### Org -- 4 skills -- model organizational structure and decision processes

/org-roles      typed role registry with orientation statement, decision lens, and expertise profile per role
/org-chart      org structure with named areas, committee charters, and operating rhythm cadences
/org-review     artifact reviewed through all relevant roles from .craft/roles/ with verdict per role
/org-committee  meeting simulation with agenda items, named participants, and decision per item

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare): Print all 61 command names, one per line. No descriptions, headers, or blockquotes.
FILTERED MODE (when /signal <namespace>): Print only the matching namespace section. One section only.
```

---

## V-05 -- Full Integration: All 5 Aspirational Criteria + R1 V-05 Excellence Patterns

**Axis**: Full integration -- all 5 aspirational criteria (C-09 through C-13) + R1 V-05 patterns
**Hypothesis**: Explicitly enforcing all five aspirational criteria by rule, combined with the
global routing decision tree (R1 V-04/V-05 pattern), T3 annotations (R1 V-05 pattern), and
the bare-mode order contract (R1 V-05 pattern), produces a prompt that achieves 100% on the v2
rubric. The five rules collectively prevent any aspirational criterion from being missed by omission.

```
Show the Signal command index. Signal has 12 namespaces and 61 skills.

What are you trying to do?
  Research before committing            ->  /scout   (8 skills)
  Author a design artifact              ->  /draft   (4 skills)
  Validate design or code               ->  /review  (4 skills)
  Simulate a domain process             ->  /flow    (7 skills)
  Hand-compile platform behavior        ->  /trace   (7 skills)
  Gather and prove evidence             ->  /prove   (9 skills)
  Hear customer signals before ship     ->  /listen  (3 skills)
  Orchestrate multi-topic work          ->  /program (2 skills)
  Manage topic narrative and coverage   ->  /topic   (6 skills)
  Improve skill prompts                 ->  /quest   (4 skills)
  Generate synthetic coverage           ->  /mock    (3 skills)
  Simulate org structure and review     ->  /org     (4 skills)

Describe what you need and the most relevant skill will run automatically.

INVOCATION MODES:
  /signal                  full index (routing guide + all 12 namespace sections)
  /signal <namespace>      one namespace only (no routing guide; that section only)
  /signal --bare           flat list of all 61 command names, one per line, no other text

FIVE FORMAT RULES -- every rule must be satisfied in every output:

RULE 1 (C-09 COUNT): Every namespace header must embed the skill count.
  Format: ### <Namespace> -- <N> skills -- <tagline>

RULE 2 (C-11 TAGLINE): Every namespace header must end with a purpose tagline starting with a verb.
  The tagline must answer "what is this namespace for?" and be distinct across all 12 namespaces.
  PASS: ### Scout -- 8 skills -- discover what's true before you design
  FAIL: ### Scout -- 8 skills (no tagline)

RULE 3 (C-12 BLOCKQUOTE): Every namespace section must end with a Markdown blockquote routing hint.
  The `>` must be at line start. Inline prose routing hints are not acceptable.
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Run any scout skill directly, or describe your need.

RULE 4 (C-13 QUANTIFIED): Every sub-skill description must name a specific output --
  a count, named format, or rated deliverable. Vague single-word nouns alone are not sufficient.
  PASS: "5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"

RULE 5 (C-10 T3): Skills whose full runbook loads on demand carry  *(T3)*  after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match the order of the sections below.

---

### Scout -- 8 skills -- discover what's true before you design

/scout-competitors   competitive landscape map with inertia as primary competitor; 5-8 rivals rated HIGH/MEDIUM/LOW threat
/scout-feasibility   traffic-light ratings (RED/YELLOW/GREEN) across technical, team, timeline, and budget dimensions
/scout-naming        name shortlist with trademark clearance status, domain availability, and per-persona score per name
/scout-compliance    regulatory framework map: applicable laws, enforcement risk rating, and design-blocking constraints
/scout-market        market sizing with TAM/SAM/SOM table and segment ranking by fit score
/scout-stakeholders  power/interest grid with named stakeholders, veto risk rating, and influence path per stakeholder
/scout-positioning   per-audience positioning statement (3+ audiences) with differentiation axis per audience
/scout-requirements  MoSCoW-prioritized requirements list with dependency graph and ambiguity flags

> Describe your discovery need and the most relevant scout skill will run.

---

### Draft -- 4 skills -- author design artifacts from intent

/draft-spec        specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    proposal with 3-option minimum, option comparison table, and recommendation rationale
/draft-pitch       pitch deck in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  idea pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

### Review -- 4 skills -- validate design and code before committing

/review-design     design review through 6 disciplines with named expert and pass/fail verdict per discipline
/review-code       code review with file-level annotations, severity rating per finding, and pass/fail per discipline
/review-users      5 persona advocates each produce usability score and cross-persona synthesis
/review-customers  12 customer personas each produce would-adopt rating, NPS prediction, and top concern

> Describe your review artifact and the most relevant review skill will run.

---

### Flow -- 7 skills -- simulate domain processes before building them

/flow-lifecycle    phase-by-phase lifecycle with entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation multi-turn conversation trace through topic graph with dead-end count and loop detection
/flow-trigger      fire-order list and side-effect table for every field/event change in the trigger set  *(T3)*
/flow-dataflow     pipeline stage-by-stage trace with data loss event count and schema mismatch list
/flow-integration  cross-system integration trace with named connector gaps and failure mode per gap
/flow-throttle     throughput table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   scenario table for offline, partial failure, and eventual consistency with recovery path per scenario  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

### Trace -- 7 skills -- hand-compile platform behavior step by step

/trace-request     request path with every service boundary named, hop count, and latency estimate per hop
/trace-state       state transition table with precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    three-directory expected-vs-actual comparison with mismatch severity (CRITICAL/MAJOR/MINOR) per delta  *(T3)*
/trace-component   user action traced through component tree with re-render count and state update path
/trace-deployment  deployment sequence with pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   schema change with before/after row counts, data loss detection, and rollback SQL
/trace-permissions RBAC matrix showing who can do what with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

### Prove -- 9 skills -- gather evidence before claiming something is true

/prove-hypothesis  hypothesis card with claim, falsification condition, confidence (0-100%), and experiment list
/prove-websearch   evidence set with direct quotes, source URLs, and strength-of-evidence rating per source
/prove-intelligence internal evidence with file-path citations, line references, and relevance rating per source
/prove-prototype   prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    correlation-vs-causation analysis table with source attribution per finding
/prove-interview   simulated interview transcript per persona with quoted responses grounded in documented roles  *(T3)*
/prove-synthesize  answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     paper with abstract, method, findings table, limitations, and implications
/prove-topic       full prove campaign from hypothesis through synthesis in one automated command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

### Listen -- 3 skills -- hear what customers will say before they say it

/listen-feedback  pre-ship reaction across 12 customer personas with per-persona NPS prediction and threshold gate verdict
/listen-support   ranked top-10 support tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  adoption curve across 5 Rogers archetypes with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

### Program -- 2 skills -- orchestrate multi-topic investigations

/program-plan   staged plan with named milestones, gate criteria, and signal tracking per topic  *(T3)*
/prove-program  multi-contributor research orchestrator producing contributor assignments and synthesis plan

> Describe your program scope and the most relevant skill will run.

---

### Topic -- 6 skills -- manage the narrative across a topic's lifecycle

/topic-new     topic registration with strategy document, planned signal list, and coverage roadmap
/topic-status  terminal coverage dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  shareable status document with coverage table, gap list, and readiness statement
/topic-plan    strategy revision with change table per signal and user confirmation before commit  *(T3)*
/topic-story   narrative synthesis across all signals with coherence score and design recommendation  *(T3)*
/topic-echo    unexpected findings list with source signal and implication per finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

### Quest -- 4 skills -- optimize skill prompts through systematic variation and scoring

/quest-rubric  rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate N complete prompt variations (default 5) labeled with axis and hypothesis
/quest-score   per-variation scorecard with composite score, ranked leaderboard, and failure patterns  *(T3)*
/quest-golden  full optimization loop producing the converged golden prompt with convergence report  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

### Mock -- 3 skills -- generate synthetic signals when real data is not yet available

/mock-all     synthetic artifacts for all 9 namespaces with coverage percentage per namespace  *(T3)*
/mock-ns      single-namespace mock artifact with category annotation and coverage gap summary  *(T3)*
/mock-review  namespace-by-namespace verdict: MOCK-ACCEPTED or REAL-REQUIRED with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

### Org -- 4 skills -- model organizational structure and decision processes

/org-roles      typed role registry with orientation statement, decision lens, and expertise profile per role
/org-chart      org structure with named areas, committee charters, and operating rhythm cadences  *(T3)*
/org-review     artifact reviewed through all relevant roles from .craft/roles/ with verdict per role  *(T3)*
/org-committee  meeting simulation with agenda items, named participants, and decision per item  *(T3)*

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```
