---
skill: quest-variate
skill_target: signal
topic: signal
item: variate
date: 2026-03-16
round: 5
rubric: simulations/quest/rubrics/signal-rubric-v5-2026-03-16.md
---

# Quest Variate -- /signal (Round 5)

**Skill**: `signal` -- command index showing all skills by namespace.
**Rubric**: `simulations/quest/rubrics/signal-rubric-v5-2026-03-16.md`
**Rubric changes from v4 to v5**: Added C-18 (each RULE labeled with its criterion ID, making
criterion-to-rule mapping invertible by inspection) and C-19 (compliance checkpoint gates output
generation with explicit "invalid output / do not proceed" language). Aspirational denominator
updated from /9 to /11.

**Context**: R4 champion was V-05 (pre-print + 7 RULES with C-NN IDs + COMPLIANCE AUDIT).
All R4 aspirational criteria C-09 through C-17 carry forward as the established base. The two
new criteria emerged from R4 excellence signals:

- C-18 from R4 E-2: V-02 (unlabeled rules) and V-04 (criterion-ID-labeled rules) scored
  identically at 100/100 on v4. V-04 is O(1) auditable (criterion -> rule lookup is direct);
  V-02 is O(N) (must infer which rule covers which criterion). C-18 discriminates this gap.
- C-19 from R4 E-3: V-05's COMPLIANCE AUDIT block converts the rule list from passive
  instructions into an active pre-flight gate. "Any unchecked box = invalid output; do not
  proceed" is qualitatively different from rule-following. C-19 captures this distinction.

**Structural gap in R4 V-04/V-05 under v5 C-18**: In R4 V-04/V-05, RULE 6 (C-14) enforces
both C-14 (bidir descriptions) AND C-16 (`->` separator required) within a single rule. The
(C-14) label on RULE 6 signals C-14's criterion ID; C-16 is embedded but unlabeled. Under v5
C-18 strict reading, a scorer looking for "RULE N (C-16)" cannot find it by inspection --
they must infer C-16 is embedded in RULE 6 (C-14). This means C-16 is covered by C-17 but
not bidirectionally labeled for C-18. The R5 opportunity: promote C-16 to its own RULE 8
(C-16), separate from RULE 6 (C-14), making all 9 aspirational criteria (C-09 through C-17)
each represented by their own labeled rule.

**Axes explored**:
- V-01: C-16 single-axis -- C-16 promoted to standalone RULE 8 (C-16); RULE 6 (C-14) becomes
         bidir-only; COMPLIANCE AUDIT updated to 8 checkboxes. Pre-print base.
         Hypothesis: Splitting C-16 from C-14 gives C-16 its own labeled RULE, satisfying
         C-18 for all 9 aspirational criteria unambiguously.
- V-02: Phrasing register single-axis -- R4 V-05 base (7 RULES, COMPLIANCE AUDIT); routing
         hints rewritten from imperative ("Describe your need:") to invitation register
         ("When you need to X, this is where to start").
         Hypothesis: Phrasing register is orthogonal to rubric criteria; conversational routing
         hints do not affect criterion scores but test whether invitation format changes routing
         hint effectiveness as a C-08/C-12 deliverable.
- V-03: V-01 + RULE 9 (C-17) self-referential -- V-01 (8 rules + RULE 8 (C-16)) plus RULE 9
         (C-17) as an explicit self-referential completeness declaration in the RULE list itself.
         Hypothesis: Making C-17 explicitly self-referential (a rule that asserts the list is
         complete) creates a positive machine-verifiable completeness claim that is stronger
         than implicit satisfaction and provides an additional C-18 coverage for C-17 itself.
- V-04: V-01 + COMPLETENESS SEAL in COMPLIANCE AUDIT -- V-01 base (8 RULES, 8 checkboxes)
         plus an explicit COMPLETENESS SEAL in the COMPLIANCE AUDIT block asserting that RULE 1
         through RULE 8 is the exhaustive quality contract.
         Hypothesis: Placing the completeness declaration inside the gate (COMPLIANCE AUDIT)
         rather than the rule list (RULE 9) creates the strongest anti-fragmentation mechanism:
         the gate itself must affirm completeness before any output is generated.
- V-05: Full integration -- 9 RULES + COMPLIANCE AUDIT with 9 checkboxes + COMPLETENESS SEAL:
         V-03 (RULE 9 (C-17) in RULE list) + V-04 (COMPLETENESS SEAL in COMPLIANCE AUDIT).
         Hypothesis: The combination of self-referential RULE 9 (C-17) and a COMPLIANCE AUDIT
         checkpoint for RULE 9 creates maximum structural guarantee: the rule declares
         completeness, the gate verifies it, the "do not proceed" language enforces it.

