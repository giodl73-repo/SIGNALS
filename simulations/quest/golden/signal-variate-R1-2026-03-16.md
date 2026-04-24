---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-16
round: 1
rubric: simulations/quest/rubrics/signal-rubric-v1-2026-03-16.md
---

# Quest Variate — /signal (Round 1)

**Skill**: `signal` — command index showing all skills by namespace.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v1-2026-03-16.md`
**Axes explored**:
- V-01: Output format — indented-list (single-axis)
- V-02: Phrasing register — declarative/imperative (single-axis)
- V-03: Visual hierarchy — section headers with counts (single-axis)
- V-04: Routing-first framing (combination: routing prominence + count headers)
- V-05: Full integration (format + counts + T3 annotations + routing)

**Canonical sub-skill counts** (per rubric C-02):
scout:8, draft:4, review:4, flow:7, trace:7, prove:9, listen:3, program:2, topic:6, quest:4, mock:3, org:4

---

## V-01 — Output Format: Indented List
**Axis**: Output format
**Hypothesis**: The indented-list format (namespace header + indented arrow-prefixed sub-skills + routing hint) matches the existing CLAUDE.md structure users already know. Familiarity reduces friction and the format naturally satisfies visual hierarchy (C-07) and routing hints (C-08).

```
Show the Signal command index.

MODE DETECTION:
- No args: print the full index, all 12 namespaces.
- One arg (e.g., /signal flow): print only that namespace section.
- --bare flag: print only command names as a flat list, no descriptions, no headers.

FULL INDEX FORMAT -- repeat this pattern for each namespace:

- /<namespace> -- <Namespace> namespace -- <N> skills for <domain purpose>.

  /<sub-skill-1>  -> <one-line description of what it produces>
  /<sub-skill-2>  -> <one-line description of what it produces>
  ...

  Run any sub-skill directly, or describe your <domain noun> and the most relevant <namespace> skill will run.

NAMESPACES AND SKILLS (output exactly these, in this order):

scout -- 8 skills:
  /scout-competitors   -> competitive landscape analysis leading with inertia as primary competitor
  /scout-feasibility   -> technical feasibility with traffic-light ratings and team/timeline assessment
  /scout-naming        -> name generation and evaluation with trademark and domain search
  /scout-compliance    -> regulatory and policy constraint scan before design begins
  /scout-market        -> market sizing and segment ranking by fit score
  /scout-stakeholders  -> stakeholder mapping with power/interest grid and veto risk ranking
  /scout-positioning   -> per-audience positioning statements with competitive differentiation
  /scout-requirements  -> requirements extraction with MoSCoW prioritization and dependency graph

draft -- 4 skills:
  /draft-spec        -> specification authoring with guided section structure and self-review
  /draft-proposal    -> proposal or ADR with three-option minimum and recommendation rationale
  /draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
  /draft-brainstorm  -> idea pool generation with inertia baseline and peer-comparison scoring

review -- 4 skills:
  /review-design     -> multi-expert design review through 6 disciplines and domain-selected experts
  /review-code       -> multi-discipline code review with file-level annotations and pass/fail per discipline
  /review-users      -> five persona advocates walk through design with usability scores
  /review-customers  -> twelve customer personas evaluate for usefulness, clarity, and would-adopt

flow -- 7 skills:
  /flow-lifecycle    -> multi-step business document lifecycle with phase contracts and exception flows
  /flow-conversation -> multi-turn agent conversation simulation with dead-end and loop detection
  /flow-trigger      -> automation trigger fire order and side effects per field/event change
  /flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
  /flow-integration  -> cross-system integration tracing through connectors and APIs with gap analysis
  /flow-throttle     -> rate-limit throughput simulation showing backpressure propagation and burst paths
  /flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

trace -- 7 skills:
  /trace-request     -> request hand-compilation through service boundaries with no boundary skipped
  /trace-state       -> state transition with preconditions, postconditions, and invariant checks
  /trace-contract    -> expected vs actual output comparison with mismatch severity ratings
  /trace-component   -> user action through UI component tree, state management, and re-render chain
  /trace-deployment  -> deployment sequence with pre-checks, validation, and rollback path
  /trace-migration   -> schema change with before/after data state and data loss detection
  /trace-permissions -> RBAC walk-through with privilege escalation detection

prove -- 9 skills:
  /prove-hypothesis  -> hypothesis framing with claim, falsification condition, confidence, and experiments
  /prove-websearch   -> web evidence with direct quotes, URLs, and strength-of-evidence rating per source
  /prove-intelligence -> internal source search with file-path citations and relevance assessment
  /prove-prototype   -> smallest-possible prototype with predicted vs actual results
  /prove-analysis    -> data pattern analysis distinguishing correlation from causation
  /prove-interview   -> persona-driven stakeholder interview simulation grounded in documented roles
  /prove-synthesize  -> answer-first evidence synthesis with confidence rating and counter-evidence
  /prove-publish     -> investigation write-up as paper with abstract, method, findings, and limitations
  /prove-topic       -> full prove campaign orchestrating hypothesis through synthesis in one command

