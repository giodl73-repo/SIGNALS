---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-17
round: 1
rubric: simulations/quest/rubrics/signal-rubric-v1-2026-03-17.md
---

# Quest Variate -- /signal (Round 1)

**Skill**: `signal` -- command index showing all 12 namespaces with sub-skills and one-line descriptions.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v1-2026-03-17.md`

**Variation axes selected**:
1. Single-axis A -- Output format (list vs table vs structured prose)
2. Single-axis B -- Phrasing register (declarative/reference vs imperative/conversational)
3. Single-axis C -- Lifecycle emphasis (implicit dispatch vs explicit branching logic)
4. Combination AB -- format + phrasing register
5. Full integration ABC -- format + phrasing + explicit lifecycle

---

## V-01 -- Output Format: Table Layout

**Axis**: Output format (table instead of `->` list)
**Hypothesis**: A Markdown table per namespace scores higher on C-10 scannability and C-06 count
accuracy because the table header enforces column discipline. May score lower on C-07 dispatch
footer if the table leaves no natural place for a routing hint.

```
You are the Signal command index. Respond with the full skill catalog when invoked as `/signal`,
a single-namespace table when invoked as `/signal <namespace>`, or bare command names when
invoked as `/signal --bare`.

INVOCATION MODES
----------------
/signal             -- emit full index (all 12 namespaces)
/signal <namespace> -- emit one namespace table only
/signal --bare      -- emit command names with no prose, one per line

FULL INDEX FORMAT (one table per namespace):

For each namespace, output:
  ## /<namespace> -- <purpose phrase> -- <N> skills

  | Command | Description |
  |---------|-------------|
  | /<namespace>-<skill> | <one-line canonical description> |
  ...

  > Run any sub-skill directly, or describe your <domain> and the most relevant skill will run.

NAMESPACE CATALOG (emit in this order):

scout    -- 8 skills -- discovery and research
draft    -- 4 skills -- authoring design artifacts
review   -- 4 skills -- design and code validation
flow     -- 7 skills -- domain process simulation
trace    -- 7 skills -- platform-level simulation
prove    -- 9 skills -- hypothesis-driven investigation
listen   -- 3 skills -- post-ship signal simulation
program  -- 2 skills -- orchestration and planning
topic    -- 6 skills -- narrative management
quest    -- 4 skills -- prompt engineering and golden prompt discovery
mock     -- 3 skills -- synthetic signal generation
org      -- 4 skills -- organizational simulation

SUB-SKILL DESCRIPTIONS (authoritative; use verbatim in table):

/scout-competitors  -> competitive landscape + inertia analysis
/scout-feasibility  -> technical feasibility + team/timeline assessment
/scout-naming       -> name validation + trademark + domain search
/scout-compliance   -> regulatory framework scan
/scout-market       -> market sizing + segment analysis
/scout-stakeholders -> stakeholder map + power/interest grid
/scout-positioning  -> positioning framework + category definition
/scout-requirements -> requirements extraction + ambiguity flags

/draft-spec        -> technical specification with guided section structure
/draft-proposal    -> proposal or ADR with three-option minimum
/draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
/draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring

/review-design     -> multi-expert design review through 6 disciplines
/review-code       -> multi-discipline code review with file-level annotations
/review-users      -> 5 persona advocates walk through design with usability scores
/review-customers  -> 12 customer personas evaluate for usefulness and would-adopt

/flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
/flow-conversation -> multi-turn agent conversation with dead-end and loop detection
/flow-trigger      -> automation trigger fire order and side effects per event
/flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
/flow-integration  -> cross-system integration tracing with gap analysis
/flow-throttle     -> rate-limit throughput and backpressure propagation
/flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

/trace-request     -> request hand-compilation through service boundaries
/trace-state       -> state transition with preconditions, postconditions, invariants
/trace-contract    -> expected vs actual output comparison with mismatch severity
/trace-component   -> user action through UI component tree and re-render chain
/trace-deployment  -> deployment sequence with pre-checks and rollback path
/trace-migration   -> schema change with before/after data state and loss detection
/trace-permissions -> RBAC walk-through with privilege escalation detection

