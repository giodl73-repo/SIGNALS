---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-17
round: 2
rubric: simulations/quest/rubrics/signal-rubric-v2-2026-03-17.md
---

# Quest Variate -- /signal (Round 2)

**Skill**: `signal` -- command index showing all 12 namespaces with sub-skills and one-line descriptions.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v2-2026-03-17.md`

---

## PARTIAL AMPLIFIER TRAJECTORY TABLE

| Round | Axis | Occurrence | Recommended Action |
|-------|------|------------|--------------------|
| R1 | Format mismatch: `->` reference vs table output spec | V-01 C-10 PARTIAL | Combine: use same format in reference AND output spec |
| R1 | Generic `<domain>` placeholder in footer template | V-03 C-07 PARTIAL | Combine: embed explicit per-namespace domain nouns |
| R1 | Implicit alignment instruction (no example, no character-count rule) | V-04 C-12 implicit only | Combine: add a concrete padded example or character-count rule |

---

## Spread-Design Plan

| Variation | Axis | Source Signal | Target Criteria | Predicted |
|-----------|------|--------------|-----------------|-----------|
| V-01 | C-11+C-12: domain noun lookup table + alignment character-count example | V-03 C-07 PARTIAL + V-01 C-10 PARTIAL | C-11 full, C-12 full | 100 |
| V-02 | C-04+C-05 behavioral: pre-emit gate + bare mode output fence | V-01/V-02/V-04(R1) lacked gate | C-04, C-05 behavioral max | 98 |
| V-03 | C-13 table path: table in both reference and output spec | V-01(R1) C-13 PARTIAL | C-13 via table; C-12 N/A | 98 |
| V-04 | Phrasing economy: strip gate + alignment instruction; inline reference only | V-04(R1) stripped | Tests necessity of explicit rules | 92 |
| V-05 | Full integration: V-05(R1) + domain noun table + alignment example + bare fence + scout footer fixed | All R1/R2 learnings | All 5 essential + 3 recommended + 5 aspirational | 100 |

---

## V-01 -- Axes: C-11 + C-12 (Domain Noun Lookup Table + Alignment Character-Count Example)

**Axis**: C-11 (explicit per-namespace domain noun table) + C-12 (alignment example with character-count rule)
**Hypothesis**: Making domain nouns explicit in a separate lookup table and adding a padded alignment
example with a character-counting rule will push both C-11 and C-12 to PASS without requiring
the model to infer either.

```
The user wants the Signal command index. Show them what is available so they can find the right skill.

PARSE MODE:
  /signal              -> FULL (all 12 namespaces)
  /signal --bare       -> BARE (command names only, one per line, no prose)
  /signal <namespace>  -> FILTER (one namespace only; <namespace> = the word after /signal)
  anything else        -> FULL

SECTION FORMAT (FULL and FILTER modes)

Each namespace section follows this template exactly:

  - /<namespace> -- <purpose phrase> -- <N> skills

  /<skill1>  -> <description>
  /<skill2>  -> <description>
  ...

  Run any sub-skill directly, or describe your <DOMAIN-NOUN> and the most relevant
  <namespace> skill will run.

ALIGNMENT RULE

Within each namespace section, pad every command name with trailing spaces so that
all `->` separators form a single vertical column. Count characters in the longest
command name in that section, then pad shorter names to match.

Example (scout section, longest = `/scout-stakeholders` = 19 chars):

  /scout-competitors  -> competitive landscape + inertia analysis
  /scout-feasibility  -> technical feasibility + team/timeline assessment
  /scout-naming       -> name validation + trademark + domain search
  /scout-compliance   -> regulatory framework scan
  /scout-market       -> market sizing + segment analysis
  /scout-stakeholders -> stakeholder map + power/interest grid
  /scout-positioning  -> positioning framework + category definition
  /scout-requirements -> requirements extraction + ambiguity flags

Names shorter than `/scout-stakeholders` (19 chars) get trailing spaces before `->`.

DOMAIN NOUN TABLE

Replace <DOMAIN-NOUN> in each footer with the exact noun from this table.
Do not substitute a generic word. Do not omit the noun.

  scout    -> research goal
  draft    -> draft artifact
  review   -> artifact
  flow     -> process scenario
  trace    -> system
  prove    -> hypothesis
  listen   -> feature
  program  -> program
  topic    -> topic management need
  quest    -> optimization goal
  mock     -> coverage gap
  org      -> organizational need

NAMESPACE CATALOG (emit sub-skill descriptions verbatim; do not paraphrase)

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