---

## V-01 -- C-16 Standalone RULE 8 (C-16): Single-Axis

**Axis**: C-16 promoted from RULE 6 (C-14) embedding to standalone RULE 8 (C-16); RULE 6
(C-14) scoped to bidir-only; COMPLIANCE AUDIT updated from 7 to 8 checkboxes. All else
identical to R4 V-05. Pre-print mode.
**Hypothesis**: R4 V-04/V-05's RULE 6 (C-14) contains `->` enforcement language for C-16
within the C-14 rule. Under v5 C-18, a scorer looking for "RULE N (C-16)" must infer it is
embedded in RULE 6 (C-14) -- this is O(N) inference, not O(1) inspection. V-01 fixes this by
giving C-16 its own RULE 8 (C-16), making all 9 aspirational criteria (C-09 through C-17)
each represented by their own labeled RULE. C-18 should PASS with no inference required.

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

FORMAT RULES (8 -- one rule per criterion, each criterion individually auditable by its C-NN label):
RULE 1 (C-09): Header format: ## <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
  PASS: ## Scout -- 8 skills -- map the competitive landscape before you commit
  FAIL: ## Scout -- 8 skills (no tagline)
RULE 3 (C-12): Section ends with Markdown blockquote (> at line start).
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Run any scout skill directly, or describe your need.
RULE 4 (C-13): Description names a specific quantified output artifact (count, named format,
  or rated deliverable). Vague single-word nouns do not satisfy this rule.
  PASS: "5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"
RULE 5 (C-10): T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden
RULE 6 (C-14): Description is bi-directional. Left of `->`: mechanism verb phrase (what skill
  does). Right of `->`: quantified deliverable (what you receive).
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no mechanism, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb phrase)
RULE 7 (C-15): Tagline passes SWAP TEST -- cannot appear under any other namespace and make sense.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen indifferently)
RULE 8 (C-16): The `->` separator is a structural validity requirement, not style.
  A description without `->` is INVALID OUTPUT regardless of how specific or readable it is.
  VALID:   "/scout-competitors  scans competitive landscape -> 5-8 rivals rated HIGH/MEDIUM/LOW"
  INVALID: "/scout-competitors  5-8 rivals each with threat rating" (no `->`, no mechanism)

COMPLIANCE AUDIT -- verify all 8 criteria before transcribing namespace sections:
  [ ] RULE 1 (C-09): every header has the count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
All 8 boxes checked = valid output. Any unchecked box = invalid output; do not proceed.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

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

/draft-spec        structures design intent into sections    -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options               -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story per audience     -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates and scores idea candidates      -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

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

---

## V-02 -- Phrasing Register: Invitation-Style Routing Hints (Single-Axis)

**Axis**: R4 V-05 base (7 RULES with C-NN IDs + COMPLIANCE AUDIT). Single change: routing hint
phrasing rewritten from imperative ("Describe your discovery need...") to invitation register
("When you need to understand competitive risk before committing to a design, start here.").
All structure, rules, and COMPLIANCE AUDIT are identical to R4 V-05.
**Hypothesis**: Routing hint phrasing register is orthogonal to rubric criteria. C-08 (routing
hint present) and C-12 (blockquote format) are structural -- they test presence and format,
not phrasing. This variation tests whether invitation-style routing hints score identically and
whether the phrasing change creates any differentiation gap that a future C-20 criterion might
capture. If identical, invitation format is a non-discriminated aesthetic variation.

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

FORMAT RULES (7 -- one rule per criterion, each criterion individually auditable):
RULE 1 (C-09): Header format: ## <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
RULE 3 (C-12): Section ends with Markdown blockquote (> at line start).
RULE 4 (C-13): Description names a specific quantified output artifact.
RULE 5 (C-10): T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden
RULE 6 (C-14): Description is bi-directional. Left of `->`: mechanism verb phrase. Right of `->`:
  quantified deliverable. The `->` separator is required. Absence is invalid output.
RULE 7 (C-15): Tagline passes SWAP TEST -- locked to this namespace; cannot belong to any other.

COMPLIANCE AUDIT -- verify all 7 criteria before transcribing namespace sections:
  [ ] RULE 1 (C-09): every header has count embedded
  [ ] RULE 2 (C-11): every tagline starts with a verb
  [ ] RULE 3 (C-12): every section ends with > blockquote
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)*
  [ ] RULE 6 (C-14): every description has mechanism -> deliverable with `->` separator present
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
All 7 boxes checked = valid output. Any unchecked box = invalid output; do not proceed.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