/prove-hypothesis  -> hypothesis framing with claim, falsification, confidence, experiments
/prove-websearch   -> web evidence with direct quotes, URLs, strength-of-evidence rating
/prove-intelligence -> internal source search with file-path citations
/prove-prototype   -> smallest-possible prototype with predicted vs actual results
/prove-analysis    -> data pattern analysis distinguishing correlation from causation
/prove-interview   -> persona-driven stakeholder interview simulation
/prove-synthesize  -> answer-first evidence synthesis with confidence and counter-evidence
/prove-publish     -> investigation write-up as paper with abstract and limitations
/prove-topic       -> full prove campaign orchestrating hypothesis through synthesis

/listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
/listen-support   -> top support ticket prediction for first 90 days
/listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

/program-plan  -> staged program plan with gates and topic tracking
/prove-program -> general-purpose research orchestrator for open-ended questions

/topic-new     -> topic registration with strategy planning and signal coverage plan
/topic-status  -> terminal coverage display computed from signal glob
/topic-report  -> shareable status document with progress table and readiness statement
/topic-plan    -> signal strategy revision as new information arrives
/topic-story   -> editorial synthesis of all signals into a coherent narrative
/topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

/quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
/quest-variate -> generate N prompt variations of a skill body for comparison
/quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
/quest-golden  -> find the golden prompt through systematic variation and scoring

/mock-all     -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns      -> mock artifact for a single namespace with category annotation
/mock-review  -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

BARE MODE:
When invoked as `/signal --bare`, emit only the command names (without leading `/`),
one per line, in namespace order, with no headers, no descriptions, no blank lines
between namespaces. Example first three lines:
  scout-competitors
  scout-feasibility
  scout-naming
  ...
```

---

## V-02 -- Phrasing Register: Imperative/Conversational

**Axis**: Phrasing register (conversational imperative -- tell Claude what the user wants to
accomplish, not what to print)
**Hypothesis**: Imperative framing ("the user wants to browse commands") elicits more natural
dispatch-footer phrasing (C-07) and better routing behavior (C-05), at the cost of format
precision (C-10) because it delegates layout decisions to the model.

```
The user has typed `/signal` (or `/signal <namespace>` or `/signal --bare`).
They want to browse what Signal can do and pick a skill to run.

Your job: show them the command index so they can find the right skill fast.

HOW TO RESPOND

If the user typed `/signal` with nothing else:
  Show every namespace. For each one, give a short header naming the namespace and its purpose,
  list every skill in that namespace with a one-line description, and end with a routing hint
  so the user knows they can just describe their situation instead of picking a command manually.

If the user typed `/signal <namespace>` (e.g. `/signal flow`):
  Show only that namespace. Same format: header, skill list with descriptions, routing hint.
  Do not mention other namespaces.

If the user typed `/signal --bare`:
  Emit just the command names. No descriptions. No headers. No blank lines between namespaces.
  One command per line in namespace order. Nothing else.

THE 12 NAMESPACES (show in this order):

1. scout (8 skills) -- discovery and research before committing to a design
2. draft (4 skills) -- authoring specifications, proposals, pitches, and ideas
3. review (4 skills) -- validating designs and code through expert and persona review
4. flow (7 skills) -- simulating business processes and integration paths
5. trace (7 skills) -- hand-compiling platform behavior at the service and component level
6. prove (9 skills) -- gathering and synthesizing evidence for or against a hypothesis
7. listen (3 skills) -- simulating customer reaction after a feature ships
8. program (2 skills) -- orchestrating multi-signal programs and research tracks
9. topic (6 skills) -- managing the narrative: coverage, status, story, and surprises
10. quest (4 skills) -- engineering prompts: rubric, variation, scoring, golden prompt
11. mock (3 skills) -- generating synthetic signal artifacts for coverage gaps
12. org (4 skills) -- simulating organizational structures and review committees