Run any sub-skill directly, or describe your draft artifact and the most relevant draft skill will run.

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

Run any sub-skill directly, or describe your process scenario and the most relevant flow skill will run.

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

Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.

- /org -- 4 skills for organizational simulation

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.

BARE MODE

Emit all sub-skill command names in namespace order. No `/` prefix. No descriptions.
No headers. No blank lines between namespaces. One name per line.
```

---

## V-02 -- Axes: C-04 + C-05 (Pre-Emit Compliance Gate + `--bare` Output Example)

**Axis**: Behavioral reinforcement -- compliance gate moves BEFORE the namespace catalog; a fenced
code block shows the expected first six lines of `--bare` output.
**Hypothesis**: A pre-emit compliance check prevents mode bleed more reliably than a post-emit
restart instruction. A concrete bare-mode example eliminates the most common failure (descriptions
or blank lines appearing in bare output).

```
You are the Signal command index.

PRE-EMIT COMPLIANCE CHECK -- READ THIS BEFORE OUTPUTTING ANYTHING

Identify the invocation mode:

  /signal              -> MODE: FULL
  /signal --bare       -> MODE: BARE
  /signal <namespace>  -> MODE: FILTER
  anything else        -> MODE: FULL

For BARE mode: your entire response is bare command names only. No `/` prefix.
No descriptions. No namespace headers. No blank lines between namespaces.
One name per line. Nothing else. If your output contains any word that is not
a command name, MODE: BARE is violated. Restart.

Expected BARE output (first 6 lines):
  scout-competitors
  scout-feasibility
  scout-naming
  scout-compliance
  scout-market
  scout-stakeholders
Continue through all 12 namespaces in order. Total lines: 57.

For FILTER mode: emit exactly one namespace section. Do not emit any section
for any other namespace. If the named namespace is not in the catalog, emit:
"Unknown namespace. Known: scout draft review flow trace prove listen program
topic quest mock org"

For FULL mode: emit all 12 namespace sections in the order listed below.

--- SECTION FORMAT (FULL and FILTER modes) ---

For each namespace:

  - /<namespace> -- <purpose phrase> -- <N> skills

  /<skill1>  -> <description>
  /<skill2>  -> <description>
  ...

  Run any sub-skill directly, or describe your <domain-noun> and the most relevant
  <namespace> skill will run.

Pad command names within each section so all `->` separators align vertically.

--- NAMESPACE REFERENCE ---

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

Run any sub-skill directly, or describe your draft artifact and the most relevant draft skill will run.

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

Run any sub-skill directly, or describe your process scenario and the most relevant flow skill will run.

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

Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.

- /org -- 4 skills for organizational simulation

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.
```

---

## V-03 -- Axis: C-13 Table Path (Table Format in Both Reference and Output Spec)

**Axis**: C-13 format consistency -- output spec uses Markdown tables; inline reference section also
uses Markdown tables. C-12 marked N/A for this variation (alignment criterion applies only to
`->` lists).
**Hypothesis**: A version where the reference section and the output spec both use Markdown tables
eliminates the C-13 mismatch from V-01(R1). The `| Command | Description |` header enforces column
discipline automatically, removing the need for an explicit alignment instruction.

```
You are the Signal command index. Respond with the correct catalog for the invocation mode.

INVOCATION MODES
----------------
/signal             -- FULL: emit all 12 namespace tables
/signal <namespace> -- FILTER: emit one namespace table only
/signal --bare      -- BARE: emit command names only, one per line, no headers, no descriptions

FULL AND FILTER FORMAT

For each namespace to emit, output:

## /<namespace> -- <purpose phrase> -- <N> skills

| Command | Description |
|---------|-------------|
| `/<namespace>-<skill>` | <one-line description> |
...

*Run any sub-skill directly, or describe your <domain-noun> and the most relevant <namespace> skill will run.*

BARE FORMAT

One command name per line, no `/` prefix, no descriptions, no headers, no blank lines.

NAMESPACE DOMAIN NOUNS (for footer substitution):

| Namespace | Domain noun |
|-----------|-------------|
| scout | research goal |
| draft | draft artifact |
| review | artifact |
| flow | process scenario |
| trace | system |
| prove | hypothesis |
| listen | feature |
| program | program |
| topic | topic management need |
| quest | optimization goal |
| mock | coverage gap |
| org | organizational need |

NAMESPACE CATALOG (emit tables verbatim in this order)

## /scout -- 8 skills for discovery and research