listen -- 3 skills:
  /listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction and threshold gate
  /listen-support   -> top support ticket prediction for first 90 days with gap analysis
  /listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

program -- 2 skills:
  /program-plan   -> staged program plan with gates and topic tracking
  /prove-program  -> general-purpose research orchestrator for open-ended questions

topic -- 6 skills:
  /topic-new     -> topic registration with strategy planning and signal coverage plan
  /topic-status  -> terminal coverage display computed from signal glob against strategy
  /topic-report  -> shareable status document with progress table and readiness statement
  /topic-plan    -> signal strategy revision as new information arrives with user confirmation
  /topic-story   -> editorial synthesis of all signals into a coherent narrative with recommendation
  /topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

quest -- 4 skills:
  /quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
  /quest-variate -> generate N prompt variations of a skill body for comparison
  /quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
  /quest-golden  -> find the golden prompt through systematic variation and scoring

mock -- 3 skills:
  /mock-all     -> synthetic signal artifacts for all 9 namespaces with coverage picture
  /mock-ns      -> mock artifact for a single namespace with category annotation
  /mock-review  -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

org -- 4 skills:
  /org-roles      -> typed role registry with orientation, lens, and expertise for a domain
  /org-chart      -> org structure with areas, committees, and operating rhythms
  /org-review     -> full org review running artifact through all relevant roles
  /org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

BARE MODE: When --bare flag is present, output only the slash-command names as a flat list.
One command per line. No descriptions. No namespace headers. No routing hints.

FILTERED MODE: When a namespace argument is present, output only that namespace's section.
Same format as full index but only one namespace block.
```

---

## V-02 — Phrasing Register: Declarative/Imperative
**Axis**: Phrasing register
**Hypothesis**: Switching from descriptive prose to a purely declarative command table with no soft language reduces ambiguity in what the AI should produce. Imperative phrasing ("output exactly", "do not include") is more precise for controlling output fidelity.

```
You are the Signal command index.

INVOCATION:
  /signal             -> full index, all 12 namespaces
  /signal <ns>        -> single namespace only (e.g., /signal flow)
  /signal --bare      -> flat list of command names only, no descriptions

---

OUTPUT RULES:
1. Full index: print all 12 namespace sections. Order: scout, draft, review, flow, trace,
   prove, listen, program, topic, quest, mock, org.
2. Each namespace section:
   Header:  ## <Namespace> namespace -- <N> skills
   Entries: one per line, format: `/<command>` -- <description>
   Footer:  > Describe your need and the relevant <namespace> skill will run.
3. Bare mode: one command name per line, no headers, no descriptions.
   Format: /<command-name>
4. Filtered mode: emit only the matching namespace section. Same structure as full.
5. Do not invent skills. Do not omit skills. Counts are fixed.

---

SKILL REGISTRY (authoritative -- do not alter):

## Scout namespace -- 8 skills
`/scout-competitors`   -- competitive landscape leading with inertia as primary competitor
`/scout-feasibility`   -- technical feasibility with traffic-light ratings and budget chain
`/scout-naming`        -- name generation with trademark, domain search, and persona scoring
`/scout-compliance`    -- regulatory and policy scan before design begins
`/scout-market`        -- market sizing and segment ranking by fit score
`/scout-stakeholders`  -- stakeholder map with power/interest grid and veto risk ranking
`/scout-positioning`   -- per-audience positioning with competitive differentiation
`/scout-requirements`  -- requirements extraction with MoSCoW prioritization and dependency graph
> Describe your discovery need and the relevant scout skill will run.

## Draft namespace -- 4 skills
`/draft-spec`        -- specification authoring with guided section structure and self-review
`/draft-proposal`    -- proposal or ADR with three-option minimum and recommendation rationale
`/draft-pitch`       -- pitch deck narrative in exec, developer, and maker versions
`/draft-brainstorm`  -- idea pool with inertia baseline and peer-comparison scoring
> Describe your authoring need and the relevant draft skill will run.

## Review namespace -- 4 skills
`/review-design`     -- multi-expert design review through 6 disciplines
`/review-code`       -- code review with file-level annotations and pass/fail per discipline
`/review-users`      -- five persona advocates walk through design with usability scores
`/review-customers`  -- twelve customer personas evaluate for usefulness and would-adopt
> Describe your review need and the relevant review skill will run.

## Flow namespace -- 7 skills
`/flow-lifecycle`    -- document lifecycle with phase contracts and exception flows
`/flow-conversation` -- multi-turn agent conversation with dead-end and loop detection
`/flow-trigger`      -- automation trigger fire order and side effects per event change
`/flow-dataflow`     -- ETL pipeline tracing with data loss and schema mismatch detection
`/flow-integration`  -- cross-system integration tracing with gap analysis
`/flow-throttle`     -- rate-limit throughput with backpressure propagation
`/flow-resilience`   -- degraded-condition simulation: offline, partial failure, eventual consistency
> Describe your domain process and the relevant flow skill will run.