/scout-competitors   scans competitive landscape with inertia-first framing    -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat with inertia always scored first
/scout-feasibility   assesses technical, team, timeline, and budget constraints -> traffic-light ratings (RED/YELLOW/GREEN) per dimension with blocking items highlighted
/scout-naming        generates name candidates and validates each one           -> shortlist with trademark clearance, domain availability, and per-persona score
/scout-compliance    surveys regulatory obligations for a domain                -> applicable law list with enforcement risk rating and design-blocking constraint per regulation
/scout-market        sizes the addressable market by segment                    -> TAM/SAM/SOM table with segments ranked by fit score
/scout-stakeholders  identifies decision-makers and maps their influence        -> power/interest grid with veto risk rating and influence path per named stakeholder
/scout-positioning   frames the product for each target audience                -> 3+ positioning statements with competitive differentiation axis per audience
/scout-requirements  extracts and classifies feature requirements               -> MoSCoW-prioritized list with dependency graph and ambiguity flag per item

> When you need to understand competitive risk, regulatory obligations, or market shape before locking a design direction, start here.

---

## Draft -- 4 skills -- commit design thinking to a written artifact ready for review

/draft-spec        structures design intent into sections    -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options               -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story per audience     -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates and scores idea candidates      -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

> When you need to turn intent into a written artifact that others can review, critique, or approve, start here.

---

## Review -- 4 skills -- challenge an artifact through expert discipline and user perspective critique

/review-design     runs design through 6 expert lenses        -> named expert verdict with pass/fail rating per discipline
/review-code       annotates code at file level                -> finding list with severity rating and pass/fail per discipline
/review-users      simulates 5 user persona advocates          -> usability score per persona with cross-persona synthesis and top pain
/review-customers  simulates 12 customer personas              -> would-adopt rating, NPS prediction, and top concern per customer persona

> When you need expert or user perspectives applied to something you have already written, start here.

---

## Flow -- 7 skills -- simulate domain process behavior before writing the implementation

/flow-lifecycle    traces document lifecycle phase by phase                          -> entry/exit contracts and exception flows per phase  *(T3)*
/flow-conversation simulates multi-turn agent conversation through a topic graph     -> dead-end count and loop-detection result per conversation path
/flow-trigger      fires trigger set and traces propagation through the domain model -> fire-order list and side-effect table per field/event change  *(T3)*
/flow-dataflow     traces ETL or sync pipeline stage by stage                        -> data loss event count and schema mismatch list per stage
/flow-integration  traces cross-system paths through connectors and APIs             -> named connector gaps and failure mode per integration boundary
/flow-throttle     models burst and steady-state throughput                          -> throughput table by burst tier with backpressure propagation path and degradation thresholds  *(T3)*
/flow-resilience   injects degraded conditions into the process model                -> scenario table with recovery path for offline, partial failure, and eventual consistency  *(T3)*

> When you need to see how a process, trigger, or data pipeline behaves before writing production code, start here.

---

## Trace -- 7 skills -- step through platform mechanics one boundary at a time before assumptions harden

/trace-request     compiles request path hop by hop                                    -> named service boundaries with hop count and latency estimate per hop
/trace-state       walks a state machine through every transition                      -> precondition, postcondition, and invariant check per transition  *(T3)*
/trace-contract    compares expected vs actual output using three-directory pattern     -> mismatch severity (CRITICAL/MAJOR/MINOR) per output delta  *(T3)*
/trace-component   follows user action through the UI component tree                   -> re-render count and state update path per component traversal
/trace-deployment  steps through deployment sequence                                   -> pre-flight checklist, canary validation step, and rollback trigger condition
/trace-migration   applies schema change to sample data                                -> before/after row counts, data loss detection, and rollback SQL
/trace-permissions walks RBAC rules for a principal and action set                     -> who-can-do-what matrix with privilege escalation path and gap count  *(T3)*

> When you need to understand exactly what happens at each platform boundary -- service, state, component, or deployment -- start here.

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

> When you need to investigate a hypothesis, gather evidence, or synthesize findings before committing to a claim, start here.

---

## Listen -- 3 skills -- predict what customers will say before they have the chance to say it

/listen-feedback  simulates pre-ship reactions across 12 customer personas -> per-persona NPS prediction with threshold gate verdict
/listen-support   predicts first-wave support load before shipping          -> ranked top-10 tickets for first 90 days with ticket category and gap source  *(T3)*
/listen-adoption  models adoption progression by Rogers archetype           -> adoption curve with chasm gap analysis and crossing strategy