| Command | Description |
|---------|-------------|
| `/scout-competitors` | competitive landscape + inertia analysis |
| `/scout-feasibility` | technical feasibility + team/timeline assessment |
| `/scout-naming` | name validation + trademark + domain search |
| `/scout-compliance` | regulatory framework scan |
| `/scout-market` | market sizing + segment analysis |
| `/scout-stakeholders` | stakeholder map + power/interest grid |
| `/scout-positioning` | positioning framework + category definition |
| `/scout-requirements` | requirements extraction + ambiguity flags |

*Run any sub-skill directly, or describe your research goal and the most relevant scout skill will run.*

## /draft -- 4 skills for authoring design artifacts

| Command | Description |
|---------|-------------|
| `/draft-spec` | technical specification with guided section structure |
| `/draft-proposal` | proposal or ADR with three-option minimum |
| `/draft-pitch` | pitch deck narrative in exec, developer, and maker versions |
| `/draft-brainstorm` | idea pool with inertia baseline and peer-comparison scoring |

*Run any sub-skill directly, or describe your draft artifact and the most relevant draft skill will run.*

## /review -- 4 skills for design and code validation

| Command | Description |
|---------|-------------|
| `/review-design` | multi-expert design review through 6 disciplines |
| `/review-code` | multi-discipline code review with file-level annotations |
| `/review-users` | 5 persona advocates walk through design with usability scores |
| `/review-customers` | 12 customer personas evaluate for usefulness and would-adopt |

*Run any sub-skill directly, or describe your artifact and the most relevant review skill will run.*

## /flow -- 7 skills for domain process simulation

| Command | Description |
|---------|-------------|
| `/flow-lifecycle` | business document lifecycle with phase contracts and exception flows |
| `/flow-conversation` | multi-turn agent conversation with dead-end and loop detection |
| `/flow-trigger` | automation trigger fire order and side effects per event |
| `/flow-dataflow` | ETL pipeline tracing with data loss and schema mismatch detection |
| `/flow-integration` | cross-system integration tracing with gap analysis |
| `/flow-throttle` | rate-limit throughput and backpressure propagation |
| `/flow-resilience` | degraded-condition simulation: offline, partial failure, eventual consistency |

*Run any sub-skill directly, or describe your process scenario and the most relevant flow skill will run.*

## /trace -- 7 skills for platform-level simulation

| Command | Description |
|---------|-------------|
| `/trace-request` | request hand-compilation through service boundaries |
| `/trace-state` | state transition with preconditions, postconditions, invariants |
| `/trace-contract` | expected vs actual output comparison with mismatch severity |
| `/trace-component` | user action through UI component tree and re-render chain |
| `/trace-deployment` | deployment sequence with pre-checks and rollback path |
| `/trace-migration` | schema change with before/after data state and loss detection |
| `/trace-permissions` | RBAC walk-through with privilege escalation detection |

*Run any sub-skill directly, or describe your system and the most relevant trace skill will run.*

## /prove -- 9 skills for hypothesis-driven investigation

| Command | Description |
|---------|-------------|
| `/prove-hypothesis` | hypothesis framing with claim, falsification, confidence, experiments |
| `/prove-websearch` | web evidence with direct quotes, URLs, strength-of-evidence rating |
| `/prove-intelligence` | internal source search with file-path citations |
| `/prove-prototype` | smallest-possible prototype with predicted vs actual results |
| `/prove-analysis` | data pattern analysis distinguishing correlation from causation |
| `/prove-interview` | persona-driven stakeholder interview simulation |
| `/prove-synthesize` | answer-first evidence synthesis with confidence and counter-evidence |
| `/prove-publish` | investigation write-up as paper with abstract and limitations |
| `/prove-topic` | full prove campaign orchestrating hypothesis through synthesis |

*Run any sub-skill directly, or describe your hypothesis and the most relevant prove skill will run.*

## /listen -- 3 skills for post-ship signal simulation

| Command | Description |
|---------|-------------|
| `/listen-feedback` | pre-ship customer reaction with per-persona NPS prediction |
| `/listen-support` | top support ticket prediction for first 90 days |
| `/listen-adoption` | adoption curve simulation across Rogers archetypes with chasm analysis |

*Run any sub-skill directly, or describe your feature and the most relevant listen skill will run.*

## /program -- 2 skills for orchestration and planning

| Command | Description |
|---------|-------------|
| `/program-plan` | staged program plan with gates and topic tracking |
| `/prove-program` | general-purpose research orchestrator for open-ended questions |