## Trace namespace -- 7 skills
`/trace-request`     -- request hand-compilation through service boundaries, no boundary skipped
`/trace-state`       -- state transition with preconditions, postconditions, invariants
`/trace-contract`    -- expected vs actual output comparison with mismatch severity
`/trace-component`   -- user action through UI component tree and re-render chain
`/trace-deployment`  -- deployment sequence with pre-checks and rollback path
`/trace-migration`   -- schema change with before/after data state and data loss detection
`/trace-permissions` -- RBAC walk-through with privilege escalation detection
> Describe your system behavior and the relevant trace skill will run.

## Prove namespace -- 9 skills
`/prove-hypothesis`  -- hypothesis framing with claim, falsification, confidence, and experiments
`/prove-websearch`   -- web evidence with direct quotes, URLs, strength-of-evidence per source
`/prove-intelligence`-- internal source search with file-path citations and relevance assessment
`/prove-prototype`   -- smallest-possible prototype with predicted vs actual results
`/prove-analysis`    -- data pattern analysis distinguishing correlation from causation
`/prove-interview`   -- persona-driven stakeholder interview simulation
`/prove-synthesize`  -- answer-first synthesis with confidence rating and counter-evidence
`/prove-publish`     -- write-up as paper with abstract, method, findings, limitations
`/prove-topic`       -- full prove campaign orchestrating hypothesis through synthesis
> Describe your hypothesis and the relevant prove skill will run.

## Listen namespace -- 3 skills
`/listen-feedback`  -- pre-ship customer reaction with per-persona NPS prediction
`/listen-support`   -- top support ticket prediction for first 90 days
`/listen-adoption`  -- adoption curve simulation across Rogers archetypes with chasm analysis
> Describe your feature and the relevant listen skill will run.

## Program namespace -- 2 skills
`/program-plan`   -- staged program plan with gates and topic tracking
`/prove-program`  -- general-purpose research orchestrator for open-ended questions
> Describe your program need and the relevant skill will run.

## Topic namespace -- 6 skills
`/topic-new`     -- topic registration with strategy planning and signal coverage plan
`/topic-status`  -- terminal coverage display computed from signal glob
`/topic-report`  -- shareable status document with progress table and readiness statement
`/topic-plan`    -- signal strategy revision as new information arrives
`/topic-story`   -- editorial synthesis of all signals into a coherent narrative
`/topic-echo`    -- unexpected findings synthesis: what did we learn that we did not expect?
> Describe your topic management need and the relevant skill will run.

## Quest namespace -- 4 skills
`/quest-rubric`  -- define what good output looks like: criteria with pass conditions
`/quest-variate` -- generate N prompt variations of a skill body for comparison
`/quest-score`   -- score outputs against a rubric with leaderboard and failure patterns
`/quest-golden`  -- find the golden prompt through systematic variation and scoring
> Describe your optimization goal and the relevant quest skill will run.

## Mock namespace -- 3 skills
`/mock-all`     -- synthetic signal artifacts for all 9 namespaces with coverage picture
`/mock-ns`      -- mock artifact for a single namespace with category annotation
`/mock-review`  -- coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace
> Describe your coverage need and the relevant mock skill will run.

## Org namespace -- 4 skills
`/org-roles`      -- typed role registry with orientation, lens, and expertise
`/org-chart`      -- org structure with areas, committees, and operating rhythms
`/org-review`     -- full org review running artifact through all relevant roles
`/org-committee`  -- committee meeting simulation for ROB, shiproom, or architecture board
> Describe your organizational need and the relevant org skill will run.
```

---

## V-03 — Visual Hierarchy: Section Headers with Skill Counts
**Axis**: Visual hierarchy + namespace headers with counts
**Hypothesis**: Formatting each namespace as a named section with the count prominently in the header (satisfying C-09 aspirational) makes the index easier to scan. Users compare counts against their memory of what's available — putting it in the header removes the need to count manually.

```
Show the Signal command index. Signal has 12 namespaces and 61 skills.

INVOCATION MODES:
  /signal              full index, all namespaces
  /signal <namespace>  filter to one namespace
  /signal --bare       command names only, one per line

FULL INDEX: emit one section per namespace in the order below.

Each section follows this structure:
  ### <Namespace> -- <N> skills -- <purpose phrase>
  (blank line)
  <skill-name>  <description>
  <skill-name>  <description>
  ...
  (blank line)
  > Tip: describe your need and the most relevant <namespace> skill will run.

Descriptions must name the concrete output artifact or method -- not generic phrases.
Two skills may not share the same description text.

---

### Scout -- 8 skills -- discover what's true before you design

/scout-competitors   Competitive landscape map leading with inertia as primary competitor, then 5-8 named competitors with threat ratings
/scout-feasibility   Technical feasibility assessment with traffic-light ratings, team size, timeline, and budget chain
/scout-naming        Name shortlist with trademark clearance, domain availability, and per-persona scoring
/scout-compliance    Regulatory framework scan identifying applicable laws and enforcement risk before design begins
/scout-market        Market sizing with TAM/SAM/SOM and segment ranking by fit score
/scout-stakeholders  Stakeholder map with power/interest grid, influence paths, and veto risk ranking
/scout-positioning   Per-audience positioning statements with competitive differentiation and category definition
/scout-requirements  Requirements extraction from intent with MoSCoW prioritization and dependency graph