THE SKILLS PER NAMESPACE (use these descriptions verbatim):

scout: competitors (competitive landscape + inertia analysis), feasibility (technical
feasibility + team/timeline assessment), naming (name validation + trademark + domain search),
compliance (regulatory framework scan), market (market sizing + segment analysis),
stakeholders (stakeholder map + power/interest grid), positioning (positioning framework +
category definition), requirements (requirements extraction + ambiguity flags)

draft: spec (technical specification with guided section structure), proposal (proposal or ADR
with three-option minimum), pitch (pitch deck narrative in exec, developer, and maker versions),
brainstorm (idea pool with inertia baseline and peer-comparison scoring)

review: design (multi-expert design review through 6 disciplines), code (multi-discipline code
review with file-level annotations), users (5 persona advocates walk through design with
usability scores), customers (12 customer personas evaluate for usefulness and would-adopt)

flow: lifecycle (business document lifecycle with phase contracts and exception flows),
conversation (multi-turn agent conversation with dead-end and loop detection), trigger
(automation trigger fire order and side effects per event), dataflow (ETL pipeline tracing with
data loss and schema mismatch detection), integration (cross-system integration tracing with gap
analysis), throttle (rate-limit throughput and backpressure propagation), resilience
(degraded-condition simulation: offline, partial failure, eventual consistency)

trace: request (request hand-compilation through service boundaries), state (state transition
with preconditions, postconditions, invariants), contract (expected vs actual output comparison
with mismatch severity), component (user action through UI component tree and re-render chain),
deployment (deployment sequence with pre-checks and rollback path), migration (schema change
with before/after data state and loss detection), permissions (RBAC walk-through with privilege
escalation detection)

prove: hypothesis (hypothesis framing with claim, falsification, confidence, experiments),
websearch (web evidence with direct quotes, URLs, strength-of-evidence rating), intelligence
(internal source search with file-path citations), prototype (smallest-possible prototype with
predicted vs actual results), analysis (data pattern analysis distinguishing correlation from
causation), interview (persona-driven stakeholder interview simulation), synthesize (answer-first
evidence synthesis with confidence and counter-evidence), publish (investigation write-up as
paper with abstract and limitations), topic (full prove campaign orchestrating hypothesis
through synthesis)

listen: feedback (pre-ship customer reaction with per-persona NPS prediction), support (top
support ticket prediction for first 90 days), adoption (adoption curve simulation across Rogers
archetypes with chasm analysis)

program: plan (staged program plan with gates and topic tracking), prove-program
(general-purpose research orchestrator for open-ended questions)

topic: new (topic registration with strategy planning and signal coverage plan), status
(terminal coverage display computed from signal glob), report (shareable status document with
progress table and readiness statement), plan (signal strategy revision as new information
arrives), story (editorial synthesis of all signals into a coherent narrative), echo (unexpected
findings synthesis: what did we learn that we did not expect?)

quest: rubric (define what good output looks like: ranked criteria with pass conditions),
variate (generate N prompt variations of a skill body for comparison), score (score skill
outputs against a rubric with leaderboard and failure patterns), golden (find the golden prompt
through systematic variation and scoring)

mock: all (synthetic signal artifacts for all 9 namespaces with coverage picture), ns (mock
artifact for a single namespace with category annotation), review (coverage review writing
MOCK-ACCEPTED or REAL-REQUIRED per namespace)

org: roles (typed role registry with orientation, lens, and expertise), chart (org structure
with areas, committees, and operating rhythms), review (full org review running artifact through
all relevant roles), committee (committee meeting simulation for ROB, shiproom, or architecture
board)

FORMAT GUIDANCE
Use a consistent visual style. For the list format, the `->` separator works well:
  /scout-competitors -> competitive landscape + inertia analysis
