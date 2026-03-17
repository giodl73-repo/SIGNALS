---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-16
round: 3
rubric: simulations/quest/rubrics/signal-rubric-v3-2026-03-16.md
---

# Quest Variate -- /signal (Round 3)

**Skill**: `signal` -- command index showing all skills by namespace.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v3-2026-03-16.md`
**Rubric changes from v2**: Added C-14 (bi-directional descriptions: mechanism + deliverable),
C-15 (mutually distinguishable taglines); aspirational denominator updated from 5 to 7.

**Context**: R2 champion was V-05 (100 pts on v2). All R2 aspirational criteria (C-09 through C-13)
are carried forward as the established base. The two new criteria emerged from R2 excellence signals:
- C-14 from V-04 C-06 evidence: compound rules produced descriptions with two specificity dimensions
  simultaneously (mechanism + deliverable). This wasn't enforced by rule -- it happened structurally.
- C-15 from V-04 C-07 evidence: taglines that are namespace-locked reinforce hierarchy because each
  header carries a unique identity. C-11 requires a tagline; C-15 requires it to be irreplaceable.

**Axes explored**:
- V-01: C-14 single-axis -- bi-directional descriptions (explicit BIDIR RULE: mechanism + deliverable)
- V-02: C-15 single-axis -- mutually distinguishable taglines (explicit SWAP TEST rule)
- V-03: C-14 + C-15 combination -- both new criteria enforced, confirm no interference
- V-04: Full integration -- R2 V-05 base + C-14 RULE + C-15 RULE (all 7 aspirational)
- V-05: Structural pre-print -- two-part description format that enforces C-14 mechanically;
         uniqueness-anchored tagline pre-prints that enforce C-15 mechanically

**Canonical sub-skill counts** (per rubric C-02):
scout:8, draft:4, review:4, flow:7, trace:7, prove:9, listen:3, program:2, topic:6, quest:4, mock:3, org:4

---

## V-01 -- C-14 Single-Axis: Bi-directional Descriptions

**Axis**: C-14 -- every description names both mechanism AND deliverable
**Hypothesis**: Adding an explicit BIDIR RULE ("every description must answer BOTH what the
skill does AND what you receive") ensures descriptions carry two specificity dimensions
simultaneously. R2 descriptions often had one or the other; a rule forces both.

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

BIDIR RULE (C-14): Every sub-skill description must be BI-DIRECTIONAL.
  It must name BOTH the mechanism (what the skill does -- a verb phrase) AND the
  deliverable (what you receive -- a specific noun phrase with count, format, or rating).
  Test: Does this description answer BOTH "what does it do?" AND "what do I get back?"
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  PASS: "simulates 12 customer personas -> per-persona NPS prediction and threshold gate verdict"
  FAIL: "competitive landscape analysis" (mechanism present, deliverable absent)
  FAIL: "5-8 rivals with threat ratings" (deliverable present, mechanism absent)

FOUR FORMAT RULES -- all must be satisfied in every output:
RULE 1 (C-09 COUNT): Every namespace header embeds the skill count.
  Format: ### <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11 TAGLINE): Every namespace header ends with a purpose tagline starting with a verb.
  The tagline must answer "what is this namespace for?" and be distinct across all 12 namespaces.
RULE 3 (C-12 BLOCKQUOTE): Every namespace section ends with a Markdown blockquote routing hint.
  The > must be at line start. Inline prose routing hints are not acceptable.
RULE 4 (C-10 T3): Skills whose full runbook loads on demand carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.

---

### Scout -- 8 skills -- discover what's true before you design

/scout-competitors   scans competitive landscape with inertia-first framing -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat
/scout-feasibility   assesses technical, team, and timeline constraints -> traffic-light ratings (RED/YELLOW/GREEN) per dimension
/scout-naming        generates name candidates and validates them -> shortlist with trademark clearance, domain status, and per-persona score
/scout-compliance    maps regulatory obligations for a domain -> applicable laws with enforcement risk rating and design-blocking constraints
/scout-market        sizes the addressable market -> TAM/SAM/SOM table with segments ranked by fit score
/scout-stakeholders  identifies decision-makers and their relationships -> power/interest grid with veto risk rating and influence path per stakeholder
/scout-positioning   frames the product for each target audience -> 3+ positioning statements with competitive differentiation axis per audience
/scout-requirements  extracts and classifies feature requirements -> MoSCoW-prioritized list with dependency graph and ambiguity flags

> Describe your discovery need and the most relevant scout skill will run.

---

### Draft -- 4 skills -- author design artifacts from intent

/draft-spec        structures intent into a specification -> document with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates and scores idea candidates -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

### Review -- 4 skills -- validate design and code before committing

/review-design     runs design through 6 expert lenses -> named expert verdict with pass/fail per discipline
/review-code       annotates code at file level -> findings with severity rating and pass/fail per discipline
/review-users      simulates 5 persona advocates walking through the design -> usability score per persona with cross-persona synthesis
/review-customers  simulates 12 customer personas evaluating the feature -> would-adopt rating, NPS prediction, and top concern per persona

> Describe your review artifact and the most relevant review skill will run.

---

### Flow -- 7 skills -- simulate domain processes before building them

/flow-lifecycle    traces a document lifecycle phase by phase -> entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation simulates a multi-turn agent conversation -> topic graph traversal with dead-end count and loop detection
/flow-trigger      fires a trigger set against a domain model -> fire-order list and side-effect table per field/event change  *(T3)*
/flow-dataflow     traces an ETL or sync pipeline stage by stage -> data loss event count and schema mismatch list per stage
/flow-integration  traces cross-system integration paths -> named connector gaps and failure mode per integration boundary
/flow-throttle     models rate-limit and backpressure behavior -> throughput table by burst tier with backpressure path and degradation thresholds  *(T3)*
/flow-resilience   injects degraded conditions into a process model -> scenario table with recovery path for offline, partial failure, and eventual consistency  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

### Trace -- 7 skills -- hand-compile platform behavior step by step

/trace-request     compiles the request path hop by hop -> named service boundaries with hop count and latency estimate per hop
/trace-state       walks a state machine through its transitions -> precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    compares expected vs actual output using three-directory pattern -> mismatch severity (CRITICAL/MAJOR/MINOR) per delta  *(T3)*
/trace-component   follows a user action through the UI component tree -> re-render count and state update path per component
/trace-deployment  steps through a deployment sequence -> pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   applies a schema change to sample data -> before/after row counts, data loss detection, and rollback SQL
/trace-permissions walks RBAC rules for a principal and action set -> who-can-do-what matrix with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

### Prove -- 9 skills -- gather evidence before claiming something is true

/prove-hypothesis  frames a falsifiable belief -> hypothesis card with confidence (0-100%), falsification condition, and experiment list
/prove-websearch   queries the web for evidence -> direct quotes with source URLs and strength-of-evidence rating per source
/prove-intelligence searches internal codebase and docs -> file-path citations with line references and relevance rating per source
/prove-prototype   builds the smallest testable artifact -> prototype spec with defined measure and actual-vs-predicted result comparison
/prove-analysis    examines a data set for patterns -> correlation-vs-causation table with source attribution per finding
/prove-interview   runs persona-driven stakeholder interviews -> simulated transcript with quoted responses grounded in documented roles  *(T3)*
/prove-synthesize  weighs all gathered evidence -> answer-first synthesis with confidence rating and named counter-evidence list
/prove-publish     writes up an investigation as a paper -> document with abstract, method, findings table, limitations, and implications
/prove-topic       orchestrates a full evidence campaign -> hypothesis card through synthesis in one automated multi-step command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

### Listen -- 3 skills -- hear what customers will say before they say it

/listen-feedback  simulates pre-ship customer reactions -> per-persona NPS prediction across 12 personas with threshold gate verdict
/listen-support   predicts post-ship support load -> ranked top-10 tickets for first 90 days with category and gap source  *(T3)*
/listen-adoption  models the adoption progression -> Rogers archetype curve with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

### Program -- 2 skills -- coordinate multi-skill investigations across a topic

/program-plan   structures a multi-topic program of work -> staged plan with named milestones, gate criteria, and signal tracking per topic  *(T3)*
/prove-program  orchestrates open-ended research -> multi-contributor assignment plan with synthesis strategy

> Describe your program scope and the most relevant skill will run.

---

### Topic -- 6 skills -- track signal coverage and synthesize the story as evidence accumulates

/topic-new     registers a topic for tracking -> strategy document with planned signal list and coverage roadmap
/topic-status  computes live coverage -> terminal dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  generates a progress snapshot -> shareable document with coverage table, gap list, and readiness statement
/topic-plan    revises the signal strategy -> change table per signal with user confirmation before commit  *(T3)*
/topic-story   synthesizes all signals into a narrative -> coherent story with coherence score and design recommendation  *(T3)*
/topic-echo    surfaces unexpected findings -> list with source signal and implication per unexpected finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

### Quest -- 4 skills -- evolve skill prompts from draft to golden through systematic testing

/quest-rubric  defines what good output looks like -> rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate generates prompt alternatives -> N complete variations labeled with variation axis and hypothesis
/quest-score   scores variations against rubric -> per-variation scorecard with composite score, leaderboard, and failure patterns  *(T3)*
/quest-golden  runs the optimization loop -> converged golden prompt with convergence report  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

### Mock -- 3 skills -- fill coverage gaps with synthetic signals when real data is unavailable

/mock-all     generates full synthetic coverage -> artifacts for all 9 namespaces with coverage percentage per namespace  *(T3)*
/mock-ns      generates a namespace-scoped mock artifact -> single-namespace document with category annotation and coverage gap summary  *(T3)*
/mock-review  audits mock coverage quality -> MOCK-ACCEPTED or REAL-REQUIRED verdict with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

### Org -- 4 skills -- model roles, hierarchy, and decision processes in a simulated organization

/org-roles      defines the role landscape -> typed registry with orientation statement, decision lens, and expertise profile per role
/org-chart      builds an org structure -> named areas with committee charters and operating rhythm cadences  *(T3)*
/org-review     routes an artifact through relevant roles -> verdict per role from .craft/roles/ registry  *(T3)*
/org-committee  runs a committee meeting -> agenda items with named participants and decision per item  *(T3)*

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```