> Tip: describe your discovery need and the most relevant scout skill will run.

---

### Draft -- 4 skills -- turn intent into written artifacts

/draft-spec        Technical specification with guided section structure, completeness check, and self-review
/draft-proposal    Proposal or ADR with problem statement, three-option minimum, and recommendation rationale
/draft-pitch       Pitch deck narrative in three versions: exec (1-page), developer (technical), maker (hands-on)
/draft-brainstorm  Idea pool with inertia baseline, named competitors for each idea, and peer-comparison scoring

> Tip: describe your artifact need and the most relevant draft skill will run.

---

### Review -- 4 skills -- validate design and code before committing

/review-design     Multi-expert review through 6 standard disciplines plus domain-selected experts
/review-code       Code review with file-level annotations, severity ratings, and pass/fail per discipline
/review-users      Five persona advocates walk through design producing usability scores and cross-persona synthesis
/review-customers  Twelve customer personas evaluate for usefulness, clarity, and would-adopt with NPS prediction

> Tip: describe your review need and the most relevant review skill will run.

---

### Flow -- 7 skills -- simulate domain processes before building them

/flow-lifecycle    Document lifecycle through phases with contracts, exception flows, and rollback conditions
/flow-conversation Multi-turn agent conversation through topic graph with dead-end and loop detection
/flow-trigger      Automation trigger fire order and side effects for every field/event change
/flow-dataflow     ETL and sync pipeline tracing with data loss detection and schema mismatch identification
/flow-integration  Cross-system integration through connectors and APIs with gap analysis and failure modes
/flow-throttle     Rate-limit throughput simulation showing backpressure propagation and burst path coverage
/flow-resilience   Degraded-condition simulation covering offline, partial failure, and eventual consistency

> Tip: describe your domain process and the most relevant flow skill will run.

---

### Trace -- 7 skills -- hand-compile platform behavior step by step

/trace-request     Request path hand-compiled through every service boundary -- no hop skipped
/trace-state       State machine hand-compilation with preconditions, postconditions, and invariant checks
/trace-contract    Three-directory expected-vs-actual comparison with mismatch severity rating per delta
/trace-component   User action traced through UI component tree, state management, and re-render chain
/trace-deployment  Deployment sequence with pre-flight checks, canary validation, and rollback path
/trace-migration   Schema change with before/after data state, row-count verification, and data loss detection
/trace-permissions RBAC walk-through showing who can do what with privilege escalation and gap detection

> Tip: describe your system behavior and the most relevant trace skill will run.

---

### Prove -- 9 skills -- gather evidence before claiming something is true

/prove-hypothesis  Hypothesis card with claim, falsification condition, confidence level, and experiment list
/prove-websearch   Web evidence gathering with direct quotes, source URLs, and strength-of-evidence per source
/prove-intelligence Internal source search across codebase and docs with file-path citations and relevance assessment
/prove-prototype   Smallest-possible prototype design with defined measure and predicted vs actual results
/prove-analysis    Data pattern analysis isolating correlation from causation with source attribution
/prove-interview   Persona-driven stakeholder interview simulation grounded in documented role knowledge
/prove-synthesize  Answer-first evidence synthesis with confidence rating, supporting evidence, and counter-evidence
/prove-publish     Investigation write-up as paper with abstract, method, findings, limitations, and implications
/prove-topic       Full prove campaign orchestrating hypothesis through synthesis in one automated command

> Tip: describe your hypothesis and the most relevant prove skill will run.

---

### Listen -- 3 skills -- hear what customers will say before they say it

/listen-feedback  Pre-ship customer reaction simulation with per-persona NPS prediction and threshold gate
/listen-support   Top support ticket prediction for the first 90 days post-ship with gap analysis
/listen-adoption  Adoption curve simulation across Rogers archetypes with chasm identification and crossing strategy

> Tip: describe your feature and the most relevant listen skill will run.

---

### Program -- 2 skills -- orchestrate multi-topic investigations

/program-plan   Staged program plan with milestones, gates, and topic-level signal tracking
/prove-program  General-purpose research orchestrator for open-ended questions requiring multiple contributors

> Tip: describe your program scope and the most relevant skill will run.

---

### Topic -- 6 skills -- manage the narrative across a topic's lifecycle

/topic-new     Register a topic: strategy planning, signal inventory, and coverage roadmap
/topic-status  Terminal coverage dashboard computed live from signal glob against strategy
/topic-report  Shareable status document with coverage table, gaps, and readiness statement
/topic-plan    Signal strategy revision as new information arrives, with user confirmation before update
/topic-story   Editorial synthesis of all signals into a coherent narrative with design recommendation
/topic-echo    Unexpected findings synthesis: what did we learn that we did not expect?

> Tip: describe your topic management need and the most relevant skill will run.

---

### Quest -- 4 skills -- improve skill prompts through systematic variation and scoring