Each namespace should feel like a self-contained section a user can scan in 5 seconds.
End each section with: "Run any sub-skill directly, or describe your <domain> and the most
relevant <namespace> skill will run."
```

---

## V-03 -- Lifecycle Emphasis: Explicit Branching Logic

**Axis**: Lifecycle emphasis (all three invocation modes declared as explicit branches with
preconditions and output contracts)
**Hypothesis**: Explicit precondition/output-contract framing makes `--bare` and `<namespace>`
modes reliable (C-04, C-05) because each branch has a named output contract the model must
honor. The cost is verbosity -- the prompt is longer and may feel mechanical.

```
You are executing `/signal`. Parse the invocation to determine mode, then emit the correct
output per the output contract for that mode. Do not mix modes.

PHASE 1 -- PARSE INVOCATION

Read the full invocation string:
  - If it is exactly `/signal` with no arguments: MODE = FULL
  - If it is `/signal --bare`: MODE = BARE
  - If it is `/signal <word>` where <word> is a known namespace name: MODE = NAMESPACE
  - Otherwise: MODE = FULL (default)

PHASE 2 -- EXECUTE OUTPUT CONTRACT

CONTRACT: MODE = FULL
  Emit all 12 namespaces in order. For each namespace:
    HEADER: `- /<namespace> -- <purpose phrase> -- <N> skills`
    BODY:   one entry per sub-skill in the form `/<namespace>-<skill>  -> <description>`
    FOOTER: `Run any sub-skill directly, or describe your <domain> and the most relevant
             <namespace> skill will run.`
  Separate namespaces with a blank line.
  Total output: 12 namespace sections.

CONTRACT: MODE = NAMESPACE
  Identify the requested namespace. Emit that namespace section only, using the same
  HEADER / BODY / FOOTER structure as FULL mode.
  Do not emit any other namespace sections.
  If the requested namespace is not in the catalog, emit:
    `Unknown namespace: <word>. Known namespaces: scout draft review flow trace prove listen
     program topic quest mock org`

CONTRACT: MODE = BARE
  Emit all sub-skill command names in namespace order. One name per line.
  No leading `/`. No descriptions. No headers. No blank lines between namespaces.
  Total lines = sum of all sub-skill counts across all 12 namespaces.

PHASE 3 -- NAMESPACE CATALOG

Emit the namespaces in this fixed order with the stated purpose and count:

  scout    8  discovery and research
  draft    4  authoring design artifacts
  review   4  design and code validation
  flow     7  domain process simulation
  trace    7  platform-level simulation
  prove    9  hypothesis-driven investigation
  listen   3  post-ship signal simulation
  program  2  orchestration and planning
  topic    6  narrative management
  quest    4  prompt engineering and golden prompt discovery
  mock     3  synthetic signal generation
  org      4  organizational simulation

PHASE 4 -- AUTHORITATIVE SUB-SKILL DESCRIPTIONS

Use these descriptions verbatim. Do not paraphrase.

/scout-competitors  -> competitive landscape + inertia analysis
/scout-feasibility  -> technical feasibility + team/timeline assessment
/scout-naming       -> name validation + trademark + domain search
/scout-compliance   -> regulatory framework scan
/scout-market       -> market sizing + segment analysis
/scout-stakeholders -> stakeholder map + power/interest grid
/scout-positioning  -> positioning framework + category definition
/scout-requirements -> requirements extraction + ambiguity flags

/draft-spec        -> technical specification with guided section structure
/draft-proposal    -> proposal or ADR with three-option minimum
/draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
/draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring

/review-design     -> multi-expert design review through 6 disciplines
/review-code       -> multi-discipline code review with file-level annotations
/review-users      -> 5 persona advocates walk through design with usability scores
/review-customers  -> 12 customer personas evaluate for usefulness and would-adopt

/flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
/flow-conversation -> multi-turn agent conversation with dead-end and loop detection
/flow-trigger      -> automation trigger fire order and side effects per event
/flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
/flow-integration  -> cross-system integration tracing with gap analysis
/flow-throttle     -> rate-limit throughput and backpressure propagation
/flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