---

## V-02 -- C-15 Single-Axis: Mutually Distinguishable Taglines

**Axis**: C-15 -- each namespace tagline is namespace-locked; no two are interchangeable
**Hypothesis**: An explicit SWAP TEST rule ("before writing each tagline, verify it cannot
credibly apply to any other namespace") forces taglines to capture what is *uniquely* true
about each namespace. Without the rule, generic verb phrases like "research and analyze"
could appear in both scout and prove. The swap test makes the uniqueness constraint
operational rather than aspirational.

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

TAGLINE DISTINCTNESS RULE (C-15): Every namespace tagline must be NAMESPACE-LOCKED.
  Apply the SWAP TEST: if you placed this tagline on any other namespace header, would it
  be obviously wrong? If the tagline could plausibly fit a different namespace, reject it.
  - LOCKED: "map the competitive and regulatory landscape before the first design decision"
    (cannot apply to prove, flow, trace, or any other namespace)
  - GENERIC (fail): "gather and analyze relevant information" (could be scout, prove, or trace)
  Taglines must name the namespace's unique contribution, not its general activity class.

FOUR FORMAT RULES -- all must be satisfied in every output:
RULE 1 (C-09 COUNT): Every namespace header embeds the skill count.
  Format: ### <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11 TAGLINE): Every namespace header ends with a purpose tagline starting with a verb.
  Combined with TAGLINE DISTINCTNESS RULE: the tagline must also pass the SWAP TEST.
RULE 3 (C-12 BLOCKQUOTE): Every namespace section ends with a Markdown blockquote routing hint.
  The > must be at line start.
RULE 4 (C-10 T3): T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.

---

### Scout -- 8 skills -- map the competitive and regulatory landscape before design begins

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

### Draft -- 4 skills -- commit design intent to a written artifact before implementation

/draft-spec        specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    proposal with 3-option minimum, option comparison table, and recommendation rationale
/draft-pitch       pitch deck in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  idea pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

### Review -- 4 skills -- challenge a design or codebase through structured expert critique

/review-design     design review through 6 disciplines with named expert and pass/fail verdict per discipline
/review-code       code review with file-level annotations, severity rating per finding, and pass/fail per discipline
/review-users      5 persona advocates each produce usability score and cross-persona synthesis
/review-customers  12 customer personas each produce would-adopt rating, NPS prediction, and top concern

> Describe your review artifact and the most relevant review skill will run.

---

### Flow -- 7 skills -- simulate domain process behavior before writing the first line of code

/flow-lifecycle    phase-by-phase lifecycle with entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation multi-turn conversation trace through topic graph with dead-end count and loop detection
/flow-trigger      fire-order list and side-effect table for every field/event change in the trigger set  *(T3)*
/flow-dataflow     pipeline stage-by-stage trace with data loss event count and schema mismatch list
/flow-integration  cross-system integration trace with named connector gaps and failure mode per gap
/flow-throttle     throughput table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   scenario table for offline, partial failure, and eventual consistency with recovery path  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

### Trace -- 7 skills -- step through platform implementation mechanics before assumptions harden

/trace-request     request path with every service boundary named, hop count, and latency estimate per hop
/trace-state       state transition table with precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    three-directory expected-vs-actual comparison with mismatch severity (CRITICAL/MAJOR/MINOR) per delta  *(T3)*
/trace-component   user action traced through component tree with re-render count and state update path
/trace-deployment  deployment sequence with pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   schema change with before/after row counts, data loss detection, and rollback SQL
/trace-permissions RBAC matrix showing who can do what with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

### Prove -- 9 skills -- frame a hypothesis and build an evidence case before claiming certainty

/prove-hypothesis  hypothesis card with claim, falsification condition, confidence (0-100%), and experiment list
/prove-websearch   evidence set with direct quotes, source URLs, and strength-of-evidence rating per source
/prove-intelligence internal evidence with file-path citations, line references, and relevance rating per source
/prove-prototype   prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    correlation-vs-causation analysis table with source attribution per finding
/prove-interview   simulated interview transcript per persona with quoted responses grounded in documented roles  *(T3)*
/prove-synthesize  answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     paper with abstract, method, findings table, limitations, and implications
/prove-topic       full prove campaign producing hypothesis card through synthesis in one automated command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

### Listen -- 3 skills -- predict what customers will say before they have the chance to say it

/listen-feedback  pre-ship reaction across 12 customer personas with per-persona NPS prediction and threshold gate verdict
/listen-support   ranked top-10 support tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  adoption curve across 5 Rogers archetypes with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

### Program -- 2 skills -- coordinate multi-skill investigations into a staged plan with gates

/program-plan   staged plan with named milestones, gate criteria, and signal tracking per topic  *(T3)*
/prove-program  multi-contributor research orchestrator producing contributor assignments and synthesis plan

> Describe your program scope and the most relevant skill will run.

---

### Topic -- 6 skills -- track accumulated signals and synthesize them into a decision-ready story

/topic-new     topic registration with strategy document, planned signal list, and coverage roadmap
/topic-status  terminal coverage dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  shareable status document with coverage table, gap list, and readiness statement
/topic-plan    strategy revision with change table per signal and user confirmation before commit  *(T3)*
/topic-story   narrative synthesis across all signals with coherence score and design recommendation  *(T3)*
/topic-echo    unexpected findings list with source signal and implication per finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

### Quest -- 4 skills -- test skill prompts against criteria until the best version emerges

/quest-rubric  rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate N complete prompt variations (default 5) labeled with axis and hypothesis
/quest-score   per-variation scorecard with composite score, ranked leaderboard, and failure patterns  *(T3)*
/quest-golden  full optimization loop producing the converged golden prompt with convergence report  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

### Mock -- 3 skills -- generate placeholder signals when real evidence collection is blocked

/mock-all     synthetic artifacts for all 9 namespaces with coverage percentage per namespace  *(T3)*
/mock-ns      single-namespace mock artifact with category annotation and coverage gap summary  *(T3)*
/mock-review  namespace-by-namespace verdict: MOCK-ACCEPTED or REAL-REQUIRED with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

### Org -- 4 skills -- define roles and run decisions through a simulated organizational structure

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

---

## V-03 -- C-14 + C-15 Combination: Both New Criteria Together

**Axis**: C-14 + C-15 combined -- bi-directional descriptions AND mutually distinguishable taglines
**Hypothesis**: Both new rules can be applied simultaneously without interference. The BIDIR
RULE (mechanism + deliverable) applies at the description level; the SWAP TEST applies at the
tagline level. They operate at different levels of the output structure and should not conflict.
Combined, they should produce outputs that pass both C-14 and C-15 reliably.

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

TWO NEW RULES -- both must be satisfied in every output:

BIDIR RULE (C-14): Every sub-skill description must name BOTH the mechanism (what the skill
  does -- a verb phrase) AND the deliverable (what you receive -- a noun with count, format,
  or rating). Neither alone is sufficient. Both must be present in every description.

SWAP TEST (C-15): Every namespace tagline must be NAMESPACE-LOCKED. Before writing it, ask:
  "Could this tagline credibly appear under a different namespace header?" If yes, reject it.
  Each tagline must name what is uniquely true about that namespace's purpose.

FOUR FORMAT RULES (carried from R2):
RULE 1 (C-09): Every namespace header embeds the skill count.
  Format: ### <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11 + C-15): Every namespace header ends with a purpose tagline starting with a verb.
  The tagline must also pass the SWAP TEST above.
RULE 3 (C-12): Every section ends with a Markdown blockquote (> at line start).
RULE 4 (C-10): T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee.

---

### Scout -- 8 skills -- map the external landscape before writing a single requirement

/scout-competitors   scans competitive landscape with inertia-first framing -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat with inertia scored highest
/scout-feasibility   assesses technical and resource constraints -> traffic-light ratings (RED/YELLOW/GREEN) across team, timeline, and budget dimensions
/scout-naming        generates name candidates and validates them -> shortlist with trademark clearance status, domain availability, and per-persona score per name
/scout-compliance    surveys regulatory obligations -> applicable law list with enforcement risk rating and design-blocking constraint per regulation
/scout-market        sizes the addressable market -> TAM/SAM/SOM table with segment ranking by fit score
/scout-stakeholders  identifies decision-makers and maps their influence -> power/interest grid with veto risk rating and influence path per named stakeholder
/scout-positioning   frames per-audience product positions -> 3+ positioning statements with differentiation axis per target audience
/scout-requirements  extracts and classifies requirements -> MoSCoW-prioritized list with dependency graph and ambiguity flag per item

> Describe your discovery need and the most relevant scout skill will run.

---

### Draft -- 4 skills -- commit design thinking to a written artifact that others can review

/draft-spec        structures design intent into a specification -> document with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing design options -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       translates the product story into audience-tuned narratives -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates idea candidates and scores them -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

### Review -- 4 skills -- challenge an artifact through structured expert and user critique

/review-design     runs design through 6 expert disciplines -> named expert verdict with pass/fail rating per discipline
/review-code       annotates code at file level through 6 disciplines -> finding list with severity rating and pass/fail per discipline
/review-users      simulates 5 user personas walking through the design -> usability score per persona with cross-persona synthesis and top pain
/review-customers  simulates 12 customer personas evaluating the feature -> would-adopt rating, NPS prediction, and top concern per customer persona

> Describe your review artifact and the most relevant review skill will run.

---

### Flow -- 7 skills -- simulate how a domain process behaves before writing implementation code

/flow-lifecycle    traces a document lifecycle phase by phase -> entry/exit contracts and exception flows per phase with rollback conditions  *(T3)*
/flow-conversation simulates a multi-turn conversation through a topic graph -> dead-end count and loop detection per conversation path
/flow-trigger      fires a trigger set and models propagation -> fire-order list and side-effect table per field/event change  *(T3)*
/flow-dataflow     traces a pipeline stage by stage -> data loss event count and schema mismatch list per pipeline stage
/flow-integration  traces cross-system paths through connectors -> named connector gaps and failure mode per integration boundary
/flow-throttle     models burst and steady-state throughput -> table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   injects degraded conditions and observes recovery -> scenario table for offline, partial failure, and eventual consistency with recovery path  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

### Trace -- 7 skills -- step through platform mechanics one boundary at a time to find gaps

/trace-request     compiles request path hop by hop -> named service boundaries with hop count and latency estimate per hop
/trace-state       walks a state machine through every transition -> precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    compares expected vs actual outputs using three-directory pattern -> mismatch severity (CRITICAL/MAJOR/MINOR) per output delta  *(T3)*
/trace-component   follows a user action through the UI tree -> re-render count and state update path per component traversal
/trace-deployment  steps through a deployment sequence -> pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   applies a schema change to sample data -> before/after row counts, data loss detection, and rollback SQL
/trace-permissions walks RBAC rules for a principal -> who-can-do-what matrix with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

### Prove -- 9 skills -- state a hypothesis and build an evidence record to test it rigorously

/prove-hypothesis  frames a falsifiable claim -> hypothesis card with confidence (0-100%), falsification condition, and experiment list
/prove-websearch   queries the web for evidence -> evidence set with direct quotes, source URLs, and strength-of-evidence rating per source
/prove-intelligence searches internal codebase for evidence -> file-path citations with line references and relevance rating per source
/prove-prototype   builds the smallest testable artifact -> prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    examines a data set for patterns -> correlation-vs-causation analysis table with source attribution per finding
/prove-interview   runs stakeholder interviews through documented personas -> simulated transcript with quoted responses per persona  *(T3)*
/prove-synthesize  weighs gathered evidence for an answer -> answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     writes up an investigation -> paper with abstract, method, findings table, limitations, and implications
/prove-topic       orchestrates a full evidence campaign -> hypothesis card through synthesis in one automated multi-step command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

### Listen -- 3 skills -- simulate customer voice before real customers are exposed to the feature

/listen-feedback  simulates pre-ship reactions across customer personas -> per-persona NPS prediction across 12 personas with threshold gate verdict
/listen-support   predicts the first-wave support load -> ranked top-10 tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  models adoption progression by archetype -> Rogers adoption curve with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

### Program -- 2 skills -- structure multi-skill work into a coordinated plan with decision gates

/program-plan   builds a staged plan for a program of topics -> milestones with gate criteria and signal tracking per topic  *(T3)*
/prove-program  assigns and coordinates open-ended research -> multi-contributor assignment plan with synthesis strategy

> Describe your program scope and the most relevant skill will run.

---

### Topic -- 6 skills -- accumulate signals and synthesize coverage into a story that recommends action

/topic-new     opens a topic and plans its signals -> strategy document with planned signal list and coverage roadmap
/topic-status  computes live signal coverage -> terminal dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  generates a shareable progress snapshot -> document with coverage table, gap list, and readiness statement
/topic-plan    revises the signal strategy as new information arrives -> change table per signal with user confirmation before commit  *(T3)*
/topic-story   synthesizes all signals into a coherent narrative -> story with coherence score and design recommendation  *(T3)*
/topic-echo    surfaces unexpected findings across all signals -> list with source signal and implication per unexpected finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

### Quest -- 4 skills -- iterate skill prompts against scoring criteria until a golden version emerges

/quest-rubric  defines what good output looks like -> rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate generates prompt alternatives -> N complete prompt variations labeled with variation axis and hypothesis
/quest-score   scores prompt alternatives against rubric -> per-variation scorecard with composite score, leaderboard, and failure patterns  *(T3)*
/quest-golden  runs the full optimization loop -> converged golden prompt with convergence report and final rubric  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

### Mock -- 3 skills -- generate synthetic signal artifacts to fill coverage gaps during development

/mock-all     generates synthetic coverage across all 9 namespaces -> artifact set with coverage percentage per namespace  *(T3)*
/mock-ns      generates a mock artifact for one namespace -> document with category annotation and coverage gap summary  *(T3)*
/mock-review  audits existing mock coverage -> MOCK-ACCEPTED or REAL-REQUIRED verdict with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

### Org -- 4 skills -- define an organization's roles and run decisions through its simulated structure

/org-roles      defines the organizational role landscape -> typed registry with orientation statement, decision lens, and expertise profile per role
/org-chart      builds a full org structure -> named areas with committee charters and operating rhythm cadences  *(T3)*
/org-review     routes an artifact through the org's relevant roles -> verdict per role from .craft/roles/ registry  *(T3)*
/org-committee  runs a committee meeting simulation -> agenda with named participants and decision per agenda item  *(T3)*

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```

---

## V-04 -- Full Integration: R2 V-05 Base + C-14 + C-15

**Axis**: Full integration -- all 7 aspirational criteria (C-09 through C-15) + R2 V-05 patterns
**Hypothesis**: Adding RULE 6 (C-14 BIDIR) and RULE 7 (C-15 SWAP TEST) to the R2 V-05 skeleton
produces a prompt that achieves 100% on the v3 rubric. The routing guide, bare-mode contract,
and T3 list from R2 V-05 remain unchanged. The two new rules extend the five-rule set to seven.
The interaction effect: RULE 6 (description level) and RULE 7 (header level) operate at different
output positions and should not interfere with each other or with RULES 1-5.

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

SEVEN FORMAT RULES -- every rule must be satisfied in every output:

RULE 1 (C-09 COUNT): Every namespace header must embed the skill count.
  Format: ### <Namespace> -- <N> skills -- <tagline>

RULE 2 (C-11 TAGLINE): Every namespace header must end with a purpose tagline starting with a verb.
  The tagline must answer "what is this namespace for?" and be distinct across all 12 namespaces.
  PASS: ### Scout -- 8 skills -- map the competitive landscape before you commit to a direction
  FAIL: ### Scout -- 8 skills (no tagline)

RULE 3 (C-12 BLOCKQUOTE): Every namespace section must end with a Markdown blockquote routing hint.
  The > must be at line start. Inline prose routing hints are not acceptable.
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Run any scout skill directly, or describe your need.

RULE 4 (C-13 QUANTIFIED): Every sub-skill description must name a specific output --
  a count, named format, or rated deliverable. Vague single-word nouns alone are not sufficient.
  PASS: "5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"

RULE 5 (C-10 T3): Skills whose full runbook loads on demand carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden

RULE 6 (C-14 BIDIR): Every description must be BI-DIRECTIONAL -- naming BOTH the mechanism
  (what the skill does -- a verb phrase) AND the deliverable (what you receive -- a noun with
  count, format, or rating). Neither alone is sufficient.
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no deliverable)
  FAIL: "5-8 rivals with ratings" (no mechanism verb)

RULE 7 (C-15 SWAP TEST): Every namespace tagline must be NAMESPACE-LOCKED.
  Test: could this tagline appear under any other namespace header and still make sense?
  If yes, reject it and write a more specific tagline.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (could be scout, prove, or listen)

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.

---

### Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

/scout-competitors   scans competitive landscape with inertia-first framing -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat
/scout-feasibility   assesses technical, team, and timeline constraints -> traffic-light ratings (RED/YELLOW/GREEN) per dimension
/scout-naming        generates name candidates and validates each one -> shortlist with trademark clearance, domain availability, and per-persona score per name
/scout-compliance    maps regulatory obligations for a domain -> applicable law list with enforcement risk rating and design-blocking constraints
/scout-market        sizes the addressable market -> TAM/SAM/SOM table with segment ranking by fit score
/scout-stakeholders  identifies decision-makers and their influence patterns -> power/interest grid with veto risk rating and influence path per stakeholder
/scout-positioning   frames the product for each target audience -> 3+ positioning statements with differentiation axis per audience
/scout-requirements  extracts and classifies feature requirements -> MoSCoW-prioritized list with dependency graph and ambiguity flags

> Describe your discovery need and the most relevant scout skill will run.

---

### Draft -- 4 skills -- commit design intent to a written artifact that others can review and challenge

/draft-spec        structures design intent into sections -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options against criteria -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story for each audience -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates idea candidates and scores them comparatively -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

### Review -- 4 skills -- challenge design and code through structured expert and user critique

/review-design     runs design through 6 expert disciplines -> named expert verdict with pass/fail rating per discipline
/review-code       annotates code at file level across disciplines -> finding list with severity rating and pass/fail per discipline
/review-users      simulates 5 persona advocates walking the design -> usability score per persona with cross-persona synthesis
/review-customers  simulates 12 customer personas evaluating the feature -> would-adopt rating, NPS prediction, and top concern per persona

> Describe your review artifact and the most relevant review skill will run.

---

### Flow -- 7 skills -- simulate how a domain process plays out before building the implementation

/flow-lifecycle    traces a document lifecycle phase by phase -> entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation simulates a multi-turn conversation -> topic graph traversal with dead-end count and loop detection
/flow-trigger      fires a trigger set and traces propagation -> fire-order list and side-effect table per field/event change  *(T3)*
/flow-dataflow     traces a pipeline stage by stage -> data loss event count and schema mismatch list per stage
/flow-integration  traces cross-system integration paths -> named connector gaps and failure mode per integration boundary
/flow-throttle     models throughput under load -> table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   injects degraded conditions into the process model -> scenario table with recovery path for offline, partial failure, and eventual consistency  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

### Trace -- 7 skills -- step through implementation mechanics one boundary at a time

/trace-request     compiles request path hop by hop -> named service boundaries with hop count and latency estimate per hop
/trace-state       walks a state machine through its transitions -> precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    compares expected vs actual outputs using three-directory pattern -> mismatch severity (CRITICAL/MAJOR/MINOR) per delta  *(T3)*
/trace-component   follows a user action through the UI component tree -> re-render count and state update path per component
/trace-deployment  steps through a deployment sequence -> pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   applies a schema change to sample data -> before/after row counts, data loss detection, and rollback SQL
/trace-permissions walks RBAC rules for a principal -> who-can-do-what matrix with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

### Prove -- 9 skills -- state a hypothesis then build a rigorous evidence case to test it

/prove-hypothesis  frames a falsifiable claim -> hypothesis card with confidence (0-100%), falsification condition, and experiment list
/prove-websearch   queries the web for evidence -> direct quotes with source URLs and strength-of-evidence rating per source
/prove-intelligence searches internal sources for evidence -> file-path citations with line references and relevance rating per source
/prove-prototype   builds the smallest testable artifact -> prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    examines a data set for patterns -> correlation-vs-causation analysis table with source attribution per finding
/prove-interview   runs persona-driven stakeholder interviews -> simulated transcript with quoted responses grounded in documented roles  *(T3)*
/prove-synthesize  weighs all evidence for an answer -> answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     writes up an investigation -> paper with abstract, method, findings table, limitations, and implications
/prove-topic       orchestrates a full evidence campaign -> hypothesis card through synthesis in one automated command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

### Listen -- 3 skills -- predict what customers will say before they have the chance to say it

/listen-feedback  simulates pre-ship reactions across customer personas -> per-persona NPS prediction across 12 personas with threshold gate verdict
/listen-support   predicts post-ship support load -> ranked top-10 tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  models adoption progression by archetype -> Rogers curve with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

### Program -- 2 skills -- structure multi-skill investigations into a coordinated plan with gates

/program-plan   builds a staged plan for a program of topics -> milestones with gate criteria and signal tracking per topic  *(T3)*
/prove-program  assigns and orchestrates open-ended research -> multi-contributor assignment plan with synthesis strategy

> Describe your program scope and the most relevant skill will run.

---

### Topic -- 6 skills -- track signal accumulation and synthesize it into a decision-ready story

/topic-new     opens a topic and plans its signals -> strategy document with planned signal list and coverage roadmap
/topic-status  computes live signal coverage -> terminal dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  generates a shareable progress snapshot -> document with coverage table, gap list, and readiness statement
/topic-plan    revises the signal strategy as evidence arrives -> change table per signal with user confirmation before commit  *(T3)*
/topic-story   synthesizes all signals into a coherent narrative -> story with coherence score and design recommendation  *(T3)*
/topic-echo    surfaces unexpected findings across signals -> list with source signal and implication per unexpected finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

### Quest -- 4 skills -- iterate skill prompts against criteria until the best version converges

/quest-rubric  defines what good output looks like -> rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate generates prompt alternatives -> N complete prompt variations labeled with axis and hypothesis
/quest-score   scores alternatives against rubric -> per-variation scorecard with composite score, leaderboard, and failure patterns  *(T3)*
/quest-golden  runs the full optimization loop -> converged golden prompt with convergence report and final rubric  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

### Mock -- 3 skills -- generate synthetic signals to fill coverage gaps when real evidence is blocked

/mock-all     generates synthetic coverage for all 9 namespaces -> artifact set with coverage percentage per namespace  *(T3)*
/mock-ns      generates a mock artifact for one namespace -> document with category annotation and coverage gap summary  *(T3)*
/mock-review  audits existing mock coverage quality -> MOCK-ACCEPTED or REAL-REQUIRED verdict with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

### Org -- 4 skills -- define roles and run decisions through a simulated organizational structure

/org-roles      defines the organizational role landscape -> typed registry with orientation statement, decision lens, and expertise profile per role
/org-chart      builds a full org structure -> named areas with committee charters and operating rhythm cadences  *(T3)*
/org-review     routes an artifact through relevant roles -> verdict per role from .craft/roles/ registry  *(T3)*
/org-committee  runs a committee meeting simulation -> agenda with named participants and decision per agenda item  *(T3)*

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```

---

## V-05 -- Structural Pre-Print: Mechanically Enforced C-14 and C-15

**Axis**: Structural enforcement -- pre-printed two-part description format and uniqueness-anchored
taglines that make C-14 and C-15 structurally impossible to violate
**Hypothesis**: Rule-based enforcement (V-01 through V-04) requires the model to apply rules to
free-form output. Structural enforcement replaces rules with format constraints: descriptions
are pre-printed with a `[verb phrase] -> [deliverable]` template structure where both slots
are pre-filled and the model transcribes rather than generates. Taglines are pre-printed with
a uniqueness anchor (a noun the model cannot swap across namespaces). This eliminates the
rule-compliance gap -- the model cannot accidentally fail C-14 or C-15 if the data is already there.

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

FORMAT RULES (5, carried from R2 V-05):
RULE 1 (C-09): Header format: ### <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11 + C-15): Tagline must start with a verb and be namespace-locked (pre-printed below).
RULE 3 (C-12): Section ends with Markdown blockquote (> at line start).
RULE 4 (C-13 + C-14): Description format: [mechanism verb phrase] -> [quantified deliverable].
  The -> separator is REQUIRED. Left side: what the skill does. Right side: what you receive.
  Do not omit either side. Do not merge them without the separator.
RULE 5 (C-10): T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden

BARE MODE: Output exactly 61 command names. Begin /scout-competitors. End /org-committee.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design begins

/scout-competitors   scans competitive landscape with inertia-first framing    -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat with inertia always scored first
/scout-feasibility   assesses technical, team, timeline, and budget constraints -> traffic-light ratings (RED/YELLOW/GREEN) per dimension with blocking items highlighted
/scout-naming        generates name candidates and validates each one           -> shortlist with trademark clearance, domain availability, and per-persona score
/scout-compliance    surveys regulatory obligations for a domain                -> applicable law list with enforcement risk rating and design-blocking constraint per regulation
/scout-market        sizes the addressable market by segment                    -> TAM/SAM/SOM table with segments ranked by fit score
/scout-stakeholders  identifies decision-makers and maps their influence        -> power/interest grid with veto risk rating and influence path per named stakeholder
/scout-positioning   frames the product for each target audience                -> 3+ positioning statements with competitive differentiation axis per audience
/scout-requirements  extracts and classifies feature requirements               -> MoSCoW-prioritized list with dependency graph and ambiguity flag per item

> Describe your discovery need and the most relevant scout skill will run.

---

## Draft -- 4 skills -- commit design thinking to a written artifact ready for review

/draft-spec        structures design intent into a specification    -> document with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates design options against criteria        -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       translates the product story for each audience   -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates and scores idea candidates             -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> Describe your artifact need and the most relevant draft skill will run.

---

## Review -- 4 skills -- challenge an artifact through expert discipline and user perspective critique

/review-design     runs design through 6 expert lenses        -> named expert verdict with pass/fail rating per discipline
/review-code       annotates code at file level                -> finding list with severity rating and pass/fail per discipline
/review-users      simulates 5 user persona advocates          -> usability score per persona with cross-persona synthesis and top pain
/review-customers  simulates 12 customer personas              -> would-adopt rating, NPS prediction, and top concern per customer persona

> Describe your review artifact and the most relevant review skill will run.

---

## Flow -- 7 skills -- simulate domain process behavior before writing the implementation

/flow-lifecycle    traces document lifecycle phase by phase                          -> entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation simulates multi-turn agent conversation through a topic graph     -> dead-end count and loop-detection result per conversation path
/flow-trigger      fires trigger set and traces propagation through the domain model -> fire-order list and side-effect table per field/event change  *(T3)*
/flow-dataflow     traces ETL or sync pipeline stage by stage                        -> data loss event count and schema mismatch list per stage
/flow-integration  traces cross-system paths through connectors and APIs             -> named connector gaps and failure mode per integration boundary
/flow-throttle     models burst and steady-state throughput                          -> throughput table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   injects degraded conditions into the process model                -> scenario table with recovery path for offline, partial failure, and eventual consistency  *(T3)*

> Describe your domain process and the most relevant flow skill will run.

---

## Trace -- 7 skills -- step through platform mechanics one boundary at a time before assumptions harden

/trace-request     compiles request path hop by hop                                    -> named service boundaries with hop count and latency estimate per hop
/trace-state       walks a state machine through every transition                      -> precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    compares expected vs actual output using three-directory pattern     -> mismatch severity (CRITICAL/MAJOR/MINOR) per output delta  *(T3)*
/trace-component   follows user action through the UI component tree                   -> re-render count and state update path per component traversal
/trace-deployment  steps through deployment sequence                                   -> pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   applies schema change to sample data                                -> before/after row counts, data loss detection, and rollback SQL
/trace-permissions walks RBAC rules for a principal and action set                     -> who-can-do-what matrix with privilege escalation path and gap count  *(T3)*

> Describe your platform behavior and the most relevant trace skill will run.

---

## Prove -- 9 skills -- state a hypothesis then build a rigorous evidence case before claiming certainty

/prove-hypothesis  frames a falsifiable claim                                     -> hypothesis card with confidence (0-100%), falsification condition, and experiment list
/prove-websearch   queries the web for supporting and opposing evidence           -> direct quotes with source URLs and strength-of-evidence rating per source
/prove-intelligence searches internal codebase and docs for evidence              -> file-path citations with line references and relevance rating per source
/prove-prototype   builds the smallest testable implementation                    -> prototype spec with defined measure, predicted result, and actual-vs-predicted comparison
/prove-analysis    examines a data set for causal patterns                        -> correlation-vs-causation analysis table with source attribution per finding
/prove-interview   runs persona-driven stakeholder interviews                     -> simulated transcript with quoted responses grounded in documented roles  *(T3)*
/prove-synthesize  weighs all gathered evidence against the hypothesis            -> answer-first synthesis with overall confidence rating and named counter-evidence list
/prove-publish     writes up an investigation as a research paper                 -> paper with abstract, method, findings table, limitations, and implications
/prove-topic       orchestrates a full evidence campaign                          -> hypothesis card through synthesis in one automated multi-step command  *(T3)*

> Describe your hypothesis and the most relevant prove skill will run.

---

## Listen -- 3 skills -- predict what customers will say before they have the chance to say it

/listen-feedback  simulates pre-ship reactions across 12 customer personas -> per-persona NPS prediction with threshold gate verdict
/listen-support   predicts first-wave support load before shipping          -> ranked top-10 tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  models adoption progression by Rogers archetype           -> adoption curve with chasm gap analysis and crossing strategy

> Describe your feature and the most relevant listen skill will run.

---

## Program -- 2 skills -- structure multi-skill investigations into a coordinated plan with decision gates

/program-plan   builds a staged program plan with gates     -> milestones with gate criteria and signal tracking per topic  *(T3)*
/prove-program  orchestrates open-ended research            -> multi-contributor assignment plan with synthesis strategy

> Describe your program scope and the most relevant skill will run.

---

## Topic -- 6 skills -- accumulate signal coverage and synthesize it into a decision-ready story

/topic-new     registers a topic and plans its signals         -> strategy document with planned signal list and coverage roadmap
/topic-status  computes live signal coverage                   -> terminal dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  generates a shareable progress snapshot         -> document with coverage table, gap list, and readiness statement
/topic-plan    revises signal strategy as evidence arrives     -> change table per signal with user confirmation before commit  *(T3)*
/topic-story   synthesizes all signals into a coherent story   -> narrative with coherence score and design recommendation  *(T3)*
/topic-echo    surfaces unexpected findings across signals     -> list with source signal and implication per unexpected finding  *(T3)*

> Describe your topic management need and the most relevant skill will run.

---

## Quest -- 4 skills -- iterate skill prompts against scoring criteria until the best version converges

/quest-rubric  defines the scoring criteria for a skill           -> rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate generates prompt alternatives for comparison       -> N complete prompt variations labeled with variation axis and hypothesis
/quest-score   scores prompt alternatives against a rubric        -> per-variation scorecard with composite score, ranked leaderboard, and failure patterns  *(T3)*
/quest-golden  runs the full golden-prompt optimization loop      -> converged golden prompt with convergence report and final rubric  *(T3)*

> Describe your optimization goal and the most relevant quest skill will run.

---

## Mock -- 3 skills -- generate synthetic signal artifacts to fill coverage gaps during development

/mock-all     generates synthetic coverage for all 9 namespaces -> artifact set with coverage percentage per namespace  *(T3)*
/mock-ns      generates a mock artifact for a single namespace   -> document with category annotation and coverage gap summary  *(T3)*
/mock-review  audits mock coverage quality per namespace         -> MOCK-ACCEPTED or REAL-REQUIRED verdict with rationale per namespace  *(T3)*

> Describe your coverage need and the most relevant mock skill will run.

---

## Org -- 4 skills -- define organizational roles and run decisions through a simulated structure

/org-roles      defines the organizational role landscape     -> typed registry with orientation statement, decision lens, and expertise profile per role
/org-chart      builds a full organizational structure        -> named areas with committee charters and operating rhythm cadences  *(T3)*
/org-review     routes an artifact through relevant roles     -> verdict per role from .craft/roles/ registry  *(T3)*
/org-committee  runs a committee meeting simulation           -> agenda with named participants and decision per agenda item  *(T3)*

> Describe your organizational need and the most relevant org skill will run.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```