/quest-rubric  Define what good output looks like: ranked criteria with pass conditions and weights
/quest-variate Generate N complete prompt variations of a skill body along specified axes
/quest-score   Score N skill outputs against a rubric with leaderboard and failure-pattern detection
/quest-golden  Run the full golden prompt loop: variate -> score -> extract -> evolve until convergence

> Tip: describe your optimization goal and the most relevant quest skill will run.

---

### Mock -- 3 skills -- generate synthetic signals when real ones are not ready

/mock-all     Full set of synthetic signal artifacts across all 9 namespaces with coverage picture
/mock-ns      Single-namespace mock artifact with category annotation and coverage gap summary
/mock-review  Coverage review per namespace writing MOCK-ACCEPTED or REAL-REQUIRED with rationale

> Tip: describe your coverage need and the most relevant mock skill will run.

---

### Org -- 4 skills -- simulate organizational structure and review

/org-roles      Typed role registry for a domain with orientation statement, lens, and expertise profile
/org-chart      Full org structure with named areas, committee charters, and operating rhythm cadences
/org-review     Artifact review run through all relevant roles from the .roles/ registry
/org-committee  Committee meeting simulation for ROB, shiproom, or architecture board with agenda and outcomes

> Tip: describe your organizational need and the most relevant org skill will run.

---

BARE MODE OUTPUT (when --bare):
Print all 61 command names as a flat list. One per line. No descriptions. No headers. No tips.
/scout-competitors
/scout-feasibility
... (all 61)

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Same structure as full index. One section only.
```

---

## V-04 — Combination: Routing-First + Count Headers
**Axis**: Routing prominence + count headers (combination)
**Hypothesis**: Starting with a routing decision tree ("what are you trying to do?") collapses navigation time for users who don't know the namespace taxonomy. Once they pick a category, they see the full section. This front-loads routing guidance (C-08) rather than appending it per section.

```
You are the Signal command index -- a navigation aid, not a simulation artifact.

INVOCATION:
  /signal                 show the full index
  /signal <namespace>     show only that namespace
  /signal --bare          flat list of command names, no other text

---

ROUTING GUIDE (include at top of full-index output only):

Not sure where to start? Signal has 12 namespaces covering the full feature decision lifecycle:

  Research & Discovery  ->  /scout (8 skills)
  Authoring Artifacts   ->  /draft (4 skills)
  Validation & Review   ->  /review (4 skills)
  Process Simulation    ->  /flow (7 skills)
  Platform Tracing      ->  /trace (7 skills)
  Evidence & Proof      ->  /prove (9 skills)
  Customer Signals      ->  /listen (3 skills)
  Program Planning      ->  /program (2 skills)
  Topic Management      ->  /topic (6 skills)
  Prompt Engineering    ->  /quest (4 skills)
  Synthetic Coverage    ->  /mock (3 skills)
  Org Simulation        ->  /org (4 skills)

Describe what you are trying to learn or build and the most relevant skill will run automatically.

---

NAMESPACE SECTIONS (emit all 12, in order):

## /scout -- 8 skills for discovery and research

  /scout-competitors   -> competitive landscape leading with inertia as primary competitor; 5-8 named rivals with threat ratings
  /scout-feasibility   -> technical feasibility with traffic-light ratings, team size, timeline, and budget chain
  /scout-naming        -> name generation with trademark clearance, domain availability, and multi-persona scoring
  /scout-compliance    -> regulatory framework scan identifying applicable laws before design begins
  /scout-market        -> market sizing with TAM/SAM/SOM and segment ranking by fit score
  /scout-stakeholders  -> stakeholder map with power/interest grid, influence paths, and veto risk ranking
  /scout-positioning   -> per-audience positioning statements with competitive differentiation
  /scout-requirements  -> requirements extraction with MoSCoW prioritization and dependency graph

  Describe your discovery need and the most relevant scout skill will run.

## /draft -- 4 skills for authoring design artifacts

  /draft-spec        -> specification with guided section structure, completeness gate, and self-review
  /draft-proposal    -> proposal or ADR with problem statement, three options, and recommendation rationale
  /draft-pitch       -> pitch deck in exec (1-page), developer (technical), and maker (hands-on) versions
  /draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring for each idea

  Describe your artifact need and the most relevant draft skill will run.

## /review -- 4 skills for design and code validation

  /review-design     -> multi-expert review through 6 standard disciplines and domain-selected experts
  /review-code       -> code review with file-level annotations and pass/fail per discipline
  /review-users      -> five persona advocates walk through design with usability scores and synthesis
  /review-customers  -> twelve customer personas evaluate for usefulness, clarity, and would-adopt

  Describe your review need and the most relevant review skill will run.

## /flow -- 7 skills for domain process simulation

  /flow-lifecycle    -> document lifecycle through phases with contracts, exceptions, and rollback
  /flow-conversation -> multi-turn conversation through topic graph with dead-end and loop detection
  /flow-trigger      -> automation trigger fire order and side effects per field/event change
  /flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
  /flow-integration  -> cross-system integration tracing with gap analysis and failure modes
  /flow-throttle     -> rate-limit throughput with backpressure propagation and burst path coverage
  /flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

  Describe your domain scenario and the most relevant flow skill will run.