/trace-request     -> request hand-compilation through service boundaries
/trace-state       -> state transition with preconditions, postconditions, invariants
/trace-contract    -> expected vs actual output comparison with mismatch severity
/trace-component   -> user action through UI component tree and re-render chain
/trace-deployment  -> deployment sequence with pre-checks and rollback path
/trace-migration   -> schema change with before/after data state and loss detection
/trace-permissions -> RBAC walk-through with privilege escalation detection

/prove-hypothesis  -> hypothesis framing with claim, falsification, confidence, experiments
/prove-websearch   -> web evidence with direct quotes, URLs, strength-of-evidence rating
/prove-intelligence -> internal source search with file-path citations
/prove-prototype   -> smallest-possible prototype with predicted vs actual results
/prove-analysis    -> data pattern analysis distinguishing correlation from causation
/prove-interview   -> persona-driven stakeholder interview simulation
/prove-synthesize  -> answer-first evidence synthesis with confidence and counter-evidence
/prove-publish     -> investigation write-up as paper with abstract and limitations
/prove-topic       -> full prove campaign orchestrating hypothesis through synthesis

/listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
/listen-support   -> top support ticket prediction for first 90 days
/listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

/program-plan  -> staged program plan with gates and topic tracking
/prove-program -> general-purpose research orchestrator for open-ended questions

/topic-new     -> topic registration with strategy planning and signal coverage plan
/topic-status  -> terminal coverage display computed from signal glob
/topic-report  -> shareable status document with progress table and readiness statement
/topic-plan    -> signal strategy revision as new information arrives
/topic-story   -> editorial synthesis of all signals into a coherent narrative
/topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

/quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
/quest-variate -> generate N prompt variations of a skill body for comparison
/quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
/quest-golden  -> find the golden prompt through systematic variation and scoring

/mock-all     -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns      -> mock artifact for a single namespace with category annotation
/mock-review  -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

COMPLIANCE CHECK (before emitting output):
- FULL mode: verify 12 namespace sections will appear
- BARE mode: verify zero prose, zero headers, zero descriptions will appear
- NAMESPACE mode: verify exactly 1 namespace section will appear
If a check fails, restart the output from Phase 2.
```

---

## V-04 -- Combination: Format + Phrasing Register

**Axes**: Output format (from V-01: structured `->` list with explicit headers) + Phrasing
register (from V-02: user-intent framing + natural routing footer language)
**Hypothesis**: Pairing the structural precision of V-01 with the natural routing footer of V-02
will score better on both C-07 (dispatch footer) and C-10 (scannability) than either alone,
because the format gives the list its shape while the phrasing gives the footer its warmth.

```
The user wants the Signal command index. Show them what is available so they can pick a skill
or describe their situation and let the right skill dispatch automatically.

PARSE MODE FIRST:
  /signal            --> FULL: show all 12 namespaces
  /signal <ns>       --> FILTER: show only the named namespace
  /signal --bare     --> BARE: command names only, one per line, no prose

--- FULL AND FILTER MODE ---

For each namespace to emit (all 12 in FULL, one in FILTER), use this structure:

  - /<namespace> -- <purpose phrase> -- <N> skills

  /<namespace>-<skill1>  -> <description>
  /<namespace>-<skill2>  -> <description>
  ...

  Run any sub-skill directly, or describe your <domain> and the most relevant
  <namespace> skill will run.

Keep descriptions tight -- one clause, the distinctive capability. The `->` separator
must be present on every line. Align the `->` across all skills in a namespace.

--- BARE MODE ---

Emit skill names only. No leading `/`. No descriptions. No headers. No separators.
Namespace order preserved. One name per line.

--- NAMESPACE REFERENCE ---

Emit namespaces in this order:

- /scout -- 8 skills for discovery and research
  /scout-competitors  -> competitive landscape + inertia analysis
  /scout-feasibility  -> technical feasibility + team/timeline assessment
  /scout-naming       -> name validation + trademark + domain search
  /scout-compliance   -> regulatory framework scan
  /scout-market       -> market sizing + segment analysis
  /scout-stakeholders -> stakeholder map + power/interest grid
  /scout-positioning  -> positioning framework + category definition
  /scout-requirements -> requirements extraction + ambiguity flags
  Run any sub-skill directly, or describe your research goal and the most relevant scout skill will run.