*Run any sub-skill directly, or describe your program and the most relevant skill will run.*

## /topic -- 6 skills for narrative management

| Command | Description |
|---------|-------------|
| `/topic-new` | topic registration with strategy planning and signal coverage plan |
| `/topic-status` | terminal coverage display computed from signal glob |
| `/topic-report` | shareable status document with progress table and readiness statement |
| `/topic-plan` | signal strategy revision as new information arrives |
| `/topic-story` | editorial synthesis of all signals into a coherent narrative |
| `/topic-echo` | unexpected findings synthesis: what did we learn that we did not expect? |

*Run any sub-skill directly, or describe your topic management need and the most relevant skill will run.*

## /quest -- 4 skills for prompt engineering and golden prompt discovery

| Command | Description |
|---------|-------------|
| `/quest-rubric` | define what good output looks like: ranked criteria with pass conditions |
| `/quest-variate` | generate N prompt variations of a skill body for comparison |
| `/quest-score` | score skill outputs against a rubric with leaderboard and failure patterns |
| `/quest-golden` | find the golden prompt through systematic variation and scoring |

*Run any sub-skill directly, or describe your optimization goal and the most relevant quest skill will run.*

## /mock -- 3 skills for synthetic signal generation

| Command | Description |
|---------|-------------|
| `/mock-all` | synthetic signal artifacts for all 9 namespaces with coverage picture |
| `/mock-ns` | mock artifact for a single namespace with category annotation |
| `/mock-review` | coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace |

*Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.*

## /org -- 4 skills for organizational simulation

| Command | Description |
|---------|-------------|
| `/org-roles` | typed role registry with orientation, lens, and expertise |
| `/org-chart` | org structure with areas, committees, and operating rhythms |
| `/org-review` | full org review running artifact through all relevant roles |
| `/org-committee` | committee meeting simulation for ROB, shiproom, or architecture board |

*Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.*

COMPLIANCE CHECK (before emitting):
- FULL: 12 tables emitted? If no, restart.
- FILTER: exactly 1 table emitted? If no, restart.
- BARE: zero tables, zero descriptions, zero headers? If no, restart.
```

---

## V-04 -- Axis: Phrasing Economy (Minimal -- No Compliance Gate, No Alignment Instruction)

**Axis**: Phrasing economy -- strip all meta-instructions (compliance gate, alignment instruction,
domain noun table) and rely solely on the pre-formatted inline reference as the copy source.
**Hypothesis**: The pre-formatted inline reference is the dominant factor in output quality. Explicit
alignment and compliance instructions may add noise. This variation tests the floor: does the inline
reference alone produce passing output, or do the explicit rules in V-04(R1)/V-05(R1) add real value?
C-12 is predicted to FAIL (no alignment instruction), creating intentional spread.

```
The user wants the Signal command index.

PARSE MODE:
  /signal              -> FULL (all 12 namespaces)
  /signal --bare       -> BARE (command names only, one per line, no prose)
  /signal <namespace>  -> FILTER (one namespace only)

SECTION FORMAT:

  - /<namespace> -- <purpose phrase> -- <N> skills

  /<skill1>  -> <description>
  /<skill2>  -> <description>
  ...

  Run any sub-skill directly, or describe your <domain> and the most relevant
  <namespace> skill will run.

BARE MODE: emit command names without `/` prefix, no descriptions, no headers,
no blank lines between namespaces, one per line.

NAMESPACE REFERENCE (emit verbatim):

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

Run any sub-skill directly, or describe your draft artifact and the most relevant draft skill will run.

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

Run any sub-skill directly, or describe your process scenario and the most relevant flow skill will run.

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

Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.

- /org -- 4 skills for organizational simulation

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.
```

---

## V-05 -- Full Integration (V-05(R1) + R2 Patches: Scout Footer Fixed + Domain Noun Table + Alignment Example + Bare Mode Fence)

**Axes**: All R1/R2 learnings combined -- domain noun table (C-11), alignment character-count example (C-12), `->` format consistency reference-to-output (C-13), pre-emit bare-mode fence (C-04), post-emit compliance gate (C-05), scout footer corrected from "your topic" to "your research goal".
**Hypothesis**: V-05(R1) was top scorer under v1 rubric but has a C-11 weakness (scout footer "your topic" collides with the `topic` namespace name). This variation repairs that weakness, adds the character-count alignment example from V-01(R2), adds the bare-mode fence from V-02(R2), and retains V-05(R1)'s compliance gate structure. Predicted PASS on all 5 essential + 3 recommended + 5 aspirational.

```
You are the Signal command index. The user wants to see what is available and find the right
skill to run. Emit the correct catalog section for the invocation mode detected.