## /trace -- 7 skills for platform-level hand-compilation

  /trace-request     -> request path through every service boundary -- no hop skipped
  /trace-state       -> state transition with preconditions, postconditions, and invariant checks
  /trace-contract    -> expected vs actual output comparison with mismatch severity per delta
  /trace-component   -> user action through UI component tree, state management, and re-render chain
  /trace-deployment  -> deployment sequence with pre-checks, validation, and rollback path
  /trace-migration   -> schema change with before/after data state and data loss detection
  /trace-permissions -> RBAC walk-through showing who can do what with privilege escalation detection

  Describe your system behavior and the most relevant trace skill will run.

## /prove -- 9 skills for hypothesis-driven investigation

  /prove-hypothesis  -> hypothesis card with claim, falsification condition, confidence, and experiments
  /prove-websearch   -> web evidence with direct quotes, URLs, and strength-of-evidence per source
  /prove-intelligence -> internal source search with file-path citations and relevance assessment
  /prove-prototype   -> smallest-possible prototype with defined measure and predicted vs actual results
  /prove-analysis    -> data pattern analysis isolating correlation from causation with source attribution
  /prove-interview   -> persona-driven stakeholder interview simulation grounded in documented roles
  /prove-synthesize  -> answer-first synthesis with confidence rating and counter-evidence
  /prove-publish     -> investigation write-up as paper with abstract, method, findings, limitations
  /prove-topic       -> full prove campaign orchestrating hypothesis through synthesis in one command

  Describe your hypothesis and the most relevant prove skill will run.

## /listen -- 3 skills for customer signal simulation

  /listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction and threshold gate
  /listen-support   -> top support ticket prediction for first 90 days with gap analysis
  /listen-adoption  -> adoption curve across Rogers archetypes with chasm analysis and crossing strategy

  Describe your feature and the most relevant listen skill will run.

## /program -- 2 skills for orchestration and planning

  /program-plan   -> staged program plan with milestones, gates, and topic-level signal tracking
  /prove-program  -> general-purpose research orchestrator for open-ended multi-contributor questions

  Describe your program scope and the most relevant skill will run.

## /topic -- 6 skills for narrative management

  /topic-new     -> topic registration with strategy planning and signal coverage roadmap
  /topic-status  -> terminal coverage dashboard computed live from signal glob vs strategy
  /topic-report  -> shareable status document with coverage table, gaps, and readiness statement
  /topic-plan    -> signal strategy revision as new information arrives, confirmed before update
  /topic-story   -> editorial synthesis of all signals into a coherent narrative with recommendation
  /topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

  Describe your topic management need and the most relevant skill will run.

## /quest -- 4 skills for prompt engineering and golden prompt discovery

  /quest-rubric  -> scoring rubric definition: ranked criteria with weights and pass conditions
  /quest-variate -> N complete prompt variations along specified axes for side-by-side comparison
  /quest-score   -> per-criterion scoring of N outputs with composite leaderboard and failure patterns
  /quest-golden  -> full optimization loop: variate -> score -> extract -> evolve rubric -> converge

  Describe your optimization goal and the most relevant quest skill will run.

## /mock -- 3 skills for synthetic signal generation

  /mock-all     -> synthetic signal artifacts across all 9 namespaces with coverage picture
  /mock-ns      -> single-namespace mock with category annotation and coverage gap summary
  /mock-review  -> coverage review per namespace: MOCK-ACCEPTED or REAL-REQUIRED with rationale

  Describe your coverage need and the most relevant mock skill will run.

## /org -- 4 skills for organizational simulation

  /org-roles      -> typed role registry with orientation, lens, and expertise per role
  /org-chart      -> org structure with named areas, committee charters, and operating rhythms
  /org-review     -> artifact review through all relevant roles from the .roles/ registry
  /org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

  Describe your organizational need and the most relevant org skill will run.

---

BARE MODE: When --bare, output only command names. One per line. No descriptions, headers, or routing text.
FILTERED MODE: When given a namespace name, output only that namespace's section (including routing tip). No routing guide, no other sections.
```

---

## V-05 — Full Integration: Format + Counts + T3 Annotations + Routing
**Axis**: All axes combined
**Hypothesis**: Integrating the indented-list format (V-01), count-in-header (V-03), explicit routing guide (V-04), and T3 tier annotations (C-10 aspirational) produces the highest composite score. The T3 marker tells users which skills load an extended runbook on demand -- important for managing expectations on first run.

```
You are the Signal command index. Output depends on invocation:

  /signal              -> full index: all 12 namespaces, all 61 skills
  /signal <namespace>  -> filtered: one namespace section only
  /signal --bare       -> bare: command names only, one per line, nothing else

---

ROUTING GUIDE (full-index mode only, print at top before namespace sections):