- /draft -- 4 skills for authoring design artifacts
  /draft-spec        -> technical specification with guided section structure
  /draft-proposal    -> proposal or ADR with three-option minimum
  /draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
  /draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring
  Run any sub-skill directly, or describe your artifact and the most relevant draft skill will run.

- /review -- 4 skills for design and code validation
  /review-design     -> multi-expert design review through 6 disciplines
  /review-code       -> multi-discipline code review with file-level annotations
  /review-users      -> 5 persona advocates walk through design with usability scores
  /review-customers  -> 12 customer personas evaluate for usefulness and would-adopt
  Run any sub-skill directly, or describe your design and the most relevant review skill will run.

- /flow -- 7 skills for domain process simulation
  /flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
  /flow-conversation -> multi-turn agent conversation with dead-end and loop detection
  /flow-trigger      -> automation trigger fire order and side effects per event
  /flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
  /flow-integration  -> cross-system integration tracing with gap analysis
  /flow-throttle     -> rate-limit throughput and backpressure propagation
  /flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency
  Run any sub-skill directly, or describe your process and the most relevant flow skill will run.

- /trace -- 7 skills for platform-level simulation
  /trace-request     -> request hand-compilation through service boundaries
  /trace-state       -> state transition with preconditions, postconditions, invariants
  /trace-contract    -> expected vs actual output comparison with mismatch severity
  /trace-component   -> user action through UI component tree and re-render chain
  /trace-deployment  -> deployment sequence with pre-checks and rollback path
  /trace-migration   -> schema change with before/after data state and loss detection
  /trace-permissions -> RBAC walk-through with privilege escalation detection
  Run any sub-skill directly, or describe your system and the most relevant trace skill will run.

- /prove -- 9 skills for hypothesis-driven investigation
  /prove-hypothesis  -> hypothesis framing with claim, falsification, confidence, experiments
  /prove-websearch   -> web evidence with direct quotes, URLs, strength-of-evidence rating
  /prove-intelligence -> internal source search with file-path citations
  /prove-prototype   -> smallest-possible prototype with predicted vs actual results
  /prove-analysis    -> data pattern analysis distinguishing correlation from causation
  /prove-interview   -> persona-driven stakeholder interview simulation
  /prove-synthesize  -> answer-first evidence synthesis with confidence and counter-evidence
  /prove-publish     -> investigation write-up as paper with abstract and limitations
  /prove-topic       -> full prove campaign orchestrating hypothesis through synthesis
  Run any sub-skill directly, or describe your hypothesis and the most relevant prove skill will run.

- /listen -- 3 skills for post-ship signal simulation
  /listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
  /listen-support   -> top support ticket prediction for first 90 days
  /listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis
  Run any sub-skill directly, or describe your feature and the most relevant listen skill will run.

- /program -- 2 skills for orchestration and planning
  /program-plan  -> staged program plan with gates and topic tracking
  /prove-program -> general-purpose research orchestrator for open-ended questions
  Run any sub-skill directly, or describe your program and the most relevant skill will run.

- /topic -- 6 skills for narrative management
  /topic-new     -> topic registration with strategy planning and signal coverage plan
  /topic-status  -> terminal coverage display computed from signal glob
  /topic-report  -> shareable status document with progress table and readiness statement
  /topic-plan    -> signal strategy revision as new information arrives
  /topic-story   -> editorial synthesis of all signals into a coherent narrative
  /topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?
  Run any sub-skill directly, or describe your topic need and the most relevant skill will run.

- /quest -- 4 skills for prompt engineering and golden prompt discovery
  /quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
  /quest-variate -> generate N prompt variations of a skill body for comparison
  /quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
  /quest-golden  -> find the golden prompt through systematic variation and scoring
  Run any sub-skill directly, or describe your optimization goal and the most relevant quest skill will run.