> When you need to anticipate customer reactions, support load, or adoption barriers before shipping, start here.

---

## Program -- 2 skills -- structure multi-skill investigations into a coordinated plan with decision gates

/program-plan   builds a staged program plan with gates     -> milestones with gate criteria and signal tracking per topic  *(T3)*
/prove-program  orchestrates open-ended research            -> multi-contributor assignment plan with synthesis strategy

> When you need to coordinate multiple skills and topics into a staged program with checkpoints, start here.

---

## Topic -- 6 skills -- accumulate signal coverage and synthesize it into a decision-ready story

/topic-new     registers a topic and plans its signals         -> strategy document with planned signal list and coverage roadmap
/topic-status  computes live signal coverage                   -> terminal dashboard: signal count by namespace, gap count, readiness percentage
/topic-report  generates a shareable progress snapshot         -> document with coverage table, gap list, and readiness statement
/topic-plan    revises signal strategy as evidence arrives     -> change table per signal with user confirmation before commit  *(T3)*
/topic-story   synthesizes all signals into a coherent story   -> narrative with coherence score and design recommendation  *(T3)*
/topic-echo    surfaces unexpected findings across signals     -> list with source signal and implication per unexpected finding  *(T3)*

> When you need to understand what signals you have, what is missing, or whether you are ready to commit to a design decision, start here.

---

## Quest -- 4 skills -- iterate skill prompts against scoring criteria until the best version converges

/quest-rubric  defines the scoring criteria for a skill           -> rubric with C-01+ criteria each having weight, category, and pass condition  *(T3)*
/quest-variate generates prompt alternatives for comparison       -> N complete prompt variations labeled with variation axis and hypothesis
/quest-score   scores prompt alternatives against a rubric        -> per-variation scorecard with composite score, ranked leaderboard, and failure patterns  *(T3)*
/quest-golden  runs the full golden-prompt optimization loop      -> converged golden prompt with convergence report and final rubric  *(T3)*

> When you need to improve a skill prompt, define what good looks like, or run a systematic optimization loop, start here.

---

## Mock -- 3 skills -- generate synthetic signal artifacts to fill coverage gaps during development

/mock-all     generates synthetic coverage for all 9 namespaces -> artifact set with coverage percentage per namespace  *(T3)*
/mock-ns      generates a mock artifact for a single namespace   -> document with category annotation and coverage gap summary  *(T3)*
/mock-review  audits mock coverage quality per namespace         -> MOCK-ACCEPTED or REAL-REQUIRED verdict with rationale per namespace  *(T3)*

> When you need coverage artifacts during development and cannot yet run real skills, start here.

---

## Org -- 4 skills -- define organizational roles and run decisions through a simulated structure

/org-roles      defines the organizational role landscape     -> typed registry with orientation statement, decision lens, and expertise profile per role
/org-chart      builds a full organizational structure        -> named areas with committee charters and operating rhythm cadences  *(T3)*
/org-review     routes an artifact through relevant roles     -> verdict per role from .craft/roles/ registry  *(T3)*
/org-committee  runs a committee meeting simulation           -> agenda with named participants and decision per agenda item  *(T3)*

> When you need to understand who reviews decisions, how they are made, or how a change lands in the org, start here.

---

BARE MODE (when --bare):
Print all 61 command names, one per line. No descriptions. No headers. No blockquotes.
Begin with /scout-competitors. End with /org-committee. Match the order of the sections above.