Signal covers the full feature intelligence lifecycle. 12 namespaces, 61 skills.

  What are you trying to do?
  - Research before committing   -> /scout (8 skills)
  - Write a design artifact       -> /draft (4 skills)
  - Validate design or code       -> /review (4 skills)
  - Simulate a domain process     -> /flow (7 skills)
  - Trace platform behavior       -> /trace (7 skills)
  - Gather and weigh evidence     -> /prove (9 skills)
  - Hear the customer voice       -> /listen (3 skills)
  - Plan a multi-topic program    -> /program (2 skills)
  - Manage the topic narrative    -> /topic (6 skills)
  - Optimize a skill prompt       -> /quest (4 skills)
  - Generate synthetic coverage   -> /mock (3 skills)
  - Simulate org structure        -> /org (4 skills)

  Not sure? Describe what you need and the most relevant skill will run.

---

NAMESPACE SECTIONS (print all 12 in full mode, one in filtered mode):

Format per namespace:
  ## <Namespace> namespace -- <N> skills -- <purpose>
  (blank line)
    /<sub-skill>  -> <specific description of output artifact or method> [*(T3)*]
    ...
  (blank line)
  > Describe your <domain noun> and the most relevant <namespace> skill will run.

T3 ANNOTATION RULE: skills whose full runbook loads on demand carry *(T3)* after the description.
T3 skills: flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
           trace-state, trace-contract, trace-permissions,
           prove-interview, prove-topic, listen-support,
           program-plan, topic-plan, topic-story, topic-echo,
           mock-all, mock-ns, mock-review,
           org-chart, org-review, org-committee,
           quest-rubric, quest-score, quest-golden,
           draft-brainstorm.

---

## Scout namespace -- 8 skills -- discover what's true before you design

  /scout-competitors   -> competitive landscape map leading with inertia as primary competitor; 5-8 rivals with threat ratings (HIGH/MEDIUM/LOW)
  /scout-feasibility   -> technical feasibility with traffic-light ratings per dimension, team size, timeline, and budget chain
  /scout-naming        -> name generation with trademark clearance, domain search, and multi-persona scoring
  /scout-compliance    -> regulatory and policy scan identifying applicable laws and enforcement risk
  /scout-market        -> market sizing with TAM/SAM/SOM segments ranked by fit score
  /scout-stakeholders  -> stakeholder map with power/interest grid, influence paths, and veto risk ranking
  /scout-positioning   -> per-audience positioning statements with competitive differentiation and category framing
  /scout-requirements  -> requirements extraction from intent with MoSCoW prioritization and dependency graph

  > Describe your discovery need and the most relevant scout skill will run.

## Draft namespace -- 4 skills -- turn intent into written artifacts

  /draft-spec        -> specification with guided section structure, completeness gate, and self-review checklist
  /draft-proposal    -> proposal or ADR with problem statement, three-option minimum, and recommendation rationale
  /draft-pitch       -> pitch deck in exec (1-page), developer (technical), and maker (hands-on) versions
  /draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring for each candidate idea *(T3)*

  > Describe your artifact need and the most relevant draft skill will run.

## Review namespace -- 4 skills -- validate design and code before committing

  /review-design     -> multi-expert design review through 6 standard disciplines plus domain-selected experts
  /review-code       -> code review with file-level annotations, severity ratings, and pass/fail per discipline
  /review-users      -> five persona advocates walk through design with usability scores and cross-persona synthesis
  /review-customers  -> twelve customer personas evaluate for usefulness, clarity, and would-adopt with NPS

  > Describe your review need and the most relevant review skill will run.

## Flow namespace -- 7 skills -- simulate domain processes before building them

  /flow-lifecycle    -> document lifecycle through phase contracts with exception flows and rollback conditions *(T3)*
  /flow-conversation -> multi-turn conversation through topic graph with dead-end and infinite-loop detection
  /flow-trigger      -> automation trigger fire order and side effects for every field/event change *(T3)*
  /flow-dataflow     -> ETL and sync pipeline tracing with data loss detection and schema mismatch identification
  /flow-integration  -> cross-system integration tracing through connectors and APIs with gap analysis
  /flow-throttle     -> rate-limit throughput showing backpressure propagation and burst path coverage *(T3)*
  /flow-resilience   -> degraded-condition simulation covering offline, partial failure, and eventual consistency *(T3)*

  > Describe your domain scenario and the most relevant flow skill will run.

## Trace namespace -- 7 skills -- hand-compile platform behavior step by step

  /trace-request     -> request path through every service boundary -- no hop skipped, latency annotated
  /trace-state       -> state machine hand-compilation with preconditions, postconditions, and invariant checks *(T3)*
  /trace-contract    -> three-directory expected-vs-actual comparison with mismatch severity per delta *(T3)*
  /trace-component   -> user action traced through UI component tree, state management, and re-render chain
  /trace-deployment  -> deployment sequence with pre-flight checks, canary validation, and rollback path
  /trace-migration   -> schema change with before/after row counts, data state, and loss detection
  /trace-permissions -> RBAC walk-through mapping who can do what with privilege escalation detection *(T3)*

  > Describe your system behavior and the most relevant trace skill will run.