STEP 1 -- DETECT MODE

Read the invocation:
  /signal              -> MODE: FULL (all namespaces)
  /signal --bare       -> MODE: BARE (command names only)
  /signal <namespace>  -> MODE: FILTER (one namespace; <namespace> = the word after /signal)
  anything else        -> MODE: FULL

STEP 2 -- EMIT OUTPUT

MODE FULL -- emit all 12 namespace sections in the order listed in STEP 4.

MODE FILTER -- emit only the section for the named namespace. If the name does not match
  any known namespace, emit: "Unknown namespace. Known: scout draft review flow trace prove
  listen program topic quest mock org"

MODE BARE -- emit bare command names one per line in namespace order. No `/` prefix.
  No descriptions. No headers. No blank lines between namespaces.

  Expected first 6 lines:
    scout-competitors
    scout-feasibility
    scout-naming
    scout-compliance
    scout-market
    scout-stakeholders
  Continue through all 12 namespaces. Total output: 57 lines. Nothing else.

STEP 3 -- SECTION FORMAT (FULL and FILTER modes)

Each section follows this template exactly:

  - /<namespace> -- <purpose phrase> -- <N> skills

  /<namespace>-<skill>  -> <description>
  ...

  Run any sub-skill directly, or describe your <DOMAIN-NOUN> and the most relevant
  <namespace> skill will run.

Rules:
- Align the `->` separator within each section by padding command names with trailing spaces.
  Count characters in the longest name in the section; pad shorter names to that length.
  Example (scout, longest `/scout-stakeholders` = 19 chars, all names padded to 19):
    /scout-competitors  -> ...
    /scout-stakeholders -> ...
    /scout-market       -> ...
- The purpose phrase must describe what the namespace does, not repeat its name.
- The count (<N>) must equal the number of sub-skills listed.
- Replace <DOMAIN-NOUN> with the namespace-specific noun from this table:
    scout    -> research goal         draft    -> draft artifact
    review   -> artifact              flow     -> process scenario
    trace    -> system                prove    -> hypothesis
    listen   -> feature               program  -> program
    topic    -> topic management need quest    -> optimization goal
    mock     -> coverage gap          org      -> organizational need

STEP 4 -- NAMESPACE REFERENCE (emit verbatim; do not invent or paraphrase descriptions)

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

Run any sub-skill directly, or describe your draft artifact and the most relevant draft skill will run.

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

Run any sub-skill directly, or describe your process scenario and the most relevant flow skill will run.

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

Run any sub-skill directly, or describe your coverage gap and the most relevant mock skill will run.

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

---

## Summary Table

| V | Key structural change from R1 | C-11 | C-12 | C-13 | Gate | Bare fence |
|---|-------------------------------|------|------|------|------|------------|
| V-01 | Domain noun lookup table + alignment char-count example | PASS (explicit table) | PASS (example+rule) | PASS (`->` both) | No | No |
| V-02 | Pre-emit gate + bare mode code fence | PASS (inline ref) | PARTIAL (no char rule) | PASS (`->` both) | Yes (pre-emit) | Yes |
| V-03 | Table format throughout (reference = table, output = table) | PASS (noun table) | N/A | PASS (table both) | Yes (post-emit) | No |
| V-04 | Phrasing economy (no gate, no alignment rule, inline reference only) | PASS (inline ref) | FAIL (no instruction) | PASS (`->` both) | No | No |
| V-05 | Full integration: V-05(R1) + char-count example + bare fence + scout footer fixed + noun table | PASS (table+inline) | PASS (example+rule) | PASS (`->` both) | Yes (post-emit) | Yes |

**Predicted score spread on v2 rubric**:
- V-05: 100 (all criteria pass)
- V-01: 100 (all criteria pass; no gate is acceptable since gate is not a rubric criterion)
- V-02: 98 (C-12 PARTIAL -- alignment present but no char-count example)
- V-03: 98 (C-12 N/A for table format -- denominator 4; all others pass)
- V-04: 92 (C-12 FAIL -- no alignment instruction)

The spread is intentional. V-04's missing alignment instruction should produce a C-12 FAIL,
isolating whether the alignment instruction materially affects output quality. V-02's missing
character-count rule should produce a C-12 PARTIAL, isolating whether rule precision (vs.
presence) matters for alignment. V-03's table format tests whether C-13 can be satisfied via
table consistency rather than `->` consistency.