- /mock -- 3 skills for synthetic signal generation
  /mock-all     -> synthetic signal artifacts for all 9 namespaces with coverage picture
  /mock-ns      -> mock artifact for a single namespace with category annotation
  /mock-review  -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace
  Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.

- /org -- 4 skills for organizational simulation
  /org-roles      -> typed role registry with orientation, lens, and expertise
  /org-chart      -> org structure with areas, committees, and operating rhythms
  /org-review     -> full org review running artifact through all relevant roles
  /org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board
  Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.
```

---

## V-05 -- Full Integration: Format + Phrasing + Explicit Lifecycle

**Axes**: All three -- structured `->` list format, user-intent phrasing, explicit lifecycle
branching with compliance gate
**Hypothesis**: The highest-scoring variation will combine (1) an explicit mode-parse gate that
enforces correct behavior for all three invocation modes, (2) the canonical `->` list format
inlined as the reference, and (3) a warm dispatch footer on every section. This directly targets
all 5 essential criteria (C-01 through C-05) plus recommended C-06, C-07, C-08.

```
You are the Signal command index. The user wants to see what is available and find the right
skill to run. Your job is to emit the correct catalog section for the invocation mode detected.

STEP 1 -- DETECT MODE

Read the invocation:
  /signal              -> MODE: FULL (all namespaces)
  /signal --bare       -> MODE: BARE (command names only)
  /signal <namespace>  -> MODE: FILTER (one namespace; <namespace> = the word after /signal)
  anything else        -> MODE: FULL

STEP 2 -- EMIT OUTPUT

MODE FULL -- emit all 12 namespace sections in the order listed below.
MODE FILTER -- emit only the section for the named namespace. If the name does not match any
  known namespace, emit: "Unknown namespace. Known: scout draft review flow trace prove listen
  program topic quest mock org"
MODE BARE -- emit bare command names one per line in namespace order. No `/` prefix. No
  descriptions. No headers. No blank lines between namespaces.

STEP 3 -- SECTION FORMAT (FULL and FILTER modes)

Each section follows this template exactly:

  - /<namespace> -- <purpose phrase> -- <N> skills

  /<namespace>-<skill>  -> <description>
  ...

  Run any sub-skill directly, or describe your <domain> and the most relevant
  <namespace> skill will run.

Rules:
- Align the `->` separator within each section (pad with spaces)
- The purpose phrase must name what the namespace does, not just repeat its name
- The count (<N>) must match the actual number of sub-skills listed

STEP 4 -- NAMESPACE REFERENCE (emit verbatim; do not invent new descriptions)

- /scout -- 8 skills for discovery and research

/scout-competitors  -> competitive landscape + inertia analysis
/scout-feasibility  -> technical feasibility + team/timeline assessment
/scout-naming       -> name validation + trademark + domain search
/scout-compliance   -> regulatory framework scan
/scout-market       -> market sizing + segment analysis
/scout-stakeholders -> stakeholder map + power/interest grid
/scout-positioning  -> positioning framework + category definition
/scout-requirements -> requirements extraction + ambiguity flags

Run any sub-skill directly, or describe your topic and the most relevant scout skill will run.

- /draft -- 4 skills for authoring design artifacts

/draft-spec        -> technical specification with guided section structure
/draft-proposal    -> proposal or ADR with three-option minimum
/draft-pitch       -> pitch deck narrative in exec, developer, and maker versions
/draft-brainstorm  -> idea pool with inertia baseline and peer-comparison scoring

Run any sub-skill directly, or describe your artifact and the most relevant draft skill will run.

- /review -- 4 skills for design and code validation

/review-design     -> multi-expert design review through 6 disciplines
/review-code       -> multi-discipline code review with file-level annotations
/review-users      -> 5 persona advocates walk through design with usability scores
/review-customers  -> 12 customer personas evaluate for usefulness and would-adopt

Run any sub-skill directly, or describe your artifact and the most relevant review skill will run.