## Prove namespace -- 9 skills -- gather evidence before claiming something is true

  /prove-hypothesis  -> hypothesis card with claim, falsification condition, confidence level, and experiment list
  /prove-websearch   -> web evidence gathering with direct quotes, source URLs, and strength-of-evidence per source
  /prove-intelligence -> internal source search with file-path citations and relevance assessment
  /prove-prototype   -> smallest-possible prototype with defined measure and predicted vs actual results
  /prove-analysis    -> data pattern analysis isolating correlation from causation with source attribution
  /prove-interview   -> persona-driven stakeholder interview simulation grounded in documented role knowledge *(T3)*
  /prove-synthesize  -> answer-first evidence synthesis with confidence rating, supporting evidence, counter-evidence
  /prove-publish     -> investigation write-up as paper with abstract, method, findings, limitations, implications
  /prove-topic       -> full prove campaign orchestrating hypothesis through synthesis in one command *(T3)*

  > Describe your hypothesis and the most relevant prove skill will run.

## Listen namespace -- 3 skills -- hear what customers will say before they say it

  /listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction and threshold gate
  /listen-support   -> top support ticket prediction for first 90 days with gap analysis *(T3)*
  /listen-adoption  -> adoption curve across Rogers archetypes with chasm identification and crossing strategy

  > Describe your feature and the most relevant listen skill will run.

## Program namespace -- 2 skills -- orchestrate multi-topic investigations

  /program-plan   -> staged program plan with milestones, gates, and topic-level signal tracking *(T3)*
  /prove-program  -> general-purpose research orchestrator for open-ended multi-contributor questions

  > Describe your program scope and the most relevant skill will run.

## Topic namespace -- 6 skills -- manage the narrative across a topic's lifecycle

  /topic-new     -> topic registration with strategy planning and signal coverage roadmap
  /topic-status  -> terminal coverage dashboard computed live from signal glob vs strategy file
  /topic-report  -> shareable status document with coverage table, gaps, and readiness statement
  /topic-plan    -> signal strategy revision as new information arrives, confirmed before update *(T3)*
  /topic-story   -> editorial synthesis of all signals into a coherent narrative with design recommendation *(T3)*
  /topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect? *(T3)*

  > Describe your topic management need and the most relevant skill will run.

## Quest namespace -- 4 skills -- optimize skill prompts through systematic variation and scoring

  /quest-rubric  -> scoring rubric with ranked criteria, weights (essential/recommended/aspirational), and pass conditions *(T3)*
  /quest-variate -> N complete prompt variations of a skill body along specified axes for side-by-side comparison
  /quest-score   -> per-criterion scoring of N outputs with composite leaderboard and failure-pattern detection *(T3)*
  /quest-golden  -> full optimization loop: variate -> score -> extract excellence -> evolve rubric -> converge *(T3)*

  > Describe your optimization goal and the most relevant quest skill will run.

## Mock namespace -- 3 skills -- generate synthetic signals when real ones are not ready

  /mock-all     -> synthetic signal artifacts across all 9 namespaces with coverage picture and gap summary *(T3)*
  /mock-ns      -> single-namespace mock artifact with category annotation and coverage gap analysis *(T3)*
  /mock-review  -> coverage review per namespace writing MOCK-ACCEPTED or REAL-REQUIRED with rationale *(T3)*

  > Describe your coverage need and the most relevant mock skill will run.

## Org namespace -- 4 skills -- simulate organizational structure and review

  /org-roles      -> typed role registry with orientation statement, lens, and expertise profile per role
  /org-chart      -> org structure with named areas, committee charters, and operating rhythm cadences *(T3)*
  /org-review     -> artifact review through all relevant roles from the .roles/ registry *(T3)*
  /org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board with decisions *(T3)*

  > Describe your organizational need and the most relevant org skill will run.

---

BARE MODE: print all 61 command names, one per line, no other text.
  Begin with /scout-competitors and end with /org-committee.
  Order: scout (8), draft (4), review (4), flow (7), trace (7), prove (9),
         listen (3), program (2), topic (6), quest (4), mock (3), org (4).

FILTERED MODE: print only the matching namespace section (including its routing tip).
  Include the T3 annotations. Omit the routing guide and all other sections.
```

---

## Variation Summary

| ID   | Axis                         | Key Hypothesis                                          | C-09? | C-10? | C-08? |
|------|------------------------------|---------------------------------------------------------|-------|-------|-------|
| V-01 | Output format: indented list  | Familiar CLAUDE.md format satisfies C-07 natively      | No    | No    | Yes   |
| V-02 | Phrasing: declarative         | Imperative rules produce more complete, less drifting output | No | No  | Yes   |
| V-03 | Visual hierarchy: count header| Count-in-header is the fastest way to satisfy C-09     | Yes   | No    | Yes   |
| V-04 | Routing-first + count headers | Front-loading routing guide reduces navigation time    | Yes   | No    | Yes*  |
| V-05 | Full integration              | Combining all axes maximizes composite score           | Yes   | Yes   | Yes   |

*V-04 routing guide is global rather than per-section; per-section tips still present.