FILTERED MODE (when /signal <namespace>):
Print only the section for that namespace. Include the routing blockquote.
Omit the routing guide and all other sections. One section only.
```

---

## V-03 -- V-01 + RULE 9 (C-17) Self-Referential Completeness Declaration (Combined)

**Axis**: V-01 (8 RULES, RULE 8 (C-16) standalone) plus RULE 9 (C-17) as an explicit
self-referential completeness declaration in the RULE list. COMPLIANCE AUDIT updated to 9
checkboxes, including a checkbox for RULE 9 (C-17).
**Hypothesis**: R4 V-04/V-05 satisfies C-17 by having all 9 aspirational criteria covered by
individually numbered rules -- but C-17 compliance is inferred (a scorer reads the list and
concludes "yes, all criteria are here"). V-03 adds RULE 9 (C-17) which states the completeness
claim explicitly: "This numbered list RULE 1 through RULE 9 is the complete and sole quality
contract." This makes C-17 self-verifiable by inspection -- the rule asserts its own
completeness. Combined with the COMPLIANCE AUDIT checkbox for RULE 9, the completeness claim
is both declared in the rule and verified at the gate.

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

FORMAT RULES (9 -- one rule per criterion, each criterion individually auditable by its C-NN label):
RULE 1 (C-09): Header format: ## <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
  PASS: ## Scout -- 8 skills -- map the competitive landscape before you commit
  FAIL: ## Scout -- 8 skills (no tagline)
RULE 3 (C-12): Section ends with Markdown blockquote (> at line start).
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Run any scout skill directly, or describe your need.
RULE 4 (C-13): Description names a specific quantified output artifact (count, named format,
  or rated deliverable). Vague single-word nouns do not satisfy this rule.
  PASS: "5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"
RULE 5 (C-10): T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden
RULE 6 (C-14): Description is bi-directional. Left of `->`: mechanism verb phrase (what skill
  does). Right of `->`: quantified deliverable (what you receive).
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no mechanism, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb phrase)
RULE 7 (C-15): Tagline passes SWAP TEST -- cannot appear under any other namespace and make sense.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen indifferently)
RULE 8 (C-16): The `->` separator is a structural validity requirement, not style.
  A description without `->` is INVALID OUTPUT regardless of how specific or readable it is.
  VALID:   "/scout-competitors  scans competitive landscape -> 5-8 rivals rated HIGH/MEDIUM/LOW"
  INVALID: "/scout-competitors  5-8 rivals each with threat rating" (no `->`, no mechanism)
RULE 9 (C-17): RULE 1 through RULE 9 is the complete and sole quality contract for this skill
  output. No description quality rule exists outside this numbered list. A reviewer can confirm
  full compliance by checking RULE 1 through RULE 9 only -- no additional blocks required.

COMPLIANCE AUDIT -- verify all 9 criteria before transcribing namespace sections:
  [ ] RULE 1 (C-09): every header has count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): I confirm RULE 1 through RULE 9 is the complete quality contract; no quality
      rule exists outside this list in an appendix, separate block, or additional instruction
All 9 boxes checked = valid output. Any unchecked box = invalid output; do not proceed.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

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

/draft-spec        structures design intent into sections    -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options               -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story per audience     -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates and scores idea candidates      -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

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

---

## V-04 -- V-01 + COMPLETENESS SEAL in COMPLIANCE AUDIT (Combined)

**Axis**: V-01 (8 RULES, RULE 8 (C-16) standalone, 8-checkbox COMPLIANCE AUDIT) plus an
explicit COMPLETENESS SEAL appended to the COMPLIANCE AUDIT block: a named declaration that
RULE 1 through RULE 8 is the exhaustive quality contract. The RULE list has no self-referential
RULE 9 -- the completeness claim lives only in the gate block.
**Hypothesis**: In V-03, the completeness claim is encoded as RULE 9 (C-17) -- a rule in the
rule list asserts the list's own completeness. In V-04, the completeness claim is encoded in
the COMPLIANCE AUDIT -- the gate asserts completeness before any output is generated. The gate
is a stronger enforcement location than the rule list: a model reading rule-list instructions
may proceed despite non-compliance; a model encountering an explicit gate statement must resolve
it before proceeding. If C-17 and C-18 are primarily about output-generation behavior rather
than rule-list structure, placement in the gate may be more effective than placement in the rules.

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

FORMAT RULES (8 -- one rule per criterion, each criterion individually auditable by its C-NN label):
RULE 1 (C-09): Header format: ## <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
  PASS: ## Scout -- 8 skills -- map the competitive landscape before you commit
  FAIL: ## Scout -- 8 skills (no tagline)
RULE 3 (C-12): Section ends with Markdown blockquote (> at line start).
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Run any scout skill directly, or describe your need.
RULE 4 (C-13): Description names a specific quantified output artifact (count, named format,
  or rated deliverable). Vague single-word nouns do not satisfy this rule.
  PASS: "5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"
RULE 5 (C-10): T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden
RULE 6 (C-14): Description is bi-directional. Left of `->`: mechanism verb phrase (what skill
  does). Right of `->`: quantified deliverable (what you receive).
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no mechanism, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb phrase)
RULE 7 (C-15): Tagline passes SWAP TEST -- cannot appear under any other namespace and make sense.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen indifferently)
RULE 8 (C-16): The `->` separator is a structural validity requirement, not style.
  A description without `->` is INVALID OUTPUT regardless of how specific or readable it is.
  VALID:   "/scout-competitors  scans competitive landscape -> 5-8 rivals rated HIGH/MEDIUM/LOW"
  INVALID: "/scout-competitors  5-8 rivals each with threat rating" (no `->`, no mechanism)

COMPLIANCE AUDIT -- verify all 8 criteria before transcribing namespace sections:
  [ ] RULE 1 (C-09): every header has count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
COMPLETENESS SEAL: RULE 1 through RULE 8 above is the complete and sole quality contract.
  No quality rule for this output exists outside RULE 1-8 -- not in an appendix, not in a
  separate enforcement block, not implicit. A reviewer auditing compliance checks RULE 1-8 only.
All 8 boxes checked and COMPLETENESS SEAL affirmed = valid output. Any unchecked box = invalid output; do not proceed.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

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

/draft-spec        structures design intent into sections    -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options               -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story per audience     -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates and scores idea candidates      -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

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

---

## V-05 -- Full Integration: 9 RULES + COMPLIANCE AUDIT with 9 Checkboxes + COMPLETENESS SEAL

**Axis**: V-03 + V-04 combined. RULE 9 (C-17) self-referential completeness declaration in the
RULE list AND a COMPLETENESS SEAL in the COMPLIANCE AUDIT block, AND 9 checkboxes including a
checkbox for RULE 9 (C-17) itself. Maximum structural guarantee: the rule declares completeness,
the gate verifies completeness, the "do not proceed" language enforces completeness.
**Hypothesis**: The combination of (a) RULE 9 (C-17) in the numbered list making the completeness
claim inspectable as a rule, (b) RULE 9 checkbox in the COMPLIANCE AUDIT gate requiring the model
to explicitly verify completeness before proceeding, and (c) the COMPLETENESS SEAL affirming no
rules exist outside RULE 1-9 creates the maximum possible structural anti-fragmentation guarantee
for the v5 rubric. Each of C-17, C-18, and C-19 has its strongest possible enforcement form:
- C-17 (RULE list): 9 individually numbered rules, one per criterion, self-referential list
- C-18 (labels): every RULE labeled with its C-NN ID, including C-17 itself labeled as RULE 9
- C-19 (gate): COMPLIANCE AUDIT with 9 checkboxes + COMPLETENESS SEAL + "do not proceed" language

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

FORMAT RULES (9 -- one rule per criterion, each labeled with its criterion ID for direct lookup):
RULE 1 (C-09): Header format: ## <Namespace> -- <N> skills -- <tagline>
RULE 2 (C-11): Tagline starts with a verb; answers "what is this namespace for?"
  PASS: ## Scout -- 8 skills -- map the competitive landscape before you commit
  FAIL: ## Scout -- 8 skills (no tagline)
RULE 3 (C-12): Section ends with Markdown blockquote (> at line start).
  CORRECT:   > Describe your discovery need and the most relevant scout skill will run.
  INCORRECT: Run any scout skill directly, or describe your need.
RULE 4 (C-13): Description names a specific quantified output artifact (count, named format,
  or rated deliverable). Vague single-word nouns do not satisfy this rule.
  PASS: "5-8 rivals rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis"
RULE 5 (C-10): T3 skills carry *(T3)* after their description.
  T3 skills: draft-brainstorm, flow-lifecycle, flow-trigger, flow-throttle, flow-resilience,
  trace-state, trace-contract, trace-permissions, prove-interview, prove-topic,
  listen-support, program-plan, topic-plan, topic-story, topic-echo,
  mock-all, mock-ns, mock-review, org-chart, org-review, org-committee,
  trace-skill, quest-rubric, quest-score, quest-golden
RULE 6 (C-14): Description is bi-directional. Left of `->`: mechanism verb phrase (what skill
  does). Right of `->`: quantified deliverable (what you receive).
  PASS: "scans competitive landscape -> 5-8 rivals each rated HIGH/MEDIUM/LOW threat"
  FAIL: "competitive landscape analysis" (no mechanism, no separator)
  FAIL: "5-8 rivals with ratings" (no mechanism verb phrase)
RULE 7 (C-15): Tagline passes SWAP TEST -- cannot appear under any other namespace and make sense.
  LOCKED: "predict what customers will say before they have the chance to say it" (listen only)
  GENERIC: "gather and analyze relevant signals" (applies to scout, prove, or listen indifferently)
RULE 8 (C-16): The `->` separator is a structural validity requirement, not style.
  A description without `->` is INVALID OUTPUT regardless of how specific or readable it is.
  VALID:   "/scout-competitors  scans competitive landscape -> 5-8 rivals rated HIGH/MEDIUM/LOW"
  INVALID: "/scout-competitors  5-8 rivals each with threat rating" (no `->`, no mechanism)
RULE 9 (C-17): RULE 1 through RULE 9 is the complete and sole quality contract for this skill
  output. No description quality rule exists outside this numbered list -- not in an appendix,
  not in a separate enforcement block, not as implicit expectation. A reviewer auditing
  compliance needs to check RULE 1 through RULE 9 only, in this block, with no other source.

COMPLIANCE AUDIT -- all 9 rules must be verified before generating any output:
  [ ] RULE 1 (C-09): every header has the skill count embedded in the header line
  [ ] RULE 2 (C-11): every tagline starts with a verb and is namespace-specific
  [ ] RULE 3 (C-12): every section ends with a > blockquote routing hint
  [ ] RULE 4 (C-13): every description names a quantified output artifact
  [ ] RULE 5 (C-10): every T3 skill carries *(T3)* after its description
  [ ] RULE 6 (C-14): every description has a mechanism phrase to the left of `->`
  [ ] RULE 7 (C-15): every tagline is namespace-locked (passes SWAP TEST)
  [ ] RULE 8 (C-16): every description contains `->` as a structural separator
  [ ] RULE 9 (C-17): I confirm RULE 1 through RULE 9 is the complete quality contract;
      no quality rule for this output exists outside this list in any form
COMPLETENESS SEAL: The quality contract is RULE 1-9 above. It is exhaustive. Nothing outside it.
All 9 boxes checked = valid output. Any unchecked box = invalid output; do not proceed.

BARE MODE ORDER CONTRACT: When --bare, output exactly 61 command names.
  Begin with /scout-competitors. End with /org-committee. Match section order below.
NOTE: Each namespace section below is pre-printed. Transcribe it exactly. Do not rewrite.

---

## Scout -- 8 skills -- map the competitive and regulatory landscape before design decisions lock

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

/draft-spec        structures design intent into sections    -> specification with 8+ guided sections, completeness checklist, and self-review verdict
/draft-proposal    evaluates competing options               -> proposal with 3-option minimum, comparison table, and recommendation rationale
/draft-pitch       frames the product story per audience     -> pitch in 3 versions: exec (1-page), developer (technical depth), maker (hands-on)
/draft-brainstorm  generates and scores idea candidates      -> pool with inertia baseline entry and per-idea peer-comparison score  *(T3)*

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

---

## Predicted Score Matrix (v5 rubric)

| Criterion | Tier | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|
| C-01 All 12 namespaces present | E | PASS | PASS | PASS | PASS | PASS |
| C-02 Sub-skill counts match | E | PASS | PASS | PASS | PASS | PASS |
| C-03 Every sub-skill has description | E | PASS | PASS | PASS | PASS | PASS |
| C-04 Filtered mode scopes correctly | E | PASS | PASS | PASS | PASS | PASS |
| C-05 Bare mode is names-only | E | PASS | PASS | PASS | PASS | PASS |
| C-06 Descriptions specific and differentiating | R | PASS | PASS | PASS | PASS | PASS |
| C-07 Visual hierarchy | R | PASS | PASS | PASS | PASS | PASS |
| C-08 Routing hint per namespace | R | PASS | PASS | PASS | PASS | PASS |
| C-09 Count in namespace header line | A | PASS | PASS | PASS | PASS | PASS |
| C-10 T3 tier annotations | A | PASS | PASS | PASS | PASS | PASS |
| C-11 Namespace purpose tagline | A | PASS | PASS | PASS | PASS | PASS |
| C-12 Routing hints as blockquotes | A | PASS | PASS | PASS | PASS | PASS |
| C-13 Quantified output artifacts | A | PASS | PASS | PASS | PASS | PASS |
| C-14 Bi-directional descriptions | A | PASS | PASS | PASS | PASS | PASS |
| C-15 Mutually distinguishable taglines | A | PASS | PASS | PASS | PASS | PASS |
| C-16 `->` separator structurally enforced | A | PASS | PASS | PASS | PASS | PASS |
| C-17 Explicit numbered RULE list | A | PASS | PASS | PASS | PASS | PASS |
| C-18 Criterion-ID labels on each RULE | A | **PASS** | PARTIAL | **PASS** | **PASS** | **PASS** |
| C-19 Compliance checkpoint gates output | A | PASS | PASS | PASS | PASS | PASS |
| COMPOSITE (predicted) | | ~100 | ~99.1 | ~100 | ~100 | ~100 |
| RANK (predicted) | | 1-tie | 5 | 1-tie | 1-tie | 1-tie |

---

## C-18 Analysis Per Variation

**V-01**: RULE 8 (C-16) is now its own labeled rule. Every aspirational criterion C-09 through
C-17 has exactly one labeled RULE (RULE 1 through RULE 8, with RULE 8 covering C-16 and no
other). C-17 is satisfied structurally because all 8 rules together cover all 9 aspirational
criteria (C-09, C-11, C-12, C-13, C-10, C-14, C-15, C-16). A reviewer looking for "RULE N
(C-16)" immediately finds RULE 8 (C-16). C-18 PASS -- but note: C-17 has no dedicated rule
label; it is satisfied structurally. This is the ceiling V-01 hits.

**V-02**: Retains R4 V-05's RULE 6 (C-14) which embeds C-16 enforcement without a C-16 label.
A scorer looking for "RULE N (C-16)" must infer it is inside RULE 6 (C-14). C-18 PARTIAL --
criterion IDs are present on some rules but C-16 has no labeled rule.

**V-03**: RULE 9 (C-17) adds a labeled rule for the completeness criterion itself. All 9
aspirational criteria now have labeled rules: RULE 1 (C-09), RULE 2 (C-11), RULE 3 (C-12),
RULE 4 (C-13), RULE 5 (C-10), RULE 6 (C-14), RULE 7 (C-15), RULE 8 (C-16), RULE 9 (C-17).
C-18 PASS for all 9 aspirational criteria. Strongest C-18 pass of the 5 variations.

**V-04**: Same RULE structure as V-01 (8 RULES, RULE 8 (C-16)). C-18 PASS for C-09/C-16. Same
ceiling as V-01: C-17 has no dedicated rule label. COMPLETENESS SEAL in COMPLIANCE AUDIT is the
differentiating mechanism, not C-18 coverage.

**V-05**: Full 9 RULES including RULE 9 (C-17). All 9 aspirational criteria labeled. Same as
V-03 on C-18. Strongest C-18 pass. COMPLIANCE AUDIT extends to 9 checkboxes including RULE 9
(C-17). Strongest C-19 pass (most explicit gate, largest checkpoint count).

---

## C-19 Analysis Per Variation

**V-01**: COMPLIANCE AUDIT with 8 checkboxes + "All 8 boxes checked = valid output. Any unchecked
box = invalid output; do not proceed." Explicit gate language present. C-19 PASS.

**V-02**: R4 V-05 COMPLIANCE AUDIT with 7 checkboxes + "All 7 boxes checked = valid output. Any
unchecked box = invalid output; do not proceed." Explicit gate language present. C-19 PASS.

**V-03**: COMPLIANCE AUDIT with 9 checkboxes including RULE 9 (C-17) checkbox. "All 9 boxes
checked = valid output. Any unchecked box = invalid output; do not proceed." C-19 PASS.

**V-04**: COMPLIANCE AUDIT with 8 checkboxes + COMPLETENESS SEAL + extended "do not proceed"
gate: "All 8 boxes checked and COMPLETENESS SEAL affirmed = valid output. Any unchecked box =
invalid output; do not proceed." Two-layer gate (checkboxes + seal). C-19 PASS -- strongest form
of gate with completeness affirmation embedded in the gate condition.

**V-05**: COMPLIANCE AUDIT with 9 checkboxes + COMPLETENESS SEAL + "All 9 boxes checked =
valid output. Any unchecked box = invalid output; do not proceed." Combines V-04's
COMPLETENESS SEAL with V-03's 9-checkbox coverage. Highest C-19 structural strength.

---

## Notes for Quest-Score

When scoring R5:

1. C-18 key question: Does RULE 6 (C-14) in V-02 satisfy C-18 for C-16? The C-16 criterion
   requires `->` enforcement. RULE 6 (C-14) states "The `->` separator is required." The
   criterion ID is C-14, not C-16. A scorer looking for C-16's labeled RULE cannot find RULE N
   (C-16) by inspection -- they must infer it is inside RULE 6 (C-14). Score V-02 C-18 as
   PARTIAL: criterion IDs present on most rules, C-16 uninferrable by inspection alone.

2. C-17 key question for V-01 and V-04: Both have RULE 8 (C-16) but no RULE 9 (C-17). Does
   C-17 require a self-referential rule, or does having all criteria covered by individually
   numbered rules satisfy C-17 without an explicit completeness declaration? Score as PASS if
   C-17 requires only that "all quality rules are in the numbered list" (which RULE 1-8 satisfies);
   score as a structural-advantage note if C-17 requires explicit completeness assertion.

3. C-19 comparison: V-04 has the COMPLETENESS SEAL embedded in the gate condition itself
   ("All 8 boxes checked and COMPLETENESS SEAL affirmed = valid output"). V-05 has the
   COMPLETENESS SEAL as a separate line plus a 9-checkbox gate. Test whether the gate-embedded
   seal (V-04) or the rule-declared + gate-verified seal (V-05) is scored as stronger C-19.