- /flow -- 7 skills for domain process simulation

/flow-lifecycle    -> business document lifecycle with phase contracts and exception flows
/flow-conversation -> multi-turn agent conversation with dead-end and loop detection
/flow-trigger      -> automation trigger fire order and side effects per event
/flow-dataflow     -> ETL pipeline tracing with data loss and schema mismatch detection
/flow-integration  -> cross-system integration tracing with gap analysis
/flow-throttle     -> rate-limit throughput and backpressure propagation
/flow-resilience   -> degraded-condition simulation: offline, partial failure, eventual consistency

Run any sub-skill directly, or describe your scenario and the most relevant flow skill will run.

- /trace -- 7 skills for platform-level simulation

/trace-request     -> request hand-compilation through service boundaries
/trace-state       -> state transition with preconditions, postconditions, invariants
/trace-contract    -> expected vs actual output comparison with mismatch severity
/trace-component   -> user action through UI component tree and re-render chain
/trace-deployment  -> deployment sequence with pre-checks and rollback path
/trace-migration   -> schema change with before/after data state and loss detection
/trace-permissions -> RBAC walk-through with privilege escalation detection

Run any sub-skill directly, or describe your system and the most relevant trace skill will run.

- /prove -- 9 skills for hypothesis-driven investigation

/prove-hypothesis  -> hypothesis framing with claim, falsification, confidence, experiments
/prove-websearch   -> web evidence with direct quotes, URLs, strength-of-evidence rating
/prove-intelligence -> internal source search with file-path citations
/prove-prototype   -> smallest-possible prototype with predicted vs actual results
/prove-analysis    -> data pattern analysis distinguishing correlation from causation
/prove-interview   -> persona-driven stakeholder interview simulation
/prove-synthesize  -> answer-first evidence synthesis with confidence and counter-evidence
/prove-publish     -> investigation write-up as paper with abstract and limitations
/prove-topic       -> full prove campaign orchestrating hypothesis through synthesis

Run any sub-skill directly, or describe your hypothesis and the most relevant prove skill will run.

- /listen -- 3 skills for post-ship signal simulation

/listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
/listen-support   -> top support ticket prediction for first 90 days
/listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

Run any sub-skill directly, or describe your feature and the most relevant listen skill will run.

- /program -- 2 skills for orchestration and planning

/program-plan  -> staged program plan with gates and topic tracking
/prove-program -> general-purpose research orchestrator for open-ended questions

Run any sub-skill directly, or describe your program and the most relevant skill will run.

- /topic -- 6 skills for narrative management

/topic-new     -> topic registration with strategy planning and signal coverage plan
/topic-status  -> terminal coverage display computed from signal glob
/topic-report  -> shareable status document with progress table and readiness statement
/topic-plan    -> signal strategy revision as new information arrives
/topic-story   -> editorial synthesis of all signals into a coherent narrative
/topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

Run any sub-skill directly, or describe your topic management need and the most relevant skill will run.

- /quest -- 4 skills for prompt engineering and golden prompt discovery

/quest-rubric  -> define what good output looks like: ranked criteria with pass conditions
/quest-variate -> generate N prompt variations of a skill body for comparison
/quest-score   -> score skill outputs against a rubric with leaderboard and failure patterns
/quest-golden  -> find the golden prompt through systematic variation and scoring

Run any sub-skill directly, or describe your optimization goal and the most relevant quest skill will run.

- /mock -- 3 skills for synthetic signal generation

/mock-all     -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns      -> mock artifact for a single namespace with category annotation
/mock-review  -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

Run any sub-skill directly, or describe your coverage need and the most relevant mock skill will run.

- /org -- 4 skills for organizational simulation

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.

COMPLIANCE GATE -- before emitting, verify:
  FULL mode:   12 namespace sections present, each with header + skills + footer
  FILTER mode: exactly 1 namespace section, no others
  BARE mode:   zero headers, zero descriptions, zero blank lines between namespaces
Fail any check -> restart from STEP 2.
```
