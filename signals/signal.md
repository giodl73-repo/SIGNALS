You are running /signal for the current workspace.

If called with a description or intent, route to the best skill (see ROUTING below).
If called bare, show the NAMESPACE OVERVIEW below.

---

## ROUTING

Read the user's words. Match to the closest intent. Suggest the specific skill.

Examples:

"I need to decide whether to build X"
  -> /decide (full campaign) or /competitors (start with inertia)

"I need to understand the competition"
  -> /competitors <topic>

"Is this technically feasible?"
  -> /feasibility <topic>

"I need to size the market"
  -> /market <topic>

"I need to write a spec"
  -> /spec <topic>

"I need a proposal or ADR"
  -> /proposal <topic>

"I need a pitch deck"
  -> /pitch <topic>

"I need to brainstorm ideas"
  -> /brainstorm <topic>

"I need to review my design" or "review this spec"
  -> /design <topic> or /validate <topic>

"I need to test with users" or "user walkthrough"
  -> /users <topic>

"What will customers think?"
  -> /customers <topic>

"Will this get adopted?"
  -> /adoption <topic>

"What support tickets will this generate?"
  -> /support <topic>

"I need to simulate system behavior" or "simulate the flow"
  -> /behavior <topic> or /lifecycle <topic>

"I need to test edge cases" or "stress test"
  -> /stress <topic> or /resilience <topic>

"I need to trace a request"
  -> /request <topic>

"I need to check permissions"
  -> /permissions <topic>

"I need to check state transitions"
  -> /state <topic>

"I need to prove a hypothesis" or "research question"
  -> /hypothesis <topic> or /prove <topic>

"I need to do market research"
  -> /websearch <topic>

"I need to register a topic" or "start tracking"
  -> /new <topic>

"What signals do I have?" or "coverage check"
  -> /status <topic>

"Write the story of this feature"
  -> /story <topic>

"Run a governance review" or "ROB review"
  -> /product-review <topic> or /pull-request <topic>

If the intent is ambiguous, show 2-3 options with one-line descriptions and let the user pick.

---

## CONVERSATIONAL ENTRY

Describe what you need, or pick a namespace:

  -> To decide whether to build something:      /decide or /competitors
  -> To write a spec or proposal:                /spec or /blueprint
  -> To validate with users or customers:        /validate or /design
  -> To simulate system behavior:                /behavior or /stress
  -> To gather evidence or research:             /prove or /websearch
  -> To manage your topic narrative:             /status or /story
  -> To run a governance review:                 /product-review or /pull-request

---

## NAMESPACE OVERVIEW

Signal has 77 skills across 14 namespaces. The one rule: the primary competitor
is always inertia. Before any feature, ask "why would teams do nothing instead?"

### scout -- PM proves the idea
  /competitors    inertia-first competitive analysis
  /feasibility    traffic-light technical assessment
  /market         segment sizing and fit scoring
  /naming         name candidates with persona scores
  /compliance     regulatory constraint scan
  /stakeholders   power/interest grid with veto risk
  /positioning    per-audience positioning statements
  /requirements   MoSCoW requirements extraction

### draft -- Author writes the design
  /spec           guided specification with self-review
  /proposal       ADR with three-option minimum
  /pitch          exec, developer, and maker versions
  /brainstorm     idea pool with inertia baseline

### review -- Team validates the design
  /design         6-discipline expert review
  /code           multi-discipline code review
  /users          5-persona usability walkthrough
  /customers      12-persona NPS evaluation

### flow -- Domain developer simulates the process
  /lifecycle      business document lifecycle
  /conversation   multi-turn agent conversation
  /trigger        automation fire order and side effects
  /dataflow       ETL pipeline with data loss detection
  /integration    cross-system connector gap analysis
  /throttle       rate-limit backpressure propagation
  /resilience     degraded-condition failure modes

### trace -- System developer simulates the platform
  /request        request hand-compilation
  /state          state transition validation
  /contract       expected vs actual comparison
  /component      user action through UI tree
  /deployment     deployment sequence with rollback
  /migration      schema change with data loss detection
  /permissions    RBAC walk-through

### prove -- Prove what you believe
  /hypothesis     claim + falsification condition
  /websearch      web evidence with cited sources
  /intelligence   internal source search
  /prototype      smallest-possible prototype
  /analysis       correlation vs causation
  /interview      persona stakeholder simulation
  /synthesize     answer-first evidence synthesis
  /publish        investigation as paper

### listen -- Team simulates post-ship feedback
  /feedback       pre-ship NPS prediction
  /support        top support ticket forecast
  /adoption       Rogers archetype adoption curve

### program -- Lead orchestrates all
  /program        staged program plan with gates

### topic -- Anyone manages the narrative
  /new            register topic and plan signals
  /status         terminal coverage display
  /plan           revise signal strategy
  /report         shareable status document
  /story          editorial narrative synthesis
  /echo           unexpected findings synthesis

### org -- Governance infrastructure
  /roles          typed role registry generation
  /chart          org structure with committees
  /product-review full org review through roles
  /committee      ROB, shiproom, or arch board sim
  /pull-request   code review via org roles

### mock -- Synthetic preview artifacts
  /mock           generate mocks for all namespaces
  /mock-ns        mock for a single namespace
  /mock-review    MOCK-ACCEPTED or REAL-REQUIRED

### quest -- Prompt quality tooling
  /quest-rubric   define what good output looks like
  /quest-variate  generate N prompt variations
  /quest-score    score outputs against rubric
  /quest-golden   find the golden prompt (full loop)

### Campaigns -- Full-stack orchestrators
  /decide         full pre-commitment decision campaign
  /validate       full design validation campaign
  /behavior       full technical simulation campaign
  /blueprint      full specification campaign
  /evidence       full evidence campaign
  /track          full topic narrative campaign

---

Quick start:
  /decide <topic>         run the full pre-commitment campaign
  /competitors <topic>    start with competitive context
  /new <topic>            register a topic and plan your signals
  /signal <description>   describe what you need and get routed
